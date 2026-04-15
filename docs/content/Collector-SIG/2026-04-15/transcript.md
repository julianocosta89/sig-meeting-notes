SIG: Collector SIG
Date: 2026-04-15
Duration: 15 minutes
============================================================

## Zoom Recording Transcript

**Andrew Wilkins @ Elastic Observability** 02:54 Hey, Josh. How you going?
**jmacdonald** 02:56 Andrew.
Happy Tuesday.
**Andrew Wilkins @ Elastic Observability** 03:01 Happy Wednesday.
**jmacdonald** 03:04 Oh, you're right, good morning, I guess.
I, I've made it to several of these in a row.
But it's still the thing that I see happening, is it's a very low attendance.
Oh, good! Look at this, we have more than one… person from the time zone that I live in. Or… no, gee, I don't know Dimitri's time zone.
Hey, Dimitri, what time zone are you in?
**Dmitrii Anoshin** 03:32 Hi, folks, I have PST.
**jmacdonald** 03:35 Yes, okay, you're in my time zone.
Well, this is always a small meeting, but, I can pull up notes and project and… If you'd like.
**Andrew Wilkins @ Elastic Observability** 03:49 I just had one thing on the agenda, I don't know if we want to go through the board or not? Does anyone… Wanna do that one?
**jmacdonald** 03:58 I've done a terrible job of the board in the past. If anyone else would love, I'd be glad to do it with us.
**Dmitrii Anoshin** 04:07 Yeah, I would skip it this time, given that it's only three of us, and I got a run earlier today, so… Andrew Wilkins @ Elastic Observability 04:13 Okay.
**Dmitrii Anoshin** 04:14 Yeah, probably we can just go with your item.
Yep.
**Andrew Wilkins @ Elastic Observability** 04:19 Okay, cool.
Alright, so, some people on my team, or an adjacent team, are working on migrating, or sorry, porting some code from Elastic Agent to hotel collector receivers, and these are effectively They're doing sort of what a scraper does, but they don't work quite the same way.
So these are receivers… these are inputs that wake up every now and again and, send some data, on an interval. That's why I say they're sort of like a scraper. The reason why they're not exactly like a scraper is, that they stream data out, so they don't… They don't just scrape something, get a batch of data, and then return it. So this is where the things don't quite line up with the scraper interface.
I don't know the details of what the scraper is doing exactly, but apparently they're… they're gathering, like, on the order of Hundreds of thousands of log records at a time.
And they have quite a large interval in between each scrape.
So there's two problems that we've encountered. So one is that the interface for Scraper is basically get a batch, return it to the scraper controller, scraperController then sends it to the next consumer. So that doesn't work for streaming. And then the other problem is that these scrapers need some kind of cursor committing, so they want to… Resume scraping from a particular point.
whatever, they're scraping from some external API, and that API returns a position, and then they want to resume scraping from there in the next iteration.
And that's not really possible with the API as it is either.
Because you… you wouldn't want to commit the cursor until you know that the data has been consumed.
And you… once you've… once you've returned to the controller, you have no way… no visibility into that.
I mean, you could with some gymnastics, like, wrapping the next consumer and so on, but it's just not very, Straightforward.
**Dmitrii Anoshin** 06:30 It sounds like, stanza… regular stanza receiver.
**Andrew Wilkins @ Elastic Observability** 06:37 Okay, I'm not familiar with the stencil receivers.
**Dmitrii Anoshin** 06:39 A stance receiver is essentially any lock-based receiver that we have in-country. Like, file lock receiver, for example, syslog, and others. They… if you have a file lock receiver currently configured in the collector, you have to provide, storage extension to… Holy … To persist checkpoints.
So you're reading from particular files, and, like, you… you… whenever it's succeeded from that file. I guess it actually waits for the consume function to return before it updates the checkpoint. So it's pretty much exactly what you what you described.
**Andrew Wilkins @ Elastic Observability** 07:27 Yeah, the reason why I want to use the scraper interface is related to the RFC that I recently wrote around extensible controllers. Basically, what we're trying to do is have External scheduling of scrapers, so they're not always idle.
And so the idea was that we would have some ephemeral workloads be triggered.
Do some work, and then go back to sleep after committing the cursor.
**Dmitrii Anoshin** 08:00 Yeah. Those tensor receivers, they work not on any, like, schedule. They just… watch.
Or, let's say, if you configure it on a file, it will watch for new updates, and whenever something new comes up there, it just starts reading from it.
So, it's, like, some set of workers, and if nothing… nothing comes out, they just, in the… They're just sitting and waiting there, so it's a bit different.
approach, but if… I'm still… we potentially can somehow bridge the gap between scraper, helper, and those… the receivers, and whatever you're trying to introduce to scrapers also may… Applied to those receivers.
I'm just trying to figure out What, is, is… you have two suggestions, right? One, URFC, another one is the team is working to replace.
Is it somehow related? Is it part of the same goal, or they are separate?
**Andrew Wilkins @ Elastic Observability** 09:09 Yeah… They're sort of tangentially related, They're separate efforts, so I just want to make sure that we're aligned, on the… in the eventual… The way these things come together. And we can… we can use the controller… the scraperController extension interface directly, but it wouldn't go through the scraper helper API, because of the reasons I mentioned before. So the scraper, controller interface, I, I… described in the RFC as basically, you register yourself, and it'll tell you when to do something. But it doesn't imply that you have to use the scraper Helper API.
As in… the bat… like, return a batch, and the controller sends it, it's just a signal, and then you can do whatever you want. So if you… on that signal, you could stream out And you could have full control over… Committing the cursor and whatnot.
**Dmitrii Anoshin** 10:09 Yeah, if you add this capability to this, like, SURIS controller.
scraper controller, right? And potentially, it can be even… help us bridge the gap between stanza and receiver helper. So, for example.
like, stanza receivers might be re-architected in a way that They also receive some signals.
Instead of using a constant… Workers.
And those signals would just, like, be… Apply it to itself whenever something is… succeed downstream, or something like that. I mean, just like… just an idea, I'm not saying that that's the right approach, I'm just thinking that, potentially, how we can combine them together, because I… ideally, I think it's beneficial to not… have separate… Separate, like… projects. Sub-projects. Agreed. Several projects. But, just FYI, that's gonna be super complicated, because stanza… It, like, its own mechanics, it's very complicated to replace, but we can at least start with something.
**Andrew Wilkins @ Elastic Observability** 11:25 Okay, I'll look into it. I haven't looked into the stenza code before, so I'll have a look and see.
Where the overlap is. Thanks.
**jmacdonald** 11:34 Could you imagine a different extension point or another extension interface that would You could add to the scraper helper that would… Give you a hook you need to commit, or, like… give you some sort of, like, conditional success-failure look. I'm just thinking out loud.
**Andrew Wilkins @ Elastic Observability** 11:56 Yeah, I think we probably could for that issue, for the… tell me when to commit. I think that could be done.
But that would still leave the issue related to not being able to stream data out.
So I feel like those two things probably should be solved in the same way with a new interface that doesn't imply returning a single batch.
And giving up control.
I… I was thinking… I haven't looked into it deeply, like, I haven't… thought about what the API should look like, but I was thinking that maybe there could be two two interfaces for scrapers. One, a simple one, like what we have now, where it's, you know, just, give up all… give up all control to the controller, and the other one would be more like, just give me a signal, and I'll decide what to do. And that would be for more expert cases.
But again, I haven't… I haven't really thought about it super deeply.
**jmacdonald** 13:01 It makes Dimitri's suggestion about looking at how to fit Stanza into your model quite relevant. I can… I can see. I can imagine it. Some sort of checkpoint-oriented watcher.
API, or something like that, and you could simulate a webhook, or… A file growing, And then, yeah, that's a design question.
**Andrew Wilkins @ Elastic Observability** 13:30 Yep, I'll have a look and see.
What categories we have.
**jmacdonald** 13:35 I also have not looked closely at the stanza. Now I know how much complication there is.
**Dmitrii Anoshin** 13:40 You'll be surprised, Josh, it's like, it's a new world.
**jmacdonald** 13:44 Interesting. Good to know. I have not… yeah, no, no one… yes, okay.
**Dmitrii Anoshin** 13:51 Yeah, and it's, for the context, it was donated by, BindPlate.
And then…
**jmacdonald** 14:00 It was Dan Jaglowski's baby, right? And then he left. Okay.
Maybe I'll have to get into it.
**Dmitrii Anoshin** 14:07 it has its own concepts that were not fully adopted or replaced by OpenTelemetry concepts.
So, there is… ideally, we would need to… do something with them, but yeah. Even, like, some… in terms of performance improvements, they, like, stanza… receivers operating over a different model that is wrapped in OpenTelem3, so yeah, there are a lot of things there.
That's what I'm saying.
If we at least start somehow bridging the gap with the receivers, it might help, potentially, going forward to refactor it.
**jmacdonald** 14:51 At the high level, I really like the observation that a scraper and a file watcher are kind of… a scraper, processor, scheduler, and a file watcher are kind of similar to distance.
**Dmitrii Anoshin** 15:03 Yep.
**Andrew Wilkins @ Elastic Observability** 15:06 That's all I had.
**jmacdonald** 15:10 Thank you, Andrew, and happy Wednesday!
**Andrew Wilkins @ Elastic Observability** 15:14 Alright, we're leaving it there.
**Dmitrii Anoshin** 15:16 Over there.
**Andrew Wilkins @ Elastic Observability** 15:17 Cope.
Alright, thanks. See you next time. Have a good evening.
**Dmitrii Anoshin** 15:20 Yeah, stand right.
