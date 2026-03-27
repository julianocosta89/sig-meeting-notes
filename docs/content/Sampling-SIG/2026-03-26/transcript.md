SIG: Sampling SIG
Date: 2026-03-26
Duration: 22 minutes
Zoom Recording URL: https://zoom.us/rec/share/5mClZWdmqRX6fQNjVsLnrkq37AU3zkmukSw14TpfJKQctahwkjIAwfi7GWCEMPqn.b1NWS4OE4ewYgu0c
============================================================

## Zoom Recording Transcript

**jmacdonald** 00:33 Hi, Chris.
**Chris Marchbanks** 00:34 Good morning.
**jmacdonald** 00:35 Morning.
Well, I always like when these meetings are short, but it's also nice to have them to talk about things that are important.
So, in the last week, let's see, I was gonna just do this while we talk. In the last week, I saw an important Slack thread between some of us, you and… I guess it was Yuan Yuan, and you, and Peter, I think.
**Chris Marchbanks** 01:06 a little bit, yep.
**jmacdonald** 01:08 And we have 3 of us here, and… So I thought we could just run through that conversation briefly, and… I'm gonna call it that, and then I know Yuan Yuan has asked me to review a PR, which I'm going to do.
And I will… Just for fun, put a link to that. This is adding a trace ID ratio sampler in Go.
Come on.
Anyway, there it is. Okay, so, so… Nguyen Yuan has joined us, cool. View on… So, the topics that we have… I was just going to run through that Slack conversation. So, the way I recall our history here, we have… definitively defined TH0 means adjusted count 1 of known sampling probability, and then we have this unknown case, which is a missing TH value, and over the time, we've discussed ideas about what to do when you see this legacy, and Peter has been, I think, the guiding light on this, and I respect the position, which is to say, unknown. You don't know anything if you see no TH.
And that gives you an opportunity to add one, to count for one if you want to, like, wave your hands. Gives you count to count zero if you want to wave your hands. It's just an unknown.
**Yuanyuan Zhao** 02:48 Yeah, so the current behavior, we implemented in the spam metrics connector is to calculate as one, because that's backwards compatible, right? Today, with nothing before our change, it's calculated exactly as one.
So we are keeping that behavior. What we did additionally is to, add a attribute.
that specify how, the Kant, came into place. Is it just the content? Is it extrapolated? Or that's just a nothing, right? It's, so people can distinguish it.
from…
**jmacdonald** 03:40 Right, so there's two attributes, as far as I recall, and they just tell us whether we were making…
**Yuanyuan Zhao** 03:44 Do what?
**jmacdonald** 03:45 up.
**Yuanyuan Zhao** 03:46 One attribute. Two values. Two values. You actually suggested, I think.
**jmacdonald** 03:51 No, no, no, that's what I meant, that's what I meant. One attribute.
**Yuanyuan Zhao** 03:53 Right.
**jmacdonald** 03:54 The attribute is named… Temple.
**Yuanyuan Zhao** 03:57 a method.
**Chris Marchbanks** 03:59 find it. Anyway…
**jmacdonald** 04:01 The point is, yes, absolutely.
**Chris Marchbanks** 04:03 There's an attribute that tells you, yes, was this extrapolated? Was it… okay.
**jmacdonald** 04:07 That gives you the opportunity to, like.
**Yuanyuan Zhao** 04:09 Yeah.
**jmacdonald** 04:10 adjust.
Bye.
Yeah. You can always count those for zero by just not summing that portion, or whatever.
**Chris Marchbanks** 04:19 Yep. That…
**Yuanyuan Zhao** 04:20 So, I just want… I mean, this is probably obvious, but I just, wanted to bring that explicitly, is that if you have TH0, right, then that, that's gonna… count as but the distinction of this is that you are going to get The, sampling method is extrapolated Versus counted, so that they belong to, the same stream.
I, because, like, if people are adjusting their sampling rates, they could change, so you will get things Continuously within… Yeah.
**Chris Marchbanks** 05:03 Yeah. Cool.
So yeah, I basically implemented the same thing in Tempo last week, so yeah, we used slightly different code there for legacy reasons, but yeah, it does the same thing.
that it works backwards compatible. If there is no TH information, we will count it as one. It does leave, like, this unknown case… there's not really a user choice in this? Like, we started this discussion with, the user can choose to count it as 0 or 1 in this unknown case. That's not really what's happening, I guess, because… all of the processors I know counted as 1.
So is that something we'd like to support? Like, is it worthwhile supporting some state of, I know that this exists, I know that this should not be counted, basically? Like, is that worth supporting?
I'm kind of on the fence.
I can live with… I can live with this, it's okay.
I think.
**Yuanyuan Zhao** 06:05 I think that, we, previously in, some of the SIG meetings, were mentioned something related to this that, in case we didn't know, still counted in some way, so we get some information out, right? And then… so that's… if I remember it correctly, I see, Josh nodding, and Peter… didn't, but… but Peter was probably on the same page. That's how I remember. Just speak out, I shouldn't put words in your mouth. But, the thing is that If we still count it, right, now we also have the attributes to, distinguish, them, or the lack of attributes. I think that,
**Chris Marchbanks** 06:56 The attributes only help after, like, your metric is already potentially incorrect by the time those attributes are added, right?
**Yuanyuan Zhao** 07:06 Yeah, it's better than nothing, I think that was what we…
**Peter Findeisen** 07:12 Right.
**jmacdonald** 07:12 Yeah, and I was… I was thinking you could, intentionally exclude the attribute… the attribute, and therefore avoid the incorrectness, but you're… you're right. In some sense, you've made the mistake already. This does get back to a topic where… my thinking has changed so much on this over the years, and we've made real progress, but I did, at one point, have a sort of hobby of talking about zero-adjusted count.
It has to do with my learning path for weighted sampling, which is, like, you open up the paper on weighted sampling, and you read through it, and you're like, finally get to the point where there's, like… and some of the ones that you don't choose, we're just going to call that adjusted count zero. Like, zero means the same as selected with no weight and not selected.
And… And I… and I have… studied reservoir sampling algorithms with great interest, thinking, this is cool, I want to figure out how to apply this. And very often, you end up Having things come out of your weighted sample that are zeros, because they don't count.
And then, in these earlier days.
we were having this debate about, well, I want to have a sampling policy like Peter has now described for us, which says, I want all the errors, and I want 1%.
And if you end up with all the errors in 1%, that some of the spans coming through are going to be errors that were not selected by the 1%. Those are zeros.
Or they're ones. And that has been the, like, philosophical debate that we've had here, which is to say, you wanted all the errors, they are one for one, count them as one, call them TH0. And my original thinking was.
I have two things going on, two policies. One is probability sample flat, and one is all errors. And if I stream those two together, some of them should have zero count. That was what I was pushing for so many times. But eventually, Peter and Atmar convinced me that we were better off just looking at that error case as a sampling of one.
It changes the way you analyze a bit.
**Chris Marchbanks** 09:16 Yeah, it would require… so if we see a cent… like, if… If there was a policy anywhere with 1, Because, like, what you wouldn't want to do is, on one of these errors that happened to be sampled by the 1%, Counted as 100.
Because you have all of them. So that's what you would have to be careful about, right?
**jmacdonald** 09:41 Yes, and I believe the work that Peter did with OTEP250 will give us that 1.
Correct.
**Peter Findeisen** 09:46 Yes.
**jmacdonald** 09:47 And so I've forgotten about zero adjusted count. It just keeps coming back like this.
**Chris Marchbanks** 09:53 Okay.
That, to some extent, makes sense. I'm trying to think, so, like… Where I ran into this some is specifically, like, customers running tail sampling. I would like to have tail sampling… Basically, be able to say this was something that was sampled or not.
like, accurately, and be able to run metrics still after tail sampling, which is annoying to do, and only works on some of the sampling policies. Like, you can't do errors, you can't do latency, etc.
So I'm trying to think if this… that would work… I think we would have to modify… like, we would have to have the tail sampler modified TH in such a way that those are only counted as one.
Right.
**jmacdonald** 10:50 Okay, this is a tail sampling situation.
Peter, please.
**Chris Marchbanks** 10:54 Yes.
**Peter Findeisen** 10:55 So… so if I understand correctly, you have… You have sound traces with errors.
which you… which already have a TH value, which is not 0.
Right.
**Chris Marchbanks** 11:12 Yep.
**Peter Findeisen** 11:13 And you want to keep all of them.
**Chris Marchbanks** 11:16 Yep.
**Peter Findeisen** 11:17 You need to preserve the TH value, because you need to know what was the original number of traces with errors.
**Chris Marchbanks** 11:27 Okay.
**Peter Findeisen** 11:28 So, you… you… we should not… modify the TH value, unless we are… Looking at the randomness of the trace.
**Chris Marchbanks** 11:41 Okay.
**Peter Findeisen** 11:43 So, there is a very tight connection between the TH value and the randomness value.
We cannot… we cannot break it.
Because further sampling steps, if any, will get completely confused by that.
**Yuanyuan Zhao** 11:59 Right.
**Chris Marchbanks** 12:01 Okay.
That makes sense.
Okay, I'll give that some more thought. I think I agree with this analysis that we can… It is okay.
**Yuanyuan Zhao** 12:13 Yeah, were you in that Slack thread? We were discussing this?
**Chris Marchbanks** 12:18 Yes, yeah.
**Yuanyuan Zhao** 12:19 Yeah, that was what I was eventually saying, that the TH value has very specific meaning, and it's tied to the algorithm. But what you are, bringing up is actually a case that, we also encountered is that it's several stages of sampling. And one plausible way is that another algorithm that does the sampling downstream put in their own some kind of… Like, the sampling rate thing, something we actually call the PSR.
The internal tag. So, with that information, then downstream you can piece together, but you will have to understand both something algorithms in order to… calculate whatever downstream information you want. But the idea of that, each algorithm does the sampling, pulling their own stuff To preserve the information, I think that's probably safe.
to proceed then modifying TH. Eventually, the idea is that if the two stages of sampling are orthogonal criterias, then what you get is actually the product, right? The multiplication of both, but how you achieve that result, then there are different approaches, and modifying TH It can be very dangerous.
**Chris Marchbanks** 13:55 Okay. I… yeah, I think I'm convinced this is okay, I'm gonna give it a little bit more thought.
Yeah, I'm trying to think of the…
**jmacdonald** 14:05 Are you using the tail sampling processor, Chris?
**Chris Marchbanks** 14:08 Yeah, we use…
**jmacdonald** 14:09 The one true tail sampling pasta.
**Chris Marchbanks** 14:12 And we have some customers that use it, and we have some customers who use something else, too. Like, they have their own little, whatever, customized things. Because, like, this is both internal and, like, people sending traces to Grafana Cloud, and they can do whatever they want to their traces before they send it to us.
**jmacdonald** 14:32 this gives me questions, but I don't know how to phrase them. Actually, So I've also looked at the tail sampling processor and tried to imagine how you could Indicate its sampling probabilities, which is what we've been talking about.
I… this is not a… this is a… this is a complicated one. I know that… that there has been talk in this room of, what is called adaptive sampling. There's, like, a pretty nice paper that was published a few years back that basically says if you have a randomization function and you can at a threshold you would like to establish. You can do that, and then you can re… re-weight the ones that make it through your sample, and I was trying to understand how you know, I have torn apart the tail sampling processor a bit, and… like, it starts to run out of memory, and it just drops stuff. And at that point, I was thinking to myself, wouldn't it be cool if I could take my bucket, sort my traces by trace ID, cut some of them out, adjust my sampling probability.
But I'm doing it by trace… by randomness, so the intention is to use the same randomness function, and therefore somehow modify the threshold, but… I find myself with conceptual mistakes here. Like, there's some gap in my thinking, and I wasn't quite there.
**Chris Marchbanks** 15:58 Yeah, yeah.
**jmacdonald** 16:00 Like…
**Chris Marchbanks** 16:00 The other one that we very much want to implement, like, we're working on implementing is… Like, it's effectively… Yeah, yeah, it's calculating, like, okay, I see traces that look like this, I'm going to give them This pers- this chance of going through.
And therefore, I am going to have to change that, like, I am going to have to modify TH in that case, because, like, traces from this service, and this operation in this service are going to have a different… weight to them compared to even other operations in the same one. And that's going to be, like, the idea is that that will just work. Somebody isn't configuring it at all.
**jmacdonald** 16:43 Okay, I suggest, Chris, that we continue this thinking after some pausing to think more. I think there is a… we have a shared interest, I think, in improvements to the tail sampling processor that would give us what we're looking for, and it's not easy.
Is the way I think about it.
And, yeah, I'm sure that we can talk about it in this room. Peter can help us, with his thinking. That would be great.
Alright, well, I think we've wrapped up that topic.
And as far as agenda, I started looking at Yuan Yuan's PR. I… it… so far, exactly what I was expecting to see, so I will keep reading it after this meeting, and just… Given approval.
Is there any questions?
**Yuanyuan Zhao** 17:35 They are… I want to point out that, there are a couple of, nuances, that might be a bit different from your… I mean, this is basically having what…
**jmacdonald** 17:48 Yeah, let's pull it up. Here it is.
**Yuanyuan Zhao** 17:51 Josh is doing. It's… it's a bit too small, let me see whether I can…
**jmacdonald** 17:56 Yeah, sorry, I'm, I'm not, I'm baking it, begging it.
**Yuanyuan Zhao** 17:59 Okay.
**jmacdonald** 18:00 Here we go.
I was… I was right about in the middle here, where I looked at this This is the part where we do not put a randomness value in.
**Yuanyuan Zhao** 18:10 That's right.
**jmacdonald** 18:11 Yep, so I've seen what I expect to see. This is different than what I wrote, because we evolved the spec a bit.
**Yuanyuan Zhao** 18:17 Right, so I just want to make sure you are aware of the change, and raise if you're opposed to this change, or you're okay with it.
**jmacdonald** 18:28 So, like, scan through this. So, we're saying, we look for the existing threshold. If it doesn't have one, we, Existing hotel trace state, so if it doesn't have one, we make up a randomness.
And then if it doesn't have… we get the randomness from the trace state. If it doesn't have one still, we make one up.
But if we make one up, we're never gonna encode it. That was Peter's rule. If the threshold doesn't meet randomness, we're done here, just drop it. And then… This is the… this… this is the tricky bit, I think.
**Yuanyuan Zhao** 19:03 That's right.
**jmacdonald** 19:04 to get right, but I saw it, so good, we're on the same page. So, if you didn't have randomness, we're gonna… we're gonna erase the threshold.
Again, Peter's rule.
And if you did have randomness, or the randomness flag was set, then you can Update the trace threshold.
So that's where I was. It looks good to me. I will keep reading the rest of it.
**Yuanyuan Zhao** 19:28 Good. So, there is this part of insert.
Alright, we're trying to insert that. So the API… Well, return.
the.
**jmacdonald** 19:43 Oh.
**Yuanyuan Zhao** 19:44 Go down, go down.
**jmacdonald** 19:45 Yeah, yeah, yeah.
**Yuanyuan Zhao** 19:46 is in insert, or app.
Up. Maybe 84? 84, 984 of sampler.go.
**jmacdonald** 19:56 Okay, my A4.
**Yuanyuan Zhao** 19:58 Right, so we are trying to insert, the new, OT value into the key OT. This It complains about a coverage, because… but it's… this is actually not just gonna happen.
**jmacdonald** 20:16 Okay.
**Yuanyuan Zhao** 20:17 because OT is valid, a valid key, so this insert will fail if you don't have, like, a valid key, like, the format, the syntax, and new OTTS, and it's, so…
**jmacdonald** 20:32 This is not covered by the test.
**Yuanyuan Zhao** 20:34 Yeah, but trying to get it covered is just artificial.
**jmacdonald** 20:38 Yeah, I know.
**Yuanyuan Zhao** 20:39 very hard to do, so that I want to point that out.
**jmacdonald** 20:42 I think that's a fair reason to not cover something in a test. It's unreachable in some sense.
**Yuanyuan Zhao** 20:47 Yeah.
**jmacdonald** 20:47 But I also feel like…
**Yuanyuan Zhao** 20:49 You have to kind of, like, you know, make the… make that pass.
**jmacdonald** 20:55 the Go SDK's library interface for trace data is quite heavyweight, unfortunately. Like, this call has so much error checking. Like, come on, I just wanna… Just instrumenting a little bit here. Okay, but yeah, I, I don't worry about coverage issues like that, but I do like to get as much as I can, but this, you know, if you can't get something, it's not worth extraordinary measures.
Yeah.
**Yuanyuan Zhao** 21:20 It just had that glaring… Red Cross in, from.
**jmacdonald** 21:27 I mean, this bit is the same as the thing…
**Yuanyuan Zhao** 21:30 Of course!
**jmacdonald** 21:31 Yeah, yeah, yeah, I remember this. We have another copy of this somewhere we could point at. I might make that comment, but otherwise, just for the reader.
Cool. Yeah.
I love reading tests. Look how fast I can read them.
And, okay, so this is, A little bit of manipulation.
**Yuanyuan Zhao** 21:54 I simplified it a bit, because, yeah, I think you had a broader case of, merging and multiple kind of… Yeah, yeah.
**jmacdonald** 22:06 I've, I've tried to implement this many ways, many times, Like, remembering where you parsed something so you can make it faster, whatever, I… yeah, I remember that.
Okay, well, I will read this more carefully when I'm not standing up, right after, in fact.
**Yuanyuan Zhao** 22:24 Right now, in fact.
**jmacdonald** 22:25 If… unless… unless there's more agenda item.
I would say that I'm gonna go do that.
And we conclude the call.
**Yuanyuan Zhao** 22:34 That sounds great.
**Peter Findeisen** 22:35 I just wanted to say that I am on vacation in two weeks, so I will miss the next meeting.
**jmacdonald** 22:43 Thank you, Peter. We appreciate your being here.
See you in a month, then, or so.
**Yuanyuan Zhao** 22:48 Enjoy your vacation.
**Peter Findeisen** 22:50 Thank you.
**Yuanyuan Zhao** 22:50 Yeah.
**Chris Marchbanks** 22:51 Thank you.
**Yuanyuan Zhao** 22:51 See whether I want to take some time out. See you guys. Bye.
**Peter Findeisen** 22:55 Do it bye.
