SIG: CI/CD SemConv SIG
Date: 2025-10-16
Duration: 38 minutes
============================================================

## Zoom Recording Transcript

**Dotan Horovits** 01:54 Hey, Drew.
**Adriel Perkins** 01:58 Hey, Dotan, how are you?
**Dotan Horovits** 02:00 Good, how are you?
**Adriel Perkins** 02:02 Doing okay, thank you.
**Dotan Horovits** 02:04 Congratulations, man! It's been… first of all, it's been too long, and yeah, really happy to hear the, the good news.
**Adriel Perkins** 02:10 Thank you, thank you.
And yeah, it has been a while. It's been… been too long for sure, for sure.
**Dotan Horovits** 02:18 Yeah.
Cool.
**Adriel Perkins** 02:37 So how, how are things with you?
**Dotan Horovits** 02:40 Good, good, pretty, busy, and there's also, like, a… Holiday period here, so, Even more hectic now, coming in, trying to pick up all the pieces and everything, so, yeah.
Catching up on lots of things.
**Adriel Perkins** 03:00 Cool.
**Dotan Horovits** 03:01 Yeah, yeah. Got the, SIG approved, I don't know if you saw that, for the, service and deployment, SEMconv.
**Adriel Perkins** 03:11 Oh, nice, nice.
**Dotan Horovits** 03:13 Yeah, yeah, it's, there's the one, one meeting already. I, couldn't make it because I was in, in Poland for, for an event, but, Yeah, really happy to see this, picking up.
**Adriel Perkins** 03:30 Sweet, it's right before this one. It's at 8.
**Dotan Horovits** 03:34 Sorry?
**Adriel Perkins** 03:35 It's it. That meeting is right before this one?
**Dotan Horovits** 03:39 It's not weekly, first of all, and it's, See, I need to check the… because we talked about, like, alternating times and things like that, so I need to check, actually, what's the latest on this one. The previous one was, was Thursday, but, But I think the last discussion was to try an alternate, because there are a few folks from India, and trying to find the right time, so… You know how it goes when you're, you have a new, new SIG.
Nailing it down isn't easy, so.
**Adriel Perkins** 04:11 Well, I'll try to join the Thursday morning ones, because I know there's gonna be collaboration for deployment.
**Dotan Horovits** 04:18 Yeah, for sure, I, yeah, yeah, that's why I flagged you, on the, on the charter formation time, because I, I was sure that you, you'd probably have good feedback there, but, Anyway, it's open, and I'm sure that you can give some… they're already starting discussions on specific, like, the meeting was about the phases, but then we already got into discussing the specific attributes and things like that, so things are moving nicely.
**Adriel Perkins** 04:45 Nice.
**Dotan Horovits** 04:46 Yeah, yeah.
So what about you? Are you going to, carry, like, what's your capacity with the new role? Will they allow you to carry on expanding your involvement here, or, like, do you know what's, how it's going to fit in?
**Adriel Perkins** 05:04 It's definitely going to fit in. It was a condition of my acceptance. So, they're looking forward to… They don't have an open source con… Hey, good morning.
They don't have an open source strategy, so that's something that I would like to work on. They're definitely wanting it, and so that's part of the reason I think I'm getting brought on. But yeah, I don't know all the measures of bandwidth that I'll have, but it seems like I'll have a reasonable chunk.
enough time to continue to drive things forward. More so than I certainly had at the last place.
**Dotan Horovits** 05:44 Nice, nice, I'm really happy for you. I know that you were looking for that, and I'm really happy today. Like, sounds like a perfect fit that they're looking for someone to shape up the, the open source, strategy and structure and everything, so, right man for the right job.
**Adriel Perkins** 06:00 Thank you.
**Johannes Koch** 06:01 Where are you headed to, Adrian?
**Adriel Perkins** 06:03 I work for Grainger now.
**Johannes Koch** 06:06 For what? Grainger. Never heard. Grainger, yeah. Grainger! Oh, yeah, I heard of Grainger. Okay.
Cool.
**Adriel Perkins** 06:16 Yeah, it's been good. I think this is week 3? Yeah, this is week 3. It's been good so far, which, I mean, you know, there's always a honeymoon period, but, It's been good.
I know my boss, so…
**Dotan Horovits** 06:28 Summer.
**Adriel Perkins** 06:29 He lives, like.
**Dotan Horovits** 06:30 20 minutes down the road for me, which is a bigger part of the reason I joined, because I enjoy working with him, so…
**Johannes Koch** 06:37 That can be good and bad, if you know your boss.
**Adriel Perkins** 06:39 Yeah. Yeah. In this case, I think it's good.
**Dotan Horovits** 06:43 Nice. Very nice.
**Johannes Koch** 06:46 Cool.
**Dotan Horovits** 06:46 How big is it, by the way? Like.
**Adriel Perkins** 06:49 There's, like, 27,000 people at Grainger, I think is the total, and that's… they're not all in the technology portion, but… Yeah, it's a, it's a large company.
They've been around for 100 years.
**Dotan Horovits** 07:06 And this is, like, across the board, like, it's not a specific unit. What you're going to do with the open source and everything is, cross-cutting throughout the company.
**Adriel Perkins** 07:16 Well, you know, definitely the technology portion. We'll see how cross-cutting it is, but, yeah, it's, My boss and my boss's boss are pretty… Not… not very far away from the CTO, so…
**Dotan Horovits** 07:31 Yeah, super cool.
**Adriel Perkins** 07:33 We'll see.
**Dotan Horovits** 07:34 Yeah, no, no, sounds amazing, really, really happy with you, man.
**Adriel Perkins** 07:38 Thank you.
**Dotan Horovits** 07:41 I'm not sure if we're, waiting anyone else, so, Adrian, if you want to, Okay, go roll it, and I'll let you lead that.
**Adriel Perkins** 07:51 Yeah, I only had, the one thing, which is the straw poll. I was gonna repost your LinkedIn post that I saw, actually, and just include that straw poll in there.
**Dotan Horovits** 08:02 Yeah, actually, it's a good idea. I should have thought about that, just, It was a moment of, like, I just enjoy the, okay, let's share it to the world, and, not, polished, but, Honest, yeah, so… Sure.
**Adriel Perkins** 08:16 Yeah, so yeah, that's it, just… I think most of y'all have filled it out. Looks like we have a little bit more time openings this year.
**Johannes Koch** 08:28 Can you tell me that I can't remember if I did, but I will find out.
**Adriel Perkins** 08:31 Yeah, I'm actually really surprised it's, like, green across the board. There's a lot of greens.
**Dotan Horovits** 08:39 Nice.
**Adriel Perkins** 08:40 So… That's cool.
Tuesdays at 10am and Thursdays at 10 a.m. appear to be, like, the really good days.
**Dotan Horovits** 08:52 Do you wanna share your screen and, or maybe I…
**Adriel Perkins** 08:56 Yeah, I can.
**Johannes Koch** 09:00 Oh, I did not fill it out yet.
That was an old pork.
**Dotan Horovits** 09:06 Yeah, yeah, but we did that, like, just before the beginning of the summer holidays, and people were not responsive, and so we said it's not really reflective, and that we'll… Re-issue it after the summer break, and… It's good we did, according to the results.
**Adriel Perkins** 09:30 Yeah, a lot… people are a lot more open now.
That's good.
**Dotan Horovits** 09:43 As you said, like, let's repost it just to, remind people that it's still open, and I guess, finalize it in a week or two, and see what's the… What's the answer there?
**Adriel Perkins** 09:57 Yep.
**Dotan Horovits** 09:59 Sounds good.
Beyond that, yeah, sorry, I didn't put my name in it, I'll add it in. Beyond the poll, do you want to, Discuss the, the Phase 2 scoping, anything related to that that.
**Adriel Perkins** 10:21 Yeah, I can. I'm going through the comments.
Now, I think I've pretty much addressed 99.8% of them.
There's certainly a little bit, like… I mean, I had someone in mind here, but I don't want to name it, because it's… it's not solidified.
But yeah, I mean, I think there's really just, like, the two comments. I just pinged Josh to see if he was willing to continue to be a sponsor for this one. Carlos has already approved, so we're good there. I've already resolved all the other ones. I'm making the update here for this one, so I have that changed locally I'm about to push.
Yeah, I'm gonna phrase it.
denoting signal.
**Johannes Koch** 11:20 But when did we want to get this closed? Because I came back from vacation today. Sorry, German, we have too many vacation days, and I did not have time to read it yet.
If you say yesterday, then that's fine. I'm just…
**Adriel Perkins** 11:39 Yeah, I mean, we wanted to months ago, but it is what it is. So, like, you know, we're just… hopefully by the first meeting, before the first meeting, which on the… on the straw poll said, like, November 4th or 6th. So as the first week in November would be our first meeting of Phase 2. Okay. Well, in two weeks.
**Johannes Koch** 11:57 Cool.
**Adriel Perkins** 11:59 I don't know if they have approvers in the community template.
I don't mind.
**Dotan Horovits** 12:04 That's why I asked. No, no, if it's not part of the… that's why I addressed it to Dan, just to guide us if this is… I think I saw it in one of the others, but I might be confusing templates or formats or whatnot, but… I thought I saw, approvers listed as well. So, I'm just saying.
How about… let, Don see… actually, see, someone did, I like there, is that him?
Who did they like on the, on my question? Because if it's him, maybe that's his answer, I don't know.
**Adriel Perkins** 12:37 I don't know. I don't know.
**Dotan Horovits** 12:38 So, hover over to see… Yeah, I was typing Yeah, just.
**Adriel Perkins** 12:42 It was Carl.
**Dotan Horovits** 12:43 No, no, it's Carlos, okay, so it's, I don't know if it means that he knows that we need or not, but anyway, so let's.
**Adriel Perkins** 12:49 Yeah, I'm just gonna add CICD SIG approvers, because we have a group for that.
**Dotan Horovits** 12:55 Okay, all good. So that's also a good idea.
**Adriel Perkins** 12:58 And that way, if it changes, it's, like, very clear, like, oh, hey, look, a person… like, it stays up-to-date instead of me having to go update someone's name every time they get added.
**Dotan Horovits** 13:06 I like this solution, yeah. Alias is always good. It tastes fresh.
**Johannes Koch** 13:11 So as a first look at it, just a quick question. Are we also, kind of, considering deliverables like… best practice implementations, and or, like, marketing slide deck for this kind of stuff. So… so… the SIC has established a way of talking about semantic conventions and CICD metrics and stuff like that, but I think that's all stuff that is somewhere hidden in stuff that you have already created for your presentations, Adriel, right?
is… would that be a deliverable of the SIC as well, or not? Like, a docs document of, this is how we explain, this is how we talk about that, and this is how we… Shh… I don't know. Do I make sense?
**Adriel Perkins** 14:07 You do, I'm not sure.
**Johannes Koch** 14:15 Yeah, we haven't dealt formally with the, like, we did advocacy for that, like, ad hoc.
**Dotan Horovits** 14:20 As opportunities arose, and as we got excited, but we never scoped it as part of the… the core work of the… of the team, I guess.
**Johannes Koch** 14:30 It's just a question if we want.
**Dotan Horovits** 14:31 No, no, no, it's a legitimate question, I'm not saying the question, I'm just sharing that the core scope of the SIG was always the main thing about the sort of… either the semantic conventions or the reference implementations, or, or, you know, things like that.
**Johannes Koch** 14:52 at the end, we could make, I don't know… we have that one… we have that… those two blog posts that we have on the CNCF block, right? We could potentially make another blog post part of the deliverable, we could potentially make a… a SIG page to it, where we kind of validate vendors that have implemented the semantic conventions already, or stuff like that.
that support the Semantic conventions. I mean, I don't know if that…
**Dotan Horovits** 15:19 So, I'm saying it's, well, for blog posts, it's, again, it was also ad hoc. I remember actually one blog post. Did we have two? No, I'm confused.
**Johannes Koch** 15:28 I think maybe it's only one, but, but, so…
**Dotan Horovits** 15:30 Yeah, we reposted afterwards to the hotel blog, but it's the same text, besides some editorial changes that they requested for signing.
**Johannes Koch** 15:40 What I'm trying to say is that this would make make things… give other people a chance to contribute a bit more as well, right? And then get us to have more deliverables that are actually trackable, like measurable, right? Measurable commitments, if that makes sense.
**Dotan Horovits** 16:00 I don't know. It's a, like, we can do that.
I know that we were pretty short on people involved in the core thing, so maybe this will open up the door for others.
Maybe less technical, that can help more about, documentation, things like that, but, I guess our main challenge has been to get the folks on the, on the core, either development of the reference, implementations or, or, SEMCON themselves, but, Adrio, feel free to, to chime in with your take on that. I don't know.
**Adriel Perkins** 16:36 Yeah, we definitely, started strong, but… it was few that did a lot of the work, for Hands On Keyboard, and that took a lot of time. We're also not… I don't think Phase 2 is gonna be the last phase.
Right, so I think there's an opportunity for a Phase 3, and maybe even a Phase 4. We want to… the guidance from the GC and the TC is that we want to keep These phases small.
Relatively to what we could reasonably accomplish within a, like, guesstimated timeframe.
And then we can always open up another one for another set of things. Now, does that mean if we get more done, that's a bad thing? No, absolutely not, right? Like, we can certainly over-deliver in the period of time we have.
But I think the main focus for this is actually getting, like, real integrations, and I think the marketing kind of comes… can come as a byproduct of that, because, like, until we get, say, integration with GitHub, or integration with GitLab, or, like, until we get a collaboration going on with CD Events.
Like, I don't want to, like, plan to market that if it doesn't happen. I'd rather just, like, as a byproduct for talks and, you know, maybe some blog posts, we could certainly, like, be agile and add, hey, we just got this collaboration going on, we should announce this, let's go ahead and add a, like, a piece of work on that, and someone can take that. That would be great.
I just don't know that we should scope it into the Phase 2 outline.
Because I'm trying to be, like, a little nebulous on the Phase 2, like, just enough to where it's, like, we have flexibility to be agile, or nimble, rather, so… Does that make sense? What are your thoughts on that.
**Johannes Koch** 18:12 It does, it does make total sense, Adriel. That's essentially what I kind of was trying to say.
Yeah, so…
**Dotan Horovits** 18:23 By the way, Adriel, we can maybe try and do a follow-up, it's a good idea, in that sense to, do, sort of, maybe to open and to publicize the Phase 2. Again, I had my spontaneous LinkedIn post, but that's beside the point. We can maybe have another blog post to, you and I together, to summarize Phase 1, Let people know that Phase 2 is beginning, it's sort of a… another, like, compelling event for folks to join the bandwagon, or something like that, so… Maybe you can even piggyback on the KubeCon time frame like we did last year, so… even though, I won't be at KubeCon, you will be there, so maybe even if we make sure that this is published before KubeCon.
This can be an incentive for people to look you up, there in the hotel observatory, or, or something like that, to, to kickstart some discussions.
**Johannes Koch** 19:16 Yeah, and potentially we could also make sure that we get some more vendor involvement here, right? So I know that GitLab didn't really want to do what we wanted, right? But…
**Dotan Horovits** 19:25 Yeah.
**Johannes Koch** 19:25 But I know… like, "-0, as an example, I have a good friend working there, supports things out of the box, like, that kind of stuff is what we could… Kind of start going as well.
If that makes sense.
**Adriel Perkins** 19:39 Yeah.
Hmm.
**Dotan Horovits** 19:41 So, again, the question is, and I know, Adriel, you're also, just ramping up on a new job and everything, so… and the time frame for KubeCon is not that far off, so… Does that make sense? Do you want to do something like that?
**Adriel Perkins** 19:58 I just don't know that I want to add it in the doc.
**Dotan Horovits** 20:00 Because, like, the more things we added… Let's keep it.
**Adriel Perkins** 20:04 Oh, yeah.
**Dotan Horovits** 20:04 Okay, so I'm just asking if this, time-wise, if this is something that you're…
**Adriel Perkins** 20:08 Yeah, that sounds good. You think that you can…
**Dotan Horovits** 20:10 Because I'm also traveling, you know, but I thought maybe between the two of us, maybe we can, Pick it up and do something like that.
**Adriel Perkins** 20:18 Yeah, yeah, that sounds good.
Yeah, did you all see GitLab posted their observability stuff?
**Dotan Horovits** 20:29 No. They said they were stopping doing it, and then they made their… I saw an announcement about it the other day.
Really?
**Adriel Perkins** 20:36 It came from someone from another company, though.
**Dotan Horovits** 20:39 Can you, yeah, let me see if I can…
**Adriel Perkins** 20:43 Let's see if I can find it. I'm gonna go to my personal account, see if I can… I think I saved it to go back to it.
**Dotan Horovits** 20:52 Well…
**Adriel Perkins** 20:54 Hope I saved it to go back to it.
**Dotan Horovits** 20:58 We'll give us at least some.
**Adriel Perkins** 20:59 Oh, I did.
**Dotan Horovits** 21:00 Kansas.
**Adriel Perkins** 21:01 It's literally the last thing. Alright, copy link to post.
I should read this in detail for what it's worth.
Yeah, so, founder of Kilocode, And co-founder at GitHub, yeah. Yep. Or GitLab, yep.
**Dotan Horovits** 21:33 Yeah, club.
**Adriel Perkins** 21:35 They did it.
**Johannes Koch** 21:43 But this is… this is… Does this include observability?
for GitLab itself, and not for only CICD, right?
**Adriel Perkins** 21:54 That's a good question, I don't know.
**Dotan Horovits** 21:59 I don't provide any… There is a link on the comments, I see, for the communication.
**Adriel Perkins** 22:03 Here's the docs, yeah.
**Dotan Horovits** 22:08 The Atlanta.
**Johannes Koch** 22:08 But no auto support, as far as I said.
**Mihir** 22:11 I think they have mentioned that…
**Johannes Koch** 22:13 I have an auto support.
**Mihir** 22:14 Yeah, profile, endpoint, support.
**Dotan Horovits** 22:18 Play me here.
**Johannes Koch** 22:20 If they have auto support, then they should also implement the conventions.
**Dotan Horovits** 22:42 They ask for the hotel endpoint URL for instrumenting.
Interesting.
**Johannes Koch** 22:54 But this is more, like, for receiving.
**Adriel Perkins** 22:58 Yeah, so I think what they're saying is they're gonna… they emit telemetry now.
And… Well, where'd the thing go?
**Johannes Koch** 23:06 But on there it says CICD observability repository includes an example of a GitLab CI-CD pipeline with OpenTelemetry instrumentation that works in the dashboard.
**Adriel Perkins** 23:26 Oh my gosh.
I see what you're saying.
**Dotan Horovits** 23:31 Yeah, I see the paragraph. This helps you monitor your CICD pipeline performance and identify bottlenecks.
**Johannes Koch** 23:38 But that means they… so, this is, like, only the visibility of the that stuff, right? So if you look at this template code over here, it feels like… They haven't implemented the semantic conventions in the… So… in the exporter, right? They are just displaying stuff, is what I'm trying to say, right?
At least that's the… that's just the dashboarding tool of what I see.
So I can now send OTEL data to GitLab and display that hotel data in GitLab, is what I'm understanding.
**Dotan Horovits** 24:17 It's funny.
It'd have been great to, Have someone, the focal point, whoever is the, like, the product owner or whatnot, to ask them what's the story behind that, and if this…
**Johannes Koch** 24:31 Do we know the product owner?
**Dotan Horovits** 24:32 No, no, I, like, There's no one signed on this, it's… well, it's TechDoc, so it's okay that there's no one signed on it, but And the one who posted is not from the… from GitLab himself?
Right? It's, founder.
**Adriel Perkins** 24:48 No, I think he is, I think he's co… co- something on GitLab.
Or co-chair, something?
Is that what his profile said?
**Johannes Koch** 24:56 Co-founder and executor share at GitLab Inc.
**Adriel Perkins** 24:59 Yeah.
**Dotan Horovits** 25:00 Actually, I now see on the comments, Pranai, Prateek.
wrote, is the co-founder of Signals. Great to see signals is powering observability underneath GitLab.
**Adriel Perkins** 25:12 Oh, really?
**Dotan Horovits** 25:13 The visualization part, like the engine behind, is actually signals. That's funny, huh?
Okay, that's interesting.
Okay.
And they use ClickHouse, I see.
Alexander from Victorometrics asked them, they said the Click House is the back end. Like, they really created their own, Stark, but is… which is essentially based on, like, open source tools.
**Johannes Koch** 25:45 Well, which is what most vendors do, to be honest.
**Dotan Horovits** 25:48 Yeah, but the thing is that, like, they're established with their own… I don't know, I'm not saying right or wrong, I'm just saying, that's, like, the…
**Adriel Perkins** 25:58 Interesting.
**Dotan Horovits** 25:58 I'm not connected to him, but, you know, I don't mind, like, cold… link… LinkedIn him, or whatever, the CNCF Slack, and see if he's willing to, share some more, or… but if any one of you is… Adriel, you found it, so maybe you're more connected to that, and you want to reach out to him. Maybe just asking, if he can provide more information, and how that maps to the SEMCOM, or whatnot.
**Adriel Perkins** 26:22 Yeah, I'm very curious, because we basically got told no, and then, it… the issues were, like, shut down. Like, they weren't gonna do it, and then they did it.
So I was like, okay, cool.
**Dotan Horovits** 26:34 Yeah, but I wouldn't be surprised if he's a whole different part of the organization is not aware of any of the discussions we had, so…
**Johannes Koch** 26:41 But they didn't do it, they did do something completely different, Adriel, that's the point, right? So I think… The issue that we had, or that you had, was more like, okay, implement semantic conventions, as in to export the ultra data out of the GitLab runners, right? And they didn't do that, right?
**Adriel Perkins** 27:00 I think that was one of the.
**Dotan Horovits** 27:01 At least look like Rebecca. Yeah.
Well, if it's just a backend, it's less important for us. We want the native exportion, like, to export their own data, but maybe if they're taking ownership end-to-end or something, like, maybe they can be the right focal point.
**Johannes Koch** 27:21 Yep, let's do that.
**Adriel Perkins** 27:23 Very…
**Dotan Horovits** 27:23 So, Adriel, since you brought it up, do you want to reach out? Sure. Okay, sounds good. So, just let us know if you need my help in anything, you know.
I can nag people, so let me know if I can help, chase down the relevant folks there.
But yeah, good catch.
Would be interesting to hear more what they're up to, and Yeah, anyway, going back to the agenda item, so just to make sure, so in terms of Phase 2, I think we're pretty, solid on that. Sounds like, Adriel, thanks so much for, you know, doing all the, heavy lifting there and, cleaning it up. In terms of the marketing side, I think we'll leave it outside the formal scope and carry on in the, best, best, best effort type that we, we've done, but I think at least once, phase to sort of, get… get folks updated, and also, beginning of phase is a good time to maybe start a blog post as a teaser for folks that weren't aware to, to join. So, I'll follow up with you, Adriel, and we can see how to, to come up with something. Okay.
I think at least this one is also good.
Mira, I don't know if you, were in the first part, but we were talking about, like, the… decision of the new times for Phase 2, so… I don't know where you're based, but if you want to, to take the poll and see what times can work for you as well. We're about to close the poll soon, so… This is the other thing, like, to determine the times, yeah, I think this is…
**Mihir** 29:13 So, this is my first meet, I'm based out of India.
Just, you know, getting started with hotel.
and, yup.
Look forward to learn from community.
**Dotan Horovits** 29:29 Sounds good. Glad to have you here. Thanks for joining.
Adriel, do you have any on the triage to do, or are we good on that side?
**Adriel Perkins** 29:39 Yeah, I think I still need to create a…
**Dotan Horovits** 29:41 Yeah, sure.
**Adriel Perkins** 29:41 I think… I think I still need to create a Phase 2 board.
I did reach out to figure out anything about TeamCity, and I never heard back. So I messaged both of them on Slack, and I had an airbag, so I don't know what the status of that is. I will probably just, like.
close it as not done or something, or, like, gone stale, yeah.
**Dotan Horovits** 30:02 Yeah, for Phase 1, for sure, it's just a shame that we… By the way, when they, the folks from TeamCity themselves, because it was the other guy, I forgot the name, from, Australia that independently started doing some sort of integration, and then they… they hooked up, so I don't know if maybe one gone stale, if we can carry on with the other, although, obviously the… the vendor having the native one is always the best, but just wondering if… When you said them, is that both ands, or…
**Adriel Perkins** 30:32 It was the two that were linked on the issue.
**Dotan Horovits** 30:37 Okay. Because I don't know, I don't remember the other guy's name.
Yes.
Okay.
So, TeamCity, and I guess the other one that was… showed a bit of signs of movement was Jenkins.
that started implementing, but, I don't know where that stands, so, you know what, let me… unless you heard… did you hear anything from them?
I did not, no. So let me take that one, I'll ping them again to see where that stands. I think I tried to… piggyback on the end of phase one to try and push them to… across the finish. Hey, we're about to finish Phase 1, but I think the answers were pretty, no, it's not going to be in that time frame.
But I'll ping them again and, and see where things stand there.
Anyway, we're not naming them on the, thing, right? On the, on the, on the… yeah, so… Let's see which vendors are actually going to, you do that?
Okay.
So, you can write me down on the, on the Jenkins one. I'll take that task.
Was there anything else that.
**Adriel Perkins** 32:05 I do not have anything.
**Dotan Horovits** 32:06 Okay. In the… in creating the new board, essentially, we're porting all the, definitely the backlog, and what about the… are there, like, in-flight ones that will need to be ported, just to, know what's, like… is there any question marks regarding the, the porting phase, if it's just technical, or is something…
**Adriel Perkins** 32:28 There's a couple that will get ported over that are in Todo. I think the in-progress ones… can be closed. Nicholas, so, so, yeah, so Nicholas, who did the comment, or the talk on GitLab.
Long ago, KubeCon NA of last year.
**Dotan Horovits** 32:47 Handa… Those other devices, yeah.
**Adriel Perkins** 32:51 Yeah, he finished out the implementation, so it's, like, merged in to the hotel collector. It got merged in, like, 2 days ago.
So we can… we can clo- we'll close that issue. And then I think, mostly.
We'll probably just import some of the stuff that's on the no status backlog and re-evaluate it as we go.
**Dotan Horovits** 33:15 Okay, so the porting is pretty straightforward then, sounds good.
Okay, so just, I guess, we should figure out who's going to be our champions for Phase 2, if you say that it's in question mark.
And, Yeah, then I think we should be good to go for beginning of November, to start it, Salty's fresh.
Do you know if Nicolas is planning on carrying on getting involved now that he's finished it? I think so, yeah. So I hope that gave him an appetite to stay there.
**Adriel Perkins** 33:50 Yeah, I'm pretty sure he filled out the… no, he didn't. I'll message him.
But, yeah, he works for Jurassi at Olive Garden now.
**Dotan Horovits** 33:58 Oh, right, Olive Garden, so yeah, that'll probably be a good fit. By the way, Olive Garden is also a good link to Dash Zero, because they work together. They also adopted the Olygarden, so, Sounds like Dash Zero is, are eager to… because they also went for the branding of OpenTelemetry Native, or something like that, so, they should be… if we are looking for, for early adopters amongst vendors, looks like, from their adoption, also Percy's, they adopted, and others, I think this could be a good, ping. So actually, Ioannis, if you're connected and you want to lead that part, touching base… I know also folks in Dashdir, but if you have a good friend there, feel free to do that.
**Johannes Koch** 34:38 I will ask, he's also a hero. I will ask Raphael if he's interested, and can let you know if not, okay?
**Dotan Horovits** 34:46 Okay, if they want to put some, like, someone to, to create this, preferably, again, not a receiver, but natively emit it, that'd be, that'd be amazing, and of course.
**Johannes Koch** 34:58 What do you mean with emitted?
**Dotan Horovits** 35:02 Sorry, not emit, receive it, sorry. Making sure that they, they support it in the way that they, they present the CICD data, so, sorry.
**Johannes Koch** 35:11 Yeah, yeah, makes sense. So, so you mean something a little bit more natively, like templates or something like that, that people could directly use?
**Dotan Horovits** 35:17 Yeah, I guess, but let's… I don't know how they structure it, so I, you know.
**Johannes Koch** 35:22 I will…
**Dotan Horovits** 35:23 I'd actually open the discussion exactly to know what their native support is, and then see what's considered native on Dashir. But anyway, it's just thinking if you have the connections there.
**Johannes Koch** 35:34 We're asking and sounds like…
**Dotan Horovits** 35:35 They're early adopters, yeah, sounds good. So that's another thing that could be good to have another vendor for Phase 2 that can help.
**Johannes Koch** 35:44 We also have, Liz at Honeycomp. Maybe… So… Doton, do you know that? Anyway, I'll ping you.
**Dotan Horovits** 35:54 Okay.
Sounds good. So, Okay, I need to drop four.
**Johannes Koch** 35:59 another call.
**Dotan Horovits** 36:00 Yeah, yeah, we also need the… bye, Joanna, it's good to see you.
I think, largely, we also, anyway, I think we covered most of what we wanted to, so, Like, Adriel, do you have anything else on the agenda?
**Adriel Perkins** 36:15 I do not.
And.
**Dotan Horovits** 36:18 Mir, I see your question, sorry. Yeah, exactly. So, if you, if you know, Mir, if you know folks with Bitbucket, I'm happy to touch base with them as well. As you can see, it's opportunistic based on who we know, and who is willing to, to engage in conversation, because it's open source, you know, we don't pay anyone. So, do you have any connections with, Bitbucket, or any, I don't know, Bitbucket, Power engineer that can implement it, as a receiver or something?
**Mihir** 36:48 No, currently we also use Jenkins, and we are in the phase of migration to Argo CD, and for CI, we want to use Bitbucket pipelines.
So just getting started over here as well.
**Dotan Horovits** 37:04 I see.
Okay. But it's a good, if you do, while exploring that, if you do find someone who's, Who can help, creating… and do we have references? Since you're new, I'm telling you, we have references both for GitHub and GitLab receivers, auto collector receivers, so it should be easier now to implement, given the references we already have, so if there is someone was willing to undertake, that is familiar enough with Bitbucket, that can implement even as a receiver, even if not native.
But as an auto collector receiver, then, let me or Adriel know.
We can put you in the right direction, and, for helping with the implementation.
**Mihir** 37:46 Just got a shot.
**Dotan Horovits** 37:50 Cool. So I think, this is, this is pretty much, what we had for this day, but, great to see you, all. Thanks, Mir, for joining, and Adriel, so, So glad to see you again, man.
**Adriel Perkins** 38:03 Good to see you, too.
**Dotan Horovits** 38:03 Yeah, yeah, let's catch up offline and.
**Mihir** 38:06 And, carrying…
**Adriel Perkins** 38:08 For sure. Thanks, everyone. Have a good day.
