SIG: Semantic Conventions SIG
Date: 2026-10-12
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Serkan Kenar** 00:35 Hello.
**Christophe Kamphaus** 00:38 Hello.
**Serkan Kenar** 00:39 Christian.
**Liudmila Molkova** 00:52 Hello, hi everyone.
How was the.
The summit observability summit. Right, Christoph, you've been there.
**Christophe Kamphaus** 01:44 Yeah, it was really nice.
I met several people.
It's always nice to talk with everyone that you otherwise only see online.
**Liudmila Molkova** 01:58 Right.
Any cool talks?
**Christophe Kamphaus** 02:05 Yeah, I talked with Severin about some infrastructure for observing the CICD infrastructure of OpenTelemetry.
**Liudmila Molkova** 02:17 Hmm, right.
We've had a widespread problem of, like.
Queuing jobs, it would be very handy.
**Christophe Kamphaus** 02:26 Yeah, and also to make it, publicly available.
**Liudmila Molkova** 02:32 Oh… Like, for example, as a part of the demo.
**Christophe Kamphaus** 02:37 No, that we would have… the hosted infrastructure from OpenTelemetry, and we would show our own CICD metrics and, observability data.
But yes, the question there is, which backend do we want to show?
Since we don't want to favor one vendor over another.
So that's a question for the governing committee to solve.
**Liudmila Molkova** 03:14 Yeah, it's a good one.
**Christophe Kamphaus** 03:23 If you want, I can drive the meeting.
**Liudmila Molkova** 03:28 Yeah, thank you.
**Christophe Kamphaus** 03:43 All right, let's start with some triage.
Otherwise, looks like this one needs some more review.
It's this one.
Needs review specifically from, charlene.
We have here a few.
Does that look like they need a second approving?
**Liudmila Molkova** 05:18 Yeah, I'll add this to the agenda.
Oh, should we…
**Christophe Kamphaus** 05:23 Get with later, son.
**Liudmila Molkova** 05:25 Yeah.
**Christophe Kamphaus** 05:41 Okay, here's another one that needs a second review.
Oh, I put that one on the agenda later.
Is this one ready to be merged?
**Liudmila Molkova** 06:11 I think we wanted the order to maybe add another follow-up, or say that it's a separate PR, so there is an open discussion.
**Christophe Kamphaus** 06:22 Okay.
I think that's all of them.
There's nothing to be ready to be merged.
Okay, this one was almost ready, but I saw there's a last minute Question.
Okay, so I'm… Let's wait before we merge that one.
Oh, yeah.
Okay, I think we are… That's the time box for triage.
And let's get to the agenda.
Sven, are you here?
If not, we can get back to it later, if he joins afterwards.
I put this one the agenda. It was about A follow-up to this one.
In this PR, Ricardo defined… alignment between metric and span attributes.
But it left a lot, to be defined when it comes to How to define metric conventions and I took A stab at, flushing that out.
So I based myself on his PR.
And I… Had a question here to the group.
Should we merge both together?
Or… Is it fine to merge Ricardo's PR first, and I would then retarget mine to… Auto Main.
**Liudmila Molkova** 08:54 Mmhm.
What?
I said this is like a general guidance, right?
**Christophe Kamphaus** 09:02 It talks how to write conventions.
The section around metrics.
**Liudmila Molkova** 09:09 Yeah, I mean, like, the text here is… Very generic.
**Christophe Kamphaus** 09:16 Yeah, I… I put it under its own section here.
Oh.
around metric attributes.
**Liudmila Molkova** 09:33 Do you think like you you probably spend most time with it? Do you think there is something in the first PR that's not in your PR?
**Christophe Kamphaus** 09:43 No, I, I completely took over what he wrote around.
span and metric attributes, relationships here. That's, his part.
And I just flashed everything else around it like symmetric name unit.
When it was defined in other parts of some conf docs, I just linked to it, like here.
So we don't have duplicate guidance.
And it… pretty much follows also the structure we had for Spence.
**Liudmila Molkova** 10:26 Nice.
What's your preference?
**Christophe Kamphaus** 10:36 I'm fine with ISO.
If we put mine… towards Maine.
It would include also Ricardo's. Okay, yeah. If we changed it to main, it would also include his commit.
I guess for readers of some conflict would make more sense to.
Just have everything together, because here… Yeah, it's not nice to have a… to be defined and send… As this guidance without any context.
But I think this is ready to be merged, just for this part.
I think here's the deciding factor would be how close are we to another release?
**Liudmila Molkova** 11:38 We are overdue, I think 2 months overdue.
**Christophe Kamphaus** 11:40 Yeah, yeah.
So I would not release just this part.
I would rather see… The complete guidance around defining metric conventions.
When it's released.
**Josh Suereth (Google LLC)** 12:06 I think, Christophe, I really like what I'm seeing from what you wrote. I think it's better that we get the whole thing written.
So, I would say just target yours in Maine, because, again, it'll give, original author will get, you know, credit for the commit, because you pulled it in directly, and we've needed this for a while, so I think it's really good you wrote it, so let's just get it merged. I'd be happy to just review yours instead.
**Christophe Kamphaus** 12:33 No.
To be honest, I asked Claude to write it up.
But yeah, I reviewed it myself, and I made sure there's no… Duplicate content… In other parts of the conventions.
**Josh Suereth (Google LLC)** 12:50 Which Claude though? Because If you use Cloud5, I'm probably gonna have lots to say on it, because I have not found it to write human-readable docs at all.
Without lots of help.
But it doesn't look like Claude to me so far, so I'm guessing you didn't use just 5.0.
**Christophe Kamphaus** 13:11 No, it's 5.5.
**Josh Suereth (Google LLC)** 13:13 Okay, that one's slightly better, but still, I'll… I will do a thorough review for Claudisms and putting too much content in one sentence, which are the common things I think are really problematic.
**Christophe Kamphaus** 13:26 Okay, I'm looking forward to it.
**Liudmila Molkova** 13:29 Have unsloped skill in Semantic Conventions Genea repo.
And it's very helpful. I'm passively aggressively sometimes asking people to run on slopeskill on what things and.
**Josh Suereth (Google LLC)** 13:42 This is one of those things where I tend to have Gemini go fix the documentation for Claude, and I bet if I had OpenAI, I would do the same.
Because having Claude figure out what to write, and then having something else clean it up, and then you going and doing the final cleaning seems to be faster than writing it all from scratch. But, man, I don't know if you've seen Claude 5's output, it's… it… I would ask no one to give us PRs from Cloud5 that include documentation.
**Christophe Kamphaus** 14:20 Okay.
I will retarget it. And yeah.
Hopefully it's not too bad.
**Josh Suereth (Google LLC)** 14:31 What I'm reading so far looks great, so…
**Christophe Kamphaus** 14:43 Next, Ludmilla.
**Liudmila Molkova** 14:47 Yeah, I… sorry for spamming, but I've sent a bunch of PRs, yeah, assisted for the V2 migration for entities. We've merged some.
And we talked about it last time. There were a couple of development scenes.
So… the problem today, why do we need it, is because the entities we have today is… are not proper entities. They were initially… Are.
Created as resources, as groups of resource attributes.
And we are due to do something with it.
And some of them are pretty straightforward.
So, for example, there…
**Christophe Kamphaus** 15:38 Do you want to share the screen?
**Liudmila Molkova** 15:40 Yeah, thank you.
Alright.
I'm sorry.
Takes a moment.
Okay, so, for example, something like this is pretty straightforward.
So we have WebEngine. You can think it's straightforward, or not.
And currently, nothing is, marked as identity or description attributes.
And presumably Vampagen name is.
identifying.
Because version is not always available, and for example, for service, we only use name as identity.
So here, we also have the required attribute level on the name, which is good. In some cases, we can have it recommended, and I'm changing to required now.
Okay, so this is a few examples of straightforward, things.
So, for this one, Josh, you asked, and this is one of the escape paths we have.
We have Android NDT, and it's actually probably not Android, maybe it's Android OS.
But it's still kind of empty. It has just one attribute.
And from one side, it's trivial, it should be identifying, but maybe it shouldn't be an entity.
So Josh suggested in Escape Hatch that we call things that we are… that are not designed as entities as public attribute groups.
This would keep them documented, this would keep their past resource.
Story, and they could be converted to entities later, if it still makes sense, in whatever way possible.
So I'll probably do it for Android, because it's somewhat controversial.
So, the pass for converting to attributed groups, is… needs some, policy suppression, because we cannot just remove entity.
We can call it deprecated, but we would need to remove attributes from it then, or do something. So I would just propose to remove them.
There are no CodeGen and OpenTelemetry that generates code for entities, so even though we would break CodeGen if Somebody used it, we actually won't because nobody does.
Then the last, if we kind of agree with this part of the fix, the other step is to support suppression, and I have a couple of PRs that want to weaver packages to the policies where I'm suggesting how to suppress them, but I actually would prefer if I just did it in Weaver.
So like we have the suppressions for life checks in River config.
And we could suppress arbitrary policies there.
We are… more config.
Sorry, we would suppress check policies, the, the, some kind of definition time checks there as well.
If we… kind of agree on this direction, let's take a look at this PR, and once it's merged, or whatever we end up with merged, I would… I don't know, Rails Weaver, and we'll go ahead and start using them in Semantic Conventions.
There are more things to discuss, but I wanted to first check if there are any objections to converting things that are not designed as entities to the public attribute groups, and just removing the entities altogether, and suppressing the policy findings via whatever mechanism will decide.
**Trask Stalnaker (Microsoft Corporation)** 20:14 So the ones that you're proposing to convert to attribute groups are, Android and browser, anything else?
**Liudmila Molkova** 20:24 Oh, there's more, yeah.
Oh, wow.
Yeah, the Android browser, I… Haven't decided… For this difference, the AWS log, or… this AWS ECS.
We can talk about it, but essentially, we had, An attribute group that consisted of 3 entities.
So it was called an entity, and it had multiple… URLs.
So they are… this is effectively 3 entities.
And we can do a better job and split this up into three entities, what I have today, where we can postpone doing this and say, okay, it's an attribute group.
do whatever.
with it.
Well, maybe I'd rather still prefer to fix it, because having a public attribute group We would have to keep the compatibility with this public attribute group.
Because it's a contract anyway. So it's better to have somewhat reasonable entities than, the… Attribute group we know is to be wrong.
Yeah, I think the device, what was it?
The… the Android… the device… And… This friend are the 3 that would become.
Attribute groups.
**Trask Stalnaker (Microsoft Corporation)** 22:17 And… and browser?
**Liudmila Molkova** 22:19 Browser, yes.
**Trask Stalnaker (Microsoft Corporation)** 22:27 I'm… I'm good with it.
Makes sense.
**Liudmila Molkova** 22:36 Okay.
And then the… Another big question is the… the one you brought, Trask, is with renames.
So we have a bunch of, entities which… Don't seem to be… The name doesn't seem to be specific enough.
So, like, for AWS, it… EKS.
The attribute there and the cluster are an implied kind of cluster.
And so on, like, for… there's Fast Instance, and Heroku app, and so on, and the cloud resource.
test… Just needs a little bit more eyes on the review, but also this would follow the same pattern of, okay, we drop the old entity, we suppress the policy findings, we allow it because we know nobody generates entities.
And we proceed with then more or less trivial change.
And in most cases…
**Trask Stalnaker (Microsoft Corporation)** 23:52 Suppression… what's the suppression for in this case?
**Liudmila Molkova** 23:56 It's the same problem that we are removing the old entity.
**Trask Stalnaker (Microsoft Corporation)** 24:01 Oh, okay. Oh, I see, so that's what the… so there wasn't a problem with adding an attribute group, it's the… it's removing the old entity in either case, that's the suppression. Right.
**Liudmila Molkova** 24:14 Yeah.
**Christophe Kamphaus** 24:16 Yeah, and you suggest this instead of deprecating the old one.
Because nothing… Depends on it yet, so we can just remove it and create a new one instead.
**Liudmila Molkova** 24:29 Yeah, also, we cannot just deprecate it, because it will remain invalid.
In the new schema.
I would deprecate totally.
**Christophe Kamphaus** 24:42 Makes sense.
**Liudmila Molkova** 24:53 Cool. So… In general, I don't hear major objections.
Of course, we'll need to spend some time reviewing it, and I think the first step is to Figure out the suppression mechanism.
Josh, would you mind to take a look at the VIVA PR, or share if you would prefer it done any other way?
**Josh Suereth (Google LLC)** 25:19 Yeah, happy to take a look. I think I… Might have already commented on that one, but I don't. I don't know. I thought.
I approved one of your PRs over the weekend, but I don't know if it was that one.
So…
**Liudmila Molkova** 25:32 Might have approved… oh, no. So, I had another way… of… suppressing it in the policy, but I'd rather go ahead with the Weaver config.
**Josh Suereth (Google LLC)** 25:42 this.
**Liudmila Molkova** 25:42 because.
**Josh Suereth (Google LLC)** 25:43 Okay.
Okay.
**Liudmila Molkova** 25:54 Okay.
And then I would appreciate your reviews on this retrieval, guys, for now.
And… I'll try to get… some… Interest from Mindframes. People do really have vertigo here.
I'll put it under agenda or in the Slack channel.
Cool, so then this is the next step, and we'll move on from here.
Okay, and that's all I had about this topic.
Josh, you're seems to be the next one related.
**Josh Suereth (Google LLC)** 26:41 Yeah.
It's somewhat related. So we made some syntax changes to entities.
And, there is unfortunately a breakage. And the breakage is not in your definition of entities. It's actually in your templates, the template files. It doesn't break Semantic Conventions, but it does break Gen AI and it breaks Weaver packages. So I'm going to submit fixes to both of those.
What the change is, is, requirement level on identifying attributes is basically always required. We have a policy that will warn you if you ever make it not required for semantic conventions, so what we're doing in V2 is we're just removing the field.
as a field that exists. If you have it there, it gets ignored and issues a warning.
But the… it broke all the templates, because it's actually removed by the time you get to the template.
So I'm gonna fix all the templates to just basically hardcode that as required. We all know it's required. There's a policy that prevents it in SemConf, but it might break your template rendering.
when you pull in the new Weaver, if you're not part of our nightly test. So, I'm gonna go issue those fixes to the downstream, like, to Gen AI and to, Weaver packages, before we cut the next Weaver release, but just wanted to give a heads up that that was a… we did our best not to break anyone, and There is… Yeah, that's a fun one.
We could synthesize something if you want to have it there, as always being required, but I thought it's easier just to fix the two breakages, because most of the ecosystem's working.
**Liudmila Molkova** 28:19 We should, by the way, switch… Some come Gen AI too.
the packages.
Templates.
**Josh Suereth (Google LLC)** 28:30 Yeah.
Yeah, I think that was waiting for V2 to be fully rolled out everywhere, right?
**Liudmila Molkova** 28:36 I.
**Josh Suereth (Google LLC)** 28:36 Can we do it early?
**Liudmila Molkova** 28:37 you I think it can be done now. It's just maybe that… We need to make some decisions. Do we render registry of spends and metrics?
Maybe, yes.
**Josh Suereth (Google LLC)** 28:51 I mean, I'd say yes, but… Yeah, anyway.
If you want, I can make a PR for that as well, at the same time. Last thing I do want to add, because we talked about this in the tooling SIG, we're going to mark the V2 syntax as stable soon.
This Weaver, we're trying to get to a 1.0 of Weaver, where everything will be stable.
the V2 syntax being stable means you won't get a warning every time you pass dash dash V2. So, you know how we're moving to V2, and we have a warning, so we can… address things. With this final set of PRs from Ludmilla, if we agree on the approach.
we're going to actually commit to non-breaking changes from here on out. So this is, like, the last breaking change.
And then from there, we would not allow ourselves to make breaking changes at all.
So that is my hope for the next Weaver release.
Which I think would be pretty big.
**Liudmila Molkova** 29:50 Oh, maybe we will issue the Viva release for the small stuff, like, the suppression.
In the midway, like, the small feature, and…
**Josh Suereth (Google LLC)** 30:01 Yeah, we still have another two to three weeks before the Weaver release hits, so… Theoretically, because we just cut Weaver last week,
**Liudmila Molkova** 30:10 And it would be… it would be really nice to… Release the suppression.
As an ad hoc one, and then it will then block a lot of E2 stuff in Semconf.
**Josh Suereth (Google LLC)** 30:26 Okay. Do do you think that's something we should try to do this week? If so, we can talk about it tomorrow or on Wednesday.
**Liudmila Molkova** 30:32 Yeah, I would love to do this, and if we wait for the next Weaver release, I would then ask to do some mid… mid… term thing in the Viva packages.
**Josh Suereth (Google LLC)** 30:44 Okay. Yeah, I think, so all the breaking changes are done. Getting, getting that through this week actually would make sense. I just wanna make sure the Weaver packages and the SemComp Gen AI fixes are in before we cut the release because we, we have that break.
**Liudmila Molkova** 30:58 control.
**Josh Suereth (Google LLC)** 30:59 So that's the only thing blocking the Weaver release, is getting the upstream… because we can fix the upstream independently of the release, and then when the release goes, we won't break anything.
Good, Christoph.
**Christophe Kamphaus** 31:13 Yeah, I was wondering how… Where are we in the migration to V2 in all the models in GenAI and in the main SAMConf?
I'm just wondering… If that's pretty much complete, then we can be pretty much sure there won't be any more issues we would find.
**Liudmila Molkova** 31:38 So for Gen AI, we are… Done, we are fully on V2 there, and I think all the federated registries are… at least I hope so.
Where we are with some cons.
So… We have a couple of PRs, well, not couple, a couple of categories of the PRs.
So this friend, we need to follow up with mainframes.
Where, since they are federated repo now, maybe we just remove them?
I'll check.
In this repo.
So this is the bunch of changes for the entities without identity attributes.
I'll put… there are, I think.
There is a big, big one for databases, and there is a new feature in Weaver that would allow to migrate it better.
We can talk about this, but essentially, there are a few leftovers.
And then, the main interesting part that comes after that… so this, this will help us be done with this definition.
And it will… remove all the controversial parts in the definition. The rest of definition should not be controversial to migrate to V2 at all.
And it's not essential that we do this. Hopefully the resolved output would be the same.
Regardless.
But then, after we do this, we can start producing V2 output, and we can switch fully to V2.
And this is where we would… publish V2 schema.
So… The rest is, like, up to us how we do this, how we migrate, like, all the attributes from the groups and registry to the proper attributes, then all the definition files. We should migrate later.
So, it's still a decent amount of work, but it's the things that we prototyped for and kind of know what to expect.
There could be some minor issues with it, of course, but it's mostly trivial after we untie.
This ugly piece.
I'm, I'm kinda… Like, from subjective perspective, I think, for this definition, we are… We experienced a lot, and we kind of know What to expect as publishing, it's probably trivial.
But we didn't do it yet.
And I've heard client would do this, right?
They were going to publish something?
**Josh Suereth (Google LLC)** 34:44 Yeah.
There's a bunch of people trying to publish, yeah.
I mean, the… The thing that makes me not too scared about it is that the way that we change resolution is effectively we do a publish step internally on all of your dependencies. So if you have a dependency on Semconv, we basically publish it locally and then use it as a dependency, and that's how the new system works.
But There could still be some issues, so it'd be good to sort them all out.
**Liudmila Molkova** 35:17 The only piece I'm worried about is that if we don't convert all the, even if we convert all the semantic conventions to V2, like we need to make sure that the V2 we publish.
Not from the schema perspective, but from the content perspective, stays the same. Oh, stays compatible, right?
**Josh Suereth (Google LLC)** 35:38 Yep.
**Liudmila Molkova** 35:38 And.
**Josh Suereth (Google LLC)** 35:39 That's also a commitment we would make, yeah. Like, if we're going to make this V2 be stable, then the commitment would be we make non-breaking changes, so we have to be comfortable with what it looks like.
**Liudmila Molkova** 35:51 Right.
And then, what I'm worried that if there is some small issue, and we, I don't know, prepend dot in front of something, nobody will review the published schema, and it's megabytes of… barely readable text, so it's hard to review, right? So.
I… I'm thinking it does not block us from publish… from saying that the published schema in Weaver is stable.
But I would hesitate to say that we produce this, the schema we publish is stable from Semantic Conventions.
**Josh Suereth (Google LLC)** 36:32 Oh, I I see what you mean. Yeah, like this is the notion of you want to split V2 and or you want to split the experimental and stable pieces of the schema. Is that part of part of what you're saying, or is this different?
**Liudmila Molkova** 36:45 I would say that the Weaver, the published schema in Weaver is stable, and Weaver V2 is stable. We don't make breaking changes to the schema.
But we are not publishing Semconf's table.
Yet until we are more confident that the content we produce with Weaver V2 schema is valid.
**Josh Suereth (Google LLC)** 37:08 Right, yeah, so we would publish Semconf.
on the new schema somewhere, we would make sure Gen AI can consume it successfully and can work off of releases there before we would mark it stable in SemConf. Yeah, okay. Right. I'm in, that makes sense.
**Christophe Kamphaus** 37:25 Would that also include code generation?
**Liudmila Molkova** 37:33 E… It would include the river.
Schema that's used for code generation.
Right? But the cogeneration itself What does it mean to mark it stable?
**Christophe Kamphaus** 37:51 I mean, would C code gen consume V2 schemas?
**Liudmila Molkova** 38:00 Yeah.
**Christophe Kamphaus** 38:01 Yeah, so… If there were any changes in the schema, It would impact code, John.
**Liudmila Molkova** 38:09 Oh, yes. So the V2 PodGen Is.
Completely different from… well, not completely.
Quite different from V1 code gen.
I'm thinking if we have a migration guide, probably not.
Or a list of breaking changes.
I think we should have a guide, or at least we should list breaking changes.
Create an issue.
**Josh Suereth (Google LLC)** 38:50 We do in our change log, we list breaking changes, but.
**Liudmila Molkova** 38:55 I mean, comprehensive one.
To feed to your AI to do, to migrate Jinja files, to point it to the right place.
**Josh Suereth (Google LLC)** 39:03 Oh, about how to do Jinja files between V1 and V2. Yeah.
**Liudmila Molkova** 39:06 Yeah.
**Josh Suereth (Google LLC)** 39:07 I… okay, we should… we should actually just formalize the skill, because really, all you do is you say, hey, AI, here's the schema for V1, here's the schema for V2, go update this, and it just figures it all out. And you don't really need to give it anything comprehensive, but maybe if we had the comprehensive thing, it would use less tokens, I don't know.
**Liudmila Molkova** 39:27 I mean, even there's this comprehensive for AI, right?
And it's very helpful, otherwise it would be just doing it blind.
**Josh Suereth (Google LLC)** 39:37 Oh, I gotcha, yeah. Like, you don't want to just copy and paste the prompt I use, you want to actually have it as a formal thing, right? Yeah.
**Liudmila Molkova** 39:44 And yeah, and we can put it in the Weaver packages or something and link from Weaver.
**Josh Suereth (Google LLC)** 39:49 Okay, sounds good.
**Liudmila Molkova** 40:42 Okay, I can take it.
And.
I don't know why I'm presenting, but anything else on this topic?
**Christophe Kamphaus** 40:59 I can share my screen again.
So, I have one question around this issue.
It's about runtime.
Events, around which dependencies are loaded.
And the question was… What would be needed to identify a dependency?
So, for .NET… It was the package… Pearl?
Artifact Pearl.
But for other languages, That attribute might not be available.
So, the question was, what would be needed for other languages, like artifact name and version, or would there be other information available.
**Liudmila Molkova** 42:03 Is it… Like, what is the telemetry that's being emitted?
**Christophe Kamphaus** 42:10 So, the proposal is to emit an, load event.
I have it here somewhere.
I think it was discussed. Now, we had a longer discussion around this.
Artifact loaded.
That would be the events that's emitted once… An executable loads a dependency at runtime.
And it's specifically at runtime to distinguish it from.
all dependencies, so not an SBOM that would be sent at each process start.
but only see dynamically loaded dependencies.
**Liudmila Molkova** 43:02 I think it would make sense to do, like, research where we release the languages, the runtimes we support in OpenTelemetry.
And checking what is the API.
that instrumentable API looks like.
And then listing the properties, of the runtimes that are actually available.
And then it would probably be more clear what is the what's common between them and what can be generalized.
**Christophe Kamphaus** 43:40 Yeah, makes sense.
**Josh Suereth (Google LLC)** 43:43 This is supposed to be an inventory of, like, what libraries are installed in the system? Is that what the goal is here?
**Christophe Kamphaus** 43:49 Not the installed one, the ones that are loaded at runtime.
**Josh Suereth (Google LLC)** 43:54 Right. Is this supposed to work with, like, ELF and, you know, like, LDD and DLL loading and that kind of crap for more native languages, or is this at a higher level?
**Christophe Kamphaus** 44:08 I guess it could.
But the prototypes, or… It has existed already for some times.
or in Java instrumentation.
**Josh Suereth (Google LLC)** 44:20 Right.
So a jar is a clear thing there.
**Christophe Kamphaus** 44:24 Yeah.
And, he wants to also implement it for .NET.
**Josh Suereth (Google LLC)** 44:31 Okay.
And for Java instrumentation, it's just when you load the instrumentation library, not any library, right?
**Christophe Kamphaus** 44:40 No, I think it's for any jars that's loaded into the class pass.
**Josh Suereth (Google LLC)** 44:47 Right, but Java has like multiple class loader. I'll have to look at the prototype.
Like, is this dealing with all the class loaders that Java has and the crazy-ass stuff that's there, or is this, like, specifically, like, one type of Java environment?
**Christophe Kamphaus** 45:05 I think it's part of the auto instrumentation. So if it's turned on.
I guess it would, Instrument C class pass loader.
Yeah, I don't know exactly.
**Josh Suereth (Google LLC)** 45:21 Okay.
This is one of those things that seems like, The thing that I'm nervous about is you can create, like, code isolation, if you will, in Java. So you can actually isolate how you load things between class loaders. You can actually create a class loader that's completely isolated from everything else and shove stuff in there.
But generally, my concern is just, are we… are we making something really generic?
Without actually having done the due diligence on the general thing, and we should actually just stay not generic.
To start with, you know? That's… that's my fear here.
So… Anyway, I can put comments on the PR.
**Christophe Kamphaus** 46:09 Okay.
Yeah, I did some, I pushed back a little bit.
Because it looked like he would just send the full S-bomb at process start, and yeah, there's better ways to do it.
Can identify the process, and then… Look up CS from.
Somewhere else.
**Josh Suereth (Google LLC)** 46:36 This is a general question.
**Liudmila Molkova** 46:37 I'm…
**Josh Suereth (Google LLC)** 46:38 Oh, go ahead.
**Liudmila Molkova** 46:40 My main concern is that we.
Oh shit, I I I push back on all PRs that don't define a signal, and I think we have it in the conventions that the the core is the telemetry.
Signal, not the attributes.
**Christophe Kamphaus** 46:59 So yeah, we did some discussion and in the end it's the artifact loaded events that would come out of it.
So it's not a PR yet, it's just the issue.
**Liudmila Molkova** 47:11 Yeah.
**Josh Suereth (Google LLC)** 47:14 This is making me wonder about.
I think artifact loading makes sense, by the way, because you finally have an event, but just whether or not OpenTelemetry needs a new signal I mean, I think it does need a new stereotype. We've been talking about entities for a while, but this notion that you have a… State of an application.
And that you can communicate that independently of your other signals.
So… Profiling needs this, right? Profiling, you have to send, here's my symbol table, here's my application identity, here's how you can interpret the profile, because you're gonna get symbol IDs and not method names, and you need to interpret them to method names, and the symbol table lives outside of the process. Or, if you're lucky, someone put it inside the process, and then the executable's ginormous.
Right? One of the two.
But this is kind of similar of, like, what's your SBOM? If we had a means of, like, getting the SBOM and contributing it and sending it somewhere as, like, a side signal that somehow Joins in with the data later.
I… I keep wondering if… like, I'm glad you pushed on this to be a log event, I think that makes sense, but I keep wondering if there's.
something there around instrumentation, where we need to have this notion of, like, collecting information about the process, about the identity of it, about, you know, it's executable, it's SBOM, you know, this sort of thing, and communicate that as its own deal. How many things like this are showing up in the SemConf, generally?
**Liudmila Molkova** 48:46 And Gen AI content is exactly that, right?
**Christophe Kamphaus** 48:51 You mean the references?
Yeah. Or, big request response bodies.
**Liudmila Molkova** 48:57 Yeah, so wherever this thing exists, we would probably want to correlate that thing with some attribute, and it can exist in your build system, or in GitHub, or somewhere.
And it can be an external reference that you supply instead of, like, instrumentation figuring it out or something.
**Christophe Kamphaus** 49:18 I guess it could also be the… Descriptive attributes of entities.
So if you can externalize all of the descriptive attributes into a side channel, you would only need to send the identities.
**Josh Suereth (Google LLC)** 49:34 That's… that's in the design of entities, that's why we made that signal. I've just… when I see things like this, I start to wonder, like, did we get… did we get it right?
Since we're still on the, like, as we're launching entities. So, if you're not aware, Entities Java SDK prototype is now, like, part of the last release. So you can now use Entities in Java.
**Trask Stalnaker (Microsoft Corporation)** 49:57 So, I think this one is slightly… may slight… I see it slightly outside of entities, only because it's runtime.
versus build time.
So, I mean, you may even have dynamically loaded packages at runtime, so it… that's why it feels not quite an entity to me.
**Josh Suereth (Google LLC)** 50:22 So there's two pieces to entities. There's the piece that's in the prototype, and then there's the second piece, which is the relationships. So that would be where you have a signal that sends events that would say, like, okay, this process has loaded these packages. And that would be, like, an entity relationship event that you fire. Every time that changes, or you need to update it.
**Trask Stalnaker (Microsoft Corporation)** 50:43 entity.
**Josh Suereth (Google LLC)** 50:43 It's similar to this…
**Trask Stalnaker (Microsoft Corporation)** 50:44 event.
**Josh Suereth (Google LLC)** 50:46 Yeah, like, you'd have to look at the specification, to see the relationship event right now. It's not something that is… There's a prototype of it in the collector, but it hasn't hit any SDK. But the idea would be you can have the signal of relationships of, like, resources.
That doesn't come out the telemetry. So it doesn't go out logs, it doesn't go out metrics, it doesn't go out spans, but you could say, like, okay, my process has these 20 packages, and anytime I add a package, I'm gonna send an event that says, this package is part of this process, and I've loaded it.
So you get this, this, and it's, it's like basically metadata tracking.
**Trask Stalnaker (Microsoft Corporation)** 51:27 Okay, cool.
**Josh Suereth (Google LLC)** 51:28 Yeah, that's… that's Entity's Phase 2. And when I see things like this, I'm like, man, I, like.
It makes me wonder if we have solved the right problem.
And when things are gonna land, with entities, because this… this… reads a little bit like some of our goals with entities, where you get this big graph of, like, this process is these things loaded, this process is these things loaded, I can join it together with my data later, that kind of stuff.
**Trask Stalnaker (Microsoft Corporation)** 51:56 Yeah, yeah, I think it's a super interesting problem, like, the runtime packages.
is, like, you could do a lot of interesting things by having the runtime packages available. Versus the SBOM, even.
**Josh Suereth (Google LLC)** 52:16 But anyway, I don't think we should hold this up at all. I think having it as if it's literally a log event that gets written.
That's awesome.
So, we should, continue to make progress here, but I might talk about this at the Entity SIG a little bit as another use case to think about.
**Trask Stalnaker (Microsoft Corporation)** 52:33 And Christophe, this might be interesting for the spec meeting, just for re… broader reach of SDK maintainers to the, I think, Josh's earlier question about how many, languages does this Apply to…
**Christophe Kamphaus** 52:52 Yeah.
Was there a question there?
Or do you want me to bring it up in that meeting?
**Trask Stalnaker (Microsoft Corporation)** 53:03 If you… if you are the… If you want to recommend to the author, also.
to bring it up, just to get more SDK. I guess the question Josh asked was.
Is this limited to just, like, 2 or 3 languages, or is this… In which case… maybe we don't… generalize it, or is it, you know, 5 or 6 languages in case we do? I don't know, Josh, I was gonna ask you what… if you had a line where… In mind for how many it should apply to, to be worth generalizing.
**Josh Suereth (Google LLC)** 53:49 Yeah, I… so… so my… my mind is there's a general… dynamic loading, aspect of binaries, which is basically ELF and DLLs, right?
And I would argue that this should work for that, and then extend to ecosystems like .NET and Java that have custom dynamic loading on top of that.
Things like Python, or interpreted languages.
are crazy. And so I'd want to make sure this can work with those, but they're, you know, almost anything in a dynamic language is dynamic by nature of the language, so it's not, like, the same kind of hard structural rigor. So that's where I would… I would target the the foundations, right? So start with ELF.
Start with DLL.
and then work your way up the stack, is how I think. But I think this is starting from Java and .NET, which are… well-reasoned VMs on top of, you know, the core.
But bridging that gap, to me, is the important one, and then once you… because once you hit ELF and DLL and that level.
all the other languages basically are built on top of that in some fashion, even in Java, right? When they dynamically load crap, they can… you can load in DLLs. In .NET, you can load in DLLs. So I… that's why… the thing I was trying to get at was, I think if you can abstract this at that layer, then I have no concerns at all, that you're abstract enough.
But if it only works with Java and .NET, I would… I don't know if I would give this a different name.
Or somehow just say, yeah, this is limited in scope to things that have… languages that have known package modules and dynamic loading of packages, not general purpose, you know?
**Christophe Kamphaus** 55:38 Yeah, makes sense.
Okay, I will write that as a comment here.
Anything else? I don't think we have… Sven with us today, so I will put it into next.
And I will give you back 3 minutes, now 2 minutes.
**Liudmila Molkova** 56:28 Thank you.
**Christophe Kamphaus** 56:30 Thank you, everyone.
See you next time.
**Armin (Dynatrace)** 56:32 expect.
**Liudmila Molkova** 56:33 Yeah.
