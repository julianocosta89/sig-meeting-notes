SIG: JavaScript SIG
Date: 2025-11-05
Duration: 58 minutes
============================================================

## Zoom Recording Transcript

**Bhaskar Banerjee** 00:43 Love books.
**Marc Pichler (Dynatrace)** 00:46 you… Right? Hello, everybody.
**Hector Hernandez** 01:13 Hello.
**Marc Pichler (Dynatrace)** 01:15 Let's get started on… There's nothing on the agenda today.
Let's wait a little bit, in case anybody wants to add something.
**Bhaskar Banerjee** 01:34 I have the data here, certainly. I don't have access to this document from my… enterprise network, so I cannot add to it.
**Marc Pichler (Dynatrace)** 01:45 Back in touch for you.
**Bhaskar Banerjee** 01:47 Thank you so much, Ben.
**Marc Pichler (Dynatrace)** 01:51 Yes, do you want to.
**Bhaskar Banerjee** 01:55 is… there's a feature that, I'm seeing, it is for OpenTelemetry JSON exporter.
directly, or console.
I see that for Java, it is an experimental phase. I see there is a PR open for Python. I wanted to know what is the… update or plan for JavaScript grip for that.
**Marc Pichler (Dynatrace)** 02:21 Is there an issue open already for this one? I'm not exactly sure which exporter you're talking about.
**Bhaskar Banerjee** 02:29 It is not in the JavaScript group, but there is already support for Java and Python. So before we open an issue, I wanted to check in and figure out, is there already a plan? Maybe I am not seeing it correctly.
I mean, I'm happy to open an issue, work on it, either way.
**Marc Pichler (Dynatrace)** 02:48 But kept connecting to figure out.
**Bhaskar Banerjee** 02:51 Is this group aware of this feature? If yes, is anything in works? If not.
I'll be happy to… Opened up an issue.
And do whatever it takes there.
**Trent Mick** 03:07 Definitely open up an issue. Mark, I'm not sure if you saw, there's a comment in the chat with a link to… this is the OTLP slash standard out experiment.
**Marc Pichler (Dynatrace)** 03:15 Okay.
**Trent Mick** 03:17 You mean?
**Bhaskar Banerjee** 03:18 That's right, and for Java, there is a support for this, in experimental phase.
to send out… send it out in JSON format.
Likewise, in Python, it isn't… it's a PR yet.
I don't know what's about JavaScript.
**Marc Pichler (Dynatrace)** 03:37 I think there's no… issue for opened for that yet. But since it's in the spec, we'd be happy to, add this one then.
So, if that's something that you would like to work on, I think we would appreciate that.
**Bhaskar Banerjee** 03:56 Sure.
**Jamie Danielson** 03:56 Yeah, I think it's use… Sorry.
**Bhaskar Banerjee** 04:01 We have a pressing need for that, so happy to contribute any way we can to… Make it quick.
But yeah, we'll go with whatever this… Committee comes up with.
**Jamie Danielson** 04:14 The best starting point is to create an issue, like you suggested, with kind of the details of, you know, where like, what this is, some of the links, and, like, pointing out Java and Python, like you mentioned, that way it's sort of easy to, like, reference in the different places, and then from there, we can sort of agree, like, yes, we're all in agreement of that's the right way to move forward, and if you have time to take that on, that would be good.
**Bhaskar Banerjee** 04:40 Sounds good. I shall send that out today. I have sufficient write-up with me. I'll create one today and send it out.
**Jamie Danielson** 04:48 Cool. Thank you.
**Bhaskar Banerjee** 04:49 Thank you so much.
**Marc Pichler (Dynatrace)** 04:50 Thank you.
Alright, and I think it should be, probably fairly simple to implement that one as well, because all the, internal representation to OTRP transformation logic is in the OTLP transformer package, so it would just be a matter of taking that and then writing it to a file, if I understand correctly.
**Bhaskar Banerjee** 05:17 Right. I'll refer to what's there in Python as well, because I find a similarity there, so… will share whatever I find, and seek your thoughts.
**Marc Pichler (Dynatrace)** 05:28 Thank you, that sounds good. Thank you.
Thank you for, Epic, I said I was going to do it, but now somebody else is doing it, thank you. All right, There's no more… questions or comments about this, then I guess we could move on to the next topic.
Hector, about, existing JS features in the compliance matrix.
**Hector Hernandez** 06:03 Yeah, well, the thing here is that it looks like several PMs in Microsoft are using this as the source of truth, and I can see that JavaScript has not been updated for a while. There's a lot of stuff that is actually support it, and, So, my question was, I can send a PR to update this, include the JavaScript approvers. Just wanted to know if we're actually… Taking a look at this, or if this is something that we missed, or…
**Marc Pichler (Dynatrace)** 06:33 Yeah, it's likely something that we missed. There is, like, keeping that up-to-date is, Sometimes, it's, it's not in any of our, checklists, usually, so… Okay.
**Hector Hernandez** 06:48 That's fine.
**Marc Pichler (Dynatrace)** 06:49 of date quite quickly, and you might find that there's other, other SDKs that aren't too up-to-date as well.
**Jamie Danielson** 06:58 Yeah, there was discussion of removing this entirely, because it's hard for people to keep up to date, because it's, you know, people forget to go in and change it, but I don't think there's an alternative that anyone has settled on that's…
**Marc Pichler (Dynatrace)** 07:10 Yeah.
**Jamie Danielson** 07:10 better, so it's sort of in a limbo state. But yeah, so we were behind in updating this for sure.
**Hector Hernandez** 07:16 But it's not going away, right? So…
**Jamie Danielson** 07:19 I don't think so.
**Hector Hernandez** 07:20 Okay. Okay, I will, I will… Okay, I will send the PR later today, then, to update this. It's just, I get asked, is this supported? The matrix says not, and then I need to find a actual source code that does that, so… Okay, yeah, I will… I will take care of this. Thank you.
**Jamie Danielson** 07:40 Thank you.
**Marc Pichler (Dynatrace)** 07:41 Thank you for taking care of this. It comes up periodically, and then it gets updated to whatever is the latest, info, and then it goes out of sync again, unfortunately. So having that, there is, for sure helpful, I hope, that, yeah, it doesn't go away too soon, so that your work is in vain, but.
**Jamie Danielson** 08:07 It's definitely been updated by other people in the last few days, so that… That seems good.
**Marc Pichler (Dynatrace)** 08:12 Yeah, and even if it were to, like, go away, I think we would still use it. If anything, I think the question was whether.
**Jamie Danielson** 08:17 each, like, repo should have their own version, so it's easier to, like, find and update, but I don't think, like, the table itself in general is really gonna go away, so no matter what, I think it's still useful.
**Marc Pichler (Dynatrace)** 08:34 Yes.
Thank you for looking into it, and thank you for bringing it up. It, I wasn't thinking about it too much anymore.
And, yeah.
Probably shows.
Alright.
Any other, topics that you would like to discuss?
If there are none, then we can move on to the bug triage.
section. As always, if you have any topics that you would like to discuss where we're doing backtrash, please feel free to just… Interrupt me, and then we can talk about your topics.
Right? So, in the core repo, there's no new… Pack tickets opened, and in the country people, Personal new park ticket system. Correct.
Seems like there's something wrong with the filter.
books.
Alright, let's have a look here.
Well, let's have a look at the… Origo again, because it's… Didn't seem to work earlier.
Pretty good.
Alright, the first one is Fire Store Talentimetry course span at the event of the gRPC instrumentation ended the span.
From the title here, it seems that this is actually some other instrumentation code that tries to add something to an ended span, if I understand that correctly.
Telemetry automatic instrumentation, Firestores, telemetry wrapper course, span at event in the stream, and… handler after gRPC instrumentation has already ended the span.
Interesting. That seems that they are obtaining the span and then trying to add information to it.
But the span has already ended, which would mean that they are… They should change their behavior there.
I'm not too familiar with, Google Cloud Firestore, I'm not sure if anybody on the call here is… So, I think we would need to look into that a little bit more.
**Jamie Danielson** 11:40 Is there, like… a fire store… Like, I'm wondering if it makes sense for the issue to exist on the… Firestore wrapper, if that's what one of these things are.
Versus… here.
**Marc Pichler (Dynatrace)** 12:00 Yes, In the thing here, it says, what did you expect to see? Consider whether span and timing should be configurable for streaming RPCs.
I wonder what SEMConf… If there's any specification that tells us to… Let's read this. It tells us when, span… or RPC spans should start and end, and gRPC specifically, if there's any guidance on that.
I know for HTTP, there is… Some information that you should, like, once the headers are received, End the span, or something like that.
For clients.
What's RPC?
gRPC.
Seems, Not too detailed.
Distinction from HTTP spans.
Doesn't seem to say anything here. Yeah, I'm late.
Initial feeling is also that, there should be… some adjustment on, the Firestore.
site that they… Either add that information… earlier?
Or… Create their own span, which, just encompasses the, streaming spin.
That's already closed.
**Jamie Danielson** 15:00 I'm not sure if this is… the thing or not, I'm just reading it for the first time now, but in the spec, it has, you know, that you should ignore all subsequent calls to end, and anything else.
But then says, there might be exceptions when Tracer is streaming events and has no mutable state associated with the span. I don't know if that's… the same.
Thing.
**Marc Pichler (Dynatrace)** 15:43 That's different.
This thing I don't think I've ever… seen this before.
It's also pit.
vague. It would have… -Oh.
Would be nice to have some sort of example where this may be used. As far as I… understand the… all SDKs do it in a way that, Once you end it, you can't do anything anymore.
That's the main reason why the on-ending, span processor, functionality was proposed, So that you could, like, finish up whatever you're doing.
Before it's… the end, operation is actually finished.
I guess we would definitely need to dig into that a bit more. I'll put a comment here, seems like.
**Trent Mick** 17:22 There is a repo for this.
Google Cloud Firestorm module. Like, I don't know.
Issue should be there, or… Yeah.
**Jamie Danielson** 17:37 My thought is to at least have something there, like, in case, like, they have… A more… like, one, if there's a different way that they can… do this, or to, like, if they have ideas on how to solve it, because I don't see it as being, like.
a super high priority right now, unless we get more feedback, because this hasn't come up Before… Or at least not commonly, that I'm aware of.
**Marc Pichler (Dynatrace)** 18:06 Yes.
Damn.
Something already exists.
**Trent Mick** 18:30 I didn't find anything.
Just that one here.
**Marc Pichler (Dynatrace)** 18:33 Hmm.
Totally.
I will take some time after this meeting to type up a response. I think the reason why it's, being ended in… on receive status.
Is… because that is… Essentially also where, when we end, server spans for HTTP.
I think it's when we sent the status, that's when we end it, and for the client spans, it's also the same way.
Like, once the headers are received. So that's probably the closest, match to that.
Yeah, I will do some more digging, I will assign myself, And then come up with a comment. Thank you for the… Input on this… wasn't aware of this, specification as well, so I will also do some digging in other SDKs and see if they, have some sort of functionality somewhere that, Implements that, or if that's just some remnant of… Some thought that, came up when writing the spec.
And the next one is instrumentation runtime. Node time series errors when trying to send metrics.
Boom.
An online time series, good luck piece.
**Raphaël Thériault** 20:48 It looks like a single cloud error again.
Cause, like, I know we've been ingesting those just fine.
**Marc Pichler (Dynatrace)** 21:07 Yes.
Let's see if there's any… Transformation under that… Suggests what's wrong.
They have their own metric exporter as well.
So that's probably also… Why they get such a detailed, Error message passed on to the metric reader itself.
I think in the UltraPX portal, we mentioned that, And, we log it in the actual exporter.
Just see, yeah… I mean, thanks for reaching out.
Alright, let's just look… Real quick, real quick. There's this… Metric export that they're getting from… This thing right here… Not sure where the code for this is, hosted.
Open telemetry Operations JS.
Slip away.
There we go.
Or just, Let's see if you… Amongst here in the chat, there's… Potentially related…
**Trent Mick** 25:16 So that… that error message is… maybe you guys are already here, is coming from the Google Cloud Metrics.
Whatever the receiver is on that.
And then there's a comment in there.
From someone from Dashpole on January 25th.
That was linking to the Google Cloud thing, talking about metric quotas, which is probably… Where the error's coming from, and then suggestion, at least for this case, that it could be… Not having sufficient labels to separate, separate, streams, which means that the receiver on Google Cloud would see effectively what OpenTelemetry is thinking, separate metrics coming in as one? I don't know.
Anyway, at least for that example.
**Marc Pichler (Dynatrace)** 26:16 Interesting, I wonder… Maybe we could also… comment here, I think I've seen, Looks like Aaron is… working on this.
air ping, error.
Maybe he has some input, or knows who to… Send to help this person out.
They would probably have the context that's also in the, collector issue.
There.
And hopefully they will be able to help out.
Then there's a second one that's… As information how to… Exclude metrics… In case they want to do that, that would also be an option.
Boom.
This is… 20 seconds, so it's for sure more than the… 5 seconds that they also had mentioned in that other comment.
Alright, let's see if, Aaron can help here, and we'll just keep that as on triage for now.
And we'll get back to it.
Based on the comments there.
This one seems to be already assigned, so that's great.
Pretty slower, and if… Looks like Morivia did already more or less triage this one.
I grab it.
-Oh.
tool.
And we're gonna assign D.
Discrimination.
Mr. Bishop G… And… that's it for this one.
Seems that there's already a VR as well, so that's great.
And then there's, Spencer, not be super… I tried to reproduce this, but… loaded up, so… Let's keep it open for one more week… one more… one more week, and then, we'll close it next week, if there's no response.
Memorial needs… author response, and I will ping them again.
Alright, and that's it for the country preval.
And then we move on to… -Oh.
Yeah, our triage, or… Head back to the agenda, Jackson added something here.
This is the filtering log record processor. I think I wasn't able to… Looking to this after I came back from… Vacation… I think this used to be this, other configuration, which was… this year.
So to anybody unfamiliar with this, there's this logger configurator, thing that's in the SDK spec that basically says that, it's a function that computes a config, and you can essentially have some shortcuts where you would be able to disable one or more bloggers, or do some sort of filtering based on Severity and stuff like that.
And… I was looking at the initial implementation of this, And… Was a bit confused by the specification feature, because, it… Panda seems to duplicate some of the existing functionality, like the log record processes, specifically.
which would allow you to filter out, some stuff. I guess the reason why this was added was to make sure that, log records can actually be dropped Before it creates a bunch of allocations later on.
So the way that it works right now is, you create a log record, you emit it.
And then, we basically create, like, an SDK internal log record that's, Then… used.
There, somewhere, and it does some, checks on the attributes, and stuff like that to make sure that, the attributes conform with whatever limits we have and things like that, and that can be an expensive operation. The… Logger Configurator would allow us to basically not do all of these checks.
at all, because we can just drop it based on the severity and stuff like that.
I guess I just have a general question to everybody that's on the call today. Do you think it would make sense to… have this sort of feature in, like, a logger configurator way, or do you think we should optimize the internals of the, SDK itself to make sure that a log record only does all of these expensive checks when it's actually being used, rather than, Immediately.
Been rambling for a bit, maybe.
If there's anything unclear, please let me know.
**David Luna Bistuer** 34:35 Is there a way to see the benefit of that?
to measure it? Sure.
**Marc Pichler (Dynatrace)** 34:42 The, the benefit of, So, the benefit that we would have by, essentially saying we don't have this logger configurator, and we move it to the end of the pipeline, is that we wouldn't have another… thing that could potentially confuse users. So, you have two ways of doing the same thing, right? And by just reusing the existing interfaces and building on top of these.
We could just give them one way to do it.
**Jamie Danielson** 35:19 It looks like, Jackson did update that, actually, after this. Just mentioned that his mic isn't working.
**Marc Pichler (Dynatrace)** 35:28 Cool.
Yes, so that one is now… seems to be actually doing a filtering log record processor, so that would be… likely what I suggested, we would do instead. So everything is basically contained in this one processor right now, where you can filter by severity or other things.
This, I think, still has the downside of, all the overhead in the SDK still existing, so you're not filtering before you're doing the expensive operation of, like, going through all the attributes, making sure that they are all okay in terms of limits, and potentially allocating more strings, because you're truncating stuff and things like that.
So what I would suggest to sort that is that we change the… Implementation of the… block record.
itself to… Only do these checks on the attributes once.
They're, once they're accessed.
So, if you're doing, like, a filtering log workout processor like this, you would be able to just check the severity number.
And access that, you're never touching the, the attributes at all.
They don't get, checked.
And then you could basically drop it beforehand. That's the general idea.
**Jackson** 37:20 Yeah, thank you for explaining, Mark. My apologies for the microphone problems. I was installing Zoom on a new computer today.
**Marc Pichler (Dynatrace)** 37:34 So I think what we're here… I'm sorry, for not making it clear that I'm, not exactly sure what to do yet with this PR.
So, now you did a bunch of extra work, and I'm not sure if we can merge it as it is right now.
**Jackson** 37:50 Oh, I see.
**Marc Pichler (Dynatrace)** 37:51 But, yeah, I was, I guess, just really… Confused by the specification, because there's also these, the go-seek who had similar concerns as I did with the added interface of, like, basically doing the same thing again.
**Jackson** 38:14 Yeah, is the current concern with the log record processor implementation just a performance problem?
**Marc Pichler (Dynatrace)** 38:23 I think it's the performance problem, and also, Since it is not a specified component.
We… I'm not sure if we would put it into the, block.
record, in the logs SDK packager, if we would move it.
trip.
Where it would be its, like, separate package for, you know, log filtering and stuff like that, which then, of course, makes it a bit more difficult to configure. And then, also, there's the question of the declarative config, which… might allow people to define, like, a logger config that does exactly that. And then we have to, like, kind of make that fit somehow. So I guess there's a bunch of open questions, depending on which route we're gonna take that we will have to answer before actually merging that.
So… Yeah.
I was just hoping that, yeah, if anybody has any… other concerns and stuff like that to, mention it on the PR, You know, if there's, a lot of… new stuff. I guess we can also just skip the discussion for now and keep… have it on the PR. I was just wondering if anybody has any opinions right now.
**Trent Mick** 40:09 I feel bad, I want to have opinions, but I'm not there yet.
So, like, I totally should not hold anything back.
That just sucks.
**Marc Pichler (Dynatrace)** 40:21 Yeah.
I guess for the filtering stuff itself, Would we be opposed to having that as a country package, in case we want to have that unblocked?
I guess it's an easier question than, which route to take immediately.
**Trent Mick** 40:43 Sorry if this is rehashing, we didn't do the spec route, or originally this PR was doing…
**Marc Pichler (Dynatrace)** 40:50 Yeah.
**Trent Mick** 40:51 configurator, but…
**Marc Pichler (Dynatrace)** 40:53 Yeah, exactly. It was doing the login configurator, and it says here, oops, where do we have it?
So, it goes into logger configurator, and then it says, modeled as a function to maximize flexibility. However, implementations may provide shorthand helper functions to accommodate common use cases and, Severity and trace-based filtering are one of the two examples that are given.
**Trent Mick** 41:28 Did you have a link to that, Go… that was pillored, or I can't remember, is GitHub handled that other issue.
**Marc Pichler (Dynatrace)** 41:34 Yes, that's in the second comment.
**Trent Mick** 41:37 Oh, okay. Thanks. Yeah, I'll get it there.
**Marc Pichler (Dynatrace)** 41:41 Yeah, thank you. So… Yeah.
Interestingly, there's also this configurator for metrics and traces, if I understand correctly.
Which we also haven't implemented yet, and this is also an experimental.
Where we would probably have to answer similar questions, They don't have this, extra specification on the shorthand functions.
So… It's a bit easier of a case to make that we're just not gonna implement that there.
for this one, there is, definitely some merit to, Implementing it as a local configurator because of these performance things.
But anyway, if anybody has time, I would appreciate you having a look. I just don't think I should make the decision here myself, on my own, to… Cool, either.
One way or the other.
I think having some more discussion on it would be helpful.
But thank you very much.
**Jackson** 43:06 feedback, too.
**Marc Pichler (Dynatrace)** 43:08 Yeah, thank you for, Also, addressing this and changing it, so that we can see how that would look like, with the filtering log record processor.
**Jackson** 43:19 Yeah, I figure I always have the, the old hash, so… No worries if folks change their mind and want to go back.
**Marc Pichler (Dynatrace)** 43:26 Yeah. Alright.
Guess we'll let that sit for a while, and then… We will get back to this one.
Alright.
then I guess we could move on to… I'll trip the arch triage.
Right.
So I see there's a few PRs that haven't had any, movement here.
So let me skip over these, the web exception instrumentation, I think, has been Revived and has had some, movement recently.
Looks like Jared already approved this.
So, this is now waiting for us, for some more reviews.
Nope.
Sign myself here.
See if, I can help them get unblocked.
But, yeah, if… I know myself that I had requested Another review… Oh, looks like… Can't seem to find the button to dismiss my own review, so I just re-request review from myself.
Because that was mostly related to the, component holders, which they have, added here, so…
**Jamie Danielson** 45:41 I think the bottom of the PR, right above the, like, status checks or whatever?
There's an option for dismissing your review.
**Marc Pichler (Dynatrace)** 45:52 Yeah, I think it should be here somewhere.
**Jamie Danielson** 45:55 I'd make it up.
**Marc Pichler (Dynatrace)** 45:55 It usually is.
I'm pretty sure it usually is here. That's where I was looking for it before, but…
**Jamie Danielson** 46:03 Huh.
**Marc Pichler (Dynatrace)** 46:04 Maybe just some, inconsistent.
**Jamie Danielson** 46:10 Never know.
**Marc Pichler (Dynatrace)** 46:12 with the top.
Right.
**Jamie Danielson** 46:20 Oh, that's the one I was looking at.
**Marc Pichler (Dynatrace)** 46:25 I guess we haven't had any… Progress on this one yet.
Yeah, this is, Environment for everyone.
**Jamie Danielson** 46:39 Can you actually assign me on that?
**Marc Pichler (Dynatrace)** 46:42 Yes.
Thank you for looking into it.
**Jamie Danielson** 46:50 Thank you.
**Marc Pichler (Dynatrace)** 46:58 I guess usually, I guess our, our, Component bonus file is outdated as well, because we had, Auto-instrumentations note assigned to all the maintainers before, so… That's why it doesn't show up on the SI Need list as far.
And the next one… It's this one, I was on vacation, so I didn't have time to… do this here yet.
Let's see if there's a single triages… Or it's just blue.
Couldn't work. I'm just… And then, I would just add this here. So, essentially, what's, going on here is this is being updated to the, Latest semantic conventions for messaging, but… They aren't stable yet, so we can't use the stable.
Thing in… other, same kind of stability opt-in, I opened this issue and talked with, Wow, about it.
And, he marked this as… ready, so I can just… issue a PR to add this new thing, which would then have, like, an experimental opt-in.
For that, and then we can probably keep that PR as it is right now.
But instead of using that, we just use this other value, and we'll be able to merge that in.
Alright, so the next one is, AWS Lambda SQS Context Propagation.
Seems like there's been quite a few… Comments up until last week.
Looks like, just due to the RAWS SDK instrumentation deeps.
Currently have implemented context propagation through message attributes.
I guess this one is waiting for Jonathan's… Response… I'm just gonna check if there's… keep getting lost to the apps that I have here, Quested.
Famous.
Trust.
Maybe this was in a SIG meeting or something like that.
I will, also, put this in my notes.
I'll try to… See, what the current status on this is to get this unblocked, if possible.
Otherwise we can also wait for Jonathan's response on that one.
And there is link chain instrumentation.
It's a new package, and I haven't had the time yet to… Look into that… in detail.
We have… practice cluster Instrumentation support… Let's ask if Amia maybe has some time to look into this.
And it seems that… I'll see this also… a component owner.
Alright, then… this one… Has had some trouble with, NPM.
6 weeks.
**Trent Mick** 52:56 That one's on the go, we'll get that.
Figured.
**Marc Pichler (Dynatrace)** 53:00 Yeah, thank you.
Then this one here has owner approval, actually.
So… Where some failures… I'll update this one to see if they're still there.
Oh, that seems like the latest… Which was working out?
Once that's done, we can merge this one in.
Oh, this is the… Lang Chain Instrumentation, initial package skeleton, which is the way that it's… we should do it based on the guidelines to make the PRs a bit more reviewable.
Seems like there are two people that are… Suggesting themselves to be component owners, which is great.
Temples are already, members of the org, so… I guess.
If anybody has time, please review this PR over the… -Oh.
Over this one here.
Unless that would be a bit easier to get started with.
Alright, this one I said that I was going to look into, but, was out of office last week, and didn't get to it yet.
It's really just missing the, Starting this up and testing it out. But overall, it looks good already.
As always, if anybody else has some time to review these, I would also appreciate it.
As I don't get to all of them, usually.
**Trent Mick** 55:27 And Martin, you're here, so… yeah, question, if you scroll down to the bottom.
**Jamie Danielson** 55:32 and, like.
**Trent Mick** 55:33 So, setting… One, okay.
**Jamie Danielson** 55:37 We can put it, like, at the top of the agenda for next week, just… I don't know if we have one next week.
**Trent Mick** 55:42 No, no, no. No, no, no, I'll just… I was just gonna take the opportunity, given that we're on the call, but we can… discuss on the thing. I think this one's basically ready to go, there's just a thing worth… that… my question there, it's doing set context info with at OpenTelemetry underscore trace parent. The spec says to use just at trace parent, but I'm not sure it matters. I don't know if this is something that just disappears in the query.
And… It doesn't matter what that variable name is, so… That's probably fine.
If all the Microsoft SQL experts could stand up and…
**Jamie Danielson** 56:23 Comment on that, that'd be great.
It's been many a year.
**Trent Mick** 56:31 It's been no years for me.
Ever.
**Marc Pichler (Dynatrace)** 56:37 Yes.
**Jamie Danielson** 56:39 But yeah, so I just realized that I think next week is KubeCon in North America. I don't know how many people are… going. But I don't know if we are still holding… the SIG meeting next week, or not.
**Trent Mick** 56:56 Yeah, we'll see. Sometimes they just call it general pause.
**Jamie Danielson** 56:59 That's true.
**Trent Mick** 57:00 We'll see.
**Marc Pichler (Dynatrace)** 57:03 Any preference? .
**Jamie Danielson** 57:06 I'm gonna be around.
**Trent Mick** 57:09 Yeah, I'll be around too.
**David Luna Bistuer** 57:11 Me too.
**Marc Pichler (Dynatrace)** 57:11 birth.
around at KubeCon, or around,
**Jamie Danielson** 57:16 meeting. I'm not going to CubeCon in Atlanta.
**Marc Pichler (Dynatrace)** 57:22 Alright, I will also be here, in the SIG meeting, so, I guess we could still do it, and… see if… Anybody joins, and if there's no agenda items, we can also skip it then.
Does that sound okay?
**Jamie Danielson** 57:45 Yep.
**Marc Pichler (Dynatrace)** 57:48 Alright.
I guess we're pretty much out of time for today, anyway. So thank you all for joining.
I have a nice… week, or two weeks, depending on if you're going to KubeCon or not.
And see you then.
**Trent Mick** 58:09 Cheer. Thanks, mate.
**Marc Pichler (Dynatrace)** 58:11 Right.
