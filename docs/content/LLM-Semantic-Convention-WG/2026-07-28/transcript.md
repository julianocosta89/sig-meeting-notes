SIG: LLM Semantic Convention WG
Date: 2026-07-28
Duration: 133 minutes
============================================================

## Zoom Recording Transcript

Liudmila Molkova 00:59:27 Hello! Hi, everybody.
Huxing Zhang 00:59:35 No.
Steve Rao 00:59:40 Yeah, hello.
Ziming Liu 00:59:45 Hello?
neil yashinsky 00:59:51 Hi there.
Liudmila Molkova 00:59:52 Give me a sec.
Okay… So let's get started!
The… blog post.
I think we started talking about it last time.
Huxing Zhang 01:01:05 Yeah, but we didn't have any next steps, I think. I'm not sure if I can do anything I can do before. I'm planning to, like, send the PR to the… official OpenTelemetry.io report. Is there any actions I should do, I should take?
Trask Stalnaker 01:01:33 I know the one thing we wanted to… that you brought up… was… we brought up last week was the… conformance.
Link.
And… into Open Telemetry.
Liudmila Molkova 01:01:53 Yeah, I've been thinking a little bit about it. It's not strictly… For the blog post.
But… Okay, I'm thinking this.
We can, and I just did.
brought up the confirm and story we have, to Python Genie AI.
I have a PR that effectively just runs the scripts that you Trask have in the Semcock Gen AI here.
And it generates the same… Data. Oh, I'm sorry?
Trask Stalnaker 01:02:39 Oh, the markdown.
Liudmila Molkova 01:02:42 Yeah… So cool.
Okay, alright.
Am I showing that?
Trask Stalnaker 01:02:52 Kind of like a code coverage.
Liudmila Molkova 01:02:55 Yeah. Report.
Yeah.
But I'm thinking it does not… So, it's just a part of the story. The other part I want to have is that Today, the conformance test here, it's a little bit involved.
It's like you have a lot of stuff.
R… What if we just… got, like, we would get a script, some Python code.
We would get, some minor stuff to run it, like performance text and whatnot.
And we would be able to run this conformance suite on whatever.
We would be able to cover native instrumentation, third-party instrumentations, and reference instrumentations in some kind of Gen AI.
And we would produce reports. I per… I don't care where these reports live. They should live somewhere in our help.
This place is not the right home for them eventually.
But we can produce reports, and we can upload them somewhere, or… We can.
keep them here for the time being, I don't know.
Trask Stalnaker 01:04:29 Yeah, I remember in the thought I had about, I was thinking a little bit last week after this discussion, and I think you had mentioned, which made sense to me, that this Because of my… my… Struggle was whether we wanted a… Repo that had, you know, a central repo that had them all, or we wanted to push them into the, instrumentation repos themselves.
And… The instrumentation repos… I mean, there's more… it's more like a code cover, like, it's… it's… the conformance tests are very basic.
And uniform, and… there is… Some niceness to having them all together.
At least for… A good while, until we really nail them down, and then maybe people could… Run them in a repo.
But there's something nice about having them all in the same repo, as far as being able to, keep them uniform.
Liudmila Molkova 01:05:45 Hmm, I see.
So, I think that this repo needs conformance tests inside them, because it's part of the testing coverage, right? This is conform to the SIMCOM compliance.
And it's very useful, actually. I found quite a few bugs with them.
Trask Stalnaker 01:06:05 Oh, nice.
Huxing Zhang 01:06:09 Yes, I agree with that. We actually have done a lot of tests based on the performance test. We're extending that… extending the one that Trask has done, and I think the… we should… put it into a CAD, like, CAICD pipelines, and to check against each, like, PRs, sending to this report.
I'm not sure this repo should go into this repo, or we have a centralized repo for all the Since I'm not quite sure about that.
Liudmila Molkova 01:06:47 It's already part of the CIA here.
So I think this is the tricky question. We have some form of conformance tests here.
And we have another form of conformance tests in Semconji.
Well, they're not conformance tests in some Gen AI, they are, like, the report generation for now, that can feed Trask's, dashboard, right, Trask?
This is the day dashboard.
Trask Stalnaker 01:07:17 the… I did… I split them at some point, so they're kind of separate code paths, it's… can… But, I mean, yes. The… the… I don't really care if they match the dashboard over there. What I care about in the GenAI Semcon repo is… to be able to pair PRs with real-world code, for review purposes.
like, that's kind of the only target that… I mean, if we can… if… we could expand it. I mean, we could… Yeah, we could… reuse… that, but at some point, I kind of tried to just narrow the purpose down for that repo.
To keep it simple, because that's all we needed at that time, but, I mean, it certainly, you know, there's a lot of options on the table. Moving that, you know, into this repo.
And having people send PRs here that they're, as prototypes for the GenAI Semantic conventions, PRs, is certainly an option.
Liudmila Molkova 01:08:54 Okay.
So, I don't know what would be the next steps. I think, what I'll try to do independently is… I want to have the… the… Story where we can… Let's say, have a folder Somewhere here in Semantic Conventions was for native instrumentations.
Because we want to test native instrumentations. Yesterday, somebody signed a PR for crew. It turns out they have native instrumentation, but that's Very… so far, and it's awesome to just see the report of how far it is.
So, I think… I'll try to make this happen.
I kinda… maybe we should do it in the SemComgen Gen AI, and then SemCom Gen.EI would be the place. But this, this, repo would provide The… It feels to do stuff. Like, to run this conferment suit.
And it… we would… the one thing I miss in the semantic conventions is validation.
So that it fails when you don't follow Semantic Conventions?
And, like.
Trask Stalnaker 01:10:30 Yeah.
Liudmila Molkova 01:10:31 review, and…
Trask Stalnaker 01:10:32 but it's also not part of CI… And I think that's… that's a downside to the separate repo Design is that it's run against releases, instead of against… main, or each PR.
There's also the… Multi-language aspect, where… I mean, it's nice… to… But not required to have them in the same repo, but different languages in the same repo makes it, again, kind of easier to ensure they're consistent.
Liudmila Molkova 01:11:22 Oh, we can start with Python, but we can easily extend it to be language agnostic if we're… like, the only piece of code we need to be able to be provided is this.
Which is fun.
the rest of the test is just the plumbing, and we can have a config that says, okay, I'm expecting this.
And… Then…
Trask Stalnaker 01:11:48 live in the Python Gen AI repo?
Liudmila Molkova 01:11:53 The tool that runs… can live anywhere, doesn't matter.
Trask Stalnaker 01:11:57 Oh, I see.
I see, you're calling… Right, and you can call something from Python…
Liudmila Molkova 01:12:06 Yeah, and it's Probably the right home for it would be SimConge AI.
Or even, I don't know, some kind of tooling, part of Weaver.
Bluetooth.
Trask Stalnaker 01:12:23 So if we had the harness in Semcon Gen AI, And then you could use… if we could use that harness for CI for these things.
And potentially, even if we could use that harness for… would we… okay, so all the Python, yeah, and so native… we would add native instrumentation tests here. We would basically add all those all the… those conformance tests over here for Python.
Liudmila Molkova 01:13:09 Y-y-yes.
the semantic conventions, I kinda like the reference instrumentations there.
And we would still run them against… Native instrumentation… oh, sorry, reference instrumentations.
Trask Stalnaker 01:13:30 Is that gonna be awkward to have the harness stuff in a different repo, especially when we're building out, maybe… I mean… If we just put it in here.
Liudmila Molkova 01:13:42 And if… yeah, and maybe initially, it's nice to have it next to the code you run, but, like, after… A month or two. Once it settles down, it can go anywhere.
Trask Stalnaker 01:14:01 And so, back to that blog post, will that… would that satisfy, sort of, the… Target here… pushing,
Huxing Zhang 01:14:19 Yeah, I think, we can adapt to you to the… what we're gonna post to, propose to do. I heard… what I heard is that we… like, to move the tools in a, like, under a repo of, like, SAMconf, and then we call that tool in different rep language implementations, is that correct?
Trask Stalnaker 01:14:45 I think what we're thinking for, initially at least, since we're just focusing on Python and… It looks like your screenshot here is all Python anyways.
That we would build everything out for now in the Python GenAI repo.
Huxing Zhang 01:15:06 Okay.
Trask Stalnaker 01:15:07 in… and we would test native instrumentations. Would we test other… instrumentations… third-party instrumentation is Liudmila, or…
Liudmila Molkova 01:15:22 We… we can?
The only concern I have is whether it's an ethical idea to report somebody else's instrumentation.
in Open Telemetry, but I kind of… kinda wanted to do this, right, because we wanted to show the… Compliance.
with Semantic conventions.
Yeah. So, yeah, I think so.
Trask Stalnaker 01:15:58 Okay, yeah, let me, yeah, I mean, there's still something to having… Especially for the testing of the third parties, And… well, you said for native… yeah, I guess native makes a lot of sense.
In the… along with the instrumentation, since we're… tying that… We're hopefully replacing that, or maybe building on top of that?
Trying to think, because that… those could live… outside… In a central… Place.
I mean, there's… We could do both, potentially, and in this, like, central repo.
Could be the testing, the version-based testing of the… Native instrumentation, the… Third-party instrumentations, and even alongside of our instrumentations.
Liudmila Molkova 01:17:08 I see.
Trask Stalnaker 01:17:09 of, like, a little bit more of a public-facing…
Liudmila Molkova 01:17:15 Right.
And it's cross-language.
Trask Stalnaker 01:17:18 Yeah.
Liudmila Molkova 01:17:19 Yeah.
Do we need a new repo for it right now, or should we just abuse Semantic Convention's Gen AI?
I prefer to abuse Semantic Conventions GenAI, just because there are so many repos these days.
Trask Stalnaker 01:17:42 Yeah, that's why I had built out also the HTTP compliance was to show that, like… because, yeah, I didn't want to create something only Gen AI, because then it would be… it should live in the Gen AI.
But the, I don't know if this links to the latest one.
Let me find… Semantic conventions, conformance… Oh, I'll put it in the chat here.
This is the… Latest one.
And so, like…
Liudmila Molkova 01:18:34 Nice.
Trask Stalnaker 01:18:35 It would be interesting to, you know, also have database, Instrumentation and conformance, and… And what I was… I was thinking, well, like, this would be nice to push into the repos, but also… It's very nice to have it all centralized from a… Not only from a reporting perspective, because we could pull data from individual repos, but just from… And I remember from talking with the Open Inference folks.
How much they were proponents of having multi-language repo, like, to be able to do Stuff across all the languages.
on…
Liudmila Molkova 01:19:26 Yeah, okay, so you're leaning towards a different repo.
Trask Stalnaker 01:19:31 Yeah, I'm kind of leaning towards this.
And… From a public-facing… perspective.
And so, then, I guess the question is… how… for… How to get… also, we want the benefits of… the, CI benefits.
a running… this, or running more detailed. Would you want to run more detailed tests in… Python, Gen AI… Or the same tests, just on main.
Liudmila Molkova 01:20:17 I think… Okay, two things. First.
I don't think it's more details.
You see, you probably want to cover… This French, too, right?
It's like… It's more like the full coverage and a happy pass, and maybe even sometimes unhappy past. It's…
Trask Stalnaker 01:20:41 more tough. Yes.
Liudmila Molkova 01:20:42 Yeah, but… yeah, so… but it's still probably a handful of tests per instrumentation, not like it replaces unit tests by any achievement.
Trask Stalnaker 01:20:51 Right, right.
Liudmila Molkova 01:20:53 Yeah.
And then, I'm thinking this way. So, imagine we run this, I think I lost the… okay, so we run this test.
This one, the only substantial piece. It produces a WIVER report.
So currently, my harness around it fails if there are violations.
But, it doesn't need to, so you can run this harness in two modes. The one is just capturing the report.
Another one with violations.
And even, in the capturing report state, it would be kinda nice to see violations here, somewhere.
So, like, yes, this attribute is emitted, but… or… There is also… a warning if something unknown is reported. You can ignore it in the report, but you have the information to put in.
Trask Stalnaker 01:21:55 Right, right.
Liudmila Molkova 01:21:56 And, like, overall beige compliant, not compliant.
Trask Stalnaker 01:22:01 Yeah, I see. So we could, in the conformance tests, we could spit out more data.
the dashboard, though, could… doesn't have to consume all of that data, necessarily.
Liudmila Molkova 01:22:13 Right, yeah.
But it would include more than just attributes and, you know, spend name, right? And it would be nice to see if it's… If we have means to validate it, we would show that, okay, this is the proper spend name we would expect.
Trask Stalnaker 01:22:31 Yeah.
I like that. I… I actually could… I couldn't put up a community issue today about… Creating that new repo.
I'm ready to move.
Liudmila Molkova 01:22:52 Nice.
Trask Stalnaker 01:22:53 With that, and get some… get the code up there, and then we can rearrange code, move code around different repos and stuff after that.
Liudmila Molkova 01:23:03 Nice, okay, I'm glad, then I can bug you about the reviews of my improvements to confirm and tests.
Huxing Zhang 01:23:10 Okay. Awesome. We will agree, we are glad to, like, to hear that, and I think this is a very important report to us, and we would like to contribute our, like, conformance reports into that.
Might as well.
Trask Stalnaker 01:23:26 Fantastic.
Huxing Zhang 01:23:27 Right.
Trask Stalnaker 01:23:28 Cool, yeah, so we'll target getting, by next Tuesday, getting that repo, set up, and have the initial codebase in there, and then, yeah, you come PR away.
Huxing Zhang 01:23:43 Okay.
Liudmila Molkova 01:23:46 Yeah, sorry we didn't get to anything else. Can we handle something offline?
Huxing Zhang 01:23:53 Yeah, it's not in no hurry. I can definitely discuss the rest of the topic next week, maybe.
Trask Stalnaker 01:24:02 Oh, Huxing, I see you're, yeah, I've been attending the AAIF, observability Working Group.
As sort of an open Telemetry representative.
So if you have any thoughts on that, just DM me on, Slack.
Huxing Zhang 01:24:21 Okay, I'm glad to hear that. Okay. I just, looked around in the AIF, so I saw this working group, and I was wondering if we could have any connection with that.
Yeah.
Trask Stalnaker 01:24:33 Yeah, yeah, I'm on it, and they've been… they actually reached out to us initially, and, the… I think we have a good… they're… Their goal is not to create a new specification, their goal is to, bring things to us at some point after they, you know, do all their white papers and that sort of thing.
Huxing Zhang 01:24:58 Yeah, that's one of my biggest concerns, so I'm glad to hear that they will not create a new open Telemetry.
Trask Stalnaker 01:25:06 Y-yot… So, hopefully, I'm there to keep them… keep them to that promise.
Huxing Zhang 01:25:13 Okay, I'm planning to join that working group.
Great. Because we just, like, have a collection with this, new, foundation.
Yeah, I can keep some eye on that working group as well.
Trask Stalnaker 01:25:31 Alright.
Liudmila Molkova 01:25:32 You gotta go.
Yeah, Steve, mind sending a PR for this? I think it's very straightforward and non-controversial. I would love to have it.
Steve Rao 01:25:41 Okay, thank you.
Liudmila Molkova 01:25:43 Yeah, thanks.
Trask Stalnaker 01:25:46 Rail.
Huxing Zhang 01:25:47 Okay, see you.
neil yashinsky 01:25:55 Alright, thanks.
