SIG: Configuration WG
Date: 2025-10-27
Duration: 35 minutes
Zoom Recording URL: https://zoom.us/rec/share/vfa-fEGgTm4wXvPHC14gETJ7tJ4RcHrmnpjlA2i_9azHM4if0OpQYK0UJ4cGw2Ef.cR4I_Oz65Nuq7DSp
============================================================

## Zoom Recording Transcript

**jberg** 01:18 What's going on?
**Alex Boten** 01:21 Whoa.
**jberg** 01:22 Can you hear me okay? I'm testing a new AV setup.
**Alex Boten** 01:27 Clear as day.
**Tyler Yahn** 02:18 Hey.
**Alex Boten** 02:20 Hello.
**Tyler Yahn** 02:22 How y'all doin'?
Jack, did you move?
You're muted.
**jberg** 02:37 No, I did not move. Why? Oh, okay. Maybe my camera angle, or maybe I've just been on blur forever.
**Tyler Yahn** 02:43 Maybe. I feel like you were, like, upstairs somewhere at some point, like… but I… yeah, I don't know. It's been years, so who knows? I was just maybe gone delusional, so…
**jberg** 02:53 I didn't… I did move, like…
two and a half years ago, but that's… that's a while. We knew each other before that, so maybe.
**Tyler Yahn** 02:59 Yeah… yeah, I mean, maybe that's what I'm thinking of, but yeah, maybe then you've just been blurred ever since, so…
**jberg** 03:04 Yeah.
**Alex Boten** 03:15 Alright, should we… Should we get started?
**jberg** 03:19 Let's do it.
**Alex Boten** 03:22 I… We already have a thing for today, but…
I think I just forgot to delete this.
**jberg** 03:30 Oh, my bad.
**Alex Boten** 03:31 Yeah, yeah, it's all good.
Yeah, it's because I put my name in the wrong place. Man, today is just not my day. It is, in my defense, 8AM where I am, so, you know, it's still early.
So I just wanted to bring up the one topic, which was this enable-disabled discussion that's going on.
Because if we're going to make any changes to…
Enabled or disabled, we gotta do it now.
And just be okay to live with it.
And this discussion's been going on for…
Almost a year, so it's actually a fairly young discussion in our terms here, but, it's still…
I guess there was discussion about this at the spec. I totally missed it last week. I don't know, Tyler or Jack, if either one of you were at the spec call to talk about it.
**Tyler Yahn** 04:26 Yeah. Or if it was captured there.
**Alex Boten** 04:29 Do you wanna… do you wanna talk about it?
**Tyler Yahn** 04:33 Well, in classic spec fashion, nothing was really decided, but…
Yeah, I mean, there's just… like, the issue hasn't really been resolved.
There's not much… More in the way of, like, conversation that's happened here.
-Oh.
Other than people just…
are starting it back up, like, there's… all the points that have been made are still the ones that are being made, all the points that…
Yeah, so it's like, there's… you know, it was discussed that, like, there's…
good opinions to forward on both sides, and, like, there's not a really good solution here.
**Alex Boten** 05:13 Right.
Right, and as Charles documented, there is a bunch of uses for enabled. As Pablo documented, there's a bunch of uses of enabled. There's one use of disabled.
In the collector… I guess in a couple of different places.
In the kitchen sink, we use disabled.
I guess, should we use enabled to be more aligned with the other examples of it in OTEL, or…
**jberg** 05:47 What really matters for stabilization purposes is, is the top-level Enabled or disabled?
Right? Because the… all the other usages we have in declarative Config are for experimental properties.
**Alex Boten** 06:01 Right.
**Tyler Yahn** 06:06 Yeah, I'd like to… I'd like us to keep…
the… the way it currently is, with disabled, I think there's…
The way… the way defaults are working, and the way defaults work here, I think, is something important to keep in mind. If people don't want to include a double negative, they don't have to include the option at all.
You know, not including the option is the same as just not being there, and that, like, is the same default. If they want to disable something, that's when they include it in the configuration.
I understand that there's, like, this argument being made about use, but that's not really a great argument. I think that just means that…
Opinions have… spread. It doesn't mean that it was the correct opinion from the get-go.
And I think that we want to try to promote making, like, concise,
usage of… concise usage of, like, our configuration, so if not applying something, I think, is important. I think the problem you see when you have enabled included in the configuration is that people will always include it, and it becomes just additional lines in the configuration that aren't needed.
And I think that this is something that we want to try to discourage use. I think that you want to have your configurations to be as concise as possible.
I think that there's…
reason that we could switch. I mean, I think that there's… it's not, like, the end of the world, but I do think that, like.
just saying that, like, it's used in other languages. It doesn't necessarily mean that we should do that here. I think that, like, we should make a decision that, like, is effective,
I understand that, like, the configuration thinks it's important, but, like, there's a translation layer in the configuration, so I'm not exactly sure why that's the end of the world, either.
**jberg** 08:00 So,
I've been of the opinion for a long time that we should be unopinionated in declarative config, and, like, with property names, and with what the scope is of, you know, our data model and things like that, we should just delegate to the spec to the extent that it's possible.
And I guess with respect to this, you know, we made our decision in declarative Config to, you know, go with
You know, naming, enabled or disabled, that reflects the default, because there's language in the spec that suggests that.
And so, I think, you know, for us to…
I just… I don't want it to seem like the spec can go and say, like, hey, declared config, go figure this out for yourselves, because right now, we're following the spec's guidance.
If the spec wants to carve out an exception and be like, okay, this guidance for enabled versus disabled naming only applies to environment variables, then in, you know, basically they're like, hey, explicitly, declarative config, go decide this for yourself, then we can, we can make that decision. But until then, we're just, like, we're just another data point in this discussion, which is happening at the spec level.
So,
Has… has that… is there… is there any indication that the spec wants to do something like that? Or are they just trying to, like…
reach a consensus and, you know, solicit input from declarative config as a part of that consensus reaching process?
**Tyler Yahn** 09:29 Yeah, I mean, I think that that's kind of, like, the whole thing, like… Alex, you say that this conversation's been going on for, like, almost a year, but, like, it hasn't been going on for much longer than that in the…
**Alex Boten** 09:37 Yeah, yeah, like…
**Tyler Yahn** 09:39 like, it came from the spec, right? And so I think, like, what you're seeing now is that, in that sense, people who are, like, unhappy with the decision that was made in the specification are trying to get, like, the next version to change, and so…
Yeah, I don't think that there is, like, there was suggestion that we could change the environment variable, but I don't think that that's, like, a realistic suggestion at this point.
**jberg** 10:03 We can't change the environment variable guidance, but we could, like, say that the guidance and the spec is limited to environment variables, and thus, like, carve out an exception for declarative config to go in a different direction.
**Tyler Yahn** 10:14 Yeah, and I think that's what people are asking, yeah.
**Alex Boten** 10:17 I guess my concern with this particular issue is, is… are we blocked on our release candidate if this decision is not made in the spec? In the sense that, like, going back on this decision, particularly in…
Declarative config would be…
like, a breaking change, and we would have to then release, like, the next major version to be able to support this if it changed, so… I guess…
I think you're right, Jack, I think this decision needs to be made at the spec level, and maybe we can just continue the conversation there. And I guess from our standpoint, you know, we're just, as you said, following what the spec originally had said, for disabling the SDK, so…
You know, if we want to make that change, and it needs to be made there, but…
**jberg** 10:58 That's why… that's where I'm interested in as well, is like, hey, what is the implications for our stability goals? And, like, that's why I brought up that there's…
we don't actually have many usages of it, and all but one usage that we have of a Boolean property are experimental. So there's only one that really matters, and like, you know, this top level disabled, and then, like, you know, even if the spec were to change its guidance, would we want to go back and
You know, publish a new major version, just to change one top-level property.
I like to think not.
But what do you, what do you all think?
**Alex Boten** 11:39 I mean, if it was If it was a top-level property that's changing,
Like, I think we would have to, right? Because it would be a backwards incompatible change at that point.
**jberg** 11:51 We'd have to cut a major version if we wanted to change the naming of it from disabled to enabled.
And maybe, actually, we wouldn't, actually. Maybe we could just, like, you know, we have a disabled property, like, let's say later we want to switch it to enabled.
**Alex Boten** 12:06 You just add enabled in there and respect both of them?
**jberg** 12:08 Well, that's what we have to do in several places. We're gonna have to get used.
**Alex Boten** 12:11 I know.
**jberg** 12:11 of it, actually. Like, if we mess something up in our schema, we're going to have to, like, introduce an alternative name for something, and then have, semantics, like, descriptions of those properties that say, hey, it's only valid to use one or the other. Using both is, like, you know, invalid, and, you know, implementation should throw. Like, a perfect example of this, of where this is going, is with this new, composable sampler.
In the specification. So you have, like, you know, sampler, which you can set on Tracer Provider, and that's, like, the old way of doing things, and then you have Composable Sampler, which we think, like, a lot of people will use in the future. And it's, like, rule-based, and, you know, it's… it's a lot more powerful and things like that. We're going to end up having tracerProvider.sampler.
And probably traceoprovider. Like, composablesampler, or something like that.
And so, you know, and we'll have to say, like, use composable sampler or sampler, but not both.
So I think, like, we're gonna have to get used to this, like, type of thing of,
And we already have it, actually, too. Like, think about this. You can set your resource attributes. You can say, like, hey, here's my list of key value resource attributes, and then you also have, like, what is it, resource attributes list?
**Alex Boten** 13:23 Yep.
**jberg** 13:23 like, where you… which is, like, you know, the string representation that's comma separated, and, you know, the semantics are basically, like, hey, there's two ways to specify this thing, and implementations have to merge them. So, like.
Two ways to specify the same idea happens in our schema today. And, I think disabled as a top-level field is a fine naming of it, but, like, I don't think it would be the end of the world if we ultimately had to switch to enabled, and we already had a stable major version.
**Alex Boten** 13:55 Alright, I will go on record to say that if we have to support enabled and disabled, people will be very unhappy, and I can only imagine how confused users will be by this.
By this functionality. Regardless
how good the implementations are. I, like, this will fuck people over, I'm sure, like, 100%.
**jberg** 14:15 I would vote against adding enabled, like, but, you know, I wouldn't publish a major version if we had to add enabled.
**Alex Boten** 14:24 Right.
Okay, so I will… let… how about we do this? Let's try and get some clarity in this in tomorrow's spec call, and… I… I don't think they should block us.
From the release.
candidate.
**jberg** 14:43 From the release candidate. Like, say more about that. Like, so… I've been out of things for a while, and I know there's, like, a lot more implementations and things are further along. Like, I tried to make this all go stable before I went out on parental leave.
And we weren't quite ready. And so, like, like, just… this is kind of a tangent, or maybe just, like, we're at a place where we can kind of move to the next point of the conversation, but are we feeling closer to actually publishing a stable version of the schema?
**Alex Boten** 15:13 So, I have finally come back to implementing this in the Go implementation, over the past week and a bit.
And I'm finding some amount of changes that need to happen. So, for example, the TLS block that I submitted last week. So that, you know, that'll require a new RC candidate to be created, which is totally fine. I don't think we're very far from
Cutting a, like, a natural release, like a staple release.
At least not as far as I can tell from my implementation, but I know Marilla is working on the JavaScript implementation, so…
She might have different, opinions there.
**MG Marylia Gutierrez** 15:50 Yeah, so for… the only thing that I noticed that…
some things is… maybe it was very based on, like, Java and things like that, because, for example, like, on the SDK,
it separates a lot the packages for things, so even, like, when they say this pack, like, oh, it has to… the create needs to return, like, tracer and logger, provider, and all that stuff. I… I wouldn't… I'm not gonna create, like, one create that returns everything, because it gets too heavy for a single package, and people actually can import different things.
So I'm doing a little, like, adjustments on things, but still making sure that it's still spec compatible.
**jberg** 16:29 On that specific thing, you know, there's obviously, like, wiggle room for language-specific implementation details. I think that's probably within it.
In Java, so we have that same type of concept. We have packages for metrics, traces, and logs individually. And, and so, yeah, what do we do? And so we actually have, also, in addition to those separate packages, we have, like, a composite package, which depends on all three of them, and
you know, has these additional helper classes, that are composites. So we have, like, a single open telemetry object, we call it, which is a composition of tracer provider, meter provider, logger provider, and propagators. And, you know, there's nothing in the spec about that, but we went ahead and built that, because it's, like, way more convenient than having all of your instrumentation except three different things.
Three different providers. And so, yeah, like, all this is to say that, I think there's wiggle room for something like that. The spirit of the spec is, like, hey, you know, you should have a create method that returns, you know, the top-level SDK components from this configuration file.
**MG Marylia Gutierrez** 17:37 Yeah, so the way that I did it was pretty much, I created a new package that is called, like, configuration, that handles both environments or config file.
And then, so if you have, like, the environment for config file.
it parses that, otherwise used for environment variables. So the only thing that it does is just parse and return an object that is called, like, config model, and that's it. So then, whatever you were importing to your other packages, you have your create that just returned this model, and from that, you have the config that you need to create your provider. So then each one can create what is applicable to their own package.
**jberg** 18:14 So is it correct to say, then, that each of the different packages, trace metrics and logs, respectively, will have some logic embedded in it that understands the configuration model and can, like, has a create method?
**MG Marylia Gutierrez** 18:28 Correct.
**jberg** 18:29 Yeah, so that's, like, I think that's a choice. It's like a design choice of, you know, the language and its maintainers. You know, you can either distribute the logic to a bunch of places, or have it centralized.
in one package. In Java, for example, we didn't do that. We have all the logic to interpret the model in one package. And, you know, there's reasons for that, but we don't need to get into them here, but I think it's interesting that different languages are going in different directions based on, you know, what's idiomatic, what makes sense for their users.
**MG Marylia Gutierrez** 18:58 No.
Yeah, and it's been going, like, kind of helpful for some things, because there are…
several things that are, like, not implemented on JavaScript at all, but then when I was creating, like, this package, like, oh, we have this thing now, where should I put this? Or, like, oh, we don't have a package for that, so that is good, you know, opening issues, like, we need to actually implement all those things to actually make it work, so that has been helpful as well.
**jberg** 19:25 That actually… that's… that's really helpful, right? I think, like, a side effect of this whole body of work is that when you have the configuration model laid out in front of you.
it becomes very apparent which things you have and haven't implemented as a language implementation. And so, I think a side effect is that it'll drive more consistency across all the languages, which will only be good for our users.
So… Yeah, that's great.
Alex, any other thoughts on, on this, other than, you know, just going in and, you know, so I guess just to kind of wrap this up, so we want to…
it seems like there's sort of soft consensus that we want to delegate to the spec on this, and if the spec wants to carve out an exception for declarative config, you know, and say that the naming conventions about Boolean properties are only applicable to environment variables, and other configuration interfaces, you know, aren't
don't need to conform to this, then, you know, the conversation can come back down here, and we can actually have a debate about it. But, like, until then, I think it makes sense for us to just say, look, we're just following the spec.
**Alex Boten** 20:34 Yep.
Yeah, I agree. I just added a couple notes in the, in the Google Doc that, you know, we don't think it's necessary to have that decision to cut a stable release and…
We can… we can just let the spec do the spec thing, and… Yeah.
I think that's fine.
Okay, cool, do you want to move on to the next topic?
**jberg** 20:57 Yeah, it's a triage project board, that's part of a copy-paste. Do we have anything new that we want to tr… have we been triaging recently? Should we triage today? Let me just make that clear.
**Tyler Yahn** 21:09 I think it's been a few weeks.
I don't think there's much to triage, though, to be honest. I think probably your meta scheme is the only thing to talk about.
**jberg** 21:25 Yeah, I guess I'm just thinking about whether there's any other… any new…
things that have come up that are potential blockers to stability. That's what I would want to triage, is…
you know.
Like, Alex, for example, you mentioned
we had a conversation in one of your PRs that was like, hey, is there any other discrepancies between the collector and, the configuration model that we should look at now while we still have the chance to before stability? And you were talking about the naming of things like OTLP HTTP exporter, the case specifically. Like, I think we've talked about this before, like, we use Snake Case in declarative Config and,
I tried to figure out what to call the collector's case, and it's… the best thing is, like, mumbled case. It's mumbled case, because there's no separator between the words, no indication that, like, one word is found in a new…
**Alex Boten** 22:16 things.
**jberg** 22:16 For some things, right, it's like…
**Alex Boten** 22:19 Maybe mumbo is the perfect thing, because you never know what you're gonna get, so…
**jberg** 22:23 Yeah, so, like, on that one, I guess I didn't respond to you, I haven't had a chance yet, but, like, you know, even though the collector has, kind of, has a much longer history than this, it's like, I think a lack of consistency around the collector's naming, like, I don't want to kind of carry that forward if we can avoid it, so…
**Alex Boten** 22:40 Yeah.
**jberg** 22:41 That's my opinion there, but…
Okay, so that was an example of, like, you know, something that we should get ahead of before that's potentially blocking stability. Has anybody else come across any of their topics like that, that they think, you know, could throw a wrench in our plans?
Alright.
Then, you know, the next topic is mine. It's, it's about this meta schema. So, a couple weeks ago when we met, it was just, Tyler and I, and so, you know, I've been working on this thing that I'm calling the metaschema,
And, you know, I went into it for about 30 minutes with Tyler, just talking about the PR, what it does, the benefits that we would potentially have from it. And, so I guess…
for this group here, I can either regurgitate some of that information, if you're interested in hearing it, or, you know, I also linked to last week's recording, if that's just, like, a faster way for everybody to consume the information.
But, you know, essentially, this goes back to a couple of things we've touched on today. So, you know, we have these things like,
We have these little bits of the schema which don't fit neatly in JSON schema. Things like default values, things like semantics that, like, prohibit multiple properties being present, or like, you know, how to handle collisions between properties, or merging, or things like that.
And then, you know, things like implementation status.
You know, Marlia, you talked about JavaScript doesn't have support for all of these things. It'd be really nice to see, in a very… in one place.
what the status is across all the languages that have implemented a declarative config for all types and all properties. So, like, how do maintainers capture that information in, like, a centralized place and present it to users? And then, you know, one more example is,
which of our types represent SDK extension plugin interfaces, which things are, like, you know, extendable and can reference, you know, users' custom exporters and processors and things like that. And all of this is information that I think should be captured in what I'm calling the meta schema. And, you know, it's just schema about the schema, or meta, you know, info about the schema, so additional info about the schema. So this PR is
all about, like, build tooling to, and data structures to record this information, and then build tooling to generate artifacts from it. Like, notably, one thing that I do from this is I generate, Markdown, which is documentation for our whole schema. And so, like, when you have the JSON schema and the meta schema, and, you know, you can ensure consistency and validation between those things, like
all the same types are represented, you can do a lot of interesting stuff from a, you know, a programmatic, you know, markdown generation standpoint, so that's one of the things that's in there as well, so…
I don't think it's a blocker for stability, but, you know, Alex, I know we talked about this a while ago, that it would be good to capture some of this stuff in a more structured way, and so these are my thoughts on that.
there's a lot of lines of code in the PR, a lot of it is generated code, so, like, you know, but there is a decent amount of JavaScript as well that's, like, this build tooling, so I'm not sure the best way to consume that.
I don't know, it's, it's, it's… I think I mentioned this somewhere, but it's,
it's build tooling, it's not like schema itself, and so I think it's a much more, malleable asset as, like, a part of the codebase. Like, it's something we can iterate on a lot more, and just, like, you know, revert if we need to, or take it in a different direction, so… as opposed to the JSON schema, which has much, like, broader repercussions if we were to change it, so…
Keep that in mind.
Yeah, if anybody wants to talk about it more, I'm happy to share or share my screen or anything, but if not, we can just kind of move on.
**MG Marylia Gutierrez** 26:43 I was just gonna ask, have you seen the…
well, it's the Metadata Explorer project that is spinning up also in the hotel. So that kind of, like, reminds me a little of that one. I don't know, so if it's something that could be combined?
**jberg** 27:00 I think… I think they should be combined. I've been talking to Jay DeLuca from… from the Java SIG. He's been doing this… this crazy work, so just for other people that aren't involved with Java, so, the Java instrumentation, codebase has, like, well over 100 instrumentations.
And, like, the instrumentations all have their own configuration properties and emit their own telemetry, and, you know, for a user to understand, like, what is configurable and what telemetry is emitted, it's kind of a nightmare for them right now. They have to, like, dive into the code and see it for themselves.
And so Jay's been doing this, like, huge task to create a kind of structured representation for every one of these instrumentation modules. It's kind of like the collector's,
what's a… what's it called? The collector, every single component has a little, like, YAML file that describes, like, what it emits and what's configurable, something like that. And, you know, just like…
just like the collector probably has, you can take this structured representation and do all sorts of cool, like, you know, markdown generation from it. And so…
yeah, that's like… there's an interesting parallel. They're trying to do the same thing as we… as I am, and at least there's some overlap, so,
I don't know exactly how it's gonna overlap, like, I know Gregor's also working on declarative config to some extent, so, his mind's on both of these things, but, you know, the thing that we want to make better for our users is,
is not, like, understanding the full array of what is configurable, and making it easy to understand how you actually do that. So, both of these projects are kind of in that same…
Up that same alley, so we should collaborate.
**MG Marylia Gutierrez** 28:46 Yeah, because he's both looking at, like, he started with the Java, and now he's looking at a few other SDKs as well, and he's also… we are talking with the…
Also, on the, like, docs level, how we can actually use this to show official documentation so people don't have to create it.
And, well, you can talk also internally with us, because me, Jay, and Greg are all on the same team.
**jberg** 29:09 Yup.
**MG Marylia Gutierrez** 29:10 Yeah, yeah.
**jberg** 29:13 Starting very soon.
**Tyler Yahn** 29:17 Jack, I don't know if you saw, we also had talked about Weaver possible usage, and that Lude Miller had responded.
**jberg** 29:23 I did see that. What did you make of that? So…
For others… go ahead, Tyler.
**Tyler Yahn** 29:30 Yeah, I think the idea was to try to use it as some sort of, like, generic parser of schema into, like, something else, but the middle of this thing, it was so tied to semantic conventions that she would recommend not doing that, and just going with what we already have with the JavaScript, is my understanding.
**jberg** 29:44 That's… that's… that was my read of it as well, but it's good to hear it from the horse's mouth, right? So…
**Tyler Yahn** 29:51 Yeah, yeah, that's what I figured, yeah, so…
**Alex Boten** 29:54 We're gonna have a…
**Tyler Yahn** 29:54 It's.
**Alex Boten** 29:55 We're gonna soon need a standard for, code generation…
schema parsing tools within OTEL, because we're gonna have, like, a fourth one.
Spinning up here, if we keep.
**jberg** 30:06 Yeah, and then we'll have to rebuild it in Rust.
So, that would be a fifth.
**Alex Boten** 30:10 That's right.
**Tyler Yahn** 30:12 Yeah, we'll call it Open Weaver.
**Alex Boten** 30:14 Open waiver. There we go. There you go.
**Tyler Yahn** 30:22 Yeah, you shake your head. Just wait.
**Alex Boten** 30:24 I am. I was trying to think of, like, you know, calling it even more… an even more confusing name, like Weaver with two E's or something, instead of W-E-A.
**Tyler Yahn** 30:35 That'd be a good one.
But yeah, other than that, Jack, it still looks good. I'm in favor of the… I don't know how we want to progress it going forward, I guess, is maybe the next question.
**jberg** 30:45 If you all wanna… if anybody wants to rubber stamp it,
like, I guess it's hard to articulate this type of thing, but, like, I'm on board to find the bugs and fix the bugs and, like, roll forward with this thing. And, like, you know, if people have comments about it, like, you know, it's… it's…
it's a very… like I said, it's very malleable right now, and it's not being, like, you know, consumed by OpenTelemetry.io. Those are all, like, future things, so,
Yeah, just depends on what folks want to do.
We could try to make it perfect, or we could try and make it, like, okay and iterate.
**Tyler Yahn** 31:22 If you get the reviews, we're good with merging it, though, is what you're saying?
**jberg** 31:25 I'm good with merge… well, yeah, yeah, exactly. There's a follow-up draft PR, actually,
that, maybe I should just kind of merge into one PR if it's all going to be rubber-stamped anyways, but, like, you know, I tried to break it up to some extent and, you know, do the language implementation status bit. I talked about tracking that as a piece of metadata. I tried to do that as, like, a separate bit of work, but, like.
I don't know, it's like…
both PRs end up being big, and they, like, all touch the same thing, so maybe it should just be one big, nasty one.
**Alex Boten** 32:01 If you… if you can wait until tomorrow to merge it, I'll… I'll spend some time actually reviewing your presentation from last week, and then reviewing the PR today, and then we can move forward with it.
**jberg** 32:15 Much appreciated, Alex.
**Tyler Yahn** 32:19 Yeah, I'll try to get a review in as well, and then I… please don't merge the two PRs.
Let's just leave it at the 1.
**jberg** 32:25 Okay. Perfect.
**Tyler Yahn** 32:26 Merge the PR later, but don't, yeah, don't put the two together, yeah.
**jberg** 32:29 The problem is the second PR, like, I improved some of the core bits of the first PR, so it's like, I don't know. That's the only reason why, like, you know, when I was making it better, making it more generic to support tracking language implementation status, it's like, I realized some flaws in my original thinking. So, I don't know.
**Tyler Yahn** 32:48 Gotcha.
**jberg** 32:52 I'll leave it… I'll leave it as 2, though, and just qualify it and say things are already getting better than what you see.
**Tyler Yahn** 33:01 Yeah, sounds good.
**jberg** 33:04 Alright, any other topics?
Alright, well then, let's give everyone 30 minutes back.
**Alex Boten** 33:16 Alright.
**jberg** 33:16 Thanks a lot.
**Tyler Yahn** 33:17 Bye, everyone.
