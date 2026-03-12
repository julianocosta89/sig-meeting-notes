SIG: Prometheus WG
Date: 2025-10-08
Duration: 64 minutes
============================================================

## Zoom Recording Transcript

Arthur Silva Sens 00:04:31 Hello.
Jonathan 00:04:35 Hello?
Owen Williams (he/she) 00:04:37 8.
Arthur Silva Sens 00:05:00 I have a feeling we won't have too many people today.
And maybe… Maybe we start with the… David's point?
Not sure if you saw the message David sent on Slack channel. David… I think David recently joined the technical committee of OpenTelemetry?
Which is great, For us, actually, to be honest.
Because the technical committee… makes… Like, he's, like, the tech lead of OpenTelemetry?
And having someone that understands Prometheus very well will help us make OpenTelemetry and Prometheus Bye.
going in the same direction, I guess. But the problem is that This tech… the technical committee meetings.
happens in the same time of Oracle.
So that means that if we keep the same time, David won't be able to join the Prometus SIG meetings.
I saw that Jonatha created… created a…
Jonathan 00:06:29 when to meet Link, Can you confirm if this… if this works?
Hold on, maybe share yours.
Arthur Silva Sens 00:06:43 Yeah, I can share my screen.
But how do I do that?
Oh, sure.
Jonathan 00:06:55 Does this.
Arthur Silva Sens 00:06:56 what I'm supposed to see?
Jonathan 00:06:59 I think that you don't need to log… to do a login… to sign in.
I think that you'd… Just need to select when you are available on the right.
Arno.
Arthur Silva Sens 00:07:16 So I just put my name, and I select… My time's descended.
Hey.
Arv, Owen, when you have the time, could you fill in this link? Actually, let me add it to the meeting notes.
Jonathan 00:07:38 Maybe we can send an email for everyone that participated on this call in the past, I don't know, 3 months?
Arthur Silva Sens 00:07:49 I'm gonna personally… I'm gonna send DMs to everybody.
Jonathan 00:07:55 Okay.
Arthur Silva Sens 00:08:35 I'm moving this… Yeah.
Owen Williams (he/she) 00:08:42 Is this in UTC?
Jonathan 00:08:48 UTC here.
Owen Williams (he/she) 00:08:49 Okay.
Arthur Silva Sens 00:08:55 Why is it only 9AM to 6pm?
Jonathan 00:08:59 I assume it's right.
Owen Williams (he/she) 00:09:00 viewers.
Jonathan 00:09:03 Yeah, I said just, I assume that you're just available in working hours.
Would you like to… And more, more times.
Arthur Silva Sens 00:09:14 I… people will naturally just choose working hours, so we… I don't think we need to limit But yeah, I guess, I guess it's fine.
Who else do I need to send this to?
Remember Yurai?
Jonathan 00:09:40 Other people could…
Arthur Silva Sens 00:09:43 Yeah, okay, Cryo… Carrie Edwards? Probably not.
Owen Williams (he/she) 00:09:52 Yeah, she's on patern- parental leave for a while.
Arthur Silva Sens 00:09:57 Cyriola Clark?
Owen Williams (he/she) 00:10:03 I don't know.
I mean, he… I don't think he's ever joined this.
Arthur Silva Sens 00:10:07 He joined us a few times, at least twice.
Fuck.
Cryo… there is a guy called Kyle, Kyle Eckerd, I think?
And then… Anthony Mirabella, who I have never seen.
But he's a co-owner.
There's a birdie… Who is also co-owner.
that I've never seen here.
I'm gonna take a look at this later.
Arve Knudsen 00:10:48 What's the time zone of when to meet? Is it a local time zone?
Arthur Silva Sens 00:10:54 It is OTC.
Arve Knudsen 00:10:55 It's you to say okay.
I see.
Arthur Silva Sens 00:11:07 Okay, I'll take a look at this whole meeting notes, look at whoever joined, and I'll start sending that.
To everybody.
Okay, next topic, I'm mentoring… Someone called Anna.
And she is doing UX research and UI design.
And, her goal is to brainstorm ideas that Enables two concepts.
Those concepts are called navigation and telescoping. This is documented in Hotel website.
And… yeah, she's not technical, she… she doesn't understand observability, how she's learning, but she doesn't know much.
So she needs help. She needs people who uses Prometheus, uses OpenTelemetry.
And… Yeah, the idea is… I don't know, create a new UI or change the existing UI of Prometheus to enable navigation telescopy.
We are probably doing that I don't know, in 3 weeks, or next month?
But we need participants.
So if you'd… if you'd like to join.
send me a DM, I'm going to organize the session.
And if you've… I don't know, if you have people… if you know people that would like to join as well, please let me know.
Jonathan 00:12:57 It's just for the ones that know something about design, or…
Arthur Silva Sens 00:13:01 No, it's, it's for devs. She is the designer.
And we need… we need people who understand Prometus and OpenTelemetry. That's it.
Okay. You will… we… when it works, we… first we need to find people, and then we will make something that works for everybody. So we don't have a date yet.
Jonathan 00:13:27 So, I would like to participate, just to… True.
Arthur Silva Sens 00:13:30 Awesome.
How about Arv, Owen? Interest? It's okay to say no.
Arve Knudsen 00:13:43 Yeah, I don't… I don't think, I'm going to join, sorry.
Arthur Silva Sens 00:13:48 No problems.
How do you feel, Owen?
Owen Williams (he/she) 00:13:57 Yeah, I don't… I don't… Yeah, I don't think it's a good time for me to take on new things right at the moment.
Arthur Silva Sens 00:14:04 Alright.
I need at least 5 people. Do you have any ideas how can I find Alright.
Owen Williams (he/she) 00:14:29 What's the timeframe for this?
Arthur Silva Sens 00:14:32 Oh, we… we need to… to have this brainstorm session, and then let Anna work on creating wireframes until end of November.
So I think the interviews will be, like.
end of October or beginning of November, and then she has 3 weeks to create the wireframes.
Owen Williams (he/she) 00:15:02 Yeah, I'm just… I'm… Looking at 3 weeks of work, travel, and conferences, so it's just like… I'm just gonna be slammed with… Making sure I'm doing all that. Yeah, the timing isn't great.
Arthur Silva Sens 00:15:17 No worries, like, if you really… Like, we would rather have people who are really engaged than somebody who feels obligated to be there.
Oh, it's totally okay if you don't have the time.
Okay.
I'm probably gonna send a message in the hotel Prometheus channel.
I don't know. If you have any ideas on how to recruit more people, I would love to hear that.
Jonathan, next topic's yours.
Jonathan 00:15:59 Yeah, I think that we can use the rest of this time to discuss that… that PR.
Reschedule a meeting in the past week, but… What do you think?
Arthur Silva Sens 00:16:15 Okay, I didn't prepare at all, but I guess that works?
Jonathan 00:16:19 Or we can find another time for that.
Arthur Silva Sens 00:16:25 I have the same problem as Owen. Next week, I'm traveling, I'm coming back only end of October.
Jonathan 00:16:33 So I don't think we'll be able to schedule anything.
Okay, so… Let's try to discuss it on async?
Arthur Silva Sens 00:16:45 No, we can use the time now, but… Rf Owen.
There is a bug, and it permissive remote ride receiver.
It's nasty. There's a lot of… there's… we suspect there is a concurrency issue.
So we would appreciate some special, like, people who really knows their stuff.
But I don't think that's what you… you two signed up when joining the meeting.
If you wanna stay, That would be nice, if you have… if you need the time for other things, I want to be respectful… respectful of your time, too.
Arve Knudsen 00:17:26 I could stay for the length of the meeting, like, I, I mean, I… I don't really have expertise on the auto collector.
I have to say.
Arthur Silva Sens 00:17:39 Cool.
Oh, and do you wanna leave, or do you wanna stay?
Owen Williams (he/she) 00:17:44 No, I could stick around for now. Depends how much the dogs who have not had a walk today get antsy. For now, they're being nice and quiet, so… Yeah.
This is not code I'm familiar with, so I am, yeah, just reading it for the first time.
But I'll, I'll take… Yep.
Arthur Silva Sens 00:18:05 Just so, context. We are working on Prometus Remote Write Receiver.
So it's a component that receives remote write, and then translates it to OTLP.
And people are reporting.
That when a remote write request comes in.
They are able to process the first request.
But all the following requests are discarded, there's no logs, there's nothing.
The data just disappears.
I think they gave us a reproducer.
Here… If we just ran the docker compose, they see… Let me go through this config.
this config is scraping Prometus itself.
And there is a relabeling config to keep only one metric.
Go to see he belongs bytes.
This is being kept, and all the other metrics are being discarded.
And this is being sent to the collector through the remote write V2.
And then the collector config, Has only the remote ride.
Receiver component, and there is… it is… exporting to debug. Debug is just logging the metrics and not doing anything.
Should I run this?
I don't know.
That's not red.
So I… I… while I was investigating, I was able to… To write a test.
That reproduces the issue?
So, when we receive concurrent of remote write requests.
I guess I would just run this…
Jonathan 00:20:22 The test, or the container test?
Arthur Silva Sens 00:20:24 The task, the assess, yeah.
So, we are receiving 5… We are building remote write requests here. Can you read this? This is readable to you?
Okay, we're creating, 5 remote write requests. All of the requests have the same metric, And then we are sending… we're spinning up different go routines that sends this request to the collector.
So if we receive 5 remote write requests, that means we should be seeing 5 OTLP.
Messages afterwards?
And so, we are logging a lot of stuff here.
I can see that I have… I've received 5, remote write requests.
The first one… After the translations, there are zero resource metrics, zero data points.
Second one, the same. The third message… Then we have one resource metric, and the single resource metric has five, Data points, or 5 samples.
Jonathan 00:22:53 Anya?
Arthur Silva Sens 00:22:54 All the rest are different. If I run this again.
Owen Williams (he/she) 00:22:58 Wait, so…
Arthur Silva Sens 00:22:59 Probably s…
Owen Williams (he/she) 00:23:00 They're… it's not all the same metric name. The metric name is different for each one, right?
Arthur Silva Sens 00:23:06 Yeah, let's see… There's a metric name here.
And when you… The metric name should be… Okay, so…
Owen Williams (he/she) 00:23:17 It's got an… yeah, it's got an incrementer, so all… so the metric names are different.
Arthur Silva Sens 00:23:21 Okay, yeah.
Good call, good find.
But, like, they are separate remote write requests, so they should be translated to separate OTLP messages, right?
Owen Williams (he/she) 00:23:42 Well, it looks like they're getting batched up.
Arthur Silva Sens 00:23:45 Yes.
So if I run this again…
Owen Williams (he/she) 00:23:49 Sorry, I thought the bug was gonna be that some of the metrics didn't get received, but it looks like they're all getting received. Is it just weird the batching isn't even?
Arthur Silva Sens 00:24:00 Yeah, I heard… now I run it again, now I have… four data points in the first one, and I have one separate in the fourth… If I run this again… Oh, now it passed.
Owen Williams (he/she) 00:24:17 So, okay, so it's, you're… Sending… You're HTTP posting them concurrently.
Yes. So is then the concept that… each individual post should be a separate batch? Is that what the…
Arthur Silva Sens 00:24:43 Yeah, it should be translated to different OTLP messages, but somehow they are getting grouped together.
And sometimes they're split, sometimes they're… yeah, they're grouped.
Owen Williams (he/she) 00:24:56 I mean, is, well, first of all, this is V2, and isn't V2 not done?
Arthur Silva Sens 00:25:04 What do you mean?
Owen Williams (he/she) 00:25:05 Remotewrite V2.
is incomplete.
In the hotel.
Arthur Silva Sens 00:25:10 the… It is. Actually, we… we promoted that to Alpha.
So people should be using that. And the first feedback we received was, this is completely useless because it's not working because of the.
Owen Williams (he/she) 00:25:27 Okay, so this is… this is… it's… yeah, so if you used V1, it would probably just work as expected, but it's just… it's a V2 bug.
Arthur Silva Sens 00:25:34 No, because there is no V1 receiver, only V2.
Owen Williams (he/she) 00:25:40 Receiver, okay.
Okay, so the question is, is there some sort of buffering happening in the receiver where it's seeing multiple messages and it's just sort of bundling them up?
Arthur Silva Sens 00:25:55 Yeah.
I… Jonathan and I, we already did an investigation. I think we found the root cause.
But we have no idea how to fix it.
That makes… Get this out.
So there is a cache.
We've implemented a cache for resource attributes.
Let me find it… So… A resource… resource… Resource attributes comes from target info metrics, right?
So, if… if somebody sends a remote write request, And sends a message.
like, in Prometheus, the way Prometheus is implemented, like, different metrics are sent separately.
And then… Let's say we have a goal GC logs bytes metric.
And then afterwards, we receive a target info metric.
Or the other way around. First, we receive the target infometric, and after we receive the go GC log bytes.
The labels from the target info should be translated to resource attributes.
and the go GCLOX bytes, if it has the same job and instance label as the previous target info.
then with those match, and we should be taking the labels from target info, and adding as resource attributes of CodeGC log bytes.
So for that, we implemented a cache.
That if the metric name is target info, instead of creating a metric, we create a resource attribute.
And we keep this resource attribute at the cache.
Afterward, when we receive a real metric, we look at the cache, see if the job and instance label… the job and instance labels match, and we take the results metrics from the cache.
The problem here is, I think, resource metrics, the way it's implemented in OTL, P metrics?
whatever this… Package.
Yeah, Pimetric… package.
This is, pointers.
this is the interface, I don't know what that I have. Honestly, I don't know Go enough to tell.
That if we… histor… As it is, It keeps a pointer.
And when we were receiving multiple… Requests at the same time, we are… We are changing the message inside a pointer, and then it gets, like, gets messy.
I honestly don't know how to solve this. I… I can see… us changing this cache to use, mutexes?
So, we cannot change the pointer?
At the same time, but that makes things very, very slow.
Owen Williams (he/she) 00:29:08 So.
Arthur Silva Sens 00:29:09 we could…
Owen Williams (he/she) 00:29:09 Sorry, I'm just… I'm just trying to understand. So, You're saying that you're updating values in the resource metrics, but because the thing you're caching is a pointer, you're clobbering the other ones.
Arthur Silva Sens 00:29:23 Yes.
Owen Williams (he/she) 00:29:24 Yeah.
Okay.
Arthur Silva Sens 00:29:30 Got it. This is… this is, filling. Like, this is the only thing that makes some sense to us.
But, yeah. Since we cannot fix it, we couldn't find a way to fix it, I don't guarantee that this is the problem.
Owen Williams (he/she) 00:29:59 Yeah, adding the resource.
Arthur Silva Sens 00:30:01 Oh, this guy here?
Owen Williams (he/she) 00:30:02 Okay.
Arthur Silva Sens 00:30:04 he's trying.
Owen Williams (he/she) 00:30:04 I mean… Yeah.
Arthur Silva Sens 00:30:08 He's trying to solve… He's using a defense?
Jonathan 00:30:11 a different structure, like BigComo Map, And, in the text.
Arthur Silva Sens 00:30:19 Yeah, that makes sense, because resource… he, instead of, caching resource metrics, he's caching only the attributes. That makes sense.
but this is what I'm not liking.
I… If we use a mute tax.
that's gonna serialize all the requests. So if… if a receiver receives 1 million.
remote write requests, we'll process one by one instead of parallelizing everything.
Does that make sense? Like, that… Do you feel like…
Owen Williams (he/she) 00:31:04 Yeah, yeah.
Arthur Silva Sens 00:31:04 MuteTax is a… is a… is a valid way to solve it, or should we be changing that?
Owen Williams (he/she) 00:31:13 I mean, I could… the other… other thing you can do is… You know, do a deep copy when you're extracting from… like… No, I think, I think, yeah, yeah, it doesn't, yeah, it doesn't make sense to cache pointers. You want to cache data, that's for sure.
Or, it's fine to cache pointers as long as, if you need to modify it, that you're making a copy of the underlying data instead of mutating the data.
Pointer… the… yeah, instead of mutating the pointer, which… Yeah.
Jonathan 00:31:56 Like, before save it into the cache, do a deep copy of the object, deal with that, and after that…
Arthur Silva Sens 00:32:04 No, because a deep copy will be a pointer again, right?
Jonathan 00:32:09 Oh.
Owen Williams (he/she) 00:32:10 Well, yeah, yeah, you don't… yeah, you wanna, you have to…
Jonathan 00:32:16 No.
Owen Williams (he/she) 00:32:17 The, okay, as, as for the, as for storing the map, the attribute map.
I forget, in Go… Are you allowed to concurrently read from a map?
I forget what the… I know you're not allowed to write concurrently, but the question is, if it's read-only, can you get away without the mutex?
Arthur Silva Sens 00:32:48 Yeah, I think it's okay.
Arve Knudsen 00:32:50 Oh, sorry, RF… I was just saying that, I mean, concurrent readers of a map shouldn't be a problem. I mean… I don't see how that would be an issue, right, Owen?
Owen Williams (he/she) 00:33:03 So… Yeah, as long as there's no writes occurring, then reads are fine.
Arve Knudsen 00:33:10 Yeah, I mean, that's also why you can use, you can take a read lock.
Because, so long as only, there are only readers, taking the lock, you can have as many as you wish. It's the same principle.
Owen Williams (he/she) 00:33:27 So I think, yeah, I think in general, it also makes sense to just cache the data you want to cache, so this PMAP, I think that makes sense.
Since that's the only thing that's needed. And then… Yeah, as long… You only… and then you only need to… you have a rewrite mutex, and you only need to care about… If it's grabbed for rights, then you can't have any other routine reading from it, but once the As long as the writes aren't occurring, then you can read as much as you want.
Does that make sense?
Arthur Silva Sens 00:34:07 Yeah, yeah, it does.
How are you feeling, Jonathan? Does that make sense to you?
Jonathan 00:34:17 The necessity to use the mutex also exists.
Oh, already exists.
Arthur Silva Sens 00:34:27 Let's see where…
Jonathan 00:34:28 So we need to use, we need to use, we must use NewTexas.
Owen Williams (he/she) 00:34:33 But the… and then the mutex only needs to be around the… the right… Correct. To be… Correct.
Yeah.
So right now, the cashmutex is around the whole, all of the… logic. And this could be reduced to, I think, just the put stir.
Wow.
No, you really… So these PMAPs will need to be different, right? So it's… it's gonna be… No, it shouldn't be…
Arthur Silva Sens 00:35:12 Right to the sketch.
Owen Williams (he/she) 00:35:13 Just a second.
Huh?
Arthur Silva Sens 00:35:15 I'm trying to figure out when do we write to the cache.
It's when we don't…
Owen Williams (he/she) 00:35:25 It's the armcache.add. It's… right now, in the existing code, it's at, like, 284, 281, it looks like.
Down a bit.
Arve Knudsen 00:35:41 And, yeah, can't you change to only take a right lock when you actually insert into RM cache?
when you… when you read from ARM cache, a read log should be enough.
I'm just done.
Arthur Silva Sens 00:35:58 So, okay, okay, okay, okay, I got it, got it.
Arve Knudsen 00:36:01 Reading the code quickly here.
Owen Williams (he/she) 00:36:02 But wait, caches should be thread safe.
Jonathan 00:36:08 Yeah, this library that I'm using is ThreadSafe.
Owen Williams (he/she) 00:36:11 Okay, so, you don't need a lock, so when you write in… yeah, so the problem is, Yeah, why do you… why do you need a mutex at all? I don't think you need a mutex at all, because…
Arve Knudsen 00:36:23 That's true.
Owen Williams (he/she) 00:36:24 you… If you're writing to the cache, you create… let's say you start with a new thing, it's a new object, you insert into the cache. Definitely no concurrency there.
If you find some… so the idea is you can find something in the cache, and then you need to update it, and then you write it back to the cache? Is that sort of the operation?
Arthur Silva Sens 00:36:46 I think this is the… the problem.
Like, resort… since we're caching resource metrics, resource metrics is a very… complex and complete.
Owen Williams (he/she) 00:36:55 Right, so we're starting with the… just working on the maps, so just these attributes, so…
Arthur Silva Sens 00:37:02 Yeah, if we're only using the map, if we're only caching the attributes, we are not caching the metrics inside the resource metrics, so they don't mess around with each other.
Owen Williams (he/she) 00:37:12 Yeah.
Arthur Silva Sens 00:37:14 I feel like we don't need the mutex.
Owen Williams (he/she) 00:37:16 I… I think I agree, because… Because there's no operation where you're mutating data. You're not mutating… you're not mutating…
Arthur Silva Sens 00:37:30 dudes.
Owen Williams (he/she) 00:37:30 existing map, because the whole point… as long as you… as long as you make sure that when you… okay, when you extract one of these maps from the cache.
You want to make sure you're duplicating it.
Yeah, you want to make sure you're only duplicating the map, then mutating it, and then adding that new object to the cache. So that should be… safe, and so then, therefore, okay, if I have loaded the map from the cache, and then I'm reading it, that's fine, because nobody's going to be writing to that map, because the whole point is the cache is not mutated. You're only adding new objects to the cache, you're never mutating any object in the cache. So you just, yeah, you definitely want to make sure you're not… that you make a deep copy of the thing you extract from the cache.
Before mutating it. And then you shouldn't need any mutix.
Arthur Silva Sens 00:38:31 Jonathan, how… how much of this you didn't understand?
Jonathan 00:38:39 Dutch… Instead of use resource metrics, we can use the Big Formal map.
And…
Arthur Silva Sens 00:38:47 You didn't understand that.
Jonathan 00:38:49 No, I understand that. I understand that you need to do that, and before save.
new element in the cache. We need to do a copy of that.
And validative doing that, the test will pass.
Without you.
Arthur Silva Sens 00:39:06 I think we don't need to copy before adding, we need to copy after retrieving.
So we don't mess around with whatever we have on the cache.
Owen Williams (he/she) 00:39:21 I think you're saying the same things.
Jonathan 00:39:24 Totally.
Arve Knudsen 00:39:28 I think I'm also seeing now, that the cache mutix is unnecessary, because, it protect… it protects an LRU cache, which is actually thread safe.
Arthur Silva Sens 00:39:39 Yeah.
I think the main problems here, like, this is the main fix. This is the fix, actually. All the mess around with the cache is… It's just… I think that's right. Making things more complicated, yeah.
Owen Williams (he/she) 00:39:52 So the thing, yeah, the thing I'd want to see in the PR is just to make sure that when you load something from the cache, because a map itself is a pointer.
You need to duplicate that map before… Editing it.
Jonathan 00:40:07 Oh.
Okay.
Arthur Silva Sens 00:40:09 But we don't… like, this… Actually, this is not a problem, like, this was a problem before with resource metrics, because resource metrics has attributes and has the metrics itself, so we are changing resource metrics because we are adding the sample as a metric.
But on the map, This is separate from the metrics.
So we don't need to change the attributes. We are gonna read this from the cache, and we are never gonna opiate this map. We are not writing to this.
Owen Williams (he/she) 00:40:42 Well then, what's your… Wait, okay, so you're gonna…
Arthur Silva Sens 00:40:50 Let's go through the code.
Owen Williams (he/she) 00:40:52 Yeah, yeah, yeah.
Arthur Silva Sens 00:40:58 We gotta resort.
Owen Williams (he/she) 00:41:00 Yeah, it's just a… wait, okay, sorry, go ahead.
Arthur Silva Sens 00:41:03 We're getting a resource method. This is… it's not the PR, right? This is main.
Owen Williams (he/she) 00:41:07 Yeah.
Arthur Silva Sens 00:41:09 We get the resource metrics.
We… if we fi… if we find the resource metric in the cache.
we get the… we, like, RM becomes the one that we got from the cache. If it's not… We created a new one.
Well, this is the attributes.
Owen Williams (he/she) 00:41:27 Yeah.
Arthur Silva Sens 00:41:28 the thing that… this is the common map.
Then we parse some labels, we add this RM to the cache, We continue.
Owen Williams (he/she) 00:41:42 But, okay, so what I'm look… what I'm looking at is the put stir.
You're doing something to the attributes on 281.
Arthur Silva Sens 00:41:53 Yeah, we are adding the job and instance labels.
as… Like, if it's not the job at NASIS label, we are adding those labels as attributes.
For example, service.name, service instance ID, or if it's a Postgres thing, the postgresdb.name, there's resource attributes from the metric.
From the target infometric.
Owen Williams (he/she) 00:42:21 So isn't that… A mutation of the thing you got out of the cache.
Arthur Silva Sens 00:42:26 No, because… Okay, wait, maybe that it is… It is. Good point.
Owen Williams (he/she) 00:42:38 Yeah, okay.
But that's okay, then you just… you make your deep copy first, then you can do your modification and nothing, and you still don't need a… you still don't need a mutex.
Arthur Silva Sens 00:42:50 So, should be something… like, this… It doesn't exist, but we can implement that.
Owen Williams (he/she) 00:42:58 Yeah, exactly.
And in this case, you'll be deep copying the attributes, so it'll be ATTRs, yeah.
Arthur Silva Sens 00:43:10 Wait.
I think… There is a… Overriding the destination. So we do, like.
Is he said, I am.
Up to… yeah, this is… Copy2 copies all property from the current instruct, overriding the destination. The destination is… here.
So, we are creating a new resource matrix, and we are deep copying this… here.
How do I… how do I remove the… go cash.
I wanna run this… But if it's… Okay, the, didn't fix.
Okay.
Arve Knudsen 00:44:23 Are the tests now supposed to catch data races? Because I tried just removing the cache locally, and I ran the tests with race detection, and there were no data races. Everything worked, just for reference.
Arthur Silva Sens 00:44:45 No, I don't think this is… Adding the race.
Arve Knudsen 00:44:50 No, but I did it myself. Like, I, I ran the tests with race detection.
Explicitly.
Owen Williams (he/she) 00:45:01 So, also…
Arthur Silva Sens 00:45:03 And it succeeded.
Arve Knudsen 00:45:04 Yes.
Owen Williams (he/she) 00:45:06 Attributes also has a copy to function, so I think, I mean, I think it's a good idea to only cache what you're actually using anyway, just to save memory. And then you can use attributes.copyTo to do the same.
The same thing.
Arthur Silva Sens 00:45:27 Hey.
Super weird that the race flag doesn't catch that other races.
Owen Williams (he/she) 00:45:36 Well, there's no data race, you're clobbering.
There's no… a race would be two things editing the same data at the same… you're editing data while you're trying to read it. But this isn't a data race, this is just clobbering. You're just overwriting… data that you didn't want to. So, it's correctly concurrently reading the data that you have Clobber.
Arthur Silva Sens 00:46:01 So it's not a race.
Arve Knudsen 00:46:03 But the club ring will be caught, by the tests, right?
Owen Williams (he/she) 00:46:09 the… Yeah, the tests should catch it, but the race to.
Arthur Silva Sens 00:46:14 Dammit.
Owen Williams (he/she) 00:46:14 So the point is, you can make your… take this PR, take out the mutexes, run it with the race detector, and that will tell you. And, I mean, you should have more iterations, probably, to really hammer it, but, like, yeah, that'll tell you if you've got… If you've got a race problem.
Because the PR fixes the clobber problem.
Arthur Silva Sens 00:46:38 Marv, did you… did you add this test to your code?
Arve Knudsen 00:46:42 I'm…
Arthur Silva Sens 00:46:43 It doesn't exist.
Arve Knudsen 00:46:44 I'm using the… I'm using the… the branch from the PR.
Arthur Silva Sens 00:46:49 So I just modified the PR to not have the mutex.
Arve Knudsen 00:46:54 And then I wanted to see if the mutex actually prevents any erases, and… And without the mutex, no races were detected.
Interesting. I also could not… I also could not see myself in a… in a use… in a need for the mutex. And, and after Owen's suggestion to… to… to kind of repeat the tests, I… I… I ran with a test count of 100.
And the race detection, and there were still no racist calls.
Arthur Silva Sens 00:47:27 Interesting.
Owen Williams (he/she) 00:47:28 And the test passes?
Arve Knudsen 00:47:30 Yes. Like, all I did was remove the mutex. Everything passes.
Owen Williams (he/she) 00:47:35 Great.
Arve Knudsen 00:47:35 Yeah.
So… If the.
Arthur Silva Sens 00:47:40 I guess the…
Arve Knudsen 00:47:40 to… if the tests are sufficient, I don't see any races, I don't see the mutex protecting from any races.
Arthur Silva Sens 00:47:50 So, effectively, this is the fix.
This fixed the problem, and this is just adding complexity.
Arve Knudsen 00:48:00 It could look that way, because it looks like it protects the cache, which is already thread-safe.
So, if the mutex were to be necessary, it would have to be… because it would protect what's in the cache.
I personally, I personally didn't see, that… any need of that, I mean, but I could be missing something.
Arthur Silva Sens 00:48:25 Right?
Jonathan 00:48:26 And RV, RV, you are not… you're not using the deep copy function, right?
Arve Knudsen 00:48:33 I did not. I kept original PR, except I removed the mutex. That's the one thing I did. I just removed the mutex.
Owen Williams (he/she) 00:48:43 I think there's still a problem with the PR, If you look at more line 270 or so, So, like, so in the case where… so I do see the copy, too, for cached attribute, that's good, but… 271, it's taking the existing RM.
And then… 283, it takes the attributes of that.
And then… 288, it's still mutating that.
So I think you still need to create an empty… if the thing is existing, I think 271, you have to do that… you have to create an empty one and do a copy 2.
So it's weird that the test isn't… that might be a different bug.
But yeah, I think you still need to make sure that everything pulling out of the, cache is being mutated.
Yeah, well, sorry.
Arve Knudsen 00:49:52 It has to be.
Owen Williams (he/she) 00:49:53 Copied if you're going to mutate it.
Arve Knudsen 00:49:55 It's also possible the tests are not sufficient, I'm not sure, like, I… of the insight yet.
Owen Williams (he/she) 00:50:00 I'm guessing that in this test, it's never… 288's never happening. There's no mutation happening.
But I think that's a pretty… I think it's a pretty trivial fix. You just, create… A fresh… well, you have…
Arthur Silva Sens 00:50:15 You can add the cover, cover flag to the goal test, and you see if the test is covering this part.
Owen Williams (he/she) 00:50:22 Yeah, but… Yeah, one, but it's hard to do combinatorial coverage. You want to know if 288 ever runs, if 271 also runs.
Arthur Silva Sens 00:50:38 I see, yeah, makes sense.
Owen Williams (he/she) 00:50:40 yeah, so it's… it's gonna be… it's a little tricky. So, yeah, the… Okay, so the question is, what is 288 doing? Why is it… what is the mutation that's happening here?
Arthur Silva Sens 00:50:56 Imagine we receive Yeah, I think this is a book, to be honest.
We receive a target info with job and instance, and there's no labels.
Then we receive another target info with the same job and instance, but then there's extra labels.
Owen Williams (he/she) 00:51:14 Okay, so this is fine, because it's gonna be added the first time you create it, and then when you retrieve it from the cache, it's already gonna have that added, so it'll never need to add it again if there's an existing one. So you're still… yeah, so that's why… That… I think that's a little too magical, but that's why it's working.
Does that make… is that… did I explain that well?
Arthur Silva Sens 00:51:41 Yeah, I still feel like this is a bug, though.
I imagine we receive one target info with job an instance, with a lot of labels, then we receive another one.
that matches Java instance, but with no labels.
we are not removing the labels from the previous one. We are only adding… we are only ever adding.
Jonathan 00:52:04 What do you need to remove?
Arthur Silva Sens 00:52:07 I don't know, to be honest.
Jonathan 00:52:11 We are… we don't need to fill with new labels when they appear.
Arthur Silva Sens 00:52:21 I don't know how… I don't know how to explain it, but something feels off.
Jonathan 00:52:25 Okay.
Owen Williams (he/she) 00:52:26 Yeah, so the whole point of this block is to… Add those labels if they don't exist, right?
Arthur Silva Sens 00:52:33 Yeah.
I think this is a different problem. Let's focus… Okay. And what we have…
Owen Williams (he/she) 00:52:44 It makes sense why this works, because the first time you encounter that metric that didn't have the labels, you added them, you added it to the cache with the labels. The next time you do the lookup, you pull it out.
It's the same thing, it already has the labels added, you're not gonna add them again, it's not gonna mutate it. So, I… yeah, I agree it smells bad, but I see why it's working.
Arthur Silva Sens 00:53:12 Okay, I… Jonathan, how do you want to proceed with this? Like, do you want to guide the… the author?
to remove the mutex, do an open API yourself.
Do you want me to open a PR? How are you feeling?
Jonathan 00:53:30 I think if I open a PR, it will be faster, because the guy, it's… It's, like, 3 weeks that the guy.
Owen Williams (he/she) 00:53:37 Don't enter us.
Jonathan 00:53:40 So maybe I can just open a new PR.
Arthur Silva Sens 00:53:44 Yeah, sounds good to me, but if you do that, please… Let the author know why you're doing this.
And not just… leave him…
Jonathan 00:53:56 Like, we've developed any information?
Okay, nice.
Arthur Silva Sens 00:54:02 can review PRs until Friday. After Friday.
I cannot promise anything. I'm gonna be away for 2 weeks.
Jonathan 00:54:13 Okay.
Arthur Silva Sens 00:54:17 Alright, thanks, Owen and Arv.
I honestly, that was too hard for me here.
Owen Williams (he/she) 00:54:25 It's… yeah.
Jonathan 00:54:25 Yes.
Owen Williams (he/she) 00:54:26 A bit convoluted, but yeah, yeah.
Arve Knudsen 00:54:28 I can actually… I can also recommend using Claude Cold to review the PR. It's pretty good at this point.
Arthur Silva Sens 00:54:39 I never used it. Is it better than Copilot?
Arve Knudsen 00:54:43 I think so. Yeah, I think so.
Arthur Silva Sens 00:54:46 Awesome, I can try that.
Arve Knudsen 00:54:47 Just, like, ask it to… to analyze the… the branch, versus, main, and… And then ask if it finds any bugs. I always do this, like, two-pass process, because when you ask it to find bugs, it goes, it goes kind of deeper.
Jonathan 00:55:07 Which is the name of the tool?
Arve Knudsen 00:55:09 Cloud Code.
Jonathan 00:55:11 Quote, quote.
Arve Knudsen 00:55:13 So, like, yes, you need, you probably… maybe there's a free tier, I'm not sure, but usually you have a subscription with Anthropic.
So, at least Claude, it complained that the original PR has serious bugs, like Deadlock Risks.
And after… after I removed the… the mutex, it's actually happy.
So… But this is, like, you know, a kind of, like, superficial review from my side. Like, I would have to kind of look more closely.
But I think, kind of, my approach would be… If… if we still think there are… If you still think there are bugs there, we should try to devise tests catching the bugs.
Because that's both, a proof that there are books, and then you have… Protection from future regressions.
What do you think, Owen? Do you… At this point, you don't think there are bugs there, after removing the musics?
Owen Williams (he/she) 00:56:23 I… I think there might be. I think… I think it's a little… you're relying… there's still some clobbering happening, and it may be okay because of the way the data is, but that doesn't feel good to me.
Arthur Silva Sens 00:56:37 Yeah, but I like your suggestion, Arif. Like, we have one test, let's fix that, and then we create another test for the other bug.
Arve Knudsen 00:56:48 Which, which Pergistat?
Exactly.
Arthur Silva Sens 00:56:53 There is a… there is… we are cat… we are retrieving resource metrics, and then adding labels Without deep copying the resource metrics.
Let me just find the line, it's… Line 270…
Jonathan 00:57:18 And then again, on line, 3…
Arthur Silva Sens 00:57:22 2, 3…
Arve Knudsen 00:57:41 Can you share the screen on… poem… point out the… what you think is possible again, because I have a modified copy.
Arthur Silva Sens 00:57:56 Here… We are retrieving Resource metrics from the cache.
We are not… Using a deep copy.
And then we take the attributes.
Where do we take the attributes?
Owen Williams (he/she) 00:58:19 283… Oh, yeah, yeah, you take them from there, yeah, yeah.
Arthur Silva Sens 00:58:24 We take the attributes from… The resource metrics that were not… Deep copied, and then we add new labels to those attributes. So we are changing… when we get something from the cache, and we do this, we are changing directly the object that is in the cache, because this is the address.
Arve Knudsen 00:58:49 Yeah, I was also uncertain about that code, but I… I cannot say… I can't say it's a bug, necessarily. I mean, that… That cache is local to the function, so it's not shared with other requests.
I mean, the resource metrics map, it's… that is created in the function.
Arthur Silva Sens 00:59:09 Good point. Yes, it is.
Arve Knudsen 00:59:12 So it's not shared states.
Arthur Silva Sens 00:59:14 is different from RMCatch.
Which is in the…
Owen Williams (he/she) 00:59:18 That's true.
And your cache is based on the labels.
Arthur Silva Sens 00:59:23 Yes, it is.
Owen Williams (he/she) 00:59:24 So, you'll never pull… something from the cache with different labels. You'll never add new, weird, different labels to it.
Because it's… Yeah, the problem with the code is… If the thing's in the cache, you don't have to do anything.
The whole point is it's in the cache. Why don't you just return?
Arve Knudsen 00:59:58 Yeah, that's also what struck me as strange. It's like, if you find it in the cache, why are you changing the attributes?
Owen Williams (he/she) 01:00:06 Yeah.
I think, by definition, if you put it in the cache, it's because you've done the work. There's no other… once you've got it, if it was in the cache, you did the work.
Return, exit early, you're done.
Arthur Silva Sens 01:00:18 No, that… So the cache is only for the resource attributes, right?
So we only add to the cache the labels from the target info. If we receive a metric that is not target info, then we retrieve from the cache, and then we create the whole resource attributes using The attributes from the previous target info.
Owen Williams (he/she) 01:00:47 That should just be a copy of that.
Arthur Silva Sens 01:00:52 Yeah, yeah.
Owen Williams (he/she) 01:00:53 Yeah, the point is, you don't need this… this loop At 286.
add the remaining labels as resource attributes. You already did that work when you made the cache entry. There should be an early return.
Arthur Silva Sens 01:01:07 Alright, so this is because… I'm not talking about that section, I'm talking about the lower section.
Owen Williams (he/she) 01:01:13 Like, I think this is what's wrong with this code, is that the point of a cache is you've got the cached item, you're done with the work. And if you have to do more modification after that, it's getting confused about what you're modifying, because there's two caches here, like, there's the attributes, the resource metric, you've got, like, two lookups. You've got cached attributes, and you've got the existing RM, so there's two caches. So… if… so, I think… I think the code should be sort of reorganized to say.
hey, if I do a lookup, that means I need to do no work, do no work. If I've got… if I've done a lookup, that means I do need to do a little work, do a little work. If I fail it completely, do all of the work. And then if you've got that sort of, like.
Logical flow, then you won't have this thing where, like, you're getting the thing, and then also doing all of the work.
Arthur Silva Sens 01:02:11 Yeah, that makes sense.
Owen Williams (he/she) 01:02:14 Because this block that you've highlighted, I believe, is the… all of the work if you've failed the cache lookup, but that shouldn't be required if you've succeeded the cache lookup. And so, I think there… I think there just may need to be some juggling around to… to have it be that more, because it sounds like there's 3 cases. The total cache miss, the attribute lookup succeeded, and the whole thing succeeded. And those should be treated, sort of.
Distinctly.
Arthur Silva Sens 01:02:50 Okay, we are on time already.
Owen Williams (he/she) 01:02:52 Yeah, yeah, no, I think… but I think it's… I think it's getting… it's… it's close, but, like, yeah, it's just… it just could… it just needs a slight… Reshuffle.
Arthur Silva Sens 01:03:03 jonathan, I can see you doing this.
You're faking too much?
You're doing this… Like, I don't know how to say that in English, but I can see your, hookahs.
Inca, in English.
Owen Williams (he/she) 01:03:26 From which languages I was gonna ask.
Arthur Silva Sens 01:03:29 Portuguese.
I can see your wrinkles.
Owen Williams (he/she) 01:03:36 Yeah, in English with a furrowed brow.
That's the…
Arthur Silva Sens 01:03:40 Alright, Zai, I…
Owen Williams (he/she) 01:03:42 Yeah, excuse me…
Arthur Silva Sens 01:03:44 I am assuming you're having a hard time, but I can help you with that.
Jonathan 01:03:49 I think that I understand the whole… the whole discussion.
But I just need to take more time to… Because we, we discover other things.
That are not related to the bug, but the way that we are organizing the code.
And the way that we are copying and assigning new values to the attributes?
So, we just find all other things here.
Arthur Silva Sens 01:04:15 Yeah, yeah, code is a little bit messy.
Okay, but let's end here today. Thank you, thank you everybody, and ping me when you have the PR, Jonathan.
Jonathan 01:04:31 Thank you, Owen. Thank you. Thanks, Arif.
Arve Knudsen 01:04:34 Bye-bye.
Right.
