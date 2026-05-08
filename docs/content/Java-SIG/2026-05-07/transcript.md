SIG: Java SIG
Date: 2026-05-07
Duration: 44 minutes
Zoom Recording URL: https://zoom.us/rec/share/yXzqcGE88Jj4wGchFCYJn_Tv-rFNTU5PFdhiwcsc9EWTgupmKXaP1HYs6fDQqy04.Gx4vA4qs_9HcDQUs
============================================================

## Zoom Recording Transcript

**Trask Stalnaker** 01:21 Good morning, John.
And… And everyone, hey.
**John Watson** 01:32 Morning.
**Bruno Baptista** 01:35 Hello?
**Trask Stalnaker** 01:37 Hey, Bruno.
**Gregor Zeitlinger** 01:55 Hello!
**Trask Stalnaker** 02:48 Alright, it is May 7th.
Let's kick it off.
Jack.
**Jack Berg** 03:10 Okay, so… the must-haves. So… Let me just back up, I'm just kind of getting my bearings here. 1.62.0 releases tomorrow. Must-haves and wish lists. There's a must-have, which is… Okay, I… There's a moderate-level security advisory that we need to fix, and it's debatable whether it's an advisory or whether it's a bug fix. And I have a fix out for it out on a private fork right now, and I need… I need somebody to take a look.
**Trask Stalnaker** 03:51 Probably easiest for me, since I have permissions already.
**Jack Berg** 03:56 Yeah, maybe. I don't know…
**Trask Stalnaker** 03:58 John, I think John… Should have permissions now that we bumped.
Y'all to admin…
**Jack Berg** 04:07 Yeah, and can you confirm my understanding that, like, when it's the maintainers that are added as collaborators on these advisories and not approvers?
**Trask Stalnaker** 04:18 Correct. It is maintainers that are added as collaborators, But that… sadly, that… Doesn't give you permission to… See the… the private floor.
**Jack Berg** 04:35 Oh, the collaborators don't. Who has permission to see the private force?
**Trask Stalnaker** 04:39 admin… well, maybe clever… I don't know, we had some problems, the Go folks had some problems, the GitHub permission model is… is… doesn't support us well. I actually brought this up. I was in a GitHub Virtual Summit earlier this week, and I actually raised this specific concern, because you basically have to be an admin on a repo to be useful… to have useful security Triage… permissions.
**Jack Berg** 05:16 Yep.
**Trask Stalnaker** 05:17 And the OpenTelemetry model had… doesn't really… I mean, we've tried to limit Admin… number of admins on repos.
But it's really failing.
Now, and so now we're basically going back and saying, hey.
Maintainers can have admin rights just because… They have to, in order to be func… in order to function with the security advisories.
**Jack Berg** 05:47 Yeah, else every… all the security advisory flow has to be delegated to the TC.
And with the uptick, because of AI, it's just not practical to…
**Trask Stalnaker** 05:59 Yeah, and we want… We want maintainers to own The stuff for their repos anyways, so… It's weird to have a central… security authority in our model. I know in other models, obviously, it works.
**Jack Berg** 06:23 Yeah, so, you know, coming back to this issue,
**Trask Stalnaker** 06:27 You…
**Jack Berg** 06:28 I'm trying to speak in code a little bit, because I just don't know how much I can reveal about this, and it might be, honestly, so close enough to the release tomorrow that I can just make the PR against the public repo. We review it, merge it, and… and release it.
Because that's ultimately what we have to do, right? It's like, we do have to open a PR against the public repo at some point, we just want to minimize the amount of time between the amount of time, like, where we, you know, have this PR open and before we publish.
**Trask Stalnaker** 07:00 Yeah, I think you can… Merge it… Direct… I… We're all learning. A…
**Jack Berg** 07:11 We don't have many advisories in the Java repositories, so we gotta kind of learn how to do this, develop the muscle.
**Trask Stalnaker** 07:18 Well, and the whole private forking aspect… Because we've had advisories in instrumentation, but basically my… my take has been if it's not a high Then… there's not a need to… Keep it.
Private.
It's just gonna go into our next minor release.
Maybe that's… not… Ideal.
So yeah, we have not done much with the private forks.
**Jack Berg** 07:56 So my take on it was, like, that's a good distinction between high and moderate, anything lower than high. But, you know, I was thinking that, like.
Let's say we find out about a moderate security advisory, like, a week after our last minor release. And it's like, we decide that because it's moderate, we don't want to… because it's moderate, and because it's existed for a long time, we don't want a patch. We just want to, like, you know, get this fix in and publish it with the next minor release.
Even though it's moderate, I would… I still feel like we shouldn't, like, publicly disclose it, or we should minimize the amount of time that we publicly disclose it, and so, where I think that the private fort comes in handy is, like.
it can get a review preemptively, such that once… once it's, like, a day or two before the release, it's like a rubber stamp PR and merge into the actual main branch. And then, you know, maybe just the day of the release or something like that.
open the PR with the, you know, against the actual main, rubber stamp it, merge it, release it. And, like, it all happens in quick succession.
**Trask Stalnaker** 09:16 That makes sense to me. I'm just trying to understand if… I think you might be able to merge… I'm not sure what the ideal… what the… designed approach for these private forks are if it's designed to merge directly into main, bypassing PRs.
But right now, I'm… I have another window open, I'm looking at the… your… PR, and of course, there's GitHub status problems, and merge status can't be loaded, so I can't even tell, like, what's… what's the correct flow? So why don't we take this one offline, and… I'll help you get it in.
**Jason Plumb** 10:02 So…
**Jack Berg** 10:03 Yeah, and I just thought it was interesting to talk about, because it sort of, like, creates a precedent that we can follow for future issues. I don't think this… like, we're actually working on… Pablo from the GC is working on clarifying our stance on, you know, the distinction between advisories and bug fixes. Like, it matters, kind of, because there's this gray area on whether something is just a bug or is actually vulnerability, especially in, like, this sort of… space of denial of service, excessive resource consumption. And, I think with Pablo's proposed revised stance, that this wouldn't even be an advisory. This would just be considered a bug.
And… Go ahead.
**Trask Stalnaker** 10:47 I disagree with this particular one, but since we're trying to not… Talk about what it is, actually, or let it.
**Jack Berg** 10:56 Yeah, okay.
**Trask Stalnaker** 10:56 got offline… Jason, yeah, sorry.
**Jason Plumb** 11:00 I was just gonna say that, like, I thought the way that the RMI one was handled was… I thought that went pretty smoothly, like, the PR went in… there was no disclosure that was explicitly part of the PR. Like, if you read it, you might… like, if you were educated, you might realize that that was fixing something very critical, but it, like, it was just a pretty…
**Trask Stalnaker** 11:18 vague.
**Jason Plumb** 11:19 Yeah, and I mean, I feel like that does enough, and there's probably plenty of other PRs that if you really scrutinize them, are fixing something that, you know, is potentially a security problem, but… I feel like there's a way to, like, probably do the PR without it being explicitly a disclosure.
**Jack Berg** 11:38 Yeah, and I think you do have to do that, because ultimately, at some point, you need to have a PR to the main branch, but I think, you know, in the case of the RMI one, that was high.
And so, it was significant enough that we released a patch as well, right? So, like, I think in all cases, you should open a PR, have it be vague and, like, non, you know, not disclosing, and you should do it in such a way that there's, there's a release coming with that in… soon.
**Jason Plumb** 12:09 Yeah.
Yeah, especially for moderate, that seems completely reasonable to me.
**Trask Stalnaker** 12:19 Cool, alright. So, Jack, I will help you get that in. We'll figure it out.
**Jack Berg** 12:25 Okay.
**Trask Stalnaker** 12:25 We can do a post-mortem next week for, Everyone else.
**Jack Berg** 12:35 And of course, I have a wish list of things that I'd like to get into the release, but are, you know, not time-sensitive. So… just… I don't want to spend too much time on these, but I can if we need to. We have a light agenda. But, Tras, we had this, this conversation a while back about this performance optimization I made that basically traded concurrent performance or contention performance for, you know, single-threaded, no-contention performance on metric recording. This one kind of takes a different approach, and it moves the place at which delta metrics need to coordinate between the record threads and the collect threads. There's, like, this atomic long, or an atomic integer, which needs to be incremented and decremented, and it's at the instrument level right now, which means that all series for an instrument need to increment and decrement this… this atomic integer, and that… that's the… that's the hotspot, that's the contention point.
that limits performance. And so… you know, in this implementation, I… shift things around so that each unique series has its own atomic integer, and so that reduces contention by striping it across the series. And it… because of… Because of some things, there's no performance compromise for this single-threaded or no contention case, and there is a performance benefit, although more modest, for the contention case.
And anyways, I don't know, maybe we should punt on it for this release, because it is kind of complex code, although I am quite confident in the tests and asserting the correctness of all this, but, yeah.
**Trask Stalnaker** 14:28 Cool, yeah, thanks for the, the overview. Thought.
Mix… sense.
why, did you do… Have a feeling for why it didn't… Get as… so, when you say striped, before it was doing real, like, striping at the, like, for multi-threaded, kind of that, striping.
this… You used the word striping, but this is just… Is this still being striped across threads, or this is… just only…
**Jack Berg** 15:12 each time series gets exactly one atomic integer, and before, the entire instrument and all of its time series got a pool of atomic integers. And so, if you could imagine, the differences is that, like, with the other version, let's say there's only, like, Let's say there's only one series within the instrument. That one series could have its record threads striped across the pool of atomic integers.
And in this case, this alternative approach, you know, that one series only still has one integer, one atomic integer, and so if multiple threads are recording to it, it still is the, you know, the bottleneck.
So its performance ceiling is lower, but it is still an improvement.
**Trask Stalnaker** 15:56 Okay, so if you're basically hammering one particular time series, it only… it doesn't really help, because you've just moved the lock in different places, but if you're hitting Multiple time series, then yeah, it helps a lot.
**Jack Berg** 16:13 That's right.
**Trask Stalnaker** 16:15 Nice Guidance for not checking…
**Jack Berg** 16:27 Yeah, so this is the thing that we talked about, I think, a couple of weeks ago, and we came up with this pattern to… That is merged now, where we want to put these types of APIs, which are for our own internal consumption, but need to be public to avoid the diamond dependency problem, or to at least reduce it and not continue extending the scope of that. We decided to put them in the Impul package, and that's, like, a new pattern that we have.
And so this is, like, kind of the first usage of that. It, like, it proposes adding this new API usage logger with the semantics that we talked about, where, the f- The first time it's ever called, it emits a warning log, and any subsequent time that it's called, it's gonna emit a finest log, and the first warning log, which is emitted exactly once, or zero or one times, contains information on how you can turn on more detailed logging at the finest level to discover more issues about this. So that's what we talked about a couple of weeks ago, and this whole API now is in this impulse package.
So, yeah, I haven't gone so far as to, like, going and applying this everywhere.
This is sort of like establishing the guidelines for where we do null checking, and promoting the API usage logger to this new location, and then a subsequent PR would go and apply this everywhere, and that's gonna touch a lot more things.
**Trask Stalnaker** 18:12 Cool. That one looks simple enough. I can… Probably look at that today.
**Jack Berg** 18:18 It's, again, this is a wish list, so, yeah, don't… If you have time and interest.
Take a look, but… And then OSGI support, this is…
**Trask Stalnaker** 18:30 I don't have time or interest.
**Jack Berg** 18:32 It's ready, if anyone just wants to rubber stamp it.
Anyways, I, that's available if we ever want to, make that happen.
**Trask Stalnaker** 18:48 How do you feel about the test coverage?
**Jack Berg** 18:52 That's coverage is, so… OSGI is similar to Graal in the sense of, like, you know.
you need to test different combinations of our artifacts being present to fully exercise… to have full confidence that things will work, right? Because, like, just to make this concrete, like, if you just use the API and the SDK, maybe everything works.
But if you include AutoConfigure, which relies on SPI in some reflection, maybe you haven't included the right, you know, dependencies or metadata in order for OSGI or GraalVM to work with AutoConfigure. And so, you need to sort of test the different combinations of packages that our users might have in order to, like, gain full confidence that you are exposing the right metadata to work for these various scenarios. And so, I don't want to test all those combinations right now. I'm just, like, establishing the base, and then I want to add different test suites in a follow-up to, you know, account for these different cases.
**Trask Stalnaker** 20:00 Awesome, thank you, Gregor. Any feedback from… Folks who have been requesting the OSGI support?
**Jack Berg** 20:14 Are you asking me, or,
**Trask Stalnaker** 20:15 Yeah.
**Jack Berg** 20:16 Yeah, there was feedback, and and it's all incorporated.
**Trask Stalnaker** 20:21 Okay, so, okay, awesome, awesome.
**Jack Berg** 20:27 Yeah, they were… they were pretty helpful, so I think they're… I don't know, I wouldn't say optimistic or excited about this, because it's been so long, but I think they'll be happy when it's done.
**Trask Stalnaker** 20:45 All right, let's move on. Gregor.
**Gregor Zeitlinger** 20:56 Yeah, not much, more than… a friendly ask. I remember that you were aiming for April, but I haven't heard it, A lot in the last meetings.
So… What's the current idea?
**Trask Stalnaker** 21:14 For a few months now, I, I, it's been first half of the year, so… I'm… still hoping for that, so I'm thinking… Mmm… That would mean… Ideally, it would mean an RC in June, but that's maybe ambitious, so maybe it's RC in July.
**Jason Plumb** 21:40 There's 24 issues in the milestone.
**Trask Stalnaker** 21:45 Of which we could defer some.
The big one that I want, the biggest one that I want is the database semantic convention stability.
And that's… mostly… Done.
So, basically, yeah, just, I guess putting everyone on notice. If there's anything that you want in 3-0, get it in soon.
**Jason Plumb** 22:15 Yeah, I kinda want that JMX one.
**Trask Stalnaker** 22:19 What's the JMX one?
**Jason Plumb** 22:21 Just to prefix the thing with experimental for the ones that are non-stage.
**Trask Stalnaker** 22:24 Oh, yeah. Yeah, yeah.
**Gregor Zeitlinger** 22:27 I mean, would it make sense we go over the dashboard so that everyone sees, oh yeah, maybe I have this one, or do you want to do it.
**Jason Plumb** 22:36 So, just…
**Gregor Zeitlinger** 22:37 to, Events.
But we have a last-minute rush before the release.
**Trask Stalnaker** 22:47 Let's… we've got… what do you… Gregor, do you think the milestone or the project is better?
**Gregor Zeitlinger** 22:54 That's why I asked you, because I don't know…
**Trask Stalnaker** 22:59 I usually…
**Gregor Zeitlinger** 23:00 I haven't look at it in a while, so that's why.
**Trask Stalnaker** 23:02 I usually put both of them on things, because I don't know, Well, let's see, so, all the indie stuff, we've got, yeah, we've got Sylvain here, so I know that y'all want… to get the invoke the indie stuff in, so… Let's see… I rename… Okay, this… Jason, you brought up… The RPC SimConv, we are… May or may not happen, by the release, I'm excellent. I figured that out.
**Gregor Zeitlinger** 23:49 working on it, and at the moment, I thought someone else wanted to take over.
How… how's that?
**Trask Stalnaker** 23:57 Oh, more I mean, we have not declared semantic conventions RPC as stable yet.
Okay. We declared it as release candidate, but we are currently… negotiating with the GRPC team.
To figure out, if, how we can align with them before we market stable.
This… Also, is another case that hasn't actually… stabilized in SEMCONG for reasons, so it may or may not happen in 3.0.
Because of that.
I guess the declarative configuration stuff, Gregor.
All of that stuff, whatever's left, probably worth doing a pass.
And if there's anything… remaining there.
taking care of it, but I feel like it's in pretty good shape. I know there's the distro stuff that there's a couple of open PRs for that, I think Robert And you are both looking at.
**Gregor Zeitlinger** 25:18 Nothing, really big, so nothing concerning, I would say.
And we have decided that we don't want to make DC default, so that also alleviate some pressure.
**Trask Stalnaker** 25:47 Yeah, yeah, so we may just push some of these things to be more forgiving on, like you said, not making it the default, not it will be a stable option for people to use declarative Config.
But we may not be… Aggressive about, kind of, deprecating other options.
**Jason Plumb** 26:18 It's been so long since, too. Is the release process set up to do RC?
**Trask Stalnaker** 26:25 I don't even think we did that.
RC for two, I think we…
**Jason Plumb** 26:30 Yes.
**Trask Stalnaker** 26:31 We'll do, like, a two-dot whatever and call it RC.
**Jason Plumb** 26:39 Okay.
Yeah, I'm asking selfishly, because in Android, we did not have a good process of doing a release candidate. It was… it took a lot of… it took more effort than I wanted to.
I wish it was smoother.
**Trask Stalnaker** 26:52 Jack, did… I forget, did… You all did a RC.
But that was, like, a one-time thing.
**Jack Berg** 27:00 For a core.
**Trask Stalnaker** 27:01 Yeah.
**Jack Berg** 27:02 Yeah, we did RCs, I think, back when, When metrics was stabilizing, and maybe when tracing was stabilizing.
**Trask Stalnaker** 27:13 And you did the actual dash RC thing?
**Jack Berg** 27:16 It… we did, and it was… it was Honorag that was, running the releases at that time.
And so, I'm pretty sure that, like… and also, we didn't have all of this release automation that we have now, so things have changed considerably, but I'm pretty sure he, he was manually intervening in that.
**Jason Plumb** 27:38 Yeah.
**John Watson** 27:39 Also, if I recall, we don't… we didn't… like, basically, there was no… it didn't buy us anything. Like, nobody actually picked it up and used the RC and tested it out, so the value of it was actually pretty small.
**Jack Berg** 27:54 I would recommend, like, just doing a minor release and calling it an RC.
**Trask Stalnaker** 28:01 And we do have that nice new, V3 preview flag.
Which basically… gets people the 3-0. It's kind of like RC.
Switch this table, some.
**Gregor Zeitlinger** 28:20 Sorry for the last one.
schema generation, that was… Oh, I missed it.
created under the assumption that the default would switch, so it would actually be more a 4.0. I don't know if you wanna… have… A milestone for that already.
**Trask Stalnaker** 28:38 Schema generation for spring starter. What does that…
**Gregor Zeitlinger** 28:45 It means that the auto-completion in spring suggests the new style, and that would only make sense if this is a default.
**Trask Stalnaker** 28:53 I see.
Yeah… Probably we need to, I think we need to get… I'm not sure we'll have time to push on getting the declarative configuration instrumentation node.
Things stabilized.
Which I think would be a prereq for all of that.
So, that…
**Gregor Zeitlinger** 29:24 Yeah, I'm not contradicting, I said this would be 4.0, and we should just reflect that.
Should I create the milestone, or is that overkill?
**Jack Berg** 29:36 4.0 milestone.
**Gregor Zeitlinger** 29:38 Yep.
**Jack Berg** 29:39 Might as well.
**Trask Stalnaker** 29:41 Yeah.
against it, I, I'm… I think we're good with doing… it has been a while since the 2.0 release, But in general, I think yearly majors… Alright, good thing.
And a year will fly by.
**Gregor Zeitlinger** 30:07 Sure, bud.
**Trask Stalnaker** 30:09 Some of these are pretty, some of these we could implement now, by just, if we just hide it behind the V3 flag.
Then, when we are ready, we'll just automatically Strip out all that stuff.
**Gregor Zeitlinger** 30:31 That's actually a good reminder.
**Trask Stalnaker** 30:34 Yeah, yeah, this would be another good one, probably easy one to… implement… Because it's just, opt-in flag on the SDK, I believe.
Yeah, so some of these are pretty easy, we've just kind of… Delayed them because of the braking change nature, but we can… Now… send PRs for them.
In the… DB… stability… Simple braking.
Yeah.
So yeah, there's definitely some… reasonably straightforward things that, if people want to send PRs, you know, add them behind the flag.
That would be awesome.
**Gregor Zeitlinger** 31:53 Does this really work for everything, or is this a case-by-case?
Thing, just to get the right expectations.
**Trask Stalnaker** 32:03 I mean, it works for a lot of stuff, for sure.
**Gregor Zeitlinger** 32:10 I would…
**Trask Stalnaker** 32:12 say, most of the things it works for. What it doesn't work for is breaking API changes.
Oh, yeah, yeah, thanks, I'm glad we went over that. Yeah, I… I think… yeah, let's plan on, let's plan on June being the RC… And July being 3-0.
I feel like that's… Currently.
**Gregor Zeitlinger** 32:47 Do you think it's a good idea if maybe every other week we go over that, just to keep… The momentum building?
**Trask Stalnaker** 32:54 Probably every week, that's a good… yeah, I'll dump that into our template, not that we… Our template, yes.
**Gregor Zeitlinger** 33:14 Correct.
**Trask Stalnaker** 33:16 Alright, Jay, do you want to share?
**Jay DeLuca** 33:21 Yeah, there's nothing to share, I was just more of an inform, but yeah, the site's LLM-enabled now, so basically we have like, special indexes for the LLM to discover and then, crawl the information.
I was experimenting with it a little bit, earlier. This isn't the… It's, it's explorer.openslemetry.io.
But yeah, I was exploring, experimenting with asking, like, ChatGPT specific questions, and then it did terrible, and then I told it, reference this, and it got a lot more information, so it's still not perfect. I think I ran it against some score, and we're like a B-plus or something.
At the moment, but yeah.
**Trask Stalnaker** 34:11 How does this work?
**Jay DeLuca** 34:14 Which part?
**Trask Stalnaker** 34:14 like, the whole LLMs… I've seen the… I've seen the LLMs.txt, but, like, how does the… do… do agents just know to look for that, or you have to tell it to look for it, or…
**Jay DeLuca** 34:30 Both. So, like, a lot of agents will know to look for this LOMs.txt as kind of the landing page, as, like, the… I don't know if it's a protocol or what, but… but we also have an edge function that, does some content negotiation and looks for user agents and will kind of guide them to the right place and set the right headers and stuff like that. So it's… it's a little bit of both.
**Jason Plumb** 34:56 Kind of analogous to robots.txt.
**Jay DeLuca** 34:59 Exactly, yeah, we updated something in robots.txt to point to this as well.
**Trask Stalnaker** 35:07 Nice, so if I ask… so I… I would still need to tell my agent to… I'd still need to point them to this…
**Jay DeLuca** 35:17 Now, yeah, until… I think until it ends up in the aging zeitgeist. Trading model. Right, right.
But yeah, so I was just gonna say, like, as you guys are doing your stuff, if you're… if you're ever doing anything that has to do with, like, understanding the telemetry, I'd say give it a shot, let me know if you encounter any issues or anything, we can make it better, but…
**Trask Stalnaker** 35:45 Jason.
**Jason Plumb** 35:46 So… people… I mean, at least internally, people ask about this stuff a lot, and so, like.
I always have to go and decode, like, the second Wednesday after the third Monday, like, that weird scenario. So I… this might help you to not have to do that. It's pretty stupid.
**Trask Stalnaker** 36:04 Love it.
**Jason Plumb** 36:05 Yeah.
**Trask Stalnaker** 36:07 Except I should really probably just change this to Friday-ish, because… I rarely get it out.
**Jason Plumb** 36:14 window.
**Trask Stalnaker** 36:14 day.
**Jason Plumb** 36:15 I can have.
**Trask Stalnaker** 36:17 Although…
**Jason Plumb** 36:18 There's hopefully enough… there's hopefully enough disclaimer in there that's like, these are not firm dates, but… Yeah.
**Trask Stalnaker** 36:26 I don't know if I shared… I forget if I shared already the… Release… No, what is it? Yes.
Workflow… Release nodes.
Where's the good stuff?
Run, oh yes.
**Jason Plumb** 37:03 Oh yeah, what does this do again?
**Trask Stalnaker** 37:06 So, it, classes… so… it looks over all the PRs, because our PR titles.
**Jason Plumb** 37:16 tend to be hard.
**Trask Stalnaker** 37:16 horrible, and.
**Jason Plumb** 37:17 Yeah.
**Trask Stalnaker** 37:18 I have always, like, gone through and kind of manually massaged them, and often have to read the PR to see what it's about, and see what it matches.
So, this… pulls all the PR data, classifies them, basically, whether it should be, a bug, enhancement, a breaking change.
And then it creates a… a nice… Tech… a nice title for it, based on what it actually does. Like, it actually looks at the diff.
And it's cool, because it actually, like, works well with the mini models.
Cool.
**Jason Plumb** 38:05 Boom. Did you use it for the last one?
**Trask Stalnaker** 38:08 I did. I built it in process while.
**Jason Plumb** 38:13 Yeah.
**Trask Stalnaker** 38:13 the last one?
**Jason Plumb** 38:14 Cool.
**Trask Stalnaker** 38:15 So this next one will be the first one where I get to actually, hopefully, benefit from it.
**Jason Plumb** 38:24 Yeah.
**Jay DeLuca** 38:24 Port this over to Contrib, too.
**Trask Stalnaker** 38:29 Yeah, go for it.
I can add, I'm happy to add my, Token to the secrets there.
**Jay DeLuca** 38:38 Cool.
**Jack Berg** 38:44 Wait, so, I do this via a skill right now. You're doing this, like, as part of CI?
**Trask Stalnaker** 38:51 Well, for now, it's a… I have a, I made it a… Workflow, just so that other people could trigger it also.
But… The reason why I… like this is… the pattern that I found works really well is having, having a deterministic step download all the information that it's going to use to make decisions, so download the PR diffs, download, the conversation history and the PRs.
And then point the model Add it.
And also, what I found is it helps to do that… do the inference one by one on them, versus, like, if you do have a skill, like, it tries with… at least with the instrumentation repo, we have, like, 400 PRs, and so it tries to be clever and shortcut.
And so it tries to overgeneralize and doesn't actually look at all the data.
So, this… actually loops, and… asks.
to do the inference, basically, on each PR one at a time, and that has… that gives me much better results.
**Jack Berg** 40:19 Yeah, I designed some skills like that to have, like, a script component, which, like, kicks off other agents to do some sort of iterative thing so that they can each have fresh contacts, but, It can… it can be kind of convoluted.
**Gregor Zeitlinger** 40:34 I, I found that… there's at least one tool that I stumbled across that does this, also. Just put it in chat.
**Jason Plumb** 40:44 Tras, that workflow, does… what's the output like? Does it… does it actually… Commit something back to the repository, or does it just display it?
**Trask Stalnaker** 40:53 I think it opens the PR.
**Jason Plumb** 40:55 Okay.
Cool.
**Trask Stalnaker** 41:12 We'll see.
Oh yeah.
**Jason Plumb** 41:15 Nice, yep.
**Trask Stalnaker** 41:16 Fantastic.
We will see that part. I did not. Oh, actually, I can run this anytime, yes. I remember, I did test it after, like, a week after the release, once there was a few, because we can actually run it like, early.
And, yeah, just so it did actually produce… let's see, did it… is there a label? Probably not.
What's the title?
Yeah, so this was my test of it.
And so, I have been adding… Or rather… My agent has been adding, to the changelog when I've done PRs.
For breaking changes stuff.
So that's why there's existing stuff in there.
I did instruct the… Draft release notes to basically overwrite all of that, but, then it's there so that we can kind of then review and double-check it.
But I still liked that.
**Gregor Zeitlinger** 42:50 So, it makes sense to put stuff in a changelog?
As input.
**Trask Stalnaker** 42:54 I'm… break, the breaking changes stuff is, I think, worth adding there, just, but it's really okay if you don't. It seems to do a good job of detecting that.
I don't know, my agent just seems to want to put stuff in there, whether I want it to or not, so I haven't been removing it.
**Gregor Zeitlinger** 43:17 I mean, you could, just, add to the knowledge base however you want to have it.
**Trask Stalnaker** 43:24 Yeah.
So, we'll see. Maybe… might change.
my mind on that Cool. Any other topics?
**John Watson** 43:51 I'm gonna be gone for a couple weeks.
Oh, I'm going to Europe for a couple weeks.
**Trask Stalnaker** 43:59 Bye.
Have fun. Enjoy.
**Jason Plumb** 44:05 You're gonna miss all the fun back here.
**John Watson** 44:07 I'll get different fun in Europe.
**Trask Stalnaker** 44:13 Alright, well, I'll see the rest of you next week, then.
**Jack Berg** 44:18 See ya, take care.
**Gregor Zeitlinger** 44:19 dear?
**Pranav Sharma** 44:22 Bye-bye.
