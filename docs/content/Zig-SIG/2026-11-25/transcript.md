SIG: Zig SIG
Date: 2026-11-25
Duration: 45 minutes
============================================================

## Zoom Recording Transcript

**Francesco Gualazzi (OpenTelemetry)** 01:48 Hello?
And…
**Antoine Gagniere** 01:53 Hello?
**Francesco Gualazzi (OpenTelemetry)** 01:55 Apologies for the delay, I was, Caught up into something and, didn't know.
**Antoine Gagniere** 02:00 program.
**Francesco Gualazzi (OpenTelemetry)** 02:02 How are you?
**Antoine Gagniere** 02:02 Nope.
**Francesco Gualazzi (OpenTelemetry)** 02:03 Hi, Giovanni, hi.
**Giovanni** 02:04 Yay! Hi, guys.
**Francesco Gualazzi (OpenTelemetry)** 02:06 Got the full room today.
Last week, Yash joined the meeting. You know the metrics contributor that we have?
**Giovanni** 02:14 Yeah, yeah, it's, I mean, yeah, it's like, you know, I know Yashin, so… I swear.
**Francesco Gualazzi (OpenTelemetry)** 02:19 You know what I mean.
**Giovanni** 02:20 But, yeah. No, I mean, I saw some PRs from him, so…
**Francesco Gualazzi (OpenTelemetry)** 02:24 Okay.
I thought that you were working together, maybe.
Beautiful. Yeah, so how are you doing? Are you also, like, impacted by the Thanksgiving holidays of our American and U.S. friends?
**Giovanni** 02:40 Well, honestly, I don't know about you, but, I mean, yes, so I'm in a PTO, and I have so many.
**Francesco Gualazzi (OpenTelemetry)** 02:49 deal.
**Giovanni** 02:49 that I'm in PTO from today to next year.
I have a one. Yeah. Excuse me. Yeah. I have a…
**Francesco Gualazzi (OpenTelemetry)** 03:00 What?
**Giovanni** 03:01 45 days of PTO to consume, so I'll go back to work, I think, like, in the middle of January, so…
**Francesco Gualazzi (OpenTelemetry)** 03:14 I mean, okay.
**Giovanni** 03:15 Indeed, indeed, indeed, I mean, I think that this month I will work a lot on OpenTelemetry. No, I mean, it was…
**Francesco Gualazzi (OpenTelemetry)** 03:21 I agree.
**Giovanni** 03:22 Exactly, so, because I have some time, so between, you know, my, my daughter and, you know, the, the, Thanksgiving, I mean, the Christmas and, you know, other stuff in this period, you know.
**Francesco Gualazzi (OpenTelemetry)** 03:38 My PR is waiting your approval.
**Giovanni** 03:41 Absolutely, so don't worry, so…
**Francesco Gualazzi (OpenTelemetry)** 03:43 The x.
**Giovanni** 03:44 I expect that I will be more active in these days, so…
**Francesco Gualazzi (OpenTelemetry)** 03:48 Oh, okay, okay, okay. There's a bunch of bugs. Also, the one that you already looked into, the 162 conformance.
It would be very nice to progress, not on the tasks, not on the tasks themselves, but rather on the… and understanding what needs to be done, also creating the issues and all.
**Giovanni** 04:07 Yeah, I really, I mean, I prefer to do this kind of stuff, because, I mean, improve my knowledge on OpenTelemetry, because, I mean, as I'm not an expert like Antoine and you, I would like to improve my knowledge on the API and the specifications, so it's… I'm glad to work on this kind of stuff, so… and obviously follow your suggestions, so…
**Francesco Gualazzi (OpenTelemetry)** 04:30 Beautiful, beautiful, thank you, Giovanni.
Thanks for volunteering. Anyways… Yeah, yeah. Yeah, other than that, not much to shove on my end. Just, you know, that, We've been discussing, the issues with the ASHA, the…
**Giovanni** 04:50 Hmm.
**Francesco Gualazzi (OpenTelemetry)** 04:51 I created a big one.
Where is that? Yeah, independent aggregation for multiple metric readers. You know there's been, a series of PRs from Yash, and the last that he did, I was not very happy with that, because it was tangling even more the metrics API with the SDK.
So I created this one, and I added to the AlphaReez milestone 190.
And this one is basically missing features in the metrics that we have, rather bug.
And, it's due to… What is that?
And the issue's open.
Here. You should be seeing my screen very…
**Antoine Gagniere** 05:38 Yes, receipt. Yes, from…
**Giovanni** 05:40 masadias.
**Francesco Gualazzi (OpenTelemetry)** 05:41 So, let me Zoom a minute on this one.
My issue that I created was this one, and in order to make it happen, I, you know, broke down… the… the steps, no? And… and the PR that is blocked currently, one for approval, is, is this one.
So he created one, I created a follow-up, but before proceeding, we need to merge this one, which is waiting for your review, and then we go and create probably another couple of PRs.
**Giovanni** 06:17 Okay.
**Francesco Gualazzi (OpenTelemetry)** 06:17 To say, this thing is at… let's say, bug, because right now, every time we attach multiple readers, which is not very common, but could happen, so if you have multiple readers attached to the same meter provider.
**Giovanni** 06:33 Essential.
**Francesco Gualazzi (OpenTelemetry)** 06:33 this could happen… let's imagine that you… I don't know.
you want to aggregate things differently, you know? You have one reader with some views, like, maybe cumulative for the… for the Instagram, or, like… Delta for counters, and then you have another reader for the same metrics, but with another type of aggregation, I don't know, last value.
Now, these two… As of today, they gobble each other's data.
Because the output that we do out of the aggregation is not properly shared. So, it is… it should be… fanning out, but instead it's chain, right? So that's the problem.
And I'm fixing that with the Ash, and we have a clear path ahead, but we need your help in… In the review of this one. Which is not cool.
profiles are on hold, and I haven't seen much new issues, apart from this one.
Antoine which you should decide if they need to be in for the alpha release milestone or not.
**Antoine Gagniere** 07:51 Yeah, I opened a bunch of issues, because I'm using the SDK in some I've… And so I noticed, some… yeah, so for example, the 195 is just, an inconsistency of the API, but it's not… so I don't think it can be postponed, it's…
**Francesco Gualazzi (OpenTelemetry)** 08:19 If it's a bug, it's a bug.
**Antoine Gagniere** 08:20 I mean, it's not a bug, it's just…
**Giovanni** 08:23 Consistency on, yeah.
**Antoine Gagniere** 08:25 But it would be a breaking change of the API, right? So we… we won't… To change it before being stable, but it doesn't… we can do it after alpha.
**Francesco Gualazzi (OpenTelemetry)** 08:39 I mean, Alpha is still, very subject to change. Even Beta is subject to breaking changes.
**Antoine Gagniere** 08:46 sued.
**Giovanni** 08:46 Yeah.
**Antoine Gagniere** 08:47 urgent.
**Francesco Gualazzi (OpenTelemetry)** 08:48 No, but it's okay, let's put it there. I mean, I think we have, we don't have a deadline, right? The ideal target would be start of next year, which could be January, it could be February, I don't know.
**Giovanni** 09:00 Well, as I said in other contexts, we have a deadline when we have a customer.
**Francesco Gualazzi (OpenTelemetry)** 09:06 Exactly.
**Giovanni** 09:07 base hours.
**Francesco Gualazzi (OpenTelemetry)** 09:08 Wait, wait…
**Giovanni** 09:09 whatsoever.
**Francesco Gualazzi (OpenTelemetry)** 09:09 Now that Giovanni… now that Giovanni is out in PTO, I mean, we… we should say that, I don't know.
Otherwise, it's gonna slack,
**Giovanni** 09:19 Everyone's a guy.
**Francesco Gualazzi (OpenTelemetry)** 09:21 Oh.
**Giovanni** 09:22 Oh, yes.
**Francesco Gualazzi (OpenTelemetry)** 09:23 is, yeah, feel free… I mean, I assigned this one to Alpha release, and if you want to work on that.
Because, again, gRPC is pretty stable, and thank you, Antoine, for, following up so extensively on that topic, I had a chance to… use the gRPC backend in an application in production at my work. It's my first Zig production service at work.
And it is exporting via gRPC. I haven't tried compression, but I will. It is exporting via gRPC to an OpenTelemetry-compatible backend, and everything works seamlessly. So I'm very, very happy about that.
Yeah.
**Antoine Gagniere** 10:07 Very good.
**Francesco Gualazzi (OpenTelemetry)** 10:08 Awesome.
So yeah, feel free to work on this if you have time and energies to do that, and Honestly, if I go back to the alpha release, I don't see something super priority other than fixing the metrics bug.
And the conformance, yeah, but this is unusual, Andy. I count on you for that.
Documentation is gonna be the last thing, because, again, before creating the PR to the OpenTelemetry repo, we need to have something working.
And then… Yeah, this is… this is in progress.
Oh yeah, this is just configuration, so I don't think it's gonna take… Oft, but… It needs to be done.
I can handle this.
Actually, I probably assigned it to myself, yeah. I meant to develop it, but I haven't found… Time?
And… not sure if this is… needed for the Alfa Liz, honestly, Antoine.
Maybe… maybe yes?
This is the improvement of the SEMCOM to support any value.
**Antoine Gagniere** 11:24 Right, it was part of the… the 126.
I think?
**Francesco Gualazzi (OpenTelemetry)** 11:30 I don't think this is…
**Antoine Gagniere** 11:31 Is it the case, or…
**Francesco Gualazzi (OpenTelemetry)** 11:33 Oh, yeah, yeah, you mean it's gonna be a subissue of this one?
Yeah, okay.
**Antoine Gagniere** 11:38 And it leads to some issue, right?
**Francesco Gualazzi (OpenTelemetry)** 11:41 So this also falls into Giovanni's end.
This was actually great work, Giovanni. When I saw the table and everything, I really enjoyed it.
**Giovanni** 11:52 Well, you know, a great part was by, I mean, you know, but in any case, I, I mean, I changed it a bit. Some, some stuff was super, super strange.
Fair enough.
**Francesco Gualazzi (OpenTelemetry)** 12:06 Les, this is very good.
Hmm, okay.
**Giovanni** 12:11 But, I mean, I saw the comments from Antoine, so there are some missing issues related to that, so I can open the other.
**Francesco Gualazzi (OpenTelemetry)** 12:21 The conformance?
**Giovanni** 12:23 Okay.
**Francesco Gualazzi (OpenTelemetry)** 12:24 Yeah? Yeah, ideally, ideally, all of the stable ones.
**Giovanni** 12:28 Yeah.
**Francesco Gualazzi (OpenTelemetry)** 12:30 At least once a issue.
**Giovanni** 12:31 Okay.
**Francesco Gualazzi (OpenTelemetry)** 12:32 So then we can… we know how to track, you know, the things.
The development, if you all agree, I would not bother too much.
**Giovanni** 12:42 No.
**Francesco Gualazzi (OpenTelemetry)** 12:43 Maybe we can do, after the Alfari's, full.
Pass of, you know, deciding which development features should get in, one by one.
I… Let me know what you think.
**Giovanni** 13:00 No, I mean, honestly, from my side, I postpone, so honestly, it's okay to have only the stable for the alpha, so… It's good enough.
**Francesco Gualazzi (OpenTelemetry)** 13:10 By the way, by the time that we make all the stapling, the spec is probably going to be bumped.
**Giovanni** 13:16 Yeah, probably, yes. In any case, we'll be, I mean, we have, I mean, we can be online at 2 to 1, so 62, so… it's… in any case, it's an achievement, honestly, guys, so…
**Francesco Gualazzi (OpenTelemetry)** 13:32 Yeah.
If I remember correctly, One of this was fixed.
Yeah, this one. I think this one is done.
I recently worked on it.
**Giovanni** 13:47 Yeah, I said, I wrote a comment related to, open the final conversation, yes.
**Francesco Gualazzi (OpenTelemetry)** 13:51 No, no, this is definitely done. I fixed it last week.
Let me, let me actually, point to the PR point.
Number 7… was fixed in…
**Giovanni** 14:10 111, if I don'.
**Francesco Gualazzi (OpenTelemetry)** 14:12 Oh my god.
**Giovanni** 14:13 Yeah, if I recall correctly, it should be 1-1-1.
**Francesco Gualazzi (OpenTelemetry)** 14:20 Yeah.
But this is the issue, right?
**Giovanni** 14:26 Yes.
**Francesco Gualazzi (OpenTelemetry)** 14:27 Okay, well, whatever.
Then the issue links that we have.
Hmm. Okay.
Oh, what.
**Giovanni** 14:34 Yeah, GitHub… GitHub in this period of this life.
**Francesco Gualazzi (OpenTelemetry)** 14:36 Like, you know.
**Giovanni** 14:37 is in a PTO.
**Francesco Gualazzi (OpenTelemetry)** 14:38 It's also naughty,
**Giovanni** 14:40 Yeah, yeah.
**Francesco Gualazzi (OpenTelemetry)** 14:47 I mean, do you even remember what… what… what coding was like before GitHub. I do remember what it was like.
**Giovanni** 14:57 I don't know Antoine… for Antoine, and for you, I remember Susforge, if you remember SusseForge.
**Francesco Gualazzi (OpenTelemetry)** 15:03 Source for, of course.
**Giovanni** 15:04 Yeah.
With SVN, so…
**Francesco Gualazzi (OpenTelemetry)** 15:08 I remember to… beat bucket.
**Giovanni** 15:10 Meetings.
It's already, it's already… I mean, both of them are either, still there.
I mean, present, but…
**Francesco Gualazzi (OpenTelemetry)** 15:20 Okay.
Beautiful.
**Giovanni** 15:26 Cool.
**Francesco Gualazzi (OpenTelemetry)** 15:27 That was all I had.
**Giovanni** 15:30 Okay, so… Let me, okay, so…
**Francesco Gualazzi (OpenTelemetry)** 15:43 You want to discuss anything, I think?
**Giovanni** 15:44 No, no, I'm only comment, an issue, so… so the one related to the, meter provider, local providers, 195.
**Francesco Gualazzi (OpenTelemetry)** 15:58 Happy with everything, Antoine?
**Antoine Gagniere** 16:01 I was reading the issues to see which should be included in the release.
Yeah, yeah, okay, I think I'm adding all of them.
**Francesco Gualazzi (OpenTelemetry)** 16:20 No, it makes sense. Again… Don't… don't be… don't be afraid of… Increasing the scope of the alpha.
if what we put in the milestone is needed for a working solution, right? So, a working SDK.
Because.
**Antoine Gagniere** 16:38 Right, right.
**Francesco Gualazzi (OpenTelemetry)** 16:39 Even if it's not perfect, it has to be working, right?
It doesn't have to support the development features, okay, but it cannot be completely broken.
**Antoine Gagniere** 16:53 Okay.
Because maybe we want to release it early, and then to have multiple alpha releases, right?
**Francesco Gualazzi (OpenTelemetry)** 17:01 Yeah, my point is… If we start saying that this thing exists, and it's ready for usage, even if we say it's an alpha, you know, the bar, the quality, the bar… the level, the bar of the quality, the quality bar…
**Giovanni** 17:20 The level of, you know, the…
**Francesco Gualazzi (OpenTelemetry)** 17:22 Nothing. The level of quality expected in the Zig community in general is usually higher, right, than the average programming language community. So.
If we say, this is a targeted release, try it out, bring it in your application, and then, you know, we find the memory leaks, which we had.
Something is not working as expected, like, the metrics are… Yes, of course we expect some bugs, but the one way we know we have, we try to fix them, no?
**Giovanni** 17:57 Yikes.
Oh.
In my opinion, honestly, for an alpha, it's okay if we target a version, a specification, a specification, and we try to be compliant as much as possible. This is… obviously, the quality is important in the project, but I think that it's important also that we define a set of, you know, a version that we want to support and say, okay.
From this, I mean, at least we are… from our understanding, we do support this level of API, so… And by the way, if we.
**Francesco Gualazzi (OpenTelemetry)** 18:39 Make the alpha good enough.
Then, moving to the beta, And it's gonna be simpler, you know?
And let's not forget, when we do the alpha, we also release, all together all the other modules, so SAMconv, the Proto.
Which, by the way, for the proto, sorry for the off-topic here, I… I recently used our proto to build a frame graph visualization in in WebAssembly, with Zig, And… guys… it was very good. Like, it was… easy to do. Not that the Proto is good, because the proto for profiling is especially Tangled, let me be politically correct.
But, But, yeah, the fact that we have the module with the proto and all the types already defined, it's awesome.
Because it lets you work.
with the data types directly, and then you can do whatever you want. You can adapt them, you can merge them, you can put in multi-array list.
It's… Bonka.
Very good. Sorry for the off-topic here. So yeah, I'm… I'm positive. I'm very happy.
Also, Christmas is coming.
Or Hanukkah, if you celebrate that.
Put it as you want, but, you know, snow, eating, that's always good.
Alright.
We good?
**Giovanni** 20:17 From my side, yes.
**Francesco Gualazzi (OpenTelemetry)** 20:19 Love you guys.
See you next time!
**Giovanni** 20:22 Bye. Bye, bye, Francesco, Banco.
