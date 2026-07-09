SIG: Semantic Convention Tooling
Date: 2026-07-08
Duration: 55 minutes
============================================================

## Zoom Recording Transcript

**Josh Suereth** 00:07 Hey!
**Joao G. (Dynatrace)** 00:15 Hello?
**Josh Suereth** 00:17 How's it going?
**Joao G. (Dynatrace)** 00:19 I'm good. How are.
**Josh Suereth** 00:22 Not bad, not bad. Busy.
**Joao G. (Dynatrace)** 00:24 Going, good, okay.
**Josh Suereth** 00:27 Yeah, okay.
**Joao G. (Dynatrace)** 00:29 Nice.
**Josh Suereth** 00:34 It's been, like, summertime is always interesting in OpenTelemetry, because we, Joao G. (Dynatrace) 00:40 Mmhm.
**Josh Suereth** 00:41 You know.
All the meetings are, like, half attended.
**Joao G. (Dynatrace)** 00:46 Yeah, that's true. Yeah.
Yes.
I guess it's a… A pattern everywhere, right?
**Josh Suereth** 00:56 Yep.
**Joao G. (Dynatrace)** 00:57 A lot of people go, go, go, go away during this time.
**Josh Suereth** 01:06 Yes.
Okay.
**Joao G. (Dynatrace)** 01:13 Can't complain, especially when it's so hot outside.
**Josh Suereth** 01:16 Oh man, it's been crazy too, right?
**Joao G. (Dynatrace)** 01:19 Yeah. We're okay here now. It's, it's, it's, it's chilled, but it was, it was a rough couple of.
days last last weeks. It's it's tough.
Hmmm.
**Josh Suereth** 01:34 Yeah.
**Joao G. (Dynatrace)** 01:37 Oh well.
**Josh Suereth** 01:37 Oh, man. Oh, Jeremy's here.
Let me, I need to push a change, but I haven't had a chance to review.
all the ugliness or fix it. Okay.
So, I have two things. One is, we broke all our tests for me.
There was a change that was made where, it was the… all the flexibilities for, like, the if-when stuff that Lamilla added, to the test suite.
You know how in Weaver we have all the, observed output directories? All those tests reuse the exact same observed output directories, but don't have any sort of, concurrency primitive to prevent them from being run simultaneously?
And so, it consistently fails on my machine because of how much concurrency I throw at Rust, but it didn't fail in our, In, in, in our Docker thing.
**Joao G. (Dynatrace)** 02:47 So…
**Josh Suereth** 02:48 I don't… like, do we want to do something about this? It… I think we should have a principle where we don't reuse The test directories between different unit tests, because unit tests can run in parallel.
But I'm not… not sure what to do there, yeah.
**Jeremy Blythe** 03:09 Yeah, I think I was tempted to make I think when I was doing some live check things, I was tempted to go like.
Yeah, if I just do these in series, then I get rid of all of these problems of, like, poor overlaps and stuff.
But then.
No, I'm not. No, I'm doing it in series. So I think we should.
The principle should be that tests should be able to run in parallel. Yeah.
**Josh Suereth** 03:40 Yeah, okay.
So then that gets into, Do we… is there a thing we think we can do to solve this kind of generically or not? I don't know. For the port thing, you saw the crazy-ass thing that I had.
an agent make for me, because I didn't feel like thinking about it.
**Jeremy Blythe** 04:01 Did that go in, in the end? I can't remember.
**Josh Suereth** 04:03 I think it did. I think it did. I cleaned it up a good bit.
**Jeremy Blythe** 04:07 I think that's something like the fourth attempt.
**Josh Suereth** 04:12 Yes.
Yeah, with, like, file locks?
But I… part of the problem is we're running… Like, if we had a, integration test.
You know what I mean? Where we could isolate an environment.
If we had a hermetic environment that we could spin up.
In parallel.
That would be good.
**Jeremy Blythe** 04:35 Yeah, me too.
**Josh Suereth** 04:36 The other option is, what we did there, which is we literally lock a file.
There's, like, anytime you want to reserve a port, you call the helper method, and it checks the file lock to see if you can get access to a port so that you don't have conflicts.
In this case, it was, Anytime you want to write to an observed output directory, don't just copy and paste a previous test and use the exact same observed output directory. What I did was I changed the method where you have to send in a string of your test name.
And, just made sure everyone uses a different string, and now all the observed output directories don't conflict.
I can show you that if you want to see it.
but… Okay, anything we want to do specifically?
or key point fixing.
I think another thing we could think about doing… are we able to get more parallelization in GitHub Actions so that we catch the failure in GitHub instead of only on Our machines that have parallelization.
**Jeremy Blythe** 06:11 How are you getting more?
like.
We've got it runs cargo next test.
That's the same thing that runs in.
the Github action.
**Josh Suereth** 06:27 No, no, no.
**Jeremy Blythe** 06:28 Tuning you've got to.
**Josh Suereth** 06:29 This was a.
**Jeremy Blythe** 06:30 Different about cause or something.
**Josh Suereth** 06:32 I mean, I do have it set to use all my cores,
**Jeremy Blythe** 06:36 And then have you got like a giant machine or something?
**Josh Suereth** 06:41 It's a VM from Google that I just run everything on.
So it's not even my, like, my laptop, I'm running it somewhere else, so I can use all the cores and I don't care. Doesn'.
**Jeremy Blythe** 06:54 Maybe that's something to do with it.
**Josh Suereth** 06:58 No, no, no. I could consistently reproduce this. I can show you what the fix is here. Let me… So, basically, this was in Forge.
Oh, this one, this one, this one's even better.
It… it was actually the order of the test suite determines whether or not you got a failure.
So if you… if you did cargo clean, it would always pass, and then the second time you ran it, it would fail.
That's why we never caught it in GitHub. But the fix is in Weaver Forge, we say prepare tests where this creates all the directories and crap.
For where you're gonna output data and all that kind of stuff. So this is where it makes observed output. So what we're doing here is instead of, we have expected output, we have observed output, and we're putting observed output into a different directory than target, because we were actually reusing The… if I scroll up.
We're reusing the templates With different expected outputs.
**Jeremy Blythe** 08:17 Are you using tempdas for this?
**Josh Suereth** 08:19 Why are we doing what?
**Jeremy Blythe** 08:21 Why are we not using temp, tempda?
for this.
Why does it have to be in a fixed location at all?
**Josh Suereth** 08:27 Because when it fails, the most common thing you do is copy from observed output to… Target output, and that's what fixes the test, because you made a change, you look at the diff that fails, you say, hey, that diff looks good, let me copy it from A to B.
If you put it in temp directory, you can' That's how all, like, literally, that's how all our resolution tests work, that's how all of our forge test This… I think the problem was, and I… Ludmilla's here, so I don't want to throw her under the bus, but basically, we created a brand new set of tests.
where, before… like, test SEMCONF JQ functions, right? We only ran it once.
Now we, like, have a thing that tests, this one's fine, that one's fine.
Those… those is just… my agent was over a year, I can clean that up, basically. The tests that were added that duplicate things were… Test, evaluate, win.
So test evaluate when, basically, is using the test setup But with a different set of, like, expectations, basically, for when templates. And, this is the thing that was causing everything to fail, because the observed output directory would conflict for test evaluate when and test evaluate.
So, you could not run those two functions in parallel. But for some reason, the way it runs in GitHub, when you clean, it runs one and then the other, and everything's gravy. But if you run them in the opposite order, which is what happened when it wasn't clean.
everything would fail.
Because it was, like, abusing the same output directory.
I think the other thing that would happen is, effectively, the observed output directory gets deleted, Right here.
And so, what would happen if you run in parallel, there's a race condition, where if one test runs and finishes before the next test runs, everything's gravy, but if they run in parallel, one test will delete the other test's output.
While it's running.
**Liudmila Molkova** 10:41 I'm sorry.
**Josh Suereth** 10:42 It was fine.
**Liudmila Molkova** 10:43 An investigation, I'm sure.
**Josh Suereth** 10:45 I had an agent do it, I didn't… I just looked at what it reported. I can fix this up, but that's why I wanted to ask, like, what the agent did was really ugly, and I, like, literally the only thing that has to happen is in prepared tests.
Not prepared tests. In, test, evaluate, win.
Right? We just… we want to reuse the initial test setup but have a different, execution environment for where expected output goes, so that this works correctly. The other option is… we could have test-evaluate-win have a different input directory completely, so it's completely disjoint. Like, that would also fix it, instead of doing this ugliness. But what I really wanted was, this, this setup directory, I wanted output name to default to target name, but if specified, it will be different, and then inside of here, when we call prepare test for test generate or test evaluate win, we just give it a different thing so that the names don't conflict, and then everything's gravy.
**Liudmila Molkova** 11:54 That's, that's… Yeah, it makes sense.
**Josh Suereth** 11:56 Good.
**Liudmila Molkova** 11:58 It it seems like a great fix there is a.
In other languages that are more friendly to reflection and stuff. There is usually some test info that you can get.
And it contains the test name, so that, like.
Somebody can copy it over, right, and not change it, and we need to catch it during review or something.
But maybe there is some way to just automate it and know what the name of the test you are running is.
**Josh Suereth** 12:27 We can do that. I think, like, really, the issue here is that prepared tests was not meant to be reused between two different tests. It only works for one.
Because of how it works. Like, it's… it's not… it was not designed so multiple unit tests can call it With the same name.
Which is what this.
**Liudmila Molkova** 12:48 Yeah, and it still is not designed if the strings are the same. What I'm saying that it's cool, it's fun, let's do this, but can we not… Copy paste the… Strings, can we have it?
**Josh Suereth** 13:05 Okay.
**Liudmila Molkova** 13:05 isolated in runtime.
**Joao G. (Dynatrace)** 13:07 Mmhm.
**Josh Suereth** 13:08 Yes, but again, like.
This here? Yeah, I could probably do that. That's a simple macro, I think.
**Liudmila Molkova** 13:17 Okay, so instead of the runtime reflection, Rust has compiled the macros.
**Josh Suereth** 13:23 Yes. I can look at that. We'll probably do this initially, but I guess my point being, though.
we probably need to find a way for these tests, these prepare test things, to basically call out… I might document them all, like, you cannot reuse the same Target in multiple tests, because we actually rely on this directory to, like, exist and be, you know, be idempotent. Like, only one unit test can own that directory at a time, and so if you reuse the same string across two unit tests, everything is broken.
That, I think, was not clear.
And I think I'll just add some comments about that as well. So, maybe I keep this fixed, maybe I default it, maybe I get a macro in, but I had a comment to these things to make sure that, when people read the code, they know what is safe to do and what is not safe to do for these Methods, because I think that's what led to the breakage.
Okay, it is.
**Joao G. (Dynatrace)** 14:24 Could we just create a temp directory with a, you know, like a UID for the thing? And because it is the only problem that, you know, we use the… The final thing to copy paste to fix the test.
Or is there any other thing that you would, you know, like, you would want to look at the output?
**Josh Suereth** 14:43 So the reality is, I think actually the thing that we should fix is this test evaluate when doesn't need the observed output at all.
**Joao G. (Dynatrace)** 14:53 Mmhm.
**Josh Suereth** 14:54 I don't think it uses it, does it?
Yeah, like, it's not even interacting with the observed output, it's actually just doing something completely different. It just, it just needs the test data. That's it. So, like, it's calling this helper method, where the helper method's designed so I can copy from observed output. Here, let me show you.
where we have crates.
we were forged… I'll show you the intention of these unit tests, and then what that test is actually doing, and I think we can just fix that test.
Overloaded templates test expected data. Okay. So we have these data registries, right? This data registry is what we run all of our tests based on. It's like all the YAML files that we will render and forge under expected output, we have this.
you know, each individual test is supposed to be named. So, under Whitespace Control.
There's a registry MD that is generated from the test.
Okay.
If I… So that's our expected output for whitespace control. I believe that, where's data?
Registry. Yeah, that's the registry. Where's the templates? Min Here, templates. Whitespace control exists here, and the test picks up whitespace control, right? Which is this Weaver YAML, and then… this registry. And so expected output is what we expect this to generate when fed through the template that we refer to works. And then in your target directory, you get a diff. So if.
**Joao G. (Dynatrace)** 16:37 Okay.
**Josh Suereth** 16:37 If the thing that's generated looks different, I get a diff that says, you know, things just changed here. Here's the diff. If I'm not happy, I copy paste from the known location to the other thing. If it's in a temp directory, that directory can actually get deleted before we even have a chance to copy paste over, which is why we want to put it in a known location.
But the issue here is, like, I guess maybe a simpler fix I can do. I was trying to make it so we can reuse these things going forward. A simpler fix, I think this is… is it in Lib? Was that where it was? To… Let me see, it's like underscore Evaluate, test, evaluate, win, right?
Yeah, the issue here is this is reusing this prepare tests, which expects you to be doing observed output stuff.
But it's only using prepared tests to get an engine in a registry, and it's ignoring the observed output to do diffs.
**Joao G. (Dynatrace)** 17:32 I see, I see.
**Josh Suereth** 17:33 So, actually, what I should do, and I can, I can go fix this, is I can change prepare tests, where we can just say, we can make a prepare test no diff.
That gives you an engine and registry where you don't touch observed output at all in any way, and that's probably what we'll do here.
**Joao G. (Dynatrace)** 17:48 But we still might run into the concurrency problem because we still reuse the thing, right?
**Josh Suereth** 17:54 Right, which I think what I'll do for that, because I think this will help agents not make mistakes so that we notice it, is I'll comment on prepared tests. This is not safe to use with the same name between multiple tests. This gets into another thing.
**Joao G. (Dynatrace)** 18:10 Yeah, next.
**Josh Suereth** 18:11 Yeah, go ahead.
**Joao G. (Dynatrace)** 18:12 No, no, I think that's fine. Or we could also do the same thing, and then the diff, you can just log, because then you don't need to… You don't need to cop from a file. That's like, what I don't know, like, what is the Java unit thing, whatever it does, like, if there's diffs or something, it just logs the diff, and it just cops from the log instead of from.
**Josh Suereth** 18:31 The problem there is these diffs get too large to copy.
**Joao G. (Dynatrace)** 18:34 Yeah, yeah, that's what I was thinking, yeah.
**Josh Suereth** 18:37 Like, we… I tried that, Joao G. (Dynatrace) 18:39 Yeah, yeah.
**Josh Suereth** 18:40 It was… In fact, sometimes the diff is so long, you literally can't see it.
Even in our log file, so you have to go, yeah. Anyway.
**Joao G. (Dynatrace)** 18:49 Alright, that sounds good.
**Josh Suereth** 18:50 Okay, so AI.
I'll make a separate PR for that, Let's see… fix up tests so that we don't split.
orange open method.
One.
is not.
Reentrants.
Okay.
Just one second.
Okay.
Not reentrant, what's the word I'm looking which is not.
Let's see for parallel.
**Joao G. (Dynatrace)** 19:32 I doubt it, I doubt it or something.
**Josh Suereth** 19:36 Yeah, yeah. Okay.
Alright, wanna do a quick update on, since I'm here… the dependency resolution stuff. So, I created a new branch.
And I started, I made a design and asked an agent to implement it.
And I'll show you what it looks like now, because I want to fix this up a bit. But… This fixes the… Dependency hell.
Problem with semantic conventions.
So, if you're not familiar, we have this, is it the Resolve Conflict Test?
No, that is… I think this is the one.
No, that's an invalid version. Get rid of you.
get rid of you.
Compatible version, we don't want you. Diamond, I think this is, this is it, the diamond resolved.
Diamond conflict, yeah, okay, so what we have here is we have a, Registry A, Depends on version 1.1 of C.
Registry B, Depends on version 1.2 of C.
Okay.
The main registry… Depends on A and B.
And what we want to see out of this.
All the tests are somewhere else. What we want to see out of this, between these two things, is, if we look at 1.1 and 1.2, we have attribute from 1.1, group from 1.1, and we have, attribute from 1.2 and group from 1.2. What we want to see is, in this case.
Because they're both compatible major versions, that we always get 1.2.
in the final registry. So we do a version conflict resolution that says, okay, I see 1.1, I see 1.2, instead of erroring, which is what happens today, it'll say, no, actually these are the same major version, I'll just pick the 1.2 data.
For that hierarchy.
That's the goal of this.
What it does is rather exciting.
I think this is where it is. It's split across a few files, so… that's matches explicitly. Yeah, where do I? Where's the cash? Look up.
And that's okay.
Create schema cache lookup, I think, oh, it's in lib, is where I put it What I have is, Chosen version is after we do dependency resolution, so at the start of resolution, we pick versions for every main schema URL to say, this is the version we're going to use when we need it.
And then now there's a cache lookup that uses that lookup, or the cache that we had before.
This is for… yeah, I gotta get rid of this. I was gonna use this for testing, but it turned out I didn't need it… yet. Anyway, we have a lookup schema.
which can say, okay, given a particular schema URL, go give me the resolved schema, that is in our cache. If you remember, we built that out, that was, like, the last PR I sent, that was, like, the foundation for this. So, when we do schema resolution in, Weaver, we can now basically say, hey, here's a schema URL, go give me the resolved schema. If it's in the cache, it gives it to you. If it's not in the cache, it goes and res Okay? That's one thing we wanted to do for, live check, et cetera, et cetera. I'm using it here.
So the idea is, with these two things, effectively, what I'm doing is, when I look up dependencies now.
And I see a schema URL as a dependency.
I will actually say, okay, give me the actual chosen version.
and then give me the data from the chosen version. And I have all kinds of weird shenanigans to make that work right now. It's a little bit gunky. So when you read through it.
that's effectively what's happening, but this is… this is the big piece that, like, makes it work. If you want to see what we're actually doing, we just have, a chosen versions hash, which is defined when we do dependency resolution. So when we walk the dependency chain, we'll pick a version for everything.
And then this LRU cache is the one that we, built out previously.
And so, I just throw them both in here, and then I updated the whole dependency resolution algorithm to, use these. There's a few other helper methods of, like, if you have a bunch of schema URLs and you want to, like, figure out what the chosen URL is, this figures out whether or not to insert it into chosen or keep the previous. This is literally the dependency resolution logic.
Okay? So, if the current version's greater than the previous version, we put the current version in there. And then when we actually do conflict resolution on dependencies, there's another dependency resolution thing that says, okay, as long as the versions are compatible major versions, everything's gravy.
alright.
that's… that's basically the gist of this. I need to do a little bit of cleanup on here. Wanted to get some early feedback on that, like, overall design Though, I think the.
**Liudmila Molkova** 25:33 This is awesome!
**Josh Suereth** 25:35 Okay.
it was a pain in the ass, but yeah, thank you. Oh, here's… here's an example where we use the schema lookup cache, right? So, if we're looking for a particular crate as a dependency when we're resolving an import, Right, we figure out our chosen URL, and here is where we look at the major version.
Before we decide, you know, what to do.
Okay, anyway.
Feedback.
**Liudmila Molkova** 26:06 You mentioned something.
Hockey or some complications. I didn't see them yet.
**Josh Suereth** 26:14 So…
**Liudmila Molkova** 26:15 Larissa first.
**Josh Suereth** 26:16 It's it's right here.
The implementation of this thing, I'm not gonna walk into until I have a chance to clean it up, but effectively, we have shenanigans where, we will load the dependency the way we did before, where everything's resolved and we have, like, you know, imported groups in the sub-registry. But if we get an imported group that is the wrong version.
First, we just look for conflicts and resolve them, but if we get one that's the wrong version and not what we need, we actually go re-resolve the dependency, like, the downstream dependency. We figure out what it's supposed to be and just kind of slam it in there.
There's a set of things I'm concerned about with that, of, like.
In CEMCOM, this isn't an issue, because when we deprecate things, we don't But if 1.1 to 1.2 removes a deprecated item, and the deprecated item is the thing you referenced.
right now, I think I crash with an… like, I give you an error, and say, yeah, you did something horrible, you can't have this dependency. Sorry. Like, I literally cannot resolve the fact that I need deprecated 1.1, and it doesn't exist in 1.2, because I can only give you 1.2.
So, I'm not happy with that, but it's also esoteric. Like, it will hit us in practice, we do have to clean that up.
and I still need to.
**Liudmila Molkova** 27:42 No.
**Josh Suereth** 27:43 To make this code more readable by humans.
So that's the other thing I'm trying to work on. But the overall idea is working out as a way for us to kind of go through things early.
**Liudmila Molkova** 28:00 Yeah. We we cannot really do anything about this. We don't have to crash. Right? We can just say it's it's impossible, but it's their message.
**Josh Suereth** 28:10 Well, yeah, when I say crash, I mean I return an error.
Like, it stops resolution at that point, error gets returned.
And you get an error that says, hey, this is an unresolvable problem.
Yes.
Don't depend on this.
Okay.
Okay.
Other things that I'm a bit nervous about, we… you know, originally I was talking about trying to change all imports to actually always be pointers?
So instead of actually recording the group fully.
that we would have a pointer to the, that says import, like, instead of having a full group in our resolve schema, resolve schema would have a pointer that says, I'm importing group X from this dependency.
Because then, that would actually make this thing more consistent. I did not do that because I would need to break resolved schema format to make that happen.
And it would make Forge much more complicated.
I can still make that change, but it's actually, like, incre… This is somewhat hacky to make this work, but it's working.
that would actually break resolved schema format, and I'm a bit nervous to do that right before we want to stabilize.
**Liudmila Molkova** 29:31 resolved schema V2 format.
**Josh Suereth** 29:34 Yes.
**Liudmila Molkova** 29:35 I mean, nobody we know uses it.
**Josh Suereth** 29:39 Right.
Right. It would make… it would also make Forge awkward.
**Liudmila Molkova** 29:45 Yeah, that's the…
**Josh Suereth** 29:46 That's more than…
**Liudmila Molkova** 29:47 For me, it's a bigger problem.
**Josh Suereth** 29:49 I… like I was saying, it will take me a long time to get that all working, so I don't just break you 100% if you're using V2, whereas this, I know, doesn't break you right now.
And so I'm not sure which direction to go.
**Liudmila Molkova** 30:03 How would, like, imagine we'd do it one day.
How would it break resolved schema?
**Josh Suereth** 30:11 Right now, Resolve Schema, you have, like.
at least the branch that I threw away, or I still have it, but, you know, it's ugly as shit. You have… Resolve Schema has the schema that you are currently looking at, with all the things there.
and then it has the import list of what you need to import, and that is, like, I'm importing this group from this dependency, this group from this dependency. Then it has a dependencies block, which is the full Forge schema for the dependencies that you've imported.
**Liudmila Molkova** 30:48 Oh.
**Josh Suereth** 30:49 It's… it's giant.
This does…
**Liudmila Molkova** 30:53 Would need it.
**Josh Suereth** 30:54 I think we needed, anyway, the giant block, but what it… the problem is you can't just go in and say, give me all my groups, and get the imported ones. You actually have to look at them completely separately.
how I have it now for Ford Schema. I have to do a lot more work, and then I can get them actually embedded in the Ford schema with the appropriate, you know, annotations and all that.
**Liudmila Molkova** 31:19 Oh, it's for the forge schema, we need to…
**Josh Suereth** 31:22 schema, yeah.
**Liudmila Molkova** 31:23 Yeah, and for the result schema.
We just need to change what we show there.
**Josh Suereth** 31:31 For resolve schema, it would change the signature, but the main problem with resolve schema, though, is I no longer import the actual Group definitions in that world.
**Liudmila Molkova** 31:44 They disappear from… Wherever they were, and they would appear as imprints.
**Josh Suereth** 31:55 Mmhm So, I… I don't know if I actually want to go that deep, I guess is what I'm saying. Like, what we're doing here, in the PR I have, is… it's acting like that's true, but I'm not actually changing things. So resolve schema, you can… if you get a resolve schema independently.
You see all the imports, and you know exactly what they were at the time we resolved it.
But if I depend on resolve schema.
I can ignore those imports.
and go deeper, which is what the resolution algorithm does. So, I kind of like that better, but I was curious it's different than what we talked about, what, like a month or two ago? I forgot how long we were talking about this. But, it's different than what we originally discussed, so I just wanted to run that by everybody.
**Liudmila Molkova** 32:56 I, I'm, I'm fine either way. I just don't understand the problem well enough.
It seems… You're comfortable with it, and yeah, let's go with it.
**Josh Suereth** 33:06 All right, I… the the main thing that we have to. Yeah, yeah. So so let's say, to do discussion.
It's all good.
The main thing would be, if I made that change, would we change anything about resolve schema? I'm at the point now where I think I'm comfortable not changing the resolve schema format at all, and I would prefer that personally, because I think we have enough in there It looks like we have enough flexibility to solve this issue, and… our code might look a little gross, I'll work on cleaning it up a bit more, but I… I think we can do what we need here.
And, yeah, I don't want to make drastic changes, at this point in the game on V2.
I am going to make that dependency change, that is coming, but I think I can do it in a way that doesn't break anything, because if I keep Resolve Schema the way it is, the only thing I'm adding would be… it's completely additive, like, Forge Schema will get a dependency section. There's nothing changes in regular forest schema, so all of our stuff works today, continues to work, the whole ecosystem doesn't break, we just add the dependency section, and then people can start leveraging it from there. So, I like this better going forward.
**Liudmila Molkova** 34:29 Awesome.
**Josh Suereth** 34:30 Cool.
Yeah, and by the way, Jeremy, if you want to look up schema by schema URL, it works!
You can start prototyping with it for live check if you want, dynamically looking up schemas and Figuring out what the hell you want to do with it.
**Jeremy Blythe** 34:45 Yeah, I actually want to figure out, if I can… Include… Some… Somehow include information about.
When the when you get the report out of life check about what's been checked.
if I can include in that report something that is then pointing at the schema URL, where that is the match to the thing that LiveCheck matched it with, if that makes sense. So, like, I could be further down the dependency Yes?
Than just the registry that was loaded.
And that might be really handy.
when you're looking at the results.
I'm not explaining this very well.
I've been playing with a way of… visualizing the output of a live check, like, in the… in the web UI.
So that you can kind of explore the outcome of a live check session, or… Or maybe even live, live, live check as it's happening.
So that you can kind of go in and go, like.
Because one of the nice things is, like, it's matched with something, you want to click on it and go like, oh, what is that? Where did that come from? What's the… where was that in my dependency?
stuff. So I think this… So yes, I do definitely want to dig into it. So I think there's like, there's also a flip side to it.
**Josh Suereth** 36:20 Yeah, I was suggesting the, the other side, which is, like, if I get… if I get an OTLP, you know, message, and it has a schema URL, and that's not the one I loaded, you can go load it.
**Jeremy Blythe** 36:35 Yeah, yeah, okay.
**Josh Suereth** 36:35 Yeah, thank you.
**Jeremy Blythe** 36:37 I'm.
**Josh Suereth** 36:38 Okay.
**Jeremy Blythe** 36:39 But you kind of want to know that that's happened in your life check results.
**Josh Suereth** 36:43 Yeah, which is cool. I like, I like that. Yeah.
by the way, I really like the UI, edition you had with all the stats, that's…
**Jeremy Blythe** 36:52 Okay.
**Josh Suereth** 36:52 Makes it feel like it was worth making those changes.
Anyway.
**Jeremy Blythe** 36:59 It's fun. That was just fun.
**Josh Suereth** 37:02 Cool. Should we move on to Yao's topic? Because I think that's enough for me to finish up that PR and get that out of draft mode. And that, again, was my… When this is done, I think I'm ready with… Schema features.
Right? Then I think it's just we fix all the bugs that we have from CENCOM.
Okay.
Cool.
Alright.
Take it. Take it away.
**Joao G. (Dynatrace)** 37:37 Yeah, so, as I said, there… Mondays are a bit tough for me to join, so this one is easier, so I'm just trying to catch up on the… V2 things, I saw that the two folks there start to change a lot of stuff, and a lot of confusing things, so I'm just… because I looked it up some time ago, and it looked straightforward-ish.
to do the migration, like, in two steps, we would migrate the… Templates and all the scripts and stuff. And the model shouldn't change because it should work, right? More or less.
And then we could slowly migrate the things.
But I don't get with the problems that they are coming.
coming coming with now all this.
Yah.
**Liudmila Molkova** 38:27 I think they are going down the path of migrating definitions first, and it probably can work, and I don't understand the problems that come up there. But the path of, okay, let's do definitions v2.
In the schema.
and then keep all the commands on v one because, like, the the output should change.
like, this process of V2 to V1 is probably lossy, and it's not, like, worth it, because we need to change templates to accommodate, like, this quirks of V2 to V1, and then we need to change them again to actually migrate to V2.
**Joao G. (Dynatrace)** 39:05 Exactly, so that was the part that was confused, because… yeah, because I saw some stuff is gone, like the brief thing, because of the way the structure works, but I think that's… Yeah, I know.
We just have to live with it, I guess.
**Josh Suereth** 39:20 The other thing is, we synthesize group IDs, and they look really gross. Like, we don't want to change all our templates to work off of… like, V2 embedded in V1 output is horrible. It looks gross, and that's… We didn't bother with that, because we assumed people would upgrade to V2 output, then upgrade to V2 input, right? Like, that's kind of how we expected it to go.
**Joao G. (Dynatrace)** 39:43 Yeah, okay, so… so I was… I was not so far, because that's what I also thought about the… the process would be.
Oh.
But then I saw, like, the huge, I don't know, PR, so many files, and I didn't have, like.
I was like, I started looking, it was like, this is too much, I don't think this is, like, I don't know.
It looks really strange, but I didn't want to bother reviewing all of that, so, okay.
**Josh Suereth** 40:10 Yeah, we're gonna deal with the giant PR no matter what, but… Joao G. (Dynatrace) 40:14 Yeah, that's fine, yeah.
**Josh Suereth** 40:16 Let's keep it limited. I think Ludmilla, the plan you walked through, and I think it was SemConf this week, right, of like.
**Liudmila Molkova** 40:24 Yes.
**Josh Suereth** 40:24 let's go through all the outputs one at a time and move them to V2, and then, yeah, it's gonna be a big change, but we can go through them one at a time, and it'll be, like… I think it's gonna be less overall.
Giant CLs.
But there will be a giant… when we do templates, That's gonna be everything, right?
**Liudmila Molkova** 40:44 Yeah, yeah, yeah.
**Joao G. (Dynatrace)** 40:45 But I mean, they are automated, right? So you know that the change is the same. So if you see one file and it looks fine, then you know that all the others are the same because it's just mechanical, right? It's all good.
What I was, what I was confused is that the, the, like this addition of public groups and, and like the thing that Thompson, Thompson was mentioning.
Oh.
**Josh Suereth** 41:10 James, there's a set of features he wants to add into V2 that we did not add.
But because, like, he was really focused on trying to get, everything automated 100%, so he wanted, like, this notion of, like, a namespace that you would define that would have briefs and things, and then all of our docs would be auto-generated, because all the markdown moves into YAML.
That's not there, and I don't know if he's trying to do that right now with his PR, but I wouldn't be surprised if he was trying to continue down that path without the feature support for it.
So, I… that would… that would make me a little bit nervous, but, like, we, Right now, the group… the group mindset in V1, where everything was a group, we, like, flattened it out, and so you don't have to be part of a group to define attributes.
Which means you don't have briefs and namespace on attributes.
**Joao G. (Dynatrace)** 42:04 Which…
**Josh Suereth** 42:05 It does change some things, but I don't remember what you did, Lyudmila, but like most of those.
most of those names weren't, like, super meaningful, and we're kind of trying to line against signals now. And so signals, you can have briefs and descriptions and attributes. So we're trying to provide less on people thinking about attributes, and more on people thinking about signals.
And I think that's, like, an explicit, like.
we might make changes to the template. The demo Lyudmila gave, I don't know if you want to do that now.
I really liked what you had on Monday, so maybe it's worth… have you seen this, Joe?
**Joao G. (Dynatrace)** 42:43 No, no, no, I wasn't at the meeting on Monday, unfortunately.
I saw only the ticket plan, like, the updated plan on the, let's say, Epic ticket.
Yep.
That's about it.
**Liudmila Molkova** 42:57 Yeah, so I think the tricky part, I'm opening the demo, the tricky part is R.
Some attri- some groups that are attributed groups that carry some meaning, like exception.
That we decided that we want.
What we miss currently is requirement levels on those.
And I'll add them to Weaver for public groups only.
And we will declare some of the groups public.
And there are other tricky places, that we will need to decide what to do. For example, for example, cloud events, right, where where this is the attribute group, but it's also a span. It's it's in Markdown, it says it's a span.
In YAML, it's an attribute group, and neither is completely right, but the truth is somewhere in the middle.
So we'll need.
**Joao G. (Dynatrace)** 43:59 But for donke.
**Liudmila Molkova** 43:59 Right, right.
**Joao G. (Dynatrace)** 44:00 Right, like with having the attributes and then use the signal like.
**Liudmila Molkova** 44:05 Yeah, if we don't want to go into like.
All this messaging discussions and merging and blending spans together, we probably would do some half ass job with it and call it a day. We will, I don't know, create an issue to follow up. Maybe we already have an issue to follow up, but we will do something reasonable but not complete.
So, like, there are… this part is a little bit involved.
Okay, I'm going to… Share.
So this is the proposal that we… we don't have to adopt right away, but we can adopt Just a little bit later.
You see my screen, right?
**Joao G. (Dynatrace)** 45:02 Mmhm.
**Liudmila Molkova** 45:03 You see the the geosematic conventions. Genii.
**Joao G. (Dynatrace)** 45:08 Yes.
**Liudmila Molkova** 45:09 Okay.
Oh.
So what I'm thinking about.
After we just finished the migration.
Oh dear, look at it.
Oh.
Okay, so… maybe we can render stuff a little bit differently. We can render… if we render registries, we can do this. So, instead of, like, having registry of attributes, registry of metrics and spans.
We can have a registry of namespaces.
And in each of these namespaces, you could have a readme file that's a list of things that are defined in this namespace, all the signals.
And on the bottom, we can have all the attributes, even if this file gets very long, this is just the reference documentation, it's fine.
And.
And we probably should generate table of contents here for an easier navigation. And then these are the signals the registry of signals. You can decide if you want it.
So in semantic conventions, we don't have it, and if we do, we'll have some duplication. Maybe initially we don't, and at some point we will switch or we'll figure it out.
**I… Joao G. (Dynatrace)** 46:32 But today it's already, the register is already like structured like this, no? With namespaces.
**Liudmila Molkova** 46:39 No, the registry is… Joao G. (Dynatrace) 46:43 Or, I mean, it's the areas that they match.
More than one.
**Liudmila Molkova** 46:48 The areas, yes.
**Joao G. (Dynatrace)** 46:52 It's.
**Josh Suereth** 46:54 I was just gonna say, the difference is the registry right now is split by signal, so there's one for attributes, one for entities, whereas what Lamille is proposing is there's just, like, here, it'd be all the namespaces, and when you click on a namespace, we would show signals first, before we show attributes. Like, everybody comes here and looks at the attributes.
**Joao G. (Dynatrace)** 47:12 And…
**Josh Suereth** 47:12 What we really want to do, because of how we work, is, like, point at namespaces, and who owns that namespace, and then signals in the namespace, and then attributes come last, because we're trying to really emphasize, like, the signal is what's important.
**Joao G. (Dynatrace)** 47:27 Right down.
**Liudmila Molkova** 47:27 And what we probably miss was this is I kind of like for entities, for example, that there is one Page that lists the ball.
And we can… generated here, right? So do we have a… README here, we can generate a list of the file with all the entities and links to them, like the… just the index.
Yeah, but it's it's probably the next step after V. 2. I kind of want to play with it for semantic conventions. Gen. AI. And for the shared Templates. So, John, I don't know if you've seen this recall.
**This is the… Joao G. (Dynatrace)** 48:09 Nope.
**Liudmila Molkova** 48:10 Well, yeah, yeah.
**Joao G. (Dynatrace)** 48:11 Yeah, I saw that you merged, that you had a PR to move some of the… The functions there, the policies.
**Liudmila Molkova** 48:20 Right, because we want them shared, right?
**Joao G. (Dynatrace)** 48:22 Mmh.
**Liudmila Molkova** 48:23 to do federated Semconf mainframes are going to do them. We've been telling client SIG to maybe also look into this.
And semantic conventions are now separate. We want them shared.
And then the templates ideally by Jamie, but templates ideally should leave.
Here, too.
But I kind of want to… Change semantic conventions templates to keep the current structure, so that where Of the markdown, so we don't deal with… Changing a lot of minor things, plus overall structure.
And we can… Switch to, like, this, this view later on.
**Joao G. (Dynatrace)** 49:14 So you mean you want to have the templates to have them… change to v. 2 to v. 2, but have the minimal amount of changes, or so.
**Liudmila Molkova** 49:23 Yeah, minimize the amount of changes in Markdown for the migration purposes.
**Joao G. (Dynatrace)** 49:28 Yep.
**Liudmila Molkova** 49:29 Yeah.
I'll be looking into, like, the problems, that… Like structurally block us from.
switching to V2 templates in Weaver, and switching templates, and maybe some YAML fixes.
If you have some capacity to do things for V2, there are other things that I feel are not blocked at all.
**Joao G. (Dynatrace)** 49:55 Yeah, sure.
**Liudmila Molkova** 49:57 Yeah, I don't.
**Joao G. (Dynatrace)** 49:58 We do have some cycles right now, so that would put… Yep.
It will be fine.
**Liudmila Molkova** 50:04 Nice.
So, like, if you look into the makefile, there are other.
We have, like, what?
The… this one. We use Weaver here.
And we can easily switch to these commands to redo.
All right.
where This is on V. 2.
Or let's go, I'll merge it soon.
There is this one that can switch, and the coolest part.
I feel we are, we can… explore the publishing right? Nothing stops us from actually Starting to publish schema or at least starting to generate artifacts.
**Joao G. (Dynatrace)** 50:55 Mmhm.
**Liudmila Molkova** 50:57 And we can switch the, yeah, we can either keep the schema that we have today, but also generate artifacts during the release.
to for for the scheme of it to.
Now we don't, we won't publish them first because we still might break schema V two.
But… Also, we need to work with our Telio people to figure out how to publish new schema.
**Joao G. (Dynatrace)** 51:32 Right.
**Liudmila Molkova** 51:34 So this this this is probably a decent, amount of work and some some maybe even interesting work. This are, like, AI agent would do them in an hour with all the validations and review.
Well, in your responsible hands.
**Joao G. (Dynatrace)** 51:53 Yeah, for sure.
Okay.
Yeah, I might ping you again, but yeah, okay, I'll try to take a look at this then.
Because the GenAI one was able to move to V2 because, like, it was… pretty much the same problems right there, and now it's on the B2 schema there.
**Liudmila Molkova** 52:16 Wow.
**Joao G. (Dynatrace)** 52:17 Gen AI.
Well, no.
**Liudmila Molkova** 52:19 It didn't have… Joao G. (Dynatrace) 52:20 But yeah, yeah.
**Liudmila Molkova** 52:21 Yeah. So most of the problems are well, first, we didn't have any public groups. We the GenAI conventions appeared after we Knew enough about how to do this.
**Joao G. (Dynatrace)** 52:33 Same.
**Liudmila Molkova** 52:34 Convention, so we didn't have like this.
Attribute groups a lot, and we didn't, yeah, we just… It was.
**Joao G. (Dynatrace)** 52:44 The signals, yeah.
**Liudmila Molkova** 52:46 Yes.
**Joao G. (Dynatrace)** 52:48 Makes sense. Okay.
Yeah, the biggest…
**Liudmila Molkova** 52:52 Violator, I think, go ahead.
**Joao G. (Dynatrace)** 52:54 No, sorry, you can go.
**Liudmila Molkova** 52:57 The biggest violator we have is hardware.
**Joao G. (Dynatrace)** 53:00 Yeah, that, that, that seems to be the problem always, right? Like, You know.
And it's so, so big as well.
Yeah, really.
**Liudmila Molkova** 53:10 We would federate them if we could, right?
**Joao G. (Dynatrace)** 53:13 Yeah, because that was also the problem when I started looking into the requirement level thing.
Oh.
There's there's like reuse of of attribute between metrics and and completely different values for the enums, and and so on. But whenever I just stopped because it was like, you know, I start changing one thing, and then I had to change another thing, and then change the other thing. And then, when I looked, it was like I was so far so far out what I was initially doing. I was like, I'm just gonna stop Oh.
Yep.
Yeah, what I wanted to say is, the… HTTP thing that the person took, I just closed the PR.
hope… hope they don't… they don't feel that I… I just, didn't like what they were doing, or want to waste, but yeah, I felt it was… it was going on circles, and I didn't want to give the impression that we don We're not just ignoring them, so I just said that there's blockers, we'll work on them I just assigned for the unassigned for the from the person.
**Liudmila Molkova** 54:15 Excellent.
**Joao G. (Dynatrace)** 54:15 The on the on the block. Yeah, sure. Or do we? We? Yeah, fix the blockers, and then we can.
I guess, distribute the migration?
Right, okay.
Yeah, thanks for the for the infos insights.
**Liudmila Molkova** 54:32 Thank you. Do you want to join this one? Does this time work for you?
**Joao G. (Dynatrace)** 54:36 Yeah, this time works better. I will just. I'll just. I just already put it on my blocker on my calendar, so there will be no no overlap anymore. So this one I will. I'll start joining irregularly now. The other one is a bit a bit tricky, because I have to Pick up my daughter, and then, yeah.
Sometimes it works, sometimes it doesn't, so… but this one, this one always works.
**Liudmila Molkova** 54:57 Awesome. Great to have you here.
**Joao G. (Dynatrace)** 55:02 Yeah, there's enough overlap anyway, so.
Makes sense.
**Liudmila Molkova** 55:10 Cool.
Should we call it?
**Joao G. (Dynatrace)** 55:16 Yes.
**Liudmila Molkova** 55:16 Thank you all.
**Joao G. (Dynatrace)** 55:18 Yeah, have a nice day, by.
**Liudmila Molkova** 55:20 Yeah, you too, see you.
