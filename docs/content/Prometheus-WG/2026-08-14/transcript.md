SIG: Prometheus WG
Date: 2026-08-14
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Arthur Sens** 00:32 Hello.
**krajo (Grafana Labs)** 00:33 Hey, sorry, we were caught up in talking about the Joe Bend instance stuff. David's going to be.
A few minutes?
**Arthur Sens** 00:44 You were talking about it somewhere else?
**krajo (Grafana Labs)** 00:47 Yeah.
I just let Arve know that the Zoom link is changed. I'm sure he joined the old one.
David should know that.
Revenue.
**David Ashpole (Google LLC)** 01:40 Hey, Arthur.
Hello. Mac.
**Arthur Sens** 01:44 Thank you.
Long time, we'll see.
**David Ashpole (Google LLC)** 01:50 You, you live, like… You were on vacation, right? Did you vacation somewhere other than where you live? Which is… A vacation spot, or… Did you, like…
**Arthur Sens** 02:00 oh… What's go here.
Oh. So… the… it's more of a summer place.
To do holidays, so I went to Japan, actually.
And it was way too hot.
more than I expected.
**Kyle Eckhart (Raintank, Inc. – Grafana Labs)** 02:21 Disgustingly hot.
Yeah. David, you're in… you're in the US, right?
**David Ashpole (Google LLC)** 02:27 Yep, Cambridge, or… I'm in the Boston area.
**Kyle Eckhart (Raintank, Inc. – Grafana Labs)** 02:30 Okay. It's like Florida summer hot, like, in… in Japan.
**Arthur Sens** 02:36 And Kyle was… was there as well.
**krajo (Grafana Labs)** 02:40 What was where, sorry?
**Arthur Sens** 02:42 In Japan.
**krajo (Grafana Labs)** 02:44 Who was there? You?
**Arthur Sens** 02:46 Kaya.
**krajo (Grafana Labs)** 02:48 Oh, Kyle! Sorry, I thought you said my name. Oh, man.
**David Ashpole (Google LLC)** 02:52 I know as well.
**krajo (Grafana Labs)** 02:54 Yeah, sorry, I'm on a lot of painkillers, because I was at the dentist.
And, like, my mind is mush a little bit.
**Kyle Eckhart (Raintank, Inc. – Grafana Labs)** 03:03 To be honest, sometimes when people say your name, I hear my name, so…
**krajo (Grafana Labs)** 03:08 Okay.
**Arthur Sens** 03:09 I put some… some stuff on my teeth.
I don't know how to say that in English, but something that moves the teeth around.
**David Ashpole (Google LLC)** 03:18 Invisalign?
**Arthur Sens** 03:19 Invisalign, exactly. I got Invisalign, so I'm having a hard time talking because of this thing as well.
**David Ashpole (Google LLC)** 03:25 Your teeth are looking great, though.
**Arthur Sens** 03:27 Thank you.
**David Ashpole (Google LLC)** 03:30 My wife got it, and she loved it, so hopefully it works out.
**Arthur Sens** 03:34 Yeah, I hope that looks… It's very expensive.
**David Ashpole (Google LLC)** 03:39 Okay, so… I'll just… the backdrop to this is that, Arve and… krao and I just had an hour-long discussion about job and instance, and… Round tripping and stuff. And, I think it might be helpful… krao and Arve, would you like to continue that?
Or would it be better to go through any other agenda items, and then… Return to that, and blow out the rest of the time with it.
**krajo (Grafana Labs)** 04:14 Yeah, I think it would be very confusing for… Kyle and Art to repeat John back into that discussion, so let's, let's, let's, yeah, let's try to do… The other points, if there are in the agenda.
**David Ashpole (Google LLC)** 04:28 I have a couple small ones.
Breaking.
**Arthur Sens** 04:34 But if you can summarize later, I would love to hear, like, eventually…
**David Ashpole (Google LLC)** 04:38 Beautiful.
Yeah, we will definitely summarize and try and bring you all along.
Okay, well, welcome, everyone. Please add yourself to the attendees list.
And then… Okay, looks like we've got at least some… some topics.
Alright, I wanted to run just through… there's a couple of small discussions, Arthur, on the… These miscellaneous ones just never had issues open for them.
Let me share my screen.
There we go.
So unknown, state, set, and info, we never made tracking issues for them, so we stabilized the rest of the spec, but didn't touch these.
**Arthur Sens** 07:23 I bet.
**David Ashpole (Google LLC)** 07:24 No, no, that's okay. I think I might have even created them all.
So unknown looks, I think, mostly… Like, we're okay with it.
We have state sets.
Which… like, the Prometheus… receiver… I think right now it does handle state sets properly, or according to the spec.
But… If we wanted to do anything different with state sets.
Then we might want to feature gate that.
That behavior.
And leave this in development.
**Arthur Sens** 08:05 Yeah, I would prefer that. I know it's gonna take a few years, but I've seen a lot of discussions about the current state set is not… does not perform well.
Yeah, I bet we'll change.
**David Ashpole (Google LLC)** 08:29 And we're… but we're okay for this group leaving it in development for… A couple years till that happens.
I think that's okay.
**Arthur Sens** 08:40 Yeah, as long as it doesn't block, stabilizing the Prometheus receiver, I'm fine.
**David Ashpole (Google LLC)** 08:55 Okay.
Any… any objections? Otherwise, I think we can scooch on.
Cool.
And then I guess… I guess we'll drop state set metrics for now?
Unless someone turns on the feature key.
**Arthur Sens** 09:41 That makes sense.
**David Ashpole (Google LLC)** 09:51 Okay.
And then… Last one to discuss is InfoMetrics.
So right now, we have special handling, obviously, for target info.
But we have no special handling for other ones, so they're currently just turned into up-down counters.
**Arthur Sens** 10:12 Yeah, this is related to the project, the krao and Arve are… are working on about metadata storage, but I don't know if, like, I know we discussed potential… A potential scenario where all infometrics somehow become resource attributes or metadata.
But, yeah, I don't know if this is what we're aiming for in, like, Phase 1, or, like, Phase 10, or…
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 10:45 I don't really think we have talked about that per se, krajo. I guess, I think more the idea is that, infometrics become obsolete over time, because… because metadata are stored natively instead. Does that match your thinking, krajo?
**krajo (Grafana Labs)** 11:04 I mean, there's an aspect where if you want to support the use case of X… exposing… We're federating, you know, metadata, and or sending over remote write Then we will have to think of something, and for example, when you want to expose, maybe infometrix will be the way to do it.
So… But definitely not in Phase 1.
**David Ashpole (Google LLC)** 11:35 I think the more important question from my point of view is.
Will infometrics that are scraped ever not be queryable?
in the way that they are today. Like, today I can… write a query for CubePodInfo.
that gives me them, like, as time series. I think the question is whether we're ever gonna take that away, because it's totally fine if we want to Take infometrics and do additional things.
with them.
**krajo (Grafana Labs)** 12:04 I put it into the design doc. I think I wrote that we should keep the interface that you can.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 12:11 Nope.
**krajo (Grafana Labs)** 12:12 Fire them the same way as now, so be backward compatible in that way, because… I assumed, maybe wrongly, but I assumed that that's not that hard to implement with native metadata store.
Like, I wouldn't really break them, because, like.
we learned in the native histogram work that when you break the queries, then people freak out. So…
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 12:37 Yeah, I mean, that's what I was saying before, that, at least I, myself, I foresee that we keep infometrics as they are. Yep.
It's just that native metadata should become, like, an alternative that people should prefer with time.
But I think, you know, the… I think the exposition of native metadata is an unsolved problem.
right guy, but I think that's something… I think we have to develop an exposition of it, I think.
And I… but I also think, at least for now, I think that… I think they should not be… I think they should be in parallel to Infometrics, I think. I don't think they should… I don't think they should kind of, like, be… masquerading asymetrics? I don't think so.
That's what I think at the moment, at least.
**krajo (Grafana Labs)** 13:30 Yeah, that's fine as well. I mean, yeah, the point we are trying to make is that we don't want to take that feature away, yeah.
**Arthur Sens** 13:53 So, what?
So, let's… Let's say we ingest something and it becomes native metadata.
And then you expose it again as… and Federation, for example, as Infometric.
Then we would transform those infometrics into up-down counters.
Which then becomes a gauge.
**David Ashpole (Google LLC)** 14:19 I suspect native metadata is… a thing that's internal to Prometheus?
Right?
**Arthur Sens** 14:27 Yeah, but we need to expose it.
To, like, through federation or remote, right?
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 14:33 Yeah, but what, what… what I was suggesting was that we… I mean.
It's just my idea at the moment that we develop, like, an exposition of native metadata.
Instead of masquerading them as infometrics.
**Arthur Sens** 14:49 Okay.
So, okay, so it's an addition, then that doesn't… it's not a breaking change.
And then eventually, we can… We can deprecate infometrics and rely only on native metadata.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 15:07 That's my current thinking, at least, and is that also your thinking, krajo?
**krajo (Grafana Labs)** 15:14 I haven't fought that far ahead.
the only thing that I wrote in the design doc so far as a requirement that eventually we will have to be able to do federation and remote, right? And then how we do it, it's, like, future stuff. I think… you know, there's more major question first in the design doc, like, does Prometus actually want to go for native metadata and lift it into first?
Like the, What, what's the word I'm looking for?
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 15:48 You mean, like, a first-class citizen?
**krajo (Grafana Labs)** 15:50 citizen, yes, thank you very much.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 15:52 Right, right, right?
Yes, no, I agree 100% with you, krajo. I don't think this is, like, a first stage concern at all, but we will have to think about, you know, if it succeeds and then goes into Prometheus, we have to think about this at one point.
And it's just my, you know, it's just my vague idea at the moment that we should probably keep, keep native metadata a separate channel from InfoMetrics.
I think if we were to… I think if we were to serialize them to InfoMetrics, that would be lossy.
I think…
**Arthur Sens** 16:27 Sounds good to me.
**David Ashpole (Google LLC)** 16:29 I'll just… end that with, and I think the important thing for this specification.
is mostly weather… like, whether there would ever be a case where we would get an infometric from Prometheus and not want to store it as an up-down counter. Like, we can always convert it back into an infometric when we send it to Prometheus, but I don't think there's a case where this would impact Like, this is… it's internal to Prometheus, right? So it's not like… anything in the OTLP representation of an infometric would necessarily need to change.
As long as we can round trip it.
**Arthur Sens** 17:21 Yeah, I… I agree. But, yeah, then in the future, let's keep this… This narrative, where… native metadata is separate from info. They… they will… Yeah.
Let's keep the narrative identified.
**David Ashpole (Google LLC)** 17:48 Okay, are there any… are people okay if I open this PR up for review? Are we generally supportive of the idea of stabilizing the way that infometrics are translated into OTLP.
I see krao nodding. Okay, cool.
Bones.
Alright, and then I think there was one more pull request on this list.
Prio, are there any updates you want to give on this?
Oh, it looks like it's ready to merge.
**krajo (Grafana Labs)** 18:38 Yeah, I think it's ready to merge. The one thing that came out of this to me is that what I realized is that For a native histogram.
You cannot tell… If it contains negative observations, like, at all.
Because of the… A little interval around zero point, the zero count.
You just don't know if there's anything zero in that… negative in that. So… I'm tempted to write up some proposal for native histograms, Version 2.
Where the zero count is exactly that, it just counts the number of zero observations.
And… the… The… environment around, or the literary… interval around zero is split into two. A negative, One and the positive one.
And they would be… Like, an underflow bucket in the negative and positive buckets.
Like, you know.
Basically, the buckets are offset by a number, and there's a minimum number, because it's 32 bits.
So you could define underflow, and that would mean that you could actually Tell.
If your small numbers came from positive side or negative side.
I think it would fit everything, but then… then again, it's… it's… I don't know if it's worth… Even trying to do this, because that would impact exponential historians in OpenTelemetry as well.
So…
**David Ashpole (Google LLC)** 20:25 I was gonna ask. Are you gonna fix them in October as well.
**krajo (Grafana Labs)** 20:29 I mean, you could convert from native histograms to exponential… I mean, X… yeah, exponential open territory, because you just add up those three numbers, the zero count and the positive and negative small numbers.
But the other way around it will… Yeah, the other way around it will not work.
So… Yeah, I don't know.
Probably not worth it at this point. It's, Yeah, I mean, people that accidentally or intentionally have negative numbers in histograms, it always sucked, and will continue to suck.
**David Ashpole (Google LLC)** 21:11 We're good to merge this.
**krajo (Grafana Labs)** 21:13 Yeah.
**David Ashpole (Google LLC)** 21:14 Any questions?
I think it's just me from the SIG that has approved.
No, Arthur did approve as well. Okay. And we've got… we've got Quorum.
Cool, so that's one big… and then you still have the pull request to actually stabilize it, right? That we need to reopen?
Yeah. This seems like it's…
**Arthur Sens** 21:36 life.
**krajo (Grafana Labs)** 21:37 Sorry?
**David Ashpole (Google LLC)** 21:41 Arthur?
**Arthur Sens** 21:43 is a one-line PR, right?
**David Ashpole (Google LLC)** 21:46 Ray, I'm just… just for tracking purposes. I was just…
**Arthur Sens** 21:49 shit.
**krajo (Grafana Labs)** 21:51 Yeah, I need to do the stabilize, need to… I don't know if you have… are you in the same meeting with… I want to say Josh McDonald, or what's his name, James McDonald?
**David Ashpole (Google LLC)** 22:04 Josh McDonald.
**krajo (Grafana Labs)** 22:05 Josh McDonald.
Like, I don't… I don't know if he wants to do something about the… reset hint, because he was very, you know.
For defining a different way of working.
And we deferred it, but I don't know if he wants to pursue it.
**David Ashpole (Google LLC)** 22:25 Heat?
I'll tell you… so this is what I told him.
As I said, Prometheus currently defines this.
As very strictly, like, The Prometheus time series database has determined that this is a reset.
And hasn't yet defined this as a, like, generic, stable algorithm for external people to implement.
**krajo (Grafana Labs)** 22:48 Yep.
**David Ashpole (Google LLC)** 22:49 Right? So that's… that's what I told him. And I think that Prometheus Remote, right, has always had, like.
It is mostly a way for you to transfer the contents of one TSDB to another Prometheus TSDB.
And… Like, it's kind of secondarily an open-source protocol meant for Like, other things to adopt?
And that this field is, like, more or less just not today meant for external people to sell. That's what I told them. If that's wrong, then I think we can explore it.
I think… I think there's… he has wanted for a long time for OpenTelemetry to Be more, accurate about How it defines resets?
And we… I think the spec today… Has some, like, discussion of it.
But… I don't know. It's unclear to me if it's actually worth it. It's mostly a performance optimization, right? Where…
**krajo (Grafana Labs)** 23:59 Yep.
**David Ashpole (Google LLC)** 23:59 you can, like, avoid some work in the Prometheus server if you set this field.
**krajo (Grafana Labs)** 24:03 Yep.
Yeah, I mean, we will… again, if you send us that there was a reset, we will not calculate, we will just believe you, but if you say no reset or unknown, in both cases, we ignore you and try to detect.
**David Ashpole (Google LLC)** 24:19 Interesting.
**krajo (Grafana Labs)** 24:20 Because the more critical thing is that You know, if you send a… reset, then it's… I guess it will be probably fine.
Because you base it on something, I guess, so it's probably fine, but if you send us no result, we cannot believe you, because you might be using the wrong algorithm, or wrong data, or whatever. Like, yeah, it's just not a thing.
And the good news is that we are working on the Indeed, Delta.
working for Prometheus on supporting start time stuff. So if you… set the start timestamp, then, you know, the functions in PromQL will understand it, and they will treat it as a result, and you'll be fine.
So… Yeah, the… So I don't think it's worth pursuing.
so far, nobody complained that there was issue. And in the vast majority of the cases, you will not be sending it, so we will do the detection anyway, so it's not like you get a lot of… you know, performance gain, probably next to nothing.
**David Ashpole (Google LLC)** 25:29 I think unless you are interested in reopening this… then it's… Fine to leave it as is, and we will send unknown.
**krajo (Grafana Labs)** 25:38 Okay. The other thing that came out of this is that the compatibility… The spec is not consistent with what's implanted for the normal histograms.
**David Ashpole (Google LLC)** 25:52 Okay.
Which we have stabilized, right?
**krajo (Grafana Labs)** 25:56 I think so.
**David Ashpole (Google LLC)** 25:59 Those are stable.
Not NHCBs, but the regular histogram histograms.
**krajo (Grafana Labs)** 26:04 Yeah.
Yeah, because the… the implementation does one thing, the protobuf does one thing, which is that they have the sun as optional, or explicit, so the normal histograms.
But the spec says.
The data model aspect says, oh, it's mandatory field, when it's not implemented that way.
Okay.
**David Ashpole (Google LLC)** 26:31 I mean, we can fix the implementation then.
I think.
**krajo (Grafana Labs)** 26:41 And…
**David Ashpole (Google LLC)** 26:41 Do you think that's not the right path forward?
**krajo (Grafana Labs)** 26:44 I… I don't know.
Do you mean to say that you would update the protobuf as well? To say that it's mandatory?
**David Ashpole (Google LLC)** 27:03 No, no, it… this is the translation spec, so it just means that if it's not present, we would have to drop the point.
**krajo (Grafana Labs)** 27:10 Yeah, yeah, yeah.
**David Ashpole (Google LLC)** 27:11 One way to solve it would be to update the PromUF, but I think that's a bit much.
**krajo (Grafana Labs)** 27:15 Yeah, yeah, that's… yeah, yeah, I plan to open a PR, and…
**David Ashpole (Google LLC)** 27:18 Okay.
**krajo (Grafana Labs)** 27:18 And fix the… Spoke, yep.
So, two to-dos. One is to… Actually stabilize, and then the other is to… Fixed the, visible spec.
**David Ashpole (Google LLC)** 27:39 Do you remember which components are out of compliance?
Is it the Prometheus Remote Right exporter, or the Prometheus Exporter, or…
**krajo (Grafana Labs)** 27:51 Is the remote ride, exporter.
Wait, wait, what? Yeah, the real trite exporter… The, the, no, the exporter is out of spec.
for… on the NHCB stuff, and also the… the compatibility spec itself.
**David Ashpole (Google LLC)** 28:14 The compatibility spec needs to be updated.
**krajo (Grafana Labs)** 28:18 I think so, yeah.
**David Ashpole (Google LLC)** 28:20 The one we just stabilized, right?
**krajo (Grafana Labs)** 28:22 No, no, we stabilize the exponential one.
This is about the normal histograms.
**David Ashpole (Google LLC)** 28:27 Is this about NHCBs, or… normal histograms, because I thought normal histograms…
**krajo (Grafana Labs)** 28:35 Let me open it up, because I'm getting confused.
So, if I look at… specification, if I look at compatibility, Prometus and compatibility, yeah.
Auto Primetric points to Prometheus… histograms… Yeah, it… so the spec says… For compatibility, going from OpenTeometry to… Prometus for histograms.
Sum is converted to the histogram sum.
But the sum might not exist.
That's the problem.
**David Ashpole (Google LLC)** 29:24 Okay, and so we wanna… It's stable, so we should… I guess this is clarifying behavior that isn't currently clarified today.
**krajo (Grafana Labs)** 29:34 Yeah, exactly, because… The implantation is correct in the remote right exporter, it just doesn't generate the sun, time series, the underscore sun. So it's… so the… so the implantation is correct.
**David Ashpole (Google LLC)** 29:48 Okay.
**krajo (Grafana Labs)** 29:48 spec is wrong, and then for the same for the NHCB. For the NHCB, You cannot just leave it out, so it has to be the same as the exponential histograms, which is to reject the sample, but fortunately, that's development.
Status.
Anyway, I don't want to, you know, take up a lot of time with this. I will just open the PRs.
And, we can take a look in more concretely.
**David Ashpole (Google LLC)** 30:21 Arthur, you have the next one.
And feel free to drop for those who need to attend the Kubernetes Instrumentation SIG.
**Kyle Eckhart (Raintank, Inc. – Grafana Labs)** 30:31 They… they canceled.
**David Ashpole (Google LLC)** 30:33 Oh, they cancel.
Nice.
**Arthur Sens** 30:37 Nice.
Okay, the… My topic is about the compliance.
historically, the OpenTelemetry Collector Contrib repository used the Prometheus compliance repository to make sure that the Prometheus Remote Ride Exporter Sens valid remote exporter, remote Bright, messages.
However, I think Bartek, with a mentee, they did a refactor of the compliance repository.
And it… the compliance repository is now a Go library that is reusable So we can… I… I can… I think there's a… Yeah, the link there, Prometheus itself is running compliance tests within its own repository. Can you click that, David?
Yeah, in part…
**David Ashpole (Google LLC)** 31:42 We could just adopt something like this.
**Arthur Sens** 31:45 Yeah, and this, this, my PR, is doing exactly that.
But… once I got this PR up, we started failing a lot of the compliance tests.
So, yeah, I'm a little bit worried. I don't know if, like, the compliance has some error after the refactoring, or if we messed up remote ride exporter somehow.
**David Ashpole (Google LLC)** 32:14 Either is possible.
**Arthur Sens** 32:16 Yep.
from my understanding as well, the refactoring only tests remote write V2, So we, we are not… That's…
**David Ashpole (Google LLC)** 32:28 I don't know if we implement… er, I think we're mostly implemented, right?
**Arthur Sens** 32:33 Yeah, I saw some errors about, start times.
I think the Prometheus receiver does not propagate the start time, and therefore the remote write doesn't have start time to translate to.
**David Ashpole (Google LLC)** 32:50 We might… oh, maybe we need to use the metric start time processor.
**Arthur Sens** 32:55 Oh, really?
**David Ashpole (Google LLC)** 32:55 Remember, we moved all that logic out.
**Arthur Sens** 32:59 That is true.
So that means that… If we want… Remote write Sens Start Time. We need metric start time processor.
**David Ashpole (Google LLC)** 33:16 Otherwise, we don't… I mean, or you need to… so this is scraped metrics, right, on the Prometheus receiver?
Or is this metrics received via Prometheus remote, right, too?
**Arthur Sens** 33:27 No, the compliance suit, has an application running, and we need to scrape.
And they compared the remote ride to… With what they expect from what is being exposed in the app.
**David Ashpole (Google LLC)** 33:45 how does Prometheus get start times? Did it also add, like, logic to drop the first point? Okay, okay. Yeah, so this… they added the… it's funny, because, Bartek… Bartek was like, oh, look, you're dropping… dropping points and making start times, and this is really cool, like.
we should do this in Prometheus, and, borrow the… some of the logic, so…
**krajo (Grafana Labs)** 34:08 Yeah, I'm…
**David Ashpole (Google LLC)** 34:09 should work with the Prometheus, or with the metric start time processor.
**krajo (Grafana Labs)** 34:14 I'm really against that. That's a workaround in my book, what Prometus… what they put into Prometus with the mountain.
Gross.
**David Ashpole (Google LLC)** 34:21 I wouldn't have expected that to be opt-in, at least.
**krajo (Grafana Labs)** 34:25 Yeah, it's a feature flag. Like, I… I will… I will never let that be stable, basically. I… I think… We should update the… client libraries to emit open metrics to and have start time properly.
**David Ashpole (Google LLC)** 34:41 100%. I… I agree.
But okay, so the Prometheus Compliance Suite is using that feature flag, then?
Yeah, I mean, I guess we…
**Arthur Sens** 34:55 If you go some lines below, you'll see the pigeon flags.
**David Ashpole (Google LLC)** 35:04 Start time storage… XOR2 encoding.
Hmm…
**Arthur Sens** 35:16 Oh.
Only SD storage is enabled.
**David Ashpole (Google LLC)** 35:22 I mean…
**Arthur Sens** 35:22 Wait, the Prometheus parser… This handle is start time.
**David Ashpole (Google LLC)** 35:31 Yep.
But the question is whether the target being scraped has…
**Arthur Sens** 35:35 So the Prometheus receiver also does, because it uses Prometheus code.
**David Ashpole (Google LLC)** 35:40 Right? So, but we may… there may be some disconnect there.
That's very, like… I would probably trust the compliance suite, unless they're turning on weird features.
We.
**Arthur Sens** 35:52 Yeah, I'm… I'm not so sure.
If I have to trust the compliance.
Yeah, I feel like there… some weird stuff happened in the refactoring, and yeah, I'm not sure, though.
I don't know who to trust, to be honest.
**David Ashpole (Google LLC)** 36:11 Probably, probably clawed.
**Arthur Sens** 36:14 Yeah.
**krajo (Grafana Labs)** 36:16 Never.
**David Ashpole (Google LLC)** 36:19 Never.
**Arthur Sens** 36:22 Okay, yeah, this is mostly to let you all know that I'm trying to get… The compliance to work again.
And it's not really going smoothly.
**David Ashpole (Google LLC)** 36:35 So, do you need help?
It would be helpful, maybe, if you documented the things that are failing, so we can…
**Arthur Sens** 36:42 Yeah, yeah, I need to put more time into this. I'll let you all know.
**David Ashpole (Google LLC)** 36:46 Okay.
Okay, cool.
We have 15 minutes left, so hopefully we can at least, krao and Arve bring, Arthur and Kyle.
Up to speed on job and instance.
Sound like a good plan?
Okay.
Let's see, I will start talking, but Arve and krao, please jump in if you feel like there's, stuff you want to add.
Okay, so… let's… let's start with the problem, and I think I'll actually jump So, first.
I would recommend against trying to read this document. It's become… so long, and the actual proposals being discussed are, like, at the bottom instead of at the top. So, We can discuss it here, and then we can maybe try and Come up with next steps.
If we look at the problems that exist today, right, that this… that this is looking at. So, there's a few kind of funny things that exist today.
The main one is that when you scrape, a Prometheus endpoint.
That has a target info metric with service.name on it.
Right, so, like, an OTel SDK with a Prometheus exporter.
Let's go, maybe, to the table here.
At krao's table. See if we can find it.
Can everybody see this? It's kind of zoomed in, isn't it?
**Arthur Sens** 39:10 It is.
**David Ashpole (Google LLC)** 39:10 Moving over here.
Does that help at all?
**krajo (Grafana Labs)** 39:14 Oh, yeah.
**David Ashpole (Google LLC)** 39:15 move it to my 4K screen.
Okay… Is this the best we can do. Can people see this?
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 39:27 Yes.
**Arthur Sens** 39:28 Yep.
**David Ashpole (Google LLC)** 39:29 Okay.
**krajo (Grafana Labs)** 39:29 You can call out the comments, by the way.
**David Ashpole (Google LLC)** 39:33 Oh yeah, good idea.
Did they go away? No. Collapse.
There we go. Did that do it?
I've just moved it over.
Hmm.
Okay, so I think the first thing that happens today is that when you… My goodness, there's so much here, I can't find anything.
This is… krao, this is your table, right?
Default translation, so… The one thing that… so the fir… today is the column that I want you to pay attention to.
So, if you have an OTEL SDK, with… a Prometheus exporter.
Today, this is roughly what you get by default, so you'll end up with your target info metric, and that will have a service underscore instance underscore ID and service underscore name here.
And when that gets scraped by the Prometheus receiver.
You end up with a service name, That's your job.
you end up with a service instance ID that's your instance.
And then you end up with a service underscore name, that's your actual service name, and your service underscore instance underscore ID, which is your instance ID.
So you end up with this, like, duplicated scenario.
Then if you… either send that via OTLP to Prometheus, or if you use the Prometheus Remote Write exporter.
then you end up with something that looks a little bit more sane, right? Where you have Your job set to your original scrape job, your instance set to your scrape instance.
Your service name with an underscore.
set to your service name and your service instance ID, again, with underscores.
Set to your service instance ID.
So… Today, this round trip, it maybe makes some sense, right, where you have job and instance set normally, and these, because you weren't Because you were doing underscore escaping, they end up underscore escaped.
When we go to the UTF-8 version, right, so if you today have no translation turned on everywhere.
Or… the UTF-8. No UTF-8 escaping.
Things change slightly, so… Your target info metric on your endpoint.
instead now has service.instance.id, right, and service.name.
And then… in the Prometheus… the Prometheus receiver, it's actually the target info metric that takes precedence over the scrape labels, right? So you end up with service.name is your service, service.instance.id.
Is your instance, and then your scrape job and instance are actually dropped in this case.
**Arthur Sens** 42:32 We have different behaviors for driving instance, depending on UTF8.
**David Ashpole (Google LLC)** 42:38 Yes, so that's… that's one of the dimensions this problem, right?
So, right, one problem is that this is… different.
Right? Oh, and let's complete the story, just so that we're complete. Then when you send this via Prometheus RemoteWrite, or via OTLP, you end up with, job is my service, instance is my instance ID, And that's all you end up with. So you don't even have service instance ID.
Preserved anywhere.
everybody… everybody following so far? Are there any questions about what happens today?
**Arthur Sens** 43:16 How did we get to this?
**David Ashpole (Google LLC)** 43:19 So… I can answer that, but I don't know if that's actually useful, so maybe let's say that Are there any questions about how it works?
Or, like, what the scenarios are.
**Arthur Sens** 43:32 No.
**David Ashpole (Google LLC)** 43:33 Okay.
So let's… let's for now ignore option A, so just don't pay attention to that column.
Let's go through… So let's go through the goals then, right? So, some of the goals… the main goal that we actually wanted to come out of this is that in the UTF-8 case.
Right, so this case here.
It would be nice to preserve job and instance somewhere.
Right, so that's… that's, like, the main thing that I think all krao and Arve and I agree on, is that, dropping data seems like At least not ideal.
**Arthur Sens** 44:17 Yep.
**David Ashpole (Google LLC)** 44:18 And then we disagree on some of the other things that came up.
But let's… let's talk through, first… option B, which was, So option A is what's currently in my pull request upstream. Option B is the same as option A, But… Instead of… the literal strings job and instance, it uses Prometheus.job and Prometheus.instance.
So I… Art… Arthur and Kyle, are you… Have you read through the pull request upstream, and do you understand it, or should I go over what it proposes?
**Arthur Sens** 45:03 I, I read before my PTO. Okay, so I should go over.
**David Ashpole (Google LLC)** 45:08 So, let's go over… Basically, it might even just be easier to walk through it, so… the text exposition from the SDK is always the same.
The interesting thing starts here.
Where… Here we have… Prometheus… instead of… The job… Let's see.
Your job would become Prometheus.job in the Prometheus receiver.
And… your service Let's ignore these for a sec, because we had discussed removing them.
Your job becomes Prometheus.job, your instance becomes Prometheus.instance.
And then this is the scenario with UTF8, or with the underscore escaping still applied. So you have service underscore name.
and service underscore instance underscore ID.
So you'd end up with… job as my job, instance as… or Prometheus.instance as your instance, your service name as your service name, your service instance ID as your service instance ID.
then when you export that… if you export that with Prometheus RemoteWrite, or via OTLP to the Prometheus receiver.
You would end up with… Let's see, where's your target info? Here we go. You would end up with job as your job.
Instance as your instance, service underscore name as your service name, or sorry.
Wait, why is this?
I'm slightly confused by this.
Wait, sorry, one sec.
Meetings.
I don't… you would just end up with service underscore name is my service, and service underscore instance underscore ID as my instance ID. I don't think this is correct.
But that's basically… The same as what you have today.
Cryo, did you want to say something?
**krajo (Grafana Labs)** 47:26 No, yes, for reference for… to clarify for the others. The tables are made with clothes, not everything is… Verified 100%, and there's… the algorithms are in flux, so my plan would be to POC… these options that remain, and run it through a testbed. I already have, like, a small test program, and I have, like, the collector, so I could verify up to the… what the collector sees as the model with the debug exporter, but then I need to add the other stuff. Like, it's just… even… even Claude is making mistakes sometimes. Like, it's so hard to follow through, so, yeah, we just… we need to verify.
**David Ashpole (Google LLC)** 48:17 Cool.
But I believe that this option, when it gets back into Prometheus format, looks identical to what it is today, where job is job, instance is instance.
And service name has underscores, and service instance ID has underscores. Basically, you can think of this path as, while it's in OpenTelemetry format, job and instance have a Prometheus prefix.
But that's removed when it gets back to Prometheus.
And that is for the… That's for the case where we're substituting dots with underscores.
Okay, now for the case where we have no translation, right, so we are leaving the dots in.
The first difference starts here. So when it gets to the Prometheus receiver, Currently, we are… Dropping job and instance, right?
Now, Java and instance would be preserved as… Prometheus.job and Prometheus.instance.
and service instance ID, or service name and service instance ID, would stay the same in this case.
And they would be set to the service name and service instance ID from your target infometric.
And then when it gets back to… Prometheus.
Today, job becomes your service name, and instance becomes your service instance ID, Now job would become… your job.
Instance would become your scraped instance.
And… your service.name, I'm just gonna fix this instead of… having a comment here, would be your service name and your service instance ID would be your service instance ID.
This is a change from what currently exists today, because your job would change, and your instance would change.
And you would gain your service instance… your service name and your service instance ID as resource attributes.
Are there any questions about option B?
**krajo (Grafana Labs)** 50:31 Just a comment that, basically, You fix the inconsistency that is caused by the… You know, difference between… Using underscores and not underscores in the job label.
But it is breaking.
**David Ashpole (Google LLC)** 50:56 Let's see, I can't see your faces, so let me… Arthur or Kyle, any questions?
Or do you feel like you have a good understanding of… Essentially, more or less what it… what it proposes.
**Arthur Sens** 51:10 I, to be honest, I'm still a little bit lost.
**Kyle Eckhart (Raintank, Inc. – Grafana Labs)** 51:13 I feel good about the end state, it's a lot of the middle points.
Right? Like, there was the, like, it looked like, you know, hey, we're gonna prefix it, but that's only for actual, like, in-processing. We'll translate it out at the end, which I think was the most important part. It's, like, someone who knows Prometheus.
they'll see Javin Instance, and then, like, Javin Instance preserved, and then someone who's also hotel will see service, name and service, instance preserved.
**Arthur Sens** 51:40 Yeah, but, like, in the collector, that makes sense, because in the collector, we want to get data in, and then we get data out.
In the Prometheus, we only have data in, we're not sending data out.
So, in Prometheus, we… under option B, we would have Prometheus.job instead of job there. Is that it?
**David Ashpole (Google LLC)** 52:04 So as soon as it gets to Prometheus… so you can think about it as when translating from OpenTelemetry, or when translating from Prometheus to OpenTelemetry, you… add the Prometheus prefix to job and instance.
When translating back from OpenTelemetry into Prometheus.
you strip the prefix from Java instance.
**Arthur Sens** 52:33 Okay, so it… OTLP, when we've seen PTO… okay, I think I understood.
**David Ashpole (Google LLC)** 52:41 So that's the simplest way I could try and explain this, how this would work, is that it… and it's maybe even simpler… I said we weren't going to discuss option A, but option A is… leave Java instance.
as the literal strings J-O-B, and however you spell instance.
While they're in the Prometheus, or while they're in the OpenTelemetry data model, so…
**Arthur Sens** 53:04 Yeah.
**David Ashpole (Google LLC)** 53:04 in your OpenTelemetry collector, you would get Java instance.
And then, when it gets back to Prometheus, it would stage off an instance.
**Arthur Sens** 53:12 Then, krao and Arve were saying that option B is breaking?
**David Ashpole (Google LLC)** 53:18 Option… well, so, the key here is that, look at today's state.
Right, today, job is set to your service name.
An instance is set to your service instance ID from your target infometric.
So, if we set it to your… your job to your scrape job name, and instance to your scrape instance… That's a change from what we're doing today.
**Kyle Eckhart (Raintank, Inc. – Grafana Labs)** 53:46 Every, every option's a breaking change, from the looks of it.
**David Ashpole (Google LLC)** 53:51 No. Well, so, if you consider a label addition, to be… Non-breaking, then… the final option, option C here, is purely just… it's keeping job set to your service name, and instance set to your service instance ID.
But it's now preserving prometheus job.
and Prometheus Instant as separate resource attributes, similar to… other resource attributes.
So basically, instead of dropping job and instance, as we're doing today.
We're just preserving them and attaching them as net new resource attributes at the end.
This… this is still inconsistent with B… Behavior that you get.
If you are sanitizing dots to underscores, right, the default, underscores gaming with suffixes behavior.
But it's not breaking from today's behavior that exists in the Prometheus receiver.
Actually, let's walk through option C. Do people feel like they have any more questions about option B before I walk through option C?
Oh, and we are out of time. Are people… Interested in continuing, or do we want to table this?
**Arthur Sens** 55:21 I do need to drop, by the way, feel free to continue.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 55:24 I also have…
**David Ashpole (Google LLC)** 55:24 We'll have to be…
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 55:25 I have to drop also, yeah.
**David Ashpole (Google LLC)** 55:29 Then maybe we can pick this up.
at a future point.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 55:33 Yeah, obviously.
**David Ashpole (Google LLC)** 55:34 Obviously, Arthur… obviously, Arthur, I think we're very interested in your opinion on this, because we've For quite a bit.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 55:41 krajo, are you done with your Tableau representation, or do you need to add more use cases to it?
**krajo (Grafana Labs)** 55:49 I want to, like… again, POC, the options, B and C, I don't believe in A, and, run it through, and actually, like.
Verify everything in the tables that we have, that they are 100% correct.
And, there is one more use case that I want to… Well, update, not add, but just update.
And in general, I want to think about what's more important here?
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 56:19 So it's… maybe it's best if we have the… we have the full discussion when the table is, done.
Right? Yeah, exactly, and it's like, yeah, I think… I think that this will be the best starting point for a full discussion.
And yeah, and as we discussed in the previous call, I mean, there were some details in option C that need to be fixed from my side.
So, I'm going to do that.
**David Ashpole (Google LLC)** 56:47 Arthur Cryo Arve.
Kyle, is anyone interested in joining a call next Friday? That's sooner than our Two weeks from now, scheduled call.
Or should we wait 2 weeks before we talk again?
**Arthur Sens** 57:05 I… I can join, if you… if you want.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 57:10 I think I can join next Friday. I mean, I don't see any blockers in my calendar, at least.
**David Ashpole (Google LLC)** 57:15 Thanks.
My calendar's pretty open on Fridays, Do we think we can, do the action items and reconvene by… by then?
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 57:29 What do you think, can I…
**krajo (Grafana Labs)** 57:30 Yeah, I think, again, if the… Like… Yeah, please update option… C, and B, just take a look if they need to be very precise, basically, for me to do the POC.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 57:45 Yeah.
**krajo (Grafana Labs)** 57:45 generate code from it. If I don't manage that, I will reach out to you, but I think it's doable by now.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 57:51 I'm going to try… I'm going to try to fix up option C by Monday, but you can reach out to me, krajo if… If you have anything I should be fixing.
**krajo (Grafana Labs)** 58:00 Cool.
**David Ashpole (Google LLC)** 58:02 Awesome. Thank you, guys.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 58:04 Thank you so much, everyone.
**David Ashpole (Google LLC)** 58:05 Next week.
**Arthur Sens** 58:06 Bye.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 58:06 Regardless. Bye-bye.
**krajo (Grafana Labs)** 58:08 Bye-bye.
