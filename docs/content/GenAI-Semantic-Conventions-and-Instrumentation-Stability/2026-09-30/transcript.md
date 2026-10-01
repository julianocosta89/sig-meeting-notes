SIG: GenAI Semantic Conventions and Instrumentation Stability
Date: 2026-09-30
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 02:22 Hi, folks!
**Siri Varma Vegiraju** 02:26 No.
**Christopher Cordi** 02:27 Hello.
**Liudmila Molkova** 02:29 Yeah, let's wait for… A couple of minutes for more people to join.
Yes, let's get started!
So please add your name, So I haven't been here for the past couple of weeks.
Like, Aaron, do you want to drive or do you want to tell me how you folks approach it here?
**Aaron Abbott (Google LLC)** 04:03 So, we've been doing, like, both, you know, agenda items, and then there's this tracking tab. I don't know if you've seen that one in the documents. Yeah.
And then we've just been kind of doing… anybody can give, like, the daily update if they want, Or if you go through, invite them, and discuss stuff.
**Liudmila Molkova** 04:24 Okay, so then, let's do this… And since we're here… Do you… I'm not sure if Neil is here.
Do you folks have any update on the… Json schema?
**Aaron Abbott (Google LLC)** 04:42 I don't have… I filed a bunch of issues, and then I remembered why we made some of the decisions we did.
So, and we chatted about things a couple of times, so… I think… I think I have enough to, like, make progress and just send out PRs, but… is it… do I sound like you, by the way, or is it in the background noise?
**Liudmila Molkova** 05:01 Oh, there is some background noise.
**Aaron Abbott (Google LLC)** 05:04 Okay, sorry. Yeah, I'm just gonna say, basically, that we have, I think we have an idea of what we want to do, and we discussed a couple of things, but we weren't sure… should we just, like, merge breaking changes directly right now? And that's something we were discussing last week, is how to do these breaking changes.
**Liudmila Molkova** 05:24 Why wouldn't we?
**Aaron Abbott (Google LLC)** 05:29 I don't know, because we have no, like, we have no tags in the new repo.
As, like, a starting point or anything like that.
**Liudmila Molkova** 05:38 Yeah, like, we… We are merging breaking changes anyway, right?
For everything else, so why wouldn't we do it here?
**Aaron Abbott (Google LLC)** 05:49 Okay, yeah, that's fine. We're also discussing in the context of the instrumentation as well, so… But that's fine. So I don't really have much to update then.
**Liudmila Molkova** 06:02 Would you be able to, I don't know, start filing PRs or like what are the next steps?
**Aaron Abbott (Google LLC)** 06:09 Yeah, yeah, definitely, I can, I can send a couple of yours.
**Liudmila Molkova** 06:20 Okay… I think Dylan is not here.
Right.
I would encourage everybody to review this.
Oh, sorry, this is not a PR, there is a PR deal and sent… Here we… R.
I made a bunch of proposals here, and I would like to get people's opinions.
But I'm thinking… We.
Call it message.
And it's not always correct.
And because it also applies to system instructions, to arguments, memory records, and whatnot.
So, maybe… We can keep supporting it in the instrumentations, but what we document is something more generic for the environment variable.
And for the configuration, which is probably not part of Stabilization because of the… this API.
In our tell is not stable. I I would propose the like.
Some… some way to make it more.
Extendable.
So I have some ideas here.
But my main interest for the scope of the stabilization is polishing the name of this environment variable.
**Aaron Abbott (Google LLC)** 07:55 So I get you mentioned tools and all that stuff. Do you think we want to have them? I know we're making it more specific in this config below, but do we want this environment variable to just be like all of them?
**Liudmila Molkova** 08:09 I'm in… Ideally, we want more, but it's… it's what we do today.
And it's not blocking anything else in the future.
And, like, tool arguments and responders can be large and sensitive, so we do want them opt-in, and then we need an opt-in mechanism.
And I would love for the stabilization effort to just start with environment variable documented.
But, like, just polish it.
Yeah, anyway, so there is this PR, Dylan is not here.
And… He'll probably get back to it once he's back.
But I would encourage you to review if you're interested in the configuration.
Okay… Oh… Transcript.
So… This guy still needs the review and approval.
It's ready for review… I'm working on fixing the Ci.
So it's just more renames. Like this is an example of breaking change, right? We a very disruptive one, actually.
I.
So this renames this France to Quentin France.
This one is no longer applies to inference.
And… Don, it's a bunch of… Additions, renames, and… Moving things around.
I also put everything in, A single document for the client inference.
So like it now describes this operation fully. It describes the span.
all the metrics, event… And… For this front, it just links to the other doc.
We can rethink it, but I think it's not important, really.
**Aaron Abbott (Google LLC)** 11:14 Uma, were you there when we were discussing with Felix about I don't think he loves it, loves the name inference.
I don't remember if it was Monday or Tuesday.
**Liudmila Molkova** 11:26 Yeah, I mean, we can rename it.
But again.
But… It will be a huge change. Let's just do it one by one.
If we have a better name, let's find a better name.
**Aaron Abbott (Google LLC)** 11:47 Okay.
**Liudmila Molkova** 12:00 How do you feel? Do you want to block on this?
**Aaron Abbott (Google LLC)** 12:04 No, no, no, I… I don't… I don't have a strong preference, like, this isn't here, but the argument was definitely, like, the… What we see on the server side is usually not like the actual inference. It's like an API.
With profits over cycle calls and all this stuff, so… I don't think we made a decision or anything like that.
Yeah, maybe I'll just ask him to review, maybe I'll turn on a Slack for it.
**Liudmila Molkova** 12:32 I mean, I understand the problem.
It's more like there are 2 orthogonal problems.
That however, whatever word we use here.
We need the set of metrics.
To be special.
And we can renew… change the word, just replace whatever we have here with something else.
But structurally, we should have it.
And I don't think we need to solve this all at once. We can solve that problem too, separately from this problem of The operation duration being problematic.
**Aaron Abbott (Google LLC)** 13:11 Yep, agreed.
**Liudmila Molkova** 13:20 Okay… Okay, so and this is the the inference thing.
**Aaron Abbott (Google LLC)** 13:59 Yeah, I kind of volunteered for this because I, because it's really similar to the parks, but if anybody else I think that's kind of the option that I'm feeling.
I don't… I don't have anything since Monday. I… I was discussing on this one, but I… since we're in good order, I did that.
**Liudmila Molkova** 14:21 Need.
Oops.
Agent workflow… I don't have any updates. Surya, do you have any updates?
**Surya Teja** 14:44 Yep, Ludmila, I was just planning on meeting you. I took a look at our, at your PR that we discussed yesterday.
And, from what I have, from my homework, I understand that merging both the spans makes a lot of sense, and also creating a turn span is really good if, Really good for reporting metrics, and Helping people understand the token consumption as well as the duration for each turn that's happening with agent or whatever they're conversing with.
But.
I have… few questions around the timing, because we want to do this before November, and how feasible is that is not known to me, because we still need to merge this first.
In my mind.
and how I'm planning, and then merge both invoke agent and workflow, and then create a turn span. So, the body of work is huge, in my opinion. I might be wrong.
But since you already have a draft PR and stuff, I would lean on you to provide some guidance on what do you think for the body of work.
**Liudmila Molkova** 15:59 I wouldn't be… I don't think we should be… Constrained by the timeline… I mean, We… If the choice is between the scope, like, what can be stabilized, and the timeline.
Let's just do the right thing.
Can we stabilize without merging?
Agent and workflow, I think it's problematic.
**Surya Teja** 16:33 Yeah, I'm sorry, what is problematic? The merging or having both spans? I'm sorry, I'm not…
**Liudmila Molkova** 16:40 Having both spans, like, we know it's a problem.
**Surya Teja** 16:43 Yeah, I agree.
**Liudmila Molkova** 16:46 If there is somebody who… Okay.
I think it creates… So many… Concerns, at least in my head.
That we should not stabilize without it. If it means it will take longer to stabilize, then so be it.
I… we can… we should still try.
But if there is somebody who… Want to advocate for, like, keep… keeping things as they are.
But let's talk through.
**Surya Teja** 17:27 Yeah, but no one actually gave any, negative feedback on combining the spans, as far as I understand. It's more or less, the definition of turn, as well as.
Up.
Only the definition of turn and how we can report metrics is only contention, based on my latest read, but… Mostly it's positive around merging those spans and.
Hmm, defining a turn span.
**Liudmila Molkova** 18:04 Yeah.
Okay, so I guess let's forget about the timeline for a moment.
**Surya Teja** 18:11 Yeah.
**Liudmila Molkova** 18:12 I think the good next step would be to… And.
Maybe summarize… The mental model.
And the pros and cons.
In… And I'll try the dock of some sorts.
We can review it.
by the next call on Friday.
And… we can see, like, how controversial it would be. If it's not controversial, then it should be easy to merge. If it is controversial, well, we'll see.
**Surya Teja** 18:52 Yeah, I can dump my thoughts on a doc and share with you.
**Liudmila Molkova** 18:56 Okay.
**Surya Teja** 18:56 And yeah.
**Liudmila Molkova** 18:58 Sounds great.
**Surya Teja** 19:00 Yeah, cool. Thanks Rutunila.
**Siri Varma Vegiraju** 19:12 One of the largest city.
Oh.
For the agent invitation time?
03 Bible.
**Liudmila Molkova** 19:23 Sorry, I have a hard time hearing you. Can you repeat?
**Siri Varma Vegiraju** 19:25 Are you able to hear me now?
**Liudmila Molkova** 19:28 Yeah, it's just… it's a little bit noisy.
**Siri Varma Vegiraju** 19:31 Yeah, I'm outside currently. I'll mute myself once I do the update.
**Liudmila Molkova** 19:43 Sorry, I didn't catch it.
**Siri Varma Vegiraju** 19:45 Yeah, what I was trying to say was I'm outside. I will mute myself once I get the updates.
**Liudmila Molkova** 19:51 Oh, okay.
Yeah, sure.
Cool, oh, okay, so Siri, you're next, and you would want to… Later… Not sure if Wolfgang is here.
Okay, so this one is merged, nice.
Yeah.
Okay, so… It seems like this solves the… Concerns… Around agent name… This is another thing to review.
But.
Okay, so it seems… no… Announce here… Okay, tools.
**Aaron Abbott (Google LLC)** 22:04 It's like, Okay, so that'll be… I, I was waiting for… Maybe I'll just point to this about this one, because I left some comments, but it seems like pretty much all the inference APIs support this now, so… I don't know. I don't know if we're at speed tool. We need to do anything. But this is another influence.
**Liudmila Molkova** 22:43 I'm trying to understand what's the problem.
Oh, content part. Oh.
**Aaron Abbott (Google LLC)** 22:51 Yeah, so basically, most, most, like, Anthropic, OpenAI, and Gemini, they all allow a tool part to contain, like, nested content block, which includes, like, for example, inline bytes, or an image, or something like that.
But they pretty much all added it in, like, this and these styles.
Google added it in the last year.
Since we did the original stuff, so… But the question is kind of like.
Every agent framework might represent this slightly differently. So yeah, this is, this is on chain.
They have, like, a special… type that you can return, but from, like, the agent framework's perspective, it doesn't seem like it needs to be schematized.
Like, for a hotel, and then… For, for the models, though, we should probably update the… Because all the models pretty much support this, because when I built them, it's not the same.
**Liudmila Molkova** 23:42 Wait, wait, it can still be a random object.
**Aaron Abbott (Google LLC)** 23:48 Okay.
**Liudmila Molkova** 23:48 So.
**Aaron Abbott (Google LLC)** 23:49 And I'm obvious, so…
**Liudmila Molkova** 23:52 Like, we do convert this into the content parts.
Or we don't, like, if it can be an object, how can we chorus it to the content part ever?
**Aaron Abbott (Google LLC)** 24:06 You're talking about for the execute tool?
**Liudmila Molkova** 24:08 Yeah.
**Aaron Abbott (Google LLC)** 24:10 Yeah, I don't think we should do that for a speed tour. I think we should just do it for the inference.
**Liudmila Molkova** 24:19 Oh.
So, like, for the… when we see a tool call response and input messages, we try to See if it's the… The.
known type.
**Aaron Abbott (Google LLC)** 24:34 Yeah, because it will already match, like, the API that we understand, so it's a little bit easier than underneath the AgentForum platform.
**Liudmila Molkova** 24:44 I see. But then it would still be… Annie is just a dad.
It can be any, we might fail to recognize it.
**Aaron Abbott (Google LLC)** 24:55 Yep.
**Liudmila Molkova** 24:57 Okay.
So… Should we, like, say it's Post Stability? Because it's nice… it's kind of nice to have.
To recognize specific types.
**Aaron Abbott (Google LLC)** 25:15 I mean… Honestly, my two cents is we should probably… It seems like a lot for… The… the Stability, potentially, because… It's just a lot more research than supporting a couple of inference APIs.
We have to figure out how each framework.
how each panel does this, and then make sure there's nothing to go here.
**Liudmila Molkova** 25:41 That's me.
Maybe leave a comment here.
**Aaron Abbott (Google LLC)** 27:37 Yes, I think my only concern is, like, for any… Any or whatever is just still any, so it's hard for, like, downstream consumers to understand.
That it's supposed to be one of this new thing.
You know what I'm saying?
**Liudmila Molkova** 27:52 What can we do?
**Aaron Abbott (Google LLC)** 27:55 Yeah, I mean, we could, we could wrap the current calendar.
Inside of, like, a… I have, like, a tag me on it.
I'm trying to make it forward compatible.
**Liudmila Molkova** 28:13 Okay.
Like, we would have some discriminator that would say, like, a generic part.
Right.
**Aaron Abbott (Google LLC)** 28:38 Yep.
**Liudmila Molkova** 29:16 Do you have any thoughts, Evan, on whether we should put it into the scope?
Or is it already covered there?
**Aaron Abbott (Google LLC)** 29:28 I mean, I'll think about it, but, like, we did discuss making everything forward compatible, and it seems just like a good… Good way to do it.
I can see the list.
**Liudmila Molkova** 29:42 Okay. It sounds like you already put it here.
In scope for Stability.
And we can rethink if we… Okay, we are at time… Umm.
Then please take a look at the PRs. There are some.
3 velvets, for example.
This couple of friends are super trivial.
And there are some less trivial ones.
Yeah, and see you on Friday then.
**Aaron Abbott (Google LLC)** 30:34 Okay, well, thanks, everyone.
**Liudmila Molkova** 30:37 Thank you.
