SIG: PHP SIG
Date: 2025-08-27
Duration: 12 minutes
Zoom Recording URL: https://zoom.us/rec/share/hC0K_DWk8NmpWnDn6cxd7UDT7JP2Ju6ZXCRXnJK-EQwFi5Z10vQFKM32qGwXv_wH.L_o57Tnxxy-jAcx7
============================================================

## Zoom Recording Transcript

**Chris Lightfoot-Wild** 00:40 Hey, Bob.
**Bob Strecansky** 00:41 What's up?
**Chris Lightfoot-Wild** 00:43 Hey, watch, how are you?
**Bob Strecansky** 00:46 Same old, same old.
**Chris Lightfoot-Wild** 00:50 Nice.
**Bob Strecansky** 00:55 One of our vendors disclosed a big security vulnerability today, so I have a very strong feeling I'm gonna have a rough day.
**Chris Lightfoot-Wild** 01:01 Oh, dear.
Sorry to hear.
**Bob Strecansky** 01:05 You know, you know how it goes.
So I will be… I have a hard stop. …to 8.30 for sure today.
**Chris Lightfoot-Wild** 01:15 Oh, is it 7.30 for you now, then? Oh, 7? 8?
**Bob Strecansky** 01:20 It's 8 for me right now, yeah.
**Chris Lightfoot-Wild** 01:22 Oh, okay.
**Sergey** 01:31 I don't know.
Hi, guys.
How do you do?
Oh, quite well.
So, does the scope start, … In US, 1st of December, I mean, after that.
That's Labor Day, right?
**Bob Strecansky** 01:48 So, it's… that's a funny question, because it's, like, all over the United States, it's very, very different. My daughter started school, like, 3 weeks ago, and some of the Northeastern schools don't start until, like, after Labor Day.
It's interesting. They do it, but… they do it based on, like… it sounds goofy, but they do it based on temperature. So, like, in the Northeast right now, it's not, like… in the Northeast right now, it is… like, that's, like, good weather for the Northeast, so they want to, like, the kids… everyone wants to have a little bit more time in the summer with their kids, but down here, we're, like, it's hot and we're ready for the kids to go back to school, but at least that's how I've always taken it, but… Yes, some schools back, some schools not back.
**Sergey** 02:34 Nice.
**Bob Strecansky** 02:35 Interesting.
Hi, y'all. I told Chris at the beginning of this call, one of our vendors disclosed a pretty big security vulnerability today, so I will have to leave at 8.30.
Or, you know, half pass, so….
**Sergey** 02:54 Nothing, … not related to OpenTelemetry, right?
**Bob Strecansky** 02:57 Not related to OpenTelemetry, thankfully.
Should be sharing my screen, huh?
Let's get rockin'.
Y'all see my screen okay?
**Chris Lightfoot-Wild** 03:22 Yep.
**Bob Strecansky** 03:37 Alright, let's take a look. Pull requests… Couple GitHub actions… And then a bunch of old stuff. I'll take a look at those later today, if I have time.
Looks like we have auto-instrumentation hooks for a PHP session… And some more GitHub Actions.
Looks like this one has a lot of conversation on it. Brett, you are… you are on it, my man.
**Brett McBride** 04:08 Yeah, I'm starting viewing that one, yep.
**Bob Strecansky** 04:11 That was open 10 hours ago, and there's already 23 comments, back and forth and real hard.
Thank you for that.
Instrumentation, another GitHub action pump, I'll take a look at that later, too.
Does anybody have anything that's in the prioritized backlog that they would like to discuss today?
Nobody's good news?
… Looks like we have… the road to SDKV2 is just blocked by updating metrics temporality.
Is this… this one also has not yet been assigned, so somebody will take that eventually, but I wouldn't.
I'm not putting too much emphasis on that right now.
Installations to… oh, we're throwing clothes.
20 million? Up.
didn't have a whole lot to walk through there. Does anybody have any open agenda topics for today?
**Sergey** 05:19 … Just something to… to beef up the meeting. … I think Brad saw that, we have this issue of implementing the, how do you call it, … The new sampling algorithm, … forgot how they call the new one.
But I also saw there was an older one called Experimental. I was wondering if you guys remember… What happened to that one? Was the decision not to implement it for PHP, or was it just, … It stayed experimental, so you guys waited and… Do you remember anything about it?
**Brett McBride** 05:55 Is this the rules-based sampler?
**Sergey** 06:00 Yeah, I think they're similar in the sense that they also record something to the trace state, but I think it was a little bit different.
… Oh, yeah, I guess I will, I will investigate, maybe I will have a more focused question next time.
Because I was wondering if you remember anything about that, but… Yes, I….
**Bob Strecansky** 06:20 I do. I remember hearing them talk about it in the maintainers meeting over and over again for, like, it was, like, 6 weeks in a row, and I was like, I am not touching that thing anytime soon, because it was just, like.
it was, like, one of the biggest points of contention that I'd seen in OpenTelemetry. They, like, were constantly talking about the right way to sample and the right way to, like.
use configuration files for keeping that sample in? How do we make sure that the environment stays the same? It's, you know… classic 12-factor auth problems, but they were just, like, talking about the right way to implement it, and it was one of those things where it just seemed like it had so much contention that it was never going to get completed, and I think that's why it stayed in experimental for so long, but… I think eventually we'll have to evaluate some of our sampling.
techniques, because there are bits in the spec for it, but we haven't had any customer feedback about that yet, so I would… I think that we can prioritize that if somebody wants to, or if we get customer feedback saying that we need a better sampling mechanism, but my opinion is we should wait for that to be stable in the spec, or wait until we.
**Sergey** 07:29 No, it's already stable, but it's different.
**Bob Strecansky** 07:31 Oh, it's put it in.
**Sergey** 07:31 So, whatever became stable, it's a bit different for experimental.
That's why I was wondering, like, if you guys remember anything about the… but it seems that what you're saying is that it was… hot topic for a while. Yeah, we would like to contribute to this implementation for the stable version, so….
**Bob Strecansky** 07:49 Oh, cool.
**Sergey** 07:49 I guess we'll skip the experimental approach and not have it at all.
I was just wondering if you guys kind of, like, maybe implement experimental and waited with it, but, it sounds like you were waiting, for good reason, and it probably was the right decision, because… the new one is not the same as experimental, and I guess… I don't know how much it's different anyway, but… Yeah, we would like to contribute the new, the stable one.
**Bob Strecansky** 08:13 Cool.
**Sergey** 08:14 I will… I will open the PR for that.
**Bob Strecansky** 08:16 Thanks.
Excellent, that's… sampling is… It's important.
Thank you for that.
**Sergey** 08:29 That's it for me.
**Bob Strecansky** 08:34 We've had to have the world's fastest OpenTelemetry PHP SIG meeting.
**Brett McBride** 08:43 Like, we ran well over last time, so we were due a short one.
**Bob Strecansky** 08:47 We were due a short one. Alright, well… I'll give you all a bunch of time back, and if you see any… if you need anything, talk to us on the internet, we'll catch you. I'll be here next week, but then the two weeks afterwards, I will be out of the office. I will be on vacation.
**Chris Lightfoot-Wild** 09:04 Sure.
**Sergey** 09:05 Yeah.
**Chris Lightfoot-Wild** 09:06 Enjoy.
**Pawel Filipczak** 09:06 No, you're okay.
**Brett McBride** 09:07 By the way.
**Pawel Filipczak** 09:08 My guess.
