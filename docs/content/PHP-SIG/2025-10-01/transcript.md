SIG: PHP SIG
Date: 2025-10-01
Duration: 23 minutes
Zoom Recording URL: https://zoom.us/rec/share/yMOO2XVo5LGKnWnPv9M5CL-61ZadsVs6neVwpS9T2EBRUECKfy1Z924TQfuWAUx3.k-XVLHd6SYARF__c
============================================================

## Zoom Recording Transcript

**Chris Lightfoot-Wild** 01:20 Hello.
Hey.
Oh, sorry, I don't think I can hear you, Brett, if you are there.
Oh, is it in April? Are you there, buddy?
**Brett McBride** 01:37 example.
I'm here. I'm here.
**Chris Lightfoot-Wild** 01:40 boom.
**Brett McBride** 01:40 Okay, I can hear.
**Chris Lightfoot-Wild** 01:44 Nice, I can hear you as well.
**Bob Strecansky** 01:46 We can hear you.
**Brett McBride** 01:47 You can't hear me?
Oh, good. Okay.
**Chris Lightfoot-Wild** 01:55 There's been, like, a bit of a downturn there or something, Bob? It's looking a bit quiet.
**Bob Strecansky** 02:02 Oh, this is… yeah, we, we, like, move desks at work. I'm just in a different desk.
Okay.
**Chris Lightfoot-Wild** 02:09 Oh, there you go, this is a cousin. You know him.
**Bob Strecansky** 02:12 Hold on, let me…
**Brett McBride** 02:13 You can see someone in the background there.
You feel like you're in, like, an aceman.
**Bob Strecansky** 02:17 See if I can unblur.
Where is that?
I don't know.
Probably here.
Yeah, that's about as… these cameras that they have are not good. Yeah, it's like… this is the… you go around the corner here, there's, like, conference rooms and then a kitchen here, so it's kind of nice. It's a good corner… good corner office. The only problem is there's a pool right outside my window, so I, like, watch people swim all day, and it's just…
Defeating.
**Brett McBride** 03:00 Hello, Powell.
**Pawel Filipczak** 03:02 Hey guys.
**Bob Strecansky** 03:13 Happy October, everyone!
**Brett McBride** 03:17 Great to be here.
**Bob Strecansky** 03:19 Where did this year go?
**Brett McBride** 03:23 That's gone pretty quickly.
**Bob Strecansky** 03:25 Well, you're in fast-forward mode, Brett, with a new baby. I feel like that always makes it go even faster.
**Brett McBride** 03:31 Yeah, yes. I've done absolutely nothing this week. The only thing I need to achieve is…
Getting my annual review done.
And then I… yeah.
I'm ready to moonwalk out for a year.
**Bob Strecansky** 03:47 Oof.
That's so nice that you get that. Like, I felt so… I felt so fortunate that we got 3 months here. Like, that's crazy for paternity leave here.
You just eclipsed it by 4 times, which is…
**Brett McBride** 04:08 Yes.
**Bob Strecansky** 04:11 Alright, can y'all see my screen okay?
**Brett McBride** 04:13 Ken?
**Chris Lightfoot-Wild** 04:14 Sweet.
**Bob Strecansky** 04:14 Alright.
I don't expect anybody else to be here. I'll…
We don't have all the usual suspects, but that's okay, maybe they'll… Maybe a little time later.
Alright, chris, would you like to talk about logging again?
**Chris Lightfoot-Wild** 04:30 Yeah, sorry, I did put again, because I know I've asked the question previously, and I did… I think it was over a year ago now, I added a question to the…
the hotel, login channel, but it didn't really go anywhere. But then I just noticed by chance that, Python, SIG had some discussion around
Kind of introducing…
the log level… because there's already an OTel log level environment variable, but it applies, like, specifically to the SDK.
But, for one, more specific, perhaps, to auto instrumentation.
So I don't know… it feels like maybe it's…
fairly experimental concept, as it's not landed there. But if you look at our PSR3 login.
typically, if you're using, like, monologue, as I guess most things do, They do call out to…
You know, you might call the debug method, which then wraps the log abstraction
But then, in the PSR logger, it is omitted anyway, from the debug level?
But you might have it not handling that level in, like, your replication code. You might have configured it to, you know, 1 and above.
So I just wondered if there was a way we could suppress the lesser levels, because I…
Don't think we've got any concept of doing that at the moment.
I mean, Bob, you… sorry, not Bob, Brett, you've perhaps used the…
Having written the instrumentation, you probably know this a bit better than I do.
Have you got any opinions on…
**Brett McBride** 06:15 Ink?
**Chris Lightfoot-Wild** 06:16 We could head in that direction.
**Brett McBride** 06:18 Yeah, so I think that there's… There's… there's an enabled…
feature that's been added to spec, probably in the last 6 months or so, that we have. I think that that…
applies to the logger as well. And…
Oh, from memory, you sort of… you meant to…
You're meant to call it, and it'll tell you whether the logger is enabled for, you know, the input, which
I think could be level for logging.
Does that make sense? .
**Chris Lightfoot-Wild** 06:56 So then, I guess, is it… is it a declarative configuration at the moment to…
change the log level that we're capturing, or… I guess, would that be the…
Would you like to not just grab everything?
**Brett McBride** 07:11 I don't think it would have to be in declarative config, no.
Hang on, I wonder what I'm trying to look for?
Yeah, so in our logger interface now, we have an is enabled and one of the…
One of the parameters to it is the severity number.
So, can we use that?
**Chris Lightfoot-Wild** 07:40 So, potentially, we just update the…
PSR3 instrumentation. We'll test that out, that it works with the… is enabled.
**Brett McBride** 07:49 Yeah, we've got to check what the actual implementation is in the SDK, of course. Let's have a quick look now.
Hmm, I think there's probably some more…
I think it uses a configurator in there, so… so possibly, yes.
I think that would be the mechanism anyway, even if the implementation's not…
Sort of ready out of the box now.
But, I think that's the way to do it.
Because you… you really sang, you know…
and I think it says in the spec, you know, you should…
You should call this method before you, before you try to, you know, before you do any work, or try to send it on.
**Chris Lightfoot-Wild** 08:48 Good.
**Brett McBride** 08:50 Yeah.
Yeah, I think that's the thing to look at.
So, but just to go back, the problem statement is that if you've got the OTL log level, say, set to warning, but you're emitting debug messages, then they're…
not being… Like, those debug messages are coming through in…
Open telemetry, because we're not looking at,
We're not doing anything with that log level.
**Chris Lightfoot-Wild** 09:22 Yeah.
**Brett McBride** 09:23 Yep.
**Chris Lightfoot-Wild** 09:26 Yeah, so the good side of that is that we're getting close-ish in, like, work terms, so that probably means months away, but, from, you know, going to production with some hotel stuff, so…
Yeah, locally, loads of debug messages are fine, but it will just flood.
Production. So, yeah, it'd be good to try and address it before we get to that point. That's why I was, raising it.
**Brett McBride** 09:53 Yeah, yeah, absolutely. I mean, that seems like it should be an integration test on, you know, the… the logger. You're probably talking about the PSR3.
Sort of auto-instrumentation mechanism.
It feels like it should be, like, an integration test, if not a unit test.
Against that, because it… Yes, what you're describing is unexpected. You know, if I've…
log level to warning, I should be only seeing warnings and above.
**Chris Lightfoot-Wild** 10:25 Alright, thanks for that one. I'll… I will look into that.
Thanks so much.
Well, sorry, I should have said the overall thing as well, for the liveal instrumentation, I would like to rely on
the PSR3 logger as well, rather than the log… events.
admitted.
Because it looks like, obviously, we're just duplicating the functionality otherwise.
Some of the context flattening stuff at the moment, on the LyraL side is just JSON encoded.
You can't use those, sort of facets to, you know, further filter, on the…
On the back end.
Whereas when they're flattened down properly, in, you know, key-value pairs.
And I think the PSR3 blogger already does that, so…
**Brett McBride** 11:18 Yep.
Yep.
**Chris Lightfoot-Wild** 11:22 Go with what's better, so… Sorry, that was it, stop runton.
**Bob Strecansky** 11:29 No, that's good. Thank you for bringing that up, Chris.
Alright, open… main, pull request. Doesn't look like there's anything too super crazy there. Brett, we were… I was… I DM'd you about this, I think, with, these two, Jerry… Jerry reviews. Is there… do you,
I saw that you were still working with him a little bit. Do you… are you planning on continuing with him, or do you want me to take over there?
**Brett McBride** 11:58 I think we can both do… I haven't… I haven't looked at it, and I've seen that there have been some updates from Jerry, and I haven't looked.
Okay. Yeah, I feel like maybe I should go back and remove my approval on… On that…
**Bob Strecansky** 12:12 On this one?
**Brett McBride** 12:12 I still don't understand whether it's… replaced, or… Expanded upon in that other…
You know, that other payable request.
**Bob Strecansky** 12:26 I'm just gonna ask him.
Yep.
Show this… The RB replaced.
This one.
Well, hopefully we'll get an answer back from…
A good friend, Mr. Jerry, there.
**Brett McBride** 12:50 Yep.
**Bob Strecansky** 12:54 Instrumentation. This picks observing namespace functions pull request. Looks like Chris started… Chris and Niveaeh started reviewing this with you.
**Brett McBride** 13:04 So I think that's, I think that's cool now. Chris, did I…
**Chris Lightfoot-Wild** 13:10 It was kind to suggest I was perhaps trying to review it. It was more of an idiot's question, but…
Yeah, neither that we've did it, so thank you.
**Bob Strecansky** 13:20 I'll also review that today, because I'm curious, too.
Right? Doesn't look like there's any new… Questions here… Nothing crazy on the board…
Almost done with SDKv2, that's so exciting.
**Brett McBride** 13:40 Actually, that middle one when you're there, Bob, can actually move across. That's been… merged now.
**Bob Strecansky** 13:48 Got it.
It says that it's open, but…
**Brett McBride** 13:53 Oh, really? Hmm.
**Bob Strecansky** 13:54 Oh. Oh, I see.
I think it changes… Hmm.
Okay.
Sounds good. That means we can do SDKv2 at some point.
**Brett McBride** 14:08 Yeah, yes.
**Bob Strecansky** 14:12 We'll have to think about when that's going to be.
**Brett McBride** 14:15 Yeah, I… yeah, timing, and also I just… I think I need to think more about…
how to do that in our monorepo, and what it means for… for everything else.
**Bob Strecansky** 14:27 Okay.
Well, obviously, no hurry.
Oh, I have a question. Paul, did you… were you able to, sync up with the C++?
**Pawel Filipczak** 14:46 So I will try to attend the SIG meeting today.
**Bob Strecansky** 14:49 Oh, it's today, okay.
Zig came and DM'd us with…
bunch of good questions, and not concerns, but just like, hey, this is the state of where we think things are, and they seemed very receptive to it, which is good. I just wanted to make sure that you were able to sync with them.
**Pawel Filipczak** 15:04 I will.
**Bob Strecansky** 15:06 Cool.
Alright, anything else on the agenda from anybody?
**Brett McBride** 15:16 Oh, just to report on an experiment I've been running.
So at my… at my day job, we run PHP 7.4,
on some old, crusty servers. And…
every year, we've got, like, I don't know, 150 apps running on this one big-ass, 7.4 server, and so the… the Rust implementation that I demoed 6 months ago or so, I went back and made that work all the way back to PHP 7.0.
Which was interesting, with some auto-instrumentation, and so I installed that, on our… on our development server,
And it worked. So, that was interesting. It was actually the…
the main goal was that I needed to, sort of, sort of work on some,
sort of dashboards and stuff for, sort of tracing data, and we didn't have any because it's just taking us, you know, excruciatingly long time to develop anything new in my workplace.
Yeah, so… so I turned it on. It's been running for probably about 2 months now, just quietly in the background, and nothing's gone wrong yet, which I was quite pleased about. Yeah, I still don't know what… what this means, you know, what to do with this in the future, but I've,
Yeah, I'm still playing with it in the background. But I thought that was an interesting use case anyways, that you can do auto-instrumentation, some types of auto instrumentation, all the way back to
you know, versions that we never ever supported in our PHP language, our version.
**Bob Strecansky** 17:11 Very cool.
That's exciting, that's exciting, that's probably… it's so cool to see, like, a pet project go into prod and not break things.
**Brett McBride** 17:20 Sorry, I missed all of that, Bob, what did you say?
**Chris Lightfoot-Wild** 17:22 So.
**Bob Strecansky** 17:23 It's always exciting when you get a pet project into production and it doesn't break things.
**Brett McBride** 17:28 Yeah, I… it's… well, production, it's… it's very much a development server, and I, I had to promise it wasn't going anywhere near production anytime soon.
Yes, I have a bit of a reputation, I think, for getting things done without necessarily
Doing all of the paperwork, or asking all of the… all of the right people.
**Chris Lightfoot-Wild** 17:52 A livable rogue.
**Bob Strecansky** 17:54 Better to beg for forgiveness than ask for permission. That's what I always say.
**Brett McBride** 17:58 Yeah, yes.
**Bob Strecansky** 18:01 Excellent. Well, congratulations, I guess? That's… that's, that's pretty exciting.
**Brett McBride** 18:06 Yeah, look, it's, it's, it's something, it's, Yeah, yeah.
**Pawel Filipczak** 18:12 That's nice, if you have some layer, which is… which is handling everything, the differences between the version, and you're just relying on the data, and not, you know, you don't need to dig.
Too deeply, and, and, and, you know…
Because there are a lot of differences in PHP.
engine and data structures, so…
**Brett McBride** 18:33 If the replayer is handling everything for you, then it's quite easy to, you know, to maintain all of the past versions, which are not supported.
Yes, yes, that's right, and that's sort of…
I don't know, if nothing else, it gives me a good vision for what… what we could do in… in a,
In an extension.
You know, can we follow the same pattern with C++?
And…
you know, I suppose in my mind, and what you've already started to do is sort of replace the, you know, the things that we need to be asynchronous and
walking, and maybe the hot path, you know, what…
where do we spend the most time if we were to profile OpenTelemetry, and how do we move that into something faster? Which is probably…
you know, C, C++, Rust, anything but native PHP.
**Pawel Filipczak** 19:32 Yeah.
I agree.
**Brett McBride** 19:34 Hmm.
**Pawel Filipczak** 19:36 Yeah, I'm taking… I'm looking into your… into your projects, and I'm watching your PRs, and.
**Brett McBride** 19:41 Oh, I ain'.
**Pawel Filipczak** 19:41 I mean, what you are… how you are… and you are progressing quite fast, so yeah, a lot of work.
**Brett McBride** 19:49 Yeah, well, you haven't seen… actually, so here's a good story. So, instead of doing my annual review today, because it's really boring, I implemented the logging,
I haven't submitted the pull request for it, but…
But probably in about 5 hours today, I went from 0 logging to, I think logging's working. I mean, it's a simple signal, there's not a lot to it, but,
like, the hard part is just working at header interface to Rust them, and once you've got that, you know, have a high degree of confidence in
in the Rust implementation, and things just work. It's really nice to… nice to see.
**Pawel Filipczak** 20:34 Great. Maybe I'll.
Maybe I will try to convince…
Some people to help you at some point, so… Let's see.
**Brett McBride** 20:42 Yeah, well, yeah, if we had more Rust developers or something, I would be a lot more enthusiastic about, you know, really trying to push that, but…
Yeah, if it's just me, I can't…
you know, I feel like that's too much responsibility for the whole OpenTelemetry PHP if, nobody else can fix it and work on it.
**Pawel Filipczak** 21:06 Anyway, I did this quarterly, you know.
form, and I've made the same works today. It's so… it was so boring.
Yeah, but, you know, there are tools which are helping to solve that, so, yeah.
**Bob Strecansky** 21:27 Okay.
**Brett McBride** 21:29 Nothing else for me.
**Bob Strecansky** 21:31 Excellent. Well, we'll see… We'll see you all on the internet.
**Brett McBride** 21:36 Yeah, yep. And just a reminder, I think you've all remembered I'm going on 10 months leave in
two days. I'll still be around. I do still plan on, you know, answering questions and reviewing pull requests. I might not make it to so many SIGs once the time zone shifts and it becomes midnight my time. I'm not feeling very enthusiastic about that.
Just at the moment.
**Bob Strecansky** 22:05 Would, would you prefer a SIG time change prep?
**Brett McBride** 22:09 I don't know that there's…
I mean, it's always been the same problem, you know, it's got to be terrible for somebody.
Yeah.
So, no, I don't… I don't think there's a time that's good for me that doesn't then make it awful for you, or Chris, or Powell, or…
Somebody, so…
**Bob Strecansky** 22:30 I'm wondering… I'm wonder… wondering if it makes sense to shift it a little bit earlier at some point, so, like.
would be 6, you know, 6 AM for me, and 9pm for you, or something, like, to that extent.
Or later in the day, we can always revisit if we need to.
**Brett McBride** 22:47 Yeah.
**Bob Strecansky** 22:48 We're gonna miss… we'll miss you while you're not here.
**Brett McBride** 22:51 Wow, I will be popping in. I'm not… I'm not planning on completely disappearing, because I…
you know, this is my pet project, and I actually enjoy working on this much more than what they pay me to work on.
**Bob Strecansky** 23:04 Same.
**Brett McBride** 23:06 Yeah.
**Bob Strecansky** 23:09 Sounds good. Alright, well, enjoy your paternity leave, and I'm sure we'll see you on the internet.
**Chris Lightfoot-Wild** 23:14 Fabulous. Alright, thanks, team. Bye-bye.
