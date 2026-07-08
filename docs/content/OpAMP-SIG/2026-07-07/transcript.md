SIG: OpAMP SIG
Date: 2026-07-07
Duration: 16 minutes
============================================================

## Zoom Recording Transcript

**Dakota Paasman** 02:50 Hello.
**tnajaryan** 02:52 Hello.
**Evan Bradley** 02:57 Hi, everyone.
**Andy Keller** 03:01 Thanks.
Sorry I've been gone for so long Everything.
**Evan Bradley** 03:10 I get.
**tnajaryan** 03:11 You've been gone. I wasn't in Glasgow as well, so I don't know.
Were you on vacation?
**Andy Keller** 03:19 I was, I was in Austria for a week with Dynatrace, and then I was in Norway and Sweden with my family for two weeks.
Norway for a week, and then Sweden for a week It was nice to get over the jet lag and then just stay there for a little while. Yeah, yeah.
**tnajaryan** 03:44 The first, I guess, few days are not very pleasant for them. Yeah.
**Evan Bradley** 03:51 To say the least.
**tnajaryan** 04:04 Okay, I'm gonna share my screen with the agenda.
Oh, it's not letting me share. What's going on?
Yeah, it's not working. I can't share the agenda. But anyway, let me see what is there.
Two items.
Yeah, I think we can start. Kelsey, you want to talk about the… What is it that consumer component status report not working?
**Kelsey Ma** 05:01 Yeah, so this is something I saw someone open for the extension, but I also ran into this when I was just testing the supervisor. I believe when I — after I dug into it, I believe what happened is the PPID support for — Preventing, like, the collector from being orphaned.
it was added right before the migration to component status and because of the migration it sort of changed the when you can call like report status and things like that and so now extensions don't have the ability to send those sort of like fatal events. And so the detection just, it will work, but then nothing will happen. So the collector, I noticed, stays around on… In certain cases, like, I think on Linux, if you run it as a service, you get by because the service group will help close everything out for you, but Windows, it doesn't really work, and then if you run it as a, just like.
processes, it won't work.
And so I wasn't quite sure the best, kind of approach for this in terms of technically, I guess, like.
if extensions are able to kind of do like the wrapper similar to the rest of the pipeline, how they have this sort of host wrapper that lets them implement the reporter interface. I'm not sure if that… Is like a large change that needs to be.
surface, like, on a higher level, or if we wanted to add, like, some more localized, kind of.
workarounds to a degree.
In in just like the supervisor or something.
**tnajaryan** 07:07 Yeah, I don't know how these parts work. Maybe, Evan, do you.
**Evan Bradley** 07:11 Not off the top of my head. It sounds like this might be an issue… With the component status reporting itself, Am I… understanding that right?
**Kelsey Ma** 07:23 It seems to be the.
I was reading, I was digging back through a bunch of these PRs. It seems to be they elected to, do this. So basically anything that doesn't have that reporter interface implemented was at the time it was agreed upon that they aren't able then to.
send these sort of events.
**Evan Bradley** 07:52 that I think… I might have to just… Read up on this. The component status reporting, mechanisms have evolved over the course of a couple years, and I don't really have the context in my head.
Right now.
**Kelsey Ma** 08:09 Yeah, I just linked the… There was a… PR for the RFC, that had a good majority of the discussion on it, I believe.
but yeah, I think that change went in and then, kind of… change the the base like assumptions for for the status reporting.
**tnajaryan** 08:56 Maybe worth pinging Tyler to see.
If you can help in any way, clarify.
I really don't know much myself and anything about this, this part. So.
I don't think I can be helped. I can help in any way.
**Andy Keller** 09:18 Yeah, same here.
**Evan Bradley** 09:21 I can follow up on this, but it just… I need… it's gonna take me a minute just to… Reacquaint myself with why these interfaces were designed the way they were.
But I can, you know.
I'll assign myself to this issue, and I can take this one.
**Kelsey Ma** 09:42 Awesome. Yeah, thanks. Appreciate that.
**Evan Bradley** 09:46 Sorry, I can't help more right now, but.
**Kelsey Ma** 09:50 Yeah, no, I figured this seems to be a larger thing that needs to be looked into for the component status as well.
**Dakota Paasman** 10:02 Did I… Misunderstand the original part or.
This is the issue you linked is related to something else that you found in the supervisor related to the component status report, right?
**Kelsey Ma** 10:20 Yeah, so, the PPID detection was added, and then right after that, how, so that, that works by, when the collector sees the, or, or it's more so.
In the extension side of things, the OpEmp extension side of things, it's not working as expected. So if the supervisor goes down, the collector doesn't actually clean itself up. So we have like that same orphan issue again, because how it's doing it is when it doesn't see the… process anymore, it will send like a fatal event to the, like the fatal health event. And it just goes nowhere at this moment because we're not implementing this, I believe, the reporter interface, which the component status introduced.
So it's just kind of, there's, like, a check in the code that checks if you're, you have that reporter, and only if you have that reporter interface, then it like calls the report method.
If it doesn't, which is currently the case for all extensions, then it just doesn't do anything.
They added a wrapper on for any of the other like pipeline components. There's like this thing called a host wrapper in which they implement the interface, but extensions didn't seem to get the same.
**Dakota Paasman** 11:53 Okay, yeah, okay, so it's specific to the op-amp extension just being surfaced in the supervisor right now?
But… Evan, I might actually be able to take this. I had a side project a few months ago.
Kind of touching in this area.
And I'll look back at that code and see if it addressed this or not. So I'm assuming this was still a problem a few months ago when I was working on that.
I can let you know about it, at least, see if it… When I look back through the code, see if it addresses this or not.
**Evan Bradley** 12:29 Cool, yeah, that'd be Thank you.
**Dakota Paasman** 12:32 Yeah, okay.
**Evan Bradley** 12:41 And feel free to ping me if there's anything you need from my end.
**Andy Keller** 12:48 Yeah, I still think looping in Tyler would He probably knows how it works.
Unless extensions… And we either, you know, they didn't get to them or they work differently and have different expectations or something.
I'm not sure.
Anything else on this?
**Kelsey Ma** 13:15 Nothing else on this from my side. Yeah, thanks.
**Andy Keller** 13:18 Yep.
Okay, I just added an item.
Unfortunately, Michael is no longer on Elastic and it's not clear how involved he's going to be in OpenTelemetry.
For a bit, if anybody has, Openings, I'm sure you should reach out on.
So.
CNCF Slack. I think you'd probably be open to some opportunities.
He was the, he had this PR for using an alternative.
Websocket client.
Gorilla WebSockets haven't been maintained for a very long time, but we still use them.
I'm gonna look at this, but I also just wanted to see if anybody else Had a chance to look at this, or had any interest in… Yes, I think, you know, changing out the WebSocket library could Be totally great and, you know, improve performance or it could be a disaster. So it's behind a.
A build tag right now, so… Should be… Interesting to attest.
**tnajaryan** 14:32 Again, check with Michael if he plans to stay with OpenTelemetry, and I guess It probably is going to take some time for him until he knows what his next job is.
In which case, hopefully, he will be the maintainer. So…
**Andy Keller** 14:47 You know.
**tnajaryan** 14:47 Maybe we can do that, right?
**Andy Keller** 14:49 Well, I know he reached… he reached out to me on the CNSAFE.
**tnajaryan** 14:53 Yeah.
**Andy Keller** 14:53 Wanted to make sure I ushered this through, so.
**tnajaryan** 14:57 Okay, okay. But we don't know, right, whether he's staying with OpenTelemetry or not yet.
**Andy Keller** 15:03 Yeah, we don't know, but I know based on his message to me that he would like me to.
help see this across the finish line.
**tnajaryan** 15:12 Okay.
Okay, yeah, I guess if there is anybody who is interested.
Of course, that's fine. If not, maybe we'll see. Maybe Michael continues working on that.
Otherwise, we'll decide what do we want to do about that.
I suggest we keep it open as it is, and I did take a look at the PR. He updated it with the with the build tags, so that it's a feature flag, essentially, which is built.
But it's quite a big PR. I didn't do any thorough review on that. So I think we should keep it open for now.
and we can decide what we want to do about it in the next few weeks.
**Andy Keller** 15:58 Sounds good.
**tnajaryan** 16:05 And it was, by the way, I was surprised that the amount of changes was so small, really.
So which is a good thing.
**Andy Keller** 16:16 Yeah, agree.
**tnajaryan** 16:28 Cool.
That's all we have in the agenda. Anybody has any other topics.
**Andy Keller** 16:45 Nothing here.
**tnajaryan** 16:48 Okay, thank you all.
**Andy Keller** 16:50 Thanks. Bye. Bye.
