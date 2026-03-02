SIG: PHP SIG
Date: 2025-08-06
Duration: 94 minutes
============================================================

## Zoom Recording Transcript

Brett McBride 00:01:06 Alright, Bob, top of the morning to you.
Bob Strecansky 00:01:10 Good day, Mr. Mcbride. How are you?
Brett McBride 00:01:12 Yeah, I'm not too bad. Thank you.
Bob Strecansky 00:01:15 I'll tell you what I've I've started using that all the time, and I realize that I said I sound like a fake Australian. But it's good, because then you never get where the person you're meeting with local wrong.
Brett McBride 00:01:26 Yeah. Do you deal with a lot of different time zones.
Bob Strecansky 00:01:29 Yeah, I do into it. Has people in India, in East coast, West Coast Europe. So
as we say around the sun.
Brett McBride 00:01:40 Yes, yes.
Bob Strecansky 00:01:44 How's the baby?
Brett McBride 00:01:47 Yeah, she's going pretty well. I'm
yeah. Still, not thinking about my nearly year off of leave. And what I'm going to do with that.
Oh.
Bob Strecansky 00:01:56 When when does that start?
Brett McBride 00:01:57 It's still about 2 months away.
Bob Strecansky 00:02:00 Okay. So you Jodi's taking her time. And then you're gonna take your time after that. Is that the plan.
Brett McBride 00:02:05 Yeah, yeah, yeah. She pretty much high fives me on the way out the door to her job, and I walk on in. It's like. Did you ever watch Sam and Ralph? The sheepdogs
in the old bugs, Bunny cartoons.
Bob Strecansky 00:02:20 No, I I'm not familiar with the reference, but it sounds sounds like pretty relevant.
Brett McBride 00:02:26 Yeah, anyway, that's that's what's going on there. Yeah. Otherwise pretty good.
Made my way into town today and did some training at Amazon, Hq.
Was actually Grafana training at Amazon, Hq. For some reason. But
That was a bit of an adventure. Travel into
into town and catch a chart.
Bob Strecansky 00:02:51 How far are you from town?
Brett McBride 00:02:53 It's about an hour on the train into into Melbourne.
Bob Strecansky 00:02:57 Nice the
I remember going to Grafanicon in 2016.
That was one of my favorite conference that was like the 1st conference they had, and it was in Los Angeles, and I remember like thinking like this is dumb. Why am I going to a conference? For like a graphing you like a graphing Ui tool, but they
really good conference, and I learned a lot. But trim.
Brett McBride 00:03:22 Yeah, there must have been brand brand new back then, because I only became aware of it.
Yeah.
Bob Strecansky 00:03:29 2016, it might have been 20. It might have been a little later, maybe 2,018. It was like it was right when, like version 1 point oh was coming out.
And man that that tool has grown, leaps and bounds holy Canola.
Brett McBride 00:03:44 Yes, it has. Yes, that's what I was learning about today.
AI. Ops.
Sergey 00:03:52 Hi guys.
Bob Strecansky 00:03:53 Okay.
Brett McBride 00:03:54 See you again.
Bob Strecansky 00:03:54 Hellscape. My personal hellscape. AI Ops.
What were they talking about with AI Ops Brett. Anything anything notable that you can share.
Sergey 00:04:13 Is it like devops? Is it a continuation? Devops.
Brett McBride 00:04:18 Yeah, sort of yeah. But maybe not all. Maybe AI problem analysis. So they had. They had the open telemetry demo actually running. And that that sort of broken something.
so you could see.
you know things had gone red, and so he just brought up the AI chat and said, Oh, something looks broken. What do you think it might be? So? It's something really vague and whatever. And it's been like a minute.
Sergey 00:04:43 But I always wondered why it's not used more like
at all companies that deal with like Apm. Like application, performance, monitoring or telemetry like whatever buzzword we will change to in a couple of years. It's always kind of like was focusing on just presenting the data that we have, instead of kind of like already helping people with investigation of potential problems. And I've understood why. Maybe I'm missing. Maybe there are approaches that they want like, why, they're not presenting
like you come to this ui, and a system already presents you like try even can try to guess
no problem.
You're trying to present your potential problems that it is aware of. You can choose.
guess correctly. And from there it can suggest you. These potential avenues of investigation and resolution eventually.
because for me, like the problem, always like you get to the this new system like discoverability of features, right? You get to the system. But you don't know. What are you supposed to do to investigate instead of system just suggesting to you what are the.
Brett McBride 00:05:43 Awesome.
Sergey 00:05:44 Ways, maybe even signing them probabilities. So you can kind of like even realize what kind of like, but at least kind of helping you along the way, so that less burden on on a person
to understand what to do next. But is this what this Ops AI in this direction, or it's good.
Brett McBride 00:06:03 Yeah, yeah, it was doing a bit of what you say, like, it's still, yeah, look.
Sergey 00:06:08 So it's.
Brett McBride 00:06:09 Trivia to be.
Sergey 00:06:09 Maybe so you're saying that maybe there are technical reasons why it's not done like this. The we don't have technology good enough to facilitate it.
Brett McBride 00:06:17 Well, I think I think it's coming, because I saw I saw an implementation of it of it today, and it did some really clever things, you know, starting from a a dashboard which had some, you know, some red on it. It kind of.
and caveat like. There was a lot of metrics going on under the hood that it could see like you know, kubernetes.
Sergey 00:06:38 That's that's what we want from the system, right? We know
huge amounts of data. So it's impossible for the person to try to look at all of them. That's why you want the system to try and essentially summarize it for you and tell you what are the potential.
Brett McBride 00:06:52 In the demo. I saw that they've done something like, set the maximum database connections to a hundred so, and then hit it with a load test, so that, you know, if if you knew the right chart to look at, you'd say number of connections go up and then container crashes down to 0. And and it was doing that. And and so this little AI
assistant did actually manage to work that out and and really point you towards where an engineer should go and look.
So that that was but it was also sort of an engineered demonstration of of what could happen. So
you know, they made sure that they had all of the right
inputs available to to do that. I'm sure I would have.
Chris Lightfoot-Wild 00:07:39 Eaten.
Bob Strecansky 00:07:40 In a couple of years since I wore my sre hat, but I know that honeycomb, like they honeycomb I/O is really keen on solving that problem, although a lot of the Apm. As you all know, I'm sure some of y'all work with, and for Apm. Vendors, a lot of them don't have like really great
distinction between them, right? Like they're all just collecting data and metrics and logs and whatever, and then spin them back out. So like you need to kind of be able to differentiate yourself in the space that's getting super saturated. And I think that that I have a strong feeling, Brett, that that's going to be like the next
iteration right is like.
Oh, use AI to help with solving problems. Or, Oh, use AI like AI has the pager duty service right like being able to help triage issues and then hopefully, triage and remediate would be big.
Brett McBride 00:08:28 Yeah, I don't know that I want it to remediate anything but.
Bob Strecansky 00:08:30 I don't think I want.
Brett McBride 00:08:31 Way to look is a really good start.
Bob Strecansky 00:08:34 Yeah.
Nick Schuch 00:08:34 Give it admin coup access. Let's go retainer for you.
Chris Lightfoot-Wild 00:08:40 Yeah.
Bob Strecansky 00:08:41 That that credential is going to be read only for a very long time. There.
All right, we're here. Welcome everybody! Happy Wednesday, for all those that celebrate does anybody have any special agenda topics today before we start clocking through our open Prs and issues?
Let's rip, then.
Brett McBride 00:09:04 Yeah.
Yep.
Bob Strecansky 00:09:16 need a little macro that does this every week.
Alright, let's see go get some pull requests, migrate remove cloud trace propagator.
It's like this has and open.
Brett McBride 00:09:29 So I've I'm across that one. I'm just waiting on one change from the the author, just a minor one. We've got a bit of a plan
in one of the pull requests on on the order to do it. So it's basically switching something out from
from our core repo to our contribut repo.
Bob Strecansky 00:09:49 Got it. Okay, sounds good. Thank you. Brett, update Sig meeting info, think
in updated Google calendar invite. I guess we can. I prefer this, I guess we can merge it.
Oh, Sean hasn't drafted in a while.
Sergey 00:10:06 Link stays the same right. There will no change in the in the zoom link.
Bob Strecansky 00:10:10 I think. Yeah. The the zoom room should stay the same. I know that like.
Brett McBride 00:10:14 Just 9.
Bob Strecansky 00:10:15 I know that's yeah. These. This is just changing times. I know that the Cncf has a dedicated 2 dedicated Zoom Rooms, and we use one of them so
that should not change. Brett, you got spi for spam processors. This one's a little bit old, but it's.
Brett McBride 00:10:34 So I I've actually just done some work on that in the last couple of hours.
Yeah, I think I need to update the name, but otherwise I I removed the
the ht, matrix component out of it.
so now it's just basically tidying up how we do spam processes for for v. 2.
Bob Strecansky 00:11:02 Very cool. Thank you.
Alright. Let's take a look at control.
A lot of contribute requests open. That's good.
Oh, I saw this one yesterday.
There's
This one was just talking about adding, HP, method, Http route looks like you approve this one, Brett
Urget will.
And then this is that same person that was working on the open, the one in the main repo.
Brett McBride 00:11:35 With the same. Yep.
Bob Strecansky 00:11:37 And then
I know we were. I know I saw stuff about postgres auto instrumentation. But I think you had your finger on that pulse? Didn't we merge a.
Sergey 00:11:47 Is it also working on that? Is it different?
Brett McBride 00:11:49 Think I think I did merge the other, which probably means that one can be closed.
Bob Strecansky 00:11:57 Oh, yeah, just wanna mention, I'm working on the same implementation here. I'm just gonna this one
3 weeks old, probably hasn't been mentioned. I'm just gonna close this.
We believe this is a duplicate.
And if you have additional shares or concerns.
all right. Okay, sorry.
Across here.
These are relatively old. Is there anything anybody here wants to talk about?
Should we close some of these old ones or leave them open.
Chris Lightfoot-Wild 00:12:46 You've got a style, but I don't know. Is it? Is it kicking in on these ones, or.
Bob Strecansky 00:12:51 Mine at the bottom. But
yeah, I wonder I don't know why it's still about isn't kicking in for this. Maybe it's not available.
Believe it.
This repo.
Brett McBride 00:13:02 Yeah, it it kicked in like it hadn't run for ages. And then something changed. And I it might have been when our Trask
was sort of changing permissions in our
repos, so it might have been missing a permission in.
I feel like that happened in the core repo recently.
Bob Strecansky 00:13:22 Very, very welcome. I'll take a note to ask about that.
Chris Lightfoot-Wild 00:13:25 It seems a bit hit, miss. Doesn't it? Like I don't see it being on the regular. It seemed to come in at 1 point do something, and then I've not seen.
Brett McBride 00:13:31 Yeah, you're I remember it being regular for a time, and then it just stopped and no one noticed. And then you really notice, kicks in again.
Bob Strecansky 00:13:42 Yeah, sorry. And yeah, obviously, that hasn't worked on this repo for a long time, because this Pr has been open for over a year.
and these are all marked still.
Yeah, I'll follow up.
Chris Lightfoot-Wild 00:13:55 Pick up that bottom one, though. Again I was in my head, just thinking there'll be a perfect time to do it, but I don't know if that
what I was waiting for, if it was like v. 2 of the.
Brett McBride 00:14:07 Which one was that Chris? Sorry.
Chris Lightfoot-Wild 00:14:10 The liable instrumentation at the bottom.
Brett McBride 00:14:13 Oh, yeah. Yeah.
Chris Lightfoot-Wild 00:14:13 Using spi quite heavily. And
yeah. So I guess maybe some discussion around what the V 2.
Brett McBride 00:14:21 You know. Let's we were waiting, waiting for. I've I've long forgotten.
Bob Strecansky 00:14:29 You mean you forgot about a Pr. That was open 14 months ago. Brett. Come on, man.
Brett McBride 00:14:33 Oh, shit.
Chris Lightfoot-Wild 00:14:34 What's happened.
Bob Strecansky 00:14:36 Haven't.
Chris Lightfoot-Wild 00:14:38 Is, is no doubt stale, so I need to obviously pick it up again. But it was more 2 stuff, and obviously you've got a Pr going into v. 2 now and with the spi things.
I wondered what if you want to discuss that at some point.
what the plan was, or it with outlined. The plan was.
Brett McBride 00:14:57 I don't think it was waiting on v. 2 of the SDK. I think it was just.
I thought it was more about just stabilizing what
Laravel auto instrumentation did, so that we were happy with it. There.
Chris Lightfoot-Wild 00:15:13 Yeah. Well, the the reason it it kind of got a a bit stuck. Was, there was a couple of things where people had reported issues. So I was like, Well.
wait until those are out of the way. But it was more than in general. But this spi usage in here.
I don't want it to
align with what was happening with the SDK.
To a degree as well. I I know there's a split between some spi stuff in v. 1, and then more and more of it in SV. 2.
But I wonder what the when does v. 2 become a thing?
Do I target this at v. 2, and actually have liable instrumentation v. 2, instead of 1.1.
Just bump it because really depends to initially
free version. But someone's then added that in anyway, before this pl. One did so.
Brett McBride 00:16:06 Yeah.
Chris Lightfoot-Wild 00:16:07 Split.
Brett McBride 00:16:09 I mean, the public interface doesn't change, doesn't even have one.
so it it's not necessarily breaking. We should. We should think about that.
Sergey 00:16:20 Yeah, I you mean, I wondered, when instrumentation is considered to be breaking, breaking the changes right as long as produces data
that is compatible.
Does it matter if the code changed drastically? But I wonder, like, in the other way around, right, it produces a little bit different data. Is it considered to be.
Chris Lightfoot-Wild 00:16:40 Was dropping 6, 7, 8, 9, 10, or something like that. Oh, maybe up to 9.
Sergey 00:16:47 Drop in some.
Chris Lightfoot-Wild 00:16:47 So I thought that that felt drastic enough that maybe actually it should be a major bump.
Sergey 00:16:52 Yeah, I I agree, probably drop and support versions probably will justify.
Chris Lightfoot-Wild 00:16:56 It's not to say it doesn't work with them because it like it. It maintains all of them at the moment, but then it gets obviously more and more involved to maintain
and.
Sergey 00:17:06 Are you saying?
But you want to drop them so it will be easier, or it
deprecate. So it will be easier to completely drop in the future.
Chris Lightfoot-Wild 00:17:14 Yeah, just like the the viral framework introduced like changes. And like, you know, new static things. And you know things that are incompatible without version checks and property checks, and
you know.
Sergey 00:17:27 So you do want to drop. Then.
Chris Lightfoot-Wild 00:17:29 I'd rather get the older version instead.
Sergey 00:17:31 Go to version 2 or instrumentation, so you can completely drop the.
Chris Lightfoot-Wild 00:17:35 Yeah, I'd rather so stay more in line with what's currently supported with the framework than that's, you know, 5, 10 years.
Sergey 00:17:42 Our policy in general, the same as for Php itself, only support this. The versions of technology that is supported by vendors themselves.
Chris Lightfoot-Wild 00:17:53 I don't know if we've got a policy for that.
Sergey 00:17:56 Itself, right.
Brett McBride 00:17:57 I feel like it is, yeah.
Sergey 00:18:00 Although I don't know if it's the if we can parallel it, because in Php there are also considerations like security issues.
it probably might be relevant also to technology, especially for frameworks.
So it would make sense to say, Okay, if vendor dropped it, maybe we should else.
Bob Strecansky 00:18:16 The whole Php security thing is always like a fun negotiation, because how many people are still running? Php. 5, 3, and 7, 4, 7, early 7.
It's.
Sergey 00:18:25 Places. Raise your hand. If you have.
you can say, Okay, but I'm good. I'm doing a disservice to people. If I'm providing them support for telemetry right? Because they will stay on this insecure version longer.
Bob Strecansky 00:18:39 For sure.
Brett McBride 00:18:40 And and really.
Chris Lightfoot-Wild 00:18:41 They've got as well that works.
Brett McBride 00:18:42 We do still have older versions that work with older versions of you know, we're we're not taking it away. You're just
stuck on older versions of of the of the package.
Sergey 00:18:52 But I assume our approach is more selfish, right? If it, if it was easier to support, we probably wouldn't care with drop old versions. But as long as it becomes harder to support. Like you said, you need to introduce all kinds of
version discovery and different approaches based on version. Then.
Bob Strecansky 00:19:08 Yeah, we.
Sergey 00:19:09 It was rapid, right.
Bob Strecansky 00:19:10 Yeah, we have to be selfish. Right? We only have. We have very limited resources. And we are we are providing the exact we are providing the exact support we are being paid to pro paid to provide.
Sergey 00:19:23 Yeah. So if it's a consensus that it's okay to drop
So then
maybe like, if you have a considerable number of versions that you would like to drop Chris. Maybe it would make sense then to go directly to version 2.
Chris Lightfoot-Wild 00:19:36 Yeah, well, I'll try and pick this up, then again, and make it not style, and then incorporate some of the changes. And
Brett McBride 00:19:42 See if we can get hold on that.
Sergey 00:19:44 Maybe you know, maybe you don't want to make it kind of like all all in one thing, like, if you just want to switch, drop the versions. Maybe it's better to do in one step and then to do everything you wanted to do them incrementally. If it's not interdependent, right? But otherwise you're trying to do a lot in one. Go, and
that's you will be blocked. Usually this is what it ends with. Right. If you're trying to
put too much in one change, then it will be very hard to to do it. One go.
Chris Lightfoot-Wild 00:20:12 Yeah, that makes sense as well.
Bob Strecansky 00:20:18 Okay.
yeah. I think that was all. The trim stuff.
No auto, no instrumentation. Prs, no new overflow questions.
Couple of things in our prioritized backlog.
Chris Lightfoot-Wild 00:20:38 That top one in progress. Actually, you merged that this week, didn't you? Thanks, Brett. The Spi stuff in call.
But maybe worth following up on that issue to ask if they could give it a try potentially
for the.
Sergey 00:20:56 Asking if I had a chance to try. Not yet.
Chris Lightfoot-Wild 00:20:58 No, no! So sorry in in progress. The the the top issue.
Brett McBride 00:21:05 Oh, right the the dot enveloaders. Yes.
Chris Lightfoot-Wild 00:21:09 Yeah, you you moved that in. I don't.
as some kind of thing. Oh, yeah, or it's just in main still. But we could ask them to potentially give it a go.
Brett McBride 00:21:19 Yes.
Bob Strecansky 00:21:22 Different. Guy.
Brett McBride 00:21:23 It's have I tagged it and released it yet would be the next question.
They might. So it might. It might not be in a in a in a released version of
Chris Lightfoot-Wild 00:21:35 So they could. They could try manner right? It will still split.
Brett McBride 00:21:39 Yes, it would. Yeah, you could install main. Yeah.
that's not a bad idea. Get some feedback. It works before we tag it. If.
Sergey 00:21:54 The way. The subject of the issue is a little bit misleading. I guess so when they say when loading configuration files, they don't mean this declarative configuration file right? Because with declarative configuration file, that would be the expected outcome. Rightn file will be ignored in that case.
So they probably mean Ini file and and the environment variables.
Right? This is what I mean as well.
Brett McBride 00:22:20 I think you're probably right. Yes.
Chris Lightfoot-Wild 00:22:24 When in Laravel. I guess people treat dot envy as configuration files in like not open telemetry lingo, but Laravel lingo.
Sergey 00:22:34 No, but they but they will say they say, when loading configuration files, it sounds like there are multiple configuration files, and one of them. They would expect it just to tender to work
so, but they probably mean the 10.th And then the rest of it, environment variables. And I. And I,
yeah, do you know, if do people even use this declarative thing, or almost 30 years.
Brett McBride 00:22:57 Not very much. No.
Bob Strecansky 00:23:05 Oh, look at that new project board! Call alright cool!
Is there anything else.
Sergey 00:23:13 Do we have some time left? I kind of like had a question that oh, do we have most.
Bob Strecansky 00:23:17 Yeah.
Sergey 00:23:17 Go through.
Brett McBride 00:23:18 Yeah, we do.
Bob Strecansky 00:23:19 Yeah, let me.
Brett McBride 00:23:19 Yeah, there's more stuff. We've got more time.
Bob Strecansky 00:23:21 Yeah, let me. I was just looking. There's nothing on the SDK. V. 2 that's really super
pressing and nothing really cool on the statistics. So the floor is yours. It's okay.
Sergey 00:23:32 I I saw some issues regarding the metrics. I was just wondering. I wanted to ask,
what is the current situation with metrics and Php, we wanted to kind of like expose part of this distribution to provide like CPU memory metrics. And I was wondering currently we have metrics, but if people want to use them, is that something that will be kind of collected? Your request, and then send at the end of the request, what is the current approach with the metrics? How how do they work? Currently.
Brett McBride 00:24:02 Ow.
think your so so the main issue with metrics, and this this applies to shared nothing. Runtimes. Apache fpm.
is that?
Oh, the metrics are.
It's described in an issue somewhere, but effectively. The metrics keep clobbering previous metrics, I think, in in lay persons terms, and that's about the extent that I understand it. Yes.
Chris Lightfoot-Wild 00:24:36 Humility.
Brett McBride 00:24:37 Is a problem.
Sergey 00:24:39 When you say global, you mean on the receiving side which we send, the those kind of like objects that contain metric value.
Brett McBride 00:24:46 Countryside.
Sergey 00:24:47 So just override them, override the previous value.
Brett McBride 00:24:50 Yes, yes, and I I feel like it's a Prometheus issue as well.
Sergey 00:25:00 We push them out right.
I know that there is a pool model push model. I don't know which Prometheus works in, but open telemetry works in push model, right? So the.
Brett McBride 00:25:09 Doesn't get.
Sergey 00:25:09 Pushes collector the value for metrics, right.
Brett McBride 00:25:13 Yep.
Sergey 00:25:15 So.
Brett McBride 00:25:15 Details.
Sergey 00:25:16 So I assume. Then there are some ways to mark metric as kind of like. Maybe there is timestamp like like. For example, if I want to push a memory memory usage or CPU usage value outside, like.
I assume it should be somehow timestamp. And it's okay that it will be like the receiving side should understand that it's a value that corresponds to that timestamp. I you're probably talking, maybe, about some kind of like gauges like counters and stuff like that, they they will override each other. This what you meant.
Brett McBride 00:25:49 It's it's well described by in an issue. I don't know what the issue is at the moment, but that'll yeah. But that's that's the main issue that I'm currently aware of with with metrics.
what other problems there, there are some minor like the spec has changed that we haven't updated, you know, the aggregation temporality for a couple of instruments?
as I remember
But those that those seem fairly minor.
Sergey 00:26:25 Maybe I will rephrase the question. So let's say, if I want to send a metric that will, you know, account for CPU usage.
Is that something that is already available, and I can just include it in my composer, Json, and it will send it, at the end of which request or.
Brett McBride 00:26:41 No.
Sergey 00:26:41 For example.
Brett McBride 00:26:42 No. So so the Api and the SDK to
send metrics is there, and and working, as far as we know. But we don't have any. We don't have any code or any packages that will generate metrics.
So you would need to write something.
Sergey 00:27:01 Nice.
It looks similar. Let's go ahead.
Bob Strecansky 00:27:05 Yeah, I was gonna I was. I would also be curious as to your use case for that. I'm just like more curious than anything else. What like? In what case do you want to write.
Sergey 00:27:13 Yeah. So let's say so. Let's say we have a presentation for a service that we monitoring with the telemetry for. Php, right? So we're monitoring it. We send in spans so we can construct all this. Trans, you know. Trace flows, and that's fine and good. But also, maybe some people want to know what's going on on that environment while those spans were running right?
So they would like to see, what is the? So yeah, we can say, Okay, but you need to install, maybe a different tool for that. That monitors, the environment. But maybe they just want to install this open telemetry distribution again. It doesn't need to be part of the SDK, maybe, but
this is at least how it worked in classic, elastic agent so so far. But I was just wondering, are you guys thinking that this use case? So let me finish describing the use case. So so essentially, they expect us to send data, and then they will populate some kind of like dashboard. Right? So you see, on the some part of the dashboard, you see what's going on with your kind of like transactions, like a request, like how many of them, and with errors? So you can drill
deeper and see what were the spans on those requests, and then on the same dashboard. You might also want to see what was going on with the environment at that time. Right? What was the CPU usage. What was the memory usage related to those Php processes? Right? So so I guess to some degree it makes sense for that tool to collect them, although you can say, no different tool should collect those metrics. And we can maybe create some kind of like correlation based on
timeframe. And the id. Yeah, yeah, I agree there, that might be not the best fitting tool. But let's and I would be glad to hear you guys feedback if if you consider this use case outside the scope.
but like, for example, collecting metrics such as CPU and memory, is that something that open telemetry metrics suited for, or
because other other agents, for last, we just trying to follow the example that they already did it. They implemented it for python, and I'm not familiar if if they use something that is already exists upstream in open telemetry, or they implemented it. Elastic specific. But yeah. So what do you think about this use case.
Bob Strecansky 00:29:26 That's not. I think it's not instrumented that way right now. I don't think it would be super duper, complicated, because, like we have all the the we have the ability to push Prometheus metrics, using our package right like our open telemetry metrics, packages written essentially as a thin shell wrap around the the Prometheus package. So I think that that would be
okay. I think in practicality, if it like. If it was me doing the work on the other side. I probably just like install node exporter, and correlate the spans that I have with the specific time from
then from the note exporter package, because that gives you all sorts of really great system metrics, and it's like a more curated package and consistent. But I totally see how you could want to have, like very explicit pieces of data coming from metrics that correlate to your spans and your logs, whatever. So like, I definitely see the utility and what you're talking about, Sergey, but we know we haven't prioritized it yet.
Brett McBride 00:30:22 And my.
Chris Lightfoot-Wild 00:30:23 Next.
Brett McBride 00:30:23 That Sergey would be. Yes, we have the Api. Yes, we have the SDK. Yes, you can do it.
Sergey 00:30:30 For example, if we implement such a package, it would it make sense to contribute it upstream to put it in contribute like? Do you think it will be interesting to people? I I'm I'm at this point. I I need to even evaluate like, will it even work with vanilla? SDK, or we will need to use the powers of extension kind of like, run it in.
because we obviously don't want to add overhead, right? So maybe we will collect those metrics in the background, so that also might be a challenge in that sense all the issue with the, with the blocking calls with which we don't want to do in the context of requests.
Brett McBride 00:31:04 That.
Sergey 00:31:05 But yeah. So Christie, also, yeah, please go ahead.
Brett McBride 00:31:10 Yeah, I I think your bigger challenge is only doing it once. So you've got one, you know. Apache Web server with, you know, 100 workers which one's going to generate the metrics. So.
Sergey 00:31:22 Do you think we should do it only once, like it would make sense to collect them? Per the id, right? Because you do want to understand. Okay, this one handled it because the correlation between the request and which request caused that you, Spike, might be valuable. Right? So you do want to understand which of the workers use that CPU or memory, so that that correlation might be valuable.
But I it still can be done in one process. So this by itself is not.
It's something that forces us. But even if we do it in one process, then it becomes even more of an issue to do it in. SDK, right? Then we'll definitely need extension what? I will mention a couple of times this. He's working, I think, on that this additional process that will be forked and it will be responsible for all the background activity and including this. But then it will definitely need an extension. It will not be possible to do an SDK
unless 4 can process from SDK, but I don't think we want to do that.
Yeah.
Brett McBride 00:32:20 So so doing, any contribut, and and and, as part of you know, a a request, lifecycle seems.
Sergey 00:32:28 So like. If the way I envision what can be contributed to country is essentially
implementation in well, I wonder if we can do it now in Php. Because if we will run it in the background, then it must be native, unless we will go with this external process. But even then
I don't know if we want to invoke Php in that context. But yeah. So
I guess. But you you guys ever need this kind of a shot like in your work, like when you use open telemetry. Do you ever want to correlate with the environment and to use like a different tools, and you correlate them based kind of like on this additional parameters like time, frame and id and stuff like that. Or
you're not familiar how it can.
Bob Strecansky 00:33:10 I think, from my perspective, and above your breath, too, because he looks like he has his mouth half open. But from my perspective this isn't something that we would do because of like with volume, we can sort of correlate to when we have actions that are high CPU or memory spike, and we can, the spoiler alert. They end up all being database calls so like the actual
process, is very, very infre, at least for us, is very frequently, infrequently the culprit, so like the spans around the database calls, and having those like the long time. But CPU and memory usage
for us, we tend to monitor more like system level or like Kubernetes, level rather than individual process, individual call level. I think we might be worried about volume and cardinality of that data. But I'd be interested like I would be interested to see if it could work effectively, because I think it would be that might have some really neat some really neat use cases.
We tried.
Sergey 00:34:07 Yeah, we even planned like a Java implemented correlation even on profiler level like that. They correlate it kind of like a profiler. That much contributed already upstream to open elementary.
correlated with the telemetry data. So you can see spans versus all these flame graphs that show even not instrument, even native libraries that were invoked
on that timeframe. But yeah. Okay, any other, Chris, are you? You.
Chris Lightfoot-Wild 00:34:35 Yeah, sorry I was. I was, gonna say my understanding in lieu of any kind of support from the distro, or, you know, building that into the instrumentation was that
open telemetry collector has got host metrics
module to it. And if you were in like a sidecar, the idea would be. Obviously, that would cut the entire metrics for that.
So that that was how I'd plan to use that, you know, through work.
And I think the point that you were suggesting. Obviously, you don't get per process.
Metric.
Sergey 00:35:09 Plan to add some kind of like Plugin into a collector that will collect them.
Chris Lightfoot-Wild 00:35:13 The open telemetry collector already has host metrics. So you can Mount Proc into it, and then it can. You know, script, that on whatever cadence and ship that out. So it wasn't part of Php per se. But you get that as like asynchronous part of the test definition or whatnot.
Okay.
Sergey 00:35:31 So it will be run per kind of like per host thing to collect per.
Chris Lightfoot-Wild 00:35:36 Yeah, yeah, that's right. Because obviously, you could have
depending on how you've set up like multiple threads or Fpm workers serving requests on one single host. So I guess you don't want each one of those to say I've got.
You know, CPU usage is at 80%, because you've only actually got one CPU. 80, not 20.
Sergey 00:35:55 Yeah, if you bring threats to do it, it will make it absolutely more complicated. Because, yeah, then you will need to. Yeah.
especially if those threads can be suspended with fibers. So that becomes, I agree, even more complicated. But assuming that we have simpler model per pid
Chris Lightfoot-Wild 00:36:12 I put a link in the chat as well, so it might not have been relevant from my basic understanding. But when I was looking at in the past about gathering metrics.
and it was that the thing about the shared nothing like Brett was saying the count resets to 0 every time.
and you kind of stumbling block. I got to this code
Sergey 00:36:33 Yeah, I remember, we discussed. But then I assume those metrics. So if I understand correctly, most usage that you guys currently encountered, it's for kind of like all kinds of internal metrics, so people do all kinds of gauges counters, and they send them. So the current approach and the way SDK exposes those Apis
is mostly because people want to just create ad hoc metrics. So we don't have any country packages, because people mostly use metrics Api for ad hoc metrics, that they do want to fly pure application right? So there is no point of packaging anything as part of the country.
Bob Strecansky 00:37:10 Did did I understand correctly, or.
Chris Lightfoot-Wild 00:37:12 But the the my, I guess understanding is perhaps lacking. But how do we count that
to increment and and work in the ecosystem? Because that's the bit I wasn't sure about.
But you you needed. I thought you needed some S something central that kept a long running counter that made sense when it exported.
Sergey 00:37:29 Well, you, you have this. You have this temporality that Brad mentioned. Right? So if you just want to increment stuff, then you can just send deltas, and then the receiving side will be aware of that, and it will increment it centrally for you.
Brett McBride 00:37:43 Yeah, I feel like I feel like that was.
Yes, I assumed
exactly as you have, Sergey, but I feel like I suggested that in that very issue. And it wasn't the answer.
But.
Sergey 00:38:01 But I wanted to know what back end they use like. Where do they send the the metrics like? I know that in elastic. We also had some issues of but I think it was specific to histograms or something.
There was some kind of like issues with the deal and with the with delta temporality. So maybe because obviously Delta makes it harder to deal with it in distributed way. Right? So because then Delta means that you will need to somehow always find your initial value and then recalculate everything from that point unless you do it somehow. Cache.
cache it, you know, while you receive the data.
because, yeah. So, having values already been absolute makes it simple. Right? You? Then you don't need to go
back in time and find the initial value from which you need to, you know, accumulate all the deltas.
So I was wondering, like, maybe it depends on the backend. Maybe backend cannot do it. Then using Delta is
is it possible for? So that's why.
maybe. But I will take it. So that's the same issue. We're talking about the the one that you sent, Chris. That's the issue. Where those those counters came up were delta versus not delta.
Chris Lightfoot-Wild 00:39:09 I feel like it was. I don't know in all honesty I don't know if I was on the right path or not, but it mentioned about the Delta temporality. And then, just before that, there's a block of code where
takes the it's comparing like the data points and drops the older one, so it only ever counts the one where it's just bumped up from. You know you've got a request counter, and it's gone from 0 to one.
Every request commits that metric, and then you only end up with one in the account, because it's always using the latest one
and it didn't. I didn't find a way of working around it.
but I could just be wrong.
Sergey 00:39:43 So they just wanted to implement a metric that will count the requests.
Chris Lightfoot-Wild 00:39:47 I mean, that's how we do supply at work where we're, you know.
bump in a simple counter. But
Sergey 00:39:53 Right, so so.
Chris Lightfoot-Wild 00:39:55 It makes sense, for example, to provide this.
Sergey 00:39:56 Part of the country, so people will just use it. So if we know how to do it.
maybe put into in the country will make sense like, is this something that like request counter metric? And then we'll just people don't need to then. But I wonder, like,
do we have any examples like, what is the.
I guess? What is, what is the standard implementation of the we know bacons that will correctly interpret like? Because
with spans. It's a little bit easier. I guess it's the kind of like safe self contained.
But I guess, like, for example, if we would go for this delta temporality. And this is how we implement this request counter metric.
I wonder
do we know if Bacons will be able to deal with it like? Can we go and try it on like, what are the Bacons that we usually try it on like Zipkin or
Yagara like?
Do do you guys have any experience with the with using metrics, with the some backends that can get can represent open telemetry, metrics.
Chris Lightfoot-Wild 00:41:02 I haven't been able to crack any metrics stuff yet, so
I've I've.
Sergey 00:41:07 If I'm hearing you correctly, guys, it's a bit of virgin field. We need to to see what's going on. But a lot of experience.
Brett McBride 00:41:14 It is. I suppose the the approach I'm planning on taking is
having. So this is in a Kubernetes setup, having kubernetes emit all of its Prometheus metrics with labels
and so my containers are running in a
in a pod. So we add labels, and the collector can do this already. Add labels to that telemetry to associate it with the Kubernetes cluster and the I guess the host, or whatever it's on.
and use that to correlate host level metrics with traces.
Sergey 00:42:05 But this is done completely outside the open telemetry for Php. Right? The the mechanism that knows how.
Brett McBride 00:42:10 It is outside.
Sergey 00:42:11 Fix those.
Brett McBride 00:42:11 Okay.
Sergey 00:42:12 Part of the metric Kubernetes. How we call it integration, or is it? Is it some kind of plugin on collector that knows how to collect it? Or.
Brett McBride 00:42:21 Yeah.
Sergey 00:42:22 Okay, so.
Brett McBride 00:42:23 It's a oh, I can't remember what it's called
but yes, it. It enriches
traces by adding kubernetes, node information, or cluster information, or both.
Sergey 00:42:40 Right. So so
just to get you guys in practice of so far the way we envision the usage of metrics
as part of the SDK for open telemetry. Php, it's mostly for kind of like ad hoc metrics kind of like counting some business logic stuff. So if people have something that
specific to the application, then they can use Api for the SDK, and so so essentially, it's by itself. It's not clear what can be provided. So
like we, we don't have like clear cases to somehow tie it, maybe to support in some frameworks like Laravel.
we we don't have those use cases in mind. So far, right mostly that was just most exposed as Api. And people then can use this Api for ad hoc metrics specific to their business, logic, or whatever they.
Brett McBride 00:43:29 Yeah.
Sergey 00:43:30 Right.
Brett McBride 00:43:31 Yeah, that said there, there is someone who's
sort of trying to get started working on generating database metrics from some of our instrumentations.
And that that makes some that makes some sense.
Yeah. But but beyond that no, not yet.
And it it just hasn't come up yet.
Sergey 00:43:55 Okay, yeah, no. It makes sense, like, I guess it makes sense like to say, Okay, these rotations will generate the spans. And if you want to convert them to metrics, you can take spans and convert them on collector or whatever
whatever. But yeah. So not to duplicate the functionality and make the instrumentations also generate metrics. Right? Because then there will be some duplications, I guess. Okay, okay,
I was just wondering, like, I'm trying to to see like what? Because, for example, I know that in classic agent, sometimes we use metrics to deal with sampling right? So if you have sampling, sometimes you would want. Okay, let's at least generate metrics for sampled out requests, because at least have some visibility in what's going on.
instead of just completely dropping them, and then only only extrapolating, sampled in requests right instead of having some exact information about sampled out. But obviously you cannot go and collect all the information, because then
it will effectively be sampled in as well. Right. You will just not send it, but
you might incur all the overhead of collecting. So that's but I was wondering like, it's interesting a question like so. But so far we didn't have any example of something that we want to collect as part of the open telemetry itself. It's mostly Api for users to use directly.
Brett McBride 00:45:13 So far, that's true. Yep.
Sergey 00:45:15 Okay. Thank you.
Nick Schuch 00:45:17 Excuse my
excuse my lack of depth of knowledge. But would it be handy to get instead of
you know? CPU, memory of the of the container or the host that's running, running the process and emitting that as metrics, would it be handier to
grab like memory utilization of a request at that point more about the Php process rather than the the actual.
You know, host or system, it's running on. So I'm thinking, like.
I've used tools like Spx, and things like that, so it'll give you like a over you. You do a request, get a trace well, and then it builds out your heat map, but it also gives you a line about the memory consumption.
Sergey 00:46:06 So understanding? That is it. What is the specs? Is it? Is it a Php specific tool, or.
Nick Schuch 00:46:12 Yeah, yeah, it is. Yeah, it's
pretty handy. We use it a little bit. It's an extension, gives you a little web interface. You turn it on, and then you can generate heat maps out of it.
Sergey 00:46:23 Yeah, technically, you're right. I mean, I agree with you that doing it, your request would make a lot of sense, but you can do it with metrics as well. Right? So essentially, it's just a matter of how you essentially how you present it. But yeah, sounds like we can collect usage at the beginning and at the end of the request, and then we can send it, and it can be interpreted as a delta, a pure request, on the on, the on.
Nick Schuch 00:46:46 Yeah, yeah, it was just like it was. It was less about the tool and more, just about like some of the data I'd grabbed out of that like around like going. Oh, like that! You know that trace, or that period of time, that request, or that.
Sergey 00:47:00 Yeah, you hit the nail on the head. Because we essentially, we're already in position where we inside the process, we can collect richer information more fidelity than anything that can be collected from outside. And we can minimize. So instead of, you know, requiring people to install
our open telemetry and then additional tools, which is space that you mentioned, and then maybe even making it harder to correlate because spans. They come in this format, and space maybe shows it in its own ui. So you need to open both uis to try to correlate, based on pids and timeframes. So if you can collect all this information in one back end. Then maybe it will be easier for people to
to see the data in one pane of glass. Kind of like thing. Right?
Yeah, yeah.
So that's that's essentially the purpose. Yeah, purpose is to have all the data in one storage back. And if you can query it, and if you also have ui for the storage that will present it. Yeah, so that that's the goal. Yeah.
so
yeah, okay, okay, I just wanted to to see what is the current landscape and to understand how we can contribute. And
if that use case is even though you guys thought about it. But okay, but I will investigate. I will say I will report later
if we will find some some ways that we can already contribute? Or should we wait until extension is contributed? Then that
that is because, yeah, we have an issue here. Beach piece kind of has this inherent limitation of what can be done in the context of the request.
And everything needs to be done in the context of request. So, fortunately we cannot do anything heavy.
I don't know if querying Apis that will give CPU and memory can be considered heavy. Maybe not.
We'll need to run experience to see.
Brett McBride 00:48:52 And and this is where Paul's proposing, you know, like a separate thread, to do all this background work.
Nick Schuch 00:48:58 Yep.
Brett McBride 00:48:59 Outside, of.
Sergey 00:49:00 If you go to thread, then you immediately cannot do it in php, right? Then you need to do it in native.
Yes.
that's kind of becomes an immediate limitation. So yeah, we'll need to consider pros. And cons, I agree with you. Yeah.
Brett McBride 00:49:19 That's it.
Sorry are we done talking about metrics?
Sergey 00:49:25 No, guys, if you have initial ideas. This was the only question that I had in mind. But if you have additional ideas in that area I would be glad to hear. Please go ahead.
Chris Lightfoot-Wild 00:49:38 Well, mine was only that I'd love to use metrics, but just having them. My understanding is that it can't get it to work currently because it needs some other thing of tracking account or whatnot. So not put any real time into it. But
if there's a solution there, I'd love to.
Yeah, we've got in next week.
Brett McBride 00:49:56 Different run times like
You know, road runner, react those
Chris Lightfoot-Wild 00:50:04 Hmm.
Brett McBride 00:50:04 Sort of modern ones where the process is long running and serves multiple requests. But yes, I don't.
I don't think it's a solved problem, working in, say, Apache and.
Chris Lightfoot-Wild 00:50:20 Yeah.
Brett McBride 00:50:21 Solve. No one's looking at it either.
Chris Lightfoot-Wild 00:50:24 I wonder if we should be using like one of the Psr Cache implementations, and like saying, the count is backed by that.
and you could use spi at some point to.
you know, or or to provide one or something along those lines, that the count is external and
can be incremented. And but obviously that's it seems, seems very custom and opinionated.
Brett McBride 00:50:44 Yeah, it's come up before I I yes. Now that you've said that, I can remember someone talking about, you know.
Why don't we use Redis, or you know something as a as as storage for these metrics to work around this problem.
Chris Lightfoot-Wild 00:50:59 Currently we.
Brett McBride 00:51:00 Hasn't gone through.
Chris Lightfoot-Wild 00:51:01 Things are ready.
Brett McBride 00:51:01 Audio.
Chris Lightfoot-Wild 00:51:03 Hmm.
We currently stuff stuff into Redis
that is then scraped and then pushed like cloudwatch. So it's totally outside of open telemetry. But obviously it'd be great to just say, Oh, yeah, open telemetry does this, and use the Api and throw whatever metrics they are script somehow, and end up wherever we want to put them.
and then it's easier to sell.
Sergey 00:51:24 So
wouldn't. Even if you solve the problem per host, you're collecting it correctly, discount per host. But if you're running multiple hosts.
wouldn't you encounter same problem, or is it somehow.
Brett McBride 00:51:36 No, because they should have different resource attributes, which is a important identifying part of.
Sergey 00:51:42 Okay. So then it will be solved. But it's also a good. Okay? So then the fact. So you're saying, the problem is only so you you can. You can distinguish between them your Pid. The problem is, if you're sending it from the same Pid, then then it will override itself. So that's the only issue that needs to be solved.
Brett McBride 00:52:01 I think that's it. I think so.
Sergey 00:52:03 Okay.
Brett McBride 00:52:04 I'll I'll try and find the the issue.
Sergey 00:52:07 So you're saying, if it was working like you mentioned in the context of long running cli process like reactp, then there is no problem. Like, as long as you keep this counter in memory of that process.
the fact that they will not override each other. Multiple processes can send the data, and because of the resource attributes they will be distinguished
so they will not.
Brett McBride 00:52:27 Danger, yes.
Sergey 00:52:30 I see.
But then you're saying the result in whatever tries to more understand those metrics that it will understand that it needs to kind of like, maybe summarize them like there is some understanding of the meaning of that metric that, for example, it's number of requests on it will just sum them up right.
because obviously some metrics would not make sense to sum them up Alex D. Or whatever
so I wonder like
if it knows that it needs to sum them up, then it seems a solution, then to just add some attribute that is a timestamp or something, and then you will also solve the problem. Even if you have a regular process. Right then, with that additional attribute, they will not override each other, because they will have a different timestamp or something.
Brett McBride 00:53:17 Yeah. Doesn't that give you cardinality explosions, though? I that seems to seem.
Sergey 00:53:22 So how that additional attribute that allows you not to override it will also contribute to cardinality automatically.
Brett McBride 00:53:28 I think so, I see, so there is no way
it because I haven't. I haven't worked with metrics enough to have good answers to to
to sort of these low, level questions. Sorry, Sergey.
Sergey 00:53:44 I see, but that's interesting, because it's interesting that you're saying so. There is no inherent kind of like metrics by themselves, like you remember the Api. They don't have an inherent kind of like understanding of time time line kind of set up because
a lot of metrics would make sense for them to be mapped to the time point in time when they were measured. Right?
So I wonder? Because then it makes sense like understanding. The time
point is a special thing and should not contribute to cardinality. Right? It's not like Host Id, or whatever.
Brett McBride 00:54:14 Oh, yeah, yeah, yeah. Time, certainly. A part of of metrics. Yes.
Sergey 00:54:18 By the way, if you consider it the Id. You might also have a lot of those I also kind of like cause
Cardinal to expose. I wonder like, if system.
that process, those resource attributes they have understanding what should should not be. But maybe the idea is not big of an issue.
but you're saying a matrix Api does have kind of like a time time stamp understanding like it understands that some metrics per timestamp.
Brett McBride 00:54:47 Yep.
Sergey 00:54:49 Okay, I will take a look.
Brett McBride 00:54:58 Yes, I'll I'll try and dig up the the issue that I'm thinking about, that that talks about about some of these.
Sergey 00:55:06 I'm under like. Why, then, this counter would not have been solved with timestamp, because
a lot of time it would make sense like, even if you, counting, for example, requests
it, will also make sense to assign them Timestamps, right? Because then you might want to know what was number of guests of in different time frames right? So being able sort of seeing them as one big pile.
so then they will also not also override each other.
But
I guess I will need to dig deeper to understand how this whole Api. And if we have alternatives it will achieve the same purposes.
That counter was supposed to chew.
Okay.
Brett McBride 00:55:51 Okay? So I actually one more thing, and it's a really quick one, which is semantic conventions. So the Pr to sort of re-architect semantic conventions to align with how the spec now suggests that it be organized which is catching up with Java and some other seeks that's been merged. So I'll probably
or release that soon. Nothing should break but our contract might go red because we deprecated, or I've deprecated the old the old way, so it'll still work but just expect complaints.
Sergey 00:56:36 Is that the end of that work that you did with the split of regular namespace and the experimental? Or
how was it so.
Brett McBride 00:56:45 Yeah, they what do they call it?
Sergey 00:56:48 What was the.
Brett McBride 00:56:50 Incubating, incubating.
Sergey 00:56:52 Incubate. Yeah.
Brett McBride 00:56:53 Yes, that's that bit of work.
Yes.
Sergey 00:56:57 So that essentially will kind of like
cause people that use something from incubating. If the if it's broken, or it will be easier for them to see that they're using something that is not stable. Right? That's the purpose of division.
Brett McBride 00:57:13 Yes.
Sergey 00:57:15 And the other way around like if they already use. Well, I guess not. So. What will happen if you promote something from incubating to stable. It will also stay in incubating, so it will not break needlessly.
Brett McBride 00:57:27 That's correct.
Sergey 00:57:27 So incubatoria will always grow, it will never be reduced. It will.
Oh you!
Something is decided to be removed and not promoted, then it will be removed from incubation.
Brett McBride 00:57:37 Yes, it is removed from incubating yes.
which is which is the supposed to be the danger of using incubating. You were warned.
Sergey 00:57:46 Right, right.
Brett McBride 00:57:47 Yep.
Sergey 00:57:47 But, on the other hand, like this, in so just because you see, so, this indication only works in one direction. So just because, you see, incubation doesn't mean that that feature is not stable. You need to look at it. Maybe it's already stable. Then you need to change from incubating to stable namespace.
Yes.
I guess we'll need to see how it will work. So are you visioning that we will somehow like review instrumentations. And in time. How do you envision this work flow? Do you think like when when we see in semantic.
when, for example, change between semantic convention, we see that some attributes were promoted to stable.
Do we want to go and proactively go and change it all the instrumentations in country to use stable? So it's clear. So we don't want any stale kind of reference to incubate in, in at least in contribut instrumentation.
Brett McBride 00:58:41 So, yeah, yeah, I think we should preferentially be using stable and.
Sergey 00:58:48 But will we go proactively and update all the instrumentations.
even though they will not break right? We'll still references to to incubation will still be there.
they still will be maintained, if I understand correctly, even when
is it mostly attributes, or is there other parts that are.
Brett McBride 00:59:04 Automatically.
Sergey 00:59:05 It's all about attributes.
Brett McBride 00:59:06 I think it's all about the attributes.
And and I mean there's metric names in there as well. But yes.
Yeah, I feel like we should be proactive, and I would love it if someone submitted.
It doesn't make sense.
Sergey 00:59:19 Student to maybe implement some kind of automatic tool that will do it.
That will go and understand the difference between 2 semantic conventions and then go and scan some
part of the repo all the repo, and suggest what like automatically create a Pr or whatever.
Brett McBride 00:59:36 Hmm.
Sergey 00:59:38 Like it's a it's automatic work right now. No human.
Brett McBride 00:59:41 Oh, it's absolutely just run work. Yes, I if there's a tool
a a did you have a tool in mind?
Sergey 00:59:52 We had something it should not be that of an issue like I don't know what is the performance like, but just parsing the code. Everything is there like parses, the parses, right? And
I don't think there will be such, you know, big effort to implement this kind of tool. But
yeah, so no, the radio tool. I'm not that familiar, maybe worth investigating. I know that, for example, certain
certain runtimes like, for example, rust, I think, or maybe I I remember Kotlin. They were really kind of like for providing as much migrations, automatic migrations as possible.
So I I will have to look at it now. There is a rotor for Php, right? There are some tools that are supposed to.
Brett McBride 01:00:32 Yeah, kind of like migration.
For example, we'll we'll change your code. Yeah. And I was just thinking about that. But it's probably more work to write the Rector Plugin than it is to just.
Sergey 01:00:46 Yeah, yeah, definitely, I agree with you that this probably will be easier at the beginning to implement that hawk solution like quickly with the parser and just.
But yeah, maybe if somebody will come along to this group that is more familiar with director, they can later upgrade it to be right like, if it's more fancier. But yeah, I mean, yeah, definitely so when do you plan to do that? I guess it would make sense. I I would I would like to contribute such a tool. I wonder like if it's worth waiting for the 1st time we need it. So we can, you know, implement it for a particular case. When it becomes
when the real games come along right, we will have this situation where we promote some things from
by the way, it's interesting question, like, well, let's say, let's leave it alone, like
it would also make sense, then.
that this tool will also be somehow used in all the cases when schematic conventions are changed right to give us indication like it will scan everything that is upstream like a contribut. I guess SDK, automatically will be updated to to fit the semantic measures. But
all the other parts that are not always in sync, then it will also need to at least flag when something gets broken. Because of this, many crash, right? At least people will will know. Maybe it will open kind of like issues.
Let's say, put that aside, at least what can be solved automatically also, not just open issues. That is promotion from incubating to stable.
So
yeah, let's wait for the. So when do you plan to to check it in the this change.
Brett McBride 01:02:23 So so it's in Maine now.
I can probably do it in the next 24 h. There's there's no reason not to do it, except that
it's can you say.
Sergey 01:02:34 Do you mean to to have a release.
Brett McBride 01:02:37 Yeah.
Sergey 01:02:38 Oh, okay.
but we still need to for the, for the tool to be useful. We need to wait for the 1st time when we encounter this
change, like the promotion of incubation to stable right
Brett McBride 01:02:51 Yes, yeah. But I mean the the 1st step would just be.
Sergey 01:02:56 You know.
Brett McBride 01:02:57 3 names in your behalf.
Sergey 01:02:59 Change.
Brett McBride 01:02:59 Mentions.
Sergey 01:03:00 Do you need to change instrumentations to fit that new semantic conventions.
Brett McBride 01:03:05 Yep.
Sergey 01:03:06 Okay, so we can implement a tool that will deal with that and the
what will go. So so if you, if you, if you are planning to do it manually. So then you will have 2 versions of inside instrumentation, you saying which, so, you will essentially create a new version of notations that will declare that now, from that version on, it will require this new version of semantic connection.
Brett McBride 01:03:31 Yeah. Yeah. And and the versions 1.36. So yes, we'll require from 1.36, and then
Sergey 01:03:40 By the way, what is the result of that? If people by mistake take dependency on this new version of limitations, but they forgot to update the SDK,
and they still still use older version of SDK, that dependency on all semantic conditions. That's something that will not be automatically discovered by composer right? Or is it? Do we take also in composer of the instrumentation? We also take dependency.
and
Brett McBride 01:04:01 That's a.
Sergey 01:04:02 On a. On particular version of Api, that.
Brett McBride 01:04:04 Should probably, if I haven't update the composer Jason, of the SDK. To also rely on 1, 36.
Sergey 01:04:14 I'm just trying to wrap my head around like, what is the use case for this declaration at Runtime when when we have this?
I remember there was this call where you acquire some object tracer, or there was something the way you provide. What is your semantic convention version? Right? That you reliable.
Brett McBride 01:04:31 From instrumentation. But that happens at runtime.
Sergey 01:04:34 Although this kind of like dependency mismatch should possibly can be detected at composed time, right? When you already can declare that particular instrumentation depends on particular version of semantic conventions.
Brett McBride 01:04:46 Yes.
Sergey 01:04:47 We also do that right? We also have this kind of like declaration component.
Brett McBride 01:04:51 We do? Yeah.
Sergey 01:04:53 So then, what is the use case for this runtime? Is the expectation.
Brett McBride 01:04:57 So that's that's a.
Sergey 01:04:58 On our top.
Brett McBride 01:04:59 So that's instrumentation scope, and that is supposed to be a signal for backends Apm tools to know
the that. This was the meaning of this semantic attribute, as of this version, because things can change.
Sergey 01:05:19 So you're saying it's more about semantic thing and less about syntactic. So syntax might be the same. So technically, we don't need to release even the new version. But well, I guess it will be released. So.
because you're saying the the name of the attribute is the same, but the meaning of it is different.
Brett McBride 01:05:37 Well, the amazing!
Sergey 01:05:38 Professionals.
Brett McBride 01:05:39 Yeah, it may be it may be different.
Sergey 01:05:41 Does it mean that in this case the new semantic versions will be released, even though statically nothing changed. You have the same attributes because you change the meaning, there will be new versions released just for the change of meaning.
Brett McBride 01:05:56 Potentially yeah.
Sergey 01:05:57 Yeah, okay.
Brett McBride 01:05:58 Yeah, yeah, yeah.
Sergey 01:05:59 No, this is, I think, what semantic means, even though sometimes.
Brett McBride 01:06:01 Yes.
Sergey 01:06:02 Hear from people when they talk about.
Brett McBride 01:06:04 And so look back. Ends haven't back ends haven't completely worked. Worked this out yet, because there was a moratorium, and possibly there still is on changing some.
Sergey 01:06:15 You're saying, this whole thing is pure, theoretical. We don't have a clear examples like use cases where we know that in this case this is what people do. And in this case this is what the backends do, and whatever it's kind of like all theoretical.
Brett McBride 01:06:28 I think it's the well. Look, if someone does, then it's probably the the engineers of data, dog and elastic. And you know the people who are coming up with these conventions, and not and not me as as the implementer.
Sergey 01:06:44 To tell you the truth. Yeah, I guess. Yeah,
it's quite complicated. But yeah, but I understand what you mean. At least, this is the the. This is purpose, this indication at one time, I see. Got it. Okay. So so did you plan then? Okay, so you want to release this new semantic conventions. But
do you plan to do instrumentations later and separate? So do you think it's and tools.
Brett McBride 01:07:14 They can be done later, because they're not going to
blow up. They're just going to emit deprecation warnings.
yeah. So if you remember the change was, add the new. Don't change the old ones, but just mark them as deprecated. Mark those classes as as deprecated. So
Sergey 01:07:35 The the new you have. Incubation is a separate namespace, but stable is also namespace. Or is it just top namespace? And it's kind of like implicitly understood that it's stable.
Don't remember, I I wonder, like, when you say you deprecated the old ones. Do you mean the the attribute, particular attributes of the duplicated or the whole namespace
the whole class. I just deprecated the class.
Oh, okay, it's in class. It's not in the space. Yeah. Okay? So it's in class. So so you do have a separate, a new class, even for stable. So before it was all in one, okay, I see. So. But that change probably can be done quickly with just just a tool is kind of like a Php storm. Massage. Right can be just
done. Fold.
Brett McBride 01:08:21 Look, I could probably do a find and replace.
Sergey 01:08:25 Yeah, exactly. So.
Brett McBride 01:08:25 Thing.
Sergey 01:08:26 That's the.
Brett McBride 01:08:26 Include.
Sergey 01:08:28 I guess. At the end of the day this stable promotion
from incubation to stable also kind of like, find and replace, maybe semantically aware.
But okay, okay, I got it. Okay, So
let me know. If at some point you might think it might be a good good good thing to contribute this when we have this
like use case for.
So you think for this, just for this, for this particular change, we don't need it right, because it's 1 time thing
to switch in between just.
Brett McBride 01:09:01 Should be a 1 time. Yeah.
Sergey 01:09:02 Yeah.
Brett McBride 01:09:03 Yep, yeah. But.
Sergey 01:09:04 And then let's.
Brett McBride 01:09:05 As we say.
Sergey 01:09:06 Maybe they will also change it again upstream. So if they will, maybe until we get to the situation where something is promoted from incubated stable. They might decide that it's not a good idea to begin with, and we won't need to implement this tool.
It's like, I remember my 1st job.
Brett McBride 01:09:21 They're pretty careful. They're pretty.
Sergey 01:09:24 They? You think it's they will stay with this approach longer?
Yeah, my, on my 1st job, when I was just after the university my manager told me that every work they give you it's better to wait a couple of weeks, because manager might change their mind. And if you might wait. And yeah, so I.
Brett McBride 01:09:44 We would. Yes.
Sergey 01:09:45 Principle stays with you. But okay, okay, no, it's it's interesting idea. Yeah. Let's see. So you okay, with the then waiting the 1st use case we get to this promotion from incubate into, and then we can. We can see if this tool would make sense.
Brett McBride 01:10:03 It looks realistically, it's gonna be like they're they're well documented in the release notes.
Sergey 01:10:09 Yeah.
Brett McBride 01:10:10 You know we could probably probably should be.
you know, when we regenerate a new version of semantic conventions, the release note will say, these things have changed from.
you know, incubating to to stable create an issue, and then just go and search for those through through contribut.
Sergey 01:10:31 Yeah. Yeah. Yeah, the implementation should not be anything kind of like,
should be, okay? So yeah, I'm just saying, the plan. Do do you think the plan is good? Let's wait for when we have the 1st case of this of this kind of like promotion
already with this new system, and then let's see if we want to implement this tool, and so don't
we'll not commit to it this. Now let's see when we'll be there in that situation. And if we'll see that it would make sense, we'll see that this attribute is used by any of the instrumentations. Then let's see if we want to start with it, because we want to use case where we will actually be useful. Right? We don't want to go and implement something theoretically, where.
Brett McBride 01:11:13 Yeah, most of the work. So guys in in this initial, let's cut everything across to, you know, incubating and stable.
Sergey 01:11:22 Yeah.
Brett McBride 01:11:23 I feel like once that's done.
It's only a very small number of
of conventions that that might stabilize in any given release.
Sergey 01:11:34 Yeah, I understand what you're saying. So so do do you think so? Do. Are you planning to the work, or you will be glad to somebody to to help you with that.
Brett McBride 01:11:44 I would love it if someone else did it. I might take your.
Sergey 01:11:47 So, essentially.
Brett McBride 01:11:48 Just wait a week.
Sergey 01:11:48 Going to release the semantic conventions, and if somebody can pick up and do this adoption of all the instrumentations in country, but then
you. You don't need to do that, you can. You can delegate it to somebody else.
Brett McBride 01:12:00 Well, I might at least do the 1st one to to make sure it works, and see how it's.
you know, demonstrate how it how it can be done.
or what it should look like at the end, anyway. But yes, I would love for somebody else to to do the work that's.
Sergey 01:12:16 So yeah, I would love to help here. So if you how can you PIN me on the slack when it's released? When when you release this new semantic conventions, and then I will see if I can help I will see if it's better to do it manually, or like you said, find a replace, or or maybe is to implement some tool, though it sounds like it will be a 1 time use. But
let's see whatever will be simpler. But yeah, we'll be glad to to start, you know, picking up chores like that taking bigger part. Yeah. So please let me know when when it can be something that can be already used as a release. And I will. Yeah, I will see what I can do that.
Brett McBride 01:12:59 And and look well, it's just you and me. If we're done talking about that. The the donation proposal is, some things are happening anyway. Someone from the technical committee contacted me and said, You know, do you have any concerns you know? What do you think of the proposal.
you know, just just questions like that. And.
Sergey 01:13:21 I was not following that. Do you? Can you please update me? What what is the latest decision about like having this kind of like 2 alternatives that are currently not
Brett McBride 01:13:31 No decisions yet. It's it's just someone from the technical committee. I can't remember who is really just getting organized to get the right people together. So and just ask some initial questions from me about.
you know, am I supportive of of the code donation? Do I have any concerns just just high level questions like that. And and one
one thing that that occurred to me, and I'd like to tackle from a couple of angles is that I saw that one of the data dog engineers commented on the sort of the proposal
issue the code donation proposal. And it just
I just got me thinking, is this, is this a good point? Because this, your.
Sergey 01:14:21 Would you mind sharing what was the point? So I will be clear.
Brett McBride 01:14:24 Yeah, I can.
Sergey 01:14:26 Sure because I was not. apologize. But I was not following that that closely. It was kind of like
Pavel, kind of like took took it under his wind. But I should probably pay more attention to that.
Yeah, so I will. I will raise it, obviously with Pavel as well.
I think I saw notification.
Yeah.
So you're saying it was some kind of like technical it was some technical issue about the implementation itself.
I'm not sure I'm hearing you. I
I think you muted yourself so ready. You muted yourself.
You're on mute now.
Brett McBride 01:15:12 Yes, yes, I am sorry about that.
What was I saying?
no, no, no problems, no problems at all. It just seeing that Datadog had noticed
the code donation just made me think, is this the time when elastic and datadog work together to create one
open telemetry
extension that, you know, is the best of is the best of both of them. Because we we originally, like our very 1st commit
and set up, was done by by data, Doc. So they were. They were in open telemetry right at the start for a little while, and then and this is before my time. But that they're obviously not here now. They've dropped out for a couple of years.
Have we reached the critical mass, or are we about to reach the critical mass, where like the big Apm players yourself
and Datadog are the ones that come to mind who work in the Php extension space as well can sort of
come back into the open telemetry project and
Sergey 01:16:23 Is there any way to? Because we would be glad to to interact with those guys and come up with something that will be kind of like amalgamation of both of our efforts that.
Brett McBride 01:16:32 Okay.
Sergey 01:16:32 Great, like, so.
Brett McBride 01:16:33 Yes.
Sergey 01:16:34 If you, if you have some ideas, how we can facilitate that process.
Brett McBride 01:16:37 Yeah, and so I said, I wanted to.
Sergey 01:16:39 We okay to do it incrementally like, if we cannot, you know, we don't need to agree on everything like, I will be completely okay, I think it was probably as long as we can.
you know. I think our goal is, you know, like to be agile about it. Let's agree on. First, st like 5%.
Right? Let's let's just choose. If we cannot agree on all within as part of this contribution, let's choose what what is the 1st feature that we want to contribute, and it will be the base of all the future contributions on top of it. Right? And I think it will be easier to get this ball rolling so.
Brett McBride 01:17:11 And it's gonna be an open space for a while, isn't it?
Sergey 01:17:14 How we can like if the concern I I see it immediately. Right now I read it. I think the concern is that maybe datadog approaches to add additional functionality in separate extension on top of the existing existing SDK extension existing extension.
I I think we we can switch to that as well. That's why I I will discuss this particular technical point with Pavel.
But it might be worth like, if you can bring it together. Maybe if we can reach out, or we can also reach out. But I think it might be more valuable to come in from you guys. As so if if we can organize a meeting or ask them to come to the, you know, separate meeting.
I would be glad. Yeah, I think as long as we can, you know, find consensus between all the parties. Everybody will agree, and they will feel comfortable to also contribute in the future whatever they have.
We will be completely fine, you know, creating as vendor, neutral base, so everybody can contribute on top as possible. Right? So we, we will be glad to discuss with them. Maybe they even have some solutions to particular issues that we have now like this support
for this new extension. Right? So maybe they are that already have solutions that so maybe we can, even, you know, find the solutions just by discussing. But I think the biggest purpose of that meeting would be, how can we, you know, create some kind of like base that we can all agree on.
have it started. And on top of it. We can then incrementally contribute. And you know, we we can have, you know, already, independent, like, get the ball rolling right? So so, yeah, I I definitely think, Pavel will also be on board with that approach. So now, if we can take on self, organize this meeting, and then we can run.
Brett McBride 01:19:06 Oh, I thought I.
Sergey 01:19:07 Yes.
Brett McBride 01:19:08 I thought I'd tackle it through the technical committee. So like there are.
Sergey 01:19:11 Whatever is whatever is the right procedure to do it. But.
Brett McBride 01:19:16 I think we will.
Sergey 01:19:17 To have a meeting right. It would be the best like trying to discuss it on the on. The Github will take much longer, I think.
Brett McBride 01:19:23 And so, yeah, and I don't know anyone at data dog, I don't know if they're interested. They may not be. But but data dog are very big contributors, because I had a look at the contributors.
Sergey 01:19:35 They are the ones that designed the observability Api. They designed it together with the HP engine guy. Right?
Right? No, definitely. We will be completely glad. I I think we can, even, you know, benefit from the expertise. They probably huge experts in this field. So
if we can, anyway, like, even if I'm not 100% sure. Remember, they had idea to contribute all the agents. It's kind of like initial contributions. I don't know what happened with other languages, but I think that was the idea to do it for Php. As well. But maybe maybe I misunderstood. Did you hear that at some point that the dog proposed even to contribute
everything, at least agent from agent level. It contributes a base for open telemetry for all the languages, and I don't know if it happened in any other languages such as Java. Maybe it did happen I was not following.
They close it, but I understand that was implemented from ground up right without the contribution.
Brett McBride 01:20:33 Yep.
Sergey 01:20:33 Which is direct
a contribution. Okay, yeah. So I mean, if at this point, like as long as they want to, some in some level participate.
Let's have a meeting with them. Let's understand, like what is like. If they would even participate level, like given suggestions. Maybe they I don't know what is their plan. Maybe at this point they don't feel comfortable contributing their code.
but we will be fine like even you know, we don't need commitment. But then, as long as we leave the door, if they will be comfortable, that we will structure this contribution a little bit differently, so they will feel that the door is still open for them also to contribute in the future. I think we'll be fine to, you know, restructuring our contributions, so the other vendors will also be comfortable with that, you know, not feeling that. Okay, it's too much elastic like, and it's harder for us to contribute.
We don't, you know, for us the the goal at the end.
We don't want to implement. We want to implement as least as possible on the elastic level. We want to implement as much as possible directly upstream.
and so we save ourselves effort later to contribute in the upstream. Right?
We don't want to keep as little as possible that we need to keep it elastic level. It's easier for us that we don't need to think about how we merge it, how we maintain it at the same time. Right? So it's it's 1 hand completely selfish goal. But it's also completely company. Aligned company wants everything to be done as much as possible upstream. So you know, killing just to birds with one stone. It's also less work for us then, and
so definitely, not an issue. So if if I understand your your concern here like, will we be flexible enough to change our contribution so that we, you know other vendors, feel comfortable 100%. Yes, right? So let's discuss it. How we can do it.
Did I understand your unique kind of like, yeah, so yeah.
Brett McBride 01:22:23 That was done.
Sergey 01:22:24 We're on the same page regarding that we definitely want to to leave door open for other vendors, even though they maybe don't have direct plans that they, you know they they are going to contribute right now in your future. But we are fine. Let's let's you know we can. Let's attribute. Let's change the structure.
at least to contribute initial part right? And then whatever is necessary to change like, if they will feel that okay, other parts will also require additional changes. That's fine. We can do it incrementally, like I'm I think, trying to do it in one go. It doesn't need to be right. Let's let's create some base. And we, we can then contribute on top of that.
Brett McBride 01:23:05 Yeah. And and look, I think we should assume there's gonna be a an incubation period where
you know it's it's there and it's not released, or it's released as an alpha version or where we expect it to change and break and evolve.
Sergey 01:23:22 Yeah, I definitely will be incubation, because we still want to understand how we even position it, even though I assume we probably want to come up with that story. We probably should invest some time when the the contribution is done. At least. Okay, see how we position it from. I wouldn't say marketing, because it's open source. But like use case point of view for the users. Right? We need to make.
It's clear for them why they need to. If it's additional extension, why do they need to install that? What to do like, what is the what is the kind of like use cases? And what? Why would they need to do that additional step.
Brett McBride 01:23:55 Yep.
Sergey 01:23:56 To achieve what? Right? So yeah, so we definitely want to. And I assume we'll probably in time, we will better understand. Okay, so now we better understand all these use cases. Maybe we'll even change. How is we approach this? You know, additional extension, or whatever we would want to do to package those things right?
So I completely agree with you. We don't want to lock ourselves in into anything. Let's that's why we want to, you know. Get, get. We want to get to the situation where we start, and getting feedback from the field as soon as possible, because without feedback we will. Might fantasize a lot now and try to implement all kinds of solutions that might prove themselves not relevant. And we'll just be wasting our time right? So that's why it's better to get to the situation where we get feedback. And if it's a marked as incubation, no problem with that as long as people use it. We want people
amazing.
Brett McBride 01:24:43 Yes.
Sergey 01:24:45 So so let's see, what are the action items. So are you okay with taking on yourself to try to organize.
Brett McBride 01:24:51 Oh, yes.
with me. So I'm so I'm hoping that the technical committee has, you know, someone fairly important at Data dog. And they can just
going down and talk to their engineering department or their.
Sergey 01:25:06 If you need some like. I know that the elastic also has some people in some key positions there. I don't know if it's technical committee or whatever. But if you feel that things not move along, please let us know. Maybe we can
from other direction. Let's see if we can bring it together. But yeah, so please let us know as well. I know that there are some key people in collector, or I don't know if.
But yeah, so definitely would, because the goal again is to contribute some base that to all the vendors that are interested at least to at least, you know, reviewing it and comment on it will feel comfortable with whatever we are doing. And yeah, we'll be okay with doing additional work to to get there.
Brett McBride 01:25:46 Yeah, yeah, that's great. That's what we want is is the solid base that, and and not just not just Apm vendors. But you know myself. You know, the community can can contribute to as well, because it is a, you know, is a big, public, open source project that we want.
We want people to.
Sergey 01:26:04 Yeah, I agree with you, like, if we can create, maybe some base. So if you also have feedback like, for example, if you want to contribute some feature, and you want to implement it in rust.
How we, you know, tie it all together. I agree with you. So maybe at some point we would want to, I know, but we currently use C plus plus. But I don't know if you're aware of what's going on in that community like. There was a huge blow, and when the White House released this white paper.
Brett McBride 01:26:30 I did see that. Yeah.
Sergey 01:26:31 Yeah. So there is a security. They kind of like proclaim that I don't know if it will. I mean, at least in in simple plus community. It did cause a serious upheaval, and people started to think, I don't know if it will be kind of like situation when C plus will start to decline, and people will switch completely, you know. Give much better boost to rust.
and Rusty will take over. Maybe there will be some, you know some interesting steps done in C plus plus and c plus plus will, you know, get a second breath to it, and it will be able to continue, because technically, they have some solutions that they can do, maybe to, you know, to create some kind of subset of C plus, plus. That is more safe, easy to use.
and you know great tools that will allow people to stay with that subset. So it would be interesting to see what they can do, I see, probably will not go away, considering that I don't even see see people being too, you know, being too worried about it. They just you will not be able to do anything without us anyway. So you know.
Brett McBride 01:27:27 Yeah, yeah, that's right.
See people taking it seriously. C, plus, plus, I think c plus plus takes it much more seriously because they see competitors like rust.
Sergey 01:27:36 So I guess I guess rust also gets into Linux kernel, but I don't think. Still, it's to degree that they consider that they can, you know, overtake the amount of C code? I think C. Is probably less worried about.
Brett McBride 01:27:47 It's it's generations worth of.
Yeah.
Sergey 01:27:51 So they probably get more gun in which makes sense for them. They got in for higher level kind of like things which is good at. So yeah, that for them, it's better niche to try to take over. Yeah. So I agree with you. Let's that's my, you know, starting with the base, not committing to anything.
and then later, like, if somebody like you come in, or maybe I would want to implement some trust, then we can reevaluate and say, Okay, let's create some kind of layer here where we can add stuff with rust, and it all together will work somehow right? And people outside. They don't need to know too much about it. It's all about development, but then they
they will just install stuff and get this additional features. And again, we'll need to discuss how it's all integrated together. But yeah, I completely agree with you. Let's not. We don't need to, you know, commit the it's done now.
Brett McBride 01:28:38 I'm not necessarily angling at the moment, for for you know, rust inclusion, I just mean.
Sergey 01:28:43 What I'm saying. Let's.
Brett McBride 01:28:44 Just like, if I can write CI can write.
Sergey 01:28:46 Oh, yeah.
Brett McBride 01:28:47 Also, I assume. Yes.
Sergey 01:28:51 Yeah, yeah, let's let's do that. I mean, it's it's again. We. Also, you know, obviously, some code will be, maybe, even if we contribute it, we can always change it later, right? As long as it's you know, working, and we'll test it we can live with it as long as we get to it. When we want to add some feature, we need to refactor and change some stuff. You know.
Brett McBride 01:29:13 Yeah.
Sergey 01:29:13 It should be possible as well. Right? So. But yeah, so if, for example, that wants to restructure this in differently like, have this as additional extension, and the basic functionality will be inside the the regular extension. And this will be, we can go for that structure. If this is the the main issue. That they will flag in that meeting, and this is will be the main blocking point that we can address and and create this base that we can start from that. Yeah.
Brett McBride 01:29:43 Yeah. And and look, that's that's just the message that I'd want to get across to them like, this is a good time for you to get in, and, you know, help this to incubate in a way that's useful for for you. If this, if this is something that you data dog are interested in doing.
Sergey 01:29:59 Yeah, whatever like, even if I don't even want them to feel that they must commit now, or must contribute now to be kind of like a place at the table. No, it's fine like if they want to stay in this position where they comment. Review. We we have find that as long as they, just leaving for door for them open, contribute later.
even if they don't have a particular, you know, timeframe with which they are planning even to do that, but even just using their expertise just chiming it like that, I think it still might be worth an effort to just leave the door open for them to eventually feel that they are not blocked out, and they can come in and.
Brett McBride 01:30:33 Yeah. Well, and that that was the.
Sergey 01:30:35 I'm fine with it.
Brett McBride 01:30:36 That was the other part of what I what I what I asked the the Tc. Guy was would they be interested in doing the code review, because that needs to happen as part of the
sort of part of the donation process. And I'm not qualified
to do that. I mean I'll do my best, but
but you know I'm not a.
Sergey 01:30:58 Yeah.
Brett McBride 01:30:59 I'm not a Php. Call.
Sergey 01:31:00 No, no.
Brett McBride 01:31:00 Maybe not.
Sergey 01:31:01 Understand? Yeah, I understand, yeah, especially a lot of like technical things involved there that require.
Brett McBride 01:31:04 This is.
Sergey 01:31:05 Is in the area of interaction between Bnp engine, a lot of like clocks there that are dependent on yeah. All kinds of things that usually people season people that when they work a lot with this Php engine thing they already kind of like,
yeah, they already encountered for a few weird things. And they they just walk around them. So yeah, it's not always obvious why something is done on implementation. Yeah, they can also see something that is not done that they know needs to be done so for us to discover it later, you know, by debugging crashes.
Yeah. So that's why I'm saying I'm fully 100. I think we're on the same page. We want. The other vendors feel comfortable and feel that they are at any stage they can contribute in any way that they feel.
you know, comfortable. This stage of contributing reviews. Yeah.
Brett McBride 01:31:54 Yep, that's fantastic!
Sergey 01:31:55 Let us know how we can participate in that. And if if we have a meeting and like, I said, we are completely open. If the decision of that meeting is that we need to restructure a little bit or, you know, doesn't need to be a little bit if we all agree that fit better with the model that is great to everybody, then we will do that. It will be okay.
Brett McBride 01:32:17 Fantastic. That's great news.
Sergey 01:32:19 What is time for you now? Is it like.
Brett McBride 01:32:21 Yeah, it's getting. Oh, yeah, it's a nearly midnight. So and so.
yeah, probably time I called it.
Sergey 01:32:27 Sorry about that. You are you in in Western Australia? Are you in Perth?
Brett McBride 01:32:32 No in Eastern Australia, in near Melbourne.
Sergey 01:32:35 Okay, so, even worth, okay.
Brett McBride 01:32:37 Yes.
Sergey 01:32:37 Yeah, we have a few members now, team and Australia, like a wider team like, but I think, yeah, he's from birth. You're familiar with him. No.
Brett McBride 01:32:49 No, not Andrew Wilson, but there are a couple.
Sergey 01:32:51 Yeah, I guess big enough not to be familiar with everybody from Australia, but he's in the area of Pm. As well. He worked on the but I guess you go like if you use the last go agent he was. He was responsible for that. But if nothing to go, then probably. Yeah.
But anyways sorry for for taking.
Brett McBride 01:33:13 No, that's okay.
Sergey 01:33:13 Do you have a lot of meetings like that? Do you need to meet with people with the Us. And Europe a lot or.
Brett McBride 01:33:18 No, no, I'm really only in open telemetry.
Sergey 01:33:23 Okay, got it?
Brett McBride 01:33:23 Otherwise. I know I avoid meetings.
Sergey 01:33:26 A lot of sacrifice on your side on your part open telemetry 1 1 day a week.
Brett McBride 01:33:33 Thousands of hours that I've spent and unpaid. Yes, yeah, it's a big well, it's a passion project.
Sergey 01:33:42 So, yeah, thank you for that. Yeah, yeah, definitely, you're pushing it so definitely. No, it's all open source build on enthusiasm. Yeah, I guess without it. Would that be so? Yeah, that's why I would be glad to help out any way we can. And take bigger role. So please let us know how we can, you know, meeting or whatever else. If you feel that if you feel that it's at this stage, we can do something that is
will help push it along. Let's discuss it. And.
like, I think we are completely on the same page, like our goal is to create something that will be. We can get into the hands of people as soon as possible. And this is our goal. Let's let's see what get. Let's start getting feedback right? If it's better to start getting feedback on 10% on 20% of what we have don't need to push everything in one go so fine as well. Let let's let's see what we can do here.
Brett McBride 01:34:37 Exactly.
Sergey 01:34:38 Have a good night. See you.
Brett McBride 01:34:39 Alright, thanks very much.
Sergey 01:34:41 Bye, bye.
Brett McBride 01:34:42 Goodbye!
Sergey 01:34:44 Bye.
