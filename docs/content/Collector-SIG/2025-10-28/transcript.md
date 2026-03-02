SIG: Collector SIG
Date: 2025-10-28
Duration: 21 minutes
============================================================

## Zoom Recording Transcript

**Andrew Wilkins @ Elastic Observability** 01:36 Rob, fancy seeing you here.
**Rob Bavey** 01:38 Hey, Andrew, how's it going?
**Andrew Wilkins @ Elastic Observability** 01:41 I agree.
Normally would have a couple of people by now. I might just ping… pick on Slack.
Sean's not able to make it.
Antoine's not online.
Maybe, Dimitri?
Right, I think so.
It's worth a couple of minutes.
Apollo.
**Paulo Janotti** 04:23 What are you gonna do?
**Andrew Wilkins @ Elastic Observability** 04:26 I think this might be all of us. Sean's not able to make it, Antoine's not online.
So, I guess we can start. I added a couple of things to the agenda. The first one actually is probably… I don't know if there's any point in bringing it up, but I'll bring it up anyway. It was mostly in case Sean was going to be here.
Since we were chatting about it on the issue. So our… my team is… is working on a… a receiver, which is currently not open source, but we're,
would like to offer it upstream, to the Contrib repository, and it's a receiver that can receive events from AWS Lambda.
And the events that it deals with specifically are events from CloudWatch and S3 event notifications. And the idea is to be able to forward logs and metrics from AWS, or sorry, not forward them.
receive logs and metrics from AWS services, parse them.
Convert them to OTLP, and then export them.
And the whole… whole point of that is to be able to have
minimal operational overhead, so you have, all auto-scaling of Lambda at your disposal.
**Paulo Janotti** 05:41 Since we don't have… if you don't mind, I have a few questions. I worked in the very beginning of the Lambda…
sick when you're doing… still creating the layer for the collector, so I stopped working on that, before there was anything, usable, at the time.
But I… I have two things in my mind.
One thing that they had, A problem was with,
The trigger to start, and the thing to have a time to kind of,
flush the data, because otherwise, either you send the data synchronously, or there is the risk of shutting down the Lambda before you send the data.
Do you know if that was solved, or if your component somehow, has any,
Let's say, change that picture, or is it still kind of just a receiver separated from that problem?
**Andrew Wilkins @ Elastic Observability** 06:55 So it's still a relevant problem.
Let me just step back a sec. They're trying to solve different problems, so the Lambda layer, the Lambda extension, is all about recei… tell me if I'm off here, since you worked on it, but my understanding is the Lambda extension is there for receiving telemetry from applications that are running as a Lambda.
Whereas what we've built here is for receiving data from AWS services, so they're not… they're not producing OTLP or anything.
That, I mean, there's a… there's a bit of a subtle distinction. The… the… where it matters is that, or, sorry, where it differs is that AWS services typically produce data in bulk to S3, or to CloudWatch, or whatever, and so…
when we're running with this receiver, we do… we do enable synchronous exporting, so we have wait for… wait for result true on the sending queue.
And so, we'll receive a batch of data from S3, or a batch of data from CloudWatch, and then just export it, wait for it, and then respond, and that way we've got durability all the way through.
But it's… it's a bit different, because in the… in the Lambda extension case, you're going to be receiving small amounts of data, and so we… we don't have the same behavior.
**Paulo Janotti** 08:19 Okay, so,
But in the end, the idea is for this receiver to be also in the layer, or in the collector layer that they create.
**Andrew Wilkins @ Elastic Observability** 08:30 I don't think it makes sense to combine them, just because they're solving different issues, but, I guess…
It could be. I would probably be inclined to have a separate thing altogether, maybe a separate extension, sorry, separate layer.
**Paulo Janotti** 08:47 So, perhaps a different question. If I have my Lambda, I own the instrumentation, but I want also the data that you… your receiver collects.
How should be the setup?
**Andrew Wilkins @ Elastic Observability** 09:00 Sorry, Seth, could you repeat the question?
**Paulo Janotti** 09:04 So, I'm instrumenting my lambdas.
Java.NET, Python, I'm instrumental, I want to collect that.
But I also wanted this, richer data. I'm almost seeing, like, an infrastructure data.
**Andrew Wilkins @ Elastic Observability** 09:25 Yo.
**Paulo Janotti** 09:26 That your receiver is collecting. So, how you envision the setup for that scenario?
**Andrew Wilkins @ Elastic Observability** 09:32 Gotcha, okay. So, I would have them as totally separate lambdas. So, in your application case, you wouldn't… I don't think it would be a good outcome if you combine them, because you're going to have…
the, like, the scale of all the AWS services affecting the scale of your application lambda. So if you, if you have your
whatever, your application is running in Lambda, you add the hotel Lambda
layer to it as an extension, and that is how you'll get your OTLP out to your destination.
off to the side, you'll have a totally separate Lambda function, which will just be subscribing to CloudWatch.
you might want to have a separate one for S3, but you can combine them. Actually, no, that's not true.
No, sorry, let me back up. You have a separate lambda per…
per data source, effectively. So your data source might be your application, and in that case, the Lambda layer is combined with your application.
For AWS services, you'll have one per data source, so you might have one for VPC flow logs, you might have one for CloudWatch logs.
one for web application firewall, and so on. Each of them will scale according to the throughput for that particular data source, and each of them will be configured for a particular S3 bucket, or whatever. So you can configure them to have the right
Encoding extension and the right, you might want to send them to different destinations or whatever.
**Paulo Janotti** 11:12 So, so, just to, to, to kind of illustrate, suppose that I'm…
I'm writing these funds as logs. I could use, then, your receiver to collect via CloudWatch.
**Andrew Wilkins @ Elastic Observability** 11:26 Yes.
Yes, exactly. So you would… you would have, a CloudWatch log subscription filter, I think it's called, and you have that trigger… trigger this… this new Lambda receiver.
**Paulo Janotti** 11:38 I see, I see. So… so they are really, yeah, they are kind of…
orthogonal, I think they… they help each other if you want to kind of… perhaps some group has the application already instrument that is already collecting, and you don't want to touch that.
But you also wanted to start to collect some of this other data that comes from AWS, then they go to the new receiver and implement that data, yeah.
**Andrew Wilkins @ Elastic Observability** 12:07 I like the way you put it, with the infrastructure logs, basically, for…
**Paulo Janotti** 12:11 Yeah, and you can have the correlation, right? If you have context of things, you can have correlation. Okay, interesting, interesting. I… I've not worked with that, so I'm really, just going for memory from 4.
5 years ago, but sounds interesting, sounds… sounds like cover a kind of a gap in the… in the monitoring of lambdas, and also…
Yeah
I can… I can give an eyeball review, but I'm really not on top of the things in Lambda, so I'm not the best person to do that.
**Andrew Wilkins @ Elastic Observability** 12:52 No, that's fine. I appreciate the discussion. We are looking for a sponsor, but if you don't feel like you have enough context for that, that's okay.
It has also been raised that… sorry, like, my team is working on it, apparently it's okay if…
if I approve it, sorry, if I sponsor it, but I was hoping that we would get some… someone outside of Elastic to… to buy in.
But I'll… I'll discuss a little bit more with Sean's Slack as well, because he had some questions, and then figure out where to go from there.
I guess… thanks. Thanks, Paulo. I've got the next… next one as well. I don't know if, Paulo, you have any…
thoughts on this one. So, we are running Hotel Collector as a
in a multi-tenant setup at Elastic.
On behalf of our customers, so we…
We expose an OTel collector deployment to our customers.
receive data, do processing, get it to Elasticsearch clusters, and each Elasticsearch cluster is single-tenant. But on the… in the middle, we have this multi-tenant service, and this presents some interesting challenges, like we have to do context propagation to get…
The right tenant header, have to get, have to…
do multi-tenant authentication, and so on. So there's all sorts of issues here, that we need to solve. And, recently we had a, an incident that was caused by a bug in OTL Collector Core, where there was a,
memory pooling issue in the Z standard compressor.
That was… it was all solved, but it really highlighted a bit of a…
lack of testing, I would say, for this kind of… these kinds of setups.
It seems that not many people are doing this, but I wanted to…
I guess this is a bit of a small group here, but I wanted to ask if, if anyone is interested in working on this. Paula, do you have, are you doing anything similar? And do you have any interest in this? No. Okay.
**Paulo Janotti** 15:08 So…
**Andrew Wilkins @ Elastic Observability** 15:09 Alright.
**Paulo Janotti** 15:09 I…
I'll be curious if you can put in the dark later the original bug and the fix. I would like to take a look, because…
I think there is a lot of subtle things for… but, when people use the sink pool, especially, I don't know if it is involved with the sink pool.
But, there is… there are very subtle things with ownership when you…
So, sometimes you have to wrap the thing that you want to put in the pool to have some communication to say, hey, now it's safe, because people run the benchmark on their machine. Oh, great, great improvement. And then,
When you really get concurrence, then this kind of very hard bug pops up, like,
you couldn't have returned the thing to the pool yet, you know? Yeah.
**Andrew Wilkins @ Elastic Observability** 16:13 I think in this case, it was a case of double… it was like a double free, where it had… had two things that put it back into the… into the pool, but I'll find the issue, and I'll… I'll add it to the agenda after.
Yeah, I guess what I was… so we have our own testing framework, which runs the collector in a…
you know, with multiple virtual tenants, and make sure that no data crosses over and whatnot. What I'm going for here is
It would be great if we pushed some of that, not… not…
duplicate some of that in Otel Collector, so we catch these kinds of issues earlier. I think it could be beneficial to others, but I'm not sure if anyone else is doing this, so maybe it's not worth it.
I'll raise it on the Slack channel again, and see if anyone cares.
I don't know what this last one is… this might be… a PSA…
Do you know what the third agenda item is, Paulo?
**Paulo Janotti** 17:25 Sorry?
**Andrew Wilkins @ Elastic Observability** 17:26 There's another agenda item with Alex's name next to it, but I don't know what this is about.
**Paulo Janotti** 17:32 No.
**Andrew Wilkins @ Elastic Observability** 17:46 Mmm… Okay, I don't… I don't know what… so I won't cover that.
**Paulo Janotti** 17:52 I've been in the meetings of the stability group, So,
The, the, the message is, is well summarized there on the issue that, basically,
Having a distribution that should satisfy, kind of, 80% of what people want.
With just stable components.
And, kind of, I think this is the main message, you know, so this is what…
This work for its abilities, kind of, looking for
I think there is, there is a bunch of work, because
In a sense, people have a very good idea of which components they think should be.
But I think in the end, for this to work, we have to have a kind of criteria first on the paper, instead of the components themselves, you know?
**Andrew Wilkins @ Elastic Observability** 19:06 Yep, makes sense.
I don't have anything else.
Rob, did you have anything to propose?
**Rob Bavey** 19:20 No, I'm here, I'm just here to listen today, just to show my face and listen and get more, you know, just say hi to everyone.
**Paulo Janotti** 19:30 I'm just giving a quick update,
about Windows ARM, I don't know who's interested on that. For us, eventually, because we have a bunch of,
Customers that run the collector on Windows clients.
And Windows Client ARM is kind of…
going relatively fast. So, we… I… I talked with Douglas Kamata, and he works on the release, and he's gonna be, preparing for us to have our Windows installer for ARM.
And, I hope by… At most, by the beginning of the year, we declare our…
Tier 2 support for Windows Arm.
**Andrew Wilkins @ Elastic Observability** 20:23 Cool, sounds good. I don't know… I think it will be relevant for us if it's not already.
Are there any other areas that need help?
**Paulo Janotti** 20:33 Fortunately, the part has been, mostly identified the things that can't, that aren't supported and are very few. So, basically, most of the things work out of the box, one or other exception, you know.
**Andrew Wilkins @ Elastic Observability** 20:53 Who?
**Paulo Janotti** 20:54 And they are all fixed it, so we…
**Andrew Wilkins @ Elastic Observability** 20:58 Thank you.
Alright, I guess, we can leave it at that, then. I don't have anything else.
Right.
Have a nice evening.
See you later.
**Rob Bavey** 21:13 You too, cheers.
**Paulo Janotti** 21:14 Bye.
**Rob Bavey** 21:15 Better.
