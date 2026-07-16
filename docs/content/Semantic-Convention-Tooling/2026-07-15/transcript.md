SIG: Semantic Convention Tooling
Date: 2026-07-15
Duration: 55 minutes
============================================================

## Zoom Recording Transcript

**Josh Suereth** 03:08 Hey!
I'm a little slow today. How are we all doing?
**Jeremy Blythe** 03:17 Good.
I gotta drop it. Half past.
**Josh Suereth** 03:25 Okay.
I've been a bit swamped with, work-related things, so I really actually haven't had a chance to do much, even code review of Weaver lately, so that's unfortunate. That, and I was trying to get entities kind of finished.
Yeah.
So, did you have anything you wanted to talk about?
**Jeremy Blythe** 03:48 I've been doing some UI stuff.
Which is fine, actually. I never used to like UI coding, but now that the coding's done for you, I kind of like it again.
**Josh Suereth** 04:04 You just get to yell at someone to write the UI for you, yeah.
**Jeremy Blythe** 04:07 Yeah, you know, I've…
**Josh Suereth** 04:09 Yes.
**Jeremy Blythe** 04:09 I want that button a different… I want that button over there, and yeah.
And.
So I've got in, there's a PRN to add a tree view.
for search.
Which is a thing I had.
way back, which got me into Weaver right from the beginning, was I had my own tool that was… had a, like, it's like a… it's a tree view of your model, and you can kind of explore through it. So there's a PR up for that.
And then I haven't got it, I haven't submitted it yet, but I've also got a, another UI where you can… And this leads back to what we were talking about, where LiveCheck is going to respond to the schema URLs as they come in.
But what I've done for now is you can… If you've done a live check and you've got a report.
You can give the report.
Back to Weaver.
And and then it will make an explorer of your report. So you can go through and see all of the things that a live check is found, and it turns the things like, oh, you… you know, this is incorrect for this metric, and that's a… that metric becomes a URL that you can then click on, and then you can see the information about that metric in… in the whole, sort of, UI. So, that's coming soon.
But I did that, tree view thing.
First.
That's what I've been playing.
**Josh Suereth** 05:43 Right. Nimrod, it sounds like you have an issue here.
**nimrodavni** 05:48 Yeah. Hi, everyone. Just wanna give a… just wanna point out, where I'm coming… I'm coming from the OBSIG, and we've been using Weaver lately to, validate, basically, our telemetry, creating telemetry schema, so I also wanted to say that, like.
I'm very… it's, like, a really cool tool, and I think it helped us kinda, discover a lot of gaps we had with, the way that we produce telemetry and declaring our own and following OTEL.
I just want to give her like a quick, like what we do. We basically inherit from the hotel, like the normal semantic conventions and override them with some stuff of our own. For example, like common example, like for example, DNS metrics.
That's the one I encountered as bug DNS metrics. You want to make one of the labels, instead of required, making it opt-in because of cardinality issues, mainly. So we kind of wanted to make an override of our own.
and what I encountered is basically that if you do if you have like the same basically same attribute or same metric name same I guess any type of signal or something like that it will resolve them in alphabetic group ID order so you basically need to add some suffix, or, or, like, make a, like, an X dot something to make sure it resolves latest.
I could, like, submit something to fix it, but I just want to know what is the exact, like… What do we expect to be the hierarchy, then?
**Josh Suereth** 07:33 Yeah, I think we're… we're going to be deprecating this syntax pretty soon, and we're moving to the V2 syntax, where you define things as metrics with overrides and all that. So in, like, the… in the new… models, like in V2, you actually can't have multiple groups that are the same metric name.
With different IDs, unless one is a refinement.
And you can only refine from the source, you can't, like, refine a refinement right now.
So that's like… so I don't know exactly how your refinement is working. You're saying, like, I extend this, and I'm doing this, right?
I need to look at the details here, but my guess is what's happening is you're trying to refine a refinement.
Versus refining the core or something like that, what.
I… if you have a reproduction here, I'll take a look, but we, My expectation would be that this should not be an issue.
In the long run because.
We'll have a… like, the namespace won't allow that kind of, like.
override in that sense. Like, everything will be explicit.
Because I think when you're referencing something to extend, and it's a metric, and it's looking up by ID That's part one. The other thing I'm curious about is… Has no reliability to override a group in inheritance.
Relax attributes when the dependency's copy of the group enters the resolved registry.
Which happens under this, right?
So you want to… you want to actually import something and then refine it.
**nimrodavni** 09:18 Yeah, mainly from the OTEL. I put a link in the Zoom. It's basically our schema is basically we inherit OTEL and we just do either custom new signals or override existing signals, attributes, definitions.
Just to refine them, exactly as you, as you said.
**Josh Suereth** 09:42 Yeah So let me see if I, it might be. Might be easy to see in our docs If you look at V2 syntax, what what we recommend in the new syntax makes it more clear what's going on. You like. The we, I might change yours from bug to like won't fix by the way but let's talk through whether or not this solves your problem.
we don't want those definitions to change. We want them to remain as is, so that we know that, like, you're compatible with it. So, like… but you can refine it. In a refinement, Where's our syntax? Is that under specs? No.
**Liudmila Molkova** 10:21 Chand.
**Josh Suereth** 10:21 Schemas. It's under schemas, okay.
I always go to Docs first. Okay, so… In V2, we have this notion of a refinement.
which I think… should be somewhere here. Let's talk… let's look at, like, metrics.
Okay.
Yeah, do we not have… oh, here's a metric refinement definition. So in a refinement, basically, you give yourself a new ID, which is the thing you're going to use, like the group ID that you want to leverage.
In your, schema, you refer to the metric that you are refining, and then the things that you provide kind of override.
the upstream one, but we make sure when we have refinements that they're compatible. So, there's a set of rules around refinements to make sure that you're not doing something where you would no longer abide by semantic conventions.
If you change things, like stability or, the requirement attribute, requirement level. You can do that for, like, attributes underneath it, with attribute references, but if you do that, you can't actually make something Less.
Restrictive than it was.
Like, that's actually… would be considered, like, breaking.
So, if something was optional.
you can make it required for you, but if something is required, you can't make it optional. That's considered a breaking thing, right? Because it's literally required for the semantic invention. So you… if you were to actually run your code through a validator, like LiveCheck, you would fail the semantic convention in that case.
**nimrodavni** 12:09 Yes.
So you're saying, like, this is, for example, one of the scenarios that we have, so I'm just wondering if the question is, like, should we… say, like, we're redefining the whole metric and not relying on the cement, because we want to make, yeah, DNS question name, we want to make it opt-in instead of required, because we… we don't want… because… because if we make it required, then if we don't send it, which is some cases in OB, the validation fails. So we want to make sure that we say we're not, like, requiring this to be sent, it's an opt-in that you can configure in OB.
**Liudmila Molkova** 12:50 It sounds like you just need to follow V2 syntax and do a refinement, and it should work.
**nimrodavni** 12:56 But you're saying that I can't refine it to make it, from, required to opt-in?
**Josh Suereth** 13:02 Yeah, that… that… what that means is you're not following SEMCOM, right? Because if in SEMCOM the requirement level's.
**nimrodavni** 13:09 Yeah, I'm not, like, standing it. Yeah.
**Liudmila Molkova** 13:12 Well, I think it's a good idea to enforce it, but I don't believe it's enforced today.
**Josh Suereth** 13:17 Oh, right, it's only enforced in our… In our policies, isn't it?
**Liudmila Molkova** 13:23 I don't even think it's enforced in the policies. We don't have any policies for refinements.
But it brings us to a separate question of should we not require it in the, semantic convention that should at least be recommended or conditionally required?
And this would solve a problem too, but it's.
Then it would allow to relax it, even if I introduce these policies.
**Josh Suereth** 13:58 Yes.
I think this should be something that we take to SEMCONF and ask if this should be Actually opt-in, because we're not able to do it in OB as a required thing. I think that's reasonable. The other option, I'm curious about this, Ludmilla, is this metric itself opt-in?
**Liudmila Molkova** 14:20 This metric is currently, I don't think it's obtained, I think it's recommended, but it's defined. Recommended.
Let me see… but it's defined for in… Okay, this is another trick, in .NET doc.
But YAML is not… Does not understand these boundaries.
And.
For… when we defined it, the… Oh, DNS metrics. No, not not. Oh, metric is opt in. Yes.
**Josh Suereth** 14:56 Okay, so if the metric itself is opt-in.
I think you could… you could basically make it… I mean, are you saying that an OB… in Obi, is the metric itself opt-in as well? Like, they opt-in to making the metric, and then you want a second opt-in for whether or not this question is filled out.
**nimrodavni** 15:15 Basically, yeah.
**Josh Suereth** 15:16 So you have two things, okay. Since this is still development upstream.
I think it's not too late for us to decide to make this… to switch this.
**Liudmila Molkova** 15:26 Okay.
**Josh Suereth** 15:27 So, I think what I would do is actually open an issue against raw SEMCOM to say, hey, this requirement level doesn't match OB's needs, and fix it there.
Because, like, conceptually, one of our goals with, like, how we do refinements and things is to avoid, you breaking expectations of SEMCOM. So if someone thinks it's required, they might hard code their dashboards and things to use that attribute, and then you don't provide it, suddenly the dashboard's broken.
That's why we don't want to allow that, necessarily.
Okay.
**nimrodavni** 15:59 Makes sense.
**Josh Suereth** 15:59 Okay.
**nimrodavni** 16:00 Specifically for this, I'll open a Semcov issue.
Regarding, like, this, you're saying the V2… is it already, like, supported by Weaver currently? Can I… Yeah. If I, like, redefine my telemetry schema in a V2 format, I can… For example, I have… like, an attribute, enum that I'm extending with additional values of, like, you know, a DB system name. I've added… we've added a couple of DB system names that are not part of the SEMCOG.
Will that just… is this just, like, an enhancement, and that should work fine, because I'm not changing any requirement level?
**Josh Suereth** 16:42 That's 100% why we have refinements and one of the, like, one of our expectations in that, right? Yeah. Go ahead, Luca.
**Liudmila Molkova** 16:49 For the requirement level with V2 syntax, you should totally be able to do what you want.
If not, I would be very surprised, and we will fix it.
I.
But for enums, it's tricky. So you cannot add a couple of new enum members when refining.
This is a long-standing issue we have, and, it is not possible today.
**nimrodavni** 17:20 It's not possible, but if I… if I re-declare everything and add my… my enum, is that also…
**Liudmila Molkova** 17:27 But no, maybe, let me show you. So before… First, if you want to try out syntax with you, I have a skill and pasting a link.
That might help.
But it should be trivial anyway, But let me find the link of this metric refinement.
Give me a second.
I'll be here in Asheville.
**nimrodavni** 18:16 Maybe another question, just another scenario, which I don't know if it makes sense if I can… Extend something from being an enum to being a string, or, like, a non-numerated value, for example, and.
**Josh Suereth** 18:33 So here's a thing for you to know that I think is a common misconception.
Enums are strings.
In OpenTelemetry, they're open, meaning you can add any value you want to it. The reason that we have enums is that there's a set of known values, but all of the dashboards that leverage one of them need to be able to support open extension of that enum over time.
So that like adding a new value doesn't break it. So if you're just you have things that don't fit in the enum, you should be able to just define a constant and like throw it out there. As and you're still within some kind of right. If there's things you need to push upstream into the enum like open PRS and that sort of thing. But you.
You shouldn't, like, from a practical standpoint, on, at runtime, there is no such thing as an enum, it's always a string.
But also, because of the way we do, like, versioning and, like, stability, enums are open, so you can… you can throw a new value in there that's not on the enum, and that's fine, with the caveat, if it's a metric.
Worry about cardinality.
**nimrodavni** 19:41 Yeah, because I wanted to, basically, I have Weaver, like… Weaver, like, basically, throws these, advisories of, like, this value is not in the enum, set. I think it's, like, a recommendation or something, but I wanted to make it basically fail our, CI in order to, let's say, that we follow, like, for example, we found that, for example, we threw, status codes or HTTP methods that are not part of the HTTP methods, and if that happens, I want to be, kind of, I want to inform about that.
But there are scenarios where we explicitly say, okay, if this is an enum, but we don't have a closed set of values for it, should I either declare it a string in my schema, or should I say specifically for this metric, ignore this rule of… of enums, and if it's the latter, can I do it only with Weaver rules or something, or should I do it in my Weaver validator code?
**Liudmila Molkova** 20:51 You can Jeremy might say more, but you can suppress specific checks in two ways. The first way is through the tunnel config, and I think it gives you, like, the the context on this metric, ignore this violation rate.
The other thing we do in more granular.
I can show you an example in GenAI instrumentations.
We instead of, like, just relying on Weaver to do exit code, we get the report back, and we do granular checks. Let's say this span was supposed to have that value on the attribute.
And then we rebuild violations, and we have, like, the granular violation story saying, okay, on this span, it's okay, because, well, it's… someday we'll fix it, but not today.
**nimrodavni** 21:47 So I think I did the latter, I had… I have some… basically post weaver like thing that reads the weaver output parses it and then like if this specific thing happens then ignore it and like you know don't fail so I can do that, but then the only thing I'm thinking about, it makes the schema less descriptive, because we still keep it an enum, but maybe if you're saying that enums are supposed, like, you're supposed that enums should be, like, free strings.
Then that's… maybe that's fine.
Because for other enums, we're kind of forcing it, and for some enums, we're saying it's still an enum, but we don't force the… those values.
So, I don't know if that should be communicated to the consumers of these schemas.
In some way.
**Jeremy Blythe** 22:45 Oh.
the oh, Josh, you just put a link. Yeah, the the, in the toml file.
You can specify exclusions, like, really quite specifically, so you can say this signal with this name, should have… this type of finding excluded. So you can be very precise to say, like, you know.
for my run.
you know, pick this one out.
And don't don't issue any information about it. Right? So you can.
You can do that. If if it doesn't quite fit what you need, then I'd like to know, because we could. We can improve that as well.
**nimrodavni** 23:29 Okay, that's the, the Weaver, YAML file, like, the, the schema itself, with.
**Jeremy Blythe** 23:34 No, no, no. So when you launch… when you launch Weaver, it's got quite a rich command line already, but we wanted to add even more to that, so, like, instead of bloating the command line, you can provide it with a TOML file, or it will look for .weaver.toml.
From your… from your current working directory up.
So I'll find that, and then there's a definition for What you can put in there, so… because you need to be quite… you may need to be quite descriptive about how you want to exclude findings or adjust things, so you can fill it up in that toml file.
**nimrodavni** 24:10 Okay, so I'll have a… I'll have a deeper look at the… both the V2 and… And those exclusions and things, I'll try to see if it all matches what we can do.
If if not, then maybe I'll I'll just.
No, bring it up again with more info.
**Liudmila Molkova** 24:35 Yeah, by the way, there is… you mentioned you parse the… the Weaver output?
**nimrodavni** 24:42 You know.
**Liudmila Molkova** 24:43 There is a better way now. I'm going to share a thing we did in Python, but you can obviously rewrite it to anything you want.
And this is the wrapper around, Viva CLI.
And it, the Weaver, has admin endpoint where you stop it.
**nimrodavni** 25:08 You know.
**Liudmila Molkova** 25:08 I think, it's the, like, you can get the report in over stop command as a response to it.
**Jeremy Blythe** 25:18 Yeah, if you set the output to HTTP, when you call stop.
Over, when you call that stop endpoint, it will return to you the entire report.
**nimrodavni** 25:27 Oh.
**Jeremy Blythe** 25:27 That's the response back from the stop, the stop call.
**nimrodavni** 25:31 That's better. I think I'm just like copying it from the docker. Oh, but that's way better.
I'll try to… change that.
**Liudmila Molkova** 25:43 Yeah. And essentially, we have this wrapper. I just put the link in the doc, and you can.
Call, you essentially say.
stop with end, and it returns the parsed report. And it's even, a type thing, and you can add as much convenience as you want around it, and it helps a little bit. But, yeah, using the HTTP response helps a lot comparing to Docker logs.
**nimrodavni** 26:13 Okay.
**Jeremy Blythe** 26:13 And of course, don't forget, we've just added the GitHub Actions.
for LiveCheck as well, and that has a report, and that allows you to say you want to fail on particular levels and things.
So there's a… there's loads of different ways.
Lots of different ways to crack this egg.
**nimrodavni** 26:35 Cool. I'm just, like, because we have a lot of, like, test suites, and I'm trying to push Weaver into every one of them, So I'll… I'll try… so first of all, thank you for all the info, and then I'll try to, yeah, to handle this specific issue and all the others, and if I have anything else, I'll… Come back and let you know.
So, thank you very much.
**Liudmila Molkova** 27:00 Awesome. Thank you.
**nimrodavni** 27:02 Okay.
**Josh Suereth** 27:06 Always good to hear from users, so… Anytime you have feedback, let us know.
Ludmilla, you have a blank, blank slate here.
**Liudmila Molkova** 27:18 Oh, yeah, sorry, I didn't paste my link there. I'm here again.
You to review my PRs.
Yeah, you must…
**Josh Suereth** 27:29 I said this week I haven't had a time to do any reviews or even update my own PR, so apologies. I, Yeah, it's on my queue.
**Liudmila Molkova** 27:39 Yeah, so then we can just return back to that tool after you take a look.
I'm.
Or if we don't have any other topics, we can just call it, and you'll have some time to review.
**Josh Suereth** 27:52 Yeah, I guess the only thing I wanted to know is, should we… Should we merge? So, you're making changes to attribute catalog here, slightly, or not really?
**Liudmila Molkova** 28:03 Ahhh.
Let me remember.
I don't think so, I… Oh, attribute catalog.
**Josh Suereth** 28:13 Yeah, I'm just nervous about this with the, multi-version… resolution PR that I have. I think that we have version con… like, we have conflicts with touching the same code.
That's… the only thing I'm nervous about with actually all of your PRs, if I remember. So, I had… I haven't had a chance to look at them, but I was gonna try to figure out cross-registry refinements and supporting entities, with the way that I'm doing the external dependency conflict resolution, and that kind of, like, you know.
using a lens to kind of cast something into a different version. I think we have a conflict here, and I don't know if it's better to merge yours first, and then I update mine to leverage them, but because I'm actually changing how those methods are called.
You're touching the same methods that I at least when I first looked at it, but I wanted to, like, verify.
**Liudmila Molkova** 29:07 And… anything stopping us from merging yours?
**Josh Suereth** 29:12 Your comments, actually, I have to fix them, I haven't had a chance to.
**Liudmila Molkova** 29:16 Okay.
**Josh Suereth** 29:17 I literally looked at all of them and I did not have a chance to actually do anything to fix these because you had one comment that I think is legit and needs to get fixed.
**Liudmila Molkova** 29:29 It's just too hard.
**Josh Suereth** 29:31 No, no, no, you had a bunch of, like, nits that are super trivial to fix and not a problem, right? Like, but you had a bunch… you had one that was like, holy crap, we have to think hard about this, I can't just, like, fix it. I have to, like, think through all the implications.
Actually, so we can talk about this one here, because this one, I think, is a bit easier. I did think through this one.
Provenance.
we have to make some decisions around provenance. So, provenance tells you the path, which is the file I read, and the schema URL.
Okay.
When I am dealing with a dependency, I am erasing paths always.
Because I don't think they're super useful.
Because it's not… it doesn't actually tell you, like, the file and the model where it came from anymore, especially with package dependencies.
And because I'm using virtual directories, it gives me the virtual directory file for a lot of these, or it's like one giant YAML file for everything. So that's why when I'm resolving from a dependency, I'm basically erasing path and putting schema URL.
And saying this came from a dependency, like, you need to go look at that dependency and figure out the lookup from there.
**Liudmila Molkova** 30:44 -H.
**Josh Suereth** 30:45 But I wanted to make sure, like, I'm not missing something here of, like.
am I too grumpy about how bad the paths were when I first did this, that we should include the path, or not?
**Laurent Querel** 31:02 Josh, what would prevent to have the the relative files here.
**Josh Suereth** 31:07 What?
**Laurent Querel** 31:08 What prevents to use a relative pass?
Yeah.
For me, that behave exactly the same way, independently of a local versus, An imported registry.
**Josh Suereth** 31:22 We… we… remember we're not preserving the path when we publish, because the path gets erased, and it becomes a single file.
So, basically, when we… when we do that, we… I… when I went through everything, I just,
**Laurent Querel** 31:37 Okay.
**Josh Suereth** 31:38 There's a path, I just… By default, basically have empty paths for all…
**Laurent Querel** 31:45 Okay, yeah. And and we don't store the We don't store this initial location in the resolved schema.
**Josh Suereth** 31:54 No, and I can confirm that with you here. Let's just take a quick look.
I… because, again, I remember making that change, but it could be that somebody undid that change later, and I'm not aware.
Is it under lineage, just provenance?
Where does Providence live, do you remember?
Oh, here we.
**Laurent Querel** 32:19 No, I don't remember.
**Josh Suereth** 32:21 Okay. Yeah, this is always skipped.
**Laurent Querel** 32:28 Okay, okay.
**Josh Suereth** 32:29 Only kept for local debug messages, and it's only meant to be for your local definition files.
Yeah, okay.
**Liudmila Molkova** 32:38 Yeah, most of the time dependencies are.
Published and resolved. Well, at least the future we want to have.
**Josh Suereth** 32:48 Yes.
**Liudmila Molkova** 32:48 Yeah.
**Josh Suereth** 32:49 Yeah. So that's the idea there.
Okay, as long as you're okay with that one, that's… that was the one issue, and then the other thing, what… what did you have in here?
Because I think, the thing I'm… what was your other comment?
You need to return otherwise? Yes. There's, The error handling in this function is super suspect, and I forgot how lazy it was.
I just if-okayed everything, Lauren. That's all I did. I don't have else's at all.
And so, there's an error scenario that is just not handled that I have to think through. So this… this is actually, I will work through that, but once that's done, I think we'll have good error messages, and then, the rest of this is relatively trivial to, To… to sort from.
**Liudmila Molkova** 33:43 My AI told me that maybe you have some check somewhere else that prevents it from happening, so you would never… Have an error case here, but then if it's.
**Josh Suereth** 33:55 I do, but that doesn't mean that I should just silently ignore it. That means I should… might want to expect it away, right? Or something like that, yeah.
**Liudmila Molkova** 34:05 Yeah, okay.
**Josh Suereth** 34:06 To make it clear to the reader what the hell's going on, because if you read it, it's like, okay, cool.
This one here, I… Yes, this is how it's supposed to be, I have to go remember why.
of… Local dependency attribute, we pick one from dependency. Yes. This… this is also… there's something else that makes this okay.
And then, do we need fallback when lookups fail, or it's not possible? Yeah, if a lookup fails, we have nothing we can do.
Because a… the lookup schema, it's not actually lookup schema in the cache, it is lookup and resolve.
**Liudmila Molkova** 34:56 Okay.
**Josh Suereth** 34:57 is probably a misnomer, like, maybe I need to change the name, but if the cache doesn't have the schema, it will actually go do the resolution at that moment.
**Liudmila Molkova** 35:07 Oh, I see. So it it will never fail.
**Josh Suereth** 35:11 It will never turn out.
**Liudmila Molkova** 35:13 Okay.
**Josh Suereth** 35:13 If it fails, it's because when we try to resolve the schema, we fail to find it, or that schema's illegitimate or bad in some way. So, it will not fail in a way that's not legitimate.
Like, it will fail…
**Liudmila Molkova** 35:25 -H.
**Josh Suereth** 35:26 telling you, like, hey, I can't find this dependency that you told me exists.
And is transient.
So, yeah, that's literally why we wrote the cache lookup here, is so that we can find the transient dependency in the chain and go look it up fresh as needed.
Okay.
Yeah, that's also the thing that I want to hook up into Weaver Live Check, because Weaver Live Check can just call lookup schema, and it will actually go do the resolution for the schema it hasn't seen yet, and then you can live check against the schema you're on.
Okay, so if that's all there, then we can merge this and do merge conflicts, because I do think… let me just confirm, real quick.
I had to do a crap ton with Attribute, and I was not happy about it, but I couldn't… I didn't have an alternative.
And I believe… Yeah, I blew away all these attribute things.
With this, like, upgrade attribute crap, right?
**Liudmila Molkova** 36:29 Mmhm.
**Josh Suereth** 36:30 And this is what I think conflicts with some of the work that you did.
But I can go check. If you touched attribute RS… I know that you touch lib and loader and stuff, they might be trivial. If you touch attribute RS, that's the one I'm worried about merge conflicts, and I don't know what's going to be easier here, but I'm hoping it might be easier for you to build on mine than me to build on yours.
**Liudmila Molkova** 36:51 Yeah, absolutely. So let's, like, focus on your PR when you… I'm not sure if I approved it, maybe not. If not, then ping me, I'll approve it after you address the comments, and we'll merge it, and I'll… rebase. And yeah.
**Josh Suereth** 37:07 Cool, that sounds like a plan, and I'll try to get through reviewing the rest of yours, Because I think that was, honestly, the only concern I had was just how we're going to merge these all. Cross-register, you're fine. And in terms of priorities, Do you have one that I should look at first?
**Liudmila Molkova** 37:28 Now both of them are blocked in different parts of V2 Migration and Semconf.
But it's not that if I don't, we don't migrate tomorrow or somebody dies. So, like, both of them are necessary, same priority. But the first one is self-contained, this one.
And then the second one is the the head of stacked three PR.
Long story.
So probably this one is easy to get through and be done. And, The next ones are just the beginning.
**Josh Suereth** 38:05 Okay.
So this is interesting.
You're actually caching the extends group type instead of… Anything. Alright, I'll take a look then.
Cool!
**Liudmila Molkova** 38:20 Yeah.
**Josh Suereth** 38:21 We do have… oh, and if… in case folks didn't see, I didn't call this out, I think, we have a pull request dashboard now, in addition to the dependency dashboard. So if you click on this, it's… it's really handy to basically say, oh, a maintainer has to implement this.
Or has to do something here.
And what's waiting on reviewers, waiting on authors, waiting on external, and the draft. So, waiting on reviewers, we do have quite a bit to go through.
Although I think some of these really old ones, we might just want to close.
And, and…
**Liudmila Molkova** 38:53 Tailgot?
**Josh Suereth** 38:54 We… maybe we should add a stale bot? I think we can just go through manually and close them, and say, hey, you know, reopen these against latest, because we made a lot of changes.
But…
**Liudmila Molkova** 39:10 Yeah.
**Josh Suereth** 39:11 But yeah, the tolerate unknown properties and resolve schema published manifest.
This one…
**Liudmila Molkova** 39:19 It's still relevant. It's just waiting for the time where it will be important. I think we have to do this before stability.
**Josh Suereth** 39:26 Yeah, okay.
I do like that most of these are under 7 days, like, 1 week for this. That should be easy to patch, too. That's just a renovate annoying thing.
This is one that's waiting on us that I wanted to call out, the Semantic Convention V2 for Weaver Registry Infer. I did approve this, and I was… it's sad Jeremy's not here.
It looks like it's ready to go. Any concerns if I merge this sucker?
This was dead simple. No? Okay. I'm just gonna merge it now.
**Liudmila Molkova** 40:00 Awesome.
**Josh Suereth** 40:01 Touches. Yeah, it only touches it for her Okay.
Cool. But if you hadn't seen the pull request bot, I installed it, Trask made it, it's freaking amazing.
In my opinion, and it makes, like, if you only have, you know, 30 minutes on Weaver, just go through there, look at the waiting on maintainers first, go through waiting on reviews.
I think this is a game changer for us in terms of maintenance, so I'm happy.
**Laurent Querel** 40:28 That's nice. We, we are looking at something like that for the, for Telero. So, so how you asked basically Trask to to enable this capability how that works.
**Josh Suereth** 40:39 No, it's… it's super easy. You can do it… you can self-service. So there is a proj… oh, crap. I have access to private things.
It's fine. Shared workflows.
**Laurent Querel** 40:52 I will approve.
**Josh Suereth** 40:53 flows.
There is a pull request dashboard, and so there's a JSON file that you just add yourself to.
**Laurent Querel** 41:01 Nice.
**Josh Suereth** 41:02 Look at the pool requests, I'm guessing.
I can show you the one where I added all our stuff.
Where is it?
Oh, wow, a lot's happened on here.
Oh.
Where?
Where's the thing I opened, huh Is it owner or author? It's author.
**Liudmila Molkova** 41:29 Author.
You can also do author at me.
**Josh Suereth** 41:34 Author at me, I'll have to remember that. So, yeah, if you look at what we did here, basically, you just list your, repository, the approver teams, so that it knows whether it's, like, goes into the waiting for maintainer, waiting for approvers.
And then you list how many required approvals there are, so it actually, like, knows whether it's waiting for more approvers, even when one person approved. And then you can optionally put Slack channels and Slack user mapping. I know you're using that in GenAI with Bella.
**Laurent Querel** 42:03 Nice.
**Josh Suereth** 42:04 I don't know what that does Yet.
**Liudmila Molkova** 42:06 It it it posts, review notifications in the channel. We all ignore in the same way as GitHub notifications.
**Josh Suereth** 42:16 Do you want me to put that in the, like, the Weaver Maintainer's chat, so we can have more chat messages in our lives?
Or…
**Liudmila Molkova** 42:24 Actually, it'd probably be better for Weaver because we have relatively low number of PRs.
Maybe Rust is the best language to do things, in the era of AI where everybody sends PRs your ways. But in GenAI, it's just too too many notifications. For Libra, I can't I can't see it being helpful.
**Josh Suereth** 42:47 Okay. I, I did add it for Weaver examples and Weaver packages, so maybe I'll update the Slack channel. But yeah, Lauren, I would, I would highly recommend, just go configure it for…
**Laurent Querel** 42:56 Yeah, yeah.
**Josh Suereth** 42:57 Let's see what…
**Laurent Querel** 42:58 That's super nice. Thank you. Yeah.
**Josh Suereth** 43:02 Yeah.
**Laurent Querel** 43:02 Mmm.
**Josh Suereth** 43:03 I also, internally, I have something that I was using that I was thinking about. Survey on merge PR shared workflow. Interesting.
Anyway, the idea here is that we can have a whole bunch of, shared workflows that we can use across projects in OpenTelemetry, so there's a lot of cool things here.
**Laurent Querel** 43:28 Okay.
Okay, great. Yeah, because yesterday I was, I was exactly looking at something like that. I discovered something named pull down.
I think it's a product with an option, a free option for open source projects.
Basically, it's a GitHub app that you can connect with your project.
connect a set of metrics and states from the the pr list.
and and creating a report and sending that to slack.
But it looks like it's already doing more as that. So that's cool.
**Josh Suereth** 44:08 Yah.
**Liudmila Molkova** 44:08 I hope they use CI/CD semantic conventions first.
**Josh Suereth** 44:13 So, what I have is a bit more intense, which actually goes through each issue, and, like, does an AI summary of the activity from the past 24 hours on the issue.
Okay. Then I take issues in, like, 30 to 40 chunks, and I have AI generate a set of categories for all the issues, and a prioritization score based on my interest like, fit in.
**Laurent Querel** 44:40 Oh, okay. Yeah.
**Josh Suereth** 44:42 I'm going to have it make me a dashboard with categories and priorities of things to look at. This is how I was paying attention to Otel Arrow, where it would be like, I'm like, I'm interested in Otel Arrow, none of its high priority, but just tell me what's interesting that's happening. I'd be like, oh, here's a new PR that defines your language, or they're working on a security vulnerability on this thing with Rust over here, that kind of stuff.
So I get, like, that… that's at the bottom of my dashboard.
And then at the top of my dashboard is, like, you know, Weaver, SemConf, Entities, like, all that kind of junk. It was… it's pretty awesome. You might be able to work your way to victory there, if you, have enough tokens to do it, but I was trying to make it semi-automated.
**Laurent Querel** 45:27 Okay. And it's, it's, it's an app that you have.
Public, or this app is public, the one that you are just describing?
**Josh Suereth** 45:37 It's private, unfortunately. It's 100% vibe-coded, and I'm working on trying to figure out what to do with it to make it easier to use. Lubella can use it now. I think I sent it to you way back.
Yeah, I… it's something I want to make a bit easier.
Okay.
I'm debating rebuilding it, because it didn't take me too long, on top of this.
So basically, like, you would give it a set of projects in OTEL, it would grab the PR dashboard and then go through it. The one I was doing, actually, it used, you had to give it your API credentials for GitHub, read-only, and it would look at all issues and all pull requests, and put them all together in one big glob.
So… I was gonna take a look at what Trask did here and see if maybe I can… Take some of what I did and contribute. The only thing I'll caveat, mine used a lot of tokens.
And… But there's a lot of caching.
So if an issue hasn't changed, right, you don't recalculate the, like, sum.
**Laurent Querel** 46:43 Mmhm.
**Josh Suereth** 46:43 And prioritization score of it.
**Laurent Querel** 46:46 Yes.
**Josh Suereth** 46:47 Okay.
**Liudmila Molkova** 46:47 I think this one is based on GitHub notifications and this is the nice part of being a GitHub workflow that you just.
focus on things that's changed.
**Josh Suereth** 46:59 Yes.
Yep.
Cool. Alright, we should probably call it.
**Liudmila Molkova** 47:07 Yeah, good to see you.
**Josh Suereth** 47:08 Yeah, good to.
**Laurent Querel** 47:09 Yeah, thank you. Thank you. I was away for a long time.
Try to reconnect.
**Josh Suereth** 47:17 Yeah, I hope.
**Laurent Querel** 47:17 Thank you so.
**Josh Suereth** 47:18 one. Yeah.
**Laurent Querel** 47:19 Sorry?
**Josh Suereth** 47:20 I hope everything's going well. It's been.
**Laurent Querel** 47:22 Yeah, it's going well. I was on vacation for 3 weeks, so I can. I can't complain And, otherwise, a lot of work that prevents me to be, part of Weaver for a long time. But I think I told you a long time ago that I was trying to to use. We were massively into a terrible. So we are. I think we are ready to go in this direction. Finally.
So, hopefully I will be able to show you, a deep integration in, I don't know, in one or two months.
Hard to say exactly, but,
**Josh Suereth** 48:02 Nice.
**Laurent Querel** 48:03 Really, the inter for me. It's it's not only using live check.
Obviously, the ability to create custom semantic conversion registry, but also.
to create a new Rust, a little bit special client SDK that will be used into the project. So the code generation will be used definitively.
And I will base that on the version 2 of the format.
What what's worried me a bit.
Was the discussion we had just before with this, user.
Regarding the… the idioms.
Especially in the code generation.
because the open for me in the code generation, especially for attribute that are any type.
Oh.
I'm I'm not a big fan of at the client Sdk level letting things open.
So, if we caught,
**Josh Suereth** 49:08 That's actually fine, by the way, if you want to have things closed at the client SDK level.
But with the caveat that you need to be able to add enums, because most languages have closed enums, but adding enum is not considered a breaking change.
**Laurent Querel** 49:25 Yeah, but we we can't. It looks like even now, we can't really refine an existing enum and extend it.
That's my understanding of what I think Lydia mentioned before.
So if this capability does not exist, then… the the trend or the the cost. The consequence of that will be a redefinition of existing attributes just to.
**Josh Suereth** 49:52 Well, well, no.
**Laurent Querel** 49:53 The corresponding and invariant.
**Liudmila Molkova** 49:55 Oh.
**Josh Suereth** 49:55 Here's what the consequence should be, Lauren, or I hope. We have a longstanding bug to allow it in some fashion. And so I think the consequence should be that you fix it.
**Laurent Querel** 50:06 I was thinking, seeing it, I was thinking.
**Josh Suereth** 50:12 Yeah, there's…
**Laurent Querel** 50:13 That's the apology. Yeah.
**Josh Suereth** 50:15 Yeah, I don't.
**Laurent Querel** 50:16 I agree, I agree.
**Josh Suereth** 50:17 number off the top of my head, but, like, I think Ludmilla had a proposal, if I remember right, about what that would look like, and how to do refinements and things on the news. We had some back and forth, I think it was, like, Ludmilla, myself, James, you.
basically revive it and fix it, is what I would say.
**Laurent Querel** 50:34 Yeah, yeah, yeah, no, but that's, yeah, good, good, good, good answer. Thank you.
**Josh Suereth** 50:39 Yes.
**Liudmila Molkova** 50:39 Exc.
**Laurent Querel** 50:40 Yes.
**Liudmila Molkova** 50:40 I, I, I think we need to, like, I, I'm happy if somebody would work on it, but I think.
We… I don't have a good Idea.
how to do this, but mostly alright. I think I found an issue in the chat.
I think we have two types of enums, and maybe we should somehow separate them. The first one effectively acts as a refinement identity. It's like, for this database, this enum value must be that.
And in other cases, we just want an open… set.
And we want to add things.
Well, sometimes maybe we want to remove things, but that's… You see that like.
The way we use enums today is not… Maybe we abuse them.
So maybe we need the discrimination, you know?
And we need some whatever, you know.
**Josh Suereth** 51:53 I… I was actually thinking that as well, as we were talking, of, like, it might be… That we want to have a, okay.
a flag on Enums that says whether or not you can lock them down, so it's not all… you know, What it, you know, has to be this, has to be that kind of a thing.
**Laurent Querel** 52:13 Yeah, we…
**Liudmila Molkova** 52:14 What happened?
**Laurent Querel** 52:15 once… with consequences on… the stability of the… what will be allowed to do, I guess.
Because the the openness, give us a lot of flexibility on the evolution of those syndium.
So we… If we close them, then we lose basically some of those capabilities.
Which is maybe okay.
**Liudmila Molkova** 52:45 I think, well, in my past experience being client library developer, closed enums is the source of so much pain. We never even had the idea of having a closed enum because the day comes that you legitimately want to extend it, then you break the world with it.
**Josh Suereth** 53:06 I hear what you're saying. I think closed enums are a form of hubris where you assume you know what the shape of everything looks like.
and you lock it down, and then you're wrong.
And now you're screwed.
So I… I hear what you're saying, but what… I guess what I mean is… yeah, to your point of, like, there might be two types of extension, the… the lockdown closed extension is what I was kind of referring to, like, this thing is this value in this refinement, like, I am this database, it is this thing.
**Liudmila Molkova** 53:39 I would even go further.
I would say that's a special thing that we probably… I need to think how to define, but when you define a metric refinement or a span refinement, you say that this is my discriminator.
**Josh Suereth** 53:54 Yes.
Yeah, and that's how you determine me as a refinement instead of something else. Yeah, I like that. Maybe we could call them discriminator enums or something.
**Liudmila Molkova** 54:03 Yep.
**Josh Suereth** 54:05 I mean, that's a word that we both understood right when you said it, so… I like that already.
As opposed to, like… This is a namespace.
Okay.
You know, Discriminator, I really like. It really tells you what you're using it for.
Cool. At this point, I'm just chatting and not doing anything useful, but good to see you, Lauren.
**Laurent Querel** 54:31 Thank you.
**Josh Suereth** 54:32 Looking forward to all the pull requests you have to make to make things work.
**Laurent Querel** 54:36 Thank you.
**Liudmila Molkova** 54:37 Thank you.
Okay.
**Laurent Querel** 54:40 Yeah, I'm sure that I can do infinitely more than the last year.
**Josh Suereth** 54:47 Good.
It's all good. I actually do think, our adoption has started to really start to grow a lot, so it is good to have you adopting and back, because I do… like today's discussion, I think we're going to get more and more of those kinds of bugs and use cases, and it's going to be… it's going to be a good time. It's going to be a little frustrating with, you know, all of the usability bugs will show up at the same time But, I think it'll be a good time. The next 6 months is my expectation.
**Laurent Querel** 55:15 Yep.
Good. Great. Cool.
Thank you, guys.
**Liudmila Molkova** 55:19 See ya.
**Josh Suereth** 55:21 See you.
