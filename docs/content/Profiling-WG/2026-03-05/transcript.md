SIG: Profiling WG
Date: 2026-03-05
Duration: 62 minutes
Zoom Recording URL: https://zoom.us/rec/share/1wWipkM3pC8MYpOCxS2j_vqYKawH9DvI3QL9SAZP92Jf6Sde_xQ26TpvCYqWAkx6.T9AfGGuY-zG6GVFW
============================================================

## Zoom Recording Transcript

Florian Lehner 00:00:51 Hello.
Felix Geisendörfer 00:03:48 A few minutes in, so I'll slowly get us started. Let me share my screen.
So, as usual, we'll start by going over previous action items.
I'll copy them…
Hey, is, Alexi here?
Ivo Anjo 00:04:30 He's not joined yet.
Felix Geisendörfer 00:04:32 Okay, it's not… yeah, he sometimes joins a little later, it's early for him in his time zone. I would suggest, we'll… we'll just move this a little bit lower.
Ivo Anjo 00:04:40 Oh, he just joined, so…
Felix Geisendörfer 00:04:42 Oh, okay.
Well…
Ivo Anjo 00:04:44 Hello, Alexei.
Felix Geisendörfer 00:04:46 Hey, yeah, we were just talking about you, so I'm gonna group all of yours together so we can cover the.
Alexey A 00:04:50 Yes. Hello, sorry, I'm a bit late.
Felix Geisendörfer 00:04:54 No worries. We were gonna go over action items, and your draft blog post has a link for people to review, I would guess? How ready for review is this? Is this, like, early draft, or should people start commenting?
Alexey A 00:05:11 I think you can start commenting on…
introduction, production profiling for all, standardizing data representation. I would love, like, feedback on the structure,
I try to…
Can I cover three… I'm thinking of, like, covering three areas in the blog post. One is…
data format, which is the proto, kind of, like, what the proto… what the format itself entails, what work has been done, since, like, previous blog posts, and for Alpha, what are the notable things.
The second one is eBPF Profiler, and kind of, like, agent infrastructure, and I think eBPF Agent is an example of that.
And then third section down below is…
kind of, like, fitting into OpenTelemetry ecosystem, and there I was thinking of, like, talking about collector, and… and kind of… so, like, essentially, yeah, profiling as part of hotel ecosystem,
this is kind of, like, the outline. Also, there's getting started section. I don't have, like, specific thoughts. If people have, I think it would be nice to…
Kind of, like, get an idea of, get to people the idea of, like, where they could get started, and then at the end.
What's next?
That's kind of like introduction into the future, and what people can do, and how they can report bugs. So this is kind of like the rough structure. If anyone wants to take, like, for example, if anyone…
like, first… I would love feedback on whether this structure makes sense.
Second, I would love feedback on, particular wording. Like, English is not my second… is not my first language. English is my second language. I know that I can… I know that,
some of my passages can be… can be rough for a native speaker, so if anyone wants to, like, take added permissions and Polish all that, I would more than appreciate it, and I will not, like, get offended or anything. So, I just need… I know I… I know my English needs Polish. And then also…
Felix Geisendörfer 00:07:17 It's actually… I just want to say, it's really refreshing to read something that seems to be written by humans these days, so I think this is pretty nice.
Alexey A 00:07:24 already.
I… I did talk, like, I did talk with, Gemini in some parts for, like, a, like, to polish the language in particular, but… but no, like, yeah, no, this is, this is written by human, by a human.
And… and also for the EPPF agent and for, hotel ecosystem.
If anyone has even, like, if anyone has any thoughts, or if anyone wants to, like, add
Like, basically, I'm… I'm ready to, like… I would… I will take as much contribution as anyone can give, but other than that, I will keep finalizing it, but I would like to turn this into a PR… PR next week.
Yeah, I was also thinking, like… I was also thinking, like, who else should review it? I will probably also ping Morgan, and Josh specifically to take a look from the, kind of, like.
OpenTelemetry PR perspective, I don't like terminology…
do we make any promises we should make? I don't think there are any problems like that, but I would love someone who is just familiar with, kind of the PR process to take a look as well.
Felix Geisendörfer 00:08:43 Yeah, I think this looks good on a high level. I think there's always a question on things like that, on how much we should talk about, sort of.
the nitty-gritty details that went into making it happening versus, like, what's in it for the users, and this seems balanced, as in, like, having, both content for the users as well as people who want to know a little bit on how we got there.
Alexey A 00:09:07 Yeah, I would… I would encourage everyone to, like, take a look and comment with whatever thoughts you have. I don't promise to take them all into account, because usually it's not possible to take all opinions into account.
But, yeah. I see Christos raised hand.
Christos Kalkanis 00:09:25 Yeah, I'll pay Damien, so he could probably contribute to the Open Telemetry Collector section. He has a lot of context there, he did a lot of the work.
And therefore, the EVPFA Zoom part, I think.
like, it would be nice if we gave, you know, every reader of this blog an easy way to test the system end-to-end, and the best way to do that is to also mention DevFiler, because if you put the eBPF profiling agent together with DevFiler, you have an end-to-end system, because DevFiler acts as the backend.
So that way, you know, everyone can just, if he has access to a Linux system, can try it out immediately.
Felix Geisendörfer 00:10:05 Yeah, and going one step further, it might be nice to have a screenshot from, like, a flame graph from DevFiler in there.
Alexey A 00:10:12 That do open the imagery log posts…
Christos Kalkanis 00:10:16 I can make suggestions, like, I can add suggestions other than, Feel free to add them.
Alexey A 00:10:22 Yeah, yeah, yeah, yeah, yeah, that sounds good. Yeah, feel free to, like, make suggested edits, or feel free to ask for edit permissions, or feel free to leave the comments, and I will…
I will incorporate that. Does Google Posts
didn't OpenTelemetry allow peak images? Like, I assume they do, it's just, I think, the two previous ones for profiling.
We didn't have any images, but I assume there's something like image directory or something. They don't have to be all text, right?
But I'll take a look. Yeah, a picture would be nice.
Felix Geisendörfer 00:11:06 Okay, but this looks great. I think this is off to a good start, and we can all leave some comments on there. Thank you so much, Alexi. Anybody else has immediate thoughts before we move on to the next action items?
Going once, going twice, I think this one is probably about the, validation tool you're building.
Any updates on that, Alexi? You might be muted if you speak up.
Alexey A 00:11:34 Yeah, I got muted. No, I didn't work on that, I assumed this is not a, alpha blocker, so, I'll…
I'll maybe try to get it done before alpha, but no promises.
Felix Geisendörfer 00:11:48 Yeah, I think this is not an alpha blocker.
So, yeah, I think the blog post is a much higher priority.
Alexey A 00:11:58 about what period?
Felix Geisendörfer 00:11:59 type and profile text messages?
Alexey A 00:12:01 Not done yet, but I will… I will do this, because this one is quick, and I think it's good to get documentation clarifications before. Like, I don't think it's alpha blocker, but it's just good to get, clarifications in, so I'll…
I'll… do it.
Sometime next week.
Felix Geisendörfer 00:12:17 Okay.
Context propagation, OTAP, how's that coming along? EVO, any…
Ivo Anjo 00:12:26 I dropped a quick note below. So basically, in terms of the spec, we've gotten a few more comments. I've replied to a few more comments. I think the big three things that need to be kind of updated slash improved in the spec are there. Like, he's documenting the discussion we had two weeks ago of the default resource.
And how does that, fit into when you have multiple SDKs?
We discussed the, the publish, the synchronization on, a publish is done with the signature, not with the timestamp, and…
But on update, we synchronize with the timestamp, so it's kind of… we can fix that up as well. And the one thing that we were kind of discussed a bit, but didn't not have time two weeks ago, was deciding on, like.
if we do want a monotonic timestamp or not.
Felix Geisendörfer 00:13:24 Right. I think we had a… sort of… popular…
stands in the room that we want a monotonic timestamp, but I…
I don't know if we wrote it in the notes, let's just quickly recall that.
Ivo Anjo 00:13:40 I might have… Miss… it…
Felix Geisendörfer 00:13:45 Oh, dude.
Ivo Anjo 00:13:46 Because it was kind of the last, like, a bit at the end of the discussion, so I might…
Yeah, I guess we had that.
Yeah, so I can make that up late as well, so I think right now the ball is on my side to make those updates, and then ask folks if they're happy with the current version of the spec.
Felix Geisendörfer 00:14:10 Yeah, and when I say, like, it was a popular opinion, it apparently was my opinion, and it was popular with me. If anybody has thoughts, please let Ivo know.
Frederic Branczyk 00:14:20 For what it's worth, I agreed then, and I still agree.
Felix Geisendörfer 00:14:24 Okay.
Cool. So, yeah. Anything you need from the group right now, Ibo, or you'll ping people once you've done the iteration?
Ivo Anjo 00:14:37 I think, we're good on this right now.
Felix Geisendörfer 00:14:40 Awesome, cool.
Then I think we can get into 733, which has landed, this is amazing. And Florian has a bunch of other PRs and flights that we could talk about.
Do you want to introduce it?
Florian Lehner 00:14:58 Yeah, there are in-flight draft PRs that once we get a new release cut.
we can start using it in the collector. We have… Breaking change.
And the change of the reference-based attributes, so that's… that's significant.
And, yeah, that's why there are free draft PRs. The later one, so to collect a contract, this one, yeah.
is to fix tests, and currently we assume that input is always the output, and, if we change in between something, the validation does no longer happen, as we, update Indeed tests in place.
For memory efficiency. So, yeah, there was a…
needed some adjustments in the collector, but I think at the moment.
We are just all waiting for the cut of the release, and then we can continue.
Oh.
Sure.
Josh Suereth 00:16:05 Yeah, I'll see if I can kick that release off today. I'm not the on-call for the TC for doing releases, but the
proto-repo is kind of ad hoc anyway, so I'll sync with the TC right now and see if we can cut that.
just for context, is there anything you need in there before we cut a release? Like, I know that we made the changes, the docs are up to date, is there anything…
before I just, like, push it, is there anything that you think we need in that repo? Because, again, releases…
You know how they're few and far between, so I want to make sure we got everything.
Florian Lehner 00:16:41 I think the only discussion point is key value and attribute with Bochtown.
But, I think the consensus between the majority is that this is not a blocking…
Blocking topic, to be, for the… for the cut of the release and declaring profiles as alpha.
Josh Suereth 00:17:00 Yeah, we met.
Florian Lehner 00:17:01 with the T.
Josh Suereth 00:17:02 yesterday, and Bogdan wasn't there, but the consensus of the TC who were, was that this is not Bogdan, so I think you're fine.
Florian Lehner 00:17:11 Yeah, for the rest of the… of the profile signal, I think it's… no matter how we end up with key value and unit.
it might be a breaking change after the alpha release then. But alpha release is no promise, so this…
should be fine, but this will be at least a breaking change, I would say.
Josh Suereth 00:17:34 So, the breaking change would be the name of the proto-message, right?
Florian Lehner 00:17:40 No. If we decide on, hey, we drop key value and unit attributes and just used, regular key-value attributes.
as Bogdan is suggesting, just without the unit attributes, and have the units in the semantic conventions, then it would drop a message.
Josh Suereth 00:18:01 No, no, if we… if we add key value and unit, you would… we would update key value to include an optional unit reference to a dictionary.
Florian Lehner 00:18:09 Okay, yeah, that's, like, the odds.
Josh Suereth 00:18:10 Yeah, if we were to make these the same, there is no world where that unit doesn't live in OTLP, because we need that for PROP. That's another thing we discussed, like, that's, again.
Florian Lehner 00:18:22 currency.
Josh Suereth 00:18:23 when and how we do that, like, it still is a breaking change, by the way. Even if the protos are exactly the same shape, you don't break the protocol behavior, but the way we've designed our rules, it kind of breaks instrumentation, code generation, so, and it may break some JSON thingies, but we can look at that. It's just…
Yes, it's a braking change, but it's like a…
Slightly breaking change that we'd want to do before you go to full release.
Florian Lehner 00:18:51 Yeah, right, yeah. So, yeah, I see it as a breaking change, no matter how we end up.
Yeah, but yeah.
Felix Geisendörfer 00:19:05 Okay, Florian, do you need anything from this right now, other than the proto-release to move forward?
Florian Lehner 00:19:12 No, I would just back collector and collector contract people.
Okay. I think in this group here, no one has the necessary, Permissions to bring this forward.
Felix Geisendörfer 00:19:26 That makes sense.
I think that takes us through the action items. I want to quickly share the roadmaps that I put together to kind of make sure we're all sort of in agreement on what needs to happen before Alpha.
Oops, let me make this bigger. So I think the biggest thing that we need to decide is whether we need to, and this goes back to your question, Josh, like, anything you need in the proto, before the release.
we need to be on the same page whether we're going to rename the import pass. Right now, this would probably… I think we're probably not in favor of that, and just want to leave it for the alpha, and only bump it once we go stable.
But we never, I think, had a written down confirmation that this is acceptable. I think somebody found a link or some docs in the Proto repo that says we probably shouldn't even have done this import pass naming to begin with that we have right now, but…
I don't remember the exact history there. Anyway, Josh, can you shine some light on, sort of, how you're feeling about the import path right now?
Josh Suereth 00:20:34 Yeah, yeah, apologies if I didn't follow up on that. We documented this in the Proto repo.
So basically, all the way through Alpha, until you're ready for release candidate, you will continue to use development. There's a reason it's development and not experimental.
So, the development tag you'll use through Alpha, you'll use through beta, you'll use through the whole process. And then when you're ready… when we're confident we're ready to go stable, then you're gonna move it to V1. So you're gonna go straight from V1 experimental to V1.
Felix Geisendörfer 00:21:06 you want to develop.
Josh Suereth 00:21:07 Excellent.
Felix Geisendörfer 00:21:07 To be one.
Josh Suereth 00:21:09 Sorry, yeah, from development to V1, yeah.
Felix Geisendörfer 00:21:12 Sorry, we used to call it experimental. We created this new thing called development so that you can do that, but the idea is.
Josh Suereth 00:21:18 And if this isn't clear.
I can go update it, but that's the intention of what this was.
So that you, you would remain, in… in that, you know, development layer.
Yeah, see, we recommend using development, alpha, beta, release candidate levels to communicate different grades of components.
And then you go to stable. But the whole, like, package name is supposed to be this experimental thing all the way through. Go ahead, Alexi.
Alexey A 00:21:51 I think… I posted a note yesterday in the Slack chat. One thing that confused me, there's also… there's a document called
It's under specs, it's called versioning and Stability, and one thing it says is, like.
Terms which denote stability, such as development, must not be used as part of a directory
or import name. Package version numbers… package version numbers may include a suffix such as alphabet development, so that quote kind of, like, made me think that, like, oh, maybe we did…
A wrong… the wrong thing a long time ago.
Josh Suereth 00:22:31 No, so this is one of those, you know, the song, One of these things is not like the other.
the protocol doesn't really look like normal instrumentation, like normal packaging and stuff, so that guidance is geared towards, like, instrumentation packages, libraries that you release, that sort of thing. This is an embedded thing inside of the proto, and we… the proto has a lot more restrictions on it.
To begin with, around what we consider stable, and there's more limitations on, you know, consumption. It's a lot more expensive to churn package names in the proto than it is instrumentation.
So, yeah, this is an area where we have chosen to kind of deviate from that guidance purposely to give a good OTLP experience for people.
But it's a good call-out.
Christos Kalkanis 00:23:27 Hey, Josh, I asked some questions in Slack, so the…
Yeah, maybe just clarify in the actual document, because it's not clear what the packet's name, needs. Like, there's nothing… there's no language there that specifies that.
But there's also language that says maturity levels, such as alpha, beta, and so on, need to be communicated, but it doesn't specify how. So if we can say it's the package name, what alternatives do we have to communicate the maturity level of the protocol?
Josh Suereth 00:23:55 I would put that on comments in the files of the proto.
Christos Kalkanis 00:24:00 Okay.
Josh Suereth 00:24:00 So, and I'll tell you what, I'll just take the AI to go write a proposal to reframe this language.
for why we're doing this, and, like, the rationale behind it, and put it in there. But yeah, so basically, the package that you use needs to be not our stable package, because once we go to stable, we don't want that to change ever, and we're allowing the unstable bit to change. So that's like a tooling, you know, human review kind of thing.
inside of your protos, and this is what we do in our spec, we actually just denote on the proto the stability level that we're giving to that proto. So, if you think of it this way, you're dividing the protocol, where you have
a package in which you can make braking changes, but all the other packages do not have to have braking changes, okay? And then, on particular fields and things, you annotate their stability level.
This is what we did when we added things into key value in the common proto, for example. So, if you, if you were to open up the proto repo and take a look, right, the, the, just take a look at the,
I think it's in… if you want to see what we did for entities, you can look in common resource, and I can show you what we did there.
But just take a look at any of those files, in common that we have some of these fields on. Yeah, so you should be able to see for particular fields, like if you… yeah, entity ref is status development.
Right, so it is in a stable package, but that particular message is still considered development, and this is a necessary thing for us to evolve the protocol just practically.
Because the reason it has to be in this package is it actually modifies resource, and so there's a field on resource that is marked with a different stability level than the rest.
Otherwise, we wouldn't be able to evolve our protocol.
So the important bit is that you have it documented somewhere what the full stability level is. Like, I would… and again, if this isn't true in profiling today, I would go through every single message and put that… unless it's stable, put that status of where it actually is in terms of, you know, stability.
And then when we go alpha, we'll flip from, you know.
development to alpha on that line.
Go ahead, Alexi.
Alexey A 00:26:26 more of a profiling-specific question. Once we release Alpha, will we stop the practice of changing the proto-field IDs? Because I think so far we've been renaming them to kind of keep them tidy.
I assume that after alpha is released, even if we make a breaking change, we will… we probably will not reuse the… the IDs, right? Because it's,
Because it's… it's just…
Or, or will be. Like, I think it depends, like, what we mean by no guarantees and braking changes are okay, like, what kind of braking changes is okay.
Christos Kalkanis 00:27:06 So maybe that's related to my next point, which is right here in the document. So I think, up to now, we've been kind of lax with breaking changes, like, we've been breaking the protocol a lot. That affected the collector, it also affected the profiling, but post-Alpha is one goal of the alpha, is for us to attract multiple users and multiple types of deployment.
And then, if we keep this practice of making silent breaking changes, by silent, I mean producers and consumers have no way to detect that the breaking change took place, so then data propagates through the processing pipeline, and we have no control over how breakouts takes place, or what the side effects are, and so on. So, this doesn't seem conducive.
to that more expanded use of the alpha profiling, right? So ideally, producers and consumers would have a way to detect that they're incompatible, and then prevent data from actually being processed. Now, I'm perfectly about, you know, what the scheme has just described.
They were keeping the packets fixed, but then…
we need, I guess, another way to make that incompatibility post-alpha.
More, easier to detect.
Florian Lehner 00:28:18 I think this incompatibility is possible to detect with, resource attributes.
And if we set the respective,
I think it's SDK, telemetry SDK version, to the respective alpha version, or beta, or alpha 1, or a date, then we can do this. And, the routing processor of OTECollector, makes use of this,
Of these resource attributes, so we can use them. So, just like… Differentiating.
Alexey A 00:28:58 Aye.
Yeah, I… I'm kind of like a…
In two minds, because on one hand, yes, it's… it's, like, we don't want to break people, but also, like, if you go all the way versioning.
it's… It can be tricky, and it's… it's not like in…
Easy thing to maintain perfectly.
So… I… I wonder if something, like, we… like, we… we… we stop reusing, and, like, changing proto IDs?
For example, like, specific scenario, K, value, and unit. Let's say, like, we figure out that this, like, goes into the, like, it becomes the standard representation, and we need to make that change in the proto. One change we could make is just, like, just change the message type and keep the current ID.
And that is not good, I think, because it basically is just, like, if you have a serialized proto from alpha, and you try to read it after this change, it's just, you get, like, who knows what, right? Because it's just, like, the same field ID, serialized, but the meaning now changed, so maybe it will crash, maybe it's something. But if we don't reuse the ID,
you will read the data, you will have the data missing, and maybe that code… the code could… can… can use that to detect that, like, oh, there are no attributes, and act accordingly. But if you try to also kind of, like.
capture this in the resource ID, okay, like, this is, like, version alpha…
2.0 or something, and then people need to have some kind of, like, the code that checks, like, oh, if this alpha 2.0, then, like, use this field, otherwise use that. You can do this, but I think it piles up also very quickly. Maybe I'm wrong, it just… it's just, like, versioning has costs, and I think…
It would be good To be, kind of, like, pariet-optimal here.
Christos Kalkanis 00:30:47 I think what I had in mind was, like, while we're in development, like, before we hit stable, we don't want to support multiple versions, right? So, whether that's the collector, or… you would typically try to support the latest version of the protocol, so
from that point of view, we don't introduce additional complexity. Versioning exists only to allow a simple check. Am I compatible? And if I'm not compatible, I stop whatever it is that I'm doing, whether that's ingestion or processing and so on.
But it's not to allow the backend to support multiple versions of the protocol, right?
Josh?
Josh Suereth 00:31:27 It's gonna basically give you some guidance on things that we already have, but I think what you need is slightly different. So the…
Instrumentation scope has a version.
that you can use to say what the version of the profile would be underneath it, but that is intended to be, like, the attribute conventions. So if you change from using, like, you know,
process.id to P… to PID, that is what that version's meant to be. And, that is what we're trying to have, like.
translation, because the OTLP message is not supposed to be different at all. It's just the contents of the OTLP may be different, or may have additional meaning, and that, version and instrumentation scope and the schema URL parameter are supposed to tell users what that happens to be.
That is the versioning that we've built into OTLP. But it's kind of like, you know, LTLP can handle any kind of data. Instrumentation,
The instrumentation scope scheme URL tells you exactly what to expect in messages, is kind of the idea. It's like a refined, cool, here's the structure you should expect.
specifically. So this would be, you know, maybe there's one for PPROF that says, here are the fields that PPROF fill out. Maybe there's one for the eBPF profile you're building in OTEL, right?
that doesn't sound like what you want here. What we did previously with, like, metrics and things.
I don't know if this is good, but basically, when we'd make those changes, we'd always use new IDs, and I think you should… we should probably formalize this to say after alpha, you can't reuse IDs, but effectively, the way you fail is if the ID doesn't exist that you need, you say, hey, this isn't a format I support anymore.
You know, like, you would have required things that you need to find.
I don't know if I like that, I'm just saying that's kind of what we did for metrics.
Christos Kalkanis 00:33:27 Yeah, that works as long as you don't change the semantics of a field with an existing ID, right? If you only add new fields, that's fine, I guess.
Josh Suereth 00:33:36 Right, and are you willing to limit yourself during alpha to only do that, right? If you need to change semantics, make a new field ID. You don't have to necessarily make a new field, but you have to make a new ID for the field that changes semantics.
Christos Kalkanis 00:33:51 So, the failure case that I had primarily in mind is, we have back-end infrastructure in place, we update the backend infrastructure to the latest, because we made a breaking change in the protocol, we update the auto collector,
to support it, and then we have existing, agents or other libraries that, right, that are still on the older version. We need… so…
Having a way to detect that a breaking change took place, and then having the agent error out with, I don't support this, you know, this version of the backend, is an easy way to force clients to upgrade to the latest version, and also prevent further processing from taking place.
but I guess, yeah, I mean, I have to…
think about it a little more, also, in terms of how the internal deployments look like at Elastic.
with the alpha, we want to expand the usage of the protocol internally.
Felix, what are you using this? Because I think Datadog is using it, right? Internally, or not?
Felix Geisendörfer 00:34:59 The OTLP protocol.
Christos Kalkanis 00:35:03 Right, yeah.
Felix Geisendörfer 00:35:04 As far as I know, we've always just tried to stay on top of the changes to the proto without trying to support older versions, but maybe NAF or EVO can…
Keep me honest on this one.
Nayef Ghattas 00:35:19 Yeah, so far we've been trying to update to the latest versions of the portos, and
Each time we get a breaking change, we stop supporting the older versions of our…
Christos Kalkanis 00:35:33 Okay, so, but,
But you're going to have errant clients, possibly. In a complicated infrastructure, you can't just, you know, be aware of every agent that runs your infrastructure that tries to ingest another version of the protocol, right? So you update the backend to the latest version, what happens if you have older clients trying to write to the backend? Is that a scenario that concerns you, or not?
Felix Geisendörfer 00:35:55 I mean, it's not good for the older clients, let's put it this way, but the way we've solved it so far is by not using the OTLP protocol in any load-bearing cases. It's mostly been used for internal testing, or
early design partners who wanted to try it out, but we've not given it to anybody and be like, this is something you should rely on. Now, our hope is that once we go to alpha, that that is something we could do, so I think
we would probably be interested in, being able to easily detect if an incoming payload is from an older version of the proto, like the first alpha, or, like, a later iteration, and then…
we wouldn't expect the whole ecosystem to do that, but maybe we would be willing to actually support, like, several versions and do the necessary conversions between them for a while. So I think it would, in other words, would be nice if we had, like, some metadata on the payloads that told us which
OTLP version it is, in particular, that's on the payload. It's my… I'm thinking here.
Alexey A 00:36:55 Christos, I'm also curious what you said, like.
like, a simple am I compatible check, but I wonder, like, what that simple am I compatible check would look like. I can definitely check against, like, the exact version of the, like, say, like, OpenTelemetry prototy release, that's easy, like, but that's also very fragile, and you need to update it very often. And if I want to do, like, oh, if the version is at least X,
But future changes could be… could be breaking, right? So, it's like… like, what… what exact…
Like, what exactly… unless you check for a feature bit.
like, what would the… and maybe we need to discuss this separately, because I'm also, like, a bit afraid to go into a lot… into the weeds, but…
Christos Kalkanis 00:37:39 So, it would be a version that we bump whenever we make a breaking change to the alpha, right? So…
Whenever we make a break-in change, we bounce that version, and then if the client,
isn't on a version, it just stops, essentially, because it knows that the American change was made. Nothing further than that.
Alexey A 00:37:55 Oh, I see. So it would be a separate versioning from OpenTelemetry Proto itself, or we would kind of, like, coordinate, like, bump the minor version whenever OpenTelemetry Alpha protocol makes a breaking change?
Christos Kalkanis 00:38:11 Yeah, I don't know what the best way to do it… to do it. Okay.
Alexey A 00:38:14 Yeah.
Felix Geisendörfer 00:38:15 I would personally feel pretty strongly that I don't want to, like, reinvent a new versioning scheme or some semantic versioning inside of OTLP. I would
if anything, just really take the release tag on the OTLP proto repo and just carry that through the payloads and allow clients to do something with it. This would not probably be recommended for the collector or for most of the ecosystem, but for, I think, backends that want to support stuff.
It would be path well, but maybe the collector is on the critical path for that, so…
But yeah, anyway, I don't think we should have another versioning system on top of what OTLP versions are.
Christos Kalkanis 00:38:54 Nia?
Nayef Ghattas 00:38:56 So yeah, I think there's a schema URL field in Scope Profiles.
Which says that this is a schema that applies to the data under the scope field and all profiles in the profiles field.
My understanding was that this is already used for scope attributes, and for resource attributes, respectively, for the one that is on the… on resource profiles.
Because, attributes can change, like process.id might be process something else, and this is used to sort of be able to differentiate, and I wonder if we can use the same thing also, if there are any semantic changes on the…
on the profiles.
Josh Suereth 00:39:42 We… we did actually talk about that about 10 minutes ago, and yeah, I don't… I don't think so. That is designed for, like, the shape of the attributes, and so if you start to use it to mean…
the actual protocol itself, I think we get into really confusing territory. There's rules around what schema URL should be. Like, schema URL might be, hey, this is a PPOF profile.
Versus this is one generated by the OpenTelemetry eBPF. So yeah, I don't know if that was gonna work. I was gonna say, I think you should open a bug against the protorepo, because honestly, I really like the idea of communicating the version of the protocol you're using.
in the request.
And I think that maybe should be a protocol thing that we have, so that when you get something in, it'll tell you, like, this is 1.7, or I'm trying to send you 1.7. I'm trying to send you 1.8, right? This is giving us some future compatibility. I've heard the term, throw yourself a forward pass, like in football.
if we start doing that now across the board in OTEL, it actually opens room for us to make good changes, and one of the issues we had for profiling specifically that led to all of that pain
figuring this out, was we don't have that today across the board, and so it's really hard for us to make changes, where, like, that semantics would be needed.
if we start communicating early, I think it's a good idea. So I… I would open a bug about that discussion to see if we can solve this more generally. I'll take that to the TC to kind of talk through, or we take it to the spec meeting. We'll probably start with the spec, then TC if we need.
I really like that idea, but I think you want a new place for this. And I think it's a need across the protocol.
Nayef Ghattas 00:41:29 But my understanding was that the schema file format would support any sort of changes. Right now, it only has changes for the attributes that are implemented in them, so it only supports that, like, there's rename attributes and rename events and things like that, but in theory, couldn't we also
Use that to… Support other types of changes that are,
Signal-specific, because there's already one keypark signal as well in that file format.
Josh Suereth 00:42:00 It can… it's not designed to handle the protocol changes.
It, like, it can handle a signal change of how you put the data in the protocol. It is not designed to handle an actual protocol change. One of the things that we're modeling there, like, one of the reasons we only do attribute renames right now is it might have transformations that are tied to the data model of the signal itself.
And once those start to get added, that data model cannot change, right? And that would be hugely breaking.
But it's… it is not, like, again.
you're half right that it's designed for that, but I don't think it's quite what you need here for this particular use case, which is we might be making some changes, and we need room to be able to do that without breaking the whole ecosystem and
things that people have set up.
Felix Geisendörfer 00:42:53 So if you're… if you like this idea of, like, including the OTLP version in the payloads, I'd be happy to, A, raise the initial issue, but also maybe come up with a proposal.
Because I think it could also, yeah, help with a lot of other things in the future to extend OTLP in various ways that we've discussed. So I think I have some ideas there and would like to work on this, so I'll assign myself an action item.
Josh Suereth 00:43:21 Yeah, if you… if you guys open the issue with what you need, and then I can just take and make sure the right people are in the discussions.
Felix Geisendörfer 00:43:37 Okay, I'll kick off this discussion. I think for now, maybe we can just agree that
We're not gonna try to make lots of little breaking changes during the alpha, we're mostly gonna try to add, like, new stuff that wouldn't invalidate old payloads, and if we have to make
some breaking changes, maybe we can hold off until we go to the next level, potentially better, and do it all in one go, maybe queue them up in a branch or something. That would be my preference, to just keep the alpha stable for now until we have all the answers. What do you all think?
Christos Kalkanis 00:44:15 Yeah, sounds good.
Felix Geisendörfer 00:44:39 Okay,
I do want to go back to, sort of, the roadmap again to make sure we just have, everything on the boards that we need to think about here. So, I think we've settled the V1 development question, as in, no, we don't need to make an update to that.
I guess we've got Josh to confirm it. I guess there is some language in the README already, and Josh is gonna take a step at maybe making this more clear.
But I think for this room, we can conclude that this is not a blocker, so that also means that this is unblocked. And Josh said he could push this forward, cutting off the new proto-release.
So that would be the most critical next step to basically unlock, the three pull requests that Florian has pending. I only have one here, but I'll probably update this. Maybe I'll switch back to, like, a simpler view if we don't have so many cross-dependencies and just group things by what's critical and what's not.
Alpha, we've, the blog post, we've got a good progress from Alexi, that's great.
lauren is going to present at the, secondification meeting. Can you remind me when that's coming up?
Florian Lehner 00:45:49 Next week, Tuesday.
Felix Geisendörfer 00:45:51 Next week, Tuesday? Okay, thanks, that's awesome. And then we need, a TC review. Josh, I put your name down for now, because you've been the most helpful, so unfortunately you're the one I think of first, but if you want to give this to Tcran or something, feel free. But yeah, I think, I guess once, once 110 is tagged.
It would be good… oh, actually, sorry, you did say something earlier that makes… give me a pause on the 110 release. You said you want the maturity indicator levels as comments on all the message types. This is something you need before you cut the release. This is something we should do real quick.
Josh Suereth 00:46:27 I think, yeah, now that you're moving to alpha, we should totally do that, so that we denote that these things are now under alpha. If you want… like, so if you want the 110 release to be the alpha release, that's fine. The other thing we could do is we could release it, you could make the changes to the collector, and then we can have a second release where it's marked as alpha?
Where, that is, basically, there's no change to the proto itself, just those annotations are now there. Whatever, like, I'm fine either way. The second one isn't a big lift.
Go ahead, Alex.
Alexey A 00:47:01 On, on, on the roadmap, there are two… this, like, present at SIG, and present, and, TC Review.
those are two things that I… I think, like, those are the only two things that have kind of, like, external to profiling SIG dependency. I'm…
slightly, like…
Do we expect any potential blockers there? I'm just… I'm just a bit, like, worried that we go to that meeting, and then there's…
someone…
who never heard of the profiling work, and they're like, oh, like, profiling releases to Alpha? Let me, like, I need two weeks to take a closer look. But.
Josh Suereth 00:47:36 Yeah.
Alexey A 00:47:37 Are there any… are there any risks here?
Josh Suereth 00:47:40 Oh, yes, yeah, as you know, so, I know this is recorded, I'm just gonna be blunt, like, that, that, that, the reason we're doing this is because, like, I, you know, Tigran and I have been here and active, and we're supposed to be your liaisons in preventing that risk.
And so one thing I did drop the ball on is I know you wanted to go alpha, but I didn't think about, like, oh, we have to advertise this through the TC in case they have concerns. So I'm trying to be more proactive, and I think for your next release, going to beta, I'd like to actually be more involved in the process to make sure we're giving communication to TC and keeping them abreast to reduce that risk.
early.
And is there anything that we haven't already talked about that I'm worried about here? Not really.
But, getting the TC to, like, start to pay attention, to get up to speed on what you're doing, get up to speed on major decisions, that is something that we're trying to do here. That's why, in the… if you look at the recording of the TC meeting yesterday, you can see we talked a lot about profiling.
like, at the very end. It's the last thing, because we had a big agenda. That discussion has basically been, hey, I, you know.
as many as possible should come to this SpecSig meeting so that they can get up to speed on what you're doing, they can hear that communication, and we'll have a list, I'm putting a document together where they can just put questions in it.
Of concerns that they have, and we'll know what we need to address. And do I expect anything? Honestly, no, I don't, because, like, I've been working with you all, and I'm comfortable with what we're doing. However.
What… what… if you were a betting person right now, you should bet against me on that. Just… just calling it out. So we'll… we'll see. Like, I'm not aware of anything, I don't expect anything.
But it's possible, is what I call it.
Felix Geisendörfer 00:49:29 If I had to call out any particular risk, I think that during the last TC meeting, you agreed that profiling can go to alpha, ignoring the key value attribute, or unit, sorry, the unit discussion, and Bogdan was not in that meeting, so if Bogdan comes back and is like, oh, no, this is a blocker, then
That would maybe put us in an awkward spot, so hopefully that doesn't happen.
Josh Suereth 00:49:51 It might, but at that point, I think I'd take it to TC Vote, because I think we've… we've gone back and forth on that, enough that it's worth just…
like, we… the TC, we generally try to get 100% consensus, but in times where we can't, we take it to vote. So, in this case, given timelines and things, my plan there would be to take that to vote.
Felix Geisendörfer 00:50:14 Okay.
Alexey A 00:50:15 There's also… there's also a separate box for Spec SIG review. There's, like, separate…
TC and… is this, like, the same thing?
Josh Suereth 00:50:25 So, the spec sig, it's actually… we… what we… bleh.
Let me, let me formulate my thoughts quick. The spec sig…
was originally just about the spec. What we've tried to turn it into is maintainers of projects in OpenTelemetry, maintainers of the specification, and the TC. That is supposed to be a channel where we can all meet and discuss things publicly together. There's a private TC meeting that is publicly recorded.
Where the TC can meet to discuss things at higher bandwidth, but what we're trying to do as a TC is have most of these large technical decisions happen in that SpecSIG meeting. So, like.
we… if you want to get TC feedback, that is a good place to go, because there's a require… well, it's not a formal requirement, it's kind of an unofficial thing we have on ourselves, that we need to have sufficient TC members in that meeting, so that you can run things by us and get our feedback.
Usually, there's between 4 to 6 TC members in that meeting, which is over half of the TC.
Right.
So that's why, like, if you want to think about your TC review, that discussion you're having there will be your initial feedback of what the TC thinks.
I'm also going to, in the private, discussion, just have a chance to… and it'll be publicly reported, so you can watch it, but that's what we'll do, a follow-up the next day, to just try to get through things a lot faster.
Does that help explain, like, the process and what those two things are?
Felix Geisendörfer 00:52:00 I think that was very useful, yeah.
Alexey A 00:52:02 Thank you.
Felix Geisendörfer 00:52:09 Okay, I think then, we still haven't made a call here, what we want to do with V10. Do we want to make the update to the alpha, comments or not?
if it's really as simple as just slapping alpha on there, I think we can get an approved pull request to you by either end of day today or early tomorrow before you start your day tomorrow. And you could just merge that in.
Josh Suereth 00:52:38 it might be that the TC will want to approve the alpha before we mark the proto as alpha. So I don't think… like, if you want to get me that by the end of the day, and we'll see if we get approvals, great.
Felix Geisendörfer 00:52:51 Actually, I think…
Josh Suereth 00:52:52 Good.
Felix Geisendörfer 00:52:53 I think you raise a good point there, like, if we mark the messages as alpha, and then you cut a release, we have effectively released the alpha of profiling, and if that is pending on TC review, we can't do it. So we need to cut V10 without C stability indicators, as it is right now.
So I think we want your help going forward with that, and then we… if we get the TC's approval, then the only step remaining is to update those comments, from my point of view.
Okay.
Florian Lehner 00:53:20 I would also support this, that, because the documentation and the blog post is also not yet ready for alpha.
So, if we cut the release now, we can…
Do all the stuff to the collector, and make sure everything is working fine, and then if everything is working fine, we can just…
Change the tags from development to, to alpha.
Have the blog post in place, and also the documentation.
Alexey A 00:53:50 And also, this is released for the… this is… this is released for the whole… this is version for the whole OpenTelemetry Proto
repo, right? Like, it would be nice… it would be… it would be odd to have alpha in that name, or would it be, like, profiling alpha? Like, what would be the… like, what would be the suffix? I… sorry, I didn't get that part.
Josh Suereth 00:54:07 The release of OpenTelemetry Proto will just be 1.x, and in the release notes, it'll say that the profiling.
Alexey A 00:54:13 Oh, the…
Josh Suereth 00:54:13 Snail Alpha.
Alexey A 00:54:15 Oh, okay. In the release notes, not the… okay, this is not about the version itself, okay.
Felix Geisendörfer 00:54:28 Yeah, so we're not touching the import path, to be very clear here. The thing that we would be touching is, I think I had a comment here on entity refs. We would basically just add comments like this, like status would be alpha instead of development, and we would do that for every…
message on… in… in profiling, I suppose.
Florian Lehner 00:54:47 I can make it for development today, and then…
Josh can probably prove it and cut it.
Felix Geisendörfer 00:54:57 Do we need some development techs? I mean, we didn't have some before, and we're still in development technically, so… I mean, it's nice, but I don't know.
Josh Suereth 00:55:03 Yeah, you don't need the development tags, because you're in a.
Florian Lehner 00:55:05 development.
Josh Suereth 00:55:06 It's, it's when the, when your stability doesn't match the expectation of the package.
Florian Lehner 00:55:13 Okay, cool, yeah. On the reference-based attributes, we have the development text already, but just not on the profiles protocol.
Josh Suereth 00:55:20 Yeah, yeah, and that… again, that's why we asked for them in the… the reference attributes are in the stable package, so that's why they have to have the declared locally, like, don't use this, yep.
Alexey A 00:55:31 I also remember there is a separate versioning schema for Go-generated messages repo, or something like that. I remember, like, protobuf is, like, separate there. Is… will that stay the same way for Alpha, or does it need to change?
Josh Suereth 00:55:47 Sorry, say that, what, what's… what's the difference?
Alexey A 00:55:51 I think, like, in the Go-generated package, there is, like, a separate…
Package or, like, separate version for profiling, like, 0.10 or something?
Josh Suereth 00:56:00 Oh, that's… so, we… okay. The… the packaging, we don't own. That's a GoSig question. My guess is, because of our stable-by-default requirements, and because of craziness with Go, that will probably be the same. It'll probably be a separate package you have to import with profiling in it.
But the weird thing is, they… we will have to probably give them a warning about these unstable bits in the proto to make sure that they're exposed. I'll have to look at what they did for entities. That's something I haven't paid attention to, sorry. But that's… the… each language owns their…
proto-packaging.
There's a whole…
fun can of worms we can get into if you want to talk about how it works individually for each language and some of the complications, but like, you know, all the Java ones are handwritten, for example. I don't know if Jonathan Halliday's here, he's been maintaining those for us, but…
For profiling. So, so it's,
This is one where, when I do cut the release, we're gonna have to warn the languages ahead of time, and it might take a while for them to adopt this version of the protocol because of that.
Alexey A 00:57:11 We will probably want the code gen to update at least, like, Shortly, or…
At the time when we announce all the phone, so that if people start using it, they kind of like, they get the…
Felix Geisendörfer 00:57:31 Yeah, it depends a little bit on the use case. The collector, I think, also has its own hand-rolled code gen for Go, so… and Florian's pull requests have already been updating that, so once those lines, the collector will have,
A working,
version, I think that's initially the most important, and then we can figure out the SDKs, I think, afterwards.
Alexey A 00:57:50 It's eventually consistent.
Jonathan Halliday (IBM) 00:57:51 Yeah, the Java SDK is non-critical. The only slight caveat to that is that because all the proto is released in lockstep as a single
release artifact. There's no way for.
the Java or any other SDK to consume
An update, say, to metrics, without also consuming profile update.
So if there is…
Some reason why it urgently needs to patch metrics, but the stuff for profiles isn't ready yet.
There's no way to do that.
I don't think it'll be an issue, because the other
Signal types don't update that often.
Felix Geisendörfer 00:58:41 Okay,
Going back to the roadmap, I think we now have a pretty clear path of what we need to do, and who's gonna work on it. The main unblocker being the V10 release, so thanks for your help with that, Josh.
And…
Yeah, and I think there was another idea of, like, meeting weekly now. I would actually, support that. Would others here be able to make it next week as well?
Awesome, then now I'll just capture this right here. I don't know if we had an agenda item for it, but…
Alexey A 00:59:24 I don't know who has, like, the
permission to copy that calendar invite? Or should we just, like, add it for ourselves and just join the same Zoom as usual?
Josh Suereth 00:59:35 In OpenTelemetry Community Repo, there's a whole thing about how to modify the calendar. If you're in the community, there's a group you become a part of, and then anyone in the OpenTelemetry ecosystem can change calendar. So, you might actually have access already, by being in the right set of groups, but there's docs on
community for how you can update and modify it. Like, you as a SIG should have full control of your calendar entry, if you want it.
Felix Geisendörfer 01:00:01 Yeah, I'll take an action item, I'll handle it to make sure the official event gets updated. If it's not for some reason, if I can't figure it out, I'll send communications through the CNCF Slack to let… I'll let you know how we convene otherwise.
Josh Suereth 01:00:14 Yeah, actually, your GC liaison, would be the person to ping if you have trouble. Yeah.
Felix Geisendörfer 01:00:20 Morgan?
Josh Suereth 01:00:22 I believe that's Morgan, yeah.
But that, that, that infra is all owned by the GC, not the TC, so…
Alexey A 01:00:30 And I think it's only one extra meeting before 26th, so if we want…
If we want to also meet, like, last moment.
before KubeCon, then I think it will have to be a different time, not Thursday.
If I counted days correctly.
Felix Geisendörfer 01:00:48 Yeah, let's… decide on the next meeting also in the meantime, like, like, let's be very active on chat, let's talk to each other. If needed, let's hop on ad hoc Zooms, because we don't have a lot of room for error, but we do have a realistic path to get the alpha out for KubeCon, so it'd be awesome if we can make it.
Cool. I think we're out of time, Frederick, Ivo, are you okay if we push yours to the next meeting?
Or do you wanna… Yeah.
Frederic Branczyk 01:01:20 I'm fine with that. It's not that big of a deal anyways, it's just something that made us pause and think.
Because we were adding column support to our storage.
Ivo Anjo 01:01:32 Sounds good from our side as well, and if people are curious, I left the PR draft there so we can start looking into it as well.
Felix Geisendörfer 01:01:43 Okay, cool. I'll copy these both over to the next meeting, so…
And then I'll wrap us up here. Thank you, everybody, for joining, thank you for all the hard work leading up to the alpha release, and have a nice local time.
Frederic Branczyk 01:01:58 Thanks, Al.
Ivo Anjo 01:01:59 See you, everyone.
Florian Lehner 01:02:00 Thank you.
