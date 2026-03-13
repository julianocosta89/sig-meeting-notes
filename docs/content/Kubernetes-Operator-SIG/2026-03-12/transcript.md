SIG: Kubernetes Operator SIG
Date: 2026-03-12
Duration: 29 minutes
Zoom Recording URL: https://zoom.us/rec/share/HTy3Ffb7oHkZmKCO_iC1B3tP-e0FpWE04eKjlOs2E7V3RYMquO5Ol-YC0t3kdOHS.tJuezV7B8XQqP_xF
============================================================

## Zoom Recording Transcript

**ploffay** 00:16 Hello, hi Jacob.
**jea** 00:17 Hey, Paul, how are you?
**ploffay** 00:19 Thank you, thanks. How about you?
**jea** 00:22 Doing well, not much going on.
Getting ready for KubeCon.
very excited to go, but my passport, is not expired yet, but it's, like, within the 3-month window that the EU requires, so I need to get it renewed.
Which is annoying. It's in, like, 2 weeks, so… We'll see what happens.
**ploffay** 00:52 Yeah, it's always… my parents were… my parents were supposed to go to Australia.
**jea** 00:58 Yeah.
**ploffay** 00:58 And my father's passport was as well, expiring, he was stressing out.
**jea** 01:04 Yeah.
**ploffay** 01:04 Then I called the embassy, because he doesn't speak English very well, he speaks German.
**jea** 01:09 Yeah.
**ploffay** 01:10 And then at the end, they were supposed to fly… on Friday, the week before, the… through Dubai, and the war started.
**jea** 01:20 Oh, my… ploffay 01:20 Actually, cool.
**jea** 01:22 Yeah, so did they not… did they end up not going?
**ploffay** 01:25 You know… jea 01:26 Oh, man. That's a bit of a bummer.
**ploffay** 01:29 Yeah, because… They were supposed to go the first day the war started, then the Dubai airport was closed, and then… They were offered some alternative flights.
Through a different city, but it was the Almost a week after, and then they wouldn't have enough time, you know, to do the stuff they wanted to do.
**jea** 01:52 Yeah, oh my god. Well, at least they didn't get stuck in Dubai, that would have been worse.
**ploffay** 01:56 Yeah. Yeah, yeah, that's completely, pretty bad.
**jea** 02:01 Yeah, that would have been bad. I mean, there have been a bunch of people that have just been fully stuck there, which does not sound fun.
**ploffay** 02:09 Yeah.
**jea** 02:10 That's a shame, though.
It's a long trip, too, to get to Australia from… I mean, from America is probably the same distance, right?
**ploffay** 02:21 It's like two 7-hours flights, or something like that.
**jea** 02:24 I think here it's a 24-hour flight to get there. Like, there's a… I think there's a direct flight that takes you there, and I think it's 24 hours.
**ploffay** 02:33 Shit. That's a long.
**jea** 02:35 I know.
**ploffay** 02:37 The longest I was going was to Alaska, to Anchorage.
**jea** 02:41 Yeah.
That's a long flight from where you are, too.
Hello, let's see if it's just us today. I don't know, who else will… Pop their head out.
**Mikołaj Świątek** 02:56 I'm completely out of it. My day today was, and yesterday was, like, a series of meetings and, like, high priority, fix, 6, 6, 6, 6, right, right, right, right, right, no, no, no, no, no, basically, and… jea 03:12 Yeah.
**Mikołaj Świątek** 03:12 I don't know, like, I marked some stuff we've discussed at SIG that I kind of wanted to discuss, but otherwise, I don't really.
**jea** 03:20 Yeah, no, I'm looking through, I think the release thing we should definitely do, I like that idea a lot.
Let me just do it. I'll prove it. I think Pavo already proved it.
**Mikołaj Świątek** 03:36 Yeah, I made it so that you can actually… well, I made it. I instructed an AI which is better at writing Bash than myself.
**jea** 03:45 Yeah.
**Mikołaj Świątek** 03:45 They're great at that. I love that about the uploading agents, that they're good at writing bash.
**jea** 03:51 I know, I hate writing Dash.
You know, this looks good to me. I think we should just go for it.
**Mikołaj Świątek** 03:59 Yeah. The other change I had is the… oh, I actually did not mark this one, so scutterbrains these past two days. I have a change which finally, finally changes practically all the integration tests to just use Vue and Beta 1, because… jea 04:18 Oh, right, yeah, I think I saw that.
**Mikołaj Świątek** 04:21 We have a bunch of, like, flaky integration tests right now, and my suspicion about them is that we've, like, merged the change, where we don't use, like, the… is the… is the, you know, is the operator-ready Go program anymore. Instead, we just use a, use the health check, because, like, the… whoever it was that did that change, noticed that our health check is really… just doesn't… our health endpoint didn't include checking whether the webhook server was ready.
**jea** 04:54 Yeah.
**Mikołaj Świątek** 04:55 twerk.
**jea** 04:58 Yeah, that'd be… Mikołaj Świątek 05:00 So we switched to that, and since then, the tests have become less, less stable, and I think the reason for that is that, for some reason, the conversion webhook isn't, like, doesn't work correctly with that.
**jea** 05:16 Yeah.
**Mikołaj Świątek** 05:17 So, I decided to fix this by just making the conversion webhook just not used anymore.
**jea** 05:24 I think that's fine. Certainly soon we should just deprecate it and remove it.
**Mikołaj Świątek** 05:29 Yeah, I wanna do that as well. I put.
**jea** 05:32 Paulo and I both approved. I think we, you want to just merge it?
**Mikołaj Świątek** 05:36 Yeah, I just did.
**jea** 05:37 Nice.
**Mikołaj Świątek** 05:37 This is, like, the upgrade test is still flaky, and it's still flaky for, like, the same reason.
I think, because it depends on the conversion webhook in the middle, in some, like, weird, strange way. Which, like… I don't know… I don't know if I want to try and debug why the conversion webhook is having problems, like, on the.
**jea** 06:00 Totally true.
**Mikołaj Świątek** 06:01 I kind of don't want to.
**jea** 06:03 I think I'd rather we just get rid of it in the next coming months.
**Mikołaj Świątek** 06:07 kind of what I'd rather do as well. Okay, I'm also merging the automated release thing.
**jea** 06:12 Yeah, yeah.
**Mikołaj Świątek** 06:12 Because I… jea 06:13 We now have this… the last one is the weight class configuration.
**Mikołaj Świątek** 06:17 Yeah, yeah, so this is, like, this is also from me, and it's a… jea 06:24 This is a doozy. I read through this, and… I mean, my initial comment for this person was, like, we just shouldn't do this.
**Mikołaj Świątek** 06:32 I'm kind of… I feel bad, because I told… I told them to do something else originally in an issue.
Because… Basically, they want more customization for the… for the least weighted strategy.
**jea** 06:47 Yeah.
**Mikołaj Świątek** 06:48 And the reason they want it is because they're doing something that's an anti-pattern. Like, they have these massive cube state metrics targets, which this is, like, a problem we all know and love.
**jea** 06:58 Yeah.
**Mikołaj Świątek** 06:59 To that problem is to not have those targets.
essentially.
**jea** 07:05 The solution is to shard it, right?
**Mikołaj Świątek** 07:07 Yeah, the solution is to shard it, either just shard it as a stateful set manually, or just shard it as a daemon set, and then you don't have that kind of problem.
but I want to… I guess what I'm looking for is, like, some… Guidance on how we want to make these configurable?
My view of this in general is that least weighted is not a great thing, and we shouldn't, like, encourage people to use it.
**For… jea** 07:37 Yeah, I mean, I kind of agree with that.
**Mikołaj Świątek** 07:38 reasons.
**jea** 07:39 I think the idea of doing this, like, patch, like, hint strategy.
and then we, like, look at that to change the weight is probably fine, but I do think it's kind of hacky.
It's definitely the cleanest way to do this type of thing.
**Mikołaj Świątek** 07:55 I really don't like the idea of setting numeric weights for anything in this strategy.
**jea** 08:01 I mean, it definitely will result in some very odd… it could result in some weird behavior, right?
it can result in some pretty weird behavior. I think what I would rather is we create a new strategy called, like.
annotation-weighted strategy or something, where you can use this, but even… but that also feels kind of hacky. I don't know, all of these feel wrong.
You know, it feels like we're designing around this Thing that somebody else has already solved, right?
**Mikołaj Świątek** 08:36 I don't know, like, there used to be… there used to be a, like, a… something that they wanted to do as well was to actually do it dynamically, and just look at the collector metrics to assess how heavy the targets were, because everybody's solving… jea 08:50 like… Mikołaj Świątek 08:51 like, the problem they are solving, the problem they are solving, and I'm just saying it because Pablo looks confused since the start of this conversation. The problem they are solving is that they want to be able to control, they want to be able to avoid situations where they get, like, a lot of heavy Prometheus targets in a single collector, because, like, Prometheus targets are not born equally, right? They can be very small, or they can be very, very big. Them being big is an anti-pattern, but people still do it from one region or another.
**jea** 09:25 I mean, sometimes it's unavoidable for some services, right? Like, you… there's not much… but you also, you can't shard a single target, right?
**Mikołaj Świątek** 09:34 Yeah.
**jea** 09:35 Like, that, to me, like, it's the… the anti-pattern is that you're trying to just make it… like, you're trying to really hack it so you can have one collector… like, I don't know. To me, the way to solve this is you have a dedicated pool for just heavy targets, and then you just change the label selector on the service monitor.
**Mikołaj Świątek** 09:55 That is something… that is also a, valid… answer those questions for me, because what we're trying to do here is, basically, we're trying to kind of add a small feature to the least weighted strategy, so that you can set the weight somehow, and then the least weighted strategy actually kind of operates on numeric weights, which it doesn't right now. Right now, the only thing it does is it, like, tries to spread things, you know, the same number of targets on each collector.
**jea** 10:24 Yo.
**Mikołaj Świątek** 10:25 and… I kind of agree that if you have a problem where some of your targets are very heavy, then the answer to that problem should be make a separate collector.
Specifically for those, and then you can control what you want. Like, I don't know if, like, we want this to be a feature inside the target allocator, basically.
**jea** 10:50 I… yeah, I mean, I understand the goal, but… I worry that it adds in, like, a ton of logic.
Into something that right now is purposefully pretty dumb.
**Mikołaj Świątek** 11:02 Yes. I like the fact that it's dumb, and even though it's dumb, it still has tons of bugs in it, so… jea 11:09 I mean, I don't think there's tons of bugs in the target allocator. I think it's a pretty stable piece of software at this point.
**Mikołaj Świątek** 11:15 I… I deeply… something I deeply dislike about the target allocator is the fact that we don't actually have a good way of testing exhaustively whether the stuff we do with the labels inside of it is correct, basically.
It's, like, the question of, here's a production cluster with metrics coming from all sorts of places.
Here's a target allocator, here's a set of collectors, and here there's a remote where all of this lands.
And does this whole thing work correctly? Is that just not something that we verify, or that we are, like, really able to verify?
**jea** 11:57 I mean, we don't have, like… yeah, we don't have, like, unit or integration tests for that, but anecdotally, like, I used… Target allocator and, like, a… You know, 200-node cluster for a bunch of charters.
**Mikołaj Świątek** 12:08 Yeah, I used it in a freaking, like, 3,000 mil cluster, and it was fine. But what I mean is more that, for example, we come in, there's a request for a feature where do… so we can do target relabeling inside a target allocator.
And that is, like, would solve a bunch of really awkward and kind of hacky solutions inside Target Allocator that already exist.
But how do you test that whatever you did is correct?
**jea** 12:42 You mean if we were to keep the targets?
**Mikołaj Świątek** 12:45 What I mean is that right now, what happens is that You take a target.
you maybe do some relabeling on it, but you only do relabeling to figure out if you're keeping it or not. Right now, you also… you'd hash the relabeled targets, because otherwise you run into, like, bugs if the user rewrote the address or something, you know?
But… and essentially, you just keep the target as is, the labels are kept as is, and you send that to the collector, and then the collector does relabeling on those target labels.
**jea** 13:20 Yeah. Right?
**Mikołaj Świątek** 13:22 And this would all be solved, and it would probably be way more efficient as well, because you send those targets down, they're very big, a lot of the time, there's a lot of them.
**jea** 13:30 Yup.
**Mikołaj Świątek** 13:31 this would be solved if you instead did the relabeling inside the target allocator, and just sent the already relabeled stuff down, because we're already doing the work, so it's not any more work. It's just a question of, if you do that, does it break anything? It probably does, but we don't really have, like, a good way of verifying, you know.
**jea** 13:50 Yeah, I mean, we could make… Mikołaj Świątek 13:51 doesn't, right?
**jea** 13:52 We could make a harness. I think the benefit of the AI stuff is that making these types of harnesses is a lot easier than it was previously. Like, we could spin up, a pretty exhaustive suite to verify that this does the thing that we want it to.
**Mikołaj Świątek** 14:11 I… I mean, if you think you can, like, instruct an AI agent to build that for you, I would be very interested in seeing it.
**jea** 14:21 I can show you… I did something similar for, like, some company stuff that I did for, test case suite recently. I can just show you what I did there.
**Mikołaj Świątek** 14:33 Maybe that already exists somewhere, and we just… or at least, like, because the main thing… jea 14:38 It's been added, honestly.
I wrote this, like, conformance suite… Where… I told you about, like, the policy stuff I'm doing already, right? I showed you that.
So in here, I just… this is, like, a very easy benchmarking, benchmarking suite, where there's some input, like, you know, JSON payload, like, OTL JSON payload.
Then there's some policy that you're running.
And then there's some expected output for what that payload should look like.
Right? Ignore… I get rid of all the default fields, which are in this massive payload. I should probably get rid of that, but… this was, like, pretty easy to spin up, and then I just wrote… Like, 200 different test cases to go through, and then went through and checked each of them.
That's right.
**Mikołaj Świątek** 15:35 So, like, for me, the main issue is basically that.
**jea** 15:40 Stop.
**Mikołaj Świątek** 15:40 Actually, to actually… Show you.
to, like, actually test this, you kind of need to put it through the whole system, right? It needs to be, like, a proper integration test, and so it starts by having some applications which generate metrics.
**jea** 15:58 Yup.
**Mikołaj Świątek** 15:58 and you need them to generate, like… Weird ones. A variety of metrics, maybe that exists? I don't, like, I know that there exist, like, stress testing, tools, like Avalanche, which generate a lot of metrics, but those.
**jea** 16:13 Those are folks.
**Mikołaj Świątek** 16:13 on generating lots of metrics, not on generating a variety of metrics. So you need those. Then you need the target allocator collector layer. Those need to export somewhere, let's say Prometheus, to make things simpler, right?
**jea** 16:27 Yeah.
**Mikołaj Świątek** 16:27 have to verify in Prometheus that what you got is what you expected, is what you expected to get.
**jea** 16:37 Yeah.
**Mikołaj Świątek** 16:37 Like, a lot of stuff.
This is actually a good topic of conversation. I don't know, I'm not gonna be there because I'm not… I arrive on Monday.
**jea** 16:46 But… Sorry, one sec.
**Mikołaj Świątek** 16:48 You know?
**jea** 16:49 I arrived there on Monday, but I think that they're doing some sort of, like, Prometheus Hotel Summit.
Did you see this already? Yeah, here it is. It's at the Maintainer Summit, but I'm not going to be there, because that's.
**Mikołaj Świątek** 17:03 I am, I am there, so I can go.
**jea** 17:06 Yeah, I would just ask, like, Arthur or any of the Prometheus folks if this is, like, a suite that they already have that we could sort of Crib off of, or something.
**Mikołaj Świątek** 17:17 It would be really nice.
**jea** 17:19 It feels like… Mikołaj Świątek 17:20 shipping.
**jea** 17:20 that they built for this, like, OTEL Prometheus, conversion stuff.
Also, while I have you, I just want to review this PR with you. The… This is a bad scare.
**Mikołaj Świątek** 17:33 So, if it, if it builds, then it's probably correct.
Right?
**jea** 17:41 Yeah, I mean, most of this is just a renaming, like, it's pretty minor.
**Mikołaj Świątek** 17:45 Yeah.
I didn't… I wasn't… I wasn't, like, I wasn't reviewing it because I wanted it to, like… because this is by Antoine?
**jea** 17:56 Should this be a cho- should we have him make a changelog for this?
**Mikołaj Świątek** 18:00 No, I don't think so.
**jea** 18:03 you think? I thought I saw one. Yeah, he wrote.
**Mikołaj Świątek** 18:05 Maybe here, maybe the braking change, because it's, like, a module move.
**jea** 18:09 It is a breaking change, but, What is the… I hate the… sometimes this thing is so.
**Mikołaj Świątek** 18:15 Yeah, I know, it's like… jea 18:17 What is failing here?
**Mikołaj Świątek** 18:18 No, no, nothing is failing here, it's just that the end-to-end test report, it goes into the wrong section.
in GitHub.
And I don't know why that is.
**jea** 18:29 I don't know, I'm just gonna merge it.
**Mikołaj Świątek** 18:31 That's fine.
**jea** 18:33 Well, anyway, Yeah, I would just go to the Prometheus Summit and see what they have to say.
**Mikołaj Świątek** 18:48 Yeah, because that's, like, the main, main problem for me. Whenever I make a change in target allocator, I'm like, okay, my unit test passed, my integration test passed, but I'm never, like, confident that this is actually, like, end-to-end works correctly. We have an integration test that does this, but it does it in, like, a very limited scope.
Yeah. It's like, if you ask me, oh, but if somebody rewrites… you know, we… and I said we had bugs. We had a bunch of bugs, for example, for, like, people doing slightly weird stuff with, through labeling. Like, for example, rewriting the address.
label.
Which I would never think that you would do at all, but you can, and if you do.
**jea** 19:30 Yeah, people do a lot of crazy shit.
**Mikołaj Świątek** 19:31 Yeah, yeah, and it would actually break… break target allocator, it would, like, break the hashing. Yeah.
So… I am now a little bit paranoid about that stuff.
**jea** 19:45 Well, either way, I don't think we have anything else. Is there anything else you want to go over?
**Mikołaj Świątek** 19:50 I'm good.
**jea** 19:52 Okay.
**Yeah, I think, I mean, the next one we have is at KubeCon, so… Mikołaj Świątek** 20:01 I've heard something that there's not gonna be, like, this big observatory booth, so… We might have to arrange in some other.
**jea** 20:11 Yeah, we're not gonna have the observatory. I don't think Splunk is sponsoring it this year or something.
**Mikołaj Świątek** 20:16 Yeah, and there's, like, some… some weird thing… jea 20:20 I don't know, we'll have to just figure it out. I'm sure we'll have, like, a spot that we post up at, so… I'm not concerned.
We'll figure it out.
Okay, I'm gonna… I'm gonna hit it.
**Mikołaj Świątek** 20:33 Actually, I have a question before you go.
**jea** 20:35 Yes.
**Mikołaj Świątek** 20:37 What do you think is the motivation of the person submitting all these limp… limp PRs?
**jea** 20:44 Oh my god, I'm so glad you asked, because I have no idea. One of my friends thought it was an open claw bot.
**Mikołaj Świątek** 20:51 It looks like a person from the GitHub profile.
**jea** 20:53 Yeah, but it could just be their GitHub, which is run by OpenClaw.
**Mikołaj Świątek** 20:59 Mmm, that is possible.
**jea** 21:01 Because, okay, I looked at this because I was really… I had the same thought. His name was, like, Morrell, right? And Morrell.
And I looked at his GitHub.
**Mikołaj Świątek** 21:16 Strangely, strangely, the contributions are private.
**jea** 21:20 Odd to me.
And so I tried to find out, like, where this guy worked.
And I'm pretty sure it's this guy.
you know, just kind of like a bog-standard developer. Like, not much… some cloud provider, I guess?
I don't know.
**Mikołaj Świątek** 21:46 I mean, if it's a… if it's someone's open claw, I don't mind.
**jea** 21:51 No, I mean, these have been… all the PRs have been small and fine, like, I'm not… Mikołaj Świątek 21:55 Yeah, and they're not, like, actually changing anything. I did, like… there's one of them which I had to, like, read a little bit more carefully, because it was kind of.
**jea** 22:08 One of the things that I wanted us to watch out for is the, Did you read this, blog post, Open Klein… Mikołaj Świątek 22:17 Was it… was it the one where the clawbot published some blog post accusing someone of being biased?
**jea** 22:24 No, this is, an expansion of that, so… not that.
No, not that, sorry, I changed around my Slack recently.
So just read that when you get a chance. I think you'll find it very interesting.
**Mikołaj Świątek** 22:41 One argument against this being, like, an open claw is that I think if this was an actual, like, agent, all the PR descriptions would have been way nicer than they are.
And they are not very nice, they're just, like, barely edited. This is, like, a very human behavior, to, like, not want to… not want to write anything in those.
**jea** 23:05 Yeah, I… I don't know.
**If it's a human, then this guy works fast. Like… Mikołaj Świątek** 23:11 I mean, maybe… maybe he's probably using… I wouldn't be surprised if he's using, like, AI to actually, like, go through them, and he has, like, a bunch of agents running in parallel, creating these, like… but he's submitting the PRs manually, I think. I don't think, like, it's, like.
**jea** 23:25 Maybe that's true. Maybe that's true.
**Mikołaj Świątek** 23:27 That's… I would definitely believe.
**jea** 23:29 So the thing that I sent you, the way that this person got this injection done is that they made a bunch of PRs, and then they, like, did a fork, and they changed one of the PRs to use their fork.
And it became, like, very… then that was, like, the injection failure. And we definitely have a repo That is gonna be, like, is one of the ones that is susceptible to this type of, Security pattern?
And so I want to… during all these PR reviews, I've tried to be very careful about it, because the way that this guy got in was by, typo-squatting GitHub Actions slash Klein, but it was spelled G-L-T, not G-I-T.
And so that's how we got the PR approved, is that nobody noticed the change.
**Mikołaj Świątek** 24:17 Yeah, I would… I would be a much more… I generally scrutinize any change that touches any GoMod or anything in, like.github much more than anything else, but he was, like, just changing… making changes to the Go code, which… and not to any tests at all, so… jea 24:37 Well, so there was one PR that he did which had, a bunch of GoMod changes. Or Go, Go Sum changes.
And so I was, like, really looking at those very carefully.
**Mikołaj Świątek** 24:52 I think that was the one which, replaced something with something?
**jea** 25:01 So it was, like, this GoMod change that I was, I was, like, looking out for.
**Mikołaj Świątek** 25:05 Yeah, but it was just, like, a change to go from… jea 25:10 Yeah, but you could imagine that, like, if this guy wrote in over here his own version of, like, the hotel HTTP thing.
Right.
**Mikołaj Świątek** 25:20 Yeah.
**jea** 25:20 It'd be called.
**Mikołaj Świątek** 25:21 This is a bit hard… this is a bit harder to do in Golang, because package names are actually sequential? Domain names.
**jea** 25:29 Yeah.
**Mikołaj Świątek** 25:29 Yeah.
**jea** 25:31 You could imagine if you replaced, like, an I right here with an L.
Right. If you did the… if you did, like… something like.
**Mikołaj Świątek** 25:42 Well, well, you know, we have this scanner running on every PR, I would expect the scanner to… to… jea 25:51 I don't know. You never know.
**Mikołaj Świątek** 25:53 Like, it's a valid thing to be worried about, and I suppose this is, like, just more, I suppose confirmation that we should, be… we should have more stuff scanning for, like, the dangerous changes.
**jea** 26:11 Yeah, and it should not be an AI scanner. That was the… that was the problem that… It was basically an AI reviewed it, and then it was like, oh yeah, whatever, looks good.
**Mikołaj Świątek** 26:21 I'm fortunate.
**jea** 26:22 It ran the, the bad code, like, on the, on the, like, the host repo with the secrets, and then it exposed the secrets via the bad code. It's a really interesting post, you should read it.
**Mikołaj Świątek** 26:39 Yeah.
Oh, I actually have a request for you, because this bothers me. It's stupid, but it bothers me.
**jea** 26:47 Yup.
**Mikołaj Świątek** 26:47 this.
**jea** 26:54 Oh my god, okay, okay, I'll do something about it.
**Mikołaj Świątek** 26:58 It's like, almost all of it passes. It seems like.
**jea** 27:01 I know, they've been… they do a pretty good job of not breaking the API. It's probably just a few new methods.
You already assigned it to me, or it's somehow… no, Dependabot assigned me.
I don't know how.
I'll do something about this.
**Mikołaj Świątek** 27:20 I know, no, no, I know why, because I assigned you to one of the previous.
**jea** 27:25 Yeah.
**Mikołaj Świątek** 27:25 of this, and Dependabot… wow, Dependabot is smarter than I thought. I didn't know it could do that.
**jea** 27:32 Yeah, it remembered.
They're learning.
Yeah, they're learning. All right, Jacob. Okay.
**Mikołaj Świątek** 27:40 I'm not gonna hold you up for now.
**jea** 27:41 No, no, all good.
Yeah, I'll see what Kupan.
Anything you want from the States?
**Mikołaj Świątek** 27:47 What kind of question is that? What's, like, Wisconsin brick cheese?
**jea** 27:52 Sure, I'll bring you some cheese. I mean, it's not like they don't have cheese in Amsterdam, but… Mikołaj Świątek 27:57 They don't have Wisconsin brick cheese, okay? I like making Detroit-style pizza.
buying similar cheese around in Europe is surprisingly difficult.
**jea** 28:06 Yeah, I believe that.
**Mikołaj Świątek** 28:07 I've suffered. That's, like, half-joke, but if you actually bring me Wisconsin brick cheese, I'm not, you know, I'm gonna take it.
**jea** 28:14 Yeah.
Okay, I'll try and smuggle that for you.
**Mikołaj Świątek** 28:20 You… you asked, you shouldn't have asked if you didn't.
**jea** 28:23 No, that's fair, that's fair. What were you?
**Mikołaj Świątek** 28:24 expecting that I would ask for, like, an American flag or something?
**jea** 28:28 No, I don't know, some American, candy, or like, people ask… I've… not me personally, but I know people that have asked, somebody to buy them, like, an Apple device because the tax, is lower here.
For buying devices.
**Mikołaj Świątek** 28:45 I have all the devices I need for a very long time.
**jea** 28:49 Well, you're all… Mikołaj Świątek 28:49 I have, I have, I have an excessive… I have an excess of devices.
**jea** 28:54 Yeah.
Well, no worries, then.
Okay, I'll see you later.
**Mikołaj Świątek** 29:00 Right.
