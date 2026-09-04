SIG: Python SIG
Date: 2026-09-03
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Riccardo  Magliocchetti 00:00:24 Hey, everyone.
Tammy Baylis 00:00:30 Hey, Riccardo, hey everyone.
Riccardo  Magliocchetti 00:00:41 Hey, Tammy, how is it going?
Tammy Baylis 00:00:47 I'm okay, I've had some dental work this week, so…
Riccardo  Magliocchetti 00:00:51 Not…
Tammy Baylis 00:00:52 But at least I got things done.
How about you?
Riccardo  Magliocchetti 00:00:59 No, that'll work, so it's fine.
Tammy Baylis 00:01:04 Hello, Joe.
Welcome.
I think, We had that, Slack thread in the Approver's channel about which board to use for triage, and I think today, instead of, the traditional board view of all the PRs ordered by no status, etc, I'm going to try looking at The bot-generated issues this time, and see how that goes.
Yeah. Though I was having a… I wasn't here yesterday because of dental work, so I'm a bit behind on my PRs, but everyone will chime in as usual, so it's… it'll be fine.
Riccardo  Magliocchetti 00:01:52 Yeah, no worries.
Tammy Baylis 00:01:54 Thanks.
Riccardo  Magliocchetti 00:01:57 But is it a U.S. festivity today?
Because it'll get rid of some.
Tammy Baylis 00:02:03 Yeah, another quiet day,
Riccardo  Magliocchetti 00:02:06 Cool. Or maybe everyone is on holiday.
Tammy Baylis 00:02:09 Could be. Our North American Labor Day is not until Tuesday next week, which is a little late this year, so… Yeah, maybe people extending their vacation times.
Riccardo  Magliocchetti 00:04:02 Welcome, everyone, to this week's Python SIG call.
We're remaining… waiting one more minute for more people to join.
In the meantime, please add yourself as an attendee.
To the notes, and also feel free to add any topic you want to discuss.
Or to list, whatever we are working on this week. Thank you.
Tammy Baylis 00:04:42 I think we're at 9.05, and I'm sharing screen on… so I'll just start with a bit of triage this morning, and… Yeah, I just wanted to mention that, yeah, thanks, Carlos, for reminding us of the, bot-generated issues.
for, I guess, the first 5 minutes, we'll try that as our time cap. I'll go through each of the issues, top-down, and yeah, if this works, great. I think this will work better than the other board.
Because this, prioritizes what's waiting on maintainers, and whatever is waiting on authors is at the bottom. So… Get a bit bigger… let's start… This is the OTELPython Core bot issue.
And, this is what's waiting on maintainers.
First one… Fix base configuring new.crash. We have a couple… well, we have maintainer approvers… approvals already.
So I think… I think this is just ready for the merge queue. Yeah, it's in there already.
Riccardo  Magliocchetti 00:05:56 Yeah, I think it failed the MargeQ.
Tammy Baylis 00:05:59 Oh.
Riccardo  Magliocchetti 00:06:00 Don't that tool.
And it's again.
Tammy Baylis 00:06:04 Alright.
Thank you, Riccardo.
This one has a maintainer approval… Renovate bot, update CI, that's probably… Yeah, another one that needs to be put back in the queue, but we're aware… This one's got a lot of greens. Enable pi in the rules.
Going to clash.
Rebased… Diff is down, I think… Yeah, if it's already approved… This one will be put in the merge queue, I'm assuming.
Okay, more than a chore, fixed tracer provider crash.
Two maintainer approvals… Yeah, I think this one's ready for the merge queue.
Unify Logging Force Flash… Yeah, I think we talked about this one last week, and… Yep, gotten approval a couple days ago.
This one has one approval and some comments.
Koja and JSON support decoding.
Yeah, question from Lucas.
Not stale. Waiting on maintainers, I think… No, we're waiting on…
Lukas Hering 00:08:05 It's just that last comment, I think.
Tammy Baylis 00:08:08 Yeah.
Aaron Abbott (Google LLC) 00:08:10 which column was it in? Was it not in waiting for reviewers?
Lukas Hering 00:08:14 I recently updated it, so it was, waiting on me.
Tammy Baylis 00:08:22 Okay.
Oh, you did make a change,
Lukas Hering 00:08:27 It wasn't related to this, though, so yeah, I wasn't really sure.
Tammy Baylis 00:08:34 Sorry, I keep scrolling.
Lukas Hering 00:08:39 I can, maybe… Oh, I see Dylan's… Dylan's on the call now.
Yeah, we don't need to spend time in this, but yeah, if you want to maybe take a look at… this… 5402.
And see if we're…
Tammy Baylis 00:08:59 Thanks, Dylan.
Thanks, Lukas.
Sorry, I could spend the whole time. Let's… Yeah, how to split time between sections and boards for this method of tree, Josh, I wonder.
This one has conflicts.
So… In this case, should it be the author's responsibility to do this? I think so.
What was the command again? Oh my god.
Can't remember, I'm sorry, but I want to push this back to the author to… Resolve.
I'll just do that. It's 9-10, I think we have some real topics, so I'll hand it back to Riccardo, and if we have time.
Carlos Alberto Cortez 00:10:00 By the way, if I can say something quickly…
Tammy Baylis 00:10:04 Basically.
Carlos Alberto Cortez 00:10:04 I was trying to, thank you. I was trying to check, and there are a few sections there, there's… you may see that there are two categories. One of them is waiting on maintainers, which means that some people may have approved that already.
And the second one is waiting on reviewers. So, waiting on maintainers is kind of fine, it means that we're making progress, but waiting on reviewers means that nobody has done much. So probably, looking forward, it would be nice if people go and check some of those ones. We don't have to do it now.
But some of them are actually very old.
And nobody has paid attention to them, and I think that some of them are probably been outdated.
So, I will try to spend some time tomorrow going through some of these, and probably adding some notes. As I said before, some of them are probably outdated, and they are… they should be closed instead.
That's old.
Tammy Baylis 00:10:58 Okay.
Riccardo has his hand up.
Riccardo  Magliocchetti 00:11:01 Yeah, like, we should do automation.
for closing still PRs?
So maybe the… oh… Could be that the bot comments will keep the… PRs up to date.
20 MTPR dashboard comment.
Maybe we…
Liudmila Molkova 00:11:26 Oh, we should just complain.
We should probably, create an issue in the… Shared Workflows repo for this.
That the comments should not… like… prolong the life of the stale for requests. I don't know how to do this, but hopefully Trask will figure it out.
Tammy Baylis 00:11:51 I'll put this one in the chat as an example.
Oh, for those interested…
Liudmila Molkova 00:12:02 If you wonder, it can create an issue, it also was, like, kinda… Not awesome. I've seen it before.
Tammy Baylis 00:12:09 Oh, that'd be great, yes please, Liudmila.
Liudmila Molkova 00:12:12 Yeah, sure, thank you.
Tammy Baylis 00:12:16 Alright, great. Already identified improvements, so thank you. Back to you, Riccardo.
Riccardo  Magliocchetti 00:12:22 Bill?
I'm just… Okay.
Thank you, Tammy again. First topic?
for today, he's from Carlos.
Carlos Alberto Cortez 00:12:40 Yeah, it's a pretty small PR, if you could open that. Yeah, it's just basically updating the specification, the matrix, you know, See, you opened this one, he went through… he went through the actual code.
Just a good, like, maintainer tool.
Confirm this is the case, and he's correct on these ones.
I was checking quickly, and they seemed fine, but yeah.
If that's fine, just approve that, so we can merge this one.
Riccardo  Magliocchetti 00:13:11 Brooke, thanks. Like, I think that, seizure, also, like… fixes some issue regarding this, so I guess… Is up to date on implementation?
And… by the way, speaking on compliance matrix… Lukas had… you opened a PR as well, some time ago?
Cor… right?
Lukas Hering 00:13:39 To add the, environment variable flag, right?
Riccardo  Magliocchetti 00:13:44 Like, is it still open? Because I don't remember how…
Lukas Hering 00:13:48 No, no, it's merged, and now it's off by default.
Riccardo  Magliocchetti 00:13:54 Okay, thank you.
Okay.
Lukas Hering 00:14:06 Oh, sorry, you're referring to the, sorry, you're referring to the compliance matrix PR, right? Yeah, yeah, yeah, that's still open.
I think, there was… Let me double check on it, there might be action I have to take. Sorry about that.
Riccardo  Magliocchetti 00:14:35 Yeah, I think you were waiting for us.
go through, so…
Carlos Alberto Cortez 00:14:39 Yeah, okay.
Yeah, I thought it was merged, but yeah, if you could confirm on this one, we are good to go.
Riccardo  Magliocchetti 00:14:58 Okay, thank you.
Ehhhhh Any other topic you want to discuss?
Carlos Alberto Cortez 00:15:23 There's a comment from Leighton, maybe Leighton we need to talk about that.
Leighton 00:15:30 Can you hear me?
Carlos Alberto Cortez 00:15:32 Yes, we can.
Leighton 00:15:35 Yeah, just… it was just a response to, what Ludmila was mentioning. It's probably the same PR that we were talking about, about the… Example comment.
I think we didn't have a strict… what's it called, Like, the only requirement for instrumentations being added was that we get, you know, component, like, ownership Like a indication that they will support it in the long run.
I think although native instrumentation is desirable, like.
I don't know if we were in the business of just rejecting people outright, just because they can't add it.
into native instrumentation, it does look like this person is the… part of the maintainers, I guess? So… was wondering… what we wanted to do in this regard, because it does seem like they're doing this in good faith, so… It was kinda… Backwards to me, just to be like, oh, we're not gonna help you because… you know, you're not considering native instrumentation, so…
Liudmila Molkova 00:16:43 I think criteria should not be, like, native instrumentation, was attempted, or, like, there are some blockers from doing this. It's more like… Are we happy with the current model of component ownership, where We… take random people on the internet. I'm sorry, I'm pretty sure most of them are acting in a good phase, but, like, once it's in this repo, and especially if it's a part of the distro, it's kind of maintainer's responsibility to Have this component to make sure it's reasonable and updated, and… There should be some, either criteria to take it in, or a criteria to take it out if the component owners don't, Follow the process, or are not responsive, don't… update the instrumentation. So what we end up with is that the bunch of instrumentations in repo are unmaintained, right? I… maybe a bit too harsh, but I think it's true.
And is it the good state to be in?
I actually, at some point, I want us to, like, do… have a conversation about how we reach stability, right? And I have some policy I want to propose to the SPAC around this, but I think we should not take instrumentations that we don't… not plan to have stable at some point in the future, that we don't have energy to drive to stability.
Leighton 00:18:19 Yeah, definitely, I'm empathetic towards what you're saying, and being one of the people who had to maintain a bunch of instrumentations that we don't understand, definitely, empathetic towards that. I think we had a brief discussion about this, like, a while ago, in which, like, we had a… we tried to… not enforce, but, like, definitely uphold a certain bar for what can be entered as an instrumentation. And then we did mention that, like, there should be a process for getting rid of them as well, if we had that same, you know, same bar. I don't think it was just fully, kind of, enforced, To get rid of them. I think… we all fully acknowledged that the maintenance burden was too much, and we were on board of getting rid of the instrumentations, but I don't know if, like.
The backlash and the optics were something that we were ready to… kind of deal with, or at least, like, the maintainers didn't have time. I'm just… maybe speaking for myself, I'm not sure if it's the same for Aaron Riccardo.
Yeah, but I think that was the historical reasons of… Why we were accepting them, but not really getting rid of them, so… Oh, sorry, some people have their hand up. Yeah, Diego, go ahead.
Diego Hurtado (Dash0) 00:19:46 Right, you guys can hear me?
Riccardo  Magliocchetti 00:19:53 Yep.
Leighton 00:19:53 Yep, I can.
Diego Hurtado (Dash0) 00:19:55 Okay, great.
Tom… there is, I mean, this approach of holding all these customizations in one single repo.
As always said, there are certain disadvantages, the… I mean, besides what you have all mentioned, the… We are upgrading them I mean, it kind of forces us to grade them in lockstep, which means… Some instrumentations get a new version without any changes.
And, and so on. I… the git history gets mixed, and… I don't think it's, it's a good idea.
To add more… Instrumentations.
Any person who volunteers to… Maintain, an instrumentation can disappear.
so… But I think the… We also have, A problem right now.
Which is the fact that, We are kind of stuck with what we have.
Not, releasing.
Any of our instrumentations anymore.
Can cause an issue.
Because of, the fixed dependency we have on… Oco, other… Proponents, being pathology instrumentation or semantic conventions, So… I would prefer to be safe, to… I have a strict policy right now that no more instrumentations are accepted.
it is also… a way to be fair, right? We are treating everybody the same.
So we just decide not to accept any any other instrumentation, because if not, the judgment tends to be subjective, right? If we decide to accept one instrumentation and reject another, I mean.
So, yeah, I agree with not adding any more instrumentations, With a very strict policy that is, on, we don't accept anymore, we support what we have.
But, we don't want to make the problem bigger, so… yeah, that's… that's what I would… Yes.
Riccardo  Magliocchetti 00:22:50 Okay, it's my end to… to say… One thing about the… The current limitation I see with the current model Is that, the component owners It's not working for us.
Because maintainers of a specific instrumentation, component owner of an instrumentation need to be in a group.
Of the very same repo.
We had, recently, like, an issue with the… Azure Resource Detector.
And we have a bunch of component owners now.
But they didn't get assigned automatically because we're not a member of any Python trip group.
And I think this is the first thing we need to sort out.
And then, an answer to Diego, like, I'm not sure that all instrumentation are created equal.
For example, I reckon recently we had, like, a user trying… wanting to contribute, the disk of the PIE package, instrumentation.
We said to them, well, this looks like something that's better shipped, with the library itself.
And the issue is there is that Yeah.
is that, like, for Discord, we don't even have a semantic convention for which kind of… Of stuff.
And on the other hand, well, Ludmila cited the HTTPX true.
But also, like, we have an anarchical biblical client from Lukas.
And, like, since Lukas is already an approver, I think if… It won't be the same.
Yeah… Regarding a component, Leighton, I think that… Buff.
Your colleague are, open Tammy members already?
So, like, regarding the complaint owners, I think we can maybe introduce the traging group.
And add the users there.
or just made approvers, I don't know, like… Bye.
Leighton 00:25:22 Even then, it's difficult with the current model, because, like, every random Joe that comes, we have to add them to a triage group. Seems kind of unreasonable.
So, your concern is still valid.
Even with that.
Riccardo  Magliocchetti 00:25:36 Yeah, like, it's… more my concern is just, like, what is… Annoying for them also to not receive notifications.
Leighton 00:25:42 Yeah, yeah.
Yeah.
Riccardo  Magliocchetti 00:25:46 I think Lududilmila was first.
Liudmila Molkova 00:25:51 I think Aaron Bush before me now.
Aaron Abbott (Google LLC) 00:25:56 Yeah, I can go, I was going to kind of second what you said, Riccardo, like.
I just wanted to call out the Gen AI situation.
of… like, there's kind of two parts to the contrib repo, and one of them is, like, governance, so having stuff in a repo in OTEL is nice because It's not just something somebody can change the license or lock down or whatever, and we're trying to build, like, a community, so… I do feel like we kind of need to take it on a case-by-case basis, and Same thing with, like, the PyPi package names.
I just… I can't help but feel like a lot of the feedback we got was, if Contrib was better.
we would have less divergence in, like, the GenAI instrumentations. We wouldn't have all these distros floating around, and people would have felt like they can contribute.
And, we would have, you know, some conformance, and we'd have ownership of the packages and stuff like that.
But I also hear you, Diego, like, I think the… the lack of guidance is probably a little frustrating for contributors, and maybe we could do, like, a sponsorship model or something like that. So, somebody, maybe we could say, like, an approver has to sponsor agree to be a code owner for some of the packages, for example. We could… Come up with some kind of… Guidelines or something that's not… leaving these PRs in limbo and not having a bunch of deprecated code sitting around either.
Liudmila Molkova 00:27:24 Yeah, I wanna…
Aaron Abbott (Google LLC) 00:27:25 what?
Liudmila Molkova 00:27:26 Yeah, thanks. I wanted to also second that we should use some judgment on which instrumentation to accept and which to reject.
And, like, people… approvers approving something is a good signal, actually, if you really want something to happen, if you, like, think I have a spike or whatever.
Discord is important.
you approve it, and maintainers also decide when to merge, right? This is the judgment. So we can kind of rely on the process, but we should also be up front with the, contributors, and, like, PR… this PR is sitting there for more than what 8 months.
it's de facto rejection, right? You just didn't say no, but it didn't change the fact that it's a rejection.
I think the whole premise of Oh, let's… Decide what we're going to reject is… it's useful, but, like, what can we do to make instrumentations maintainable?
at scale.
Like, how can we do better with the instrumentations we already took in? And I think there could be good things to learn from Java experience, and I can… I've talked to Trask recently to learn what they've done good.
maybe I should prepare some, I should prepare, and maybe some people want to help me, like, a plan on what to do for Titan, so it's more maintainable, and then… We are not just saying, okay, we cannot maintain what they have, what we have, we reject everything else, but more like, okay, we are currently trying to make things to scale us and make everything maintainable better.
And then, for this time, we are pausing on things that don't feel essential, but, like, we will decide on a case-by-case basis, but here is the plan and the timeline, maybe some, at least roadmap on, like, how can we get repo to a maintainable state.
Diego Hurtado (Dash0) 00:29:35 May I go?
Liudmila Molkova 00:29:39 Yeah, of course.
Diego Hurtado (Dash0) 00:29:41 Alright.
Okay, sorry, I think, I… I wasn't… clear… I'm sorry.
Okay, let's first define two groups of people. Group A and Group B. Group A is basically, us.
the maintainers, the approvers, you know, people who… Regular commit to this, prey, right? A bee is pretty much everybody else.
when I said, we reject any… other instrumentation, I mean, we reject any other instrumentation from Group B from now on.
Because if there is, a new instrumentation, sorry, a new library, for example, that it's important, and appears nowadays.
we… Or, I mean, group… someone from Group A can create that instrumentation, and I… If someone from Group B comes, with a… Available implementation.
Earl Ederson.
And says to Alec, okay, fine, it can be added, but… don't count.
on that person from Group B to be the maintainer.
Basically, what I'm trying to say is that We should, Consider everything that is in the contributory book, owned, and by people in Group A. That is the reality, right?
We should only have and add new solicitations if either people from Group A are the authors, or people from Group A can become the… delightful maintainers. The reason why I suggest to be strict when it comes to instrumentation from Group B is that we don't have… we don't want to… sorry, have this dilemma, right? To decide an instrument… an instrumentation from someone from Group B, And another miscommutation from someone would be, we don't want to be unfair, except one object, right?
So that, that's, that's what I proposed to Mark here.
Riccardo  Magliocchetti 00:32:19 Lukas?
Lukas Hering 00:32:23 Yeah, I'll be, I'll be quick here. My, just going back to the, the point on, like, not all instrumentations are really equal, I think, like, we should be able to factor in just general popularity. So, like, for example.
like, HTTPX is multiple words, it might actually be more popular than something like Aerospike. Like, just looking at the PyPy specs.
Aerospike has, like, tens of thousands of downloads a day, whereas, like, HTTPX has millions.
And even though we still need maintainers, like, there's, like, you know, a good chance someone might flake, but if, you know, if it's something super popular, chances are people are going to come back, too, and contribute and help maintain it, right? So… And I don't know if, like, like… we can't just say, like, oh, it has to have this many PyPy, you know, downloads, like, that's kind of arbitrary, but, like, I think it's, like, something to take into account, like… I think, actually, we did have a discussion in Slack on this, like, and something I pointed out is that, like, if we accepted it, it would be one of the lowest Popular packages that we support by download volume.
So, like, I mean… I mean, kind of that alone, like, and especially because, like, no one in the approver or maintainer group really is, like, has strong feelings on it. I don't think we should accept it, but, I definitely don't think, like, we should, you know, stop accepting new, contribute packages all together, like, it just… Yeah, I think… yeah, maybe updating the README to kind of summarize everything we've just said would be probably good, but I don't think there's, like.
One, like, deterministic formula rule we can… we can follow for everything.
Liudmila Molkova 00:34:14 They have trust.
Aaron Abbott (Google LLC) 00:34:16 Yeah, did we just summon Trask?
I don't know how this happened.
Trask Stalnaker (Microsoft Corporation) 00:34:21 Hello!
Leighton 00:34:21 I asked him… I asked him to join.
Aaron Abbott (Google LLC) 00:34:24 Oh, heh.
Leighton 00:34:28 That's the GC magic right there.
Trask Stalnaker (Microsoft Corporation) 00:34:31 the connections. Yeah.
Leighton 00:34:33 Trask, thanks for joining. Just for context, we're discussing a long-running PR that has had no traction for months now. It's like a, you know, an owner of a library that is not super popular.
We just wanted to know, how does… we're trying to learn from, like, what the Java repo has done in regards to Contributors, contributing instrumentations that… you know, might have the risk of, not taking ownership, as well as having some maintenance burden, as well as possibly never going to stability. We just kind of want to know, how do the job repository deal with this?
As well as the messaging.
Trask Stalnaker (Microsoft Corporation) 00:35:16 Yeah.
So… The Java has… we've split into two repos, right, so it kind of depends on the repo. We have the instrumentation repo, which is a little… which is… which is… Hands-on, managed by maintainers.
We have the contribib rep repo, which is modeled more like, I think the Python contribib and other contribib repos, where there's component owners.
In the instrumentation repo, since they're maintainer-owned, we're a little bit… A little bit more picky, Although we still, accept generally things that follow semantic conventions.
So, like, messaging, instrumentations.
you know, database instrumentations, HTTP instrumentations, were pretty generous as far as accepting those it is… I mean, yeah, there's a little bit of suspension of, like.
like, I do not know a lot about the… how Rocket MQ works, and how RabbitMQ works, and how I understand Kafka a little bit better. But, like, there's… a lot of things that I don't understand But… I… that I rely very heavily on tests, to be comfortable with.
With merging, and to be comfortable with maintaining, as a maintainer.
That's… kind of the… And for instrumentations that follow semantic conventions, right, there's… I kind of want to categorize these into a bucket, because they are… They're all fairly similar, they all have fairly similar tests.
That are needed, test infrastructure, you know, we're… we're… We have that… this new conformance testing repo, which is sort of… Based on that fact, but you could still, you know, do a lot, like, we have a lot of, Test infrastructure for those.
And we can check them against each other. I mean, part of the great thing with, I mean, AI is really good at if you've got other things in the same category of instrumentations.
Of checking those to see if things are aligned or not.
I think the one-off sort of contrib… things like SDK processors, you know, metric bridges, things like that are harder, so that's kind of where… I also think they're less… honestly, I think they're less valuable to user, like, as if we're prioritizing. I think the instrumentation that conform to semantic conventions are… A critical delivery of… Well, not… We would love to have native instrumentations of those, but in lieu of that, you know, open telemetry.
the concept of OpenTelemetry relies on people being able to actually use these instrumentations, and people are not going to instrument, you know, RabbitMQ themselves.
So, yeah, I mean, on the… this… Now, that, that does require maintainer time, I don't know how… you know, we've done a lot of work in the Java instrumentation repo around Sort of our agent instructions and, agent, sort of, we have an agent knowledge base of, sort of.
things that help us to, you know, get PRs into kind of a pretty decent shape, on its own before we look at that.
And then, really, what, we're looking at when reviewing those are, does it, you know, does… is there anything weird going on there, or is it pretty standard, like.
Here, create a span, you know, there's not some kind of weird… you know, global cache that could erupt, or like, I don't know, things that aren't kind of pretty standard for the repository.
And, you know, and the tests.
And if we'd… don't understand… Yeah, so… And then, you know, getting it out to users and getting feedback from users.
As far as if it's… Working out in the wild.
I don't know, that's a lot, let's… Let's hear what, kind of more specifically, where… where you all are… are kind of… having troubles, and maybe I can help guide the conversation, or provide stuff we're doing.
Digger.
Diego Hurtado (Dash0) 00:41:04 Yeah, thank you for… for showing up and helping us. Two straight questions, So, a problem that we have is that there is people that, are… willing to… Introduce a new contribution.
But we are not sure if we should accept that, because if they then disappear, it is… Our job to maintain that contribution. So… In that situation, has that situation happened to you in Java? And if it happened, what did you do?
That's a question.
Trask Stalnaker (Microsoft Corporation) 00:41:45 Yeah, so in the instrumentation repo itself, we do not do component owners.
So, basically from day zero, when an instrumentation is… when somebody proposes an instrumentation, the maintainers own that. So that has not happened there.
And we do have just, you know, a ton of instrumentations over there.
In the contribib rep repo, we do the component ownership.
Peace.
And… over there, you know, if something falls below… I think we've had a couple times where we have retired things, because people weren't interested, and, you know, we put out the call on the Slack channel for owners and whatnot, and nobody wanted to, so we did retire those.
In general, you know, Those components have been maybe not as… widely used as the components. The more widely used stuff tends to land in the instrumentation repo.
Diego Hurtado (Dash0) 00:43:05 Okay, so as far as I understand, you potentially have the same problem that we have. I mean, someone… in… that added a contrib in Java can disappear, and then you're left with the burden of maintaining it. And if that happens, I… from what I understand.
You may decide to retire that contribution.
Trask Stalnaker (Microsoft Corporation) 00:43:32 Is that right? Yeah, I think that's how all of the, more or less, all the, contrib repos that do the component ownership Function.
Diego Hurtado (Dash0) 00:43:44 Okay, that's great. Yeah, that helps, that helps a lot, make a decision. Something else I wanted to ask you.
when… how… If you retire one of these components, from the country repo.
Has that… Cost… Issues for people who used to use them.
Has that been a scenario you have faced in Java?
Trask Stalnaker (Microsoft Corporation) 00:44:13 So, I should probably, for folks who don't know, give some perspective here, is probably relevant, Whoever is, riccardo, can I share for a sec? Thanks.
So, the instrumentation repo, has the majority of… instrumentation. So, let's see, we've got 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13… 13 pages, you know, of… what's this?
At least 10, you know, plus per page, so we've got, like, 150 instrumentations in this repo.
Compared to… Contrib is really more, like, kind of some miscellaneous, stuff. It's gotten bigger, too.
Two and a half pages of… You know.
15 plus, so… You know, under 50.
So generally, I mean, the popular stuff lands in this repo, and so that's… and we have a… We have a pretty strict policy in this repo about dropping things.
So dropping support for older library versions, so for auto instrumentation, we almost never drop support for libraries, or even old versions in auto-instrumentation.
Because auto-instrumentation, at least in our users, tend to be, you know, there's a lot of people running old Java Enterprise Legacy Apps out there who need monitoring.
And the Java agent auto-instrumentation is very… Heavily used by those people.
So we… Rarely, very, very, very rarely ever drop anything from auto-instrumentation.
Library instrumentation, is where somebody actually compiles against it and brings it in, and so that one, we're a little more flexible with.
dropping older… we don't… I don't think we've ever removed support for a library here, but we have dropped Older version support in this case.
Diego Hurtado (Dash0) 00:47:06 Right, thank you.
Question. In… so, here in Python, we… Pretty much have, like.
two groups of people. People who are regular contributors to Python, maintainers, approvers, people who regularly show up, and pretty much everybody else. So I named these groups A and B.
So, the… The concern we have is not that someone from A, Brings in a contra… sorry, an instrumentation, right? The concern is that someone from Group B, someone who we barely know, right, brings a… A contribution, and then… this person may disappear. So I wanted to know if, in Java, does the same thing happen to you? Do you also have, like, a group of people who are regular and well-known, and a group of people that you don't know, and if this other group B of people in Java also contribute and bring in instrumentations, because maybe in Java, every instrumentation you have received has come from someone who is a regular contributor, so maybe you don't have this issue in Java, as we have here.
Trask Stalnaker (Microsoft Corporation) 00:48:25 We'd definitely get, both.
types, a example… This is, you know, first-time contributor, you know, at, New instrumentation, you know, it's non-trivial.
I… initially, like, this falls in some gray area for us, so I kind of, I pushed back a little bit initially, because there's not semantic conventions for circuit breaker instrumentations, but we do, in this repo, have two other circuit breaker instrumentations, and so I… We could have pushed back, I would have been fine on that, but I felt… I was like, okay, well, as long as you make it look exactly like these other two that we already have, then, you know, I'll have… I'll review it, and we'll accept it.
There's definitely both types, but I do think, you know, that, that's where the semantic convention limitation, you know, can help you, I think, because that gives you something to… baseline what is good instrumentation. Also, what is useful instrumentation, as opposed to having to, like.
decide ad hoc what even instrumentation should look like. That's very time-consuming. Just… Checking conformance of something, you know, is a lot… less burdensome.
Diego Hurtado (Dash0) 00:50:15 Okay, so what I understand is that if someone that you don't know in Java comes with a new instrumentation, but that instrumentation is compliant with semantic conventions and follows a certain structure, you will be okay with accepting.
Even if that implies the risk of this person then disappearing and you having to maintain it.
Trask Stalnaker (Microsoft Corporation) 00:50:39 For the most part, yeah. You know, I will check, like, oh, is this, like, somebody's personal Project, library that, you know.
has 10 stars and nobody's using, yeah, I mean, I'll push back on that, but, like, if it's, you know, relatively, reasonably popular, then We're accepting it.
And the whole… I mean, AI has made me more comfortable with doing that.
Just because, again, like, we can… It has reduced a lot of that burden of, comparing, again, with the conformant, like, checking conformance. Like, AI is very good at checking conformance to stuff. Like, I can ask it, to check conformance against the semantic conventions, things like that.
Diego Hurtado (Dash0) 00:51:42 Right, great. And just to confirm.
If, someone comes with a… with a… someone you don't know comes with a new instrumentation, and this instrumentation looks perfect, like, super compliant with semantic conventions, follows the structure we want, everything else.
and then this person disappears, you still have the… the opportunity to drop it if in the future, you don't find it convenient to keep maintaining it. That's also a possibility for you, right?
Trask Stalnaker (Microsoft Corporation) 00:52:17 Not in this repo. Not in the instrumentation repo.
Diego Hurtado (Dash0) 00:52:22 Okay, but in the other one.
Trask Stalnaker (Microsoft Corporation) 00:52:24 In the contrib repo, yes, but the instrumentation repo, which is, again, where most of our instrumentation lives, It's… we do, you know, dropping support for older library versions for the Java agent, for auto-instrumentation specifically, we have, we… have a very high bar, and we basically just never do it.
Diego Hurtado (Dash0) 00:52:51 Great. Okay, yeah, that's… that's very important for us, because, we don't have, like, a defined policy on how or… how to… Dropout instrumentation, without, causing issues. I mean, we are working on that. That's… that's a issue we have, but… Solving that issue is also important for the discussion. Thank you for your help. It, It really helps a lot.
Trask Stalnaker (Microsoft Corporation) 00:53:22 Yeah, let's go, got a couple of hands. Riccardo.
Riccardo  Magliocchetti 00:53:25 I have a question about your testing strategy, since you said, like.
you don't drop support for very old, libraries, versions. So, like, are you testing every version, or you have, The minimum, or max, or last version.
Trask Stalnaker (Microsoft Corporation) 00:53:42 Yeah, so we test… The minimum version and the latest version, always.
For all instrumentations.
So we have a nightly job that, you know, bumps the latest version, whatever the latest released version is, and so we find out if there's breaking changes there. And that's another area where, AI has made it a lot less painful to have these around, because if, you know, a new version breaks something in our instrumentation, it's pretty easy to have AI fix it. I don't have to dig into the weeds of, like, what was changed, where, who, why, what we need to do about it.
We do test a few in a decent number of cases. We test a few intermediate versions. Oh, actually.
So… we'd… We have this… yeah, we have a whole… some, other… thing we… it's called… we call it Muzzle, came from a term that Datadog, created, before we inherited this, or before we, started from their base a long time ago. What it does is, it does actually check every version of a library. It doesn't run the tests.
against every version, but it checks the API shapes in a way that tells us if they're Our instrumentation is relying on, anything that would… Not work in that version.
And that's a fairly complex… tool, and I don't know if, you know, it's very cool if you… can do something like that, but that… that gives us a lot of confidence in those intermediary ver… or at least gives us a decent confidence in those intermediate versions. And then there's certain times where we know there's, you know, problematic… Version bumps, where we'll test a particular intermediate version.
Riccardo  Magliocchetti 00:56:00 Thank you.
Head on?
Aaron Abbott (Google LLC) 00:56:03 Yeah, I was gonna ask about muzzle, because… Sorry?
Trask Stalnaker (Microsoft Corporation) 00:56:07 Yeah, let me… let me actually… we have some… I spelled it wrong. We have, some docs that I can share. Oh, I think, actually, I think it's called Safe De Mechanisms, yes.
And I can drop this into the… Hype on notes here.
Aaron Abbott (Google LLC) 00:56:30 Yeah. I mean, Trask, I think you're kind of aware of the… the stuff with Python, we're doing something similar where we monkey patch a bunch of internals, so, it's not… like, relying on version numbers isn't great, and I guess you have the same problem in Java, so I'll definitely take a look at this one.
Trask Stalnaker (Microsoft Corporation) 00:56:49 Yeah… Yeah, so I think here we talk about, the instrumentation test, the latest dependency tests, The muzzle compile time checks.
Runtime checks. Yeah, these are all our safety mechanisms for the Java agent, specifically.
Aaron Abbott (Google LLC) 00:57:13 Cool. We're almost out of time. I just wanted to ask one other question, which was specifically in those ones that don't have semantic dimensions, like you mentioned the circuit breaker instrumentation. What's… what is, like, the policy for breaking… I guess it's in this doc as well, but for breaking specifically the produced telemetry, so say, like, metrics, or removing trace attributes, stuff like that.
Trask Stalnaker (Microsoft Corporation) 00:57:34 Yeah, so in the 1X line, that Java agency used to just break telemetry, we made no promises about telemetry, Stability.
In the 2X line, we started getting… More serious about that, and at some point in the last… Well, maybe, like, when the stable by default discussion came up, maybe, you know, 9 months ago in OpenTelemetry, we, buttoned that, that we decided, you know, we were comfortable, we've been, you know, doing this long enough that we felt comfortable saying, okay.
We're just… we're gonna say yes for, stable artifacts. We do guarantee stable telemetry.
And we do… the Java agent is marked stable, which means that The majority of our instrumentation Then has stable telemetry.
What we've found that has worked really well for us is we have, like, we're working on the V3, 3.0, release right now. We have been for several months here.
And we have a V3 preview flag.
Which allows us to hide all of our breaking changes behind that.
And then… we don't even really care so much whether users are testing that. It's like, okay, yes, you can preview what 3.0 is going to be like, but really it's more for our internal bookkeeping So that when we do go to major version bump, all we have to do is, you know, switch that, you know, on, delete all the code that was hidden.
Previous… that is no longer relevant.
Aaron Abbott (Google LLC) 00:59:34 Yeah, I… I feel like some of the stuff isn't one-to-one, because in Python, the line between, like, manual and auto is a bit blurred. We can just, you know, we don't have, like, this bytecode step where things need to be loaded as an agent, so we don't necessarily ship, like, a… single agent, right? So,
Trask Stalnaker (Microsoft Corporation) 00:59:52 We do ship individual library instrumentations,
Aaron Abbott (Google LLC) 00:59:56 Yep.
Trask Stalnaker (Microsoft Corporation) 00:59:56 as well.
And those, we haven't marked those stable. I'm trying to get a bunch of those marked stable for 3-0. But, they produce stable… Telemetry, just by the fact that they're used inside of our auto instrumentation, but we haven't been… ready to commit to the API shape.
Aaron Abbott (Google LLC) 01:00:23 Yeah, yeah, I feel like that's where some of our pain is coming from.
Yeah, thank you so much, Trask, really appreciate it.
Trask Stalnaker (Microsoft Corporation) 01:00:33 Yeah.
Yeah.
Great, that you all are going on this journey. I know it's a tough and a long one, but yeah, happy to, join Discuss more.
Liudmila Molkova 01:00:46 Thank you.
Aaron Abbott (Google LLC) 01:00:47 through I ought to.
Diego Hurtado (Dash0) 01:00:50 Here, y'all. Bye.
