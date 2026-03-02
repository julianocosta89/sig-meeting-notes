SIG: System Sem Conv Stability WG
Date: 2025-11-20
Duration: 17 minutes
Zoom Recording URL: https://zoom.us/rec/share/9pzufFF96RSIgkjc07KRODlbwUOm86IuANOLeN0q-t1E_P2eJq4uMF3Mr6wsQmmx.cZWOqXjFQhxrxes_
============================================================

## Zoom Recording Transcript

**Max and Ruby (ca-wat-brt3)** 00:05 ridiculous.
That's okay.
I won't.
Fair enough.
**Pablo Baeyens** 02:02 Hey, sorry for the delay.
**Max and Ruby (ca-wat-brt3)** 02:05 No problem.
**Dmitrii Anoshin** 02:07 Hi, folks.
**Pablo Baeyens** 02:21 I think we can get started. I think Christos is out.
**Max and Ruby (ca-wat-brt3)** 02:28 Okay, sounds good.
Hope everyone had a good time at KubeCon. Folks who went?
I added the first agenda item, which is, last week we talked about the…
it's like setting up the requirement levels for all the stuff in the process namespace. I drafted that out and opened it just as a PR on my fork, just so we can
We can discuss on there without…
worrying about folks outside our group looking at it. We can just discuss as a group how we feel about all this, and then if we feel good about the stuff on this PR, then I can turn it into an actual, properly formed PR on the upstream repo.
So, take a look when you get a chance.
**Pablo Baeyens** 03:37 Would you mind, if it's not too much work, generating the markdown? I think that…
It's probably easier to read.
**Max and Ruby (ca-wat-brt3)** 03:46 Sure.
**Pablo Baeyens** 03:48 Thanks.
Hmm…
**Dmitrii Anoshin** 04:28 So far, it looks good to me, Braden, thank you. Just keep in mind that when we say required… requirement level for that attribute, in the collector context, it would mean that
there will be no option to aggregate over that attribute. And I think…
everything here makes sense. Like, we don't want people to remove
CPU mode and aggregate without it, because it'll just give you, like.
essentially 1. Value 1, right? And, yeah, but otherwise… Looks good.
**Max and Ruby (ca-wat-brt3)** 05:09 Yeah, in the process namespace, all the attributes seem to be, like.
the mode, or, like, the I.O. direction, or things like that. Like, things that we don't want.
people to aggregate across. Although, I don't know, IO direction, is there any reason to aggregate across both write and read?
I wouldn't…
**Dmitrii Anoshin** 05:28 Only…
**Max and Ruby (ca-wat-brt3)** 05:29 I've heard of that use case, but…
**Dmitrii Anoshin** 05:30 Users want to, like, let's say, do total traffic, which kind of doesn't make a lot of sense, but…
And we… and this also aligned with the… with the semantic conventions, right?
Or not. Oh, no, this is PR semantic intervention, sorry.
**Max and Ruby (ca-wat-brt3)** 05:48 Yeah, this, yeah, this is the semantic connections peer.
**Pablo Baeyens** 05:53 Boom.
One question,
Is it bug words compatible to make any changes to the requirement level? For example, could we go from required to recommended in the future?
**Max and Ruby (ca-wat-brt3)** 06:12 Hmm…
**Dmitrii Anoshin** 06:14 If we speak from collector perspective, that would… wouldn't be a breaking change, because we start allowing, aggregating over that attribute, but from semantic conventions, I don't know what's the rules.
**Josh Suereth** 06:25 So, what was the order? Required to recommended, or recommended to required?
**Pablo Baeyens** 06:30 Required to recommend it.
I assume recommended to require would be a breaking change, but required to recommended is the way.
**Josh Suereth** 06:37 No, it's,
required to recommended would probably also be a breaking change, because if I design a dashboard that expects that attribute to exist everywhere, and then it doesn't.
like things break, or my alert, right? So, like, the way to think about required and recommended are, I'm designing a dashboard, I'm designing an alert, I'm designing some sort of query.
Required means this will always exist, and so I can depend on it being there, and I will not even check if it's there or not. So if you switch that to be recommended, you actually would break users. So required and recommended actually can't change.
Without it being a breaking change.
**Pablo Baeyens** 07:17 Okay, and what I would opt in to recommended?
**Josh Suereth** 07:23 Yeah, that, I think, would also be… That would probably be okay.
You do have to manage the opt-in to recommended
ness of things. Now, if this is on a metric.
That would also be considered a…
It's considered a breaking change today because we can't deal with opt-in effectively.
We're actually missing, like, what we need to consider opt-in things safe. Like.
Theoretically, what you're saying of moving from opt-in to recommended, totally safe, totally fine.
If done correctly. We don't have the control in semantic convention to force that with our YAML model, so it's not allowed today.
But, like…
**Pablo Baeyens** 08:12 Yeah, I'm… I'm not talking about today, I'm not thinking about specific changes, it's just, like.
**Josh Suereth** 08:17 Oh, conceptually…
**Pablo Baeyens** 08:19 Yeah, thinking about what things are more important to get right, or, like.
Where we have more leeway or less.
**Josh Suereth** 08:27 Yeah, for metrics specifically, I would… I would make sure that they're acquired, you are comfortable with those, because those will be locked in for quite some time.
Recommended, we can add in recommended over time safely.
that's… that's kind of by design. You will have to make sure that, like, any specific instance of instrumentation, like, if there was an opt-in feature that you're defaulting on, you'll probably want that component to go through a major version bump to explain to people that that's happening, or some kind of a, you know.
Cycle where you warn them that this is coming, just in case they were not opted in and not, like, relying on those attributes, and then suddenly they're there and their metrics break.
Or their alerts break.
But, that is a safe thing to do if done correctly.
**Pablo Baeyens** 09:21 Okay.
**Max and Ruby (ca-wat-brt3)** 09:23 Is there no requirement level on metrics?
**Josh Suereth** 09:27 No, there… there's a… you mean on the metric itself?
**Max and Ruby (ca-wat-brt3)** 09:30 Yeah.
**Josh Suereth** 09:31 On the metric itself, not yet. That's an open feature request. We might… I might be adding that in V2 schema once I get through all the other stuff.
**Max and Ruby (ca-wat-brt3)** 09:42 Got it. I had it written down in the PR, but it's not a field in the schema, so I will just remove those.
**Josh Suereth** 09:54 The issue with requiring a metric right now, and this is an enforcement issue, we're trying to avoid putting stuff in YAML that we can't enforce in some fashion, or that we don't have a validation check for. So, requiring a metric,
Basically, what does that mean?
Does it mean that if I have a host resource, I should always expect this metric to show up?
What's it required within, you know?
So I think required right now might be more your, like, a configuration concern of the component in the collector. So the host receiver would say.
Here's what's default on, here's what's not default on.
You can use annotations if you want to put that in the SEMConf.
For, like, collector code gen?
But that's not… like, from a SEMCOM model perspective, we don't have a way to enforce required in any reasonable manner.
**Max and Ruby (ca-wat-brt3)** 10:50 Okay.
**Josh Suereth** 10:50 For metrics. Like, for a metric itself. For attributes, we can, right? Because that's within a metric.
**Max and Ruby (ca-wat-brt3)** 10:59 Yeah, I was… I was mostly thinking about it from a collector perspective, where, like.
required would be, like, always enabled
don't allow users to disable, although I don't know if we have a mechanism to do that name data, Jane.
**Dmitrii Anoshin** 11:14 We're done, right?
**Max and Ruby (ca-wat-brt3)** 11:15 basically… Is… there isn't?
**Dmitrii Anoshin** 11:18 No, we don't have it. We have only, like, we… essentially, for the metrics, we support only recommended and opt-in, and it translates whether it's enabled by default or disabled, but users can enable and disable any metrics. And I'm not sure if it's… if it's really, like, good to provide a metric that can never be disabled, because
But potentially, they can still, like, set up a filter processor and remove everything if they want to.
**Max and Ruby (ca-wat-brt3)** 11:48 Yeah, yeah. That makes sense.
**Dmitrii Anoshin** 11:52 So I'm not sure if we even want to translate a required label… a required level in the collector.
**Max and Ruby (ca-wat-brt3)** 11:59 No, you're probably right.
**Dmitrii Anoshin** 12:05 But yeah, this is, like, probably another discussion. Speaking about… The context switches.
Hmm, what did… are we sure that…
Context switch type is a required attribute?
Potentially, because if I want to…
Doesn't make any sense to have a total number of… Context visuals.
As a metric.
**Max and Ruby (ca-wat-brt3)** 12:35 I'm trying to think about…
whether it would, because if I'm thinking about it from a monitoring perspective, I would probably be watching for
If I'm watching for, like, a voluntary Voluntary context switch…
Meaning some sort of in-application problem, and involuntary meaning some kind of, like, system pressure.
I don't know what the use would necessarily be of adding them both, but I also don't know if that's not useful. I, like, I don't… I couldn't say, actually.
Yeah, I could… I could go either way on making…
making those recommended instead of required, like the directions and the types and stuff, I'm not sure.
**Dmitrii Anoshin** 13:39 Yeah, and I don't have a strong opinion here, I'm just raising it for debate, I don't know. Maybe forward direction, it's not that obvious, like, but for context, which is potentially maybe someone would be interested in…
**Max and Ruby (ca-wat-brt3)** 13:55 Yeah.
**Dmitrii Anoshin** 13:56 Or both, I don't know, like, maybe… like, let's keep it like this, submit a PR, and put maybe some kind of a comment saying, hey, if you think,
aggregating over… This attribute would make any sense, we can make it recommended.
**Max and Ruby (ca-wat-brt3)** 14:17 That worked for me.
**Dmitrii Anoshin** 14:25 Yeah, I wish we'd have more people.
I believe we st…
We have some more people involved these days, at least, in submitting PRs and reviewing, so that should work, I hope.
**Max and Ruby (ca-wat-brt3)** 14:45 Probably too late now, but I did push the markdown generation.
I just got slowed down by the… The schema problem.
**Pablo Baeyens** 14:56 No worries.
Yeah, no, I mean, I think in general.
what you could make sense, but it's useful to have the markdown to read it again.
**Max and Ruby (ca-wat-brt3)** 15:09 Yep.
So, if… if that's all good, I can clean that up and submit it as an actual,
SEMCOM PR, properly formed.
**Dmitrii Anoshin** 15:24 Sounds good. Thank you.
**Max and Ruby (ca-wat-brt3)** 15:25 And I'll also be… Working on,
the rest of the process namespace issues that were assigned to me for the rest of the week, I'll be working on those.
**Pablo Baeyens** 15:41 Thank you. Thank you, Braden, for…
Getting this through the finish line.
**Max and Ruby (ca-wat-brt3)** 15:46 No problem.
**Pablo Baeyens** 15:56 Yeah, it makes sense for me to open up here. Sorry, I always finish in green there.
Scheme through the markdown.
Stuff.
**Max and Ruby (ca-wat-brt3)** 16:04 Yeah, no problem. I will… Do that today.
**Dmitrii Anoshin** 16:26 Okay, if we don't have anything else, should we wrap it up early today?
Yep, might as well.
**Max and Ruby (ca-wat-brt3)** 16:34 I guess I'll mention everybody in here probably knows, but I did make the project board for the collector component stability, and so if there are any, like, host metrics issues that you can think of to add, I've added a few already, but if you can think of any more that I missed, you can go ahead and add it to the board. There's just, like, a label.
That you add component stability phase one, and it'll add it to the board automatically.
**Dmitrii Anoshin** 16:55 Awesome, thank you. Thank you, Braden.
**Max and Ruby (ca-wat-brt3)** 16:57 Cool.
**Pablo Baeyens** 16:59 I know to use that board for the collector seat meeting.
To know what we should review. So, yeah, thanks.
**Max and Ruby (ca-wat-brt3)** 17:08 Yeah, I think it just needs a bit of… a bit of triage work. I did… I did for postmetrics, and I can do for file log, but for the other components, you know… I think Arthur's already been doing some stuff for the Prometheus one, too, so…
**Pablo Baeyens** 17:18 Yeah, I'll try to spend some time next week. Anyway, something for the collector's sake.
See you all on the internet.
**Dmitrii Anoshin** 17:27 Fantastic.
**Max and Ruby (ca-wat-brt3)** 17:28 Thanks, everyone.
