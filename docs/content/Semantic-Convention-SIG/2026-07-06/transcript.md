SIG: Semantic Convention SIG
Date: 2026-07-06
Duration: 56 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 03:51 Bye folks.
It seems we don't have a quorum today.
Maybe everybody's coming back from long weekend.
**Armin (Dynatrace)** 04:00 Yeah, is there any public holiday that I've missed today? There isn't, right?
**Liudmila Molkova** 04:06 The 4th of July was over the weekend, and maybe some companies have Monday off?
**Armin (Dynatrace)** 04:14 Oh, mine observed it on Friday, day before, but.
Maybe some other safe Monday, yeah.
**Liudmila Molkova** 04:22 Yeah, or maybe people are just tired.
But it seems we should call it, what do you think? Oh, Josh is saying we can join now.
Okay, then let's wait for Josh.
**Josh Suereth** 04:38 Hey, sorry, my previous meeting ran really long.
**Liudmila Molkova** 04:42 It's okay, it's super quiet here today.
**Josh Suereth** 04:45 It's… it's, really hot in a lot of places, so…
**Liudmila Molkova** 04:50 Okay.
**Josh Suereth** 04:51 We're just all tired.
**Liudmila Molkova** 04:53 air.
**Armin (Dynatrace)** 04:55 Or have power outages.
**Josh Suereth** 04:59 Oh, that's true. We had really bad storms, so we had power outages here, too. It went from over 100 Fahrenheit, which I think is what, 37, 38 Celsius, and it dropped to 30.
And so, we just had this crazy storm system come through.
**Armin (Dynatrace)** 05:17 Mmhm.
**Josh Suereth** 05:18 few places.
Anyway, I would say, regardless of whether it's your summer or your winter, now is a great time for vacation as well.
You know, it's, like, halfway through the year.
you just finished your Q2 check-ins or whatever, like, financial reporting. Everybody wants to take a vacation before they have to deal with all the craziness.
**Liudmila Molkova** 05:44 But it gives us opportunity to talk about V2 stuff.
**Josh Suereth** 05:48 We can, yeah.
I, I just approved your, policies.
By the way…
**Liudmila Molkova** 05:57 The ones in waiver packages?
**Josh Suereth** 05:59 Yeah.
**Liudmila Molkova** 06:01 Yeah, so I'm thinking we can approach the V2 migration from the other side, from the output first, and then we gradually switch everything.
and I've been trying to figure out what would it? It would take. So maybe I'll present.
**Josh Suereth** 06:19 Oh, that'd be.
**Liudmila Molkova** 06:21 I'm sorry.
Okay.
Sorry.
I'm going to present this.
1 sorry.
And.
Let's go to semantic conventions and.
So we have a bunch of things in Makefile that we will need to switch.
This one… As switching to policies that we just talked about, and once it's merged.
We can… I can undraft this one, and… Hopefully, this will work.
The next more difficult step is templates.
I… So… I'm sorry, I have a P, I have a change for it, but it's on a different.
come… Peter, the key trick there is attribute groups, of course.
So, if we… Take a look at, let's see, hardware… Anything here?
So this friend's.
This is an attribute group.
And it's not a problem. We can render attribute groups.
But… It has requirement levels.
And We can think and we can fix it, right?
We can include this attribute group into all of the…
**Shashank Reddy (New Relic)** 08:24 Of course, we were seeing the other screen, like, we were seeing the different screen.
**Liudmila Molkova** 08:29 Oh, what are you seeing?
**Armin (Dynatrace)** 08:35 Meeting notes.
**Liudmila Molkova** 08:38 Oh, I'm sorry.
and… Okay, Thanks for pointing out this. Can you see?
The semantic conventions, the hardware, CPU, MD now?
**Armin (Dynatrace)** 09:08 Yep.
**Liudmila Molkova** 09:08 Yeah, thank you.
Okay, so, long story short.
There are this.
A bunch of these places where we render attribute groups.
And.
the… this is not a problem. The problem is that we don't have requirement levels and attribute groups in V2.
And even if we start converting to V2, we wouldn't be able to have them here.
We can fix it, right? Which would mean, fixing all those metrics, and there are, I don't know, maybe even a hundred of them in hardware, and it's a long, hairy change I don't wanna make.
So what I maybe want to do… is… Just.
They're up their requirement level.
We know this metrics like most of them, let's say, in hardware space or Needs a lot of work.
And they're not actually formally defined well yet because.
For example, this group is shared across all these metrics, but the formal definition never mentions the group itself.
So I… Well, try to figure out some reasonable hack that.
like.
Allows us to come back to it later.
Where we can decide, okay, let's fix it.
I'm kind of curious what you folks think.
**Josh Suereth** 10:49 Can I rephrase this, I guess? So…
**Liudmila Molkova** 10:52 Yes.
**Josh Suereth** 10:53 Requirement level in V2 is signal only, right? Like you need a signal to have a requirement level of required recommended.
hardware metrics, we already know, aren't necessarily up to our standards, right? In other ways. But you have a group That you want to reuse that defines a default requirement level that is then inherited when that group is included in the signal.
**Liudmila Molkova** 11:17 Ma'am.
**Josh Suereth** 11:19 And in the new one, we have the ability to have groups, but we assume you're going to mark the group with the requirement or recommended, and they all come in together, or they all don't come in together.
**Liudmila Molkova** 11:28 Right.
**Josh Suereth** 11:30 Yeah.
Yeah.
I know… I know what I would prefer, because I'm thinking about cogen, right? Like, the reason why we made those decisions is we wanted cogen to be possible, where it's not just… a, you know, here's a bunch of strings that's really hard to use. We want it to be, here's a, here's a function that makes a metric, you know, and then here's recording a point that takes a structure or something, or key value pairs. So, if we, if we go along that line, the way this is defined is actually really hard to code gen.
**Liudmila Molkova** 12:09 It's impossible. It's just not the definition that can be co-generated because the definition is broken down into pieces.
**Josh Suereth** 12:20 Right, which is why I think I'd rather… clean this up if possible, if we can do so in a way that doesn't change the metrics themselves? Like, can we change the model without breaking the metrics? Is that something we can do or not?
**Liudmila Molkova** 12:34 We can, it's just because.
We can… merge this group and reference it in all the metrics. There are some interesting problems with this one.
So, look at this metric. It's hardware errors.
And it's, oh my gosh, it's defined in multiple files.
And this is hardware errors for CPU.
And.
Effectively, this metric Is a giant blob of things.
That's… With attributes conditional to the context.
For CPU, it's reported with this attribute, for fan, it's reported with that attribute, and so on.
We can try to fix this as well.
**Josh Suereth** 13:34 Are those actually refinements or not? They're not refinements, are they?
**Liudmila Molkova** 13:39 We can call them refinements, yeah?
I like it. Well.
You can't say it's refinements.
Right?
**Josh Suereth** 13:51 I mean, it sounds like that's what it's supposed to be,
**Liudmila Molkova** 13:57 Right. Okay.
Cool. We're getting somewhere with it.
Okay.
And I think we've discussed it… okay, so let's say we fixed hardware.
It's probably the biggest problem, the the in terms of quality quantity of things.
This one is… Another.
Interesting problem.
But it's it's a legit case, right? The exception.
So if we look here.
This is also an attribute group.
And it has requirement levels.
I can probably.
We can probably change them, but that's also another story, because it's a stable document.
And we… Want to declare there's a group, right? It's an exception type. If we quadgen it, this is the whole type we would quadgen.
And it has optional properties and required properties, maybe.
So, I don't want to lose these things, but also, it's not… it's not the same kind of… it's not… the signal, anyway.
**Josh Suereth** 15:35 Yeah, sure.
I guess this goes back to the Cogen thing again. If we were We don't… when it comes to exception, we really don't have a way to co-gen them, right?
**Liudmila Molkova** 15:50 Oh, we do.
**Josh Suereth** 15:51 Do we?
**Liudmila Molkova** 15:52 Bye.
And.
Well, you can hack something. You can say, okay, this is an event.
Or it's, yes, it's an event.
When you… are It's an exception event.
And we kind of have a convention now, we're saying that if you have an operation, like a span type, the HTZP client request.
then the exception for this operation is the span type dot exception HTTP client request exception.
And then, we can… Either by this convention, or by the presence of exception attributes on this.
Definition.
Say, okay, instead of, sorry, this individual attributes, take the whole exception type that's idiomatic for this language.
**Josh Suereth** 16:54 Mmh This is making… so… but then, it's an event, though, right? At that point?
**Liudmila Molkova** 17:09 It is an event.
But we want all events.
And even, Arbitrary logs.
Oh, we want codgen logs, but we… events to support this right.
We don't know the event name up front.
**Josh Suereth** 17:34 So this is where it gets into what we were talking about before with public attribute groups.
Should, should we treat a public attribute group as a signal?
I see it as kind of like an annotation, right? Like, there's a set of attributes that I can annotate on a span, or annotate on a log, or annotate on a metric, and say, if I add this to that thing.
It's like a… I'm thinking in type theory terms, if you will, but it's like an extension to the type, where I'm appending this information, and it kind of, like, augments the type.
With some…
**Liudmila Molkova** 18:12 Thanks.
**Josh Suereth** 18:13 Sure, we can call them traits.
Possibly. That could work.
Yeah.
what's the other thing? A concept? Is that the C++ horrible thing that they added, because they don't have traits? Yes. Yeah. We can call it… but I think traits actually works. It's like a… it's a… it's a meta signal that can be attached to other signals, right? Like, this thing carries an exception, and here's the information about the exception, and this thing can be added to any other signal that's generated and still be compliant to SEMCONF.
That… you know.
I'm still nervous about that concept, because I don't think we have a great model for it, for how to enforce it, how to make sure that it's compliant, all that kind of stuff. And we call it a public attribute group now. We could call it something else, but I'd be okay if we were to say public attribute groups can carry requirement levels.
And we figure out…
**Liudmila Molkova** 19:11 Let's start there, yeah.
**Josh Suereth** 19:13 What?
**Liudmila Molkova** 19:14 Let's start with it.
**Josh Suereth** 19:15 Yeah. And if we ever want to change the name to something that gives people an idea of what the hell it really is, that'd be good. Because again, an attribute group doesn't tell you when to use them, why they exist, what they're for, you know, what it means semantically. It's just sort of like, yeah, here's a group of crap, go deal with it, you know.
**Liudmila Molkova** 19:37 Yeah, sure.
We will, at least in the core semantic conventions.
gate the creation of new public groups. There should be quite a bit of scrutiny before we declare them, so that we Can control the blast radius once we do the hypes properly.
**Josh Suereth** 19:55 But see, that's the… my point is, I, you know, the thing I'm asking myself is, can I write down the decision logic that I go through when I decide if something should be a public group.
or a span, right? Like, what… what makes it a group versus a span? Because there's… the private groups make sense, it's just a… it's a way to group things together to make it less verbose when you have to bundle a set of things together, right? Got it. That's fine.
But a public group is actually part of our semantics in some fashion, you know? It actually, like, impacts how we do validation.
of, is the span compliant? We don't want a span that matches all the attributes, but has these exception things on to be marked as non-compliant, because it has attributes that aren't defined in semantic conventions. When they are, they're just defined in a way that can be added to any span, right? So we need to have, like, Weaver, LiveCheck actually understand that in some meaningful way, that these could be added to anything.
So that it doesn't issue warnings, you know, erroneously.
Which is why, like.
Okay, cool. So there's some sort of principle here I want to write down so that it's not just like those of us who maintain some kind of know if it can be blessed or not. It's not like a cabal decision. It's like a written down principle that people can reason through is what I want to get to. And I actually think we're almost at the point we could do that.
Right? Like, given the discussion, given how far we've explored V2, I think you could probably write down how you would make that decision.
And it still requires judgment, but I think we could write it down. Is that fair?
**Liudmila Molkova** 21:42 Yeah, I think so.
I'm thinking how I can.
Fix.
Make the weaver life check, understand it.
So, by… Having… So after things are resolved, if it's a public group, after things are resolved.
All the… Information on where it came from. Well, not all, there is still provenance, but it shouldn't be based on provenance.
I'm.
So we need some education that these things.
either came together.
So that when you see a span with exception message, but without exception type, maybe you should flag it.
**Josh Suereth** 22:39 Yep.
Which means having requirement levels make sense, and then, if we see exception type, we go look, we… instead of flagging, hey, exception type's here and it's not allowed, LiveCheck would go look for a public group that has it.
And then once it finds that group, it would try to examine does it have all the attributes or not, you know, and go into a different mode of conformance testing. I think that's reasonable.
**Liudmila Molkova** 23:03 Oh, we are back to the spend type problem, but now, like, years later, we will have a problem of discriminator for Bye.
These groups, if we have a lot of them.
**Josh Suereth** 23:17 Right, like, if I have both exception type in a group around exceptions, and I have it in some other group that someone defined, how to resolve between the two of them and make sure they don't overlap. I think we can… I don't think we have to open that can of worms right now. Yeah.
**Liudmila Molkova** 23:35 Yeah, please.
**Josh Suereth** 23:36 I think that is resolvable, but I'm saying that from gut feeling, not from anything I've written down.
**Liudmila Molkova** 23:43 Okay, so we want the principal.
For when we define those.
Down the line… the road, we want, LiveCheck to be aware of the things better when they are referenced on something.
But we don't have anything today.
Nope.
**Josh Suereth** 24:01 But that's a feature request we can make and fix.
I also think what I would add right now would be in our policies, in our namespacing policies, I would make a thing that prevents the same attribute from showing up in two public groups independently of each other, right? So if, like, exception type is used by this exception group.
It cannot also be in another public group.
So that we can do the live check lookup successfully. For now. Until we know more about how we want to do the modeling. Does that seem reasonable?
**Liudmila Molkova** 24:38 Yeah, it also reminds me of entities.
Yeah.
**Josh Suereth** 24:47 That's another story. We can, we can dive into that if you want, but no, I think, I think that's, yeah.
Okay.
**Liudmila Molkova** 24:55 So let's write down some notes before we forget.
Come on.
Okay, so the public, requirement levels.
Then… Oh.
And… This, the templates part, would be the hardest.
There are some minor stuff that will… Show up, so let's say we look on the registry here.
I'm… Okay, let's take a look, let's say, at Azure.
So we do a trick today, that the location of this MD file, the name of this MD file, depends on the name of the YAML file.
And we're, Put multiple namespaces.
in the same file. So here we have both Azure and AZ.
In one file.
And once we switch to V2, we will have maybe a handful of these new namespaces pop up in the attributes. I think it's okay. It just shows the reality.
I'm.
What else interesting will happen?
At.
This, okay, yeah, the last thing I wanted to mention, we will lose some stuff.
Again, if we look here.
There is this general, attribute section, and there is This piece of text that comes from.
I'm.
Brief.
on the registry group, attribute group. Most of them are, like, they don't add value, and it's okay to drop.
In a few places, they are meaningful, and maybe, usually it's the same set of places that is a public attribute group.
So for public attribute groups, briefs and notes would still make sense. I don't remember if we allow them, but if we don't, it would not be controversial to add them.
**Josh Suereth** 28:17 Yep.
**Liudmila Molkova** 28:21 Cool. Okay, so let's imagine we've done all of this and.
This will be a giant PR to just change the… the… Templates, because it will affect Pretty much everything.
So we'll need to review it. I don't see a way to break it down into smaller pieces.
Let's see.
And… After that.
Things should get easy. So, updating this to V2 should be trivial. There is some waiver involved for some supplementary things. It's easy.
Check policies will update.
This should be easy.
And this will be another big piece with the V2 publishing.
Off Yeah.
So, we'll probably tackle this one the last… or in parallel with some other stuff, but anyway. Okay, so after we were done with templates, it should be almost trivial, and only after that, I think we should start switching the definitions to V2.
**Josh Suereth** 29:51 That makes sense to me, yeah.
**Liudmila Molkova** 29:55 Okay.
I know, yeah.
Okay.
Cool.
I think we know what to do next, and I think we are blocked on the template stuff.
try to make progress on this, and then it should be possible to divide and conquer.
and… If we can talk more about this, if people have questions, I have another.
somewhat related thing I want to talk about.
**Josh Suereth** 31:23 So did you mention you already had the pull request for the policy part? Did I miss that?
I might have missed that one.
**Liudmila Molkova** 31:30 Yes.
**Josh Suereth** 31:30 Where's.
**Liudmila Molkova** 31:31 You approved it.
**Josh Suereth** 31:32 Oh.
This is your draft, switch to Policies V2.
**Liudmila Molkova** 31:36 Right, yes.
**Josh Suereth** 31:38 Okay.
I just want to call out, I'm really happy with what annotations look like in this. This, this is… I think it's really clear, but I wanted to check with everyone. You know, before we had, like, policy violations for naming conventions and things, be, inside of the Rego policies, and with V2, now they're actually part of the YAML, right by where the definition is.
Which I really like. Like, I think, as a maintainer, I think this is easier for me to kind of track and understand.
what's going on?
Or, like, when I fix it, you know, I can fix it right there at the same spot. So that's pretty cool. We could have, comments and things to know why the exception's allowed and that sort of thing as a maintainer. So I'm… I'm pretty happy with how that turned out there. I think that's much better.
**Liudmila Molkova** 32:30 Yeah, one thing to mention that Where… need to proactively then add this exceptions mechanism to Rego, because now it's not in every policy.
And unless you have it, you cannot exception something out.
Maybe, let's create a bug in Viva packages.
**Josh Suereth** 32:53 Yeah. I think I only added it where we already had exceptions prior. And didn't add it to things that didn't have any exceptions, but I think you're right We should just consistently have the ability to have exceptions so we can. Work with the real world.
**Liudmila Molkova** 33:33 Okay, since we're here, I'm going to jump to the other, Related topic I wanted to discuss.
Moving the templates here.
But… Okay, I'm sorry. Again, I have this change on my other computer. Maybe there is something.
Good, here we can reuse.
So… I have this PR that… that brings the SEMCON templates to the Weaver packages, so that they are reusable.
And we had a bunch of discussions in Weaver, and… Maybe on this call before, that We want to run the registries.
And we want to render snippets, right? So, we have registry for attributes and registry for entities in Semconf.
Maybe we should have registry for spans and metrics.
I'm not sure, given how much markdown and context we have in Semconf, we are ready to switch completely.
And we can duplicate.
But we can also make things configurable, and, thanks to Josh's suggestion.
I made them configurable, so if we look into Weaver YAML, this is, a PR that's based on my local Weaver with some features that are not released yet.
But, we… have this.
New thing here.
When? It's a condition.
And I made some improvements since, but effectively, it's a JQ Boolean expression that should relate to a Boolean.
And if it's true.
we render this template. If it's not true, or if it's missing, if it's null, we don't.
Sorry, when it's now, when it's missing, we render the template.
If it's… if it relates to… False, and we don't render it.
So, and we can have these flags to generate span registry or not, and we can render some stuff. It made me think, like, how do I want registries to be rendered in general?
And I can stop doing this and return back to what we have, but I wanna send, I wanna show you what I came up with.
okay.
I've totally lost where it is in this repo.
**Josh Suereth** 36:32 It's in tests, yeah.
**Liudmila Molkova** 36:34 Yeah, so.
**Josh Suereth** 36:36 And then whatever the test you want to show us, yeah.
**Liudmila Molkova** 36:41 So you see, I do it with AI, I no longer understand what's going on.
Okay, so this is, let's say, my app.
We currently, let's switch the semantic conventions for a sec.
And.
Maybe it should be registered.
Okay, so, we now have registry of attributes and registry of entities, and they are… independent of each other, right? There is app here, and app in entities.
If we… Redo it, I'd rather make the root namespace to be the place where you have things together.
related things.
And here you would have an entities file with the entity definitions.
There will be all the standard snippets we have today, but, generated automatically.
And the most interesting file is this one.
It shows what you have.
And it shows the signals.
And finally, it renders all the attributes.
I think, like, I kind of want… I didn't want to have an individual file with attributes, because we are prioritizing attributes too high.
And them being a blob of text in README.
At the bottom.
Makes more… Sense to me, but that's totally a subjective choice.
I'm curious if you What are your thoughts?
**Josh Suereth** 39:03 So basically, if I get this right, everything's namespaced.
And then we try to… we try to use the signals first and then attributes second, because we're trying to prioritize people to use signals versus attribute. I… I'm on board with the mission of signals versus attributes. I actually like how this reads.
Interesting. Did you run this against all of Semcom and how does it look? That's more my fear because I'm worried we have so much crap that this one markdown file with all this stuff might become unwieldy, but I might be wrong. I don't know. I'm just curious what it looks like.
**Liudmila Molkova** 39:42 I ran it against GenAI, and I liked how it looked like. So, maybe… Well, I cannot really run it against the whole SAMCONF because they're on V1.
Mmhm Yet.
**Josh Suereth** 39:59 Yes.
**Liudmila Molkova** 39:59 Maybe I can.
**Josh Suereth** 40:00 You can try, it should be able to convert to V2, it just… things might be missing, but if you click on, like, a span there, it goes to the actual spans markdown file.
**Liudmila Molkova** 40:11 Yeah.
Oh!
**Josh Suereth** 40:14 Well, it should. Yeah, it should.
**Liudmila Molkova** 40:15 Right, yeah.
**Josh Suereth** 40:16 It probably would have if you weren't looking at, like, a pull request. That might be a GitH Okay, and then this is basically what we had before for spans.
**Liudmila Molkova** 40:25 Yes, that's exactly the same that we had before I first spent.
**Josh Suereth** 40:29 Okay, okay.
And… Cool. I like it. Just my feedback. But I'm curious what others think.
**Daniel Dyla (Dynatrace)** 40:39 I like having a big list. It, if nothing else, makes it easier to like.
Find things, you know, just to quickly search for stuff.
**Liudmila Molkova** 40:56 Oh.
I'm thinking I'll try to… Do it on the whole SEMConf, I'll publish it somewhere.
So that people can look themselves.
And I also want to hear what other people think.
I don't want to make this change in… Semconf now, because it's just too much, we're changing all the templates, and we're also changing the markdown structure, let's stage it, so we'll have this templates in V2 templates and Semconf as a first step, and if we like this.
And we will switch to the shared templates later.
Cool.
And that's all I had.
I'll probably create an issue to… I'll find a plan for a V2.
So that people don't jump onto switching definitions to V2 before we're ready for it.
Bye.
People don't have other topics, then that's it.
Have a great week, everybody.
**Josh Suereth** 42:41 Yeah, this is Michael.
**Shashank Reddy (New Relic)** 42:43 I have a query, actually, so… last… A couple of weeks back, I've raised a PR in a semantic convention report to add an attribute to messaging area that is related to the Kafka.
Messaging queues, so… I've raised a PIA, but that was automatically closed because, there is… there is no maintenance. I think there is maintenance. It is not active. The current project is not active.
So… It was closed automatically.
I've reached… PR, so that was closed. I didn't raise an issue.
Yes.
**Liudmila Molkova** 43:26 It was about class cluster.
**Shashank Reddy (New Relic)** 43:28 ID, yeah, cluster ID.
**Liudmila Molkova** 43:29 Yeah.
**Shashank Reddy (New Relic)** 43:30 Right.
**Liudmila Molkova** 43:32 Okay.
Thank you.
**Shashank Reddy (New Relic)** 43:34 Restart.
**Liudmila Molkova** 43:35 Oh, it's a pull request. Yeah.
**Shashank Reddy (New Relic)** 43:37 Oh, God.
enclosed one citizen.
**Liudmila Molkova** 43:45 Yeah, this friend.
Yeah. Right, we don't have messaging group active, and yeah.
**Shashank Reddy (New Relic)** 43:52 Right, so I've raised an issue today in the community to revive… if we get buy-in from the community, if folks are interested to join us, so that we can work together and get it running.
So, yeah.
I just raised the question that I added you to the CC.
**Liudmila Molkova** 44:18 Yeah, thank you.
**Shashank Reddy (New Relic)** 44:21 So.
So, what I was trying to think is, right now, the messaging group is a little inactive, and, there were a few PRs that are going on, but those are maintenance-related work, but actually, the development is not happening on the… on the instrumentation packages or the or the semantics as well. So from my side, I'm going to work.
for a few months maybe from now to get few features into the instrumentation packages related to the messaging queues, related to Kafka, RabbitMQ, and other ActiveMQ if there are any. So I was thinking to post a message in the community if a few folks who are working on Different companies who are working on messaging systems, they can join us so that we can take it forward with the folks.
Maybe that was the plan. What do you suggest here?
to go forward.
**Liudmila Molkova** 45:21 Yeah, thanks a lot first for, working on this. So the messaging sig.
It was kind of a big effort, and it involves quite a bit of work. I think we were pretty close to… Like, having a good path forward and some clarity, but for some personal reasons, one of the key players need to step down and… then, we couldn't find our way back. And people who initially worked on this are currently heavily involved in some other efforts. I personally won't be able to participate in this match. Maybe, I don't know if Trask can. He's not here today, but he'll be back tomorrow. Maybe he will have some thoughts.
Zhao, who works, on semantic conventions and is still around, he might be interested? I don't know, maybe Armin or Daniel know more, because they're from the same company, but I, I would ask him.
I think this group needs somebody who… Works on semantic conventions, and knows the at least the semantic conventions context.
So that it's just you don't repeat the mistakes we've done in the past again.
on… I would ask these people specifically, Johannes, you mentioned him, he's not in Attel anymore. And as far as I know, he doesn't have time to work on Attel, at least right now. Well, a couple of months ago, he didn't.
I… But, if you're interested in improving construmentations.
What I can offer is, like, if you have some issues, you're identified by instrumenting things.
and you want to fix them in SimConf, I can sponsor this, like, just the fixes based on the instrumentation needs.
If that's, and I, I would even suggest that.
I don't know what others think, but we don't need a group for this. I can offer to review PRs and instrumentation fixes, I think, are high enough of a priority for us to,
**Shashank Reddy (New Relic)** 48:01 That works.
**Liudmila Molkova** 48:02 Two changes, yeah.
**Shashank Reddy (New Relic)** 48:04 That works for now. Like, going forward, if you get any of the same PRs, are you going to work, or, like, do you have any other colleagues who can jump in as well with you?
**Liudmila Molkova** 48:18 So this will essentially be an exceptional process, where… because there is no active SIG, this PRS will be unfortunately closed, but if… like, you give me a heads up that it's coming, and this is a fix for instrumentation, or if you ping me, I'm sorry, this is kind of difficult, but if you ping me or give me a heads up, I can take a look and.
**Shashank Reddy (New Relic)** 48:47 Sure.
**Liudmila Molkova** 48:47 Reopen it, and, like… give you a review.
**Shashank Reddy (New Relic)** 48:54 Got it, got it. That makes sense, Malko.
Thanks. Thanks for that, I think.
**Michele Mancioppi** 49:01 I have a question.
You said you want to fix a bunch of messaging instrumentations. Do you also plan to actually implement span links as they were intended. As opposed to the abomination, we have many instrumentations with an internal span, which is child of the consumer span, which links to exactly one producer span.
Hello, Mila, it's.
**Shashank Reddy (New Relic)** 49:26 Yeah, I actually don't know the issue which you are talking about. The one which you are trying to fix right now is, suppose a producer is talking to the multiple Kafka clusters. Right now, we don't have a mechanism to identify on the instrumentation spans or the instrumentation matrices to which cluster the messages are passed to.
So we are trying to fetch the cluster ID on the instrumentation packages. I added a few PRs to get the cluster information, the cluster ID, so that can be added as an attribute to the spans of producers and consumers.
So, that's the idea here. I'm not sure the problem which you are trying to save, but maybe I can sync up with you and know what exactly the problem which you are trying to… mention.
**Michele Mancioppi** 50:18 It's not a chat.
**Shashank Reddy (New Relic)** 50:19 Yes.
**Liudmila Molkova** 50:21 I think the useful context here could be that if you look into messaging semantic conventions.
**Shashank Reddy (New Relic)** 50:30 Right.
**Liudmila Molkova** 50:33 So, and it's, it's a common pattern in multiple places. We have this blurb of text.
Saying that, okay, this is actually in the process of, active changes. Well, not that active, but.
There was a previous version of this convention that was doing some interesting things, to, Avoid the problem of spam links.
You could only provide at the start time, I think, or maybe some other problem, but essentially, the span hierarchy was weird.
Okay.
And it was implemented in a lot of instrumentation libraries.
**Shashank Reddy (New Relic)** 51:16 I see, okay.
**Liudmila Molkova** 51:18 And then we started changing the semantic conventions for messaging.
And we are now proposing a different pattern and less awful structure. There is a big.
There should be some examples with some mermaid diagrams. Yeah.
The bottom.
Yes.
But it's not what is implemented in multiple instrumentation libraries, and if you fix individual attributes.
First, you would, not fix, like, the compatibility with this version.
Right? Okay. You would still have the spans and a lot of things or for the old version. And usually updating instrumentation would mean you need to switch the instrumentation library to a new convention, like, as a whole, not as, like, individual attributes that you would want that.
**Shashank Reddy (New Relic)** 52:14 Okay.
I mean, by instrumentation packages means, the Java, Java, Python, that, right? So, I'm going to add the attributes to those packages, right?
**Liudmila Molkova** 52:28 Are you looking into any specific instrumentation libraries?
**Shashank Reddy (New Relic)** 52:32 Yeah, java.net.
And Python and Node Node.js. I've looked into them and I added few changes to get the attribute which we are trying to add in the spec added over there in the instrumentation packages so that we get the in the spans which are currently being produced, we are going to get the next attribute along with the existing.
Span attributes, which we have in the bottom of this page.
**Liudmila Molkova** 53:01 Awesome. So, okay, so for Java, probably people in the Java.
**Shashank Reddy (New Relic)** 53:06 Yes.
**Liudmila Molkova** 53:06 instrumentation community would also guide you into the stability, and they they have some mechanisms for for the subten feature.
Dan, do you know for JavaScript, in the country, do we, like, care about the opt-in? Do we have any messaging stuff updated to the new conventions?
**Daniel Dyla (Dynatrace)** 53:28 I'm not sure where the messaging-specific stuff is in JS.
I know we have some instrumentations that have the opt-in, but I don't know if messaging is one of them.
**Liudmila Molkova** 53:41 Mmhm Do we… okay, so we have them, like, are we open to, like, do we have good code owners there? Do people care about messaging in Node?
**Daniel Dyla (Dynatrace)** 53:54 I mean, we have people that care about all of Contrib. I don't know that we have anybody that is, like, specifically focused on messaging.
But… We do have people assigned to maintain specific packages, and we do have people who generally watch Contrib.
I don't know if that answers your question.
**Liudmila Molkova** 54:20 Yeah. So, like, if somebody sends a PR for to update messaging instrumentation, we, in general, would take a look at this PR.
**Daniel Dyla (Dynatrace)** 54:30 Yeah, I would expect it to get looked at.
**Liudmila Molkova** 54:33 Okay, awesome.
Yeah, so then, maybe, Shashank, maybe I would suggest to maybe start with Java, because Trask is also a maintainer on this repo, and he knows messaging stuff, and he is also, knows about, the… this opt-in, and.
**Shashank Reddy (New Relic)** 54:58 Okay.
**Liudmila Molkova** 54:59 For the semantic convention changes, yeah, I can offer help for small fixes, but anything big would probably go through the whole community project.
**Shashank Reddy (New Relic)** 55:11 Sure, sure, sure. That makes sense. As of now, I think just this PR is fine for now. We can see in future if you need any big changes, then we can form a group.
Okay.
**Liudmila Molkova** 55:22 Awesome. I'll update. I'll wrap on your PR. I'll give it a review. It looks good in general. I don't have any concerns.
**Shashank Reddy (New Relic)** 55:35 That would be… Helpful. Thanks. Thanks, Makula.
**Liudmila Molkova** 55:40 Yeah, thank you.
And I hope we can revive messaging. It just made me.
**Shashank Reddy (New Relic)** 55:46 Yeah, yeah, I will actually try from now on. I started a few days back.
**Liudmila Molkova** 55:56 Awesome.
Great!
Then anything else?
And let's call it. Thank you all.
See you around.
**Armin (Dynatrace)** 56:12 Yeah, bye-bye.
