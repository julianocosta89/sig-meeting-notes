SIG: Semantic Convention Tooling
Date: 2025-09-03
Duration: 40 minutes
Zoom Recording URL: https://zoom.us/rec/share/O5PmMcEGy_HzM-1K1SXq54hOQh_1jfDZAU7vCq2CM1A7fKeq4-PBH3KCp2AXP4hE.KfTwQi9AaM75ybrI
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 03:22 Hey, folks.
**Jeremy Blythe** 03:24 Hello.
**Liudmila Molkova** 03:38 I guess let's wait for Lauren to join.
**Jeremy Blythe** 03:42 Yeah.
I did manage to do some work.
On reboot.
At the weekend, so… That was a welcome change.
Just some maintenance stuff, yep.
**Liudmila Molkova** 04:17 I managed to write some Rust code over the weekend.
**Jeremy Blythe** 04:23 Funk.
Do you like the language?
**Liudmila Molkova** 04:37 I mean, I… I don't… I don't have personal feelings to languages.
**Jeremy Blythe** 04:43 Okay.
**Liudmila Molkova** 04:45 I like certain features, but I don't know enough.
About it.
**Jeremy Blythe** 04:52 Right.
**Liudmila Molkova** 04:55 It seems you do like the language, right?
**Jeremy Blythe** 04:58 It's the only language I use now.
**Liudmila Molkova** 05:00 Oh, okay.
So I know why it does it. I used to write some C++ years ago.
And I understand it… It has to be sometimes verbose when it comes to Safety.
But man, if I need to… I don't know, iterate over something and collect it into a list.
Like, 34 Alliance.
My name is… C-sharp or Java features on streams.
Where you can do it with a couple of short expressions.
**Jeremy Blythe** 05:52 There's probably a way.
**Laurent Quérel** 05:59 Hi everyone, sorry to be late.
**Liudmila Molkova** 06:02 Oh, we're talking bad about Rust here.
It's a joy.
**Laurent Quérel** 06:06 I understood that.
What was the issue with West in that case?
**Liudmila Molkova** 06:14 Not an issue. I was just rating some Rust over the weekend. There is no issue.
**Laurent Quérel** 06:22 13.
Yeah, it's definitely, there is a long curve that is not, not worked, definitely.
I did, I asked my team, recently, some of them to, to learn Rust.
that took, I think one month's… To be comfortable with.
**Liudmila Molkova** 06:51 One month's is not much.
**Laurent Quérel** 06:54 Sometimes a little bit more, but Let's say, in average, one month.
Definitely, you are not expert after women's, but, at least, you stop fighting the compiler.
Most of the time.
And I think also that depends also which area of Rust you are… Dean, Louise.
Standard rest, I think it's okay. Async REST is… is more… is more complex, more polymetic.
**Jeremy Blythe** 07:27 Yep.
**Laurent Quérel** 07:28 Most of the time, that's where people are complaining a lot.
But there are ways to… To avoid that incense circumstances.
For example, for the project, I'm leading with, Joshua McDonald, the Rust days, Telemetry pipeline system.
I decided to use a thread-per-go approach.
So we can rely on… For each claw, you have the sync runtime.
But it's a specialized asynchron time, because you don't have this, concept of, not sand, not sync… But you don't have this concept of send and sync that is required when you are using Tokyo in a standard way.
In that case, there is no such constraint.
No bound of this type on the… On the type that will be, manipulated by this runtime engine.
And that simplifies a lot the entire story.
**Liudmila Molkova** 08:48 What runtime is that, then?
**Laurent Quérel** 08:50 In fact, Tokyo is coming with tour on time.
There is the… the work ceiling approach, that's the standard, the multi-suaded slash rock ceiling.
Runtime is the standard one, but there is also, a local runtime.
**Jeremy Blythe** 09:09 How are you?
**Laurent Quérel** 09:10 Slash single threaded runtime.
And and for this one, you… you have a spawn method that does not expose or force you to have this constraint of send.
**Jeremy Blythe** 09:28 I have to look.
**Liudmila Molkova** 09:38 I love this discussion. I don't want But I… I will need to run in 15 minutes.
**Laurent Quérel** 09:44 Yeah.
**Liudmila Molkova** 09:45 Friend, something by you?
And hear your thoughts.
**Laurent Quérel** 09:51 Sure.
**Liudmila Molkova** 09:51 thank you.
Maybe I'll share it?
**Laurent Quérel** 10:01 I like the mini bed for you, for your cat.
**Liudmila Molkova** 10:04 Aw, thank you.
**Laurent Quérel** 10:06 Pretty cool.
**Liudmila Molkova** 10:07 Thanks.
Okay, I was playing with attribute groups, and what have I done?
So, to remind the problem, we have… In Schema V2, we have spans, metrics, right, entities, I forgot all our signals. Anyway, so we have signals.
We don't have attribute groups.
And… in order to migrate to V2, we need to figure out a couple of things for them.
First one, we use them quite a bit for to reduce copy-paste, right? So there are metrics that share certain attributes, or multiple signals that share them.
And if you look to, let's see… Here, you would see that we use attribute groups for… And actually…
**Laurent Quérel** 11:24 every extent, yes.
**Liudmila Molkova** 11:26 Yeah, with Xtend, yeah. Xtend… well, Xtend sucks, but that's a separate problem.
And essentially…
**Laurent Quérel** 11:33 Yeah.
**Liudmila Molkova** 11:35 There is quite a bit of common grouping here that allows us to avoid copy-paste.
And it's not just avoiding copy-paste, right? It's when we make small changes in one, let's say, server address.
how it's captured for HTTP case, it actually affects all the HTTP client metrics and spans, and it's important to have it written once, otherwise we will just forget.
**Laurent Quérel** 12:08 Sit up.
**Liudmila Molkova** 12:10 Okay, so this is one scenario. These groups… are interesting. They are irrelevant to anybody who's looking at it out from the outside.
I can reshuffle them, I can move it to dispense themselves, nobody would care.
There are groups that are not like this. There are groups like exception, and we can attach exception information to Pretty much any span or event.
So… For these groups, I'm actually… let me scroll down to the proposal.
**Laurent Quérel** 12:51 I didn't understand, sorry to interrupt you, Limila, regarding when you said, there are groups where we care, groups where we don't care, I guess during the… after the resolution phase.
And you mentioned exception.
Why, why exception is different from the others?
**Liudmila Molkova** 13:13 And there are a few groups like this. Imagine you are writing something, and exception happens.
You would say, okay, Annotate the signal with exception information.
Like, if it's a span or an event.
It's not that exception is an event on its own. It is, currently, but it's actually… it feels not great.
But it's more like an additional set of attributes that describes a thing that you would populate on arbitrary signals.
**Laurent Quérel** 13:50 Okay, so, So, if we consider a stand which is misnamed, probably, and that could be something like, you compose, in fact, you include a set of attributes. If we consider that, do you think that the two scenarios that you exposed are really different?
**Liudmila Molkova** 14:13 They kinda are. So, If you look into this… these groups.
that are internal implementation detail. They… they actually… there are two properties, right? The sum ID to refer to this group later, and a list of attributes.
You wouldn't have brief, you wouldn't have stability, you would never deprecate this group, you would just remove it, it's… it's essentially these two things.
There will be no annotations.
When you think about the publicly visible group, it has all those properties, right?
And… where… Could, in theory, fit it into one concept of the attribute group.
But then we would… we would not validate the presence of these properties, right? It would not be the… the serialization time validation, it would be something, some construct that says, oh, okay, this is a public group.
Let me actually check that certain properties are present and valid.
Something like this.
**Laurent Quérel** 15:24 Okay. Yeah.
**Liudmila Molkova** 15:26 It's… it's not a strong opinion, but… In my mind, they are… they are two different things.
**Laurent Quérel** 15:38 The most important thing is, at the end, After resolution, the… Validation constraints that we like to see on attributes should be observed.
Either there have been, like you said, override.
Along the way, independently of the type of the attribute group.
Looks like it doesn't really matter, but at the end, the end product has to be valid.
With the constraint that we decide to apply.
**Liudmila Molkova** 16:17 Right.
**Laurent Quérel** 16:18 Okay.
**Liudmila Molkova** 16:21 And, in my… Proposal later.
I call this, internal groups mix-ins, and just to set expectations, Josh does… is not super happy about it.
So, we might… End up with something else.
But let me… let me go through the proposal, and I'll talk about Josh's point. Yeah, Alexandra?
**Alexandra Konrad @Elastic Security** 16:48 Yeah, sorry, I just came and, looking into all of this. Why do we need, internal groups? Could you just, a few words, elaborate, why we make this difference now?
**Liudmila Molkova** 17:02 So if you look into the existing semantic conventions, there are tons of those groups.
They are meaningless.
They are not used, in any use case, they're just used to combine,
**Alexandra Konrad @Elastic Security** 17:18 group, attributes, yeah? That's what you mean.
**Liudmila Molkova** 17:22 They are used in the use cases, they are… they should not be visible after we resolve schema.
They are only used as internal implementation detail.
So, this group, is used on metric… HTTP metrics and spans.
**Alexandra Konrad @Elastic Security** 17:42 Yeah, I understand what you mean now,
**Liudmila Molkova** 17:45 I like, like this.
And after it's used for the span, it's essentially… it should not appear in the resolved schema.
But more and more… the most important part is we are working on the schema V2, which helps us to clean things up and express it more easily. I'm not sure if you're aware of this effort.
**Alexandra Konrad @Elastic Security** 18:10 No, I was reading it today, but haven't finished yet.
**Liudmila Molkova** 18:14 Yeah, and it's actually… it… it doesn't have attribute groups, so that's… that's all we have, plus imports.
And in order to migrate to Schema V2, we need to find a way to represent those attribute groups.
If I tried to implement this today, I would end up with tons of copy-paste, like, tons of it.
**Alexandra Konrad @Elastic Security** 18:46 Okay.
**Liudmila Molkova** 18:48 Okay.
So… Back to the attribute groups.
So what I've done? I've done some hacking in Rust, and I've… Came up with this.
Approach, let me find a good one.
It's called HTTP.
So… This is the V2 version.
We have attribute groups here. These are internal groups, I didn't tackle the external in this prototype.
It looks pretty much like what they described.
there is a little bit different way of grouping things. So, for example, we can group by feature, so… Some signals have URL, others don't.
There are specific groups around, like, server address, server port, which are repeating all the time.
But essentially, if we look into the spans where it's more interesting.
Instead of extension, we can now… Mix and match different groups.
So, the span includes all these groups. They cannot have any conflicts. Like, if there is an attribute that appears in more than one, we'll fail.
But don't…
**Laurent Quérel** 20:23 Okay, so I was trying to find the end to, to ask,
**Liudmila Molkova** 20:31 Yeah, yeah, go ahead.
**Laurent Quérel** 20:32 Sorry, I didn't. Include groups, so we replace the extern, which… That will be much clearer, in my opinion, and you can list multiple of them.
So it's like, you compose, and if there is, Some overlap between the… we… we return, an issue.
**Liudmila Molkova** 20:55 Yeah.
**Laurent Quérel** 20:56 Okay, good.
**Liudmila Molkova** 20:59 And we have a single place to refine them, additionally, so that this works.
Okay, so what Josh mentioned he doesn't like. So, okay, so one more thing before I, we go to the Josh's point.
I prototyped it in Weber.
I prototyped it in HTTP and databases, I've got effectively zero difference in Markdown, so it's a viable approach.
I kinda like this way a little bit more. I shaved a little bit of code, in YAML.
Not much, but it seems like it allowed me to be more flexible.
To Josh's point, he doesn't like mixing, it's the personal preference, He would rather see something like.
let's say we would have a template span for HTTP client, or… well, for HTTP client, it wouldn't fly.
But he would rather not have the… Makes sense.
**Laurent Quérel** 22:16 What you may be missing here, in this example, is the…
**Liudmila Molkova** 22:21 these guys.
Let's call them groups for now. Let's just stick with attribute groups. But they… it's… they are effectively a mixing pattern, right? You are combining… Multiple pieces together, and those, they are used instead of, inheritance, right? And they provide some features if you mix and.
**Laurent Quérel** 22:47 That's good.
**Liudmila Molkova** 22:48 together.
**Alexandra Konrad @Elastic Security** 22:50 That means all attributes from those groups will be available in this, new span all.
Is it not then… Similar to the embed feature we discussed before?
Like, we're just reusing some of this, or this, like, how would semantically different?
**Liudmila Molkova** 23:15 It's different in the way that we are just using refined attribute.
We are not, we are not French editor.
**Alexandra Konrad @Elastic Security** 23:24 Finally, okay, yeah.
**Liudmila Molkova** 23:26 It's essentially current extents, but for multiple groups, and it does not, like, inherit anything except… it just includes the attributes listed there.
**Laurent Quérel** 23:44 Yeah, they are include, but can be override inside the attribute section.
**Liudmila Molkova** 23:50 Right.
**Laurent Quérel** 23:53 And they can't overlap.
Okay.
Okay, so, sorry.
**Liudmila Molkova** 24:02 Go ahead.
**Laurent Quérel** 24:02 I was, just, it's… it's closed… Also, to the… This other import option that we, we have.
Where we can use WorldCard.
The question for you is, do you… Do you think that supporting Waycard will also, for some scenarios, the, a pool?
To minimize the amount of things that you have to, To specify when you have a signal, and you know that you want to import every attribute, starting with this prefix.
**Liudmila Molkova** 24:49 If it's about attributes, the wild card, rough wildcard…
**Laurent Quérel** 24:53 Yeah, we'll be there, yes.
**Liudmila Molkova** 24:54 Yeah, it could be.
It's like we do this when we know that attributes inside that group are refined already.
**Laurent Quérel** 25:04 So…
**Liudmila Molkova** 25:05 we… I don't… I don't see how wildcards could be helpful for this.
**Laurent Quérel** 25:17 Yeah, okay.
**Liudmila Molkova** 25:22 Yeah, so I wanted to run it by you, and since Josh is not super happy about this approach, I will probably keep thinking about alternatives, and if you think… could think about anything Drop it in the issue, there is a thread on the Weaver channel, feel free to… Drop by.
**Laurent Quérel** 25:43 Yeah, I need to read it to better understand the complaint.
For why Joshua is, is not happy with that.
I don't responded.
**Liudmila Molkova** 25:56 Yeah, I will continue to… we'll probably run it by, on the semantic conventions call on Monday.
And we'll collect some… Other ideas and feedback from Josh and, other semantic convention authors.
**Laurent Quérel** 26:18 what I'm reading, at least at the beginning, is he's complaining about this difference between Internal slash public.
So… Maybe later in the conversation, he's also talking about the mixing.
**Liudmila Molkova** 26:39 Yeah.
**Laurent Quérel** 26:39 expect, but.
**Liudmila Molkova** 26:41 It is kind of a long conversation.
**Laurent Quérel** 26:44 Okay.
But, personally, regarding the internal slash public.
I'm not sure that there is a real need to, what is your argument to have this, If we have any way, a generic mechanism that ensures that we never use, attributes in Signal that are not… Compliant with the set of policies slash rules that we, we defined.
Why that will matter to have, Because anyway, even if you have a public affidu group, If it's not used.
It does not, in fact, it does not hurt if this public affiliate group Does not have all the… the field required for attributes, because they could always be override… When they are used, When they are, included?
And then that's where they will be validated. So the… my question is really why we need the difference between the… these two attribute group concepts.
**Liudmila Molkova** 28:08 Yeah, that's a great question. So, I think we have a problem now.
Well, if you look into this, this file, General Attributes.
At least some groups of the attributes.
And, like, I'm not sure exception is here, but those are these orphan groups.
That have some… Sometimes have meaning.
So I think a good example is also… cloud events.
It's actually not spans, it's events.
It's actually just attribute group.
Not, not a span definition.
So we have… some groups in the documentation that we document explicitly, and it's not just the namespace, it's a convention. So here, you would see there is a context propagation of some sort, some section on it.
You might see… Some additional information.
Or, when it comes to, let's say.
browser stuff, user and session, that are also propagated over the wire, and sometimes are used to stamp on the backend telemetry. So these are actually conventions on its own.
And… Where… guarantee something about it, right? So, there are, for example, requirement levels within this group. They are meaningful, so if you populate this group at all.
you follow… This, convention.
I cannot say, okay, the namespace is the group, because it's now not bounded, right? I don't know what will be there in this namespace at some point.
And…
**Laurent Quérel** 29:55 I see.
**Liudmila Molkova** 29:56 Yeah, and we have a problem, we have no means to say, okay, this group is meaningful, but that group we don't care about. Like, if you remove it, we don't care.
**Laurent Quérel** 30:08 Yeah, okay.
Yeah, we could reorganize, internal groups, differently, if at the end of the day, After resolution, we end up with the same set of attributes, with the same characteristics in the signals.
We don't really care.
As opposed to this one, where… It's, it's, first, it's in the documentation, so it's, it's documented and visible.
And I can understand that in that case, the field that we have in the table are… somewhat useful, because they… they will inform the reader of what is… what are the expectations, everywhere where they are used.
**Liudmila Molkova** 30:55 Right.
**Laurent Quérel** 30:56 Okay.
Yeah, I think I'm convinced about the… The requirement of having, Either it's a property, saying it's public versus not public, or maybe it's a different concept.
Personally, I think I would see that as a property.
Like, when you… you have a… A prefix for a function saying it's public, it's… It's… it's just, like, an annotation, or… Something that, specified that the function is public, but it's still a function.
**Liudmila Molkova** 31:39 this video.
**Laurent Quérel** 31:40 I will see that as a property more than a… a new concept.
**Liudmila Molkova** 31:50 That's a good feedback.
Okay, I appreciate your time in this, I need to drop off, I'm sorry.
**Laurent Quérel** 32:05 Thank you so much for having me, Lam.
**Liudmila Molkova** 32:07 Yeah, thank you all.
**Laurent Quérel** 32:10 Jenny or Alexandrois, I don't know if you… if you had, time to read the… I created a description on the metric set, the concept of metric set.
If you have any feedback on that, or if you didn't, or if you are not aware, I know that Jamie is aware, but I don't know for Alex or… I'm still interested by having some, some feedback about it.
**Alexandra Konrad @Elastic Security** 32:42 No, I haven't. I just read today in the chat, what have we discussed, but I… I'm not sure I know about… about which PR are you talking right now.
**Laurent Quérel** 32:57 not Pierre de…
**Alexandra Konrad @Elastic Security** 33:00 I…
**Laurent Quérel** 33:01 8.
**Alexandra Konrad @Elastic Security** 33:01 Hmm.
**Laurent Quérel** 33:02 288, yes.
**Alexandra Konrad @Elastic Security** 33:04 Yeah, metrics.
**Laurent Quérel** 33:05 I think that could be interesting for… in your context, because, Elastic, search is one of those Systems that naturally supports multivariate object.
As opposed to primitives that, Which is not supporting multivariate matrix.
So, supporting multivariate matrix for Elastic will be natural, in my opinion.
And, and, and very beneficial, so I'm interested by having your, your feedback.
With your, background and, Knowledge of what your customer expects to see if there is, Something that is missing right now, and people find some workaround.
But, if they had, a f… A first class, or first citizen concept, like a metric set available, they… they will use it right away.
**Alexandra Konrad @Elastic Security** 34:11 So let me check it.
Thanks.
**Laurent Quérel** 34:17 And, and Jeremy, did you, Have you been able to read.
**Jeremy Blythe** 34:24 I haven't…
**Laurent Quérel** 34:25 It's a guitar issue.
**Jeremy Blythe** 34:26 Yeah, I haven't looked at it deeply, I… Aye.
Okay. I'm just, yeah, struggling to find time right now, but.
**Laurent Quérel** 34:34 Yeah, like me, I agree.
**Jeremy Blythe** 34:36 I think all of I don't know, it's like a busy season or something. Something's happened, we've all got crazy. But, I think I mentioned last time, like, I don't have a huge amount of experience using metrics, like, at all, so I…
**Laurent Quérel** 34:53 Yeah, okay.
**Jeremy Blythe** 34:55 really offer… too much, feedback, but I will… I have it open in front of me, so…
**Laurent Quérel** 35:03 Okay.
**Jeremy Blythe** 35:04 Yep.
**Laurent Quérel** 35:06 Okay, that was the only, topic I had in my mind.
Any other, scene that, I don't know, Alexandra or Jeremy, you want to discuss?
**Jeremy Blythe** 35:22 I think at some point soon.
We should have a clear-up of, like.
old PRs and old issues that maybe don't make sense anymore, like… At the weekend, I actually managed to do a couple of PRs on some maintenance, which was good, but there's still two… there's two PRs that have been… Sitting in the list for, like, Over a year.
then I think we just need to, like, decide whether we're going to… do something with them, or just close them off. And there's probably a bunch of issues. We're up to 100 issues. There's probably a bunch of really, really old issues that we can close down.
I think a bit of.
**Laurent Quérel** 36:06 Yeah.
**Jeremy Blythe** 36:07 Let's go through.
You know, close things down might be… might be a good idea to tidy up.
**Laurent Quérel** 36:13 For example, they create a more flexible HTML command parser and raise warning.
**Jeremy Blythe** 36:19 Yeah, right.
**Laurent Quérel** 36:20 this one… Yeah, that's someone that can dip something, but never finish.
**Jeremy Blythe** 36:33 Right, so July 2024?
**Laurent Quérel** 36:36 Yeah.
**Jeremy Blythe** 36:37 Proof of concept attribute ref renaming.
Like…
**Laurent Quérel** 36:42 the Russian Emi were.
**Jeremy Blythe** 36:46 It's a draft.
**Laurent Quérel** 36:47 Oh, yeah, the first one?
**Jeremy Blythe** 36:47 on the…
**Laurent Quérel** 36:49 This one, I think we can close it.
**Jeremy Blythe** 36:51 I remember this one.
**Laurent Quérel** 37:07 Yeah, it's… I don't think it's well aligned with, Especially with what we are doing with Schema V2.
Oh…
**Jeremy Blythe** 37:22 And then… We seem to have a bunch of proposals as PRs rather than proposals as issues.
**Laurent Quérel** 37:30 Yeah, that's a common pattern we had with, We stop son, yes.
And most of them, I know that Joshua mentioned, okay, right now we are focusing on Schema V2, and for some of those proposals.
Which should be, indeed, in the… as a GitHub issue.
I think he mentioned that he'd like to, to keep them, open until we have a stabilization regarding scheme, maybe too.
**Jeremy Blythe** 38:07 Okay.
**Laurent Quérel** 38:14 Okay, what I can do is, So, for you, Jeremy, the last two, You will not be against to close them?
If I understand well, and you were asking what about the values proposal?
So I can, myself read the, the various, Pierre… And maybe, Purpose something into this, into the… With you and, and Josh and Lumia.
Making sure that we are all aligned, and then, we, We take the appropriate action, close the pier on which we have an agreement.
**Jeremy Blythe** 39:04 Yeah, I guess… For the PRs, it really… it's just, like, those last two.
they've… They click… They've been there ever since I started contributing, I think, and… And I think if you look at the issues, there's some issues going back to, like, you know, when the project was first created, and…
**Laurent Quérel** 39:25 Yeah, yeah, okay, I will do, I will do some, some cleanup there.
**Jeremy Blythe** 39:31 Yeah, it's just… it just struck me, because, like, hang on, now we've got 100 issues, or I think I got.
**Laurent Quérel** 39:37 No, no, it's always good to have some…
**Jeremy Blythe** 39:39 million.
**Laurent Quérel** 39:39 some thinning phase, yes, I agree.
**Jeremy Blythe** 39:43 So…
**Laurent Quérel** 39:44 So do you agree?
**Jeremy Blythe** 39:45 Yeah, that was the only thing I had, really.
**Laurent Quérel** 39:50 Okay.
**Jeremy Blythe** 39:51 Yep.
**Laurent Quérel** 39:55 Put that on my to-do list.
Okay, so if there is no other topic, suggest to, To stop there and get back at the last 15 minutes.
**Jeremy Blythe** 40:11 Yep, sounds good.
**Alexandra Konrad @Elastic Security** 40:13 Thank you.
Thanks. Bye.
