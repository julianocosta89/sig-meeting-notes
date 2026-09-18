SIG: Browser SIG
Date: 2026-09-17
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**maxime quentin** 01:18 Hello?
**Cleo Schneider** 01:21 How's it going?
**maxime quentin** 01:23 Pretty good.
And you've…
**Cleo Schneider** 01:28 Doing alright.
**Martin Kuba** 02:20 Just, like, wait one more minute… Alright, hi everyone.
We can get started, As usual, if you have something to talk about, you want to talk about, just put it on the agenda. We have a few things.
First one is mine.
I just wanted to give a quick update on… Semantic conventions work, just for visibility.
There is… We have… We started working on adding semantic dimensions to this repo, kind of following… what Android SDK has done.
But there's now a new, client-side, semantic conventions dedicated repo that has been… is getting bootstrapped, and there is… there is a discussion whether or not it would make sense to have Browser-specific and mobile-specific semantic conventions there. So… This PR that's in progress, I'm… Waiting on… on that decision before, getting it, trying to get it merged. So that's just a quick update on that one.
Any questions on this?
**Joaquín Díaz** 03:58 Does… is Andrew going to have semantical versions on that?
repo, or their own, like, SDK repo?
**Martin Kuba** 04:11 Yeah, so there's, that's… that's the question. So there's a new repo, And, we're trying to decide, like, if some of the conventions that are, like, the platform-specific only, if they should live there, or if they should be, like, along with the SDK.
**Joaquín Díaz** 04:32 Okay.
**Martin Kuba** 04:38 Alright, david, you have the next, next topic.
**David Luna Bistuer** 04:43 Yeah, kind of, maybe an idea that come lately, so… Sorry that I didn't post an issue for that. Maybe I'll do it later after this meeting.
But long story short is that, Something that was already fixed for the spans, now we're getting the same with logs, so… When you're doing a request, now with resource timings or a list.
the search link I'm sharing here is, like, the sandbox is using, ignore URLs.
To avoid, sending telemetry.
From our own exports, okay?
So, well, I think that's not the best, device configuration, so I think that should… that should be transparent. I think it's not… would be better if that's… configuration goes away, so you just set up the SDK, you don't have to… mines the export URLs that you're setting up. They are already ignored.
And that reminds me about the PR that is in the core repository about, doing suppressed tracing.
For Spence.
And I think that that might work with the logs, too.
When we are getting resource timing logs, we can get the spam context and then actually check if that's… If that's suppressed or not.
And then we can omit the… the… the log record, the… the log from research timings. There is one case, so that would work if we have both instrumentation, we have Fetch, XHR, and And… and resource families, because they talk to each other through the… Context manager, that network context manager is the… that utility tip we have in the middle.
There's one situation that maybe it wouldn't work.
And I need to check if there is a possibility to actually suppress something there.
But it's… it's if you're using only resource timing instrumentation and not… and you are not instrumenting fetch or XHR.
Then the logs, the resource timing logs, they don't have any context, so you cannot check the context if there's… if tracing has been suppressed… suppressed or not.
So yeah, I think just a heads up, that I'm gonna work on something.
Here on the proposal.
But do you have any ideas, or so?
Let's just add it here, or ping me.
So we can, work together on that.
But by the way, I don't know if you are… Maybe just, just to measure the temperature here, so… do you think that it's a good idea just to say that… make that, or make an effort to make that transparent, or just, you know… it's just a matter of documentation and say, hey, by the way, you need to put this in the ignor URLs, because if not, you're going to send internal telemetry.
**Martin Kuba** 07:44 So, sorry, Dale, like, is there a precedent for this, like, in the JS SDK? Maybe, It's a…
**David Luna Bistuer** 07:53 Present, yeah.
It happened… it already happened, so let me check the, Sorry, there was another PR, I'm just… I'm going to add it here.
when the… Yeah, this one. I'm going to share in the… Here in the chat, and also gonna put it in the document.
So… that PR that I created in the exporter.
was just unwrapping the fetch, so we were getting the original fetch API.
And… and the PR that I'm showing right now in the… in the document.
It's, It covers another scenario.
So, the idea, if you can… is that if we can't suppress, if we can set the context there in the fetch… on the fetch PR… on the fetch request, sorry.
Suppressing the tracing there.
then we are not getting in this infinite loop that, you know, I'm exporting, then I get the resource timing.
And then I'm exporting another log, I'm getting the resource timing from the next export, from the previous export.
I'm just, creating another log record, and then… So, just to find a way… To stop that.
Oh, and of course, you can, as the sandbox is doing, you can just, you know.
put more URLs in the ignore URL, so you can't… you have to put these URLs there, so you make sure that you are not… Measuring your, the, the exports.
So, okay, maybe my question, so before starting this, maybe a question would be.
Do you think that it's okay to have the… configure the URLs, the export URLs in the configuration.
To ignore, and then put them as mandatory into the quotation.
Or should we work on… Trying to get… You know, a simpler configuration for… For the Browser SDK.
**Joaquín Díaz** 09:59 I think it's fine to have a flag that is… true by default, that is, like, ignore exporter URLs, or whatever.
That you can turn off if you want, for whatever reason. But I think it makes sense, because it's something that… You may not be aware at the beginning that you are building this look, so if we have a way of avoiding that for your users, and then if they want, they can ignore that.
Yeah, I think it is.
**Jared Freeze (Palo Alto Networks)** 10:26 Yeah, I think we already have Quick Start.
So click start should do this by default, and then the regular… Should I just have guidance?
I don't know if that solves the problem, but it seems like… You know, quick start is more hand-holding.
And the regular is just wide open, so… Might be an option. And just document both.
**Wolfgang Therrien** 10:55 Jared, are you suggesting that the default for, sort of, the non, like, quick start be, like, be on or off?
**Jared Freeze (Palo Alto Networks)** 11:05 be off, like, no… like, basically the regular is just whatever you want to do. I don't like the opt-out idea, even if every single person does it, because I think it helps people understand the system.
That's kind of my feel. Like, if it's naked, it's, like, really naked. Like… Even if, you know.
I mean, I understand it's, like, an implement loop, but I just feel like you should copy and paste and know where the URL is, you know, to the block, or whatever.
**Trent Mick** 11:43 So, is it clear to people here that on the Node.js side, at least the design decision, this is before I got involved, is that… the exporters are… or this system, I guess, as various components that are involved, are set up to not… Propagate and generate spans for… For exporter calls.
So, like, they're out of the picture, there's no, like, you need to configure it or anything like that.
For better or for worse. I know what you're saying, Jared, and then maybe users should be exposed to that and have to turn it off explicitly, I don't know, but anyway.
Just, I'm not sure if it was clear to people from what David was suggesting.
**Jared Freeze (Palo Alto Networks)** 12:22 Well, not everyone's gonna use resource timing.
It's so it's not… You know, like, the thing David did works if you don't use resource timing.
So, it's also part of, specific config you've got.
Now, it wouldn't necessarily be overkill just to have it off by default.
You know, whether you use resource instrument edition or not.
So yeah, I mean, if that's the precedent, we could follow that too. You said for better or worse, like, what would be the worst case?
**Trent Mick** 13:01 Well, I'm just… I was leaving that open in case people have different opinions. It was the current state of affairs before I got involved with OpenTelemetry. I can see the argument both ways, like… Instrumentation shows you everything that's happening, and one of the things that's happening to your app is it's sending 700 megabytes of data out through this pipe to your telemetry thing that might be relevant. Should that get hidden all the time by default, is a question, perhaps.
**Jared Freeze (Palo Alto Networks)** 13:25 Yeah, that's a good point. I mean, it does affect… You know, it could be costing you something for sure, you know?
Anyway, Network's not free, so that's a good point, too.
**Joaquín Díaz** 13:38 Yeah, but I think the fact that it creates a loop, I think that is what may not be transparent for users. I think they… Probably want to know what's going on, even when they send telemetry.
But I think if we can avoid creating that loop where we start, like.
I create a spam, then that creates a log, then the log creates another span, so on. I think if we can break the log, that would be great.
**Trent Mick** 14:03 Oh yeah, that's a fair point.
**Joaquín Díaz** 14:04 By default.
**Trent Mick** 14:05 Yeah, having that infinite loop is not… Helpful.
**Joaquín Díaz** 14:17 And that only happens if you have resource timing, because… even if you don't use the Moki… the Moki batch fetch, we still create a… you still get a resource timing entry for the request you do.
**Jared Freeze (Palo Alto Networks)** 14:30 Yeah, you're right. I think I… I think I might have mischaracterized that. No one will ever want this. So, it could be odd.
There's… that's not a real person.
**Joaquín Díaz** 14:41 The minimum we should do is… on the resource sign-in API, add the export the URL to the ignore URLs.
by default.
That will break the loop, and then we, if users want that for any reason, they can override it, but I think by default we should do it.
**Jared Freeze (Palo Alto Networks)** 15:02 Yeah, maybe it's just a… a diag.
line.
you know, it's a debug, but it doesn't do any work. And that way.
If you want the full picture, you can go to the debug mode, but it doesn't actually produce.
All this noise.
**Wolfgang Therrien** 15:18 Yeah, I think that sounds really reasonable.
**Martin Kuba** 15:27 So it sounds like the dis- like the… Decision is, like, we should, by default not… not trace or not, collect these URLs, but… But, log them.
In… in diagnostic mode.
So even this would happen by default, even, like, outside of the quick start.
Yeah.
**David Luna Bistuer** 16:01 Okay, thank you. So I'll… I'll hit the issue and… explain a little bit better the situation, and then I'll propose some.
Some changes.
Thank you.
**Martin Kuba** 16:14 Thanks, David.
Right, next one, so there's this, OpenPR… This one is maxime's, I think.
Yeah.
And there's just one pending… Comment… Before this, this is mergable.
Since it's been open for a while, I just was wondering if you can make a decision here.
So, essentially, this is what validated configuration.
If, I guess… We have this invalid config.
parameter that's being set, but, Joaquin, you had you proposed that we just have a more generic one, for failed or start failed, with maybe a message for… Explanation why it failed.
Yeah, so what do you… does anyone have any strong opinions on this?
**Joaquín Díaz** 17:14 I think it's fine to move on, and we can, like, in the future, if we see the need for this, we can add a new parameter.
I don't want to lock the API on this, so I approve. We can take a look there.
**Martin Kuba** 17:27 Alright, so I'm gonna resolve this, and… And we can open. Yeah, alright, cool.
I think it's, ready to merge.
Yeah.
**maxime quentin** 17:40 I'm sorry, I lost track of, some comments.
But yeah, I think we can go… we can proceed on this one.
**Martin Kuba** 17:49 Alright, yeah, I can merge this right now.
Alright.
Jared.
**Jared Freeze (Palo Alto Networks)** 18:05 Yeah, maybe go ahead and open that link.
the fetch Transport in, let's see, LP Exported space… uses Fetch Keep Alive, or Browser, and… Chrome has an interesting choice that they made. I'm not sure if I went over this before, but for new people, if you use no-store on your collector response.
Chrome will not release the Keep Alive budget at the point of reading headers. It's at the point of reading the body.
from my understanding, the reason they made this decision differently from Firefox and Safari is because they were sort of doing it literally.
I don't know if Cleo knows anything about this, so… They… basically, if you say no store, it does not store.
Like, it just… it doesn't hold it. So, until you read the body, it doesn't go into memory.
Which I get, like, okay, cool, it's, like, how they decided to design it, So, it means that you have to drain the body.
Now, we don't use the responses, so what this does is it does not await the drain, which is the previous PR that somebody had put through.
Not everyone is really happy with that. It does work, so this is my modification that releases the body if you're using Keep Alive, and it's got a little bit of logic here to, timeout, and some other things. And so… It wasn't basically, like, some of the pending, byte size and all that stuff was going negative, or… Not releasing at all.
So there… there were just some issues here. So what this does is… this is purely for programming, to not… have requests stall out after the budget is exhausted, if they take too long or something like that, because it would be, an unresolved promise.
And then it just doesn't do anything. It doesn't retry, it wasn't caught, it just… just fell over. We actually had somebody internally, using our vendor SDK, run into exactly this problem and slacked me.
and say, hey, I googled for this bug, and I saw you're actually working on it, so let me know when it's done. And so, Yeah, if you guys want to check this out, Jackson from Ore… looked at the last one, and said he would check it out. But, if you guys wanna see what's going on.
That is the background. The other browsers don't do this. They also have a much higher budget, set 64K. It's set at 60, sort of assuming we're the only vendor on the page.
It's set lower in other places. Century does that, we do that. We can also crank it down a little bit, that would be a different PR. I believe we use 48K.
you know, if people are A-B testing, you know, OTEL with another vendor, you're gonna run out of budget pretty quickly, and our budget number's gonna be wrong. But the browser doesn't tell you that, so that's, like, a service-separate thing, right? If people want to look at this, please do. It will be part of the 3.0 release.
They won't throw up before that.
Correct me if I'm wrong.
I believe the merchant approach. Yeah, I think this is just gonna fall into line with 7002, which was the original Terushu.
**Martin Kuba** 21:56 Alright, any thoughts or questions about this?
**Cleo Schneider** 22:04 I'll poke around and see if it's been reported internally as well.
**Jared Freeze (Palo Alto Networks)** 22:09 Yeah, so I linked to the, the Chromium link, and a Google dev responded, like, this is not a regression, but it is a bug.
I did not respond that I do not think it's a bug. I think the original intent of the author was to, like I said, take no store literally. But you can see in the code, it's a very specific branch. Like, the person who made the last one linked to the Chromium source code and was like, somebody very obviously put this in here. It's not an oversight.
it is just different than the other browsers. So, yeah, I mean, if you have any background, that'd be cool. But I think, you know, it was done years ago, and then.
**Cleo Schneider** 22:45 Yeah.
**Jared Freeze (Palo Alto Networks)** 22:46 person was like, oh, definitely a bug. And I was like, I don't know about that, but we'll see how it shakes out. You know, people are talking about it, so…
**Cleo Schneider** 22:54 Cool.
**Jared Freeze (Palo Alto Networks)** 22:55 Actually, sorry, the link is in the code, it's not in the PR, but I can… I can dig it up and add it this way.
**Cleo Schneider** 23:03 Sweet.
**Martin Kuba** 23:08 Okay, Jared, there's… got one more?
**Jared Freeze (Palo Alto Networks)** 23:12 We can do that last.
**Martin Kuba** 23:13 Yeah.
Maxime?
**maxime quentin** 23:17 Yep, so, like, I was playing a bit with the sandbox, and I've noticed that the navigation timings, instrumentation is not registered properly anymore, so it's not triggering the event anymore.
If I understood that correctly, it's, we have first, a refactor that is needed on the, instrumentation and registration overall.
So, before fixing that, I wanted to know if you needed, like, help, Jared, on peer reviews or anything, or…
**Jared Freeze (Palo Alto Networks)** 23:58 Yeah, definitely. So the branch I have in progress refactors instrumentation base to have a web instrumentation base, and part of the motivation for that was that when you're in your editor, TypeScript is unaware of the browser branch.
of instrumentation. Like, hotel slash instrumentation package. And so, it validates itself against the node version, which is… doesn't exactly do what we need to. Now, this is in-flight changing, because I'm about to remove all the browser branches out of Node 4.
that will also affect us. I did that yesterday, so I'll update next week with, sort of, the status, but, yeah, my thought was that… It's just a refactor where we're using a local import.
So instrumentation-based would move into the browser repo, and we would not rely on it. The one thing I didn't consider that I think might blow up my idea is that registration instrumentations can be called on third-party instrumentations, and people will do that. They may not use the browser SDK purely.
That is a problem. So, I… what I did may be a bad idea. I'll try to… get it up, and so we can just look at it. I'll put up the draft.
yeah, it's just been super busy, so, I'll try to do that over the weekend, and then we can look at it, but, that may be… that may… they may kill the idea, because You'd have to fully commit to doing You know, to not… load anything using the node registration.
**maxime quentin** 25:44 Yeah, makes sense to me, if you… I mean, no need to rush, so I guess I could also try to find a small patch for the current instrumentation, or just wait for your overall refactor.
What do you think? Like, should I, try to patch, current, instrumentation already,
**Jared Freeze (Palo Alto Networks)** 26:05 Yeah, yeah, I would say just fix the bug. I mean, the telemetry matters more than the internus, so yeah, that's a good idea. I will say, too, the other thing, for using the event name, it was more of a pitch. You know, I think I wanted to get some feedback on it. Just… Adding event name to absolutely everything.
I wound up talking… it may have been Trent that mentioned it, but whenever others are using processors that only want to apply to certain kinds of telemetry, they actually match against instrumentation scope.
which is, like, the name of the instrumentation, which makes a lot more sense. So, event name would be more granular.
But then you have to know a lot more about the instrumentation.
So, you know, then you're digging around in source code, or having a look at the docs or something. That may be okay, I don't know how people feel about that, but event name was an attempt to Have something to hook into as a filter.
that was the initial idea, so… I don't know if it's a good idea or not, but, you know, if you have different kinds of blogs that you want to process or something like that, you would… you would look onto it, but… you know, there's no real format, you know, I sort of use the, Dot, the limited impacts, like, attributes and stuff like that, but it's really freeform.
**Joaquín Díaz** 27:32 I don't think there's a hard rule on… Instrumentations and even names being one-to-one.
Big… You can have an instrumentation that has multiple events.
So, in that case… Filtering by… instrumentation name might not be enough, if you want to do something for just a specific event on one instrumentation.
**maxime quentin** 27:57 Yeah, like, that's right.
Navigation could be, like, you have one event when it starts, one event when it ends, or stuff like that, and maybe you still want to have only one instrumentation.
And therefore, you mapping, like, instrumentation name with event names would be, like, complex, so I agree with Joaquin.
**Joaquín Díaz** 28:18 Yeah, I don't think there is any harm on… I mean.
Discrete event names, like, specify even names for each event, and then we have some sort of documentation that says, these are all the events we have, these are the names, this is what they do.
So you don't have to go dig the TSC code, you can just see the name somewhere.
**Jared Freeze (Palo Alto Networks)** 28:44 Yeah, Volt's probably better.
enforce through TypeScript.
Who knows?
We'll just do string, you know, string OR, so you can sort of see what's going on with autocomplete.
**Joaquín Díaz** 28:56 Yeah, even maybe the SDK can export some union type of, like, these are all the events this SDK produces, so you can use that on your processors.
**Jared Freeze (Palo Alto Networks)** 29:09 And of course.
**Martin Kuba** 29:17 Alright, we're pretty much at time. I think Jerry wanted to ask if anyone's going to KubeCon. I also saw that you posted that in the Slack channel.
I'm aware.
**Jared Freeze (Palo Alto Networks)** 29:31 just… You're not going.
**Martin Kuba** 29:33 Oh my god.
**Jared Freeze (Palo Alto Networks)** 29:34 Okay.
Yeah, I have… I mean, I… I have less interest in going if it's not gonna be more Browser people. I mean… No offense, Nared, but…
**Martin Kuba** 29:50 Alright, well, I think, I think that's… that's all for today.
Any last minute thing?
Alright.
Thanks, Cheryl.
**maxime quentin** 30:02 Bye.
**David Luna Bistuer** 30:03 Bye-bye.
