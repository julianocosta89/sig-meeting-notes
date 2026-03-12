SIG: Kubernetes Operator SIG
Date: 2025-12-04
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Benedikt Bongartz** 00:34 No…
**jea** 01:19 Hey, everyone. Oop.
Nevermind.
**Mikołaj Świątek** 02:04 Okay, can you hear me now?
**jea** 02:06 Yes.
**Mikołaj Świątek** 02:08 Alright.
I… Zoom just did some really weird stuff.
First, it froze for, like, 20 seconds while joining the meeting, and then after I got in, I had literally no sound.
And my microphone apparently wasn't working either.
Well, that's fine.
**jea** 02:39 We don't have anything on the agenda… oh, no, never mind, we do.
Ben, are you writing something?
**Mikołaj Świątek** 02:47 Yes. There's something… issues… issues to discuss.
**Benedikt Bongartz** 02:54 Yeah, unfortunately, antoine is not here.
Because I would like to discuss the cluster Observability Custom Resource.
But, just as a reminder, I pinged all of you, would be nice to get some input.
**jea** 03:14 For which?
**Benedikt Bongartz** 03:16 This initial draft of the, observability… class observability custom resource.
I will just link it in… give me one second, I will find it.
Copeling… Oh, wrong meeting note.
On this one. I think we can extend this also to what Mikolai was adding, that we don't want to support all the OTAB fields.
I personally would prefer to just… if there are things we are unsure about, just rip them off, and then just add them later, so that we can get this thing in, and it's not an… For requests, which is… Open for 10 years, so basically just unblock it, and then get it in, and continue then.
I'm also fine with just insecure OTLP export, so just one endpoint you can set, and you're ready to go.
This should be good for experimenting with it.
**Mikołaj Świątek** 04:57 Yeah, it's like… It doesn't… we're… we can make breaking changes to it, as it is, like, whatever is in that PR, even if we merge it, is not enshrined forever.
**Benedikt Bongartz** 05:12 then I would prefer to just fix it up, and just merge it, and then continue.
**Mikołaj Świątek** 05:18 Oops.
Probably fine with me not having actually read any of that discussion for a while, but I'll check it out.
**Benedikt Bongartz** 05:34 This other issue, there is… oh, this other pull request.
I don't remember his name.
He reached out to me, Simon, and asked.
specifically about this pull request, and if we can move on with this. Last time we, I guess, discussed a workaround for the host ID, that you just deploy a pod, and just add OpenTalent Collector as a sidecar.
And this doesn't work because of the receiver that he wants to use. I didn't have the chance, unfortunately, to look into. It was more that I just also wanted to raise awareness about it.
**jea** 06:17 Yeah, I forget exactly, like, Is it fine to do this? I honestly forget. This was, like, 3 months ago, I think.
**Benedikt Bongartz** 06:28 I forgot to, so I said that I will try before this meeting to refresh my mind on it. I didn't have the chance, unfortunately.
Yeah, so I will try to get some… better understanding in the next days, and I thought I would just mention it and, you know.
**Mikołaj Świątek** 06:50 Something I did not understand from the start about this is, like, why is adding this field any different than adding any other field?
**Benedikt Bongartz** 07:00 I think the… I don't remember exactly, because it's quite a while ago, I think we had some security concerns.
**Mikołaj Świątek** 07:12 I mean, but if it's a security concern, then it's a security concern that the user inflicts on themselves by setting it. And it's settable in the… in, like, a normal pod, so it's not like we are any different than playing Kubernetes.
In this respect.
**Benedikt Bongartz** 07:32 So I have currently no real objection. It's… yeah.
**Mikołaj Świątek** 07:38 You can only set it in daemon sets, so maybe it's worthwhile to… I don't know, you can set it everywhere.
Right?
I don't know, like, this PR, if it were completely up to me, I would, like, allow this PR to be merged as is, with, like… Maybe a… some, like, nitpicks about, like, how there's, in my opinion, two… the end-to-end tests are unnecessarily large, there's some, like, customization remainders, and so on.
It's like… I don't really see any problem with letting users just set this value.
Give me a moment, okay, I need to quickly… Let me do something.
Okay.
**jea** 09:35 Sorry, I'm… I got distracted answering other questions in the Slack channel.
So we just need to give some feedback to these folks, is that the… is that the idea?
**Benedikt Bongartz** 09:52 Nope.
**Mikołaj Świątek** 10:05 Alright, but I personally don't see any problem.
Of the host PID stuff. If you find a problem that you… or you figure out what problem you originally had, I'd be happy to… Talk about that.
But, in my opinion, we can… Easily.
merge that PR once it's cleaned up a little bit.
Alright, so you wanna, you wanna go through the… Future flags? This is just, like, a reminder.
So, like, the co… the Golang flags, we just set to beta, so it can stay in beta for a little bit more, I think.
MTLS is not ready.
**jea** 11:09 there's a PR, which is…
**Mikołaj Świątek** 11:12 messing with the renewal and the durations of the certificates, because this is… there's, like, a subtlety in there, as it turns out. You have to be a bit careful about, like, how your CA certificate that you have inside the cluster renews.
callback strategy is in alpha, and it should probably be removed once I get to implementing the… Configuration, for… for strategies.
It will happen at some point. Enable config defaulting is stable, and I think should just be removed. I don't know who's, like, in… In charge of that.
But it should happen, and the other two are relatively new, and I don't think… We need to do anything with them.
So, for me, the only… The only conclusion is that the config defaulting in future 5 should just be dropped.
Who's, who's doing the release this week, by the way?
**jea** 12:14 I think Tyler?
**Mikołaj Świątek** 12:16 I wonder if he's actually… not on PTR or something.
Okay. He's not because he wrote today on our channel.
on the list.
**jea** 12:27 I think it's just probably busy.
**Mikołaj Świątek** 12:30 No.
Alright, no, that's fine. He's aware that it's him, and that's good enough for me.
And the final bit is issues to discuss.
**jea** 12:43 I think it's basically just review the PR that Ben already linked.
**Mikołaj Świątek** 12:47 This is what it seems like to me.
I added an issue to this cost, but it's actually a pull request. Oh. And it doesn't show up here for some reason.
**jea** 13:00 We probably just need to… it's because we have the Issue label on it.
**Mikołaj Świątek** 13:04 Okay.
**jea** 13:05 Let me… let me change the… I'll edit the link in there so that it doesn't include that anymore.
**Mikołaj Świątek** 13:14 Anyway, it's… the PR I wanted to discuss is this one. I'll put it in chat.
It's about adding scrape classes, and the technical side of this PR, I think, is fine. Like, the implementation looks fine to me. Yeah. The only problems of it is that It's a similar problem to the OTLP exporter situation. So, like, a scrape class is not a CRD, it's like a struct that has embedded in the Prometheus CRD.
And the question is, how should this work on our end, right? The question is… there's two problems, potentially, of it. One problem is that it makes us dependent on that, on the Prometheus struct, and that one is in V1, it's stable.
So, there's, like, some decent guarantees.
But it's still gonna be something that whenever we bump the Prometheus operator, dependency is gonna cause, you know… Yeah.
**jea** 14:19 more things.
**Mikołaj Świątek** 14:19 Like, that's not the problem in itself, like, every time we bump the Kubernetes core libraries, it also results in changes, so that by itself is not a big problem, but it is an additional dependency. In my opinion, the larger problem of it is that This is quite big. It, like, makes the CRDs bigger, and… The alternative is maybe to change it into some, like, you know, some blob?
some, like… list of maps. For example, we have this for scrape configs in the target allocator CRD.
Or scrape configs are just a list of, any config.
And… so that's something we could do. We could also say, and this is also fine for me, from my perspective, is that we're not adding this to the OpenTelemet Collector CRD.
Which is too big.
But the target allocator CRD is smaller, so we're fine adding it just there. In my view, this is, like, more of an advanced user feature, so it's fine to confine it to the target allocator CRD.
I'm definitely kind of against adding anything new to the… Opentelemetry collector.
**jea** 15:41 And this is also one of those things that feels really Prometheus-specific, and not everybody's gonna take advantage of.
And I think it just… I think I agree, it makes sense to only add it to the target allocator, where it's like… If somebody really wants to use this, they're probably… they know what they're doing, they should be… they should be, able to deploy the target allocator CR themselves, and move things to that, so that they have more of the configuration there. I think that it's a good lever, so I'm in favor of that.
**Mikołaj Świątek** 16:14 Okay, cool.
In any case, there's a discussion happening in that PR, so if you have a… if you have an opinion, please put it in there.
**jea** 16:24 Yeah, I'll just put… I'll put what I just said in there, to make that clear.
**Mikołaj Świątek** 16:39 Independently, like, we don't really have any topics, but one thing that kind of stands out to me, and we don't have an issue for it, is that… There's a… we have, like, an end-to-end test, which is flaky, which has to do with file log receiver somehow, and it's only flaky on Kubernetes 125.
And I'm, like…
**Benedikt Bongartz** 17:00 Isn't that fixed? So we had this when I added the end-to-end test profile receiver.
Mmm… Alright, I can see.
I think it was last time?
I'm not exactly sure, but I had in mind that the problem was, in the newer Kubernetes version, we used the native sidecar, that's why the OpenTent Collector is up and running before the file is produced.
And then we changed it to start from beginning of the file, which means even if the collector is started afterwards.
**Mikołaj Świątek** 17:53 Hmm.
**Benedikt Bongartz** 17:54 It will transmit the same data.
And I thought that's the fix, and it was good afterwards.
I will look into this.
**Mikołaj Świątek** 18:10 Because I see it crop up on, like.
**Benedikt Bongartz** 18:12 Yeah, I see it now, too, on the latest Comet, for example.
But I thought I did fix this in the past.
Let's see, this was… Yeah, I will have another look.
**Mikołaj Świątek** 19:05 Maybe all this stuff kind of proves that this test is too complicated, and maybe it should do something simpler. What does it even do exactly?
**Benedikt Bongartz** 19:16 It's a while ago that I wrote it. I think it just reads some logs, and writes them, and then we query… The collector, if there are some lock lines, so it's not really complicated.
So I really thought it's just a race condition.
**Mikołaj Świątek** 19:45 You know, you can also… you can also use, like, a train cell function to parse Prometheus metrics.
We do that in other.
**jea** 19:54 Oh, did they add that in Finley? Did that land?
**Mikołaj Świątek** 19:56 Yeah, we actually use it in a bunch of instrumentation tests.
**Benedikt Bongartz** 20:01 But that's what it does at the end, right? So it goes… Here to search.
**Mikołaj Świątek** 20:09 You're looking at the change, you, you… You linked, and that one runs, like, a bash script.
**Benedikt Bongartz** 20:27 Yeah, which is then calling the metrics endpoint.
**Mikołaj Świątek** 20:33 So you think this is a problem with sidecars?
**Benedikt Bongartz** 20:38 I think, yes.
Because it… the main issue was it disappeared with the newer Kubernetes version, and I was completely confused that it works with newer ones, and it doesn't work with the old one.
And… Disabling native sidecar, just… Cause the same error.
**Mikołaj Świątek** 20:59 But is this supposed to do anything with sidecars, or is it just supposed to check if…
**Benedikt Bongartz** 21:07 The idea here is to read from a specific log file within a container, so not from standard out or something. So, like, imagine you have an application which produces standard out logs, but also has something like access.log or something.
And now you would like to deploy the Open Savage Collector as a sidecar, which… Then, just starts reading this extra file, which is on… the POTS file system.
Yeah, but this is already more than a month ago, so I really need to… C.
**Mikołaj Świątek** 22:02 It is definitely a race condition if you are not, like, waiting for it in a loop.
Right? Because you don't actually know when you're gonna read those logs, in principle.
It might also be possible that it's something like the scheduling, but no, it shouldn't be the scheduling, right? Because… You have to wait until the pod is actually running before you can do any of the things that are… Or do you?
**Benedikt Bongartz** 22:34 No, so the only thing is that… In the native sidecar scenario, you start the open talent collector, you wait until it's up and running, and it's… Physically ready to do something.
And then the second… Pod is launched, and then you should receive the logs, and you're good to go.
And…
**Mikołaj Świątek** 23:02 I think there should be a… I think this test is just missing a step where it waits until the pods are running, because I don't see it doing it anywhere.
**Benedikt Bongartz** 23:14 industry.
**Mikołaj Świątek** 23:15 goes, like…
**Benedikt Bongartz** 23:16 And so the deployment is ready.
**Mikołaj Świątek** 23:19 Right.
**Benedikt Bongartz** 23:19 replicas already?
**Mikołaj Świątek** 23:21 There is an assert here.
**Benedikt Bongartz** 23:23 Yes, sir.
**Mikołaj Świątek** 23:27 Yeah, that should be fine then, then they both should be running in that case, so I'm not sure what the problem is.
**Benedikt Bongartz** 23:38 Yeah, so maybe the bash script?
Generate logs.
Terminates before the collector is able to… Get the data?
And chainsaw is able to scrape it or something, I don't know.
**jea** 24:18 I'm gonna drop, it sounds like you guys are in.
**Benedikt Bongartz** 24:22 I think it…
**jea** 24:23 I would…
**Benedikt Bongartz** 24:24 Try if we can just add another sleep in this generate log script, that it sleeps forever.
Because I currently expect… it's just a guess from what I'm reading, it just terminates before the collector gets this data, and Chainsaw is able to scrape it.
**jea** 24:45 I'm gonna drop this. I'll see you later.
**Benedikt Bongartz** 24:47 Bye.
**jea** 24:48 Then I'll review that PR, sometime maybe tomorrow or next week, but… Okay, bye.
**Benedikt Bongartz** 24:56 Sir, bye.
That's the only thing that… looking at it, and then… Could potentially make sense to me.
Let me share it.
How does it look?
So currently, this thing gets started?
We have the files here, so we go to… deployment.
So now, the deployment is created, this pod is created, we inject the sidecar.
BusyBox, I imagine… starts quite fast.
And then this script is executed, which takes… 30 seconds? 60 seconds. So this part is alive for 60 seconds in total.
Until it will die.
And now the question is, will this produce some logs in this… during this 60 seconds? And the open terminology collector.
Here, where we can go to the collector config.
Maybe even reads the logs in these 60 seconds, and… I don't know when the metrics are scraped.
Timeout 90 seconds… Yeah, I think I need to execute it and just observe it.
**Mikołaj Świątek** 27:16 I don't know, like, my just general intuition is that there should be a way of making this work.
Like, there should be a way of making chainsaw just repeat the… Their metrics, their request for metrics, and just do this that way.
**Benedikt Bongartz** 27:34 Select a retry here.
**Mikołaj Świątek** 27:37 Yeah, there should be a way, right?
**Benedikt Bongartz** 27:41 I don't know.
**Mikołaj Świątek** 27:54 Because if you do an assertion Normally, when you do an assertion, that's what happens, right? It will just retry and wait until the thing is true. It's just that here, it's asserting on some value that we retrieved in the previous step, right?
**Benedikt Bongartz** 28:14 The question is if… The… the deployment simply doesn't live long enough.
So if they retry with, let's say, 30 seconds, maybe in the first call, nothing is there,
**Mikołaj Świątek** 28:34 Deployment has to be.
**Benedikt Bongartz** 28:35 So you do the first assert, you do the first assert at 29 seconds?
So before the pod starts?
So it remains… it claims it's there, but OpenTime Collector is still starting, so yeah, let's say it takes 1 second, and you make the first… Call?
And then you have 31… Where you would do the next one, and then technically the open circuitor should be up and running.
Maybe the runner is just too slow.
Wouldn't surprise me.
**Mikołaj Świątek** 29:52 Maybe I'll try to… I'll try to mess with it locally, see if I can, like… make it simpler somehow, because I feel like it should be possible to make it simpler.
But I'm not sure if, like, what I think… Should be possible, is possible.
**Benedikt Bongartz** 30:15 I like the description.
**Mikołaj Świątek** 30:21 Yeah, it's true.
That's true.
A valid… a valid observation on the first half in the third.
Alright, buddy, I'll be, I'll, I'll be, I'll be off as well, if you like.
figure out anything, or need more eyes, then just hit me up on Slack, okay?
**Benedikt Bongartz** 30:45 I will do. See you then. Have a nice evening. See ya. Bye-bye.
