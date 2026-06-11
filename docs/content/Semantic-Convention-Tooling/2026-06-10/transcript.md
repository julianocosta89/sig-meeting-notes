SIG: Semantic Convention Tooling
Date: 2026-06-10
Duration: 52 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 02:22 Hello, hi, folks.
**Jeremy Blythe** 02:25 Hello.
**ariannavespri** 02:28 Hello.
**Jeremy Blythe** 03:33 I'm just setting up the… Document.
We have an empty agenda at the moment.
Whatever that means.
I think last time we were trying to figure out… Things we needed to do so we could get to a release.
So… Maybe we should look at that.
**ariannavespri** 04:06 I just put…
**Liudmila Molkova** 04:06 It's happening.
**ariannavespri** 04:07 Sorry.
No, I just wanted to ask you, like, like, last week we were talking about having, like, a similar PR for a metric requirement level, so having one for a spanning event.
And, but I couldn't, I couldn't find the, the, like, the, the issue.
Yeah, I, I…
**Liudmila Molkova** 04:34 I created it, but they didn't… tell you about it? I… I wanted to get some… Oh, cause some people, I'm looking for it.
I'm going to paste it in the… in the… Meeting. Sorry, I was going to tell it, but I'm still waking up.
Okay.
**ariannavespri** 05:05 I just wanted to make sure that I didn't, misunderstand anything, because then, coincidentally, in the meantime, then Josh assigned to me, issue number 970, That we said, maybe you should wait a bit because of that, SIG about messages that has been kind of put on hold, so I just wanted to make sure that… I mean, I didn't have the time to look at… to begin working on anything in particular, but I wanted to make sure that when I do so, then I'm actually focusing on the right things.
And that I'm not misunderstanding priorities, and that's it.
**Liudmila Molkova** 05:47 Yeah, I would say that the span links, in YAML, or… Much less interesting problem, an important problem then.
The requirement level.
So I pasted it in the chat, maybe I'll share my screen.
Brilliant.
So, this friend… So…
**ariannavespri** 06:17 Yay, amazing, amazing.
**Liudmila Molkova** 06:20 so what I'm suggesting… We have these requirement levels.
Or attributes today.
And they're kind of complicated. They support, like, this way of expressing them, or this way, and it depends on the level. But we don't actually need all of that, for signals. I don't think so. And also, we… Have 4 different levels for, attributes.
And for signals, we had a couple of discussions, then maybe we just need two.
Like, on by default and off by default.
And I'm proposing to… Piggyback on the requirement level, but limited to two options.
And it would mean a new Rust clause, because… The current requirement level for attributes is so… complicated.
**ariannavespri** 07:31 Yeah, I think there is, like, if I recall correctly, there is, like, this issue 986 that I think Josh is tackling, which is about removing That… 4… Identities is possible.
I think, I think that… It would be, like, a related… Kind of thing, if I'm not mistaken.
**Liudmila Molkova** 07:54 986?
**ariannavespri** 07:56 986, yes.
**Liudmila Molkova** 08:01 Oh, this is for attributes.
**ariannavespri** 08:04 Yeah, so there is, like, disallowing that, like, right? Because… because… because of V2, if I'm not… if I understood things correctly.
And that is like Josh's, so it's… I don't have to do anything there.
**Liudmila Molkova** 08:18 Yeah, that's… that's separate. It's… it's about attributes and their requirement level.
Or signals, like, the only thing it shares with the requirement level for attributes is the name and some basic ideas.
**Jeremy Blythe** 08:38 If you go back to the, the previous one.
I was going through the issues, and there's a really old one. If you scroll down.
**Liudmila Molkova** 08:47 Oh.
Oh, I didn't notice, sorry!
**Jeremy Blythe** 08:51 I don't know if that is… Related, or we should just close this one off, or some… something was made.
**Liudmila Molkova** 08:57 Oh, I see, yeah.
**Jeremy Blythe** 08:59 Back in.
**Liudmila Molkova** 08:59 Hmm.
**Jeremy Blythe** 09:01 Long time ago.
**Liudmila Molkova** 09:22 Yay.
And, yeah, I think… This is so annoyed.
Not sure if I need to talk about anything.
Else?
Rihanna, how do you feel about it?
**ariannavespri** 09:49 I mean, I can, I mean, I can start working on it. I mean, I don't know if you were waiting on any input from the people that you tagged?
Of…
**Liudmila Molkova** 10:03 Yeah. David, sums it up.
**ariannavespri** 10:06 Okay.
**Liudmila Molkova** 10:07 I can ping Joe, because he introduced network requirement level.
**ariannavespri** 10:12 Exactly, yes, and that…
**Liudmila Molkova** 10:17 Yeah.
Oh, sorry, you're muted.
**ariannavespri** 10:20 Oh, yeah, sorry. Yeah, I… yeah, I, I… I know about him because I had a look, you know, to, just to have, like, some, some, some, some bearings, and I saw that he was the one who authored the PR about the… about the requirement level for Matrix, so, yeah.
**Liudmila Molkova** 10:39 Yeah, I'm pinging him right now. Yeah, I was, I didn't tell you about this issue because I was wondering if they would like to have a…
**ariannavespri** 10:52 To chime, yeah.
**Liudmila Molkova** 10:53 Yeah, yeah, before you start working on this damn pinky jowl.
Okay, yeah, I, I… I think him… Maybe I should have created a chat with you, Ariana. Sorry, I'm slow still.
**ariannavespri** 11:52 Oh, no problem, no problem. I mean, it's not that I'm… I'm not fast at all. Also, next week, I'm not gonna be there, because I'm gonna be, like, away. But, I am… I might have some capacity for starting work in between… within the end of this week.
So that's why I was asking. Otherwise, it's gonna be when I'm back, which is gonna be on the 23rd of June, or something like that, so… but thank you so much, thank you so much, because, you know, you have way more insight and bearings than me, so, thank you so much for supporting me.
**Liudmila Molkova** 12:26 Thank you for volunteering to do all this cool stuff.
**ariannavespri** 12:30 Because it's cool, that's why I want to be part of the, you know, group of the cool kids.
**Liudmila Molkova** 12:39 Thank you.
Hey, jeremy, we should talk about the release breaks.
**Jeremy Blythe** 12:51 Yeah.
Happened.
**Josh Suereth** 12:53 Quick topic, sorry I was late.
**ariannavespri** 12:56 Hello!
**Josh Suereth** 12:57 Have you tried the UI in the Docker image?
**Liudmila Molkova** 13:02 No?
**Jeremy Blythe** 13:03 to run.
**Josh Suereth** 13:03 it recently.
**Jeremy Blythe** 13:06 Running the UI in the Docker image.
**Josh Suereth** 13:08 Yeah, so in the Docker image, you run the UI and then try to connect to the port that it opens.
**Jeremy Blythe** 13:14 Do you know what? I have not done that.
**Josh Suereth** 13:16 Okay, I just tried it yesterday and it was failing for me, with no errors. It would just refuse the connection repeatedly.
So, I will look into it, but if no one else has tried it, or tested it, or cares, maybe it's not that big a deal. But I tried to demo Weaver, and that used to work, and now it doesn't.
**Jeremy Blythe** 13:36 Hmm.
**ariannavespri** 13:37 So we don't even know when that started failing, basically.
**Josh Suereth** 13:40 I don't think we have a test for it, right? Because we have to build the Docker image, run Weaver UI, and then try to connect to the HTTP endpoint, make sure you don't get a connection terminated error, which is what I'm getting.
**Jeremy Blythe** 13:53 Yeah, I think what we really… there's a couple things, obviously we need to fix that, but I think, I was talking before about having, Like a… a playwright, test suite.
Because I just, I did a… I've just done a PR to add the new entity associations into the UI, so you can see that with its new… all of them, one of them. I just did that, little simple thing. And I was like, hang on a minute, how do I prove… How am I gonna prove that it doesn't break in the future? So… I can look at the… I'm happy to look at the test suite.
**Josh Suereth** 14:36 Yeah, please do. I was doing shenanigans in my personal project where I was trying to do shaders.
like, graphical shaders, and I was trying to get the AI to implement them for me.
And I had it… I spent, I don't know how long.
Not of my time, because I tell it to do things, and I go to something else, and I come back and see what it did, right? But it took me, like, several days to get it to record videos, where I have to literally take a screenshot video of the shader, and then put that in its, like, report of what it did, so I could see it.
And, it's awful. I mean, it works, right?
But it's, like, the worst version of, like, testing something works ever.
So, if there's, like, automated things we can do here, I'm well out of my element now. I used to do JavaScript in 2000, you know?
But I don't know what the latest state of things are, and from my experience previously.
Everything was flaky as hell.
My only argument would be, whatever we get, we should try to make sure it doesn't become flaky.
Selenium was what I used before.
**Jeremy Blythe** 15:47 Oh, yeah, no.
Playwright's really good, especially with, agents.
It's got a really good MCP thing.
So… You don't have to write all of that ugly, ugly, test code.
You know, go and click on this element.
with this XPath and all that.
That's a kind of a solved problem now.
Sam, I, I'll… I can take that, if you like.
**Liudmila Molkova** 16:28 It sounds though that the problem was even before that.
Just don't show any UI.
So the smoke test would be to just hit the port against the container, and that's it.
**Jeremy Blythe** 16:41 Yeah, I guess we can do a… Two things, yeah. One, do a smoke test.
That's, like, really quick. And then spend longer on a whole test suite.
**Liudmila Molkova** 17:00 Hmm, awesome.
Oh, I ran and Jeremy… oh, sorry, Joao just got back to me, and he's fine with it as well, so it's good to go.
**ariannavespri** 17:11 Okay, then it can be assigned to me.
**Liudmila Molkova** 17:15 Oh, okay.
**ariannavespri** 17:29 Yeah, because I'm not part of the team, so I… I can just, like, comment on it, and, you know, just like I did on the other…
**Liudmila Molkova** 17:38 Oh, okay, yeah.
**ariannavespri** 17:39 Sometimes it's… I don't know why sometimes it works, sometimes it doesn't, when people are not, like, approvers or maintainers, which is a peculiarity of OpenTelemetry, repo, I would say, organization. So, yeah, I will just comment on that.
And, like, as discussed, I'm gonna assign this student. That's it.
**Liudmila Molkova** 17:59 Yeah, sounds good. Thank you.
Okay.
Before we talk about race, any other topics?
**Josh Suereth** 18:21 I'll save mine for after. I've been doing design around, multi-dependencies.
And there's a lot of hard decisions to make.
I can't share my screen, unfortunately, because it's using proprietary internal tools that I'm not supposed to share publicly. That has all of my thoughts in it, but we can talk through it. I'll add to the notes.
**Liudmila Molkova** 18:41 Awesome.
So let's see what we've been considering for… Oh, this is the wrong board.
What have we been considering for the next release?
Oh, this friend, I have a PR.
And… For… for this… Issue… And even though it's cop… Pilot… is it a pilot?
Okay, I'm pretty sure I reviewed it and I was happy with it.
Okay, I'll take another look, but it would be awesome if people also took a look at just the JQ code and some tests.
okay… We have to consider the strict mark for ginger.
Don't think there was any progress on this.
But… Cannot load directory beginning with dot, also not… don't think anything has happened.
What… what was this about? The post-commit hook to regenerate published JSON schema using latest weaver. I think we… We have it, we have the check, we have the commands.
Do we need it?
**Josh Suereth** 20:33 No, I think that one was… it just… I couldn't figure out how to mark it as closed. You have to, like, turn it… you could just drag it over to closed or archive it, but it's, it was a template issue. So I think we never marked it closed, is all.
**Liudmila Molkova** 20:49 Yeah.
You're working on the multi-dependency support… SSL dependency decisions into features. I think there was some discussion on this, I have… I don't remember.
Oh, it was an old one.
So this one, just waiting for somebody to take it and work on it.
I hate Zoom overall. Sorry.
Okay, so this one I need to finish… Guiding a pilot to do the right thing… This assisted on me as well to investigate diagnostic templates. This is… we just talked about requirement levels for all signals.
Nothing interesting here, nothing we have made progress on.
Do we still want to cut the release? Do we have some cool things? We do, right?
**Jeremy Blythe** 22:08 We have a lot of… Cool things.
**Liudmila Molkova** 22:12 Yeah.
**Jeremy Blythe** 22:13 In that release, that would be cool.
One of the… One of the nice things that we get if we release it is the whole, sort of, we can do the whole round trip now.
Where you can… So, at my company, I've got a project, which is for the company that is dependent on the open telemetry.
That… That project is using the package, the new package stuff, and it packages it.
And it makes it an… when we release it, then makes it an artifact in… a GitHub artifact as part of that release. And then with the code, with the authorization code.
That's in the unreleased version of Weaver.
You can then go and get that.
It will auth… It will auth correctly so that you can get that private, artifact.
And… and then, everyone can use that from the actual released artifact, which is pretty cool. So that… that whole round trip thing is in there.
I think that's my favorite one.
There's a whole bunch of stuff in there, though, but I think that's my favorite one.
**Liudmila Molkova** 23:31 Yeah, I have a small worry about releasing metric requirement level.
And we're going to break it immediately after.
We can… Quickly remove it, for now, from the schemas.
**Jeremy Blythe** 23:53 Yeah?
**Liudmila Molkova** 23:54 And then we will be… there will be no problem releasing, right? We're in a good shape to release.
**Josh Suereth** 24:01 So, what, what's breaking?
**Liudmila Molkova** 24:04 So… We've been talking about the requirement levels for all signals.
**Josh Suereth** 24:12 Oh, right, right, we don't want to release it if that… yeah, yeah, got it, got it, got it. My bad.
**Liudmila Molkova** 24:16 Yeah.
**Jeremy Blythe** 24:19 Can we back that one out, then?
**Liudmila Molkova** 24:22 Yeah, we can, in theory, revert this for now.
**Jeremy Blythe** 24:32 I guess I'll… I'll quickly add an issue, then, for the… Making sure the UI works in Docker, and… And a quick smoke test for that.
Before we release. We need… we can't release it with a broken UI.
Or, or you can.
**Liudmila Molkova** 24:59 I was going to just add a placeholder, do you want to create a real issue?
**Jeremy Blythe** 25:04 No, you go ahead, whatever, just so we don't forget.
**Liudmila Molkova** 25:20 why can't I just… Wonderful.
Okay, and then, Let's revert… Ariana, do you think you will be able to remove it from the schema, or, send a PR to revert, or would you, rather somebody else do this?
**ariannavespri** 26:00 Maybe somebody else do that?
**Liudmila Molkova** 26:04 Okay.
I can do this… Okay, nice.
Do we need to… does anybody know if anything interesting happened recently?
**Jeremy Blythe** 26:53 Didn't really see any new… That, issues coming beyond… Things we knew about, like, last week.
**Liudmila Molkova** 27:02 Yeah.
Yeah, nothing new in the past week.
Nice. So Josh, should we talk about multi-dependencies?
**Josh Suereth** 27:13 Yeah, I'll tell you about some of the decisions I'm agonizing over that I haven't made.
That could dramatically change how we approach this.
But effectively, we'll start with, like.
two things, right? So one is, I wanted to get to the point where in live check, you can just ask something to say, hey, I saw schema URL X.
I need the schema so I can live check against it. Go get it for me right now. Right?
The second use case is actually when we resolve dependencies to, like.
chart stuff, or like, you know, generate code, or whatever.
we want to be able to have the dependencies there as well, so you could iterate over all the dependencies, like, always. So there'd be a new, like.
In template schema, there'd be a dependencies array that would just have the dependency schemas.
And I'm planning to have that be a map of, like, name dependency.
And it would have the version in it somewhere, that sort of thing. Alright, so now… This led me to think that I need to refactor Resolver.
In some fashion.
to have more structure to it, to, like, have more capabilities. Like, right now it's a bunch of raw methods, but I'm thinking of making it be a structure that you can actually ask things of.
Right? So I could say, hey, go resolve the schema URL and give me the resolve template. I could say, hey, and when it does that, it would make sure that it does dependency resolution and gives you, like, the sub-things. It would have a cache of previously seen schemas that may be at a VIX after a while, that sort of thing, right?
But some of the major decisions I need to make are… Like, do we need this to be concurrent friendly? I think for live check, we do, right? You're using async, await, Tokyo stuff in there?
**Jeremy Blythe** 29:08 Yeah.
**Josh Suereth** 29:09 Okay.
I'm thinking about, then, Making, like, a new resolver component that is 100% synchronous.
And then for live check, we have an async wrapper on top of it.
I think.
I don't know, like, I need to go check some of the… resolution stuff to make sure that's gonna work, and make sure that we have the right async boundaries for efficiency reasons, but that's kind of what I'm thinking.
And I think I need… I would do that refactoring first.
Before I start diving into, like, the craziness with dependencies, because I think that's gonna be a really significant architectural change. It'll touch a crap ton of code.
And it'll be kind of, like, half-assed a little bit, is the other problem I have. So, I wanted to run that by you all, like, does that make sense as the next step? Because that was what I was going to start on.
**Jeremy Blythe** 30:15 So, at the moment… at the moment, we ignore the schema URL, and we kind of… we… we ask Weaver to do things at the command line.
loot this thing. Let me give it… Yep.
And then it can follow the dependencies and the manifest files, if it's that thing, or what have you. So, what you're proposing is that when the schema URL comes in in the telemetry itself.
It will, at that point, go and… grab whatever it needs. At that point, it's gonna go and do the authentication it needs, if it's, like, a private repo or whatever.
**Josh Suereth** 30:51 I'm actually suggesting two things there, okay? So one is… Live check could be run without a registry specified.
**Jeremy Blythe** 30:59 Yes.
**Josh Suereth** 31:00 and then it would do that behavior. If you specify a registry.
You could have live check worn if the scheme URL doesn't match the version you're looking at.
**Jeremy Blythe** 31:10 Yeah.
**Josh Suereth** 31:11 You can also… use that as the default. So, like, you would say, cool, this is, like, if I don't see a schema URL, I'm gonna warn that I don't see one and say, I'm applying the registry you gave me locally to, like, not break users, right?
**Jeremy Blythe** 31:29 Yep.
**Josh Suereth** 31:29 So we could start actually giving warnings to people about, you're not using schema URL.
Effectively. And if schema URLs are not aligned, like, you give me a registry of X, but the schema URL says Y, we could say, hey, your schema URL's not up to date. And we can start enforcing schema URL.
As well. So, I don't want to actually make that change in live check just yet. What I want to do is make this component where you can make that change in the future.
**Jeremy Blythe** 31:57 Yes, so this ties in with… Some ideas.
around… look.
Dynamic… dynamically loading the registry for things like the user interface, or…
**Josh Suereth** 32:11 Yes.
**Jeremy Blythe** 32:11 Or anything.
**Josh Suereth** 32:13 Yeah, like, again, I would see this component get used in the user interface to basically kind of resolve and cache things that you're looking through, and so if you wanted to iterate over stuff or click through into dependencies, we could update the user interface to do that in the future as well.
**Jeremy Blythe** 32:29 Yeah.
No, that sounds cool.
**Josh Suereth** 32:33 Okay.
I think what I'm gonna do is start by making the component in Weaver Resolver.
And making… I don't know where you want the async extension, if that needs to be in a separate crate, I don't care, but I might make the default API of the component in Weaver Resolver that we can agree to.
With, like… and I'll document what the three known use cases are of Weaver UI, Weaver Live Check, and then actual, just general resolution.
Right?
And then, you know, template registration. Okay. That was the main thing I wanted to run by everyone, is I think that's going to be a significant refactoring.
I've been agonizing over, like, how to do it, when to do it. I think you saw my other PR that does all this, like, you know, template dependency crap and all that. I… it got really entangled when I started to do this, and I'm like, okay, let's chunk this out into small pieces. So that's gonna be piece one, and then we'll figure out piece two next.
Okay.
Cool.
**Liudmila Molkova** 33:32 we really need to publish some schemas in order for it to work, right? Because currently, when you're going to download the semconf.
Schema, you won't be able to get anything from it.
**Josh Suereth** 33:47 Yep.
Yep, we'd have to… so, the other part of that design will be, I think we'll have a config file somewhere. Maybe we use the cargo, or the Weaver TOML, I'm not sure, but a config file where you can say, like, this URL is here, this URL is here, so we can do some sort of mapping, and then this, this, thing can respect that.
So that way, like, we can support, you know, remote registries or registry proxies and that kind of crap.
**Jeremy Blythe** 34:18 Oh, you could add that to… in the Weaver Tunnel to, like, the auth section, where you say.
At the moment, it has a URL prefix that says when you get this URL prefix, use this auth.
**Josh Suereth** 34:31 Yeah.
**Jeremy Blythe** 34:32 you could have, when you see this URL prefix.
Use this auth, but actually go here.
If that's what you mean.
**Josh Suereth** 34:42 Yeah, I might actually keep it as a separate section from auth.
But it's… but it's effectively something similar, like, when you see this schema URL, here's the actual, like, Weaver template directory.
**Jeremy Blythe** 34:52 Okay.
**Josh Suereth** 34:52 go-to for it, yeah.
**Jeremy Blythe** 34:54 Like a redirect.
**Josh Suereth** 34:55 Yeah, exactly.
**Liudmila Molkova** 34:56 It's the same what we have in Manifest.
Actually.
**Josh Suereth** 35:01 Yep.
And like, that's kind of common for most dependency resolution systems. Like, Maven supports it, Cargo supports it, you know, in Cargo, where you can say, here's the Git repo to go, instead of the actual cargo, like, repository.
Yeah, so… it'd be something like that.
Okay.
I will put together that PR and get that out for review. I think that'll have to be in the next release. I don't think I'm gonna get… I don't think I'm gonna get much done prior to this one, but I will also try to fix the, we reserve thing. Related, I have another topic.
because I was testing some things, And, We're missing a manifest and semantic conventions, so I was unable to just run Weaver package on it if I pointed at the model directory.
It does… it didn't work, right? And then, when I tried to use it as a dependency, in some of my flows, it would fail because the manifest doesn't exist.
So… Do we have any concerns with just adding a manifest to Semantic Invention's model?
**Liudmila Molkova** 36:09 No… I'm thinking if we are ready to start the migration… so, when you had Manifest, you would add Manifest V1, right?
Yeah. Because otherwise, it's crazy.
Yep. And are we ready to start migration process and semantic conventions?
**Josh Suereth** 36:32 I think we… we almost have to for how we're federating.
like we're forcing our own hands. I guess the question is.
Are we comfortable enough that we will make non-breaking changes to publication?
going forward. This dependency thing… with the way I'm proposing it, I don't think I will make any changes to the actual published format.
Right? Like, currently, this proposal for, like, the template schema, where we have this optional dependency name thing, I need to have the same in resolve schema, possibly.
But I think, depending on how we design the resolver, I might not.
Because Resolve Schema tells me all the dependency URLs that it's gonna use, and it has, you know, the resolve set.
So, I think that I can actually use the resolver to store those additional things, and then feed into a template registry. Like, it might be that we don't have direct, struct-to-struct convert methods anymore, that we have to go through this component.
But I'm pretty sure I can build this out effectively with the way we're publishing today. Like, I don't think we need changes. The only thing that has me nervous is the… Pointer thing that we had designed.
Where…
**Liudmila Molkova** 37:48 to attribute?
**Josh Suereth** 37:50 Yeah, pointer to attribute, pointer to signal.
So, today in Resolve Schema, When you are importing something, we duplicate it into the Template schema.
So you have complete access to everything you need, right there, locally, if you're just consuming that one schema.
I think that's okay, and when we do resolution, we'll do crazy-ass things where if somebody depends on two things, and those imports are bad, we'll treat them as pointers and fix it.
When I initially implemented, I made them actually physical pointers, but that means to resolve, you have to, like.
Actually resolve the whole chain every time.
As opposed to just re-resolving on conflict?
So I… I think that I'm comfortable with how everything is, and that we have enough design space, everything will be fine, but just to, like, to tell you, like, the only thing I'm nervous about is that.
**Liudmila Molkova** 38:50 I'm pretty sure if once we go through the full loop of converting key definition to V2U and SMConf, and publishing it, and publishing stable and unstable will probably find some minor issues. I don't think we should declare any stability before we actually do this.
Or a place, do most of it.
Yeah.
**Josh Suereth** 39:14 Do you want to do that in a branch, so that we can start it now, and get the feedback we need, or do you want to actually do that on main? Like, how do you want to make that happen?
**Liudmila Molkova** 39:25 I think we can start doing it on main, like, first we can convert the definition schema. Nothing should change based on this.
Like, ideally, it just works.
Dan…
**Josh Suereth** 39:38 Anything that might… no, I think we have attribute groups now, so we're okay. Some of the namespacing shenanigans we do might be a little weird in the V2.
**Liudmila Molkova** 39:49 Which ones?
**Josh Suereth** 39:50 So, we synthesize attribute groups.
For the registry, and I think it should be okay, but it could be that our templates break. Like, that's… that's the only thing I'm worried about, because our templates expect hard-coded semantics that I tried to match with V2, but I'm, you know, there's that, like, import, like, synthesized V2 header for, like, group names.
If you're familiar with what I'm talking about.
**Liudmila Molkova** 40:15 Alright, we essentially adopted adapted, some conf templates in GenAI repo, and we use V2 there.
Okay. And it's fine. So there are some changes, but maybe we should port these templates to Weaver packages, the more advanced ones.
**Josh Suereth** 40:37 That would be awesome.
Yeah.
Okay.
Yeah, so I think maybe we can start on that, because I do want to start, like, really hammering on bugs, and get, like, into a bug-fixing mode as much as we can.
So that as we build out these crazy dependency things.
I have a good set of integration tests.
Oh.
**Liudmila Molkova** 41:01 Right.
**Josh Suereth** 41:01 Yes.
**Liudmila Molkova** 41:03 So then… on Monday. I don't know if I have time to actually do… a lot of work around this, but in Monday.
Let's present, I can present, all the stuff in some convo, and maybe there are people who are interested in grabbing this.
Especially if we break down, like we've done with the attribute amplification, we can take group by group, and we can ask people to do this if they're interested, and then we can probably move faster.
**Josh Suereth** 41:38 That sounds good. Okay.
**Liudmila Molkova** 41:39 Awesome.
Cool, and then getting back to your, topic, Where… I think we should be… we should be fine. And also, it will mostly affect Brand new things, and we didn't declare stability on them anyway.
**Josh Suereth** 41:59 Yep.
Whoo!
Cool. So I'm… I might make a, a PR.
that adds a V2 manifest.
Which I think shouldn't break anyone.
And then I might also make a PR, separate one that just migrates one particular namespace to V2.
To see if it breaks things.
**Liudmila Molkova** 42:35 Sounds good.
**Josh Suereth** 42:36 if I wasn't lazy, instead of just asking an agent to migrate things to V2, I would ask the agent to make a tool to migrate everything to V2.
Cause then we could just run it.
**Liudmila Molkova** 42:46 I have a skill, I'll send you.
**Josh Suereth** 42:49 Okay.
Shoot… Man, maybe we need to start… I've put skills in Weaver packages.
Yes! Like, have a skills section in there for people to share. Feel free to contribute one, yeah.
**Liudmila Molkova** 43:04 Yeah, I Yeah, I'll contribute that one. It's kind of naive, but it worked with GenAI.
**Josh Suereth** 43:11 Yeah, Gen AI's really good. I just, like, I feel like I'm wasting tokens and burning down trees when I… if I don't turn it into a tool, you know what I mean? Like, it feels like I should make the tool, and then the tool will be more efficient, instead of just having Gen AI do it every time, but it's so much lazier to just have Gen AI do it.
**Liudmila Molkova** 43:27 The trick is that I think Trust created the tool, the script, that did it.
But, we want to redesign things, so, like, The principle we have in… video schema that the attributes should be as flat as possible. You should not have a hierarchy of groups. If you'd have… I think I have a stupid rule in my skill that if it's higher than 2, the hierarchy is deeper than 2, then you should redesign.
**Josh Suereth** 43:57 That's awesome.
Okay, cool. I think that's all I had.
**Liudmila Molkova** 44:06 Okay.
**Josh Suereth** 44:07 Oh, also, Jeremy, I'm following up on… we have a, we have a ding on our… you got us an awesome score, right?
We still have a ding on our score for our branch protection on our main branch.
So, I've fallen up on GitHub admins about that to see if that's something other people see. The one I'm not sure of… Because I don't think there's enough of us for this, and it would be frustrating.
Is having more than one reviewer.
per PR.
**Jeremy Blythe** 44:36 Yep.
**Josh Suereth** 44:38 Yeah.
**Jeremy Blythe** 44:39 I don't think we can do that.
**Josh Suereth** 44:41 I agreed, okay.
I'll see if I can resolve all the other warnings, though, except for that one.
**Jeremy Blythe** 44:47 The other ones are, that you can… You can get an approval, and then you can still make changes, and then, and then, And then push… and then, push.
Merge.
**Josh Suereth** 45:05 Oh, I added that so our verge queue works.
**Jeremy Blythe** 45:10 It is… it's complaining about that.
**Josh Suereth** 45:13 Yeah.
**Jeremy Blythe** 45:14 Because the other alternative…
**Josh Suereth** 45:16 Remember when you had to click, like, update to latest, or… well, anyway.
**Jeremy Blythe** 45:20 Yeah, yeah, so it's moaning about… some of those things, and I'm like, yeah, but I like that.
**Josh Suereth** 45:28 Yeah.
**Jeremy Blythe** 45:28 Oof.
**Liudmila Molkova** 45:29 It's a completely miserable experience.
**Jeremy Blythe** 45:32 Alright.
**Josh Suereth** 45:33 They are warnings, though, so we could, huh, okay.
Maybe we don't do that one.
**Jeremy Blythe** 45:43 Maybe we just don't do that.
Hey, we've got a badge now.
**Josh Suereth** 45:48 Yeah, which is awesome, like, good. Thank you, that's… that's phenomenal.
**Liudmila Molkova** 45:54 The badge.
**Jeremy Blythe** 45:55 On the REMI at the top, we've got two OpenSSF badges.
**Josh Suereth** 45:59 Security audit passing, OpenSSF best practices is passing, and our scorecard is 8.7.
**Jeremy Blythe** 46:05 Yeah.
**Liudmila Molkova** 46:06 Nice.
And we're not miserable.
**Josh Suereth** 46:10 Oh, we don't…
**Liudmila Molkova** 46:12 Proven.
**Josh Suereth** 46:12 Did they sign our releases? We do sign our releases! What the hell are they talking about?
**Liudmila Molkova** 46:21 Maybe we didn't release anything signed yet?
**Josh Suereth** 46:27 No, it's, it's, it's, I think, I think it might be our tags.
**ariannavespri** 46:31 Maybe it's… there is cryptographic, maybe? There is, like, a difference between, like, just signing and having, like, some sort of verified identity kind of thing.
**Josh Suereth** 46:45 Alright.
Yeah, I don't know, here, I'll show you, I'll show you the score. Oh, you're looking at it, yeah. Signed releases.
What the heck?
It says we have zero.
**Liudmila Molkova** 46:58 Yep.
**Josh Suereth** 46:59 Oh, it does not have provenance, some of them, and some of them are not signed. So, when you push your tags.
I'll have to see who cut each release. It might be the ones I cut, I didn't sign, and I thought I was, but I released them on Windows, so it could be I don't have my signing set up correctly there.
Huh.
**ariannavespri** 47:21 But then why is it 0 and naught?
Like…
**Josh Suereth** 47:26 Well, so even when we do sign it, you're supposed to have provenance, which is where you, like, publish the signatures of people.
**ariannavespri** 47:31 Okay.
**Josh Suereth** 47:32 validated signature.
I… yeah.
Branch protection settings apply to administrators is required to merge a branch main.
Still review dismissals, disabled, right. Requiring approval, review count.
is 1, 3.
LastPush approval, that's one of the ones they complained about in updated branches. And then CII best practices, it just says… Passing, but we only have 5 out of 10?
What does that even mean? Why do we only get 5?
**Jeremy Blythe** 48:10 Because there's passing, and then there's silver, and then there's gold, and if you want to get silver or gold, you then have to be… Completely miserable.
**Josh Suereth** 48:21 Oh, I see. Okay.
**Jeremy Blythe** 48:23 So, I just went for passing, which is… It's still a bar, it's just not a super high bar.
**Josh Suereth** 48:31 I think that's fine. Honestly, an 8.7, like, we're in the green. I think anything that's super dangerous is taken care of. It's pretty awesome.
**Jeremy Blythe** 48:39 Okay.
**Josh Suereth** 48:42 It says we haven't pinned all our dependencies. Where are we using pip?
**Jeremy Blythe** 48:50 It is inside of… the new… The new live check… Action. GitHub action.
**Josh Suereth** 49:07 Oh, okay.
So we just need to pin the pip dependency in the new GitHub live check action.
**Jeremy Blythe** 49:15 It's confusing, it's not pip itself. It's complaining about the command, because the command is then pulling in… these OpenTelemetry libraries, and those are not being pinned.
However, it's a test.
Right? So that… it… that's, that isn't in, It's just… it's that commo… it's line 39.
Right.
it's kind of awkward, because then if you pin the… you can pin them, but then Renovate won't be able to see that stuff, and then you have to do a bunch of renovate stuff, and then… but this is only… this is a test.
**Josh Suereth** 49:57 Yeah.
**Jeremy Blythe** 49:58 This isn't the actual thing.
**Josh Suereth** 50:01 I think what they're worried about…
**Jeremy Blythe** 50:02 Come on.
**Josh Suereth** 50:04 Right, it's more… it's more about, pinning dependencies is about, supply chain attacks, because tests are where we get attacked. Someone tries to get into your test, get access to credentials inside the test, and then take over your project from there. So I get… I get why it's there, but it's also annoying, because you are giving specific versions.
**Liudmila Molkova** 50:25 There is a different way, people set up things in Python these days with UV.
And you set up UV, and you're on UV, and I think… It does not raise complaints, I'll check.
**Josh Suereth** 50:40 Yeah.
**Jeremy Blythe** 50:41 can renovate.
the problem I have is through… is renovate, and then… if Renovate can then look… can continue to… To renovate those pins.
**Liudmila Molkova** 50:54 Yeah, it can, because, yeah, we use a renovate and this repost, too.
**Jeremy Blythe** 50:59 Okay.
**Liudmila Molkova** 51:00 I wonder if you change it to the Python minus, pip install, maybe it will go away, because then you're using… oh, it will complain about Python, anyway.
**Jeremy Blythe** 51:16 I'll be honest, I got to that one, and I just had run out of energy to be…
**Josh Suereth** 51:20 Yeah, no, that's fine, yeah. It's just funny seeing these. I mean, we're at a 9 out of 10 for pin dependencies, that's our only vulnerability. I think that's really innocuous, so…
**Jeremy Blythe** 51:33 But some of them I had to fix.
by… Getting the hash, and then… and then running… Running the… Command.
to check the hash, like, an echoing against it, like, inside of the release YAML that is made by CargoDist that is, like, always overwritten. So there's this, like, chain of, like, horridness.
Ugh.
just to… Get scorecard to shut up.
Anyway…
**Josh Suereth** 52:08 Yeah.
**Liudmila Molkova** 52:14 Okay, we have 8 minutes left.
Do we wanna chit-chat?
**Josh Suereth** 52:21 I think we're good. Good to see everybody.
**Liudmila Molkova** 52:23 Good to see you all!
Have a good day.
**ariannavespri** 52:25 so much, bye, bye bye.
**Jeremy Blythe** 52:27 Cheers.
