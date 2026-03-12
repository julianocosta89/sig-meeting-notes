SIG: Client Instrumentation SIG
Date: 2025-06-24
Duration: 21 minutes
Zoom Recording URL: https://zoom.us/rec/share/Waecbqr1Hopz7x8g3MyOeXdhV_YHgMU1-giHm8dBUfPVT_YSMkZECk0KySXkt8yG.EQI_ulgUsJdxCThw
============================================================

## Zoom Recording Transcript

**Jason Plumb** 05:55 Hey? Just wanna say, Hi! There's other stuff I gotta chase down. I'm gonna drop.
**Dan Gomez Blanco** 05:59 That's okay. I do wonder if there's like this is, if people are at the hotel community an open observability con this week. I'm not sure if many people are going to be joining.
**Jason Plumb** 06:13 Yeah, I I don't. I'm I'm sure that there's a good contingent that's already out there, or is traveling. I'm traveling, or 1st thing in the morning.
**Dan Gomez Blanco** 06:22 So.
But yeah, sure, yeah.
So okay, I'll wait. See if we join. So if someone put some anything in the agenda, otherwise we can just and cancel this one.
**Jason Plumb** 06:35 Cool. I'm gonna drop early. Thanks. Bye.
**Dan Gomez Blanco** 06:37 Alright, yeah. Bye.
**Abinet Debele** 06:41 Yeah, I think last week I heard that people were saying, they're not gonna come to this meeting, and also that this meeting is can is going to be like once in 2 weeks. I think.
**Dan Gomez Blanco** 06:55 Yeah, so I think, yeah. So yeah, so this week.
yeah. So maybe we want to start in the next week.
**Abinet Debele** 07:04 Oh, okay.
**Dan Gomez Blanco** 07:06 With that it hasn't been changed yet, so there is something probably the thing that I wanted to raise. Oh.
**Abinet Debele** 07:16 Okay.
**Dan Gomez Blanco** 07:17 I'll add a topic for the agenda today. So I wanted to raise something. But
**Abinet Debele** 07:22 Alright!
**Joaquín Díaz** 07:31 What's going on with the processing? I know we there is no meeting this Thursday as well, and they say that we may start on like doing something over slack, but I didn't read anything.
**Dan Gomez Blanco** 07:45 Yeah, so I'm yeah. So basically, this, well, last week it was Juneteenth and and in America, so like, none of us take leads or sponsors were going to be able to join that 1st initial meeting of the browser sake the second. So this this Thursday that's when it would be. The the second meeting also had to be canceled because of Hotel Community day. So the 1st meeting for the browser sake will be next week on Thursday.
Okay.
**Joaquín Díaz** 08:18 Thanks.
**Dan Gomez Blanco** 08:31 so I don't know if we've got enough quorum But, Leonardo, if you.
if you want to raise your question, maybe maybe none of us. I don't know if someone here would be able to to help. Compared to some of the like sick leads. I can definitely try. But yeah, we can talk about it, anyway.
**Leonardo Serrano** 08:54 Yeah, yeah. So guess I'll try to raise the question anyway. So I know that we have, you know, a larger effort to move away from the concept of span events.
in lieu of, you know, log records as events correlated with spans, so.
**Dan Gomez Blanco** 09:19 Yep.
**Leonardo Serrano** 09:19 My question is, and I don't know if anyone here can help with this. It's not necessarily a question of It's more of a semantic question. I don't know if anyone's put any thought into this. So there's an experience on back ends, collectors where, you know. If today I am expecting spans to have certain span events. Okay, well, now, if I need to separate them out into log records and ingest them as part of like, you know logs. Otlp.
there's a sort of a disconnect here if I today expect them to be in basically in the same otlp request. Essentially.
okay. Well, now, if we're moving away from span events, they're going to be in separate things. Basically, it's the problem of getting everything in one context versus getting everything spread out piecemeal, which for a back end is is a slightly more difficult thing to reason about, because then you need to start thinking about like, okay? Well, you know, caching distributed caches like, how do you quarrel? And something that happened at like T equals 0 with T equals one, because things are, you know, being ingested sort of not at the same time. Right?
So, yeah, I'm I'm wondering if anyone has put in in any thought into this.
**Dan Gomez Blanco** 10:57 Yes, so I linked a I think we we have talked about that in the spec meeting as well.
in. I think we even talked about that in one of the Governance Committee meetings as well, there is a duplication plan that is in the Otep that are linked in in the notes.
so yeah, so basically, that's after the the span events deprecation in favor of like log based events. Right? So I'm the the. So the the only thing that is planned to be deprecated is a span event, Api.
And while retaining the you know, the ability to emit span events via the logs. Api. So you will be still having the logs. Api, but will still be able to emit span events.
M.
With that, so there will be a long term deprecation plan for span events. I think you know, as you said, you know, one of the main concerns would be the I don't know in terms of tail sampling, for example, right? You not only have to have like something that can sample spans, but you also need to have something that can keep spans and logs for a particular trace and memory, and then sample them together right?
And so. There are many questions that still need to be answered on the on that side of things, but I think is, the idea is is more more full-fledged. Explaining that deprecation plan. There was a an action as well, communication plan of publishing a blog post.
You know, giving readers more ways of providing feedback.
I guess that will be that will be important as well, M.
So yeah, that hasn't happened yet, but it will happen. I think it's not going like span events.
We're not going away tomorrow, and the span events. Api is the bit that's replicated, but not the ability to emit span events via the locks Api.
**Leonardo Serrano** 13:06 Yeah.
**Dan Gomez Blanco** 13:07 Tends to like answers a little bit. Your question. I know that is probably not super like like concise or super, like specific, but But there are things still like the underlying transport. I don't think there's a plan to deprecate that at the moment.
**Leonardo Serrano** 13:27 Yeah, that's my understanding as well. I'm I'm speaking more from the perspective of someone who actually wants to migrate things away from span events to the log record event format.
it's just this caveat that like is preventing me from fully migrating where currently, you know, with span events, we have that expectation where you know spans, and the correlated events with them are sort of like maintained in memory in the same Otlp request instance. And now, if you start generating them as separate like log records via the logging Api, you don't have that guarantee.
**Dan Gomez Blanco** 14:11 There will be certain things that the SDK. Will convert to span events in the underlying otop that is supported, though I think that's the current plan. So the SDK should allow to basically transform or encode certain events, certain logs that are produced with the logs. Api as span events. That's my, that's my understanding of it.
**Leonardo Serrano** 14:41 Oh, really.
**Dan Gomez Blanco** 14:43 Yeah. So if you scroll down.
I know that I'm not sharing my screen. But yeah.
yeah, so is here, basically, which is the part of the deprecation plan. But if you scroll down to the bottom, that is, send in log based exceptions and events and span events.
and this should basically, there should be a should be a log processor that converts certain ones of those events into span events and attaches them to the current span, which, basically under the on the on the resulting otop, it will still be a span event attached to the span right and.
**Leonardo Serrano** 15:35 See you.
**Dan Gomez Blanco** 15:37 Yeah. So I think how that is done.
I think there's a prototype that I've not been able to to look into. But yeah.
The booby ways of doing that I don't know.
I've never seen this working, but I do think there is something that's been M.
I mean, this is a must right. So there must be a way to send log-based exceptions and events and span events for use, cases that we're allowing span events.
How that's going to be configured hopefully with the clarity config now would be a case to to do that. But yeah.
does that provide a bit more clarity? I guess.
**Leonardo Serrano** 16:23 I still have some questions, but I actually have not seen this specific, doc.
So I'll take a deeper look at this and see if maybe this Doc can answer some of the questions I have.
**Dan Gomez Blanco** 16:37 Sounds good.
And yeah, probably the the the best way to or the best place to answer this will probably be the hotel specification channel.
**Leonardo Serrano** 16:51 Sorry the which channel.
**Dan Gomez Blanco** 16:53 The slack channel, the hotel specification hotel, that specification that's got it.
**Leonardo Serrano** 17:00 Okay.
**Dan Gomez Blanco** 17:01 To ask.
**Leonardo Serrano** 17:04 Yeah, I'll raise a question there. Thanks.
**Dan Gomez Blanco** 17:06 No worries, and you know any feedback is I mean I I did have my my like concerns as well similar to yours on on this. So yeah.
And the feedback is good feedback.
M, yeah. The next point I want to raise is the I guess the the current.
the client side Sig, current projects and moving forward with the bi-weekly meeting. So the current project, if you go to the community, see if I can link it go to community projects, I'll link it in there.
this one.
Yeah. So as I linked in the in there, basically, the yeah. So the current, the current project has a set of deliverables in it, and then we need to in a project board, and we need to decide how to close this project with the current, and possibly start a new one for the session.
We talked about that in the last one, for the crosscutting aspects of telemetry instrumentation on client side that are affecting both mobile and browser.
So I think that the next step here will be to define those. What was next, I guess, for that crosscutting the client client side, Sig.
and then keep this meeting as like a bi-weekly to align on those things.
And yeah, I think, from what we.
from what we got, I think the next thing to try to focus on only one thing would be the the session management stuff.
Believe that was the the main, the main thing.
**Abinet Debele** 19:28 Yeah, just simple question. There are some instrumentations that are going on in in the Atlantic project, for example, I was. I was working on one that the page view instrumentation.
**Dan Gomez Blanco** 19:45 Yeah.
**Abinet Debele** 19:46 Supposed to emit logs when a page is viewed, and should that be moved to the browser, seek project, or should we should we continue doing it in this? The client, sake.
**Dan Gomez Blanco** 20:01 Yeah. So there was. The last week there was a call to action from Ted to start to populate the the other browser Sig Project board, maybe that maybe this is something that we can do, Async, and start a thread, maybe in the.
and I can start a thread if you want, and then we can say, Hey, what? What in this board do we want to move to the other board, especially if it's currently in progress, right, like instrumentation for page view. I think that sounds like a.
**Abinet Debele** 20:33 Yeah.
**Dan Gomez Blanco** 20:33 Will be a candidate for that. Yeah.
cool.
**Abinet Debele** 20:40 And do? Are we going to create some, a new repo for browser sync? Or do you have any idea on that, and is, or is it? Are we gonna keep working on the current repos.
**Dan Gomez Blanco** 20:51 I don't know. I that's yeah. That's my I don't know. I think that will depend on, though. That's 1 of the discussions that that's 1 of the deliverables of of the initial browser Sig.
**Abinet Debele** 21:02 Yeah.
**Dan Gomez Blanco** 21:03 It's, how do we handle that? Yeah.
**Abinet Debele** 21:06 No.
Okay, thank you.
**Dan Gomez Blanco** 21:16 Let me start a thread and don't think we've got any other topics.
M, okay, we can. We can take some time back.
Is that okay with everyone.
**Leonardo Serrano** 21:46 Sounds good. Thank you.
**Joaquín Díaz** 21:48 Sounds good.
**Dan Gomez Blanco** 21:49 Alright. Thank you very much.
**Joaquín Díaz** 21:50 Thank you.
