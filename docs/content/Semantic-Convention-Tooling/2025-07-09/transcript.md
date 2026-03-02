SIG: Semantic Convention Tooling
Date: 2025-07-09
Duration: 53 minutes
Zoom Recording URL: https://zoom.us/rec/share/vlqn-Sn3XU_wAO4PGrZKI_WbqljY_bz-P92oODwpLiBPgQCvPyO5vkviZnTmebcJ.HuLxLNwOKMwQTunY
============================================================

## Zoom Recording Transcript

**Josh Suereth** 01:39 Hey?
Sorry.
I'm a bit late.
**Liudmila Molkova** 01:46 Hello! No worries. I joined a couple of minutes ago.
**Josh Suereth** 01:50 I I got distracted trying to write some Jq.
Oh.
**Liudmila Molkova** 01:54 Oh!
**Josh Suereth** 01:55 And I was trying to use AI to help me make the Jq. And it just took me down a rabbit hole of pain that was not right.
**Liudmila Molkova** 02:03 Oh, I'm sorry! It's it's always hit or miss right.
**Josh Suereth** 02:07 Yeah, it's a.
It's like the stupidest thing like
knowing when Jq. Will expand a list and where it expands. The list, I think, is the biggest pain of Jq.
**Liudmila Molkova** 02:23 Oh, and this is where you try all the possible combinations of dot and square brackets.
and hope. It works.
**Josh Suereth** 02:29 Yep.
I can show you what I'm doing, though, because it's related to the topic, I wanted to talk about today, so,
I want to continue schema. V. 2. If that's possible.
Is there anything else folks want to talk about?
Jeremy? I think your read me is the other thing. I wanted to try to get through.
**Jeremy Blythe** 02:51 I'd like to get that in if we can.
Okay, and stop thinking about it, I'll do something else.
**Josh Suereth** 02:59 Let's do. Let's 1st check
triage a bit. I'm not presenting yet at my apologies.
**Jeremy Blythe** 03:07 Nope.
**Josh Suereth** 03:10 Okay, let's see.
I'm going to check the weaver triage just to see if we have any new bugs coming in.
So it's some schema.
New bugs be at the bottom, I assume.
Collector, configuration, generator.
interesting.
Anyone read through this one. Yet.
**Jeremy Blythe** 03:53 Hmm.
**Liudmila Molkova** 04:07 So they want something that generates
not just semantic conventions, but auto collector config files and everything else.
**Josh Suereth** 04:22 What
I think. I get the idea. So there's 2 things that we need to sort out with the collector folk. One is, I don't think their yaml is something that you can
generate and have it interact with other yaml successfully.
Right? So it's not a
we can't item potently throw a processor into a collector and have it just work with whatever's there. Right?
If that makes sense. So we could auto generate a gamble that you use as your foundation to start.
But if you need to change that Yaml in any way, then suddenly your whole pipeline's broken, because there's no like merge capability
right?
But I think what they're asking for is they want us to generate like the Ottl transformations.
Really, schema translations.
We should ask for more information. I think this is this is interesting.
I'm going to. I'm not going to give it a label, but I'm I'm going to call this a
enhancement.
I mean, I'm not gonna like, anyway, I think we should question and ask further information about this of what what they want it to generate.
And they've certainly put in a good amount of detail right? So it's a good issue, right?
**Jeremy Blythe** 05:46 That says to me that there's someone behind. This is a genuine need.
**Josh Suereth** 05:51 Yeah, yeah, I think we. There's a good amount of detail here. What I'm not sure of, though. See a library tool that parses the Yaml and generates hotel collector config with attribute processors for insert update drop attributes. Now.
what does that mean from the semantic convention? Yaml, because we define deprecated behavior right? But the semantic convention Yaml we have today is just a definition.
The diff is where we get like update drop delete. So that's why I think we should ask for clarification on. Is this about the telemetry schema diffs?
It also mentions resource, detection, right and signal specific optimizations
need some more info on what that means. Right? But I did. I think it's cool. We're getting proposals like this. I just think we need to know more what it means.
**Jeremy Blythe** 06:42 Yeah, for sure.
**Josh Suereth** 06:43 Yep, extract required attributes. Does that mean we'd get rid of ones that aren't required.
anyway? Cool. That's fun support for instrumentations
like to be able to reference via an array property on my implementation. The instrumentations that use this implementation
**Liudmila Molkova** 07:12 It seems it sounds to me like the there.
How do you call it? Refinement?
**Josh Suereth** 07:20 It does.
Yeah.
this is something that you're
that makes sense for us. Right? So there'd be a particular instrumentation that says, I'm creating a Mysql connector.
I don't know what this tags thing is.
**Liudmila Molkova** 07:45 I don't know either. Oh, I think
the goal is to somehow, for some reason use it for registry.
I was thinking that it would be useful to host
a refined schema next to the instrumentation, wherever it is.
**Josh Suereth** 08:08 Yeah.
**Liudmila Molkova** 08:10 And then, when you
submitted to the auto registry, it's actually cool to have to require a link to this refined schema.
**Josh Suereth** 08:24 Gotcha, I mean I I'm a fan of that. I don't.
What you're saying is what I think we want to do what this is proposing.
I don't know if it lines up a hundred percent
from what I'm like looking at here. Do you know what I mean? Like what you're saying, I'm absolutely on board with, and we should go forward with this seems to be
similar, but adjacent. So maybe this is one where we respond with what we want to do
like, hey? This is how we're thinking about the problem right now with refinements where, like.net would have a yaml that that defines the refinement. And then, when you post your instrumentation
to the open telemetry registry, you would, you would link to your yaml, and we would use that
as opposed to, I think, because this it looks like they want in.
Is is this defined in the Mysql client? Or is this defined in semantic conventions?
No, this would be the my single client. Right?
**Liudmila Molkova** 09:27 I can reply and document where we would.
how we we see it currently.
**Josh Suereth** 09:35 Yep.
**Liudmila Molkova** 09:36 And the James you can reply with is counter suggestions.
**Josh Suereth** 09:45 Yeah, yeah, that sounds good.
Okay,
the other thing. We have this 2 yaml. So we're back to 2 yaml, which I think you brought up last week. This is not a new bug. Is this something blocking that we should push on right now? Or is this something we should move on to the regular discussion. Topics.
**Liudmila Molkova** 10:07 We need it for the scheme of it, too, but it does not. It's not an immediate burn, and if it becomes one I'll
take a look at this. I don't think it's it's it's a crazy problem to solve.
**Josh Suereth** 10:21 Okay, cool.
I have a feeling I know what might be going on, and it's fun.
**Jeremy Blythe** 10:29 I hate escaping.
**Liudmila Molkova** 10:32 It's worse than that. It's not just escaping. It's like you take the groups
and you remove the the 1st reference thing that says groups, and then you just dump whatever
under each group into a huge structure. I don't think it's a valid yaml, because it has repetitions.
**Jeremy Blythe** 10:55 With.
**Josh Suereth** 10:57 I think the the fact that groups were getting ripped apart is probably
we are taking the groups, Yaml, and we're treating it as an object instead of an array, and it's doing some sort of implicit coercion.
**Liudmila Molkova** 11:12 Only.
**Josh Suereth** 11:13 And the ginger. That's my guess. So like that kind of bullshit it.
Sorry. This is why I prefer typed languages where it'll say, hey? You're using an array. I can't. You know I would expect an object, and you get an error as opposed to. Just let me magically make this work, and then it does the wrong thing in weird ways. Yeah.
okay, anyway, let's let's move on. So let's talk about the readme first, st Jeremy, do you want me to pull up the Pr.
**Jeremy Blythe** 11:41 Sure.
**Josh Suereth** 11:42 Okay.
all right. Get home fever.
Oh, I missed these this morning. Man.
Okay, my bad
new read me.
Alright. I'm not sure what the state of the discussion is. But I was gonna pull open.
**Jeremy Blythe** 12:19 It may be easier not to look at this
in this view, but if you click on the go back to the conversation and click on the link. You'll see it. It's
in the in the 1st comment.
**Josh Suereth** 12:34 Oh, this year!
**Jeremy Blythe** 12:35 Yeah, I was gonna try to resolve comments on this. Yeah.
Well, the thing is that I was going to get to that is that I changed it completely because we did the blog post.
I didn't. Yeah want to repeat everything that's in the blog post. So instead.
what I'm trying to get from this is to refer to the blog post, and actually to to bring in
more of the other things, that more of the other documentation and examples, and how to's and things that are out there
and bring them into this. Read me just as a kind of so this is like a jumping off point to go. Oh, you want to know about this. Here's a how to for that. Here's how to for that. Here's a how to for that. Here's a video. Here's a presentation, here's a whatever. So this one of your comments, Josh, was to have the elevator pitch at the top. So I just stole that exactly from the Tldr in the blog post. That's that paragraph exactly
kept this observability by design piece, and then
the rest of it all the way down is like, how do you install it? What are the main commands and links to all of the stuff.
**Josh Suereth** 13:42 Oh, beautiful. Okay, yeah, I really like this.
**Jeremy Blythe** 13:45 That's it, like really short and sweet. It's a it's like a table of contents to go and find out stuff all over the place, everywhere else. Really.
**Josh Suereth** 13:54 Yeah. Yeah. So we have our elevator pitch. We have a link to places where we talk about the elevator pitch.
and then it's get this thing installed and start using it. Yep.
**Jeremy Blythe** 14:03 Yeah.
**Josh Suereth** 14:04 Beautiful. I will approve this right now. Honestly.
Okay.
You can mark all the the comments as resolved from the the previous one.
**Jeremy Blythe** 14:19 Yeah, sure.
**Josh Suereth** 14:20 By the way, yeah, like, just looking through that, that's exactly what we want.
Cool.
**Jeremy Blythe** 14:26 Yeah, it's funny how I did that. I generated the readme from the
from the talk that you guys did. And then Lauren took that read me and did the blog post. I'm like, Okay, we've gone in a loop.
anyway.
**Josh Suereth** 14:43 That's fun. Cool. Yeah, that I think this will definitely help the getting started experience. So thank you again for that together.
cool and feel free. I know Lawrence on vacation right now. So Ludmilla, if you wanna take a look at it and and review it, please do otherwise. Feel free to merge like sometime today.
**Jeremy Blythe** 15:02 Yeah. And if if you, if you know of any other places that we want to link to, because there are other presentations, or there's other how to use documentation examples anywhere we need like, we can just start plowing them into this, provided we agree that they're good examples or that they're good.
**Josh Suereth** 15:16 Yeah, hold on. My cat's about to knock my USB cable out alright. We're good. We're good. Okay, my, I have a USB hub, and my cat likes to sit on it and rip it out.
Yeah, it's.
**Jeremy Blythe** 15:28 Think.
**Josh Suereth** 15:29 It's
yeah. No, she's she's just like demands attention every once in a while, for some reason, and I don't know why.
okay, so I agree with you like, let's get what you have in, because I think the shape and structure is way better than what we have today for getting started. And then we can just start making changes to it over time. So beautiful.
**Liudmila Molkova** 15:52 And that's it.
**Josh Suereth** 15:55 Yeah, I'll write that down here. Merge it
alright. Let's get to planning. I don't know if you had a chance to look at this, Jeremy. I know that. Ludmilla took a took a look, and we talked about this a little bit in the some kind of meeting yesterday, not yesterday. It was 2 days ago, right
but I have a draft where I was starting to toy around with what it looks like to have 2 versions of semcom. It does not match what Lawrence expectations were from our previous discussion. So I want to show this and say, proposed roadmap. Right?
Definition.
Model files allow new schema resolved.
How do I want to phrase mechanism.
resolved Schema, to use new model and then update forge
policy. Okay, anyway, I I don't know if what? What this, what I'm typing here makes any sense. But I'll show you. I'll show you the basic gist. So
I think the basic. The thing that we want to look at is the end to end test. Possibly.
I'm not sharing the right tab again here. So v. 2 schema
looks like this. So you define. And this is this is the proposal that Lydmilla had last week. So you define your attributes raw just in a thing that's labeled attributes. So instead of having groups with a type, we have specific named sections.
**Jeremy Blythe** 17:40 Okay.
**Josh Suereth** 17:41 It cleans up so much.
**Jeremy Blythe** 17:43 I love it.
**Josh Suereth** 17:44 So much, so good. Good! Call Ludmilla so, and then the other thing is, attributes, uses key, which is what you see in Otlp. So we want the things that are in the model to match what is in Otlp as much as possible. So you have a set of attributes. You have a set of metrics, you have a set of entities. The other thing with entities is, you know, how we have role on attribute now, because we wanted to be able to share and inherit things from groups and all that kind of junk.
this you you define identity, and you reference attributes. You define description, and you reference attributes, which is what we expect the Otlp to look like.
So so it matches better. And the other thing is this is type instead of name, because the type column isn't stolen for group type.
So we can actually start using type which we do use then in span span. Now has a type
which is something we plan to get on the wire
for you to find what your span is. And then the other thing I did was I started using name. And this is actually Group name to define the pattern for the span name. So we can actually get that into Yaml.
And this is what it turns back into. Okay. So this test basically says, okay, let's assume that I am pulling a v 2, and I'm converting it to v. 1 where this is the provenance or the group provenance that I have.
There's a reason that's needed which is when we construct the attribute registry, that registry of attributes. We have to put it in attribute group, and I need an Id to throw it into for every gamble file.
I have a way of synthesizing it which is really bogus and horrible and ugly.
which we can get into. Because I want this group Id to basically become meaningless over time.
or relatively meaningless.
and we can talk through how we do that. But I that's 1 reason I was working on Jq.
Before the meeting.
anyway. So we get we get our regular group. We get our entity group with the attributes split by rapid roll. We get the event all that kind of stuff. If you want to see the details of how I did this, basically, just oh.
we'll do. Maybe entity is the most complicated one. So I'll do that.
There's just a thing that takes your group and turns it back into a v 1 group spec.
Where we construct an attribute array, where we take our attribute, array and convert it into the v. 1 attribute spec. Because again, everything is defined in v. 2,
we give it the appropriate identifying descriptive attributes. And then we construct a group spec with all the defaults for our particular group type.
Okay, what's interesting with this is when I define the v. 2, I can force type to exist. And then, when we generate the stupid like schema validation stuff.
it'll say type is missing instead of group name is missing for entity and all the bogus weird validation we do today. So that helps a lot.
Yeah. And I tried to do.
I try to follow what Ludmila had with getting rid of the empty attribute serializing. So I try to have skim serializing. If everywhere that it makes sense.
identity is required to be non-empty. I haven't done any validation on entity group in v. 2. What I'm actually relying on is that once you convert it into v 1 that validation runs and you get a validation error. It's ugly as sin today. So I want to fix that.
But that's that's the state of the current prototype. Now, what's interesting, the other thing I tried to do was create common fields that we think are necessary across semantic inventions with common requirement levels. And so I'm using the flatten method to kind of share these across everything. So common fields are defined in MoD. And this is basically brief
note with skip serialization. Stability deprecated right?
And deprecated is optional stability is not note is optional because it can be empty.
Brief is not optional.
And then annotations. I found out that we actually are inconsistent with our use of btree and hashmap with our annotations in weaver.
Some areas use Hashmap. Some areas use Btree. When I tried to standardize, I had to go update all of them to btree.
Yeah.
So so for context with Mela, if you have a very small tree, or you don't have access to a good hash. Btree is more efficient.
If you have a great hash and you have enough data. Hash map is better.
**Liudmila Molkova** 22:53 Yeah, I think I used B 3 on members because of it had to be hashable, or there was some.
**Josh Suereth** 23:01 You know.
**Liudmila Molkova** 23:02 Requirements.
**Josh Suereth** 23:03 Btree does not require it to be hashable.
And somehow, I think attributes had hash, map, and everywhere else used btree.
**Liudmila Molkova** 23:16 Hmm, okay.
**Jeremy Blythe** 23:18 A big tree or so sorts, right?
**Josh Suereth** 23:22 Be tree. Yeah, when you that. That's how the bee tree is implemented by default. Yeah, it's sort of thing. So.
**Jeremy Blythe** 23:27 So you'll see the output will, regardless of what you put in. You're going to get alphabetically sorted keys on the output.
**Josh Suereth** 23:34 Yeah.
Speech tree requires a comparison. Hash map requires a hash
is another way to think about it. If you are a type theorist or a what do you call it?
A parametricity person.
**Liudmila Molkova** 23:50 Oh, man!
**Josh Suereth** 23:51 Anyway.
So yeah, this actually starts adding some requirements where things are required. Annotations obviously are optional. I was actually thinking of making. I want to see if we can do this instead of having this be an option where we skip it, if it's none.
just having it be a B tree with a default, and we we skip it if it's empty.
just to make the code look a little bit better.
**Liudmila Molkova** 24:16 Okay.
**Josh Suereth** 24:16 If anyone cares like. If if we'd prefer in rust to have option of a B tree or bee trees that are empty.
I, personally don't care, I think, for deprecated. It has to be an option. But for that one
we could do the same thing. We do like with string here. I think there's some inconsistencies.
I'm getting, too, in the details.
**Jeremy Blythe** 24:38 That is right.
**Josh Suereth** 24:40 What?
**Jeremy Blythe** 24:40 We do it for for vec, right? So we have, we allow, vex to be empty versus office.
**Liudmila Molkova** 24:45 It's a collection, it.
**Josh Suereth** 24:47 And same for string.
**Liudmila Molkova** 24:48 It's just empty. If it's not a collection, then it's an option. If it's an if it's optional.
**Josh Suereth** 24:54 We don't do that for annotations, and I think part of that is about lineage tracking.
But I'm not positive. So, anyway.
**Jeremy Blythe** 25:03 Just one thing here.
**Josh Suereth** 25:04 Go ahead!
**Jeremy Blythe** 25:06 One thing here. So the properly typing everything. So you've got attribute entity like love that absolutely.
It's the other conversation we've been having with, and it's shame she couldn't be here. But with Alexandra about the types. So this it came up to this point where we where
we're having the enums, and I'm wondering whether.
like my suggestion in there, and somebody else has chimed in saying that they like my proposal, so that, you know.
must be great, but it's could we have a top level thing, which is type.
**Josh Suereth** 25:44 Yes, yeah, we we could do type. We could do enum. I I don't care. But I think enum should move as a top level thing, absolutely.
**Jeremy Blythe** 25:52 Yep.
**Josh Suereth** 25:53 That's tracked absolutely agree. That is a possibility. We can go with.
**Jeremy Blythe** 25:57 That would have the other ticket that Alexandra is like.
I think, 2 meetings ago, we said, we need to have more of a discussion on this May. Maybe this is gonna mean that we don't have that deep discussion about that, because
it will all change when this comes in.
**Josh Suereth** 26:11 Yeah, yeah, I think it'll help out a lot. The the main thing we have to deal with right now is we have to have v, 2, and v, 1 be compatible
because we're gonna have to go through a transition phase.
So I,
when it came to attributes. Oh, but the other thing I did was I actually made definitions and refinements be explicit? Oh, that's the wrong attribute. Here we go. So an attribute ref is a refinement of an attribute.
and
you refer to the attribute by its key, which is its pure namespace. And this is where we have brief examples. Tag all that kind of stuff. The reason I'm not using common fields here is, I think there might be a common fields and a common refinement fields
of okay. If this is a refinement, I allow you to override certain things, but also for refinement. One of the things that I wanted to do sampling relevant right now right?
Do we want like a span, attribute ref where sampling relevant shows up on that specifically differently
from attribute graph?
Does that make sense.
**Liudmila Molkova** 27:23 Trampling craft shows up differently.
**Josh Suereth** 27:26 Right. So sampling relevant is something that we could require or have only on spans.
**Liudmila Molkova** 27:35 Right.
So it's not good. Trif.
**Josh Suereth** 27:40 Yeah.
that's 1 of my open, or maybe.
**Liudmila Molkova** 27:47 Maybe so. One thing I wanted to suggest. By the way, this looks awesome. Thanks a lot for materializing this and going this far.
I want to mention. I did a stupid thing. I left some comments on on the commit and not the pull request.
**Josh Suereth** 28:03 Oh, okay.
**Liudmila Molkova** 28:04 And they are pretty minor, but mostly let's nuke everything we can like prefix and stuff.
**Josh Suereth** 28:12 That was gonna be the next question I have. I want to kill this.
I'd love to just absolutely get rid of it, not have it at all. I think prefix is a problem. So let's let's kill it. What was the other thing? Right? These stability requirement level tag tag is the other thing. I think I want to nuke
but stability brief. Those things, I think, will be on a
common refinement. Fields is my plan to move it there. So we basically have common fields that are on definitions which are brief notes, stability deprecated. And then we have common refinements which are optional, brief notes, stability deprecated where you can override to talk about your refinement.
Then
sampling relevant. If we, I think we need to keep it, because that is absolutely that is important, very important for spans.
If you're comfortable, we'll move to a specific span. Attribute ref that has this.
**Liudmila Molkova** 29:23 Yeah.
**Josh Suereth** 29:24 Okay.
**Liudmila Molkova** 29:26 But the other thing I like the bigger thing
it seems so what I'm thinking refinement is the unresolved schema concern
result. Schema does not have refinements, at least not yet, at least not until we're talking about lineage.
**Josh Suereth** 29:47 Yep.
**Liudmila Molkova** 29:48 And we we actually, if we feel this is the good direction we can start.
We can like, do the minor cleanup and merge it, and actually produce the refined schema. V. 2.
Sorry, resolved Schema. V. 2.
And then we can start thinking about how to
do the attribute groups and how to reference them and do all this more complicated things. I don't feel they're they will change how we
results, what what we produce in the results scheme.
**Josh Suereth** 30:25 The main problem we have right now
is, if we, if we come back here to what we define, right
key is the namespace for attribute.
**Liudmila Molkova** 30:37 But on a refined attribute, the key is exactly the same
**Josh Suereth** 30:43 And that's why we have that difference between id and key, like the refinements need an Id. That is not the key, and you need a way to namespace them. Right? So what we could do in the resolve schema is we could have attributes. And then an attribute refinement registry
of okay. I referenced this key. And here's what I changed right.
**Liudmila Molkova** 31:06 So like we would have an implicit or explicit id as well. That identifies this instance. It's the property of the refined attribute.
It's the property of the refined attribute, not the original definition.
**Josh Suereth** 31:21 Yes.
**Liudmila Molkova** 31:22 And then, when we.
**Josh Suereth** 31:24 So so right now today, attributes have an Id, and the key is the name is the name which is the key is separate right.
And so when the basically every id for an attribute definition
would be the same exact, same as the key
for refinement. What we would do is we basically mangle
the place where the refinement occurs with the key.
We could also do it the other way where we have the key, dot. And then the the mangled thing or something. But we need some id way of generating Id that that won't have conflicts.
And so I think it's actually pretty easy to mangle like the the span that it that it's being refined on the id of the span, right? So mangled or refined ids are the id of the place that's doing the refinement dot the id of the thing you're refining.
**Liudmila Molkova** 32:21 It's I feel like we
can at least start by not generating the Id, but asking humans to set one.
**Josh Suereth** 32:35 You could. But I also don't like I could generate that Id
and humans don't have to specify anything at all.
**Liudmila Molkova** 32:45 And I don't know if I want. If we have human specify it, we'll have to
keep that working, going forward. And what if we actually want to like, get rid of it or change shape as we explore here. So.
**Josh Suereth** 32:57 But you know what one of the things I'm thinking about is
When we make registries right now, we have an attribute registry that has all attributes in it. And it's basically all raw attributes and all refinement attributes. Right?
We we could change what that looks like going forward. But I I also don't see why us
having an Id that we generate to do the linking is a problem for users.
**Liudmila Molkova** 33:27 It's not a problem. But the moment the let's say I'm defining Http metrics, right? I want to refine a span.
Oh, sorry. Refine an attribute. Let's say, server, dot address.
And essentially, what I'm generating is an instance of server address attributes for Http. I would love to have this Id, and then I will reference this id in my, let's say metrics or spans.
and then it leaks to me. Anyway, I have to know this Id. It cannot be fully
a pack to me.
**Josh Suereth** 34:07 Yeah, that gets into how we want to do extension. Because that was the last problem I ran into is I basically broke extends completely. You can't use it.
You can't make actually proof.
**Liudmila Molkova** 34:17 That's awesome.
**Josh Suereth** 34:19 Well, also the the thing you're suggesting you. You can't do right now in this proposal.
and I wanted to sort out how we would do it, so I can refine
directly in a signal. So for an entity, I have a refinement. So I don't show this. I think maybe I do in the actual hold on. Do I do this in the test here?
Yeah. So when hold on, where's the test?
Okay? I don't. I don't show it. That's bad. I did it in something else. But anyway, there's a you can actually define, attribute refs in metric
right?
You cannot refine a refinement in the way I've defined it. Now, there's no way to reuse a refinement.
**Liudmila Molkova** 35:08 No way to reuse a refinement. Yeah, it would. It's not controversial, either, that
you should be able to refine inside signal definition.
**Josh Suereth** 35:22 You can refine inside a signal definition, but you cannot refine a refinement from another signal. So if there's a refinement in a metric, I cannot reference it in a span, and I cannot reference it in another metric.
Yeah, so what if.
**Liudmila Molkova** 35:39 We you could refine as a top level thing and say, Okay, this is my attribute, and then.
**Josh Suereth** 35:49 Thing we'd have. So you're saying like in the in here.
Oh, God! Here.
**Liudmila Molkova** 35:57 You could have an attribute that is a refinement of another.
or it's the separate section attribute refinements or
And then you reference that refinement, the common one.
**Josh Suereth** 36:13 I think that'd be okay to add, but we should sort through what that looks like. My current doesn't allow that at all.
**Liudmila Molkova** 36:20 Yeah.
**Josh Suereth** 36:21 And is that a problem in practice.
**Liudmila Molkova** 36:25 It is for semantic conventions. We would need to copy paste a lot. But it's I don't feel it's a
problem that it's an incremental problem to solve.
**Josh Suereth** 36:42 Yeah, the other thing I was thinking about for the semantic invention case. Right now, you have.
You basically define a set of attributes and then, like spans, will reuse them right.
Would it make sense for us to have an attribute set
where I can refine a set of attributes in it? And then I can refer to that attribute set in the signal. So in the Signal, where, I say, you know where I ref attributes, I could instead ref a set
about you.
**Liudmila Molkova** 37:11 So the the attribute groups.
**Josh Suereth** 37:13 It's like attribute groups, but very explicit. Yes.
**Liudmila Molkova** 37:17 And you can reference multiple sets. So composition, yeah.
**Josh Suereth** 37:21 Yes, it's it's not inheritance. It's composition. Yeah.
**Liudmila Molkova** 37:25 Love it.
**Josh Suereth** 37:26 Okay, cool figuring out how to turn that back into v, 1 is gonna be exhausting.
**Liudmila Molkova** 37:34 Oh, we don't need it, though, right? We don't like.
**Josh Suereth** 37:40 The reason we want to turn it into Vivan is, we want to turn it into.
**Liudmila Molkova** 37:45 Resolved the one to make it compatible with call. Gen. And at this point the extension doesn't exist anyway.
**Josh Suereth** 37:54 Yeah, I see. So we could just erase it when we turn it into v 1. For now.
**Liudmila Molkova** 38:02 Right.
**Josh Suereth** 38:03 And then, later on, we can preserve it.
That works. Okay, I can probably make that happen cool.
The other thing that I was working on, and
I don't have a Pr to show this.
Let me come over to here.
So this is this is to make the make way, if you will.
for this change in the attribute registry today.
entities are fine.
but in the attribute registry, if we look at, say, Http or Keats is a better one.
I think Amazon's a good one, too.
Well, okay, this is a bad example. You see, Kubernetes attributes right? This is a description from the group.
Then you see deprecated attributes.
And that's a description from the group of deprecated attributes. If we look at, I believe aws, is the one that has a bajillion.
These are all the groups
right? The way we're figuring out general versus bedrock dynamo ecs eks kinesis is, we're actually using attribute groups.
But I want to make attribute groups not important to make the signals important.
So if you want kinesis attributes, there should be a signal about Kinesius, an entity, a span, a log, whatever. Right?
Same with bedrock.
So all of these group names just don't seem to be providing much value.
So what I was proposing to do was this, Aws will actually have the entire aws set of attributes not grouped by group just grouped by. Here's the non deprecated ones. Here's the deprecated ones for every single thing we do, and the namespace doesn't come from the group. Id. It comes from the attribute id in the group.
and we start erasing the notion that attribute groups need to be used in semantic conventions.
Sorry in the in the generated code.
So when we start moving to this raw attributes, model everything's gravy for us for doing Koja.
Does that sound reasonable.
**Liudmila Molkova** 40:32 Yeah, it reminds me of the discussions we had about Cogen, like how you group by the attribute namespace. Is it the 1st layer? 2 layers, custom
and I I in the Cogen. We grew by the 1st layer wherever we group
by aws and it matches, and again
going forward, we can come up with some customization allowing you to. I don't know, render it differently, but it doesn't feel important to me.
**Josh Suereth** 41:04 Yeah, yep, cool. So I what I'll what I'll do then is I'll update the attribute registry to
basically ignore all groups. It'll just it'll rip out. It'll rip up, rip out attributes.
It'll group them by the 1st dot.
and then it'll secondarily group them by deprecated and non-deprecated. It'll show non-deprecated first, st and then I'll show deprecated, because I still think that that was a change that we requested. Not the Gcp. One. Where's the
Http. Was the one that had it right? Yeah.
where we have Http and deprecated Http, I think this makes a lot of sense to have them split like that for people
right.
**Liudmila Molkova** 41:50 Yeah.
**Josh Suereth** 41:51 So okay, I will progress with that pr as well.
And I think that one needs to come in first.st So.
**Liudmila Molkova** 42:01 Do you need help?
**Josh Suereth** 42:04 If you want do you see this?
Can can you tell what I why, I was late to the meeting.
**Liudmila Molkova** 42:12 You did the grouping.
**Josh Suereth** 42:14 I I'm trying to do a grouping, and I'm trying to erase attributes. And I I used AI to generate crap, and
it's bad. So I'm backing out of it now.
But yeah, basically, I don't think I want to group here. I think I want to flatten attributes 1st and then group, and then we'll be fine.
**Liudmila Molkova** 42:32 Yeah, if it helps by any means. There is the the
Jq helpers which group and erase.
**Josh Suereth** 42:42 Yes, that's not necessarily what I want. I need to flatten 1st and then group one arrays. Yeah.
**Liudmila Molkova** 42:49 Okay.
**Josh Suereth** 42:50 So like. You see how this is a bunch of credit, what what I was doing. I'll just show you
if you do. Dot bang dot attributes. You almost get what you want.
But see how the same ideas repeated with the attributes.
Hold on! I'll make this more realistic for what this is. This is from Namespace one. This is from Namespace one.
We see how you're ending up with 2 2 groups instead of.
**Liudmila Molkova** 43:19 Hmm.
**Josh Suereth** 43:19 Instead of one, where all the attributes are nested underneath it.
**Liudmila Molkova** 43:24 Yeah.
**Josh Suereth** 43:25 That's what I've been fighting.
**Liudmila Molkova** 43:28 I see? Yeah.
**Josh Suereth** 43:30 Yeah.
**Liudmila Molkova** 43:30 And if if you it seems way in the middle of it, but if if you want me to go and update the registry and find it
and focus on the rest part that that I can do this.
**Josh Suereth** 43:47 Okay, that that'd be fine. Yeah. I I didn't it? Updating the registry actually, isn't that hard? So if you want to take over that. That'd be awesome. Yeah.
Sorry. The hardest part, I should say, is the Jq. Part. The rest of it. Once you get Jq. Done the rest of it, I think, is kind of not not that hard.
I.
**Liudmila Molkova** 44:06 Like the challenge of it. I hate and love it at the same time.
**Josh Suereth** 44:10 Yes, yeah, I I feel you. I feel you okay. Now, to come back to this discussion here. I think
my proposed roadmap was. And this is where Laurent had a different opinion.
First, st we update the
this file so that we can start using it when we define some conf and semantic conventions.
or that code, like people who are writing semcom can use it. Then we update the resolve schema to have this as an output. So we 1st we figure out what we want people to. Input right? Then we figure out what the resolve schema is based on that. And we clean up that resolve schema as much as we possibly can, and then we gut the core where live check policies, rego policies, all of the above start to see v. 2.
I think that
that's my current, proposed path forward. Laurent was assuming we would do the the right hand side 1st
and work our way backwards.
I yeah.
**Jeremy Blythe** 45:15 It's hard to visualize the right hand side if you don't do the left hand like.
**Josh Suereth** 45:20 That that was my.
**Jeremy Blythe** 45:21 You can.
**Josh Suereth** 45:22 Yeah, that's my thinking, too.
**Liudmila Molkova** 45:25 But I I kind of think that those 2 are parallel to some extent efforts.
So we already have like, if you number those, 1, 2, 3 we already have in your Pr. We have 2.
**Josh Suereth** 45:42 Do we.
**Liudmila Molkova** 45:44 Pretty much right. We we have everything except lineage for the result. Schema.
**Josh Suereth** 45:51 In my Pr. I'm converting the model files into the old thing and then doing resolution. I'm actually not doing any of the resolution or the resolve schema stuff, and I'm not sure I cannot create resolve, Schema, with the new stuff I would have to translate backwards. I only have it going one direction.
**Liudmila Molkova** 46:12 I see. So oh, like what I'm going to is
that all the complex problems are in one.
**Josh Suereth** 46:20 I think many are. Yeah. And that's why I'm focused on that first.st Yep.
**Liudmila Molkova** 46:23 Okay. Yeah.
**Josh Suereth** 46:26 I beat your head against the wall first, st and then break a hole in it, and then everything's easy from there, so like, take the hardest possible problem, wrestle that to the ground, and then move forward right.
**Jeremy Blythe** 46:38 What is the scope of the v. 2. So there, there are other things that are
so. One of the things that
makes it like some live check. Things, for example, impossible right now are conditionally required, is expressed in natural language
as an example like, do we want to try to fix that.
**Liudmila Molkova** 47:06 Like on on metrics, you mean metrics are requirement level is not formalized.
**Jeremy Blythe** 47:14 You know, I forget where it is now. You can specify a conditionally required, and then people can type in whatever they want as an English.
**Liudmila Molkova** 47:20 Oh, I see!
**Jeremy Blythe** 47:22 Oh, well, if you've got this one, and it's a Tuesday that means that you have this one.
**Liudmila Molkova** 47:27 I see.
**Jeremy Blythe** 47:28 Yeah. And so we don't have
is this, should we include things like fixing that in the scope of v, 2. So we have a v, 2, and not a v, 2.1 later
is that expanding the scope too, much.
**Liudmila Molkova** 47:44 My feeling that we don't know what to how to formalize it yet, which probably means it's 2.1.
**Jeremy Blythe** 47:53 Okay.
**Liudmila Molkova** 47:57 But it's a good question. What's in the scope? I feel like the resolved schema.
and and and like the the better result, schema schema result schema. V. 2. Unlocks.
Multi registry.
8.
Unlocks our version properly versioned fully.
Described schemas right? All the tooling changes.
And actually you it makes it way easier to do live checks in the long run.
because you you can easily get somebody else's schema that you cannot easily get yet great.
**Josh Suereth** 48:46 I agree our target should be getting resolved. Schema? Yeah.
I guess the question is, do you, Ludmilla? Do you think.
should I start focusing on how to convert existing groups into the new schema for resolve schema now.
or should I focus on like, let's work out the issues of how? V, 2 goes back to v. 1. First, st
like, what? What priority do we see there? How to take? v. 1 into v. 2. Or how to take v. 2 into v, 1. That's the difference between one and 2
is if someone has something defined in v, 1, can I create our V 2 out of it
would be number 2.
**Liudmila Molkova** 49:28 Think you you can. But what's more.
regardless of the what we target first, st we'll need to do all of them eventually.
So it doesn't matter.
**Josh Suereth** 49:43 Okay, yeah, that's fair. I I think I still am finding in my my feeling. Is that doing one? I'm learning a lot about what that eventual model needs and the full requirement set. So when we do resolve schema, it'll be as minimal as possible.
Right?
So my plan is to get this into a mode that we're comfortable with, and works and submittable.
and then start working on 2.
But I can do a little bit of both at the same time. It's just, you know.
I'd prefer to have a focus. And and to me, unless you have, like major concerns with that this path I'm I'm gonna stay with the same focus. So.
**Liudmila Molkova** 50:29 And no major concerns. I'm all I'm saying that. Yeah, actually, you already have 2 pretty much.
**Josh Suereth** 50:36 I think I think we we made a lot of decisions where we could go implement to. And it's not going to require hard decisions. Yes, agree with that. Yep.
cool
I don't have anything else. We only have like 3 min left, but I think we could end early for the 1st time ever, if
unless someone has something they want to talk about.
**Jeremy Blythe** 51:01 Did you see that you can already do the use? The annotations in the live check.
which is really nice? Somebody chimed in on slack going. Oh, I'm going to learn Rego, so I can do that now, which was seems interesting. The sad thing is, Rego doesn't have
a concept of an int or a double.
So while you can do the check, the check is not
my dog. The check is not perfect
in that. If it ends in dot. If if it's like 1.0, that's interpreted as an Int.
I don't know how to get around that. So anyone who's like super Rego.
**Josh Suereth** 51:46 That's another fun challenge
that matches our otop model where we don't care if it's an inch or double either, though. So like, I,
yeah.
**Liudmila Molkova** 51:59 So we can probably say we don't care.
**Josh Suereth** 52:05 Yeah, if we do have to care, that's gonna suck, that's all. I'll say.
**Liudmila Molkova** 52:11 We can care in the rust code like it would be ugly to care about some things in rust and some things in Rego, but it's probably inevitable
if we need to. Yeah.
**Jeremy Blythe** 52:25 Anyway, it was just an amusement.
**Josh Suereth** 52:28 Yeah, I did. I did see that your your bug update of we can check for whether there's a period.
**Jeremy Blythe** 52:37 What I did.
**Liudmila Molkova** 52:37 Well.
**Jeremy Blythe** 52:39 I did, but the sprintf takes off the dot 0.
Oh, when it's a 0 nice. Yeah.
So the sprint doesn't work.
If if it has training zeros.
**Liudmila Molkova** 52:55 Let's hope there are no exponential things there.
**Jeremy Blythe** 53:01 Anyhow.
**Josh Suereth** 53:02 I think what it means is you can. You can express things in the annotations.
**Jeremy Blythe** 53:06 Anything you want like ranges and things, which is what this person was talking about. They want to express like a range and say, well, it's an error, if it goes, you know.
beyond, if it's a percentage and it goes beyond a hundred. That's
maybe that's meaningless. So I want to have that to be showing up in live stream.
**Josh Suereth** 53:24 I think that's this is a huge win. Honestly, the fact that, like
you can define your own conventions
and then your own policies. It's like exactly what we want Weaver to do. So I think that's I'm excited. People discover that because it like
it reinforces that we are building the right set of things. We just need to get the friction down. Yeah.
cool.
**Jeremy Blythe** 53:45 Here. I use the 3 min for.
**Josh Suereth** 53:49 It's okay. We'll see.
**Liudmila Molkova** 53:51 Yeah.
