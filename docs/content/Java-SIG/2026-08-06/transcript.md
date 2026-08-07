SIG: Java SIG
Date: 2026-08-06
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Trask Stalnaker (Microsoft Corporation)** 00:49 John, Jason, y'all feeling cooped up?
**Jason Plumb** 00:53 Yes? Yes.
**John Watson** 00:54 Yes, although the air is getting better, below 100 out here on… up on the mountain.
**Trask Stalnaker (Microsoft Corporation)** 01:06 Yes.
I can't wait to be able to open the windows.
**Jason Plumb** 01:10 I know.
**John Watson** 01:11 Yeah.
**Jason Plumb** 01:11 really cramping my style, and this Sunday is Bridge Pedal, which I hope happens, because I have a ticket for it.
Yeah.
**Trask Stalnaker (Microsoft Corporation)** 01:19 Yeah, it's supposed to clear up, right?
**Jason Plumb** 01:23 I hope so.
**John Watson** 01:25 Yeah, the ocean breeze is coming through and hopefully pushing all this stuff Into the other side of Oregon.
Somebody will have to breathe it.
**Trask Stalnaker (Microsoft Corporation)** 01:35 somebody else.
**Jason Plumb** 01:36 Oh, the ocean.
The ocean breeze that's gonna fuel those fires for another month.
**Trask Stalnaker (Microsoft Corporation)** 02:11 Let's, so for the 3-0 milestone, did I not add the… Messaging… Thank you, Lauri, for… I saw you chugging away on those reviews today.
How do you like the stacked, pRs.
**Lauri Tulmin** 02:42 Huh? I think they're nice.
**Jason Plumb** 02:45 It doesn't work from forks, though, right?
**Trask Stalnaker (Microsoft Corporation)** 02:49 Right. But we have… Set in this repo… And I want to do it in other repos to allow people to push Who have right access to the repo, so approvers… and maintainers… to be able to push to branches with your GitHub, Alia, GitHub username, slash something.
**Lauri Tulmin** 03:18 Do approvers actually have BrightX's?
**Trask Stalnaker (Microsoft Corporation)** 03:21 Yeah.
**Lauri Tulmin** 03:24 They can merge PRs.
**Trask Stalnaker (Microsoft Corporation)** 03:26 No, so… The only reason they can't merge PRs, though, so in other repos in the world, they… you could.
But we have, in OpenTelemetry, we have… and this is the only reason we still have to keep around these classic branch protection rules.
Is for this setting… Restrict who can push to matching branches, to repo… Maintainers.
But, yes, they can push to other branches.
**Jason Plumb** 04:08 So, in instrumentation, you have it set up so that approvers and maintainers can push to a branch that is named with your GitHub handle prefix, and then a slash, and then the actual name?
Yeah. So it looks… in that case, it looks like a fork, even though it's not, right? Like, it's… it's not precisely, like, the same syntax, but… okay, so it kind of… It pretends to be a fork. It scope fits, yeah.
**Trask Stalnaker (Microsoft Corporation)** 04:32 Scopes it so that it's clear that that's your branch and not some, like, official branch on the project.
**Jason Plumb** 04:38 Cool, but that would allow you to stack, because I tried this in another hotel repo, and it didn't work, because of the fork problem.
Cool, thanks for clarifying that.
**Trask Stalnaker (Microsoft Corporation)** 04:47 Yeah, yeah, so here's the little stack icons here.
If you want… I'll try and push the, what I need is… I need somebody to approve this. I need a GitHub admin to approve this.
And this adds a, allow approver branches, easy setting to basically enable that feature where then you can have approver prefixed branches outside of C… You can do that today, but, like, the CL… easy CLA will then prevent you from updating those branches, so they're basically useless.
Oh yes, so I was going to this… Messaging… Where's my messaging?
Issue.
Did this, here we go.
I need to tag this… Throughout… A couple others that are not required for 3-0, but I'm gonna see, if I can get them in, is… Stabilizing the runtime telemetry library… Stabilizing the HTTP library instrumentation.
And stabilizing the micrometer metrics bridge.
Cool, let's move on. Jack Shirazi.
**Jack Shirazi** 06:51 Yeah, this was a couple of weeks ago, Jack, the other Jack, suggested that, we want to transparently support nodes Where there are currently nodes… nodes slash development.
if it becomes a stable node, then even if you have node slash development in your YAML, it should support it as if it's node.
So that you support both at the same time.
And… Yeah.
I just wanted some feedback on that.
Because… I may need to support that in the config, provider stuff that I'm working on.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 07:40 I agree with it, and I just linked in my PR that embodies that for all of the generated POJOs from the declarative config data model.
There's, I do some clever things in there to basically check if you included the development suffix on anything, and, you know, log a warning if that property has been promoted to a stable version of it.
so… I agree with it. I'll say that the, some people… there's an issue open in declarative config where some people don't like that that is how we denote experimental properties. They would rather have that it be… the fact that a property is experimental be denoted in some sort of metadata, either in the description field or in a non-standard JSON schema.
keyword, and so that… there's, like, I can link to this issue as well.
That sort of complicates it, because, you know, the, the, the strategy that, you know, you're questioning on whether you should embody elsewhere is, like, under question itself, so…
**Jack Shirazi** 09:05 There's also, so part of… what I'm asking is… There's a combinatorial explosion if you have lots of slash developments in your inner… inner path.
And… so what's your approach? What are you taking there to… as your approach to… Handle any one of these nodes, or all of them becoming stable.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 09:31 So you're, you're saying, like, you have the full JSON path, which has, you know, walks down a tree, and maybe you have several in a row that are, like, nested slash developments?
**Jack Shirazi** 09:43 Yeah.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 09:45 Is it combinatorial explosion, or is it just times 2?
**Jack Shirazi** 09:54 It's 2 to the N, isn't it?
Isn't it?
Any… any one of them can be… Stable, and then any pair can be stable, and any combination of them can be stable and not stable.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 10:10 But you'll walk.
**Trask Stalnaker (Microsoft Corporation)** 10:11 One at a time.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 10:14 Right. So, like, you know, you walk one at a time, and the first node that you encounter that, like, you check, is it development or is it not development? And, you know, you resolve your node, and you do that same thing.
But it's not like for each of the is development or not development, you have to walk both trees and explore. I think, like, you know, you kind of encounter and resolve that, like, iteratively.
**Jack Shirazi** 10:39 No, so the… with the callback that I'm adding to the spec.
That's got a path. So the path is a… The path has the combinatorial explosion.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 10:55 Right, okay, so this is… because it's a callback, you're watching a specific path, you're not, like, Yeah, because it's watching some set of paths that it needs to resolve, rather than, you know, knowing the path that it needs to go down, and then just, like, exploring.
Okay, I see the difference.
**Jack Shirazi** 11:23 We don't need to resolve it here. There's a… I've put the link to the thread that I've got open.
So, if you want to continue a discussion there, then that'd be fine.
**Trask Stalnaker (Microsoft Corporation)** 11:41 Yeah, would definitely be interested in, yeah, I'll read this also, I hadn't seen this, but, Jack Shirazi would be interested in your… Thoughts on this?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 11:56 Yeah, thanks for finding that. I can summarize my point of view that I expressed on that really quickly, which is, There's no standard way to record this type of metadata in JSON schema. We'd have to… like, if we want to adhere to the standard set of JSON schema keywords, we'd have to put it in description, and have some sort of, like, identifiable marker in description. And it, you know, I think it really changes the UX around using experimental properties.
With what we have today, with the slash development suffix, it's really in your face. It's unavoidable to know that the property that you're using is experimental. You have to type it out explicitly, and it's ugly. It's, And, you know, it's… I feel like as soon as we get rid of that, and we embed that information in some sort of metadata, like a description, we're making it really easy for users to misinterpret the stability and maturity of what they're using. So, that's my main.
**Trask Stalnaker (Microsoft Corporation)** 13:03 We're also… Not putting any pressure on ourselves to… Move things to stable.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 13:09 That as well, yeah.
I guess the other thing is, so… think about instrumentation schemas. Like, each instrumentations, you know, the schemas for them is a distributed problem. They're not going to go in, and we're not going to allow this for, you know, instrumentations to record their configuration schemas in the OpenTelemetry configuration repository.
So, you know, what they have to do, if they want to use JSON schema, they have to, like, you know, have a little snippet of their JSON schema for them, you know, somewhere, you know, in their own repo, next to the instrumentation itself, and, you know, maybe do some code gen things or something like that.
But more likely, they'll do the lightweight approach and do what I call, you know, what's called schema on read, which is like, you know, we pass them this generic declarative config properties object, and they introspect on it, and evaluate the properties, and check if the, you know, the expected properties or the required properties are present, and the you know, any optional properties conform to the expected types and semantics, and if they don't throw exceptions, right? So that you're enforcing whatever your schema is at read time when you're reading the properties out. That's the lightweight way to do it, that's the way that I think everybody's going to do that. And in that type of world, there really is no way to record which properties are experimental And which are stable, right? The schema is, like, embedded in the source code, when you're doing schema on read. And so, you know, I think that's another… Nod in favor of having some very explicit, you know, signal that a property is experimental.
**Trask Stalnaker (Microsoft Corporation)** 15:01 even if instrumentations did define a JSON schema.
We don't… there's no discoverability mechanism.
I'm thinking of, like, semantic conventions, like, we're going through this whole big effort of having federated semantic conventions, and they are discoverable. There's a schema URL in… that the instrumentations emit, and you can go there and, you know, navigate through the whole thing.
Where we would have to then Introduce something similar like that for configuration to… truly support, That way.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 15:43 Yeah, so I would love it if you could leave your feedback on that.
**Trask Stalnaker (Microsoft Corporation)** 15:50 Cool, I'll leave that open.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 15:52 And Jack, just as we were talking, like, one thing came to mind about this, like, this slash development stuff, and the combinatorial explosion, which is that, so there's this question of, like.
To what extent do you need to include the slash development suffix, like, all the way down the tree?
You know, right? Like, if you… since the top-level instrumentation slash development has that suffix, it's implied that everything underneath it is experimental and subject to change.
And so, like…
**Trask Stalnaker (Microsoft Corporation)** 16:30 The intervention we've been using in the instrumentation repo is we only put the slash development Well, it's all the way up at the top of instrumentation node. We're ignoring that one.
But then we put it on whatever we consider experimental, but then not on the ones below it.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 16:50 Right, and so maybe we could, like, codify that convention somewhere to get it from, like, a 2 to the n problem to limit it to where, like, n is a maximum of 1, so it's just, like, a maximum of 2 paths to watch instead of 2 to the n.
**Jack Shirazi** 17:06 So, what happens if we decide to stabilize one instrumentation?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 17:13 Yeah, right, yes, and this is the issue with this, is like, you know, then something underneath it has to change, right? And so, I don't know, I think we need to analyze this.
You're right, though. I've had that same thought.
**Trask Stalnaker (Microsoft Corporation)** 17:32 Oof.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 17:40 Okay, so open questions.
**Trask Stalnaker (Microsoft Corporation)** 17:42 Yeah, no easy answers.
Alright.
Anything else worth… Spending more time on here.
In the meeting.
Cool, yeah, I will, I'll look over that, issue, Jack.
Berg… And, yeah, that's really interesting.
problem, Jack Shirazi, of the… because it only comes up Because of the listeners, right?
How I understood, okay.
Alright, SDK release.
Tomorrow.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 18:45 Yep.
Just a call, if anybody… thinks that anything important is missing. I've linked one PR here.
that I plan on merging. I just wanted to call this out mostly synchronously for John Watson. So, last week I was talking about these, you know, these thoughts of extending the OpenTelemetry API attributes default implementation to be, like, limits-aware and, and, you know, basically allow us to get rid of attributes map, and I opened some PRs and left some comments on my own PRs for the different, like, you know, routes I explored with that, but basically, it was a dead end. Like, there's no way to have an array-based, attributes implementation that doesn't significantly degrade, you know, the span record throughput and log record throughput.
Which really depend on incrementally building up, attributes, by calling, you know, setAttribute, or put, or whatever it is.
So I was seeing that I couldn't get anywhere past, at least, like, a 20%.
Regression and performance.
And so I gave up on that route, and so that leaves you with, you know, trying to improve the existing attributes map implementation.
And, you know, what this person has done here, just to kind of summarize it really quickly, is like, so our attributes map, it doesn't have last right wins semantics, because the keys in the map are attribute key.
So, if you have a long key and a string key that has the same name, those are not equal in the eyes of the hash map.
Right? And so, what this person has done is essentially, like, hand-rolled, the important bits of a hash map, and, such that we can, have this string-based identity, without, like, any extra allocation or wrappers.
And, you know, I think they've also done a couple of things that sort of improve the implementation as well by stripping out things in HashMap that we don't really like. Like, AttributesMap today, it extends HashMap.
And that's a problem with keep with promoting it to part of our public API, because that means it inherits all of the HashMap APIs, and those become public things we support. And we couldn't have a delegation approach. We couldn't have the attributes map have, like, an internal HashMap reference and hide that API, because that increased allocation and made the performance worse.
And so, like, by having… by hand-rolling, you know, essentially the important bits of a hash map internally, we now have a route to promote this to being part of our public API without excessive API service area.
That's… that's one of the benefits.
**John Watson** 21:47 So, would you then imagine this replacing the array-based implementation?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 21:55 That's a question I've asked myself, is, like, could this be the thing we standardize on?
And… I think… I think it's probably gonna hurt performance for the array-based implementation.
**John Watson** 22:08 From a memory… from a memory… from a memory perspective, for sure.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 22:13 Right. Because, you know, we're doing extra work that we didn't need to do before. But it's not like the array-based implementation is completely free. Like, it does this sort operation.
If, like, during build time, and, you know, maybe that offsets this, like, extra hash map-type tracking in some way. So, I think that's still on the table, is standardizing on a map-based implementation, but I just don't know yet.
**John Watson** 22:39 Could we imagine… so, one of the… one of the reasons why we do that sort during build time is the assumption is when you're using that implementation, you're doing all this stuff up front. Like, you're not doing it in the hot path, right?
You're building those attribute… the array-based attributes as something that's kind of statically allocated up front before you actually go in to work on things.
Which means it doesn't matter if you're having to do those sorts during the… like, if it's not in the hot path, it doesn't matter. I'm wondering if there's a way we could kind of get the best of both worlds with using something like this map implementation this HashMap, you know, minimal HashMap implementation, and then freezing it into a memory-efficient Array-based implementation when it's Like, when it gets shoved into whatever, wherever it's being used.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 23:33 Yeah, because what this is really the analog of is it's an analog of the attributes builder, not of attributes itself. Yeah. You don't need the map by the time it's, like, resolved to attributes. Yeah.
**John Watson** 23:45 So I wonder if there's a path that way to having one builder that is basically a map And then freeze it into the array-based, memory-efficient implementation when needed.
Just a thought.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 23:58 Yeah, yeah, So, yeah, luckily there's no API change for this, so, like, you know, rather than being this sort of, like, big you know, scope creep, like, sort of the routes that I was exposing, or exploring. This just is like, you know, a more targeted fix. It's like, you know, maybe this opens us up to having a single implementation down the future that's map-based, but for now, all it really does is fix the last value wins semantics that we're expected to have.
Without any performance regression.
**John Watson** 24:35 There isn't a way on a regular hash map to provide custom hash codes for your keys, is there?
**Trask Stalnaker (Microsoft Corporation)** 24:46 Wrap your keys and implement hash code.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 24:49 Right, exactly, that's it, and that's what I… I sort of was alluding to that with, like, this doesn't have any extra allocation. So, like, yeah, you could wrap your keys, or your values and get the semantics that you want, but…
**John Watson** 25:05 I'm thinking of, like, the… the tree map API, or the sorted map API, where you give it the comparator up front, but there's not, like, a hash map… hash code equivalent for that, which would be interesting.
Anyway, just, just thinking out loud.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 25:23 Yeah.
So, so I am planning to merge this, unless, unless anybody contests, or, and so, like, one thing that I added to this, because I pushed a commit to this as well, was, I added a, a fuzz test.
That, like, that builds up one of these, you know, limited attributes map implementations with a bunch of, like, you know, random, combinatorics thing, and it compares to a standard HashMap-based implementation, right? And make sure that it's, like, you know, it's equals… it's equivalent in all the ways that matter incrementally as it's built up, so…
**John Watson** 26:02 I was going… I was literally going to suggest something like that, some sort of… Big, randomized test… To try to break it in any way we can.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 26:12 Yeah, yeah, because, you know, when I see this kind of low-level code, you know, it makes me worried about bugs, so I had the same thought.
**Jason Plumb** 26:21 Getting HashMap out of the picture is such a win, I think.
I like it.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 26:28 I'm glad you like it. Like, it does… I am excited that it gives us a path to actually promoting this to part of our stable API, which, you know, is aligned with our reduced shared internal code. Right now, this is shared internal code. And so, you know, we gotta get rid of it at some way, and this sort of provides a path for that.
That's all.
**Trask Stalnaker (Microsoft Corporation)** 26:54 Nice.
Alright, let's move on. Pranav, hey!
**Pranav Sharma** 27:05 Hey, yeah, first of all, my apologies, I joined the meeting a little late, so some of the questions I'm about to ask might already be answered in the first point, but I just wanted to know, like, in 3.0 release for instrumentation that's about to come.
What would a path to stability look like for individual instrumentation libraries?
Like, I noticed that there's an opt-in attribute for stable semantic conventions, and the last time I asked this question, I think the major blocker was unstable semantic conventions. So now that we have that opt-in thing.
Can we typically consider these instrumentation libraries to be stable? Like, hotel.stable equal true, can we publish the libraries with that, or do we need to wait until all the SEMCON have stabilized?
**Trask Stalnaker (Microsoft Corporation)** 27:56 We do not have to wait anymore.
for, SEMCOM, to be stabilized.
That has changed at the project level.
As long as we… Don't introduce any breaking, changes to, without a major version bump.
So we still can't break telemetry. We can't break the telemetry we output, Without a major version bump.
Is basically the only rule we have to conform to now.
**Jason Plumb** 28:44 Can I… Can I ask for clarification on that, Trask? So a stable… an instrumentation that has declared itself as stable may output telemetry which contains in-development semantic conventions.
**Trask Stalnaker (Microsoft Corporation)** 29:00 Yes.
**Jason Plumb** 29:00 And, an instrumentation that has declared itself as stable will not break the existing shape of the telemetry that it outputs. So if today, if it's generating a span when X happens, then it needs to keep generating that span. Is it okay for an instrumentation that is declared stable to generate additional telemetry?
**Trask Stalnaker (Microsoft Corporation)** 29:22 There's the whole… there's a whole document in semantic conventions, or in the spec, I always forget which place, about what constitutes breaking telemetry changes.
**Jason Plumb** 29:33 Okay, this is newer?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 29:35 No.
**Trask Stalnaker (Microsoft Corporation)** 29:35 No, no, that one… that one's… yeah, that one.
**Jason Plumb** 29:39 Okay, sorry, I thought you were suggesting it was, like, a newer project-level change.
**Trask Stalnaker (Microsoft Corporation)** 29:45 The change is that, previously, It was… there was guidance that instrumentation should not be marked stable unless the semantic conventions were marked stable.
**Jason Plumb** 30:01 That's the recent change.
**Trask Stalnaker (Microsoft Corporation)** 30:02 That's the more recent change, yeah.
**Jason Plumb** 30:05 Okay, cool. Thank you for that clarification. I will go hunt the stock down.
**Pranav Sharma** 30:09 Yeah, thank you for that. So, So, most of the libraries right now are published with the alpha tag. With the 3.0 release coming up, that tag would be removed then?
**Trask Stalnaker (Microsoft Corporation)** 30:23 Not necessarily. It's still a case-by-case decision of do we… Are we comfortable with the… do we like the API? Do we like the telemetry? Mostly it's… mostly about the API, some about the telemetry.
Yeah, I was sharing, actually, in the V3, it was on my mind just yesterday, and I marked a few of these as targeting 3.0, so run… stabilizing the runtime telemetry library.
The HTTP library instrumentations, and the micrometer bridge.
**Pranav Sharma** 31:09 I see. Also notice the database semantic conventions were stable now, right? There was this project, and all of the tasks were completed there, so that will also become stable come 3-0.
**Trask Stalnaker (Microsoft Corporation)** 31:21 The Java agent will emit the stable database semantic conventions.
By default, in 3.0.
We aren't currently planning to mark the database library instrumentation as stable.
**Pranav Sharma** 31:41 Okay.
And just to be clear, like, this is… this is no longer blocked on, like, semantic conventions, as you mentioned, it's more about the API shape and… and whether we feel okay.
**Trask Stalnaker (Microsoft Corporation)** 31:53 Yeah, so if you look at a couple of these, to kind of get a sense of what stabilizing a library looks like. So, the HTTP library, right, like, I did a lot of rounds of review, to, to get it to a shape where I felt Comfortable marking as stable.
**Pranav Sharma** 32:17 Okay, I'll take a look.
**Trask Stalnaker (Microsoft Corporation)** 32:18 Some of them are… some of them are less, but still, like, you know, there's certain things that we need to kind of… look at, and this was great. Like, Bruno provided some feedback, and I'm working on, Getting that there. And then, same with the micrometer. There was a request for logging I probably don't want to tackle that for 3-0.
But yeah, if there's, like, very specific ones that you care about, that's the best, and maybe open an issue or two.
And get, kind of, thoughts, and if you can kind of start taking a look at those and comparing them to, you know, our conventions and other… other library instrumentations, that would be great.
**Pranav Sharma** 33:08 Okay, that sounds good. Thanks for the clarification. Yeah, I'll take a look at these, projects, like instrumenting HTTP and the database one to… for reference, and I'll see if I can open up some issues. Thank you so much.
**Trask Stalnaker (Microsoft Corporation)** 33:20 And it doesn't have to… 3.0 isn't, like, we can stabilize them in 3.1 or 3.2. Like, if we miss 3.0, we haven't missed a major version bump since it was never marked stable before we can… Still break things mid in minor versions.
**Pranav Sharma** 33:43 Got it.
Thank you.
**Trask Stalnaker (Microsoft Corporation)** 33:46 It's just the Java agent.
that we can't break mid-version, because the entire Java agent is marked stable.
Right. So all the telemetry we emit has to be preserved until major version bumps.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 34:05 Trask, I wonder what your thoughts are about, relaxing, the scrutiny that we normally apply to public API surface area, you know, given that instrumentation does have periodic major version bumps that, like, Core does not benefit from.
**Trask Stalnaker (Microsoft Corporation)** 34:24 Yeah, I agree, I don't want to have no scrutiny, scrutiny.
So… Because… and I'm still, like, hesitating on, like, instrumentation API package, which we have marked stable.
A long time ago.
We have… Even in the 2.0 and the upcoming 3.0, we have not made any breaking changes to that.
We have deprecated things.
But I'm nervous to deprecate… to actually break, especially that one, because it's… Could be a.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 35:10 That one might actually be more like an API in the core sense, in terms of, like, you know, you know, despite it sharing the versioning schema of the rest of instrumentation, it, like, it really should just… If we could… if we had a blank sheet of paper and no other constraints, we might try to keep it on 1.x for a long time.
Yeah, okay, just, just curious what your thoughts were on that.
**Trask Stalnaker (Microsoft Corporation)** 35:40 I totally agree that it puts us somewhere in the middle there, since we do these, major version bumps. It gives us… Some… a lot more flexibility.
Cool. Oops.
Last year, our… Jonathan!
**Jonathan Halliday (IBM)** 36:07 Yeah, this one's not urgent, but if no one's got anything else, we'll talk about it a little bit.
One of the many things that we do here at IBM in the OpenJDK engineering team is Project Leiden. So this is… Essentially a head-of-time compilation. You run the VM under load in a training environment, and then snapshot certain internals from it, class metadata, compiled methods, whatever, and you can reload them and subsequent runs of the VM, and it gives you a faster startup. So, yay, great.
**Trask Stalnaker (Microsoft Corporation)** 36:45 Can you compare for us to Grawl?
**Jonathan Halliday (IBM)** 36:48 Yeah, yeah, yeah. So, This is essentially, the OpenJDK team, which is not the same as the Graal team inside Oracle, having a look at the stuff Graal did for Native Image, and saying, hmm, there's some nice ideas here, what if we can, steal some of them and build them into OpenJDK instead of GraalVM?
So it's, yeah, it's filling a similar kind of… of use case, where the users are saying, hey, Golang starts instantly, Rust starts instantly, we want this, but all our people only know Java. What do we do now?
So it's… it's kind of targeting the organizations who are, you know, very heavily invested in the Java ecosystem and… and want fast startup for microservices or… function as a service kind of environments as well. So yeah, same use case as Graal, different implementation.
**Trask Stalnaker (Microsoft Corporation)** 37:46 Cool, thanks.
**Jonathan Halliday (IBM)** 37:48 So yeah, this… this obviously is very environmentally sensitive, so you need to be running exactly the same version of Java that you trained it on, you need to be running it on exactly the same CPU architecture, you need to be running it with exactly the same class path, and, you know, all of that is taken into account. The archive kind of captures that environment and makes sure that the environment in which you're trying to reload it is identical.
And that works fine up to a point, but one of the things that breaks it is agents, because the behavior of the agent is kind of opaque to the the VM, it doesn't really know what the agent is doing.
And the agent can kind of transform class loading behavior, and transform methods that are going to get compiled, and so on.
And there's no guarantee it's going to do that the same every time, so if it transforms a method in one way in the training environment, and for whatever reason transforms it differently in the production environment.
that invalidates the assumption that Lehman is built on, that the, you know, the class is the input, and as long as the class file checks them as the same, the output of the JIT is going to be the same. Obviously, if you transform the class between the The point where it's in the class file, and the point where it's jittered, that breaks.
So we're heading towards a world where… yeah, exactly, there are, users who are going to be saying, hmm, we like OpenTelemetry, we use OpenTelemetry, we like the agent, but we also like this latent thing, we like the fast startup. Can we please have both?
And right now, the answer is, no, you can't. This is… this is not possible.
So, some of our latent engineers have been looking at this, and trying to develop some guidelines or some thinking. Is there a way that we can let agents do at least a limited subset of what they can currently do?
and play nice with Layden in some way.
And one of the agents they've been looking at as a kind of test case for this is the OpenTelemetry one.
At some point, one or more of those people might show up and start asking questions or making suggestions about the way OpenTelemetry works in order to try and well, inform what Leiden is doing, because ideally we'd like Leiden to play nice with any agent.
but also potentially, say, hmm, if you could tweak the OpenTelemetry Agent to please not do this nasty thing it's currently doing, or… please do it in a different way using this shiny new API we introduced.
That would really help it play nice with Leighton.
So, that's where we are, just giving you a heads up that, These things might be happening somewhere down the road.
**Trask Stalnaker (Microsoft Corporation)** 40:47 Cool, yeah, definitely extend our welcome to, that team that, you know, we'd be more than happy to chat and cooperate in ways that we can.
**Jonathan Halliday (IBM)** 41:04 Yeah, that's great. Well, no doubt they'll come this way when they're ready.
But meantime, I'm kind of keeping an eye on them as well, and potentially, if I get a break from doing profiling stuff, I might… might get involved on the fringes of that. I'm not really a JVM internals engineer, I don't get involved at the sort of C++ code level that they do, but some of the agent work I might do.
**Trask Stalnaker (Microsoft Corporation)** 41:28 Cool, thanks.
**Jason Plumb** 41:29 Not sure entirely how related this is, but we, you know, a long time ago we had a contribib module that did… Build time instrumentation.
I don't know if that's worth ever, like, looking at or reinvestigating, if there's, like, build time stuff that helps with some of this problem or not, but… That module was unmaintained, and we ended up dropping it, but…
**Jonathan Halliday (IBM)** 41:53 Yeah, I looked at some of that when I was looking at making OpenTelemetry work with Graal native image, and… I was looking at the idea that as part of the build pipeline for the native image, you can run the… the instrumentation, and basically capture the output of the instrumentation, so the modified classes, and then just put them on the class path. So, on runtime.
they're… they're not actually getting transformed by the agent, because they've been sort of pre-transformed. Exactly. So that bypasses a lot of the… problems with Layden, except that the agent also changes class loading behavior and changes some of the Java internal classes, which is a big…
**Jason Plumb** 42:33 Yeah, that was something that definitely wasn't reached by that module.
**Jonathan Halliday (IBM)** 42:36 Yep.
**Jason Plumb** 42:37 Dip.
**Bruce Bujon** 42:41 We see that, huh?
Abdel time.
Transformation working, I mean, as part of Datalog, which is part of the mirror, not exactly the same, but yeah, for GRA and the TV image, we got it working, so… If you want to have a quick look at our source code, how we did it, what kind of… Argument we use for native image, and how we set up the build and class path there.
feel free to have a look, if it turns.
**Trask Stalnaker (Microsoft Corporation)** 43:12 Cool.
Yeah, I think that somebody was doing… a couple of people were doing some experiments, let's see, there was… Somebody from Alibaba was working on… The… Let's see, not… Merged.
Yes.
I'll just… Throw a link, I don't… Remember… details, but I remember they were working with some GraalVM folks to support some of the stuff.
But I love the… I mean, it's great, for this to be coming into OpenJDK, and, yeah.
Would love to see that, see the agent.
Work over there, so… Yeah, yeah, hope to see books from that project.
Show up.
Or let us know if that's something, you know, we can show up in their space. I'd be happy to join and, you know, have some… Intro chats, at least.
**Jonathan Halliday (IBM)** 44:47 Yeah, that's great, I'll pass that along. Thanks, Trask.
**Trask Stalnaker (Microsoft Corporation)** 45:00 Cool, anything anyone else wants to chat about today?
Abdel, that is probably… maybe, post that in our Slack channel.
To discuss, I'm guessing that's a… More than a… off-the-top-of-the-head kind of.
Answer.
Alright then.
Good to see everyone!
**Jack Berg (Raintank, Inc. – Grafana Labs)** 45:35 Take care. Bye.
**Trask Stalnaker (Microsoft Corporation)** 45:36 Right.
**Pranav Sharma** 45:37 Bye-bye.
**Abdel Elyagoubi (Sofrecom)** 45:38 Take care.
