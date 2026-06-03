SIG: Arrow SIG
Date: 2026-06-02
Duration: 68 minutes
============================================================

## Zoom Recording Transcript

drewrelmas 00:00:44 Hey there, Aaron.
Aaron Marten 00:00:47 Ginger.
drewrelmas 00:00:48 Kennedy, Josh?
jmacdonald 00:01:00 Whoa.
Welcome to the meeting. I see everybody I know. Put your name in the notes.
And let's have topics that we want to talk about.
Listed.
drewrelmas 00:02:06 I do want to mention, Josh, that, thanks to Aaron and Tom, we've done a little bit of an overhaul of the issue triage, as well as a lot of the labeling.
So if you look at what's actually open in issues, there's only a few that should still have triage deciding, and… hopefully… That should work for you.
jmacdonald 00:02:39 Yeah.
drewrelmas 00:02:39 Oh, we actually are already back at 2 weeks ago, that's amazing. So everything else is… triaged.
Aaron Marten 00:02:48 There is also a tag, needs discussion, triage needs discussion, which is kind of meant for You know, things that we think rise to the level of discussion in this meeting.
drewrelmas 00:02:59 Do we have anything in needs discussion right now?
Aaron Marten 00:03:02 I think there's only one last time I checked a few minutes ago.
jmacdonald 00:03:07 Alright, what is it? Let's figure it out.
drewrelmas 00:03:12 It'll be a separate label.
Yeah.
jmacdonald 00:03:20 Aha.
That's pretty old.
surely we can discuss it?
drewrelmas 00:03:28 Do we have Albert?
jmacdonald 00:03:31 Don't see how.
drewrelmas 00:03:31 I actually don't.
jmacdonald 00:03:33 I'm sure Jake could represent this topic, since I know Jake was involved on the other side with Azure Auth for Cloud Object Store.
Jake Dern 00:03:46 Yeah, I'm sorry, what is the new, I remember this issue, from a while back.
jmacdonald 00:03:52 I mean, it's…
Jake Dern 00:03:53 The new.
jmacdonald 00:03:54 It's a year old at this point.
drewrelmas 00:03:56 Did Albert add… who added the needs discussion? Was it… Albert, Aaron?
You can scroll down to the bottom and check.
jmacdonald 00:04:04 Yesterday.
done.
Let's see, Tom, on the call, I think this may just be a reminder that this is an important issue. I believe GoCan would be sort of on track to help us with.
drewrelmas 00:04:19 With Austin.
jmacdonald 00:04:20 implementations for Cloud Auth.
That's kind of one of the examples that we have.
Don't see him here on the call either.
But… Otherwise, I don't think we tremendously need to discuss that. We just kind of are aware that we want to have Azure and other cloud storage extensions available, or per K.
drewrelmas 00:04:44 Sure.
With that in mind, does that mean we're not doing issue triage at all? We have nothing in the last two weeks that…
jmacdonald 00:04:53 It sort of seems that way, yes, Drew.
I did look over what's here, I don't see any, I guess… I don't know how we decided to remove those labels, but, you know, one that might be a little controversial or want discussion was maybe discussed last week, so I wasn't… and I had to miss last week's, so… Kdl…
drewrelmas 00:05:19 We talked about it briefly, but more in the motivation of what needs to happen. You're talking about the… release it in GitHub.
jmacdonald 00:05:26 Yeah.
drewrelmas 00:05:27 Yeah.
We didn't so much talk about that, we mainly talked about it In the context of we need to get the Rust change log up and running, and being able to say we're git tag versioning, OTAP data flow, which we are hopefully doing, as we speak, because we have the first prepare, release, PR out with automation that would turn OTAP data flow into something versioned, along with the Go stuff in our repo.
But we didn't really dig into… the outcome of… publishing… the image.
jmacdonald 00:06:14 Yes. Well, I'm aware, at least for the reason I filed the issue, of an interest in both having Docker container images as well as actually Debian D package images would be great.
Otherwise, it does seem like we have no great issues to discuss, meaning discussion, and I guess that means while everyone adds their name to the list on the notes, we can move on to your topic, Drew.
drewrelmas 00:06:41 Sure.
So, I will go ahead and share my screen, if that's okay.
Let me know when… That's coming through, looks like we're good.
Can you… I'll confirm you can see?
jmacdonald 00:07:09 Yes.
drewrelmas 00:07:10 Yes, okay, cool. So, I want to talk about, an issue that I've been working on with respect to… a concept in the repo called flow metrics, which I'm using as a way to essentially, in Joshua's words, which I very like, represent virtual nodes, meaning I might have a set of processors that combined do a certain logical action, but I only want self-telemetry From the beginning of that work to the end of that work, tracking things like incoming, outgoing, and duration.
So, in that, I have a use case where I wanted to use the OTOMetrics SDK Views concept to filter To produce metric streams outgoing.
based on these flows, and I wanted to do filtering with scope attributes, which is actually something opened A long time ago, or something completed a long time ago, if I search for… scope.
attributes… This right here. So, we had an issue a while ago that said, hey, in our views, we should be able to.
filter based on scope attributes. No huge contention there.
However, as I started to dig into actually making use of that feature, I noted… A problem that I've documented in this issue 3161 right here, which is that In our current internal metrics, implementation for metrics.
Every single attribute, including the ones that should be resource level and scope level, were actually showing up as metric data point attributes.
I have proved this by setting up a really basic pipeline that had a couple of custom resource attributes, and then a… just for fun, like, we exposed the Prometheus one through the admin API by default, but I also added a console metrics reader.
Through Prometheus, what you can see here is that the user-provided resource values did show up in Target Info like they're supposed to.
But, the other ones, like, where am I going? Process instance ID, host ID. These we have in the code set up as resource attributes, so I was surprised to see them showing up here.
In addition to that.
Things like pipeline group and core ID, which I thought were scope level, also showed up here, not prefixed by OTEL underscore scope.
Again, if you inspect the console output, you can see exactly what I talked about. Resource only has the user-provided ones.
And everything else… showed up under… oh, it looks like it got cut off. Everything else showed up under… Data point attributes, and scope had nothing. There were no scope attributes.
So, through all this, I talked offline with a few people, and I do actually have a PR out that should, resolve this problem. It's gotten a cursory look by CJO and Alit.
And the result, again, to contrast, is… When I run the Prometheus, I can see both the user-provided resource attributes, as well as the ones injected by the engine.
And all of the scope attributes, core ID, pipeline ID, etc, are prefixed with OTEL scope, like they should be.
And if I look at the OTLP export in console, I can see all the four things on resource, and the scope attributes I would expect sitting under scope.
This did have one interesting follow-up, which I thought would be fun to talk about in, the SIG meeting, which was… CJO actually didn't like that there's a couple of… resource attributes that we're auto-injecting from the engine level, we probably want to allow some level of customization on this. In addition, the ones that we support right now, which I think are host ID, among others, these are really only Linux only, and also, we're publishing host ID, but actually, the value we're using would more likely be classified as host.name, so there's already something a little incorrect in what we're doing.
So I did raise this as a separate follow-up issue. I see, Aaron, you marked it as accepted a little bit ago, but I think this is a good, you know, this brings us closer to OTEL semantic convention, if we allowed, a little bit more configuration of this.
Really, that was all. I just wanted to raise awareness of the metrics thing. This is definitely classified. The last thing before I call on Steve, Joe, is this is a and it is marked as such in the changelog, this is a breaking change, for sure, because we're moving where a lot of attributes are around. So if anyone downstream is depending on these sorts of attributes, for example, our perf tests were, it's gonna require a bit of a change. But… This is definitely moving in the right direction, so it's not something we should put off.
Cj, you want to say anything?
Cijo Thomas (Microsoft) 00:12:59 Yeah, I mean, just want to say, like, I agree with the change, that's one thing, and I want to spend one second on the… hostady thing, because my topic, which I put at the very last, is also related to that.
This is something which we intend to solve, like, an entire, engine and entire repo level. Every telemetry we produce should be backed by a… semantic invention, and we'll use our favorite tool, Weaver, to ensure we are producing them. So I… I think George just merged the PR, where we are using Beaver LifeCheck.
Early today, it only does, like, events. I'm actually working on metrics as well.
So everything we produce will be checked against the published semantic conventions from either Open Elementary, or for things which are our own, we'll publish it ourselves, so it'll be validated. So, we should be able to catch such issues.
Yeah, so my only thing, topic which I added to the agenda, which is at the last, now we can't skip that, because I just wanted to raise awareness that we are working on adding viewer checks for these things. Step one is done, I'm booking on. Step 2, there is an open PR where… We are getting a… new version of Weaver, which has more capabilities to help with the validation. So that's the PR which I wanted to draw attention to, but since we were in that topic, I just read it here.
drewrelmas 00:14:23 I thought I had a link… I should have had that open. I remember looking at the hotel website where it talked about host.id and host.name. I'll include a link to that on this issue.
Cijo Thomas (Microsoft) 00:14:34 Yeah, that's awesome, yeah. And, like, my other topic is done, so we can now remove it from the agenda.
drewrelmas 00:14:41 Okay, that was all I wanted to say. Does anyone else have… Josh, do you want to say something?
jmacdonald 00:14:47 Yeah, just a little bit of a conversation, maybe, for everyone's benefit. I think the way you're encoding the scope attributes, just to be clear, I think that travels from the point of instrumentation To the point where the dispatcher makes OTEL SDK API calls.
So it's essentially just a convention used within our internal SDK, or our ITS, effectively, for our hotel… using the hotel metrics SDK. I wanted to say that because if someone saw… and the Prometheus view that you showed us in the… in the text of the description is also using our kind of ad hoc Prometheus exporter. Yes.
drewrelmas 00:15:31 I had to prefix… yeah, I had to run the prefix on everything from… with HotelScope.
jmacdonald 00:15:37 Yeah, that made me feel a little bit kind of uneasy, just adding, like, 10 bytes or almost, you know, 9 bytes or so to every attribute, but it's okay. The reason I'm saying this is that I think what a real… a sort of on-spec Prometheus exporter would do in this case might be pretty different, and it would involve having a hotel scope info section, so that's a metric, it's an info metric that has some sort of correlating identifier, which is the tricky part, and then it has hotel scope name and version, and then you don't have to put every attribute on every metric line then, you just need those correlating identifiers.
But…
drewrelmas 00:16:20 So it behaves more like the OTLP exporter in terms of avoiding the duplication of scope.
jmacdonald 00:16:29 Yes.
and it's on… it's sort of, like, accepted by the open metrics slash Prometheus community for that. I like the model, actually. It's a one-valued metric, so you're saying, you know, if you wanted to do a join in sort of some logical sense, you could just join the target info.
sorry, scope info. So it's identical to the target info, but it's for the scope. And you need, you know.
OpenTelemetry has never given us a specification for how to do scope attributes completely. It's in the protocol, so we can do what we want here. But, effectively, they don't… we don't say how to create a unique identifier for your scopes.
drewrelmas 00:17:10 I see. Well, regardless, I will say, I think that's… you know, I'd like to get this behavior fix in first, because it affects a lot more, and then we could revisit what the Prometheus implementation we use is.
jmacdonald 00:17:26 Yeah, I don't.
drewrelmas 00:17:27 At the very least.
jmacdonald 00:17:28 Hotel SDK, if you turned on their exporter, in theory, you'll get something, and I don't know how they handle that uniqueness.
Cijo Thomas (Microsoft) 00:17:35 Josh, the OpenTelemetry Rust Prometheus exporter may not be spec compliant. We have an open PR from Fox to fix that, because the spec for hotel 2 Prometheus mapping, it's being merged as or marked as stable as we speak. It's, like, literally being marked as stable. So Rust hasn't caught up. Arthur has some PR to fix that in the Rust SDK. But if you're following the same spec, whether we… whether it's our own admin premise.
or the hotel one, the output should be exactly the same, like, I mean, the order may be different, but it should be following the exact same spec.
jmacdonald 00:18:15 Yeah, that was more of an FYI, so thank you.
Cijo Thomas (Microsoft) 00:18:17 Yeah, Yeah, one thing, Drew, do we plan to offer any ability Promote some of the resource attributes to data points, because I believe Promise generally has such capabilities. I forgot, like, maybe, Josh, you can help me out. Is that something we offer in the Prometheus Exporter, or when Prometheus scrapes it, it knows how to… convert it. I actually forgot, like, maybe, like, that's one thing we should offer, but irrespective, it's not to be part of this PR, we can definitely follow up.
jmacdonald 00:18:53 Good question. I don't actually… That confuses me a little bit.
Cijo Thomas (Microsoft) 00:18:58 There's.
drewrelmas 00:18:58 a lot of resources over the years.
jmacdonald 00:19:02 Cops.
Cijo Thomas (Microsoft) 00:19:03 Okay, now I remember, like, no, what I meant to say was, like, Prometheus natively understands OTLP, so we don't really need it to scrape. So when we send it via OTLP to the actual Prometheus product, it has a setting to convert some of the resource attributes into metric point attributes.
drewrelmas 00:19:20 Oh, okay.
Cijo Thomas (Microsoft) 00:19:21 So, when scraping, it already knows how to do that, because we already convert that into target info, and they get stored, like, different. Okay, so you can ignore what I just said now.
drewrelmas 00:19:33 Thank you.
Cijo Thomas (Microsoft) 00:19:33 If this change is good, I'll start reviewing more closely, but direction-wise, yeah, this is pretty good.
drewrelmas 00:19:39 Okay, great. Barant, just because I see you also joined late, I don't know if you have any thoughts on this, or if you'd like us to just move on to the next topic.
Laurent Querel 00:19:48 Glad, sorry to be late, So, we are talking there about the… moving attributes to the scope attributes, right?
drewrelmas 00:19:59 And resource, yes.
Laurent Querel 00:20:01 Yeah, okay, yeah, makes sense for me, and totally aligned with, The telemetry documentation that we created a few months ago.
Where, I was basically advocating for an entity-based internal telemetry system.
Where we clearly identify entities by their attributes.
And for matrix, it's more or less a one-to-one, or… resource plus scope, attribute to a corresponding entity. So, yeah.
drewrelmas 00:20:34 Yeah. Okay. I don't think we need to spend much more time on this topic, the PR is out there, but thanks all for listening.
jmacdonald 00:20:43 Great. Alright, I've been taking notes, and welcome, Laurent. Let's see. On the… on the agenda next, we have an item from Kennedy.
And if you're here… I invite you to speak.
kennedybushnell 00:20:59 Yeah, I'm here, thanks. So we talked about the file log receiver… maybe 2 weeks ago?
And it looks like there's been some progress in the issue.
For, for design, some comments made there.
I've been talking to somebody internally named Ashwarya. She came a couple of weeks ago as well, and she's really eager to start contributing.
And has some capacity, so wanted to figure out, what we can do to really enable that.
She has not been involved in this project, and she's not in our direct team, just for some context for the non-Microsoft people here.
So she's hoping that we can kind of break the… like, kind of give her a chunk, like, a really chewable chunk of work to do, and was hoping to kind of kick that off.
Laurent Querel 00:21:54 Fantastic news. Can you just remind me the name of this person? So if I see, him or her, I know that that's the right person.
kennedybushnell 00:22:06 Yeah, so her name's Ashwarya. I put it in the meeting notes as well.
Laurent Querel 00:22:11 Oh, okay.
kennedybushnell 00:22:12 I'm not sure what her GitHub Handle is… yet.
But that's the name, yeah.
Laurent Querel 00:22:20 Okay, okay. Yeah, so, I didn't look at the recent, comments in the file log receiver, but I think the first thing we need to do is, Making sure that we… We take into account those comments, and we make some decision on what makes sense, what does not make sense.
And we, and like you said, once we have this updated version of the GitHub issue, then we can create sub-GitHub issues to split the work.
I… if I remember well, because I put that a few weeks ago, I think the idea was… First splitting the discovery from the… the effective, by scrapper.
of FideReader.
So the discovery part was based on… The extension mechanism.
So I don't know if, Gokuan is there today.
Because, if that's the case, I will have a question for him. No, he's not there. Maybe, Josh or, anyone in the Microsoft team, maybe you know, I think to achieve properly the discovery part of the final receiver, We need, A pipeline-level extension mechanism, as opposed to… Let me think about it once they bond.
Yeah, I think a pipeline level.
So, what is the status of the extension mechanism today? That will be the first question. Are we able to achieve the discovery implementation, so basically, we… we specify the… The directories, the files that we want to, to scrap, to… to read.
On which we want to apply rotation, and so on.
And basically, this extension will discover dynamically those files, because obviously they can appear. We could specify some word cards and, automatically discovering new files.
And… and then the extension will be there to… basically distribute, the discovered file To the available, receiver instances, because the difficulty that we… it's both a difficulty and also an advantage.
We have to find a way to distribute, basically, the… the discovered file to individual File log receiver instances, which will do the real work of reading the file, Reading the frames, so that basically a frame in this, space will be either A single line separated by… A line feed, or carriage return.
And, but that could be sometimes a different format, which is, I don't know, whatever is the separator or the mechanism to frame the individual login tree.
And, so this extension will distribute the load over multiple pipe log receiver instances.
And then, we can imagine that we have a third, a third GitHub issue that we'll talk about, decoding and parsing the… Those slogan trees.
So… at the minimum, I see 3… GitHub issue, I'm sure that we can speed that, even further.
I can probably sell sometime by the end of the week.
To… to propose something there, and I can, include you, Kennedy, and any other one that is interested by that?
So I can get your feedback, and probably also get some additional, ideas.
jmacdonald 00:26:51 That sounds good. Sounds like we might want to have Gokan and Aishwarya start working on the discovery implementation and the discovery interface for the extension, but…
Laurent Querel 00:27:03 Yeah.
jmacdonald 00:27:03 we would appreciate your help with, forming issues if you want to work on that, and we can also just do triage and start creating sub-issues. I will take notes on the three things you just mentioned.
Laurent Querel 00:27:13 I think the, this effort will be also a pattern that most likely will, Will appear, in, in other, situations.
the fiber receiver, I don't think is, is, I mean… it's not a network-oriented receiver, where we can rely on things like the SLU support. So every receiver, similar to something where the resource is Could not easily be shared, and where we need to distribute the load with some kind of coordination.
we'll have to follow what we will implement. So, doing that properly and well designed.
Will, will be, fundamental for the future, equivalent receivers.
And I think we need also to take into consideration D1.
The fact that we want to support properly shut down and live reconfiguration, including for this kind of receiver.
And that obviously complexifies a little bit, but at the same time, having the… this ability to… Manage the logic of distributing the… the… the work.
Make also, Probably will simplify the live reconfiguration effort.
So it's… it's a little bit of complexity, additional complexity, but at the same time, I think that will also simplify Our ability to support properly the level configuration in the future.
jmacdonald 00:29:06 All right, well, I do know how to reach out to Aishwarya, as well as to Gokan about this topic, so I can also try to get them started, Kennedy.
kennedybushnell 00:29:14 That sounds great.
jmacdonald 00:29:17 Cool. All right, well, so I projected.
Laurent Querel 00:29:19 Maybe you can, add, their, GitHub, at least for the… the… Pogo can I know, but for, sorry for the conversation.
jmacdonald 00:29:29 I swore ya.
Laurent Querel 00:29:30 I'm not sure. So if you can, add, maybe in the comments, the GitHub, handle, that would be nice.
jmacdonald 00:29:44 Got it. I'll work on that.
Okay, and we covered CJO's issue, that he wanted to talk about already, associated with the conventions topic from Drew.
So, more or less just to say that we have a Weaver LiveCheck PR that I think has merged, right?
With conventions and everything.
Laurent Querel 00:30:07 That's great.
jmacdonald 00:30:08 Yeah.
Laurent Querel 00:30:10 Super happy with that.
jmacdonald 00:30:13 For myself, I just wanted to say I've kind of, was a little bit offline for the last month with some travel and so on. I'm back. I also have some work that I've dedicated myself to for the Go Collector, so I'm going to be working on batch processing, standardization there, as well as just kind of helping with some release velocity.
Or the collector. And while I was looking at the repository to come back up to speed for us, I noticed how many open PRs we have, and I don't like looking at open PRs.
So, I thought we could… we could, maybe just briefly chat about this in case anyone else, wants to. And, you know, like, it's pretty… the top of this page is usually pretty straightforward. Like, a lot of new stuff lands every day, some of it's depend to bought or renovate.
And some of it's just kind of merging really quickly. Like, we all know how to review the top of this page, but then when you look at the bottom, you know, it starts being, you know, more than a couple weeks old, even. And, The problem that I'm noticing is that we have a lot of legitimate interest from real people who are first-time contributors, but it's a pretty mixed bag of what we're getting from… in terms of the work.
And it sort of overwhelms me to look at it, and I hope you, I don't know if anyone else is feeling that way, but I just wanted to talk about, if anyone has thoughts, how we can manage, well, so many first-time contributors. Drew has his hand, thank you.
drewrelmas 00:31:42 One thing I'm thinking of, just because I was looking at the OpenTelemetry Collector and CollectorContrib repos the other day.
They're big into ownership areas of having parts of the repo actually assigned to people, so that might help You know, we've done a great job with, like, some of the auto-labeling, but part of what their workflow does is when a PR is opened, it will actually assign the PRs to relevant authors. So.
That's something we could attempt, that to kind of cut down on the number of reviews each individual is doing. However.
Those of us that are… You know, owners of the core repo pieces might not see much improvement like that.
jmacdonald 00:32:37 Yeah, and I know the mechanism in that collector repository is to use the metadata YAML file, where the owners are listed, and then someone… someone with a GitHub token has to run a command that fills in all the code owners, And they use this mechanism to make sure that code owners stay active, basically. It's pretty heavyweight, I'm sure we could do it, but I think what you just said, Drew, is true. We won't necessarily save load on the core set of us, who are reviewing… trying to review, like, most of it. What I've been thinking about is some way to, like.
Just kind of have a… have a… maybe an agent that could coach all the new PRs into, like.
proving that they are serious, proving that they are human, that they have read our style of… our contributing document, and have made an effort to understand how to work here. Because half of the… half of these PRs will not pass that bar, and I think users don't actually do want to help us and contribute.
True.
drewrelmas 00:33:40 One other thing I was gonna say is we can also encourage folks who aren't approvers or maintainers to also review PRs. So anyone on the call who doesn't have, like, an official name, like, it still helps everyone out a great deal if you take a look at other PRs that are open.
jmacdonald 00:34:03 Very good. And we might say, Drew, that right now is a good time, since there's time in the meeting, and nothing left on the agenda, to take a look at some of the big ones.
So… And I think what we should do is work backwards, so… If I go to, page 2 of the PR list.
There's some old ones that are marked draft, and I generally let things that are draft sit, but at least one of these is somebody who I think is, means well. And, the problem is, I couldn't quite read the PR very well, and at some level, it's hard to dedicate time to all these. So, And, the problem is, eventually, the person kind of maybe leaves, and then we end up with PRs that are hard to build, and I feel bad closing this, but I'm not sure it's helping anybody being open since a month ago.
But I did look at this person, they are real, you know what I mean?
And then, so that's the oldest one. If you have one of these.
drafts, and I am one of them.
you know, I think I should close this PR, and yet I'm still trying to find a sort of timeline and a schedule of work for the… what we think of as the internal telemetry system for metrics instrumentation in the data flow engine. I still want to do this work, it's just that I haven't found a way to get it moving.
Oh my gosh, this one has not merged yet.
looks like while it took it out of readiness, although I remember looking at it and thinking it was almost ready. This is an area where somebody helping us by reviewing the work would really help. So if anyone who wants to review this, 2788, please do.
And then, CJO, if you feel like you want help with any of these PRs, I'd still like to see us handle OS signals correctly, so I like to leave them open if they look like.
Cijo Thomas (Microsoft) 00:35:59 Yeah, I mean, they are, draft because I haven't solved, like, some edge cases, I'm still working on it. You can see, like, I'm pushing commits once every week when I get to it, but yeah, it's still… it's not abandoned, it's just draft because I don't want anyone to review it until I finish, it's.
Laurent Querel 00:36:17 It's.
Cijo Thomas (Microsoft) 00:36:18 abandoned.
And I hate that.
Laurent Querel 00:36:20 community.
Cijo Thomas (Microsoft) 00:36:21 issues, yeah.
Laurent Querel 00:36:22 Yeah, same thing for me, for example, the 2472.
It's still something I need… I like to finish, but Along the way, we had, additional priorities, and the system is working good enough. Even if, fundamentally the 24-72, I think, will be nice to have.
Oh, no, even this one is a cleanup, so yeah, that will be nice to have, but it's not fundamental.
It's just a matter of time for me to finalize the work. Right.
jmacdonald 00:36:58 Actually, any of us could do this as well, it's just a cleanup, thank you.
I… just kind of working backwards, we've got one from a contributor who, You know, this is Max on the call. Hi, Max.
I want to support Max, and…
Laurent Querel 00:37:19 No.
jmacdonald 00:37:20 It's in draft mode, so I… usually when something is draft, I let it sit. But we're watching, and thank you very much, Max. Appreciate having you here.
This stuff work… oh, Max, please.
MAX JACINTO MESTANZA 00:37:34 Yeah, just to clear up, I was working on that PR for, like, a month or so ago, I just have the time to go back to it. It's pretty much to, you know, improve the handling for shutdown cases.
Albert was really kind and left some comments there, some I am addressing right now. The main things missing would be, like, the, you know, the special test for the case of… In case there are the shutdowns, so… Hopefully, I'll get that done in 2 days or so? So, yeah, once it's done, it should be, you know, not a draft anymore.
And then it will be ready for the proper review.
jmacdonald 00:38:15 Thank you, Max.
It's great that you came to talk about it. We definitely know you're real.
And I've been keeping my eye on this one. I'm glad that we were able to talk about it.
Okay, we've got a few more in this category. I know the STEF work was kind of, kind of an experiment to show that we could. I was glad to see it, but… Yeah.
Laurent Querel 00:38:40 Again, that's something I'd like to finish, but I didn't… I didn't have the… I don't think it's… necessarily super urgent.
And I need that to… to do some tests, and to let also Jake, do… running some tests.
So, most likely that we'll stay there for a few weeks more, but, Is it really a product? I don't know.
jmacdonald 00:39:07 No, it's not a problem. Mostly I wanted to look at what I think of as kind of just an overload scenario, where we've got first-time contributor here, and then here, and here, and… four of them right now. And, nothing wrong with first-time contributors, but it's creating a lot of uncertainty around review work, because they tend to be… everything is difficult to review here, in my opinion.
So I just wanted to say that I'm kind of thinking about if anyone has great ideas for how we could improve this for everybody, I'd love to hear it. And Drew has his hand up.
drewrelmas 00:39:40 One that just caught my eye, if we have a second to talk about it, was CJO's draft about PR size labeling, which kind of relates to our PR velocity topic.
So, this was, I think we had an ad hoc discussion, or maybe I left a comment.
Cijo Thomas (Microsoft) 00:40:01 You left tick on that.
drewrelmas 00:40:02 somewhere about, hey, maybe we should find a way to encourage, smaller PRs, and… This was one idea, and I'm very curious if people on the call are supportive of this, or think it's not really going to help us.
Cijo Thomas (Microsoft) 00:40:20 I think it's something we can try out for a few days and see if it helps. The only challenge I had was it's not a… well-known.
GitHub Action, it's… it's not… super popular, but I would assume that these kind of things do not have, like, 10,000 stars or something, but it's still… okay to try it out for a few days, and if it helps or not, then it's not a big deal to remove it, it's just a simple workflow, so we can remove it if we don't think. I cannot remember why, what was the thing which I… which led me to keep it draft.
maybe I wanted to check the, the GitHub actions, because there are so many security issues being reported, so I wanted to… triple check the work… the workflow we are using, the GitHub action we are using.
But anyway, I'll take a look and mark it ready for review, but if anyone has opinions.
Please feel free to, like, use this time to share.
Laurent Querel 00:41:21 So, CBO, the… if I understand well, it's… it's a labeler, so… We don't block anything, it's more like an incentive, if you, if you are not, if you are an XXL,
Cijo Thomas (Microsoft) 00:41:38 Yeah, I mean, it can be… it's just like a sizer right now, it just determines the size and adds a label, but it also posts a comment, if it's, like, too big.
Post a comment saying that, hey, this is a big one. And we can do… we can do some rules, like.
For example, we can give some exemptions to the maintainers if you want to do a big PR, but if it's, not, then we can probably… Close the PR with a very soft, general message.
We'll need to do something pretty sure, because I'm seeing, like, everywhere across OpenTelemetry, there are a flood of TRs.
And some reports are going very extreme. They're, like, simply closing. I, myself, faced That from semantic conventions, when I open PR, and it immediately says, this is not an active area, so we'll just close it. So, we don't want to do, like, very extreme things, but maybe this is a very soft way of, letting people know, okay, this is too big of a PR, can you split?
Laurent Querel 00:42:38 Yeah, personally, the incentive… incentive is okay. For me, the… the… automatically close PR because they are too big, I'm not sure.
Cijo Thomas (Microsoft) 00:42:49 Yeah, that's why I don't want to do that, yeah. This is just, like, a minimal, gentle, comment on the PR itself. It doesn't do anything.
Laurent Querel 00:42:59 Especially because we are still, and that's something we, We didn't discuss that during this meeting, that's my fault, because I didn't add 18 to the… the list of topics. But, we, we, for people that are not aware of that, we, we are, working… when I say we, it's, the, the maintainer, working on a blog post.
Regarding the Phase 2 of this project.
And, we are also announcing… The Phase 3?
And, one goal of the first three is to stabilize, also, a lot of, things into this project. So I think until we stabilize, APIs, everything.
a lot of things. I expect to see still a lot of activities.
And sometimes when we are at this stage, It's…
jmacdonald 00:43:55 Thank you.
Laurent Querel 00:43:55 taking much more time to split, a PR in many, And it's also more complex for the reviewer not seeing the global picture sometimes. I'm not advocating for big PR, but I'm saying that depending on where you are into the maturity of your project, it's more or less realistic.
Cijo Thomas (Microsoft) 00:44:16 That's why we put such guidance already in the contributing guide. We don't blindly say no to big PRs, we just say that if it's not possible to split, just describe why in the PR description. So, so if you do follow that, that's quite fine. Like, if there is a concrete reason why we want to keep it big, that's fine.
Yeah, anyway, I'll work on it offline and come back. It looks like Nicole had his hands up, but…
Nikhil Manchanda (SlickNik) 00:44:40 Yeah, no, I was just plus one on it. I think the folks that you mentioned, at least in the data gathering phase, like, having this as a data point would be super useful, right? Like, even when in terms of we were going over the PRs and looking at which ones sort of needed review and so on. I think being able to just have that data point in, like, it is the larger PRs that tend to get stale, or what is the velocity of, like, the different sizes, or maybe there's some improvements there. I think, like, gathering data and having some more data around this is going to be good, and Just in terms of, like, understanding how well we're doing with the reviews as well, so I'm definitely for it.
Cijo Thomas (Microsoft) 00:45:25 Okay, thanks.
jmacdonald 00:45:26 Yeah, thanks, Mikhail.
Cijo Thomas (Microsoft) 00:45:28 Josh, I didn't… oh, sorry.
jmacdonald 00:45:30 I feel like we might need bigger size categories, though, like, 500 lines is barely a test sometimes.
Cijo Thomas (Microsoft) 00:45:37 Yeah, it's customizable, so we can…
drewrelmas 00:45:39 Rust format or likes, new lines, I don't know.
jmacdonald 00:45:43 Yeah, multiply by 10. Maybe. Ukarsh.
Cijo Thomas (Microsoft) 00:45:53 Not able to hear.
Laurent Querel 00:45:55 Yeah, we can hear you.
With cash?
Utkarsh 00:46:02 Could we consider, like, going forward… Oh, yeah.
would we consider going more aggressive on the stale workflow? Like, currently it's… We closed the PRs after 30 days of inactivity. I think, if we could… Maybe just have a more aggressive.
threshold, like, 10 days or maybe 14 days, then at least people who are not actively working on their PS, once they have the time to work on it, they can always reopen it.
And… That way, at least, we don't see so many open VRs when we go to the pull request tabs tab.
drewrelmas 00:46:37 Yeah, I think that's a reasonable step.
jmacdonald 00:46:41 Yeah, I agree. I remember my own PRs that I've closed and want to reopen, so I think most people can do that as well.
All right, well, that was my item on the agenda. Thank you all.
Cijo Thomas (Microsoft) 00:46:55 Hey, George asks, if you don't have any other topic, can I steal some time for, some discussion? Yeah, this is about, Something we started discussing a week ago, about how do we want to move our metrics generation macros to use. We were… And I did look at Viva. Viva does not have that capability yet, and I don't see anything in the, like, maybe it's in the long-term roadmap.
Since Laurent is also a Weaver maintainer, I want to see, like, whether we are… like, ready to start defining semantic conventions ourselves, and let Beaver generate the… Macros for us, or, like, if that's going to take much longer time.
Then what is the best way to… define our own metrics and semantic dimension, because if I… I was trying to do a viewer check for matrix, just like I did for events, and for metrics, the challenge is we define our metrics using, like, custom Rust code with a special annotation saying, this is my metric.
But the semantic conventions would be, like, a YAML file, and these two are disconnected. How do we… I mean, we can do some CI checks to ensure they are always in sync and failing the PRs and all.
But are there any better ideas to… really start from the schema and have the schema get converted into code using Weaver, and if Weaver is not doing it.
What's the best alternative for now?
Laurent Querel 00:48:27 So, just want to make sure I understand the challenge, because for me.
The only challenge I'm aware of in using… However, for our project is the fact that in semantic convention, the concept of metric set does not exist.
But those are wise…
Cijo Thomas (Microsoft) 00:48:49 No, no, no, no, that's not the challenge we have, yeah, because the.
Laurent Querel 00:48:52 But which one?
Cijo Thomas (Microsoft) 00:48:53 Yeah, we can define semantic conventions in our own report. We don't have to rely on the semantic conventions. We just need to be pointed to a valid semantic conventions file.
So the challenge which I see is we define the semantic conventions using EAML, the metric name, attributes, description, and then the code which is used to emit those metrics, it comes from the Telemetry macros, create which we.
Laurent Querel 00:49:17 Yes, yeah, yeah.
Cijo Thomas (Microsoft) 00:49:18 They're not, like, auto-generated, like, one, you create the YAML by hand, and then you also create the code by hand. There is nothing automatically generating the code from the YAML file. They believe the plan for us is to use Weaver to look at the semantic elements in this video.
Laurent Querel 00:49:35 So, yeah, so I understand all of that.
what I'm seeing is… there is nothing preventing, I think, in theory, to do that with Weir today.
The only thing that will be a little bit difficult is the fact that the concept of metric set does not exist in semantic convention. When I say semantic convention format, I should say.
So we have to rely on something like an annotation, or… So there is the concept of annotation supported by Weaver.
Where we could say, oh, this metric and this metric, this metric, belong to the same metric set.
once we have this ID, that will make the… the link or the relationship between multiple metrics defined by those, YAML files.
Then we can generate the code that is basically what the macro system is generating.
Cijo Thomas (Microsoft) 00:50:34 Okay.
Laurent Querel 00:50:35 And then we have, a crate.
that is generated by Weaver, that will, basically be, like, a materialization or an instantiation of what the macrosystem is doing today. And then the semantic convention file, the custom registry that will be attached to our project, will be the source of truth.
And then we… we would add… a kind of client SDK based on our own way of, Exactly like we have today. We have a set of, we have an API that we can use to report metrics directly into the values component, receiver, processor, exporters.
And, they are basically behind the scenes using, an MPSC Channel, and we can do the… we can reuse exactly the same concept, the same concept of snapshot, with the same concept of registration at the beginning to declare the values attributes.
there is currently no… obviously, there is nothing like that in the standard generated code from Weaver. But because Weaver is an extensible system, we can, in fact, use the Jinja templates to simulate or to mimic what the micro is doing. It's a little bit of work, but it's definitively not impossible, in my opinion.
Cijo Thomas (Microsoft) 00:52:12 Got it. And Josh, have you done this exploration already in your general metrics pipeline?
jmacdonald 00:52:17 So actually, yes, I was gonna bring this up. I put a link, and I can open the, that's the draft that I was just talking about a minute ago.
I had put together a draft roughly covering both of the topics that you both described. So, proposing a markdown format for YAML to… or a YAML format for schemas of a metric set, which, again, is a non-standard format that Weber doesn't really have.
And mainly what I was trying to do was get to where we could have a metric level that would determine, at runtime, the dimensional characteristics of your SDK. So, like, do you want to have a signal attribute or not? And, because my goal, I think, that I think we should have is that we move away from having, like, individual counters have separate individual metrics when they're part of a group or part of a set. So if you have a counter that's consumed success, consumed failed, and consumed refused today, what I'm hoping is that we move towards consumed with an outcome attribute that says success, failed, or refused. But that's a breaking change, and that's a Semantic Convention migration to me. So what I was hoping to do was to, first of all, get to where we have this Semantic Convention Format for metric sets, and then get to where it would also include metric level detail, but then to get to where we can actually configure at runtime which semantic convention we want.
Which, I mean, this is actually very timely. The hotel spec sig has been talking about how do we change semantic conventions of stable but very… but variable instrumentation, libraries.
So I was getting to that here at the end, basically saying, we should be able to say, configure the engine telemetry scope, and for this particular instrumentation scope, please use a new URL, which will be somewhere in your markdown, or your YAML file. Now I've said a lot. Please, Laurent.
Laurent Querel 00:54:18 Yeah, there are things where I disagree there, but I think, in general, I agree. But saying that we want to split metric set is, in my opinion, the wrong direction.
That's the exact opposite we've.
jmacdonald 00:54:33 Oh, I did not mean to imply that we should…
Laurent Querel 00:54:35 Oh, okay.
jmacdonald 00:54:35 what metric set. In fact, I was just trying to make a… to switch from having macros generate that code to having a code.
Laurent Querel 00:54:41 Oh, okay, okay, okay, okay, okay.
Cijo Thomas (Microsoft) 00:54:43 Oh, joke.
jmacdonald 00:54:44 Yeah.
Laurent Querel 00:54:45 That definitively, I totally align with that. And so, what you also shown into your document was two types of attributes.
The, the attributes that are… Statically defined… not statically defined, but, At the beginning of the life cycle of an entity, it's defined, and set forever.
And, and you have, attributes that are… That should be only a new-oriented attribute, so where the cardinality is well-defined, at least for matrix.
That could represent state, or like you said, you have different, type of outcome.
And that could be an attribute that we provide in addition to The fact that we increment on contour, or we set a specific gauge.
And that today is not supported well.
And for this type of attribute, and for the metric set presentation into semantic convention.
what I tried to do, with the… the Weaver Group and the Semantic Convention people.
I said, okay, are you open to, to discuss about metric set, and the answer I got was, yes, but please go and create a full specification to be honest, I think it's… it's way too much work for now, at least for me. And I was looking more for an intermediary step, where we rely on the extension mechanism that we already support in semantic convention, the annotation system that I said before.
And… and where we use this… because annotation can be applied to metrics, can be applied to attributes.
Basically, can be applied even to groups.
So… We… and they are very flexible and visible inside the weaver, a template engine, which is based on the Mini Jinja, the Jinja template system. So, we should be able to leverage that And that will be, I think, a good, a good, a good example of a metric set and how it's, we put that in place into… in place into a realistic project.
And and then, once we have that in place, The migration… the migration from… This, let's say, ad hoc concept.
put on top of annotation and migrate it at some point into a first citizen concept. I don't think that will be super painful. We could mechanically move the annotation to whatever will be the format, this ID, that's, at some point. But we will have a proof of concept At scale, that will work.
And, I think based on, at least on my side, my own priorities, my own priorities is to make this project on which we are working ready as soon as possible. It's not to create another round of semantic convention, because I know that that will take 6 months, sometimes more, and I'm not ready to put this effort and to wait 6 months to have that.
Cijo Thomas (Microsoft) 00:58:20 Blue.
Laurent Querel 00:58:24 You are muted, Josh.
jmacdonald 00:58:26 All right. It sounds like you agree that we could do this ourselves by defining our own schema YAML format for a metric set, just to get exactly what we need.
Laurent Querel 00:58:35 What I'm saying is we need to… I will prefer to use the semantic convention format.
And use the annotation mechanism.
To extend what is missing.
I'm not advocating for another new format, because then that will be even… I mean.
If we do that, we can't use Weaver, and if we do that, that will be super hard for us to explain to the rest of the semantic collection community that, yeah.
jmacdonald 00:59:03 And to be clear, that's sort of what I was hoping to do, was to extend this format with… here, for example, XOTAP labels. It's like, this is my own invention of… I want to have variable dimensions by level, and that's not part of a spec.
Laurent Querel 00:59:19 Yeah, I probably need to, to read more carefully that.
jmacdonald 00:59:23 Don't… please don't, it's draft. I'm gonna come back with this when it's ready.
It also drew…
Laurent Querel 00:59:28 Okay.
drewrelmas 00:59:29 I was just gonna… we kind of already covered it, I was just gonna make an interesting note that this kind of relates to the refactor I'm doing, because it's disallowing res… or sorry, it's making all metric attributes either resource or scope, whereas here we're talking about data point attributes. So, not… I mean, not directly related to my PR, but basically you would need an additional code change on our side to allow metric sets to declare data point attributes.
Cijo Thomas (Microsoft) 01:00:00 Yeah, because when we use Weaver to validate right now, if everything is on… scope attributes, I don't know if Weaver can even validate that, because I don't think any semantic conventions were different on scope attributes, so it's going to fail.
But anyway, like, let's attack that problem after we fix the current set of problems, and I can come back to Weaver for Matrix a few days later.
Laurent Querel 01:00:25 I think what we can do, but, we need to double check.
is to embrace the entity model.
So we can attach attributes to entities, and I think it's already supported by Weaver.
And then, we attach, entities to matrix.
And then because… and then we can decide, oh, by convention, in our project.
oftt attributes, attributes, sorry, or, scope attributes.
So the identification of which attributes need to be in the scope Will be derived from their inclusion into an entity.
And, I think at the end, that will make the… the modelization super nice, because we will have clear entities with their corresponding… with a name, with a description, so an entity in our case will be a pipeline, a node, a channel.
A controller, and so on.
With our questioning attributes. And then, we will have metrics which, will, define the OTT relationship.
So, multiple metrics will… oh!
I'm just, thinking out loud. I think we just figured out what… how we can model this entire thing properly.
Because if you, if you have, values, individual metrics.
That are, in fact, connected to the same entity.
You get the metric set, you can infer the metric set.
Because, obviously, the metric set are the metrics that belong to the same entity.
that's how we do the things securely in the project. So, I need to double-check, but I think we are very close… if it's… yeah, I think we are very close to have something that… Will not require too much, annotation.
to represent, entities, because they are already supported by Weaver.
And, derived metric set from those connections.
jmacdonald 01:02:38 This sounds good. I understood, and I want to note that we're on time, so we should probably, cut the conversation off. I personally would love to see CJ pick up all this work, but I'm going to talk with him about that offline.
The… what you just said about entities is absolutely correct. I put in the notes there that this is also what I was referring to about a correlation identifier between the metric And the scope, the hotel scope info, technically is supposed to use some sort of entity definition to correlate metrics with scopes, so you can have all the other attributes that are, you know, not necessarily needed to be repeated every time in your scope info.
Maybe that's a good place to end.
Thank you all.
Laurent Querel 01:03:19 And Sidro, I will be super happy if you work on that. Let me know if you… if you need to discuss that with me, I will be, I will try to be available also.
Cijo Thomas (Microsoft) 01:03:30 Yeah, okay, yeah, I'll start… I'll finish the events thing in a couple of days. I won't add all the events validation myself, I'll just do it for 3 or 4 events, and then create, like, help-wanted kind of thing, so more people can pick it up.
Yeah, I'll see what I can do for metrics in the meanwhile. Maybe I'll send you a draft later today, and we can discuss in the PR, yeah.
jmacdonald 01:03:51 Thank you.
Laurent Querel 01:03:55 Thank you, buddy.
Cijo Thomas (Microsoft) 01:03:55 Alright. Thanks, everyone. Bye.
kennedybushnell 01:03:57 Nope.
