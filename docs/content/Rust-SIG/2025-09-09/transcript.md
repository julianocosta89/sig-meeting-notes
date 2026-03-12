SIG: Rust SIG
Date: 2025-09-09
Duration: 17 minutes
============================================================

## Zoom Recording Transcript

**Cijo Thomas (Microsoft)** 01:44 Hello?
**Sven Cowart** 01:48 Hey, how's it going?
**Cijo Thomas (Microsoft)** 01:50 Wait, hey, we can wait maybe another minute to see if anyone else joins.
Yeah, feel free to add your name to the list of attendees.
**Sven Cowart** 02:40 How can I find this lock?
**Cijo Thomas (Microsoft)** 02:42 I can put it in the chat, Zoom chat, but it's usually shared in the… Teams channel.
And we have it in the.
**Sven Cowart** 02:54 Slack.
**Cijo Thomas (Microsoft)** 02:57 I think there should be a contributing document in the report.
**Sven Cowart** 03:02 I see it now.
**Cijo Thomas (Microsoft)** 03:04 Yeah, this should con… yup, this one.
This is a contributing section which has link.
Let me just make sure that's the right one. Oh yeah, that's the one.
Okay, I think we can get started. We didn't meet last week, I believe, most of the people were on the Rust conference, including myself.
And from the meeting notes, I can see we did not have anything last week. Yeah.
Looks like there are… some new folks, I think… I don't think I ever seen, like, Sven before. Nikhil, I think you have been here before. Christian, I think I saw your name, like, somewhere in the, yeah, last few weeks. But if anyone wants to do a quick intro, like, please, go for it. Maybe, like, Sven, you can start.
**Sven Cowart** 03:55 Yeah, yeah, so I'm, Sven Cowart. I'm co-founder and CTO of Elastiflow. We're getting into, the hotel space. We're… Focus on network observability, and, Like, there's a big opportunity in the hotel space specifically to provide better network telemetry As a whole, is it SEM… new SEM, semantic conventions or otherwise, but we have a number of Rust projects going on right now.
**Cijo Thomas (Microsoft)** 04:28 that…
**Sven Cowart** 04:29 Where we intend to use the OTLP ecosystem and the Rust libraries that I think we're discussing here, and so I'm just kind of trying to get plugged into the community, the OTL community as a whole, and see where it goes, and see how we can contribute.
Back to the community, push it forward in a positive way.
**Cijo Thomas (Microsoft)** 04:53 Okay, yeah, glad to have you here. Feel free to look around for any issues which you may find interesting to work on.
**Sven Cowart** 05:01 Sure.
**Cijo Thomas (Microsoft)** 05:03 Anyone else wants to do an intro?
I think, Christian, you are probably the only relatively new person, Okay, if you want to skip also.
**Christian Leghadjeu** 05:17 No, I think I was… I was in the first meeting two weeks ago, just I was on a vacation, so I could not attend last meetings.
Babindeer, I think you… There was one meeting with just both of us.
Hmm.
**Cijo Thomas (Microsoft)** 05:37 Just give me one second, I need to relocate my laptop, so I'll be back in, like, a few seconds.
**Christian Leghadjeu** 05:43 Yo.
**Cijo Thomas (Microsoft)** 06:19 Okay, I am back, I'm still… I hope I'm still sharing my screen.
Oh, yeah, okay.
Yeah, there is only one topic, put in the agenda.
Which, I believe Scott has put, asking for reviews. We haven't gotten to it.
Yeah, Beyond has already reviewed.
Yeah, I think it's more like call for, reviewers, Don't think we need to discuss anything in this call.
Beyond, like, do you think anything, any open topics in that PR which could use a discussion right now?
**BA Björn Antonsson** 07:03 No, I have, I only reviewed the HTTP part, so I'm gonna take a look at the… at the… The tonic changes as well.
But, yeah.
**Cijo Thomas (Microsoft)** 07:16 Yeah, there was, like, some comment earlier about… In order to do retry, we need to stabilize the…
**BA Björn Antonsson** 07:24 I think… I think that's been changed, so we broke out the part, so it's… at least on the HTTP side, it's… it's very well hidden, so you don't have to… you only need to enable that if you want to retry.
**Cijo Thomas (Microsoft)** 07:43 Got it. Okay, yeah, I'll take a look. This should be quite interesting.
One, Yeah, and since there is nothing else, we'll quickly go through the open issues. There are a few more PRs that requires attention.
But yeah, pretty much no action occurred last week, so we'll have to get back to it this week.
like, there are a few small PRs, you have something to… Optimize the preference… not… okay.
**BA Björn Antonsson** 08:17 I was just trying to stabilize the benchmark results, but I… I… I'm at a loss. I think, I don't know.
I think, we're trying to measure two small things sometimes that rely on allocations and, and… The numbers are just… Moving.
**Cijo Thomas (Microsoft)** 08:40 Yeah, it's, like, we are measuring, like, most of the things are, like, in nanoseconds, very low nanoseconds, so… yeah, even a simple cache miss or anything will, Fluctuate… cost fluctuations in the number.
I don't know whether we have… Started running it in the… Dedicated machines… Yeah, that's something which we should be able to leverage now.
I forgot, like, Scott was looking at it.
**BA Björn Antonsson** 09:12 I think it… there was an issue with, outside… Like, forked pull requests not being able to run on those machines.
**Cijo Thomas (Microsoft)** 09:20 Yeah, but we did fix that, yeah, I'll follow up, actually, because in other repo in OpenTelemetry Arrow Collector, we were able to use the new dedicated… Machines.
Yeah, it's, like, much more powerful, and you get, like, exclusive access to that machine. It's something which we are already using in, like, Arrow Repo, and other… I mean, in Arrow, I know it works, because I was trying to get it to work.
Yeah, I think that may be another thing which will give us better stability than the typical GitHub runners.
But anyway, nothing actionable right now. I'll check with Scott if we are in a position to switch to that, or we are already switched.
yeah, I think I'll go through the issues, and, like, thing which… I don't think there is anything worth, discussing here, so we'll go to the issues.
Okay, there is request for Awesome. Unfortunately, we don't have… a good support. We have been accumulating issues related to wasamine to this label. We have, like.
multiple of them right now, so… yeah, it's… if anyone has, like, more experience in, like, awesome, we should work on adding it, but the first step would be to… add a CA check, which compares against that platform, and run some tests, so we'll know exactly what is failing.
And then work toward, like, adding it, but I don't think we have the bandwidth to cover that, so most likely we'll have to just leave it like that.
Validate feasibility. This is a spec issue.
Yeah, we'll need to take a look at this, right? We, like, Spec had put a, explicit statement saying… Like, changing or adding new types to… Attribute values are, like, considered breaking change, but they… since backed off.
So for now, it's okay for Rust, because we marked our, value as Non-XOST, so we can technically, add new things.
But whether… That's something which we intend to continue forever. That's to be discussed, I think. If I remember correctly, it should be… Yeah, we marked it with XOST, so we can add, like, new types, without… Making it as a breaking change.
But we'll need to see whether that's something which we can control. Anyone has, like, comments on this one? Nothing important to address right away, but something to keep in mind.
Okay, if not, I'll just move to the next one.
**lalit** 12:15 Aww.
**Cijo Thomas (Microsoft)** 12:16 This has a PR, this one, I will come back in a moment.
These two are, like, us, feature us, which is already, replied to.
And there is… relatively small one, so we should be good, yeah. I want to, like, quickly talk about this one.
So we did have a PR to bump, Tony Kan Prost to the latest version.
Usually, we don't do a one-off release, but many people, even in this PR, were asking, can we do a one-off release for just the… Proto, maybe, like, OTLP crates, because the newer version of Tonic has, like, some security issues addressed, and people want to move to that one.
We cannot do a blanket release at this moment, because we are in the middle of, like, breaking changes, so we want to… like, to the next release, once we are comfortable that we have done the bulk of the braking changes. It's mostly related to tracing, but it's still a braking change.
Anyone have thoughts or comments on doing a… one-off release for just the protocol crate, and probably the OTLP crate. That's only when we should depend on this change.
**lalit** 13:34 It should be okay. I mean, just to add that Proto has a new version.
probably I'll create a PR to bump up the proto version itself, and then probably we can take both of them.
**Cijo Thomas (Microsoft)** 13:46 When you say Proto, the OTLP protocol.
**lalit** 13:48 OTLP photo, yeah, sorry. OTLP photo, yeah.
**Cijo Thomas (Microsoft)** 13:51 I think if you can do that, and then we can do a one-off release for this one.
Do you know if OTLP exporter itself would require… A new release, or… This alone would be sufficient.
I'm not quite sure how the dependencies are organized, whether… There was not… we didn't have to touch the OTLP exporter, because all the serialization is done in the… Protocrerate, so most likely… This would just work.
**lalit** 14:26 Lilith, like, will you have a moment to check if we need… I can check that, yeah. I can check that, yeah.
**Cijo Thomas (Microsoft)** 14:32 Yeah, if needed, yeah, we can do… because these are on the edge, like, leaf things, so we don't need to release anything else if you're just releasing a point one of these two, yeah.
Oops.
Yeah.
Okay, that's pretty much the issues we want to cover, and since we have plenty of time left, like, if anyone has topics to discuss, let's take it now.
Okay, like, beyond, like, since you are here, one quick question. So, I saw that the tracing open elementary PREs merged, does that mean, like, we are now completely unblocked from making, breaking changes, doing the cleanups in our tracing API.
**BA Björn Antonsson** 15:24 Yeah, I actually started doing that, and I noticed there is one thing that is still… That is still, being used on the other side, so to say.
But I can… I can clean that up in… in… Tracing OpenTelemetry as well, and do those changes here.
**Cijo Thomas (Microsoft)** 15:46 Okay, yeah, makes sense, yeah. Like, once you, like, start doing it, then only you'll realize, okay, there are more things to clean up, but I'm happy to hold the next release until we at least get the, APIs to be, like, I think we… Marte.
Tracing API stable milestone, which is put at end of this month.
We'll see how much we can figure out, because most of these things are… like, relativity does not change, we are simply.
**BA Björn Antonsson** 16:13 window.
**Cijo Thomas (Microsoft)** 16:14 Because of tracing.
**BA Björn Antonsson** 16:15 Exactly.
**Cijo Thomas (Microsoft)** 16:17 Alright, yeah, I don't have anything else, like, any… any other topics people want to discuss, we can do it now, otherwise we can give back time to everyone.
Okay? Nothing. We can end early today. Thank you, everyone. I'll see you next week. Bye-bye.
**BA Björn Antonsson** 16:38 Beer.
