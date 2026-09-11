SIG: Java SIG
Date: 2026-09-10
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Trask Stalnaker (Microsoft Corporation)** 01:31 Can you all hear me?
This headset is…
**John Watson** 01:39 Yes.
**Trask Stalnaker (Microsoft Corporation)** 01:39 beeping at me. It's not gonna stop beeping at me.
Okay.
**Jason Plumb** 01:45 Low battery.
Trask, can you hear us?
Nope.
**Trask Stalnaker (Microsoft Corporation)** 02:20 Okay, can you hear me?
**Jason Plumb** 02:21 Mic check, 1, 2, 1, 2.
**Trask Stalnaker (Microsoft Corporation)** 02:24 Alright.
**Jason Plumb** 02:26 Sibilance.
**Trask Stalnaker (Microsoft Corporation)** 02:27 Stupid headset.
Hey, off.
I feel so narrow, looking over myself in the, the…
**Jason Plumb** 02:50 That's it.
**Trask Stalnaker (Microsoft Corporation)** 02:51 Yeah.
**Jason Plumb** 02:56 He lost 20 pounds, just like that.
**Trask Stalnaker (Microsoft Corporation)** 03:14 Alright, well, why don't we kick it off, Jack, with you, with the, I assume, release tomorrow?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 03:22 Yeah, there is a release tomorrow. Let's see, the… Trying to think if there's anything… that I want to call out related to the release. I'm planning on merging a PR that's about the histogram performance improvements under contention. I left a comment on that, saying, like, hey, you know, if… unless somebody is planning on dissenting or actually giving it a review, I'm okay giving it more time. If somebody is intending on giving a review, I'll merge it before tomorrow's release. So, you know, speak now or forever.
That type of thing.
And then there is a… there's another bug that comes to mind that somebody opened up recently about a deadlock issue with our completable result code. I don't know if you saw this, John, there's sort of a…
**John Watson** 04:16 Yeah, John Bly… John Bly opened that up, and it sounded, like, more like it wasn't something that was actually observed in the wild, but it was just from code analysis.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 04:27 Yeah, because I was imagining, like, I don't think that our deadlock, or our completable result code usage, actually uses, you know, the result codes in that way, where they resolve each other, and they can get deadlocked. But, like, maybe if somebody else picked that up at the API level, and, you know, we're using it for their own purposes, you could run into it in a real way.
Anyways, it seems like… it was like a reasonable complaint, and, you know, as things… as things go today, as soon as there's an issue open, a couple of people pointed at their LLMs at it and were in a race for who could get the contribution first, and so I'm going to try to get one of those contributions in before the release tomorrow.
**John Watson** 05:16 I don't… I don't feel like this is super urgent. Like, as I said, well, I logged it based on analysis, not based on actual Like, an actual event that has occurred or been observed, so…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 05:31 Did you talk to him about that, or I guess, like, I guess.
**John Watson** 05:34 No, I just read… I just read through… read through his report, and he literally said it was just done by analysis.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 05:41 That's… that's helpful context. Okay, so, And I am not going to be in a rush to merge that either, so thank you.
And if anybody else has any PRs that you think need to get in before the release tomorrow, let me know. Those were the things that came to mind for me. I've been playing catch-up this week and burning down the list of open PRs, and so a lot of stuff has been merged.
And everything that hasn't been merged, I'm, like, I'm aware of, and nothing else seemed urgent to me.
**Trask Stalnaker (Microsoft Corporation)** 06:18 Yeah, I saw you were doing some cleanup on the, old… PRs, too.
That's pretty nice.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 06:25 Yeah, I guess I should say something about that. So, you know, previously, I guess historically, I… we have been okay with letting draft PRs be open for long periods of time, sometimes, like, indefinitely, to prove out ideas. And, just with the uptick in PR numbers due to LLMs.
I'm not in favor of that anymore. You know, I think I want the set of PRs to be… the set of open PRs to be the thing… the set of things that we think reasonably could be merged in, like, say, a 1-2 month time horizon. And if that amount of time passes, or if things go stale, I'm just going to be more inclined to close them.
And, you know, we can re-pick that up later, when there is more interest. And the interest could be on the contributor's side, maybe we left a comment and they let it go stale, or on our side. Like, if I or the other maintainers and approvers haven't looked at it for a couple of months.
It's… it's not that important.
And so, you know, I think you as a contributor need to create more of a sense of urgency, or do, like, consensus building to explain why your contribution is important. So… That's kind of where I'm thinking on that. I'm happy to be wrong, I'm happy to update my stance, but like, you know, there's undoubtedly a large uptick in PR counts, so I think we need to adjust our behavior a little bit accordingly.
**Trask Stalnaker (Microsoft Corporation)** 07:57 Makes sense. The… Sometimes we have, like, prototypes for spec issues.
that… Take a long time.
But… if I… if… If the spec issue goes stale also, then, like, you know, like you said, somebody needs to drive… drive that at the spec, and… Then, you know, we can deal with that.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 08:28 Right, there was a PR I closed that was just that, recently. It was about having a fallback OTLP endpoint, so, like, you know, you can configure two endpoints, and if your first one fails, go to this one. And, the contributor asked that I leave the PR open because they were going to go push it at the spec level.
And the spec effort sort of stalled out, but, you know.
I initially said yes to that, like, sure, I'll keep that open while you push this at the spec level, but I'm not even sure that was the right decision, because you don't need to have a PR open in order to have a conversation at the spec. You can have a branch, and you can point to the comparison between your branch and the main branch.
Like, that's a permalink that you can send on your spec PR, so people can see, kind of, what the code change looks like.
Having actually an open PR that's a draft, indefinite, I'm not sure what that does. It provides a place where you can have comments on it.
that, you know, a compare permalink doesn't have persistent comments, so that's something, but I don't know.
**Trask Stalnaker (Microsoft Corporation)** 09:41 I like the… prototype PR concept.
I use that a lot in semantic conventions.
But I do think it needs to be an… an active… Moving forwards.
And if not, yeah, it can always be resurrected.
**Jason Plumb** 10:11 So, Jack, are you enforcing any sort of timeline there, and if so, what sort of timeline are you thinking?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 10:17 That's the troubling… that's the troublesome part with, is that it really quickly becomes subjective, and so, you know, one alternative that allows you to have sort of a prototype PR is to have a PR against your own main branch.
If main… if you keep your forks main up-to-date, then you can open a PR that just, like, is a persistent place to leave commentary about this code change.
And, you know, it doesn't clutter up the PR list of the main repository either, so then you can keep open your draft PR as long as you want, and I don't have to, you know, come up with subjective measures for when progress has halted or stalled out.
**Jason Plumb** 10:59 Is that worth noting and contributing or anything?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 11:02 You know, I'm an evolving conversation, so, you know, I think if folks don't…
**Trask Stalnaker (Microsoft Corporation)** 11:09 I went the right pattern.
**Jason Plumb** 11:11 Yeah.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 11:11 If folks don't revolt against me, I'd be happy to codify this.
**Jason Plumb** 11:16 I like that pattern of, like, doing PRs on your fork, but then I forget about them. I'm like, God, where was that again? And then I'm like, oh yeah, it's on my fork.
**Trask Stalnaker (Microsoft Corporation)** 11:24 Jack.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 11:25 Yeah, I mean, should the main repository be as sort of a place for you to jot down notes that are personal to you? I think probably not.
**Jason Plumb** 11:36 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 11:37 We do, in the specification repo.
We do make some distinction about prototype PRs that have some mild blessing of the maintainers.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 11:55 Yeah, the place where… so, you know, if you are trying to get a feature from in development.
to stable, like, you know, the question is, what counts as a prototype? We have a three-prototype requirement. And in some languages, they're pretty strict, and they say, like, hey, we're not going to land anything until it's stable in the spec. And so, the furthest that they can get in that language is, like, a prototype branch.
I think in Java, we have really good facilities for this, for actually landing prototype code.
Because we have, sort of, segregated out experimental and incubating features, and we can have them land and published in a way that the Go ecosystem has, like, has not, you know, either because of structural issues with the language or their own SIG sort of deliberations, they have not gone in that direction.
But the one place, I think, where, you know, that still has merit Trask is, like, if you're trying to land something for the first time in the spec, so it's not trying to get it from development to stable, but you're trying to say, like, hey, this is, I'm trying to land an in-development feature itself, and this is the first and only prototype of it.
In that case, I think, a draft PR.
With the blessing of the maintainers is still a useful signal, but it's pretty narrow.
**Trask Stalnaker (Microsoft Corporation)** 13:17 One thing as far as, making it, as far as, like, expiring things, I haven't… It's been kind of on my mind to do for the dashboard, is to integrate that into the dashboard, where But that would be… I was thinking of, like, if it's been waiting on author for, you know, 180 days, then, you know.
Or, you know, something smaller. We would… we could auto-close those.
But that wouldn't necessarily address… If it was… waiting on spec. I'm not sure what the dashboard would do with that.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 14:07 The waiting on spec, because this, you know, the PR is a sort of supporting artifact for a spec proposal, is sort of a… A niche case.
Doesn't happen very often.
But it's… yeah, I don't know quite how to detect it and quite how to handle it.
**Trask Stalnaker (Microsoft Corporation)** 14:29 Well, I support, I support, Pruning.
Things.
It's hard. I know it's hard closing things,
**Jason Plumb** 14:38 So, instrumentation definitely has the needs author feedback and has an auto-close mechanism, and we cribbed from that for Android as well.
If you just use the label, you'll see a bunch of closed ones.
And if you just go to the first one, you'll see how it was auto-closed.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 15:00 What do you all think about So this is an interesting category. It needs author feedback. The maintainers and approvers have given some feedback to the author, and they let it go stale. Great. Some period of time passes, and you auto-close it. But I think there's, like, a… like, LLMs have enabled this new kind of category, which is, like.
somebody opened a PR, and And it's just not a winner. Like, it's not something that even garners the attention of approvers or maintainers.
Like, should I, as a maintainer or approver, feel obligated, when there's, like, 50-plus PRs open on any given day, to give some sort of feedback to every single one of them? Or is the fact that, like, nobody has looked at something in two months a signal in itself?
**Jason Plumb** 15:51 I mean, it seems like the volume is the problem, right? Like, realistically.
I mean, like, ideologically, I think that maintainers should respond to every PR, but it's hard given the volume and the fact that so many of them are not even human-created anymore, right?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 16:08 Yeah, if I knew a human was on the other end, I would always give them constructive feedback, and I'd always try to, like, give them an answer. But that's not the case anymore.
**Jason Plumb** 16:15 Yeah.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 16:16 People are farming reputation, and, like, I'm arguing with LLMs, I'm arguing with meat proxies.
**Jason Plumb** 16:23 So, one of the things we did to help with this in Android is to… we have a label that we can put on stuff just to indicate that it looks like it's just… Kind of, like, robo-spew and come back to it later.
When time allows, which it never does. So, at least the label helps to quickly identify some of these, but you still have to do something, right?
**Trask Stalnaker (Microsoft Corporation)** 16:44 So the, the spec repo, I mean, it's… that has definitely been the way that's worked forever, of if nobody's paying attention, like, if nobody responds to it, that's a very good indication there's just not interest to move it forward.
And the spec repo has… a, timeout, stale.
For PRs, where basically… and I know some authors get annoyed by that, because, like, it goes stale, because nobody's paying attention to it, because nobody's really… Feel strongly that that needs to go in, and so that's its own… Feedback mechanism.
**Jason Plumb** 17:34 And then the people… but then the stakeholders for a given one can, like, just, you know, nudge it. Like, nope, not stale, still interested, and… You know, that drags on and on and on, and eventually stuff happens. Like, that's kind of the way that works, right?
**Trask Stalnaker (Microsoft Corporation)** 17:50 Jack, what kind of things are you getting… Because I would say most of the stuff that we're getting in the instrumentation repo Are things that are… Worth landing?
But they tend to be more about, like.
features and things, versus maybe in the SDK, people are… Kind of a little bit more… like, I don't know, what kind of things are you seeing there that aren't worth landing?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 18:26 I see bad attempts at landing good features sometimes. Like, there's this one that comes to mind recently about somebody trying to… add a timeout feature to Periodic Metric Reader, that, like, dictates the, the, the time requirement for, for each, each request in a batch, because now there's, like, you can break out, you can break up, export requests into batches. There's, like, max batch size. And, you know, like.
you don't know this until you get further along, but, like, you know, at this point, I've spent much more time trying to guide this PR in than had I just done it myself.
And, and I'm getting very, like, the other signals are, like, they're, like, similar types of things, where it's, like, somebody opens an issue for something, and then there's a race where, like, 3 people point their LLMs at it, and try to open, like, a fix for it, and, like, all the fixes are sort of bad.
like, they're not terribly bad, because the LLMs are very capable, but, like, you know, it's clear that the person you know, maybe didn't experience the problem themselves, maybe isn't a Java developer, and never, like, looked over what their LLM, like, put out.
And so, it just ends up being sort of, like, a waste of time to guide their LLM to land something, versus, you know, if that same thing would have been driven by somebody That experienced the problem themselves, that was a Java developer, and, you know, actually filtered the results of their LLM.
**Trask Stalnaker (Microsoft Corporation)** 20:10 BRUNO, hey!
**BRUNO Baptista** 20:12 Hey, good morning, afternoon.
So, yeah, I created a tool request for the periodic meter reader timeout, but I never got any feedback.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 20:25 I'm not talking about your PR, by the way.
**BRUNO Baptista** 20:28 Oh, okay.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 20:29 No, no, no, I'll send a link to this one. This was a different one.
Yeah, I looked…
**John Watson** 20:35 Right, right, fine.
**Trask Stalnaker (Microsoft Corporation)** 20:36 I'm like, wait, wait!
**John Watson** 20:38 No one's looked at BRUNO's yet, that is true, but… Jack, I looked at the one that you were commenting on this morning, and I'm like, whew, Jack's doing the Lord's work, but… Perhaps it is not the Lord's work.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 20:52 Yeah, I'm not sure it's, like, it's doing anyone good to have a, I don't know, this sort of…
**John Watson** 20:58 I agree.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 20:58 with somebody who's a front for an LLM.
**John Watson** 21:02 Well, and that person also… I don't know whether it's the LLM or the actual user, but they are very, very aggressive at, demanding feedback.
**Jason Plumb** 21:13 That's a smell, that's a smell, I think. That's like a contributor smell.
**Trask Stalnaker (Microsoft Corporation)** 21:20 So, Jack, you said something interesting, which is, I mean, the, People who have experienced the problem themselves,
**Jack Berg (Raintank, Inc. – Grafana Labs)** 21:31 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 21:32 Because that, yeah, like… for… I… That's my ideal world.
for this would be for issues, like, I don't want… I really don't want people… to… it's not… like you said, it's just not helpful for people to come into the issue list and find something and send a PR.
For it. These days.
Unfortunately.
So I've actually started assigning myself to issues that I open, just to kind of avoid that. But, for people who do… I love when users have problems, and they point their LLM at the problem, and send a PR You know, because they have, you know, they can… Validate that it fixes their issue.
So, yeah, I'm wondering if there's some kind of guidance That we could make in our repos about… about that.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 22:51 It makes me not want to open issues anymore.
like… I'm going to detect the problem, and I'm going to, like, you know, say why it's a problem and identify the scope of, like, what the solution should be. Like, why would I want somebody else to come in and give me their haphazard solution to it?
Versus just doing it myself. It's like, the times where I think issues are still useful is, like, when I'm trying to seek consensus from other maintainers, and I think that's, like, a loss, that it's kind of going in that direction, that I'm feeling this inclination to not make issues about problems that I've identified. But that's what I feel.
**Trask Stalnaker (Microsoft Corporation)** 23:30 So what work… what I found works well is, and I've been doing lately, because I have been… there's just been too many, sort of, parallel things going on with the 3-0, changes.
That I need to defer things, But I've been assigning it to myself.
And people… at least in this repo, people have mostly asked, like, hey, can you assign this to me? Something like that.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 24:01 Yeah, for some reason, people do key off of that as a signal, like.
Is it assigned to them or not?
Sometimes, not always, but… Yeah.
Maybe I should try that.
**John Watson** 24:16 I wonder if there's some way we could also have… an automation… When we get a contributor who's not a member of the community.
To put some sort of shibboleth that they have to respond to, to show that they're an actual person doing some work that they care about, rather than just a bot.
**Jason Plumb** 24:43 That's an interesting idea.
**BRUNO Baptista** 24:48 Well, it's actually very hard to understand if the person is a bot or not.
**John Watson** 24:53 No, I know, that's why we need to come up with a shibboleth that will be… that a bot is not going to be responding to, right? That it's going to be a… that it's going to basically be… need to be a human.
I'm not saying I know what it is off the top of my head, but it feels like it definitely should be possible. Like, there's pretty easy ways to suss out bots.
If you… it can interact with them.
**Trask Stalnaker (Microsoft Corporation)** 25:21 I've contributed to a couple of repos now that have implemented things like that, and, like, my agent will stop and it'll say, hey, I cannot proceed, because of XYZ, and… I don't know, I haven't seen a good one yet. A good way to solve the problem yet.
**Jason Plumb** 25:46 The author of that periodic metric reader, Time Out PR, in their bio, it literally says, pushing commits nobody asked for.
That's a… that's a point of pride for them.
**John Watson** 25:57 Hmm.
**Jason Plumb** 25:58 I would…
**John Watson** 25:59 We just closed that one.
and just, like, say, sorry, we don't accept… we don't accept, PRs from randos who don't care very much about what they're actually doing.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 26:11 And if they're real, like, 5 or 6 cycles deep in it.
**John Watson** 26:16 No, no, I know, I know, it's super frustrating, no doubt, but at this point, I would just close it, and just be like.
we… and just… and just say, hey, if you're a real person and you really care about this, get back to us, reopen the PR, and we can talk.
Which they're not, so it's not gonna happen.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 26:34 I mean, they might be a real person guiding a harness, so, like, they can jump in once they get blocked and say, like, oh wait, I am a real person, here's what I am, here's proof, and then it just reverts to the harness.
**BRUNO Baptista** 26:49 So, one thing that's… I found that sometimes work is, Ask explicitly to the person to explain the change that they are proposing.
In, in very short, concise words.
And if it's an LLM replying, you will see it's an LLM.
Someone writing an explanation for a problem that they understand will… Whoa.
not write a page of Markman.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 27:27 Yeah, and I guess the challenge that I'm grappling with is, like.
I often don't want to reject the PR out of hand just because it's an LLM. Like, there's one contributor I can think of that has I think a very well-tuned harness, and I think it's a harness, I think it's an LLM, but, like, they limit the number of things that are open. The PRs that they open are always, like, very discreet, tiny and, like, useful fixes.
And, you know, if I push back on them, they're very reasonable. And, you know, a human gets in the loop. And, at least I think. I don't… and I don't even care if it's a human or… but, like, the harness, whoever's responding to me when I do push back, it's like, you know, they're not, you know, just trying to merge at any expense.
So it's not like I just want to dismiss the LLM contributions out of hand. It's like… it's like a certain shape of LLM contribution that is just going to detect… it's going to take more effort than it's worth.
And I don't know how to know that up front, whether it's gonna take more effort than it's worth, or whether it'll be, like, fruitful to go back and forth for a few cycles.
**Trask Stalnaker (Microsoft Corporation)** 28:41 Now, how much of the feedback that you have provided on that one, for example, Is common enough feedback to add to your, you know, Agent.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 28:57 knowledge.
**Trask Stalnaker (Microsoft Corporation)** 28:58 line.
Yeah… Because that's… in the… in the instrumentation repo, right, we have so many common mouths, like, such commonality across so many things that it's been super worth, you know, like, on my… all of my PRs, for example, that are, you know, heavily LLM generated, and Lauri will find, you know, something on each one that's, like, dumb and I missed when I scanned, And, you know, I will send the coding guideline PR, to update our coding guidelines, and… The… PRs have been getting substantially better.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 29:50 I'd have to reflect on that. Some of the stuff that I corrected was already in the coding guidelines. Some of it is, like, conceptual flaws, and then, like, they fix one conceptual flaw and create a new one, and it's, like, whack-a-mole.
It's like, you know, each time they fix one flaw, they come up with a new one, and they're not following the coding guidelines as well. And, you know, you can always say, like, hey, fix all… fix your stuff, follow the coding guidelines before I give it attention, but just detecting that they didn't follow the coding guidelines is like a context switch, and, you know, to come back to that later to find the conceptual flaws and to play whack-a-mole with it. It's like, you know, be…
**Trask Stalnaker (Microsoft Corporation)** 30:32 Shouldn't… I mean, shouldn't the co-pilot reviews be flagging that stuff then?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 30:40 I haven't been able to give co-pilot reviews, like, the latest generation, where they can actually, you know, they're better, like you said, and they can take more context into consideration. I haven't given that a proper shot, and I don't know what the state of those are.
**Trask Stalnaker (Microsoft Corporation)** 31:01 Let's check two things. One is… Okay, we're gonna switch you from light to… Balanced, which is a heavier duty.
Effort level for the co-pilot reviews.
And the other thing I would encourage… is, in the… Pull request dashboard has a feature this guy.
Yeah, you can see my… this is my slop repo. but what this… I couldn't require… what this will do is, once they reply, once they address your last… the first co-pilot review.
It'll automatically run another co-pilot review, and then they have to address all of that, and then it'll run another co-pilot review, and it just iterates until they have a clean co-pilot review, and only then does it go to waiting for reviewers.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 32:20 Interesting.
I don't use the Polaris dashboard anymore. I created my own local tooling, but I could still use the same signal, right? Yeah. To… before I give something attention.
**Trask Stalnaker (Microsoft Corporation)** 32:33 I'll take a look at that. What I found in the instrumentation repo, yeah, I mean, people… I mean, it's, you know, people have to go through a lot of rounds, sometimes, of those co-pilot reviews.
But it's all automatic, and it, like, keeps… like, as soon as they… Push another commit, it'll trigger that next co-pilot review, until it's fully cleaned.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 32:59 And I assume you've, you've, like, iterated on the, you know, you watch those co-pilot reviews, at least in the early phases of them, to see what kind of comments it's making, and to tune, like, the guidance, to make sure that you're not leading the contributors down, like, the wrong path.
**Trask Stalnaker (Microsoft Corporation)** 33:18 Yeah, and I mean, it runs on all of my PRs.
So I have to deal… I have to deal with it myself.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 33:26 Alright.
**Trask Stalnaker (Microsoft Corporation)** 33:27 And, you know, occasionally, it will have led it down a more complicated path.
That then, when I do a manual review, I have to wind back.
But that's fairly rare, and I'm okay with them having to have done some extra work there before I looked at it.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 33:51 Sure.
So, invest in tooling. That's what I'm hearing.
**Trask Stalnaker (Microsoft Corporation)** 33:58 Yeah, I mean, I'm still… I'm sending probably, you know, Even to… even as much as we have let's see what the… how many PRs in our, agent knowledge, So… what?
about… One or two… PRs a day, basically.
I'm still fine, you know, anything that comes up that, you know, we have, that I find that, yeah, there's just a lot of stuff I'm adding continually to the knowledge articles.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 34:41 Did,
**Trask Stalnaker (Microsoft Corporation)** 34:42 And it really does help. It didn't… it honestly… it didn't help earlier with Copilot reviews, because Copilot reviews were kind of dumb, and they weren't using great models and all of that, but it's definitely a lot better and able to handle a lot more guidance there. It doesn't just be, like.
oh, there's so much guidance, I don't know what to do, and I give up.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 35:06 I remember at one point, like, you could only access, instructions that were in a very specific place in the repo, and then it could only access the files that were changed in the commit, or in the PR. Like, you know, has…
**Trask Stalnaker (Microsoft Corporation)** 35:19 And there were limits of, like, 4,000 characters for, you know, instructions files, and there were all kinds of limits.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 35:27 Is the… can it access, like, this sort of, like, knowledge-based style information, outside of the GitHub directory? Do you know off the top?
**Trask Stalnaker (Microsoft Corporation)** 35:36 Yeah.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 35:36 I, of course, been researching.
**Trask Stalnaker (Microsoft Corporation)** 35:37 It'll even go to other repos.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 35:40 Okay, okay, so it's like, that is completely, the bounds are completely taken off.
**Trask Stalnaker (Microsoft Corporation)** 35:46 It's… it's a true Agentic, like, it gets… it has tool access and other things, yeah.
Yeah.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 35:59 Well, we spent a lot of the meeting on that.
**Trask Stalnaker (Microsoft Corporation)** 36:02 Yeah, I'm excited for you to enable that, yeah, the… well, we bumped up your co-pilot review there.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 36:10 Effort.
**Trask Stalnaker (Microsoft Corporation)** 36:10 Level, and then, turn on… turn on that… that… that… the PR dashboard setting. So far, the instrumentation repo is the only one who's using that option.
But I'm, I would love to have your feedback on that.
That.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 36:30 Yeah, yeah.
I'll check it out.
Speaking of… Issues and consensus. So this is, you know… John, this is, I guess, is to have a conversation with you. We have this experimental feature that's been in our metric system since the beginning, which never got landed in the spec, and there's no progress in this direction.
some of the things that we've been doing recently with, Bound Instruments and some optimizations I'm making have been, like, sort of intersecting with this, and, you know, supporting this feature has become more complex, I would say. And so, I… I want to… I want to delete it.
What say you?
**John Watson** 37:19 Sure. I don't have a problem with that.
I mean, I doubt anyone's using this feature, so… kill it. Kill it with fire.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 37:28 I could imagine someone using it, but, like, I also don't… Care, because they haven't made a push to land it in the spec for 5 years.
**Jason Plumb** 37:37 Is there any instrumentation around it?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 37:41 Instrumentation around it, or instrumentation that leverages them?
**Jason Plumb** 37:44 Yeah, that's what I mean.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 37:47 Baggage has always been this, this, you know, sort of under-leververaged capability in open telemetry. So, I don't think any instrumentation intersects with baggage except for propagation.
**Jason Plumb** 38:04 And the fact that this exists makes me wonder if somebody had, at some point, built instrumentation that leverages this, like, as part of an agent or an agent extension, but…
**John Watson** 38:13 My guess is that this was a holdover from OpenCensus, that this was a feature OpenCensus had.
And it got… put in because it was in OpenCensus, or because it wasn't available in OpenCensus, but if no one's actually using it, and it's not in the spec, it's not something we need to support.
Even though I think it's a cool idea, because baggage can be used for things like canaries and stuff like that, where you might want to be leveraging some extra metrics, etc. I mean, it totally makes sense why this thing would have existed, especially in Open Census.
Or baggage. They use baggage a lot at Google, as I understand it, to do this kind of canary deploys and make sure and measure specific things around how their canaries were functioning.
But if it hasn't made it into the spec, then… I don't know. I don't think we need to keep it around.
Burn up.
**BRUNO Baptista** 39:08 Yeah, I… I think it's… it's a bad idea to have something like this, because I've heard a few instances where PII ended up in metrics.
Because someone was just forwarding things from the baggage, and they weren't expecting that the baggage had that information. So it's kind of easy… well, it's easier to… to, manage PII if you are local in the instance, but if someone unknowingly sends you something that you don't know, will contain that, that could easily end up In, metrics quite bits.
I hope.
**Trask Stalnaker (Microsoft Corporation)** 39:48 Nobody is sending PIA.
**Jason Plumb** 39:50 active.
So that's the first step.
**Trask Stalnaker (Microsoft Corporation)** 39:53 over the wire.
**Jason Plumb** 39:54 Yeah.
**BRUNO Baptista** 39:55 Yeah, but there are…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 40:01 I actually think that this feature has utility, and you know.
But I think, you know, we just can't… support experimental concepts indefinitely. It's, like, the wrong incentive structure. We need to encourage people that want this to land and be maintained in a permanent fashion to go through the proper channels, which is, like, gaining consensus across languages at the spec level, landing something.
Maturing something, stabilizing something, so… Alright, I shall delete.
**John Watson** 40:36 I had an idea, by the way, just given that I think there's a LLM-driven response directly below the… your issue there.
I wonder… I wonder if another approach we could take is that we… if a user is not assigned Too… an issue?
and they put in a PR anyway.
that we just say, we just reject it. Like, you're not assigned to this issue, sorry. Like, that will prevent the race… Like, the multiple people trying to go and put stuff in.
Around a particular issue.
And it'll also mean that they have to… like, there's a little… there's an extra little bar to go over.
For… to get someone to actually, care about the issue.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 41:27 I think that that type of shape of solution is right, and maybe you could have exceptions for people that are part of the OpenTelemetry org, or are approvers, or like, you know, have named roles, or something like that. Yeah.
I don't know, like, I wonder if we… if we could do that, like, unilaterally within… within Java, or… or within one repo, and… or if, like, you know, sort of we need the blessing of… of GC to do something like that.
No. No blessing, Trask?
**Trask Stalnaker (Microsoft Corporation)** 42:02 No, you don't need a… you don't need a blessing.
**John Watson** 42:05 For Trask, you just need to say you're blessed, and we're done, right?
**Trask Stalnaker (Microsoft Corporation)** 42:10 We're… we are all about maintainer, authority, maintainer, independence, autonomy, thank you for the word, yes, in… in OpenTelemetry.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 42:23 So the rough shape then, just to, like, sketch out that idea a little bit more, would be, like, okay, anybody can open an issue.
And the people who are triagers, approvers, maintainers have the ability to assign somebody to an issue.
And, you know, basically, all PRs must be linked to an issue.
And you must be the assignee of that issue, unless… and the unless is, like, you're a maintainer, you're an approver, you're an OpenTelemetry community member, something like that.
So there's, like, an escape patch for… but, like, you know, the path for, you know, strangers making, making contributions is open an issue, get that issue blessed by the maintainers, approvers, triageers, and get yourself assigned to it.
**John Watson** 43:13 Yeah, and I would say the intermediate step is if someone says, hey, can I take this? And then you respond, please sketch out what your solution might look like.
And if it looks reasonable, we'll assign you this issue, and you can go.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 43:30 Yeah, and sketch it out even in the issue, even. I mean…
**John Watson** 43:32 That's what I mean. Yeah, that's what I mean. Like, in the issue, like, sketch out a shape of your solution.
Something like that.
**Trask Stalnaker (Microsoft Corporation)** 43:43 I like it. I think the only thing that I might… I might do differently in the instrumentation repo is not necessarily requiring an issue to be open first.
Because I… I don't… the… the behavior that I… that… is… more difficult is, like, the open issues that people farm. And… but if somebody has their own problem, and they come, and they want to submit a PR directly.
I haven't normally seen that.
be a problem.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 44:25 Yeah, and I guess, how do you… how do you tell the difference? Like… How do you tell the difference of that person opening the PR for a problem they encountered?
And they're not just farming issues, is… is that? Is, like, or versus somebody that, you know, set their LLM basically on the same path as, like, farming issues, but skipping the issues and, you know, going through the code and looking for imaginary problems.
**Trask Stalnaker (Microsoft Corporation)** 44:50 Oh… Yeah, I guess we haven't had that in the instrumentation repo, but I know you have.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 45:01 Alright, well, I'll… I'll maybe… noodle on this and see if I can, like, come up with, like, a proposal that, you know, doesn't have a bunch of sharp edges that are gonna be horrible. Maybe we can take a trial run and be open to just, like, you know, ripping it out, or switching paths, or something like that.
**Trask Stalnaker (Microsoft Corporation)** 45:23 Cool.
Yeah, I think some… I know that some of the… you might even look… I think, like, the collector… I think a couple other repos have done something similar in terms of you have to have an issue and be assigned to it before… You can open a PR. I feel like the collector did that.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 45:44 Sounds familiar.
**Trask Stalnaker (Microsoft Corporation)** 45:55 Alright, let's go to our last topic.
**Jack Shirazi** 46:00 Yeah, I'm the, meat proxy for this, agenda item.
But for a Sylvan, not for an LLM. I promise you, Sylvan's not an LLM now.
You've seen the picture, and it was… it was really well animated. Yeah, he's just got these two JMX, PRs… I think the… one of them looks like it's… I think the other one is the one… I can't remember which one.
**Trask Stalnaker (Microsoft Corporation)** 46:28 Include, exclude, okay, yeah.
**Jack Shirazi** 46:29 One is dependent on the other, and the one that's the other… is… is… anyway, he's addressed everything that's in there. He just wants you to have a look, and it's… it's, it's on the milestone for this release, this upcoming release. So… I think this is… it's just a prod to please have a look at it.
**Trask Stalnaker (Microsoft Corporation)** 46:58 Yeah, why does it dashboard… Where's the dashboard? Our runners have been so slow lately that, That's the gosh.
Oh yeah, it's just… behind.
almed.
I wish the… I don't understand why the GitHub actions, this actually doesn't look so far behind. Okay, I'll have to look at that and see why it issued… Fix that.
**Jack Shirazi** 47:36 He thinks he's addressed everything, so… If there's anything outstanding, just… he'll respond quickly.
**Trask Stalnaker (Microsoft Corporation)** 47:43 Cool.
Yeah, speaking of the, this month's release, I want to put out already that I'm thinking it will probably be, one week late.
So instead of next Wednesday, a week from next Wednesday.
Just so that we can get all of these, last 3 out of things in.
Lauri, sorry, but I had no idea the server address and network peer address database stuff was gonna explode, so… So much.
But yeah, that turned into, like, 40 PRs or something.
**Lauri Tulmin** 48:28 Yeah, it's surprisingly complicated.
**Trask Stalnaker (Microsoft Corporation)** 48:38 Alright, anything anyone else wants to chat about?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 48:49 Since we have time, A while ago, we added some… content to our knowledge base about null guards, and the idea is, like, we use null away everywhere, and NolaWay makes sure that we're internally consistent, and that, you know, There's… there's no methods that… are non-nullable, or that are nullable, that don't have null checks in them, and vice versa. But, like, it says nothing about external consistency. So, like, you know, somebody can take a dependency on our library.
call one of our APIs, which is non-nullable, with null, and, you know, end up with a null pointer exception, or something like that. And, So, the null guard advice is all about, like, hey, you know, there's different sorts of classes of APIs we have, some that we should fail fast, some that we should fail gracefully. Let's have, like, at the perimeter of our API, let's have, like, a consistent policy for what we do around null arguments and checking and things like that.
And, I set the LLMs on it and had them go find all the instances, and to, like, have it comply across the whole repository with this policy, and as you can imagine.
hundreds of files, thousands and thousands of changes, just, like, sort of intractable to review. And so I sort of gave up on it, because I was like, I don't want anybody to have to look at this. And even still, like, you never really know when it's done.
I sort of picked this up again recently, and I'm kind of taking a different tack to it, and I'm wondering if folks are interested in this. And the tact that I'm taking is, start with, like a sort of API conformance test.
an automated test that we can run against all… a single module or all modules that, you know, determines if a particular module's public API surface area conforms with what our policy is. And so it's, like, it's programmatic and deterministic.
Right? So it can find all the instances where, you know, we need to have one of these checks in where we're not conforming to the checks. And then once that's in place, it's sort of like Trask you know, instrumentation conformance, where, you know, you have a big, table somewhere where you have checks or X's, and then the X's are all the things you need to fix. And then you can sort of submit, PRs in increments to sort of, chip away at all the X's until everything conforms.
And so, yeah, this is just an idea in my head. I've sketched out some of the bits of this locally, wondering if you all think that this idea of checking for nullness in a consistent way at our API boundaries and doing it across all of our modules is, like, is worth investing in? Like, is worth being consistent on, or if, you know, I should just sort of abandon this.
**Jason Plumb** 51:57 It seems cool.
**John Watson** 52:00 Jason, I thought you were the just-don't return null camp.
**Jason Plumb** 52:04 I am. But now, now I'm in the camp of use a language that has, explicit null types.
Knowable types, yeah.
You don't know me.
**John Watson** 52:17 I've worked with you a lot.
**Jason Plumb** 52:19 20 years.
**John Watson** 52:20 Yeah, it's been a long time.
I personally am… ambivalent, like.
It would be great to get it cleaned up so we're in a tidy, neat… Place, and we're actually conforming to what we say we should be conforming to.
But it also doesn't feel like a super high priority.
So…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 52:42 Yeah, and that's why I would want to make it, like, sort of a task that we can chip away at in the background without stealing too much of people's attention. Like, the shape of what this would look like from a contribution standpoint is, like, an initial PR to, like, add the automation, the automated detection.
And then, you know, sort of background PRs that are capped at the number active in progress, maybe, like, one at a time, where we go module by module and actually apply the conformance shape to all the public APIs, and so, I don't know. I would hope that it gets to the point where we can just, like, sort of do a quick scan of these automated PRs, and just be like, yep, looks about right, check the box.
Merge it, move on.
**John Watson** 53:28 Yeah, I mean, if it's easy to get that automated, then I'm then definitely in favor, and I'm… I'm happy. Like, when I have downtime, I go through and skim through and see if there's easy-to-review PRs, and I'm happy to check them off.
So, if it's easy to automate, make it so. That's what I say.
**Jack Shirazi** 53:47 Alternatively, you can consider that as a lembate.
And then anyone that does a PR for that, you can… Just reject them.
**Jason Plumb** 53:55 Is Dan…
**John Watson** 53:57 them from the community.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 53:59 Yeah, there's a pretense to ban me.
Got myself banned.
**Trask Stalnaker (Microsoft Corporation)** 54:09 Just wanted to share this quickly, So we did, a little bit of the project laden, the JDK AOT, folks reached out, Jonathan, thanks for hooking us up, connecting us.
And we did a little spike here, There was just kind of a small thing we needed to do to be able to support, at least with a workaround at this point.
And… You can see the… results of, like, our little benchmark here, with the AOT.
And we're continuing to kind of… Lauri and I have a chat with them, continuing to look at ways that we can integrate better with AOT.
But it's cool, they have them in JDK25 now. I hadn't tried out the AOT stuff at all.
And they're looking at making some things work better with agents in… future JDK2829.
**Jason Plumb** 55:35 Cool.
**Jonathan Halliday (IBM)** 55:37 Yeah, there was some nice speed up there. Andrew's, gonna reach out to… Someone client who's, an early adopter of Leyden and also uses OpenTelemetry Agent, and, see if they're willing to… To try this out in, some form of limited production environment, to see what the performance gain there is. But, yeah, looks very promising. Thanks.
**Trask Stalnaker (Microsoft Corporation)** 56:02 Yeah, also, I'm very curious if there's other, I mean, about any compatibility issues, because this is the… this is a very, very small, slice of, like, happy path that, it works.
But I would be very interested to… I was trying to think, and Lauri, I don't know if you have… I was trying to think of what it would take to run our entire All the integration tests.
using AOT.
I think it would probably be a mess, but maybe worth trying.
**Lauri Tulmin** 56:47 I'm not sure, like, whether… Whether it would actually prove something.
Look… Traska, did you try that, after… After the boot class path change.
Did it actually start, like, Did it actually start, starting up faster?
Like, does the AOT actually work?
**Trask Stalnaker (Microsoft Corporation)** 57:19 Sorry, what?
**Lauri Tulmin** 57:20 like, did you compare, like, before you did the boot class path change, To…
**Trask Stalnaker (Microsoft Corporation)** 57:35 I mean, I don't think the AOT work, like, is not… we… I don't think it'll work without that.
the…
**Lauri Tulmin** 57:45 Like, what I was meaning, like, was, like, in the current state, with the agent, does AOT, like, have any benefits?
**Trask Stalnaker (Microsoft Corporation)** 57:54 In the current state.
I mean, it has, like, You mean other than…
**Lauri Tulmin** 58:03 Okay, like the normal versus AoT, so it must have something.
**Trask Stalnaker (Microsoft Corporation)** 58:07 Yeah.
And it's, you know, it's mostly… this is without the agent.
So, you know, there's… Alright, this is just, like, showing the AOT improvement on this basic Spring Boot app.
And then when you throw in the agent, It's… What?
**Lauri Tulmin** 58:29 Yeah, I think it's, like, probably, like, dishes still that, the AoT training run is done without the agent, so when the agent starts, it has to, like, re-transform a bunch of classes, and that, like, still has, like, a lot of overhead.
**Trask Stalnaker (Microsoft Corporation)** 58:45 Yeah.
That was the last email I just sent. I don't know if you saw this.
replied to Andrew this morning about that. Yeah, I'm really… I really would love if we could… I know that re-transform… Transforming the core JDK classes is pretty much off the table.
My… but being able to transform application classes during the AOT training phase.
Could be really big for us, both with being able to install the virtual fields.
And the performance, the startup.
Cool, yeah, if anybody happens to hear of anybody else out there using, AOT.
Very curious.
Alright, we have hit our time. Thanks, everyone.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 59:49 Take care.
**Jason Plumb** 59:51 Bye.
**BRUNO Baptista** 59:52 Okay.
