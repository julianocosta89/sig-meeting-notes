SIG: Semantic Convention Tooling
Date: 2025-07-16
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Liudmila Molkova 00:01:19 Hello! Hi! Everyone!
Matthew Hensley 00:01:23 Hello!
Liudmila Molkova 00:02:52 Okay? So while we are waiting for Joshua, let's start some triage.
See? What's going on.
okay, this is semantic convention tooling triash. We haven't looked here in a while. I forgot what we have here.
think we don't have a link for new issues. So they went.
Year.
Oh, interesting.
Think I can close this now.
Okay, let's use this opportunity to close issues.
Yay.
can we close something else?
Add a filter record version that reboot was deprecated. Did you know what we can do it with annotations.
Jeremy Blythe 00:04:48 Annotations, everywhere.
Liudmila Molkova 00:05:10 Yay.
pulling the source of registry funds.
Oh, by the way, I think we should remove it from this board then.
Oh, wait!
Yes, we can move it to improve Yano schema.
Well, it's already improved.
No, no, there is no link.
Okay, I don't see.
Okay, are we can talk about fever. So anybody has a something they want to discuss today.
Jeremy Blythe 00:06:57 There were a couple of pull requests.
James, someone.
I was gonna bring up because I'm wondering whether these things should be annotations.
So there's this one that's at the top. There, introduce name spaces.
And then there's 1 further down which is similar thing.
So it seems it seems this. And yeah, that guy.
Liudmila Molkova 00:07:46 Which one.
Jeremy Blythe 00:07:47 The aggregation parameter metrics can be defined. 8, 4.
Oh, yeah.
Liudmila Molkova 00:08:06 Oh, this is part of some semantic conventions. Pr. We discussed some. Oh, sorry.
I not sure what's going on here, so I think we need to talk about it. I don't understand what namespace is. We hadn't have a notion of namespace.
and we never talked about it, so I don't know how to review those Prs because we never defined what it is. So the the context James works on a bunch of per requests and 70 conventions to create, let's say, an event registry or metric registry.
Jeremy Blythe 00:09:12 Okay.
Liudmila Molkova 00:09:13 And somehow he progressed from just having a registry of events to registry of namespaces. But I'm a bit lost there.
so I think we would need him to come and share his vision and namespaces. And why like? Why would we have them? What are they.
Jeremy Blythe 00:09:44 Right. It seems that this is this feels like information just to drive the documentation I don't like. If you look at the implementation of it. It's not weaver's not really adding anything.
It's just like data that it can then be available to the documentation templates.
And so I feel like. And the other one the aggregation. One has also been implemented in that same sort of way where new new fields have been added to the schema for something that is then just a yaml block.
which is so in both cases that feels to me. That's what that's what annotations are for in the you want to. You want to define something in the model in the model files.
and you want access to them in the Doc generation or the code generation.
But Weaver's really just passing them through.
And so the contract is just with yourself about between your own templates and your own model, and there's nothing that we? There's no resolution to be done or no.
Liudmila Molkova 00:11:05 I see. So what you're saying. So let's say the bucket boundaries for histograms. You would suggest to use them for to use annotations for them.
Jeremy Blythe 00:11:16 No, this is this one. I don't, so I don't.
I think you you either go one way or another. If the bucket boundaries are something that should be specified clearly, because there's like some good meaning to them that we can check on. That we can clarify is correct. That weaver will actually add some benefit to.
Then I feel like it should be defined in a typed way. So that so we understand what bucket boundaries are.
Liudmila Molkova 00:11:44 The way that the Pr has been implemented.
Jeremy Blythe 00:11:48 And if you scroll down a bit, James's comment is like, Yeah, I didn't in. Oh, in the Pr. I think you're in the issue.
He was like, Oh, I didn't do it like that. I just used the yaml block. And I'm like, Well, okay, if you're just going to use a yaml block. You can put a yaml block in annotations.
Do you see what I mean?
Liudmila Molkova 00:12:14 Not yet.
Jeremy Blythe 00:12:15 So Josh, ma'am, yeah. So if we're going to specify, yeah, if we're gonna specify things that have, like, you know.
because we ran into this with value type just recently. Right? It's the same. It's a similar kind of argument.
Either it's part of the spec, and it should be.
It should be typed. It should be properly typed in the spec, and readers should understand what a bucket boundaries are, so that it can do you know proper checking against it.
Check the syntax is right. Check that they're valid with all sorts of all sorts of things. We can have live checks with them like the whole thing, or it's just an annotation. I don't think there's, but I don't see the value in adding a new field which has the same.
It has the same effect as just having an annotation.
which is the way it's been implemented.
Liudmila Molkova 00:13:16 So it's, it's actually a good question. Okay, so what would be the reasons to have it as strongly typed? Would we live? Check it.
Wow!
We would not, for like, it's not a violation. But if I'm testing the quality of my instrumentation, if I just run like implemented instrumentation, and I want to make sure it follows semantic conventions.
I might And I can still use annotations for the live check.
Depart packet boundaries are not part of stability guarantees, I think, shouldn't be so I don't know what would be the good reason to put it in the Kima.
Maybe it could be there.
But okay, I don't see a problem with having it in annotations. But you're saying the the concern is that it's implemented in some
Jeremy Blythe 00:14:32 Yes, what's been done here is a new. There's a new thing called an aggregation has been made, which is a new field.
But that aggregation.
Everything under parameters is just a yaml block.
So under parameters.
Liudmila Molkova 00:14:53 Hi.
Jeremy Blythe 00:14:54 Like that which, so I may as well have an annotation.
Liudmila Molkova 00:14:58 As okay. Yes. Then it definitely sounds like anundation.
Jeremy Blythe 00:15:02 Yeah.
Liudmila Molkova 00:15:02 Okay. And it seems there is already a discussion around it.
Jeremy Blythe 00:15:07 There is. Yeah, but I I guess I'm we need to like conclude, I suppose otherwise.
If someone's gone to the trouble of making a Pr, they probably like feel like this is a really important thing to have right. That's my and I don't.
I didn't. I didn't. I was. I felt, in the position to say, Well, yeah, you can. You can do what you've done with the annotation.
but it's but is that? Is that really the?
Is that the right answer?
I guess I don't want us to fall in the same trap that we fill in with value type right where we went. Oh, this is a thing we should have, and we went to the effort to do it.
and then backed all the way out and went. Do you know what this is? An annotation thing which is totally fine?
Don't do that again and again and again.
Liudmila Molkova 00:16:09 Yeah, I I really, I feel really that was special. I mean, I would in general, we should probably develop some mental model of when we put things into the annotations versus in the schema. Right? I don't feel we. We have this litmus test.
Jeremy Blythe 00:16:30 Maybe we need some guidance that is in the in the the developer notes.
Because if you look what James said, he said. Oh, I wrote this according to the notes, developer to the notes, weaver, or something.
So I think perhaps that's what we we need that says to to explain more about what annotations are.
Liudmila Molkova 00:17:31 So I highlighted something around that top level structured property. It's something essential, right?
But how do we express it?
Jeremy Blythe 00:17:46 Yeah, that's the challenge.
I think, mixed in with this. There's also There's also the trap that I fell into as well, which is tying the internals of weaver very specifically to what happens in the semicond project.
So I, when I started doing live check, I started writing stuff, assuming that there were namespaces that were separated by by period characters, and I had to learn a whole bunch of code in there.
Then Josh and the Ron set me on the right path, which is like, actually, do you know what?
That's not part of the that's not part of the standard. That's just something that the Simcom group have decided to settle on this thing.
And so in that, in that.
maybe in that guidance document, we need to have something about that as well.
Liudmila Molkova 00:18:50 Yeah, definitely. But that's the if if you can create an issue about this. So we don't forget. Yeah.
nice. I'm I'm just trying to figure out what we would do for this specific one.
And so the reason we moved valued type donations was because it's essentially in an important detail.
You can change it. Nothing should break.
Paratha doesn't care where the histogram boundaries you can change it.
It would result in the in dashboards actually being broken potentially right alerts, not dashboards, alerts, or you may use precision, but you probably wouldn't change histogram boundaries in the way that it will be broken. The exponential is to grab while there is this nonsense.
so let's try to summarize this So we put properties.
It's something that goes over the wire.
It translates into something that goes over the wire right?
Oh, done! It's something you that instrumentation sets 8 should not be breaking. Well, it should affect telemetry in the ways that it would be broken.
Oh, hi, Josh, hey? Sorry.
Josh Suereth 00:21:19 I'm late.
Liudmila Molkova 00:21:20 Yeah, we are struggling. We're trying to define what is the litmus test to put something into annotations versus the structured property.
It seems it boils down to something being essential enough.
For the consumers produced by instrumentations.
and it should probably go over the wire. If it doesn't go over the wire.
It might not be there.
Josh Suereth 00:21:57 Yeah, I'm I'm a fan of it has to be an otop.
And then it has to be something that impacts stability.
Or it should be something that impacts stability like the whole discussion about int versus double.
Since we have defined our model where that should not cause problems, that is why it should not be modeled directly, because it is a optimization detail for passing data, not a actual hard requirement for streams.
and the fight to not use integers at all. I don't know if any of you guys were here when we defined metrics that that almost succeeded, but kind of lost by like 1 1 strong voice.
So us, starting to require int versus double would be horrendous, in my opinion, from from that right. But that's an example. Similarly.
Histogram boundaries is a fun one, because you.
Liudmila Molkova 00:23:03 Exactly.
Josh Suereth 00:23:04 Implementation. Yeah. But we don't want.
we need to figure out when histogram boundary changes would cause errors. Our recommendations today and the assumption in open telemetry for exponential histogram is that bucket boundary changes should not break you.
But this requires you to interact with histograms in specific ways. For example, always using percentile functions or rate functions or interacting with the sum right?
That's that's how we recommend interacting with histograms. And then it's non-breaking to change buckets in Prometheus. People do shenanigans, because you can rely on buckets being some cumulative sums of like up to a certain point.
and like there was just a recent collector, Pr.
To try to drop buckets from a histogram as it flows, for example.
which would that be considered breaking semantic inventions if people use histograms the way we recommend it's not so. Should that be an annotation? Or should that be A specific thing in in open telemetry? I I'm a fan of that is a hint that's an annotation that helps instrumentation. Provide a default bucket boundary list. But we want to encourage people to have flexibility there, right? So that second lit litmus test is from from my perspective. Is, does it break the our data model and our conventions around stability?
That was long winded addition. You may have already said that, but I'm just adding that one.
Liudmila Molkova 00:24:54 No, that that was a great explanation. So yeah, market boundaries even quote advisory parameters. Users can change them.
It's still useful to record them, because it's part of cogeneration and part of the expectations we show. For the consumers. And what is the range of this thing?
and they're optional. So this is another thing that potentially makes them optional in a sense that instrumentations do not have to provide them.
Another thing that makes us less essential for the both instrumentations and consumers.
so our consensus it seems to be it should be an annotation.
Okay. Now, going back to the pull request ballots.
The by the way, this thing is completely unstructured, right? And when we define how we're well, we need some way to define how we record, and bucket boundaries in the annotations we want to have lose but fixed syntax, and it will be used by the Cogen.
We need to express the schema somewhere. Currently, it's just the the follow, the example and semantic conventions.
Maybe let's solve it some other day.
Jeremy Blythe 00:27:14 Oh, I see you want within the same Conf group. You want your a schema for how you use annotations.
Liudmila Molkova 00:27:24 And it can be part of semantic convention schema. It shouldn't be part of the weaver per se rust models, but it would be useful to have a Json schema defined first.st
Jeremy Blythe 00:27:38 Right? Interesting.
Josh Suereth 00:27:41 Yeah, weaver could support the Json schema even. Hey? Your annotation should match the schema if we want to make it really complicated and fun.
But yeah, I, yeah, let's do the the minimal thing that works that makes sense if we can. So using annotations getting Cogen to work with this defining bucket boundaries via that it it I don't see a world where that's going to be a horrible long-term decision.
You know what I mean.
Liudmila Molkova 00:28:19 Do something.
Josh Suereth 00:28:20 We evolve in the future. But yeah.
by the way, I missed the the talk on the previous Pr. And I don't see notes. Where did you add all the notes of things you discussed to the Pr. Itself?
Liudmila Molkova 00:28:46 We didn't actually talk about it.
Josh Suereth 00:28:48 Oh, okay, okay, cool.
I'll wait. Then.
Jeremy Blythe 00:28:57 We talked about it enough to realize that we didn't understand what it was about.
Josh Suereth 00:29:03 I. I think I understand the context behind it.
It's okay. Great that I can. Yeah.
Liudmila Molkova 00:29:14 If you want to share the context, you can start talking. I will finish writing my notes. But they I probably know half of this context.
Josh Suereth 00:29:22 Yeah, sure. So in in semantic conventions, and with Schema v. 2, planning one of the proposals that I had, and that I'd like to execute on in semantic convention code. Gen.
And just generally is removing the attribute group like name spacing that we use so inside of semantic conventions today.
We render like the Http semantic conventions and we group them by attribute group as a namespace. So there's like, you know, Http, dot foo http dot bar. Okay?
In the docs, and there are brief and description for those attribute groups, and those get rendered in semantic conventions.
The brief and the the notes are usually just like this is the group name they're not like really used today. And so before they get really used, I wanted to gut them get rid of them.
And so we would have automatically generated attribute like names, and we can control the the rendering and the format of attribute names. However, we want, but there is no such thing as a namespace of attributes. We're getting rid of it.
Okay?
similarly, I think, like, you know, entities or groups and stuff. If you look at the V 2 schema that Ludmilla proposed, this is kind of in line with that. I think it's it's it's going this direction towards. We have a namespace for attributes. We have a namespace for events, we have a namespace for entities, we have a namespace for metrics, we have a namespace for spans.
We don't have a giant group namespace with all this crap in it. Okay.
that takes away the grouping mechanism for attributes. We have to figure out how to do like shared attribute groups and that kind of stuff. I think this proposal is around the V 2.
Where the idea is you would have a namespace because he even mentions v. 2. You would have a namespace where you could put information to generate Markdown around that namespace. Right? So I could say, okay for HP Sem conv.
I want to have a namespace for HP. Sendcom, which is just here is header information I need around. Http.
here's footer information I need around Http, and then we can plop in the signals and things in Http in this one big document.
right? So this this is, this is like.
how do we define in Yaml the content and things we want around for Cogen?
One of the things that I think Ludmilla had asked of of James. For this Pr. Was, is it James? Or it's Thompson, is it James Thompson? Is that right?
Liudmila Molkova 00:32:24 Thompson.
Josh Suereth 00:32:25 Yeah, I I like to use people's names, but I sometimes get them wrong. So apologies if I do that, anyway. One of the things with? Millie asked to James was like, Hey, before you remove everything from like event in semantic convention and create this automatically generated document with all the events we have content in the markdown that needs to get into the Yaml in some fashion the most significant content in the Markdown is.
Hey, this whole file is is going from Rc. To stable. However, there's a de facto stable version of version Xyz of Semcov that you should use by default, and we made a bunch of breaking changes from that version. And here is the opt-in flag to go from version A to Version B to release this piece of the pie.
And I think James is basically saying cool, I'll make this namespace thing. That's where we'll put the header that says this whole set of stuff is under this opt-in version now.
and you should. If you're a semcom author, you should stick to version. Foo.
do you? Wanna do you want to show one of those examples with Mila from, like the database. Some conf.
Liudmila Molkova 00:33:43 Oh, sure!
Josh Suereth 00:33:52 Yeah, so it's it's basically, where and how do we put the that? Oh, the bit at the top, actually.
Liudmila Molkova 00:34:00 Right.
Josh Suereth 00:34:02 Where and how do we put this warning right?
Liudmila Molkova 00:34:07 Yeah, I feel like we didn't talk enough about how we see the future.
Right? So imagine. We have a let's say, metric register, a span registry.
Imagine I'm a user.
I'm exploring open telemetry. I/O, right?
I'm going here. Semantic conventions. Here is the registry of let's say Spence. I open it. I click on something, and here we go. There is. I don't know database spend here.
We let's assume we put all the context into the database pan. Here as an instrumentation as a user, as an instrumentation author, do I have enough of the information? If I just look into one span definition.
No.
right? I I'd rather know. Okay, this. There are database, semantic conventions, and you know there are a bunch of spans, metrics, maybe events defined for them. And okay, they use this database attributes.
maybe there are some database entities in the future.
I I need the central place like there should be a readme that points me to additional places.
Do you see what I mean?
Like the the semantic conventions is a thing that consists of false signals. It's not.
You cannot implement one signal. Well, you can, but you probably shouldn't.
And if we take what we have in this markdown and put it in Yaml like here.
with headers, footers, content.
What we do we take content from Markdown and put it in Yaml. We don't make it accessible, or we make it accessible to code generation. But it wouldn't care.
It's not the information you would use when you're generating code.
So I'm I'm not. I'm not. I don't understand this namespace vision. I understand that we can take all we have, and we can great fake namespaces in in Jq. But why they should appear in the Yamo.
Josh Suereth 00:37:08 Yeah. I agree with your assessment I was 1st trying to describe. Why I think this exists.
Liudmila Molkova 00:37:17 And.
Josh Suereth 00:37:18 Problem is trying to solve. And I think that, like, you're absolutely right, we should be asking, what's the right way to solve this problem. Not necessarily. What's the 1st way to solve this problem?
So I if if we look in v, 2, I I kinda I'm not a fan of what this looks like in v. 2. Right now, for a lot of the reasons you just mentioned. I. And to me part of it is, I don't know if weight we've been stabilizing will be a namespace by namespace thing.
So this header around like these things are stabilizing in this document right now we're stabilizing namespace by namespace. But what if we do it for like a sub namespace, or like a portion of a namespace? We don't have a vehicle to handle that. This doesn't give us a vehicle to handle that. And so the question is, is it worth building this out, adding all of that, having that as something we have to maintain going forward.
whereas embedding things in Markdown. For now is working okay? And yes, we don't have registries. We don't have everything generated by Yaml. But when we move to that we want to make sure that it will continue to work for our use cases going forward.
So you know, we have something that works now. We don't need namespaces. It just prevents us from having registries for events. Right? Go what.
Liudmila Molkova 00:38:48 Sorry your microphone is. I can hear you, but you're very noisy.
Josh Suereth 00:38:54 You know what it is, hey? Is this working now? Can you hear me now?
Liudmila Molkova 00:39:01 I can hear you, but it's still.
Jeremy Blythe 00:39:04 Heard a lot of noise on it.
Josh Suereth 00:39:06 A lot of noise. Huh?
Jeremy Blythe 00:39:07 Like you were like, you've got a broken.
That's true.
People.
Josh Suereth 00:39:12 Alright, one second.
Jeremy Blythe 00:39:14 Like static noise.
I guess the other thing with this sort of documentation make putting the documentation into the model makes it complicated when you're doing when you want doing.
you've got a dependency. So if you've made an enterprise level model.
and you're making reference to the semcom model.
and I'm just pulling out an attribute or a span, or like I'm you know, I'm just picking out bits that I want, and I'm changing some of the.
So I'm making a reference, and I'm changing something like the requirement level. Or what have you like?
Do I want to go and grab the documentation or not like a kind of there's a complication there as well. Right?
So.
Liudmila Molkova 00:40:51 Can. Can you elaborate?
You're you're saying that what we have today is more complicated because you need to go and get some documentation from some random page, and mark down.
Jeremy Blythe 00:41:16 I don't have an answer. I'm just saying that what we have today is complicated.
because, like, it's just in the Markdown, so I can't go find it.
and if I want to put that in my documentation like, I don't have access to it.
If I've pulled in the animal, then I've got the I've got the potential to have it.
But then, how do I reference?
How do I then go and reference it.
Liudmila Molkova 00:41:41 I see.
Jeremy Blythe 00:41:42 Right cause. I just want that one attribute from the whole library.
Do I need? Do I want the warning about such and such that might not be relevant. So how do I know whether it's relevant or not like I don't know.
Liudmila Molkova 00:41:56 So let's say, if we look here, there are cross links.
So let's say this database query text.
And to understand it properly, you need to read this mark down.
Jeremy Blythe 00:42:15 Yeah.
Liudmila Molkova 00:42:15 And you might or might not have an easy way, we we should have an easy way. So it's an absolute URL. And you can actually go and read this Markdown. But when you let's say generated in your registry.
you would rather have this section somewhere in Yaml. So it's easier for you to reference it or to.
and I'll show it in some way to some extent.
If it's an absolutely early, you're fine.
there will be things that are external to semantic conventions that we reference.
And there are just Urls on the Internet.
Josh Suereth 00:43:09 Can you hear me now?
Liudmila Molkova 00:43:11 Yeah, nice.
Josh Suereth 00:43:13 Okay, that's better.
Fun. Hey?
I still think the there's 2 problems here. One is, how do we auto generate documentation? That's cohesive and consistent from Yaml.
This one makes some progress towards it, but it doesn't solve. I think the core issue, which is, how do we take a batch of things and mark them for stabilization together with headers around them.
which is a slightly different problem.
Because, again, I don't think this does not unblock the event. Registry Pr.
That James has.
Liudmila Molkova 00:44:02 It, it raises more questions.
Josh Suereth 00:44:05 Yep.
Liudmila Molkova 00:44:07 So I think what? Here, the, the actually the namespace here. It's a document. It's not the namespace. It's a document.
And that this as a document. It makes sense. It has had their food. Their other things.
Document has stability. Right? That's totally fine.
The thing is.
do we need to have a document defined in the Yaml. Why, we cannot just write it in Markdown.
And the other question is, I I'm hesitant to look closer, because I don't understand what we are. What does the proposal look like here, or in semantic conventions? What are we trying to achieve with this right? Is all, all the registry.
It sounds like we.
We are having discussions between ourselves. It'd be useful if we had a discussion with James, and he could show his vision so we can understand what the problem he is trying to solve.
I can leave a note on the Pr. And we can.
And now ask him for his thoughts.
Josh Suereth 00:45:49 Yeah, I think I think a little bit with with James we should start encouraging him to write up like the direction he wants to take things in like a proposal in an issue prior to opening Prs and then bringing those to our attention via just like, add it to notes and that sort of thing, because I think we want to avoid him doing a whole bunch of implementation for things that are directionally, not where we want to go and see if we can see if that helps here, because I I like what he wants to do at the high level, but like the actual steps I tend to disagree with so.
Liudmila Molkova 00:47:24 Okay. Josh, do you wanna leave a note? Should I leave a note either way? Works for me?
Sorry, not the node, but comment on the Pr.
okay, I won't do this.
Okay.
So we talked about those 2 this. I left the comment for this one. I'll come back to it.
I promised last week. I think that I will do something similar, but for attributes that I will get rid of attribute groups. I didn't have a chance. I'll try to do it today. And maybe it can be useful for James to see that the tape space we can fake it.
Okay, so let's move on to the schema. V. 2.
Josh Suereth 00:48:29 Yeah, we only have 10 min. I don't want to take too long, but just a reminder that we're experiment with this. I didn't have a chance to do much work. Since last week I've mostly done thought.
but yeah. So the the premise here is this, this is adding a version, 2 of the schema.
that version, basically, instead of having a single groups.
Yaml, we have specifically attributes, metrics, events, entities, and whatever spans And then this actually fully works. It creates that new, that new schema.
And when you resolve a Yaml file it will look for that new schema, and it'll look for groups. It will take the new schema and automatically convert it back into groups before continuing with resolution. So you can actually, with this Pr, you can use it today, I need to do a bit more cleanup around it.
And then the next thing I want to sort out is the resolved registry being updated to match the same structure.
Because I think right now, resolved, registry and registry are actually 2 different definitions. There's weaver semcom. There's weaver semcom resolved. What I've done here is, I've created a v 2 that has the V 2 things, but not all of them. So if you actually go to, I think it's under lib. It might be under weaver semcom lib.
No, it's it's under simcom. Yeah. So right now, if if you pop this open a little bit. There's a simcom spec.
and what I've done is
Liudmila Molkova 00:50:16 This one.
Josh Suereth 00:50:17 Yeah.
So semcom spec right now, there's groups and imports. Right? What I want to do is effectively can keep the semcom spec as the central source of truth for Simcom.
We have imports, and we have well, actually, how to do the let me take a step back.
What I've done so far is I haven't changed imports at all.
This gets resolved where it will, either it'll grab Semcon spec, or it'll grab groups.
and semcom spec is a flattened one that has attributes and all that kind of defined. So you can actually define attributes and groups in the same thing.
All of the new V, 2 things are erased into groups prior to resolution.
So everything works as is today. And we can start defining things in the new model imports. I don't know if we want to change that at all like should we have? Because I think we have 2 options here with semcom spec, we can actually have a v 2 semcom spec that gets resolved into v 1 semcom spec. Or we can have a blended spec that has both of them at the same time.
And we start adding warnings when people are using groups, the old style groups, okay.
if you pop open imports, though, or it's right below this, right.
It is importing by group.
However, it's called metrics. It's called events. It's called entities. And the group wildcard vector. That we're looking at is, if I recall correctly, it's just like the name of the group that gets chosen. So I think this is fully compatible if named weirdly for v. 2.
So.
Liudmila Molkova 00:52:19 How is it named? Weirdly.
Josh Suereth 00:52:21 It's called Group Wildcard, as opposed to.
Liudmila Molkova 00:52:23 Oh!
Josh Suereth 00:52:24 Or just wildcard or name Wildcard, right or Id. Wildcard, but that's all. So like.
I might update the description of this when we go from v 1 to v. 2. But I think the content wise. It doesn't change.
Liudmila Molkova 00:52:40 We can just rename Group Wildcard to something else. Our Api names are not exposed to the end users, anyway.
Josh Suereth 00:52:49 Well, no, the so the if we auto synthesize our Yaml Schema or Json schema.
that rust documentation, the slash slash a list of metric group metric name wildcards. We just updated it to say, a list of metric name wildcards.
That's that's what I'm suggesting. So this would remain, as is because I think it works in both case like the V 2 and the v 1.
If you go back to to the go back up to Semkov. What I what the thing I want to add to this Pr. Before I would like propose to to import. It would be a warning or an error if you use both v. 2 and groups at the same time.
Liudmila Molkova 00:53:35 So.
Josh Suereth 00:53:35 So I'd like it. I'd like to when we roll this out, force people to put everything in one.
However, I wanted to check with with everyone here. I think we could actually start rolling out this ingestion part of V 2. Initially, while we work on the resolve schema in a separate. Pr, I don't want this to explode and make like get really really big as we work on. V. 2.
However, if you're more comfortable with us, making sure we can translate resolve schema to v. 2. I can start doing that as well. But the only thing I was planning to add here was a bit more end-to-end testing, and then a warning or error.
If you use both v. 2 and v. 1.
Conventions in semcom spec. That was it. What? How do? How, how are we feeling with that.
Jeremy Blythe 00:54:31 How long do we intend to continue supporting? v. 1.
Josh Suereth 00:54:38 We? We have N. Versions of semcom. We have to support.
Jeremy Blythe 00:54:45 Right. So it has to align with that which is based on the release the release of the sem conf projects output.
That's what we're talking about. So it's like 1.3 5 or something in the moment, and we go back. N versions.
Josh Suereth 00:55:12 Yep, I think it's gonna take a while until we can actually remove support for v, 1.
Jeremy Blythe 00:55:18 Is it worth having in the new spec? Is it worth having a head where you have to specify the version.
Josh Suereth 00:55:25 That was another thing I was thinking.
it does right now. Our resolution is so dumb, though basically right, we we we just resolved the Yaml model.
What we could do is we could have a header where you specify the specification version, and then I can issue errors if that is defined incorrectly, and I could issue warnings if you don't have one, and just do the best job of parsing what you have with the with either version like that's that's an option of something we could do.
Jeremy Blythe 00:56:01 If you haven't specified a version, then it means it's v. 1, because the spec for v. 1 doesn't have a version. So it should be paused like it's v. 1. If you're using 2, you have to put the header that says it's v. 2, in which case you're parsing it just as v. 2.
Then you don't have to do any guesswork. It's going to be an error if you do that way, or it's gonna be an error. If you do that way.
Josh Suereth 00:56:24 That's fair, I think, no matter what we will have to parse both like the way we're parsing Yaml today is super lazy, so we will have to have a structure that can parse both.
and then we'll have to do everything with validation unless we change our parser.
So it's that we check for version first, st then we parse the rest of the file.
Jeremy Blythe 00:56:47 That's what I'm suggesting. I think you do an initial quick check for version. Then you can switch to the version of the puzzle.
Josh Suereth 00:56:56 If I'm writing a custom parser, I want to write a custom language and not use Yaml at all. But that's just because you're walking through dangerous territory there in terms of like config setup, all that kind of stuff I get what you're saying. I would still be freaking lazy here if I can.
personally like, I prefer that because I think that I like what you're saying with having a version and and declaring what version it is, and using that for validation, I don't really want to significantly. Go change how parsing and and file handling works through all of weaver right now. Partly, I don't have time to do that much work, but partly I think it's it's a it's something we will probably need to build eventually. But I don't want to rush that like having a custom parser.
Jeremy Blythe 00:57:47 You. I mean, you can still use survey. Right? You just have. You just have that version in.
So they just has the version block.
and the rest of the entire document will be ignored.
Josh Suereth 00:58:02 Oh, I see you want to do. We could probably do a tag union. Where version is the tag for the version of the spec. And then we have one structure for spec. v. 1, 1 structure for spec. V. 2. And the version is the tag that determines which one is chosen where it defaults to version one.
I can probably do that.
Liudmila Molkova 00:58:27 What I I think.
I agree that eventually we'll have it.
Would it be hard to add it later?
Would anything change in how to write code today.
Could we could have disjoint models for V, 2 and v, 1, do we want to have these joint models.
Josh Suereth 00:58:57 I think.
What if if I do the disjoint union insert? I don't think it. It is as invasive as trying to actually change the parser. I think it accomplishes what Jeremy wants, and it gives us a little bit of explicitivity.
I can. I can Update the Pr to do that, and let folks look at it and tell me what you think.
The thing that it might give us is we could potentially then, auto generate schemars for the Json Schema for v. 2, independently of v. 1, and dump them both in an automated fashion, so we could have a. v 1 schema and A. V. 2 schema separately, if I do it right.
The only thing that might that might be missing is the requirement that you specify a version number. But it. I think I think we could probably make that happen.
So I'm willing to try it, and we can see what happens.
This. The version is a discriminator. It's a polymorphic model, Josh. I think you should enjoy this.
Jeremy Blythe 01:00:15 This.
Josh Suereth 01:00:15 It's not polymorphic.
Liudmila Molkova 01:00:18 Okay.
Josh Suereth 01:00:18 Is, or sorry. It's not inheritance-based polymorphism. So yes, I will enjoy it.
Liudmila Molkova 01:00:26 Okay.
Yeah.
Josh Suereth 01:00:27 As long as there's no parent-child relationship, it's it's fine. You have way, lots of flexibility. It's it's more of a parametric polymorphism. Yeah.
Liudmila Molkova 01:00:35 Okay, you're enjoying it, I see. Okay, we have to drop now.
Jeremy Blythe 01:00:41 See you later.
Thanks.
