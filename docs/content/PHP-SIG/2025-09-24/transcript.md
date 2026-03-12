SIG: PHP SIG
Date: 2025-09-24
Duration: 19 minutes
Zoom Recording URL: https://zoom.us/rec/share/J1To17tCigTbA2QUInHVLRKRu_5XsI9ycL6trhJ608G7nncJpun-ea664U7XNVac.IXAvp0pezWv_056t
============================================================

## Zoom Recording Transcript

**Brett McBride** 00:33 Hello.
**Bob Strecansky** 00:35 Hello, how are you?
**Brett McBride** 00:37 Good, thank you.
**Bob Strecansky** 00:39 Let me, I'm in a place… my Wi-Fi is, like, kind of spotty, so let me see if Zoom will work on video, or else I might have to be… Camera, let me double check.
Can you stand here today?
**Brett McBride** 00:55 I can see, yeah, a little bit laggy.
**Bob Strecansky** 00:59 Okay, so should I just go get you off of that better?
**Brett McBride** 01:03 Yep.
Are you able to screen share and drive, or would you like me to do that?
**Bob Strecansky** 01:11 I think so, let's… let's test it out.
**Brett McBride** 01:20 Welcome back, by the way.
**Bob Strecansky** 01:22 Thank you, thank you.
It was, had a really great… some really great time off.
**Brett McBride** 01:30 Wonderful.
**Bob Strecansky** 01:31 Got to spend some time with my dad, which is always good.
**Brett McBride** 01:36 Oh, that's excellent.
**Bob Strecansky** 01:37 Yeah, we went to the… we went to Oregon and did a little road trip from… Portland to wine country to the coast, and it was just… everything about the trip worked out perfectly, which never happened, so…
**Brett McBride** 01:53 That sounds great.
**Bob Strecansky** 01:54 Yeah, we had a… we had a really good time. I don't get to see my dad that much, he retired this year, so I was like, I need to take you on a retirement trip.
Sounds good.
Do I have anything exciting or important?
**Brett McBride** 02:09 Me? No, no, I've got… Oh, about a week and a half left before I, sort of, start my big leave.
**Bob Strecansky** 02:17 Oh yeah, that's right.
**Brett McBride** 02:18 I'm just… I'm really, really dialing it in at work.
**Bob Strecansky** 02:24 When you say dialing it in, is that… are you talking… is that, like, you're doing really great, or you have, like, terrible senioritis?
**Brett McBride** 02:32 Dialing it in means doing the least amount possible. Yeah.
**Bob Strecansky** 02:38 Okay, so for… for… in the United States, that means you're, like, locked in really hard, and you're doing awesome, so…
**Brett McBride** 02:44 Okay.
**Bob Strecansky** 02:45 Then no, not that.
**Brett McBride** 02:48 The exact opposite. Well, that's okay, but you're allowed to…
**Bob Strecansky** 02:53 Australia and dial it in.
**Chris Lightfoot-Wild** 02:56 Well, we have the same as Brett style it in the UK as well.
**Bob Strecansky** 03:00 Okay, so… the Americans are just the weird ones.
**Chris Lightfoot-Wild** 03:03 It's not the outreach.
**Brett McBride** 03:04 Yes.
**Bob Strecansky** 03:07 Wow, what a surprise, America is there.
**Brett McBride** 03:09 It is.
**Bob Strecansky** 03:11 That doesn't shock me at all.
**Pawel Filipczak** 03:18 Hey, guys.
**Bob Strecansky** 03:19 Hey, pal, how are you?
**Brett McBride** 03:20 Oh, well. How are you?
**Pawel Filipczak** 03:22 Thank you.
**Bob Strecansky** 03:27 I said to everybody… I said to Brett, I think, before the rest of y'all got in, my internet connection's being a little spotty, so I'm just gonna go camera off today, but I am here and present with you, so… Alright, do we expect anybody else, or should we get rid of it?
**Brett McBride** 03:47 I'm not expecting, no.
**Bob Strecansky** 03:50 Alright, let's rip them. Brett, I'm glad you put this on the agenda, because I wanted to talk about it, too. The C++ SIG reviewing and discussing our Elastic contribution. It looks like they were able to discuss it during their… last SIG meeting, but still have some open questions, so I expect that we'll have to field those in the next couple of weeks, but… It seems relatively, like, I don't know, maybe I'm just reading it the way I want to read it, but it seems like it's a relatively positive thing.
**Brett McBride** 04:20 Yeah, I think so, and I think they're… my impression is they're more looking at it as… from a lens of, You know, how can we… Reuse more of their code, and how can, sort of, any of the, sort of… what do we have that they don't? You know, what can we…
**Pawel Filipczak** 04:40 provide to each other's.
**Brett McBride** 04:42 Sort of seeks.
**Pawel Filipczak** 04:44 Yep, I wrote… I read the notes from… from these meetings, this… this document, and… Yeah.
**Bob Strecansky** 04:51 Oh, wow.
**Pawel Filipczak** 04:53 There are a few issues.
There, which, okay, and it should be solved. It's possible to solve that.
So, the main issue with the C++ library is that… It's not linked together, so if you want to use that, you have to pack a lot of shared libraries, but it's not… it's a minor problem.
**Brett McBride** 05:20 The problem with the code, which is…
**Pawel Filipczak** 05:24 duplicated in the PHP and the… in the C++ in the Elastic distro.
It's because of the startup.
Issues, and the… PHP engine, which is initialized much, much later, so we have to, for example, to get the service name.
And other resource attributes, and make use of those data in the In the… in the op-amp client, collaborative client.
we have to do that very early, so then the SDK is neutralized later, so it's too late to get the first config as quick as possible, so that's the… That's the issue here.
Maybe it will be somehow solvable, and maybe it's possible to do that.
Maybe we can expose the native function with the… With the detected attributes on the… on the native site, and then add and make some… some together what was found in the… on the PHP level.
And in the native, who knows?
I will join the C++ segarity when it is… I was trying to find the… the invitation, but something… it wasn't compatible with my calendar.
So… Do you remember when it is?
**Bob Strecansky** 07:00 the… Sit.
Looks like it's 4 to 5 p.m. They have two, they have 4 to 5 p.m. and 12 to 1 p.m.
**Pawel Filipczak** 07:19 Eastern.
**Bob Strecansky** 07:23 You know how to get to that OpenTelemetry calendar, right, Paul?
**Pawel Filipczak** 07:27 I will, I will try again. Maybe, yeah.
**Bob Strecansky** 07:32 Sounds good.
**Pawel Filipczak** 07:33 Maybe I did something wrong.
**Bob Strecansky** 07:36 Those calendars can be unbelievably annoying. Dealing with time zones, as we all know, is never fun.
**Pawel Filipczak** 07:43 Yam.
**Bob Strecansky** 07:45 Welcome, Nick, how are you?
**Nick Schuch** 07:49 Gun! Gun!
Doing really good.
**Bob Strecansky** 07:55 Nice.
**Pawel Filipczak** 08:01 So, we were feeling after the meeting with the C++6 that… They're okay, and I… it looks like they accepted the… the way that we'll merge it to the PHP, and then try to contribute it to the C++, right? I mean, that direction.
**Brett McBride** 08:19 Yeah, yeah, yeah, I think so.
Yeah, I don't have the impression, I mean, we have input, because it's our SIG, but that, you know, that, that anything is a showstopper. And I think the plan What I would like to see is that it just goes into an incubation phase, for a while, so everything doesn't have to be fixed up front. We just, you know, we're probably happy to, sort of.
Accept it as… As is, or with minor changes, and then… and then get to work on You know, improving it.
**Pawel Filipczak** 09:03 Right.
**Chris Lightfoot-Wild** 09:05 Does that mean some of that SIG has an active interest in making those improvements as well, or is it all just gonna be, yeah, it's fine, and then Powell has to do it?
Zuh.
**Brett McBride** 09:15 I think if it… in terms of, Making… OTel, C++, more useful.
2 hours, if they're sort of minor API changes, then yes. But no, they were pretty clear that they're… somewhat like our SIG, light on for contributors, so they can't just, you know, step in and fix everything for us, no.
**Pawel Filipczak** 09:42 Hmm.
**Chris Lightfoot-Wild** 09:43 True.
**Bob Strecansky** 09:45 Unsurprising, but very thankful for the help that they have given us so far.
**Brett McBride** 09:49 Yes.
**Pawel Filipczak** 09:50 Yeah.
Okay, so I'll do some planning and book some time to… to… to make some draft, what should be done, and which order, and how to solve that, yeah. Thank you.
**Bob Strecansky** 10:04 Sounds good. Let us know if we can help at all.
**Pawel Filipczak** 10:07 Thank you.
**Bob Strecansky** 10:08 Alright, let's stroll through the board. We made it past 20 million while I was out. I guess all I needed to do was leave for a vacation, and then we hit a big milestone. That's exciting. Hooray, everyone.
Alright, let's take a look at our poll, open pull requests… Update D4 temporality to spec.
**Brett McBride** 10:29 I think that's right. It's… it's got through 3 or 4 different reviews from… from Nive.
Look, I think it's okay now.
**Bob Strecansky** 10:44 I can… I can, I can take a look at it later today, thank you for doing that.
**Brett McBride** 10:49 Thank you.
**Bob Strecansky** 10:50 I think that's the only one that's open in the… PHP, repo that's recent.
Contrib… excuse me?
Looks like all of these are still…
**Brett McBride** 11:04 Yeah, so some of the… some of the sort of context propagation ones I have been, merging. There was one into core… And… wanting to contribib… So this is a… this is, like, the SQL commenter is a different, Yet another type of, of sort of forwards propagator, and, and that's what this, This pull request is kind of trying to… workout, and I think there's even another one as well, but… but how do we do it? Because it's sort of supplementary to the… Sort of standard… text map propagator, where we, you know, use for HTTP headers, so… I'm trying to keep up with it, but there's at least one other reviewer in there, Who seems to know a bit about… What's going on? Yeah, this guy, chimps.
**Bob Strecansky** 12:00 This kitty cat.
**Brett McBride** 12:02 Yeah.
**Bob Strecansky** 12:04 So, what's the, What's the… I guess I gotta read through both of these. They seem like relative… oh, it's a follow-up replacement.
**Brett McBride** 12:14 Yeah, so, so my understanding… so this comes back to the, the donation of SQL Commenter.
**Bob Strecansky** 12:21 Oh, God.
**Brett McBride** 12:22 to open telemetry, and, this guy's trying to implement that.
And so… there is… now an accepted, sort of, merge change into… into the spec, about at least the beginnings of how this should work. And one of the… yeah.
But I guess one of the… one of the key points is that The propagator that you would normally set for… Doing, sort of, regular distributed tracing and propagation, where you would inject into headers, is not necessarily The propagator that you would use for… injecting… Context propagation to a database.
And there are… at least 3 different ways, depending on which database you're using, to… to do that. Sort of there's inject some comments, and then, some databases have more mature, sort of, telemetry-like things. I think SQL Server and Oracle, in particular had, You know, actual database level.
Functions that you could use to, sort of, propagate context.
**Bob Strecansky** 13:40 Very cool.
**Brett McBride** 13:41 Anyway, yes, please do jump in, because, it's… Yeah, yeah, because the specs… The spec's new, things aren't clear.
**Bob Strecansky** 13:52 Got it.
**Brett McBride** 13:53 You know, yeah, need to work out how to… how to do things, what to name things, etc.
**Bob Strecansky** 13:58 And naming is always very difficult. So this feels kind of like… do y'all have those in your locales, the choose-your-own-adventure books?
Where, like, you would read and then pick the next place you go. It sounds like I gotta read this one and then choose whether or not I go to the next one and read that. Yeah.
**Brett McBride** 14:14 Yeah, at least now the other two… now that the, sort of, backwards propagator's done, because I was getting very confused, because this person has two completely different, but similar-looking and sounding streams of Things relating to propagation.
Context propagation, so…
**Bob Strecansky** 14:31 Got it. Okay, cool. I'll spend some time later this week.
Clacking through those.
Then instrumentation… that's just a… GitHub Action Bump, I'll merge that later.
My new stack overflow questions… Nothing crazy on the board.
- And is this the only thing left, Brett, in the road to SCK V2?
**Brett McBride** 15:03 Yeah, look, I think that it is. Yeah, which is why I was trying to knock it off.
Quickly, last week.
Yes.
**Bob Strecansky** 15:11 Cool. Well, then maybe we can finish this up and consider cutting a V2 of the SDK?
Cool beans.
**Brett McBride** 15:26 And there was one other pull request that needed review today.
But it wasn't against any of those, it's in our, in our other, other repo outside of the OpenTelemetry.
You have a…
**Bob Strecansky** 15:43 Going for it.
**Brett McBride** 15:44 Yeah, it was for the DevTools, and it's in, I do. It's, it's in the, slack channel.
**Bob Strecansky** 15:53 Okay, let me pull it up.
**Brett McBride** 15:54 new PRs.
Something for DevTools.
**Bob Strecansky** 16:00 Got it, I'm looking… I'm trying to help this one.
**Brett McBride** 16:28 Yeah.
**Bob Strecansky** 16:31 I will, I'll give that a peep later, too.
**Brett McBride** 16:34 Thank you.
**Bob Strecansky** 16:35 You're welcome.
Got a nice, a nice stack of them today. Alright, Which I guess I should expect when I abandon the group for a little bit.
Anybody else have other things that they would like to discuss today?
Alright, well then we'll wrap up a little early. Thank you all for attending, and we'll catch you on the internet.
**Chris Lightfoot-Wild** 17:01 Cheers.
**Brett McBride** 17:02 Thanks, all. Goodbye.
