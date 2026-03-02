SIG: Sampling SIG
Date: 2025-09-11
Duration: 30 minutes
Zoom Recording URL: https://zoom.us/rec/share/IKWwtzI0nwz44x2TChowGFq7lMkfTMy84D53QV4KM01pn2x3QzFVrXaLr4cn9KzE.UM--6b3fCfRYPmQM
============================================================

## Zoom Recording Transcript

**jmacdonald** 00:10 Hello. Good morning.
**Peter Findeisen** 00:13 Morning.
**jmacdonald** 00:16 Here we are. I have…
**Otmar Ertl (Dynatrace)** 00:18 notes.
**jmacdonald** 00:19 for us.
A… small update?
So, you may have seen from the notes, I posted a blog post draft, and I want help from you all.
So…
I, this was sort of encouraged by, by the technical committee, this was, like, encouraged by the people who know sampling,
Wanting to see a blog post so that we could advertise what we've finished.
And encourage all the people to get excited about it. So… So here we are. I…
time boxed this to a few hours, and then just did it, and I… and I didn't look back.
I've already gotten feedback telling me that it would be nice to have, you know, like.
some sort of more introductory text, and honestly, this is my own idea of a post, because,
this is the way I thought of telling a story. So I'm… here I'm telling a story of,
The point of sampling is that we can count things, and there's math here. It's not just selective filtering. A lot of the code in OTEL looks like selective filtering.
calling it sampling, right? So we want to be able to say, I saw this piece of data, I'm counting it. That's the whole thing.
So, I,
I explained what we'd done, and, you know, tried to introduce the term adjusted count.
I explained what will happen when we're done with our… getting our SDKs to implement our new standards.
And then I gave an example, which is, showing how we can retrofit
New sampling thresholds and randomness values onto old sampling systems to keep them, compliant with, or, you know, compatible with their past, but also count things.
So, I walked through a quick example of that.
And then I,
talked about, how we can begin to mix SDKs and collector samplers, and then I gave a little bit of a roadmap.
For me, the roadmap… this is my own opinion, but I think we've kind of talked about this a bit.
You know, the idea that, we're… we're looking at configuration.
We're looking at the tail sampling processor.
And, eventually, I think the big goal that… for me, the important part of this post is to, like, let the community know, let the world know, that we're focusing on…
A feedback-based sampling loop.
In the long run. That's where I'm focused, at least.
So just… just the idea that we will configure our SDKs, send sampled spans, and then reconfigure our SDKs to reduce the, you know, the noise or whatever. So that's my… my draft, and
I, of course, I put my name on it, but I would love this to be more like a sampling SIG announcement. You know, no names need to be on it, or all of our names could be on it.
And I just wanted to, and so… so Jurassi has given me a bunch of comments.
I think the first one is like, yeah, we need an intro to the intro, and I'm not very good at this, so…
I just let it sit for a few days. I thought I'd share it with you and ask for help, ask for feedback, ask for suggestions.
That we could post. And maybe this is not a good example. Maybe you have better examples or better frameworks for this post, but I put this out as a draft.
May I ask if anyone has read it or has thoughts?
**Carlos Alberto Cortez** 04:10 Yeah, I have some, not exactly feedback, but opinion,
I think what you're asking once is something that is appealing to people who are not part of OpenTelemetry.
And… this document, I like it a lot, it's very technical.
But… and based on his… what he wrote, probably this is a… for a different… Crew.
And I would like to keep, honestly.
Both of them, if possible, and somebody probably can help with the announcement, like, general announcement, the way he requested that.
Like, just, like, how users could use that, but at the same time, keep this one, which is very nice, and you can call it, like, deep dive into probabilistic sampling.
That's both, People implementing backends and, maintainers can breathe, you know.
**jmacdonald** 05:06 So I hear you as suggesting that this sounds like part two of a deep dive, and that there's part one, which is like, hi, we're OpenTelemetry, we do sampling, we're making progress.
**Carlos Alberto Cortez** 05:16 Yeah, correct, yeah.
And actually, I can volunteer to do the first part one, if nobody else wants to do that here.
I guess I have an idea of what Urasi wants based on the stuff that he himself writes, so I could probably do that.
**Yuanyuan Zhao** 05:36 What, BRL, let's speech?
**jmacdonald** 05:38 Yeah. Yeah.
**Yuanyuan Zhao** 05:39 Oh, okay. Yeah, so I just came back from a long vacation, so I may not have
definitely don't have the full context, so I'll just say something at a very high level. I think a roadmap is a great idea.
From my experience, I've seen…
customers struggle, they want to use hotel, but they don't, don't know what they can expect, from hotel. So that has been a repeating theme.
having a roadmap, gives them some clarity, and let them, make a committed decision. So I think that's…
Very good. I don't know the details of this. I'm definitely interested to read it. On the surface, when Josh was just showing, I saw something like coordinated sampling.
I don't know exactly what that means in this context, but I'm wondering whether it's, like, across different products, that kind of thing, right? Get all kinds of signals together.
**jmacdonald** 06:48 Yeah.
**Yuanyuan Zhao** 06:49 Aww.
I don't know, is… am I…
**jmacdonald** 06:52 Yeah, I may have used the wrong words. Okay, so I was… this is, like, the first… I see this as the first time in OTEL that we have a potential to,
do sampling in the head, send a span, do some more sampling, and actually get a meaningful, like, final weight. And to me, that was coordinated, meaning that, like, we have
we have cooperation between multiple parties doing the same type of sampling so that we can do multiple sampling stages. I would remove that word if you think… I just wanted to expose the idea that we see the future where SDKs and collectors both sample.
**Yuanyuan Zhao** 07:33 Okay.
**jmacdonald** 07:34 And we don't lose information.
**Yuanyuan Zhao** 07:37 Okay, so, that's fine. so this brings up another topic, right? Sampling is, we've so far been focused on, traces.
There are many different kind of things. I don't know, maybe it's already in your proposal, but is that something we should put on our radar? Because it's far more valuable if users could have
All the different kinds of signals together, right?
**jmacdonald** 08:08 So I think you're talking about, maybe larger ways to combine hotel signals.
**Yuanyuan Zhao** 08:14 I also… but I also agree… It's also sampling, because different… there are… sampling is happening everywhere, not just the traces, right? So, if we're looking at the sampling, what exactly
is our charter? Are we only going to look at traces? Are we going to look at something else, other projects as well? That, I think that's a question we… this is probably the time we think ourselves, and we also,
I, make our stance known to the community.
**jmacdonald** 08:48 Yeah.
That's a really nice point, Yuan Yuan. I, I did brief… one of the reasons I like this example that I put in the deep dive is that it… it uses the… the… the…
specifications we've written, but it also doesn't change its old sampling algorithm, and it's nice, I think, to show that you can take this explicit randomness value to encode a legacy hash value, and you can use this threshold to encode probability,
But, the… It also applies to logs, and so this probabilistic sampler processor that we've… that we have in the collector
is very compliant with OTEP 235, but it also has a code path for logging events that it can sample, and it has… and it's all the way off-spec. It has, like, a hash function over an attribute value that it configures.
And then you can hash the log record.
it knows about log records, have trace IDs some of the time, so it's, it's, approaching log sampling, at least, and I…
**Yuanyuan Zhao** 09:56 Yep.
**jmacdonald** 09:56 I'm afraid to go talking about log sampling
Without unraveling this, like, long thread, because…
I don't believe that… well, I have feelings about sampling log statements and how you do that, and until there's more structure, I'm not sure I'm going to want that. But, users will get the high-level idea. Of course, you're sampling your logs.
And this specification does work for log sampling, is another.
**Yuanyuan Zhao** 10:25 I think the mechanism definitely would work, right? It's… if the log's capturing certain kind of,
keys or IDs we use for submitting decisions, then it's naturally, well-fitting. So it sounds like, is this something that we don't want to.
Xiang at this point, and we also, don't want to,
We actually don't want to… we want to leave that topic untouched.
**jmacdonald** 10:59 I don't…
**Yuanyuan Zhao** 10:59 If we want to do something, definitely we are going to state, this is what I'm gonna do.
**jmacdonald** 11:04 Hmm.
**Yuanyuan Zhao** 11:05 when you don't want to do that, I mean, we could say it's not currently in scope, but we could also just leave that topic untouched.
So it sounds like you are leaning toward a letter, or… I'm sorry if I'm putting words in almost…
**jmacdonald** 11:19 I don't want to leave it untouched, but I don't know exactly what to say.
I also have a great long feeling about metrics sampling, and it's so far from affecting users… like, so far from having an impact on users, my ideas, that I don't feel like talking about them, like…
OTEL has SDKs that talk about metrics reservoir sampling, and talks about, like, how do you choose your exemplars? And that's a sampling task as well, but I don't feel there's benefit from investing in it, because without, you know, a much greater framework.
for working with that data, I'm not sure what benefit any user is ever gonna see.
So there's that type of feeling. I don't… I don't know how to make metrics get sampling in a way that's useful to users, but…
And of course, we now have profiles in OTEL, and that's, like, basically a sampling activity, so…
**Yuanyuan Zhao** 12:18 Yep.
**jmacdonald** 12:21 So I think… thank you for the… I think high-level point you've made is good, that we're… that we… we've always done sampling in the trace world, but it's not that we… but we know how it applies elsewhere, and we can, you know, we can imagine it moving into OTEL
as users wish. I don't know what users wish for when it comes to log sampling.
Actually, I think I do, but…
**Yuanyuan Zhao** 12:40 It's not probabilistic sampling often.
Okay.
It's chewy.
leave this as detailed discussion on the roadmap, or should we just…
They will work together on the roadmap discussion.
**jmacdonald** 12:56 I… I think it's an open question.
**Yuanyuan Zhao** 13:02 Okay.
And I think we can leave it alone.
**jmacdonald** 13:05 That's true.
**Yuanyuan Zhao** 13:05 PRs.
**jmacdonald** 13:06 Yeah, okay. Don't have to.
**Yuanyuan Zhao** 13:08 Resolve it now. Yeah, we don't have to resolve it now, just… but in general, I think it's a great idea.
**jmacdonald** 13:14 So, yeah.
**Yuanyuan Zhao** 13:17 Roadmap is a great idea.
**jmacdonald** 13:21 Okay, so yeah, I'm gonna start thinking about… I like both of your, you know, these pieces of feedback from both of you, Carlos and Yuan Yuan. I think,
I hadn't, you know, I… when Jurassi asked, I didn't know what to think, but now I see, like, roughly speaking, what we're saying is that, like, the whole point… the whole topic of sampling is underexposed right now.
And, many people don't… don't know what OpenTelemetry has to say about sampling. Sort of like a, hey, five years into OpenTelemetry, let's review what we have for sampling, because it's changed, and you might not remember, or something like that.
Anyone else have feelings or thoughts? I would… based on what we've just discussed, I would take my… my… I would go back to the…
my desk and think about it. What's a sort of better introductory post look like?
And I would be glad.
**Kent Quirk (he/him)** 14:19 I have one thought here.
that,
without having read this post in detail, one of the things that I feel like I keep hearing from customers is kind of a level of
What's the right word?
And the fear. The fear around sampling means… that… I'm… Losing important information.
You know, or vital information, and maybe even… you know, a lot of people get freaked out about sampling because they think they're…
That means that when they need to debug a particular problem, they're not going to have the data they need to solve it.
And… and…
you know, we have to… I think… I sort of feel like there should be some nod to that thing of, like, you are…
deliberately… Reducing your precision in order to reduce your volume.
And also, that statistically, you know, like…
There's a really good chance that if you're having a problem, it's happening more than once.
Excellent.
**Yuanyuan Zhao** 15:41 I have the same challenge talking with not just, I mean, not just customers, but also internally folks working on this kind of things as well. They got super nervous, oh, we might not see that. Which, statistically, if something… if you've never seen it again, you've missed it forever, it doesn't matter.
**Kent Quirk (he/him)** 16:01 It was a cosmic array!
**Yuanyuan Zhao** 16:03 It doesn't matter, yeah, but if it matters, it's gonna happen again, it's going to affect you repeatedly, you will have a chance to catch it. You will also have a chance to adjust, to catch it with a higher probability, but that is a challenge, we both have.
**Kent Quirk (he/him)** 16:19 And so that's why I feel like maybe, as part of the intro, a nod to that might actually be valuable.
**jmacdonald** 16:27 It's like the idea that if a thing happens once, it's just never… it's, like, not worth debugging, because…
It'll never happen again. The things that have happened once never happen again. Therefore.
You don't need to worry about losing them.
**Kent Quirk (he/him)** 16:44 Yeah.
**jmacdonald** 16:44 And if they're interesting, they will happen again, or whatever. If they're real, they'll happen again. That's a really good, memory… reminder, I think.
**Yuanyuan Zhao** 16:53 Yep.
**jmacdonald** 16:54 This is, this is great. This is what I wanted to talk about.
Okay, anyone else have thoughts? This is wonderful. I would be glad to synthesize and think about this for another week or two.
**Peter Findeisen** 17:06 Well, so, yes, again, I did not read this post yet.
**jmacdonald** 17:13 You guys shouldn't.
has said, I sometimes write things a little bit. But my impression, when quickly looking at it was that there is a significant part of the document.
**Peter Findeisen** 17:24 Devoted to the math behind it.
And I think this could be scaring some people.
I believe that a blog post, which is really introductory for what we did, should be a lightweight reading for our customers, and
Of course, we cannot ignore this part, but I think it…
It should be really, simplified, and perhaps
had some pointers to more advanced, considerations, so…
I believe that saying that we have 56 bits to represent the values, And, therefore.
the precision of threshold is defined by these 56 bits. It's sufficient.
Yep.
**jmacdonald** 18:21 Yeah.
Well, to your point, like, that is all worrying about the, like.
after I've collected my sample, I'm gonna have some… some errors involved, but… but the fear that people… that Kent and Yuan Yuan just described happens first, and I think is more of an obstacle. Like, the idea that you're going to lose the information, never mind being able to count it accurately. So yeah, that's a good point.
Okay.
Don't dwell on error.
rates. Okay, I liked all of your feedback.
Thank you.
what I propose to do with it is to sit on it and think, and maybe next Monday, I will try and do something with this, because, well, I want to. So,
Yeah, I'll take back… a look at these notes in a day or two, and, maybe work with that.
I'll make another proposal to you all.
I have another item in the agenda.
It is a…
Let's see if anyone's… okay, so I did… I gave some feedback to this fellow who had submitted, sort of, from outside the community, a change in the tail sampling processor. As you know, I've been trying to ramp up on tail sampling processor. I've met the owner or the maintainer of the code, I've gotten to know the code.
So when I saw this, they asked me to review it.
It is… Not what I… well…
We've already talked in this group about how there's a thing called a composite sampler rule in this tail sampling processor that lets you say 50% goes this way to this particular value, 25% goes to this other value, and the remainder goes to the rest. That's almost stratified sampling. This person
It's interesting that we just mentioned how there's the event that you only see once, and that the loss of the event that you only see once is, like, actually a really important problem for many people. So that's…
when I… when I…
If you read the title, you think you're gonna get stratified sampling. I don't see this as stratified sampling.
But if you read what he's doing.
whenever it is encountered for the first time within a sampling interval. He's really just trying to make sure that the first example of anything passes through, and then you start sampling.
So I gave feedback to say that.
I don't think we want this PR exactly the way it is, but it continues to remind me that users want tail sampling processors that do things.
So, I…
made some recommendations. One thing is, they're introducing new modes of, like, hashed, salt-based hashing. Like, we've already got that, we've already tried to remove that.
I want… I want to use… I want to see us using more of the…
OTOP235 sampling routines in this code. So,
So I suggested not using the hash salt approach. I don't like it.
And I…
**Kent Quirk (he/him)** 21:47 So let me… can I just toss something in?
**jmacdonald** 21:50 Sleep.
**Kent Quirk (he/him)** 21:51 reference purposes here. So, Honeycomb, the refinery that I maintain,
has a sampler called the EMA Dynamic Sampler. And what it does is you specify some key fields, and the sampler hashes the combination of those fields, and then stores counts for a time period
For those particular fields. And then, at the end of the time period, calculates how many it's seen of each of those particular hashes, and guarantees that you will see one of every unique hash in that time period, and then basically
Adjusts the sampling rate for each of the buckets, separately.
So that you can get, basically, you know, you'll get a lower percentage of the things that are most common and a higher percentage of the things that are less common. But always… but has that note that you gave of… the first time it's seen one is always… it's always going to guarantee that it appears.
So this may well be an attempt to try to back-solve for some of that same capability.
into the tail sampling processor.
**jmacdonald** 23:04 So you're trying to be a slider.
**Kent Quirk (he/him)** 23:06 model.
**jmacdonald** 23:06 the hotel.
**Yuanyuan Zhao** 23:07 Is that PR from someone from Honeycomb?
**Kent Quirk (he/him)** 23:11 No, no. Oh, okay, this is… I don't recognize… I don't…
**jmacdonald** 23:14 the author.
**Kent Quirk (he/him)** 23:16 I don't even…
**jmacdonald** 23:16 they're not an OTEL, like, frequent contributor.
So, they're from the outside, is what I… part of why I had to.
**Kent Quirk (he/him)** 23:23 But they may have gotten the idea by reading about Honeycomb's dynamic sampling, or something like that, or had experience with it. So, anyway, that… I wanted to give you the reference as to where this is coming from. It feels very similar, or maybe it's a case of parallel evolution, and they just thought of the same basic idea, so…
**jmacdonald** 23:40 Yeah.
**Yuanyuan Zhao** 23:41 Yeah, Datadog has… this sounds like something similar to what, Datadog calls a rare sampler.
**jmacdonald** 23:51 I'm sorry, what's it called.
**Yuanyuan Zhao** 23:52 Rare.
R-A-R-E.
**jmacdonald** 23:56 Rare.
**Yuanyuan Zhao** 23:57 Basically, some mechanism Because if you are applying a uniform sampling rate, you… Are about to miss.
The rare, kind of, events. Yeah. So, it has this capability of calculating some kind of signature.
To make sure if some signature hasn't seen for a while, then… and it sees that, it gets captured.
That… I don't know whether… so I didn't… it existed for a while, I wasn't involved. The feature today was off by default.
**jmacdonald** 24:44 I see. But users… but some users come looking for it.
Okay, well, this isn't…
**Yuanyuan Zhao** 24:49 Yeah, there's definitely a need.
**jmacdonald** 24:58 I think this is interesting, I wonder about… Yeah.
I'm gonna have to think about this.
But we know how to sample things that are rare and weren't selected probabilistically by a uniform sampler. We know how to drop the TH and so on. So this sounds like something we could do.
So then I'll say my big reaction to this PR is that the tail sampling processor needs
Much more before it gets this.
And I…
don't see this being especially helpful on moving us towards where I'd like us to be. Now I remind… now I'm reminded that
this, part one, where OTEL and we sample, really could use some text about what the tail sampling processor does and its roadmap. I want it to do reservoir sampling, I want it to do OTEP 235, and I want it to do, you know.
That sort of thing. Once it does those things, then I can imagine retrofitting on more, like what we've just talked about, this, like, making sure that everything rare passes through.
idea.
Does anyone else have anything to say about this? I'm at a high level.
**Kent Quirk (he/him)** 26:26 No, I think you're right, I think this… there's some…
More fundamental work that should probably happen first.
**jmacdonald** 26:32 Yeah.
I have… I learned… I don't know, I think I gave an update last time, Kent, you weren't here. I… I got to know a little bit more about the tail sampling processor and the politics of it. OMG, it's like…
**Kent Quirk (he/him)** 26:46 Oh, no, really?
**jmacdonald** 26:47 Yeah, it's, it's like, there are private interests kind of, like, attached to it, like, companies that are, like, built it and are using it, but aren't really using OTEL, and it's like…
I don't want to name names, but the point is that there's, like, the people who are maintainers aren't necessarily trying to make OTEL move forward. They're kind of, like, trying to use this piece of code. And so, like, what I want is not necessarily what they want, and what I want is more like, you know, let's start counting, basically. So,
There's gonna be some… a little bit of struggle there.
at one point, I was asked, wouldn't you like to just make a new component? And I think… I don't think that's helpful either. Like, I think the… like, users come in, and they see this thing, and they start to contribute. I think we should just make it better. So that's on my mind.
**Kent Quirk (he/him)** 27:35 I do think, though, actually, it's so… like…
This is the old… this is the old engineering thing, right? Like, is it so broken that you should actually just start over? This might be one of those cases where it is, like.
**jmacdonald** 27:52 Yeah.
**Kent Quirk (he/him)** 27:52 I got in there once and tried to get involved, and then realized that it was so far from what we needed that I just felt like, no, actually, we need to do this better separately, and then, you know, life happened that I never got around to it. So, anyway.
**jmacdonald** 28:08 That could be the answer. It still might be the answer. So I'm glad you said it.
**Kent Quirk (he/him)** 28:15 Like, architecturally, it's really…
in rough shape, in terms of being able to do, like, OTEP235 stuff. And so… I felt like…
**jmacdonald** 28:27 Yeah.
I kind of agree.
**Kent Quirk (he/him)** 28:29 in any combat-compatible way.
**jmacdonald** 28:31 At the same time, it does things that I can't do with an OTEP 250 rule-based sampler. The way it mixes drop rules with sample rules.
And it, it appears.
**Kent Quirk (he/him)** 28:41 Yeah, but it does so in a binary way, which is a problem.
And I'm sorry, I actually have a hard stop, I have to draw.
**jmacdonald** 28:48 Okay.
**Kent Quirk (he/him)** 28:48 So…
**jmacdonald** 28:49 We're gonna continue this conversation.
**Kent Quirk (he/him)** 28:50 Apologize.
**jmacdonald** 28:52 Thank you, Kent.
**Kent Quirk (he/him)** 28:52 Okay. See ya. Bye.
**jmacdonald** 28:54 Feelings were shared. Well, okay, everybody, that was great. I learned what I wanted to learn from that. I knew Ken had that feeling, and I knew he… anyway.
I… I will resolve to do nothing about tail sampling processor in the next month, anyway, but I will come back to these blog posts, and making our roadmap, and sharing it with you, and talking about it with you all again. So I propose we end the meeting. Thank you all, as usual.
**Carlos Alberto Cortez** 29:22 Josh, just a second. Sure, Carlos. There's a PR that I pasted in the chat that I saw somewhere regarding…
sampling process, or, I suggest we take a look offline, with just a reminder.
**jmacdonald** 29:37 Yes.
Okay, this is from Sean Porter. He's at least the maintainer, so he's doing what he wants. I will help him. Thank you.
**Carlos Alberto Cortez** 29:46 Perfect.
**jmacdonald** 29:47 Yeah, alright. Thanks, Carlos. Yeah, I'm becoming a reviewer for this code either way, and I'll see you next time.
**Peter Findeisen** 29:56 Thank you, bye.
**jmacdonald** 29:57 Thanks, Al.
**Otmar Ertl (Dynatrace)** 29:58 Thank you, bud.
**Carlos Alberto Cortez** 29:59 No, no.
