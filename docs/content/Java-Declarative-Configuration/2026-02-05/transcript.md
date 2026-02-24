SIG: Java Declarative Configuration
Date: 2026-02-05
Duration: 48 minutes
Zoom Recording URL: https://zoom.us/rec/share/7JtexBhnqCSa4nzFAEXWLAVYs_mjc5IBNWHG7-bBsTEsmi_jN8PiZSGcCnnCWB9I.TAja38_bvTZOqwEh
============================================================

## Zoom Recording Transcript

**Gregor Zeitlinger** 00:43 Hello!
**Jack Shirazi** 00:46 Hey.
**Gregor Zeitlinger** 00:51 How's it going?
**Jack Shirazi** 00:56 Yeah, it's cool.
**Gregor Zeitlinger** 00:59 I don't trust?
**Trask Stalnaker** 01:09 Hello!
**Gregor Zeitlinger** 01:12 I was hoping to see you at Hotel Unplugged.
**Trask Stalnaker** 01:17 Yeah.
Hopefully they'll have one in, closer.
Sometime. I'm, I'm not, I'm not, also not going to KubeCon, EU this year. I'm, a little traveled out,
**Gregor Zeitlinger** 01:33 Okay.
**Trask Stalnaker** 01:34 But it sounded… sounds like it was, super successful.
**Gregor Zeitlinger** 01:39 It was my first, unplugged, but yeah.
We had great discussions.
**Trask Stalnaker** 01:48 Alright, let's…
check our agenda, since I know sometimes you'll populate Populated.
Alright, we do have, Jack Shirazi. Alright.
**Jack Shirazi** 02:10 Hello! I'm not entirely sure of the remit of this meeting, since I've never been…
**Trask Stalnaker** 02:14 I'm gonna assume it's everything. Whatever we want it to be.
**Jack Shirazi** 02:18 Yeah, perfect.
**Trask Stalnaker** 02:19 It's all good.
**Jack Shirazi** 02:20 So the first… Everything…
**Trask Stalnaker** 02:22 declarative configuration.
**Jack Shirazi** 02:24 Okay, perfect. Yeah, so, I'm gonna need a…
a mutable config provider, but it doesn't actually need to be a separate mutable config provider. We could just add isMutable.
to config provider.
And… Potentially a callback which does nothing if it's not mutable.
Or I can create an extension, which is Mutiful Config Provider.
The…
So that's… that's kind of question one, and the question two is, where does it go in the repos? And bearing in mind that I need it in Contrib, but I also need it in instrumentation, because the, for example, the methods instrumentation is going to be directly
checking and adding a callback to the mutable config provider, so it needs to be able to see it. And the place… the proper place for it would probably be in the, in the SDK repo.
I guess in the incubator part.
So, that's maybe an easier question to answer.
**Jack Berg** 03:38 So…
**Jack Shirazi** 03:40 scope of the SDK repo is obviously stuff that's in the spec, but .
**Jack Berg** 03:45 I don't think that this is, like, unreasonable to get into the spec, just nobody has driven it yet.
So, I think, like,
Yeah, like, are you interested in opening a spec PR to talk about the issue here, and potentially, you know, propose, you know, language changes?
**Jack Shirazi** 04:08 Kill me.
**Trask Stalnaker** 04:08 So it's kind of coming from the… this PR, this proposal, Does it, I think.
**Jack Shirazi** 04:20 It's… it's not… it's not in there at all. It's not relevant to there yet.
**Trask Stalnaker** 04:28 how would, I guess… I'll… Once we have these telemetry
Policies… oh, are they doing… talking anything about op-amp yet in this proposal?
**Jack Shirazi** 04:44 Yes, Ish. I mean, there is basically an OPAMP provider, which is the entry point. You can send… it's saying you can send through OPAMP to the entry point of the policy pipeline. That is one entry point for the policy pipeline.
And it specifically mentions it, but other than that, pretty much nothing.
**Trask Stalnaker** 05:06 Okay.
Yeah, like, I… so I see this whole… part as…
inevitably flowing from this, but yeah, there's definitely some steps along the way there from a… spec perspective,
But we can help to drive prototypes. I guess, so the question, yeah, is back to where does it live. Obviously, it can live in…
Contrib… .
**Jack Berg** 05:42 I mean, they could It can live in the core repo, too.
Thank you.
**Trask Stalnaker** 05:48 Vader.
**Jack Berg** 05:48 in the incubator, right? Like, I think what…
So for incubating things, I don't want things to be incubating in core forever if they have no chance of landing in the spec, but I also want to be sort of, like, pragmatic, and, like, you know.
if something is reasonably likely to end up in the spec, then we can sort of, we can bend the rules a bit and add something to the incubator ahead of time, just to reduce churn. And so…
Yeah, like, we have the incubator, if you can make the case, and maybe at least, like, open an issue or something in the spec that suggests that progress is going to be made there along those lines, then let's do that to reduce the churn.
**Jack Shirazi** 06:35 Okay, I will put it into the telemetry policy as a… As a comment.
For… for that bit.
**Jack Berg** 06:48 Because, Jack, I know we talked about this in the past, like, there's actually a comment in some of the declarative config stuff, like, hey, it's a to-do, like, hey, like, let's revisit these APIs in the context of dynamic config to make sure that they're not going to get in the way of that before stabilizing them. So, like, this dynamic config, mutable config, has been on our minds for a long time. It's just…
We just gotta kind of connect the dots and figure out, like, you know, which concepts in the spec are going to, like, leverage that and, you know, be the first people that have to, you know, write that language.
**Jack Shirazi** 07:22 Okay.
And the second part of my question here, which is, would…
would we… could we add an isMutable to config provider, or would we just have it completely separate, so there'd be an extended mutable config provider, and everything goes into that?
**Jack Berg** 07:42 I think I'm inclined to… That's tough.
Because we're talking… so where are you gonna call this thing, by the way? Are you gonna call it an instrumentation?
**Jack Shirazi** 07:54 Yeah.
**Jack Berg** 07:55 Okay.
Yeah, because I guess that was my other question, is because, like, there's no config provider right now,
it only has references to the instrumentation block, and so, you know, it's not even relevant for updating the config of SDK stuff.
So… That, that, that means that the, the…
is mutable needs to be an API-level method, not an SDK-level method. Like, we couldn't just put it on SDK config provider, and then, you know, look… cast it in instrumentation and look for it. And so, you know.
Beautiful.
if it's in the API, that means it's either directly on the base config provider interface, or there's something like an extended config provider, or a mutable config provider, which, which extends config provider, and it just has that, and that just kind of seems like
too many layers for not a good enough reason, so my gut reaction is to put it on the base.
**Trask Stalnaker** 09:00 I mean, do we need is mutable? I mean, I kind of like the idea of just…
Have the callback method, and it just no-ops if the… config provider.
**Jack Shirazi** 09:11 Cool.
**Trask Stalnaker** 09:11 Doesn't provide anything back.
**Jack Shirazi** 09:14 That works absolutely fine, except that means that we have a callback in the API, instead of just, is mutable.
**Trask Stalnaker** 09:23 Well, don't you need a callback anyways to… don't you want to…
get… Notified of config updates, as opposed bullying for them.
**Jack Shirazi** 09:35 I was… yeah, I mean, the ideal situation is we have a callback in the API, that's the perfect situation. I was thinking of a halfway house where if mutable is there, then if it is mutable, then it can do a reflection to find the callback.
But…
And then the first case of having none of that in config provider, and just having a mutable config provider that's available, and then you can do instance of and see if it's a mutable config provider. So those are, like, three different options. Yeah, the ideal would be to have the callback in
the config provider API.
**Trask Stalnaker** 10:14 And so in incubator, it would be in an just extended config provider.
And so we wouldn't stabilize that along with config provider for now, but it would be on the extended config provider, kind of, as next up to be stabilized,
**Jack Shirazi** 10:39 And it's so…
**Jack Berg** 10:44 And so, how would a callback work, actually? Like, what are you… what are you listening for? Are you, like, maybe, like, you're interested in watching a particular node of the… of the config, like, a particular declarative config properties, and whenever there's a change to that, you get this callback invoked?
**Jack Shirazi** 11:00 Yep.
**Trask Stalnaker** 11:04 I think there's… it's,
Oh, yeah, this is a good question of the tie-in with the… I think there's two competing
thought, like, two competing, options. I think that's one option, and that's a nice option. It…
Very much ties this to the config… Schema?
The other option actually would be…
To have this outside of config provider as just the policy like, a policy provider?
Where you have the callback on the policy provider.
So you can get notified of, policy changes, and that would be… something defined…
Maybe it looks like config schema, but maybe it doesn't.
Kind of a thing.
**Jack Shirazi** 12:04 Another, because the instrumentation… the instrumentation needs to… to have… that callback, right? The instrumentation… Regardless of… of…
of whether it's in the config or not, it still needs to register that it's interested in getting a callback when there's a change.
**Trask Stalnaker** 12:24 Right, so you… we… we could have… I mean, policy provider could be an API-level thing.
**Jack Berg** 12:35 Yeah, but I think, I think for now, policy is, it's pretty speculative.
And, and so the… I think the pragmatic thing to do is kind of move forward with callbacks with config provider, and then…
expect some churn in the future, potentially, because I think there's gonna need to be some, resolution between policy provider and config provider, and whatever comes to be with those things.
**Trask Stalnaker** 13:01 I like that.
I mean, and you can… then the callback could be pretty simple in terms of just, notify me when this node has changed, and then you… yeah. I mean, it's pretty straightforward.
API at that point.
We have to know when it's changed via the policy.
Provider stuff, but yeah.
**Jack Shirazi** 13:29 Okay, so I will, I will, put it into the spec, and I'll do a PR for the core, unless you want to go ahead and do any of that. Anyone else? I'm happy.
**Jack Berg** 13:41 Honestly, it's better if other people do it, because nobody reviews my PR, so, like, it's hard for me to get my own code in, so you all have better luck than me.
**Jack Shirazi** 13:50 Okay.
I'm just making that spec.
Alright, this next item, also mine.
So that goes back to that telemetry policy document where it was fairly… pretty…
incomplete in terms of how declarative config
Can specify mutable or dynamic updates.
Runtime updates.
And the thing that I understood from it, although it's not explicitly spelt out there, is that we can have this additional node. So I gave the example here of changing the sampling rate. So you've got the sampler, and that's the… the…
the way you define a sampler in the declarative config, and then it would have an extra node, which is policies, which…
You could use initialization, or ignore initialization, it doesn't really matter. The point is that at runtime, you can change this value.
And the… The thing that reads it, the provider that reads…
wherever it's coming from, would ignore everything in the declarative config, except for the policy's nodes.
And then, since… I mean, that's… that's pretty… pretty clear and straightforward and easy to implement. So it would just convert… it would find a policies mode, and it would convert it into…
the JSON format that the telemetry policy specifies, so that it can do a merge with any other sources of changes.
But essentially, this is the only bit here that the…
The policies node is the bit that we need to specify.
And the rest of it is pretty much defined according to how the component needs to change.
So, for a sampler, it's defined that it has to be trace sampling probability.
That's… That's kind of straightforward.
Yeah, so I wanted thoughts on this one.
**Jack Berg** 16:01 So if I understand, just to kind of repeat some of the things you said, clarify my understanding. So, you know, you can explicitly set things like the sampler, and maybe some metric views, and maybe some cardinality limits, things like that.
Or you can alternatively, explicitly set, like, a policy, and the policy is sort of like a higher order construct of what you want, not, like, kind of how you… how to do it. So, you're saying.
I don't even know if those are the right words, but, you know, under the hood, your policy specification gets translated to equivalent
samplers and views and things like that, cardinality limits, and the policy is, like, sort of contains all the things that are mutable about an SDK spec, and that's sort of, like, the advantage in it, is that, like, you know, it sort of limits the scope of what we have to think about from a mutability standpoint.
**Jack Shirazi** 17:01 Yes, except that it's not either or, you can do both. You can… you can also specify the way it's currently done in declarative config, so that's what I have here. I have the sampler with the probability
And the ratio set.
And then, you can also specify the policy which…
would take… which you could then change at one time. So that if you… if you change the… the line above that policies line, that would have no effect.
Exactly. If you change that, that's part of the static construction of the SDK. That has no effect, that only happens at initialization. But if you change the subsequent one, then that does have effect, because the reader would be looking for the policies node and any… and look for changes there.
**Trask Stalnaker** 17:54 Does this… then, for the callback.
With the callback, would you only ask for policy nodes?
via the callback.
**Jack Shirazi** 18:04 The callback would ask for the sampler node.
And the config provider would say, okay, I'm only looking under the policies under the sampler node.
And I… and I'll… I'll send that to the callback.
**Trask Stalnaker** 18:24 I see. Okay, so you register at this level…
And the callback returns you any policy changes under that node.
**Jack Shirazi** 18:38 And the telemetry policy pipeline has a, like, so it's going to essentially ignore anything that isn't a change, and it will also merge… if there's multiple different sources of this information, it'll merge that for us before that you get to the callback.
So don't… we don't need to worry about that. This is just… adding in…
the runtime changes into declarative Config.
And the only way that I can see…
works with the telemetry policy OTEP.
**Jack Berg** 19:17 The two problems I see with this, like, I think this, you know, we're just talking about, sort of big picture and examples and things, and these are sort of a kind of, finer detail problems, but, like, so when you specify a sampler, sampler is one of these SDK extension
plug-in interfaces, and the schema asserts that we have exactly one key-value pair underneath it. So, you know, this idea of having two key-value pairs, probability development here, and policy-slash-development.
That, that doesn't work.
Need to find some other way to do that. And that… that type of pattern, asserting one key-value pair underneath these types is, it's something that we're… we depend on quite a bit throughout the schema, so it'd be hard to change.
And then the other thing is that we're talking about callbacks for config provider, specifically on SDK components, and config provider is limited in scope right now to instrumentation.
So we'd have to, you know, think about somehow changing the scope of that so that there could be, like, sort of watchers or something within the SDK itself for changes in notes.
**Jack Shirazi** 20:28 All possible things, but…
Yeah, the… so that latter one isn't a problem, because the config provider can stay with just instrumentation changes, and this can be…
Because what happens is the policy pipeline
does the… takes the source. It does… it will know what to feed it to, and in this case, the implementer, the policy implementer, would be directly, affecting samplers rather than instrumentation. So there'd be a different implementation that,
Would be the config provider callback.
**Jack Berg** 21:03 What I'm saying is, though, is the config provider itself doesn't have access to this tracer provider node or anything underneath it. It only has access to the .instrument… the instrumentation development node.
And so, like, the idea there is that, we don't want instrumentation to be introspecting on SDK configuration and potentially accessing sensitive information, like.
API keys.
**Jack Shirazi** 21:26 Okay.
**Trask Stalnaker** 21:27 Is this policy on the… on a specific sampler?
**Jack Shirazi** 21:34 Or it is, like…
**Trask Stalnaker** 21:36 Can replace the whole sampler.
The reason I'm asking is whether…
**Jack Shirazi** 21:42 It… Do you mind?
**Trask Stalnaker** 21:43 kind of like an SDK concern. Like, if it's at the sampler level, and you're saying, swap out this sampler, then the implementation of that
It's gonna be in the SDK itself.
**Jack Shirazi** 21:56 usually.
**Trask Stalnaker** 21:57 Versus if the policy is for a specific sampler.
Then that policy can be fed to that sampler, and that sampler can update itself.
**Jack Shirazi** 22:09 It's not entirely clear. I mean, I'm expecting a chain of samplers for the… our distribution, because we need the rule-based one, and we need the parent-based one, and we need the… this one.
the one that does, numeric changes, rate sampling. So… Yeah, that's… so, I think…
we're kind of saying this structure here that I'm proposing is a no-go.
And that the policies… it sounds like the policies need to be… Maybe a separate… Top level node?
**Jack Berg** 22:49 That's… that was my intuition, Jack, is that, like, it's a separate top-level node, and…
you know, I'm not really deeply in… I haven't read this OTEP recently, and I haven't been following the changes, but, like, the type trace sampling there kind of suggests that
policy slash development has an array of objects, right? And one entry in this has a type of trace sampling and has the specification with a probability of .001.
And so that kind of suggests that this is sort of like a higher level construct, in that, like, you know, kind of scattering these all around the SDK,
you know, config objects, it's gonna be, like, a bit, like, cluttered and, you know, kind of annoying, because you're not going to be seeing all your telemetry policies in one place.
you know, it's also at odds with the schema for the reasons that I was talking about earlier.
**Jack Shirazi** 23:46 Okay, I mean, I'm good with that. This part of this discussion is where does it fit in? So I'm fine with it being a top-level node, in which case it's just list policies underneath it.
**Trask Stalnaker** 24:01 And does it just beca… is it… should it just be policy provider, then?
As opposed to blending it in config provider.
**Jack Shirazi** 24:09 No, policy provider is a specific component, so within the declarative config, you can build the policy pipeline.
But that's separate from the policy itself.
So each policy is… Entered into the policy pipeline, and then it progresses through until it's applied.
So a policy… a policy is basically a rule defining an outcome. Like, this policy here is… it's saying, I want my trace sampling probability to be…
0.1%.
**Trask Stalnaker** 24:45 I guess the argument for separating them is that the declarative config
Doesn't have to change at all, like, it's just the fixed component, and then you have kind of this separate layer that some…
that SDKs and instrumentation and other things can sort of opt into listening for… to applying policies.
**Jack Shirazi** 25:13 Okay, wait, so you're suggesting not to use the declarative config at all for the policies?
Which is… I mean, it's fine, because I'm already going to be supporting the JSON format, and I just wanted to… if I was going to support the declarative config format, then I just wanted to… I mean, I'm absolutely fine with the JSON format. Our distribution already uses
not the exact JSON format that's specified in that telemetry policy, but a very similar one.
So that's absolutely fine for me.
I know that Jacob Arloff is proposing also to… Build a proto-Buff, format.
I discussed it with him, I'm not entirely sure why, but I'm fine with supporting that too. So what I'd say then from this discussion is that we don't need
the policies to be defined in declarative config at all.
**Trask Stalnaker** 26:18 I… we don't hear you, Jack.
**Jack Berg** 26:20 No, I'm just thinking, like.
**Trask Stalnaker** 26:22 Sorry, I thought I saw your lips moving. They did briefly.
**Jack Berg** 26:25 I'm trying, like, so… I… I think an SDK still needs to, like, some sort of…
It needs to be notified some way that, like, policies are in play, and that it needs to… there's going to be something
like, this policy provider or something that is receiving updates to the policy and manipulating SDK objects.
Like, so that needs some surface area in declarative config, I would think.
**Trask Stalnaker** 26:56 Why in declarative config?
**Jack Berg** 26:59 Well, so, like, so what else is going to initialize that thing? Like, so the…
you know, declarative config is responsible for, like, you know, bootstrapping all the SDK components.
**Trask Stalnaker** 27:12 Oh, you mean for bootstrapping the policy provider itself?
**Jack Berg** 27:17 Yeah, yeah, exactly.
**Trask Stalnaker** 27:19 With, like, an op-amp address, that kind of thing.
**Jack Berg** 27:23 Something like that, exactly, right, yeah.
**Trask Stalnaker** 27:25 Sure, so that…
**Jack Shirazi** 27:26 That's the policy pipeline, that's the.
**Trask Stalnaker** 27:28 Then, yeah.
**Jack Shirazi** 27:29 Exactly, that's… so that's the policy provider, the policy implementers, the policy store, and the policy aggregators. That is an actual pipeline that fits in perfectly with declarative config. We just haven't come up with the… the… you know, we haven't defined the schema yet, but that's… that's separate. So you're absolutely right, that's the construction of the pipeline.
And that's the same as all the other pipelines that we construct in the SDK.
And that's separate from… The policies that are actually being pumped into the pipeline.
**Jack Berg** 28:00 Okay, so then I think the policies that would be pumped in, should those have surface area and declarative config? One thing that comes to mind, and this is maybe what we're looking at here, is, like, do you need to be able to specify, as a part of your policy provider, an initial policy?
**Jack Shirazi** 28:15 No, you don't.
**Jack Berg** 28:17 Okay.
Okay, so the initial state of all these things is implied to be sort of static.
that you, you know, you're getting it from your sampler, you're getting it from your views, you're getting it from your, you know, your scope config. And then, you know, the policy provider piece is reaching out to some network location and getting, you know, dynamic changes to that and updating the SDK accordingly.
**Jack Shirazi** 28:43 Exactly.
**Jack Berg** 28:43 Okay.
**Trask Stalnaker** 28:47 I think, I have the… I have… I think it's gonna be simpler.
To separate them.
I think it's gonna, like, from a… I know, and maybe that's just an initial piece, but, like, blending them introduces a lot of questions that separating them,
I think keeps it simple, like, you don't have to answer, because you already have…
They're already defining these policies, what they are, and if we just expose them independently to components.
Then we don't have to answer any of these questions about how does… how do policies merge or blend into declarative configuration.
**Jack Shirazi** 29:41 Okay, that's all clear to me, thank you very much.
**Trask Stalnaker** 29:48 Wait, let's see if Jack's got…
Any more thoughts? Because I know… Okay.
**Jack Berg** 29:53 No, no, no, like, yeah, I think it sounded like we were all sort of converging on the same idea, so…
**Trask Stalnaker** 30:00 Awesome.
Alright, Jack D.
**Jack Berg** 30:08 Yeah, this, this is, this is a topic that came up from Anurag.
And, Anurag has been working on a bunch of internal telemetry instrumentation, updating, the SDK, all of… there's a bunch of…
Let me back up. There's new semantic conventions for internal telemetry. They're sort of wide-reaching. They touch, like, the core of the SDK themselves, like Tracer provider and logger provider. They touch the processors, like batch span processor and, you know,
batch log record processor, and I think the simple processors as well. And they touch the exporters, the OTLP exporters and the Zipkin exporters. And so, there's this other PR that Honorag opened, 8037, and, he…
Added a system properties slash environment variables mechanism to specify the version of internal telemetry that you want.
as a sort of stopgap. And I was like, okay, this, this, this is cool, this is a stopgap, but, you know, just as a principle,
I want declarative config to be a strict superset of everything that's available in system properties and environment variables. And so, you know, I, you know, drafted up the declarative config counterpart to this.
And in declarative config, there's this sort of, there's this question that I don't think exists with system properties, and the question is, what should the default internal telemetry version be?
And, so if this isn't specified, if the user doesn't specify this, what should we do? And some of the context is, like, declarative config is green field, and so, you know, we can… we have permission to make breaking changes, and, you know, we can…
Whereas with system properties and environment variables, people have been using that for a long time, and so there's, maybe people depending on the existing behavior of this internal telemetry.
That's, like, that's one bet.
The other bit is that the various components around the SDK, they use different versions of internal telemetry by default.
So, like, if the tracer provider, for example, has this new internal telemetry that it emits.
There was no legacy equivalent.
So, it's net new. And so, when… as soon as you set a meter provider on your tracer provider, like, it is going to be emitting the new internal telemetry schema.
And… and that's in contrast with, like, batch span processor, batch log record processor, and the OTLP exporters. If you don't do anything to those except for set a meter provider, those will emit the legacy.
semantic conventions, or not even semantic conventions, the legacy internal telemetry, which, like, we sort of kind of came up with ourselves. And so, like, if you don't do anything, you get this sort of split-brain mode, where some components are emitting legacy, and some components are emitting
new.
and that's the case with…
the system properties and environment variables, and so onorox PR is affected by that as well, but, like, you know.
do we want to do something different for declarative config? Do we want to sort of be opinionated and, you know, align all the components to the latest by default, for example?
**Trask Stalnaker** 33:40 So, we could definitely realign I'll do a one-time realignment.
Because of what you mentioned about, basically.
Opting into declarative config is a change, so we can have different behavior there.
I think the conservative thing, at least, what we've kind of tried to express through semantic convention migrations is
Same… don't, once we do that realignment.
Then… don't change.
Anything…
Until… well, I guess you'll never be able to do a major version bump. This is part of the problem.
**Jack Berg** 34:31 Right.
**Trask Stalnaker** 34:33 So, I guess…
The most conservative we could say would be no… no change to default behavior until it's stabilized, and then we would do one breaking change there.
While… We can support an opt-in setting to let people You know.
Say they… they accept those… Braking changes along the way.
**Jack Berg** 35:03 Yeah, and the issue that I have with that is that means that our default behavior is split brain.
And that's ugly. And so, another, conservative approach that I thought we could take, Trask, and, you know.
I don't love this either, but, it… it saves us from the split-brain problem, is to actually disable internal telemetry by default.
And wait until… so there's no split-brand problem, but there's no internal telemetry at all until you tell us what you want.
**Trask Stalnaker** 35:38 Yeah… And then we can enable it by default once it's stable.
**Jack Berg** 35:45 Right, and in the interim, like, let's say that takes a bit of time, in the interim, the agent could be more opinionated about its default.
Because the agent has the ability to have major version bumps.
**Trask Stalnaker** 36:01 Right, and so this would be how you could do internal telemetry version slash development.
To make it… Kind of clear that that's an experimental opt-in setting that Can be bro- can break.
**Jack Berg** 36:17 Yeah, there's a separate question around whether, like, we need that slash development suffix, if the… if there's a parent element that already has that slash development suffix, like, you know, the instrumentation slash development.
I, I…
**Trask Stalnaker** 36:31 She don't know.
**Jack Berg** 36:31 the answer to that. Like…
**Trask Stalnaker** 36:34 But aren't we gonna remove the slash development out…
**Jack Berg** 36:38 Exactly.
**Trask Stalnaker** 36:38 slash development everywhere, intentionally in… the Java age in the instrumentation.
**Jack Berg** 36:46 Oh, God.
**Trask Stalnaker** 36:47 under the…
**Jack Berg** 36:47 Yeah, yeah.
**Trask Stalnaker** 36:48 Under the assumption that This node will be stabilized at some point.
**Jack Berg** 36:55 Yeah, right,
And, like, you know, but, like, let's say we had OTEL SDK, the, like, you know, the… not the terminating property, but, like.
One level above that. Let's say we had slash development on that. Would it be implicit that all direct, like, children of that would be in development?
**Trask Stalnaker** 37:16 Yes.
Okay, yeah. I say that definitively, but that's just my… that's how… that's how we've been interpreting the rules in the instrumentation repo.
**Gregor Zeitlinger** 37:29 Okay. Wait, you're saying that slash development is not transitive in… across all levels?
Did I get that right?
**Jack Berg** 37:40 We're… we're kind of…
**Trask Stalnaker** 37:41 Are you asking me?
**Jack Berg** 37:42 on the floor.
**Trask Stalnaker** 37:43 Yeah.
**Gregor Zeitlinger** 37:45 Because I'm highly surprised now.
**Trask Stalnaker** 37:49 In the instrumentation repo, Gregor, we have been treating it as transitive.
**Gregor Zeitlinger** 37:54 Okay, that's also what I have been, yeah. Thinking so far.
**Trask Stalnaker** 37:59 You and I are aligned on that.
**Gregor Zeitlinger** 38:01 Okay.
**Jack Berg** 38:03 Now, I've been treating it as transitive as well, but what Trask is pointing out is that it's problematic, because, like, if you treat it as transitive all the way down, and in the short-term future, the instrumentation block removes this suffix, then that, like, all of a sudden, all the children become, you know, stable.
**Trask Stalnaker** 38:21 I… that's funny, yes. So, I have not been treating… we have not been treating the…
this one as transitive. So yes, we have very… Contradictory rules.
**Gregor Zeitlinger** 38:36 We have.
**Jack Berg** 38:36 some…
**Gregor Zeitlinger** 38:37 Kind of double,
development. So we have added… we have it at the top, and we also added in… And…
the individual properties
But I think mostly because we had experimented there before declarative configuration, and we kind of translated it, I think that's how it turned out. Or have you been thinking about it differently, Trask?
**Trask Stalnaker** 39:02 I've been under the assumption that this was going to change, they were going to drop the slash development here at some point.
That's a good reason.
Shit.
**Jack Berg** 39:17 You were thinking ahead, so I think you were correct, I think, to try to have this double slash development situation.
**Gregor Zeitlinger** 39:30 But what about other people who have not been thinking.
**Trask Stalnaker** 39:34 So, what do you…
**Gregor Zeitlinger** 39:35 iPad.
**Trask Stalnaker** 39:36 proposing.
is, so we wouldn't turn it off… By… oh, by default.
Would we only turn it off by default for people using declarative config?
**Jack Berg** 39:51 Yes.
And I guess I would go to Honorog's PR right now, and Honorag's PR is like, hey, if you don't specify this property at all.
you're going to get whatever the programmatic APIs do by default, which is, like, split brain.
And so, I would give Anurag this guidance, like, hey, like, let's avoid split brain. So, you know, we should… we should have the… we can have for the environment variables and system properties, we can have the default for that be legacy. But when you specify legacy, that should turn off the internal telemetry.
That only supports the new semantic conventions.
**Trask Stalnaker** 40:40 Yeah.
**Jack Berg** 40:40 So, like, that would be the principle. Like, choose whatever default you want, but, like, you know, no matter what, don't be split-brained.
**Trask Stalnaker** 40:52 Makes sense to me.
**Jack Berg** 40:53 Okay. I just wanted to talk that out with people that were more on the instrumentation side of things, because…
Yeah, this… This is in the core repository, but it's definitely instrumentation.
**Trask Stalnaker** 41:07 I like the… I think it's a really good strategy to not emit anything.
By default, that's not stable from the SDK.
**Jack Berg** 41:18 Learn our lesson.
**Trask Stalnaker** 41:20 I mean, I know we think of internal telemetry as being internal and fungible, but, like.
It… people are using it, and alerting on it, and stuff.
**Jack Berg** 41:31 Oh, yeah, and Anrag makes the case down here that, like, hey, with enough notification time, Like, even a…
Maybe we could change from legacy to latest without a major version bump?
But I don't know, that's… I don't…
I wish we could do that, but I just feel like we're gonna receive a lot of complaints.
Did Trask?
Is Trask still here?
His face is very frozen.
**Jack Shirazi** 42:23 I'll give him a minute to come back.
**Jack Berg** 43:14 We'll start sharing my screen.
Just as a contingency for Trask not coming back.
Oh!
Drask is back, his re… his router.
**Trask** 43:27 No, but I'm on my phone now.
**Jack Berg** 43:32 Alright, I got, I got the screen share taken care of.
**Trask** 43:35 Okay, great.
**Jack Berg** 43:39 Okay, so I think we've probably spent enough time on that topic, unless you have any last bits, Trask?
**Trask** 43:48 No, that sounds good.
**Jack Berg** 43:51 Alright, Gregor.
Two PRs. You want to start with this distro node one?
**Trask** 43:57 Yeah, I can…
Take that. Gregor, have you seen my runtime telemetry, PR that I put up yesterday?
**Jack Berg** 44:15 Gregor, you're muted.
**Gregor Zeitlinger** 44:18 Thanks for pointing out!
So that PR is gonna change things?
**Trask** 44:24 Yeah, so that PR came out of my struggles to…
review this P… your PR here?
Because our, our runtime… telemetry…
configuration story is really a mess, and so I think your PR just,
Highlights what a mess it is already.
So, I spent a good bit of time,
On this, I think it came out nice, but it needs some… serious.
review cycles.
**Gregor Zeitlinger** 45:05 Yeah, okay, got it.
**Trask** 45:08 And also, I think we'll need to… we should wait until after next week's release to merge it, because…
I had already put in a runtime… merged a runtime telemetry PR to deprecate a bunch of things that were public that maybe shouldn't
have been… And so one, I think, would kind of need that deprecation cycle
To go through in this next release, and then we can remove them in here.
**Gregor Zeitlinger** 45:44 Okay, Jack, can you just, add a comment to my PR that it's blocked by the other one, then I won't forget?
**Jack Berg** 45:53 Got it.
**Gregor Zeitlinger** 45:54 Thanks.
**Trask** 46:02 Yeah, I reviewed everything in your PR, except for the… all the runtime telemetry-related changes.
**Gregor Zeitlinger** 46:11 Yeah, I like…
**Trask** 46:13 I think you'll like the… my PR from, like, the, like, the spring. It simplifies the spring stuff, also, to have now only one
not have… not have, kind of, that…
Java 8 versus Java 17 branching everywhere.
**Gregor Zeitlinger** 46:36 Didn't you already have a different PR? Okay, I'll figure it out.
**Jack Berg** 46:48 You want to go to the next one, or do you want me to try to find that code?
**Gregor Zeitlinger** 46:51 No, no, no, just go to the next one.
**Jack Berg** 46:54 Okay.
**Trask** 47:00 This one is… Just blocked on me reviewing it.
Apologies.
**Gregor Zeitlinger** 47:08 Would it make sense if we, take a look now, or…
**Trask** 47:11 Todd.
I think it'll be a… oh, a little hard on my phone, let me see how my computer's doing here.
**Gregor Zeitlinger** 47:22 No worries!
**Trask** 47:23 Yeah.
Maybe we can,
huddle on Slack at some point. If I… how about by Monday? If I don't get it, let's… let's do a Slack huddle and look at it together.
**Gregor Zeitlinger** 47:39 Hey, yeah, just send me a message.
**Trask** 47:41 Okay. Awesome.
Yeah, I think I'm gonna need to reboot my computer here. So… Cool, anything… else…
You want to chat about before having a little break before our next meeting?
Alright.
Go declarative config.
**Gregor Zeitlinger** 48:17 Canton.
**Trask** 48:19 Bye.
