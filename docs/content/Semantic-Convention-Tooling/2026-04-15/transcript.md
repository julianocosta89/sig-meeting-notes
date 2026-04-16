SIG: Semantic Convention Tooling
Date: 2026-04-15
Duration: 61 minutes
Zoom Recording URL: https://zoom.us/rec/share/muWFR9mYk5uB-hFyTtgZ-jbQFwjnjssSCR4-nt7EK5rzKLovzvLXRvOZrReDbDWm.rM9N9OnqN8WIddNd
============================================================

## Zoom Recording Transcript

Fraggle Rock (ca-wat-brt3) 00:02:39 Hello. Hello.
ariannavespri 00:02:43 I love the Fraggle Rock reference.
Fraggle Rock (ca-wat-brt3) 00:02:45 Yeah, the whole… this whole floor, all the meeting rooms are named after Saturday morning cartoons.
ariannavespri 00:02:53 Okay.
Fraggle Rock (ca-wat-brt3) 00:02:56 So I think… I think last time we video chatted, I was in Jet… the Jetsons.
Laurent Querel 00:03:04 Hey everyone.
Fraggle Rock (ca-wat-brt3) 00:03:06 Hello.
ariannavespri 00:03:06 Hello, hello, Laurent.
Laurent Querel 00:03:08 Boom.
Fraggle Rock (ca-wat-brt3) 00:03:13 The other day, one of these assistants, I… I, like, whispered it in the Zoom chat to fuck off, and it actually did. So I wanna… I wanna see if it works again.
Liudmila Molkova 00:03:36 Oh, no.
Laurent Querel 00:03:36 Dude, what?
Tero…
ariannavespri 00:03:42 No.
Liudmila Molkova 00:03:55 There are two Bradens on the call.
Fraggle Rock (ca-wat-brt3) 00:03:58 Yeah, I'm… I'm… I'm doing an experiment.
With the… with the assistant.
I wanna see if it works with this one. I don't think so.
I was… I was in a different meeting, and I actually whispered it in the chat.
the words, fuck off, and it actually left. So I wanted to see if it worked again.
Laurent Querel 00:04:20 You want to all produce.
Yeah.
Fraggle Rock (ca-wat-brt3) 00:04:24 It does not look like it's gonna work this time.
Friday.
Laurent Querel 00:04:27 We have a special agent.
Do you have any topic today?
There is a Google Doc, if you're not aware.
That you can use to, to fill in the agenda.
Can cookie does the… the Duke… It's in the chat.
Liudmila Molkova 00:05:15 I think we have a bunch of pull requests, and even if it don't have a topic, I think we should review them.
Laurent Querel 00:05:24 You want to do that?
Liudmila Molkova 00:05:28 Okay?
Fraggle Rock (ca-wat-brt3) 00:05:29 I think I… I had mostly joined to talk about the Python PR that I saw from Ludmila this morning. Not that I think there's much to discuss, but I'm… I'm curious about it, because the… Some of what it's doing is related to what we're trying to do with, like, the collector unit test framework around it.
Now, in your case, it uses sub-process management instead of containers.
For us, we still feel that there's… there's a reason to use containers, namely that we don't want people to have to have Weaver installed as a binary on their system just to run tests in the collector.
So that was the main reason that we introduced it, but… I don't know if that's necessarily a concern for the use case you're targeting with Python.
Liudmila Molkova 00:06:26 So the main… so, okay, so we experimented with both. I did initially prototype with test containers, and Ricardo from Python6 prototyped with pOpen.
And with containers, There are tricks with volume mapping, accessing logs, it's all very difficult, but… Since then, Jeremy did a bunch of improvements on the Viva itself, so you don't need to deal with it, you can just get the report from the stop.
When calling stop and so on.
And it became less important. The main goal is to test it in CI, anyway.
So, okay, people don't have Weaver, but Weaver does not validate something that unit tests.
Don't validate. Well, in a good case, unit tests validate pretty much everything Weaver does, but we don't know the coverage of unit tests, so the Weaver test check is just that… Nice, optimization for a PR reviewer to know that it does not introduce something totally broken in terms of semantic conventions.
Fraggle Rock (ca-wat-brt3) 00:07:40 Makes sense. So that assuages that worry. For us, we want to actually have it.
As unit tests that anyone can run at any time on, like, a collector receiver to make sure that it's still valid against semantic conventions, so that we know if someone… like, if someone's locally introducing a change.
That.
screws with the metrics that host metrics receiver is producing, for example, and it violates something, you know. I mean, presumably a pre-commit hook that blocks it first would be nicest, but I think people don't really do that, but at least it would be blocked in… in the tests in CI.
Liudmila Molkova 00:08:17 You can still, like, install it as a makefile or something.
Fraggle Rock (ca-wat-brt3) 00:08:21 Yeah, it's mostly that I don't, I don't want, To say, to run these tests locally, you have to install, versus the test container just kind of pulling it.
Right. Seemed like it was… more convenient.
Liudmila Molkova 00:08:37 I think it doesn't matter, right? Who cares?
Yeah. Test container, or IPopen.
Fraggle Rock (ca-wat-brt3) 00:08:46 Yep, either way is fine, really.
But the… the stuff that you mentioned in your… in your thread for… Next steps are all relevant to us, whether we interact through a test container or 3POpen. I think we're interested in all of that.
Because it would, it would benefit our work some.
Liudmila Molkova 00:09:06 What are your top… Things that you… you miss.
Fraggle Rock (ca-wat-brt3) 00:09:11 So I… the… the… email URL one is kind of a big one, because I am sort of just working under this assumption that eventually we'll be able to do that such that, like.
My long-term vision for a collector component is for, in its metadata, to say, this is the semantic conventions schema I am targeting, and… a PR could be bump that schema URL and see if our unit tests still pass.
And it doesn't look… I couldn't find a way for that to work right now. It seems like it's just tied to the version of Weaver that's used, rather than the schema URL. Unless I'm missing something. I could definitely be missing something.
Liudmila Molkova 00:09:54 totally ignore schema URL, but you can pass the registry that you want, and when you pass the registry, you pass the, essentially, the, let's say, a branch in GitHub.
Fraggle Rock (ca-wat-brt3) 00:10:05 Yeah.
That is… that might work for some components.
for host metrics, all of ours are gonna live in the same… in, like, the central schema that lives in Weaver anyway.
So, to have to go fetch the schema from somewhere else to be able to pass it in.
Liudmila Molkova 00:10:25 You don't need to. You just need to pass the URL. You can pass URL to semantic conventions tag.
And it will understand it.
You can'.
Fraggle Rock (ca-wat-brt3) 00:10:35 It'll clear that out.
Liudmila Molkova 00:10:37 Yeah.
Fraggle Rock (ca-wat-brt3) 00:10:38 Okay, okay.
So then maybe that part already works then, and I just didn't realize it.
Liudmila Molkova 00:10:45 I'm more like, I want to force every freaking instrumentation up until eventually decide schema URL.
This is where I'm coming from.
Fraggle Rock (ca-wat-brt3) 00:10:55 We are… we don't touch schema URL right now at all, which is something I would like to… push more components into doing. I'm… I'm sort of operating under this, like, if we get post-metrics receiver to do it right, other things can then follow our suit, rather than trying to, like, come up with one broad-reaching way to do it, but… That is the hope, is that host metrics receiver eventually becomes the, like, cream of the crop. This is the right way to handle the semantic conventions transition, and then hopefully other ones will just sort of fall like dominoes after we do it right the first time.
That's kind of the way I'm treating it, which is why I also want to get this unit test framework into the collector, and then post-metrics receiver when we have We're planning to do, like, a double write, so the ability to write the old schema and the new schema, and we're gonna have unit tests around the new schema to ensure that they're always correct against… Semantic conventions Registry.
So I'm… That's kind of a tangent for this group, but… That's something we're working towards.
ariannavespri 00:12:03 Then maybe another thing, if, if I remember correctly, the Lumina's PR is around the regular policies that maybe could be also interesting for us.
Liudmila Molkova 00:12:17 What? What exactly?
ariannavespri 00:12:19 Rego policies?
Liudmila Molkova 00:12:21 Oh, you can ride them today.
ariannavespri 00:12:23 Yeah, I mean, it's like, yeah, I mean, that's one of the things that, the extras that I think we are missing right now.
Yeah, sorry. I'm coming down with a cold, so…
Liudmila Molkova 00:12:38 I'm sorry.
Fraggle Rock (ca-wat-brt3) 00:12:39 Yep.
Liudmila Molkova 00:12:43 There we go policy, if you need them. It's… it's… So the one reason to have them Is unfortunately, if you want to… Check spans… But Collector does not emit many spells, and you probably don't hear about spuns, right?
Fraggle Rock (ca-wat-brt3) 00:13:01 We don't emit a lot of spans. We have, receivers and exporters that can process them, but the collector itself doesn't really… like, we have… we have… like, we have components that produce metrics, we don't exactly have any that produce spans. The collector self-telemetry is the main spot where spans are produced.
Those probably do still… need verification. Like, right now, the collector's self-telemetry… this is a separate topic, but it's kind of a mess right now, where we're still writing with underscores, and we don't have any of this semantic convention schema for The collector's self-telemetry at all, and we kind of need that, too.
Because now we're talking about, like, oh, we are naming everything everywhere with semantic conventions rules, except for the collector's own telemetry, which is still produced with underscores, and not following the rules at all.
And it's just because we don't want to break people, but that is another… That is another area, and those actually would need span verification, because we do have self-telemetry that produces spans.
Liudmila Molkova 00:14:09 Yeah, so for the span verification.
The problem is identifying span to validate against.
And for this, currently, the only option that somewhat works is custom rego policy.
We will need to solve it. I mean, I'm… I'm trying to make verification seat for… GenAI.
And it's so difficult without span identity.
ariannavespri 00:14:41 That was the other PR that you posted in the Slack thread.
the GenAI thing?
Liudmila Molkova 00:14:51 Y-yeah.
ariannavespri 00:14:53 Okay.
Liudmila Molkova 00:14:53 Yet.
Yeah, so maybe I'll share for Sakwas, Jeremy, and, Lauren. So, We have an interesting problem in Gen AI, where we have complex attributes.
And how we… How we, approached, Documenting them is through Jason's chemo.
So I actually have JSON schema here, and we have some freeform text saying that that attribute value should follow this JSON schema.
And everybody cringed. I cringed when I introduced it, but it's the easiest means to get things done. Well, turns out Rigo likes it.
So you can just match something against the schema.
And, this works pretty nicely. I, I think it should be, like, at some point, we will need to make the, whatever.
type definition, whatever it looks like in Weaver, this will be part of.
Rust code, because we know the attribute, we know the schema we should validate, it follows this type.
Laurent Querel 00:16:14 Nice.
Liudmila Molkova 00:16:17 But…
Jeremy Blythe 00:16:18 me. Huh?
You just reminded me of an issue.
But I forgot to put in here. So at the moment, if we're doing things with, custom policies for live check.
currently, what happens is if you provide REGO policies on the command line.
that replaces the internal OTEL policies that are in there, that are baked into Weaver. So the things like checking that the… Namespace collisions, and… I think. And, you know, that the… we're using the right… we're not using, like, camel case, we're using the right sort of thing, so that's a… That's been the beginning, but I just realized, I think, in the last meeting, or the one before, that it's… What it needs to do, I think, is to… I think we're gonna have to have another option, er, yet another option, but we have to have another option as to whether you want to replace the internals.
Or merge with the internals.
Liudmila Molkova 00:17:35 Wait, so the baked-in policies are for definition?
their life, they don't… Cute!
Jeremy Blythe 00:17:42 Oh, there's… there's some baked in for life track.
Liudmila Molkova 00:17:45 Oh, I see.
Jeremy Blythe 00:17:47 Yeah.
And I… and I think… Sometimes you want to override those, and, you know, write them again yourselves, probably.
So we need that option.
Liudmila Molkova 00:18:05 Right.
Jeremy Blythe 00:18:09 Which is annoying. I wish I'd… I just got it wrong the first time around, and I should have… followed what we've done for Czech with LifeCheck, and then it would have all made sense. But I don't think Czech has built-in Policies.
Liudmila Molkova 00:18:30 Mmm.
Jeremy Blythe 00:18:31 So this is this weird… it's this weird thing where… They're built in, but you may want to override them. We had… months and months ago, we had a whole conversation about how we were going to express a built-in?
with, like, You know, protocol thing, like built-in colon slash slash, and then the built-in that you want, maybe.
So, it may open all of that can of worms, but anyway, it needs to be noted. So, looks like you're doing that.
Liudmila Molkova 00:19:01 Yeah.
The other thing, I think it's related, we chatted with Josh, I think, mentioned it, That, when… Sorry, wrong one.
When we… What do we do here?
is… I need the access to those policies, and I can put them as JSON file in the repo, and… Like, next to the policy, and it should be discoverable through data, but we override data.
So then, I needed to hug… My way through, and it's actually generated, Yeah, this is this ugly, ugly piece of… thing that's generated with JSON policies, but I'm going to just leave a note there that, this is another probably related issue.
Jeremy Blythe 00:20:10 Yeah, okay.
Josh Suereth 00:20:14 For context, Jeremy, the built-in validation that's done for Weaver Check is actually part of the resolution engine, so it happens when you do live check anyway. There's no… there's no, like, built-ins beyond the stuff that the resolution engine does.
Right.
Jeremy Blythe 00:20:29 If you…
Josh Suereth 00:20:30 Yeah.
Jeremy Blythe 00:20:31 If, if in a minute, like, Lamila, if you, just… do Command-POTel.rego.
you'll see the file that's actually baked into Weaver.
Josh Suereth 00:20:49 Oh, that's the one you're talking about, gotcha, gotcha.
Jeremy Blythe 00:20:51 That's the one I'm talking about, yeah.
So you get that.
as standard, that's, like… I think you get.
But if you do… if you provide your own policies on the command line, It replaces that.
That's the current behavior.
So in the past, when I've wanted to add to it, I'm then copy-pasting out, and it's gross, right? So, there needs to be a nice way of going… I do or don't want that internal… Policy.
Liudmila Molkova 00:21:42 Now, what? I… I would like to… I thought I will drive the meeting, but, like, money cubo, no, it's working, interesting.
Cool! So then, for the live check, I've created an issue for schema URL. I think we will need to figure out how to work with it, but… It's all pretty cool, it's super useful. How we've been using it, we feed it to Claude, and it creates instrumentation until it follows semantic conventions.
Cool, should we move on? Florence, you wanted to do a demo?
Or I'm Biden, do you still want to talk about LifeCheck?
For Arianna?
Fraggle Rock (ca-wat-brt3) 00:22:31 I think we pretty much covered what I was interested in talking about.
ariannavespri 00:22:37 I agree.
Laurent Querel 00:22:40 Okay, so… Need to share my screen and present, So I think that will be, of interest for, Ariana, for sure, because you discussed about that.
and probably a few other folks.
We discussed about that last week, a mechanism, a way to… to integrate with our life check, basically, into, what we name OTAB Dataflow Engine.
Which is a set of libraries that are… Like a ROS version of a Go Collector.
So, let's share my screen and show you.
what we are… Oh, interesting.
Need to share.
I have a huge screen, so I need to share just part of my screen.
Okay, portion… how that works.
Hello?
That's not the potion kit they want.
So ish.
I should have tried to do that before.
Okay, later, do you see, this OTAB data from Gene?
with bitch.
ariannavespri 00:24:11 Yes, among other things, yes.
Jeremy Blythe 00:24:14 You can see your entire, like.
Laurent Querel 00:24:15 on screen.
Jeremy Blythe 00:24:16 Your desktop's really messed.
ariannavespri 00:24:18 Yeah.
Laurent Querel 00:24:18 Yeah, it is, it is. That's strange, because the… let me try again.
ariannavespri 00:24:25 I was just thinking that it's kind of comforting to see that I'm not the only one with a very crowded desktop with screenshots and stuff like that, like…
Fraggle Rock (ca-wat-brt3) 00:24:35 I only fixed that by removing every icon from my desktop entirely.
Laurent Querel 00:24:38 And now it is better.
Liudmila Molkova 00:24:41 Yeah, but it's a Mac problem, screenshots.
Laurent Querel 00:24:44 Yeah, yes, exactly.
Josh Suereth 00:24:47 Please never look at my home directory, is what I'd say.
Laurent Querel 00:24:51 So, let me give you the context.
So, we have a project inside OpenTelemetry, which is named Hotel Aron.
Started with, the creation of, an alternative protocol for OTLP named OTAP, Which is based on… Apache RO, so a columnar representation, and the protocol defined a mapping between open telemetry, Object Model.
So for the matrix, traces, logs.
Profile, we don't support it right now.
And, so a mapping between those, objects to, a columnar representation.
So that's the purpose of the hotel project, and there is a sub-project inside this project, which is named OTAB Dataflow Engine, which is a set of Rust libraries Which are basically implementing a new generation of collector.
We will retrieve a concept of receiver, processors, exporters, but there are additional concepts And and slightly different, design decision there.
With the purpose at the end of having something that is much faster, consuming less memory.
N, and more of this.
in this context now, what I did is, trying to integrate Weaver as a processor inside this system.
So here we have a configuration.
So it's a configuration that, for this system, for this engine.
It's not exactly similar to what we have in the GoCollector, there are some, Correspondences, obviously, but, so we have here a pipe… a pipeline.
don't, so the name of this apartment is man, it could mean anything.
And we have, here, a set of nodes, which are receiver, processor, exporters.
And really, we can build a DAG. It's more… let's say, complete then in the Go Collector, the type of deck that you can create, or, Broader and more comp… more complex, potentially.
So here we have the first use of Weaver that we… we integrated into this project day one.
So now a long time ago, let's say, one year.
Which is the traffic generator, which is the version of the emit command that we have in Weaver.
That take a semantic convention and generate a sensitive traffic?
that follow the semantic convention. So we have multiple variations around that.
The traffic generator can generate a static source with a pre-generation.
Or, and I will demonstrate that after, it could use directly a semantic convention as it is here.
Then, there is this new processor, which is really a proof of concept, definitively not production-ready, way too slow, but… Doing the… doing the job.
Working similarly, it's taking a semantic conventional registry.
And will generate, so it will behave in two ways.
Every telemetry arriving to this processor will be emitted To the default output, which is ear-name telemetry.
And we have, in this, bagan gene, data fluent gene.
Processors, can have multiple outputs, as opposed to the one that we have in, in the Go Collector, and they could be named.
So in that case, we, identify an output name filings.
And, internally, in this processor.
When we… we basically duplicate the traffic, one will go directly to telemetry output.
And one will go to, the Weaver Life Check Library.
It notifies the findings, violations, They duplicate them, and every new event of that will be sent to a specific output NEMP findings.
And that could go wherever you want. That could go to something that will display on the screen, that could go to… Any, telemetry backend that is already supported, this kind of stuff, or for further processing.
And in this case, we… we have… Two, export, one is named TelemetryNoop, just, something doing nothing, basically, but simulating a super-fast backend.
And this one, which will take every logs in that case, and will display, on the console the logs. So basically, it will display the findings.
Okay, so now let's run that and see what is happening.
So, I will first go… And show you what we saw in terms of configuration, but in a graphical representation.
So we have this, traffic generator named static, traffic.
So if you remember the, that's static traffic.
That's a receiver, that's why we see it here in this diagram. Life check.
Which is the… This one?
So the name that you have here matched perfectly the… the node ID into the configuration.
And we have the finding console and the telemetry loop.
So here, we generate, 3,000 messages per signal. 3,000 signal.
That are grouped per batch of, 1,000, signal.
So we see that… The live check, behave like a pass-through, Posses all?
And sometimes we have something that is generating. So it was too fast, we didn't see the initial phase, but because this traffic is static and always generating the same signal.
which is a combination of metric logs and span.
We… we duplicate very quickly.
And, we… we don't see any, additional traffic here, because, in fact, the findings have been identified and they duplicated.
If we… if we click on… on this node, we can see, several, printers that represent box… Yeah, attribute name scene, so, basically, I map a set of metrics That we can easily, infer from the LifeShake library.
In order to see what is happening, what we detected, and this kind of thing.
So now, let's go to the portal where the findings will be displayed.
So we… depending on, obviously, on what you are producing, we can have a lot of findings. But here we have, So the… so we have a way to represent, basically, batch of logs.
Which are, displayed this way. So we have a resource, from where it's coming.
And, and then we have the Weaver Leipcheck, that created log object?
And I mapped, when we have a violation, it's converted into a log error. When we have, Some findings, it's either a word or an info, this kind of stuff.
And I map, basically, the… the field that we have into the findings to attributes into this log, in order to do something with it. In that case, just display what we have.
Yeah, here we have an info.
Okay, and if now I… let's say I want to remove this one.
Enable the traffic generation based on semantic convention.
We can't… We should not see that. Oh, I forgot to say that.
Sorry.
Not familiar with Zed enough yet.
Okay, we saw here the few messages, which are basically the detection.
We should see here… Some findings, Yeah, findings information, improvement, few of them, violation.
And if we go to the console, we will see… those, warnings and errors. So, if I take one, for example.
RPC message and compress size. So, this one has been randomly selected among the, the list of, metrics, logs, and span identified into semantic convention. Then we take the definition of this signal, we look at the attributes, the mandatory one, the optional one, we generate the… a representation of that, that will feed the batch, so nothing new here, it's basically… we are not using directly the weaver emits exactly for this one, but that's exactly the same idea.
And then, in this specific case, we use the Weaver Light Check, and we will detect exactly what we have here.
Which is the fact that this signal is not stable, and blah blah blah, with all the context.
It's an improvement, and so on.
Liudmila Molkova 00:36:34 I have to ask a stupid question. Can you return back to the previous… to the browser?
Laurent Querel 00:36:40 Yes.
Liudmila Molkova 00:36:42 Do you folks have dashboards as part of the collector of the arrow?
Laurent Querel 00:36:47 We have a… we have a debug, troubleshooting interface, which is this one, yes.
Liudmila Molkova 00:36:54 Nice.
But, oh, you've shown the logs, like, the findings in the charts.
Laurent Querel 00:37:02 Oh, yes, oh, that is automatic, we… we have a way to discover… oh, I did not mention that.
I'm using, can show you that.
That would be nice.
Thank you for that, for this question.
I didn't think about showing that, yes, so this file… is the… or the list of metrics I'm using for the… this, specific processor.
And we have a special macro, in that case, the metric set.
And everything is, is properly annotated. The, the, this, comment is useful. It, it will be… it will become into a semantic convention, like a brief.
We have the other unit and so on. So what we do, is we basically generate a semantic convention registry, expose it.
That will represent exactly what this specific system is able to emit in terms of semantic convention. And then the UI that you see here Is, able to interpret that.
And create the proper, Chart.
dynamically.
So, if there is a new processor tomorrow, that will be automatically done.
Liudmila Molkova 00:38:39 Nice.
Laurent Querel 00:38:41 Yeah, and this, diagram, for this, yes, this, network, the norm.
Is only inferred On the… the… the metric and the event.
There is no… no need to look at the configuration file. We are able to infer, because everything is implemented.
The channel, the nodes, and so on.
and we are able to re-infer the… dynamically, and that's why I didn't have to restart this UI, because there is a mechanism to, To look at the… To look at a specific port, and when this port is there, we discover what is beyond this port, and then we display, Dynamically the… the pipelines, because we can manage many pipelines all together. They can be linked together with topics and so on, and that would be represented here dynamically.
Liudmila Molkova 00:39:45 Nice, I have another… Question about the life check, so… We talked about it, I think, last week, and in the context of WASM, or making similar things in the collector. And the life check is not the processor, right? It's… it's everything. It's the whole pipeline.
Like, if we… do we have the modularity? Do we want to extract the processor part of the life check?
Somehow.
Laurent Querel 00:40:16 That's what I… so here, the life check is really, mapped as a processor.
I'm not sure I followed exactly what you wanted to say about the overall pipeline.
Liudmila Molkova 00:40:32 So last week, we talked about maybe making something similar in the collector itself, right, in the gold collector. Yeah. And then, there is a receiver, OTLP receiver part of LifeCheck. There is the actual processing part.
Laurent Querel 00:40:47 Oh…
Liudmila Molkova 00:40:48 There is the, findings that are sent to Exporter.
With whatever exporter.
Laurent Querel 00:40:54 Yes, yes, so I just used the… The part that was interesting for me from the live chat.
So, it's, it's basically, Where it is.
I think it's there.
Liudmila Molkova 00:41:11 No, because you use it as a library, you can just…
Laurent Querel 00:41:14 Yeah, yeah, because.
Liudmila Molkova 00:41:15 Take the API.
Laurent Querel 00:41:16 It's a Rust project, that's why I was able to do that very quickly.
Fraggle Rock (ca-wat-brt3) 00:41:22 If I remember ER correctly, that Josh posted, I think it was, a lot of the work was to make it so that just the stuff that… probably just the stuff that this is using is exposed as a WASM API that the processor can call into.
So I think that is… I think you're right that that's the big question, like, we need to be able to access just that part of it to make it feasible in the collector, and… I guess the… the WASM is probably the right way to do that for… for… the co-collector.
Laurent Querel 00:42:00 I think we need to figure out a way, maybe, with the… the Go Collector team, so we… Joshua is part of the… of these two projects, so that will be easier, but At least partially, if we could imagine to have… a WASM interface, For processors that are, at the minimum, are compatible between this engine and the GoCollector, that would be nice. We could… we could, Reuse the same components?
We definitely have challenges, because the way that, so why we created this system initially was because Technically, We… we are not representing, object… the… the signal with OTLP internally in this project. So that will mean that we have to convert on the fly the OTAT representation into a TLP object, which is basically what I'm doing here.
We have a very easy way to convert back and forth between these two representations.
So we could technically have… A WASM interface, or processor.
One for OTLP, which will be supported by this project, with the additional overhead of conversion.
And we could have… and we could have an OTAT processor which is only, able to run in this engine.
That could be an option.
And then, we could imagine that, this Weaver LifeCheck processor will be compatible in these two worlds, automatically. I think that's something that is always unable to, to imagine.
Right now, we don't integrate yet with them time inside this data flow, but that's one of the next, Major focus.
I don't feel that as a big deal for us, Because the WASM story for us is very well, well designed.
But, right now, it's not something we support.
Jeremy Blythe 00:44:21 The room, too.
Did you… what was the experience with, like.
the API in the live check crate.
Laurent Querel 00:44:30 Is that… Yeah, I'm going to… so the… For all the context of, a collector where we won't basically… that's my opinion. They are… No, in fact, let me backtrack.
I was initially thinking, for a processor of this material, where It will act as a pass-through processor for every, incoming traffic.
And then we'll have a second output, findings, where we will emit things.
This approach is fine, but it's definitely not very scalable.
Because of all the override we have, in the Weaver Life Check crate.
We, we have this, Let's say, layer of abstraction, the sample.
That, duplicate, basically, the entire traffic just for the purpose of being, abstract enough to support different types of entries. I think that's the goal.
that's not ideal in the context of a collector. Definitely not. At least with this approach.
Because you will, you will enforce, A lot of pressure.
For all the traffic, So then we could imagine, oh, we have downsampling or something like that.
And we just applied the life check on a certain part of the traffic.
That's an option. Another option is, let me show you that I think that should work.
Yeah, this one.
Okay… People… Yeah, I made some changes that make this thing not working correctly.
So, basically, We could imagine that, the traffic go across… use the standard, pipeline, and we have this concept of topic into this project.
A topic, is like a mini Kafka, internally into this engine.
Where you can subscribe to with a consumer group, to the topic.
and behave like a load balancing mechanism. The back fissure is enforced end-to-end.
And there is a broadcast, View of the same topic on which you can plug something that is super slow, for example.
And then it's like a ring buffer. This broadcast system is like a ring buffer.
And, whatever you plug on it.
the topic will adapt to the slowness of these components. So in that case, we will have a processor that just takes traffic as fast as he can.
We'll generate findings, but will not act as a pass-through processor.
And I think it's like you tap the system and you plug your detector. That's exactly what I was trying to achieve for today, but… Yesterday, I decided, okay, let's do that later. But I think that could be, without any modification of the Weaver light check, that could be the right way to go for now.
And, in the future, in my opinion, we need to rethink the, the life check.
Slightly differently for an integration into the collector to be much, faster than it is today.
Jeremy Blythe 00:48:43 Yeah, I agree.
Laurent Querel 00:48:43 And I didn't identify all the slowness here and there, but… This conversion layer is one example, but I'm sure there are probably also, In the way that we represent internally the resolved registry.
We probably have things here and there that are not necessarily, in terms of retrieval, super fast.
So that's, maybe another example.
Jeremy Blythe 00:49:17 That's very cool, though.
ariannavespri 00:49:19 That's super interesting. I've got, like, a naive question. So, because, you, you, you started with saying, OTAP, like, is like a new protocol, but it's way more than that, because here you presented, like, a whole ecosystem.
And, so I was, I was wondering, and this, like, just a general question, just because I'm curious, I don't know if you've already, like, surfaced this in any other SIGH meeting, because there are, for example, lots of hotel collector Sikh meetings. Sometimes I go there, and I've heard about other, like, other alternatives to OTLP, but they are, like, just the alternative to the protocol itself, so it's not like this whole, new, concepts, or, or, you know, additional con… con… for example, this stuff, I don't know if you've heard about it. Yeah, sure. And so, And so, how do you see, like, how… because I… one thing that I… that I always wonder is that when… whenever there is, like, the proposal of, like, a new protocol in open source, so what is the… how do you see, like, the future for this? Like, what is your… if… if you see, like, this eventually, I don't know, like, replacing OTLP altogether, or, like, they have to coexist, or… how… what is your vision?
Yeah. For the future.
Laurent Querel 00:50:44 So, so, short answer, I think they will, they will, coexist.
For different reasons. This engine is already able to process a TLP and a typing differently.
Receiver side and exporter side.
We are even able to… basically take the OTLP traffic, and depending on the nature of the processor you have in between.
We don't do the decoding.
So in some circumstances, we are… even able to remove the gRPC, decoding, uncoding entirely.
And we are not even trying to translate that into Whatab, in some circumstances.
But otherwise, it's transparent, the OTLP to OTAP is done internally, and if you have an OTLP exporter, then it's OTAP to OTLP done automatically.
So, in terms of protocol, I really think that we, for many reasons, we will have to support, multiple protocols.
But we have the, Mechanic bridges between the two that make that relatively smooth.
No… The question about, it's like a collector, yes, it's like a collector. We, we want… so the contract we had with the governance committee.
was… create a set of libraries that we can, at some point, maybe integrate into the GoCollector, or maybe integrate as Rice Collector.
So we, we are not yet… I mean, we are very close to have, again, this conversation with the governance committee and technical committee.
Because I think we made a lot of progress in many directions. I didn't show everything there, but we have more than that.
And it's true that it's, it's an entire, ecosystem.
we have a new language, we have many, many things in this system. We are trying, basically, to learn from what was working and not working.
From the existing, open to an image-free ecosystem.
Including the GoCollector, and trying to figure out how we can solve some of those problems.
So what you see with the traffic generator semantic convention base, what you see about the internal list segmentation, and how we can leverage it to create very nice UI, that's another example. And, and how to speed up the entire, telemetry processing.
Leveraging OTAP, that's another example.
Yeah, so it's a little bit too early to go, to print on that, because I… we… the commitment we had with the governance committee was, okay.
You have Captain Blanche to experiment that. We are part of open telemetry.
Once we… you have a full story, let's fully discuss about that, and and I think the discussion will end up with some conclusion.
which, I'm not able to… to predict right now. We'll see how that works.
ariannavespri 00:54:16 It's super exciting.
Laurent Querel 00:54:22 Okay.
The chairing, and, go back to the… But if you want to know more, you can go to the, Hotel Arrow Project part of Open Telemetry.
It's not very visible, because the main Realme is still talking about the Go implementation of the collector, but if you go in the REST subfolder, OTAP data flow, then you will end up into this, New World.
ariannavespri 00:54:58 Fantastic, thank you so much.
Josh Suereth 00:55:02 It's come a long way, Lauren, it looks really cool.
Laurent Querel 00:55:06 Yeah, I know that you are well aware of that.
Josh Suereth 00:55:09 Yeah. So, I do… we only have 5 minutes left. Can we talk about release planning?
Liudmila Molkova 00:55:16 Yep.
Josh Suereth 00:55:17 Yeah, I want to cut a release of Weaver soon, but I wanted to see what we want to get in.
So… I think, Jeremy has PR I want to get in, around auth, but I think I just approved that?
So, that one should be good. This is one I had a question on.
This is support for ARM64.
with glibc. I think that we need to do the thing where we, make a build of this. So, here, I'll show this.
All it's doing is just adding a new Linux GNU version for Arc64 instead of just the muscle version.
Where before we only did muscle.
I'm fine with this, but I think we need to run a test of the release pipeline.
So, I might ask Cloud to do that, and then see if it works, and then merge the PR.
merge this PR instead of the one Cloud makes, or whatever. But just curious if anyone has concerns with the number of distributions we're supporting.
Okay.
Right. Then, I wanted to do the quick tracker for V2.
To see if there's anything else in here we wanted to get done.
In the next release. There's a few things that we had open, One was deciding on namespacing. Actually, I looked at, Ariana's PR for docs, and we're still grouping everything by namespace.
In that doc, and we're using, like, JQ expressions to do it, and I'm just wondering if maybe we should make namespaces first class in some way.
So that's… that's open question one.
And I'll… since we don't have a lot of time, I'll… because we'll have to talk about this next week, probably, Input policies can be different between V1 and V2. Do we need an abstraction to allow policies to work both on V1 and V2, or are we just expecting to have, a complete divide and separation of policy? I'm thinking the latter, so I'd like to mark this closed, and this issue.
And then the third thing to talk about is, basically, we want to decide what public attributes are and how they work in the Weaver model. I think we're kind of there, at least enough for release, and we can evolve it as we go. Like, they exist, we use them, they're propagated, you can define them, you can do… We'll have to figure out live check for them, but they're there.
So, I'd like to mark that one complete as well. So I'm just kind of curious if there's any other V2 things we need that we want to get in this release.
Liudmila Molkova 00:58:12 There are some things we know that we will need, and that will be broken. I think… One of them is… Oh, there are two. So the first one, I think the most important one. I have a PR for it, but it's… it got broken, I will… sorry, not PR, the change. We, like… Today, we're saying that the schema version is, let's say.
2 for the resolve schema 2.0.
We need to allow… to make schemas tolerant to new versions. So if we read 2.1, While on this version of Weaver, we won't crash.
And break, if we see a known property.
And it's relatively easy to do, so we just need to add a bunch of Additional properties back in the… Unfortunately, in… In the rust?
types.
I found a trick that allows us to still stay strict, so we can see, okay, if there is… if the schema matches, then none of these property bags should have anything, if we know exactly the schema, if the schema is lower than other hours, or the current one.
We will fail if we see any unknown property in the bag.
But for the… but we should tolerate them.
we need to do this as early as possible for the obvious reasons. We cannot really bump version or add new fields until we do this.
Josh Suereth 00:59:50 Okay, that's forwards compatibility, right?
Liudmila Molkova 00:59:53 Yeah, for compatibility.
Josh Suereth 00:59:56 What's the other thing you wanted to do? I wanted to…
Liudmila Molkova 00:59:59 to find a better name for a resolved schema URI that we have in manifest, because that's the feedback from Jack, and it's weird that we have schema URI URL returning manifest, and then another property, just a terminology problem.
Josh Suereth 01:00:16 Okay.
Cool, I'm gonna… I'll make a comment here, we'll update the tracker. This one, absolutely. Do you think we'll be able to get that in? Like, I'd like to cut a release next week, I think. Do you think that's something we could get by next week? Or should we… Cut a release and add that later.
Liudmila Molkova 01:00:36 Yeah, I have a prototype of within the branch, it just became messy, I'll re-prompt, and we can do it, we can have it today, bro.
Josh Suereth 01:00:45 Okay, awesome.
Awesome. If there's any, if there's anything else that folks want, I did update, I know, I know we're over time, sorry. I did update the Weaver project, to consider for next release.
And, for next release. So there's a set of things that I think might… we might want to move over.
Yeah, anyway, I'd like to fill this out. If folks have anything, let's put on chat things that we want to make sure are, are needed for the next release, but I'd like to cut one, if not, like, Friday, like, sometime early next week, with a bunch of the stuff that's been going in. Because I think there's a lot of… a lot of good work we need to keep getting out. And I want to keep getting all the bug fixes through.
Cool.
That's it.
Liudmila Molkova 01:01:38 Thank you.
Josh Suereth 01:01:38 Brilliant.
ariannavespri 01:01:41 Thank you so much, bye, bye.
Laurent Querel 01:01:43 Thank you.
