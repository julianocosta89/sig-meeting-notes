SIG: Java SIG
Date: 2025-11-20
Duration: 55 minutes
Zoom Recording URL: https://zoom.us/rec/share/yCDxukn8vaO8g-NvLo0kxig3u_YWDmIiB4zLj5n7-IJf-VQMqU1XNeL9uXcMcAyZ.jZPiGjgEe-otleXy
============================================================

## Zoom Recording Transcript

**GZ Gregor Zeitlinger** 01:15 Hi, folks.
**Trask Stalnaker** 01:19 Hello!
**Peter Findeisen** 01:21 Hello?
**Jack Berg** 01:22 Bye.
**Trask Stalnaker** 02:27 Alright, well, we've got people and topics, so let's start.
Let's see, I think this maybe had carried… over from last week, and I know, Jack, that you have looked at it recently, so I don't know if there's really anything we need to discuss here.
Except… maybe the… Whether it should go straight into stable or not.
**Jack Berg** 02:59 Yeah, so… January 15th is obviously kind of close, and… I guess question for the instrumentation folks. Would you have to, would you have to provide instrumentation for this?
like you do other parts of the, the API to bridge them into the agent?
**Trask Stalnaker** 03:26 Do we bridge… I don't think we bridge extended attributes.
**GZ Gregor Zeitlinger** 03:32 We do.
**Trask Stalnaker** 03:34 Oh, we do.
**GZ Gregor Zeitlinger** 03:34 an OpenTelemetry API and instrumentation.
Basically, every method of the API An instrumental…
**Jack Berg** 03:48 That was just… that was just something I was thinking. Well, is it every method of the API? Because… No, not there.
**GZ Gregor Zeitlinger** 03:57 It's an instrumentation.
Okay.
**Jack Berg** 04:00 Yeah.
**Trask Stalnaker** 04:02 So many things called OpenTelemetry.
**GZ Gregor Zeitlinger** 04:04 That's true. Yeah, it is basically every.
**Trask Stalnaker** 04:08 Because of.
**GZ Gregor Zeitlinger** 04:11 Because of class loading issues.
**Trask Stalnaker** 04:14 I wouldn't… Do we, though?
You're sure that we're instrument… can you, maybe in the background, Gregor, find where we instrument extended attributes?
So… but to your question, Jack, we… I don't think we have to.
We have chosen in the past not to instrument certain things.
**Jack Berg** 04:47 So that would just mean that, like, you know, those APIs, until they, you know, are either instrumented or promoted into the stable API, and then instrumented, would, you know, a user recording using those APIs in their application for custom instrumentation would not see those attributes reflected in their telemetry?
And that doesn't…
**Trask Stalnaker** 05:08 I'm the agent.
**Jack Berg** 05:09 Right.
Right, and that doesn't seem like that big of a deal. I guess, like, I'm just trying to be a little bit conscientious of the agent folks, and not having to, like, you know, put you through the churn if it's unnecessary. But I don't have any issue landing this PR, and then in January doing a follow-up one to promote it.
**Trask Stalnaker** 05:33 Jason, would you…
**Jack Berg** 05:35 Switch…
**Trask Stalnaker** 05:36 Android, I think you all are using the extended attributes already.
**JP Jason Plumb** 05:41 I think we are… Yeah, we would switch.
Although we don't really have any use cases right now, I think there's probably some that will follow shortly after.
**Trask Stalnaker** 05:55 For spans or for event.
**JP Jason Plumb** 05:57 events.
**Trask Stalnaker** 06:06 Thank you, anonymous hyena.
Alright, so we do, yes.
Okay, my… I think my preference would be to merge it, just to be able to, because we want to push on getting it stabilized all in the spec.
Before Jan 15.
And, so this would kind of… showing that we have a… something out in the world would… be beneficial.
**Jack Berg** 06:48 Yeah, that sounds… that sounds fine.
And just… so I've taken, like.
I've looked at this Trask, but I haven't gone deep into, like, all the code paths to understand, like, the performance implications of it. So, like, when we promote it to stable, I'll probably, like, look at it more closely and really kind of stress test it. But, you know, I don't think it needs to be perfect right now.
It definitely works.
**Trask Stalnaker** 07:18 Cool. Also, we have, a couple weeks before the release.
**Jack Berg** 07:23 Yeah.
**Trask Stalnaker** 07:26 as I think would be my… just my wish list would be to get it in the next release.
**Jack Berg** 07:32 I think that's super reasonable.
**Trask Stalnaker** 07:36 Awesome. Let's move on, then. Jay Gregor.
**Jay DeLuca** 07:44 Yeah, so, Gregor and I were just talking last week, and we know that you guys, as maintainers, have a ton on your plates, especially around releases and other things, and so… Gregor and I, we, at least for us personally, we kind of try and identify areas that we think we can help and, understand what the various priorities are, but we were just wondering if there might be some other ways that would be useful for you guys as the maintainers to be able to… Communicate things that you would appreciate help with, or areas that you think are higher priority for others to contribute to.
Yeah, Gregor, I don't know if you have anything else to add there.
**GZ Gregor Zeitlinger** 08:28 Right, when I'm seeing all the PRs scrolling by the whole day, it's quite hard to see where, where it's, difficult for you, where I can take work off you, and where it just would take me more time to review, and so having a list of, a short list of PRs and issues is helpful, and Laurie has, given me a list, last week, because I asked how I can help in the, release, and I hope that helped. But, would be better if that was, for everyone to help, I guess.
**Trask Stalnaker** 09:11 So… Stability is on my… Top of my mind right now.
I… these are the… Areas that are highest priority for me that would be… Great to just, you know, Chip away at.
Some are more clear than others. This one, I think, is pretty much done now.
we have… We just merged in after this last… yesterday's release.
the, removing some deprecated methods. The next thing here is… oh, this didn't come in with links. Let's try pasting that in. Oh, wow, that didn't work at all.
**Jay DeLuca** 10:12 If you do the… there's, like.
Paste with markdown formatting? I don't know if that's a thing.
**Trask Stalnaker** 10:18 Paste. From Markdown.
Wait, that didn't…
**Jay DeLuca** 10:24 Sort of work, maybe not.
**Trask Stalnaker** 10:27 Cut… Paste from Markdown.
**Jack Berg** 10:31 What?
**Trask Stalnaker** 10:32 Awesome.
**Jack Berg** 10:34 And a whole new font.
**Trask Stalnaker** 10:36 Jason.
**JP Jason Plumb** 10:42 Okay, I'll have to fix it.
**Jack Berg** 10:45 I opened an issue with Google Docs.
**Trask Stalnaker** 10:46 Do you, though?
**JP Jason Plumb** 10:49 You know I do!
**Trask Stalnaker** 10:51 Alright, so this is in… so really, I think the last thing there is the, JPI, the compare stuff, and, you know, just kind of really, maybe prepping that and combing through that to see, if all the public APIs kind of look like we want them to… The database stability… I think there's more… there's a few things… to do here, including, I think, some kind of complicated stuff, potentially.
around the, SQL parsing this would be great. I would love to get this into 3.0.
The logging stability is a little bit more… Less well-defined.
So, you know… I don't know, it's not super specific, but I would love to stabilize, sort of, like.
I think we have a good sense now, like, we didn't know some things before about how we wanted… whether we wanted to use the log body for structured logs, like mapping log for J structured logs into log body or log attributes.
We now know that we want to map those to log attributes.
And we have extended attributes, potentially, could come into that.
And so maybe combing through log… there's various log-related issues, and sort of… Trying to tie a bow and… Marking that all as stable, which might require some semantic convention work.
clarifications.
And declarative config stability.
Gregor, you're on that.
**GZ Gregor Zeitlinger** 12:49 You can put my name there right away.
**Trask Stalnaker** 12:54 This was just on my personal, like, short list to make sure that I pay attention to your PRs here, because those are priority.
And then RPC stability is coming.
We do have the RPC SEMCOM group and so… We could start… Adding the changes there behind the feature flag.
And preparing for that.
**GZ Gregor Zeitlinger** 13:26 So just to double-check, are you saying that you're more interested in those longer-term topics than helping out short-term, and you're fine with the maintainer load you have? And that's also great feedback.
**Trask Stalnaker** 13:43 Yeah.
**GZ Gregor Zeitlinger** 13:44 Okay, cool.
**Trask Stalnaker** 13:49 I don't know, Laurie, you have… Thoughts.
**Lauri** 13:55 Well, if you want, you could always help out with, with the issues from the users and the GitHub discussions.
And reviewing pull requests.
**Jay DeLuca** 14:16 And I was just thinking, like, so, like, last week, I think there was, like, a lot of moving pieces with the Sprint upgrade and all that. I would just say, like, if there are situations like that where there's a lot of moving pieces, and you guys need help with specific things. Like, maybe you could just post in the back channel, or something like that, but just wanted to… Like, start that discussion of more, like, the reactive stuff, as opposed to, like, the standard or long-term.
Kind of stuff.
**Trask Stalnaker** 14:46 Cool.
**Jay DeLuca** 14:47 But, yeah, we don't have to go back on concrete.
**Trask Stalnaker** 14:49 Yeah.
I'll definitely keep that in mind.
Thank you.
of the offer.
Alright, let's… Let's see, did we… I saw we lost Jack Shirazi… Okay, so let's maybe… Push that back.
Till later, in case he's able to rejoin.
Garib, I see you, hey!
**Ghareeb Falazi (IBM)** 15:25 Welcome.
So, this is my first time joining this meeting.
Yeah, so I'm Garib, I work for IBM Germany.
And, yeah, I have a… I have a PR to add library instrumentation for Apache Iceberg, specifically for metrics.
So, Apache Iceberg emits, metrics for scans, and, this, this PR, kind of.
transforms these, these scan metrics into OpenTelemetry, metrics.
And it's been around for a month, almost, and it was reviewed, like, from Laurie and Jay over the last… Two weeks, I guess?
And, I think I addressed the comments, and… but nothing is moving forward, so my question is, is there something, like, fundamentally wrong with the PR, or is it just high workload for the reviewers, and I just need to wait a bit?
**Trask Stalnaker** 16:38 Yeah, usually, the latter… Just, yeah, we've got a lot of, these new… big new instrumentations take a while to get… for us to get through, because of the size.
We have… discussed also. Now, are you, are you involved in the Apache Iceberg project?
**Ghareeb Falazi (IBM)** 17:05 We do use it in, in our IBM product, so it's, Yeah. We don't contribute yet to it, we plan to, but…
**Trask Stalnaker** 17:19 You considered.
sending the… doing the instrumentation upstream in Apache Iceberg.
**Ghareeb Falazi (IBM)** 17:30 Yes, that's, that's a possibility, but, it's a bit more difficult. There, there, their approach for doing that is quite limited, so I need to introduce a special reporter in their library, and I think they are hesitant to do that. So basically, they do the reporting to look for Jay.
And… With some basic JSON formats.
And it has been like this for quite a while, so they don't, They don't accept to add a new reporter.
**Trask Stalnaker** 18:17 Oh, a new reporter that Sends to.
**Ghareeb Falazi (IBM)** 18:22 Open Telemetry, yes.
**Trask Stalnaker** 18:25 I see. Oh, that's too bad.
Yeah, I mean, the… This repo, as you can imagine, there's no way this repo is going to scale to the number of Java libraries that exist.
And so, long term, we would like to see more of these instrumentations being driven up to the upstream libraries and hosted by them.
That said, you know, we aren't… blocking stuff from coming in here is just… that's kind of the reality of why it's, takes a while, and… There may be some pushback on some things.
**Ghareeb Falazi (IBM)** 19:11 Huh.
**Lauri** 19:12 Jay and Gregor, this would be one of the pull requests where you could help out.
I think they're all, like, some, improvements in the code that could be made. And also, I think there is some confusion about, what attributes actually can be added to metrics, because I think in current implementation, there could be some attributes that… Might have a high cardinality.
But would need to figure out, like, what those attributes actually are.
It's kind of hard to tell without knowing anything about the framework.
**GZ Gregor Zeitlinger** 19:49 Great, then, how, do we identify those PRs that are maybe a little bit more time-consuming, or something like that, at a label, or what would make sense?
**Lauri** 20:08 I don't know.
**Trask Stalnaker** 20:09 really, any… Any PR is helpful.
get reviews on… Especially new instrumentations.
I… Lori generally does most of… I haven't been reviewing the new instrumentations, very much. Lori's been doing most all of that work, so… We could definitely use help there.
Like, here's one for… Servlets that… I think needs… Help.
What can we… I was… there should be a sort by most lines of code.
Because, honestly, that… those are the ones that, right, take… A long time for, to go through.
**GZ Gregor Zeitlinger** 21:29 So conversely, if you can manage to split up your PR into smaller bites, then it's easier to get it reviewed.
**Lauri** 21:40 Oh, but sometimes your feature is, like, quite large.
**GZ Gregor Zeitlinger** 21:44 Yeah, it's not always possible.
**Ghareeb Falazi (IBM)** 21:48 especially introducing a new instrumentation, there's a lot of code that is not really production code, so to speak, just modifying configuration files and… all the, like, README and so on.
**Trask Stalnaker** 22:05 Yeah, a thousand lines seems about… Right to me for, like, it's kind of typical for new instrumentation.
Which is why those, in particular, the new instrumentations, often Take a while for us to get through.
Cool, Garib, did you… have you found our Slack channel also yet?
**Ghareeb Falazi (IBM)** 22:35 Yes, okay.
So, I haven't tried this before, so I just… I can access it directly, or do I need some invitation, or…
**Trask Stalnaker** 22:47 So I saw the link.
Yeah, you should be able to join, yeah, yeah, it's the CNCF Slack, and we have a hotel Java channel there.
But, yes, yes, I would… Say, things look like they're… This is not, this has gotten feedback more recently than other PRs.
**Ghareeb Falazi (IBM)** 23:14 Huh.
**Trask Stalnaker** 23:17 Apologies.
**Ghareeb Falazi (IBM)** 23:20 Okay, so I'll just wait then, and hope for some more comments.
**Trask Stalnaker** 23:28 I'm afraid… afraid that's the… Yeah.
Yeah, I would, I mean… you know, I'm personally very in favor of, you know, trying to push more of these things to the upstream libraries, again, just because this repo just literally is going to fall under its own weight if we try to instrument every Java library in the world.
And so… If you do, I mean, it's certainly worth exploring in Apache Iceberg. You know, maybe they won't accept it as a core component, but maybe they have.
Would accept it as a separate module.
anything… if there's anything they need from the OpenTelemetry project to feel more confident about that, that would be great, feedback for us. We'd be welcome to help out there.
**Ghareeb Falazi (IBM)** 24:31 Huh.
**Prasad Sawool** 24:35 Sorry for, interrupting, but I think, the iceberg library instrumentation would rightfully belong in, like, the Java Concrept report.
**Trask Stalnaker** 24:48 That's another option.
So we do have… the Java contrib library, repository.
I don't know, Laurie, any… thoughts or preferences?
**Lauri** 25:12 I think, the current state of affairs is such that, But for Java agent instrumentations, it's more convenient to have them inside agent, because otherwise, the users would need to add An extension, specifically, Jenna.
To enable that instrumentation.
**Trask Stalnaker** 25:32 This one looks like a library-only instrumentation.
**Lauri** 25:37 is it?
**Ghareeb Falazi (IBM)** 25:37 Yeah, so… so far, yes, so… I was planning to add a… a Java agent instrumentation in a second step.
Okay.
So I didn't want to make it big, so that's why I split it.
**Lauri** 25:55 then yeah, what Lori said makes sense.
Yeah, but, the thing with Contrib is that getting anything reviewed, there is, Even harder than in the instrumentation repository.
I believe.
**Trask Stalnaker** 26:12 You would need to find another sort of co-owner arms.
But… Yeah, it's gonna be… Hard then to necessarily… you may not get as much feedback, as you're getting in the instrumentation repo.
Like, already, you know, there's been a lot of good review, and… Time spent on, kind of, you know, trying to… Flesh it out to, sort of, the instrument… the standards that we'd follow in this repo.
**Ghareeb Falazi (IBM)** 26:52 Yeah, yeah. So I'll just wait. I will explore upstreaming it to Apache Iceberg. It could be… difficult.
But I think the PR is already, like, it already has 22 comments and answers and so on, so… I think I'll just wait a bit, so it's not a big issue.
**Trask Stalnaker** 27:18 Okay.
**Ghareeb Falazi (IBM)** 27:20 Yeah, thank you.
**Trask Stalnaker** 27:21 Sounds good. Yeah, thank you.
Next… alright, hey, imagine that, another…
**Tyler Benson** 27:29 Speaking of instrumentation…
**Trask Stalnaker** 27:30 documentation… Yes.
**Tyler Benson** 27:34 So, last week, I got some good feedback and, spent some time refactoring the, the unit tests so that, there's a whole lot less duplication there. Yesterday, I… I bet the buck, I just decided, hey, let me, because there was still a lot of concern of the size of the PR, even after reducing the test duplication.
So, I opted to, refactor and remove all the code duplication, the, sorry, the code copying, and, explore using Shadow, to.
To just bring all those dependencies in via Shadow, and it makes the PR, a lot smaller. So I think it's gonna be a lot more, reviewable at this point. I know that there's some concerns, around having a library instrumentation shadow a Java agent instrumentation.
But, I think this is gonna be the best approach long-term, unless we, like.
restructure everything so that, most of the Java agent instrumentation classes are in the library instrumentation, and then have the dependency reversed.
But there's still some class dependencies that go out to other packages that we probably wouldn't want to do that in, so it really makes it kind of difficult.
But anyway, I wanted to, just bring it up here to see, if there… if that addressed the concerns, and if there was any other feedback that, that… You could share.
**Trask Stalnaker** 29:23 I don't love the idea of shading the Java agent.
modules inside of the library instrumentation. To me, that just because we… don't do that anywhere else. It's always the library, the Java agent that depends on the library instrumentation.
So… I would… Prefer to see that explored more, if you can achieve the same code deduplication, but move that common code to the library side.
Without having looked at Anything else? Sorry.
**Tyler Benson** 30:08 Yeah, if you pull up the PR, I can point out some dependencies where I don't think that would work so well, but I'm open to…
**JP Jason Plumb** 30:19 Discussion on it.
**Trask Stalnaker** 30:21 Maybe you can add some inline comments?
Honor.
**Tyler Benson** 30:26 On the side, if you go down to the, the POM, or sorry, the, the Gradle file.
So, examples of this would be, scroll up a little bit more, it's in the, the other Gradle. So there's now two Gradle, projects.
**Trask Stalnaker** 30:53 Where did I change my filter?
View.
But I could filter files… oh, here we go.
This one?
**Tyler Benson** 31:09 Yeah.
So, those are all of the, the projects, that are basically getting… that have dependencies that are getting shadowed in, So, I imagine it would work for, like, the servo instrumentation, but there's still, some classes in the Java Agent Extension API where I don't think that would work.
Unless Java Agent Extension API is published, but I don't know that it is.
**GZ Gregor Zeitlinger** 31:38 Why are you depending on the Java Agent Extension API?
**Tyler Benson** 31:42 There's classes in there that are, transitively used.
**Lauri** 31:49 Because the original code is, is for Java agents, so it can depend on that.
**GZ Gregor Zeitlinger** 31:57 So should we move, the classes in question, to a module that is, Published.
**Tyler Benson** 32:08 I'm not opposed to that. I… it's really a question.
the… so, one example of a class that falls into this category is, like, the agent config class.
Which… obviously is very, you know, Java agent specific, but I don't know that moving it…
**Lauri** 32:30 The trick with agent config is actually simple. You just shouldn't use it inside library instrumentation.
And it's just… generally, the same strategy applies with the other classes also.
I understand it's going to take a lot of work to figure out how to do it.
**Trask Stalnaker** 32:54 Yeah, but I think that there's probably… My initial feeling is this would be a blocker to getting this merged.
**Tyler Benson** 33:02 Okay, so if you do the comparison of, like, the previous commit onwards, like, you can still see that there's, with the copying of the classes, it still has, like, a 4,000-line commit, change.
Would… so… If you would like, I can…
**Trask Stalnaker** 33:20 Can you find…
**Tyler Benson** 33:21 blast commit where it, switches over to shadow, and having, so just removing that and going back to the copying, and letting that be the review.
Is that… What you'd like me to do?
**Trask Stalnaker** 33:36 I think you need to find some way to make it smaller and iterate You know, that… some… Some narrow use case that you can solve, like, even if it's from scratch, But not… I don't know. I… I would have to spend a lot of time digging in, right? And this is the kind of.
**Tyler Benson** 34:00 No, I understand.
**Trask Stalnaker** 34:01 So, all I can kind of provide…
**GZ Gregor Zeitlinger** 34:06 But what about shadowing the other way around? Having the library instrumentation, and then, shadowing, for the Java agent instrumentation. I think that… that is, more in line with what we do. And for the configuration thing.
We have other, cases where, we have a common configuration that can be used both in library and in Java agent, and then, then this should work. This is called a common config.
**Tyler Benson** 34:43 So… I think that, you know, we can certainly explore that option. The concern I have with that is that a lot of cases where the config is there on the Java agent side, it doesn't necessarily make sense for this. It's just gonna default to a no-op. For example, like, with the, I think it's, like, the snippet.
Injection. We just… the library instrumentation cannot, do anything with that.
And so, the config doesn't make sense for that.
**Lauri** 35:23 Actually, why do you think that the library instrumentation can't do the snippet injection?
I think you can wrap the output stream, or whatever.
**Tyler Benson** 35:34 So, I looked into it, and in the case of the print writer, so one of the cases it could, but another case it could not.
So, I figured, in… just because, I couldn't get 100%, compatibility, it was probably better just to not include support for it.
**Lauri** 35:56 Yeah, like, the snippet injection is, like, If it makes things easier, it's definitely something that can be omitted from the library instrumentation.
**Tyler Benson** 36:08 Okay.
Well, I'm hearing the feedback that Shadow is a non-starter, so I will… restructure the PR and see if I can… Make something that's more, more compatible.
Thank you.
**Trask Stalnaker** 36:31 Alright, thanks.
Bruno.
**Bruno Baptista** 36:41 Hello, good afternoon, good morning.
So, a couple of weeks ago, I'd, so, Jack implemented a refactor of the senders, the HTTP and gRPC senders.
For our exporters, and I, tried it, I implemented that, new API, on the Quarkus side, and it works okay.
the impact on the user side API is minimal, even if the APR is quite big.
And it passed all our integration tests with a real hotel collector, so… And we test for TLS, compression, and gRPC and HTTP, so… I think it's good.
I have a couple of suggestions, just to try to improve the final version.
And, well, let's see how it goes.
**Jack Berg** 37:43 Hey, thanks a ton for doing that. It's always hard to, you know, test something out off of a… off of a, you know, a fork in a branch, but, you know.
We're doing this specifically for Quarkus, at least that's, like, customer zero, besides the internal implementations of the sender, so… Really awesome feedback, I appreciate it.
I see your comments here, If you want, we can discuss them synchronously. I don't think there's anything that is, like, you know, very surprising about the questions you've asked. I think they're good questions, and, you know, we can work through them.
**Bruno Baptista** 38:21 Yep, yep, sounds good.
And that's it on my side.
**Jack Berg** 38:27 Exoton.
**JP Jason Plumb** 38:28 Sorry. Jack, do you…
**Trask Stalnaker** 38:30 Oh, go ahead.
**JP Jason Plumb** 38:31 Sorry, I was just gonna get caught up on this one. So the goal here is to have, like, a true public API for the senders.
**Jack Berg** 38:38 Yeah, yeah. Bruno and other folks have been asking for this for a long time, and, you know, it's also related to this, this goal I have, and another issue, which seems really far out now, but it's still something to work towards, which is like, hey, we shouldn't have any, shared internal code.
Right? So, like, if you… if… like, we say that stuff that is in our internal packages, we can make breaking changes on.
**JP Jason Plumb** 39:06 Right?
**Jack Berg** 39:06 But the practical reality is if you have intermodule dependencies on internal code that experiences breaking changes, then you have to have all your versions of your dependencies aligned, or else, or else you can have runtime errors.
**JP Jason Plumb** 39:23 So, this is something, you know, Lyudmila gave us feedback on a while back.
**Jack Berg** 39:27 And, you know, after a bunch of talking, you know, she convinced me, like, hey, this is absolutely the way to go. So, it's a long-term goal. I don't think we have, like, the resources to get it done in, you know, the immediate future, but this works towards that.
**JP Jason Plumb** 39:42 I'm mostly asking because there was such… there has been, over the last few years.
a pretty strong reluctance to expand the API surface at all in Core, and this is a pretty big change.
So that's… I just wanted to… to make sure that I…
**Trask Stalnaker** 39:58 Yeah, it's been brewing for a long time.
**JP Jason Plumb** 40:01 Okay, that's cool. The asks have been there for a long time. I definitely have seen people ask for this, yes.
**Trask Stalnaker** 40:07 We have held off, like, I think as long as… It has been reasonable.
**JP Jason Plumb** 40:13 Yep.
**Jack Berg** 40:13 I caved.
**Trask Stalnaker** 40:15 I support, and support it.
I was gonna ask Jack, so, do you want to… are you ready for review of, sort of, the public API surface? Can it go to out of draft? What's the next step?
**Jack Berg** 40:32 So, I want to coordinate with John on this, because I want to be able to make sure that whether we do this in one big PR, or if I break it up into, like, you know, different PRs, I opened a draft so I could have, you know, a PR showing the complete, finished vision.
But I'm happy to break this up into smaller chunks to make it more reviewable for John and other folks. But, you know, when we do start actually making a push to get this merged. I want to do it in one release cycle, because it's going to be a lot of churn for Bruno and folks who depend on these internal APIs, so let's get it done at once.
In one shot.
**Trask Stalnaker** 41:13 And as far as the new… public API is all… This stuff right here, these.
**Jack Berg** 41:25 Yeah, it's in the Exporter Common module, and it's, like, I… I basically… the PR gets so big because I jump through some hoops to minimize the API surface area. I want to make sure that the API is evolvable.
And as we have more and more configuration options, we want senders to be able to respect and implement. Like, there can't be a breaking change every time we do that. There can't be breaking changes, period. We need to have it be evolvable.
And, you know, I want to hide all the things that we can that are internal implementation details. In particular, the implementation right now, if we were just to promote it to public, it would drag all of our hand-rolled marshaller utilities into the public API surface area, and that would be a disaster. So, I introduced some much more narrow, you know, abstractions that, like, you know, basically allow all the martial arts have to be, like, encapsulated and hidden.
So that's what makes this big, is like, you know, a shuffling around of things to keep the API surface area as narrow as we can possibly, you know, achieve.
**JP Jason Plumb** 42:34 And then this idea is that by making these interfaces public, presumably, in addition to our, kind of, default implementations of those interfaces, Quarkus and others can then provide their own implementation? That's the idea?
**Jack Berg** 42:48 That's the idea. I still think it's an advanced use case, and so I hope that there's not, like, a dozen of these things, but, like, you know, Bruno has convinced me that, you know, there's a real need for another implementation of this in the corporate ecosystem, so let's support it.
And I was initially skeptical of this because of two reasons. I didn't think that we could, provide an API that would allow us to evolve without, you know, breaking all these implementations all the time.
And then the other one was, supportability. I was afraid, like, hey, if Quarkus and these other sender implementations are, you know, experiencing issues, there'll be a bunch of additional support load on John and I, and it'll be hard to track down who's responsible. And, you know, basically both have been put to rest. Like, over the course of time that Quarkus has depended on these internal APIs, we haven't gotten any support requests.
about their implementation.
And, you know, I… also, I figured out how to evolve the… adjust the API so it's evolvable, as our config options change, so I'm happy enough.
**JP Jason Plumb** 43:52 Cool.
**Bruno Baptista** 43:53 Just another note. So, since we created these senders, Wildfire has started to use them.
as well.
And I'm… I'm preparing probably to… to… to create some… some kind of… library that will encapsulate and that we will support, so whoever wants to use those vertex senders can, but it's supported by us.
**JP Jason Plumb** 44:22 And is the intent, then, to also support this through auto-configuration, this pluggability, or is that something that's already covered today?
**Jack Berg** 44:30 It's covered today because there's a system property that you can specify to indicate which sender should be used if multiple are discovered on the class path.
So, but, like, it's not… it's not part of declarative config, for example. Like, it's, like, there's a few things where, you know, the only way to con… that are, like, you know, internal configuration options, and the only way to actually, you know, toggle these knobs is via system properties or environment variables, and sender implementation selection is an example.
**JP Jason Plumb** 45:00 Okay.
**Bruno Baptista** 45:01 But I think that the correct way, probably, is to use different exporters that each one have their own senders.
That's probably the more obvious way to do this.
**Jack Berg** 45:17 You could do that too, if you wanted to. Senders are abstract enough where, like, you know, you could imagine that, you could replace you could replace Zipkin's internals with, like, a center implementation based on the Quarkus implementation, or the, but… Yeah, right now, I don't think that exists.
**Trask Stalnaker** 45:43 Cool. What's the inter… What's the overlap between this and authenticators?
**Jack Berg** 45:52 Yeah, Authenticator would need to be, you know, if you go to, for example, GRP sender config, or HTTP sender config? Let's do HTTP, because GRPC is lame. So this is a… this is an interface that has, like, all of the configuration options that can exist.
And, you know, the… ideally, a sender implementation adheres to all of these. You know, like, you know, reads the Java docs, and if one of these options is set, or, like, non- null , like, you know, configures their underlying client library to adhere to it. But, if a new authenticator concept is introduced.
and the specification, you know, we'll have a new SDK extension plugin point, and maybe it's called Authenticator or something like that. And so, we would have to evolve this interface to, like, add a new getAuthenticator method. And, you know, it would be null able, and at first, there'd be a default implementation where the default is null , which means there is no authenticator.
But then, you know, the expectation would be that if it's set.
You know, the senders adhere to whatever specification we have around it.
**Trask Stalnaker** 47:08 Okay, and did we… is… is our authenticator, did we ever implement or make that public?
**Jack Berg** 47:17 No, we deleted it.
**Trask Stalnaker** 47:20 Oh, okay. Because…
**Jack Berg** 47:22 It was… it was like a… it was a bad idea. Like, it was… it was poorly thought through, if I'm… if I'm honest. It was… it was essentially a, just a supplier of… of… of headers that was invoked And, like, for each request response, and I'm forgetting the details, but, like, I explained it in a PR description where I deleted it, but, like, it basically had no utility at all. And I don't think anybody was using it, because it was deleted and nobody made any noise.
But…
**Trask Stalnaker** 47:56 We just have static headers? I forget what…
**Jack Berg** 47:59 We have a supplier of headers. You can configure static headers and a supplier of dynamic headers. That's what you… that's what we got.
**Trask Stalnaker** 48:07 Oh, okay, and is that… oh, and that's over here already.
**Jack Berg** 48:11 Right, and so when you invoke this, like, you know, the idea is you keep a reference to this supplier, In your sender implementation, and invoke it for each and every export request.
**Trask Stalnaker** 48:24 Yeah.
**Jack Berg** 48:25 And, the underlying implementation here is going to provide a merged representation of your static and dynamic headers.
**Trask Stalnaker** 48:39 Awesome. Makes sense, yes. And then, if we have the more generalized spec authenticator concept that I know Gregor has proposed from a declarative config perspective, then we would just have a new getter here.
**Jack Berg** 48:55 Yeah, exactly. And any other options that pop up as, like, you know, things that senders need to be configured with? Would it manifest as new getters here?
**Trask Stalnaker** 49:09 Alright.
That was a good deep dive.
Let's move on. Did we get… oh, is this Jack Shirazi or Jack Berg?
**Jack Berg** 49:22 This is maybe… this is just a quick inform. There's, there's something in the spec that was added within the last couple of months That's, you know, there's a formal specification for a rule-based sampler.
So, like, you know, all the work that we did in the JavaSig to support this use case of, like, hey, I want to… I want to not sample health… health check spans, or some other types of spans. So, there's now actually, like, a formal spec for how you do that. And, Adarag, our old friend, has been driving the implementation in OpenTelemetry Java and in Declarative Config.
Writing up, like, exactly what the configuration interface looks like in YAML to be able to specify those rules. So, that's coming.
And it'll be standardized across languages, which will be nice, and then not just, like, a Java Contrib-specific thing. And, you know, what we'll have to do after that lands is come up with, like, an end-of-life, you know, path for the rule-based sampler that lives in Contrib.
**JP Jason Plumb** 50:24 We had talked a couple of weeks ago about using CEL or something else for that kind of stuff. Is that being considered, or… Like, just for the actual language of doing this stuff.
**Jack Berg** 50:36 So, there's a balance here, and I brought this up to the SamplerSig. I was like, hey, samplerSig people, go look at this. This is the configuration interface that we're looking at, you know, landing for how you specify this in YAML. And I was like, you know, there's a balancing act between expressiveness, like, how rich of an expressive language do you have.
And between implementation, so, like, how much effort is it for the, like, SDK maintainers to go and implement this thing, and then UX. Like, you know, what's the user experience like for actually, you know, writing out these rules?
And, you know, these things are in tension with each other, and we have to find a way to strike a balance.
I trust Anorog a lot with this, because of his experience with OTTL and the collector, and so, you know, and just… he's just been all across open source for a long time, so he has a big breadth of knowledge and experience of, like, other systems and how they express rules like this. So, you know, I know he's been using, like, Envoy's rules as, like, a reference for what he's been sketching out.
So no CEL, you know, right now, but this is just the first draft, it's not the final set.
**JP Jason Plumb** 51:48 Cool.
**Trask Stalnaker** 51:50 And we would keep the CEL router, base, rule, router in contribib.
Sure. For, you know, people who want that more advanced, use cases.
**JP Jason Plumb** 52:03 Yep.
**Trask Stalnaker** 52:05 But this is amazing. Yes, this will be so nice to have this standardized across all the languages.
And I was just checking, because I got nervous, but thankfully we use… a different name. We… we use rule-based routing.
**Jack Berg** 52:24 By sheer luck.
**Trask Stalnaker** 52:25 based. Yeah. Thank God. Otherwise, migration would be more painful.
Cool, awesome.
**JP Jason Plumb** 52:42 Still no sure, Azi.
**Trask Stalnaker** 52:44 Okay.
**JP Jason Plumb** 52:46 I hope that fi- I hope that fire alarm was just, like, a test.
**Trask Stalnaker** 52:50 Yeah… Jack, I saw you were commenting on this. Thank you.
Yeah, I'm… I mean… however we end up solving it, I'm excited that people are interested in solving this problem now.
**Jack Berg** 53:11 Same.
**Trask Stalnaker** 53:11 And, yeah.
**JP Jason Plumb** 53:14 Not a day goes by over here that we don't hear about this. Like, someone's asking about it every day.
**Trask Stalnaker** 53:18 Nice.
**JP Jason Plumb** 53:20 Yeah.
**Trask Stalnaker** 53:22 Let's make it happen.
**JP Jason Plumb** 53:23 Yep. We need to contribute release.
I can probably run that today, if that's helpful.
**Trask Stalnaker** 53:32 Sure, go for it.
Let's see, this… I don't know why I renovate… why are you trying to update us to a snapshot?
**JP Jason Plumb** 53:42 And I blocked it.
**Trask Stalnaker** 53:45 Yes.
**Lauri** 53:45 It might be because it previously was a snapshot.
**Trask Stalnaker** 53:51 Right, but yeah, I hit… I did this this morning, thinking… thinking the same, and you're probably right, but it is just not smart enough to.
**Lauri** 54:03 We could remove the snapshot repository.
**JP Jason Plumb** 54:07 Yeah. Is it used… it might be used for other stuff, though.
**Lauri** 54:10 It was used temporarily, because it made some stuff easier to update Asian dependency just now.
**JP Jason Plumb** 54:16 I think I remember that.
**Trask Stalnaker** 54:18 Oh, okay, okay, cool, we'll do that. That's a good idea.
**JP Jason Plumb** 54:25 I didn't see anything… I didn't see anything else in the list that was, like, super pressing, or that people might be interested in, maybe?
**Trask Stalnaker** 54:38 Nope.
**JP Jason Plumb** 54:40 Cool.
**Trask Stalnaker** 54:40 Yep.
**JP Jason Plumb** 54:42 Okay.
**Trask Stalnaker** 54:43 Let's do it.
**JP Jason Plumb** 54:44 Thanks.
**Trask Stalnaker** 54:45 Thank you.
We've got one minute.
Gregor?
Let's, We've got our declarative Config meeting next… Week.
**GZ Gregor Zeitlinger** 55:04 Yeah, the meeting agenda was pretty empty when I added it there.
It's all good.
**Trask Stalnaker** 55:10 Alright, then.
Well, any last… short.
Topics, comments…
**Jay DeLuca** 55:19 Next.
Thanksgiving.
**Trask Stalnaker** 55:21 Oh.
Indeed, yes. So, no meeting next week. I will go cancel that now.
Alright then.
See you all in… 2 weeks!
**JP Jason Plumb** 55:38 Okay, have a good one.
**Jack Berg** 55:40 Dear.
**GZ Gregor Zeitlinger** 55:41 Fair.
