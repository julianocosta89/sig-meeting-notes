SIG: Semantic Convention Tooling
Date: 2026-09-16
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Josh Suereth (Google LLC)** 00:23 Hey.
**Liudmila Molkova** 00:28 Oh, hey…
**Josh Suereth (Google LLC)** 00:30 Sorry, I was late.
**Liudmila Molkova** 00:32 It's okay, I just joined.
**Josh Suereth (Google LLC)** 00:34 Will we get to have a one-on-one for a bit.
**Liudmila Molkova** 00:37 Yeah, recorded, yeah.
**Josh Suereth (Google LLC)** 00:40 It's all good. I'm used to everything I do being recorded now. I have the worst merge conflict from your PR.
somewhere.
**Liudmila Molkova** 00:48 I can do it.
Sorry.
**Josh Suereth (Google LLC)** 00:50 No, you would have had it with mine, like, it's fine.
I'm throwing tokens at it, but then we'll go figure out if it did anything stupid, but it's, what did you think of the V2V1 stuff? Like, is it… do you think it's… too over the top? Or will it help eventually?
**Liudmila Molkova** 01:11 Which part? What is over the top?
**Josh Suereth (Google LLC)** 01:15 Oh, the PR that you reviewed for me, where… what's over the… what's over the top? The fact that I… I literally have a skill with a Python script that looks for any directory with V1, that has an import with V2 in it, it does a grep.
And I have anything with V1 that has an import for V2, and then it also flags every single file that has an import that has both V1 and V2 in it.
And, like, lists all the files out, so I can track where they are. If they're in convert.rs, they're fine.
And then there's specific, like, pieces of infrastructure where it's like, okay, cool, like, these are fine, but I've been trying to minimize it. So, like, LiveCheck is almost all on V2 now, or it has those V1, V2 things.
So, I did a full audit, and I'm down to, like… there's, like, 4 or 5 places that are… To detangle at some point.
But I'm not quite at, can I gut Weaver Resolver and have a V1 and a V2? I'm not there.
so close, like, I'm so… It's gonna be the worst PR ever when I make that one.
But that's been my goal, is to get to the point where, like, V2 resolution has a V2 section, and V1 resolution has a V1 section, and we're not doing all of it blended together in Doom.
**Liudmila Molkova** 02:35 We will stop doing W2 to V1 conversion.
At all.
**Josh Suereth (Google LLC)** 02:39 Yeah… Cool. I want to get there. Yeah, I'm like, I'm close… so first I'm doing the detangling, and making sure we have the interfaces.
Anyway, we're… it's… it's the same thing that LiveCheck has, where it has, like, V1 and V2 wrappers.
We just do that in the resolution.
But we actually have to delegate to know if it's a V1 thing that we actually resolve differently, so the algorithm can actually diverge between the two.
And I don't know if I'm happy about that, or really happy about it, you know what I mean? Like, because… I think it'll be a lot clearer, the semantics and everything.
**Liudmila Molkova** 03:21 Yeah.
I didn't… This… this is… Very tangled today.
I mean, I don't think you're over the top.
**Josh Suereth (Google LLC)** 03:32 Okay.
I… you're the one who has to look at the code, so that's why… I mean, I have to look at it too, and I'm kind of cringing a little bit.
**Liudmila Molkova** 03:41 I mean, it's rust code, of course you're cringing.
I still don't… I still don't understand Rustcod well. I… just when I see it, I don't… I need to think.
**Josh Suereth (Google LLC)** 03:57 So, this is how I feel when I review the conformance repo, because I can't read the Python. Like, it… it's all arcane magic to me. Like, I understand what the code is saying it does, but half the things are just magical.
I haven't been paying attention enough, I don't know what the hell they do. I have to ask a… LLM to tell me, like, what the hell is this function doing, why does it exist, that sort of thing. Because I… And Python, to me, is really hard to follow.
**Liudmila Molkova** 04:25 I agree, the Python is also hard to follow.
Well… I mean… C-sharp is the best language ever.
**Josh Suereth (Google LLC)** 04:36 No, my favorite was always Scala, but there's a… there's a… That'll tell you why I like Rust. Alright, anyway.
We should probably talk about useful things. I… I think we're gonna call it short today, because I don't think we're gonna have a lot of people.
Ariana couldn't make it.
But her PR is merged, conflict merged and ready.
I am now doing the new… like, tabs on the left instead of at the top, so I literally suck at controlling my computer, because I'm trying to learn it.
Have you… so I don't have the notes up or anything. Have you… have you used this yet, by the way?
**Liudmila Molkova** 05:20 No, I haven't.
**Josh Suereth (Google LLC)** 05:23 It's…
**Liudmila Molkova** 05:23 I… yeah.
**Josh Suereth (Google LLC)** 05:25 I'm… I'm losing less tabs.
Like, they don't disappear on me, right?
But I… It's like that, like, mental friction where it's just consuming so much brainpower to remember to look on the left, or move things on the left, and all that kind of stuff. I don't know why.
Alright.
**Liudmila Molkova** 05:46 Yeah, I… I converted to Mac recently. I feel your pain. It was the worst transformation of my life.
**Josh Suereth (Google LLC)** 05:57 I'm thinking about, switching to Windows.
Actually.
And, yeah, I just lost all credibility with OpenTelemetry, probably.
Or maybe not open telemetry, but open source in general.
**Liudmila Molkova** 06:13 How is it related to Windows?
**Josh Suereth (Google LLC)** 06:16 Oh, just in my previous days with open source, it was… you either were a super nerdy Linux person or an OSX person.
There was no windows.
**Liudmila Molkova** 06:27 Yeah. Huh.
It kind of sucks.
was especially… Well… You either use Docker or you use WSL, and then… You… it's slow, regardless.
**Josh Suereth (Google LLC)** 06:45 Okay, so I wanted to go through the… a little bit of the PRs, if that's okay. Sorry, I'm, like, already…
**Liudmila Molkova** 06:52 Ehh.
**Josh Suereth (Google LLC)** 06:53 I only have, like, 20 minutes, so I want to use our time wisely.
I have to bail a little early today. So, refactor live check to combine OTLP and admin flow from Jeremy. We'll have to… that one, I think, is super critical to review and get through.
I haven't had a chance to look through it, but that's… that's on my list. Cache Git registries on disk across invocations. I need to take a look at this one. Did you see this?
**Liudmila Molkova** 07:19 I've seen this, so I didn't have a chance to review.
A way of… yeah, give me a second.
**Josh Suereth (Google LLC)** 07:27 There's some shenanigans in here. They said that they were using AI to help, right?
I like the idea of being able to share the cache.
But I don't know about the approach, and that's where, like, I… I also think we might be… we're talking to someone who's using an AI, and I don't know how much, whether I'm talking to the AI or the person yet.
**Liudmila Molkova** 07:58 I see.
**Josh Suereth (Google LLC)** 08:00 Yeah.
**Liudmila Molkova** 08:05 Oh, whoa.
Well, I mean, we should ask.
them today, I had…
**Josh Suereth (Google LLC)** 08:14 I mean, it's… it's not… how do I want to phrase it? It's not bad right now. Like, in terms of DAI-ing.
But it's at the point where we have to make an actual design choice.
So, the thing that matters the most is, like, the CLI changes.
And, there's this notion of cache and cache refresh, and then it's actually storing, like, information in the cache. I think the VDIR, RS changes are the most significant to kind of talk through and look at.
Specifically, it's doing shenanigans with making, like, binary hashes, and then shoving things into, like, a cache file to track whether things are stored. Like… Generally, I'm supportive of the idea, and I think AI is just doing its AI thing here.
But I think we probably should say, and we've never had to do this with Weaver, yet.
But for things that are this significant.
even for ourselves, like, the work Jeremy's doing, I almost wonder if we should make a first PR be a, like, markdown design doc.
That grounds us all in what we want the feature to be, and that gets submitted first, and then if you want to throw AI tokens at the design doc, great, but I, like, it would be easier for us to have the discussions on the design.
Than it would be to have it in the code.
**Liudmila Molkova** 09:44 Yeah, I see.
Assuming this is the design doc.
**Josh Suereth (Google LLC)** 09:49 This… that is basically the design doc, yeah.
**Liudmila Molkova** 09:53 Van… It sounds very… unexpected for a CLI tool to have that many parameters.
For the cash.
**Josh Suereth (Google LLC)** 10:08 Yeah.
**Liudmila Molkova** 10:08 There's probably a… standards.
File system caching approach.
library cargo.
**Josh Suereth (Google LLC)** 10:18 There probably actually is, like, a library we can use, but the reality is… so, if you're… are you familiar with how VDER works today? Have you looked at it at all?
**Liudmila Molkova** 10:28 Vidir?
Yeah, I looked at it.
**Josh Suereth (Google LLC)** 10:32 Okay, do you know how when we, like, reference Git, we, like, download it to a local temp directory, and then kind of ignore the temp directory later? Let it get deleted?
I think the TLDR is basically, instead of doing that, we actually have a cache directory where we remember these things and keep them on your disk, if you opt in.
So, what I would like is if Weaver Toml had a use cache, and, like, if you say yes, by default, it's, like, tilde.weaver, or something.
And then, basically, we just changed Vita to say, hey, grab some cache if you can't. And it looks like what they're trying to do is also mix this with an offline-only mode, where you can download a bunch of repositories to a cache.
And then do we have a resolution without having access to the internet?
So I think there's two interrelated things, which is why I really feel like a design doc or an issue describing what you want would be a little better first.
Because we need to tease out those decisions. Anyway, wanted to walk that through with somebody else live, because I think while I talk, If that all sounds reasonable, I can add those as comments on the CL. They force-pushed a change, but they haven't responded to my comments yet, so we'll see what goes on.
**Liudmila Molkova** 11:51 I see, yeah.
**Josh Suereth (Google LLC)** 11:55 There was another, I think, AI-generated CL here, too.
Or new contributor, I should say. Where was that?
Weaver Pools… ver… Huh We have a lot of PRs, right?
**Liudmila Molkova** 12:26 But dear!
**Josh Suereth (Google LLC)** 12:30 this load registry file has been root path is dot prefixed1. This has been open for a long while now. This was August 4th, it's, like, 2 months.
I was waiting for, Lawrence to… do a review, you had Copilot do a review, but I don't think any of us actually commented on this.
**Liudmila Molkova** 12:57 This person, by the way, contributes to the BPF instrumentation.
**Josh Suereth (Google LLC)** 13:02 Yeah.
**Liudmila Molkova** 13:03 And I think today they need it further, for good reasons.
**Josh Suereth (Google LLC)** 13:08 Yeah, well, I think what they're trying to do is put the Weaver registry in a dot name.
And by default, we ignore dot when we look for markdown files in our loader.
So they're saying, cool, you can… What?
**Liudmila Molkova** 13:25 Markdown?
**Josh Suereth (Google LLC)** 13:25 Or, sorry, for YAML files.
Yeah, sorry, brain dead.
And since we ignore all the dot files, like, you can't actually use a dot directory as your route. But what's weird, like, this… is kind of a workaround that I think is… Could also lead to the bug getting reopened, which is just, as long as the first directory has a dot, everything's gravy, but anything under there that has a dot, we ignore.
And the reason we ignore dots is, like, we don't want to explore .git.
Generally. And we would.
Otherwise.
So… This is another one where I get what they want, I get that our current filter is not ideal, this, like… is a band-aid, not a solution. And we can accept it, that that's probably okay.
But I don't know if this is gonna cause more friction in the long run, or be weird in some fashion. Like, I wanna avoid… breaking changes to how we load files over time. So, I didn't have a chance to think of anything better, or think through this problem.
**Liudmila Molkova** 14:37 I mean, we can do this by default, if somebody passes just a directory, we ignore it, but we can accept some version of a globe.
And in the globe, they can say exactly what they want, and then we want to run a filter.
**Josh Suereth (Google LLC)** 14:56 Yeah, there was another PR that Laurent rejected that was, allowing Weaver to look at hidden files, and there was, like, a flag that would turn it on and off.
So maybe, maybe what, what we want to do is change our, the definition manifest to allow you to specify, like, here's your ignore files, or whatever. And we actually have it fully configurable.
**Liudmila Molkova** 15:22 I… I mean, is it worth fixing?
like… Why would you put your registry in the… dot directory.
**Josh Suereth (Google LLC)** 15:43 Bye.
I don't know, this is the second time we've had a PR around this.
**Liudmila Molkova** 15:47 Okay.
**Josh Suereth (Google LLC)** 15:50 And yeah, I… I agree with you, I don't think it's, like, it seems… Really insignificant, but the implications are kind of high if we get the dots wrong.
Like, if we ever start trolling through .git, it's problematic, we know that, we don't want that.
**Liudmila Molkova** 16:07 Okay, let's just ask, why is it necessary? Because… Okay.
Bye.
**Josh Suereth (Google LLC)** 16:25 Alright, and then I think, That sounds like a good resolution to that.
Reader input… I think all the other open bugs and feature things are from… you.
Which is good.
**Liudmila Molkova** 16:45 Yeah, so I'm sorry about this, but whenever I do something around Weaver and I see a bug, I prefer to file a bug, or maybe even a PR, and if it takes, I don't know, months or years or never, there is a of mind.
**Josh Suereth (Google LLC)** 17:00 That's… honestly, I think this is great. Like, this is what we want.
I was actually gonna say, like, is there anything, any general feedback you have we should talk about?
**Liudmila Molkova** 17:17 There's a… there are a lot of rough edges, but… It's… It's kind of rare learning.
what we do? We are doing something pretty new.
The… I wish Jeremy was here. So… You know how we do this reporting in Conformance Repo?
Essentially, this is what I probably want to see in the… Beaver Life Check Report?
Like, not the pure stats, not the pure samples… well, maybe all of this, but… also a summary, but what the summary is, I think we are actively checking out in the confirmments repo.
And… I… I kind of feel like this… this PR is a good example of where we might fail, is… if Conformance Reaper succeeds, then we will have a lot of stuff related to it. I mean, conformance program, I don't know, gate to the OpenTelemetry registry and whatnot, the stability of the libraries.
we would have a lot of people discovering the small issues, and we don't look at the PRs that are not ours.
Yep.
And it's not a great experience for people, and Rust is not the easiest language to contribute to.
Yeah.
**Josh Suereth (Google LLC)** 18:52 I mean, I've been trying to keep up with PRs generally, but I… My problem is I have to divide my attention, and, like, when there's a significant PR, I can really only deal with, like, specification proto.
or Semantic conventions, any of the crazy amount of Semantic conventions we have now, or Weaver. Like, I… so I actually split, and so if you send a PR on, like, a Monday, I'm not gonna review the Weaver PR until at least Wednesday, probably.
Because I usually reserve money Tuesday for specification, and then Friday is proto.
**Liudmila Molkova** 19:30 Yeah.
**Josh Suereth (Google LLC)** 19:31 At this point, right? So it's like… I… I get that, and yeah… we… we… we are lacking reviews and approvers. We probably need to be training up more people to approve Weaver PRs, like, get an approver set, because right now it's… Pretty much everyone's a maintainer.
**Liudmila Molkova** 19:48 Yeah.
I'm reviewing… some crazy amount of AI-generated Python PRs these days. I mean.
**Josh Suereth (Google LLC)** 19:59 Oh, in Japan.
**Liudmila Molkova** 20:01 A hun… more than a hundred a week.
And I'm just in… in such a review, Bankruptcy, so I, I… Okay, just… Cannot pay attention to.
**Josh Suereth (Google LLC)** 20:15 So how do we dig ourselves out of the hole? Yeah, I did install the PR dashboard, if you haven't used that. That one is nice. You saw the issue in Weaver, right?
**Liudmila Molkova** 20:26 Yeah, I mean, this is the issue.
**Josh Suereth (Google LLC)** 20:29 I think the main thing is, though, like, when it says waiting on maintainers, do you… Do you look at that and then go re-review those PRs or not?
Oh, the problem is, waiting on reviewers is all of us. We need to do all of those things.
**Liudmila Molkova** 20:45 Yeah, I think we need to turn on the stale bot.
It would… Hide all of this, yeah.
**Josh Suereth (Google LLC)** 20:55 Yeah.
Okay.
**Liudmila Molkova** 20:56 And this one, I'm kind of waiting now for you to finish the V1-V2 split, because it's much better to do it for V2, and do nothing for V1.
**Josh Suereth (Google LLC)** 21:08 Oh, yeah, yeah, I… and that one, I… I started… I started liberally pulling ideas from it for some of the V2, V1 stuff I was doing.
For toll… for, like, Yeah, basically, I don't know why we didn't do this first, but having a specifically a structure that represents the serialization format that CERD loads in, and then having it from to that goes into the structure we use to represent things. Like, we should have just done that from the get-go.
**Liudmila Molkova** 21:37 A lot of copies, for not super clear reasons, yeah.
**Josh Suereth (Google LLC)** 21:42 Initially, yeah, but once we… once we started having multiple versions, like, we're… we're there.
I mean, when you say a lot of copies, half the time we're loading a JSON, reading pieces of the JSON, then deserialize the JSON into a structure. So, we're doing a crap ton of copying right now, like… Huge amounts.
**Liudmila Molkova** 22:03 Yeah.
This is the copy you see in the design doc. The copies you're talking about, you don't see in the design doc.
Yeah, they have been in the code.
**Josh Suereth (Google LLC)** 22:13 Yeah, right, right, right.
Oh.
**Liudmila Molkova** 22:16 So, okay, so let's say we turn on the stale PR, it will just make things a little bit more manageable, but yeah, we need more people who can… Review and approve.
And…
**Josh Suereth (Google LLC)** 22:39 I think, I think I need to spend some more time doing Weaver reviews as part of the problem, but we also, like, we'll have to talk to Laurent and see if we can at least get one review a week, maybe?
Because he… the… the… The stale reviewer bot keeps trying to remove him as a weaver maintainer.
**Liudmila Molkova** 22:57 Yeah.
**Josh Suereth (Google LLC)** 22:59 So, I think that's also a sign. It's basically you, Jeremy, and I, doing a lot of these reviews.
We should try to have a little bit of activity here.
**Liudmila Molkova** 23:09 Yeah, I'm thinking…
**Josh Suereth (Google LLC)** 23:11 Good.
**Liudmila Molkova** 23:15 like, I feel… We should probably ask in the Semantic Conventions call.
Because Semantic Conventions depend, maybe Christoph would be interested in more of the Weaver stuff, and Conformance 3.0 depends on it. It's kind of a critical dependency in open telemetry.
Yeah. Where… yeah. If I was not that, like.
busy with the AI stuff, I would definitely… Pay more attention.
**Josh Suereth (Google LLC)** 23:48 I have trouble paying attention to the conformance repo. I think I reviewed 2 PRs so far.
Of, like, the 30 or so you've had.
Or more.
**Liudmila Molkova** 23:59 It's… Okay, so we, with this federation, and with all the schema work, and with all the, whatever, confinement stuff, we diluted You, Trask, me, Christoph, and a few other people who actively work on Semantic conventions across, I don't know, 10 different repositories.
**Josh Suereth (Google LLC)** 24:21 Yeah.
**Liudmila Molkova** 24:22 It kinda sucks.
**Josh Suereth (Google LLC)** 24:27 Are we ending up with faster velocity or not? That's the main question.
That'd be the retrospective.
**Liudmila Molkova** 24:35 To some extent, yes. So, like, confirmance repo is… you probably have a hard time reading it, because nobody ever read this code, except for once. It's very wipe-coded, and I think it's appropriate for it to be wipe-coded, the first version.
But, yeah.
But… In Semantic Conventions, G and AI, no. We… we… We don't have higher velocity, we… we don't even consider a lot of breaking changes in the future. Like, we want… we do stabilization now.
And we will… not… we don't plan to do V2 in, like, 6 or 12 months. Well, we could, but we don't want to.
Okay. So, it kinda… we did the split.
But was it a… and absolutely necessary? I don't know. The Federation makes sense, but not maybe… But… not… not all the time.
**Josh Suereth (Google LLC)** 25:48 Yeah, yeah, I… I mean, that's the downside. Basically.
The thing I think we're running into is the decision makers are still all the same people. The federation works if you can make the decisions decentralized.
And give people a charter, and then they work against the charter and don't try to… like, if the pressure always keeps coming back to the central decision makers for everything, it's broken.
So, you know, is some of this temporary as we build out the conformance repo and get the tooling up and running, and then it becomes decentralized and it's fine?
I don't know, because the other question I had for you is basically publishing.
you know, not having published a GenAI thing, I think, and getting our Weaver Resolve schema to the point where we're comfortable publishing it, like… The fact we're not there yet is worrisome to me, you know?
And is it a matter of time and attention, or is it actually there's fundamental issues that we haven't figured out?
**Liudmila Molkova** 26:54 I think it's a matter of time and attention.
Okay. You guys, I've been slowly going through the things that… like, to publish V2, we need to clean up the V1 stuff that's unpublishable, right?
And there's still a little bit of stuff. I think the… there are a couple of PRs, but most… the thing I didn't start yet is that there are… We have entities without identity attributes.
And they will fail in the two.
Yep.
So… Well… yeah.
**Josh Suereth (Google LLC)** 27:34 That's in Semantic Conventions. I can take a crack at some of those, too, to make sure that we get that.
Like, what we should do is basically, if something is de facto stable, all its attributes become identifying.
**Liudmila Molkova** 27:49 Right.
**Josh Suereth (Google LLC)** 27:50 And, like, if you're not happy with it, we need to make a V2 of that aspect, or, like, go make braking changes, yeah.
**Liudmila Molkova** 27:58 Yeah, I think none of this is stable, like, the ones that have this problem, and then it's probably not… doesn't… unconsequential yet.
**Josh Suereth (Google LLC)** 28:08 Yeah, to me, the big thing would be if we can finally get Semantic Invention to publish a stable and unstable piece, that'd be really powerful.
Like, I want to get to the point where we can do that. Like, that initial proposal you had for that.
Because until we get there, it's just problematic.
**Liudmila Molkova** 28:26 Oh, did you… there was a few items from James about the database conversion.
Did you talk about them on Monday?
**Josh Suereth (Google LLC)** 28:37 James wasn't there, and so it got glossed over as, like, oh, James isn't here, we'll deal with this later. Yeah.
**Liudmila Molkova** 28:44 Yeah, I… I think… This is something we'll need to tackle before, because the database are… stable.
And they will be in the stable version, and we need to pay close attention, but I think what he's talking about, that we have in a hierarchy of refinements, there is a database, and then there is a SQL, and there is, I don't know, MySQL database.
And how do we model this? And we can find solutions, and we'll probably be fine with solutions we make for a while, but, like, there are options.
**Josh Suereth (Google LLC)** 29:25 Yeah.
Yeah.
**Liudmila Molkova** 29:31 okay.
to Veaver.
There are people who are interested.
And…
**Josh Suereth (Google LLC)** 29:43 I'm getting kicked out of my room. I only got up for 30 minutes. I have to drop anyway, because I'm supposed to be in another meeting. There are people who are interested. Let's talk about that more. I think you and I might meet later, so we can talk about it then, but we can also talk in chat with the other maintainers, since we were the only two here.
**Liudmila Molkova** 30:00 Right.
**Josh Suereth (Google LLC)** 30:01 I'll see you.
**Liudmila Molkova** 30:01 Later.
