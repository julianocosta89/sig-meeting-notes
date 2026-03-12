SIG: Swift SIG
Date: 2026-01-22
Duration: 19 minutes
============================================================

## Zoom Recording Transcript

**nacho** 01:17 Rey.
Hey, Bryce.
**Bryce Buchanan** 01:25 Hey, Nacho.
Hmm… Light crew today.
**nacho** 04:09 Yep.
**Bryce Buchanan** 04:14 I guess we can get started. Don't wanna wait too long.
Alright. So, topics from last week… It looks like this is an outstanding topic, the fixed OSSF card issue.
Have we done any investigation on this yet? I haven't had a chance to look at it.
**Billy Zhou** 04:39 No, I can take another look today.
**Bryce Buchanan** 04:45 Interesting. No URL found for sub… oh, why do we have a submodule path? That seems like a mistake.
**Billy Zhou** 04:54 Yeah.
**Bryce Buchanan** 04:57 That should be a quick fix, let's see. So… Mmm… Oh, that's interesting.
Hmm… and get modules… We do not have a Git module, that's interesting.
Hmm… Is it maybe this here?
This probably doesn't need to be in here.
Maybe it does. I guess that's fine.
It's very bizarre.
**nacho** 06:21 Maybe there is something in that folder that is making that… I think it's a somatic in the…
**Bryce Buchanan** 06:28 Oh, yeah, grip, that's a good point. Semantic convention… I bet I know what happened.
Scripts, semantic conventions… yeah, somebody… committed… This folder, that's what happened.
**Billy Zhou** 06:52 Is it… You're supposed to be generated on build?
**Bryce Buchanan** 06:58 I… well… So, when these are run… when this generate script is run, it clones the semantic conventions folder.
And so it looks like that might have been committed.
**Billy Zhou** 07:14 Okay, let me, okay, I'll take another look and fix it then.
**Bryce Buchanan** 07:22 I can't delete it from here, so…
**Billy Zhou** 07:29 I think it might have been necessary to, Add, like, certain, tags, so if it's not, I don't know if… Yeah, I'll have to double-check to see if it's… it'll still work after you delete it.
**Bryce Buchanan** 07:46 Okay.
huh, alright.
Is that where that is? Let's see.
Okay.
Cool.
So, rebase, hotel, Swift V6, upgrade PR, or… Is this just pulling the Swift 6 into… On the main one, okay.
You're still working on this?
Billy?
**Billy Zhou** 09:14 Yeah, I need a… Rebase it, and… Yeah.
**Bryce Buchanan** 09:20 Okay.
Are there any, topics today?
**Billy Zhou** 09:28 No, there aren't any topics today, I did a… I think there was just one issue that we were looking at, Last week, with, Rinode, about… Something to do with the, the metrics API for things like… Someone's asking about, like.
Histogram or something, let me find it.
But I didn't see any, outstanding issues last week. Like, I think the last issue that was cut was, like, December 1st or something.
So there are no escalations.
**Bryce Buchanan** 10:09 Yeah.
Okay.
**nacho** 10:14 I think I have read somewhere someone asking for a graspberry partner?
If that was going to be added.
I don't know where I read that. Was it in… in the Slack channel? No.
**Billy Zhou** 10:30 it's f…
**nacho** 10:31 Maybe an issue? Can we open a Nissim?
Where was it?
Yeah, it was opened as an issue in OpenTremetry Swift.
Or it was a comment in the experimentary suite.
a PR rally, and… the PR10303.
God, I don't know if that's useful. Yeah, yeah, that one, yeah.
**Bryce Buchanan** 11:05 Oh, yeah.
**nacho** 11:06 And that's there. Yeah, I… You also did that, right, Billy?
**Billy Zhou** 11:13 Yeah, Alex left a few suggestions that I need to,
**nacho** 11:18 Yeah.
**Billy Zhou** 11:19 need to put in, because he's a contributor there, he, you know, has a lot of good,
**nacho** 11:24 Yeah, if you… yeah, I mean, they make sense, and yeah, it will… but if you consider it's very difficult, or it will take you… No, I can do it. Lots of time.
We could merge what It is now, and create another… Issue just to update, like, as a… As a improvement, fit.
So, yeah, I, I mean… definitely it will be better with that, but it's useful as it is now. So, yeah, just if you… If you… Want to address that.
It would be great. If not, your current tier is better than what we have now, that is zero. So we can release that with.
**Billy Zhou** 12:17 Okay, I'll Slack you, today, then, after I take a look at it, and, .
**nacho** 12:24 Yeah, I mean, also, if you feel some of those things are… Very difficult to achieve for… Or it will take too much time for you?
we can just… Land it, and improved later.
Because it's not something that everyone is gonna use. It's a library that people can use, can link, can use, can improve, can… that's… Yeah, that… that's my take, I don't know if probably Bryce has…
**Billy Zhou** 12:59 Okay.
**nacho** 13:00 or not? What do you think, Bryce?
**Bryce Buchanan** 13:06 I need to take a closer look at this, I haven't had a chance to, so I think that there might be some good feedback in here that we should probably resolve.
Before, Before merging it.
And, and that's… I think that was the main reason,
**nacho** 13:27 that I've held off on merging it so far is because I was waiting for these, yeah.
**Bryce Buchanan** 13:32 to be resolved, but I can also add my two cents to it as well, and maybe give some recommendations if they're, or at least just some feedback onto which things I think we should resolve before merging.
**nacho** 13:50 Okay.
Yeah, the thing is that this is a new thing, this is a new feature, it's really optional.
**Bryce Buchanan** 13:57 Yeah, maybe Just like, flag it as, like, like a beta or something.
**nacho** 14:04 Yeah, landing and improving is… is something that… Pass… We have done in the past with some features, I don't know if… So, yeah, I think… I was more in the sense of… If we need to delay this a lot more to address the feedback, which I think is great feedback.
but maybe we can do that in several steps. That's my… Instead of… Yeah, of… Waiting for a perfect solution.
**Billy Zhou** 14:43 Yeah, well, let me at least, address the feedback. Honestly, I, and, Yeah, and then I'll, I'll slack you guys for, the next revision.
**nacho** 14:54 Okay.
**Bryce Buchanan** 14:56 Right.
Let's also add a README to it.
**Billy Zhou** 15:04 Okay.
**Bryce Buchanan** 15:08 At least, yeah, somewhere where we can put a brief description and, Just warned that this is, You know, kind of a… a beta… a beta instrumentation.
Alright, cool.
I think I saw a new… A new issue here ensures the swift implementation of environment context propagation matches the specification.
With the environmental variable context propagation spec being added, we'd like to have it supported… its support added to SWIFT.
This is a larger effort to add support in each of the current supported languages. Okay, so…
**nacho** 16:03 Yeah, I must say we were the first library to add environment.
support, to the library, and they started using our implementation in other languages, but they have probably changed, yeah.
**Bryce Buchanan** 16:17 Yeah, they've updated the way that it works. okay.
Repositories to update… okay, wow.
Respect. Okay.
Swift already supports environmental popularity. The issue focuses specifically on compliance. Yep, yep, yep, yep.
Alright.
**nacho** 17:29 Yeah, this is really useful when you want to… Open a binary from another.
The command line, for example.
**Bryce Buchanan** 17:37 Hmm.
**nacho** 17:38 and inherit the context from one processor to the other. Maybe not in a… iPhone environment, but…
**Bryce Buchanan** 17:45 That's maybe for, more, for, you know, background, or, server-side SWIFT.
**nacho** 17:52 Yep.
**Bryce Buchanan** 17:53 Okay.
Okie dokie.
I guess, are there any other topics?
No?
I guess we can call it there today, then.
I'll do some follow-ups on, I can, Billy, I can probably, fix the… this issue.
So you don't need to worry about that.
**Billy Zhou** 18:42 Okay, thanks.
I'll just do the rebase for the main one, and do the crash reporter then.
**Bryce Buchanan** 18:50 Cool.
Alright, yeah, and I'll review the crash report, PR as well.
Okie dokie.
**Billy Zhou** 18:58 you know, when I'.
**Bryce Buchanan** 18:59 Or at least the feedback.
Alright.
**Billy Zhou** 19:04 Thanks, guys.
**Bryce Buchanan** 19:05 Yep, have a good day!
**nacho** 19:08 Bye.
