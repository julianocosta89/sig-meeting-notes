SIG: Semantic Convention Tooling
Date: 2026-01-28
Duration: 59 minutes
============================================================

## Zoom Recording Transcript

**Nicolas Takashi** 01:59 Hello!
**ariannavespri** 02:03 Hi!
**Josh Suereth** 02:22 Morning, everybody, or afternoon.
**ariannavespri** 02:25 Hello!
**Liudmila Molkova** 02:42 Hey, everyone.
**Josh Suereth** 02:55 Alright, sorry I'm a little late, just getting caught up. I was trying to get some demos, but I'm not ready for that, so… I added a bunch of stuff to the agenda, feel free to add your topics.
And apologies, okay.
And Ariana, I think we need to… I wanna, I wanna talk about a few things. Let me… Also add the, so let me see hack into this repository.
Okay, I'm gonna add that there. Alright, let's get started. First, I want to talk a little bit about build issues.
With Weaver.
Oh, I'm not sharing, sorry.
So basically, the TLDR is a few of our image bumps, or version bumps, are starting to run into an issue with symbol not found.
And that issue is actually because we are building Weaver in Debian.
And then, in Docker, at least, we are running it inside of Alpine.
There was a major bump of the CLIB, And the version that we build with in Debian and the version in Alpine are now different. And we haven't actually had a problem yet, because generally CLIB is relatively stable until it isn't, and then all hell breaks loose.
So… we had tried at one point to always build in Alpine, for Docker, but the problem is the build goes from being, like, 30 minutes to being about, 4 hours, because if you… do Docker multi-architecture builds, it just really sucks, so what we do is we build once.
in Debian for multiple architectures, and then reuse the binary.
Yeah, there's a whole bunch of caveats here.
That's… that's part one, is basically CLIB is changing, and I think we're gonna have trouble updating some of our dependencies. Our ability to read GET repos is one of the most problematic ones, in my mind. We can't upgrade that dependency right now.
The second issue is with Node.js, and I think we need Jeremy to talk through this more, but basically, with the Shaihalud, virus in Node.js.
Work has locked down Node.js for me. Oh, Jeremy's here, good. I… I am not supposed to change my Node.js version willy-nilly, everything has to go through a proxy, all kinds of fun.
right now, because we don't lock down what version of Node.js we're using, and because we have different versions between people, package. PackageLock.json keeps churning, and anytime we check out, like, we can't build the Rust code because the UI code's broken, for example.
I think maybe we should find… like, I really do want to just escalate, we need to find a solution to this.
Yeah. Anyway, for context, let's see.
NPM V10 versus V11. I did some research, change how… Optional packages are reported in PackageLock.json.
Npmci.
It's supposed… Fix the problem.
But can't across major versions of NPM.
So basically, we have to pick a version of NPM I… I am on Debian, and I'm locked to version… is it… I think I mean 9 versus 10, let me check.
**Jeremy Blythe** 06:44 You're on 10, and I'm trying to use 11.
**Josh Suereth** 06:47 What?
**Jeremy Blythe** 06:48 You're on 10.
I'm on an island.
**Josh Suereth** 06:51 I'm on node… I'm on node 10 and NPM 9.
And it was no… and, like, what NPM version are you using? It's… NPM is the issue, that's what I discovered.
Like, the Node version is actually not as problematic as NPM. NPM is the thing that's churning package lock and causing issues.
**Liudmila Molkova** 07:19 We use… sorry, stupid question, we use Node for the new serve functionality, right?
**Josh Suereth** 07:25 Yep. And Rust cargo tries to build it, and you're unable to build or work in Rust if it fails.
**Jeremy Blythe** 07:34 We could take it out of the Rust build and do it.
do the builds of the UI independently?
So then, if you're making UI change, you're building UI.
That would stop the churn.
**Josh Suereth** 07:51 it could stop the churn, but it doesn't necessarily… like, I still think we need to figure out this problem, because, I can tell you what I think success is. Success is… we know what versions of dependencies we're using when we build a release of Weaver.
That's… that… that's frankly what we need. What I don't want to do is shenanigans with switching, like, how we download stuff, just because, like, again, this should scare us a little bit, in terms of, like, safety of using Node. Like, we need to be careful about what package we pull in.
how we pull them in, and, like, that whole ecosystem. So, I just want to make sure that we're not, being a little too… free with what's included in Weaver. I don't want the ability for the Weaver release To get, you know, infected.
Because we're not being careful.
In any case.
**Jeremy Blythe** 08:53 we could have two projects, we could have Weaver, and then we could have Weaver UI, so a completely separate thing.
**Josh Suereth** 09:00 and Weaver UI dumps a… dumps a distribution of itself. Yeah, I don't know, like, that seems so high friction, Jeremy. I don't want to do.
**Jeremy Blythe** 09:07 Oh, it is.
**Josh Suereth** 09:07 yet.
**Jeremy Blythe** 09:10 You could force NPM9 as the version that we use.
**Josh Suereth** 09:15 What I… I was trying to look into this, of seeing if we could actually force NPM9 packaging.
And then you can use MPM11 successfully, but the resolution algorithm is NPM9. I don't… I couldn't figure out how to do that.
**Nathan Smith @ Elastic Observability** 09:30 You, you can, you can declare in the, in the package JSON, do you have engines? You can declare the required NPM and node version.
Yeah. In the engines. I don't really know how that's enforced or anything, though, especially if you don't have NPM, or NVM.
**Josh Suereth** 09:50 I did a prototype where I added that, and basically, if we do that, it forces everyone to the least supported version of any developer, which would probably be me at this point, and I'd feel bad forcing Jeremy to downgrade everything.
To what Deviant has.
But yeah, like, that's an option as well.
**Nathan Smith @ Elastic Observability** 10:10 And can you… is it possible, like, there's the official Node Docker images that have different pinned versions, are you restricted from… Using those?
**Josh Suereth** 10:23 We… so, in our build for Docker, I'm actually not restricted from using those Docker images, so I actually could hide things in there, but it's still the same issue where I… I need to make sure that those things go through some proxy before I download any node artifact, to make sure that that node artifact is not, infected.
And to do that, I have to have, like, my own personal note config that does junk. So, there's a bit of this from… that's a me problem.
Using locks. I think… I think, let's… let's move this… JSON on node, and then PM version.
let's actually lock the version in Node and NPM, and then I can figure out my… we can lock to the latest LTS version, and I'll figure out what to do on my system, and then make a proposal from there. But I think at a minimum, we should actually… prevent the churn by forcing aversion. Does that sound reasonable?
**Jeremy Blythe** 11:28 Yeah, makes sense to me.
**Josh Suereth** 11:30 Yeah, this does mean, once that PR goes through, I might not be able to make contributions to Weaver until I fix this, which is what, when I first tried, it literally, I just broke me contributing to Weaver.
Because I couldn't get the version of Node that's required.
but, we can get that sorted out later.
**Jeremy Blythe** 11:49 But if you know you haven't changed anything in the UI, you don't have to include package log in your commit.
**Josh Suereth** 11:58 Yes, but if you add the lock on packageJSON, basically what I have to do is change package JSON to remove that, run npm install, and then, like, not commit that repeatedly.
It's fine.
We'll, we'll figure it out from there.
**Jeremy Blythe** 12:13 I guess I'm saying, yeah, that's awkward, but you can carry on writing Rust.
**Josh Suereth** 12:19 Fair. I mean, that's… literally, I'm doing that now. If I were to show you any of my branches, all of them have a change to package lock.
For annoying reasons.
Yeah. Anyway, okay, cool. So let's, let's do this.
We'll make progress that way.
**Nathan Smith @ Elastic Observability** 12:39 And I'm not advocating it, and I don't have a preference, but is the… Would… using yarn… be any different than using MPM?
**Josh Suereth** 12:52 Yarn… yarn is also not recommended right now, yeah.
**Nathan Smith @ Elastic Observability** 12:57 Okay.
**Josh Suereth** 12:59 I, thank you.
**Nathan Smith @ Elastic Observability** 12:59 There's JavaScript.
**Josh Suereth** 13:00 And there's… there's my… like, personal computer, where it's fine, but then in my company computer, I have… there's, like, a whole bunch of things I have to abide by.
Okay.
This thing, though, this is actually still an issue.
I'm guessing nobody really has time to dive into, dealing with Rust builds and Docker images at this point, is that fair?
Okay I… I think I'm gonna… Yeah.
I'll come up with some proposals for this, because this is… this is going to become super problematic. We might need to actually change completely how we build our Docker image.
at a minimum, just have to do some more research about the Alpine… the CLIB used in Alpine, and the CLIB used in Debian, and see if there's a workaround.
Maybe we can, like, force update the syllab on our Docker image build.
for Rust, and then when we build Rust, the AlpineClib will be compatible. But just for context, If you get a bunch of broken, renovate things, that's why.
Go ahead, Arthur.
**Arthur Silva Sens** 14:24 Completely… shooting in the dark, couldn't we reach out to the JavaScript SDK as sick?
like, this is… like, packaging and writing SDKs, totally different things, but maybe they have a lot of expertise in packaging as well.
**Josh Suereth** 14:42 Oh, that's a good question, yeah.
Drought 2.
JavaScript.
Let's see for help here. Yeah, actually, let's, I'll do that after the meeting.
Cool. That's a good idea, ping them on chat.
Talk about the issues, see what they recommend.
Yep.
**Jeremy Blythe** 14:59 Is the… is the C lib thing the dependency on the C library, like, if we just live, like, if we built a… So, like, if we did a muscle build instead, would that get around it?
**Josh Suereth** 15:12 That's worse.
Muscle is a version of Lipsy, yeah.
Right?
So, it, it, it's… I think it's actually the issue is… is with muscle versus Libsy.
hold on, let me try to remember. We moved away from muscle.
And back to libc, because muscle's really inefficient.
So we're using an Alpine that has a version of libc, but if we used a muscle, it's more of a problem, because we would need to build completely differently on Debian. And it might be that some of our dependencies, like the get one, doesn't work at all.
Cause that would have to be muscle compatible.
I think GIX is actually somewhat native, that's part of the problem.
Anyway, if you'd like to try that… Before I just nix it.
Look into moving that to muscle.
for, doctor.
**Jeremy Blythe** 16:13 Yeah, we just did a PR to add muscle builds for Weaver, right? That just went in.
**Josh Suereth** 16:20 That's… I think Docker had always been using Muscle prior to that.
like, we were building muscle for Docker, but we weren't building it for, Any, like, for just independent download?
**Jeremy Blythe** 16:37 Okay, got it.
**Josh Suereth** 16:39 Yeah.
For context.
when we build our Docker image, we're not reusing the tar files we build as part of our release system. What we're doing is we're rebuilding Rust inside of Docker.
So there's also… I'll add this as another possibility.
Okay.
Cool.
I took more time on that than… than… I really wanted to, just… I wanted to escalate this so folks are aware. This is gonna bite the crap out of us if we don't… makes slow, steady progress. So, we'll reach out to the JavaScript SIG. I think let's pull the trigger on the package lock, and then let's continue to push on the Node.js thing, because I'm… I'm witnessing a lot of churn on it already, and a lot of questions about it, so… Cool.
Alright, template repo.
So… This is related to, Ariana's here.
If you're not familiar, we… we merged the proposal to have a… complete repository to include out-of-the-box defaults for Weaver and templates. So, what I'm doing right now is I'm going to pull up the docs so you can see that, that specification.
where we want default templates to live. So here is the… spec file.
where we want to move default templates into their own repository. The idea would be, if you say, like, Weaver registry check.
you can point at something that looks like it's baked in, but it actually lives in a different location than the Weaver repository itself, and it doesn't have to be baked into the binary, it might be.
the initial thing would be we have a Weaver Templates repository.
and every directory has a theme inside of this repository, so we'd have, like, templates slash docs. Arianne, I think your proposal here that you're proposing into Weaver would actually belong in this repository as, like, a documentation template. I think it's fine to add where it is now, because actually.
we'll get into the discussion, but I think it's gonna, the things you're using, we'd move over to be able to be usable in this place, so we could just merge it when we grade this. Anyway, so that's context.
Things that I'm thinking about. We want to be able to have a template repo to… to… Reach out to people to get folks to write out-of-the-box templates.
My goal is to have one package that does markdown generation. I think using Ariana's contribution makes a hell of a lot of sense there. I want to have one package that does policies. I was going to actually add stability policies. So, you know, you can't mark a signal as stable unless all the attributes are stable, and then actually backwards compatibility policies.
I want to have tests in this repository, so when you build a package, you can test to make sure it works in some fashion.
So that you can actually cut releases and make sure it's stable, and make sure new versions of Weaver don't break it. I want to use the Weaver GitHub action in this repository, so that, you know, we're using a version of Weaver that's launched, and we're using the GitHub infrastructure we have, kind of testing our own dog food. I'd like to have Renovate bump versions.
Et cetera, et cetera. And then finally, I want to document That describes how to add and test new packages, so as we reach out to folks.
to add and contribute packages, they have a clear onboarding guide for what they're gonna build. That's my goal.
Few decisions that we need to make.
How do we want to test?
For example, for policies, what I'm thinking is we have an example repository that you define locally.
You have a JSON document that's the output of all the findings.
From Weaver Check.
And we just kind of run that and do a diff, and fail if there's any changes, and report the diff.
Yeah. The second test… Yeah, go ahead.
**Liudmila Molkova** 21:02 Yeah, I… the biggest pain is to define test cases today in SemConf, and if we have them in YAML instead of in Regal, it would be much better.
**Josh Suereth** 21:13 Yeah.
Do you mean the output of findings would be in YAML instead of Rego?
**Liudmila Molkova** 21:18 Yeah, yeah, I mean, we write semantic conventions that test data in Regal, and it sucks.
**Josh Suereth** 21:25 Yeah, yeah, I hear you, I hear you. Go ahead, Arthur.
**Arthur Silva Sens** 21:28 I'm also thinking that you want to have multiple policies, right? This example repository will need to trigger all the policies at the same time?
**Josh Suereth** 21:39 No, the idea behind the test would be that we can test each individual package.
independently. So we'd actually test, like.
we'd test the one policy package just independently of each one, and then hopefully everything's composable. So if you include more than one, you know, they shouldn't conflict with each other, because they're all independent policies.
Yeah, I don't think they can conflict with each other, but that's a good thing for us to actually find out.
I think that would lead… Yeah, anyway, I'll think about that later. What I'm proposing is maybe we create a Weaver registry test command that actually takes some of our test infrastructure.
That we're using for doing policy checks and template checks. And we create a command where you can write a test for whether or not your policies work.
or a test for whether or not your template works. So it'd be test Weaver Registry, test policy, and Weaver Registry Test template.
Thoughts on that?
**Liudmila Molkova** 22:51 And…
**Arthur Silva Sens** 22:52 Isn't… isn't diff… like, very standard things that people do on CI. If we're just… Like, the task command will do what you're describing above, but in a single… Command instead of tree.
**Josh Suereth** 23:10 It's not… yeah, I don't know if it'll be 3 commands… like, the thing that's awkward here, I guess, to start with, I was debating just making a makefile.
That would, like, run all the things in order.
But the problem is, you need… you need a good diff command as well, the diffing the findings, and failing on change. We actually are using, like, a, syntax high… or an ANSI coloring diff.
That shows you, like, what's different in green and red, for example.
We'd have to make sure that all those tools are installed independently. I don't know, it's like a friction thing.
You're right, we could probably do this manually today by just calling Weaver the right way, it's just actually doing that is not non-trivial.
And I don't want to make it terribly difficult to add new packages.
**Arthur Silva Sens** 24:04 I would suggest starting with what's possible already.
And then document. Like, if people say it's too hard, then yeah.
Let's do it.
**Liudmila Molkova** 24:19 Will it have a makefile with a test target?
Similarly to some conf, where we can run multiple commands together.
**Josh Suereth** 24:32 So that's… that's probably what we'll do. I'll try to do a make-file approach to this. So every… test directory.
So right now, what I have is there's a package directory that has the Rego files in it, or the template directory that has the Weber YAML and the Markdown files in it, right?
Inside of that directory, there's also… will be a tests directory, and each one of those will be an independent test that runs, that will… Use your template.
use your policy.
And then check the output of that thing.
Okay.
Cool. Alright, so… that's that, and then… Last question is, how good do you think the initial packages have to be?
To ask people to start making and contributing them.
You know, do these have to be, like, fully formed, awesome, we want people to adopt them? Or can they be, like, yeah, the test will fail if you make a breaking change, and it's in progress, you know?
**Liudmila Molkova** 25:39 I think they should be easy enough so that somebody can read Ginger.
So, which means they are not awesome.
**Josh Suereth** 25:47 Okay, good.
**Liudmila Molkova** 25:49 So, it's like, easy ginger, I would… I would prefer this over complexity and awesomeness.
**Josh Suereth** 25:57 Okay.
Yeah.
Hope there's not an easy Ginger.
Enrico.
So, like, make sure.
**Liudmila Molkova** 26:07 Truly on.
**Josh Suereth** 26:08 read it, yeah. One thing I want to call out that I didn't realize until I reviewed this PR, did you know that Jinja has a different templating?
Syntax? Hold on.
You taught me something, Ariana.
**ariannavespri** 26:23 Yes, yes, I saw that that's, also what, yeah, when I was working on the PR, that's also what I had to discover, because it was not working until there was this, what are these signs called in English? I don't remember, like, this kind.
**Josh Suereth** 26:39 I don't know either. Are they less than and greater than? Yeah.
**ariannavespri** 26:42 Yeah, exactly. I don't know if there is a… according to the semantics and the context, they have different names in English, but those, the… those things, yes, because there is, like, a… Because there is, like, an over… they get over… I mean, what you would normally use, which is the curly braces, get overridden, unless it's, like, a dynamic thing where you have the double curly braces, and that's… is the same. But yeah, that's what I also… noticed, at the beginning, I didn't do the right thing, in fact, but yeah.
**Liudmila Molkova** 27:14 Should we switch to this? It looks so much better.
**Josh Suereth** 27:18 I think so, yeah, yeah, I think so.
Yeah, so you're saying, Aaron, that you couldn't use the percentages before?
**ariannavespri** 27:31 Like, where you can bracket percent?
Actually, when I try to use the, like, what would be the standard.
I'm not sure I was succeeding, actually.
So I just went for what worked.
**Josh Suereth** 27:44 Yeah, I, I, I do like this better, so I, yeah, anyway.
things we learn, right? Okay.
Sorry, I got distracted. Okay, cool. So, Ariana, I might actually take what you have as one of the initial packages, if that's okay?
**ariannavespri** 28:03 Absolutely, I mean…
**Josh Suereth** 28:05 Beautiful.
**ariannavespri** 28:05 I, I fixed, I fixed, the, the two things that you pointed out, the sorting, and then, like, the, the file name definition, I put it into the Weaver YAML file instead of the template themselves, so I don't know if, then if you, start another CI run, if it works.
I hope so.
Oh, yeah, I have to click that manually, don't I? Yeah, I mean, exactly, because that's the thing, yeah.
**Josh Suereth** 28:31 Okay. Are you… you are a member of the OTEL organization yet, or not?
**ariannavespri** 28:37 I don't think so, I mean, I… No. Okay. I mean, I just started contributing, so…
**Josh Suereth** 28:42 Yeah, I forget what the rules are around getting added to that, but I'm happy to sponsor you if you wanted to start that off.
**ariannavespri** 28:50 I mean, yeah, I mean, it's like, whatever, whatever, whatever can, like, how can I say, avoid the, the… the cumbersome aspect of it to ping somebody to just start a CI. I mean, the only thing that I would like to be able is start the CI myself, so…
**Josh Suereth** 29:08 Yeah.
Yeah, I think if you get audited to the OTEL organization, that will happen automatically on your behalf without someone in the organization having to approve it.
But also, like, we could get you triage permissions as well, if you want to, like, assign bugs and move things around. Like, we… anyway, there's a… on OpenTelemetry slash community, there's a process for becoming, like, a member. Go ahead and kick that off, and we can talk about that then.
Okay.
**ariannavespri** 29:34 much.
**Arthur Silva Sens** 29:35 You need two sponsors, I'm happy to sponsor you as well, Ariana.
**ariannavespri** 29:40 Yeah, thank you so much, I was thinking of asking Jurassi, because I think it makes more sense, if you don't mind.
**Liudmila Molkova** 29:47 You can ask Jerus, you can ask any of us, we would be happy to sponsor. I'm pasting the link to the…
**Josh Suereth** 29:54 -Oh.
**Liudmila Molkova** 29:55 this year.
**Josh Suereth** 29:56 If you need exactly two sponsors, you can have more. You just need at least two.
**ariannavespri** 30:01 What, okay.
**Arthur Silva Sens** 30:02 I thought that.
**ariannavespri** 30:02 safe.
**Arthur Silva Sens** 30:04 Yeah, I was raising my hand for another thing, actually.
**Josh Suereth** 30:07 Go for it.
**Arthur Silva Sens** 30:08 I… I created a template for Prometheus SDKs, and one of the first things they asked me already was performance.
if we could add benchmarks for the generated, output. Well, definitely not something that we'll ask for initial packages.
But something to consider when we call, like, a template stable.
**Josh Suereth** 30:35 I like that, that's interesting. Okay, yeah.
Cool.
I think… I think that's it for this topic that gives us a way forward. For context, I think, Jurassi's gonna have me on the Telemetry Beats podcast to talk about this, so my hope is to get the basic scaffolding of the repository up and working. I'll probably focus on getting the policy thing and some documentation written. I could definitely use some help in some reviews, so I'll send that out when that's ready.
But my hope is to have that actually out for people to view in a very rough state next week, like, by next Wednesday.
Cause I think the podcast is either Tuesday or Wednesday of… it might… It might be another week after that, I have to check, but I think it's Tuesday of next week.
I'm really good with time. Okay, cool.
Next up, depending on resolve schema, so this is part 2 of the, resolution changes, this one actually lets you depend on a published schema.
And import things from that publish schema.
in the V2 syntax.
So, few things. You can import from the registry, so you can import the things that are allowed to be imported.
Except, it turns out, and I should have realized this, you can only import events, metrics, and entities, you cannot import spans with our current syntax, both in V1 and V2.
**Liudmila Molkova** 32:13 Do you like that? Like, I mean, it's…
**Josh Suereth** 32:15 No?
**Liudmila Molkova** 32:16 Okay, yeah.
**Josh Suereth** 32:17 you want to The, the other, the other thing interesting here, I should mention this, you can only import from the registry. You can't import a refinement.
Cause the current syntax, you're importing metrics by name, you're importing events by name.
You're importing entities by type, And there was no identity for span in V1, Remember we invented the span type thing?
So, that, I believe, is why you can't.
**Liudmila Molkova** 32:55 So we could… we can import spans by type or by the group ID in the V1.
But refinements, we would need to find, like, import… metric refinement, so we have metrics, And… We could rename it to metric definitions and add metric refinements, or we can break it down and, like, import signals and import refinements, and it would match the schema we have.
For… the result one.
**Josh Suereth** 33:34 Yeah.
Do you, like, should we wait for a use case where people would want to import refinements before we do that?
**Liudmila Molkova** 33:45 I would not… it wouldn't be a problem, I think. I would be… it would be fine, but I think we need to… Have the syntax, the final syntax, in mind.
Yeah. Do we have a flat import structure? Do we break down by signal and refinements?
Or a registry and refinements to match it.
**Josh Suereth** 34:08 Right? Well, this gets into the next problem, because I think this is related. In V2, You can only extend groups via V1, So, the whole notion that you can, like, depend on something and refine it from a V2… like, you can't do that in V2 syntax.
Because we never implemented refinement in V2 syntax. So there is no way to create refinements in V2. So I guess maybe this, this is… I don't know if you have time to help me here, Lyudmilla, if anyone else is interested, but I think we need… to know how to refine things in V2. Like… I don't know how to create refinements in V2, we need to figure out what we want that syntax to look like, and then make that a reality.
And I think that will help with the import.
A bit, because it'll give Notion of, like, how things are layered, to know what imports should look like.
**Liudmila Molkova** 35:06 Yeah, I'll try my best, but I don't believe I will have any chance to work on this this week. I will be traveling since tomorrow, until the next meeting, and yeah.
**Josh Suereth** 35:16 Okay, okay. No worries then. But I do, I do think that I, I'm… hesitant to declare everything stable, like, for V2, until this is sorted. Like, I think this needs to be a blocker.
**Liudmila Molkova** 35:30 Yeah.
**Josh Suereth** 35:31 Related… With attribute references, this is the third thing that we figured out, in this, in this PR. So, right now, We have provenance, where we remember, like, where things came from.
When you refer to an attribute.
There's this notion of source group that it came from, okay? But when I am depending on a V2, registry.
It's just a registry of attributes. There is no group to attach it to. When we create a group, we just synthetically make a fake one to begin with.
So, I'm actually changing this to be, for now, I'm just pretending it's the, something like, dependency.registry name.
something like that. Like, we… I think we just synthetically make something for Providence, but, there's a thread I have with, Laurent, we have to figure out what Providence needs to be going forward, what we need to track, what we need to keep, and I think today, it's just becoming more and more broken, so I'm probably gonna take, after we get… the shape we want done for things, I'm probably gonna take a crack at just breaking all of it.
And making it what we want.
**Liudmila Molkova** 36:47 Yeah, I've been… sorry, go ahead.
**Josh Suereth** 36:51 No, go ahead.
**Liudmila Molkova** 36:52 I've been trying to… Imagine what the dependency… conflict resolution would look like, and I think Lauren just also replied about this, that the provenance, at least in my view, the main use case is the dependency resolution, the conflict resolution.
and the group ID is… Only important if it's needed there.
But the registry itself, the registry, the same thing you're doing, the registry is the… Source. For refinements.
this is… better, but then we will have a group ID.
**Josh Suereth** 37:39 Well, yeah, well, for refinements, we'll have the refinement ID. Yeah. Which is the replacement of group ID, yeah.
Yeah.
Okay, the second part here, which is more important, in V2, attributes don't have a requirement level in the registry.
In V1, they did.
And so, when you import an attribute, you have to pick a default requirement level, if you refer to one from V2.
**Liudmila Molkova** 38:10 when you reference.
**Josh Suereth** 38:12 When you reference it, you have to pick a requirement.
**Liudmila Molkova** 38:14 Right,
**Josh Suereth** 38:16 So, like, I have to provide one.
But, like, in the Rust code, I can't make it optional. I have to create a default.
I can actually add some sort of flag where if you have a V2 dependency.
That this causes a breakage.
if you don't override the requirement level when you import a V2 thing, it's… you're unable to express it in V2 syntax to begin with, so it's not a problem with V2 syntax, but if you're using V1 syntax with a V2 dependency.
We have to, like, fake a requirement level, which seems so temporary and awkward to me that I was just making it be required.
That's what I did in the PR.
**Liudmila Molkova** 38:58 Why not?
**Josh Suereth** 38:59 Okay.
Cool. So that, that's that. And then provenance, we just had a discussion on that. So, for context, please take a look at this PR. Ludmila, it actually implements your OTEP.
**Liudmila Molkova** 39:12 Nice.
**Josh Suereth** 39:13 The other thing that I'll call out, it's in the notes of this, So, right now, it doesn't work where you can't extend groups from V2, because we don't have a way of extending groups, and it's using manifest.yaml.
Your OTEP uses manifest.yaml, I use registrymanifest.yaml, because that is what Weaver used previously.
**Liudmila Molkova** 39:37 Do you have a preference?
**Josh Suereth** 39:39 I don't care, but if we want to keep compatibility with what we had before, and you want to move to Manifest YAML, I just have to write more code and do a lot more testing, and I have some shenanigans in there that you'll have to take a look at.
Basically, the TLDR is, in the OTEP, 1.0.0 could be a directory that has a manifest YAML, or 1.0.0 could be the manifest itself.
And then it can point at a different file that way. It supports both.
To make that work was actually… I probably spent too much time on that, but I had fun doing it, so we'll call it even.
those are, like, the two things for you to understand from the OTEP, but I'm fine moving this to be both manifest and registry manifest, just… I… I'm not gonna write code unless I have to.
**Liudmila Molkova** 40:32 Let's keep it registrymanifestyleupdate.tub, it doesn't matter, we can always support roles later.
**Josh Suereth** 40:39 I'm fine either way, yep. Okay.
Cool, but this should be a full implementation of what you need for the OTEP now, for doing the dependency resolution.
**Liudmila Molkova** 40:51 Awesome.
**Josh Suereth** 40:51 And it has one test that should test all the features, but please take a look.
Cool.
Alright, I spent a lot of time here, sorry. Let's move on to the next one, building registry on top of hotel.
**Liudmila Molkova** 41:05 Yeah, so I've been playing with the specific example, for the OTAP, and… I… have two things maybe I can share?
**Josh Suereth** 41:16 Yeah, go for it.
**Liudmila Molkova** 41:28 Sorry.
Great, sorry, I've lost my notes. And… Anyway… Here we go. So, there are two examples. The first example is what I think we should not do.
But it's, it's, representative. It's, let's say, it's based on one of the Java examples, for our GMX metrics.
So this combines whatever the… Attributes defined there, and also metrics defined there, plus import some references, some attributes from the central registry.
We had some debate with Store, and I'm… it's, Said he couldn't make it. What this should look like, the output.
And currently, it is the subset of the combined registry. It does not include anything that's not used.
And this matches my mental model. Lauren would like to see the combination, the open registry. Like, it's… it's the superset. I think we can add a Later. It makes sense as something that you publish, that you only publish what you emit, and it's what we need for, OpenTelemetry subregistries.
**Josh Suereth** 43:21 There's a flag, Lyudmila, that if you specified the flag, it would include everything.
**Liudmila Molkova** 43:27 Right, yes.
**Josh Suereth** 43:28 I wanted to get rid of that flag, but we… that… yeah.
**Liudmila Molkova** 43:32 Yeah.
**Jeremy Blythe** 43:33 Would be useful, though.
**Liudmila Molkova** 43:35 How do you use it, Jeremy?
**Jeremy Blythe** 43:38 So when you're developing, you're exploring, or we are looking in the new website, or with the MCP, you don't… you haven't made your registry yet, so you want to have everything available to you so you can search and find, and so on. So it's really good during, like, the development phase.
Maybe you don't want to resolve to that?
Like, as an output.
But internally, it's really useful to have Weaver resolving that in memory.
So that you've got everything available, the whole search space.
**Josh Suereth** 44:11 That's interesting. Should the MCP and the API be able to search your dependencies for things and tell you this comes from a dependency you haven't imported?
**Jeremy Blythe** 44:21 Yeah, so that's what we need the provenance for.
So that then we can show in the UI that this is coming from such and such a registry versus the hotel registry, right?
**Josh Suereth** 44:35 Right, but what I mean is, like, in the manifest, if you see there's a dependency chain, you could actually load the dependencies as well, so that when you search, you can search, here's what's from your registry, by the way, your dependency is this too.
**Jeremy Blythe** 44:49 doesn't it do that?
When you resolve, isn't it doing that already?
**Josh Suereth** 44:56 Sort of. If you specify… so, it is doing that, but it's not keeping it for you.
Like, what I'm saying is it keeps it as a registry that says, here is… here's the registry from this dependency. You can actually search across it and do things.
**Jeremy Blythe** 45:18 I think I must be… I don't have my brain switched on today.
**Josh Suereth** 45:22 So, no, the way it's implemented today in Weaver is that your dependency gets embedded into yours, no matter what.
And then it garbage collects things that aren't used. So it actually is not preserving the dependency as the dependency solving. It is importing everything.
Right? So if you don't set that import flag, Jeremy, you don't get any of the data. What I'm saying is, why have the import flag if we could instead have the search actually search over the dependency itself? Because I have loaded it, like, with the changes I've made, it gets loaded as a resolve schema that you could search across.
So, you.
**Jeremy Blythe** 45:57 Oh, I see.
**Josh Suereth** 45:58 resolved schema of you and the resolve schema of your dependency.
**Jeremy Blythe** 46:02 Obviously, so you've kind of got two resolve schemes in that.
**Josh Suereth** 46:05 Except we're dropping the one and throwing it away.
**Jeremy Blythe** 46:09 Yeah, so you're suggesting keep, keep, keep all of… Resolve the… resolve all the dependencies as well.
like, independently.
**Josh Suereth** 46:18 Yeah, yeah, I have to resolve them anyway to make this thing work, but I could, like, keep the tree and give it to you.
**Liudmila Molkova** 46:26 And it would be necessary for the conflict resolution anyway, once we need it.
**Josh Suereth** 46:32 By the way, just for context, it's disturbing how close this is to designing a new language.
Yeah! It's… this is, like, all the same problems.
Anyway…
**Liudmila Molkova** 46:44 And we are not even started to define types, but we will. Anyway, yeah.
**Josh Suereth** 46:49 That'll be the easy part.
**Liudmila Molkova** 46:50 Yeah, okay, so… the thing I'm focusing on here is what we publish, right? This is what they want to write in DotApp so we can make progress, and I think the publishing part, it should be the leanest one.
And the linest one is the smallest one, and there could be alternative ways to represent it and parse it. But this is just one library, so one of the things, I don't think we need to define, decide on and document, but I think we should have an opinion.
And how do we do this for, let's say, collector or a Java instrumentation? And I think it should be a registry per repo, essentially.
We're per some large group of instrumentations. Otherwise, it's impossible to manage, and we would have a very fun time Resolving conflicts if everything depends on the hotel.
So I think people would combine multiple things together, realistically.
And, as the result, we would have a registry per repo.
It has some interesting, maybe, problems with versioning.
So that you cannot version independently, but at the same time, you can have multiple schema versions, and different instrumentations can use different schema versions in the same registry.
So it probably has a solution, but it could have some interesting complications, the grouping.
**Josh Suereth** 48:21 I'm leaning towards, like, I want to go back to, like, what principles we have for how this will be defined and where it lives. I would personally… I still think we should lean towards, the schema being tied to the versioning scheme used for that component.
So, like, if Java instrumentation is all versioned together in one big go, having a big bundle is fine.
But, for example, for, like, Go modules, if they are versioned independently in some fashion, and you can, like, release them all independently, and they wanted to say, cool, we're gonna have one registry for each version that's released independently.
I'm okay with that, like, because I think it ties to the thing you're releasing.
Right?
**Liudmila Molkova** 49:08 Yeah, both are possible. It's just… it would… could be a huge headache publishing all the schemas.
**Josh Suereth** 49:15 Bye.
I don't know. I think it will be a huge headache publishing all the schemas no matter what. I guess what I'm asking, how much more of a headache it is if there's more than one?
per repository.
**Liudmila Molkova** 49:30 the automation should probably do it for… regardless. But this brings us to, the second question.
Meh.
We need… Do you have an idea of how we name them? This is what we do today. I think we should replace it with some conf, and leave this part of pass for The component name.
This creates an interesting possibilities, so somebody in the future can do this and discover all hotel schemas, but let's not get there yet.
Yeah.
This is FYI, if you have opinions, let me know.
the… conflict resolution. So, Josh, I started writing in .tab that there is no conflict resolution.
I've wanted to… you left a comment, I wanted to dig a little bit more into this, but I think the principle is let's avoid conflict resolution as long as we can, and the only place we cannot avoid is dependency… diamond dependency problem.
**Josh Suereth** 50:49 I… I… Yeah, no, I think we have to pay attention to this earlier, we're gonna get bitten hard. Like, think of ev… we were just talking about node package lock JSON. Do you know why it's breaking? Because they changed their dependency resolution algorithm.
And they did so in a way where optional dependencies look different, and it breaks the crap out of everyone because, like, the package lock changes, and the… dependency resolution is the hardest problem in build tooling, and programming language tooling. It is, like, I don't want to take… I want to make sure if we're taking a shortcut, that is one that we can fix in the future. I… I am not comfortable… I would rather go with a Python linearization approach than with we… we allow things to happen.
Right? So, linearization would be great. We force flatten everything. So, if you give us a… what looks like a diamond.
I'm gonna force flatten everything into a linear order dependency.
and one version gets inserted here, and I will tell you, hey, you have two… you're… depending on two things, I'm forcing this one, or I'm breaking, right? Like…
**Liudmila Molkova** 52:05 Okay.
So… This would mean we will need to change our result schema.
Because… Because we need to understand your further dependencies?
because… this… This. It came from your dependency.
And you should just mention where it came from, and drop everything else, so that.
**Josh Suereth** 52:38 Well… Yeah, this is where… what I want to… I think you're right, we have to keep Providence there to know where it came from.
You're also adding a notion of, semantic versioning, right, to the version scheme.
**Liudmila Molkova** 52:54 Yes.
**Josh Suereth** 52:55 Okay, so the principle I want right now is basically we linearize Everything, to try to make a linear order, when we have two nodes that are squashed together.
If they are of the same major version.
Right? We will drop all instances of something from the lesser-minor version and replace it with the most recent major version.
When we encounter it.
If you have two different major versions, we actually call that a dependency in a conflict, and you cannot… we cannot resolve it.
Like, that… so, the second piece is what's most important to me.
**Liudmila Molkova** 53:34 Yes.
**Josh Suereth** 53:35 Because I think we have to do that now.
We, like, we have to have that ahead of time.
The first thing about what we do when there's two different major versions and how we handle it.
We probably need to be consistent now, because what… if we're… if we're not a little bit… strict here. What winds up happening is people have patterns that work, that are really hard to implement safely. We add a check to prevent broken patterns, and we start breaking valid usage.
This is, like, the issue of taking Python and adding a type system.
no one will buy it. It's better to start incredibly strict and loosen up over time than it is to start, like, completely loose and strict up, right?
**Liudmila Molkova** 54:22 Yeah, that, that's what I… thanks for… Creating more clarity, that's the… my proposal, is be as strict as possible.
**Josh Suereth** 54:30 Oh, oh, okay, okay. When you say, like, we don't… I thought you were saying we just ignore problems and, like, allow things to get merged from different depending.
**Liudmila Molkova** 54:38 No, no, no, no, no, no, not… not allow any conflicts at all if this is… it's, it's actually… It… it could be possible, to some extent. I don't think we can, like… if we publish multiple versions of this… of libraries, of semantic conventions, that anybody who depends on them would not be able to build their own registry. So we have to allow… we have to have some resolution mechanism, but it should be as strict as possible.
And yeah, the using latest version makes the most sense, in my experience.
**Josh Suereth** 55:19 Cool. We'll have to make a new resolution algorithm to grab that. One last thing to think about for your OTEP, we should mark semantic conventions 1.0, if they're not alright. I think they're 1.x, right?
**Liudmila Molkova** 55:35 Mmm, I did.
What do you mean?
**Josh Suereth** 55:39 So if we're using the same major version, things are compatible, and minor versions are where bumps are.
**Liudmila Molkova** 55:46 Right?
**Josh Suereth** 55:48 semantic conventions right now is, what, 1.39. Next release is 1.40. Next release is 1.3.
Okay, cool. As long as the way we're releasing it, that is considered compatible, that's great.
And we'll have to actually, like, have version bumps now in semantic conventions when we do breaking changes.
**Liudmila Molkova** 56:07 Oh, so you're saying we… It will be 2 point something.
**Josh Suereth** 56:14 we… yeah, sorry, that's what I meant. When I said 1.0, I guess I meant 2.0. But yeah, I think, like, maybe it's worth making a 2.0 of semantic conventions, or I'm fine keeping it 1.0, but when… if we do changes that, like, are breaking, we make it 2.0.
**Liudmila Molkova** 56:33 That are breaking unstable, which we've never done so far.
**Josh Suereth** 56:39 We haven't done so far, but I'm thinking of that dev artifact.
That, you know how you want it to be, like, 1.x-dev?
go look at the rules for how SEMCOM treats that, because I think we will… We will not be able to support our dependency resolution that we want effectively with that, and breaking changes will not be breaking. Like, it… all hell breaks loose with that particular thing. I think you might need to actually call it something different.
**Liudmila Molkova** 57:12 I see. So the, the, okay, dependency are… Dependencies on death.
**Josh Suereth** 57:20 Yeah.
Dependencies on dev will be hell, unless we actually figure out that thing.
**Liudmila Molkova** 57:26 1B, because… We don't allow… we don't remove things, ever.
**Josh Suereth** 57:35 But we break things. How do I know that the dev that you're using is not… it is actually compatible with the dev I'm using to replace your version with a different one?
**Liudmila Molkova** 57:46 Compared with Spyton, if it's perilous version, the hell is expected.
**Josh Suereth** 57:54 Right, but the way… I'm gonna use the semantic versioning library.
To compare the version numbers.
1.x-dev, and 1.x plus 1 dash dev.
are considered compatible.
Are you gonna be breaking me in those versions?
Or are you going to be bumping the major version? If you bump the major version, that means you're bumping the major version for all semconf, not just the dev artifact.
I think there's a problem here.
**Liudmila Molkova** 58:25 Let me think about it, but I think this problem is… Similar to what somebody has depending on semantic convention artifact.
It's exactly the same problem, unless, say, Java or Python.
And we've done everything we could to prevent it from being, like, the terrible problem. Because we don't… Remove things, we only deprecate them.
Anyway, we are out of time.
**Josh Suereth** 58:54 Okay.
Cool.
I'll follow up on the OTEP, but I think we're making really good progress. We had a lot to get through.
Yeah, we're out of time. Arianna, I hope you don't mind… I mentioned your PR several times already. Thank you for making changes, I'll continue to review it. I think I… for… for context here, for Jeremy, and I know Lauren is not here, but for Jeremy and Ludmila, I think what… makes sense here is possibly to take this PR and merge it into Weaver, and then move it to the new repo when the new repo exists, but…
**ariannavespri** 59:26 Goodly.
**Josh Suereth** 59:27 Yeah. Please comment on the PR if you feel differently.
**Jeremy Blythe** 59:31 Makes sense to me.
**Josh Suereth** 59:33 Cool.
Awesome. Thank you, everybody, and we'll see y'all next week.
**ariannavespri** 59:39 Maybe, maybe, Lyudmila, you can sponsor me then?
**Liudmila Molkova** 59:43 Absolutely, yes.
**ariannavespri** 59:44 Fantastic, thank you so much. Bye-bye.
**Liudmila Molkova** 59:46 Thanks.
