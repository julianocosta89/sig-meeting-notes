SIG: Ruby SIG
Date: 2025-09-30
Duration: 25 minutes
Zoom Recording URL: https://zoom.us/rec/share/pCv80BzRYO1g6rR1_Gd2C5hkcOINeVhmTtMBV5NcouM_0Y7zatglrOxtGlI5YeHx.uTXxtbpSoZw8QbU8
============================================================

## Zoom Recording Transcript

**Kayla Reopelle** 01:41 Hi, everyone!
Let's see… Don't know of anyone else who's… Definitely joining us today.
Yeah, Eric and Eric and Arielle aren't able to come, so I think we might be good to start.
Okay…
So… Specsig, I… I got there late, and it was already over. So, let's see what is,
Going on?
User Facing Logging API. Oh, that's interesting.
Versus just the existing logging API that's a bridge.
So that… could impact us.
Adding code info in a span.
File name, line number…
Okay, yeah, we do something similar to this in New Relic's proprietary agents.
I kind of thought that was already a… a thing in hotel, but…
I must be mis-thinking of something else.
Oh, and the trace ratio-based probability sampler is deprecated, and…
This is part of a plan, I guess, for how they're going to remove it.
I forget what it is. Sorry, I'm, like, full of unhelpful information. I forget what it is that it's being replaced by. I guess the probability sampler.
That's what it looks like here.
Yeah, we'll need to look into this to see if that means we need to remove our sampler, or just mark it as deprecated.
And…
Disabled config must be eventually visible.
Oh, I think it just, like, needs to be…
exposed so that someone in code could find it, which I think would be kind of hard to not have happen in Ruby whenever we implement that feature.
Oh yeah, and it's getting close to Open Telemetry Governance Committee election time.
there, if you would like to vote, and you haven't been detected as a member of standing, come to this Community Issues 3001, I guess I'll put this in the notes.
And I think they're also still accepting nominations, so you can nominate yourself if you're interested in joining the governance committee, or nominate someone else, but…
That is… that it is the season. So, GC…
Cool, cool. Alright, yeah, nothing on the agenda. I…
really wasn't able to work on OTEL last week, so I'm still catching up on notifications. Is there anything in particular with Core and Contrib that people want to…
Take a look at.
If not, one thing that I'll call out that's happening with Contrib…
is that, we're gonna have a bunch of new versions of GEMS very soon, by updating the minimum OTel Ruby API to 1.7.
I think we had a bunch of releases this morning, but it looks like there are a few errors, so,
Ariel is working on fixing them, but expect a couple releases probably today to get that up and running, and then that should get us back into a state where all can be installed, or at least our installation tests were failing because of a mismatched OpenTelemetry API version.
Also, keep an eye out,
that the minimum Ruby version for Contrib, and I think also Core soon, will be, raised to Ruby 3.2, since that's no longer supported by the Ruby maintainers, and we try to,
Align with, you know, what the… Libraries and the language.
Has official support for.
Yeah.
Okay.
So, yeah, I guess, sorry, while we're on Contrib, was there anything else that people wanted to…
Take a look at…
Actually, this one might be a good source for discussion. So there's a PR open right now that proposes relevancing the version constraints in Instrumentation All to just have minor version.
limits.
And since, you know, none of these gems are at a 1.0 yet, that would just have all automatically bring in whatever the next version is.
I think we tend to just kind of try to release them at the same time, to have all except the new version, but since we do introduce breaking changes often in these minor versions, since we're not at 1.0 yet.
That could cause some unexpected behavior for users. So I think if this is… something…
You have thoughts about.
**Robb Kidd (he/him)** 09:18 Well… Okay. It came from Robert, which has me going…
Which has me… I was gonna say, how about no? But it came from Robert.
Yeah, yeah.
**Kayla Reopelle** 09:28 I think Yeah, there were some issues because of this anthropic…
minimum version that I think maybe this PR came out of, I'm not sure.
**Robb Kidd (he/him)** 09:37 Okay.
**Wendy Smoak** 09:41 Yeah, same. That's supposed to work because of semantic versioning. Like, the reason you can just say, oh, any minor version is okay is because semantic versioning
Means that the developers are… Guaranteeing or making an effort to not break stuff, but… It's a free-for-all, so…
**Robb Kidd (he/him)** 10:01 Well, it's, it's like, until you get a 1.0,
Everything sort of shifts right on the semanticness.
**Wendy Smoak** 10:09 I'll see you.
**Robb Kidd (he/him)** 10:10 arrow dot release. So, like, That's why we're, pessimistic.
At the patch level, because… Until we go 1.0, we can break… In, in patches.
**Wendy Smoak** 10:25 And this makes you… having the dot zeros there makes you, like, explicitly say, this works with that.
**Robb Kidd (he/him)** 10:33 Or at least within a, within a minor.
It's like major… Breaking changes, we would… we would increment the minor version with these zero dots.
**Kayla Reopelle** 10:46 Yeah.
**Robb Kidd (he/him)** 10:47 Semantics shifted a decimal point, right?
**Kayla Reopelle** 10:53 And I don't think we'll make a major version like 1.0 until we have stable conventions for them, and also probably metrics included as well, is my guess.
But at a minimum, stable conventions, so it kind of aligns with the instability of the conventions.
**Robb Kidd (he/him)** 11:10 What's the problem?
I'm still trying to hunt down this issue.
**Kayla Reopelle** 11:16 the… the problem… sorry, I'll drop it in the notes, too. The… I think the problem is just kind of related to…
like…
needing to re-release the instrumentation all gem with the bump. Our release tooling has made that kind of complicated. There was a permissions issue in the past few weeks that prevented us from releasing all, because our release process right now requires, you know, manually editing the release PR.
But, that is resolved now, and we hopefully won't run into a problem like that again.
But I do…
Yeah, I do worry that this is more than just a chore. This is probably more of a breaking change for users.
**Robb Kidd (he/him)** 12:06 Yeah,
We can rev the minor on it, and then…
**Kayla Reopelle** 12:15 Yep.
Yeah, I think… I think this is worth talking about on the PR, if there's concerns.
I'm somewhat concerned, I feel like the…
Extra stuff is helpful, but yeah.
**Robb Kidd (he/him)** 12:37 My gut tells me that, somebody using the All Gem probably wants the convenience of, just give me the latest.
this change could surprise them with… the latest would bring in a breaking change. The workaround would be
Put a more pessimistic version constraint in your own project's gem file.
**Kayla Reopelle** 13:00 Yeah, that's what I heard.
**Robb Kidd (he/him)** 13:02 So there's a… there's a reasonable workaround, but it's the… your telemetry might break until you notice.
Huh.
And the problem… the problem that this would be solving is…
The time it takes to do an all-release?
**Kayla Reopelle** 13:28 That's… My guess…
You don't have to wait for a release of Instrumentation All, if you're using Instrumentation All.
And I do think with the current setup, you could not just install a newer version, because you'd hit a permissions issue.
**Robb Kidd (he/him)** 13:51 Yeah, if you wanted a newer version of a specific instrumentation with this…
patch-level, pessimistic version. You couldn't take a new minor.
All would prevent you from using something newer.
**Kayla Reopelle** 14:04 Yeah.
**Robb Kidd (he/him)** 14:11 Yeah, I guess as Ariel notes, if we update the README, it's saying…
**Kayla Reopelle** 14:15 Yeah, yeah.
**Robb Kidd (he/him)** 14:16 All is a convenience thing, but because…
It's a zero dot, and every… go ahead.
**Wendy Smoak** 14:24 I was gonna say, I can't imagine anyone using all in production. I mean, it's just a… let's play with it! You just… you're just never gonna do that. No one should be doing that.
**Robb Kidd (he/him)** 14:33 Every… lots of people do it. I agree that… I agree that they shouldn't.
But lots of people do it. But maybe that's some things that we should put on the README. All is a convenience package. Like, if we go this route, make it convenient to bring in
the latest.
And we update the README and say, all's a convenience gem, we recommend not using it in production. You use it while you're sussing out which instrumentations you want, and then we recommend, when you go to production, get specific about your instrumentation versions.
Tune your version constraints to your risk tolerance.
**Kayla Reopelle** 15:15 Yeah, so I think this PR's maybe frozen until… Are y'all… Ariel's feedback gets addressed.
But I like… I do think we should make it clear in documentation if we are going to change.
**Robb Kidd (he/him)** 15:31 Yeah, and Wendy raises a good point. We should probably.
**Kayla Reopelle** 15:34 Yeah.
**Robb Kidd (he/him)** 15:35 recommend people not use all in production, like, all of your, that's your taste test experience.
**Wendy Smoak** 15:51 I mean, all's in Contrib, so it, like.
it seems like there's a point at which there's conflicting stuff in… like, you can't all at some point. Isn't there…
**Kayla Reopelle** 16:03 Yeah.
**Wendy Smoak** 16:04 Like, you're not gonna be using this and that. I mean, we may not be at that point yet, like, there's not enough stuff in there, but…
Just… I don't know.
**Kayla Reopelle** 16:11 Yeah, I don't think we're at the point where we have, like, multiple instrumentations for the same thing.
**Wendy Smoak** 16:17 Oh, and they… they… but they kind of detect, right? They don't…
**Kayla Reopelle** 16:20 Yeah, exactly. Exactly.
**Wendy Smoak** 16:23 Other gems there, so…
**Kayla Reopelle** 16:25 Yep, yeah, so it's, it's kind of just…
you know, no op code if you don't have whatever library installed. I don't think it'll come through and try to install them.
**Robb Kidd (he/him)** 16:37 I guess one, one advantage is if, if you use all in production.
When new instrumentation comes along, that instrument's something that you use.
You automatically get it, and suddenly…
**Kayla Reopelle** 16:49 And then you don't have to follow.
Yeah.
**Wendy Smoak** 16:53 Yeah, no.
**Kayla Reopelle** 16:55 Still no?
**Wendy Smoak** 16:59 I mean, I realize you've gone through staging at that point, you know, like, you've been messing with it, but still, like…
My gem files locked down to 3 digits. I know exactly what's going in production.
**Robb Kidd (he/him)** 17:10 Well, that's a… that's an interesting pattern, maybe, in,
Maybe there are patterns where you can use You can have.
**Wendy Smoak** 17:19 It probably depends.
industry, too, right? I mean…
**Robb Kidd (he/him)** 17:22 Yeah.
**Wendy Smoak** 17:22 Are you… are you doing financial stuff? Are you… Not.
**Robb Kidd (he/him)** 17:26 Financial stuff should not use all.
Please don't.
**Kayla Reopelle** 17:30 Yep, yep.
**Wendy Smoak** 17:32 Yeah, some more… some more advice on the… because…
A lot of people copy and paste what's in the examples and go for it.
**Robb Kidd (he/him)** 17:40 So there's probably a follow-up, not only README for this gem, but maybe we go and update the hotel doc site and say, like.
put some warning emojis around the example, like, here's getting started, don't…
**Kayla Reopelle** 17:52 Yep.
**Robb Kidd (he/him)** 17:53 all… all is a Wild West of…
All. And maybe you don't want all.
**Kayla Reopelle** 18:14 All right, cool. Well, thanks for discussing that.
Let's see, any, any other new… Issues…
Still working on the installation errors, it looks like.
All right, let's jump into core. Yep, there's the MIN3.2 PR there as well.
And I think the problem, at least on Contrib right now, is that the CIs for 3-1 need to be pulled out.
But, yeah, anything here that people want to call out to take a look at?
**Robb Kidd (he/him)** 19:04 Well, it's been a minute since I've been here, did the semantic convention stuff?
Moved on without me, as planned.
**Kayla Reopelle** 19:11 Yeah, we've got the semantic conventions Gem is out, yeah, your PR was merged and released, and, yesterday merged in an update to the README, but that… that won't trigger a release. I can trigger a release if we think that would be helpful.
**Robb Kidd (he/him)** 19:33 I was just checking and seeing if anything was held up by me.
**Kayla Reopelle** 19:36 No, nope, you're good, you're good.
Yeah, anyone else have a core issue that they want prioritized this week, or they want to discuss?
**Wendy Smoak** 19:56 I think you commented on one of mine where we were…
One of the logging issues, and said you might have a chance to look at it.
Oh, that's that.
**Kayla Reopelle** 20:12 Nope.
**Wendy Smoak** 20:13 Oh, maybe, maybe it got…
**Kayla Reopelle** 20:16 Maybe it got closed. I… I hope not.
**Wendy Smoak** 20:18 Oh, no, it's not a PR, it's an issue.
**Kayla Reopelle** 20:20 Oh, okay, I thought I was in issues.
Was it this one?
**Wendy Smoak** 20:28 Yes, if anyone has any ideas on how you could possibly
Like, we sanitize the heck out of things.
And I just… there… I don't know how to debug it.
Because I can't make it happen on purpose.
But someone else said they'd possibly seen it. It's just…
Can it say anything else, or do anything that would help?
**Kayla Reopelle** 20:56 Yeah.
**Wendy Smoak** 20:57 I just… and I haven't seen it recently, but…
**Kayla Reopelle** 21:00 Every once in a while, I was just, like.
**Wendy Smoak** 21:03 Shopping!
I can't… Figure out what… how it can even happen.
**Kayla Reopelle** 21:10 Yeah, because I think we have to have the UTF-8… I wonder if that's maybe an opportunity to add a config?
Because I don't think we're supposed to do any, like, coercion.
And… I'm… I forget… I'll… I'll look again today, Wendy. The… I don't remember if you have…
access to the string at this point when the error is raised. Hopefully you would…
But I guess would printing that string be an option, to help decode it?
Or…
**Wendy Smoak** 21:47 Yeah, I don't know, I don't know what's appropriate.
**Kayla Reopelle** 21:49 Yeah.
**Wendy Smoak** 21:50 Or if it's gonna, like, have bells, you know, like, if you try to print it, is that gonna make things worse? Yeah.
Could it, I mean, and then as, like, could it be something malicious?
**Kayla Reopelle** 22:01 Could it?
**Wendy Smoak** 22:02 I don't… I don't really quite know what's going on, but I just got stuck by that.
**Kayla Reopelle** 22:07 Okay. And we have… no, it's not an emergency, we have since moved on, and like, well, that was weird, but I don't have an answer for this, or any way to…
**Wendy Smoak** 22:15 Had to figure it out.
**Robb Kidd (he/him)** 22:17 What, what type of process did you see these errors appearing in? Was it a background job? Was it a web handler? Was it…
**Wendy Smoak** 22:25 I don't think I… oh, okay, I could probably figure out which… I don't remember which kind of server, so, like, we do have background servers and web servers.
That's a flashlight.
**Robb Kidd (he/him)** 22:37 What made me curious about, if it's a malicious thing, if it's trying to log some…
Something coming from users.
**Wendy Smoak** 22:44 It could, I mean…
**Robb Kidd (he/him)** 22:44 Actually, that could be in a background job, too.
**Wendy Smoak** 22:47 I don't know, I'm gonna… there are more web servers than anything, so I think it was possibly from that? I did have…
Something similar when, some debug logging was on.
And it was trying to pass probably some binary data through.
It's not that anymore.
So yeah, I just…
Because we already sanitized everything before we even tried to log it, because, you know, we've had this problem before. And it was super surprising, and there's just no, like…
So yes, if it could… if it could write it out, that'd be great, because then I would know what it was, but I'm not sure that's…
Appropriate or safe.
**Kayla Reopelle** 23:24 Yeah, yeah.
Right, and so seeing if we can UTF-8 check it earlier in the pipeline so that the batch isn't rejected because of that.
**Wendy Smoak** 23:34 Yeah, I'd rather drop the one.
**Kayla Reopelle** 23:35 and…
**Wendy Smoak** 23:36 Offending thing than the whole batch that it happened to get into.
**Kayla Reopelle** 23:40 Yeah.
That makes sense.
Yeah, I…
**Robb Kidd (he/him)** 23:46 Put some guards in the log exporter.
**Kayla Reopelle** 23:48 Apparently, it's inside a method missing.
Hmm.
**Robb Kidd (he/him)** 23:52 Which is exciting.
**Kayla Reopelle** 23:55 Interesting.
I'm also kind of surprised that we saw it…
in just OTLP exporter in code, and not a log exporter in code.
**Robb Kidd (he/him)** 24:10 I think it is.
**Kayla Reopelle** 24:10 So maybe that… yeah, it is. I guess I was just expecting the class name to be different. Maybe that needs to be updated.
Just a small thing.
**Wendy Smoak** 24:21 Anyway, just…
**Kayla Reopelle** 24:22 Yeah, okay.
**Wendy Smoak** 24:23 privileged since I'm here.
**Kayla Reopelle** 24:24 Yeah, thanks, Wendy.
Mmm.
Anyone else?
Alright, cool. Well, I'm… yeah, just working on taking down hotel notifications the rest of the day, so if anyone needs anything, let me know.
Cool. See y'all later.
**Wendy Smoak** 25:06 Thank you.
