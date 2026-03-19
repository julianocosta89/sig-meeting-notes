SIG: Semantic Convention Tooling
Date: 2026-03-18
Duration: 60 minutes
Zoom Recording URL: https://zoom.us/rec/share/fLsoTs0OhMd3_H1hqyHLDmFqX5eSLCrEHcnCtaG2tfGAERg0R_any2YMlhpFLRbB.A6wzzPzu4vo1d39o
============================================================

## Zoom Recording Transcript

Liudmila Molkova 00:01:46 No permission to record.
Josh Suereth 00:03:11 Hey!
Liudmila Molkova 00:03:16 Oh, hi! I thought I would be alone here. Oh, well, with James, fellow notaker.
Josh Suereth 00:03:22 Nothing wrong with hanging out with AIs, right?
That's totally normal.
My cat keeps singing on my hand while I'm trying to type.
So, apologies.
Laurent Querel 00:03:35 I agree with.
Liudmila Molkova 00:03:36 Okay.
Josh Suereth 00:03:37 Hey.
Liudmila Molkova 00:03:39 I don't.
Josh Suereth 00:03:40 Do we have an agenda? I didn't… I didn't make one today. I'm a bit behind. I have a couple things to talk about.
Alright.
So… Let's do, instead of registrate ID, and then… lineage discussions.
Okay.
So I have two things. I don't know if anyone has anything more urgent than what I want to talk about, which… the stuff I want to talk about is… Important, but maybe not the most urgent.
Oh, I should mention the filter playground.
Mmm… True.
Even segment.
Okay, let's see if I can get these PRs linked here.
Then we have… Built your playground. I don't know if you saw this, but man, I've been abusing agents a lot, so apologies.
Thank you all.
Laurent Querel 00:05:14 So we're in the… Josh Suereth 00:05:15 What?
Laurent Querel 00:05:16 You are not alone, I think.
Josh Suereth 00:05:19 Yeah.
Laurent Querel 00:05:19 Our world is doing that all over the place.
Josh Suereth 00:05:24 It's… it's just… it's interesting, how… many itches I can scratch simultaneously.
And I don't know if it's healthy or not, but, like, there are things that are always low on my priority list, and so what I do is I kick them off in the morning, and then I do my daily work, and then in the evening, I check on them, and if they've made progress, I'm like, holy crap, this is amazing, let me send it. Or I'm like, oh my god, this is the dumbest thing I've ever seen.
Let me just nuke this.
And you get both.
Sometimes in the same session.
Laurent Querel 00:05:59 Yeah.
Josh Suereth 00:05:59 Yes.
Laurent Querel 00:06:01 It's an observation on the same. Basically, Coding is becoming, just, Yeah, nothing in terms of cost.
So.
Josh Suereth 00:06:16 The AI quota is pretty expensive.
Laurent Querel 00:06:20 Yeah, but… Liudmila Molkova 00:06:22 I mean, babysitting cause not cheap.
Josh Suereth 00:06:27 Yeah.
Yeah, I'm just thinking of how many forests I'm burning down.
Laurent Querel 00:06:33 Yeah, it's more regarding that than the real cost in terms of money, at least for us.
Josh Suereth 00:06:40 Yeah.
Liudmila Molkova 00:06:40 The mental energy you spent on understanding what they did is less than writing good, but still pretty significant.
Josh Suereth 00:06:49 Yes.
Laurent Querel 00:06:50 Looks together.
Josh Suereth 00:06:50 The only thing I'm finding, this is really frustrating for me, I don't know if you've used several of the models.
But, I… I… and this is recorded, but, like, don't… take where I work in a account. I think… I think Claude is the best.
It seems to make progress the best.
Gemini is really sloppy as hell. It will not follow instructions, I have to constantly remind it. I have to basically, like, make a Rust workflow that says, actually pay attention to Clippy, actually format things, don't call unwrap everywhere.
Because it tries to.
It's really bad with a borrow checker, so I don't know if that's, like, a Rust reasoning thing or not, but I… when I use Claude, the first hit is usually way better, and it usually follows instructions and conventions in the repo better. So, it's more expensive for me.
Like… Laurent Querel 00:07:49 Yeah, it is.
I'm going back and forth between Cloud and Codex on my side, and really depending on the… There are some type of works where upload is better, and definitely there are some type of work where codex is better also.
And I agree, regaining Gemini, I'm trying, time to time to reuse it.
And I agree, it's, it's slightly veering.
Josh Suereth 00:08:22 What, what you should do, though, anti-gravity is frickin' amazing. It's, it's just… Laurent Querel 00:08:28 Yeah.
Josh Suereth 00:08:28 It… yeah, it's just, I use that with my Clawed quota.
And then when that runs out, I switch back to Gemini, and .
Laurent Querel 00:08:37 Yeah, I'm using it on the Linux box.
Josh Suereth 00:08:43 Alright, let's start talking about actual things we need to do. I think you saw I had, co-pilot Claude fix our build for muscle, which I was really happy with, because that was, like, one of those, like, tricky, stupid things where we didn't configure it right.
Yeah.
I'm happy that's fixed, and I think maybe we need a strategy I don't know if you want to do this, but maybe before we cut a release, we should actually do the thing Jeremy recommended, and, like, temporarily change the PR to run a release and build the artifacts when we make that release PR?
And then before we submit the PR, we turn that back off.
Right? So that you basically have an interim commit that gets dropped that says, hey, run the release pipeline workflow, so we know that it will succeed before we merge the PR.
Laurent Querel 00:09:39 Mmm.
interesting.
Josh Suereth 00:09:41 What do you think?
Laurent Querel 00:09:43 Yeah, looks like, I mean, yeah, a good strategy, I agree.
Josh Suereth 00:09:51 Okay.
Maybe I'll update the release notes for that later. Alright, let's move on to the first topic. So, schema URL instead of… oh, URL instead of registry ID.
This is… this is a PR that actually has some breaking changes.
So basically, I want to show you what this does, What this tries to do is modify everything to consistently use schema URL for provenance.
So, before we had this notion of registry ID, now everything is schema URL.
the path still remains for Providence, and the idea would be that path might only be a locally available thing if you're resolving from a remote registry that is not divided into paths. You would basically… the path is just gonna be the resolve schema.
Lyudmila approved this, but there were a few weird things I had to do here, but I… yeah, I just want to show you the basic gist is… Registry ID is gone, it's always schema URL. Schema URL gives you a default and a version.
I did another thing of shenanigans where, schema URL could fail to render, and, where is it?
Did I not? Yeah. So the other thing I did was I actually, Clippy does not like using once lock when you put something into, like, a hash map or a hash structure.
Because it considers it to have interior mutability.
So I actually changed schema URL now, so that we… Have a string, and then we have the range, like the integers.
for version, and then, when you call getName and getVersion, it's actually ripping them out of the schema URL string.
and now Clippy is fully happy with everything again, and we don't have to suppress all the warnings. I think structurally, it's a little bit better, too, because it's gonna use less memory, compared to once-locked strings.
Because we just have version ranges. That did cause it… anyway, that was one thing I did, and then there was a second thing, which I can jump… your hand's up, so I'm gonna let you talk, but there's a second thing I had to do where I actually changed lineage to be optional.
we were synthesizing default registry IDs in a few places, and I was putting a default schema URL of, like.
You know, unknown.
And I changed Lineage to be optional to respond to a comment from Ludmila, but I kind of hate what it looks like now, and you can take a look at the PR if you want to see it. I actually think having the default unknown looked better.
But is also confusing. Anyway… Go ahead, Lauren.
Laurent Querel 00:12:29 Yeah, my comment was about the… So we, we had a discussion regarding the reserve schema, and this idea for reusing the idea that we already have in some place where we have the, like, a mapping between for example, an attribute and a numerical ID.
So for the schema ULA, I'm just… Questioning myself why we are not using the same approach.
Because the schema URL can be super big.
So… so, already in terms of, memory usage.
We should not use a string in that case, we should use, maybe a… C or ARC STR.
If we want, really, to keep the… the schema right now.
Josh Suereth 00:13:25 This… Laurent Querel 00:13:26 an integer, if we consider that we will generalize this idea of having dictionaries of things.
Josh Suereth 00:13:34 So, so you're getting to my next point, which is I want to talk about lineage. I actually want to change lineage to, instead of remember schema URL, to be an index in a schema URL registry.
Laurent Querel 00:13:44 Okay, okay, that will solve the problem, yes.
Josh Suereth 00:13:47 Exactly, because I went through, and I was building out group lineage for things, and I'm like, we're repeating the same damn string thousands of times.
For no reason. And so first I was like, well, let me not put schema URL if it's the same as the registry. And then I was like, no, this is dumb, let's just make this an index, and have an index of the schema URLs that matter somewhere in a registry.
Okay, so we're aligned there. In terms of names and aliasing, yeah, I think we could have an alias for the schema URL, but also the name that we use, the thing that's extracted.
And Lyudmeli, you'll have to check and see if I did this right, because I did vibe code it and was super lazy.
But I'm basically just ripping out the URL part, and grabbing the second half of the string up until, like, any kind of end of the URL, and I'm turning that into the name.
So we do have, like, a shorter name to use to reference it.
which I think is what was being done before, effectively.
Liudmila Molkova 00:14:48 Yeah, I think this, it probably will fail, because… You can imagine, valid… URL, that's a different scheme approach, but that's… let's ignore it.
Josh Suereth 00:15:03 Sure, yeah. And so this is… this is the other thing that's kind of weak about this, Because I couldn't figure out how to make the previous URL parse work and not necessarily… so we force it to pass the URL parser.
Then we rip out our… the segments we need.
I guess what we could do is instead, when we parse it and get the segments, we could just pull out the range. I'll see if I can change it to do that. That might be safer.
Like, if you're synthesizing a name that's not in the original string, this referencing thing doesn't work.
Okay.
I'll clean that up.
Liudmila Molkova 00:15:52 It shouldn't be a problem.
Like, why would we use a name that's not part of the string?
Josh Suereth 00:15:59 Right, if we wanted to, like.
Unify the name, like, get rid of underscores, get rid of dashes, get rid of dots, that kind of crap.
Then… then we can't have a reference to the underlying string, we have to actually store a new string. That is the scrubbed version.
Liudmila Molkova 00:16:21 It's some very theoretical scenario. Like, personally, I'm… I don't care about it at all.
Josh Suereth 00:16:28 Alright, I'll fix this up. The other thing is, I think this is a breaking change.
I think it's an acceptable breaking change, because I don't think people were relying on registry ID significantly, but they might have been.
So I just want to call that out, like, are we okay making this a breaking change?
Laurent Querel 00:16:48 Makes sense for me.
Josh Suereth 00:16:50 Right.
Liudmila Molkova 00:16:52 Yes.
Josh Suereth 00:16:54 Okay, cool. I'll do some more cleanup on that, and we'll move on. That goes into the second thing of lineage discussions. So… My current thinking for lineage, what I want to do in V2 is just focus on provenance. So there's two pieces to this. I want a dictionary of schema URLs slash schemas, that… We're used in the resolved schema, and then lineage becomes An index into that dictionary.
for the schema URL part.
And I think what I had… I had a PR that I was working on that got really convoluted and weird, but what I want is basically, every single component in the Resolve schema will have a lineage. The lineage will have an integer which represents the schema it came from.
And that's… that's V1, or sorry, that's… that's MVP of lineage for the V2 schema.
Right? And if we need to do more, if we need to track things deeper, we do have already the ability to kind of track some refinements, where we can say, just naturally in the Resolve schema, we know that a refinement came from a metric, so we know that there's a tie there.
And with lineage tracking, I think we get pretty much everything we need out of the get-go for some of the refinements, to know where things came from, to know where signals came from, so if I import something, it will have the schema URL of what I imported it from, so I'll know where it came from.
Attributes get a little interesting. I think… I think we can preserve that. I need to go through and finish up that algorithm that was getting a little hairy for… I couldn't get the agent to do it without me hating what it did, so I might have to write that myself.
And that's fine, it'll just take me a little while, but are we okay with that for, like, a V1?
Or for M… oh my god, it's V2. I don't want to confuse anyone. Are we okay with that for MVP?
Liudmila Molkova 00:19:01 MVP of V2. So, there will be a list of schema URLs in the result schema.
Josh Suereth 00:19:10 Yeah, so what we would have in the resolve schema is we would say, here's the schema, like, we would… I'm thinking we have a, like, schema URL dictionary for the dependencies.
But I don't know how to do this effectively. Like, 0 can refer to my schema URL, and 1 could be in the dictionary, like, that gets a little awkward.
Liudmila Molkova 00:19:35 Mmm, I see. Why dictionary? It's just a list of URLs.
Josh Suereth 00:19:42 I mean, that's the same thing to me? Oh, okay. Oh, do you mean dictionary would be… I see, you're thinking Python. Yeah, to me, to me, a dictionary is just a place I look stuff up on, but the keys would be the index and the list. Yeah. It's just a list. So, let's… let's actually strawman it here.
So… we have V2… Resolvedregistry.json, or no, let's do YAML.
This would have schema URL, This would be my schema URL, right?
Liudmila Molkova 00:20:18 Huh?
Josh Suereth 00:20:19 I won't know if I like that or not.
But then we have registry, we have, let's say we have a, attribute, right?
We have a key, Sue, And this would have lineage, And Lineage would have, I don't know if we want to call it source, if we want to call it schema URL, maybe we'll just call it schema URL.
would be zero. To say, I came from, like, this, this was to find myself.
Right? Oh, so… Laurent Querel 00:20:54 I was thinking that you were… Looking at replacing the entire body of lineage by an integer.
So that will be lineage, column, 0 instead of, I was thinking that you were thinking about that.
Josh Suereth 00:21:11 Yeah, here, then I'm thinking of this, used schemas.
Liudmila Molkova 00:21:17 maybe dependencies? It would match exactly what we have in the definition manifest, just without the… Path.
Josh Suereth 00:21:30 Here's the problem, dependency.
The problem is, if I want… I want this zero to refer to both my URL and my dependency URLs.
Liudmila Molkova 00:21:45 Why, by the way? Like, who… whom does.
Josh Suereth 00:21:48 Do you think I just don't put lineage if it's the local thing? Because I could do that, too.
Liudmila Molkova 00:21:52 Yeah?
Josh Suereth 00:21:54 Okay, so, so let's, let's change this then. So, we would say dependencies, dependencies… we would have dependencies, schema URL… oh my god, I can't spell. Okay, dependencies… schema URL would be my HTTP… me.com, 1.0.0.
fancy scheming your, 1.2.3, yay. And this lineage would be… this only exists if… The, attribute came from a dependency.
Right?
That's what we're saying? Yep.
Liudmila Molkova 00:22:42 Yep.
Okay.
The lineage could exist if you… reference… Something in the same registry, right?
So the provenance would be missing in that lineage.
Josh Suereth 00:23:01 Yeah, so, so this… but this is the published schema.
So, provenance, I can actually preserve provenance for Forge and things, and I can make sure that Resolve's schema only ever publishes this integer when it's, like, not myself.
But I can still preserve the file location for Forge.
Right, so the idea would be the file location doesn't get published.
But I have it available locally for development and everything, if I need it.
Liudmila Molkova 00:23:38 So then we will only ever record the provenance.
In even shorter, the dependency schema URL index.
Josh Suereth 00:23:49 Yeah, yeah, so basically, the provenance under lineage is just the schema URL for now.
Liudmila Molkova 00:23:55 So should we call it dependency, or so, source, or something?
Josh Suereth 00:24:00 Yeah, that's why I'm thinking, yeah, we could call it source… source dependency, maybe?
Liudmila Molkova 00:24:06 Yeah.
Something.
Josh Suereth 00:24:08 Okay.
And I… Laurent Querel 00:24:12 So, yeah, I'm thinking about if we remove provenance.
Josh Suereth 00:24:20 I like the Z.
Laurent Querel 00:24:22 Will that be, will that be a problem regarding… error messages that we could emit.
I mean, the provenance, the… especially the pass, But we had, initially, Thank you.
Was used to generate messages, error messages that target a specific file, especially for the… so the… so how that will work, now, if we… if we get rid of that.
Josh Suereth 00:24:54 What… so, Lauren, I'm only getting rid of it from the serialized.
schema.
Okay. So, and only the resolved serialized. So it actually, it goes to Forge.
Laurent Querel 00:25:08 Yeah, okay, so, okay, understood.
Josh Suereth 00:25:11 locally for error messages, because we need it for error messages, but it is not published.
Laurent Querel 00:25:17 Yeah, and… okay, okay.
Josh Suereth 00:25:21 Yeah, well, I ran into… when I was first publishing it, all the file names showed up, and I'm like, what the hell? Alright, that's not what I wanted, because then it's a bunch of useless file names, right?
When you're published, because you don't have access to the files anymore.
And it had, like, schema URL all over the place, and it bloated everything dramatically. So this is… the idea here is this is just a resolved schema registry, what we want it to look like.
All the provenance stuff that we keep for error messages needs to stay.
for, for, like, a good experience inside a Weaver.
And then it's erased at publish time.
Laurent Querel 00:25:59 Okay.
Yeah, because when it's published, yeah, people that will import this registry don't really care about the specific pile that they don't own anyway, so yes, that makes sense.
Josh Suereth 00:26:12 Yeah, from their standpoint, they see a file.
Laurent Querel 00:26:15 They don't really care about the detail. Yeah, I… Josh Suereth 00:26:23 Yeah, yeah, so I think… okay, thanks for the suggestion, Lamel, this makes sense. So basically, under provenance, we'll add that it came from a dependency.
And that will come from the dependencies list.
Beautiful.
Okay, I will work on, well, I'll see if I can tickle an agent to do this, but I might need to make a design doc for it, and I'll share that if I do. Okay.
Second up, this is a fun one. I made a filter playground for WeaverServe. I don't think I can demo it, because I don't have it built in a public… visible tool, so apologies. But this just adds… I don't know if you saw back, I added a, The ability to execute JQ functions in Weaver UI previously?
What this does is a few things.
I had the AI vibe code the UI for me, because, yay.
UI code, it takes a dependency on Monaco, which might be large. Jeremy, you'll have to let me know if that's okay. The other thing that I think is more interesting is I actually extract the semantics of the error message, like line column numbers and spans of start-end locations.
And so, when we get a filter error.
from JQ, we can actually have annotations per source.
And then we have the ability here, oh, this is just turning it back into a string that we display on the command line. So we'll display, you know, it is, yeah, line, column, colon, error. The way you would expect from, like, a compiler, you know?
When you… that you get out of a JQ function, so you can see, like, where in your JQ filter there was an issue.
And then… I include the details in the error message, and then I serialize them out the API.
Oh god, I scratched the… I gotta delete that. Okay, sorry about that.
I thought I had deleted that, it must have snuck back in.
This here is, the handler, where basically, when we call the run filter, inside of WeaverServe, then, we grab those details out of Weaver error.
We extract them all and put them into a big JSON thing, and return them, and then the UI is actually able to put little squiggles on the editor to tell you when you have a JQ expression error. Yay. That was fun.
Anyway… I… personally really like this, because this is what I wanted for a long time, because I hate writing JQ, and having an editor to do it would be awesome.
It turns out that nowadays I can just tell an agent to start up the WeaverServe utility on my current project, and call that API endpoint if I describe what it is, and it will write the JQ for me. And so, I don't even need to write it anymore, but man, I like that it has squiggles, and I like the editor, so I'd like to merge it.
But, let me… apparently I have to do some cleanup, so I left my scratch crap in there. Let me kill that. But, yeah, anyone… anyone have thoughts on this?
Laurent Querel 00:29:41 That seems really cool.
Josh Suereth 00:29:45 Okay.
Laurent Querel 00:29:46 I think we all dreamed about something like that at some point, and we never did it because it was too much work.
And, personally, I'm not, a web guy, a web developer guy, but having such a solution is definitively great.
Yeah, that will improve the user experience. Yeah, the user exp… let's say the user-developer experience, depending on how we look at it.
Greatly.
Josh Suereth 00:30:21 The next thing… oh, go ahead, Jeremy.
Jeremy Blythe 00:30:23 Yeah, I was just saying, in the… on our little Slack exchange, one of the things I think we need to look at. So at the moment, we've kind of labeled the WeaverServe and the MCP both as, like, experimental, which is kind of okay.
They are… the UI… Is boogie right now.
Right, so it needs… if we're going to make this… if we want to make it more, sort of.
Take away the experimental label.
I think we need things. Like, for example, we should have some, some automated tests, like using Playwright, for example, so we can't break it.
you know, it needs… it needs the… yes, we're going to AI code it, absolutely, of course we are, right? But, it still needs the feedback back to the AI so that it knows it hasn't, like, broken something when we… right? So, at the moment, it's like… Discussion things and go, I hope it works.
Josh Suereth 00:31:27 I honestly think the value, though, Jeremy, is gonna be the actual API interface, and less so the UI. Like, in a world of agents, the API interface is what I need, I don't need the HTML.
Laurent Querel 00:31:40 Yeah.
Sure. Yeah, almost experiment, doing screenshots to, to instruct the agent to know how to move the mouse? Yes, I don't think that will fly for a long time.
Josh Suereth 00:31:54 Well, no, I'm saying the agent can actually use the Weaver endpoint directly, because we've.
Laurent Querel 00:31:58 Yeah, yeah, yeah. I was joking about, some experiment that happened, one year ago with, with Codex and Fusers, but with OpenAI, with users, trying to… P's… To crawl the web and making screenshots everywhere to, do things like a human when there are APIs everywhere.
Josh Suereth 00:32:26 Yeah.
Well, well, I… but I agree with you, Jeremy. We should probably, like, to remove the… We could think about two things. We could think about WeaverServe, the API endpoint going stable, and the UI going stable separately, but it might make sense to do them both at the same time, and we should add integration tests. The other thing I wanted to talk about there was… so, Either serve.
Allowing multiple industries… within… I was doing some investigation into this, I would like to get WeaverServe, like, baked on a cache of schema URL to resolve registry.
And I would like to see if we could get that same thing for live check, where we have a system where, on demand, if you say, I need access to the semantic conventions for this schema URL, it can go resolve that schema URL, pull it in as a resolved dependency or whatever we need, do the indexing it needs for UI, get LiveCheck up and ready, and so if we can change some of LiveCheck to say, cool, you get telemetry against a particular schema URL, live check can be configured to go grab that data.
and then verify against the schema URL it sees, right? And I wanted to put together a proposal around what that could look like, and then first drive that out of WeaverServe.
Jeremy Blythe 00:33:59 It's interesting how… Where we seem to be gradually evolving Weaver from a CLI tool to a service that's running somewhere.
Liudmila Molkova 00:34:11 It doesn't have to be a service, right? It can pull them at a startup time. You can even pass them explicitly. It's still a CLI.
Laurent Querel 00:34:23 Yeah, it's a perfect solution, because we are also using it in CI, with LifeCheck, and… things like that. We are using it to generate, traffic.
And now we have a UI, so yeah, it's a multiform thing.
Jeremy Blythe 00:34:39 Yeah, it's great. It's like… Josh Suereth 00:34:42 Well, Jeremy, I blame you for giving us the idea.
Jeremy Blythe 00:34:46 Hannah, I'm sorry.
Josh Suereth 00:34:47 Like, you had too many good ideas. We're like, maybe we should do this.
Jeremy Blythe 00:34:53 Yeah, I should say… Laurent Querel 00:34:54 And the next step is to generate a UI for Ginger.
Josh Suereth 00:34:59 I actually thought about that.
Laurent Querel 00:35:03 I can imagine.
It's one of your advance training in the morning, and you control what it does during the evening.
Jeremy Blythe 00:35:16 Ginger is solved, right? Ginger is now a solved thing. You just ask… You just asked Claude, or whatever. Hey.
make my template. No, I don't like it. Make it… make it this shape. It's… you know, it's… it's done.
Josh Suereth 00:35:30 That's actually the third thing I wanted to start. So, first of all, if you guys are in for this WeaverServe thing, of allowing multiple registries to be pulled and apply a check and stuff, what one thing I'm thinking about for the future of MCP, if you guys haven't… Jeremy and I had a brief discussion about this, but it seems like things are going the way of skills, where basically we would have a, you know, food at… or skill.md.
that describes how to use Weverse CLI, Serve, etc, to get information.
And then we just dump lever itself, or describe Now it's downloaded.
And this would be something we would, like, distribute, like a Weaver skill that you can download and use. And we don't need, necessarily, an MCP anymore, because we can have it directly use, our CLI and WeaverServe.
If those APIs and things, like, if the CLI itself is well described and self-describing, if the serve is well described and self-describing, we can put skills together which give us that, what MCP would otherwise do.
Unless we think there's a use case that only MCP can solve.
This might actually reduce some of our complexity here a little bit, in terms of, like, what we have to maintain.
Go ahead.
Jeremy Blythe 00:36:59 I think.
Laurent Querel 00:36:59 For me, the… oh, sorry, go ahead. First.
Jeremy Blythe 00:37:03 I've… I've actually been using the Weaver MTP, my… my… in… with my, with my team.
Yeah. Against our model.
I… It's been awesome.
So, I'm happy, but the outcome is awesome. I think you can achieve the same outcome using skills and CLI.
Right? But the outcome is awesome. I just… I'd love people to… like, I was just using it this morning. In fact, what I've done is I've written a skill to use the MCP.
So the skill says, hey, go and crawl this whole, project that this person's written to do a semantic conventions review. So I want to find all the telemetry that you've made, and I want to compare it against our semconf library that is loaded into Weaver in its registry.
And… just hammer away at it and come back, and then it can even make a… it can even make a PR, and it will put comments under it saying, hey, this is a thing… oh, this is missing from our registry, you should probably add this as an attribute into the… like, it just does the whole… it's… it's amazing.
Josh Suereth 00:38:08 Yeah.
Jeremy Blythe 00:38:09 So I don't want to lose… that's kind of a really powerful part of what we're getting. Now, it doesn't have to be an MTP, no.
but provided we still get that. And actually, just this morning, I was thinking.
It… when you ask it to go and, like, do this thing where it crawls over and it's… it's calling search, it goes such, search, search, it's doing loads of searches.
Josh Suereth 00:38:30 Yeah.
Jeremy Blythe 00:38:31 And the search API returns the whole block of everything, when really.
What we need are… we need some other tools in there that go, like, just list me all the attribute names.
And you'll get, you know, you'll get 2,000 attribute names, just so it's got, like, a reference to start from.
Laurent Querel 00:38:49 And things like that. Maybe we can expose the GQ endpoints?
Jeremy Blythe 00:38:53 It's… Liudmila Molkova 00:38:54 The cloud would actually do this, it would JQ over the output.
Josh Suereth 00:38:59 Right. You know, Jeremy, just describe… so do this, try this. Take your skill, Describe the WeaverServe command.
and how it can discover what it's able to do. And there's a filter command with JQ in it.
Where it can do exactly what you're saying. Already.
Like, WeaverServe already supports that today. The thing that I showed you where I'm.
Jeremy Blythe 00:39:23 Energy.
Josh Suereth 00:39:24 The JQ filter already is in the API, it just wasn't exposed with the UI.
So you could even try… that… I was doing that. That's why.
Jeremy Blythe 00:39:33 Okay.
Josh Suereth 00:39:33 Like, I would try it out, like, see what you think. What I want to do is I want us to be able to get the use cases that you're talking about as quickly as possible.
But I don't want to build it twice. And so I keep looking at… we have… we have, like, HTTP use cases and, like, loading in multiple things, we have that for the MCP. And I… I'm trying to decide which one should I target with my time, right? If I'm going to target one of the two.
Yeah.
Laurent Querel 00:40:00 It's so… Jeremy Blythe 00:40:00 One more focus on that.
Laurent Querel 00:40:01 Let's go in.
Jeremy Blythe 00:40:03 I'm really sorry. I have one more thought on it.
If our loading of a registry, now, from a resolved registry.
And we wrote it in Rust, so it would be super fast. If that's super fast, do I even need WeaverServe anymore?
Can I just have it? It will take another… fraction of a second to do the resolve, ask the question, give me the result back on the CLI.
Josh Suereth 00:40:27 Yeah?
Jeremy Blythe 00:40:28 And I'm done. I don't actually need… so… I don't need anything to hold any states anymore.
Josh Suereth 00:40:33 Interesting, yeah, so if we have the right CLI commands.
and we're fast enough in the CLI, I like that direction.
Yeah.
Okay.
Laurent Querel 00:40:46 Yeah, my point was… not really aligned with that. It was a little bit in the opposite side, but I can understand the argument.
that the state is outside in that case, and if we have a super-fast CLI, maybe that will work. I'm not sure of that, because, the fact of having an MCP server with a state that is conserved and kept inside this process offer some, I think, properties in the future that will be hard to achieve with the approach that you are saying, because it means that we will have to multiply in the CLI options to… accept state, a transitory state. I mean, okay, I think the example of you provide, a publish, a publish registry, and you do some stuff on it, will work.
But if we, at some point, we need to work in a multiphase, Mistage, transformation on something That is, the production… the first step is the production of one command, the second step is the production of second command. Then we will have to… to add, CLI entry, That are able to… To be filled with those, intermediary states.
I'm not sure that that will be super, human-friendly, so the question will be, is it something that we need to put into the CLI just for the agent, or… you see what I mean? For me, the fact that the MCP server keep a state, has some interesting properties.
And for me, it's complementary with the skill.
approach.
Jeremy Blythe 00:42:44 Yeah, and if we want to keep the… user interface.
Then we need something that's running.
Anyway… So I got that. I was just like… Laurent Querel 00:42:57 Yeah, yeah.
Jeremy Blythe 00:42:58 What if?
Laurent Querel 00:42:58 We could imagine, we couldn't imagine not having UI, I'm just having an API, and then MCP will work.
That will work, but… Yeah, the comfort of having a UI for the exploration, is… probably nice, and at least it's always the same experience. It's not a generated cloud UI, just for the… for 5 minutes, and you come back tomorrow, and it's a different one.
Liudmila Molkova 00:43:38 I'm curious if we… neat… MCP as a part of… Weaver, because it only helps The agent talked to schema.
But Agent can… Know this schema.
And work with it without… MCP. The Weaver is then the skill… like, if you have a result schema, then Weaver skill is needed to materialize it for the agent to… or maybe agent doesn't even care.
Josh Suereth 00:44:11 I've had success with the agent just reading the schema from our CLI, and then interacting with it directly.
The thing that I think is helpful is, like, what Jeremy said, if it has to do a bunch of searching.
giving it a fast path to search for, hey, what attributes look like this, right? Like, you've seen agents do this all the frickin' time, where they're like, do a search for this. And so, one of two ways to do it is they will do a search where they will grab a giant document, and then use all of your tokens to look through it.
Or you can give them a hot path, where, like, you give them a search capability.
And so, which is less tokens. Now, I don't know how much we… anyway, go ahead.
Liudmila Molkova 00:44:52 In the exact search is a rare case.
And, having it… In a file and some… some basic rag over it.
the agents will do it at some point. I think it's… today it's JQ, but just rag over this thing would be… Easier.
Josh Suereth 00:45:13 Yeah.
That's fair.
Jeremy Blythe 00:45:17 The other nice thing that I've found with the search.
is that I do dash dash include unreferenced, so I get the entire SEMCOM library.
Which now is big.
And it's a… it's… when it's searching, it's also searching over all of the brief and the notes.
So, my skill says, if you don't find this attribute.
go and, like, go and find something that maybe it is similar to, based on the context that it's seen, how the attribute's being used. Then it's using all of those rich notes and briefs.
To go, like, oh, it seems like maybe you're talking about this thing.
And it makes a suggestion for the… in the pull request.
Which is pretty cool.
Liudmila Molkova 00:46:06 Yeah, that's cool.
Josh Suereth 00:46:08 Okay, I want to get to next steps, because I think we're… we have a lot… there's a lot of cool stuff we can try.
Lot of cool stuff to go.
Jeremy Blythe 00:46:16 Maybe we need to just try it.
Josh Suereth 00:46:18 Yeah, that's what I'm saying.
Jeremy Blythe 00:46:19 fun.
Josh Suereth 00:46:20 Yeah, next steps… next steps, I think, is, yeah, like, let's… Let's try a CLI-only skill.
Let's try a, API only skill… oh, sorry, API plus CLI only skill.
And then let's decide on MCP.
API, CLI.
after 20. Does that… does that sound fair?
Jeremy Blythe 00:46:47 Sounds great.
Josh Suereth 00:46:48 Do you agree with this goal of, like, I want to try to, if we can, I know that agents are crazy, we should do lots of exploratory stuff, but I want to get to a goal of when we build core features.
that we can focus our efforts a little bit. So, like, when I was going through this, you know, making live check dynamically load registries based on schema URL, What I don't want to do is build that twice, or 3 times, or 4 times. I want to build it once and have everyone benefit from it. So, that would mean the CLI should get it, and then Serv will get it, and… MCP would get it, right?
Jeremy Blythe 00:47:25 Yep.
Josh Suereth 00:47:26 Okay.
Jeremy Blythe 00:47:28 I think it makes perfect sense, yeah, to do that.
Josh Suereth 00:47:33 Man, that was a really fun discussion. Let's move on to another fun discussion, PR.
Ducks.
You want me to, you want me to show that?
Liudmila Molkova 00:47:45 Yeah, so most of it is trivial. There were… a couple of things I wanted to discuss. The first one is… Yeah, there is this docket just, mostly I generated… but blessed and reviewed, explanation of what's going on in JSON schemas.
The important thing is I don't want to have file format for Materialized SchemaForge, or Div, because we don't publish files yet.
And that you consume it with, generate, or with templates.
And you transform it in whatever ways you want.
So, I'm not adding any file formats for them.
And also, I'm removing this externally visible name of the Fort Registry to materialized registry, because nobody outside VIVA would know what forge means.
Laurent Querel 00:48:46 Yeah.
Liudmila Molkova 00:48:51 And I have that… bike shady thing that I want to talk about.
So we have file formats. They are something slash 2.0.
2, and then something else.
There is no point in this. I mean, there is no point in, we decided not to have somewhere in definition.
And we decided to have somewhere in… published things.
Just because it's somber, and just because currently what we have is somber.
Maybe we should just stream it down to the major version everywhere?
Josh Suereth 00:49:45 I'm of two minds here, but yeah, I'd be… I'd be willing to do that.
The reason I think we don't use SEMVR is because of the OpenTelemetry specification that's marked stable, and we're trying to, like, have our version be the same as that file format from that thing. So if your OTEP changes it, and people agree to it, great, let's do it, and that's probably worth trying.
Yeah, that's.
Liudmila Molkova 00:50:10 Let's, let's try it.
Josh Suereth 00:50:12 Yeah, I think we might make additions to version 2, but, like.
we would make additions in a way that's backwards compatible, I think.
Liudmila Molkova 00:50:21 If we do this, then we would say allow extra properties everywhere.
Josh Suereth 00:50:27 That's what I'm thinking, yep.
Liudmila Molkova 00:50:29 Okay.
So, let's review this, and let me create another, issue and follow up on that separately, because it's, Artug and all.
Josh Suereth 00:50:41 Yeah.
The other, the other thing we could do is, if… if we wanted to have the version number be significant.
we could actually have Weaver crash if it encounters a major, minor version that is, sorry, a minor version that is more advanced than its current version that it knows and understands. So this is a… so basically, like, we would support 2.0.
But if we see 2.1, we'd fail.
Liudmila Molkova 00:51:16 Yeah.
So we can keep… like, the… let's get rid of the patches, no matter what.
I don't think.
Josh Suereth 00:51:24 Gotchas, yeah. But, like, when it comes to definition things, unless we have that mechanism I was talking about, where, like, it's safe to ignore an addition, and that's what patch version means, we could do that, that'd be fine, we could keep patch versions, and patch version schema would… might have new things in it, but those new things are always safe to ignore.
And then the other version bump would be things that are not quite safe to ignore, where you want old versions of Weaver to fail and say, hey, you need a new version of Weaver to resolve this.
That… it's… that still feels awkward as hell to me, so I still think just two versions is fine.
Or two numbers, I should say.
Liudmila Molkova 00:52:10 Okay, let me think a little bit more about this, but let's try to do it, because it bothers me, however minor.
Josh Suereth 00:52:19 Yeah.
We need to set ourselves up for future success, and not over-engineer all at the same time. And Weaver has been a balance of that, where we started off with, let's do the hard thing, and then let's work backwards towards ease of use.
I think we're finally starting to get towards the ease of use part. But the core has been really helpful for us, I think, in a lot of places.
Liudmila Molkova 00:52:46 Yep.
Cool, so then there is not much here. Oh, I'm adding, head and paste, schema URLs to diff.
Josh Suereth 00:53:02 Nice, yeah.
Yeah, so that… I think there's not much else to look at here.
We got rid of default.
Liudmila Molkova 00:53:15 It's just written down in a different way.
Josh Suereth 00:53:19 Oh, did you not want me to get rid of the unknown method then? You asked me to.
Liudmila Molkova 00:53:24 On the provenance, because it's not used.
Are you getting rid of it in the schema URL itself?
Josh Suereth 00:53:31 I did, yeah.
Liudmila Molkova 00:53:32 Okay, I mean, let's make… make your PR in, and we'll figure out.
Josh Suereth 00:53:37 No, let me go clean… let me go clean that sucker up. I think there's a bunch… anyway, there's a bunch to do based on the discussion we just had. I'll go clean it up.
Liudmila Molkova 00:53:47 And we use it so extensively in tests, and it's useful.
Dear, at least.
Josh Suereth 00:53:54 Yeah, I think it's absolutely critical and tests. What I did was I made it optional in places where… anyway, I'll go clean up my PR and make it less gross. And I think this is my number one.
going forward, real quick, since we have 5 minutes, hopefully everyone who's going to KubeCon, have a great time.
I wanted to do a little bit of next release planning, if that's okay, in the 5 minutes that we have.
of, like, things we want to get done. I would like to get to the point where we can call V2, and Alpha, or beta, or whatever we want to call it, where we're like, hey, people take a dependency. So this means we need to verify that Publish is working, I want to get lineage in and finished before that.
Is there anything else that we need?
here… for V2.
Liudmila Molkova 00:54:53 I'm not sure we have an issue, but I remember the discussion about dependencies, and whether we… Josh Suereth 00:55:03 These multi-dependencies.
Liudmila Molkova 00:55:06 Not even multi-dependencies, but whether we have… we allow… Transitive dependencies to be public, to be accessible.
Josh Suereth 00:55:18 Oh, oh, oh, yeah, we currently have the imports thing. Yeah, whether or not you can see a transit dependency or not. Some languages allow it, some languages don't.
Liudmila Molkova 00:55:29 I think that the problem today is that, let's say, I… depend on… A depends on B, B depends on hotel.
If I don't see Otel, so Ruby.
I cannot even take Autel as a dependency, because we allow just one dependency.
Unless I use definition schema of B, and then I can see through.
Josh Suereth 00:55:55 No, no, no, so this is… yeah, that, that sucks.
What… what do you think about allowing multiple registries, multiple dependencies? I think with the schema URL fix and lineage, I can actually resolve the dependency hell problem. Yeah. Okay.
Alright, let me, let me add that, Do we have… do we have that defined here somewhere, of multi… I'll just add it to consider for next release as a raw item.
Add… multi-dependency support. I think we're at a point… I think we added all of the junk that we need to make that… to actually do that… this… this… next release. So… I might be overconfident, and Laurent, you can make fun of me if I am.
Or if you have time to do this, feel free, but I… I think with all the structure we put in place around resolver and dependencies, it's probably time. So with the schema… I'll get the schema URL thing in first, because again, that's a requirement. I need the ability to disambiguate.
And that solves that for us. So let's get that in.
I might need Lineage 2, because I need it in resolved schema to deal with dependency hell.
But we'll say the next release will be gated on allowing multiple versions to be specified. How's that sound?
Alright, any concerns, Jeremy? You might know how to step away, I know.
Jeremy Blythe 00:57:27 Sorry, I did. I was wondering, where are we at with… So, sorry, I took my eye off this for a week or so, I got really busy at work.
Should I now be able to, with the release, should I now be able to do a package?
get that manifest then resolved, YAML.
And I should be able to go weave a serve, and point it at the directory that's got the manifest and the resolve YAML in it, and it should serve it. I should be able to do that today.
Josh Suereth 00:57:59 Absolutely, 100%, yep.
Jeremy Blythe 00:58:01 Okay, I must be doing something wrong. Currently, when I do that, it says… it panics and says it's trying to convert V2 to V1.
I'll look into that some more, but… I've just got it in a local directory.
And the… it's pointing… in the manifest, it's pointing to… to resolve YAML.
So the… Whatever it is. The schema URL says .slash resolve.
And it, yeah, it panics.
Josh Suereth 00:58:37 Is it Resolve V2 in the file format?
Jeremy Blythe 00:58:41 I did a… I did a… Yes, it does. The file format is, is, yeah, 2.0.
Josh Suereth 00:58:49 And you're using V-v2 for both of these?
Jeremy Blythe 00:58:53 Yes.
I'll go through the sequence again.
I just wanted, before I… Josh Suereth 00:58:59 Boom!
Jeremy Blythe 00:59:00 dig deeper, I want to make sure it actually is something that should be working now.
Josh Suereth 00:59:04 No, no, no, there's one thing we're missing. That's, that's a good call-out, Jeremy. So, Right now, the way that you would have to do that is you'd have to make a new definition registry that depends on the other one, include all references.
I don't think I fixed the actual… Like, actually, the Weaver source directory flow only allows registry definitions. It does not allow you to skip straight to resolved right now. I don't think I fixed that.
Unless you did Libbilla, but I don't think I did that.
So, I think there's one last fix to make. Like, you, you should be able to do that, we just have to fix the Weaver, the Weaver thing. Okay, let me, let me add that here as an item.
Jeremy Blythe 00:59:50 Yeah.
Josh Suereth 00:59:51 That might be a quick fix, though. But yeah, that doesn't work yet. Apologies.
Where's my… Where's my add item thing? Where'd you get… oh, there it is. Okay.
fix uber-r, and then register.
Laurent Querel 01:00:09 I have to go, sorry for that.
doing retition.
Josh Suereth 01:00:14 Excellent.
Let's do that, yeah.
Okay, good draft.
Alright, awesome. Thanks, everybody.
See y'all.
Liudmila Molkova 01:00:24 Thank you.
Jeremy Blythe 01:00:25 Bye-bye.
