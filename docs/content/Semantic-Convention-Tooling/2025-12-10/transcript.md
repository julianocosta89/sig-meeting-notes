SIG: Semantic Convention Tooling
Date: 2025-12-10
Duration: 62 minutes
============================================================

## Zoom Recording Transcript

Josh Suereth 00:02:24 Hey, can you hear me?
Jeremy Blythe 00:02:28 Yep.
Josh Suereth 00:02:30 Cool.
How's it going?
Jeremy Blythe 00:02:34 Good.
Josh Suereth 00:02:37 Let's get this, set up here.
Jeremy Blythe 00:02:42 Yeah.
Josh Suereth 00:02:46 Alright, should we do a quick triage?
Jeremy Blythe 00:02:53 do it.
Josh Suereth 00:02:55 Okay.
Find replacement for deprecated Serdiamil. Is Sergeyaml still deprecated? I believe it is, right?
Jeremy Blythe 00:03:05 that, isn't it Sapphire? And we already started using it?
I'm not sure if it's complete enough for everything that we do, but…
Laurent started using Sapphire in a few places, I think.
Josh Suereth 00:03:20 Okay.
So I think we still have to take care of this one. I'm gonna put this into consider for next release of Sapphire. Do you think… do you think Sapphire is ready for us, or not?
Jeremy Blythe 00:03:31 it's still, like, early days. We could… We could try.
Josh Suereth 00:03:35 Okay, I'm gonna leave it… I'm gonna leave it where it is, then. Weaver Registry Search subcommand…
This is about having a registry search.
Jeremy Blythe 00:03:46 If we get time today, I'd like to show you a proof of concept I've been working on.
Josh Suereth 00:03:53 Cool, okay.
Jeremy Blythe 00:03:54 That.
Josh Suereth 00:03:56 Yeah, yeah, that'd be awesome.
I'm gonna skip down to just newer ones, because I think they're here.
Our dependency dashboard, allow attributes to be excluded. I don't think we have anything new, then.
Jeremy Blythe 00:04:09 Nope.
Josh Suereth 00:04:10 Real quick look at… oh, for you, Lauren, because I just sent this, we have 22 open PRs.
In the 22 open PRs, a whole bunch are updating actions around, cargo disks, and then the notion that we pin all of our dependencies cannot progress because it's tried to do cargo disk things in that one.
So what I wanted to do, what I think will fix it is this. Basically, we just tell it to ignore the release workflow, and then I think everything should start cleaning itself up.
Jeremy Blythe 00:04:50 Cool.
Josh Suereth 00:04:52 This isn't the best, because the release workflow, like, there's a depend… there's, like, version numbers in a YAML file for CargoDisk that I think Renovate doesn't understand.
So, I want to get to a point, eventually, where we get Renovate to Understand CargoDisks version numbers. Or…
Possibly not use cargo disc, but that's,
I don't… I don't have aspirations to build my own, you know, release pipeline right now. Just… with the friction we've had with it, I'm not… I'm not sure. We don't touch it at all, right? So…
If we just set something up that worked.
Jeremy Blythe 00:05:32 The thing with CargoDust is, when it works, it really works well.
Josh Suereth 00:05:36 Yeah, and when it doesn't work, it's impossible to fix.
Jeremy Blythe 00:05:39 Exactly.
Josh Suereth 00:05:43 Yeah, no, I agree. Like, when it works, it works really well, but it's… it's very loosely maintained.
So… yeah. Anyway, we can talk about that later, but if you have a chance to review this, I'd like to get this merged to clean up our PRs.
Because I believe, we have continuous live check. Is this one you wanted to get in for the release?
Jeremy Blythe 00:06:05 I would like to.
Okay. Yes?
Josh Suereth 00:06:08 Let me add that to…
Jeremy Blythe 00:06:11 I'm just refactoring that, your… based on your comment.
Josh Suereth 00:06:15 Yes, yeah, yeah.
Jeremy Blythe 00:06:17 It will be… Maybe tonight?
I'll be ready.
Josh Suereth 00:06:22 Okay.
That sounds good, or maybe I didn't even want to take a look.
Jeremy Blythe 00:06:28 I'm gonna go with an enum, actually, but, it's kind of…
You end up with… you end up in the same spot.
Josh Suereth 00:06:37 Yeah, when I first started writing Rust, I was really adverse to ever using Dyne, and then, as I started using it more and more in anger, it was like, oh yeah, actually…
You do this everywhere in, like, C++ and in other languages, it's just, you know…
Eventually, we have to do it, so…
Okay, oh, update markdown now supports V2. I would like to consider this for next release, but I think we need to hear from Lyudmila if this is actually broken.
Because this is still kind of a preview feature, so I think we have room to change it.
If we don't like how it works now.
Liudmila Molkova 00:07:15 It's not broken, but let's talk about it because of the… Public groups.
Josh Suereth 00:07:22 Oh, yeah, yeah.
Liudmila Molkova 00:07:25 And, let's talk about the, sorry, registry versus refinements.
Josh Suereth 00:07:30 That's… Yeah.
Liudmila Molkova 00:07:31 Maybe we don't need both.
Josh Suereth 00:07:34 Maybe we don't… I just threw in everything for completeness. Yeah. I have an idea around that, actually. Do you want to talk about it now?
Liudmila Molkova 00:07:43 Yeah, so I played with it in some cons.
it's kind of weird to sometimes use snippets that start as registry, sometimes with refinements. Like…
Four of us here might understand why we do this, but people in SEMCONF will always make it wrong.
So I think we should either tell them to always use refinements, because we will have everything in refinements, right?
Or we should just remove the prefix, because why is there a need to… use… Registered dot.
Josh Suereth 00:08:21 Yeah, what I wanted to do here was just have this be a JQ expression on the…
On the output.
Liudmila Molkova 00:08:30 Oh!
Josh Suereth 00:08:31 Seriously.
Yeah, like, I can do that. So what I might do is support any JQ expression,
in the SEMCOM thing.
and then have this as a speed syntax. So the other thing I can do, which is a lot faster, that I could do for this release, is just make it so if you put events without
registry or refinements in front of it, it defaults to refinements. So in some conv, we would say events.whatever, group, attribute group.whatever, and you get the refinement of it.
Liudmila Molkova 00:09:07 Yeah, you mentioned something about the… JQ.
like, I had a crazy idea of how to solve attribute group problem without solving it.
Josh Suereth 00:09:21 And if we…
Liudmila Molkova 00:09:22 could have… Registry.attributes.namespace, it would actually solve it.
Josh Suereth 00:09:33 registry.attributes that namespace.
like…
there'd be… you'll have to… you'll have to write this down for me. What was I… what would I want to show you? Where's the markdown?
What I was thinking was, in this markdown, you could just have this, instead of being, you know, foo.bar.bar, this would just be a JQ expression against the whole registry.
Liudmila Molkova 00:09:58 In V2 format Yeah, this alliance, because let's say I want to run their server group.
I don't care if it's a group, I actually want to run their server namespace.
And then… If I write registry attributes…
Josh Suereth 00:10:22 Server!
Liudmila Molkova 00:10:23 I don't know.star, or if I can write a JQ.
Josh Suereth 00:10:28 You, you could just JQ it there. Yeah, because, like, that's, that's, that's what we would get to.
In that world, the other thing is snippet.md.j2 is hard-coded.
It could be that we turn this into set, have, like.
Okay, so what it would be is this would say Weaver instead of semconf, because I would need a new parser.
then you would pass it a JQ expression and a template that you want to render.
And it will run… it'll be just like a normal templating engine, right? That was the idea.
Liudmila Molkova 00:11:06 That's cool.
Josh Suereth 00:11:09 Okay, I don't have time to do that this week.
Liudmila Molkova 00:11:12 Yeah.
Josh Suereth 00:11:13 we can hold off on this PR, and I can go that direction, if that makes more sense.
Liudmila Molkova 00:11:21 Yeah, we can hold on this off, so what I was thinking, that maybe actually switching snippets…
2V2, markdown generation is not a burning need. The burning need is the…
Josh Suereth 00:11:36 Resolved schema.
Liudmila Molkova 00:11:38 And I can make progress this year and see… and, like, start maybe publishing results schema.
Josh Suereth 00:11:47 Okay, sounds good. Ideas… Move from… this, Senkov… Syntax.
2… Bever… syntax… Jq expression. Sorry.
This is… group.
And then we have the attributes.
To JQ expression and template.
File.
more flexibility…
Default to refinements.
Let's simplify… 90% usage.
What was the other… you had another idea here, Luke Mellon.
GQ Hopper.
functions to create, namespaces for Azure.
I think. Okay, does that capture everything?
Liudmila Molkova 00:12:58 The snippets to support, namespaces.
But then, your idea is more generic.
Yes. So, yeah.
Josh Suereth 00:13:11 Excluded to support namespaces.
Okay, cool. Yeah, I'll… I'll…
We'll pause this one, I'll take it off of to consider for next release, and we'll just mark this as…
V2 schema, and go from there. Alright, so…
Do we have anything else we want to consider for next release? Continue to support live check, I… if you make that refactoring, everything else looked gravy to me there, Jeremy, so I think that one's good to go.
This prom name function.
I don't think there was anything in here that was blocking…
Prometheus metric names, Prometheus Unit Name.
Liudmila Molkova 00:14:10 Do you know why it's plural?
Josh Suereth 00:14:13 No.
I mean, it is… I think it's getting more than one name.
Liudmila Molkova 00:14:22 Oh.
Josh Suereth 00:14:27 I need to get actionable helper function, the prom unit goes through unit… yeah, where's the prom stuff?
Ugh, not applicable per unit. This is weird that he puts a 1 there instead of the bracket, because the bracket…
Oh, God, okay.
We'll have to… I think this doesn't handle UCUM…
100%. And I don't know why he's using string instead of cal. I should do this, yeah.
Just, tolerance.
Okay.
Oh, wait… No, no, no, never mind.
I just come… Instead, there we go.
Stay with the end.
Very different.
Alright, so this looked good. Where's the multi-name thing? So, he looks for sanitizing the name.
Grab suffixes for all these things.
And sanitizes the name as a vector. Where's his test case? I want to show this, because this is where things get weird.
This hard codes every single unit that is supported currently today in our spec for Prometheus.
here's the name sanitization thing. So, he gives us a single name, and then this is the name that gets output from Prometheus.
That's for sanitize name.
Here's test unit suffix where those convert, and then test get names. I believe this is an example, right? So, if you have a HTTP with a unit of 1 and it's a counter, you get back both HTTP requests and HTTP request ratio total.
Liudmila Molkova 00:16:57 Okay.
Josh Suereth 00:16:59 Now, How are you intended to use this
I feel like we should get the docs to be updated, so…
I can make a comment. I might… I might hold off on this…
Liudmila Molkova 00:17:14 I'm gonna go…
Josh Suereth 00:17:15 to consider for this release, but I think we need some back and forth here. I'll spend some more time on the code review.
But yeah, this is the example, like, so memory usage and memory usage bytes.
New Prometheus will allow this, because they are not limiting metric names anymore, right? Old Prometheus will use this. He's returning both of them in the same function. I feel like that should be a flag.
No.
Oh, God.
This is because it's a summary.
Liudmila Molkova 00:17:51 Yeah, I mean, if Gregor can write the documentation, it will be clear on what's intended usage, and then we can…
But yeah, it's, it's, it's… I don't know how to use it.
Josh Suereth 00:18:02 Well, so this one here, just for context, when OpenTelemetry sends one histogram, in Prometheus, that gets turned into three individual metrics.
So, bucket, count, and sum are the three metrics names that are used in Prometheus for a single histogram.
And then there's also the conversion of, do I include the seconds in the thing? Do I use dots? Do I use underscores? Like, he's expanding all possible Prometheus metrics that could be defined from a single hotel metric, depending on your configuration params.
Liudmila Molkova 00:18:37 Right, and it might make sense for the documentation purposes, but if you want to do quad generation, you probably want to say, okay, give me…
Josh Suereth 00:18:48 The things, yeah.
Liudmila Molkova 00:18:49 -Oh, maybe just the first one.
So, like, you would want to know where in this array the thing you actually want is, and what they mean.
Josh Suereth 00:19:01 Yeah.
I'm fine with a thing called Prometheus metric names that returns all possible, if we also had Prometheus metric name that had configuration parameters, that would say, like, dots are acceptable and add unit, right?
then it'd be… okay, I will make that comment on this. I'm gonna add this to consider for next release.
And we'll see if we can get that fixed up, in time.
Where I always go past it.
artwork, and then…
Cool. I think that's it for PRs that are in a shape that we can merge them.
Yeah, this one's still blocked, I believe. Okay.
Let's go start some discussion, then. Triage.
figured out.
Consider…
The next release. Alright, so what I would like to do is release this week and call it a V2 preview.
So my question is, what remains to be done for V2 Preview? If we were to say, hey.
Try out Lever.
You can try this dash dash v2 flag. It should work with live check, it should work with registry generate, it should work with, policies.
It won't work with Update Markdown, but again, I think we're not gonna be promoting Update Markdown, we're gonna be promoting Generate for everyone.
It works with Emit, right, Jeremy? I think every… it works for everything. Let me pull over the,
I'll pull over the tracking bug.
What do we feel like we want for that before… like, is there anything missing?
Liudmila Molkova 00:20:52 You're not sure in the tab.
Josh Suereth 00:20:54 I know, sorry, I'm gonna try to get over to the other one.
Okay.
So yeah, update markdown is on hold, registry stats… we only get stats for signals, not refinements, but I don't think that's a big deal for a preview.
We have emit, we have JSON schema, we have live check. Those are, like, the biggies, or LiveCheck. LiveCheck, Check, and Generate, to me, are the biggies.
A few things that are also missing…
I don't think… let me, let me add this.
Well, this is baseline integration. I want the ability to…
Resolve a registry from a resolved repo file instead of always from source?
But that could be follow-up work. I actually did some refactoring where it's easier for us to do that.
But, yeah. Okay.
Liudmila Molkova 00:22:08 I… So for, for the…
V2 perspective from some conf. We need the resolve, and we need DIV.
As a bare minimum.
we want…
The update markdown will come later. The check is already supported. So I can switch all but update markdown and some conf…
And… it would… I don't expect any issues there after I had bits and pieces of each of them, except diff, and it should just work.
Josh Suereth 00:22:45 So, diff… Diff is supported now, and DIFF might actually work better
Well, I mean, sorry, it'll be easier for us to maintain, because it's like… the hard part of diff was they were inferring
the V2 schema in diff, and then doing the diff on it.
And now, we already have something that forces the V2 schema, So Diff was actually…
I thought it was easier to read when it was done, because I just copied, you know, Lawrence general diff into one template function.
So… Yeah.
Liudmila Molkova 00:23:18 Cool, so I think we should be good to go.
Josh Suereth 00:23:22 Alright?
The only thing I'm a bit nervous about is do we… we can cut the release, do we want to do any docu… like, this is assigned to you, Ludmila, but it's a huge task.
Is there any documentation work you think we need? I'll put some release notes together and send them out for folks.
Liudmila Molkova 00:23:42 I mean, we won't finish it this week, and realistically, I will write the documentation as I switch semantic conventions to V2.
Okay.
Josh Suereth 00:23:54 Should we advertise that there's a V2 preview prior, or should we just make the V2 preview, put it in the release notes, and then as you work on it with semantic conventions, we can make a big splash later about.
Liudmila Molkova 00:24:07 Yeah.
Yeah, let's do it.
Josh Suereth 00:24:09 Okay.
Let's do it that way.
Liudmila Molkova 00:24:12 If there is documentation, if it's merged, we don't need even a release for people to try it out.
Josh Suereth 00:24:18 Exactly. Because it's already there, yep.
Cool. Let's go back to here, then.
So… Let me write that down.
Let's cut the release, to note, this is a preview for dash dash V2.
And… Link to the issue for all of the commands.
Should work.
Will announce… Broadly.
After we have a chance to… We dig in with SimCone.
Okay, it talks.
There.
Okay.
Alright.
Cool. So, I'd like to cut… so, Jeremy, you're gonna work on your thing today.
Let's sync in the morning tomorrow on whether we can cut the release then. There might be a few fixes I want to get in, sorry. There might be, one or two things I can get in before then that might be useful for the release. I want to talk about a V2 conversion tool that I almost had ready for review.
But not quite for this meeting.
So, let me show you… Yeah, let me show you what this is.
How many branches do I have? 33 branches, wow.
Alright.
Jeremy Blythe 00:25:48 We've got some deletion to do.
Josh Suereth 00:25:50 I do, I do. I am so bad about deleting. What I tend to do is, like, once every 5 years, I'll go clean up my Git repos.
We'll open a pool request to see what this is. Okay, so what… what this sucker does…
Get rid of the expand here.
He is… Oh, oh, sorry.
Jeremy Blythe 00:26:15 Okay. I'll put it, I'll put it in the notes, too, so you can click and follow along if you want.
Josh Suereth 00:26:23 What this sucker does is a giant N2V2 on SEMCOM spec V1,
And it's meant to be mostly lossless, but there are a few things that get lost, and that's what this dot dot is for.
But I make some assumptions. So anytime a group extends another group, I turn it into a group ref in V2.
Anytime I have an attribute roof, ref, I turn it into an attribute ref. Anytime I have an attribute ID, I turn it into a raw attribute on the registry.
Which means I don't know if I have conflicts when I do this. Like, it's so possible you can have conflicts between files.
I don't sort unique and issue warnings yet. That's a thing I can do. This is just baseline.
And I do that for events and entities and all that. I'm also, when I'm doing this, I'm,
like, putting sampling relevant on the ref for spans. When I do entities, I'm splitting things, this is metrics. I'm doing unwrapper defaults on briefs to make sure that you get a string. I'm defaulting stability to alpha if you haven't specified it, like, things that were allowed in V1.
That we would enforce with, like.
errors or warnings when you ran, I had to do something about, so I'm actually doing something here with this, like, forcing things to be alpha, forcing requirement levels, turning annotations into empty maps, that kind of thing.
Yeah, for metrics, for example, if you don't define a unit, I just give you a unit of 1. If you don't define an instrument, I give you a gauge. If you don't give me a metric name, I give you an empty metric name, which might be problematic. We'll have to see.
Yeah, I was just trying to make sure this doesn't fail.
And then you'll have to do some human evaluation on the other end. For entities, for example, I turn all attributes into identifying, that are marked with a role, and anything that is not marked with a role or is descriptive gets turned into descriptive, so you're forced into the entity model here.
And then… right, I warn on a few things that,
if you haven't defined certain stuff, I will do some warnings, and I need to improve that a bit.
Here's an example of it working. Here is the YAML.
that we're converting. It's just a bunch of raw groups for event, attribute group, counter, that sort of thing. And here's the output. We get our attributes array with all the attributes.
We get our entities, we get our event, we get our metric, we get our span, and… oh, that's the other thing, I'm turning every single attribute group into a public attribute group.
Liudmila Molkova 00:29:13 Mmm.
Josh Suereth 00:29:13 We don't know.
Right.
And so, the next thing I'm working on is a way to go through a directory, search for all the Weaver YAMLs, parse them, see if they're version 1. If they are version 1, perform this conversion and write them back, and or do a dry run where I, you know.
tell you what I would produce for each file.
Liudmila Molkova 00:29:39 So it's like, if you have your semantic conventions written with V1, you would use this tool to rewrite it to V2, and then do a human, intervention to correct if anything needs correction. Yes.
Josh Suereth 00:29:53 This is actually, kind of… this is targeted at making it easier to transition to V2, and I'm also thinking about how painful it will be to go through all SEMCOV and change these at some point. It'd be nice if we had an automated tool that we trusted to do this work.
And kind of tell you where it has problems, or, like, what might be broken.
But it also lets us know where we're missing things, so… It's really cool.
Liudmila Molkova 00:30:21 I think we would need some, like, there are tricky places in some conf, where we have group inheritance, and this is where I think we would…
Rather refactor as humans, but there are maybe 10 of these places, and the rest should be trivial.
Josh Suereth 00:30:40 Yeah, we don't have the ability to do refinements yet, and that's the main problem this has, is I'm treating all…
Group inheritance as group ref, instead of refinement.
Because we actually don't have ref… in this model, we don't have refinement in the model.
So I literally don't know if you are extending from a, like, the problem with this is it tries to do it locally, and it's gonna do things wrong.
And you have to do an aggregate view to get things right. So the other way I was thinking about this is if we wanted to have a conversion tool pointed at a directory in SimConv and convert the whole directory at once into one YAML file.
boom.
Because you would have, in that directory, hopefully, all of the, like, internal extends groups are there.
But I also need to… before we can use V2 definition schema.
We need refinements in the definition schema.
We don't have them.
Liudmila Molkova 00:31:49 when you're converting V1 to V2, there is no refinements in V1 either. And when, let's say, we extend the span from a span, what we actually mean is assuming that the
Extended span is a group, attribute group, we don't care if it was a span.
Today, in Vivan.
Josh Suereth 00:32:12 Yep.
Liudmila Molkova 00:32:13 So, like, here two would actually match the current stupid semantics.
Josh Suereth 00:32:18 Yeah, so it's like this, but then you don't end up with a span refinement, so you would end up with two spans with the same type, that would then be a conflict, that would then cause an error.
Liudmila Molkova 00:32:28 No, because… Oh, because you populate type based on the…
You wouldn't. You would just use.
Josh Suereth 00:32:38 Oh, yeah, I wouldn't… yeah, I would actually populate type to be different. You're… that's true, when I do this conversion, so it would actually be okay.
It doesn't support what SemComp wants it to be.
Right. But it would work.
It wouldn't work for metrics, though.
Or no, it would work for… it would… metrics would have a conflict, because we use metric name.
Liudmila Molkova 00:32:59 But we don't metric refinement, we don't have metric refinements. We want to, but we don't have them.
Josh Suereth 00:33:04 Exactly.
And a metric refinement, like, again, I think we could add…
We have to figure out what we want the syntax to look like for metric refinements, you know?
Liudmila Molkova 00:33:20 And whether you can refine the refinement.
Josh Suereth 00:33:23 I think it's fine to refine a refinement, personally. Like, that… we can… we can deal with that. But…
Yeah. Anyway, okay.
Just wanted to show this,
If this… if you think this has legs, I will,
finish up this PR with, like, a basic thing. I don't think we would advertise this to people yet, but we could try it on at SEMCOM and see what it looks like, and see if we like it.
Okay. Cool.
I was pretty happy with how it turned out, actually, and I think it's good…
it's a good exercise to just continually pressure test the V2 syntax to make sure that we're happy with what it looks like, and then, you know, it's cleaning up issues that we had, so…
Cool.
Dang.
Jeremy Blythe 00:34:10 It's… V2 is definitely easier to work with, like, In the codebase. It's like…
Josh Suereth 00:34:15 Yes.
Jeremy Blythe 00:34:16 so it's… and it's so much cleaner in the code, like, when you're…
Even just writing tests where you're, like, mocking out registries and things, you don't need all those…
Millions of null s all over the place, or… nuns.
Stuff like that. Yeah, it's so much better.
Josh Suereth 00:34:36 You don't like nuns? I mean, I thought they were everyone's favorite.
That's when we could start calling ourselves a monastery.
Anyway, alright, let's,
Okay, cool. I just wanted to show that. Now, Jeremy, you had a demo, right?
Jeremy Blythe 00:35:00 Maybe… maybe, I'm on a different laptop, so I'm…
when I try to share my screen, it's probably gonna ask me to do some security thing, but…
Let me see what happens.
Do you mind if I try?
Josh Suereth 00:35:18 Yeah, go, go for it.
Jeremy Blythe 00:35:37 Oh, yeah, it doesn't want me to do that.
Sorry.
I'm gonna have to try and figure out what I do here.
Screen sharing… M.
I'll be back.
Josh Suereth 00:36:03 Okay.
Liudmila Molkova 00:36:07 In the meantime, Lamila, I'm adding to the notes, I want to talk about attribute groups, then.
I agree with you that they cover the gaps in our design.
Josh Suereth 00:36:29 Yeah, it's, it's like a, it's like a current workaround. I'm okay keeping the… here's, here's where I'm leaning towards. Things like thread or, Session.
I think… no, was it session? I forget what you had there.
Liudmila Molkova 00:36:47 Bunch of things.
Josh Suereth 00:36:50 What? Exceptions?
Liudmila Molkova 00:36:52 Exceptions. Exception is a good one. Cloud events, they all can be on spans, or they can be on logs.
I can taste them in the… Shut.
Josh Suereth 00:37:07 So, I feel like there's this contextual… attribute, right? So, maybe exception… Rogue.
Things. So this would be… Cloud events.
Jeremy Blythe 00:37:24 Can you see my screen?
Liudmila Molkova 00:37:26 Yep.
Josh Suereth 00:37:27 Yep.
Jeremy Blythe 00:37:37 Oh, you ready?
Josh Suereth 00:37:38 Oh, this is cool!
Jeremy Blythe 00:37:40 Okay, so, I deprecated search and I felt really sad about it.
because I really wanted to search.
I kind of… well, what I did was I made, like, an API layer, and then…
to be honest, Claude really taught me how to use Svelte for a UI, because I'm not very good at UIs. But I did the API backend, I promise.
So then you've got a search tool,
So, you just go, you go to Weaver and you do Weaver serve, And the compiled
User interface is, like, included in the executable, so there's nothing else to… there's no other deliverable.
It adds about 40K at the moment, so it's really not a lot. Svelte's really tiny, which is one of the reasons that I chose that one.
But anyway, so Search is back.
So, I don't know, do you like…
Oop, HTTP… let me go to one of these.
I don't know.
That's an attribute.
So you've got search…
It's searching in the text as well. I found that we used the word impose in a few places, so if I go to, like… oh, that's a bad… that's… that…
There's a bad one where the examples don't render very well, but…
Using the word impose somewhere in the description. So it's searching in the description. It's searching in the notes as well.
Josh Suereth 00:39:16 Nice.
Jeremy Blythe 00:39:18 You get a score.
You get, like, a… you get this score based on where it's found it, so if it's found it in the name, it gets a higher score, so it's at the top of the list. And if it's found it, like, somewhere buried in the…
In the text somewhere. Like that.
it's searching attributes and metrics and…
You know, all the diff… all the signals, so… You know.
When you click on a metric, you then see all of the stuff to do with it?
And you can click through to the attribute.
See that?
That's cool.
There's also, like… so that's, like, the search results. There's also, like, browsing, so you can just go, like, oh, I'm gonna go to the metrics and sort of scroll… scroll through the metrics that are there.
I don't know. Then click on it, and then you get to the same view.
But I wasn't thinking of this… as a…
replacement for search, actually. More as a user interface for Weaver.
So I've also included
started to include schemas, so one of the things we have… one of the problems we have is all the documentation that we need to produce, and I know, Josh, you had a go at, like.
turning a JSON schema into some document file.
You could… you can kind of put it in here. So this is the new forged registry. I can go to attribute groups, and then I can see their information in here.
Josh Suereth 00:40:50 That's awesome, dude.
Jeremy Blythe 00:40:51 the raw adjacent…
And then you can click through, oh, it's a thing of attribute, I can click through, I can get to deprecated.
tells me information. It still needs tidying up, but, like, I just…
Spent a little bit of time, not a huge…
Josh Suereth 00:41:06 Man, this is… this is awesome. Like, let's…
If this is ready, I would… I would review this as soon as possible and get this in. This is great.
I mean.
Jeremy Blythe 00:41:14 how do we… so I've got a… I've got a few, like…
now I'm like, oh, I can turn everything in Weaver into, like, things you can do through our webpage. Like, we've talked about having a playground where we can try out Rego.
policies, we've talked about JQ Playground built in. I want to be able to, like, hot… hot change, the model.
just through the UI, so I could go and, like, make a change to the model and go, like, okay, now this model, and see what it looks like in the UI.
Yeah.
I also looked at what Martin did recently for the, hotel… Demo…
project, and, like, all of the documentation that he built, and he's basically just, like, Boilerplate, just normal documentation.
And it feels like, well, if I've got a tool like this, maybe I don't even need the documentation. I can just use Weaver to show me all of the things.
Josh Suereth 00:42:06 We still need static docs somewhere, like, yeah. Or, we need to find a way to host this, like, the other thing,
I don't know how you're serving this, but if you think about having this as a, there's an option where all the content is completely static.
And so the dynamic, like, things happen via, just pulling in static
static JSON files on, like, with JavaScript and doing it there. That's a way that we can support Martin's use case or get things onto OpenTelemetry I.O, right?
Cause we're not gonna host Weaver and then serve OpenTelemetry I.O. from it, right?
Jeremy Blythe 00:42:44 Both. Well, I'm just thinking, so in my company, one of the things… so I recently had a discussion with… so, OpenTelemetry is spreading out throughout my
my company more and more, and I just had a conversation with another team, and they're like, so tell us about metrics in Open System. I'm like, well, I'm not an expert, but, like, I know that you should name things the same.
Josh Suereth 00:43:03 Right?
Jeremy Blythe 00:43:06 And they've got all these archaic things that they've been doing for years, with bits of hardware, and trying… and having all these problems. Same story we have every day, right, with this stuff.
And then I started to show them the semantic conventions. I went, hey, look, there's this documentation, there's a website, you can go and have a look. And he went, oh, so is there a thing for temperature?
I'm like, probably. How do I find that?
Oh, I need to search.
And I went, oh, it just deprecated search.
I'm sad. So I want to give… I want to give the team, like, here's how you're gonna search, but you're searching over…
When you're developing, you want to search over all of the available stuff in order to pull it into your
Library.
Into your model, right?
Josh Suereth 00:43:51 No, I think this tool, like, if you think of this tool as a tool for developing your semantic conventions, absolutely. If you think of this tool as a replacement for documentation.
Not quite. Like, like, again, there's a… that's where I think…
I like the template layout you have here, and the search, and if we could find a way to expose that on OpenSum.io, absolutely, I would do that immediately, if we could. But I think that's a hard problem to solve. Instead, I think we should focus on getting this out for Weaver. We could call it Weaver Interactive Mode, or something, too.
Weaver… Weaver Host Interactive, I don't know, like, let's give it a name that implies that this is for doing your registry development.
equally.
Jeremy Blythe 00:44:37 Yeah, okay, I just wanted to, like…
Before I put more hours into it, I just want to make sure that we the…
Where the lines are, where we feel comfortable.
like you say, it's not a replacement for the documentation, so if I have that in mind.
it's really extending Weaver being A developer's tool.
And kind of keeping that as the main…
Mindset to have whilst developing it further, right?
Liudmila Molkova 00:45:08 escort extension.
Jeremy Blythe 00:45:11 Yeah, right? So what do you do? Like, okay, now I've made a website, but should it be an MC… oh, when it should be an MCP, right? You don't have… you don't have UIs anymore, right? You just have LLMs that talk to things and tell you stuff.
It's true.
Liudmila Molkova 00:45:23 MCP, yeah, it should be MCP. Like, there should be MCP wrapper around Weaver, for sure.
Jeremy Blythe 00:45:29 Right? We should do that too.
Josh Suereth 00:45:31 Yeah. Yeah.
Jeremy Blythe 00:45:33 Anyway, okay, I just wanted to show you, I'll put some more…
Josh Suereth 00:45:36 The API for it is amazing, and yeah, we can wrap that API in MCP and all sorts of cool stuff. This is awesome, dude. Like, the…
Is the API that you created documented somewhere, too?
Jeremy Blythe 00:45:49 Oh, no, this is, like, I've just really thrown this together. I will… It's just real fast.
Josh Suereth 00:45:57 It looks better than what I would do real fast.
Liudmila Molkova 00:46:02 Last one.
Jeremy Blythe 00:46:03 I think, like, I chose a… I chose a nice looking… Component set?
Josh Suereth 00:46:10 So.
Jeremy Blythe 00:46:10 It's none of my… This is the other thing, is like, how comfortable do we feel about having
This being, like, largely the user interfaces that, like, largely, AI-generated.
Josh Suereth 00:46:24 I… that… doesn't… I… I… let's review the code, but that doesn't bother me too much.
Jeremy Blythe 00:46:30 I think the code is actually quite easy to read, than these giant, things like React or whatever, where it's…
It's quite a… it's quite a… it's quite a thin…
like, component layer, so it feels readable. I was… I'm able to make changes without the AI, and I don't feel bad about it, so…
Josh Suereth 00:46:50 I've done React.js, and yeah, I…
I actually used AI to generate pieces of ReactJS. I forget what it… I needed, like, a component. I was making an escape room for my daughter. She wanted, like, a… I can send this to you, but it's, like, the New York Times Connection game. It's not New York Times Connection.
But it's a connections game, where you have to, like, group things into categories, and then based on how you group them, there'd be a secret number that you have to flow through words that get highlighted, and then you have to type them into a thing, and then it tells you something else to do in the escape room, and this was on a tablet somewhere that, like, the kids had to do. It was pretty fun, and I used AI to do pieces of it, but I will say ReactJS needed a lot of my time
And less AI time than, than I expected, and when it was done, it's, like, somewhat readable, but you have to just… you have to know ReactJS. Like, it's very readable if you know ReactJS, but there's all these weird caveats of, like, what's updated live, what's not updated live. I…
if the… send us the code, we'll take a look. If this is easy for us to maintain.
And, then I'm a big fan of, like, let's get this in and let's move it forward.
Jeremy Blythe 00:48:06 I did… I looked at, like, native Rust things, but I think that would be even harder to maintain.
Josh Suereth 00:48:12 Oh, God, yeah, this is… so this is basically a little bit of JavaScript wrapping a Rust API, right?
Jeremy Blythe 00:48:17 Yeah, yeah.
Josh Suereth 00:48:19 Beautiful. That's exactly what I would have expected. And that's a good separation of concerns for us, too.
Jeremy Blythe 00:48:26 Okay.
That's true.
Josh Suereth 00:48:29 Cool. One thing I did want to mention that I've been thinking about is,
for, like, AI-generated code, I do want to get to a point where we share, somehow, an agent that does that, so we can all leverage it together.
So, like, if you're using an AI agent that is building that UI, whatever context you've built up to that thing, and the instruction set you use.
It'd be nice if we had a way to share that.
in the project, so other maintainers can use the same instruction set, or whatever. I know that, like, with GitHub Copilot, you can put instructions in the codebase. I do want to get to a point where when we think about AI contributions, we're thinking about…
there's… there's the… as Ludmila says, sometimes there's baby, and we take care of baby, and we teach baby how to do things, right? Like, we have… we have an AI that we can write instructions to.
And so when you would submit a PR, you would submit, and here's, you know, updated instructions to that AI agent that will help maintain this section, or…
Theoretically, we should be able to do this just with good docs, you know, of what we did in the architecture, but…
it's something I've been thinking about, that I want to make sure we can successfully share
AI, instead of one person gets a whole bunch of context and is productive, and the rest of us actually are less productive because that context is being lost in the project. Like, I wanted… does that make sense?
Jeremy Blythe 00:50:03 Yeah. Yeah, it does. I mean, I did all of that with, zero
like, no claud… it was Claude code, but I did no Claude code files specifically to, like, tell it my preferences or anything. I did it, like, it's just… there's nothing.
It was all…
Josh Suereth 00:50:19 That's good.
Jeremy Blythe 00:50:20 prompts. But you're right, like, That the context of going through those prompts is gone.
Josh Suereth 00:50:29 Yeah.
Liudmila Molkova 00:50:30 So, AgentsMD is now supported by everything, even Copilot. So, the…
VS Code Edge, and it sounds Google also supports it, right?
Josh Suereth 00:50:43 Which one?
Liudmila Molkova 00:50:44 agents.md.
Josh Suereth 00:50:47 Oh, yes, yeah, yeah.
So we could start, actually, if, like, if you find that you need to fix Copilot with various things, right, we could actually have a WeaverAgents.md file.
where we describe things about our project in agents.md with instructions, and then these… that's what I was getting to, like,
In fact.
It's almost true that our agents.md should be like, hey, here's how you set up, here's how you run tests, here's our code style, but it all points at the other docs to get them to pull in the right context.
But I know from Gemini specifically, when I used Weaver, it literally doesn't know how to run Clippy correctly and fix the problems, unless you make a Gemini.md file.
Jeremy Blythe 00:51:39 Oh, really?
Liudmila Molkova 00:51:40 And Gemini should also support Sajunct.md.
Josh Suereth 00:51:44 Yep, yep, it does. So I think…
it might make sense for us to make an agent.md.
Okay, cool. Let's, let's move on. I want to talk a bit about attribute groups, if that's okay.
Can I copy-paste what you have here?
Yeah, sure.
Liudmila Molkova 00:52:04 Okay. It's in the chat.
Josh Suereth 00:52:06 Yep. Two use cases, so… Semantic convention…
Okay.
So basically, I think there's… there's two cases that I want us to think about whether we have the right model for.
Raw loggy things, like cloud events, Log exception.
Liudmila Molkova 00:52:34 They aren't raw log things, they can be on spans or logs.
Josh Suereth 00:52:39 That's why I said log E things.
Liudmila Molkova 00:52:41 Oh, I see, okay.
Josh Suereth 00:52:43 It's like, there's an event that happened, and I might put it on an event, I might put it on a log.
Oh, sweet.
Liudmila Molkova 00:52:50 spends…
Josh Suereth 00:52:51 Or a spin, sorry, I might put on an event, I might put it on a spin.
There is then contextual things, like, I think…
Source destination might be that thread.
session ID, I don't know what RUN is, what is RUN?
Liudmila Molkova 00:53:12 It's from the previous description, please remove it, it's not an attribute. Not the namespace.
Josh Suereth 00:53:20 Okay.
yeah.
So, I'm seeing these two things, right? I think…
This one here, I absolutely think,
there's something like attribute group, but possibly stronger that we should have. Like, I want… I keep asking two questions in my head as we go through this, is, what does…
generation look like, meaning dock generation or code generation? And the second is, what does live check look like?
And so, for these contextual things, these… there should be a rule where in live check, if you experience an attribute that is defined in a contextual group.
On something that doesn't say implicitly it uses the contextual group, that it's okay.
Because this is additional context, right? So, for a span for an event.
If you get in one of those signals, and there's an additional context from a contextual group, it's cool. And you'll be like, okay, let me look at the contextual group and understand that. And you'll need a lookup to figure out how to go from raw attribute to contextual group.
To do… to, like, do that understanding.
Liudmila Molkova 00:54:36 So wait, let's forget about contextual group. If you see a span in the live check.
And you see an attribute that's not in the definition.
It's not a problem. Spans, in general, are allowed to have arbitrary attributes.
Josh Suereth 00:54:53 They are, but I think we issue some sort of information about, hey, here's an attribute that we don't see in your SEMCOM.
Jeremy Blythe 00:55:01 Well, attributes themselves are tested against the definition of the attribute.
But… but…
So, well, one, spans aren't… we can't identify spans, so we have no way of saying it's required or not. Let's imagine we could.
So even in a metric today, what LiveCheck will do is, if there's a new attribute.
That's in the list.
and it's not one of the ones that's been defined, it will still print it out, but it will just test that attribute and go, like, it will run all of the advisors against that attribute as a standalone attribute.
Josh Suereth 00:55:39 Okay.
So we're not actually checking to make sure, like, are we checking requirement level on attributes for the metric?
Jeremy Blythe 00:55:50 Yes, if they're defined, and then you'll get different… so you'll get a warning that, you know, you'll get a… you'll get a violation if there's a required one that's missing.
Josh Suereth 00:55:57 Yeah.
For men…
Jeremy Blythe 00:55:59 That hasn't been defined at all, is what I'm saying. It's not going to say, hang on, you shouldn't add new attributes here.
Josh Suereth 00:56:08 Interesting. We might want it to for metrics, but that's a different story.
Liudmila Molkova 00:56:12 But imagine, like, a span processor, a metric processor.
We don't have metric processors, but one day we will. That stops something like thread ID. I don't think it's useful, but let's imagine a hypothetical example, it stamps Thread ID on everything.
Yep. It's…
user application which does it, and it should be allowed. We shouldn't… we can… we can maybe warn about it, but we cannot.
Josh Suereth 00:56:44 Well.
Liudmila Molkova 00:56:45 violation.
Josh Suereth 00:56:45 Literally, if you have a dashboard that relies on HTTP semantic conventions, you would break it if you did that.
Liudmila Molkova 00:56:52 you break the… like, okay, the life check is not about, change, right? It's about the compliance.
Josh Suereth 00:57:00 Yeah, I know, but, like, if you were to do that, you would not be compliant. And what I'm saying it's not just that, like, you literally are no longer abiding by the metric definition for which alerts and things would be defined and work. So if you had a whole set of dashboards and such that don't use that attribute, and don't group by it away.
Which is what the problem is with Vetrix. You literally… everything is broken downstream because you've done that.
Liudmila Molkova 00:57:25 I mean, you edit it from the start, and you already have a dashboard that supported.
You built your own dashboards.
Josh Suereth 00:57:32 Then you should not… that metric should not say it's abiding by the semantic conventions.
Liudmila Molkova 00:57:37 I see. Okay. Okay, so metric…
Josh Suereth 00:57:40 Right, yeah.
Liudmila Molkova 00:57:41 Okay, so metrics is a special case.
Josh Suereth 00:57:44 Yeah, that's the special case for metrics. In logs, in spans, not a problem at all.
Liudmila Molkova 00:57:50 Then, does it… does it matter whether it's a group or not a group?
Like, if you have an attribute you don't recognize in metric definition, it's a problem. If you have an attribute that you don't recognize in span definition, it's okay.
Josh Suereth 00:58:03 So, we had, there… there was a…
what can I share? There was a company that wanted to adopt OpenTelemetry, and any attribute that they found not in semantic conventions, they were flagging.
As errors. And they were using our definitions, and I don't remember if they were using Weaver Ford or something else, but they were basically flagging it. Any attribute that didn't show up.
So, if we, you know, if we're going to do… and there was some tool that they had that was, like, telling them that this isn't supported.
I'm not sure where that was showing up or whatever. It could have been how they configured live check, it could have been something else.
Liudmila Molkova 00:58:48 So you can have a strict mode that demands…
Josh Suereth 00:58:52 Yes. You could have a strict mode for folks like that. Then there's, like, the general purpose, let's be realistic here, where we're trying to keep things, like, as best practice as possible, and try to keep things stable.
But there's things that you can do that will violate this contract, and that's fine. You know, it's the real world. I think we will have both, but I'm trying to understand the model
if you are in super strict mode, if we're in super strict mode of, okay, I want to make sure my telemetry definitions match this so that my dashboards work, so I can depend on things reliably.
Right? What do… what does this thread thing mean? Like, what, what does it mean in CodeGen? What does it mean in, LiveCheck? So, the thread thing, if… the way LiveCheck works, where we check attributes independently, everything's great.
If we ever start to enforce on, say, metrics that, like, all of the attributes in your metric have to have been in the definition, otherwise, even as an opt-in, right? Otherwise, you're not conforming to this shape, and we can't guarantee that, you know, alerts and things are designed correctly for the shape of your metric.
I think we could put that into live check, and that'd be reasonable for metrics, and so these groups would not be able to just randomly be attached to metrics implicitly in the model.
But if you wanted to attach them to a metric as an optional thing, I think you… there should be a way to do that, where I can, like, declare a metric refinement that says, here's a refinement of this metric where I have opt-in attributes, which are these other groups.
You know, where I can say this ref group is entirely opt-in.
That, that seems reasonable to me as well.
So if I want to go full strict mode, right, I can ref group this thing as an optional dependency.
And for some signals, we can implicitly treat every public attribute group as a, optional ref group.
That's kind of what I'm trying… I'm trying to tease out if that's the case or not. So these… like, I want to call this, like, a contextual group.
Where this is context that could come from anywhere, they're implicitly opt-in.
And they're implicitly opted on every signal.
Liudmila Molkova 01:01:14 And that if we make it…
reasonably easy on users, and we would have two versions for, let's say, each metric. One is the bare minimum, the other one is this metric plus all these contextual groups.
Josh Suereth 01:01:36 Yeah.
Liudmila Molkova 01:01:41 And we should be extremely conservative on what becomes public attribute group.
Josh Suereth 01:01:49 So… that's where I think that what I'm suggesting is…
this contextual thing we should be very conservative on, like thread?
But that's why I want it to not be an attribute group. I want it to be something that we can be very conservative on that has that meaning, and then attribute groups are just dumb.
Right? Like, I feel like there's this thing that I want to model that is somewhere between a signal and a group.
Liudmila Molkova 01:02:20 Yeah.
Jeremy Blythe 01:02:21 I'm gonna have to, I'm gonna have to drop.
Josh Suereth 01:02:22 Yeah, we're way over time. Okay. Yeah. You get what I'm saying, though, right? Like, it's not… I'm not insane, or am I overthinking it?
Liudmila Molkova 01:02:30 No, no, you're right, you're thinking about much longer perspective than I am.
Josh Suereth 01:02:34 Okay.
Liudmila Molkova 01:02:35 Alright, cool. Yeah, see ya.
