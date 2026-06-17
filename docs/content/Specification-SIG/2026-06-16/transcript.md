SIG: Specification SIG
Date: 2026-06-16
Duration: 54 minutes
============================================================

## Zoom Recording Transcript

**Reiley** 02:04 Laura.
**Pellared** 03:42 Hello? Can you excuse me?
1, 2.
**Matt Wear** 03:50 Yeah, we can hear you.
**Tigran Najaryan** 03:52 Terrible.
**Jack Berg** 05:22 Well, we're missing this week's… TC member who's supposed to lead this meeting, so I'll jump in.
And kick us off. Give me a second to organize my screen for a screen share.
Alright… So, it's June 16th, We have a relatively short agenda compared to recently, so if you have topics, please add them. Also, add your name to the attendees list if you haven't already. Let's get started with this first topic from… Jacob.
**jea** 06:19 Hey everyone, coming back to just sort of… continue, reminding and continuing discussion about the policy zip that I wrote.
I got some feedback from, Lyudmila that we wanted to go over in this meeting to talk about, declarative config, and dynamic configuration, and sort of how these things are going to interact with each other.
So, Lamila, maybe you could share some of your thoughts to get the discussion going?
**Liudmila Molkova** 06:51 Yeah. So, first of all, this policy on tap is awesome. It allows us to do a lot of things that we couldn't do. For example, to have a more, structured and strict language around, telemetry transformations, that is what I'm specifically interested in, and the dynamic one, and it allows to have, like, hundreds or maybe thousands of those rules combined.
That's amazing. The part that I think is controversial, and it's more from me reading the discussions on the OTEP than, my own concerns, I think there are people who know way more about this, is that the policy combines… sorry, the OTEP combines two parts, the… Policy itself, what to do, was the dynamic configuration part of it.
And I think there is a big question, we should have some consensus on, is whether… how we expect dynamic configuration to be handled. Is it the SDK who reloads and rebuilds the whole pipeline following the config that updates, or there are the dynamic parts of the config that are handled by individual components. And I think there was some comments from Jack, where… Jack, I think you… you were, talking about the, like, potentially reloading everything, if… if configuration changes.
And, I think, Jacob, you were more in the camp of, let's have the individual components that will be responsible for the dynamic config, at least for themselves.
And, yeah. Oh, Jack, you're muted.
**Jack Berg** 08:39 My comments were from November, It's been a long time, not sure I remember, the contacts entirely. I don't consider them… them blocking.
**Liudmila Molkova** 08:54 Okay, wonderful. I'm curious if we had discussions in the declarative config in the past about this, how the… we envisioned the dynamic configuration to be handled.
**Jack Berg** 09:08 It's… It's come up in a variety of places, the JavaSig, the Spec SIG. Declarative config has, you know, it's… maybe the topic has been broached, but we didn't have serious, discussions about it.
There's a person, Jack Shirazi from Elastic, that has a PR open right now against, the spec.
to update a part of declarative config, the API portion of it. There's this thing called config provider, and config provider is supposed to be the way that instrumentations read config and initialize themselves, in a standard way. And what Jack has been working on, in this update PR is to add the ability for an SDK to push updates to a config provider and for instrumentations to subscribe to changes. That's… That's the only material thing that has manifested in declarative config on this sort of dynamic config topic, and that's sort of strictly related to instrumentation. So it's not like, you know, dynamic config of samplers, or processors, or this or that.
we knew it would be a problem that would need to be solved in the future, and I think this is kind of going in a different direction than at least I initially envisioned.
And I guess I'm okay with that. I don't have the time to be sort of the champion or lead for Dynamic Config. So, you know, I'll let others take the lead on that.
**Liudmila Molkova** 10:56 I think, Braden, you wanted to share something related to the collector, it would be awesome.
**Braydon Kains (Google)** 11:02 Yeah, we've been having this sort of discussion on not necessarily dynamic config, but in terms of, like, how individual components reload. We have… an interface under the hood, also called Watcher, for config providers, that will let you listen for external changes. But right now, the only way that that works is that the collector has to reload entirely. So every pipeline has to reload whenever any part of the configuration map, conf map, changes.
And we've been… there's been a few related efforts to fix that. The first one is an RFC that I linked in the chat that anyone can go take a look at, which is allowing into just certain components that change to reload without, breaking the rest of the components.
exactly the mechanism by which that works changes depending on what part of the pipeline it is. Like, a receiver swapping out is different than a processor or an exporter swapping out, for example.
something that I've been looking into personally because of a similar problem is people want to load, like, rotating secrets into configs.
And now this is different than this larger dynamic configuration portion. This is an individual value, but it's kind of the same problem, where we want some sort of way for the configuration to dynamically provide updates, to a running pipeline.
And exactly the way that we do that hasn't really been worked out yet. The RFC has an alternative proposal for, like, a reload interface that every component could Theoretically implement if they want to be able to dynamically reload without triggering, like, a full component reload.
that is my personal favorite idea so far, but there's a few going around. All this is to say that, like, we're thinking about this on the collector, the current state of it is not… Super useful, because any change requires a full reload.
But we're thinking about it, and if people have ideas, I'm sure we'd be open to hearing about it.
**Jack Berg** 13:15 That collector idea is sort of what I envisioned for SDKs as well. So, you know, the collector has this this data model, that, or, you know, it's encoded in YAML, where you express your receivers, exporters, processors, and your other components, and you watch for changes to that, and when there's a change, right now, you naively, you know, reload every component, the entire collector config, but now you're trying to get more, surgical about it.
And, maybe only change the components that are impacted.
And so that's kind of how I envisioned that analog to SDK would be, you know, we have this declarative config data model. It's expressed in YAML, just the same as the collector. There's some sort of mechanism to watch for changes to your express config file, and when you watch, and when you notice a change.
You know, you go and you update the components that changed, whether that be samplers.
processors, exporters, whatever it is. And so, I think this, this policies approach is… is… is… is different. It's more, like, about, changing responding to changes of policies that impact the shape of the telemetry that's emitted, the quantity, the shape, all that type of stuff. Notably, I don't think, would address things like, hey, I want to I want to change my OTLP endpoint, or something like that. I'm not sure if that's, like, a useful thing to do, but there's all sorts of SDK-level configs, which, you know, are outside of the scope of what policies tries to express.
**jea** 14:55 Yeah, that's kind of the goal of the OTEP in general, is to be really specific on What a policy is and is not, and what we are, like, attempting to do here.
I don't think that we're, like, in, like, envisioning working on routing anytime soon. I don't think it's a discussion that, I've had with Josh. I don't think Josh is here, but, that's not something that we've discussed. Really, the focus is around you know, filtering transformation, and also the goal of this is so that they can be merged in dynamically. I think one challenge with the existing declarative config and collector config is that layering YAML dynamically is actually really challenging.
It's not really meant to be layered in that way. Trying to do the layering and ordering of those mechanisms combined with pipeline semantics, I think, is something that this avoids by designing a data model that is meant to be, like, dynamically updated. So, like, the actual independence of each policy is really the design change in that, which enables that fact.
So hopefully that clarifies a bit.
**Jack Shirazi** 16:16 I'm gold.
**Liudmila Molkova** 16:20 So it sounds like there is no… it's not the one-way door.
**Jack Shirazi** 16:25 I'm gonna place some visitors.
**Liudmila Molkova** 16:26 So if we have policies, we can still, in the future, have a dynamic config as well. They can coexist.
**jea** 16:34 Yeah, the policy dynamic configuration mechanism is currently its own thing, and I think that we need to… once we begin on the integration phase, we can figure out what that one-way… what that two-way door is.
I guess not one-way door, whatever the opposite of a one-way door is. But yeah, I think once we actually begin the implementation phase, we can look into that, but as far as the way that I've implemented it now, it's definitely not binding.
And we can figure out the right way to do it. I'd say it's very flexible in this model today.
**Trask Stalnaker** 17:16 It could be a little confusing, though, to have both. I mean, I was viewing this as… won't sort of… the alternative to dynamic… .
**Jack Shirazi** 17:30 by the point.
**Trask Stalnaker** 17:31 configuration, and I was kind of viewing this as, like.
we would… I mean, I like the… I like the policies proposal because, it… Limits… it's sort of saying, here's very specific things that we support dynamic configuration of.
As opposed to, which kind of… Potentially could help with, like, the collector stuff of, like, you're reloading the entire configuration.
And I could see the collector, you know, could still offer that as a thing.
But SDKs cannot.
Right, the collector can, you know, restart itself, essentially.
But I'm not sure that… SDKs really can support that, or… we wouldn't want to support everything dynamically. It would be very, very challenging.
**David Ashpole** 18:45 Alright, are there any more, points people want to raise. Otherwise, we can move on, I think, to the next… topic. Evo?
**Ivo Anjo** 18:56 Yes, hello. So, I… there's that issue there that I dropped a link, the proposal to replace profile and key value and unit.
Which is that, For profiling, we kind of, for a number of reasons that are kind of discussed in that thread, we would like to have a unit attached to a key and value, so we kind of did that in the profiles proto.
**Jack Shirazi** 19:24 food.
**Ivo Anjo** 19:24 But then, since that's kind of, different from the, some of the other signals where there's key and value, there was a lot of discussion about, like, how should we represent this? Is this the correct way? Do we want to consider other things? We want to… If we change this for… if we have this for profiling, does that mean that we have this for everyone else, etc?
And I think TLDR is that, right now, there's… I don't know, maybe two, three or four options going on. One is the one I dropped a link as well in the meeting notes, which is, like, a proposal to just encode the unit as part of the key, just kind of append the unit in the end of… at the end of the key with some extra rules.
We could also, keep the unit, or there's also some discussion about, like, maybe we could use the metadata as Metrix does, but Metrics also does not use this for units, because it has its own units, so it's kind of a, like.
This ticket has been around for a while, and it's, how can we move on? How can we decide on this one, is the big question.
**Tigran Najaryan** 20:48 Do you need this for, Or anything other than profiling, or you're asking for profiling specifically?
**Ivo Anjo** 20:57 For profiling specifically, although, like, there's a question of if we want, like, more as a generic, do we want to generalize this, but we need it for profiling right now, yeah. That's the blocker.
**Tigran Najaryan** 21:14 So for profiling specifically, I think it's, yeah, we're obviously allowed to make changes, it's still experimental. What the impact of the change is going to be, performance-wise, is probably something that you guys need to look at.
I guess it is not going to be a big deal, because they aren't… There's a small number of this key value attributes there in the profiles.
As far as I understand, but maybe show that, right? Do that benchmarking that demonstrates it's fine.
As for whether we want to extend it to the other signals, the question is where exactly So if it's going to be in form of semantic conventions, where do we store that?
Is it another set of attributes, or the same attributes?
how are you envisioning that? So, I think a more detailed proposal would be nice to have and review that.
**Josh Suereth** 22:18 I want to jump in and just ask, like, like, what is the… what is the blocking decision here that we have to sort out, right? Like, Profiling right now allows unit to be reported next to attribute on the data plane, like in OTLP, right? One of our proposals is that if we can start to rely on schema URL, We can move that unit into the schema.
and report it separately, right, via, like, semantic conventions. So that if I have an attribute, I could define what the unit for an attribute is and semantic conventions on the attribute. That's a thing… a way that we could move forward where this is on the side.
But that only applies to if I decide to send schema, right? If I use schema URL, which is not necessarily true for all signals in the data plane.
We also have the problem where metrics, for example.
directly report unit and description, always, on the data plane, versus relying on semantic conventions. So there's, like, there's this hairy… Tangled, nested set of issues of, like, how much metadata do we put on the data plane versus how much metadata do we want to communicate via an optional side channel?
When we looked at this, initially for profiles, right, we know that we absolutely need to report the data in the data plane for PPROF compatibility. So I think if we take that as a hard requirement.
It has to be there. Now, the question is, is it something we can make optional for profiling, where if I provide it via semantic conventions, I can… I can ignore Or, like, I can use unit locally if it exists, but I can ignore, like, empty unit values and use semantic convention schema URL instead if we wanted this side channel to report unit information. Is that something we can do going forward? Right?
To me, the blocking decision… I know I'm, I'm, like, sorry, I was late to this meeting, and now I'm, like, talking, hopefully not in circles, but to me, the important decision here is, are we okay with the way OpenTelemetry works, where profiling can send unit per attribute.
In the data plane.
But other signals cannot do the same thing.
And in my opinion, Again, if we look at, like, this PPROF thing.
Because of PPROF compatibility, we know that that's the minimum requirement for what OpenTelemetry the protocol, has.
So then, the question we need to answer is, do we feel like we need that for other signals?
or… Should we rely instead on, like, a semantic invention-driven mechanism for passing unit?
of attribute values.
I have concerns around, for other signals.
We aren't using the dictionary approach.
And so, I actually think it's gonna be incredibly expensive for us to throw all this metadata on the data plane all the time, with limited value.
So, my own thinking here… and I, you know, I listed this, is I don't think this is a block… like, I would literally just close this book, as won't fix, personally.
I don't think this needs to block you stabilizing, and I think, yes, it's not a perfect solution, but it's kind of the state we are at today, right? We have a hard requirement of PPROF compatibility.
We don't have dictionaries other places, and, we do have folks who want to see units and other things, particularly like logs. If I'm passing logs that are metric-like, sure. But I think that this, this, capability where we use a side channel, like schema URL, to communicate that information is actually better overall for the ecosystem.
Because… The unit doesn't really change significantly from batch to batch to batch to batch to batch.
So, it'd be better for us to communicate that on the side, and adjust that on the side, in my opinion. So, like, I don't think this is a blocking change for you. I want to propose that as a straw man, I think we can close this issue.
But it is…
**Tigran Najaryan** 26:25 And just to agree with you, Joe, that's exactly how it works today, informally, right? The semantic conventions, they describe what the expected unit is. We don't have it codified anywhere, but if you read the wording of a particular attribute definition in semconf.
It inevitably says what is the expectation there, unit-wise.
**Josh Suereth** 26:50 Right, exactly.
So, like, if we were to move forward with without fixing this, I think we're in a totally fine state.
And I don't think we're in… like, I don't think there's anything, like, super problematic here.
That is not kind of implicit in the hairiness of, like, supporting PPROF and existing OTLP.
**Tigran Najaryan** 27:11 And to add a bit more, I would be inclined to fix it if I thought this is an actual problem that needs fixing.
We have had these attributes for years now, on spouse and metrics.
I can't recall a case where anybody asked for a unit there. I don't know if there is anything recorded like that.
But it seems to be, as far as I know, it's… it's a known issue.
It's not an issue, right?
As far as I know. I may be wrong, if there is… If anybody has a knowledge Point me to that, that this is… A problem people want to be solved.
then, yeah, let's take a look at it. Otherwise, I'm with Josh.
Alright.
**Florian Lehner** 27:59 Hey, thanks for the feedback. Unfortunately, Ern was out last week, so I didn't catch up last week and did just, follow up on the topic today.
my… My thinking, as coming from the profiling side, is that we try to adopt profiling, key, value, and unit.
So that, it becomes key and value, key value, like everything else in the auto collector, and can be just treated at this. At the moment, key value and unit cannot be treated in any way, in the… In the collector, which makes it hard. Introducing it into the connector seems to be hard, and I think it could be a lot of tension. With regard to the SEMCOMF approach.
Hmm… Yeah, I think this would be the easiest way.
But it would break, compatibility with PPROF.
Because PProf does not specify some kind of units and values.
And… Yeah, depending on how we decide on, hey, how do we want to have compatibility. And, third point, I just learned about the matrix metadata key value.
And, it seems like there is a similar topic around this, but I think if we introduce the same approach with, like, meta… matrix metadata, I think we… we have not… we introduce a lot of complexity that I really would like to avoid in the protocol to have.
Yeah, but that's just from my learning from today.
So yeah, short… short term could really be like, hey, you have something in SEMConf?
Which makes it a little bit more complicated to follow up, but ultimately, it would be nice to have it more in the proto field, but yeah, it should not be a blocker.
Check.
**Jack Berg** 30:05 have… Have folks considered, keeping the unit, at the proto level, but only populating it in cases where you're trying to do round tripping between PPROF?
So basically keeping it as a compatibility layer, but, like, under normal circumstances for net new instrumentation, not producing it, and instead of relying on the side channel of semantic conventions and schema?
**Florian Lehner** 30:37 I think we did not discuss this in particular, but it was more implicit, applied, I would say.
I think…
**Jack Berg** 30:47 Is that fair?
**Florian Lehner** 30:48 like…
**Jack Berg** 30:49 You mentioned metric metadata, and metric metadata only exists for round-trip compatibility.
And so, like, the analog applied to profiling would be to keep unit for round-trip compatibility, but not to populate it under normal circumstances.
Or net new circumstances.
**Florian Lehner** 31:10 Yeah, I think for… Depending on the approach we are going down, If we introduce a field into key value that… Has some kind of unit information.
Then it should only be populated if the field is really needed. So, yeah, sparsely populated.
But this assumption is implicit, I would say, so not, discussed somewhere directly, I would say.
If this makes sense.
**Ivo Anjo** 31:52 In the structure that we have in the PROF, it does already say, above the units, zero indicates implicit, biosemantic conventions, or non-defined units, so, Yeah, there's already a comment there in the current protot format to kind of say that.
I'll send a link in the chat, I guess.
**Jack Berg** 32:11 Yeah, I see that.
If you wanted to make it explicit guidance, you could add something to the profile data model document in the spec that sort of reinforces that.
Anyways, just an idea.
**Ivo Anjo** 32:38 Yeah, so I think, like, just to recap, I think the current approach Yo.
The current approach we have, I think, has been working. The question is, like, do we want to change it? And if so, how do we want to change it? Because I think what we need is this ability to do the PROF round trip. I think that's the main use case.
**Josh Suereth** 33:01 I'd vote that I think we can just close the issue as won't fix. Like, we did a bunch of… we did a bunch of investigation, we looked for alternatives and things here. I think that this should be a won't fix myself. The only thing that makes me concerned is when Florian says we're having issues implementing it in the collector.
We need to make sure that we have an implementation… sorry, that we have an implementation in the collector for profiling that can round-trip PPROF. But, like, you know, whatever we need to do there, let's figure that out, to make that efficient.
**Florian Lehner** 33:32 Yeah, to narrow it down with the collector, key value and unit is not used on the resource level of the protocol. It's just a little level below, and most of the… collector stuff is not touching this, so, if you look into the, OTLP, OTLP and filter protocols, they are not touching it at the moment, so they are not going even down this level. So, it would be nice to have it in the future so that we can say, you can just describe your filter in your regular OTLP listing, and then be able to filter on it, but it will not be an immediate issue, and on the resource level, we are still already compliant with the key value on the resource attribute. So that's, that's already given.
**Josh Suereth** 34:33 So can I rephrase this? You're saying, like, if I use, like, OTTL in a transform processor.
**Florian Lehner** 34:39 Yeah, OTI was, yeah.
**Josh Suereth** 34:41 Right, right. In OTTL, I cannot see unit.
But I can see key and value.
**Florian Lehner** 34:47 Yeah, practical.
**Josh Suereth** 34:49 Interesting. Okay.
**Jack Berg** 34:51 Can OTTLC metric metadata?
**David Ashpole** 34:56 I believe so, yes. I think I've written some OTTL that touches metric metadata.
**Florian Lehner** 35:10 But it should not be a blocker, to be honest, if you are fine adding key value on Unit 2 or GTL, Then this could be resolved, and we could close the rest of the issue as it won't fix.
**Josh Suereth** 35:26 Yeah, it… that still feels like an orthogonal discussion with OTTL to me. If… if you, it might be worth it for us to have a discussion with OTTL about that issue. So, like, maybe we grab, like, OTTL maintainers and profile containers, and we have a discussion about how we can model this effectively, but again.
If we talk about what this affects, it only affects people trying to take PROF, embedded into OTLP, and then fire it through, right? Because we're not using Unit in OpenTelemetry itself yet, we're only planning that for PPROF compatibility.
And so what's the likelihood someone would be changing the unit?
in a way that, like… for example, if I drop the attribute itself, the unit's also dropped, right?
So, the only thing this impacts is if I'm trying to actually change the unit of a PPROF profile in the OpenTelemetry Collector.
So, I think it's a little bit narrow of a use case that I think we can sort out, but it's… it… it's… this seems to me like something we should be able to sort out with OTTL and with the collector without changing the protocol.
So, I don't see this as a blocker for the protocol. I think we could close that issue and open a new one on the collector to sort out what we want to do with OTTL.
**Florian Lehner** 36:45 Yeah, sounds good to me.
**David Ashpole** 36:59 Alright, good discussion.
Robert, you have the next two issues.
**Braydon Kains (Google)** 37:04 It's… there's one more from Evo. You were… you were one off in the…
**David Ashpole** 37:09 Oh my goodness, okay.
**Ivo Anjo** 37:12 The other one.
**David Ashpole** 37:13 If I'm for that.
**Ivo Anjo** 37:14 Yes, I will hope to be fast. That PR on the bottom, I think I've addressed all the issues, I fixed it, there were, like, a few conflicts, I feel the conflicts. There's, like, 4 or 5 approvals, and no pending comments, so… yes.
Hmm…
**David Ashpole** 37:46 Tigran or Josh, I'll probably assign one of you, and you can merge when you think it's ready.
Or I can merge it now.
**Josh Suereth** 37:55 I didn't… sorry, sorry, Eva, I didn't have a chance to look at how you resolved some of my comments. What did you end up taking as your approach for some of the concerns around threading?
Like, with the dictionary.
**Ivo Anjo** 38:09 I think this, this is the other, that's the other thread stuff, the, this.
**Josh Suereth** 38:15 You're a different…
**Ivo Anjo** 38:16 This is just the protobuf thing in the… yeah. The other… that one, I have not yet replied to your concerns. I'm still kind of looking at it, and I've been doing a few changes, so I… I am… I owe you a response on the other one.
**Josh Suereth** 38:28 Okay, I think this one's probably good to go for me. I'll take a quick look, because I get the two confused, and I forget which comments I made on which. Sorry.
**Ivo Anjo** 38:38 Sorry, too many PRs.
**Pellared** 38:41 Yeah, I think this is good to merge, this is more the intent and the OTEP, and the fact that we want something like this, and that's also why I approved it.
**David Ashpole** 38:53 Cool.
Robert, why don't you take us away with your issues?
**Pellared** 38:59 Okay, so, first one, I have this one, and here I have mostly questions about stabilizing these parts. So, recently, like, I don't know, a month ago, I started creating these PRs for non-OTLP representation of attributes and attributes collections.
And I started to have them as development, because the other parts of the document were stable, and I also wanted to give other people also to a chance to review, and I think this is the way to evolve the spec to make them as development.
And, I just had a question. I think this is, This part of the documentation is quite straightforward. These are just little extensions.
And we do not have… the only prototypes we have are just, draft PRs in, AutelGo, because this is our, this is our, like, public… This is just, like, two-string or string methods to existing types, and we are not able, really, to… we are not to really have a way Make them as experimental.
And the question is basically, is it okay just to mark them as stable?
Just with having these prototypes.
I proposed here just to… give a little more time, and first have a release which marks them as development, because both of these sections has not been even published, none of the releases even as development, so at least just wait, give a few, just, I don't know, a month, so they are at least for a month as development.
in a release, and on open material, and then stabilize it.
Any concerns or questions around this approach?
**David Ashpole** 41:01 It seems like it would be nice to see it in other languages. Like, I'm sure it can be implemented, but… the… If we're gonna leave it open for a month, I feel like if… even if you just opened issues and… like, Java and… somewhere else that… would get implemented.
**Pellared** 41:20 I can look into even implementing myself, I can take a look at how other languages implement it. So, I'll make a SIGNote for myself to try to implement it in other languages.
So, at least it will be available in other languages, and others will also, during reviewing, then they will have feedback. So, yeah, I will take it as an action item.
To try to make it in other languages.
Any other proposals?
Okay, then let's go to the next one.
This one is similar, but you're in a lot better, state here regarding implementations. So, this is the environment variable carrier specification.
And it's already, like, implemented in, 6 languages, and 2 are almost, like, ready to merge. They're just waiting for more approvals.
And initially, Mark had some concerns, but I think the concerns were mostly addressed in the previous PR regarding normalization, and this just proposes to have a release candidate, and then wait, like, 5 months or something like that, and mark it as stable For, for the KubeCon. This is my proposal. So far, it has two upvotes from, I think from the CICD guys, and yeah.
So this will only… proposed this as an RC.
And even if this will get approved, I will at least wait for two weeks, and to make sure that nobody blocks it.
**carlosalberto** 43:11 Yeah, I would like to see that, people who grow to maintain or plan to maintain the implementations, you know, the other languages give, you know, their blessing.
Even if it's just symbolic, like, you know, gray approval. Sorry, yeah, gray approval.
**Pellared** 43:29 Yeah, great, great idea.
Helping people, then.
**David Ashpole** 43:42 Otherwise, seems like it's in a good state.
Alright, if there's nothing left for that, Carlos, you have the remaining two items.
**carlosalberto** 43:57 Yeah, I will be, quick on those ones. The first one is the old OTEP for the context of attributes that you may remember. We are very close to merge it, There were some last updates mentioning some trade-offs.
And, some notes regarding the plan on instrumentation libraries using or not using context attributes. And, after discussions and discussions and discussions, especially with Jane AI groups, JAI people, sorry, The outcome is that we will not recommend that instrumentation libraries use them, but we will have a bigger discussion when this lands into the spec, regarding on what… under what conditions instrumentation libraries can't use this, you know, because of the… of all the potential consequences, you know? Other than that, it's just, like, there, it's… I think it's mostly fine, I need to solve a pair of issues, but it generally is good. I think that the only big issue is from Tyler, so if you can review that, Tyler, get Tyler said a call. Otherwise, we're ready to merge this, so it should happen in the following weeks, and then when this lands, I will start working on the specification part.
That's all from this side. And the second PR is, one for extending spam processor, So, this is a very simple thing, which is… it basically… we have a spa processor, three new operations, which are experimental at this time.
Basically, just for reporting when a spam is getting a new link, when an attribute is being added.
or replaced, and when you're updating the name, that's it, pretty much.
there are minor, things mentioned there by CEO and Robert. I plan to solve them, but I need also review from other people as well.
This is adding 3 new methods, as I said before, I know that, Jack, you wanted to have me to consider a single method, but this is something we talked, Robert and I, at some point, regarding how it could be better, at least for the Go implementation, to have 3 meters instead of 1.
for technical reasons, we can discuss offline if you think that… if you think that I should still try to go with that prototype, we can discuss out of line. Otherwise, just waiting for reviews.
**Liudmila Molkova** 46:32 Could it be language-specific? Like, how to implement this? Like, one meta-term is the whatever variant that describes what happened, versus multiple methods, because I think for Java, it would be… well, Java people, correct me, it would be easier to have one interface managed than multiple ones.
**Jack Berg** 46:55 I just worry about clutter. That was the point of my argument. You know, the span has a lot of fields on it, and if you have a listener for every field, that's a lot of clutter.
**carlosalberto** 47:05 So, in theory, those should be only 3 metals, but to Lamila's point, yeah, we could allow that.
Sorry, Lamilia, you want to say something.
**Liudmila Molkova** 47:18 Yeah, I'm just thinking that this… the list of three methods might grow in the future.
Like, on status set, or if we invent another property on the span, there will be more. And every time, for languages, for some languages, it is a breaking change to the new method.
And then you might be better off.
With one method that does multiple things at once.
**carlosalberto** 47:50 Yeah, Robert?
**Pellared** 47:53 I think because you are kind of in the prototyping state, I think I have support to have some loose language or some note that, implementations and prototype reveal what's the better pattern Because I think there are pros and cons, and maybe once we start implementing them in some languages, we'll have more feedback, what is… what is better long-term, because backwards for word compatibility, etc.
**carlosalberto** 48:23 Okay, in that case, I will massage the text, and probably will work on the prototype for Java. We will need more languages in the near future, but yeah, hopefully that's, That's the path to make progress.
Okay?
We looked, oh yeah, Jack.
**Jack Berg** 48:41 So, this is a proposal to extend span processor with some new in-development methods, and it just sort of, while we were talking about this, I remembered that there… there is still a method on span processor that is still in development, on ending.
And I'm wondering, you know, it feels like it's been a while since that was introduced. I'm wondering what we can do about that, and you know, I tried to look, there's no tracking issue for stability. Let's put together a tracking issue, and if you have on-ending implemented in your language, please look out for this, and… And, you know, linked to your prototype.
**carlosalberto** 49:24 Yeah, probably we… I don't think we have a… we should have an issue for that, and somebody needs to be assigned to drive that, but yeah, otherwise, yes. And probably we should… we can discuss later, like, go and check any feature that is experimental.
That has been experimental for a little while, and then just tried to, you know.
Just to complete that, you know?
**Jack Berg** 49:50 I'm gonna create an issue to, to at least start the conversation about tracking implementations and stabilization. So, yeah, look out for that, and I'll send a link to it in the… in the spec Slack channel.
**carlosalberto** 50:04 Perfect.
Thanks. Good deal.
**Liudmila Molkova** 50:09 Carlos, I have a question about the context sculpt attributes. You mentioned there is some tension and concerns from, from, I'm blanking. Mr. Elias. I know his name, of course. Tyler.
Is Tyler here?
Can we talk about this?
**carlosalberto** 50:31 I think that, it's more about that he wants things to be as clear as possible about expectations. I don't think he's supposed. Tyler, you around?
**Tyler** 50:51 Yeah, sorry. Yeah, Carlos is right. I'm not opposed, it's just cleaning up.
This, it, like, comes from a discussion like, there's been a few things on that PR… That have been, like, historically just been, like, gray areas, and, like, it's… It's just turned… my initial rejection wasn't… Like, I don't think this is supported. If you look back at the history, it was more just, like, the implementation of it was not clear, and we clarified that.
I… I don't… I mean, I could have cleared… cleared my review, but… yeah, at this point, it was just follow-up on, like, what Carlos said, like, there's just… Things that need to be captured, things like, mitigation risks and things that, like, weren't there in the evolution of the PR, so it's just more cleanup at this point.
**carlosalberto** 51:40 Yep.
**Liudmila Molkova** 51:41 Awesome.
Thank you.
**carlosalberto** 51:46 And that's all from his side.
**David Ashpole** 51:50 And I think, unless any other topics were added, I think that's it for today, so you can all have 9 minutes back. I'll see everyone next week.
Bye.
