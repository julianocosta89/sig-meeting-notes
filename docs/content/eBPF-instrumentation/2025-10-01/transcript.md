SIG: eBPF instrumentation
Date: 2025-10-01
Duration: 51 minutes
Zoom Recording URL: https://zoom.us/rec/share/wALy_ilt56cS6ErV2kPHKl2QRG6i3Twh_9aeAq8_g-FECstMkvqg2lynTJ6rZVo.-crgGzUnJW9OAo81
============================================================

## Zoom Recording Transcript

**Tyler Yahn** 00:25 Hey, Mattia.
**Mattia Meleleo** 00:26 Hello, Tyler.
**Tyler Yahn** 00:28 How's it going?
**Mattia Meleleo** 00:30 Pretty good.
**Tyler Yahn** 00:32 Yeah, doing good myself. Hey, Steven.
**Stephen Lang** 00:36 Hi, how you doing?
**Tyler Yahn** 00:38 Doing well, how are you?
**Stephen Lang** 00:39 Good points.
**Tyler Yahn** 00:43 Steven, where are you based out of?
**Stephen Lang** 00:45 The UK?
**Tyler Yahn** 00:46 Oh, okay. Near London, or…
**Stephen Lang** 00:49 No, closer to Edinburgh, Scotland.
Oh, cool. Yeah, no, we're in the northwest of England.
**Tyler Yahn** 00:55 Yeah. So just, just below the border of Scotland.
Nice, yeah.
Yeah, last time I was there for KoopCon, I really wanted to go up there, but the train was gonna take the whole day, essentially, so it was like, yeah, no.
**Stephen Lang** 01:08 That's excellent.
**Tyler Yahn** 01:10 Looks like a really cool part of the country, so, yeah, kind of jealous.
**Stephen Lang** 01:16 It's nice, it's green, nice hills, we're on the coast, so…
**Tyler Yahn** 01:19 Yeah, yeah.
**Stephen Lang** 01:20 Nice.
**Tyler Yahn** 01:20 Pretty dramatic.
I feel like it's, so I live in Portland, Oregon, so it's kind of the same on the coast, it's just more dramatic.
Yeah. So, yeah.
**Stephen Lang** 01:31 A lot bigger up then.
**Tyler Yahn** 01:32 Yeah, yeah, exactly, yeah.
A little bit more history, too.
**Stephen Lang** 01:42 very easier to get between places in England than it is in the Pacific Northwest.
Yeah, especially if you don't have a car, that would be… that'd be very much a challenge out here.
**Tyler Yahn** 01:51 But, yeah, even there, like, having a car, like, you're on, like, Forest Service Road sometimes, and, like, yeah, it's a whole… It's very vast, yeah.
Well, cool. I'm seeing a lot of people join. We could probably get started in here in just a second. If you haven't yet, please, go ahead and add your name to the attendees list, and if you have agenda items you want to talk about, please go ahead and add them there as well, and then we can jump in here in just a second.
Cool. Alright. So, yeah, let's, let's jump in here. So, first off, I saw this last, or this first item from last week's, that we didn't get to talk about, but Nicola, you were proposing, I think you'd like to propose, that we add Mattia and Steven as approvers to the project?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 03:18 Yeah, I… I don't know, like, what's the typical… I'm new to this process as much as everyone from Grafana is on the OpenTelemetry, but I don't know how much engagement typically is required for adding new approvers. I believe that, Matti and Steven have been kind of constantly participating, but I don't know if it's… time, or is it really break a little bit longer? I don't know.
**Tyler Yahn** 03:42 I think originally there was, like, a strict definition, but I… I don't know if that's still followed. It's funny to think that there's been years since that definition was defined. But yeah, like, I think it's more up to each individual SIG, more than it is actual a strict definition, but… I, I agree, I think if they meet that definition, it's in the community, I think it's a month of sustained's, involvement with something like 5 or 6 PRs or something? I can't remember exactly what it is, but, But anyways, yeah, I was… I wanted to bring it up again as well, because I think these are good, additions, to the approver set, so yeah, I would be in favor of this. So, yeah, obviously, Steven and Mattia, you'd have to be, I don't know, open to accepting their responsibilities, which is, just continued involvement in the project, so, yeah.
**Mattia Meleleo** 04:35 Yeah, sure.
Thank you very much.
**Tyler Yahn** 04:37 Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 04:39 I mean, maybe even Nimrod, I don't know. Maybe it's close.
**Tyler Yahn** 04:44 Yeah, I… I think that's a… that's a good discussion as well. I think adding Nimrod seems like a valid idea. Again, it just has to… you have to have interest, I guess. Yeah. I've definitely seen a few people not have interest in these sort of things, so we would want to make sure, but yeah.
I don't see Nimron on the call.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 05:03 But yeah.
He's not here, but, yeah, maybe we can reach out to him separately, if he's willing.
I know that Steven… Steven prompted me for this because he… he actually requested approver status, so we have one requested.
So I know Steven was up for it, but I… I didn't want to approve, I wanted to bring it up here for discussion.
Sorry, Matti, I interrupted.
**Mattia Meleleo** 05:29 Yeah, I was about to say that today is a national holiday for Nimrod, but I'll pass forward and see what he thinks.
**Tyler Yahn** 05:39 Yeah, that'd be great, yeah, if you could do that.
**Mattia Meleleo** 05:42 Well, cool.
**Tyler Yahn** 05:43 I can, I can take the action item. It used to just be as simple as adding some… permissions, but I think now we're using Terraform here. I'll figure this out.
Yeah, okay. I… if not, it's just about, updating some docs, I think, as well, so… I do think if we don't already, we should document this. I think it is documented, if I'm not mistaken.
Usually, you keep… this is kind of, like, the official way to do it, is to make it, a third-party thing. Maybe it's in contributing?
Yeah, so it's just down here. We would add up PR, and we'll add, both as approvers, and then… Yeah, then the other thing is the Terraform, or… Yeah, it might be. It's a group management thing, so I might be able to do it manually still, but maybe not. I'll have to figure that one out.
Okay, cool. So, moving on, in the agenda is, Mario, you wanted to talk about providing more context to source code, via comments.
**MM Mario Macias** 06:58 Yeah, basically today I've been chasing a bug.
And I've been sweating blood for understanding what's going on with the… even with… if we have the backlogs that more or less show you where the program is going. Sometimes it's… it's… it's very difficult to get the whole context.
So I'd ask that, anyone that touches the code and shows something that might be interesting for anyone else coming after, just to add some comments. I pasted this… this example of pull requests of some… some stuff that I would like to have known, while I was, investigating. So, yes, yeah, it's just a few comments. It's not just saying or describing what's in the code. I mean, if you describe this.
map, not saying this map stores this, but maybe this map is updated in some points, it's retrieving in some points. There are some assumptions, So, yeah, it's just… Call for… or a reminder that is fine.
comments from time to time, I mean, even into existing code, if you think something is is useful.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 08:28 Yeah, good call out. Yeah.
just call out that the UVPF code definitely can be better documented.
**Tyler Yahn** 08:38 Yeah, 100%. Adding docs is important, especially in this, where you think, you're gonna write it once, but it actually is read probably more than you are writing it. So yeah, it's a good idea to have these sort of things, so… Looks good. You're… I think we just need review on this one, so if you haven't yet, please take a look.
**MM Mario Macias** 08:56 Oh, yes, yes, because especially I wrote those comments, but maybe they are wrong, or maybe I'm doing some wrong assumptions.
So… even those comments might be wrong, so it's… I think it's better not having comments than having wrong comments, so if you can double check… Could be nice.
**Tyler Yahn** 09:19 Yeah, that sounds good.
Perfect.
Okay.
Moving on then, next up, Steven, you want to talk about an update for the CI performance, for both the Cates and the, the VM?
**Stephen Lang** 09:35 Yeah, so I've been spending a fair bit of time trying to reduce the CI execution times.
So if you look at the K8s one first, this is now merged.
So we're looking at about 10 minutes for the Kubernetes integration tests, down from 45.
The way this works is there's one shard per kind cluster.
And there's a one-to-one mapping with cloud clusters and, KX integration test packages.
So this is… this is a different approach to the way that we just sharded all tests across multiple runners.
For the non-KX integration tests.
But the reason that I had to do it this way was because if we tried to run multiple kind clusters on the same GitHub runner.
And they're all using the same host ports. We were just getting… A load of, kind of port conflicts, and a I was having to make quite a lot of changes to the test logic and the config, and I just felt it'd be simpler just to shard it by.
package, and effectively kind clustering. So this, this seems to be working really well.
I was hoping to have, like, a shared workflow between the normal integration tests and the KX integration tests, but because they're using a different sharding strategy, that's not going to be the case anymore.
So this is in May.
The other thing was, the VM integration tests.
So this is still in progress. I did some, like, benchmarking to find where the bottlenecks are.
I think I found where it is. It seems to be… that we do the GoTest compilation within the QEMU VM.
And that is what takes the majority of the time.
So what I'm experimenting with at the moment is, doing a pre… pre-compile or cross-compilation first on the GitHub runner itself.
Before we enter the QEM UVM.
And what that means is the cross-compilation takes just a minute or two.
And then we're immediately booting up the QMU VM and running straight to the tests.
I've also cleaned up the workflows. We had two separate workflows before.
And each of them, with matrix strategies, now we just have a single VM workflow.
With a more complex matrix strategy for both kernels.
Also, each one is sharded.
I haven't really decided how I'm gonna do this finally yet.
I've got some issues with executing the pre-compiled tests.
It's running, but the tests are failing.
So I'm going to continue on with this.
But I'm thinking… this is going to be a lot faster, because I'm already hitting the integration tests, you know, they're failing within, sort of, 5 minutes.
As opposed to, you know, previously this thing was taking 90 minutes to… to complete.
So I'm hopeful that this should be sorted soon.
**Tyler Yahn** 12:37 Yeah, this looks great.
**Stephen Lang** 12:39 Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 12:39 It's gonna be a big help.
**Stephen Lang** 12:41 There was one last thing, the… I don't know if you noticed, the normal integration tests have been getting slower.
Since the sharding.
And what happened was, because they were deterministically ordered in the shards.
the test names, I mean, that we just sorted alphabetically.
All the test network tests were landing in Shard 2.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 13:03 And Shard 2 was taking, like, 25 minutes, and everything else was taking 10 minutes.
**Stephen Lang** 13:09 So, what I've done, just as part of the K8s integration, the other PR.
I just introduced random ordering.
For the test names, and this just means… We get a more even distribution.
environment.
Of the integration test, the integration tests in my testing are now completing within about 18 minutes.
So hopefully once all this work gets in.
The majority of CI should be done within 20 minutes. Fingers crossed.
**Tyler Yahn** 13:40 Yeah, that's great. That's a huge step forward, from where we're… where we're at today, so… Yeah, this looks… this looks great.
I like your approach, here as well. This seems like a smart move, Yeah, I think all of this sounds good. Any other comments on this one?
From other people?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 13:59 You know, it's gonna be great help, like, CI's been a major… Problem for everyone.
**Rafael Roquetto** 14:06 Yeah, this is awesome.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 14:08 I just want to say this is awesome.
**Rafael Roquetto** 14:11 Thanks for doing that.
**Mattia Meleleo** 14:12 Yeah, big thank you.
**Rafael Roquetto** 14:16 See, everyone's mind… everyone's minding, Steven. Everyone is happy with you.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 14:19 Everyone's having a great day now, yeah.
**Stephen Lang** 14:24 Yeah, no, thanks, Mattia, for the earlier point around using GoTestSum. I didn't use it for the test distribution, but I used the approach where nobody has to maintain, like, this manual list of shards.
So, none of the tests themselves have actually been touched. You can just write and contribute more tests as normal, and they'll all be automatically sharded based on Whether it's K8s, or integration, or VM tests.
That's kind of the general approach, I think.
**Mattia Meleleo** 14:52 Yep, sounds good.
**Tyler Yahn** 14:55 Yeah, that's great. Dynamically being able to do that is a good idea, so yeah.
Okay, cool. Moving on then, Nicola, you wanted to discuss tracking disconnects in DNS?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 15:12 Yeah, I… I kind of, like, Andre came last week, right, and he was talking, or maybe the week before, sorry, I'm losing track of time, but, he was talking about, the proposal to add DNS tracking, and then… I got thinking about, well, what if, yeah, we could do that, but then another thing that popped to my mind was that, if a request is going, to a service, let's say a service is calling another service, but the… the services… something's misconfigured, and it's not even gonna hit there, right? So, right now, that… we… for everything but Go, we do protocol instrumentation, right? So, we look at the protocol, but you can't connect, there's no protocol, so we're sort of oblivious to these things happening.
So, got me thinking about that, how can I actually, do something about this?
So I have made two prototypes, for both these disconnects, or failure to connect.
And, so that branch is pushed. Dns also made a prototype.
I was gonna show you how it looks, and I wanted to kind of get feedback if… We wanna do this.
Maybe also, Let's see… So, here's a captured a couple of requests with the work that I've been doing. So, I'm playing with this thing called, This is a demo application, book info, with a couple of services.
From Istio. This is what, I don't know, screen's too small.
Is it too small? People can read this?
**Rafael Roquetto** 17:03 Good to meet you.
**Stephen Lang** 17:03 That's fine.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 17:05 So here's one that… where… so you run this simple bookstore app, so I shut down the rating service. So… So I can't run it, technically.
And because of it, I wanted to see what happened. And typically, what would you get? Like, they've written the code in a way that this Java service is supposed to call this rating service.
But then it doesn't actually necessarily fail if ratings cannot be provided. It simply returns back an error to the end user saying rating service is not available.
But the actual request does not fail, so this reviews finishes.
So, with me adding this stuff in, it looks like this now. So, we can kind of see… that this product page here called Reviews, but reviews eventually failed to connect to a downstream server address, so we actually see A failure there.
Because right now, like, there's no, like, HTTP request, or whatever it is, or SQL, we can't even see the protocol, because the Simply Connect fails.
So then I was playing around with something else, then I kind of said, okay, well, the DNS is also along the same lines.
It's a separate protocol.
So, if we look at the DNS, It looks like something like this now.
So, I configured… a little Python program that's talking to Google on a wrong URL, so get users does not exist on google.com slash users.
But we can kind of see the name resolution happening, so… this… Kind of has the question, and… This might be an older one, actually, I believe I… May have actually added… The, Anyways, I can't find it.
So you kind of see what you're asking, like, I think I fixed it, but maybe this ordering is… Let's see… Yeah, no, no, let me… just one second.
I, modify… Last… Founding.
Why would I do it?
Anyways, it's supposed to have the resolved IP addresses for these, but this is one where it actually fails, so when it succeeds, it should have something like… The actual, span would also have the answers, right? Like this.
So, this is the IP address that we resolved for google.com.
and then it issues another kind of DNS record.
Which gets the IPv6 address.
And eventually fails on users, because that one is… With a 404 not found.
When it fails, and I have a much quicker failure, which is where the DNS actually Does not work, because of server failure.
So, there's a… something… here, like, a URL from our test that's… I haven't booted, so it just can't even resolve the name, so… The transaction fails, but you know why it fails now, so the DNS couldn't resolve it.
So those are kind of the two things that I've kind of wanted to show and, get some feedback of… Is this something we want to add? In what form, if we want to add? I think it's useful for debugging.
**MM Mario Macias** 21:14 That's amazing, that's amazing. I will even… I don't know how standard is that, but for the bagging, showing it by default, but maybe… Assuming that DNS will always succeed, ignore…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 21:33 successes.
**MM Mario Macias** 21:34 Yes, ignore the successes by default, or let's configure to show them, but show, show anyway the failures, because a DNS failure is something that… That the users shall see by default.
**Tyler Yahn** 21:54 That's a great idea.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 21:56 Yeah.
Yeah, we can do that. We can definitely do that. I think this… some people may find this useful, but I agree with you. The reason why I think people will find this useful is because If you're not caching the responses from the DNS, you're constantly asking for DNS?
**MM Mario Macias** 22:14 You're likely paying some penalty, like, over here, this…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 22:17 15 milliseconds or something.
**MM Mario Macias** 22:20 Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 22:20 you're waiting on the DNS to complete.
**MM Mario Macias** 22:25 I, I, I won't anyway allow them to… or configure to add a flag, yeah, to add a flag and… and show it… Just to maybe thinking of some users that could complain this being a bit noisy if we enable it by default, but…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 22:44 Yeah, it's gonna pollute their traces for sure.
Yeah, I agree. But I think this is kind of useful, knowing be able to resolve an.
**MM Mario Macias** 22:53 Definitely, definitely. I think… I think this… this is super useful, an amazing… an amazing feature. That will itself justify moving from… to OVI.
If it is… if it cannot be provided by other libraries.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 23:13 I think a normal SDK would actually probably show a failure here somehow.
I don't know, actually, that's a good question. We need to see if SDKs can catch this. This is not possible to find, I think, in regular terms.
The actual resolution time, It would have to be really fine-grained instrumentation onto the… the underlying Language.
**Tyler Yahn** 23:37 I think you'd have to use, like, a profiler there.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 23:39 Yeah, to be able to catch this, right? Yeah.
**Tyler Yahn** 23:43 Yeah, and I… so, I think it's actually kind of a question I had for you, is like, so I think Mario's idea of, like, not showing these by default is good, but I think the success is… I would definitely want a flag to turn these on for that exact reason of, like, whether you can… you know, do some debugging to find out how long that's taking. So yeah, I definitely like that idea of, like, default errors only, and then going somewhere there.
The other question I asked is, like, I, like, I see some of these requests failing, like this one, right? This fails, but the parent span isn't failing? Like, is there a reason why that is?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 24:14 my code is like that. I sort of, like, eat it up.
Okay. Yeah, the code's, like, doing that.
Yeah, it's actually not doing anything, I don't know why it's doing this now.
What is this byline supposed to… I have no idea.
But… so I'm actually just getting a response back, and I'm checking to status code 200, and if then I used to otherwise return pong, so… I'm not failing the request.
**Tyler Yahn** 24:55 Oh, oh, I see what you're saying. Okay, so yeah, it… oh, okay, okay, I got you.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 25:00 Right. So, you can see this succeeded, but if you drill down, you kind of, like…
**Tyler Yahn** 25:05 Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 25:05 you can see that this failed. It's not, like, bad programming practice, but this, this other application I was looking at, this book info.
It's doing the exact same thing when you think about it, like… it's…
**Tyler Yahn** 25:21 Yeah, it is, that's actually where, right, the Java one was the one that confused me the most, because I was like, why isn't the whole request to that failing? Yeah.
But that's… yeah, sorry, I thought it was us doing that. If it's the code doing that, then that's not really… yeah, that's…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 25:36 code is actually failing, but for you, doing a trace investigation, you have no idea this actually failed. The only way is your customers, like, your programmers designed this in a bad way, so your customers are seeing the error, but Operationally, you're not able to see the error, because of the way the application is written, so… adding the indication that disconnect failed here, I mean… It's kind of useful.
**Tyler Yahn** 26:05 I think that's, yeah, a really good, call-out. So, like, if you design poor instrumentation, you can still see failures, even though, like, they would be masked otherwise, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 26:13 Yeah, but I also wanted to show you something, like, so this product page, this is also running with a DNS instrumentation. So you can kind of see over here, these services are calling each other, so this Python is calling this Ruby, and so on.
But there's no DNS involvement here at all. It doesn't show up. And the reason why is that these applications actually have cached the IP addresses.
So, there is no noise unless this noise is happening, so…
**Tyler Yahn** 26:45 Yeah, I mean, that's actually a good point, cause, like.
Yeah, I don't know. I feel like if you have somebody who's not caching their DNS, which is… it'd be a little weird, you'd have to kind of go out of your way, but, like, it would… it would be a little noisy. I think those might also be the people that would complain about it being a little noisy.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 27:01 Okay, fair enough.
**Tyler Yahn** 27:02 Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 27:04 All right, yeah, I can make that happen, and we can add an option to have DNS success.
Shown up as well, and…
**Tyler Yahn** 27:13 Yeah, I think… And we can always turn it on at a later point, too, right? If we find a lot of users are really like, this is really helpful, can we just have it on by default? I think we can always change that, right?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 27:25 Yeah, yeah, fair enough, yeah.
So, yeah.
I think this would solve that issue, and I'm specifically, like, kind of excited about this, kind of knowing that these things there were a failure there, and we can kind of see it down in Trace. So, another question I had is that, do we want to produce metrics for these things, or just…
**Stephen Lang** 27:52 I was like.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 27:52 Superman Traces.
**Stephen Lang** 27:53 That was gonna be my question, if there's, like.
A histogram, maybe, of the, you know, the DNS lookup times.
Or, if there was… Another metric, just tracking number of, you know, DNS errors, like a counter or something.
It could be a good way to… Like a lightweight way just to, you know, alert on something happening.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 28:17 Yeah.
I think so, too. I think the DNS metrics will be useful, even if you know how many successes you've done, just to kind of see the sheer volume of DNS flying through. I also think this TCP disconnects, I don't know if there's a metric in the spec defined for something like this, but… I'd like to know how many client requests fail to even connect to a specific remote service.
**Tyler Yahn** 28:48 Yeah, I mean, that sounds good. I'd be careful on the attributes for the metric, just so that you don't have cardinality explosion. But yeah, I think that both of those sound like great metrics, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 29:01 Yeah, this one is low cardinality, it will be nothing, pretty much. We're just… probably want to exclude the server address, but I think by default now, we turn this into a low cardinality for any… any of our span service graphs, sorry, metrics.
So, we'll see the port, and… Potentially, we'll turn this into, .
**Tyler Yahn** 29:27 The server address, yeah, like, I'd be worried about it, but I might not, like, it might be… Because I don't know how many DNS servers you're going to be talking to, maybe over an entire cluster.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 29:38 but failed to connect. Yeah, so this DNS succeeded.
**Tyler Yahn** 29:42 Yeah. But the service is down.
Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 29:48 yet.
So this one… sorry, the DNS, is gonna be here.
So I'll definitely want to report this. Probably not… the… Where, but maybe just saying that it failed.
And what was the, initiator service? So, this Python 312, whatever.
**Tyler Yahn** 30:14 Yeah, that seems like a reasonable… Especially if you have, like, exemplars or something like that, like, you could always… then you can come take a look at this, so I think, like, having just a metric, yeah, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 30:25 Yeah, we don't have to specify the name or, or any of this. Maybe the type of record, so that we're doing both A and this I agree.
**Tyler Yahn** 30:35 Aquatics, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 30:37 right? Yeah.
**Tyler Yahn** 30:39 Yeah, I mean, I think that seems reasonable, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 30:43 And then the failure code, status error, and I think the error message, the kind of error. So, there's few. It could be, like, DNS temporary failure or something, and so on, so… Yeah, okay, cool.
Thank you.
**Tyler Yahn** 31:02 Yeah, awesome. It looks great. Pretty excited about that.
Cool.
Alright, so moving on, Rahal, you wanted to talk about internal metrics of BPF to usage and frequency?
**Rafael Roquetto** 31:20 Yeah, so… I was debugging something else, like, there was a problem.
with the, network observability Tracer. And then, when I was profiling it, I saw that, we're spending a lot of… everything's relative, right? A lot of time is very relative, so… Bear that in mind. But we're spending significant time in reporting internal metrics, and part of it has to do with when we're gathering data for the BPF probes. The way it works.
Is that we… sorry.
we… periodically iterate every eBPF program, to see how they're doing, like, in simple terms. And this iteration means that, you know, enumerating all these programs, and for each program, we create a sillian eBPF program object, and that's, like, it gets initialized by a file descriptor, and then runs a couple of system calls, and creates the object, and that allocates things, and maps, and… and at the moment, I think it's running… every… a couple seconds. So you can imagine if this is deployed to a large cluster, you know, with, hundreds, hundreds of programs running, you know.
generating question, this… You know, amount of seconds.
adds up. So, I pushed a PR yesterday that just increased the polling time to be, like, every… I don't know if it was every hour or every half an hour. I wonder if that's okay? Like, how are these metrics used? You know, how important they are?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 33:19 Yeah, that might be a little bit too infrequent.
**Rafael Roquetto** 33:23 Okay.
**MM Mario Macias** 33:25 I, Rafael, for me it's fine, what you, what you said, but I was suggesting as an alternative, some kind of back-off. I mean, if you want to debug and restart.
Bela, maybe you want to… you don't want to wait 30 minutes, but maybe waiting 1 minute.
Then, starting to, to do some exponential back-off and start to parse the metric less frequently.
As another suggestion, but it's fine. We just disable it, and then if you need to debat, manually increase the… manually incre… yeah, manually increase the frequency, and that's also okay.
300, huh To be honest, I've never looked at those metrics.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 34:13 So how expensive this really is, right?
**Rafael Roquetto** 34:15 If you, look at the PRJ merger, I, I, I put, I put a, like, a flame graph there.
With both CPU and memory.
So it's relatively expensive, based on this running code.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 34:32 It's not Merge, right?
**Rafael Roquetto** 34:34 It is, it is merged, but all it does is set the default value, it's easy to undo it. I just, I just changed the default configuration value. Now this one.
**MM Mario Macias** 34:43 No, I think it's… there is a… you did it in another pull request.
**Rafael Roquetto** 34:48 this.
**MM Mario Macias** 34:49 Pull request is not yet merged.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 34:50 She's normal.
**Rafael Roquetto** 34:51 Oh, it's not… it's not merchant.
**MM Mario Macias** 34:52 I added a comment previously.
**Rafael Roquetto** 34:54 Perfect. Yeah, that one. Yeah, okay.
Sorry, just… I'll start. So, yeah, so you can see the flame graph here. The first one is the CPU.
And it's being covered, but this is the collect internal metrics. It's basically this BPF collector, that the time spent… it's most of the time spent in collecting these metrics on this… on this cluster. The rest, like, this is the entire cluster, and I'd say, like.
naked eye, 70% of the time is just collecting these metrics. CPU and memory is under as well. And you can see the orange ones, if you look at the memory, for instance, it does… these… CDWPF program info, and new program info from FD, and that's what really takes time. So, in doing that.
We can maybe limit it only for OB programs, maybe, instead of all of the, all of the, you know, actual BPF programs in the entire cluster. It's not… this is not a problem, per se. I just… I just thought it was a bit out of proportion, given, you know, it's likely interested in taking all of this. So I increased the defaults, but… I don't know how these metrics are used or consumed, you know, it's just… we can revert it if, I mean, it hasn't been merged, I can drop it, I don't know.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 36:21 Right, so it's really important to know which programs are actually running when we have… if we enable these, BPF metrics, because we use that to determine, like, if we… some of them are really slow.
But I, I mean, this new program info from FD, I suppose we can cache the result.
in an LRU cache of some kind, so we don't have to repeat it if it's the same file descriptor.
**Rafael Roquetto** 36:44 Oh, I'm not sure about that, but I can look, yeah.
Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 36:50 Yeah. Maybe. Maybe there's something like that. If that's the most expensive operation, maybe something along those lines that we can… Actually, But how frequently do these things run? Every 30 seconds?
**Mattia Meleleo** 37:04 15 seconds. Yeah, something like that.
But.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 37:07 It's 15 seconds. 15 seconds?
I'm surprised at that.
is this much overhead running every 15 seconds? Like, how much CPU can you possibly burn if… Every 15 seconds, that's, like, eternity in computer.
**Rafael Roquetto** 37:26 Exactly.
**MM Mario Macias** 37:27 Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 37:28 To be this much.
I don't know.
Something doesn't add up here, in my opinion.
We would… we would… this would need to be, like, if this… profile here is doing all this, HTTP and… Kubernetes… Unless it was a profile from an application that barely does anything, or there's nothing on this cluster.
I mean, it sounds pretty… Wild here, that this is such a big proportion running every 15 seconds, something… I think we need to do more investigation here.
**Rafael Roquetto** 38:15 Okay, I mean, just something to bear in mind. I can drop the PR for now.
Then, and we can take it from there.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 38:23 I mean, if it's minutes, then we're getting, like, really low-quality profiles, right? I mean, you have to technically run this for minutes to be able to tell, I don't know, what the… to be able to tell which eBPF programs are the most busy.
I mean, I only work in a really long-running.
**Tyler Yahn** 38:43 Yeah, I was gonna say the same thing. Like, the total here is 39 seconds, right? And, like, you're looking at 27 seconds for the total operation time, like… first off, that's horrible, but, like, to Nicola's point, like, if you ran this for 5 minutes, would you see the same proportion, I guess, is kind of what the other question is.
I definitely think, Rafael, like, I wouldn't just close this and forget about it. Like, I definitely… I would track this in an issue, or I would try to find some sort of other solution, because, like, to Nicholas' point, like, that's a lot of time spent doing these sort of things, so we probably want to address it. It's just how we want to address it, I think, is the question.
**Rafael Roquetto** 39:18 Right. Yeah, yeah, this is running on our dev, our Grafana dev, clusters, so I'm looking here on the past 12 hours.
I mean, maybe that is more to the story, as Nick was saying, so I'm just reporting the naked eye, macro view. It's still, like, for… for 4… 4 to 59 hours, it's still taking… Yeah, it's still taking, 62% over, like, 4 hours or something. And…
**Tyler Yahn** 39:51 This… Wow.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 39:52 Yeah. Okay.
**Rafael Roquetto** 39:54 I don't know. I don't know, I…
**Tyler Yahn** 39:56 Are we, like, Bitcoin mining there? Like, what's going on? That's crazy.
**MM Mario Macias** 39:59 But… but looking here, like, these, these…
**Rafael Roquetto** 40:03 part of 59 hours, only 50 minutes is actually the BPF collector.
And map iterator, I mean.
it's not the most expensive, but still showing up there. And the rest is the BPF probe latency… it's a Prometheus reporter, get match… that's nothing to do with this code that I'm… it's a… Failure, though.
**Tyler Yahn** 40:29 Are you able to share your screen, or is this kind of sensitive information?
**Rafael Roquetto** 40:32 No, I think it's okay, right? Or…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 40:34 I think Sarah's fine, yeah.
**Rafael Roquetto** 40:36 Hold on, I was looking at a different computer. Let me open this here, and I'll share my screen.
**Tyler Yahn** 40:41 Yes. Just give me a moment.
**Rafael Roquetto** 40:51 Alright.
Sick.
Okay, how do I do this?
Share… Alright.
Alright, are you guys able to see this? I mean, it's a bit small because I'm on the laptop. Let me try to…
**Tyler Yahn** 41:21 Looks good.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 41:22 Okay? Yeah.
**Rafael Roquetto** 41:23 Okay, so this is CPU, how do I?
Jack, there's always food here.
Let's go for…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 41:38 So, last 30 minutes.
**Rafael Roquetto** 41:40 Yeah, that's 6 hours, for instance.
So, this is the beginning.
**Tyler Yahn** 41:45 Just to be clear, Rafael, this is not your change, this is, like, what's in Maine, right?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 41:48 Yeah.
**Rafael Roquetto** 41:48 That's what's emailing, yes.
**Tyler Yahn** 41:50 Okay, okay.
**Rafael Roquetto** 41:52 So… Yeah, you see there's collecting internal metrics here.
And then… This collects internal metrics. A big part of it is… most part of it is the Provictus Reporter VPF probe latency.
And then it goes into this… like, these histograms labels are always… whenever they show up, not only here, they always look, like, I noticed that, but that's beside the point.
And then, yes, looking here now, you guys are right. I mean, this is probably the most chunk, which is unrelated to my APR. MyPR would be this blue part here, which is the get metrics, which is, yeah, 10% of everything in this map iterator, etc, etc, etc. So… but this is… this… part here is still a big chunk. I mean, it's the majority of time being spent.
So…
**MM Mario Macias** 42:42 Actually, 10% of the time is… I think, is not negligible, so it's… it's worth improving.
**Rafael Roquetto** 42:51 Yep.
And memory…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 42:54 Very, very strange, like, if this one…
**Rafael Roquetto** 42:56 I…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 42:56 15 seconds. Yes.
**MM Mario Macias** 42:58 In the past, in the past, I've observed that when the VPF collector generates, or, generates so much memory, it's because we might have some… We might have some… some attribute that is growing, creating a lot of cardinality, so the chunks.
**Rafael Roquetto** 43:19 Hmm.
**MM Mario Macias** 43:20 that are reported by Prometheus are very high, so maybe we should manually… we could manually query the Prometheus endpoint of some of the… of… of some of the Bayless OBIs in that cluster, and see if it is generating a lot of data or not.
**Rafael Roquetto** 43:40 Hmm.
Okay, yep.
Yeah, so…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 43:44 Maybe. Yeah, I'm also thinking in these scenarios, like, this is maybe our dev cluster, and… maybe every OB is watching every other OB, so there's maybe many, many of these BPF programs loaded, so it's iterating through a large collection of…
**Rafael Roquetto** 44:01 Yeah, it's possible.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 44:02 nodes are in the cluster, so we should definitely optimize it. That's my take on it. Should not make it.
**MM Mario Macias** 44:09 God bless you.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 44:09 frequent.
But…
**Rafael Roquetto** 44:11 Okay.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 44:11 I'm still surprised that something that runs every 15 seconds could have this much impact. This might… Then it runs for seconds.
To perform this operation.
**Rafael Roquetto** 44:22 Yeah, if you look here, like, because it goes… it's linear, right? It goes program by program for each program, so it's an iterator.
And it does this lookup, and then if you look here at the bottom, it's a Cisco output, so whatever this is, like, it's trading the map. I noticed this map iteration is really expensive. This is one side of this, and the other one, if you look at this new program info from FD, is also very expensive on its own, and then there is this program from proc, you know, it passed the proc file system, scan FD, so open file… it's doing a lot of I.O. too, you know, that's the problem.
That's why it slows it down, I guess, so much, and I don't know what the hell this program, if they have to look at the source code does, that half of it is spent… more than half is spent on itself.
So, I mean, the bottom line is that it's… it shows up on the profile and caught my attention, but yeah, my PR was a bit naive, I guess. We'll have to… reassess this.
So, for now, I guess something to bear in mind, if it shows up for customers, just tell them to adjust the scrape time, BPF metric scrape time, if it becomes an issue. It's a workaround for the time being.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 45:37 I mean, this is similar to the functionality of that tool that Netflix developed, BPF Top, I believe.
We should take a look how they've done it. Maybe there's.
**Rafael Roquetto** 45:46 Yep.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 45:47 much more efficient way of doing it. Maybe it suffers from the same issues. To me, it seems unreasonable that it's every 15 seconds, and it takes that much Overall, percentage-wise?
It must be…
**Rafael Roquetto** 46:00 Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 46:00 Taking forever to complete.
**Rafael Roquetto** 46:03 Yeah.
Yeah.
Yeah, so that's, that's the situation.
Like, if no one does, look into it in the meantime. I'm going on PTO, by the way. I'll be back in this meeting in the last week of October.
So… I can look into it then, once I'm back.
**Tyler Yahn** 46:22 Raphael, is there any chance you can open an issue just to track this?
**Rafael Roquetto** 46:25 Yes, absolutely. I'll do that.
**Tyler Yahn** 46:28 Because, yeah, maybe then, while you're gone, somebody can take a look and just, like, we can have what your knowledge base already exists, we don't lose that, yeah. Or what you've just discovered here, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 46:37 brilliant.
**Tyler Yahn** 46:39 Yeah, that'd be great. I think, want to just track that, yeah.
**Rafael Roquetto** 46:43 Yep.
**Tyler Yahn** 46:45 Okay.
Cool. Jumping back in here… Awesome. Alright, so… looks like we've got 15 minutes left. Just wanted to quickly go through the open PRs. I think we've made a lot of progress here, actually.
I saw, Mario, you were working on this replace internal tools. It looks like it still is a work in progress, right?
**MM Mario Macias** 47:10 Yes, yes. Basically the… is the oats testing… that is preventing this to work. I've been updating OATs and the oats environment, but I had some difficulties, because there are some breaking changes, and yeah, I have to do other things, and…
**Tyler Yahn** 47:32 Yeah, no worries.
**MM Mario Macias** 47:33 We'll try to provide more… More… or to get more time.
**Tyler Yahn** 47:38 Yeah, yeah, absolutely, and it's a work in progress, so, yeah, understood.
And then the last three, we've actually already talked about. Mario's definitely looking for some reviews on this one. We just looked at this one from Rafael, and then the VM integration test from Steven we've talked about as well, so I think that's probably it.
Cool. So, Nikola, you also added this, V01 milestone. The only thing left is this, Code Swap, which we've taken a look at a few times. Mario, I think you actually had a PR to move some things as well.
**MM Mario Macias** 48:11 Yeah, I moved, all the packages that could be directly moved to internal are moved now. I would like to also check if inside the packages that cannot be directly moved, if there are some components That could be made private, or moved to the… or only some components moving to some other internal package.
**Tyler Yahn** 48:38 Yeah, okay.
That sounds good.
**Rafael Roquetto** 48:41 Okay, so…
**Tyler Yahn** 48:41 Oh, yeah, well…
**Rafael Roquetto** 48:44 Just one thing to bear in mind when we're doing this, it can affect the beta, so it has happened. Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 48:52 Yeah, yeah, yeah.
**Rafael Roquetto** 48:52 just make sure that the API doesn't… is not being used by beta when it gets moved to internal, because I had to copy code around, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 49:00 Yeah, we do that. Yeah, and this, like, Tyler's done a lot of work in here to kind of find all the packages that Vela uses, and… Hmm, sir.
**Tyler Yahn** 49:09 Yeah, I'm basing it off of this list here, is what I was looking at originally, and obviously, it's evolved, because Mario's been doing cleanup, or changes inside of Bela, so this was originally… this rep was done in Bela to get the dependencies, but yeah, we're trying to… yeah, that's… that's the main concern right now. So yeah, good call out, Rafael.
**Rafael Roquetto** 49:29 Cool, thank you.
**Tyler Yahn** 49:33 Okay, cool, so we'll wait on this one. Looks like we're still a work in progress on this, but then moving closer towards, that initial release, so, yeah.
Okay, that's the end of the agenda.
I can stop sharing my screen here. Any other topics people want to talk about that we don't have, written down?
**Mattia Meleleo** 49:56 I just wanted to introduce you to Giuseppa, which is a new colleague. We'll be starting to work In Obi, I think, in a couple of days. He's doing the onboarding right now, so if you have any… any issues, eBPF-related, he's very… Excited to start working on it.
**giuseppe.ognibene@coralogix.com** 50:16 Hi, everyone. Nice to meet you.
My name is Giuseppe.
Actually, today's my first day, so… I'm just started.
But I'm really excited to work with you.
**Rafael Roquetto** 50:30 Benvenuto.
**MM Mario Macias** 50:34 -
**giuseppe.ognibene@coralogix.com** 50:35 Nice, Italian.
**MM Mario Macias** 50:38 Rafaelis is our master in Latin-derived languages, knows Spanish, Portuguese, Catalan, Italian.
**Tyler Yahn** 50:46 What Romania.
**MM Mario Macias** 50:47 There's…
**Rafael Roquetto** 50:48 Mario's lying.
**Mattia Meleleo** 50:51 Peace.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 50:51 What about Romanian? Yeah, do you know Romanian, Durfan?
**Tyler Yahn** 50:54 I'm expecting fluency, too.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 50:56 She wants to do this.
**Rafael Roquetto** 50:58 Only a bit of gold, that's all I know.
**Tyler Yahn** 51:05 Well, awesome, yeah, glad to have you here. Thanks for joining, so yeah, hopefully we'll, we'll see you, see you around.
**giuseppe.ognibene@coralogix.com** 51:11 Thank you. Thank you, everyone.
**Tyler Yahn** 51:16 Well, cool.
Yeah, if there's no other topics, we could probably end it here. Thanks, everyone, for joining, appreciate all the hard work, a lot more to look into, so yeah. And Rafael, have a good time on vacation. We'll see you in a month.
**Rafael Roquetto** 51:30 Thank you.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 51:31 Bye.
**Tyler Yahn** 51:31 Bye, everyone.
**MM Mario Macias** 51:32 I…
