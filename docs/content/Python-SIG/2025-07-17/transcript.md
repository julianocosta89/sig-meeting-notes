SIG: Python SIG
Date: 2025-07-17
Duration: 54 minutes
Zoom Recording URL: https://zoom.us/rec/share/6Z0vE2xTsRAspMld9FyjHZEWVa75-wY7vFyWSQiF7YoxS3ePdCsMjjZ5NyIK3G0S.FYbeQcWKrJuJb_F3
============================================================

## Zoom Recording Transcript

**Pablo Collins** 04:52 At all, not seeing any evidence that this meeting is happening.
There's no entry in the signets for it.
We have somebody.
How many Maintainers are gonna be joining this meeting today.
**Emídio** 09:04 Yeah, seems so. I'm not sure if it's any holiday.
I don't think so.
**Pablo Collins** 09:13 Sorry. What was that? Emilio.
**Emídio** 09:15 I'm not sure if it is happening any holiday on like record that that hikado lives.
**tammy.baylis** 09:33 Yeah, I didn't see anything on slack, either.
I don't think it's a holiday in the U.S.A. Today.
**Jeremy** 09:48 Layton did say yesterday that he was really busy with something. Maybe maybe he can't make it. I'll I'll message him.
**Pablo Collins** 10:22 Well, does anybody have any topics for today.
**Emídio** 10:31 Oh, by the way, Jeremy, do you want to talk about?
Your Pr.
**Jeremy** 10:37 Yes, I can. I can do that. Give me a second to get set up.
**tammy.baylis** 10:50 Just thanks to you, Pablo, for looking at my exporter pr this week. That's been really helpful.
**Pablo Collins** 10:58 Yeah, my pleasure. Thanks for doing that, Tammy.
**tammy.baylis** 11:00 Yeah.
**Aaron Abbott** 11:47 Everyone. How's it going.
**Emídio** 11:52 Hey!
**tammy.baylis** 11:54 Hey? Erin.
**Aaron Abbott** 11:55 Sorry I'm late. Looks like we didn't start Were there any agenda topics today, or.
okay.
**Emídio** 12:06 I don't think we have too many topics. I would suggest to talk about. Jeremy Prs society was reviewing.
**Aaron Abbott** 12:18 Jeremy, would you wanna talk about that today.
**Jeremy** 12:21 Yeah. Just getting getting everything set up. I'll share in a sec.
**Aaron Abbott** 12:26 Okay, great I'll let you share your screen. But everybody else, if you could just add.
you know, attendees, and if you have any topics.
**jeremyvoss** 12:41 Alright! Can people hear me? Sometimes my headphones get messed up.
**Aaron Abbott** 12:45 Yeah, I can.
**jeremyvoss** 12:47 Okay, cool.
Right here we go alright. So I think this, I think this Pr has made a good amount of progress. I think it's pretty close to to being closed. But there's some some things we kind of need to agree on. Thanks to everyone who's who's provided feedback. I know it's like a pretty big Pr, and it's it covers some kind of complicated use cases that may not apply to everyone. So appreciate the the patience and input. I think the last thing that remains is this discussion with Rj and and sorry I I the username looks a media right?
basically, there's this method within instrumentations that can be overwritten. That's instrumentation dependencies. And it just it just returns a list. It doesn't do the dependency check itself.
And basically as of right, like, given, given the fact that we're adding this this either, or list in addition to the and list. It's a bit unclear what this method should do now in my in my head. So I think what we can do is just make this change non invasive, and just have it return. The same return. The same thing that it is currently so currently it actually doesn't use those. It actually doesn't use instruments or instruments any. It really just checks like manually for it's just overwritten and like for Kafka and Psychopg 2. That's kind of the same thing. Checks for a given given package and just returns the package restraints on for that given package.
And then, if neither are present, which obviously would mean that the instrumentation shouldn't happen. It currently returns the list of both.
The default case, in my view, doesn't quite matter too much, because if it is returning the default case like we, we shouldn't instrument, anyways. So it's it's kind of strange to return something.
But what I can do is just change this to instruments any which is the new list of the 2 of them.
And yeah, I guess I'm wondering. Media, what do you? What do you think of that? Would that kind of solve this problem. It was a bit hard tracking what what you and Rj, were.
we're saying here, and exactly what you were suggesting for me.
**Emídio** 15:57 Yeah. I did some tests on your Pr.
And realized that if we return like a only instruments any.
we will break the main instrumentation path like I said it in my comment, like.
**jeremyvoss** 16:15 I thought you were saying that it it does work. Okay.
**Emídio** 16:19 It does. It does work, if you will just return like instruments like it or nothing, you know.
**jeremyvoss** 16:26 But the wait, but the current, the current the current behavior of returning instruments is equivalent to the new behavior of returning instruments. Any, because the current value of instruments is both packages and the new value of instruments. Any is also both packages. So how could one break and not the other?
**Emídio** 16:47 The breakage is because in the during the check we are not passing like the depths any.
**jeremyvoss** 16:55 During the check. We're not passing the website. Let me let me see.
**Emídio** 17:01 Like in the instrumentor.py.
we are checking only the depths, but when you pass that we didn't pass any, it's not the same format like it won't be a or it will be an end.
**jeremyvoss** 17:21 Are you talking about this here like? What? What uses this.
**Emídio** 17:28 Can you? Can you go back to the comment.
**jeremyvoss** 17:33 Yeah.
**Emídio** 17:35 In my comment in in my comment before the one you did like.
**jeremyvoss** 17:47 This one.
**Emídio** 17:47 Yeah. Click on. Yes, please.
On on the 1st link. Yeah.
**jeremyvoss** 17:56 Okay, digitally, as opposed.
**Emídio** 17:58 Nope, okay.
**jeremyvoss** 17:59 Okay.
**Emídio** 17:59 So, even if we pass the instrument is any, it will be treated as a end.
**jeremyvoss** 18:09 Yeah, that that makes sense to me. But ultimate, this is just a list. Just a list of 2 values are, are we talking about?
okay, so there's 3 cases here. There's off. The python. Ng is installed, or or both of them installed. It would. It would go here either way.
in which case we'd return the Ng list, which I haven't changed, or Kafka, Ng, isn't installed because Python is we return this or neither are installed, which is the default case. Are we talking about the default case? Or we're talking about one of these.
**Emídio** 18:49 I'm talking about returning, both of them.
**jeremyvoss** 18:54 Returning, both of them. So the default case, where neither are installed.
**Emídio** 18:57 Yep.
**jeremyvoss** 18:59 Well, I mean, if neither are installed, the dependency check should fail.
**Emídio** 19:09 Hmm!
So I think that's there's something wrong.
I can create a reply script and send to you.
**jeremyvoss** 19:22 Okay. Okay.
**Emídio** 19:23 We can vote it together.
**jeremyvoss** 19:25 Alright. That'd be great, I think. I think, if anything what I'm what I'm doing right now, because I haven't changed this value is this value used to return both and it would fail because both are not installed.
like, that's the current. That's the current behavior. Right now I'm returning 0. Which or right now, I'm returning the same value. But this value has changed.
It's become an empty list or an empty array.
Which probably means that the dependency check would pass. So I wonder if what the problem is? Actually that it's passing when it shouldn't pass.
in which case I think it would be solved by instruments. Any but yeah, send me your repo script, and I think it'd be easier to to figure it out.
**Emídio** 20:15 Okay.
**jeremyvoss** 20:17 Alright, cool.
**Emídio** 20:18 Finger in his life.
**jeremyvoss** 20:19 Alright awesome.
I think. Is that the is that the last bit here?
Oh, I guess I guess one thing I'm wondering is so that's the scenario where neither are installed. Have you tried the scenario where either installed? Does that work.
or do you think that might be broken, too.
Feel like it should work.
**Emídio** 20:42 Yeah, it should work.
**jeremyvoss** 20:44 Okay, alright cool. Yeah. Just send me the repro we can. We can talk about today.
Any other, any other thoughts on this? Pr, yeah.
**Emídio** 20:59 Nope, I would just take another look on the test to see if you are missing something from the previous pr, like, we removed a lot of tests.
**jeremyvoss** 21:09 In the other. Pr.
We moved. Say that again.
**Emídio** 21:13 In the Apr that actually did, we removed a lot of tests. So I would just check if I'm missing something.
**jeremyvoss** 21:22 Yeah, I think a good amount of them, I added back.
there are a lot of tests added added into this like this thing here. And yeah.
yeah, I can. I'll go over that one more time. See if see if there's any tests that I missed, adding back.
**Emídio** 21:48 That's fine!
**jeremyvoss** 21:51 All right.
Okay, I think it's I think it's it for me.
**Aaron Abbott** 22:01 Okay.
Great. I don't know if I'll have.
Don't sure.
**jeremyvoss** 22:07 There you go! Can you stop screen sharing.
**Aaron Abbott** 22:10 So.
**jeremyvoss** 22:11 Do you just say pause, maybe I can changed.
Okay, feel free to take it.
**Aaron Abbott** 22:20 I can't. I can't. Yeah, that's okay. You can just keep sharing this.
No. So I was, gonna say.
**jeremyvoss** 22:26 There you go. I see it. Okay. Got it.
**Aaron Abbott** 22:30 Okay, I'm not sure if I'll have a chance to review that anytime soon. But yeah, thank you, Amidio, for the for the good review, and I hope you guys can work that out. Alright, I think we have Anita. Did you want to talk about those fixes to do after release, or did you wanna just just a quick call out, I couldn't share.
**Emídio** 22:55 Yeah, I think I just to state those 2 issues that appeared after the release that is pretty much related to the change we did recently, like in.
**Aaron Abbott** 23:07 Yeah.
**Emídio** 23:08 Deprecating things, and mostly in the logs. SDK.
**Aaron Abbott** 23:13 Yeah.
**Emídio** 23:14 Oh, I didn't look too deeply on them, but I'll take a look later to see if we can provide a quick fix.
**Aaron Abbott** 23:25 Okay? So this one, I think the init function which one are we talking about? That's we edited to match the new deprecation warning.
That's probably true.
Yeah.
So I guess this code is triggering it from within the event. Logger. They pull it.
**Emídio** 23:48 Yup!
**Aaron Abbott** 23:51 And yeah, Dylan, are are you around? Do you have any any thoughts on this one.
**Dylan Russell** 24:00 Sorry. So it's which warning is it? Triggering.
**Emídio** 24:07 But sorry one like we are passing. Trace id and spin id set of context.
and we are emitting deprecation wirings at one time.
But since we didn't update here, people are getting this warning.
**Aaron Abbott** 24:26 Right. I think this is actually I'm sorry. I think this is Tammy's Pr. Or maybe.
in any event, like, I thought we also deprecated the the events.
**tammy.baylis** 24:39 Yeah, they should be using the the logging Api instead of the event. Api,
**Aaron Abbott** 24:48 Yeah, it's awesome.
**tammy.baylis** 24:49 And we we do have instrumentor Prs in progress. Now, following this last release that are going to do the switch.
**Aaron Abbott** 25:04 Right.
I think there were some subtle small issues also related to, like the resource for the using the Api directly for the instrumentation. So I don't know if we're blocked on that one.
I'm not sure if we have a bug for it, either.
**Dylan Russell** 25:20 Yeah.
I opened a bug, but I wanted to talk about that a little bit.
Okay.
**Aaron Abbott** 25:33 Okay, well, I mean this, yeah, this one seems like a small change. Maybe we should just fix it.
What do y'all think.
**Emídio** 25:42 Yep.
**Dylan Russell** 25:43 Yeah.
**tammy.baylis** 25:44 Yeah, that sounds good.
**Aaron Abbott** 25:46 Okay, Does. Anybody have time to take this.
**Emídio** 26:10 Yeah, okay, I can take a look.
**Aaron Abbott** 26:13 Okay, I think we're not assigning people bugs anymore. But I do. I do think you would. You would handle it if I decided to. But you know, I'll just tag you.
Okay, yeah. And feel free to ping me if you need review, it should be a really small one.
Okay? So then, this is the second second one. Right?
**Emídio** 26:38 Right? Right? This is basically another case. I believe another case of recreation when we are emitting logs.
And yeah, I think we fix it. Something related a few weeks ago.
Less release, I guess.
**Aaron Abbott** 27:05 Yeah.
**Dylan Russell** 27:09 Yeah, we removed that. We fixed it the other time by just removing the log.
**Emídio** 27:18 Yes, it was a long term solution.
**Dylan Russell** 27:22 Right.
**Aaron Abbott** 27:24 So this is this related to the release, though because it seems like not like a new long message.
**Dylan Russell** 27:32 No, I think this one has been here for a while.
Okay.
**Aaron Abbott** 27:37 I thought we removed all the places that we were next.
Oh, I see this is the exporter.
**Dylan Russell** 27:48 Yeah.
**Aaron Abbott** 27:51 But they they must be using.
They are using the batch processor. Okay.
**Dylan Russell** 28:03 We'll yeah, either way. Do we want to remove the log or.
**Aaron Abbott** 28:09 Yeah, I don't. I don't think it's a sustainable thing. We gotta.
I think we need a longer term solution because it's just too brittle and like. The logs seem really useful, especially from the exporter.
I prefer to keep them.
**Dylan Russell** 28:27 Right.
I kind of forget, if we can, how else we would fix this we can.
There's some way to turn off like propagation to the root logger. Right?
**Aaron Abbott** 28:51 We could do that like we could divert the logs, so they never go back to the hotel handler. But I'm I'm still a little confused how this is happening in this bug, because if you do.
they set up the SDK with the Batch processor, and then the Batch positors calling export. And then it's potentially in queuing. I don't understand why that would pause an infinite loop. Maybe maybe they mean.
let's see, I can't. Yeah, yeah, go ahead. Sorry.
**Dylan Russell** 29:24 I think, trying to write the log results in that failure message which then, like that, turns into another log.
**Emídio** 29:39 Yeah.
**Dylan Russell** 29:42 So it's not the recursive loop, right? It's just it just.
**Aaron Abbott** 29:46 Yeah.
**Dylan Russell** 29:47 Is it infinite loop? It's just tries to log forever. It just keeps logging.
**Emídio** 29:52 Yeah, yeah, right.
**Aaron Abbott** 29:52 That's yeah. I'll try to clarify, because here, it says, expected result. Not quite sure, at least not any application that is stuck in this infinite loop. So it sounds like it's hanging right?
I don't know. Let's get some clarification, because I think the latter is expected, because, otherwise.
You know if it's a transient error, you would want to see those logs right, whereas it's a.
**Emídio** 30:18 I think it's It's the same case as this issue. Let me share in the notes.
**Aaron Abbott** 30:27 Okay.
**Emídio** 30:29 I paste a link in the in the notes.
which I believe is a similar case.
**Aaron Abbott** 30:40 Okay, it's actually going to be the longest for login procession.
**Emídio** 30:44 I believe it's the same case.
**Aaron Abbott** 30:47 Yeah, this looks like the same case.
**Emídio** 30:51 Oops!
**Aaron Abbott** 30:55 Okay, I'm I'm still a little confused how this is possible, based on my understanding of the code. But button, I guess.
Yeah, is anybody have to have time to look into this one.
**Emídio** 31:17 Like. What I understand is, we failed to export logs, and we meet a log with error.
and we start a loop again to export, and we keeps in that loop forever.
**Aaron Abbott** 31:34 Right, but is it.
**Emídio** 31:36 That's okay.
**Aaron Abbott** 31:36 Or is it? Is it just.
**Emídio** 31:40 Desire to the new loop.
What I understand is, it's at least from what I remember from that issue.
It's like we never stop till he try.
**Aaron Abbott** 31:57 I mean to me that that doesn't. That seems kind of expected. Like, I, I wouldn't be okay. I double check and change to simple.
Okay, I I guess I could try to take a look at this one. Maybe I can take a look tomorrow.
**Emídio** 32:31 Yeah, I think I have a heapro for this one I sent to Dylan some time ago.
when reviewing his Pr. I can send to you.
**Dylan Russell** 32:43 Yeah, I think the other solution I was thinking of, for this is like filtering out if we see it like, if we see the same log again, somehow filtering it from going to the root handler.
like, I think there's a way to add a filter to the to the login module.
Yeah, that I could. Yeah, I'll share that approach, maybe in the bug. And we can talk about it.
**Aaron Abbott** 33:20 Okay.
**Emídio** 33:21 Okay.
**Aaron Abbott** 33:22 Yeah, my kind of concern with that kind of thing is like.
it seems sensible in this case. But then there's there's times when people will be like, Hey, this is swallowing my logs.
There's this replacement log, or whatever. But maybe we could scope it to just the Otlp exporter.
**Dylan Russell** 33:39 Yeah, yeah, that's a good point just to fix this bug.
**Aaron Abbott** 33:46 Okay, So I'll I'll wait for a plan here. Like I I still, it's still not really clear to me what the behavior is because nobody's sharing like the is it stack overflow? Is it just the logs repeating.
It sounds like immediate. You had a repro, and it was the latter. It was just the log repeats indefinitely, but it wasn't like a.
**Emídio** 34:10 Yeah, now it's it. To me it seems like to be more related to the repeated the logs, and not a a recursive infinite.
**Aaron Abbott** 34:27 Yep, which is good.
Okay.
alright. Any other thoughts on that one.
So just wait for the reply.
Okay, So let's move on. Then, Redeemah, is that you? Are you on the call.
**Ridhima Satam** 34:53 Yes, I'm here.
Okay, if you can open already, you're sharing right? So we don't have much to show. But this is the Pr. For the Langshon instrumentation support. We are going to start adding, and it's just the 1st Pr with the skeleton files, and I'm still circling back couple of times like last in the Llm. Sig. And this Sig. So it must be repetitive, but it's been looked at by a couple of people, I think. Pablo looked at it, and I got approval from Ludmilia, but I need approval from the Maintainer, so just that.
**Aaron Abbott** 35:33 Okay, so a couple of questions.
Firstly, I'll just take some notes here.
Did. Were you able to get in touch with near from Traceloop regarding the package name.
**Ridhima Satam** 35:44 So I contacted him on the slack channel. The Hotel Gen. AI Channel. I haven't received any feedback from him yet, so I'm just planning to drop drop a personal DM to him. So let's see what he says. But I don't see it online yet. So that's why I'm waiting for that. But regardless of that, we can come back and change that again right? Even if this gets mulched before the release or something.
**Aaron Abbott** 36:13 Well, I mean we can't like we can't release it if we
**Ridhima Satam** 36:17 Yes.
**Aaron Abbott** 36:18 If we do merge it so it would. It would be nice to have some clarity on it, I mean, I guess. Yeah, we could, we could merge it, and then the release will just fail if somebody tries to do it. But if if you could DM. Near and get some feedback and maybe have him drop a comment that he's okay with the the shared, naming thing, and I can work out the the pipe stuff behind the scenes with him.
I think that would be.
**Pablo Collins** 36:44 How does how does the release part work? Because we wanna just we wanna have this be living in this repo for a little while and not have it be released like we wanna merge a skeleton implementation and then add some features, and then once we're happy with it, then release it.
**Aaron Abbott** 37:05 Yeah. So if so, that's what we've done for the other. Gen. AI. One. So my, the 1st thing would be, let's not add it to Bootstrap. Jen, just leave a comment.
**Emídio** 37:15 Yeah, I was. I would say that.
**Aaron Abbott** 37:19 Let's see.
**Emídio** 37:22 I think we need to put the instrumentation on the ignore list.
**Aaron Abbott** 37:28 Yeah. Do you know where that is?
**Emídio** 37:31 It's a the scripts folder.
We have the file which generates the bootstraction. We need to append.
**Aaron Abbott** 37:41 On that list.
Okay.
**Emídio** 37:42 I can point it out.
**Aaron Abbott** 37:44 Yeah.
Do you happen to know the path? Maybe I can just get it here.
**Emídio** 37:55 6 contribute scripts.
Yeah. Left a comment on that line.
**Aaron Abbott** 38:23 Are you the one on the on the Pr.
**Emídio** 38:27 Yeah, I left a comment on those girls.
**Aaron Abbott** 38:29 Okay?
And then yes, I think there's there's probably a couple more steps to make it do the independent releasing. I will follow up on the pr, but the gist of actually doing the release is in here. So there's these. Alright, we have.
we have instructions, for, like, you know, regular releases that the maintainers do. And then it says, per package releases supported by these packages only.
And then there's a separate workflow that these that can be run for these which right now is just. I think the Maintainers would still be the only ones with access to run this. But you can just reach out when we're ready to do that, and it doesn't require releasing anything else. But we should add to this list also.
since.
**Pablo Collins** 39:24 Are you sharing something?
We're just seeing the city notes being shared.
**Aaron Abbott** 39:32 Oh, I'm sorry.
It's probably my bad. I thought I was sharing this one.
Okay, that was weird.
Sorry I was trying to share this? Can you see that now.
**Pablo Collins** 39:57 I am only seeing sign notes. What are other folks seeing.
**tammy.baylis** 40:00 I'm also seeing the save notes.
**Aaron Abbott** 40:02 Okay, that seems like a bug. Hold on.
Alright. Can you see this file now?
**Pablo Collins** 40:16 Yes.
**tammy.baylis** 40:17 Yes, thank you.
**Aaron Abbott** 40:19 Yeah. Sorry about that. So this one we could. It's very manual process right now. Unfortunately.
See.
just drop a link there. There's probably a couple more steps, so I'll follow up.
But yeah. One other question I had was, do we opt into type checking for this package.
**Pablo Collins** 40:48 Yeah.
**Dylan Russell** 40:50 But we can look at it.
**Aaron Abbott** 40:52 Yeah.
that would be my strong preference. Just because I found it.
I would like to have it turned on by default for new stuff and just opt things out. But we'll share a link to that just makes it a lot easier to maintain. Sorry, where's the pr.
yeah, I'll take a look at this. Pr.
and yeah, thank you for the contribution. Did you have anything else you wanted to call out in here?
**Ridhima Satam** 41:42 Oh, no, that's all.
Thank you.
**Aaron Abbott** 41:47 Okay.
Great.
Okay, Timmy. I think you're next.
**tammy.baylis** 42:00 Yeah, thank you. Just to call out, it's pr I've had out for a while now, and let's add a Max export batch size to the Http. Metric exporter to match with the Grpc. Version is already doing. I've already had reviews from Layton and Pablo. Thank you for that. But I've made more changes, so it'd be good to for someone to have another visit, and it's just a shout out. So so I wanted to say, thanks.
**Aaron Abbott** 42:35 Okay, great looks like Paulo, you approved. So maybe we can just get that's weird watching it show.
**tammy.baylis** 42:46 Oh, I see!
**Aaron Abbott** 42:46 Be real quick.
**tammy.baylis** 42:47 I might have dismissed it because of one small change to change the final success. Return?
Yeah, that that one.
Okay.
Sorry. Sorry. I dismissed it. Pablo.
**Pablo Collins** 43:03 No no problem.
**Aaron Abbott** 43:06 Okay, cool. If Leighton's not able to take a look you can just ping me on slack. And hopefully, we can get this in been open since may.
**tammy.baylis** 43:16 Thank you.
I will also be off for a couple of weeks, so I we'll probably probably come back to it when I'm back.
**Aaron Abbott** 43:28 Okay, that sounds great.
Alright. Last one here. Dylan.
**Dylan Russell** 43:37 Yeah. I had a question on this Pr removing, which is removing log data.
Hector, are you on the call?
Who you there, Hector?
**Aaron Abbott** 44:02 Maybe.
**Dylan Russell** 44:06 Yeah, I'm wondering.
Yeah. My main concern is, we have like 2 log records right now, we have, like the Api one and the SDK, one and this pr, it updates the SDK, one to include instrumentation scope.
But I'm wondering if we should instead.
**jeremyvoss** 44:33 Yeah.
**Dylan Russell** 44:36 Potentially remove the SDK log record entirely and put have, like a have log data like we had with the Api log record instrumentation, scope and resource.
or we can call that whatever whatever name you want to give that but just a data structure with those 3 things.
Because I think, yeah, I think that's all we need in the SDK,
**Aaron Abbott** 45:22 Yeah. Was there any discussion on this Pr already about the do you leave a comment on here, or get any feedback from Hector?
**Dylan Russell** 45:34 Yeah. I added a few comments.
And yeah, Hector replied, about the name.
I'm okay with whatever name we want for this data structure. But I'm not sure what Hector thought of just of there being just 3 fields on the on it.
**Aaron Abbott** 46:00 alright, there's a little discussion in slack here, so hector says, mike issues, sorry comments haven't just reply, we didn't make sense. I'm fine updating to Dylan's suggestions.
**Dylan Russell** 46:11 Oh.
okay.
Cool.
**Aaron Abbott** 46:18 Yeah. And I can add a little more context here, if it's helpful. So we have like a oops.
I think, for span exporter. We have this kind of flat structure. So the export takes just a list of readable span.
And the kind of weird thing about it is it doesn't really look like the Otlp data model.
And so so everything is kind of flattened here, right?
And we're just reusing some of the the stuff from the Api and sticking it here.
So for metrics, I think what we did was we want maybe more similar to Java, but also because metrics, the Api and the SDK have, like very different data structures.
We did this thing. Where is it? Metrics, metrics, data?
That's not the right one. Sorry, it's actual protocol.
You did metrics data.
It's in this file.
I think this has pretty much all the stuff. So so these look very similar to the protobus. And they're just kind of stupid data classes that are frozen. So they're immutable.
**Pablo Collins** 47:38 And
**Aaron Abbott** 47:39 The the kind of nice thing about it is from the Otlp exporters perspective. It doesn't. It doesn't have to re-aggregate anything. And if you're copying the logic from like a collector exporter, or something like that.
Pretty much looks like the data models we have. You know, the top level resource metrics which has resource, scope, blah, blah, blah!
And then, as we add stuff like scope, sorry schema, URL, and stuff like scope attributes, they can just kind of be added here, instead of having to make that one flat object wider. So I kind of like the logs data approach and make it look more like the Otlp myself.
and keep the the Api and SDK data model separate. But that's kind of the context.
are they?
**Dylan Russell** 48:29 It's cool.
**Aaron Abbott** 48:32 Alright anything else on this one.
**Dylan Russell** 48:37 No, not for me.
**Aaron Abbott** 48:40 Alright.
Oops awesome. Well, we've got about, you know, 15 min to spare, so if anybody has something last minute, call it there.
**jeremyvoss** 48:51 Just an update media changed the code so that it should be the same behavior as before.
yeah, let let me know if the new version works and send me a repro, so I can test it too. But this is basically I realized that by not changing a certain variable. I was actually changing the value. So I changed the variable, kept the same value. And I think it should be the same as before. But.
**Emídio** 49:20 Sure, I'll take a look.
Thanks.
**jeremyvoss** 49:23 Cool.
**Aaron Abbott** 49:28 Alright. Well, thanks for joining everyone good to chat and see you next week.
**Emídio** 49:33 Thank you. Thank you.
**Dylan Russell** 49:35 Moment. Bye-bye.
