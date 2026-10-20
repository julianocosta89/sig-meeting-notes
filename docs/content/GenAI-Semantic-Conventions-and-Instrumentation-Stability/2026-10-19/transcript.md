SIG: GenAI Semantic Conventions and Instrumentation Stability
Date: 2026-10-19
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Neil Yashinsky** 00:35 Hello, Ludmila, how are you today?
**Liudmila Molkova** 00:39 Hi, Neil, how are you?
**Neil Yashinsky** 00:40 Very good, thanks. It's nice to, chat with you. I don't know if I could quite say one-on-one, since we're on a recorded line, or whatever, but, you know, just… I mean, I don't have anything specific to chat, but just like, hey, there's nobody here yet, so just us.
I hope you had a nice… was it a vacation, whatever, you were, like, off, for a few weeks or so back?
errors.
**Liudmila Molkova** 01:01 Hannah!
**Neil Yashinsky** 01:02 Or just time off from work?
**Liudmila Molkova** 01:04 Oh, I was in Norway, I… it was a vacation, the proper one.
**Neil Yashinsky** 01:08 Fun. Fun! That sounds, wonderful. I'd love to hear, maybe more, more about it if you, because you're, are you, do you live in Central Europe, is that right?
**Liudmila Molkova** 01:16 Oh no, I live in the US.
**Neil Yashinsky** 01:18 Oh, you live in the US! For some reason, I thought, differently. Forgive me, obviously, just my… my ears biasing my expectations or whatever, but… have you been to Norway before?
**Liudmila Molkova** 01:29 No, it was my first time. It was pretty cool.
**Neil Yashinsky** 01:33 Yeah.
**Liudmila Molkova** 01:34 First time that far to the north.
Have you been?
**Neil Yashinsky** 01:38 No, actually, my mom just got back from, like, like, her and my stepdad did a little bit of a cruise through, it was, Sweden, they did, like, I joked that they went Viking, because they did… they went to Sweden, and then they forgot exactly the route that they took.
But, like, yeah, they ended up in Paris in classic, what was that, Rallow fashion or whatever. And they did a few places along the way, before ending up in northern France, and, you know, just, like.
was, they took us a boat, trip, and they had stops along the way, I think, through… I'm trying to remember… some really nice spots along the Mediterranean, even.
I don't remember exactly how… but yeah, it was a lot of fun, but not a long way to answer… I've never been. I've been as far as, the UK, as far as Europe, I think, as I've never been at all.
Just one time. Dude, it was a long time ago, it was 20-some years ago.
Hey, Aaron. Hey, Dylan, how's it going? Sorry, we're… I… you know, got… got looped me a lot of distractions.
I know we're, all really keen on, you know, more meetings and getting to work right around reporting status, so I'll let everybody get back to the status reporting of their meetings and updating on their tasks, as I'm sure we're all excited to get to.
**Aaron Abbott (Google LLC)** 02:58 Hey everyone.
**Liudmila Molkova** 02:59 Yay.
I'm just thinking, what should we, put on the agenda?
I… I took the… the… Reviews from the previous section we had.
And just add a little bit of context to them.
Doesn't seem like we have Max today.
So I'm not sure if you want to talk about the… Agent versus workflow stuff.
**Neil Yashinsky** 03:34 That makes sense. Yeah, I guess we'll have to wait and see if Max shows up, and yeah, it sounds like if not, then we should just wait on that one, right, without Max. I don't want to… I'm just guessing, totally could be wrong on that, but it seemed like he was very, I don't know if critical's the right word, or crucial for the conversation, but he had a big PR that was part of it, right? So it seems like he would be… it would be… incomplete to continue that conversation without him? I mean, we can talk about it, like I said, but, you know, to, define, or come to resolution, I guess is the word I'm looking for, on anything.
But again, Ludmila, I'm just… Trying to synthesize what I know.
**Liudmila Molkova** 04:15 Yeah. I'm just checking what we have here.
**Neil Yashinsky** 04:20 Yeah, that's what I remember we left off on.
And… The one I was wondering is… someone else asked this question too, so it's not, like, definitely not my idea, but, like, a, What's the word I'm looking for? The detailed information? Aaron, was it you who asked for, like, the Google Doc about, like, the structure of how this would work? I feel like somebody else had a request. It's certainly not mine, of how, like, the… whatever, the… the data structure would be populated in a real-world example, and thus allow us to, like, look at the two forms, you know, side by side, or whatever. I don't know, maybe do a little your IDI, forgive me, I'm… or Lududmila, am I making stuff up?
More… more flashbacks of the 80s from too much LDS in the 80s?
**Liudmila Molkova** 05:08 Which one? I missed this.
**Neil Yashinsky** 05:11 I thought it was Friday that we talked about, it was like, a Microsoft… oh, sorry, a Google Doc that was separate from the existing documentation that showed, The data structures populated by, like, one approach versus the other?
Am I just making all this stuff up, nobody remembers it?
**Aaron Abbott (Google LLC)** 05:34 No, I think it's just the tab, yeah.
**Neil Yashinsky** 05:37 Oh, this one. Oh, okay, yes. Yes.
**Aaron Abbott (Google LLC)** 05:40 Yeah, so there's… there's a couple here, and then, I… we left some… myself and Felix left some comments on the other tab, and I was just hoping that Max would take a look, but it hasn't yet, which is totally fine. And, Yeah, I said I could move them to the other… tab here, but I think I'll just wait for Max to take a look at these comments.
**Liudmila Molkova** 06:01 Today, probably, let's just talk about other things.
**Neil Yashinsky** 06:04 Yeah.
Thanks for highlighting that, Aaron. Yeah, so it's just its own separate tab right now, which is great. I'm not… no need to move it or anything, I just… I just forgot what the… what the structure or whatever the container… Was used to hold the content.
I'll look at that, too.
**Liudmila Molkova** 06:19 So let's, let's take a look at the PRs that we have that may be easy to move on with and, get to things.
So… I think Trask is proposing to resolve the comments that we have on counters to record zeros.
And… I think we went back and forth with it, we… This one proposes only positive values.
Four counters, and zeros for histograms, if it happened to return zero.
And the motivation here is that When it's zero, then you would… Need to record zeros for all modalities, or for a known only, and then it kind of gets very… ugly.
So I guess it's just the call for reviews, since Trask is not here.
**Aaron Abbott (Google LLC)** 07:24 I… yeah, I think… I guess I don't like that it's inconsistent with the histogram, but yeah, that's a good… the modality thing seems like a big issue, and then… I think in OTEL, do we ever have separate, like, error metrics? Because that's one other way I could think to kind of address this later, is if we wanted a separate intra… Separate counter to count, like, errors with, But yeah, I guess the modality would still not make any sense there.
**Liudmila Molkova** 07:52 Yeah, and that would be… would not be the… The usage, token usage.
metrics.
Yeah, but we… You, you would get this from histograms.
**Aaron Abbott (Google LLC)** 08:11 Yeah.
**Liudmila Molkova** 08:13 And if it's not… if there were some tokens used, we would record them.
Yeah, Neil?
**Neil Yashinsky** 08:21 Alright, thanks. So, just to make sure that I understand what the question is, like, and you just said it, I think, really well, but I just want to make sure, when you record a zero, that because you're, if you will, recording a zero, or listing a value as zero, that there's a lot of overtime resources associated with that value that don't justify the resources involved when you could just infer the value otherwise by it not being set. Is that… does that… Summarized that right?
Why a zero is… Not desired.
**Liudmila Molkova** 08:53 So, when we record talking usage, we record individual modalities, we don't record the total, like on counters. We have metrics that record it per modality.
and zero… does not… it's ambiguous how you record it. You can record for multiple points, for four different modalities, or you record one with a known modality.
And neither are super meaningful.
**Neil Yashinsky** 09:26 I see.
Okay.
Is that… and I thought at some point the decision question was even a zero value was to be used, or no zero value, or… but it sounds like you said… what I heard was that that's not correct. The histogram will also have a zero value.
It's a question of whether the… The value itself will be broken up.
As an individual property, or just covered by the histogram itself?
**Liudmila Molkova** 09:55 So the histogram always reports the… the number, the single number across all modalities, so it doesn't have any problem with reporting zero.
The counters, all of the counters have permodality, breakdown.
**Aaron Abbott (Google LLC)** 10:18 Okay, I'll take a look at the PR. I… one question, I guess, I hope it's addressed in the PR, but if you have, like, partial stream tokens, say you have, like, a request times out to consume the whole stream or something like that, do you record The tokens you did see, the tokens you did count.
**Liudmila Molkova** 10:36 I would expect whatever you've seen, if it's not 0, if it's bigger than zero, you record.
**Aaron Abbott (Google LLC)** 10:42 Okay, but do we record the error on that one, or just removing the error altogether from this metric?
**Liudmila Molkova** 11:03 from successful and failed operation, and we're not removing error type from them. And I think they do have error types.
**Aaron Abbott (Google LLC)** 11:12 Hmm.
**Liudmila Molkova** 11:17 Wait, where is it?
Huh? There's no error type.
Wait, it's OpenAI when I'm here.
There is no error type.
**Aaron Abbott (Google LLC)** 11:42 Okay.
I don't know if that was changed here, maybe I was just confused, but I guess that makes more sense.
**Liudmila Molkova** 11:48 Well, we should probably edit.
**Aaron Abbott (Google LLC)** 12:14 So, so, like, Yeah, no, I'll think more about it and give it a review, but… Yeah.
**Liudmila Molkova** 12:26 Okay.
Cool.
Okay, moving on, there is the configuration pure from Dylan.
And… I think there is a one open question.
Related to the hook.
**Dylan Russell** 12:49 Right, so this comment here is… maybe something better discussed at the SIG meeting, because I feel like it's gonna… Took a while to figure out, but… I was thinking it's interesting to maybe upload parts.
Using the upload hook.
That's what, like, Alibaba does.
If it's, like…
**Liudmila Molkova** 13:17 Yeah.
**Dylan Russell** 13:18 Yeah.
**Liudmila Molkova** 13:21 So, I think, like, let's, break it down. The… this meeting is focused on stabilization. Uploading parts is a new feature, we won't be able to stabilize it.
We have an implementation for the whole thing, right? And we know how it's used, pretty much.
Maybe that the fact that Thank you, you're mentioning that the Alibaba upload individual parts, right?
And that, at Google, we upload the whole thing. Maybe it's a sign that we are not ready to stabilize the uploading part yet?
Or…
**Dylan Russell** 13:57 They do also, like, depend on us, and do, like, like, depend on Util GenIA and do the whole upload.
So it's, like, an additional thing they offer.
**Liudmila Molkova** 14:11 Yeah.
**Neil Yashinsky** 14:13 Ludmila, I think Aaron has his hand up.
**Dylan Russell** 14:16 Yeah.
**Neil Yashinsky** 14:17 I mean, I guess I know it's a hands-off.
**Aaron Abbott (Google LLC)** 14:21 I was gonna ask… I don't… Ludmila, were you done with what you were saying, though?
**Liudmila Molkova** 14:26 Yeah, yeah, yeah, I'm just capturing, yeah.
**Aaron Abbott (Google LLC)** 14:29 Yeah, what I was gonna say was, Dylan, is there anything you see in, like, the current state, like, spec that we're planning to stabilize that would Make this, like, difficult, or would impact being able to do this later on?
**Dylan Russell** 14:42 Mmm… I… Don't think so.
I hadn't thought too much in detail about how the individual part upload would work.
But, yeah, it seems like it could be done separately.
**Aaron Abbott (Google LLC)** 15:05 Yeah, I mean, I think… does Alibaba use the URI part for that? Because I think…
**Dylan Russell** 15:11 Yes, exactly.
**Aaron Abbott (Google LLC)** 15:12 Okay, yeah, so I think if we can see a path forward, we could probably de-scope this one. I think I agree with Ludmila.
**Liudmila Molkova** 15:25 Agree with doing it later?
**Aaron Abbott (Google LLC)** 15:28 Yeah.
**Dylan Russell** 15:34 Yeah.
It's kind of interesting, they… what they do.
But I'll… pass on that. They also have this, like, pre-signed… like, URL auth mechanism?
Pretty extension, extensive, like, way to do, like, pre-signed auth.
Which… We could also potentially try and support, but yeah, another, like, big additional feature.
**Aaron Abbott (Google LLC)** 16:07 Yeah, I would love to chat more about it in the Tuesday meeting. I'm interested in this.
**Liudmila Molkova** 16:15 So, with this one? Should we take?
the upload away for now, from this PR, and… Discuss the upload separately?
Language would also be helpful, too.
Combine it with this discussion.
Because it advises against percent URLs.
Because credentials and telemetry.
**Dylan Russell** 16:49 But the pre-signed awe thing… is not about the URL that gets uploaded.
It's… It's like… what's a good summary of it?
It's like, you call a… a separate service to generate a pre-signed PUT URL for you.
And that… that's the URL that you call to do the upload.
**Aaron Abbott (Google LLC)** 17:32 Do you store, like, the pre-signed URL in the reference, or do you just use it for the upload and then put, like, the standard URI?
**Dylan Russell** 17:42 Right, that, that second one.
**Liudmila Molkova** 17:48 Hmm, okay.
**Dylan Russell** 17:50 Ew.
**Liudmila Molkova** 17:50 but anyway, so, like, from this perspective.
The stabilization scope, we would… It's not targeted for stability.
**Dylan Russell** 18:06 Well, we could still stabilize what's… what we have today.
Right.
**Liudmila Molkova** 18:13 Yeah, what it meant?
Like… I was reviewing this PR, actually.
And I realized that it's just, it wouldn't fly, the current design for the hook wouldn't fly in cross-language story.
For example, like, we pass the log record, and in Java, you cannot modify the log record after. You would need to parse a log record builder.
And it… it's… it would… we will need to spend some time polishing this.
And… It's just, it's completely additive.
We can, but it's just, it will take longer.
The whole thing.
**Dylan Russell** 19:00 Okay.
Do we want to proceed with, like, renaming the environment variables, like, the way you proposed?
**Liudmila Molkova** 19:09 I'm thinking the content enablement is orthogonal to the hook, right? We can… The environment variable enablement should be in the stabilization scope, but who configuration?
is completely separate.
Oh, and, like, I suggested to rename the hook as well, right?
**Dylan Russell** 19:28 Yeah.
**Liudmila Molkova** 19:30 Whatever you like. If you don't want to rename it yet, you guys wouldn't.
**Dylan Russell** 19:35 Alright, that's my repert.
Okay.
Alright.
**Liudmila Molkova** 19:44 Yeah, Neil?
**Neil Yashinsky** 19:47 Yeah, I was wondering, like, kind of towards Dylan's point, maybe, and, like, I felt like this was part of the, the woman from the World Privacy Forum's kind of question the other day, too, and, like, for folks who are coming and they want to be able to try to… ground decisions that they're making today in, like, questions that OTEL won't get to until tomorrow, if you will. Like, I thought, like, implicit in the stabilization effort and just trying to not get too far behind in a really fast-moving field, and so I'm just wondering if, like.
maybe… maybe separately, or, like, as a small part of this effort, or something like that, or just, like, I'm kind of thinking out loud, but, like, helping people understand… maybe two things, like where… what they're interested in is in the process, vis-a-vis these stabilization semantic conventions, and also, like.
How to make a decision that's grounded in, you know, the thinking of the committee that did the stabilization, if you will, and what we liked or didn't like, or we, you know, the voting public, if you will, what they agreed on and didn't agree on, so you could, you know, validate questions like this in… In the philosophy that we took to establish it? Does that make sense?
So that we…
**Liudmila Molkova** 21:06 If I'm fair, no, I don't understand what this question is about, and how it's related to stability at all.
**Neil Yashinsky** 21:12 We're making decisions now, right, to stabilize certain conventions, and we are… not… adding additional functionality right now, as you just said, like, we're stabilizing what's there, and we're not adding additional capabilities. Which makes sense to me, like, that's what I'm literally here for, is to ensure that some things get finalized and are used before we add additional scope.
But for those people who are working in the scope that we're not focusing on right now, to how it kind of… proactively… I think someone talked about, like, the roadmap of OTEL, and this is, like, maybe one level, higher, than the roadmap. It's something we're not considering right now, and just, like, you know, here's how to… Here's how we… not only made the Conventions, but decided on what wasn't a good convention, or was a good convention, and so you then… for people who want to do things that OTEL will eventually get around to liking.
then do it this way. And maybe it already exists, and I just forgot about it, and I just didn't know about it. It's probably just, like.
RTFM? I am totally okay with RTFMing me, because I…
**Liudmila Molkova** 22:29 I just heard TFM'd you in the chat.
**Neil Yashinsky** 22:31 Yes, yes, I consider that the highest possible compliment. I'm gonna be quiet for several weeks on this Meetings as a result.
**Liudmila Molkova** 22:37 Oh, please don't.
**Neil Yashinsky** 22:37 Motel sense.
**Liudmila Molkova** 22:39 Please, please keep talking. Anyway, let's… let's move on to the next one.
the… the parts.
So… Aaron, you updated it, right? And it now… it's now not on the unknown parts. I… Oh, you're already addressed.
**Aaron Abbott (Google LLC)** 23:09 we may have had a race condition with my agent, but…
**Liudmila Molkova** 23:14 Yeah, I think I'm…
**Aaron Abbott (Google LLC)** 23:16 I think I was in the process of updating description and stuff.
Was there… was there something besides that?
**Liudmila Molkova** 23:26 the normative guidance and examples, some trivial stuff.
**Aaron Abbott (Google LLC)** 23:30 Okay. No, I'll take a look.
**Liudmila Molkova** 23:32 Yeah.
Oh, I thought, like, your agent reacted to my feedback without, like… Any of your brain cells participating.
**Aaron Abbott (Google LLC)** 23:42 No, not quite yet.
**Liudmila Molkova** 23:45 Okay.
Cool, Dan, yeah.
**Aaron Abbott (Google LLC)** 23:48 Major on this one?
**Liudmila Molkova** 23:50 Nothing major. I, I, I almost approved it, it's just yet, yeah, there are some minor stuff.
**Aaron Abbott (Google LLC)** 23:56 Okay, just one note, I did… so there's a new PR in the stack?
Which does the same thing for the dual calls. I think we have… Something really similar, it's like a generic tool part.
And since we're seeing a lot of people have you know, custom server-side tools.
This just does exactly the same exact thing.
**Liudmila Molkova** 24:20 Yeah, so I guess maybe this comment my agent, noticed for two calls is addressed by that other PR.
**Aaron Abbott (Google LLC)** 24:30 Yeah, yeah.
**Neil Yashinsky** 24:33 Yeah, and I owe you feedback on this, too, if you will, Aaron, and I did have a chance to look, but I'll confess, my agent actually got a little bit confused and didn't notice the feedback that Lududmila left.
The first time around.
And so, I didn't think I saw anything that was broken, per se, but I recall there was one thing that I was trying to… quantify upstream of… I think it was, like, the, like, the blobs upstream in the Python hotel library that caused, like, I can't… I can't bring… I'll Slack you, though. I'll Slack you, because like I said, I was just trying to validate, I didn't want to, you know, go down, send you down the wrong… path, or whatever. Oh.
Yeah, I…
**Aaron Abbott (Google LLC)** 25:29 I mean, feel free to leave a review on the PR as well, that's totally fine.
**Neil Yashinsky** 25:32 Okay, cool, good, yeah, you know, I… yeah, I always like myself as, like, oh, here's a little… and because both, you know, prevent me from saying something unjustified, but also, like, make sure that… I mean, I don't think you'd be embarrassed, obviously, but just, like, sometimes it's always, like, best to ensure that my feedback is valid with the person I'm targeting with, rather than… first, rather than the whole internet. If you're okay with that.
**Aaron Abbott (Google LLC)** 25:58 Yeah, whatever you're comfortable with.
**Neil Yashinsky** 26:00 Awesome, awesome, yeah.
**Aaron Abbott (Google LLC)** 26:03 Cool.
**Liudmila Molkova** 26:04 Okay, cool. So, I think we're… Most dear, where's the parts?
And… it should… Should I review this one?
Any reason to keep it in draft?
**Aaron Abbott (Google LLC)** 26:21 I'm just doing human review and touching up the… gory AI description, but other than that, yeah.
**Liudmila Molkova** 26:31 So… Then… I think we need Felix for this one.
**Neil Yashinsky** 26:39 Just shout out on that one, Aaron, that's been really, insightful. That's, like, my favorite part about, working with… with, all you folks, these very, very smart folks, is, like, the amount of… useful information that you get exposed to on this call is just outstanding and really, enriching, so thanks.
**Aaron Abbott (Google LLC)** 26:59 Yeah, of course, I think, yeah, I think it would… I tried to put, like, the information that was in the comments into the… into the code so that next time we'll have more context on the kind of design and stuff, so…
**Neil Yashinsky** 27:16 Yeah, especially, like, tool… agent tool use, I feel like, is something that… is… I don't want to say it's underappreciated, but, like, the subtleties, or the importance of, or I guess a little bit of both, maybe, is like… really powerful stuff, maybe? Just, I don't know.
Good to know in detail.
**Liudmila Molkova** 27:40 Cool, and I think this one is the last among the reviews that we have.
And… And there was, comment from Trask.
So, in the couple of minutes that we have for the context.
This PR tries to define how to do the handoffs and other transfers.
And you can do it through a tool.
And… You can, in theory, do it in some other way.
So, like… Dev workflows, they just call agents.
Where you can… In LangGraph, you can do GoTo.
And it's… it's not a tool, it's just the… the return value.
Like, literally go to.
**Neil Yashinsky** 28:35 I'm sorry for laughing out loud, everyone, but I personally find that hilarious. I don't know of anybody.
**Liudmila Molkova** 28:42 Yeah, or there could be an orchestration that picks the next agent to run. And there are also transfers not to agents, like, among The main ones is transfer to human to approve.
And it could be a tool, and, essentially, I think we need to discuss more on, like, so, the proposal, Nikkio.
landed on is the generic way to describe any kind of transfers, and Trask is asking if we can limit it to the two calls, essentially.
So I think we need to talk more about it, maybe on tomorrow's call.
But I'm also thinking that… I don't know if it should be in the stabilization scope, because… It's… it's an extra feature that… We cannot…
**Neil Yashinsky** 29:35 Yeah, I think.
if I underst… Oh, sorry, go ahead, let me…
**Liudmila Molkova** 29:39 No, no, go ahead.
**Neil Yashinsky** 29:40 If I understand this correctly, they're asking to create a new additional transfer that is separate between humans and agents, is that what the ask is on that?
**Liudmila Molkova** 29:51 And so this PR trade mostly targets the agent calling agent.
**Neil Yashinsky** 29:57 Huh.
**Liudmila Molkova** 29:57 but it's just one of the possible things. Agent can call, non-agent, like a human, or an arbitrary node, or, It can be, not necessarily a to-call that.
transfer.
That makes a transfer from one engine to another.
**Neil Yashinsky** 30:19 Sounds good. Alright, I'll stay tuned on that. Yeah, thanks.
**Liudmila Molkova** 30:25 Okay, so Dan, we are done for today. Thank you for coming.
Please take a look at the PRs.
**Neil Yashinsky** 30:32 Have a good day, Vern. Bye.
**Aaron Abbott (Google LLC)** 30:34 You go, Peter.
