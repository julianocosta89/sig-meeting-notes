SIG: .NET SIG
Date: 2025-09-16
Duration: 14 minutes
============================================================

## Zoom Recording Transcript

**Zach Montoya** 00:55 Hey, Blanche.
How are you?
**Mike "Blanch" Blanchard** 00:59 Ben. How you doing?
**Zach Montoya** 01:02 Pretty good.
Just decided to stop in.
From the, usually I'm on the, .NET instrumentation calls, but I figured I would drop into the .NET SDK ones to see how things are going.
**Mike "Blanch" Blanchard** 01:17 Yeah, it's kind of why I joined at this point, just to…
See how the project's coming along.
**Zach Montoya** 01:25 Yeah. Have you, been actively, contributing to the project recently, or are you working on some other things now?
**Mike "Blanch" Blanchard** 01:32 I've kind of switched roles at Microsoft, so I'm working more on, like, the OTel Arrow repo.
**Zach Montoya** 01:41 Oh, okay.
**Mike "Blanch" Blanchard** 01:43 More in, like, the collector space.
**Zach Montoya** 01:47 Gotcha.
**Mike "Blanch" Blanchard** 01:48 been writing a lot of Rust code the last, I don't know, 9 months.
**Zach Montoya** 01:53 That's exciting.
**Mike "Blanch" Blanchard** 01:54 It was a little intimidating at first, but no, it's kind of fun.
**Zach Montoya** 01:59 Yeah. I wish I had more reasons to write Rust.
**Mike "Blanch" Blanchard** 02:04 It's cool. Some days it…
I go back and forth whether I love it or hate it.
Because it's like, it… it just…
it's kind of like in .NET, you have, like, the analyzers, you know? But that's, like, in the compiler. Like, it's giving you…
You're not building your code unless it's, like, perfectly happy.
So when you're learning it, like, you're just fighting the compiler, and you're kind of learning through pain and suffering, but once you figure kind of out what it's telling you, and it all clicks into place, then it's kind of beautiful.
But I still love .NET.
**Alan West** 03:00 Hey, everybody.
**Rajkumar Rangaraj** 03:04 Hi, everyone.
Nope.
I'm sharing my screen, are you unable to view it?
Yep.
I think… Martin has added a topic here, but I don't see him… Here.
**Alan West** 04:56 Yeah, I think he pinged in Slack and said that he wasn't gonna attend.
**Rajkumar Rangaraj** 04:59 Okay, I did not pay attention to the Slack today.
Yeah, this makes more sense what he says. Probably, this is the PR that we need to review and merge first.
He created the direction as an issue also last week. He had a… as a part of this PR, the direction looked good to me, and I asked him to move out
And, I think every one of us,
agree on this, more or less. We did the discussion and everything.
Probably I wanted
all the maintainer and approver to take a look at it, as this time… this caused a lot of controversies last time. So, it would be nice for, everyone, every contributor to… in… here to take a look at this peer, and we merged this one. Once this gets merged,
we can go ahead and merge the .NET 10RC changes and do a beta package.
At this point.
**Alan West** 06:07 Yeah, it sounds good.
So I'm… Oh, I'm getting an echo, is that?
Because of the water.
**Rajkumar Rangaraj** 06:14 Maybe I'll go on mute.
**Alan West** 06:17 Oh yeah, I think that helped.
Strange.
Yeah, I've…
I'm good with this direction and this PR. Are we ready to merge it, I guess, is,
My only question.
**Rajkumar Rangaraj** 06:36 The only big change that we have performed is the… the OTLP exporter,
the header issue, that was a T, the trailing header issue that we have fixed. That's the major thing that we have done.
If need be, we can do a hotfix for that and release it, and then we can go ahead and merge this one.
**Alan West** 07:06 Okay, so yeah, so in my one, I want to fix.
You're saying do a release with OT fix.
Before merging an SPR.
**Rajkumar Rangaraj** 07:16 Yeah, even Martin also echoes the same thing, that we should be saying and doing the same. So, in case someone comes in at a later point and say that, like, like, we are blocked
Due to this change.
It would be very difficult for us at that point in time to do any release.
**Alan West** 07:37 Great.
**Rajkumar Rangaraj** 07:38 So we did some major fixes here.
the first and the… So, we did this long time back, all of these fixes, but still, no one asked for an immediate release and everything, but it's always good
To do the fix before we do, because we are going to block our,
the pipeline with all these new changes added to it. Probably if customer needs or any other critical things come, we may need to rely upon the previous tag and
Like, do ethical fixes on that.
**Alan West** 08:15 Yeah, worst case, we can figure it out.
**Rajkumar Rangaraj** 08:17 Yeah.
**Alan West** 08:18 Yeah, okay.
Sounds good.
**Rajkumar Rangaraj** 08:29 That's the direction of this one. I think we are in agreement, on this.
Is there any other topic for discussion here, apart from that?
**Alan West** 08:47 I don't have anything else for today.
**Rajkumar Rangaraj** 08:49 Good. Let me move on to the…
I think there were some new issues that were created.
One of them, all of them are, like, feature… most of them are feature requests,
This one is, like, there is a… Piotr created it to add a user agent to the OTLP exporter.
I think that should be a simpler one. And next is, I don't know, this is pretty new, and…
Don't know why it's here instead of the contribib.
Yeah, they were asked for a clarification.
It looks like an automatic instrumentation. Probably it's a kind of a misroute.
For this one, we will…
**Alan West** 09:44 And this is another tool. I'll be the first one?
The user agent customization.
Is that a spec… is that a spec change?
**Rajkumar Rangaraj** 09:53 Yeah, I think the spec now says the user agent could be added and everything.
**Alan West** 09:59 Gotcha, okay, I just missed that.
Good deal.
**Rajkumar Rangaraj** 10:04 Yeah, that's what we are going to do in here.
Let me move on to the PRs. I… just before starting the SIG, I merged the renovate,
the beer.
So I think, we should be good in to get, this one bumped as .NET SDK. I'm going to close this out and see how Renovate handles this, so I just left it for that, instead of me manually modifying it. Just want to see how Renovate does and how… what kind of maintenance burden it reduces.
Well, just closing this, and there is a…
support for ZZip added to the OTLP exporter. We don't have a very good integration test and everything, so I just asked, how did the test and ensure all the changes here works against all the variation and everything?
There is one other concern also I have, the way the code has been written. I see few allocation and everything, probably.
once I have an answer for that, I might ask them to do a benchmark and see what kind of allocation is happening with these changes.
With the compression being enabled.
I think Martin addressed.
**Alan West** 11:26 collection. I have this vague memory that… Compression… HTTP client.
had compression enabled by default, I…
don't know what type of compression. I guess I would have assumed that it's GZIP, but…
I guess I'm not sure about that.
Is there any mention here?
**Rajkumar Rangaraj** 11:52 I did take a look at it. It's a manual compression that's been done.
In… in… in somewhere here. They had a compression method, and… That's where the… yeah.
the actual GZIP compression happens. It's not… there is no mention of whatever you called out, right?
**Alan West** 12:18 Hmm.
**Rajkumar Rangaraj** 12:22 this needs a very careful and thorough review, so, yeah. Martin also has left a lot many, comments about the… he did not ask directly about the puff, but his questions were indirectly related to the puff stuff, so I think we are on track with the reviews. I'm waiting to hear back from the…
contributor here.
The next… we don't have anything that's…
Big that's missing over here. Mmm…
So, I have a few years need to catch up. Still, I did not find the complete time, or I did not see that it's much more higher priority than the other PR, so I could get the other things merged and kept this,
when the other things goes off, that's when I would be able to get to this one.
Yeah, that's all I have it from all of this,
I think, Alan, like, I think an additional maintainer over here will… I feel it will reduce the burden.
Pyotr is doing a very good job in keeping up things up-to-date and everything, but he might have not worked on the features here in the SDK very well, but he has proven, like, capability from the… both Contrib and the auto-instrumentation repo shows us, like.
he can take good care of it. So just want to take your thoughts before I reach him out and see if he has interest towards it.
**Alan West** 14:06 Yeah Yeah, I would support that.
**Rajkumar Rangaraj** 14:10 Okay.
Cool, that's all I have it here,
There is nothing else I think we could end now.
**Alan West** 14:27 Sounds good. Thanks, Rosh.
**Rajkumar Rangaraj** 14:28 Thank you, everyone.
