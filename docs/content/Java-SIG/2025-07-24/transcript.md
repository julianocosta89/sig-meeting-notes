SIG: Java SIG
Date: 2025-07-24
Duration: 48 minutes
============================================================

## Zoom Recording Transcript

**GZ Gregor Zeitlinger** 02:34 Hello! Again.
**Robert Niedziela** 02:39 Hello! Hello!
**GZ Gregor Zeitlinger** 02:40 I added your name to the last agenda, Robert, but I thought I might misspell your last last name. Sorry.
**Robert Niedziela** 02:48 Okay, I'll I'll yeah. It's not trivial one. I will put it there.
Thanks.
**GZ Gregor Zeitlinger** 03:02 But I can actually copy it from the last one.
**Robert Niedziela** 03:09 Okay. Great. Thanks.
**GZ Gregor Zeitlinger** 03:42 Peter, you're typing in the wrong.
Oh, that was the meeting an hour ago.
**Peter Findeisen** 03:52 Okay.
Yep.
**GZ Gregor Zeitlinger** 03:58 You already figured out that Trask is on vacation.
I can drive the meeting.
Someone else wants to do it. I also don't mind.
Traska's joining just didn't have time before.
**Trask** 04:26 Hey, folks? Sorry I'm driving today, so need somebody else to join somebody else to drive the meeting. I'm driving the car.
**GZ Gregor Zeitlinger** 04:39 Yep, I can do it.
**Trask** 04:42 Thank you.
**GZ Gregor Zeitlinger** 04:45 Where are you driving Strask.
**Trask** 04:48 Up to Washington. vacation meeting some friends.
**GZ Gregor Zeitlinger** 04:57 Nice.
**Trask** 04:59 Yeah.
**GZ Gregor Zeitlinger** 05:07 Hey?
Can you read my screen, or is it too small?
**Jason Plumb** 05:13 It's good.
**GZ Gregor Zeitlinger** 05:16 Okay, this is the right place, but we don't have any agenda yet.
**Jason Plumb** 05:27 Is that right? Or that's right.
**GZ Gregor Zeitlinger** 05:32 Okay?
Then that's add topics.
**Jason Plumb** 05:36 Unless people put it in the wrong place.
**GZ Gregor Zeitlinger** 05:39 That's why I'm asking now with 2 meetings that are happening, or 3. The Apec also, then, and can happen.
**Trask** 05:54 Yeah, we had no topics for Apac yesterday, so we skipped it.
I think it's summer.
**Jason Plumb** 06:04 Robert, did you want to spill over your configuration topic? Then.
**Robert Niedziela** 06:10 Yeah. So maybe that's a good good point
**GZ Gregor Zeitlinger** 06:29 Do we do those first? st Did you try it?
**Trask** 06:39 We haven't been lately.
**GZ Gregor Zeitlinger** 06:42 Okay, and let's not change habits in summer.
Robert, do you want to start.
**Robert Niedziela** 06:50 yeah, so actually, I wanted somehow to start discussion about ways to validate the declarative config after it's customized because we we have really big flexibility in making customization.
But at least I don't know. Maybe there is. But I didn't find a dedicated place to make the validation. If if the data is consistent, or if we want just to make some extra validations that are not present already in the core, and yep.
**GZ Gregor Zeitlinger** 07:31 Are you talking about like the property? Has the right name, or something else?
**Robert Niedziela** 07:36 No. If, if, for example, URL is is valid I know it. It explodes at some point right somewhere in the future, when some request is, for example, the endpoint right but I would like to have this validation as early as possible, not waiting for the 1st reporting metrics or or some other stuff.
Or I don't know if we have like a service name provided, or in resource, or some other property. Because we don't have later easy way to to validate it. The resources particularly tricky stuff. There, there's some Pr about constructing resource.
and have some some insight into it, but now now it's it's pretty tricky to validate some some resource properties.
**GZ Gregor Zeitlinger** 08:34 Do you have an example, handy, that you could paste here to illustrate the problem.
**Robert Niedziela** 08:41 I'm afraid I cannot paste it here.
**Jason Plumb** 08:44 So I is this is this stemming, Robert, is this stemming from in our distribution? We have some customizers that do validate that? Yeah. Okay. So when switching over to declarative config, we wanted to be able to maintain that same level of validation early in the lifecycle in order, and I think the result of a validation failing is probably just a log message.
**Robert Niedziela** 09:07 Yes, there is some log message displayed. Yeah.
some warning, actually. And that's that's it. But there are also URL validations. And and this kind of stuff, because we may. Yeah.
**GZ Gregor Zeitlinger** 09:29 Okay, what? I'm.
**Robert Niedziela** 09:31 That's 1 more thing. Why, it's it may be needed.
Because with this declarative configuration customizer we can really rebuild the whole config, and while, while some schema is validated. When parsing right, we can programmatically or make really nasty stuff inside.
After parsing.
**GZ Gregor Zeitlinger** 09:58 Yeah, but.
**Jason Plumb** 09:58 Isn't this isn't the schema more about the shape of the data model and the types, and not necessarily the content.
**Robert Niedziela** 10:08 Yeah.
**Jason Plumb** 10:09 But the thing that you're describing is more of like a content validation like a validator for content.
**Robert Niedziela** 10:15 So I think we need both, because with this customizer we can create additional notes. We can.
you know, at add some how to say it.
**Jason Plumb** 10:33 Got it. So the customizer allows you to manipulate the the data model in a way that would break the schema.
**Robert Niedziela** 10:39 That's I think it's possible.
**Jason Plumb** 10:42 Okay.
**GZ Gregor Zeitlinger** 10:47 I think you cannot break the schema, because the model has getters and setters only for the things that can also be in in Yaml.
**Jason Plumb** 10:58 That's what I thought, too. But if you have access to like the raw nodes, or whatever I haven't, I haven't built a config customizer yet, so I'm not as familiar with the Api.
**GZ Gregor Zeitlinger** 11:11 I don't think so.
**Robert Niedziela** 11:12 Maybe I'm exaggerating a bit.
**Jason Plumb** 11:16 But in any case, I mean still validating like content. Seems like a pretty reasonable. Ask a pretty reasonable use case, but then I still have to think of like how like, what? What is the outcome of that validation failing?
And do you allow validator to to set a default.
you know? Is there like a fallback in the case of failure in some cases?
And then what do you do? Aside from logging, and how how helpful is that.
**Robert Niedziela** 11:46 How helpful is that is that I don't know, because the customers should say, if it's helpful for them. I'm just as you said, trying to replicate the previous behavior in a new configuration.
**Jason Plumb** 12:00 Right.
Which maybe it's maybe it's not necessary. I'm just. I'm supposing.
**Robert Niedziela** 12:15 Does anyone else see the need for it? Because maybe that's right. Maybe it's not necessary. Maybe we should. Just communicate that we are no longer supporting this thing, or or report it from somewhere else.
But anyway, there is no good place. If we would like to do this kind of warning.
There is no good place for it right now.
**GZ Gregor Zeitlinger** 12:42 So I'm still at one step before I'm wondering what the desired outcome is if there is some configuration that doesn't make sense, should the application.
or the observer or the Java agent just stop working and do nothing, so no observability at all.
Or do you want to have a degraded version.
I think if that the Login question comes later, at least for my understanding.
**Robert Niedziela** 13:16 So. So I think it depends on the failure. Right? Does it make sense to have the great degraded observability? If you, if your endpoints are not working right. They are.
I don't know.
Incorrectly created, or just in existing.
**Trask** 13:43 Right, Robert, in the current config customize declarative config customizer.
I thought that that allowed you to except the declarative config and modify it and spit out. Another version is that, am I remembering that right?
**GZ Gregor Zeitlinger** 14:06 Yeah, that's true.
**Trask** 14:09 So, could you? I mean, would that wouldn't you be able to read through if you wanted to validate some stuff at that point?
**Robert Niedziela** 14:20 Yes, the issue with this approach, or maybe it's not the issue, but it it has to be run at the end of all the customizers, so the order number would be some. I don't know, Maxine, or something like that, right to make sure that that everything else was already run.
because you know, you can. You can update one property in multiple customizers, and you don't know what you. You have to have the final state right?
**Trask** 14:51 I see. So you're what you're asking is, should we add a a separate validator step that would allow.
**Robert Niedziela** 15:02 That's what I mean. Yes.
**Trask** 15:03 Sure.
**Robert Niedziela** 15:04 Another spi or something like that. If if you think it's useful, because if it's not useful, yeah, there is no point to. Do do this.
**Trask** 15:20 I'm trying to think of what we do in our distro as far as validating.
I mean, since everything is sort of.
I think, with just property by property, as we check phase as we use things.
There's not sort of an overall like this global like.
Everything all together.
Validation.
**Robert Niedziela** 15:55 So I'll give you a specific example. Why, why, it could be needed for us. So the service name basically validation that is put as a property of resource.
and the resource is with declarative config, the full, fully initialized resource is put as as a shared state in the providers that I have no access to to the internals of this right.
It can be validated in in some agent listener, for example, at point where the the agents started. It's configured right? It's it's still early in the Runtime but with the way, how resource is constructed with declarative config. There is no. This data available for me.
The resource that is input as a root of auto configure open telemetry. SDK is just default, empty resource that the real resources are buried inside some internal data that I have no access to.
**Trask** 17:09 I see. And you wanna log you wanna log a warning to the user saying, Hey, you didn't set any service name here. You're gonna get some weird results.
**Robert Niedziela** 17:19 That's the point.
**GZ Gregor Zeitlinger** 17:30 And let's try to keep this resource question out of the general question, at least that that I think we should solve first.st Do you want to warn? Or do you want to stop everything.
**Robert Niedziela** 17:47 Hard is enough.
Word is enough.
**GZ Gregor Zeitlinger** 17:53 And if if you currently log a warning, is that not like good enough, does it? Do you want to have all the warnings in one place, so that it's easier for the.
**Robert Niedziela** 18:04 No, I just.
**GZ Gregor Zeitlinger** 18:05 Fine.
**Robert Niedziela** 18:05 I just. I just thought that it may be useful for some other things as well to have some dedicated framework for making any validations we we may need.
**GZ Gregor Zeitlinger** 18:17 Right, I'm thinking, how is it consumed? Is it still a lock message? And maybe in as a Json log, or something that can be more easily consumed.
**Robert Niedziela** 18:27 I think it. It's it doesn't matter much. It it was logger log to the output.
**GZ Gregor Zeitlinger** 18:34 Okay, got it?
**Trask** 18:39 Robert. It's probably worth opening a issue, either in the Java repo, or potentially even configuration repo, like to ask cause. I I don't remember, if the configuration spec is defined, this like customizer concept or not.
But it sounds like something that would be worth if we're going to do it.
Do it consistently across languages?
And I would mention the fallback, which I mean sounds like a reasonable today, where you can add, you know, have a customizer just with the Max order.
so that it runs last.
**Robert Niedziela** 19:31 Yes, that's that's 1 workaround for this.
Yeah, but that that's not for not the I mean main purpose of customizers, right? So it's not not what it should be, I think.
**GZ Gregor Zeitlinger** 19:49 I'm also using the customizer in that way. So I think you're not the only one.
**Robert Niedziela** 19:53 System.
**Trask** 19:55 Yeah, I think even the yeah, even the current config properties customizer that we have. I think that we're probably doing some of that in there.
Yeah, I don't actually don't think it's the worst.
I I get your point, though. But I feel like that's should be a cross language decision.
Whether we're going to, you know, config, declarative config is going to have Yay validation step like that.
**Robert Niedziela** 20:34 Okay, I will make that and attempt to create this customizer with a high number. High order number for now, and the discussion May may be somewhere in in the background.
**Trask** 20:48 Okay.
**Robert Niedziela** 20:49 Yeah. Thanks for the tips.
**GZ Gregor Zeitlinger** 20:53 And Robert for the resource. I have just created an issue today, because I have also found that this is a problem. I will tag you there.
**Robert Niedziela** 21:03 Yeah, so there is my my Pr. Already on Java. Open telemetry repo. But Jack is on vacation. So you know it's it's not.
**GZ Gregor Zeitlinger** 21:17 Okay, but it.
**Robert Niedziela** 21:17 Not moving forward.
**GZ Gregor Zeitlinger** 21:23 And with that Pr, you're simply passing the resource.
**Robert Niedziela** 21:28 Okay, I called some factory to create a resource and put it instead of this empty one.
**GZ Gregor Zeitlinger** 21:45 All right.
Shall we move on.
**Robert Niedziela** 21:48 Yeah, thank you very much. I'm done.
**GZ Gregor Zeitlinger** 21:53 Hey? You're next.
**Jay DeLuca** 21:55 Yeah, I just wanted to not to put you on the spot, Jason, but I was just curious. If you have any high level you know, notes or findings from your experience with beaver. I'm just starting to kinda dig in and learn about it and potentially see if there's any ways. We can leverage it within. You know the instrumentation project. So just kinda wondering your thoughts.
**Jason Plumb** 22:17 No, no, I appreciate that. It's it's a it's a super interesting topic.
and so I think this is within the context of that Pr that I linked to here. Do you mind if I drive Gregor.
**GZ Gregor Zeitlinger** 22:30 Sure.
**Jason Plumb** 22:31 I'll just share a couple of things.
It might make things a little clearer. Okay, so this is the Pr that I think we're talking about, and for those that haven't reviewed it yet, because it's pretty sizable, we're introducing a new module and contrib. And it is called Ibm Mq. Metrics. And the context is, it allows it has a bunch of different ways of fetching internal operational metrics about the Ibm Mq. Itself.
So send a message. It's like a diagnostic request, and then you get back a response, and then it parses and turns that into open telemetry metrics which are not semantically conventioned. Right? So this is like a new thing, these these are not yet in simcom. So for the purpose of of this we created our own semantic conventions.
and Antoine did the lion's share of the work on this, so I don't. Wanna I don't wanna take credit where it's not due, like he, he definitely you know, defined a bunch of this stuff.
and I've just been helping helping out with that. So from an experience standpoint, I didn't start with a blank slate. I started with something that was like pretty well established.
I probably need to go here instead. Right? Is this the correct place? Nope?
Oh, there's a registry right somewhere.
**Jay DeLuca** 23:50 Think it's in the model folder.
**Jason Plumb** 23:53 There's so much there's so much stuff here.
Model not marked.
**Jay DeLuca** 23:58 I think it's even a step up. Maybe.
**Jason Plumb** 24:00 Yeah, I, I think you're right.
This, no, yeah. Model. Okay? So model metrics. Yeah, okay, so this is kind of like, the the weaver style definitions that exist in semantic conventions. And so we put all of these new metrics that we're creating into this new semantic conventions formatted styled file that weaver can understand. And then from this we do several things. In addition to generating these Markdown files that can be used as documentation, readable human readable documentation to put in front of users. We also use it to generate some code.
Let me find that we have a couple of classes, and there was a there was a critique about their location. But I think it's let's see, I think it's yeah. So one, yeah. Yeah.
So metrics.
this is a purely auto auto generated class that we built with weaver. And I can show you kind of the weaver code down below that or the template that generates this. But basically Weaver reads in that big Yaml file of all of the different definitions. And then we have static factory methods here on this metrics class, and I think I think almost all of them are gauges, but I think there's 1 of them that's account. And so it's it's a pretty standard, pretty simple template to generate these.
But then we get this auto, like code generated class that we can then refer to in the rest of our in the rest of our code, and if and when a name of a metric changes, then we just regenerate this, and we don't have to go hunting in the code. So there's automation that can do some simple things. If we changed it to we change the type. That would be a a breaking change, right. We'd have code that breaks, but that's it would be very apparent when that happened, and fixing it is is not too bad. So want to come back to your question, though, like, what's the experience like? It's really it's really not that bad like, I feel like it's it's fairly straightforward. In fact, I shared your thing that you built around internally to some folks, including Antoine. And he was like, oh, that's awesome. Is that using Weaver like that? Was his very 1st question. And I was like, I think it is. And then you shared the code, and I was like, Oh, I think it's not which I think is maybe also why you're asking about this right.
**Jay DeLuca** 26:23 Yeah, I'm yeah. I'm I'm trying to. So I mean, I like, I see a couple of ways forward. And and some of this is is naive still, because I'm I'm still kind of learning. But like, I think that potentially.
you know, maybe there are areas for us to leverage something like this, although we don't. We don't write a ton of metrics in the agent that I've seen but but like maybe we could, you know, for our experimental attributes. We could create registries. The code generation is interesting because the other thing that I was thinking is, we've been talking a lot about all the configurations. And now that we're mapping them with the the metadata files like we could potentially use the the stuff that I've been generating in in my format to then generate the weaver specific templates, and and maybe maybe we eventually abandon the stuff that I've been doing and just use it to kind of bootstrap the weaver configs. But And then, you know the the ability to like maybe hook up the live checker to analyze all the signals that I'm already intercepting and dumping from the tests and and things like that. But yeah, I'm still very much in the beginning of my weaver exploration. But I thought this was pretty. This looks pretty cool in terms of you're generating the metrics, the configurations, the attributes, and and things like that, although I.
**Jason Plumb** 27:46 I didn't.
**Jay DeLuca** 27:47 See explicitly. It looks like the the configurations like the metrics config. Is that all like implicit? I I didn't see like a configuration necessarily in a yaml file that that seemed to map to those as opposed to like. It just looks like, maybe, for every metric it just generates and is enabled.
you know, behind the scenes.
**Jason Plumb** 28:08 Yeah. So I think I think the idea was for users to be able to specify a configuration file to to turn off certain aspects of monitoring of Mq. Like this is is, I think, I think, the one we ship with here should be a superset as well.
Let's see, it's probably just config the yaml right?
Nope.
**Jay DeLuca** 28:34 Maybe I just missed it somewhere, but I didn't.
**Jason Plumb** 28:36 Or maybe we didn't. Maybe it's maybe it's missing like, maybe we didn't include that one.
**GZ Gregor Zeitlinger** 28:42 You have it. It's just Yml.
**Jason Plumb** 28:46 Ymo this one!
Now that's test.
**Jay DeLuca** 28:57 Test. Yeah.
**Jason Plumb** 28:58 Go. I'm just past it.
Where is it?
Is it in something that collapsed.
**GZ Gregor Zeitlinger** 29:11 I thought you mean the test one.
**Jason Plumb** 29:15 No, there, there should be one. That's the real configuration for the application.
**Jay DeLuca** 29:20 Do you? These? These ginger files in this templates folder, these are generated by weaver, or you.
**Jason Plumb** 29:26 No, these are read by Weaver to create the out.
**Jay DeLuca** 29:29 Oh!
**Jason Plumb** 29:30 So weaver weaver sources these and applies them as a as a ginger template.
**Jay DeLuca** 29:35 Gotcha. Okay.
**Jason Plumb** 29:37 I will also share.
Yeah. So the idea, I think this test config at least demonstrate. So it we might be missing the real config that's like that seems like real feedback.
But the idea is being that with a yaml file you should be able to configure like the name of your queue, and, like some others, some other like connection, level information.
And then I think there's all of the enabled stuff here. Yeah, exactly so like, which go in this block, and if you enable it with true, that's where that can. That's where that Java configuration file is generated.
This one which says each of the features. And then there's, I think there's other stuff in here, too, but maybe not. It's just the is enabled right now, but that allows us, like programmatically to check if features are enabled to to turn on or off these different collector subsystems. But the thing I also wanted to share. I was doing some like side hacking and I will also send a link to this branch in my fork of the semantic conventions.
That is pretty basic. I was experimenting with Weaver here and saying, I just want to look at all of the metrics in the entire semantic conventions repository and generate this HTML file, and the script is pretty simple. This shows you how to run weaver through Docker.
And what I'm I'm just just touching metrics. And here's the really dumb guy, basic HTML, file, and I just generate like a card, I think, for each of them. And it looks, you know it looks like this.
None of this interactive stuff works at all. I have no Javascript in here yet, but the idea is that you could have like a searchable metric registry. I thought it'd be cool like if this could end up like even on the dock side, or something right?
**Jay DeLuca** 31:37 Right.
**Jason Plumb** 31:38 Where you could search. And then this is this was intended to be like categorization, or like maybe namespacing. But right now it's just a flat list. But if you wanted to see like I don't know like alright garbage collection, right like, here's the dot. Here's the definition of.net Gc. Garbage collection, and it gives you the type of instrument, and then the units. And whether or not it's stable. And then, you know, it's this is all pretty standard like we get a lot of this already in each of the different places. But I thought having like a 1 kind of combined registry, would be pretty fun. And so this is, I'm just sharing this like as another resource. If you're experimenting with Weaver and want another look at so cool.
**Jay DeLuca** 32:19 Yeah, because the the generating whether it's a markdown page or an HTML page. That's 1 of the other things I want to look at, too, as I know I was going to do, like a proof of concept of how we can use the metadata to now to now like, generate a read me essentially.
**Jason Plumb** 32:35 Yeah.
**Jay DeLuca** 32:36 It sounds like with the ginger templates and stuff. This weaver probably would work for something like that.
**Jason Plumb** 32:42 Totally. Yeah. There, I mean, of course, there's a learning curve on the semantics of like this stuff, you know. And how do you loop. Well, there's a way to loop, and there's the way to do conditionals. And you know there's all kinds of like string replacement, splitting reject stuff.
and it. You know it. Sky's the limit, and it's just a matter of time and and learning it. I I'm not an expert by any means.
But okay, think we hit the end of that.
Does anybody else have any questions about weaver stuff? I'm happy to to talk more about that. I don't. I'm not. I'm also again not on a weaver expert. I just know that it can take some structured yaml and fill out a template.
**Trask** 33:26 The other piece that would be interesting to look at. Jay is the Schema. V. 2.
Time, which is work being done by the weaver folks as well.
And I haven't been following it, and I don't so like there's the semantic conventions right where, like we have a Http spam.
and we've got these optional attributes, these recommended attributes, etc.
But then there's like specifically what a given instrumentation sends.
And I don't really know if that's I mean, maybe Schema v. 2 is just essentially the Yaml what's encoded in the Yaml already?
And we could have. We definitely could have Yaml definitions for each instrumentation spans that essentially like extend. If you've seen in semantic conventions, you can have things that extend other things so like you could extend. You know the Http client span, and then refine attributes or add attributes.
But I would look at what the scheme of E. 2 is, and if that's at all relevant here.
**Jay DeLuca** 34:58 When you say schema. V. 2. Are you talking about the telemetry schema?
Or is it different?
**Trask** 35:08 Yeah, yes, yes, it is telemetry schema.
We add, schema. v. 1 is those the schema files in semantic conventions that but all they are is their dips from the last version.
They're like transform. So it's supposed to be for being able to automatically transform one schema version time can't remember, never really took took flight. And so the Schema v. 2, isn't going to be. It's not only diffs, it will be a real schema like you would expect from a database schema describing everything.
There's a spec issue that Josh Surath opened a few months ago. About it.
but I haven't been following it beyond that.
**Jay DeLuca** 36:12 Well, I'll take a look. Yeah, I found I found the in the spec there was like an otep, for like the vision and roadmap for telemetry schemas.
but I didn't see anything that was more defined than that. But I'll I'll take a look again. Maybe maybe I just missed it.
**Trask** 36:30 Is that a recent? Is that a recent Otep, or is that the old?
Years ago Otep 1st Chemo b, 1.
**Jay DeLuca** 36:39 This was a more recent. I think this was like 2 or 3 months old.
**Trask** 36:44 Oh, perfect. Yeah, yeah, yeah. That's the work.
**Jason Plumb** 36:49 I dropped a link to an issue in the Weaver Repo that's called Schema, v. 2. Proposal from Libmilla as well, and that has a lot of text in it.
**Jay DeLuca** 36:57 Oh, yeah, I hadn't seen this one great. Thank you.
Cool. Yeah. And I'm gonna I I meant to. I wanted to go this week. But I I had a conflict. But I'm gonna go next week and and kind of break the ice there, too, and and talk to the the Weaver group specifically see what their their initial thoughts are, if they have ideas of of where to to start, and all that. But.
**Trask** 37:21 Awesome.
**Jay DeLuca** 37:26 Cool. I think that's all I had for for that topic.
**Jason Plumb** 37:30 We hit the end of our agenda.
**Jay DeLuca** 37:41 I mean, I have one more just kind of thing. Oh, go ahead.
**Jason Plumb** 37:50 Yeah.
**Jay DeLuca** 37:50 Go ahead! Trust.
**Jason Plumb** 37:55 He's driving.
**Jay DeLuca** 37:58 Alright. Well, what I was gonna say is, I opened an issue for this, but I just I'll just throw it out here, just in case anybody has an initial thought. But as I've been working through the the metadata for the different modules, one of the things that I've encountered is there? Seems like I've tried to classify them a little bit. I think I started with.
There's like internal instrumentations that are used for, like within the agent there are custom instrumentations which are used for generating custom telemetries like the the annotations, the methods, things like that with the library instrumentations. And now I'm realizing that some of the library instrumentations they don't necessarily generate telemetry on their own like, there's a pretty significant amount of them. They essentially, you know what I've been referring to as enriching other instrumentations. And so I was gonna add another category, essentially for these enrichers.
but I just wanted to. You know, it's that seems to make sense to me. That does that not make sense to anyone else, or and and the the benefit of categorizing them differently is essentially, we can generate a different type of documentation like for for most of them that I've seen, they basically are optional like they're not on, they're not enabled by default, and then they usually add, like the experimental attributes for a particular library or or vendor, or something. But yeah. So so my thought was to to categorize them as enrichers. But.
**Trask** 39:33 2 categories that jump to mind are context propagation, like ones that are just helping with, you know, propagating context across Async or frameworks and threads.
And then we've got a lot that do the route thing. The Http route.
Are there other?
What other kinds of stuff are you running across.
**Jay DeLuca** 40:08 I think the the Http route is the most common that I've seen but then there's other ones for like spring, for like spring jobs. And I'm trying to think maybe that was a different one. But yeah, I think majority of the ones that I saw were were things related to either Http server routes.
or I'd have to think about the examples of the other ones that were just for kind of like library specific attributes.
**Lauri Tulmin** 40:39 Won't there be instrumentations that fall into multiple categories.
**Jay DeLuca** 40:46 Yeah, that's another good point.
**Jason Plumb** 40:54 Are there some that only serve to bridge like logging? Mdc.
**Jay DeLuca** 41:07 Like the yeah, I I guess.
**Jason Plumb** 41:12 Like bridge some of the bridges. I don't know.
**Trask** 41:24 Right. Those don't actually create any telemetry. They just populate. Mdc, yeah, it's.
**Jason Plumb** 41:31 Yeah.
**Jay DeLuca** 41:37 I would consider the logging bridges to to be like an enricher.
**Jason Plumb** 41:42 Okay, I think that's fair.
And the stuff where we instrument the SDK, that you're considering that internal.
Yes, yeah.
**Trask** 42:00 And to Laurie's question about point about there being, you know, some apply to multiple categories like the A lot of the route instrumentation.
Also has the option to create an internal span.
so it it can enrich the parent. Its main purpose is to enrich the parent span, but can also produce its own span.
**Jay DeLuca** 42:30 Yep, like the is that the receive?
Or maybe that's something different.
**Trask** 42:39 Like Mv. Spring, Mvc.
Is kind of classic example at all. Yeah, the controller.
**Jay DeLuca** 42:47 And the views.
**Trask** 42:49 Yeah, yeah.
**Lauri Tulmin** 42:51 If you search for this Controller telemetry enabled option.
and you will find that there is a bunch of instrumentations that can that can create Controller telemetry that's disabled by default, but usually they work often. They also set the Http route for the parent span.
**Jay DeLuca** 43:17 And when those are disabled by default to Oh, go ahead.
**Trask** 43:23 Oh, go ahead!
**Jay DeLuca** 43:25 I was. Gonna say, do, and I can look into it. Never mind, I'll I'll look into it myself.
**Lauri Tulmin** 43:29 Only like creating the controller span is disabled by default.
These spirit stuff is enabled.
**Trask** 43:41 What's the jay? What's the benefit of having a single categorization versus multi, multiple like being able to tag an instrumentation with multiple categories.
**Jay DeLuca** 43:58 I don't. I don't think that there's a a downside to doing multiple. I just I just hadn't considered it the the like, the initial way that I've been using. It is essentially just in the instrumentation list. I I just display them differently in terms of the Associated information and I was thinking like for enrichers, instead of necessarily displaying, like a telemetry section with spans and metrics. It could just be like attributes or something, but it doesn't need to be that way. Like I could have.
I could come up with a different way to display the information based on which categories they fall into. So I I think I think one takeaway for me, for this is to rethink the way that I'm I'm handling the categorization and and to support multiple, because I think that totally makes sense. And I don't think it.
I don't think there's a downside to, even if I continue in the the way that I've been doing it now with like libraries, custom, and and whatever like, I could always have instrumentations I do to fall under both, or or come up with another way. So I think that's that's a good piece of feedback that I can take away and then I I can dig into this a little bit further and and try and hash out like the actual.
If there are problems with the implementation, or if there are other categories like, I think that the the context propagation one is interesting. So I can. I can go back, and I don't know if that would be separate from an enricher or whatever. But but yeah, I'll take this back to the drawing board and think about a little bit more.
**Trask** 45:31 Cool, I think, on the supported libraries page that we have in the repo we have, like Http route as a category there sort of. And I think context propagation as a category there when we display, like what it produces like. If it's Http client or server metrics.
**Jay DeLuca** 46:00 Oh, yeah, I do see that. Yeah. For like Apache, Petco is categorized as context propagation. Well, I hadn't. I hadn't noticed that.
**Trask** 46:10 Cool.
**Jay DeLuca** 46:19 Oh, thanks, guys! Appreciate all the the insights there.
**Jason Plumb** 46:32 All right until next time.
**Trask** 46:37 Thanks, huh!
**Jay DeLuca** 46:39 Have a good one.
**Robert Niedziela** 46:40 Pay.
**Trask** 46:41 Bye.
