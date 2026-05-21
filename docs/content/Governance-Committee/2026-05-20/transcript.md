SIG: Governance Committee
Date: 2026-05-20
Duration: 42 minutes
============================================================

## Zoom Recording Transcript

**Marylia Gutierrez** 00:29 Whoa.
**Pablo Baeyens** 00:30 Hello.
**Severin Neumann** 00:35 Hello?
**Ted Young** 00:40 Loohoo-loo!
**Trask Stalnaker** 01:22 Where's my video? There's my video.
Hello.
Why do I feel laggy?
**Ted Young** 01:34 Not enough coffee.
**Trask Stalnaker** 01:37 True.
**Ted Young** 02:33 the.
**Trask Stalnaker** 02:42 I know we eternally debate this, whether Quorum is 5 or 6, But… Probably worth.
Continuing regardless.
**Ted Young** 02:54 Yeah.
It's 5 in odd years and 6 in even years.
**Trask Stalnaker** 03:09 Wait, I think you need to flip that.
**Ted Young** 03:18 Six and odd years.
Just to make it weird.
**Trask Stalnaker** 03:22 No, well, yeah.
That, and also so that we have a quorum today.
**Ted Young** 03:29 Oh, yeah.
Fair enough.
**Trask Stalnaker** 03:34 Do we want to… we've got, I think that's just a standard time box, the 10 minutes for a stability graduation.
Do we want to chat? Ted, anything you want to…
**Marylia Gutierrez** 03:48 Actually, my question's gonna be, is graduation still a topic that we should get there? Like, yeah, stability makes sense, but graduation… Happened, so…
**Ted Young** 04:00 Right, so graduation happened, but we still have, you know, this set of work, you know, I wouldn't say I'm sad graduation happened, like, I am, but I was liking it as a stick and a carrot, you know, to get people to focus on finishing these things.
But we need to continue with that by saying we promise to do these things.
And, you know, people were having various feels about the prior doc, and it was true that it was a little bit hard to… it seemed like we were a little bit stuck trying to turn that into action items, so please have a look at this.
New doc, that's an attempt to… to take everything that was in stable by default and sort of reorganize it into things that maybe look more like work streams that we're used to.
So I believe we've captured everything. Austin, definitely have a look. Let me know if there's something important that's missing from here.
But… My goal is if we can get this thing with enough detail that we feel like we have agreement that this is the roadmap, then we would follow up Kind of with, like, a works, you know, a separate doc for each work stream.
That's managed or, you know, engaged with by the SIG that owns that work stream.
the… Trickiest bit in here, by the way, I think is… is the… the instrumentation.
everything else, I think, is a little more straightforward and attached to, like, a particular SIG, but… you know, SEMCOM tooling is gonna work on better instrumentation, tooling. We're gonna try to test run that stuff in the GenAI SIG, but… You know, I feel like there's, like, bigger issues with… Like, where do we get the people from? How do we make writing and maintaining instrumentation cool?
So, that's a little more open-ended.
And the other open-ended thing is, you know, changing around… our roadmapping. I added that.
that wasn't really in the original doc, but it was in the due diligence, and I do think it's, you know, it's something we're actively trying to do, so why not socialize it here? You know, come up with a better way of doing project management that you know, de-centers the TC and the GC and brings the maintainers in and is a little bit more of, like, a public process, because it seems like things are working better when we're doing this stuff more in public, and with the maintainer's input.
**Austin Parker** 07:00 I haven't read it yet, I saw that you tagged me on it, thank you.
I thought we had decided to call it production readiness?
**Open Telemetry Meeting 1** 07:10 I, I suppose.
**Ted Young** 07:11 That is a suggestion.
**Austin Parker** 07:13 Alright, I'm fine with… I mean, I'm fine changing it, I don't.
**Ted Young** 07:17 People are gonna complain about all the words, and like, production readiness is implied.
**Austin Parker** 07:22 Like I said, it's.
**Ted Young** 07:22 Not ready for production, but our problem is less that it isn't ready for production, more like it is ready for production, but we, like.
**Austin Parker** 07:30 I mean, I'm… I, I accept, I accept that… Calling it stable by default was causing an unnecessary amount of… Anxiety.
In certain parties, or among certain parties, so I'm fine changing the name.
**Ted Young** 07:48 We could call it Bob, but that was the reason I changed it, was just a.
**Austin Parker** 07:51 No, let's call it Bob, OpenTelemetry Bob, like Microsoft Bob.
**Ted Young** 07:57 Yeah.
**Open Telemetry Meeting 1** 07:57 are clipping.
I…
**Ted Young** 08:00 I was saying GA or Generally Available, because that's actually the term we used to use when we naively thought this was just around the corner.
**Austin Parker** 08:09 Yeah.
I mean, I think the only, like.
thing I would push back a little bit is that GA and graduate, like, graduating and then saying, okay, now we're going GA is maybe a little…
**Ted Young** 08:23 I can change the… change the words, I don't…
**Austin Parker** 08:26 No, it's… that's… I will look through it and, like, put feedback in, this week.
**Ted Young** 08:34 Yeah.
**Austin Parker** 08:36 Thank you for… I… I want to say thank you for, like, Running with it.
**Ted Young** 08:42 You're welcome.
I feel like the community is gonna like… we've been socializing this in the specsig for weeks and getting feedback, so I think this is a good way to lay it all out, that the community will like better, because… They seem to like it.
In those meetings, but yeah. Anyways, take a look.
**Trask Stalnaker** 09:02 I totally agree, the most contentious part is the naming.
**Austin Parker** 09:09 It's no way.
**Ted Young** 09:10 No, no issues.
**Trask Stalnaker** 09:11 Yeah, I also don't…
**Austin Parker** 09:12 It really is winning.
**Trask Stalnaker** 09:13 I also don't like GA, but I have zero better proposals for you.
**Ted Young** 09:18 I'm happy to change it if someone.
**Trask Stalnaker** 09:21 I know, I know, it's just a…
**Austin Parker** 09:23 Look, this… there is so many coats of paint on this bike shed.
**Marylia Gutierrez** 09:28 Let's call it good to go.
**Open Telemetry Meeting 1** 09:30 GA, GA, sorry.
**Austin Parker** 09:31 Good to go.
**Open Telemetry Meeting 1** 09:33 Let's go with it.
**Austin Parker** 09:33 called G2G.
**Ted Young** 09:34 Go.
Alright, anyways, that's… that's all I got on that. What else we got?
**Austin Parker** 09:45 Did we want to… chat real quick.
I… just wanted to close the loop, because I did post about it, in the thread, but we did reorder the quotes.
But we moved the AWS quote out into end user.
**Open Telemetry Meeting 1** 10:11 Nice. Austin, I'm trying to get a code signed off also.
**Austin Parker** 10:15 Done. It's too late.
**Open Telemetry Meeting 1** 10:17 No worries, no worries, you can use.
**Austin Parker** 10:19 Yeah, the cut was technically, like, yesterday at.
**Open Telemetry Meeting 1** 10:22 Yeah, yeah, yeah, I know.
**Austin Parker** 10:25 It is… it is locked and loaded, so, And I think they've been doing… I think Chris… Chris A. did some analyst briefings and some stuff yesterday, I… well, apparently none of us went to Minneapolis.
Given that we are all here, and I'm in San Francisco, so.
**Open Telemetry Meeting 1** 10:51 What? You come and see me? No.
**Austin Parker** 10:55 Look, you wanna take the Waymo up? I'm very busy.
**Ted Young** 11:02 Yeah, I didn't want to troll Chris, but I was… I was thinking, it's like, you know, of all the years to cancel OpenTelemetry Community Day.
**Open Telemetry Meeting 1** 11:11 theory.
**Austin Parker** 11:11 Yeah.
**Open Telemetry Meeting 1** 11:12 And, we'll.
**Austin Parker** 11:12 Anyway, either way… Open Telemetry Meeting 1 11:14 Had the gift card.
**Austin Parker** 11:14 Either way.
Great, it's done, I'm happy, everyone's happy. Are we all happy? Everyone feeling happy?
**Open Telemetry Meeting 1** 11:26 Yes.
**Morgan McLean** 11:27 And great work getting that through, Austin, seriously.
**Open Telemetry Meeting 1** 11:29 You know, seriously, good work.
**Ted Young** 11:31 Yes, thank you so much.
**Austin Parker** 11:34 We are.
**Ted Young** 11:35 Chris, by the way.
**Austin Parker** 11:36 You're throwing a party.
**Ted Young** 11:37 Excited.
**Open Telemetry Meeting 1** 11:37 Yes, cool.
**Ted Young** 11:40 They are excited about trying to think outside the box of, like, you know, other than get up on stage at KubeCon in A, like, like, what are other things we can do? They're willing to put some time and effort into, like, celebrating harder for… because of that.
**Austin Parker** 11:58 Yeah.
**Ted Young** 11:58 big project, but Chris, I didn't have any great ideas other than, like, I don't know, swag or something, but… but it's… we've got a bit of time before KubeCon in A, and then, of course, KubeCon EU, we've got plenty of time, but…
**Austin Parker** 12:13 Yeah, I mean, we can get a full year of celebrations out of this.
**Ted Young** 12:17 Yeah.
They're willing… they're willing to make some programmatic changes, or, you know, they're willing to put some effort into doing this, if we can come up with… Like, interesting ideas for… for.
**Austin Parker** 12:29 Yeah.
**Ted Young** 12:30 better.
**Austin Parker** 12:31 Yep. And it's press release official. We are now… we are the de facto observability standard, so… good job, everyone.
**Open Telemetry Meeting 1** 12:39 Good job.
**Ted Young** 12:40 OpenTelemetry, de facto is our middle name.
**Open Telemetry Meeting 1** 12:44 Defecto. It is, it is.
**Ted Young** 12:48 50 facts are the same.
**Pablo Baeyens** 12:49 Total.
**Ted Young** 12:50 Standard.
**Austin Parker** 12:51 The press release goes out on the 21st at 9am Central.
**Pablo Baeyens** 12:57 But is that, like, there's an analyst room or something on…
**Austin Parker** 13:02 Right, there's, like, there's Preston analysts there. Yeah.
**Open Telemetry Meeting 1** 13:05 Please, we have a room.
**Austin Parker** 13:06 I think Reese… Reese… lies in, like, today or something, and I think I'm trying to… we're trying to get Reese in front of some people as a, like, community manager.
So there's… Not just Chris.
And if anyone is in San Francisco, we're gonna do… we're throwing a… we're gonna have Kate.
Tomorrow?
And cupcake?
**Open Telemetry Meeting 1** 13:33 Send me a link.
Possibly.
**Austin Parker** 13:36 You should have gotten several, but… Open Telemetry Meeting 1 13:38 I didn't… I didn't get anything, what?
**Austin Parker** 13:41 Why? Oh, it's because you probably don't use honeycomb.
I'll DM you.
**But… Open Telemetry Meeting 1** 13:49 Okay.
**Austin Parker** 13:50 I'll have to… I'll share pictures of the cake.
**Trask Stalnaker** 13:53 Okay, foot.
**Austin Parker** 13:53 Correction, there will be… there will be cake if I can find a bakery that will turn the cake around in 24 hours, because the bakery that we tried to do, took our money and then, stopped calling us back, so… Open Telemetry Meeting 1 14:05 You didn't use Tartan?
**Austin Parker** 14:07 No.
**Open Telemetry Meeting 1** 14:08 Oh, forgets.
**Austin Parker** 14:10 our office manager found someone else. I will… I'm probably gonna do Novalley.
Anyway.
**Open Telemetry Meeting 1** 14:15 And lots of good places.
**Austin Parker** 14:19 We got… we have, cupcakes, though. The cupcakes came through. They're a blue… it's a blueberry one, and a yellow lemon one.
Pretty good.
**Open Telemetry Meeting 1** 14:29 Do share.
Pictures.
**Marylia Gutierrez** 14:34 Oh, I don't want to share pictures, I want to share cupcakes, just like this.
**Austin Parker** 14:38 I don't know those pictures.
Freeze dry, yeah, we'll try freeze drying, I think… Other than that, okay, that's… and that was the last graduation update.
**Open Telemetry Meeting 1** 14:54 Cool.
**Austin Parker** 14:54 stunned.
What else we got?
**Ted Young** 15:05 Just to jump… just because it's related to graduation, Severin…
**Severin Neumann** 15:12 Yeah, I was thinking that as well, so maybe we can quickly… I think we talked about this in… only in comms so far. I wanted to share this with everyone. Like, when this press release comes out from the CNCF, we wanted to have social media posts.
And also at least a small blog post that's pointing to it, and at the same time more saying something like, hey, thank you everyone for being part of this journey.
And read more over there, so we will not write another lengthy thing.
I think mainly Tiffany already took care of that, so if you can take a look into the draft.
That would be helpful, and then we can send it out the moment the press release is available.
**Marylia Gutierrez** 15:55 Yeah, so she's gonna open the PR today, in case there is any feedback, and have it ready to publish tomorrow, right after the official one.
**Open Telemetry Meeting 1** 16:06 Yeah, looks good. 7.
**Severin Neumann** 16:08 Only thing, I just… the GitHub, banner, should we also do one there?
CNCF, like, on… like, we do it for KubeCon and something like that, because there's a lot of people that interact with our project only through GitHub, and maybe not visiting the website from time to time.
So, I don't know.
If this is, like… Just for a week or something, say, like, hey, we graduated, here's this thing.
**Austin Parker** 16:36 You know?
**Ted Young** 16:37 Yeah.
I…
**Severin Neumann** 16:39 Okay.
I think I had handled it.
**Austin Parker** 16:44 Okay, I did leave, like, Two comments on this? Like, I don't think from is the right word?
Because it implies we're, like, leaving somehow?
**Severin Neumann** 16:55 Yeah, I see it, yeah. Within? Is that the right word?
**Austin Parker** 17:00 I… I would maybe look at how other projects have described it.
**Severin Neumann** 17:06 Yep.
**Austin Parker** 17:07 Maybe they use FROM, I don't know, but… It reads like you're graduating from, like.
**Open Telemetry Meeting 1** 17:12 I know.
**Austin Parker** 17:13 Like, you're graduating from college, so you're leaving college, and it's like, no, we're not leaving the same thing.
**Open Telemetry Meeting 1** 17:18 Yeah, it could be at… at… Within.
**Austin Parker** 17:22 then, yeah, I don't know, I'm just… That was the one thing that jumped out.
**Severin Neumann** 17:26 Fallout, yeah, yeah, yeah.
**Ted Young** 17:30 one.
**Pablo Baeyens** 17:30 One more thing that maybe would be good to fix. This page from the CNCF still shows Gitter, I did the PR on CNCF Landscape.
**Open Telemetry Meeting 1** 17:42 Did they merge it?
**Pablo Baeyens** 17:42 ordinance.
**Open Telemetry Meeting 1** 17:43 Huh?
**Pablo Baeyens** 17:44 Yes.
Yeah, it was merged yesterday.
But this is still wrong.
**Ted Young** 17:50 So maybe this is, like, a different… Different web page or something?
**Austin Parker** 17:55 I don't know where this comes from.
**Open Telemetry Meeting 1** 18:00 Be told.
Like, the links come from somewhere else.
**Severin Neumann** 18:03 Maybe it takes a little bit until they, like.
Update that, maybe it's not live.
**Open Telemetry Meeting 1** 18:11 Could be.
**Austin Parker** 18:13 I don't know what populates… this.
**Pablo Baeyens** 18:16 Oh, well, the… the guy said within a day or two. No, it is populated by the landscape thing, it seems.
**Austin Parker** 18:22 Oh, well… Did we remove Gitter from the landscape? YAML?
**Pablo Baeyens** 18:28 Yes.
**Open Telemetry Meeting 1** 18:29 Yeah, I… Yeah.
**Pablo Baeyens** 18:30 I made this PR that was merged yesterday, but maybe a day or two has not yet passed.
**Open Telemetry Meeting 1** 18:37 Yeah, probably.
Maybe somebody has to do it manually, Pablo, when they push.
I changed…
**Austin Parker** 18:47 or anything, do you mean?
Override the… maybe… I mean, my assumption would be that it doesn't actually work like Chris thought it works, or that… I don't… -No.
Like, maybe those have to be there? I would… if it's still there tomorrow, I would, like, open a follow-up issue.
**Pablo Baeyens** 19:14 Okay, yeah, would be great if… We didn't, like, send people together when the… press release comes out, but I guess it's… if it's still out there tomorrow, that it's too late.
**Ted Young** 19:35 I just got a.
**Pablo Baeyens** 19:36 I'll try and fix it tomorrow morning… tomorrow evening. Let's see… Here we go.
**Austin Parker** 19:42 What's…
**Ted Young** 19:45 Real quick, I got a ping from the CNCF asking if anyone's gonna be at KubeCon India.
I assume no.
**Open Telemetry Meeting 1** 19:54 No.
**Morgan McLean** 19:55 I think one of my staff will be there, but not me.
**Ted Young** 19:58 Okay.
**Open Telemetry Meeting 1** 19:59 Yeah, Morgan, you have a big team there, right?
**Morgan McLean** 20:02 Splunk does, but not me personally, but I just have someone who'll happen to be traveling there at the same time.
Yeah.
**Ted Young** 20:13 I'll be at KubeCon Japan. I don't know if.
**Open Telemetry Meeting 1** 20:17 I'll be there, too. I have a talk. Yeah.
**Ted Young** 20:22 Cold.
In terms of this, press release, do we want to go into any detail about the GA road ahead at all, or is that… Not the right.
vehicle.
For promoting that.
**Austin Parker** 20:54 I mean, I think if we had, like, specific things we could sort of drive people towards… Like, if we had…
**Pablo Baeyens** 21:05 I wouldn't mention the GA thing specifically, but… I don't know, we can say that we're working on Profiling, or entities, going… Open Telemetry Meeting 1 21:16 or semantic conventions for Gen AI.
**Austin Parker** 21:19 Yeah, like, my thought was, like, do we have specific projects to kind of funnel people towards, and be like, hey, this is a great time to get involved, like… Open Telemetry Meeting 1 21:26 Yeah.
**Austin Parker** 21:26 Just because we're… Just because we graduated doesn't mean we've stopped, like, go here.
**Ted Young** 21:33 Okay.
maybe that's a to-do, you know, after this call. Everyone have a look at that section and think about what What… what we could promote.
What can we safely promote about the OpenTelemetry roadmap?
**Open Telemetry Meeting 1** 21:50 Gen AI instrumentation and semantic conventions, as Pablo said, profiling, stability.
**Morgan McLean** 22:01 Those are the big 3 that I would… that I would recommend.
**Ted Young** 22:05 Cool.
Marillia?
You wanna…
**Marylia Gutierrez** 22:23 Leaders?
**Ted Young** 22:23 through your section?
**Marylia Gutierrez** 22:25 Yeah, so yeah, thanks for all the ones that already put it their… their info there, and the ones that noted that they were missing, you know, already created stuff, so yeah, thank you for that. But yeah, I think Austin, Morgan, and I guess Alolita, for your others, are still missing, because I saw you put the to-do there.
**Open Telemetry Meeting 1** 22:44 Yes, yes, I'll add them in, Marilla.
Because, I don't have a formal channel, but I'll create that.
**Marylia Gutierrez** 22:53 Yeah, just because we were doing all those things, like, making sure we are listening to maintainers.
**Open Telemetry Meeting 1** 22:58 Yeah.
**Marylia Gutierrez** 22:59 But the.
**Open Telemetry Meeting 1** 22:59 Totally.
**Marylia Gutierrez** 22:59 that I'm getting is that… None of them were getting listened to, so… make sure they are actually doing that. And then I noticed there are a few that I think.
both Trask and Ted Market a few that are no longer active, so is the plan… is already, like, definitive non-active, so we just should remove them from that list?
**Trask Stalnaker** 23:22 I'll send a PR to remove the… secure… the SEMCON security from the list.
**Marylia Gutierrez** 23:30 And for both of yours?
**Trask Stalnaker** 23:32 That one's been dead for a long time.
**Marylia Gutierrez** 23:34 Okay.
**Ted Young** 23:36 I'll… I'll… yeah, I'll be making PRs for mine. The… the client SIG is… is, like, not rea… it's still like a… it's like a touchpoint for the different… SIGs, but now that we have Browser and Swift and, you know, Kotlin, Android. It's more just, like, we're keeping the meeting around to occasionally sync up with each other, but it isn't, like, a SIG that's got maintainers working on things, so we'll keep it on the calendar.
But there's no… no one to check in with there.
**Marylia Gutierrez** 24:08 Okay.
And I think also the one for, I guess this one is for Austin, the project infrastructure, because there was also still, like.
a PR open for the emeritus, and the comments, like, should we revive this SIG? So, I don't know how active is that SIG? So, probably another one for you to take a look.
**Austin Parker** 24:29 Yeah, true.
**Trask Stalnaker** 24:30 I had proposed archiving the repo.
**Austin Parker** 24:35 Yeah.
**Trask Stalnaker** 24:35 Channel a couple of months ago, because…
**Austin Parker** 24:38 We've… we've all rolled off of it, pretty much. It's… which… Yeah.
I think there's… Oh.
Yeah, we should just archive it.
**Marylia Gutierrez** 25:01 Well, since you are… Liz, do you mind taking… corn…
**Trask Stalnaker** 25:05 Yeah, Austin, I'll start a… chat, maybe, with us and, Adriel and…
**Austin Parker** 25:12 Gabriel, yeah, and Jacob, yeah.
**Trask Stalnaker** 25:15 Just to see, like, if there's…
**Austin Parker** 25:19 I don't… I don't know if… Jacob Roydrill is doing that much anymore with it?
**Open Telemetry Meeting 1** 25:23 Yeah, Jacob's working on other stuff.
**Trask Stalnaker** 25:27 Yeah, I know that nobody's working on it, because the repos… Yeah, if you look at the repos…
**Austin Parker** 25:33 Sure.
**Trask Stalnaker** 25:34 The question is whether they have anything… if they have a strong desire to revive it, and if they have things that they want to drive in that SIG.
Just as a, you know, courtesy to them, because they have been active in the past there.
**Austin Parker** 25:54 Damn.
**Marylia Gutierrez** 25:55 Yeah, so the last message that is on the Emeritus PR is from Adriel, saying, we should probably figure out if we want to do this, or just reinvigorate the SIG. We are kind of… kind of have let the SIG sit static for a while, as other things have been going on, so that is his latest message.
Yeah, so I guess just for the ones missing.
Let's make sure that you're adding… that is also helpful whenever, like, if… liaison, like, changes between people. We know there is already a channel that we can add people and stuff like that.
**Open Telemetry Meeting 1** 26:40 Yeah, certainly.
**Marylia Gutierrez** 26:42 And the other topic that I have, unless anyone has any questions about this one?
is that I was just looking, like, the… basically security-related stuff, and I was planning to add, like, this more to a few of the ripples that I'm working on, and I was like, well, assuming, like, CodeQL is already enabled for the majority, but then I check on, like, the admin, and… Seems like only a few repos, actually, is enabled, so I don't know if I'm missing a place that it says, like, all of them should be, but I searched the… just by the term, and show, like, require code scanning in just about 3, 4, 5, like, 8 of them?
**majority pretty much Java ones. So, yeah, just any objections? Otherwise, I can just copy that requirement to all the… Open Telemetry Meeting 1** 27:37 Yeah, enable it, really. It's definitely a good idea.
Because, it was… actually, we did do a pass of full coverage But that was, like… At least 2 years ago.
Two, two, three years ago.
**Trask Stalnaker** 27:50 I think this…
**Pablo Baeyens** 27:50 Do you have the list there.
Proposition.
**Trask Stalnaker** 27:53 Yeah, most repos have CodeQL, running, but, they don't have it as a required status check.
**Open Telemetry Meeting 1** 28:02 connecting.
**Trask Stalnaker** 28:03 Marillia, I think that's what you're seeing.
**Marylia Gutierrez** 28:05 Okay.
**Trask Stalnaker** 28:06 the admin repo is… the Java repos, I've added that as a required status check.
Basically, meaning we can't merge a PR.
If it's not… green.
**Marylia Gutierrez** 28:18 Mmm, okay.
**Trask Stalnaker** 28:20 So, I do think it's a good thing, but I would… B… Cautious rolling it out en masse, and maybe, Maybe just posting in Hotel Maintainer's channel?
And… Recommending that maintainers do that as a first step.
**Marylia Gutierrez** 28:46 Yeah, yeah, I can do that.
**Trask Stalnaker** 28:49 Awesome.
**Pablo Baeyens** 28:50 I believe on the collector records, for example, the CodeQL check is very long, so maybe… People won't be super happy, even if everything works perfectly, people won't be super happy about, you know, having to wait a lot.
**Trask Stalnaker** 29:07 So, Pablo, what… we had a similar problem in the Java instrumentation repo, and, I switched it to use one of the, CNCF Oracle runners that has a lot more, Coors.
And that makes it run a lot faster.
**Pablo Baeyens** 29:30 Okay, yep, maybe… maybe we can take a look into that.
**Trask Stalnaker** 29:34 Yeah, I can follow up on Marillia's message to point people to that, if that's a concern.
**Marylia Gutierrez** 29:45 Thanks.
Yeah, that was all for my topics.
Austin, you're next.
**Austin Parker** 29:59 Yeah, I just wanted to update on the, Claude for AI thing.
So, I've still heard nothing back from either OpenAI or Antopik, I don't fucking know.
I'm pivoting, or… well, first what I'm doing is I'm pivoting.
**Pablo Baeyens** 30:18 Is this the thing where they were going to give us access for, like, security things?
**Austin Parker** 30:23 Yeah, like, security… just… API credits, da-da-da-da-da. So… I am… So here's the thing that's annoying, is, like, I went and, like, I haven't heard them.
I went and asked… Jeffrey Sika.
at CNCF about it, and Jiffy said.
When they talked to the program managers over there, they were like, Well, They don't want to do… basically, they said, maintainers should just go apply themselves individually.
So… I think what we need to do, is, like, I think we just need to put something… like, I just think we need to promote this internally better. We need, to say.
Hey, maintainers… If you individually are a maintainer of a repo, an hotel repo, then you should go apply for this.
**Pablo Baeyens** 31:44 Do maintainers get API credits? I mean.
**Austin Parker** 31:47 Yes.
**Pablo Baeyens** 31:49 Okay.
**Austin Parker** 31:50 Well, the API credits in the U.S.
**Pablo Baeyens** 31:51 theme, project-wise.
**Austin Parker** 31:53 They also get code… I mean, they also get, like, Claude Security, Claude… I mean, both of the programs are similar.
Codex is… 6 months of ChatGPT Pro, which includes codecs, conditional access to codec security, and API credits.
Claude for open source is 6 months of Claude Max X20.
But no API credits, I guess.
But apparently… They are unlikely, at least for now, to do sort of a site license.
And I think CNCF is also kind of… they don't seem thrilled with how the co-pilot thing worked out for them, so I don't know.
But… Yeah, I think what we need to do is we just need to flip around and say, like, hey, maintainers, you… if you are a maintainer of one of these repos, then you should go apply for this.
**Pablo Baeyens** 32:52 And what is the benefit of these programs when compared to the Copilot access that we have? Do we have access to other models, or…
**Austin Parker** 33:01 I mean… certainly with the API credit stuff, it's… the two big things is, this gives you… This will… The biggest advantage to the… to this is that Copilot, as far as I'm aware, doesn't have any, like, security-focused Cool, like, doesn't have, like, the security harness stuff.
And both of these do. So, this gives you, sort of, the automated security if you read all, you know, if you've read the stuff about, like, Project Mythos, and, like, Glasswing, and sort of the… you know, Find vulnerabilities stuff, like, that is what you can get through this.
But it's at, like… but it has to be at an individual.
Cloud security isn't mythos, but it's…
**Pablo Baeyens** 33:55 No, I mean, and I don't think it is available through that program, because, I mean.
**Austin Parker** 33:58 That would…
**Pablo Baeyens** 33:59 the…
**Austin Parker** 34:00 Cloud security isn't.
**Pablo Baeyens** 34:01 build enterprise.
**Austin Parker** 34:03 Okay, so, right, cloud security is a different thing, but you can still, like, individual… the short version is.
OpenAI Anthropic do not appear to be interested in working with us as a… Organization?
They appear to be interested in working with maintainers individually.
I don't know why.
I would assume something to do with… just the way they've got things set up, but I think we need to change our strategy here. Instead of saying, like, hey, let's keep waiting for them to approve something, I think we just need to say, hey, Maintainers share these programs, You should go apply for them.
Ted.
**Ted Young** 34:49 So, you know, we've been talking about OpenAI and Anthropic, but, like, the two organizations that are invested in OpenTelemetry that also do this are Microsoft and Google, right?
like… To what degree should we maybe be just focusing more on tools provided by those organizations, since, you know, we literally have reps from those organizations, you know, heavily involved in the project, and those organizations are heavily involved in OpenTelemetry?
**Austin Parker** 35:22 Right?
I don't think Google has a… I don't think Google has, like, an anti-gravity or Gemini for open source thing.
Anyone know?
**Morgan McLean** 35:37 Not that I'm aware of.
**Open Telemetry Meeting 1** 35:38 I haven't seen anything explicitly called out.
**Ted Young** 35:41 Mean.
**Austin Parker** 35:42 Yeah.
**Morgan McLean** 35:43 I mean, but to Ted's point, you could always ask.
**Open Telemetry Meeting 1** 35:45 Yeah. Right there.
**Morgan McLean** 35:46 But I don't know if.
**Austin Parker** 35:47 Surely, I'm sure.
**Ted Young** 35:48 I imagine a bunch of stuff is about to get launched. At any rate, I'm not talking about, like, short-term right now, I'm just… Open Telemetry Meeting 1 35:55 Sing is a lot.
**Ted Young** 35:56 long-term strategy.
The… the… you know, whether or not, like, the… Current best, absolute best of whatever class of thing is, like, coming out.
Like, those organizations, those are the ones… those are the organizations we can partner with, right?
**Austin Parker** 36:13 Sure. I think my point more broadly is… The problem, like, yes, we should pursue that, but the problem exists today of, like, hey, like, we need to make sure our maintainers have access to these tools.
And if the most expedient way for them to get access to them is to just apply individually, then that's what we should tell them to do, rather than saying, hey, keep… wait for us to do something for you.
**Ted Young** 36:38 Yeah.
**Trask Stalnaker** 36:40 So, a lot of the maintainers, recently there was discussion, and they've been just using the regular, tools to search for security bugs in their repos, not these, you know, special security harnesses for… from Anthropic and OpenAI.
And they've been having a lot of success just with that, and there have been a flurry of, kind of fixes in repos.
**Austin Parker** 37:12 Yeah.
**Trask Stalnaker** 37:13 So, I mean, I think that's… A very, you know, I… Wish it.
Push that, at least.
But I would love to see, to Austin's point, I mean, none of us have, at least that I'm aware of, have tried one of these specialized security harnesses.
I would love to see one of the, you know, one of the repos have access to that, one of the bigger repos to have access to that, just so we can compare and see if it's finding things that regular, you know,
**Austin Parker** 37:49 Yeah.
**Trask Stalnaker** 37:49 Tooling.
**Austin Parker** 37:51 the regular tooling isn't… yeah, and I think the…
**Trask Stalnaker** 37:54 fueling is great at finding this stuff. I mean, like, just as an anecdote, a couple months ago, Datadog reached out to us in the Java Instrumentation repo that there was a 9-plus CVE, in, and… while… But they didn't tell us what it was yet. I mean, they were going to, just… they were setting up… Pablo was setting up the right back channels to provide the details, and in the meantime, I just asked Copilot, I told it in our repo, hey, there's a… C9 plus CVE in our repo, find it. That was… and it did find the exact one that then Datadog reported.
**Austin Parker** 38:38 Nice.
Yeah, I think, I mean, my… again, my overriding point here is… I think there is value in… I think there's definitely value in, like.
us getting access to these, I just think that, at this point, like… It's not helping anyone to kind of just, like, ping back and forth and try to do this at the org level.
I think we just need to tell maintainers, like, hey.
if you are a maintainer, if you are listed as a maintainer, if it is provable through GitHub, like, through automation that you are a maintainer, and you are actively contributing to this repo, then… go apply for this, and it should be handled pretty quickly. Like, I think the… As… my understanding is that the tooling they have set up is basically oriented towards the idea of, like, an individual maintainer is applying.
and not…
**Trask Stalnaker** 39:38 An organization.
**Austin Parker** 39:39 is applying to… yeah, so if you are a maintainer of, like, job instrumentation, or a collector, right, then… you know, go fill out the forms, right? Like, and see if it turns around really quickly. But we should just go tell maintainers, hey, do this. I have the links, I'll put them in.
**Trask Stalnaker** 40:00 Cool.
**Austin Parker** 40:00 I'll put them in the…
**Trask Stalnaker** 40:02 can guinea pig the Java instrumentation repo, and see if they… see if we get replies.
**Austin Parker** 40:10 Yep.
I would probably… I think the OpenAI one has a… Yeah, with OpenAI, you can specifically request access to codex security, so that might be what I would start with.
Because I think the cloud security is, like, a separate application that you have to do.
But yeah, we should definitely just, like, if you want to try it out, and, like, Pablo, maybe you could do it for Collector.
**Pablo Baeyens** 40:42 Yeah, I can request the Codex one, I'll see… Yeah, let me write it down. I think I looked at it at some point, and it asked if you were, like, a core maintainer or a main… some sort of distinction that didn't make sense to me, and I just forgot about it.
**Austin Parker** 40:59 Primary or core?
I just…
**Pablo Baeyens** 41:01 I don't know what that is.
**Austin Parker** 41:03 I also don't know what that one is.
**Pablo Baeyens** 41:08 If you can send me the link, I'll fill in the form.
**Austin Parker** 41:10 It's… it's in the… I put them in the meeting notes.
**Pablo Baeyens** 41:14 Oh, okay.
**Austin Parker** 41:16 But, yeah.
Let's do that!
And then if that works… and if it works for you two really pretty well, then I think we'll just… we'll just, like, go tell maintainers and announce it at spec, and be like, hey… Primarily core, yeah.
But that's all I got on that.
**Pablo Baeyens** 41:40 I put a message on the GC channel about something that maybe we should talk about? I don't know if you're private, or… Or we could do it in public.
**Austin Parker** 41:56 We could talk about that privately.
**Pablo Baeyens** 42:03 Okay.
**Austin Parker** 42:05 interrupt, and I'll start another call.
**Pablo Baeyens** 42:08 Yep.
**Austin Parker** 42:10 Right.
