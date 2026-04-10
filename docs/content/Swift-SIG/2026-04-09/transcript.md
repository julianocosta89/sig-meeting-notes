SIG: Swift SIG
Date: 2026-04-09
Duration: 58 minutes
============================================================

## Zoom Recording Transcript

**nacho** 01:42 Hi, Nina.
Bye.
**Vinod Vydier** 01:45 Hey, Nacho, how are you?
Yeah, we've not been having very regular meetings.
With… I mean, we have… having very short meetings, I'm sure.
**nacho** 01:56 Yeah, I, I know. I mean, yeah, the product, for me, has been basically the, the time, the summertime change that made Dismitting into my work.
**Vinod Vydier** 02:09 So one hour difference makes a lot of diff… yeah.
Changes, yes.
Well, you guys also have, actually, time change, right? Change.
**nacho** 02:24 We've had it before. No, we had it later. So we had that just before Eastern.
**Vinod Vydier** 02:32 Hmm.
**nacho** 02:33 And last, last week, it was, it was holidays here. But yeah, we had just the weekend before, and that.
**Vinod Vydier** 02:42 Because there are some countries that do not have this, and it becomes really… Confusing.
**nacho** 02:48 Yeah, yeah, and we have, like, a difference, sometimes 2-3 weeks.
That make me…
**Vinod Vydier** 02:53 Yeah, it's very confusing.
They should know, they're talking about getting rid of it, but, I guess… Hasn't happened yet.
You might get… there is a legislation to remove.
**nacho** 03:13 That's it.
Classical.
take that… politics use.
To… Make you talk about other things.
Not the real product, usually.
**Vinod Vydier** 03:26 That's true, yeah, yeah.
**Ariel Demarco** 03:32 Hey, guys.
**nacho** 03:35 Hello.
**Vinod Vydier** 03:36 Hey, hey.
**nacho** 03:40 Yeah.
Okay.
Yeah, we are fairly young.
Do they hear?
I've been, I've been out, for a period, so, I… do you want me to… To lead it, do you want to do it?
Artie?
**Ariel Demarco** 04:07 If you can, I'm… I'm driving, I'll be.
**nacho** 04:09 Oh, okay, okay.
**Ariel Demarco** 04:10 But, wanted to join.
**nacho** 04:12 Okay.
That's the case. Yeah, then let me… Yeah, I will.
I will change.
then things… Okay, so, let me say… Spring… Okay, yeah, that peaks… The referral topics here are open, sorry.
There is a release 2.4.1, This comes from 26th of March.
Because it was merged, 1PR, and we had to… rerun… it would rerun all jobs in Autel Swift after releasing two for… 1.
Was that released?
**Ariel Demarco** 05:17 I just finished some fixes in CI. Okay.
And… Okay.
I think both you and Bryce approved the PR.
But I had to make some changes in the way we use the build and test workflow.
**nacho** 05:33 Okay.
**Ariel Demarco** 05:34 basically, it was failing because macOS runners sometimes have some… some devices, sometimes they don't, and it was, like, super painful, because I was fixing one error, and sometimes another error appears.
So, what I'm doing now is basically list the devices, I gather the latest device that we can test.
And use that one to… to run the VLAN test, basically.
**nacho** 06:02 Okay.
So you're always using the latest, right?
**Ariel Demarco** 06:06 Yes.
**nacho** 06:07 Instead of a fixed device. Okay. Exactly.
Yeah, that makes sense. That… that has always been very, fragile with… with… with Yitav actions, yeah.
**Ariel Demarco** 06:21 Yeah, but I don't know, I think that it was in this macOS 15 thing that they started to do a bunch of changes with the way simulators work, and that's… that's a bummer, because it was kind of stable at some point.
But now, it's super, super fragile.
**nacho** 06:43 Okay.
So…
**Ariel Demarco** 06:46 So, it's just merging that, I just wanted to validate if you are, like, okay with this new approach I created.
**nacho** 07:01 So it's in the… so you, you would like to have a new, review?
**Ariel Demarco** 07:09 I'm not sure, guys, what, it was mostly… Because it was approved, and I did that change, and I didn't want to merge it without, like, telling you guys.
**nacho** 07:19 Okay.
Yeah.
So let me…
**Ariel Demarco** 07:26 You can merge it, no worries.
**nacho** 07:41 So, the 10 years were in your last commit, then?
This is a… this is… Yeah, Yeah, I had to agree.
**Ariel Demarco** 07:52 done.
I had to create PRs to merge.
**nacho** 07:58 Yeah, get devices in a dynamic way.
**Ariel Demarco** 08:00 beyond.
**nacho** 08:01 Dude.
**Ariel Demarco** 08:01 We'll run the…
**nacho** 08:02 Okay.
**Ariel Demarco** 08:02 the jobs… That's it, so yes, the… the last one is the last PR I emerged, and that's the last one that have background figures.
**nacho** 08:24 Okay.
Yeah, this result simulator.
Right?
A script.
Yeah, I am putting it here.
Yeah, it looks cool.
I think it looks good if it works.
As you… I think that's good.
**Ariel Demarco** 09:01 Yes, it was the first time the CI actually did a failure.
**nacho** 09:05 Okay. So, do you want me to merge it for you?
**Ariel Demarco** 09:10 Yeah, sure.
**nacho** 09:50 So, I just clicked them.
Yeah, it's merged now.
Okay.
So that means we have released with it?
The core, right?
**Ariel Demarco** 10:05 Right.
That's okay.
**nacho** 10:14 Should it have created?
a new release?
**Ariel Demarco** 10:23 It's true, that, yeah. Oh, yeah, it is. I'm going to.
**nacho** 10:27 Okay, yeah. Oh, it's… it's as pre-release, right?
It has been created, but as a pre-release.
We use that to validate that nothing breaks.
Before going to release?
Yeah, yeah, yes, yeah, the thing is, I am seeing that it's created The version release is created, but it's created as a pre-release mode.
So, no public release for that.
You can ping to that version, but, you…
**Ariel Demarco** 11:07 Yeah.
Basically, what happens whenever it's marked as pre-release.
if you have some things activated in CI, it tells you that it's a pre-release.
And by default, the SPM is not going to select them.
**nacho** 11:21 Okay, yeah, yeah, yeah.
So, the flow for this is that we should Use it for testing with the… the core with the other library?
**Ariel Demarco** 11:37 Yeah.
**nacho** 11:38 for making it…
**Ariel Demarco** 11:39 if we see that it's working in code, and there's no problem with it, we can just move it to latest, or… and that's it. Or basically remove the… the pre-release flag.
**nacho** 11:49 Okay, yeah.
I think I merged a change in OpenTelemetry Swift, which… Which had, like, a nightly build?
**Ariel Demarco** 12:05 Yeah.
**nacho** 12:06 I merged… I mean, it has been for a long time there. I had approved long ago, and I had no movement, I merged that yesterday.
So, I don't know if we can use that, or that… will merge from… That will be from Maine, right?
**Ariel Demarco** 12:27 The nightly… Yes, it's going to use main.
Renovate, probably.
renovate this for you and to create a PR.
With the new version.
So, if that works… We can use that one.
**nacho** 12:46 Okay.
And… When we… it created? Sorry.
Do we… do you know when we create?
Automatically, or can we run Renovate manually?
**Ariel Demarco** 13:17 I think you can, let me see…
**nacho** 13:23 Yeah, you are driving, right?
**Ariel Demarco** 13:28 Let me first join from my Mac.
**Ariel Demarco** 13:47 I'm here.
**nacho** 13:49 Okay, yeah, great.
Nightly build this one.
But it takes from Maine.
It built tonight.
And it worked.
the nightly Yeah, sorry, I am thinking while looking at the screen. I was going to check what were… If we can check what commit we have in the release.
Because this is the release.
We have no difference then.
from… No. This release… Yeah, no, I was thinking where this release came from.
What version… of the release it had. What… Because probably this committee is not there. It's only this one, right?
**Ariel Demarco** 14:58 That's a good question. I think it just happens.
**nacho** 15:04 Barely.
**Ariel Demarco** 15:05 The make on the not only clock, yes, because that was the one that it was breaking.
**nacho** 15:10 Yeah, okay.
So then, if… The span context entries stay sendable.
Which was grown here.
Pass.
That means that… This version passed, right?
**Ariel Demarco** 15:27 Yeah, exactly.
**nacho** 15:29 Because it was just changing to making them sendable.
And nothing break… broke in the test.
So I would say that this is a good version.
**Ariel Demarco** 15:44 Of course.
**nacho** 15:47 Or the other thing is making the… renovate what to run.
**Ariel Demarco** 15:57 Let me… Do you feel like I'm rooted.
Finally.
**nacho** 16:11 Or probably we have a nightly build. I know, but I built it yesterday.
After the same double.
If not, we will have a nightly bit from that commit, probably.
Best to validate.
**Ariel Demarco** 16:27 I just triggered the update dependencies job.
**nacho** 16:30 Oh, okay.
How did you do that? Yes, for…
**Ariel Demarco** 16:33 You go… you go to auctions?
**nacho** 16:37 Yeah, in a pandemic history, yes?
**Ariel Demarco** 16:39 And there's an update call dependencies job.
**nacho** 16:43 Oh, this one.
**Ariel Demarco** 16:46 on that one.
Okay.
For some reason, it failed.
Okay.
Bummer.
So this probably is not using… It's not using Renovate, it's just using something else.
**nacho** 17:09 But it says it cannot… Grid this one.
**Ariel Demarco** 17:14 Second red.
Let me see the workflow to see what it's doing.
in which… step… did it fail? .
**Vinod Vydier** 17:37 Right at the top, right?
**nacho** 17:38 Yep.
**Ariel Demarco** 17:41 update the dependencies, okay.
Update dependencies.
So, it fails validates the version.
Then, update the tendencies.
So you advance the script. Let's see what that script does.
**Vinod Vydier** 18:22 Ori, do you want to share your screen?
We're doing something later.
**Ariel Demarco** 18:27 What's room?
**Vinod Vydier** 18:28 Do you want to share your screen?
**Ariel Demarco** 18:30 Oh, yeah, sure. Why not?
Hello.
Old school Windows.
So I'm basically… I was trying to do exactly that.
basically this.
With 2.4.1, it works.
So, I don't know why it's not working.
The other way around.
Maybe because it uses… Yes?
Nope.
What?
**nacho** 19:28 Okay, yeah, we can wait for the other, if not.
For the other task.
**Ariel Demarco** 19:37 Yes, I think that.
I can run it manually, though, if you want.
like, now, create a PR with this, and that's it.
That's another thing we can do.
And create the PR.
**nacho** 19:59 Oh, yeah, that's right.
**Ariel Demarco** 20:01 Okay, good.
update.
I'm automatically nerge.
What's the problem?
**nacho** 20:45 Yeah, probably because you need approval.
**Ariel Demarco** 20:47 Scheme.
Maybe interesting.
Oh.
**nacho** 20:53 Oh, you mean…
**Ariel Demarco** 20:56 Maybe there was some changes… Let me write down this again.
Yeah, that's worth.
Update.
What's your fault.
Running again.
Without an ape.
practically the same company, too.
Oh.
I'll do something.
22…
**Vinod Vydier** 21:40 No, your question to embrace, right? Yeah, maybe…
**Ariel Demarco** 21:43 Yeah, it's my fork.
**Vinod Vydier** 21:45 Okay, okay.
**Ariel Demarco** 21:45 open.
Open telemet.
Rit.
I probably won't use it anymore.
Oops.
What's deleted.
Awesome. Bang.
Beautiful, obstacle name.
Oh, shit, right?
I'll keep that updated.
Get your code.
Can… Oh, ideally needed. Bye-bye.
Deep punch, deep.
Ps… Oh, yes.
Now it does, able to migrate.
I realize I fucked up.
Okay, everything looks fine.
That PR is up then.
Hopefully this… This works.
**nacho** 23:11 Okay.
Yeah, we can even merge these, right?
or the… Or this… For the street person.
For the main laborer?
Right?
**Ariel Demarco** 24:01 Do you mean if we should… if we should merge it?
**nacho** 24:05 Yeah.
**Ariel Demarco** 24:07 Yeah, I think we're done.
**nacho** 24:08 I mean, it's gonna run the test, right? That's what we wanted, but it's also the… we prefer also to have things updated, right? Whenever we release OpenTelemetry Swift to the same version.
**Ariel Demarco** 24:23 Yeah, and also there'.
**nacho** 24:23 That's…
**Ariel Demarco** 24:25 there's an issue in… that I remember, that it was waiting for… For this fix to be done.
Yeah.
I think this… this issue, I'm sharing this in the chat.
This issue was waiting for this new version.
So… I think we've done… Just merge it, and that's it.
**nacho** 24:51 Oh, okay.
**Ariel Demarco** 24:54 If, obviously, if they're PR.
Has no issues, obviously.
**nacho** 25:07 Okay, yeah, that's right, yeah. So let me approve it.
your…
**Ariel Demarco** 25:14 Yeah, and we can't wait to do the status checks and all that stuff.
**nacho** 25:17 Yes.
Okay, so while that works… More things that we have, do you want me to share the document and we continue with other tasks?
Okay, so this is… Yeah.
So, that for now. So… This is another topic.
span… Yeah, this span content.
**Ariel Demarco** 26:10 there's…
**nacho** 26:10 station double. I immersed it… Because, basically, the only concern now was that if there were some compatibility issues.
And as I had approved the nightly bill.
in the other project. Basically, I mean, if it builds in the other library, the changes will be for the users of the library when they update, and that should be doable.
We are not breaking.
not… non-users of this library. That, that, that was my main concern for this.
So, yeah, it's… Yeah.
That's what he said. If it breaks code that is changing it directly, then we should have.
fix that.
So yeah, that, that's… That was the only concern.
That's why I immersed it. So, yeah, that's merged.
Oh, man.
merits… Repository review. Now, this one, span events, getting deprecated. Yeah, that, that.
**Vinod Vydier** 27:28 Yeah, that… you can remove that, because I think it's all… I already created an issue on the…
**nacho** 27:33 Okay. Yep.
Yeah, that's true.
**Ariel Demarco** 27:36 Yeah, that's… that's station.
We're not, do you know, what… I haven't gone through all the new API and all that stuff. Is the span event getting deprecated, and it's going to be replaced one-on-one with the Autel Events API?
**Vinod Vydier** 27:58 Yeah, that's dope.
Let's see a summary of it, yeah.
**Ariel Demarco** 28:03 Okay, awesome.
Okay, so I think we should just do the auto elements API. I think Bryce started that at some point, but I think that with the whole baby thing, it's going to be… Kinda complicated for him to do.
do you guys want me to give it a try, and start raising some PRs about this?
Maybe some drafts with… the idea, I can go and read.
old Bryce SPR that he closed, and see if…
**nacho** 28:39 Yeah, I mean…
**Ariel Demarco** 28:39 and work.
**nacho** 28:40 For me, sounds perfect, if you have time band-wise, and all that stuff.
**Ariel Demarco** 28:48 Yeah, I think it's… nothing good.
We needed…
**nacho** 28:58 Yeah, I mean, I… I done… I really like the span events.
**Ariel Demarco** 29:03 Yeah.
I'm… I'm… it's… I… I…
**nacho** 29:07 The thing is that it simplifies a lot of things, right? You don't need to have… you only need traces to have most of… things. Now you have to have logs, one, and have to have span.
So you need two different backends, and you need to mix that information.
Which… or… or do you need… Two places to restore things, and then you have to mix information from Two different places.
**Ariel Demarco** 29:35 Yeah.
Yeah, that's… that's the weird thing, but… I know that during the whole lifetime of the span event, a bunch of people complained about not fully understanding what's the difference with logs.
What are the… big… where do you place big attributes, or stuff like that, so… I don't know, seems like they want to…
**Vinod Vydier** 29:58 No, you also have to… yeah, you also have to create an event name, so that'll be interesting.
And then, you know, correlated, right, with a sum attribute.
Yeah.
**nacho** 30:13 I think it adds a level of complexity, depending on what you want, right? It forces you to have a complete observability.
backend.
To… before you could do that simpler, with just, with, with, with this infrastructure.
Bye, okay.
I can understand that.
Yeah, once you add the span ID to a log, then what's the difference between a span event and a log associated with that span, right? Yeah.
It's just the graphs, but keeping in different places.
Okay.
And, yeah, there are no more topics here, from last week, Do we take a look to the… To the different… Issues and pull requests that we have open?
**Ariel Demarco** 31:16 Awesome.
**nacho** 31:18 Yeah, we have these… I don't know how it has been done.
review required, other things await APIs for exporters.
Support at W33 random trace.
Flood propagation?
And you have this documentation. This was from you, right, Dina?
No.
**Ariel Demarco** 31:44 This was a long time ago, and he had to do some updates and stuff like that.
**nacho** 31:50 Yeah, and… Yeah, that's right, okay, yeah. I remember another? Okay.
I guess so.
**Ariel Demarco** 31:56 I've seen Billy. I haven't seen him for a long time.
**Vinod Vydier** 32:01 Yeah, he was, he was in one of the calls recently, yeah.
**Ariel Demarco** 32:04 Oh, okay, that's awesome.
**nacho** 32:07 He was, like, 2 weeks ago with, you know.
In fact, the last… We… the last meet was then.
The random trace propagation.
Okay, yeah, I, I reviewed this.
Some checks haven't completed.
**Vinod Vydier** 32:46 Oh, this person is not… It'd be… Sign the CNA.
**nacho** 32:56 What's this pending tick?
Required status check.
What's this estate?
**Ariel Demarco** 33:22 So, that is the one that waits for all the others to run, but though the others haven't run yet, don't know why.
So… Which is the… let me go… this is in OpenTelemetry Swift or Core.
**nacho** 33:36 This is Coral.
**Ariel Demarco** 33:38 Let me see if I can force it to rerun.
this BR is there.
to poor WCU3G, this one? Yes.
**nacho** 33:52 Yes, yeah. In fact, I reviewed this long ago.
**Ariel Demarco** 33:57 So check's been there.
Okay? We'll answer.
**nacho** 34:12 Yeah, he was just trying to… I don't know how I can refund that.
**Ariel Demarco** 35:28 It's weird, it's like, I don't have the rerun.
**nacho** 35:32 Yeah, there is no rerun button anywhere.
**Ariel Demarco** 35:36 Mmm.
**nacho** 35:44 Maybe I cannot rerun?
Should I trade?
**Ariel Demarco** 35:48 Let me see if I can rerun it with… no.
Oh, unable to retry this workflow run because it was created over a month ago.
Oh, really?
Yes.
Good to know.
**nacho** 36:09 Where did you get that?
**Ariel Demarco** 36:11 I tried to do it with the CLI.
**nacho** 36:15 Okay, okay.
**Ariel Demarco** 36:16 Just… just for everybody to know it, you can do it in this way.
Give Run, rerun.
That is to run the whole… The whole… the whole job.
**nacho** 36:32 So maybe, what can we do here, then, then?
**Ariel Demarco** 36:42 We should ask this guy to rerun an empty commit, or something like that.
Because for some reason, the whole CIA system Packed up.
Probably because the commit wasn't verified.
**nacho** 36:58 No, but it was perfect, yeah.
**Ariel Demarco** 37:04 Yes, but if you go below… If you go to all the commits. The last commit, it was unverified.
**nacho** 37:10 Oh, really?
**Ariel Demarco** 37:12 Yeah.
I don't know why that happens, to be honest.
The other way… no, but it's not going to work right now.
Good luck.
**nacho** 37:27 I don't know what we can do with this.
**Ariel Demarco** 37:37 Main issue is that we cannot do it manually, like, run the test manually, because… this job… It's in his repo, in his fork.
So, I don't think we have access to it.
Well, at least… Just be slow.
No.
**nacho** 38:09 Yeah, I cannot recall anything like that, yeah.
**Ariel Demarco** 38:19 We have access to the nation.
**nacho** 38:22 Yeah, I think I will ask him to…
**Ariel Demarco** 38:28 Maybe it seems like it was completely done with AI.
And maybe that's why it's not verified.
Like… branch name is Codex.
So… He, like, induced tragedy.
**Vinod Vydier** 39:02 GitHub will catch it and… It won't let… I'm missing.
**nacho** 39:09 Like me?
Yeah, but the thing is, I had tried to run this… And it had failed.
Beautiful.
Because in the previous… Yeah, I don't know… yeah, I don't know what we can do, more than asking him to…
**Ariel Demarco** 39:33 Let me… let me check if I can do it.
Okay, for the year, It's gone.
Take a message.
Let me see if I can do an empty permit.
Let me check out savings… Chicago next.
Keep commit.
Seems I was able to.
**nacho** 40:31 Yes… That we have no statue checks?
**Ariel Demarco** 40:57 What the hell?
It's not running anything.
**nacho** 41:22 It's like it has no axions assigned, somehow, no checks.
**Ariel Demarco** 41:28 But the checks that should run, so, are the ones that are on our… pipeline.
**nacho** 41:35 Yep.
**Ariel Demarco** 41:36 I'm… Let me go, Just…
**nacho** 41:48 I think they have probably never run.
Or they got stuck the first time, and…
**Ariel Demarco** 42:11 No. No, I can't.
It's running.
Yes, they are running right now.
**nacho** 42:25 Oh, yeah, really?
**Ariel Demarco** 42:27 Yes.
**nacho** 42:31 Great.
Yeah, you basically added… I don't know if you have reviewed that, but basically added, Instead of adding 01 or 0, it added a different… Different platforms.
Yeah, and it had a test to validate that, and everything looked… Correct.
**Ariel Demarco** 43:01 Okay, bye.
**nacho** 43:05 But we've been met.
**Ariel Demarco** 43:07 Cool.
**nacho** 43:10 Yeah, run them… different flak.
Okay, so this one is handled at least for now.
Ugh.
more public, let's see. Yeah, I think about the APIs for exporters.
It's also really interesting.
work.
**Ariel Demarco** 43:48 Hmm.
**nacho** 43:50 But it needs…
**Vinod Vydier** 43:55 Want to test it.
**Ariel Demarco** 43:58 Yeah.
Also, the timeout…
**nacho** 44:06 I am not sure this is the approach we would like to have.
**Ariel Demarco** 44:11 No.
**nacho** 44:13 I think we should add, I think… To the existing exporters, as in methods.
**Ariel Demarco** 44:21 Yeah, I think… We should do something like that, and that's it.
**nacho** 44:28 We had not asked about it. The thing is that You can't have the same classes having async and non-async methods. They are different methods, and if you are in an async.
task, it will use the… if you use a wait for calendar method, it will use the async one, and not… and if not, it will use the non-async.
And I think it will… That will simplify the things.
But having a different exporter, Just because being a sync is not what… I think it's good.
**Ariel Demarco** 45:10 Yeah, and I think that… Eventually, what we can do is just… progressively.
Apply a single way to the different exporters or processors that we We already have in our repo.
**nacho** 45:23 Yeah, I think that's… that's.
**Ariel Demarco** 45:25 And makes the migration easier, also, because if not, you should do it all at once.
**nacho** 45:34 Yeah, I think that's also the approach that Apple took with many APIs, just adding the async variants.
And… and working from there.
Yeah, he's on… I don't think this is the solution to bring, yeah.
Should we say that to him?
Yeah, he had… the truth is that he had done a lot of work.
**Ariel Demarco** 46:11 Yeah.
**nacho** 46:11 Yeah, I need to be there for a month.
Okay, I will add… what should I say? Something like…
**Vinod Vydier** 46:23 I guess you can say that, you know, you try adding a sync to the existing exporters and see if Because that should work, so…
**Ariel Demarco** 46:49 in this AI era, this kind of PRs are going to be common. Yeah.
**nacho** 46:54 That… that… that I was thinking the same.
I'm not sure. Maybe it's, it's, it's not the Yayera,
**Ariel Demarco** 47:03 No, the PR… the PR description has, did it with cloth color or something like that. It's…
**nacho** 47:10 Oh, he's…
**Ariel Demarco** 47:10 You don't… Yeah, the bottom, generated with Cloud Cold.
**nacho** 47:15 Where it says in the commit. Oh, yeah, okay.
Okay, then… then it's not so much effort for him to be bred.
**Ariel Demarco** 47:25 If we… if we would be stricter, like, there's a rule that the first three contributions shouldn't be… full AI, but, you know… I guess I prefer people interested in a project at least committing things, but this is not the preferred approach, I think.
a rather hub.
The protocol with a default no-wop extension.
For… Yeah. So we don't break compatibility, and we start providing Support.
One by one.
it's a really complex thing to migrate everything to a single weight, and I don't want to, like, do it in… Without thinking.
**nacho** 48:07 Yeah, and might… Get the correct threshold.
Okay, what about this? Do you think it's…
**Ariel Demarco** 48:18 Mmm… Yeah, I would also… And protocols genetic levels.
Classic. Default implementations, default no-op, if you want. Default no-wop implementations should be… In an extension of that protocol.
Until we fully migrate to a single weight, which I don't know if we wanted in the future, maybe it's something to discuss.
But…
**nacho** 49:05 I don't… I'm not sure migration is what we want, but flexibility.
For us as a library, right?
**Ariel Demarco** 49:16 Yeah.
**nacho** 49:17 We should allow… both approaches, both have, pros and cons, I think.
**Ariel Demarco** 49:24 Yeah.
**nacho** 49:25 Yeah, right.
**Ariel Demarco** 49:25 like URL session, like, if you try to use URL session, you can use completion blocks, and you can use async await.
**nacho** 49:33 Yeah, the truth is that we have some APIs that will probably, benefit from a, from a callback. Like, exporting and giving an error instead of… returning success, directly. We have some of those that might improve, but yeah.
Probably going async is the way for having better.
better behavior.
And that's also a nice tip, too.
to improve.
Okay.
So that's the… What?
I have to approve workflows?
**Ariel Demarco** 50:18 You have to approve in order for workflows to run.
**nacho** 50:22 Aye.
No. Yeah. Okay.
I thought they had started, but this is the same. No, no, they started.
**Ariel Demarco** 50:30 the… the other.
**nacho** 50:34 I have seen this before in this epid. You change that, and it… They started already, right?
Okay, I don't know. It was in the other one, okay.
Yeah.
**Vinod Vydier** 50:51 Yeah, there was… there were two of them, right? The same person.
**nacho** 50:59 Okay, and this is another… var propagation carriers get transferred.
**Ariel Demarco** 51:08 What the sis.
I haven't read this.
To be honest.
**nacho** 51:15 Yeah, this is… You know, it was quite… I couldn't review it, it was quite weak.
**Ariel Demarco** 51:24 Oof.
Oof.
**nacho** 51:28 And it has lots of documentation there also, with usage and things like… yeah, which looks… Good, but we have to… I, I, I…
**Ariel Demarco** 51:40 Ridges.
**nacho** 51:41 Time to read it.
**Ariel Demarco** 51:43 Yeah.
**nacho** 51:43 I don't… I did it long ago.
In fact, we have.
**Ariel Demarco** 51:53 I…
**nacho** 51:54 We, we had… we… we… we supported environment variables for… for transparent?
We were the first library in OpenTelemetry, and some other libraries take our names, and we had to update them later.
Tuesday.
**Ariel Demarco** 52:10 Oh.
**nacho** 52:11 environment names common. They didn't like our one.
But yeah, Yeah. Yeah, because having an environment variable for race propagation is wonderful. You can really, do propagation between different binaries, which is… which is nice for a system.
Okay, so that for, yeah, we… this must be reviewed. It has been there.
Not for so long, I think.
Last week, okay.
So this for core library, Do we go to the non-cor?
And take a… oh, these are the pull requests, maybe it's some issue, sorry.
**Ariel Demarco** 53:00 No, no, there's no new issues. I added that one.
**nacho** 53:05 Okay.
**Ariel Demarco** 53:06 That was a long time ago. Well, one, two months ago.
I'm going to send you guys, you and Bryce, obviously, a question. I don't wanna… ask it in live, because, you know, it's been recorded. Just… Just for you to know, and it's… it's another thing.
**nacho** 53:30 Yeah, we… we can't have anyone there.
we, we… We can create another Zoom, if you want, some pretty…
**Ariel Demarco** 53:41 No worries, no worries.
**nacho** 53:41 Attend this meeting, no worries.
**Ariel Demarco** 53:44 I, I sent it through, through the community Slack, privately.
**nacho** 53:50 Do you want a yes-no answer?
That we can provide now, or do you want to know.
**Ariel Demarco** 53:56 I think you have experience, because you did something similar, I think, a long time ago, so…
**nacho** 54:04 Yeah.
No, not… Okay, yeah, I will answer that, I think, but I don't really worry much. But yeah, if you… We had had some of those things already there for longer than that.
The unexpected, so, okay, yeah, I think we can talk that also there.
So, regarding issues… Yeah, the only issues are created from you guys.
**Ariel Demarco** 54:41 Yeah.
**nacho** 54:42 This was the issue that we are fixing? Okay.
**Ariel Demarco** 54:44 Yes.
**nacho** 54:45 So then, for the pull request.
Yes, we have 5 minutes, so… So, do not merge, which is great. Upgrade to Swift 6.
This is Willy Draft.
Yes, gradually, we also.
**Ariel Demarco** 55:05 I think that the…
**nacho** 55:06 Oh, this is really interesting.
Yeah, she did it within the tracing bridge.
He… I added some… comments yesterday. Yeah, it was a draft, but it added support for the Apple Distributed Tracing Library.
Which is really nice.
**Ariel Demarco** 55:23 That's awesome.
**nacho** 55:24 This is still a work in progress. I didn't… yeah, I said this.
Basically, that it's… it was really nice. It… Easiest a weapon to convert to a word.
Things.
No.
So, yeah, it's not finished, but it looked good so far for me.
So I ask him to continue, maybe. I hope it… Yeah, last month.
We have been a bit out.
Maybe.
**Ariel Demarco** 55:59 Yeah.
**nacho** 55:59 So that's… that will be really cool.
**Vinod Vydier** 56:04 Does it require a dependency on the apples?
Tracing that bench?
**nacho** 56:09 Yeah, it adds the dependency on the Apple. If you see here in the file change, it has here a dependency on the package from Apple, yeah.
Which, you know, we have this project for dependencies. By the way, we… I saw that now you can… just build some libraries, with… in the packages, but I… I probably still downloads all the packages anyway, in the new package. Sorry.
From the wrong one.
Comment. What more?
Yeah, these are Docker and things like that.
**Ariel Demarco** 56:52 Yeah, Docker with… Docker with 6.3 and 6.2 in the Docker Digest.
**nacho** 57:00 Okay.
Those come, yeah, I said that… Directly, right?
**Ariel Demarco** 57:06 Yeah, the gRPC one, I asked… I approved it to run the jobs today, seems like everything's fine, so you can merge that one, too.
I gotta jump, guys, so… Okay. I'm leaving you.
I mean, it's early.
Cheer.
**Vinod Vydier** 57:30 See ya Bye.
**Ariel Demarco** 57:32 Bye-bye.
**nacho** 57:37 And… Okay… So… I think we can… A proof and run, right?
Oh, you live.
Dina, you've left.
Yes. Okay. Then, bye.
