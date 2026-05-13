SIG: Communications SIG
Date: 2026-05-12
Duration: 34 minutes
============================================================

## Zoom Recording Transcript

**Tiffany Hrabusa** 01:59 Hello.
**Jay DeLuca** 02:00 Hello. I'm gonna stay off camera, I'm having some, lunch, but I'm here.
Wonder if anybody else is, gonna join us today.
**Tiffany Hrabusa** 04:32 Just wondering that.
Give it another minute, maybe? Let's see.
**Jay DeLuca** 04:39 Yeah.
Vitor, so you're in Germany now? Is that right?
**Vitor Vasconcellos** 05:04 Not yet, not yet. I just got my visa. I went to the consulate to get my passport back.
So… Everything should be ready now. I mean, I still need the… Travel documents for the dogs, but…
**Jay DeLuca** 05:22 Do you have a tentative time frame?
When you hope to be over there?
**Vitor Vasconcellos** 05:28 I believe on… 25 or 26th May, over… in the next 2 weeks, maximum. Nice.
**Tiffany Hrabusa** 05:39 Wow.
**Vitor Vasconcellos** 05:40 Yeah.
**Tiffany Hrabusa** 05:41 Excited?
**Vitor Vasconcellos** 05:41 Can't wait.
**Tiffany Hrabusa** 05:46 Yeah.
**Vitor Vasconcellos** 05:50 It's deserving crazy already.
**Jay DeLuca** 05:55 And do you have a… you have a place all lined up where you'll… you'll live and all that?
**Vitor Vasconcellos** 05:59 Yeah, I have a temporary apartment for the next 2 months, and… There will also be a consultant to help me finding the permanent place.
So… That'll be easier.
**Jay DeLuca** 06:17 And did you start a new job? Is that what…
**Vitor Vasconcellos** 06:21 Oh, yeah, yeah.
It's a… it's a new role. I'm going to vote, which is DoorDash, basically.
Oh, cool. So, I left MercadoLibre, and… It's a… it's a… Totally new role.
**Jay DeLuca** 06:37 Also, to remove, like, they're… They're moving you out there?
**Vitor Vasconcellos** 06:42 Yeah.
**Jay DeLuca** 06:43 Nice, very cool.
**Vitor Vasconcellos** 06:44 They're… they're supporting and providing all the… all the support that I need.
So… The only… the only thing I'm having to worry for now is the docs. They are not covering the documentation or the… The process for the dogs, it's not included, but… It's fine.
**Jay DeLuca** 07:04 How many dogs do you have?
**Vitor Vasconcellos** 07:06 Two… I have two dogs.
**Jay DeLuca** 07:10 So, yeah, that's… that's important.
**Vitor Vasconcellos** 07:12 Oh, no.
None of them is around.
**Tiffany Hrabusa** 07:18 A consultant to help find an apartment is… is clutch. Like, there's… I've not moved internationally for long term, like, I've spent months there, but never had to find an apartment. But I did move across the country in the U.S, from Connecticut to Los Angeles.
And, while my partner went to work, I didn't have a job yet. I literally just drove up and down the streets looking for apartments with signs saying that they had… had space for rent. It was not fun.
**Vitor Vasconcellos** 07:56 Yay!
**Tiffany Hrabusa** 07:57 I've heard that.
**Vitor Vasconcellos** 07:57 Very hard.
**Tiffany Hrabusa** 07:58 rental market in Germany is… Is very competitive, so…
**Vitor Vasconcellos** 08:04 Yeah.
Especially for someone who is… who never… who's never been in Germany, or… Who is not a… who's a foreigner, and… Those are all those… the difficulties we have to find that, so having a consultant is… Will be awesome, and they are also providing the support to visit places and find good neighbors and neighborhoods.
And… everything, so… I've… I spoke to Georgia Rasi, and… He also mentioned that he gave me some advices on neighborhoods and places where he… Hmm… Around where he's living now, so… But the consultant is.
Way better, also.
It's, I mean, it's someone who's already there, and who already knows the city, so…
**Jay DeLuca** 09:08 Yeah.
**Tiffany Hrabusa** 09:10 Well, congratulations.
**Vitor Vasconcellos** 09:12 Thank you. Yeah, definitely. Congrats. Thank you, thank you.
**Tiffany Hrabusa** 09:16 Hey, Sophie, I saw that you joined while we were chatting.
**Vitor Vasconcellos** 09:20 Hey, Sophie.
**Sophie’s iPhone** 09:21 Hello! Hi, everyone.
**Tiffany Hrabusa** 09:24 We don't have a lot on the agenda, but I think it's almost 10 after, so I think we can probably get started.
For the, approvers and maintainers on the call, you probably saw me, like.
flailing about in our, channel yesterday about the… the supply chain attack, and Marlia was… very helpful, but there are several outstanding Dependabot PRs that I am just… Really afraid of touching.
Because I don't really know what I'm looking for. Like, I understand I'm supposed to check the commits, but like… It's tricky. So… if there's an engineer among us who has time to take a look at those, and just make sure that I'm not going to, like.
blow up the repo by merging them. That would be great.
**Jay DeLuca** 10:21 Yeah, dependable ones are tricky, because, like, I mean… A lot of times, yeah, you just want to check the, like, the package JSON, make sure that nothing is being added to, like, pre-run scripts or things like that, but… like, sometimes… You can go deep and be like, okay, what actually changed?
Between versions, but that's, like… That's a big investment of time. I think, like, some of these I see are, like, OpenTelemetry, specific dependencies, like, those should be… Fairly safe, and I don't see anything weird in, like, the diffs.
Do either of you know if we have rules around the age of dependencies? Probably doesn't matter so much for, like, the OpenTelemetry ones, but, like, in the Explorer project, we make it so a release has to have been out for at least 7 days before the PR is even opened.
And so, like, that's usually… like, these things usually happen within a day or two of the release, so, like, that usually gives plenty of buffer. But I don't know if we have that configured.
**Tiffany Hrabusa** 11:29 I don't know.
**Vitor Vasconcellos** 11:31 Yeah, for the I.O. repo, I don't think we have.
I don't know if… There is something for the… the JavaScript recalls, or the limbs.
**Jay DeLuca** 11:46 Yeah, maybe we can…
**Vitor Vasconcellos** 11:47 Consider it.
**Jay DeLuca** 11:47 adding that.
**Tiffany Hrabusa** 11:49 Okay, let me make a note about that. And I can create a follow-up issue, I'm sure Patrice will have something to say about it when he's back, so…
**Jay DeLuca** 12:04 Okay, so we're just using Dependabot right now, or do we use Renovate, too?
**Vitor Vasconcellos** 12:10 No, we are using Defendabot, but… I… I had raised an issue yesterday to, to migrate, so… I think we should… Big net over the next days, and…
**Jay DeLuca** 12:31 Yeah, because I think it was with the Renovate that I was able to add those rules. I mean, I'm sure Dependabot probably has similar, but, I think most of the projects are using.
Renovate.
**Tiffany Hrabusa** 12:53 Did I represent that right, Jay, in the note?
**Jay DeLuca** 12:57 Sorry, I was on LinkedIn.
Yes.
**Tiffany Hrabusa** 13:04 Okay, I will create an issue.
**Jay DeLuca** 13:07 And I'll, I'll put a link for how we do it in the Explorer.
**Tiffany Hrabusa** 13:14 Okay, thanks.
**Jay DeLuca** 13:32 Cool.
I don't know if we want… do we want to move on to the next?
Yeah, I mean, I think you… the people here, probably already have seen it and already know, but I was just gonna raise awareness that I created, like, a skill that looks back at the previous week's activity in the Explorer, so that I can post regular updates in Slack.
So it's easier for people to keep up with what's going on there.
We've had a lot… The number of contributors is pretty crazy, let me see what we're actually up to now.
Or up to 2 and they've been… multiple PRs and issues a day. So, lots of activity, which is great. I think we need to… provide some feedback to some of the contributors who seem to think that they should get a review an hour after they open a PR, and they're… I can't tell you how many times I was tagged over the weekend, like, Jay, can you review this? Jake, can you review this? But… but we're making a lot of progress, so it's pretty awesome.
But yeah. So yeah, I'll be posting, some updates in Slack. I'm gonna try to do it on a weekly basis.
**Tiffany Hrabusa** 14:44 Wonderful.
Yeah, I've been trying… I haven't… so, I subscribe to the repo, and I have seen all of the notifications come through. I have not been able to look at, like, in detail at most of them, but anything that I see, like, flagging collector, I kind of, like, take a look and see, So, that's exciting.
**Jay DeLuca** 15:08 Yeah. Yeah, the, the collector stuff is interesting, because we have a bunch of contributors who are, like, looking to build out the pages and stuff, but… Some of it is a little, I don't know, I don't know if it… if the way that we're visualizing it makes sense, so that's why I don't know if you saw, but I tagged Pablo to… to see if he can give a look at it, but if you're ever curious and want to look at some of those deploy previews for some of those PRs, if anything pops out to you, We're mostly looking at, like, the stability levels and stuff right now, but… So that gets a little complex, because, like, they have different stability levels by signal, and then, like.
By pipeline, like, traces to… to metrics and things like that. It's… it's bizarre, so we just gotta come up with how we want to visualize it.
But, yeah, most of those PRs probably wouldn't be worth your time, to be honest.
But… But yeah, the collector ones would be good to get some eyes on.
This morning, I think Marillia, Vitor, and Martin from my team at Profana, too, all chipped in. We were making some progress, and Luca, too, so it's… It's great, we got so much activity, it's awesome.
**Tiffany Hrabusa** 16:18 Yeah.
I think people are excited about having a front-end project.
**Jay DeLuca** 16:23 Yeah.
**Tiffany Hrabusa** 16:24 Which is great.
That's really great.
**Jay DeLuca** 16:27 Yep.
Yeah, I think our biggest problem is just… or challenge is just getting people to submit changes, like, incrementally in, like, small, reviewable chunks.
And not, like, 50,000 lines of code. But…
**Tiffany Hrabusa** 16:41 Yeah, I'm still, along those lines, I don't remember if I mentioned this in our channels, but at, KubeCon, EU, in March.
one of the maintainers, I think it was Tyler Helmuth, Helmuth from Honeycomb, did a lightning talk about how to contribute to open source using AI, and how to do.
**Jay DeLuca** 17:10 diverse.
**Tiffany Hrabusa** 17:11 Possibly.
Hmm.
there were some really good tips in there, and so I want… I haven't had time, but I… what I would love to do is ask him if we can take that content, like.
like, strip out all the honeycomb stuff, and just, like, make it hotel-specific content that we can… post everywhere. Like, in all of our contributing guides, and like, because it… I don't know. I feel like it would be…
**Jay DeLuca** 17:46 There is a contributing… in our contributing guide, I think we have a link to some version of an AI policy.
That I think lays out some of it, but… I agree, I saw that, presentation, I thought it was great.
**Tiffany Hrabusa** 18:03 Yeah, I feel like we could do… it doesn't even have to be, like.
Like, a video, necessarily. It could just be, like, a voiceover.
**Jay DeLuca** 18:18 Yeah, maybe this isn't exactly the same as what he… yeah, this isn't really what he did. His was more like… As a contributor, the procedural approaches, this is more like… the do's and don'ts of actually using LLMs.
Yeah, I think that would be really a great addition. I mean, even if we just linked to his existing talk, like, I don't… I don't remember it having a much, like, vendor… Nuance to it, necessarily, so… It'll be worth liking.
**Tiffany Hrabusa** 18:51 Yeah.
Okay, Sophie, I saw your message. If you want to take that on, feel free to contact Tyler.
And, see if he'd be open to us using his content, content, and… At, like, linking to it directly, or… redoing some of it in, like, hotel world. I know, adriana and Reese.
And Julia, the community managers, are trying to Like, unify and make our… like, videos and everything kind of consistent and more professional-looking, so, they may have some input there. I know that you've worked with them before on the… humans of hotel stuff, so… Yeah.
That was an impromptu topic. I'll just add it here.
But yeah, I… the massive PRs are definitely… Problematic.
So…
**Jay DeLuca** 20:01 Yo.
**Tiffany Hrabusa** 20:02 We also… I saw, yoshi, one of our, localization approvers, I think? Maybe he's a triager, I'm not sure, has been going through some PRs and pushing back on people who aren't following the policy, which is nice.
**Jay DeLuca** 20:21 Yeah, I saw that.
Yeah, I think it's good to have some… some guardrails, and I think I've been a little lax on the Explore side with some of the contributions, but I don't want to discourage anyone, so you just gotta find that balance of… Please follow these rules versus… I'll just keep going, but…
**Tiffany Hrabusa** 20:44 Yeah.
**Jay DeLuca** 20:45 do it this way.
**Tiffany Hrabusa** 20:46 Yep.
Okay.
Alright, Sophia, I'm… I'm gonna link you, or not link you, I'm gonna, add you as an action item on here.
**Sophie’s iPhone** 21:20 Yeah, that sounds good.
**Tiffany Hrabusa** 21:21 Okay.
Thank you.
Yep.
Okay, anyone have anything else?
**Vitor Vasconcellos** 21:37 I think… I think I have something, I don't… I don't know if you'll… Don't have a chance to… to see those.
images from the Explorer. We are… how can I… how can I say? Refactoring the… the fronting? The… the UX for that, and… Those pages are… More, like, of a concept.
And there are some changes that I'm applying, like… Trying to… to use the… a very similar layout from the .io website now.
And… Well, this is something I've been working Over the past week, and… Hopefully, after this first phase, we can… Also have other contributors, and… After having the… after we have the foundations ready, we can have other contributors and start to… To get more traction on that.
But… Anyway, if you have any… this was purely generated by AI, I'm not a… Designer, so… I've just contributed to, with some prompts.
I kind of enjoyed the results, and…
**Jay DeLuca** 23:07 Yeah, I think it looks great.
I have, like, I think we'll still need to work out a bunch of stuff as we go along, but, like, in general, like, I like the banner approach, I like the color schemes, the navigation, I liked the, the side panels for… Component detail navigation, yeah, I think it's great. I think it's… So, similarly, I have the same caveat. It's like, the initial design was all kind of AI-guided, and I'm not a designer, and I tried to massage it and put it In the right direction, but I think this is, like, this is a big step up from where it started, so I'm super stoked on it. I think it'll be… as we're already discussing in the comments on some of the PRs, I think it'll be tricky to have the development happen in parallel, because there's going to be a lot that changes.
I even wonder if, like, for some of the pages, it makes sense to create, like, completely separate Instead of trying to, like, feature flag individual components within a page, just to have, like.
like, a V2 kind of even directory of pages and components, and then we just delete the other one when we get there, but… Yeah, I think the biggest challenge here is just gonna be, like, figuring out how to develop it in tandem and be able to review it and all, but… I'm stoked.
**Vitor Vasconcellos** 24:34 Yeah, that makes sense. I was trying to have the feature flagged to avoid many conflicts, but… I think this is… Gonna be too hard to… to avoid them, or to… Have both versions.
Living under the same space at the same time.
**Jay DeLuca** 24:55 Yeah.
**Vitor Vasconcellos** 24:56 I don't know.
**Jay DeLuca** 24:58 I think it, like, it also has to do with how long it… we were in, like, the state of flux, like, I think if… if we were just, like, had a full week of just, like, heads down, just bang it out, then maybe it would make sense to interleave things, but I imagine that this is gonna take us weeks, if not months, to get Right? Potentially, I don't know, we're moving pretty quick, but, so I think having it as separate as possible for the review process is probably our easiest.
path forward, but I don't know, I haven't looked too deep into it, just kind of brainstorming, maybe there's a more clever way for us to do it, but I think what you did so far with, like, the theme selection is all very nice and clean.
it's just gonna be when we get into these individual layouts.
**Vitor Vasconcellos** 25:50 Yeah, perhaps the V2 makes more sense, so yeah, I'm gonna give it a try instead of… Using the same codebase, or… I mean, we can.
**Jay DeLuca** 26:02 Yeah, exit.
**Vitor Vasconcellos** 26:02 The same codebase, but creating separate pages makes more sense.
**Jay DeLuca** 26:07 Yeah, especially with, just with how much gets touched each time, and how many PRs we're now having, like, the merge conflicts, I think are just gonna be, tremendous. So… And that de-risks the reviews a bit, too. Like, if we're just touching completely gated files, then, like, the risk of regressions and stuff is… Non-existent, so… But very cool. And, I don't know if, Tiffany or, Sophie, if either of you have also seen, but… Vitor hooked up some automation that adds Screenshots as a comment for all the different themes.
the different, desktop revolution… resolutions. So this is gonna make it a lot easier, too, to do reviews, which is… Amazing. I'm stoked on this.
**Tiffany Hrabusa** 27:11 I did not see that.
That's incredible.
Yeah.
**Jay DeLuca** 27:17 Yeah, looks great.
**Vitor Vasconcellos** 27:19 This is looking interesting.
**Jay DeLuca** 27:23 Like, this is… this would have already… helped catch… like, some… some missing pieces on some of the other ones, like, a lot of the mobile screens have, like, cut-off stuff on a lot of the pages, and if we had this on all of our PRs up to now, we would have caught those, like.
Way sooner, so… I think, yeah, it's gonna be a great addition. So all you have to do is add a label to it, and it… it will kick off.
**Tiffany Hrabusa** 27:55 Nice.
**Jay DeLuca** 27:56 Cool stuff.
**Tiffany Hrabusa** 28:00 Yeah.
**Jay DeLuca** 28:07 Anything else?
**Tiffany Hrabusa** 28:11 Not for me. I'm just still trying to get caught up.
everybody wants everything all at once, right? So…
**Vitor Vasconcellos** 28:23 Oh, and we graduated, so… This is the most important part. We didn't mention that.
**Tiffany Hrabusa** 28:32 Yeah, congratulations to everyone.
Yeah.
**Vitor Vasconcellos** 28:36 And it's…
**Tiffany Hrabusa** 28:37 I'm…
**Vitor Vasconcellos** 28:37 So nice.
**Tiffany Hrabusa** 28:38 I'm still a little, like… everybody's talking about it, and OpenTelemetry has said nothing officially, and I'm like.
But I understand the GC is working with CNCF to figure that out, but I'm like…
**Vitor Vasconcellos** 28:54 Yeah.
**Tiffany Hrabusa** 28:56 We have, like.
**Jay DeLuca** 28:57 I think as we got close, they would have everything canned and ready to rock.
**Tiffany Hrabusa** 29:01 Well, I kind of get the sense that the vote came out of the blue. Like… that… I mean, at least that was… the sense I got, because I didn't hear any wind that it was coming down.
**Jay DeLuca** 29:13 Yeah.
**Tiffany Hrabusa** 29:14 to an actual vote. I saw, Pablo had posted in, Some of the collector channels, like, the notes about that we had met all of the requirements.
Like, there was a document that kind of… Spelled it out.
But I didn't realize that the vote was gonna come Like, immediately on the heels of that, so… And it happened on, like, a Friday night, right?
So… Everybody else got to it on the weekend before… before we did.
**Jay DeLuca** 29:46 Yeah.
**Vitor Vasconcellos** 29:49 And I saw the comment, it was like, double pass it, it is done, and I was just like, okay, is that it?
What else? What do we do now?
**Tiffany Hrabusa** 30:03 Yeah, I'm not.
**Jay DeLuca** 30:04 I'm like.
**Tiffany Hrabusa** 30:04 Ages, yeah. I mean, I think… From my understanding, there were some… requirements that the TOC had asked for that We haven't fully implemented, we've started, and they were happy with that, but I think we need to follow through on those, so…
**Jay DeLuca** 30:24 Yeah, like, the whole Stable by Design initiative, and…
**Tiffany Hrabusa** 30:28 Yeah, and there's some collector stuff, too, I think, that is still… and… the docs refactoring is definitely not done. So, I think they just kind of dropped that off the list.
**Jay DeLuca** 30:43 Well, we're making progress.
**Tiffany Hrabusa** 30:45 Yeah, we are.
VR.
Cool.
Okay.
I think that's it, unless anyone has anything else.
And get another half hour back in our day.
**Jay DeLuca** 31:02 Nice.
Okay. See you guys later.
**Tiffany Hrabusa** 31:04 See ya. Bye.
**Sophie’s iPhone** 31:06 Hi, everyone, thank you.
**Vitor Vasconcellos** 31:07 I hope, mad.
