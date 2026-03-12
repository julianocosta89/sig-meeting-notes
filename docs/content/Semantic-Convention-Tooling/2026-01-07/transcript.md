SIG: Semantic Convention Tooling
Date: 2026-01-07
Duration: 60 minutes
Zoom Recording URL: https://zoom.us/rec/share/uJXjnywt0vBQX3KSNap51hGlbF--CziMDedCZGBcL7Ff6gFkEff4CSxKJVnt5ISo.Ztlp0LuSjuU2arYO
============================================================

## Zoom Recording Transcript

Laurent Querel 00:00:19 Maybe it wouldn't.
And a PDUR.
Jeremy Blythe 00:00:27 Hello.
Happy New Year!
Laurent Querel 00:00:33 Yeah, you do.
ariannavespri 00:00:34 You as well, thank you.
Josh Suereth 00:01:02 Hey, can you hear me?
Laurent Querel 00:01:05 this…
Josh Suereth 00:01:06 Okay.
I'm on a… a new laptop, and my camera's not working, so apologies.
Alright, I'm gonna try the camera again, and see if we can get it to work.
Alright.
It's a Chromebook, which I've never had before, but, you know.
Yeah, it doesn't feel like a computer, that's all I'll say.
I'll do one quick rant while we wait for Vanilla, because I think she might be the first topic, but, or she's the second topic.
There was a dream I had once where I wanted to just be able to plug in my phone.
To a, like, docking cable, and have that be a computer.
Right?
And a Chromebook really feels like that, if you've used a Chromebook, because it's actually, like.
feels kind of like an Android operating system, it has, like, a store. I know that Windows has been moving that direction for a while.
And I realized that… okay, I'm old and grumpy, I don't want that to actually be true. I kind of miss having a terminal… Having a computer, you know.
Yeah.
Laurent Querel 00:03:13 Yeah.
Josh Suereth 00:03:18 Anyway.
Laurent Querel 00:03:19 recipe.
Josh Suereth 00:03:21 Alright, I think we have a really exciting week here, to talk about. Hope everyone had a really great break.
But let's… let's jump into it.
Live check for OTEL instruments. I think this is Lyudmilla?
Liudmila Molkova 00:03:38 Yep, this is me.
Give me a sec.
We can go, maybe, to start with something… Elves?
Josh Suereth 00:03:50 Okay, let's start with MCP, then.
Jeremy, you want to… or no, actually, this one's easy. Let's do the Scheemars one, because this is related to MCP.
Jeremy Blythe 00:04:02 Yeah.
Josh Suereth 00:04:02 yeah, I'll comment on this. So, I saw in your… PR that you were using, SkiMars 1.0.
What we're blocked by is that ordered float does not support 1.0.
And so, when you move to 1.0, ordered float breaks. So we have a few options. We can stop using ordered float.
And write our own wrapper to ordered Ferote.
That does the same thing as ordered float, and has schema support.
There are two PRs.
In fact, I don't know why I don't like one of them, but there are two PRs that fix ordered float for SkiMars 1.0. One to the SkiMars project, and one to the ordered float project.
Order Float doesn't want to bump to Scheemars 1.0 because it's a breaking change, and they don't want to break their users, so they said, why don't you make this change in the Schemas project? The Scheemars project has not reviewed the PR in 2 months.
So… we're kind of in a rock and a hard spot of… we have, oh, my camera died again, wonderful.
Wait… We're in a rock and a hard spot of, basically, we want to move to 1.0, ordered float could have support trivially.
But because we don't own ordered float, like, we don't own the type, we actually can't provide.
a trait that implements schemas for ordered float in our library. Unless we wrap ordered float in our own type.
So, if somebody… like, if you think that's what we want to do to work around this, we can. We… that's option one. That, I think, is the safest option and the most annoying.
Second option is we can point at one of the branches of ordered float that support Scheemars 1.0.
from GitHub, in cargo.
That one, I'm… I don't really like that much, because we won't get any other fixes from ordered float, in case there are vulnerabilities or something that gets batched, so I'm not happy with that either. And option number 3 is, we… We don't use ordered float, and we change any comparison Operator that we need to use to, like, manually write the floating point comparison arithmetic that we need.
where we need it.
Those are kind of the three options we have.
Oh, and option number 4, which is what I was doing… was just waiting.
Because I assume, given the number of people that use ordered float, this will eventually get resolved.
Jeremy Blythe 00:06:41 Where are we comparing flirts?
Josh Suereth 00:06:44 We have partial order on things that use float. I think examples has partial order on it. So, that's, that's at option 3 of, basically, we would just manually implement partial compare.
For examples. I don't think artists used many places.
Laurent Querel 00:07:03 It's also used because, for the duplication reason, When we, we deduplicate… Groups, for example, or attributes, groups in general.
When we reserve.
We have to compare the entire, group So all the values that, are part of the group, I think it's, One of them in usage.
Josh Suereth 00:07:35 Yeah, but I'm pretty sure with that, Lauren, it's just, If we look at where ordered float's used, it's used in value, and it's because of examples.
Like, I believe if we just implemented partial ordering.
on examples manually, we wouldn't have.
Laurent Querel 00:07:55 Oh, okay. Yes, that could be it, yeah.
Josh Suereth 00:07:58 Because, let's see, this is it here.
This is the only usage of it, right here.
And… I think if we just implement… we'd have to implement partial equals… I think hash is fine for float, but I can't remember.
Laurent Querel 00:08:18 Yes, I think so.
Josh Suereth 00:08:19 equals… If we implemented partial equals, equals derives automatically from it, so I think we just have to implement partial equals manually on this enum.
Laurent Querel 00:08:28 Yeah.
Josh Suereth 00:08:28 And we should be fine.
Laurent Querel 00:08:29 You know, that's the best solution.
Josh Suereth 00:08:31 Yeah, okay. So… so, Jeremy, that… if… if you… if you want to take that over.
All we have to do is drop the partial equals here, and implement it manually.
And then drop the whole ordered float dependency.
Jeremy Blythe 00:08:49 Okay.
Let me make a note.
Josh Suereth 00:08:54 Yeah, I actually think we might be at a version of Rust where floats now have an ordering.
I know that they're working on stabilizing that.
You know how they, they, they just recently got NAN working in… Compile time static stuff.
So, I don't remember if floats are ordered yet.
Anyone… anyone a Rust aficionado that might know?
Okay.
Jeremy Blythe 00:09:25 Sorry, just to be clear, you're saying drop ordered float from here.
Josh Suereth 00:09:30 Yeah, drop ordered float here, like, get rid of this and just make it be an F64, and then you'll have to implement partial equal By hand.
Jeremy Blythe 00:09:38 Okay. Yeah, again.
Josh Suereth 00:09:41 Yep, the other thing I did in this… this check, by the way, is I basically did the same thing for something else. What did I change?
Right. Oh, this can be automatically derived, so you need to do that, but there was another… That's just a change in how the YAML works.
Right, so anywhere where there was a custom JSON schema, you actually have to use this macro now. All the types are now hidden.
So, you can just steal that from there, but I did something… Right, the SEMCOM version. I, I made… you know how I was saying, like, we could wrap it and define our own… ordering and things. I actually had to do that for, SEM version, because we didn't have the appropriate schema or support. So this is an example of how to do it, if you're curious.
Jeremy Blythe 00:10:39 They're not sure.
Josh Suereth 00:10:40 can implement your own JSON schema, on… On the thing that's not supported with 1.0.
I… I ended up doing that for Semver, because I couldn't get Semver to work otherwise. So we make a transparent type, like a… I think this is called the new type pattern.
Laurent Querel 00:11:01 Yes, when you abrupt something?
Josh Suereth 00:11:04 Yep.
Laurent Querel 00:11:05 Yes.
Josh Suereth 00:11:06 Yeah, so…
Jeremy Blythe 00:11:07 sharing that screen, John.
Josh Suereth 00:11:08 Oh, oh, oh, oh, oh, sorry. This one here. So this is, under Weaver version. This was the other one that was problematic.
And this one I wrapped.
Jeremy Blythe 00:11:19 Got it.
Josh Suereth 00:11:20 But this one was a little less annoying to deal with than ordered float wrapping.
Because basically I had to do what I'm suggesting you do now, Yeah, the, so for me, I had to manually implement the JSON schema.
Jeremy Blythe 00:11:37 And again, if you implement JSON schema manually ever.
Josh Suereth 00:11:41 In the new one, you have to… you basically just copy-paste what the result definition is.
In 1.0.
So, I think if you make this change, you get rid of that one change there.
What did I do in attribute group? Yeah, we just got… anywhere where it was previously broken with that allow unused qualifications is now fixed, so you don't need that anymore. So these, like… Macro expansions that we hid, you can get rid of them.
Jeremy Blythe 00:12:10 Nice.
Josh Suereth 00:12:11 Yeah.
Cool. If you have time to take that, please do. If you want to just take this PR and own it, like, feel free to take it. If you want to make your own new PR, whatever, I can kill this one.
Jeremy Blythe 00:12:24 Yeah, yeah, sure, I'll take a look. It's… It's an incompatibility with the Rust MCP library.
That's… that's where… Okay, no, yeah.
Josh Suereth 00:12:37 Well, yeah, it… I ran into that as well.
with pretty much… SkiMars 1.0 really… It pulled a number on us with its braking change.
Okay.
Ludmel, are you ready for your topic, or should we move on down?
Liudmila Molkova 00:13:03 I'm ready.
Okay. Can I share?
Josh Suereth 00:13:06 Yeah, go for it.
Liudmila Molkova 00:13:09 Okay, so I've been playing with LifeCheck, and I wanted to use it for Gen AI, validation?
Just because we have an overwhelming number of PRs that nobody wants to review, and I want to automate it.
But, so what I've tried… And it's pretty much work.
R… So, I have this wrapper around Weaver, using test containers. We have a Weaver container.
It can start… the… it takes a bunch of parameters, like the schema version to validate against. It has the VIVER version, the policies, I hope we can get rid of templates at some point, but we have templates. Anyway.
So we can start this container, it would start the weaver. We… at some point, decide to end life check, right? And then… this is the part that they want to discuss and improve. So this… this took me, like, a reasonable amount of time to write reliably.
What happens is that, okay, sometimes the container doesn't start because there are errors in my policies, or errors somewhere else, And… I need to read logs.
Or maybe it fails during the check, because the rego policy is actually evaluated at the check time, and then it fails during the check, somewhere when telemetry is received, and again, I need to read logs to understand what happens.
And finally, when I get the… if everything went smoothly, I need to read the report and get the violations and fail on them, so that when I, get the… see the fail check in CI, that I can easily go and find what actually is problematic.
So, it's all possible now.
But I think we can improve it. The first improvement I think we can make is that why don't… response I get here at the stop include the report. I think it's… it was suggested also when, I did our talk, Jeremy, I think Robert, from GoSeq also suggested that maybe we should just return the full, report here.
And not just the report, maybe we should also return errors here.
that happened during evaluation. We don't stop fever process, we just record an error, and then we return it as an evaluation error in the special section in the report.
maybe it shouldn't be stopped, maybe it should be status, I don't think it's an interesting discussion, maybe we should have both, but maybe we should just return everything in the stop?
And it will save someone from using the REST API of this, from needing to ever read the files. The file permissions, mounting, volumes, all the stuff goes away and becomes much easier.
So, but other than that, it's worked pretty well.
I automated the spam stuff with custom policy.
Here, it could be better, but it's fine?
So the part that they ended up also doing… is… Okay, I actually pretend that I got full report here. I just hide it behind abstraction, and then I can validate that I actually seen certain metrics that I expected to see in certain logs.
So this is pretty much the API. I'd like to see plus errors, if… if there were errors.
Yeah, but overall, it's great. I created an issue to track changes. I think Schemav2 comes at the first priority to me right now, but once I have more time, I will probably explore the proposal I made.
Yeah, Josh?
Josh Suereth 00:17:40 Yeah, this is amazing. I'm gonna ask the long-term question first, because it's probably the most annoying.
these, test containers, should we have, like, a place where we have Weaver test container libraries to make it easy for people to just use Weaver in integration tests?
like, is this… is this a Python library we should export, or do you think, like, SDKs should have that in Contrib somewhere that get exported?
Liudmila Molkova 00:18:09 I think there is no good reason for us to have it as the case… should. I'm planning to bring it to Autel Python test tools. It's a tiny file, actually.
And it would be even half smaller if we fixed the reporting.
Josh Suereth 00:18:31 And removed files from it.
Yeah, I'm just thinking, like, I will want to use this on every… like, everywhere I use Weaver, kind of a thing. Like, in Java, it'd be nice if I could use test containers as well, but it's gonna be a different set of code. Like, it's like a… there's a test container wrapper on top of Weaver, right?
And I think that that wrapper will need to be, like, per language.
Liudmila Molkova 00:18:56 it needs to be per language. The reason to have it in Weaver is that somebody who writes native instrumentation could More easily leverage it.
But they could as well import test library from Java.
Josh Suereth 00:19:13 Right. I guess what I'm saying is how… you're saying that it's not that hard to just wrap the Docker container if we get the API right.
Liudmila Molkova 00:19:23 Yeah, it's easy.
So, I mean, there is no strong reason to have it in Weaver, but there is no, like, there is no strong reason not to.
Josh Suereth 00:19:36 I think it's.
Liudmila Molkova 00:19:37 tick.
Josh Suereth 00:19:38 I'm suggesting we have this in Weaver. I also want, like, a set of Weaver test container libraries that people can use, where they don't even have to know about the Docker container at all, it just looks like a live language library.
See, you know what I mean?
Liudmila Molkova 00:19:54 Oh, but then… Yeah, I see what you mean. And we don't even care about Docker, that… We don't need to run it in Docker, actually.
Josh Suereth 00:20:06 Sure, like, if it… yeah. Anyway, I'm probably getting ahead of myself, but I think this is awesome.
And, it, like, this is a… this kind of library, I think, would be really valuable to have, you know, outside of OpenTelemetry as well, I guess is what I'm saying.
And so… the… the Python wrapper you have around test containers, I think, is usable outside of just Yeah, absolutely. Yeah.
Okay.
Cool.
Anyway, I'll let Jeremy jump in to talk about live check, things, because I… the feature totally makes sense to me.
Laurent Querel 00:20:46 Yeah, for me too, I think the… Would be very nice to have the outputs.
the outcome of the life check. I directly returned by the… The, the post and punt?
For the errors, I guess we can have some of them, not necessarily all of them.
Yeah, for this one, I'm not sure, because, I mean, if it's because you have a misconfiguration, I don't think that it's… I will normal to, to expose that with the, the stop, I mean, you are in a development mode, and you are creating this stuff for the live check. It's not working because you misconfigure your weaver.
you don't necessarily expect to have the result into the HTTP endpoint in that case.
But for the… Sorry, for the light shake, I totally agree.
Liudmila Molkova 00:21:48 If it's a misconfiguration, like, for the static part, for the comment line, I agree with you, but let's say I mistyped something here in the rego policy.
The life check should not stop.
And it could actually return the least of… Errors we've seen from the policy. It's just a better user experience, because you, you, you want to know.
Laurent Querel 00:22:16 Yeah, true.
Liudmila Molkova 00:22:17 Not too late.
Laurent Querel 00:22:18 If it's a… if it's a policy… error, because the, the, the rego is, is not, properly, is not valid. Do you… you are not in the same cycle, in terms of, On one side, you are creating a policy.
And you could do that, for example, with, without the container at all.
And on the other side, you… you are part of the CICD integration.
And you want, maybe, to leverage the result of the analysis done by LifeCheck?
In that case, I totally understand why it's written by the stop end.
Liudmila Molkova 00:23:13 Okay, yeah.
Thanks, so I… I think I… Here in general, support for this idea, and we will definitely discuss it more.
Jeremy Blythe 00:23:24 Yeah.
I think it makes… Perfect sense.
Obviously, it will only work in report mode, not when you're streaming the data out.
like LifeJack can do.
Liudmila Molkova 00:23:34 Oh, yeah.
Jeremy Blythe 00:23:35 Yeah, so we just need to make that clear, I guess, in the docs or whatever, but… If you want a result returned on stop.
If you're in streaming mode, I think you could get the statistics.
Liudmila Molkova 00:23:49 If you're in streaming mode, you would actually also appreciate if we ever didn't stop on the policy failure and would report the policy failure as a log to your backend.
Jeremy Blythe 00:24:05 Yeah.
I think it would be interesting to set up something that exposes one of those failures, so that we could see Where it is in the… In the life cycle.
If you get a particular type of error.
Why it's not… why it's only found… at that point of runtime. I think that would be interesting to have something that exposes that.
Liudmila Molkova 00:24:29 Oh yeah, sure. It's just because if it's… if it's not… if a specific telemetry item.
Would not have something, and we expected it to be there.
Done.
It would fail.
Jeremy Blythe 00:24:42 Yep, feels like something to do, like a… Test driven.
Maybe.
Anyway, yeah, no, I think returning that stop makes great sense.
Liudmila Molkova 00:24:54 Thanks.
So, I think next topic… There's also mine, hope you don't mind me… So, I want to talk about Schema V2, and we had some great discussions over the break.
On Slack. Thank you all. I wanted to focus on one specific thing today.
So, I've tried to document resolved, materialized. Source.
canonical, whatever schemas we have, and I have some, questions, probably, and topics to discuss.
so, I've brought this overview for Russell, and… not married to terminology, just want to suggest something, and I think, Lauren, you expressed interest in other terminology. But anyway, there is 3 distinct types we want to talk about. The source schema is what you write some conf in, it's pretty straightforward, and there is Whatever we call resolved, that's the optimal version of it.
And then there is the materialized result. This is the… what we… the forged one.
What we give the templates.
if you have ideas about terminology, bring them on. The thing I wanna discuss is why the resolved and forge… R… So different.
do I have… I had to write up somewhere.
I have a comment on this, Pierre.
Yeah.
So if you look here, so this is how result looks like.
We have attribute catalog at the top, then there is registry, attributes, attribute groups, paths, metrics, event entities, refinements.
And this is materialized.
This is, like… The registry plus refinements.
The refinements are the same. This internal things are pretty much the same.
Can we make them closer?
Josh Suereth 00:27:29 Yeah, you can blame me for this, I was just lazy. So… Yeah, when, I was focused on forge schema.
And so forge schema was the way I wanted it to look.
And then I never went back and fixed up resolve schema.
After we kinda ironed out what Ford's schema was. So… This also gets into understanding what attribute groups are, but the difference here is that the attributes list in Forge is the attribute… it's not the catalog, it's the attribute registry.
Attribute groups is also the registry of public attribute groups, and then signals is meant to be, like, the registry of signals, and refinements is all the signals, right?
So, I think we could… we could go one of two ways. Basically, we could go back to the way The resolved thing is, and Forge just doesn't have the catalog. So… The forge schema would be the same as the Resolve schema with no catalog, so it's registry and then all the things, refinements and all the things. Or we could, like, if we think calling out signals.metrics makes sense for people, cool, we can… we can have that. I, I'm fine going either way, that was, like, you can… it… there wasn't… this was one of those things I just did without a lot of thought behind it, so it's not, like, an intention thing that it's different and broken, so apologies.
Liudmila Molkova 00:28:58 Oh, thanks, and no worries. So, I… I… I don't have a prefre- like, I probably have a preference that the… this seems cleaner, like, registry and refinements versus signals and refinements, but…
Josh Suereth 00:29:18 Yeah, okay. I mean, that's… that's an easy change to make. It will be slightly breaking, but, like, We're still in our, like, preview phase, yeah. So, if you open a ticket, I can fix the forge schema. So basically, we'll make forge schema be the same as Resolved, the only difference will be the forge schema will not have the attribute catalog, because it doesn't make sense, yeah.
Liudmila Molkova 00:29:45 Okay, I'll just drop it here so I don't forget… Quote.
The other thing I'm suggesting to do, which is a trivial one, that… We align the three fields everywhere.
the file format schema URL and registry URL. They will appear in both registry and Forge.
Josh Suereth 00:30:26 Do we… do we need more than that?
Liudmila Molkova 00:30:30 Why?
Josh Suereth 00:30:31 Oh, I see, file format's gonna say that it's resolved. Gotcha.
Liudmila Molkova 00:30:37 Oh, it's going to say it's resolved! Oh, cool.
Josh Suereth 00:30:40 Yeah, yeah, okay, okay. Yeah, like, what… we… what I want is a way to know if you're looking at Resolve Schema or Forge schema, like, from the manifest. So yeah, we should make the file format actually say.
This is resolved, or this is not, so that we can, We know that.
Liudmila Molkova 00:31:11 Cool, cool, cool. Yeah.
I… don't really want to go deep into the schema V2. We had some discussions, good discussions in Some conf call and spec call.
One thing I probably… there is an add-up, it's in draft. The one thing I probably need help with is, I have a section about Importing and decentralization, the multi-registry stuff.
Could someone help me write this section? Have… have an example that's representative of this feature.
Or do we have it, and can I just steal it?
Josh Suereth 00:32:04 We do… we do have some examples with, imports. Lauren, I don't know if you have time to do this yet.
Laurent Querel 00:32:12 If not, I was… I was gonna work on the import code to support importing resolve schema.
Josh Suereth 00:32:18 In addition to importing unresolved schema, So, I'm happy to take a crack at it, but it might take me a little while.
Laurent Querel 00:32:29 I can tell you.
Josh Suereth 00:32:32 Alright, if you're not able to get to it by, say, Monday, ping me and I'll take a crack.
Laurent Querel 00:32:39 Okay.
Liudmila Molkova 00:32:50 Awesome.
Thanks, so then I'll, stop sharing and let Jeremy talk about… MCP server? Wow.
Jeremy Blythe 00:33:07 Yeah, okay.
Let me see if I can share properly here.
Here we go.
Okay, you should be able to see some… VS Code.
Yeah, so I, Had a bit of time over the holidays, and thought I'd have fun making an MCP server.
turns out… It's not that challenging to do, because it was just building on top of the… the search stuff and the API stuff that I did for the user interface. So there's things like… You want to be able to run a search, you want to get an attribute, get… get, you know.
Get any of the signals.
So, yeah, essentially I've done that.
I just, while we were talking, I loaded it up in. So this is a co-pilot in agent mode. You can ask it questions. I put some questions in here. Let's say… Which one do we like?
Let's just grab… get the details for the blah blah blah.
So, it's calling getAttributeTool.
You have to be quite careful with your tool description. I don't know if people have written MCP servers before, but you have to be kind of… really explicit in your tool descriptions so that the LLM Picks the right tool to do the right thing, and fills it out.
And it's just gonna go get that attribute, and… Give you some stuff back.
Which is cool.
I also added… Life check?
So what you can do with the live check is… it can create a sample… let's see if I can do it, D.
Can you make a sample of this?
Contribute… What was this I asked it for?
An attribute, yeah. Some of these aren't sure if you… with, we need, parent life.
Let me check it. Let's see if… see if it does.
So what it should do is build a sample. Yeah, there you go. So it's built this sample up with a GET.
And then it's gonna call the live check tool.
That will get back the results for that.
Pull that.
Live check?
So, with the violations and so on?
And then… Tell me all about it.
So yeah, so that's what… that's what I made. It's fun.
One…
Laurent Querel 00:36:13 boom.
Jeremy Blythe 00:36:14 I think that's really cool, let me stop sharing this one, I'll share a different one.
So let me share…
Laurent Querel 00:36:20 We were talking about, tools to help, developer to create new policies and so on, I think that that could be the interface also to To help people to, to test, Basically, to express a policy in a natural language.
And to get, this agent… to create the policy in REGO, to test it, and get the result.
Jeremy Blythe 00:36:55 Yeah, okay, so this one, what's interesting about this one, so this is in Claude Code.
The nice thing about… call it, I think you can do it in most things, but you can have different MCPs for each project that you're in inside of VS Code, or which directory you're in when you launched Claude.
So what that means is this… I think this tells a really nice story, because this is some real production code from my company to do with a thing called market switching, which was what I would have talked about.
If I was… had been able to get to KubeCon.
But anyway… So in here, I've… I've… I'm running the MCP server, but with the registry, with the model that's associated with this project.
Plus the custom policies that I've got for live check.
So then when I'm running… when it runs Weaver queries, it's querying against the model which is part of this project, which is in here somewhere.
Bunch of attributes and expans and stuff.
Yeah, so it's… so it's doing, you know, this tells the story of it, like, linking up with… Your custom registries.
And… Because it's… because this is all, MCP and LLM. I've also… we use… my company, we use Honeycomb as our backend. Honeycomb have an MCP.
So I'm able to say, like, hey, with this code open, go to my observability backend, go get the dataset, bring back the production stuff, compare it with what Weaver says about this, get a sample from production.
with the code in context. With Weaver, they're giving you information about it, suggesting ways to improve your code. It's kind of cool.
So, I had this whole conversation with it about how it's telling me things to fix.
it's… the PR's open, I want to fix the schemas thing first, because it said there's a little bit of an ugly hack in there to get around.
that problem, so I'd rather… now that I know how to fix that, we can fix that, and then I think that, again, this is like, Feels like a sort of foundational thing that we can build on, again.
Like, with the API. But, yeah.
It's from the room.
Laurent Querel 00:39:28 as you're…
Jeremy Blythe 00:39:28 over.
Laurent Querel 00:39:31 Can you provide the… the URL of, a compressed… so a compressed, semantic convention registry, and, and, and inform the… the MCP command of Weaver that you need to use this one instead of… The last one, for example.
Jeremy Blythe 00:39:57 Oh, on the fly, tell the MCP.
Laurent Querel 00:39:59 Yes.
Jeremy Blythe 00:39:59 It's a different registry.
No.
No, you'd have to…
Laurent Querel 00:40:03 But, is there any, problem with this approach?
Jeremy Blythe 00:40:09 No, and we want to do that kind of hot swapping the registry. We want to do that for the API as well. So I think we can solve those two things in parallel.
Laurent Querel 00:40:18 Yeah, okay.
That's super cool.
Josh Suereth 00:40:22 So… This is amazing, but my one concern, Jeremy, is the same concern from the WeaverServe, which is, I think we have to sort out our Weaver config and template story for these things.
Right now, like, when you run live check, or when you run serve.
in that MCP server, right? You're doing kind of the same hook to kind of get your config, get your templates, that sort of thing. There's… there's an interesting problem we have where, like, the Weaver policies and custom rego.
actually gets pulled in from the directory where you resolve The, the registry from?
And, like, the way that that loading works, the way that we find these files, the way we find JQ templates, the way we find, Jinja templates, the way we find Rego policies.
I think we need to actually kind of shore up and be consistent between these different ways of starting Weaver. And, like, because effectively, your startup code and the, like, standard Weaver startup code are different. And to the extent we can make it consistent so that it's not confusing.
where data comes from, how it comes in, when I get to use Weaver Config, when I don't get to use Weaver Config, like.
we need to get that shored up. And so, like, when it was just WeaverServe, it was like, cool, we can fix this later. Now that it's also MCP and WeaverServe, and they have different startup mechanisms, and they have different code paths to start up.
And that is different in all three, of, like, all the Weaver CLI stuff, all the WeaverServe stuff, and all the Weaver MCP. I think we need to fix that. Now, do we need to fix that immediately? No, but that needs to be, like, our immediate roadmap. Like, I would be happy adding MCP so people can try it out, and then fixing this over time.
But I do think that we urgently need to kind of get that sorted and have a story, you know?
If users don't know where their Rego policies need to live, if they don't know where their Jinja templates need to live, I think we have a big problem.
Jeremy Blythe 00:42:37 So, honestly, it's… oh, sorry, go ahead, Jim.
Didn't have anything.
Liudmila Molkova 00:42:43 It's awesome, I, I have a, somewhat, weird, question. So, there is a proposal for the MCP… server, seek for OpenTelemetry, I'm not sure if you have seen it. I'm pasting it in the chat.
And folks are interested in first building the collector-related MCP features, and I think they would appreciate from your… they would benefit from your feedback, about doing things in Weaver directly.
And if you believe there is a need for the Central LabCP team, or if you'd express how it works in Weaver with your proposal, I think it would be helpful.
on that request that proposes the SIG.
Jeremy Blythe 00:43:40 Right, yep.
Liudmila Molkova 00:43:43 Things.
Awesome.
Jeremy Blythe 00:43:52 Okay.
Josh Suereth 00:43:57 Yeah, looking at that proposal quickly, the… one of the very first things they call out is they want to build the ability to do Weaver schema generation and context-optimized query of official SEMCOM registry, which you already have now, Jeremy. So, like… I would at least make them aware of this demo and prototype.
Jeremy Blythe 00:44:18 Okay.
Liudmila Molkova 00:44:22 I'm actually curious what you thought.
I think I expressed it on the proposal. I think it does not make sense to create an MCP server for the whole open telemetry, and it's great to focus on individual pieces, and the river would expose MCP server. Do we need a group of people who who would optimize MCP servers across open telemetry? Do we want to expose a central open telemetry one?
Jeremy Blythe 00:44:55 Yeah, I guess I'll have to read what… They're trying to achieve more… something more broader than what I put together, I guess.
Josh Suereth 00:45:07 to me, I think the important bit would be, if we have… so, so, I hear… I agree with what you're saying, Lyudmila. I think if a central team existed, it should put the MCP servers together and make sure they work together. So if I'm running a collector MCP server.
and I'm running a Weaver MCP server, and I ask to do things, they should work together well.
And someone needs to figure out that friction and report bugs between the two, and I think it's fine to have people that look at the two together.
But I also agree that, like, in my experience with agents, if you try to do one big thing.
not necessarily the best idea. Stick to small, focused tasks, and then scale from there, and do, like, keep doing smaller things and making them bigger. So, I would prefer to have, I would prefer to focus our MCP efforts on, like, individual components, because I also think it's not necessary you use a collector at all.
And I think Weaver, specifically Weaver, we have people from Prometheus here who are looking at using Weaver for Prometheus. Our MCP server could be useful to them independently of the OpenTelemetry Collector. So, I feel like we should… We shouldn't try to tie all our eggs in one basket, you know?
Cool. Anything else about MCP? Because that was pretty awesome.
Jeremy Blythe 00:46:41 No, I feel like I should have read that thing before.
I hope I'm not gonna annoy people, but anyway.
Josh Suereth 00:46:48 No, no, no, no, dude, That is a proposal. Without an implementation, you have an implementation that is becoming a proposal. I would rather start with the latter, right?
Alright, I'm gonna, I'm gonna… jump back into sharing, if that's okay. This is semi-related, but not quite. You might remember before the holidays, I created the Docs agent markdown description for, like, a Weaver Docs agent that we can use to go ask it to help us write Docs.
We made a bunch of V2 changes and were unable to write docs. Ludmilla wrote some docs, and I created two PRs where I tried to get the agent to fill in the docs for me using, like, unit tests and things that have been written.
in the code, and so I just wanted to show these off and see what we think. The first one, I think, is better than the second one, because the prompt is better. So I'm going to show off the first one.
But this was basically… you can see… I think it shows my prompt to… co-pilot.
Maybe not, but anyway, the, I basically prompted it to say, hey, this PR added policy finding to, like, replace violation advice and mix them together. Can you go update the docs wherever they need to be for it? And I think I gave it a specific markdown file.
to take a look at. So, it went in, and it updated Validate Markdown.
And what it did was it added this policy finding structure.
Documented the fields that you can put in policy finding.
it describes what the finding levels are, which, again, it pulled from code, and then it shows a custom rego policy, which it pulled most of this from our unit test, and then modified some of the sections.
Which I think is quite nice. So, oh, and then it talks about how to export policy findings and, like, what the JSON format does.
And how to use it.
Right, and then it talks about backwards compatibility in case you want to use the legacy formats. So this was previously not documented. I think this looks pretty good, but I wanted to first check with folks on, how they think about this. The main… the only thing this did not do is, and I'll show this here, we talk about, please see Weaver Checker for details.
About custom rules?
This starts adding more documentation right into the validate section of our docs, as opposed to deferring everything into the crate, which I am fine with.
But that is something that, like, I don't think the agent's the best at. I don't think it knows about our dock structure. I think we will have to maintain our dock structure and point it at a particular dock and say, go improve this piece of the dock for this aspect.
Liudmila Molkova 00:49:49 And we can highlight about our doc structure in this, AgentsMD, or the Copilot Instructions MD?
Josh Suereth 00:49:58 Yep, yep, we can update that as well. In fact, if you want to see the current definition of what this is, I'll just remind everybody.
under GitHub, Agents, Docs Agent.
This is our expert technical writer. It has… it talks about the role, the project knowledge, and what it needs to do, and then a process. Basically, it prepares a branch, and it creates a docs plan of what it's going to improve.
And then it will actually go through, and it's supposed to make one PR per fix. Ironically, when I run this with Gemini, it does it. When I run it with Claude, it does not follow this process. I don't know why.
Both of them produce pretty good docs so far, from what I've seen. It's just, for some reason, they're different. Alright, and then… How do I get to this? Let me… let me do this in another tab, and I'll bring you over.
I just want to show how you use this. So in, if you have access to GitHub.
yourself, and you… GitHub Copilot.
you keep, like, oh, CNCF is not paying for us to run things, but if you go into agents.
You can select OpenTelemetry Weaver.
And then you select the docs agent.
and then you give it a task and say, hey, go write docs for this PR, go write docs for this thing, and it will do its… it will do its job from there. But that's how you actually execute this if you want to kick something off.
If you want to see, here's the, the two PRs that I have open. You can see the session, you can see the docs where I said, hey, can you improve the docs? This is what led to that policy finding structure, and I think if I scroll up, you can see its original task queue.
Where was that? Let me do… it's, to-do, I think?
No, let's do that mark down.
That's all the stuff it read.
Anyway, oh, here it is, the documenta… so this is that documentation plan that we said, so you can see what it was trying to do.
And you can actually validate things and issue fixes and stuff. It's pretty powerful, but I wanted to first make sure everybody knows how to use it, how to invoke it if you're interested. If you need to make changes to it or want to fix anything we're not happy with.
We can, go update that shared description of the agent.
One of my goals here is, if we start using agents for work, that we actually share our prompts, and we improve it together.
So, the idea would be we can make those suggestions and comment across each other, and then all benefit. Okay.
So… Things I wanted out of this meeting. Number one.
how do we… how do we feel about that doc, that… that we… that I showed? Do we think that that's ready to pull out of, by default, they're in, draft?
Do we think this is ready for review? And would we be comfortable accepting reviews from this docs… er, accepting PRs from this docs agent today?
With what it's producing.
Liudmila Molkova 00:53:23 Did you like what it produced?
Josh Suereth 00:53:26 I liked what it produced, but I want to check with everyone else, because I don't want to… I'm… yeah, I'm a bit biased.
Laurent Querel 00:53:33 I'm sitting on my side.
Josh Suereth 00:53:36 Yeah.
Okay, this one, I'm gonna show off because this was a bad prompt. This was basically, hey, I told it… We added a bunch of V2 PRs. Go find everything related to V2 and make an update for V2.
And this one, I don't think was quite as good. I think it's decent, but it's not quite as good. Effectively.
it just added a few things about, hey, V2 exists, V2 is, You know, what it affects, and it is currently in alpha status.
it added a description of how to use the V2 syntax for definition, but it said that you have to use the V2 flag for it, which is actually untrue.
Maybe it should be true, but it's not, and you know, so this one, this one went a little bit off the rails. It's actually not bad, it just did some hallucinations of things that aren't true. Specifically around, you know, version 2 of it.
The documentation around examples of version 2, I think, is totally fine, but some of the specific things it says are wrong, and I can go prompt it to fix it. But this one, I'm not going to take out a draft, because I think this needs to get reworked.
And honestly, I think it just needs a better prompt to begin with, like, of what to change, what file, that sort of thing. So I did want to show you a bad example.
Go ahead, Lauren.
Laurent Querel 00:55:02 Yeah, so, is it possible to provide directly to the peer comments Basically doing the review, and then let the agent.
Josh Suereth 00:55:13 Yes.
Laurent Querel 00:55:14 accordingly. So in that case, everything that you mentioned could be just… Guided by those reviews.
Josh Suereth 00:55:22 Yes, The… the only caveat I'll say is the… currently, because of the way you're invoking this, it is using your own quota.
So if you send a PR, and someone makes a bunch of comments to the agent, I think you have to, like, I have to be the one to tell it to do things, or you have to tag it as the agent, and then it uses my quota.
To perform that action.
So I just want to caveat that, like, if we send these things and people start making lots of comments, your personal GitHub co-pilot quota will get used.
Laurent Querel 00:55:59 Yeah. But, but you all… But you are in control, if I understand well.
You, as the owner of this co-pilot account.
We'll authorize the agent to react to the…
Josh Suereth 00:56:13 I think so, but if you could, would one of you be willing to make a comment on this PR for an improvement, and let's see if the agent does it independently?
Laurent Querel 00:56:22 Okay.
Yeah. Yeah, we can play that.
Josh Suereth 00:56:25 I'll tell you from there.
Laurent Querel 00:56:26 Yeah. Yeah.
Yeah, that's, incredible.
Liudmila Molkova 00:56:33 And then you can, you can assign… issues to Copilot and also specify the agent. Today, I learned things, Josh.
Josh Suereth 00:56:42 Yes, yes.
Liudmila Molkova 00:56:42 Preach your assignment directly.
Josh Suereth 00:56:45 Yeah, so the other way to do this, let's say, this was a documentation-related thing, we can assign Copilot here.
And to say what agent. I think if I click this, it doesn't go straight in, right?
Liudmila Molkova 00:56:57 Yeah, it will ask, it will ask about the,
Josh Suereth 00:57:00 agent. Yeah, like, I can cancel if I do it, right?
Laurent Querel 00:57:03 Mmm, we can.
Josh Suereth 00:57:05 Yeah, but if you click here, it'll ask which agent to use, and so we can make an issue that describes a documentation task and assign it to our docs agent to do, as well.
Laurent Querel 00:57:13 Which is even a better workflow, right? Because we have a tracking directly in GitHub.
Josh Suereth 00:57:19 Yeah, and before vacation, I literally went through and added a ton of labels to our project. So, for now, we actually have, like, a template engine label, for example, where it talks about Anything related to the template engine is under Template Engine. Anything related to you know, other things is there. If we end up with documentation tasks, what we can try is, grab documentation tasks for, like, a particular area.
Or just grab all the documentation tasks.
And give it to this thing and see… See what happens, you know?
I don't know, like, this one, enhanced discoverability.
I don't know if this has enough detail. Like, the agent works much better with well-defined, well-scoped tasks, so we might need to take some of these and make them more… specific?
But, that's another way that you can assign it to the agent and get the agent to do it. Just remember that when you do so, it will… like, right now, because of the way Copilot is set up in CNCF and OpenTelemetry, you have to use your quota to run the agent.
So the agent has shared the description for all of us, but we have to use our own quota.
Liudmila Molkova 00:58:42 And I think there are some discussions, GC is trying to get us quota for maintainers, at least, from CNCF.
Josh Suereth 00:58:51 Yeah, yeah. Anyway, cool, I'm gonna mark that one PR for review. One thing I will say, is, and this, I don't think we're gonna have time to talk about, the… we have an issue where somehow we're not specifying an NPM version. We're specifying a node version, but not NPM. And… If you use NPM version 10, your package diff looks like this. If you use NPM version 11, your package diff looks like what is currently checked into Weaver. And I don't know how to make it consistently always be 11 across all of the things we do.
I don't know why the Docs agent is on 10, I don't know why my computer was on 10 after I upgraded Node, but it is. I know that Jeremy's is on 11, and I know that, Dependabot is using 11.
when it does its dependable on things. So, I have no idea why this is a problem, but that is something I'd like to fix, because I don't want package JSON to just keep churning anytime someone with a different version of NPM tries to run R.
are billed.
Cool. I think that's it for today, right?
Liudmila Molkova 01:00:12 Yep, and we are over.
Josh Suereth 01:00:14 Alright, thanks everybody. Super exciting news. Looking forward to next week.
ariannavespri 01:00:20 Thank you. Thank you, bye, bye.
