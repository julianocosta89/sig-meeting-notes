SIG: SIG Injector
Date: 2026-07-02
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Michele Mancioppi** 01:45 Hello.
**Paulo Janotti** 01:53 Hi there.
**Michele Mancioppi** 01:54 Congratulations on your first merged PR!
**Paulo Janotti** 01:57 Alright.
**Bastian Krol** 01:59 They hired.
**Paulo Janotti** 01:59 Thanks for the quick review, and good improvement for the tests, also.
**Michele Mancioppi** 02:08 So, you're effectively understand that with that, you are unblocked, right?
**Paulo Janotti** 02:13 Yeah.
Yeah.
I'm unblocked now, I'm… I'm already have, a PR using, I was using from my branch, but I'm gonna switch to using from, the official branch. But it's… it's gonna be some time until we switch the official release.
And then I will… I will probably be into a tag, whenever a new release happens.
**Michele Mancioppi** 02:46 Wait a second.
Why do you care about releases?
**Paulo Janotti** 02:50 No, it's just kind of to… to have a pinhead for a specific tag, right? So, In that sense, we can, match the version of a release, you know? So, It's not a hard requirement, it's just how I envision my build, kind of. I'm tagging releases, so if there is an upgrade, a release, I check automatically my CI check, and I upgrade my build to match that release. That's…
**Bastian Krol** 03:30 So, if a release would help you, I mean, releases don't cost us anything, it's a click of a button if you're…
**Paulo Janotti** 03:39 Yo!
**Bastian Krol** 03:40 would, be easier for you with, with the release? We can just make one.
**Paulo Janotti** 03:46 Right now, I still have some, work to do on our side, so I probably need, like, one or two weeks to wrap that up.
And then, probably by then, yeah, and then if I… when I'm done with that work, a new release will be nice, just as a convenience, so I… I have a specific tag to match and keep falling from.
**Bastian Krol** 04:12 Yeah.
Yeah, that makes sense. And just, just… Ping, ping us, I mean, probably we'll have a release out by then anyway, but if not, we can just build one.
**Paulo Janotti** 04:25 Sounds good. Thanks, everyone, that, discussion two weeks ago, and the PR. Thank you, everyone.
**atoulme** 04:32 Hey, Pollo.
**Bastian Krol** 04:33 Thanks for contributing that.
**atoulme** 04:36 Paul, I had a question for you. It's somewhat related to this, and we just had a question about that in PackagingSeek, so… while I… you're here.
Do you still have a foot in .NET land, do you?
**Paulo Janotti** 04:51 Yeah, you can say that. You can say that.
I, I have contacts.
**atoulme** 04:57 You know people. Do you know… I'm asking Pyoto right now, but I'm also a CCD on that thread. I was wondering, where are we with declarative config support for .NET? And… Could we have it so that we would be able to have the injector support that, so that we'd have a good, nice story?
To do, some sort of a packaging.
That would work for everybody here with declarative config from the get-go.
Do you know that?
If you don't let…
**Paulo Janotti** 05:28 Yeah, then I'm… I'm… I'm too out of their… their SIG status for too long to be able to, kind of, I, I… I can… I can certainly, intermediate the work. I just need to understand what we need on one side, and, then I can intermediate, and the background of .NET will help on that, so…
**atoulme** 05:57 Okay.
Yeah, so you're in the discussion with Pillar, we'll see what he says. I think he's just reviewed the latest proposal, which is 6,000 lines long, so it's not a small PR.
So Yeah, we'll see. I just want to get a feel for, like, is it, like, 3 months, or is it 2 weeks, or is it a month of work, to get us to a point where we could work with that. And that would unblock all the packaging effort to just use declarative configs for everything that we're doing.
Which would make Life so much easier, because we… otherwise, packaging has to choose between environment variables or declarative config as a way to do things.
**Michele Mancioppi** 06:41 Let me, let me, lay down so also Jack is, is updated.
So, hit a snack in the packaging POC.
the, since most SDKs are… sorry, heavy SDK except Java.
that you want to support, which means Java.NET, Node, and Python as the first drop of languages.
Does not support the language-specific overrides.
for instrumentations.
instrumentation configuration.
Then, we need… different paths.
The problem is, different files means that the injector needs to inject different values for auto underscore config underscore file.
An injector cannot.
**atoulme** 07:29 Intact.
**Michele Mancioppi** 07:30 Doesn't know how to inject different values for an environment variable depending on the language it injects, because the injector does not know which language it injects.
Which means that either… we have the SDKs implement, Those, the proper full decorative SDK, which… Most tools.NET, not yet.
plus the experimental override… the experimental overrides for languages, which, in the process, they also can become stable. For now, if I recall correctly, they're experimental because only one SDK has implemented instead of three.
Which is the minimum.
So, either we manage to get the SDKs to implement the clarity configuration and the staffing it we need.
And then we can go with a better solution, so the users having only one file to edit, and have a good experience.
Or, we need to move away from the time being, for the declarative configuration, and instead make the configurations for system packages be based on environment variables, like auto underscore endpoint underscore something.
Which is not a great experience.
**jberg** 08:48 Let me jump in. So, two languages support, instrumentation config, PHP and Java, and, someone was mentioning that… to me recently that they were… Diego was mentioning recently that he was working on implementing it in Python, so we're getting close to, having… meeting the three languages requirement for stability. That doesn't solve our problem.
In the injector, because that would only be, like, two of the languages out of the… What is it, 4 or 5 that we care about from the injector's standpoint?
**Michele Mancioppi** 09:26 Bart, but, Matt?
Where I can work on the JavaScript one.
**jberg** 09:32 Cool.
**Michele Mancioppi** 09:33 And, that brings us to 3 of the 4 languages.
And .NET is the odd one out.
**jberg** 09:39 And so, speaking of… speaking of JavaScript really quickly, I know Marilia is really interested in advancing and maturing declarative config in JavaScript, so that's always good, right? When two people, especially from different employers, are, you know, both interested in, you know, seeing something move forward, then they can, like, sort of partner up and look at each other's work and get it approved and merged. So, JavaScript has a good path, that's good.
NET. So.NET's an interesting situation. I linked to this issue, in configuration, in the OpenTelemetry configuration repo. If you just, like.
if you, like, go ask the .NET folks, they'll say, declarative config isn't implemented. And that's true at the SDK level, like, but the .NET auto instrumentation has had declarative config, and it supports the 1.0 version of the schema. And that's what we care about from the injector standpoint, is .NET auto instrumentation.
And so, the story there is actually better than you would… than you would expect if you go look in OpenTelemetry.net and search for declarative config and find this issue that's, like, you know, still outstanding.
So, yeah, it's available. They do support, instrumentation config, but, like, in sort of an unexpected way. And I think… Yeah, there's more standardization that needs to take place around how you configure instrumentation.
you know, it's experimental in the config… in the declarative config schema, and, you know, I think… I think that experimental status is… is, like, plays out in practice, because people are running in different directions with it. And, you know, what that means for me is, like, I think that the injector needs to be able to plan on some sort of mechanism to have language-specific configuration files.
I don't… I think… I think this idea that, you know, you can have one configuration file that applies to all of your languages. It's, like, a nice aspirational thing, but I think in practice, there's going to be subtle differences for what you want to do for .NET versus Java versus, like, Python, and, you know, we're going to have to reflect that. And, you know, maybe someday we'll get to the point where you can have, like, one configuration file for all your languages, but You know, for now, we have to… we have to be practical.
**Paulo Janotti** 12:06 I…
**Michele Mancioppi** 12:06 That means a cheery guacamole of, Making heuristics to detect yet another build of Node.js.
**jberg** 12:17 Sorry, I didn't understand where.
**Bastian Krol** 12:19 The technical difficulty with that is that the injector does not know, and until now doesn't care which language the process is that we are injecting in, and with probably only going to be guesswork, at best, that we can do. That's the problem why we don't want to have different config files per language.
**jberg** 12:45 Right, right, right.
**Michele Mancioppi** 12:47 I mean, I'm pretty confident that we can nail the JVMs, because the builds are relatively standard, and, even with the needed symbols, we can tell the leap, there is a leap for some stuff that only Java has.
**jberg** 13:06 That is a good invariant to have, though. Like, the injector, it's nice to say that the injector is not aware of the language runtime, and, you know, we can't… we can't have logic that depends on knowing the language runtime.
**Bastian Krol** 13:19 Yeah, for now, I would keep that perspective, and keep that, standpoint, and not change that without very, very good reasons. So, if that wouldn't be the case, I would agree, yeah, let's just have different configuration files per language, because it's easier to maintain, but that technical Limitation is quite real, and that's hard to work around.
**jberg** 13:48 So, declarative config does have facilities to, you know, in a single file, have, you know, configuration for Java versus Python versus .NET, so…
**Bastian Krol** 13:57 I think only for the instrumentation… Yeah, only for instrument, right?
**jberg** 14:01 Exactly, exactly. And the stuff that is an instrumentation, though, should be standardized.
And if it's not, then we gotta update the schema and, you know, capture whatever parameters people are trying to configure that aren't represented.
So I think that's good, and maybe… maybe the lesson for me, and maybe us, but just for me, is that if we… if we are forced to have a single file, a single configuration file, then that's, like, a forcing function to, like, make sure that all the languages interpret it in the same way, and that, like, you know, in a system where we have one file that is applied across all of the languages.
You can… you can do all the useful things that you need to be able to do.
**Michele Mancioppi** 14:45 For the user, it is possible to opt into different configuration files, but then it has to be on a process-by-process basis.
setting the auto config file in their SystemD unit, so that would be kind of manual overrides to be done only in the most specific of circumstances.
I don't want to have the user have to set up environments for injection to work.
**jberg** 15:18 Good job.
**Michele Mancioppi** 15:21 So these are the options that you need implemented across languages.
The… in reality, when you look, I mean, the schema is… Cheap and cheerful, just says, you have additional properties, yo.
That's, that's fine.
As far as I can tell, but .
**jberg** 15:43 Yeah, the point of that is, you know, within each language.
You know, we expect, there to be a mapping of, you know, instrumentation libraries with their own schemas, and we're never going to define in a central place the schemas for those individual instrumentation libraries. It'll be like schema enforcement on read, when those libraries are reading out their properties.
Because we can't centralize this problem. And yeah, so that's what's captured here. It's just like, hey, each language is a mapping, where the keys are the, you know, identifiers for each instrumentation library, and the values are, you know, a mapping node as well for all the config for that instrumentation library.
**Bastian Krol** 16:28 What is with other attributes? Like, you can also set resource attributes and stuff like that. Is anything in there where we would foresee that we really want to have that differently per runtime?
**Michele Mancioppi** 16:43 The way that I understand it works, and Jack, let me take this as an opportunity to validate my understanding.
**jberg** 16:49 Yeah, please.
**Michele Mancioppi** 16:49 outside key-value pairs, this is the equivalent of all two resource attributes.
And there is an enumeration of resource detectors that are supposed to be implemented in every SDK, That you go and say, do it.
I have not figured out how to turn on language-specific resource detectors.
But I also didn't look very hard.
**jberg** 17:19 So, can you click on this link that I shared in the chat?
It's just, like, much easier to see So, backing up a bit, there's this thing in OpenTelemetry.io, which is like a type explorer for all the types in the declarative config schema, and it makes navigating and talking about this a lot easier. There's examples, there's, like, navigation between the… throughout the hierarchy of the different types. It's nice.
And so, like, down here, we're on the resource type, which you're talking about, and there's an example of this, right? So, you know, what you were referring to, Mikael, was this, the detectors, exactly. And so… there's 4 built-in detectors, container, host, process, service, and those are defined in the specification, and there's semantics, like, if you want to understand them, go look at the specification. There's nothing stopping you from having language-specific detectors that the language creates and names and supports. And so, like, let's say there is a special Java detector, like, that's the name of it. You would just reference that in this list alongside the other ones.
And I guess what's, like, undefined, Mikel, to your point, is, like, let's say you're using this in a cross-language context, and you want to, like, enable some Java-specific detectors, and some Python-specific detectors, and some node-specific detectors. Like, what happens when you reference a detector that, like, you know, exists in Java, but does not exist in Python? Like, do you fail… Do you fail fast, or do you fail gracefully?
And I don't think the semantics are defined for that. Like, hey, like, you know, all types in the schema have a description, and the descriptions include the semantics of, like, what to do when, for example, a value is included that is not recognized. And so, I think it's ambiguous right now, what the schema says about that situation, and To be flexible for this cross-language context, we could update that description and say, like, hey.
If a detector isn't, like, included, and it… if a language doesn't recognize a detector in this list, just, like, fail gracefully with a warning.
Versus, like… that's not even fail gracefully, just warn instead of erroring.
So that's something that we could do to accommodate that, Mikael.
**Michele Mancioppi** 19:41 That is something that I believe we should do, yes. The, In my head, the detectors that are the most important are the cloud-specific ones.
**jberg** 19:53 Yeah.
**Michele Mancioppi** 19:54 How do I detect EC, that I'm on EC2, that I'm on GCE, whatever?
Those exist reasonably consistently across SDKs. The names are not always very consistent, but okay.
In terms of the packages on Linux, technically, what we could do is to rely on the, on the, tell people to install the collector, and then do resource enrichment through that.
But… If we could have the lucrative config that can work reliably also versus detection of the different languages, with semantics and everything, that would be totally superior as an option.
**jberg** 20:37 So I think what you're… what you're saying would be desirable, would be, like, if those cloud-specific detectors could be, like, formalized in a language-agnostic way?
**Michele Mancioppi** 20:47 There are two steps. One is to define the semantics of what happens if a language does not know that detector, and their feeling gracefully is correct.
**jberg** 20:57 Huh.
**Michele Mancioppi** 20:58 Painful, but correct.
what is… by the way, the same should happen with the instrumentations. If that's semantic… like, if you don't recognize the instrumentation, please don't explode.
That would have removed the dependency from, from, the experiment… those experimental flags.
The, I do believe that these four detectors do not go hard enough.
in terms of the specifications, I believe resource… The quality of resource metadata makes or breaks the usefulness of telemetry very often.
**jberg** 21:37 Yeah.
**Michele Mancioppi** 21:37 And we have been way too gingerly avoiding the topic of provider-specific settings.
In OpenTelemetry. To the extent that, for example, in Java, if I recall correctly, you need to go and add additional jars that requires incantations in terms of startup parameters.
to add your detectors to the Java agent.
It's…
**jberg** 21:59 Yeah, yeah, so you're saying, you're saying, the cloud, you know, provider-specific detectors.
are… it's… it's annoying, it's worse, it's like a bad UX that they're… that, like, you know, they're not part of the specification, they're not part of the declarative config schema, and that to use in something like the Java agent, you have to go and add an extension, property, so that you can reference one of these resource detectors for GCP, or Azure or AWS from the contribib rep repository, rather than it just being, like, you know, supported and sort of native.
**Michele Mancioppi** 22:36 That is precisely what I'm saying, yes.
**jberg** 22:38 Yeah, so, like, just some background. The reason I added these four detectors, was because we needed to get something, and, like, you know, I settled for good instead of perfect, because I would have never been able to get, like, consensus on landing all of the detectors that I think really ought to exist.
And so, like, you know, the dust has settled on these. People are, like, comfortable with these detectors now, and, like, the timing could be right to propose extending this set.
I know that there's people like Josh Sureth that are working on entities, and the entities' interaction with these detectors, and what… how I anticipate that working out is the different entities are going to be defined in semantic conventions.
And, like, I think, ultimately, there'll be a one-to-one relationship between entity and detector.
Right?
**Michele Mancioppi** 23:34 Nope. No? Okay. The same point is, these two.
**jberg** 23:40 Okay, why are those not one detector each?
Why are those not one entity each?
**Michele Mancioppi** 23:45 Because the process depends on the host ID. The identity of the process is the PID, plus the start time of the process, because PADs rotate, plus the host identifier.
**jberg** 23:57 So… so you're gonna… you're telling me that in semantic conventions right now, when they're talking about the process entity, they're saying that, like, the process entity is going to include host ID as one of its identifying attributes?
**Michele Mancioppi** 24:09 Yep. That's, how I understood it from the last time I attended the SEC, yes.
**jberg** 24:13 So that… I still don't think that that's necessarily, like, breaks what I said. That's just saying that host ID would show up in two different entities, in two different detectors. So the process detector would admit it, and the host detector would emit it.
And those IDs would agree with each other, though.
**Michele Mancioppi** 24:33 Maybe. There are… there are also… I'm sorry for being so pedantic, but… The, turns out that there is, no, commonly recognized algorithm to define who the hosted is.
**jberg** 24:47 Yeah, and I… look, that's not our place to get into, right? Like, we can't… we can't, you know, you know, go down that tangent rabbit hole down there. So, you know, I think what we can probably agree on is that, Entities are going to… I see entities as, like, the mechanism by which OpenTelemetry gets, like, more accepting and able to extend this set of detectors, right? There's four right now. Entities is codifying what the different detectors and what the shape of identifiers and descriptive attributes should be present on each of these. And, like, I want to see this set of detectors grow as The set of entities grows.
And then, you know, we can take this, like, practical, you know, step now, which is to go and adjust the semantics of the declarative config schema to say, like, hey, if you don't recognize one of these detectors in your list, emit a warning. Do not fail, you know, immediately, or fail violently, I should say.
**Michele Mancioppi** 25:51 I don't eat.
It's a good idea.
**jberg** 25:55 Yeah, and if you want to, you know, be the one to champion extending more detectors, you have my support.
**Michele Mancioppi** 26:03 I think.
**jberg** 26:04 Entities is gonna get in the way, but, like, you have my support to do it sooner.
**Michele Mancioppi** 26:08 I wish I would actually properly support their detectors.
that's not the case, to the extent where I'm wondering if we actually Should… Take some parts of the country back.
I'm looking at UAWS.
**jberg** 26:31 Nobody from AWS here to comment.
**Michele Mancioppi** 26:34 Novel of AWS is here to contribute to OpenTelemmetries, and so on.
**jberg** 26:39 Yes.
**Michele Mancioppi** 26:39 specific and pointed about that, AWS.
**jberg** 26:44 Are you hoping that their AI is listening to this conversation, and it's gonna get back to a product leader somewhere?
**Michele Mancioppi** 26:51 Yeah, either that, or Jeff sends me a dead foresad, either way.
Any sign of leaving on AWS in OpenTelemetry is welcome.
**jberg** 27:02 Yeah.
**atoulme** 27:05 Yeah, I mean… Yeah.
Entities will probably help a lot with clarifying what exactly we need, because if we have entities, do we agree we don't need to contribute? We need to be a bit lean about what we add to the detectors in that case, right? The data that we would add to the signals would just be the identifiable properties.
That would map to the entity. Is that… is that the correct assumption? Okay.
Well, in that case, I mean… I'm not gonna say it's solved, but there is an existing resource detection processor in the collector, and I think it could be a good way to model what data we need to provide, so that we can agree quickly on what type of attributes we want to add in the detectors, and make sure that we align that with what the collector's already doing.
**Michele Mancioppi** 27:56 Yeah, I mean, the host detection processor is roughly equivalent with, some of the better SDKs in terms of resource detection, at least in terms of infrastructure.
They never immersed my DigitalOcean PR, but that's a different problem.
**atoulme** 28:10 It's, We have a lot of stuff. The resource detection processor, at this point, is able to go, like, about a number of cloud providers, not just the DBS, but more obscure ones, and .
**Michele Mancioppi** 28:24 Does it mean that you are the person that didn't merge my DigitalOcean PR and one?
**atoulme** 28:29 I think someone… Did that, didn't… Didn't that happen?
**Michele Mancioppi** 28:32 I opened the PR and don't think it ever got merged.
**atoulme** 28:36 I think we have DigitalOcean support, we even have Hetner support.
Which is Elias. Really shows how much there is out there.
Let me see if it's there.
**Michele Mancioppi** 28:49 So, irrespective of the tangent.
**atoulme** 28:52 It is there, for what it's worth.
There's a dual ocean support.
**Michele Mancioppi** 28:57 the meat.
So, we have… In terms of resource detection, we have a few ways forward. The, by the way, the, these detectors and the one for the collector, they do not, alight each other.
I mean, the only situation where you have redundancy in terms of discovery is if you're running inside… well, host and container, there is some overlap. So, if you have these in the collector, and all your injected processes talk to the local collector, and the local collector is put in the resource detection… the host detection processor, and the rest.
On the pipelines, then these two are… Are, redundant, but these are always process-specific, so it doesn't matter.
That's fine.
Okay.
So, Jack, do you… how do we do the bit about specifying the These semantics here.
**jberg** 30:03 I got a… I got an issue open, or a note on my desk. I'll… I'll take care of that.
**Michele Mancioppi** 30:07 Cool.
**jberg** 30:08 So that's, like, a short-term one, or a short-term solution, and then, you know, hopefully long-term, all the languages converge on the same set of detector names.
**Michele Mancioppi** 30:20 Nice.
**jberg** 30:26 And I gotta run to the JavaSig, so everyone, nice to see you. Take care.
**atoulme** 30:30 Thanks so. Bye.
**Bastian Krol** 30:31 Mine.
Bye.
