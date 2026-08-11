SIG: C/C++ SIG
Date: 2026-08-10
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Marc Alff [MySQL]** 00:44 Hi, Doug.
**Douglas Barker** 00:47 Hey, Mark.
**Marc Alff [MySQL]** 00:50 You can tell I'm back from vacation. This is the first time I see this new Zoom thing.
**Douglas Barker** 00:57 Yeah, I popped in the other meeting just to make sure everybody had got the new links, so I'm glad to see you here.
**Marc Alff [MySQL]** 01:04 Okay.
So, who have you been?
**Douglas Barker** 01:11 Oh, pretty good, pretty good. It's getting hot here in Boston.
**Marc Alff [MySQL]** 01:14 Yeah, well, it's the same in Europe as well, so… I saw that you have been, pretty active with the YAML configuration.
Looks like you like this part.
**Douglas Barker** 01:31 Yeah, yeah, I'm excited to, to get it going. I think, My, you know, my idea, I think we talked about it before, is, like, driving everything through configuration. It really helps us figure out where the missing features are.
**Marc Alff [MySQL]** 01:44 Oh, yeah.
**Douglas Barker** 01:46 It's really, really helpful to get everything working through that interface.
**Marc Alff [MySQL]** 01:52 And thanks for the validation tool that you just checked in. I mean, the… Validating the schema was a missing part, and it just caught so many things that were not in sync, so it's a good thing.
**Douglas Barker** 02:08 Yeah, and it's nice to be running the… I didn't, know how that example worked before I was testing it all wrong, so I wasn't passing in the file, so I think it was just running all the time, never… never doing anything, but now it's actually, being used correctly, so we're running that kitchen sink, YAML file on every test, which is really nice.
**Marc Alff [MySQL]** 02:31 Yeah, the kitchen sink is a very old file that existed in the config repo ages ago.
But it has been replaced with smaller examples, with, we call that snippets, with, Focused example on small areas.
That's okay.
I'm not surprised that the kitchen sink was way out of date.
**Douglas Barker** 02:52 Interesting.
**Marc Alff [MySQL]** 03:01 I saw from the previous meetings that Tom was around. Do you know if he's joining today?
**Douglas Barker** 03:09 I don't.
Nobody, joined in the last meeting, so I canceled, but hopefully, we'll just get some others to join this time.
Okay. I've carried over a few topics to discuss with CE. I don't know if you added any.
**Marc Alff [MySQL]** 03:24 Yeah, I saw that. I also added a few, in the… what is it?
Or in the Google Doc for the different notes.
**Douglas Barker** 03:34 Yep.
**Marc Alff [MySQL]** 03:34 So… All your lists… I'm assuming you wrote it, so all your lists make sense. The only thing I added is, upstream changes were lacking behind, So we need to upgrade also on a couple of things.
**Douglas Barker** 03:50 Perfect.
**Marc Alff [MySQL]** 03:55 Just so… I don't know, it is for you, but every time I connect and see the list of PRs, there is 5 more compared to the previous day. I'm trying to get rid of the easy, low-hanging fruits, like… renovate or, depend about, upgrading your dependency, things like that, so get… to get that out of the way. And then there are some easy PRs, To address test case or whatever that can be, addressed right away.
And I'm always finding myself doing the little things, and constantly ignoring the bigger PR, which I've been there for a longer time.
So, not sure how to deal with that. What's your experience with, Dealing with reviews and the merge queue.
**Douglas Barker** 04:56 Yeah, I… I also share that. I think probably we go back and just look at, like, which PRs are hanging out there. I went over the weekend and tried to at least mark the ones that had conflicts that hopefully can be resolved. I have…
**Marc Alff [MySQL]** 05:13 Yeah.
**Douglas Barker** 05:14 I have some thoughts on which ones I think we should get, like, I think we should clear out Owens, get that merged in soon, because that's just a difficult one to maintain, because it touches so many files with the CMake change.
**Marc Alff [MySQL]** 05:24 Oh, yeah, I agree.
**Douglas Barker** 05:26 So… those… those I'd like to… to get merged, and then, there's a few ones, like, with the exemplars, I think we can probably just merge some of these. I think we… Some of the times we need more feedback, but it's… some of these have been out there for over a month, you know?
**Marc Alff [MySQL]** 05:46 Yes. So, I've seen… I've seen some PRs, up for a very long time, and… what I'm seeing is that every time there is, it's not a… it's not a black or white situation, like, oh, the PR is all good and we should just merge it. It's like, yeah, what about this case? I think this needs some minor changes and things like that, and… There is always a reason to not merge something, and it's, it's… Which is okay, it's part of a review, but my concern is that I don't see that being cleared up. I mean, if there is a change to do, okay, let's do that, or let's ask some precision, but then the state of APR seems to be that nothing is done.
**Douglas Barker** 06:36 Yeah, typically how I… I think about it, especially when it's… because, like, the hard one to… to really gauge is, like, when the concern is about performance.
Yes. And I think, like, my answer to that is, like, well, let's just do a benchmark then. So I've been trying to add benchmarks, and Post something there to at least answer those questions.
Are there other cases? You know, I guess the other case would be if there's an ABI break or some kind of interface change that we're concerned about, but those are usually a little bit more straightforward, I think.
**Marc Alff [MySQL]** 07:10 So, there is… for example, just looking at all PRs, there is a PR viewers to simplify the trace context, I think.
For performance improvements, and it all looks good, and then Tom had a question and a concern on that, like, okay, what about this case where, We are no longer, We can raise the exception, even though we claim we are no exception, things like that.
And… On that comment, It's… even it's unclear to me if it was just, like, a comment from him, like, yeah, we should eventually do that, and look at it, or if it's like, no, we should not merge that PR because it's a breaking change, I mean… even the… The intent of a review is not clear to me, whether this is, a side note there, where we can file another, another issue and handle that, deal with that later, or if it's blocking and then, preventing the PR to be merged. And… Typically, when we're in the gray area like that, it's when the PR can stall.
So, I don't know what your take is on exception handling in general, Also… So, you know that we changed, we upgraded to Silent ID, which is also returning a lot of things.
A lot of… so, ceiling tidy had a lot of issues, and most of them have been addressed, actually. There is… there's quite a few left, but they are not that different. It's the same issue repeated again and again.
So in terms of number of different issues, we don't have that many left. One thing that we have is this no-accept thing.
And… I think that we should… first try to clear up ceiling tidy, for everything else, so that we have a clear picture, and then we'll be in a position to address the new exception thing, but Only dealing with no exception, because we need to… To decide what we do, so, I mean, I saw that you have a proposal, I have another one. The two might be actually the same, if we dive into the details, but… I think that to clear that no exception thing, We really should put it aside and resolve that alone, not mixed with other changes.
So, all that to say that I think we should merge your PR, but I don't know if Tom is okay with that or not.
**Douglas Barker** 10:04 Yeah, I… I feel good about it. I think the only concern is, like you said, it touches the API, it changes the default value of the variant for the start span options. I think it's a… I think it's a reasonable, like, low-risk change, but somebody may argue You know, that's breaking or something.
So I could set… if that's the only thing that's blocking it, I could, revert that specific change and follow up in a separate PR, if you think that that would help unblock it. As far as the exception concerned, I think… You know, I… I… I believe that the change is a pretty big improvement as far as, Exception handling within that particular method, you know, starting spans, and then… where the exception, you know, case that was pointed out, where that's moved to in constructing the tracers, you know, I think that that follows what your proposal was.
you know, in the case that I was trying to make, which I think we need to define, like, what is initialization? What is the initialization phase for OpenTelemetry CPP, so that we can allow exceptions in those cases, and that's where you already have exceptions in the parsing, for example, I think.
**Marc Alff [MySQL]** 11:21 Yes, yes.
**Douglas Barker** 11:22 Constructing the tracing provider should be, you know, able to throw exceptions, and so on.
**Marc Alff [MySQL]** 11:28 I think the… Well, looking at… so, if you want to… if we want to resolve exception when executing something on a trace, we should fix the start span. Well, if we want to fix the exception on a span, we should fix start span.
If we fix start span, we should, fix, get tracerProvider, and so on and so on. And it goes… it falls down all the way back to the root, and the root problem is we don't have a clean unique entry point to initialize OpenTelemetry, where we could allocate all the know-op objects that we need, and set a default tracer, and things like that.
And… this would be the proper place to actually do all the initialization that may or may not work. Like, this initialization may fail with out-of-memory exception, for example, but it will only fail during the SDK configuration.
And once we pass that, once we have an SDK which is properly configured, then… every provider, Git Tracer, start spawn, or whatever, will have a fallback.
Like, when… well, if start span is not working, just return… return a no opspan.
Which is already there.
And so, I think we can achieve, something which is resistant to no exception.
But only if we have a clean initiation point from the SDK, and we don't quite have quite that yet.
**Douglas Barker** 13:02 Yeah, to me, it seems like one… probably, certainly low risk and probably non-controversial change would be to remove no accept from all the providers, SDK provider constructors.
And allow those to throw. I mean, right now, there's a lot of allocation that happens inside those anyways, and they're no excepts, so they're just gonna terminate anyways, so we might as well let the exceptions go through and allow users to at least do something about it.
Yes.
I would also argue that we should apply that to the… scope, objects, so tracer, logger, meter, so that when you create those, those constructors should also be Remove the no accept.
**Marc Alff [MySQL]** 13:50 It's…
**Douglas Barker** 13:50 I don't know if they do it that way, but I did see a… I forget which language it was, but one of the languages at least kind of called out explicitly, you know, that you should create those components at initialization time, and that's also, you know, in my applications, that's how I do it too. I know some of our examples kind of show just calling like, get meter, you know, directly all the time, and not caching the meters, or the loggers, or the tracers, but I think that that's probably not the recommended Right? Like, you should cache those yourself and, create them at a startup.
**Marc Alff [MySQL]** 14:28 Nope.
Yeah, so I agree that the… To me, the things that absolutely need to be no exception are the virtual methods from the API.
So, when the API says, get tracer is no exception, then the SDK should implement that as a no exception.
But from that point, I think the initial design was to say, okay, well, to achieve that, just put the no exception keyword everywhere.
And… I… To your point, I don't think we should have instructors.
Because then it's putting too much constraint on what we can and cannot do, and… If you can't even build an object, then the SDK is too much constrained and cannot work.
So if we have constructors that can flow.
Then, typically, on the get tracer, well, you try to get a tracer, if it works, you have one. And if it doesn't work, then you return a node tracer that was there in the first place.
**Douglas Barker** 15:36 Yep.
**Marc Alff [MySQL]** 15:39 So yeah, so I think it's… Overall, it's feasible, but it will need some work, and it will be… I think it needs to be done separately, focusing on no exception alone, not mixed with other changes.
**Douglas Barker** 15:52 Yeah, I agree. I don't think it should block that stark span performance PR, so…
**Marc Alff [MySQL]** 15:58 Okay.
**Douglas Barker** 16:00 you know, I… Obviously, I think the PR is ready to merge, but I don't… I want everybody to review.
I think a follow-up PR to your… to your issue that has the proposal of, like, Git Tracer Imple.
maybe just an initial PR to remove no accept. You know, like I said, I think it's no… it's low risk and low… not contentious to remove it from the provider constructors. I would advocate we remove it from the logger, the meter, and the tracer constructors, too.
Do you think that that's a reasonable PR to take?
**Marc Alff [MySQL]** 16:34 Yeah, it is.
**Douglas Barker** 16:35 Okay.
**Marc Alff [MySQL]** 16:37 So, the idea to get a git tracer imp… Get Tracer versus the Get Tracer implementation, the only change is… The try and catch block It's in a separate codebase, so when you read the code for the implementation, you don't see all the try-catch, good obscuring things, but otherwise, it's exactly the same. We could… we could do without. We could implement Get Tracer as… With a try-catch, and do everything we need to do, and if it doesn't work, then we return the new op.
**Douglas Barker** 17:10 Yeah. Yeah, I think that's reasonable, too.
Okay.
Well, that's a relatively simple PR, so I, you know, either you or I can follow up with that, just to remove the no accept from those constructors. I think it seems like a good next step, at least.
**Marc Alff [MySQL]** 17:29 Yep.
Yeah, I really would like to see the… well, in fact, there are so many, so many things happening at the same time. So, there is the ceiling tidy cleanup, where one contributor in particular, she… Contributed a lot of fixes to clean that up, and other people did as well, so it really… Got a lot of momentum, but at some point it stopped, and nobody is doing the last cleanup which is needed to get to nothing.
**Douglas Barker** 18:04 Mmm.
**Marc Alff [MySQL]** 18:05 So, there is that font.
I looked at what is remaining, there is a couple of things which are easy to do, we can do it as well. The only big point is exception.
So this is one front. There is another front where I don't know why.
the same contributor is just banging curl to death.
And she's finding a lot of things in the test HTTP server that we have.
In the way CULD operates, in the asynchronous code, and… assal and Tyson failures and whatnot, so I'm… on one hand, I'm very grateful that there are people investigating time and reporting things like this, because The bug report seems to be correct, and there is indeed an issue.
But at the same time.
It's, due to just the number of issues reported and the number of PRs to review, it's taking a lot of time just on that front alone.
And for me, this is taking time off of the Yamen configuration, for example.
I, I used to… spend a lot of time there, and I don't have that time anymore.
And, it's also Preventing to, to look at other things, like OWENT changes for CMake and things like that.
**Douglas Barker** 19:32 Yeah.
**Marc Alff [MySQL]** 19:33 So…
**Douglas Barker** 19:35 I think it's okay to triage those and review them as we go, but I also feel very, like, for the next release, what I would like to do is to have the YAML configuration and the programmatic configuration in really good shape.
Yes. It's getting there now, I… you know, the issue that I logged that was going to… or that the purpose is to decouple the trace… log metrics libraries from the SDK builder so that we can, you know, use YAML, but also build only what we need, and then have full control over all the builders. I'd really like to be able to get that into the next release, so that's what I've been pushing on.
There's some other… I'm gonna lock some issues. I think there's some… some… we're in a good position now to finish up the, resource detectors. That's… that's an area that needs work there.
The sampling is in really good shape with the composable sampler, that's cool to see.
**Marc Alff [MySQL]** 20:32 What?
Yeah, sampling is making a good progress, and in fact, I see a lot of people just picking small parts which are missing in the YAML schema, and say, hey, we need this, we need that, so it's good to see.
**Douglas Barker** 20:47 Yep.
So I think…
**Marc Alff [MySQL]** 20:51 Yeah, I'm only a favor to also continue on the YAML configuration, because actually, we'll have a dependency on that, so I need that to be rock solid also, because I will use it.
**Douglas Barker** 21:07 That sounds good. So I think… with respect to that, like, my PR that is breaking out everything from the, from the SDK builder, and putting it into separate signal libraries, and then actually using all the builders from the registry in the SDK builder. Like, that is…
**Marc Alff [MySQL]** 21:25 Yep.
**Douglas Barker** 21:25 A relatively big change.
**Marc Alff [MySQL]** 21:28 Yeah, I noticed.
**Douglas Barker** 21:30 So I've got that PR. I've posted some, you know, requesting some feedback from you. I'm open to breaking it up into a bunch of smaller PRs.
But it's really… I wanted to get a sense from you if you think we're going in… if I'm going in the right direction with this.
**Marc Alff [MySQL]** 21:44 So, I definitely think it's going in the right direction. Breaking the PR in smaller pieces is not going to change much, because there will be the same volume of code anyway. And the part I like is that it's the same pattern over and over again.
So, it's easier when reviewing some code, okay, once you get the pattern for one, say, one tracer, then you can repeat that for matrix and logs and so on, and it just works, so it's, the size in that case is not, not a big issue.
If another PR is the same amount of line of code.
and is, could change in CMake and ShareScript all over the place, that might be a different, different, story, but it's not the case.
**Douglas Barker** 22:39 Okay.
All right, well, let me know, you know, if you want me to break that up or not, but that's one that is also going to be, It's not going to be super difficult to maintain, but there will be merge conflicts as people want to fill in the rest of the details in the YAML.
**Marc Alff [MySQL]** 22:55 Mercer.
**Douglas Barker** 22:55 And all that's going into SDK provider, so it's gonna be… be some maintenance for me.
**Marc Alff [MySQL]** 23:00 So, I noticed that, especially in the context of APR, which is looking at composable samplers, So… I… it's an open question. I don't know what is the best way to merge OPR first, so that we have the new layout for the registry and all the callbacks there, and have people adjust, possibly with some merge collisions.
or if we should do the other way, have the small PRs that we have merged, and then, do the change in the history after. Do you have any… Comment or preference on that?
**Douglas Barker** 23:41 So the only ones I'm aware of are the recent one that came in with the attribute filter, like, that's relatively self-contained. That hits the view.
construction, so I'd be okay merging that one, and then the other one is the span, or logs to span bridge processor.
**Marc Alff [MySQL]** 24:01 Yes.
**Douglas Barker** 24:02 I don't know how close that one is to being merged, but that also, you know, is another one that we could get those two out of the way, and then I think we could Pause on other changes until mine is merged, and then everybody will have to, you know, retarget the YAML changes to those signal-specific libraries.
**Marc Alff [MySQL]** 24:21 Yeah.
**Douglas Barker** 24:24 Do you have an opinion?
**Marc Alff [MySQL]** 24:26 Not… not true. I mean, the… the goal is to make progress, obviously, and also, if we can avoid it, avoid having a lot of merge collisions. It's not so much for the collision itself, but it's for contributors who might not be as knowledgeable with the codebase.
So, someone who doesn't know the codebase as well as us may be… stuck with a merge we cannot resolve, for example, so I don't know.
On the other hand, I mean, even if that is the case, I think we can help them.
So… I will take a look at what we have left, but I'm more in favor of just merging your work just to get that out of the way, because if we… If we wait, there will be always something else, always a different reason to… To postpone it, and then, We will end up spending more time than we should on that.
So I feel it's better to get it out of the way. And… In the event someone has a big merch religion, we can always provide them some help and feedback.
**Douglas Barker** 25:37 Okay.
Yeah, I think… I think that… that sounds reasonable. If… if those, two that I mentioned, you know, I think we can approve the attribute filters, I can quickly rebase, or, merge that in.
**Marc Alff [MySQL]** 25:51 Okay.
**Douglas Barker** 25:52 And then, if you… I don't know if you've looked at the span, or logs to SPAN bridge, but if that feels ready to go…
**Marc Alff [MySQL]** 26:02 Yeah, I glanced at it, but a while ago, I've not looked at it recently.
Okay. And I think Lalita also had some comments on that, if I recall correctly.
So we need to see, what it was.
**Douglas Barker** 26:16 Okay.
Yeah, either way, if there are conflicts in other PRs, I'm happy to help the contributors work through it.
Okay. It shouldn't be too, too difficult. I think, getting… getting, the… Somewhat of the refactoring is going to be helpful to break things up and make it easier for people to contribute.
**Marc Alff [MySQL]** 26:37 But, I mean.
I've never been in a situation where we have so many PRs coming in at the same time.
But a heuristic, which is simple is the more we wait, the more PRs will stack up. So the best way to get out of it is to start merging anyway.
Even if we pick the wrong order, at least the pile will diminish, so…
**Douglas Barker** 27:06 Okay.
There were a few that I wanted to discuss, like, one that's been out there for a while is the published Doxygen. I don't know how you guys feel about this one. It is one that we put on the pinned, issue, where we need.
**Marc Alff [MySQL]** 27:21 Yes. You hope?
Yes, so, From… so I looked at it, from what I saw in the CI, the build is not working, and it looks like it's not finding, things in the proper, directory, maybe?
But past that, We'll need to reproduce it myself and try to see what's going on. So the code looks good, the only thing is the CI is not publishing anything, because the tooling is not finding the proper files in the proper location.
I don't think it should be that hard to fix, but it needs to… To solve that, you need to investigate, okay.
what is CI doing? How is the worker doing? What is the current working directory, when the code is compiled and whatnot, and blah blah blah, so… It's up to… those things with ZRA are to, to troubleshoot locally.
But otherwise, yes, we need… we need that. I mean, there's no question.
**Douglas Barker** 28:35 The other, PRs that have been out there for a while are these ETW PRs. I don't…
**Marc Alff [MySQL]** 28:41 Yeah… So, well, this is why I wanted also Tom or Lally to be, to be presenting the call.
So, ETWU is yet another kind of exporter, which is specific to Windows, so, boom.
there is some history there, so the first thing, those things would not even be in the OpenTeametry CPPM repository in the first place, because they are not part of the official exporters we maintain.
At best, they should be part of a CPP contrib.
But for historical reasons, they were implemented in CPP, so they stayed in CPP.
But the problem is, it's platform-specific.
So, you need to have Windows to test it locally, not to mention, I'm assuming, to have some backend systems to send data to, and so forth.
So for me, it's, Well, it's, it's a blocker, because I don't have that environment.
And, My understanding is that this was specifically maintained by Tom and Larit in the past, because obviously there are… I don't know… I don't even know if there were the original offers for that, or if someone else did that.
But we have, they have a stake in that. I don't remember if they're using that for some contribution they're maintaining in CPP Contrib.
Or if it's something else, but there is also… some Geneva exporter that we have… that we are maintaining and whatnot.
So, myself, I don't… Of course, I know the OpenTeameter API, But I don't know the details of ETW and what this is supposed to do, and all this works.
Which is why their input would be great for… to see what… what to do with this PR.
And… the part which is missing there is some clean status. Looking at the PR and the comments there, I don't even know I don't see… I don't see it approved, but I don't see comments on what to fix either, so it's in between to me, and it's the part which is… That explains why it has been, stuck forever.
**Douglas Barker** 31:04 Okay.
Yeah, I don't have a Windows environment either, so if we can't… do you feel like the CI doesn't cover the… components enough.
I don't know what tests we have in there, to be honest with you.
for ETW.
**Marc Alff [MySQL]** 31:23 Yeah, but those are… typically, it's an example where… so… ETW had no, activity at all for ages. The only activity there was just to fix, include what you use, and warnings, maybe, to get a clean CI, but not more than that.
And then recently, someone actually started to use it, reported some bugs, even contributed some fixes in there, so this was picking up, and then… the experience that we have today is that someone spent time, did some contribution, and they have been… they have been waiting, like, for, what, 2 weeks Two months, maybe, by now.
**Douglas Barker** 32:03 Sure.
**Marc Alff [MySQL]** 32:03 Which is not encouraging. I mean, it's harder for people to contribute than if you… if you know the feedback, so… But unfortunately, this… This really depends on the Lita and Tom.
**Douglas Barker** 32:26 Yeah, I think… I think going forward, like, we push for… if there's a test covering the change, or if it's a performance concern, if there's a benchmark covering the change, then we rely on the passing or the benchmark, you know, being reported, and just merge it.
I don't… I don't know about the test coverage for ETW, but we can look.
**Marc Alff [MySQL]** 32:50 Good.
But on top of that, there are things that seems to be specific to that implementation, like the way they assign trace ID is not the same thing as everyone else.
my story that you need to be aware of, but I don't.
**Douglas Barker** 33:05 Gotcha. Okay.
All right, well, we'll, like you said, we'll just, get feedback from Tom, and we'll let on that, if they can, join the next meeting.
**Marc Alff [MySQL]** 33:16 Yes.
So… So, there are many… many different things in many directions. I gather that you want… you really want to make progress on the YAML config file itself?
So, I'm… I agree with that, we should, we should do… We should complete it, especially because it's, not only it's a good feature, I hope so, but also it's getting traction with different people contributing things in that code space. So it's, we should take advantage of that and Make sure that people stay… Involved.
this reminds me, I also need to… Probably update a lot of status in the configuration repo itself.
Because every time we… every time we implement a feature in the YAML config file, we should declare that that feature is, is done.
Because there is, you know that there is a traceability matrix in the spec repo for all the features? There's the same thing for the YAML config. There is a traceability matrix for every single node and property.
And for every single, SDK there, to say, does this SDK support, permit use, and this property, and things like that?
Okay. So we should, we should update it.
**Douglas Barker** 34:50 Yeah, I think… I think that makes sense. Do you want… do you need help, updating that, or what's… what's the process you typically do?
**Marc Alff [MySQL]** 34:55 Oh, no, I can… I just need to take time to do it. It's not a big deal, but… something to… To keep in mind for me.
**Douglas Barker** 35:07 Yeah, well, it's always rewarding to check off all the things that we, completed.
**Marc Alff [MySQL]** 35:11 Nope.
**Douglas Barker** 35:13 The… yeah, so for me, top of mind is the… yeah, completing all this work on the configuration, hopefully checking off, you know, all compatibility with the… that matrix. And then the other one is on, kind of, these, like, key performance-impacting things. So, top of mind is the spin lock.
Yeah, I like that issue.
**Marc Alff [MySQL]** 35:35 movies.
**Douglas Barker** 35:35 to switch to Mutex in the, In the metric stack, so there's a few storage and aggregation classes that haven't switched yet.
**Marc Alff [MySQL]** 35:44 Yes.
**Douglas Barker** 35:45 I was just gonna put in the second PR to do all that. I was hoping to get some feedback to see if anybody could either share more about why SpinLock is there, or… You know, or any concerns, but for me, it feels like, I'm concerned, especially on different platforms, like ARM, other platforms where that spin lock, you know, just has, is not configured to work properly.
That's kind of where I'm coming from, so I'd like to see…
**Marc Alff [MySQL]** 36:15 So… So, I don't know the full story of that, so it's just a guess.
But I'm assuming that a spin lock in the first place was implemented as a spin lock because it was used in the API.
Typically to set a tracio provider, things like that.
For the singletones that we have.
And it was done as a spin lock, because it's very hard to implement an API which is header-only.
and make it multi-platform at the same time. So, it was done with a spin lock.
With just one assembly function with a test and set, and then you have something, a lock, that works.
because this thing was implemented and available in the codebase, most likely it was reused in other places, including in the SDK.
Where it should not have been.
A speed lock is really for something which is very fast, like, Assigning, changing, tracer provider, for example.
When you install a new Tracy provider, you replace the old one, and that's it.
But it's not to lock the entire metric system while collecting a new batch of metrics. This is not a spin lock.
So, I think that explains the state we are in today, where we can have some spin logs which are taking a long time.
And I totally agree with you that we need to replace that spin lock with a mutex or something else, at least a mutex.
Because Verisk is, under pressure, if we keep a spin lock, we will see CPU looping to death, and… Generating heat, doing nothing, and the… the process completely stuck.
And, at least with the mutex, we have a clear, Well, we have all mechanism, to work with that, and the system and the OS will know what to do with it.
So, yeah, I'm… it's just a guess, but I'm guessing more history than anything else.
History, the spin lock was implemented first, and then once you have it, of course, you reuse it all over the place without drinking.
**Douglas Barker** 38:36 So what I'm… what I'm thinking then, because I… we're on the same page, what I'm thinking is I'll just… I'll just submit a PR to swap it out everywhere in the metrics SDK stack, leave it for the provider use case that you mentioned in the API, and then… I probably won't go through an extensive effort to do… I can run, like, benchmarks before and after for the ones we have, but maybe not go through an extensive effort to add a ton of new benchmarks Because it, I don't know, for me, it seems obvious that it shouldn't be a spin lock, but I don't know if it's like that for everybody.
**Marc Alff [MySQL]** 39:09 Yeah. Boom.
the benchmark… so… If we have a benchmark, there is a risk that, hey, in this case, the mutex is taking longer, so someone will say, well, this is an aggression, it's less performant, why are you doing that?
But the part that people are not seeing is that there is a risk that code looks forever.
And, we want to avoid that, so…
**Douglas Barker** 39:40 Yup.
**Marc Alff [MySQL]** 39:40 Even having a benchmark is good, because we need to have benchmarks in general.
But I would not advertise this too much as a performance improvement, more like a robustness improvement.
**Douglas Barker** 39:54 Yeah, I agree. Like I said, my concern is about different use cases, different platforms, different deployments. If you deploy in a Docker image, or if you deploy on a single core system, or if you pin all the threads for the batch processors onto a single core, you know, what happens?
**Marc Alff [MySQL]** 40:13 Nope.
**Douglas Barker** 40:14 I think that the spin lock case, you can probably find yourself in a deadlock.
With how it currently is configured, so… That's why I would advocate we just do the Meetix, which it sounds like you agree, so I'll submit that PR, and then see if anybody has any feedback.
**Marc Alff [MySQL]** 40:32 But it looks good to me, so I should do that.
**Douglas Barker** 40:36 Perfect.
**Marc Alff [MySQL]** 40:37 And yes, you mentioned, like, different type of deployments.
There is something else also that can come in the picture to make things more interesting, is that someone may want to pin a given thread to a given CPU, adding a lot of complexity there, because then you can have that CPU looping to death, and things like that, so it's…
**Douglas Barker** 41:03 And that, yeah, that's one of my use cases, too, so… This is why I stopped the mic for me?
Okay.
Let's see, I think we covered most of the things. There's still this, regression. I saw it pop up again, so there's another test failing because of the gRPC thing. I'll, check again to see if that… I think that…
**Marc Alff [MySQL]** 41:24 Nope.
**Douglas Barker** 41:26 Don't know if it's been released yet.
**Marc Alff [MySQL]** 41:28 I've seen a PR from THC1006, I think, is our GitHub account.
That was about a race condition that can happen on exits between OpenSSL and whatnot in gRPC.
And the… the worker… so this thing… this thing is a bug that exists in gRPC itself?
According to our research, and the workaround was to explicitly disable a test case That we have on, in order sheet.
So… My understanding is that if this is exactly the same issue, this should be resolved.
Well, at least the CI should not be failing anymore. The issue still exists in gRPC, but it's not in our control.
But at least CI should be clean for that.
**Douglas Barker** 42:23 Alright, and then… I listed a few PRs, so we already talked about Owens, the CMake Rename, we talked about the DocShin. There's one, which seems popular, because it's been multiple issues, and people are, commenting on the PRs, dropping the stale async attributes.
From the cumulative exports?
**Marc Alff [MySQL]** 42:45 Yeah, I'm not familiar with this one.
**Douglas Barker** 42:48 So it's, 4140 pull request.
That's one that's been in there for a while. I don't think the contributors responded. They stopped responding to the other issues, so I don't know if they're… Watching it.
**Marc Alff [MySQL]** 43:03 Yeah, yeah, well, that contributor stopped responding to a lot of things, so… Maybe it's, She's not at school anymore, who knows?
Team.
By the way, I saw she had also a different PR on, the YAML config to split, This is when… way back when we discussed splitting all the libraries into a core library and the YAML library.
And based on the recent work you did, I think that PR may be obsolete then, by now.
**Douglas Barker** 43:41 It is, yeah, I closed it over the weekend. I had commented, I think, 3 or 4, or at least 2 times over a 2 or 3 week period, and she didn't respond, so I went ahead and closed… I closed it over the weekend.
**Marc Alff [MySQL]** 43:55 Okay, good.
So, we are back to 42 PRs, and… to close then. I was hoping on that to make some cleanup.
**Douglas Barker** 44:07 Oh, I think there's a few really old ones that we can close.
**Marc Alff [MySQL]** 44:10 Yes.
**Douglas Barker** 44:12 But, okay.
Alright, I think that covers everything that I wanted to discuss.
**Marc Alff [MySQL]** 44:23 Yes. So, well, you're looking at the same notes as me, so, on the upstream changes, I just looked, like, 10 minutes before the meeting and noticed a couple of changes in semantic conventions.
In Weaver that goes with it, so I will probably do a PR for that, just to upgrade.
And also… As we discussed last time also, OpenTelemetry Portal was a new release, so… We should probably update it for CMake, and then the question is, for Bazel, the gap.
We have a gap between Bazel and CMEC on OpenTelemetry Portal, which is widening.
Because Bazel is still on 1.8, and this is due to the lack of support in Bazel Central repository, which has not been updated.
So, I guess it's okay.
to upgrade CMake, because we need to, anyway.
But it's, I'm not terribly happy about seeing some gap widening and widening like this.
Yeah, I don't know.
**Douglas Barker** 45:37 I don't know what to do about that. I do feel like we should stay up to date, you know, at least with the main path.
with CMake, but I think the challenge with Bazel, which we talked about in Slack, is that somebody needs to publish all of these artifacts, including open tools.
**Marc Alff [MySQL]** 45:52 Yes, yes.
**Douglas Barker** 45:52 So…
**Marc Alff [MySQL]** 45:53 Yes.
And speaking of Bazel, actually someone did the work for OpenTelemetry 128.
**Douglas Barker** 46:01 Okay.
**Marc Alff [MySQL]** 46:01 And it was actually reviewed and merged, so it's, it's got in today.
**Douglas Barker** 46:08 Awesome. Perfect.
**Marc Alff [MySQL]** 46:28 So, yes. So, one thing also I wanted to discuss with you is, the next release, Do you have any… Fults on when we should make one, the spiritual… I haven't looked at how many changes we have, since the last one, so a lot of this… a lot of changes are renovate and dependable and things like that.
But in terms of fixes, I don't know if we have a lot or not, to justify no release.
But, I will be depending more and more on the config.yaml thing, and there is a lot of recent work that went into that, so I think we should make our release… So that, everyone can see the new… Well… the config.taml in general, but also the new schema, because then the schema 1.1 is supported now.
Yep. So, that alone is a good reason to upgrade.
And to publish.
**Douglas Barker** 47:39 I agree, and post the mutex fixes, it sounds like that was really impacting some Windows users, so I think it's worth getting it out there. What do you think, like, maybe… The last week of the month, or… End of next week? What do you think?
**Marc Alff [MySQL]** 47:54 Most likely the end of August, because it's, I think we still have a lot of cleanup that we can do to… that can get in.
So, not to publish something which is, That contains some cleanup, but not others, so to be in a state where we have something where that we… We think it's consistent, that would be great.
And the other parties, it's still the summer, so, I don't know what what people's availability is in general, but I may or may not be available the entire month to start with.
And also, I don't think, a lot of people will, will upgrade, even if we publish, so if we wait the end of August, then in September.
It may make more sense, because then people will… we'll wait. To put it otherwise, even if we publish today, I don't think it will be adopted very soon.
So we might as well, publish NATO.
**Douglas Barker** 49:00 Yep.
I like the goal of trying to complete as much of the YAML configuration as we can.
**Marc Alff [MySQL]** 49:06 Yes.
**Douglas Barker** 49:07 I think that… I'll log some issues, like I said, for the resource detector, and I'll reopen that main issue, and log some issues against it, and then that should drive some contributions, because that's an area where I think people can easily jump in, add some things.
**Marc Alff [MySQL]** 49:23 Yep.
**Douglas Barker** 49:26 Cool.
Alright.
Well, I'll, you know, keep an eye on my PRs if you have any feedback, just ping.
**Marc Alff [MySQL]** 49:34 Yes, I… I wish.
Okay. And so, my availability is still up and down. I mean, I will try to be present on the different team meetings, but… I also have new commitments on… on Wednesday, all three at the same time, so I don't know.
Oh, that will work out.
But, otherwise, I will be looking at issues and PRs anyway.
**Douglas Barker** 50:06 Okay.
Alright.
That's good.
**Marc Alff [MySQL]** 50:12 Sounds good. I don't have anything else, so I don't know if you have… Other things you want to discuss?
**Douglas Barker** 50:18 No, I think that's it.
**Marc Alff [MySQL]** 50:20 Okay, well… Nice to talk to you, because this has been a while, and it's also nice to… I remember when, in many cases, I was so connected to the team meeting, only to find me alone, so… It's not a good feeling, so…
**Douglas Barker** 50:39 Yeah, I know, I know how that feels now. Yes, yes.
Alright, cool, thank you.
**Marc Alff [MySQL]** 50:46 So, yeah, so it's good when many people can make it.
**Douglas Barker** 50:50 Yep.
**Marc Alff [MySQL]** 50:51 Alright.
Take care, Vin.
**Douglas Barker** 50:54 too.
**Marc Alff [MySQL]** 50:55 Bye. Bye now.
