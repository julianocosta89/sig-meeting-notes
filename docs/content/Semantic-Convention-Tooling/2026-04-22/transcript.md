SIG: Semantic Convention Tooling
Date: 2026-04-22
Duration: 42 minutes
Zoom Recording URL: https://zoom.us/rec/share/Uom9_G2AqJZdfG1v79Rv2Oa3FIUJ-J9el1HPJ_wb8t3FY3FvuZHCJZlE4JhKq4F2.DjvZvvUO7vCHh1kX
============================================================

## Zoom Recording Transcript

**Josh Suereth** 04:43 Hey!
Sorry, I was grabbing some coffee.
How you doing?
**Jeremy Blythe** 04:51 I'm good. How are you?
**Josh Suereth** 04:53 Not bad, not bad. It might just be you and me today.
**Jeremy Blythe** 04:56 That's okay, I couldn't bring the first off, anyway.
**Josh Suereth** 05:01 Yeah, yeah, let's try to go through it quickly. Actually, I might just go to RPRs.
Let's see, hold on, GitHub Weaver, I have it open on a different… computer, so I gotta switch.
How do I share this tab instead? Okay.
Cool. So I wanted to show a few things. First, Yao has this metric requirement level one.
if you haven't seen it, it just adds requirement level to metric. It looked pretty good to me. I had two questions on it, which is just one.
I think instead of calling it metric requirement level on V2, Because you know it's a metric already?
Which is called requirement level, which is dumb.
But that does mean it has a different name than the V1 group. Anyway, I think that's fine.
**Jeremy Blythe** 05:54 It's… V2's breaking anyway, so…
**Josh Suereth** 05:56 Yeah.
Yeah, then the other thing is, There's a bit of a question on whether it should be required versus optional with a default.
And, like, what… what that would mean with refinements, but… We don't have to dive into it today, since I know you have to leave in, like, 20 minutes, so, like… just… comment on the PR, love your thoughts. I don't think… unless Yao's here, I think it's probably better to have the discussion on the PR. But just want to call your attention. That came in this morning, super excited to see that.
Dude, I don't know… I don't know if it's AI, but, seeing the number of people who can write good Rust code, or, like, decent-looking Rust code now is… is… makes me happy.
**Jeremy Blythe** 06:40 It's probably Claude.
**Josh Suereth** 06:42 Yeah, yeah, but the fact… the fact that we get something that then is, you know.
It's removing some of those things. Okay, here's another one. Remove the vendor to open SSL dependency. I approved this with a comment. I don't know if you see what was done. I think this is clever. Basically, we only vendor… where we need it. So this is basically, if the configuration's not Windows, then we vendor OpenSSL.
If I remember right, we don't need to vendor anywhere but, like, muscle.
**Jeremy Blythe** 07:14 in the north.
**Josh Suereth** 07:14 container.
**Jeremy Blythe** 07:16 It was the docker.
Yes, it was Docker because there was, There was a change to the… C libraries, right?
**Josh Suereth** 07:27 Yeah, the AWS LWC library, yeah.
**Jeremy Blythe** 07:30 Yeah, so then that meant that… We no longer had the compatibility, so then we had to… Then we had to use OpenSSL.
Yeah, that's where we are now, yeah.
So, I'm thinking…
**Josh Suereth** 07:44 I'm thinking one of two things here. What if… So, so this… we… we were vendoring LWC before.
like, OpenSSL, we're vending, but we were… we were using LWC before.
And before that, I think we weren't vendoring, we were relying on platform certs.
And we had an issue with Docker, where, like, there weren't platform certs installed, and we didn't want to install platform certs, or there was some sort of, like.
issue.
Okay. Here's… here's what I'm thinking.
Maybe we merge this as is.
But… what do you think about us making a feature, which is Vendor OpenSSL for Weaver.
And then we just build the Docker container with that feature, but that feature's off by default.
**Jeremy Blythe** 08:34 What does that give us?
**Josh Suereth** 08:36 it means that Docker… like, only the Docker build.
will vendor… will vendor open SSL, because it needs it. Every other build of Weaver will just use your native SSL dependencies the way that this thing does.
Which is, I think, what we'd want.
**Jeremy Blythe** 08:57 I think what we… I think what we wanted… Was to use, Rust TLS, or whatever it was.
You didn't want this at all. We didn't want this at all.
**Josh Suereth** 09:08 Right, but this… this effectively, I think, moves us to Rust t… well, we… but we could do that, I guess, with what I'm suggesting. So we make a feature.
that we use for the Docker build that will… that will build Rust TLS in a way.
that, it's Docker-friendly for our Docker build.
But all of our other builds just use regular Rust TLS the way you would if you were building locally, you know?
**Jeremy Blythe** 09:30 That means we would… to… Would we need a feed… yeah, we'd need a feature.
**Josh Suereth** 09:38 Yes.
Yes.
**Jeremy Blythe** 09:40 Okay.
Because we need to change the cargo terminal.
Because it's the GIX library, it's the GitHub, the Gixx library thing, isn't it?
They're causing the problem.
**Josh Suereth** 09:52 Yeah, GIX was… it's a… it's actually a conflagration. Like, it affects GIX, it affects, It does affect some of the HTTP serving things we have.
Hmm. Because there's, like, a dependency between them.
And so we have a thing where, because GIX has a dependency on, like, the… whatever the HTTP request, is that what it's called?
**Jeremy Blythe** 10:19 Yeah, I think so.
**Josh Suereth** 10:20 Yeah, like, everyone depends on request, but because we go through different tree branches, it was like a pain in the ass to untangle everything. GIX was the problem that led to us vendoring OpenSSL, right?
Right. But I feel like we could make a feature that lets you choose if you're gonna use OpenSSL, or Boring Crypto, or AWS LWC, or Rust TLS, the, like, bind-to-native thing.
And then we just make our Docker build, build with the feature that makes it build correctly, and whatever the default we pick for that should be the one that we… that we think is nicest for general development, you know?
I've never done this in Rust yet, so this is… a cool, exciting, fun thing that I'll probably bungle and get Claude to fix for me, but .
**Jeremy Blythe** 11:12 Right, yeah.
**Josh Suereth** 11:13 You're amenable for it. I say we merge this as is to fix, what… OTel Arrow does, and then open a bug to do the rest of the work.
**Jeremy Blythe** 11:24 Okay, so this is… This is… this is using OpenSSL, but not vending it.
But only when it's Windows.
Huh.
**Josh Suereth** 11:36 No, so, here, I'll…
**Jeremy Blythe** 11:38 The other big round.
**Josh Suereth** 11:39 If I, if I show you, 4 windows only.
We don't include the OpenSSL dependency.
**Jeremy Blythe** 11:51 Okay.
**Josh Suereth** 11:52 which, if I recall correctly, the way that the bundling crap works is if OpenSSL exists.
It's vendored and available.
And if OpenSSL isn't there, Rust TLS, like, looks for a thing to bind to.
the reason we're including OpenSSL locally is because of the Docker container. So, like, I think we honestly only need that for muscle. Like, I think we could change… I think everything would build successfully if we just said config muscle, if that was even a thing that worked.
As opposed to config, not Windows?
**Jeremy Blythe** 12:29 Is it… is it… is muscle the problem, or is it the… the base of the Docker container.
**Josh Suereth** 12:39 It's a little bit of both. So, the base of the Docker container has nothing in it.
**Jeremy Blythe** 12:44 Yeah.
**Josh Suereth** 12:45 There's no… there's no SSL.
So, we need to vendor something.
And the, lib SSL that we… the lib AWSLC that we were using broke their muscle build.
So we couldn't build them anymore. So we moved to OpenSSL, which was a huge negative, I think, overall for Weaver.
**Jeremy Blythe** 13:09 Yeah, I'm just wondering if there's a… how far… is it worth looking at? Because one of… We kind of fixed that in a… in a rush.
**Josh Suereth** 13:18 Yes.
**Jeremy Blythe** 13:18 You? I wonder if there's a… A little more time.
Because there are other base… there are other bays, because I… I went, oh, Debian, but then it was huge, right? So we hacked out of that, but… There are others, right? Isn't there a Google one that's…
**Josh Suereth** 13:35 Yeah, it's called Boring Crypto, yeah.
I forget what the Rust version is, though. It, like, there's a Rust thing that depends on boring crypto. That, I… and here's the thing.
I'm a Googler. Google doesn't say anyone should use foreign crypto outside of Google. Like, we build it for ourselves.
**Jeremy Blythe** 13:53 Okay.
**Josh Suereth** 13:53 it, like, but… but it's a darn good library, and, like, I have to use it internally.
So… I don't understand why we don't tell people, like, why we tell people they can't use it. I mean, I kind of do, but I kind of don't. It's just frustrating.
But yeah, that's why I think what we should have is a feature flag that lets you pick when you build, what you're gonna have.
And then we try to go for the best option in our release build. So, in Docker, if we have to go with OpenSSL, great, we use OpenSSL. But, like, we can use AWS LC, we can use Rust TLS, we can, like, whatever for the other platforms, because it's reasonable for us to expect you to have an SSL library on Windows, on Mac, and on Linux, you know? We don't need to bundle it, so let's make it a feature and go from there.
**Jeremy Blythe** 14:48 Okay.
**Josh Suereth** 14:49 Okay, I'm gonna… put this in the notes.
So, let's see this, move forward… Let's create a feature to note that you can use.
Install the libraries.
Building… We'll get, Docker to use… openness.
It's now, but… Okay.
Cool, next up.
everybody's favorite dependencies. I have two PRs here.
Oh, did the one get merged?
Oh, here it is. This is… this is part one, part two. I'm gonna show you part two instead of part one, if that's alright. Part 2 has, a few issues, but effectively what I've done oh yeah, I have some vibe-coded tests that I need to go… I didn't finish all my clippy on them yet. But I wanted to push it so you could see it. Okay, so basically what this does is a few things. First of all, I keep randomly adding clone into, our schemas. I hope you don't… like, do you have any problem adding clone to things?
**Jeremy Blythe** 16:23 Not really.
**Josh Suereth** 16:25 Yeah, it just makes testing easier if I can clone, make a change.
So I started adding clone to more stuff.
There's a Rust feature now, where you can say, here's, like.
the default derives I need, and you specify one thing instead of all of them every time. I'm wondering if we should start doing that, but anyway. Alright.
Cool. So what we have now, a few tests.
**Jeremy Blythe** 16:51 Hmm.
**Josh Suereth** 16:52 We have incompatible version conflict tests, we have invalid version conflict tests, we have, we updated published registries. I can show you what this does. Right now, I'm actually requiring the version number?
Oh, yeah, that was, that was a bug. I'm requiring the version number on dependencies to be a specific thing.
Yeah, that's the clone… okay.
But what this changes, it does a few things. First of all, this is huge.
we can now… we now require the schema URL to have SEMBER.
And if I ever fail to parse Sember.
I can't make decisions about, like, which dependency to choose over another, so I actually issue a failure and says, this schema URL is not abiding by SENVER, we can't use it.
**Jeremy Blythe** 17:48 And that…
**Josh Suereth** 17:49 we basically need to find a way to disallow bad schema URLs in the ecosystem. Otherwise, the dependency resolution won't work. So that's part one. Part two is I start having a duplicate dependency thing. So, we have an error that says a duplicate dependency was found.
This error, as of Part 2, will only show up if the versions don't have the same major version number.
So, like, if you're depending on version 1 of.
**Jeremy Blythe** 18:23 magical.
**Josh Suereth** 18:24 conventions in version 2 of semantic conventions, you'll get an error saying, hey, this thing has a dependency on SENVER1 and SENVER2. Those are incompatible. Sorry, like, you can't do that.
**Jeremy Blythe** 18:35 Okay, so we're… The decision is to not support multiple versions.
**Josh Suereth** 18:41 No, we do support multiple versions.
So if you depend on SEM for 1.0 and 1.1, you don't get this error.
**Jeremy Blythe** 18:49 Oh, because of the major. Yeah, you said that. Yes.
**Josh Suereth** 18:52 Yeah, so it's only incompatible versions, and I'll show you where I do that check-in in just a bit.
**Jeremy Blythe** 18:56 Gotcha.
**Josh Suereth** 18:57 Lastly, this one… this is part two. I have a Part 3 that I'm gonna work on after this one, but Part 2 If you try to refer to something that is defined in two separate dependencies.
**Jeremy Blythe** 19:11 Yep.
**Josh Suereth** 19:12 It's ambiguous, and we just issue an ambiguous error and tell you which dependencies, like, it comes from.
There's no way for you to fix it, because there's no way for you to disambiguate, which is what part 3 would be.
But at least now, like, we'll try to do the best we can, but if something is ambiguous, we issue an error.
**Jeremy Blythe** 19:31 Right.
Yes, okay, that makes sense.
**Josh Suereth** 19:35 So those are the errors, and then, under attribute, like, the magic is in two places, dependency and attribute. So in… independency, I had to change all of the import stuff to actually include schema URL for everything, so that we know, like, where stuff came from. And then, yeah, this, this basically is now… Oh, the other thing we're doing is we're returning… oh, that's Group of Providence, this is Group of Providence. So this is just the mechanics of trying to get the schema URL into things.
wait a second… I need to push another change. Yeah, this has a bunch of expects in it that I got rid of.
So… I'm on the fence about this. I'm curious of your opinion.
theoretically, Theoretically, this should never fail.
we're taking a schema URL, Why… why am I doing this? This should just be .clone.
I'll go fix that, that must be vibe-coded. There's a few of these expects that were, like, legit.
**Jeremy Blythe** 20:45 Boom.
**Josh Suereth** 20:46 That I have to fix. That must be Vide-coded, that expect should be gone.
Sorry.
Right, so, so this, this is just, like, accounting for keeping the, schema URL in things, then there's a fallback search for groups, where if we can't find… First, we check the provenance of the group.
Or we check this root attribute thing that was used, and we look for provenance. And then, if that doesn't work, we actually iterate over the local groups, and we say, hey, we figured out what the source was from the group provenance of an attribute, and flesh it out there.
Yeah, there was, like, some stupid bug. I might… I'm gonna try to clean this up a bit, because I kind of let… Gemini go a little too wild.
But that's basically what this does.
The next part, where… that's dependency… The bit… the big, important bit is the resolving of dependencies here. Is this all tests?
This is against Maine.
I wish I could show you in my IDE, but I can't show my IDE.
Okay, let me go to attribute, maybe it's in here.
Thought it was independency. This group for Providence, this is import.
Oh, it's in Resolver. Okay, yeah, yeah, I'll go to Resolver next. That's where it is.
Or loader. Okay, so this is… this is the meat of the dependency chain part. This is what I spent the most time in.
Effectively, what we do is, instead of just tracking what registries we visit, and trying to avoid a circular dependency.
We track what registries we visit, we parse the schema URL, And we check to see if we have a name conflict. So, I changed schema URL to have name, which grabs everything but the version.
And then we have a hash map of, like, name to version. We check to see for a particular name, if there was a previous version. If the previous version's not the same, then we check their compatibility.
If the compatibility is a problem, we issue the error. That was where we get that, like, you know, mismatch version error. But if the compatibility's fine, we just let it go.
And we will pick the latest… yeah, we, we let… Where do we pick the latest?
Visit registries.insert… I need to update this to have it actually pick the latest. Oh, that's right, it doesn't matter if we pick latest here. Okay. It kind of does, but kind of doesn't. I'll talk you through that in a little bit.
I need to update this to pick latest. Okay, so that's another bug. Let me make a note.
This should pick latest.
version, and… Make sure… Visited registries as… Latest.
Version in it.
Okay.
Cool. Alright.
So that… that's… that's doing that logic. Then, here is the… where we actually load dependencies, again.
There's yet another where… place where we have to check version compatibility. This is a fun one. So basically.
When I load a registry, right.
I'm only loading the resolved registry, and the resolved registry has a set of dependencies in it.
I'm not going to necessarily load all the sub-dependencies, because I don't need to. That's, like, where things… that's like the, you know.
my downstream dependencies that I'm leveraging, but I still need those dependencies to know if I have version conflicts between things.
**Jeremy Blythe** 24:56 Wait a minute, you're loading the resolved registry?
**Josh Suereth** 24:59 Loading the results registry, yep.
**Jeremy Blythe** 25:01 But that resolved registry has… Has been resolved from its dependents.
**Josh Suereth** 25:07 It's resolved from its dependence, and it has dependencies that it lists, right?
**Jeremy Blythe** 25:11 Yeah, but…
**Josh Suereth** 25:12 Boop.
**Jeremy Blythe** 25:12 Why do you need to then…
**Josh Suereth** 25:15 I need to track what those were.
Because what happens then is, if I… like, let's say I… let me make this practical, okay? I'm resolving registry A and B.
Okay.
A depends on C.
at a particular version, B depends on C at a particular version.
when I resolve groups, if they are re-exposed in A or B, Like, if they have an import.
And I'm resolving from B, and I get… the group from C that's in the diamond.
And I'm resolving from A, and I get the same group C that's in the diamond.
I need to see if those are compatible.
And I need to see if those are allowed.
So what I do here is I make sure… I make sure that the dependencies are at least compatible between the two, or I say, you can't use these things together. So, like, if A depends on version 1 of Semconv, and B depends on version 2 of SEMCOM, I would say that's incompatible. But if A depends on version 1.0, and B depends on 1.1, that's great, and I will actually always pick the ver- you know, if you reference something in my dependency chain, I will just pull the version 1.1 when I can.
**Jeremy Blythe** 26:37 Okay.
**Josh Suereth** 26:38 This is, again, this is rather complicated, so that's one we want.
**Jeremy Blythe** 26:42 When… when B is a published package.
Yeah. I'm talking about, that's been resolved.
Yep. Anything that it depended on in C is now part of B, right? It's like…
**Josh Suereth** 26:54 It's part of B, but it's tracked as having come from C.
**Jeremy Blythe** 26:59 Where… where are we keeping that tracking? That's just in the manifest, right?
**Josh Suereth** 27:04 No, we added.
**Jeremy Blythe** 27:06 Oh, you've added the provenance.
**Josh Suereth** 27:08 We added it into Providence, and this is why.
Because what I wanted to do is, if I have A and B both depending on SEMCOM, and they're re-exporting something, I don't want to then have a conflict when we go to resolve.
**Jeremy Blythe** 27:20 Oof.
**Josh Suereth** 27:21 Later, right? So this will automatically say, oh, cool, you're using, you know, you're using HTTP, request count, you know, from SEMCOM, great.
I can automatically resolve that conflict and just… and it's not a conflict, because I know you both pulled it from the same SEMCOM dependency.
**Jeremy Blythe** 27:41 Yes.
So we're saying that… that those… two versions of SEMCOM are compatible, provided the major version hasn't changed. Yes. And therefore, you'll pick the… Okay… But that's not the case.
That's not the case.
for non-stable.
**Josh Suereth** 28:04 Yes, but non-stable, you would… you would get a conflict.
Oh, oh, oh, I see what you're saying. Yeah, this does rely on, SemConv, like, splitting unstable into a thing that they release with an unstable version.
Which is at… which is on the docket?
**Jeremy Blythe** 28:24 It is, okay.
**Josh Suereth** 28:25 Yeah, that's something that Lydmilla wants to do, and I'm thoroughly supportive of that.
**Jeremy Blythe** 28:30 Because I think, myself included.
We kind of have a… and it's okay, because we don't have this sort of diamond thing going on, but… We just go, like, I'd rather use the thing from Semcom, even though it's not stable right now.
Which I think is quite common.
**Josh Suereth** 28:49 Well, and that's… so what will happen is, that, that should be fine here, right? Like, like, I don't think we're gonna cause a problem. We'll update SemConf. The other part is, Wait, which, which… let me go to my tab. Okay.
The other part here, then, is in attribute. This is where… this is where the meat of the version 2 of this draft spec comes in, but I update, when you resolve an attribute ref now… well, first of all, I made a new helper method, but when you resolve it, it returns a result, because it could fail.
And we return attributes remembering what source they came from, to do that resolution between attributes.
**Jeremy Blythe** 29:31 Nope.
**Josh Suereth** 29:32 And we will resolve conflicts the same way we were other things, where we'll say, cool, if I have two attributes from two sources, ResolveConflicts will basically say, you know, if these are both from SemConv, pick the… pick the latest version one.
And drop the other one. But if they're incompatible versions.
then issue an error that says I have an incompatible thing. Theoretically, I shouldn't be able to get incompatible versions here.
And that's one of the things I was struggling with in this PR. If you look at Resolve Conflict, it's a little crazy. Basically, if it was defined locally, I'm the same version number. Great. If one was defined locally, and one is from a dependency, local always beats the dependency when I'm referencing something.
That was a decision I made.
if I pull from a dependency, and local, right? The idea here is the one wins.
Oh, wait, no, I'm always… I'm always picking… I'm always picking one side on these two. I forget why I picked one side, I'd have to go look at how I call resolve conflict for that. And then here's the problem case, is if I'm seeing it from two separate dependencies, I will check to see if the schema URL is the same.
And then I will grab the version number from schema URL, so this is where it gets December, and I'll just make sure if one is bigger than the other, I return that one, otherwise I return the other one.
And if, if I had any errors, I'd just say it was an ambiguous reference. Meaning the schema URLs were not the same name.
But I'm assuming here that the resolution of versions has already happened in that dependency resolution phase. So, like, any schema URL I see should be compatible in this part of the code.
That's why it's, like, short-circuited here.
There's a lot of complicated crap in here, that's just why I wanted to walk through it. As I'm talking through it, I need to go do better with docs and get rid of some of the vibe coded.
**Jeremy Blythe** 31:42 Giant.
**Josh Suereth** 31:42 Some of the coroner cases.
**Jeremy Blythe** 31:44 Yeah.
Okay.
**Josh Suereth** 31:46 What do you think, though? Like, generally.
**Jeremy Blythe** 31:49 Yeah, I actually need to look at… I think I want to go and look at the… proven… I didn't… I didn't get a chance, really, to look at the provenance stuff that…
**Josh Suereth** 31:59 Okay.
**Jeremy Blythe** 31:59 In great detail, like, I want to look at it with my own… Yes, I… I like to throw my company library and see how it works with it. That's always how I, like, I get a really… I get a good vibe from things if… well, if that works.
**Josh Suereth** 32:13 Please, please do that. That's out. I think… I think you should be able to just…
**Jeremy Blythe** 32:18 Yeah, that's already there. Well, and actually, we want to take that provenance information and have that in the, You know, in the UI, so you know where things came from, and stuff like that.
I mean.
**Josh Suereth** 32:32 Yeah, well, right.
Right now, basically, the way it works is there's a provenance field that has a dependent… optional dependency ref, or the path of its local.
If you have a dependency ref, it's just a, ID.
Into the dependency string, and then, the… is it registry?
No, it's not registry, it's the other thing. What do… it's under Mod.
**Jeremy Blythe** 32:56 I did look at the PR, I just didn't… I haven't, like, done it with.
**Josh Suereth** 32:59 Used it in anger, yeah. So this is the set of dependency schema URLs. But what I'm doing when I resolve attributes and stuff, this schema URL is implicitly added to every attribute in the registry, or every group here. If it doesn't have provenance, it tells it it's somewhere else.
So I have, like, a lookup, you know, if it has provenance saying it came from a dependency, use that schema UL, otherwise attach everything to the current one.
is… is… A lot of the logic.
It's amazing how annoyingly tedious that code is, by the way.
**Jeremy Blythe** 33:31 Hope doesn't have to be tedious anymore.
**Josh Suereth** 33:33 Well, I…
**Jeremy Blythe** 33:34 Order, sometimes.
**Josh Suereth** 33:35 Yeah, but then you have to review it.
**Jeremy Blythe** 33:37 Oh, you have to understand it, but…
**Josh Suereth** 33:39 Yeah. Anyway, but that's… so yeah, the provenance stuff was what made this next step work.
I have it split into phases. Like, would you want me to launch it in phases? So, phase one is actually, we just open up to allow multiple dependencies, and it only impacts that dependency resolve phase, where if you… well, it actually impacts attributes, too. But if we see attributes that have different schema URLs.
We err.
**Jeremy Blythe** 34:09 Yeah.
**Josh Suereth** 34:10 any difference.
And then the dependency resolve phase does the, you know, making sure that you have a unique name.
And on any conflict, it errors. So you can't use… you can't have a diamond if the versions are different. So that's why I want to skip to Part 2, because I think part one, if we launch it, is just awkward as shit, and not useful.
**Jeremy Blythe** 34:33 Are we plant… I mean… Planning on a release?
We are, but not yet.
**Josh Suereth** 34:39 We are, but not yet. Yeah, I think we just… didn't we just cut a release, or do we need… Oh, no, we should cut a release.
But I want to cut a release prior to this change, and then I want to cut a release after the change goes through.
**Jeremy Blythe** 34:54 Yes, I forget, but do we want the… Do we want the muscle stuff in the release?
**Josh Suereth** 35:04 You mean for Windows? We should probably pull that in. I think we can pull in what they did directly, because everything builds just fine. We have no errors.
**Jeremy Blythe** 35:14 Okay.
So we just need an issue to tidy.
**Josh Suereth** 35:19 I think the muscle fixes we want to do, we can do in the next release, yeah. Okay.
Yeah, if you're comfortable with that.
**Jeremy Blythe** 35:28 True.
If this, I mean, personally, I prefer phases, because I think the PRs get bigger and bigger these days.
And then it's just hardened, it's just so hard.
**Josh Suereth** 35:48 Yeah, that's fair. So, I'll, I think Phase 1 is actually ready for review.
So, I'll go mark that one ready for review, but I'd like to cut a release of Weaver prior to that going through.
**Jeremy Blythe** 36:03 Oh, before… before Phase 1 is merged? Do you want to do a release?
**Josh Suereth** 36:06 Well, I don't think Phase 1 is useful by itself. I think there's too many shortcomings.
Yeah…
**Jeremy Blythe** 36:14 Then we can have a few phases go in.
**Josh Suereth** 36:17 Yes.
**Jeremy Blythe** 36:18 Okay, that might…
**Josh Suereth** 36:18 We'd like to at least get to Phase 2.
Before we cut our next release. But if we can get all the way to Phase 3, then I think that actually, you know, ties everything in a nice bow.
**Jeremy Blythe** 36:31 Okay.
**Josh Suereth** 36:32 Cool. If you're amenable, I know you have to go, and we're already 6 minutes over, I'll kick off the release process, unless you want to. It should be just telling the GitHub agent to do it.
So we just need to merge the one PR, And then we can kick off the release process and go.
**Jeremy Blythe** 36:50 Okay, I'm a bit tied up today, but I'll look at the, I'll look at the, Slack if you need to… PR reviews.
**Josh Suereth** 37:01 We'll do, yep. So, I'll kick off the agent, I'll send you the ping, and thanks, Ben. Have a good day.
**Jeremy Blythe** 37:06 One thing I can… I just want to show you really quick.
**Josh Suereth** 37:08 Oh, yeah, yeah.
**Jeremy Blythe** 37:09 If you've got a second. I do.
**Josh Suereth** 37:12 You know, I have another 25 minutes here.
**Jeremy Blythe** 37:14 Yeah, I don't, but I still want to show you that. Yeah. Where's it gone? Here.
No, use this properly. Okay, Zoom. You should be able to see VS Code.
You can see via screen?
**Josh Suereth** 37:32 Yes, I see it now.
**Jeremy Blythe** 37:34 Okay, so this is what I'm doing for the multi-auth dependency stuff.
**Josh Suereth** 37:40 Okay.
**Jeremy Blythe** 37:40 So in the… so in the Weaver tunnel.
you get this auth section, and then what it does is, it goes by URL prefix, so… What I did was I… I used… a private regis… a private repo, just on… in my GitHub.
Where I've got this manifest.
But the URL prefix is just to… to there for me. And what I found from… other examples out there in the world is that you… you can have You can put the token in the file, which is not really recommended, because then it's in the file, or you put the environment variable you want to have for that prefix.
**Josh Suereth** 38:25 Yes.
**Jeremy Blythe** 38:26 somewhere else. Or, you actually have it run a command for you to go and get the token.
**Josh Suereth** 38:32 Yeah, I love this. This is great. Can I have multiple auth sections, then, for different.
**Jeremy Blythe** 38:37 Yeah, yeah, this is a list. So you have many or… you have many sections. Yeah. You have a URL prefix for all your multiple things.
**Josh Suereth** 38:45 Oh, I'm not familiar with Tamil, that's what the… that's what the double, double.
**Jeremy Blythe** 38:48 Oh yeah, the double means you go… you can go again, yeah.
**Josh Suereth** 38:52 That's cool, okay.
**Jeremy Blythe** 38:55 Then I can go again.
**Josh Suereth** 38:57 Yeah.
Yeah, this is exactly what I was looking for. This is awesome. This is even better. The token command thing's even better, man.
**Jeremy Blythe** 39:04 Yeah, so you can have the token, the command, or the environment variable.
**Josh Suereth** 39:07 Should we try to get this in this release? Like, how close is this to being submittable?
**Jeremy Blythe** 39:12 I have it working.
But only with live check, because live check's the only one where I've kind of wired it all in.
What I want to do… what I'm working on at the moment is lifting it up, so it's… so that when you just come into Weaver for any command… It loads… it loads all of this stuff in, including the entire configuration, and then it calls into whatever command, because we want this in everything, right?
So I'm just doing that thing, I have to lift it up, but then every time you do that, I'm like, this PR is now getting huge.
And I just said, oh, we should do a smaller PR.
But… But…
**Josh Suereth** 39:45 I think you could… you could theoretically just do the… Oh, no. Maybe do the lift up first, and then do auth as separate PRs.
Is that…
**Jeremy Blythe** 39:56 Is that normal?
**Josh Suereth** 39:57 No? Okay, nevermind.
**Jeremy Blythe** 39:59 already in the…
**Josh Suereth** 40:00 Yeah.
Okay.
**Jeremy Blythe** 40:02 Because I do that that way around, so I don't really… Anyway, I just thought I'd show you, because this…
**Josh Suereth** 40:06 This is great, that's awesome. Yeah.
**Jeremy Blythe** 40:14 I've only tried it with Git.
like, artifact download stuff. And of course, I've got the other code in there that… If it detects that it's a Git URL that you've copied from the browser.
it then does the redirect and follows to get there, because that's not actually the URL where the file is. It has to go and turn that browser URL following the redirect into an API URL.
But of course, you don't have that, you just go, I want that one, click, copy-paste.
**Josh Suereth** 40:42 Yep.
**Jeremy Blythe** 40:42 So all of that code is in there as well, so that's, like, a special case, but anyway. I just wanted to show you.
**Josh Suereth** 40:48 Yeah, yeah, this is… this is really cool. I… this… that's exactly what I was hoping we'd build eventually, and it… it… it looks just like how Cargo does it.
So I think that's a good.
**Jeremy Blythe** 40:57 Funny or not, isn't it?
**Josh Suereth** 41:02 Alright, man.
**Jeremy Blythe** 41:02 Cargo did something like that, and was, I think you pointed out it was… there's something.
**Josh Suereth** 41:07 Maven.
Yeah, yeah. I think… I think most, like, NPM probably has something like it as well. Probably PyPy, like, all… I'm guessing… not PyPy, what do they call it? The… what's the requirements.txt for Python thing?
Where you download crap. It's like, crap. Venv, or whatever the thing that downloads Python requirements has a thing where you can specify different crap, like, I think they all…
**Jeremy Blythe** 41:34 Hi. I… I…
**Josh Suereth** 41:38 End, maybe? P-End? Yeah.
I did… yeah. Managing and working with, like, OpenTelemetry SDK deployments for all possible languages, you learn a little bit about packaging for everything.
**Jeremy Blythe** 41:56 Yeah. Cool. Alright, I'm over, so… Yep. Well, that looks good. Alright, I'll take a look at that, and then… Yeah, if you need some… Pushes to get the release done, then.
**Josh Suereth** 42:06 Yeah, and you have no problems merging the Windows SSL thing as is, do you?
**Jeremy Blythe** 42:11 No, does that need another… no.
**Josh Suereth** 42:13 No, no, no.
**Jeremy Blythe** 42:14 I mean, I…
**Josh Suereth** 42:14 I can merge it, yeah.
**Jeremy Blythe** 42:16 Yeah, let's do it.
**Josh Suereth** 42:17 Okay, awesome. I'll see you, man. Thanks.
**Jeremy Blythe** 42:19 Bye-bye.
