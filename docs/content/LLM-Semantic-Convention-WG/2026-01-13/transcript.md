SIG: LLM Semantic Convention WG
Date: 2026-01-13
Duration: 46 minutes
============================================================

## Zoom Recording Transcript

**Minghui Zhang** 09:48 Okay.
Hello, Imina.
A year?
Oh, I can't hear you.
Maybe I mute… mute?
**Liudmila Molkova** 10:16 Can you hear me now?
**Minghui Zhang** 10:17 Yeah. Yeah, sure.
**Liudmila Molkova** 10:19 Awesome. Thanks. Sorry, I have to keep my camera off today, my video setup is broken.
**Minghui Zhang** 10:25 Yeah.
My, my video setup is broken also.
Okay, how are you?
Yeah, don't have Nussi.
How have you been?
**Liudmila Molkova** 10:44 Pretty good, thanks.
**Minghui Zhang** 10:47 I think, we are also busy in the last, in the last year.
**Liudmila Molkova** 10:56 Yeah, this is the… Busy years.
Alright, everybody.
**Minghui Zhang** 11:04 so many… so many SAMCOP and, instrumentations of, to…
To work, to… to build.
Yeah. Yes, I have left two, issues in the agenda. Have you… Seen that.
**Liudmila Molkova** 11:29 Yeah, I was, typing the reply to one of them.
You mentioned… Okay… Let me close this.
So this one, if I understand correctly what you're saying, that you would like to have some specific implementation of the upload hook that would
Work with, multimodal contact, right?
**Minghui Zhang** 12:01 Yes, exactly.
So we want to, we want to, upload the, individual multi, multimodel data in the, completion hook or other hook. I, I don't think, I don't know, the existing,
a hook, if the existing hook could, allow us to do so. So maybe we, we add another hook. But we,
After all, we want to, send the individual multimodial data in, the instrumentations, so that
we can, capture them as, UI… as a UI, even if, they, returned by the model as,
raw data.
**Liudmila Molkova** 13:06 Yeah, so… I mean, it… The hook stuff is…
We intentionally don't specify it yet, because we want people to…
Actually build what they want, and see how it works.
is there… a reason…
you want to have it in OpenTelemetry, or are you happy with what you do in your own distro, like…
What is your goal here?
**Minghui Zhang** 13:40 Actually, we have our, distro… we have the implementations in our distro repo… repository. We want to proposal these, I mean, best practice
As a choice or op- option in, person contributors, so that people could,
How to see? How to see it? Mmm…
the implementation, it's, based on the, GNI UTL, right? So, we have to modify the GNIU tool to do so, and, now we, actually
do this, in this way, but it's, it's a little difficult to extend the YouTube because, we have to
extend… extend it and, pay more attention… pay more attention to the, com… conflicts, between the upstream, repository and our…
our, distro. So we want to,
build or contribute this, this logic into upstream, so that we could, maintain this logic here. And, we…
We will not, we will not have any conflicts, in the future.
**Liudmila Molkova** 15:30 I see. Yeah, I mean, it makes sense. The… Carly, you wanna…
Get some feedback or, thumbs up from people who work,
On Dotos, Errand would be the one.
I can bring it up, on the tomorrow,
call and ask everyone to take a look.
He would have more opinions and thoughts and feedback on this than me.
**Minghui Zhang** 16:07 Yes, yes, thank you. I… actually, I have, I have notified Aaron before, but he didn't, he didn't reply me. Maybe he's missing this, these comments.
**Liudmila Molkova** 16:26 Okay, he usually joins the call on, US-friendly time, so…
I'll make sure to ping him.
**Minghui Zhang** 16:36 Yes.
I will,
I will connect him, soon, and I will tell… I will tell him this, issue.
Okay, thank you.
**Liudmila Molkova** 16:55 Yeah, thank you.
Oh, by the way, you had a pull request here.
Didn't even happen?
**Minghui Zhang** 17:06 Maybe the PR is under, is still under review?
It's too many.
So you can filter this by author.
**Liudmila Molkova** 17:24 Yeah, curious.
**Minghui Zhang** 17:28 Oh, yeah.
That's it.
**Liudmila Molkova** 17:32 I think we discussed it on the… Call… last week.
And one thing that came up… S… Regarding this environment variable.
So… You know how there is this additional… Thing called… Capture mode…
Yeah, there is this environment variable as well, right?
Capture message content.
**Minghui Zhang** 18:13 Yeah.
**Liudmila Molkova** 18:14 And it could be… Span event, or span an event.
So, we've been discussing… I'm sorry, I… I… I…
was going to leave a comment, but I didn't.
But essentially, The idea was that if people
set this to event, or spend an event, it means that they want event to be emitted.
So that… Don't need to configure both.
**Minghui Zhang** 18:49 Yes, yes, I, I know, but, could you, could you see the comments from… I don't know, who, who left the comment?
**Liudmila Molkova** 19:02 Yeah, in… do you like?
**Minghui Zhang** 19:04 And yeah.
**Liudmila Molkova** 19:05 due in summer. We… been… .
**Minghui Zhang** 19:31 Oh, yes.
That's it. So, maybe in Thailand, he, he wants to,
If we set the capture model as spend an event.
He wants to send both of them, but maybe the, the, the, the, the chat history are not in event, just the metadata.
So, that's what, that's maybe what he wants to see.
**Liudmila Molkova** 20:16 Yeah, he's been in the call, and that's what we… talked through.
that… Let's say… Where's this one?
Give me a sec.
So there is this friend.
Why is the last Tuesday?
And,
We could go… Tuesday, 6.
112.
So, if this is set to event, For span end event.
then… Record.
events. Like, why would somebody
want to set it to event and not record events. It… it doesn't make sense?
**Minghui Zhang** 21:50 I mean, maybe they want to, they want to just, they want to just emit the events, but without the…
Without the chat history.
**Liudmila Molkova** 22:06 Yeah, so then, if… This is set.
is true.
Ben.
But… is span.
Then, if we emit… events without content.
**Minghui Zhang** 22:31 Yes.
**Liudmila Molkova** 22:32 Right?
And then… if…
We can also think about if it's explicitly false.
then probably…
And then said th-this.
Otherwise, people would need to all… to configure two things.
Right?
Taro, and let's say this to… Event.
And we're just optimizing the user experience for them by saying, okay, you can just save this.
**Minghui Zhang** 23:32 Mmm… So… let me see… If true God's Hispaness.
So what it means is, we set this, option as true by default.
**Liudmila Molkova** 23:57 No, this, this option is probably false by default, S… Pause by default.
But if somebody said this, Where this…
Then it's an equivalent of setting it to true.
**Minghui Zhang** 24:22 Oh, I… I got hit.
Oh… So… Yeah, it makes sense, it, it's, it will get a better, user… user… experiments, but…
I think it's a little tricky.
**Liudmila Molkova** 24:45 Okay.
**Minghui Zhang** 24:47 Because, ops… The option may be, hmm.
Okay, okay, I… I… it makes sense. I… let me, let me document it.
And we could, It, it, it is… the scenes better. It was seen better.
**Liudmila Molkova** 25:11 Okay, cool, yeah. And, Dylan was, okay with this approach.
At least verbally.
**Minghui Zhang** 25:19 Okay, okay, I will do that.
**Liudmila Molkova** 25:21 Thank you.
Cool, and then, other than that, I think people were, in general, happy with this. It's great that it's coming.
So, it's the only comment I had on my side.
**Minghui Zhang** 25:39 Yes.
**Liudmila Molkova** 25:42 Okay, and you also wanted to chat about this friend.
**Minghui Zhang** 25:49 So, yeah, yes, so this is, it's more about, Question, or a best practice.
Because we are, we are adding… we are trying to add the instrumentations for the…
multimodal, multimodal API, and, we, we, we have many long-running, think, gen… content generation tasks.
So, we want… we always want to, capture the output messages, the multimodal messages,
Even if in, in a single model, model, but,
it's a little hard to do so, because, people will just send a task and create a task. We only…
could, capture the task ID or file ID, and, people will pull… will… will, start, pulling task to query, the… to… to query the task status.
And, download the multimodel data after it's…
Actually ready, but we can't… maybe we can't, instrument this, this download span, in… in our instrumentations, so it's, very, very hard.
**Liudmila Molkova** 27:35 Yeah, and I don't think there is any magical answer that would work, so I… so what I think you're referring to, and correct me if I'm wrong, I started…
typing the response. So we have, like, a start, long-running operation thing.
And there will be some… Operation AD.
Here.
And… Then… then we will… this service, or,
Maybe even some other service will start pulling it in a loop.
And…
we will… we will be able to instrument those as, those calls. And finally, maybe somebody will call download
content.
And… Where… Ideally, you should be able to correlate All these friends together.
**Minghui Zhang** 28:41 Yes, so that's the best apprentice, right?
**Liudmila Molkova** 28:46 So I think the best one would be if we could have, encompassing…
span here. Like, if there was a…
If we could have a span that wraps this whole async flow in one Thing.
But from what you described, it sounds like we don't necessarily have it, or cannot have it in many cases.
**Minghui Zhang** 29:15 Yes, we, we could, we couldn't, always have this, encompassing span. It's very ideal.
**Liudmila Molkova** 29:31 And what you're saying, you could have, or could not?
**Minghui Zhang** 29:36 We could… we could not have this van.
**Liudmila Molkova** 29:39 Okay, I see.
**Minghui Zhang** 29:41 Hmm… Yes.
It's hard to have this, but maybe we could ask our users to add this Always.
**Liudmila Molkova** 29:56 And we could, they probably wouldn't, it would be difficult, but we probably… we can recommend.
So… Let's… This is the ideal scenario, right?
**Minghui Zhang** 30:10 Let's think about the…
**Liudmila Molkova** 30:16 The realistic one, so that in the download span, we would have attributes, events, risk, content.
**Minghui Zhang** 30:29 Yes.
**Liudmila Molkova** 30:30 and more realistic.
We would have, like, we should be able to start the track individual operations.
There will be an Operation AD.
And… The tricky part…
would be, as you mentioned, to propagate the context, right? Because… It's just…
It's just hard after the span is done.
To pass the context over to the next one.
to the pulling.
**Minghui Zhang** 31:16 Yes.
Yes, so, now, now we could, we could only do this, in, in a single process, and, so, we could, maintain,
HashMap to, to maintain the mapping between the operation ID and the spam context.
**Liudmila Molkova** 31:42 Yeah.
**Minghui Zhang** 31:48 Hmm.
**Liudmila Molkova** 31:53 So, like, in the worst case, the only correlation Is the operation idiot.
**Minghui Zhang** 32:11 Oh, yes. Yes.
**Liudmila Molkova** 32:13 So this is the worst case.
And… The… there is something in between that you're proposing, potentially.
That we would do the best effort to… Keep… Operation… ID.
To trace context.
**Minghui Zhang** 32:51 Yes.
**Liudmila Molkova** 32:52 And… Yosh. Japan.
one as… blink on… parent, or a link.
Great.
**Minghui Zhang** 33:15 Yes, yes.
And…
**Liudmila Molkova** 33:30 This is a common problem.
And so, can you… it's not specific to Gen A, right? I'm pretty sure in Alibaba, there are a bunch of…
These long-running operations that have this pattern. You start an operation, you pull, and then at some point, you're done, and the correlation doesn't work great for them.
**Minghui Zhang** 33:51 Yes, so, yes, that's what we want, that's what we want, what we want. So, I want to, I want to ask you that, if we could, maybe in future, we could, submit this,
This proposal, or best of practice as, SAM code or a specification?
**Liudmila Molkova** 34:19 Oh, so you would like to maybe document…
**Minghui Zhang** 34:24 Yes.
**Liudmila Molkova** 34:24 And how to deal with it.
**Minghui Zhang** 34:28 I'd like to try to do so because we, we don't want to have the, mixture, or temporary, temporary, implementations. But we, actually we have the…
we have the implementations in our distro. I will show some prototype, when… when I send this proposal, or document it.
**Liudmila Molkova** 35:02 Yeah, and I mean, I think it's a great addition, and just don't focus it enough on AI patterns. I think it's useful beyond that, and it's not specific to the
AI, really.
**Minghui Zhang** 35:18 Yeah,
Yes, so in my, in my opinion, we actually have this… we actually have something like this in messaging system, and, it, works
Well, now.
**Liudmila Molkova** 35:38 You mean the.
**Minghui Zhang** 35:42 Yes, the links and the, it, it solves the, relationships between producer and the consumer.
**Liudmila Molkova** 35:51 Yeah.
**Minghui Zhang** 35:55 But I… maybe I couldn't, add a… I couldn't create a… do… do this work a…
soon. Such a… in a…
these days, because we have many other things to do, but I will try to do that, and you'll show me, very great suggestions.
Thank you so much. I will try to do so.
**Liudmila Molkova** 36:29 Okay, cool, thank you.
So I'm going to just, bobby, call it a comment.
Here… But yeah, that would be cool to document.
**Minghui Zhang** 36:52 Yes.
No, let's see… Okay, maybe… that's hard?
I have… I don't have many other scenes to, sync.
Wait, I want to, a little, a little thing, a little stuff to ask, that, we want to, we are now building our, vendor, SAM call now, something like, Alibaba.
Alibaba namespace of the attributes, so we want to, put them under the…
open telemetry semantic conventions, in, vendor-specific, semantic conventions. I, I don't know, I don't know if it's, available.
**Liudmila Molkova** 37:54 It's available, what we're trying to do in some conf now, and we're…
We didn't do it in the past, and it's something we're introducing, is…
we want others to be able to host their conventions, and import up and telemetry once. It's currently technically possible, but there are, like, no docs or good examples for you to follow, so it's pretty much…
It's possible, but impossible. But, like, ideally, we would rather not have any vendors here. We have some.
So the way to, bring things in, is to…
have a group of people, and I think you have a group of people that can own Alibaba conventions here.
**Minghui Zhang** 38:45 Hmm?
**Liudmila Molkova** 38:46 what would… put, like.
like, similarly to Azure, they would exist here, but you probably would be an owner. You and a couple of maybe other folks on your site would be owners for these conventions.
And you would be, would decide how this page looks like and what you, wanna do there.
So if you want to send APR, I would rather start with, like, finding the group of people, and saying, okay, we want to work on Alibaba Cloud.
Just choose GenAI or Alibaba Cloud?
In general, And then, we would,
Create a group for you, you will be the code owners, and stuff like… this.
But you would be on the hook to review the PRs related to your area.
**Minghui Zhang** 39:46 Okay, okay.
**Liudmila Molkova** 39:47 Would you… would you… are you interested in even publishing conventions here? Like, would you consider owning your conventions and working on them yourself and publishing them on Alibaba documentation site?
**Minghui Zhang** 40:04 Yes, actually, we want to do so, but, maybe the owner or the staff is,
My… my… is my… is my…
I see my staff, not me, but I will, I will tell him to do so. So…
Maybe we should, send, send an issue or PR to, create a group first?
**Liudmila Molkova** 40:39 Yeah, so, you can send it to the, semantic conventions, or maybe to the community repo, or… I'll find some example.
**Minghui Zhang** 40:59 Okay.
**Liudmila Molkova** 41:01 So you can use this one as an example.
Let me find the chat, they lost it.
Here we go.
So you would need to mention a few folks, who…
Who would be part of the group.
You don't need to provide much context, just mention the… the part that you would wanna…
work on. It could be just Gen AI, as I mentioned, it could be…
Do we have Alibaba Cloud here? We do have some.
**Minghui Zhang** 41:49 No, I don't think so.
**Liudmila Molkova** 41:51 Okay.
So let's… Unserated.
Okay, option one, cost… In Otel, sorry.
Second option host, Provide care… Self.
If you want to pursue this, we would need, Group.
What to mention there? Which… Area.
Do you want your own?
oh, Alibaba.
Cloud, we're just… German AI part.
Members?
Include.
That's probably it.
**Minghui Zhang** 43:21 Yeah, so that's… I think that's enough. I will… I will research it and, have a discussion… have a discussion with our, co… with our, colleagues.
**Liudmila Molkova** 43:35 Yeah.
And if there is anything, like.
I don't know why you and a hosta did not tell.
if I were you, I would rather host them by myself, because then I would have
Yeah, it'd just be so much easier to update things and, I don't know.
have a full ownership on this. It takes a bit for open telemetry to move, and you can probably do it much faster, if… if you self-host them.
**Minghui Zhang** 44:06 Yes, so we… we do host our, our specific, semantic conventions now, but we want to, we want to share our implement… implementations, with,
the hotel genetic, so I think maybe, we… maybe we host in hotel could, push this, process more, smoothly.
**Liudmila Molkova** 44:40 Yeah, the one more option for you to consider, if you host it by yourself.
We could still have a page here for Alibaba, it will just point to your conventions.
So you would have the visibility, and people who discover Hotel GenA conventions would discover Alibaba's, it's just the content will be on your site, and we will just have a link there.
**Minghui Zhang** 45:06 So, yeah, okay. Also, we could just add a document to link to our own page, right?
**Liudmila Molkova** 45:16 Yeah, so if you want to study length.
add one here in the README, and feel free to add a page with a link to your conventions and provide any context you would like to have there.
**Minghui Zhang** 45:30 Cool. That's… that seems, more cheaper.
Two per week.
**Liudmila Molkova** 45:38 Yeah, it… yeah, I mean…
I think this is a good middle ground to allow you to move, fast and be flexible, and also for…
For us to not drown in every detail.
**Minghui Zhang** 45:54 I will, I will have a discussion between our colleague, and I will do it soon.
**Liudmila Molkova** 46:08 Cool, thank you, then. Have a discussion, let me know if I can help with something on Autel's side.
**Minghui Zhang** 46:15 Yes, thank you, thank you so much.
**Liudmila Molkova** 46:18 Oh, gosh.
Thanks, Dan. Have a great day, have a great rest of your week.
**Minghui Zhang** 46:25 Yes, so maybe we will, offline. So, have a good night.
**Liudmila Molkova** 46:33 Yeah, thanks.
**Minghui Zhang** 46:35 Okay.
**Liudmila Molkova** 46:35 Bye.
**Minghui Zhang** 46:37 That's all. Bye.
