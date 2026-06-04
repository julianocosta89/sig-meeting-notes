SIG: Community Demo App SIG
Date: 2026-06-03
Duration: 29 minutes
============================================================

## Zoom Recording Transcript

**Juliano Costa | Datadog** 00:15 Hello, hello.
**Donal O'Sullivan** 00:20 Hey, Juliano, how are ya?
**Juliano Costa | Datadog** 00:22 Good. Yourself?
**Donal O'Sullivan** 00:25 Good, yeah, good now.
Yeah.
Busy.
**Juliano Costa | Datadog** 00:30 That's nice. Yeah.
The story of my life.
Reviewing a bunch of, PRs from the… Yeah, from the new things on the CICD here, and, like.
No, not CHCD, on the GitHub Actions, then, it is a mess.
**Donal O'Sullivan** 00:59 Yeah, it's, yeah.
it's quite flaky, I think, just like… not just the hotel, like, not the hotel demo repo, but in general, like, CI stuff tends to be, at least on GitHub, I've noticed, tends to be quite flaky.
She's not annoying. She's annoying.
**Juliano Costa | Datadog** 01:16 Yup.
**Donal O'Sullivan** 01:19 But I've seen there's… I think we've gotten through a good bit of reviews today already.
**Juliano Costa | Datadog** 01:27 Yeah, there's one thing that I… So, I'm checking now… one of the… the Pennerbot… Docker-based images updates, let's see if that works.
But there is another one that is, like… Bumping 21 directories.
Bye.
Directories, yes.
And, yeah, I don't think that will be, like, a easy win.
Let's see.
**Donal O'Sullivan** 02:09 Yeah.
**Juliano Costa | Datadog** 02:11 Talking about EasyWee, I… I said that you… Okay, okay, okay, now I understand your, your… approval here.
**Donal O'Sullivan** 02:31 Oh, for Shinoy's work, is it?
**Juliano Costa | Datadog** 02:35 Yeah, I don't think.
**Donal O'Sullivan** 02:37 Yep.
**Juliano Costa | Datadog** 02:38 It actually is already added to the… to the checks, are they?
**Donal O'Sullivan** 02:43 Yeah, so it runs… when you hit approve, it'll actually run the check.
So I think if you open a… if you open a PR and you have a workflow change, you can see, like, GitHub will run… will run that in your CI, as far as I believe.
**Juliano Costa | Datadog** 03:01 Yeah, it's here, but this is interesting, because I… it failed on my machine, and here it's successful.
**Donal O'Sullivan** 03:09 Yeah, yeah, so it actually failed on my machine as well. Well, it didn't. It just took so long, I stopped it, because I was… I needed my… most of my hardware to do something else. But so it's interesting, it does… like, it seems to run fine in the CI. It doesn't take a huge amount of time, I think, but Yeah, like… I don't know, is it something that we want also to be working correctly on our local machine?
That is nice.
**Juliano Costa | Datadog** 03:38 Yeah, I don't know, like, here it passed in 27.36 seconds.
**Donal O'Sullivan** 03:46 Yeah.
**Juliano Costa | Datadog** 03:47 on my machine took, like, 45 minutes, and then I killed.
it was on, I think, 25 or 40, I don't know, but…
**Donal O'Sullivan** 03:56 Yeah.
So I can see here… It took 20… it took 3 minutes to actually run the tests on… in the CI for the… For the full suite.
Yeah.
**Juliano Costa | Datadog** 04:16 That's actually interesting. Yeah, I wasn't aware that it was already running on the CI.
**Donal O'Sullivan** 04:24 Like, it's not merged yet, you know, so it's just on that PR, but .
**Juliano Costa | Datadog** 04:28 Yeah, yeah, yeah,
**Donal O'Sullivan** 04:29 Yeah.
Yeah, I don't know why, like… so for your one, did it actually error out, or did you just cancel it? I think it errored out, did it?
**Juliano Costa | Datadog** 04:39 I canceled because it got stuck on… on a metric test.
Forever.
That's actually a good point, because… I think I know why it is actually failing on my machine.
Because I was… was reviewing a PR from… From one of the metrics, Renee.
**Donal O'Sullivan** 05:03 Hmm.
**Juliano Costa | Datadog** 05:03 And I couldn't find a metric on Rafana.
So, and I know Grafana queries Prometheus, so I.
**Donal O'Sullivan** 05:12 Hmm.
**Juliano Costa | Datadog** 05:12 I think the problem is on my machine, not on Shanoi's PR.
Yeah.
**Donal O'Sullivan** 05:19 You know, I… you… you just… yeah, you've, made me think there as well. I think the reason that it probably got stuck on my machine was a similar thing, because I think… Sometimes the demo can be flaky if… Yeah, if the Docker image locally is, like, an older one or something, and if it's restarting, then I guess the tests will stall out, you know, that kind of way.
**Juliano Costa | Datadog** 05:42 I think the case here is… let me just check the… I think the problem here is… Compose YAML… No. Do we have… Shanite, do we have, What is it?
What is the config that you run the collector?
Do you know?
By heart?
**Shenoy Pratik Gurudatt** 06:18 Config to run the collector.
They're younger.
**Juliano Costa | Datadog** 06:26 Cause I cannot… I cannot see the… which comment?
Like, on the… Run telemetry test.
You restart.
**Shenoy Pratik Gurudatt** 06:38 Oh, it starts… it starts the demo, right? So it waits for the load gen to… Do everything.
Yeah, but do we have…
**Juliano Costa | Datadog** 06:50 Do we have a collector config?
Because now we have different modes, right?
So… when I do… locally, when I do, like, make start dash profiling, it gets the… the collector from the profiling as well, and then it sends data to FirePit. When I do make start no observability, it doesn't start Rafana, Prometheus, Jaeger.
all of those components, so this… Config is not even there.
what is going on on my machine is that I have the extra populated, so maybe I'm overriding something that is… I'm wrongly overriding something, and then, The metrics are not reaching Prometheus, hence the tests are failing, but then that's a me problem and not your PR problem.
**Shenoy Pratik Gurudatt** 07:54 You see, do you see the exact error, what it is showing up on the test result? Is it a polling issue? Is it a missing issue?
**Juliano Costa | Datadog** 08:02 No, in my case now, the last run, I stopped because it took 45 minutes.
And, it was on 46%.
So then I just canceled because, yeah, like… And in this, Donald, approved the PR to run the… the test on the… on the pipe… on the… on the GitHub Actions, and yeah, on the CI, and it… it worked.
**Shenoy Pratik Gurudatt** 08:30 Yeah, even I need to try that.
**Juliano Costa | Datadog** 08:32 In 3 minutes.
Oh.
**Shenoy Pratik Gurudatt** 08:36 Before pushing as well, I just, try it out on my Linux machine.
By the way, I haven't tried this on my Mac yet, but I don't think it should fail.
How do we find the dip?
Do you know any diff that you have on your local?
**Juliano Costa | Datadog** 08:57 Yeah, I know. So, so the thing is that I'm also configuring, I'm also configuring the data to be sent to Datadoc.
**Donal O'Sullivan** 09:08 I have a hunch that if there's an issue with one of your Docker images, and it's just restarting, that maybe the test will just keep running, and it'll, like, not fail. It will just kind of run… it might time out eventually. So maybe we should just have, like, some kind of… timeout, if it only takes 3 minutes in the CI, maybe just, like, time out after 5 to 10 minutes or something. Just say, like, oh.
And then… maybe a prompt error, please check something in Docker images or something, because I do know sometimes if I run the demo.
on Maine and, there might be something, like, the product catalog might be restarting, or something like that, you know, I wonder, is that… that's probably going to affect the telemetry tests, I guess, if there's… A service not working, and there's no telemetry, I'll probably just keep polling, trying to collect that telemetry, right?
**Juliano Costa | Datadog** 10:00 Yeah, a timeout would be nice, like, after X, if it doesn't… Complete just kill. Otherwise, we're gonna… waste our…
**Donal O'Sullivan** 10:13 recycles with CPU.
**Juliano Costa | Datadog** 10:15 Host, yeah, or host minutes, whatever they call in, in GitHub.
**Shenoy Pratik Gurudatt** 10:21 There is a per-test timeout.
And there is a polling limit.
So… I think there is exponential back-off or something like that.
**Donal O'Sullivan** 10:31 Yeah, yeah, okay, okay.
**Shenoy Pratik Gurudatt** 10:33 And then it tries for 5 times, and after that it gives up and calls it out as an error.
So, maybe I can have an overall timeout, like we are seeing here.
So, probably 20 minutes, and if you're not done, then just come out of it.
Yeah, I can check that.
**Juliano Costa | Datadog** 10:54 Physics, I, I can reopen if you, if you want.
**FELIX GEORGE** 10:59 I kind of messed it up a little bit. I accidentally lost it, but I created a… but, so, should I reopen, or should I, you know.
I can also, re… it was a draft PR.
Should I reop… I have created a new one, which I think doesn't have any issues right now.
Still dope.
older one, while trying to merge some things, I got into ECCL economics, and while trying to fix that, I got into some changes. Like, I created a patch file, and then I applied the patch file. It changed a lot of files in the .github workflow files.
Yeah, I was trying to fix that, I accidentally closed the PR.
**Juliano Costa | Datadog** 11:48 Okay, from other comments that we have on the PR, looks like all the files are already outdated, so looks like you've already addressed them.
So I… I don't know if there is any… Objections, but… For me, it's fine if we just move on on the… To the… to the new one, and… And as the new one is already tagged as, ready to review, so then we can take a look at it.
Aw.
Three, three cases.
**FELIX GEORGE** 12:26 Oh, I think dumb.
**Juliano Costa | Datadog** 12:27 Very cautious.
Go ahead, sorry.
**FELIX GEORGE** 12:34 Okay, so I have, I have linked the older PR also in the new PR, if anybody wants to refer the old PR.
**Juliano Costa | Datadog** 12:50 Boop.
No, I'm good with it. I think I'll ask Shanai, because he was mostly involved on this. Do you have any… I don't know, maybe… your agent already has all the context of the PR, I don't know.
**Shenoy Pratik Gurudatt** 13:09 I don't begin.
**Juliano Costa | Datadog** 13:09 Workflow.
**Shenoy Pratik Gurudatt** 13:11 Yeah, I don't think agent cares that much.
**Juliano Costa | Datadog** 13:16 Okay. Great.
**Shenoy Pratik Gurudatt** 13:18 Yeah, I think it should be good to have a clean start any, so better to smooth the PR. Yeah. I told Felix that, because of some main merge, there was a lot of older PRs that got in, and it also broke easy CLA.
And it went to 1,800 commits on his PR, because he pulled all the older ones.
So, I just asked him to rebase and force push, but I think creating a new one is still better.
That's it.
**Juliano Costa | Datadog** 13:50 Cool. Yeah, I just authorized the… the CI here, so let's see. I guess… Maybe we're gonna have some license issues? Don't know.
No, the files are already with the license.
Cool.
Okay.
Yeah, this, this one is massive, yeah. I think, I think I'll take the approach when, the same approach that, we used when we started the demo. I'll just run, see if it works, and then we merge it.
We move on from there.
Anything that we should, take a closer look when reviewing?
Felix.
**FELIX GEORGE** 14:50 No, I think… so, I have asked a few of my friends also to test it out, you know, so, so there… there is a requirement of building a front-end proxy again, because, Envoy was changed to add the chatbot endpoint also to the, like, get exposed with the localhost 8080.
Other than that, there were no… no issues, because, if someone doesn't run make build before make start.
then the front-end proxy won't recognize this chatbot endpoint. Otherwise, it was straightforward. You can try out any requests which are default, by default, available in the chatbot.
So there are three. I have added caches for 2 models, GPT 5.5 and Cloud Oppos 4.7, for those 3 requests, so… So I think it should be comfortable.
I have tested with both MCP and non-MCP nodes.
**Juliano Costa | Datadog** 15:48 is, So, just to double-check, to confirm, I do not need, to configure any API token or whatever, I just make build…
**FELIX GEORGE** 16:03 No, just to test, you don't need to configure any APIs, like, the cache will… cache will be reused, but if you wanna try out any new request.
and get proper, appropriate answer, like, non-error messages for those requests, you will have to configure an API key.
**Juliano Costa | Datadog** 16:21 Okay.
**FELIX GEORGE** 16:22 But, I can, I can, you know, I already have generated the complete cache for a lot of requests, which I But I didn't add it because the PR would become even larger with those files.
Yeah.
**Donal O'Sullivan** 16:40 Felix, can you add all this stuff to the PR description? Because the context will get lost here. So, like, in your PR description, just mention the steps that you have to do to run it locally. So, like, first thing is make build to regenerate containers.
for the front-end proxy. Second one, just maybe mention about, like, the API key for an LLM, that if you want to use that, this is how you do it, and etc. Otherwise, like, I'll forget about it, and I'll go to review the PR, and I'll probably pull it, and be like, oh, why isn't this working? And then it's like, okay, I have to do… you know, it just makes it a bit easier then for us to go and review it quickly, and…
**FELIX GEORGE** 17:13 Should I add it in the changes section, or as a separate message itself?
**Donal O'Sullivan** 17:18 Put it in the… just put it in the PR description, and then just, like, a note or whatever, and, like, steps to run locally or something like that, you know?
It, like, there's people on the… there's… approvers and maintainers of the hotel demo that aren't on the call here, so for them, if they just kind of read through the description, they can, like, oh yeah, this is what I have to do. Do you know what I mean? It just makes it easier for, like, async work, if that makes sense.
**FELIX GEORGE** 17:40 Okay.
**Donal O'Sullivan** 17:41 I appreciate that.
**FELIX GEORGE** 17:43 Yeah, I'll ride that. Thank you.
**Donal O'Sullivan** 17:44 Right.
**Shenoy Pratik Gurudatt** 17:45 Felix, you also had a README, right? So, if anything that is not there in the README, you can add it in the description.
**FELIX GEORGE** 17:54 Okay.
**Shenoy Pratik Gurudatt** 17:55 Yeah, or if something that needs to be stayed there is a permanent thing for people to run even after we push this in?
It's also good to have it in the README section.
**Donal O'Sullivan** 18:05 Push out, yeah, push out tonight.
**Juliano Costa | Datadog** 18:08 Hmm… Yeah, hopefully whenever we get this one merged, I think this will be the biggest, last block of the 3.0?
And hopefully, whenever we get that, we can already start working on the bumping dependencies, getting, like… because there are a bunch of them that are… on the .env file that we should automate somehow. I know that, Renovate allows us to… Update dependencies on, like, custom files?
I don't know if the Pinnebot… Does that as well?
like, we have the Java version, the C++ version, the collector version, all of that on the… on the… .m file.
And another thing that I want to discuss with you all, I am not taking notes. Let me just open the… Then we'll see notes.
I cannot type in think.
The first thing that we discussed was the… Bests, Pierre?
authentic.
You can take demo.
They need to be reviewed.
And, okay, so now one thing that I would like to discuss is… of… I don't know if any of you have ever… Contributed to the collector.
Cool. They have a CH log file whenever you send a PR, and then you add this file to your PR.
And then, whenever they have a release, they use this file to generate the changelogs.
Why I'm bringing that up is because currently we have the merge queue thingy, so whenever we have a bunch of PRs, I review, I add everything to the merge queue, and then I start getting notifications that, things got out of the merge queue because of, merge conflicts. And when I go check, it's just a changelog.
And then I need to kind of fix the changelog, and then add to the merge queue again, and yeah, that's annoying. So as we are automating everything, I would like to maybe suggest, adding that to the demo? Any… Any opinions?
**Donal O'Sullivan** 21:43 Yeah, that's a great idea. I've, like, I've done a bit of work now in the collector and collector contrib, like, and you just do… there's a handy make target, you just, like, make changelog new, and it generates a YAML file that you populate, and then, yeah, it just… it's all… it's a bit more seamless.
Yeah.
I think, yeah, I definitely support it anyway.
**Juliano Costa | Datadog** 22:06 Yep.
**Shenoy Pratik Gurudatt** 22:07 No random conflicts, so yes.
**Donal O'Sullivan** 22:08 Yeah, yeah.
Yeah.
**Juliano Costa | Datadog** 22:10 Does that add any burden to us? Like, once I need that, and like… Do you know?
Like, I… I mean, I have an experience as a contributor, so I just add the changelog, but I… I don't know how it is, the maintainability of the tool, and like… All of that.
**Donal O'Sullivan** 22:34 Yeah, so, as far as I know, is it using the, it's the change log generator.
It's like.
**Juliano Costa | Datadog** 22:43 Some of the tools, right? Yep.
**Donal O'Sullivan** 22:45 Yeah, it's a third-party tool, so I've never had issues with it, like, I haven't done collector releases.
Either, though, if that makes sense. You know, I've, I've… I've merged a good few PRs, but I've never been involved in actually, you know, a collector release and the changelog there, so I can't comment on that.
But personally, I've never had issues. I know we do use it in Elastic as well, for, like, our elastic agent, we use that changelog generator, it's… It's just handy, like, because all the changelogs are the same, you have the same structure, you know? And there's that YAML template, so…
**FELIX GEORGE** 23:18 Hmm.
**Donal O'Sullivan** 23:18 Yeah.
**Shenoy Pratik Gurudatt** 23:23 They have some automation, I believe, to run that script whenever they are preparing for a release.
Probably can do something similar.
**Juliano Costa | Datadog** 23:36 Okay, I'll take that as a homework, so I'll sync with Pablo.
Just because I know him and I work with him.
And, see what I… what I… what we need to do to it.
**Donal O'Sullivan** 24:07 It's also an… it's an OTEL tool, so, like, I guess we're showcasing another… Hotel tool, which is good.
**Juliano Costa | Datadog** 24:21 Oh, I don't know if we can have that as of now, though. I think we need to have the release, and then start from, like, 3.0. So from… from now on, we use this approach.
And then… Yep.
Which, we changed.
Because we already have a bunch of, entries on the changelog.
**Donal O'Sullivan** 24:44 Yep.
Makes sense.
**Juliano Costa | Datadog** 24:49 Cool.
Okay.
So… we have… two things to… to take a look. One is the… the test PR from Chenoi, and then the… the agentic demo PR from Felix.
So, if we can… I know tomorrow is public holiday in a couple of countries, but yeah. If we can get that going, that would be cool.
Spr is…
**FELIX GEORGE** 25:24 I.
**Juliano Costa | Datadog** 25:25 Go ahead.
**FELIX GEORGE** 25:25 I haven't made changes to the documents, repository, I haven't added… so… How does it work? We make the PR, and then we change, or… Should it go together?
**Donal O'Sullivan** 25:40 Do you mean the OpenTelemetry I.O. website, is it?
**FELIX GEORGE** 25:43 Yeah, yeah. So, because there is this, radio button here.
To, checkbox here to, which is asking for me to change the… Appropriate documentation upload updates in the docs.
Then changelog MD, and the helm chart. The Helm…
**Juliano Costa | Datadog** 26:08 We lost you.
**Donal O'Sullivan** 26:10 Yeah.
**Juliano Costa | Datadog** 26:13 No.
Come back.
Felix?
**FELIX GEORGE** 26:19 Hello. Oh, so hello.
**Donal O'Sullivan** 26:21 Hello.
**Juliano Costa | Datadog** 26:21 Oh, no worries.
**Shenoy Pratik Gurudatt** 26:22 Okay.
**FELIX GEORGE** 26:23 Sorry, I was trying to say that I didn't make changes to the changelog file, document, docs, and The… Helm chart, so…
**Juliano Costa | Datadog** 26:35 I would say… so, Helm Chart is gonna be massive, and we need to do that just after the release, so I would hold on that.
Change log you can add now, already, you just need to add, description of the PR, and then, the link for the… for the PR? Okay.
In the end of the unreleased section, it's at the top of the dock.
And, the docs, whenever we get that merged, or if you want to start working on it.
You can already open the PRO on Opentelementry.io, and then whenever we merge, we can merge there as well, or we can approve and let the docs, owners, merge.
**FELIX GEORGE** 27:25 Okay.
So it should be on the unreleased section, bottom of the unreleased section, or the top of the unreleased section in the…
**Juliano Costa | Datadog** 27:35 Bottom, please.
**FELIX GEORGE** 27:36 Okay, yeah, yeah, it's okay.
**Shenoy Pratik Gurudatt** 27:40 Good question.
**Juliano Costa | Datadog** 27:42 Yes.
And, like, I… and… Constantly, I need to kind of gather things on the top, and then drag down, and… And then I have, What is the name like when you… But I think it's… whatever. Like, I have hyper-focused on those things, and then I… okay, so… 3 to 1 comes before 320, and then… or after, and then I kind of reorder everything, and… yeah.
Cool.
Okay, then… If that's it… I… won't see you… All in… So, I'm off for 2 weeks now, so yeah, I… we'll see each other, async, but, yeah, I won't be on the next two calls.
**Donal O'Sullivan** 29:13 Sounds good. Enjoy your holidays, Juliano.
**Shenoy Pratik Gurudatt** 29:17 Thank you.
**Juliano Costa | Datadog** 29:18 Cheers.
See you guys. Bye.
**Shenoy Pratik Gurudatt** 29:22 Bye-bye.
**FELIX GEORGE** 29:23 Bye, bye.
