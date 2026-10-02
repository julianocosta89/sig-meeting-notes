SIG: Go SIG
Date: 2026-10-01
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Robert Pająk (Splunk Inc.)** 00:05 Hello, Mark, how are you?
**Marc Schäfer (T&A SYSTEME)** 00:07 Hi, how are you Robert?
**Robert Pająk (Splunk Inc.)** 00:10 I'm good. It's hot today in Poland, in Germany as well, I guess.
**Marc Schäfer (T&A SYSTEME)** 00:14 Yeah, it is, it is.
**Robert Pająk (Splunk Inc.)** 00:16 And the forecast for next week is also very promising, Adesola.
**Marc Schäfer (T&A SYSTEME)** 00:22 Didn't expect to get it this hot again.
**Robert Pająk (Splunk Inc.)** 00:25 Yeah, almost like summer.
**Marc Schäfer (T&A SYSTEME)** 00:28 Yeah.
**Robert Pająk (Splunk Inc.)** 00:31 Yeah, but it's getting dark.
of Hello, Brian.
**Bryan Boreham** 00:44 Hello!
Some are here too.
**Robert Pająk (Splunk Inc.)** 00:50 Awesome. And back home, right?
**Bryan Boreham** 00:53 Yeah.
**Robert Pająk (Splunk Inc.)** 01:08 Tyler will not join today.
Oh, we have 2 minutes.
**Puneet Singh** 01:14 Hello.
**Robert Pająk (Splunk Inc.)** 01:16 Hello!
Nice to see you.
**Puneet Singh** 01:22 Likewise, I mean, the timing is kind of unique, like.
It's not quite far away from sleeping time, so you can…
**Robert Pająk (Splunk Inc.)** 01:32 the.
**Puneet Singh** 01:33 Either up or down, so I was like, you know, let's just join and see what happens, yeah.
**Robert Pająk (Splunk Inc.)** 01:38 Yeah, you may have problems getting a seat later.
Hello, David.
**David Ashpole (Google LLC)** 01:45 Hello?
Congratulations.
I don't think I've told you yet.
**Robert Pająk (Splunk Inc.)** 01:49 Thank you.
Thank you!
All right, let's… I'm opening the meeting notes.
I can try running the meeting today. So, you do not have maybe two days this ProMeteos meeting. Is it the other week?
Or it was some, it was some other, oh, I'm just getting confused.
Because I remember you had a conflict, but I never remember which week was it.
**David Ashpole (Google LLC)** 02:28 Conflict with the SIG.
**Robert Pająk (Splunk Inc.)** 02:30 Yeah, I think so, but maybe I'm wrong.
**David Ashpole (Google LLC)** 02:36 What did I have last week?
I didn't have a conflict last oh, I was just out of like I was on vacation last week.
**Robert Pająk (Splunk Inc.)** 02:44 Right. That's good.
**Marc Schäfer (T&A SYSTEME)** 02:51 Is anyone, is anyone next week at the Observability Summit?
I'll be there.
Are you really there? Okay.
**Robert Pająk (Splunk Inc.)** 02:59 I have a dog.
**Marc Schäfer (T&A SYSTEME)** 03:01 I have a talk. I didn't catch it in the schedule yet.
We'll take a look.
**Robert Pająk (Splunk Inc.)** 03:07 Okay.
**Marc Schäfer (T&A SYSTEME)** 03:08 Because I will be there as well, so… Awesome.
**Robert Pająk (Splunk Inc.)** 03:13 I'll be there from Sunday until Tuesday.
But I'm planning rock climbing on Sunday and Tuesday in Prague. It occurred that there are cracks inside the town, even.
Yeah, which is surprising.
**Bryan Boreham** 03:29 We also have PromCon in Munich if you want to.
Come over.
**Marc Schäfer (T&A SYSTEME)** 03:36 Munich.
Okay.
**David Ashpole (Google LLC)** 03:41 Yeah, I wanted to go, but I couldn't get approval.
**Robert Pająk (Splunk Inc.)** 03:46 Thank you.
**Bryan Boreham** 03:47 Not enough AI.
**David Ashpole (Google LLC)** 03:49 I don't know.
**Marc Schäfer (T&A SYSTEME)** 03:53 I didn't know that it was in Munich.
you.
**Bryan Boreham** 03:59 Yeah, it's actually at the Google office in Munich.
**Robert Pająk (Splunk Inc.)** 04:05 I'll start sharing my screen.
You are 4 minutes in, so please feel, you can add yourself to the attendees list. I can at least copy-paste some of you in the meantime. So, if you have any things that you want to discuss.
Please add to the agenda items. We do not have a lot here.
Mark is here… 5, And David is also missing.
**Puneet Singh** 04:33 Did I copy somewhere wrong?
**Robert Pająk (Splunk Inc.)** 04:38 No, I think it was correct. It was the PR that we have been discussing last time. I'm not sure if my PR is correct.
From my side, I have only one ask.
I just want to have more approvers here, especially from approvers and maintainers, to be sure that I'm good to release, once we are ready. There are a few… there's still, like, one or two PRs which I want to merge before getting… before the release.
But I would like to have a purpose here so I'm not blocked once we are ready with the other PRs.
And yeah, the last release was more than one month ago, so I think it will be good to have this release. Any comments here?
Alright, so… Let's go Puneet. Puneet, do you want to share or do you want me to share?
**Puneet Singh** 05:45 I think you can open it.
**Robert Pająk (Splunk Inc.)** 05:47 Yep. And I saw your, and I can scroll to the bottom, I think to your latest. I also, you have updated, I think you have updated this description as well.
**Puneet Singh** 05:55 Yeah, so I think David wasn't there last time, so just wanted to recap a bit.
I think Tyler and Robert also iterated this point that, Adding in the hot path, like any experimental feature, no matter how small the regression is, is… Something that the SIG want to minimize, and… It would be better to make it… make the feature config-aware so that the users… only those users who opt-in end up paying the price for the extra check, no matter how small it is.
So… yeah, I think most of the… rest of the adjustment has been made with respect to that.
idea?
What I have done is, is essentially meter provider when I started with, this.
Configurator option, it ends up creating another meter which is configurator compatible.
And it has its own instrument, which contains that check, but they are actually essentially wrappers, and end up forwarding the logic to the actual, the meter logic. So, I think if you go to the top, the type Yeah, I think.
Can you go down a bit?
Yeah, the structure part.
And this also kind of takes some of the ideas from the.
finish up your SYNC instrument that Tyler is trying to do.
So… In future, I also see this possibility that You won't be… a user won't be able to use Different experimental options from the.
meter provider, I think, at least. You can only use one experimental option, because The meter factory can only return a one one specific kind of.
Experimental meter, actually.
**Robert Pająk (Splunk Inc.)** 08:21 But that's my… that may… that may… I think that… Probably we'll need to recheck the recording for last week, but I think, at least, it was my understanding that not only the experimental thing was important for us, but the thing that this is an opt-in feature.
that we do not expect that the… this width meter configurator will be something that most people will use, and that's why we wanted to have. Even… even if… is not experimental. I think we both thought that having, you know, this additional overhead for atomics, maybe just, you know, It's better to avoid, if possible, the, you know, the… It usually makes the memory barrier. It's kind of cheap, but it depends on the processor architecture. You know, on Intel, it's very cheap, but I'm not sure about other processor architectures. So that's, I think, the main reason we wanted to have it, but yeah.
It.
Regarding this… other experimental features, we already have something which will be exclusive, or you're just thinking about the future, and, you know, doing it. So, you're just worried about, or there's already existing things that cannot be, you know, enabled together with these, configurators.
**Puneet Singh** 09:49 So, the feature that Tyler was working regarding the… Finish our.
**Robert Pająk (Splunk Inc.)** 09:57 finish.
**Puneet Singh** 09:57 Yeah, that… because that is also trying to bring up an experimental kind of meter, which only works Where it is needed, and it isn't… It is specifically built for OBI, I think?
I'm not sure if it meant CBPF also, that part I'm not clear about.
But, but I looked at the structure and made sure that even Either this feature, or the… the… Finish aware single instrument whichever order they get deployed they don't end up.
disrupting a lot, you know? The change would be minimal, no matter the order of the deployment is. So, that… I've taken into account as much as possible.
**David Ashpole (Google LLC)** 10:49 Does it… does it need to actually… Provide a different instrument implementation.
**Puneet Singh** 11:00 It doesn't exactly, as a different instrument implementation, but Its instrument act more as a wrapper.
for the meter config check, and then forward, reuse the logic from the, the core instrument logic, actually. So it's not, like, completely reimplementing, but more like implementing them as wrappers.
**Robert Pająk (Splunk Inc.)** 11:24 So, is it not possible even to wrap one and another? Is it really exclusive? Cannot you know if both features are enabled? Could you wrap once and the other, like a decorator pattern?
**Puneet Singh** 11:38 It would be tricky to do that with, you know, Instrument, I think.
I thought about it, but I can't recall the reason that why I decided to, Didn't do that way, because I think there is some sort of, conflict in… Putting functionality of, let's say.
Finish aware instrument and configurator aware instrument together actually. So there I felt some sort of conflict. That's why I also mentioned that.
Having to.
Experimental features on the meter may not be possible together, actually. That at a time, a user can only use one experimental feature, especially in the context of Meter, actually, yeah.
**David Ashpole (Google LLC)** 12:45 Hmm, interesting.
Yeah, I've I kind of agree with Robert, it would be nice if they could both wrap.
**Puneet Singh** 12:58 I also agree, I mean, that would be very desirable to have some sort of Composability of experimental features, but,
**Robert Pająk (Splunk Inc.)** 13:10 I think maybe it will require some little hacking, like, you know, checking the exact implementation, which is wrapped.
Sometimes.
It's necessary, you know, what is actually inside.
**Puneet Singh** 13:24 Yeah, I mean, yeah, I think, I'm, I'm open to discussion. I think this is something, this is something that can be followed up.
And I'm willing to hold for that, you know, design to dissolve. So, yeah, that is totally fine.
**David Ashpole (Google LLC)** 13:40 Or if the wrappers, wrap around like an interface instead of wrapping around the underlying concrete type.
you'll lose some performance, I think, but… Then it could, like… Like, they could implement each other's… If, as long as they all implement the interface, right, then.
They can wrap each other. We still have to pick, like, an ordering, maybe, but… I don't know if that makes sense.
**Robert Pająk (Splunk Inc.)** 14:06 Yeah, that's what I thought about interface. I think the cost will be still lower than having atomics on the hotpath.
At least, you know, on high concurrent code, multi, yeah.
**David Ashpole (Google LLC)** 14:19 Okay.
So just… it just means the embedded types here.
Would be an interface that's implemented by, like, N64 instrument, rather than the concrete types, so that You could embed a finished.
In 64 instrument as well.
And.
**Puneet Singh** 14:45 And that's…
**David Ashpole (Google LLC)** 14:45 A finished one could embed a configurator one, if that's what… We decided to do.
**Puneet Singh** 14:52 Right, and that should be okay for… I mean, it… Though it has a performance penalty, but that should be okay for experimental features, I presume.
**David Ashpole (Google LLC)** 15:02 I think so, I think the only time I would think it maybe wouldn't be acceptable is if, if the configurator was like A performance-related feature, like bound instruments.
Then it would kind of defeat the purpose to have, like.
a performant API that wasn't actually performant.
But for this, I think it's mostly about, like, can we make it ergonomic to turn something on and off dynamically?
Via this callback function. I think… I think that would achieve that goal and let people try it out.
If that's what we're trying to do.
**Puneet Singh** 15:43 All right.
Umm.
Yeah, I'll spend some more time thinking about this and see, What can I come up with?
Debit, if you get time, also have a look at.
I think I took some ideas.
**David Ashpole (Google LLC)** 16:02 I have been not able to spend time on open source reviews in the last two weeks.
It is…
**Puneet Singh** 16:08 has.
**David Ashpole (Google LLC)** 16:08 I have it open in a tab. Every time I open it, I go, I don't have time for this right now.
**Puneet Singh** 16:16 Yeah, so, yeah, I mean, also have a look at the… Tyler's PR, which is in draft stage right now.
Yeah.
from I think this one.
Oh.
If you open files changed.
**David Ashpole (Google LLC)** 16:40 Nice, okay.
**Robert Pająk (Splunk Inc.)** 16:44 I remember I was talking with Taylor on Tuesday, and he also told me that He still has… hasn't… He's not… he has not done it ready for review, because he hadn't also, double-checked everything, and he… there might be something that may need improvement.
He's right now focusing on trying to get a release of V1 release of OB.
**Puneet Singh** 17:10 I think… There is somewhere… Meter Factory… type… Oh, yeah.
So, I think based on… it tries to… Activate the feature based on the option.
And I think the first selected option.
Gets matched and based on that the specific meter.
Umm.
Gets returned, actually.
So, which is… Which is why I said that, you know, you can… have… One experimental feature at a time, if we go by this approach.
**Robert Pająk (Splunk Inc.)** 18:13 Yeah, but, you can, I think you can put a comment, as I told, as I told, Tyler didn't say that it's ready.
So, if you see, you know, this problem, that you cannot… you can just grab a comment here, and… Not today because it's late for you, but tomorrow morning you can write also this here and also you can even think about adding here even this idea about wrapping the instrument as interfaces.
you know, into the in the definition instead of concrete types.
This is November.
**Puneet Singh** 18:50 I'll do that.
**Robert Pająk (Splunk Inc.)** 18:52 If you have also any other ideas, then also write it here.
**Puneet Singh** 18:56 No, I thought of interface at that point, but that scared me because Because, you know, performance was one reason that was, you know, like.
**Robert Pająk (Splunk Inc.)** 19:06 Yes.
**Puneet Singh** 19:07 This feature was being…
**Robert Pająk (Splunk Inc.)** 19:09 Yeah, yeah.
Yeah, of course. You know, it's also about checking and then finding a compromise which way we'll choose, but I'm less concerned about using the interface than using Atomics or any other synchronization.
I think it can be.
Worse in some scenarios, it's more risky.
**Puneet Singh** 19:33 Right.
Alright, I'll, I'll… Put comment here, but I'll also think about the… How to make it, like, composable, as in the layer of decorators, and see how it looks like.
**Robert Pająk (Splunk Inc.)** 19:50 Okay.
**Puneet Singh** 19:52 Yeah, I think, yeah, that's… That should be okay.
**Robert Pająk (Splunk Inc.)** 20:01 Okay, this is the end of the written agenda.
Are there any other topics?
Bryan, Mark, anything from you guys?
No, just inviting us to Germany.
Yes, Mark?
**Marc Schäfer (T&A SYSTEME)** 20:22 Nothing from me, so…
**Robert Pająk (Splunk Inc.)** 20:24 okay.
**Marc Schäfer (T&A SYSTEME)** 20:25 you.
**Robert Pająk (Splunk Inc.)** 20:28 Okay, so… We are ending 14 minutes early. It was nice to see you all, guys.
**Marc Schäfer (T&A SYSTEME)** 20:34 Yep.
**Robert Pająk (Splunk Inc.)** 20:35 See you guys.
**David Ashpole (Google LLC)** 20:36 everyone.
**Bryan Boreham** 20:36 Thank you.
