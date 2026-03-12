SIG: Developer Experience SIG Meeting
Date: 2025-09-17
Duration: 44 minutes
============================================================

## Zoom Recording Transcript

**Damien Mathieu** 01:53 Hey!
**Tristan Sloughter** 01:55 Great.
Hopefully Bogdan can make it this week.
That's the only thing on the agenda, I guess.
**Damien Mathieu** 02:16 Sorry, the only thing on the agenda is… Oh, yes.
**Tristan Sloughter** 02:20 Interview with Bugdan.
**Damien Mathieu** 02:21 Yes.
**Tristan Sloughter** 02:23 Larry. Awesome.
Hey!
**Bogdan Stancu** 02:27 Well.
**Damien Mathieu** 02:28 Hey.
**Tristan Sloughter** 02:32 Good morning, Ern.
Yeah, is it still morning for everybody?
**Damien Mathieu** 02:36 It is here.
And…
**Bogdan Stancu** 02:39 That's it, it's 12.
So…
**Tristan Sloughter** 02:42 Good afternoon.
**Bogdan Stancu** 02:44 Interested.
**Damien Mathieu** 02:45 It's already morning for you, anyway, so…
**Tristan Sloughter** 02:49 Yeah.
**Damien Mathieu** 02:50 Or should we say goodnight?
**Bogdan Stancu** 02:54 What time is it? Where you are, Tristan?
**Tristan Sloughter** 02:56 It's 5, so it's morning.
**Bogdan Stancu** 02:58 Okay, yeah, well… I don't know how you manage.
**Damien Mathieu** 03:03 But you said it's noon, so that puts you, like, Eastern Europe?
**Bogdan Stancu** 03:09 Yeah, yeah. I mean, Romania.
**Damien Mathieu** 03:11 Okay.
**Tristan Sloughter** 03:16 Alright, yeah, the… I think the only thing we have was the interview, unless there was anything you wanted to talk about, Damien?
**Damien Mathieu** 03:25 I don't think so.
**Tristan Sloughter** 03:27 Okay.
Yeah, and…
**Bogdan Stancu** 03:30 One question before… before this. I just was curious how with the… how did you end up doing this, and how can people kind of help you? I mean, I would be interested in doing stuff in OpenTermetry other than PRs and reviews.
And I don't know what the track is there. I mean, not necessarily in this meeting, in general.
Like, how do people help with anything other than PRs?
**Tristan Sloughter** 04:00 Hoping help with OpenTelemetry just in general.
**Bogdan Stancu** 04:03 Yeah, I mean, with the project itself… I mean, I see you doing this, organizing the blog post.
That's not code, but it's still in the OpenTelementary realm.
**Tristan Sloughter** 04:16 Right.
**Bogdan Stancu** 04:17 Yeah.
**Damien Mathieu** 04:18 So, what I would do is, so if you go to the community repository in the OpenTelemetry org, you will see a list of all existing SIGs.
And so each SIG is responsible for one aspect, so some of them will be responsible for codes, like SDKs, collector.
But others have more either cross-cutting or, like, less code things.
So this is a SIG, like, it's the DevX one, and, like, just pick the SIG that interests you, and join their meetings.
**Bogdan Stancu** 04:56 Okay, so just what I'm doing right now, I guess. Because for the collective, for example, I guess you kind of show that… show interest by doing stuff.
But here, besides just joining the meeting, I… there are no… there are no tasks that anybody can do, so they can show interest. That's what…
**Damien Mathieu** 05:17 Yes, exactly.
**Bogdan Stancu** 05:17 That's why I was asking. Yeah, okay.
**Tristan Sloughter** 05:20 Yeah, yeah, here the… until we… unless we build up a backlog one day, yeah, it's just joining and bringing up ideas and… getting them… because there's, yeah, so few of us for things to do that we just keep it… keep it small, and just do things that we come up with them. And… and it's still fairly new, SIG, but… Yeah, maybe one day we'll have… Tasks that people can pick up, but, yeah, right now it's just joining.
**Damien Mathieu** 05:47 I mean, even if there are tasks that people can, can pick up, joining the meetings is always a good thing, just to know what the actual priorities are.
And if there's a task that says, we should be doing this, but it's more, like, long-term or unidal of where we want to go, maybe it's not the first thing to pick up.
**Bogdan Stancu** 06:11 Okay.
Cut it.
Thanks.
**Tristan Sloughter** 06:15 Yep. Then eventually, you can propose your own SIG through the community, repo. That's how, like, this one got started and stuff like that.
like a… it's also a PR. Everything's a PR.
Oh, yeah.
Good success.
**Bogdan Stancu** 06:33 Alright.
**Tristan Sloughter** 06:35 Yeah.
So yeah, guess we can get started. You saw… Do you see the outline for what we'd like to discuss?
**Bogdan Stancu** 06:47 Yeah, yeah, and I have… I've made the.
**Tristan Sloughter** 06:50 Oh.
**Bogdan Stancu** 06:51 let's say a presentation, I mean, it's not a presentation, it's just a list of slides that kind of match that outline, and I can share that with you, or I can just follow it, and we can talk on it, because it… besides some… Oat Hill Bins, it's… It's just… I don't know.
Nothing that we can just talk about.
**Tristan Sloughter** 07:16 I like some words, I can… I'm a…
**Bogdan Stancu** 07:18 Okay, the… within…
**Tristan Sloughter** 07:19 Visual sharing.
**Bogdan Stancu** 07:23 Would you like me to share the… I don't know if I can share the deck. I can download it and send it to you, or share the screen.
**Tristan Sloughter** 07:32 Oh, either one.
It's a LaTeX presentation?
**Bogdan Stancu** 07:37 What?
**Tristan Sloughter** 07:38 Where did you… do you say tech? Or text?
**Bogdan Stancu** 07:42 Text.
No, it's just… I didn't…
**Tristan Sloughter** 07:45 You just say it's tech. I was like, where you're not all out.
**Bogdan Stancu** 07:50 It was just for me to organize my thoughts, and In this, but I… we can, we can share that.
Share… this?
Does this work? Can you see it now?
**Tristan Sloughter** 08:09 Yup, perfect.
**Bogdan Stancu** 08:10 Yeah, okay.
**Tristan Sloughter** 08:11 Alright.
**Bogdan Stancu** 08:14 So again, Bogdan Stankhu, working for Adobe, software engineer.
And we're here, kind of, to… Discuss.
How we, deploy the whole pipeline.
Well, I don't have an actual presentation, I'm gonna wait for your questions, I just have this, Again, as a thing for me to organize my thoughts.
**Tristan Sloughter** 08:42 Okay, then we can, start with… The company's structure?
Can you give a little bit about, like, who works on the collector, deploys it, manages it? Is it a single team responsible for all the collectors in the company, or does each team… Manage their own, anything like that?
**Bogdan Stancu** 09:05 Yeah. So, I'm part of the observability team, which is… kind of the main team that is supposed to, provide observability in Adobe, but because we are so big, and… Adobe in general has acquired companies, and the… the merge hasn't been done completely. There are teams so big that Have their own observability team.
But we are the main one.
And what we provide.
is, oh, I, I can, I can describe this, this thing, this thing here, which is the… The whole, kind of, diagram.
Can you see my… my pointer?
**Tristan Sloughter** 09:53 I don't know. Yep.
**Bogdan Stancu** 09:54 Yeah, okay. So, in the left here is the user Helm chart. This thing is a Helm chart that users deploy, teams deploy, and they manage that. So, we just give it to them.
**Tristan Sloughter** 10:08 We don't touch it after that.
**Bogdan Stancu** 10:10 We can help, but we're not touching it.
Then there's this, namespace where we manage a bunch of collectors, and that's on us.
And I said before that this is a centralized one that we want to keep for filtering Stuff like that.
And then the backends, which we also keep.
So the product itself, is… I mean, what users use is this first Helm chart.
**Tristan Sloughter** 10:40 So I see that has a… it says collector in deployment mode as well. Does that mean they're… Sidecars are deploying to our, forwarding Express.
**Bogdan Stancu** 10:51 We're gonna get to that. But, yeah, well, the chart has… so we have the operator deployed everywhere.
**Tristan Sloughter** 10:59 Yep.
**Bogdan Stancu** 10:59 Every cluster has an operator deployed.
And the chart has two collectors, which are described here.
The design call collector, which is in the application pod, and that thing is configured to… get everything. It's not configurable. The user cannot touch this configuration, because we don't want them to change it and then restart the application.
So this thing exports everything.
Doesn't matter what the user wants.
Blogs, traces, metrics, everything.
again.
because we do not want the application to restart. This is… this has been designed like this, so… They're not changing it. And this thing sends to a collector in deployment mode, which they can configure through the values. We give them well, defaults. I mean, they don't really need to touch that values file at all, and the other instrumentation is gonna get stuff Extended to this… Namespace that we manage, and then to the backends.
So they don't really have to do anything. But they can.
We do have some support… other supported backends.
Configurable through the values, but they can also have just, kind of.
include their own config. Like, they have this portion where they can just paste an exporter, for example?
An exporter configuration, and it will just… copy-paste it in the config. And as long as it's in the contrib, it will work.
So we…
**Tristan Sloughter** 12:54 Goodbye.
**Bogdan Stancu** 12:55 No, no, the sidecar is… no, yeah, in the deployment.
**Tristan Sloughter** 13:00 That's a deployment.
**Bogdan Stancu** 13:01 Yeah, so if they decide to… they want to start sending metrics somewhere else, and they change something to the values file, just this, the deployment restarts.
**Tristan Sloughter** 13:11 Gotcha.
**Bogdan Stancu** 13:14 And, yeah, we have the default, which is our thing.
We have other… exporters that are in the chart, that are, like, many people use, but it's not the default, and then they can also do whatever. And at that point, we're not helping them, if they do that. Like, they can send to some crazy thing that contrib allows. It's a part of the Helm chart that just copies it over.
**Tristan Sloughter** 13:42 Okay.
**Bogdan Stancu** 13:45 Yeah.
I hope it makes sense, just… maybe I went too fast, I don't know.
**Tristan Sloughter** 13:55 No, I was… yeah, trying to take notes at the same time you're going fast on. The… So the… Did you go over the destination header? Because you… you said they could send both They could send OTLP to the deployment, which is the default, or they could configure their own.
Did they send?
**Bogdan Stancu** 14:14 It's still over OTLP, so we have…
**Tristan Sloughter** 14:16 Oh, it's still…
**Bogdan Stancu** 14:18 Yeah.
**Tristan Sloughter** 14:19 They're just configuring the destination header?
**Bogdan Stancu** 14:21 Yeah, which will be read in the… in our namespace, and then routed.
**Tristan Sloughter** 14:26 Okay.
**Bogdan Stancu** 14:27 Because even though we have I mean, we have multiple… Default backends for metrics, for example.
And they can choose which one it is. Because, I mean, that's the normal way and what we want people to use, is this chart sends to our managed namespace, and then our managed namespace sends to Whatever they have configured in this destination.
**Tristan Sloughter** 15:01 And is a destination header just a resource attribute?
**Bogdan Stancu** 15:05 It's a… it's a header in the.
**Tristan Sloughter** 15:07 There's something else.
**Bogdan Stancu** 15:08 Whoa.
**Tristan Sloughter** 15:08 Oh, wait, I have seen that, yeah. You can add HTTP headers to the…
**Bogdan Stancu** 15:12 Yeah, yeah. The OTLP exporter allows that.
**Tristan Sloughter** 15:16 Yep, yep.
**Bogdan Stancu** 15:20 This is the auto bin.
Or the sidecar.
**Tristan Sloughter** 15:25 Goodbye.
**Bogdan Stancu** 15:27 it's just… Well, I've deleted them.
some things, but this is the main part. This is just, getting some stuff, adding those, and sends over. So this is the sidecar, and as I said, these are all Always running.
It doesn't matter if the user wants logs, we're taking them, getting them to that deployment, and then maybe that one doesn't export them.
**Tristan Sloughter** 15:57 Just as a side note, because I think it… with the… Damian might know more, or definitely knows more about this. The batch processor's future…
**Bogdan Stancu** 16:08 Yeah, I know, I know, we know, we know, we know.
**Damien Mathieu** 16:11 Yeah, okay. It's not recommended to use it anymore.
**Bogdan Stancu** 16:14 I know.
**Tristan Sloughter** 16:15 I just don't want to include it in the… yeah.
**Bogdan Stancu** 16:17 Oh, yeah, yeah, we're working on that. It's, okay.
**Damien Mathieu** 16:20 I think we can include it, just… I mean, you're there, you're using it, just mentioned that you are planning on migrating.
**Tristan Sloughter** 16:29 Oh, yeah. If you… yeah.
Yeah, if… people we interview aren't moving off of it anytime soon. We'll have to include it, and we don't want to… pretend they're using something else that they're not. We gotta give the, you know… Real-world use, but… Just wanna make sure people aren't given… like, information they can't use anymore soon, but yeah.
Okay.
**Bogdan Stancu** 16:57 This is the one for the deployment, which is kind of the same.
**Tristan Sloughter** 17:00 Oh, good.
**Bogdan Stancu** 17:01 But… Again, this, the OTLP exporters, add the header.
And then…
**Tristan Sloughter** 17:10 mortgage.
**Bogdan Stancu** 17:14 So this is a slide for the managed namespace. Again, this is… these are sets of collectors that we manage.
And there's a deployment for each telemetry type.
So, there's separation.
If… if they're sending logs, and… Somehow, put the logs down, metrics still work.
**Tristan Sloughter** 17:42 Oh, wait, the… Did you say it's a separate deployment for each signal?
**Bogdan Stancu** 17:48 Yeah.
**Tristan Sloughter** 17:48 Oh, okay. Yeah, I'm gonna make a note of that, because that's… Not everybody does that.
**Bogdan Stancu** 17:55 And also, like, the… the backend can… reject.
The telemetry, for example, for metrics, maybe you're rate-limited, and the backend says no, and the queue builds up, so… the collector scale. We don't want that metrics behavior like this to affect logs or traces.
**Tristan Sloughter** 18:16 Okay.
**Bogdan Stancu** 18:20 Yeah, the autoimm for… oh, sorry.
**Tristan Sloughter** 18:24 You mentioned custom components, but is… and I know you have exporters, are there… Others in there that you can… Yeah, yeah, I agree.
**Bogdan Stancu** 18:34 Yeah, there's one that I wrote. We're gonna get to that and why. I mean, it was at the issues we've had, section. But yeah, And even if we didn't have custom components, we would use our own distribution just to avoid the necessary dependencies, like, just include what we actually use.
And these ones do the same. The ones in the user chart, they have to manually switch to contribute if they want to use a collector that's in contribib.
**Tristan Sloughter** 19:11 I'm good.
**Bogdan Stancu** 19:16 Total bin.
This is the routing processor that is, doing, The routing based on that header.
**Tristan Sloughter** 19:27 Okay.
**Bogdan Stancu** 19:29 And then on… I'm gonna get to the next… before that, is this fine until now?
**Tristan Sloughter** 19:39 Yeah. So, it can do the routing after batching? I don't know enough about the collector, because I thought that would… combined.
**Bogdan Stancu** 19:47 Yeah.
**Tristan Sloughter** 19:48 Without the header, since it's combining multiple Exports and receives.
**Bogdan Stancu** 19:54 I think the… I'm not really sure how the routing processor works, but I don't think it's reading the header. I think…
**Tristan Sloughter** 20:02 Oh, you're not basing the… that's not the…
**Bogdan Stancu** 20:06 It is, yeah, but we have to take it from the header and put it as an attribute.
**Tristan Sloughter** 20:10 Because I think…
**Bogdan Stancu** 20:10 and then…
**Tristan Sloughter** 20:11 Okay.
**Bogdan Stancu** 20:12 It's… I'm not really sure how that works. No.
**Tristan Sloughter** 20:14 Yeah, now it makes sense, yeah, if you're doing it that way, that makes sense.
HTTP header there. Okay.
**Bogdan Stancu** 20:24 Oh, good until now?
Any… any questions? Okay. And then the one issue that we had, because we are using this chain collector setup, is if the backends answer with anything that's not 200, the errors are only seen in our collectors.
**Tristan Sloughter** 20:43 But not the user ones.
**Bogdan Stancu** 20:45 So, the user would look… and I told you this in the previous meeting as well, the user would just C, 200s.
Metrics exported, all good.
Which we, well, didn't want.
And I don't think there's a fix for this, and I don't think there should be, it's just… The way it is.
Because this transaction ends before the collector does anything with the signals.
And what I did is just add an extension to the… to this receiver.
Which… sends, like, a mock request with that auth, with the auth on the signal, and caches the result, so we don't… well, overload the cache… the auth layer. So we are… I'm also checking authentication here, and then we'll do it at the backend as well.
**Tristan Sloughter** 21:51 Good. So that's checking the authentication with the backend to make sure it's… Yeah. So it's not a… yeah.
Does that… does that catch when the back ends… oh, you're just catching 401s, so you're not worried about the back ends being overloaded and, like, dropping and saying, I'm getting too much? They just… it's just whether or not they work.
**Bogdan Stancu** 22:12 Yeah, this is just for the authentication for now.
**Tristan Sloughter** 22:15 Okay.
**Damien Mathieu** 22:16 to storage backends, or… Yeah. Okay.
**Bogdan Stancu** 22:22 Yeah, and this was the… I think, the only place… I mean, the best place that we could put it, because it's in our collectors, we managed this, so we didn't kind of force people to upgrade.
But it's still… In the receiver, so it can… answer with a 401. The transaction is not done. The extension sees, that off.
So yeah, that's there, it works fine.
**Damien Mathieu** 22:55 Wait, basically you're, extension is kind of a secret breaker for the storage backend? Is that it?
**Bogdan Stancu** 23:05 Yeah, I'd say that, yeah.
**Damien Mathieu** 23:07 VATS, so it's a side thing, but that's interesting. We can chat about it, outside of here, but, I think it may be interesting to kind of… Look into opening that.
**Bogdan Stancu** 23:21 Oh, yeah, sure.
**Tristan Sloughter** 23:23 Well, I wonder…
**Bogdan Stancu** 23:24 Sorry.
**Tristan Sloughter** 23:26 No, I was just gonna say, if there's any talk of a way to… Include, back pressure that's, like, more generic from what happens in the exporter.
Rather than… like, per… Failure type, adding an extension, but doing it.
When the exporter fails.
**Bogdan Stancu** 23:47 That would be awesome, because then you would be able to chain 10 collectors, and it would still kind of work.
Yeah, I mean, this is the only major problem that we've had, and it's because we are chaining collectors.
**Tristan Sloughter** 24:04 Problem, in the sense that…
**Bogdan Stancu** 24:07 well… People don't see logs. That's the… it's not that big, but we… We wanted to solve it.
**Tristan Sloughter** 24:18 Yep.
Okay.
Very nice.
**Bogdan Stancu** 24:23 Yeah, and, I mean…
**Tristan Sloughter** 24:28 Every quarter.
**Bogdan Stancu** 24:30 I should have filled these up, I didn't.
I don't have much here. I mean, I can talk about it, but I… I don't… I didn't write anything. Yeah, every quarter, we do an upgrade.
**Damien Mathieu** 24:44 the collector.
**Bogdan Stancu** 24:47 The collector and the operator as well.
Kind of. I mean, it depends if.
**Damien Mathieu** 24:53 But, I mean, so every quarter is pretty… not often, especially since the collector is released every other week. Is that just to… because you… doing that more often would be too unstable, or because it would be too much work?
**Bogdan Stancu** 25:12 No, it's, it's kind of just a standard, update.
Schedule that we have.
we… it fits. It… we didn't have many issues with upgrades.
**Damien Mathieu** 25:25 Yeah, I mean, there shouldn't be breaking changes, but yeah.
**Tristan Sloughter** 25:28 No, really?
**Bogdan Stancu** 25:30 That was an issue.
**Tristan Sloughter** 25:32 In the Atlassian interview, they brought up this.
Upgrades would change metric names or something and stuff, and would…
**Bogdan Stancu** 25:40 Yeah, but I mean.
**Damien Mathieu** 25:42 a recent, recent Prometheus issue.
There has been several patch releases about that.
**Tristan Sloughter** 25:49 Hmm.
Yeah, hopefully that stabilizes, or has stabilized.
Okay, the… So, with the… what's frustrating? Oh, wait, well, to be clear, the quarterly… are you updating the user's contribut sidecar and their deployment as well? Or is this just the… Management namespace, deployment, and the operator.
**Bogdan Stancu** 26:20 We are updating the chart.
**Tristan Sloughter** 26:23 Right, so if they deploy again.
**Bogdan Stancu** 26:25 Yeah. But I've seen the operator does some things.
We've had users with, Well, older versions of the collector, and the operator would… I think it does some change… I'm not really sure what it does, because I haven't worked on that very much. But it does some changes to the config to match its new Kind of way of thinking. And if the collector is too old, the new way of thinking for the operator is… Well… It breaks down.
**Tristan Sloughter** 27:00 Yeah.
**Bogdan Stancu** 27:01 So we've had… we've had issues, and, like, people would just come to us, say that it doesn't work anymore, and we say, well, upgrade it, and it's fine.
**Tristan Sloughter** 27:13 Do they start losing telemetry then, or is it just… Arying that it can't do anything with their collectors, or they can't.
**Bogdan Stancu** 27:20 Oh, yeah.
No, it breaks. The collectors cannot start.
**Tristan Sloughter** 27:25 No, they can't start. So they're currently running stuff, it's still working, because the configs are already there, and it's just OTLP, but they… okay.
**Bogdan Stancu** 27:36 Oh, well, I think they restart.
Because… I'm not sure.
Well, yeah, I wouldn't want to talk about it, because I'm not sure.
But the operator is changing the hotel call, the OpenTeleventry Collector resource, And… I don't know if that triggers a restart on the collectors.
**Tristan Sloughter** 28:01 Hmm.
**Bogdan Stancu** 28:03 Don't think so.
But, I mean, it's Kubernetes. Things are… Are meant to restart.
Fandom.
D.
**Tristan Sloughter** 28:18 Yeah, whoops.
With what's, frustrating.
Have there been pain points that… Dude.
Hit before that were resolved, or anything currently?
That's… been an issue.
**Bogdan Stancu** 28:34 I'm tied… Don't think so. I mean, this, this thing with the upgrades was… but there… I think there's a flag in, In the operator.
To not rewrite?
I think there's a flag in the operator, to disable changing the configs.
So it's not going in and breaking stuff.
So it's that that's on us.
**Tristan Sloughter** 29:02 Ish?
**Bogdan Stancu** 29:04 And… I think that's it. I mean, again, we had… we've had this issue, and with the chain collectors, but I think that's… Normal.
I wasn't expecting this to work the way we wanted to.
It was fun, it was really nice, but I… I mean, the experience was good.
Not gonna…
**Tristan Sloughter** 29:26 Writing the extension, or… Do you mean? The experience was good, right?
**Bogdan Stancu** 29:29 The whole experience, the whole experience with writing the charts and deploying the whole thing, it was… Well, it went pretty good.
Not gonna… can't really think of something that we… That frustrated us. Frustrated us.
And I think we love that. I mean, the next thing is what we love. And it was… it was easy. It's this, well… plug-and-play thing, the… like, you see, you have a bunch of components, and you can match them and do stuff with them, and it's nice.
And…
**Tristan Sloughter** 30:04 And especially… I said you were using auto instrumentation, so was that fairly plug-and-play, and…
**Bogdan Stancu** 30:09 Yeah, yeah.
**Tristan Sloughter** 30:10 The operator and everything pretty, the same?
**Bogdan Stancu** 30:13 Yeah, well, we didn't do anything to it, it just… it just works, yeah. People add two lines in their deployment.
**Tristan Sloughter** 30:22 Yeah, we're kind of…
**Bogdan Stancu** 30:22 And it works.
**Tristan Sloughter** 30:24 What kind of services are you running? Like, Java, Go? What is it, auto-instrumenting?
**Bogdan Stancu** 30:29 We have other instrumentation for everything that OTEL allows, and people can just choose the language in the values.
**Damien Mathieu** 30:41 Our focus…
**Bogdan Stancu** 30:41 I don't think I can share.
**Damien Mathieu** 30:43 Are you still able to do manual instrumentation, or is that just auto?
**Bogdan Stancu** 30:47 Yeah, I think so, yeah.
**Damien Mathieu** 30:50 But it's basically not something you're really doing.
**Bogdan Stancu** 30:54 No. I mean, yeah, they can. We're not… we don't have a path to support that.
we… This has been… I mean, this is, the whole thing was thought of as something very easy.
**Damien Mathieu** 31:08 Sorry, maybe I missed that, but what is your tech stack?
Which languages?
**Bogdan Stancu** 31:18 in Adobe.
roll.
**Damien Mathieu** 31:21 Yes, the languages, is that mostly Java?
**Bogdan Stancu** 31:24 I don't know if I can share that. I've asked a bunch of people, I don't know if… I have not thought…
**Damien Mathieu** 31:30 My question is mostly, like, you're auto-instrumenting, from, like, Java, Node, Ruby, Go?
**Bogdan Stancu** 31:40 I'd say yes.
**Damien Mathieu** 31:42 Okay.
**Tristan Sloughter** 31:43 All of them, yeah. I figured it would be all of them, yeah. Okay.
That's true. So, but, I mean… Users can just, since they're running a sidecar, accepting anything, They can… Just… instrument their application with the SDK, and before… and manually send stuff, right?
**Bogdan Stancu** 32:07 Yeah, yeah.
**Tristan Sloughter** 32:08 Okay, okay.
**Bogdan Stancu** 32:14 Do you have a… But again, the… setting.
**Tristan Sloughter** 32:17 Was it… so it's such a… A large company, and… Good.
stuff has been around since before OpenTelemetry for a long time. Are you… Ex… It's interesting that you can… your namespace collector only accepts OTLP, and… but you accept, like, everything in the sidecar, and Is there a lot of conversion going on on the user's side from old telemetry they have that they still are instrumented with?
Has to get converted out to…
**Bogdan Stancu** 32:54 So did the sidecar… It's only reading from the app.
Maybe I was, I expressed myself wrong. But the sidecar is just the… It's just limited from the app, and it goes OTLP all the way to… Well, the exporter.
In our namespace.
**Tristan Sloughter** 33:16 Yeah, I would just assume that the apps… apps in Adobe have been around so long, they've been instrumented with all kinds of stuff, like StatsD or something, from… Pat, you know, long time ago.
**Bogdan Stancu** 33:27 Well, this is a new… well, not new, but we created this for new deployments, I guess?
**Tristan Sloughter** 33:37 Okay.
**Bogdan Stancu** 33:38 new apps, like, the… The stuff that has been around has… already has monitoring and more…
**Tristan Sloughter** 33:45 Not touching it. This is for the new stuff.
Okay, so there's not a bunch of conversion going on between, Old telemetry and new telemetry.
Because that's always an interesting thing the collector does, of trying to make those work together.
Are they sharing backends, or is it fairly completely just separate, like, different metrics backends for… Old and new.
**Bogdan Stancu** 34:14 the users.
**Tristan Sloughter** 34:16 Oh, you… the users… No, the user.
**Bogdan Stancu** 34:19 Yeah.
**Tristan Sloughter** 34:19 use their metrics backend, essentially? Well, you mentioned that you use the header to route them, but then, so you're not… So a team… a team has a new app and an old app.
Can they get the metrics for both of them into the same backend?
**Bogdan Stancu** 34:34 Yeah, yeah.
**Tristan Sloughter** 34:35 Okay.
Big, thick.
Don't be afraid to build custom components, yup.
I liked it.
Think… what… Mmm…
**Bogdan Stancu** 35:02 Yeah, I wrote this because it really was a nice experience to write that extension.
**Tristan Sloughter** 35:06 Yeah, that's good.
**Bogdan Stancu** 35:08 It was also one of the first things that I did with Go.
And what got me into, like, yeah, let's… this is interesting, let's learn more about it. And I got involved, and… Well, initially, I think I wanted to open source the extension, and I just went in, did a PR, and then I realized that that's not how it works. I have to… you're not just adding an extension to Contrib randomly. And that made me more interested, and yeah, well, I mean, the goal isn't to put this in contribib.
But that's how it started, for me.
that's how I got more interested in OpenTelemetry.
**Tristan Sloughter** 35:53 Okay.
Yeah, the… Speaking of, like, how I got interested, but then, how did the… did your team decide on the OpenTelemetry adoption and the collector adoption for the… for the company? How was that, like, decided on?
To move, because it sounds like you had a lot of stuff before, and then you decided to adopt a collector and push that as… what is the, what is… for new apps, what they have to use? How did that…
**Bogdan Stancu** 36:23 It's not what they have to, it's just another option.
**Tristan Sloughter** 36:26 It's just an option. Yeah.
What is that?
Supported by your team.
**Bogdan Stancu** 36:33 We still support the other options that we were supporting, yeah, it's just… this is just the new one.
**Tristan Sloughter** 36:41 Okay.
**Bogdan Stancu** 36:42 We didn't take anything out and put this in.
**Tristan Sloughter** 36:45 Gotcha. Okay.
And it seemed fairly… widespread adoption, though? Are people happy with it? Are end users happy with the actor and everything?
**Bogdan Stancu** 36:54 I'd say so, yeah.
**Tristan Sloughter** 36:56 Very nice.
Yeah, it sounds like, I mean, it's a fairly easy experience for them, so…
**Bogdan Stancu** 37:02 Yeah, that was the whole point.
**Tristan Sloughter** 37:03 True, yep.
Is that some of what, went into… adopting the collector, is this availability of the helm chart, and how you could sidecar it, and… set up these deployments. It was just, you know, a nice… way of managing observability, you thought, for… By adopting these technologies?
The operator, and collector, and helm charts, and community, yeah.
**Bogdan Stancu** 37:31 It matched everything that we wanted.
**Tristan Sloughter** 37:37 Good.
Oh, this is good. Oh, yeah, we didn't get into what… Can you say anything about… Gale, I mean, since it's a sidecar, like, the number of collectors isn't a very… good metrics, since every application in Adobe is running it.
I don't know if you can say anything about what it… what you're… namespace, collector size looks like. Like, we've been discussing about what What metrics can help people understand where they're at. Like, if they're looking to adopt the collector, and they have What size company, what size, telemetry they're seeing go through, so… whose advice on how to run it might be more applicable to them.
So I don't know if you could say anything. I mean, it's an interesting, point about you're running, Collector deployment for each signal.
With a… You mentioned makes sense that it's, in large part due to, like, isolation of faults.
So, well, you mentioned the auto-scaling, so obviously… That's related, but I don't know if you could say anything about… The size of your… What you're… what you're running.
either telem Going through it, or a number of collectors in your deployments, or anything like that?
Or any just rough, you know… we have hundreds of log collectors, or…
**Bogdan Stancu** 39:19 Well, we're in the thousands. Thousands?
**Tristan Sloughter** 39:21 Per signal?
**Bogdan Stancu** 39:23 For sure.
**Tristan Sloughter** 39:24 bill.
**Bogdan Stancu** 39:25 Yeah, yes.
**Tristan Sloughter** 39:26 Huh? .
**Bogdan Stancu** 39:29 But it… Yeah. Well… Again, I don't know if I can… or what to share. I haven't been very trained on this, and I'm kind of… well, not scared, but I don't want to say anything that I shouldn't.
So what I can say is that the… The scaling on the namespaces that we manage, the… The… the middle ones are… they're not… They're managing without the need of scale.
Like, most of them are the default number that we put.
**Tristan Sloughter** 40:08 Okay.
And I guess, yeah, something people might be interested in that, I don't know if you could get, you don't have to give it right now, but if you're able to give any… about, what type of, because I know something people have… I've heard brought up is just they're trying to figure out How to configure their collector, and what… type of CPU and memory requirements it has, and people need to just, you know, measure themselves to see what their telemetry is taking, but if you're able to share anything, like, what kind of memory limiting you're doing, like, what size of memory you're giving the nodes or anything, or the pods, that could be interesting to people, but I know that can be more into the numbers and not something you could share, so…
**Bogdan Stancu** 41:03 I think it's fine to share. I don't know right now, and I can send you the numbers after, like, in a message. I'm gonna have to ask if it's fine to share, but I don't see…
**Tristan Sloughter** 41:14 Like, did… Okay.
**Bogdan Stancu** 41:16 A problem with this.
**Tristan Sloughter** 41:18 Perfect. The one other thing on the… on scale.
So the operator is managing all of these, and it's managing each, sidecar, too, right? That's how it works, is… Yeah. The… well, I mean, it… It has to do the, I don't actually remember how that works. Auto instrumentation stuff, so it takes.
**Bogdan Stancu** 41:40 You just put two annotations.
**Tristan Sloughter** 41:44 But the… but the collector… the operator has to do some work there.
So, the scale of, like, the… have you… you haven't had any issues with, no. As users are deploying, they have, you know, all these apps throughout Adobe, the operator's been smooth sailing for handling that scale?
**Bogdan Stancu** 42:03 Yeah, yeah, no, the operator's fine.
**Tristan Sloughter** 42:09 Good.
Yeah, I don't know if there's any numbers you can give there where… yeah, because I could see people Yeah, wondering about… Yeah, no, that should be fun.
Just to know that Adobe has not had issues with the operator managing all their They're new deployments.
Okay.
**Bogdan Stancu** 42:34 And it's not all, it's an.
**Tristan Sloughter** 42:36 Right, right, they're obvi, yeah.
Yeah.
**Bogdan Stancu** 42:39 It's… we're not pushing this in people's face, it's… Yeah, it was an email, like, hey, this is it, this is why it's good, yeah.
**Tristan Sloughter** 42:49 Digital marketing, and people choose.
Richard, are you running to… you're probably running your own metrics storage and log storage and stuff like that? Yeah.
I think we've covered everything in our… Topics… Is there anything… you'd like to add on top of that, or tips? I know you've got the don't be afraid to build custom components, which is a great one. Do you have anything else you'd want to share with people reading this?
**Bogdan Stancu** 43:31 Don't think so. I mean… Nope.
**Tristan Sloughter** 43:37 Damon, do you have any other questions, or…
**Damien Mathieu** 43:43 I don't think so.
**Tristan Sloughter** 43:44 Okay.
Well, yeah.
This is great, I gotta get these written, I guess. Yeah.
There's nothing else, we'll work on… Cool, yeah. Have you in the loop on writing up a blog post?
I might have some follow-up questions, and… Oh, yeah.
As we're writing this. And… Yep.
If there's nothing else, and there's no other topic, we can… Get back 20 minutes.
Right.
**Bogdan Stancu** 44:19 Oh, that was it.
**Damien Mathieu** 44:21 Have a good day, man.
**Tristan Sloughter** 44:22 Thank you so much. It's been great.
**Bogdan Stancu** 44:24 Thank you.
