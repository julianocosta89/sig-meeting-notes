SIG: Community Demo App SIG
Date: 2025-06-18
Duration: 44 minutes
Zoom Recording URL: https://zoom.us/rec/share/xyribE7wR9hlBp7ceHupl_ODN7JnIbSktB4bdWywTmyWO-GIJSrY29y4oUpCF6tf.RU6BWeZB-j0M5tNe
============================================================

## Zoom Recording Transcript

**Juliano Costa | Datadog** 02:58 Hello! Hello!
**Pierre Tessier** 03:06 Mariana.
**Juliano Costa | Datadog** 03:11 How you doing.
**Pierre Tessier** 03:13 I'm a busy human being. I'm a really busy human being.
**Juliano Costa | Datadog** 03:19 I need. I need you back, Pierre.
The oh.
**Pierre Tessier** 03:25 Tell you it's for a while that's I'm I'm not joking, Juliana. We're we're growing. I'm I'm
I'm hiring more
**Juliano Costa | Datadog** 03:37 I spent the 1st quarter of the year running 2 different teams.
**Pierre Tessier** 03:41 And I had to take a small break, and and I and I come back and and we we did. We did some some changes
in the organization, and it's great. It's benefited me. Well, I I just need to focus on those changes.
It's my.
**Juliano Costa | Datadog** 03:57 Yeah, I I definitely need some help on maintaining the demo Miko disappeared as well. So.
**Pierre Tessier** 04:07 Yes, we do.
We? We need to get more maintainers on this thing.
**Juliano Costa | Datadog** 04:12 Yeah, and approvers. I think the only active approver is Roger.
**Pierre Tessier** 04:16 Roger.
**Juliano Costa | Datadog** 04:18 So like. When the Pr comes from the community I can approve and merge, which is great. But when the the when the Pr comes from me.
**Pierre Tessier** 04:27 You can't approve and merge. Okay.
alright. The good news is, tomorrow is actually a holiday, so I will.
**Juliano Costa | Datadog** 04:35 Yeah, and you should.
I will make sure to put. I'll put some effort in. It's a it's a holiday for United States, at least, not even a holiday for Canada.
**Pierre Tessier** 04:43 But I made a decision a long time ago. I take American holidays, not Canadian holidays, because
I work with a bunch of Americans.
So.
**Juliano Costa | Datadog** 04:52 Makes sense.
**Pierre Tessier** 04:53 You know. And it works with my family. We've we've we've we've found ways to make that work.
Okay. But yeah, I need to.
We need to find more people, I think, for this project. I think it needs to be a priority.
**Juliano Costa | Datadog** 05:08 Yeah, so on that, I I created an issue some time ago.
Issue 2185, basically.
yeah, basically calling out, all the approvers
saying that I see that only Roger is active. Please comment on this. Pr. If
if you want to stay as approver.
And Cedric came back.
And Roger, so like Roger, I was already expecting. So I'm I'm just gonna open a Pr. To move
wp. 9, 5, really, and Ziki to emeritus, if that's fine.
**Pierre Tessier** 06:08 The yeah, we would probably.
**Ani ( Opensearch )** 06:09 Let me also ask you a question. Sorry I was just on mute on multiple calls just hearing over here. I've been joining since the start. But couldn't talk in between. What does it take to be like Maintainer approval from our side? I think we've been having this goal from
like having regular resourcing on the demo. And Demo is an important part of hotel, and how we support start supporting hotel in the journey.
**Juliano Costa | Datadog** 06:38 Yeah. Well, great question.
**Ani ( Opensearch )** 06:42 I think one more person. I think the 2 of us are like dedicated for this long term so if you need any help on maintaining supporting. We've been only focusing on adding features from opensearch, but that doesn't have to be the case.
**Juliano Costa | Datadog** 06:56 So approvers. They they mainly work on checking pull requests and making sure it builds and it works, and then approving. But they do not have the power to to merge the the Prs. So that requires a maintainer, which currently is Pierre, myself and Miko from Dynatrace.
**Ani ( Opensearch )** 07:17 I think.
**Juliano Costa | Datadog** 07:20 If you say that you have the the bandwidth to to become.
Yes.
approver, I think we can, we? I'm I'm happy to add you as an approver, and then we start from there.
**Ani ( Opensearch )** 07:32 I think it'll be me and pratik both of us, I think both of us have been like constantly joining, and we have the bandwidth, or we are planning to do this for at least a couple of years from our org. We also recently started a Sig in Lf. For opensearch in observability itself. So we are going to be primarily using that Sig also basing it entirely on the demo.
**Juliano Costa | Datadog** 07:57 Cool.
**Pierre Tessier** 07:58 I I'm sorry it's open source moving under Cncf.
**Ani ( Opensearch )** 08:01 Open source is already on the same thing. It's been a year, a month.
The Opensearch is a Cncf parent project right now. Sorry. Opensearch is a Linux Foundation Cn. Project, not a Cncf. Project.
**Pierre Tessier** 08:15 Yeah, okay, that's that's what it's gonna yeah.
**Ani ( Opensearch )** 08:16 Linux.
**Pierre Tessier** 08:17 I don't think it's Cncf. Maybe I missed something there.
**Ani ( Opensearch )** 08:20 No, no, so the so we have a Linux Foundation sink for observability in open search. So open search itself is a top level entity under Lf, but not under Cmtf. You're right.
**Pierre Tessier** 08:30 Okay, are there plans for open source to go under Cncf, or is it gonna stay within the.
**Ani ( Opensearch )** 08:36 I think it'll stay. I think it'll stay in Lf, the same thing right? It's I don't think it helps or changes anything. I think, during formation. There were some discussions, but I'm not sure they panned out. I think the Lf. Umbrella gives the same amount of guarantees for the project.
**Juliano Costa | Datadog** 08:53 Yeah, I I. To be honest, I I don't know why.
We have 2.
**Pierre Tessier** 09:02 Well, there's some things.
**Ani ( Opensearch )** 09:04 I think Cncf also falls under Lf, right? So, lf, is also like, yeah, yeah.
**Juliano Costa | Datadog** 09:08 Yeah. Yeah. Exactly.
**Pierre Tessier** 09:10 It is, it is Cncf is part of the Linux Foundation overall but Linux Foundation includes clearly Linux.
a couple other Linux things which are not necessarily cloud native tooling.
I think of opensearch for what it's worth as cloud native tooling. But what do I know?
Just like.
**Ani ( Opensearch )** 09:28 I think, yeah, I think there are.
**Pierre Tessier** 09:29 Don't take it.
**Ani ( Opensearch )** 09:30 Cases for vectors and vectors, and search goes into the database. Open search is kind of a Swiss army knife. It does a lot of things and not not a lot of things. All that. Well, so our focus like, or at least my org's focus, is to focus on observability
and make sure it aligns well with observability, not just as a back end, database or a tool, but go through all the flows and user usage journeys.
**Pierre Tessier** 09:59 Okay, I mean, I think
we can talk about getting you to be an approval here.
I I don't see an issue for what it's worth. And we definitely need more people.
**Ani ( Opensearch )** 10:12 Spirit.
**Juliano Costa | Datadog** 10:13 Yep.
**Pierre Tessier** 10:14 And I think it probably makes sense to make a call to action for this.
**Juliano Costa | Datadog** 10:24 You think.
**Pierre Tessier** 10:25 Clearly, we have a people bandwidth problem. That's what I'm saying.
**Juliano Costa | Datadog** 10:28 Blog posts would not hurt.
**Pierre Tessier** 10:30 Do. You haven't been able to write a blog post.
**Juliano Costa | Datadog** 10:33 Yeah, I could do that. But like we need your help.
**Pierre Tessier** 10:36 Yeah.
**Juliano Costa | Datadog** 10:37 Something like that.
We we got 2 really active contributors to be fair.
What is? What are the their names?
One sec.
I think it's dependable. No, just kidding.
**Ani ( Opensearch )** 11:02 I don't know.
**Juliano Costa | Datadog** 11:10 I think it's our our video and our Rs, something. Oh, red TV.
And
the other person. I don't have any Pr. Here. I think I have one open that I just reviewed today.
**Shenoy Pratik** 11:34 Yeah. Let's me.
**Juliano Costa | Datadog** 11:37 Okay. Awesome.
**Shenoy Pratik** 11:38 Semi cool
So I also wanted to discuss about the prp after the Cta thing.
**Juliano Costa | Datadog** 11:46 Also.
**Pierre Tessier** 11:47 Which one's your pr sonoy.
**Shenoy Pratik** 11:50 There's the load, generator one.
I'm putting it here.
**Juliano Costa | Datadog** 11:54 Hmm!
The one with the low generator. I was a bit
I did a lot of testing on that.
**Shenoy Pratik** 12:04 I I'll be honest. I I did. See some of those comments coming up. I just want to instrument as much as possible, and then we trim down. That was my point of raising that.
because I know if we when we load, test with load balancer load generator, I know. Like, if we have 50 users, the log will just keep from onboarding the open such cluster.
So I I know we need to trim down somewhere. But I just was wanting your opinion on it first.st
**Juliano Costa | Datadog** 12:32 Yeah, the the trace thing I tried to.
I tried to get rid of this new this new spend creation. But it doesn't look like locust is actually creating spends in the requests.
So then I just gave up and accepted your suggestion like, yeah, we're gonna do this. Then let's just remove the double logging thing.
And I think I left one comment on the on the resource that we can. I also tested. So this actually works, we can use the end of our to get the resource name other than that. I.
I don't have any anything here.
One thing that I would like to discuss, as you both will become approver. Npr. Is here.
so we have one pr. That is, being open since April, from Henrik, which he introduces damper.
**Shenoy Pratik** 13:36 Yeah, okay. I have looked at it but didn't try it out. Maybe I can take a stab at reviewing and then trying it out.
**Juliano Costa | Datadog** 13:46 Yeah, I think I think it. It still has it still have some some issues on it. And what I'm concerned about it is that the dapper instrumentation for hotel
doesn't support dB, semantic conventions yet
so like we would have just generic calls to the database which is not ideal. I would love to.
**Shenoy Pratik** 14:13 You.
**Juliano Costa | Datadog** 14:13 The database instrumentation. But it looks like this is something that's being added. So then I would be finding in getting that.
It's a big change. So.
**Pierre Tessier** 14:26 Yeah, I think we talked about maybe limiting its surface area for that change.
**Juliano Costa | Datadog** 14:30 Because.
**Pierre Tessier** 14:36 yeah, like, I think it makes sense for maybe a service or 2 to have it, but not all services.
**Juliano Costa | Datadog** 14:42 Yeah. It's not all.
**Pierre Tessier** 14:45 Sure, but.
**Juliano Costa | Datadog** 14:49 I think it's just that he's adding the dapper service. Then he's changing a couple of things on like
on product catalog to actually use a database. So it's using a postgres.
That's why it also needs to change the product catalog.
I think the only thing that actually uses dapper is the current service at the moment.
**Pierre Tessier** 15:23 Okay. So he must have updated that.
**Juliano Costa | Datadog** 15:28 No! The the product catalog is also using dapper sorry. So 2 services.
**Pierre Tessier** 15:40 I see you in accounting as well.
**Juliano Costa | Datadog** 15:41 Accounting as well, yeah, your.
**Pierre Tessier** 15:44 Yeah, I seen the several services where it was added.
I don't know if that is yeah. Okay.
**Juliano Costa | Datadog** 15:59 Can definitely discuss that further with Henrik. But I
I would like to not discard this. Pr, I think Doppler is.
It's something nice to to add to the demo. Maybe again, not in all services. But yeah, I think we can.
We can always trim, trim it down
and then we have 2 prs from from Cedric here
that I I feel like his changes are not in in the place. It should be
so he's currently changing the the front end instrumentation
and adding a bunch of
remapping in the in the instrumentation itself.
But I think we should like to to avoid. Cardinality cardinality explosion, we should do something in the collector and not.
**Pierre Tessier** 17:11 Yes.
**Juliano Costa | Datadog** 17:12 Services itself, and then open an issue on the, on, the
on the Js instrumentation to kind of
properly create a spend with the a proper name, instead of
because this is a issue on the, on the, on the instrumentation.
**Pierre Tessier** 17:29 I thought we already fixed this in the collector.
**Juliano Costa | Datadog** 17:33 We had. I think we have one scenario, but I think he's complaining about another one or.
**Pierre Tessier** 17:39 Okay. So we should just admit what we have. Then.
**Juliano Costa | Datadog** 17:43 Good question now.
Well, I'll I'll double check that, because we do have something in the collector. But when I push, when I push back.
He said that
He saw some folks
using the demo without the the collector from the demo, and then the cardinality explosion happens.
**Pierre Tessier** 18:05 Maybe we should document that. Then, like, make sure you use the collector's config. So you avoid the cardinality like
because I'm looking at it. And we absolutely have that in the collector lines 1, 12 and 13.
Yeah of the hotel config.
**Juliano Costa | Datadog** 18:22 Have, and it even says, like, Hey, we're waiting for this to fix. Get fixed upstream. There's a comment in there about it as well.
**Pierre Tessier** 18:30 You know, if we have to augment this. That's fine.
But maybe we just do a like.
I would rather see a doc that says, Hey, currently, this is going on. So if you're gonna
in putting this inside code, I don't think it's the right spot is what I'm saying.
**Juliano Costa | Datadog** 18:49 Yep.
**Pierre Tessier** 18:50 Right.
**Juliano Costa | Datadog** 18:50 Yeah, me, too. That that's why I I didn't approve the Pr.
**Pierre Tessier** 18:55 Yeah.
**Juliano Costa | Datadog** 18:58 Okay, so.
**Pierre Tessier** 18:59 And that issue is still open on Nextjs as well.
**Juliano Costa | Datadog** 19:02 We are aligned on that right.
**Pierre Tessier** 19:04 In the community.
**Juliano Costa | Datadog** 19:07 I think you missed Pierre just to to bring you up to to date. I refactored the the rest service. So shipping. Yeah.
**Pierre Tessier** 19:19 Yep.
**Juliano Costa | Datadog** 19:20 And now it's actually using hectics web.
So it's a Http service now. And so I had to change the checkout
and the call to quote, and everything. But we have a hectics, web, rest, instrumentation.
**Pierre Tessier** 19:38 What about the change? Did we? Did we just move from Grpc to Http.
**Juliano Costa | Datadog** 19:43 Yeah, this was a change, and I'll like, I think we are using Tokyo and singing instrumentation
to get the traces, which was a mess. And so then I moved to actics. Web did the
Instrumentation library actics web and then use tracing the tracing library just for logs. I didn't want to. But C. Joe from the rust Community Maintainer came and said, Hey, we should show this as well. So then, now we have like tracing for logs and then open telemetry for metrics and
entrances.
**Pierre Tessier** 20:24 Okay.
**Juliano Costa | Datadog** 20:25 Yeah, tracing is a fun name. So, but.
**Pierre Tessier** 20:28 Yeah. And I know rust was built with tracing built in. But it wasn't.
**Juliano Costa | Datadog** 20:33 Awesome.
**Pierre Tessier** 20:34 Yeah, it's like activity and.net. But the activity is built a little bit more closely to open telemetry versus what.
**Juliano Costa | Datadog** 20:41 Tokyo.
**Pierre Tessier** 20:41 Tracing was built so.
**Juliano Costa | Datadog** 20:43 Yeah.
**Pierre Tessier** 20:44 I agree, yeah.
**Juliano Costa | Datadog** 20:48 yeah, docs are up to date on that. This will require a a couple of changes on helm. So we should think about releasing a
well.
**Pierre Tessier** 21:01 Will it.
**Juliano Costa | Datadog** 21:02 Release.
Yes, because we changed a couple of environment variables.
**Pierre Tessier** 21:07 Okay.
**Juliano Costa | Datadog** 21:08 And the way they are the way checkout is calling, shipping.
and the way shipping is calling a quote as well.
So it it was a a big Pr
I I spoke too much. Do you guys have any anything else that you would like to
to discuss.
**Ani ( OpenSearch )** 21:38 I think, from a I'll from this agenda person. No, I think next time I'll just have the agenda item to
discuss some of the how do we use the demo for workshops? I think we try to divide like empty services. I think that draft I've been working on, I think next time we can bring up that.
how to use like some empty services so that a demo can be used in workshop in like an how to get started with something at the empty shell.
**Juliano Costa | Datadog** 22:10 You mean having services that are not instrumented or services.
**Ani ( OpenSearch )** 22:15 Having so having us having an existing service, or a clone of an existing service, or a new small service, I'm thinking, which part to take care, but something that is not instrumented. So that way, when you learn something or keep it in the workshop session, people can start doing the instrumentation and going through the flow. Currently every. I have one session within some of our orgs and teams to go through
learning open telemetry and trying things out, and that's where like, since everything is instrumented to get started, and I have to delete and prepare something and then go through so like, how would be a workshop flow being run focusing on workshops.
**Juliano Costa | Datadog** 22:57 Yeah, this is something that is a recurring discussion. Actually.
**Pierre Tessier** 23:00 We should have an easy solution.
**Ani ( OpenSearch )** 23:03 So that that's 1 and second in the other channels we were talking about Inspector Gadget.
So I think Inspector Gadget is another project. That's I don't know how how ready. That is what we've been seeing how Inspector Gadget can be used for auto instrumentation
that might require a lot more work. But the inspector community is also pretty
active on the Kubernetes channels. And I think we've been think talking to them and see how to get this as part of the non auto instrumented code base instead. And this is very good.
**Pierre Tessier** 23:46 Right, and that.
**Ani ( OpenSearch )** 23:47 Yeah, inspector gadget is the Ebbs project. But the one good thing is, they have a very pluggable ebbs model. So they have these like pluggable gadgets that you can add, and they have a lot of good pluggable gadgets as a library available to get started.
**Juliano Costa | Datadog** 24:03 I never heard of Inspector.
**Pierre Tessier** 24:07 Inspector gadget Hotel. Compatible.
**Ani ( OpenSearch )** 24:11 They have voted writers.
**Shenoy Pratik** 24:12 What about logs and metrics in hotel Grpc.
I summarize some of this bit here that. Have the attorneys talking about. And also, I think this covers that previous discussion. I think last month
this photo
you can touch base on it again.
**Pierre Tessier** 24:35 Yeah, I remember, I remember.
**Shenoy Pratik** 24:36 More detail.
**Pierre Tessier** 24:37 I've seen a bit about this, but it's been a while.
As I looked at it I remember looking at it at first, st and it was very.
very nascent back then.
And it also. I don't believe it supported opentelemetry either.
**Juliano Costa | Datadog** 24:51 It does. I I have here. So you can export auto metrics and auto logs.
It's just the docs are like, yeah, I love, how how people structure their docs. So the the metrics are actually under exporting metrics to Prometheus.
and there is a otop Jrpc. Section in there. So thank you.
**Shenoy Pratik** 25:17 I had to navigate my way around the rocks to get hold of this piece.
**Juliano Costa | Datadog** 25:23 Yeah, I just shared the the link here, Pierre, if you want to to take a look.
But yeah, huh!
It it.
So there is someone on my team that is, that is also looking for an instrumented version of the demo.
So I think we should.
**Ani ( OpenSearch )** 25:46 Okay. Nice. Nice. Yeah.
**Juliano Costa | Datadog** 25:47 We should, we should try to to work together and
kind of create a a seek of no open telemetry, Demo bye.
**Pierre Tessier** 25:58 I wonder if sometimes I think about this, Julie? I know it's a branch.
**Juliano Costa | Datadog** 26:03 Yeah branch of the peg, and it's it's a branch, you know, and and but in maintaining that branch.
**Pierre Tessier** 26:09 Is my! Oh, my goodness! That's a mountain.
**Juliano Costa | Datadog** 26:13 Yes.
**Ani ( OpenSearch )** 26:14 So I think.
**Pierre Tessier** 26:15 That's what it says.
**Ani ( OpenSearch )** 26:17 So hold on like, why do you think of it as a branch? Just because the current services are too many and they may not be sort of
like. It's not easy to add and maintain. It's like a maintainability thing, because that we can address by having like one or 2 more calls, or one or 2 more features in the existing services and keeping them empty, empty. Maybe those features are showing a banner, or we can come up with some product thing.
**Pierre Tessier** 26:44 What language do you write those services in.
**Ani ( OpenSearch )** 26:47 I think currently the goal I was keeping was Java. And go. These are the more common things.
If you take a new service approach or a new new approach. But I think we can debate a bit, I think, more and more from maintainability aspect. If you add like functions, and calls to existing services that are available in existing languages that add features to the demo.
I think that way. Those features, when turned off are not visible in the demo. When turned on they show up as like something extra on the website, or some extra as calls.
**Pierre Tessier** 27:22 Yeah, I I think what I'm I'm come back to is let's pretend they're or let's just say they're their new services.
I'll argue that Js is more popular than go.
Certainly, when people coming to open telemetry, looking for open telemetry, things for for what it's worth to go as a cages isn't really wide in open telemetry support.
Meanwhile Js and Java are very far ahead, and so is.net. So I would argue those 3 languages before go.
Now we have 4 new services, one for each language, and the demo is already 20. Something services
go ahead total. Right? So now.
now we keep on growing it. And that's the argument of, should we have a clean version of the demo instead? Because we cover every language in that view.
**Juliano Costa | Datadog** 28:09 Just to give you some context, because
if we remove the if we remove the instrumentation from all services, we can also demo the operator to instrument those services
which is something that we also need to do as a as a project like, it's nice to demo the operator and.
**Ani ( OpenSearch )** 28:29 Got it. Got it? Got it, I think.
**Shenoy Pratik** 28:32 And it would also lend well in the lab.
**Pierre Tessier** 28:34 Meeting about about testing the the greenness of open telemetry. We would have a clean environment. You could instrument a service and retest its Co. 2 impact.
Understand how that looks? There, there's a there's definitely an argument to to be said that the whole demo could be uninstrumented.
**Ani ( OpenSearch )** 28:55 Fair.
**Shenoy Pratik** 28:56 I had fun.
**Pierre Tessier** 28:56 No, I agree, you know.
**Shenoy Pratik** 28:58 Thumbs up.
**Pierre Tessier** 28:58 A certain.
**Shenoy Pratik** 28:59 Coverage in terms of coverage. We do have a lot of services which are not
covered of for all the inter instrumentation of locked in metrics. Right? Can we start with those rather than removing the instrumentation for the things that are already there?
**Pierre Tessier** 29:13 Every service today has tracing inside of it.
**Shenoy Pratik** 29:17 Yeah.
**Pierre Tessier** 29:18 And then some of them will not have
metrics or logs, I think. For the most part it was SDK support
so as SDK. Gets support support gets rolled out. We typically get those services written in that language to support that telemetry type and and fairly short order.
**Shenoy Pratik** 29:38 I see. So the for all the popular languages that we talked about we do have instrumentation
traces everything but for logs and metrics as well, and that.
**Pierre Tessier** 29:47 Mostly we would.
**Juliano Costa | Datadog** 29:48 Metric.
**Pierre Tessier** 29:49 Sure. Yeah. And some logs, too.
**Ani ( OpenSearch )** 29:50 Groove.
**Juliano Costa | Datadog** 29:51 For Js. We do not have logs yet.
**Pierre Tessier** 29:56 And that is the jets don't
we have to use? We have to use the right log framework because Js is, it's it's it's all log bridges.
**Shenoy Pratik** 30:06 I saw.
**Pierre Tessier** 30:08 yeah. And I feel like somebody mentioned that as well. There was an issue about that. And okay, great pr.
it's it's fine.
**Ani ( OpenSearch )** 30:18 Then, if you remove the instrumentation to have a clean build.
then we still have the demo app, but the demo app fully uninstrumented.
Then the question remains whether it is a branch, or whether we do something else without a branch.
**Pierre Tessier** 30:35 Yeah, whether it's a fork or another branch, or a tag like.
**Ani ( OpenSearch )** 30:40 Yeah, that that scares me from maintainability.
**Pierre Tessier** 30:43 Yeah, the maintainability is really scary.
**Ani ( OpenSearch )** 30:47 Yeah.
like, I know, it's like, C plus plus world. You could have macros to hide code. I'm not sure all other languages what they do, but some kind of build, time, flag, or runtime flag to hide instrumentation. I'm not sure how feasible it is in all languages. That's what I'm trying to think.
Maybe just run with the flag, which is like uninstrumented or but that doesn't help the workshop builder, because then you will see the code that doesn't help. So I guess brainstorming here, then, what other options.
**Pierre Tessier** 31:14 And and even running open television and no OP. Way. There's still some kind of overhead for it.
**Ani ( OpenSearch )** 31:19 Got it.
I think the best approach over there is. Then.
seeing how much can be shared, as
I don't think the logic is too bad in the open telemetry, demo. So I don't think there are issues with the logic that have bugs, unless then we just forget or create a.
I think 4, because also I don't know. 4 feels bad.
**Pierre Tessier** 31:43 For another way to look at this is, we're not doing a lot of changes to the demo, either. At this point. Outside of dependabot prs, most of the Prs are
right.
It's a 1 time effort. That's huge. But yeah, the the ongoing maintenance of that would be
quite difficult.
**Juliano Costa | Datadog** 32:07 It would be hard on how you maintain it.
Yeah, I think once we once we fork it, it should be its own living thing
with their own dependable and stuff, because, like.
we won't be able to sync to sync with upstream ever.
**Pierre Tessier** 32:29 I would even go as far as to say, we need to remove several services.
And really just focus on a a core, a, a smaller core set.
**Ani ( OpenSearch )** 32:40 Makes sense that makes sense.
**Juliano Costa | Datadog** 32:42 Extension.
**Pierre Tessier** 32:44 Because we have.
So it's.
**Shenoy Pratik** 32:47 So there's already an issue for this by Hendrick. Maybe.
**Pierre Tessier** 32:51 Oh, yeah. Oh, yeah, yeah, it's it's been a thing that we thought about since, like
2022, I feel like we 1st talked about this.
**Shenoy Pratik** 32:59 Right.
**Juliano Costa | Datadog** 32:59 But once we do that, then I would vote to get rid of the docker. Minimal thing. But yeah, this is another.
**Ani ( OpenSearch )** 33:07 Yeah, yeah.
**Pierre Tessier** 33:08 But I think this makes sense. So this is a big thing for.
**Ani ( OpenSearch )** 33:12 I think growth or adoption, or when people start using it, because if you give a script for other creators or other teachers who can do these workshops, I think it becomes its own thing that will help promote the project more so in that respect just the value prop of it is so high supporting one more fork and not having a very clean tie up or a sync strategy. I think that should be okay.
I think that that's extra thing worth having.
**Pierre Tessier** 33:39 Yeah.
No.
I I'm gonna I'm gonna play a little bit of devil's advocate here.
**Ani ( OpenSearch )** 33:44 Yeah.
**Pierre Tessier** 33:45 And say, what's wrong with the
the way the app there, the mini app that our docs that the open help she docs are using to push people
the instrument and to do workshops with.
**Ani ( OpenSearch )** 33:58 What is the Mini app? I don't know.
**Juliano Costa | Datadog** 33:59 The the roll dice thing.
**Pierre Tessier** 34:01 Yeah, they're rolled out.
**Juliano Costa | Datadog** 34:03 Yeah, no, no, that's too too minimal. So like
**Pierre Tessier** 34:08 For a workshop. Do you need something more than minimal.
**Juliano Costa | Datadog** 34:12 Well, I run a workshop where I have 3 services and a collector.
So one services, 2 services in Java. I do. Minor instrumentation, and then I do out auto instrumentation with the agent and one service in the middle, in Rust, where I do Instrumentation library. So I explain the 3
types of instrumentation, and then I use the collector to 1st just to route traffic, and then I use the collector to also scrape metrics from host and container.
So this isn't.
**Pierre Tessier** 34:50 Workshop, Julia, is that like a like an 8 h workshop, there.
**Juliano Costa | Datadog** 34:53 2 and a half hours, 3 h, depending on on the.
**Pierre Tessier** 34:57 Wow!
**Juliano Costa | Datadog** 34:58 On the audience. But, yeah.
**Pierre Tessier** 34:59 Honeycomb has a not too dissimilar thing, but it's actually 2 different workshops. The 1st one is a small 2 service application.
Maybe they added a 3.rd I can't remember
written across like 6 to 4 different languages, and you can mix and match them. But they're very basic services. Right? They're really, really basic things that do simple Http calls to each other. And then we have another workshop that talks about adding collector of this stack
but again, we don't use the optometry demo for this, because the demo is a complicated application that has a lot of aspects to that, and introduces a lot of
just noise. Is somebody trying to learn open telemetry?
**Juliano Costa | Datadog** 35:39 Yeah, but depending on where you are focusing. So like how to use Inspector Gadget, or how to use the operator, it's better to have something that is multi language.
**Pierre Tessier** 35:51 Yeah, yeah, yeah, I I agree. I agree when when you think but those are not workshops, those are adding an auto inspector.
**Ani ( OpenSearch )** 35:59 So I think for me, for me, the where the where I use the demo the most is with the recent updates on flags, and when you run like, actually, investigation flows, and more and more, I've been using the demo with AI workflows because it you need
some level of detail and complexity. If it is too simple, then it becomes too fake, and it's not too real. I think that's where the demo really help helps with the. I think it's complex enough, and sometimes it is very complex. But it's not that daunting for people nowadays it. It can be run on a laptop, and they go to their one service, and in the whole mesh of everything they can see and focus on one thing, but still see the debugging across so many aspects. So it's the nature of it's an aspect of reality to it.
Which if I feel helps a lot when the demo, when you showcase, or when you talk about it, it feels real. It feels like something that the team would do.
**Pierre Tessier** 36:58 Yeah, I think we're coming back and saying, we probably need an uninstrumented smaller version.
What the of the astronomy shop application?
There's probably.
**Ani ( OpenSearch )** 37:13 Yeah, I think. Yes, I think yes.
And I think the smaller version. I'm looking at the language distribution and types of instrument, different data distribution we can just choose from there, like which languages or which instrumentation is more important and based on that. See if the things that are not important. How critical are they to the demo, and then take a call.
**Pierre Tessier** 37:33 Buffet.
I think, for for.net, for example, we have 2 different services. One's done with the agent, the other one's done with manual cementation.
**Ani ( OpenSearch )** 37:39 Yeah, yeah.
**Pierre Tessier** 37:40 Need that right? Like, when I think of that example in specific
we have multiple js, things.
although you kinda need a payment service to make things work, no matter what.
**Ani ( OpenSearch )** 37:51 Yes.
**Pierre Tessier** 37:54 But yeah, I I
you know there's probably things that we could trim off the demo and and reduce its size. And then I wouldn't call it an open elementary demo anymore. I would just call it a mini application right for instrumentation, like, you know, naming things is hard, but
I don't even know if it would be part of open telemetry org anymore, or if it'd just be a an application that exists and lives.
**Ani ( OpenSearch )** 38:19 So I was thinking, using the name that we have been using now like open telemetry workshop.
So open telemetry, demo and open telemetry workshops are always sister projects.
**Pierre Tessier** 38:28 Yeah, I I would almost say it's the astronomy shop.
**Ani ( OpenSearch )** 38:34 Yeah. Fair.
**Pierre Tessier** 38:35 Right. And yes, it. It came from open telemetry, which originally came from
hipster shop, which we.
**Ani ( OpenSearch )** 38:52 Move it this way.
**Pierre Tessier** 38:53 It's really an uninstrumented multi micro services. Demo application is what it is.
**Ani ( OpenSearch )** 39:00 So let me ask you a reverse question now. So if you have a workshop, I think it's fine, I think we would use it. The second part of it is like, under that workshop or in the open telemetry website. Would you have documentation
for us to run the workshop like, if you have a script to run the workshop with all the like guided assets, or how to where to go, how to maintain like this becomes like a tutorial, a cookbook, or how to script it. I think, then it serves a purpose for others to use our script and promote it more, and run it.
**Pierre Tessier** 39:33 I think.
**Ani ( OpenSearch )** 39:34 Empty shell.
**Pierre Tessier** 39:35 That was done within the opportunity community. The Docs site community in particular, where they decided to move forward with the roll dice application we mentioned for that specific
sorted use case.
**Ani ( OpenSearch )** 39:47 Got this?
**Pierre Tessier** 39:48 This is something that's a little bit granular, like like what Juliana mentioned. That use case is really simple. It's it's a single service way of approaching it.
But
yeah, if you if that's why I'm saying this almost feels disconnected from open telling you at this point.
**Ani ( OpenSearch )** 40:08 Alright that if you disconnected, then it doesn't serve that much of a purpose. If you leave it out of open telemetry, then it will not like come back with
how it can be used, together with the instrumented version, like the instrumented version. And this version, even though the logic and things little bit separate. If it's fully disconnected, then I don't think it'll get like long term maintainability or long term use.
Then it is something with a fork that we could maintain, or somebody else could maintain.
**Pierre Tessier** 40:37 I would love if somebody else built it.
I'm I'm just, you know. Open telemetry is for things that have open telemetry. If this would if you remove all things open telemetry.
does this still belong to opatology like? Yes, I I get. The intent is to put on the dock site, but
and their name is eluding me to Severn, and I forget the other person's name.
have, you know they they there was a discussion about this several months ago, maybe even over a little over a year ago, they they moved forward with going to very simple rolled ice application for this kind of use case.
**Ani ( OpenSearch )** 41:16 If that's a thought for sure. If you remove everything that it doesn't remain, it remain. Yeah, fair.
**Pierre Tessier** 41:25 You know, the only thing that keeps an hotel demo is a protobuf
for the app. It's called Hotel devil.
**Ani ( OpenSearch )** 41:29 Lunch like, unless it.
**Pierre Tessier** 41:32 No. Is it called Demo? Did we rename that Protobuff.
**Juliano Costa | Datadog** 41:39 I doesn't.
**Pierre Tessier** 41:40 I now need to look that up too many tabs.
**Ani ( OpenSearch )** 41:45 I. Still, yeah, I still think about the teaching aspect and how it would be useful to open telemetry. The project itself. I don't know enough about the role dive application you're talking about. I need to think I need to look at that. But if that serves the purpose, then then I think you're doing similar things.
Where is that thing? I'm trying to find it.
**Pierre Tessier** 42:05 The product.
**Juliano Costa | Datadog** 42:07 The main sorry. The the proto or the roll dice.
the row, the roll, dice, application.
**Shenoy Pratik** 42:13 Searching for it.
**Juliano Costa | Datadog** 42:15 On the docs itself. So if you go per language, you have the same application in all languages.
**Ani ( OpenSearch )** 42:23 Got it. No language center.
**Juliano Costa | Datadog** 42:26 How to instrument things Pr. Answering your question the package is Hotel Demo.
**Pierre Tessier** 42:34 Yeah, that's what they want to.
**Juliano Costa | Datadog** 42:35 The file. The file is called demo proto. But yeah.
**Pierre Tessier** 42:42 Naming things is hard.
**Juliano Costa | Datadog** 42:44 Tell me about it!
**Ani ( OpenSearch )** 42:46 Yeah.
we are. Still. We are still stuck with calling open search dashboards, dashboards, and severe the weirdest name ever.
**Juliano Costa | Datadog** 43:01 Hmm.
**Ani ( OpenSearch )** 43:02 You think about that? Like every device, a product called dashboards, which also has a dashboard.
**Juliano Costa | Datadog** 43:09 Oh, awesome. Yes.
**Pierre Tessier** 43:12 We're definitely over time.
**Juliano Costa | Datadog** 43:14 Yes,
**Pierre Tessier** 43:16 Let's make a call to get more approvers, more people part of this project, and it'd be great. If you both you should know, and and you could take a look at the couple of the Prs we identify. Certainly Cedric's Prs
I'm of the notion of Cedrics Prs and Hendrix, the the doppler. Well, Cedrics. Prs, we should just make those no collector changes, and Hendrix Pr. Does. There is some value in that one.
**Juliano Costa | Datadog** 43:42 Okay, tomorrow is public holiday here, but and I will take the day off. But I'll I'll make sure I move she know as approver.
**Pierre Tessier** 43:55 I'll be around tomorrow, Giuliano, to do some things.
Okay.
So it's because my.
I have a holiday. But the rest of my family doesn't. So it's it's 1 of those weird like, I said, when those weird days.
**Juliano Costa | Datadog** 44:10 Cool, appreciate the extra time.
**Pierre Tessier** 44:14 Alright!
Thanks, everybody!
**Shenoy Pratik** 44:15 Thank you. Bye.
