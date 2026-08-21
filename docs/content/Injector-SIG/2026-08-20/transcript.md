SIG: Injector SIG
Date: 2026-08-20
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Bastian Krol (Dash0 Inc.)** 03:45 They are.
**Michele Mancioppi (Dash0 Inc.)** 03:48 Hello there.
**Bastian Krol (Dash0 Inc.)** 04:55 Hey, Jack, and Nikola?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 04:57 Aye.
**Bastian Krol (Dash0 Inc.)** 04:58 How are you doing?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 05:01 I'm alright, yourself?
**Bastian Krol (Dash0 Inc.)** 05:02 They are, same.
I… So, as far as I know, we don't have anything on the agenda yet.
We see general docs don't say.
Anyone… something I want to talk about.
**Michele Mancioppi (Dash0 Inc.)** 05:27 Let's, let's see if there are new issues and open PRs. I do a triage, right?
**Nikola Grcevski** 05:34 I haven't seen any come through, but maybe I'm just in my million notifications.
**Michele Mancioppi (Dash0 Inc.)** 05:39 I believe there isn't.
No, there are no new ones.
It's just good.
No, no new issues.
Nikola, since you're here, So, something that we've been discussing in the last couple of weeks.
Is, to add language to the, specification.
A telemetry for languages that are injectable.
And, I have not opened a PR on the specification yet, but it looks In my, in my, private fork.
And I would like you to have a good look at it.
**Nikola Grcevski** 06:31 Okay.
**Michele Mancioppi (Dash0 Inc.)** 06:33 I'll put it in the chat.
**Nikola Grcevski** 06:41 Is this going to be different than Telemetry SDK name? It will be telemetry language, or something?
What do you mean by language? Sorry, maybe I'm missing…
**Michele Mancioppi (Dash0 Inc.)** 06:54 When is an SDK and a set of instrumentations? What requirements do they need to fulfill to be injectable?
**Nikola Grcevski** 07:02 Okay, yeah, okay.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 07:04 We want to have a… we want to have an entry in the spec that describes the requirements, and then a row in the spec compliance matrix that check if your language meets all of these requirements, and so the spec and the compliance matrix… the compliance matrix provides, like, the incentive for maintainers to go do this, and the spec is sort of acts as the contract between language maintainers and injector and operator folks that want to leverage.
Those capabilities in a standard way.
**Michele Mancioppi (Dash0 Inc.)** 07:34 I had seen the chat.
**Nikola Grcevski** 07:36 Cool, thanks for opening that.
**Michele Mancioppi (Dash0 Inc.)** 07:38 Yeah, please look at it with both your language hat and OBI hat, because I would love it for that to be also something that OBI Sees itself into.
Because that is a form of automate… automatic injection. It's not something that the language does, Moriko BI does for the language.
But, in my head, OBI and the Injector, they fulfilled, effectively, the same need in different ways for different technologies.
**Nikola Grcevski** 08:10 Okay.
Yeah, I should probably… Yeah. Yeah, sounds good.
Yeah, I think I saw this come through on the… on the Slack channel, and I think I saw… Bastian adding some comments, but I didn't know how to add comments. I think I looked at it briefly, but then… My attention got… I got distracted.
**Bastian Krol (Dash0 Inc.)** 08:34 Yeah, I think this is just to comment in Slack, probably, because it's not a draft PR yet, so…
**Nikola Grcevski** 08:40 Yeah, yeah.
**Bastian Krol (Dash0 Inc.)** 08:41 landed on, and we keep it… we want to keep it short, I think, deliberately, so not go into all the details. Obi is an interesting angle here. I didn't even think at all about Obi when I looked at this. I'm not sure. How do you think would this relate to OBI? I mean…
**Michele Mancioppi (Dash0 Inc.)** 09:03 I mean, purely technically, with the, we would modify… so we would add the entry under the SDK.
And OBI is not exactly an SDK. It just does much.
**Bastian Krol (Dash0 Inc.)** 09:15 not.
**Michele Mancioppi (Dash0 Inc.)** 09:15 Most of the nodes do. The SDK does.
**Bastian Krol (Dash0 Inc.)** 09:18 Hmm.
But the language you used there does not really… target something like OBI, is my thinking, and then maybe that's…
**Nikola Grcevski** 09:28 No, probably not.
**Bastian Krol (Dash0 Inc.)** 09:29 Because it's a thing of its own. But, okay.
**Michele Mancioppi (Dash0 Inc.)** 09:32 No, I would just… so the, this is a springboard.
To actually start codifying more requirements about, not only if it's A language is injectable, but are the users going to have a good experience with that?
**Bastian Krol (Dash0 Inc.)** 09:48 Sure.
**Michele Mancioppi (Dash0 Inc.)** 09:49 Which brings us to another CPR on the specification. This one already came up in the maintainer call.
And it has APR.
Let me, find it, and that is to open up The allowed scope for the service resource detector.
And you find it in the chat.
The idea there is to open up the language of the spec so that languages and automatic instrumentations that do something more refined when looking out for service name, other than either auto service name is set, or I fall flat on my face with a known service.
Would you go and do framework and library-specific things.
And there, every maintainer plus one is gonna help.
**Nikola Grcevski** 10:47 That's interesting, that's, Okay.
Yeah, it's gonna be pretty cool, I mean… Actually, it's something I'm working on right now for OB.
Because, I mean, Java has… Razor detectors, but the other ones don't.
I mean, outside of Kubernetes Cloud, There is a…
**Michele Mancioppi (Dash0 Inc.)** 11:16 a tiny bit, a bit in PHP, a little bit in .NET, but most standard distros actually do have mechanisms to provide something smarter.
And I find it terrible, in terms of user experience, that one.
The resource detector called service is usually not the one that will set the service name.
And two, that, since, in the declarative configs.
The only resource detectors that are really taken care of are the four built-in ones.
And the thing with custom resource detection is autoing it on its ass.
And I cannot live with that.
Also antithetic to the idea of system packages, so that stuff should just give you a good experience, right?
**Nikola Grcevski** 12:09 Yeah.
Yeah, sure.
No, I don't have any. I've been… I was looking at Node.js and Python, and there's nothing in the… And, SDK that does any sort of attempt to name based on it, although Node.js and… Python do have standard ways of how Most frameworks encode this information.
They should do a better job rather than unknown service.
Yeah.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 12:42 I think the reason it probably doesn't get much attention is because there's just such a good name candidate when you're in a Kubernetes environment, and so…
**Nikola Grcevski** 12:49 Yeah.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 12:50 This is… this is only a problem when you're outside of Kubernetes.
**Nikola Grcevski** 12:55 No, Jack, half of our customers are non-crubernetes.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 12:58 Yeah, I know, but OpenTelemetry being cloud-native,
**Nikola Grcevski** 13:02 Yeah.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 13:03 you know, has a Kubernetes bend.
**Bastian Krol (Dash0 Inc.)** 13:07 Probably.
But I mean, in Node.js, that was also such a good candidate, like, just a name from the package JSON would be very good.
I want to do that.
**Nikola Grcevski** 13:15 It's an easy win, right?
**Bastian Krol (Dash0 Inc.)** 13:17 Yeah, yeah, yeah.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 13:18 Is it accessible, through the runtime?
**Bastian Krol (Dash0 Inc.)** 13:21 It depends. For most deployment approaches with Node.js, you just copy the whole thing, including the package JSON. You can theoretically build Node.js code in a way that the package JSON does not land in the final container, but that's a niche use case.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 13:40 You'll come.
**Bastian Krol (Dash0 Inc.)** 13:40 Very often, it is accessible.
Or you can do some… some more work to find the package JSON. It's also not always in the current WorkNet directory, but yeah, whatever.
**Michele Mancioppi (Dash0 Inc.)** 13:51 And if anything, I mean, we are talking about a series of smart fallbacks, yeah?
**Nikola Grcevski** 13:59 Yeah, yeah.
**Bastian Krol (Dash0 Inc.)** 13:59 I think one difficult question is if the 4-back is on different levels, like, if you have one level, one value on the Kubernetes level, and one inside the SDK in the container in the process, it's hard to differentiate and to decide what is the better default value to use, but…
**Michele Mancioppi (Dash0 Inc.)** 14:18 That is not a problem, because what we're talking about is the service detector is part of the default resource in pretty much any SDK that I know, and everything else overrides it.
If you go in the SDK, the trusted provider, and merge a resource to have some other resource type, which is what Java does with automatic, with the auto-configuration.
**Bastian Krol (Dash0 Inc.)** 14:42 But the problem still remains. If the, for example, the Kubernetes operator already said something, then the fallback in the SDK will never win, and maybe the value in the SDK would be the better one, but… But anyway, you can always As long as you can set something explicit, I think it's fine.
**Nikola Grcevski** 15:01 Yeah.
Yeah, we prefer Kubernetes, right? So Adobe is, like, you have the base, the SDK determined it from the language level, but then you have a higher Kubernetes, or Docker metadata, or cloud vendor metadata that's sort of overrides.
Sure. Yes, yeah.
But yeah, I think packet.json sometimes even have the version, and I was thinking also, like, there's… Scope, sometimes?
So they scoped the names, which… you can use the scope maybe as a namespace? I don't know, there's… There's a lot of value can be extracted from that.
From what's already in the package with the application?
**Michele Mancioppi (Dash0 Inc.)** 15:49 I, the first step for me would be to… Allow languages to be smarter?
Because right now, you violate the SPAC by doing something smarter, or you go and do something more. And then through that.
Then encourage the packages to actually go and do something better.
that… since I expect resistance, and there was, for example, from Jason.
The language currently is may do that. In my opinion, it should be should.
But… One step at a time.
You're muted, Jack.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 16:29 Jason pushed back, but, I think… I think he was sort of trying to channel the… what he thought the Java SIG would think, and so, like, I think if, if I expressed support of including that type of detection mechanism in the core SDK, he would… he would be okay with it, because, like, he was trying to just… Protect, me from additional maintenance burden.
Okay. But I'm okay with it.
**Michele Mancioppi (Dash0 Inc.)** 16:56 Then… go and vote.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 17:01 Yeah, I'll review your PR. I think it's the right thing to do.
**Michele Mancioppi (Dash0 Inc.)** 17:09 And then there is also some other work that is very relevant for us and the goals of the SIG.
Trask. Trask has made some wonderful things with the repository, for conformance of instrumentations in terms of semantic conventions.
In case, you folks missed it, let me… let me put it in the chat.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 17:31 Yeah, this, this is incredible.
**Michele Mancioppi (Dash0 Inc.)** 17:33 I love it. I cannot get enough of that trip.
It's actually something that, in the ZRA we wanted to do, as well. So the, Both Matt and Diego, they have the long-term goal of uplift the compliance of Contrib for the languages that they, they contribute to in terms of semantic convention compliance, because right now it's, It's a bit depressing.
**Diego Hurtado** 18:16 Yep, we're trying to put those semantic convention tests in the Yes, limitations as well, so that it fails.
RCI.
Second, we're not semantic.
conventions compliant.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 18:35 It's just such a good thing to, to add it to your build, because once there's a target to meet, it becomes such a trivial exercise to iteratively update all the instrumentation until you check all the boxes green.
**Diego Hurtado** 18:51 Yep.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 18:56 since we're in the, in the, you know, show-and-tell phase of this meeting, so, Michele, I don't know if you saw this… But, I have started work on tighter integration between semantic conventions and declarative configuration. Right now, it's like, the… it's… it's ad hoc, the, you know, the way that semantic conventions talks about configuration properties and how they manifest into the… the… declarative config JSON schema.
And, I want to tighten that relationship, so, like, semantic conventions defines, you know, data in their EAML data model, which describes which properties are configurable and exactly what their semantics are. And, you know, that is automatically and tightly integrated with the declarative config JSON schema.
And the reason that that's important is because once it's in semantic conventions, Weaver and all the CodeGen tools can start to, Build, you know, generated tooling to be able to, you know, read the expected configuration shape of semantic conventions on a particular version, and make it really easy to access that data for instrumentation libraries, so that, you know, it's something that people actually do.
And so, Lute Miller took what I did and expanded on it, and I want to show… share my screen real quick, because I think this will do… this will be better than words.
place. Alright, so… She's got this branch where she does things like, This is a branch within the semantic conventions repo, and she does things like this.
Within the… Where's the model?
within the model of any particular convention, like HTTP, See if I can open this.
You have, data structures that describe the configurable properties, and this is sort of like a, a sort of mangled version of JSON schema with the intent that it is compiled to valid schema later, but it's, you know, there's extra keywords and extra structure to help people You know, define these properties with more rails.
And so this says, like, hey, Many times, there… many of the conventions that reference HTTP request method will have a property called… a config property called known methods. There's, like, an environment variable equivalent. It's, you know, it's a… it's a value filter property, and Loudmella has this, this closed set of the different types of configuration properties based on the common things you want to be able to do in semantic conventions. The fallback is defined, the description is defined, and all of this is bundled up and spit out into… this intermediary… intermediate representation. These are… this is the same type of YAML that appears in the declarative config repository. So, the… the data we were seeing before sort of manifests as these type definitions, declarative… or JSON schema type definitions and properties. This is… this is getting closer to proper JSON schema.
And then she went all the way and showed how, like, code generation could work with this stuff. So, you know, embedded in here is, like, a checked-out version of our generated code for, for Java, which we generate from semantic conventions. And so we have things like, You know, this would be an example of the type of thing that you can generate, And this is basically an instrumentation API that is, you know, will produce perfectly conformant HTTP client spans. And so, you know, when you start a span, and I think the ergonomics of this might shift, but basically, when you start a span, you pass it a tracer, you pass it, you know, config.
And, you know, the other things that are required at span start time, and it will automatically read all of the relevant config properties.
for HTTP client spans, apply those constraints automatically, and, you know, based on the other data you provided, you know, produce a span that is perfectly shaped, like an HTTP client span, in order to conform.
So, you know, There's generated, span instrumentation tooling, there's generated metric instrumentation tooling, and it all sort of falls out on what you would expect. Basic ideas, like, hey, the inputs are, you know, the caller needs to extract data from whatever library they're instrumenting, and, you know, call this generated code with config, plus the extracted data.
Plus a tracer or a meter, and out comes perfectly conformant, instrumentation calls.
So,
**Michele Mancioppi (Dash0 Inc.)** 24:26 And this crawled up.
And show me the package for HTTP attributes.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 24:35 This is what's here today. This is just a big registry of all the, like, constants that are, all the attributes in the semantic conventions related to HTTP.
**Michele Mancioppi (Dash0 Inc.)** 24:47 Alright, then I must have misread the code, and please open the client span again.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 24:56 So this is the part that, you know, does automatic application of the config based on, whatever the user configured. So it's saying, like, hey, record HTTP request method, apply the bounds.
**Michele Mancioppi (Dash0 Inc.)** 25:08 How is that not instrumentation dependent?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 25:13 This part, the filter HTTP request method.
**Michele Mancioppi (Dash0 Inc.)** 25:17 Yeah.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 25:19 So, what the whole point of this is, like, you know, coming up with certain config properties that are general purpose, so we want them to apply to all HTTP clients, all HTTP servers. And, you know, the thing that's instrumentation dependent is, like, the instrumentation needs to, the HTTP… the request method that it extracted from, you know, whatever… whatever types exist in the library, and then… but at that point, you can generically apply the filter.
**Michele Mancioppi (Dash0 Inc.)** 25:51 Now I understand the surface. Makes sense.
That's cool.
**Nikola Grcevski** 25:56 All these files are generated?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 25:58 All these files are generated from semantic conventions Data Model.
**Nikola Grcevski** 26:01 Wow.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 26:02 And you could go a lot further than this. This is just, like, sketching out the idea, but you could optimize this a lot.
**Michele Mancioppi (Dash0 Inc.)** 26:10 Effectively, with these files, we end up hollowing out 60% of an instrumentation.
by reusing all the facilities that already exist, because, like, when you look at 5 different instrumentations for HTTP, They're all more or less setting the same attributes with different levels of completeness, and then there is the very complex speed of where you hook in the instrumentation and where you find a particular piece of data that is specific to the client library and the client version. And this is factoring out all the common logic I'm putting it on the side. A very, a very small remark, I do not believe the signature Make sense?
Because, you are going to find… that, There is a surprising variability in terms of which framework and library can give you what.
For example, if you opened… the clients is relatively uncontroversial, although here is missing the URL template, which sometimes we have, and it's really cool to have. Open the DCP server span one, I want to see if you have the route.
No, you don't.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 27:26 The route, I think the idea is that that is not required at span start, probably.
And then there's probably a method that you can use later to add it, is my guess.
**Michele Mancioppi (Dash0 Inc.)** 27:43 the, from the… now, I like the idea, I'm just going into the nits straight away, because I don't have anything to object to the main idea. I mean, there is a matter about consistency across languages, we're gonna get to that.
Probably a builder pattern is gonna work better.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 28:00 Yep. Yep.
I guess it depends. Like, on the span start, certain things are required, and the builder pattern is bad at forcing you to provide things.
So, you know, having a contract where, you know, you can say, like, hey, these are all the arguments that are required, and if you don't… if you don't provide them, you're getting a compile time error. That's… that's a nice feature.
**Michele Mancioppi (Dash0 Inc.)** 28:24 Yes, but I would… agree more if the typing was tighter. I mean, when you look at that, there's, like.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 28:33 Everything's a string, and so there's the ordering issue, yeah.
**Michele Mancioppi (Dash0 Inc.)** 28:36 Yeah.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 28:38 Yeah, I agree. So there's things to be improved, possibly, different shapes this could take, but, you know, the basic idea is that, for the show and tell purpose, is like, hey,
**Michele Mancioppi (Dash0 Inc.)** 28:50 you know.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 28:50 So, we're working, Lyudmila and I and Semantic Conventions folks are working on tighter integration between declarative config and semantic conventions, and we're working on generated code that makes it really easy for instrumentation to consume that general purpose instrumentation config and apply it.
To, to them, so that, you know, the dream at the end of the tunnel is, like.
Like, many, many or all instrumentations adhere to the same config scheme.
**Michele Mancioppi (Dash0 Inc.)** 29:21 Yep.
I… it's a… it's a great goal, great to… to work towards, too.
We are gonna have a, interesting migration experience.
Especially in languages like Python and .NET, where instrumentations tend to have a significant amount of parameters to be set as KW args in Python and stuff like that, but the goal is… Super noteworthy, yeah.
I like it.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 29:52 And going back to Trask's work with the conformance.
You know, part of conformance is like, hey, did you populate these attributes?
Part of the conformance is also, did you adhere to the expected configuration options, right? So those are new checkboxes next to each instrumentation. The checkbox is the incentive, and, you know, with incentives and AIs, you can very quickly, or more quickly than before, you know, spin up agents to go and check all the boxes and get you conformant across the board.
**Michele Mancioppi (Dash0 Inc.)** 30:23 Where would you put this in terms of the delivery channel? Because I will put it in API.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 30:32 the generated code, where would I put the generated code? So, I would keep it in the… we have a dedicated artifact right now, Semantic Conventions Java, which contains generated constants from the Semantic Conventions data model.
I would provide the accessors in there as well, because, like, you want the semantic conventions config to be versioned alongside other semantic conventions concepts. So, like, you know, if you… if you pin the semantic conventions 1.42, you know, you want to pin to those metric names, those attribute names, and those configuration properties and semantics. All of that is sort of, like, bundled together.
into a particular version of SEMCOM.
**Michele Mancioppi (Dash0 Inc.)** 31:10 The reason why my first instinct was to reach out to API is because this thing is equally useful to automatic instrumentations and native instrumentations.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 31:21 Right, and the semantic… the way we think about this semantic inventions Java artifact.
and I hope other languages are doing the same thing with their generated constants from semantic conventions, is, like, it's separate from the API, but it's at, like, the same level of abstraction. Like, if you depend on the API, you normally depend on the semantic conventions Java artifact as well. Those are just, like, you know, kind of go hand in hand without But, you know, still are decoupled so that you could use the API without those.
**Michele Mancioppi (Dash0 Inc.)** 31:51 purely technically, I think that what you did will force the semantic convention jar files in Java, but our language is the same, to depend on API.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 32:04 They already do.
**Michele Mancioppi (Dash0 Inc.)** 32:05 Alright, I do.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 32:06 Yeah, yeah, you can't, you know, the constants that we generate aren't strings, they're, like, attribute keys, which are types that are defined in the API, so that dependency is already there.
**Michele Mancioppi (Dash0 Inc.)** 32:16 Good, then there is absolutely no downside to any of this.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 32:20 Yeah, I think it's cool, and it seems like Ludmilla's interested, and that's what you need to get stuff done in OpenTelemetry, is to have Coalitions of people.
**Michele Mancioppi (Dash0 Inc.)** 32:32 It's really, really cool.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 32:33 Alright, we're out of time.
**Michele Mancioppi (Dash0 Inc.)** 32:37 Hi,
**Jack Berg (Raintank, Inc. – Grafana Labs)** 32:38 Take care, everyone.
**Michele Mancioppi (Dash0 Inc.)** 32:38 I think there is a significant amount of work in different directions that goes all in the scope of the SIG and packaging and automatic injection. It's nice to see. It's okay.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 32:51 Yeah, a lot of complimentary work.
See ya.
**Michele Mancioppi (Dash0 Inc.)** 32:55 I will be out the next, the next two SIG meetings. Do not have too much fun without them.
**Bastian Krol (Dash0 Inc.)** 33:02 Okay. I'll be honest.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 33:03 as well, so…
**Nikola Grcevski** 33:05 We're gonna rewrite the project in Rust.
**Michele Mancioppi (Dash0 Inc.)** 33:08 Excellent.
That's exactly what I'm looking forward to.
**Bastian Krol (Dash0 Inc.)** 33:10 Okay. Bye.
**Michele Mancioppi (Dash0 Inc.)** 33:11 Why?
**Nikola Grcevski** 33:12 Bye.
**Bastian Krol (Dash0 Inc.)** 33:13 Bye.
