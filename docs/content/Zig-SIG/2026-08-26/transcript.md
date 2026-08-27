SIG: Zig SIG
Date: 2026-08-26
Duration: 38 minutes
============================================================

## Zoom Recording Transcript

**Giovanni Panice** 01:11 Hello!
**Francesco Gualazzi** 01:15 Hi, Joanne, how you doing?
**Giovanni Panice** 01:18 I'm fine. You? Back from the holidays?
**Francesco Gualazzi** 01:22 Yeah, yeah, started working this week, again.
But I'm still in the seaside. I'm still working from here remotely.
The connection is not the best.
**Giovanni Panice** 01:33 Cool.
**Francesco Gualazzi** 01:33 I'm managing to… to live with it.
What about you?
**Giovanni Panice** 01:39 Well, I'm back, I never been in a holiday yet, to be fair.
**Francesco Gualazzi** 01:44 Some of the…
**Giovanni Panice** 01:45 you know, but I need to leave, but, always at my home. Next week, I'll be… I'll be in a bit… I'll take a bit of a PTO, so… I'll be… I'll be not joining the meeting.
And, well, I'll be… a bit to the beach, so…
**Francesco Gualazzi** 02:05 Nice.
Enjoy, my friend, enjoy. Thank you, thank you. Okay.
Let's wait another couple of minutes and see if someone else joined.
And then we can discuss. I don't know, do you remember August 12th? August 12th.
Because I'm looking at the meeting notes, and August 12th, the attendees is empty, there's a question mark. I think only Antoine was joining there, so…
**Giovanni Panice** 02:36 I will…
**Francesco Gualazzi** 02:37 No.
I discussed with Antoine the Zig Hotel demo and the profiles briefly, so it was me and Antoine around it, okay?
Yeah, so this.
Cool.
Yeah.
Maybe I should raise an issue.
Is there any issues with regards to the profiles? I mean, we already have one.
But to be more concrete and discuss with the… Yeah.
Because when I talked about it with, with Antoine, he said, you know, maybe we just exposed the bindings to the proto in a good way, but also some helpers, like, I don't know, extract profiles, or even some visualization libraries, for example.
some, flame graph rendering via WebAssembly, you know, that Zig can compile to WebAs.
**Giovanni Panice** 03:40 Yeah.
**Francesco Gualazzi** 03:41 Let's see. Well, let me do this. Actually, let me bring this again here to this meeting.
So I would like to… Boo.
Go further a bit with this one.
I have UPRs, yes.
Okay.
Alright, so the existence of span end makes it confusing. Can we think of a more intuitive API? Did you create this one?
**Giovanni Panice** 04:14 Nope.
**Francesco Gualazzi** 04:16 I think it was, Antoine then, let me check the issue. Oh, no, this is, Jay Tata Takuvara.
And, yeah.
**Giovanni Panice** 04:25 Yeah, Jay Taka, who opened the PR? I don't know if you put the… you… who put the item.
**Francesco Gualazzi** 04:32 Maybe, maybe the creator of the issue, who knows?
**Giovanni Panice** 04:37 I don't think he… I don't think he has, right access to the…
**Francesco Gualazzi** 04:43 Yeah, no, the document is public.
I believe anyone can write, or comment, please? No, makes sense, I don't… I mean, I don't know, but okay.
**Giovanni Panice** 04:54 Let me check…
**Francesco Gualazzi** 04:57 Is it going incognito?
Oh yeah, I see you.
**Giovanni Panice** 05:00 Yeah, but with another account. Yes, if I use another account… Yeah, yeah, maybe you are right.
**Francesco Gualazzi** 05:08 That's okay. Anyways, yeah, happy to discuss that with you, and I think the first thing should be assigning this one to someone to triage and assign.
**Giovanni Panice** 05:19 Do you want to share the screen, or I can share the screen about…
**Francesco Gualazzi** 05:23 No, I wouldn't tell you.
**Giovanni Panice** 05:24 Okay, to… to take a quick overview.
**Francesco Gualazzi** 05:29 Yeah, yeah.
**Giovanni Panice** 05:33 Excuse me.
**Francesco Gualazzi** 05:34 Okay, do you see it?
This is what was raised, what's that, sorry.
Let me open it.
Right?
So… well, let's just read it, and then we can assign. The only code part that notifies span processor is Tracer and span… span end.
Records… no, tracer and span. SpanN records the end, timestamp and flips his recording off. No processor is involved, okay?
**Giovanni Panice** 06:08 Hmm.
**Francesco Gualazzi** 06:09 And spawn, yes.
**Giovanni Panice** 06:12 Okay.
**Francesco Gualazzi** 06:12 Yes, we call the provider, let's say, Hook.
on Span End, yes, and then it says PubFNN, which is what it's called… line 364 in the SDK.
**Giovanni Panice** 06:33 Mmm.
**Francesco Gualazzi** 06:34 Leave self-recording return. Yes.
But… Span in the valve… Okay… well, this could be flipped.
No, never mind, okay, okay, this is correct. Self and time Unix narrow timestamp, or else int cast now, okay.
**Giovanni Panice** 06:58 Okay.
**Francesco Gualazzi** 06:59 That is regarding false. Both trace examples con only span in null, okay? And reserve that… comment above them says, use Span N for basic functionality. They wire a simple processor, a standard processor, but no span.
Ever.
**Giovanni Panice** 07:16 This is the process.
**Francesco Gualazzi** 07:19 They built those plans for yourself.
**Giovanni Panice** 07:21 So, later.
**Francesco Gualazzi** 07:23 First of all, I guess this is a bug.
Right?
**Giovanni Panice** 07:26 Okay, yes.
Okay.
**Francesco Gualazzi** 07:28 I mean, how do we… I mean, we should have tests for those, not just the.
**Giovanni Panice** 07:36 Indeed it's very… indeed it's very strange, honestly.
**Francesco Gualazzi** 07:39 I remember, I remember I was testing it.
**Giovanni Panice** 07:41 Yeah, reduce one span with the same wording as the example, verifying only the ending, or, okay. So… Can you scroll down?
**Francesco Gualazzi** 07:53 Yeah, let me zoom a bit. Okay. I think the examples are meant to not print.
Okay, there should be a search in the example. We can check later. Reduce to one span with the same wiring as the example, writing only on ending call.
I used to. What does this mean?
I'm not… Okay… Oh.
Wait, wait, wait. He's saying, if you call span end before, And Span?
Reduce too much power with the same WVR, even only adding the coal.
Third row is the sharp edge. Spun end clears his recording, and end span begins with… You see? No, I spotted the bug. I said, this is wrong.
Okay, so calling both in the natural order also drops the span, no variant produces an error of line. Okay, this is legit.
But, yeah, because the API is meant to be called… to be used like so, but we cannot prevent that any… that anyone else does this.
**Giovanni Panice** 09:08 Obviously.
**Francesco Gualazzi** 09:10 This is tricky, though. Okay, listen, unit tests never take this part, which is why the suit, Okay, you see, we did, we do unit tests.
Which is why the suite passes while the example exports nothing. Processor tests call, processor and span directly. Span processing and provider test use tracer and span.
Pair the Trace SDK spec on end is called when a span is ended. This is correct. I mean, this is… this is, the whole… point of putting this line here, right? So, when the processor And a span, it needs to… so the provider has a span, it needs to call the processor, yes.
Professors.
**Giovanni Panice** 09:56 Boom.
**Francesco Gualazzi** 09:57 In other SDKs, ending the span is the single operation that triggers it. Okay, so this is his saying, basically, when the span struct is ended, that is when we should call the… as the on-end stuff, not vice versa. So, proposal, short-term. Fix board example to use the response plan and state in span end, document it in terms of this makes sense. I can send a PR for this part.
Longer term makes Pan unnotified processor itself, the span holding a reference, back to its answer. Okay, this is… I don't know, we can talk about it. Which also involves 3 silent drop. That changes the span lifecycle.
So it probably belongs… yes, indeed. But, I mean.
Okay, I mean, let's just say…
**Giovanni Panice** 10:50 Well, wait, one thing, before writing anything, I saw that a pull request. Oh, don't assign to you.
**Francesco Gualazzi** 10:58 Not? There is already a pull request open?
**Giovanni Panice** 11:01 Because, yeah, because I saw that there are… if you go back, if you go back, to…
**Francesco Gualazzi** 11:06 Are you sure?
**Giovanni Panice** 11:07 issue. I saw that there was, if you scroll down, there is a link at the April request, which was closed.
**Francesco Gualazzi** 11:13 Matt? Yeah.
**Giovanni Panice** 11:14 I want to understand who Benedict.
**Francesco Gualazzi** 11:18 The… yeah, no, the problem here was, that it was… Oh, Antoine closed it.
**Giovanni Panice** 11:25 Oftentimes.
**Francesco Gualazzi** 11:25 wrote, okay? Oh.
And we fixed it, okay?
**Giovanni Panice** 11:29 Hey, for this reason, I said, okay, so, so please assign to, Jay Takatura.
**Francesco Gualazzi** 11:38 I cannot assign to him, because he's not, in the… I mean…
**Giovanni Panice** 11:44 the issue.
No, you can assign it to email me.
**Francesco Gualazzi** 11:47 Okay.
**Giovanni Panice** 11:47 I mean, he wrote the issue, so now you can assign to him.
**Francesco Gualazzi** 11:51 Let me see…
**Giovanni Panice** 11:54 So… so… so, as you can see.
**Francesco Gualazzi** 11:57 That's right.
**Giovanni Panice** 11:57 Okay.
**Francesco Gualazzi** 11:58 Okay?
**Giovanni Panice** 11:58 Remove… and then, put the… in progress, put in done.
So, because, I mean, it's merging…
**Francesco Gualazzi** 12:06 It's not done. No, no, no, wait, wait, wait.
They are only fixed examples.
**Giovanni Panice** 12:11 That's a good thing.
**Francesco Gualazzi** 12:12 Yeah, this is the short-term fix, I think.
**Giovanni Panice** 12:14 fix… Oh, no, okay.
**Francesco Gualazzi** 12:17 Okay, that's what I was writing.
**Giovanni Panice** 12:19 So what… okay, so please write also to Jadura, thanks to report the…
**Francesco Gualazzi** 12:26 Exactly.
**Giovanni Panice** 12:26 Do you have any cycle to do AP pull requests for the long term?
**Francesco Gualazzi** 12:31 I mean… We have discussed this, right? There's no… Disney…
**Giovanni Panice** 12:37 Yeah, you can give a suggestion.
**Francesco Gualazzi** 12:40 I want to provide guidance here, because again… flipping the order around… I mean, the API is confusing, yes.
Because if you can, if you can do this… And the result is that the Spanish autosporter, it's not good.
**Giovanni Panice** 12:56 No.
**Francesco Gualazzi** 12:56 But, changing the whole thing is… I… it's difficult, and also it's creating, an entanglement. I don't know if it's the right.
It's creating a problem, because again, the whole point is that we split the span, which is part of the SDK, from the provider, which is part of the PI, right? And because Zig does not have interfaces and all of that, we are currently working around that a little bit.
**Giovanni Panice** 13:35 -
**Francesco Gualazzi** 13:37 So… yes.
And also, there is… I mean, I would like to see… yeah, the first thing that I would… ask him or her, I mean them, is what they… what do they think about this notify news, right?
**Giovanni Panice** 13:57 -
**Francesco Gualazzi** 14:03 That's why I also signed it to myself.
**Giovanni Panice** 14:05 - Yeah.
-
**Francesco Gualazzi** 14:39 Huh?
**Giovanni Panice** 14:40 Yeah.
**Francesco Gualazzi** 14:44 I'm asking because… Structural.
is, as… It pickled tomorrow.
Okay?
**Giovanni Panice** 15:31 Nice.
**Francesco Gualazzi** 15:34 I love this type of involvement from him. I hope we didn't spend… Too much time, or…
**Giovanni Panice** 15:42 Sorry, what you said? Sorry, what you said? You love?
**Francesco Gualazzi** 15:45 I love the involvement of Jada Tahura, I don't know where…
**Giovanni Panice** 15:49 Yeah.
**Francesco Gualazzi** 15:50 Junji.
Depend.
Great.
Okay.
I love this. Okay. So I would, I would write here and say, discussed.
Briefly.
**Giovanni Panice** 16:04 Indeed.
**Francesco Gualazzi** 16:05 Sure.
to…
**Giovanni Panice** 16:09 Maybe, okay, maybe… Hmm.
**Francesco Gualazzi** 16:16 2.
**Giovanni Panice** 16:17 Okay.
**Francesco Gualazzi** 16:18 Shock the car.
Nope.
**Giovanni Panice** 16:20 Okay.
**Francesco Gualazzi** 16:22 Preview PR.
**Giovanni Panice** 16:25 Okay.
**Francesco Gualazzi** 16:26 Well, we have a handful of PRs open, nice.
**Giovanni Panice** 16:28 Yeah.
All right.
**Francesco Gualazzi** 16:30 This is, this is, okay.
**Giovanni Panice** 16:33 Yeah, workflow, I mean, you can merge it. Sometimes I merge them, sometimes I wait for some liaison, because some stuff are related to the Open Telemetry, you know.
**Francesco Gualazzi** 16:44 Yeah, yeah, yeah.
**Giovanni Panice** 16:45 Foundation, so…
**Francesco Gualazzi** 16:47 I hoped that Josh would pick up the fixing of the teams, because Antoine.
**Giovanni Panice** 16:56 He's an evil lawyer.
**Francesco Gualazzi** 16:57 A, cannot.
**Giovanni Panice** 16:58 And now I'm able to watch.
**Francesco Gualazzi** 16:59 It should be able to match, huh? Yeah.
**Giovanni Panice** 17:02 Okay.
**Francesco Gualazzi** 17:03 Oh, there's also a PN format one, nice. What do you want to… you want to go older first, I suppose?
**Giovanni Panice** 17:12 Yes.
**Francesco Gualazzi** 17:15 Okay.
So, this one I reviewed, and it's assigned to me.
And, it's on hold. There are a couple of, A couple of things… Here, so this needs to be fixed.
**Giovanni Panice** 17:29 Hmm?
**Francesco Gualazzi** 17:30 I'm waiting for the… contributor, so in Cedar, in Cedar.
You see that?
incidentere, in Italian.
**Giovanni Panice** 17:42 Where, He could be Italian, so…
**Francesco Gualazzi** 17:46 Then, I'm waiting for him either to pick them up. But those are… the only one is blocking, because this one, Antoine corrected me, I mean, we don't really need… I mean, I would prefer that we have the initialization to null, because it's a new… field in a public API, so…
**Giovanni Panice** 18:06 Yes, for electrocompatibility.
**Francesco Gualazzi** 18:08 We don't have a stable API, so there's a blurry.
**Giovanni Panice** 18:11 Yeah.
**Francesco Gualazzi** 18:12 By the way, whatever.
This one, no, this one needs to be fixed, because it's an actual bug, because we don't check the validity of the span, but okay, never mind. So this will be picked up eventually. Or, if it's not, I can edit it and… And, merge it, but this is a nice fix from Inchida, thanks for putting it. And then we have a handful of things from Antoine that, is working on the gRPC implementation, finally, so let me… say this out loud, so GRPC… development in progress.
And I would like to add this one, but I don't know if I can… Party?
Yeah. Yeah, this is nice, because it's the only thing that is missing to make, like, a beta really available to users, no?
**Giovanni Panice** 19:04 Yeah.
**Francesco Gualazzi** 19:04 gRPC prototyp is probably the standard that is used across many, many, many, many implementations.
Okay, let's go back, here… I don't think this is the correct… the proper time to review, but I… yeah, I will also assign to me.
Can I assign it to me as well?
**Giovanni Panice** 19:29 Why do you want to ascend to Yahoo?
**Francesco Gualazzi** 19:31 Want to review.
**Giovanni Panice** 19:32 Okay. Put you as a reviewer. Put you as a reviewer, not as a meer.
**Francesco Gualazzi** 19:36 But I'm already… okay, whatever.
**Giovanni Panice** 19:39 Which is better to, you know.
**Francesco Gualazzi** 19:40 Okay.
**Giovanni Panice** 19:41 Only for, I mean, for the record, okay? Only because…
**Francesco Gualazzi** 19:44 Yeah, yeah.
**Giovanni Panice** 19:45 In Fisher Weekend forgot the…
**Francesco Gualazzi** 19:48 Absolutely. I will go into that later. I mean… Yeah.
Okay… I don't know if you add host resources automatically… oh yeah, this is… I remember it was also in the old repo.
This is for the…
**Giovanni Panice** 20:07 Being good.
**Francesco Gualazzi** 20:07 resource attributes.
That are automatically fetched from environment instead of manually instrumented. This is also nice, thanks, Antoine.
Okay, this is also something that I had seen in the previous repo, because it wants to… separate, building the artifacts from executing, the… Notables. That's fine. It's good.
It's certainly speeding up the development of a gRPC, because then you… the build itself is the one pulling in all the dependencies from the C library wrapper, which we agreed to use for now, because we don't have a stable ZIG gRPC plugin. So what we will do is we will wrap the C API on top of, with some ZIG bindings, and then this is a project that already lives in Antoine's personal repo. I asked them to port it over here, but it's not strictly necessary, and then we can, we can use this wrapper to build the actual OTLP, gRPC implementation.
This is also from Antoine, For the source location, oh yeah, nice.
I didn't even remember that, we missed this.
You know, the location is the file.
**Giovanni Panice** 21:37 Yeah.
**Francesco Gualazzi** 21:38 line number, no? But, why is… was it not implemented?
**Giovanni Panice** 21:43 Yeah, boo.
Honestly, I don't know.
**Francesco Gualazzi** 21:48 Okay, I will… okay, let me assign this.
**Giovanni Panice** 21:50 I know, I mean, sometimes, I don't know, mmm… Antoine is, sometimes, likes to add, fields that… because I don't remember this location, in the log, so… in the API, in the stack, honestly, so…
**Francesco Gualazzi** 22:19 Even if it's not in the… I guess the spec says, and I have to check because I don't know it by hand.
**Giovanni Panice** 22:26 Yeah, excellent.
**Francesco Gualazzi** 22:27 You are free to… you are free to add more fields if they contribute to making the event meaningful, which is… It's correct in this case.
**Giovanni Panice** 22:39 Okay, okay.
**Francesco Gualazzi** 22:40 I guess this is also something that other DKs do, I don't know. Maybe.
The gold one likely does it, because when I used it, I always saw the locations being printed, so why not?
**Giovanni Panice** 22:54 - okay, I don't know.
**Francesco Gualazzi** 22:56 And then, finally, oh, this one is important, this one is, yeah, because I don't know.
**Giovanni Panice** 23:03 I don't know if you saw the discussion… Yeah.
**Francesco Gualazzi** 23:06 Yeah, briefly.
**Giovanni Panice** 23:07 Yeah, so… so, Bach, pointed out that, there is a discussion related to the contribution in AI into… I mean, it's a big problem in a big project, but our project is not so big, That, has a lot of automated, yet, automated contribution, which mean… means, you know, a lot of work on reviewing, on do this kind of stuff, no? Triaging, so for now, it's not so big, so we don't… we are not in the loop on this kind of problem.
for open Telemetry Zig.
At the same time, I suggest to… back to, in any case, to write down inagent.md.
as a standard, and something that can be meaningful for us to, you know, at least to, you know, to point the agent to the guideline on the contribution, no? Especially to the co-author, for the, agents, so… I think that we can, we can merge it. I reviewed it, it's okay.
I didn't.
**Francesco Gualazzi** 24:18 Oh, you're…
**Giovanni Panice** 24:19 Yeah, I didn't, say okay, but it's okay. So, it's a bit… it's a starting point, so you can, you can merge it, don't worry.
Okay. It's very tiny.
**Francesco Gualazzi** 24:30 I trust you entirely.
**Giovanni Panice** 24:32 Oh, boy.
**Francesco Gualazzi** 24:33 on this one, okay. Oh yeah, the benchmarks are correctly using the optimization thing… but I don't understand you.
It isn't?
isn't this a repetition of what's already in the README, or contributing? I don't… I mean…
**Giovanni Panice** 24:50 Honey.
I don't get what you said, so, sorry, can you repeat that?
**Francesco Gualazzi** 24:53 So, when we have this block here, right?
So this, this whole thing, I'm pretty sure it's already in README, Slash contributing, you know, slash development or.
**Giovanni Panice** 25:07 Yeah.
**Francesco Gualazzi** 25:08 what's the best practice? Is it to rewrite the whole content, or link from other…
**Giovanni Panice** 25:13 Okay, yes, mostly the idea is, with an agent, AgentMD.MD is a standard, okay, for, cloud code, Copilot, not for… sorry, not for cloud code, sorry, but for, open code, Copilot.
And, mostly the idea is to.
write, again, the README, because this is the context that is already present inside the agent, okay? So it's okay to have, again, some stuff related to the README, okay?
**Francesco Gualazzi** 25:48 Okay, alright.
**Giovanni Panice** 25:49 because it's something already prepared, okay, from the agent, okay, which is okay. Important thing, because I understand your point, you said, okay, so we have to maintain the README and the agent, well.
As Antoine pointed, did you write it by end, or use an LLM?
**Francesco Gualazzi** 26:10 Okay.
**Giovanni Panice** 26:10 Well… the… okay, he wrote to myself, but the reality is, both, because you… he generated the boilerplate, the analysis with an agent, then he, changed a bit the… the… the stuff related to the agent. So, basically, it's okay to… to… you know, to give some, stuff, because you will spend more token, because you have to read from the README and recreate the kind of, you know, instead you have already the agent.
Okay.
**Francesco Gualazzi** 26:49 But isn't… so what I'm asking, actually, is isn't the agent normally going to fetch this file as well? When it reads this, isn't it going to say, I'm also going to read that one and put it in the context?
**Giovanni Panice** 27:03 Yes, huh?
**Francesco Gualazzi** 27:08 Likely, I mean, maybe, I don't know, I mean…
**Giovanni Panice** 27:13 Well, but I mean, if you are search… because you pointed the comments, no? In the first instance, if you search for the comments, you have read it in the agent.
So it's, I mean, usually when I see agent.md, they place the… the commands, usually. So, I don't know. Well, we can… maybe we can remove, we don't… I mean, it's not in our business to, you know, to… our, burn it token from contributors, okay?
**Francesco Gualazzi** 27:49 No, no, no, no, I'm saying that. For example.
**Giovanni Panice** 27:51 No, no.
**Francesco Gualazzi** 27:52 One thing that I am a bit wary is that, again, this is in the README, and when I want to change it and turn it into a build option, for example, instead of using the args, the build args here, I want to say minus the test filter counter. Now I need to update it in, like, two or three places, like this one, the readme, the.
**Giovanni Panice** 28:17 Yes. Yeah, yeah, I said, the problem from a maintenance problem, I know.
**Francesco Gualazzi** 28:22 Okay. No, I mean, it's fine.
That's okay.
**Giovanni Panice** 28:25 F…
**Francesco Gualazzi** 28:26 If we can… if we can accept this, the thing, I think this is… this is helpful.
**Giovanni Panice** 28:35 Hmm.
**Francesco Gualazzi** 28:36 Oh, this is important, yes, perfect.
**Giovanni Panice** 28:38 Yeah, I mean, I mean, my idea was only to add the guidelines. So, the stuff related to not… no, the co-author.
**Francesco Gualazzi** 28:50 That's the most important thing.
**Giovanni Panice** 28:53 Yeah, he was… but, I mean, he wrote down other stuff, so… Well, I have to say it's a normalagent.md, nothing special, so…
**Francesco Gualazzi** 29:04 Okay.
This is also interesting, I mean, he picked it correctly, right?
**Giovanni Panice** 29:10 -
**Francesco Gualazzi** 29:11 Very good.
Tesla… Okay, I will review and,
**Giovanni Panice** 29:21 -
**Francesco Gualazzi** 29:21 probably approve, because again, once it's in, we can iterate off of it, right? So…
**Giovanni Panice** 29:28 It rings.
**Francesco Gualazzi** 29:28 changes, and… See how it behaves, actually, because I haven't, I haven't been, I haven't been programming with any coding agent on this SDK project for a while now. I want to see… The most… the most recent model, how it does.
**Giovanni Panice** 29:45 Are you not using Cloud Code with, Zig?
**Francesco Gualazzi** 29:49 I mean, yes, but not for the past, let's say, 4 to 6 weeks.
**Giovanni Panice** 29:55 Oh, okay.
**Francesco Gualazzi** 29:55 I haven't done any big development with models, and, you know, Opus 5 came out, and Sonet 5 came out, like, three weeks ago.
**Giovanni Panice** 30:05 They can take into account that Cloud Code doesn't read theagent.md, huh?
**Francesco Gualazzi** 30:11 Yeah, you need to link it to close.
**Giovanni Panice** 30:13 Exactly.
**Francesco Gualazzi** 30:14 But I can do that in my… in my…
**Giovanni Panice** 30:17 Yeah, previous, your workspace. Yes.
**Francesco Gualazzi** 30:21 Okay, alright, then, yeah, everything looks, nice.
contribution… This one, I can edit it myself, probably it will be faster.
And this one, yeah, this is the biggest one we are waiting, this is a nice fix, but… We are actually waiting for it to be… fixed properly in…
**Giovanni Panice** 30:48 We're talking about flight.
**Francesco Gualazzi** 30:48 I will probably reach out to Laurent here, the author of Zig Protobuff. It seems that he's busy with other stuff, or he's just on holidays, because again, France is not very different from Italy. In August, everyone is on holiday.
**Giovanni Panice** 31:03 Well, yes, in, in France, maybe they are a bit, yes, like us, yeah.
**Francesco Gualazzi** 31:10 Yeah, yeah, yeah. Okay, then… then, yeah, check again and see… and see when we… when we land this, it's gonna be very important, because it's a nice fix.
**Giovanni Panice** 31:21 Okay, from my point of view of issue, do we…
**Francesco Gualazzi** 31:28 Have you, have you noticed it is… oh!
We have a new one.
Have you noticed this is growing too much, for our capacity, or…
**Giovanni Panice** 31:38 Well, for sure, for our capacity, yes. Indeed.
**Francesco Gualazzi** 31:42 Amazing.
**Giovanni Panice** 31:42 My suggestion is always say, hey, do you have any cycle to do a contribution?
**Francesco Gualazzi** 31:47 Okay.
**Giovanni Panice** 31:48 I mean, we, we don't have so much capacity, and I mean, we don't have any backbone from a point of view of, companies that we are paid to contribute to this, library. So, it's important to ask for community contribution.
but yes, it's growing, honestly, because I didn't see all this, issue. So, my suggestion is to, I mean, to take a look and see if there is something that can be feasible for the… Okay…
**Francesco Gualazzi** 32:25 Oh, this is a big one, actually.
Maybe this is something… this is a… this is one where I could test the agents on and see what happens.
**Giovanni Panice** 32:34 This person accepted my talk.
**Francesco Gualazzi** 32:36 Yeah, yeah, I wrote this code, I remember perfectly, I wrote this one.
Yeah, yeah, yeah, when I was building the context with, with Enrique, I…
**Giovanni Panice** 32:46 Well, well, you can ask if Beck wants to do a contribution, huh?
**Francesco Gualazzi** 32:52 Okay, okay, yeah.
**Giovanni Panice** 32:53 If he has some cycle, if he wants to take this…
**Francesco Gualazzi** 32:57 You can inspect some tokens.
**Giovanni Panice** 32:59 Yeah, exactly, so this is the new… The new open source work, so…
**Francesco Gualazzi** 33:04 The new currency, okay.
I'd rather work on this first, honestly.
**Giovanni Panice** 33:12 Meh.
**Francesco Gualazzi** 33:13 Yeah.
Yeah, this is, this is important, actually.
This is… yeah, this is blah, and… Sign myself, I will work on this first. This is more important than the trace context.
Okay.
Nice.
This is beautiful.
**Giovanni Panice** 33:36 Cool.
**Francesco Gualazzi** 33:38 Time is up, sorry for dragging over 3 minutes longer, and I don't think we have to do anything for the migration of meetings to Linux Foundation, right? Did you check that?
**Giovanni Panice** 33:50 Yes, actually from… Hmm.
**Francesco Gualazzi** 33:56 So, sorry for that.
**Giovanni Panice** 33:57 Yes, actually, we don't have anything to do, okay? Because I, maybe, I mean, maybe I'm… I don't have the credential, I don't have the role, but I tried to log into the Linux Foundation portal, okay? Yeah.
I'm able to see the calendar, all the stuff related to the new process, and I have some errors. Okay, so my suggestion is to check, to log in.
And check if you are able to see anything.
And, if not, maybe we can, I don't know, ask to our liaison if they can do anything, because, I mean, from our side, we cannot do anything, so…
**Francesco Gualazzi** 34:52 Okay. I will, will double-check that, okay?
**Giovanni Panice** 34:56 So, but I'm pretty sure that you are in the same situation of me. So, there is the link, click on the link, log in with your GitHub account, and go to the, community, I don't remember the name, the stuff related to the… But, then you… I mean, from my side, I get an error that I don't have access. Yeah, exactly, yes, so… Oh, because it was, it was interesting also for me, for, my project, for the Begin, because, it simplifies a lot of this stuff for, you know, for public, work log, and so on, so…
**Francesco Gualazzi** 35:43 Okay, nice.
I will check.
Let me add this to the note as well, so I don't forget.
And probably I will be able to join also next week, so… the profiles will be continued also. I wanna… I wanna find the time to expand on that and build something, but again, not… not… not a priority. We have a handful of bugs that are more important to voice.
**Giovanni Panice** 36:12 Yeah, yeah, yeah, yeah, honestly, yes, I would, like to… well, hmm, We should use a bit more the library, with some example, and see if there are bugs, because the problem with this library is that we don't use it in production. I mean, at least for me.
So, we don't find the bugs, so, we, need to wait for the community. I know that, I don't remember the name. In our team, there is someone that has developed some microservice and used this library. So…
**Francesco Gualazzi** 37:01 Which libraries are you?
**Giovanni Panice** 37:02 Our library, the OpenTech, yes, I remember, Jacob. Jacob is… his company has a kind of microservice, or I don't… I don't remember, some kind of proxy.
I don't And they use the library, so they can a kind of dog fooding, okay?
**Francesco Gualazzi** 37:22 Yeah, I would love to hear feedback from them on the performance and the.
**Giovanni Panice** 37:26 Yeah.
**Francesco Gualazzi** 37:26 Hey, Annie.
**Giovanni Panice** 37:27 Yeah. Yeah. So… This is the thing.
**Francesco Gualazzi** 37:32 Nice.
That, that, that would work just fine.
**Giovanni Panice** 37:37 Okay, if there is nothing else, I think that we can close here, so…
**Francesco Gualazzi** 37:44 My attention.
**Giovanni Panice** 37:45 Cool. Bye-bye.
**Francesco Gualazzi** 37:46 JMA.
**Giovanni Panice** 37:47 You too, bye-bye.
