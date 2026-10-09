SIG: GO SIG
Date: 2026-10-08
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Robert Pająk (Splunk Inc.)** 00:42 Hey, Diego, how is it going?
**Diego Hurtado (Dash0)** 00:46 Sorry. Hey, Robert!
Doing alright.
What about you?
**Robert Pająk (Splunk Inc.)** 00:53 Doing good.
**Diego Hurtado (Dash0)** 00:56 Excellent. This is the first time I joined the GO SIG meeting.
First time here.
**Robert Pająk (Splunk Inc.)** 01:04 Is there anything you want to discuss?
**Diego Hurtado (Dash0)** 01:06 Actually… Yeah, I… just, It's a friend of mine.
Who wants to contribute to OpenTelemetry?
And, openTelemetry GO in particular, so I'm here to introduce.
**Robert Pająk (Splunk Inc.)** 01:26 Okay, so we get your… Add maybe to the agenda notes so that you will not forget about.
Discussing this topic.
**Diego Hurtado (Dash0)** 01:36 Alright, got it.
Okay, let's see…
**Tyler Yahn (Splunk)** 01:44 Hey.
**Diego Hurtado (Dash0)** 01:49 Hey, Tyler, how's it going?
**Tyler Yahn (Splunk)** 01:51 Going well. How are you?
**Diego Hurtado (Dash0)** 01:53 All right.
**Tyler Yahn (Splunk)** 02:18 Looks like David's on.
**David Ashpole (Google LLC)** 02:21 Yep.
**Tyler Yahn (Splunk)** 02:22 I see Puneet added his name to the attendees list. Maybe we wait a little bit longer and.
vincentnestler: Yeah, we'll probably start in a little bit, but I guess, yeah.
Everyone's added their name to the… Attendees list?
Hmm.
Cool. I see Puneet's joining now.
So yeah, we could probably jump in here and get started.
I'll start sharing my screen.
And, yeah. So, Robert, you want to start us off? You wanted to talk about your work on stabilizing OTLP, send it out, and send it out log exporters? OTLP, I'm guessing you're talking about the logs one specifically, right?
**Robert Pająk (Splunk Inc.)** 03:21 Yeah, all of them for logs. So I started auditing, you know, I used the AI tool.
all together, so it's reviewed the specification of both proto-repo, as well as specification repo, and actually found some issues, so I'll be trying to, you know, work one by one on the… work on these issues. I already opened one PR, And I also did double check what about other trace and metrics exporters because I have a feeling that some of the issues are.
are targeting, you know, all signals, but I will just create one PR per each, you know, signal or exporter. I do not want to make, you know, too big PRs.
**Tyler Yahn (Splunk)** 04:08 Okay, yeah, that sounds good. I see you added this… different? Yeah.
And this is just…
**Robert Pająk (Splunk Inc.)** 04:18 G. O. T.
**Tyler Yahn (Splunk)** 04:19 Okay. Yeah, this is just the stabilization one, right? Yeah, okay.
**Robert Pająk (Splunk Inc.)** 04:22 Yeah, these are sub-issues and sub-issues are children out of compliance for all of the sections as we have done as usual.
**Tyler Yahn (Splunk)** 04:31 What's your timeline on this?
**Robert Pająk (Splunk Inc.)** 04:34 Working as soon as possible.
**Tyler Yahn (Splunk)** 04:36 No, yeah, yeah, no, I gotcha. Sorry, let me reintroduce.
**David Ashpole (Google LLC)** 04:42 Whenever you have time.
**Tyler Yahn (Splunk)** 04:44 You don't, yeah, you don't, you're not trying to get it done by KubeCon, right, is what you're saying, or the end of the year, or maybe KubeCon Europe.
**Robert Pająk (Splunk Inc.)** 04:50 End of the year, of course.
**Tyler Yahn (Splunk)** 04:53 Yeah, okay, alright, it's just more of, like, an open-ended work, okay, gotcha.
**Robert Pająk (Splunk Inc.)** 04:57 Yeah.
**Tyler Yahn (Splunk)** 04:58 Okay. Cool, yeah, that sounds good.
Awesome, alright, well then I guess, moving on… Puneet, you want to talk about composability, of experimental meters?
**Puneet Singh** 05:10 Yeah, so, yeah, and just a recap from last week meeting, so I brought the experimental meter, sorry, meter configurator to the, config-aware version, but, this topic, I think I myself raised that.
Are these experimental meters can work together let's say you want to have Finish Aware Sync instrument, and also have a meter configurator. And, I think this thing came up that Currently it's kind of conflict, because each one has their own kind of meter factory. And I think Robert… suggested this idea that would it be okay to have some sort of composability build-up that I want to use MetaConfigurator, but also over synchronous instrument, finish-aware synchronous instrument. But, I was exploring in that direction, but then this question also came up that are these features need to work with each other? Like, they don't look quite complementary, actually, that, I also learned about bound instrument a little bit, so I have more context on that, that someone who is using bound instrument, so they have the instrument, reference after the attribute normalization is done. So, and you want to avoid that into the hot path.
by holding the reference to them. Then why you want to… I mean, they look like not a very high priority for finish-aware kind of stuff, basically, because you have selected number of bound instruments. I think that is the… Case here, where you have, like, fixed cardinality for the attributes that you are using, and you don't want to… do the normalization every time, so there's a normalization-free path towards the aggregation, if my understanding is correct.
Same goes… I mean, Meter Configurator is slightly different, but it is overall has a low priority, but I don't see, anyone quite using Meter Configurator along with.
Finish our instrument at least in my imagination.
So, I'm okay to pursue this idea, but I'm also thinking that.
We don't need to… I mean, the individual implementations don't need to block on this functionality. Initially, they can be… Like, created as experimental feature, by being exclusive initially, that at the time you can use only one experimental feature, and then work out this composability thing that You know, how you create a path to have composability about multiple Experimental meters, does that make sense?
**Tyler Yahn (Splunk)** 08:07 Yeah, that's a… That's a good… that's a good point, actually. Yeah, because, I mean, I was just thinking, like, it'd be really nice if you could get all of them, but… That sounds hard. You know, especially if you're, like, trying to resolve Like, functional differences in, like, how these experimental features, like, interact with each other, and then, like, upstream, like, the… They never go through, or they change, or things like that. Like, that's kind of, like, just developer churn.
So yeah, I think… Yeah, let's… I think, like, what you just described is the easier way to do it, right? Like, if you pass one experimental Like, meter option, then just… like, exclude all the other ones, and be like, okay, this is just a failure. And then, like, when somebody complains, and this is like, I really need to use, like.
You know, found instruments with this major configurator, then, like, we can try to figure it out at that point, rather than try to, like, do it from the start.
That makes sense to me.
**Puneet Singh** 09:03 And that also is, like, more direct signal that, I mean, it's just not, like.
**Tyler Yahn (Splunk)** 09:09 Yeah.
**Puneet Singh** 09:10 We are not going to do it, but it shouldn't block that, like, in case of finish of async instruments, like, OBI has a direct use case, and this composability thing shouldn't block that aspect.
And just to give an idea about the difficulty, one idea came is that you have a kind of decorative layer, like one instrument wraps another, but the thing is… We ship this experimental features using concrete types. And these things.
They don't pass the wrapper boundary unless they are part of the interface, like an API interface. So, let's say the bottom-most instrument is the finish-aware. The bound-based wrapper has to ensure that That functionality is mapped, so Bound need to do extra work in order to move that functionality through the interface, and the one, let's say, meter configurator is at the highest level.
it needs to do double the work, like, make sure the API surfaces not just the bound instrument, but also, the finish sync, sorry, finish-aware sync instrument. So the… Functionality just keeps increasing for every meter who comes late to the party, basically.
**Tyler Yahn (Splunk)** 10:29 Yeah, and there's permutations there, right? Because then you need to handle all the combinations of.
**Puneet Singh** 10:34 Exactly. Yeah, exactly.
**Tyler Yahn (Splunk)** 10:36 Yeah, which is…
**Puneet Singh** 10:37 So…
**Tyler Yahn (Splunk)** 10:37 Yeah, I think you're right, just… just… You know, when somebody comes in, they're like, let's do this, then let's do it, but otherwise, let's not worry about it, I guess.
**Puneet Singh** 10:46 Yeah, yeah. All right, I might post some more notes in the… in our channel, Slack channel, on if I see any what is the existing conflict between the meter contributor and the SYNC instrument, since these both are the ones that are, like, getting quite close to the implementation.
Bound instrument, I know the, like, very high level, so that part might come later. I'll create a separate issue for the composability, just regarding the high-level problems, okay? So yeah, I think that's… that's… what I had on this.
**Tyler Yahn (Splunk)** 11:24 And just for, like, context, like, David and I had talked about, like, combining the finish with the bound instrument stuff, but, like, it's also one of those things where, like, the API might be different for, like, bound instruments, where we would say, like.
about an instrument would be finishable in, like, a different way, or maybe the same way, like, it wasn't really, like… so the, like, the composability there may also just take a different form as well, like… Yeah, like, the returned instrument itself may also return, like, a, you know, a shutdown operation associated with the instrument itself, was kind of the idea, but, Yeah, so I think that, like, just… Just punting on that is such a good idea, just to help, you know, development move forward, yeah.
**Puneet Singh** 12:01 Yeah, I mean, the finished thing on the bound instrument doesn't quite click for me, because the whole thing is… is… avoids the attribute normalization, so it all, you know, the major part is already off in the hot path, so.
I think it's kind of okay to have a separate path for bound and finish aware thing actually. So yeah.
But yeah, I'll post more on this as it goes forward.
**Tyler Yahn (Splunk)** 12:34 Cool. Yeah, alright, that sounds good.
Okay, going back to the agenda, moving on, Dago, you wanted to introduce Randall.
**Diego Hurtado (Dash0)** 12:47 Right, yes, so… I'm Diego, this is my first time here, I initially tell Python.
But, yeah, Randall here is, is a good friend of mine.
Great engineer, and We were talking about OpenTelemetry a few days ago, and Randall mentioned to me that he'll be interested in contributing. I asked Randall, okay, which language would you like to contribute? And he mentioned.
He was interested in contributing with GO. So, Torando, yeah, sure, let's, join us, the next, week in the GO SIG, and I'll introduce you to the folks. So, I don't know, how you… Folks, in the GO SIG, do when there's someone new.
So, I don't know.
I'll just let you… Ask Randall, or… Whatever you do.
**Tyler Yahn (Splunk)** 13:46 Yeah, I mean, we just say, welcome, Randall, nice to meet you. Welcome to the SIG, yeah.
**Randall Fallas** 13:52 Hey, thank you, nice to meet you all, and thanks, Diego, for introducing me here. So… Hope to contribute at some point, and yeah, it's starting to want to get involved in the community, so thank you for your warm welcome.
**David Ashpole (Google LLC)** 14:06 And if there's anything in particular that you've heard we're working on or that we mentioned that you're like, Hey, I want to work on this, just like let us know and we can make sure that you're.
like, included.
**Randall Fallas** 14:17 Thanks, David. Yeah, for sure.
**Diego Hurtado (Dash0)** 14:21 Rodel, you already joined the Slack channel for OpenTelemetry Law, right?
**Randall Fallas** 14:28 Yeah, I'm already on the Slack, channel, Focus Telemetry, so… I'm already in a couple of channels there.
Not sure if for the GOSIC there isn't a specific one, but… I can take a look.
**Tyler Yahn (Splunk)** 14:41 Yeah, it's just OTEL dash GO.
**Randall Fallas** 14:43 Okay.
**Puneet Singh** 14:46 There is also a.
Go compile time instrumentation.
I myself am not sure that what is the scope of, you know, that part that covers, actually, because I think it's different from the auto-instrumentation.
I think.
**Tyler Yahn (Splunk)** 15:02 Yeah, it's just a different form of the automated tradition. So, like, the compile time stuff is, like, a compiler-based, like, integration, for GO that, like, Automa Instruments based on this, but it uses this project kind of as, like, a base.
Same with, the auto registration using eBPF kind of uses… it does use, like, our APIs here, as well. So this is more, I think, like, the core.
There's the Contrib repository as well, that holds a bunch of, like, manual instrumentation for specific packages, and then there's a bunch of just third parties themselves that, like, host and use our APIs to write their own instrumentation. So yeah, it's used all over the place.
**Diego Hurtado (Dash0)** 15:38 Right, I took a look into the Pontolometry GO issues, and I think, if I remember correctly, there was a label for good first issue, but I think right now there are no issues labeled like that.
So, I don't know if there's a… Particular issue, do you think, will be good, maybe for Randall to start working on?
What do you think?
**Tyler Yahn (Splunk)** 16:02 Yeah, we… I'd probably recommend just, like, just taking a look on your own, and finding an issue, if you find it interesting, commenting on it, and then, like, we can… we can help you. There's not really, I think, like.
a lot of really good first issues right now. Like, that'll probably change after the KubeCon North America, when the Katrib test happens. There'll probably be a lot more after that, but… Yeah, it's more just about, like.
Trying to find something that you're an expert in, as well, try to help in that space. It's usually a good place.
**David Ashpole (Google LLC)** 16:36 I was gonna say that if we put good first issue.
On an issue, it usually disappears in, like, 10 seconds.
**Puneet Singh** 16:41 Exactly, I mean, that's what I wanted to…
**David Ashpole (Google LLC)** 16:45 Unfortunately.
**Puneet Singh** 16:47 Yeah, I also wanted to come back to the… the first item that Robert discussed. It's… it's nice that he mentioned in each of the issues that he's working on this, actually, on the every issue, so… so yeah.
**Robert Pająk (Splunk Inc.)** 17:03 I just want to maybe I think that Puneet you also agree, that for me, the easiest way to start contributing and to be onboarded was to actually review, review PRs of other approvers and maintainers.
Because it was the easiest way to also learn how the report is structured, how to, you know, describe things, what issues are important. Sometimes, also, when you review some PR, you might find some other issues, which you can complement, and fix in your own PR. Instead, sometimes you'll put in the comments if it's not, you know, tightly cut to PR, if you just see something, and sometimes it makes it easier then for us to collaborate, because we then have, you know, connections when we review each other's stuff.
**Puneet Singh** 17:52 Yeah, I agree. I think the code review part is very underrated kind of thing, actually.
Like, most of the people are, like, ready to jump in as soon as they see good first issue or help needed, but, Reviewing PR is, like, very, very useful, actually. You can take your time, and that really gets you up to the speed with certain areas in which the work is happening.
**Randall Fallas** 18:20 I think those are really good ideas. Just taking a look at the PRs, I can get an idea of how… I've been good review on which standards are being used, and the chain of thought of, you know, one review in a PR for this. It's a good idea.
**Puneet Singh** 18:36 I can give a kind of biased opinion about that, why the SIG This is good in a way it is.
So I started in March, I think, And at first, I spent time in the Java SIG looking for, maybe almost, like.
15 to 20 days, I think. And I had previous GO knowledge, so I was like, okay, let's go into GO SIG and see what's happening. I followed, like, offline for almost a month, regarding just watch the meeting recordings, and It's just about the SIG that the things… the breadcrumbs that come out from the discussion has a lot of context, and you spend enough time. You start to follow that, okay, what's the work is happening, where you can make contributions, and where can you start, having discussions and.
follow your own path, actually. So, yeah, but I'm sure the other six are equally doing very good work, so… so yeah, it just, I got up to the speed with the six of them, you know.
I have a state, so far.
But, but credits to…
**Randall Fallas** 19:57 Bye.
**Puneet Singh** 19:58 Yeah, credit to, I think, all three, Tyler, David, and Robert, to, you know, have that direction whenever I needed some help. So, yeah.
**Randall Fallas** 20:09 Hmm.
Cool. Yeah, I will take previous meetings… I will take a look at previous meetings and check ongoing PRs and closed PRs to get a little bit more of context into it.
**Tyler Yahn (Splunk)** 20:24 Cool. Yeah. Well, yeah, hopefully we'll see you continuously. Yeah. Excited.
Okay, that's the end of the written agenda. Any other topics folks had? Exciting ideas?
I guess one of them I've been doing is a shout-out, you have 3 more days for KubeCon, you… 2027 CFPs.
So, if you have an idea, you should submit a CFP. If you need help on the CFP, there's, like, an OTEL CFP channel or something like that.
If you wanted to talk with other folks, like, Slack's a good place to do that. Collaboration's another good thing. If you're an EU citizen, you are, desirable to have on the CFP title, so… It's a lot easier to get a talk accepted, in the EU, I've found, if somebody from the EU is also co-presenting with you. Just a heads up on that one.
But also the Observability Day, I think it's, like, a week after. I think you have, like, so then, what would that be? Like, 10 days until that closes?
But yeah, that's another really good one. In fact, I'd say, like.
You have a better chance of probably getting it into that talk, but you will have a smaller audience. You do get a free ticket to the main event as well, if you get a talk accepted there.
And then, probably the last one is, like, there's a maintainer summit right before that, so, it's a little bit… you have to be, like, an approver or a maintainer, I can't quite remember, to officially do it, but you can always get sponsorship from an approver or maintainer to actually get a talk accepted there. But if you have a talk, kind of Puneet, like, what your experience was just, like, joining OTEL, maybe is also a good talk for that forum. That's, like, sort of these meta issues around, like, community and organization structure are really good for the Maintainer Summit. So, yeah.
**Puneet Singh** 22:10 Is it… is it, like, happening online, or I have to be at the event?
**Tyler Yahn (Splunk)** 22:15 I think you have to be at the event to give the talk. I think you can watch them, obviously, like, after the fact, but I don't know if it's, like, being broadcast during the event as well.
It is also… the maintainer one is, like.
Sunday, I think is usually when… When the event happens, so it's a little bit awkward, for some folks to join that, just because, like, it's on the weekend.
But yeah, that is, I think, travel required.
That being said, if you don't have, like, a company willing to sponsor you, they do have, like, scholarships as well to get, funding for travel and, I think, hotels?
Correct me if I'm wrong on that one, but yeah, like, so, like, for folks listening to this that just are, you know, maybe, like, worried about the cost, that is something to also look into, if you get a talk accepted, yeah.
Yeah, the hallway track at these conferences is kind of invaluable. Just getting to meet people and talk with people is pretty amazing. Also, just, you know, inspiring to see like-minded folks talking about things that you're really interested in, so yeah.
So, I would recommend it, and yeah, I think that that's… that's a… that's another good idea.
Any other… Callouts?
New projects people are working on?
**Puneet Singh** 23:42 Oh, I forgot to mention, please have a look at meter configurator PR whenever you have time.
**Tyler Yahn (Splunk)** 23:48 Sure thing, yeah. Yep, taking a look.
Well, cool. Alright, if that's it, then we can end the meeting early here. Good seeing you all, and we'll see you all in a week.
Or, asynchronously. Until then!
Bye.
**David Ashpole (Google LLC)** 24:03 everyone.
**Diego Hurtado (Dash0)** 24:04 Thank you all. Bye. Take care.
