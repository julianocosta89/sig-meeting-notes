SIG: Swift SIG
Date: 2026-01-15
Duration: 16 minutes
Zoom Recording URL: https://zoom.us/rec/share/9Jom_aL7i_udmY1JWZ6VM2lnPOKa71grs5rAZSbwbpiZg9XzJISaRpxrils3WRO3.GRC0Ux7vXud17thO
============================================================

## Zoom Recording Transcript

**Bee Klimt** 02:55 Well, I got nothing this week. I don't know how long we should wait for the, maintainers.
**Arri Blais** 03:04 I am thinking I might wait until 5 passed.
them.
You know.
Because I got nothing, too. I was just gonna be a fly on the wall or whatever.
**Bee Klimt** 03:23 Yeah, same.
**Arri Blais** 05:50 I think I'm just gonna drop, I'll see you all later.
**Vinod Vydier** 05:54 Oh.
Yeah, it was actually…
**Arri Blais** 05:58 Okay, my, my apologies. Yeah, yeah. I did see you join Vinod, my, my bad.
**Vinod Vydier** 06:04 No problem, no problem. I was actually gonna wait for Ari, because he was gonna run the meeting today, but I didn't think he's joining, so… I can run it, or…
Yeah, let's, let's discuss what are the PRs that are… been submitted, let's…
**Billy Zhou** 06:24 Yeah, I think Billy… Billy's already sharing, right? Yeah.
Yeah, it seems like it was having some availability issues, actually. It's kind of weird.
Okay.
Well, for current state, immersed in, Swift V6, upgrading core.
Man, GitHub's really sucking today.
Yeah, so I had some weird…
I don't know what this is, Vino, do you have any context on this?
**Vinod Vydier** 06:57 Hold on, hold on, let me, let me actually get on the computer.
**Billy Zhou** 07:01 sure.
**Vinod Vydier** 07:02 Yeah.
**Billy Zhou** 07:03 Okay, anyways, there's this, workflow that goes on merge.
And, yeah, I can take a look at this later, but, we should be getting ready to release this, soon.
Probably as a major version upgrade.
Yeah, in the meantime, I don't think there are any open issues against, the court.
repository.
Yeah, just some stuff, did, and…
As soon as it's done loading, we can take a look at what these are.
Okay?
**Vinod Vydier** 07:45 Okay, I'm also, yeah, so…
**Billy Zhou** 07:48 Oh, yeah, okay, do you know what this, OSSF scorecard is?
**Vinod Vydier** 07:57 Is that… I think it's, again, automated thing, right? Yeah.
**Billy Zhou** 08:02 Okay, yeah, I'll take a look at it later. Okay. But I guess it's,
Yeah, it didn't surface until we merged.
And then… There's, like, all this stuff that Bryce did. Async OA APIs for exporters.
**Vinod Vydier** 08:23 Yeah, this is something that, we discussed last time, where…
I don't know, has anyone picked this up?
So the exporters…
Or, I think we were talking about having a sync a bit, because, currently, I think.
It is waiting, right, for it to export, and if it doesn't, it times out.
**Billy Zhou** 08:51 Oh, I see. Yeah, I actually did notice this,
When I used it for ADOT, Okay.
But I didn't… I didn't fix it, obviously.
Okay, take a look at that. Man, GitHub, maybe, maybe they're either getting paged because of some issue.
**Vinod Vydier** 09:17 No.
**Billy Zhou** 09:20 Haven't heard of any LLCs going on.
**Arri Blais** 09:26 Yeah, it says there's an incident on their status page, incident with issues and pull requests.
Just start luck.
**Billy Zhou** 09:35 Yeah.
Not good.
That's great.
I guess we can look at the, the Google Doc for the notes. At least we can look at that, see if anyone posts anything. Does anyone have a link, Andy?
**Vinod Vydier** 09:57 Yeah, let me, actually, I can open it up.
**Billy Zhou** 09:59 Yeah, since we can't really read anything.
**Vinod Vydier** 10:17 Let me share… oh, you can, you know…
**Billy Zhou** 10:32 I can look for it as well. I think it's in the calendar invite.
**Vinod Vydier** 10:36 Yeah, yeah, I got it, I got it open, I can share my screen.
**Billy Zhou** 10:39 Yeah, go for it.
Configuration for metric yet… Okay, it's merged.
monotonic clock… Yeah, I think all these issues are resolved.
**Vinod Vydier** 11:00 This is from the last week right here.
**Billy Zhou** 11:06 Okay, that's, that's good.
**Vinod Vydier** 11:08 So the only thing that is, this is the one that… with a Swift 6…
That is just about…
Oh, you were looking at this, okay.
**Billy Zhou** 11:31 Yeah, I just, I'll just add some more bullet points, so, ex…
OSR, whatever that thing is called. What's it called?
**Vinod Vydier** 11:43 Oh, sweet.
**Billy Zhou** 11:44 OSSF card.
**Vinod Vydier** 11:48 Okay, so this is also unknown, okay.
**Billy Zhou** 11:51 And, rebase me…
**Vinod Vydier** 12:10 Actually, you should probably… let me copy this over, you can…
Because, we are putting it on the…
Oh, yeah, sure. Yeah, you can type in, and then you can, yeah, copy it over to the top.
**Billy Zhou** 12:24 Very cool.
I already made it, thanks.
**Vinod Vydier** 12:36 Okay, perfect. Actually, you can put the other, the monotonic call as well, because, we can keep that as pending for next week.
Right.
**Billy Zhou** 12:45 Oh, is it not merged.
**Vinod Vydier** 12:46 Oh, no, let's see…
**Bee Klimt** 12:48 I think it is.
**Vinod Vydier** 12:50 Okay, so that's also… you can just mark it as done then.
In the previous… yeah.
Oh, let me just do that.
**Billy Zhou** 12:57 Thank you.
**Vinod Vydier** 13:18 Okay.
Oh, I think I… I should have left this the way it was here, and then…
**Billy Zhou** 13:52 Okay, and then, taking a quick look at the latest… Issues, if you're standing weird.
Doesn't seem like we have any new issues since early December, so that's good.
**Vinod Vydier** 14:05 Yo.
**Billy Zhou** 14:08 Checking for escalations now… Dependency dashboard.
That's true.
That's just a bot, okay. Okay, no escalations, since early December.
**Vinod Vydier** 14:28 What is this one? I don't know if I remember what Bryce did on this.
Let's…
**Billy Zhou** 14:35 Oh, yeah, I meant to take a look at that earlier, but… Post loading.
**Vinod Vydier** 14:41 No, he's assigned it himself, but I think this is where…
Seems, good.
Was it the version…
100 version 1.3.
**Billy Zhou** 15:06 Sure.
**Vinod Vydier** 15:12 Okay, I think we can wait for…
Anyway, I think Bryce has responded, so we can wait for Bryce to come back on this.
**Billy Zhou** 15:21 Yeah, I haven't caught up to speed on metrics stuff.
Seems like he did a breaking change to how you record raw histogram.
Let's see…
And he's doing, metric and stuff, but it's, he's using the Metrics API, so it's unfortunately…
**Vinod Vydier** 15:47 Unrelated to Bea's work.
Okay.
**Billy Zhou** 16:00 Okay, yeah.
**Vinod Vydier** 16:03 If, there is no other topic we can… discuss the list next week.
**Billy Zhou** 16:11 good.
**Vinod Vydier** 16:12 Better attendance, yeah. Okay.
**Billy Zhou** 16:14 Thanks, guys. See ya.
**Vinod Vydier** 16:14 Alright, thanks.
**Bee Klimt** 16:16 Bye.
**Vinod Vydier** 16:16 Thanks, Bianari. Yep.
