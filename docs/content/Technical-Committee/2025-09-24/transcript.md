SIG: Technical Committee
Date: 2025-09-24
Duration: 11 minutes
Zoom Recording URL: https://zoom.us/rec/share/7xGBBFK1z3FH_NQ4j3gShK4FjLDVa1zbmXGLzBhtjLHCuYfIR5l48w4a_RX2VkNA.Rw7I7Vf5bzcooENG
============================================================

## Zoom Recording Transcript

**Josh Suereth** 01:25 Hey.
**Tigran Najaryan** 01:30 Hey, Josh, how are you?
**Josh Suereth** 01:32 Not bad, not bad.
So…
It's been fun lately.
**Tigran Najaryan** 01:48 Work or OpenTelemetry?
**Josh Suereth** 01:50 Bit of both, actually. So, I feel like…
Work-wise, just a lot of, lot of crazy stuff going on. OpenTelemetry, I feel like we have a lot of fun problems we're starting to dive into, and then we're redecorating our basement, so that's actually where the fun is coming in.
**Tigran Najaryan** 02:08 Okay.
**Josh Suereth** 02:09 Yeah, so, the family was painting, which means I have to do all the drywall repair, which I'm not particularly good at. But, you know, it's something.
**Tigran Najaryan** 02:20 You're brave, you're doing it on your own.
I usually bring contractors for that sort of stuff. I don't… Yeah.
**Josh Suereth** 02:29 Yeah. I…
Well, since we're waiting for folks, we had, we adopted kittens two years ago, right? And in our basement, there's a mudroom that is not finished, and then there's the finished room.
And somehow they got up into the ceiling.
And they got stuck, where they, like, didn't know how to get back out.
**Tigran Najaryan** 02:51 Yeah.
**Josh Suereth** 02:51 One of them fell into the wall.
Between the outside of the house and the basement, right?
**Tigran Najaryan** 03:00 third book.
**Josh Suereth** 03:01 So what I did was, and this was behind our TV,
So I pulled the TV stand out, and I cut a hole in the drywall.
For her to get out.
**Tigran Najaryan** 03:11 Yeah.
**Josh Suereth** 03:12 And then I just taped it on there as a cat flap, in case she fell in again.
As soon as you kick it out.
And, now she's… she's larger, she's no longer a kitten, so she can't get back there. But, I'm finding that I was really stupid when I made the cat flap, and repairing it, I have to put, like, a whole brace and cut out more, and it's been… it's like a whole hassle. So… but yeah, we had… we literally had a cat flap in our wall to protect our cat.
**Armin (Dynatrace)** 03:41 I sometimes see those videos online where people, like, cut into the wall, which wouldn't work in Europe, because it's made of brick, and then they have, like, birds behind the drywall, or squirrels, or…
or all animals of sorts, it's something that I can't really relate to, but…
But by having, like, a personal recommendation of yours, I now know that this seems to be a thing and not AI-generated.
**Josh Suereth** 04:10 It's absolutely a thing. And it was disturbing, because you're going into the wall with a knife, and, like, slicing the drywall, and the cat literally is trying to push her head out of the drywall while I was opening it.
**Armin (Dynatrace)** 04:24 a common theme in those… in those videos as well. That's why I somehow refuse to… to believe it to some extent.
**Josh Suereth** 04:32 If I hadn't been, like, panicking, I probably should have just videotaped this so you'd have a video, but anyway. That was, that was, like, 2 years ago. It was, it was rather exciting.
**Armin (Dynatrace)** 04:42 Maybe you have a cast, so it would be ideal. You know those saws that, when you have a broken arm, the saw that just penetrates the cast, because it's made of hard tissue, but it leaves your skin intact?
That would be the ideal rescue tool for those cases.
I guess they don't show the videos where the drywall knife attempt failed.
**Josh Suereth** 05:09 Yeah, well, luckily, I think that most animals are not that,
If you're careful with the knife, most animals get out of the way. So, yeah.
Anyway…
That's something I never thought of. Alright, should we… should we get started? Do we have… we have a quorum yet?
**Armin (Dynatrace)** 05:29 We've just reached it, yes.
Hi, Thomas.
**Josh Suereth** 05:33 Do we have any agenda topics? I did… I did want to ask…
I don't think this needs to be private, so I'll just ask,
So…
Oh, right, I'm the on-call this week. So basically, in security on-call, there were a few, GitHub issues that were opened, like, 2 weeks ago, 3 weeks ago, and what I'm wondering is, I know sometimes we start private chats on these.
Should we be including the latest on-call in the private chat, or should I be pinging the person from 2 weeks ago to say, like, hey, what's the status on this one?
**Liudmila Molkova** 06:22 So you mean the incident happened a couple of weeks ago, and there was a chat with the previous one call, and the question is whether you should be or the previous one.
**Josh Suereth** 06:31 Yes, I'm trying to understand what my responsibility and on-call is right now. There's, there's, I think two open advisories that I wanted to check up on.
that I think are making progress, but I, you know, I didn't have visibility at the time they were open, because I wasn't the current on-call.
They… there's a SIG responsible for them, and I just wanted to basically say.
check in and, you know, be like, hey, I'm the current on call, do you guys need anything? Any hard decisions here? That kind of stuff.
**Armin (Dynatrace)** 07:04 Yeah, ideally the person that was on duty, two weeks and one week ago would have left you with some notes.
Of what they did, if it's not reflected in GitHub. If they reached out via Slack DM or something, it would be ideal if they would have told you so, but maybe…
Maybe check with them, and they can just add you to the group DM if there is any.
**Josh Suereth** 07:25 Okay. But…
**Armin (Dynatrace)** 07:26 chances are that things are happening in GitHub first anyway.
**Tigran Najaryan** 07:32 At least that's what I usually do.
Yes, exactly, same here. Yeah, I just comment on GitHub, so it should be visible to you as well, right?
**Josh Suereth** 07:40 Okay, so I like this, of like, let's put it in GitHub, because I don't see anything in GitHub for the one that I was… that I'm mentioning. I put… I put it in TC Chat, the private TC Chat, if anyone has a chance to look at that. I'll ping… I don't remember who was on call two weeks ago, but I'll ping them, or…
last week was Carlos, right? I… maybe, Carlos, you and I can talk offline about, like, what… what the handoff should have been, or what… anything,
anything there, because it was… the one was open 3 weeks ago, the one was open 2 weeks ago. Those are the two that I was, taking a look at yesterday. So, okay.
Cool.
Let's keep up.
information.
GitHub.
Alright.
Should we move to the private topic, or does anyone else have something they want to discuss first?
**Liudmila Molkova** 08:43 Oh, I have one small topic.
So we are following up on the extended attributes, for all signals, right? And there was a previous part of the feedback that we should blog about it.
So, we are blogging about it, and the key question,
Do we want to write it before we actually start merging changes, and notify the,
Community about it, or should we first…
Would it be okay if we first start merging the changes, and then we… they are in development, the block will be out, we will have an issue tracker to collect the feedback. Collecting feedback will take probably quite a while anyway.
So I'm, wondering, if…
We'd rather start merging before the blog.
**Tigran Najaryan** 09:44 I don't think you should wait for the community feedback. It would take just too long for that, right?
So, just don't make one dependent on the other. Whenever you're ready, with whichever one, just… just go ahead. That's what I would suggest. Because we're not…
We're not anticipating that any feedback that we receive as a result of the blog post is going to radically change the approach, like.
Us completely stopping with continuing with that, right?
So, whatever corrections are necessary, we can do them as the feedback.
comes in.
**Josh Suereth** 10:26 I'd agree with this. I'd say, unless you think that the feedback would lead to you changing the direction significantly, so that you wouldn't continue with the work.
you should continue, because I think, likely, the feedback will be, how?
you accomplish this going forward? Like, that's what we would change, but not that you are making the change?
So, like, to re-echo what Tigran's saying, you know, unless you are anticipating not doing this based on feedback.
I think you can do them in parallel.
**Tigran Najaryan** 10:54 I think we're past that point already, right? It has been discussed to death already, so…
We're not changing that.
**Josh Suereth** 11:02 Yeah.
**Liudmila Molkova** 11:03 Cool, thank you.
**Josh Suereth** 11:09 Cool. Alright, let's, let's move on to the private topic, then. Sound good?
**Tigran Najaryan** 11:17 Yep.
**Josh Suereth** 11:18 Alright.
