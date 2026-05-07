SIG: JavaScript SIG
Date: 2026-05-06
Duration: 62 minutes
Zoom Recording URL: https://zoom.us/rec/share/-uUTZgLV8_csfPbFXDA2hM-vpGmt2P8EVgQq4Sc9hrqXRmk-UXeB1kSHolx7r80U.H6FpcYbd7JT5ZK6-
============================================================

## Zoom Recording Transcript

Marc Pichler (Dynatrace) 00:00:45 Hello.
Raphaël Thériault 00:00:47 Hulu.
Trent Mick 00:00:52 Yup.
Marc Pichler (Dynatrace) 00:01:51 Let's get started.
The first topic here on the agenda is… One that I put here, I just published this security advisory earlier. This is about the Prometheus Exporter, and… Yep.
It is vulnerable to, malformed HTTP requests like this, where, you might have a… URL that is not valid, and that crashes the app. We already have patched versions out for all the packages that depend on it as well. So… Updating, is the best course of action for this one.
Not exposing it, not exposing the endpoint to untrusted users is… Or is an option to just reduce the exposure, but actual mitigation can be found in these versions here.
So just so that everybody's aware, I also posted this to the Auto.js channel, And, yeah, if you have channels within your companies, please share the word.
So that we can get people to update as quickly as possible.
Alright.
Any questions?
Around this… If not, then we can move on to more security stuff.
while looking into this, I was… Thinking that it might be useful for us to define a threat model as a kind of an extension to our security policy, which should make it a bit easier for us to triage security advisories that are opened on our repos.
So, what I'm thinking is that we may want to define what defines a vulnerability, which actors we trust and we don't trust, and Yeah, just make it a bit easier this way, and give people a heads up on what to expect when they open an advisory.
I did open the draft here. This is mostly just a brain dump.
formatted nicely by an LLM.
It just essentially says, what, we don't consider, to be… Untrusted during, During any, advisory that's being opened. So, for example, environment variables, runtimes.
all of that stuff. It just gives some guidance on what to expect for people who are looking into these sorts of things.
And kind of define some of the boundaries between, what the user is responsible for and what we are responsible for as a project.
So the idea is here, to just… Provide a way for us to discuss I don't expect this to be merged in the form that it is in right now. It's very, very much a draft, so if anybody has any comments or ideas, I would very much appreciate that. Feel free to comment on the PR. We can also discuss here a little bit, if anybody has.
Some initial ideas here.
It is quite a bit of text, so, I don't expect anybody to… To read that quickly, Yep.
It's, mostly… concerning itself with, stuff like export destination. So if you have a push exporter that you should push Telemetry to untrusted destinations, because it discloses information about your app.
Stuff like that.
-Oh.
Spoon.
Also, the instrumented libraries.
And, how instrumentations what constitutes a vulnerability in an instrumentation deck?
For example, if something would crash anyway, and we are instrumenting that, End.
We take that info and, That… that crash occurs, then, yeah.
It… like, that the OpenTelemetry instrumentation didn't add anything to that, it was just an incidental thing. So there's quite a few of these, things that can happen, and it also defines, misuse of, open telemetry APIs when… users don't adhere to the contract laid out by the TypeScript types and the documentation and stuff like this. That's, like, not just the API, but also, the configuration of the SDK, that anything that's passed into the SDK as a configuration object is considered, trusted, and if anybody adds anything there, then, it's… it's not considered a vulnerability of OpenTelemetry, in my opinion. I guess in the future, it would also make sense to generally define this, not for just Oda.js, but for all OpenTelemetry SDKs, because I suppose everybody will run into similar Similar situations, because the concepts are shared across all language 6.
Daniel Dyla (Dynatrace) 00:08:33 I'll go through this in detail and add my thoughts. The only one that I can immediately think of that I think we might But I think my challenge is that export destinations are… trusted.
Particularly if you're going through any sort of proxy layer or anything like that, I think it's… I mean… Yes, they're ideally trusted destinations, but… If they're compromised in some way, you can imagine… You know, a SaaS… Telemetry backend that is compromised in some way.
If it could crash open telemetry clients, then potentially that's a massive… Expansion of the footprint of any sort of attack.
And we saw this recently with the possible resource exhaustion in the OTLP exporter.
not that anybody was actually… I think… Exploiting that.
But it's a potential, big expansion of that footprint, so I'm not… entirely sure that I agree with that point.
off the top of my head, I'd have to think about it a little bit more.
But I'll go through the PR and leave more detailed thoughts on it as well.
Marc Pichler (Dynatrace) 00:10:01 Thank you. Yeah, that was also one of the things that I wasn't really sure, when just drafting my bullet point list of ideas that I had. So I think it's good to discuss this a bit further.
I can see… The scenario that you pointed out being, actual problem, so… That should be a bit more nuanced there. I do agree that.
Alright.
Daniel Dyla (Dynatrace) 00:10:39 On one hand, it's trusted in the sense of, like, If you're sending… sensitive data. You obviously trusted.
Marc Pichler (Dynatrace) 00:10:48 doors.
Daniel Dyla (Dynatrace) 00:10:48 sensitive data.
But… do you trust it to then not crash you later? You know.
there's different.
Marc Pichler (Dynatrace) 00:10:55 Yeah.
Daniel Dyla (Dynatrace) 00:10:55 asses of vulnerability.
Marc Pichler (Dynatrace) 00:10:57 Yeah, I totally agree. There's, Different ways in which stuff can go wrong.
Yeah.
Daniel Dyla (Dynatrace) 00:11:06 Many, much ways.
Marc Pichler (Dynatrace) 00:11:07 Yeah.
All right, and I'd say let's continue the discussion on the PR. I'm also not entirely sure if, like, the document in the form, like, that it is in now with, like, a separate doc is the right way to go about it, but we can also discuss that there. This is, as I said, just the first Idea, and then we can iterate on that later on.
Alright.
Profile has… 1… Topic here is where for synchronous hooks.
Raphaël Thériault 00:11:53 Yeah, that are, like, I don't know if everyone's a little familiar with the new API.
For synchronous hooks, but it's RC now in node 26, and the previous ones are deprecated, so… Oh, we.
like, from the reply there, it looks like… I think it's like Datadog and Neuralink are using something else for their own instrumentations, but I don't think anyone here kind of wants to rewrite every single instrumentation that we have, so… We'll probably want to have support for them in import in the middle before they stop working.
The, the old ones.
Yeah, I don't… I don't think they plan to break… require monkey patching anytime in the future.
But, it also should work for require patching, the new API, given that it's synchronous. So there's also the possibility of kind of, like, merging the interfaces of both, import in the middle and require in the middle to use that.
Yeah, I kind of just wanted to… Bring it on the radar, and I don't know, if, like… they're, like, if the maintainers of import in the Middle don't really have an interest in updating it to support that, I, like, I'll probably do it at some point.
I don't know.
I don't really have any, like, well-formed thoughts on this yet.
Trent Mick 00:13:24 Thanks for bringing it up. I don't have well-formed thoughts yet, either. I don't… I'm one of the maintainers and important in the middle, so, I think… Probably this is a… a thing we did. Well, probably, definitely, I was gonna say in the same sentence, but I think this is a thing we do want import in the middle to be able to do, at least for Node 20… fixed, and forward.
It'll still support the older versions for quite a while, so… about merging import in the middle, required in the middle? Yeah, I don't have a… I don't have a solid feel for that yet.
need to play around with this more. I think we also do need to get into, for OpenTelemetry, looking at orchestrian for supporting… at least supporting that.
I agree with you that we're not gonna go rewrite all the instrumentations.
To just use Orchestrian, but curious if, New Relic and Datadog are gonna go that way.
Marc Pichler (Dynatrace) 00:14:31 Yeah, I think I agree that rewriting the instrumentations is probably way out of scope for us at the moment.
New ones, though, would be nice to get them to work with.
orchestrian lore.
duh.
Tracing gender stuff.
Sorry.
was kind of busy with other things for a bit, but I'll get back to my PR for context attached, detach.
We should help with that.
In the next few days.
Daniel Dyla (Dynatrace) 00:15:08 I think attach, detach… helps a lot with tracing channel instrumentation, and yeah, I've been looking into Orchestrian recently, and while rewriting all of our instrumentations is probably out of scope, rewriting a couple of the… you know, more finicky ones might be worth considering.
Marc Pichler (Dynatrace) 00:15:35 I think I agree. There's also… Yeah, I think having the support for synchronous hooks, though, in input in the middle would be very helpful, definitely.
just to be able to continue doing what we're doing now. I think there's also a bunch of third-party instrumentations that would appreciate us.
supporting this going forward, so… yeah.
There was one question, should it be enabled by default?
Raphaël Thériault 00:16:13 This was mostly, like, if that API gets from RC to stabilize, then it becomes kind of… The stable accepted way, too.
hook ESM, do we want to just enable it by default?
Marc Pichler (Dynatrace) 00:16:29 Yeah, I think we should at some point, do that by default. Especially getting instrumentation for ESM by default would be great.
way to alleviate some end-user pain. I know people are running into that all the time, that they have an ESM app that they are trying to instrument, and then… They don't add the hook, and are wondering where the telemetry is, or why they're only getting part of, Part of their, requests instrumented and stuff like that, so… Yep.
Yeah, that's the, thing. I think this one, we could look into.
Raphaël Thériault 00:17:27 I mean, I think at this point, we probably don't want to recommend it in the docs, given that it's deprecated, but…
Trent Mick 00:17:34 Well, it's only deprecated in 26 forward, right?
Raphaël Thériault 00:17:36 Yeah, that's fair.
Trent Mick 00:17:39 So, like, I think for Node… 22, 24 modules.registers better than the… requiring people to use the command line switch that experimental loader.
Which is a pain. But yeah, I mean, I feel bad I never got this.
Anywhere near over the line. Like, how old is this now?
Don't scroll to the top, but I want to know.
Yeah.
Marc Pichler (Dynatrace) 00:18:11 I'd probably do some sort of, like, a feature detection approach, where we detect which version of node we're running in.
Trent Mick 00:18:21 Yep.
So we get to have a fun world where we have require in the middle, import in the middle.
Using either of those techniques and orchestra instrumentations.
Marc Pichler (Dynatrace) 00:18:36 Use all the things.
Yeah.
Trent Mick 00:18:43 In one base class instrumentation that doesn't deny browser usage.
Marc Pichler (Dynatrace) 00:18:52 Yeah, so I guess the answer for this is, yes, we would want Kind of all of this.
Getting it to work would be… Amazing.
Raphaël Thériault 00:19:05 Yeah, I don't, like, have time right now, but probably sometime in the coming weeks, I'll… I'll look into it and open a PR.
Marc Pichler (Dynatrace) 00:19:16 Thank you.
Alright.
Any questions or comments around this topic here?
If not, then let's move on to the next one, or for reviews for…
David Luna Bistuer 00:19:40 Yeah, basically this is a PR to try to, Get rid of the noted list provider.
I know that the final picture should be to have a… SDK trace.
Period. Package, but this is the first step, so… Yeah, basically, we move away, all the imports from the SDK3s node.
Because we were not using the resistor method anymore, now with the basic provider, It's… it's enough.
Also, this PR, they basically introduced a new class, a trace a provider class, which is not resolving anything from the environment.
And the basic risk provider, it's wrapping, it's wrapping it, so… just for now, it's like, okay, we're still using basic test provider to just resolve Zero limits, sample limits… whatever, sampler or something like that from the environment, if necessary, and then pass it through the research provider, the simple to provide, I would say it that way, or… Or the pure one. I need to change this a lot of tests just to, switch from that. So, then the next step would be… to actually, move the logic of resolving configuration from the M in SDK node, and, and just, the basic trust provider.
Okay, so that's the first step of, I guess, another one or two pairs more to… To get, to get there.
Okay, bye.
Marc Pichler (Dynatrace) 00:21:21 Thank you for working on this, I know it's… quite a bit of stuff to change there. The node tracer provider, we've, we've used that everywhere, so…
David Luna Bistuer 00:21:32 Yeah.
Marc Pichler (Dynatrace) 00:21:32 Thanks for working on it.
David Luna Bistuer 00:21:37 Go have a look, give me your opinions and feedback, and… Hopefully we can get this, Moving and have something for June.
Thank you.
Marc Pichler (Dynatrace) 00:21:48 I'm about halfway through that PR for reviews, so I'm hoping to post it soon.
David Luna Bistuer 00:21:54 Thank you.
Marc Pichler (Dynatrace) 00:21:59 Alright.
Then I guess we can move on to the next one. This is a topic that Carlos put on here.
He has been reviewing some of the SDK logs.
Code for specification compliance, and Looks like he's been looking into… To log or configure it and stuff.
We may want to double-check that everything there is marked as experimental, on release.
Looks like the… Main things here are… Marked accordingly, but it's good to have an issue to double-check there.
Then there's… Loga and emittant and able to repeat filtering logic.
Configure it.
Trent Mick 00:23:25 That's possible, there is some rotation. Yeah.
Marc Pichler (Dynatrace) 00:23:27 There's a code there. Yeah.
Trent Mick 00:23:28 Right now.
I don't know if they could directly call it, but maybe, yeah.
Marc Pichler (Dynatrace) 00:23:37 I will actually add both of these to the milestone, sorry.
David Luna Bistuer 00:23:42 You can assign it to me, if you want, because I was the one that added the enabled API.
Awesome.
Marc Pichler (Dynatrace) 00:23:49 Thank you.
David Luna Bistuer 00:23:49 I'm familiar with the code, so maybe I can…
Marc Pichler (Dynatrace) 00:23:58 Thanks for picking that one up.
David Luna Bistuer 00:24:04 Folks.
Marc Pichler (Dynatrace) 00:24:06 API… this SDK, and then we also have… This one here, that's also added to the milestone.
source of locks SDK.
Alright.
I'm missing the export pipeline next, so that's probably coming up soon.
Let's look into the milestone real quick. There's… Probably some stuff in here… But no activity on the issues, so I guess this is still everything at the same point that we left it at.
I probably won't have time to look into the other ones, so if anybody is interested in picking one of these up… Like this one here, feel free to do so.
Alright.
It looks like we have… Only triage left.
Does anybody have any topics you would like to discuss?
Not terrible.
Trent Mick 00:25:50 socialize a thing, maybe this is mostly for Aurelia. I kind of want to drop model from all of the… Type names in the declarative configuration stuff, but… I'll write something up.
Marylia Gutierrez 00:26:03 But just keep config… because, yeah, the reason why I put it there was mostly because it's starting to get, like, conflict, so I want to be very obvious for that.
Class was coming from.
Trent Mick 00:26:17 Yep.
And, like, so an argument, so the top-level thing is called configuration model. The spec suggests or recommends using configuration for the thing, which is kind of nice, and it feels… I don't know, for… to me, batting around using the idea config… For the classes and configuration for the top-level type.
felt.
right. I realize this is just, subjective, but anyway.
Marylia Gutierrez 00:26:48 Yeah, it was even, like.
Trent Mick 00:26:49 I've met Mara before.
Marylia Gutierrez 00:26:51 Yeah, because if you even have, like, the how to start an SDK, it has the configuration for the startup SDK, so it's like, you have two configurations with the same name, so which one is what? So this is why, yeah, I was using the name, like, putting the model, so you know the source of each one.
Trent Mick 00:27:08 Yeah.
Yeah.
Yep.
I mean, with the model, it's certainly not a bad name. It's just… I wonder if I could make it shorter.
I did notice that, like, a lot of the… internal functions in the SDK for the create for the functionality for the create step to create SDK components from the config. A lot of those internal functions would be, like, do something from config, and from config, so people… it felt like the natural tendency of the developers working on those internal functions was to call one of these things, config.
Rather than a config model, for example. I don't know if that was just for brevity, and of course, brevity's fine for just internal methods and stuff.
Marylia Gutierrez 00:27:54 So, it was…
Trent Mick 00:27:55 Interesting.
Marylia Gutierrez 00:27:55 So it was on purpose, because, like.
you can have both your config file and your environment variable create a config model. So if I say config model, it comes from both… both of them. If I was saying just config, it's probably just from the file.
Was that the case? I know that I… there were some cases like this, but I might be… Mixing up stuff.
Because, yeah, a few places you have, like, from environment, and then a few from config.
Well, we should be config model on that case. I don't know, I need to look. There's too many configs. See? The names? Again, all of…
Trent Mick 00:28:39 I… whatever name we pick, there are gonna be some weird cases. So there's gonna be the type, or interface, experimental tracer, config, config.
I didn't stutter. Or experimental tracer, config, config model, so you have config in there twice, and I mean, that's… it's fine, you're following a pattern, so there'll be some weird stuff that happens regardless.
Marylia Gutierrez 00:29:01 rename everything to TBD, and just keep it forever as TBD.
Trent Mick 00:29:08 Sounds good. TBDE, yeah, development slash experimental.
Marylia Gutierrez 00:29:13 And final. No, this is the final. Okay, for real.
Trent Mick 00:29:16 Final feature, yeah.
Yeah.
on the… the SDK logs thing, Mark, there's still the… it's… hasn't changed, nothing's happened on it since the… The up-in-the-air question of extended attributes versus widening attributes.
Marc Pichler (Dynatrace) 00:29:37 Yeah, I did post a comment on the PR, I'm not sure if you've seen it. No, I…
Trent Mick 00:29:43 spectrum.
Marc Pichler (Dynatrace) 00:29:44 It wasn't that long ago, let's see…
Trent Mick 00:29:52 6579.
Second one there.
Marc Pichler (Dynatrace) 00:30:01 Oh, that's so…
Trent Mick 00:30:02 That's funny.
Marc Pichler (Dynatrace) 00:30:04 Yeah, it… I… initially thought that I would be able to come up with more.
Ways that it could be breaking, but… the more I tried to come up with, examples where it could be breaking, the more I realized that, like, all of these are essentially the same thing.
Just, like, manifesting itself in different ways.
So I think the main… Stuff that would break in this case would be something like this, where you do, you just check something, like, if it's Nile, if it's, like, any of these, and currently it, like.
We have an array type in there, so what you could do then, since it's narrowed to an array, you can do .filter.
And if that's an object, then in the future it could break.
and… TypeScript will complain about this in various ways, because… The type has suddenly expanded, and you can have… different versions of the same package installed in your app, and then, it might either crash during runtime, because you compiled with an old version of it.
Or it might… break during… Compile time.
Depending on, like, what the… Setup is on… of versions that you… have in there, and usually that shouldn't be a problem with SDK components, because they have this upper limit of, which API they should use, but instrumentations usually depend on the API package, since they just Consume it without implementing any of the types, except for the attribute type, which… Might be used in weird ways there.
Trent Mick 00:32:03 Okay, so I… I understand the description of the breakage.
skipping to the end of the debate, what I want is to not consider this a breakage, and I want to… I would like to be in a place where we can say, like, this was a type to describe I don't know, I can't even, like… Users shouldn't be doing this. They shouldn't be using the types from this imported package to be writing their own functions that are doing type narrowing on this thing for their own internal processing of these attributes.
So it, like, I want to argue that this is a stretch, and could be ignored as… Considered breaking, but…
Daniel Dyla (Dynatrace) 00:32:51 I also would argue that it's a stretch. I think it's a stretch, too. If you… If you're an SDK component, or you're writing a component that targets an SDK, like a spam processor, then… a new SDK version should… you have a maximum API version.
If you're writing an instrumentation that depends on the API, you're not… Processing these attributes anyways.
you're only sending them to the API, you can't read them from the API.
Marc Pichler (Dynatrace) 00:33:28 Yeah, so one of the things that I would… Counter that argument with is, These attribute hooks that we have.
Where… I'm not sure if there's any places where we pass in an actual function that takes attributes, or if you have something that's, like, a sanitization function.
for… Instrumentations.
That might be doing something like this.
I do agree that it's unlikely to happen.
I just feel like various versions of this might come up in end-user apps, because they… Decide they want to write something, and they construct an attributes, something that's of type attributes, and then they just modify that a little bit, and then pass it into the API based on, like, whatever they need.
Yeah, I… kind of agree that it is a stretch. I just wanted to bring it up that it is a possibility that people run into this.
Because in the past, we've seen that people run into every possible thing that they can possibly run into.
So, yeah.
Trent Mick 00:35:01 Say we said… we decided, this is a breaking change, we can't ever change the attributes type at all.
What is a path forward for, and what are the implications on… Supporting extended attributes anywhere.
in the API, like, can span.
that attribute.
Or… set attributes. Man, I don't even remember the name of the function. Can that… Continue to… be the same, or do we need a separate function, or does that thing just take attributes or work in attributes? Maybe that one's fine.
Marc Pichler (Dynatrace) 00:35:40 I think that one should be fine, since the contract for people that implement an SDK is different to the contract that… people that use the API, perf?
Yeah, I think so.
Daniel Dyla (Dynatrace) 00:35:58 out.
I think the… the way that I would solve that is… the SDK… Types… The SDK should vendor its own types.
But there should be a different… So right now, we tell anybody implementing exporters or spam processors or whatever to use the… attributes type from the API.
And we pass it all the way through.
If instead… we were exposing an attributes type from the SDK, We would be able to… make guarantees about that differently. Like, if you're on this version of the SDK, you're only receiving these things.
That would allow us to… Expand those types.
Separately. I guess it doesn't… because you have to expand both of them.
Nevermind.
Trent Mick 00:37:02 I might not be following exactly what you said, but I don't think our concern is for implementation of SDK components here. The only… Possible breaking concern is for… someone who's… for instrumentation authors, and also, from what Marco's saying, someone who's using an existing configuration… Option for an existing instrumentation?
I mean, all the instrumentations are 0.x, so for that second case, Mark, so if someone's using… you define, like, one of the… I think what you're referring to is one of the existing… Options for instrumentation where you can pass in a function, and that thing… Finn's attributes to… the user's provided function. That could break for them.
Do we consider that a… a problem, like, we… all instrumentations are 0.x, it could just be it's a… some breaking version of that instrumentation, where, like.
Marc Pichler (Dynatrace) 00:38:04 I think so.
Trent Mick 00:38:04 No.
Marc Pichler (Dynatrace) 00:38:06 I think for our instrumentations, it's likely fine, since everything is experimental.
There might be instrumentations in the wire that… onto that, but I'm… is one of those things where I'm not sure, like, how many of these are there. Do they even do something like that?
Is it a problem for them?
desire.
questions that exist, but I can't answer them at the moment.
Generally, I do agree it would be nice to just extend the attributes type, and… Be done with it, and possibly also say, Maybe, unknown is one of the possible types of an attribute, so that we can extend it later without running into this breaking change situation.
Got it.
So… In general, I think.
Daniel Dyla (Dynatrace) 00:39:12 If you… if you add unknown as a possible type.
That's the same as just saying the type is unknown.
Like, it… the union of unknown with any other type is unknown.
Marc Pichler (Dynatrace) 00:39:29 Yeah, it just would provide some rough guidance and ease. But other than that, you could still pass in whatever, we already need to do validation in the SDK, though, so I'm not sure if that is… a deal breaker.
Daniel Dyla (Dynatrace) 00:39:50 Yeah, I mean, what we could do is redefine the attributes type As a map from string to unknown.
Trent Mick 00:40:02 It's the same basic issue here, though, then, right? Is that a breaking change for… some… We accept as reasonable usage.
That's riffing on what Mark has here as an example.
Daniel Dyla (Dynatrace) 00:40:16 Yeah, the difference is that instead of adding one possible type here, you're adding all possible future types.
So, like.
If, when we get down the line, say we want to add bigInt as a possible value type later.
we have the same break later. This is doing every possible break right now.
Marc Pichler (Dynatrace) 00:40:44 Essentially forces… forces everybody who does this here.
To actually check what the word.
Daniel Dyla (Dynatrace) 00:40:51 Yeah, to be way more exhaustive, yeah.
Trent Mick 00:40:58 So I didn't hunt, like, crazy hard, the only… and this was an SK implementer side, not… not instrumentation side, but the only example I could find if someone… playing here was in DD Trace Datadog's thing they have, because they were an example of someone last time who was broken by are sensitive to API changes.
And they were using the function that's exported from the core package that does this filtering for you. So, like, you can send in whatever mess object, and it re… it drops.
Attributes that aren't conformant to the… to the format, so… That would be the kind of… function that everyone would need to go through, right? So I have this mess of things, and I'm gonna set it on attributes, or I'm gonna mess around with it. Give me a function that filters out stuff that doesn't go through.
on.
Anyway, I don't know what I'm saying. I don't have a solid feel yet for what setting to unknown would be.
Okay.
Marc Pichler (Dynatrace) 00:42:13 Bum.
I'd just say that, adding the… Extra types there to the attribute value.
deals… Good from a, from the perspective of an end user.
Who doesn't run into this, because… you know, everything's nice. You just add more stuff, and it's… and it's fine.
It would be really nice if we could just figure out, like, how many people would be broken by this, and if it's…
Trent Mick 00:42:53 We can't.
Marc Pichler (Dynatrace) 00:42:53 who then… I guess, fine.
Daniel Dyla (Dynatrace) 00:42:59 Yeah, I… I think… SDK implementers are, you know, like, we can identify classes of people likely to run into this. SDK implementers likely to run into it.
We've already said, we've already told them, API may iterate, you should follow a maximum API version.
Users who are using instrumentations that have instrumentation hooks, like you said, like attribute hooks, yes, they're somewhat likely to run into this. All of our instrumentations are 0.whatever.
And… instrumentation… authors… Have some responsibility to follow upstream development.
I think it is a awesome but unlikely break. You would have to have implemented a very specific feature in a very specific way in order for it to be a problem.
And adding… unknown to that, if they're using the API type, which we have told them to do.
Results in a compile time cha- like, break.
that their users have to go fix their code, but it doesn't require them to re-release or anything like that. It's a… it breaks at compile time, you add a slightly more exhaustive checking, and then you push again. It's not a… like a… necessarily a runtime.
threat. Because if they're not TypeScript users, they could already be sending data that's not valid anyway.
I personally think… Changing the attributes type to be a map of… String to unknown.
is a reasonable… Way to move forward.
Marc Pichler (Dynatrace) 00:45:22 I wonder… Not block any changes.
That… do that.
Daniel Dyla (Dynatrace) 00:45:29 Because I definitely think that adding new attribute types is something we do have to consider, because right now, we don't support Big Ent. That is definitely a feature that somebody is likely to ask for at some point in the future.
we don't support, like, all types of byte buffers, like buffer, Uintdate array, everything like that, UNT16 array.
We may have to support those in the future.
and it's always possible that Node.js introduces a new type.
Like, they didn't have BigInt when they started, and now they do.
So that could happen again in the future, too. So we have to consider… That we may have to expand this in the future again.
Marc Pichler (Dynatrace) 00:46:14 I have to… document… Clearly, though, that we won't just… Start accepting everything, So that people know that, like, if they pass something in that isn't compliant with what we think they should pass in, then that it is dropped, but that's a documentation.
Trent Mick 00:46:42 And that's already the case. I think passing in whatever junk to… the API methods is already… we already have to be defensive there, and our being, so I think that part's fine. I think it's just, yeah, the word out, too. If you're writing functions that get passed in.
To an instrumentation where you're going to be receiving spans and processing them yourself, then… be aware.
You need to be very defensive on.
on those things. I guess we could… Release instrumentation utiles, whether that lives in the core package or not, that is about… filtering A given mapping down to… these various versions of what attributes mean. Like, if you've written your function only for simple attributes, then we have one that'll filter it down for you and use that as your preprocessor.
Or for the next level, or for… and we could, I don't know.
name them based on the API version or something.
Daniel Dyla (Dynatrace) 00:47:41 If you're processing attributes.
you have to be defensive no matter what, because that's user input, and those users may be using JavaScript, not TypeScript, and they could be passing whatever. Like, you have to be defensive either way. You cannot assume that… the… You know, that the user input is… Well-formed and valid.
You should already be very… be… being defensive about it.
Which is why we have that method in core that drops in valid values.
If you can trust the types.
We wouldn't even have that function.
Marc Pichler (Dynatrace) 00:48:37 Oh, I'm hearing…
Trent Mick 00:48:39 It's what it's called.
Go ahead. Sorry.
Marc Pichler (Dynatrace) 00:48:43 I'm hearing we landed on… Let's try it, maybe.
Daniel Dyla (Dynatrace) 00:48:52 problem.
I guess let's wrap this before I bring that up, so go ahead and say whatever you're gonna say there, Trent.
Trent Mick 00:49:00 I was gonna say… If you click through the changes on this, at the top is the anyvalue.ts, which… has the… the union of all the different types, rather than using unknown, but… so I'd… I'd want to explore and see what the impact is of changing that.
Set to unknown, to get a feel for it.
But hopefully that is something we can do.
I had another slightly related but unrelated nickel to talk about after, but why don't you go first, Dan?
Daniel Dyla (Dynatrace) 00:49:32 Alright, mine is that… Right now… We rely on heuristics to distinguish between integers and number… and decimals.
Or floating points in our attributes.
So, in OTLP, OTLP is strongly typed.
we specifically say, this is an integer, and then we send along an integer value, or we say, this is a float, and we send along a float value. And we are currently assuming… we just do, like, a… if it is integer, we mark it as an integer, and if it is… not, then we mark it as a decimal or float, or whatever it's called in OTLP. There is no way, currently.
For users to say, Always treat this as… A floating point number, no matter what.
As far as I know, I'm not aware of any Backends, where this is a problem.
Because… you know, see previously, that it's all pretty defensively implemented, it's all user input, you know, you don't know what's coming in, that kind of thing.
But it has just bothered me for a long time.
that… We're using a heuristic there, and that there's no way for the user to control it.
Trent Mick 00:50:59 But if we're talking about, do you have an idea of how to solve that? I agree, it's… it's gross.
Daniel Dyla (Dynatrace) 00:51:05 Yeah, so there's a couple of possible ways to solve it. Some of them are way more impactful than others. I haven't looked. Metrics may have already done this. So, when you define your metric, I think you can set it as an integer or a float.
in, like, the metric view, or the metric, you know, the metric options?
Marc Pichler (Dynatrace) 00:51:26 Yeah, it's an instrument creation.
Daniel Dyla (Dynatrace) 00:51:29 Yeah, I don't know…
Trent Mick 00:51:29 That's on the metric value, not attributes, right?
Daniel Dyla (Dynatrace) 00:51:33 Yeah, that's metric value. I think that's respected.
But in attributes, it's not.
So for attributes, the way to fix it… Would be to… Probably deprecate our existing attributes… Format entirely, where it's just the map from string to value.
And have it be… more closely aligned with what OTLP is, where it's a map from… string to… Like, attribute descriptor, which contains a value and a type.
or… The whole thing becomes a list.
of… Key-value pairs with a type attached.
Both are effectively the same thing.
Both map more closely to what OTLP is.
Both are enormously breaking changes, no matter how you look at it.
You could… on, like, the SDK span, have a getter, like, have attributes be a getter that does some transformation back to the existing format, so that we don't break every span processor that's ever been built.
But… it's… super… which is why I've never brought it up before. I've been thinking about it for a long time, and I've never brought it up, because I… there's no, like, good way to fix it without breaking everybody.
And it provides, like, I think pretty minimal value.
The only reason I'm bringing it up now is because it's related to what we're talking about.
Marc Pichler (Dynatrace) 00:53:25 I think it may help with some optimizations, too.
I was having a similar thought recently around, the discussion for bound instruments.
in the metrics spec that are going on right now. I'm not sure if the PR has merged yet or not.
Because if there would be a way to construct an attributes type, as you describe it now, from a function or something like that. We could also have It be read-only?
And then attach… Attach some form of identity.
Thing to it.
tool… Like, essentially, when you record a metric data point, you just look it up by identity before, and you can pass in the same Object multiple times, and it just takes the… identifier from that, and looks up the correct metric stream to pass stuff in… pass stuff into.
So, we don't need to compute it every time.
That somebody records a metric, which is currently the case.
So there are some extra benefits that we would gain from that. But yeah, it is… A very breaking change.
Unless we accept.
Both, maybe.
Daniel Dyla (Dynatrace) 00:55:15 We could also… I mean, we could change the… internal SDK representation which doesn't break the API, and then we can add new methods for, like.
set integer attribute, set string attribute, set Decimal attribute, you know, we could… we could have typed… attribute setters.
Marc Pichler (Dynatrace) 00:55:44 are… We work with symbols somehow to define it.
Oh, because right now, the only way to have a key is through… Pepper having to keep a string.
If we export constants… There are simbers.
I don't know, I haven't thought this through.
Probably a silly idea.
Hmm.
Daniel Dyla (Dynatrace) 00:56:26 I'm not sure entirely how much value it provides, to be honest, though. Like, I don't know… If there are any backends that meaningfully distinguish between decimals and floats in attributes.
Trent Mick 00:56:43 Looks ants, Steven.
Daniel Dyla (Dynatrace) 00:56:46 Yeah, sorry.
Trent Mick 00:56:48 Yeah.
There's a part of me that I think it can bite Elasticsearch.
Where I work.
Daniel Dyla (Dynatrace) 00:57:02 Well, it could for sure…
Trent Mick 00:57:03 An example, then.
Daniel Dyla (Dynatrace) 00:57:06 It's, like, such a low-level detail that it's, like, the type of thing where it might be messing up, like, query engine optimizations that end users never see, but it's an efficiency problem, or something like that. I don't really know.
Trent Mick 00:57:27 Okay, we're not gonna solve this one in 3 minutes, so I get to pile on my other two. Go for it. There's one that bugs me, I don't have any answer for it, and I'm not even sure how important it is, but we pretend that we meet the spec requirements for supporting INT64 types, and we don't… we never will.
I'm not sure what the various barriers on those things are, it just kind of… squint my eyes a little bit and jump forward in the spec whenever I'm reading for compliance there. The other one, more particularly on this one, if you go look at the ER that's open right now, line 26, the inclusion of undefined in any value. So, the spec link, and there's a link in the comment there to the spec for any value.
And it talks about… it just kind of tosses it off in prose, saying it supports null values, for example, null and undefined in JavaScript.
I think is the language. Yeah, EG null and undefined in JavaScript, TypeScript. I think we should go back to the spec and remove undefined from this thing, because allowing undefined in… as an attribute value means that everywhere where we have common usage of passing in a JavaScript object of attributes.
Where some of them are undefined, and everyone who uses JavaScript just assumes that those ones are going to get filtered out, and not assigned.
is now gonna have a different behavior, if you know what I mean. I don't know if I explain.
Daniel Dyla (Dynatrace) 00:58:55 I just… I just had this conversation with somebody, was it with you?
Did we just talk about…
Trent Mick 00:59:01 big.
Daniel Dyla (Dynatrace) 00:59:01 Like, a week ago?
Trent Mick 00:59:03 Maybe?
Not a week ago. Would have been more than that.
Daniel Dyla (Dynatrace) 00:59:07 whatever it was, I think we came to the same conclusion, that, like, an undefined valid… the difference between An attribute with an undefined value, and an attribute that's not even existing in the map.
is too esoteric.
Or… useful…
Trent Mick 00:59:27 Yep.
Daniel Dyla (Dynatrace) 00:59:27 Like, for use. That's what null is for. Null is like, I am explicitly setting this to nothing.
Undefined is too often used for, like, existence checking.
Trent Mick 00:59:38 Yeah.
And I think this is a… this pros got added to the spec. My guess is this pros got added to the spec by someone who doesn't use JavaScript, and if you spoke to them, would be shocked that JavaScript is so weird that it has two kind of null types like this. Two null types.
So yeah, I… anyway. Okay, if… if people here generally agree with that, then I can follow up.
I think we should remove that language from the spec.
Daniel Dyla (Dynatrace) 01:00:05 I mean, it's…
Trent Mick 01:00:06 Into adding in any value with undefined.
Daniel Dyla (Dynatrace) 01:00:11 Yeah, I think it's fine.
I mean, we already do have any value with Undefined. I think Undefined is already in there, right?
Trent Mick 01:00:21 Nope.
Don't think so.
the current one.
Daniel Dyla (Dynatrace) 01:00:27 Line 26.
Marc Pichler (Dynatrace) 01:00:30 Oh, that'.
Trent Mick 01:00:30 It's only… this is a… this is a draft.
Daniel Dyla (Dynatrace) 01:00:32 -Oh.
Trent Mick 01:00:33 Oh.
Marc Pichler (Dynatrace) 01:00:34 Use the current one.
Trent Mick 01:00:36 An array of undefined?
Marc Pichler (Dynatrace) 01:00:38 Yeah, but I think those… go away.
Trent Mick 01:00:45 It just… it would just go away.
Marc Pichler (Dynatrace) 01:00:47 They go away somewhere around, somewhere along the export pipeline, but I'm not sure.
Maybe.
Trent Mick 01:00:56 Yeah, they exist in the sh… in the shadow value.
Marc Pichler (Dynatrace) 01:00:59 Just 3.
Trent Mick 01:01:00 Throw new, weird, browsery language at them, and they'll.
Marc Pichler (Dynatrace) 01:01:03 Oh, that's.
Trent Mick 01:01:04 not alone.
Marc Pichler (Dynatrace) 01:01:09 Alright.
Trent Mick 01:01:10 We've avoided triage another week. Yeah.
Marc Pichler (Dynatrace) 01:01:12 Thank you.
Daniel Dyla (Dynatrace) 01:01:13 Don't blame that line, I think you might find that it was me.
Trent Mick 01:01:16 I guess.
Daniel Dyla (Dynatrace) 01:01:17 I think there's similar pros in the spec, probably on the same page we were just looking at, that says, like, defines arrays, and says they have to be homogenous type, but they can have… Null or undefined, entries.
I think, I think that's, like, explicitly required by the spec.
Trent Mick 01:01:54 Okay.
Marc Pichler (Dynatrace) 01:01:55 We have to cart time here.
Daniel Dyla (Dynatrace) 01:01:57 Okay.
Marc Pichler (Dynatrace) 01:01:58 Anyway… Thank you, Orif, for… the discussion?
Have a nice week, and see you next week.
David Luna Bistuer 01:02:08 Yeah.
Marc Pichler (Dynatrace) 01:02:10 Thank you, bye.
