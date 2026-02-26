SIG: Semantic Convention Tooling
Date: 2026-02-25
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Alex Van Boxel 00:00:03 Right.
ariannavespri 00:00:27 Hello!
Alex Van Boxel 00:00:28 Hello!
I'm Alex, I'm new… well, not… I've been here once.
ariannavespri 00:00:36 Okay, my name is Ariana.
I'm not one of the core Weaver people, but, you know, started contributing recently, was a bit involved last year, too, but, like, definitely…
More of a constant involvement now, so…
Alex Van Boxel 00:00:55 As an end user, it's sometimes very hard to keep track of everything.
ariannavespri 00:01:03 Yes, yes, absolutely, absolutely.
Alex Van Boxel 00:01:05 You're… are you an end user, or a…
ariannavespri 00:01:09 Yes, in that, like, I work for a company called Oli Garden, and we, basically do,
Alex Van Boxel 00:01:18 That's not end… I'm not calling that end users.
ariannavespri 00:01:21 Yeah.
So…
Alex Van Boxel 00:01:25 I work for Calibra, and we don't have nothing to do with observability.
ariannavespri 00:01:31 Yes.
Alex Van Boxel 00:01:32 We use it?
ariannavespri 00:01:33 Yes.
since we do, like, meta-observability, so it's kind of a gray area there, when, it's like the classic, the classic question that when you register for KubeCon, you don't really know what to say, so…
Alex Van Boxel 00:01:49 But for me, for me, it's also meta, because we're a data governance company.
ariannavespri 00:01:53 Yeah.
Alex Van Boxel 00:01:54 And, well…
ariannavespri 00:01:57 Yeah. Why, why were we so early on OpenTelemetry? It fits…
Alex Van Boxel 00:02:02 It's metadata, it's… it's our business!
ariannavespri 00:02:05 Yes, yes.
Alex Van Boxel 00:02:11 I also took the effort, like, a few weeks ago to… so… to get a complete semantic conventions, plus our own, in our own data governance product.
ariannavespri 00:02:24 Wow, wow. You posted it in the Slack channel, right? Yes. Because that rings a bell. Okay. Wow. Well done.
Alex Van Boxel 00:02:33 I just wanted to make it work. A reason for it is because we… we are having…
API first on our APIs, but not so much on our…
Well, like, nobody, let's be honest. On metrics and locks and so on, it's like, everybody does what I do internally.
And that's sometimes problematic.
ariannavespri 00:02:59 Of course.
Alex Van Boxel 00:03:00 We would switch it around.
ariannavespri 00:03:02 Yes, that's absolutely right.
Alex Van Boxel 00:03:04 Yeah.
neil yashinsky 00:03:10 Hi there, good day.
ariannavespri 00:03:11 Hello, Neil.
neil yashinsky 00:03:12 How are you today?
ariannavespri 00:03:14 Great, how about yourself?
neil yashinsky 00:03:16 Very good. It's Arianne, is that right?
ariannavespri 00:03:19 Ariana?
neil yashinsky 00:03:20 Oh, Ariana, pardon me, pardon me. And Alex, is it Alex, right?
Alex Van Boxel 00:03:25 Alex. Alex. As long as it starts with an A and L. Very good.
It's all fine.
neil yashinsky 00:03:31 No, you know, I appreciate you saying that, because, let's just say my ears and mouth are configured a little differently, I really… it's important to be… I mean, I appreciate people who are like, oh, my name is hard. With a last name like Yashinsky, I never, you know, take too many exceptions, but that said, I have, if you will, like, a special interest in…
pronouncing people's names properly despite it being very hard to be, or maybe because of it. So, Ariane that. And Alex, please, I welcome your…
patient guidance, if I, if I, as I seek to try and do it right, because it's like, oh, you know, it's just like I've heard our names are our favorite words, so, it's worth learning how to do it right, I guess.
ariannavespri 00:04:17 That's… that's really… that's really sweet of yours. Thank you.
neil yashinsky 00:04:20 Thanks. I try, yeah. I try.
I've been…
taking on, the moniker of innkeeper, which, of course we've all heard of innkeeper in the classical sense, right? But, innkeeper now as in the…
whatever it is, antonym, the opposite of a gatekeeper in, like, you know, culture and society and what have you. There's gatekeepers, and, you know, sometimes there's good dates to be kept or whatever, but oftentimes it's really, counterproductive.
you know, for people's own selfish interest that they keep the gates, and, in a kind of a Dungeons & Dragons.
context. The innkeeper really does the opposite, welcomes people on the road, or travelers, et cetera, et cetera, helps them find magical items, all that good stuff. So yeah, I've been trying to,
Personify innkeeping.
So, that's my,
Glad to see it's, seems like it's found a receptive audience here, so that's… that's great. Hello, Ludmila, how are you today?
Liudmila Molkova 00:05:25 Hi, Neil, hi everybody, I'm good, how are you?
neil yashinsky 00:05:28 Very good, thanks.
Liudmila Molkova 00:05:29 I'm glad you made it. I… I don't see this call on the… on the calendar.
Not sure how it happened. But we are on, we should be on.
ariannavespri 00:05:40 Yes.
neil yashinsky 00:05:42 Oh, it's so fun. Like, if it's not directly on some sort of calendar, and I didn't get 3 reminders already in the day, like, my chances of showing up for a meeting that I'm supposed to be at without any of that stuff is essentially zero.
So, yeah, I definitely know the feeling.
Liudmila Molkova 00:05:59 Yeah, okay.
I just want to…
What?
Okay.
Let me see if somebody else is coming…
neil yashinsky 00:06:26 I think, we got our template a little bit,
I'm just gonna throw this up here.
Liudmila Molkova 00:06:34 Okay, Josh is saying that he will be late.
Okay.
So… since we have Alex here…
Should we talk about events and body?
Yeah, thanks for adding it to the agenda, Alex.
Alex Van Boxel 00:07:08 Yeah, yeah, so it's like, it's like, I cleared my agenda.
Because you asked, it's like, okay, maybe I should jump… jump on this call.
Liudmila Molkova 00:07:20 I really appreciate you coming.
Alex Van Boxel 00:07:23 So… I can maybe… maybe give some context on why we're…
kind of here, we have a long history of… with OpenTelemetry. We're early adopters since 2020, with traces. We were already using logs when nobody had it, so we have our own, actually, exported to Datadoc, to Google Cloud.
We're still using them, because they're doing their job.
We… very early on, we started using our… what we call, Calibra Structured Loch Events.
what that means for us. Internally, it is, we…
everybody needs to have JSON logs, and when there's an event name, we treat it specially. When there's an event name for us, then it means we're routing it to our data office, so we have a BigQuery table with all our events. Analysts do their work on that. At the same time, it gets routed to…
to actually multiple lock providers for specific use cases, even for Elastic, because we also are actually abusing events for having a vehicle to do fine-grained measurements.
For example, metrics and so on. So, when a metric, what is already an aggregate, is not fine-grained enough.
With them in Elastic, and people can build dashboards to them, it's kind of…
It's very useful. People are very fandom of that issue.
The biggest problem is a typical big data problem, is that there is still no contracts, of our colibra structured log events.
And we are a data governance company, we have very data… good data governance for our APIs. We now want to actually introduce data governance… well, govern… let's just call it governance, on our telemetry. And then, so that's why I put, like, a few weeks ago, I put our, the semantic conventions, plus the
attributes that we already have in our data governance product, and I said, like, wow, that works, and then I could see, oh, the browser event, it had, like, a nice
I found it completely, the body out, and it has, like, events, it had, like, then code values, so you could really see it as documentation, you could look at it, and it, like, other events totally go on attributes. For us, I was starting to write, okay, it makes sense to do both.
Because, I said it, like, in Slack.
attributes, when we upgrade things for our own Calibra, so we use our own namespace calibra. And then the domain, and then, like, something specific. Before going in there, we want to do way more scrutiny and looking at that attribute to bring value.
But we do not want to be the blocking factor either, right? So, this is high value, it means, like, you will have that across different events, because… because we see a lot of users. I think, like, we have, like, hundreds of events in our company.
grown organically due to all those usage, but, like, their supports do use those correlation, and when
And people do it, like, in tickets, but mistakes are made, and support the teams, they use those correlation across events, because we… we have an internal system with jobs, and now we need to see that job triggered this and this, and this, and this, and that's…
So that's why there, for us, weigh more value, but, like, we want to have people as well, the availability to kind of…
Be flexible in that body, right?
Liudmila Molkova 00:11:23 I see. So you use attributes for something meaningful, structured, and documented.
And body for… all the crap.
Alex Van Boxel 00:11:34 Well, yeah, but I don't want to… so… so…
It is a bit true, but, like, we want to get… it's kind of a middle ground, right? Now we have nothing. It's like…
Okay! And I want to have it at least documented. Having it documented?
And having people to provide a schema.
is a help, and we will make it… if you change that.
it's your own problem, but at least we know what the meanings are. But if you say, we're going to promote it to an attribute, that means, like, okay, this has domain knowledge, or… so it has… it's… I don't want to call it crap, let's say it like…
Liudmila Molkova 00:12:19 Yeah, I'm sorry.
neil yashinsky 00:12:22 It's structured. It's unstructured.
Liudmila Molkova 00:12:23 It's structured.
Alex Van Boxel 00:12:24 No, it's, it's still.
neil yashinsky 00:12:25 The body.
Alex Van Boxel 00:12:26 We, we…
neil yashinsky 00:12:26 In the body, I mean. In the body, it's unstructured, right? It could be the word crap or something else like it.
Alex Van Boxel 00:12:33 No, but, like, no, we want to say this… we still want to say, okay, you have maybe a measurement duration, you want to have it documented, it's in milliseconds. It is an integer, but the meaning is in milliseconds or something, we want to have documented. We want to have documentation on this. And we will drop things that are not in the schema.
So…
Liudmila Molkova 00:12:56 Yeah.
Alex Van Boxel 00:12:57 So that's the thing. We have dozens of processors. We do, for example, a lot of… so,
We have already kind of our Calibra C4 model, for example, for our architecture. We have a tenant environment identifier, a group identifier. Those are already attributes, and we actually enrich
Our streams in our backbone.
And those we already have, like, what I was saying, like, those are very valuable, but, like, having the meaning of this field is still valuable. Is it a millisecond? Are there nanoseconds? Are this…
Liudmila Molkova 00:13:41 I…
let me share how we would design it inside. I'm not saying you should design it differently, but we…
Would support it in a different way.
So… We are not going to use Buddy for semantic conventions. The tooling will support
Semantic conventions will not use it. If we want to say, okay, this attribute is important.
We are sure, please never break it, we mark it stable.
Alex Van Boxel 00:14:14 Damn.
Liudmila Molkova 00:14:15 if we… Don't care. If it's supposed to evolve, it has development stability.
And in the sense, through the schema, you let your telemetry consumers know that
This thing is supposed to change.
The other… there could be other approaches. You could say, okay, this is an attribute.
And there's a part thing called annotation. It's a free-form text structured under the attribute.
And you can use this annotation during validation in life check. You can say, okay, this is actually a thing that I don't really.
Alex Van Boxel 00:14:55 care about.
Liudmila Molkova 00:14:56 Why, we're… Would rather do this, because, when people query.
we don't want them to think, okay, should I query body, or should I query attributes? Where the thing is? How do I think about it? What is the reason I put it here or there?
And it's kind of much easier to say, okay, everything is an attribute. Bodies for maybe the display text, or whatever. If it's a custom thing, we don't…
Alex Van Boxel 00:15:28 object.
Yeah.
But, also in the Slack, it's fine that you do that for… Or,
for semantic conventions of OpenTelemetry.
But we're not gonna do that.
In our company. Because… and… and so, if you're saying the tooling supports… still supports… because now it does, so now it supports body, because I was pleasantly surprised that we had, like, both, because, like, okay, perfect, that's what I need.
And I can accept that that's not in V2 now, but, like…
I can try to get some stuff, at least that we… that you supported, and that we can template it.
Because if I lose that…
because we… I was, like, this week, somebody was… I was like, okay, I'm gonna provide in V1 spec our first event.
And we will probably… we will for sure will use a mix of body and attributes.
For sure, because we're not gonna ask each and everybody how to have, like, colibra.pa, colibra.for everything that they want to do.
Because that's… that's just not undoable.
People will not look, like, do that.
So…
Liudmila Molkova 00:16:57 Yeah, in order to make it happen in V2, so, like, why we didn't move it there? Can I share?
Alex Van Boxel 00:17:03 Yep.
Liudmila Molkova 00:17:04 Also, there is something in the chat…
So, how it looks… you know how it looks today, but for others,
We have a good example,
Somewhere here was an example of the body, and it shows why it's not possible.
Oh, here we go.
Oh… here, yeah.
So we tried to use, body for… oh, shoot.
We tried to use Buddy for messages, and… We… failed?
miserably.
I'm sorry, I'm completely lost now.
Alex Van Boxel 00:18:42 key.
What do you mean by failed? Is it…
Liudmila Molkova 00:18:59 I'm trying to show you, you miss, like, I cannot talk and browse at the same time.
events.
Alright, let's… It is.
around.
Let's pretend it was around this time.
And…
They're perfect.
Yay, here we go, finally.
Okay, so let's say I have… I want to record, something.
This is the message in the chat history from, from AI.
This is how I declare my type.
So this is the assistant message, it has…
some properties, and then finally it has some nested types, right? This is a type definition.
Alex Van Boxel 00:20:35 Yeah. And…
Liudmila Molkova 00:20:37 It's deeply nested. There is more here.
This…
is a type system, but without a type system. You have to repeat your type system all over again.
Every time.
It is impossible to write, so this file… It's very, very long.
It's hard to maintain.
consistency.
Alex Van Boxel 00:21:05 It also uses a lot of nesting, right?
Liudmila Molkova 00:21:11 Intentionally.
So, what we… So if you compare all this, I will use word crap again, I'm sorry.
If you compare all this crap with… and I wrote it, so I can… I can blame myself.
where's… this.
And it grew much bigger since we, since we defined these events. The Python code is much nicer, it's much easier to read, it's maintainable, we can, I don't know, validate it, we can,
keep things dry, right? In the SAML body definitions, they cannot be dry. You have to repeat yourself all over again.
So the way forward for this thing.
Would be to define type system.
And there is an issue about it.
Josh suggested something. We could say, okay, there is a thing called
I don't know what chat history message.
And you can describe it, and then you can reuse this type
In different places, in the body.
If we don't solve this problem, we would not be able to bring typed body back.
Because, we've been there, we've done that, we didn't like it. It's not possible to maintain it well.
Alex Van Boxel 00:23:00 Does this mean you… Okay, you're talking about reusability?
So, what about the following example? You have… Two messages?
They have… those… sorry, two events. Those two events…
Share a different type. Share the same type?
But I have, for the rest, uniqueness.
Liudmila Molkova 00:23:31 Nope.
Alex Van Boxel 00:23:32 With this type system, would you… define… or… 3 different types.
Two times that reuse one.
Other type, as kind of an embedded one.
Or define one type that they reuse in each of those body… itself.
So.
Liudmila Molkova 00:24:01 Yeah.
Alex Van Boxel 00:24:02 I mean, do you… is it still possible to… if you define a type system where you can reuse blocks, is it still possible to inline the body?
Type…
Or do we need to provide every type outside of the body, and then just refer… okay, my body is of this type.
Liudmila Molkova 00:24:27 I don't know, I think it's, it's details, it could be either.
Or…
Alex Van Boxel 00:24:33 Yep.
Now you're showing me this, is that an idea that is floating around?
But I have the impression that it's still, like, okay, we're not sure that we're not even gonna do this?
Liudmila Molkova 00:24:50 It's a question of, how badly do we need it? We…
Currently, the SIG, the Weaver SIG, is focused on the
other parts of modernization, the V2, and we want to publish the schema, we want to version it better, we want to decentralize conventions, we'll, split, maybe move some conventions away.
Where we will ask, let's say, collector or some repositories to define their own.
This is our main focus.
the… this… Type definitions that are the same across attributes and body, there is no difference.
Alex Van Boxel 00:25:35 It's true.
Liudmila Molkova 00:25:36 It would be a…
Alex Van Boxel 00:25:36 You could… you could reuse this, because until now, most of the types that are defined in attributes are pretty… do we have complex ones?
We do.
Liudmila Molkova 00:25:49 We do know. It's a recent change.
And we just call them any.
There.
Alex Van Boxel 00:25:57 Okay, any… that means there's no definite… currently, there is… it's just any, you can… it's not really defined, but with the type system, it would be possible to even provide that typing to attributes, because on itself, you could envision as body as kind of a special
typed it.
Liudmila Molkova 00:26:16 It's just the same.
Alex Van Boxel 00:26:18 It's the same.
Liudmila Molkova 00:26:18 From the tooling perspective, we don't care. But this… the typed attributes is a blocker for GenAI Sig. We've been avoiding it so far. I've shown you we've used JSON schema for this.
Unless… it becomes a real blocker. I don't… I don't envision…
somebody from this SIG spending time on… on making bodies work in V2.
I might be wrong, but it's just not… not on the… on the horizon, not a burning need for… for anybody, that I'm aware of.
Alex Van Boxel 00:26:57 Is there a way to contribute on this?
Liudmila Molkova 00:27:02 Yeah.
That would be wonderful.
Of course. And… It's… The matter of… Probably refactoring this existing Bing.
And making it, I've lost it again.
And inventing some type system around it.
It's… not the small… task, but…
We're pretty much there, so we can use bits and pieces of what we've had so far here.
Alex Van Boxel 00:27:46 Okay.
I'll… I'll have a look at it. It's like, Rust is not my…
Aside from having Rust installed on my computer.
Makes it harder, but yeah.
I can see.
Liudmila Molkova 00:28:04 God is pretty good.
neil yashinsky 00:28:06 Sorry? Sorry? I'm sorry, I just said you're halfway there. You've got it installed! You're halfway there.
Liudmila Molkova 00:28:14 If you also have Claude, then…
Alex Van Boxel 00:28:18 We have.
Liudmila Molkova 00:28:19 Awesome. They, they, they work nicely together.
Alex Van Boxel 00:28:23 Well, actually, a good question,
I don't know what, for our company internally, that's not a problem, but, in contributing to open source, this is a problem.
Using.
plot.
Liudmila Molkova 00:28:37 you are responsible for the contributions you make. You can disclose that you use AI, we encourage you to disclose that you use AI, but we don't…
Really?
Alex Van Boxel 00:28:49 policy around it, that's good to know.
Liudmila Molkova 00:28:51 there is a policy, but essentially, you're a responsible adult, and you use AI responsibly, and if you send slob.
We use karma, right? You can close it.
Alex Van Boxel 00:29:04 I know, I'm not a stranger to contributing to open source, so I've… I'm doing that into the collector, so…
Liudmila Molkova 00:29:14 Yeah, I know.
Alex Van Boxel 00:29:16 Thanks.
Liudmila Molkova 00:29:17 Thank you. So… What kind of context
You would like me to share, or you're fine with what we've talked?
Alex Van Boxel 00:29:30 I think I know enough. I will probably search for those pointers, and maybe I'll contact you to have, like, exact pointers to do that, because I have to dive into this.
And see, what I can, can do.
But I'm motivated to get this decision, because now we're on V1, and we will start to find stuff in V1, and we'll see what we learn.
But because we're starting on VR1, V1 goes away, then this will be a problem if we can't define some of those types in there, so…
So, I'm motivated to get,
And I can understand that it's not a priority for you guys, but I wanted to… that's what I wanted to hear, is like, are you against it? And the answer is no, it's only time constraint, and that's, that's good to know for me.
Liudmila Molkova 00:30:30 Yeah,
That would be wonderful. I would be very excited, and I can partner with you on this, but I probably won't be able to spend a lot of time.
Alex Van Boxel 00:30:41 No, no, no, but, like, that's… that's, that's fun.
Thanks, thank you.
Liudmila Molkova 00:30:46 Thanks!
Did you… not nuts versus description?
Alex Van Boxel 00:30:52 Yeah, I put it on Slack, I don't know, it's like, it's… I don't know if it's… it's worth discussing here, and maybe it's like, because this is tooling, actually.
What I've noticed, and I don't want to take all of the time, because… unless somebody…
Does somebody else have some… some issue? Otherwise, I can go into this. So, notes versus descriptions. So, I'm… because I was doing all the…
getting everything in our data governance system, we also have things like briefs or short descriptions, descriptions and notes, and when I found out everything, it was like, you know, like, this note very looks like an implementation detail, huh, this note as well. I look… I see a lot of notes being implementation details.
And the briefs Or… short?
and good, but it feels that, like, there's something in between. It's like, okay, you have this…
A brief is very good, and I always kind of think about this as a tooltip. If you hover over something, it's like, yeah, this is a brief, this is this attribute, but sometimes you want to have real semantic meaning.
And I think, like, a lot of nodes that are in there, in here, R…
this is how you implement, this is what you have to look at as you implement. And with more and more of the AI stuff, starting to use our data governance product for doing AI stuff, extracting stuff, so you want to have, like, way more context. So I was wondering, would it be interesting to actually introduce
a description separate from a note.
Because I think, like, both are valuable. I think an implementation… a note for having implementation detail for the implementer.
of that attribute or that I think is valuable.
But having something in between the brief description of this is this.
is interesting, because, I think it was Jeremy that was pointing, it's like, yes, we have, like, a lot of…
Descriptions in the docs as well, so… it feels like…
We still have, like, descriptions that are not in the semantic conventions.
Liudmila Molkova 00:33:29 So let me see if I understand the briefest, we kind of all agree, very… something very short.
then the description is the extended version of the brief.
Alex Van Boxel 00:33:42 But that doesn't exist now, that doesn't exist now.
Liudmila Molkova 00:33:45 And then notice something else, that if you are implementing the spec, then it's for you with some very deeply technical caveats.
Alex Van Boxel 00:33:56 Yeah, that's what I noticed, that a lot of… I'm not saying that it's, like, across the border, like…
If you look, by the way, in the schema of V2, and of, like, for example, for…
Spam? What is saying? Note?
it really looks… it says, like, this is how you would create your span name. That's actually the description in the schema, so that's kind of… that's really stated out in the schema.
Okay, notice how you implement it.
Liudmila Molkova 00:34:31 I kind of see some value, maybe big value, in separating the
Definition of the thing from…
notes on implementation. Like, this is targeted for people who use telemetry, this is targeted for people who write telemetry.
I… It's…
to be fair, I… it would be very hard for… to… to actually explain it, and…
I feel we would need to do a lot of effort to maintain it, but I see the value.
Alex Van Boxel 00:35:19 Okay, if you see the value, what would be the best approach? Make an OTAP about this?
Liudmila Molkova 00:35:25 Oh, please don't, don't. There is, just send a proposal to the Weaver,
what do we do in Vivers? Should it… do we have a… we have some RFC system, but for something like this, we probably… it's just an issue, is it?
Josh Suereth 00:35:40 Well, you can make an issue. We also have, if you look under docs,
there's a… there's a set of proposals. This is how we were doing things early. So there's specs, I think?
At the… Is that the one?
Yes. So each of these is a proposal around how we want to deal with certain things. So when we added multi-registry, that's like,
Oh.
beef.
So, in specs, yeah, there's two directories in there. One is multi-registry, which is the, like, the multi-registry proposal, how we wanted to handle, like, dependency tracking and all that kind of stuff, and where we're going for that.
Again, this is the design, not necessarily what we've implemented, and you can see where we want to go there. The default templates one, that's the one that I'm working on now.
Sort of. I'm kind of taking a little pause to finish multi-registry. That's… that's right above that in specs. That's all. That's the other proposal, but this was… this was the one we did recently, to try to talk about, like.
why we want to start moving these packages, make it easy to consume, and why we need to have GitHub,
sorry, get, references, and try to resolve by SHA, and that kind of thing. So, yeah, I would recommend, if you want, either discussing the issue there. Is this… sorry, I'm late, is this talking about the type system thing, where you can add a type?
Alex Van Boxel 00:37:04 Oh, no, no, it's too late. Okay, okay.
Liudmila Molkova 00:37:07 We already talked about it, but for the type system, it would rather be a proposal.
Because it's…
Josh Suereth 00:37:15 Yes, yes. If you're able to make code that, makes it work, too, I'm fine skipping a little bit on that one, because I think we had a lot of discussion previously. However, like, the,
The reality here is we're doing a lot of changes to the core engine, so you're… just expect churn. That's why I think making a proposal would be better, so we know when we are coding not to break what you're doing. Does that make sense?
You know how sometimes in a codebase, everybody is touching the same file, and that's a bad thing, and you don't want to do that?
Alex Van Boxel 00:37:51 I read base often, you know, so…
Josh Suereth 00:37:54 Oh, that's fine. If you're willing to ride it out, like, I… no, no problems, I just, I, like.
Alex Van Boxel 00:38:00 So for the… I think, like, the notes and discussion, I think it's very fine to have a spec, because you can have the discussion. For the type system.
I already kind of know that I need to do it anyway, because there's no time, and that's fine. No time is a good answer, then, like, no, that's against our
Or principle, so I can maybe spend the time there.
But then it's best just to kind of test it out, right? And…
And that's how you… you test it out, and that's fine. Rebasing often
It's the collector as well. He pays often. That's fine.
I'll try it… I'll try it in code for the type system.
Pocketad, and then we can have a discussion. It's like, hey, it works like this, Are we agreeing?
Liudmila Molkova 00:39:01 Woo!
Anything else on this? Should we talk about multi-registry stuff?
Josh Suereth 00:39:10 Yeah, we have… we have two major efforts going on right now. I think multi-registry and the packaging work.
all for federated CENCOM.
if you want, I tried to update the project board with, like, I want to make sure we have things that we're considering for next release, and I'd like to kind of sort out what work
Like, next release is only in 2 or 3 weeks.
Theoretically. So I kind of wanted to sort out, like, what we think we're gonna realistically have in the next release that we can start pushing on further. So, like, Ludmila, I think we want to get your change in.
I think I want to get the GitHub reference change in. Actually, I don't think Lawrence is here, is he?
There's a PR I added, for next release, the Implement Git Ref spec. I really, really want to get this in, and it's marked by… it's blocked by Lawrence, so I was just gonna run it by everybody. I think all of his comments were addressed, and he just disappeared for a little bit, so if nobody has any concerns, I'd like to,
Un-, like, remove his review and merge this.
Jeremy Blythe 00:40:22 Yeah, agree.
Josh Suereth 00:40:25 Okay.
Cool.
Liudmila Molkova 00:40:35 So maybe you will…
Josh Suereth 00:40:37 Yeah, go ahead.
Liudmila Molkova 00:40:37 I don't… I don't know what happened.
Here, you've… okay, you approved, thanks.
Josh Suereth 00:40:43 Yes, yes. It should be in… did I not move that one into the next release one?
Excuse me.
Liudmila Molkova 00:40:49 What's in the next release?
Josh Suereth 00:40:51 It should be next release, right? Yeah.
Liudmila Molkova 00:40:56 Okay, yeah, cool. So then there are some final things we need to do here, and it will be…
Done?
There are a couple… More?
Josh Suereth 00:41:11 So, the two I was thinking about was, deprecating Weaver Registry Resolve.
and creating a Weaver Registry package. So when we deprecate it, basically, we would say, hey, by the way, did you know that Weaver Registry Generate does everything you need from Resolve now? Just, here's the command for Weaver Registry
generate, that does the same thing Resolve did.
And then, make the new Weaver Registry package, which does the manifest and the, result schema.
Liudmila Molkova 00:41:45 Yeah, and we didn't start on this. I think I wanted to work on this, but didn't start.
Josh Suereth 00:41:52 Yeah, well, this is one of those things where we're all touching the same files. I… I purposely didn't start on that, because I think that that is blocked by your current PR.
And once your current PR's through, I think then we can… we can actually do that one.
Liudmila Molkova 00:42:08 Okay, so I'll try to get it cleaned up, and we should be able to merge it soon.
Josh Suereth 00:42:14 Yep.
Okay.
But we… do we agree… we agree those are definitely… we want that for next release.
Jeremy Blythe 00:42:22 Yeah, I think so.
Josh Suereth 00:42:25 Okay.
Jeremy Blythe 00:42:26 I think it's a big deal to be able to resolve against a published a published registry.
And it will actually clean up a lot of our internal code, where we're going at the moment, reaching out to the SEMConf
They're making internet calls out to things. We can, in effect, vendor in are published.
Josh Suereth 00:42:47 Yeah.
Jeremy Blythe 00:42:48 Right.
Josh Suereth 00:42:50 Yeah.
Okay. Replace version and definition schema file format, you're doing that.
Weaver Registry Diff Template Extension Weirdness. I think I saw your PR today, Jeremy, on this, and
I like it, but did you see my comments?
Jeremy Blythe 00:43:11 Yes. Did you see my comment back?
Josh Suereth 00:43:13 No, no, I was stuck in meetings, sorry.
Jeremy Blythe 00:43:17 It actually only covers those formats, according to the… Documentation.
So, my… what I… what I did was…
First of all, my first commit on this, I switched off the auto-escaping for everything. And I thought, well, maybe if you're doing HTML, I can see it might be valid.
So I wrote that code to enable it.
Food.
the HTML, HTM XML stuff.
But for the others, it feels like if you're doing something like that.
I don't know. These implicit things, they just… I think they're just foot guns.
Josh Suereth 00:43:59 Yeah, well, that's… that's why I was thinking, like, while you're in there, if we just make it a configuration setting.
then… If we did it wrong, there's still a chance that, that configuration setting can save us later.
Jeremy Blythe 00:44:14 But could we…
flip the switch back. So, by default, it's a braking change. By default, the escaping is off.
Josh Suereth 00:44:24 I… I'm actually fine with that, because I think by default, the escaping has caused no end of trouble for everyone.
Jeremy Blythe 00:44:31 It's just really confusing, because, like, you'll make a… you'll make a…
template file that's, like.markdown, dot, and everything's lovely, and then you'd make a .yaml dot, and it's like, well, this is confusing, which is why this ticket came about.
But if you don't name the template .yaml, but then you save the file as .yaml, you end up with… which is exactly what is in the semconf project now.
Oh, I see. The template is just called .j2, but it makes a file called .yaml.
It's just like… it's just… that's why it just seems like a footgun.
Liudmila Molkova 00:45:04 I think I used it as a… as a workaround for this issue at some point.
Jeremy Blythe 00:45:10 Yeah, it's actually what is live in the main in SEMCOMP.
In internal tools, scripts, whatever, the diff to make the YAML.
it writes a YAML file, but without the template.
with the letters Y-A-M-L in them.
Liudmila Molkova 00:45:28 Oh, and you're discussing that… that… how much we can rely on the file name, but let's not!
Jeremy Blythe 00:45:34 Like the file… like, it's a… that's what I'm saying, it's a footgun.
you weren't… you're like, oh, I just happened to put YAML in the template name, even though I'm saving the file with a real… with a different name.
Josh Suereth 00:45:45 Yeah, I mean, I'm… I'm a fan of us, like, let's… let's… let's cut…
stem the bleeding. I think, like, I want to make your braking change, but I think we should have… the only thing I'm suggesting is let's make a flag, so somebody complains they can use the flag to control the behavior. I don't know where that flag is, I don't know if it's in Weaver YAML,
on the template itself, that's kind of what I was thinking, is just add a new field in Weaver Config, where I can say.
what this is, and then you grab it right there, because I think you have access to the template right when you're doing this.
Jeremy Blythe 00:46:17 Yeah, you have to… it's…
It's when you're creating the template engine, so it probably has to be in the Weaver YAML, because it has to happen just before you create the engine. You have to set how you want the auto-escaping to be done.
Josh Suereth 00:46:30 Oath.
God, okay, never mind then. Never mind. If what I'm suggesting is too hard, like, let's just…
Jeremy Blythe 00:46:36 I'll have a look, have a look. Okay.
Josh Suereth 00:46:38 Yeah, if it's easy to have a config where people can control it, that would be ideal to me, because I… my fear is…
Well, we could do one of two things. We could make this breaking change, get it in Weaver, and then try it out before we cut a release, on, like, the Java instrumentation, Python Go, see if it breaks them.
If they were relying on this behavior implicitly somehow, we didn't realize it.
Jeremy Blythe 00:47:03 Something weird, but sure.
Josh Suereth 00:47:04 Yes.
I don't… I don't really think that would happen. But the second would be, let's just make it configurable, and then, we can come back to it and remove the configuration option if we think it's not used.
Jeremy Blythe 00:47:16 Right.
Josh Suereth 00:47:16 Yeah. Yeah, okay, I'll look at that.
Cool.
I… I'd like, as a principal, if we make a breaking change, having a…
Either a config option that lets you go back to the previous behavior, or, like, us,
knowing that it was a bug, you know what I mean? Where, like, nobody wanted that behavior, and it's possible that this is the latter, and then that's fine.
Jeremy Blythe 00:47:41 The thing is that you… Sure, and overall, I get it. What I did put in the changelog is…
You can still use the escaping
Filters, or whatever they're called. Functions and filters.
If you really want to have, you know, you can put to JSON.
Josh Suereth 00:48:01 Oh, got it, yeah, yeah, yeah.
Jeremy Blythe 00:48:03 You just have to explicitly say, this piece of thing that I'm embedding
I want it to be escaped.
Josh Suereth 00:48:10 Yes.
Jeremy Blythe 00:48:11 And so you're being very explicit about it. Like, whereas you're relying on
Otherwise, you're relying on Mini Ginger going…
Oh, I escape everything that's inserted.
Josh Suereth 00:48:21 Yep.
Okay.
Cool.
Jeremy Blythe 00:48:26 But yeah, I'll see if there's a way to just enable it.
from the Weaver YAML, probably, is the right thing.
Josh Suereth 00:48:39 Awesome. What, what, let's move on, then. What's next for release? Oh, Neil, go ahead.
neil yashinsky 00:48:45 Thanks, Josh. Just a real quick question, I know we talked, I think it was 2 weeks ago, about me helping out with an issue, but I couldn't be assigned yet, and so I couldn't… I kind of lost it in the notes or whatnot. Unless it's already been fixed, which obviously somebody just got to it, great. But…
Josh Suereth 00:49:02 I commented you on the… let me… I'll start looking for it here. Okay. It was… it's in… I think it's in To Consider for Next Release, or it's in, the V2 stuff. I'll take a look.
neil yashinsky 00:49:14 Great. Whenever you have a chance, that'd be awesome. Thank you.
Josh Suereth 00:49:19 Oh, can we assign you issues now? Are you in the org?
neil yashinsky 00:49:24 I don't think so. It's one of those things I'm not sure if I would know… I probably would know if I was, but I don't know if I wasn't.
Liudmila Molkova 00:49:33 Do you have any, paper trail of your contributions to open telemetry, like discussions or PRs? If you do, can you apply for the membership? I will support you, Neil.
neil yashinsky 00:49:46 Oh, great, yes, I do have, like, discussion notes, or what have you, for sure. Okay, I'll do a little into that process, and I'll send you some examples of when I have a moment. Thanks.
Liudmila Molkova 00:49:58 Instead of sending me examples, just do… go to the community repo, and then do organizational membership request.
neil yashinsky 00:50:12 Perfect.
Liudmila Molkova 00:50:13 this. I'll leave it in the notes.
neil yashinsky 00:50:15 Amazing.
Thanks a bunch.
Liudmila Molkova 00:50:21 worse.
Okay, back to the project board. So we are…
So, Josh, what you're saying, you will…
Do this too, or one of them?
Josh Suereth 00:50:42 I… I think you and I might want to split up which one of us does which. So if you want, like, let's… because we're touching so much of the same code at the same time, if you want to do it, throw your… throw your head on it, or your… sorry, assign it to yourself, and then your face will show up, or whatever, your icon.
It sounded terrible when I said, throw your head on it. Anyway,
Yeah, if you want to sign it to yourself, and I'll use that for that, because I think the other, the other bit, we had Reaver Registry Package, we had Reaver Resolve. The other thing that I can work on now, that, you know, once your PR is through, is I was going to go change, the definition schema to allow refinements.
Liudmila Molkova 00:51:26 Yeah.
Josh Suereth 00:51:27 that's gonna be a much bigger change, and there's a lot of craziness in that, and I have a, like, a branch that I need to go do a bunch of resolution on. So yeah, if you want to do this one, I can do the refinement one, we could split it that way, or vice versa, like, I don't care.
Liudmila Molkova 00:51:43 Yeah, I might not have a lot of time, but this one seems pretty…
small in the scope, and we don't need refinements for the next release. We can release without it and leverage what we have so far.
Josh Suereth 00:51:58 We can, it's just, it gets really awkward when you tell people to try V2, and, like, one of the major things they ask initially is how to do a refinement. Like, that's the most commonly asked thing for now.
of, hey, I want to make a refinement, and you're like, oh yeah, you can't do it in B2.
Oh, seriously. Okay.
Oh, the other thing I could add is importing… importing anything at all that's not a metric.
Liudmila Molkova 00:52:23 Oh, that, yeah, this one is definitely a problem.
Josh Suereth 00:52:26 Yeah.
Liudmila Molkova 00:52:28 Do we have those issues?
Josh Suereth 00:52:31 We do… I think it's under V2 schema. If you look at… if you look at To Consider for Next Release, I put the… it's… it's called something about extends in V2. That… that one I assigned to myself. And then…
I think it's over in the V2 schema side, actually.
The other one.
Jeremy Blythe 00:53:01 Are you talking about the import?
Josh Suereth 00:53:04 Yeah, I thought we had an issue for that, do we not?
Jeremy Blythe 00:53:09 Yep.
So in my other crazy PR that I did about dog fooding live check, I'd have a look at sometime.
I do that. So I've written a V2.
model, and I import entities.
Josh Suereth 00:53:25 You can import an entity, you can import a metric, you can't import anything else. Okay.
Jeremy Blythe 00:53:30 Good luck.
Josh Suereth 00:53:31 Yes, you did. I assume you're only making metrics and entities, then?
Jeremy Blythe 00:53:37 I'm only importing entities.
Josh Suereth 00:53:39 Okay.
Liudmila Molkova 00:53:44 Nope, no issue.
Josh Suereth 00:53:48 Yeah, we should make one, then.
Liudmila Molkova 00:53:51 Yeah, for the next release, right away.
Josh Suereth 00:53:54 Yeah, and if you want to make it a real issue, if you want to make a pretend issue and we make it a real issue later, that's fine too.
Liudmila Molkova 00:54:00 Yeah.
Josh Suereth 00:54:08 So, which one do you think… would you say importing is higher priority, or refinement is higher priority?
Liudmila Molkova 00:54:18 Mmm… And I think Kikuli, so…
Jeremy Blythe 00:54:24 I was gonna say, yes.
Yeah.
Josh Suereth 00:54:27 I'll do them in the same PR, no.
Okay, cool. I'll, I'll do whichever one I think I can get out quickly.
First.
That might actually be importing. I think that might be an easier one to solve, initially.
Liudmila Molkova 00:54:44 Right.
The… I'm thinking in terms of their priorities.
We actually have OTAP approved by Tigran.
And we should capitalize on the moment.
this one would be probably the highest priority for the OTAP. It's kind of…
Details, how we make the refinements and importing part for everything.
So I'll try to focus on this too, and they're both small enough for me to bite.
Josh Suereth 00:55:24 Cool, if you need help with any of that, just let… let me know.
yeah.
Oh, another thing I was thinking about doing, and I don't know if this is worthwhile, there was a… there was a study done that I saw.
Where apparently the agent.md files are mostly useless in practice. I don't know if you saw this.
Liudmila Molkova 00:55:46 Sent it to you.
Josh Suereth 00:55:47 Did you… yeah, yeah, you sent it to me, Ludebella, that's right. That's how I found it. I wasn't sure if… I get so much crap about agents that I don't remember where it comes from.
here's what… here's… here's a few things I want, though, from, like, watching Cloud Code and Rust. I want a list of, like, dumb-style things that the agent will stop doing that annoy the crap out of me. For example, don't call unwrap every frickin' 3 seconds in a test.
use expect, and put a reason, you know, like, why it fails. So, I… I know that this could be the definition of insanity. I read that paper, I see what they're saying.
But in practice, the annoying things agents do that I hate, if I make an AgentMD file, it doesn't do it. And so, I kind of want an AgentMD file for Weaver that gets rid of certain things, or tells it how to do tests and, like, some style stuff.
What… how do we feel?
Jeremy Blythe 00:56:45 I have a ClaudeMD that I've been putting that kind of stuff in.
that you can make an AgentsMD, and then you make your Cloud MD just say, at AgentsMD, and then you would end up with the same thing.
Josh Suereth 00:56:57 Would you be willing to submit the agent MD?
Jeremy Blythe 00:57:00 Because then Copilot will use it. Gradually adding to it. So I have things like always write dry code, and…
use expectants. We can also change the Clippy settings, by the way, if… so we can say, even in tests, you're not allowed to unwrap.
But you're allowed to expect, so we could change Clippy, and then we'll have a lot of squiggly lines in the code, but…
Josh Suereth 00:57:24 Yeah. Well, actually, just the thing that says, like, run a test, If the test fails.
don't keep making more tests. Fix the tests, then continue. I love how you actually have to explain that, but then, when you're done with the tests, run cargo format and cargo clippy and fix all things.
Jeremy Blythe 00:57:44 Yeah, I have that.
Josh Suereth 00:57:45 Like, like, just that kind of stuff, if we should just have an HMD file without it, right? Or we could… if it's in a README that it'll use, I don't know, but let… like, yeah, if you… if you already have that, that's kind of what I was asking. If someone already has that written for Weaver.
Please submit…
Jeremy Blythe 00:58:03 I do, and we can build on it, for sure.
Liudmila Molkova 00:58:11 I asked…
Claude, since we have 2 minutes and we probably want to decide anything, I asked Claude to find public methods that are not used, or only used in tests.
And it found quite a few.
Jeremy Blythe 00:58:25 Yep.
Liudmila Molkova 00:58:26 I'll probably send a PR to clean it up.
Jeremy Blythe 00:58:31 What I… One thing I've found is that at the end, you ask it to review what it's written.
And then it will do a review.
And you… also, you can say, like, now that you did all that, how would you improve it?
Which is kind of… just like you'd ask, Curtin.
you know, a junior engineer or something. It's kind of… it's kind of funny.
And then, you can point codecs at it, or some other…
Agent, and go, like, now you do a review, and it's interesting, you get different things back.
Yeah.
Josh Suereth 00:59:04 For me, my favorite use of agent so far is when I'm writing something hard that I don't trust the agent to do, I'll still do it myself, or where I've tried to use an agent and it's failed, and so I just, like, have that natural inclination to not even bother trying with the agent.
Maybe I need to fix that, but anyway. My favorite thing is just, hey, go clean this up and make it chippable as a PR, because I have so many spelling errors and mistakes. That's my most common skill, is, like, fix up Josh's dirty PRs.
Yeah.
Hopefully you'll see a difference in how many spelling errors I have going forward, but I don't know. Sometimes it doesn't catch up.
Liudmila Molkova 00:59:44 This is how you know when you're real.
Josh Suereth 00:59:48 Yep.
neil yashinsky 00:59:50 The only way you know an agent did something right is first the agent did something wrong, and then you correct it. In my opinion, or experience. Or at least most of the time.
Liudmila Molkova 01:00:04 We are at time. Really appreciate the discussions. See you around.
ariannavespri 01:00:11 You, thank you.
neil yashinsky 01:00:12 Hi. Thanks, everyone.
Liudmila Molkova 01:00:13 Ron T.
