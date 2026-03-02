SIG: Configuration WG
Date: 2025-06-23
Duration: 56 minutes
Zoom Recording URL: https://zoom.us/rec/share/3fm_fE7-Hkn2IyKyLIHvREUlUYgpI-vOx8dgLyALIjmD4VKexFm8Ua8avY-zZRoj.Oh8oYxmvfM3Argvg
============================================================

## Zoom Recording Transcript

**Jack Berg** 00:38 Good morning, Jay.
**Jay DeLuca** 00:41 Hey, Jeff, how you doing.
**Jack Berg** 00:43 I'm good.
**Jay DeLuca** 00:47 This week.
**Jack Berg** 00:49 No! Who've gone?
**Jay DeLuca** 00:51 Is that what it is, or the community day, or something?
**Jack Berg** 00:56 No, no, I'm not so sure.
**Jay DeLuca** 00:59 Something in Denver. I think.
**Jack Berg** 01:03 I am not going. Are you.
**Jay DeLuca** 01:05 No, I'm not.
I wish.
**Jack Berg** 01:22 Hey, Tyler, Hi. Gregor.
**GZ Gregor Zeitlinger** 01:24 Hello!
**Tyler** 01:25 Hey? So.
**Jack Berg** 01:38 So we cut a release candidate.
**GZ Gregor Zeitlinger** 01:42 Yay!
**Jack Berg** 01:44 Yeah.
Now, we need to come up with an approach to figure out when we're comfortable with the release candidate and cutting a stable release.
Part of that is is, you know, I think a stable release of the configuration schema should coincide with a stable release of certain components of the specification.
And so I have an action item to draft up. A pr to the spec to propose
the different portions of the spec that I think we should stabilize. I've talked about that in an issue previously.
but I'm gonna bring that up at the spec meeting this week.
And
you know, just for other folks on this call there's some Java folks, Gregor and Jay. Welcome. Gregor's been here a few times. I think this is the 1st time we've seen Jay here. So my my plan with this Sig is after we
have a stable release. I'd actually like to wind this down and merge this back in with the specification, say.
and if I know there's more configuration work to do. But this group and the charter of this group kind of got together. With a goal of, you know, coming up with the data model. And the the spec capabilities that we've we've gotten that. We've landed over the last couple of years. And so
I think you know, in the effort of in in the interest of finishing things and and having, you know, more limited concrete scope. If we want to do additional configuration work after the stable release, I think we should sort of go through the project proposal process again, and sort of
reinitialize with a new charter of whatever scope
we want. I know some people have talked about dynamic config and remote config and things like that. Those are great. Next steps.
Yeah. Any comments or or questions about the the release candidate or you know
a future stable release.
**Tyler** 04:08 As well, so that all sounds good.
**Jack Berg** 04:19 Cool your your microphone was a little hard for me to hear. I'm not sure if it was just me or for everybody, but I think I got the gist of what you were saying.
**Tyler** 04:28 Oh, sorry!
Oh, it's all hard for me.
**GZ Gregor Zeitlinger** 04:39 Is that any better, Jack? Yep.
**Jack Berg** 04:41 Oh, yeah, oh, night and day. Better?
**Tyler** 04:43 Yeah, zoom upgraded over the night. And so yeah, settings are all jacked up. But no, I'm sorry. I was just saying that. Yeah, I I agree. I think, that that all sounds good excited to get the release out. I think.
popularizing at the specification meeting makes sense. And then I think once we get it merged. Yeah, winding this down makes a lot of sense as well kind of like other working groups. In that sense.
**Jack Berg** 05:07 Yeah, great?
Well, so I see, Gregor, you've added a bunch of topics to the agenda. I saw you opened a flurry of issues. And and you know the Java instrumentation repo, and and some in the the core repo as well.
Just before we get into those Tyler, Alex and others. What do you do? You have any other topics? Because this seems like it's going to be sort of a Java heavy conversation hereafter.
**GZ Gregor Zeitlinger** 05:39 Nope, it probably is. Yeah.
**Tyler** 05:43 No, I I didn't. The only thing I wanted to talk about was just communicating this at the specification meeting tomorrow. So we already have a plan on that. So that was kind of it. So yeah, no, I don't. I'll probably jump off, though, if this is going to be just a Java heavy thing.
But yeah, good for me.
**Jack Berg** 06:02 Makes sense.
**GZ Gregor Zeitlinger** 06:02 Well, it might also be interesting for other languages like, How do you do vendor specific configuration handling?
This is not just for Java.
**Jack Berg** 06:15 It's yeah, it. Yeah, it's
I think, with the Java agent there's in in all the vendor specific distributions of that. There's some sort of unique Java challenges in there.
I don't, I mean may correct me if I'm wrong. I don't see. You know, vendor distributions of of a succinct kind of product in other languages as often.
maybe at all.
Maybe maybe Python has something like an auto instrumentation thing. Do vendors have a distribution of that that they commonly publish.
**GZ Gregor Zeitlinger** 06:51 We have one for.net as well.
**Jack Berg** 06:52 Oh, dot, yeah.
But yeah. So anytime you want to have a vendor distribution of of what's otherwise like, you know, sort of. There's a vanilla open telemetry offering, like, you know, the collector or the the Java agent. I think you'll sort of run into these options with with like, how does the how does the user's desired configuration intersect with the vendors desire to customize that configuration, to have good out of the box defaults and other behaviors.
So yeah, I guess. Like,
I, obviously Tyler and Alex, you guys can can feel free to do what you want. But,
Gregor, let's get into it.
**GZ Gregor Zeitlinger** 07:39 Right. Should I? Just no, actually, I don't need to share my screen.
the the board is actually there to have a project. When that is done, then we consider
declarative configuration to be usable in Java, meaning
that we then would put it prominently in the documentation. Right now, you can actually use it, but it's it's not as easy to discover.
I I think you haven't been at the Java meeting last time, Jack. That's
that's why I'm making this quick summary. And most importantly, Trask was saying that he wants to have enough confidence that everything is actually working, and therefore we should have an end-to-end test.
And this is kind of the story, and
I intend to spend some time in the next months getting this to closure. But
maybe I won't be able to finish everything, so any help is welcome. And Jay already
agreed to help on it.
and a few things are in discussion. And this is particularly what I want to unblock so that we can then ask more people, to help with the effort.
Yeah, the 1st one is a schema for instrumentation section. So this one is either in the board or in the meeting notes
right?
So this came up when I wrote the 1st line of code
for a module in Java, which is for methods. So you can describe method. A should have spend kind
client. And while I was writing this. This sounded
a little bit under tooled. So this information is in the in the Java
code, but you cannot do anything with it. And compared to the other sections where we have nice generation of schema, it feels like we should have
good approach for getting that to work, at least in Java. I don't know if the same idea can be translated to other languages.
**Jack Berg** 10:15 Yeah.
Yeah. So I don't. That
I I like the idea of you know better schemas for the instrumentation modules. I anticipated us running into something like this, the you know, right now.
you sort of have to enforce the schema on the fly, as you're doing this manual parsing task of translating from, you know, the declarative config properties to whatever the schema is of your instrumentation module. And you know that's not a great experience to do dozens of times over and over again.
**GZ Gregor Zeitlinger** 10:54 Alright!
**Jack Berg** 10:55 So
yeah, I don't. I? The one? The one thing I I don't think we should do is treat the open telemetry, configuration, repository as sort of like a centralized mono repo of all the schemas, of all the instrumentation, repository, instrumentations across all the languages. I think we need to find a way to make this like a distributed problem, where you know each
instrumentation library somehow expresses its own schema. And when it's, you know, receives a declarative config properties. You know the equivalent of a yaml node. It has, we provide tooling to translate between like that generic yaml node and its actual data model for that instrumentation library.
**GZ Gregor Zeitlinger** 11:45 An instrumentation library would be like Java agent, because that is effectively
what we have, or more, we compile all the instrumentations in the Java agent to a complete
model. Because this is what you.
what you code against what you write.
your editor assists, should work against.
**Jack Berg** 12:08 Yeah, yeah, I think so. You know. But
it should also work for sort of even smaller scales than the Java agent, you know if you imagine a Native Instrumentation library ultimately that should be able to have its own schema. And maybe it's not this big, complicated thing like the the Java agent, but we it should have the equivalent ability to express the schema for for it, you know it's sort of narrow scope, and then, you know, provide good tooling to to parse to that.
So in my head there's a couple of there's a couple of things in that are
on the path to solving this problem. So
we need some way to express the schema of, you know, one, or maybe more instrumentation libraries.
**GZ Gregor Zeitlinger** 13:19 Still there.
**Jack Berg** 13:20 Yeah, I'm here.
**GZ Gregor Zeitlinger** 13:22 Okay.
**Jack Berg** 13:23 And I'm just taking some notes along the way on your issue. And so
I can see this taking a couple of different forms like so ultimately, what makes let me see if I can pull up some code.
What makes the the code generation bit of
of the declarative config implementation and the core repository work is
So you know, we have all these model classes and these these are all generated classes over here that correspond to each of the types from the schema. And you know, so there's some tooling that we have in Gradle that
parses the Json schema and spits out all of these models, and these are just sort of pojos, and they're annotated with the Jackson annotations that allow the Jackson object mapper to properly map each field to the corresponding property in the class. And so you know.
a naive version of this type of task that we're talking about over here would just be to hand code Pojo classes that represent the schema of a particular instrumentation library and then provide a really simple translation layer that
translates a declarative config properties to whatever that Pojo is
for that library. So you know, it would look something like this. So
you know. Let's say you have. So let's say you have
some class called Foo instrumentation schema.
And this is the this is, you know, a class that's annotated with you know all of your
all the properties, and it they all have Json properties, annotation. So maybe there's like a
a property called Foo in here, and it has, you know, Json property.
**GZ Gregor Zeitlinger** 15:41 Okay.
**Jack Berg** 15:44 And there's a bunch of other ones like this. This is like the expression of the schema of a particular instrumentation library.
What we could do. If once we have something like this is we could have we have this, you know, declarative configuration sort of it's a utility class. This has all the key methods of declarative configuration. It has, like the Parse operation and create operation. And you know, all the logic is essentially bootstrapped by this. But we could have, you know, a utility function that would translate a particular
declarative config properties. Node.
2, you know, you know, in in in Jackson world. This would be like a type reference.
If you're familiar with that.
So you could say, like, Hey, translate from this declarative config properties node to you know our.
our, our schema here.
and you know, out, come out. The other end would come. You know the the translated schema.
Yeah, it's basically.
**GZ Gregor Zeitlinger** 16:54 Unmarshalling, and and Jackson.
**Jack Berg** 16:57 Right. And so behind the scenes. This would take this node, which is, like, you know, an inner memory representation of a yaml node. And, you know, do whatever it needed to do in order to do this translation. And that might a really naive way to do that would be to like. Write this node back out to Json and then have Jackson do like, you know, reparse it into this like Foo instrumentation schema.
So but you know that that's just like an implementation detail, like, you know, the the key thing would be that
we provide sort of central and common tooling to do this translation process so that you know any instrumentation library can express their schema and translate. You know our representation of a yaml node to an instance of that schema.
And then, you know, from there it's much easier to initialize.
**GZ Gregor Zeitlinger** 17:49 Yeah, that solves the the runtime part.
I'm wondering how we do the build time part. I think that's the harder problem.
**Jack Berg** 17:59 Yeah, yeah, so this is so this is, you're right. So this is the runtime part of it. And you know that naive thing would be that, you know you handwrite out these schemas. But I think what Jay has, and you have been experimenting with is like, Hey, how can we write tooling to go and detect and spit out some representation
of the configuration schema of all these different instrumentation libraries, so that, like you know, users, can understand them at a glance. And so we can generate documentation, and so that we can understand them. All the good things that come out of having like sort of a structured representation of the configuration schema.
And you know this, this is what you're getting at. So whatever the output is of that tooling, you could have another step that goes and generates these
these pojos from that configuration schema. And I don't know what representation you want to have like in declarative configuration we've been, we've been. We represent our schema using Json Schema right? And so we parse Json schema, and output classes that look like this. But you don't have to use Json Schema. That's not a hard requirement, right? So it might be easier to come up with your own.
you know. Structured representation of what the config schema is for each instrumentation library, and just like, you know.
have your own little code generation tooling that interprets that structured representation and spits out pojos.
**GZ Gregor Zeitlinger** 19:33 Well, can we maybe work backwards? What is the desired output format so that we have something that can be validated by editors?
I don't know if you have thought about this story so far.
**Jack Berg** 19:50 I haven't like validated by. So like, you know, the idea would be that, you know, a user
typing in an editor could be, you know, writing their their declarative configuration scheme. So
you know, they're they're writing out this. And they say, Oh, okay, I have this Java config, and I have my this schema called Foo
or this instrumentation library called Foo, and I want to have the editor be smart enough to have auto completion options.
**GZ Gregor Zeitlinger** 20:20 Yep, yeah, I think that would be a huge improvement. I know how spring does it, and I know that you have some weird Json file that you want to have as a result, and then
it's working for spring files.
**Jack Berg** 20:36 Right. I think I saw you link to that
in in one of your issues. There was, you know, a big sort of configuration schema file that had, you know, a Json object for each property, and you know, some tooling in the editor would presumably
read in that file, and and then, you know, make auto completion better.
**GZ Gregor Zeitlinger** 21:01 Right.
**Jack Berg** 21:05 so I I don't know that that seems like a question about like the editors like, what type of
representation they expect.
I don't. I don't have any experience with that. So.
**GZ Gregor Zeitlinger** 21:17 Huh!
Jay, do you have an idea what we should do? Is it like good if we write of the
Jackson annotated classes and take that as a source of truth or something else.
**Jay DeLuca** 21:35 Yeah. A while back, I think in one of the Java Sigs. Jack had talked about this this code Gen. Idea. And and that's kind of what I was thinking we'd eventually get to is right. Now I'm going through the discovery of trying to figure out all the different configurations I I would assume that the next step would be
figuring out a way to then
work backwards and generate the code, using those definitions. So, for example, may. Maybe it's the new metadata metadata Yaml file that we're putting into each instrumentation. And maybe we then
build tooling that interprets the configuration properties and then converts them into the the pojo, or something.
**GZ Gregor Zeitlinger** 22:15 Oh, yeah, I like that. That seems like it would align with the long term vision.
Yeah, let's put that on. I like that.
**Jay DeLuca** 22:24 Yeah. And I can. I can experiment with that and try and at least come up with a an initial implementation for like a single module or something. I I know what you're talking about in terms of the autocomplete, because I I was playing around with it for for something I was looking into a while back. But I I also don't have great intuition around
how that works under the hood, but I can certainly help.
you know, dig in and try and understand that, but I would imagine that it should. Once we have the definitions. It should be pretty trivial for us to to generate some kind of file that we can then book into that I would think
But, like I, I already have, I think, like 15% of the modules mapped out in terms of the the configuration options that are available. We might have to think about it a little bit differently, for some of the global ones. But
but yeah, we we can at least start experimenting and see if we can come up with the implementation that we think might work.
**GZ Gregor Zeitlinger** 23:19 Yeah, the the 1st module is already there. This is the one with methods. The Pr is not merged, but the functionality is there. And it's a really simple one. So it's
probably a good candidate for us for trying this out.
**Jay DeLuca** 23:58 yeah, in terms of so as I've been working through this project and going module to module and trying to
work backwards and identify this configs. It's it's made me really want kind of a more centralized, consistent approach. So
yeah, may. Maybe this is a good opportunity for us to standardize the way that configurations are handled, and
improve that a little bit too.
**GZ Gregor Zeitlinger** 24:26 And from what Jack was saying we could also tap into the Json configuration
to to find out what what SDK properties are available. But that's probably a different question.
**Jay DeLuca** 24:46 But like thinking about this in in general, like, if someone were to try and
configure instrumentations with declarative config in the current state, like. I don't even know how someone would
like it. It's it takes. It's tricky to understand what configuration options are available for each module in the current state. So.
**Jack Berg** 25:05 Yeah, you have to reverse engineer it. You have to like, understand this like, trend this bridge that I wrote, and like how it translates from, you know, flat properties to structured properties, and, like, you know, do the mental math to reverse it? It's.
**Jay DeLuca** 25:21 Even before that, just to say, like this, module has these options available before you even try and map them to the declarative model. It's it's it's not intuitive like. You'd be lucky if there's a readme.
**Jack Berg** 25:32 Yeah, that's that's the problem. I think, with instrumentation config in general, is that, like the documentation for all the instrumentation config properties, even in the flat. Schema, like setting aside declarative config, is like inconsistent and weak and full of holes. It's like switch.
**Jay DeLuca** 25:48 Yeah.
**GZ Gregor Zeitlinger** 25:51 Could we create a follow-up task for documentation like how to figure out
how to maybe also generate documentation.
**Jay DeLuca** 26:03 Yeah, I have. I have another project Java project that I created over the weekend. And I that is part of the goals for that.
**GZ Gregor Zeitlinger** 26:10 Okay, of course.
**Jay DeLuca** 26:13 Yeah, at the very least. But the other project will provide the documentation. But this is the next step, I think, in terms of
making it accessible, accessible to users with declarative config. Like
I. I could foresee us being able to generate, like the the kitchen, sink
equivalent of the instrumentation stuff as like a starting point for people with all the defaults
which I think would be super useful as like an end goal.
**Jack Berg** 27:05 Alright. I'm just trying to take notes, and I'm not very good at this, at least, compared to
Trask. He's pretty amazing at talking and taking notes, at the same time.
**GZ Gregor Zeitlinger** 27:17 There can be only one task.
**Jack Berg** 27:19 Exactly.
**GZ Gregor Zeitlinger** 27:21 But I think this is really helpful.
**Jack Berg** 27:34 Yeah, okay. So we got some work to do. But
I think I think all the the pieces.
I it just seems like it's a you know. It's not a matter of like. Can we do this? It's a matter of like, you know.
Are we going to do this? And if we can just put the effort behind it, we can. We can figure all this stuff out. None of this seems particularly controversial. Or, or you know, too technically challenging or anything like that.
So.
**Jay DeLuca** 28:05 And I think a really high return on that investment from a user standpoint.
**Jack Berg** 28:10 Oh, yeah, like, if we can. I mean, even even setting aside declarative config for a second, like, if if we could have a you know, a structured representation of all the configuration options, of all the instrumentation modules and the Java agent, and then could generate documentation based on those that would be that would be huge in and of itself. And then, you know, extending it to declarative config is just like the icing on the cake.
**Jay DeLuca** 28:36 Yeah. And I and I plan to take it one step further, too, with the documentation should
provide what telemetry is emitted by each configuration variation as well.
**Jack Berg** 28:50 Right? Right?
That's a very cool idea.
okay, that's that's a good discussion on that issue.
Where do you want to go next? Gregor.
**GZ Gregor Zeitlinger** 29:09 Top to bottom in the agenda. Good thing is, we already covered the second part because it's so similar, and we already sketched how to generate the same information for the starter that we don't need to discuss it again. Actually, I put the spring ticket into blocked, because I think it's easier to do once we worked on the ticket just discussed.
and I think we can put the ticket we just discussed into.
Reggie stayed at least ready for Jay, from what I'm hearing.
**Jack Berg** 29:51 So that's this one right here, the schema for instrumentation section, and
I guess I'll move that for you.
**GZ Gregor Zeitlinger** 29:57 Yep, thanks.
**Jack Berg** 30:04 The next one that you had then was on resource. Detectors.
**GZ Gregor Zeitlinger** 30:08 Right? Yeah, this is more a Java specific question.
but maybe not. So. I was comparing the old and the new resource detectors, and I saw some gaps, and I didn't understand. If this is something, if there's a reason for something missing
are we just need to add more stuff.
**Jack Berg** 30:38 I don't think there is a reason for these to be missing. I think it's just a matter of of doing the the work. So
in the let's call it the flat configuration model
resource detectors are, you know, you implement an spi, and you know, unless you do, unless by default. You know they're all participating. They're all automatically detected in providing attributes to the resource and in declarative config. It's it's different. A declarative config has this philosophy about
What you see is what you get. And so if you want to.
**GZ Gregor Zeitlinger** 31:22 Yeah, I remember that part.
**Jack Berg** 31:26 Right. So all this is to say that detectors and declarative config, you know the detectors that you want to enable are explicitly enumerated, and they each have a sort of short name.
container, host, process and service are the ones that are explicitly enumerated in the specification, because these are the ones that we want to be consistent across all the languages, and, you know, open over in open telemetry, Java. We have a lot more detectors as you've listed out here. And so it's just a matter of implementing the right spi interface. And you know, coming up with a name for how you refer to these things.
**GZ Gregor Zeitlinger** 32:11 And I guess a special one is the one that's called environment resource detector, because it's in a different section.
So we don't need to have an equivalent for that.
**Jack Berg** 32:23 Yeah, I would say, there is no equivalent for that. That's sort of a bit of a
you know, a special case.
**GZ Gregor Zeitlinger** 32:32 Right. And I'm wondering about a service instance. It's also it was the only detector that was in the SDK before. So I'm wondering if that one should always be added, or if it should also be in the list
that you can operate.
**Jack Berg** 32:51 The the specification. And, Brandon, I wrote this specification, and it's still in development. So it's it's very, you know, plastic and and subject to change. You know, if we can go over to it for a second
on resource. I'll show you what we it has to say about
the service detector. So you know, there's a detector which is called service. It populates the service name attribute based on the value of the hotel service name environment variable, and it populates service. Instance id you know, as defined in the semantic conventions. And this basically just says, use a a uuid assign a uuid. And so,
yeah. So you
this, you have to just like other resource detectors, you have to explicitly include this service detector in your in your list of detectors that you want to enable
**GZ Gregor Zeitlinger** 33:47 Oh, so without you would not get the hotel service name, environment variable. Okay? Got it.
**Jack Berg** 33:53 So basically everyone should have that
right. And so you know, it would be one of these things that we'd want to include in our. You know, our template, that you know our getting started template.
**GZ Gregor Zeitlinger** 34:04 Okay.
**Jack Berg** 34:06 And I have a so this this is new as of you know, the release candidate version of
declarative configuration. And so I have a Pr
over in opentelemetry, Java, which implements this.
And it's you know, it's really simple. But
over in this Pr here, where I'm updating to the release candidate.
Let's see, there's a there's a service resource detector, you know. It's called service
and you know, it looks for the value of the hotel service, name, environment, variable or system property and set service name based on it. If it's if it's set, and then, you know, includes the service instance, id resource attribute just set to the value of the uuid. So you know, as a user, you can
choose to opt out of this completely by not, you know, including service in your list of detectors or you know there's because the detectors are ordered. You know they're an array of resource detectors. You can have a later one overwrite the service. Instance. Id. If you have a better service instance Id or a better service name. If you want to use some sort of detection mechanism based on the jar, name or application name, or something like that.
**GZ Gregor Zeitlinger** 35:26 Oh, I think there's a difference to the old
detector, and that you don't have a global for
the service instance. Id. I added that, so that if you instantiate
the class twice, it would not use a different uuid.
**Jack Berg** 35:44 Oh, yeah, I noticed that when I was writing this and I was wondering. That's this is a good opportunity. I have. No, I'm not opposed at all to having a global like a a static instance for the uuid so I was. I was curious. If you could recall the reasoning behind that, and I'm happy to change this implementation.
**GZ Gregor Zeitlinger** 36:03 Yeah. I think there are some
configurations where users create 2 instances of an SDK, for
whatever reason, maybe not even good reasons, and
they only differ in the service instance Id, because there's a random part.
But I don't recall exactly a concrete setup where this happened that that triggered this.
I should have added that.
**Jack Berg** 36:49 Either way, I don't see any reason why this is a bad thing, so I'm happy to do that.
**GZ Gregor Zeitlinger** 36:59 All right. Yeah, I think then that's it. So the idea is, you always name your detectors after the
entity, which is the new way, how we think about polls.
**Jack Berg** 37:12 Let's see what I wrote in the spec. So the naming is
you know it's it's loose right now, because entities aren't a thing yet, and you know resource detectors
are a thing, and you know, have some historic precedence there, and so I try to be sort of vague with the guidance to like, you know, allow some wiggle room. And so what do I say? I say? Resource, detector, name should reflect the root namespace of attributes they populate. For example, a resource detector named OS populates OS attributes.
And then, you know, if you have a resource detector which populates attributes from multiple root namespaces, they should choose a name which appropriately conveys their purpose. So you know, that's basically, you know.
choose wisely, is the advice there.
**GZ Gregor Zeitlinger** 38:05 Mean that once we support entities they will have a different configuration, a node.
**Jack Berg** 38:14 So I think, yeah. So I think the way I don't know this. But I think the way that entities are going to shake out is, you know, in declarative configuration. Today you can configure a resource block. It's like a top level block, and I think with entities they'll
I anticipate it being like, Hey, there's a separate entity block
that is mutually exclusive with resource.
You cannot contribute to both, like you say. Either I want to specify my entities, or I want to specify my resources, but not both.
So then, you know, everything in resource would essentially eventually become the sort of legacy configuration
once entities mature.
**GZ Gregor Zeitlinger** 38:59 Yeah, okay, cool. I think that that
resolves the questions I had. Can you also link the Pr for service? So that it's clear that this part
is already taken care of.
**Jack Berg** 39:12 Yeah, and issue that we were oops.
I can type.
So environment resource provider is a special case that doesn't need to be duplicated, and then the other one was the
What were you calling it?
**GZ Gregor Zeitlinger** 40:05 Service instance. Id was the old one.
**Jack Berg** 40:09 Is this? Is it not in your list here.
**GZ Gregor Zeitlinger** 40:11 It should be because I was looking at the hierarchy, but it can be hard to spot
**Jack Berg** 40:21 Process.
**Jay DeLuca** 40:22 The service instance id.
**Jack Berg** 40:24 Do you see that in this list? Am I missing.
**Jay DeLuca** 40:26 Yeah, it's it's under, up, up a little bit of order.
**Jack Berg** 40:33 Oh, okay. Yeah. Could find service. Instance id.
**GZ Gregor Zeitlinger** 40:37 Oh, yeah, now I have more questions now that I'm looking at the list. But I'll let you finish typing first.st
**Jack Berg** 40:58 Alright!
Let's go on.
**GZ Gregor Zeitlinger** 41:01 Distribution. This is a resource provider, and I don't know how this fits into it.
It's more like a Meta information that you're using the Java agent or the spring starter than anything else.
**Jack Berg** 41:18 Yeah, yeah, it's like, you know, the
the SDK has these default resource attributes that are always included like the language and the version. And these are sort sort of extensions of that something that the user should not have to opt into, that are always present.
**GZ Gregor Zeitlinger** 41:41 Right because it's for troubleshooting. Basically.
**Jack Berg** 41:45 Yeah. So
how could we accomplish that? So one way to accomplish that would be to for the agent to implement the
declarative config customizer. Spi, and you know, read the data model, and.
you know, spit out a data model where the the resource has been enriched with these additional, you know, attributes the distribution, attributes.
What's it called? What do we call this? The distro version resource provider.
**GZ Gregor Zeitlinger** 42:59 I'm actually wondering what the difference is to service. Instance Id, since
the spec also says that it should always be set.
**Jack Berg** 43:16 Let me let me finish typing this, and then we can go revisit that
right?
Alright. That's good enough.
And yeah. So what? Why isn't
this service instance Id. In the same category.
**GZ Gregor Zeitlinger** 44:10 Yeah, like.
**Jack Berg** 44:14 So what do we have to say about service? Instance? Id. So
is this in a stable part.
**GZ Gregor Zeitlinger** 44:21 I was just looking that it is recommended. But it says, Development, I actually don't know why it's development, but
probably not implemented in enough places.
**Jack Berg** 44:33 I think I remember this. So there was a Josh was making this big push to stabilize the Service resource attributes because they've been around for so long, and everybody's dependent on them. And you know, service instance, Id didn't have good semantics at that time. And Urasi actually made a push to, you know.
Define this this portion of the spec that says like, Hey, it should be automatically generated, and you should just use a uuid for it? And so that gives the user the ability to override it with a more useful you know
value, which is which you know is persistent across restarts of an application if they have such an id, but you know they make sure that service instance Id is always present, but that that was like just being proposed when the you know service, name and service name in service version were were marked stable. And so I bet if somebody made a push right now to stabilize service instance Id that people would be open
to it. And it's just like it's waiting for somebody to ask the question of like, is it time to stabilize this.
**GZ Gregor Zeitlinger** 45:49 Okay, I'll make a note of that, but we'll keep it
out of here for now, I guess.
**Jack Berg** 45:58 Right. And so, I guess, is this service instance. Id. One of these things
is that part of this special case which is always provided.
or should a user have to explicitly opt into it?
one advantage of keeping it in this sort of way where it's it's part of this name detector called service is.
it's easier to, you know, muck around with the ordering in priority of it. You know, you could have other resource detectors that also provide service. Instance Id. And you could either say that the uuid has higher priority or lower priority of those by, you know, changing the order in the list.
**GZ Gregor Zeitlinger** 46:45 That's a good argument. Yeah, right?
**Jack Berg** 46:48 And it's really easy it it might almost be too easy, though, to omit it altogether. And to lose service. Instance Id. And that's like an argument for having it be, you know, something more, more core rather than something a user has to opt into.
It's like, how easy is it to do the wrong thing.
**GZ Gregor Zeitlinger** 47:11 You could have a customizer like the one you suggested for
distribution, and that runs last, and that would just add it. If you have not added before. This is, I think.
similar to what we had before.
**Jack Berg** 47:32 Yeah, I think it is at least with the Java agent, right?
Because the Java agent automatically bundles in the service instance. Id resource detector. So it was automatically providing service instance. Id.
**GZ Gregor Zeitlinger** 47:47 No, the this was actually part of the SDK, or is still part of the SDK, that's the only resource detector apart from environment.
**Jack Berg** 47:57 But it's in the incubator. So you have to explicitly opt into the incubator to get that.
**GZ Gregor Zeitlinger** 48:02 Oh, okay.
**Jack Berg** 48:04 And the the Java agent bundles that.
So I I'm I'm open to actually like, I don't know about this. I'm not. I'm not. Gonna go and argue that this is the right way to model this service instance Id, and like, you know, a name detector that the user has to enumerate. It could be that it should be more fundamental.
**GZ Gregor Zeitlinger** 48:26 We could just say, that's an implementation.
**Jack Berg** 48:28 Some point.
**GZ Gregor Zeitlinger** 48:28 For the agent.
**Jack Berg** 48:31 Yeah. Why don't? Why don't we say that?
Why don't we make a note here?
**GZ Gregor Zeitlinger** 50:04 Yeah, I really like that. The Api offers this flexibility.
**Jack Berg** 50:12 The customizer.
**GZ Gregor Zeitlinger** 50:14 Yep.
**Jack Berg** 50:15 It's a nice escape hatch.
all right.
that's all of the topics for this.
**GZ Gregor Zeitlinger** 50:42 Final question. It's not as difficult as the other ones. Jar service name, which is, it's not
a thing. It's more like. You can also get the service name out of the jar file.
From what you said, it's probably jar service name, because this is the category when it does not have.
And an entity then just call it what it is basically.
**Jack Berg** 51:17 Oh, well, you're talking about what? To name this thing the driver service name detector.
**GZ Gregor Zeitlinger** 51:22 Part of something else, or if it, if it should really just be that as as the thing that you list.
**Jack Berg** 51:30 Yeah, that's that's the the scope of these detectors is always a question right? You know.
how many should they? Should they be very narrow in scope, and do one very specific thing, or should they be bundled with other things? And you know, if they have narrow scopes, then it's very easy to, you know. Add or remove them, and you know, add or remove that narrow scope as like a as a small unit of work. But you know, the inconvenient part about narrow scopes is that the user has to list lots of things. And it, you know, it's a bit overwhelming to see lots of resource detectors on there.
So I'm not sure what the right thing is for this. I don't think that there's an obvious thing to bundle this, you know, jar Service name detector with right now, at least, I'm not familiar enough to know what it should be bundled with.
**GZ Gregor Zeitlinger** 52:20 Okay.
**Jack Berg** 52:28 Yeah, I don't really see any obvious candidates.
**GZ Gregor Zeitlinger** 52:36 Okay, yeah. I think that's
that's very good for this issue. Maybe you have, like, 2 min for the last.
**Jack Berg** 52:46 Okay.
**GZ Gregor Zeitlinger** 52:47 Ticket, which is also an extension for what we talked in the beginning about
**Jack Berg** 52:57 Yeah, this.
**GZ Gregor Zeitlinger** 52:57 For Java distros. Is it? Was this more about schema?
No, this is not about the schema part. This is more about the
double work part that distributions have to do if they want to support old and new style.
Yeah, this is specifically feedback from the Javasig that we should try to make it as easy as possible for distros to adapt that without having to copy
everything and all the the
what are the providers that they already have.
**Jack Berg** 53:37 Yeah.
So I mean, I'm supportive of this Pr, which basically extends the declarative config bridge
so that you can use the existing config properties interface. And, you know, read data out of declarative config, you know, using, you know, the flat syntax that's dot delimited
and but you know, it's it's it's limited, right? So like, if if
if a distribution or an instrumentation library wants to represent an array of objects, there's no way to, you know in to to access that data. Config properties. Just doesn't, you know, support that type of thing.
**GZ Gregor Zeitlinger** 54:23 I think I have. I have an idea how to solve that part. In the Java agent there is an object called instrumentation config, which allows access to both the property style and also the structured
part. But I don't have an idea on the other side, which is that currently, you have an auto configure, configuration, customizer, provider, which is the old one, and there's a new one which has a different name.
do you have to implement both? Or is there potential for making this easier.
**Jack Berg** 55:05 Wow.
yeah, I mean the argument that I made previously, and why I thought that we should introduce a separate config properties. So you know config properties and declarative config properties is because I thought there was too much of a data model mismatch between.
**GZ Gregor Zeitlinger** 55:26 Yeah, I'm not arguing that I think that's a good start. What I'm
wondering is, can we build something on top to make it easier.
**Jack Berg** 55:34 What are you thinking.
**GZ Gregor Zeitlinger** 55:37 I don't have an idea.
**Jack Berg** 55:40 Hello!
I'm I would love to make it easier. If there's a way to do that.
I'm I'm I'm I'm open to proposals.
**GZ Gregor Zeitlinger** 55:51 Okay, let's just leave that in discussion. If I play around with our distribution, maybe I'll come up with something.
**Jack Berg** 56:00 Yeah. So it's it's hard for me to put myself in the shoes of distributions, because my company doesn't have a distribution. But yeah, I'm sure if we did, I would be, you know, in the same camp as you, trying to make it as easy as possible.
**GZ Gregor Zeitlinger** 56:14 Actually, our distribution is quite simple. But
Jean told me from Microsoft that they have more things, and that I think that's why Trask was asking
if I don't have an idea, then we'll just ask for more help in the Java Sig.
**Jack Berg** 56:33 Okay.
**GZ Gregor Zeitlinger** 56:34 All right. Thanks a lot.
**Jack Berg** 56:37 Yeah. Great discussion.
I'll see you all at the Java State on Thursday.
**GZ Gregor Zeitlinger** 56:43 Yep. See you.
**Jay DeLuca** 56:44 See you, then.
**Jack Berg** 56:44 See you.
**Jay DeLuca** 56:45 I guess.
