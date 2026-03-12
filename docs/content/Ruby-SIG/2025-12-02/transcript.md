SIG: Ruby SIG
Date: 2025-12-02
Duration: 20 minutes
Zoom Recording URL: https://zoom.us/rec/share/yhmjy8WK1IcRwMMv1iw4sB6ZljsZiL-w2qioAlJt09jsjtGkk_cASYvlAlTf91y0.FUdnvhQr5SZEF-zA
============================================================

## Zoom Recording Transcript

**Kayla Reopelle** 04:20 Hey everybody, I see some new faces, or at least new to me. I am sick today, so I don't have a huge voice to lead the meeting, but I'll get the agenda in the, In the chat, and if anyone has anything that they want to talk about today.
Please go ahead and add it. Oh, I guess we don't have a knot, a little spot for today.
**Hannah Ramadan** 05:06 And I can share my screen so we can look together.
**Kayla Reopelle** 05:10 Thank you. Sorry, I thought I was doing that. Thank you, Hannah.
So yeah, is there, I didn't go to the Spec SIG today.
Can take a quick look at it.
Mmm, yeah.
Let's see… Is that enabled API for synchronous instruments? Is that related to the work that you wanted Wendy to, Be able to add and remove instruments?
**Wendy Smoak** 06:32 I'm sorry, I just sat down in the… I didn't have sound for a second there, so which one?
**Kayla Reopelle** 06:38 The first point, the stabilized Enabled API for Synchronous Instruments.
Because I thought that conversation kind of resurfaced.
**Wendy Smoak** 06:47 Synchronous is just not the… not the ones that have callbacks.
**Kayla Reopelle** 06:52 Okay.
**Wendy Smoak** 06:54 So, I don't think…
**Kayla Reopelle** 06:58 Okay.
**Wendy Smoak** 07:03 I haven't heard anything further on being able to… there's a whole separate conversation about being able to remove.
**Kayla Reopelle** 07:09 Right.
**Wendy Smoak** 07:10 Which, if that work… like, that seems to be further along, and if that works, it seems like being able to get will come for free, because how else are you going to remove it? So I was kind of… and I haven't really been back to it.
**Kayla Reopelle** 07:23 Okay.
Sounds good.
**Hannah Ramadan** 07:39 This one says your SIGHB should have a new issue regarding implementing support for this flag. I don't know if I saw that come through.
**Kayla Reopelle** 08:00 Yeah, they might… it might not be until it merges.
**Hannah Ramadan** 08:03 Makes sense.
Oops, we can keep an eye out for that one.
**Kayla Reopelle** 08:16 Oh yeah, and the FYI at the bottom goes for our SEC as well, so we'll have the SPECSIG meeting The next 2 weeks, and then we'll take… I think the final two Tuesdays of the year off.
All of OTEL is just kind of having an end-of-year break.
**Hannah Ramadan** 08:35 Nice, that makes sense.
Cool. Anything else to dive into here? That looks pretty good to me.
**Kayla Reopelle** 08:47 No, I don't think so.
**Hannah Ramadan** 08:50 Perfect.
Cool, I guess we can get into any new core issues?
Oh, nope, there it is.
**Kayla Reopelle** 09:04 Nice.
**Hannah Ramadan** 09:06 They're on it.
So we know what that one is. I think… I don't know what Renovate…
**Kayla Reopelle** 09:14 Yeah, so Renovate is a new tool that we're experimenting with.
It can do two things. One of the things is there's automation to help support, like, doing things like refreshing, creating a PR to update our proto versions, you know, automatically.
Or, kind of do the same with semantic conventions.
It also, has the same functions as Dependabot.
So, we'll eventually be replacing, I think, Dependabot with this feature.
But, yeah, that got merged before… the, the U.S. Thanksgiving holiday.
And I don't think we've fully updated things yet for it.
**Hannah Ramadan** 10:04 Nice.
Cool.
**Kayla Reopelle** 10:25 Yeah, yeah, I guess maybe for these, oh yeah, do we want to talk about that one?
**Hannah Ramadan** 10:35 I forget if we talked about this last time, bye.
Can't remember if there was a PR associated with this one, maybe not.
**Kayla Reopelle** 10:59 I think not yet.
**Hannah Ramadan** 11:00 vehicle.
**Kayla Reopelle** 11:02 Okay, looks like there's a release for today.
Or maybe… Oh, I think… Okay, gosh, I thought I released that. My, My sick brain is far behind.
Alright, I'll, I'll get those today.
**Hannah Ramadan** 11:37 I still got the changelog updated, so that's nice.
Let's see… Another tool I've never heard of, but Monitor, I guess that's when we use, too.
**Kayla Reopelle** 12:09 Interesting, okay.
**Hannah Ramadan** 12:17 Okay.
**Kayla Reopelle** 12:36 Oh, nice, okay.
**Hannah Ramadan** 12:41 Yeah, that…
**Kayla Reopelle** 12:43 I guess, yeah, maybe, maybe we don't all…
**Hannah Ramadan** 12:47 I need to look at these.
**Kayla Reopelle** 12:48 need to look at them. I guess, is there anything that anyone here wants to prioritize for this week?
**Wendy Smoak** 13:12 not to be assigning work to Schwann, but that, thing where you… where it'll overflow the cardinality into just a single bucket. If you get too many… Data points? I thought it was in progress.
I need to go find the…
**Kayla Reopelle** 13:30 Oh, I think that makes.
**Wendy Smoak** 13:30 issue again.
**Kayla Reopelle** 13:31 The work that's queued up to be merged.
**Wendy Smoak** 13:34 Maybe.
**Kayla Reopelle** 13:35 Yeah, they're really…
**Wendy Smoak** 13:36 Fabulous.
That's been my one thing, that someone could possibly break it without that.
So, yay, and thanks, Sean, for all that work.
**Xuan Cao** 14:00 Do you think that's useful? Because I feel like adding those, makes a code, messier.
I was, I was looking for some, like, more elegant way to, you know, enforce that rule, but… I just don't have time to do that.
**Wendy Smoak** 14:18 Got it.
All of the work in general, not that specific one. Thank you.
You've done a lot on metrics.
**Hannah Ramadan** 14:44 In control, but didn't seem like there were any new issues, really, to… to go over outside of the dependency.
**Kayla Reopelle** 14:51 Update by renovate.
**Hannah Ramadan** 14:53 Unless anybody has one they want to talk about here.
**Kayla Reopelle** 15:03 And we'll get those releases out. Can you just, pop into the release gems and, see which ones it is?
Oh, okay.
Nice.
Is that something, Hannah, that you think we're good to release now?
**Hannah Ramadan** 15:27 Yes, yes.
**Kayla Reopelle** 15:29 Okay, great.
**Hannah Ramadan** 15:31 It'd actually be great to get that one out, because we're still popping in a little deprecation notice in people's, Console's from the old gem, so that'd be great.
And then we can probably go ahead and, if we want, I think maybe delete the old gem, SQL obfuscation? I don't think we have to, necessarily, but… Like, immediately, but… Something to do, probably in the next few.
Looks like a new issue from ARIA, or a new PR from ARIO.
Making use of the new gem, nice.
**Kayla Reopelle** 16:39 Nice.
**Hannah Ramadan** 16:43 I'm not really familiar with this spec, but I would love to take a look at this one, so I'll prioritize doing that.
Nice.
We have a… I think this might be new-ish?
OpenAI Instrumentation by Schwan.
Nice.
**Xuan Cao** 17:16 Yeah, I just wanted to mention, this one is for the official, OpenAI gym, which has actually have a lower star than the, the community code one, OpenAI Ruby.
But the reason I wanted to start. I mean, we can have, like.
two separate instrumentation for… which is for OpenAI, But, start from, just, starting from this, because it's official from OpenAI, company. So, they… Well… For sure, maintain it.
For a longer time, so…
**Hannah Ramadan** 18:01 Yeah, that makes sense.
**Xuan Cao** 18:06 And, and for the Python, they actually do have, like, two, implementation, for the opener.
**Hannah Ramadan** 18:28 Cool. I'd love to take a look at this one as well.
Does anyone want to talk about any of the other PRs here?
Or have any burning questions, or happy reports?
Nice, could be an early one. I see in the comments, hey Ronald, nice to meet you.
**Ronald Ekambi** 19:30 Nice to meet you all.
**Hannah Ramadan** 19:47 Nice. Well, we could call it.
Early. Does anyone have anything else?
**Wendy Smoak** 19:59 Nope, nothing here.
**Kayla Reopelle** 20:03 Oh, thanks, Anna.
**Wendy Smoak** 20:05 Hope you feel better, Kayla!
**Kayla Reopelle** 20:07 Thanks, Wendy.
**Hannah Ramadan** 20:10 Nice. See you next time.
**Kayla Reopelle** 20:16 Bye.
