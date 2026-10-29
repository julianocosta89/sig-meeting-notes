SIG: Zig SIG
Date: 2026-10-28
Duration: 45 minutes
============================================================

## Zoom Recording Transcript

**Antoine Gagniere** 00:12 Hmm.
Nope.
**Francesco Gualazzi (OpenTelemetry)** 00:16 Bon d'ous!
Or should I say, Bonsai already?
**Antoine Gagniere** 00:22 No, I would say bonjour, yeah.
**Francesco Gualazzi (OpenTelemetry)** 00:26 How you doing?
**Antoine Gagniere** 00:27 Great, and you?
**Francesco Gualazzi (OpenTelemetry)** 00:29 Yeah, pretty good.
Lots of fun at work.
**Antoine Gagniere** 00:34 Lots of…
**Francesco Gualazzi (OpenTelemetry)** 00:35 Fun at work.
**Antoine Gagniere** 00:36 bubble.
Oh, nice, very nice.
**Francesco Gualazzi (OpenTelemetry)** 00:39 Type 2 fund, the one that… The one that is not seen as fun from 99% of the people.
**Antoine Gagniere** 00:47 Right, right, yeah, the best kind of fun, yeah.
**Francesco Gualazzi (OpenTelemetry)** 00:50 Yeah, that kind of fun, yes.
**Antoine Gagniere** 00:52 Yeah, yeah.
**Francesco Gualazzi (OpenTelemetry)** 00:52 You know what fun I'm talking about.
**Antoine Gagniere** 00:56 Yeah, yeah, yeah.
Yeah, just saying, I will have to leave at, 15… in 15 minutes.
**Francesco Gualazzi (OpenTelemetry)** 01:03 Nice.
**Antoine Gagniere** 01:04 Yeah.
**Francesco Gualazzi (OpenTelemetry)** 01:05 And what about yourself, Antoine? Are you happy that GRPC landed?
**Antoine Gagniere** 01:10 Yes, yeah, I was going to mention. Very, very good, very…
**Francesco Gualazzi (OpenTelemetry)** 01:14 It's been… At least 2 months that we've been working on it, no?
**Antoine Gagniere** 01:19 More.
**Francesco Gualazzi (OpenTelemetry)** 01:20 More than that, yeah.
**Antoine Gagniere** 01:22 I started working on the, like, the first package, like, just… it was, like, during Christmas.
**Francesco Gualazzi (OpenTelemetry)** 01:30 us?
**Antoine Gagniere** 01:30 Christmas, holiday, so one year ago.
Just to build… build gRPC, build the liberal.
**Francesco Gualazzi (OpenTelemetry)** 01:38 Oh yeah, oh yeah, oh yeah.
**Antoine Gagniere** 01:39 And then, it was in March, then I worked on the…
**Francesco Gualazzi (OpenTelemetry)** 01:43 Yeah, in the…
**Antoine Gagniere** 01:43 The wrapper and the first version, where I was able to… Sin…
**Francesco Gualazzi (OpenTelemetry)** 01:48 Basically, this is a baby.
**Antoine Gagniere** 01:50 Yeah, that's a baby.
So, yeah, yeah, pretty happy with, finally, getting to work, getting it merged.
And, yeah, we still have… not blue, but it's,
**Francesco Gualazzi (OpenTelemetry)** 02:05 I saw you created a… An issue for the compression.
I… was expecting that.
**Antoine Gagniere** 02:12 Yeah, yeah, I actually had mentioned it in a comment in the previous repo, previous org, like, in my first gRPC pull request, I said, I'm leaving out compression, it's as a to-do.
But yeah, so I think it's not that much work, but I'll see.
So yeah, it was compression, what else was missing? Let me pull out my notes if you want.
**Francesco Gualazzi (OpenTelemetry)** 02:40 We still have that, that improvement to do… on both.
the server, and your PC.
That we want to keep a pool of, right.
**Antoine Gagniere** 02:54 school.
**Francesco Gualazzi (OpenTelemetry)** 02:55 Right?
**Antoine Gagniere** 02:55 Yeah, so both… for both HTTP and gRPC, we have to reuse some object that can keep state or whatever.
And second one is, retries, maybe move the existing retry logic that is inside the HTTP and move out to…
**Francesco Gualazzi (OpenTelemetry)** 03:13 Should we… should we write this down? Because otherwise we forget.
**Antoine Gagniere** 03:16 Yeah, yeah, I can't you if you want.
**Francesco Gualazzi (OpenTelemetry)** 03:19 I… I… I can… I mean, you can do that, I can do that. I mean, the important part is that, that we track it. Maybe I've write it… I write something, and you can edit it?
**Antoine Gagniere** 03:32 Oh, yeah, yeah, we… yeah, you can add it in the Meetings note.
**Francesco Gualazzi (OpenTelemetry)** 03:36 Yeah, give me a second, I will create it real quick, and then we… then you can expand.
**Antoine Gagniere** 03:41 Yeah, yeah.
**Francesco Gualazzi (OpenTelemetry)** 03:41 SDK OTLP, ensure we keep… Do not regenerate.
Flying instructors on every aspect.
Right?
**Antoine Gagniere** 03:58 Right, exactly.
**Francesco Gualazzi (OpenTelemetry)** 04:01 I'll never be export.
I'll be real quick, I promise.
By the way, what do you think of adding issue templates and PR templates to the repo? We don't have anything right now.
**Antoine Gagniere** 04:15 Yeah, yeah, it's, it's good, Yeah, I see… we see more new contributors.
**Francesco Gualazzi (OpenTelemetry)** 04:23 AM.
**Antoine Gagniere** 04:24 I think it's the right time to… To provide templates here.
**Francesco Gualazzi (OpenTelemetry)** 04:32 patient.
Every time we call export, we… re… Create the client.
use this FMR.
instance… Oop.
Publish.
The bait.
Right.
There's not a state.
We have a… allocated. We have a… Strap.
That is… painted once.
is very useful.
else.
export cycles.
This is, this is simple enough.
And we can expand, you know?
Good to be.
Oh, that's bad.
So this is… we'll be… we will be at 137.
Let me share with you here the link, here chat.
This is the one.
It's very, very rare right now. Feel free to edit, add considerations, put comments, whatever you want.
And…
**Antoine Gagniere** 05:51 Yep.
Hey.
**Francesco Gualazzi (OpenTelemetry)** 05:55 Other than that, I just merged 3 tiny PRs from Yashi.
Those are, fixes to the trace, State propagation and, link, ownership.
Very good. Nice contributions. One test added, few lines of code changed, super easy to review. I love them.
And then we have opened the support for example, yeah, this came in last week, 3 days ago. I was so happy to see it. Just out of the blue, this guy comes in and say, he's a PR. It's… it's quite a big one.
I just started a… A.
Copilot review.
Yeah. And, now there is a conflict after merging the improvements to the observable… Instrument API, which was another API from Yashi.
And, yeah, so there is some… there is some feedback here.
I will get back to the contributor, which is a new contributor, first-time contributor, Uzaifa Abdul Rahman.
Thanks.
Zaifa, if you're listening to this, for putting this out, it's… it's very helpful, because Exemplars was one of the… is one of the items that we want to have done of the Alpha reads, if I'm not mistaken.
**Antoine Gagniere** 07:28 Oh, okay, yeah.
**Francesco Gualazzi (OpenTelemetry)** 07:29 No. Oh, yes.
**Antoine Gagniere** 07:30 We should, let me check. Let me check.
**Francesco Gualazzi (OpenTelemetry)** 07:33 Yeah, yeah, yeah, it is, it is,
**Antoine Gagniere** 07:35 It's…
**Francesco Gualazzi (OpenTelemetry)** 07:36 out of the…
**Antoine Gagniere** 07:38 Oh, yeah, yeah, and even… yeah, what's good is… even asked us in the issue before opening the PR, so it's…
**Francesco Gualazzi (OpenTelemetry)** 07:47 Yeah, yeah, yeah, you know, he was super.
**Antoine Gagniere** 07:49 Just a random book.
**Francesco Gualazzi (OpenTelemetry)** 07:50 He commented on the issue on July 23rd, and I completely missed the notification, but now, you know, one week ago, I replied, and he got back to it, and the PR is out there, yeah, I started the Copilot review, some things have been written by Copilot. I skimmed through it, and it seemed reasonable in terms of, you know, design, so there is this new example abstract that gets handed over when needed, even in the processors, which totally Good implementation at first glance.
Let's progress with that. I am assigned to that, because I want to review it, because it's part of the metrics, mostly.
And… what else? Oh yeah, I have another open PR for me on the metrics that is, fixed on the observable counters.
And the co-pilot review here is giving me… giving me some hints. I need… oh yeah, the overflow.
Okay, that makes sense.
**Antoine Gagniere** 08:52 Wait, which one?
**Francesco Gualazzi (OpenTelemetry)** 08:53 This is, 122.
This one is opened by me, like, 10 days ago, last week, I don't remember.
**Antoine Gagniere** 09:01 Oh, yeah, yeah, yeah, yeah, I see.
**Francesco Gualazzi (OpenTelemetry)** 09:04 I need to… I need to get back on this. Jumani requested the… review from Copilot, and I mean, these reviews from Copilot are being helpful.
I didn't expect that, because the last time I had used co-pilot was total nonsense, but now it looks… now it looks reasonable, right?
**Antoine Gagniere** 09:22 Yeah, yeah, it's useful, yeah.
**Francesco Gualazzi (OpenTelemetry)** 09:24 even for a language that is not, like, mainstream, like Zig.
They start to be pretty meaningful, reviews, which is helpful, okay?
So, thank you, OpenTelemetry, for paying for the pilot review.
**Antoine Gagniere** 09:39 Yep.
**Francesco Gualazzi (OpenTelemetry)** 09:41 Yeah, that's that. I'm pretty hyped for the state of the project, you know, contributions are coming in, we are making constant progress towards the Alpha release. What I haven't started is asking to Alolita and Joshua how we are going… how are we supposed to… to do the actual process of releasing, so do we need to create an entry in the documentation, in the official documentation page? Do we need to create, I don't know.
Some announcements, do we need to have a specific naming, you know, all that kind of stuff.
And also, because of the structure of our monorepo, when we release the SDK, we also release the SEMCOM and the proto, so I guess that's not an issue, but I would like to confirm.
With someone more expert than me in such a matter.
Yeah, that's it.
Do you have anything?
Hello? You muted?
I guess you're muted, Antoine.
**Antoine Gagniere** 10:58 Sorry. Yeah, I had one last thing written down, was the OTLP partial success. I should… I don't really know a lot about it, so I need to…
**Francesco Gualazzi (OpenTelemetry)** 11:11 Partial success.
**Antoine Gagniere** 11:13 Yeah, apparently it's possible for… An export to only partially succeed.
And, yeah, there's a to-do in the HTTP code.
**Francesco Gualazzi (OpenTelemetry)** 11:26 Okay.
**Antoine Gagniere** 11:27 And in gRPC, it's the same, it's not done either, so…
**Francesco Gualazzi (OpenTelemetry)** 11:30 Okay…
**Antoine Gagniere** 11:31 the… yeah, it's a to-do we have, so…
**Francesco Gualazzi (OpenTelemetry)** 11:36 So, can you… enlighten me a bit, because I don't remember exactly what that means. So, it means… I send you a payload, you can only process half of that.
and you reply… I mean, you reply to me.
that the second half, for example, is not ingested, so the client should be resending it, or what?
**Antoine Gagniere** 11:59 Yeah, so it's in the spec, I sent you the link, so it's… Okay.
**Francesco Gualazzi (OpenTelemetry)** 12:05 Okay.
**Antoine Gagniere** 12:06 Oh, but it's only… for GRP? Okay, but… Partial success. Full success, partial success, and failure, okay.
**Francesco Gualazzi (OpenTelemetry)** 12:13 Wait, wait, if the request is only partially accepted, when the server accepts only partially without having injects the rest.
The server… this is on the server side.
**Antoine Gagniere** 12:22 Right, but so, it means the server can… reply.
**Francesco Gualazzi (OpenTelemetry)** 12:27 Okay…
**Antoine Gagniere** 12:28 to the client.
**Francesco Gualazzi (OpenTelemetry)** 12:30 Okay.
**Antoine Gagniere** 12:30 Apart from success, right?
**Francesco Gualazzi (OpenTelemetry)** 12:32 Okay, but I don't see anything… the client must not retry the request, he says.
When it receives a partial success response, where the partial success is populated.
**Antoine Gagniere** 12:42 Oh, yeah, yeah, let me read…
**Francesco Gualazzi (OpenTelemetry)** 12:47 We should populate error message. Maybe we can just bubble up the arrow.
But we already knew that. Oh.
**Antoine Gagniere** 12:56 Right.
**Francesco Gualazzi (OpenTelemetry)** 12:57 Mmm.
**Antoine Gagniere** 12:58 If it's a failure, but we must not retry?
**Francesco Gualazzi (OpenTelemetry)** 13:02 Nope.
**Antoine Gagniere** 13:03 then it's… we have to handle it differently than a normal error, right? Or…
**Francesco Gualazzi (OpenTelemetry)** 13:09 Probably not.
Because, yeah, because we do retry on,
**Antoine Gagniere** 13:16 Yeah, I guess. Okay, well, okay, anyway, I don't know enough about it, so… we'll just have to… I'll have to spend some time understanding what it means exactly, and… If we have to do something on client side, maybe the answer of that will be nothing.
**Francesco Gualazzi (OpenTelemetry)** 13:33 We are already doing the retryable and non-retryable distinction, at least in the AIC, but also in the GRPC, yes.
**Antoine Gagniere** 13:40 We distinguish the two categories, yes.
**Francesco Gualazzi (OpenTelemetry)** 13:43 Exactly. By the way, do you see an evolution in our design where we factoring OTLP, Well, Parksha is already like that, so OTLP is… now a… component that dispatches to two different underlying transports, or HTTP and GPC.
When you, basically, when you call OTLP export, you pass it a config, and the config has, you know, the protocol, which Dispatches to the, to the correct task.
Do you see an evolution of that?
Where we are able to also apply this type of logic, parser success, and failover, retry, no retry.
At that level, instead of in the transport.
**Antoine Gagniere** 14:30 Yes, yeah, exactly. I think that what I want to explore, yeah. But I don't have a definitive answer, but… Maybe we can, like, have a common logic for that, that is not specific to transport, and…
**Francesco Gualazzi (OpenTelemetry)** 14:42 Yeah, yeah, that would be nice. Okay.
Right? So, you are my man on this one, again, I trust you with my… with my dog.
I trust you with my dog on this one. Okay. So, go ahead. Feel free to explore and report what you found.
Yep.
**Antoine Gagniere** 15:04 So, yeah, I'll have to go, but… Yeah, thank you. Nice talking with you.
And Dario.
**Francesco Gualazzi (OpenTelemetry)** 15:10 True. Bye.
**Antoine Gagniere** 15:11 Right.
**Francesco Gualazzi (OpenTelemetry)** 15:14 And I think since no one else joined, we call it a meeting.
Meetings.
Alright.
Goodbye, everybody.
