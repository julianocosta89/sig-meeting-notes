SIG: PHP SIG
Date: 2026-06-17
Duration: 10 minutes
============================================================

## Zoom Recording Transcript

**Chris Lightfoot-Wild** 00:56 Soon? I'm on.
**Bob Strecansky** 00:59 Hello, how are you?
**Chris Lightfoot-Wild** 01:01 Well, dear, thanks for you.
**Bob Strecansky** 01:03 Pretty good.
**Chris Lightfoot-Wild** 01:05 Just turn anybody a little bit, sorry.
I'm gonna go to a week.
**Bob Strecansky** 01:14 Not too shabby. Yours?
**Chris Lightfoot-Wild** 01:17 Similar.
**Bob Strecansky** 01:19 That's good.
**Chris Lightfoot-Wild** 01:20 Been, warming up slightly again here.
**Bob Strecansky** 01:23 It's warm for you.
**Chris Lightfoot-Wild** 01:25 Oh, good question, what was that? What is, what was that? 17 Celsius.
**Bob Strecansky** 01:31 Oh, okay, that's pretty comfortable.
**Chris Lightfoot-Wild** 01:33 Yeah.
It's not too bad.
**Bob Strecansky** 01:36 Like, in the afternoon, it's like 38 here now.
**Chris Lightfoot-Wild** 01:39 Oh, no, that's very hot.
**Bob Strecansky** 01:41 It is very hot.
**Chris Lightfoot-Wild** 01:43 Yeah, it was kind of cold the other week. We had, you know, loads of rain, and… Boom.
I wish summer's almost over, kind of thing. Even though it's not begun yet, but… Getting a bit warmer, maybe.
Of a second spell.
**Bob Strecansky** 01:56 Maybe so.
Wonder if it's just gonna be you and me again today.
**Chris Lightfoot-Wild** 02:22 Well, it's kinda looking away.
Yeah, I'm…
**Bob Strecansky** 02:26 I wonder if the Europeans have… Like, their summer break.
**Chris Lightfoot-Wild** 02:34 Yeah, I mean, I guess I can't speak for the rest of Europe, but at least in England, the school holidays… That's sort of mid-July.
**Bob Strecansky** 02:43 I see.
**Chris Lightfoot-Wild** 02:44 Until end of August. So usually then, I guess, is where people are more likely to Take family holders.
**Bob Strecansky** 02:51 That seems reasonable. We… our summer breaks are… from… like, what, 2… yeah, 2… it started 2 weeks ago, so… the beginning of June to early August.
**Chris Lightfoot-Wild** 03:08 Oh my god.
**Bob Strecansky** 03:08 My daughter is in all sorts of different summer camps.
Summer.
She's currently at K-Pop Demon Hunters Camp.
**Chris Lightfoot-Wild** 03:18 Wow.
Is that an overnight one, then? If it's a commoner, you just send them away for a.
**Bob Strecansky** 03:23 Oh, no, these are day camps. They… they don't start going… they might go to overnight camp in, like… she might go there next year, but she's sick, so she's still a little too little for overnight camp, I think.
**Chris Lightfoot-Wild** 03:35 Yeah.
Nice.
**Bob Strecansky** 03:38 I see a pal's desk, but I don't see pal.
**Pawel Filipczak** 03:40 Hey, guys.
**Chris Lightfoot-Wild** 03:41 -Oh.
**Bob Strecansky** 03:44 There he is.
**Pawel Filipczak** 03:45 Yeah.
How's it going? How are you going?
**Bob Strecansky** 03:53 Hanging in there.
Alright, let's get rockin'. I don't expect anybody else.
Does anybody have anything they wanted to bring up?
With the agenda before we walk the boards and stuff?
**Pawel Filipczak** 04:18 So I'm working on the… on the metrics, self-metrics for the SDK. Log metrics, span metrics, and… and metrics for metrics. So I'm removing the… The hard-coded strings with the semantic conventions, constants.
I will create PR some today, maybe tomorrow.
**Chris Lightfoot-Wild** 04:49 No, it's not in the distro, just in the… the SDK.
**Pawel Filipczak** 04:54 In SDK. In SDK, then I will add metrics to the distro, enable them. So I have some initialization order issues in the distro, so I tested that locally, now I fixed that, now it works, and… it, but anyway, it will be arrived in the SDK, I mean, the changes.
**Chris Lightfoot-Wild** 05:14 Nice.
**Bob Strecansky** 05:16 Is that… I'm trying to figure that out, but maybe today… sometimes maybe, sometimes maybe… is that, like, a Europeanism? Because I've noticed that, like, cadence of talk. Has that come from somewhere? There's that famous soccer coach that says, sometimes maybe good, sometimes maybe shit.
**Pawel Filipczak** 05:32 Maybe because it's translation in my head from Polish, so…
**Bob Strecansky** 05:38 Yeah, I'm wondering, I'm wondering. But that's… when you said maybe today, maybe tomorrow, I was like, maybe this is something that.
**Pawel Filipczak** 05:44 Oh, no.
**Bob Strecansky** 05:45 But I don't.
**Pawel Filipczak** 05:46 You know, I don't want to make a hard statement that, yeah, we finished tomorrow or today, so we will see.
Understood.
**Bob Strecansky** 05:54 Very much understood. I always say, I will get that work done soon.
**Pawel Filipczak** 05:59 Yeah.
Okay. Cool.
**Bob Strecansky** 06:02 Alright.
Chris, is there anything you wanted to bring up today?
**Chris Lightfoot-Wild** 06:09 No, I don't think so.
**Bob Strecansky** 06:11 Okay, sounds good. Kyle, let… just make sure… I mean, we'll get tagged in those poll requests when… You opened them, so we'll review them for you.
**Pawel Filipczak** 06:20 Thank you.
**Bob Strecansky** 06:22 Transportation… aren't… Looks like there's a couple new ones… Renovate, renovate, renovate, renovate, renovate, renovate. Yep, I think that's it. Sergey's still working on the tree state.
Chris, you approve this one?
**Chris Lightfoot-Wild** 06:49 I have, but I think that's one… is it… not past the pipeline yet, so I was… I've got a few like this, so I probably… I probably need to pull them down and just, like, run the tests and things, because the… if they fail at fan or any static analysis, they don't get as far as hitting tests.
**Bob Strecansky** 07:08 This one passed… this one looks like it passed all the checks.
**Chris Lightfoot-Wild** 07:12 Is that in… oh, sorry, is this in the PHP? Yeah.
merge in that… sorry, yeah, I can't merge in that repo, sorry. So I did… Read the, maintenance group to it, if that was alright.
**Bob Strecansky** 07:28 I did. I can merge it, and I did.
**Chris Lightfoot-Wild** 07:31 Sweet.
**Bob Strecansky** 07:31 And then, Google Protobuff 5. This is the same thing, probably, yeah. Alright, I'll merge this bad boy.
**Chris Lightfoot-Wild** 07:38 Have you got, sort of a release plan for some of these? I'm not sure if…
**Bob Strecansky** 07:42 We… we don't have one planned currently, but we probably need to do one sooner rather than later, because we haven't done one in, what, a couple months.
Yeah.
That's not where… that's not the right thing. Where is it? It's… there it is.
Our last release was… March, so yeah, we probably need to do another one.
**Chris Lightfoot-Wild** 08:08 I mean, maybe if Powell's metrics thing's coming in, that can be the next…
**Bob Strecansky** 08:12 Yeah, we can…
**Chris Lightfoot-Wild** 08:13 At least.
**Bob Strecansky** 08:14 Yeah, we can wait for that. Sure.
And contribute… This is renovate, renovate. This is, say good, blah, blah, blah.
That's a long time ago, but… Someone has… I'll have to review this one, I believe… This one that I also have to read. It looks like you… Reviewed this.
No.
**Chris Lightfoot-Wild** 08:55 Sorry, I've got, I'll come back to that one. Okay. Again, I was, I was thinking I probably need to run the pipelines locally, because obviously people are, like, thinking… they're blocked by things that aren't their fault, and it's a pain to contribute, but I don't want to just sort of blindly click merge if the pipeline's… I've never seen the test actually pass.
**Bob Strecansky** 09:14 Sure.
**Chris Lightfoot-Wild** 09:14 We can at least do that locally. I wondered, actually, if… Do we maybe want to make the static analysis, at least fan some of them not fail?
Like, you know, continue on error in the workflow?
**Bob Strecansky** 09:29 We could… we could… I think that would be a good mediation thing for the time being, if you want to do that.
**Chris Lightfoot-Wild** 09:33 Yeah, we could at least see, then, that the code seems to pass the test suite, and then, you know, maybe there's some… Linting and things to do for the annotation of the code, but…
**Bob Strecansky** 09:44 Right.
**Chris Lightfoot-Wild** 09:44 I want to block everyone by saying, oh, it's not… it's red, so therefore I can't go.
**Bob Strecansky** 09:49 Right. Sounds like a plan to me.
**Chris Lightfoot-Wild** 09:51 Cool, I'll, I'll pay out those changes then, too.
country workflows.
**Bob Strecansky** 09:56 Sounds good.
None issues… Oh, that's that one that he opened. Yeah, there hasn't been any new issues in a while.
Cha-cha-cha-cha-choo!
Okay.
Let's check our stats. Do we make it to 40 million? Oh yeah, we did. Let's go!
And then… Alright.
That's all I have for today. Y'all have anything else?
Alright, we'll see y'all next week.
**Pawel Filipczak** 10:36 Dude.
**Chris Lightfoot-Wild** 10:36 Cecile.
**Pawel Filipczak** 10:38 Mine.
