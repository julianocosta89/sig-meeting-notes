SIG: OpenTelemetry on Mainframes Weekly Meeting
Date: 2025-08-27
Duration: 6 minutes
============================================================

## Zoom Recording Transcript

**Greg Shriver** 02:33 Hello, folks.
**Richard Nikula** 02:40 Greetings.
**Greg Shriver** 02:44 Anybody know if, … Rudiger's coming today?
He said he was out.
**Morgan McLean** 02:51 On the 10th, he said he'd be out for the next 3 weeks. He'll be back on September 1st, so no, he won't be here.
**Greg Shriver** 02:58 Oh, he won't be here. Okay.
**Morgan McLean** 03:00 Do we wanna skip?
**Greg Shriver** 03:03 Well, I don't know. Does anybody have anything?
**Morgan McLean** 03:10 I don't have any topics.
**Richard Nikula** 03:11 Was anybody here at SHARE last week?
**Greg Shriver** 03:15 I was not.
**Morgan McLean** 03:17 I was not.
**Richard Nikula** 03:18 Okay, I just thought it'd be good to get an update, but I guess we won't.
**Greg Shriver** 03:23 Yeah, I don't think we'll get an update for… not for Cher. I know that they, … I know there were some sessions
But … but I didn't get it… I didn't get a detailed debrief, no.
I did have, one item, Which…
we don't really have to talk about today, because I don't have it formulated. I'm actually, thinking about putting together a pull request so that it can get a little better scrutiny.
Just to give you guys a heads up…
Right now, we don't… I don't believe, and I still need to go back and take a look, but I don't believe that subsystem name is defined anywhere.
In, in the semantic conventions.
And I don't think it should be a resource attribute, but I think, it should be probably appropriately namespaced, like zos.subsystem.name.
And I furthermore think it should be optional. Not optional, but not required, simply because not everyone will have that value when they need to fill it in the telemetry.
So… my thoughts were to open up a PR to do that.
To… to propose that.
… I assume that… does anybody have any objections about that? No, I think it's a good idea.
**Richard Nikula** 05:05 was something I noticed when I was looking through it initially, that…
It was obviously something we would expect to have that wasn't there. Agreed.
**Greg Shriver** 05:15 Yeah.
Okay, so I'll just put it on my to-do items to, I guess, draft a PR.
Or at least get one started. I assume that they stay in draft mode for a while before they get merged, so…
So, and that one seems, you know, relatively sharp and focused, as opposed to, you know, some of the prior ones, which have been kind of bigger.
So… I assume small ones are okay as well.
**Morgan McLean** 05:46 Definitely.
**Greg Shriver** 05:48 Okay.
Alrighty.
Well, …
Other than that, I mean, I'm not really prepared to talk about that today, but thank you guys for giving me your input. But other than that, I really don't have anything for today.
**Morgan McLean** 06:03 Okay, I'll type up the notes.
**Greg Shriver** 06:09 Cool.
**Morgan McLean** 06:09 Cool. Alright, I'll see you folks next week.
**Greg Shriver** 06:11 Thanks, guys.
Bye.
