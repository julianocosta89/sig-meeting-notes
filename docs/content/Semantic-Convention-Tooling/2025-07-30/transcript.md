SIG: Semantic Convention Tooling
Date: 2025-07-30
Duration: 61 minutes
============================================================

## Zoom Recording Transcript

Josh Suereth 00:03:14 Morning, everybody.
Jay DeLuca 00:03:34 I don't think we've met. I'm
Laurent Quérel 00:03:36 Bye, guys.
Jay DeLuca 00:03:36 Legit.
I work at a grafana. I have a a quick topic. I was hoping to
to cover in the 1st half, if possible.
Josh Suereth 00:03:45 Yeah, yeah, we can. I'm I'm waiting for the the Google Doc to load here. And then we're gonna get started. We're usually a little late on this meeting, because it's it's early in pacific time.
and then I usually have meetings before this one. So apologies
so we usually start about 5 min late, generally.
and then we also go over which we will try to avoid today.
Alright, let's go back to normal.
So if you want. Throw your
item in the agenda. We normally start with triage. But since you're new and you have a topic, you want to get done, let's do that
new topic.
And then other topics.
So
2.
Alright oh, I'm not presenting yet, am I?
Yeah.
Jake, do you need to
Do you need to present for your for your topic, or do you? Do you want me to present.
Jay DeLuca 00:05:05 Yeah.
Josh Suereth 00:05:06 You do.
Jay DeLuca 00:05:06 I would like to present, if possible.
Josh Suereth 00:05:08 Yeah, yeah, go for it.
I think we have enough folks here, so why don't you take it away?
Jay DeLuca 00:05:14 Cool.
Yeah. So I'm I'm Jay. I've
My camera doesn't seem to be staying on. But I I work at Grafana, and I am active in the Java Sig.
I've been spending the past few months. Can you guys see my screen.
Laurent Quérel 00:05:34 Yes.
Jay DeLuca 00:05:34 I've been spending the past few months
working through the Java instrumentation with the hope of demystifying some of it. So for for people who may not know
a lot of the instrumentation can be almost implicit in terms of like what is instrumented under the hood. There's a lot of different
configurations that result in different
telemetry being emitted. So I've been working through trying to come up with a way to document
like given an instrumentation. What you can expect from it in terms of what libraries are covered, what other like? If there's a Java version that's specific, and then the telemetry signals in terms of what's emitted by default, or what might be emitted behind certain feature flags.
And so I have built a system that does some analysis on static code. It looks at gradle files for dependencies. And then I've started building in a system that actually intercepts test runs, grabs the emitted telemetry data. And then basically documents, them
and I've started putting together like a basic ui to just kind of talk about or to demonstrate, like some of the things that we can do with that data in terms of displaying the attributes so like. But, for example, for this click house client by default.
you get spans with you, get client spans with these attributes. Only 2 of them actually adhere to semantic conventions. But we can see if you enable this configuration flag that says opt into the stable
database, semantic conventions. We can see that not only do you get the same span, but with compliant attributes, but you also get a new metric and then the ability to then
diff between agent versions. So like, for example, coming up, we have a 3 out release where we're gonna go stable on many of the semantic conventions. And so that's gonna result in a ton of
behavior differences. So the idea here being and this is just a proof of concept. This is not necessarily something that we wanna continue with. But this is just to kind of demonstrate what we can do with this data. Once we have it, and then potentially
potentially generate documentation and things like that. And so yeah, so I've been working through this for a few months, and I've I've been following along with Weaver, and I know that there's a lot of overlap in terms of, I think some of the goals and and things like that. And so what I wanted to do was just to kind of start a discussion around like how this might fit in with Weaver. So like, for example, one of the things that I want to do is
generate documentation for all of these modules. And so I did start experimenting with one of our instrumentations, and converted it over to use Weaver to generate the metrics and and some of the like. The docs for the the metrics embedded things like that. And yeah, I had some questions like, well, 1st of all, I wanted to to get some
just initial feedback in terms of
like if you had any glaring thoughts around the goals of this or the way that I've been going about it. The the yaml file itself is is pretty much Java specific. And I've
I haven't really thought about other languages, but ideally like, if if there is like more of a unified approach to this. I want to
help contribute to to fleshing that out and and move in that direction. But wasn't really sure exactly where to start. Necessarily.
but yeah, so I'll pause there.
Josh Suereth 00:09:29 I'll jump in real quick. Yeah, this is so what you're trying to do with like defining the telemetry and what's generated and having dips and things absolutely. Weaver wants to support you in. In doing that, I think the only difference between what Weaver has and what you're doing is you're actually trying to track like versions of the agent.
Jay DeLuca 00:09:50 Yes.
Josh Suereth 00:09:50 Right and and maybe versions of a library that are supported.
So that that's something that like I think we would.
We want Weaver to support this right? We want Weaver to be a tool that you can use, that we have these diff algorithms that we're not reinventing the wheel on a per language basis for all this stuff.
We want Weaver to be that tool for, like the collector for the Java agent for everything. How we get there is the next step, and like what we can do to support you. I am really curious to hear your feedback on like using weaver. Right now, weaver is a. It's real dumb.
It's it's smart in some ways, but it's real dumb. We basically resolve a yaml file
into a big registry, and then we shove it at things that deal with Json data like rego policies
like ginger templates.
We don't have like out of the box. Jinja templates yet right? We don't necessarily have out of the box rego policies. Everything comes from like semconf. So
Since you're already self servicing like you're actually kind of in a target audience for us to say, Hey, what do we need to do for the Java ecosystem and come figure that out within weaver and then help us build the like out of the box. Java experience
for weaver.
If that makes sense.
Jay DeLuca 00:11:15 Yes, yeah, and that's exactly what I want to do. And and yeah, so I yesterday, I I did this implementation. And yeah, I had to write, you know custom, Jinja templates and and try and come up with a way to do the code generation that's like scalable. And and I'm I'm certainly interested in helping push this forward and and figuring out, like, you know, a way to make this generalized and and I had some questions about like
for a project like the instrumentation Repo, where we have almost 200 or over 250 different
modules like, would would each one of these have a separate registry, or would there be some kind of master registry? And then
I I would imagine that, like for for shared templates and things I should be able to have like kind of a generalized common one that could be referenced. But what what are the thoughts there.
Josh Suereth 00:12:08 Yeah, if someone else wants to jump in, feel free, I'll just say real quickly. You have a lot of flexibility here. I think our initial thinking is you would use the Semantic convention repository as a dependency, and you would import it.
and then you would kind of override that dependency to say like, Hey this this you know Aka library that you were showing, or this what's what's the one up there? I can't see any of the closer one. Anyway, you'd pick a library that you're supporting. Yeah, the the oracle. Ucp, right? You would say this one uses this metric, and you'd like enrich it with some things.
If you wanted to keep that all in one location, or you wanted to have individual locations for all the templates. That's kind of a a decision
on on you as as a project, if you will, weaver should support either one.
But in terms of how you would like leverage consistency from semcom, you would use it as a dependency. I don't know if anyone else wants to jump in with their thoughts. That's the only one I wanted to call out.
Laurent Quérel 00:13:11 I have some feedback also the
so I think the templates and the
under legal policies for custom policies.
So for libraries or things like that anything that is not semantic convention.
We, in fact, only need one
that could be applied to each of the the custom policies that will match
with each library that you are importing.
So that's that's the something that we described at some point in some documentation.
Right now we have a support for custom policies.
but we unfortunately don't have yet the the corresponding default templates and default policies. It's probably relatively easy to do, derived from what we did in the Semantic Convention Project. But that's something missing like Josh mentioned.
I think the for me this subject is fantastic. The the idea of having a schema driven approach
for a full development composed of many dependencies.
Again, that's the the origin of this project we were.
We are not yet there. But
I think what would be fantastic is to share a common format. So we we have this 70 convention format. We are working right now on the
version. 2 of this schema ideally having a common
or presentation between this project and what we do in river. I think that's fundamentally a 1st step.
We have a support for annotations
that could be used to represent some element that we have here.
My understanding of what you just described is
very focused on Java. So I guess, there are some
introspection. There are some element that you mentioned that are probably easy to do in Java, not necessarily for every languages. So having a source of truth that could most of the time, indeed.
the the Yaml representation, and you derive from it.
instead of creating or inferring the
what you observe from an existing library. I think that these 2 worlds should exist because we have existing
libraries, but I think moving in the direction where authors of library could define their own description
with with all the detail, with the right description. I think we will definitely make sense.
The the inferring part. I think that would be very nice if we could.
put that into Weaver. So we already have things like weaver registry live check.
having something like with a registry. Live and fail
we we will will be really cool. I think that's what you are doing by listening to the
the what is produced by the unit test or integration test. If I'm if I'm okay.
Yeah. So that's typically the the type of capabilities that we either prototype or we. We thought about it. But they are not necessarily ready in river right now, and and like Josh said.
either we help or other people help us to to to achieve that as soon as possible in river.
I think at the end that's definitively good for spoil you and.
Jay DeLuca 00:17:08 Cool. Yeah. And and so just for context, like, so what I have is when when the tests run they they write these like temporary telemetry files with the the metrics that are, or spans that are done, and then I annotate them essentially with any configuration values that were were set when the tests were run. And so I'm interested also. And we don't talk about today. But in terms of like, I think I've seen a lot about how you would
define and document metrics. But I'm curious about ways to document and describe their different spans that might be emitted from from different instrumentations and like. So right now, I've basically just been doing the span kind
and then basically a set of all attributes emitted by that particular kind, but
I don't know if there's ways or or ideas around making this a little bit more descriptive or or granular.
Josh Suereth 00:18:06 Hey? This has been a thorn in our side for a really long time. So you're not. You're not alone.
Jay DeLuca 00:18:13 Yeah.
Josh Suereth 00:18:14 The miller had a proposal that we're we're experimenting with, where we might add something in Otlp itself
to denote, and I forget what we called it? Was it span type?
Is that what we decided on.
Liudmila Molkova 00:18:31 Think, yeah, because we call everything typed now, right?
Josh Suereth 00:18:36 There's types, and there's kinds. And then once you get, you need something else. You do super kinds. Just so, you know.
anyway.
Yeah. So so there might be like span name, unfortunately, is too granular for what you want. So we might invent something called span type.
and in semantic conventions, we would have the ability to say like, this is a Http client span, and that would be the type. So kind would be client type would be Http client.
So it's more refined than kind, right?
and that that is the thing that we're trying to kind of make progress on and execute against. We have some prototypes around it for Weaver, where you'd be able to specify these as as a thing. We don't have a place to put it in Otlp yet. That's like a thing that we need to do for like live check to work. So like you would actually expect that value to show up at Runtime.
So you can validate that like this is that this is this kind of span. You can bundle spans. By that you could. You could automatically generate metrics on them. You know, with that kind. That's the thing we're thinking about actually proposing through all hotel, because the problem is so systemic
of, how do I identify what you know? The kind of spend or the type of spend? Yeah.
Jay DeLuca 00:19:58 Yeah. And I, I tried to do like a very naive implementation here, where I tried to infer it, based on the attributes. But there's so many attributes that exist across multiple that at least in my naive implementation, I wasn't able to get anything good going there. But
okay, cool. And then I think.
oh, the the last and up
time check! Do I have another 2 min, or I can also end it. There.
Josh Suereth 00:20:23 Yeah, you can. I think I think so. We have. The the next topic we have if I look, is actually the V 2 schema, where we will be talking about spanned type
and other things. So it's it's it's somewhat related. But I think, yeah, let's let's spend. Let's take another 5 min to to walk through this. Anyone else have other pressing topics. I didn't see anything else in the agenda.
Jeremy Blythe 00:20:45 I was just gonna
point out something on this that I noticed. So I think you said, if you go back to your Java code. I think you were showing
that you were creating in Yaml. Yes, at that.
That is like a capture of the telemetry. That would. That will be. Send that you would send
that you're then comparing against in order to check for compliance. Is that right?
Jay DeLuca 00:21:11 Yes.
Jeremy Blythe 00:21:12 Okay, if that was written or transformed into the Json format.
you can actually send a Json into live check and give it the registry.
Yeah, it was.
Give it that in Json form and live check will actually give you all of the rich information about
pass and fail and regular policies and all of that. So you're.
Jay DeLuca 00:21:35 Yeah. And that's that's that's on my to do list. I was, I was actually planning on on figuring out what I needed to do to to put this in a shape where I could just pass it to live. Check. And I I hadn't gotten to the point where it need to be Jason yet. So that's that's helpful. Thank you.
Jeremy Blythe 00:21:48 Alright!
Jay DeLuca 00:21:49 But not yeah. So the last thing that I wanted to to ask about was so one of the other things that we're doing in Java is the so part of the way that this works is we've created these like metadata files. And the idea being that, like
we have all the human, the stuff that needs to be import put by a human in the metadata file. We have the telemetry interceptors that that grab the data from the test. And then we have some code that basically puts it all together and generates the Yaml. But one of the things that we want to take further is potentially doing code generation for configurations
in terms of like, we can define them in Yaml and then and then generate the code, because because right now it's kind of all over the place. And I mean, I see how I could create just General Jinja Templates. But I wasn't sure that I came across any kind of like Yaml specifications for configurations in general. Just curious if if that was something that might be on the roadmap
to incorporate into any of this. I know it's not necessarily semantic convention related, but.
Liudmila Molkova 00:22:55 Oh, it is
so. We have some discussions in semantic conventions, and also some there's Jack who works on configuration that
actually the semantic conventions would be the better source of truth for instrumentation, related configuration options
exactly before the quadrant. So, for example, we say, something is obtained, right.
The attribute is opt in immediately. We should have a means to describe how to opt in inside. Yaml.
yeah. And it may be tricky sometimes it's trivial but
we, the Codegen, should go and know about this flag right? Based on the schema definition. And it should
write the code that that inter interacts with configuration to check if this flag is on or get the value of something.
So we didn't explore it. I I will look up some issues, but it sounds like
we have a path, and it's non. It seems non controversial, but 0 work has been done.
Jay DeLuca 00:24:11 Cool. Yeah, like, I'll I'll dig for some of those issues, too. Maybe it's something that I can help out with.
Liudmila Molkova 00:24:17 Very cool. So yeah,
Jay DeLuca 00:24:19 I yeah. So I just wanted to kind of break the ice here and introduce myself. I'm gonna be kind of hacking away at this, and hoping to make it a little bit more weaver focused. And and if there's anything that I can do in terms of helping drive progress for other languages, too. You know. Let me know. Or if there's other people I should talk to. But
thanks thanks for for your time and and all the input here appreciate it.
Josh Suereth 00:24:48 Yeah, thank
man. I will say, it's awesome when a whole bunch of people have similar ideas, and we can all work together to make it happen. So really looking forward to it.
Jay DeLuca 00:24:58 Cool thanks guys.
Josh Suereth 00:25:02 Tell your Pm's. We solve the problem of remediation. Huh?
Nathan Smith @ Elastic Observability 00:25:07 That's what my whole career. It's always been like, yeah, we can show you where the problems are. But we gotta. We gotta make it so they can click the button, and it'll fix everything.
you know. That's that's what that's what my Pm's have been asking for my whole career. So now, now we have that button where we can
look at. Here's the configuration change that will solve your problem. Boom!
I really like it. It's nice.
Josh Suereth 00:25:31 Nice.
All right. Let's let's get into semantic convention. Tooling.
Is my! Is this sharing? Now?
Laurent Quérel 00:25:47 It's back.
Josh Suereth 00:25:48 Trent.
Let's do about 5 min. Okay, Josh, you can hear me.
Laurent Quérel 00:25:54 Yes, you can see now the this, the shared screen.
Josh Suereth 00:25:59 Yeah, I think I'm gonna I'm gonna skip the Semcom triage board because it's mostly about
v 2 schema, which I want to have a direct discussion on. But let's just look through Weaver quick, and see if there's anything we should be tackling.
and the bug lists, and in things that are coming in.
Okay, so to consider for next release, I actually added a few things here.
one is Jq semcom signal does not filter deprecated.
I think this is actually a pretty quick fix. I actually labeled this as good 1st issue and a bug. But I do think we should probably try to fix this soon.
Liudmila Molkova 00:26:41 Is it already?
I might have.
Josh Suereth 00:26:44 Is it.
Laurent Quérel 00:26:45 It was open 2 weeks ago. So maybe you did fix this.
Liudmila Molkova 00:26:49 Oh, weeks ago. Interesting. Okay.
can you assign it to me? It's either a bug in what I've done or it's trivial. And
I already worked on it.
Josh Suereth 00:27:05 Okay, yep, done.
Let's see. I think that was it that came in that I threw into to consider for next release. We for registry diff template extension, weirdness. These are all other things that we've kind of already discussed. So they're still on to consider. If if folks have time to get to them, and then, I believe.
what was new we had replace conditionally required requirement with level and conditions.
We can talk about this when we do.
V. 2, schema.
because that that is a anyway, it's an interesting part of the Yaml
attribute. Group usage v. 2, Aka bundles
that we can talk about later, too, that one's related to the V 2 schema indicate. If attribute is user definable. I think that's
I didn't actually triage these sorry ahead of time. So we're we're kind of looking at them. We're all
which attributes are set based on user, input which ones are solely driven by the system this is related to, we had a request to do like Pii tracking of attributes.
or I know internally we have a fine grain set of things where we can say
what the purpose of meaning are of attributes are, so that you can actually do fine grained understanding of redaction and that kind of crap.
I feel like this needs more needs a proposal.
Laurent Quérel 00:28:46 Not not, we think that that could be a good opportunity to define
a new type of object into the the semantic convention format describing annotations.
And then we could imagine that for for this specific stuff
we can come with a default set of annotation related to Pii, a default set of annotation related to, for example, what
did regarding metric and defining range for for metric values and distribution? This kind of stuff?
I think we could imagine so many ways to extend semantic convention, that for this kind of thing that are not central.
coming with an annotation object that could describe the intent and let Tool comply with that, I think, would be nice.
Josh Suereth 00:29:52 I agree. So if I can rephrase what you're saying
why don't we start with building out that kind of a feature set with pure annotations in weaver, and then see see what we want to standardize from there.
Laurent Quérel 00:30:06 Yeah.
Josh Suereth 00:30:07 Yeah, yeah, totally agree. That sounds that sounds like a good response. Okay,
we're almost out of time. Box scope shouldn't require attributes. This is one that I asked to kind of hold off on
just because and and I want to run this by the rest of the maintainers.
there's a there's a pr associated with this. And basically what it's doing is it's changing the validation rules for group around scope
where you can define a scope without attributes. However.
as far as I understand, no one is defining instrumentation scope today in semantic conventions. And also, I think we need to sort out our set of rules and validations and how to interact with scope before we start really pushing on it. So I kind of don't want to make a lot of changes.
Liudmila Molkova 00:30:59 Do? Do we have scope and we do. Schema.
Can you define.
Josh Suereth 00:31:06 You. You can define a group type of scope today that already.
Liudmila Molkova 00:31:09 Are we not.
Josh Suereth 00:31:12 Could do disable it. Yeah.
Liudmila Molkova 00:31:16 Then we we keep it in v. 1. In case somebody external did. But in v. 2 we would not even introduce it. I think we will need to be able to define scopes. It's just we. We don't have them, and many languages don't properly support attributes on scopes, anyway. So.
Josh Suereth 00:31:35 Yep, I.
Liudmila Molkova 00:31:36 Honest and small.
Josh Suereth 00:31:38 I I think I think this is one of those deals where I'd rather be conservative. And let's make sure our core use cases are well supported before we expand.
and so scope is one I want us to be carefully
treading into as opposed to like. I like, I'd almost say like, Please stop using scope for now, and we'll add it as a feature later.
Yeah.
Liudmila Molkova 00:32:00 Yeah. And I think this not adding it into v, 2 would be this signal.
Josh Suereth 00:32:06 Okay?
Cool. So
we had some stuff on metric aggregation. But we already just discussed that last time. I think that's all the new stuff that we're
needed to go through. Let's start talking about the V 2. Schema
Oh, who added metric name or name.
Laurent Quérel 00:32:34 No, I didn't.
Hi! Dude.
Josh Suereth 00:32:39 Yeah, I think I call it name now, right?
Laurent Quérel 00:32:44 Okay.
Sorry.
Josh Suereth 00:32:45 Yeah, here, let's let's let's pull up the pr
I, what I wanted to do was kind of walk through
walk through some of Ludmillan's comments because they were good usual. And
I was a little bit lazy in this pull request, and we have an opportunity to just cut stuff
and add it in later if we need it. Because the way I'm thinking about this version, 2 of the specification
is, we put it out there
as, and I can actually add a warning to this if someone uses it that says it's not stable, and it could break at any time.
So you get a warning if you use version 2,
but we can put it out there. We can start trying it out. We can start trying to move semcom to it and see what it feels like, and we can evolve it because I do want to take time to get this right before we commit to it.
Which means I would prefer to cut. Oh, here I'm on the wrong tab. I'd prefer to cut things that we're not sure of until we know we need them.
Alright. So if we go.
Laurent Quérel 00:33:52 One question regarding that I mean, I totally agree with the approach.
The the only question regarding that is
right. Now we start by applying steam Iv. 2
directly at the Semantic convention level, not for the reserve schema resolution.
Josh Suereth 00:34:09 Yeah. But if we start to apply Scheme Iv to.
Laurent Quérel 00:34:13 To the the end of the the pipeline.
Then we will have to support what is supported in Scalia? v. 1.
So the question is
So knowing that that would work
Josh Suereth 00:34:31 I I think we have some options there, Lauren. I don't think it's binary like one thing we can do.
Laurent Quérel 00:34:36 I agree it's not necessary. By the way, we could duplicate the the reserve scheme now with more. No attributes, no field. I agree.
Josh Suereth 00:34:44 We'll know.
Laurent Quérel 00:34:45 Sure that everyone is aware of that.
Josh Suereth 00:34:47 I think we could actually make it so. You can't use v. 2, unless all of your sources are v. 2. So as long as your sources are still v. 1, you're stuck on v. 1. We could also make it so you can use v 1 as long as you're not using features inexpressible in v. 2. So we can actually add warnings in v. 1 to say, Hey, this won't be supported in v. 2.
And then, when we translate to V 2, we just drop it right? So that's that's partly why I think we have to do the exercise. And I want to start at the the entrance gate, because if we know what we cut in the entrance gate, we know what we can cut in the exit gate, and then we can work our way backwards to warnings and errors and things like that. So.
Laurent Quérel 00:35:23 Yeah, okay.
Liudmila Molkova 00:35:24 The good news is that I think there are very few features that we can cut. That somebody uses bad events is one of them.
and I cannot. I don't even remember if there are any other examples of what we use today. But we would like to drop.
Josh Suereth 00:35:45 Yep.
Okay. So tag, well, let's just go through each one individually. For an attribute reference.
I think we have to keep the reference
brief and examples. Also, I think we keep them as is.
if there are fixes we want to make to examples, we might need to make a v 2 version of examples. But
we can discuss that
tag is something that that Ludmilla proposed removing. And I agree we should just cut like we aren't using tags today. We aren't sure why we'd use tags given. We have annotations now. Right? So let's move to general purpose annotations. Let's get rid of tag
requirement level we need to keep.
We might make changes to it, but we need to keep it
sampling relevant, I think, needs to stay
what I was curious about was sampling relevant.
Should we have an attribute ref structure, specific for spans that has sampling, relevant
and all other attribute references? Don't have sampling relevant
so that we have. So it's very clear
to users what's going on right.
Laurent Quérel 00:37:04 So this something relevant is a new a new field into attribute, or I was not aware of this one.
Josh Suereth 00:37:10 No no sampling, relevant exists today.
Laurent Quérel 00:37:12 Okay.
Josh Suereth 00:37:13 And it exists on all attributes.
but it really gets. It's only used in spans.
and if you use it anywhere else, you get an error.
Laurent Quérel 00:37:22 Hmm.
Josh Suereth 00:37:23 So why don't we just like I can make it a span, attribute ref that has an attribute ref in it.
and like a flat naturally ref that just allows. The only thing it does is it allows sampling relevant to be defined.
Laurent Quérel 00:37:39 Yeah.
And then we can leverage all the.
Josh Suereth 00:37:42 Yeah.
Laurent Quérel 00:37:43 The mechanism in place for the schema validation
without having to create a post validation.
Josh Suereth 00:37:52 Yeah, exactly. Exactly like that's 1 of the goals of this new structure is we don't really need validation outside of the the actual schema if we can help it.
Okay.
Next, it would be note, which I think stays and stability stays.
One question.
Laurent Quérel 00:38:19 Again. Sorry for the for the attribute. I'm just trying to
to double check if there are any other indirect
2 sequences. So an attribute that is designed for span could not be reused
for a metric, or for an event, or for.
Josh Suereth 00:38:42 No, this is an attribute. Ref.
Now, that's another.
Yeah, okay, okay, we should talk about. But like.
A definition and a reference are actually separate structures.
Laurent Quérel 00:38:53 Yeah, okay.
Josh Suereth 00:38:54 So this is just references can have sampling relevant flags in them.
And yeah, we'd have to. We'd have to sort out what that looks like, and what that means, if if you're defining. But I actually don't think we should allow referencing attributes from a signal directly, we should only allow it from the attributes portion of the of the new
Yaml.
I I'll show you why, because I think it actually with the new syntax. I don't think this is a burden on users, but we.
Laurent Quérel 00:39:27 We've lived.
Josh Suereth 00:39:27 Let's talk through that, because that's a question you had. That, I think is really good. Let's get through some of the rest of Ludmilla's questions here.
Stability, I think we need to keep, and the reason it's optional is again, this is a reference.
So stability is required on the definition. It is optional on a reference, because it's an override. Anything that's an override is optional.
this here, this option deprecated thing. Do we need back compat with string case and v. 2. I think the answer is probably no. The reason I had it was to make it fully like easy to just copy paste crap
as a translation, but we can remove that and just not not use the string.
Crazy version in v. 2.
Anyone have concerns with this.
Laurent Quérel 00:40:21 Yeah, that there there is a an option related to a behavior
that Crd will use to deserialize. You can say every unknown field will be just ignored.
So, for example, that will cover what you just said if you copy past.
But I think what I used in the in the semantic convention. One was the other option. When you can say, if there is any field that are known, please raise a specific error.
Josh Suereth 00:40:56 So that's a question that maybe we need to.
No.
Laurent Quérel 00:40:59 To answer for schema. V. 2.
Josh Suereth 00:41:01 But I think we.
Liudmila Molkova 00:41:05 Yeah, we don't need to make v, 2
compatible with all semantic conventions. Right? We will not transform all semantic conventions into v, 2. And currently, in semantic conventions. We don't have string deprecated things.
We remove them.
Josh Suereth 00:41:24 Yep.
Liudmila Molkova 00:41:24 So we we don't need to keep any support with this. We can just remove support for the string in v. 2.
Josh Suereth 00:41:32 Yeah, I'm on board with this, and I can't see a reason why to keep it outside of. If somebody's still using strings, it's easier to copy paste, but I don't. Yeah, I don't think it's worth it. So I'm a fan of deleting this.
Laurent Quérel 00:41:46 Stay there. Do we want to to enable this option in 30 to say.
if we, if we ignore, or if we generate an error when the field is not defined into this
attribute? Ref script.
What what behavior do we expect with schema? V. 2. Regarding field that are not defined into the schema that could be observed into the.
Josh Suereth 00:42:11 Behavior. Yeah, like, I think, yeah, I think the V 2 schema makes it even better.
because it'll be very crisp. What things are expected.
Laurent Quérel 00:42:19 Yes.
Josh Suereth 00:42:20 In various locations.
Laurent Quérel 00:42:23 Yeah, perfect. Okay, makes sense.
Josh Suereth 00:42:26 Okay, the next one was prefix. I thought I had deleted this, so apologies.
Liudmila Molkova 00:42:32 It's big.
Josh Suereth 00:42:33 No. Brainer. Yeah, what?
Liudmila Molkova 00:42:35 It became Boolean somehow. I'm not sure. But yeah.
Josh Suereth 00:42:39 That might have been I. I may have been using some AI here. So apologies but I did some copy paste stuff that should be deleted.
annotations. I think the only change I made, by the way, is, everything is now consistently a B tree.
We were inconsistent about btree versus Hashmap. And yeah.
Laurent Quérel 00:42:59 Yeah, that's not much of it at all.
Just just for the test, for example, it's a
much easier to always have the same order.
No, no.
Josh Suereth 00:43:08 The other thing is, I'm leveraging a notion of common fields. So brief. Note and attributes. What I did in v. 2 is, there is a flattened structure that is the same, for everywhere that will require brief note and attributes
on everything.
Laurent Quérel 00:43:27 Is.
Josh Suereth 00:43:27 But I think so. Basically, here we'd remove tag
examples would remain. Type will remain as is unless we want to make changes to type and key would remain. And I think that's the definition of an attribute.
Laurent Quérel 00:43:41 Why annotation are not in the common fields.
Josh Suereth 00:43:45 Annotate annotate. When I say attributes, I meant annotations. That's that.
Let me fix that.
Laurent Quérel 00:43:51 Thank you.
Josh Suereth 00:43:53 Attributes to annotations. Yep, good call.
Yeah, I can. If you want to see, I'll show you common fields, real quick. So common fields, I think is in MoD.
It is brief. Note, stability deprecated. This is, yeah.
Remove string based deprecation options from let's see one here.
And then yeah, and annotate annotations, which is now a B tree.
What? I wasn't sure
I wasn't sure about this one. Lauren is like, Do do we need to have option. B tree everywhere, or can we just have empty B trees? I think we run into problems with lineage.
Laurent Quérel 00:44:46 Yeah, I agree. I think having an Tb, 3 will be much more pleasant, for the developer side doesn't
make any change for the semantic convention at all. So yes, I agree.
Josh Suereth 00:45:00 Okay.
Laurent Quérel 00:45:01 For collection, we should use directly the collection and not the option collection.
Josh Suereth 00:45:08 Yep, okay, I'll I'll move. I'll move that consistently across this, and then
let's talk about this a little bit, so
it might make sense if I show you the the actual yaml. But in the new Yaml
you cannot define an attribute in a signal anymore.
Okay? So in here, and you only see this in the entities, one. Because I was lazy in my test here, but you can only define refs to attributes in sections that expect attributes
right?
And if we do spans where we have a span ref that includes whether or not it's relevant for stability
only spans will be able to define that in a reference, and all attributes are defined here separately from all the signals. And it's linked, I actually think, from from using this. And like moving some repositories around, I no longer find it a pain in the butt to define attributes in one spot and reference them in another. I actually find that it's a bit nicer, because attributes can bloat in size of meaning, but saying, like, hey metrics have this, this, this, this, this is actually relatively
easy and convenient, and it to me
it felt better. But I also know I'm a super nerdy, functional programmer person, and my idea of what's easy is very different than the world. And so I want to run by. Everyone
of I arbitrarily made that decision. But how do we feel looking at this right.
Let me find a better test to show.
Liudmila Molkova 00:46:48 I. My opinion is skewed.
I.
If we think about semantic conventions, we would never define attributes inside the signal.
So for my use cases, it doesn't matter.
Josh Suereth 00:47:14 Yeah, it's this.
Laurent Quérel 00:47:15 Yeah.
Josh Suereth 00:47:15 Complicated use case. But this is a semantic convention. Use case, actually. So if you look at it where it's all split up.
You'll see like for Http, right? We reference service Server Port, and we override a few things. But Server Port is in the server file, and the server file is dead, simple.
Laurent Quérel 00:47:37 I think the most important part for custom registry, because it's a it's a question for custom registry, I think. To be honest, I think for custom registry.
The most important part is the ability to define everything in a single file.
And and then, having this constraint of defining your attributes
in a common registry, let's say at the beginning of the file, like you did here.
I think it's good enough.
Yeah, I agree. I think it's it's not a big deal even focused on registry context
not being able to define locally. An attribute is is probably fine. Now, with this new syntax.
Josh Suereth 00:48:24 Cool anyone. Anyone have concerns with that.
Okay, those were, I think, the hardest things. Now for a bit softer stuff.
Let's go through maybe metric first.st
Where's span?
Why did spam? Not show up.
Liudmila Molkova 00:48:52 It's on the bottom.
Josh Suereth 00:48:54 Oh, God, I had a pop up over that.
Let's do. Let's do metric first, st and then we'll do span, now that I can see it.
cool, so name has to remain, and it's called name. It is not called metric name.
Laurent Quérel 00:49:09 Perfect.
Josh Suereth 00:49:10 Instrument is the instrument. Spec that is unchanged
unit is is required. So you have to have unit, and then we have attribute refs again, right? So not defs refs.
And then entity association. This is another thing. We have this one we consistently have across signals. I wasn't sure if I should make a common signal field that includes this or not, but
we we just explicitly put it there as well, and then the common fields again.
Liudmila Molkova 00:49:40 That's see?
Good question. It's okay. If we don't do it right away. But we have attribute refs. Should we have entity refs.
Josh Suereth 00:49:52 Instead of a string.
Yeah.
Liudmila Molkova 00:49:54 Yeah, we would not modify the entity right? There is no refinement for entity when you have an association.
So maybe not. Yeah.
Josh Suereth 00:50:04 I'm fine calling it an entity ref and code, and making it be a string like that's that's fine, too. But yeah, it
it's a good question.
Yeah, we we aren't. We aren't allowing overrides and entity associations.
Liudmila Molkova 00:50:20 But we can allow something like requirement levels saying, Okay, this association is actually required.
Josh Suereth 00:50:27 Technically, they're all optional today.
Laurent Quérel 00:50:32 Or sorry.
Josh Suereth 00:50:33 How do I want to phrase it? There, there it's it's a 1 of association.
So one of them is required. Not all of them.
Liudmila Molkova 00:50:42 Yeah, I'm saying that there could be some additional metadata in the future that we might want to.
Josh Suereth 00:50:48 Yes.
Liudmila Molkova 00:50:49 Put into the association, which is not necessarily refining the entity, but saying how to I don't know
something else.
Josh Suereth 00:50:59 I I'm.
Laurent Quérel 00:51:00 Something that is contextual with the signal.
Liudmila Molkova 00:51:03 Yeah.
Josh Suereth 00:51:05 Yeah, I'm fine. If we want to preemptively make a ref where it's just for all Ids to start with, that seems reasonable to me.
Liudmila Molkova 00:51:11 If it does not change the schema
for the consumer, then it maybe it's not important at all at this stage.
Josh Suereth 00:51:21 It doesn't. But one thing I learned with shenanigans, with with Zurd is is.
you know, figure it out early.
I can show you. By the way, just in case you read through this, I ran into a ginormous problem with Cert.
Where is it? It's here, where not? Cert with the Json schema inference. The macro violates our lint rules, and so I had to actually manually run the macro and then Update the lint rules to add this particular, allow.
Laurent Quérel 00:51:57 Hmm.
Josh Suereth 00:51:57 Because the macro doesn't include it. I opened a bug on on schemers to fix this on their end.
But the the this, this whole thing was a pain in the butt to get working.
anyway, if you if you wonder why this is here, it's documented, it's what it is, but it it's.
Laurent Quérel 00:52:17 You can't use the unused blah at the file level. So you don't necessarily need to do this work for the for the macro.
Josh Suereth 00:52:25 It. I couldn't get that to work.
I tried
Laurent Quérel 00:52:31 Good! With a a sharp exclamation point a low
a news qualification at the top of this side.
Josh Suereth 00:52:42 I'll have to try it. I'll have to try it that way. Yeah, if if you, if you think that would work, we can do that is, I didn't want to get we.
I didn't want to bleed this through to the whole file, because there's so much in this file that we don't want unused qualifications. So.
Laurent Quérel 00:52:58 Yeah, I think that will work with the the drawback that you just mentioned.
Josh Suereth 00:53:03 Yeah.
okay. I'll take a look at that, anyway. If we keep going quickly, we have 8 min. There's there we go span again. Let's go through span quick.
So span has a type.
This is the new name of the span, if you will, or the shape that thing that I really like this, this cleaned up a lot. It has a kind, it has a name pattern.
and then it has attributes which are again, references. This would get updated to be span, attribute ref for sampling relevant. It has entity associations. We'll consider making these entity refs. And then events. I think I agree with the miller. It's nuke it.
It's a set of strings. It's like entity associations. But if if we're moving to raw, pure events now. And we're not using span events. I think we get. We get rid of that.
Laurent Quérel 00:54:01 A question regarding the name name pattern. Is there any specification describing how this pattern should be defined? And if yes, I think we should replace string by
something describing the pattern and validating it.
Liudmila Molkova 00:54:18 It's a good point. So like today, we don't have any. Well, we have something that's very human, oriented or AI oriented.
but not formal, we would probably evolve it eventually.
Laurent Quérel 00:54:32 Yeah, like we did for deprecating, like we did for many things, in fact. So maybe that could be a nice thing to to do it for fiscal, maybe 2 day, one.
Josh Suereth 00:54:42 Yep, yep, I, okay. So let's let's add, that is a to do.
Consider making this more robust explicit in how it works.
it. Would someone be willing to help me figure out? Name like Lyudmila? Is that something you might have time to do? Since this I'm working on your proposal. To begin with.
Liudmila Molkova 00:55:11 Yeah, okay.
Josh Suereth 00:55:13 Yeah, if you could go ahead.
Laurent Quérel 00:55:16 Type. Is there any so type? It's it's a free form text, or it's something with more constraints.
Josh Suereth 00:55:25 This is the same as the Id.
Laurent Quérel 00:55:28 Okay.
Josh Suereth 00:55:29 Before. And so it's basically free form text. But we expect it to have like a dot paradigm.
Laurent Quérel 00:55:35 So maybe we could introduce
again, like for the the name pattern, something that is not a string, but a name a dot
not. I'm not good for them, but something that will check the fact that we are in a dot representation.
Liudmila Molkova 00:55:54 Id identity.
Laurent Quérel 00:55:57 Yeah, a type. That's yeah.
Josh Suereth 00:56:01 Yeah. And I think identity would get used for like metric name, it would get used for type here. It get used.
Laurent Quérel 00:56:06 Yeah.
Josh Suereth 00:56:07 Or entity type. Yeah.
Laurent Quérel 00:56:08 Yeah.
Josh Suereth 00:56:09 Yeah, I'm that that makes a lot of sense. Let me do that. Consider creating a type to
a rust type cold identity which enforces restrictions on allowable strings. Okay.
Liudmila Molkova 00:56:35 Sorry the the SDK Api designer and me scream signal identity to be specific.
Josh Suereth 00:56:42 Oh, I I like, I like, signal identity. Yeah, okay.
make a comment feel free. Yeah, we're down to 4 min. So I'm going to keep going. I think common fields is common. So that's span. And let's look at event.
Event, we have a name, a body attributes
entity associations in common. I think that's that's like Crisp.
Were there any problems with any value? Spec. We need to evaluate Ludmilla.
Liudmila Molkova 00:57:18 Oh, it's it's unusable.
Josh Suereth 00:57:21 This is unusable.
Liudmila Molkova 00:57:22 Yeah, I mean.
it's it's better than nothing, but it's unusable. And we don't recommend using body. By the way.
Laurent Quérel 00:57:31 Yeah, I'm not surprised from the beginning. I never understood the.
Liudmila Molkova 00:57:36 It's no, it's worse now. We recommend to put it in the attributes. But I
it's still bloody. There is still body it's still of can be of type any but the way, like the type definition that we have today. It's it's unusable we use Json Schema now. Sorry.
Jason schema is better than this.
Josh Suereth 00:57:59 Okay to do. Remove or change this to be Json Schema, like an embedded one or something. Okay.
Liudmila Molkova 00:58:12 If.
Josh Suereth 00:58:12 I'll just make a note of that.
Liudmila Molkova 00:58:13 Body. Yeah, if we remove body, for now.
I don't think anybody would be would hurt.
Josh Suereth 00:58:21 Okay, that's
alright. That sounds that sounds like a plan like, honestly, if we just have embedded Json schema like, Hey, there's a body. Here's a schema definition for it. Go.
I'm fine with that, too. Okay, last thing is entity.
Since we have 1 min left, this one is also pretty close, crisp. The difference is, instead of having a role on attribute, I cut role from attribute, and we have an identity and a description as separate things. Identity is required as a vector description is optional.
So it makes the linting rules a lot easier and they're both attribute refs. So any attribute can be used as an identity or description. The fact of it being identity or description is a consequence of it being an entity.
Laurent Quérel 00:59:11 A question. Identity and description, especially description, is confusing for me, because we have, I mean.
maybe something like attribute identity or identity attributes, description, attributes, or something like that. But.
Josh Suereth 00:59:31 Purely description.
Laurent Quérel 00:59:33 Seems ambiguous for me.
Josh Suereth 00:59:36 Okay that. That's a that's a much bigger discussion than the last minute.
What I'll say is right. Now, if you read the entity spec. It calls things type, identity and description. And so I wanted to match those things. That's actually, I think, what shows up in otop. So.
Laurent Quérel 00:59:53 Okay.
Josh Suereth 00:59:54 I hear what you're saying. But when we had it any other name, it confused people working on entities. So it it's it's a matter of, I think, unfamiliarity with one or the other causes confusion.
Oh, it's under common hold on.
Laurent Quérel 01:00:09 Something like descriptive attributes will be easy to understand.
Josh Suereth 01:00:15 It's called id and description. Yeah.
Laurent Quérel 01:00:18 So description keys.
Maybe that is less ambiguous. If we want to to stick with the the photograph specification.
Josh Suereth 01:00:30 I'm I'm fine calling it description keys. I'm honestly just tired of that naming debacle and the arguments personally, so I don't care. Let's pick something that we find.
Laurent Quérel 01:00:39 Absolutely true, but right now.
Josh Suereth 01:00:41 Everyone finds every name confusing, and and we go in circles
honestly. Just kind of tired of that. I don't think there's a great name. I think there will be confusion, no matter what.
So let's just pick one and go. But if, like, you want to call it description keys, we can call it description keys. That's fine. Yeah, it's better now that we that this is now actually called type and not called name
in Semcov, because that confused the crap out of people and entities. So all right.
thanks, everybody. I think that was really helpful. I will update this Pr. And again, I want to kind of consider this an evolution. So the last thing I will do is I'll make it so that it's behind some kind of a warning. Where, when you use v. 2, you'll get a warning saying that this could change.
but I'd like to get it out in the next release, if possible, to let us start toying around with it and use it in anger before we commit.
I'm trying to.
You're trying it out nice, cool.
Liudmila Molkova 01:01:41 I'll thank you.
Thank you. Thanks a lot.
Josh Suereth 01:01:46 Thanks, everybody.
Liudmila Molkova 01:01:47 Bye.
Laurent Quérel 01:01:48 You, too. Yeah, very nice. Thank you. Bye.
