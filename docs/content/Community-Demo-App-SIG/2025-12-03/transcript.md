SIG: Community Demo App SIG
Date: 2025-12-03
Duration: 18 minutes
============================================================

## Zoom Recording Transcript

**Juliano Costa | Datadog** 01:17 Hi.
I thought I would be alone.
I can't hear you.
Nope.
maybe… Maybe it's me?
Okay, yeah, now I can hear you.
**Roger Coll** 01:36 I don't know, takes… Normally 10 seconds or so to…
Could be sensitive… sensitive? I don't know.
It happens every time. Good, good, good, quite good. Poor audio.
**Juliano Costa | Datadog** 01:51 Yeah, busy, but good.
Yeah.
**Roger Coll** 01:55 Cool. Did you make it to KubeCon last week, or Theodos, or not this time? No, no.
Oh, no, me neither,
Some folks were there, but yeah, unfortunately not this time.
**Juliano Costa | Datadog** 02:08 Yeah, I met… I met some of the Elastic folks on the KCD… Versal?
**Roger Coll** 02:17 Mmm, it's Poland, right? Yeah, okay.
**Juliano Costa | Datadog** 02:21 Andre, Milas left… And…
**Roger Coll** 02:25 Yeah.
**Juliano Costa | Datadog** 02:25 And another guy that I don't remember the name.
**Roger Coll** 02:28 maybe Mikolais, or, wow.
**Juliano Costa | Datadog** 02:34 Yeah, I think so, yeah.
**Roger Coll** 02:35 Nikola works a lot with the operator, and Andre in the… with the collector itself, so…
**Juliano Costa | Datadog** 02:43 Yeah, Andre was on the booth, on duty, but yeah.
**Roger Coll** 02:47 Okay.
Did he make any presentation, or not?
**Juliano Costa | Datadog** 02:53 Yeah, Andre presented a sponsored talk.
**Roger Coll** 02:57 Okay.
**Juliano Costa | Datadog** 02:57 he was, like, talking about Elastic and, Ulta.
**Roger Coll** 03:02 Oh, okay, nice.
Cool, cool.
Yeah, they're all waiting.
**Juliano Costa | Datadog** 03:08 It was pretty hotel-intensive, actually.
**Roger Coll** 03:13 I'm a truck.
**Juliano Costa | Datadog** 03:14 Yeah, it was… it was really good. Robert Patzak was also there.
**Roger Coll** 03:19 Okay, okay.
it was a Kubernetes-focused, conference?
**Juliano Costa | Datadog** 03:26 Yeah, so, like, KCD is, like, Kubernetes Community Days, but it's more like,
called Native Community Days, so to say.
**Roger Coll** 03:35 Okay.
**Juliano Costa | Datadog** 03:36 Yeah, it started with a K for.
**Roger Coll** 03:38 Boys, K.
**Juliano Costa | Datadog** 03:39 But it's more like KubeCon, not KubeCon, you know, like…
**Roger Coll** 03:45 Okay, yeah.
**Juliano Costa | Datadog** 03:45 It's, like, CNCF clone?
**Roger Coll** 03:48 Yeah, yeah, yeah, I guess. Maybe it's better to call it like that. Also, KubeCon, there's a lot of open telemetry now, and different…
projects, probably they will rename it someday.
**Juliano Costa | Datadog** 04:02 Yeah.
Or, hopefully, they will split up and have just a observability cone. Yeah, yeah. And,
let Kim Kong leave alone, yeah.
**Roger Coll** 04:16 Yeah, that's a good one, because there's a lot of observability talks that the observability day, right, before just the KubeCon, that it's pretty busy, so…
Yeah. Probably it's time.
Let's see, let's see. I would be happy if they did.
**Juliano Costa | Datadog** 04:38 I do not have any… anything on the agenda, Roger. Do you have anything that you would like to discuss?
**Roger Coll** 04:45 Hmm.
Not really, not really. I personally haven't.
They're gonna…
a look at the open telemetry, at least on the open issues, so much. I was checking this one about the open search,
limit this morning, I think there's, an issue that,
someone open, and it actually happens to me a lot the same. Let's say if I do a quick make start.
maybe the first 3-4 times, it won't work because of open search, and then, well, if you keep trying at some point, it won't go, yeah, after the.
**Juliano Costa | Datadog** 05:31 Yeah.
**Roger Coll** 05:32 And it will work. But, you know, it's me knowing that, maybe it's not the best for,
someone just trying it for the first time, because probably we'll start debugging, right? And… Yes.
**Juliano Costa | Datadog** 05:46 Yo.
**Roger Coll** 05:47 Why is that? But not sure what we can do, because…
**Juliano Costa | Datadog** 05:51 I think we can simply improve the memory. Someone said the PR improving, increasing the memory? Improving, increasing the memory.
But he didn't want to… the user didn't want to sign the ACLA, so he was like, I'm not signing me anything for this.
**Roger Coll** 06:10 Dude, what we can do, yeah.
**Juliano Costa | Datadog** 06:13 Yeah, sorry, I can't accept your identity.
**Roger Coll** 06:16 No, no, bro And it's still open at PR, or… We can…
**Juliano Costa | Datadog** 06:22 No, no, I closed it.
**Roger Coll** 06:23 Oh, good.
**Juliano Costa | Datadog** 06:24 Basically, we just need to increase the memory limit. I… I haven't done, just…
I don't know why, but it also happens with me.
I… I wish we had a better solution, not…
not that increasing the memory is not the proper solution, but I wish we could reduce the open search footprint in the demo, because it's like…
One… now, if we increase, we are talking about increasing to 1 giga now?
**Roger Coll** 06:55 Which is…
**Juliano Costa | Datadog** 06:56 Like… This just receives the logs we not even use to visualize anything.
**Roger Coll** 07:02 Yeah, yeah, yeah, yeah, exactly.
That's some concerns that my, well, my colleagues are having at the moment, that…
they just spawn some, let's say, the standard EC2 instances in cloud for AWS, or whatever, and…
they cannot launch, let's say, the default demo, right, on the average, instances, and…
Yeah, they are impacted on the size of it, but this is a long-standing issue, right? There's the open search, and the other one was the load generator as well.
And for the open search, I remember that Shinoy did some kind of PR, maybe we didn't merge it, but he was…
Trying to use, a slimmer version of OpenSearch, I don't know how.
**Juliano Costa | Datadog** 07:58 In the end, we… in the end, he got back to it, and we merged, and that's when the limit got reduced, and that's when Elastic… not Elastic, OpenSearch started crashing.
**Roger Coll** 08:14 Okay, so…
**Juliano Costa | Datadog** 08:17 I actually pinged him on the issue, but I haven't heard back, so…
**Roger Coll** 08:22 Okay, okay, good. So we reduced it a little bit already, but now we are… we're crushing it. Okay, I see.
**Juliano Costa | Datadog** 08:29 Yeah So, I can actually… let me see if I can…
Boom.
So… There you go, 2587 is the…
issue. Sharing here on, on, on…
**Roger Coll** 08:56 Alright.
**Juliano Costa | Datadog** 08:57 Result.
**Roger Coll** 09:01 Cool, yeah.
Thank you.
**Juliano Costa | Datadog** 09:06 And then in here, we reduced from… 1.1 giga to 800M.
**Roger Coll** 09:14 In the beginning.
**Juliano Costa | Datadog** 09:14 But then, like, yeah, now we go back to…
**Roger Coll** 09:19 Hmm.
**Juliano Costa | Datadog** 09:20 Now we go back to one, so…
**Roger Coll** 09:24 Whoa.
**Juliano Costa | Datadog** 09:25 Because, I think this is,
I think in Kubernetes, they have something better now. You know, whenever you start the service, you get a peak on the memory consumption, but to actually run the service, you do not need all those resources.
I think that's… that had, Java in, in, what, when they were…
planning the feature, they mostly had Java in mind.
Because to start up, Java consumes a lot of memory, but then to run it…
doesn't. So you'll have all this… because if you don't locate the memory, you cannot use it. So if, let's say, the service to run uses 50 megabits, but to start it uses 200. If you don't give 200, it would crash loop.
Okay. So, they created a new type of, resource configuration on Kubernetes that allows, like, this 150 extra to boot… to boot the application, but then once it's running, it free that memory, and you're good to use just… you just have 50 allocated.
**Roger Coll** 10:42 Okay. But in our case, like.
**Juliano Costa | Datadog** 10:45 tracking the PR, we run open search, like, the, the…
The base image, and then we run, like, remove…
A bunch of remove plugin comments.
**Roger Coll** 11:03 Hi.
**Juliano Costa | Datadog** 11:04 I do say that this is…
**Roger Coll** 11:06 Yeah.
**Juliano Costa | Datadog** 11:07 Making the image limer?
But… I think… well, I don't know, maybe you have some experience, with, something similar in Elastic?
I don't know if you guys work in some ways here, but what we could… what I… what I was thinking, what we could do is, like…
We get the base image, then we remove all the plugins, and then we generate something else, like a binary or whatever, that this goes to another image where we can run.
And then we have, like, a multi-stage build. Because in this case, what I see is that we have, like, let's say.
an image that consumes… consumes 100, 1 giga, and then we remove a bunch of stuff, and now consumes, like, 800 megas, but.
At startup, it still consumes 1 giga.
So then it doesn't actually solve the issue?
**Roger Coll** 12:19 Yeah, exactly. I think what we need to solve is, like, say, the… the start experience, right? If…
If there's no problem on the start, then it means that you already have,
available memory, etc, etc, but what I think it's,
Yeah, bad user experience is when, either in Kubernetes or in Docker, you get the constant error that you don't have enough memory, because…
you need to switch either instances, or… yeah, some, somehow.
But, yeah, I don't know, maybe we can follow up with him. He has other, insights. I saw that, there was this…
This is the PR that I remember, that it was… there's an open search minimal image.
Maybe.
**Juliano Costa | Datadog** 13:15 Whoa.
Yeah, but if you check the one that I shared, it's basically the same. I think he just closed because he wasn't able to work on it, and then he just reopened.
**Roger Coll** 13:29 But it's the minimal as well.
You see, no, you see, if… I don't…
**Juliano Costa | Datadog** 13:37 But, yeah, I think here the only thing is that… Names the… the image?
**Roger Coll** 13:46 Yeah, yeah, yeah, I see, you're right, you're right. On the from…
**Juliano Costa | Datadog** 13:50 Oh, but wait.
**Roger Coll** 13:50 So, it's the same.
**Juliano Costa | Datadog** 13:53 No, you're right. Maybe we are… .
**Roger Coll** 14:01 No, if you… if you check the from in the Dockerfile, it's open search, it's the same one, it's just… I think the naming… I… I miss…
Miss-lipped myself out.
It says open source minimal, but it's kind of the image name, not… the absolute one.
So, yeah.
You know…
Well, we can.
**Juliano Costa | Datadog** 14:31 Beautiful.
**Roger Coll** 14:31 Yeah, I will keep an eye on that thread, at least, that we have open, and yeah, probably.
Get some insights there.
Unfortunately, yeah.
**Juliano Costa | Datadog** 14:47 Yeah, no, go ahead.
**Roger Coll** 14:48 No, sorry, for the load generator,
I don't know if we have someone from Grafana, maybe…
Yeah, we had some help from that guy, don't remember his name, but…
They have a tool that it's called…
K6S, if I remember correctly, that it's actually to do this kind of load testing, let's say, with,
playwright does, that I think it's the…
Let's say the highest memory dependency within the load generator.
And maybe we could switch to that,
I think I had a note on that, and some…
**Juliano Costa | Datadog** 15:38 Yeah, I saw your issue, yeah. But I thought K6 didn't have any browser.
**Roger Coll** 15:48 Not K6, but then there's a… I'm saying that because I saw a talk just a few…
One month ago, I think. And they have, then, a KX6 crocodile or something like that, that actually it's a… it's a Docker image with a Chromium embedded inside.
**Juliano Costa | Datadog** 16:07 Okay.
**Roger Coll** 16:08 it's to actually do this kind of, yeah, JavaScript testing, if it was, a browser.
**Juliano Costa | Datadog** 16:17 Okay.
**Roger Coll** 16:18 Maybe that could work, but…
Yeah, correct? Let me show you the issue that I created. I think I added the… yeah. I added a link to this
Proko Chrome, it's a Chromium supervisor, and I know they use it with, KX, KCX, 6.
to do… You know, synthetics, and these kind of things.
In Grafana.
But yeah, maybe I will keep it for next week, in case Cyril, I think it was now, joins, and maybe we can get some help from them.
**Juliano Costa | Datadog** 17:05 But for Chrome.
Nice. Yeah, I missed that, actually. I saw the issue, but I missed this plugin.
Oof.
And… Cool, because if we can run as, like,
Without actually needing the browser, then we are good.
**Roger Coll** 17:28 Yeah, yeah, exactly, I think it…
This image should have the minimum, minimum to just kind of replicate, A chromium.
**Juliano Costa | Datadog** 17:42 Yeah Cool.
Copy.
**Roger Coll** 17:48 Yeah, I'll… I will keep an eye, and maybe next week or something, we can… Yeah, mention it again.
**Juliano Costa | Datadog** 17:56 I think people are… at reInvent today.
**Roger Coll** 18:02 Little.
**Juliano Costa | Datadog** 18:02 I do.
**Roger Coll** 18:03 Yeah, totally.
**Juliano Costa | Datadog** 18:06 The biggest thing…
**Roger Coll** 18:09 Yeah.
**Juliano Costa | Datadog** 18:10 and KubeCon, so those are the two things that folks are…
**Roger Coll** 18:14 yeah, yeah, yeah.
**Juliano Costa | Datadog** 18:16 Me too. That's okay.
**Roger Coll** 18:19 Okay.
**Juliano Costa | Datadog** 18:20 Okay.
**Roger Coll** 18:20 From my side, that's it.
**Juliano Costa | Datadog** 18:23 Yeah, cool.
**Roger Coll** 18:25 Thanks for joining, Julianov.
**Juliano Costa | Datadog** 18:26 Yeah, thank you for joining. I was alone.
**Roger Coll** 18:29 I know.
**Juliano Costa | Datadog** 18:30 Singing, Hello Darkness. Hello, Darkness, my old friend.
**Roger Coll** 18:35 Yeah, we had a quick sync.
Okay.
**Juliano Costa | Datadog** 18:39 Awesome.
**Roger Coll** 18:40 Good week.
**Juliano Costa | Datadog** 18:41 Yeah, yeah.
