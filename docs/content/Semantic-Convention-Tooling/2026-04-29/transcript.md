SIG: Semantic Convention Tooling
Date: 2026-04-29
Duration: 69 minutes
Zoom Recording URL: https://zoom.us/rec/share/IsQQ9vfUnLc0163KB7oRHlq40p69tlN7irYibKakcduMl3iJQkQ74lP7rVPnzTQh.jvDUkSP8rH8VkDiD
============================================================

## Zoom Recording Transcript

Liudmila Molkova 00:04:36 Hello, Alex.
Alex Van Boxel 00:04:38 Hello, long time.
Liudmila Molkova 00:04:40 Can you not take her.
Oh, hi, Trask.
Trask Stalnaker 00:04:55 8 bucks.
I happen to be awake, so… And I happen to be doing a lot of, working with Weaver, lately.
Liudmila Molkova 00:05:10 It keeps you awake.
That's funny.
I have a new bot here.
Trask Stalnaker 00:05:24 Alright. Let's see if this one is polite and asks if it can stay.
Liudmila Molkova 00:05:35 It does.
Wow, that was fun.
I don't know… I think Josh should be coming.
But… In the meantime, I saw, Alex, you put, this one on the agenda.
Alex Van Boxel 00:06:03 Yes, yes.
Liudmila Molkova 00:06:06 Let's wait for Josh.
Alex Van Boxel 00:06:07 Yes. Okay.
Liudmila Molkova 00:06:09 But there is one thing I wanted to show you, that we've been playing with, and I'm curious what you think.
So… what we have today, and I think I mentioned it before.
We have some very funky way of defining types, which is JSON schema.
And we just mentioned that, okay, that attribute follows JSON schema.
It… it looks super ugly. It needs some love, but it has some interesting… side effects. So, for example, we can… Validate the type. This is where we call the Weaver Policy Engine. Well, more than Weaver.
But we can just say, okay, do you match?
the type?
Does the value of attribute matches the type?
And here we go.
There is another interesting thing, that in Open Telemetry, we have a… precedent of defining… YAML schemas, JSON schemas through YAML.
Alex Van Boxel 00:07:25 E.
Liudmila Molkova 00:07:27 And overall, I think, Trask, it's the configuration, right?
Does it?
Operation.
So essentially… This is a… Another funky way of writing YAML JSON schemas.
Alex Van Boxel 00:07:52 Any of them?
Liudmila Molkova 00:07:55 Which brings us to the point that we have all the pieces, and I know we had some discussions about JSON schema before.
But you were not happy with it. So, like, I'm going to give the stage to you, and Josh is here, and maybe we should talk about your thoughts on the topic now.
Alex Van Boxel 00:08:19 Alright.
Liudmila Molkova 00:08:22 Do you want to share?
Alex Van Boxel 00:08:23 Yes, yes, maybe… maybe I'll… I'll kind of… reiterate… I'll first tell you why it's important for us.
Right.
So, as an end user.
We've been using, we've, we've been using… our own eventing. So for us.
it's all about eventing, so that's why the body is important for us, but, like, the time system for attributors makes sense. To have the same across attributes and body, makes sense.
We were already internally using, our event system, completely tailored from the body. We had also an event name, by chance, on that thing, but it was not schema first.
So every team started to create that, and that works. It works, but, like, it has the typically problems.
Where that, of course, things start breaking, because people start, creating schemas, or changing their contract, because they're just looking at it from locks, and so on. But, at the far end, you have the typical analysis being done.
That, so we want to do schema first for our logs. We do it already for APIs, we do it already for Kind of our events that are real events on our… between our microservices, where we use Proto, but this is kind of… our logging is more for an analytical purpose.
And we are all in in OpenTelemetry, so we just want to use the moving parts that we already have in place, and the V1 that we already have serves its purpose. So for us, our V2, for our perspective.
would then kind of tie into the Weaver V2 schema.
To actually, okay, let's define our contract in repo, and say, contract first for our locks as well.
We're starting to do that as well.
Like, I have a few examples of the… those are pretty new.
So… And this, we're doing that with semantic conventions V1, because there you can still define Type information in the body.
But it works! So, for us, it serves a purpose.
And that's why I'm at least invested in having this in V2, because this would, kind of be a blocker for us to move to V2 to define our semantic conventions.
I start, like, the last meeting, which was in February. I… I started, because I'm not a Rust expert, to just start to… and with all the conversations, move together, and I have a proposal on the YAML schema to then go and do the implementation.
For me, that can go over months and months. We don't need it now. We have a solution here.
That we can build upon internally, but eventually everything goes V2 on the semantic conventions, and V1 goes away, and we don't want to be left behind, for this. So, I'm invested in doing a solution.
I'm not tied into what I'm being proposed, so if you have something more based on JSON schema, I'm… I'm fine with that.
I used just kind of based what we had in V1.
In the last meeting, you said that there would be some, and that also is in the tickets, where I added my proposal on.
This one, also had conversations, having a type system as well in there to define types. I've been… Collected all that information and have a proposal.
heat, and… we can then discuss, like, having the types block that's also aligned with the comments here. There was also… I was doubting we should use struct or types, because there is already… in spans, we already use type, and so on, but, like, okay, back to types.
We could use… Typically, namings… And as fields, very aligned to what you… what we already have.
Maybe I'll show you the full example here, then.
So this is a full YAML, for example, a type, a brief stability in the fields.
All of us, this should look very familiar, but those, instead of, like, having them always in line, V1 was always in lines.
This introduced reusability. The reusability is also… you can use this, and you can use embedding.
Where you can actually embed, a type and extend it, like that.
So… this one is, like… Just two fields… This is an extension with an embed, so it has long, long, and a name.
Hmm… this is… A new type that combines… The other types here.
So the origin is the order type.
Some constraints as well, where we… I think that's important that you at least could have some constraints with some minimum and maximum for numbers and array access.
and voila, and you could use those in attributes. Pretty simple. It is… though on purpose, not completely, complete JSON.
JSON schema implementation, unless there is a very good implementation in the Rust, and I think from what you were starting to say, that you… have already started to have the parts in place where you have a decent JSON schema implementation, or did I understand that incorrectly?
Liudmila Molkova 00:15:09 So, yeah, so I… we were doing JSON schema because it's… it's there, right?
Alex Van Boxel 00:15:16 Yeah. With documents.
Liudmila Molkova 00:15:17 to invent it, it works with a lot of tooling, you can, like, there is not awesome, but reasonable code generation from it. You can validate if something aligns with JSON schema in every language. The Rust has JSON schema implementation, we use this library. I don't know if it's awesome, I think Josh and Lauren will have more information on this.
But mostly, I think what they see here, it looks much better than Jason schema. It's very tailored to what we want.
Alex Van Boxel 00:15:47 It is.
Liudmila Molkova 00:15:48 It's a lot of work.
Alex Van Boxel 00:15:50 Yeah, and, and I'm fi- and, and I understand that's… that's… that is certainly not on your priority, yeah? So, I want to take that work on… on me.
But I don't want to start on this with, kind of, without a group approval of, like, hey, this is what we want to go to. For me, it's important, it needs to happen.
JSO schema, or this.
And it's kind of an opportunity to contribute here in the Weaver Project, and learn some Rust on the way.
But I don't want to do this without kind of an agreement on which direction. I'm not so much invested in the format. For me, though, it's important that it is at least embeddable.
So that you not, have, hey, point to this, JSON schema completely disconnected from the rest.
Because I think that can introduce problems, certainly if you want to kind of reuse something that is defined in one JSON scheme or another, how do you reference that if it's part of this block and this block and this block?
I want to… that it's kind of a uni… kind of a united front.
So…
Liudmila Molkova 00:17:14 Go ahead, Josh.
Josh Suereth 00:17:15 Yeah, so I, I am supportive of this, because I actually find JSON schema really freaking hard to read and maintain.
I would prefer to have something that's simpler to read and understand.
or, like, more matches our domain, personally. So I'll call that out. But also, when it… what you're proposing kind of matches what I want to do with types, but I think there's a set of things we need to talk about, and I'm already on step two.
Right? So, for caveat, I'm a language person. I used to work on, like, language design, compilers, type systems, that sort of thing. One of the things that I kind of want to understand, as we go, And apologies if I'm using too many language terms, but basically, I think we're building a nominal type system.
But I saw structural elements to what you're doing, and so I think we want to understand that. And if you want, like, the human version of that, if you're familiar with TypeScript, interfaces, where you define an interface with, like, these things, versus, you know, named classes.
That's kind of like the, like, which direction are we going with this feature set? Is it true that if I have, you know, the same named things, that it's the same type?
And are those things compatible?
Because that's kind of how JSON schema works a little bit. Yeah.
But… for semantics, is that true? Right? And for Weaver, is that true? And that was one of the decisions in my head that I never resolved, but I also never told people about it, because it's hard to have that discussion.
Alex Van Boxel 00:18:52 For me, this is not imp… For me, this is not important. For my use case, let's say, yes.
Josh Suereth 00:18:59 But it's…
Alex Van Boxel 00:19:00 It could be for others, that I don't know.
Josh Suereth 00:19:03 Well, that's why… what I want to do is, if we don't have a str… one of the reasons we're doing a V2 is we evolved Weaver from, like, you know, a bunch of Python scripts, and it went a particular direction, and then we had to course correct and say, okay, this is going to be much simpler. I'd like to have a better foundation or at least know that we can build a foundation on things as we go. So I think what I would ask is, on this, there might be limitations we place on it initially, so that we can make that decision later of how to handle that.
And decide if it matters. So, like, as we build and explore, we can be like, oh, you know what? That's not a concern.
If you're amenable to that. But from my perspective, I'd be happy to sponsor your work here and do code reviews of it.
Alex Van Boxel 00:19:51 Yep.
Josh Suereth 00:19:51 If we agree this is the right direction as, like, a group of maintainers.
Laurent Querel 00:19:58 I totally agree with… sorry, Craig.
Liudmila Molkova 00:20:01 It's a quick one. So, I… I think it's a great direction, and I love how easy it is to read and how tailored it tailored… I mean, the thing I'm slightly worried about, that building this, like, the full story, would… would be a long way.
And in Gen AI space, we would love to have a little bit more structure around what we have today, JSON schema, so we can, I don't know, validate in life check that the value matches the type right now.
And we can probably figure out the paths where we, have some annotations saying, okay, this attribute supports this JSON schema, this is where the JSON schema lives, some hockey story for that, but that would… bring us where we want to be in Gen AI, where we need pretty much all the capabilities of JSON schema, because GenAI people are crazy about JSON schemas.
And… Over the time.
As the proper syntax.
Evolves, we should be able to switch.
Alex Van Boxel 00:21:11 You mean switch them to JSON schema?
Liudmila Molkova 00:21:15 Oh, no, I mean, like, for today, I would… I think in Gen AI space, we should you're using the.
Alex Van Boxel 00:21:22 Yeah, yeah.
Liudmila Molkova 00:21:22 Oh, sorry, JSON schemas. And eventually, once we have enough features in the proper typing systems in Weaver, we would switch to that from Genia perspective.
Alex Van Boxel 00:21:33 But the question is, would we want to implement the complete JSON?
schema features, because I… so, if I look at from… a company perspective, if you look at all the code generate… all the code generations that use JSON schema.
As an input, some of them really struggle of what the things you can define in JSON schema.
And… and, like, half of them are buggy.
Because the possibilities are so large, like, you can do that, and that's why I'm a fan for Proto. Proto is very simplistic. That's also why I was looking, like, at just importing messages and embedding and then just extending, and that's all… and you have the one-offs.
But that's about it. But all the code generators work, so…
Liudmila Molkova 00:22:34 I don't think it's a target.
Josh Suereth 00:22:36 Yeah, here's what I'll say. JSON is a structural typing system, and you have lots of craziness with, like, union types and semantics of those, that when you do CodeGen in a language that doesn't natively support that, it sucks. It's just… Frank, if we were to do something in Weaver, we need to support lots of CodeGen, so we generally want a simpler model. Which, yes, you can't express everything, but we're gonna make sure that CodeGen looks decent and everything. Lyudmila, I think it's a reasonable ask for us to say, InGen AI, can you avoid using advanced JSON schema capabilities? Like, can we avoid shenanigans with crazy unions that don't make, you know, when we use a union, if we can make it so it's a simpler concept behind it that we can migrate to, I think we're in good shape. And I don't think you're doing anything crazy from what I saw. I think you're mostly just defining a single structure, and not using the advanced stuff.
Is that fair?
Liudmila Molkova 00:23:33 Yeah, it is fair, and at the same time, we don't need to target supporting full JSON schema. So, like, crazy edge cases might be fine with just some hockey JSON schema solution if they absolutely need it.
Josh Suereth 00:23:47 By the way, in terms of let's rewrite semconf in proto.
For context, that's what I maintain at Google.
for all of the, like, Google Cloud metrics and things that people use. If you look at the docs, our docs of, like, what metrics we have, yeah, guess what that's defined in?
Laurent Querel 00:24:03 Together.
Josh Suereth 00:24:04 Anyway.
Alex Van Boxel 00:24:10 Okay, I think we come to kind of an agreement. We… I can move on. Feel free to… I'm gonna reuse that… for, like, the comments, I would propose that you… you add comments if you see something that is not aligned on the… not so much on the implementation yet, but on the JSON schema.
And then I'm gonna go very slow. I'm fine working very slow. I have, like, the proto-implementation in Apache Beam. It took a year and a half. I'm used to that in the open source. So, for me, it's fine to go very slow.
Liudmila Molkova 00:24:52 I had one, comment, but I think Lauren wanted to say something before I interrupted you. Do you still want to say something?
Laurent Querel 00:24:59 Yeah, I mean, nothing is super important. I was just, also, supportive of the pure YAML approach that is tailored for the project.
For the reason that you mentioned, the fact that it's, easier to understand, and also just focus on what we need, and without all the weirdness that Joshua was mentioning.
I think the Gen AI people like Jason Schema, because they already work a lot in this space to constrain their model, and maybe they have some, Way to automate the… The generation of those schemas, and they are well understood by their model.
Which is a parameter to take into account also for us, because if we come with our own Way to… to specify data types.
That will not necessarily be, understood right away by those models at the same level of efficiency. But what we gain, is, code generation, but more importantly, a way in life check To control, the… the compliance… of the telemetry stream, with something that is much easier to automate than the full design schema.
I think that would be a lot of work in live check if we do that.
And for…
Liudmila Molkova 00:26:25 We actually already implemented this part of JSON scheme as well.
Laurent Querel 00:26:29 Yeah, but… okay. But with, I guess with the rego capabilities, or something like that?
Liudmila Molkova 00:26:36 Yeah, this, this is through Rico.
Laurent Querel 00:26:39 I'm just wondering how efficient it is, based on the first, based on the first experiment I did, regarding the integration of LifeCheck into Something that is not just a toy where we… we generate, Well, Android, Signal, but something where we have a real production, telemetry stream.
I figured out that that doesn't fly at all today. So we have to, We really have to think about a solution that will, be scalable in terms of performance.
And, and that's another reason why having something a little bit more constrained With a… with a smaller, Objective, and yeah, easier to implement.
Yeah, so supportive of the approach that Alex is suggesting.
Alex Van Boxel 00:27:45 Alright, cool.
To be honest, it's all… based and inspired on V1 and the things in the thread anyway, and my need of, like, oh, let's make it not JSON schema complexity.
Alright.
Good, thank you, thank you. Ow!
Keep you guys posted.
Liudmila Molkova 00:28:13 I have added a few topics. Thanks, Alex, for coming.
Let me share my screen.
Okay, so I have a pull request.
For forward compatibility for resolved schema and publication manifest.
It's just a bunch of… plumbing and wiring. There is nothing interesting to see.
Except, that where we use… The same types between definition and resolved schemas.
So, the moment I relax something for the resolved schema, I'm relaxing it for definition schema.
Which brings me to the second point.
And I want to follow up on the definition schema. So today, our definition schema is just major version.
It's cool, But I think… Not cool enough.
Because, let's say we've had somebody mistyped a property in definition, we cannot really… Issue any warning?
And we cannot fail on it ever, unless the major version is different, or there are some other issues.
So, if we did… things consistently, and it's definition 2.x.
We can apply the same trick, we can say, okay, if it's a known minor version in here, it's something unknown, we are going to fail.
And if it's higher minor version than what we support, we can warn you and say, okay, go update, we will try our best, but, you know, the outcome may be not what you expect.
And it brings us consistency across all the file formats.
I've already updated OTAP with it, but I'm looking for this group to blast my changes.
And I will follow up with the PR.
Any concerns?
I think…
Josh Suereth 00:30:30 The main thing we need to do is when you update everything, we need to make sure our release process is tracking the supported major-minor versions now, right? So I think we need a constant somewhere that says our currently supported, definition version for the different major versions. And we need to make sure that in our release process, we update that.
Right, so if I bump the definition minor version, I need to bump the supported version set.
And I'm more worried about making sure we actually do that, that level of tracking. So, if we have, like, if we want to update the release skill that we have, if we want to have automation, I think you already have this to detect when you break a… make a change that should bump the minor version. That would be my only concern, is I don't want to allow, accidental human error here.
Because of the implications. Like, it gets awkward.
Liudmila Molkova 00:31:35 I think we have it, but maybe we should do something like Weaver-minus version that would print all the versions we support. We have them hard-coded in the code, for sure.
Josh Suereth 00:31:46 Okay.
Yeah, but just making sure every time we bump a minor version that we also bump that supported version.
Anyway, I'm generally, like, I already reviewed the PR, but I didn't make comments yet, because I'm still, I was still doing some thinking, but I like… I like what you've done, like, the whole handling unmanaged things and all that.
Yeah, anyway, the reason we didn't, change the definition syntax was, related to, if you think about languages, we don't really, like, you know, if you're thinking JavaScript, if you're thinking TypeScript, they don't really support A minor version thing.
Liudmila Molkova 00:32:26 Yeah, we had this conversation with Trask, and my thoughts were, okay, where is Java 25?
They release yearly. Will we release yearly? No, we will release monthly.
Josh Suereth 00:32:40 Are we making breaking changes every month?
Liudmila Molkova 00:32:44 Not breaking, but incremental, right? And when you make incremental change, we will still get better diagnostics if we know the version that people used.
Versus what we support in this version.
Josh Suereth 00:32:57 Are you expecting people to actually change the definition number?
Every month.
Again, this… it seems real high friction to me.
Like, I… I don't want to… yeah. This is where I'm… I like what you're doing with the unknown attributes, and I think we have a thing that basically can say, hey, I don't recognize this attribute as a warning.
Liudmila Molkova 00:33:23 Let's see.
Josh Suereth 00:33:24 and we could warn people if something's deprecated and changed, but, like, you're asking the entire ecosystem to change their definition to, like, 2.1, 2.2, 2.3 every month? That would be… Yeah, that has me concerned. So, I would still like for us to kind of push on Yet not requiring that to change frequently?
You know? And, like, we do incremental change, and we find a way to warn without it.
Just because of the ease of use problem.
Liudmila Molkova 00:34:04 Okay, yeah, sorry. Yeah, I totally forgot about this, this is the most important part.
So, always warn an unknown, and always tolerate.
Is there any benefit in having this? Only if you want to be really strict.
Josh Suereth 00:34:27 Yeah, I mean, there are people who run in strict mode in languages, and that's fine. Like, if they… if they want that toil, let them opt into it. I just don't… I have fears that there's a lot of people who won't want that toil and don't care, you know what I mean?
They just want it to work, they want us to do the heavy lifting.
That's… that's kind of how I think of it.
Liudmila Molkova 00:34:48 Okay, cool, yeah, sorry, I totally forgot about it, thank you for bringing it up.
Laurent Querel 00:34:53 A question, do we need to introduce a strict mode, or can we rely on the future, Flag that we introduced a long time ago.
Liudmila Molkova 00:35:06 I think this is separate, right?
Laurent Querel 00:35:08 Yeah, that's also mentioning.
Yeah.
Liudmila Molkova 00:35:13 I'd rather not touch mod now, just because we can edit later.
Josh Suereth 00:35:24 By the way, I really like the unknown fields thing you added.
Liudmila Molkova 00:35:27 Oh man, it was… we went so much back and forth with Claude to arrive here. I burned so much tokens.
Josh Suereth 00:35:38 Okay, well, it was worth it, I would say. I don't know how much money you burned, but thank you.
I like… I like the unknown field option. I… I'm surprised, I thought that would have existed for protos, like, in, Prosts.
But I didn't… I didn't see it when I was looking. Anyway, I think that that actually, from my perspective.
we get so much flexibility with that, that we might find we don't really need the 2.X stuff. We might… we might just be able to have Weaver say, here's the current miner version, and kind of recommend people upgrade to the latest things we have, using unknown fields, and if they're using an old version, and we warn them that we don't understand things.
That will implicit… you know, we can suggest upgrade your weaver.
And I think that gets us, you know, 80% of what you need.
without adding the complication for users. So, I think it gives us a lot, is what I'm saying.
Liudmila Molkova 00:36:34 Awesome.
Thank you.
Anything else on this? I'd like to move on.
To the next topic.
Cool. So, the… we have the RTAP for Schema V2.
And there is one discussion I want to get your thoughts on. So this is the judge's concern about the terminology and what points to what.
So with today, schema URL points to manifest, not a schema. And then manifest points to resolved schema, and I think this is the core of the concern, because everything is called schema.
We can live with it, we can also… do a better job with terminology. We can say that, the resolved schema, like, the manifest points to resolve to registry, because this is also what we commonly use. Any concerns with this rename?
Laurent Querel 00:37:40 Perfectly fine with that.
Liudmila Molkova 00:37:43 Okay.
And, awesome. And the last one, and Rosk is also here, we've been, bike-sharing kind of format through the schema URL, I think it's related to the dependency question, topic you have, Josh.
And we kind of landed at, okay, let's do both. So we need a suffix for the… Turns out we have a terminology for it in the spec.
Schema Family. This is called schema Family.
So we need a new, suffix here so we can order, and resolve conflicts within that one.
But also, we want a suffix, because then it becomes conventional somewhere thing, and people looking at it can easily see the It's not a stable one.
And then I'll Trask, if you want to add anything to this, but I think this is what we… should do.
And then there is a small, maybe bigger.
Josh Suereth 00:38:52 I want to add… I want to add our concerns, right? So, in Weaver, we want to use semantic versioning to determine if something can override something else, right? So, the two things we need to make sure are true is the schema family, which we'll call the name of the registry, right?
The schema family needs to be, when there's a schema family with two different version numbers, we need to know if one overrides the other. And so, if you put "-dev in the version.
That has implications for Semfer.
Which is actually fine if you don't try to blend 1.40.0 with 1.40.0-dev. As long as the family… right, because what will happen is the one that doesn't have the dash will always override the one with the dash.
In… when we do dependency resolution and dependency management.
That's why in the OTEP, I suggested that we actually make a new family name for the development stuff, because otherwise, the dependency conflict resolution was going to hell. Like, I couldn't make it work. Or I had to do stupid shenanigans where we're not really doing something for anymore. We have hard-coded rules to handle dev.
So I think, in my mind, the only thing I need from that dependency resolution stuff is making sure the family name has death.
That, that, that helps us out a lot.
The question I have, then, is does dev depend on Semper, SemComf, right?
like, is it a dependency where dev will depend on Semcov so that I know what's stable and unstable, and if I take a dependency on the unstable bits, I can still depend on stable bits, and I see them?
Or is it everything is duplicated in dev?
Because I think originally our plan was to duplicate, and now I'm on the fence about this, because you'll start to get version conflicts if you have dependency help between the two.
Laurent Querel 00:40:57 Based on what you just said, Josh, Will not that be a problem if we have a dash dev, in a realistic scenario, when we have, dependencies?
Some of them will use the 1.38.0 stable.
And maybe you are testing another one with a dev.
In that case, you will not be able to make the resolution, right?
Josh Suereth 00:41:23 Yeah, that's… so that's what I'm getting at. So, like, for context, the… you know how we have a stability level?
on all signals and attributes in Weaver.
The dash dev would only have… what I'm proposing is the stable one will only have things that are marked as stable, or deprecated.
I guess that we move deprecated, so it's only things that are stable. Anything that is unstable is actually split apart and published to "-def.
So, like, you would actually have… and the unstable stuff would depend on the registry from the stable stuff. So you can still use them both together, and you always resolve themselves But if I have multiple registry hell going on.
What would happen if we don't do that is if I depend on dev and some, you know, dependency chain depends on stable, I now get actual conflicts, and I cannot do this.
It actually fails.
Laurent Querel 00:42:23 Okay.
Josh Suereth 00:42:25 So, the other option is, we do some kind of shenanigans with, actually, the stability labels we have in the Weaver model somewhere.
as I've explored that in my head, I get very confused very quickly as to what the algorithm looks like, so I don't want to do that.
I actually like what you're doing here a little bit better.
But that's… that's a possibility we could explore.
Liudmila Molkova 00:42:49 Oh, we have stability as a… in the manifest.
We don't need to look any further.
Josh Suereth 00:42:56 What I meant was we could have some sort of, stability… like, if I get a conflict on an attribute between two versions, and the stability was not marked as stable, I could consider it a conflict.
And say, hey, you actually have a version conflict between two unstable attributes that you're depending on. We can't guarantee this is safe to do resolution, and I can fail.
like, I could… we could implement that right now, if you wanted, with the multi-dependency stuff, but… right. Trying to keep it simple.
Liudmila Molkova 00:43:29 Yeah.
What should we do if somebody depends both on some confidence, some content dev?
I think we shouldn't allow it.
Josh Suereth 00:43:38 We… I mean, we… we could dis… again.
If semconfdev duplicates all the stable things from SemComf, then you're going to implicitly disallow it, because it'll be broken.
And then people will complain.
Liudmila Molkova 00:43:51 It would not be broken if the version aligned at some point, and then they.
Josh Suereth 00:43:57 no…
Liudmila Molkova 00:43:58 Drift.
Josh Suereth 00:43:58 No, in dependency resolution, the way we do dependency.
Liudmila Molkova 00:44:01 Instagram.
Josh Suereth 00:44:02 You would see two groups Right? That are from different… semantic convention families.
And that is considered a conflict that is unresolvable, and it says, hey, you can't use these together, because they both define the same.
Liudmila Molkova 00:44:19 That's a failure. Yeah.
Josh Suereth 00:44:21 We would allow this eventually, because we're gonna allow disambiguation, but honestly, I don't know why we would prevent that necessarily, and here's why.
If I'm defining a SEMCOF, That depends on, dev.
But I depend on some other federated SEMCOM. Remember, we have multiple dependencies now.
So, I depend… let's say I depend on GenAI, stable.
Okay? But I am unstable, whatever the heck I'm building. Let's say I'm building new, you know, Agent 2.0 craziness, that I'm unstable. So I depend on unstable Semconv for some things, and I depend on stable gen AI. That should not be a failure.
Which is why we can't actually prevent people from depending on both SEMCOM Dev and SEMCOM. It's just, you know, if you depend on SEMCOM Dev, you're a dev… attribute. It's like… But sticky, or whatever, the experimental bit.
Liudmila Molkova 00:45:16 Okay, so then some conf.
Somehow, we'll need to know, through convention, the word explicitly, that it's a variation of semconconf.
Thanks.
Josh Suereth 00:45:29 I think it's explicit. I think we make SEMCOM dev have a dependency on SEMCOM.
Liudmila Molkova 00:45:34 Right.
Josh Suereth 00:45:35 For the same version. And then everything should work okay.
Liudmila Molkova 00:45:40 Okay.
Cool. I think these are the problems for future us, and I think you, Josh, is going to talk about it, about multiple dependencies. I have what I need to make progress on the ADAP.
Cools.
Josh Suereth 00:45:53 Alright, so, yeah, for multiple dependencies, there's two PRs.
Wanna present?
Sure, I can present.
Give me a second to actually find the tab.
Okay.
So, this is part one. All this one does is allow you to define multiple dependencies, and it considers any kind of schema URL discrepancy of failure.
Okay? So, if you depend on version 1 and version 1.1 of SemConf through your multiple dependencies, that fails in the first PR. Meaning, I don't think the first PR is super useful, it's just setting the foundation for the second PR.
It's because I was trying to not give you guys too much to review all at once. However.
I found in the second PR, There's something this doesn't handle, which I'll show you in a bit. Let's see… not you… Let's get rid of this. So, inside of Loader, this is where we're loading the semantic convention repos.
This logic here Has a bit of an issue.
Right now, the way we load repositories.
is, we will… we are as lazy as possible. So if someone defines a manifest with a dependency, we will load that dependency. If that dependency is already resolved, we will not go resolve the underlying dependencies or even look at them. We will only look at the resolved bits of it.
That's where the bug is. I'm not actually finding conflicts in the dependencies of the thing you pulled in, and they might show up later.
Right, so I'm actually allowing the deadly diamond to succeed in some places where it probably shouldn't.
that is fixed in V2, or in the, in the Part 2.
I am kind of done with this PR, though. I don't really want to spend more time on it, because I've been spending a lot of time on the part two, which is where I think it becomes useful.
So, my question is, Ludmila, you have an open question here, I forget what it was, let me go find it.
oh, it was about…
Liudmila Molkova 00:48:11 Rather than you just write tests in V2 rather than in V1.
Josh Suereth 00:48:16 Okay, update… update the test to V2, yeah. Do you want me to do that now, or can I do that in the… other PR.
Liudmila Molkova 00:48:25 You can do it in the other Pure.
Josh Suereth 00:48:27 Okay. Does anyone have any concerns with this V1 going in? I would like to not launch Weaver until Part 2 is merged.
Because again, I think this is a good stepping stone, but it is not, I think it's a little risky with where it is now, but I wanted to check with everyone to see if we're comfortable with that as a stepping stone to make the next PR a little easier to review.
I see your head shaking, okay. Thanks, Jeremy.
Cool. So let's… let's talk a little bit about Part 2. So what does Part 2 do?
Part 2 is where I'm actually looking at semantic versioning.
So if I see, an attribute or a signal from two different depend… from, two different places, two different schema URLs, but the family name is the same.
I will use the semantic versioning and pull the correct one in.
Based on which one is the latest. So I can show you what that logic looks like, but I had to do a bunch of shenanigans in here.
So this one has a lot of changes, apologies. Let's… let's walk through.
Maybe this actually works. Do you think this is working?
Oh, I added a few new, error types. You can see, basically.
One of the things that is really important is schema URLs have to be formatted to match the specification, or this doesn't work. So I'm actually issuing errors if your schema URL is not valid.
You can do nothing about this, though, you have to yell at the person who published the schema.
So this is kind of a breaking change.
But I think it's important to call out, so I wanted to call that one out. We have a new duplicate dependency thing, where if you find a dependency that has different versions, and those versions are incompatible.
we will issue a warning. This one is actually in the first PR, I believe. And then the next one is ambiguous reference. This is a new one of, if I get a reference.
from two different schema URLs, you'll get this error.
Okay.
I want to show the schema URL change. Effectively, what we have now is a new way to grab some version. It gives you a result because this can fail. I am automatically stripping the V.
off a version, if it exists, because I think the spec allows it, and doesn't… like, the spec was a little… vague, but I'm just allowing the V, because sometimes we use it in SEMCOM, sometimes we don't, so our test couldn't pass without it. I think the spec doesn't allow it, but we use it so often that I just added this anyway. And I would add this to the spec, of like, you can put a V, we don't care.
Not sure how you feel about that. Anyway… That's the big thing of why we have to have errors and why we enforce the spec, because SEMVR can fail, and if SEMVR fails, we really have no idea what the hell to do with dependency resolution.
Okay, if you want to see any of the complicated bits, I can show… I'll just show briefly.
Let's see… yeah, this is, this is an example attribute resolution.
we have a resolveConflicts method, so when we try to resolve a new attribute.
We look… we try to look up if we already have that attribute. If we do, we try to resolve.
The new attribute and the one that we found locally, like, because there's now a conflict, And we will insert the winning attribute, like, whichever one has the latest version, as we build our attribute catalog. So, we will only build with the latest version of attributes we see. This does have some weird implications, so if I'm depending on two different versions of SemConf.
And, I am not re-exposing the entire dependency.
I can actually end up with attributes from two different versions of SemConv in the same catalog.
Because of the way the dependency chain works?
It's a little awkward.
the way to solve this would be to make resolution take longer, and, like, fully Expand the entire tree of every possible thing that people could use, all the time.
Liudmila Molkova 00:52:54 Wouldn't it be easier if we kind of normalized the dependency tree before we went into the attribute resolution, and say, okay, we only take it from that version of, I don't know, someConf?
Josh Suereth 00:53:05 Well, here's the thing, I do, I do that.
Liudmila Molkova 00:53:07 Oh.
Josh Suereth 00:53:09 The problem is the way Resolve's schema works, and the re-exposing imports.
Right? So, the… the… think of it like everything is packaged private unless it's exported, okay? And if I depend on some other package, I don't just implicitly expose it, I actually re-expose it via import today. That's how Weaver is functioning.
So, it's almost like a type alias, in an import. Like, import this as this, right?
Liudmila Molkova 00:53:41 So, by the time we actually look into imports and attributes, what if we only knew about one version of each?
registry.
Josh Suereth 00:53:54 So, the result schema we have… If you think of the, like, the resolve schema has a bunch of things defined in it, and they have a provenance that tells you what it came from.
So, I do dependency resolution to say, here's the only schema URLs I allow.
and then when I look across dependencies, if I have a conflict, I will resolve them. But if I don't have a conflict, if that resolved dependency re-exported a span or something, right?
we get whatever schema URL that Span had from that dependency. Maybe… let me… let me draw this a little bit, so it's a little more clear. I hear what you're saying. It's… I think this gets into… do you remember all the debates we had about import versus not import?
And whether we should re-expose everything, we're kind of in that world now.
where that is causing actual problems in the algorithm. So let me… let me walk you through. So we have… let's say we have, schema A, okay? Has span A, has metric A.
We have Schema B.
Depends… on schema… A version 1.0.
Dot 0, something like that.
Imports Spanish.
Okay, now we have our schema.
depends on A version 1.1.0, depends on B, okay?
I import metric A.
and I import… oh, let's say it defines span B.
I import… Find Span B, which uses… attributes, from span A or something. Oh, hold on.
This is easier. We have attribute A. Uses attribute A.
Does this make sense, or am I jumping too quickly here? Let me know.
Liudmila Molkova 00:56:02 Makes sense so far.
Josh Suereth 00:56:04 Okay, cool.
So now this one will import span… B.
Okay?
and span A. Now, the algorithm.
when I import Span A, and I'm looking for that attribute.
I own… I… I look at, I see it in schema… A and schema B.
both have Spanish, okay? Because I was importing Spanish, so it's re-exposed.
So I get a dependency conflict. So I go to conflict resolution.
and I get out 1.1.0 as the resolved version, okay?
when… I import, metric A, no conflicts.
we just get 1.1.0. That is working kind of by accident.
Because we have no conflicts, we just take whatever it was, you know, at, but because this happens to be the latest version, that's what we get.
Where things get more fun is, if I use attribute A, that… Now gets a little funky.
Or no, sorry, if I use SPAN B.
Span B is able to use attribute A at 1.0.0.
Because… The way this algorithm works is we're being as lazy as possible with when we expend, and if something is already resolved, we don't try to re-resolve it.
Because that would kind of break the other thing.
So I end up with this weird scenario where I can actually get You know, multiple versions of attributes.
Coming down with different… Things.
To fix this, what we could do I mean, what you were talking about, Lyudmila, is one of the things we could do, but I could also, change how imports work.
So, an import, instead of actually duplicating all the data into Resolve Schema, we actually just include the imports, and they're always a reference to upstream. And so, if I have an import from Resolve Schema A, I actually have to resolve its dependency and pull it directly from it. So when we do the master dependency resolution, everything fleshes out. So, in, in the, forge schema, or template schema, whatever it is.
imports look exactly the way they do today, they show up as raw signals, and you have Providence to tell you what schema your other from, everything's gravy. But in Resolve's schema, I would make another change to it that would keep imports around. So imports always are resolved at resolution time, and imports will change the version that they pick based on that dependency resolution.
this is a rather aggressive change. I mean, I actually have to fundamentally go in and change some core data structures to make this happen. It's gonna be even more code.
I'm thinking about that being, like, a Part 3.
of a PR, but I wanted to run that by everyone to see what we think.
Laurent Querel 00:59:41 It looks essential to have that, in my opinion, because otherwise that… they fit the… the purpose of the… of this project. If we start to have two attributes, A, in different contexts.
It means that we don't really align The attribute definition, and And then we… we will have dashboard, and we will have, other, Downstream dependencies that will have some weird behavior, potentially.
I'm thinking about, for example, let's imagine that in the future we have metric set composed of multiple metrics.
If we start to have metric A with unit second, metric A with unit millisecond, because they are in different contexts.
I think this one is a very good example of something we don't want.
So for attribute, it's probably less problematic.
Because what will change is… is… except if we change the type, if… let's imagine that attribute A was in… Development mode.
Josh Suereth 01:00:45 You can't change the type, though. Like, if you change the type.
That means… theoretically, that means you have a different major version, and when we do early semantics… so I look through all the dependencies early, and if there's any kind of major version conflict, we actually prevent going further.
So, so the…
Laurent Querel 01:01:05 Immediately.
Josh Suereth 01:01:05 What happens is if they're… they… you know that they're compatible, but it will pick the wrong version on attributes at times.
Laurent Querel 01:01:15 So, so, for, for the metric, so, so, in which context That will be a real problem for downstream components that will leverage this work.
Josh Suereth 01:01:29 Oh, I'm… I have to think about that. I'm still in theoretical mode. Like, I've been running tests and generating test scenarios. I think… I think in a real-world scenario.
In federated CENCOMF, let's say host metrics is split out, let's say GenAI is split out. Let's say I have a thing that's building on both GenAI and host metrics as federated semantic conventions, like my company repo.
I could wind up with a scenario where… I am using… a stale attribute from… they both depend on actual course MCOM, right? I'm using a stale attribute from CoreSemconf, so I'm using, like, exception.type from version 1.40.
when I should have used 1.41.
And theoretically, 1.40 and 1.41 are compatible, so there shouldn't be major versions, but let's say in 1.41 we deprecate exception type.
it means I wouldn't see the deprecation error.
Laurent Querel 01:02:30 Yeah, and we could imagine, I don't know, alien values.
Where we introduce a new value, in… In the new definition, so we end up with… Two variations of the semian… violence.
I don't know.
Josh Suereth 01:02:50 Yeah, what would happen is you'd get the… you'd get the enum with not… so this only happens if, You unambiguously depend on the old version, and nothing depends on the new version.
So, what… what… the way it would manifest is, you would get in a Noom that has the old definition without the new thing.
And you just wouldn't know that the new thing exists until one of your dependencies bumps their version number.
Like, it's… it's very subtle. It's very subtle. It's not…
Laurent Querel 01:03:22 I'm not sure that I'm following, because based on your initial example.
Where you, you end up with two attribute A, if I understood well.
Rights.
Josh Suereth 01:03:33 Yeah.
Laurent Querel 01:03:35 So, Valstream, they will see… if you, if you stay with the version that your second PR, Only.
You end up with a, a reserve registry, which contains two attribute A.
So.
Josh Suereth 01:03:54 Oh, yeah.
Laurent Querel 01:03:55 in the…
Josh Suereth 01:03:55 Yeah, yeah.
Laurent Querel 01:03:56 Yeah, so it means that, you have, A component, let's say a component in your system downstream to this, to this resolution.
that we will read this file, potentially, and do something with it. For example, creating a dashboard.
And, I'm just trying to understand what this system will do with such registry, where two things are slightly different, and then… That's why I was saying that, for me.
without the other fix that you mentioned in PR3, I'm not sure that we could declare that it's really reusable.
Josh Suereth 01:04:44 Oh, yeah, yeah, agreed.
It depends, though. Like, my thinking right now is that I think this… this was really hard to write a test to trigger. Like, I could see it in the code that I could do it.
I don't think we're likely to see it in practice, but I do think we need to fix it before we declare multi-dependency things stable.
Liudmila Molkova 01:05:12 We are at time, but I think what I heard from this discussion, it's so freaking complicated that even ourselves, even Josh, who wrote it, is confused, and all the different possibilities. Our users would hate it if we exposed this complexity anyway, so I would rather make things as dumb as possible.
And I think lazy loading is not a requirement, like, it's not on a hot pass, the dependency conflict resolution. But also, imports that are just references, it's natural, right? Why would they be redefining anything?
Josh Suereth 01:05:47 Right, exactly. Okay. So, I think… I think I'll take… I'll take that approach.
I'm gonna expand the test cases in the PR so it's more obvious what's going on, and so you can see. I would take a look at them now, because that's probably what I spent the most amount of time on, was… I mean, I had AI write them because they're annoying, but I spent time making sure the test cases are realistic of things that we have to handle.
So, I'd recommend looking at that. I've been cleaning up the algorithm over time.
I'll look at making imports be, you know, pointers, if you will, or, references. Okay, I do want to briefly mention, by the way.
Please take a look at security vulnerabilities and patches. We have a bunch of them showing up. And related, we actually have security vulnerabilities reported against, Weaver packages, somehow.
It looks like it's… the security vulnerability reported is that we're not reporting security vulnerabilities, so we just need to go in and set up the CI automation to do so.
So, if anyone has time to do that, that'd be awesome.
Laurent Querel 01:06:58 So, Josh, I was thinking that what we… David did yesterday and merged by you, I think, yesterday or today.
Fix the security, issues related to… Related to, TLSSL, obviously not related to UI, so are you referring to, security issues related to UI only, or something else?
Josh Suereth 01:07:27 No, so we… the ones that are related to UI, I think we need to document that we… do not recommend exposing this port publicly, and then just mark all of those as not relevant, and why, and point at our docs. So if our docs say, don't do this, we can say, we're not exposing a security vulnerability because we don't allow the scenario of the security vulnerability with.
Laurent Querel 01:07:49 Okay, okay.
Josh Suereth 01:07:50 But for… we have a… we have a good bit from TLS and GIX and our virtual directory interface, so I want to make sure we're fixing those.
And the… just for context, that PR, the most important bit of it was not tested.
don't have test coverage for it, so I would like to get test coverage around that, and we need.
Laurent Querel 01:08:10 Okay.
Josh Suereth 01:08:11 to it that is not a new vulnerability. So, I don't want zips in our repository anymore. I've started to actually remove the zips, and have a raw directory, and have the test create the zip. I think we should do the same for GET to do VDER tests.
Sound good?
Laurent Querel 01:08:29 Okay. Yeah, I can, talk with David and see… Based on what you just said, if we can add those tests.
Josh Suereth 01:08:40 Yeah, yeah, I merged it already, because I think getting the security vulnerability fixed is more important.
Laurent Querel 01:08:45 Yeah, between TV.
Josh Suereth 01:08:46 And I think he, like, testing it by hand was okay, it's just, I'm nervous we're gonna keep breaking that area.
Weaver is one of the most important things that Weaver has in it, so I want to make sure it's well tested. All right.
Laurent Querel 01:08:58 My question is good. Bye.
