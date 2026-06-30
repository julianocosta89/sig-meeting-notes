SIG: Entities SIG
Date: 2026-06-29
Duration: 24 minutes
============================================================

## Zoom Recording Transcript

**Josh Suereth** 01:38 Hey, folks.
I guess it's just you and me, Cra.
**krajo Krajcsovits** 01:43 Hey there.
No, it's
**Josh Suereth** 01:46 Oh, Peter just joined, hey.
**Petr Langr** 01:50 Hello!
**Josh Suereth** 01:52 How are we all doing?
**krajo Krajcsovits** 01:56 Too hot.
I'm in Europe. It's way too hot.
**Josh Suereth** 02:03 We're catching the tail end of that heat wave on my side of the US as well.
So it's supposed to be upwards of 100 Fahrenheit, which I forget what that is in Celsius.
like, 30…
**Petr Langr** 02:16 38.
**Josh Suereth** 02:18 Something like that.
But you guys don't believe in AC, right?
**Petr Langr** 02:27 That's not true.
**krajo Krajcsovits** 02:30 I have AC.
**Josh Suereth** 02:31 Okay.
**Petr Langr** 02:32 too.
**Josh Suereth** 02:34 I guess every hotel I stay at when I go to Europe.
Okay.
Anyways.
**Petr Langr** 02:45 I think… Good. Go ahead.
**Josh Suereth** 02:47 I was just gonna say the heat wave, man. Environmental activism.
you know, like, it just… it feels like we shouldn't be having these bad heat waves like this all the time. Go ahead, Peter.
**Petr Langr** 02:58 Yeah, well, I was just saying that, you know, we don't think about AIC that much because you get that sort of heat for a week or two and you kind of like just suffer through. And why would you buy a thing that you use for a week or three? That is like my perspective on that.
**Josh Suereth** 03:16 All right, that's fair.
We have, I know that usually when that happens, they issue, like, a notice to check on, like, you know, elderly loved ones and that sort of thing, because it can actually hit them pretty hard. So that would be… that would be my primary reason.
Good.
**Petr Langr** 03:32 Yes.
**Josh Suereth** 03:33 Yeah, sure.
**krajo Krajcsovits** 03:34 Yeah, we did install AC because recently in the summer, it has been like one or two months, like constant, very high heat.
And, like, I'm on the top floor, and I just cannot work, like… It's just not possible to work in that condition.
**Josh Suereth** 03:51 Is that fair?
I, I, I feel ya. We, There are people near me, like, my neighbors have a pool.
Which I think is the opposite of what you're saying, where… In Pittsburgh, we only have warm enough weather, like, for 2 months of pool usage, otherwise it's way too cold, right? So, that always blows me away.
**krajo Krajcsovits** 04:12 To be fair, I was, like, considering that you know, 2 months versus 12 months, so this one actually can heat as well. So if there's some… something wrong with, you know, gas, natural gas, then we can use it to… to heat.
**Josh Suereth** 04:25 It's a heat pump, gotcha, yeah.
**krajo Krajcsovits** 04:28 Not a heat pump, no, it's a regular AIC, but it can actually… heat. So… so the out… I'm on the fourth floor, so the outside unit is on my terrace.
So it's not a heat pump, but it still has, like, heating elements in it.
**Josh Suereth** 04:49 That's, that's fun. I didn't know you could do that. I'll have to look into that.
Granted, I have like a whole house thing where I am because, you know.
That's standard. And then, I got the one that had the most efficiency, because I hate paying for electricity.
I save all my electricity for AI now.
Alright, so… Let's see, I wanted to… I wanted to talk through some of the changes we have in the Java PR. I can… I can just show you guys, in case you're curious.
This is… we're trying to get entities implemented as an opt-in for Java.
And so basically, I need to update the things. But I'm going back and forth with Jack, one of the maintainers on Java. And I think a few key decisions happened here. So one is — this adds support for Marshall and OTLP, that's what this stuff is. The second is, This creates the environment resource provider. So we make a new resource provider called ENV.
Which will read the OTel entity's, environment property. Java normalizes environment properties and makes them all underscore dots, so that's why this works.
The thing is called ENV, and then I just have a, wrote a real simple hard-coded parser that is meant to be low dependency.
That will handle things, so it's, it's just a state-based.
string parser that will give you errors. So, it tracks segments of strings, and you can figure out if you have to decode percent signs and all that kind of crap. And then it has a quick state machine.
Anyway, so that, that's, like, part one of this. The other part is it actually adds entity to resource. So inside of resource, we had to do a few interesting bits.
First off, when you create resources, the way I'm doing this is kind of similar to similar to the way we think about resource on OTLP, you get all of the attributes built up between the raw attributes you send and the entities. So I take all of the attributes out of the entities.
And shove them into this big attributes array and that's the thing that comes over OTLP On the entities or references.
But it lets you interact with the actual data model, where you can get back your raw attributes. So we're actually recalculating this on the fly instead of storing it, because generally, the assumption is people aren't rebuilding entities that much.
And when they do, it's okay to pay this.
We changed the merge algorithm to match things.
So, I think I showed an example of using it… oh, right, one more example.
Where is that? End resource provider here. So the other thing we do is we're taking the existing resource detectors. So this is service resource detector.
For a service resource detector, I'm actually picking a specific OpenTelemetry schema to say, like, this is going to abide by the right schema. And then we get the entity type, and for a service and service instance.
And we have… we check a Boolean property, which is experiment entities enabled. Again, this is that same thing in Java where it's going to be, like, hotel.entities experimental enabled or something, but we're deciding there's a… An attribute that will opt you into getting entities.
And this is a way for us to modify, like, the, You know, stable portions of code, where there'll be this… if this flag is set, you get the unstable aspect of it. So that's a convention that we're discussing with the Java folks, whether they're comfortable with it, and that's one I want to kind of promote for entities.
But if you set that, if you set that attribute or environment variable property, then what happens is you get entities added. So instead of providing, this is, this is the default where you basically get a service name and a service instance ID. Instead of that, you would actually get the entity.
For service, and you get an entity for service instance.
with the schema URL appropriately defined for, you know, the schema that this thing is based on.
For context, today, you don't get schema URL effectively in Jav So this might be one of the first times you get, like, a schema URL that's usable without you having to manually configure it.
That's fun.
But that's that's the TLDR of this thing And then there would be changes that look exactly like this in the Java instrumentation library because most of their resource detection is not in Java core. It's in a separate repo.
That has all, like, all their instrumentation. So that's where they have, like, the stuff that makes HTTP spans, that makes metrics, that makes logs, all that kind of stuff is in a separate repo. They also have their resource detection over there.
You know, So we would basically do this same thing here and we would reuse this thing.
So that's what the prototype is looking like for… The Java SDK.
**krajo Krajcsovits** 10:20 Oh, can I have a question? Sorry.
**Josh Suereth** 10:22 Yeah, go ahead.
**krajo Krajcsovits** 10:23 So I'm… I'm… the one thing that I'm trying to decipher is that You said you're… like replacing the service name and service instance idea, I guess, with with the entity. That's fine.
But then… you do add them as resource attributes, right? And the entities just point into them, like as in the model.
Okay, okay, okay, so okay.
**Josh Suereth** 10:51 Yeah, so here, where we set it as the ID, That is, when we end up building.
Oh, so here we add the entity to the builder of the resource, and all of the identifying descriptive attributes go into the resource together.
**krajo Krajcsovits** 11:09 Oh, the builder is there. Okay, okay, that's what I mean, because… yeah, okay, I get that.
**Josh Suereth** 11:15 And this is… the reason it's, like, an extra thing here is we're doing shenanigans where we don't want to break compatibility or expose a experimental interface in a stable way. So inside of, like, Resource Builder.
If we look at add entity, Where are you?
Oh, man, I don't want the reflection stuff.
Oh.
Oh, there it is.
You see, this is not public.
And so you actually can't call it.
Unless you use that entity builder, which is public, but is denoted as experimental, and you shouldn't use this unless you're opting into experimental behavior.
**krajo Krajcsovits** 11:55 Mmh.
**Josh Suereth** 11:59 But so that's how Java gets around these things. In fact if you're if you're curious it's it's.
They've done this a few times, but the way that it works is it literally reflectively grabs the method, makes it so that it can access it from outside the package, and then calls it.
Don't you love Java?
Anyway, okay.
But yeah, I think that's all the important decisions from there. Does anyone… anyone have thoughts or concerns around that? Like, I… I really like… Personally, I can show this. I really like the, what it's gonna do to… these entity detectors, or resource detectors, right? So, I like the fact that, for existing resource detectors, we basically say there's an attribute If it's enabled, use entities, otherwise do the thing you did before.
Done, you know, no, no fuss.
I think it gives users full control, and it doesn't make us go through some crazy Enablement cycle effectively, you know, when we stabilize, if we've proven that this attribute, this, this set of things is safe, which I think will, that's what it's designed to be, we'll be able to take the flag and just default it to true and everything will be gravy.
**krajo Krajcsovits** 13:27 I mean, eventually you can just remove the flag, right? I mean, from the outside, you still get the same resource attributes, so…
**Josh Suereth** 13:34 Exactly.
**krajo Krajcsovits** 13:35 Okay.
**Josh Suereth** 13:37 Yeah, I think, I don't know what our full process will be. If it's like we take the flag, default it to false, then default it to true, then remove it. You know, that's generally how you do like experiment propagation or whatever. But I think that I like what this looks like. I think this will give us the broadest reach in terms of like reaching the hotel ecosystem.
And I wanted to check with Daniel, but I think this is probably what we're going to make the specification say.
Cool.
That is literally the only topic that I had that I was ready to talk about.
for today. Was there anything else folks wanted? I wanted to talk about host entity, but I don't think Without at least… Dimitri to talk about the collector side.
I think we might have to delay that one.
anything else, Bill, either of you want to talk through?
**krajo Krajcsovits** 14:35 No, I don't know if you, had time to take a look at the that design document that we did for metadata in in promo tools that includes entities.
I mean, it's just a headline there right now, and it is. I want to flesh it out more, but we wanted to get the design lookout, because it has, like, a really basic, huge question about the level of change to Prometheus regarding metadata? Like, do we actually want to make it, you know, a first-class citizen?
**Josh Suereth** 15:09 Okay.
**krajo Krajcsovits** 15:10 That opens up a huge list of use cases and And, you know.
Things that we can do, or we don't want to do this, and you know, then we have to think of something else, and maybe try to emulate entities in, like, labels or whatnot. Like, I hope not, but… Oh.
**Josh Suereth** 15:32 I think there's two things that you should think about with resource that I think are important.
For Prometheus. One is, Some of what entities will tell you is about state changes. So if you look at like entity relationships.
Those as time series, in my mind, make sense. Because if I'm defining, like, an alert on Prometheus, or I'm looking at a graph.
and I see, like, hey, you know, this pod suddenly, died here.
That's… that's, like, a signal, or, like, the… I just changed… I'm trying to think of examples in Kubernetes that are… where it'd be the exact same ID, but, you know, like, someone changed the configuration. So these would be more descriptive attributes, and you kind of see these in some of the entities people are sending to Notel, where someone changes the configuration and a config change leads to a crash. So, like.
pushing, like, hey, here's the current configuration, you know, object version for this Kate's object as, like, a time series.
But that, that would be kind of an independent time series in, like, it's, it's kind of its own metric, if you will, but it's like a state met.
**krajo Krajcsovits** 16:47 In this proposal, we propose to not do them as time series, but as first-class citizen, like metadata. And you can query it as a… On the side, like, you query the identifying attributes, like, you query your time series, and you can query the context, so to speak, so you get the descriptive stuff, or you can, on the fly, elevate it into a label, and in which case, you create a new series.
Then, so it gives you the flexibility, I think, to to treat it as part of the time series, or on the side as well.
I don't know which will be the… like, yeah, it's very hard to say what will be the… winning formula for… for end users, but… but the feedback we get all the time is, if you keep it in two time series and we have to join things, then that's complicated. So…
**Josh Suereth** 17:41 Yeah, yeah, I'm not suggesting that your general ML should be that, I'm just suggesting that, like, for some of these, if we were to look at some of the examples here, I don't know, like, if we take a look at deployment Some of these keys are interesting.
If you look at, like, a deployment name.
Right, that's something you want to join on.
100%. It's not gonna change, doesn't need to be a time series, relatively, because, it should be, something you consistently join across.
Annotation, though, or label, you know.
These might need to become… these are descriptive attributes. This is also a descriptive attribute, but these… I'm wondering if, like, you know, you want to see a time series of when they change. Like, hey, someone made a change to my config, and that led to a crash. It could be we don't use entities at all for this use case, but it was one of the open questions we had when we started of, like, tracking configuration changes.
As a time series.
So, this would not be, like, you know, It would be a different metric name, completely.
like, you would have a metric that you're tracking where I want to join deployment name because I want to filter that metric that I'm looking at by deployment name, but there would be, like, an independent metric.
that would somehow say, like, hey, this entity's configuration changed here, here, here, here, here, that I could line up on a time series. So if I see a crash, I could query this other metric, and it's not a join in the sense of, like, a metric join, it's just I'd overlay them on the same graph and say, here's where the changes happened to the entity to say.
Someone made a change, and immediately my CPU spiked to 100%. Probably that's the change that caused it, right?
**krajo Krajcsovits** 19:37 Okay.
Hmm.
I mean, we don't have any information on which ones of the descriptive attributes to make into a time series, so that's… I don't think that's, like, viable in itself.
But I think the… we do have a use case where we provide the context for a time series.
So for your CPU.
thing, the, The current use case is that you can hover over the line for the CPU load, and you can see when the context changed. So you would see it visually. It can be made more obvious as well.
So that's that's something of a That's the use case of this providing context.
For time series. That's UC, I think, use case 6.
Oh.
We have so many use cases there that I started to number them.
But again, it's, it's, like, I would love you to comment on somewhere in this doc, like, what you mean by saying that you want to see a separate time series, because Like, we need… Yep.
**Josh Suereth** 20:52 So to clarify, I don't think you need that initially.
I mean, that's, like, a use case I'm trying to understand how you're thinking about, for any…
**krajo Krajcsovits** 21:02 Well, okay, then, yeah, I don'.
**Josh Suereth** 21:04 Skip.
**krajo Krajcsovits** 21:04 Yeah, I don't want to… yeah, don't write, you know, create a new time series, but just write me the use case, what you want to achieve, and then we can figure out… If… if it already… I feel like it's already solved in one of these, but, like, I don't know, like, we should… We should formalize it and have it written somewhere, like.
As a comment, for example, in this doc, that… Oh.
you know, I want to achieve this and that, and then we can see which one solves it. If not, we'll figure it out.
**Josh Suereth** 21:37 Okay.
Why did you jump from 8 to 21? I'm just curious.
**krajo Krajcsovits** 21:47 It's two phases, so I wanted to leave myself some numbers to use for phase one, if you want to move them over.
It's, you know It doesn't really matter. With Gemini, you can just renumber things easily.
**Josh Suereth** 22:01 Yeah, yeah, that's cool, okay.
I see. So I need to… I need to read through this more. I looked at, your CEJs. I didn't actually read your, I didn't read your motivation.
Because, I just kind of focused on… The actual… I literally only read this.
Down.
The first time.
**krajo Krajcsovits** 22:24 Yeah, that's, that's, That section is about use cases where we already fleshed out more the details.
But there's a lot more use cases defined up.
Above that. And I think that's where you could… Oh.
you know, comment there. Also, I just added a new appendix where somebody asked, like, okay, but how do we exactly calculate the context? So there's an appendix And, It's, it's fully LLM-generated, by the way, because I think the principal's fault, so it could just do it.
**Josh Suereth** 23:05 Okay.
**krajo Krajcsovits** 23:07 Yeah, I expect this to have a lot of discussion around it, because you know, adding something new to Prometheus besides time series, and Labels, floats, and native histograms in the last 4 years.
It's… it's a… it's a very big change, and I'm not… like, I don't know if it will go through. I… I would like to have some kind of cons… consensus on the… at least direction by PromCon in October.
When we are together, and there's an in-person Dev Summit.
Developer Summit Oh.
But so yeah, so you have plenty of time to to comment there, because I I think it's going to be a slow process.
**Josh Suereth** 23:47 Yeah, yeah, I will absolutely make comments.
**krajo Krajcsovits** 23:51 Awesome.
**Josh Suereth** 23:53 Cool.
With that, I think we're out of agenda topics, so I think I'm gonna call it here. Thanks, everybody. Hope you all have a good week.
**krajo Krajcsovits** 24:02 Cheers. Bye.
