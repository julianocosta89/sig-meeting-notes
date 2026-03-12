SIG: Semantic Convention Tooling
Date: 2026-03-04
Duration: 61 minutes
============================================================

## Zoom Recording Transcript

ariannavespri 00:01:32 Hello?
Jeremy Blythe 00:01:36 Hi there.
Laurent Querel 00:02:18 Hey, everyone.
ariannavespri 00:02:23 Hello?
Laurent Querel 00:02:25 Yep.
Josh Suereth 00:02:46 Hey, everybody.
Laurent Querel 00:02:48 Boom.
Josh Suereth 00:02:50 How we all doing?
ariannavespri 00:02:54 Great, how about yourself?
Josh Suereth 00:02:57 Pretty good, pretty good.
What else did I want to talk about? There's something else? Okay, please folks add your, Add your items to the agenda and your names to the agenda, and I will start presenting, and we'll probably get started shortly.
Right. Here we go.
Okay.
Ludmila's not here yet.
So, actually, Jeremy, do you want to talk about the dog foodie one?
Jeremy Blythe 00:03:43 Sure. Yeah, I… I guess, really, it was your question… That I wanted to, talk about, which was… I think you were wondering whether we should be doing this generation, like, for the entire project, rather than Just within the live chat crate?
Josh Suereth 00:04:08 Yep.
Jeremy Blythe 00:04:09 And so… I did an it-depends answer. So, like, do we… I guess… If we want the crates to… Is the idea of the crate still that at some point in the future we're going to, like, publish them and make them so they're, like, independent things? Or has that shit, like, are we never gonna get to that point? Because if it's supposed to be a totally independent thing, then the generations should sit with The crate, absolutely.
Josh Suereth 00:04:43 Yeah. Just using them as, like, folders.
Jeremy Blythe 00:04:46 and not really, like, we use them as crates, but they are always only ever going to be part of this project, then I get it.
we could move the generation out. The other part of the question is.
LiveCheck is the only thing that produces telemetry.
But do we want… this got me thinking, do we want other parts of Weaver, like, say.
Check, or other things, to be able to emit telemetry.
Don't know.
So… That's really where I'm stuck.
Josh Suereth 00:05:25 Yeah, I, I, okay, so… I think the policy that you were saying of, like, cool, if these crates ever want to be separate, it should be, like, a per-crate thing.
I'm fine with, honestly.
Except we're always gonna build them together in the repo, so… and Weaver is something that runs prior to that, so I… I could go either way here. It's more… me, I'm… I'm lazy, right? Like, I don't want to set up all the Weaver infrastructure and have to run it, individually myself, like… Let's go to a different question.
how are you going to keep this up to date, generally? Like, what are you doing to make sure that the Weaver CodeGen is part of it? Is this a build.rs? Is this… I need to look at that again. Is this something you run manually? Yeah.
Jeremy Blythe 00:06:21 if… if you… If you make a change.
this is the joy of it, right? Because live check is checking live check, so if you make a change, the live check test will fail.
And then you have to go and update it. So this is, like, LiveCheck being used the way LiveCheck's supposed to be used. That's why it's dogfooding.
Josh Suereth 00:06:39 Yeah, no, I love that. What I'm saying, I'm talking about, this manifest model here, right?
Jeremy Blythe 00:06:47 Yeah.
Josh Suereth 00:06:48 If I make a change here.
Jeremy Blythe 00:06:50 Yeah.
Josh Suereth 00:06:51 how do I make the update to it? What do I need to do locally? Do I have to run, like, a local build of Weaver? And how do I do that if my build is failing?
Jeremy Blythe 00:07:01 Oh, I see. Yeah, there is a bit of a, There's a bit of a paradox.
Josh Suereth 00:07:05 Yes. Yeah.
Jeremy Blythe 00:07:08 So…
Josh Suereth 00:07:09 like, it's fine to have that dogfruit cycle, but we have to break this. Like, in compiler design, right? A lot of compilers compile themselves in their own language. But the way that works is you use the previous version of the language to compile the next version of the language.
And so there's that aspect here of, like, we don't want to have flaky builds.
because we're using our own build to build our build. How are we gonna break the cycle? That's literally my main… so… That would be my main concern, and then the secondary concern is just the, like, how do we want to, you know.
iron this out. But I actually… I didn't, I reviewed your PR, and it's large, and there's a lot of awesome stuff in here, but I didn't… I think it was X task, right? I don't know XTask well enough to know, I think this means you have to build.
to be able to update the generated code, and you call XTask check generated, right?
Jeremy Blythe 00:08:10 Yep.
Josh Suereth 00:08:11 Which means that it's semi-stable. Like, it's… like, we're not actually building… the code as part of our real build. We're… we're… We can have a stable checkpoint where we go build all of that code.
But if I've generated code that's broken.
Can I run X task again? Or does it fail because its dependencies are now broken?
Jeremy Blythe 00:08:35 I'll tell you what I do.
I don't… I'm not sure I have the answer. I'll tell you what I do.
Okay. When it's… when it's in a good state, I make a release build locally.
Then we have debugging. I can call… I can call the release target.
To do the generation against the broken debug target.
Josh Suereth 00:08:56 Y-yeah.
See, I… I'm… this is… when we… when we were doing, trampolining in Scala, that's what we'd have as well. So, the first step of the build process was to download the previous version of Scala, and then you would build the next version with the thing you had downloaded, instead of trying to, like, use your local build to build it. So.
I think we want to figure out a way to do that here.
Jeremy Blythe 00:09:23 Okay, yeah, I get it.
Josh Suereth 00:09:26 And then I will also buy your argument, because I believe in it, is that, If we want these crates to be somewhat independent, we have different registries for each crate.
I could buy that.
How does everyone else feel about that?
Laurent Querel 00:09:49 I think I understand the problem, I agree with it.
I don't know the solution yet.
Josh Suereth 00:10:04 the… So, so the question, the question is, let's talk about schema URL and registries. Should we have a separate registry for every single crate in Weaver?
Or should we have one Weaver crate registry?
And then every crate depends on that for what data they generate.
And then you shook your head.
I saw it.
Liudmila Molkova 00:10:37 I don't know enough to make an opinion about Rust infrastructure.
Josh Suereth 00:10:43 What's your intuition around, having multiple schema URLs for Weaver itself versus one for the whole project?
Liudmila Molkova 00:10:53 Oh, it should be one for the whole project, I mean, like, how granular would we want to be?
Josh Suereth 00:10:59 Great.
Laurent Querel 00:11:00 And I think that that will also happen. One of the comments I did in the other PR that Jeremy created We will have with our use in mono repos, where we have bookkeeper services.
So I think at some point, we should be able to, for example, use Weaver Check.
with, some configuration that expresses the subset of OGC we want to check.
I think in that case, that could be applied. If we have a single registry.
for the entire set of crates, but you want to check a specific crate, we should be able to do that with a G Suite trade.
Josh Suereth 00:11:45 Yeah.
Yeah, that's fair. Okay.
Laurent Querel 00:11:49 And in the case of, and I think that's justified well with also this report for Mono Rico, which is an abuse Other case where we could imagine people creating Either, a registry per service, or… A multi-service registry, something like that.
even if I personally will not do that, but I'm sure that there are probably some use cases for it.
Josh Suereth 00:12:18 Yep.
Okay.
Laurent Querel 00:12:25 So it's… it's matching well also with this Weaver terminal, if… and… and some parameters we need to check… to… to add with the Weaver registry check command.
some filters.
That will apply to… To the subset that we want to check.
Josh Suereth 00:12:48 So, okay, let me, let me start writing down some, some concerns here. So, like, AI has, Figure out the, bootstrap.
Issued.
Can we build Weaver?
If the Weaver build is broken.
To get into a stable version.
can we allow users to provide schema URL? I need to think about that one, Laurent, because I… I get what you're saying about a monorepo that would, like, import ours, and they'd want to use their schema URL everywhere for anything they generate.
Yeah, I don't know… I don't know if that's, like, a blocking thing for this, but that's… that would be, like, a future… Future capability, right?
Laurent Querel 00:13:39 Yeah, yes.
And I'm looking to the cargo.tunnel of the Xtask. We don't have any dependency.
In this cargo terminal, to the rest of the weaver project.
Just for information.
That's, that's… So that, when you can compile, I… I didn't check. So, grain of salt there, but… I have the feeling that…
Josh Suereth 00:14:06 Time's gonna depend on it.
Laurent Querel 00:14:07 task without, even if the project is failing for the other breaks.
Josh Suereth 00:14:13 Right, but if X task depends on the rest of the project, then it would fail, right?
Laurent Querel 00:14:18 Yeah, that's not the case today. And, we should not be in this situation, because we should, we should, we already have the situation that we have, we are running, I think the Weaver registry check from… or the generate, I don't know exactly what you use in the XTAS.
But, oh.
So, Germany, I didn't look at this PR, so sorry for that. The… the each task that you added.
Is running a command.
We recommend, right?
Jeremy Blythe 00:15:03 Yes.
Laurent Querel 00:15:04 And this, we recommend, is expected to be there.
As an executable, a binary.
Jeremy Blythe 00:15:12 So… Oh, okay, just checking one with the nutrient.
My head's been in the other PR for a while, so… the X task…
Josh Suereth 00:15:28 Here's the code, if it helps. It literally is calling check during… I think… Mon check generated, it's calling RUD on it.
Check generated is…
Jeremy Blythe 00:15:40 Yeah, this is just to… This is… this is Running Weaver.
Laurent Querel 00:15:47 Just like we were tossed to…
Jeremy Blythe 00:15:49 Same pattern.
Laurent Querel 00:15:49 For example, this task will not work on my machine.
without… if I'm starting a new GitHub repo.
and I didn't compile the project at all, and I'm running the X task, I will not be surprised if this command does not work, because the Weaver exec does not exist yet.
Josh Suereth 00:16:10 Yeah, there's also an issue of if I've made changes locally that are breaking in some fashion, I can have an instability issue where, like, my local PR literally can't be reproduced.
Laurent Querel 00:16:29 Yeah, I don't have a solution, there is probably one.
Josh Suereth 00:16:34 The solution I've seen in the past is we find a way to pin version of the weaver you look up here has to be pinned from somewhere, and we have to find a way to make that work.
You know what we might want to do? This is really stupid, okay?
I'll… well, not really stupid, but it's… it's, like, my… the top of mind.
If we start actually publishing our crates, depend on the previous version of the crate hard-coded right there.
Okay? In a, in a separate, like, thing. And then you would use that previous version of the crate to do your stuff.
And then anytime we cut a release, we'll bump the release version of the crate we depend on.
Okay.
In that X task, so we're actually always depending on our previous version to do this. That, again, that is what, when I've done dogfooding before in this fashion.
That is what I've done.
Jeremy Blythe 00:17:30 to… About a year ago, we added a next task for the history.
Which follows this pattern where… It uses the weaver that you've just built.
to do tricks.
Josh Suereth 00:17:44 But that's different.
We're testing if the binary that we just built is… is… like, that… that is actually… it's an X task, but it's really a test, it's an integration test of the binary you just built.
Jeremy Blythe 00:17:59 Yeah, I'm using this as a test also.
Josh Suereth 00:18:05 How are you generating the code?
Jeremy Blythe 00:18:08 So if you look in… if you go up to the CI, you'll see I've changed the CI.
So that I run the X task just after history to check the generated.
So that was the pattern I was following.
Josh Suereth 00:18:24 how are we generating the code? We just expect everyone to install their own Weaver version? Is that what it is?
And you have to manually run that command yourself every time you check something out?
How does the generated code get there to begin with?
Jeremy Blythe 00:18:38 It's checked in.
Josh Suereth 00:18:40 How do I update it?
Jeremy Blythe 00:18:42 If you go to Dog FoodingMD, It tells you what to do.
Do you have to… you have to run commands?
There.
Josh Suereth 00:19:01 Yeah. But this is where you get the problem.
Jeremy Blythe 00:19:03 If you've broken something, and then you need to generate… You're not going to be able to… you're not going to be able to generate over the top of something you broke.
Josh Suereth 00:19:12 Well, this, where you… oh, you're using check generated. Okay, here's what I would do, man. I, like, let's… let's, I still think we want to pin the previous version. So, in dogfooding.
First of all, I'd want this to be in Contributing, which I can make a comment on. Sorry I didn't have a chance to read through all this. I was literally looking for this information and kept dorking around in this stuff and didn't make it up here. Anyway, I would suggest that we change this to a straight-up Weaver command.
And that we changed CICD to use a previous version of Weaver.
To check everything. So that we're all, like, again, the idea would be we're always using a stable version of Weaver.
Laurent Querel 00:19:58 Or to use the… maybe the… the image of the previous… the current version?
Josh Suereth 00:20:04 you could… you could use Docker image of the… yeah, you could use Docker image of the current version, you could use the GitHub action of the current version, like, but I think we always pin to a version for these commands.
Jeremy Blythe 00:20:15 Beautiful.
Josh Suereth 00:20:16 And then, and then I think you're fine. So yeah, Docker image, the CICD, actually, instead of necessarily X-tasking it, you could use, You could do the shenanigans we do in SEMCOV, where we actually do the code generation and look for git diff and fail.
On the previous version?
Laurent Querel 00:20:36 test containers, maybe, with, with Weaver, the stable version.
That could make sense in this context.
Josh Suereth 00:20:44 Yeah, yeah, that actually… that would work too. I like test containers.
Okay. But the, this bit, I think… Where… I'm scrolling like an idiot. The bit you had with the commander run, I would want this in contributing. Just… For my own sanity, to know, like, what to do to rerun these things.
Okay.
I think we spent a lot of time on this. Let's… there's a couple decisions here. One is around dogfooding, the actual mechanics of making sure we have a stable thing. Great.
We have some ideas, but Jeremy, like, whatever you figure out to do, just explore, is what I'd say. We can keep ideating, we could spend another 30 minutes on this. I don't know if it would be valuable to keep going.
Yeah.
Jeremy Blythe 00:21:32 And to be honest, this PR is, like, really interesting, but it's not critical.
Josh Suereth 00:21:38 Okay, I love that you did this, by the way. I think this is really fun.
The other thing, just to make progress, given the reaction Ludmila had, which I think matches my own.
I feel like we should limit ourselves to one schema for Weber.
I think that makes sense. And I hear what you're saying, but I'm fine if we have one schema for Weaver, but CodeGen goes into each individual crate. I think that's fine, too.
Jeremy Blythe 00:22:05 Okay.
Josh Suereth 00:22:07 Okay, cool, let's move on.
I will write that down. One. Okay.
Alright, Lunmela, registry package.
Liudmila Molkova 00:22:23 Yeah, it's a simple PR that adds registry package command, and all it does.
it creates a publication manifest. This is the sketchiest place. So we now have two manifests. One is registry manifest.
So yeah, if you look into the, just the usage, it's… it's not… it's not a problem to users.
Josh Suereth 00:22:56 Yeah, I was just… I was just reading to see what we have, in usage. Why is this… Document's so large. Alright.
Liudmila Molkova 00:23:03 And a lot of commands, yeah. So it's just yet another command. It will replace, Resolve. I have a PR for Resolve, but it's probably better to stack it on top of this. It takes, the same… like, it takes… two interesting things. First is the registry. First is resolved schema URI.
The rest is just, inherited. The resolved schema URI is something… Where you are going to publish your resolved schema.
It will not publish anything, it will just set the thing in the manifest.
Josh Suereth 00:23:49 Yeah. I like that it's here, by the way. I think that makes a lot of sense. That helps with CICD automation, yeah.
Liudmila Molkova 00:23:57 Cool. And on the insides.
Josh Suereth 00:24:01 Things get more interesting.
Liudmila Molkova 00:24:05 So, we had registry manifest, and it has optional file format and resolved schema URI, and I think it's good because it's a… It's a definition manifest. It was definition manifest so far.
Josh Suereth 00:24:20 Yeah. So I'm slightly repurposing it to be…
Liudmila Molkova 00:24:23 the superset, It can be either, and I can… we can identify which one it is.
Josh Suereth 00:24:32 And that's just if there's a schema URI, it's a publication one?
Liudmila Molkova 00:24:37 Or it's the… it has file format of the publication manifest. Maybe it should be more strict.
Maybe it should be both.
Josh Suereth 00:24:49 We can… we can clean that up, I gotcha. But… but just so we know what publication manifest is, what… what's the difference? This is…
Liudmila Molkova 00:24:56 This is required, and this is something public, like, I've added the JSON schema… it's a JSON schema, so we would publish the schema for it. It would be… something people expect to see. It might be different than the… like, it might have other properties than definition manifest in theory.
Josh Suereth 00:25:18 Yeah. I'd be fine if we do the shenanigans where we have a publication manifest and a definition manifest as separate.
Liudmila Molkova 00:25:27 Each… That's true We can do this, but then… I need to rewrite everything else, because when you load the registry, you should expect either And you still need a structure that represents either.
Josh Suereth 00:25:43 Right, we can make an enum that has one or the other, and then has a bunch of methods that lets you get information out of it, you know, based on which it is, to abstract over it. I know it's a pain, but it's, I think that that's probably what we want to do. We might not need to do that in this CL, but I think that would be probably a cleaner design there.
Liudmila Molkova 00:26:03 Okay, let me do a stab on this, and the… I think there is an important question, but an easy one. So, the publication manifest file format.
what should it be? So, Jeremy said that he would be interested in manifest slash 200. I made it initially 00200, because It matches the current file format on the… Current manifest, the 110.
Josh Suereth 00:26:35 Oh, for telemetry schema? Oh, God, yeah.
Liudmila Molkova 00:26:40 So I… I feel it's a bike-shading question, but I… I'd rather have it manifest slash because it matches everything else.
Josh Suereth 00:26:51 Yeah, let's, let's… let's make it be that. I'm fine with that. You know the other bike shit I want to give you?
I think you should put this in resolved schema.
Liudmila Molkova 00:27:05 put this oh.
Josh Suereth 00:27:10 Yeah, but that… that might also be a can of worms that we don't want to unlock right now because of registry repo and how we do dependency loading and all that kind of crap, yeah.
Liudmila Molkova 00:27:20 Okay.
Josh Suereth 00:27:21 If… if you want, we can just make a note of those kind of cleanups, and that might be something to tackle later. But one thing, I don't know, Lauren, you might not have seen all of this, but one thing I've been trying to do… Let me… Okay, just, just architecturally, we'll talk a little bit about architecture.
at one point in time, we had, effectively, the loading of Weaver schemas was mixed between Weaver Semcov and Weaver Resolver.
And, like, the real loading logic was actually in Weaver SemConf. And what I've been trying to do over time is minimize the amount that's in any individual crate, and have this loader file be the thing that knows how to load semantic conventions, and it can either load definitions, or it can load pre-resolved things, right?
This, this should probably get renamed to Definition, but whatever.
So, this is the, the, your definition manifest, and then these should have the manifest in them, but really, like.
The manifest that you have probably should only be defined in these resolved repos, because we don't need it.
For the definition repo.
the problem we have is the loading code is still split, like, the registry repo crap we use for loading, is still split between… where is that junk? I can look it up later. It's still split between the Weaver SemConv crate and this crate, but I would like to, over time.
Try to get as much of the, you know, formal loading code in here as possible.
But you don't… in my opinion, you don't have to do that in your PR.
It's… we're already in a space where it's kind of divided in a little… chunky, and we've been slowly migrating it, we can keep that process. Like, we'll just slowly evolve that way, if people agree to that.
Laurent Querel 00:29:26 Yeah, with this ability to load a registry that is purely definition or a result version, I agree with that.
Makes… It… it depends.
Josh Suereth 00:29:44 Alright.
I can'.
Liudmila Molkova 00:29:47 And try to move it to the resolved schema crate. If there is any problem, we can do it later.
Josh Suereth 00:29:57 Okay.
Yeah, if you're able to try it, go for it. If it leads to your branch getting destroyed, just… don't worry about it. I don't know how much of a can of worms that will be, but some of these things are really bad. Some of them are not so bad.
Okay, anyone have complaints with using Manifest 2.0 here?
One question, though. Publication Manifest and definition manifest. What's the definition manifest one?
shouldn't it?
Go ahead.
Liudmila Molkova 00:30:33 Just no results schema URI, right?
Or maybe it'll have some… well, probably just no schema URI.
Josh Suereth 00:30:43 Okay, so they have the same file format name, it's just this would be optional in the one and not in the other. Is that right?
Liudmila Molkova 00:30:51 It should be… It should not be present in one, and it should be present in another. It must be present in another.
Right, but I mean…
Josh Suereth 00:31:00 The file format would be the same for both. So for a definition manifest, file format is still Manifest 2.0. For a resolve schema manifest, the… or, sorry, publication manifest, it is Manifest 2.0. Like, the file format is the same in a publication and a definition registry manifest.
Right?
Liudmila Molkova 00:31:25 The definition manifest today doesn't have any file format at all.
Well, it could have.
Josh Suereth 00:31:32 We will ignore it.
I thought you added that. Yeah, I don't think we're paying attention to it, but I thought you added that, no?
Laurent Querel 00:31:38 It's optional, I think, no.
Liudmila Molkova 00:31:40 It's optional, yeah. And because… yeah.
Laurent Querel 00:31:43 But the question is still there. What will be the value if it's a sum and not a none. It will be a manifest slash 2.0.0, or it will be something else. I think that's the question.
Liudmila Molkova 00:31:56 It should be something else, because that's the whole point.
Laurent Querel 00:31:59 Or something like that, to be aligned with the rest of the technology.
Josh Suereth 00:32:03 Yeah, that's where I'm starting to get, We might… we might want… we need a different name for Publication Manifest and Definition Manifest.
So, I don't want to budget that here, I don't think that's a valuable thing. Let's just come up with a bunch of proposals and put it offline. But I'm a fan of having everything have a crystal clear, like, here's what it means, it lines up with the JSON… if we can get to the point where JSON schema uses the same name that is in file format, that'd be awesome too. So, like, the file format tells you which JSON schema you're using, and they all line up, like, that would be where I'd want to get to. So… Yeah. Whatever, whatever it takes to get there. I'm happy with, whatever proposal you make, we'll probably bike-shed it to death anyway, but we can do that in the PR.
Jeremy Blythe 00:32:58 Is some… It's file format.
A type, or is it just a string?
Because really, the… the… The first part?
Should be an enum, right?
We should have an enumeration of a… File format types…
Josh Suereth 00:33:17 Yeah.
Jeremy Blythe 00:33:17 And then, if file format is a type, then it can have a… It can, implement the display trait when you want to turn it into type slash version.
Liudmila Molkova 00:33:31 We can do this, but I'm not sure if… How would it help?
Josh Suereth 00:33:38 So basically, Ludmila, I like what Jeremy's suggesting of, like.
All the file… these are all the file formats right here.
What if we just move them somewhere centrally, and we actually, like, tell CERD, here's the… here's the string to use, here's the string to use, here's the string to use, for all of them?
And then we have a set of them, we know what they all mean, and we just set the file format to that string.
Liudmila Molkova 00:34:02 When we do this, instead of this enum, we would have an enum of file formats that we have.
Josh Suereth 00:34:10 Yep.
Liudmila Molkova 00:34:11 For V2. For V1, I don't care. There is nothing.
And we will… they will appear in the JSON schema for sure.
Josh Suereth 00:34:22 The specific strings, you mean, or…
Liudmila Molkova 00:34:26 the format string, so it should appear in JSON schema saying it's a string literal, or whatever JSON schema does to say this is the discriminator, or the static property.
Josh Suereth 00:34:38 Yep, and what I like is if we get to the point where they're more strict, we can make this JSON schema thing basically say, cool, I saw something that says file format X, go give me the JSON schema, there's a Weaver command you call, and it dumps it at you. This thing.
Right? So if file format is in a noom, and then a NUM is something we can use in the JSON schema command, and dump the JSON schema for that file format, I think we're in a really cool place.
Liudmila Molkova 00:35:05 Let's do it separately, though. It has nothing to do with package commit.
Josh Suereth 00:35:10 Yeah. What it has to do with package manifest is, I think that means we want, since publication manifest is different.
Actually, we don't have manifest in here.
Liudmila Molkova 00:35:23 We don't have it, but we should.
Josh Suereth 00:35:25 Yeah, we should.
Liudmila Molkova 00:35:26 emissions.
Josh Suereth 00:35:26 So, I think… I think where it's relevant is you're adding something that we're absolutely missing and should be here, and we probably also need definition manifest, then we just need to have different strings to label them. When you make that decision, that'll make the decision of the thing you need, right?
Jeremy Blythe 00:35:41 There's… there's definitely a rabbit hole here, because I also want to use the JSON schema thing for the Weaver config.
Josh Suereth 00:35:49 Yeah, which was.
Jeremy Blythe 00:35:51 And that works really nicely, but now Weaver config is not a registry command, like, it's nothing to do the registries, but my… but JSON schema is Weaver registry JSON schema.
So now, should we move JSON schema command up a level, so it's not under registry, because it's producing schemas that are not to do with registries anymore?
Josh Suereth 00:36:12 Yeah.
I see!
I'd say we should, we should move it, we should, we should move Jason Skuma.
Eventually. That's… that's a to-do. I, I, I agree.
with what you're saying, Jeremy, it never made sense to me that it was under registry.
Given what we use it for, I think it should be a standalone thing.
But… Does Lyudmila have to do that in her PR? No.
Jeremy Blythe 00:36:37 No, you don't have to do anything else, I think your PR's good to go, personally, but… It, it.
Liudmila Molkova 00:36:43 It actually already has to be a superset of file formats, because it includes V1, and it should stay there.
Josh Suereth 00:36:53 Yeah.
December.
This is, published.
Oops. Okay.
Alright. Is this enough to continue to make progress? I think I'll review your PR after this and see if, see what I can do. Sorry, see if I think it's ready to go as is, because I think a lot of this will be follow-on work.
Cool. What was… following up with deprecated Resolve, do you… do we need to discuss this at all? I don't…
Liudmila Molkova 00:37:34 No, no, we don't.
Josh Suereth 00:37:35 Yeah.
Liudmila Molkova 00:37:36 FYI.
Josh Suereth 00:37:37 Cool. Docs-related improvements, trivial.
Liudmila Molkova 00:37:41 Oh, nothing is trivial here! But yeah, let's go. So, I… used… I wanted to make this a reality that we… run… We produce the schemas.
And we validate them.
It's not the end, but it's a start that's resolved schema, and thanks to Jeremy pointing me to the usage docs previously, I figured out it's super easy to also check that our schemas are up to date.
Please don't tell me I should run previous version of Weaver for this, no.
Josh Suereth 00:38:23 No, no, no, no, no, that, that is… that is… okay, no.
This depends on Weaver Building, and this is the latest Weaver dock. Yeah, so no, you're fine here, yeah.
Jeremy Blythe 00:38:36 I had one question here, though.
Is this… This is obviously fine, and it makes sense… to me, it makes sense that we have the schemas in the project.
Did we also want to publish these so the schemas are artifacts of a release of Weaver?
Josh Suereth 00:38:56 I would prefer them as an artifact in the release of Weaver, personally, just because the problem with having them in the in the project, if people depend on Maine.
And we make changes that are slightly breaking or slightly different, we break anyone's usage, versus if they depend on a versioned copy.
Liudmila Molkova 00:39:17 They can depend on the version to copy already, through tags.
It does not mean we shouldn't have them in an artifact.
Josh Suereth 00:39:26 Okay.
Liudmila Molkova 00:39:26 But… it's trivial.
Josh Suereth 00:39:32 We haven't figured out how to attach artifacts and cargo discs yet, and that is a can of worms I was planning to open at some point, but have not.
So…
Liudmila Molkova 00:39:42 I'm not ready to open it.
Josh Suereth 00:39:44 Yeah, I don't think we need to open it here, this is a good question. I… this is good, this is good. I like… I like that we… we have this now. I also, finally got my AI, updated to… all this stuff, I don't do by hand anymore, I just tell it to, hey, go through contributing and, like, fix things. The only thing I'll say is contributing has confused the crap out of it, where it will copy observed output into, Into expected output.
in the wrong directory every time, and I can't get it to stop it.
And it shouldn't be doing that when things are passing at all anyway.
So, I think we might… I might have some contributing Markdown, fixes later.
Because that's been frustrating. But in terms of these things, this is awesome.
Liudmila Molkova 00:40:31 It's not… not a huge burden.
Josh Suereth 00:40:32 Okay, great. Anything else around this?
Liudmila Molkova 00:40:37 Nope, nothing.
Josh Suereth 00:40:38 Okay.
Liudmila Molkova 00:40:39 Alright.
Josh Suereth 00:40:40 So, I got one, oh, never mind, Jeremy was in front of me.
Liudmila Molkova 00:40:46 There is one more I want you to get your attention on, the add file format to definition JSON schema. So this one is a little bit more tricky, and I hope we can, I hope I found a good way to do this. So, what happens today? Can you… did you… did you open the… Oh.
Josh Suereth 00:41:06 Oh, yeah.
Liudmila Molkova 00:41:08 It's a different…
Josh Suereth 00:41:10 So, I know exactly what was happening, basically.
Yeah, this was handled upstream in our V1, V2 crap, but we're That's directly, yeah.
Liudmila Molkova 00:41:20 And it had no bad side effects except the validation against JSON schema and VS Code IntelliSense that it would not recognize file format as a good property on the V2 file.
And it would, complain, and I would imagine users would always be confused by it, would remove it, everything will fail, so I just… the sole purpose of doing this is to make it appear in JSON schema.
Josh Suereth 00:41:52 Yep. That… That makes sense. Are we… so we're actually skipping… serializing.
We… you could, and I know that this sounds really stupid.
you could skip serializing and deserializing, possibly. Will that still show up in Scheemars? And then give it a default of V2.
And so, yeah, we're attaching a Rust string that's annoying.
The other option, I don't think there's any weird way to customize schemas to just add fields.
Jeremy Blythe 00:42:28 Oh, you can.
You can do everything horrible that you want to do.
there's… there's a… Because I looked at this exact problem, LaMella, you, you beat me to it.
I will… you… you can… You can declare a transform which runs a… function for you.
That then can manipulate the schema.
So in… you can put, like, in that schema, you can put, transform equals, and then give it a… give it a Rust function, and it will… and then you can do whatever you want, then.
Liudmila Molkova 00:43:07 Okay, let me explore…
Josh Suereth 00:43:11 Yes.
Jeremy Blythe 00:43:12 But it gets, like, more and more, like.
I started doing that, and I felt a little bit wrong.
About it.
Felt a little bit like, ugh, this is a bit dirty.
Josh Suereth 00:43:26 That's how you know you're solving a real problem, is when you have to use the backdoor.
Yeah.
Jeremy Blythe 00:43:33 I would really like file format to be in… to be in enum, and then when I'm in… when I'm in VS Code, then, and I've got the schema loaded, it's actually gonna offer me manifest or blah blah blah blah.
Laurent Querel 00:43:49 We could…
Jeremy Blythe 00:43:50 Instead of adding a string…
Laurent Querel 00:43:53 Instead of adding a string, we could, just… Create a new type, file format.
With these two elements.
Third edition, we, we, Will be a single string, that's not a big deal.
And we could imagine that the schema stuff is different for this one.
Josh Suereth 00:44:15 I mean, we do have, we do have the Enum, I believe.
Liudmila Molkova 00:44:21 It's just not what it…
Laurent Querel 00:44:24 Yeah, but we need a type with the name plus the version, I guess.
Josh Suereth 00:44:30 We also have this notion that we're, like, validating against one versus the other, and Yeah, it's up.
Liudmila Molkova 00:44:39 This… this one is specific to the definition, and it's some internal detail nobody should know about.
But… I was thinking about what Jeremy said, that we would, like.
if it's a… my understanding that if it's a proper JSON schema, it should be a string literal.
So that it's… bound to that specific format, and you should not see the enum in Each particular schema.
Josh Suereth 00:45:10 Yeah.
Like, the issue we have is when we parse, we don't know what the definition is, and we're trying to figure that out on the fly.
And this is where that lives, but the JSON schema that's created from this type the schemas is ugly as sin, and really confusing error messages. So what we're doing is we're actually generating JSON schemas for this and this individually, and we have to reconstitute the fact that there's a file format in there as well.
So I'm a fan of doing the dirty, I'm sorry, I should rephrase that. I'm a fan of doing the thing that… that, doing the file… adjustment thing here to make that work. Okay.
Anyway, cool. That's… this is a good fix. Thanks a little.
Liudmila Molkova 00:46:06 Thank you, and let me see if I can hack something around with the transforming schema itself. And, I'll probably create an issue for us to revisit the file format in since it's a Orthogonal problem, but it's a very good one.
Josh Suereth 00:46:22 Okay.
Cool, Jeremy, you want to talk about the next one?
Jeremy Blythe 00:46:28 Yeah, There were some good comments. I've answered the comment this morning, I think I agree with… pretty much everything that's in there. I just wondered if we… Wanna… talk about it anymore.
Where I started hunting.
Yeah.
Josh Suereth 00:46:50 If I go to the files changed, do the comments show up, or were they on the PR?
Victoria Things I learned, yes.
It's funny that no one… no one knew that this existed, huh?
Alright.
Jeremy Blythe 00:47:09 I literally made the assumption that we & Yamil was… entirely something to do with just, Weaver Forge.
And I never read the comment at the top of that file that said, It was sort of… The idea was to use it for more than that.
But I think over time, it's just fallen into only being used for Weaver Forge-type things.
It makes sense, and it follows what… it follows what we're… Doing with making packages and having… templates that are external and all of that stuff, it makes perfect sense. But now we don't have the other bit anymore.
We just…
Josh Suereth 00:47:49 Yeah, I'm on board with what you want to do. I think Lauren's comment here would be my only major comment as well, and it sounds like, yeah, we can do this. Like, the new… The new config would, have some shared stuff that the other one would interact with in some fashion when loaded, right?
Jeremy Blythe 00:48:07 Yeah, I think what you're saying is I'm happy to use this remote template package, from… the Weaver Packages project, and I'm gonna pull it in, and I'm gonna use that, but personally, I like to have my acronyms this way.
Josh Suereth 00:48:23 Yes, and so we have a way to, like, take the algorithms and slap them together.
Jeremy Blythe 00:48:28 Yeah.
Things like that. Yeah, that makes sense to me.
Josh Suereth 00:48:32 Cool.
Laurent Querel 00:48:34 That's one use case, but you also have the use case where you have multiple template families for the same project.
And you want to share the same acronyms across them.
That was possible before, it's still possible if we do this, If we follow this approach, of having the… the safe shared nubs, across stone plate located into this, river.tunnel.
Not only for remote, in my opinion, that's what I'm saying.
Josh Suereth 00:49:06 Did we… did we decide it would be Tamil?
Laurent Querel 00:49:11 I'm not against it, personally. That's okay.
Jeremy Blythe 00:49:14 I got some thumbs up.
Liudmila Molkova 00:49:18 I, I, AI as independent observer, what should I pick, and it tells me Tamil?
For this developer CLI tool.
Josh Suereth 00:49:28 I… I honestly, like, Tamil, who had a… I write lots of YAML.
The less YAML I write, the happier I am.
I will say that. So, I'm fine with Tamil.
This… this is… this is the other thing I wanted to ask. Can we make this so that you can specify, like, the packages?
So instead of, like, the path, this is a full path, right? So I could say, cool, I want it in my Weaver Tamble to say, here's the policy packages I'm using.
Right? And it would have all the ones that I want for live check and stuff, the remote ones. So I can put it in a config, and then when I run the Weaver command, I don't have to specify them on the command line all the time, it's in the config.
Jeremy Blythe 00:50:14 Yeah.
I think that's what I'm saying.
Liudmila Molkova 00:50:17 I have a comment on this. So, I agree with policies, but the registry, like, what your… Well, maybe a registry, but there are, like.
the tools usually have two sets of parameters. One are… like, you only specify it per invocation.
And others are more persistent.
And not all of the Weaver properties should be… her assistant. Like, if I run Weaver Check.
it's natural, like, it's just idiomatic to provide the pass I am checking as the common line versus in the config. Otherwise, we will just have all the commands river… registry check.
And it just feels weird.
Jeremy Blythe 00:51:08 I… I answered that, though.
Wherever you put that in here.
I'm like, but why not? Like, I've got a project, so at my work, we have projects where we've got a model.
I want to check that model now, it's always that model.
So… Can I not just write Weaver registry check, enter? And I know it's… and because I'm in that project, that's my working directory, it's gonna check that model. If I type Weaver registry check.
Come on, 190.
with nothing else. It goes and checks Semantic Conventions Project's main branch.
That's the default. Yeah.
Josh Suereth 00:51:52 Let me add to this, Ludmelon. Like, when I run a cargo test, or when I run NPM tests.
I don't put any command lines on there. I just… it just does it.
But I would argue that you could optionally filter down to a subset. That would make sense to me, of saying, cool, I want to say Weaver checked just this policy, and then I don't use the default config, and I'm just checking one thing.
But if we compare this to build tools, right? Like, I'm with Jeremy. I think we… just running Weaver Registry Jack.
Liudmila Molkova 00:52:25 When we do… NPM test.
or other development tools, it defaults to a current directory, not to what's written in the config.
And it usually doesn't have a config that says.
it may contain a list of projects, but essentially it's just the default of the common line parameter. I'm not against it, I'm saying it's not idiomatic to development tools, to how they work to put this into config.
Josh Suereth 00:53:01 Let's take that discussion and continue that. I would like to talk about refinements. We only have 8 minutes left, if that's okay.
I hear what you're saying, but I don't think we're going to resolve this in 8 minutes, and I really want to talk about refinements.
Are we okay moving to refinements quickly?
Jeremy Blythe 00:53:17 True.
Josh Suereth 00:53:19 Okay.
Cool. So, this is the refinements PR.
Apologies, if this is too AI-y, but, I thought it actually looked quite good, and I wrote the hard parts of the code myself, but there's some bullshit that I had the AI do for me, like fill out all the isV2s. Effectively, what this does, I'll put this in the comments, is we actually add refinements to the V2 syntax.
We had to create an ISV2 flag to track groups through going back to V1, going through the resolution engine, and coming back out. I'll show you some of the big things that are there. We updated dependency resolution.
So that when you look up a group through Extends, you get the additional properties of the group, so if it's a V2 Extends, where it's a refinement, you actually keep the metric name, you keep the note, you keep those things, if you didn't specify them yourself.
So I was… I wanted to show you what that looks like in practice.
Testing and fixtures. Hey, is this working? That is so cool. Thank you, Copilot. Alright, so here's, like, an example definition. I have attributes and attribute group, I have a metric, right? So, in this one, my metric is named, base metric.
And I have my brief instability defined, and I have annotations, by the way. In the refinement, I have a different set of annotations, but what… the way this works is I actually put a quick merge algorithm together.
Where it blends the one on top of the other, so if there's a conflict at a particular key, the new one overrides it, otherwise it keeps the old one.
Which… which I think is the behavior we want initially.
And if you notice here, this has a brief, but it does not define stability, or unit, or instrument.
And so, when this comes out the other end.
In the… that's the attribute catalog, in the refinements, base entity.
here's… that's a refined entity. I did this for a bunch of different things, but when you look at the metric, the refined metric, you can see the name is still base metric. I actually had to do some shenanigans to make that work.
Not super big shenanigans. You can see the unit and the histogram get pulled over, even though we didn't have to specify them in the group itself, so resolution engine's responsible for filling it out. I still am working on provenance, that's… that's gonna be a future thing. And then… stability is stable.
And I forget where annotations lines up, I think it's after… yeah, if you look at annotations, it's a blend of the two.
Together.
So that is, oh, that… I was… might have been looking at something else. Here's the other… here's the blended annotations, right?
And here is where the metric name is still stable, the brief is now refined, stability remains stable, and it uses the previous attributes. Yeah, go ahead, Lauren.
Laurent Querel 00:56:25 So we're getting the merge algorithm for adaptation.
Do you, support… if you want to remove an entry into the annotation, do you support something like, you… you null ify an entry into the annotation in the refinement, and it's removed at the end?
Is it something that is part of the merge?
Josh Suereth 00:56:47 If you were to set null , I think that would work, I have not tested that. The logic is really stupid.
Might be under other changes… no.
V2 Refine… it's probably here.
Let me just… I… I… there's… there's a file called… Wait, oh, oh, I have to go to all files, here we go.
Under Weaver Resolver… All of that logic is in a file called merge.
If you want to see what it's doing. But it's really stupid.
It is really stupid. It's just go through the key value maps, and you know.
Apply, if the value is not empty.
fire it in. That's all it does.
I have a to-do around advanced merging logic, like, we still actually can't handle, removing attributes from upstream if you're allowed to.
That is something that we have to figure out. Like, for metrics, you can't. That would break the… that would literally break the metric and the stability of it. But for, like, descriptive attributes and entities, for attributes and spans and, things, you might be able to remove, like, opt-in ones.
Laurent Querel 00:58:02 Or annotation. You can… maybe you want to remove an entry into an array, or to a map, or whatever.
Josh Suereth 00:58:11 Yeah, so I… this merge stuff is, I think, the riskiest part of this. If you want to see the logic for where we had all the craziness around… oh yeah, here's the check uniqueness. The way I'm checking for uniqueness is I'm grabbing metric names, but I… if it's a V2 refinement, I just pretend like it doesn't have a metric name and ignore it.
Because I know that it's gonna be duplicate. So there's some shenanigans in here to take a look at.
Oh yeah, god, the fun… Rust, Rust, mutating things. You can't call it isV2 down here, because the group has already been moved. Fun times. Anyway, I can look for where that was, but you can see the dependency resolution was changed as well, so in extends now, instead of just grabbing the attributes, I created this thing called Group Summary.
And when you resolve dependencies, you have to return a group summary, and we have an index of all of those, then you look up the group summary. When you get the group summary, we say, okay, cool, if this is V2, here is your merge logic.
Okay.
So, if you want to know, like, what exactly is getting, you know, merged over, you can see here. Here are the things that you literally are not allowed to change without breaking our data model.
And then there's optional things that you might be able to override, and there's an alert that basically, if you have found a way to define V1, groups.
Manually, that will break us. We'll fire an alert. This should be impossible. There is no way you should be able to get this alert.
But I put it in there anyway, just in case.
But that's the real meat of the logic.
I'm actually really happy with how this looks now as a first step, and I think this really resolves one of our biggest issues. I actually… I like this inheritance model here for these. I think this is a bit nicer. It lets you optionally do, you know, deprecated brief note, if you want. I am allowing stability and deprecation to change for these refinements from upstream, and I think, like, on purpose.
Those are kind of, like, the hard decisions we need to make. We're out of time, yeah, we'll see you, Jeremy. But please review this. I'd really like to get this in for the next release, so I'd like to get this merged.
hopefully, like, early next week, latest, so that next week we can cut a release with the changes Libila's made, with some of the things Jeremy's done, to get this out, because I want to start getting… I think this refinement bit actually unlocks really testing this in, in, SEMCOMF.
Cool.
Alright, thanks guys. Have a great weekend, everybody.
Laurent Querel 01:01:09 Thank you.
