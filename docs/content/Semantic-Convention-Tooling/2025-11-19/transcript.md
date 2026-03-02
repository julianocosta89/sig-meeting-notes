SIG: Semantic Convention Tooling
Date: 2025-11-19
Duration: 59 minutes
============================================================

## Zoom Recording Transcript

**Laurent Querel** 00:25 Hi, Lumia.
**Liudmila Molkova** 00:27 Hello! Hi, Lauren, how are you?
**Laurent Querel** 00:31 Going well, Lance.
And you, how was, CubeCon?
**Liudmila Molkova** 00:36 It was… great, but Jeremy couldn't come.
There was a lot of flight disruptions, and unfortunately, I had to present.
his part as well, I… I didn't, I wish he was there, because, like, he is the person who actually uses the stuff, and it would be amazing to have him. But it was good.
I've heard… okay, it was fun. So, I was chatting with somebody at Grafana who hasn't been to my talk, but they told me, oh, have you heard about Weaver?
We actually want to investigate it for life checks, and like, oh, nice, you should watch my talk!
**Laurent Querel** 01:18 Nice.
**Josh Suereth** 01:22 Oh, speaking of which,
We don't have an official way to do this, so let's do it real quick.
Does anyone, like Lyudmila, would you like to be either an approver or a maintainer of Weaver?
formally.
**Liudmila Molkova** 01:39 Well, I… I would be honored to be an approver. Thank you.
**Josh Suereth** 01:43 We'll go…
**Liudmila Molkova** 01:44 project.
**Josh Suereth** 01:45 Yeah, yeah, okay. So, I think the next step is I'll open a PR that officially makes you an approver, and then the way it works is anyone here
the maintainers just approve it. That's, like, our… I had to look this up, by the way, recently, so I know our process. So we don't actually officially vote, like, the way you would think you vote, you just vote by approving the PR.
So… Cool. So I'll open to PR, because I think it's long overdue.
And then your Grafana coworkers will see your name on the list, and know.
Alright, cool.
I shouldn't probably do that in a public meeting, but you know, whatever.
I wanted to, get started, because we have a lot to get through, and there was a bunch of discussions. I have… still have a little bit of a head cold, so apologies, I'll be a little,
If I'm a little scratchy or voice cracky.
Yeah, alright, so if we look at our triage board, this one, I think I wanted to be done with this one, right?
And I still haven't cleaned it up, so let me make a to-do.
And move this here.
Dude, all this to…
Okay. We had discussed that before, I just still haven't done it. This is the one I wanted to talk through.
Okay.
So we have,
a bunch of things going on in Weaver. I just wanted to check things that are in progress.
And for next release.
So we're still working on fully resolved telemetry schema. This, I think, is being, getting a lot of pressure to…
complete quickly. So we'll talk about that in a second.
To consider for next release,
I made this too big. Let me go down a little bit.
Allow updating the new values when referencing an attribute. I think that one… I'm not aware of any progress on it right now. Is Alexandra here? No.
Alright, Weaver should resolve the full URL. I think this one, we don't have a PR for, we just have a straw man, right?
So that one's probably not going to make a lot of progress.
Weaver Diff Template Extension Weirdness. Did anyone have a chance to debug this one?
**Liudmila Molkova** 04:21 Nope, I didn't.
**Josh Suereth** 04:23 Yeah.
Go ahead.
**Liudmila Molkova** 04:30 I was just saying that I didn't have a chance, I'm sorry.
**Josh Suereth** 04:34 Okay.
Yeah, that… okay.
I'm curious if that, as we upgrade CERDYAML, if that's partly what is fixing it.
As things… Anyway…
Cool. Next one. Enable strict mode for Jinja behind a CLI option. This one got blocked, if I recall correctly. There was a PR for it, I thought.
Yeah.
And, Lauren, you were gonna look at this one.
**Laurent Querel** 05:10 Yes.
And I'm sorry, I didn't.
**Josh Suereth** 05:14 That's okay.
we might end up with higher priority things, I just want to make sure we are slowly making progress, so we'll check in on that in a little bit. Weaver cannot load registry directory beginning with a dot. This is because it's invisible.
I know that there was a fix for there, and you had a bunch of comments. Is there anything you want to say about this one, Laurent?
**Laurent Querel** 05:37 Sorry, I was writing something.
We cannot load registry directory, beginning with .
Yeah, remember this one?
**Josh Suereth** 05:50 I think Jacob opened a PR that allowed all DOTS files to be seen.
**Laurent Querel** 05:55 Yeah, that's funny.
**Josh Suereth** 05:57 I think I, I set, I need to check, but.
**Laurent Querel** 06:02 Give me one or two minutes, can you go to the next one, and I will look at that.
**Josh Suereth** 06:08 Okay. Bye.
Authenticating when using remote archive. This one, I thought we had a PR for this.
We had a back and forth. We can… this was about…
Basically, we're talking about our way forward, where I said we should try to keep things similar to Curl, and they were saying, well.
It doesn't make sense to have a full dash h header.
I do think we want to have extensible headers at some point, and figure this out, but this is what we decided for going forward.
I haven't… I haven't heard back from the author, so I'm not sure the status of this now.
If I recall correctly, this PR was,
Pretty well written, but I think it was hard-coding, like, a specific thing. Yeah.
It was, it was specifically looking at bearer token.
As opposed to just a generic header thing.
If I recall correctly.
And there was a bunch of other things in the PR that they said they wanted to…
Clean up. So…
it's still a work in progress for early feedback. I don't see any status on it from the author. Should we just leave this go for a bit, or should we do another ping?
**Jeremy Blythe** 07:41 I think you were also asking for… Laurenta.
Have a look at this one as well.
**Josh Suereth** 07:48 Yeah, to offer feedback on what you would like to see.
Yeah.
**Laurent Querel** 07:54 Okay, 97… 978, right?
**Josh Suereth** 07:57 978, yep.
**Laurent Querel** 07:58 Ricky.
**Josh Suereth** 08:01 Okay.
**Laurent Querel** 08:02 Regarding the 958, so I commented directly into the PR.
And I was asking for having,
An explicit an opt-in parameter, dash dash include Eden?
But allow exploring hidden files and directories.
Because otherwise, going directly to the dot dot, or the, let's say, the dots file.
But that could be, problematic in my opinion.
**Josh Suereth** 08:36 Yeah.
I think this is missing the point of, you still block the directory, and that's the problematic part.
I can help respond to this one, too.
**Laurent Querel** 08:53 But my answer is directly into the PR. What did you say exactly? I didn't capture exactly what you said.
**Josh Suereth** 09:01 This, this here thing that is semantic convention file only accepts these extensions.
So, it shouldn't walk… like, git config shouldn't be problematic, but the problem is it'll still look for… it'll still look in the, like, the directories, right?
That we don't really want it to go down. Sometimes just going into the directory is probably.
**Laurent Querel** 09:21 Yeah, yeah, yeah. I mean, there are so many possibilities, so many.
**Josh Suereth** 09:26 Yeah.
**Laurent Querel** 09:26 files that we don't want to see explored, or directories that we don't want to see explored. I think that should be, just an obtain parameters.
And then we assign people that want to use those .file, or .directory, it's fine, but not by default.
**Josh Suereth** 09:47 I do think it's interesting, like, we… I almost want to ask what the use case is for putting it in .seenConv.
You know.
**Laurent Querel** 09:55 Nope.
**Josh Suereth** 09:59 Anyway, okay.
Cool. So that's, that's, to release, that sort of thing. Last thing I wanted to show was,
This is… this is for a quick general discussion. If… if no one has complaints, I'd like to pull the trigger on this. I'm a bit overloaded myself to make it happen, but if we look at our pool requests, everything, everything Dependabot is struggling.
So all of these are approved, and I've been trying to merge them for weeks, but Dependabot can't, like, recreate PRs. Maybe it's fixed up now.
But Dependabot just has really been struggling. I don't think we've actually had new Dependabot bumps in a while, too.
And there's a discussion here where Trask said, most people are moving to renovate. If you'd like to switch, just open a, community issue.
After Jeremy identified that there's permission denied and dependBotCore, and it was broken.
So… Anyone have complaints if we just switch to Renovate?
Which I think most Coachella's doing.
**Laurent Querel** 10:59 Yeah.
**Josh Suereth** 11:00 I'll open a community issue, and then we have to actually do the migration, but for now, it might make sense for somebody to do a version bump on all the Rust apps manually, before the next release. So we'll just have to remember to do that, because I don't want to release with security.
Vulnerability is if possible.
We are… we are a CICD thing, so we are…
Not what you would think of attacking, but we're now the new vector of attack, by the way.
Everyone wants these build chain attacks, that's the new… the new thing.
Like, the shy hallude attack? Okay, anyway. Cool.
So that was that. Let's get into our agenda.
First off.
Have you all seen the Stability Hotel blog in discussion? If not, I can put the blog here.
**Jeremy Blythe** 12:04 Nope.
**Laurent Querel** 12:05 units.
**Josh Suereth** 12:07 Okay.
Here we go.
So, let me put it there…
Effectively, this we talked about a lot at KubeCon.
So for those of you who weren't there, basically, the goal of OpenTelemetry's first is stable by default. So we want to make sure that when you engage with OpenTelemetry and download a distribution, the things that you're…
talking to are stable by default, and that you are successful with stable components. If you have to use unstable components to be successful in OpenTelemetry, that's a problem. So we'd like to have some notion of stability. From my perspective, Weaver, we have treated it kind of as a stable thing.
I mean, we've been a little bit loose on a few things, but for the most part, we've been very particular about evolving the community and releasing, to the point where the only thing that would have me nervous about calling a 1.0 at some point would be the fact our crates are unstable. So I would not publish our crates, I would publish our binary, right?
anyway… We want that across all of OTEL, like, where people are taking it… basically.
We're not changing the bar for stability, we're changing the expectation for how long you can be unstable.
I think is what we're doing.
So, if you have been around for 4 years and have not marked it as stable.
sorry, like, that's… that's crazy. Like, either you need to move out of OpenTelemetry, because that component's unhealthy, or you should have been marking it stable earlier, right?
That's kind of the way I read this. The second thing, and this is what affects us a lot, instrumentation, stability, and semantic conventions. So there's this notion…
that we should be federating semantic conventions. So, a semantic conventions evolve slowly and deliberately, because we need to work across a lot of things, and we need to collect expertise, and all this kind of junk.
So, because of that, they want to change,
instrumentation and convention goals. They're trying to decouple full semantic convention stability from instrumentation stability.
We do have this today in the spec, it's just awkward, and people don't necessarily do it. So, one of the… one of the thinkings here that we were talking about is this notion of federation.
Where… we want to actually push on individual schemas with Weaver.
have some sort of inheritance hierarchy model for these things, and kind of deliver more, you know, in the collector, you have component X, it has its own schema, it has its own markdown it's generating, it has its own code it generates. Like, we want to kind of deliver on the Weaver vision here.
So I think this is gonna put increased pressure on Weaver.
Lastly, we want to make sure that iteration is not a blocker for distribution maintainers, meaning I can…
Deliver a stable distribution of my instrumentation.
Without needing semantic inventions to be stable.
And so what this could mean, like, to me, what this means is we don't change the bar for stability, we change how we
Enforce the bar.
Which means weaver everywhere, effectively. But it's like, we want to make sure people are advertising the shape of their telemetry, that they're making sure they're doing diff checks to make sure they don't break things as they evolve, that they're doing major version bumps if they do break, and that they're offering some sort of a, you know…
transition period, that kind of stuff. That's what we're trying to enforce here.
There's a third thing, and I almost forget what the third thing is, because it wasn't memorable in my mind, apologies. Oh, confident and stable releases. This is about doing an OpenTelemetry-wide release. So, you, as a person, can say, I'm on OpenTelemetry Epoch X, is the idea.
And you get all of the OpenTelemetry ecosystem at that epoch, and that is stable for some time.
And then there'll be another drop.
I also think this could help us a lot, too, with the crazy complexity. I don't know if you've tried to…
Use OpenTelemetry across languages, but the hunt and peck for correct versions is always exciting.
And how does this version work with that version of the thing? It… you know, this way, at least we have, like, a standard set of docs that are all released together, standard set of releases that are all released together. Okay.
Coming back to Weaver now.
Nothing in that article has me nervous in terms of where we need to go, but in terms of how fast we want to get there, I'm more nervous now. So, I wanted to have a brief discussion about what we need and how fast we need it to support this as quickly as possible.
so…
I'm gonna open that up for discussion now. Like, what do we think… I have ideas on what we need, and I've been working on a few things, but what do we…
what do we think we need? And let's collect that and prioritize that list.
**Jeremy Blythe** 17:15 I think we need to get V2.
Out of the way.
Like, I was looking at the weekend of picking up some tickets to work on.
And everyone I look at, I'm like, I don't want to do this, because V2… It's gonna change.
So I feel like V2 is blocking.
Moving forwards. Like, some… someone… someone on Slack was like, hey, can we add logs to LiveCheck?
Because I haven't done that yet. I'm like, yeah, I kind of don't want to do that until V2.
**Josh Suereth** 17:44 Okay.
**Laurent Querel** 17:49 For the Federation part? Oh, sorry, go ahead.
**Liudmila Molkova** 17:52 No, no, go ahead.
**Laurent Querel** 17:55 So for the federation part, I think we need,
The existing multi-registry support could be satisfying.
But I guess, if we really want to…
To go in this direction,
More deeply, we need a better support from Meteorology.
So the… right now, we just have, like, a long chain of things. We don't have really,
a tree, of dependencies.
So that's something we need to, to support.
**Liudmila Molkova** 18:38 I'm thinking about the discussions we had on Slack with…
Anton and, I think Java folks, that they're… the…
Federation would mean that collector, and let's say Java instrumentation and other contribib repos will
Start publishing semantic conventions on their own.
And…
They… I think they lack two things. The first one is, how does it work with information about instrumentation? Like, there is metadata YAML. It contains more than semantic conventions. It contains information about the artifact, the stability.
owners, I don't know, links to docs, and whatever.
That's not part of, like, the current schema.
**Josh Suereth** 19:27 And we probably don't need to make it all work together, but…
**Liudmila Molkova** 19:31 We should have an idea on how maybe that
Instrumentation information would reference Beaver YAML?
The other thing is publishing schemas.
Right, so, like… I don't even know how we publish.
schema on Hotel.io for symmetric conventions. It's probably easy to figure out.
But we would need to tell everyone to publish their own schema and attach their schema URL to the telemetry.
And then we need the recipe for this.
**Josh Suereth** 20:08 Yep.
Yeah, actually, if we're gonna talk about recipes we need,
I think we need, CodeGen.
So, we need… Ducten, coaten… release process.
C, I see…
Maybe CICD has coaches, anyway.
What I mean by this is, the way we generate markdown files in semantic conventions is kind of specific to semantic conventions.
we don't necessarily… like, that might not be the right way to piecemeal out things for all these individuals. Not only that, we'd want them to link to semantic conventions when semantic conventions exist. The SEMCOV markdown files won't do that.
So, I think this is where we actually need to create a set of templates, around policies, markdown, all that kind of stuff for…
Oh, shoot, come on. Sorry, Chrome's being weird for me here.
We need to create a set of templates that we can use for this.
For DocGen and CodeGen. Probably policies as well.
So, yeah, I'm getting templates…
I'll just say for DocGen, CodeGen, policies, we need a template for what the release process looks like. You know, how will people actually distribute these things within OpenTelemetry? So where does it go to get to OpenTelemetry I.O?
Right now, for context, the way OpenTelem Trio works is we push it into…
a file in our repo, and OpenTelemetry I.O. just pulls in tags.
And just hosts everything from that tag.
I think we could do better for these. I think it's gonna be awkward if OpenTelemetry I.O. has to actually import every single Git project in all of OpenTelemetry to work, so we need to figure something out there.
And then we need,
we need CICD, like, a way to explain to people how to run Weaver within their CICD.
So, I actually think this makes sense for us to kind of pick one or two SIGs, work with them closely, like we did for when we first pushed Weaver through everything, so we could pick, like, Java and the Collector.
For example.
and start, because I think they're the two most complicated ones. Start with them, get them on board, build out the set of templates and things, and start fleshing out what does our release process look like? What will their CICD work look like?
If we can make a shared set of policies doc and CodeGen. I mean, this is all stuff when we talk about having out-of-the-box docs and CodeGen. This is… my thinking is that the docs and CodeGen we want for this is what would be out-of-the-box.
And general for everybody.
And then if they want to customize, great, but, like, this is what we would help them provide.
Across the board
And this is also where we can make some simplifying assumptions, I think, because we're not building SEMCOM for these folks, we're building, like, they have one instrumentation library with one set of metrics that they're keeping stable.
And they might depend on SEMCOM or reuse SEMCOM, so this is actually going to be, in my opinion, our core use case.
But this, in my mind is, like, you're talking about getting a V2 schema ASAP. I agree, I'd love to get it in ASAP, and I'm still going to be pushing on that hard, which, you notice that's what I've been spending my time on.
but…
This is the thing I'm worried about building and getting out the door. This is a good bit of work, and this is work that we probably need to get people excited about and kind of brought in to do.
So…
**Jeremy Blythe** 24:09 But if we get… sorry, if we get, like…
People… now we're involving other teams, and getting them to do…
work with them to do their doc gen and code gen, and then we're gonna do a rug pull to the V2.
**Josh Suereth** 24:21 Yeah, I know.
**Jeremy Blythe** 24:22 We've done a bunch of work, and then we've got to go… we'll have to go, like.
Don't we want a smoother experience if we're bringing other people in?
**Josh Suereth** 24:32 I don't want V2 to be a rug pull. I think V2 is going to be one of those things where we have V1 and V2 for some time, unless we think we can get V2 out really quickly.
So, yeah.
If you want, we can talk about V2 next,
But let's… let's finish up with just, what are the… what… is there anything here we don't think we need, or directionally, is anyone concerned with this? Like, do we think we should just ask them not to use Weaver for this? I think that answer is probably no. Like, this is exactly what we want Weaver to be.
**Laurent Querel** 25:12 And when you say templates, I guess you are talking about templates for custom registries.
**Josh Suereth** 25:18 Yeah.
**Laurent Querel** 25:19 For doc gen, code gen, and policies.
**Josh Suereth** 25:21 DocGen, co-gen, yeah, so this is, this is the…
**Laurent Querel** 25:24 system, yeah.
**Josh Suereth** 25:25 Yeah, this is… I… I'm…
the things that we have in, like, Weaver examples and the stuff that we're doing there, that's the templates I want. I do feel like there will be a difference between SEMCOM templates.
**Laurent Querel** 25:38 Yeah.
**Josh Suereth** 25:38 surface templates, yeah.
**Laurent Querel** 25:40 And so these are the general purpose ones.
**Jeremy Blythe** 25:42 Where do these templates live? Do they belong to Weaver?
**Josh Suereth** 25:47 Great question. We have to sort that out. Yeah. Right.
I would love if we had a way to have them bundled out of the box, no matter who owns them, but if we can make sure code owners who care about, you know, Java CodeGen or Go CodeGen own them, that'd be better. So we need to figure out how to do both.
**Liudmila Molkova** 26:06 I'm thinking there is a… The life check would…
Play a very important role for stabilization and federation.
Because this is how we scale that instrumentations actually follows something, for real.
And we need a recipe. Maybe it's loose.
Smaller priority, or, I don't know, smaller priority than the…
just the ability to use Weaver to define conventions, but still, it's the next step.
After we need the recipe for the life check.
**Josh Suereth** 26:45 So, we need a way to identify spam in OTLP, then.
Yeah, and we can…
**Liudmila Molkova** 26:52 Either boil the ocean by defining span type, or we can have a… whatever matcher that would customize…
How to find the definition based on the, whatever, attributes in the spend.
**Josh Suereth** 27:07 I'm fine either way, as long as we get there quickly.
**Liudmila Molkova** 27:12 The quickly is probably the latter option, because spend type would take us… A very long time.
**Josh Suereth** 27:22 Not necessarily if we just make it an attribute, that the special… like, a special attribute that we write.
But, fair.
**Liudmila Molkova** 27:31 Yeah, yeah, okay.
**Josh Suereth** 27:36 Cool. We can also do some shenanigans with the name column, and use a pattern matcher on the name, possibly.
Okay, but that's… that's, that's the thing that we need to sort out.
Okay, any, any other thoughts here of things we're missing?
**Jeremy Blythe** 28:01 Good, dude.
Just to get this right in my mind. So the doc gen, the code gen and the policies will be written by, so…
for the Java Collector Project.
They would be written… by the maintenance of the Java collector, with our help, is that what we're suggesting?
**Josh Suereth** 28:19 And so…
**Jeremy Blythe** 28:20 We will then be very specific.
Their doc gen, their code gen, and their policy would be very specific to their project.
**Josh Suereth** 28:28 what I would like to have, and we will have to negotiate how much this would be, what I'd like to have is a set of Java code gen that could work for any Java project, either in the collector… sorry, in the Java instrumentation, or in Java Contrib.
The policies, I think we actually want to define
find a way to share the SEMCOMF policies, or make those be shareable. It's possible those we can share directly from SemConv, it's possible we need to split them apart into general-purpose OTEL policies, and then specific to Semantic Inventions repo policies.
But again, we need to have these things be layered to some extent for policies. So if Java wants to provide their own custom ones for their project, they would define them locally.
but I want to have a shared set of just general purpose
you know, policies, or general purpose code gen for Java. Docgen, I think, should be shared across all OTEL, so there'd be one thing that generates docs that is shared across all of OTEL.
That everyone would use the same template.
**Jeremy Blythe** 29:34 Okay, so docs would be…
Those would be the same standard across everything.
**Liudmila Molkova** 29:42 And probably policies, at least to start with, right? We would provide the shared one, and probably maintainers can customize or change it for themselves, but the baseline should be the same.
**Josh Suereth** 29:56 Oops.
**Jeremy Blythe** 29:57 For CodeGen, what we're saying is we're not making a language CodeGen.
**Josh Suereth** 30:00 We're making…
**Jeremy Blythe** 30:02 We're making project-specific coaches.
**Laurent Querel** 30:05 Mmm… I don't see so.
**Jeremy Blythe** 30:07 No?
**Laurent Querel** 30:08 No, I think the… so in terms of complexities, policies is most likely something easy to achieve, because we already have a lot, we have to do some…
Featuring and sorting, and then we get, in my opinion, the…
the policies for custom registries. For Douggen, it's a little bit harder, because we need to create,
a generic documentation, but that will be independent of any project or any language. The one that is complicated is CodeGen, in my opinion, because we have many languages to support.
But that will not be specific to a project, that will be specific to a language.
At least that's my understanding.
**Josh Suereth** 30:49 Yeah, the only caveat I'll throw is, we have to treat the collector and all other Go as separate languages.
**Laurent Querel** 30:57 Yeah, Matt, do you agree that if we provide, let's say, a standard code gen for Go.
people can derive this one and create their extension of it, or their variation, and that's up to them. At least we have one that is generic for Go in general, and then they can create their specific collector one, if they want.
**Jeremy Blythe** 31:21 Okay.
So… if we're making a code gen for Go.
Makes sense to me that that belongs to Weaver.
Yeah.
Anyone in the world, regardless of whether they're open telemetry, or CNCF people or not.
can use that, and that's what, like, I think…
The question… people just want it to work.
So…
**Josh Suereth** 31:46 Yeah, so that would be our out-of-the-box codeGen, yeah.
**Laurent Querel** 31:50 Yeah, like Protocy, when you use Protocy, you can generate, code.
In XYZ language that are supported.
**Jeremy Blythe** 31:58 Yeah, we shouldn't reach.
**Laurent Querel** 31:59 Yes, exactly. We should reach a point similar to this one.
**Josh Suereth** 32:05 Yeah, now we do have to figure out, like, the thing I'm worried about with this is less so…
The… the shape of it, but more so the governance of it.
So, where does it live?
Who are the code owners? How do we get those code owners built up? How do we make sure they're successful? If they require a review from us.
every time they merge, that's… I think that's gonna be problematic. So, like, how do we…
**Laurent Querel** 32:31 Do they agree, yeah.
**Josh Suereth** 32:33 Yeah. So, that's my main concern there. Go ahead.
**Liudmila Molkova** 32:37 Also, it's probably not our top priority, but, if we provide code gen… like, Primedia's folks are interested in using Weaver. If we provide
OTEL quad genre should be explicit, it's not just for the go, it's for hotel.
API.
**Josh Suereth** 32:53 Yes, it's for OTEL, it's for Go, yeah, and I do think if Prometheus wants to provide
Go CodeGen in Weaver as an out-of-the-box default that you can use, great! Like, let's give them a place to put that in. You know what I mean? That's where the governance comes in. That's why I'm worried about where does that live, what repo is it in.
That sort of thing. We can…
My thinking is, and I'm gonna go solution-y, by the way, but my thinking is, when we make a distribution of Weaver, there's a config file that basically says, here are the out-of-the-box
places that you get CodeGen templates from, and we bundle them into our distribution in some way.
That we can leverage. So you get, like, a local copy of them.
I don't know if we pull them into the binary, the way we do with our include defaults now, if we find another way to include them, but, like, effectively, I'm thinking that code gen and stuff that we want to include out of the box, we have some way to take it from any Git repo, and at build time, we ingest it in some fashion, right?
So there's a… there's actually going to be a distribution phase for Weaver, where we put all this stuff together.
**Laurent Querel** 34:05 Yes.
**Jeremy Blythe** 34:07 Because, like, right now, each…
each OTEL SDK for each language, they already have, like, some code gen templates that are creating the semantic convention library, so they already have templates
in external projects.
**Josh Suereth** 34:22 We do, but they're, they might need more.
**Jeremy Blythe** 34:28 They're an attribute constant.
**Josh Suereth** 34:30 They're attribute constants, and… I think we had to contribute half of them.
**Jeremy Blythe** 34:36 Right.
Is this the… is this the same sort of story, though?
**Josh Suereth** 34:41 They could be the same sort of story, yeah.
the thing is, so, like, I'm thinking about from a… I also want to worry about security of the build.
Because I don't think Weaver actually validates, that… I don't know if there's template injection that you can get when we generate code, but that's a thing that I'm a little bit nervous about. So, like, we want to make sure that we have a secure build when we generate code and all that kind of stuff. So if you're downloading from some random Git repo every time.
you can't guarantee that it's the same every time. We don't, like, limit to hash, all that kind of crap. We actually probably need those… that set of features in eventually.
in Weaver.
because initially my thought was we would just have a list of, you know, here's the Java CodeGen template directory, and so it'd be like a Git reference. And Weaver would just know about those, and so if you say Java, we could just replace it with downloading this Git repo.
But we need to get to a point where we have some kind of security around that as well.
that… that can be an extension feature.
But… yeah. Anyway, you see the magnitude of what we're talking about here as we push on this. So, this is why I wanted to get sorted on what our vision is, and then get sorted on what are the next steps to make this successful.
Okay, moving on, because we only have 15 minutes left, there's two discussions I wanted to have. I actually opened a PR on custom policies that we'll talk about in a bit. Let's start with V2 schema.
There's two things here. One is the current PR, and then next steps. Current PR, I feel like most people had a chance to review it now, so I'm gonna…
it stops at a particular point, and that's what we're gonna talk about here. I'm gonna go through next steps.
Current PR basically fixes V2 schema for Resolve?
and can fire them at Jinja templates.
So, right now, the whole each and everything work just fine. You're using JQ. If the JQ actually gets the whole, the whole enchilada.
And so if I want to send metrics, like, and have something generate per metric, I fire it that way. What I'm struggling with a little bit with templates in V2 schema is if I need to send additional context. Like, let's say I want to make,
one file per metric, but I want to send the entire schema in, And have one per metric?
I actually don't have access to the entire schema if I filter down to just metrics simply.
Right? I have to do complicated JQ expressions to, like, grab context and shove it into every single object in the array.
So that it shows up in the template.
**Liudmila Molkova** 37:32 You mean each versus, all modes?
**Josh Suereth** 37:36 Yeah, each versus all. So in all, you can just throw in an object, you get everything. With each, you send an array, and you get every element of that array.
But what if I want the elements of the array, and I want some other thing as, like, static context?
**Liudmila Molkova** 37:50 Hmm.
**Josh Suereth** 37:51 That was what I was running into with V2 schema, because that was more… like, if I wanted to go look up entities at the same time I'm writing metrics.
**Liudmila Molkova** 38:01 This is what we do with the grouped…
**Josh Suereth** 38:04 Group by root namespace was the helpers today.
Yep.
You don't need those helpers anymore in V2, but you kind of want them, yeah.
**Liudmila Molkova** 38:14 you want them, right? You want to get all the entities in that namespace.
**Josh Suereth** 38:22 Yeah… I'll have to… I'll have to show you what it looks like, but it… like, if you haven't yet, go toy around with V2 with templates, with this… with this PR.
Because I think we need to figure out what those template functions look like.
And it's gonna be a little exciting.
**Laurent Querel** 38:43 So just, so getting the, the context for the, for the 4H, mud.
**Josh Suereth** 38:48 Yeah.
**Laurent Querel** 38:49 We could, sub that outside of GQ, we could, basically, build ourselves
what we provide to the template could be generated by the ROSE code.
We take the answer of the GQ expression, and we create the con… and we add the context externally.
**Josh Suereth** 39:08 That's what I was thinking about, yeah. So you always get the entire repo in JQ.
**Laurent Querel** 39:13 Sorry, in Ginja.
**Josh Suereth** 39:14 You always get it in the same spot, and then you get the filter as a separate thing.
**Laurent Querel** 39:18 Yes.
**Josh Suereth** 39:19 Yeah.
**Laurent Querel** 39:20 That could be an option.
**Liudmila Molkova** 39:22 It's actually not a bad idea to, even if we build helpers, to always provide the whole context in JQ as well.
**Josh Suereth** 39:31 Yep.
**Liudmila Molkova** 39:32 then somebody can pass it over to Ginger.
**Josh Suereth** 39:38 to Ginger, and thank you.
Be on top of this.
Okay, I wrote that down. Alright, so the next thing is, so this, this basically does Resolve and Ginger templates. It does not do Rigo policies. This was the next thing I was looking at, was how, how to fire the new schema at Rego policies.
I also need to do, stats, which I think… where did I have that?
Don't we have a stats one, too?
Nevermind. I know I need to do stats, it's on my internal checkbox, but, I need to do stats to make sure that all the stats line up, that we're not losing groups and things.
There was some, logic errors that will print logic error if it gets to them.
like, on the command line when you do a resolve, I have not seen any of them when I've been resolving SemConv, but that doesn't mean that I don't have them. It just means that SemConv doesn't execute them.
Because of how we structured subconv, right? So I have those in there, and it says, like, report this now. But yeah, Regal Policies is next. Then,
check is basically, when we add Rigo policy checking, I think that would basically be V2 schema for the check command. Update markdown will also be interesting, because right now, the way Update Markdown works is you put one single group ID with a Semcov prefix.
This is where, for V2, I might… I might make a new… so, basically, have… have that still work against the V1 repo, and then make a new syntax that you use to reference things in V2.
Because we want to reference a metric, we want to reference a…
event, an entity, that sort of thing. So I might actually change…
the update markdown stuff for V2, not sure. That's a to-do. Live check, this is one, Jeremy, I was hoping you could help me with this, of figure out how to enforce with the V2 schema.
Yep.
It might be a new code path, where you have CodePath 1 for V1 and CodePath2 for V2. We'll have to figure that out.
**Jeremy Blythe** 41:53 Yep.
**Josh Suereth** 41:55 JSON schema for emitting the JSON schema, I think that's actually relatively easy to do, just need the V2. For emit, this is just updating the emit code to use the V2 schema.
**Jeremy Blythe** 42:07 That should be pretty good.
**Josh Suereth** 42:09 Yeah, I don't think that one's gonna be hard.
**Laurent Querel** 42:11 Gism schema, sorry, Josh,
Did you already try to use the JVN schema macros that we are already using? And the question is.
Did you observe a,
higher quality with the output with this V2 schema. That should be the case, but I just want to make sure that… okay.
**Josh Suereth** 42:35 Yeah, yeah. The only problem we have right now is most of my observations done where the version 2 is in the middle.
So, so, you know how we have, like, the version field? So, all your output says, hey.
here's your error message if you're on version 1, and here's your error message if you're on version 2. And the version 2 ones are pretty concise and obvious, and the version 1 ones are kind of…
More awkward, so you can literally see them beside each other, but the overall error message quality is not that great, because it always tells you about both.
**Laurent Querel** 43:08 Mmm, okay.
**Josh Suereth** 43:10 So… and I don't know how to kill that, necessarily, with the way that we have things set up.
Admit, we just talked about search. This one, this one I can take. We might just… maybe we just kill search. I don't know if people are gonna be building search. This is where… we had some discussions about turning search into, like, an MCP server.
I think that would actually make more sense going forward, or like, you know, Lauren, you had a very robust search implementation in the past. I tried to do just enough, people would be excited to work on it, and no one has touched it. I don't know if we don't have a good enough demo, or what we need to do there, but maybe we just kill it.
For now. And then add it back in. Yeah.
**Liudmila Molkova** 43:54 If people do MCP server, it would rupt something.
It could be, just a wraparound resolve.
**Laurent Querel** 44:03 Thank you.
**Liudmila Molkova** 44:04 It would need to resolve registry all the time.
So, like, I'd rather us to focus on the underlying tools, and if somebody wants to create MCP server around it, that's fine, but we should have the core part.
**Josh Suereth** 44:17 So maybe, maybe what we can do is just deprecate search.
Does that sound reasonable to everybody?
**Jeremy Blythe** 44:25 Yeah, I think so. We also… there was… it… I don't know.
The interest dropped away, but there were…
There was, people looking at doing… like, web GUIs.
**Josh Suereth** 44:39 Yep.
**Jeremy Blythe** 44:39 Yeah. Which one may be… is maybe more appropriate for search.
**Josh Suereth** 44:44 Yeah, that actually might be easier to implement in general, too, than trying to do everything through,
what is it? Ratatouille? Although I like Ratatouille, it's funny.
**Jeremy Blythe** 44:54 It's fun, but… Yeah.
**Laurent Querel** 44:55 Send you.
**Josh Suereth** 44:58 Okay, and then V2 schema for diff. This one, I might need some help with here, Lauren. Like, I think overall diff might actually be easier in the new schema.
**Laurent Querel** 45:09 Yeah.
**Josh Suereth** 45:14 So we'll have to… we'll have to do that. And then stats is the other thing. Lastly, we need a ton of documentation. So if we're gonna fragment this out, I can work on raw Rigo policies, which was my next thing.
Lauren, if you can help with, Emit and Live Check… not Lauren, Jeremy, if you can help with Emit and LiveCheck, that'd be ideal.
**Jeremy Blythe** 45:34 Yeah.
**Josh Suereth** 45:35 And then, Laurent, if you have a chance to do anything else on this, let us know. Like, diff, possibly, I think was the one I was thinking about.
**Laurent Querel** 45:44 Yeah.
**Josh Suereth** 45:46 Okay.
**Liudmila Molkova** 45:47 I can take a look at the templates, the namespace templates.
**Josh Suereth** 45:54 Nice. That would be awesome, because I think…
This is only the work for V2 schema to land, and so there's, like, all of the rest of the work to land the Federation stuff, Ludmilla.
So if you can make progress on that while we land, you too.
**Liudmila Molkova** 46:12 Yep, deal.
Yeah.
**Jeremy Blythe** 46:16 Just sort of.
**Josh Suereth** 46:17 How are we organize and contributing?
I wanted to use this, so actually we can just put our names behind things. So, let's see, schema for generate, we'll say…
Juicarette. I also need to… this one, Lumila, I might bug you about, because maybe you can help me out with some of these, because I didn't add this yet, but let's say…
V2 Helpard.
Options for JQ.
Okay.
**Jeremy Blythe** 46:51 Yeah, I kinda meant, like, are you… are we gonna get…
**Josh Suereth** 46:56 We…
**Jeremy Blythe** 46:56 working on Trunk for this?
Like, are you gonna get resolve?
Does LiveChair commit lots of the other things rely on having them resolved?
schema.
**Josh Suereth** 47:07 Yeah, yeah, I have my PR right now, I'd like to merge it.
**Jeremy Blythe** 47:12 Okay. Which, which gives V2 resolve.
**Josh Suereth** 47:15 capabilities, and then we can all branch off of that and work life. That's why, like, the whole point of this was, I think, with this commit, we're at the point we can start fragmenting out work.
And we can start hammering on it and really making sure that it's robust, what we've done. We're also deprecating parts of V1 model implicitly with V2, so, like, scopes disappear.
Right? There's, like, a few things that are… kind of…
being undone, that we'll have to see if we need to add them back in. But, yeah, this is just our… an ability for us to kind of split things apart. Lauren, I'm gonna put you here.
And, Lyudmila, you're on everything… That is not listed in here.
**Liudmila Molkova** 47:58 I think the helper functions? Yeah.
**Josh Suereth** 48:03 I do it, yeah.
Okay.
If you want to toy around with those and see what those look like, you can try the branch as is. Alright, I'm gonna say… that's one for each of us.
Cool.
**Jeremy Blythe** 48:20 Just, sorry, just to…
**Josh Suereth** 48:22 Yeah. Confirm then.
**Jeremy Blythe** 48:24 if you… And I'll look at… I'll look at it again, but we're saying that live check…
needs to work with both V1 and V2.
**Josh Suereth** 48:34 For now, yeah. We're gonna go through a transition period between the two, yeah.
**Jeremy Blythe** 48:40 So, if you've got a V1 model.
it's gonna resolve to a V1.
model… Internally, and so that will work as it does today.
**Josh Suereth** 48:51 Yeah.
**Jeremy Blythe** 48:52 So that means we need V1 and V2, like.
Policies, which we've always had here, but live check policies, too.
**Josh Suereth** 48:59 Yeah, that's… that's actually… so actually what the work is for LiveCheck is you need your policies to be against V2 in addition to V1. So if someone passes the V2 argument in.
we can, like, the theory is we assume their policies are against the V2 model.
**Jeremy Blythe** 49:15 Or, yeah.
**Josh Suereth** 49:16 That's what I'm working on with the policy-based stuff now, is making sure that the policies are on the V2 model.
The other thing is, you can pass in a V1 input and turn it into V2.
and then feed that through the V2 model. So, like, everything is divorced at the resolute. So, the resolve stage is all on V1.
100%. So if you pass in V2, it turns back into V1, goes through Resolve.
And you get back a V2 schema. You can turn… or V1 schema. You can turn the V1 schema into V2 before you pass it through live check, before you pass it to Forge, before you pass it to policies.
That's the idea there.
**Liudmila Molkova** 50:02 So you would pass V2 flag, and then your policies should be V2.
**Josh Suereth** 50:10 Step…
**Liudmila Molkova** 50:11 Qualice…
**Josh Suereth** 50:11 Theory, yes.
**Liudmila Molkova** 50:13 Yes.
**Josh Suereth** 50:13 When we go implement this, if that turns out to be awkward or really hard, where we might want to, like, specify a policy as a V1 policy or V2, we can figure that out. Like, I'm not saying you have to do it that way, that's just how I'm starting, and then trying it out and seeing, like, how that works.
**Liudmila Molkova** 50:36 Okay.
**Josh Suereth** 50:36 Right? Like, we need to give people a transition period, is the gist of this.
**Liudmila Molkova** 50:42 I mean, who uses policies? It's mostly SamConf.
**Josh Suereth** 50:48 Mostly SEMCOM, so I'm giving SEMCOM a transition period, yeah.
**Liudmila Molkova** 50:51 R-right.
Okay.
**Josh Suereth** 50:56 Alright, so I want to do a quick.
**Laurent Querel** 50:59 Can you go back just on the previous… I'd just like to discuss the relationship between what you just mentioned, the V2 schema work.
and the recipes that we discussed before, because I think there are some elements in this list that are super important to achieve.
For the recipes, and some of them that are probably, like, optional.
to implement the recipes. So the generate, the check, the life check?
are probably the top 3 things that we need to achieve for the recipient.
Everything else, looks like Segumdory, in my opinion.
Do you agree with that?
**Josh Suereth** 51:46 Diff, diff as well, because that's how we're gonna generate the, schema, schema URL crap that we have to…
**Laurent Querel** 51:52 Yes, yes, yeah, I agree.
**Josh Suereth** 51:53 But yeah, no, I'd absolutely, like… and if you look at where our names are, I think they're on the important things, and the rest we might be able to…
You know.
Deal with overtime.
**Laurent Querel** 52:03 Dude.
**Liudmila Molkova** 52:04 Yeah, the update markdown is also important, but I would assume it's a minor compared to the generate itself.
**Josh Suereth** 52:10 I'm hoping that this is only necessary for SemConv.
And so that's why I actually think that the other ones are higher priority than that. I would put that below, because if we think about, like, Java adopting or Collector adopting, and we say, cool, you guys use just generate, just Resolve, just Live Check, and just Diff, I think we're in good shape.
**Liudmila Molkova** 52:33 Okay, so we will make generate work for the dog generation.
**Josh Suereth** 52:37 Yes.
**Laurent Querel** 52:40 Custom registries.
Oh, for, for languages, yes.
**Josh Suereth** 52:43 For all the, like, yeah. So, and we wanna, we wanna avoid the update markdown craziness if we can.
You know, I think our goal for SEMCOV was to eventually get everything to update mark… away from Update Markdown, so…
That's in line with that.
Alright, real quick then, we have 5 minutes. Custom policies and violations. So, this is just… I was looking… I was looking at violations and looking at things, and this is just a small…
thing I made where, if you look at some of the policies we write today, everything is an attribute registry violation, and the way that works is there is a, like, an ID,
a type that gets used. I created a new custom type where the idea is, actually, I could just show you the conversation.
This idea is, we wanna… we wanna have violations for custom violations that people put in Rego, have the minimum set of things you need to filter.
and display.
So just enough to present results. It should always have a raw string we can render, a message, right? That we're doing this Sprint F thing at Rego, and that's been working out really well. And then we can allow super custom rendering via JSON object.
So, what I'm proposing here is, and I haven't done the full work, but I want to deprecate,
In violation, we have some kind of attribute, advice and custom.
I want to deprecate some comp attribute going forward, so it doesn't exist anymore. So we just have advice and custom, and custom is, today, an ID, a message, and then just raw JSON you throw at it.
it might need more. So that's what this proposal is. However.
The thing to discuss as I'm looking at this, and this is for Jeremy, is basically,
Advice looks pretty darn good.
Advice has all the flexibility in it, as well.
Should we just move to advice?
Or do we need, like, pure custom ed advice?
**Jeremy Blythe** 54:54 I don't see why…
**Josh Suereth** 54:56 Move.
**Jeremy Blythe** 54:57 Really? I think I made advice because the thing that was there wasn't… wouldn't fit.
**Josh Suereth** 55:04 Yeah.
The only complaint I have with advice a little bit right now for policies
is actually just nomenclature. So,
If we look at advice, you are here, I think?
It has a type, message, level, signal type, and signal name, right?
This might not… like, you might not have these in policy violations.
So…
**Liudmila Molkova** 55:33 When it's an attribute?
**Josh Suereth** 55:35 Those are attributes of advice you have to provide, yeah.
So that, like, custom kind of gets rid of that, so where's… oh, it's down further, sorry.
You'd think I would remember this file, I was just in it. Here it is. Yeah, so there's a signal type… oh, they are optional, though.
So you don't need them.
And advice level makes a lot of sense. Advice level is like, you know, information improvement violation. I like that.
Message, absolutely fine. You have a context, which is a value, and you have a type, which is a string.
which is kind of like the name of the policy. The only thing that I would change from advice is instead of saying advice, I would call it, like, policy.
Right? For custom. Like, they look almost exactly one-to-one what I want. This is the set of stuff I need.
for Policy Engine.
**Laurent Querel** 56:33 Yeah, should we merge, just these two,
If we think that advice is the right way to represent those, durations… Maybe, can just,
Rename the, the, the advice, field, and, and we are, and we are good.
**Josh Suereth** 56:52 That's kind of what I'd like to get to, yeah. So,
Yeah, basically, we resolve around violation, where this would just be a type string, and it would be informational improvement… sorry. This would be a type string, which is… or an ID string, which is just, you know, the user gives an identity to the violation or advice that's being generated.
This would become just context. What?
**Laurent Querel** 57:19 Yeah, context, so…
**Josh Suereth** 57:22 And then, this would just be level.
And level would be information improvement violation.
So actually, the only thing I would do is remove advice from the prefix of all these things.
So…
If we're comfortable, we leave advice, we can mark it deprecated, we can remove advice from the prefix of everything.
And then have a transition period where we warn people, hey, you're using advice, move to the generic policy error thing, whatever you want to call it.
Does that sound reasonable?
**Liudmila Molkova** 57:54 Yeah, it sounds great, and custom would not be great, because we would use custom advice everywhere, essentially, in semantic conventions policies.
**Josh Suereth** 58:04 Yeah, yeah, yeah.
But yeah, I think… so… really quick…
Jeremy, I think you nailed it here. This is what we wanted all along. We just didn't know we wanted it until now, so…
Awesome.
Alright, I will update my PR to kind of go that direction, then. I'll get rid of custom.
And… I'm… I'll do some shenanigans with CERD, because I think I want to change violation.
To, to basically support advice as it exists today, possibly with rename rules.
And then, have it… Basically, only, like, every violation just has the structure that advice has.
Does that sound reasonable?
**Laurent Querel** 58:53 Yes.
**Josh Suereth** 58:53 Cool. That will be some real fun Rust code to write, or see if,
Maybe Gemini can write it for me, who knows?
Alright, thanks everybody.
**Laurent Querel** 59:05 Exactly. Yeah, thank you.
**Josh Suereth** 59:06 I'm listening.
**Liudmila Molkova** 59:07 Add to Gravity.
**Josh Suereth** 59:09 Yep.
Good.
**Jeremy Blythe** 59:11 Right.
