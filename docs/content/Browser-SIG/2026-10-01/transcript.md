SIG: Browser SIG
Date: 2026-10-01
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Martin Kuba (Raintank, Inc. – Grafana Labs)** 00:41 Chris.
How are you?
I think you're muted, but Okay, gotcha. No worries.
**Maxime Quentin** 01:32 Hello?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 01:35 Hi, Maxime, how are you?
**Maxime Quentin** 01:37 Good, good, and you?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 01:38 All right.
Just wait a couple more minutes. I think Jared is on vacation.
I don't know if anybody else is joining today.
**Maxime Quentin** 02:45 I mean, I've seen David dropping a topic, so… Okay.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 02:52 I did do it here.
Hi, David.
**Maxime Quentin** 02:58 Okay.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 04:02 Hi, Cleo.
**Cleo Schneider** 04:07 Hey! How's it going?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 04:09 Good, how are you?
**Cleo Schneider** 04:11 All right.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 04:14 So, we've got, we don't really have A lot of topics for today, I think there's just, One request for review from David, And… Yeah, this one… It's pretty… should be pretty straightforward, and… Once that's merged.
you could probably do a release. There's a couple new features on the SDK that we could release.
Today, or soon.
Aside from that, I also wanted to just… David, do you want to talk about this at all, or… No.
And, I also wanted to say, like.
A lot of my, kind of, focus this week has been on bootstrapping the new client-side semantic conventions repository, and I opened the originally had I opened a PR here in this repo to have the browser semantic conventions here, but it's moving to the other repository, so I'm just from cross-sharing.
I'm just, sharing the link to the new, PR.
If you have time, and you care about semantic conventions, please take a look at it.
Aside from that, I don't really have any other topics to discuss.
This week, does anybody have anything that they want to talk about?
**Maxime Quentin** 05:55 Most of my side.
I'll try to have a look at your Pr. David.
**David Luna Bistuer** 06:03 Okay, thank you.
I guess, I don't know, maybe… I guess maybe it's better to have the discussion in the PR itself, but, Jared opened that PR on the Browser Instrumentation, the new instrumentation base.
what I… maybe I want to ask is that it's the… I think we'll be importing… still importing the types from the… Formal instrumentation package.
Is the intent to keep this compatibility, or… Or just, it's convenient. I don't know. Let's just ask if… that what's the point? So if you want to break it down, we're already breaking things, but… We want to have our own.
interface for Or we want to keep having some.
Dependency or compatibility with the node ones.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 07:01 David, this is for the instrumentation base.
Pierre.
**Maxime Quentin** 07:05 Yeah.
I feel, Like you were saying, the lifecycle of the instrumentation is a bit complex.
So,
**David Luna Bistuer** 07:15 if.
**Maxime Quentin** 07:15 Something that makes sense for Browser, and that is not super adapted to, like, Node.js.
I would be up to have a dedicated instrument base for us.
But then, it needs to make sense, like, in the PR, like you were saying, David, the flow is a bit complex right now, so…
**David Luna Bistuer** 07:39 Yeah, and I feel that's complex because we want to kind of keep that API, that same… So, we have separated set, loggers set, so the different providers are set.
have different setters, and… Yeah, it seems that, you know, the next complex, we have a kind of a state machine here.
With a lot of cases and a lot of arts and states.
And maybe it's because we want to keep that… the API. I don't know how much we're committed to.
with the compatibility. I remember… it's because I remember in the past that I was saying that, okay, maybe it's fine just to break things.
And have something that it's, better for Browser.
So I want to kind of, Sense, what is the… The idea here, what the other people think.
**Maxime Quentin** 08:33 Like, do we know how many instrumentation could be leveraged in both, like, environments? Because… For instance, I don't know, like, as an example, like, user action instrumentation, or I don't remember the name, but it's probably something we will not have.
In, Node.js?
And so, if we have very few instrumentations that we share with them, I would be fine with having something very custom for WOSAR.
And a state machine that is less complex.
Like you were saying, just setting some… Instantiation and startup.
And… That would be okay for me, but… Not sure.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 09:23 Yeah, I don't think there's any intent of sharing instrumentations from here with Node.
**Maxime Quentin** 09:32 Yeah, so at this point, if we don't plan to share many instrumentation with them.
Maybe it's better to start our own, Flow and make it simple, so people can contribute, and… Like, for the… For the long task, instrumentation, if we have a clear, instrumentation base, any newcomer can Come and have an idea with an instrumentation and then just land it.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 10:09 Yeah, so you're suggesting that we could just, like, simplify this PR, so remove some of the complexity for the backward compatibility?
Yeah.
**Maxime Quentin** 10:18 Yeah, I agree.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 10:22 That's a good point. Yeah, if you don't… if you don't plan to do that, then why… why have it complex?
**David Luna Bistuer** 10:36 Okay, maybe I'll… then I'll comment it out here, and maybe I'll ping Jared about this, because, I don't know, with this PR tool, the team's kind of concerned with the API that we have already.
So he has to cover a lot of cases.
**Maxime Quentin** 10:50 Yeah, there are cases where, like, if you're enabling, but at the same time, you're Like, stopping it, then you can have, cases that are not covered.
And the state machine?
It's starting to be a bit crazy, so… It's kind of out of my league to clearly block the PR, but yeah, I think it's a good input to simplify it.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 11:21 Yeah, I agree.
Okay, yeah, let's, let's maybe, like, talk to Jared about this when he's back.
It'd be good to make a decision on this soon.
Okay.
Do we have any other topics?
For discussion.
**Abinet** 12:28 I have one question.
So the the new, the open term 3 Browser repo. Does it? Does it have now all the instrumentations that we are in the Previous repos and, like, current customers, like.
Start using this, like, and is there also, like, a… Guidance for migration, because… I think there are so many changes, like, on the… We are using locks on some of the instrumentations. Some instrumentations are probably Not as… Before, like, for example, I don't know if document instrumentation is still here, or… If this is replaced by the… Navigation, related instrumentations.
Yeah, I just want to know if there is, like, Migration guidance, or if… If this.
Kind of straightforward, too, we just migrate to this, Yeah.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 13:32 That's a good question. I think all the instrumentations that we wanted to, provide are here. Like, we recently moved to XHR and Fetch instrumentations here.
you're right that, like, maybe the biggest gap, or the biggest difference is the document load, instrumentation that was in Contrib, was in Contrib, because that one is based on spans, and… It's widely used. We do not have a migration guide right now, but that's a good… Point, like, we probably should have something that Compares those two.
So I'll take an action item on this, and Start working on that, or create an issue at least, To add a migration guide.
Or some kind of guidance on how to, Yeah.
**Abinet** 14:24 Alright, thank you.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 14:43 And also, Abinet, there was, we, I think, just, like, last week or the week before, we made a decision to, deprecate the React.
Direct plugin instrumentation.
So that's being completely deprecated in JS Contrib.
That instrumentation wasn't used very much, so I don't think it's a big deal, but just… FYI, since we're talking about it.
**Abinet** 15:11 Yeah, okay.
Yeah, we are not also using it, so, yeah.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 15:16 Okay, yeah, I don't think anybody's using it.
**Maxime Quentin** 15:24 Like, I was wondering, like.
Is migrating the document load instrumentation to, logs something we considered already, or are we good with using Spans for that?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 15:39 Sorry, which one?
**Maxime Quentin** 15:41 Like the document load.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 15:45 Yeah, so… I think our stance should be, not to use the document load, spans. And instead use… Use the events, the navigation events.
Unless anyone has, like, a strong opinion or use case for using spans, but I don't… you know, I think originally that document… that instrumentation was using spans because we didn't have, events at that point.
**Maxime Quentin** 16:15 Makes sense.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 16:18 I'm…
**Joaquin** 16:19 I have to review it, because it's been a while since I've seen it, but I think it… May make sense to have a span that is… Like, the duration between the page starts to load and when it ends loading.
That makes sense as an SPAN, but if there is any SPAN event related that is being created right now, we should follow the same principles that we did for resource timing and Fetch, which is… We create a log that has the spam as a context.
I, yeah, I thought to review what we currently have.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 16:59 So Joaquin, are you saying that you think it's useful to have Spans, or trace that you… that shows the document load span?
**Joaquin** 17:09 Well, if we're going to… have a telemetry about duration, I think it makes sense to have a span.
I think we discussed this a while ago, like, do we have… do we want to have attributes that is, like, duration in a log?
Or do we have to have an actual span with federation?
Yeah. And, I think… We will be nicer to collectors if we emit a spam when we care about the duration of something.
Instead of having a log, because the log, you have to manually see the attribute that Explains the duration for something, instead of having a span that is actually alteration.
So, but I have to review what the currently document… instrumentation is doing.
To see whether it still makes sense for it to be a spawn, because if it's just us.
If it's just using a spam to group spam events, then we don't need it, but if we actually care about the duration of the spam, then in that case, maybe it makes sense to use a combination.
**Maxime Quentin** 18:14 Could we have a new event like document loaded ended on top of the navigation timings?
Rosa's having a span? I mean… So what I'm waiting for first, like, on which trace do you plug the spam?
Like, do you need a trace ID? Is it something that… Just like a spine on its own.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 18:38 Yeah, I mean, that's my biggest counterpoint, I guess, is that, like, currently that document span cannot connect to any other spans.
So you essentially just end up with being… having traces with just one span.
And we also have… we do emit the navigation timing event, which has all of the, you know, timing data in it.
**Maxime Quentin** 19:00 Great.
**Joaquin** 19:00 I guess that's the question.
Sorry.
**Cleo Schneider** 19:03 One thing that's interesting here is that for document load, I feel like from a customer perspective, like, the thing you care about is not looking at any individual load. Like, that isn't actually… nearly as useful. Like, maybe there's one big slow document load, okay, but you maybe don't care about that one, you care about it over time. So, really, to me, it's more of a metric, right? You care about the histogram of those document loads, and whether or not, you know, like, what's my P50 for this particular page, or P90, or whatever. And so… I think when a span To me, the utility is really looking at an individual trace to say, I want to see what went wrong here.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 19:53 Right.
**Cleo Schneider** 19:53 The fact that it's not connected means that it's maybe a little less useful. And I think the fact that you can't see it over time makes it even less useful. So to me, span and log are maybe not… are both not great fits for this, it's kind of a metric, but I think there are enough collectors that use logs for analytics.
That, to me, it maybe makes more sense as a law.
**Maxime Quentin** 20:20 Yeah, I agree. I mean, there are the vitals, the web vitals, too, so that also kind of… Metrics as logs.
Maybe it would make sense to have a new vital on top of the existing one, and that would be, like, document loaded, Awesome seeing as that, and… Tag it as a vital.
**Joaquin** 20:45 Yeah, if… If that's a… way, like, I'm not really familiar with collectors, I've always been on this side of the street, so if logs as metrics is something that is standard and nice to collectors, then I will be fine with that.
I'm just saying that I was thinking that a span maybe is easier on the collector side, but… If the duration is fine as an attribute, then I'm okay with it.
**Cleo Schneider** 21:29 So I always put it out there and see how, see how it's received, you know?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 21:35 Yeah.
**Abinet** 21:35 And there is also one, on advantage of, like, having the trace for document load.
So it kind of tries to… Show the dependent, spawns, like, the… Document fetch and resource fetch spans are, like.
They are children of the document load span.
So you can see some, some more… Information regarding that, but if we are migrating to the new one.
How are the resource… I think the resources are, again, blocks, probably.
Are they emitted as logs? So we lose that kind of connection, but I don't know.
If the… If we can still achieve that.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 22:24 So is that… like, I thought… I thought that the document load span… Because it's constructed after the fact that it happens?
**Abinet** 22:34 Yeah.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 22:34 Cannot really be connected to anything.
**Abinet** 22:38 But it's already a parent of the document page and the resource page spans that are That's our meeting. Yeah.
**Joaquin** 22:49 That doesn't work automatically. Like you have to do something to connect.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 22:52 Yeah.
**Joaquin** 22:53 Right? Just by having the instrumentation is not enough.
**Abinet** 22:59 Yeah, what I mean is, like, the current documentary instrumentation does that, so do we… Can we get the same kind of feature?
Yeah. If you have music logs or something like that.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 23:12 I guess I would argue is that, like, those child spans that that instrumentation creates. are already covered in the navigation timing data anyway.
**Cleo Schneider** 23:25 And how is it setting the parent ID today?
**Abinet** 23:30 I think it's, when it creates the document load, and as a response, it creates them at load time, and then… It kind of creates them within a context, I think, within one.
**Cleo Schneider** 23:40 Yeah, because then we run into the same context propagation.
**Abinet** 23:42 Yeah, yeah.
**Joaquin** 23:49 I mean, the other option is to… follow a similar pattern that we did with Fetch, HHR, and Resource Timing.
I'm trying to use the same shared context, pattern, where… The document law will set the context, and then the navigation time will try to use that context when creating the navigation items.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 24:21 So, I've, you know, I'm not… I guess, like, if we find that it's… this is a feature that people want, that's useful, then we can think about that, maybe. I would say that, like, all of this can be accomplished by Just using the data from the events that we already met.
And it just like depends how it's how it's you know, processed in the back end in the collector.
But yeah, I mean, we could. We could consider this as as an you know. an alternative instrumentation, if that's useful for 2 people.
**Abinet** 25:00 Yeah, I think it can still be achieved, but So, like I said, the migration strategy is important because we cannot just consume This data in the same way that we used to do so.
Yeah.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 25:23 I don't know if we had, Like, I feel like we must have discussed this early on.
So I'll look to see if, like, if you have any, like, old issues about this, and if not, then… Then I'll take… I'll create one.
Alright, anything else, Sam?
Got a few more minutes.
**Maxime Quentin** 25:59 Good. Beside.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 26:02 Right.
Cool, alright, thanks everyone.
And I'll see you next week.
**Maxime Quentin** 26:07 Bye-bye.
**Cleo Schneider** 26:08 Thanks.
