SIG: Swift SIG
Date: 2026-01-29
Duration: 42 minutes
Zoom Recording URL: https://zoom.us/rec/share/8i3zLkDLMZF6RuCAlErpl-bi0mVYNYysjdorSJVpoj_OqheJ63FsUtG5nfTkaZdM.IgGXZ9Zybsdkvamk
============================================================

## Zoom Recording Transcript

**Vinod Vydier** 04:50 Hi, Billy.
**Billy Zhou** 04:57 Avenant.
**Ariel Demarco** 05:00 Hey, guys!
**Billy Zhou** 05:01 Great.
**Ariel Demarco** 05:09 It's cold out there, Vinod?
**Vinod Vydier** 05:11 Oh, yes, very cold, and
I also happened to hit a wall.
Literally.
So, yeah.
**Ariel Demarco** 05:27 You know, I'm suffering the summer from Buenos Aires, but I was looking at the images from U.S. and Canada, and all the snow, and the frozen rivers and places.
Even though I don't like the heat, I think that that frozen area is not great to either.
**Vinod Vydier** 05:46 Yeah, yeah, yeah, yeah.
Yeah, you don't… you don't get much cold there at all, right? In Buenos Aires?
**Ariel Demarco** 05:53 Yes, but… like… I don't… I… in June, July…
**Vinod Vydier** 05:59 Yeah, yeah, yeah.
**Ariel Demarco** 05:59 Those are the most, cold months of the year, maybe August, depending on the year.
But the rest, it's kind of cool, the weather. I'd say that spring is the best moment, because sometimes in autumn, we still have the heat from the summer, so you are in autumn, and there's, like, I don't know, 28 degrees, 25 degrees with a bunch of.
**Vinod Vydier** 06:23 a few.
**Ariel Demarco** 06:23 BDD, so not so great.
**Vinod Vydier** 06:26 Yeah.
**Ariel Demarco** 06:28 Hey, Nacho.
**nacho** 06:29 Hello?
**Ariel Demarco** 06:33 How are y'all?
**nacho** 06:38 Sweet.
**Ariel Demarco** 06:41 rate.
**Vinod Vydier** 06:43 Yeah, I was there in July, so that was probably the coldest time, and it is
Yeah, it was not that bad.
No, it's… it's…
**Ariel Demarco** 06:53 cold.
like, quote-unquote, cold, like, compared to the cold in the US? No, it's not cold.
there are some states in Argentina that they have, like, snow, mountains, and they are really, really cold, and the weather could be, like, I don't know.
5 degrees… minus 5 degrees Celsius.
**Vinod Vydier** 07:12 Yeah. Oracle.
**Ariel Demarco** 07:13 flight 8, but the other day, I was talking with one friend from Chicago. They have, like, I don't know, like, minus 30 degrees Celsius? That's… that's, like, Antarctica.
Anyways… I create an entry on the agenda.
Wasn't here last week, so… probably I'll need some help from you guys to know.
**Vinod Vydier** 07:45 Yeah, I was also not here last week, the week before, yes, but .
**Ariel Demarco** 07:53 Share the screen.
Right. Bryce is not here, so… be not.
**Vinod Vydier** 08:06 Bryce said he's gonna join a few minutes late right now.
**Ariel Demarco** 08:10 Team.
So that… topics from… Last week…
These ones…
Bye-bye.
Like this.
Huh.
Like this.
And I'll include these ones, just in case.
Okay, so… We shall start.
Is there any new topic to include?
**Billy Zhou** 08:52 I don't have any new topics today.
**Ariel Demarco** 08:55 Okay, I'll include, Utilization, well, socket.
updates.
Okay, so crash reported feedback, this is… I think EOPR?
**Billy Zhou** 09:12 Yeah, for both my items, I didn't make progress. It's been kind of a hectic week, if you saw the news.
But, yeah, I'm gonna put out revisions for both of these today.
There's a lot of feedback on this, so I'll put out a revision.
**Ariel Demarco** 09:32 Okay, cool.
just in case, if you… if you need some… some help on the feedback from… from Alex, I can help you out. Most of the things that he mentioned is… are things that
We had to go through, when… when we did the implementations ourselves, so…
Feel free to… to reach out.
**Billy Zhou** 09:51 Oh, cool. Yeah, thanks, thanks, Harry.
**Ariel Demarco** 09:54 Okay, so… Good luck.
update that.
Okay, reviewed, this one… I don't know, what is this?
Somebody that was last week, remember this.
Ensures with implementation of environment context. Hey, Bryce!
Hmm, you're busy, I think.
**Bryce Buchanan** 10:32 Yeah, sorry, do you mind running it? I've got a,
I've got a, trainee here.
**Ariel Demarco** 10:38 Yeah. Oh.
Do you remember about this, Bryce? Ensure to shift implementation of environment context propagation matches the specific engine?
**Bryce Buchanan** 10:50 Oh yeah, we… we saw this last week. I believe what happened was, is the, the spec has been updated or extended, and we just need to, review that and, and update it.
**Ariel Demarco** 11:07 Okay, okay. Maybe we should link to…
to the… to an issue of the tracing. Maybe it's part of also the tracing spec.
Or not.
**Bryce Buchanan** 11:27 Environment?
**Ariel Demarco** 11:28 I don't remember.
**Bryce Buchanan** 11:28 I think the link there,
that, context propagation. I believe that that… yeah, here.
**Ariel Demarco** 11:37 Yeah, that's for all languages.
**Bryce Buchanan** 11:39 Yep, yep.
**Ariel Demarco** 11:42 Yeah, okay.
Okay, cool, so this one is already reviewed, I'll just remove it, just in case.
This one, fix OSF, OSSF card issue, says that you'll get this fixed. I don't know if you could do it, Bryce.
**Bryce Buchanan** 12:00 I believe that was fixed.
**Ariel Demarco** 12:04 Cool.
Done.
Great. And… last one… these… Rebase of Swift 6, seems you weren't able to do it,
Really?
**Billy Zhou** 12:24 Yeah, both my items say I wasn't able to make progress. I'll do this after the KS crash revision.
**Ariel Demarco** 12:30 Okay, cool, no worries.
Things happen.
getting back to work on January after all the…
party on December and November for US guys. It's complicated, so I understand.
Okay, cool.
Related to new topics, topics. I've been doing some work on the Euro session WebSocket.
It wasn't as easy as I expected. I thought it was just going to be a simple Swiss link and capture all the data, but it's not as easy as I expected, because all the Swift APIs are async await.
And they… and they… they don't expose
the object… and they exposed object, sorry, that are Swift only, so you cannot twistle them.
So, I… I'll do… I have two plans. I'll see which one is better.
I found out, while investigating the underlying things, that there are classes that both Objective-C and Swift uses, because if you use Objective-C, you can use URL session WebSocket, that is NSession WebSocket.
So, there's a middle class that is private, that we could whizzle, and we'll get all the methods. And the other one is just whizzle the Objective-C methods.
that they accept any object, so I would cast…
the message in Swift to an NS object, random NS object, and see if that works. I'll test both aspects, but I'll… I'll probably include all these
investigation in the issue, just in case, in the future, my decision doesn't work for some cases. At least we have information on what I did to investigate, and also why I made some decisions.
So, that's basically it. It wasn't as easy as possible, as I expected, to be honest.
**nacho** 14:31 So it was not a wrapper on the Objective-C classes as it was for the standard URL session, right?
**Ariel Demarco** 14:40 Yeah, because it's available only from iOS 15 and onwards, so a bunch of those methods are
tightly bounded to Swift, and the bridge is not as common as it is for all URL session methods.
But it's feasible, in… there are two ways to do it, as far as I could test. I'm just…
Trying to… to see which one looks better and seems safer.
I'm doing it in the same way URL session instrumentation works, like, I have the… I include this in the URL session configuration, it's disabled by default.
following Nacho's advice, I'm creating a spam.
with span events for send, receive, and pings.
whenever you ping unpong to the server, And…
There's an optional delegate that you can use.
So if I use that delegate, I will also include the span events for the connection actually started and the connection actually closed.
But the span is going to work itself whenever I create the task.
and ends when the URL session delegate, the common one that did complete with error, returns that the socket connection is closed. So…
That's… that's basically it. I'm going to try to explain everything in the issue, and some part on the… on the PR.
**nacho** 16:16 Yes, thinking about that, for example, for the async methods, we are using a fake delegate.
Or the standard URL session.
to capture things. Maybe that's an approach that you can use for this, and just swizzling the delegate?
If it…
**Ariel Demarco** 16:34 Yes.
**nacho** 16:35 a class from Objective-C or something like that. Maybe that's… because maybe with… with async methods, what happened is that they are also Swift only.
So, we didn't have access to that. So…
maybe what we see here is that Apple has used the same approach, both for the standard URL session and the WebSocket, that they have an internal, maybe, Objective-C class, as you… or a private class, as you said.
Yeah.
So maybe that could also be a way to properly swizzle.
the rest of the async methods, if you find something there. So, yeah.
I think that that's really interesting.
**Ariel Demarco** 17:17 Yeah, yeah, yeah, yeah, yeah, I'm… I even… I'm even doing exactly the same that we are using in the URL session instrumentation, that I go and check all the classes loaded in runtime to replace those methods.
The only bad thing is that the Euro Session WebSocket Delegate has only two methods. It's only to the open connection and the close. There's nothing, like, intermediate, like, you receive something, or you receive the pong, or something like that. There's no… there's… there's nothing. It's like…
pandemic to my… to… to…
**nacho** 17:50 to me. Yeah. But…
**Ariel Demarco** 17:52 I understand the why, like, if you see that your session WebSocket APIs in Async await are super easy to use, it's, like, send, receive,
whenever you receive, it's a stream, so it's easy to iterate on the async stream. So, I understand why there's no real need for that in actual Swift.
And in Objective-C, you still have the complexion-like APIs, so it's kind of covered.
So, I don't know, I'll try to do everything as possible, like switch all the delegate in the way we do it for the URL session instrumentation, try to capture those events that happened in between, like the send, the cancel, the ping, and the pong.
And see how it looks like. But that's basically it. Just saying that it's taking a bit longer, because I thought it was going to be easier, to be honest.
**nacho** 18:46 Same.
Yeah, with the async version, we also have that problem, that we don't receive any other delegate method.
Except the final one, and we recreate everything there. So yeah, maybe if you find a private class, that really helps us, I don't know. For all… for all the methods, because we have some limitations now with the async methods.
Yeah, we have a corner case there for some… for the transmitted things, and how much it has been sent.
By this.
Oh, yep.
**Ariel Demarco** 19:19 Same thing happens on Embrace, like, we have those as in methods, and we don't know how much data has been received and sent, so…
**Billy Zhou** 19:28 Yeah, I have a quick question. Are there, semantic conventions for WebSocket protocol?
**Ariel Demarco** 19:35 Oh, around that. I created a separate extension for semantic conventions for this, because there's nothing related to WebSockets. I basically saw different implementations and different proposals, and kind of merged all that stuff in between.
And that's basically it, but…
whenever I raise the PR, there's nothing written in stone, and there's nothing really official, so we can discuss ourselves which is the naming convention we could use.
if there's an attribute I'm missing, or something you'd like to see, I made everything, like, super configurable, so, I don't know, you can configure the possibility to receive pinks on pongs, the possibility to receive the callback whenever you receive data, I don't know, like.
**nacho** 20:26 I'll…
**Ariel Demarco** 20:27 All that stuff, it's configurable.
So…
**nacho** 20:31 Yeah, I was… yeah, maybe… I was thinking now something that came to my mind now about WebSockets. Yeah, that… that's something that also happens with URL session instrumentation, but here with WebSockets can be a bit more…
tricky. The thing is, If you are…
having a communication, and you are a session, and you start the span, and the app closes or crashes.
Especially crasses. While… or the user quits very quickly, you lose… Yeah.
the end of the span, and so you lose the span itself, because it's never serialized, and it never arrived. With a WebSocket, we have many more possibilities
of that to happen, right? Because the WebSocket is gonna…
**Vinod Vydier** 21:19 Leaf.
No.
**nacho** 21:21 It's gonna live… Probably the same time the app is leaving.
So we have the risk of that. I don't know if we… If that can be…
Try to minimize from the…
or something like that. I don't know. Just as a… it just came to my mind as a wild, thing.
**Ariel Demarco** 21:46 Yes. Yes, I was thinking about that when I was doing this. There are two things that we could do. One of them is flashing, and allow flashing every 10 seconds, or allow manual flashing of that span.
So, even though you don't have the complete span, you have the span with all the events inside of it.
That were generated at some time.
And obviously, it will depend on the processor, on the exporter to actually understand, oh, this is not ended, or this is, this is actually finished.
**nacho** 22:20 the spans are being processed on the end, in the current API.
We only process them in the end.
No, that's what.
**Ariel Demarco** 22:32 We purchased them, we…
We process them in both, like, we have the on start and the on-end. The implementation of the, for example, the simplest span processor, it actually exports them on the on-end, as you mentioned, but I don't know if somebody wants to flash it, like, they could just flash.
**nacho** 22:51 It can be done earlier, that's true, yeah.
**Ariel Demarco** 22:54 I don't know, the other way, or the other thing I was thinking about is maybe instead of having span… spans, like, just having events, or span… or log… or logs, or something like that…
**nacho** 23:06 looks. Yeah, yeah, yeah, that…
I think that's the reason that they came with these logs for the sessions, right? At the beginning, is because they couldn't keep this panel alive, and you lose those things.
**Ariel Demarco** 23:19 Exactly.
**nacho** 23:20 Yeah, I mean, yeah, it's not related to your peer at all. It was just that came to my mind that that's something that
That's a use case that… that's always there. That… yeah.
Yeah, or maybe we can work on… on…
helping in that issue, also in the API, instead of having to…
Let the implementers, or the users of the library just to try to… abducts.
**Ariel Demarco** 23:47 Yeah.
Yeah, I agree. I think it's a limitation from mobile, where everything would crash, or will terminate at any moment, so…
Yeah.
**nacho** 23:57 This is something…
**Vinod Vydier** 23:58 One more thing about WebSockets, I… I have to, you know, occasionally look at,
On the browser side, on the… WebSocket communication on… on the… product that I work on.
And there's a lot of binary messages there.
Is this something that is, we need to take care of, as opposed to the…
**Ariel Demarco** 24:21 I'm… I… I'm including, like, what type of data I'm sending, and the size of it.
and the protocol that it's using. I'm including that when I'm gathering the information.
I'm not actually…
sending in any attribute, like, the information that is being sent or that I'm receiving for PII and basically security concerns, but that's something we could even take care about, or maybe make configurable, if we want to.
I think the amount of information will be huge if we do that.
**Vinod Vydier** 24:58 Sure, yeah.
**nacho** 24:58 Yeah, probably for the WebSocket, it's gonna be too much.
**Ariel Demarco** 25:03 Yeah.
But, you know, it's a verbose instrumentation. It will probably generate verbose data in some cases, so it will be up to the client using it to configure it properly.
But… That's on them.
I'm trying to make it as configurable as possible, so they can actually tweak in those situations, all the things that they gather, if they want a gathering, if they want to push them, include them, blah blah blah.
**nacho** 25:35 Yeah, because for debugging purposes, it's useful, yeah, sometimes to have that information.
Yeah, exactly. In a controlled SN… Place, but yeah.
**Ariel Demarco** 25:46 Yeah, you receive messages, and some messages you really care most more than others, so maybe it's good to have the possibility to filter out the others, and just include whenever I receive those type of events.
That's why I was thinking in my mind. We have some customers asking for it on an embrace, and sometimes it's kind of difficult for them to understand what they want to see of this, so…
I think it's… the capability of filtering, I think it's one of the most necessary things that they'll have to deal with, like, how they are going to filter the amount of information this provides.
**nacho** 26:31 Yep.
Even sampling, or some… something like that, for…
**Ariel Demarco** 26:35 Yeah.
Totally.
So, that's my update.
**nacho** 26:42 I don't know if there's new issues…
**Ariel Demarco** 26:44 Let me go and see.
If… If there's anything new, open the Swift.
Want to obligate.
So we have there.
First of all, PRs.
There's nothing new.
Just… this… 4 days ago, related to Swift NI.O. and people request action.
What are we doing with the Swift NIO? Any update like this, we just included, isn't it? If everything works fine?
**nacho** 27:23 This is a landulous library.
Because it has… other Apple dependencies in between.
So, yeah, I don't know.
They must retake with care, because we might be limiting our tadien.
Persians that we support.
Depending if… on… on…
on how… what we update, that's… that's a problem. Especially with this library, I don't know.
Yeah, this… this… this is something difficult to… to really know.
**Bryce Buchanan** 28:08 Yeah, these updates skipped the tests, so this one is a little bit sketchy.
**Ariel Demarco** 28:13 Hmm.
I'll download this branch and see if everything runs correctly on the test, and if everything works fine.
I can approve it, merge it.
Do you guys agree?
**Bryce Buchanan** 28:29 Yeah, that sounds good. Thank you, Ari.
**Ariel Demarco** 28:33 I'll assign this to myself.
So I remember that.
And this one is create pull request action. This seems simpler, I think.
**Bryce Buchanan** 28:41 This one could just be merged.
**Ariel Demarco** 28:43 Yeah, I'll just approve it.
I hate when I'm on… on my Mac monitor.
Only, and, like, Zoom has a bunch of windows everywhere.
**Bryce Buchanan** 28:58 Water.
**Ariel Demarco** 29:01 Have to move everything out.
**Bryce Buchanan** 29:03 I don't have enough monitors, I don't think. Like, one plus the laptop, not good enough.
**Ariel Demarco** 29:11 Well, cool. So the others are the ones that we reviewed, and…
This one is Saproot, I think?
**nacho** 29:18 Hi.
I, I reviewed it.
yeah, as it was yesterday, I didn't merge, because maybe you want to… it's just changing some print methods to call the… the callback.
of the library, instead.
**Ariel Demarco** 29:37 Feedback hand.
**nacho** 29:38 Into us.
**Ariel Demarco** 29:39 fit.
I think we can just merge it.
Oh, still, running this.
**Bryce Buchanan** 29:45 Oh, interesting.
That's weird.
**Ariel Demarco** 29:49 Let me check out.
**Bryce Buchanan** 29:52 Is it appropriate?
**nacho** 29:52 We started 46 minutes ago.
**Bryce Buchanan** 29:54 Oh, interesting. That's weird.
**nacho** 29:57 Did we have some change on the code? Someone pulled something? Committed?
**Ariel Demarco** 30:04 Oh, I just… I just merged the PR, but this is 45 minutes ago.
So, this is weird.
I'll take a look.
**nacho** 30:16 Cut.
**Ariel Demarco** 30:18 blind.
It shouldn't take that long, though.
**nacho** 30:23 But it… I… it was approved yesterday. Did he commit anything after?
**Ariel Demarco** 30:30 Not at all. Not really.
The only thing was this switch to github.com, OpenTelemetry, open telemetry, receive fork.
**Bryce Buchanan** 30:41 Just mentioned pull request there.
**Ariel Demarco** 30:44 Maybe that was the thing that triggered this?
I don't know.
**Bryce Buchanan** 30:52 It seems like it's… it looks like the build just took a really long time for some reason.
**Ariel Demarco** 30:58 Yeah.
**Bryce Buchanan** 30:59 But it just finished, and it's on to the next step, so it should complete.
**Ariel Demarco** 31:05 Okay.
**Bryce Buchanan** 31:05 But that's really bizarre that that took so long, I wonder why.
**Ariel Demarco** 31:10 Maybe on, on…
wasn't actually on the compilation, but waiting for the runner. Could be. I know you guys, but this… this week, I've been having, like.
really, really long day with GitHub Actions. I don't know if it's something from the runners I use, or what.
But, maybe that's the case, and why it was so slow.
Let me go and see… This was the CoQL analysis.
Yee… Yeah, some of them are taking super long.
Let me go and check it out.
Yeah, most of the times, whenever this is the cold QL, it takes…
**Bryce Buchanan** 31:57 It's a build.
**Ariel Demarco** 31:59 For some reason, it takes a long time to actually do.
**Bryce Buchanan** 32:02 Is it… is there a breakdown in that job… in that sub-job that shows, like, maybe what is taking all that time?
**Ariel Demarco** 32:12 Inside, you mean the… In the building.
**Bryce Buchanan** 32:15 the Belgium.
In this step, you mean? Yeah, in the build step, yeah, sorry.
**Ariel Demarco** 32:23 No, there's no breakdown in what is taking that long, but we… we can include some logging here to actually understand where on earth it's taking too long.
I kind of…
**Bryce Buchanan** 32:35 Either one… maybe we can go take a look at one that's active right now and see.
**Ariel Demarco** 32:46 Mmm, it's really…
**Bryce Buchanan** 32:46 weird.
**Ariel Demarco** 32:47 It's a simple build.
**Bryce Buchanan** 32:48 Oh yeah, the build… the build didn't take long. A hundred… yeah, wait, hold on, how long is that? That's actually…
**Ariel Demarco** 32:57 180… That's 30 minutes.
Kinda.
**Bryce Buchanan** 33:02 Wow, yeah.
**Ariel Demarco** 33:03 This is 30 minutes on the building.
**Bryce Buchanan** 33:06 But then another 15 minutes on…
**Ariel Demarco** 33:09 fetching.
**Bryce Buchanan** 33:10 Yam.
**Ariel Demarco** 33:12 Because it does the fetch, then set up everything for the compilation.
And then it starts the building.
**Bryce Buchanan** 33:21 That's…
**Ariel Demarco** 33:22 That's weird. What, what.
**Bryce Buchanan** 33:24 I wonder what runner it's on. Can you look at the setup job?
**Ariel Demarco** 33:28 Yeah, yeah, yeah.
It's, work recommended.
**Bryce Buchanan** 33:34 Line 13.
**Ariel Demarco** 33:36 Run image… It's macOS 15.
**Bryce Buchanan** 33:39 Hmm.
**Ariel Demarco** 33:40 Alright, I'm on 64.
**Bryce Buchanan** 33:45 Oh, West.
**Ariel Demarco** 33:47 This one… shouldn't be.
**Billy Zhou** 33:49 Happening every time, or just… just went off?
**Ariel Demarco** 33:52 Yeah, no, it's happening a lot, like… Oh my god, I bet.
It's happening a lot, like, if you see most of this one?
**Bryce Buchanan** 34:02 Yeah, they're all kind of…
**Ariel Demarco** 34:03 Cardio?
**Bryce Buchanan** 34:05 Go to the… can you go to the build and test?
**Ariel Demarco** 34:09 Yeah, sure. Building tests.
**Vinod Vydier** 34:13 Those ones are, whenever they are running.
**Ariel Demarco** 34:17 14 minutes.
**Bryce Buchanan** 34:18 Can you… can you dig into that and look at the runner on there?
**Ariel Demarco** 34:22 Yeah, sure.
Should run… they're running in parallel, let's go to iOS.
Startup job.
Runner image.
Same one.
Exactly the same one, yeah.
**Bryce Buchanan** 34:39 Weird.
**Ariel Demarco** 34:40 Yeah, maybe… I don't know… I haven't looked at the CloudQL workflow, to be honest.
So… It's running this action.
A single field.
**Bryce Buchanan** 34:58 Hmm…
**Ariel Demarco** 35:01 And what we do here?
We just…
**Bryce Buchanan** 35:05 This one's a little more complicated.
**Ariel Demarco** 35:07 Yeah.
Swift test.
Yeah, Swift test, Swift build… make build for testing.
**Bryce Buchanan** 35:16 Yeah.
**Ariel Demarco** 35:19 I can take a look and see why on earth it's taking too long, do you understand?
It's weird, shouldn't take that.
**Bryce Buchanan** 35:28 Do we need to build it to run the CodeQL, or…
**Ariel Demarco** 35:34 As far as I understand, yes.
Because it reads a bunch of stuff from the… from the build resource… folder result.
So…
What I don't know is what does the first one, if it does static analysis here, and then it does some analysis of the output here. That's why I would… I would want to understand.
I'll take a look and see why it's taking that long.
**Bryce Buchanan** 36:05 Yeah, I wonder if we can, like, one optimization is we could pull whatever, whatever the CodeQL needs from an existing build, since it's all doing it together.
Yeah.
**Ariel Demarco** 36:20 Yes, you can use the GitHub Action Cache.
**Bryce Buchanan** 36:23 Yum.
**Ariel Demarco** 36:24 Are we using it in any job?
**Bryce Buchanan** 36:26 I don't think so.
**Ariel Demarco** 36:28 If that's the case, we can improve this one, as seems to be the slowest.
**Bryce Buchanan** 36:34 Yam.
**Ariel Demarco** 36:37 Other stuff would be, like, downloading the Swift package dependencies, so whenever we Swift build.
We get the ones from the cache.
If everything…
**Bryce Buchanan** 36:47 Yeah, that's a… that's another… Another solution that could improve it?
**Ariel Demarco** 36:53 But…
I'll just… I'll add some timer to understand what on earth is taking that long, either in the Swift build and in the CodeQL analysis, because…
That's weird.
**Bryce Buchanan** 37:04 Yeah, that is weird.
**Ariel Demarco** 37:06 But well, it finished, so I'll merge it.
Okay?
The other one… This one is changes requested.
Let me remove all of this stuff already.
The OTLP, Tracy's border…
What were the comments? I made none of the comments. Okay, this is waiting on myself.
Anne, you mentioned this pull request.
Okay, I understand. Okay, I'll take a look at this afterwards.
I had to really check all the changes.
And… This was for an open image space.
And I think that's it. The other one is the Crash Reporter, the Swift 60, on the Rinme.
This was from you, Vinod.
**Bryce Buchanan** 38:09 I think that there's still some, some conflicts that need to get… It looks like this can.
**Ariel Demarco** 38:14 life.
**Bryce Buchanan** 38:18 Yeah.
I'm not sure what that is… Beautiful.
**Ariel Demarco** 38:25 This one is weird.
**Bryce Buchanan** 38:27 We have to upload.
**Ariel Demarco** 38:28 two approvals from Nacho, like, it's doubly approved.
**nacho** 38:33 Oh, really?
**Vinod Vydier** 38:33 Yeah, this is… this is.
**Bryce Buchanan** 38:35 Oh, that's why, that's why. Yeah, there's a conflict that needs to be resolved, that's the only…
**nacho** 38:40 Okay.
**Ariel Demarco** 38:40 Okay.
**Bryce Buchanan** 38:41 Ram.
**Ariel Demarco** 38:43 Okay. I have been reviewing the, sorry, the cold QR.
**nacho** 38:47 code QL, thing, and I have seen that we are… Text code building.
In the build, in the make, standard make, and we… and it runs scripted milled.
In the ocean. Maybe it's just…
Not selecting the proper… it's building for all the architectures, or something like that.
**Bryce Buchanan** 39:13 Oh, okay.
**Ariel Demarco** 39:14 Yep.
**nacho** 39:15 It could be that.
**Bryce Buchanan** 39:17 Yeah.
**Ariel Demarco** 39:18 Okay, we can just start with just a… using make instead of the SwiftBuild, and see if CodeQL works. Maybe CodeQL needs to use SwiftBuild, and that's the problem.
That's why…
**nacho** 39:30 Yeah, but maybe we can select just some, some, some architecture or something like that.
Or some, target.
That it probably doesn't need watchOS target yet.
And that's another totally different.
**Ariel Demarco** 39:46 architecture, and probably also different iOS and Mac, if we…
**nacho** 39:50 Vision out of them.
**Ariel Demarco** 39:52 Yeah, you're right.
Okay, I think that this needs to be resolved conflicts, but feel free to ping Vinod whenever you do the modification, so we merge it and this doesn't happen again.
**Vinod Vydier** 40:04 Yeah, I can…
**nacho** 40:06 Yeah, I can approve a third time if you want.
**Ariel Demarco** 40:14 Cool.
Okay, so moving to OpenTeamis Swift Core.
We have PRs… This one…
**Bryce Buchanan** 40:24 Oh yeah, this one just needs to be merged. This was the issue that.
**Ariel Demarco** 40:30 Oh, yeah, we included that.
**Bryce Buchanan** 40:32 Yeah, so the semantic conventions was accidentally merged as a submodule, because the, the, the script that generates the semantic convention, files for the agent.
Pulls down the semantic invention repo, so somebody just, you know, added it on accident.
**Ariel Demarco** 40:54 Yeah, no problem.
And this one is…
**Bryce Buchanan** 40:57 A follow-up to that would be to have the script clean it up at the end.
**nacho** 41:02 Or, or add it to the gitignore.
**Bryce Buchanan** 41:05 Yeah, that's a good idea, too.
**Ariel Demarco** 41:09 I think this one needs, again, the same thing that happened with Minab to be updated, Billy, so…
Oh, I think that… Okay, got it.
**Bryce Buchanan** 41:21 I think that that other PR, needs to be… it needs to be pulled, and that should probably fix it.
**Ariel Demarco** 41:30 Which one, sorry?
**Bryce Buchanan** 41:31 The, the, the issue,
In that… in that docs update.
**Ariel Demarco** 41:39 Oh.
**Bryce Buchanan** 41:40 The reason why it's not… the build isn't working, I think it is related to the submodule thing.
**Ariel Demarco** 41:48 Okay, so he should pull right now what is happening.
**Bryce Buchanan** 41:52 Yeah, yeah, and then…
**Ariel Demarco** 41:53 Okay, understood. My bad.
On these ones, no new issues, and on… the Swift…
This one was opened last week.
Yes, it's the one that we just…
So, this one is the Euro Session Instrument WebSocket.
That's the one I'm going to do.
And I think there's no new issues.
**Bryce Buchanan** 42:24 Cool.
**Ariel Demarco** 42:25 So, anything else?
**Bryce Buchanan** 42:29 Nope, I don't have anything.
**Ariel Demarco** 42:32 Okay.
So, I think we can get 20 minutes back.
**Bryce Buchanan** 42:36 Cool?
Alright, everybody.
**Ariel Demarco** 42:38 Nope.
**nacho** 42:39 Okay.
**Ariel Demarco** 42:40 See ya, have a nice week.
**Bryce Buchanan** 42:41 Yeah, bye-bye.
**nacho** 42:42 Nice weekend?
**Vinod Vydier** 42:43 Thank you. Bye. Bye.
