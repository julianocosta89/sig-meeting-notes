SIG: Semantic Convention Tooling
Date: 2026-07-01
Duration: 57 minutes
============================================================

## Zoom Recording Transcript

**ariannavespri** 00:10 Hello?
**Liudmila Molkova** 00:11 Hello!
Sorry, I'm trying to set things up.
**ariannavespri** 00:26 No worries.
**Liudmila Molkova** 00:32 Okay, I'm here. How are you?
**ariannavespri** 00:34 I'm fine, how about truth?
**Liudmila Molkova** 00:38 Fine, it's early. Something… huh?
**ariannavespri** 00:40 What time is it? What time is it there?
**Liudmila Molkova** 00:43 7 AM.
**ariannavespri** 00:45 Oh, oh my god!
Okay, wow.
Okay.
That's dedication.
**Liudmila Molkova** 00:57 Well, it's… yeah, there are quite a few things in Atel that happen so early, for me, because that's… there are just a few hours a day when We have some intersection with you folks in Europe.
**ariannavespri** 01:14 Yes, yes.
Yes, it's true.
**Liudmila Molkova** 01:26 Alright, it seems Jeremy is out today?
Yes.
Canada…
**ariannavespri** 01:36 It's got, like, Canada's got, like, public holiday or something.
**Liudmila Molkova** 01:40 Yeah.
**ariannavespri** 01:42 That must be the same for Laurent, I guess.
**Liudmila Molkova** 01:46 Same for what?
**ariannavespri** 01:47 Laurent.
**Liudmila Molkova** 01:51 Oh, correct?
**ariannavespri** 01:53 Is, is your, is your, is yours in Canada?
**Liudmila Molkova** 01:56 No, I think…
**ariannavespri** 01:57 No.
**Liudmila Molkova** 01:58 Who's in California?
**ariannavespri** 01:59 Okay.
For some reason, I thought it was in Canada.
Okay, I… Complete, you know, fabricated memory.
Fascinating phenomenon.
Hello, Josh.
**Josh Suereth** 02:20 How are we all doin'?
**ariannavespri** 02:21 Fine, thanks, how about you?
**Josh Suereth** 02:24 Not bad, not bad.
Trying to do too many things at the same time.
Alright.
Should we get started? I don't think we have an agenda today.
**Liudmila Molkova** 02:47 We don't, but I was going to Nagyu to review my pull requests.
**Josh Suereth** 02:53 I was looking at your pull request. Now, which one is the highest priority? Is it the documentation one?
**Liudmila Molkova** 03:00 Let me pull it up, I have… 2.
Let me put them on the agenda.
**Josh Suereth** 03:14 Okay.
**Liudmila Molkova** 03:19 Those are the easy ones.
So first, I… me and Kapai… oh, you left some comments on the… no, it's some staler view.
I think I have a final fix for the… Panic when we… get kamitsa… But my keyboard is not working, I'm sorry.
Okay, finally.
So this is the… When we give, we were… A remote template, remote policy, or anything?
And if it's a commit, then we panic, and this is the fix.
And the other one… Oh, this is the…
**Josh Suereth** 04:19 coded one, right? You used… and it was doing really weird things? Yeah.
**Liudmila Molkova** 04:25 Well, I took it over, I think I fixed things, and I think they are good now.
Another one… Is for spell name refinement.
**Josh Suereth** 04:50 I gotcha. Okay, so that… this is… this is the main fix here. This is what was… Causing a hard crash, right?
**Liudmila Molkova** 04:57 Right.
**Josh Suereth** 05:01 Okay.
Yeah, okay. And then there's, if it's a SHA, then we actually do a checkout of a specific thing, otherwise we go through, yeah, this looks good.
Huh.
The result box died, huh?
Because of this.
And because you want question marks. I hate that we do that so much.
**Liudmila Molkova** 05:49 What would be, what would you prefer?
**Josh Suereth** 05:52 No, I think if you, if you, create an error, if you annotate this as from.
you should be able to just use question marks straight up and not have box dying here. You can just have this return error, and it will automatically convert from, on your behalf.
and map these. At least there was a point in time where I thought that worked in Rust. But you need to actually… the problem is, right now, because you're pulling in two things here.
Right? And you're actually getting a translation. It's not a simple transition, so you have to manually write a FROM that, a FROM conversion, where you can say from getError to result.
If you're familiar with those type traits. But if you define that implicit conversion.
The question mark operator's designed to look for those if it needs them.
**Liudmila Molkova** 06:49 That's true.
**Josh Suereth** 06:50 Promote errors between… so yeah, so instead of doing this, you can literally just return the error, and it will do the translation in line on all of them.
**Liudmila Molkova** 06:59 Okay.
Can you drop me a comment, or I can drop a comment?
**Josh Suereth** 07:04 Yeah, I can drop a comment. Yeah.
Probably.
Three, four… eager… Good dog.
Error.
What's the other one? Kit something?
Get error.
And the… underlying gifts.
Intern.
That won't integrate.
Colin.
Pushing one.
Instead of… Rapid.
Okay.
Cool.
Sorry, I got distracted. Alright, and then the other one…
**Liudmila Molkova** 08:15 The other one.
**Josh Suereth** 08:16 Note.
**Liudmila Molkova** 08:18 Yeah, so… Where… Fixed the bug in the previous Weaver release, where… The span name node.
was ignored.
**Josh Suereth** 08:32 Oh… Yeah.
**Liudmila Molkova** 08:33 Yes!
**Josh Suereth** 08:36 Good.
**Liudmila Molkova** 08:37 This is a similar front, but… The spun refinement Sometimes needs a name.
And we didn't even have it in the schema, so there's… This one adds the spend refinement name note.
And if you override Any VIN and the span name, it overrides.
the whole span name, right? So you cannot pick and choose what you overwrite. It's all or nothing.
**Josh Suereth** 09:14 Gotcha.
Before, we were doing NameNote.
**Liudmila Molkova** 09:20 Yeah, it's, it was, I think it's a bug, it leaked into the schema, actually.
**Josh Suereth** 09:27 Hmm.
**Liudmila Molkova** 09:28 But… now I… first I replaced it with the full span name.
And I am no longer leaking it into the schema.
**Josh Suereth** 09:41 Okay, yeah, that makes sense.
**Liudmila Molkova** 09:42 Well, it's clicked into V1 schema.
**Josh Suereth** 09:46 Yeah, well… I guess we can't really hide it in the schema, can we?
**Liudmila Molkova** 09:52 Oh, we do, like, we hide it with ignore serialization, I know that. We did ignore… we don't show it in the schema RS, yeah.
**Josh Suereth** 10:04 Okay. So, yeah, it's only on span refinement. I mean, this looks good. Cool.
So this is… this is blocking, GenAI SimConv, right? Because you can't override things appropriately.
**Liudmila Molkova** 10:19 It's not blocking, because we just put this note in the… Basic node, but it's the rough edge.
We shouldn't have.
**Josh Suereth** 10:32 This says there are merge conflicts for that one.
How do you have merge conflicts?
Interesting.
**Liudmila Molkova** 10:39 Changelog, of course. The usual suspect.
**Josh Suereth** 10:44 Yeah, that's why… I don't know if you know the, the, yeah.
the release, like, thing I made for the agent, I just have the agent go infer a changelog, and it was doing a good enough job from the commits that it's pulling in, as opposed to the humans writing one.
It's basically a more expensive version of that GitHub changelog thing that we use in semantic conventions that's less annoying to me, because I just make sure the pull requests and the commits are useful in names, and then it makes me a changelog.
So, I like that.
And then when you cut a release, you go look at the changelog it makes for that prepare-release PR.
**Liudmila Molkova** 11:27 Yeah.
We can do this, so I think there is a… there's this… How's it called? What we use in some conf… login. And there is a new cool thing people use, Town Cryer, when you add a… Yaml or Markdown Fragment.
Along with your PR, and Edgen does it for you, of course.
Why would you write it by hand?
And then…
**Josh Suereth** 11:55 What I'm saying is, we don't… we don't even need either of those. When I was cutting releases, you notice I don't make changelog entries for Weaver.
Or at least I haven't. So there is an agent workflow that we have here for the release agent, where one of the processes, it literally goes through and describes all of the commits, and as long as your PR had a good description in the commit.
it will actually update the changelog with what's changed. So you don't have to do anything besides have commit messages that are good.
in your… or a good PR description.
**Liudmila Molkova** 12:32 Yeah… did we actually publish it in the release?
**Josh Suereth** 12:38 when… when I've made releases using this agent.
which is how I normally do the release tags, it will do that on your behalf. You do not have to make the changelog ahead of time. It will make it for you.
**Liudmila Molkova** 12:52 Yeah, well, I don't mind, but personally, I hate changelogs from agents. They don't understand what to describe.
**Josh Suereth** 13:02 So, you think they're too stupid for it. Gotcha.
**Liudmila Molkova** 13:05 Well… I… I prefer to handcraft a… Short message, and… They don't understand when something is implementation detail that external readers have no interest in.
But the PR description is something where it might be interesting for the reviewers.
**Josh Suereth** 13:25 That's literally why, like, if you look at our change logs, right?
Where do we have it? Our changelogs tend to be… very much PR descriptions. Yeah.
So, if we look at this… reinstate bear flag support, right?
So, I think if an agent went and did a summary of this, it's not… it's basically what's in the pair description.
**Liudmila Molkova** 13:58 Okay, so next time I write pair descriptions, I won't go into the details.
Not that I did.
**Josh Suereth** 14:05 At least in the title, yeah, I'm trying to… if we look for one that I cut, where's the last one I cut?
to… contributors, GitHub Actions… oh, GitHub Actions releases all of these.
Oh, this one, definitely. Do you see this here? This was agent-added. I didn't write this.
**Liudmila Molkova** 14:27 Yeah, but the rest of it.
**Josh Suereth** 14:31 Half of it was human-written, half of it was agent-written, so the agent added things into here.
**Liudmila Molkova** 14:35 Oh, whoa, this I like! So, if we missed, we keep missing the changelog.
An agent feels certain, that's cool.
**Josh Suereth** 14:44 Yes, yeah, exactly. So that's what that release workflow does. So if you wanted to handwrite a release note, because you want it to be specific, go for it. Otherwise, the agent should fill it in.
And I'm trying to update that agent to, like, be more intelligent and less stupid with how it fills things in.
This is just to make it so that we can, like, again, if we're spending all our time updating changelog conflicts, I don't feel like that's valuable time.
But having a good changelog is valuable, so I was trying to figure out how to reduce the friction, which is why I set up that, that agent release thing.
Which, I believe… Let's see… How did I trigger the stupid thing?
**Liudmila Molkova** 15:35 Tell your documents agent to update the releasing or country BMD to say how to trigger the release agent.
**Josh Suereth** 15:46 Yeah, I'm happy to do that.
I've recently been playing with, well, internally and Claude both have a thing where you… ask it to review your previous end iterations with the agent, and figure out all the things you're annoyed with it, and then go fix the skills, you know, to, like, address the things you're constantly annoyed with. That's been pretty amazing. I don't know if it works yet, but I've been running it, and it, like, literally figured out all the things I'm annoyed with it about.
Very crisply, you know?
Anyway, yeah, like, getting to the point where we focus on actual fun problems and hard decisions and not the things that are important but tedious, like, Where, where is it? Changelog.md? Yeah.
Okay. The other thing we could do… I could probably make a little GitHub thing, Where it updates the changelog right before you merge or something.
You know, like, it would propose.
**Liudmila Molkova** 16:48 Whoa!
**Josh Suereth** 16:49 Yeah.
**Liudmila Molkova** 16:50 We can tell Copilot to do this, and add GSMD. We should finally add EdgeMD here.
**Josh Suereth** 16:57 No.
**Liudmila Molkova** 16:58 Like, even the trivial ones, so, like, about the things that are annoying. I sent a period of fever.
And I use Claude… And because we don't have AgentsMD, it doesn't tell to run cargo format, and I get the stupid CI errors, and I need to come back and run format.
**Josh Suereth** 17:19 Yeah, I just had, all the, like, Google Gemini things go through and make a set of AgentMD files for Weaver from all the various Rust things I've done, of… all the annoyances, but I literally created a, like, weaver development skill.
That is for me. That's all the things I want to do. Which is, for example, like, don't do anything with Node.js, ignore that completely, unless I tell you you're working on the UI. So I don't want to give that to everyone in Weaver, right?
**Liudmila Molkova** 17:58 Yeah… I mean, I think you shared them with me. If you don't have time and you give me your permission, I can use my AI to extract the generic pieces from your AI and send it.
**Josh Suereth** 18:11 Yeah, feel free, feel free.
Okay. I'll send you some more of the stuff I was working on there. But yeah, okay.
That sounds good. Let's get, let's get into, let's see, update all pack. One of the things that I do want to complain about briefly, and I noticed this, I don't know… with Renovate, if we're actually catching all changes anymore.
Specifically, the thing I'm worried is broken is our release management pipelines. I don't think it's actually working. We had a… we had a contribution to fix up or renovate, and it made it very clever.
Where is our Reddit? Is that in GitHub?
Or is that… I thought that was raw.
**Liudmila Molkova** 18:58 It should be here, somewhere.
**Josh Suereth** 19:02 Renovate.
Mmm…
**Liudmila Molkova** 19:07 Probably in the GitHub, yeah.
**Josh Suereth** 19:09 Yeah.
So, this is… this is, like, very clever right now with some of the things it does. Like, it has a lot of these match strings and custom managers. This one for cargo dist. I am not confident this thing is actually working, because I haven't actually seen updates Get sent to us, and then when it does send updates, they actually break the workflows, and we have to manually do the update anyway.
**Liudmila Molkova** 19:35 You know what, there is…
**Josh Suereth** 19:37 Good.
**Liudmila Molkova** 19:39 There is a dependency management issue, and it shows… What it's holding back because of the schedule or something.
And I can look there and see if what you… Our missing appears there at all?
**Josh Suereth** 20:01 You.
**Liudmila Molkova** 20:03 Oh, depends on the dashboard?
**Josh Suereth** 20:05 dashboard, there it is.
**Liudmila Molkova** 20:06 Yeah. Yeah.
**Josh Suereth** 20:07 Renovate config warnings, updating branch failures, and package lookup failures, right? Like, I'm a bit nervous about these, and so… These are, like, the new Rust came out, and yes, it's waiting to update, that's fine.
Errored pin dependencies. We have issues with particular things.
Let's try those now.
And then fail to look up dependencies, right?
This is a lot of our release workflow. Basically, our entire release workflow, it can't look up dependencies with the customization.
**Liudmila Molkova** 20:51 Okay.
**Josh Suereth** 20:53 And I'm not sure what we need to do with that.
Besides, like, someone probably needs to investigate it, but I did notice.
**Liudmila Molkova** 21:02 Honestly. Yeah.
**Josh Suereth** 21:03 dist workspace… the way… again, because we're using, like, helper methods, I'll just show you this. There is this dist workspace.
that determines all of the, like, Rust binaries we're gonna build.
And how, whether we have installers, all that kind of junk, right?
And then inside of that, you have these custom runners that you list.
These are the versions that I think need to get bumped every now and then.
Right? So this is where, in the past, for example, Ubuntu 24 went… before it was Ubuntu 24, this went, out of service, and we had to bump to Ubuntu 24.
We're using Latest for just our, coordination runner, but for actual releases, we build on dedicated known instances so we can rebuild, you know… we have as much item potency as you can get.
Similarly for, like, muscle targets, right, we have particular things that we build. Anyway, this is the interesting bit here. This is where we're specifically saying what GitHub actions we use, and we're… to be Salsa compliant, we want to use hashes that correspond with version numbers.
Then CargoDist, the thing that builds all of this, it's a set of, you know, build pipelining support, makes our GitHub Action workflow from it.
So we told Renovate not to read our GitHub Action Workflow, and instead update here.
And then we were manually updating these.
Okay.
like, like, Renovate would make a proposal, it wasn't good enough, we'd have to go manually update the proposal.
What Renovate's trying to do now is update this and the generated code at the same time, assuming it's gonna do the same thing in both places.
That's fundamentally broken, but also, the extraction of this data is not working right now.
So, like, the whole thing's broken. These have not been version bumped in quite some time.
Which makes me a little bit nervous, because this is, you know, the whole compliance and protection thing is basically, we want to make sure these versions are real versions, and this is how we attest that we're the ones who built the thing we build.
So, if there's any vulnerabilities or something in that particular package, I want to make sure we're updating relatively quickly.
**Liudmila Molkova** 23:31 Oh, wait, why do… So, we… do we have to keep those versions here at all? Because if we specify them inside GitHub Actions, Renovate does an amazing job updating those without any… anything special.
**Josh Suereth** 23:47 So, we have to have them here if we use cargo dist. If we wanted to not use cargo dist, we would have to write a distribution mechanism that does what CargoDist does, which is builds on, you know, 27 different You know, repositories, uploads all the artifacts, puts them all together, creates a release, like… Again, CargoDist is generating those GitHub actions. If the cargo dist implementation, those actions fall out of sync, it all breaks.
**Liudmila Molkova** 24:17 Okay, so what you're saying that the renovate config just does not understand the syntax?
**Josh Suereth** 24:22 It doesn't understand this. Yep.
Yep, and I don't know if we should open a bug against renovate or what to do there. We had debated in the past getting rid of cargo dist.
And just manually making a release pipeline.
**Liudmila Molkova** 24:35 It should be easy to solve this renovate, like, it has different means to match things, and you can put an annotation here in this file, a special annotation for renovate, and it would, update things, for you. There are multiple ways.
**Josh Suereth** 24:54 Right, so basically, we need someone who knows Renovate to work on this, or throw an agent at it, I guess.
**Liudmila Molkova** 25:03 Yeah, the trick is that Okay, there are multiple versions of Renovate, and the worst part, there is a self-hosted one, and there is the one that we use, and they are slightly different.
And agents, assume you use the wrong one, and sometimes… well, sometimes they assume And it needs testing.
But, we can give it a try.
**Josh Suereth** 25:33 Okay. I think this is the one here where it is trying to figure this out.
But that's the release of YAML.
That's the other weird thing, is I don't understand why we have disk release YAML CI actions, and then we have the template.
Separately.
But… I want these to run at the same time, always.
**Liudmila Molkova** 26:02 Oh, and they currently… Independently update one or another.
**Josh Suereth** 26:09 Yeah, and then it's.
**Liudmila Molkova** 26:10 inconsistent.
**Josh Suereth** 26:11 it, and then we can't merge the PR anyway.
Anyway, I'll have to… I'll have to look through. Just a random thing… random aside of, like, things that we're running into.
I don't want to suck up all the time available, because we don't have anything on the agenda. I'm still working on the dependency resolution. I haven't had a chance to do anything useful yet, because holidays and vacations, basically, since the last meeting, I only worked 2 days.
Because I had off after that Wednesday.
One last thing, I don't know if you've seen this, but I was thinking about adding this to all of the Weaver repositories. So inside of Java… They have a… Review… I think it's… is it… Tagged or something? Hold on.
Pool request dashboard, yeah, it's an issue.
And there's automation, which will create this thing.
So you can have a what's waiting on maintainers review, what's waiting on reviewers, what's waiting on authors, and then draft pool requests and how long they've been open, so you can, like, manage your input. I'm actually thinking about just installing this frickin' everywhere that I'm a maintainer on, because it's awesome.
Any concerns or thoughts there?
**Liudmila Molkova** 27:30 We use it in Gen AI, Trask added there.
It's now shared, he can edit anywhere, I think.
Yeah. Yeah, it's amazing.
**Josh Suereth** 27:40 Yeah.
Agreed, I really like this. So, if we're amenable, I might add this to, the, Weaver repo, the Weaver Packages repo, the Weaver Examples repo, I was even debating it for SEMCOM.
But I don't know about that one.
And then, probably… you know, unrelated to this meeting, but OpenTelemetry Proto is the other one I might add it to.
**Liudmila Molkova** 28:10 Yeah, I mean, it does not hurt.
At all, right? So, yeah, if we…
**Josh Suereth** 28:16 Well, I mean, it's costing somebody money and time.
**Liudmila Molkova** 28:23 Somebody abstract enough, okay, maybe the GitHub credits, CNCF gets for free. Microsoft money.
**Josh Suereth** 28:31 Yep.
Anyway, okay, so I'll, I'll take an action to make that happen. Oh yeah, and the other thing, Lyudmila, on, OpenTelemetry Weaver packages for your PR. I did submit my pull request, but to fix it.
So that it would pass. I actually… do you now have a version conflict here?
Because I fixed the span name being TBD, just to get the fix for the other test through, and then I think when your fix is done, that'll fix everything, so… or when this is through. I'm gonna re-review this, but you have a merge conflict.
**Liudmila Molkova** 29:12 Yeah, I'll fix it.
**Josh Suereth** 29:13 Yeah, but this should pass now.
ahead.
**Liudmila Molkova** 29:18 Awesome. Since Ariana is here, maybe we should chat a little bit about this one. Yes. So, yeah.
We… have, the SEM conference, SEMCon of Gen AI now, and there are more people looking into federating.
And, I'm thinking how we can give people the templates that are generic across, like, that we've been using in semantic conventions that are, Maybe hard and not perfect, but at least, they are sophisticated enough to show people everything.
And, I don't… want to… replace… your templates, because I think they are kind of good stepping ground for people to learn how it all works without being overwhelmed, but also they generate registry.
And… I've been thinking, we… One registry for, like, metrics and spans, I think it's a good experience that you don't need to write any Markdown snippets. You can… there are two ways. You can just generate all the signals, or you can write Markdown snippets, and then Weaver will, like, embed the generated pieces of Markdown into your otherwise free-form text files.
And both things kind of make sense, but for people who are just starting with semantic conventions, just the registry is awesome.
Maybe they… they just… go down the route of snippets passed later, or never?
And I'm thinking… We don't really want… let's say metrics registry, or a spend registry in, like, semantic conventions GenAI, because we have all this freeform marked down with pieces of generated stuff.
But I think it's not mutually exclusive.
So we… it's part of the Weaver YAML, if I remember correctly, that you… Choose to generate registry for a signal.
**ariannavespri** 31:44 Oh.
Yeah, I think so.
I can't remember.
**Liudmila Molkova** 31:51 Yeah… And then, maybe what we do is… I'm just opening the viewer packages to make sure.
Maybe what we do is that we keep the registry for In templates, but since people decide what they want to use, they choose… One or another.
Okay, I'm opening waiver… Okay, if I look into the Weaver YAML on main… I don't… I don't have the… Registry… I don't choose the registry.
So how does it work? How does it render everything?
**ariannavespri** 33:12 Let me refresh my memory.
**Liudmila Molkova** 33:14 Sorry, I'm looking into my fork, not, not the…
**ariannavespri** 33:17 Oh, okay.
**Liudmila Molkova** 33:18 Alright.
**ariannavespri** 33:19 Yeah.
**Josh Suereth** 33:23 Should I stop presenting, Lamela? Do you want to present?
**Liudmila Molkova** 33:27 Okay, yeah, let's do this.
**Josh Suereth** 33:32 Where's… oh.
Hold on.
**Liudmila Molkova** 33:40 Somehow Zoom stopped blocking.
Like, it used to… you… it was not possible to present when somebody else was presenting, but now it… it works.
Okay, so this is the Reaver Yamel on main.
So if somebody doesn't want, let's say, a spend registry, they just don't add this fragment, right?
**ariannavespri** 34:04 Yeah, I would think so.
I would think so.
**Liudmila Molkova** 34:07 Right.
**ariannavespri** 34:09 I really didn't think of the event, you know? Like, you know, I didn't think of the possibility.
**Liudmila Molkova** 34:18 Yeah, that's totally fine. I didn't either.
And then… We can provide a couple of… So this friend, it's not actually a template, right? It's just the… It's something you customize. So if you reuse the templates, You… point. You can provide… oh, wait!
If you don't… How can you reuse templates without Weaver YAML?
**ariannavespri** 34:58 I don't know, we should, maybe they should live somewhere else, and they should be more generic than they are now.
I don't know.
**Liudmila Molkova** 35:07 I think we need to decouple this, too, because Vvariable is essentially a config.
And… Templates are the shareable piece.
And it used to be possible to have templates in one folder, and YAML over YAML in a different place, but it's.
**ariannavespri** 35:25 Yes.
**Liudmila Molkova** 35:25 now.
We broke it in the last river.
**ariannavespri** 35:30 Yeah, I think, I think I… I think I, I did that for, for avoiding duplication, if I recall correctly.
**Liudmila Molkova** 35:37 You cannot, it's like, it's not… it's not in your control, it's in Weaver. It does not allow you to have different Weaver YAML inspired by her.
**ariannavespri** 35:46 Okay.
**Liudmila Molkova** 35:49 So maybe… Okay, I'll create a bug for Weaver to make them decouplable somehow.
I'll try to think how to solve it.
**ariannavespri** 36:03 In any case, you were not thinking about all the signals you said, right?
**Liudmila Molkova** 36:07 Sorry?
**ariannavespri** 36:08 You were not thinking about all signals.
like, to have registry rather than templates. You mentioned spans and metrics, or what did you… or it was for everything?
**Liudmila Molkova** 36:22 So the things we have registry for as semantic conventions are just attributes and… Entities?
And the rest is currently our… done through markdown snippets.
**ariannavespri** 36:37 Okay.
**Liudmila Molkova** 36:37 Oh, okay.
**ariannavespri** 36:38 Okay, Disney pits then, okay, okay.
**Liudmila Molkova** 36:41 Yeah.
But I think that's a choice.
**ariannavespri** 36:47 Yes.
**Liudmila Molkova** 36:47 People can… can prefer a registry.
Then they don't need to manually write any markdown.
**ariannavespri** 36:56 Yeah, I'm taking notes.
Right, any markdown.
**Liudmila Molkova** 37:15 And… And URVERY YAML is kind of awesome. It only includes… things that are necessary for registry? Well, there is still some decisions that people can express, like, some people would not need deprecated to render them at all.
Right.
**ariannavespri** 37:39 No.
Yup.
Mmm.
**Liudmila Molkova** 37:46 Joshua, do you think about Weaver YAML decouplable from templates?
**Josh Suereth** 37:53 Ugh, Right.
Like, so Weaver Yamble would only be used for packages? Or… you would have a different config. Like, that's kind of what I'm wondering.
Where… where do we…
**Liudmila Molkova** 38:21 So, like, there is a distributable… distributed… sorry, distribution of templates, Ginger.
They are… Well, almost, generic, right?
River YAML is full of your choices. You would put acronyms here.
You would choose which templates to use.
**Josh Suereth** 38:47 Oh, I see. You're saying the templates themselves are distributed independently?
**Liudmila Molkova** 38:51 brand, Ginger.
**ariannavespri** 38:54 Be like the template of a template, kind of.
**Josh Suereth** 39:04 I mean, yeah.
It's possible, I have to think, like, I understand we're running into reuse problems, I'm still in a walk before we run, like, until we have a good set of template.
Packages that we're happy with.
I don't want to rush to abstract. Do you know what I mean?
**Liudmila Molkova** 39:29 I… yeah.
**Josh Suereth** 39:32 But I also think Weaver YAML is weird, in that it is both the metadata that describes a package that you can download, and it is a metadata for overriding default attributes of a package that you use.
and it used to be config for all of Weaver. Like, all it… it was doing so many things all at once, where, like, pieces of it were used, it was all… it… like, it was a mess of spaghetti, right? So, like, I think having, like, specific What does the configuration a package has to say, here's how I'm consumed and used?
And then having the ability, when someone uses a package, to override capabilities makes a lot of sense to me.
Whether or not we then… tease apart these, like, code gen packages, right? Like… if you're trying to say, I want a registry, but… Maybe, maybe actually another way to phrase this, Ludmela, would be.
There'd be a package for registries, and there'd be a package for, snippets that are different.
**Liudmila Molkova** 40:39 Package for registries, package for snippets.
Then it would be, like.
**ariannavespri** 40:44 Linda.
I would… Then you could not have, like… one Weaver YAML containing all these, it would be, like, another, like, splitting this into two files, different files.
**Josh Suereth** 40:59 Kind of, yeah, that's kind of what I'm imagining. I'm just… I'm trying to, like… I'm trying to figure out how to give you what you want without, And make… make this work in the system, like… To the extent we can have a simple, dumb model, the better.
And, like, me as a user of templates, right?
I'm using a package to generate docs. Am I gonna care whether or not you're reusing the same template file between two different packages? I kind of don't, right?
Or is that what you're suggesting?
Go ahead.
**ariannavespri** 41:44 But one historical question, so you said that before, like, we were… YAML was even more, like, was conflating more things together?
And how that… how was that solved?
**Josh Suereth** 41:57 So, Jeremy created a weaver tomel.
And that is used to configure, like, the weaver that you're running as part of your build.
And then Weaver Gamble we're using to control, like.
Templates and policies and that sort of thing.
So we're trying to limit Weaver YAML to be the configuration around a package. So the Weaver package of, like, here's how I generate Markdown, here's how I generate Java, here's how I generate, here's how I generate policy checks, yeah. That Weaver YAML, is, like, one per package, and it's, like, the metadata about the package that tells Weaver how to consume it, what to do with it, that sort of thing.
**Liudmila Molkova** 42:45 I'm thinking the simple pass is that, okay, there is some decisions that are shipped with these templates, and there is a default Weaver YAML that you Use if you just specify templates.
But you should be able to overwrite the choices, the default choices that's been made.
**Josh Suereth** 43:07 Yes.
**Liudmila Molkova** 43:08 And, like, there are certain pieces, like acronyms, that are very specific to certain repo, right? We… We can tell people to pass a paramus, a list of acronyms, but it sucks, or text maps, right? If you want to do some other stuff.
**Josh Suereth** 43:25 Well, and acronyms, Weaver YAML, like, one of the original things, the reason why it was so convoluted, and I think this still exists, you can specify acronyms, and when we merge in the package, we'll join the two together.
So you can expand the list of acronyms from the package that you're using.
**Liudmila Molkova** 43:47 Okay.
**Josh Suereth** 43:48 And that shouldn't.
I don't remember if Tamil does that or not, but, Like, that's a thing… that's a thing we need to allow. I think… so the question I'd have, Lyudmila, is… I would like to be a bit more crisp about what the overrides need to be, and I want to make sure that we're overriding, like, intent, not… Exact, like, howls.
You know? So if we're getting to the point where we're saying, hey, I want to change this… actual Jinja template. The Jinja template has a set of… parameters and things that you can use to tune it, but, you know, to the extent we can say, here are the parameters and things you can use to tune.
And then, when I consume a package, I just am tuning those parameters, not like the whole dang… Kit and caboodle of all this crap, you know?
**Liudmila Molkova** 44:42 I don't think it's possible to overwrite things without letting people overwrite anything that you see here.
So, like, this is a choice.
**Josh Suereth** 44:51 I think all of it has to be overridable. Okay.
**Liudmila Molkova** 44:54 I think the natural choice is to say, okay, I decide how… what I filter by, and which templates I use.
And thus, I should be able to avoid the whole river Yamo.
**Josh Suereth** 45:13 So, I mean, the problem there is the… you're… entity readme.md, if I change V2 to be false, I might not get data shaped in a way that I render it at all, so if somebody changes that, they've just broken it.
But exclude deprecated as a flag that I say you could set it to true or false. That is a parameter that I would expose to say, when you consume me, here's a configuration parameter for me as a package.
Does that make sense?
**ariannavespri** 45:46 And it's kind of customizable to some extent, that it doesn't make it dangerous, like.
Like, that it could actually backfire, let's say, for the users.
So maybe we… it could be, like, you know, some safe… The things that we know that would be safe to actually make a personalized choice.
So, like, for example, no diversion, then.
**Josh Suereth** 46:10 Right, that's, that's why, like, my thinking is, if we know… What the configurable pieces of this are.
We have a way where you can say, here's configurable parameters for this template, and then we have a way for you to specify them when you consume the template.
Kinda like… But, but my, like, if you're right, Ludmila.
then that configurable piece will be the whole damn thing. Right?
If the configurable piece is all of Weaver YAML, Then I think we've kind of failed in terms of abstraction.
A little bit here. Like, like, what is the value of a package at that point?
**ariannavespri** 46:51 Yeah, I mean, y-yes.
**Liudmila Molkova** 46:54 Interesting.
**ariannavespri** 46:55 That's why I was… I was saying template of templates.
**Liudmila Molkova** 47:01 Well…
**ariannavespri** 47:01 I don't know, maybe, maybe… All good.
**Liudmila Molkova** 47:06 No, go ahead.
**ariannavespri** 47:07 Yeah, I mean… Maybe we should think of, you know, really, like, analyze all the pieces that are there.
And see which parts could really be, like, detrimental if they were customized In a way, rather than another.
And and maybe have those that can really, really not be changed. I don't know, maybe have them into another file, which is really, like, wouldn't say immutable, but kind of.
I don't know if we can, Make that kind of decision if you just… complicates things, I don't know, but I see the point. I see the point in… in, in having… In having the user make certain choices.
Within reason.
**Josh Suereth** 47:58 Yeah.
**Liudmila Molkova** 48:00 We can do, we can try.
Like, there are a handful of these flags here. I agree, V2 is, like, the choice that you make. It's the whole Weaver packages template, yeah.
like, there is a set of parameters here. So we also make the same choice here, so we should probably transition those to… these helpers, because they're aligned with Ginger templates. So if I extract the reasonable properties to configure from here, and each of the sections is… There is a flag allowing you to disable it.
This can be a star that works now.
at some point, somebody comes and tells, okay, I don't… I want to call this folder not attributes, but FUBAR.
Probably tell them no, or we can revisit the choice of a set of properties that we support to include this new stuff. And eventually.
We always have an option to… Let people clone and… For a current update, right?
I, I…
**ariannavespri** 49:18 Yes, sir.
**Liudmila Molkova** 49:18 I can try…
**Josh Suereth** 49:21 So, so one thing I'll just call out, like, the… the way that Weaver was supposed to work for a lot of this is there's, there's a params flag, and then Weaver YAML has params, and it's just a big key-value map that you're supposed to be able to use to customize things. And so, like, the assumption that we had initially was that's the thing we'd expose. So, params is available in JQ.
Params is available in Jinja.
So if you were to say, like, at the top of your package, to say, here's the parameters that I interact with, and here's what they mean.
That's documentation.
We can use it in JQ expressions, we can use it in these patterns and filters to do things. That would be, like, step one, of, like, what's there now? What can we do? Is it enough, I think is the question that is in my head now, based on what you're saying. I think, yeah, the answer's probably no, so we need to figure out what more we need.
Yeah.
**Liudmila Molkova** 50:22 Yeah, we need the inclusion, the flag control and inclusion of the individual section, and it's not a param, it's almost like a template for YAML.
**Josh Suereth** 50:34 Oh, no. It's gonna be ginger all the way down, is that what you're saying?
**Liudmila Molkova** 50:38 No. Yeah.
But yeah.
**Josh Suereth** 50:41 I mean, it could be… also, we could put an if statement here on the template patterns that look at a parameter, and if that parameter exists, that thing is enabled, you know.
Or a NOT parameter, that kind of thing, yeah.
**Liudmila Molkova** 50:56 Yeah.
Okay.
**ariannavespri** 51:00 Yeah, probably the most important thing is really realizing which things we want to Allow for, tweaking and what.
Really, like, a no-go.
**Josh Suereth** 51:12 Yeah.
Actually, if you just got an issue with, like, here's the set of features we want to expose for tweaking.
in the thing that we built, and then we can work through that and figure out the best way to kind of make that happen. I think that'd be the approach I'd like to take, as opposed to just… you know, you can do whatever the hell you want with Weaver YAML, That has me a little nervous, because I already think we reamals too hard for most people to care about it.
You know?
**Liudmila Molkova** 51:40 shrink.
**Josh Suereth** 51:41 I, like… The number of people who have written Weaver YAML and care about what they've written.
Is probably the folks who attend this meeting.
You know?
**Liudmila Molkova** 51:53 I would not put myself into this category, I don't care what's written there.
**Josh Suereth** 51:59 Well, that's also why with YAML, I want to get to the point where, if you don't care, we have it documented enough, an agent doesn't F it up.
You know what I mean?
**ariannavespri** 52:06 Yeah, I mean, I cared at least about the formal correctness.
And then I was, like, without many strong opinions about what was actually in there, a bit because I'm, you know.
because, you know, I'm easygoing, and of course, then I'm still a bit ignorant, more than a bit, about all of this, so… but but I definitely see a point, and I also… I definitely agree on the approach that we should first, like, understand the what, and then we'll do the how.
**Josh Suereth** 52:42 Yeah.
**Liudmila Molkova** 52:44 I'll create an issue down.
And we can chat about it more. And it sounds like, for the time being, we will… Not, have a set of… Some templates that people can reuse.
**ariannavespri** 53:01 Not for the immediate future, I would say.
**Liudmila Molkova** 53:05 Yeah.
**Josh Suereth** 53:08 You mean the ones you're using for Gen AI?
**Liudmila Molkova** 53:11 Yeah, it's okay to keep them in Gen AI. I was worried about mainframes, and I didn't want them to keep a copy.
**Josh Suereth** 53:20 if you wanted to make a Weaver package called, like, you know, just for SEMPCOM markdown.
I am fine with that, mostly because I think we're gonna be spinning off a bunch of these small repos. But also, if you, if you called it, like, Because I… Ariana, I'm not sure you're doing the markdown snippet generation, are you?
**ariannavespri** 53:43 No, I don't think so.
**Josh Suereth** 53:45 Okay. Yeah, so the fact we don't have markdown snippet generation, and that's used all over SEMCOM, I think that is, like, a, you know, workaround might be useful.
**ariannavespri** 53:56 Okay.
**Josh Suereth** 54:00 I don't know.
I'm on the fence, Lyudmila, about, like, I think we agree it shouldn't override what Ariana's does now, because it doesn't do registries for everything.
But I'm on the fence over whether you submit it. I… I… I'm… my gut tells me you should submit it with a different name.
And we should name it appropriately, that people know it's, like, not for general use, it's for SEMCOM specifically for now, and that will sort out the details between the two over time.
Is that reasonable?
**Liudmila Molkova** 54:30 Yeah, totally. Let me drop a comment on my PR.
And… I'll think a bit more about it, and I'll explore… What else we can do? And… Maybe… By the next meeting, I'll have it updated to… be in a different package, or maybe I have a better proposal by now.
**Josh Suereth** 54:56 Okay.
**ariannavespri** 54:57 I just have a very short question, like, banal question. So, this is, like, because… so all of this is because it's something that you thought, because you would like for it to be as a user, or you actually, like, somebody, you know, asked… asked for more flexibility, knew about the… the markdown templates or whatever, and… And actually, I asked you for… To have, like, the possibility of customizing things.
**Liudmila Molkova** 55:25 I'm just realizing now that the… even if we want to use the… what I have in my PR, In different repos, we'll let it already fail, because the… You cannot really override things you want per repo, or it's cumbersome.
**ariannavespri** 55:44 Okay, makes sense. I was just asking in case, because if we already had, like, some people, like, telling about that, then we could have kind of had a survey about what they wanted to see, you know, changeable, let's say.
But it makes totally sense, I understand that.
**Liudmila Molkova** 56:04 Yeah.
Well, that's essentially… I think I have… I know what to do next.
And I appreciate your thoughts.
**Josh Suereth** 56:17 Cool, yeah?
Thanks for working on this, too. I'm, keyboard packages show up.
You know?
We still need our first code package to show up in there, and If you're unlucky, it'll be me writing something for Scala, or something stupid like that, right?
Where I know no one will complete with me.
Anyway…
**Liudmila Molkova** 56:39 Yeah, I'll ask Claude if it's a dramatic scholar.
Or whatever, yeah.
**Josh Suereth** 56:44 Okay.
The question is, will it have read my book about it? And that's what it's based on? Because I get to cheat when it comes to that, you know?
**Liudmila Molkova** 56:52 Oh, okay. Is it available to agents?
**Josh Suereth** 56:55 What? What?
**Liudmila Molkova** 56:57 Is it available to agents to read? Because we can tell them to read.
**Josh Suereth** 57:00 Oh, I don't… I don't know. I don't know. It was so long ago. I mean, I… I don't even know if you can still buy it. You probably can, but yeah, it was a long time ago.
Anyway…
**Liudmila Molkova** 57:10 Okay.
**ariannavespri** 57:10 Wow.
**Josh Suereth** 57:11 Alright.
**ariannavespri** 57:14 Thank you so much, bye.
**Josh Suereth** 57:16 Alright, we'll see ya.
**Liudmila Molkova** 57:18 Let's see.
**ariannavespri** 57:18 Bye. Bye.
