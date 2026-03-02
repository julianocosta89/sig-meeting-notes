SIG: Prometheus WG
Date: 2026-01-16
Duration: 60 minutes
Zoom Recording URL: https://zoom.us/rec/share/us3XPyK7N_4SPgd6Q6qu9Jch2q8jJn-YJaMwQxTnYP_uymIooyklmZt22ojgQz9Y.aNHkrGWhJ2nfo9Ac
============================================================

## Zoom Recording Transcript

Arve Knudsen 00:00:18 Hello, can I…
krajo 00:00:26 Hi, hi.
Arve Knudsen 00:00:27 How are you doing?
krajo 00:00:29 I'm good, thank you, just super tired.
Arve Knudsen 00:00:31 Okay, Sorosia, that's…
krajo 00:00:34 Sorry?
Arve Knudsen 00:00:35 I'm sorry to hear that.
krajo 00:00:36 It's fine, it's fine, I'll… Rest over the weekend, hopefully.
Arthur Silva Sens 00:00:43 Hello!
Arve Knudsen 00:00:44 Hello.
krajo 00:00:46 Happy New Year.
Arve Knudsen 00:00:47 pop in here.
Arthur Silva Sens 00:00:49 I mean, we didn't see… Each other this year?
krajo 00:00:53 I don't think so.
But did we…
Arve Knudsen 00:00:57 Maybe they were in the Prometheus Contributors Inc.
krajo 00:01:01 I've also cried.
Arthur Silva Sens 00:01:02 So, Cryo wasn't, yeah.
krajo 00:01:05 Yeah.
But…
Arve Knudsen 00:01:08 This is the last time I'm saying it. It's the 16th, so I think…
krajo 00:01:13 Probably not worth it.
Arthur Silva Sens 00:01:28 Oh, almost a month without meetings.
krajo 00:01:32 Yeah.
I also didn't really work on all the collector for the last month, except one PR.
I've been just busy… too busy with the data, supporting Prometus.
Arthur Silva Sens 00:02:05 Yeah, yeah, no problems. We think we are almost there, and we are definitely ahead of all other components, so…
Good place.
krajo 00:02:14 Right. You can also, use Loren.
From… from our team? Or my team?
Interrupts them?
Stuff.
Arthur Silva Sens 00:02:26 There are stuff, but I… I just tell her, hey, Laurie, go do this.
I don't know your priorities.
krajo 00:02:36 Yeah, I think if you give him
tasks, or suggests, then he'll make time, because
That's kind of what he…
Started looking on my suggestion, and then when there wasn't much to do, he switched to more primitive stuff.
Arthur Silva Sens 00:02:58 I see.
Like, there are a lot of things to do. Maybe it wasn't clear to him.
krajo 00:03:04 But what is…
Arthur Silva Sens 00:03:06 What are those things?
krajo 00:03:08 Yep.
Arthur Silva Sens 00:03:10 Yeah, thanks for the deep, I'll reach out to him.
krajo 00:03:13 No, no.
Also, I don't know if somebody…
Has someone already done the update Prometheus in the collector?
The, just, vendoring, the new one?
Arthur Silva Sens 00:03:29 I'm trying very, very hard, and failing very, very hard as well.
krajo 00:03:34 Cause you know that… Probably to…
At least for native strograms, they are now governed by confirmation, not… Feature flag.
But I guess you would know that. So that should… I think there should.
Arthur Silva Sens 00:03:49 That was already…
krajo 00:03:50 That was already done? Oh, okay, okay.
Arthur Silva Sens 00:03:53 That was on 3.8, right?
krajo 00:03:58 I think 3.8 will still let you do it.
via the… feature flag, if I remember correctly, but I don't know. Again, I'm… I'm behind things now.
Arthur Silva Sens 00:04:12 What I'm seeing, I have a PR predating for Prometheus 3.9.1, I think?
krajo 00:04:21 Yep.
Arthur Silva Sens 00:04:22 But then this PR fails, because on this specific version, Prometheus is requiring goal 124.9.
krajo 00:04:33 Yo?
Arthur Silva Sens 00:04:35 Then, that is because one of the dependencies made this requirement, but then David and I, we worked on… it's a Google PProf.
We'll open up PR to pre-proof, to go back to 124.0.
krajo 00:04:51 I open a PR in Prometheus, this got merged already.
Arthur Silva Sens 00:04:54 So I'm… oopy dating.
The collector to a random commit between versions?
krajo 00:05:02 Oh, that's always fine.
Arthur Silva Sens 00:05:03 And then, yeah, and then there are a lot of appender changes. I'm seeing some behavior changes in saleness tracking as well.
yeah, the PR is up. If you can take a look, you'll see all the changes there.
krajo 00:05:18 Yeah, I don't remember changes to the stillness tracking, other than we did a small feature where I reviewed and merged a small kind of feature for the alloy forks.
To be able to turn off the stillness.
But that's the only thing that I remember regarding the CNS. That wasn't really functional change, it's just kind of an optional feature.
And Oppendorfing, Yeah, that's tricky.
Bartek is pushing… things along with the appender, but it's, it's,
Yeah, it's a bigger change, and… It shouldn't impact Us too much, because…
Currently, the old upend interfaces are still there.
But it will impact us when the old ones are deleted.
David Ashpole (dashpole) 00:06:12 Oh, it's.
krajo 00:06:12 Baby.
David Ashpole (dashpole) 00:06:12 It's so much simpler. It's gonna be awesome.
krajo 00:06:20 A little bit, yeah.
I'm still a little bit hesitant on the whole thing, because we run into problems, as usual, but, like, I don't want to stop it. I don't want to be, like, an old, you know.
Person saying, stay off my loan or something, like, you know, I don't know.
Arthur Silva Sens 00:06:36 I don't know how to stop it, but, like.
krajo 00:06:39 There's some tricky things there.
Arthur Silva Sens 00:06:45 I…
I put one topic, the same as usual, but if anybody has other topics, please do, and we can talk about the civilization after your topics.
Gave some… 10 seconds of awkwardness.
David Ashpole (dashpole) 00:07:08 I don't have topics, but I will… I had a thought.
Which is… Let me write it down in the notes.
I'll steal this.
It's steal 10 seconds, but… so, the declarative config… so the collector wants to go stable, right? And the declarative config needs to go stable.
And…
CodeBotin, I forget. And so, one of the things that's part of that is the Prometheus exporter and its config. We haven't even stabilized the mapping.
I was wondering what people would think about trying to stabilize, like.
just the bare minimum of Prometheus exporter config options.
For the collector to use, so that the name Prometheus in declarative config could be stable, and, like, endpoint could be stable, or path, or something.
Like, something so that it's usable, and we can give it to them, and say, this is stable.
without… It…
I can also see the flip side, where, like, if someone sets those, and then we make a breaking change to, like, target info or something, that they could be upset.
But I do wonder if we can… if it's possible for us to unblock them without, like.
You know, resolving our discussion, for example, on entities or other, like, bigger questions, you know?
Arthur Silva Sens 00:08:37 I think for the exporter, it's easier to stabilize, because an exporter
means that it's gonna be some HTTP requests, and therefore, it is a service, and there's…
And target info just makes a lot of sense for this case,
I, just, like, you want this to be before the Prometus receiver, or after? Because I don't know if we can do both.
David Ashpole (dashpole) 00:09:04 Doesn't matter if it's before or after. I think, like…
I agree, we should do one than the other. The only thing is, like.
If we can stabilize the specs.
then we can unblock both the efforts. There's a lot of, like, legwork that's gonna need to happen, obviously, in the Prometheus receiver, but then…
In the declarative config to, like, actually
Like, market stable, get it released.
get whatever else is needed in the, like, Go OTelConf package, so…
If we can unblock it from a spec perspective, then, like.
I think that's fine. It's more…
Do people… I guess, would it be okay if I opened a PR to stabilize just a couple of the config options? And…
Do we want translation strategy to be stable?
Is the only other question, because that feels like the only, like, big thing I have a question mark on is, like, are we happy with translation strategy? It feels like we did the big redesign, and we're happy with it, but…
Arthur Silva Sens 00:10:13 Yeah.
I feel like it has been some months since I don't see any complaints on that, so…
David Ashpole (dashpole) 00:10:20 Yep.
Arthur Silva Sens 00:10:21 People, people are using.
David Ashpole (dashpole) 00:10:23 So I… I think… I think maybe I'll start with the exporter options.
And then we can try and stabilize other stuff as well.
But I'll probably… If that's okay with everyone on the call, I'll go for that.
But expect to see some spec PRs from me in the next… Few weeks.
Arthur Silva Sens 00:10:55 Would that mean that you were removing the… if I remember correctly, the Prometus Exporter config has some fields, like…
Remove, units of fixes, remove types of fixes, or something like this?
I…
David Ashpole (dashpole) 00:11:11 Those would just remain marked experimental.
Arthur Silva Sens 00:11:15 That's okay.
David Ashpole (dashpole) 00:11:16 And then the declarative config.
Would have to gate those behind, like…
an environment variable, a feature gate, or something, right? So, you wouldn't be able to access them… you would be able to access them if you turned on a feature gate.
like, set an environment variable, but you wouldn't be able to access them just straight out of the box. So, it's kind of in line with the whole, like, stable-by-default OTEP stuff, where, like, you have to do extra work to turn on experimental things.
Arthur Silva Sens 00:11:44 Okay.
Okay, that, yeah, that works for me.
David Ashpole (dashpole) 00:11:48 Okay, cool.
You can have the floor now.
Also, Happy New Year, everyone. I think this is the first time I've seen… See you guys.
Arthur Silva Sens 00:12:01 conversation.
Yeah, Happy New Year. I had the same conversation at the beginning of the call.
David Ashpole (dashpole) 00:12:06 Sorry.
Arthur Silva Sens 00:12:10 Okay, I'm gonna share my screen and talk about the receiver now.
Move you up.
Oh, this is it. I… yeah… officially…
fitting in one screen, before I had to scroll down.
Should I go to the ones in progress, and then we go to the others?
David Ashpole (dashpole) 00:12:51 Sounds good.
Arthur Silva Sens 00:12:53 First one is considering separating permit to service discovery from receiver module.
I worked on a few PRs upstream, and now Prometheus can remove, service discoveries with build tags.
But then, to make this work in the collector, we need to bump the version of Prometheus.
And that's what we were talking about, Cryo.
David Ashpole (dashpole) 00:13:22 That's… that's fine, I think.
Arthur Silva Sens 00:13:25 Yeah.
It's good. Goosebump?
Yeah, but this is getting difficult. Like, every time I bump to a new version, I see random new tests failing.
Now, I'm seeing, timeouts…
on metric, this is test… Test metric relabeling.
Locally, it passes every time.
on CI, I triggered this at least 5 times now, and it failed every single time.
So I'm not sure what to do with this one.
There was the…
David Ashpole (dashpole) 00:14:07 PR to improve the test timing.
From someone else.
Arthur Silva Sens 00:14:15 Yeah.
I don't think this problem is about test timing. Like, the PR that this other guy did is just…
it reduced the scrape interval from 1 second to, I don't know, 50 milliseconds.
That doesn't change anything.
David Ashpole (dashpole) 00:14:32 I'll just… so, okay, so this is… this is timing out after 15 minutes.
Right?
Arthur Silva Sens 00:14:38 Yes.
Yeah, the timeout would be shorter, yeah.
David Ashpole (dashpole) 00:14:41 Like, if we're doing all the tests way faster, then hopefully it shouldn't take 15 minutes.
So basically what you're saying is your computer is too fast.
And it's actually passing the tests instead of failing them.
Compared to CI.
Right? Like, that's what we learned?
Arthur Silva Sens 00:15:02 That sounds weird, a test shouldn't take 15 minutes.
David Ashpole (dashpole) 00:15:06 Have you run?
Our tests, like, they take, I would say, 5 minutes for me locally.
They would…
Arthur Silva Sens 00:15:17 Do you think… do you really think this is a timeout problem? Like…
I feel… I feel like this is… something is stuck there, and then because it's stuck, we breach time out.
David Ashpole (dashpole) 00:15:28 I…
krajo 00:15:29 Do you say the same thing in every trace? Like…
David Ashpole (dashpole) 00:15:34 That's true, that's a good question.
Oh yeah, is it always?
Arthur Silva Sens 00:15:37 this metric.
David Ashpole (dashpole) 00:15:37 renaming keep action. If it's the same failure, then that would be suspicious. If it was just, like… Yes, yes.
Okay.
Arthur Silva Sens 00:15:44 It is the same fader every time. It always does test.
David Ashpole (dashpole) 00:15:49 So that's probably some race, but… It does seem like…
It's likely some weird timing change, but it's… the bigger issue is probably just that our tests are not, like, super predictable, right?
Arthur Silva Sens 00:16:07 Yep.
krajo 00:16:10 But do comment out this test, run it, and see how long it takes.
Without it.
NCI.
David Ashpole (dashpole) 00:16:18 You can also, right, we can also merge this with, like, a test skipped and open an issue, so that it's not blocking… because, like, each time…
This waits another day, you have to do the whole…
version pump again, right? So, like, that's not tenable for you, so…
If it's just this test, skip it and do the update, and then open an issue, and we can prioritize fixing it.
Arthur Silva Sens 00:16:40 David, do you have time to… if I add this skip today, do you have time to review
And, possibly paying someone so much.
And I'll do this after the call.
David Ashpole (dashpole) 00:16:51 Ping me as soon as it's ready, okay?
And that goes for other PRs, too. Like, I will review things if you ping them to me on Slack.
Quickly.
Arthur Silva Sens 00:17:11 Okay.
So, bumping… Promise shouldn't block this one.
this… is about…
David Ashpole (dashpole) 00:17:25 Hmm, this is the one where I was like, what if I open a can of worms?
Arthur Silva Sens 00:17:29 A new contributor opened up PR that adds two metrics.
the amount of metric… metrics that we attempt to translate, and the amount of metrics that we drop because the translation fader. The translation, I mean.
Prometheus… Product buff format to OTLP.
It's not about naming, it's about the data format, the objects.
And, David opened a few questions, pinged a few OpenTelemetry maintainers.
Because it would be a lot more helpful if,
The ops report could also say… could have a metric about metrics dropped.
But we didn't get any answers from them.
I don't know, should we ping them again?
David Ashpole (dashpole) 00:18:21 I'm gonna open an issue in OpenTelemetry Collector, not in Contrib, about this.
And ping them directly there.
Arthur Silva Sens 00:18:31 If that's alright.
I wanted to also say that we already have a PR open for adding dropped But it's for exporter.
We… then we would need something very similar, but for a receiver.
David Ashpole (dashpole) 00:18:48 Well, so this is… I guess, do we want dropped separate from refused?
Because there is a receiver-refused metric, right?
Arthur Silva Sens 00:18:59 Oh my god.
David Ashpole (dashpole) 00:19:00 I guess we got them, and then we were like.
We just want to drop them instead.
Arthur Silva Sens 00:19:09 I think we would need to understand the semantics difference between refused and dropped.
I have no idea what's the difference.
David Ashpole (dashpole) 00:19:18 Well, clearly someone thinks there's a difference in this PR, because I think.
Arthur Silva Sens 00:19:21 Yeah. I think there's…
David Ashpole (dashpole) 00:19:23 There's failed, so I don't know what the difference is between dropped and failed.
Failed is maybe, like, the person who…
We tried to send it to. Rejected it.
I don't know.
Arthur Silva Sens 00:19:39 And… Then…
David Ashpole (dashpole) 00:19:41 Can you click on.
Arthur Silva Sens 00:19:42 This failed… this failed could work if there is, like, an extra label there of, like, reason. It failed because…
The receiver that we send the metrics to rejected, or failed because we failed the translation internally?
David Ashpole (dashpole) 00:19:59 Or something like this.
I guess, in terms of discussing this issue, do people… agree that… Reusing the…
Obs report metrics is the right direction here.
Arthur Silva Sens 00:20:18 I feel like this would be awesome, because other receivers, other exporters may also benefit from that.
David Ashpole (dashpole) 00:20:28 Well, and if someone has, like, a generic alert on receivers failing to do stuff, then…
These cases will be gone, right?
Arthur Silva Sens 00:20:37 Yep.
Beautiful.
David Ashpole (dashpole) 00:20:41 Can… what issue number was the… there was the one about exporter dropped?
Or I can also just try and find it.
Arthur Silva Sens 00:20:47 It's 44196.
Oh, sorry, you meant, exporter dropped?
David Ashpole (dashpole) 00:21:01 This is an old one.
Arthur Silva Sens 00:22:36 This one is about the metrics that we are adding for appending and commit.
This is also another metric that we are adding upstream, and needs the bump.
To… to… to close this one.
David Ashpole (dashpole) 00:22:54 Just needs a rebase? No.
Oh, yeah, yeah, okay, cool, awesome.
Arthur Silva Sens 00:22:59 It's about these two metrics here.
Script, commit, and total duration.
If we get the bump, then we get this as well.
David Ashpole (dashpole) 00:23:13 Awesome, awesome.
Arthur Silva Sens 00:23:21 Oh, one of the workable items, we don't have anything open yet, is eliminate time dependency in tests,
We have one PR from a…
one of the OpenTelemetry maintainers, I think, or approver. He… he didn't eliminate the time dependency, he just switched the task intervals from one second to, like, a few milliseconds.
it… It changes the… the total time to test from 5 minutes to, like.
50… 5 seconds, something like this, something super small.
But we still depend on time, though.
David Ashpole (dashpole) 00:24:01 Yep.
Arthur Silva Sens 00:24:02 I don't know if we are happy with just this, or if we really want to go after sync tests, or clock injection, or anything else.
I'm not following if we… Sorry, go ahead.
David Ashpole (dashpole) 00:24:19 Alright, you finish, and then I'll say what I was gonna say.
Arthur Silva Sens 00:24:22 I was gonna say that I'm not following the flaky test anymore. I don't know if our tests are still flaky because of this.
David Ashpole (dashpole) 00:24:33 I haven't seen too many new flakes.
Or comments on the old Flake issues. I'm pretty sure there are still, like.
Quite a few of them open.
But… Honestly, it would just be really nice for development.
Because running our unit tests takes a long time.
Arthur Silva Sens 00:24:56 Yeah, I don't… I don't have a problem merging that… that guy's PR.
David Ashpole (dashpole) 00:25:01 Yeah, we can also then undo it if we… I guess it's a question of, like.
One, do we think we actually will address this in the next… say, month?
If so, maybe we should block his PR and do this instead.
But if we don't think we're gonna get to it, then I think it's totally fine to just make incremental progress.
Arthur Silva Sens 00:25:23 His PR has just changed the intervals. I don't see why we would block his PR, because we are working on this as well.
David Ashpole (dashpole) 00:25:29 It adds a bunch of, like, cruft to the actual receiver. It's not, like, a test.
Arthur Silva Sens 00:25:33 Oh, really?
David Ashpole (dashpole) 00:25:35 Yeah, yeah.
It's like, there's plumbing, and…
It makes the code, like, it certainly makes the code a little harder to read, but it's not like…
the end of the world. Got it. Yeah.
Arthur Silva Sens 00:25:47 Owen reached out to me this week. Okay, go ahead, Cryo.
krajo 00:25:52 I just wanted to say, in general, I hate timeouts. They do cause freakiness, they do… they can run into, like, with scrape especially, you can run into a situation where you…
miss a script or something, and then you might never get your data, meaning that you time out after 15 minutes. I wouldn't be surprised if
If that was a problem.
So… But on the other hand, like, right now, I have zero time for this, for sure.
David Ashpole (dashpole) 00:26:21 Yeah.
Arthur Silva Sens 00:26:25 Yeah, I've been playing around with sync tests for a while now, and I…
I have a feeling that SyncTest doesn't work for this, but every time I say it out loud, somebody comes to me and say, no, it should work.
And I don't know if I'm doing something wrong. But, Owen… Owen reached out, earlier this week, saying… asking if he could take this test for me, and I said, please do.
But, I feel like he's… his priority is the Delta.
Work, not this.
krajo 00:26:56 Yeah, for sure.
I mean, I think, yeah, we talked about the fact that going through the HTTP, so basically, I don't know if it's a TCP thing or local, like, a Unix socket.
That's getting cold, but that's the problem. That's not really working well with the sink.
But… I thought that you could always You know, replace the… Transport channel.
and use channels, and that works with Sync, so…
again, I think there's probably a solution, but, like, it's not… may not be trivial or, like, easy to do, which, again, points to…
Kind of a longer-term project.
Arthur Silva Sens 00:27:41 If we add channels, that would go to the script manager, or this goes to our tests… Ollie.
krajo 00:27:51 It would have to be in tests only, like, I'm talking about…
if the problem is indeed the fact that we are using TCP, and, you know,
basically system calls, I guess, underneath.
then the solution would be channels, because that's handled by Google. So sync tests should work with that.
But maybe I'm talking out of my ass, like, I haven't…
You know, dove into it.
Arthur Silva Sens 00:28:27 Damn.
I can try… I can give this another go that I fail every time since… since I started trying.
Hey.
the other one…
David Ashpole (dashpole) 00:28:52 Do we…
Arthur Silva Sens 00:28:53 workable.
David Ashpole (dashpole) 00:28:54 Do we think that that should block…
I mean, it's… it would be nice to have. I don't know if it should block our stability.
But I'm also… it does result in a lot of flakiness.
Arthur Silva Sens 00:29:13 Yeah, maybe not block stability.
But it's, like, a very good to have.
David Ashpole (dashpole) 00:29:19 Yes.
We'll make all of our lives easier. Yep.
Arthur Silva Sens 00:29:29 The other one that is workable is…
We have a configuration option called Report Extra Script Metrics.
We already opened a lot of… PRs for this?
the idea is that this is… this should not be a config option, because it's a feature flag in Prometheus.
So we are removing the… the config.
And we cannot just remove all out of… out of nowhere. We will add a feature flag.
So, that's where… when it gets confusing. We replace this configuration option with a feature flag, because in premise this is a feature flag, but we also need an extra feature flag for removing the config option.
Yes, Greg?
krajo 00:30:19 Wait, didn't I review and merge a PR from you to…
Arthur Silva Sens 00:30:24 Yes.
krajo 00:30:24 make this not a feature flag in Prometheus? I'm confused.
Arthur Silva Sens 00:30:29 Yes.
Let me explain.
By showing the code.
Or in Prometheus.
I open a PR to remove the feature flag and add the configuration to the prompt config, right?
krajo 00:30:56 But we have…
Arthur Silva Sens 00:30:58 this as well.
Yeah, sure. And this is the same thing.
So, since, extra script metrics is already on prompt config.
This doesn't need to exist, and this is about removing this one.
Does that make sense?
krajo 00:31:16 Yeah, yeah, it makes sense. Oh, and you're talking about the fact that you cannot simply remove it somehow, like, just.
Arthur Silva Sens 00:31:22 Yeah. Deleted. Needs to be done in a few releases.
krajo 00:31:27 I mean…
It's kind of weird that we are trying to work towards stability, but we are hampered by this kind of thing, but yeah.
Arthur Silva Sens 00:31:36 If we were alpha, that would be fine, but since it's better, there are some extra rules, and even for better, we need to be careful.
Yeah, but this is super easy. Like, I think the feature gate for removing is already in place.
Just needs to wait two releases, I think, and two releases is, like, a month?
And after one month, we can… we can just simply remove.
I guess this is not workable, actually.
What is the latest?
43…
Then we have some… things under discussion, like documentation.
I have no idea how to solve this,
I'm doing a mentoring program, starting in March. It goes up until May.
it's focused on tech writers. I got some tech writers from Grafana working on this as well, and I'm so… I'm trying to solve the general
it's not focused on Prometus receiver documentation, but it… it is Prometus and hotel, so it touches…
Prometheus Docs, hotel docs, and Component Docs.
Eventually, we'll get to you, but…
I don't know if we want to wait, like, the mentorship is gonna end in May.
But I'm also terrible at documentation, I don't know what to do.
notes, thoughts on this, I'm gonna go to Community Support.
Community support says… No, sorry.
The component instability document says.
That bugs and performance problems should be reported, and there's an expectation that the component owners will work on them.
Breaking changes, including configuration options and the component's output, are not expected
To happen without prior notice, unless under special circumstances.
A component must have at least 3 active codowners.
Like, this… Solved… the other… Like…
Do we need a process? Do we need to establish a process for this?
Like, if a bug or performance problem is… issue is open.
Is there something that monitors how much time it's open and who is responding? I have no idea.
David Ashpole (dashpole) 00:35:02 I think… I think we would,
Maybe the best thing is for us to just set aside
The last 15 minutes of the meeting or something to do triage.
And, like, just something like that that's lightweight.
I think it's fine.
The idea is just, like, we should try and make sure things don't fall through the cracks, so it wouldn't be focused on whatever the newest thing is, because presumably the code owners can get to most of that.
But, just to make sure that, like.
If something has sat around for a while, then it doesn't fall through the cracks entirely.
What do people think?
Or do you want to have more process?
We can do dev stats, but I don't think that gives us component-level stuff, and I don't want to.
Arthur Silva Sens 00:35:57 Yeah. Like…
David Ashpole (dashpole) 00:35:58 Over-engineer this, either.
krajo 00:36:02 I mean, I already get, or we already get, you know, pinged on GitHub on new issues and PRs, but sometimes, like, this week.
I didn't have my OSS day, so I basically couldn't look.
So, I like the idea of triage, too.
Make it a little bit more personal, and sometimes it's…
valuable to discuss, like, very briefly before we do anything. It could save us time, I think.
So, I… I like that.
David Ashpole (dashpole) 00:36:36 Right, yeah.
Arthur Silva Sens 00:36:36 I'm also…
David Ashpole (dashpole) 00:36:40 I'll just say, we get a lot of volume, so I don't think we can triage everything in person. But I think, like.
We'll do best effort to respond to things as they come up, but there's gonna be stuff that we miss, and we can triage those together. And that hopefully should be enough to, like, satisfy this requirement.
Arthur Silva Sens 00:36:58 Well, what I'm also… what I'm thinking is that,
For example, we are preparing the permitius receiver to be stable
Independently, if any of, you know, any of us, is working on it, like…
Cryo, sometimes doesn't have time. I don't know what my priorities are gonna be for the next year.
Like, if I need to step down, how to ensure
That the community part's still… is still happening.
David Ashpole (dashpole) 00:37:30 I mean, like, we'll have to…
Send out a request for new code owners.
You know.
See if there are people who are interested.
And we should also… I mean, I think we're actually in not a very bad place compared to other groups I've been a part of. Like, we do a lot of, like, LFX mentorships and those kinds of things that tend to bring people in who are interested in becoming maintainers.
Arthur Silva Sens 00:37:58 I guess, I guess if we leave, it's also collector sick's problem to find people
If this component is really, really important to them.
That's…
Config coverage.
specifications.
the document about stability also says.
Unit test suit should cover all configuration options.
I'm pretty sure we cover all configuration options to an extent. For example, we don't cover all service discoveries from PromConfig.
But, like…
should we make this more explicit? Like, this is the test that we'll do that will exercise all the config options.
Oh, I still…
krajo 00:39:03 What do you mean? Sorry, what do you mean by that?
Arthur Silva Sens 00:39:07 we have a lot of tests that I'm pretty sure covers almost everything, like, at least as much as possible, but they are always catered around, like, some, like, we have multiple test files in different locations.
There is no flexion.
David Ashpole (dashpole) 00:39:23 just the, like, configtest.go stuff. This is not, like, actually making sure the config options work.
Right?
Arthur Silva Sens 00:39:33 Why would a test… Just test config option.
David Ashpole (dashpole) 00:39:37 Just test that you can parse the config.
Arthur Silva Sens 00:39:40 This is auto-generated then, right?
We have…
David Ashpole (dashpole) 00:39:47 Is it now?
Arve Knudsen 00:39:55 Is this something you could call… is this something you could consult an LLM about?
like.
Arthur Silva Sens 00:40:02 following me.
Arve Knudsen 00:40:03 I mean, I think that's, like, a perfect case for an LLM, like,
I mean, Claude found that, for example, that config fields were not copied, I think, in Prometheus.
So it… that's very… it's not exactly the same, but it's very similar.
Arthur Silva Sens 00:40:21 We are just… If you're just… Testing if the… it's parsable.
That should be an easy test.
And yeah, LLM could definitely do that.
Arve Knudsen 00:40:36 Yeah, so that would be my first step, just, like, have an LLM, you know, try to solve this issue.
David Ashpole (dashpole) 00:40:45 We already also got permission that, like, we don't need to test the full surface of the Prometheus servers config.
We just need to test our extra options that come in the… Receiver.
krajo 00:41:00 So we should make sure to remove as many as possible before starting it in.
David Ashpole (dashpole) 00:41:04 That's basically what we're doing, right?
Arthur Silva Sens 00:41:06 We are removing a lot of stuff.
Arve Knudsen 00:41:13 I didn't mean to say that an LLM can build a test, I'm saying that an LLM could kind of, like, tell us whether any config fields are missing.
From, from, from tests,
you know, like, it could say to which degree, config fields are covered by tests. That's what I was saying.
And I think if I were to do this, I would actually… I would point LLM at this issue, and then, like, ask it to kind of parse the issue and tell you whether it's,
Whether it's met or not.
the, yep.
krajo 00:41:53 It would be quite sad if we didn't cover all of them.
David Ashpole (dashpole) 00:41:57 There's only.
3, right?
Arthur Silva Sens 00:42:00 Yeah. Like…
David Ashpole (dashpole) 00:42:02 Not that many.
Arthur Silva Sens 00:42:05 Yeah, but then, I think, yeah, we already…
Pablo already told us that we don't need to cover it, but prompt config is huge, and target allocator is huge as well.
David Ashpole (dashpole) 00:42:16 Okay, so we do need to make sure…
We'll look at the target allocator one, but the rest of these, like… oh, and the API server one, too. Start… but all the start time ones are gone, report extra…
Oh, trim metric suffixes, did we ever talk about this? No, we're keeping that, right?
Arthur Silva Sens 00:42:33 Yeah, we're keeping it.
David Ashpole (dashpole) 00:42:34 Those 3 were removed.
Arthur Silva Sens 00:42:36 So we only have Prometheus config, target allocate… Prometheus Config, three metrics to fix this, target allocator, and API Server.
David Ashpole (dashpole) 00:42:44 Yep, yep, yep. Okay, so it's not… it's not too bad. They're, like, 5.
Arthur Silva Sens 00:42:49 I don't even need an LLM for 4.
configs, I guess.
But yeah, LLM will probably cover if there are, like, nested objects.
David Ashpole (dashpole) 00:43:08 If someone wants to use an LLM, they can. I… as long as they abide by the new GenAI use policy.
And disclose that your PRs are partially… All I'm generated.
I don't know if you guys saw that.
The community repo.
Arve Knudsen 00:43:25 I have not seen that. Is that, like, a requirement now for all the old OpenTelemetry repos?
David Ashpole (dashpole) 00:43:31 I think so, yeah. It was just funny listening to the discussion.
krajo 00:43:36 Why? Like, what was the reason? People are annoyed? Is that the only reason, or, like, is there some…
David Ashpole (dashpole) 00:43:41 I mean, I don't know if you've tried to review some of the PRs that are LLM-generated, but they're.
krajo 00:43:46 Oh, yeah.
David Ashpole (dashpole) 00:43:47 Full of garbage, and like.
You think you're spending time with a human, when actually, like, you're just going back and.
Arve Knudsen 00:43:52 That's weird.
And it's wasting your time. Okay. Yeah, so it's sort of like to try to filter out the spam, I guess, because I think I see, I've seen…
Like Mitch Lashimoto has introduced such a policy, right?
Or, maybe not…
maybe not him, but someone, someone, like, prominent did. And I think… I think they said it's not… it's not because they're against AI, it's just to kind of, like, feel crowd noise.
David Ashpole (dashpole) 00:44:19 It… well, it's… it's one thing… I think it's when… when PR review gets really difficult.
Right? Like, when someone is not responding well.
Like, it's nice to know whether it's because it's an LLM and you're wasting your time, or whether you're actually helping a human learn.
Arve Knudsen 00:44:38 Hmm. Yeah. That's, that's true.
krajo 00:44:42 And is there a, like, Percentage of… what, like, how do you define
You know what, I don't want to spend time on this, I don't care. Okay, never mind.
David Ashpole (dashpole) 00:44:53 Okay, yeah, we can go to another topic, but…
Arthur Silva Sens 00:44:58 Last, last topic is the spec.
I think we want to stabilize this back. Yeah, David.
But also, there is… a very old PR that I've also had a hard time
This part of the spec we still haven't implemented.
When we…
David Ashpole (dashpole) 00:45:21 When we scrape.
Arthur Silva Sens 00:45:22 a metrics endpoint, and the metrics have these labels, or telescope, and then attribute.
Today, we… they… those become, normal labels, normal metric attributes, but they should be scope attributes instead.
David Ashpole (dashpole) 00:45:40 Yup.
Arthur Silva Sens 00:45:43 I had a PR a very long time ago.
It was very close to finish.
Oh yeah, this is the one where you have, like…
David Ashpole (dashpole) 00:45:52 Weird bugs or something that you couldn't figure out.
Arthur Silva Sens 00:45:56 No, like, the code was just too difficult to review, I think.
And then the reveal got stale, but then now the receiver… the codebase is totally different, and we… I can just revive this.
Yeah, this needs to be done.
But, this pack, you're saying that you were gonna take care of this one?
David Ashpole (dashpole) 00:46:22 Yeah, I'll take care of it. It's… you can assign… or is it assigned to me? That one's assigned to me.
Arthur Silva Sens 00:46:27 Yeah, I think so.
David Ashpole (dashpole) 00:46:29 I just… I open the issues, and then I meant to open some PRs, but I haven't had time.
Arthur Silva Sens 00:46:34 This is different from the… the one we talked at the beginning, about the config… the collective config?
Okay, so you want to stabilize both.
David Ashpole (dashpole) 00:46:43 It's like, to allow the config sig to unblock and, like, start moving.
forward somewhat.
Just… yeah. Just to allow them to parallelize things a little bit.
Arthur Silva Sens 00:46:57 And I don't… it seems like it's almost blocking, like, the stabilization of declarative config.
David Ashpole (dashpole) 00:47:02 As a general concept.
So…
I just want to get out of their way, and I feel like there's no good reason for us not to stabilize some basic stuff.
Arthur Silva Sens 00:47:13 Sounds good.
Cryo?
krajo 00:47:17 I just wanted to comment on the other one, the… Autoscope labels?
Arthur Silva Sens 00:47:29 Yep.
krajo 00:47:30 Oh, yeah, so if you open up PR, and if you ping me directly, I'm not saying I will immediately review it, but I'll get to it.
In, like, in a couple of days, that's my kind of throughput right now.
Arthur Silva Sens 00:47:44 I think you were… you were not a… Co-owner back then.
krajo 00:47:52 Maybe. I don't remember it, to be honest, but I recently reviewed something for Eric Wu, that was…
Oh, that was for metric names, but, like.
I'm kind of familiar with the code all around, so, like, I have a good chance to review it.
But, but…
Duping me.
Paul's book.
Arthur Silva Sens 00:48:12 Yeah, just to clarify, I'm… yeah, sounds good. If I open a PR in the future, I'll ping you. But, like, this PR was May last year. I think you were not a coded owner.
Yet.
a super old PR.
krajo 00:48:25 Maybe.
Again, don't remember, too old.
Okay.
Arthur Silva Sens 00:48:35 That's it.
David Ashpole (dashpole) 00:48:37 Yep. We have 10 minutes.
Arthur Silva Sens 00:48:39 If you want to triage, or…
David Ashpole (dashpole) 00:48:41 But feel free to assign things to me. But I need to drop.
Arthur Silva Sens 00:48:47 Okay. Sounds good.
krajo 00:48:50 I do have one question.
Hey, bye.
Arthur Silva Sens 00:48:53 No, it's just that.
krajo 00:48:56 again, I'm behind things, but, like, native histograms is now stable in Prometus.
So… And I guess we are still having a feature flag in the Prometus receiver for NetSuums, right?
So…
Arthur Silva Sens 00:49:11 Take a look.
krajo 00:49:13 Maybe it's changed already, but, like, my last recollection is feature flag.
So that's something that we could just… Remove, basically. And document it.
Document. How do you… Scrape.
You know, native serums.
Arthur Silva Sens 00:49:35 I'm looking at the README, I can already see…
Mentions of script native histogram in the script config?
krajo 00:49:46 Oh, okay, okay, good.
Arthur Silva Sens 00:49:49 Let me see if there's feature flags… Yeah, but the…
It's… it has a feature flag called Enable Native Histograms.
krajo 00:49:57 Yeah, that's.
Arthur Silva Sens 00:49:58 It is…
krajo 00:49:59 Basically.
Arthur Silva Sens 00:50:00 It is stable, so it's on by default.
krajo 00:50:04 Okay. So, in, like, in a couple of…
releases, we can remove that, right?
Arthur Silva Sens 00:50:13 Yeah, I don't remember which release we changed to stable, but two releases after that, we can just remove it.
krajo 00:50:20 Okay, good, alright, done.
That's fine.
Thank you.
Arthur Silva Sens 00:50:31 Oi?
so, should we end here? Or anything else to discuss?
krajo 00:50:40 I mean, David mentioned the triage. We have 10 minutes. Is there some old, stale issue or PR that we should discuss, maybe?
Arthur Silva Sens 00:50:50 Take a look.
Let's start with not trash.
krajo 00:51:10 Oh, there's 9… oh yeah, there's only 3.
Yeah, please.
Arthur Silva Sens 00:51:17 Enable using memory limiter extension.
I have no idea what this is.
krajo 00:51:25 Yeah.
How is this related to the receiver? It seems totally generic.
Arthur Silva Sens 00:51:55 This extension can be used as an extension for all HTTP and gRPC receivers.
We are not…
I go through config HTTP.
We don't use ConfigHTP, right?
krajo 00:52:18 Yeah, we don't need that. We're not that kind of receiver.
Or maybe that's the problem.
Arthur Silva Sens 00:52:26 Oh, there is an answer already.
krajo 00:52:28 Oh, okay.
Arthur Silva Sens 00:52:31 I… 25 minutes ago.
krajo 00:52:34 Right.
Multitasking.
Okay, I mean, David replied, so we don't have to look at this.
Another one…
Arthur Silva Sens 00:52:49 failing tests.
Export when all is enabled.
I mean… If it failed, Doesn't need to be trashed.
Last week, 3 days ago, 2 days ago.
Seems consistent.
The remote right receiver, returns failed sample message back to Prometes.
When target info is not in the payload.
krajo 00:53:53 Huh.
But unknown if… Approve it, we'll try it.
What?
That makes no sense, like, RemoteRite doesn't care about target info, like, at all.
Step 2.
Arthur Silva Sens 00:54:13 Does… This is the receiver, right?
krajo 00:54:17 Yeah, yeah, but still, like, what I… like, remote ride doesn't care. Like, audio IP… If you…
I don't know if we ever care about targeting fool, like…
Arthur Silva Sens 00:54:34 The receiver cares, because it needs the target info to rebuild the resource attributes.
krajo 00:54:41 Oh yeah, I see what you mean. Yeah, yeah, yeah, you're right, you're right, you're right.
Yeah, this looks legit bug, then.
Arthur Silva Sens 00:54:57 Send V2 requests with 4 samples.
Got 200, but the responsibility statistics indicates Nothing was accepted.
If we receive only the target info and nothing else, we wouldn't… Generate any metrics, any samples.
Because we are just building the resource, attributing nothing more.
Could that be it?
krajo 00:55:29 But he says he sends other things, but…
The problem goes away if he's not… Including target info. So…
Arthur Silva Sens 00:55:42 Yeah, if he's not sending the target info.
Then the sample is just created without any attributes.
But if it's the target info and nothing else, then we are just building resources, attributes with nothing.
With nothing in the resource.
krajo 00:55:59 Right, right, but I don't think… Yeah, I… it…
So, my guess would be that, the data in Target Info is wrong somehow.
Maybe it has a… label that's weird or not transmittable or something, but Seems like alleged…
problem, but… We could ask the person to… Provide a sample? Like… Meaning…
A sample of target info and a metric to try to reproduce in a unit test, like.
So that we don't have to…
You know, build this out.
Arthur Silva Sens 00:56:56 You're asking for, like… Isn't this the… Way to reproduce.
krajo 00:57:07 Right through the config source labels, name generated, or… What?
Keep…
No, that… I mean…
I mean, I assume that we have some tests for target info, so…
It should work, but in his specific case, it doesn't work, which tells me that he has some kind of data that
Make this fail.
Arthur Silva Sens 00:57:45 I wouldn't assume that we have tests.
I think we do, but I… but let's… let's check.
krajo 00:57:55 That makes me sad.
Yeah, I'm less familiar with the receiver than the… I mean, the remote right receiver than with the Prometus.
Receiver.
Yeah, so we probably have… It's going.
Arthur Silva Sens 00:58:12 But I… I think we don't have a test for only target info and nothing else. Like, this has…
Target info, but it has the metric.
Together.
But, if I remember correctly, Prometheus doesn't send several things at once, right? He… No.
It sends only one sample, but it sends a lot of samples
It sends one sample for a time series, but sends multiple time series, okay.
krajo 00:58:44 Yeah.
By the way, depending on that, you will get the series and your target info in the same message.
Like, that's not how the word works, basically.
Like, you can cut up remote write messages in any way to fit them the size limit, so…
Yeah.
Yeah, that's a good question. I think he's sending more than just the target info, but let's, let's verify. Yeah, that's a good question.
Maybe I'm just misunderstanding this.
Arthur Silva Sens 00:59:54 We are at times…
krajo 00:59:55 Yep.
Arthur Silva Sens 01:00:00 Nice to see you again.
krajo 01:00:02 Nice to see you. Bye-bye.
Arthur Silva Sens 01:00:04 Bye-bye.
