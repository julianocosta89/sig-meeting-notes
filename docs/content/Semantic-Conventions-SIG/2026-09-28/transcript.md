SIG: Semantic Conventions SIG
Date: 2026-09-28
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Michele Mancioppi (Dash0 Inc.) 00:01:15 Thank you, Christoph.
Christophe Kamphaus 00:01:18 Hello, Michel.
How are you doing?
Michele Mancioppi (Dash0 Inc.) 00:01:26 Oh, good.
I'm here.
Fits in demo apps and stuff, it's always fun.
What's going on in the, mainframe SIG? You're involved, right?
Christophe Kamphaus 00:01:41 No, I'm not involved.
I, I… I know that they have their own repo, but I haven't seen any act… I didn't watch it, so I don't know what's going on there.
Michele Mancioppi (Dash0 Inc.) 00:01:56 It was most out of curiosity.
Somehow in my head you were involved. Sorry for that slot.
Christophe Kamphaus 00:02:03 No problem.
Michele Mancioppi (Dash0 Inc.) 00:02:05 I slandered you.
Christophe Kamphaus 00:02:07 Yeah, I know, at work we still have a mainframe, so… Could be.
Michele Mancioppi (Dash0 Inc.) 00:02:12 So yeah, mainframe idea sent.
Christophe Kamphaus 00:02:15 Yeah, at our job, we are still trying to get rid of it.
Michele Mancioppi (Dash0 Inc.) 00:02:20 Those things are sticky.
Christophe Kamphaus 00:02:23 Yep.
Michele Mancioppi (Dash0 Inc.) 00:02:24 It's hard to get through those.
Daniel Dyla (Dynatrace) 00:02:37 This meeting get canceled or something, or just.
Christophe Kamphaus 00:02:40 No, I haven't seen that it would be.
Maybe there is a Us. Holidays that I missed.
Michele Mancioppi (Dash0 Inc.) 00:02:47 No, not again. Come on. It was already.
Daniel Dyla (Dynatrace) 00:02:49 Not right now.
This is the new Zoom link, right? I didn't accidentally join the old… aha, there we go, okay.
Christophe Kamphaus 00:02:59 It's the new one.
Trask Stalnaker (Microsoft Corporation) 00:03:21 Hey, folks.
Christophe Kamphaus 00:03:23 Hello?
Ashish Singh 00:03:28 Hey, everyone.
Trask Stalnaker (Microsoft Corporation) 00:03:45 Christoph, are you able to… Drive today.
Christophe Kamphaus 00:03:49 Yeah, I can drive it.
Trask Stalnaker (Microsoft Corporation) 00:03:52 Thank you. I just.
Woke up, and I'm not… Fully present, I'm afraid, not yet.
Christophe Kamphaus 00:04:01 You see my screen?
Trask Stalnaker (Microsoft Corporation) 00:04:03 Yeah.
Christophe Kamphaus 00:04:07 I don't know if Ludmilla will join, so I will… Leave.
A point in next.
Trask Stalnaker (Microsoft Corporation) 00:04:14 Yeah, I think she's out.
Today, still.
Christophe Kamphaus 00:04:20 So folks, please try to add your name here in the list.
And any agenda items you want to discuss?
But first, let's start with some triage.
And we have one PR that's ready to be merged.
I think it was just, If everyone agrees to it, because it touches pretty much every Every docs file… I can show what it looks like.
Basically, it adds here a link to The full list of enum values.
So we trust… links to each corresponding values list.
What do you think? Should we… Merchant.
Trask Stalnaker (Microsoft Corporation) 00:06:00 Got approvals.
Christophe Kamphaus 00:06:02 Yep.
Oh, just the link check.
Yeah, I think that's… that's resolved.
And we have a few.
To be reviewed… Yeah, that one we just took a look at.
This one has a lot of… approvals as well.
Oh, and it needs… Merge conflicts to be resolved.
Trask Stalnaker (Microsoft Corporation) 00:08:17 Possibly everything will with that last PR merge.
Christophe Kamphaus 00:08:21 Probably, yes.
Any other PRs we should take a look at?
I don't see any others that jump out to me.
Michele Mancioppi (Dash0 Inc.) 00:08:52 Trask, can you remind me what is the status of… So if you think that was something that I I had to To do for the.
POC for the, log, for the recording exceptions as logs.
Christophe Kamphaus 00:09:15 Do you have a link to it?
Michele Mancioppi (Dash0 Inc.) 00:09:17 Yeah, when you go back to the, to the list.
Yeah, it's that one. And there is a, linked POC.
For Java. Robert left some comments about a hypothetical Singh, when you do change.
Log levels to running applications, which… I don't believe we're doing in any… Any agent right now?
So I'm a bit lost in what is left to do.
Christophe Kamphaus 00:09:48 Sorry, can you help me? Which one?
Michele Mancioppi (Dash0 Inc.) 00:09:51 the, the POS, and let me pull up the browser.
Trask Stalnaker (Microsoft Corporation) 00:10:00 Here, I got it, I'll drop… or, well, here's the Java.
Michele Mancioppi (Dash0 Inc.) 00:10:06 Yeah, exactly.
Trask Stalnaker (Microsoft Corporation) 00:10:11 so, looks like Robert replied…
Michele Mancioppi (Dash0 Inc.) 00:10:39 I don't see anything that talks about this changing after startup.
Trask Stalnaker (Microsoft Corporation) 00:10:45 Did you see Robert's reply in the… Java Poc.
VR.
Michele Mancioppi (Dash0 Inc.) 00:10:51 Yeah, it says it's not a correct implementation, because the provider can be initialized with the instrumentation API logger being disabled. If it's disabled, it stays disabled.
Trask Stalnaker (Microsoft Corporation) 00:11:02 No, did you see his reply after that?
He gave some links to the spec.
Michele Mancioppi (Dash0 Inc.) 00:11:09 Yeah, but the spec doesn't align with what I know of the implementations.
That's why I labeled the concern as theoretical.
And I'm wondering if I'm missing something.
Trask Stalnaker (Microsoft Corporation) 00:11:23 I mean, Java does support… This… the Java SDK has an experimental feature to update them dynamically.
It's not… We don't… I mean, the goal is to be able to do that via OPAM.
on… It's not, you know, end-to-end implemented.
But I guess…
Michele Mancioppi (Dash0 Inc.) 00:11:52 Because when I look at your original code Trask This also doesn't get updated.
if somebody does some magic. I mean, the decision about whether exceptions need to be metered or panel event, it's a private static Arrival. That doesn't change.
Trask Stalnaker (Microsoft Corporation) 00:12:13 is Log Recognition.
What?
Let me look at the implementation, so… On… I think it's the calling is enabled.
That piece is what's new, so, from your PR. So, it's… It's okay that the flag… is static, right? That… there's nothing that can update that.
at runtime.
But… You're calling, like, on line 105, it's calling is enabled.
And I think that's.
probably what… Robert is referring.
2, although, let's see, should emit… Yeah, so that is all being… that's being called only at startup, the is enabled part. And so I think that's what Robert is talking about, is that is enabled.
If you're relying on that, that can be… changed later, but… Since you're only using it for… An exception, a startup… you're only using it to log at startup exception.
A warning, right?
Michele Mancioppi (Dash0 Inc.) 00:13:57 Yeah.
I mean, is log record emission enabled?
It tells you… it's usually a warning. Say, hey, if.
If you opt in, but it doesn't look enabled, then it'll tell you, hey, it's not enabled.
Which…
Trask Stalnaker (Microsoft Corporation) 00:14:18 Yeah, I would just… I mean, I think you just need to… follow up with Robert on that.
to… align… if there's… I mean, if it really… if there's a really a fundamental disagreement there, then, you know, I guess I would prefer not to break that. I would prefer to not, as a maintainer, not to not override Robert.
Michele Mancioppi (Dash0 Inc.) 00:14:44 Okay.
Trask Stalnaker (Microsoft Corporation) 00:14:44 I'd prefer for you all to… For you to convince him.
Michele Mancioppi (Dash0 Inc.) 00:14:53 Alright.
Fine.
Thanks.
Christophe Kamphaus 00:15:05 And, next topic on the agenda is this issue.
Is Ashish here?
Yep.
Ashish Singh 00:15:12 Yep.
Yeah, so basically… sorry, yeah, so this was the, basically, I think, Christophie has commented, so I agree with, basically, all the comments which he added. So I agreed with that, so, shall we go with the, attribute called the artifact loaded as the event?
And.
the attribute which we can expose as an artifact.purl.
If everyone is agreed, so I can read the PR.
Christophe Kamphaus 00:15:45 I didn't have the time yet to read your answer. I can do it after… This meeting.
Ashish Singh 00:15:52 Shit.
Christophe Kamphaus 00:15:56 So basically, my objection was that I didn't want, to send log records, duplicating the content of an SBOM at each startup of the application.
So that's why I only wanted… The real runtime information, which… Artifacts are really loaded because that's not something the S. Bomb would give you.
And for the rest, I wanted to have a resource attribute In the surface, which you can use to pivot to the Aspom information.
Ashish Singh 00:16:36 Yep.
So right now, this is basically all the, basically, part will be… all the attributes which you said, right, it will be the part of the resources, and now this artifact.purl, right, which we can, as a part of the logs. I think then, basically, there will be no kind of duplicate, things will be present.
Christophe Kamphaus 00:16:57 That sounds good to me.
An event like that.
And then, we need to see which attributes from Artifact it needs, and… Do we need to add some attributes to artifact namespace?
Ashish Singh 00:17:12 Yeah.
Christophe Kamphaus 00:17:13 I don't have it in my head right now.
Trask Stalnaker (Microsoft Corporation) 00:17:20 Ashish, have you seen the Java.
kind of, I guess you could call it a proof of concept for this.
Ashish Singh 00:17:29 Correct, yeah. Okay. So, with the Java, actually, it is, basically the package of stars is there, but those are basically not a kind of, very semantic. So, basically, it is a part of the local variable, everything.
Which I can see right now.
Christophe Kamphaus 00:17:47 So it would make sense if we add this event artifact loaded to SAMCONF, that we would also adapt OpenTelemetry Java instrumentation to emit that event instead.
Trask Stalnaker (Microsoft Corporation) 00:18:02 Yeah, and that is hidden behind an experimental flag in Java, so we… Can freely update it.
You might also, if you haven't already, CC Jack Berg.
Who implemented the original in Java.
Christophe Kamphaus 00:18:27 Doesn't look like it.
Is it him?
Trask Stalnaker (Microsoft Corporation) 00:18:35 Yeah.
Christophe Kamphaus 00:18:46 Yep, as I said.
Ashish Singh 00:18:47 So we will wait for the feedback.
Christophe Kamphaus 00:18:50 Yeah.
I will, take a look this evening.
Ashish Singh 00:18:55 Thank you.
Christophe Kamphaus 00:19:08 What? Okay.
Is Stephanie with us today?
Is anyone else aware what this is about?
Josh Suereth (Google LLC) 00:19:45 Oh, is this the OCSF stuff about…
Trask Stalnaker (Microsoft Corporation) 00:19:48 of a… yeah.
Josh Suereth (Google LLC) 00:19:49 Okay.
Christophe Kamphaus 00:19:58 I think let's, let's move it back to next, so if… Stephanie joins next time.
If you can't pick it.
Josh Suereth (Google LLC) 00:20:09 It says on it that she's joining at 11:30, so I'll just move it to the bottom of the…
Christophe Kamphaus 00:20:13 Oh, Central.
**Josh Suereth (Google LLC) 00:20:14** 11:30 EST, it said, which is in 10 minutes.
Christophe Kamphaus 00:20:19 That's fine.
Okay, are you here?
Aryan (New Relic) 00:20:25 Yeah, yeah, hi, everyone, I'm back again. Just a friendly reminder to, like, if somebody could, like, scrape out some time to review my POS.
Trask Stalnaker (Microsoft Corporation) 00:20:46 Yeah, still, same situation on the Java repo, we were just…
Aryan (New Relic) 00:20:53 Totally.
Trask Stalnaker (Microsoft Corporation) 00:20:53 Totally backlogged with the 3.0.
work.
Aryan (New Relic) 00:20:57 Yeah, yeah, just… Still, could be, yeah.
Trask Stalnaker (Microsoft Corporation) 00:21:00 Couple weeks, sorry.
Aryan (New Relic) 00:21:02 That's okay, that's okay. I'll just keep coming every week.
So it's not forgotten.
Trask Stalnaker (Microsoft Corporation) 00:21:09 Okay.
Aryan (New Relic) 00:21:11 Yeah.
Christophe Kamphaus 00:21:20 Any other topics?
Yeah, maybe from my side in Semantic Conventions Conformance.
I think there's a few PRs there we can take a look at.
So, I did prepare one… To auto-fix the log file regeneration.
Yeah, I… I used… Which language?
Trask Stalnaker (Microsoft Corporation) 00:22:12 Which is…
Christophe Kamphaus 00:22:13 Awesome.
Trask Stalnaker (Microsoft Corporation) 00:22:13 All of them, okay.
Nice.
Christophe Kamphaus 00:22:21 Yeah, it follows the same principle.
that you put in yours for the data Json file.
Yeah. And it adds commands to relock.
And it is scoped to just the scenario log files, because those are the only ones which have file local dependencies.
Trask Stalnaker (Microsoft Corporation) 00:23:04 Cool, I will… I will scan that today, and leave an approval on it.
And I think the… Only way we're… Gonna know is merging that and giving it a run.
Christophe Kamphaus 00:23:18 I also created a second one that fails if PHP has stay logs because It turns out that Composer doesn't have a strict mode.
If you could take a look at that one as well, that would be great.
Trask Stalnaker (Microsoft Corporation) 00:23:41 Yeah, let me get that.
PHP… Yes, I see it, okay, yeah.
Christophe Kamphaus 00:23:57 Yeah, I tested it because I noticed from a previous PR set The dependencies were old and were stale, and so I just… first, verified that my script worked, and then I fixed it.
By updating the… dependency.
Trask Stalnaker (Microsoft Corporation) 00:24:16 Cool.
Yeah, it's wild having so many languages in one repo.
Christophe Kamphaus 00:24:23 Yeah.
Yeah, this one also, it has a matrix drop in the runner, so it only updates the Log files where something changed.
So it doesn't run the update for all languages all the time.
Trask Stalnaker (Microsoft Corporation) 00:24:45 Oh, okay.
Christophe Kamphaus 00:24:49 And only for… it only runs the… log file update or run of APRs.
Trask Stalnaker (Microsoft Corporation) 00:24:57 Yeah.
Christophe Kamphaus 00:25:05 Other than those, are there any other PRs here? I know there's still… A lot of instrumentation to be added.
Josh Suereth (Google LLC) 00:25:16 Can I ask a question about that Renovate one? Is that one automatically… is that submitting a PR to be merged, or is that one automatically merging Renovate PRs?
Christophe Kamphaus 00:25:26 No, it's not auto-merging some.
Josh Suereth (Google LLC) 00:25:29 good.
Christophe Kamphaus 00:25:29 Renovate creates PRs automatically according to its config.
Yeah. And then, depending on if the build fails, which can happen because data JSON is out of date. If the semantic conventions change, or if the instrumentation emits other signals.
Or, if the log files are stale, the build would also fail now.
So.
Trask Stalnaker (Microsoft Corporation) 00:25:55 And it pushes… oh, sorry.
Christophe Kamphaus 00:25:58 Yeah, so, we detect these conditions in the runner.
And triggers the autofix workflow automatically.
And it only triggers, it only runs if it's triggered from a random fate, Drop.
Josh Suereth (Google LLC) 00:26:19 And then, and then this is still a PR that we manually approve and everything. I just want to make sure.
Christophe Kamphaus 00:26:23 Yes.
Josh Suereth (Google LLC) 00:26:23 Like, we cannot remove manual approval process at all. That is not a thing that we can do. So I just want to make sure that we're not trying to do… this actually sounds awesome. How reusable is it if we wanted to do something similar in other repos?
Christophe Kamphaus 00:26:39 Oh.
I think Trask, it's already used in other repos.
Trask Stalnaker (Microsoft Corporation) 00:26:47 You mean the… the auto, yeah,
Josh Suereth (Google LLC) 00:26:53 Yeah.
Trask Stalnaker (Microsoft Corporation) 00:26:54 Yeah, we… so, with Renovate PRs, so it's safe to do on, PRs which are on branches… upstream branches.
Because we can push directly to those, and those already have, basically, access to secrets. We don't have to worry about, like, the whole.
Security aspect.
auto fixing… contributor PRs is a whole other ball of wax. I can… we have a community issue that's stuck on that.
Christophe Kamphaus 00:27:30 Yeah, just to give you some idea, we have a lot of validations here.
Same here. We validate that the patches are safe to apply.
I also added some additional checks here, so it only… only applies modifications. I think here we can even make it stricter for the data JSON to also only allow modifications.
And only then do we create a token to push the commit.
Trask Stalnaker (Microsoft Corporation) 00:28:06 Steve Cook, Even that is, I think, not totally required, given that, I mean, I support the extra layers, but… Steve Cook, Since it's a trusted branch already, from Renovate.
I think it's… not entirely required.
Christophe Kamphaus 00:28:32 No.
Stephanie joined in the meantime?
Yeah, otherwise we can still talk about the conformance PRs.
What is the idea to progress on these?
Trask Stalnaker (Microsoft Corporation) 00:29:09 When I am done with the Java 3.0 work.
I'll get back to it.
Unless somebody… unless you want to… Start pushing them, in which case, more than welcome to, just… push fresh PRs and close.
close out.
Mine.
Christophe Kamphaus 00:29:32 I can take a look.
Trask Stalnaker (Microsoft Corporation) 00:29:35 Cool.
Yeah, or you can push to the branch. I think they're probably all… they should all just be upstream branches.
Christophe Kamphaus 00:29:47 Yes, I think you created some… Yep.
They are in this repo, so yes, I can push on some.
Yeah, and the Docs PR was merged recently.
So, people here in this meeting We haven't seen it yet.
We have now this beautiful dashboard, where we can see per signal.
What is currently being checked?
And if you want to give some feedback on it, you are more than welcome.
Josh Suereth (Google LLC) 00:30:51 This is awesome, guys.
Michele Mancioppi (Dash0 Inc.) 00:30:54 It's seriously awesome.
Josh Suereth (Google LLC) 00:30:56 I think I've only approved two CLs in that new repo, so I feel like I haven't… Done anything at all, and this is amazing, so thank you.
Christophe Kamphaus 00:31:07 Thank you.
Trask Stalnaker (Microsoft Corporation) 00:31:15 Yeah, now that we have this, yeah, that would be great to… build out more instrumentations. Definitely feel free to do whatever you want there, Christophe, with the… My PRs are taking that work forward.
Josh Suereth (Google LLC) 00:31:30 You think we'll have a competition for which language gets the biggest?
Bart.
Trask Stalnaker (Microsoft Corporation) 00:31:37 Is it a… is it… are you winning if you… Or losing if you have more.
Josh Suereth (Google LLC) 00:31:43 customer.
Trask Stalnaker (Microsoft Corporation) 00:31:43 Foundations to maintain.
Michele Mancioppi (Dash0 Inc.) 00:31:45 So, you are losing depending on how many of your HTTP instrumentations do not set HTTP.route. That, definitely.
I cannot tell you, like, the amount of pain that that thing not being consistently used can cause, in reality.
But the cardinality of metrics is, like.
Josh Suereth (Google LLC) 00:32:08 I believe it. I also think it's really painful to get HTTP that route depending on where you instrument.
Michele Mancioppi (Dash0 Inc.) 00:32:14 Absolutely, absolutely. That's why, for example, we are, we automatically calculate them now on behalf of customers because Sometimes they even set them.
Wrong.
It's, it's mind-blasting.
Christophe Kamphaus 00:32:32 I think in the hotel collector, there's even examples how you can rewrite the HTTP route.
Michele Mancioppi (Dash0 Inc.) 00:32:41 Yeah.
And the next one is URL.template.
And then there is the DB query text.
And I don't think we ever put a DBQuery template in there.
It's just fun.
Josh Suereth (Google LLC) 00:32:55 So, I'm gonna ask the question that is, like, the classic launch question.
Why are there no reds?
Shouldn't we have something that fails? Or is it just we're only adding things that will pass because no one's going to bother to write that they don't pass?
Trask Stalnaker (Microsoft Corporation) 00:33:13 like.
Josh Suereth (Google LLC) 00:33:14 Yes.
Christophe Kamphaus 00:33:15 I guess if it's required and it's blank, then it could be red.
Josh Suereth (Google LLC) 00:33:20 Oh, okay, okay, gotcha. So if it's required and it's blank, then that's basically a red. Okay.
Cool.
We should, I mean…
Christophe Kamphaus 00:33:29 a.
Josh Suereth (Google LLC) 00:33:29 I was expecting to see red, green, and yellow. Like, that's what stoplights have taught me, you know, traffic lights.
Christophe Kamphaus 00:33:38 Maybe we should make it red.
Michele Mancioppi (Dash0 Inc.) 00:33:41 Josh, I have an entire rant waiting for you at KubeCon about the misuse of green in that situation.
Josh Suereth (Google LLC) 00:33:48 We should make sure that if you choose a red.
that it is visually distinctive from green for colorblind people, because having red and green both be… Like, the same hue is very problematic.
Michele Mancioppi (Dash0 Inc.) 00:34:03 Copy, copy the hue from their steroid. There is, the green is a kind of mint green. Which then, with most.
But most, color, the vision deficiencies still reads different.
It's a small problem.
But this green here, when you put up bright green.
That… they're the same picture.
Josh Suereth (Google LLC) 00:34:28 That's why the traffic light has 3 in an order, and the only thing that matters is the order of the light, not the color, but…
Christophe Kamphaus 00:34:35 and.
Josh Suereth (Google LLC) 00:34:36 Yeah.
Christophe Kamphaus 00:34:37 More often you put a different symbol. So if you put, if we put here an X.
Make that red, that will also work.
Josh Suereth (Google LLC) 00:34:45 Yeah, like make all the greens check marks because that makes you feel better if you're a list checker person, you know?
Michele Mancioppi (Dash0 Inc.) 00:34:52 Yes.
Josh Suereth (Google LLC) 00:34:56 Still, this is like so much coverage already.
And is this right now just showing HTTP or is this like everything that we have in the repo?
Christophe Kamphaus 00:35:09 We can choose here the signal. So here we have Gen AI.
And we have a few databases.
Josh Suereth (Google LLC) 00:35:17 Okay.
And then, next question… What's the plan for getting this on Open Telemetry IO?
Christophe Kamphaus 00:35:32 I think there were discussions to include it in the Ecosystem Explorer.
Trask Stalnaker (Microsoft Corporation) 00:35:41 That's, a good question for Jay.
I think he's been… Thinking and working with, Docs, folks, also.
Christophe Kamphaus 00:35:55 And one of the difficulties could also be.
the data file. I think that one will keep growing.
And currently, I don't know how big it is at the moment.
Okay.
Already one and a half megabytes.
So basically, here we accumulate all the individual Data files from the different signals.
And put everything in one file.
Josh Suereth (Google LLC) 00:36:35 God help us if we need a database.
Oh, Yeah, and the other thing I remember, because I reviewed the… this is the one PR I did review, we're still pushing to, like, a branch for GitHub pages, as opposed to using, like, the package publishing technique.
I do wonder if, Well, anyway, I can take this offline, but us, like, bundling up that data and the website is like a, a zip that we can push somewhere that then is hosted, or where you can take that JSON and shove it into a database if we end up using that for OpenTelemetry.io, if we ever get large enough that we have to, like.
not pull in everything all at once in one big file and make the browser do all the work. I don't know if that's, like, a thing we've thought about, but if you're worried about it getting larger and larger and larger.
I don't know what your size limit is, but we should probably have that tracked.
Christophe Kamphaus 00:37:35 I think it was just a discussion for now on the PR.
And we do not have an issue for it.
I can take a look later.
Josh Suereth (Google LLC) 00:38:12 I think Stephanie's here if we want to talk about OCSF.
Stephanie B 00:38:26 Hi, everyone, can you hear me?
Christophe Kamphaus 00:38:28 Yep.
Hello?
Stephanie B 00:38:30 Let me… Hi!
I'll turn on my… video.
Okay.
Christophe Kamphaus 00:38:40 If you want, you can also take over screen sharing.
Stephanie B 00:38:44 Okay.
Alright, so give me a moment here… Were most of you at the meeting that I was at.
Who was it?
Trask Stalnaker (Microsoft Corporation) 00:39:00 Last, Tuesday?
Stephanie B 00:39:01 Last Tuesday? Yeah.
Trask Stalnaker (Microsoft Corporation) 00:39:06 Some of us, at least.
Stephanie B 00:39:28 All right, can you see my screen?
Christophe Kamphaus 00:39:32 Yes?
Stephanie B 00:39:34 Yeah, so I won't go, like, all into the, specific details of the document. I believe everyone has a, link to the.
To the document that I was, That went over during the Tuesday sync, but basically, This was… I kind of… I went over… a… trying to… a proposal for OCSF OTEL, for OTEL extension within the OCSF framework to introduce, categories and classifications in regards to, OTEL data.
And so the document that I have is a link into… I put a link to it in the, agenda as well for those that weren't able to, make the last one, but… It's just a proposed idea that we want to implement, but one of the main things is we wanted to get feedback from the OTEL community, so… which is the reason why I joined.
last week's sync… well, two weeks ago, the sync on Tuesday, and then it was recommended to bring it to, this group here. And one of the questions that came out of the, sync last… the other week was.
What was the difference between having the OTSF Operational extension versus the.
versus the Semantic Conventions. So, I just… I just put together a couple slides just to kind of, just answer that question for this, group in regards to that. So.
So that's what I'm sharing here. I wonder if I can… let me… Do, like, slideshow… All right.
So, so this is just kind of just to answer that question that was presented, like, what's the difference? Why?
we're proposing a OCSF extension. So, with the OTEL, basically, you know, we have what fields actually exist, and then with OCSF extension, we're more referring to what type of operational event it is.
So, I put in a… two examples. So, like, for, you know, your user login event data with OTEL, you have all the different fields and the values there, but the OCS, extension would add, like, a cloud of category. So this category actually already exists, in OCSF, identity and authentication in the class, and then actual logon activity. So, with the OCSF extension, we would be just adding these actual.
Categories and classes on top of that.
on top of that particular log. And here's another one I just pulled.
Partial log for some of the data that we get.
And then, you can see here the OTEL, you know, you would have the, OTEL attributes there, and then on the, with the OTEL, with the OTEL OCS extension.
We would… a new category would be, like, a configuration, and then a new class would be infrastructure resource activity, and then, you know, and then it's just adding that overlay on top of.
On top of the already hotel, normalization that happens.
So, as I was saying, it doesn't replace the semantic conventions, but it adds, like, the category, class, activity, and type classifications that exist in OCSF for all the log activity data.
And then, the question would be, you know, with OTEL, we know who, what, where, but the extension would add, like, what kind of operational event is it? Is it a storage type event, authentication event? What type of event is it? And then kind of align it there to help, at a higher level, group the activity.
Josh, I think your hand is raised.
Josh Suereth (Google LLC) 00:43:58 Yeah, so, thanks, this helps clarify a lot. Quick question, so, when you're, like.
I think you answered this, but I have two questions. First would be, are you adding this information into the signal itself? Like, you're trying to actually… you know, are you trying to actually send the data with that, classification inside of it, or is this something that you just want in the semantic model that people understand what this means? That's question one, and then question two is based on what you answer for one.
Stephanie B 00:44:29 Okay, so, To answer question one.
So, this would be… This would be to add into that data. I guess it depends on, like, for our particular use case, we have all of our data going into one, scene database.
And, so we… we would… whatever your tooling is for our particular tooling, we would add the classification on top of that data that already exists there. So on top of the OTEL fields, and we add the classification category and all that, and all of that.
whatever tooling you use would, you know, send it to. For us, it'll be our scene where we would query that data.
Josh Suereth (Google LLC) 00:45:15 Okay, can you go back to this?
Yeah, yeah, can you go back to the slide, then, that shows the semantic convention? Because I think this is an area of clarification, that if you go back… yeah, one more, actually. So this one here.
The event name is user.login, right? And we have this idea in Semantic Conventions that all of these actions and signals have a, unique identity, which, in this case, event name is one of those things that identifies it.
And so, theoretically, that is supposed to serve the same purpose that you have, you're just adding more, better data to it. So I think this is really highly aligned with what you want to do. What I'm curious about, like, so from my perspective as, like, a SemCom person, event.name equal user login.
you should be able to infer 100% from that that the activities log in, classes authentication, category might not be… like, I don't know if you have other authentication, or if IM is the only thing there, but sure, IM, and that makes sense to me, but on the wire.
We're going through this, like.
kind of design cricy, if you will, with OTLP, where some people want to throw all the data on the wire, and then we end up with inefficient formats and transports, and then some of this might be sent kind of on the side.
Right? Where, like, you… if you know OTEL Semantic Conventions, you know event name user login is this activity in this class, and someone can easily annotate that data on a side channel later, if they need it, versus having to send it in every single payload, right? Yeah.
Yeah, so if the proposal is in OTEL, for every single, like, telemetry type. like event name, or for spans, we have, you know, a span that represents a call to, an LLM, right? Or we have the invoke agent Gen AI, you know, span.
If this is for every single one of those, we add a category class and name the activity, which the activity, I think, is what we would call the span name or the event name now.
this sounds awesome, like, this would be great. We can actually find a way to, in our SemConf, put those categories and classes. What I'm trying to tease out, though, is whether or not you would want this in the data we send, or if this is just, like, a layer of semantic meaning that you can consume from us. So you could take the model you have here.
provide that into OTEL, and say, hey, for Semantic Conventions, this particular span is this category class activity. This particular log is this category class activity, for all the things we've defined. I think there's huge alignment there, because we actually already wanted this level of understanding in SemConv.
We didn't make our model as rich as yours is, and so I think tying the two together would really make sense.
But if you just want it as a layer that you can read back from our data model, or if you want it in the data that's sent, transmitted over the wire, that's the thing I want to tease out.
Of, like, where would that boundary be? Because it would depend how we integrate what we do.
Stephanie B 00:48:29 Right.
So.
I'm just digesting what you said. So… It doesn't have to be in the wire, so when we talk about extensions, right, extensions are, you know, within OCSF, it's optional. So it doesn't have to be, you know, if an end user customer doesn't want to use it, then they don't have to. But.
from what you were just explaining, right before, as something that you can consume, like, afterward, I believe that could be fine. So that's… this is what I want as far as, like, open discussion and communication. We.
We hadn't thought about it as high as in detail as that, but if that makes sense and better to be able to get that extra layer of detail there, then, you know, we would be for it.
Josh Suereth (Google LLC) 00:49:20 Okay. One thing I'll say that, like, in terms of the framing of the document, though, in OTEL, that semantic meaning and that layer that we have, we have that in our data model that you can start to leverage. What we don't have is we don't have class and category.
we have this notion of namespace, and we have these notions of signals, like actions that are taken, so we have spans, we have metrics, we have events. They're all named. All those names have a meaning behind them that is written in just big old text strings.
That is not… it's not just the attributes, it's actually the event has a, like, name and description.
So, we can show you that if you want to see that in our docs, but that exists, and you could layer this information right on top of it.
Because it's intended to be the same.
Stephanie B 00:50:08 All right.
Josh Suereth (Google LLC) 00:50:08 Yeah, so I think we have very similar goals here, just you're far more along with this category class activity than we are.
Stephanie B 00:50:16 And what we were doing even so, with the O… when I say the OCSF extension classification. The proposal is just to have it within already the OCSF, our data model, and then those OTEL events, we can layer that. So, like I said, this is a proposal. In the document, I talk about all the different.
well, it may be more categories, but just at a high level, what the different categories may be as it relates to OTEL, data, and then implementing an extension within the OCSF framework, where you know, it can be added as needed. In OCSF, they do have extensions, like Windows extension, Linux extension, different things like that, where, you know, it's a part of the OCSF, but it's an extension. You can enable it if you want it there. And then.
on… on the back end, the legwork would be, as I stated in the document, it's just, like.
classifying, like, all the different types of data. So.
from my perspective, it'd probably be, you know, based off of the logs that we have, and then seeing, that's how we got the categories there from what we, have, seen so far. It's like, config, you know, updates to, configuration, and.
compute different things like that that we go in more detail with what those classifications may be.
Josh Suereth (Google LLC) 00:51:45 I want to hear from the other SemComp maintainers, but, like, the straw man that I see here is, you know, in OTEL.
Stephanie B 00:51:51 Go tell them.
Josh Suereth (Google LLC) 00:51:53 You it's not just the user login event, it's not just raw attributes. And I think that's the thing I really wanna harp on is, like, in your your framing, you say in Semantic Convention, it's raw attributes. That's not true. In Semantic Conventions, it's actually signals, it's events, it's spans, it's metrics. And those have those have a grouping. Right?
The, and so I think as a straw man, we could.
Today.
have annotations for OCSF that would say, for each of these, here's the OCSF category, class, and activity for that thing. In… inside of our repo.
So, like, you could… you could just come into OTEL and say, here's the, you know, OCSF things we need, and then if you need to do code gen, if you need to, like, have these, documents spread somewhere.
the source of truth for how to map OTEL into OCSF would live right with OTEL, and if you agree that, like, OTEL is the one producing the operational data that you leverage, like observability, AI, that sort of thing, it might make sense there, since we have this whole conformance plan and program and all this instrumentation around OpenTelemetry for the conversion to live there. So, like, you would own telling us, like, hey, here's the categories and classes and extensions we have, and there'd be a place in our data model where you can just write these.
And then the mapping happens automatically. And we can even have, like, checks that would say, hey, did someone add a new signal that doesn't have OCSF bindings, and if they don't, we can actually, like, open an issue, ask you guys, hey, do you want to take a look at this one, tell us where it fits, that sort of thing. I think there's a lot of opportunity here.
But I want to, like, you know, take it a little further from what you're saying and kind of frame it, this, like, signal-to-signal correlation. I'll give it to the other maintainers to talk about what they think.
Christophe Kamphaus 00:53:44 Yeah, I also asked myself the question, where does this integration live?
as it sounded here, what you described, it's more on Ocsf side, where you say in your own data model.
how OTLP maps to the OCSF model.
And what Josh was describing was more, how can we put this mapping data on our site, and how could it be transmitted over OTLP, so you could read it and directly map it.
Stephanie B 00:54:20 Yeah, so those, yeah, they're…
Christophe Kamphaus 00:54:22 So where this integration lives, we can discuss it.
Stephanie B 00:54:27 Yeah, I think just based off of just what I know now, like I said.
Initial, the initial concept, as we determine what the categories, and as we determine where things fit, it would be in the.
in the OCSF space, but then If I'm understanding correctly from what Josh just said.
Once we know what those categories are and what those pieces are, then we can add it.
into the OTEL piece where it automatically is integrated. Is that… am I understanding that correctly, Josh?
Josh Suereth (Google LLC) 00:55:02 Kind of, let me… let me rephrase a little bit, or actually, can you… the, the, the, IT Ops Unified Telemetry Schema PDF, I have version 1.2 open. I don't know if you have a more recent one.
Stephanie B 00:55:17 Yeah, no, that's the one I haven't updated since then, no.
You want me to, share that, or you want to share?
I can share it. Let's see if I have it up here.
Trask Stalnaker (Microsoft Corporation) 00:55:33 Josh's video, at least, has frozen.
Christophe Kamphaus 00:55:45 Yes, Josh, you raised your hand.
We cannot hear you, Josh.
Josh Suereth (Google LLC) 00:56:20 Apologies, my internet decided to crash right at that moment.
Yeah, so in your proposal, if you can scroll down to some of your categories, I have a question.
So, like, here you have, like, compute, network performance, storage, application configuration. I think this is where things get really interesting between the two.
And this is what I was looking at, of like.
Inside of Semantic Conventions we have this notion of like sub-Semantic Conventions and namespacing and that is really equivalent to what you have here. And we spin up groups, and this is probably similar to what you do, but we spin up a group that is like our Systems SemConf. They own host metrics, process metrics. I don't think they own container. I think actually the Kubernetes folks take that on our side.
But there's still a group that owns container metrics. VM life cycles might be part of host metrics, right?
we have these sets of experts that are meant to be figuring out these signals on our side as well as on your side. What I'd love is if we can get to a point where, instead of you defining your own set of categories, and us defining our own set of categories, what if we just frickin' share, right? So, where we already have something, right?
Come to our SemConf SIGs and discuss it there, the things that you need. And then, if we have a way to easily transmit the data both places, when it's an operational signal, like compute and host metrics, you can come right into SemConf, you can put all the things you need for OCSF bindings right into our data model.
Like, and I, again, I think we can do this today with very little effort. In terms.
Stephanie B 00:57:49 And then we're at… Would it add, like, the classifications? It would automatically add those classifications and categories?
Josh Suereth (Google LLC) 00:57:57 Yes, I can give you a straw man for what that would look like. Okay. Actually, like, I can even put together a PR that might do, maybe I'll take one of these, like, storage or computer something, whatever you think is important there. But the difference would be, like, in terms of the categories and the descriptions.
That's where we… I think we should have a bit of a discussion. We have this notion of ownership. So, what we do in SemConf is a category is owned by a group of people.
And they have freedom to define the areas of convention in there. And what I'd love is if we kind of get an agreement where the group of people who own host metrics, if OCSF needs to define things, joins into that group and becomes one of those experts, and then we share that definition between both.
And we make sure that everything you need is represented in both places, right? And we make it very seamless to do this transition. To me, that's like our… that would be our ideal, right? And if we can make that happen, that'd be awesome.
So that's that's I want to like take what you have here and say, what if we were to look at open telemetry and open telemetry, there's a group of people that are adding networking.
performance right now.
They are actually spinning up their own Semantic Convention registry and adding stuff around everything you list there, right? And we call it our networking SIG. It'd be awesome if that work was kind of, like, shared.
And that if we could agree that the way that we make decisions around when there's a new category.
what the scope of that category is, if we can agree to the two, I think we can avoid having divergence, then, between OCSF and OTEL going forward. So I'm being a little bit more aggressive than your proposal, because I'm looking at this, and this just… it all feels a lot like what we do today.
And I feel like there's a really good opportunity for us to work together and to put a real seamless, you know, hook between the two if you're if you're amenable.
Stephanie B 00:59:47 Okay, okay, no, no, that, that sounds, that sounds good.
I do have a question. Is this call… is it recorded as well, that I can go back?
And, yes.
It is.
Trask Stalnaker (Microsoft Corporation) 01:00:01 Yes, it is.
Stephanie B 01:00:02 Okay, alright, alright.
Christophe Kamphaus 01:00:04 I think it's…
Josh Suereth (Google LLC) 01:00:05 Now Trask.
They moved, and I don't know where they are.
Trask Stalnaker (Microsoft Corporation) 01:00:08 Yeah, they're hard to find now. They're in the calendar, the LFX calendar.
I think we… let me see, I think we updated the community repo to explain this, but, I will post in the OTEL Semantic Conventions Channel. Thank you.
Christophe Kamphaus 01:00:30 I posted it in the chat.
Stephanie B 01:00:34 You posted it in the chat, okay.
Armin (Dynatrace) 01:00:41 You might need to log in, but I think any GitHub account should work for that.
Stephanie B 01:00:46 Alright.
Christophe Kamphaus 01:00:47 Only it's a Linux Foundation account.
Armin (Dynatrace) 01:00:51 Alright.
Trask Stalnaker (Microsoft Corporation) 01:01:02 Oh, we hit time here. Yeah, we're good.
Stephanie B 01:01:05 Past the time, yeah.
Trask Stalnaker (Microsoft Corporation) 01:01:06 I mean… Quick, last… Anything?
Christophe Kamphaus 01:01:13 Thank you, everyone.
See you next time!
Trask Stalnaker (Microsoft Corporation) 01:01:18 Look forward to hearing more, Stephanie.
Stephanie B 01:01:21 All right. Thank you so much.
Christophe Kamphaus 01:01:23 Bye.
Stephanie B 01:01:24 time today. Thank you.
