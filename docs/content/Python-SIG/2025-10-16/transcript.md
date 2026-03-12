SIG: Python SIG
Date: 2025-10-16
Duration: 55 minutes
Zoom Recording URL: https://zoom.us/rec/share/cY172jiKN97BTD2gpfOnweer5PAAWNeuXq4gH5tz3qTNrAcdv-Zt2RLRpw9fcp-F.Z4oU0587LIzOZaW8
============================================================

## Zoom Recording Transcript

**Riccardo Magliocchetti** 02:53 Hello, everyone.
**aditya mehra (splunk)** 03:00 Hello.
**Dylan Russell** 03:00 Blue.
**Riccardo Magliocchetti** 03:33 So welcome, everyone, to this week's Python Seek call.
In the meantime, we are waiting for more people to join. Please add yourself to them.
notes document?
And if you have any topic you want to discuss, also add it to the document, please. Thank you.
**Aaron Abbott** 05:15 Hey everyone, how's it going?
**lechen** 05:18 Here it is.
**Aaron Abbott** 05:20 April.
**Riccardo Magliocchetti** 05:40 Okay, welcome everyone again. I think we can start.
12 people, huh?
And… okay, first stopping is from me. Like, early today, I released, 1.38, release.
Finally, it was a smooth release.
Just one small annoyance… That is that, the tool you're using to check for, backward incompatibilities.
in API, once… well… Reports, change of version as error.
And so I created a quick PR, to… Like, ignore that.
Yeah, since it's trivial to do, I think.
We can do that.
And yeah, like, we don't need to… I'll take a look right now, but if you have time, please take a look.
Adjust to one line change.
And… on the next topic, also from me… About the log stabilization.
Like, now it's time to decide what to merge next.
And… Hector, unfortunately, is not attending right now, but the option We have our, this true.
4676, and 4647.
So, I think it's up to Hector, the first… you know, once he replays one, we can… Review, and then merge, and then move to the other.
Unless any of you have any opinion on that, but… I guess we want to merge them both at the same time, so… Yoga doesn't count much.
**Aaron Abbott** 07:41 Ricardo, we released the, warnings PR with the last release, I'm guessing.
**Riccardo Magliocchetti** 07:48 Yeah, the release I did today introduces a couple of warnings on some classes that we are going to rename or remove in the next release, and that is log data and log record.
And… yeah, so it's just, like, for… like, the warnings are only for, callers outside our own SDK, at least, what was the plan?
And so, we hope that downstream users like, OpenLelementary, we'll see that there, and… Act accordingly, or at least prepare to change some code.
**Aaron Abbott** 08:35 Okay, cool, yeah. I mean, I think… Let's definitely do these for the next release, then.
Yeah, thanks for leading this, Ricardo. It's kind of a… Tricky situation, but yeah.
**Riccardo Magliocchetti** 08:51 That's true. Thank you for reviewing, helping me with the warning stuff.
By the way.
**Aaron Abbott** 08:58 Oh yeah, of course.
Did we merge also the, like, the simple renames?
**Riccardo Magliocchetti** 09:04 Nope, because both, PRs are, I think they are, have conflicts.
And so all… Yeah.
I think we can ping Ektel and ask to… Rebase then, so we can… Stop looking at them.
Thank you.
**Aaron Abbott** 09:34 Okay, great.
**Riccardo Magliocchetti** 09:38 Cool, and… okay, next topic is from Nakwar.
**Nagkumar Arkalgud (Microsoft)** 09:43 Hi, so, not quite Microsoft. So the land… we successfully released the… OpenAI agents tracing, and we called it V2, so we get a new package and all those. Similarly for Langchain, OpenLLM Metri has the namespace for, OpenAI and the, like, OpenTelemetry Langchain, package.
So, we want to rename it as V2, and this is a PR. So, I've done two things here, which I'll be breaking up into two different PRs. This one is updating the collectors to the latest According to the data spec, and renaming it. So I'll create a new PR for the rename, and then follow up with this one.
So we are all in sync. I wanted to bring up the rename part, just to stick to the standards of what we have done before, and make sure everyone's on board with calling it hyphen V2, like, adding SFX of V2.
**Aaron Abbott** 10:51 Do we have… do we have Surya on?
I don't think so.
Yeah, I thought… I think we had checked with TraceLoop before, and kind of agreed to do the normal thing, or the thing we did for Vertex, where we share the package versions, but it seems like, maybe Nira's on vacation, we haven't been able to get in touch.
Is that still the case for this one?
**Nagkumar Arkalgud (Microsoft)** 11:23 Leighton, I think… I haven't directly reached out, but .
**lechen** 11:29 Aaron, what did you mean by, is this still the case for this one? Is it still the case that you're on vacation, or…
**Aaron Abbott** 11:37 No, no, no, like, I think, if I remember right, we had talked with him before about, The correct response.
**lechen** 11:46 I reached out to him, about, like, a couple of weeks ago, and I didn't get a response, and we also At least for the, Openai agents, which is… I guess, more urgent, was more urgent, which is why we just went ahead with the V2 moniker.
**Aaron Abbott** 12:09 I think Nagomor has…
**lechen** 12:12 Customers who are kind of waiting on this to be… Or at least, to take dependency on this, which is why we have velocity in mind.
I don't want to, kind of, step over, like, you know…
**Aaron Abbott** 12:27 Oop, or…
**lechen** 12:29 what Nier is expecting.
Especially if we did, kind of… Discussed.
With them, but we do have a… Urgency for needing this.
released. I think it's been merged for a while now, too, so… I think Nakamar also, Did you have a chance to speak with the original authors or component owners of the instrumentation?
**Nagkumar Arkalgud (Microsoft)** 12:56 Yes, Sergey and, another person. I spoke to Sergey on Slack. Sergey is okay with this, just a little too as, his suggestion.
He said he's not feeling great today, so he'll probably not join this, but I'll definitely get his approval before merging.
**lechen** 13:20 Yeah, I guess either that, or, I think… There does seem to be another… Owner of the original… Package names, please?
What is… when do we need this bike?
Nakamura?
**Nagkumar Arkalgud (Microsoft)** 13:41 This one can probably go down next week. Right now you will be out on vacation, and I have no idea how to release them.
**lechen** 13:53 Right. Well, I won't be here next week, so, you can take a couple of strategies where Either… We can reach out to… I think… What is this thing? G… G-A-L-K-O-M? Gal?
**Aaron Abbott** 14:17 Yeah, no.
I think it would be…
**lechen** 14:21 Aaron, either Aaron or Ricardo, if you could email them, because I only have, like, a day left, so probably can't continue correspondence with them, even if they do respond.
But if we can get ownership of this namespace, we can just produce… we can just proceed as planned.
Or if it's really, like, a… Yeah, yeah, I guess we'll just see how they respond, and if it's not within a meaningful amount of time, we might have to revisit this.
**Aaron Abbott** 14:50 Okay.
**Nagkumar Arkalgud (Microsoft)** 14:52 Yeah, I dropped in my email in the chat, Just if somebody's emailing, please keep me in the loop, and I can take it from there.
**Aaron Abbott** 15:00 Once somebody starts the convo with an intro or something.
Yeah.
So it looks like Ricardo won't be here next week. I… Should be, but, Yeah, I feel like maybe… You know, we can sync on Slack also, but maybe we should just go ahead with, the lane chain V2 thing, I don't know, is anybody from Cisco on the call?
Who knows what's going on here, or what the previous, like, discussion was?
**Keith Decker** 15:35 Hey, Keith here.
**Aaron Abbott** 15:38 Oop.
**Keith Decker** 15:38 we're… Is this where we were talking to Nair? Or no, that's TraceLip stuff.
anything about the version stuff for LangTune, sorry.
**Aaron Abbott** 15:49 Okay.
Okay, why don't we pull up in Slack, maybe, But I guess I'm okay to do the V2 thing, it seems… better than, you know… I'm not sure we'll get a timely response, so yeah.
**lechen** 16:08 Right.
**Riccardo Magliocchetti** 16:10 Yeah, maybe, like, next time we introduce a new, instrumentation from what is, already been… Which name has already been taken by TraceLoop?
maybe we can, like, sort out the naming with Tracelope before.
merging that.
So, at least, like, We are not blocking anything, like, later, we are in a hurry later.
What do you think?
Yeah.
**lechen** 16:48 I think, realistically, like, I mean… I think logically, that is the desired outcome, but realistically, like, that doesn't really happen in the community, right? So… Like, we did… we reached out to Nier, like, weeks before… or, like, two weeks before.
But it's just unfortunate timing that he is on vacation, so cases like this does happen, and if he's the only point of contact, like, we need to get… sometimes making rushed decisions, it's unavoidable, but I think in the future, yeah, if… I don't foresee that many, kind of, like, as urgent, kind of, rollouts.
So perhaps we can kind of get ahead of these… Conversations before needed.
Hopefully the Vertex AI one, Aaron was, was a lot easier.
**Aaron Abbott** 17:45 Oh yeah, it was fine, I guess my… I think what… I think what Ricardo's saying is maybe, like, we could get the ownership added before we do the… merge the initial PR.
To get, like, the share ownership on PyPy in the future.
Which seems reasonable to me, yeah.
**lechen** 18:15 With that being said, I guess, is there any other instrumentations right now that we want to kind of push forward ownership for that are not released yet?
**Riccardo Magliocchetti** 18:27 I think we have a PR for Weave yet, or something like that, right?
**Keith Decker** 18:32 Yeah, I was gonna mention, we have the initial structure PR merged, but we haven't done the actual instrumentation yet, because we're still waiting for ownership and some of the genetic tool stuff.
**lechen** 18:48 Cool, so we definitely should start that conversation and reviviate?
I'm assuming Trace Liberty has a… Instrumentation for that.
**Keith Decker** 19:01 Yes, and it would follow the same… V2, though I changed it.
**lechen** 19:10 Cool.
**Riccardo Magliocchetti** 19:22 Okay… Any other comment, or we can move to the next, topic?
that is this PR for implementing, severity filtering on logs.
**guptaradhika** 19:41 Yeah, so, this is according to the spec which is linked in the description, so it introduces two filtering, parameters. One is the minimum severity, and the other is, if it's, like, trace-based. So right now, I've implemented the logic, in the SDK, OpenTelemetry SDK package, and I've added to the, log, record and log processor, but, Leighton, like, correctly pointed out that maybe Like, it's not the best idea, considering that we're still stabilizing the logs, so if we should kind of go with the approach that Language Go is taking, where they added to the log account processes instead, so… I wanted to get people's thoughts on it, like, what would be the best way to go forward?
**lechen** 20:42 Yeah, so for context, just a little bit about this PR, this spec recently added new VIN severity and trace-based Filtering, like, log filtering, configurations.
It's, it's part of, like.
a component that is still in development called the Log Configurator.
Since it's still in development, it's like, You know, it's like… Implement as… you please, I guess, until it's stable. You take that risk.
I think, the spec got approved, and… Just like me, some other language owners have, expressed concern that we're, like, adding additional things to the API layer, or the API of the SDK.
Especially Go, and they went ahead and did the implementation internally via log processors instead of directly changing the API.
I was just making a suggestion that perhaps we could do the same.
Either that, or, like, just… Not implement this right now.
Or at least create the component, but, indicate that it is in development.
The timing is kind of poor, though, because, like, we are trying to stabilize logging SDK, so, like, my personal preference is to, like, wait Until we do that.
Especially because this is in development into spec, but interested in what everyone else thinks.
**Aaron Abbott** 22:27 So I just looked at the PR, it looks like it's just adding two new, like, named arguments… optional named arguments, right?
Like, that's the only public API change here.
**guptaradhika** 22:37 Yes.
**Aaron Abbott** 22:40 Leighton, like, what was your concern, Like, it's not introducing log configurator, it seems like, it's just adding those two.
**lechen** 22:50 Yup.
**Aaron Abbott** 22:52 Yeah, I don't know if…
**lechen** 22:54 If you take a look… can you open the spec, Radhika?
I linked it in the chat there.
Yeah, so, like, the min level and then the trace-based filtering It looks like it is… Like, attributes or, like, parameters of the logging configurator, so… it's like… I don't know if, like, if we eventually introduce this, it's like, we're gonna have different ways of… configuring this, and I don't know if that's a… A good state to be in.
**Aaron Abbott** 23:32 I see.
I mean, that seems like.
**lechen** 23:36 We'll see…
**Aaron Abbott** 23:38 Yeah, certainly, like, good feedback for this PR.
If it's just not, not exactly implementing the spec here.
**lechen** 23:46 That's right.
Weird.
Yeah, so I would say, like, we either want to, like, fully implement Login Configurator and, like, explicitly mark it as, like, in development.
We either wait on implementing this once… until, like, logging… logging SDK is more stable.
or we implement it internally, similarly to how Go's doing it.
Okay with either one or two.
But that's just my preference.
Yeah, recorded.
**Riccardo Magliocchetti** 24:23 Yeah, kinda related to this.
**lechen** 24:25 Kinder alert.
**Riccardo Magliocchetti** 24:26 I was, investigating implementing the trace configurator.
**lechen** 24:32 Fifth place, right?
That is, in development too, so…
**Riccardo Magliocchetti** 24:37 Yeah, like, if you can… you know, have a shared vision on this.
would be helpful against.
**lechen** 24:47 Yeah, it's leaking.
Oh, that's a good… that's a good point. I didn't even know they… Tracing kind of configurator, yeah.
I guess it's a, kind of a push from the community to kind of align on converged component, or a story of how to make configurations, I guess?
It's interesting that they're actually pushing this to the spec.
I thought this would be, like, implementation detail, but I guess not.
Yeah, so, Radica, I would say that, like.
I think you got this from Ludmila's feedback, right? In terms of reviewing our API layer?
Right. So, I think if… This is needed.
I would say… you should probably implement Login Configurator as well.
Which is probably a… like, you want to think about the… Reusability of our architecture, across the signals as well, if we want to do that.
**guptaradhika** 26:13 Okay, yeah, I'll move, I'll do that.
**lechen** 26:15 Okay, yeah, I'll move under that.
Yeah, and keep in mind, I think this specific task is not needed for the logging stability work, so… keep that in mind as, like, a… I know you kind of picked this up because, like.
There is a list of stuff under logging, but… In terms of, like, stability, it's not the highest priority.
or stabilizing the SDK.
Just… just a net wire.
Okay.
**guptaradhika** 26:55 Yeah, thanks for the feedback.
**lechen** 26:57 And thanks for the people that read.
Thanks.
**Riccardo Magliocchetti** 27:09 Thanks. And then, next topic from Alitia.
**aditya mehra (splunk)** 27:16 Hey, hello guys. Yeah, from… From Cisco Splunk. Yeah. So, one thing that I… the instrumentation Langchain package.
I was going over the dependencies, and I just see this on line 29 and 30. I think we are using a version of, Which is, Which is older, but the tracer is referring to a schema which is not present in these versions.
So I think we need to bump up these versions to the latest one, so, like, 50… 8 or something.
Yeah.
But I was going over Nagk Kumar's PR, and he has that change in his.
But I don't know if we should wait for that PR to go in, or if we can make a different PR for just this small change.
that I can unblock, Like, I think, now, Kumar, you were following up with Ridhima and Sergey, right, on an example?
So that, you know, we can create an example from here, and utils, and how to instrument it.
Yeah, just that.
Yes, please, Aaron, you have your hand raised.
**Aaron Abbott** 28:31 Yeah. Yeah.
So, sorry, was this change needed?
After the other change, or is it already broken, just in the main brain?
**aditya mehra (splunk)** 28:40 it is already broken, because if you go to source, right, in the init, because I had ran it, and I'm getting an attribute error, because the schema URL is throwing a fit because… I can share the link.
**Aaron Abbott** 28:56 Okay, yeah, I know, please send a PR whenever, I don't think it needs to be blocked on the other one.
**aditya mehra (splunk)** 29:02 I can put that PR, the init one here as well, just where am I?
I just put it here as well, in it on line 79, where it is referring that, if somebody wants to open it.
**Aaron Abbott** 29:14 Huh.
Yeah, and if I can make a recommendation, For some of the other packages, I don't know if we have it here, but let me add this to the notes.
**aditya mehra (splunk)** 29:25 Let's see you.
The thing that it is referring is the… is available in the newer semantic convention.
**Aaron Abbott** 29:32 Are you able to hear me?
**Riccardo Magliocchetti** 29:35 Yeah, exactly.
**aditya mehra (splunk)** 29:36 signal.
**lechen** 29:39 Yeah, we can hear you.
**Aaron Abbott** 29:43 Okay.
Yeah, I was saying that.
**lechen** 29:47 Enjoy the podcast.
**Aaron Abbott** 29:50 Yeah, I think that makes sense. I'm adding to the meeting note an example, Where you can test against two different versions. I don't know if we're not already doing that, but my recommendation would be, like, set the lowest version in the requirements, and then Set, like, an explicit upper version, because the tilde equals doesn't really work with those beta versions.
So what you can do is… I had an example in the meeting notes that you can look at, but, please do that so that the tests cover both, like, the oldest and the newest scenario.
And you can, have a little bit more confidence.
**aditya mehra (splunk)** 30:29 Okay, got it. So it is, like, just changing how we are adding the dependencies, like the tilde and all those things.
Got it.
**Riccardo Magliocchetti** 30:42 Thank you.
And then… Next topic is from Kyiv.
**Keith Decker** 30:56 Oh, hey, so… When we did the GenAI utils, we just got the first PR through for inference. As part of doing that PR, we had kept the scope of it pretty small in order to keep the review as small as possible. This one is just adding a lot more of the SUMCOM attributes for request and response, as well as cleaning up some of the unit tests to just not have a bunch of, repeating code as soon as we're testing for these attributes. So, just get some eyes on this for additional attributes, and that would be nice.
**Aaron Abbott** 31:32 Okay, cool.
Is… is the next step kind of to integrate one of the interpretations with the… with the utils here?
**Keith Decker** 31:43 Next up for me is to add metrics and events for Chennai Utils, and we also have some parallel work going on for putting these into Langtrade.
For the instrumentation, so…
**Aaron Abbott** 31:57 Yeah, I think we're kind of waiting on metrics and events for those as well.
Okay, yeah.
Alright, that sounds good to me. I imagine when we go to integrate everything, there might be some… Small kinks, but that makes sense.
**Keith Decker** 32:13 Oh, I'm sure. It'll be fun.
**Aaron Abbott** 32:17 Okay, cool, thank you, I'll, try to take a look.
**Riccardo Magliocchetti** 32:27 Alright, thank you.
Next topic, also Gen AI stuff.
From Luke.
**Luke (GuangHui) Zhang** 32:36 Hi there.
So, this is the PR. We introduced the instrumentation for MCP. The problem we are facing, we are trying to resolve, is, So currently, there's no open telemetry support from MCP SDK, so that means, you know, when we trace the distributed system, if they involve the MCP server.
It doesn't propagate as a context, so that causes a broken trace.
Right, so, the work this PR, does is, number one, propagate the context, so make sure, you know, we have a good choice.
Number two, just add some attributes. I understand, you know, we only have a draft for semantic convention for MCP, It's a student trial, we don't have a standard. We haven't standardized it yet, so that's the two things this PR will do.
The core code is just around 400 or 500 lines of Python code, and most of the code are examples. I, I built some examples, for the end-to-end testing, MCP client, MCP server.
Yeah, I haven't found any PR related to this. I hope this can be a place, you know, the community can work together to get this done, because without this context propagation.
I don't know, the tracer would be broken, right?
As a background.
I already got some career feedback, I probably will address them by today.
Yeah, that's in my… That's on my PR.
**Riccardo Magliocchetti** 34:28 Thank you. I think I already added a comment.
Yeah.
About, do we have semantic convention already for this stuff?
**Luke (GuangHui) Zhang** 34:40 We have a draft, I will put the link there. The semantic convention group, they are reviewing that. It's not finalized, it's just a PR.
**Riccardo Magliocchetti** 34:51 Okay.
**Luke (GuangHui) Zhang** 34:52 Another question, your feedback, why Python 3.9 is not supported? Because the MCP SDK, explicitly say they don't support Python 3.9.
**Riccardo Magliocchetti** 35:09 like, there has never been a release working on Python 3.ni?
**Luke (GuangHui) Zhang** 35:14 the MCP SDK.
**Riccardo Magliocchetti** 35:16 Okay.
Okay, so it's fine. Like, I thought that you didn't add that because it was recently… Made the EO.
But, yeah, it's fine, no problem.
**Luke (GuangHui) Zhang** 35:31 Nope.
**Aaron Abbott** 35:34 yeah, a couple things that… I mean, On the 3.9 thing, what's, like, the oldest version of the MCP client that you support? Because… There probably was a release recently that did support it if you, you know, need backward compatibility.
**Luke (GuangHui) Zhang** 35:50 I think they require Python 3.10, I can find that there are docs and put a link in the PR.
**Aaron Abbott** 35:59 Okay, so yeah, I think somebody mentioned, but yeah, please, please join the, Hotel Gen AI SIG, it's on, Oh god, here we go again. Tuesdays… Tuesdays at… 12 Eastern?
I don't know if you've seen that already, but this would be a great topic. We also discussed, like, instrumentation PRs over there.
**Luke (GuangHui) Zhang** 36:25 Okay.
**Aaron Abbott** 36:26 Yeah, that was one thing. Another thing is… the package name here is… it's like introducing a new package, right? This one is also part of Traceloop already, So, like, that discussion we were having a little bit before about the package ownership, we should get in touch with TraceLoop and see if They would be open to sharing the… this package on PyPi, like we're doing with some of the other ones. Have you been in touch with them at all?
**Luke (GuangHui) Zhang** 36:55 No.
**Aaron Abbott** 36:58 Okay. Yeah, because otherwise, I mean, we can't… we just can't publish this, right? We don't own the package on FiveBy.
**Luke (GuangHui) Zhang** 37:06 Okay.
Would you please give your feedback, also put your feedback on the code review, so make sure I will record that and follow up that.
**Aaron Abbott** 37:17 Yep, yeah, and then one last question, you s… Do you think we could split it into, like, I mean, I think this is good, because we can kind of see everything working end-to-end, but the PR is a little bit big. I know a lot of it is generated files and stuff, but, Yo.
**Riccardo Magliocchetti** 38:05 Luke, are you still around?
**Aaron Abbott** 38:09 Okay, yeah, what do you think about maybe splitting this, or we could get… I think maybe wait until after the SIG meeting on Tuesday, if you're able to make it, and we can, And I discussed splitting it just because it's a little bit difficult to review with the number of examples and stuff.
**Luke (GuangHui) Zhang** 38:23 Sounds good. We'll do that.
**Aaron Abbott** 38:26 Okay, cool, yeah.
I'll try to take a look.
**Luke (GuangHui) Zhang** 38:33 Thank you.
**Riccardo Magliocchetti** 38:36 Yeah, by the way, like, I repeat what I said last week.
And… and please, like, people that is trying to contribute instrumentation, please also spend time in reviewing someone else's instrumentation.
Because otherwise, it will be very hard to move things forward, because there are more people that write code, but reviews code.
And… Yeah.
Thank you.
Okay, next topic is from Aaron.
on independent releases?
**Aaron Abbott** 39:20 Yeah, we don't have to spend too much time on this, But I think we probably have, like, closer to 10 packages now in Contrib, which are using, like, the independent packaging, they're not part of the lockstep release in the overall contribib rep repo.
I think we've ironed out a lot of the kinks, specifically, like, around releasing, so I just did a couple releases, and they went pretty well. I had to send, like, one PR to update the workflows.
But… I think the issue that I see a lot is when somebody adds a new package, there's, like, a lot of small areas of boilerplate that you need to remember to add. Like, there's, like, the… Which file is that?
They each just the INI, which excludes things.
**lechen** 40:08 The HDIST INI, which excludes things.
**Aaron Abbott** 40:18 Yeah. So… so there's that. But also, I don't think we have, like… so… I'm wondering what, like, we want the release process to be for these, Because right now, it's just maintainers, right?
So, somebody asks, like, a maintainer to do a release, we can go click the buttons to run the workflow to do it. I think… I think it's okay for now.
But, yeah, it might become a bit of a bottleneck as we have, like, you know, 10 independent release packages, somewhere around there. And then also, like, we don't… we haven't really written down the process in terms of approvals, so when you click the button, it sends a PR… sends two PRs, right? Do we expect to have somebody review those PRs, or do we want this to be super lightweight, and just let people kind of… Do these independent releases without a bunch of scrutiny.
I think I'm okay with that. We should probably just write it down somewhere.
See, I just want to get people's thoughts on that.
**Riccardo Magliocchetti** 41:23 And in order… True… Like…
**lechen** 41:27 Yeah, in order to… Oh, sorry, go ahead, Robert.
**Riccardo Magliocchetti** 41:30 Sorry, like… We need, like, at least approvers, like, because code owners, code component owners won't work, like, where approval won't work, right, for merging.
**Aaron Abbott** 41:47 For merging the release, you mean?
**Riccardo Magliocchetti** 41:49 Yeah, for merging the PRs, but the release creates… That the workflow creates, yeah.
**Aaron Abbott** 41:55 Yep.
It's a… It's not a big thing, but it's just a little toilsome, so you have to, like.
Click a couple buttons, and then you have to, like, find the branch name, and it's kind of a human process, so you have to… Make sure that you fill out the form correctly when you, run the workflow, so… I think that would scale alright if we made that a little easier.
like, I'd be okay with just, like, a maintainer being able to do that.
If we make that process a little smoother, but… Yeah.
**Luke (GuangHui) Zhang** 42:29 What is the process to become a code reviewer and an approver?
I am interested… In working in this area.
-Oh.
Can anybody share with me, the process?
**Aaron Abbott** 42:47 Yeah, so there's… Maybe I can, stick it in the chat, But there's, like, a pretty well-defined process. Have you… have you contributed at all to the project yet, or is this kind of your first contribution here?
**Luke (GuangHui) Zhang** 43:01 Contribute a lot to JavaScript, Java, C++, and Donet. It's the first… also a few… a few Python.
Pit…
**Aaron Abbott** 43:13 It's just you?
**Luke (GuangHui) Zhang** 43:13 I joined Amazon a few months ago, started working on this area.
**Aaron Abbott** 43:18 Yeah, gotcha.
**Luke (GuangHui) Zhang** 43:20 Okay.
**Riccardo Magliocchetti** 43:22 You are already a confident owner for Potoco Instrumentation, right?
Yeah, probably, like, again, like, People stick reviewing stuff.
we can probably add more approvers in the NGA group, I think.
**Luke (GuangHui) Zhang** 43:44 Sure, I'll be happy to… to learn and contribute.
**lechen** 43:48 I'll be happy to… In the… in terms of the, Aaron, we're specifically talking about, like, Some of the boilerplate stuff.
And, like, we have a pretty good… Guidance on contributing for, like, instrumentations already, like, when you're creating the instrumentation?
The pain point right now is, like, because we have this special manual release process, there's a lot of things related to our, like, infrastructure that people might have to consider when releasing, right?
How do you envision, like.
Like, I don't think having a list of approvers would, like, automatically tag them.
To review that kind of stuff.
Right? Like, it's… you would have to just have prior knowledge of how the ecosystem works, right?
How do you imagine tackling that?
**Aaron Abbott** 44:46 yeah, I don't know… I don't know if that's even what I… wanted to bring up here. It was more just, like.
it's been a somewhat toilsome process. We've worked out a bunch of kinks, but… still, like, every time I do a release, I have, like, 5 tabs open, And then I, Have to copy the… the right branch name for the release, and then sometimes the… or usually it's too long for the field on GitHub, so I can't see what I typed. Sorry, I'm kind of ranting at this point, but… And then also, like, the each disk thing, like, there's a bunch of small places that you have to update.
**lechen** 45:21 And then also, like, each of this thing, like, there's a bunch of… Yeah, so yeah, yeah, I think those are actually valid concerns that, like, us maintainers are into. I'm just wondering, like, how does having more approvers on release PRs help with that?
**Aaron Abbott** 45:44 That's not what I was asking. So, like.
right now, I could… since the OpenTelemetry bot sends the PRs, I could approve both of them and merge them. And I'm just… I'm just asking if people are okay with that, like, I think that's… that's fine for these independent releases, we should just write it down somewhere.
**lechen** 46:06 I see, I see what you mean.
Got it.
**Luke (GuangHui) Zhang** 46:09 How much effort do you take to do the release?
**lechen** 46:12 How much air first?
**Luke (GuangHui) Zhang** 46:16 Oh, I heard some echoes, sorry about that.
I probably can't spare.
**lechen** 46:21 some time to help.
**Luke (GuangHui) Zhang** 46:22 to the release.
**lechen** 46:24 Yeah, that's me, my bad.
**Luke (GuangHui) Zhang** 46:27 Let's say I can probably 3 hours every week, or 4 hours, half day every week, to help you do the release thing, if you have a well-defined document.
I think I'm… I'm pretty… I quite understand how this open telemetry works, because before this, I had been working with Microsoft for the Office of Telemetry for almost 10 years.
before this open telemetry things, so I can spend maybe 4 hours every week to help you do the release things.
If you need.
**Aaron Abbott** 47:01 I think, I think, I appreciate… I think a better… like, I guess what I'm getting at is we could improve the process a little bit, so if you have time to work on that, and you're really familiar with, like, Python tooling, I think that would be an awesome thing, and we can… we could put together, like, an issue with some discussion on this, but, like, there's tons of projects out there, like.
Python monorepos have gotten a little bit better in the last couple of years, but, like, there's, like, release please, there's the changelog generation stuff, we have, like, a bunch of penetrials and things that are… a bit annoying with our process right now, and we could look into approving, Sorry, I think, Ricardia, you had your hand up.
**Riccardo Magliocchetti** 47:42 Yeah, like, was going to ask, like.
since, like, I don't… well, I probably have done, like, one, release of, of a separate, package with our tooling, and then don't remember the details.
So, like, maybe if you can write down what the pain points are at the moment?
Like, not right now, like, we can maybe discuss on specific issues.
**Aaron Abbott** 48:12 Nope.
**Riccardo Magliocchetti** 48:13 Yeah.
**Aaron Abbott** 48:14 Okay, yeah, let's do that, and then, Luke, if you have time, maybe we can chat on the issue. I can tag you there, if you.
**Luke (GuangHui) Zhang** 48:22 Yeah, yeah, definitely, feel free to Slack me. I think I can promise maybe just 4 hours every week, and that should be fun.
**Aaron Abbott** 48:31 Okay, awesome. I think for this discussion, let's just… I want to move on, but, just… can we focus on this one question? Like, if I send the independent package release PRs, is it okay if I approve them and merge them? Like, can we just write that down? Are people okay with that?
**Riccardo Magliocchetti** 48:49 It's fine for me.
**lechen** 48:57 Yes.
**Aaron Abbott** 48:59 Okay, cool. I will, I will follow up with that, and we can move on. Thank you very much.
**Riccardo Magliocchetti** 49:06 Thank you.
Last topic is also for me. No need to… discuss much, but, I've opened, some PRs, like, implementing the… patterns to the URLs, your URLs.
to the HTTP instrumentation, but we're… we're missing it.
And… yeah, no hurry, but if you have time, you can take a look.
Please do.
Thanks.
**Hector Hernandez** 49:48 Yeah, one quick question. Sorry, I joined late. Looks like we're ready to start merging the lock stabilization PRs. Is that correct? I'm happy to merge the latest.
Is there any process that we want to follow?
Or I just can just update the PRs and ping you guys.
**Riccardo Magliocchetti** 50:11 I think we maybe want to decide which one to merge first.
**Hector Hernandez** 50:16 If you ask me, I will grab the… The first one, 46, 76, is the one with… more changes, basically. It's going to be harder to merge with the other one, so… If that's okay for everyone, we can start with that one.
**Riccardo Magliocchetti** 50:34 For me, sounds great.
**Hector Hernandez** 50:41 Awesome, thank you.
**Riccardo Magliocchetti** 50:50 Okay… So… well, plenty of topics for today.
Anyone want to discuss something else?
Otherwise, thank you, everyone.
And see you in the next Python 6 course.
**Hector Hernandez** 51:14 Thank you.
**aditya mehra (splunk)** 51:14 Bye.
**Aaron Abbott** 51:16 Good.
**Dylan Russell** 51:16 Yes.
