SIG: Semantic Convention SIG
Date: 2025-11-24
Duration: 27 minutes
============================================================

## Zoom Recording Transcript

**Josh Suereth** 00:51 Hey, how's everybody doing?
**Armin (Dynatrace)** 00:54 Wired start today, huh?
**Josh Suereth** 00:56 Yep.
Yeah?
Ludmilla has, like, 4 items, so hopefully she's here.
**Armin (Dynatrace)** 01:06 Good point, then.
**Trask Stalnaker** 01:13 Yeah, fuck.
**Josh Suereth** 01:25 Armin, do you want to run the meeting?
**Armin (Dynatrace)** 01:29 I can, sure.
Let me get my sharing browser ready in the meantime.
**Josh Suereth** 01:40 I was just sorting out the notes myself.
**Liudmila Molkova** 02:08 Hello, hi everyone.
**Trask Stalnaker** 02:11 Yay…
**Armin (Dynatrace)** 02:12 Meh?
Is it just me, or is he tucked on?
I get an angry unicorn.
**Trask Stalnaker** 02:23 Oh, no.
Not here.
**Armin (Dynatrace)** 02:27 Hmm.
**Josh Suereth** 02:27 That's working for me, huh?
**Trask Stalnaker** 02:32 Could be regional.
**Armin (Dynatrace)** 02:33 Yup.
I think that's looking better now.
C.
Alright, so there we go. Let's kick it off with Ludmia, you have the first items on the agenda.
**Liudmila Molkova** 02:59 Yeah.
Okay, so… I have a few small PRs I wanted to… get… People's thoughts on,
So the first one is about, well…
it's somewhat problematic, and we managed to avoid this problem so far. We have…
The dependency between the folder name.
and the root namespace, and the area name, and they should be the same, actually. So now,
our automation Is complaining about, database.
Sorry, if somebody comes and makes changes to the database folder, the database is not an area.
So it will complain, and it will close the PR.
So, I'm changing, database to DB, it also will be helpful, the schema V2, it was problematic there as well.
Yeah, that's it for this one. We can build more tooling.
To allow multiple… aliases for the same thing, but I don't feel it's worth it.
**Trask Stalnaker** 04:23 Seemed fine to me. I mean, I can see benefits for people who, browsing it for them to match anyways.
**Liudmila Molkova** 04:36 Cool, then moving on to the next PR…
We… have PRs that don't touch anything semantic conventions related.
But we closed them and ex… So what I'm suggesting is that we… Somebody who…
has write rights on the repo. They can add a label, and they can get, they can be fine, but we can also allow to add chore in front to exclude the PRs from obnoxia checks.
If we see PRs with chore that are not chores, that actually change something meaningful about semantic conventions, we should…
As the reviewers, kindly ask.
author to update the title, and… but, in… in most cases, chore PRs are something that's tooling, and we… we actually…
Should allow them, regardless of ownership.
**Armin (Dynatrace)** 05:55 Also, I think if it's not a job but claims to be one, it should also be fine for us maintainers to just… just fix that and adapt it to reality.
**Liudmila Molkova** 06:05 Yeah, that's true, we can also update the PR title.
**Trask Stalnaker** 06:11 If we update the PR title, will the automation kick off again?
**Armin (Dynatrace)** 06:18 Aye.
**Liudmila Molkova** 06:18 Question.
**Armin (Dynatrace)** 06:19 I think with the, like, sure to bypass changelog request thingy. I think I have not been successful with that, only with adding the labor, but I… I might be mixing up one of the 15 reposts that all have their own way of checking it.
**Liudmila Molkova** 06:39 I'll check where the… Ownership check runs, which event triggers it?
If it's a label, then it should…
It should be fine. If it's the PR creation, then no.
Well, it's committe, probably.
Maybe we should change it to label check. let's a little…
**Trask Stalnaker** 07:03 If it's labeled… if it's labeled check, it won't get… the title name won't… Get picked up, though.
**Liudmila Molkova** 07:12 Right.
Let me leave a comment, and I'll check.
**Trask Stalnaker** 07:19 We could have… yeah, I mean, we could have the chore title to re-add the label.
And then we could… that way we can remove the label.
**Liudmila Molkova** 07:30 And if you can remove the label, you can use the… Accepted already.
as well.
**Trask Stalnaker** 07:40 Oh, I mean, if we decide that it's not a chore.
**Liudmila Molkova** 07:43 Oh, I see, yes.
**Armin (Dynatrace)** 08:04 Alright, but looks good other than that, right? No objections.
And look, Mia, you'll leave a comment, right?
**Liudmila Molkova** 08:12 Yeah, I just left it.
**Armin (Dynatrace)** 08:13 Cool.
Alright.
**Trask Stalnaker** 08:15 Yeah, that could be a follow-up, also.
**Armin (Dynatrace)** 08:20 Also, worst case, you can always, like, close and reopen, and then at the latest, it will run the check again, even though it
Looks a bit odd in the… in the overview page, but shouldn't do any harm other than that.
**Liudmila Molkova** 08:37 Yeah.
But let's see what we can do.
**Armin (Dynatrace)** 08:40 Alright, and next up is Lutan again.
**Liudmila Molkova** 08:45 Yeah, so the last one, this is, yet another thing. We didn't have an areas container.
R… So, I'm not sure what we should do with it,
I asked, container approvers and also trusts suggested to maybe merge container with Kubernetes.
Christus replied that they are actually
Not… not interested in contributions to container.
They only own it because it… adjacent to Kubernetes.
**Trask Stalnaker** 09:25 Yeah, I think it's very similar to… other, like, HTTP, approvers.
We have area, client, and server under it, but we don't…
really care about… we're not really handling those outside of client and server things that relate to HTTP.
**Liudmila Molkova** 09:49 Yeah, from this sense, it sounds like we should merge it with Kubernetes, and
they… if somebody sends a large request unrelated to Kubernetes about containers, the Kubernetes seek can, triage it and decline if they don't think this contribution is timely.
**Armin (Dynatrace)** 10:16 it would not make the situation any worse for someone trying to make a change than it is today, right?
Just gives them a… Another chance of sorts.
That's awesome. Yeah.
**Liudmila Molkova** 10:31 Yeah, so now we just automatically close container, any container changes, and we want, but then it would require Kubernetes to manually triage.
Cool, so then it sounds, let's merge it into Kubernetes.
Is somebody…
From Kubernetes Secure, okay, I'll also check with them if we need to keep two different groups.
**Trask Stalnaker** 11:12 Oh, yeah, yeah, that would be good. We can close that other… the containers approvers group.
Yeah, I did look. It was,
It was a subset of…
It was almost the same, except for one person who was a more recent member of Kubernetes.
Approvers who they hadn't added to containers.
**Liudmila Molkova** 11:40 Sounds like yet another reason to merge them.
**Trask Stalnaker** 11:44 Yeah.
**Liudmila Molkova** 11:49 Cool, I'll leave a comment, they'll follow up.
**Armin (Dynatrace)** 11:56 Alright, thank you.
And then our next topic is, Josh, do you want to share, or should I… should I do that?
**Josh Suereth** 12:06 You can keep sharing. Yeah, this is… this is gonna be a discussion a bit.
So, basically, we're working on the V2 schema.
for Weaver. So this one will be a lot nicer for folks to write semantic conventions, and we're actually at a point now where you can start using it for… oh, I need to click some buttons on there.
let's see, that one needs to get clicked, and… This one needs to get clicked. So we merged… we merged, I think, 3 of the… 3 PRs so far, and we have live check coming, but effectively, what this lets you do…
is you can define your models in V2 schema, or V1,
you can resolve into V2 schema, and then you can use Forge…
to make your Jinja templates, your Rego policies, all that on the V2 schema. What V2 is, is things are called metrics. Things are called
spans. Things are called events. They are not called groups with a group type anymore.
So it's a bit more clear what's going on.
The goal of this work, and the reason we're trying to get it out quickly, is we're going to commit to a publishing format.
very soon.
Because we want to start federating semantic conventions, which is the discussion I want to have. If you look at the proposal from the GC,
On, the blog post about moving towards a different way of thinking about OpenTelemetry stability, and trying to unblock instrumentation.
Where they don't need to use our centralized, you know,
semantic convention repo to stabilize their components, we need to start thinking about federation. So.
this is the tracker on Weaver for what's going on to actually make it easier and more convenient for folks to basically define their, their,
their version of semantic conventions, and then publish it.
The publishing is the important part. We want them to publish, you know, here's the data I'm generating, we want them to publish a schema next file.
Or, what do we call it? The schema URL?
With the differences, so they have, like, versions. We want to have policies around, like, what is safe to upgrade, what is not safe to upgrade, so that they don't accidentally break their users, but they are allowed to do that for, like, a major version bump, that sort of thing.
we want to actually take what we've built in semantic conventions and make it a reusable piece that, like, the collector could pull in for, you know, a particular receiver. So let's say the collector's building a receiver that we don't think needs to be in Semcov.
you know, they're doing technology X, and it's not ready for CENCOM yet. They should still be able to make a stable component.
And what that means is they would define
a schema in a more natural style, right? They would publish that schema, they would publish docs.
And they would have some kind of a version dependency policy check to make sure they're not breaking their users from version to version.
Our goal with what we're doing on the Weaver tooling side of this is to get that reusable set of that ecosystem out the door as quickly as possible.
We had decided, I guess, about a year ago, that the current schema for semantic conventions needed some reworking to make it more human-readable and consumable, and less
Confusing?
And so we decided to accelerate that work.
Which is actually going quite swimmingly, in my opinion.
Move semantic conventions to it.
and then start decomposing some of the semantic convention features, and having them be out of the box in Weaver, that everyone can make use of. For example, the,
compatibility rules that we have in Weaver, or sorry, in semantic conventions, I'd like to have just out-of-the-box default as a set of policies in Weaver for folks.
Some of the code gen we have right now in semantic conventions is…
somewhat complicated, because the way we're doing global semantic conventions is a little complicated. We want a simpler version of CodeGen that we give out for distribution.
Right.
Anyway, what I wanted to talk about here is give everyone an overview of what's happening.
In the tooling side.
what we're building out in Weaver and what we're doing, why we're trying to get V2 out the door. If you want an example of V2 schema, I don't know, Ludmila, do you have one handy? Because all of mine are…
inside of Rust, in, in… Example.
examples. I don't think I have one that's flat.
**Liudmila Molkova** 16:54 You mean resolved schema?
**Josh Suereth** 16:57 Yeah, the resolve schema, or just, like, the V2 definition?
**Liudmila Molkova** 17:01 I have a resolved schema, but it's 3 megabytes,
**Josh Suereth** 17:05 Oh, no, no, no, no, that's fine. Let me, oh, you know what? I have a test we can show.
Okay, so let's do… I'll send you, I'll send you a link, in chat here.
Do you mind opening that one, Armin?
And then pop open test.yaml.
So, if you look at this, the main difference is, if you look at the YAML file.
All the attributes are in a big array called attributes, all the groups are in an array called groups, and these are just the publicly visible ones you want to document.
Events are in a group called events, entities are in a group called entities, metrics are in a group called metrics, spans are in a group called spans. The other thing we've tried to do is, the values that you set, for example, for attributes, it is key, which represents the key value of OTLP. When you do metrics, it is name, it is not metric underscore name, right? So that's one of the things we did.
And then if you, if you click, back.
Armin, to the previous thing, and then look at the REGO policy.
You also get the same view here. So, when you want to write a policy, you can look at these signals and say, for every metric, grab the new metric, grab the baseline metric, and then I can do diffs on metrics when I write REGO policies going forward.
So this is an example of how we'd, like, update our…
tools and policies and things and semantic conventions. So.
Alright, going back to the notes now.
Our goals in Federation are, we want…
components of some kind to be reusable.
across hotel…
to do a…
Feasibility. Bump.
2, alright.
Okay, so basically, I think there's 3 things I want to accomplish between the semantic invention group and the tooling group that's supporting semantic conventions, right?
we want to start taking our components of CENCOM and figuring out how to make them be reusable in the ecosystem. So this is our markdown generation.
To make docs for folks.
We want to figure out a way to, like, you know, we have a registry right now.
We'd love if we could actually just give folks the ability to generate that registry in a way that OpenTelemetry.io can consume it.
We have our REGO policies. We want to find a way to make those REGO policies general, not just specific to SEMCOV, which they're not quite.
But we want to guarantee that they are, and have them in a reusable place that everyone can make use of them.
CodeGen features currently are delegated to other languages. That, I don't expect this group necessarily to engage with that, but the first two, I definitely do.
The second thing we want to do, we want to do this readability-usability bump. That's what V2 is. Make this more readable, make this more usable.
To the extent that you can try, Weaver has a latest, and they have, I think it's main is a tag, let me check real quick.
So, Docker Hub.
If you were to, this one fucking DJ.
If you were to try the, which tag is it? I think it's main.
Yes, main. If you were to try the main tag of the Docker container, you can actually use V2 today.
And you can use it with all of the Rego policies, and like, there's enough in there that we can actually start experimenting with moving to this new human-readable format. What we want is we want… Lyudmila's been doing a really great job of giving us feedback for Semcov. Yeah, the main tag here.
That one, as of 4 hours ago, should have policies, should have forge, should have emit. So, live check should be coming soon. We're rapidly… we're gonna have a launch of Weaver relatively soon, but what we really want is to understand
is this accomplishing the goal, right? Is this more usable? Is it more readable? Is it easier to work with? So, to the extent that folks can take a crack at, like, let me try to generate docs with this, let me try to generate a registry. We don't have a registry for events, we don't have a registry for spans, we don't have a registry for, metrics.
if anyone has a chance to actually work on that with V2, that would be ideal.
Right? And lastly, we want to try to iron out our CICD pipeline to get reusable pieces. So, I… we haven't gotten to the diff part, so that's not there, but one thing our CICD pipeline does that I want to give to everyone is automatically generating schema URL.
when it's required.
We're figuring out how to, like, make that a reusable piece that folks have, so that no one has to worry about schema URL going forward.
We want to figure out how to publish these things, how to get them into OpenTelemetry IL.
if there are pieces in our pipeline that we've made, and we've highly customized them for Semcov, I want to start thinking about pulling them out and making them reusable.
That's the body of work here, to basically start to accelerate OpenTelemetry's, stability stuff. So that… I wanted to have a discussion about… this is the kind of the vision of things I think need to happen, and, like, areas where that's happening, and then, like, a call to action for us all to participate. Go ahead, Trask.
**Trask Stalnaker** 23:03 Can I share for a minute?
So, we have… you were asking, for people to try it out, and we have this, Antoine had done this in the Java Contrib repo.
Using Weaver, and, right, like, it was helpful to see this problem that you're essentially talking about of how we have to replicate everything over here.
What I… my question is, is it… I didn't quite follow if it was in… if the new stuff was in a state where I could try it out on here or not.
**Josh Suereth** 23:51 you can try it out on there. You'll want to do it on a branch, and if you're doing… if you're using, I don't know what your Weaver Dockerfile is doing. That's interesting.
**Trask Stalnaker** 24:01 Oh, it's just, pinning. Oh, it's just pinning, yeah. So, if you pin to… instead of version 0.19, if you pin to the tag main.
**Josh Suereth** 24:11 It will pull in our latest nightly build.
So, the latest nightly build of Weaver has everything you need to try this out.
So you can actually pull in the main tag.
**Trask Stalnaker** 24:22 And so it will… it has…
Because I think all we're doing is producing… is generating this doc page.
Does it have… it covers this…
**Josh Suereth** 24:33 it… you should be able to generate that exact same doc page with V2.
**Trask Stalnaker** 24:38 Sweet. Okay.
**Josh Suereth** 24:39 Now, what it'll do, if you look at your YAML files as well.
Oh, yes, we have to update our YAML files, yeah. You don't have to update them, it should actually convert from what you have there into V2 on your behalf.
**Trask Stalnaker** 24:53 Mmm.
**Josh Suereth** 24:54 But… but… and you could, today, upgrade what you have to the V2 format without moving to main.
So, the ability for you to do in the YAML is something you can just do… you get a warning about it, about it being unstable, but you could just do it today.
the resolution phase and the rendering phase, that's the part that is in Nightly.
Yeah.
**Trask Stalnaker** 25:18 Okay.
Okay.
Awesome.
**Josh Suereth** 25:21 Yeah, we're trying to move rapidly, so getting feedback, getting any kind of, like, hey, I'm running into issues, I tried this out, and I don't like how you do XYZ, or there's a feature I relied on called Y, you know?
that we didn't know that you needed, but I absolutely need, and it's broken, let us know. We are, as part of V2, cutting some of the features.
From V1. Like, they're things that we just don't think people actually engage with. An example, I think group types.
There's a group type of instrumentation scope.
As far as I know, no one has used that in practice. That's getting cut. In Weaver, there's the ability for you to define a resource in a registry of, like, this
entire set of things I'm generating is about a resource, that is cut in V2 right now. We can add it back if folks need it, for example. Anyway, I don't want to get into too much specifics, just like…
there's a call to action here. We're trying to move quickly, we're trying to federate, and I think that this is like a, an all-hands-on-deck open telemetry experience of, let's figure out how to get our core stable, the things that people depend on.
There's a second approach of this, by the way, of… we need to understand which semantic inventions people rely on that have no path to stability today, or no SIG behind them, and then get a SIG behind them, but that's… that's a secondary concern. For now, let's federate.
Cool.
We have nothing else on the agenda, so I don't want to waste everyone's time by just continuing to talk for…
25 minutes when I said I'd only talk for 10.
**Armin (Dynatrace)** 27:09 Any other last-minute topics?
All right, and let's call it here. Thanks, everyone.
See you around. Bye.
**Liudmila Molkova** 27:23 Thank you.
**Josh Suereth** 27:24 Thanks for running the meeting, Armin.
**Armin (Dynatrace)** 27:26 Sure.
