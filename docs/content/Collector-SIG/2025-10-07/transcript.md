SIG: Collector SIG
Date: 2025-10-07
Duration: 13 minutes
============================================================

## Zoom Recording Transcript

**Andrew Wilkins @ Elastic Observability** 00:40 Hi, Paulo.
**Paulo Janotti** 00:41 Hi, Andrew.
**Andrew Wilkins @ Elastic Observability** 00:43 How you doing?
**Paulo Janotti** 00:47 going well, did less than I wanted on the collector this week. I need to catch up.
**Andrew Wilkins @ Elastic Observability** 01:03 Are you primarily working on Windows-related things? I've seen your name around Windows things before.
**Paulo Janotti** 01:09 Yeah, yeah, I had some experience for many years with Windows, and nowadays it's a skill that's very rare, you know, so…
But… but fortunately, I… this is one of the things that I want to do this week, is open the PR to enable the rest of the tests for Windows ARM in Contrib.
Most things work smoothly, you know?
I do expect some, we have to be careful with,
see Google, because, the GCC compiler that's available on the runner doesn't have, I'm librarians, so…
Because the… I don't know if you know that part, but the Windows arm, what it does, it has a layer to run AMDX64, and it runs pretty smoothly, but you can't mix in the same process, right?
So, when you use CGO, what happens? It builds ARM,
and try to load the things with AMD64, and then it's kind of weird errors everywhere. But,
I identified that there are very few cases. I actually already submitted those PRs. I just want to do a clean pass on everything, and we should be able to enable Windows Arm for, the contrib, no?
**Andrew Wilkins @ Elastic Observability** 02:50 Cool.
Sounds good.
Might be a quick one, because I don't have any topics, actually.
**Paulo Janotti** 03:36 Yeah, I'm just trying to be on top of the meetings that match my time zone I try to join, you know.
**Andrew Wilkins @ Elastic Observability** 03:47 Whereabouts are you based?
**Paulo Janotti** 03:50 I'm, I'm near Seattle. I'm, it's a small city nearby Seattle, so… And… where are you, Jason?
**Andrew Wilkins @ Elastic Observability** 04:02 I'm in Perth, Western Australia.
**Paulo Janotti** 04:05 Oh, a long way away. What, what is in your time zone?
**Andrew Wilkins @ Elastic Observability** 04:10 Singapore, Beijing… like… Oh, Southeast Asia.
**Paulo Janotti** 04:16 Yeah.
**Andrew Wilkins @ Elastic Observability** 04:17 and China.
**Paulo Janotti** 04:19 Yeah. We have to be mindful about this. I had a time that I was working with a bunch of people in Poland,
And at the time was good, because I was waking up very early, and I tried to meet with the folks, like, 6, 7, 8 AM my time. 8 AM is already pushing for them.
In my time, it's the end of their day. So, yeah, we have to be mindful about people's time zones, you know.
**Andrew Wilkins @ Elastic Observability** 04:48 Yep.
**Paulo Janotti** 04:50 Yeah, unfortunately for me, I think the meeting that has having a lot of demand, a lot of attendance on the collector is the one that, in my time zone, is Wednesday at 5 AM.
**Andrew Wilkins @ Elastic Observability** 05:07 Yeah, it's also inappropriate for me.
As you can probably imagine.
Yeah, we didn't… we didn't even have a… there was no meeting previously that was suitable for me, but that changed last year, I think, when we revived this one.
Well, it doesn't look like anyone else is coming. So…
**Paulo Janotti** 05:32 Yeah.
**Andrew Wilkins @ Elastic Observability** 05:33 Thing you wanted to discuss?
**Paulo Janotti** 06:00 Yeah, I think we can wait one, two more minutes, and if nobody shows up. I think I did by not intentionally, but I communicate about the Windows Arm stuff that I'm planning to do, so…
**Andrew Wilkins @ Elastic Observability** 06:13 Yep.
Yeah, the only thing I've got going on is telemetry-related changes in core, so I've been working on
Making it possible to inject a different telemetry provider.
So normally we would just use the one from the SDK, and I don't expect anyone will use anything other than that, but our use case is that we want to…
inject additional attributes into all of the metrics. So, extract metrics… sorry, extract attributes from the context, and then inject them into metrics, or, like, sorry, data… data points recorded, and… and so on.
And so, we need to…
Well, ideally, we would use a processor. There's processors for traces and for logs, but not for metrics.
So the way we can get around that is by injecting a custom wrapper around the SDK that will inject additional attributes. It's a bit of a heavy-handed approach, but it's really the only option we've got at the moment.
**Paulo Janotti** 07:19 Are you a member also of the Golang SDK?
**Andrew Wilkins @ Elastic Observability** 07:25 No, I've done a little bit of contribution, but I'm not in the SIG.
**Paulo Janotti** 07:29 I see, I see. Yeah,
I think this is… is a good thing that now we can really leverage the SDK. I think,
many years ago, there was no SDK when the collector came, so… and now that we are moving to… it's much better.
Better division of, concerns and work for everyone.
**Andrew Wilkins @ Elastic Observability** 07:57 Yep.
Maybe one other topic I'm looking into on the side, I'm not sure if you're interested at all, but there's, we have a need for…
basically running scrapers, but on demand, rather than on a timer. So we want to trigger them, in…
Due to some external event.
And…
So I opened an issue about this on Core a while back, about introducing a command, like a scraper command to the collector, which would run one pipeline with a particular scraper receiver just once, and then exit once it's been delivered.
Is that interesting to you at all? Is that something you would use?
**Paulo Janotti** 08:45 It sounds interesting, I think it has…
the potential to cover some stuff that… we still have some legacy of people running telegraph stuff, via script.
And I think that has the potential to… I will not say 100%, there are some use cases that are very strange, but I think it… it has the potential… I will guess, like, this is a gas, but I will guess, like…
67% could be satisfied with this kind of stuff, you know? If you think even the more, let's say, complicated cases, like.
we can have these scrapers that… if we are able to reuse these scrapers that we have in receivers that are very specialized, we put in packages. Okay, so, but if you're able to use those packages, like the internal packages that we have.
I think it has the potential to satisfy a lot of those script cases, you know.
**Andrew Wilkins @ Elastic Observability** 09:55 Okay.
**Paulo Janotti** 09:57 That was most…
**Andrew Wilkins @ Elastic Observability** 09:58 Okay.
**Paulo Janotti** 09:59 I know most of these scripts, if you look.
Some users have, on the timer, but…
a lot of them do things like, hey, you have some data? Oh, I have, and then they do something. So, if we have the trigger that can monitor this presence of files or other things like this, then we can, really kind of get a good chunk
But… Anyway, I'm interested in taking a look at that.
**Andrew Wilkins @ Elastic Observability** 10:30 Okay, cool. I'll, I'll leave a link in the agenda, I'm just looking for it now.
**Paulo Janotti** 10:36 Oh yeah, and after we finish here, I'll put my name there, so people know that at least the two of us were here.
**Andrew Wilkins @ Elastic Observability** 10:44 I already added you to the agenda.
**Paulo Janotti** 10:46 Oh, thank you.
**Andrew Wilkins @ Elastic Observability** 10:47 That's right.
There we go.
Yeah, if you have any input.
Feel free to leave on the shoe.
There's a couple of use cases I have in mind.
One is, you might want to perform a scrape in relation to,
like a webhook, so actually it's in the example there. Another is…
well, I guess it's related to a webhook, but you might have an alert fire, and then you want to trigger something in relation to that alert.
And then the other one is… Timer-based, but not…
In the collector, so you might have a, you might want to horizontally scale periodic collection.
So across a fleet of collectors, and then you obviously want to do that outside of the collector. So that could… well, it could be done inside, so it could be polling, you know, a job queue or something, but alternatively, you could use something along the lines of a Kubernetes cron job.
And, trigger once, and then exit.
So those are the kinds of things I have in mind.
**Paulo Janotti** 12:27 Yeah, I think that there are some… some good use cases for, for this. I, I…
We have some things that, people nowadays filter out, stuff, because it's sugar bowls, but what actually they want is kind of,
The capability of collecting around interesting events.
So, for instance, the audit on Windows is very, very, very, very verbose. You don't want to collect that all the time.
But giving certain things happening, you want to collect everything around that time window.
**Andrew Wilkins @ Elastic Observability** 13:11 Yep.
**Paulo Janotti** 13:12 You know, so for this UKZ, it's very interesting. Yeah, I'll take a look at that.
**Andrew Wilkins @ Elastic Observability** 13:18 Cool, thanks.
Alright, well, no one's coming, obviously, so…
**Paulo Janotti** 13:25 Yup.
**Andrew Wilkins @ Elastic Observability** 13:25 I guess we can finish there, unless you have anything else.
**Paulo Janotti** 13:29 Yeah. No, I'm… I'm good. Thanks for coming!
**Andrew Wilkins @ Elastic Observability** 13:35 Have a nice evening.
**Paulo Janotti** 13:36 Alright, bye.
**Andrew Wilkins @ Elastic Observability** 13:37 See ya.
