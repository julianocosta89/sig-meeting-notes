SIG: Configuration WG
Date: 2025-11-24
Duration: 60 minutes
Zoom Recording URL: https://zoom.us/rec/share/pTKIRGrV3BCYXZPdv3dqrp8w2PwwyyE-BSLbIQ4kMpi8FYcNpA9PyLuV19XQc-Ow.Rqg66CiSwzOykf7q
============================================================

## Zoom Recording Transcript

Jack Berg 00:01:04 Hello.
Marylia Gutierrez 00:01:05 Hello.
Jack Berg 00:01:50 Alright, let's get started in just a minute or two.
I didn't expect to have this many people on a holiday week, but this is great.
Marylia Gutierrez 00:02:00 Well, not EOS.
Jack Berg 00:02:02 Yeah, exactly.
Marylia Gutierrez 00:02:05 Go, Canada!
Jack Berg 00:02:08 We got a global project.
GZ Gregor Zeitlinger 00:02:11 Hello!
Jack Berg 00:02:15 Hi, add your agenda items if you have any, Add your name to the attendees, and we'll get started in just a minute.
Yeah, Penny? Am I saying that right?
Yevhenii Solomchenko 00:03:16 Yeah, that's right.
Jack Berg 00:03:18 Great.
Nice to… nice to meet you. I think this is the first time I've seen you at this meeting.
Yevhenii Solomchenko 00:03:23 Yeah, that's the first metam.
Jack Berg 00:03:26 But I think I might have seen you in some of the issues. So, yeah, good to put a face to the name.
Alright, Jamie, you have the first agenda item. Do you want to take us away?
Jamie Danielson 00:03:38 Sure. So, when we were starting to… we're starting to implement this in JavaScript, and we're trying to figure out what the… What the precedence should be if we have… We have something in the config file that… conflicts with something someone set up programmatically. Like, so if they're setting up the Node SDK, for example, and they set, like, a span processor for traces, and then they have something different in the declarative config file, I don't know if that's specified.
What should win there?
Jack Berg 00:04:23 Yeah, so I think, Marilla, you and I were talking about this in a separate conversation outside of the SIG, but, Yeah, so I think… I want to say that this challenge… well, so, first of all, I can't really relate to this challenge, because in Java, there's no opportunity to have a conflict, because, declarative config is built on top of the programmatic interface.
And, when you configure an SDK with declarative config.
there's no opportunity to layer on your own programmatic configuration. You're instructing… there's, like, an abstraction built on top of the, you know, the SDK programmatic APIs that says, like, hey, you know, it's the create and parse methods, right? So, like, create an SDK, from this declarative config file, and then, you know, it handles all that magic internally. And there's no hook in there to say, like, hey.
somewhere in the middle, I want to take some of these components, modify, or, like, you know, that are being configured by declarative config and change them, enhance them, change them in some way. So, I can't really relate to that. Marilla was explaining to me the node process a little bit, and how you know, if I understand correctly, and let's jump in if I get this wrong, but there's sort of, there's sort of a global initialization phase, where before any sort of application code runs that would configure SDK components.
The declarative config file is potentially red, if it's present, and set up as, you know, there's a global tracer provider, meter provider, logger provider, which are configured from it. And then later in application code, there's this opportunity for users to configure their own SDK, and so you're… it's essentially a question of what happens between that global that was configured from the declarative config file and this sort of user space, which is… is that a kind of correct characterization of it?
Jamie Danielson 00:06:24 Yes, I think so. Yeah.
Marylia Gutierrez 00:06:33 Yeah, and to give, like, the example is also, like, right now, for example, you… we have the same issue with environment variables and the programmatic one. So today, we… have giving priority to the programmatic one. So if a user has something, like, they enable or do something on programmatically, we kind of ignore whatever is the value on environment variable.
So that, if you want to, like, for example, continue with that same idea. We are just changing the environment variable to be, like, the clarity config, and the programmatic will still take precedent.
Is that a fair assumption, or we should change the order? But yeah, that is the challenge there. We don't know Who takes priority?
So there's no specification on this, and, you know, there's no specification on this other thing that you were describing, the interaction between environment variables and the programmatic config APIs.
Jack Berg 00:07:34 And so, like, I'm not sure this spec can give us guidance.
On environment variable and programmatic configuration interaction and priority at this point, because people have tried, and I think, essentially, the ship has sailed, because some languages have gone in one direction, and other languages have gone in another direction, and both are stable at this point. And so there's no way to, like, retroactively give guidance that makes everybody happy.
So… Maybe we can fix that with declarative config. Maybe there's still an opportunity to, like, have some very clear text that says a particular thing.
I… my guidance on this is… and so… I mean, I know you all are from the JavaScript seg, but I think JavaScript got this wrong, actually. You know, and so this question of… and let's just take environment variables and programmatic, programmatic API interaction. I think the JavaScript direction of trying to layer in both leads to unintuitive behavior.
you know, and it's not really clear what you're going to get, and you can get some sort of surprising results. And I wouldn't try to figure out how declarative config continues that pattern. I would use this as an opportunity to say, like, let's start fresh, and, like, what's… What's the best thing we can do, sort of independent of what we've done previously?
And I know that's sort of an abrasive position, but… I've heard about the JavaScript state of the world for years now, and every time it comes up, I've just found myself shaking my head.
Jamie Danielson 00:09:18 Yeah, I mean, even thinking about, for example, like, with declarative config, it's… we do have it specced, right, that once this is enabled, then ignore other environment variables unless they're, you know, specified within the config file. It could be a similar, sort of.
Idea of if there's declarative config.
Nothing else.
Like, it wins, always.
Could be a reasonable way of looking at it.
Jack Berg 00:09:44 Yeah, because the principle behind declarative config is, like, what you see is what you get. So you want to be able to write something in a config file and know that that's the state of the configuration of the SDK.
And so, any sort of layering sort of breaks that philosophy.
Where if you try to layer in, you know, programmatic API configuration on top of that, work, like, in that, it breaks that philosophy.
Marylia Gutierrez 00:10:13 Another option would be, like, if we can eventually just I don't know, does not allow programmatically config. It all has to be from the file, but right now, we do have a lot of configs that do not exist on the creative, like, it's not… do not exist on the file, so that means that we have to actually come here to this backend at all of those, and a lot of them, yeah, it's gonna be specific for JavaScript that doesn't make sense for the others, so we have, like, the sessions of the languages that we could potentially add everything there.
that is an option as well, but I don't know how people that are using will feel about that.
Jack Berg 00:10:51 Yeah, that's actually a great point, and Java has that same problem, so now we can speak the same language. So, if we go down to the declarative config section here, there's a kind of relevant bit to this, and it's, Where is it? So, Implementations may provide a mechanism to customize the configuration model parsed from the configuration file.
And so, the idea is, like, okay, when you set this environment variable, that's instructing the implementation to go and find the file at this location.
parse it into the in-memory representation of the data model, and then call create on that in-memory representation to configure SDK components from that.
And so, there's places where what is read from disk is not, like, sort of sufficient. And, One of them is, like, distributions. Like, maybe a distribution of the Java agent or the Node Auto Instrumentation tool.
wants to layer in its own, like, reasonable defaults, right? It doesn't agree with the defaults, and so it wants to read what the user is providing, and then, like, you know, automatically provide some fallbacks, or layer in some things.
And, So that's one use case. And then the other, and this is kind of a related topic, is, like.
How do you deal with parts of the, The programmatic interface that are not representable in declarative config.
And in Java, for example.
you know, if I can just kind of go navigate to the source code. Our OTLP exporters are a good example, so, I'm a TLP… So, we have all these setters on here to set a variety of things, and some of these map to declarative config, and some do not.
Right? So, like, you know, you can, for example, set a very fine-grained retry policy.
for how you want to retry OTLP export requests. That doesn't exist in declarative config. I think it's just, like, a Boolean enabled, or maybe we never even added it, because it was just assumed to always be enabled.
we have this, like, memory mode, and, like, memory modes are, like, this, you know, we can turn on these optimizations that make OTLP export essentially zero allocation, or very low allocation.
You can set a custom executor, so you can have some fine-grained control over how threads are managed in your OTLP exporters. And so these are Java-specific options that have no corollary in declarative config, and probably won't ever. You know, there's some things that, like, you know, we just need to solve in declarative config, like authentication. I think Gregor was talking about that. We need a new, We needed a new SDK extension plugin interface for authenticators.
And we need people to agree on what that interface is like, and, you know, what are the built-in authenticators and stuff, but, you know, that should come eventually. But then there's always going to be language-specific configuration options, which don't quite work.
And so, in Java, like, our solution to this is to, like, our first priority is to push everything into declarative config that we can, so that the set of Java-specific options are minimized.
And then the… the backup to that is, well, we have this thing.
So, let me try to… We have, the way that you load custom… implementations of any interface in Java is this… there's this mechanism called Service Provider Interface. And so you can say, like, hey, Java runtime, give me all implementations that implement this interface, and it'll load them up. And this is very convenient for providing, like, pluggability and And things like that. And so, we have this… we have this SPI that we have that's called our Auto Configuration Customizer.
And you can implement this interface, and if you do, then we will allow you to customize the SDK components, which are loaded.
by… right now, it's just our environment variable auto-configuration mechanism, but we're gonna do a similar thing for declarative config as well, where needed, right? So, like, you know, if you're… if you're saying, like, hey, interpret the environment variables and return SDK components.
you know, the environment variables are insufficient for describing all the things that you would want to configure, and so you can implement this interface to further customize things. You could take, like, you know, a propagator and, you know, customize it. You could take a… a span exporter and customize it, and every single component that is part of the SDK has, like, a customizer, where you can, like, get a handle to the instance that is being auto-configured, and then, you know, customize it to suit.
So this is the tool we're going to use to solve that problem of how do you configure Java-specific options and declarative config when those options don't appear in the config file.
That was a long…
GZ Gregor Zeitlinger 00:16:31 Can you say that we are adding that for Java as well?
Jack Berg 00:16:35 Yeah, so we reached a conclusion to do that in one of the Java SIGs, Gregor.
GZ Gregor Zeitlinger 00:16:40 Oh, crap.
Jack Berg 00:16:41 We're going to do it on a case-by-case basis. So where, for the environment variables, we have every single SDK component is represented here. For declarative config, we're going to do it as needed, right? So if somebody's like, hey, I want to be able to customize my OTLP exporters, and, you know, I can't… I can't express what I need to express in declarative config. Well, then we'll add a, you know, a hook in there to be able to customize that. So, the same concept, but just ad hoc instead of, You know, everything.
GZ Gregor Zeitlinger 00:17:13 So I could theoretically solve this, header use case with that instead of adding it to the spec, is that right, or am I missing something?
Jack Berg 00:17:25 No, you could do that, but the downside of solving it that way would be that it would only work for Java.
Right, so the…
GZ Gregor Zeitlinger 00:17:31 Yeah, understood.
Jack Berg 00:17:32 Yeah, but in the short term, you could.
Alex Boten 00:17:37 So… so bringing this back all the way to the initial question, in… in this case, how do you… How do you reconcile someone configuring… their… their settings in a Java application.
And then having these, service provider interfaces override or change what that configuration says, because it seems like it would end up being the same problem as what JavaScript was describing, is that right?
Jack Berg 00:18:08 It's… it's a different problem, because, like, let's take… let's take this, for example. So, this is a customizer that, is invoked for each span processor that is automatically being loaded and configured. So, you know, if you did a classic declarative config file with, you know, a batch span processor with an OTLP exporter, this would be invoked one time with your batch span processor.
And so, the difference is we don't have to… we don't have to figure out conflicts. There are no conflicts, right? So, like, every… it's like, the declarative config is the source of things, and then every component that is loaded from declarative config, the appropriate customizer would be invoked, and so, it's a very clear, I guess, prioritization, because it's not like, you know, the code is adding a processor, and declarative config adds a processor, and now which wins?
Right? Like, declarative config is the source of things, and then there's an opportunity to programmatically customize, you know, that source of truth.
Alex Boten 00:19:20 But am I understanding this right, that this is… so I guess in this case, programmatic would win over the config?
So whatever you have loaded in your environment that… like, whatever SPIs you have loaded in your environment would… potentially win over whatever is configured in the file. So, like, if… if the customizer goes and changes, like, the destination of your… of your OTLP export configuration or whatever, then, like, as long as that SPI is found in your Java environment, then you would… Like, that would be the end result that would ultimately override the config file, is that correct?
Jack Berg 00:19:55 Yeah, so, I guess then there's two things that we were talking about. There's, like, how do you resolve conflicts, and which sort of takes priority? And so, there is no opportunity for conflicts here, because, you know, you don't have this issue of two people providing processors. It's just the declarative config provides the processors, and then the customizer is maybe invoked, you know, depending on what is the… in the declarative config file.
and… but then the other question is, like, yes, you know, you can say that in a declarative config file, my OTLP exporter should export to foo, and then, you know, that might not end up being the case, because something overwrote it, and this… a customizer was on the class path and overwrote it.
And, like, that's why I don't like this, right? So, like, this… this violates the what-you-see-is-what-you-get philosophy, too, but it's like, what choice do we have?
like, I'm stuck. You know, declarative config is insufficient for describing everything, and it always will be, because you can't describe everything in text.
GZ Gregor Zeitlinger 00:21:07 I have worked with such a setup in the Java agent, where I had processors and declarative configuration.
And from that experience, I would say that, the, the… what is it called? The plugins that work on the… on the YAML, they are not overriding, they're just, adding the pieces that are not possible to describe in YAML, so in… In that sense, they are not overriding it. You still get what you see in the YAML file.
Jack Berg 00:21:42 But Gregor, you totally could write a customizer that, you know, said, hey, there's a span exporter here. It's an OTLP span exporter. I want to, you know.
detect that, and change its endpoint, and return a different one in response.
GZ Gregor Zeitlinger 00:22:01 Yes, you could, you could. The thing is that this is not, how it's meant to be, and you, so you kind of have the instructions not to do things that are, causing unexpected behavior.
Jack Berg 00:22:15 Yeah, I would agree with that. Like, don't… don't do that.
Alex Boten 00:22:19 Yeah, I mean…
Jack Berg 00:22:20 Use this as a tool to enrich your configuration with things that can't be expressed in YAML, not to, like, you know, break the philosophy.
Marylia Gutierrez 00:22:28 I guess the idea that what Java's doing is just, you don't have… well, I guess you can have, but the theory is that you don't want to have any programmatic config that already exists on the declarative file.
Jack Berg 00:22:43 Yeah, I would say that. It's like, you know, if you want to use the programmatic config API, use that. And use only that. And maybe you can layer in some calls to fetch environment variables, you know, when you're typing out your programmatic config, but that's your choice.
And if you use to… if you want to use declarative config, then, you know, use that. But don't try to mix these two things together.
Alex Boten 00:23:07 Yeah, I mean, I often think of this as different personas, right? So you might have the person who wrote the code initially, and then you have the operator who's just trying to use declarative config, because it's easier to… Deploy the same application across, or the same configuration across multiple different applications, without necessarily needing to know the ins and outs.
But maybe the person who authored it didn't know about it or wasn't planning on using declarative config, and so I think… even assuming the best possible intentions, you know, reading all the instructions on the package or whatever, I could imagine how… like, it's not possible to get it right in all cases, no matter what we try, I guess.
Marylia Gutierrez 00:23:48 Yeah, so one thing that I'm thinking now is, though, okay, I'm gonna go case by case of all the available config that we can do, like, programmatically, see the ones that we can move to the declarative config.
maybe, like, just remove them as an option to the programmatic, but probably gonna open, like, this as a discussion of the JavaScript.
Repo, and just get, like, actual users' feedback on that.
Jack Berg 00:24:13 Yeah, a couple of comments. Like, one, I would say that a good, safe starting position is to not try to layer in programmatic config at all. Like, wait for demand for that, and then figure out how you're gonna solve that. Because, you know, just like, adding that complexity initially without knowing really how people want to use that, it's gonna be a big headache.
So, it's definitely simpler to punt on that for now.
Marylia Gutierrez 00:24:37 I kind of have to start with having, because there are things that don't exist on the declaratory config, so I need to have config for some of those things, at least.
Jack Berg 00:24:46 And have you actually had people that have asked for those? Because I know the configuration space is, like, really wide, and there are going to be things that can't be expressed in declarative config, but in practice so far, this capability that I described for customizing components this is hypothetical. Like, we haven't added this yet for declarative config, even though we're okay with adding it, because nobody has needed those additional customization options.
like, there are things that you cannot express in declarative config. It's only available in the programmatic API. We're okay with adding a mechanism to, you know, access those programmatic config APIs. We haven't had it to yet, because nobody has actually, like, needed those things.
So it's like, you know, this is a… this is how we would solve this in principle, but we haven't actually needed it.
GZ Gregor Zeitlinger 00:25:34 But this is also a chicken and egg problem. People are not picking up declarative configuration because it is missing a lot of features. So, for some cases, you can wait for demand, but kind of have to determine what a good minimal set is.
Jack Berg 00:25:54 Definitely. If you've heard anything that suggests that there's some key features missing, some key minimal features missing from declarative config, I would love that, to know that, and definitely want to accommodate those users.
So…
Marylia Gutierrez 00:26:09 Yeah, I just put it here in case you're curious. Those are all the options for, like, programmatic config that we can do, so… A few of them, yeah, you can see that we have a way of doing this.
like, the processors, like, log records, stuff like that. But yeah, a few things we need to kind of, like, check.
Jack Berg 00:26:29 ID generator is not supported yet. It should be supported. It's just a matter of us implementing it.
This is… this is obviously the top-level set of things, right? And so, within these, there's, you know, the configuration surface area just kind of balloons outwards and gets really big, so… Yeah, but it'll be hard to say just what the full set of unsupported things are, but, you know, there are things.
Yeah, so, like, it… Does anyone else… does anyone think that we should write this in the spec?
this, like, you know, this thing I suggested, which is, like, when you use declarative config.
We don't try to layer in… by default, we don't try to, like, layer in programmatic configuration. It's like, you know.
Just like the environment variables are ignored, other calls to programmatic configuration APIs are ignored.
GZ Gregor Zeitlinger 00:27:37 I would tend towards yes, since this has come up Repeatedly.
Tyler Yahn 00:27:44 I would… I would suggest… If you want to add that, it would be supplementary. Like, I don't think you can normatively say something like that, though.
Jack Berg 00:27:53 Why?
Tyler Yahn 00:27:55 So I think that it may work for some languages, but I don't think it's gonna work for all languages.
Jack Berg 00:28:01 But this is Greenfield, right? So, like, I know there's historical context, which has, like, caused… where, you know, languages took different approaches with environment variables and programmatic configuration, and, like, the interaction between those, but, you know, maybe we have an opportunity to have a fresh start.
Tyler Yahn 00:28:19 Yeah, I still don't think that applies if you have a language that already has a precedent set, and you have expectations from users, and then if you come along and say that now this isn't going to actually happen, that language may be put out because their user base is not going to have that expected behavior.
I think there's also languages where, like, And they can go, and it… you can explicitly do whatever you want.
So if a user decides that they want to actually mix in their declarative configuration with a programmatic configuration.
they can go ahead and do that. So I don't think you can normatively say that we need to restrict that. I think that would be a misstep.
Jack Berg 00:29:00 Well, okay, so two thoughts there. So one, the lack of normative language around this is gonna haunt us.
So, you know, it's just like the environment variable programmatic configuration interaction just continues to come up, and, you know, we… it's like every couple of months, it comes up in the spec. What do we do about this? We're like, well, we can't… we can't say anything, because the ship has sailed there.
And then, so, like, you know, I think we're not in a great spot if we can't normally… if we can't have normative language around this. And then the other thing that you said, How does that work? But you're saying go… You said Go could, you know, you can explicitly do whatever you want.
Tyler Yahn 00:29:46 Because you're producing an SDK with some sort of, like, configuration provider, right? But that SDK can be configured external to that?
Jack Berg 00:29:59 So I guess what I would say is, like.
like, the normative language that I would say is, like, hey, we have these operations, parse and create.
I would say something to the effect of, like, when you call create.
The SDK returned by that is only configured via the contents of the configuration file, and, you know, there's no sort of attempt to layer in calls to programmatic configuration APIs.
Right? So it's just within the bounds of this create method. Like, when you call this, everything is, like, what you see is what you get.
And, you know, you can of course create SDKs outside of that with the programmatic configuration API.
Tyler Yahn 00:30:39 Yeah, I think… I'm a little hesitant to say that it, like, it should be that way, because like you've already described, like, in Java, that's not sufficient, right? And you need these extensions.
Jack Berg 00:30:51 I know, I know, and I would try to thread the needle, but, like, I guess what I would try to solve with that normative language would be the, like, the… the conflict problem.
Like, I hate that there's, like, conflicts. Like, hey, somebody wrote a pro- like, tried to add a processor to the SDK, and there's already a corresponding processor in the declarative config file. What do we do about that?
Tyler Yahn 00:31:14 Yeah, I mean, I understand that you hate that, but, like, you have to understand, like, that's an emotional, like, understanding of how you think the world should be and how code should be, right? But that may not be a shared… sentiment within a community of programmatic, like, configuration.
And it may not be something that is, I think, universal to all languages. So what I'm saying here is, like, I think maybe a recommendation seems reasonable.
And I think that, like, it helps in that sense, but I think saying that, like, people can't do this.
If they want to be… you know, fully implementing the declarative configuration, I think that that may be restrictive, especially… when we already have these things that you're saying, like, you're trying to thread the needle, but I think you're trying to thread the needle in a way that works really well in the Java ecosystem, and that may not, like, follow suit for other languages. Like, that's the first thing that comes to mind, is all of these things that you're talking about that are not representative in programmatic configuration, right?
like, there's nothing saying that, like, okay, you should also be able to provide, like, customizations to this SDK during, like, the creation, but I'm gonna also include here a little caveat in saying, like, you shouldn't do X here. In the same way that you're saying in these extension APIs that you have in Java, like, you could… you could, in theory, like, completely change the endpoint of this OTLP endpoint, but you shouldn't.
Right? Like, if we're going to restrict on a documentation base, not on a syntactic base.
I think that that's something that then becomes relevant to the instrumentation, or sorry, to the language implementation.
Jack Berg 00:32:47 I see what you're saying.
Tyler Yahn 00:32:51 And I don't disagree with you, I think, like, your desire to strive for… lack of confusion is not only admirable, but I think is what we want to try to do. But I think to say to all languages that, like.
Prescriptively, this is how you need to implement something, is going to… is going to be too restrictive.
Jack Berg 00:33:13 Yeah, So, like, this is probably… this conversation right here is probably just, like, an example of why… an example of why we don't have specification around this. You know, this just basically bleeds into the… that long-standing issue about environment variable programmatic configuration interaction.
And, you know, this is just, like, a new flavor of it. And so, when I was writing the declarative config spec, I probably couldn't reach consensus on this, or didn't think I could get consensus on it, so I just ignored it.
Tyler Yahn 00:33:51 Yeah, and I, I mean, I'm… I like… I like the… the recommendation idea, but I think… I think… Putting hard requirements, saying that this is not something you can do.
It just seems, I'd have a hard time selling this, I think, in Go, is to try to redo this in a way that you can't do that.
Jack Berg 00:34:10 Let's… yeah, so Alex is calling time check on this.
Tyler, I am just out of curiosity, I'm not disagreeing with this, but, like, out of curiosity, I am interested in how you could achieve what I was talking about in Go, like, you know, customizing the results of declarative config. So, yeah, maybe I'll just reach out to you in a sidebar, just to see how that works.
Tyler Yahn 00:34:32 Yeah.
Jack Berg 00:34:32 Maybe there's… 4 Alex.
Yeah, URLs, right?
Tyler Yahn 00:34:35 Yeah.
Jack Berg 00:34:39 Okay.
Long, good discussion.
Didn't reach a conclusion, but That's some of the context, Marlia and Jamie.
You have any. You have the next topic.
Yevhenii Solomchenko 00:35:00 That's about, where we should place the vendor-specific configuration.
Jack Berg 00:35:06 Okay.
Yevhenii Solomchenko 00:35:09 row.
Pre-proposals for that?
Just a small example.
Right.
What workplace?
Jack Berg 00:35:24 So, this… this question has come up a number of times. I don't have good answers on this. So sometimes vendor-specific code, or, you know, vendor-specific stuff that's bundled in distributions, it's like.
you could call it instrumentation. You know, maybe if you just look through it through the right lens, it's like, oh, this kind of feels like instrumentation to me. And in that case, like, I think it's a no-brainer to put it in its own instrumentation block, you know, in Proposal 3 here.
But then there's other bits of vendor-specific instrumentation, or vendor-specific config, which don't feel like instrumentation at all. And that doesn't feel right. Like, you know, putting them in instrumentation when they're not, and, like, maybe we're kind of looking at this with this realm and access token, like.
what do those have to do with instrumentation? Those don't sound like instrumentation concepts to me, and so it feels weird to put them under the instrumentation block. These feel, like, more like parameters for an exporter, maybe, or something like that?
But I'm not really sure how the… The, you know, the vendor distribution works.
I think what I would say is that, At the top level, the OpenTelemetry configuration type.
allows additional properties. So you can have a top-level key called Splunk with whatever configuration you want in it. And, you know, I think if we dug back through the Git history, this type of thing would be the reason why this is… additional properties is true instead of false.
So, We don't have guidance on this. You have options available right now, and I guess we gotta kind of figure this out as we go.
Maybe, maybe.
Yevhenii Solomchenko 00:37:18 Okay.
Jack Berg 00:37:18 Maybe more use cases would be good, if we could have, like, a… if we could get other distributions, like Grafana and other folks using this to, like, engage on this issue that you've opened up, we could start to see if there's any common threads.
GZ Gregor Zeitlinger 00:37:32 I have, had the same question with the Grafana distro.
And, I would agree that instrumentation is not the best place.
But I'm also not happy with the top-level configuration, since recently I had a bug that I accidentally put something there.
Which, luckily, you caught. So, having a vendor block.
Like, your proposal one at the top level sounds, like a much more natural Affixed to this specific use case.
Jack Berg 00:38:13 I'm not opposed to this idea.
Yevhenii Solomchenko 00:38:24 Right.
Jack Berg 00:38:27 Do you want to open a PR proposing this? And folks can kind of vote with their… their approvals?
Yevhenii Solomchenko 00:38:37 Okay, I'll open the bar.
But, you have a comment later about, Which, that, vendor… should do. It's a… must provide some… Provider to get those configurations, like in the instrumentation.
Jack Berg 00:38:59 Oh, how does… how does the vendor code actually access this?
Yevhenii Solomchenko 00:39:03 Yeah, for that.
That, config provider.
GZ Gregor Zeitlinger 00:39:08 I know how this would work in Java. Is this a Java question?
Yevhenii Solomchenko 00:39:13 It's for a .NET question. I don't know, I think for Java and, for JavaScript also.
GZ Gregor Zeitlinger 00:39:19 Yeah, maybe, we can, take the idea from Java, where we already have, A callback, to, I think to modify the model, you get a model in, and… You return a model out.
And then you can set… in this case, I think you would set the header.
If it's a dynamic header, then things are more difficult, And I have already tried to take that through the spec, but in Java, it's not possible.
Because we don't have this callback that Jack talked about.
Couple of minutes ago.
Jack Berg 00:40:04 I think this could be a little bit more complicated than that, Gregor, because, like, this vendor-specific configuration, it might want to do things like… Dynamically modify the contents of a config file.
Or at, like, you know, interlay.
default values, right? Or maybe, like, add an exporter, or a processor based on, you know, the configuration that's in the vendor block.
And so, if that… if those types of use cases emerge, then you kind of end up having a sort of interaction between the content in this vendor block and the create and parse operations, potentially. And kind of what's that interplay? Like.
You know, are there hooks or callbacks or something, you know, that, the vendor-specific code can, can access and use to, you know, access this information and then manipulate the results of create and parse? Something like that.
GZ Gregor Zeitlinger 00:41:09 But in Java, we already have that.
Jack Berg 00:41:13 It's… We, can you do all of this stuff? Yeah, maybe you can do all of it already, because.
GZ Gregor Zeitlinger 00:41:20 Well, the limit is if you want to have a model that has dynamic behavior.
That is not possible in Java right now.
Jack Berg 00:41:31 Yeah. Okay.
GZ Gregor Zeitlinger 00:41:32 So you can add static headers, if we are talking about an exporter.
Jack Berg 00:41:39 Yoveni, so this is kind of what we're talking about here. There's a line in the spec that say, says, implementations may provide a mechanism to customize the configuration model that's parsed from, you know, the contents of this file. And how that manifests in Java is, like, we, What's it called? Model Customizer?
GZ Gregor Zeitlinger 00:42:04 Sounds about right.
Jack Berg 00:42:05 Something like that, right? I think… I think I got it right.
So… you know, the way you do that in Java is you implement this interface, and then when a declarative config file is being, like, loaded and interpreted, you get, you can, you know, implement this method to get access to the resolved configuration model, and you can return your own instance of it.
So this function here could then have access to all of the vendor-specific code in there, interpret its contents, and use that to selectively modify the, you know, the model itself, or to do whatever else it needs to do upon initialization.
GZ Gregor Zeitlinger 00:42:48 I actually have a, draft PR for the Java… sorry, for the Grafana distribution that already does that. I can link it here to look at as a reference.
Jack Berg 00:43:02 So I guess, like, that, you know, this guidance and the spec Might be sufficient to be able to accommodate these vendor requirements.
If a language actually adheres to this guidance.
Yevhenii Solomchenko 00:43:19 Okay.
So, we decide to use a first proposal, yes, a vendor where we have a vendor note, or…
GZ Gregor Zeitlinger 00:43:31 I would support that, yes.
Jack Berg 00:43:33 I would support that, you know, we can't really say that we make decisions synchronously on the calls. We can agree amongst the three of us, but there's other people that are engaging in this discussion. They might have other things to say when you open a PR. So, but, you know, I think I tentatively approve of this direction, so…
Yevhenii Solomchenko 00:43:51 Okay.
Cool. Thank you.
Alex Boten 00:43:54 I have one question. So, do we have the concept of vendor as a thing that we support in the spec?
Like, would it make more sense if this was called, like… Distribution? Or something like this? Because at least we have that concept, and as I'm listening to your discussion here, it seems like distribution is the common use case for wanting this.
Jack Berg 00:44:15 I think that's a good recommendation. Just use whatever vocabulary we already have, sort of prior art around, and distribution seems to be the open telemetry vocabulary for this.
And, you know, that'd be great, honestly, because this concept has come up a number of times in Java, so, you know, I'd be happy if we got a resolution here, and we could just point to people to something concrete. So, thanks you, Venny.
Yevhenii Solomchenko 00:44:46 The term?
GZ Gregor Zeitlinger 00:44:48 Actually, a good point, and that, JavaSIC, we discussed that we want to have a node under Java that is called Agent and Spring Starter, or Spring, I forgot, which are also distributions, but they are not vendor distributions, so I'm not really sure if that's a good argument or not, but they have some properties under there.
Jack Berg 00:45:14 Yeah, maybe… yeah, we could… we can argue about that, Gregor, whether they belong in an instrumentation block or a distribution block.
GZ Gregor Zeitlinger 00:45:22 Yeah, right, but I don't want to complicate this discussion.
Yevhenii Solomchenko 00:45:25 Right, yeah.
Issue for that also created in the configuration issues.
With having .NET similar situation.
We have a lot of… Falcon version.
Jack Berg 00:45:42 Any other comments, or should we move on?
Yevhenii Solomchenko 00:45:47 Click on mobile.
Jack Berg 00:45:48 Okay, As I've noted in Slack and on these calls, I'm aggressively trying to tackle all of the problems that stand in the way of stabilization of this.
Long-time contributors like Tyler and Alex and I have… have been doing this for coming up on 3 years now, and it's time.
So, one of the key things that is underdefined in our data model is what to do when properties are, are omitted, or are set and null . And, that's an important thing to specify.
Because if we don't specify it, when we later try to specify it, we're going to have disagreements between languages. So, like, this is one of the things you want to define up front, rather than try to add later. And so, what this PR does here is it adds build tooling, That goes and, you know, it goes through all the types and properties in the schema, and if any property is optional.
it enforces that you add a field called default behavior. And default behavior is where you're going to describe in just, you know, plain English, what happens when that field is omitted or null .
And so, you know, Alex and I kind of were going back, there's this… JSON schema has this, this keyword called default.
Which is, like, you know, similar in concept as this, but default is supposed to be, you know, the value of your default is supposed to be the same type as whatever property, you know, you're defining that default for. So, you know, it's supposed to be an integer, or a string, or an object type that actually compiles against the schema that it's, you know, representing the default of.
And that's, like, in my opinion, it's insufficient. We have a… we have things… we have semantics which are embedded in our defaults, which you can only describe in plain English.
And so that's kind of why I've deviated from using that keyword.
There's also a new keyword I've added called null behavior, and that's because sometimes you want to differentiate between the behavior when a property is omitted versus the property is present and null .
Right? Those are two different behaviors. Sometimes they're identical, sometimes they're different. And, you know, I have examples that I talk about in this PR of where the semantics are different, so… This PR adds all the tooling for this, and if and when it gets merged, there'd be a follow-up step to actually go through the schema and replace all of these to-dos with actually formal specifications for what the default semantics are.
So, that would kind of be a follow-up step. So… Yeah, take a look at this, let me know what you think. That's my pitch for this PR.
Tyler Yahn 00:48:52 So, Jack, I think this is great, by the way. I just had a question on, like.
I haven't looked too deep into this, I took a quick look, but what's the… What's the default null behavior if it's not specified?
Jack Berg 00:49:05 So, you can… every optional property requires a default behavior, and you can optionally include a separate null behavior. But if you don't define null behavior, then it's, like, assumed that the default behavior and null are the same.
Tyler Yahn 00:49:21 Okay, yeah, that was my only question. Okay, yeah, cool.
I do think this is great, though, because, like, it does allow a lot more… clarity into what… what should be done here, and I think that this is… yeah, I think we should try to move this forward. I still have… like I said, only written through it, like, once, so I'm trying to read through it again.
Jack Berg 00:49:52 Oh, and check it out, so, when… this is the branch that PR is based off of. And so, we have build tooling that takes sort of the source schema, which is defined in YAML now, and has additional keywords, like this default behavior and null behavior, which aren't part of JSON schema, and the build tooling compiles, you know, a JSON schema, which is completely valid, only uses JSON schema keywords, and is defined in JSON instead of YAML. And, you know, there's reasons for that, that, you know, I've been iterating on this rapidly over the last couple of weeks. But one of the cool things now is that, So we have build time validation that all properties that are optional, you know, are forced to have a default behavior defined, and then that default behavior, it's rendered in the descriptions of all of these properties, right? So your build tooling, when you're generating bindings for your language.
you can, you can generate, you know, comments, descriptive comments for all those fields and types automatically, where the default behavior is, you know, explicitly stated. So, better user experience around this as well.
Tyler Yahn 00:51:04 Yeah, it looks great.
Jack Berg 00:51:08 If omitted, no op meter provider is used. If omitted, blah blah blah, so… Yeah, and, like, we can… we can kind of take this further if we want to. Like, anything else that we want to include in this description, which is available to the, you know, the… the tooling, we can… we can figure out how to represent it as text and embed any information we want in this description. So, that's nice.
Tyler Yahn 00:51:34 So what does happen when you want the default behavior to be, like, a particular value that is, like… type value. Should you still just use the default, field in JSON schema?
Jack Berg 00:51:46 That's… that's a good question. Here's what I… here's some examples, right? So, like, like… here's an example where, you know, you actually need text, right? You can't describe this with just you know, a string that is going to compile against the string type expected by this property. This is the endpoint. So you have to say, like, hey, the endpoint is this, and depending on the context, the signal is either traces, logs, or metrics, right? But, there's other cases where it's a very concrete value, and here's one. So, like, this is… what is this? Timeout, some sort of timeout field. So, 1,000 is used. So, I wrote it as English, 1,000 is used, or maybe that's 10,000. 10,000 is used, but, like, it could just as easily be, you know, a number, 10,000, and then maybe the tooling would interpret that and do something different with it, but… This is what I've done for now. It kind of looks ugly to have to say, like, is used for all of these, but… I don't know, that's where I'm at.
Tyler Yahn 00:52:54 Yeah, maybe… maybe iterating and having, like, a default value field as well here would be cool, but… Yeah, then you got conflict resolution, which maybe… actually, I don't know, maybe there's a reason for both, but… I think this is a great starting point, at least. Yeah.
Jack Berg 00:53:11 Yeah, and like, what I want to do, Tyler, is I want to update our… I want to update our stability definition. We have this block here about what are… what changes are allowed and disallowed, and I want to… I want to find the right language to describe that, like, default behavior like, we… we have… we have to be able to evolve it, but we can't break users. And, like, what are the right words to describe, you know, how default behavior can be evolved safely? And, you know, we're gonna have to take a crack at that. But, you know, essentially, the philosophy will be, don't break users.
And, you know, but I think within that, like, we should be able to modify the tooling for how the default semantics are described, you know, in the source schema, without it being considered a breaking change. So…
Tyler Yahn 00:54:05 I see, so… so, like, that timeout, right? Like, if you wanted to change that timeout value.
From… I can't remember if it's a thousand or something.
Jack Berg 00:54:13 10,000, yeah.
Tyler Yahn 00:54:14 Yeah, it's a 10,000 to, I don't know, 2000 or something like that.
Like, you're saying, like, we have to have rules on whether that's allowed or not?
Jack Berg 00:54:23 I think we have to say, in abstract enough language to cover all of these cases, that changing it from 10,000 to 2,000 is not allowed.
Tyler Yahn 00:54:33 Yeah.
Yeah, I think that's… that's… that's important.
Right. Because I think about…
Jack Berg 00:54:40 But I do want to preserve the ability to switch from, like, saying, like, 10,000 is used to just, like, 10,000.
Right? As long as the meaning is the same. I want to preserve the ability to do that, but I don't want, like, I want… because that's just build tooling stuff, like, how you're expressing it. But, the meaning of it shouldn't be able to change in a breaking way.
Tyler Yahn 00:55:01 Yeah, I gotcha. I mean, I think as long as it's semantically equivalent, right, like, that's… that's what you're going for, you know?
Jack Berg 00:55:07 That's right.
Tyler Yahn 00:55:07 Yeah.
Jack Berg 00:55:12 We're coming up on time. Gregor, do you want to give a quick pitch for your topic, or do you want to take it over, do it async?
GZ Gregor Zeitlinger 00:55:23 I want to give it a trick, a quick try. I've come across this issue. I don't know if it has a fix. Environment variable replacement in the SDK part does not change the type, so you can, Use a variable to put in your port, because the schema knows that it's supposed to be an integer.
But this is not true when you are getting into the untyped territory with additional properties.
And, I don't know if this is a buck, or if this is already covered.
Jack Berg 00:56:02 This should be covered, because the environment variable replacement should work.
sort of before a YAML parser goes and interprets the value.
And so all the examples here sort of, are… are still the same. These are examples about, like, you know, for a given input and, you know, set of key-value pairs, how does… how does environment variable substitution resolve?
And all of these are schema agnostic. So these examples are true, whether or not we actually know the schema and the expected types of these properties. And so, if there's an issue with that, Gregor, it might be Java-specific, and we should go look at that.
GZ Gregor Zeitlinger 00:56:41 No, it's not about Java. I'm just thinking about, in an environment variable, how do you say that it's a Boolean instead of a string?
Jack Berg 00:56:50 So, in, the… just… so, in… in YAML, if you put quotes around something, it's guaranteed to be a string. If you leave it unquoted, then there's YAML-like semantics for how that, like, unquoted value is interpreted as a.
GZ Gregor Zeitlinger 00:57:08 Okay, that is what I was looking for. Thanks a lot.
Jack Berg 00:57:14 And there's also ways where you can force the type to be something else. There's this special syntax where you can, like, instruct the YAML parser to interpret it as a particular type.
Okay.
Alex, how do we get this moved out of development experimental? The spec's gotta be stable.
Alex Boten 00:57:34 Ugh… Fair. I… this is me being very selfish here, but the problem I am running into is the collector's configuration has forever, exported things with Prometheus colon as the key to configure the Prometheus Exporter, and in this latest version, we're… Replacing it with… Yeah.
Maybe I'll just follow… Follow up with those guys.
Jack Berg 00:58:06 They're working on stability. They have this same goal in mind. They want to stabilize the Prometheus compatibility document and the Prometheus exporter document.
Alex Boten 00:58:16 Yep.
I'll follow up with him.
Jack Berg 00:58:23 Propagator discussion from last week.
GZ Gregor Zeitlinger 00:58:25 Yeah, this was just a quick question, Two weeks ago, we said that we could continue the discussion about default propagators in a PR, but I couldn't find a place where that PR should be open, which repository, and which page.
Jack Berg 00:58:48 So, if I recall correctly, that was about the default semantics of of propagator.
Right, so…
GZ Gregor Zeitlinger 00:58:57 You don't specify.
Any…
Jack Berg 00:59:02 Right, so, the schema is defined here, propagator is defined here, and somewhere we say we have language that says this, like, you know, if the resolve lists, the propagators is empty, and no op propagator is used. So, like.
GZ Gregor Zeitlinger 00:59:17 This is the… Oh, that's where it is.
Jack Berg 00:59:18 Yeah, this is where we define the defaults.
And all of that sort of propagates to other places throughout the configuration repository, like, you know, the build tooling copies all that into OpenTelemetryconfiguration.json.
GZ Gregor Zeitlinger 00:59:34 Okay, I didn't find that, thanks.
Jack Berg 00:59:36 Okay.
All right, somehow we made it through those last three topics very quickly, in just a couple of minutes. So, yeah, we ran over a little bit, but, thanks for the discussion, everybody.
If you live in the U.S, have a good Thanksgiving, and I'll see you all in a couple of weeks.
Jamie Danielson 00:59:59 Thanks, Austin.
GZ Gregor Zeitlinger 01:00:00 True.
Yevhenii Solomchenko 01:00:02 Fair.
