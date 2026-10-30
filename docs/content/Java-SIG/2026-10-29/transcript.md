SIG: Java SIG
Date: 2026-10-29
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Gregor Zeitlinger** 01:36 Hello!
**John Watson** 01:41 Hello? Hello!
**Trask Stalnaker (Microsoft Corporation)** 03:11 Hey, hey.
**John Watson** 03:16 Hello?
**Trask Stalnaker (Microsoft Corporation)** 03:53 What's your new last name, Jason?
**Jason Plumb (Splunk Inc.)** 03:55 I realize I don't know how to spell Jason Voorhees, so I gave up on it.
**John Watson** 04:01 V-O-O-R-H-E-E-S.
**Jason Plumb (Splunk Inc.)** 04:06 Just like it sounds.
**John Watson** 04:08 Just like Steve Voys, whom we do.
**Jason Plumb (Splunk Inc.)** 04:11 Oh, yeah.
**Trask Stalnaker (Microsoft Corporation)** 04:20 We've got a light agenda.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 04:28 So I'm gonna go through any of these open PRs and OpenTelemetry Java, and See if any are candidates for, like, an interactive review.
**Trask Stalnaker (Microsoft Corporation)** 04:42 I think I saw…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 04:45 That's scoped attributes.
**Trask Stalnaker (Microsoft Corporation)** 05:42 Did you see there's a… PR… I think it was… David… to stabilize… The attributes instrument advisory parameter.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 06:03 That's cool.
**Jason Plumb (Splunk Inc.)** 06:04 What the heck is that?
**Trask Stalnaker (Microsoft Corporation)** 06:07 That is the thing that we rely on very heavily in the instrumentation repo.
We send all the attributes that we capture on, like, a span. We send those all to the duration metric.
Yep.
But we thought there's a lot of high cardinality attributes in there.
We use the… advisory parameter, it's a mouthful. The advisory parameter, when we're setting up that metric to say which Attributes we want to capture by default.
**Jason Plumb (Splunk Inc.)** 06:45 So it's a feature of metrics.
**Trask Stalnaker (Microsoft Corporation)** 06:47 Yes.
**Jason Plumb (Splunk Inc.)** 06:49 Interesting.
**Trask Stalnaker (Microsoft Corporation)** 06:51 And it… what it does is it allows people to opt in to, More of those span attributes, if they want, via metric views.
**Jason Plumb (Splunk Inc.)** 07:05 Got it.
That seems cool.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 07:15 Yeah, there's a related one that I added as well, which is, David, merged a PR to the spec, at least I presume he merged it, to add this new metric opt-in parameter.
And, the idea with the metric opt-in is that, You know, it's similar to the attribute advice, so it's basically saying, like, hey, we want instrumentation to be able to record the fact that you probably don't want this metric by default unless you explicitly opt into it.
And so… Yeah, record metrics, but don't process them and enable them unless you explicitly opt-in via the SDK.
And, I have thoughts about this one. Yeah, there's an agenda, but it's light, like you said. So, you know, the ability to opt into a metric, it, it has similarities to log severity.
In the sense that, like, severity is this, This kind of enumeration that allows you to quickly select which logs you want to see, you want processed and exported.
And so, you know, the metric opt-in, the name is different, so that's kind of a smell to me. The fact that it's a Boolean, it's just, like, true or false, versus, like, you know, an enumeration, that's kind of a smell to me.
And, I know similar ideas have been expressed about spans as well, like, so what would it look like to have a severity-type concept or equivalent? Just, like, some sort of, like, enumeration of importance conveyed at the instrumentation time that would allow you to, like, you know, configure at the SDK level, like, what you want to see and what you don't. And so.
I don't know, I'm kind of wondering what we should do about this in Java, because I don't think the spec is quite there yet, even though it merged this PR for this opt-in parameter. I would like to see something that's more, like, signal-agnostic around this concept.
**Trask Stalnaker (Microsoft Corporation)** 09:31 I think it's… I don't… we're not clamoring for it, in instrumentation. I mean, it's a… it's… Yeah, so… could be nice in some cases, but I think we're… Kinda… we're okay.
with the status quo, so I don't think there's a necessary-to-rush experimental feature.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 10:04 But I recorded some notes on there. I'm gonna… I haven't gotten to reviewing David's PR, but yeah.
**Trask Stalnaker (Microsoft Corporation)** 10:19 Context, scoped attributes.
The long… time coming…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 10:30 Yeah, so how are they gonna do this?
Okay, so there's a context attributes, and a context key.
That allows you to… what does it do? It, like, you know, when you add attributes to this context key, it merges them, if there's some already there.
And then, what's the intersection over with the SDK?
at the logger provider level, and presumably tracer provider and meter provider, there's a new Boolean which says, like, hey, are context-scoped attributes enabled?
And if they are enabled, Presumably, we're gonna… Extract all those attributes out of context and stamp them on the telemetry.
So, Trask, do you know of any, issues in instrumentation that relate to this?
I think it's been a, like, a pretty popular concept for a while for, you know, use cases like applying a tenant ID to all your telemetry, or, you know, other sort of global state-type things, like a user ID, something like that.
You know, if you can, ahead of all your telemetry recording, if you can put the user ID or the tenant ID in context, and then have instrumentation automatically apply that to all, all telemetry recorded within that scope, that's a pretty powerful lever.
But I don't know of an issue of it in the core repository.
**Trask Stalnaker (Microsoft Corporation)** 12:26 And there is, I think, the… Inherited attributes… I think this is… the big, I don't know.
Yeah, there's been… Definitely interest, I mean, Halo 4 is a Java… Or has been involved in the Java… Repo.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 12:58 Oh, there we go, yeah, that's the… that's a similar concept.
I think my main rub with this would be the… just the expressiveness of it.
I think it's just a Boolean that indicates whether your meter provider, logger provider, tracer provider lifts context-scoped attributes onto all of your telemetry, and I think it needs to be more granular than that, of course, because of, like, cardinality explosion with metrics.
But, you know, I'm thinking just some sort of, some sort of predicate, would be enough, at least to start.
you know, do you want the predicate being, like, just, like, the attribute key? Like, do you want to lift this attribute key onto all of your all of your telemetry, because if it's just, like, a Boolean, it's kind of a… it's kind of an attack vector as well.
Just thinking out loud, like, if somebody can get a hold of a context, they can put a bunch of data in context and, cause excess resource allocation, excess resource utilization, by spamming that onto every exported span log and metric.
**Trask Stalnaker (Microsoft Corporation)** 14:21 I mean, at the point where you can get that kind of access, you can emit all kinds of garbage telemetry.
**Jason Plumb (Splunk Inc.)** 14:29 Yep.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 14:35 It's true.
**Jason Plumb (Splunk Inc.)** 14:36 I wonder, so that, yeah, I mean, like a… You mentioned the tenant use case. I'm instantly applying it to, like, maybe Session and Android.
Which we… we don't have metrics, so that's kind of… I mean, we do, but, like, no one uses them because of cardinality problems.
the… Session we put on every… every span.
And we just do that with a span processor. There's, like, no… and it doesn't come from the context, like, we don't put it in the context.
But I'm wondering, like, what other use… what other… I mean, you mentioned the multi-tenant thing, I'm wondering what other use cases there are for this.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 15:15 That's sad.
**Trask Stalnaker (Microsoft Corporation)** 15:16 Increase.
I think we've had cases where… I'm trying to think through where you want to… Pass some… Context down to a… Oh, yes, so… I think a good example is… Database instrumentation, database… we have, like, DB operation name.
And you may… we, like.
Extract it heuristically from queries if we're parsing it, or, you know, people who don't parse it don't get that.
And… but… Application can have a much better name for it.
look up my product, blah blah blah. And so… To be able for them to influence that, that database.
span… They have no way to influence the database span currently.
As opposed to server spans, they can influence, because they can get the current span and attach attributes or something, override stuff if they want. But client stuff, they can't get access to that, there's no hook.
So, the context attributes would allow them to pass down A better operation name, and the database instrumentation could use that Instead.
**Jason Plumb (Splunk Inc.)** 16:56 Okay.
**Trask Stalnaker (Microsoft Corporation)** 17:01 I think we even have, I think we were even thinking… Towards that direction with… Let's see… No.
I remember having that discussion, but yeah.
Where I thought was that if instrumentation could, it would be nice to allow people to… Provide their own.
Maybe query summary… Summary may be available to instrument through instrumentation hooks or other means.
Yeah.
Anyway, something like that.
Which is a little different, Jack, than, automatically… like, I guess the… do… So, instrumentations could read that context.
Attributes, and do their own something with it.
But in this case, I mean… You may as well just auto-stamp, auto-override.
I kind of wonder why… why we need an opt-in for… for it, like, why… Like, could it be as simple as just… stamping… Automatically, like, once you put something in the context attributes, that means stamp it all the way down.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 19:07 But there's probably…
**Trask Stalnaker (Microsoft Corporation)** 19:08 use cases where you want to just pass some data around…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 19:17 I… I'm in favor of having this default off, but giving you easy ways to enable it.
And I…
**Trask Stalnaker (Microsoft Corporation)** 19:34 That's how the spec is written today, right?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 19:38 Yeah, I'm reading… I'm re… it's not even a spec, that's the problem, is, like, there's an OTEP that was merged, and then no one followed up and wrote a spec.
And so… This is… this whole thing is, like, questionable, but, I think the author here has, put it in incubating.
Incubating packages and things like that, so… I don't know, maybe we can, like, I think I'm inclined to, like, you know, pretend that a spec exists for this, because there is an OTEP, but, like, have, like, a time bound on it. Like, if there's not a corresponding spec that codifies the OTEP in a certain amount of time, delete the feature.
So it's not just, like, perpetually incubating.
**Trask Stalnaker (Microsoft Corporation)** 20:31 I know the Python Gen AI folks are talking about it.
I think they have some use cases.
as well.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 20:44 I should pick it up and… Take, take ownership of the spec.
I think on the enablement, that's, like, the main thing that I wonder about for this, is, like, what is… you know, we were talking about whether it should be enabled or disabled by default, but I also, am thinking about what the shape of configuration is, if you do want to enable it, and like, the OTAP just… I think there was, like, there was a… if I remember correctly, when people were debating the OTAP, there wasn't… there was a lot of different ideas of what config could look like and what it ought to look like, and I think everyone just, like, collectively punted on it and said, like, let's treat it as a Boolean for now, and we'll come back to it.
Because, like, you know, we couldn't… we couldn't sort of wrap our heads around it. And so, I'm not really looking at the Boolean, that landed in the OTEP as, authoritative.
I'm looking at… I'm, like, sort of reading it as just, like, you know, this is what we could come up with at the time, but this is not necessarily what the final shape would look like, and And for a more appropriate final shape for me, I was mentioning a predicate, where you could, like, select a, you know, on a per, you know, attribute key basis.
which, which context scope attributes you wanted to bring in, but I think it'd be better to even go more granular than that, and have the predicate be, like, a tuple of the, the… the scope and the attribute key. So you could, like, decide for a given instrumentation scope whether you want this attribute to be stamped on your span log metric.
And I think that that… that, like.
gives you granularity if you want it, but it doesn't force you to use it, because you can just have a… you can just, like, have a predicate that returns true for all. Like, include all contact scoped attributes on all scopes, and it's really easy to express that, and there's no usability concerns for expressing that. But if you do want the additional granularity, I don't think There would be any performance, Hit to exposing this expressiveness.
So… That's just, like, off the top of my head where I lean.
**Trask Stalnaker (Microsoft Corporation)** 23:00 Declarative configuration first.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 23:04 Yeah, and that's the problem, is, like, then, you know, people have not opened that PR to declarative config, so…
**Trask Stalnaker (Microsoft Corporation)** 23:13 Yeah, it might be worth, ping Lyudmila to see, if there's any concrete efforts on the Python Gen AI Yeah, it sounds like this is more like a… Poc for the spec.
At this point.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 23:33 Yeah, exactly. And I'm looking at the code, and it doesn't really look controversial, it seems like, how I would imagine it, with just, like, a few exceptions. So, I'm inclined to land it in, like, in some version of this that's, like, you know, mostly as the author has written it, but… Yeah, I don't want a repeat of the view baggage processor, where that, like, stuck around for 5 years, waiting for the spec to land that codified it.
So, you know, if we're gonna sort of go outside our normal boundaries and have code that is, like, outside of the spec, I'm thinking that all that type of code should have a TTL attached to it, so it automatically is deleted if the criteria is not met.
So… Right.
**Trask Stalnaker (Microsoft Corporation)** 24:31 Cool.
Shall we move on to our…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 24:41 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 24:42 other… topic I threw on randomly…
**Jason Plumb (Splunk Inc.)** 24:53 Is there spec work around what's identifying for host?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 24:58 Yes, that's in the semantic conventions.
**Jason Plumb (Splunk Inc.)** 25:00 Okay.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 25:02 And host ID is identifying. This is kind of odd, and I don't know the history of this Trask, maybe you can recall it off the top of your head, and Lauri, maybe you as well. But, like, so there's a, the host ID, which is the key identifying attribute for the host entity, is opt-in.
And it defaults to false, because, you know, you… apparently you have to do some stuff to detect host IDs, so, they, you know, instrumentation has an opt-in right now, but… so, the way that it works, then, is, like, if you don't have the identifying attributes for the entity, you can't omit the entity.
So it's like, if you opt into collecting host ID, then you get the host entity, and if you… so then, by default, you don't get a host entity.
So, Lauri left a comment on this, and I'm not sure, Lauri, whether… what the history is behind host ID and it being opt-in, and if, like, the intent of your comment was, like, we should get rid of this opt-in, and we should just have host ID collected by default.
Collected all the time, maybe even.
**Lauri Tulmin** 26:08 Oh, I thought that it was, opt-out, not opt-in.
But I think probably the history is such that the host resource was there before.
And the host ID was added later.
But, I think…
**Trask Stalnaker (Microsoft Corporation)** 26:26 Okay.
**Lauri Tulmin** 26:26 Currently, If they are in the same resource, Then, I think, currently.
You can't opt in when using the declarative configuration.
**Trask Stalnaker (Microsoft Corporation)** 26:44 Which is… Fine to consolidate and simplify, as long as, is there any… do we have to do… do you remember if we have to do anything expensive to… capture the host ID that we might want it to be off by default.
**Lauri Tulmin** 27:04 Oh, I don't remember exactly. It might execute some external command.
On some operating systems.
**Trask Stalnaker (Microsoft Corporation)** 27:12 That's fine, just as long as it's not, like, the AWS… Ones where resource detectors, where it has to make a remote call that can time out or something.
**Lauri Tulmin** 27:23 I think the comments came from the spec, anyway.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 27:33 So then what I'm hearing, sort of, is that we… pending a little analysis around the safety of host ID, of collecting it, we… we might want to just get rid of this, this enabled flag altogether.
Or do you want to be more nuanced than that and keep it, but, like, default it to enabled instead of defaulting it to disabled? Because right now, I think it's default disabled.
**Trask Stalnaker (Microsoft Corporation)** 27:58 I would check just where it came from.
You know, get history.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 28:06 Yep.
**Trask Stalnaker (Microsoft Corporation)** 28:09 my… I mean, I… I don't mind just removing it for 3.0, and if we get people coming and saying that there's a problem, that we can Add it back.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 28:27 Alright, I'll do some spelunking in the Git history.
**Lauri Tulmin** 28:30 I think, if we are going with a flag, then we should make sure that, It's also configurable in the declarative configuration.
To have some… feature parity.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 28:52 Yeah, I… So, okay, but that doesn't matter if we remove the flag.
And so, but if the Git history tells us information that suggests that we should keep the flag, then we want to try to have parity with declarative config, which I, of course, agree with.
So, yeah, okay.
**Trask Stalnaker (Microsoft Corporation)** 29:18 Whoa.
And, yes, as… If you haven't noticed, folks, the V3 continues to get pushed.
we did just stabilize RPC semantic conventions yesterday, so that's going to be in 3.0 now, and there's a couple other, the… Lauri the, I have a PR to the… the peer service name stuff.
That got renamed, it got renamed again, earlier this year already, people didn't like the new name, and so there's a new name now.
just that I think everybody agrees on, just waiting for that, and then with 3-0, we'll be… we'll remove both of those and just have the… support the 1, so that'll… Trim a few things.
**Lauri Tulmin** 30:18 Are you also going to use the rename for those messaging attributes?
**Trask Stalnaker (Microsoft Corporation)** 30:25 Yeah.
Did that one actually get merged already?
Yeah… Okay, okay, yes.
Thanks for that reminder, I forgot already.
**Lauri Tulmin** 30:49 So, in another 300 or so pull requests, we should be good to go.
**Trask Stalnaker (Microsoft Corporation)** 30:56 I'm sorry.
Yes, thank you for your… Patience and support.
**John Watson** 31:05 Hey, breaking news, congratulations, Trask on being re-elected to the GC.
**Trask Stalnaker (Microsoft Corporation)** 31:10 I'm seeing a bunch of… Slack messages. I haven't actually seen the results yet. Awesome. Fantastic.
**Gregor Zeitlinger** 31:23 But this time, you cannot purchase that.
**Trask Stalnaker (Microsoft Corporation)** 31:32 I don't think we caught what you said, Gregor.
**Gregor Zeitlinger** 31:36 This time, you're only number 2. That's outrageous.
**Pranav Sharma** 31:45 So, where do you see the results?
**John Watson** 31:49 I got email about it. Yeah, if you voted, you should get emailed about it.
**Pranav Sharma** 31:55 Oh, okay. This was the first time I voted, I'll check my mail.
**Trask Stalnaker (Microsoft Corporation)** 32:05 Thank you all who… Voted.
Regardless of who you voted for, voting is important.
Cool. Anything else?
For us to chat about.
We're at halfway.
Alright, then.
Let's get some time back.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 32:42 Alright, thanks, everyone.
**Trask Stalnaker (Microsoft Corporation)** 32:45 Bye.
**Pranav Sharma** 32:45 Thank you.
