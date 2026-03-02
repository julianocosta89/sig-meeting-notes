SIG: System Sem Conv Stability WG
Date: 2025-10-09
Duration: 31 minutes
Zoom Recording URL: https://zoom.us/rec/share/mcE3Li_OZ7P6s7sZfGxnJfV900U5AFIV59lWhgtNRlHbmikqg2JFw6ZJSrU0EG9c.qWezp9PLvFvxSrO8
============================================================

## Zoom Recording Transcript

**Pablo Baeyens** 00:24 Hey!
**Braydon Kains (Google)** 00:28 Hello.
**Pablo Baeyens** 00:30 LinkedIn tells me to congratulate you for 4 years at Google?
**Braydon Kains (Google)** 00:35 Oh, yeah, thank you.
**Pablo Baeyens** 02:08 By the way, we discussed your PR about partial success on…
The stability meeting on Monday?
**Braydon Kains (Google)** 02:18 Oh, yeah. Yeah, sorry I couldn't make it, my internet went out, like, right when I was supposed to join. I wanted.
**Pablo Baeyens** 02:23 No worries.
**Braydon Kains (Google)** 02:25 Oh.
**Pablo Baeyens** 02:25 So Josh and me left some comments, and Evan also had some thoughts, so feel free to reach out to him if you want.
**Braydon Kains (Google)** 02:34 Yeah, sure.
I haven't had time to… go through. It sounds like there's some…
deeper discussion than I was ready for. The thing I really wanted to handle is the fact that
we get partial success from our API. We don't actually know
what entries failed or why. We just need a way to report that and actually get the right number of dropped records. That's all I was thinking about when I did it.
**Pablo Baeyens** 03:01 So, be warned, the…
PR with the most comments ever in the collector was related to consumer error.
**Braydon Kains (Google)** 03:13 Ugh.
**Pablo Baeyens** 03:13 And had multiple parts. So, yeah, it's a thorny part of the codebase.
**Braydon Kains (Google)** 03:20 Well, it's… it's really killing us, so we gotta…
We gotta do something about it.
I've had a bunch of people saying, like, we're losing all of our data.
And it's not… it's not actually what's happening.
They're losing, like, one per rec… one per record, but their dropped… their dropped count is skyrocketing.
I forgot to open the agenda doc, I only had one thing.
to mention.
Because we can get started.
First with, Issue Christos mentioned… Is this the one…
About actually referencing SEMCOM from m.edgevin.
**Christos Markou** 05:21 Yeah, so we have this,
discussions there, the collector side. One…
One thing is the, discussion around stability levels, and if… how we should…
Define the rules for, defining stability levels in the collector.
And if we should have a requirement for
linking to some ad conventions after some specific stability level, let's say beta or whatever. And, the other part is to, find a way to…
like, reference.
from…
metrics that we define the collector to reference to some ad conventions, if existing. So, yeah, we… yeah, feel free to have a look there. I would love your…
Your inputs.
**Braydon Kains (Google)** 06:11 Yep.
**Pablo Baeyens** 06:22 Is the… PR… 13920…
Ready for having a first look, or do you want to… to do more work before?
**Christos Markou** 06:35 I think I would need to revisit it and verify some things, and I will mark it ready for review soon. I saw your comment, but I didn't manage to get back to it this week.
**Braydon Kains (Google)** 06:46 Okay. Yep.
**Christos Markou** 06:48 I will, make sure to ping you once I open it.
Probably a question for Josh, since we have you here.
What's your opinion about having metrics, stable metrics, let's say, defined only in the collector, and not in the semantic conventions? Because I think that's something that we are discussing within the collector,
Second, yeah, my, my, my, my thought is that
at least what I would expect is to have every… having most of them defined in
Semat conventions, especially those that are stable, because you cannot have guarantees that something will not change, and if you have it as stable in the collector, and then another project comes and wants to define it differently, and takes it to Semat conventions.
We might end up having something different in some other conventions, but the metric is already stable.
But, who was it? Yeah, Alex. Alex Botten, I think, mentioned that there might be cases that metrics will never be defined in somatic conventions for specific use case or whatever, but my question is, why not to define everything in semantic conventions or, yeah.
**Josh Suereth** 08:16 I mean…
Yeah, so, to Alex's point, that's a practical thing. We… if we try to force every metric definition in the world to go through semantic conventions, we're just gonna die under the weight of that, right? So, there will always be the case that there are metric definitions outside of semantic conventions.
The hard question here is whether or not everything in OpenTelemetry should be under semantic conventions.
Right now, if you read our specification.
It requires semantic conventions for stable instrumentation, or you are not allowed to change your metric at all.
So if you read the specification, and you're the collector, and you want to mark something as stable, you cannot make any changes to that metric, ever.
Buyspec.
**Christos Markou** 09:08 Okay.
**Josh Suereth** 09:09 Which is… like… an absolute no, right?
the semantic invention should give you the ability to change things and advertise that to users. That's the intent behind that part of the spec.
Personally, I think we can be nuanced here, because there are things in the collector
You could think of it one of two ways. Something in… something in contribrib that is, very, very nuanced and not in semantic conventions should be able to have stable metrics and move to stability.
Right?
and whether or not there's a semantic invention group that is working on stabilizing that. The important part of that specification goal is that once you mark something as stable, you have clear communication of changes, that you clearly understand if you've broken things.
Right? It's about stability for consumers.
So.
I'm personally okay if the collector marks things as stable that are unlikely to ever be in semantic conventions, as long as you have the same mechanics that we provide with Weaver to enforce stability, to define differences, to make sure you're not accidentally breaking things,
You know, to put things behind opt-in flags.
But, like, you have to abide by the stability conventions of metrics. And we can update the spec to account for this, but from what I understand, the way metadata YAML works right now, I don't think you have the
So, I would be uncomfortable today just saying, yes, like, go ahead.
And it took us a while to build out our stability, like, stuff. Like, we're still doing it, you know, as you know. But what I'd love to say is, cool, every collector component can have a little tiny, you know, YAML thing of, here's the set of metrics I have.
and that we have the same policies and guarantees on that, that Weaver enforces for Semcov in the collector, and you guys can just go ahead and run forward with things and mark stuff as stable. And it's fine.
Right? And… but we need to have two things, right? We need that enforcement of stability and communication of change.
And the second thing we need is some kind of a litmus test.
for when something needs to come into SEMCOM, and not a, oh, SemConv is hard to deal with, so yeah, of course this won't be in SEMCOMF.
Right? That is another failure scenario we need to avoid. Yes, SEMCOM's hard to deal with, because you're making a metric that's supposed to be usable across many, many, many systems, and that's way harder than making it usable in just a collector. If that's the reason we want to be different, that's not a good reason.
Right, so that's the… that's where we need that litmus test there. But, I do agree with Alex that the inevitability here is we need a capability for a collector-constrip component to define its own SEMCOF. We don't have that today, and we don't allow it today by spec.
**Christos Markou** 12:18 Okay.
So it seems there are things missing, right? With going with this approach, right?
**Josh Suereth** 12:31 I think if we… so, we've been talking about metadata, YAML, and Weaver working together in some fashion.
**Christos Markou** 12:38 Yeah, yep.
**Josh Suereth** 12:38 I really think we need to keep pushing on that. If we can get to the point where you have, where I can give you the SEMCOM compatibility policies.
To the collector, that is enforced on your metric definitions, and we share those between us.
And I think we can start lifting the spec and basically changing the rule to be that you have to have those policies enforced, and you have to be generating the diff that we are generating for telemetry schema. I don't know if you saw, but Ludmila has that completely automated now, so it's actually generated directly from the YAML.
So…
We will look at the previous version of our tag, and the current version of our tag, and we will automatically generate telemetry schema with the diffs that have been… happened.
**Christos Markou** 13:26 In semantic conventions. That is a completely automated thing.
**Josh Suereth** 13:31 We should be able to give that to you, we just have to, like, you're… you'd be the first to, use it, so… bleeding edge, and the fact that we will bleed and it'll hurt a little bit, but, like, that's… that's a thing that we'd love to have. If we get that all in place.
Then, yeah, you can totally define them in the collector.
**Christos Markou** 13:50 So, I have two questions based on this. Do you think we cannot proceed with, like.
Increasing stability level… changing stability levels right now for collector, metrics in Contrib, because there were questions, why to start… we had, like, a bunch of PRs starting with stability… defining stability level per metric, and we started with development.
Which is kind of safe right now. Do you think we are blocked, proceeding to alpha, beta, and so on until we have this, sort of, like, using Weaver and enforcing this, ruling?
**Josh Suereth** 14:31 If you, if you read the specification today.
If you mark something as stable with a metric, you can never change the metric definition.
**Christos Markou** 14:42 Okay.
**Josh Suereth** 14:43 So, you are not blocked from marking it as stable.
Just once you do, you're completely iced.
on that method. And I think… I actually think that's a problem. But it's, like, you could do that initially.
to get things stable, like, again, and not have it be a blocker. The Weaver solution unblocks this and gives us that communication channel we need to make sure users know when things change, and we have that safe rollout, right? And that's the ecosystem we're building out.
So, what you could do is, if you're willing to mark something stable that you will never change.
Go ahead.
And then we can come back behind this with the ecosystem to communicate changes.
**Christos Markou** 15:26 Okay, alright. So, the way I can see this working is that, we can suggest, for example, that, we can start defining… so, the problem that we have to solve from the collector side right now is to define these rules.
about changing stability levels, right? So, all the code donors that have components in Contrib, they can know, I want to move my metrics to, for example, from development to alpha right now, what I need to do. So, we don't have these rules right now. So, we can start with defining these rules.
Yeah, I'm not sure if we should allow, like, moving to stable. We don't have anything stable right now, right, in the collector, I guess, in contrary, at least.
**Pablo Baeyens** 16:15 Yeah, no, we don't.
**Christos Markou** 16:17 And.
**Josh Suereth** 16:18 I recommend, if you can, just reuse our rules, don't build your own.
Yeah.
**Christos Markou** 16:23 Yeah.
**Josh Suereth** 16:23 You know, like, like, I don't…
I don't think there's value in that.
Especially… you already have a metadata YAML file, you could just generate the Weaver file from it. Like, theoretically, these things should be the same…
mental model, or if you can't generate Weaver YAML from your metadata YAML, then I would argue your metadata YAML needs more sophistication. Because the, like.
Is your metadata YAML covering all aspects of OTLP?
Yes or no? I think it is, and so I think you should just be able to generate the Weaver YAML. And then this is, this is the,
the set of policies that we enforce, and I think you could literally just pull these in, as is. If you look at line 55, you'll see, like, the things that we're doing. Spans are interesting, because we have to actually change the protocol to fix span.
conformance, that… because we physically cannot check spans right now. That is a…
That's a fun thing that really hasn't been advertised enough in OTEL, but basically, it's impossible for you to know if you are breaking spans, because we don't track spans at a granularity where we can check.
That is, Luna's been working on that, so I think that'll get fixed relatively soon. But for metrics specifically, for resources or events, that's the set of rules that we enforce, and so that's the ones you want.
If you can generate Weaver YAML,
this… you can just use this file, straight up. You can actually use it from the SEMCOM repo.
when you do your, your, your policies, you can reference it. There's, like, a way to do that. So,
That would be my preference, so that as we evolve our…
rules around compatibility, the collector and the rest of OTEL are in sync, right?
**Christos Markou** 18:16 Okay, okay, I will try to incorporate this and move the discussions forward. And the second question is, for this group, since we are working on stability and we will try to, like, at some point, once we have
even one metrics table, to… will go to use it in the collector.
Are we blocked on this? On the same,
Aspect that we were discussing before.
in order to use a stable metric in the collector, which is already stable in SemConf, who will be… who will be allowed to do it, or… Yeah.
**Josh Suereth** 19:02 You're funny.
Yeah, I mean, we do want to get to a point where we can run, I'd love if we had a conformance test, where you would run the collector against
Weaver Live Check to make sure that the metrics line up with the definition from semantic conventions. So, you know the whole schema URL thing, where you define the version of the metric?
So basically, the theory would be, you would put the schema URL in the collector, metadata YAML would say which one to use.
And you could have an integration test that would run that component, fire the data via OTLP into Weaver LiveCheck. Weaver Live Check would find no issues.
And that would be a conformance test to make sure your metric actually is matching the definition.
That would be ideal, if we can set that up.
**Braydon Kains (Google)** 19:50 That was something I was messing with.
In my… prototype. I was having some trouble with the, like.
You know, how do you… how do you run…
Weaver, like, you probably need to run the Docker image and, like, how that all fits together, like, that orchestration part of it, I was having trouble coming up with a good way to do, but…
**Josh Suereth** 20:13 I can… I can help you with that if you want. I did all the Docker setup, so if it's bad, it's my fault, so I'm happy to help.
**Braydon Kains (Google)** 20:21 Yeah. Yeah, I'll let you know. I had to sort of push that task to the side recently, so I haven't gotten back to it.
**Josh Suereth** 20:28 you should be able to run that Docker image without any, like, special
permissions, you just have to open the port that it will be listed on OTLP for.
**Braydon Kains (Google)** 20:36 Yeah.
**Josh Suereth** 20:37 But you should be able to point at SEM versions by tag.
**Braydon Kains (Google)** 20:41 So, it should just be command line stuff. Yeah.
**Josh Suereth** 20:50 I can also talk to the tooling group, and see if maybe, like, so Jeremy, Blythe is the one who's been working on all the live check things. They actually use it at work now, apparently. At their work, I should say. I don't remember where he works.
I… he has a… he has an example of doing live check as part of, like, an integration test. Maybe I can ask him to help with a collector live check test for conformance, so we can get a template set up and go that way.
**Braydon Kains (Google)** 21:21 Yeah, I think… I think the… the biggest hurdle is, like.
when you run the Go test, you have to also, like, run the Docker binary at the same time, and the test has to know where it is, and, like, that… that wiring is a bit awkward.
**Josh Suereth** 21:37 So, do you know… do you have anything like test containers for Go? Is there test containers in Go?
**Braydon Kains (Google)** 21:42 Maybe…
**Roger Coll** 21:44 Hey, there is! Here you go.
**Josh Suereth** 21:47 I only know this because I know the guy who invented this technology or whatever, he's a public speaker at some of the Java conferences.
Yeah, there's a library that's supposed to make it dead simple to just run a container.
**Braydon Kains (Google)** 22:00 Oh, interesting.
**Josh Suereth** 22:01 Yeah. Oh, yeah, this would be nice.
Yeah, so, so I would recommend, like, try that out for.
**Braydon Kains (Google)** 22:06 I'll look into this.
**Josh Suereth** 22:08 If that doesn't work, or if that's hard to use, you know, let us know.
**Braydon Kains (Google)** 22:12 Yup.
**Josh Suereth** 22:13 Yeah.
**Braydon Kains (Google)** 22:13 I'll give it a try.
The… the second item on the agenda was this…
PR that won't hyperlink for some reason, which is about… adding a new Unix.kernel namespace.
I don't really like it, like… I…
The… the whole, like, kernel information thing… It's pretty universal, like…
Windows needs it, and any Unix-based operating system needs it, and it's generally the same information that you need to report.
and also, this makes Unix.kernel an entity, which I really don't think is right.
Because the entity should be…
the host, and then has all the os.whatever attributes on it, feels like it makes more sense to me.
So I… I kind of want to read… I… I want to see if anybody remembers…
why we can't… why, like, this breaks ECS somehow, and, like, why we can't just do what Pablo pitched in the initial…
Issue.
It's not… it's not clear to me why we can't.
**Pablo Baeyens** 23:33 I think there was some sort of problem with the fact that os.kernel was,
convention in ECS, and we… like, my original proposal is… Putting things that are…
within that… treating OS.kernel as a namespace instead of a… Yeah.
**Braydon Kains (Google)** 23:58 And that… that breaks ECS, but what's the… what's the relationship with ECS? Like, why can't we… do something…
different than what ECS did.
**Christos Markou** 24:09 I think that's not an issue anymore, but probably we can… Czech was,
Why there's a mod conventions group.
But I think this, restriction about not having a namespace, not using, a field that is defined in ECS as a namespace in, in Semcon, that's not an issue anymore, I think.
**Braydon Kains (Google)** 24:34 Okay.
That would be good, because, like, the… in issue number 66, which I'll also
Link in the agenda. But the… the issue this was addressing…
Why doesn't auto-hyperlink? I don't know, whatever, it worked now.
the initial comment basically has what I… what I would think would be… The… the best option.
Because it would work for… any Linux-based…
pretty much any, like, POSIX, Unix-based, and… in Windows. So…
**Pablo Baeyens** 25:30 I think we should… Check with the elastic forks.
Whether this is still a problem. Because this discussion is, like…
2 years old at this point.
**Braydon Kains (Google)** 25:44 Yeah.
**Pablo Baeyens** 25:45 Most of it.
**Braydon Kains (Google)** 25:48 So I'll just ask on… on this issue again. And does anybody…
Disagree on the idea of the kernel being an entity?
like, it could be, like, a… like, an OS has a kernel, like, entity relationship, but that… doesn't feel…
Right, it feels like the kernel information should just be attributes on… Whatever entity is representing
The machine, in general, or the operating system.
**Josh Suereth** 26:23 Is there code behind this, like a prototype that fills this…
**Pablo Baeyens** 26:33 I think I originally proposed this because we have a product in Datadog that sends these fields, and I wanted to have an equivalent in OpenTelemetry, so that people that…
that use the OpenTech one can also get this information.
**Josh Suereth** 26:52 Sorry, I dropped.
**Pablo Baeyens** 26:55 Okay, yeah, let me repeat that. So the… I think the reason why I originally opened this is because,
well, probably the data log agent reports this information, and I want it to have an equivalent in…
**Braydon Kains (Google)** 27:09 in the OpenTymmetry world.
**Pablo Baeyens** 27:11 So… There is. I don't think this part of the data look agent is particularly good.
**Braydon Kains (Google)** 27:16 But…
**Pablo Baeyens** 27:18 Yeah, like…
**Josh Suereth** 27:20 Well, no, I'm interested.
**Pablo Baeyens** 27:21 case.
**Josh Suereth** 27:22 Yeah, I understand the use case. I mean, for this specific PR, we're trying to avoid defining semantic conventions where there's not instrumentation that generates it.
Like, that's one of the… that is a failure scenario in semantic conventions, where we end up with, like, bloat, and, like, we're not sure if people use it, we're not sure, you know, how to do it, that sort of thing. So, this is an example where I think it's reasonable to say, hey,
is there a resource detector that detects a UNIX kernel as a thing? And what is it attached to? Like, what's a… what's a, you know.
show us in OpenTelemetry where this is done and how this is filled out. So I think that to answer, like, Braden's question about should Unix kernel be an entity, I think partly we need to see a prototype, or someone, you know, doing this, and that will help answer it. So, Pablo, like, if you… if this original issue was from something we were doing.
you know.
Are these attributes you want in resource? Are these descriptive attributes to another entity? Like, that might be a thing.
Yeah, I, I just… You know, understanding the use case and the demo will help us answer questions better.
**Pablo Baeyens** 28:30 Right, so for my use case.
**Braydon Kains (Google)** 28:32 These were just discussed.
**Pablo Baeyens** 28:33 Subscribing a particular host.
It was, I guess, disgrace.
**Braydon Kains (Google)** 28:38 Two attributes for a host entity.
**Josh Suereth** 28:47 Gotcha. Okay.
**Braydon Kains (Google)** 28:48 Let's see if I can find… the… what's in the OS…
Resource Detector, or the system resource detector, sorry, and it looks like it doesn't even…
It doesn't report kernel information at the moment.
I would think that could be useful.
information.
It's like, if someone's… Impacted by a particular…
CV in a kernel version or something, and you can get a read of all your VMs that are affected by a particular version or below a particular version. Like, that feels like a valid use case to me.
**Josh Suereth** 29:25 Yeah, but, so, okay, I do think the fact that it's an entity
has some interesting complications here. So, one thing, it might make sense as an entity.
I do want to see a prototype, but I also think this is where entity as a signal starts to come in.
So entity as a… I need to jump to another meeting, but I'll finish my rant real quick for you. Entity as a signal is phase two of the entity's work. This is like the configuration of your system. So this is like observing how things are configured and set up, and finding CBEs as an example, but that's where you have a relationship, right? So you would say, this host has this kernel.
And then I can search that graph database of my configuration. That absolutely makes sense for us to have an OTEL, except all the mechanics around generating and reporting that data is tied in resource, so you only get that data if a log exists, or a metric exists.
**Braydon Kains (Google)** 30:18 Hmm.
**Josh Suereth** 30:18 Or a, you know, and so, is it valuable independently? Yeah. But I actually think, like, kernel's a thing I would want to fire in an entity signal, but not in every single log.
or in every single metric. You see what I mean?
**Braydon Kains (Google)** 30:33 Yeah.
**Josh Suereth** 30:34 This is where, should this be in SEMCOM the way it looks? Probably.
Is it useful today? Is there something that generates it in a way that we desire? I don't think so yet. So, I'm more of a fan on these kinds of things of just holding.
temporarily, until we get, like, get things into a usable state. Like, we have… we have so many things we're trying to get done, like stabilizing collector components. I'd rather focus our efforts in PR reviews on that stuff, and then as we build out these other features, like reporting configuration of your system.
as a signal with relationships, cool, then those features can launch and go.
So Pablo, to your use case, I need to jump, but I'm, you know, I can follow up offline, and I'll read through the bug, but I'm curious if you were relying on, like, an event that is a, you know, here's the state of the operating system to get this information, or if you wanted it on every metric, every trace, every log.
**Pablo Baeyens** 31:32 I think the latter, but just because entities weren't a thing when I wrote that issue. I think entities is a better fit.
**Josh Suereth** 31:38 Well, it's… entities only barely exist, so yeah, it definitely didn't exist before. Yeah. Okay, cool.
**Pablo Baeyens** 31:45 Yeah.
**Josh Suereth** 31:45 Yep, awesome, thank you.
**Braydon Kains (Google)** 31:47 I gotta jump, too, so…
**Pablo Baeyens** 31:48 Do you…
**Braydon Kains (Google)** 31:49 See y'all.
**Pablo Baeyens** 31:49 Thank you.
