SIG: Semantic Convention Tooling
Date: 2025-10-22
Duration: 58 minutes
Zoom Recording URL: https://zoom.us/rec/share/HglGO6NGXGX_5SUmLRmuwWkUp9oJ1baEEtvFjHuzbyKB3CfsaBQqUjQI7n8Ak3g.eLqHzI8xss51l2zv
============================================================

## Zoom Recording Transcript

**Josh Suereth** 00:00 Beauty.
**Jeremy Blythe** 00:53 Good morning.
**Liudmila Molkova** 01:30 Hi, folks!
**Jeremy Blythe** 01:31 Hello.
**Josh Suereth** 01:38 Hey, is my audio working now?
**Liudmila Molkova** 01:40 Yeah.
**Josh Suereth** 01:41 Alright, sorry about that. Okay, how y'all doing?
**Liudmila Molkova** 01:46 Good, huh?
I'm not upside down today.
**Josh Suereth** 01:50 Yeah, you went to the Upside Down, and got out with your powers of telepathy, I think, right?
**Liudmila Molkova** 01:56 I hope so.
**Josh Suereth** 02:01 Alright, so, I wanted to talk about V2 Resolve schema. There's, like, two other things I want to talk about that I threw on the triage board. I might have to leave in 30 minutes, so apologies.
I'm not sure. Anyway, let's try to get through triage quickly, if we can.
Oh right, I need to kill this triage project board for the Weaver one, which is a to-do.
That I haven't been able to execute on, so apologies. Let's go to the Weaver one. We have two PRs that were added that were, I think, significant. We should think about pulling them in. So one was, we have the Panic and Weaver bug, and then we have a Panic and Weaver fix.
So this, someone was kind enough to submit the fix for the panic.
I made one suggestion here, which is basically, there's an error message.
Wait, what the heck? Mismatched types?
Oh, yeah, Clippy's probably saying the same thing, I was saying. Anyway, okay. Get out of there.
I think this looks okay. This basically just removes the panic and has a return of an exit code, right? The thing that I'd like to see, though, is if… this exit code could be for one of two reasons. One is the dry run fails, which means the markdown is out of date.
And the second is, there's just a failure to talk to your file system, or, like, write strings, or allocate memory. In which case… we have no frickin' clue what the heck happened, right? But the error should be somehow before that, so… Anyway, my suggestion is we should actually have a, if dry run, use an error message like this, otherwise the one they have is fine.
Because we really don't know what's going on.
**Liudmila Molkova** 03:55 Okay.
**Josh Suereth** 03:57 I'm actually… it looks like this is not building, and I think it's not building because they use two-string instead of two-owned, which Clippy hates.
I don't know why Clippy hates one versus the other. I think two-owned is more Rush General for turning a reference into a… non-reference. But anyway, I would… this is a first-time contributor, I think it's awesome. I'd like to merge it, and I think this is a good fix. Wanted to run by other maintainers, like, do you think we should just… fix this and then merge it ourselves, or should we, like, post a fix to the PR and merge? Like, I'm not sure what our convention here is.
**Jeremy Blythe** 04:36 I, I, I, I looked at this as well. I think it was written by Claude.
Okay. And also, I'm wondering whether it's a… I'm just not sure about this if hasError.
thing. I'm not sure that's the pattern anymore, because don't we have the diagnostic messages, and then if there are any diagnostic messages, then… It… we produce an error anyway? Like…
**Josh Suereth** 05:08 We… we did something special here, and this is… you can blame me for this, because I wrote this code initially. You're right that there are diagnostic messages, and we dump them out later, but we also log them right here.
**Jeremy Blythe** 05:22 Right.
**Josh Suereth** 05:24 So, if you looked at the error that, is it Michelle?
McKelly?
the original, like, thread that led to this Was basically all of the output was printed that we want.
And then we also panicked.
**Jeremy Blythe** 05:43 Yeah.
**Josh Suereth** 05:43 And when I looked into it, I think this is what's doing the logging of everything we need, the diagnostic messages.
And then, instead of panicking, we just need to return. So I actually think this is okay.
If we wanted to, we could actually have a, right here, log the error and return an exit code of 1. I think that might be fine, too. Move this entire thing up into there.
So that we log the error and return exit directives?
I'm also fine with that.
The reason why we aren't doing that right now is we have to aggregate across every possible individual markdown file. So we're logging errors for them individually.
**Jeremy Blythe** 06:33 Right.
**Josh Suereth** 06:35 Yeah, that's the whole, I'd rather have all of the errors from all of the markdowns show up, instead of just the first one, in case… You know, it's unrelated.
**Jeremy Blythe** 06:46 Yeah, I guess I was just wondering whether there was an opportunity here to… Make things more consistent across all of the commands.
**Josh Suereth** 06:53 I… I am absolutely fine with that. If you think this is cloud-generated,
**Jeremy Blythe** 06:59 I think it is. If you look at the PR, I think it even says on the PR.
**Josh Suereth** 07:02 Does it… I didn't actually.
**Jeremy Blythe** 07:03 Under that.
**Liudmila Molkova** 07:07 But why would it be a problem? I mean, it's…
**Jeremy Blythe** 07:09 that it's a problem.
**Josh Suereth** 07:11 Oh, yeah.
**Jeremy Blythe** 07:11 It's not that it's a problem, it's that I'm not sure that the person, like, put a lot of love and care into understanding exactly what to do, they just went, hey, Claude, fix this.
**Josh Suereth** 07:22 Yeah, that just means that we're… I'm hoping we can get more contributors, but getting Claude as a contributor is not the same as getting a person as a contributor.
**Jeremy Blythe** 07:31 That's my point, and it's, like, Claude's fine to use, right? But it's… but understanding… understanding more about What a digital fixing is.
**Josh Suereth** 07:41 Yeah, well, this is also the case where, like, if we want Claude to be a contributor.
we should be… we should be setting up, like, the GitHub co-pilot rules and things, and having it fix bugs for us, as opposed to… like, because I think there'd be value if we continually refine the instructions used.
As opposed to them being someone external, right? Like, if we can get the instructions, that actually gives us velocity over time, because we'll have an AI agent that can fix bugs for us.
**Jeremy Blythe** 08:12 Yeah, I've heard horror stories of other… Open source projects, just dealing with… PR slop, I don't know, PRs which are just AI slop, and all you get is, like, oh, I'm fixing things that Claude's done that will… Copilot's done.
I don't know if we want to think about that.
**Josh Suereth** 08:32 I'm… That's something we can think about later. The main thing is, I want to consider this fix for the next release. If we're not happy, like, I actually think this is dead simple, it fixes the bug, I do think the error message needs to change.
Ideally, but I'm actually okay with it not changing it. The fact that this is too… I said too old, the clawed thing makes sense.
If they update this, great. If not, this is actually, like, I don't know, 10 minutes of work for one of us, if we need to. I was hoping someone would do this that would become a contributor, but Claude is not a new contributor for us.
**Jeremy Blythe** 09:10 The other PR that you're gonna get to, I think, is more interesting in this.
**Josh Suereth** 09:14 Yeah. Okay.
**Jeremy Blythe** 09:15 less… less AI.
**Josh Suereth** 09:18 We'll go to the other PR, because that one is actually super interesting.
Where did I put it?
This one here.
**Jeremy Blythe** 09:27 Yeah.
**Josh Suereth** 09:29 So this is basically talking about how to deal with authentication with remote archives going forward.
So, there's a PR that adds an auth token option.
Which would be, I believe they were saying it'd be the bearer token?
In the authorization header.
And wasn't sure if this would be safe. So, I wrote down my thoughts on this PR, which is basically, I think whatever we do.
We should match, kind of, curl's command line structure for auth on the command line.
And then, if you want to have something advanced, we do it in a config file.
Is the basic gist.
**Laurent Querel** 10:12 Makes sense.
**Josh Suereth** 10:15 Go ahead, Jeremy, you have thoughts here. I think you were… Looking at this as well.
**Jeremy Blythe** 10:19 Well, I had a quick look at it, and I'm like, oh, I really like this, because I wanted to solve… I wanted this solved.
Yeah. I think that's as much It doesn't much as I did, actually. I just went, oh, this looks interesting, but yeah, I was worried. I think, I think he says in here, open for discussion, what happens if you've got a chain of dependencies, and you need… I need this auth for this one, and I need this auth for that one.
**Josh Suereth** 10:47 Yep. Because we've got… we've got the manifest file, and then…
**Jeremy Blythe** 10:50 He's saying, yeah, but we can't put that… we can't embed the authorization inside of the… manifest file, clearly we can't. So somehow we need to be able to go… when I… when I write this authorization thing, I need to understand my dependency chain so I can… so I can match the right authorization to each thing in the chain. So I think it's a harder problem.
than… just the first thing in the chain, right? So, like, in my case… Right.
In my case, I could write an application, but, My next thing in the chain is a private repo for my company, and then that repo then goes to OpenTelemetry, which just… doesn't need authorization on it.
So there's, like, it's actually the one in the middle that I need to auth on, right?
**Josh Suereth** 11:41 Well, that… this is why my thinking is, like, for simple auth cases, it's curl.
Right? You just throw something on the command line, that's how I auth against the thing there. If we need auth for, like, I need an auth token for a particular repo.
We probably want to create some sort of config.
That you could have, that we can pull in.
Or, like, some way of getting that off.
**Jeremy Blythe** 12:06 Whoa.
You'd need something that's secret, right, to… You need to make a doc file or something that you don't.
**Josh Suereth** 12:14 But…
**Jeremy Blythe** 12:15 Right.
**Josh Suereth** 12:15 I would prefer us to rely on other things that keep secrets, so our config would say, here's the secret manager to use and talk to.
**Jeremy Blythe** 12:23 Okay.
**Josh Suereth** 12:24 Yeah.
But it would be, like, for, you know, here is the key… The way I envision our config would be, here's the key I go to to get… or here's the secret manager I'm integrated with.
And then we would go ask it for auth for particular things. Or here's the key to use in the secret manager to get the auth, right? That kind of a thing. Not like we would actually store the auth in our config file, no. That…
**Jeremy Blythe** 12:47 No, no.
**Josh Suereth** 12:48 That's Frog Apparel.
**Jeremy Blythe** 12:51 Yeah, didn't do that.
**Josh Suereth** 12:55 I even… I'm not a huge fan of having it on the command line, too, personally.
**Jeremy Blythe** 12:59 Number 2.
**Josh Suereth** 13:00 Just, for history reasons, right?
But at least this is something, you know?
**Liudmila Molkova** 13:06 Jeremy, I'm curious, why would you want this? Like, why would you keep your telemetry schema secret behind authentication?
**Jeremy Blythe** 13:15 Oh, only that it's in a private company reaper.
**Laurent Querel** 13:19 Yeah, the same thing for us. I mean, every, So, for example, we are using a combination of GitHub Enterprise and GitLab.
and CI pipelines, they don't necessarily have access without authentication to to those internal repos, where we leave the… the customer histories.
**Liudmila Molkova** 13:42 Oh, okay. But then…
**Laurent Querel** 13:43 I think it's.
So, sorry, go ahead.
**Liudmila Molkova** 13:47 And this is part of the solution, because the talking you get, it's dynamic. It, I don't know, it can last for a day, or 30 minutes, or something.
**Laurent Querel** 13:57 Yeah, the solution that needs to be implemented, For a full support for an enterprise scenario.
Indeed, more complicated than that.
But it's a… it's… I think it's a good, a good start.
We need to go in this direction anyway, if we really want to enable the custom registry story.
brought on top by this, and not just for our basic project.
Because, obviously, they… at the minimum, they will have one or two levels in the custom registry stuff, and they will all.
**Jeremy Blythe** 14:35 be sold in…
**Laurent Querel** 14:37 pilot repositories.
In a best scenario, the same mechanism for notification, in worst-case scenario, with various, with various systems.
An example for us, for example, I think we have some projects relying on GitLab and GitHub Enterprises at the same time.
Because of some dependencies.
**Liudmila Molkova** 15:06 Assuming we used Git, like, if we could recognize it's a Git repo, and we used Git commands instead of HTTP, requests, the credential manager will take care of itself through the Git Credential Manager.
**Josh Suereth** 15:25 Does Gix… I think Gix does use that, but we're not… we're not actually using Git, the command line, we're using Gix, which is like a Rust implementation of Git. It's like using, JGit and Java, if you will. But I think GIX might actually integrate with that in some fashion. I'd have to look.
Yeah, I don't know.
Yeah, because GIX might actually literally depend on the Git source code. I don't remember if it's a complete reimplementation.
**Laurent Querel** 15:52 It's a complete.
**Josh Suereth** 15:53 It's complete? Okay, never mind then.
**Liudmila Molkova** 15:58 Cool, I didn't know, I thought we'd just go to the link and download it.
**Josh Suereth** 16:04 No. No. We have, we have a Git implementation in, in Weaver. If you ever wondered why Weaver's such a large mega, like, binary, So basically, Tokyo and Git.
Are kind of embedded in it.
**Liudmila Molkova** 16:21 Okay, interesting.
**Josh Suereth** 16:22 Or, sorry, pieces of Git, I should say.
Okay, It sounds like, we're supportive. If we can get a few folks reviewing this, I'll do another review over the actual code itself. It looked pretty clean, but I didn't do a review, and since this is a first-time contributor, I wanted to do a review before I approve the workflow, just to prevent, injection attacks on our, pipeline. Like, again.
I want to make sure we're all aware of that. Do not click Approve Review Workflow until you've actually looked at the code.
Yep. Anyway, cool. But, this discussion I thought was really interesting, so I wanted to talk through it. Let's go back to our agenda then. Those were two new PRs that are in, so… First PR.
That's interesting.
Easy to fix.
Second PR… Good first step.
Need to sort counts.
registry. Okay.
Cool.
Since I might need to leave in 15 minutes, I want to talk about V2 Resolve schema Design.
So, primarily, I've… I got… the PR that everyone reviewed, I only wanted you to look at the high level, not details yet, because it's not ready. But thank you for all the reviews, I think we got the discussion we need there. There's a few important things.
One is, I just got merged into main and updated all of the, all the code. So, like, or all the tests. So all the tests are now passing.
It doesn't support attribute groups yet, so I need to add attribute groups.
This led me to thinking about catalog versus registry.
Right now, the catalog is just a list of attributes.
Going forward, I need to track attribute groups. Plan is to do lineage for that.
Oh, and since we're reverse engineering from V1 schema, I might have to add lineage tracking for things from V2 in V1.
and then reverse engineer them in V2, that's what I did for groups, as you saw. We're tracking if one group extends another, and that's how we're tracking refinements.
So, long story short, I'm thinking about having two things, and I don't know if we want to call them catalog versus registry, or… because, actually, in SEMCOM, we call this thing a registry, not a catalog.
So, naming is hard here. Catalog and registry both kind of mean the same thing.
Basically, thing 1 is used for documentation conformance checking, it's live check. This is just… this… everything within this must be something that shows up in OTLP.
like, every piece and information that we have outside of, like, extension mechanisms, like annotations. So the idea here is, you know, Spans, we need a way to identify spans, we've already talked about that, and we want that to show up in OTLP somewhere.
This would be used by LiveCheck. You can take the catalog, throw OTLP at it, and confirm that, like.
Everything lines up.
The registry is what's used for code gen.
The registry is like, okay, cool. Generically, we have a database span concept, but for, you know, Postgres, I'm going to have a specific set of things where I can hard code attributes, for example.
And so, I have a refinement of the database spin.
that is specific to Postgres, and I can code gen from there.
Everything that shows up in catalog, as you saw, I'm copying into Refinement.
As well. So there's a raw… like, if I have a metric defined, it shows up as a refinement of itself.
with no modifications, but I can make a new ID to refine it further and limit things, right? Refinement should never break compatibility.
which we have to find a way to make sure we enforce in the model or some way, so it's not important to live check to understand refinements. Live check would not have to engage with refinements, for example. When I document things, maybe I do want to document the MySQL-specific things, and that's fine.
But my thinking is the default documentation we provide should be only at the catalog of all the stuff.
That's, like, what we provide out of the box, is here's a catalog of all your things.
**Liudmila Molkova** 21:13 A few thoughts.
**Josh Suereth** 21:14 Yeah.
**Liudmila Molkova** 21:15 We… Do… Have refinements today, in whatever form they are.
And we do document them, and we would absolutely live-check them, so if I see it's a Postgres, I can live-check Postgres-specific.
Things.
**Josh Suereth** 21:35 How do you know to Postgres, or to live-check Postgres-specific?
Like, how do you know it's Postgres at that point?
**Liudmila Molkova** 21:42 to be… System name as Postgres?
**Josh Suereth** 21:47 So what you're saying is inside, like… like, if we think of this practically, in span refinement.
you're refined by something, and we need to understand that classification, then, to do the live check. Like, generically, how does LiveCheck know to use the Postgres refinement group ID?
When does it know to do that?
**Liudmila Molkova** 22:09 It could, the custom policy could.
based on the span I spent time And, something else.
**Josh Suereth** 22:16 Yes.
Generically, how does Weaver do that?
**Liudmila Molkova** 22:21 Generically, now it would not.
**Josh Suereth** 22:24 We could.
If we are stricter on what refinement looks like.
So, if we were to say, right, in a refinement, this refinement Has this enum, Of exactly this value.
Okay? And we make that formal in the model.
then… then I think you're right, LiveCheck could, interact with refinements directly. And then what I'm doing here doesn't make any sense.
**Liudmila Molkova** 22:52 I'm kind of curious, why do you want this split? How is it helpful?
**Josh Suereth** 22:58 My goal, my goal is twofold. So, one is, I want, the raw, like, definite, like, The other feature that Jeremy made was the one where we synthesize a bunch of data and fire it out OTLP.
What I want that to be on is this.
So basically, the idea would be, I need to build a set of alerts, dashboards, you know, transformation processing, whatever.
This is what I use.
effectively, I split things into generation and consumption in my head a little bit. This is my consumption experience. So, I need to make alerts, I need to make dashboards, I want to make sure they're stable, I want to design that. I would use the thing that synthesizes data on this catalog.
**Laurent Querel** 23:51 And why not, why not Joshua, Josh, I mean, if I'm building a dashboard, or if I want to test, To generate synthetic traffic, telemetry traffic. I also like to get the… The specialized matrix, or the specialized event.
What?
**Josh Suereth** 24:13 The specialized metrics are instances of this metric. They have to conform to that shape.
But the name of this… okay, so the name will be the… The name cannot be changed.
**Laurent Querel** 24:26 Yeah, okay.
**Josh Suereth** 24:26 The metric name here is the same as the metric name there.
**Laurent Querel** 24:30 Okay, goodies.
**Liudmila Molkova** 24:35 And if I have, let's say, some of the… I don't know, for Postgres, I have a bunch of Postgres-specific metrics, and some of the metrics that I'm inherited, well, refined from the catalog.
then I'm dealing with… and I could build a dashboard that's… That… that uses both.
And then… It's… it's kinda… I'm not sure if as a user I would understand.
the difference.
**Josh Suereth** 25:08 That's… that's my fear here with refinements, but remember… sorry, I actually booted myself off, somehow.
The thing to remember, though, is that this metric name is the exact same as this metric name. A user can't tell the difference between the two in a dashboard. The spam name…
**Laurent Querel** 25:26 The description is different, but the notes are potentially different, and so on, so it's important for a dashboard or for a query.
A query engine, right?
**Josh Suereth** 25:36 Yeah, but how do they… how… like, okay, practically, though, they aren't going to do that. They're not going to have that distinguishment.
Today. Like, if you think about, like, definite descriptions in Prometheus, right, the help message shows up to describe messages. It's on a per-metric basis.
it's not on a, like, refinement of a metric basis, that refinements are not a thing that those systems have today, or show.
So unless… unless we… we find a way for refinements to somehow Show up in these databases and stuff.
I don't think we're going to be… like, I don't think there's value in that. Well, sorry. I think there is value. I don't think there's, a practical way to have that value show up.
I think we're starting to destroy the cardinality of these data storage side, and we're actually designing a system that they couldn't support.
Like, just getting them to have metric descriptions and descriptions on labels.
That… that's like a win. But if we try to go and say, cool, and on a per-metric basis, there's gonna be different labels for… and different descriptions for every possible thing in here.
I… we're really gonna struggle.
Right? This is where I think the notion of a generic metric versus a specific metric shows up, of… Cool, I have a generic RPC metric.
If I need to have something specific to, like, gRPC, it's gonna be gRPC-specific. And then it has its own descriptions and customization.
**Liudmila Molkova** 27:12 So how would this difference manifest for the… end result schema. Like, there will be two… Top-level properties, catalog and registry.
**Josh Suereth** 27:25 Yep.
**Liudmila Molkova** 27:25 Or… What if we call the first one registry and the second one refinements?
**Josh Suereth** 27:32 I actually like that, because I hate calling it catalog and registry, I'm just keeping the terms. So let's say if we call this registry, and we call this Refinements.
I'm fine with that, right?
But my point here with refinements is some of the things we're trying to do with refinements I don't think are practical on the consumption side.
**Laurent Querel** 27:56 So… I have to admit that I have some gap in the understanding.
Most likely because I didn't follow as I should.
All the detail, but, so the concept of catalog initially was there… I mean, independently of the name?
The catalog was there to… make unique… Instances of signal description.
Because sometimes we have the same, let's say, base signal used in different contexts, with some variations.
And the goal was… once we have something that is fully reserved.
How can we minimize the number of duplication into the artifact that we will deliver at some point?
Like, the result registry, that will be something that will be versioned on GitHub or whatever.
So that was the purpose of the catalog initially.
And that's why we have indices, 1, 2, 3, blah blah blah.
To represent… because we can't name them, multiple entries into this catalog will have, in fact, the same metric name.
Except that the, they, they, they have slightly, small differences.
So, I'm trying to reconsiderate that with, the refinement mechanism… .
**Josh Suereth** 29:45 So, refinement right now, the way refinement works today.
Right? The name is the same.
There's an explicit link that says this is a refinement of that.
And there are things that you cannot change in a refinement, right? Like, that I cannot actually break the stability of the metric in any way, the stability of the span, I can… I can't, I can't remove required attributes, for example.
I might be able to say this recommended one won't show up.
I might be able to say this enum only has this one value.
And I also require a unique ID for the refinement.
So, the refinements have to be addressable.
Like, I have to say, this is the MySQL refinement of database spin.
So there's an ID.
But the… and there's a clear link to the original name of the original span that represents the abstract thing.
Okay? Implicitly, what I've done in this to make CodeGen work and everything, every single metric, end event, N entity, end span, has a refinement that is basically the no-op refinement, where the ID is the same as the name, and there's no changes.
But my thinking is the reason we're doing refinements is to make Cogen easier.
And to make it… and to make it more clear when I write instrumentation for MySQL, what MySQL is going to do, versus the generic database thing. So I want that use case to be supported.
However, that use case is really specific to instrumentation. When I think about the user of the registry, if you will.
That's the person who's writing a dashboard about databases.
They can expect any database to show up, and so them interacting with the general metric thing makes sense to me.
If they're making a MySQL-specific dashboard, that's where things get more interesting.
Where they don't care about every database, they only care about MySQL.
**Laurent Querel** 31:51 Should we not, in that case, integrate… so, is there any kind of attribute in those signal that represents the… the refinement. I mean, the name of this refinement. If it's MySQL.
So the database model, or database vendor, or whatever is the name of this attribute.
Is a refinement also coming with something that will identify During the runtime, so something that is accessible from a dashboard system.
Or from any downstream component, That is participating to the observability of the system.
We'll use to, refine, basically, the understanding or the semantic of this signal that has the same shape, okay?
But not the same exact semantic.
Or the same exact restrictions, like you said, for the alien, for example.
So is there such a such mechanism? In that case, Refilement will be important also.
During the runtime.
could be leveraged by dashboard, could be leveraged… more importantly, could be leveraged by AI-assisted query engine.
Because knowing the, the, the nature of a… The nature of the producer of a metric that shares the same shape with another similar Producer of telemetry, but with a different flavor.
Would be interesting.
**Josh Suereth** 33:22 I agree, it could be interesting. I think the main problem we have now is we can't tie the knot. So is it theoretically possible that we can understand this. Yes.
Do we have that today? No.
Today.
**Laurent Querel** 33:39 Could we… could we, in the semantic convention, define some kind of attribute that make that possible at some point?
**Josh Suereth** 33:47 I don't think I… well, first of all, I don't really want it to be an attribute. I'd rather have it be something more implicit.
But, for example… Okay.
We have database system right now, right? If we say, when you refine something, you have to put a constraint on the original definition.
That constraint is what you would use to understand the refinement applies.
Now, the problem is, from a practical standpoint, we could use this for live check, then, and use the refined things. From a practical standpoint, though, when do I know that that constraint applies, and how many of these will I have in practice? Right? If I'm writing a database system, or even an AI that needs to evaluate stuff.
Do I have to go through, like, you know, a thousand-some rules to understand all the possible refinements to figure out what the description really is? That's almost impractical at times. We need, like, we need to keep things simple, key-value hash maps as much as possible.
For… A lot of the stuff that we do.
And… when it comes to, like, the value, we are trying to create this T-shaped idea, right?
the value of having a general-purpose RPC is you don't need to know the system to use it effectively. So if we've designed something where the AI has to drive through to refinement.
to use the span effectively, I think we've already failed.
Now, that said, if the AI finds its MySQL, and then engages with a subsystem to do further refinement, and further investigation of MySQL, I'm fine with that. That makes a lot of sense, right?
But what I would disagree with is, do you have to do that from the very first, like, that first metric is meant to be Figure out where generally things are wrong.
not, I need to know it's MySQL specifically, or I need to know it's… like, I shouldn't… if you've designed a metric where I have to know the refinement, I think we've failed, is the TLDR.
In the design of that metric, or that span, or that log.
**Laurent Querel** 35:56 Yeah, I'm not sure to capture the… I think I understand what you're saying, I'm not sure to capture the real problem for what I was saying, because for me, it's part of the context.
Not necessarily part of the identity of the metric, where you have a list of attributes that will participate to the aggregation, but there are some families of attributes that just represents some kind of contact that you can use to identify the producer.
And, I mean, it's a regular thing, it's not something that is, out of this world, in my opinion. And, I don't see why… We could not… Just provide this context optionally.
to, to help, and that could be done, I don't know, as a metadata, as an attribute.
We have to define that, but I don't think that it's a big deal, and it's a failure at all.
**Josh Suereth** 36:57 I think you could.
Like, it's a… okay, let's talk about, like, what I'm going at for here is the general usage and the well-lit path.
Right? Advanced stuff, sure. Like, theoretical stuff, sure. I gotcha.
That's not what I'm after here. I want to actually… the thing I'm worried about is I think refinements are really hella complicated.
In practice, in use. And I don't want them to be, because we've decided we need them.
Right? Like, it optimizes CodeGen in a way that we absolutely want. And so, how do we make it so that… that use case of, cool, I have a general Semconv and I have a refinement, is not a pain in the ass for everyone to deal with?
And so, what I'm looking at here, this design is effectively cool. Live check, by default.
We'll use the registry and make that dead simple.
Documentation. By default, we'll use the registry and make that dead simple.
Okay?
Refinements, by default, CodeGen will use that, and make that dead simple.
And we'll code Jen against refinements.
**Liudmila Molkova** 38:05 In my mental model, it's slightly different, not in general, but generic. So if we take semantic conventions artifacts, they would only generate registry or catalog.
If you want to provide, let's say, documentation or code gen for a specific library, it would only generate the refinements first that apply to this library.
It's like the generic versus specialized. This is my mental model.
**Josh Suereth** 38:37 Yeah.
Yep.
Yeah, I think that's… that's fair. That's kind of what I'm getting at. But then, this… this gets into, like, the… what do you… what do you experience in our JQ?
What do you experience in, in live check, Rego, right?
And what do you experience… what do you… what do you deal with in Rigo generally? So, in terms of DIF, I really don't want to be diffing refinements. I don't think there's a lot of value in expanding diff to handle refinements. I think that's going to be… a huge pain in the ass with not a great set of value. If we can make sure that refinements are always just specializations and cannot break the model of this, we can just do diff at the catalog layer, or, sorry, at the, registry layer, and we're good.
When we have backwards compatibility and everything we need.
And then… Okay, cool. So, if we're on board with that.
I can… I can keep working on Resolve's schema design and update it so that, I'm gonna get rid of catalog, and I'll just call it Registry and Refinements.
in the resolve schema V2. We can… we can evolve from there, but the registry will have the attributes, the attribute groups, the metrics, the events, the entities, the spans, and they will reference each other. I'm actually thinking about making everything be a deep link to it… to each other, so if I reference an entity from a metric, it will actually be a reference to it in the registry.
For example.
I don't know if we expand those when we do CodeGen, because that might lead to a ginormous thing in WeaverForge, we can talk about that later. But yeah, they'll be… they'll reference each other for a compressed registry on Resolve, and then in Forge, we'll expand it out to be usable for Cogen.
Refinements, similar thing. Refinement will refer to the registry.
With the extension that it's doing.
Okay? In Forge, though, refinement will be Expanded out with all of the stuff.
We might want to have command line configurations about whether or not you engage with these, or my thinking is there's literally a namespace now. So instead of just context, you would have registry and you'd have refinements, and you can engage with whichever one you want.
in… JQ, and then, brain's not working, Jinja, and Rigo.
Okay.
And then we need, like, a documentation defining, like, this discussion of, like, how we feel about registry refinements, when to use one, when to use the other, what the goal is. I honestly think for very simple use cases, if I'm doing my own library, and I'm not semantic conventions, I just make a registry, and I don't care about the rest of it.
**Liudmila Molkova** 41:45 Right.
**Josh Suereth** 41:46 In semantic conventions, I think we need refinement, so then we engage with it. And we make it dead simple for people with those two, like, I consider those the two users, right? We have three users. We have semantic conventions itself.
We have dead simple, I just want to define a metric in CodeGen and Doc, and write it. And I don't do anything else. And then we have multi-registry.
And those are kind of the three things we should be optimizing for.
Multi-registries where I am the weakest in terms of understanding what we need, so this is where Jeremy and Laurent, I need you to help evaluate this.
But given the discussion we had, given the way we're thinking about this, this is what I'm thinking of for V2 registry. And I'm pretty close to having an implementation.
So, I think we can actually get to this relatively quickly, where we can start using this in… live check, using this in Forge.
And at that point, I would like to have help integrating those, so my… okay.
My thinking, if we can agree on this… I will make the Weaver Resolver fix, I'll make the initial WeaverForge proposal of what the schema looks like, with some helper methods to generate it.
And then, with some help, if someone could take on the Rego policy engine.
for just doing policies on V2, and then live check on V2. Are there other areas of code… well, anyway, I was thinking we could start dividing and conquering at that point.
Does this sound like a plan?
**Jeremy Blythe** 43:25 Makes sense that I look.
trick, obviously.
**Laurent Querel** 43:31 Good.
**Josh Suereth** 43:33 That was the big thing I wanted to discuss, and this is the thing that I… I feel like I'm behind on, but we're slowly making progress, right? And apologies for reading through my Rust code. I'm gonna try to figure out how to share some of the copy-paste sections, it's pretty gross, but we'll get there.
The other topic on this… V2, and attribute ref. So, the other topic on this from that PR, and I think I'm just gonna open up the PR.
Is this… this is not the right one.
Is what do we include in attribute?
Oh, come on.
So, the attribute for attribute registry, I think Laurel had a bunch of really good… questions. That's all… oh yeah, I updated this so you can see all the fixes to, to the Xtends group now, where it's now showing up in all of our example data.
Okay.
Where is… some kind of V2… no, we want Resolve Schema V2. Right. So right now.
I made the attribute match exactly what's in the attribute catalog of SemConf.
So, that was what was previously an attribute, but not requirement level, and not sampling relevant.
My rationale is that requirement level is specific to a signal.
And it is not an implicit behavior of the attribute. Whereas, I think the goal of semantic conventions would be common fields of brief description examples.
They should be generally broad enough to handle every possible signal. So while you can refine it, you are limiting the definition, not changing the definition.
when you use the same name somewhere else. Otherwise, and again, if we go… if we go into this, like, semantics and meaning.
If I have the same name, but it means different things, then we have failed at defining semantics.
So, that's the other part of that.
So I was trying to find out the limited set of what we think is implicitly intrinsic to an attribute.
That we would put in the registry.
And this is what I came resolved on. But it's… I was really lazy, because I just looked at semantic conventions and figured out what we do there, and said, okay, this is probably the right list.
do we have concerns with that, like, given that discussion? I mean, Lauren, you had… I don't remember where your comment is, but, I think you had some points around that.
**Laurent Querel** 46:27 Yeah, I need to refresh also my memory.
When's a home.
**Josh Suereth** 46:43 I think that might be in the resolver, was where you made the comments, but I don't see… Yeah, maybe it isn't lib here, then.
Oh, right, okay. I wasn't using Result when I first made that.
These are here.
Yes.
That was just not understanding the fact that we were doing it, and I think you mentioned this somewhere else. Oh yeah, this attribute rough dance.
**Laurent Querel** 47:35 Yeah.
**Josh Suereth** 47:46 Okay, so now you have the rationale, Behind why we're doing that.
**Laurent Querel** 47:53 Yeah.
**Josh Suereth** 47:54 Do you agree with the rationale, or do you have concerns with that?
**Laurent Querel** 48:13 I need to go back precisely, because I'm still not sure that, If I remember well, what was the… This comment about, it was about the fact that we… We have this concept of attribute refs, which are, sort of, set into a vector.
That we convert back to an attribute, basically an instance, And then you have backed that to another reference. I was interpreting that as just an intermediary implementation detail.
**Josh Suereth** 48:54 Oh, yeah, that was how we're dealing with V1.
to VG.
**Laurent Querel** 48:59 Okay. That was the point. Yeah, I had to get the pure attribute, and then come back to ref. Yeah, that was the point. I just want to make sure that, And I guess, I don't see why that will not be that way, but just to validate that. Once the V2 migration is done, we will not have these dumps between the… Yeah. Okay.
**Josh Suereth** 49:20 In fact, it was so annoying I had to do that. That's actually where all of the code came from, that's where all the.
**Laurent Querel** 49:26 Okay, okay, because it's, it's… Definitely builds super inefficient.
**Josh Suereth** 49:31 Oh, yeah, yeah, yeah.
**Laurent Querel** 49:33 Because of the… the fact that you, you are in a kind of O, ON, Look up into a vector to retrieve the corresponding attribute.
looks like a weird thing to do, but I understand the fact that it could be… Something easy to do for this… Russian migration.
**Josh Suereth** 49:54 It… it's still… in terms of time, it still resolves faster than the old Python code, just so you know.
If you look at the timeout.
**Laurent Querel** 50:02 Yeah, yeah.
Maybe even.
**Josh Suereth** 50:05 I hear ya, like, we need to kill it as soon as possible.
gonna be… like, I… I… if you have another algorithm you think we can use, let me know. But the reality is, I have to pull this out, and so I can't just… that's why I have to go through the dance.
**Laurent Querel** 50:23 I think we just need a hash map where we have the, The key are, in fact, the attribute instance and the value RDF set into this, Into this catalog, slash, whatever.
**Josh Suereth** 50:36 I thought I did that, actually. Did I not make.
**Laurent Querel** 50:38 No, I think what you did was a vector, and you are… you are scanning the vector to retrieve the… The… to retrieve, one by one, the… I didn't see any Ashma.
**Josh Suereth** 50:51 Oh, this one here, you mean?
**Laurent Querel** 50:53 No.
**Josh Suereth** 50:54 No, this is where the, this is where the lookup is.
**Laurent Querel** 50:58 No, no, there is a… I think it's close to the, yeah.
**Josh Suereth** 51:05 That's where your comment was.
**Laurent Querel** 51:10 Yeah, you… attribute is a vector, if I remember well. So you are trying to retrieve and to reassign an offset into this… so you have an attribute as an input.
**Josh Suereth** 51:23 Attribute's a vector, but this is an index into the vector, so it should be O of 1 lookup. It's not O .
in an ID and getting back the full attribute here.
And then when I convert ref here, that's the one that I think was the, I have to look at the V2 catalog.
**Laurent Querel** 51:42 Yeah, the covert FEF is…
**Josh Suereth** 51:47 Oh, yeah, yeah, okay. I'm, position A.
**Laurent Querel** 51:51 Yeah, definitely it's ON, it's not the ON.
**Josh Suereth** 51:53 This is a linear scan, yeah. I can… we can make this not be a linear scan, that's fine.
**Laurent Querel** 51:58 I'm saying that because if you, Once we are in the custom registry, scenario.
I will not be surprised if, for an enterprise, you have thousands and thousands of metrics and signals.
**Josh Suereth** 52:13 Yep. That are purely custom.
**Laurent Querel** 52:15 That will happen.
I mean, I already see that, here, so… When you start to have multiple thousand things that start to be a problem.
**Josh Suereth** 52:26 Well, I think the main problem we have here, and I can fix this, I can fix this in the resolution step, this is the output type.
**Laurent Querel** 52:36 Yeah.
**Josh Suereth** 52:37 So we.
**Laurent Querel** 52:37 But the construction of that needs to be efficient, yeah.
**Josh Suereth** 52:41 Yes, so what I need to do is create an intermediate type for construction that can do fast lookups. That's what I should.
**Laurent Querel** 52:46 Yes, yes, I did.
**Josh Suereth** 52:47 Absolutely. Okay, so that… that I can make happen. That's… that's actually an easy fix. And I need to go in, and I'm gonna… I'm gonna change this to be a registry anyway. So… so as I go through and do that, we'll… we'll probably… you'll see this code evolve, but yeah, I can absolutely do that.
Yeah, anything we do that is, like, a row scan like this, we should kill. Agreed.
I was also super sad that, I had to do it this way.
Because I couldn't infer an equals method, Why couldn't I infer an equals method?
**Laurent Querel** 53:26 I think you can, depending… I think the… There is nothing specific there, except maybe for the annotation.
**Josh Suereth** 53:33 annotate, we don't have an equals method on, surd.yaml that we put in annotations, so I have to go first derive equality for CERDYAML somewhere, and then we can do it.
**Laurent Querel** 53:45 That was one.
**Josh Suereth** 53:46 That was why I couldn't do it. Attributes was similar, I believe.
Stability, we also… yeah, anyway, I need to go to… there's a bunch of junk I have to clean up in this PR, but that's, like, specifics. I think you're right, we shouldn't row scan, but that's an implementation detail, not, like, a conceptual.
**Laurent Querel** 54:03 I agree.
**Josh Suereth** 54:04 I'm not focused on that initially, yeah.
Related… Do we have a, performance benchmark suite, or, like, a, you know, a, a way to do profiling on Rust for Weaver.
**Laurent Querel** 54:20 So, you have a micro-benchmarks that are available for any Rust project. Now, I guess…
**Josh Suereth** 54:26 We're looking for.
**Laurent Querel** 54:27 world.
**Josh Suereth** 54:28 Hold on.
**Laurent Querel** 54:28 Oh, good… sorry.
**Josh Suereth** 54:29 Is there a stable one?
Last I used microbenchmarking in Rust, I had to use experimental features, which I really don't want us to depend on experimental Rust to do microbenchmarking.
**Laurent Querel** 54:43 Yeah, anyway, I think what you really need is, like, something like a continuous benchmark, so that's what we put in place, for example, for, For the other project on which I'm working.
**Josh Suereth** 54:54 Yeah.
**Laurent Querel** 54:56 So we, we… We have a dedicated, server.
part of OpenTelemetry, on which we run A set of scenarios.
We, generate traffic with, with our libraries, by the way.
So we, we generate traffic, and, and then we, we have, an infrastructure to… with the system under test, so that the Rust-based pipeline engine, we could imagine that we have river That is the system under test, and we have some elements to capture the metrics that are collected, and we generate charts over Over the time, so for every commit.
That touch the main branch, we have, a data point.
We also have that for an IT with some bigger scenarios.
That's an infrastructure we put in place for this project.
we could imagine some variation of that for Weaver.
Where we try to identify if we have any performance regression for resolution, for code gen, for, life check.
And, and various other, capabilities of Weaver.
It's a big work to do. It's not… I mean, I had an engineer to work on that for more than one month for the project.
**Josh Suereth** 56:25 I… I… yeah, but that's… I don't want perfect to be the enemy of good for us.
it'd be good if we just have a test we can run to look for bottlenecks, that's all.
**Laurent Querel** 56:36 So…
**Josh Suereth** 56:37 If you have recommendations for that, Laurent, like, of, like, here's a good performance benchmarking test, I think we just want a way to performance benchmark downloading SEMCOV to start with. Like, let's just… let's just be able to run it and look for bottlenecks. That's it.
And then, evaluating over time, like, let's start walk before we run. So, let's just get something that we have a performance benchmark that you can run, that you can look at, that has an output.
That's it. And then later on, we can do all the testing over time, make sure we have a stable thing that we use to do that benchmarking, where we get consistent results from CL to CL. That's fine. At this point, though, I was just trying to figure out if I wanted to look at where bottlenecks are, how would I do so in Weaver?
**Laurent Querel** 57:24 I think, regarding bottleneck, where you need a profiling system, I think, more than a benchmark system.
**Josh Suereth** 57:31 Yeah.
**Laurent Querel** 57:33 So there are multiple profilers that exist.
Most of the code is not async in Weaver, so that simplifies a little bit the story.
Yeah, I can give you some lists of profile… profilers that, we are using sometimes here.
**Josh Suereth** 57:56 Okay.
Yeah, that'd be good. I gotta drop for, another meeting, but, This sounds like a plan for V2. Apologies for monopolizing the entire time, but I think this is, We're making good progress.
Alright.
**Laurent Querel** 58:13 I'll see y'all.
**Jeremy Blythe** 58:14 Bye.
