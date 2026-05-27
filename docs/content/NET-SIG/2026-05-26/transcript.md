SIG: .NET SIG
Date: 2026-05-26
Duration: 12 minutes
Zoom Recording URL: https://zoom.us/rec/share/HSBNicO8wQ_gA3QAZyWwlRCtOnVmfQ3C5e31Dkm_VO3i5kbbbD_CC4-XyKuvI1YB.2AsSOKZCEyVZPVud
============================================================

## Zoom Recording Transcript

**Julius Koval** 01:13 Hi, how's it going?
**Rajkumar Rangaraj** 01:19 Hey, it's going good for me. How are you?
**Julius Koval** 01:22 Yeah, I'm fine, thanks.
**Alan West** 02:03 Hey, everybody.
**Rajkumar Rangaraj** 03:12 Am I still audio? Like, my headset has changed. Just wanna check.
**Alan West** 03:17 I can hear you now.
**Rajkumar Rangaraj** 03:19 Cool.
I think Julius has a topic, like, Can we start with that? Let me go ahead and share my screen also now.
Meanwhile…
**Julius Koval** 03:50 Yeah, so a few weeks back, I… I guess almost 2 months, actually. I created this PR for, Which would allow the protocol serializer to serialize key-value lists, essentially.
And, So, Martin noted at the bottom that it's basically waiting for at least one other approving review, so… I guess I wanted to ask someone if they could take a look.
**Rajkumar Rangaraj** 04:25 I will take a look at this.
Don't think we were aware of this, and… If I recall correctly, we did not want to do this for the both reasons. So, let me take a look at it.
**Julius Koval** 04:44 Sorry I mentioned that you didn't want to do this.
**Rajkumar Rangaraj** 04:47 Yeah, we didn't want to… When I did the… most of the serialization part, this was… the topic came around that time.
And we did not want to, serialize the key-value list separately, because it's… some perf considerations, because of that, we left it off. Let me go ahead and figure out the context, and then take a look at this one.
**Julius Koval** 05:12 Okay, cool.
**Rajkumar Rangaraj** 05:22 Any other topic from anyone else?
**Alan West** 05:29 A small thing that I… Had missed… One second, what was the… PR.
Raj, you had pinged me a while back about… Number 7160.
**Rajkumar Rangaraj** 05:54 Number 7160, let me go.
**Alan West** 06:03 I forgot to bring this up, and One of our recent meetings, I just wanted to check in one more time. My opinion was basically that we should just not make this change for now, but I wanted to, you know, get your input.
Before responding.
**Rajkumar Rangaraj** 06:25 Yeah, I have the same opinion, Alan. Like, there are so many… today, I also thought I'll bring up another topic. There are so many changes being proposed to this, getting proposed. I know AI is making it simpler, but I also need to, we also need to have a… Very strict triaging here. If… what is the customer need for that?
RO.
Yeah, and also, if AI creates a… we use AI to create a PR, and I would also recommend, if I'm reviewing the same PR with two, three AI models, I'm planning to update the contribution contributing.md with those information. Because when I just take a look at the PR that has been in there, and give it to the, Copilot CLA and ask it to use 3-4 models to review it, every model comes up with some… random issues being spotted in that. So you just wanted, like, write up a process saying that. And this also falls under this… under that category. Solving this is not going to benefit or do any improvement to what we have it now.
Just to say, because people have been using this for a longer time, and just saying… I understand it's PICC compliant, and we need to be there, but… but it's a complex topic at this point, especially touching the runtime context.
the stuff here.
**Alan West** 08:00 Yep, okay, I agree. I can comment briefly and just say… tell Steve that We're gonna pass on this for now.
Unless… Unless there is actually, like, a customer need that arises, and then we can come back to it at that point.
**Rajkumar Rangaraj** 08:18 Yes.
Yeah, I was much worried about a lot of Prometheus work happening here. I don't know who's… where is the customer ask for that.
Because Prometheus, I… I don't know whether there is still a big demand for the, the… this pull model of the Prometheus, and who… where is the ask coming from? There are a lot of peers, and I approved, like, a lot of them early in the past week also.
But still wondering, like, without a customer ask, should we, like.
Spend our effort in this space, or not.
So, just want to, as a… I think, as a maintenance, we need to get all the maintenance in one of the meetings, and lay out a process so that we maintain the quality of the repo, and also honor everyone's bandwidth over that we had to spend here.
**Alan West** 09:25 Yeah, I've not been very much involved with the Prometheus stuff, really, ever.
**Rajkumar Rangaraj** 09:29 But my impression…
**Alan West** 09:31 My impression of this work, though, was that it's really less about a customer ask and more about the fact that I think at the spec level, they're getting very serious about stabilizing the Prometheus spec, and so… I think if that's… if that's the work that's going on at the spec level, then… I don't think we need a customer ask if…
**Rajkumar Rangaraj** 09:57 Yeah, that makes sense.
**Alan West** 09:58 If what the effort is to basically, like.
Match our implementation to the spec and move this towards stability, I think is the, I think is the goal from Martin.
Here, because I think… I think it's people from Grafana that are… that are moving the spec forward, and then he's basically just… doing the .NET.
Part of that.
as he said in a previous meeting, you know, it's… as with all spec work, it's like, the spec can't go stable until prototypes have effectively been, made for all these things, and so it's like this chicken and the egg type of thing, right? You have to… you have to have… Implementations that are ready to go stable in order for people to be comfortable with marking the specs stable.
**Rajkumar Rangaraj** 10:52 I agree with that.
**Alan West** 10:54 Yeah.
**Rajkumar Rangaraj** 10:55 Yeah, even my…
**Alan West** 10:57 That's the context that Martin shared, like, in the last few weeks about this.
**Rajkumar Rangaraj** 11:01 Okay, I think I missed that, because, even I'm very less engaged in this Prometheus part, so don't have much clue, but a lot of things started piling up, so I'm not also keeping up in the spec for the Prometheus, so I think that's how I missed this part.
Yeah, I'll take a look at it. I just unblocked last week, last few weeks, I've been… at least minimum 9 to 10 pairs, I would have unblocked. Let me go and take a look at it, if it's for the spec. I'll continue to review there.
**Alan West** 11:34 Cool.
**Rajkumar Rangaraj** 11:37 I think no new issues or anything, customers, do we have, Any other topic for discussion?
**Alan West** 11:54 Not for my end.
**Rajkumar Rangaraj** 11:57 Cool, I think in that case, I think we could end early. Thanks, everyone.
**Alan West** 12:01 Okay, thanks, everybody.
