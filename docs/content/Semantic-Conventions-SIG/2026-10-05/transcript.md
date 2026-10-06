SIG: Semantic Conventions SIG
Date: 2026-10-05
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Liudmila Molkova 00:02:38 Aloha, everybody.
Shawn Alpay (Linux Foundation) 00:02:40 Oh.
Liudmila Molkova 00:02:58 Okay, so let's give people a few minutes to join, and if you folks have any agenda items, please add them, and please add your name.
Single.
Josh is out today, Christoph is out today… Hopefully, oh, Dresco's here.
Should we add some conformance?
repo items here. Jay, do you think we need to discuss anything?
Jay DeLuca (Raintank, Inc. – Grafana Labs) 00:03:45 We could.
I, I have one thing that… I can talk about.
Liudmila Molkova 00:03:52 Cool, because I… I think, like, we… we don't use the… I'm here, but I probably have some topics.
Okay.
Yes, Sean, you can just add things to the Google Doc.
Go for it.
And… Here is the link.
Okay.
So, while we are waiting, let's take a quick look… And… What we have… In… Or… project board.
I still use Project Board for this repo, actually.
Not the PR dashboard, for some reason.
We have a bunch of things that need more approval.
And I think this, this friend is probably actually blocked, even though it has a lot of approvals.
On the spec change.
Oh.
I have some things for the RPC.
Probably miss.
Togo.
here.
And some other changes.
There is the big… PR from Network SEEK, Network Conventions SEEK, on restructuring the network docs.
I reviewed yesterday, it's in a good shape, I just suggested some minor… Changes, but it it's.
If you're interested, in network.
It's a good time to look at it.
It's also RPC, RPC, and once here… Okay, a lot of attributes are… related to system, or moving to RC. I think there are some final touches that need to land before It's merged, but it is coming.
Oh, and well… Didn't forget, let's talk… About release.
Okay, anything blocked that we can talk about?
For the old things.
We had some discussion last time about this, if I, I think I saw it in the notes.
Does anybody have the context on what happened here and why it was blocked?
Okay, then, let's…
Trask Stalnaker (Microsoft Corporation) 00:07:34 Nick Kelly.
Liudmila Molkova 00:07:38 Let me go here.
Trask Stalnaker (Microsoft Corporation) 00:07:39 Yeah, I think he was going to follow up with Robert to…
Michele Mancioppi (Dash0 Inc.) 00:07:44 I did follow up with Robert. Robert said, then we need a second POC.
Because the Java… The Java agent does not… it violates, some parts of the specs with respect to loggers.
Being, the severity of loggers being modifiable at runtime.
Open the POC, then you will see the comments there, right?
Liudmila Molkova 00:08:28 There.
Sorry, I didn't read the proposal. The proposal here is to Logo warning. Why do we need to change… Severity mountain?
Michele Mancioppi (Dash0 Inc.) 00:08:42 Because, what is going to happen the moment that you start with the auto-sync of exception opt-in?
And then, you do not… It's… it's a little bit… a little bit more convoluted. So, the… the auto-sancon exception signal obtained flag.
effectively states that You should fall back to emitting, log events if you cannot emit log records. Sorry, spend events if you cannot emit log records, yeah?
How do you know that you can automate log records?
You could have, for example, a no-op logger provider, or you may have muted the logs, where you're not printing anything, right? And, that flag, the way it is defined, technically, should react to changes in the logging configuration.
Which is, for example, not something that in the Java agent you can, you can observe.
And react upon.
For example…
Liudmila Molkova 00:09:51 You wanted to make a span event, and you could not.
Because this…
Michele Mancioppi (Dash0 Inc.) 00:09:58 around.
Liudmila Molkova 00:09:58 Table is set and OK.
Michele Mancioppi (Dash0 Inc.) 00:10:01 The other way around. So your instrumentations should be able to decide Based… so when the flag is in, an instrumentation, instead of creating a span event, should create a log record.
And, since the log records are a completely different pipeline.
You do not really know if that can work.
If you create a span, you can create a span event.
If you can create a span, it doesn't mean you can create a log record.
And, since the specifications state that The logging SDKs and the libraries should actually allow for the minimum log level to be configured.
Technically, the Java agent, this flag doesn't comply with that. So the POCID against the Java agent is considered invalid.
Liudmila Molkova 00:10:58 Okay, and then Robert is saying we need the second POC to demonstrate implementability.
Michele Mancioppi (Dash0 Inc.) 00:11:05 Yes.
Liudmila Molkova 00:11:06 Okay.
Trask Stalnaker (Microsoft Corporation) 00:11:09 McKellie, is it, so, I guess I was originally imagining this as a one-time, like, startup.
Warning.
But it sounds like that's not the case.
Michele Mancioppi (Dash0 Inc.) 00:11:25 I also saw it as a one-time startup warning Trask until Robert started pointing out that in the specs, it wasn't supposed to be like that, and actually, the implementation in the Java agent Even today, like, besides my code. It only really works at startup. The thing is saved in static variables.
That thing, the moment that you later configure, for example, a logo provider via OPAMP.
Is anyone gonna do anything about it?
Trask Stalnaker (Microsoft Corporation) 00:11:57 Right, but, like, is it… incorrect. Like, if we do emit the warning at startup.
Based on the configuration, I mean, It's correct at that time.
It's just, it might be incorrect later on.
Michele Mancioppi (Dash0 Inc.) 00:12:16 Exactly, and that is where a second aspect should come in. Like, if you… then, when the thing actually starts working.
Do you tell the user or not?
Trask Stalnaker (Microsoft Corporation) 00:12:29 I mean, so maybe… Can we just scope this down to a… like limit it some… Behaviors, basically scope it down to just a… one-time startup message. Not even… not even from the instrumentation.
Right, because the instrument… we have multiple instrumentations, we don't want to log it multiple times. It's more like almost a distro.
Michele Mancioppi (Dash0 Inc.) 00:13:00 Yeah, it's literally my PR Trask.
What you're proposing is a digital MIPR.
Trask Stalnaker (Microsoft Corporation) 00:13:07 The problem is, so how… where do we specify things about distros, is maybe… Part of the issue.
Michele Mancioppi (Dash0 Inc.) 00:13:18 I mean, this flag is specified in Semantic Conventions, and honestly.
Should not be in Semantic Conventions.
Should be in the, in the, specification rep, in my opinion.
There, we could go and say, okay, then if the logger changes, then you can go and do that.
I… to be honest, I do not.
Trask Stalnaker (Microsoft Corporation) 00:13:42 I don't see the reason to do anything with… Dynamic logger… Let's see, what's the… Let's read this here… So this says the instrumentation. So maybe we scope this… language down to… Distros.
and basically say, has… Distros… Can or should emit a one-time startup.
Michele Mancioppi (Dash0 Inc.) 00:14:28 Is this an official entity in, In the specific.
Trask Stalnaker (Microsoft Corporation) 00:14:32 No.
Well, I did. I think we have…
Liudmila Molkova 00:14:37 It's in the glossary.
Trask Stalnaker (Microsoft Corporation) 00:14:38 Telemetry distro name.
Michele Mancioppi (Dash0 Inc.) 00:14:39 Awesome.
Trask Stalnaker (Microsoft Corporation) 00:14:40 Yeah, we do have the… telemetry.distro.name.
Liudmila Molkova 00:14:47 Would that be… Fair to say that whenever something tries to emit a log record.
Regardless, what is it? Over the logger pipeline.
There should be a one-time… Warning that the logger pipeline is not configured.
Michele Mancioppi (Dash0 Inc.) 00:15:06 Sure, internal.
Liudmila Molkova 00:15:07 Okay.
Michele Mancioppi (Dash0 Inc.) 00:15:09 The, the, the moment that somebody tries to log, that is problematic, because you don't have a defined point of startup, and then you need to provide Either intercept the log as it is being created, which is a bucket of fun with log bridges and the like.
Or you, also, it's going to be unpredictable at which point in the startup process, if any, you're going to see that. That is not a great UX. Ideally, knowing it up front.
That would be better.
So the idea of the startup would work.
Liudmila Molkova 00:15:45 I mean, the instrumentation wouldn't know.
like, the logger provider is not configured, right? So it's the SDK that would know. Only the SDK.
Michele Mancioppi (Dash0 Inc.) 00:15:55 Yes.
Trask Stalnaker (Microsoft Corporation) 00:15:56 Right, we'd have to push that into the SDK itself.
Liudmila Molkova 00:16:00 And then it becomes not a question of whether you're trying to log the exception or anything. Like, why why why does it matter?
Trask Stalnaker (Microsoft Corporation) 00:16:10 We could have a D… I wouldn't want to do a warn.
Because that's, could be very… could be expected.
Michele Mancioppi (Dash0 Inc.) 00:16:20 Why? Why would it be expected? The moment you opt in for the, for having it as log records.
and it doesn't do it because some other part of your configuration is not working, I don't think we can assume it's intentionally like that.
Because then you set up an environment variable setting that has no effect.
Trask Stalnaker (Microsoft Corporation) 00:16:42 I thought… I think Ludmilla was talking about doing it generically in the logger. We're not looking at this environment variable.
But maybe I misunderstood.
Liudmila Molkova 00:16:54 Yeah, because it doesn't matter.
At the point where we know.
That logger provider is not configured.
It's a very generic place.
We can't probably look at this one.
But maybe, let's get back… let's reserve 4 more minutes for this discussion and try to identify the next steps. How would… Like, is there a component that would know?
That logger provider is not configured.
Except the SDK.
Michele Mancioppi (Dash0 Inc.) 00:17:30 I had a really hard time finding one in the Java agent.
To the extent that I actually went and created a logger and asked, hey, can you omit Warren or not?
Liudmila Molkova 00:17:46 And it doesn't mean it's not configurative if it's false, right?
Even if you say it's critical, it doesn't mean it's not configured. Maybe somebody just opted out of it completely.
Michele Mancioppi (Dash0 Inc.) 00:17:56 But… Since… so the, the way that the minimum… that this would be a war, yeah?
The, the exceptions that would go out on error… severity range error.
Yeah.
So, if you cannot do warning, you cannot do error.
Liudmila Molkova 00:18:16 Not necessarily.
Now, it doesn't, like, if somebody opted out of warnings, it's not the same as it's not configured, right?
Michele Mancioppi (Dash0 Inc.) 00:18:25 Right.
You're right.
Liudmila Molkova 00:18:30 The SDK now send the distro book might now.
Michele Mancioppi (Dash0 Inc.) 00:18:35 Actually, I did try, for example, by introspection to look if it was a no-op logger, logger provider.
And it felt finicky as heck.
Didn't feel…
Trask Stalnaker (Microsoft Corporation) 00:18:48 I'm not spec'd, so you wouldn't really be able to cross language.
Expect that.
Michele Mancioppi (Dash0 Inc.) 00:18:58 plaster out, like, 3 layers of wrapping around local providers in some SDKs, it's.
Go in there and find out the actual one behind, it's… Really difficult.
Liudmila Molkova 00:19:11 He said the distro at startup time would know, and SDK would know.
Michele Mancioppi (Dash0 Inc.) 00:19:16 Mmm.
Liudmila Molkova 00:19:17 And then it falls onto the distro.
or generic SDK.
And Distro can, I think, do the… Something specific for the exception.
span events, but the SDK probably shouldn't… the generic SDK would only be the… The signal that, okay, somebody's tried to log something, but I'm not supporting the signal.
Michele Mancioppi (Dash0 Inc.) 00:19:51 Interesting.
So, what you're… what you're implying is that I hooked in the wrong place in my POC?
And instead of putting it inside the Sankov exception signal thing that doesn't look at anything except the configurations, I should have hooked it in the configuration process for the Java agent.
Yeah.
Which means that we need to change from having data statically initialized.
So, as a static field in Java, to actually go and have it as an explicit step in the configuration provider.
Trask would they accept such a PR?
Trask Stalnaker (Microsoft Corporation) 00:20:37 I mean, I think that what I would focus on is the spec language.
Right, we… we have some, like, like, if the spec said distros should emit this warning one time on startup.
Then how we implement it in Java?
is… up to us.
Right? Like, your… I think your current implementation I forget, but I think it might be compliant with that already. We don't have to necessarily… so I would focus on the behave… speccing the behavior.
Michele Mancioppi (Dash0 Inc.) 00:21:18 No, my PR would not be, because it doesn't know that the logger is not set.
It does, it checks whether the logger can emit warn, but…
Trask Stalnaker (Microsoft Corporation) 00:21:29 Oh, okay, I see. Yeah, yeah, so then maybe we do need to move it, Into the actual distro.
Start up and look at the configuration.
Michele Mancioppi (Dash0 Inc.) 00:21:43 Yeah.
Trask Stalnaker (Microsoft Corporation) 00:21:46 It's all a bit tricky with the… I mean, but maybe we could… Tie it to declarative configuration, because that's a little bit more… .
clear, like, there's actual hook that all the SDKs get the whole declarative configuration And so, that might be the more reliable place to… emit that warning.
Michele Mancioppi (Dash0 Inc.) 00:22:12 We are not talking about declarative configuration as in the yaml, right?
Trask Stalnaker (Microsoft Corporation) 00:22:16 Yeah, yeah, yeah.
Michele Mancioppi (Dash0 Inc.) 00:22:19 That doesn't… Fitting my hat, because this is an environment variable.
Trask Stalnaker (Microsoft Corporation) 00:22:25 Yeah, but we should, if we don't already, we should have a YAML equivalent for it.
Michele Mancioppi (Dash0 Inc.) 00:22:32 But then that means that we need to remove the environment variable from the SEMCOMS.
Because if you.
Trask Stalnaker (Microsoft Corporation) 00:22:38 forward.
Michele Mancioppi (Dash0 Inc.) 00:22:39 It's supposed to work on the clarity conflict and environment. I mean, the moment you set up the clarity conflict, the configuration by environment is supposed not to happen.
Trask Stalnaker (Microsoft Corporation) 00:22:49 Yeah.
Liudmila Molkova 00:22:52 Oh, yeah, good point. So, sorry, calling time on this, I think the… The issue we're discussing belongs in the spec, and then we can continue tomorrow.
On the spec call.
Michele Mancioppi (Dash0 Inc.) 00:23:08 I would appreciate if we could actually, the three of us, take some time and discuss it offline instead of bringing it in the whole round of the specs.
Because it makes some discussions, especially if there is not a strong proposal on the table yet, it makes some discussions frankly difficult.
Liudmila Molkova 00:23:26 We have a…
Trask Stalnaker (Microsoft Corporation) 00:23:27 need Robert.
Liudmila Molkova 00:23:28 Yeah, maybe we can, Michele, if you can join, we have a login call dedicated 10 a.m. Pacific tomorrow, 2 hours after the spec call. Oh, 1 hour after the spec call. Maybe we can use this time, since it's on the calendar, tomorrow to discuss. And Robert.
Michele Mancioppi (Dash0 Inc.) 00:23:47 I cannot promise that.
It's a bad time in Europe.
Liudmila Molkova 00:23:52 Yeah, I know, sorry.
Trask Stalnaker (Microsoft Corporation) 00:23:55 Why not in the spec meeting?
Michele Mancioppi (Dash0 Inc.) 00:23:58 Too many people, too many kitchen, too many cooks in the kitchen until we have a good idea of what we want to propose Trask.
Then, at the… There are, like, a million comments on the PR, and then it gets sandbagged, just because of the sheer weight of… All the points to comment upon.
Liudmila Molkova 00:24:20 Can we try? We probably won't get anything on the calendar today anyway.
Michele Mancioppi (Dash0 Inc.) 00:24:25 Feel free to try with me.
Liudmila Molkova 00:24:32 Okay, let's try, and if… if it would not be constructive for…
Michele Mancioppi (Dash0 Inc.) 00:24:38 Oh, they're very constructive discussions, it's just that everybody has a different opinion.
They're super constructive.
Liudmila Molkova 00:24:46 We'll get straight, don't worry.
Okay, moving on, to the next topic. I… send a bunch of, PRs, sorry for spamming, but they are very similar.
Most of them, or… Trivial.
For the transition to V2, this is for entities, and… Some of them are a little bit controversial, but maybe not. So, the problem today, our entities don't have, many of them don't have identifying or descriptive attributes defined.
And they had this warning.
And the goal, is to eventually transition them to V2, and in order to do this, they would have to have strictly, strict separation between identity and description.
So this is an attempt to mark attributes.
In this way. And I'm showing some maybe controversial PR that Mark's user agent original is identifying for browser.
But that's the only change. All the markdown you see is just resorting, because the identifying attribute appears first, and then you just shuffle.
Trask Stalnaker (Microsoft Corporation) 00:26:15 Is there… is there a way we could do the mechanical changes without… Identify… naming identifying attributes.
Liudmila Molkova 00:26:26 Mechanical.
Trask Stalnaker (Microsoft Corporation) 00:26:27 I mean, could we do this PR and leave them all as descriptive as a first?
Like, make an exception somehow.
So we could…
Liudmila Molkova 00:26:39 Oh.
Trask Stalnaker (Microsoft Corporation) 00:26:40 All these mechanical changes in without, because it'll I mean, yes, you did open up a this one is probably a big can of worms.
this particular…
Liudmila Molkova 00:26:52 Unfortunately, not the worst one. So you're saying just mark them all as descriptive and then what and like figure out how in Weaver work it around so it doesn't complain.
Trask Stalnaker (Microsoft Corporation) 00:27:07 Yeah.
Liudmila Molkova 00:27:08 Mmm.
What benefit would it have?
Trask Stalnaker (Microsoft Corporation) 00:27:11 We get to schema V2.
Liudmila Molkova 00:27:16 Oh, okay, so… special case, something in the schema V2, so it allows the.
Trask Stalnaker (Microsoft Corporation) 00:27:23 Sort of like a backwards compatibility.
Liudmila Molkova 00:27:29 Okay.
I see.
Let me think about it, How we can do this so it's allowed for the old things, but… Not allowed for the new.
Umm.
Trask Stalnaker (Microsoft Corporation) 00:27:50 Yeah, if it doesn't work or not worth it, then that's fine. Just, I would love to be able to just blanket approve all the V2 schema migrations.
But… With… when there's contentious… or… confusing, or… Yeah, ambiguous things.
Then… I think that's gonna slow those down quite a lot.
Liudmila Molkova 00:28:29 Okay, let me see,
Trask Stalnaker (Microsoft Corporation) 00:28:37 And maybe that's not working.
As you say, maybe there's just not that strong of a benefit to getting those ones to V2 quickly, and we can get the other ones that are… we can get the ones that are clearer.
to V2, and… Let browser and maybe a couple others.
Wait for the…
Liudmila Molkova 00:28:59 Oh, I see. I'm, like… The.
The problem here is that we need to move.
Everything to the state that's compatible with V2 before we can move.
Like, the output to V2?
Otherwise, it would be… the output would be invalid, or we wouldn't be able to produce it.
And, I my view on this was that okay, these are development entities.
They are already invalid by saying something is identifying.
We are not saying it's set in stone. We're saying, okay, they were invalid, now they are valid.
Trask Stalnaker (Microsoft Corporation) 00:29:40 Like…
Liudmila Molkova 00:29:41 Like, they are semantically… no, not… they are schema-wise, they're correct.
Semantic suite, we don't know. It's… it doesn't move the status quo.
Trask Stalnaker (Microsoft Corporation) 00:29:52 That's fair.
Liudmila Molkova 00:29:54 But maybe, okay, let's focus on the non-controversial ones, and there are, I think, plenty of them.
I'll… For the general group, I'll probably post them on Semantic Conventions channel because there are like 10 of them.
I want to maybe it will add a data point to our analysis. There are a couple that are just completely wrong.
And, So, for example, there we had the AWS log entity. It is not an entity, it's a group of attributes that are set on resources.
Where… sorry, this is CS.
And.
Oh, sorry, I'm…
Trask Stalnaker (Microsoft Corporation) 00:31:08 That makes sense, so you just removed them as they're not entities anymore.
Liudmila Molkova 00:31:14 Y- yes.
And, for this one.
And the other one is… it was the… just a list of different entities, and I split them up.
It can be an argument in both directions, so, like, it's another controversial change, and we don't really have a group of people that can Say if it's a right or wrong choice.
And… We can say… That, okay, let's push it away and allow invalid things for now.
And.
But it also could be an argument in the sense that, okay, let's do it all just a little bit better.
I think if there are problems, they're obvious, at least.
Trask Stalnaker (Microsoft Corporation) 00:32:05 Makes sense.
Liudmila Molkova 00:32:06 Okay, anyway, I'll post a list of what I think is non-controversial, and I'll try to get approvals for, like, things like browser, and we'll see, like, in a week.
From today, we'll see how far we can go.
Where's this?
Okay, Let's move on to the next topic. Lewis, AI instance.
Should I present? Do you want to present?
Lewis Lewis 00:32:36 It's completely fine if you want to present.
So… Hello, I'm back. I've previously came to talk about the service instance, and what would be the right value for it for Azure. We ended up using the website instance ID, which is what's used as instance in an Azure application.
Performance monitoring, Azure Insights.
So, other than Azure Insights, there is also the Azure Metrics Monitor in OTEL, the Azure Monitor Receiver, which gets metric data, which emits instance as a different value.
And not just a different value, but a different value that behaves differently across different types of Azure App Service hosting plants.
So, I have come here to say I am not sure what semantic convention this should be.
Please give me advice.
I would like to be able to have this so that we can match behavior from the resources to the metrics.
But yeah, it's reasonably inconsistent and confusing.
So if you're… what you're scrolling past now is all the screenshots of 3 different ways it behaves. There's also a little table at the end, which might be good.
Yes.
So… in some places, this is a host?
In some places, this is, you can get this from the value called computer name, and in some cases, it is a pod or container name. And as you can see, there's some variations in how it's formatted also.
Computer name, as far as I can tell, is a Windows value.
which still appears on the Azure App Service Linux plans, I assume, so that they can continue to export this metric with a consistent tagging, so long as it's not on Flex.
Yes. So… I thought, in some places, this is a host, but it doesn't actually seem like it makes sense as a host, because it's not a host everywhere.
This is similar to the service instance ID, and usually changes at the same place, but it's not really a service-level attribute, because it's kind of specific to Azure App Services, as far as I can tell.
Not that I would consider myself an expert in… everything Azure has ever released.
And, it does seem to be related to the App Service plan, which is a thing that's shared by anything that's hosted on Azure App Service.
Which includes Logic Apps and a couple of other things.
So, that was what seemed to me like the best idea, but like I said.
Please advise.
There's questions I can try to answer questions.
Liudmila Molkova 00:35:37 Yes, sorry, I missed the beginning. What… which attribute we're trying to set?
Lewis Lewis 00:35:44 So, I don't know what… there is a value.
And this value is exported from the Azure Monitoring Hotel?
Resource detector, as instance.
There's a different value that's used as instance in, Azure Insights.
So we have these two instance values. One of them, we already know, or we have already agreed, Trask was really helpful in this, as what it should be set as in Semantic Conventions. That leaves no space for this other one.
That I can identify.
But basically, this is a way of matching The instance to the metric.
Trask Stalnaker (Microsoft Corporation) 00:36:33 And so this is, So I'm trying to understand why we need… This… an attribute, so I see your attribute.
like, example, so for example, appserviceplan.instance.id, you're kind of trying to figure out Can we put all this different data into one consistent attribute?
Lewis Lewis 00:36:57 This attribute is used as one consistent attribute.
As the instance on the metric.
In Azure.
Trask Stalnaker (Microsoft Corporation) 00:37:05 And so right now, so the… this is the collector-receiver that is… taking all of these different data sources and pushing them to Azure Monitor under the instance.
Dimension.
Lewis Lewis 00:37:27 What I would say is I am trying to match things that are not metrics.
Right?
That are coming from the resource to things that are to the metric for that thing.
Right?
And on that metric.
I can match it at the resource level?
But I can't match it at the instance level.
Because… we have a different value, for instance.
Because there are these two different instance values that behave differently.
And have completely different formats, and… The other one behaves consistently, and this one has multiple formats depending on your hosting plan.
Trask Stalnaker (Microsoft Corporation) 00:38:15 And was that a.
The… a decision made just in the collector-receiver of, like, what things to push into this instance?
Lewis Lewis 00:38:27 No.
Trask Stalnaker (Microsoft Corporation) 00:38:28 mentioned.
Lewis Lewis 00:38:29 So Azure does this. The screenshots I'm showing are actually directly from Azure.
Trask Stalnaker (Microsoft Corporation) 00:38:34 Oh, okay. Thanks.
Lewis Lewis 00:38:38 I would never… if this was just an OTEL, I don't think you guys would have ever done anything this inconsistent.
Like, these are from Azure… the Azure Metrics page. I could pull them up in Azure right now if you want to see.
Trask Stalnaker (Microsoft Corporation) 00:38:58 Okay. Which aren't coming from the collector at all. Nothing to do with OpenTelemetry. Gotcha.
Lewis Lewis 00:39:05 Collector… The Azure Monitor exporter in OTEL does export this value, I assume, because it's getting it right off the metric, which is from Azure.
Trask Stalnaker (Microsoft Corporation) 00:39:16 Oh, okay.
Lewis Lewis 00:39:18 Yeah. So, this is in Azure, this is in OTEL, this is not in the resource detector.
Trask Stalnaker (Microsoft Corporation) 00:39:25 Okay.
And so you want to introduce something in OpenTelemetry Semantic Conventions.
Lewis Lewis 00:39:38 sort.
Trask Stalnaker (Microsoft Corporation) 00:39:39 back, backwards… Back compat for… I'm trying to think how to say that.
Lewis Lewis 00:39:49 I would love to use an existing value if there is an appropriate one. I do not know what that would be.
Trask Stalnaker (Microsoft Corporation) 00:39:58 Because instance ID is already something different.
Lewis Lewis 00:40:04 Which is also an instance ID, and that one behaves consistently, and it seems like… and is used in a different Azure monitoring context.
You can't replace that one, because it's also used. There's just two.
Michele Mancioppi (Dash0 Inc.) 00:40:19 Wait, isn't it actually a cloud resource? Ready?
Liudmila Molkova 00:40:30 The code resource ID would be the resource, right? Not the instance in the resource.
Lewis Lewis 00:40:36 I believe the cloud resource ID is a combination of the subscription and the resource group and the app name.
Which is very human-readable compared to this value.
Michele Mancioppi (Dash0 Inc.) 00:40:51 So, the way, for example, that cloud resource IDs work on AWS.
Is that… it's, it's, it's effectively the ARN, right? And there is an example for Azure.
if you go back to Cloud Resource ID, there is in the examples, and it shows the path, the subscription path, right? So here, if you scroll to the right, you will see the… A very long thing.
Why does this not work in your case? I do not understand.
Lewis Lewis 00:41:27 The value that I am trying to match to the metric is not included in any of these constants.
Those are all human readable values. That is the correct format for the resource group. Everyone uses that as the resource ID. Sorry, the resource ID, not the resource group.
I would not add this value there. That would break everyone who is using the resource ID in its current format.
Liudmila Molkova 00:41:52 Yeah, and it doesn't have the resolution.
The multiple functions has multiple instances.
Lewis Lewis 00:42:00 You can put multiple things in this.
Under this, yeah, that's also true.
Michele Mancioppi (Dash0 Inc.) 00:42:06 But if it is… so function, are you talking about Azure Function now?
Lewis Lewis 00:42:11 Some Azure functions are hosted on Azure App Services. So, one of the reasons that one of the options I describe here is calling it on an app service plan.
It's because an app service plan can contain functions, app services, logic apps.
I think API services also? I'm not entirely sure what those are. I have to look into that more. But basically, Azure App Service infrastructure hosts things that Azure considers different cloud services, is my understanding, and differentiates them by things like what metrics they send, and some… Various environment variables that sometimes aren't even there.
Michele Mancioppi (Dash0 Inc.) 00:42:53 And using fast instance in this case, fast instance ID in this case is not appropriate.
Lewis Lewis 00:42:59 Fast instance is already used for the other instance ID, the one that's used by, Azure Application Insights. So, like, if you look at this first screenshot, you see where there's machine name and instance ID?
Michele Mancioppi (Dash0 Inc.) 00:43:11 Yeah.
Lewis Lewis 00:43:12 Fast instance is instance ID. The problem that I'm having is that the metrics are exporting the machine name as the instance ID.
Liudmila Molkova 00:43:23 So what are they calling it?
I might not understand the problem completely, but it sounds like there is the source of Consistent information available.
And there is a source that is inconsistent, and we want to capture both. Do we need to capture both? Can we just capture the consistent one as instance and just drop the other one for the time being?
Lewis Lewis 00:43:50 And that is…
Liudmila Molkova 00:43:51 another one.
Lewis Lewis 00:43:52 That is what you're currently doing, so you could do that.
But because the metric is exporting this other value.
I will not be able to match to metrics.
Liudmila Molkova 00:44:03 Oh, I see, and the metrics are in… I see, okay.
Lewis Lewis 00:44:07 Yeah.
And that's coming directly from Azure. That's not an OTEL choice, that's an Azure-specific thing. I don't think you could not do that on the metric, because Azure splits the metric by this instance value.
Liudmila Molkova 00:44:21 And what you're suggesting is to maybe give it, like, either you use existing attribute or give it some other attribute.
To capture that information.
Lewis Lewis 00:44:30 So you can match metrics to resources, which I think is a… pretty normal observability desire.
Liudmila Molkova 00:44:36 I see, yeah. And then the question is, what is the… Essentially, what's the attribute name for this thing that we have to capture?
I see.
Lewis Lewis 00:44:46 the So… One of the interesting things about App Service Plan is that an App Service Plan is, in its own way, a resource.
You could put a resource detector on this, you can add other descriptions there that are useful to the end user, like the plan tier.
And then if you have the planned tier there, you can, for example, see how this inconsistent behavior of the format of this value Well, really, it's consistent behavior. It's consistent per plan type, right? You can then see that extra dimension and say, yes, my dedicated apps are giving me this information format, and my flex apps are giving me that information. I understand now.
Or that might also be useful for cost, etc.
Michele Mancioppi (Dash0 Inc.) 00:45:34 Yes, please.
Wouldn't this be a very good use case for cloud provider Semantic Conventions the way we have them for AWS and GCP?
Lewis Lewis 00:45:45 I think I actually even call out a GCP example in my, brief here, which is, the instance name.
But.
Yes, so… I agree with that.
Michele Mancioppi (Dash0 Inc.) 00:46:00 For example, something that I could imagine could work… I mean, for these things, effectively, it's Azure deciding what should happen, right?
Have you folks considered publishing a Weaver registry with how you annotate the telemetry and the shape of the telemetry?
I have not…
Lewis Lewis 00:46:18 Private Azure?
Oh, okay.
Michele Mancioppi (Dash0 Inc.) 00:46:21 Alright.
Liudmila Molkova 00:46:24 Trask, have you considered?
Michele Mancioppi (Dash0 Inc.) 00:46:26 the.
Trask Stalnaker (Microsoft Corporation) 00:46:30 That would be amazing.
Someday.
Michele Mancioppi (Dash0 Inc.) 00:46:36 Having trust. Tashneer is doing that.
Why don't you?
Trask Stalnaker (Microsoft Corporation) 00:46:43 I mean, I think in this case, the kind of the example you have here.
makes sense to me. I don't know if it's .id or .name, but you're basically… Saying, hey, there's a value that is captured, it's… by Azure, and I just want a name for that value, and here's the definition of that value.
It's not really something that we would… It's sort of reverse engineering the… from… But I'm… it's interesting there's actually… it looks almost identical, no, to that GCP instance name.
at the visible name of the instance in the UI.
That's essentially the same thing that you're describing, right?
Lewis Lewis 00:47:37 I mean… So.
There's a Process Explorer screenshot in here where it actually uses both instance IDs, so just depending on where you are in the UI, you will see one or the other of these.
Trask Stalnaker (Microsoft Corporation) 00:47:52 Okay.
But so, more specifically.
As defined by the, where it's the metric, the instance used in the metric.
Lewis Lewis 00:48:04 Yes.
Trask Stalnaker (Microsoft Corporation) 00:48:05 I.
Lewis Lewis 00:48:05 you.
Trask Stalnaker (Microsoft Corporation) 00:48:07 I… Seems very reasonable to me.
Lewis Lewis 00:48:10 Okay, would you guys like me to go ahead with this issue, or do you want me to write something up about trying to capture as much of the app service plan information as I can separately from this?
Because I am completely happy to do that.
If you guys think that would be a useful thing to have in the backlog or otherwise.
Trask Stalnaker (Microsoft Corporation) 00:48:32 In general, smaller chunks are easier for us to get merged.
Lewis Lewis 00:48:38 So I figured, I'm completely fine with that. Thank you for considering this.
Trask Stalnaker (Microsoft Corporation) 00:48:42 Yeah, and if you can put up a prototype or something in the, you know, collector contribute something. Where would it fit in… that.
Oh, it would be exporting that value.
Lewis Lewis 00:49:00 Directly? Yeah, it might need to be in a couple places because of how the Azure App Service infrastructure is used.
But I will… Build as many test apps, and come up with some prototypes, and post more screenshots.
I've gone through this process a little bit now, so I can do it.
Michele Mancioppi (Dash0 Inc.) 00:49:21 There is technically the, there are a couple of Azure receivers where this could be exposed, right?
Lewis Lewis 00:49:27 that's.
Trask Stalnaker (Microsoft Corporation) 00:49:30 Yeah, my initial, preference leaning towards, the dot name, just… Matching the GCP attribute seems very similar.
But I don't know. I mean, ID… ID… Sounds a little bit more formal, like, and as you said, it's not… Yeah, I don't know.
Lewis Lewis 00:49:56 We also have the option of, machine name, which is what some of the Azure interfaces are calling it, if we wanted to be specific.
Trask Stalnaker (Microsoft Corporation) 00:50:07 Is it machine name?
Lewis Lewis 00:50:10 In some of the interfaces, it is labeled as machine name.
What machine name means exactly, I can't answer since I am not at Azure.
Trask Stalnaker (Microsoft Corporation) 00:50:20 Okay.
Michele Mancioppi (Dash0 Inc.) 00:50:22 By the way, why did we call it cloud.resource underscore ID instead of cloud.resource.id?
Liudmila Molkova 00:50:29 No, not really. We should rename, but yeah.
Trask Stalnaker (Microsoft Corporation) 00:50:35 predated us.
Liudmila Molkova 00:50:37 Yeah, yeah.
Trask Stalnaker (Microsoft Corporation) 00:50:40 Yeah.
Liudmila Molkova 00:50:42 We have 10 minutes left, and two important topics on one note.
Lewis Lewis 00:50:49 Good with any other discussion on being on the issue. I can stop.
Liudmila Molkova 00:50:55 Awesome. Thank you.
Jay, are you sure we can skip it?
Jay DeLuca (Raintank, Inc. – Grafana Labs) 00:51:02 Yeah, mostly I was just saying that the, the automation that I've set up for the aggregating of the data, we had the first run succeed, I had to fix some permissions bugs. I'm gonna continue to clean this up a little bit, but… Basically, this will keep the UI updated overnight. And then one other just quick note is I was talking to somebody about… they were trying to interpret the results compared to what they were seeing with their app.
And I think there was some confusion because a lot of our runs require an environment variable to be set in order for the them to actually be compliant, like the SEMCONF opt-in. And I just don't think that's currently obvious, so I'm gonna also… update the UI to make it clear.
When someone can expect to see that information.
And then just one other note, I'm also working on trying to incorporate some of the provenance, so, like, identifying which versions of the instrumentations are used.
It's turning out to be a little bit more complex than I thought. It might require some small changes to the directory structures and conformance files, but I think it's doable. But yeah, I think that's it. I think we can move on to the other items.
Liudmila Molkova 00:52:10 Do you, like, I would love… I think very few people saw the UI.
Maybe it's not the case, but it's my impression. Maybe we should plan for some demo in this call or maybe even in this back call.
Jay DeLuca (Raintank, Inc. – Grafana Labs) 00:52:28 Yeah, I mean, I was, I would like to get at least one more view out that shows, like, kind of digging into an individual instrumentation and seeing the actual findings. I think that makes it all a little bit more, end-to-end useful, so maybe once I implement that, we can… we can plan for the demo.
Liudmila Molkova 00:52:46 Okay.
And I… I shouldn't… I think we should put it in the spec call, like, where we have project updates. This is effectively an amazing project update.
Jay DeLuca (Raintank, Inc. – Grafana Labs) 00:52:56 Okay, sounds good.
Liudmila Molkova 00:52:58 Yeah, thank you.
Jay DeLuca (Raintank, Inc. – Grafana Labs) 00:53:00 No problem.
And just one other note, I thought it was awesome last night, the, the PR updated the Java agent to the latest release, and it, it showed a bunch of the findings from the previous version disappearing. So, great work, Trask.
Liudmila Molkova 00:53:16 you.
Trask Stalnaker (Microsoft Corporation) 00:53:18 Yay!
Liudmila Molkova 00:53:20 Nice.
Awesome.
Trask Stalnaker (Microsoft Corporation) 00:53:22 Performance repo is, yeah, is a good feedback loop.
Jay DeLuca (Raintank, Inc. – Grafana Labs) 00:53:27 Yeah, love it.
Liudmila Molkova 00:53:29 Cool. Moving on, Sean, do you want to talk about focus partnership?
Shawn Alpay (Linux Foundation) 00:53:35 Yes. Hi. So I am, Shawn Alpay. I work as a director of data engineering at the Linux Foundation. I've been working, more specifically at the FinOps Foundation for the last couple of years.
I became a member of the Focus Project, which is the FinOps open cost and usage specifications for an open format for billing data. I became the working group chair about 2 years ago, and we have had several releases. We're on a twice-year release schedule.
And you may have heard about the Tokenomics Foundation, which was just stood up in June, which is now driving towards token economics and AI economics, and so this becomes an important time for us to be able to take our billing data and glue it together with observability data, telemetry data, to be able to tell the story of unit economics or token economics. So, thus why I'm here. We have heard from many of our practitioners.
who need this data, and I very much do not want to build it ourselves. There's no reason to do that when OpenTelemetry exists. And we have a partnership with most of the organizations that are on this call, like.
Google supports us, Grafana supports us, AWS supports us, Microsoft supports us, Dynatrace, I believe we're in conversation with. Anyway, there are dozens of data generators in the Focus ecosystem, and so my goal here, and why I'm in this call, is to get some… start the ball rolling, getting some basic guidance on How do you go from 0 to 1 on standing up a new telemetry schema? Maybe you have some docs, maybe you don't. Maybe it's been white glove partnerships, but I want to do the necessary, and I want to do it right, to be able to get from where we are to having my vision being a new telemetry schema called Focus.
So I'm sure there's a lot of stuff to cover there. Obviously, we can't cover it all here, but I'm looking for a guide, a person, someone who can help me start that process, understand what the process is, because I don't have clarity there at first.
And then walk me through all the things that I and a task force that will stand up in our working group will need to do in order to get all the way to the promised land of that data being generated by data generators.
Liudmila Molkova 00:55:50 Wonderful. Thank you for the intro. I have a bunch of questions, but do you have any links, like, for people to go and take a look?
Shawn Alpay (Linux Foundation) 00:55:58 Yeah, of course. Let me, I mean, first of all, the just the main splash page for focus would be this. I'll put it in the chat.
our repo. I will also put that in the chat.
Stand by.
There's our repo.
And so, you know, if you want to understand what our our solution is so far, it is a Small handful of data sets, the main one being cost and usage data.
Which tells you the story of what did you use and how much did it cost.
But that, of course, doesn't tell you the whole story. It doesn't tell you what the CPU utilization was, or the memory utilization, not to mention what all the stuff you kicked off to generate the money you spent. So, the goal here would be take that cost and usage data on the focus side.
take telemetry data in hotel format and be able to put it together so that you can perform your unit economics or token economics use cases.
Liudmila Molkova 00:57:04 Cool. Okay, so then the, the… The thing you would like to end up having is the definition of the telemetry, like, the part where you're here.
the definition of the cost and usage telemetry in some, hopefully coherent way, so that you can correlate the CPU and the… corresponding costs and stuff. Cool. So… I think there are two… interesting parts. The first one, we would probably have some of the data, or some of the metrics in common. So, for example, token usage, we have it defined in Semantic Conventions Gen AI repo.
And you might also have them defined, and it would be interesting to see how far, how close we can come together in those definitions. But then there is a second part of, okay, whatever the schema you would like to have for your data, how do you… define it and own it, right? So you're interested in ownership for this, the schemas.
Awesome.
Shawn Alpay (Linux Foundation) 00:58:11 Certainly. Yeah. And and you know, our our task force will do the work. It's just a question of what the work is. And so we definitely want to have a partnership here. But I just I don't. I don't know the blocking and tackling yet of like.
what's the process by which we would get to the point of issuing a pull request against your repo? Like, what are the things… what are the… what are the things I need to do in order to get to that point, right? So, like.
I'm just… I'm looking for someone who could help sponsor this, that I could maybe have a one-on-one meeting with and talk through the next steps. Maybe it's you, maybe it's somebody else on this call, maybe it's somebody else, but… I just… I want to do this as efficiently as possible while also going through the proper procedures. I mean, I chair a working group in the Linux Foundation. I understand how these processes go, and I want to make sure that I adhere to the processes that you all have to move forward.
Liudmila Molkova 00:59:03 Yeah, I think that the first question is, I… I don't know… We were pushing back a little bit on adding things into this repo, because the process to, for things to land here is… we would have a SIG, it's a special interest group in OpenTelemetry, that would need, like, a little bit of diverse set of different companies.
And we would go through the project proposal, we would need a sponsorship from, like, OpenTelemetry, governance and technical committees.
And I think it could be doable, because Phenops is an important thing, and I, like.
it's my personal opinion, but I would imagine there is interest in this, and it can happen. This is, probably a little bit bureaucratic process, it would take some time, and it would be awesome to start it. But also.
you don't have to live in this repo. We did a thing that where we, federate… we federate. So, like, for example, we have this friend and a couple more like this, where we say, okay, we depend on OpenTelemetry Semantic Conventions.
But we don't, like, depend on the… This is the different ownership model.
And for your case, it might be that you would prefer to live in your own repo. And if it's up in telemetry, it's the same process as Semantic Conventions, it would be a SIG within OpenTelemetry, but it's… if it's part of, your project, then… It would be your repository, and then there is a question of how we can collaborate so we create something coherent together.
Shawn Alpay (Linux Foundation) 01:00:50 I want to do whatever is… is gonna be the most extensible. Like, I'm… I'm not… I'm not set on, like, quote-unquote, owning anything. I just want to… I want to make sure that we can move swiftly, so if this is something you think can help us move… keep our velocity up, then great. I just don't want to create any, like… I don't want to be a special child over here.
Trask Stalnaker (Microsoft Corporation) 01:01:10 I would highly recommend doing the federated Semantic Convention approach. Because you already have a governance body and people foundation.
Which is, you know, a perfect place for you to own, you know, vendor neutral, own that stuff already. I think that… that is our vision for the, federated Zack Miller, of federating the Semantic Conventions is to let those things grow out there, and not for our repo becomes a bottleneck for you, which is what unfortunately has happened in the past. And one, the reason, one of the main big reasons we've been pushing for federating here.
Shawn Alpay (Linux Foundation) 01:02:07 Okay, but I see here this is still an open telemetry. Like are you saying that I would go a step farther and it would be like in the focus organization or would it be here?
Trask Stalnaker (Microsoft Corporation) 01:02:15 Right.
No, it would actually be within your, GitHub org. So you would be able to… we have Tulene, and this is, we've… been doing this for, what, like, half a year now, so, it's still fairly new of, federating the Semantic Conventions, but you can definitely look at the Gen AI and the mainframe repos… And the… I think the browser also… we have a, repo here. But essentially, none of these… oh, it's client-side, I think. None of these are.
have to live in the OpenTelemetry org. They happen to live in the OpenTelemetry org because the SIGs That own them, and are OpenTelemetry SIGs, and this is the vendor-neutral body where, the people are coming for those.
Shawn Alpay (Linux Foundation) 01:03:24 So then I guess, and I know we're at time, so I don't want to take up too much more of your time, but what I'm craving next is like, what are my next steps? Like, what do I, I'm still not super clear.
what is the next few things that I and on my task force need to do in order to get to move forward, other than creating a repo? Like, okay, let's say we stand up our repo and we create our schema, then what? What happens then?
And I'm happy to meet with one of you later. We can schedule some other time if you prefer, but those are the kinds of questions I'm looking to answer.
Trask Stalnaker (Microsoft Corporation) 01:03:57 Yeah, why don't we… I mean, why don't we follow up next week, get, get your topic at the top of the agenda, we can pre-populate it there, we can spend some more time What I would do before then is take a look at the… like, you can spin up locally just, a repo for, you know, a federated SEMCOM repo, and kind of play around with that and get a sense from the technical side. I will say that's an area where we haven't then, we don't have a good answer yet of discoverability, right? That's, we want people to… but I mean, honestly, from your… like, you are… like, it's kind of like with… when GraphQL creates their federated Semantic Conventions.
Shawn Alpay (Linux Foundation) 01:04:47 Yes.
Trask Stalnaker (Microsoft Corporation) 01:04:48 Discovery isn't too big of a problem, because they are the body, like, but there… we still do need some pointers from OpenTelemetry out to them.
Shawn Alpay (Linux Foundation) 01:05:01 Definitely.
Well, I'll look through that stuff then, and then I'm happy to come back next.
next week. I'm going to be at Open Compute Project at the conference next week, so I don't know if I can come next week.
I will, go ahead.
Liudmila Molkova 01:05:21 You can ping us on the… in the Slack channel, and we can go on from there, but essentially, we'll be looking at you, like, you wanted the schema. We can, like, put a link to the schema, and.
You… we can show you what else to do, like the validation against the schema and stuff like this, but essentially, for the purposes of this group, like, you define semantic conventions, you have instrumentations, you are the owner of this thing, and we would love to work together and Like, try to eliminate any unnecessary, Conflict between Semantic Conventions and FinOps things.
Shawn Alpay (Linux Foundation) 01:06:05 That sounds good. I'll ping you on the Slack then, and we'll get going from there.
Liudmila Molkova 01:06:10 Awesome. Thank you for staying longer. See you next time, or whenever.
Shawn Alpay (Linux Foundation) 01:06:14 Alright, sounds good.
Trask Stalnaker (Microsoft Corporation) 01:06:15 Bye.
