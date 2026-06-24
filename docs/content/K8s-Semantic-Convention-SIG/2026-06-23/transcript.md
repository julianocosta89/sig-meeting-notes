SIG: K8s Semantic Convention SIG
Date: 2026-06-23
Duration: 16 minutes
============================================================

## Zoom Recording Transcript

**Stephen Lang** 00:29 Hey.
**Christos Markou** 00:33 Hey there.
**João Marques Correia** 00:39 A.
**Stephen Lang** 01:44 So, I added a link to An issue that spoke about.
And a couple of times about the generic workload attributes.
So, David previously said that this should probably be trapped in its own issue, because it was, like, a comment of another issue previously.
So now I've raised it with semantic conventions, that seems to be triage accepted. So I just wasn't sure on the process now for, Getting some attention on this, if we need to just wait and see and leave it with… semantic conventions, SIG, or if it's… like, is the K8 SEMCOM, like, a sub-sig?
of the semantic convention sig, and do… do we need to sort of triage this here? So I was just kind of wondering what… where this kind of goes.
From, from being triage accepted.
**Christos Markou** 02:41 I guess, maybe start the discussions with APR to… since there is no objection so far.
Maybe APR will be the next step, and we can check there.
If there are any additional objections or something.
**Stephen Lang** 03:01 Sure, I can do that.
**Christos Markou** 03:04 Okay, so on the… on this or… old issue.
Yeah, I see the summary, David said that… Okay, so it's two different things. So one thing is the ruling, which we should establish at some point.
to follow when we have objects that are not of the default API of Kubernetes.
And what you… Are willing… What you're willing to add here is… Workload name and type. Okay, I see. And David has… Yeah.
is positive on this. Okay, that's good. Probably, yeah, that should be fine. I guess PR should be the next step, then.
**Stephen Lang** 03:50 Sure, thank you, yeah, I can erase that and discuss more on the PR.
**João Marques Correia** 04:06 Okay, I guess I can go next, if there's anything else. I wrote a comment in… So it was regarding an issue, like, we discussed a while back, regarding the container CPU usage metric.
So now I spent some time Just trying to validate that, so, and actually show the issue, that there is with the, way we exist… well, we collect the metric… the metric right now.
So, I shared the… comment, I put the link in the… the meeting notes… But basically, yeah, it's easy to see, basically, like, if we increase the step interval, then we start missing data. Like, the service was designed in a way to show that problem, but We start missing data, and… if we compute, basically, the container CPU usage within the receiver, we get much more valuable data, right? And it basically adapts based on the script interval defined by the user, so… For me, it makes way more sense to just start computing the… to basically compute the container CPU usage within Kubelet.
Based on the scrape interval, but those are basically my findings, and I wanted to share that with you, and also see if there are any comments Or any objections, or if it's something that maybe we should push for.
**David Ashpole** 05:31 Awesome, thanks for doing all that work. Results look really cool.
And so, sorry, just, paging this back in. So this is… we had previously discussed doing this, right? And I… What was the conclusion we came to last meeting?
Because I thought we were…
**João Marques Correia** 05:52 That's… I think that we basically missed the conclusion, right? Because I think even Chris had shared, like, a comment where we were still lacking a little bit the conclusion, right? So these were basically just trying to, one, prove the point, that I think the current, way we collect and share usage does have a problem, right?
**David Ashpole** 06:11 Yep.
**João Marques Correia** 06:12 and trying to propose a solution, but I just wanted to check if everyone agrees with this, or if there are any concerns, basically. Because if everyone agrees, then I guess we can raise an issue, like, potentially look into the implementation, but that's what I wanted to confirm with everyone.
**David Ashpole** 06:29 I think I was on board last time. I think, Dimitri, I think you had some concerns? Does this alleviate those?
**Dmitrii Anoshin** 06:36 So…
**David Ashpole** 06:36 You remember the previous discussion?
**Dmitrii Anoshin** 06:38 Yeah, like, just… Briefly, so what's the suggested solution here? I don't remember that part.
**João Marques Correia** 06:47 The solution is to compute the container CPU usage within QBlad Sass receiver using the, CPU time, right, because we are emitting CPU time, so we do have time, and basically just do the difference of two CPU time values based on the scrape interval, if that makes sense.
**Dmitrii Anoshin** 07:06 Yes.
**David Ashpole** 07:07 Do you want to share your screen and show the graphs? I think the graphs are pretty… pretty cool.
**João Marques Correia** 07:13 Let me maybe try that.
**Dmitrii Anoshin** 07:16 As long as we are not… bringing any issues with that approach. I guess we shouldn't be, but… Yeah.
**João Marques Correia** 07:28 Yeah.
**Dmitrii Anoshin** 07:28 if we… if we get a metric, a scraping the role, that provides us, like, the most accurate data with existing CPU usage.
And… We… if we apply… Calculation based on the… Time, it should provide the same values, right?
**João Marques Correia** 07:46 That's the thing… actually, I can maybe share this screen, and maybe that'.
**Dmitrii Anoshin** 07:50 Yeah, go ahead.
**João Marques Correia** 07:51 Because… Actually, using container CPU can sometimes even be a little bit better, and if I can… let's see if I think this is the one.
Are you able to see? Yeah, well, actually, no one.
Why is it?
So basically, the first two are what we are doing right now, right?
And so you can see mostly the problem when you increase the script interval, where basically a lot of the spikes are being missed.
And also, when I increase the scale interval, technically the spike should be smoothed out, right, because then you can expect, like, everything to be much smoother.
Which is what's happening here, it's just that it's way more precise. Like, if you look, there's, like, three decimals, but it's basically, like, a straight line, in a way, which is, like, the new way of, like, the proposed way of actually computing it on the service.
And one major advantage, actually, over straight pulling time, because this is doing the rate on time, that if I use a 10-second scrape window, right.
with container CPU usage, I get basically the exact behavior on how the service behaves, which is 50 seconds sleeping, 10 seconds of maximum CPU, and I can definitely see that.
When you do a 10-second pulling on time, the thing is, when you apply the rate, you need to apply the rate over an interval, right, because you need multiple values. And to be safe, you probably need, like, 3 to 4 values on that interval, so… it starts smoothing out things, so for you to get the same kind of this precision level, you maybe have to strip even more with time. So, that's one benefit you can gain as well by doing continuous CPU usage this way, if that makes sense.
Because then you don't… basically, you can have that window over the 10-second interval, right? Just see the delta over 10 seconds. When this, like, you probably have to use, like, if you're scraping still every 10 seconds, you need… A bigger, like, slide… like, sliding window to basically, ensure that you have enough values. And so you can see that basically this is already way smoothed out, like, we stay around 0.2, right, which is basically around the average, or a little bit above average, and we see some spiky behavior, whilst here, with the same 10-second scrape window, we basically get the exact behavior of how the service is consuming CPU. Does that make sense?
**Dmitrii Anoshin** 10:18 Yeah, it does make sense.
**David Ashpole** 10:20 I see, so the bottom one would look like the top one if we used a 10-second… Scrape interval, or if we used a 10-second interval.
**João Marques Correia** 10:28 But the thing is, this should look exactly… yeah, so if we use 10-second interval on this bottom one, it should look like this. The main problem is you probably need to pull every, let's say, 2 to 3 seconds to ensure you have enough values.
within that 10-second window to ensure that the data looks correct, right? Because otherwise, if you don't have two values within the 10-second window, then you cannot compute the rate, if that makes sense.
**David Ashpole** 10:53 I thought… Is this PromQL, or is this a different query engine?
**João Marques Correia** 10:57 This is from Killa, everything's been prompted.
**David Ashpole** 10:59 I thought it extrapolated outside of window boundaries.
**João Marques Correia** 11:04 Can it extrapolate? But what I was seeing when I… at least with extrapolation, when I tried to remove the window, sometimes, it can spike.
over what is supposed to be the limit. Like, I saw spikes, like, if it doesn't have any… like, for example, it should not go above 1. I saw spikes at some point at, like, 1, 2, 1, 3, right, which… didn't make sense in this case, because there was a limit of one CPU, basically.
**David Ashpole** 11:30 Yeah, I wonder if the new, rate parameter things they added recently would help here. There's, like, an anchored one that prevents it from over… over-extrapolating.
**João Marques Correia** 11:42 Oh, okay. Maybe that…
**David Ashpole** 11:44 I guess the downside of… The middle one is that if you ever… missed… Like, if you ever drop a data point, then… You actually just have a gap in your graph, right?
For the pre-computed… Instantaneous usage.
**João Marques Correia** 12:04 You might have… yeah, because that, I guess, we will rely on the scrape.
to compute, so I guess what might happen is you will have, like, a bigger window, right? Because the computation happens when it's sprayed, right? So, if there isn't a hit, what might happen is you might just miss.
**Christos Markou** 12:24 But this is expected, though, should be the same on other things, like host metrics and process usage, and… Utilization.
**David Ashpole** 12:34 No, I think it's exactly right. I was…
**João Marques Correia** 12:37 But even my point is, like, I think it's valuable, like, this should be probably the lower one is what we say is the… recommended way, right? I think this is nice to have, but I just feel like at least what we are doing now is definitely wrong. So that was kind of been the point, just trying to at least move from what is at the top to this, we already get, like, way more meaningful data. Does that make sense?
**David Ashpole** 13:00 Yep.
**Christos Markou** 13:02 I guess we can, try this in the implementation directly, behind feature gates.
see what people believe. If nobody complains, it's okay. Yeah, hopefully nobody will notice or will complain about this, and then we can get back and probably tune the semant conventions, to clarify. I'm not sure if we need to do… do it, maybe we need to do it. But first, let's try and see if the implementation… Should be okay. Behind the feature gates, we can promote them to better, see someone complaints and, proceed accordingly.
**João Marques Correia** 13:47 So I should be able to take a look at that. I have an implementation, but it's very hacky, at least to get this going, so yeah, I'll need to clear that out to make it…
**Christos Markou** 13:56 And if my assumption is correct, based on these, so if we change the usage.
And we calculate this on the fly. We should also change, we should use this on the fly calculation for the utilization.
Metrics that we have, right?
That rely on this usage metric. Okay, so all those should be botched together. Great, okay.
Thanks, thanks, Joe, for taking this.
**João Marques Correia** 14:26 That.
**Christos Markou** 14:31 Okay, I think we don't have anything else.
Anything else from your side, folks?
By the way, it's related to this group, the attributes, have been released as… the K attributes have been released as stable, for a couple of weeks now, and go… OpenTelemetry Go project created the new semant conventions package, and I have a PR that… downstreams, the new… the new version, the stable, generated some other conventions to the KH processor.
And I'm also suggesting the CH processor for graduation, after some discussions that we had with Pablo. Dimitri, you should be pinged there, if anyone else is interested to have a look or whatever.
everything should be linked to the KH processor stability meta-issue that we have in collector country, so feel free to have a look. I guess it will take some time, so we can collect feedback, but there is intention to move this forward.
And, Pablo will be doing, from the side of maintainers, the, let's say, the… will run the process of evaluation and everything.
So, we will have, I guess, something more concrete in the implementation side as a result of this group. So, yeah, thank you everyone for… Helping with Okay, that's all we had then.
For today. Thank you, everyone. See you in the week.
**Dmitrii Anoshin** 16:14 Equals.
**David Ashpole** 16:16 Bye.
