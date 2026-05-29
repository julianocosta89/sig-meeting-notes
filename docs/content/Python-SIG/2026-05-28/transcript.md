SIG: Python SIG
Date: 2026-05-28
Duration: 27 minutes
============================================================

## Zoom Recording Transcript

**Riccardo Magliocchetti** 01:02 Hello?
**Keith Decker** 01:09 Good morning.
Afternoon.
Good evening.
**Leighton Chen** 01:28 Hey, everyone.
**Diego Hurtado Pimentel** 01:36 Hello, buddy.
**Leighton Chen** 01:59 Cool, so, I think I can share today, since, Ricardo's on… On his phone right now.
Yeah, we'll just give it a minute for people to kind of start playing. Yeah, as usual, please add your names to the attendees list, as well as any kind of topics or PRs you want to bring up.
This is the place to do so, especially if you want attentions on your PRs.
I think Aaron is out today, so we'll just get started.
About a minute or so.
Also, curious, Tammy, are you still leading the, kind of, triages, or did you want me to do it?
**Tammy Baylis** 04:03 Hey, Leighton, sorry, I've been kind of away for a bit, and I actually haven't looked at any PRs. If you could please just do the 5-minute triage today, that'd be wonderful, thank you.
**Leighton Chen** 04:15 Yeah, sounds good.
Also, do people hear any, like, feedback from my mic or anything?
Everybody's fine.
**Tammy Baylis** 04:28 It's fine on my end.
**Leighton Chen** 04:31 Okay, cool.
Alright, we can just get started. I'm going to timebox the… Triage to 5-10 minutes.
Let's see… I think this one is just the Docs PR.
From 3 weeks ago.
But we just need reviews on this.
Does anyone have any context on this, and why this PR is closed? Or this, it… This issue's closed?
Okay, well… I see. Probably a multi-PR… Okay, well, we'll just put this into… Country for review.
Okay, alright, we have, PR here to refactor some Docker tests.
I believe this touches some stuff in test utils as well.
Looks like… Looks like Ricardo left some comments, but it does seem to be the case in which we need some more eyes on this, so… I will also move that to… There you go.
Oh, yeah, this, just probably don't even gotta look at it.
Cool, fix AWS Lambda support ALV multi-value headers.
Yeah, I don't have that much context on AWS Lambda, Yeah, if anyone else does… feel free to speak out, but this does look like it is continuing an OPR that that was closed, so we probably just need… Line's on this as well.
Yep.
Okay.
And I think we have a… All the typing… Pure… yeah, okay.
Pretty straightforward, probably.
Is there a… Difference between easy-to-review merge… I forgot we had definitions for these, but Is there, like, a manual intervention for, like, telling if a PR is actually easy? Or is there, like, some kind of indicator where it's, like, it's… if it's already approved or something?
**Riccardo Magliocchetti** 07:42 No.
**Leighton Chen** 07:43 Anybody help me?
**Riccardo Magliocchetti** 07:43 annually.
**Leighton Chen** 07:45 Oh, this is just manual? Okay.
**Riccardo Magliocchetti** 07:47 Yeah, like… I like to think as this review, columns as, like, really trivial stuff, like typos, or, like, maybe the Python As well, yeah.
**Leighton Chen** 08:01 Okay, yeah, I'll probably put typing stuff related to… And, like, dogs, probably.
Is that kind of, like, the… the criteria, Ricardo, they usually use, or…
**Riccardo Magliocchetti** 08:15 Yeah, like… I don't know the detail of the documentation one, but…
**Leighton Chen** 08:23 Okay, yeah, I can take a look at it after the… So… Got a little bit 2 more minutes for this, probably, and we can just move right along.
Oh, this does look like, so it is generally related, but it is in the BodoCore instrumentation.
So this one's still in the contribute repo.
Looks like… Ricardo, you already left some comments on that, so…
**Riccardo Magliocchetti** 08:55 Yeah, I haven't looked at the responses, but I'll take a look.
Next week. Okay.
**Leighton Chen** 09:02 I'll move this into, What is this?
**Riccardo Magliocchetti** 09:12 I think it's ready for review, like, for someone from Genai people.
**Leighton Chen** 09:20 Cool. And then probably… Last one of gRPC instrumentation.
Add support for metrics.
Okay.
Yeah, makes sense, probably just need… To take a look at this, so… It does look like a media was tagged, so that's pretty… pretty interesting.
**Riccardo Magliocchetti** 09:48 Yeah, also, like, I think we discussed about metrics for GRPC some months ago.
I think there was a discussion with Judemila about the semantic convention, and also, like, gRPC export environment metrics, or something like that.
**Leighton Chen** 10:06 Yeah.
**Riccardo Magliocchetti** 10:07 My funeral.
**Leighton Chen** 10:12 Was it, like, was there, like, any point of contention or anything?
**Riccardo Magliocchetti** 10:16 I think that were discussion, On defining a semantic convention for this stuff.
**Leighton Chen** 10:23 Right.
**Riccardo Magliocchetti** 10:24 and also, like, gRPC people Wanting to contribute on the discussion?
**Leighton Chen** 10:31 Okay.
You mean, semantic conventions that are in addition to the already… metrics that exist, like the RPC.
**Riccardo Magliocchetti** 10:41 Yeah, I think so.
But, like, maybe we should… maybe, I think, Ludimila's… I have more… details, so maybe we should just mention the… her in the… in the PR, maybe, yeah.
**Leighton Chen** 10:57 That's good.
I'll, add a comment after the meeting.
Okay, cool. Yeah, then, let's… let's just move on.
Cool, so, I think we are trying to continue the… what I'm working on this week, kind of… process… That Ricardo proposed a while ago, though it would definitely help at least the maintainers to kind of get a sense of, like, where the direction and what people are prioritizing. So, yeah, please fill this in if you are planning to work on something this week.
But we can get started. First topic is from Tammy.
Did you want to talk about how to proceed with opt-in experimental feature?
**Tammy Baylis** 12:00 Yeah, we already talked about this, I think, 2 weeks ago at the last SIG, and I think last time we wanted to get… more information about whether this is specific to Gen AI or just in general.
So I posted on the issue and the PR. Adrian here is saying it's not just for LLM, but other cases, and they agree that… There should be better agreement in the future.
I think, but then if we look at the PR, krishna… Is, really enthusiastic about wanting wanting to merge their PR right away as… an NVAR-gated default off feature, so I'm… I'm just wondering if we wanted to have more discussion, or push them more towards spec, or if we're okay with having this… In, the core repo as an opt-in feature right now.
**Leighton Chen** 13:14 Yeah, that's a good question, and thanks so much for following up and driving and continuing the conversations on this.
I think this is, kind of a pattern that the maintainers have noticed so far.
Where, let's see, let's take a look at the… This is the original issue, right, Tammy?
4 or 5?
**Tammy Baylis** 13:39 Yeah, 4533, yes.
**Leighton Chen** 13:42 Okay, yeah, there has been a kind of… A pattern that we've noticed that, like, before an issue has been resolved, There are contributors who are open PRs to attempt to fix, From their con… with a context that they know of the issue.
This usually is okay, especially when issues are kind of… Pretty obvious and direct that, like, They will be helpful.
But in cases like this, when, Kind of conversations are still open.
It is kind of like our protocol, not officially, but process to And beneficial for the SIG to kind of not adhere to just, like.
I guess, pressure from contributors, and Uphold, like, a… a clear process.
So, I don't have a lot of context on discussions of whether or not we decided, this is GenAI-related or not, or what the situation with the spec is.
But, in general, we don't want to kind of push Just because a feature is envar gated or default off, Something through if it's not something that is, generally agreed upon, so… That's my two cents before talking about this PR. Yeah, Ricardo, go ahead.
**Riccardo Magliocchetti** 15:21 Yeah, Leighton, could you please open the specification issue that is linked?
**Leighton Chen** 15:27 Yeah, sure.
Is it up here?
**Riccardo Magliocchetti** 15:32 It was, like.
**Tammy Baylis** 15:33 I also added it to the meeting minutes. Last minute. Yeah, the third link.
**Leighton Chen** 15:39 Oh, thanks.
Oh, yeah, I remember this one.
God… Is there a specific comment you wanted to look at, Ricardo?
**Riccardo Magliocchetti** 15:55 Nope.
Just, like, maybe if there is a resolution here, or… We're still discussing also.
On this side.
**Leighton Chen** 16:07 Yeah.
I guess, Tammy, since, maybe you've taken a look at it more, do you know, kind of, like, the current situation of, like.
What the point of contention is in the spec.
Versus, like, what has been decided, or if it's just at a standstill right now.
**Tammy Baylis** 16:27 I… I believe it's at a standstill. I think, like, the general two sides of the argument are, like, number one, it… shouldn't… how do you say? If the hotel collector doesn't handle 413s, then why should the SDK… it should be… the platform or the backend that should be dealing with this, and, like, not… not the source. But then there's the other argument where, you know, payloads are getting bigger and bigger, we should, make it more clear, you know, we should be able to… to batch, or whatever, that, like, metrics can be batched on retry, for example, but… Yeah, it's… in my mind, TLDR, it's a standstill, and to me, there's no clear direction for where this is going, so, In my position, I'm not sure what to do.
**Leighton Chen** 17:28 No, no, no, makes sense.
I don't think it… Requires of a single person, to make a decision for, but… I think… kind of adhering to what Ricardo's saying, I think, Pointing back to the spec before… Pushing any changes, even if it is experimental, is usually the protocol that we go with, so… It's just the nature of it.
Might have to just, wait until… Whatever open, kind of, conflicting… Topics?
Have been resolved first.
I can make a comment on that PR, too, if you want me to handle the messaging, so…
**Tammy Baylis** 18:16 Yeah, yes please, if you with maintainer status could do that, that'd be very helpful for me. Thank you.
**Leighton Chen** 18:24 Okay.
Sounds good.
Nice. Is Keith here today?
Oh, hecky.
**Keith Decker** 18:38 Just wanted to bring up OpenTelemetry Bootstrap, and with splitting off the new repos, we don't have the… Oh, what is it, the generation stuff in place for that yet? Just want to make sure we don't miss that when we do that first initial release on the new repos.
For auto instrumentation.
**Leighton Chen** 19:06 Right, could you refresh my memory again? So, OpenTele Bootstrap, is the… Helps with the, OpenTelemetry instrument zero code, kind of… pipeline, right?
**Keith Decker** 19:25 Correct. It'll go look at, like, your requirements and your installed PIP packages, and then go reach out and see what those are mapped to for instrumentation.
And then pull those packages.
**Leighton Chen** 19:37 Right, and then your concern is, Since we are… is it related to using new project names or package names?
**Keith Decker** 19:45 New package names is… is, I think, the biggest one, because the generate command is in the old contrib repo, and the main… Python repo, I think?
On how it generates that mapping.
And so I do… yeah, we haven't actually done a release yet out of the new repo, right?
**Leighton Chen** 20:07 Fair enough.
Yeah, that's a good point. Definitely thanks for calling that out. I don't know the… plan yet, of what we want to do that. Hey, sorry, Ricardo, go ahead.
**Riccardo Magliocchetti** 20:22 No, I was just going to say, please open an issue. I think in Contrib, where the bootstrap code is.
To not forget about whispering.
Okay. So, yeah, like, once you have the instrumentation published, we can just update, on the Contrary Bootstrap site as well.
**Keith Decker** 20:44 Okay, yeah, I just wasn't sure if there was an automatic procedure around that, or if it was something I should… flag for… For us to review.
**Leighton Chen** 20:54 Yeah, definitely there's no issue out yet. This is kind of the forum to bring up things that we might miss, like this.
Yeah, please, please create an issue, we could… it's, we could… it's probably more… detailed and, like, some nuanced things that we might miss, might sort of stop there. But… Yeah, I don't see a problem.
With this, as long as we just keep track of it, so…
**Keith Decker** 21:20 Yep, I'll create an issue over there.
**Leighton Chen** 21:24 Thank you.
**Riccardo Magliocchetti** 21:24 Yup.
Because, like, I think we need to update our tooling to look, like, to check out the Python Gen AI instrumentation, and… And look for instrumentation there as well, yeah.
**Leighton Chen** 21:47 Okay, cool, nice.
I think that's… Pretty much all the topics we've had today, as long as That's what I see. Does anybody else have anything they want to talk about, bring up?
Okay, well, we might have a shorter meeting today. It does seem like the… because now that GenAI has been moved to a different SIG and repo, we might probably get Less and less topics related to that. But, you know.
This is just kind of what happens as a… As a result of that.
That's fine. I think we can just, like, keep these discussions scoped to, now, specific Python SIG issues, so it's awesome.
Okay, well, if there's nothing else, thanks everyone for joining, and we'll see you, everyone, next week.
**Tammy Baylis** 22:55 Yeah, thank you.
**Riccardo Magliocchetti** 22:57 Thank you.
**Dylan Russell** 22:57 See you guys.
**Diego Hurtado Pimentel** 22:58 Thank you all. Take care. Bye.
**Keith Decker** 23:00 Dance.
