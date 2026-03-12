SIG: Semantic Convention Tooling
Date: 2025-09-17
Duration: 58 minutes
Zoom Recording URL: https://zoom.us/rec/share/RByi6CdDquqsO7p2BWRPUk2Ejz9KgViMNkcsqZdfKslKryBDtOZ9W6oBIrB58ajv.i-qVAjQCL-2olh-0
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 03:47 Hello, hi folks.
**Josh Suereth** 03:52 Hey!
How's it going.
**Liudmila Molkova** 03:56 Good. How are you?
**Josh Suereth** 03:59 Not bad, not bad.
So… Should we, get started a little bit here.
Should we wait a little bit? What do you think?
I think Laurent… Did he make another thread that he was busy this week, or… Late. I forget which one.
**Liudmila Molkova** 04:30 I hope Jeremy will join, I see him.
commenting on GitHub.
**Josh Suereth** 04:37 Oh. Which one gets further.
Yeah.
We're getting a lot of good questions, by the way, on… we verb, and I think there's a lot of good things that we're building here.
I have recently been completely absorbed in other work, basically entities and then work.
projects, so apologies that I haven't been able to make progress on this. Ludmila, your PR looks… Awesome. I think we have to talk through… some minor things? .
**Liudmila Molkova** 05:23 You mean the… What? The attribute groups.
**Josh Suereth** 05:28 Yeah, yeah, I actually, I do really like it. So, I'm working on a PR to do the other side.
**Liudmila Molkova** 05:36 The results?
**Josh Suereth** 05:37 to be… Yeah, this, like, the resolve schema would… resolved to a V2, and that one is… is far more hacky and shenanigan-y, so… I'm looking forward… I think your PR will actually make it a little bit better, but there's also a lot of weird decisions I have to make that we should talk through.
**Liudmila Molkova** 05:57 Yeah.
**Josh Suereth** 05:58 Yeah, cool.
I'm just worried, I hope we're moving fast enough for how fast the community is moving. Alright, let's do a little bit of triage. I wanted to ask a few questions. I want to cut a Weaver release.
So let's go into… I did not merge the project boards yet, like I said I would, apologies.
But let's look at to consider for next release. I think Did my PR get out of here?
Oh, this is another fun one.
Weaver tool fails to correctly parse provided Jinja2 template when generating a markdown file from a YAML data source. EPA file is empty, indicating the tool is either not passing the data to the template correctly, or is encountering an error during rendering.
**Liudmila Molkova** 06:58 Yeah, so I've done some, So, essentially, the problem is that This person didn't use the… The data that was available?
Yeah. And it's… like, if you refer to something that doesn't exist in Jinja, it's undefined.
And we can make it strict, but I tried it in semantic conventions.
semantic conventions explode, so we can only do this behind the feature flag, or we need to fix both semantic conventions and all the code generation stuff. So, I feel like we can only do this behind the feature flag.
**Josh Suereth** 07:39 This is because we… we literally allow referencing something that doesn't exist on purpose and use the undefined behavior in our templates, yeah.
**Liudmila Molkova** 07:49 I don't think we did it on purpose, Ginger does it on purpose, and we just didn't put the… Any guardrails in place?
**Josh Suereth** 07:59 No, I think I leveraged this when I would make templates. I'm like, cool, it's gonna be undefined, it's not gonna increment. That's… that's my bad.
Oh, my camera's not on, I can turn it on, sorry.
Yeah.
No, this looks good, so we can add a feature flag for this. Is this something you think we should add in the next release?
**Liudmila Molkova** 08:20 If somebody has, any capacity, I… I don't.
**Josh Suereth** 08:25 I'm gonna add this to… to consider. I don't know if we're gonna get to it this release, but that seems like an easy one to win.
I want to actually take a quick…
**Liudmila Molkova** 08:35 I opened… I don't know if it's into consider for next release yet.
**Josh Suereth** 08:39 But we had… we had a bug that I had a pull request for. I don't know, maybe it got merged already?
Yeah, it looks like it did… Okay, so we had a few things that we already merged for next release.
Make intermediate registry directory optional within templates. I don't think Laurent has any… PR is active for that.
Allow updating names and referencing attribute. Again, no active PR. Weaver should resolve full URL. I think this one, we have no active PR.
And revert to template extension weirdness. This one, we haven't actually figured out what the problem is yet.
**Liudmila Molkova** 09:22 Yep. Okay.
**Josh Suereth** 09:23 So, I would like to cut a release this week.
Meaning, like, even today, because I think that all the things we need are merged.
Let me… Let me just go through, let's take a look at what those are.
There's a way for us to compare against the current release, right?
So, Lyudmila, your failed when a template doesn't match a file, I think that's a big one we want in. Serializing brief and registry URL, it turns out our resolve schema was not consumable, because we were deleting those.
Which people assumed are required fields, because they kind of are. So, that one's fixed. Ludmeli, your debug logs about config and template loading, I think that one's important to fix. Everything else, I think, is mostly version bumps.
There was a bump of the OTLP proto to handle 1.7.0. That I'd also like to get in for live check. I don't think that hit the previous tag.
Do you remember, Jeremy?
**Jeremy Blythe** 10:29 No, no, that's not been released yet.
**Josh Suereth** 10:33 Yeah. Okay. So I think, we have, we have, like, 3… three things… well, four things, then. And I believe this was on the previous tag, fail when JQ filter fails.
**Liudmila Molkova** 10:47 No, we didn't release it yet, so this one also part of…
**Josh Suereth** 10:51 So this one also… okay, yeah, like, there's… I think we have a lot of good cleanups right now. We don't have anything, like, stellar, but… but we have a lot of good cleanups, so I'd like to cut another major branch with these fixes.
Anyone have any concerns with doing that?
**Liudmila Molkova** 11:07 No concerns. I'm… also would like to check if we can, if we will reach an agreement on the life check, minor improvements, PR, that I have, that if we have a chance to review it today, or in the next few days, I would love it to be part of the release. If not, then it's totally fine to wait longer.
**Josh Suereth** 11:30 That is this one here.
**Liudmila Molkova** 11:32 Yeah.
**Josh Suereth** 11:33 Okay.
**Jeremy Blythe** 11:34 I, let's pump.
**Josh Suereth** 11:36 Let's talk about that.
**Liudmila Molkova** 11:38 Good, Jeremy.
**Jeremy Blythe** 11:39 Are you replying?
**Liudmila Molkova** 11:41 I have it on the agenda, so let's talk about it.
**Josh Suereth** 11:44 Yeah, I'm gonna add it to consider for next release, so that we have it marked, and, why don't you walk us through it while I do that?
**Liudmila Molkova** 11:53 Yeah, so maybe I can, share a quick, not a demo, but just the thing that I'm trying to achieve.
So, I have my demo, which does some regular instrumentation for PenUp.
And I'm also running, VIVER… telemetry check.
So, like, CI-like thing, I'm just hitting an endpoint, I'm receiving whatever telemetry I'm receiving, and what I would like to get as a result is the list of violations.
So this was something I imagine, as the CIA check for open telemetry instrumentation, you run integration tests, you get some telemetry, you validate this telemetry against the semantic conventions.
And what I, duo is… Okay, I want to get all the violations, and I want to summarize them to a list of, things, that are kinda obviously broken.
So… I have my custom Weaver YAML, I have some… JQ, that's custom. Today, maybe we can make it default, or… let's not talk about it here, doesn't matter.
But essentially, I want to build the report. And in order to build the report, I want to have a list of advices that are self-contained.
If I query this full report today, it's… it's extremely difficult to query it with JQ.
The advices are in different places, they don't contain all the information, they don't tell you, which signal they appear on. So, essentially, all I want to do is I want them self-contained. If… We will follow down the path of reporting advices as telemetry items. What Martin suggested, this is also something we would do, we would have Information about what went wrong, on which signal it went wrong, as one item.
So, all my PR does is adds some information to, advisors?
And it also structures them in the way… so maybe I can open it up.
So, for example, what we've done in the past, we, we have the value on the advice, which means… a lot of things, it depends on the context. So what I want this value to be is maybe it's just the map of different properties. It's already a map, it could be a map.
And we can put… Like, contextual stuff there.
Also, the message, I… I… I don't know what we put in the message. I'm suggesting to put the full description, so consumers of this thing does not… need to know how to format the message, what goes into the message. So, you read the message, you understand what went wrong.
**Jeremy Blythe** 15:08 Lamila, are you showing me a different window?
**Liudmila Molkova** 15:12 Oh, sorry.
**Jeremy Blythe** 15:13 We're looking at VS Code at the moment, is that right?
**Liudmila Molkova** 15:16 Okay, so let me share the right thing.
Yeah.
Here is the example of the PR. Now you see the PR, right?
**Jeremy Blythe** 15:29 Yes.
**Liudmila Molkova** 15:30 So, like, here, we used to have value, which is the attribute name. Instead of this, we have it contextualized.
It says, okay, I'm the attribute name, not an arbitrary string.
But also the message, it was just something, and, what my PR does, it explains it, in more details.
So, what I've tried, I've tried to format a useful message out of the advice.
And I couldn't. It's very hard to do, and I don't think it makes… sense. We could just format this message here, because we know what's the problem.
**Jeremy Blythe** 16:21 I think adding more detail to the… adding more detail to the message totally makes sense.
If we update the value to be… I think we just need to check that the standard template that prints everything out is… Gonna be able to understand that?
So… Like, the normal ANSI output.
It's gonna be able to… Work with more… like, detailed… Json in that value.
It'll probably just… If we just print it out, I don't know if it'll just look really ugly.
So… But the point of that value object being, being that is that we could… put anything in there. Just happened to be putting in strings.
**Josh Suereth** 17:16 Yeah.
**Liudmila Molkova** 17:16 Yeah.
**Josh Suereth** 17:17 to double down on it, first of all, I just want to comment, because I'm distracted, the JSON exclamation syntax, I haven't seen that before, but I really like it. Man, macros are fun. Anyway, that's, like, way better than what I would have done. So… The thing we should focus on is, do we have the right data?
In advice to make good reports.
That's, like, part one. And then part two is, does our default rendering of reports give you useful information? So, you know, the question I would have, that message that you have where you format it right there.
it is lower amount of investment initially for us to put it there. Does it make sense to have that formatting be in the, the ANSI template that we do by default for advice?
I'm curious if the answer to that is yes or no, because that would actually imply a lot of things about Weaver. But overall, if you want to add more content to these advices, and, like, figure out what the right boundary is for us to give it to a reporting tool, what we want… what we don't want is to be in the business of changing our format and our structure based on anyone who comes in who doesn't like the way it looks, right? We want to make sure… The fact that you could get so far.
with, JQ and, Ginger, I think, is a good sign that we can, like, serve everyone with craziness if they want it.
**Liudmila Molkova** 18:49 That's exactly…
**Josh Suereth** 18:50 Yeah, the two things we should have is basically, is our out-of-the-box good enough? Which I think you're fixing. And the second is, do we have the right set of information? The only thing I would question here is that message format. We had it before, it's the default, Is there a reason… is there a reason we want it there, or should we move that out too?
that's the only question I have. Otherwise, adding more info here, I'm totally… like, please do. Like, let's get the right set of data. I still think violations from RegO policies are problematic, and really not well-suited for what we need. So, anything you do here where it's like, here's a better you know, set of data, I'm on board with personally.
**Liudmila Molkova** 19:33 Yeah, Jeremy, do you remember on top of your mind how we used this for the ANSI thing?
**Jeremy Blythe** 19:42 how we use…
**Liudmila Molkova** 19:45 like…
**Jeremy Blythe** 19:45 the message.
**Liudmila Molkova** 19:47 Right, because it's, it's essentially impossible to format anything around this, because, everything in… in this Structure depends on specific advice type.
Anyway, I can check.
**Jeremy Blythe** 20:05 I've gotten it, because I've been working on something as well.
Basically, what… What it does today is it prints out every sample as it comes in.
Scrolling, scrolling, scrolling, see if I've got one.
Yeah.
I'll put a little screenshot in the chat.
Unable to send files due to admin restrictions, okay.
**Liudmila Molkova** 20:53 I should… I'm sharing the… what we print today.
Okay, so it prints this.
**Jeremy Blythe** 21:03 So, yeah, so… Because it's… it's… it's in a context of the… So you've got the hierarchy, right? So you know that you're in a metric, that that's the metric, and then there's a data point in that.
And then these are the… those are the advice lines.
So you've got… you know the signal type, because you're… because of the hierarchy.
For example, and you know that… you know all of that.
So it's the current designers putting it, like, in place.
As the messages come in.
but not so great for a summary after the fact, which is what you're trying to achieve. So my… what I did for the sort of summary after the fact, so sort of aggregating things together, was that statistics object.
**Liudmila Molkova** 21:50 Right, but… I think this is problematic because we… If we want to make it customizable, we would want to have information in that device, right?
that people can query in JQ and build custom reports. They don't have to, but they could.
And… But probably what I… what I've done broke this nice little view, so I'll need to get back and make sure this nice little view can continue be… To, to, to be nice.
**Jeremy Blythe** 22:34 Okay, so then it's… the… Just like… just like everything in Weaver.
What you want to see.
is, like, there are so many different use cases for LiveCheck.
the… one of the use cases is, well, I want this… I want this summarization at the end. There's another use case, which is, I just want to see my… I want to see every message as it flows through.
I just want the stats, I just want this, I just want that, like… It feels very much like Weaver is.
unopinionated.
It's, like, fully flexible, so…
**Liudmila Molkova** 23:21 Let's try to keep it this way, and, it sounds like I need some job to do, to… preserve… what the good thing we had for this thing, but I still… Would like to push for better information inside the advice, that they don't need to walk up the hierarchy to understand which thing the advice belongs to.
It seems we… I only need a few more days to work on this, so let's not block the release on this.
**Jeremy Blythe** 24:03 Cool.
**Josh Suereth** 24:04 Yeah, I think we can release more often, by the way.
This is a thing that I've noticed with SemComp and this… and Weaver, is, Our willingness cadence is sort of very ad hoc right now, and I'm debating just making a calendar entry.
That will, on the OpenTelemetry calendar for us, and our group that says Release Weaver, Release SemConf, so that we remember.
Cause it's not, it's, it's, it's, it's, I think, omission, not, Or no, what is it? Like, it's not on purpose that we're not releasing frequently.
**Jeremy Blythe** 24:39 Speaking of release, the other thing that I did do is I updated to the new Cargo dist.
So when the release happens.
You'll be using the new… Not new library.
**Josh Suereth** 24:54 that… Okay, so I… that means I would like to cut the release today to make sure the release is not broken.
Last time we set up Cargo Dist.
We had to make 4 or 5 releases before we knew that the release worked.
Because it does a good bit of stuff. Related to that.
there is a new, requirement where we're going to be branch protecting tags and releases on GitHub and making them immutable. There's, like, a new feature in GitHub. So, if we, like… I just want to make everyone comfortable with it. If we try to cut version X, and that release fails.
Then we cut version X plus 1, or version X, you know, dot 1.
we don't try to delete and re-release version X. That is not a thing we're going to do. Like, just treat releases as immutable and move forward, and that it's okay to make a mistake. If people are like, what the hell happened to release X? Be like, I'm sorry, our release process got botched. We're gonna have to deal with that going forward. So… Anyway, I'll… Jeremy, if you're, if you're able to this week, what I might do is try to, try to cut a release sometime today. I'm not sure… It'll probably be around, in, like, 3 hours or so.
When I have some time.
I'll send out the PR.
try to get the release process kicked off, and we can, we can, run through debugging it together. How's that sound?
**Jeremy Blythe** 26:31 I can… yeah, I'll try my best.
**Josh Suereth** 26:33 If you're… if you're not available, that's fine, I just, like… I think I want to kick off the process today, so that we can debug it between tomorrow and Friday, and have something out this week.
**Jeremy Blythe** 26:46 Yeah, oh, I should be able to multitask a bit, I can't give it… 100%.
Oh, for that to…
**Josh Suereth** 26:53 Nope.
**Jeremy Blythe** 26:53 In and out.
**Josh Suereth** 26:54 The way the debugging works is you kick off the process, you wait an hour or two.
you look at whatever failures it has, you debug, you kick off the process, wait an hour or two. This isn't, like, active-active, this is just more, can you pay attention to things every hour or two?
**Jeremy Blythe** 27:10 Yeah, yeah.
**Josh Suereth** 27:13 Alright.
So… with that… To consider for next release… I need to cut, release, this week.
Include this next. Alright, let's talk about attribute groups.
Do you want… do you want to present again, Ludmela? Or I was gonna, What I wanted to do with this, like, the basic idea you have, I think I'm totally on board with.
The notion of having ref group and ref… Absolutely on board with, The notion that we have a visibility on attribute group, it does default to public?
**Liudmila Molkova** 28:01 It should default to internal.
**Josh Suereth** 28:04 To internal, okay.
Is this a required… this is required on V2, is that right?
**Liudmila Molkova** 28:11 It is required on V2, yes.
**Josh Suereth** 28:16 Okay.
We, we could…
**Liudmila Molkova** 28:18 not required, but I think we've been moving away from implicit things.
**Josh Suereth** 28:26 I'm totally fine requiring it and giving people a good error message if it doesn't exist. Alright, so let's talk about possibly contentious things in the PR.
That we need to discuss.
I was gonna… I was looking through this before, and there's one thing I want to call out that I want to make sure everyone's comfortable with, which is, right now.
visibility will go onto V1.
And the notion of including groups versus extending will go on to V1, and it's called out that it's only used, to convert V2 schema into V1 and in resolution.
I'm personally fine… I think someone could accidentally, or, you know, on purpose, put this into V1 schema, but I'm actually… I'm honestly fine with that, if we just don't document it, add it in there, use it for V2 things, if people use it in V1.
**Liudmila Molkova** 29:26 I can add errors, in case somebody uses this V1.
**Josh Suereth** 29:32 I… I guess what I'm saying is, I don't think you need to.
**Liudmila Molkova** 29:36 Okay.
**Josh Suereth** 29:37 Personally, but I wanted to run that by everyone.
Like, do we want to prevent… I think this is fine to add to V1 schema, not document it, only really document it and use it in V2, personally.
This is… But I want to run that away, folks. Yeah.
What are you thinking, Jeremy?
**Jeremy Blythe** 30:05 Was distracted.
**Liudmila Molkova** 30:09 So we have a couple of properties here that are used as the… way to sneak V2 things into resolved schema. They… nobody actually, is expected to use them with current schema.
And the question is, do we put any additional validation, and I think my proposal, and Josh's, seems to be fine with it, that we don't, we just don't document it, we're not going to evolve V1.
We're not going to block people from using this, it probably will not be valid, but we just don't put much effort into preventing people from using it on V1.
**Josh Suereth** 30:57 Yep.
**Jeremy Blythe** 30:58 Nope.
**Josh Suereth** 30:59 Okay.
**Jeremy Blythe** 31:00 Makes sense.
**Josh Suereth** 31:01 Oh, go ahead.
Okay, so the other thing, I guess, to talk through, would be kind of a Rust thing.
Right now, this is using a structured enum versus an enum with a structure in it.
that's, like, a coding-style thing. I was gonna… I wanted to run that by you, I wanted to run it by Laurent, too. Basically, this might be… this might be a me thing, I don't know, but, I found when working in Weaver.
That every time we have this, we wind up moving to… And Noom that has a structure inside it anyway, almost immediately later, and, like, the ergonomics is kind of awkward, sometimes, in Rust. So this is not a, like, complaint at all about the design, this is just a… should we have an enum that has a structure in it instead of the structured enum?
Again, not… not a big deal. I just wanted to ask that. That's the only other comment I saw when I was reading through this.
**Liudmila Molkova** 32:19 Do you have an example of what we want it to look like? Because I'm not sure I understand.
**Josh Suereth** 32:25 Yeah. So, if we look at, say, here… Okay, hold on. It'll be easier if I just show you… go into the Weaver code.
**Liudmila Molkova** 32:44 Yeah. So let's do this…
**Josh Suereth** 32:48 Why is it just OpenTelemetry? I don't know.
Attempted Weaver. Okay, so let's go crates.
Weaver-semcov… Source… If we look at the actual semconf thing, right, this is an example of a, an enum with a struct.
That represents that… that thing, right?
So, in here is an enum, where you have V1 and V2, and each thing is… there's a struct that actually represents The two options.
As opposed to, we could have had the enum have structure within it.
Right?
So, it's an enum with a single anonymous structure versus a structured enum.
If we contrast this with what you have over here… Where is it? Again, if we contrast it here, where's the… Share this tab… Basically, you'd have internal, and then in parentheses, you'd have an internal attribute struct, and a public attribute struct. An attribute group would have been a numb of internal, with, in parentheses, internal attribute group.
or public with parentheses, public attribute group. That's the only…
**Jeremy Blythe** 34:08 Are you saying you prefer the anonymous struct to the named struct?
**Josh Suereth** 34:13 I've found, and I don't know if this is just a me thing.
Or if it's overall in Weaver, but if you look at what we've done across Weaver, when we have these, they slowly move into the other one, and when I was working on the V2 schema, I wound up turning almost everything into a Noom with anonymous structures in it, instead of, vice versa.
again, it's a question I just wanted to have, like, this is fine to go as is, because that's a refactoring we can do without impacting any users at all. Like, it does not impact the design of what you've done. It's more a, an ergonomics rust thing that I was curious, like, which direction we were leaning towards here.
**Jeremy Blythe** 35:04 I think you're right that it ends up… these things end up becoming… structs… Mike.
Typed strokes, because you end up needing to use them for other purposes outside of the enum.
That's what I found. Like, oh, I just want that thing, now I can't use it anymore, because it's anonymous inside that thing.
**Josh Suereth** 35:23 Right, right. It's impossible for you to pass public groups.
without also having to deal with internal groups everywhere, because it's in the enum, and you have to deal with them all in one bundle, yeah.
**Jeremy Blythe** 35:35 That's the… that's the reason that I… I generally prefer the other way.
Okay. I think everything has its place, right? Normally.
I end up going this route for something that's way down the tree.
If it's the further up the tree it goes, then the more likelihood is you're gonna have to, like, take those out and make proper structs anyway.
That's what I've found.
**Josh Suereth** 36:00 Yep.
**Liudmila Molkova** 36:01 Oh, I'm happy to do this.
**Josh Suereth** 36:04 Cool.
What else do we… Was there anything that you had to do that was crazy in Resolver?
So…
**Liudmila Molkova** 36:15 I don't think so, but, there wasn't…
**Josh Suereth** 36:23 Yeah, I love that this worked, by the way.
**Liudmila Molkova** 36:29 It was too easy to believe, yeah.
**Josh Suereth** 36:32 the… the thing… the thing that I… I didn't have a chance… I'll do this in a code review later, was, I think you did some work on the visibility and provenance rules to make sure things are up to date.
I just want to make sure that we, when there's an intermediate group between A and B, that the provenance rules, Are also dropping that intermediate group.
In some fashion. We publish the registry at the end, yeah.
**Liudmila Molkova** 37:00 I believe they are. The interesting question is that we… okay, so maybe we should talk about this. There is a property we call source group.
And with internal groups, in V2.
It becomes irrelevant.
**Josh Suereth** 37:19 Yeah.
**Liudmila Molkova** 37:21 Oh, by the way, I have a… where I still need to work on this. So, with just the attributes, the provenance becomes… I don't know what to do with it at all.
**Josh Suereth** 37:34 I ran into this issue when I was designing the V2 Resolve schema.
of… I was trying to take the provenance and turn it into what we do with V2, and I wound up deleting so much, or just ignoring it. So I kind of… I personally just gave up, and just started writing the rest of the code there, but I actually think that, it might… I don't want to do this, but I'm worried with this attribute lineage and provenance that we do today, that… there's a big disconnect between V1 and V2 that we have to resolve.
I don't think… you know, like, we can basically ignore half of it, or we have to do some translation. I'll take a look at what you did, because I don't think this makes it any worse than it already is, and if you're ignoring things, I think that's… might be okay, or if, like, the attribute group disappears.
**Liudmila Molkova** 38:31 Since V2 is not launched.
**Josh Suereth** 38:34 And since the side that I'm working on is still having trouble with lineage.
I think you're probably fine as is with what you… whatever you did. I'll take a look.
Because I do think… When it comes to lineage in the Resolve schema, we wanna… we wanna only talk about the things that are public in the Resolve schema, right? So any… Any hidden attribute group disappears.
**Liudmila Molkova** 39:00 Right.
**Josh Suereth** 39:01 And the notion of what group owned raw attributes, it's actually the file that matters, not the group ID.
**Liudmila Molkova** 39:09 Right, yes, and actually, this is one of the changes that we use file name instead of the group ID, and maybe we should have the Not the source group, but the source file.
**Josh Suereth** 39:24 for attribute lineage. Yeah, I feel like what… And I think it's outside the scope of this PR specifically, because again, I'm… I will need to do this on the side that I was working on, of getting, like, that final output dump.
I think we're gonna have to go redesign lineage in Resolver, and try to come up with something where we might track V1 and V2 lineage simultaneously as we go, and then export V1 and export V2 Just because I think the design of V1 Lineage, when we broke apart groups and we changed everything, I just don't think it's gonna work.
for V2.
**Liudmila Molkova** 40:04 Right.
So, I can create a work item for us to rethink before we do, yeah.
**Josh Suereth** 40:12 Yeah, I think that makes sense. I also like that you added a bunch of debug statements for us.
Does… Yeah, I think we probably need more of these.
**Liudmila Molkova** 40:23 I…
**Josh Suereth** 40:24 It's working in here, yeah.
**Liudmila Molkova** 40:25 Maybe I'm not using the tooling right, but debugging Rust is not the most pleasant experience, and debug logs make it better.
**Jeremy Blythe** 40:36 I think we, before we added the logger?
It was almost impossible to put debug in.
And control the debug out.
So the… there was a ton of code written before we had, like, an actual logger as part of it.
missing.
**Josh Suereth** 40:57 the way… the way I write this is basically, I… I do real heavy unit testing on, like, just this function.
And I do very little end-to-end testing. The only reason I need the log debugger is when I have to write an integration test and something fell apart in my assumptions. I don't know if that helps or not, but… That's how I roll.
**Liudmila Molkova** 41:18 I struggle with printing things in debugger. Maybe I used the wrong debugger, but it shows me the address of the thing, and.
**Josh Suereth** 41:30 That, yeah, yeah, I hear ya.
Okay.
You're still… you're still stepping through code. I… I only do unit tests. That's, Maybe I'm mentioning my limitation here. I literally don't use, like, a GDB-type debugger that often.
Only in, like, really rare scenarios will I actually step through with a debugger.
**Liudmila Molkova** 41:55 I mean, I'm spoiled.
A lot of languages that… that make it a pleasure.
**Josh Suereth** 42:02 Where… where it works well.
**Liudmila Molkova** 42:04 Yeah.
**Josh Suereth** 42:06 Yeah. But the bug logging helps.
**Liudmila Molkova** 42:09 Quite a lot, especially if you're… Actually, people who try to use Weaver and they fail with something, it can at least tell them what's going on.
How far it goes.
**Josh Suereth** 42:28 Yeah. Is there anything in here you want to call out while we're going through it? While I get distracted on debug logging?
**Liudmila Molkova** 42:38 One thing that's probably worth mentioning, I've, checked with Trusk, on the overall design of the thing.
So, there is, there are two… things. First one, we kind of went through his feedback on the current state of things, so the current story with attribute groups, that we build attribute group, we extend it, we add stuff, and then we extend, they extend the thing, and it's kind of hard to work with semantic conventions as a result, because you don't know What you're extending.
And you don't see everything in one place. So one thing we've been thinking about is Limiting, the ability or just the usage of nested groups.
I've redesigned my prototype, I only have one nested group, And I can only achieve it if we have… if we will have span ref.
**Josh Suereth** 43:42 Yeah, like the notion of a template spin, or a… yeah.
**Liudmila Molkova** 43:46 Right, yeah. I think it's still additive.
So I think we… we can… I can finish cleaning this up, we can finish reviewing it, and then, I'll figure out how to use SpanRef. The interesting thing that, the SPAN is also a group, and since we're translating the span into the… Group V1, we can hack things around, but we will do it, and…
**Josh Suereth** 44:12 I, I, I, this, this makes a lot of sense to me.
I expected us to have to have template things like that, like reshareable templates, but think of it like, okay.
So, you can either have a span, which is internal.
Visibility, the way you did attribute group.
Or we call them, like, template attribute group for internal, template span for internal.
And those can get reused, or that's, like, the phrase we use to say that this is an internal thing that doesn't get exposed to the world, but I can, like, reference it.
And inherit from it.
**Liudmila Molkova** 44:48 I don't think we need internal spams yet.
We have public spend, and we also have a reference of a public span, which is.
**Josh Suereth** 44:57 Oh, refinement, I gotcha. When you say reference, that's what we called refinement before.
**Liudmila Molkova** 45:01 Yeah, the refinement, yes, yeah, thanks. Yeah, yeah, got it, got it, got it.
**Josh Suereth** 45:05 Yeah, okay, I absolutely agree, we should have a span refinement. How are you planning to do identity for that? I think that was the big thing we ran into before.
**Liudmila Molkova** 45:14 Yeah, I don't… I don't know yet.
**Josh Suereth** 45:19 Okay.
We did that whole big, big shenanigan with, like, what ID means, what span type means, that sort of thing. I think, having a span ref, or span… and I'll… I'll keep recalling it refinement, you can call it ref, it's fine.
we probably need to have a new ID for refinements in this new world. So, the original is the span type, which is the core, and then a refinement always has a new ID, and I think you can just call it ID.
**Liudmila Molkova** 45:47 Right, yeah, like the group ID, which is… meaning equation meaningless, yeah.
**Josh Suereth** 45:52 Yeah, and then we can refer to it, and I think for the SEMCOM feature, where we say, like, I want to generate, you know, SEMCOM markdown for this group.
effectively, we invent a namespacing prefix for the things that we have. So there'd be one for span refinements, there'd be one for spans, that sort of thing. So we can have, like, you know, spanref.id.
And span.type.
like the namespace you use when you have your Weaver markdown syntax.
**Liudmila Molkova** 46:24 I think that.
**Josh Suereth** 46:24 That could work.
**Liudmila Molkova** 46:26 Yeah.
**Josh Suereth** 46:27 Okay.
I'm just trying to figure out how this all hangs together when groups disappear. And the Weaver Markdown thing was another deal I was running into of, alright.
I move that off a group, what happens?
**Liudmila Molkova** 46:42 Yeah.
So, with attributes, we don't have this problem, because we will use… we don't have the snippets for namespaces, right?
And we don't need to.
**Josh Suereth** 46:54 Yep.
**Liudmila Molkova** 46:55 If we want to do snippets, though, we now have public attribute groups, so we can have an attribute group with an ID, and that's all fine, yeah.
Yeah.
We're… Can use one type metric name, and… These things as the… Snippet idea.
In Markdown. It's only the refinements that we will need… we need some… some new trick.
**Josh Suereth** 47:24 We… yes. For… I think the… the raw… The raw span, we probably need, too. So if you look at, Probably looking at it in Weaver is not the best. Let me… Where do I have this defined?
I'll just show you what I'm thinking about.
Come on.
There we go.
Where is that? You were so contagent… I think that this is readable.
And the parser's where it is.
Did I describe the syntax comments?
Yeah, I didn't describe… yeah, we have end sumconv versus startSumConv.
So, basically, we have semconf and then some random ID that we pass in, right?
And that is currently the group ID.
By thinking here, I'm gonna put this into… Alright.
Future reference in… G.
So, my current thinking here is we have, trace.
type.
would be what you'd write there. And when we generate groups, we'd, like, you know, synthesize it, but eventually, when we move this rendering and stuff, and we… start leveraging the Weaver v2 Senconf directory, I'd update that parser to understand what trace.means, what metric.
Name means?
We'd have, event.name, We can have entity.type.
Right? So, like, it would actually understand… this would be special case.
And I think we could have ashbygroup.id, and for a ref, we would have something like tracerref.id.
or metricref.id.
**Liudmila Molkova** 49:38 Should it be race or span? I think the span would be.
**Josh Suereth** 49:42 Oh, yeah, it should be banned, my bad, sorry.
We can also make it plural if you want, like spams, metrics, entities, but… That doesn't matter to me.
The key thing is, when we synthesize group IDs.
from V2 into V1, we would synthesize these IDs, For the group ID.
And then… This will be updated to that, and then if groups disappear in the future, we update the… you know, weaver hook for this Markdown generation.
To match the same thing.
Okay.
So as long as that sounds reasonable, I think attribute group fits in here perfectly. I think getting span ref and metric ref work… oh, and event ref. We need all of them, right?
**Liudmila Molkova** 50:35 Hmm.
**Josh Suereth** 50:36 We'd probably also… we probably need entity ref, etc.
Entity ref.
Yeah, so if this, if this works, I think this, this is our new nomenclature.
**Liudmila Molkova** 50:47 Further?
**Josh Suereth** 50:49 And I'm… I'm perfectly fine with that.
**Liudmila Molkova** 50:55 Yeah, that sounds great.
**Josh Suereth** 50:57 Yeah, the other thing, if Laurent were here, he would put, repo name.
dot. So you could also do this, right?
Where if you don't provide repo name.
It assumes the local one. But if you want to reference something from an upstream, you could.
**Liudmila Molkova** 51:18 Oh.
Is this necessary? The combination of…
**Josh Suereth** 51:25 I don't think so, but I… what I want to do is, if we define this for here.
I want to have a consistent naming, namespacing.
in Weaver, overall, So, if I'm trying to access a span from a repo.
What would I write? Repo.type?
**Liudmila Molkova** 51:50 spend.type should be unique, right? Regardless.
**Josh Suereth** 51:54 Yeah, so I make a new span wrap with a… ID… and I reference something from another repo, that's what we're thinking?
**Liudmila Molkova** 52:05 So you're given ID, and it should be unique among all span refs across all repos.
**Josh Suereth** 52:12 Can we enforce that, though, if we inherit?
I guess we can.
So you're saying if I inherit from a different repo, I cannot define an ID that was already in that first repo?
**Liudmila Molkova** 52:30 Right.
**Josh Suereth** 52:32 Okay.
**Liudmila Molkova** 52:34 Otherwise, I mean… it could be part of the ID.
It's not the prefix for this.
Pan, but it's the heart of… the ID, and the type, like, event name, it's globally unique, right, or a metric name, so you would never have them, the collisions.
**Josh Suereth** 53:00 Gotcha, because you can't have the event name conflict, but refinements can use the same event name. That's fair.
I… I'm a little bit more nervous with refinements of whether the idea itself is unique, but we can talk about that later.
**Liudmila Molkova** 53:14 But then you can put the repo name inside the ID, so it's PanRef, repo name, and then ID.
**Josh Suereth** 53:24 What I'm saying is Weaver would do that implicitly. So, like, implicitly, when you define a span ref for something, we are adding the repo ID on your behalf, and we're creating that namespace for you.
So instead of Weaver treating everything as global, and like, we actually provide the namespacing for you.
And then we provide a way for you to access the namespace. Like, this… this here of you calling span.type, you're not writing span.type as your type. We… Weaver is creating that construct for you to access spans.
Buy a raw string later.
**Liudmila Molkova** 54:02 Right.
Yeah, so when you write span ref, in the ref, you don't need repo name, right? Because the type is unique, anyway.
And.
**Josh Suereth** 54:12 If type is unique, then I don't need repo name.
Yeah, that's fair. That's fair.
**Liudmila Molkova** 54:18 And then the repo name is part of your ID. Either we ask you to do it explicitly, or we… we can do it implicitly for you.
**Josh Suereth** 54:27 Right, and we're not gonna allow a span ref on top of a other… a different ref.
**Liudmila Molkova** 54:34 Right. Oh, okay, interesting question. I hope not, I hope we can avoid this.
**Josh Suereth** 54:40 Yeah, yeah, okay. We can talk… I don't want to open that door unless we actually need it. Let's avoid it for now. But if we did need that, that's where this kind of comes in, of like, let's pretend, like, the namespace is, you know, A fully qualified name.
in Weaver would be repositoryName.
thing, whatever, whatever the model thing is, dot its ID.
And that ID for SPEN is a type… for SPEN is a type, for SPAN ref is the SPAN ref's ID, that sort of thing. This is a fully qualified name, right?
if you provide a piece of it, but contextually we understand what you meant, right, because I'm referring to something, we can… we can drop pieces of it.
and still succeed, but if you want to explicitly refer to something, you can always explicitly refer. This is… this is kind of the principle I have around naming in languages and things, of like, cool, there's a… there's a global namespace that we have of just raw strings that we can access. We need a global namespace because of this feature here.
But we provide this thing where, inside of Weaver, when the context… when we know the context, you don't have to use the full namespace. The full namespace exists on your behalf, for you to reference if you need, and you will have to in areas where we have no context, but You know, otherwise, we don't need it.
So that's… that's the model that I like. It just… it gets a little awkward. Like, this… this… I don't know if I like that.
But if we don't need it, let's ignore it for now, and just, you know, only allow A ref to be a span type.
And since types are unique, we don't even have to specify A repository, right?
**Liudmila Molkova** 56:39 Right. Cool.
**Josh Suereth** 56:43 Alright, I'm on board with that. I will, review the rest of your stuff. I think the only… questions I'll probably have are Rust-related things, From a design standpoint, I think I'm completely on board with what you did here.
Cool.
**Liudmila Molkova** 56:59 Awesome, thank you, and happy to address any Rust or not Rust questions or concerns.
**Josh Suereth** 57:07 Alright, I don't think we have any other topics, so with that, I think we're gonna call it. I'm gonna go try to cut the release, and I will see y'all next week.
**Liudmila Molkova** 57:16 Awesome. See you next week.
**Josh Suereth** 57:18 Alright, see ya.
