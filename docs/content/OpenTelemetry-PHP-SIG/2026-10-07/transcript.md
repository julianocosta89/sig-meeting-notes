SIG: OpenTelemetry PHP SIG
Date: 2026-10-07
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**James Strecansky** 01:14 Hey, Chris, can you hear me? Okay.
**Chris Lightfoot-Wild** 01:17 Boom.
**James Strecansky** 01:20 I can hear you, I think.
**Chris Lightfoot-Wild** 01:22 James?
**James Strecansky** 01:24 James. Oh, that's right. It's the that must be an update. My name is actually James Robert Strucansky, but I go by Bob.
**Chris Lightfoot-Wild** 01:31 Really?
Yo, Jimbo!
**James Strecansky** 01:35 I am a Jim Bob, it's true.
**Chris Lightfoot-Wild** 01:37 Oh, nice.
Is your dad called James or something, huh?
**James Strecansky** 01:42 Yeah, so my dad is James, and my… My other grandfather is Bob is Robert.
And it was, I am the fourth James, but normally in the States you do like.
James Robert Stracansky the first, the second, or third, whatever.
**Chris Lightfoot-Wild** 01:58 And…
**James Strecansky** 02:00 my family just decided the first name is going to be the same, so it was… it's… I'm very glad that we didn't do that with our kids, because it was just, like, insanely confusing all the time.
I explicitly named my son Jack because it's another J letter, but not.
James?
And…
**Chris Lightfoot-Wild** 02:17 Okay.
**James Strecansky** 02:19 And my daughter, her name is Madeline. And my mother-in-law had a really great idea because I told my wife's family that I didn't want to name my son James.
And if I had one, my daughter's first, obviously. And so my mother-in-law was like, why don't you name her Madeline James? That's a really pretty name. So my daughter's name is Madeline James. So we're still keeping the James, but not as the first name.
**Chris Lightfoot-Wild** 02:46 Ryan, can I add that as, a female, sort of, name before?
**James Strecansky** 02:50 Yeah, yeah, it's, it's not usual. I've heard… my daughter's not the first one, but…
**Chris Lightfoot-Wild** 02:58 Oh, that's cool, it sounds good.
**James Strecansky** 03:01 Pretty name, pretty girl.
**Chris Lightfoot-Wild** 03:08 Other… other attendees? Hello!
**James Strecansky** 03:11 Yeah, I got it.
**Chris Lightfoot-Wild** 03:13 Lovely.
Collins? Hello, Collins?
**Collins Adom Baffour** 03:21 Hi, Chris.
**Chris Lightfoot-Wild** 03:24 gonna.
**Collins Adom Baffour** 03:28 Good afternoon from Ghana.
**James Strecansky** 03:32 Oh, nice to see you.
**Collins Adom Baffour** 03:35 Asia.
Yeah.
I've been joining 6M. I'm planning to, at a point, try and contribute, become a contributor.
To open telemetry, so I joined S6 to know how, The meetings are conducted and all that, yeah.
So I'm just here to learn.
**James Strecansky** 03:57 Cool. Well, welcome.
**Collins Adom Baffour** 04:00 Thank you.
**Chris Lightfoot-Wild** 04:02 You'll have to let us know how we compare.
**James Strecansky** 04:07 I think this is everybody that we're expecting today, yeah?
**Chris Lightfoot-Wild** 04:13 Yeah, it was still not heard of Brett. I've seen earlier activity again.
**James Strecansky** 04:17 I think he's just lurking in the shadows.
Shadow contributing.
**Chris Lightfoot-Wild** 04:22 This is life for him, isn't it?
**James Strecansky** 04:24 Say it again.
**Chris Lightfoot-Wild** 04:25 He's a Latin.
them anyway, so…
**James Strecansky** 04:30 Yeah.
**Chris Lightfoot-Wild** 04:31 But it's late night in Australia.
**James Strecansky** 04:34 Yeah, yeah, I think… I think it's… I think this meeting was at 10 or 11 p.m. for him, depending on when the, like, with time changes and stuff, so… He was he always that's when he preferred, but I think maybe with baby it might be a little different.
For good reason.
First order of business for y'all is this is going to be my last OpenTelemetry PHP meeting.
I am turning in the keys. I got a new job, and I won't be able to contribute anymore. So, after 7-ish years of contributing, I'm… I'm gonna go… I'm gonna change to an emeritus status on, in our repo, and I'll still be around for, like, approvals if absolutely desperately needed, but… I'm, yeah, I'm gonna be taking a new job as a Senior Director of Smart Mobility at Transcore, which will be a fun and exciting challenge, so… Yeah.
It's been an absolute pleasure to work with y'all, and it's… I have a very heavy heart for turning this in, because it's my first and biggest open source contribution, so.
Oh, I will be, I'll be missing y'all, but I need to do it for my career, so…
**Pawel Filipczak (Elasticsearch B.V.)** 05:54 Congratulations.
**James Strecansky** 05:55 Thank you, thank you.
**Chris Lightfoot-Wild** 05:58 Of course, yeah.
**James Strecansky** 06:00 Thank you. So, I wanted to make sure that I told you all in person, didn't just, like, shoot you an email, so… I'm also planning on logging out of CNCF Slack, so if you need a pull request or to talk about anything, just feel free to shoot me an email. I think y'all have my email address.
**Chris Lightfoot-Wild** 06:20 Yeah, have you told Severin already?
**James Strecansky** 06:23 Yeah, I told him, too. I wanted to make sure… I told him first, because I wanted to make sure that was false. I didn't know if there was any, like, protocols or whatever, so…
**Chris Lightfoot-Wild** 06:31 Yeah, cool. Well, obviously, sad to hear that, but I wish you the best, and we may well see you around, I guess, at times.
**James Strecansky** 06:38 Yeah.
**Chris Lightfoot-Wild** 06:38 time permitting. Yeah, just wonder if, obviously, with Brett gone as well, or less visible.
In… we might need to discuss maintenance, I guess, or is that something Severin's gonna come to the fold and…
**James Strecansky** 06:52 I'm… I'm assuming… I'm assuming that everyone will take… take that response. Like I said, I can… I can… bridge the gap for a little bit. I don't start until, November, so I can definitely bridge that gap until we find the right, right, maintainers.
I think y'all are more than willing and able to do it, or willing and capable of doing it if you would like. So.
So.
**Pawel Filipczak (Elasticsearch B.V.)** 07:17 There will be a problem with the releasing, merging, and everything, so…
**James Strecansky** 07:23 Yeah, yeah, I think we definitely need to get at least one, if not two more maintainers. We'll have a discussion about that in the admins channel.
And see see what what's everyone wants how everyone wants to handle it, but So… Anyway…
**Pawel Filipczak (Elasticsearch B.V.)** 07:44 No.
**James Strecansky** 07:48 Yeah, sorry, I'm being a Debbie Downer in this meeting, but…
**Chris Lightfoot-Wild** 07:51 No, not at all. I mean, that's the usual deviation, just for Colin's benefit, that's not…
**James Strecansky** 07:56 This is not our.
**Chris Lightfoot-Wild** 07:57 You know what I mean?
that… Well timed.
Well, do you want to walk the board up one last time, then, Bob, for…
**James Strecansky** 08:08 Yeah, I certainly will. Very happy to.
Mmm.
**Chris Lightfoot-Wild** 08:14 Can I ask, I guess, the new role, then? Are you in a different language, a different ecosystem?
**James Strecansky** 08:20 Well, different altogether, I'm working on a, Transcore does smart mobi… they do, like, all the important stuff for Department of Transportation, so, like.
traffic lights, and toll roads, and express lanes, and apartment gate arms, and, like, all these really cool things, and so I'm working on, building up a team for them to do, like, a tech refresh, so, like, you'll be able to drive through the United States just with your phone and a Bluetooth beacon, and go through all the tolls and express lanes and stuff, and… A bunch of other cool stuff like that, so…
**Chris Lightfoot-Wild** 08:58 Sounds fun.
**James Strecansky** 08:59 Yeah, so I'm… I'm gonna be a… my new title is Senior Director, so I'll not be IC-ing, which will be a very, very stark change for me, but… Bulla. Bulla.
Take it as it comes.
**Chris Lightfoot-Wild** 09:12 Absolutely.
**James Strecansky** 09:14 I've been doing that at Intuit for a very long time, but without the title.
Alright.
Looks like Brett has a couple open.
There it is.
**Chris Lightfoot-Wild** 09:33 I think I approved that top one already, but… Yeah, so we'll have to wait for some… in fact, so keen, I did it twice by mistake.
**James Strecansky** 09:40 The two times over.
**Chris Lightfoot-Wild** 09:42 And I was like, oh, this is good. Twice.
**James Strecansky** 09:44 Oh, she is. I got signed out of GitHub. Hold on a second.
Oh, shoot, my phone's upstairs.
Oh.
Yeah, hold on.
Give me one second, I'll be right back, I can't get my phone.
**Pawel Filipczak (Elasticsearch B.V.)** 10:25 Oh.
**Chris Lightfoot-Wild** 10:27 How are you, feeling about… Powell, would you, consider being a maintainer and.
**Pawel Filipczak (Elasticsearch B.V.)** 10:34 Yeah, why not? Yes.
**Chris Lightfoot-Wild** 10:35 the.
**Pawel Filipczak (Elasticsearch B.V.)** 10:36 Yes, we have to.
**Chris Lightfoot-Wild** 10:38 I was just kind of thinking between us there, we could do it for the releases, because we can't… well, I can't merge into the main… repo either, and I can't merge the distro on, which, obviously, we've got you, and I'm doing the contrib, but then… It would just be down to bat otherwise.
**Pawel Filipczak (Elasticsearch B.V.)** 10:53 No.
**Chris Lightfoot-Wild** 10:55 Yeah.
**Pawel Filipczak (Elasticsearch B.V.)** 10:55 I guess we have to… so I will, I will review the, the… The… I'm not sure.
The repository of the distro, and I will see if you are maintainer or approver, I don't remember, so I have to take a look.
**Chris Lightfoot-Wild** 11:12 I think I'm a prover, at least, and that's fine. I mean, it's not my area of expertise, that's on, you know, for you, but Yeah, certainly the other one, PHP code, I can… Try and help out there.
**Pawel Filipczak (Elasticsearch B.V.)** 11:23 No.
That looks like me, but…
**James Strecansky** 11:28 You guys working on the reviewer for this one.
Kinda baby.
Oh, nice, an update for OpenTelemetry configuration. That's kind of cool.
This is still on the draft.
Looks like y'all are talking through that with them.
Nothing else new.
Control… OpenTelemetry bot.
Laravel fix, Laravel fix, monologue fix.
That's pretty much it.
What is this, Joe? Okay.
Sounds good.
**Chris Lightfoot-Wild** 12:25 I think… I looked into his profile before, I think he's to do with the Ruby SIG as well, and he's done quite a few good contributions for, like, the… You know, the pipeline stuff, so…
**James Strecansky** 12:36 Yeah, I think that it seems like.
Seems like it fixes the repo status and renovates, so… Good enough for me.
And then looks like y'all Brett is working on remediating more findings.
And then… queuing spans for request signature. Chris, you're already commenting on this one, too. Chris, you're all over it, huh?
**Chris Lightfoot-Wild** 13:18 I'll try my best.
**James Strecansky** 13:20 doing.
**Chris Lightfoot-Wild** 13:21 Too much on a blip, but…
**James Strecansky** 13:22 Great. This one, I'll tell you about this one. Huh?
Why am I even walking the board? You've already walked it.
laughs.
**Chris Lightfoot-Wild** 13:30 There was one in here that I did, I sort of seen, but I thought, again, that's not one for me. I didn't want to just blindly approve it, so maybe Powell?
**James Strecansky** 13:38 Talking about… Yeah, the constant AC attribute args.
**Chris Lightfoot-Wild** 13:43 Yeah.
Sort of inner workings of the experience.
**James Strecansky** 13:45 Yeah, that one's…
**Pawel Filipczak (Elasticsearch B.V.)** 13:47 Very difficult.
**James Strecansky** 13:48 Okay, cool. I'll do the, balance copilot request, just… I've found that that is… Good to do, just because sometimes it catches a little dumb stuff, but… And then distro.
Perfect.
**Pawel Filipczak (Elasticsearch B.V.)** 14:06 Nothing.
Nothing serious here.
**James Strecansky** 14:09 Nothing of note. Got it. Okay.
Let's see.
We did the project board last time, which is really nice.
We can look at our package sets.
Made it to 53 million, let's go!
Wow.
**Chris Lightfoot-Wild** 14:29 Are we above a million a month now? Did that say, or did I misread that? Sorry.
It's a half a million, okay.
Cool.
**James Strecansky** 14:38 Last 30 days is 4.5 million.
**Chris Lightfoot-Wild** 14:42 Nice. So over a million a week at least then.
**James Strecansky** 14:46 Whoa.
Pretty cool.
**Chris Lightfoot-Wild** 14:50 It's kind of that.
**James Strecansky** 14:52 Yes.
And then… looks like there's… New Laravel bug.
**Chris Lightfoot-Wild** 15:02 Oh, that's the first one, I've not seen that.
**James Strecansky** 15:03 Yeah, 2 hours ago.
Redis command watcher using microtime instead of an API clock.
Yeah. Okay.
**Chris Lightfoot-Wild** 15:14 That was one where… because it just looks at the event in Laravel already, it's kind of aware of it. It tries to… because it doesn't start a span, so it calculates from the event, what… how long the duration is. And then backfills the start time of the span. So it's not using the underlying light telemetry.
But I'll… I'll have a look at that one. That was kind of the ones where I was thinking, you know, when we move away.
toward using actual, like, PDO instrumentation.
that actually does things properly. This kind of just goes away anyway.
Oh, so it's on Redis, isn't it? But it's the same, the same problem, the backdating based on the event data.
**James Strecansky** 15:57 Yeah.
**Chris Lightfoot-Wild** 15:58 Yeah, but…
**James Strecansky** 15:59 Cool.
All right.
Hmm.
I think that's everything that's relatively recent.
Ta-da!
And that's… that's all she wrote.
Anything else you all want to discuss today?
**Chris Lightfoot-Wild** 16:23 I mean, I did have a thing I was going to ad hoc ask, but.
**James Strecansky** 16:26 Sure, yeah.
**Chris Lightfoot-Wild** 16:27 I don't know. Just in light of your, you know, sad… with sadness, it was, Justin, so obviously I've got… I've been looking at the Laravel instrumentation again, and obviously there's various reports of things where, you know, the snagging and… One of the main ones I was wanting to try and tackle was about spam suppression.
I couldn't quite get my head around where… the way the SDK is instrumenting things now, so it's using SPI, Early on in the process, it… It sets up all the instrumentation, and everything is deferred to resolve you know, a tracer, there's meeting providers, tracers, log providers, etc. That are deferred.
I guess at the last moment.
Boom.
But then, within Laravel, obviously there's a whole bunch of… Classes that are instrumented.
And it's at a very specific starting point that, ideally, I'd like to… the spans to start mattering. Like, you can say, right, from this point on, start a trace, and end at this point, and then everything outside of that is just discarded.
And I don't quite understand at what point you decide From now, it should matter, everything else shouldn't matter.
Outside of that window. Because there's other stuff bootstrapping, like, within the framework.
even when you're doing, like, a console command, it's checking, has there been some cache entry to say I shouldn't be running? There's, like, a maintenance mode, etc.
And I don't want that to start a trace of its own, because that causes the… Trace provider to resolve.
And I don't quite… yeah, I don't know if anyone's got any insight into that, or what question I should be asking, or am I thinking about it wrong, or…
**James Strecansky** 18:16 Yeah, I'm not certain. I remember that being implemented. That would be a really great question for Brett. I know that he worked heavily with Nibet on the initial SPI implementation. He probably could give you a lot more insight than I could.
**Chris Lightfoot-Wild** 18:28 Yeah, I think it's even outside of SPI as well, just in general, I've never quite understood it, and I've seen some stuff that Nevi had, commented on one of Jerry's.
PRs for some of their instrumentation, and saying, oh, you captured the… The initial context, when the instrumentation is constructed.
And then you can activate and deactivate when you need.
But that… that was the bit that I couldn't quite get my head around. Like, I can capture it during the construct, but then… when the tracer resolves, I guess it's in that con… in that context, I wanted… I'm guessing I want to switch context in some capacity, I'm just not… not sure. But maybe I could put it in the channel, I guess, and tag Brett, potentially Nive.
**James Strecansky** 19:11 Yeah, I think that would be your best bet.
**Chris Lightfoot-Wild** 19:14 Yeah.
I don't know if I phrased that question very well, though, but, I could probably do with an example, I suppose, so…
**James Strecansky** 19:23 Yeah, sometimes… sometimes situations like that, actually having, like, a fungible example really, really helps to… I know I've done that so many times myself, like, I write that example, I'm like, oh.
**Chris Lightfoot-Wild** 19:33 I.
**James Strecansky** 19:34 Obviously, or like, oh man, this is really bad, let's, like, let's talk through this as a group.
**Chris Lightfoot-Wild** 19:39 You end up getting, like, unusual… like, something else will start a trace. I guess in your head, you might think it's out of sequence, and, like, a long-running command will keep accumulating spans in that trace.
And then… Like, at some point in the telemetry, it just says, you know, this is, like, an orphaned Spartan, there's no… I can't find a parent for this, and… It never comes along.
And then even in local testing, then I discovered that Yeah, so I've got a console command.
You send a SIG into it, and that prevents the instrumentation from actually cleanly wrapping up. Like, the extension just I guess the signal handler just tells it to sort of die almost immediately.
And then it doesn't wrap up its existing spans and clean up after itself.
**James Strecansky** 20:29 Well, it seems like something that shouldn't happen, but, you know, it's always like a… Well, maybe there's a con…
**Chris Lightfoot-Wild** 20:36 Yeah.
**James Strecansky** 20:37 behind the…
**Chris Lightfoot-Wild** 20:38 I feel like I was definitely at the boundaries of my knowledge and, yeah, probably do with some bigger brains to Point me in the right direction.
**James Strecansky** 20:46 Oh.
I think, yeah, I think… writing it down, either as an issue or in Slack, whatever is easiest for you, we'll help… we'll help to help you remediate it. We've got a lot of big brains around.
Yeah.
**Chris Lightfoot-Wild** 21:02 Thanks very much.
Hey, Collins, did you have anything you wanted to ask, or do we just hear, yeah?
observational capacity.
**Collins Adom Baffour** 21:18 Yeah, I'm just, listening to, yeah, the conversation, yeah.
**Chris Lightfoot-Wild** 21:24 Sure. Well, thanks for attending.
**Collins Adom Baffour** 21:31 See you.
**Chris Lightfoot-Wild** 21:36 Anything from you, Pawel?
**Pawel Filipczak (Elasticsearch B.V.)** 21:40 For me, I've… So I have.
I will start working on the head-based sampling.
**James Strecansky** 21:48 Oh, cool.
**Pawel Filipczak (Elasticsearch B.V.)** 21:49 So it's one of the issues which is pending somewhere in the space, in the backlog, so I'll pick it up.
And yeah, I hope I will finish this soon. It requires a bit of effort. I have to take a look what's already implemented, what's missing.
And I… I have to compare, because there are two different versions of that, at least in Java. I saw that there's old style and new style, so I have to refresh my knowledge.
Next week maybe I will I prepare something to for for the for review, so we'll see.
But besides all that, I was… for two weeks, I was a bit off of PHP, so now I came back and… I hope I've been… I will get more focus into it.
**Chris Lightfoot-Wild** 22:42 Sounds good.
I'll look out for that PR.
Cool.
Well, Bob, it was an absolute pleasure.
**James Strecansky** 22:53 It was. I'm really… I feel really fortunate to work with y'all. I've learned so much from y'all, and Stay in touch. Like, getting a little… a little misty out here, sorry.
**Chris Lightfoot-Wild** 23:03 Yeah, no, absolutely, we'll do it.
**James Strecansky** 23:05 Alright, we'll catch y'all soon.
**Chris Lightfoot-Wild** 23:07 Take care. See you later. Thank you.
Right.
