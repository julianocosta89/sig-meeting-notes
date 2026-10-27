SIG: GenAI Semantic Conventions and Instrumentation Stability
Date: 2026-10-26
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 00:42 Hello.
**Dylan Russell** 00:47 Hey.
**Liudmila Molkova** 00:59 Oh my god.
There's some things from the… General call… I'm trying to do this one… I've added parts to the agenda today.
J alone!
Christopher… Absolutely.
If you have anything you wanna talk regarding the stabilization, please add it to the agenda.
Just do a little bit of housekeeping.
But there was a… a couple other PRs I wanted to see if we can make progress on.
This friend, if we have anybody.
Okay.
Feel free to add more things.
So maybe let's get started.
I see, Erin, you're here. I wanted to chat about parts.
I think it's in a good shape, it's just that… Need to decide what to do with the system parts.
**Aaron Abbott (Google LLC)** 04:08 Yeah, I just pushed a fix for what you suggested before.
**Liudmila Molkova** 04:13 Oh, nice. Yeah. And then this becomes irrelevant.
**Aaron Abbott (Google LLC)** 04:18 Yeah, it just, it makes it so you can… It does the same thing that we did for the other one, where it just allows text and other ones.
**Liudmila Molkova** 04:26 I see.
**Aaron Abbott (Google LLC)** 04:27 Yep.
**Liudmila Molkova** 04:44 And we have a test for it. Nice.
Okay, then we'll just need another approval on this, and we should be good.
**Neil Yashinsky** 05:03 Ludmil, do you know if I should be able to… if I have, whatever, needed to approve this myself? I was looking at it, and I wasn't sure if it needed another review first, or what… if my… Credentials were inadequate.
Or both, maybe?
**Liudmila Molkova** 05:18 You already approved?
**Neil Yashinsky** 05:20 Oh, I did, we… Oh, yeah, so did you… Did you say we needed another one, or no?
**Liudmila Molkova** 05:30 And another approval from, from a formal approver.
**Neil Yashinsky** 05:35 From a formal approval. Okay, perfect, thank you.
**Liudmila Molkova** 05:38 Yeah, thanks. It's still very valuable to see your approval. Yeah, yeah, no, I'd like to stop you.
**Neil Yashinsky** 05:45 It's also good to know why limitations, as they exist, so I can figure out how to, well, expand them or whatever.
I guess not expand my limitations, but yeah, you get it.
**Liudmila Molkova** 06:28 Okay… Do we have cakes?
We do not have Felix, so then… I think… I addressed… Everything… He had, and I think on the last call.
we figured out the source of the confusion that I was proposing. He thought that I was proposing this as a solution for the internal… the inference on the model.
And… I'm not, and I try to… Explain it.
And I think the last, discussion we had is that I put it initially in the registry, so it applied to every usage of this, the token usages that they reported for the whole request.
And since then, I moved it to the client inference, so nothing changes in the registry.
GitHub Corporate.
Okay, maybe there is more, too.
Oh, so this is for Entropic.
So… Where is the registry change? GitHub.
Yeah, so this is the commit. It's no longer in the registry.
And instead, it's a note on each attribute used by the inference span.
To say that It is.
The number of tokens reported by the provider for this inference operation.
So it no longer leaks into other operations or into general definition, so when we define… if we define the internal inference or other shapes of inference, we would be able to Override this.
With this, I'm thinking about merging it. Since it's been out for a while, we discussed it, and I hope I addressed everything. If there is anything else, we will just… Send a follow-up.
Craig.
And then… We don't have Macs, and I thought… He updated this, but he didn't. It's still in vogue.
invocation.
So it seems we're waiting for him to update, and I don't know if it makes sense to review now, because it's just… In the previous state.
So there is… doesn't seem to be any discussion here.
Do we have any other topics?
Seems now.
Okay, let's see where we are.
**Neil Yashinsky** 10:16 Yeah, just one last question, like, on a top level for the overall stability effort on the board, remind me, QCon is, like, in, is it 3 weeks? Is that right?
To me.
**Liudmila Molkova** 10:28 It's more like 2 weeks, maybe 2 and a half.
**Neil Yashinsky** 10:31 Two and a half weeks, huh? Was there… was there any specific… I guess things we, or I can assist with to… Ensure… You know, we're… we're achieving all the, Keith, I'm just bringing up the board myself, I wasn't sure if there was… if it was… if it was, you know, forgive me if it's obvious, but it looked like there was a lot of things on the board. But I'm never good at looking at the right board, so I probably could be seeing… or maybe there's a view in the thing, that would better point me in, like.
triage, efforts.
Further, for me or, you know, someone else like me who wants to continue to Contribute where they can.
In the remaining weeks?
**Liudmila Molkova** 11:22 Yeah, let's talk about it, Sweet.
Lost the project again.
**Neil Yashinsky** 11:48 Right there. Okay.
Mmm…
**Liudmila Molkova** 11:52 I think we should… Look here first.
And… I'm thinking where we are… let's just go through the different efforts and see where we are, and if every… what's… what's remaining for the stability.
So, for the parts… Think where we are, Aaron, what do we need, what's blocking?
**Aaron Abbott (Google LLC)** 12:20 Yeah, so most of these, I think, are not blocking.
I should probably… I could do a better job of making that obvious. Maybe I'll do that after the call?
But I think one of them to decide on is this first one.
which I think I discussed with you offline, Liudmila, and I filed another issue also, but… Right now, we… We kind of have to decide between these options. I think right now.
most Python… most of the Python code generates these, like.
Field with null values instead of removing it.
And I think my preference would be to treat Optionality and null is the same to just try to make everything a little bit easier.
But yeah, we could also go the strict, not required route, and then not allow nulls at all.
Which is a little harder to encode.
**Liudmila Molkova** 13:19 I support not differentiating nullability and requirement.
**Aaron Abbott (Google LLC)** 13:28 Okay, cool, I can, I can send a PR for that.
I think… That was pretty much the only… strict one. The other one was… Let me see… actually, it's probably an issue.
It's at the bottom, it's number… 619?
If you scroll down, it's in, like, a comment, a GitHub, yeah, that thing.
So this, this one's kind of similar, it's… I don't know if we need to do it before stability, unless we want to make the change, but the general idea is We have some fields that are required besides just the type discriminators.
And it's… it's kind of okay, but it… if you add new fields that are required, it's obviously not going to work for older producers. That's the kind of first issue.
And then we had this exact same thing happen with Finish Reasons, I think.
At least this is what my agent found with, PR363.
**Liudmila Molkova** 14:47 When it stopped being required.
**Aaron Abbott (Google LLC)** 14:50 Yes, yes.
So, like, generally what we do… I posted a couple links here, some from the OpenAPI perspective, but, like, with Protobuff, which I have some experience in, we usually just avoid using required.
And it means that a lot of stuff on the wire is kind of, like.
can be null, and you have to add a lot of checking, but it makes it easier to evolve the API in the future, so… That's kind of my proposal here, is to make some of this stuff not required.
**Neil Yashinsky** 15:25 That approach makes sense to me.
**Aaron Abbott (Google LLC)** 15:28 Okay.
**Liudmila Molkova** 15:35 Yeah, I'm thinking… in the popular OpenAI API schemas, you would see some required things. It's common to put them there.
**Aaron Abbott (Google LLC)** 15:47 Yeah, I can… I can look at the OpenAPI… sorry, OpenAI API a little bit.
**Liudmila Molkova** 15:52 Oh, sorry, I meant of an API.
API schemas.
**Neil Yashinsky** 15:58 I have… what's funny is I knew what you were talking about, I feel like, maybe, even…
**Aaron Abbott (Google LLC)** 16:03 Yeah.
**Neil Yashinsky** 16:07 That's a good call, actually, great, great reference source.
**Aaron Abbott (Google LLC)** 16:16 Yep, so it's kind of, I think we could work with it either way, but this is just in the vein of, like, decisions we have to make before stability. I don't… I don't know if we even have to do something necessarily, but kind of for offline reading for folks, and maybe we can discuss it more next time.
**Liudmila Molkova** 16:36 Yeah, I think we need to make a call. Either… either way can work, but we will need to stick to it, whatever we decide.
Okay.
So it sounds like… These are the two friends. Lost it. Oh, that's 619.
And the… the 619 is probably the… bug, or a semantic issue, I don't know, or a structural…
**Aaron Abbott (Google LLC)** 17:17 Yeah, I actually have it there now that I'm looking. It's the last.
**Liudmila Molkova** 17:20 Oh, And you're seeing this, friends.
Oh, we're fixing it, right? Because you're…
**Aaron Abbott (Google LLC)** 17:35 Yeah.
**Liudmila Molkova** 17:36 Change.
**Aaron Abbott (Google LLC)** 17:37 It…
**Liudmila Molkova** 17:39 And this one…
**Aaron Abbott (Google LLC)** 17:41 We can close.
**Liudmila Molkova** 17:41 Weird.
Yeah.
So what they're saying is… These friends are raised by definition, and we will probably never expand the top level.
thing to carry more properties, would rather have more attributes.
On this fence than… Adding things into the series.
**Aaron Abbott (Google LLC)** 18:19 Yep.
**Liudmila Molkova** 18:51 Sorry.
Okay… And for this one… It's, like, a feature of work. It can be done later, as long as we allow extensibility.
**Aaron Abbott (Google LLC)** 19:25 Yep.
**Liudmila Molkova** 19:26 And you have a PR to do the same with the fill definitions as we… Or is something that we've done with the messages.
**Aaron Abbott (Google LLC)** 19:36 Yeah, that one, I… and I made the same change that you asked for on the first one. It's just stacked on top of the other PR we were looking at.
**Liudmila Molkova** 19:43 Oh, nice.
Oh, by the way, Trask, we… we would need another… approver… This one?
No.
**Aaron Abbott (Google LLC)** 19:58 I think it's…
**Liudmila Molkova** 19:59 This one.
No.
**Aaron Abbott (Google LLC)** 20:06 It's…
**Liudmila Molkova** 20:11 This friend, 584.
**Aaron Abbott (Google LLC)** 20:14 Yeah, that's the one.
**Liudmila Molkova** 20:23 Okay, back to the… This one.
Anything we would need to be done.
Around these issues.
Common server, same, it's feature work.
**Aaron Abbott (Google LLC)** 20:41 The one other thing that we discussed, Ludmila, I don't know if it's in any of these issues, but it was for the tool call, result.
**Liudmila Molkova** 20:50 Hmm.
**Aaron Abbott (Google LLC)** 20:51 We were considering introducing, like, a type discriminator on this one as well, so that, Like, there's always gonna be the need to return any.
But that makes it really difficult to type anything else, and using it, like, basically wrapping it so there's a type discriminator.
Makes it a little bit easier to do that. So, maybe this is another one that we should… Oh, there's a… there's a PR from somebody.
**Liudmila Molkova** 21:18 Oh no, it's just some mention.
**Aaron Abbott (Google LLC)** 21:20 Oh, okay, okay.
**Liudmila Molkova** 21:21 Oh. Oh, no, wait, yeah, there is a PR.
Wow.
**Aaron Abbott (Google LLC)** 21:38 Do you… I think Models PY might be…
**Liudmila Molkova** 21:51 This is the… discriminate.
Dary…
**Aaron Abbott (Google LLC)** 21:57 Yeah, I think… I think computing it.
**Liudmila Molkova** 22:00 But it does more.
**Aaron Abbott (Google LLC)** 22:05 If you scroll down, I'm assuming there's another… Union, that wraps it, yeah.
**Liudmila Molkova** 22:14 And this is a union… Meaning… It does one… is there… Wait, is there a discriminator?
Type literal.
**Aaron Abbott (Google LLC)** 22:33 That one's typed with literal value. Value.
**Liudmila Molkova** 22:39 And I think what you were suggesting is that There is no discriminator, it's just the property, either the array or an object.
**Aaron Abbott (Google LLC)** 22:49 Yeah, yeah, we were discussing that. I mean, I could kind of go either way, I think… they're the same thing, it's just ergonomics. This is consistent with what we have for the other ones, but it's, like, a bit clunky. I don't know if you have a strong Opinion on diverging.
**Liudmila Molkova** 23:05 I don't have a strong opinion, except for the… this friend, it's out of scope.
Would you mind giving it a review?
**Aaron Abbott (Google LLC)** 23:20 Oh yeah, absolutely.
**Liudmila Molkova** 23:22 Awesome.
**Neil Yashinsky** 23:25 Ludmila, I'm sorry, you said one part about your, your concern, or the… I thought you said, like, the issue, the… the… what you highlighted here. Do you mind, like, I… if I missed that? Like, what your, what's your, Highlighting or describing?
**Liudmila Molkova** 23:39 It's just not in scope of this PR. We can discuss it, but it's… it's not… It's a new feature for the type.
We didn't have it here, it's on this pen.
**Neil Yashinsky** 23:53 Yeah, yeah, great, thank you. Just for my education or whatever, people, other people's like, like, you… not that this is good or bad, but, like, it's out of scope, and we should just do it separately and not as part of this PR.
If I'm hearing you right.
**Liudmila Molkova** 24:06 Yeah, it's kind of bad, but it doesn't matter, it's just it shouldn't be in this PR.
**Neil Yashinsky** 24:12 From a process standpoint, right, the key… the key, thing to keep in mind, if you will, for people who are doing this or other things like this at home is, you know, that's, I think, what I'm trying to understand how to better operate within this context and, you know, respect the boundaries, and granted, that one I wasn't very familiar with to begin with. Thank you.
**Liudmila Molkova** 24:36 Cool. So Dan, what was the issue number? 604… 532. This is also something we should do.
Is it related to the…
**Aaron Abbott (Google LLC)** 25:20 How's Novo.
**Liudmila Molkova** 25:21 March?
**Aaron Abbott (Google LLC)** 25:22 The schema union.
That's a great question.
Oh, I think we put Finish Reason in the parts also, right?
Somewhere.
**Liudmila Molkova** 25:37 We're in… oh, we… but we deprecated it there.
**Aaron Abbott (Google LLC)** 25:41 Okay.
**Liudmila Molkova** 25:42 Maybe not.
**Aaron Abbott (Google LLC)** 25:44 Yeah, it's probably not needed.
**Liudmila Molkova** 25:50 Let's check.
Yeah, it's deprecated, so we… We don't have any back compat, we can… We can just remove it.
**Aaron Abbott (Google LLC)** 26:19 Yep.
**Liudmila Molkova** 26:23 Yeah.
**Aaron Abbott (Google LLC)** 26:24 And even if we do have by compatible, like, I think that's kind of what the required thing was… was saying, is we can remove fields, and it'll still validate with newer and older schemas.
**Liudmila Molkova** 26:38 I mean, yeah, but it would still flag if it sees something that's… well, the extra properties are allowed anyway.
**Aaron Abbott (Google LLC)** 26:46 Yep.
**Liudmila Molkova** 26:47 So, yeah. Okay.
I'm not going to close it, because I think it still has some merit for the attribute, it's just that, it's not related to parts.
Let's drop it here.
53 And I think there is a PR for this friend.
Anyway, I'll find it.
Okay, so it sounds like we have a few things here that need… Reviews or work.
And some of them will be closed.
It's the… but some of them are in progress.
**Aaron Abbott (Google LLC)** 28:02 Yeah, I'll make it clear, maybe I'll just split this into two sections and put those stability bloggers together.
And… If it's good with everybody, I can send PRs for them.
Although I'm also happy if somebody wants to send one, I can review.
**Liudmila Molkova** 28:21 I think we have… PR for one of them, right?
**Aaron Abbott (Google LLC)** 28:24 Yep.
heard.
the 6041.
**Liudmila Molkova** 28:40 Am I trying?
**Aaron Abbott (Google LLC)** 28:41 The PR is 604, it was for… Issue… 532.
**Liudmila Molkova** 28:51 Sure do.
Okay, we have it marked here, yeah.
Cool, yeah, please go ahead, send a PR for things we don't have yet, and I'll… Yeah.
We are at time.
We can talk more, or we can, call it, we'll meet on Wednesday.
Okay.
Let's call it.
See you on Wednesday. Or see you tomorrow.
**Trask Stalnaker (Microsoft Corporation)** 29:31 Yes, yes, I'll review that one PR, and then, yeah, for the part stuff, feel free, just, ping me after Ludmila.
looks at it, and I will look over them also.
**Aaron Abbott (Google LLC)** 29:45 Okay.
**Neil Yashinsky** 29:46 Thanks for your leadership, everyone, contributions here in and everyone. Have a good day.
**Trask Stalnaker (Microsoft Corporation)** 29:50 Are you…
**Liudmila Molkova** 29:50 Thank you. Bye.
**Don Branson (International Business Machines Corporation)** 29:51 Dude.
