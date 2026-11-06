SIG: Java SIG
Date: 2026-11-05
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Trask Stalnaker (Microsoft Corporation)** 02:04 Hey, we'll get started in a minute or two.
We're currently running agenda lists, so please add anything you want to chat about today.
Alright, we have people, but we have no… Agenda.
In case… folks missed, previously with, V3 is… postponed until December now.
End of the year.
2026.
That would still be good.
**Jack Shirazi** 04:24 Why?
**Trask Stalnaker (Microsoft Corporation)** 04:26 The KubeCon, and I had to work on some other stuff, for a couple of weeks, and… those… a few… kind of tricky, semantic invention open questions that I need some more time to think about.
Alright, magically appearing… Agenda items.
declarative config… I mean, oh yes, yes, I remember this, jack said he… Is out today.
But yeah, anything in particular you wanted to… Raise or ask about?
**cleverchuk** 05:44 Yeah, just wanted to ask whether the… The last commented proposal, whether that's okay before I start?
So we add the URL and the username, but the username and the password will just be optional.
**Trask Stalnaker (Microsoft Corporation)** 06:16 Seems pretty basic.
to me… PR against exporter… Follow up, Yeah.
I mean… Might as well, I think… go ahead and… I would go ahead and open the PR, because that's how, more people will pay attention to it then.
**cleverchuk** 06:52 Okay.
**Trask Stalnaker (Microsoft Corporation)** 06:54 Kind of forces that discussion to happen, whether… It's gonna get accepted or rejected.
**cleverchuk** 07:02 Alright, sounds good, thanks.
**Trask Stalnaker (Microsoft Corporation)** 07:15 Oh, we'll… let's… Probably cancel next week.
For KubeCon, I… Assume Jack is… Gonna be there, I forget.
But, of course, pinging on… Slack.
If, in the Java channel, if there's anything… You want looked at in the meantime.
Well, I'm happy to give people back a lot of time.
**Bruno Baptista** 08:10 Alright. Sorry. Oh, Bruno. Hey, hey.
I've added a couple of things.
I think they are minor, but they are… they are giving me, some headaches.
So, the first one is that I found out that we had, some breaking changes on 167. Small things, but… Well, So, this first one is kind of a difference of interpretation of what should happen when the tracer is set to none.
So the exporter is set to none. So, on the last release.
when that happens, the tracer itself is a no-op, so no work is done, that's fine.
For efficiency.
However, this… Is a breaking change on the previous behavior, because… We were doing, context propagation.
And we had context that we could use on NDCs to log things.
So, I know that the… The metrics and logs are being disabled when the exporter is disabled, that's fine.
But for the tracer, there's two different outputs. So there's the exporter, and then these context propagation features.
So there's… there's a discussion on that PR, on how to handle it, and I think… There's a way to… to bring back the… The features that were removed, just so people be aware of it.
**Trask Stalnaker (Microsoft Corporation)** 10:04 Can you, so there's an open PR right now?
**Bruno Baptista** 10:08 Yes, I created a PR with a possible solution, but the discussion is happening on the… So, I left a link on the… on the notes, it's…
**Jack Shirazi** 10:18 He's added it to the last week's agenda, so if you.
**Bruno Baptista** 10:21 Oh, boy.
**Trask Stalnaker (Microsoft Corporation)** 10:22 Oh, sorry, okay. Thank you.
**Bruno Baptista** 10:25 Oh, let me move them.
**Trask Stalnaker (Microsoft Corporation)** 10:27 I got it.
**Bruno Baptista** 10:27 Okay.
Yeah, and then there's the resourcing,
**Trask Stalnaker (Microsoft Corporation)** 11:07 Yeah, so the problem… what's the pro… the problem is that we end up sticking no-op spans, invalid spans… I mean, that… that basically empty span into the context.
which then… breaks the, like, then downstream, you don't see that. I hate that.
That's… Yeah, and… It's a confusing… Thing that we have to watch out for in… Instrumentation is gen… in general.
**Bruno Baptista** 11:50 So there's quite a discussion that I had with Jack, and I think we have an easy enough solution.
There's a PR, as a prototype. If people want to look at it, it's done in the bottom, the link.
**Trask Stalnaker (Microsoft Corporation)** 12:30 Out the export part.
Okay.
So, we… Is it effectively the same as… Setting the trace, the sampler… So if… if the sampler's always off, In that case, We'd… Create the span… Is it sort of a no-op span? Still? But it… Propagates the context still.
Trace context?
**Bruno Baptista** 13:09 I think so, but, yeah, yeah, I think so.
**Trask Stalnaker (Microsoft Corporation)** 13:14 Thanks, Peter.
**Bruno Baptista** 13:15 But it's kind of a two-in-one, because it also disabled the exporter.
**Trask Stalnaker (Microsoft Corporation)** 13:26 And so, with now here… it… We create a span. Do we still get some performance benefit?
In terms of no-opping, like, set attributes and things like that on it, so that we're essentially only using it to carry The span context.
**Bruno Baptista** 13:51 No, that would require more work to… on the tracer to create some optimizations, knowing that things are not going to be exported.
**Trask Stalnaker (Microsoft Corporation)** 14:02 Okay, okay, that's fair.
**Lauri Tulmin** 14:05 Just curious, what's the use of creating a span if you're not going to export it?
**Bruno Baptista** 14:12 Because if you are on a chain of calls, you might be breaking the propagation to other services that might be being generating the spans.
**Trask Stalnaker (Microsoft Corporation)** 14:27 So, if you still want Your trace context propagation.
Downstream to… and, downstream to your remote service calls.
But by… oh, go ahead.
**Lauri Tulmin** 14:47 Does it mean that, then the instrumentation part… Somehow reacts to the tracer being a no-op.
like, maybe the instrumentation should be the one that Should change and cope with the new op tracer and continue propagating the context.
**Trask Stalnaker (Microsoft Corporation)** 15:09 I mean, there's certainly the… yeah, I mean, that's kind of what we do in the instrumentation repo, where we check Should… if we should start the span?
Even… That's so that we sort of avoid… putting… It into the context.
Although… What do we call… I don't know if we've connected that 2R should start… Check.
Because there's a… there's a, a new… it's still… oh, no, I think it's… stable, I forget, that is enabled on Tracer. Is that stable now? Jack Shirazi, maybe you remember if Tracer is enabled, is stable?
**Jack Shirazi** 16:01 I'm using it, but I think I'm using, like a reflective axis, not… a… an API.
Mmm.
But I'm definitely using it.
**Trask Stalnaker (Microsoft Corporation)** 16:17 Yeah.
Okay, it did, it made it into 161.
So, yeah. So, I mean, Bruno, like, this is… And if we're not doing this already in the instrumentation repo, we should… But this is sort of like an early check that instrumentation can do to then, from an optimization perspective, then not even Call start span.
**Bruno Baptista** 16:46 Yeah, yep.
**Jack Shirazi** 16:49 But… but that would… that would also… yeah, that would also stop propagation, context propagation, because… That… that would terminate the instrumentation before it does any context propagation.
**Trask Stalnaker (Microsoft Corporation)** 17:06 I guess it depends on how you write the instrumentation.
And I think I checked this recently in the instrumentation repo, where, because we have that should start.
And I think I checked that that was independent of the Trace context getting propagated.
like, because if we don't, I think we still call the context pro- like, in the HTTP client instrumentation.
Oh yeah, we have to, because we have often nested HTTP client instrumentations, and the lower one gets suppressed, the span gets suppressed.
But it's still… oh, I guess we've… add the headers up higher than, probably, so I'm not sure.
Okay.
**Peter Findeisen** 18:02 What is the mean… what is the meaning of Tracer not being enabled?
Does it mean that it will not create even trace IDs or span IDs?
**Jack Shirazi** 18:15 Yeah.
**Peter Findeisen** 18:21 Yeah, so that… that will break downstream services.
I don't think this is… usable.
**Jack Shirazi** 18:34 It's as if you don't put the instrumentation… if you didn't enable the instrumentation, you have the same effect, so… And you can do that. That's perfectly well supported, so it's… I don't think it's a problem.
**Trask Stalnaker (Microsoft Corporation)** 18:48 Peter, I think I remember Jack going through that, and… Some… and with… if… If it's not enabled.
Oh, but would it be the same problem… That Bruno ran into.
I thought with it's not enabled, because you don't have to call this.
It can, right, there's still an internal check.
If the instrumentation doesn't call this, you still should get… Let's see…
**Jack Shirazi** 19:28 I thought when it creates a span, it checks that first, and then it returns a no-op span if it's not enabled.
**Trask Stalnaker (Microsoft Corporation)** 19:37 Yeah, and so the question is, is that no-op span… is it a fully NOP span with no trace context? Because then… I think we end up in Bruno's problem.
**Lauri Tulmin** 19:55 I think you're looking for the class called Default Tracer.
**Trask Stalnaker (Microsoft Corporation)** 20:00 Thank you, Larry.
**Bruno Baptista** 20:03 Sorry, I think so, because when you… when you try to create a child span.
and you are in this context, there's no parent, there's nothing. They all look the same.
**Lauri Tulmin** 20:25 So basically, the problem is that if you have, like, this new op tracer, then the span it creates has, like, this invalid span context.
So even if you got something from remote, it will overwrite it.
**Trask Stalnaker (Microsoft Corporation)** 20:45 Yeah, and that's the problem Bruno ran into.
But I feel like the is enabled flag, because we support it dynamically changing, Oh, if it's not enabled… oh, it does, it calls the Noop Span Builder… Okay.
I don't know, I'm not probably gonna figure that, this out on the fly, and we don't have Jack, who would… Know the answer.
**Lauri Tulmin** 21:12 So, what would make sense here, like, Should, like, it somehow, like, not create a span and just return whatever the current span is?
**Bruno Baptista** 21:27 Well, the solution that we thought about was that Okay, let's… let's keep the… the… the disabled like it is.
And let's create another exporter option that is NOAP.
And when you set the export to none, like today, the tracer will be disabled, like today.
And if you set it to no op, it will just… create a no-op exporter, leaving the tracer enabled, so the legacy behavior.
**Lauri Tulmin** 22:07 Still, like, isn't it, like, still kind of broken, because it creates a span, but, But, like, the trace ID will propagate, but still it, like, the trace will be broken, because you will have, like, missing spans from it.
**Bruno Baptista** 22:23 That's fine.
We don't need to have spuns for all the hops in the chain.
But they will all share the Cintrace ID.
**Lauri Tulmin** 22:43 Yeah, I think this should be dumped on Jack.
**Jack Shirazi** 22:51 I'm… I have… I have the same, thing.
We have, in the dynamic control, we have, exporters that can be turned on and off.
They're not… it's not implemented yet in the conjure repo, but… We do it all the time, and that's… it's customers who want that. And you're right, Lauri, that you miss… in the waterfall that you get, you'll… you'll… you'll miss spans out, but… Customers… have…
**Trask Stalnaker (Microsoft Corporation)** 23:20 That's wild.
**Jack Shirazi** 23:20 that requirement, because there's occasions when they just want to turn off all of the instrumentation that's being generated.
And that's the quickest way to do it, without breaking the context propagation.
**Trask Stalnaker (Microsoft Corporation)** 23:36 That's what I thought that, jack had worked on… was… Having this, when the span, when it was disabled, that… it would… B as if it was never there, and the next span would parent.
Back up here, so that you wouldn't have a missing… Parents, ban ID.
But I'm not seeing it in the code, so I'm probably… misremembering stuff.
Bruno, you said there was one other thing with resources?
**Bruno Baptista** 24:21 Yeah, so we, recently added that the resource, the new resources based on entities.
And, I have not formalized what I think is… needs to change, but I found a breaking change on my code, so… I… I've… I've had to adopt it.
And it's kind of a pain, because, well, these two…
**Trask Stalnaker (Microsoft Corporation)** 24:48 Hmm…
**Bruno Baptista** 24:49 I need to fix those two in order to backport the 167, because it has a CV fix.
And this.
**Trask Stalnaker (Microsoft Corporation)** 24:58 I agree.
**Bruno Baptista** 24:58 It's going to be a pain all over the place.
**Trask Stalnaker (Microsoft Corporation)** 25:03 I think I know… I might know the problem. The schema URL change… And so the merging behavior…
**Bruno Baptista** 25:15 Yeah, it's different, yeah.
And I'm getting… So the problem that I'm seeing is that I'm getting warnings, that I'm, Unsettling from entity?
**Trask Stalnaker (Microsoft Corporation)** 25:30 Yes, we had this in the instrumentation repo, and I… Forget what we… Yes, so we… we released a patch Specifically, Related… to… If this is the problem… Yeah, and it was just a… it was a warning message that was annoying.
It didn't actually… wasn't… yeah, so… I guess we'll have to… what happened? Align it to the schemas? Yeah, so I think this… the SDK updated the schema.
Maybe. I forget what was sort of the… Oh, I think we had a thread, even, also about this in the Java channel.
Maybe I can find that.
**Bruno Baptista** 26:52 But the origin of this is in the SDK.
**Trask Stalnaker (Microsoft Corporation)** 26:56 Yeah, yeah.
Okay, here.
So, the problem was… I'll drop the, Slack link.
Yeah… So, in this PR, it… Before, it had no schema URL, the SDK had no schema URL, and that's why it didn't cause any problems.
And then it added the schema URL, To that, which then created those merge warnings.
Yeah, I mean, definitely it's a… I think it's a question for Jack as far as… I don't know if it's… really a breaking change, it's… Not so… it's… Not supposed to be, but that… Certainly didn't have a great Side effect.
**Bruno Baptista** 28:37 Yeah.
So, I'm still researching this. If I think it's… it needs some action, I'll create an issue.
**Trask Stalnaker (Microsoft Corporation)** 28:54 Cool.
**Bruno Baptista** 28:57 Yeah, that's it for me.
**Trask Stalnaker (Microsoft Corporation)** 29:01 Alright, anyone else have… oops, I didn't really need to… Anyone else want to sneak on the agenda here? Think of anything new?
Alright, then see you in 2 weeks!
**Jason Plumb (Splunk Inc.)** 29:28 I'll see you in less than 2 weeks, Trask.
**Trask Stalnaker (Microsoft Corporation)** 29:31 See you Sunday!
**Jason Plumb (Splunk Inc.)** 29:33 Yep.
Bye!
**Bruno Baptista** 29:36 Bye-bye.
