SIG: Semantic Conventions SIG
Date: 2026-11-16
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Josh Suereth (Google LLC) 00:02:43 Hey, late week.
Christophe Kamphaus 00:02:47 Hello?
Josh Suereth (Google LLC) 00:02:49 I ran to get coffee, and it looks like there's only 3 of us.
Christophe Kamphaus 00:02:54 I hope a few more will join.
Michele Mancioppi (Dash0 Inc.) 00:02:58 I was told that the hallway truck at the airport was wild.
Josh Suereth (Google LLC) 00:03:03 God.
That was insane.
Michele Mancioppi (Dash0 Inc.) 00:03:06 Okay.
Josh Suereth (Google LLC) 00:03:07 What?
Michele Mancioppi (Dash0 Inc.) 00:03:08 You missed here at KubeCon.
Josh Suereth (Google LLC) 00:03:10 Yeah, I know. It's all good.
I, hope that I can attend to all the ones going forward here, so… We'll see.
If it makes you feel better, I, my heat broke.
So it was quite an exciting week.
Michele Mancioppi (Dash0 Inc.) 00:03:33 It's, considering how flat was KubeCon overall.
Only 8,000 attendees, including 1,000 sponsors.
The, location of the venue, all the best.
The layout of the venue, not the best. The food? Not the best.
Then, at least you got some excitement out of it.
Good to know.
Josh Suereth (Google LLC) 00:03:59 Not the excitement I want, though.
Michele Mancioppi (Dash0 Inc.) 00:04:02 In our job, usual excitement is of the wrong kind.
Josh Suereth (Google LLC) 00:04:05 Yeah.
Interesting, because I was at… the last one I attended, I think, was Europe, and that was… that was pretty packed.
Michele Mancioppi (Dash0 Inc.) 00:04:15 Hey, we're in Amsterdam, right?
Josh Suereth (Google LLC) 00:04:18 Yeah.
Christophe Kamphaus 00:04:19 Yeah, it was really nice, that one.
Michele Mancioppi (Dash0 Inc.) 00:04:22 Amsterdam was good. It was, like, 14,000 attendees. It was very alive.
Now, let's see Barcelona. I expect it to be wild, and if not, then, the writing for Kuba is on the wall.
Josh Suereth (Google LLC) 00:04:41 Alright, should we try to get through some of the agenda?
I might move Trask down, if that's alright, Christophe?
Christophe Kamphaus 00:04:53 Yep, finalists meet.
Josh Suereth (Google LLC) 00:04:58 Do you want to go through your two issues here?
Christophe Kamphaus 00:05:01 Yes, so my… It's about the long-running spans.
And how we can model some as… events.
That one is just for context. The second one, I posted a comment where… I analyzed, I did some analysis, and And wrote about some options.
So, yeah, I thought that we could mark the spans.
Where we expect them to be long-running.
And son… A big question is, should we define Lifecycle events in a generic way.
Or should we define… Events for each span that we expect to be long-running.
And a very related question to that is… how much tooling do we want to be able to ensure these pan events have the right Attributes that match the span attributes.
That one would probably be easier with… Per span event types.
While for a generic hotel span event, we could still… You will see spam type, if it's defined.
Josh Suereth (Google LLC) 00:06:53 I'm just catching up on this. I think, just generally.
from my own prototyping of, like, trying to improve OTLP and, instrumentation, like, these are the right 3 events that you end up with, right? Like, I started, I progressed, I ended, I think the important bit with these three events, though, is you want to define, like.
who wins in the event that both events report the same data? That's actually the part of the data model that I, you know.
would want us to… to make sure we have. And then, for the spend type OTEP, I think you could… That gets into, can it show up in multiple, right? Like, to your question.
So… I kind of am of the opinion that, it should be included and started.
And mandatory and started, and then not be included in the others.
Michele Mancioppi (Dash0 Inc.) 00:07:49 I'm having really conflicting feelings in singles going down.
the HTrace span model.
Because this is what it looks like, right?
Christophe Kamphaus 00:08:04 I'm sorry, I… What were you talking about, CH trace?
Michele Mancioppi (Dash0 Inc.) 00:08:09 So, in, openTelemetry is a dapper descendant.
The span is a single piece of telemetry. It has a start time and an end time, and it could be that if the span is not ended and flashed.
First, before your process goes, you will never get information out of it. This moves, this is a way of defining spans in an asynchronous fashion.
You have the span, been, created, or started, and the span been ended, as to entirely disjointed piece of telemetry. But not entirely disjointed, but independent pieces of telemetry, which means that you end up in a situation where you will have information about the spam end started but not ended, or even the opposite.
You know when a span ends, but not when one starts.
The, the model that we're following is the upper model, and what I see on screen is the edge trace model, which is an event-based model for tracing.
The, this one is powerful, but, the back end's then back for forgiveness and mercy, because all of a sudden, you need, actually, to effectively Keep track of the spans in multiple asynchronous messages.
And I'm curious how we got here, to be honest.
Josh Suereth (Google LLC) 00:09:29 So… Yeah, I'll jump in a little bit.
the… yeah, I agree that, like, the current model we have in OTLP is better for backends, because everything is kind of consolidated. However, when you actually write instrumentation, like the way the SDKs are implemented, or, like, in eBPF instrumentation, right? These are the core events that you use to create that model.
So one way to think of it is we're actually creating a layer of tracing that can live somewhere between the, you know, raw instrumentation and OTLP, where I could actually have these events and get them out. And… for long-running operations like, CICD, right?
who stitches that together and makes the core tracing model? Like, I… we are effectively, with this, asking backends to start to support that. And I know that it's, like, complex, because that's what our SDKs do today.
Michele Mancioppi (Dash0 Inc.) 00:10:28 For example, you could achieve the same. So these models as events, meaning log records with event name, yes?
Yes.
sort of the same, by saying that, a span Does not have to have both.
Span ID, start time and end time set.
And then in that case, instead of modeling them as separate log records, there would be two copies of the same span with the same ID.
Which is less devilish to deal with in a backend situation, because effectively it becomes an absurd, yeah?
Josh Suereth (Google LLC) 00:11:04 Yeah, but what's the difference? So, so I hear what you're saying, and it actually has been a question that we've had internally about whether spans can be partial.
And you can actually, like, up certain information by writing the same span twice.
The difference, though, is the… do you know that you need to do that? Like, the nice thing about having span progress and span ended is it's very clear what you are allowed to upsert, what you are not allowed to upsert.
Right? And so…
Michele Mancioppi (Dash0 Inc.) 00:11:36 Absolutely nothing.
in this that I'm reading on screen is preventing me from adding additional attributes, the span.
By having the span ended carrying more things. Also, this doesn't tell me, if span ended carries less things, what am I supposed to do?
Josh Suereth (Google LLC) 00:11:57 Right. I think this needs to say that, is kind of what my first point was, is we need to define, like, what… what is the model for each of these attributes, and when do you append versus not?
Yeah, I… I can…
Michele Mancioppi (Dash0 Inc.) 00:12:11 And now…
Josh Suereth (Google LLC) 00:12:12 Yeah, what?
Michele Mancioppi (Dash0 Inc.) 00:12:13 And now, this OTEP is defining tracing information in a completely unrelated pipeline.
Because this goes over logs.
Josh Suereth (Google LLC) 00:12:23 Yes.
Christophe Kamphaus 00:12:24 Yeah, and the idea was that we could have a log processor in the collector that would transform them back into Spence.
Or it would be done in a backend.
Michele Mancioppi (Dash0 Inc.) 00:12:40 I mean… Probably a connector.
Josh Suereth (Google LLC) 00:12:44 The other alternative is we would have a delta tracing signal.
Where we would actually call these, like, we would have OTLP tracing and OTLP delta tracing, and this would be the delta version.
Where you get these events, but yeah.
Michele Mancioppi (Dash0 Inc.) 00:12:58 I would expect… I mean, one way would be to introduce, kind of, temporality on spans, just look at it differently.
And, because this is what we're talking about, right?
The dispensers we know them today are cumulative, it's a whole shebang, and we're defining delta here.
Josh Suereth (Google LLC) 00:13:16 Fair. But I… I… it's… it's not quite the same, because I think the, This is more… we're turning the protocol stateful, so it's more like a stateful I mean, tracing is somewhat stateful to begin with, but yeah, this is, like, the spans become stateful, not just the trace, yeah.
Michele Mancioppi (Dash0 Inc.) 00:13:35 Wow, that's why I say it's temporarily but different, right?
Josh Suereth (Google LLC) 00:13:38 Yeah.
Michele Mancioppi (Dash0 Inc.) 00:13:40 So, all in all, I am not… I… I like that they're going down this route.
My first reaction to seeing this as log events is… Surprised and confused in equal parts.
I really expected it to be partial spans.
Because then, we would have had all the machinery right in place.
This is less risky, because… I mean, no span pipeline is going to break because of some log events that nobody's looking at, so this is more backwards compatible.
But…
Christophe Kamphaus 00:14:25 There's a reason we wanted to go in this direction, is that… all the OTAPs stalled.
So, when nothing got forward, I mean.
Partial spans, or stuff like that.
So, we've wanted to go here, define some schema for Span events, and then see… Where we can go from there.
Michele Mancioppi (Dash0 Inc.) 00:14:52 I, it feels to me like the kind of thing that… Before we put… Any implementation out there, we would be… We have to have an exquisite level of prototyping, right?
Christophe Kamphaus 00:15:07 Yeah.
Michele Mancioppi (Dash0 Inc.) 00:15:08 It's a bit premature to actually have this in a PR, ready for review.
Josh Suereth (Google LLC) 00:15:13 We already have a prototype of this kind of thing, like, I build it.
So there's this LTLP MMAP thing where we can actually send these events and then reconstruct spans. Like, I don't think the prototype of being able to do event-based spans and turn it into OTLP is problematic. What do you want out of a prototype, Michele?
Michele Mancioppi (Dash0 Inc.) 00:15:34 I actually feel that, it's not… this is the… a kind of… Change so potentially large, in terms of implications?
that it feels it should be prototyped outside of OpenTentry proper. This is a matter of implementing it in backends.
Alright, so you won.
Josh Suereth (Google LLC) 00:15:53 I want to see a backend that supports ingesting these values, yeah.
Michele Mancioppi (Dash0 Inc.) 00:15:56 What does that stuff?
Josh Suereth (Google LLC) 00:15:57 Yep, cool.
Yes, sir.
Christophe Kamphaus 00:16:01 households, so…
Josh Suereth (Google LLC) 00:16:02 Good.
Christophe Kamphaus 00:16:02 a thought I had. What if we now define these events? They get into a release, and people start building on it.
Yeah.
Josh Suereth (Google LLC) 00:16:17 I think that's fair, but from an open telemetry standpoint, though, we don't have a backend, right? So what do you prototype in?
Oh.
Michele Mancioppi (Dash0 Inc.) 00:16:24 Zero, and something else.
Josh Suereth (Google LLC) 00:16:28 To prototype in Jaeger, I'd do what Christophe was suggesting of make a collector reconstitute these into spans and fire them at Jaeger, right?
So I might write, like, I might write the logs to one data store, and I might write the spans to a different one, and I might interact with them separately, for, like, a dumb prototype.
But I, you know… I guess, from my point of view here, Christophe, is, like, it might be… I know we have an OTEP and all this, I think it does make sense for us to start Showcasing more prototypes of this style… And then we… we should probably do a full, like, trade-off. So this… this particular issue here is a SEMCOM issue, not a, we're trying to build this outside of, like, a big design OTEP for,
Christophe Kamphaus 00:17:21 Yeah, and if we start using the OTAP namespace for it, it would require spec.
Michele Mancioppi (Dash0 Inc.) 00:17:27 Exactly. I mean, that is, like, the big surprise of… a lot of the surprise from this.
It comes from having this discussion in the Semantic Convention SIG, and not in the spec.
Josh Suereth (Google LLC) 00:17:40 Well, I think… I think the… so, the reason why is Christophe has an issue where he needs this as a solution in SemConf, and the spec doesn't have a good answer for it. So…
Christophe Kamphaus 00:17:52 And basically, there have been a lot of discussions in spec already. I did some analysis there, where I… Got all the history, it goes back several years.
Yeah.
Josh Suereth (Google LLC) 00:18:04 I do think… I do think, Christophe, that, like, we can try to, like, put a workaround in Semcov for what you want to do, but I think we should continue to push on the spec.
problems and concerns, right? Like, we… we should really try to drive, the OTEPs upstream, if we can, that are needed for this… this kind of a thing, because I… it'd be nice if we, as a community, made a decision Either we're going to make this be first class, which is what that OTEP around span lifecycle events does.
or… we're going to kind of work around the fact that OTEL doesn't support it first class and create this secondary ecosystem you have to engage with, which is what you're proposing. Which, again, it's something you can do.
Michele Mancioppi (Dash0 Inc.) 00:18:47 Oh, I would like to point out, from the point of the end user.
Nobody is going to understand that this is a second-class thing.
It comes from the Semantic Conventions of OpenTelemetry, with auto dot as a prefix, hello.
Does it get more official than this?
Christophe Kamphaus 00:19:08 Yeah, as a workaround, I thought of defining per… spend-type events, I guess there we wouldn't need the blessing of the, spec.
Michele Mancioppi (Dash0 Inc.) 00:19:19 If you call it CI.experimental.span, then sure, I would not have given you this feedback, right? Yeah. But it looks awfully official.
Christophe Kamphaus 00:19:29 I agree, for hotel.something.
Michele Mancioppi (Dash0 Inc.) 00:19:33 In the main Semantic Convention repo.
Otel dot? I mean, that's a perfect storm.
Christophe Kamphaus 00:19:40 Yeah, that's why I gave both options, and I… I think it is a topic worth discussing in, in the spec.
Michele Mancioppi (Dash0 Inc.) 00:19:50 Overall, I think it's a great idea, like, if we could get… a fallback event model for spans that actually works.
And I'm not saying that this is not gonna work. I'm just saying that if we could do something like that, it would be fixing probably the biggest flaw of the OpenTermetry tracing model.
Josh Suereth (Google LLC) 00:20:09 Yep.
Michele Mancioppi (Dash0 Inc.) 00:20:11 That would be great.
I do not know if this is the way, and definitely should not come in the semantic conventions, like this.
This is spec work.
Josh Suereth (Google LLC) 00:20:24 This here would be spec work. This is SemComp work, yeah.
But again, this is a workaround. I agree. I think… so, Christophe, let's take this to the meeting tomorrow, if you're cool with that.
Christophe Kamphaus 00:20:36 at what time is it again?
Josh Suereth (Google LLC) 00:20:38 It's the same time as this one.
Christophe Kamphaus 00:20:40 Okay, yeah, I think I can mix that one.
Josh Suereth (Google LLC) 00:20:43 Okay. If you can't, we can raise it on your behalf and have that discussion. I… again, with what I'm seeing here of what you're defining, this is actually 100% in line with what I would see in an OTEP around a span event model.
And, I think we just need to kind of make that model a little more rigorous about, like, what values are in here, what values are in here, when things upsert, when things merge, what things have to be the same, that kind of junk.
Michele Mancioppi (Dash0 Inc.) 00:21:13 What is the expected behavior? What is the supposed behavior of a backend when those things are not the same?
Josh Suereth (Google LLC) 00:21:20 Yeah. And if you need… if you need, like, a prototype around these lifecycle events and stitching together spans, you can grab, in my… in my repo, JSarette, on GitHub, you can grab OTLP-Map, or mmap.
That is a prototype implementation where there's a completely event-based protocol for metrics spans.
and logs, but logs are already events, that gets converted into OTLP later. So, you can use that if you want, yeah.
Michele Mancioppi (Dash0 Inc.) 00:21:47 Do you realize?
That this… for this to work reliably at scale, you are going to need the same two-tier architecture of time series aggregation and tail sampling.
Because you will need to set up a load balancing exporter, exporting on the partitioning probably on the auto span ID, in this case.
not trace, like everything else, and that should be part of the validations for the OTAP.
Christophe Kamphaus 00:22:20 Yeah, I've wrote a paragraph about sampling.
It is an issue if it needs to be consistent with tracing.
Michele Mancioppi (Dash0 Inc.) 00:22:28 It is not even sampling, just to be able to reconstruct it with a processor that is mentioned, then you need to funnel them into the same place. If you're having these pants come over something like Firehose, because you started doing them from Lambda, which in some cases would be a perfectly reasonable thing to do.
Then you need to make sure that in the indigestion pipeline on the other side of the fire hose, they end up in the same collector.
Christophe Kamphaus 00:22:54 Yeah, so all the started, progress, and the defense for the same span, that they end up in the same electron.
Josh Suereth (Google LLC) 00:23:01 If the collector's reconstructing the OTLP, yes. If someone downstream is collecting these, though, you just need to make sure the sampling decision's propagated, not necessarily the data.
Michele Mancioppi (Dash0 Inc.) 00:23:15 Yeah, but in reality, what you're describing is the same thing, Josh.
In the world of probabilistic sampling, where you just do modular arithmetics on trace ID, Fine, no problem.
For the sampling, it works the same as the construction.
And, for example, what you're talking about, the propagation of the decision, that doesn't exist in Otta right now, because the decision is centralized to a single collector.
Josh Suereth (Google LLC) 00:23:42 I agree, I don't think OTEL has great tail sampling support right now.
Michele Mancioppi (Dash0 Inc.) 00:23:46 I, I agree with you. And, to some.
Josh Suereth (Google LLC) 00:23:50 And, like, setting up tail sampling is really frickin' expensive right now.
Christophe Kamphaus 00:23:54 Especially if it needs to be for long-running spans.
Josh Suereth (Google LLC) 00:23:57 Yes.
Michele Mancioppi (Dash0 Inc.) 00:23:58 It requires a PhD that nobody has, and it's still easier than time series aggregation.
So, yes.
Josh Suereth (Google LLC) 00:24:07 Wow, alright. As one of the people who works on the metric stuff, I… anyway, we… I think, actually, the notion, like, tail sampling and, time series aggregation that is spatial are actually two of the most important things we need to be addressing in OTEL architecturally.
So, like, and I think that is… that's outside the scope of what you're doing here, Christophev. This exacerbates the problem, but it doesn't actually, in my opinion, make it worse.
Sorry, it doesn't… it doesn't change the fact that it's still a problem or the priority, that's what I meant.
Michele Mancioppi (Dash0 Inc.) 00:24:42 I do think… I do think it does make it worse, because now you start having…
Josh Suereth (Google LLC) 00:24:47 That's what I meant by exacerbate. It makes the current problem worse, but it doesn't change the priority of the problem.
Because I think the priority should still be rather high.
It's one of the most frequently asked for things that I hear about is tail sampling.
Michele Mancioppi (Dash0 Inc.) 00:25:02 But there are solutions for tail sampling, which are… In the world of pure auto-tail, they're not great, but they're workable. Now, this… but the tail sampling has always been exceedingly obtained.
As a mechanic, and there was… there were alternatives with probabilistic head sampling, where the complex… you could escape the complexity.
Entirely. This thing here, Doesn't give you that option anymore.
In any realistic deployment.
If you're having an event-based model for spans, you must have a way to reconcile them.
Josh Suereth (Google LLC) 00:25:38 You need a way to reconcile spins to convert them into things, sure.
But I don't… anyway, let's take this offline. I think we've exhausted this topic, we know we need to talk about it in the spec. I think for the purpose of SEMCOM, let's move on.
We spent, like, 30 minutes on it, so sorry I wasn't tracking time too well.
Yeah, I look forward to continued discussions there. You want to move on to the next one, Christophe?
Christophe Kamphaus 00:26:03 It's related to my last point.
I did an overview of the different collaboration options we had in the past few weeks, months.
And one of some, is an federated registry.
They reserved, no, they defined focus namespace on their side.
With a policy to exclude any other namespace.
My proposal is to… Reserve some namespaces in the core sumconf.
like, the ones that, are in OpenTelemetry for Gen AI client-side, a registry.
And then, the big question from a governance point of view is.
Would we have such a registry?
In some conv, in the core.
especially here in the README, it lists them.
Maybe we could have an unofficial one just in the RECO policy.
But if we start listing federated registries like that.
I guess it would need to be discussed in the governance committee, or…
Josh Suereth (Google LLC) 00:27:25 Yeah, this is a good thing for us to talk about. I can… I can actually ask… this is the one… so this one is… is easier. Anything that is still in the OpenTelemetry org, where we've decided to delegate ourselves, I think is… is clear. Like, that.
add this, we can make it clear who owns it, and we can have… I like that you added Rigo, and I'm going to assume that you also say, like, where the convention belongs when there's a problem.
Christophe Kamphaus 00:27:51 Yes.
Josh Suereth (Google LLC) 00:27:52 Yeah, oh yeah, beautiful, right? Define it there instead. This is awesome. That, so I think this, this is, to me, just a clear win, for these, and then for Client SemConv, we should add those as well here.
since client is moving out, and I think, Who else moved out? Networking, maybe?
Christophe Kamphaus 00:28:15 a mainframe.
Josh Suereth (Google LLC) 00:28:16 Mainframe, yeah.
So, so I think this is a clear win for all of us. This one here, I'll talk to the… I'll take this up with the GC. It's a great question, because this is, like, one of our open source partners, but not necessarily OTEL. And so, I think we've negotiated that with them, where, like, they own this and we own… everything else, and we don't want to conflict with what they're doing. So I think this is reasonable to do, but there's going to be a limit here of what is the criteria for when something shows up here versus when it doesn't, right?
Are you going to give it to vendors? Are you going to give it to, you know, others?
Yeah.
Michele Mancioppi (Dash0 Inc.) 00:28:53 Liudmila and I spoke to, actually, a couple of people from Focus at the survey today.
They, it was a very nice discussion.
It's, There is great interest on their side to make it work. They believe that this will make OpenTelemetry show up in use cases that are way beyond DevOps.
So… I think it's cool.
Josh Suereth (Google LLC) 00:29:19 Yeah.
Christophe Kamphaus 00:29:19 Nope.
Josh Suereth (Google LLC) 00:29:21 100%. And so I think there's… I guess what I'm saying is there's a… there's a line we have to draw. I don't think this is the line, but there's a line we need to draw for when… when you show up here, where I don't want it to be, any corporation gets to put their name here, and it becomes one of those hells of everybody wants their name in this list, right? That those groups are unscalable for us. But if it's, like, these are open source foundations that are part of, like, Linux Foundation or Apache or something like that, where we have some criteria, then I think it's fine, right?
Christophe Kamphaus 00:29:52 Agreed.
Michele Mancioppi (Dash0 Inc.) 00:29:53 the level of, effectively, external governance under the CNCF for the NAX Foundation.
I think that's fine. It should not be that every CNCF project gets to put their name on, because very often there's a one-to-one mapping between them and a company.
Josh Suereth (Google LLC) 00:30:10 Right, right. And, like, Kate's, for example, is not gonna show up here.
Because we already own Cates, and it's in the court.
So anyway, that would be my only feedback, is, like, let's actually add a litmus test for when you get added to this.
that is part of policy here. If you want to change your draft just to include the core Gen AI ones now, I think you can. And then for the focus one, yeah, you can have a separate PR where we define the, the policy that we'll use for adding names to this namespace from outside the hotel brand. Does that sound good?
Christophe Kamphaus 00:30:50 Sounds reasonable.
Josh Suereth (Google LLC) 00:30:52 Cool.
Alright, let me add this to my notes for, what we need to talk about in the GC meeting, and then, yeah.
Goodbye.
Liudmila Molkova 00:31:06 Sorry, I just joined.
We had a good chat with Focus people, at KubeCon.
And the, It's a good idea to have some… some criteria for things to land here, or some additional information, because, we discussed that they kind of want us to bless them, and the fact of us including them into semantic conventions.
Could be this blessing.
And by including them, we recognize some level of support and compatibility, some endorsement. So it's good to have a litmus test and maybe different criterias of, okay, this is ours, like Gen AI, and this is external, but we like it.
Christophe Kamphaus 00:31:59 Yeah.
I saw those ads as well. How can we show support for them?
without directly starting a full project under the OpenTelemetry organization.
Michele Mancioppi (Dash0 Inc.) 00:32:13 We have the same, with the, I never remember. Security, semantic Conventions? OS, something?
Josh Suereth (Google LLC) 00:32:24 itself, yeah.
Michele Mancioppi (Dash0 Inc.) 00:32:25 Okay, then, right?
Christophe Kamphaus 00:32:29 Yeah, if you open my, twists there… I had AI write up some analysis of Different organizations we are.
collaborating with?
Also, what's their governance?
structure is.
Michele Mancioppi (Dash0 Inc.) 00:32:50 Hmm.
Christophe Kamphaus 00:32:51 Yup.
And basically, what came out of it said, for both OCSF, and, Green Software Foundation, that… In core open telemetry, we would keep the neutral signals and attributes.
energy, for example, would be used by both green software Foundation and OCSF.
And that could go on… the Kubernetes container and process namespaces.
And for the rest, they would define additional signals In their federated repositories.
Michele Mancioppi (Dash0 Inc.) 00:33:40 By signal, do you mean, attribute groups.
Christophe Kamphaus 00:33:44 Yeah.
Josh Suereth (Google LLC) 00:33:48 So, for OCSF, I think we need to continue the discussion we were having with Stephanie, who I think is here now, but, I think that one's going to be a bit deeper, because there's, like, a compatibility layer, and then I think there's actually things that need… like, our core Semcov will probably have to support OCSF concepts for that translation to work, so I think that's going to be a bit of a deeper discussion.
Not just like a, hey, we give you a namespace and you can use this, and then you won't conflict with SemComp. This is more, we want operational telemetry to be shareable between the two standards. So, if we own the instrumentation in OTEL and are producing it, OCSF folks can consume the data Exactly. Similarly, like, with Focus, where their namespace is a, like, layer on top of what we do, that makes sense. For OCSF, it might be the same, but from the, the initial proposals I was seeing, I think this is gonna be a bit different and a bit deeper.
Michele Mancioppi (Dash0 Inc.) 00:34:46 I mean, in focus also, it's not just a bag of attributes. For example, the first proposal I've seen, they effectively created their own version of cloud.resource.ed.
So there is overlap there as well. It's not so orthogonal the way you make it sound.
Josh Suereth (Google LLC) 00:35:04 Yeah.
So… These seem… Thanks for putting this together, by the way, Christophe. This is, this is nice.
Does this… this looks about sustainability. Does this look into the overlap we have between things, where…
Christophe Kamphaus 00:35:20 Yes, I think parts of it, it, it, goes into that.
Josh Suereth (Google LLC) 00:35:28 Okay.
Christophe Kamphaus 00:35:29 I prompted the AI to, analyze the relationship between, both organizations, also, and, theirs.
What was discussed, previous work, And, how we can collaborate.
So it… It also came back with some options and a recommendation at the end.
Josh Suereth (Google LLC) 00:36:00 These… these are also, I think, important, by the way.
these common threads, like the… like, this is the principles that we use to make decisions. To me, this is the most important thing for us to get out of your gist here, right? Like, this is… OTEL owns neutral facts and building blocks, and then the outside group can build on top. That would… like, color how we work with other groups and other teams. Upstream first, yeah.
Michele Mancioppi (Dash0 Inc.) 00:36:33 I don't think that a formal Well, no, okay, it's project, not SIG. Okay.
Josh Suereth (Google LLC) 00:36:40 Yeah, is the route to official status.
The thing… the thing that I want to see here, because again, the Semantic Conventions is useless by itself.
Why Semantic Conventions is powerful is because we have instrumentation that produces it.
And that is the true thing we have to, like, consider, is, like, users don't… Like, they want observability, and what observability means is instrumentation. So, the thing that produces the signal is the thing that we need to care about. And so, where… What we've done for the OTEL ecosystem is we've tried to, you know, create these groups of experts that say, here's what you should produce, and then all the different languages fall in line and just produce that set of signals, so you have consistency.
When we meet with these other teams, to me, the foundational thing we have to be asking, and how I would phrase some of this stuff here, Christophe, is where does the instrumentation live? If that group is providing the instrumentation.
then they are the source of truth, right? But if they need our instrumentation to produce the values, they have to work through our core and have that deeper integration. And this is my expectation with OCSF, is that we need to actually work with them on the instrumentation itself. Stephanie, have your hand raised, great. Go ahead.
Stephanie B 00:38:00 Hi guys, just joined in at, I think after 11.30, I have an 11 o'clock, conflict, but, so… I haven't looked at this document that, that you're showing now on your screen. Is this in a shared location somewhere?
Christophe Kamphaus 00:38:16 I put it in the Meeting Notes.
Stephanie B 00:38:19 I mean, okay.
Because I think, Josh, you can correct me if I'm wrong, but it looks like this is kind of similar to some of the things I had brought up about a month ago, like with some of the, How we could integrate, both. And, I think there needs, just to kind of piggyback on what you were saying, just some additional follow-on discussions and What would be the best place to, to really… continuously talk about how this… how would this emerge. You know, we're gonna do it based off of the you know, with OTEL being the, instrumentation piece, like, for that, like, that is prototype example that, you provided, like, a couple months ago with, merging in, like, the, OTF stuff within OTEL or not, but just, the way to move forward to be able to start, pro… continue to prototype some of this stuff out. I don't know if this would be the meeting for it.
I… I do have an open… I know you said, adding another weekly meeting might be a lot, but… maybe… This meeting, or the second half of this meeting, or something where we can continuously, have weekly discussions to push it forward.
Michele Mancioppi (Dash0 Inc.) 00:39:42 I would say that, given that the discussions are going into directions that Semantic Conventions are useful only insofar there are implementations for them.
This is quickly turning in my head to be a SIG.
To be honest. There is actually, in the world of AI, there is an interesting effect, and it is semantic that are not implemented are not useless, they're a liability, because AI is trained on OpenTentry.io, takes it in great importance, then goes and looks for stuff that doesn't exist.
So we need to be extra careful in this day and age to actually saying that the standard is actually live implementations for this to be ratified.
Which sounds like a SIG twin.
Josh Suereth (Google LLC) 00:40:35 We are a SIG.
Michele Mancioppi (Dash0 Inc.) 00:40:38 And I'm a dedicated SIG shop.
Unless…
Josh Suereth (Google LLC) 00:40:43 You mean a dedicated SIG around OCSF?
Michele Mancioppi (Dash0 Inc.) 00:40:47 Yeah, I'm thinking that.
Josh Suereth (Google LLC) 00:40:48 Okay, yeah, yeah, go ahead.
Stephanie B 00:40:49 The CSF hotel collaboration type. That's what I… I'm kind of thinking, like, specifically with how we would just go with, Conversion the two together.
That's what I'm thinking, but I don't know if that's…
Josh Suereth (Google LLC) 00:41:04 Yeah, I'm on the same page, but here's what I'll say, is I think we need to put together a project proposal for OCSF and some kind of integration.
I… I might be wrong, but I think, like, Stephanie, with the ideas you brought here, we're still in a brainstorming phase.
And so, the problem we have right now with OpenTelemetry and our, like, SIGs and stuff, SIGs are supposed to be dedicated projects where you know exactly what you're building, what your end state is, and you're executing against that. They're supposed to have a timeline and a deliverable at the end of the timeline, and you bring a project proposal, we make sure it has people who are contributing to various pieces.
And that's what a project proposal is, or a SIG, right? So… I think we're a little early on that, and we still need a dedicated spot to do some of this brainstorming and these discussions.
Which is why I'm thinking we should set up a time with interested individuals to meet, and we can reuse some, you know, CNCF resources to have Zoom calls and that kind of stuff.
But we should probably have a dedicated group to brainstorm what the project proposal is. So we put together a group that's gonna make the project proposal that is not yet a SIG. But the goal of it is to put together, you know, here's what we think the phasing looks like, and how, you know, who's going to be involved, and we put together that proposal together.
And then we can make an OpenTelemetry formal proposal around what we'll build. Does that… Li have your hand up, I don't know if you want to add, or if you'd.
Stephanie B 00:42:34 Thank you.
Liudmila Molkova 00:42:36 Oh, Stephanie, go ahead, I'll… I can speak.
Stephanie B 00:42:38 Oh, no, I was just gonna say, and it, you know, as far as setting a particular time, I know on the OCSF side, We do… so… I do have, like, a time slot.
No one, we haven't had anyone attend, from the, hotel side, recently yet, but on Tuesdays at 1.15, as a time slot that we can dedicate, if that works for interested people. If not, I mean.
I don't mind, like, you know, trying to figure out a different time or day that we can just get a few individuals on a consistent basis to, to meet the kind of, like I said, brainstorm. But, I know right now, on my calendar, we do have, like, a 1.15 slot that could be for the OCSF Hotel Collab.
If you guys… if that… that fits most people's schedules. But, just want to put that out there as an initial place.
Liudmila Molkova 00:43:46 Yeah, I was going to say that we probably need to find somebody specific from this group who would be… who is familiar with Semantic Conventions, at least one person.
And let them play with Stephanie, if you're the representative from YCSF that is interested in the project.
And, like, this 2+, more people would figure out the project proposal that you, Josh, referred to. And then we, we kind of can look at this, project proposal and see what's missing, and what we can… where we go together.
And then it's… the matter of time is the matter of who is interested and have capacity to work. I'm interested, but I don't have capacity.
Stephanie B 00:44:33 Yes, I am one of the point people on the OCSF side, so, like I said.
whoever on this side, who's all interested, then I could kind of work with my schedule to figure out, like, a mutual time for everybody.
If the Tuesday at 1.15 doesn't work, we can shift it to something, that everyone else is available. So I guess on you guys' end, I just need to know who the hotel POCs are, and then I can either reach out to Slack, email, or something like that to kind of figure out, a time to meet.
Josh Suereth (Google LLC) 00:45:09 I will… I will try to make some time here, Stephanie. I… I do have a monthly conflict, which is this week.
At that time, so I definitely won't be able to make it this week, but I'll, I'll, I just added a block to my calendar to try to prevent further conflicts, and I'll see if I can make it in the future. For context, you said it's at 1.15. How long is the meeting?
Stephanie B 00:45:31 Just an hour. Yeah, we just… We just, have a spot, because at first we had it on Mondays and, later afternoon, but I changed it to, we changed it to 115, and it's just, it's dedicated for OCSF hotel collaboration, so, Just 115 to 2.15, that's the time slot.
Josh Suereth (Google LLC) 00:45:52 And that's Eastern… Eastern Standard Time.
Stephanie B 00:45:54 Eastern Standard, yes, sorry, yes, Eastern Standard Time.
Josh Suereth (Google LLC) 00:45:58 Cool. Yeah, I'll try to be there next week, and I think we should follow up on some of the, the, follow up on some of the stuff Christophe put together, follow up on some of the stuff that, you have, the issue that you brought up a month ago. I don't know if that is back in the agenda, with, like, a link to some of your proposals, so people can take a look at it, but yeah, let's, let's continue, and then find folks who are interested in Slack.
Stephanie B 00:46:23 And then… Okay.
And I'll just put a draft agenda, and then, I'll go back in these meeting notes to link this, and then the previous, documentation and stuff that we had, and then for agenda starting for, next week, next Tuesday. Yep. Give people time.
Liudmila Molkova 00:46:42 I guess some… some people might be interested who are not in this call, maybe Trask could be… Stephanie, could you post on the Slack channel that, we're going to do this?
Stephanie B 00:46:55 Yes, I'll send the, So I have a, the Teams link, and then in the Slack channel… oh, yeah, we do have a Slack channel as well, where we do have a OCSF Hotel, Slack channel, so I'll put that in the link now. Just give me a moment, thank you.
Liudmila Molkova 00:47:15 And for comments.
Josh Suereth (Google LLC) 00:47:16 The contact of that channel is on the OCSF Slack, not the CNCF Slack, if I recall correctly.
Stephanie B 00:47:21 That's… that's correct.
Josh Suereth (Google LLC) 00:47:23 Yeah, so if folks want to join, there's a different Slack you need to… Add yourself to.
It is open.
Cool.
Liudmila Molkova 00:47:38 Maybe we should… maybe we should advertise it on our Semantic Conventions look, too?
Josh Suereth (Google LLC) 00:47:42 Yeah, if I were… if I had enough tokens this week, I would, Make something that automatically synchronizes messages between the two.
Just because…
Liudmila Molkova 00:47:52 Unlimited tokens?
Josh Suereth (Google LLC) 00:47:54 Think about it, think about it.
Liudmila Molkova 00:47:56 Don't you have unlimited tokens?
Josh Suereth (Google LLC) 00:47:58 No, I… I… we, yeah, I don't know if you've experienced this yet, Ludmila, but I have gotten to the point where I've run out of my Google tokens.
Liudmila Molkova 00:48:08 Wow.
Josh Suereth (Google LLC) 00:48:08 Really disturbing, yeah.
Liudmila Molkova 00:48:10 Okay, tell me how you updated.
Josh Suereth (Google LLC) 00:48:12 You don't… don't look at my internal, prototypes, because I have a… A bajillion of them. Anyway.
It is possible to run out of tokens, I will… at Google, I will say that.
Okay.
Cool.
Let's see, let's move on to when to admit database response status codes.
I know Trask isn't here, so I was thinking we could try to make some progress on this while he's out, since we have 10 minutes. General bid database rule requires DB's response status code on spans and DB client operation duration when the operation failed and a code is available.
should duration metric follow the span-specific rules? So… Verify that duration metrics use the same status code and value in the inclusion condition.
Whether or not a span was recorded.
Or… make these things follow a general failure-based rule. Successful response codes would become opt-in.
I see.
So you don't report the duration when the operation succeeds?
Liudmila Molkova 00:49:37 You know, the status code.
Michele Mancioppi (Dash0 Inc.) 00:49:41 We have had that… we have had this in the HTTP Semantic Conventions.
And, the, on case of timeouts, the, it's still open.
The, my opinion is that we should have a status for timeouts.
But… That would be more an error.type.
And… there is no real good answer. In general, I don't believe there is any problem in actually recommending the status code on these metrics.
Whenever possible, because most of the times they're going to be consumed in an aggregated fashion.
But we should be consistent with what we do for HTTP, RPC, and, client metrics in, In the mobile SDKs, and I believe that right now we're not consistent about it.
Liudmila Molkova 00:50:44 Yeah, I probably have some thoughts, but I need to check what we do today. I'm not sure if we… if we require… If we… Require a status quo on… duration.
When the operation failed, we cannot Start adding the status code.
To this metric, if operations succeeded.
Michele Mancioppi (Dash0 Inc.) 00:51:12 I don't believe we should require, I believe we should recommend.
Liudmila Molkova 00:51:16 We cannot start doing it by default, because it will be a breaking change from metric.
But I want to check the specific wording, because Maybe it's when operation failed, or code is available, but then… okay, so… I thought we require it when the code is just available.
But maybe something slipped through. So, like, if we designed it from scratch, I would probably say whenever this data squad is available.
But now it's the question of backward compatibility, whether we can change it.
Josh Suereth (Google LLC) 00:51:50 Yeah, yeah, we can't break alerts on duration, those are pretty critical.
Michele Mancioppi (Dash0 Inc.) 00:51:55 Yeah, but somebody is going to… these are histograms, somebody's going to read a single time series.
Josh Suereth (Google LLC) 00:52:01 It shouldn't be, but the problem is the default, easy way to make alerts groups by attributes, and so if you divide the time series, you break people.
Michele Mancioppi (Dash0 Inc.) 00:52:11 No, but that's exactly what I'm talking about. In all aggregations that I can imagine, the attributes that you want to break out are an allow list.
adding more attributes will not break those queries.
Josh Suereth (Google LLC) 00:52:24 They're querying in that fashion, yes.
Michele Mancioppi (Dash0 Inc.) 00:52:28 Yeah, but I would have a very different opinion if these were sums.
other histograms. I've never seen anybody use single buckets.
For this.
Liudmila Molkova 00:52:39 Oh, it's not a single bucket, right? It's the breakdown by status code. If you didn't, filter aggregate by it, then your alerts will be broken if accidentally Somebody uses…
Michele Mancioppi (Dash0 Inc.) 00:52:53 The reason why I'm saying this is that in all metrics for languages I know.
You are not able to access, single, single buckets without an aggregation, and all those aggregations Require you to specify which attributes you want to project.
So adding… adding more activists to a time series does not change the aggregations calculated so far.
Josh Suereth (Google LLC) 00:53:19 This is specific to histograms because it requires an aggregation in Prometheus, yes.
Yeah, this is… this… so this gets into the reason we allow, like, bucket boundaries to change on a histogram is the same, because we expect you not to be engaging with a specific bucket, we expect you to be using an aggregation function. So I… yeah, I… I could buy that as a one-off only for… histograms that we expect in, like, a Prometheus-style metric system, because users should not be alerting on the raw metric itself. That doesn't mean they can't, but according… so, the way our data model's written today, though, it's generic across all metrics, so that point, Michele, is not, accounted for. We just… we… we… our policy does not allow you to make these changes.
Michele Mancioppi (Dash0 Inc.) 00:54:04 No, I agree that the policy does not. I, think that this has… attenuating circumstances, and I would love to hear from experiences with different metric languages, because I have BronQL in my head, and a couple of others, and in none of the metric languages I've used, this would actually be an issue.
But maybe there are some I don't have top of mind.
Josh Suereth (Google LLC) 00:54:29 I want to check… nowadays, I think we have to check SQL, because apparently that's a thing, too. All the crazy-ass SQL time series stuff that's going on in, in modern hipster databases. So I want to take a look at that, but I… I think you're right, that it's probably going to be… because you need to aggregate in some fashion, you're less likely to do it. So, this is one where I think we could call it out as a change that we know breaks our data model, but we're comfortable with because of Reasons?
However, like, I think let's look into the details first before we make any decision there.
Liudmila Molkova 00:55:03 Yeah, I'll look into this, but I think maybe for this one, it's not even I can change because the attribute is already there, and let's say if you wanted successful operations before, you would already needed to, like, say, not equals empty or something.
Yep. Or equal some… Oh, equals empty is interesting. This would be breaking equals empty.
Josh Suereth (Google LLC) 00:55:26 Yep.
Michele Mancioppi (Dash0 Inc.) 00:55:28 No, impromptu would not break, because equals empty and not set is the same.
Liudmila Molkova 00:55:34 Equals empty, but now nothing is empty.
Michele Mancioppi (Dash0 Inc.) 00:55:37 You're right.
It would… it would change the semantics of the… of the metric, yeah.
Josh Suereth (Google LLC) 00:55:42 Because suddenly it would be 200 instead of empty, yep.
Liudmila Molkova 00:55:45 I'll check the specific wording. I… for some reason, I… I thought we have something else there.
So I'll check on this year.
Josh Suereth (Google LLC) 00:55:54 Okay, so take a look. And if this already exists on the metric but was empty, then it still would be a breaking change, because it's possible someone could be grouping by it already, and we would be moving the time series around and breaking all your alerts, so we don't want to do that.
Liudmila Molkova 00:56:13 And, Michele, you mentioned the HTTP, and we have an interesting story there with canceled. We even added something that, that, yeah.
So…
Michele Mancioppi (Dash0 Inc.) 00:56:23 Yeah, I didn't know from my side open the tissue, if I recall correctly.
Liudmila Molkova 00:56:27 Yeah, yeah, I'm calling out to you because I know you've done it. So, it's an interesting problem in HTTP that we discovered that, okay, let's say operation is canceled, but it's canceled benignly. It's not failing.
And there is no single way to record it on metrics today.
You can only record it as a success, or a failure with error type set to canceled. And this is because HTTP status code is integer.
And we can, like, hack and say minus 1 is the canceled or something. But it's… it's a hacky way. So I think going forward, we kinda should not use integer status codes, because they are not expressive.
Michele Mancioppi (Dash0 Inc.) 00:57:12 No, I actually think there is a deeper problem there, because when you have And by the way, Josh, I'm doing that thing where I derail conversations, so if you want to stop me in the interest of agenda, please do that. In ACP status codes…
Josh Suereth (Google LLC) 00:57:27 I'm gonna stop you then. I think let's take this offline. We're almost out of time, and there's one topic I missed, so apologies, Ludmila.
Liudmila Molkova 00:57:37 edits.
Josh Suereth (Google LLC) 00:57:38 Okay, I want to make sure we get to this, if that's okay. So, I think this is a really important thing for us to talk about. Can you… can I ask you two to talk about it on the issue?
Cool. So Ludmila, do you want to talk about transitioning schemas to V2?
Liudmila Molkova 00:57:54 Yeah, so there are… there is just one thing before we do this. We need to figure out the Telio story. So we can, from Semantic Conventions 3.0, have a draft PR to actually generate the V2 schema, the dev version of it only.
And we can attach it to the GitHub artifacts that we publish.
And we can do this today. The interesting question, what should we do with the schemas?
So, turns out, whatever we put in the schemas folder gets published on Autel.io. Autel.io doesn't care what's in this folder. So it's totally in our control to publish anything.
And for this issue, I still need to discuss… I learned with Severin and Patrice about, if they are okay with it, I want them to okay… to okay it. But what I think we should do… once they, blessed, that we would, put, Semcon dash deaf, and one, like, the version after.
We would start maintaining this folder structure.
And… This is trivial. For the future, for stable fully stable subset. It would be similar, but we'll need to figure out how to do this. We cannot do this today. It's impossible with Weaver Publish, because it cannot filter.
That's fun.
So we… I think we should also, for the transition period, publish the current schema, the delta.
And this is a good place to start for us.
I kind of want to just FYI it, and I think I've got some approvals from Josh, from you, maybe from Christoph.
And we can just start doing this. There is a tree quiz latest we need to do, because it's hockey.
Today, the schemas slash latest.
Picks the latest by the… the biggest file, seriously.
And we'll fix it.
Josh Suereth (Google LLC) 01:00:00 Wait, what?
Liudmila Molkova 01:00:02 It chooses latest, because it's the biggest, which is true today, but it won't be true in the future.
Josh Suereth (Google LLC) 01:00:11 That sounds like an Agentic thing, where it happened to be true, and so it locked it down. Okay.
Liudmila Molkova 01:00:16 Yeah.
Josh Suereth (Google LLC) 01:00:17 That's fun. Cool. I… this is really exciting to see. Yeah. So, do you need… you need us to review this issue and make comments on it, then? Or thumbs up it? I think I already…
Liudmila Molkova 01:00:27 You're… yeah, you already summed up. I want your blessing to start doing the… the stable… the Semconv, but I think I already got it, so it was… it's just FYI, and I'll ping the hotel.io people.
Josh Suereth (Google LLC) 01:00:42 Awesome.
Christophe Kamphaus 01:00:43 Sounds good to me.
Josh Suereth (Google LLC) 01:00:46 I'm gonna warn you as well, I'm gonna… I have a ginormous PR for Weaver that changes how resolution works, that will fix about 6 different resolution bugs I found with, multi-schema resolution that we had just never addressed.
So, yeah.
I'm… I'm excited, because I think we're… We're at the point this is gonna be amazing.
Liudmila Molkova 01:01:11 Yeah, I found a few minor issues, with the resolution, or maybe something else. I posted them in Weaver. We should discuss in the Weaver call.
Josh Suereth (Google LLC) 01:01:19 I'm wondering if you found the same ones I found, I just found them via different means, so…
Liudmila Molkova 01:01:24 No, they weren't, like, super nasty.
Josh Suereth (Google LLC) 01:01:28 All of this is, like, stupidly subtle things of, basically, if you do weird things in your YAML file.
Weaver gets really confused, and so it's all edge cases, but they're all, like, things we should resolve before we… anyway, cool. Awesome.
Liudmila Molkova 01:01:43 Yeah.
Josh Suereth (Google LLC) 01:01:44 Thanks, everybody. Sorry we ran a little bit over. We had really good discussions, though. Look forward to continuing them.
Christophe Kamphaus 01:01:50 Thanks. See you.
Stephanie B 01:01:52 Thank you.
Armin (Dynatrace) 01:01:53 Bye-bye.
