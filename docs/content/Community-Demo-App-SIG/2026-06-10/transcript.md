SIG: Community Demo App SIG
Date: 2026-06-10
Duration: 26 minutes
============================================================

## Zoom Recording Transcript

**Shenoy Pratik Gurudatt** 03:20 Hey, Pierre.
**Pierre Tessier** 03:27 Hi, Shanoy, how are you?
**Shenoy Pratik Gurudatt** 03:28 Doing good. What about you?
**Pierre Tessier** 03:33 I'm well.
Enjoying my outdoors today, my outdoor office, I like to call it.
**Shenoy Pratik Gurudatt** 03:42 Nice.
**Pierre Tessier** 03:43 Which is really just my backyard. But it's getting a little hot, so I might go… end up going back in-house here soon, but, I like to try to… I don't know, just come out here and work outside in the late spring, early summertime.
As well as the late summer, fall time, because it's just, it's nice, right? It's nice to be out in the fresh air.
**Shenoy Pratik Gurudatt** 04:07 It's sad that we are in June and we're still calling it late spring.
**Pierre Tessier** 04:11 Well, it is late spring. Summer doesn't start until June 20th.
**Shenoy Pratik Gurudatt** 04:15 Oh, wait, where are you?
**Pierre Tessier** 04:16 I'm being very exact here.
**Shenoy Pratik Gurudatt** 04:19 Yeah, June 28th is a very specific date.
Are you based in… you are… you are in PST, that's what I know.
**Pierre Tessier** 04:26 No, I'm actually in the New York time zone.
**Shenoy Pratik Gurudatt** 04:29 Oh, okay. Okay.
**Pierre Tessier** 04:30 Yeah. I live near Detroit, but in Canada.
**Shenoy Pratik Gurudatt** 04:35 Detroit, but in Canada, okay.
I'm based in Seattle, and we are seeing a late summer start.
**Pierre Tessier** 04:44 Yeah, we also had a late summer start, for what it's worth.
**Shenoy Pratik Gurudatt** 04:50 I know Giuliano is out for 2 weeks, he's on vacation, is what he told the last meeting.
**Pierre Tessier** 04:56 Oh, okay.
**Shenoy Pratik Gurudatt** 04:58 Yeah.
**Pierre Tessier** 04:58 Good for him. I didn't know he was allowed to take vacation.
**Shenoy Pratik Gurudatt** 05:09 Okay.
**Pierre Tessier** 05:10 So what do we… like, I wasn't part of the last meeting. I seen… I know we have your test harness, or your CI harness going there, and it's about finished?
I see some messages go back and forth, and thread kicked off. I didn't really… look at that thread. Is that Done? Merged? Are we ready to go?
**Shenoy Pratik Gurudatt** 05:28 Yeah, that one is done and merged, but I have a follow-up. Let me add that in here. The follow-up that I mentioned in the.
Fair.
**Pierre Tessier** 05:36 threat.
**Shenoy Pratik Gurudatt** 05:37 Yeah.
Follow a telemetry test.
And there's one PR that would be great if you could help merge from Juliano about adding some health checks.
Which I can rebase and build upon.
It's also part of keeping the health of the services in check.
Should be, yeah.
These are the two that I wanted to discuss today. I have some questions and want to know your opinion on one of Keelix's messages as well, on the telemetry test follow-up.
I can give you a quick brief on the situation.
And then you can give your views. So, first thing is.
**Pierre Tessier** 06:39 No.
**Shenoy Pratik Gurudatt** 06:39 telemetry test need some images to build on. Like, after… your tests, CI build checks run.
I was in the assumption that it… even the ones that are not merged, we send it to our Docker hub, but we don't. The build checks that run do not save their images anywhere.
And not save Docker artifacts, or even any artifact that I can reuse in my telemetry list.
So the only way to get around this is either we merge those build PR, build CI here in MyTress, or rebuild the images on the PR again, once we get an approval.
Or, Kilik mentioned another way of, just merging both of them, the CI Builder.
And the test framework that we have.
Together.
But that would be a bit different than what we had thought initially, that the build checks be one of our initial gates before even we give an approval, and only after approval, the telemetry tests run.
So, that's where I'm… a bit stuck at and, like, need your opinion. Do you want to merge the build?
of the images for these services, and then run the tests in the same CR.
**Pierre Tessier** 08:05 Because… And they're not shared, so we're… the test is effectively just rebuilding all the images, again, is what you're saying? Yeah.
**Shenoy Pratik Gurudatt** 08:15 Yeah, in the follow-up here, it is doing that right now. Initially, I thought it was saved somewhere, and I just pulled the latest.
**Pierre Tessier** 08:20 You know, there's no cash.
**Shenoy Pratik Gurudatt** 08:21 This one was only the merged ones, so it doesn't make sense at all.
So, there are multiple ways also, if you want to still keep it separate, like, we can… we could have GitHub cache, where the build… CI just builds and saves it in cache, and CI workers can share caches, but cache is only valid till… what, 2 days or something. There's some GitHub limit. And after that, they'll just clear it out. So, for example, if the build images worked.
And then, after 3 days, we approve the PR, the cash is gone. We still need to rebuild from a gold cache, which is still fine, I believe.
This is still fine.
To just rebuild it if cash doesn't exist.
**Pierre Tessier** 09:11 The thing is, though, if the PR changes.
We need to rebuild the images.
**Shenoy Pratik Gurudatt** 09:18 Yeah, that is true.
**Pierre Tessier** 09:22 And we're not doing the immigration test until after it's approved, right?
**Shenoy Pratik Gurudatt** 09:27 Yeah.
**Pierre Tessier** 09:28 Why can't we just cache within the session?
within the same CI pipe.
The workflow?
**Shenoy Pratik Gurudatt** 09:41 different, so… It's not even sure they'll get the same session, like, the worker may be different.
get a worker that spawns this particular new CI for telemetry tests after we approve.
I'm just checking. There was a way to get cash sharing between the workers.
I thought I was looking at good morning.
Anyways, I'll check that as well.
If you can just share it in the session.
There is another approach of loading the artifacts from the build images workflow, and then the telemedic test pulling those built images from the artifacts generated by the CI.
But then, storing those artifacts also have a 10GB limit or something.
**Pierre Tessier** 11:00 Part of me says this is a problem that I don't really care about, Because once we approve it, I don't care, you know, as long as it doesn't take another 35 minutes or something like that, or… And it just, you know.
it does its thing. Like, I don't think we should have the CI test as part of the… It should just be part of an approval process, not part of a merge queue.
Do you know what I mean?
So we don't… we don't make our merge queues slower, we only make the… when I click approve, we run this CI. And if that CI is long, oh well, that's fine. Because we could click approve, and then we can click Merge when ready. And if the CI fails, merge when ready will never hit.
So, from a user perspective, I'm done. I could walk away from this now. I don't need to worry about that anymore.
Are we consuming a lot more resources on GitHub? Absolutely. And we should probably minimize that, but… I don't think it blocks us from going forward now with this, if that makes sense.
You know? I think we should absolutely create an issue, and the way I think about it is, can we cache images per PR? Because one PR will have different images than another PR.
If that makes sense.
**Shenoy Pratik Gurudatt** 12:11 Exactly, yeah, yep.
**Pierre Tessier** 12:13 So, can we just cache images and they stay within just that PR?
If they only last 3 days, whatever, I don't care about that, you know, if you have to rebuild them. But that would be the way I want to look at it, but I just… to me, it seems like a lower priority thing.
Because we only run this when we click approve.
I don't know if we should be running the CI test as part of our merge check. It should only be done as an improved check.
Does that make sense?
And manual. We should be able to kick it off manually anytime we want as well.
I think it'd be… .
**Shenoy Pratik Gurudatt** 12:51 Yeah, because that.
**Pierre Tessier** 12:51 Just because it's a long, it's a heavyweight test.
**Shenoy Pratik Gurudatt** 12:55 Yeah.
**Pierre Tessier** 12:55 And, you know, I was reading a funny thing now on Twitter, and it makes a lot of sense, and it's like.
We run CI tests that check 18,000 different things to fix a typo in a code comment.
This doesn't make sense.
Right? We don't need to do this in our world, but this is what we've built ourselves into, because we need to make sure we retest everything. I think that makes sense, but the longer things should maybe be only called upon when we really, truly need them, which I think is after a PR is approved.
Specifically so we could run these dependent bots faster.
**Shenoy Pratik Gurudatt** 13:32 Yep.
**Pierre Tessier** 13:34 Because dependent bots do create a lot of maintainer toil.
**Shenoy Pratik Gurudatt** 13:38 Yep, yep. I agree.
By the way, typo change can make our weaver checks fail. So yes, we need CIs for typos as well, but we don't need these integration tests for sure, always.
Yep.
Yeah, so what do we do with the PR? Do we want to just go ahead for now, and then work on the optimization of it with the cache?
Something. Currently, it just rebuilds every time you approve. It will rebuild, the images.
And then run telemetry tests on top of it.
**Pierre Tessier** 14:19 Yeah, let's do that.
**Shenoy Pratik Gurudatt** 14:21 Okay.
Then I'll follow up with Kilik, again, and see what… what's his plan as well, or what's his direction that he wants to go, towards.
**Pierre Tessier** 14:37 We can start using your CI right now for all these Dependabots, right?
**Shenoy Pratik Gurudatt** 14:44 Yeah.
**Pierre Tessier** 14:46 Okay, because it's like… A lot. Metabots right now.
1, 2… 4, 5, 6, 7… oh my goodness, 8, 9, 10, 11, 12… 12 of our 16 PRs would depend upon.
**Shenoy Pratik Gurudatt** 15:02 Yep, yep, yep.
**Pierre Tessier** 15:03 And the other one's the one that you're talking about right now that we're gonna move through.
Okay.
In the end, you said health checks. What do you got left, then, for PRs? The MCP service, which we're still waiting on?
**Shenoy Pratik Gurudatt** 15:16 Yeah. Did you get a chance to take a pass on it?
**Pierre Tessier** 15:19 I have not, I'm sorry, I've… And I'm gonna be… I'm missing the next, SIG meeting. I'm gonna be at the AWS Summit next week.
**Shenoy Pratik Gurudatt** 15:29 Oh, nice. It's the New York one?
**Pierre Tessier** 15:31 Yeah.
**Shenoy Pratik Gurudatt** 15:32 Thanks, thanks, thanks.
Me.
**Pierre Tessier** 15:35 Understood.
**Shenoy Pratik Gurudatt** 15:36 The open source team is doing some serverless stuff there.
**Pierre Tessier** 15:41 Oh.
I have a session to talk about Agentic.
Using AI to fix your AI.
**Shenoy Pratik Gurudatt** 15:49 Dominic.
**Pierre Tessier** 15:50 If AI is writing all your code, then why are humans fixing it?
Should AI be fixing its own code, basically, is the nature of the session, but yes, that's what it is.
**Shenoy Pratik Gurudatt** 16:01 Nice. Agents doing agentic observability or something.
**Pierre Tessier** 16:05 I wouldn't call it a gentic observability, I would call it a Gentic SRE.
**Shenoy Pratik Gurudatt** 16:10 Mmm.
**Pierre Tessier** 16:10 Right? Leveraging observability to drive the signal?
But yeah.
So, like, observability is still super important, and it's still needed, and agents should leverage all that, the content from it, the data from it. But if… AI wrote the code that's broken, AI should fix its… maybe another AI, but AI should fix the code that's broken that AI wrote. This is the premise of the… of my talk.
Nice.
**Shenoy Pratik Gurudatt** 16:44 And then…
**Pierre Tessier** 16:44 Okay.
So really, the last one that's really outstanding here is that MCP, right? And then we could really move forward with the release?
**Shenoy Pratik Gurudatt** 16:56 Yep.
That's alright.
**Pierre Tessier** 16:58 the helm… Death that will follow?
**Shenoy Pratik Gurudatt** 17:03 Yes.
It should be better now. Should be better now, with glory.
Only thing is, you need to double-check what it writes.
**Pierre Tessier** 17:15 Yeah, it's… I think it's just… it's… it should be… it'll be fine.
It's a lot, and… I'm not gonna bring over all the same stuff we have from, like, the Docker layer compose files. I think we could do that at a future Helm release, that have similar capabilities there. I think, for the most part, we should just try to get Helm working.
A long time ago, we said it's okay if the way we deploy to Kubernetes is different than how we deploy to Docker.
Because they are two different worlds.
So, I'm more fearful of the Docker Compose… layering of Docker Compose files, that kind of framework, how does that carry over to a Helm world? That's what really concerns me.
**Shenoy Pratik Gurudatt** 18:00 Oh, we still want to do composable health charts.
**Pierre Tessier** 18:04 I think we want to do, like… Right now, when you install with Helm.
You can modify the whole thing, but it's just, it's a lot of effort, so… should we make it easier for you to… you know, right now, with Docker, it's… you get these modes, I guess, and it's easy for you to use any of the modes. In Helm, we don't have the same concept. We don't even have a concept of minimal mode in Helm.
**Shenoy Pratik Gurudatt** 18:30 It's just wrong, long file, single file.
**Pierre Tessier** 18:33 It's just one… it says, you get everything. Here you go, here's everything, and if you don't like the observability, modify the OpenTeometry config part. Seems kind of hard.
It could be better, it could be much more user-friendly, but I think this should be reserved for a post-3.0 launch.
On the Helm side, at least.
Okay, so really, we just need to… finalize this… Mcp.
There's also one more of using zero-code.js instrumentation via NODA options.
Have you looked at this PR?
normal.
**Shenoy Pratik Gurudatt** 19:16 This I didn't see. Okay, no options. Let me take a look.
**Pierre Tessier** 19:21 I've not really looked at it either.
So… oh, you're just gonna use, environment variables instead of anything else.
I don't hate this change.
At all.
I think it's a good change.
Why is there a Claude file mentioned in here?
Oh, it's in a git ignore. Okay, yeah, that's fine.
**Shenoy Pratik Gurudatt** 19:57 Yeah, I don't see a clause.
**Pierre Tessier** 19:59 Yeah, yeah, yeah, yeah, yeah. We pushed agents, right? We're gonna just use agents instead. Or we have a cloud file, and I think the Cloud file just references agents, and agents has their definition of how to do things.
He just added ignore for claw.localmd here.
Oh, this is full auto instrumentation for JS.
Do we have another service that does full-auto dissertation at all for JS?
I don't think so, Ashley, right?
**Shenoy Pratik Gurudatt** 20:43 I don't know.
**Pierre Tessier** 20:45 Okay.
I will review this PR here, this node options one.
I'll put my effort to review that.
**Shenoy Pratik Gurudatt** 20:52 I think.
**Pierre Tessier** 20:52 I think it's a good PR to have. I just want to make sure that we're not duplicating That we don't have the same kind of, workflow elsewhere. Yeah. I like to have one of each, right? One that's manual, one that's auto, one that's something else, whatever, but… you know, in .NET, we have one that's all agent-based, and we have one that's manual, for example.
**Shenoy Pratik Gurudatt** 21:11 Everyone has all the libraries imported, which is also JS.
**Pierre Tessier** 21:16 Which one? Front-end?
**Shenoy Pratik Gurudatt** 21:17 Brandon.
**Pierre Tessier** 21:18 Yeah, front end is super manual.
And front-end Superman, we do a browser and backend instrumentation on the front end.
And I think our only other JS is payment, so it makes sense that payment's all auto, in this case.
**Shenoy Pratik Gurudatt** 21:30 Yeah, does that make sense?
**Pierre Tessier** 21:31 I will review this pair, let's get this one in.
I will trust between yourself and Juliano, if the FCP is great.
**Shenoy Pratik Gurudatt** 21:43 Juliano mentioned that he would take a look, and then… Went on everything.
**Pierre Tessier** 21:47 Of course.
**Shenoy Pratik Gurudatt** 21:48 Yeah.
**Pierre Tessier** 21:49 Okay.
**Shenoy Pratik Gurudatt** 21:51 I know, Donald was also interested, let me ping him separately.
**Pierre Tessier** 21:54 Yes, if we could just get a couple, approvers to just take a good look at it.
**Shenoy Pratik Gurudatt** 21:59 Yeah.
**Pierre Tessier** 22:00 And, validate that it's good to go.
So we could start working on a 3.0 release, which would involve moving all the labels over.
or cutting the release, there's a couple little prep work for it. And then, you know, we'll… probably be a week behind before we get Helm updated, but I'd rather cut the images first and then work on the Helm PR.
Instead of trying to do them in parallel like we've done before.
**Shenoy Pratik Gurudatt** 22:27 Makes sense.
We also had a follow-up for the breaking of Docker Compose for all the downstream, folks.
Warfoking.
OpenTelemetry demo.
**Pierre Tessier** 22:45 I thought what we were gonna do is make a really big blog post to say we broke the demo.
**Shenoy Pratik Gurudatt** 22:50 Yeah.
Should we do it after the release? And that makes, like, a…
**Pierre Tessier** 22:56 I think, you know, as part of us pushing the 3.0 release, there should be a blog post that comes out at the same time.
**Shenoy Pratik Gurudatt** 23:02 Okay.
**Pierre Tessier** 23:03 Like, that same day, whatever. It says, we broke the demo, and we're all proud about it. It's great.
Giuliano said he was already writing that blog, and now you're telling me he's on vacation through next week as well?
**Shenoy Pratik Gurudatt** 23:14 Yeah.
**Pierre Tessier** 23:17 Okay, I'm gonna ping him on Slack, maybe he responds back while he's on vacation?
Just to check and make sure.
That's all we could do.
And it'll take us… A good bit.
I don't think we'll cut a 3.0 next week, but I think the week after, we should be ready to cut a 3.0.
Yeah. So the SIG meeting should be us, like, celebrating cutting a release.
For the week after NAX.
And if it gives us a little bit more time, maybe we do get a little bit more ahead of this helm thing.
Okay.
I'll put the agenda then. I will look at the note options. I'll let you carry over on the MTP then.
**Shenoy Pratik Gurudatt** 24:03 Yeah.
**Pierre Tessier** 24:06 Look at that node options PR, and it is… R… this…
**Shenoy Pratik Gurudatt** 24:15 Also, can you help merge the health check PR?
**Pierre Tessier** 24:20 Yeah, I will. I'll get it merged.
**Shenoy Pratik Gurudatt** 24:22 Perfect.
**Pierre Tessier** 24:24 Shania will work with Donald.
True.
Give final… new on MCP PR.
Which is… this one.
I should call it chatbot PR. MTP's a bad name.
Okay.
Fantastic.
Dang.
I will approve the health check things.
And merge them?
I am going to test… your… CI checks on all these dependabots, and I'll report back.
Alright, fantastic!
Good!
**Shenoy Pratik Gurudatt** 25:22 It would be good if we can get the follow-up PR, in for the delimited test, and then run the Dependabot merges again.
**Pierre Tessier** 25:31 Yeah, I will, I will, sorry. I'll get all the CIs in, everything in for the CI first, and then I'll be testing… I'm sorry, that's what I meant by that.
plan to… work on 3.0 release.
next week.
with… Potential release date of… 2h of this 24, 624.
Okay.
will need… blog post from Juliano.
to the… Published.
Okay.
Fantastic.
**Shenoy Pratik Gurudatt** 26:22 Awesome. Should be good.
**Pierre Tessier** 26:24 Alright, Chanoy, I will not be around next week. I'll be on Slack. Please ping me.
And then the following week, let's finalize all the things, and I'll make sure I'll let Juliana know. Hopefully he reads my messages.
**Shenoy Pratik Gurudatt** 26:37 Yep, yep. Cool. Alright.
**Pierre Tessier** 26:39 Thanks.
**Shenoy Pratik Gurudatt** 26:40 Bye-bye.
**Pierre Tessier** 26:41 Yep.
