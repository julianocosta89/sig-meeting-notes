SIG: Go Compile Time Instrumentation SIG
Date: 2025-10-23
Duration: 26 minutes
============================================================

## Zoom Recording Transcript

**Kemal Akkoyun** 01:52 Hello!
Alright, I thought I was late, but there aren't any other people.
Oh, okay.
Except they won't be late.
**Romain Marcadier** 04:35 Hey, guys.
**Kemal Akkoyun** 04:37 Hello.
**Dario Castañé** 04:38 globe.
**Huxing Zhang** 05:29 Hello?
**Kemal Akkoyun** 05:31 Hello.
**Huxing Zhang** 05:32 Sorry, sorry for being late. I have a meeting, and I have a couple minutes late.
**Romain Marcadier** 05:39 No.
**Kemal Akkoyun** 05:39 group.
Okay, I think, you are the facilitator?
**Huxing Zhang** 05:48 Oh, really?
**Kemal Akkoyun** 05:50 Oh, yeah.
**Huxing Zhang** 05:52 Maybe check.
**Kemal Akkoyun** 05:54 I'm assuming Vini is not here, you're the next one in the line, so…
**Huxing Zhang** 06:00 Zemming, currently it's, busy with working on other projects, working on, instrumentation, Python instrumentation about AI, so maybe it will be less active in this project recently.
**Kemal Akkoyun** 06:19 Hmm.
**Huxing Zhang** 06:21 I'll do the name just with a second.
Let me find the doc.
Okay, I got it.
Let me share on the screen.
Okay, let's look at the… topic and agenda. Maybe we can review the action items last week, yeah, discussed.
First one is, yeah, we updated the plan to Eon. Oh, Ian is not there here.
Shall we look at this?
**Kemal Akkoyun** 07:28 I think he updated that. I see that several things are added.
**Huxing Zhang** 07:35 Yeah.
I think at the time we have discussed the, things that we want to do, working towards the first demo, like, we had… want to add the NetHTP instrumentation, use this, OTL SDK on the demo app.
And it's asking this item, right?
**Kemal Akkoyun** 08:01 Yep.
I bel… take care of that. I will… I will start working on it today, actually.
**Huxing Zhang** 08:09 Okay.
So, is there any estimated time?
That you may finish, finish this.
**Kemal Akkoyun** 08:21 I will try my best to create a draft this week, but next week I will be traveling, so probably I won't have time. I'm… I will be going to New York for the headquarters for a meeting, so, the week after that, I guess, the more sane.
Deadline would be.
**Huxing Zhang** 08:44 So… Let me set up an estimate date, that, maybe… Right now, it's turn…
**Kemal Akkoyun** 08:53 Yeah, I can do that, let's say, before our, like, 6th of November.
**Huxing Zhang** 09:00 Okay.
6th of November.
**Kemal Akkoyun** 09:03 Like, that's the next time I can attend to these meetings.
**Huxing Zhang** 09:08 8… 11… Thanks.
**Kemal Akkoyun** 09:13 Yeah. I carried over to the, This week's action item, so let's update in there.
**Huxing Zhang** 09:21 Okay.
**Kemal Akkoyun** 09:23 I'm doing this typing.
**Huxing Zhang** 09:26 And, So maybe, if you have to travel, so maybe we cannot use this to demo in the… KubeCon North America, right?
That might be, might not be possible.
**Kemal Akkoyun** 09:44 Let me check, when is it?
No, KubeCon is hand, so it's a matter of recording something, or, like, creating a documentation, and if I can deliver that by 6th of November, it should be okay.
**Huxing Zhang** 10:02 Oh, okay.
**Kemal Akkoyun** 10:04 Sorry, it started at 10th, but 10th is the Maintainer Summit.
Then the co-located events… And the real presentation sat on at 12st.
So, there's nearly a week in between, and I haven't checked when is the OpenTelemetry, like, the update track, so we have time.
**Huxing Zhang** 10:24 Yeah, I think we can at least provide a, like, barcode, and at least the link can be in the slides, and we can update, keep the link updated while we are.
**Kemal Akkoyun** 10:37 Exactly. I can do that. I can, like, this is, like, one of the things that I'm planning to do today, create a one-page slide so that we can share, and I was thinking to put in there, like, the previous YouTube recordings of the talk that you have given in KubeCon China.
We gave a talk in GopherCon UK and GopherCon US, another talk, and we all… all of these talks mention about the compile time sync.
So we can put those recordings, some documentation already, I can create a… maybe… yeah, I think that the best way to do this is to create a markdown page in our repo.
And then put a… create a QR, from that, and give that, to the… to the committee, so that they can share this as a… as an update, and we can send PRs to update that page. It would be easier for us to… do this.
**Huxing Zhang** 11:34 You mean… you mean we create a GitHub repo.
**Kemal Akkoyun** 11:39 No, no, not a repo. We already have the repo. I will create just a documentation page, where we aggregate all the links, create a QR of that page, and give that away, and it will be in our repo, so everyone can update.
**Huxing Zhang** 11:52 Right, right, I agree with it. That's okay, I think.
**Kemal Akkoyun** 11:58 And I will initialize a proposal document, like, two proposal documents for Platform Engineering and Observability Day, which I will do this, actually, until tomorrow, so that we can start commenting on it, because the deadline for that is 2nd of November, so… Let's have a week of, like, discussion, at least, on the content.
**Huxing Zhang** 12:22 Okay.
So… I will take a note here.
Or maybe we can put… oh.
**Kemal Akkoyun** 12:31 I'm taking a note.
**Huxing Zhang** 12:33 Okay, thank you.
**Kemal Akkoyun** 12:34 public page from unwind.
And I… I like that we are setting out some deadlines now.
You see, it should export this, I should do until tomorrow.
**Huxing Zhang** 13:07 Okay, cool.
**Kemal Akkoyun** 13:11 Okay.
I think last two items, you already done, right?
**Huxing Zhang** 13:16 Right, yeah, yeah, I shared a link. Did you read about this?
I… actually, I can have some brief… Introduction to this. This, actually, it's kind of, AI agent framework, in China, it's, called… I know it's open sourced by the ByteDance, and it is kind of agent framework written in Golan, and then we can build AI agents, like, talk… talking to ALM.
And, using tools, and etc. And, what we're doing is, in this project, we use this compile time pro… Instrumentation to, like, to instrumentally, call to the LAM, or using tools, or… Critical things, or the agent have, and, Just a, Create a span and record the, key attributes, like.
input and output of the LM, and the tokens, we… tokens that we… it consumed, something like that. And, this is, completely follow the semantic convention of the JNI working group, the JNI spec, that OpenTelemetry has a special working group working on that.
So…
**Kemal Akkoyun** 14:54 Do you use… like, do you use compile-time instrumentation for this already?
**Huxing Zhang** 14:59 Yes, in our Alibaba, project right now, it has been implemented, but what we are… we are working on that we can, yeah.
contributed to the OpenTelemetry project as well, but since the… this project is not ready for, Contributions we first implemented in our repo.
Yeah, that's what we've done, and I think… there's something we can learn from that. We can try to promote things like, using this, project to observe… observe the AI agents might be a good topic, I think, that people may be interested In, in, to, to here? Yes.
So, if that is possible, we can maybe… Create a topic, something like that, to… maybe group, Kang EU, I don't… I'm not… not sure.
Or, also, something like that.
Or we can do it later as well.
**Kemal Akkoyun** 16:19 Yeah, I think, considering KubeCon EU deadlines, like, we can't submit to the main track, it should either be I think observability today?
Which this could be a part of it, but I wonder if there is an AI co-located event.
keep creating these co-located event, so maybe there is one. Yes, cloud-native AI and Kubeflow, there is another co-located event, so maybe… since it's AI, we can try our chances, or we can still Try to summit something more observable today.
**Huxing Zhang** 17:00 Hmm.
You see…
**Kemal Akkoyun** 17:02 Do you want to create a proposal specific to that?
**Huxing Zhang** 17:05 Yeah, I'm thinking of the button, I'm not sure I'm going to there or not. I'm not quite sure about that, so… I'm just a… Tentative right now.
**Kemal Akkoyun** 17:20 Okay.
**Huxing Zhang** 17:21 Yeah.
**Kemal Akkoyun** 17:25 we should at least have, someone from Alibaba to actually present that, because we don't know anything about it, so… If you can say that, like, there will be someone.
Yeah, we can try to submit something.
**Huxing Zhang** 17:38 Yeah, I think we can sub… try to submit. I actually… I have submitted another topic about the… But some, similar, project, but it's not related to this project. So… since you have already want to submit a proposal, I don't… I'm not sure we… maybe we can submit to a different track, I think, if we decide to do that.
So let me think, let me think. Okay. I will try to, do, if it works for me, yeah.
**Kemal Akkoyun** 18:21 Okay.
**Huxing Zhang** 18:25 Yeah.
**Kemal Akkoyun** 18:27 Cool. I will submit to… I will create two proposals and share with you. One of them… one of it for Observability Day, the other one is for platform engineering, and they will talk about the compile time instrumentation, but In different angles, so whatever… which one is ever accepted.
Gotta accepted, we can talk about that.
**Huxing Zhang** 18:52 Do you want to, do you want me or Parzmec to be a co-author of this proposal?
**Kemal Akkoyun** 19:01 Yes, like, we should def… this should definitely be a joint talk, right? So I will create these proposals, and we can decide, like, who will, Actually present this.
it doesn't necessarily need to be me from Datadog's side, and yeah, we can have, Yeah, we shouldn't have, like, Any men up the stage? Maybe just two?
So we can decide if… if it's Datadog and Alibab, or Datadog and… Benchmark.
I guess.
**Huxing Zhang** 19:39 Okay, no.
**Kemal Akkoyun** 19:39 Tejman, Alibaba. Like, you already did that combination, so, let's try to have someone from data on this time.
**Huxing Zhang** 19:47 Okay.
**Kemal Akkoyun** 19:51 I already… I have these proposals somewhere, I just need to revert them, because I'll be already some bits Similar things, so… Yeah, I will, I will share them on the Slack, either today or tomorrow.
**Huxing Zhang** 20:11 So I moved this to the… Here?
Oh, it's already…
**Kemal Akkoyun** 20:18 I already did that. They're already done.
**Huxing Zhang** 20:22 So… So let's just cross this route, okay?
**Kemal Akkoyun** 20:29 Okay, whatever.
**Huxing Zhang** 20:32 Hmm?
Nope.
I want to cross it out.
I don't find… I can't find it.
**Kemal Akkoyun** 20:46 I think it's in format, then strike true.
Yeah, text.
And strike true.
**Huxing Zhang** 20:54 strikes through. Okay.
Oh, this is down already.
And, this, yeah, I already asked the Jurassi about this.
And, it… I think he said yes.
So, in, besides… besides submission to the… collective event. We can do… One… one more thing here. I… I think we can split into… maybe we can do two or three.
If you want different topics, what do you think?
**Kemal Akkoyun** 21:32 But, of course, I think we have I don't know about the co-located events, but KubeCon, you can submit up to 3 total proposals per person, so… I have two ideas, but they're different tracks, so why not? I mean…
**Huxing Zhang** 21:52 Hmm.
**Kemal Akkoyun** 21:52 If others also have some other, like, proposals, let's try to add them as well.
**Huxing Zhang** 21:59 Okay.
So I'll… I'll… so… Maybe… I'm thinking about how to do things like this. So, maybe there is a page that we can share all the ideas that we want to submit, and we can discuss, which… Idea will be submitted to… Which track?
Do you think that is… is that possible?
**Kemal Akkoyun** 22:29 We can try, I mean, Let's have the proposals first, I think the other is, like, easier to decide.
**Huxing Zhang** 22:36 Hmm.
Okay.
So… Is there any actions? I don't think so, this is… Dong, right?
Yep. Okay.
**Kemal Akkoyun** 22:56 I think we are done.
We also discussed the main… what to do with the maintainer track.
**Huxing Zhang** 23:06 Okay.
Oh, there's, there's one thing… oh, slides, slides in… so you will create the slides?
Have you trusted…
**Kemal Akkoyun** 23:18 I think it's just one slide, because it will be part of a presentation, so a couple of words and some QR code, I will try to take care of that. Of course, I will share that with you in the Slack before we send that to… Jurassic.
**Huxing Zhang** 23:36 Okay, so you will create the one, one page?
Okay.
Oh, okay.
So… Okay, this is the… This one will cover the thing you said.
**Kemal Akkoyun** 23:54 Yeah, yes, and we can also add, like, also one-pager slide, slides to that.
Why didn't worry.
**Huxing Zhang** 24:06 Point.
Oh, I have one… one update from our side, Sony.
about the KCD Hangzhou, we have been… We have one topic, got accept.
Objective about our project, so we'll be talking about this.
Compile time instrumentation.
in the KCD Hangzhou, will be… which will be held next week, I think. It's maybe similar than the Cubic… KubeCon… North America. In November 15th… 15th, I think.
So I'll… I'll add one more update.
**Kemal Akkoyun** 25:08 Huh?
**Huxing Zhang** 25:09 Tongue.
Okay.
Is there any other thing that we should discuss?
No.
Good books, huh?
Probably not.
Okay.
**Kemal Akkoyun** 25:46 I think we are…
**Huxing Zhang** 25:49 Without here.
Yeah, we are done, I think. We covered the immediate action items.
Okay.
It's working on that.
**Kemal Akkoyun** 25:58 Cool.
**Huxing Zhang** 26:00 Okay, see you next meeting. Thank you, everyone.
**Kemal Akkoyun** 26:05 Alright, see you soon. Bye-bye.
**Huxing Zhang** 26:07 Bye bye.
