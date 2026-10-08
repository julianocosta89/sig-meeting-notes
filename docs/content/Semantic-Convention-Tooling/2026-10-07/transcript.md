SIG: Semantic Convention Tooling
Date: 2026-10-07
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Laurent Quérel** 00:30 Hey Luna.
**Liudmila Molkova** 00:31 Hello, everyone. How are you?
**Laurent Quérel** 00:33 Boom.
you Going well. I was just thinking, am I the only one today? Usually I'm not there, and just today, no one.
So, how that works…
**Liudmila Molkova** 00:50 I think we would hear from, oh, the Jeremy, he can't make it today.
But I have.
**Laurent Quérel** 00:57 Yeah, I just read that, yes.
**Liudmila Molkova** 01:00 Yeah.
Yeah, so let me give Josh a few minutes to join.
We had the release.
Last week.
Maybe.
Let's see… I wanted to talk about… Refinements and entities.
**Laurent Quérel** 02:22 I saw your message in Slack.
Who needs to peek?
I have to admit that I didn't read the proposal.
**Liudmila Molkova** 02:36 Yeah.
Yes, sir.
**Josh Suereth (Google LLC)** 02:41 Hey, sorry I'm late.
**Liudmila Molkova** 02:43 No.
**Laurent Quérel** 02:44 Pleasure.
**Liudmila Molkova** 03:01 I'm just filling in the agenda.
**Josh Suereth (Google LLC)** 03:09 Yeah, I'm a little behind today, sorry.
**Liudmila Molkova** 03:16 Yeah.
Right.
Sorry.
Do we have anything interesting on this board?
So we are… we just released.
Yep.
I wish we could.
Target.
Some milestone for V2 for the next release.
I'm not sure if we can…
**Josh Suereth (Google LLC)** 03:54 I… is it possible we could stabilize packaging, or do you think there's more things for V2?
**Liudmila Molkova** 04:01 Double Ace Packaging.
**Josh Suereth (Google LLC)** 04:03 Yeah, Weaver package.
Like, I'd like to get to the point where we can remove the warning about the V… like, when you do dash dash V2.
It says, warning, this is unstable.
I think our target for the next release should be removing the warning.
**Liudmila Molkova** 04:17 Wait, the definition format?
Or packaging, because packaging, there is no single… User effort, yet, that we are aware of.
**Josh Suereth (Google LLC)** 04:28 Yes, but I would… but given what we… is going on in the Semcom chat with, like, the client side, I think Package will have a user pretty soon.
And so…
**Liudmila Molkova** 04:41 Seriously.
Wow, okay.
**Josh Suereth (Google LLC)** 04:44 Well.
I mean, we can keep pushing people at resolving from Git URIs, but I… yeah.
**Liudmila Molkova** 04:53 I mean…
**Josh Suereth (Google LLC)** 04:54 with packaging, let me know. It's just…
**Liudmila Molkova** 04:58 I've never seen that. Well, I've seen the output. I just never had a chance to test it out, and, like.
Since everybody would depend on what we produce in some conf, if.
The… there is no consumer for this thing.
But anyway, we can try.
**Josh Suereth (Google LLC)** 05:20 Yeah, I'd like to… so I'd like to try to get Weaver package stabilized. And I'd like to also get rid of the dash dash V2 for the definition syntax.
Not get rid of dash dash V2, sorry, get rid of the warning when you use dash dash V2.
**Liudmila Molkova** 05:54 Okay.
So this, I'm super comfortable with. Like, we could have done it in the previous release, I think.
Anyway.
And.
So… .
I wish we could produce the package from some kind of before we stabilize. Like, we can call it RC, but, like, we should produce the output.
**Josh Suereth (Google LLC)** 06:23 Yep.
**Liudmila Molkova** 06:24 and what's stopping us is.
a bunch of… Maybe we'll just… can we just jump into this one?
**Josh Suereth (Google LLC)** 06:38 Yeah, let's jump in.
**Liudmila Molkova** 06:40 I've… tried to switch semantic conventions, the entities, to something compatible with V2.
Entities didn't have identifying attributes, and I spammed the repo a lot. There's a lot of crap.
**Josh Suereth (Google LLC)** 06:57 Oh, cool, I was gonna look at this later, but it already exists. Yeah, no, no, that's great.
**Liudmila Molkova** 07:04 It is a can of worms, though.
So… What…
**Josh Suereth (Google LLC)** 07:10 of worms that we have to deal with. I think mostly some of the entities are actually attribute groups, I think is the problem.
**Liudmila Molkova** 07:18 Yes, there are… some of the entities are attribute groups, some of the entities are multiple entities.
Like, we have a… device?
And okay, so device and device ADE is probably the best example of the the can of worms.
Okay.
**Josh Suereth (Google LLC)** 07:37 God, you know.
**Liudmila Molkova** 07:39 Give me a sec.
So this looks amazing, great. The device entity should have identified an attribute device ID until you look inside.
So this thing is opt-in.
And under the assumption that it is, I… I'd say it's a… sorry, it contains identifying information for the machine, for the device.
And it's probably two different entities. One is, like.
Some device model, and the other one is device itself.
**Josh Suereth (Google LLC)** 08:24 Yeah.
**Liudmila Molkova** 08:25 But it is like there are maybe 10 similar.
And so we would need to split them up, or rename them to be more narrow, and so on.
**Josh Suereth (Google LLC)** 08:36 This is my straw man proposal.
All of the resource attributes that we define should be public resource groups first.
And then we can find an entity that pulls in the attributes from the public resource group when we're ready to model the entities appropriately.
**Liudmila Molkova** 08:55 Okay.
So, we would replace all the… The controversial ones.
Was…
**Josh Suereth (Google LLC)** 09:02 just.
**Liudmila Molkova** 09:03 Same data groups.
**Josh Suereth (Google LLC)** 09:04 Yep.
**Liudmila Molkova** 09:05 Okay.
**Josh Suereth (Google LLC)** 09:08 So, like, for device, it'd be like, cool, you can have a public attribute group that describes, I want this information. And then we can say we expect it on a resource with whatever matcher thing that Jeremy has now for things.
Yeah. Because that's basically what they were doing. They're not really modeling an entity.
But the kind of modeling entity, it's just, it's optional that they would report it, right?
**Liudmila Molkova** 09:33 Right. And the thing was not designed to be an entity anyway.
**Josh Suereth (Google LLC)** 09:38 Okay. Most resource attributes were not designed around, modeling the identity of something. They were modeled… they're just a bunch of crap that you throw on that's, like, labels you need to search for, which is like attribute groups, basically.
**Liudmila Molkova** 09:53 Okay.
**Josh Suereth (Google LLC)** 09:56 So that's my straw man proposal.
**Liudmila Molkova** 09:58 I like it.
It's also what, The feedback from Trask was, like, do we have to open the can of worms, and can we do something To… not do it right now.
At least for everything.
**Josh Suereth (Google LLC)** 10:16 Yeah.
**Liudmila Molkova** 10:22 But, okay, so I'll do this, and it'll get us, away from the terrible problems.
Then… We would I would have to suppress.
Some policies, because we were removing entities, and we are not allowed to, but we'll figure it out.
**Josh Suereth (Google LLC)** 10:45 Well, they're not stable.
**Liudmila Molkova** 10:47 Yeah, they're not stable. It's just that the policy will still complain. And the thing that I did last time, it… it only allows you to remove… suppress the refinement, like, so if you have a… if you convert something into refinement.
You can suppress.
**Josh Suereth (Google LLC)** 11:01 Oh, Do something where it got changed to an attribute group. Yeah. Okay.
**Liudmila Molkova** 11:06 Yeah, and there is nothing, like, to say that it used to be an entity with that name. Anyway, we'll figure it out.
But it brought up an interesting question that we don't have to resolve, but maybe we should anyway.
What are the requirement levels for the entities?
the entity identity. I kinda thought that maybe it's required, but maybe at least one is required.
Today, we don't validate anything. Opt-in… the single opt-in identity attribute perfectly… is perfectly fine for Fever.
**Josh Suereth (Google LLC)** 11:49 Mmm.
So… The reality is, for the identity attributes, all of them have to be required. There cannot be opt-in, right?
**Liudmila Molkova** 12:06 Either. Well, I can imagine that You could have…
**Josh Suereth (Google LLC)** 12:11 There's another bug for this, Ludmila. There's another bug for this from the entity SIG that I haven't gotten to, but I was going to remove requirement level from entity identity attributes completely, because they're always required.
And they cannot be… like, there is no scenario where they can't be required, you just don't report the entity.
That's… that's by the data model.
**Liudmila Molkova** 12:34 I… Does it mean, like… You only put into identity things that are always available.
**Josh Suereth (Google LLC)** 12:43 Yes.
**Liudmila Molkova** 12:45 Okay.
**Josh Suereth (Google LLC)** 12:46 That's… that's… that's the idea behind it, is it always has to be there, and if you can't dis… like, if there's an attribute that, like, you can't discover in all situations, you just fill it out with an empty string. But it has to be a required attribute for entities to hang together.
Like, you have to have the attribute there for the thing to hold together.
**Liudmila Molkova** 13:05 Okay.
So, we can either… Remove the requirement level from identity attributes, or… we would… Require it to be required.
And the first one is cleaner, and we better do it before the next release when we.
**Josh Suereth (Google LLC)** 13:25 Yeah.
**Liudmila Molkova** 13:26 Yeah, there's…
**Josh Suereth (Google LLC)** 13:27 That's, I was gonna get to this, and I forgot. It's in… if you look at our project thing, it's one of the, like, to-dos.
in the Weaver Project Board. Yeah, if you look at… I think it might be… Yeah, there you go. Disallow requirement level field in identity section.
**Liudmila Molkova** 13:44 Oh.
**Josh Suereth (Google LLC)** 13:46 Yeah, this was opened by Dimitri, like, a while ago.
From Entity SIG.
Almost a year ago, actually.
But we're at the point now where we can do it, because we decoupled everything.
**Liudmila Molkova** 14:02 Okay, and so this should be the next release.
**Josh Suereth (Google LLC)** 14:07 Yes.
**Liudmila Molkova** 14:09 Awesome.
**Josh Suereth (Google LLC)** 14:11 Because I think that's the last breaking change, and I think.
I think that's that should be the last breaking change to V2 definition.
**Liudmila Molkova** 14:23 The last one we know of.
**Josh Suereth (Google LLC)** 14:25 Well, The ones we don't know about no longer are allowed to be breaking changes.
**Liudmila Molkova** 14:32 Exactly.
**Josh Suereth (Google LLC)** 14:33 that's… That's what stability means. It doesn't mean you don't make changes, it just means you can't make them be breaking.
**Liudmila Molkova** 14:39 Yeah.
Just keep the compatibility.
**Josh Suereth (Google LLC)** 14:43 Yeah.
**Liudmila Molkova** 14:45 Okay.
And.
Cool, so with this, we would have a good future for entities, we would.
Convert non-entities in SEMCONF, who should be unblocked in SEMCONF.
And… we can start packaging.
And I'll get comfortable with stabilizing it as soon as possible.
So.
**Josh Suereth (Google LLC)** 15:18 So yeah, so to remove the warning, once we get the entity identity fixed, maybe we remove the warning on V2 and call it stable.
The definitions index.
So we would no longer make breaking changes to definition syntax.
**Liudmila Molkova** 15:34 Right. Oh, we have checks for this. We need to enable them.
**Josh Suereth (Google LLC)** 15:39 Yep.
**Liudmila Molkova** 15:55 Should we do an RC release?
purchased.
**Josh Suereth (Google LLC)** 16:00 No, because I don't want to do the full RC until stabilized… until package is stabilized, too. Like, I think we need package, actually.
usable.
**Liudmila Molkova** 16:09 I mean, like, it's probably, Very minor, but if you look… Yeah.
or Tulsa?
**Josh Suereth (Google LLC)** 16:21 Oh, yeah, that we would change. That we would call Release Candidate, sure.
Or move it… I'm actually fine moving it straight to release, but we can move it to release candidate, that's fine.
Yeah.
**Liudmila Molkova** 16:36 I mean, I don't mind moving it straight to stable, because either way, we would say we're not allowing breaking changes.
**Josh Suereth (Google LLC)** 16:44 Yep.
**Liudmila Molkova** 16:48 Thanks.
**Josh Suereth (Google LLC)** 16:49 And we can remove the, we can remove the callout that says, like, this is… you know, not yet stable and actively changing kind of a thing. We can have a call-out that says it might add new features, but not that it will be remain backwards compatible.
**Liudmila Molkova** 17:11 Okay.
Awesome.
Oh, right. This is the… another thing that's probably less pressing, but still, I wish we could solve it before we publish.
Some cons, V2.
that, I'd like to unref, and I implemented your suggestion, Josh, that, we cannot unref required attribute.
**Josh Suereth (Google LLC)** 17:45 Yeah.
**Liudmila Molkova** 17:47 Which should…
**Josh Suereth (Google LLC)** 17:48 I'm fine with that then because I think it fits the data model. So Laurent, for context, this is when you refine something.
You can mark an attribute that says, actually, my refinement can't use this either recommended or optional attribute.
And so it doesn't show up in the docs at all. I like this. I think unref is fine as a word. I wish there were better names.
**Liudmila Molkova** 18:12 Well, I can give you a couple of other ideas.
**Josh Suereth (Google LLC)** 18:15 Oh, I'm sure there's a whole bunch of worse names. I'm, I'm absolutely positive of that, but I think unref is fine, yeah.
**Liudmila Molkova** 18:21 Okay.
**Laurent Quérel** 18:24 Yeah, makes sense for me.
**Liudmila Molkova** 18:28 The idea I entertained, I have to tell you. The requirement level, not applicable.
**Josh Suereth (Google LLC)** 18:35 Oh.
**Liudmila Molkova** 18:36 Dan, the…
**Josh Suereth (Google LLC)** 18:38 I thought you were gonna say delete. Delete would have been an outright no for me.
**Liudmila Molkova** 18:42 Okay.
So, a little bit better.
Well, I… anyway, so I think it won't fly, mostly because I don't want requirement level to be super different across… Everywhere.
Okay, so then I would appreciate reviews, and… the,
**Josh Suereth (Google LLC)** 19:08 Cool.
Yeah, I'll take a look then, and… That… that looks like a good fix.
**Liudmila Molkova** 19:14 Thank you.
**Josh Suereth (Google LLC)** 19:18 I didn't add this to the notes, but the PR that Laurent and I reviewed yesterday, can we talk about that briefly, out loud? If you look at open pull requests, we have a few from people outside the community, and some of them are actually pretty good.
It's the cache git registries on disk across invocations.
So I think I don't remember if the author got back to us yet or not because I didn't check.
**Laurent Quérel** 19:42 No, I don't think so.
**Josh Suereth (Google LLC)** 19:44 Okay.
This is actually a pretty cool change. Basically, what it does is it makes a Weaver cache directory, so when you check out a Git repo, that Git repo sticks around, and then you have an offline mode where you can basically say, don't hit the internet and resolve everything.
But it could lead to, like, you know, disk slash performance improvements, especially for slow internet, where you don't have to download repos all the time, because you have them cached locally. I think when we get to the point where we are packaging and publishing.
schema URLs, and we're downloading that file. This is… Actually less important?
But we're not there yet.
And there were a few concerns I had with this, but I want to go over the… if you can find my comment at the top.
I wanted to go over this right here, a few suggestions. So, A few thoughts around this.
What is… I want to kind of outline, if we were to do a cache.
what do we think we want that to look like from a user perspective? Because from my mind, we can evolve a cache over time, there's a lot of things going into a cache that are problematic, but I want to agree what we think it would look like. So, my thinking is there would be a Weaver cache directory.
That would be the cache by default.
You could specify a command line flag that could change where the cache is if you want, but we would say, here's a directory where we'll cache things we've resolved remotely for you.
There would be a dash dash offline flag, which if you cap, if you pass that into Weaver, we want to consistently everywhere not reach to the public Internet for anything.
Right?
So that would be… that's the idea… like, I think that that capability is something we probably want to have as, like, a global flag for Weaver, for, like, all… Operations of Weaver.
And then the last thing is, here, the… there's this notion of ignoring the cache, so this is… even if you have a cached access, I want you to ignore it and pull in fresh.
This is used to, like, reseed a cache, or deal with, like, cash key problems?
it's basically your escape hatch for if your cache is broken in some fashion. So, anyway, I wanted to propose, like, if we agree that those three things make sense across Weaver, the whole thing, like, in live check, not in live check, that kind of stuff.
I think that can help us unblock this PR pretty quickly.
With that. And then… So, let me end my comment there. There's more in my comment above that we can go through, but I wanted to first check that with everybody.
**Laurent Quérel** 22:29 Yeah, like I said in my comment, I totally agree with your… feedback.
I dig into the code a little bit more. I think there are multiple issues.
But they are not fundamental issues.
And I think he will, be able to align very quickly with the recommendation you did.
But for me, there are issues like, The possibility of having two weavers running at the same time, basically consuming, a partial registry.
There is nothing preventing the… preventing, in fact, the consumer.
an atomic, non-atomic Snapshot.
There is no concept like that in the implementation that this hotel did.
So, that's what I recommended to.
To follow in terms of principle, making sure that when you start to consume A directory, subdirectory of the cache.
You always get the entirety of it, and not.
something that has been deleted by another instance of Weaver, or that has been replaced by another instance of Weaver.
Yeah. Otherwise, you will get something that is partial, or something that is a mix between two versions.
**Josh Suereth (Google LLC)** 23:54 That's a good call out, I remember, in the build tool that I used to work on.
We had a lot of code and tests around file locking for our CAP.
**Laurent Quérel** 24:05 Ashka.
**Josh Suereth (Google LLC)** 24:05 directory. So we could make sure only one person was mutating the cache directory at a time, or that you could take out a lease for like a particular file.
And my favorite is that file locks.
exist… But they're a pain in the ass in practice, particularly in Windows. You always have to deal with an issue where a process died but didn't leave its… like, didn't clean up the file lock, and it's just sitting there dangling.
And you needed to not break things. So there's, like, all of these, like, weird scenarios around caching that we'd have to deal with when we add a cache.
And I'm comfortable personally with, like, okay, if we have a good escape hatch.
That people can use to work around the cash.
We could add it as an optional thing initially, but if we agree to what it should look like generally, I'm okay having someone contribute and evolve it over time.
to figure out all those different scenarios and what that looks like. Like, to me, I'm comfortable with that as, like, a direction forward. I think we need to agree that we want a cache.
And.
**Laurent Quérel** 25:13 Yeah, totally.
**Josh Suereth (Google LLC)** 25:14 How much it impacts, yeah.
**Liudmila Molkova** 25:16 I have stupid question.
Caching something remote makes sense. Caching local.
Doesn't.
**Laurent Quérel** 25:27 Or there is no cache for something local.
**Josh Suereth (Google LLC)** 25:29 Yeah, it doesn't cache local, it just caches the remote stuff, yeah.
**Liudmila Molkova** 25:32 Yeah, yeah, I didn't ask my question yet. So if it's the remote only.
Then remote only is schema URL and unique and immutable.
And it reminds me of the package caches.
Please, let's not invent the virtual environment in Python, but the… are, like.
we don't want to do NPM either, but we can probably learn from them. And I don't think they have, like, I didn't remember… I don't remember having, like, terrible File locking issues there, because things are immutable and versioned and structured in a certain way.
**Josh Suereth (Google LLC)** 26:13 They do do some level of locking, though, and they also, like, with NPM, the cache is local to a directory.
As opposed to, like… so the caches I worked with in the past were, like, Maven, and SPT, and Gradle.
And there, you're trying to share a cache globally for the whole… Like, laptop, if you will, or VM, or whatever.
But, yeah, there's still… how do I want to phrase this? I think we should learn from those things and not reinvent the wheel. It's just, I know that that space is really complicated in practice. There's a lot of subtleties, and you have to go into it with knowing what they are, yeah.
**Liudmila Molkova** 26:57 I understand, it's just if we design the structure of this cache.
in a way, that's.
displayed by the version and artifact and registry by schema URL.
For most cases, the locking issues wouldn't matter, because they are… things are immutable. We only need read-only access to them.
**Josh Suereth (Google LLC)** 27:19 You still have an issue where the file's half-written and someone tries to write it. So you still have to lock in some fashion. Because, like, you can have a process that's reading while you're writing. Or you could have two processes try to overwrite the same file at the same time. Like, you still have to lock there.
**Liudmila Molkova** 27:36 Okay, you…
**Josh Suereth (Google LLC)** 27:37 Yeah.
**Liudmila Molkova** 27:38 It's just that the main case is that you run Weaver.
And the only race condition, if you run multiple ones, and they try to cache at the same time.
**Josh Suereth (Google LLC)** 27:49 Yeah, yeah. So it's kind of a startup risk, yeah.
**Liudmila Molkova** 27:53 Yeah, but then it's not a race cluster.
**Josh Suereth (Google LLC)** 27:56 No.
**Liudmila Molkova** 27:58 And so, like, the exposure to the problems is pretty minor.
**Josh Suereth (Google LLC)** 28:04 You, you say that.
**Liudmila Molkova** 28:06 Okay.
**Josh Suereth (Google LLC)** 28:07 But from experience building a cache and maintaining it with immutable artifacts.
you run into them more frequently than you'd expect, particularly with, like, build servers. Like, you know, they're doing a crap ton of stuff there, and Yeah, it's… it's… It's not that… it's not… they're… they're particularly hard problems, it's just they're tricky, and you have to actually account for it, or pay attention to it. And if you don't put any safety in from the get-go, you're guaranteed to run into the problem.
**Liudmila Molkova** 28:40 This I agree.
**Josh Suereth (Google LLC)** 28:41 Yeah.
And, you know, there's a ton of code out there that we can just curb if we need to, like, handle all the locking or cleanups or whatever. We can decide… this is why, in my opinion, there's, like, 3 decisions we have to make that are super critical.
One is, we decide if… where the cache directory lives. Is it going to be per machine, per user, or per project, right? Node… npm does per project.
I actually think we should do per machine, because that's kind of what we're doing already. We're doing, like, a slash temp, I think, or per user, I should say. We put it… we put it there. I think that's a little bit better. Then we pick a cache key. The cache key is the thing that I was most worried about when I dug through this, because the cache key wasn't stable. So we're saying schema URL is the stable thing, right?
Here, the cache key was the virtual directory reference. Oh, by the way, Ludmilla, this cache is more than Scheme URL, this would cache Weaver packages as well.
So this would… this would cache, like, the Weaver package download for policies.
**Liudmila Molkova** 29:44 Oh.
**Laurent Quérel** 29:45 A Git URL, for example.
With a tag is not immutable. I mean, there are many ways for this thing not being immutable at all.
**Liudmila Molkova** 29:55 The Khamid Shah.
Is is a mutable.
**Josh Suereth (Google LLC)** 29:58 MetShot is immutable. The.
**Laurent Quérel** 30:01 And that's the key that I. TAIG is done.
**Josh Suereth (Google LLC)** 30:04 Yeah, so, like, one of the things that we want here is if we pick a cache key, the cache key should be the immutable thing.
And then, when we look something up, we have to basically say, okay, cool, you want this URL. This URL, let's go resolve… what the actual commit SHA of a tag is, in some fashion, first, then we know if it's in our cache.
**Laurent Quérel** 30:26 Yes.
**Josh Suereth (Google LLC)** 30:27 And that's a thing that has to get sorted out on this, because that's actually a bit of complicated logic.
If the remote URL is a schema URL and you downloaded the file, great, cool. You just, like, that's simple, that's easy. But when it's, like, the Weaver packages repo, you'd have one cache URL for the whole repo, and then you can reference the subdirectories from it and use it… use them all from the same cache, but you have to do that resolution.
But that… yeah, anyway, the concurrency around touching the cache is something we have to, like, work on.
So, yeah, okay, cool. I think… The general gist, though, is, do any of us have concerns adding a cache to Weaver? Like, do we think that would be something we wouldn't do at all?
No? Okay, cool. So let's keep shepherding this one, let's get a set of principles down. What I don't know is, a lot of the code looks to be somewhat AI-generated, right?
And so… the thing I like about this PR, which I think is higher quality, is there's a set of docs, it's well documented of what the decisions being made are, and that sort of thing. So I think if we can get those decisions we just talked about into the codebase, then the AI flywheel will start to be faster and be more efficient and involve less review. But we have to get, like, the concerns we talked about kind of written down, you know?
**Laurent Quérel** 31:52 Yeah, and that's fine, my comment. I think.
Hopefully, the user knows how to use this AI, and it will read the command directly into the PR description.
Yeah. And your comments and my comments, I think they are relatively well detailed.
We can probably complete that with maybe one or two missing pieces, but I think it's… that's exactly why I try to… To make those comments as much as, precise.
**Josh Suereth (Google LLC)** 32:26 Awesome.
Okay.
Cool. I think there was one other PR I wanted to take a look at together, if we can.
Because I wanna… I wanna, like, my context is I want to keep encouraging, folks to… contribute, so I want to be fast and responsive to this. User-provided JQ modules. I think this one's ready to merge.
And you didn't know.
**Liudmila Molkova** 32:50 Prove.
**Josh Suereth (Google LLC)** 32:51 Did I not approve?
What did I write?
Oh, right, he added an integration test, and I haven't approved it yet.
Did I not approve this after I re-reviewed it? Oh my god.
Okay, I thought I did.
I think this one's ready to go.
they added a new integration test that actually shows how this is used. I think this is really good. But I wanted to run through, I think this is another one where there is some decisions made.
Around, like, the interface for Weaver. So, it's in Weaver config, yeah.
You, inside of your Weaver config, you can add new JQ modules that are used for your local template.
And they get pulled in.
**Liudmila Molkova** 33:38 Oh, are there, like, functions?
**Josh Suereth (Google LLC)** 33:40 Yeah, like, you can define options or whatever.
Yeah.
**Liudmila Molkova** 33:45 That's awesome.
**Josh Suereth (Google LLC)** 33:46 Yeah, I think… I think this is awesome. Like, I… I… and what… the… the reason I blocked it at first was there was no tests.
**Liudmila Molkova** 33:54 that.
**Josh Suereth (Google LLC)** 33:54 that showed… sorry, there were tests, but there weren't end-to-end tests or, like, human-readable tests. Now you can literally see, like, he has a test that has a JQ module package, he has the Weaver XML, so you can see it working, like, it's a more human-readable test, so I wanted to get this one through.
**Liudmila Molkova** 34:10 So good.
**Josh Suereth (Google LLC)** 34:11 Isn't it? Yeah. So I wanna get this one through. I just wanna check to see if anyone had any concerns. I thought I had approved this, like, two days ago, but I must not have clicked the submit button.
I bet I have a review that's, like, pending.
**Liudmila Molkova** 34:28 Finally, we don't have to read JQ inside YAML.
There could be a syntax highlight. You can run it in the sandbox, in the playground.
**Josh Suereth (Google LLC)** 34:39 Yeah, exactly.
**Liudmila Molkova** 34:40 Yes.
We can do the modules and Vivr packages if… In the future.
**Josh Suereth (Google LLC)** 34:49 I know, like, this is huge, this is big, let's, let's, okay, cool. If no one has concerns, I'll approve and merge that then. Or, Ludmilla, if you want to just approve and merge it now, feel free.
**Liudmila Molkova** 35:01 I didn't read the.
**Josh Suereth (Google LLC)** 35:03 You didn't read the code, that's fine. I will… I will do the approval and merge, then. Cool.
What else do we have going on? Was there any other, like, user-contributed PR we want to review or look at?
**Liudmila Molkova** 35:16 That's true.
Just manage this front.
**Josh Suereth (Google LLC)** 35:28 We'll just have to get some Renovate things through.
**Liudmila Molkova** 35:30 Benchmark, Rigo, I think Jeremy… Try to work on this with the other.
**Josh Suereth (Google LLC)** 35:37 Yeah, it has a bunch of merge conflicts, so it's actually not mergeable at all right now.
**Liudmila Molkova** 35:43 Okay.
**Josh Suereth (Google LLC)** 35:44 Yeah.
**Liudmila Molkova** 35:46 Alone.
**Josh Suereth (Google LLC)** 35:49 What did Jeremy say, though? I forget what his last thing was, oh, right,
**Liudmila Molkova** 35:59 Parks for a while.
**Josh Suereth (Google LLC)** 36:12 Yeah, I think this is one where we should probably respond with how we're planning to do performance work, so that they can contribute.
**Liudmila Molkova** 36:19 Yeah. Do you know the context? I don't.
**Josh Suereth (Google LLC)** 36:23 So, basically, LiveCheck was built to be functional.
**Liudmila Molkova** 36:30 but.
**Josh Suereth (Google LLC)** 36:30 But there's a few things that we know we need to change in LiveCheck as part of V2, so we're… like, he's… Jeremy's in the process of gutting it architecturally.
One of those things was the matcher syntax, right?
But then, you know how we added the cash so that we can actually, like.
dynamically load in different schema URLs, and LiveCheck would be able to use more than just the one you specified on the command line. It could, like, dynamically load things.
there's… there's a whole slew of features where we want to change. This is also why we don't want to, put our crates on Crate.io, because we're planning to go through and actually change all our public interfaces across the crates.
To optimize for whether we use references, whether we're, you know, thread-safe, whether we're send and sync.
All that stuff we want to change. Right now, everything is a clone.
Everything is send and sync always. We don't use ARC, so we're copying data like crazy. Like, there's a whole bunch of performance work that Jeremy and I wanted to kind of tackle over time.
probably, like, I would start with the resolver, continue with the resolver, and he would do the live check things. So that's why it was like, okay, you can benchmark stuff now, but in terms of the optimizations you're doing, you're optimizing an architecture we're planning to gut from under you.
So that… that was… that's the context here, I believe. Basically, like, hey, maybe… maybe we don't want to benchmark Rego just yet, maybe we'll benchmark it once we get to the more final architecture. That said, this isn't… this isn't a lot of.
It's not a lot of code here.
**Liudmila Molkova** 38:10 Not at all.
And then it is the… Essentially, the… the benchmark.
**Laurent Quérel** 38:16 Yeah, it's just a benchmark.
**Josh Suereth (Google LLC)** 38:18 It's Criterion, yeah.
I do think maybe this can go in now that, all of the new advisory stuff has changed, but we could check with Jeremy.
**Liudmila Molkova** 38:32 Let's put it into the next…
**Josh Suereth (Google LLC)** 38:35 Yeah, regarding criterion and, benchmarking in general, I do want to get some of that set up so that we can have long-term benchmarks around like the key pieces of Weaver, like the resolution engine.
One thing I've been really successful with, I don't know if you've done this, Laurent, but when you have criterion with a baseline.
Then you make sure you have enough integration tests, and overall tests.
Then you just throw, hey, Gemini, or Claude, or whoever.
go take this… Benchmark, and make it as small as you possibly can.
Okay.
What I what I normally do is I don't say as small as you possibly can. I say, like, this currently takes, you know, two hundred milliseconds. Make it a hundred.
And then just see what it does.
And if you have the bounds around it correct, like, if we have the right set of integration tests, if we have the right set, and we… you force it to actually run integration tests and Clippy and all that between every phase, but you have that baseline criterion, I've had really good success.
**Laurent Quérel** 39:45 Oh, yeah.
**Josh Suereth (Google LLC)** 39:46 dress code.
**Laurent Quérel** 39:47 No, you don't.
**Josh Suereth (Google LLC)** 39:47 Success. So I, I think we might want to to do that, like take a round of that at some point. I don't have enough tokens right now with my Claude, but I might try that with Gemini, see how that goes.
**Laurent Quérel** 40:01 Yeah, definitively, we are using this technique.
or attitude often. And also the slash goal that exists in Claude or Codex, or something like that.
Where you can precise… like you said, if you have a good, set of guardrails.
to make sure that the AI will not go.
In any direction that are not controlled.
And then you specify a goal, like a function to optimize. It could be the minimizing the memory, minimizing the CPU usage, both of them, whatever is the… The targets, yeah, it's working very well.
Yeah.
**Josh Suereth (Google LLC)** 40:46 Okay, so that might be part of this. We can talk about that later.
I think that was the last, like, PR to take a look at in this repo.
**Liudmila Molkova** 40:58 There's this friend as well.
We're all gone, we never…
**Josh Suereth (Google LLC)** 41:02 you We've never even…
**Liudmila Molkova** 41:04 And looked at it.
**Josh Suereth (Google LLC)** 41:05 Wait, wait, is this the one with the at?
**Liudmila Molkova** 41:08 Yeah.
**Josh Suereth (Google LLC)** 41:10 I thought I made comments on here, did I not? Or is this a new one?
True.
**Liudmila Molkova** 41:15 Another one, no comment.
**Josh Suereth (Google LLC)** 41:20 Can you look at files changed? Is this… is this a reopen of an old one, or is this one that we commented on in a meeting and never wrote on the document?
Oh, right. I I did review this and I didn't like it, but I is this a new PR of that or not?
**Liudmila Molkova** 41:46 It's from August 19.
Oh, wait, there is…
**Josh Suereth (Google LLC)** 41:51 Yeah.
**Liudmila Molkova** 41:53 There's an issue, maybe you commented… no.
**Josh Suereth (Google LLC)** 41:56 I didn't I thought I did.
**Liudmila Molkova** 41:58 Oh, wait, so somebody created an issue in July.
And then…
**Josh Suereth (Google LLC)** 42:04 to fix the issue.
**Liudmila Molkova** 42:05 Right, and whether they are fixing it because they care, or they are fixing it because they have tokens to spare, that's a separate question.
**Josh Suereth (Google LLC)** 42:14 Wait, look at the, there's another one below.
So, the… what's the one that was 4 days ago, that one? Is this a different… is this a different one?
**Liudmila Molkova** 42:27 Where it goes to the sad.
Results to spend.
So, I think…
**Josh Suereth (Google LLC)** 42:42 Interesting. Okay.
I mean, these are things we should fix. The @ one, though, the actual fix, when I first saw it, looked sketch.
Can you go back to it?
Right, it, like… Some of the… some of the starts with and URL things I was a little nervous about.
**Liudmila Molkova** 43:08 Oh, I see.
**Josh Suereth (Google LLC)** 43:10 Yeah, like, it… I don't know if this actually… I need to figure out how to comment what I'm saying, but I, like, this one actually makes me more nervous than anything else. So if you look at his registry path, where he wants, like, tempfu at bar slash model, that kind of crap.
That's a little, like… I.
we need… I think this… this… Jeremy and I talked about this when it was just Jeremy and I, because when this came in, and I think it's in our meeting notes of, like, we were like, oh yeah, we should get a formal parser here.
for…
**Liudmila Molkova** 43:46 URLs.
**Josh Suereth (Google LLC)** 43:46 Like, this is… like, doing this kind of stuff, I actually don't think we want to do, because I think this might open up more bugs than it solves.
**Liudmila Molkova** 43:54 So we would try to parse the URL, and if it fails, we assume it's not, or we would use the library functions to say if it's a local path.
**Josh Suereth (Google LLC)** 44:02 Right, because using a regular expression and just constantly, like, updating the regular expression for random shenanigans over time, eventually we're gonna end up with a full parser. So, like, why don't we just use either a URL parser or a Git parser, and then when we find an at symbol, right?
Like, we… Then we would handle it in that, like, subpath of the parsing stack, but… We, we have this, hierarchical problem with, with our URLs, if you will, you know, where if it's http, sorry.
**Liudmila Molkova** 44:36 Give me a sec.
I.
**Josh Suereth (Google LLC)** 44:37 Oh, you're trying to type what we're saying? Oh, okay.
**Liudmila Molkova** 44:39 No, no, no, I'm trying… I need to take care of a kid for a sec, sorry.
**Josh Suereth (Google LLC)** 44:43 Okay.
Yeah, what do you think here, Laurent?
**Laurent Quérel** 45:08 For this specific, thing? I try to remember, because I think I wrote this code. The initial one.
On the left.
Try to remember why I didn't use the URL.
Great.
And maybe it's because… URL was expecting to see encoded… Aerobus or Bracket, maybe. I don't remember exactly the reason, but I'm surprised not using the URL trait in this specific case.
**Josh Suereth (Google LLC)** 45:42 I think you use it later.
**Laurent Quérel** 45:44 Okay.
**Josh Suereth (Google LLC)** 45:45 Like, basically what we have going on is we're trying to differentiate, is it a Git URL?
Is it a local file, or is it a, actual URL?
**Laurent Quérel** 45:54 Yeah.
**Josh Suereth (Google LLC)** 45:55 And… like, the reality is, when you parse that, I think the only ambiguity we can actually handle is it's either a Git URL, or it's either a URL that could be Git with some extension-y crap that we have.
**Laurent Quérel** 46:08 Mmm.
**Josh Suereth (Google LLC)** 46:09 Or it's a file.
And so this is URL… I thought I had comments on this already that said, like, don't use a regex here, use the URL library that we have.
That might be a different Pr. That I commented that on.
Okay.
**Laurent Quérel** 46:32 Yeah, if it's used after, yes, I totally agree, the ease URL could rely on the URL traits.
**Josh Suereth (Google LLC)** 46:39 Yeah.
But, I mean, the reality is, I think the… Two things… two things showed up in my mind from this. One is the VDIR, like, documentation for what is a valid virtual directory. We don't actually have that in our public docs. We only have it in Rust.
So I think we need to make a public doc of what that is, and we should specify how we parse things there, and have a formal spec.
And then this would implement that formal spec, and I'd be more comfortable with that. But just adding shenanigans here and there with, like, regex parsing and stuff, this is fraught with peril. Like, this is one of those areas where it's gonna be this never-ending churn of bug fixing over and over every release of Doom until we actually, like, solve it.
at least in my experience, this is one of those things that I'm afraid of with VEDAR. So, I would rather have, like, a proper URL parser, and then make sure we know which space of VEDA we're supporting. So, are we… is this a HTTP Git URL path? Is this a file path? And maybe when we land on the file path case, we allow at in different ways, but… If we can't define that formal parser for, like, how we parse and make it consistent and understandable for humans, it's problematic.
So, I'm not a huge, I'm not a huge fan of local paths with that, basically.
Like, we could say, sorry, we don't support local paths with that.
It could be that we add an escape mechanism where you can treat that whole thing as a file.
and you don't hit the other parser, right? But that means we have to write formal rules for when that happens. But I don't want to just have shenanigans that guesses and says, oh, this at… obviously isn't a URL, you know? We… like, I'd rather have a formal, like, people know, the same way when you write syntax in, like, a language, you know if the at is some symbol that is used appropriately or not. Like, it should be obvious to the user the behavior of the at symbol.
From Weaver.
**Laurent Quérel** 48:38 them.
**Josh Suereth (Google LLC)** 48:39 And if it's not, I think it's problematic. So this one is just too magical for me, basically.
**Liudmila Molkova** 48:52 Okay, I'm going to leave this comment. If the author comes back, awesome.
I don't know how to…
**Josh Suereth (Google LLC)** 49:00 Okay.
**Liudmila Molkova** 49:01 Formalize all the requirements. Well, I know, but we'll see.
**Josh Suereth (Google LLC)** 49:05 I can take a crack at commenting on it, too.
I thought I had, but that's my bad, I must not have actually written down anything.
**Liudmila Molkova** 49:14 Yeah, and it seems there's a group of issues around this, which… As you pointed out.
**Josh Suereth (Google LLC)** 49:21 This is why I think that… I think that all the group of issues around the virtual directory path, which is why I want to make a specification for it.
In docs that says exactly how to use it. And then, when people make changes, instead of just making changes to the code, we actually look at the spec… like, the user docs first, and we look at the behavior users expect.
Because all these, like, I'm gonna change VEDAR, I think there's a problem where, you know, you throw in a fix, and you don't know if it has rippling implications on the other usages of theater.
I could call it virtual directory, by the way, if that's better than VDIR, I don't know.
**Laurent Quérel** 50:01 Beside.
**Liudmila Molkova** 50:29 Okay.
Cool, that's it! I think this is the older user… Oh, external contributions. We have oh, Docker build cache. I think it's essentially the same cache.
**Josh Suereth (Google LLC)** 50:49 I think it… Oh, no, no, Docker build cache is the same cache as what?
**Liudmila Molkova** 50:55 So I think it solves the same problem.
**Josh Suereth (Google LLC)** 50:58 No. So, if we…
**Liudmila Molkova** 51:00 If we had a cache.
**Josh Suereth (Google LLC)** 51:01 Shake.
**Liudmila Molkova** 51:03 If we had a cache.
**Josh Suereth (Google LLC)** 51:05 Yeah.
**Liudmila Molkova** 51:05 Oh, Docker build cache.
**Josh Suereth (Google LLC)** 51:08 This is for building Weaver itself. This is for our CI. Yeah, we had an open… this is another one where I think someone picked up an issue that's been on Weaver. It's basically to speed up our own GitHub actions and make them more efficient.
So this is, I think someone picked this up, but our GitHub actions are somewhat inefficient with how we use Docker, because we're not using caches appropriately for the Docker pieces of our build. So this would be, like, if we can actually cache Yeah, so he's adding caches for the Docker build itself for when we publish Docker. So we're not rebuilding our baseline layer images. We're only building the Rust code that's changed. Yeah.
**Liudmila Molkova** 51:44 Is there any controversy in this at all? Like, why didn't we review it?
Medicares?
**Josh Suereth (Google LLC)** 51:51 No, I reviewed it, but I didn't have time to look into the implications. It's more… We could approve it right now.
It's untestable until we cut a release.
The other thing that I'm concerned about that I need to look at or ask, this does increase the amount of caching that we have for Weaver.
Right?
And what's more expensive? The amount we pay for the caching gigabytes, or the amount we spend on GitHub Actions when we cut a release once a month?
I don't know.
**Liudmila Molkova** 52:27 Oh, I see this. I so, essentially, the concern is the the release time doesn't matter, because we are doing it once a month, and nobody actually anxiously waits for it to finish. And the caching wouldn't help because what are you caching for?
**Josh Suereth (Google LLC)** 52:47 Although this might be caching the test as well. Like, if you see there under steps, you see how it's under run, like, name test? I think it's caching the test… that we do to make sure the Docker build succeeds on every PR. So this might actually… this might be worth it.
**Laurent Quérel** 53:05 Definitively, on our side for Hotel Hero, we… Definitively improve that multiple times, because that's.
When you have many, many PRs, and it looks like in Weaver, we start to have a lot.
That's not to make sense.
**Josh Suereth (Google LLC)** 53:21 Okay. Yeah, I feel like we could probably add it. I just, again, I didn't have time to look through it, and the other question is, did I… I think I approved this to run.
It did run through all its checks, right?
**Liudmila Molkova** 53:34 it.
**Josh Suereth (Google LLC)** 53:35 Yeah, okay, because when I first looked at it, it hadn't run all of its checks. You have to have, like, a maintainer approve it, so I had it run the checks first, and then I forgot about it. That's probably what happened.
**Liudmila Molkova** 53:45 Yeah.
Actually, the Copilot is pretty good at identifying at least syntax issues and the validity of the GitHub actions. So if it… Doesn't find any problems, we can just approve it, and let it be, and if it doesn't bring up any performance improvements, we either want notice where we can revert it.
**Josh Suereth (Google LLC)** 54:12 Okay.
**Liudmila Molkova** 54:18 Anyway, we are at almost the time. I can monitor its progress and… Approve it if it's fine.
On.
Otherwise, good to see you all.
**Josh Suereth (Google LLC)** 54:34 Yeah?
**Laurent Quérel** 54:34 Yeah.
Have a good day.
**Liudmila Molkova** 54:37 video.
**Laurent Quérel** 54:38 Right.
