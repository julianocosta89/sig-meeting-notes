SIG: Java SIG
Date: 2026-07-23
Duration: 62 minutes
============================================================

## Zoom Recording Transcript

Gregor Zeitlinger 00:12:38 Hello!
Jason Plumb 00:12:44 Hello, Gregor.
Jack Berg 00:13:38 Hello, all.
Jason Plumb 00:13:42 Hey, hey!
Jack Berg 00:13:47 Rask is not here today, so I'm gonna get my machine set up for sharing.
We'll get started in a few minutes.
Please add any items to the agenda that you want to talk about.
All right, let's get started. Felix, I see you are here again, to talk about backporting CVE fixes. I know we didn't get to this item last time, so let's talk about it first. Sorry about that for the last time.
Felix Wong 00:15:49 Yep, no worries.
So, the… the reason is we would like to backport the, CVE back to earlier version, is we have a micro-profile telemetry, project, which has a specification of each version, right? So, and we have 1.0… 1.1, 2.0, and 2.1, and each version has a specific version of OpenTelemetry Java that we are using.
So, for the old one, I mean, back to the old version, 1.0, we only had, like, tracing only, so we did not even support, light logging and metrics.
So, for the 1.0 version, or even the 1.1, I mean, those old ones, migrating to the latest 1.62 is… too much for us, I think, to, work with.
Because I think the, like, the 1.62 has everything the latest and greatest, right? So, backporting it back to our old spec will be exposing a lot more function than what originally intended.
So, I would… I mean, to be practical, to, bring back the CVE fixes to these old versions. I think it's the… backporting it back to the, older version of the OpenTelemetry Java will be my recommendation.
Jack Berg 00:17:19 So, I guess… What… So, let's talk about the CVE a little bit. So this CVE, what happened with this was that there is a, There's an opportunity where the W3C baggage propagator, it didn't add bounds on the memory that was allocated, so you could have a large number of baggage entries, and that could cause a large amount of memory to be allocated in your Java service.
And the… the reason why it's only a moderate, a 5.3, is this impact part here. You know, practically speaking, these propagators are used, you know, most of the time, not always, but most of the time, with HTTP servers. And HTTP servers apply limits to the size of header values already. And so, because this CVE is about you know, large header values, or large, you know, baggage values, which are communicated via headers, resulting in large memory allocation. The fact that every server framework that already applies limits to headers dramatically reduces the impact of this.
For you to be impacted, you would have to, you would have to be using an HTTP server that did not have limits on its header values, or, you know, be propagating baggage outside of, you know, HTTP, so something like, you know, a message system or something like that. So that's a little bit of background about the CVE.
And, like, I guess… So, you know, we talked about this in Slack a little bit, and, you know, as a project, we have a policy that says, as a project, we have a policy… the project being OpenTelemetry Java, and I think this is also the policy of OpenTelemetry at large, which is, like, we backport, security vulnerabilities, CVEs, fixes, to, you know, the latest minor version.
And, you know, in the case that we would ever produce a new major version, you know, we're on 1.64, so if we ever want to to that X.
then, you know, we would also backport fixes to the latest major… n-1 major versions for some period of time. So far, that's been about a year, but we don't have… we haven't exercised that much, because we don't have major versions, at least in the core OpenTelemetry Java repo. OpenTelemetry Java instrumentation does have, Additional major versions, so they have a little bit more experience with that.
So, like, you know, besides the project policy.
You know, there's also, like, this practical policy, which is, like, we're very resource-constrained in terms of people. I've been trying to advertise for, you know, three plus years to get more reviewers, and we don't have many of them. And, you know, there's, you know, I would say one and a half maintainers. There's myself, and then John Watson, who's not on this call, who has, like, another full-time job, so he just moonlight So, in a very real way, we are, you know, people constrained in our ability to do the types of maintenance tasks like this that, that a properly staffed team could do. I would not characterize us as properly staffed.
So, so that's a little background where I'm coming from on this. I definitely hear your point of view here, especially with, like, this latest… the earliest version, 1.0 of MicroProfile being pinned to 1.0 of OpenTelemetry Java. I guess, like, what I don't fully understand and maybe it doesn't matter because of the things I just said, but, like, what does it mean for MicroProfile to pin to a specific version of OpenTelemetry? Like, why do they do that? That seems like a risky position in general, but I also don't understand, you know, the problem you're trying to solve by doing that.
Felix Wong 00:21:29 Right, so… so we have a micro-profile community, so more than, like, more than, OpenTelemetry, so we have, a lot of other specifications as well. So, we… we define a specification, so a lot of vendors, so they can opt in.
to implement those specifications so that, like, a customer, like, they have a micro-profile application, they can bring it from vendor to vendor, so they're not logged in.
to a particular vendor, right? So if they are with IBM, so they would like to switch to another vendor, as long as the other vendor implements the same spec, so their application is not logged in.
That's the rational behind us. I mean, why don't we specify a version of everything.
Similar to, like, the J2 Yigi, I mean, or the Jagata Yigi concept.
Jonathan Halliday (IBM) 00:22:26 Yeah, that's a little bit different, because if you think about something like Hibernate, which is a JPA implementation.
What a spec would normally do is specify what version of JPA, what version of the API.
And as long as you… had a version of Hibernate that implemented that, you can actually change the version of Hibernate, that's fine. You can ship a later Hibernate, as long as it keeps implementing the same version of JPA.
And similarly, you know, Hibernate is a superset of JPA, and you can ship.
Felix Wong 00:22:57 Right.
Jonathan Halliday (IBM) 00:22:57 technology than is supported by the spec.
And that's also fine. Users just can't use it in a supported fashion. They have to be willing to, you know, cast to hibernate specific APIs to do that.
And I think for OTEL, in my view, it's implementing the same API, right?
As long as there's no API breakage, why can't you ship a later hotel?
Felix Wong 00:23:20 Yeah, but I think the problem is, I think we all… I mean, if we're jumping from 1.19 to 1.64, like, that would be a huge jump with a lot of new… things, and then some of the breaking changes as well, I think, like.
Jonathan Halliday (IBM) 00:23:34 The new thing's not…
Jack Berg 00:23:35 There are no breaking…
Jonathan Halliday (IBM) 00:23:36 Right? The question is, for the old things, is the API the same?
If you've got code against the old API, will it compile against the new JR? Because if it does, you haven't got a problem.
Jack Berg 00:23:49 There are no breaking changes to the API, so by definition, yes.
Jonathan Halliday (IBM) 00:23:55 Yeah, so I don't see…
Felix Wong 00:23:58 Yeah, some of them were, like, from, like, incubating, like, to stable.
Those might be…
Jonathan Halliday (IBM) 00:24:05 getting more stable, oh, my breaking heart, you know?
That's a good thing, ship it!
Jack Berg 00:24:14 There are API additions. There are no AP… there are no breaking API changes, and, you know, we test this on every single release. We have a tool called JAPI CMP that, you know, programmatically verifies that our API is back and forth.
Felix Wong 00:24:29 Yeah.
I understood that… that you guys have resource constraint, and then I… I also like coming from… because, like, from us, no customer will buy our product if we have a CVE in it, right? So… what if we contribute to backporting, I mean, APR, to, like, the corresponding versions that we wanted to? Maybe you guys can, like, help us do the code reveal and publish it?
Jack Berg 00:25:00 Exactly.
Jason Plumb 00:25:00 The problem is…
Jack Berg 00:25:02 Rakuten.
Jason Plumb 00:25:03 Yeah, I mean.
Jack Berg 00:25:03 There's no benefit that you could have to contributing the back port. Like, it's maintaining the tooling and executing the tasks.
And, like, you know, all the tasks that are meaningful would have to be done by maintainers, and it's really about, like, precedent. Like, if we do this once, are we going to do this every time, like, where do we draw the line on which minor versions we backport, CVE fixes to?
Jason Plumb 00:25:35 That was gonna be my point, Jack, is, like, the future of every CVE that might be coming out.
Patched into every prior version of… the APIs is just not feasible, right? So, I understand one vendor may be picking and choosing their favorite ones that they've pinned to and wanting to bump that up, but just from a project standpoint, it's really not sustainable to try and do patches for every… or a large set of previous versions.
And if we don't do it for one of the versions, the question is, why not? Some other vendor might use that too, right?
Jack Shirazi 00:26:11 I… I don't understand why… MicroProfile doesn't just fork that version.
And do it themselves.
Felix Wong 00:26:22 I mean, we can, I mean, definitely, I mean, but I think if… we can work with you guys, and you guys can publish it officially. That seems, like, more legit, I mean…
Jason Plumb 00:26:34 There's third… effort taken to not have breaking changes, and to stay in the 1.x release line, and that should be sending a message that, I mean, a lot of effort has been put into not having breaking changes, so I would consider I mean, I know that you have considered, the jump there to 1.64 or 63, wherever we're at now.
And evaluating if that's actually too big. Like, have you identified specific things in that jump from your earliest version to 64 that are problematic?
Felix Wong 00:27:10 Right, so we have not actually tried the, I mean, like, switching from 1.19 to 1.64, but I think the fact that, like, from 1.19, we only have traces, and, like, 1.64 have metrics and logs, right? So… That seems to be exposing extra features that we don't support in backend 1.19.
Jack Berg 00:27:37 But what I want to push on is microprofile is a specification.
there's a specification, and the specification has bound itself to the, let's say, 1.0 of the OpenTelemetry API.
Why can't the implementation of that specification use a version of the implementation of the API that is backwards compatible with 1.0, and which has the backported fix, or which has the CVE fix?
why can't all the vendors… like, a specification is just a bunch of lines specifying, like, what you need to do in order to be compatible with it, you know, an API definition.
It shouldn't matter that the specification has an API dependency that has a vulnerability in it. It should matter what the implementations are bringing in, which version of the implementation of that API the MicroProfile implementations are using.
Right, right.
Felix Wong 00:28:41 I ain'.
Jack Berg 00:28:41 that.
Felix Wong 00:28:42 I totally, I mean, I agree, I think, like, what you're saying, but I think, like, most of these are, like, open source, right? If you, on a particular minor version, right, or, I mean, basically, they're normally keeping similar functions with similar capability.
Right, so once you bump up, like, a… a, major version, right, you expect breaking changes and new features and something, right? So, but I think for… like, for OpenTelementary Java, we have been adding new features without bombing the, like, the, major versions, right? So, we keep adding stuff to the same 1.
Jack Berg 00:29:27 I think we have a different idea of what semantic versioning means, so I don't think there's any problem with adding new features and minor versions, so long as you don't have breaking changes.
bumping major versions every time you add a new feature has issues of its own. It signals breaking changes that wouldn't be happening almost ever.
So we, you know, we'd… and, you know, think about it if we had done that type of thing. We'd be on major version 64, and or something akin to that, and we'd have… we'd have a real problem deciding which major versions to backport CVE fixes to.
Felix Wong 00:30:07 Okay, so seems like we don't have a, like, a, a way to solve the problem right now, right? So, we'll… Will Yuf… I think it's… if we fork it, and then fix it ourselves, so… would that be a okay approach, if you guys…
Jack Berg 00:30:34 What are you guys mean, then?
I have no problem with a fork and a fix, so also, it's just like, we're missing several of the maintainers today, so, I think… I think you should take what I slash we are saying with a grain of salt, you know, I don't necessarily represent the consensus opinion of everybody. For the consensus opinion, I think the best way to get that would be to open an issue on GitHub. And the issue is really about, like.
a policy. Like, what you're doing is you're requesting an adjustment in policy about you know, are about backporting CVE fixes and minor versions. And the question that you have to address with that sort of policy change is, like, when and why? Because it's impractical to backport a CVE fix to 64 minor versions.
We're not gonna do that, and so is it upon request? And, you know, where do we draw the line for requests? So, I would recommend… like, I can't say that this conversation here is, like, the end-all, be-all. I think some of the maintainers would probably agree with what I'm saying, but it's… it's worth opening an issue just to sort of Codify or clarify, you know, the result of this.
Felix Wong 00:31:59 Okay, yep, sure, I can do that.
Jason Plumb 00:32:02 Felix, I'm sure that MicroProfile also has a similar… challenge with its, users, that if a problem is found, and you… and they raise it to you, that you also probably don't go back and patch every single version of MicroProfile.
Felix Wong 00:32:21 we… do, actually. I mean, for… especially for IBM products, we have a, zero migration policy, so… and as well as we don't…
Jason Plumb 00:32:33 pepper cake.
Felix Wong 00:32:33 Features, yeah, so we go back to… Do everything, yeah.
Jason Plumb 00:32:37 Okay, that… that is exciting to hear. I… I did not expect that. Okay, that… that gives me a better understanding of, yeah, that challenge, that if…
Felix Wong 00:32:48 Yeah, so…
Jack Berg 00:32:49 Every major version, or every major or minor version?
Felix Wong 00:32:52 No, we support, I think, up to 2 years.
Like, all the… we have a release every quarter, like, yeah, we provide them support up to 2 years.
Jack Berg 00:33:03 Every minor version.
Jonathan Halliday (IBM) 00:33:04 Only on the latest quarterly release.
Right. If someone finds something in a release that's 6-month ill, the answer is upgrade to the 3-month one.
Jason Plumb 00:33:13 Exactly. That's what I… yeah, so that's kind of the… that's where I was expecting that conversation to go.
Felix Wong 00:33:19 No, we have a full long-term support, release every year, so we're back porting, like, fixes for, like, I think 8, 8, LTS versions.
Jack Berg 00:33:31 So you specify certain…
Jonathan Halliday (IBM) 00:33:32 Only the tip of each other.
Jason Plumb 00:33:33 Yeah, RTSs, yeah.
Okay, thanks for clarifying that.
Felix Wong 00:33:38 Yep.
Jack Berg 00:33:39 Yeah, so essentially, like, what… what our policy is, just in the vocabulary of MicroProfile, is we have one LTS version.
No, multiple.
Felix Wong 00:33:50 Okay.
Jack Berg 00:33:51 I'm not saying, like, it just is what it is right now, and so that, like, that's why an issue is, you know, useful, because it can, like, clarify it. And, you know, part of a policy might be, you know, decisions on backporting based on the severity of the CVE.
like, maybe there's a threshold after what you backport, or maybe there's, you know, certain pinned minor releases that we could backport to. I'm not exactly… there's a lot of different shapes this could take place, or this could, like, you know, manifest with, so… Let's talk them through.
Felix Wong 00:34:24 Okay, sure. Hey, thanks for your time.
Jack Berg 00:34:27 Thanks, Felix. Sorry that it took so long to get to your topic.
Gregor…
Gregor Zeitlinger 00:34:43 Yep.
I just wanted to raise awareness that, we have a couple issues in contract that are, required, until we can move forward with 3.0, meaning that if we don't, then we cannot update the contract.
And I have, worked on both that I'm aware of, but I think, We should, track that somehow, creating milestone or label, I don't really care, but… In mentioning it here, I make sure that you're also aware of it.
Jack Berg 00:35:22 But, so it's a… it's a contribib issue that is, is dependent on features that will be gone in the next version, in the 3.X version of the instrumentation?
Gregor Zeitlinger 00:35:36 Right. So, to put it in simpler words, it's using features that will be removed in 3.0.
Jack Berg 00:35:43 And is it, like, the cyclical thing, where, you know, the… some… we have some contrib packages that are actually bundled in with the Java agent? And so, you know, in the past, I think we've… You know, it's like… how does it work? It's like the…
Gregor Zeitlinger 00:36:01 No, it's… it's not a… it's not a problem where we have to, Sync it in one release, because we already have replacements available.
That have just been published this week.
Jack Berg 00:36:13 Okay, so it is just a matter of… updating the code to use the new APIs that are available in the latest published version.
And getting those incorporated and published in Contrib.
So, so is… did you say that there's a PR for this?
Gregor Zeitlinger 00:36:36 I have, two PRs, but they are, stacked.
Jack Berg 00:36:41 Okay.
Well, if they need additional reviews, I'm happy to lend some eyes, just to help them move forward.
Gregor Zeitlinger 00:36:51 I'm not sure if a milestone would work, since we have a different numbering scheme.
But I can create a label, is that…
Jason Plumb 00:37:02 I don't… yeah, I don't think we use milestones and contribute, do we?
Gregor Zeitlinger 00:37:06 I can select some, but maybe it's only outdated ones.
Yeah, yeah, they're… they're older.
Jason Plumb 00:37:14 Okay.
Jack Berg 00:37:17 Who's been releases for Contra lately, it's you, Jason, right?
Jason Plumb 00:37:21 Jay. No, Jay's been doing it lately.
Jay DeLuca 00:37:25 I think Trask did the last one, but yeah, other than that, I think I did the others.
Do we want to…
Jack Berg 00:37:31 this… I guess whatever the mechanism, it's just whoever's gonna… doing the release should just be aware of it, so that they don't jump the gun.
Jay DeLuca 00:37:40 Yep.
Gregor Zeitlinger 00:37:45 Okay, I'll create a label then for those, pRs and issues.
Jack Berg 00:37:51 And can you tag Jason, Jay, and Trask in, like, in a Slack conversation, just to inform them of it? Just… whoever are the people that could be actually running the release, just so they're aware.
Gregor Zeitlinger 00:38:04 Yeah, I'll put it in our back channel.
Jack Berg 00:38:07 Okay.
Jack Shirazi 00:38:08 associated to… what Gregor's working on there.
but not dependent on it is, there's an issue that Jason raised in the spec… about declarative config for op-amp.
And I'm just wondering, what's the process for that? Is that… is the spec that you raised, Jason, is that where we decide on the declarative config, and then… We try and promote that into a development version.
Jason Plumb 00:38:43 I think so, I mean, I stopped looking at that because it kind of fizzled out, but yeah, it's this one.
Jack Berg 00:38:53 So, so just to kind of… put my config maintainer hat on. So, In the config repo, we generally don't make decisions about, like, concepts.
Like, we don't want to introduce a new concept, we just want to codify a concept that is specified elsewhere into a schema.
Right? So, like…
Jason Plumb 00:39:20 because they're not That's what this was doing, right?
Jack Berg 00:39:23 Well, so the thing, and this is sort of my last question here. So, like, somebody is suggesting a potential schema.
what happens when this is specified? Like, what is the expectation of what an SDK does when this is specified? And where is that expectation actually discussed in a spec elsewhere?
Jason Plumb 00:39:43 I see what you're saying. So there's a bridge that's missing between the schema and the implementation. Like, that's the thing that needs to be specified.
Jack Berg 00:39:50 Right, like…
Jason Plumb 00:39:52 Okay.
Jack Berg 00:39:52 Yeah, and like, I…
Jason Plumb 00:39:53 Because op-amp is certainly a spec, right? Like, all of these things exist in the op-amp spec, too, right?
Jack Berg 00:39:59 Right, and so when this… when this exists, like, let's say this gets added to the declarative config schema, and I go and try to implement that, and it's like, okay, I now see this, like, in YAML. Yeah. Like, what do I do with it?
Jason Plumb 00:40:12 Yeah.
Jack Berg 00:40:13 I just, like, start an op-amp client, and what do I wire it up to?
Jason Plumb 00:40:17 that endpoint.
Jack Berg 00:40:19 But, like, what does it have a reference to? Like, what can it manipulate by having, like, a connection?
Jason Plumb 00:40:25 No, I understand where you're coming from, Jack. I think that is… I think that is a valid gap.
Jack Berg 00:40:32 And, like, I'm all about this. This, I think, makes sense. It's just somebody needs to describe those semantics.
Jason Plumb 00:40:41 And that needs to be in the op-amp spec, or the main spec? Like, where does that live?
Jack Shirazi 00:40:46 So, the thing is that the op-amps there is defining a component that is used by other components.
So I guess that's similar to a processor or a sampler.
It's not something that you just create… And it works on its own, because by itself, it doesn't do anything.
Jack Berg 00:41:14 Yeah, and so I guess, like, that's the same thought I have. So the contract of, you know, the declarative config is you give it a model, which might include content like this, and out comes an OpenTelemetry SDK instance.
Which is a composite of propagators, meter provider, logger provider, tracer provider. Like.
I don't know where OPAMP fits into that contract. Like, I don't know, like… what I'm expected to give op-amp when I initialize a client instance with this config, or, like, if I'm supposed to return it, if it's supposed to be part of this composite OpenTelemetry SDK instance. These are just, like, questions that are ambiguous.
And as for where it lives, like, the main spec or op-amp spec, I'm not quite sure, I think.
I think I would lean towards, like, the main spec, some sort of… because the main spec talks about the things that op-amp might manipulate, and so, like… It could go in either place. I'm sort of unopinionated, but if I were to just put my finger in the wind and just give my, like, gut reaction, I would say the main spec, but I sort of don't care, it just needs to live in a spec.
Jason Plumb 00:42:36 Yeah.
Yeah, this touches a little bit on a separate issue I raised in the contrib repo on the op-amp client about, like, wanting some SPIs. Because, like, what you're describing is that, yes, you have this, like, op-amp client, and if you just do this bare minimum declarative config, like.
Maybe you spin one up, and the side effect of spinning one up is that you have a connection to a server, and that's maybe about it. It doesn't actually impact the runtime at all.
The other issue I raised was, like, there need… like, the client, the actual Java implementation.
outside of the actual op-amp spec, could use some SPIs for plugging into the various things that you can do using that protocol.
And right now.
the way that you hook into that is just by building the entire callback implementation. I feel like there's a way to make that more modular, but anyway, the fact that it's, like, bridging implementation that actually does stuff with the declarative configuration that shows that a client should be spun up at all. I think there's… so…
Jack Berg 00:43:38 The words are missing. The SPI would be a cool thing. It would, like, generalize it, and, but, you know, even setting aside, like, generalization, it's like, what is the… what's the base expectation about how an op-amp client interacts with the SDK?
Jason Plumb 00:43:55 Hell yeah.
Jack Berg 00:43:56 if that was present in a spec somewhere, what we could do is we could promote op-amp implementation from contribib to the core repo. Like, that's another practical thing that makes this hard, right? Is, like.
You know… This is a top-level entity, like OpAmp. It's a peer of, you know, meter provider, tracer provider, logger provider. Like, I don't know how to make that pluggable, where, like.
to, you know, do something and contribib with this top-level entity. Like, that's missing as well.
So, it'd be beneficial if OpAmp lived in the core repo, you know, if we're gonna have a top-level op-amp.
type in declarative.
Jason Plumb 00:44:38 Yeah, yeah.
And, I don't know, if it becomes more important, maybe we consider promoting that one day, but I think it's premature now.
Yeah, all of the… all of the exciting stuff that falls out from, like, Remote Config, I mean, as Jack has been… Jack Shirazi's been dealing with for a long time now, is, like, just so challenging. I just wish we could keep a stateful system. Stateless system, but, you know… There we are. I think we got onto this through the config.
3.0 breaking change, because it's around the declarative config props, and… it's not… I mean, it's not directly related, because that is just an issue that's floating out there, right?
Jack Berg 00:45:26 Yeah, I want to say it's like a dead end.
That was Shirazi.
Jason Plumb 00:45:32 Go ahead.
Jack Berg 00:45:32 Sorry. Now you.
Jason Plumb 00:45:35 There… so, I think, Jack Shirazli, the reason you brought this issue up in the first place, based on our conversation about that contrib, and the 3.0 declarative config props, is because this is kind of, like, one example, and there's stuff in the dynamic control module that uses declarative config and config props, is that right?
Jack Shirazi 00:45:56 Yeah, this isn't a blocker at all, it's just, it occurred to me because I have to support op-amp configuration, and at the moment it's using properties.
And I was wondering, yeah… So, yeah, it's… it was a good time to discuss it, but I don't… it's like Jack says, there's… I think there's a specification that we need to complete, and how it's handed off to something.
Jack Berg 00:46:28 Yes, and I know…
Jason Plumb 00:46:29 Challenges that…
Jack Berg 00:46:29 can feel daunting, to… to go do, but, like, so, and Jason, I know you said you thought that this issue fizzled, so, like.
there's people that are interested in this. The fact that, like, 4 or 5 unique people are commenting on this, that's a really good signal that people are interested in this topic. And, like, what I would encourage you to do is, you know, select somebody that is motivated enough to go roll up their sleeves and do the spec work, and form a little coalition where you get the other people that are interested, to contribute to that spec work, to be the ones that are actively reviewing it, commenting on it, and giving it their… their gray checkmark approval. That's the best route, I think, to actually making this happen in the spec.
Jack Shirazi 00:47:16 Yeah, and that's gonna be… that's gonna be Elastic. My colleagues are the one who pointed out that you'd raised that, because we have to implement RPAMP across the languages.
Jack Berg 00:47:29 Yeah, and Jack, I think you… you have, like, your… the dynamic config spec PR that's been open for a while, and it's like, I really like the content there. I like your… like, your prototype implementation in OpenTelemetry Java, and, like, you know, it's got thumbs up from me, and it's just… We need more folks, and so, like, that's where, like, coalition building is, like, you know, a useful thing to do. Find like-minded folks and get them to, like, you know, just back-channel them to go and review and approve the PRs.
Jason Plumb 00:48:00 Yeah, the reason why I raised this, I think, in the first place is because I was thinking about this, and… We're building stuff on OpAmp, too, and if we want to support declarative config for this, we have to have this schema structure defined somewhere, and if we end up doing it different than Elastic, different than New Relic, then we've got a problem on our hands. So the idea was to try and at least lock in the schema. That was kind of the intention of that issue.
And… Yeah.
Jack Berg 00:48:30 Yep.
I understand.
I wanna see this.
Yep.
Speaking of declarative config, do we have any more comments on that? Do we want to move to the next issue, which is mine?
Jason Plumb 00:48:51 I'm good.
Jack Berg 00:48:53 Okay. I opened a P… Great, thank you.
I opened a PR to, OpenTelemetry Java Core, which does an interesting thing. So, Right now, we have all these generated models in declarative config, and they're generated from the JSON schema, and there are certain stable types which reference experimental types.
And an example of this is the top-level OpenTelemetry configuration model references the instrumentation model, which is in development. And so that's a problem for stabilizing this stuff. We can't have stable types referencing experimental types.
And so, I have a PER, which attempts to unwind this and, like, you know, separate them, and so that you actually can only access the in-development stuff through internal packages.
And so, you know, what we end up with is something like this, where, you know.
the OpenTelemetry Configuration Model… now only has public APIs for all of its stable types.
And, like, you'll notice that instrumentation is not in here anymore, so even though instrumentation slash development is a experimental property on this, it doesn't appear in this class at all.
And so, the way that you would interact with that is there is now, for every type that has properties that are experimental, there is an accessor class, and so… There's an… Open Telemetry Configuration Model Accessor.
This is in an internal package, and this allows you to get and set the experimental properties on that otherwise stable type.
So… That's a thing. That's, that's a useful thing.
The other thing that we have a problem with is, like, hey, what happens when we stabilize, a experimental property? So, like, what happens when we go and do something like this?
Will this work?
No, it won't let me do. Just mark down in here.
But we go from, like, instrumentation, development… Foo.
And then in some future version, we just, like, the property name changed, the instrumentation property is now stabilized. And, you know, the… The implementation in OpenTelemetry Java expects to see this without the development suffix, but the user's YAML looks like this.
And that's… that's terrible if that's, like, a breaking change for the user. We want to ideally warn the user that, like, hey, this property has been promoted, let's continue to accept this as configuration.
And not just, like, silently fail, right? So, I solved that, and now, like, every time… suppose we get in this situation, every time we ask for a property, instrumentation, for example, here, the internals will say, like, hey, did the user specify instrumentation or, instrumentation slash development?
And so we'll, like, you know, append the development suffix and say, like, hey, did the user specify that?
And if they did, then we'll, you know, use that instead, and we will… we'll warn the user. We'll emit a log warning that says, like, hey, this property name was promoted.
And the reason I am bringing this up at this SIGS, because, Gregor, I know you have been doing a ton of stuff in the instrumentation module, and instrumentation related to this, and I'm wondering if, If we need to do anything on the instrumentation side to do a similar thing, where, you know, whether a property… when a property is promoted from experimental to stable.
You know, mechanisms to ensure that users presenting the old experimental version continue to function.
And they don't break.
Gregor Zeitlinger 00:53:18 I think the answer is yes, What is the right level where this should live?
Jack Berg 00:53:30 Exactly, because… and this, I think, is what you're getting at, like, most of the stuff in the instrumentation module is built on top of declarative config properties, so…
Gregor Zeitlinger 00:53:39 Right.
Jack Berg 00:53:39 If the implementation of declarative config properties can seamlessly do this, like, behind the scenes, then you might get this for free over an instrumentation.
Gregor Zeitlinger 00:53:49 Yeah, I think this, would be ideal.
Jack Berg 00:53:54 Okay, so… I don't… so, basically, I wanted… I wanted just to, like, you know, inform, right, and say, like, hey, I haven't done this yet, where this works seamlessly for declarative config properties, so, it won't work there yet, but it could. It could… the same concept could be made to work there, and it's just, like, a matter of doing the implementation. And I guess, like, once I did the implementation.
I would want, sort of, you to fact-check it, and I guess, indicate that it solves the problems in instrumentation.
Gregor Zeitlinger 00:54:29 Yeah, we have many tests, so once we add those tests, then I think we can be fairly sure that it works across the agent and also across the Spring Starter, which has some custom code in that area as well.
Jack Shirazi 00:54:47 So this also has an impact on the callback that I was adding.
To the config provider, because that's got a path Where you're registering for callbacks, and if… If that needs to be transparently… Handling slash development, then it needs to… It needs to implement the callback twice for every… anytime there's a path that includes development, it needs to include the non-development path.
Automatically.
Jack Berg 00:55:20 Something… something to that effect, right? So,
Jack Shirazi 00:55:22 Okay.
Jack Berg 00:55:24 And I get… there's probably some implementations in there, Jack Shirazi, about, like, you know, if the… you know.
if the property is originally, you know, this, then maybe you only watch that. But if the property is originally, you know, the stable version, then you only watch that. Like, should you… should you watch for both, or whatever you originally observed? I don't know.
It's just a kind of silly sort of implementation question.
it can be hashed out. But yeah, I think this is something we should consider throughout the stack of, like, everything that depends on declarative config. It's like, you know, properties will be promoted from experimental to stable, and we need mechanisms to be able to have, like, a seamless user experience when that happens. And seamless user experience means it continues to work, and you log a warning message that, like, informs the user of what's happening and encouraging them to upgrade.
You're muted, Jack.
Jack Shirazi 00:56:30 Is it always slash development? Is that the only… Supported experimental option.
Jack Berg 00:56:37 Yeah, for now it is, and that's codified over in the schema itself.
So… If that ever changed.
Or maybe it's inversioning. But if that ever changed, things would have to upgrade, but… Oh, okay. So experimental properties are denoted by development alpha, beta, but in practice, we've only used development, but I guess while we're building this… these mechanisms, we could just make them future-proof by looking for any of these suffixes.
Yeah, anyways, this was just kind of an inform, because this is a big PR I don't expect most people to look at,
Jason Plumb 00:57:24 Jack, I was gonna… I was gonna bring this up, but… I had this moment of, like, introspection, like, a week or two ago, and I was talking with Robert on my team, and I said, anytime there's a declarative config PR, I just kind of get sad, because they're always over 5,000 lines.
Jack Berg 00:57:39 Wait, check this out. They're not always, but the recent slew of them have been, because they're all related to changes in the generated pojos.
Jason Plumb 00:57:48 Yeah.
Jack Berg 00:57:48 So, like, you change one line of, like, code generation logic, and there's.
Jason Plumb 00:57:52 Yeah.
Jack Berg 00:57:53 generated POJOs, so you touch 100 files.
Jason Plumb 00:57:57 it wasn't.
Jack Berg 00:57:57 So.
What you need to do, like, is, like, filter down to the actual meaningful changes, like, in this case, like, the meaningful change, and I'm not trying to defend this too much, but, like, the meaningful changes are to the generator, like.
And, you know, this is, like, 248 lines of code, which changes how the models are generated.
And then you find some, you find some samples of the models to see if you like the output.
Jason Plumb 00:58:25 So, on this topic, one thing that we went back and forth a little bit recently on Android, because Android now has its own federated semantic conventions, and we're doing code generation with Weaver for that stuff.
is we, we talked about it, and we flip-flopped a little bit, and we chose now not to commit those generated sources to the repository. They're purely a build artifact.
And that avoids this large PR problem. I mean, it helps with that. The downside is…
Jack Berg 00:58:55 It hides it.
Jason Plumb 00:58:57 It does, yeah, it's much harder to see what the actual code is doing from the templates, but at least, you know, it does solve A couple of problems like that, as far as, like, quantity or size goes.
Jack Berg 00:59:09 Yeah, and that actually was originally the case for declarative config Java, that they were in a generated package, and they will publish them. They're part of the things that we publish when we go to Maven Central, but, they… you don't see them in PR reviews, and, like.
I think there's trade-offs. For me, for me, because these are going to be part of our stable API, it's really important to see, you know, the exact details of what's being committed to source code. The exact, like, API contract, the exact implementation, Yeah, and the analog.
Jason Plumb 00:59:50 I get it.
Jack Berg 00:59:51 describing is semantic conventions Java, right? So, like, every time we Every time we upgrade to a new version of semantic conventions, we see.
Jason Plumb 00:59:59 Yeah.
A thousand lines, yep.
Jack Berg 01:00:03 Let's see. This is… Would this be it?
No.
Jason Plumb 01:00:08 That's release prep.
That's changelog.
Jack Berg 01:00:15 Who actually did that?
the upgrade.
Does it get, like, bundled in with one of these… Upgrade all… update all patch versions.
Jason Plumb 01:00:25 That would be funny.
DavidGrath 01:00:27 Number 518.
Jason Plumb 01:00:34 Which one, David?
DavidGrath 01:00:35 518, I think.
Jack Berg 01:00:38 2018, okay, you're… You're being helpful. Thank you.
I realize as I'm doing this, this is a silly way to do it.
Oh, this one actually wasn't too bad. Right.
Jason Plumb 01:00:53 Right, but it is the same point, though.
Jack Berg 01:00:56 Right.
Jason Plumb 01:00:57 Yeah.
Jack Berg 01:00:58 getting generated.
models is… Makes for big diffs.
I do hope they'll stabilize. So, I said this here, and, you know, hope springs eternal, but I said that, like.
This is the last time.
Jason Plumb 01:01:17 Yeah.
Jack Berg 01:01:20 You know how that goes.
Anyways… That's my topic More to come.
Any other conversations or topics people want to do before we… before we end?
Going once, going twice.
Alright, let's end a little bit early. It's nice to see you all. Thanks for the discussion.
See you next week.
Jason Plumb 01:01:52 Figure.
