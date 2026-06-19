SIG: Python SIG
Date: 2026-06-18
Duration: 64 minutes
============================================================

## Zoom Recording Transcript

Riccardo Magliocchetti 00:00:24 Hello, everyone.
Tammy Baylis 00:00:29 Hey, Ricardo, hey everyone.
Hey, Diego!
Hey, Shuin.
Diego Hurtado Pimentel 00:00:45 Hey, sorry, I was muted.
How's it going?
Tammy Baylis 00:00:52 Yeah, good, how's your day?
Diego Hurtado Pimentel 00:00:56 They're crazy, you know.
No?
Not too bad, because you're in 2026.
So great.
So, please.
Riccardo Magliocchetti 00:01:52 Welcome, everyone, to this week's Python SQL.
We're waiting a few more minutes for more people to join. In the meantime, please add yourself.
Zanathing this to the notes, and also feel free to add any topic you want to discuss.
to the notes as well, thanks.
Aaron Abbott 00:03:44 Hello.
Diego Hurtado Pimentel 00:03:48 Darren.
Aaron Abbott 00:03:49 Hey, what's it going?
Diego Hurtado Pimentel 00:03:51 It's a glimp.
Aaron Abbott 00:03:53 Oh, pretty good.
Riccardo Magliocchetti 00:04:14 Well, Caleb and people, I think we can start.
Michael, everyone.
Again?
Let's start with the triage.
Oh.
Amy, do you want to drive, or…
Tammy Baylis 00:04:36 Yeah, sure, I can… share my screen while I ramble for 5 minutes. Thank you.
Window, Chrome board… Yeah, alright.
Let's go through no status, we'll stop at 9-10.
Sorry, schooled too far.
Config inner SDK longer.
Add a way to configure instrumentation scope.
Aww… Wonder how this ties into stabilization. Oh, this is, an older issue.
Sorry, I'm locked in under the wrong account. There we go.
I think this is ready for a look, or… oh, Lucas has already commented.
Not conformant with the spec.
Lukas 00:05:53 Yeah, I looked at it, and it's, like, changing… I, I, I, yeah, I don't… this isn't… Pretty sure this is configuring the interlogger on… Actually, I can't remember what this is exactly, but he's, like, changing API… function, signatures in the API, which is definitely not what we want.
If you look at the… the diff quick.
Unless I'm, like, missing something, but yeah, if you go to, like… Logs internal, That, yeah, just the internet.
Tammy Baylis 00:06:29 Hmm.
Lukas 00:06:32 Yeah, he's, like, adding instrumentation scope to… Yeah, so I think this is actually… yeah, now if I remember correctly, this is for configuring the instrumentation scope.
On the interlogger for the… logging handler, so I've actually opened a PR and contribute that, actually.
does that properly.
Tammy Baylis 00:06:53 Okay!
Do you happen to remember the… PR number…
Lukas 00:07:02 Yeah, I can grab it.
Tammy Baylis 00:07:04 Oops.
Riccardo Magliocchetti 00:07:06 I think it was a reference on the issue as well.
Lukas 00:07:09 I'll say goodbye.
Tammy Baylis 00:07:14 Yeah.
Lukas 00:07:15 Yeah, we can, like… address it later, but I think that… that PR should maybe be closed.
Yeah. Original one, but others can take a look, too.
Tammy Baylis 00:07:29 Okay… Okay, cool.
Thanks for this.
Freeze… This one… Okay, thank you for that.
Two more minutes.
Oh, this one's closed, why is it still in the column? That's okay.
Removed from board, maybe? Or should it be done?
Oops, no!
Lukas 00:08:30 Yeah, maybe we need to update the automation.
To… remove.
Tammy Baylis 00:08:37 Make note of that for later.
Let's see… Thank you!
Fix.
Clear… Open Census Execution Contest.
Oh my goodness.
Okay.
Aaron Abbott 00:09:14 Is the PR just fixing the test?
Tammy Baylis 00:09:16 Yeah.
That'd be… that'd be really good, actually.
Aaron Abbott 00:09:22 Yeah, I think there was also some discussion in the spec, maybe… two or three weeks ago about whether or not we could just get rid of the OpenCensus shimming altogether.
Liudmila Molkova 00:09:37 And there's a PR for it to deprecate.
Aaron Abbott 00:09:40 Okay.
Yeah, awesome.
carlosalberto 00:09:43 Actually, the PR is already merged, and we will release that in the specification.
So it's ready to go.
Tammy Baylis 00:09:52 Oh, great!
Would this… The timing of this, would this be nice to merge anyway in the meantime? Or… Removing the test entirely, or…
carlosalberto 00:10:07 I have an opinion, but Yamila, I would like to… to hear what you think first.
Liudmila Molkova 00:10:17 I mean, I… I'd rather not marriage, but it's not a strong opinion.
carlosalberto 00:10:23 Yeah, I wanted to say that if it's something small, go half, be nice to the person who opened this PR, but if it's too much work, maybe say not worth the effort, you know.
Tammy Baylis 00:10:40 Okay.
Aaron Abbott 00:10:41 Okay. And maybe, like, as an action item, we should probably… You know, delete this code and groom the, backlog for… other issues, because I'm assuming somebody just picked this one up, because it was, You know, sitting there, and they found it, so…
Liudmila Molkova 00:10:59 It's not a signal that they're actually using the shim.
Right, yeah.
Aaron Abbott 00:11:04 Yeah.
And maybe we could validate that with them, but…
Tammy Baylis 00:11:12 In the spec, we might actually be removing this altogether.
I'll get back to you.
Okay, I will… Yeah, I'll follow up on this.
Oh, thank you! Notetaker!
Let's call it that for triage today.
Leighton Chen 00:11:39 Thanks, Tammy.
Riccardo Magliocchetti 00:11:47 Hey, you tell me?
Okay.
Thanks to the people have filed, what they're working on this week.
I see… exporter letter work from Lucas.
I added, like, some reviews before next release?
For the June release.
Dylan is working on standard attributes.
Yeah.
higher on stretch goal, looking at tool improvements and locking, and later looking into instrumentation stability. Thank you.
Okay, first topic from me, very quick one. I've seen this issue about the OpenAI instrumentation.
And then I see that, it looks like this has already been fixed.
But we're just missing a release.
And so… yeah, wondering if… If it's fine for everyone if I cut release for the… old OpenAI virtual instrumentation.
Liudmila Molkova 00:13:00 The one and the patent contract.
Riccardo Magliocchetti 00:13:02 Yes.
Liudmila Molkova 00:13:04 Okay, yeah, that's interesting. So, the… what we wanted to do, we wanted to release the things from New Repo?
Then make the final release from this repo.
deprecating and referring to the new packages. I guess one extra release for OpenAI does not change the plan at all.
And I… yeah, that… no concerns for me.
Riccardo Magliocchetti 00:13:36 Okay, thanks.
Liudmila Molkova 00:13:39 Yeah, thank you for taking care of it.
Riccardo Magliocchetti 00:13:43 Sure.
Ben, next topic… is from Diego, policy regarding AI usage and reviews.
Diego Hurtado Pimentel 00:13:54 Yes, hello everybody. So, sorry if… this… everybody already knows this, and this has been discussed before. I mean, I've been active, in a while.
I am… And I'm aware that we're getting more things, more BRs and stuff, that we can't review them all.
So, this one's very simple, though.
What do we think about using AI for reviewing these PRs at all? What's our policy on that, if there's a policy?
Aaron Abbott 00:14:37 Diego, could you… so, like, one thing is we have Copilot set up, and I think we have some custom instructions as well, but… Was your question, like, if I point my own thing at it and it drops Comments as myself, or something like that, or a specific tool.
Diego Hurtado Pimentel 00:14:56 This is a very open-ended question. What I want to know is, So the way I see this is that we have a problem, right? That we have too many PRs to EV.
And my question is, Are we willing to use AI to solve this problem? If so, how… Do we want to use it? What risks do we see? And so on. It's a very open-ended question.
Liudmila Molkova 00:15:33 that there… I think there is no policy across Otel, so what exists today, and it can be moved further. There are instructions for Copilot, there are in the GitHub instructions.
And they are very basic, but they're supposed to be short.
And, one thing we've been doing in some other repos, in GenAI repos specifically, that we, rely on Copilot as a first round of review.
So it finds, like, obvious issues, or… well, not so obvious, but, like, something that's… that's easy to put in the instructions that are specific to the repo, right?
And, the human review would come after, the GitHub is green for… oh, sorry, the Copilot is green.
we have access to Copilot, I think, as up in telemetry or maintainers can get… oh, no, sorry. I don't know if it runs on your personal, as your personal account, but I think for some repos, we set up Copilot as… default, so it just automatically runs on every PR, and we cannot figure out how to do this, as Trust would know for sure.
And… Yeah, it hallucinates, but at least my personal experience, it provides some reasonable feedback.
It might not catch some serious design flows, but it catches a lot.
Diego Hurtado Pimentel 00:17:06 Alright, thank you, Lumito.
Anyone else has, comments or opinions on this?
Aaron Abbott 00:17:16 Yeah, I feel… Oops, sorry.
carlosalberto 00:17:18 Sorry, I just wanted to ask something that… do you have something in mind, Diego? Because it sounds to me that you are asking this because you want to do something.
Diego Hurtado Pimentel 00:17:29 Yeah, you got me, Carlos, then. No, actually, I… don't have… something in mind yet. It may… it sounds like, I have, like, a secret plan. But no, I actually was just thinking the, like, the… the obvious.
thing was, okay, if we human beings cannot handle the volume of PRs to review. The obvious solution would be of, well, then, offload… Oops… Maybe part of this… Work to… to an AI, right? That sounds so obvious, but of course, that comes with lots of questions that need to be answered before we do that, so I am pretty much starting the discussion here.
Regarding how much can we rely on AI if we are… if… Are we willing to… let an AI agent fully… handle an entire PR review process, even to the point of maybe just telling us this can be managed or not, and so on. That's the kind of questions that… that, that I have, and that's the discussion I want to start here.
I don't know if… yeah, I don't think.
Riccardo Magliocchetti 00:19:07 Great, yeah.
Leighton Chen 00:19:08 Oh, sorry, can you guys hear me?
Diego Hurtado Pimentel 00:19:10 Yeah.
Leighton Chen 00:19:12 Oh, okay. Yeah, I think, the… the large amount of PRs has always been an issue.
In addition to what you mentioned, Diego, about possible solutions for, kind of, alleviating, like, the tail end of that funnel.
I think we found that, like, some of our policies of how PRs even get created in the first place have been kind of loose and not really well-defined. One example I can really think about right now that I've been running into recently is, like.
There are a lot of issues that are created, and that are not specifically pruned by approvers or maintainers to be even, like.
Something that we want to do, or, like, the solution is something that we think is a good idea.
And then, contributors create a PR for it, without the issue actually being, addressed or anything. So that's actually a big part of the top of the funnel, which is why we have so many open PRs.
Some of which may not even be of interest to a lot of people. So, I think one thing we can do to first even combat that without even involving PR reviews or AI is to kind of, like.
be a little bit more strict, in that. Either, Change our issue template, or even using, You know, automation to kind of remind, contributors.
Yeah, second thing is, I found that, or I think this has come up a couple of times, the reviews are… sorry, sorry, PRs are also actually being created en masse by some users who are using agents and AI on the top of the funnel as well.
And I think that part, we're not… we're also not very, kind of, strict.
on. We kind of have, Like, a loose policy, where it's like, if we feel like this person is… not a real person, or they're not being very constructive, with their… their PRs and issues.
So those are things that probably we want to address alongside your question, Diego.
Before we come up with some, like.
automated way, leveraging AI to, like.
fully cover reviewing the PRs from the… from the review side.
Yeah, so the symptom is not just, like, the fact that we have a lot of PRs, so…
Diego Hurtado Pimentel 00:22:02 Alright, thank you later.
Riccardo Magliocchetti 00:22:08 You'll cuss.
Lukas 00:22:10 Oh, yeah, I think Leighton kind of covered… the later half was my concern. Like, I see a lot of PRs… Now, where… I mean, it's even… literally, the PR description says, generated by Claude.
And at that point, I'm like… like, what we need to probably try to… I don't know how to solve for this, but what I don't… what I don't want happening is, like, someone submits an almost completely AI-generated PR, we review it, they just feed our responses back to the AI, they make more changes, right? At that point, it's like… you know, I could have just done that myself with Claude, right? So, Yeah, maybe, I mean, we can start being more strict, like, I mean, I've closed some PRs, like, that are blatant spam.
But yeah, so I think, yeah, we should try to address the volume before maybe… Jumping right to just, like, AI reviewing all the AI PRs, so…
Aaron Abbott 00:23:15 Yeah. No, I like that perspective. I think I agree. If it's the AI PRs, we should do something. I also mentioned in chat, trying to dig up the link, but GitHub lets you limit concurrent PRs for new contributors now.
I don't know what the criteria for deciding new contributors are, but if the… concern is, like, you know, the AI… AI PRs from new users who are trying to get You know, some kind of brownie points or whatever we can… Try that feature out.
But, you know, one other thing I wanted to say was, like.
All that aside, I think the improving the co-pilot review would be really good.
I would totally be welcome to that. I think we could… Tune the, tune the instructions a little more. So, in particular, I think The laborious part of a lot of the reviews is making sure You know, it, like, fits into our plans, which sometimes aren't written down, so if it has some kind of knowledge of the spec, like, what's going on in, open source, like, what's experimental, what's stable.
All that kind of stuff that requires a lot of subjective decision-making.
That would be awesome as, like, a first pass. I don't know how good it would be at that, but maybe we can at least, like, settle on using Copilot for reviews.
I think that's pretty much what we've done.
I think we have, you know, support for it in CNCF, but… yeah, like, we could just improve the system instructions. I think. I think I've heard, like, the GoSig has done this, and it's been really great. They feel pretty happy with the result.
Yeah, unless anybody is super opinionated and wants to share, you know, some other tools amazing or whatever, I think…
Diego Hurtado Pimentel 00:25:01 They said the go… the goal… I know people have… got good results with, Copilot, right?
Aaron Abbott 00:25:10 Yep.
Diego Hurtado Pimentel 00:25:12 Yeah, I'm just writing this out to us, go and ask them.
Okay, thank you, thank you.
Aaron Abbott 00:25:21 Yep.
Liudmila Molkova 00:25:22 a quick, thing to run by you. So, one thing we can do on more, like, hotel level, probably, it's a proposal to say that if you are, like, a full AI, just make it obvious. Do it on behalf of AI agent. Don't use your human identity for this contribution. Whatever AI agent you use, just the… send the PR from its name.
And then it's obvious for everybody that you're talking to AI, and the AI replays back.
Like, to Dylan's point, human attention requires human effort.
Riccardo Magliocchetti 00:26:05 Yeah, but, like, I think we added already some instruction in the agent's file.
To… to ask agent to… to make it obvious, but… the PRs are AI-assisted, but I have to say, I haven't seen… any PRs, but… Mentioned that?
And given the description, but does not follow our template, I think most of them are AI-generated, so… Yeah, like, I'm not…
Diego Hurtado Pimentel 00:26:40 Sounds like we need a reverse… a reverse CAPTCHA to figure out if the…
Riccardo Magliocchetti 00:26:45 Yeah, so fair.
Diego Hurtado Pimentel 00:26:46 the authorities.
Such cheap.
Great.
Great. I'm writing everything down.
I don't know if anyone else… I don't see any more recent.
In any case, I'm not, I wanted to… to ask all of you, what do you think. And, And from your comments, what I'm getting is that we can… the problem comes in… from two sides. One of them… too many… issues, being created that may… many of… some of them could not even be valid, and also PRs, many PRs getting opened and… Even the wild ones are… require human potential, right? So, I can, put some effort into investigating what can we do, how can we leverage AI to help With the… with this problem we have here. Just for the record, it's not my intention, just to… To automate this fully, what, my intention is to try to find Tools that can help us, not, Not completely remove human beings from… From the… the review process, right? I can work on that, on this, and maybe report back next week on whether…
Riccardo Magliocchetti 00:28:35 Thank you.
Nope.
Diego Hurtado Pimentel 00:28:45 Nobody.
Riccardo Magliocchetti 00:28:46 Next topic is from Aaron.
load stabilization.
Aaron Abbott 00:28:50 Oh, yeah. So Ricardo, we chatted about this last week. I… everything in italics, I just kind of copy-pasted from last week.
I think… I forget who it was, but somebody was, you know… oh, I think it was, Hector. He was like, you know, what… what can I do to help with the log stabilization?
Well, I think, first of all, like, it should probably be a little more of a priority for us. I think we have, like, a pinned issue.
Saying something about it, but… Yeah, like, this seems like an active area, so… I… I just wanted to, for right now, figure out if we can consolidate the tracking of this… of the log stabilization, because we have you know, this issue, which I think for a while we were working on, we have the project board.
But then there was just some kind of conflicting information that we found between that.
And some of the open issues in the repo. So, Yeah, Ricardo, any thoughts? Like, is this first issue something we can close out? Should we use the project board?
I think you were kind of leading this, if you had any thoughts.
Riccardo Magliocchetti 00:29:54 Yeah, I think that we implemented everything, we had, in this one… And, yeah, so we can close it, of course.
Aaron Abbott 00:30:11 Cool.
Riccardo Magliocchetti 00:30:13 Let me check what… okay, it's already managed, so… Closing right now, so we don't forget.
And yeah, like, I kinda… got distracted by other things.
But as far as I remember, like, we… We merged and fixed all the big issues.
And what is left is really, like, renaming stuff, and move to the proper names. I, like, I just said, we have the boards, we have a lot more issues.
But… I don't remember what you have in these boards.
Aaron Abbott 00:30:54 Yeah, I think if I remember right, we wanted to sort out the things that would require breaking changes or be disruptive first, and then we decided that would be good enough for Potentially making a, like, a release candidate, and then if there were… things that were, you know, pretty, pretty minimal bugs. Oh, also, we do… we had the GC review from Lyudmila, and I think Lyudmila, I don't know if you had time to look at this again, but that was another one, was… to take another pass and approve from the TC perspective, but.
Liudmila Molkova 00:31:27 he didn't have a chance this week, but I'll try before the next call, and well, it seems that everything is pretty much resolved, so very optimistic about this one. Also, TC perspective, not GC.
Aaron Abbott 00:31:41 Sorry, sorry, my bad.
Definitely didn't mean to say that. So I think, like, the… maybe we could go through the issues again offline. Like you mentioned, there's some new issues, Ricardo, but, Yeah, like, maybe we should… Ludmel, I don't know if it's super urgent, maybe we could come up with a date for you that we're aiming to, like, do this. I think we have a release coming up, so maybe the following release we could try to do… an RC for the logs, We feel like everything is good, but we don't need to talk about it more in this meeting, I just wanted to loop Ricardo in from last week, unless anybody else has thoughts.
Liudmila Molkova 00:32:17 So just to confirm, you would tell me when to look.
Aaron Abbott 00:32:24 Or… or we could come up, you know, I just don't wanna… like, if you're busy with other stuff, I'm just not trying to put it on your plate urgently.
Liudmila Molkova 00:32:33 I think this is an important thing I can do, by the next week, but if you'd rather, me wait until you finalize the things, we can also do this, whatever works for you.
Aaron Abbott 00:32:44 Honestly, if you have time, that would be great, I think that would.
Liudmila Molkova 00:32:46 Awesome. Let's do it, yeah.
Aaron Abbott 00:32:50 Okay.
Cool. Anyone else have thoughts on this one?
Cool, and I think I had the next one, too, so…
Riccardo Magliocchetti 00:33:07 as well.
Aaron Abbott 00:33:08 Yep.
I'm gonna put Lucas on the spot. Sorry, Lucas, I was… oh, cool, you put a… an issue there, yeah.
Lukas 00:33:18 Yeah, we just decided to, there's, like, a common, OTLP HTTP client that lives in here, and we also brought… I also brought in, like, there's some of the aggregation helper functions, so this is just, like.
One last common package that… that I want to use for the… that we can use for the final JSON exporter, so… So this should be the last one.
Aaron Abbott 00:33:48 Last one, and then you would…
Lukas 00:33:51 And it's the final… JSON exporter, which should be actually very, very small now that we have all of these utilities, and then we can also work on the work to, kind of remove the duplicate code in the OTL, the regular proto-HTTP exporter.
Aaron Abbott 00:34:10 Okay, awesome, thank you so much. I'm kind of just asking because I'm excited about it, and… I keep hearing people say that Protobuff is annoying, so it would be great to have something As an alternative. So, again, thanks for working on this. Was there anything you want to discuss in this one, or is it, like, pretty straightforward?
Lukas 00:34:30 I think it's pretty straightforward.
Aaron Abbott 00:34:34 Oath?
I will take a look. Thank you so much.
Riccardo Magliocchetti 00:34:45 Okay, later you're next.
Leighton Chen 00:34:54 Sorry, I was typing something. Yeah, Just continuing the discussion from last week regarding, Bumping the instrumentations to stability.
We had a couple opinions, but where we kind of left off last week, was, Ricardo, if you could scroll up a little bit… I think Aaron took some notes about what our discussion was. Yeah, go down. Yeah, so, we want to… are… Our preference is to, you know, leave the… e-comveying folders… so, sorry, then back up. There's two components that we have to address before the instrumentation stability. It's the semantic conventions and the instrumentation package. All instrumentation depend on those two, so we probably have to address those first.
With the semantic conventions, I believe we were discussing that we wanted to leave the incubating module, as within the semantic conventions, for the 1.0.
This doesn't break people, and… we… similar to Java, like what Aaron has mentioned here, we want to… Recommend external customers, to copy the constants, instead.
Yeah, and then I think the only thing we kind of wanted to get Caro, because I think, like, was your opinion? Because I don't… I believe you weren't here last week, as well as what we wanted to do for the instrumentation.
My, package as well.
So I believe users left a bunch of comments here.
We can, like, go through them one by one, unless there's any point of contention, unless you want to bring up something first, Ricardo.
Riccardo Magliocchetti 00:36:49 No, no, it's fine.
Leighton Chen 00:36:52 Okay, cool. Bump semantic dimension to 1.x for stability signaling, but we should also bump every contribute instrumentation baseline.
Since it won't be a break and change, okay?
And I think we don't want to bother to maintain the O.X branch, so do you mean… bump every contribute instrumentation, like, dependency on the 1.x semantic invention as a minimum version?
Riccardo Magliocchetti 00:37:18 Yes.
Leighton Chen 00:37:19 Bobby. And… Could you refresh my memory? What does it… what does it mean to maintain the 0.x branch? Are you talking about, like, releases?
Or what?
Riccardo Magliocchetti 00:37:30 Yeah, like, I mean, like, if you release, a .1X semantic package done as a break, Anything for current and, for car instrumentation.
I like, I guess, like, from our maintainer point of view, It will, like… remove the need to maintain the 0.something branch. We… Any backports?
And so, like, we can just bump the baseline of all instrumentation to the 1.txt branch.
And live with that, yeah.
Leighton Chen 00:38:11 Right, yeah, I totally agree with the first part. Could you remind me what we're maintaining today that is 0.x? I'm only seeing the release branches.
Riccardo Magliocchetti 00:38:27 Yes.
Leighton Chen 00:38:28 Maybe it's not a huge nuance there.
Riccardo Magliocchetti 00:38:32 Yeah, like, I mean, but one of the options on the table was to… Use 1.txt for one.txt instrumentation, and use 0.txt for the… Zero tax instrumentation.
Leighton Chen 00:38:48 Right, right, right. Got it, got it. Makes sense.
Do we have any opinions?
on this… Everyone?
Aaron Abbott 00:39:09 So if I understand, I think I was just confused by the wording here, like… Is the… is the goal to… Make them all 1.0?
Leighton Chen 00:39:24 It's just to update their minimum dependency.
Aaron Abbott 00:39:28 Sadie and Leighton, sorry.
Leighton Chen 00:39:31 Oh, sorry, I think the goal is to, once we bump semantic conventions to 1.x, we bump the minimum version of every contrib instrumentation to 1.x.
Aaron Abbott 00:39:41 Oh, okay, okay, okay, got it.
That makes sense.
Leighton Chen 00:39:44 Right, Ricardo? Hopefully I got that right.
Riccardo Magliocchetti 00:39:47 Exactly that. Thanks.
Right? Like, I think that… Right, this… also, like, the same issue we discussed in the second point, Diego? Yeah, go ahead and raise?
Diego Hurtado Pimentel 00:40:07 Okay, this question's gonna come, like, super, super late, for all this stability topic, but, When we declare this to be 1.0, What are we declaring to be… The things that should be backwards compatible.
Leighton Chen 00:40:40 Oh, sorry, Dia, could you repeat that? I missed it.
Diego Hurtado Pimentel 00:40:43 Yeah, so… When we're gonna declare this to be 1.
What is it going to be?
What things are going to be the things that we will need to keep backwards compatible?
Lukas 00:41:05 isn't… it's everything in the public namespace, right? We still have, like, private, incubating that's, like, internal, right? So that wouldn't need to be necessarily backwards compatible.
Diego Hurtado Pimentel 00:41:18 Okay, so, every, every public symbol.
in those instrumentations.
Lukas 00:41:23 Isn't that what we discussed, either last meeting or the meeting before?
Diego Hurtado Pimentel 00:41:28 Maybe, sorry if I… if I missed it.
Lukas 00:41:31 No, I'm just… I'm also asking.
Aaron Abbott 00:41:36 I think so, yeah, and I think maybe one, like, nuance Hotel has kind of been taking this… We kind of changed the approach, Where we used to be a little bit more, like.
afraid of major version bumps, and for example, like, I think JS is going for their SDK 3.0 major version soon.
I could… they definitely have 2.0, I could be wrong on the 3.0, but generally the idea is to just kind of be a little… go ahead with stability a little faster, and then we can use versioning to show people when things are breaking. So we would try to… yeah, $3 is in progress.
So the ask… yeah, that is the ask, but I think it's a little bit… less burdensome with the, you know, kind of assumption that it doesn't have to be around forever. You can fix things later.
Diego Hurtado Pimentel 00:42:26 So, we are allowing ourselves to… Make backwards and comparable changes.
Aaron Abbott 00:42:36 Yes, if they get a major version bump.
Diego Hurtado Pimentel 00:42:40 Good.
Good.
That's good, that's… that's the right usage of semantic version. Okay, sounds great.
Leighton Chen 00:42:50 I think… I think part of that, like, do we also decide to start conditioning users to not depend on the incubating? Like, we just have in our wording that, like.
These are not promised, I guess, to be…
Aaron Abbott 00:43:04 Yeah, I think we said… we said people should copy in constants from incubating if they need to. They should just copy it into their code.
Leighton Chen 00:43:11 Right, right, right. Yeah, we should… we should get some clear documentation on that when we do bump it.
Diego Hurtado Pimentel 00:43:17 Yeah.
We should crash their applications that will teach them not to use Yeah, yeah.
Leighton Chen 00:43:28 Okay, so, I think, second point… Should we allow users to mix stable and unstable instrumentations?
Car, do you want to kind of talk about the findings you've had about the stability mode?
Riccardo Magliocchetti 00:43:49 like, I think the other… the second point discussed, was to… To bump, and to bump to 1.X, the open terminate instrumentation.
And I think it was discussed to introduce some… Breaking changes as well, like that, zero.tax instrumentation will depend on zero.tax opener instrumentation.
And the WonderText will, depend on the WonderText.
And what time… And so, like.
I think that in real life, like.
Companies that would like the stable thing.
Only will probably just install 1.6 instrumentation, but other people that are fine with Zero doTax instrumentation, like.
It has always been… it has been up until now.
We'll probably have, like, the… The need to have both one.tax and zero.tax instrumentation installed at the same time.
And so we cannot have a true version of OpenTeameter instrumentation package?
And so what, I think I brought here is that we should probably cut, 1.text containment instrumentation package, but does not have breaking changes, so that people can have both All the new instrumentation installed at the same time.
I think that discussion was about, like, removing the stability mode default entry in the enum.
And… just to see, like, if it's… was used outside our country repo.
I did a GitHub search, and I haven't found any users of… this, Variable, and so probably just, like, a matter of… what we want to do inside the contrib, or maybe GenAI, I don't know if… If you're looking at the… obvious flag as well.
Lucas?
Lukas 00:46:21 I think, like, maybe the easiest approach is to just, like, in these new staple HTTP instrumentations, we just, like, forcibly load stability mode HTTP.
So we don't actually touch any of the… Stuff in the… OpenTelemetry instrumentation package. It's just, like, if you were to pass in try to pass in, like, opt… any of the opt-in stuff, it would just be ignored for the stable stuff.
And that should be, like, a very trivial change, like, it's just… just be, like, temporarily, again, like, hard-coding HTTP, and then later we can go in and remove the shim code entirely.
Riccardo Magliocchetti 00:47:06 I think what the spec says that we… We must comply also with the loop, opt-in.
Or something like that. So I'm not sure we can remove the handling of the NVAR.
But yeah, like, I was thinking as well, like, to change the default to the HTTP mode.
And maybe, like, if the user is… passing the fault as MVR, just… Write an error, a warning, and… Ignore it, something like that.
Lukas 00:47:43 Yeah, I mean, do we need to support dupe if… once we're… once we're in a stable… Like, we don't need to support the… old.
incubating stuff that we were emitting, right? Maybe I'm wrong, but that was my impression, is that we could just… I don't have to worry about that either.
Leighton Chen 00:48:04 Yeah, I think the guideline was, like, there should be, like, an X amount of months in which we have the opt-in support, and then afterwards.
We have the freedom to… Just go with the version that we want, like the newer semantic conventions, given we have a major version bump.
That was the guidance.
Ricardo, just to clarify, when you're talking about OpenTelemetry instrument package. You're referring only to the stability mode support, right?
The thing that only relates to semantic conventions, right?
Riccardo Magliocchetti 00:48:54 Yeah, I think that the discussion I've seen in the previous point was about dropping the stability default from the stability mode.
Like, as far as I understood.
So, yeah.
Leighton Chen 00:49:06 Right.
Right, right.
Yeah, my, my… Yeah, sorry, go ahead.
Riccardo Magliocchetti 00:49:18 Go ahead, go ahead, go ahead.
Leighton Chen 00:49:21 Yeah, so I… I think if… if we don't, like, kind of… Have the instrumentations all bumped at the same time.
I think there are… Real use cases in which, like, there would be a mixture of stable and stable?
So, it does make it a bit tricky for the stability mode specifically.
Unless if we move the stability mode logic out of instrument, and, like, have it… per package.
Yeah, we… this might be something we have to support in the interim, maybe?
I'm open to other suggestions, too, but… like, we have instrumentations that are not HTTV, and… and DB.
Sorry, that are not in the process of going into stabilization.
Immediately following this, so… Those would be… the users would be locked in those cases.
Yeah.
Riccardo Magliocchetti 00:50:36 Yeah, yeah, like, all this… comments I added are, like, I think about the use case of… users that… We want to have, like, Like, we appreciate the 1.X bump.
But also may have, like, a lot of work to do in order to move to the new semantic convention.
So, like… I was thinking, like, to just, like.
I mean, fine, like, to drop the ability to send the old semantic invention, but… Yeah, it's breakable.
Leighton Chen 00:51:15 Break it. Zero to X, right?
Riccardo Magliocchetti 00:51:17 Yeah, it goes.
Le Dumila?
Leighton Chen 00:51:22 Sorry, Lumilia hand up.
Liudmila Molkova 00:51:24 Yeah, I think so. Not sure if you've seen and how far we are along with the declarative config, but, the declarative config now defines some options that are specific to instrumentation, specifically for the stability opt-in.
And they kind of belong in the namespace for this instrumentation.
And it kinda makes sense to, have them implemented, maybe even in individual instrumentation, but the configuration API looks like, okay, give me if this value is that, or give me this if this value is this, so there could be some generic helper, or it's just part of the configuration API that provides the value of this, thing.
And it could, in theory, be part of individual instrumentations, or some generic representation of it could be part of the The common package.
And I guess there is also the discussion in the… Stability by default.up, and now the, the project, the post-gradation roadmap, that, there could be, distro-wide.
Experimental opt-in.
Into everything? Oh, like, all experimental features are gated by this.
And they said this can be the common… thing. In addition to declarative config that can override it on individual instrumentations level.
Leighton Chen 00:53:07 Would that be a lot more work?
Liudmila Molkova 00:53:14 I guess, like, one way to implement it would be to… like, I think I've seen, like, that if your instrumentation has something like metric supported, it can have a flag that does it have stable Things?
And the first approach would be… to just mark all existing instrumentations, most of them as it doesn't have stable things. It's probably easy.
And then have the distro Do not enable them if they don't have stable things, unless there is an experimental Just to provide experimental opt-in.
It doesn't look like a lot of work.
Leighton Chen 00:54:00 Right, so I'm hearing another option, besides from the one That was suggested is, instrumentation level configuration via declarative config.
Liudmila Molkova 00:54:17 This would be more work, probably.
Leighton Chen 00:54:20 Right.
Liudmila Molkova 00:54:20 Yeah.
Leighton Chen 00:54:21 Yeah, but definitely something we can consider. Dude, does anybody have any opinions?
Yeah, it's okay, we can continue the discussion and the issue.
We just… let's… Let's table that for now.
I think that's probably the only outstanding point. Number 3… Oh, yeah, there's one more topic, too, so we would probably want to… I think the third one, Ricardo, is just… Just looking for volunteers for the rest of the database instrumentation, so…
Riccardo Magliocchetti 00:55:00 like, I've seen we have a couple of PRs. I haven't looked at the PRs.
Weird.
closely enough, but we have a bunch of PRs that says that we're bumping simultane convention for, I think.
One is by Mongo, MongoDB client.
And another one.
And so, like, we're probably, like… Do you have a list somewhere, I think… under the… Not to… okay, anyway, like… Yeah, so, like… Just, like, free… instrumentation… We'll be missing the… the stable semantic conversion support.
And so, like, if someone has time, maybe we can also, like, finish the DB1.
And, last, have the complex.
set of the beast augmentation supports the very same, semantic conversion by default.
But yeah, like… If we had time, it will be nice, otherwise not an issue for me.
Leighton Chen 00:56:15 Cool, yeah, it definitely can be done in parallel with the, The instrumentation and semantic.
bumping.
But yeah, just… Don't want to spend out too much time on this, I think we do have another topic.
Oh, we have many topics, actually, yeah.
Riccardo Magliocchetti 00:56:37 Okay.
So, Lucas, profiling…
Lukas 00:56:43 Yeah, I just wanted to discuss this briefly, but it looks like the profiling SIG, like, created this issue in the… in our repo, I asked on our channel, like, what exactly the scope of this is, like, I don't know if anyone else has any information or context, But, yeah, I was just wondering, like, are we looking to, like, start At least defining, unstable… some… some unstable, like, API and SDK.
methods for… You know, creating profilers and stuff.
Do we want to start picking this up?
Aaron Abbott 00:57:27 Yeah, I, so I actually, I talked to, This is Frederick. Yeah, I talked… I talked to him about this a little bit, so I… I've looked at this process context and thread context, specs before, and I think I actually pointed out that this 314 Plus has this PyContext ad watcher, but it's… it's only a CAPI right now.
So, so basically this is making the context available to… something like an eBPF profiler, something that lives out of the process, and the idea is, I guess two things. One.
you can set additional, like, attributes in this context, which can be… which will then automatically be attached to the profiles, so you can have, like, find me all profiles serving this HTTP target, for example.
And then the other thing is just, actually threading the context through, which can be helpful for something like OBI, which is the other… OpenTelemetry EVPF thing. So, I think there's that. I haven't really looked super closely at the profiling spec.
But I'm kind of curious what the actual API is. I imagine it's basically just set the attributes, And the last thing I wanted to say was, I think in 315, there's, like, an experimental, profiler… sampling profiler built into Python.
So that's kind of another thing we can look at. If it handles heat profiling.
like, that would be awesome, we can expose this data for the eBPF or whatever, but yeah, I also didn't really understand the scope of what what this needed, so… more research, but I'm pretty interested in this, I think it would be great.
Lukas 00:59:05 Got it, yeah, it doesn't look like there's any… Any spec for what the, like, API or SDK would look like?
So, I didn't know, like, Like, do we want to just start with Doing stuff? Or… wait until there's a spec?
So…
Aaron Abbott 00:59:24 Lucas, do you mind… I think you probably have the most context since you're on slide, do you mind leaving a comment on this issue, just so we can, Have that tracked here.
Lukas 00:59:34 Yeah, I can… I can post the same comment that I posted in the profiling slide.
Aaron Abbott 00:59:40 Okay.
Cool.
Riccardo Magliocchetti 00:59:46 X… Okay, Tammy, you ordered this one.
Okay.
Tammy Baylis 00:59:54 Hey, yeah, just 10 seconds. I created an issue. We should come up with a plan for how to stop OpenCensus support in OTELPython, and I found, the spec issues and just linked them there, so… For future discussion.
Riccardo Magliocchetti 01:00:11 Thank you.
Aaron Abbott 01:00:13 Awesome. Thank you, everyone.
Leighton Chen 01:00:16 Thanks, guys.
Riccardo Magliocchetti 01:00:16 Thank you.
Aaron Abbott 01:00:17 next week.
Dylan Russell 01:00:17 this.
Riccardo Magliocchetti 01:00:18 Here, right?
Liudmila Molkova 01:00:19 Thank you.
Diego Hurtado Pimentel 01:00:20 You highlight the curve.
