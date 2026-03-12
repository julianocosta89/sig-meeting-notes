SIG: Go SIG
Date: 2025-12-18
Duration: 9 minutes
Zoom Recording URL: https://zoom.us/rec/share/-JEpNHRlqqCILh0vG-s-5ia-2UBflNn0TxEeA1Kr2l2zk2BdzCahgEuFK464WPI.TiCASkacNP79BAaj
============================================================

## Zoom Recording Transcript

**Bryan Boreham** 02:00 Hey there.
**Tyler Yahn** 02:01 Hey, how's it going, Brian?
**Bryan Boreham** 02:04 Okay.
**Tyler Yahn** 02:06 Yeah.
**Bryan Boreham** 02:07 just Trying to get a Prometheus release candidate out the door.
**Tyler Yahn** 02:12 Oh, nice. Last one of the year, or…
**Bryan Boreham** 02:15 Yeah.
**Tyler Yahn** 02:15 more.
**Bryan Boreham** 02:16 No, no, it's… it's every 6 weeks.
**Tyler Yahn** 02:20 Oh, okay, cool, yeah Yeah, that's exciting.
How much work is it for something like that?
**Bryan Boreham** 02:27 I've… been writing… well, most of today, basically. Which is… is… It shouldn't be that hard, but it, There was a few inconsistencies, you know, just to… to save you the…
**Tyler Yahn** 02:48 Yeah, yeah. I… yeah, releasing hotel is kind of the same. Sometimes it can take, I mean, Hotel Incip, you know, maybe an hour or two, and then sometimes it can take all day, maybe even to the next day if there's, like, conflicts or something like that, yeah.
So, I, yeah, I hear ya.
Hmm, I'm looking at, Slack. I'm not too sure if, the other maintainers are going to make it. I'm also looking at the agenda, and we don't have… I don't have anything, I don't, I don't see, David on, he sometimes has some things, But yeah, I mean, this could be a short, sweet meeting as well. But yeah, if y'all haven't yet, I think you have, yep, add to the attendees list, or if you have agenda items you wanted to talk about, go ahead and add them.
We can wait a little bit longer, and otherwise, yeah.
Can… can jump in.
I guess, I don't know, I think, Owen, you might have been here last week, but, Brian, I don't think you were. We're definitely… one of the things we talked about last meeting was, planning to plan, so next year, one of the first few meetings we have, I think our goal is to have, like, a little bit of a year start kickoff.
And I think I'd love to get, like, feedback, especially from folks that are maybe not maintainers, and more, contributors, or even better, like, if you know users, like, of OTEL, of, like, what they would like to see, and things that they want from the project.
So we can prioritize, I think, some of our goals, for the next year.
Obviously, I think all of us have our own pet projects that we want to, like, move forward, but I think having some voices, included would be great. So, yeah, just kind of a heads up, like, if you can, you know, over the break, dedicate 1% of your time to thinking about, like, what you would love to see in OTEL, I think that that'd be awesome. I think there's definitely some great things to work on still, so… Yeah, just kind of an announcement that we're looking to get some feedback at the beginning of the year. I'm probably posting Slack before the meeting as well. It may not be the first, because I don't know if everybody's going to be back, but yeah, hopefully at the start of the year we'll get something going.
**Bryan Boreham** 05:28 Now, will that… planning be… because it's something I kind of trip up on all the time, is, like.
It's a goal library, but actually it's owned by the collector.
Team.
And so is there, like, one plan across the various different teams, or… Three parts of it.
**Tyler Yahn** 05:47 the… the… the Go… this, like, the Go Sig?
**Bryan Boreham** 05:52 Yeah, so if, you know, if you sort of say to people, what are the things that you want in the hotel Go libraries? And so this is something I've tripped over myself, I want X, and the answer comes back, oh, well, the Go Sig doesn't own that.
**Tyler Yahn** 06:07 Oh, oh, I see what you're saying. So, like, one of the things is you want the collector, Yeah, I mean, we definitely don't have a lot of, ownership or any… like, we don't have any ownership of the collector stuff. Like, we have overlap, obviously, I think we can all contribute there, but.
**Bryan Boreham** 06:20 So my question is… so it sounds like you're saying there's going to be separate planning.
**Tyler Yahn** 06:25 Yeah, it definitely would be a separate plan. But I hear your point, though, because, like, one of the things is a lot of… you know, it's a little chicken and egg, so if you wanted a feature in the collector, sometimes they come back to you and say, like, well, that's impossible because the Go library doesn't support it, and then you come here and we're like, well, I don't know, the collector needs… so it's like, yeah, I hear you.
So maybe, like, yeah, like, I'm not saying, like… I want to hear that, even if it is, like, a collector-specific thing.
Because if it's entirely a collector thing and, like, that's all up to them, like, I think if that's something we can even communicate to them, or just talk with them about, but… if it's some sort of dependency cycle where the GoSig has something that needs to get done for the collector to actually enable something, like, we definitely want to hear about that, like, absolutely, and help move it across, because I think that there's, like.
There's definitely people like Alex Bowen and, others in the past, especially, that, like, work in both worlds fluently.
So, like, it may just be, like, getting that in front of their face and enabling them to actually make this happen. You know, I've definitely contributed to the collector as well in the past, so, like, it's not something that we can't help as well, but… Yeah, it definitely depends on, like, you know, if you're… if you're saying, like, I want to re-architect the entirety of the collector, like, there's… there's no way for this sake, but yeah.
**Bryan Boreham** 07:40 Or, I think maybe if you phrase it this way, like, like.
I mean, you said you want to hear from, like, end users, so we should say… Or we should take the position that if an end user asks for something, And… it happens that they've come the wrong side of the Ghostig collector boundary, then we sort that out.
**Tyler Yahn** 08:00 Yeah, yeah, exactly.
**Bryan Boreham** 08:02 They're a problem.
**Tyler Yahn** 08:03 Yeah, I agree. Yeah, and I'm happy as a maintainer here to, like, reach out. I'm not… I don't think I am any… but anyways, like, yeah, I know the people, so I, like, I think I'd love to hear the feedback here, and if I can express that to the collector SIG, I will do my best to, like, you know, get them to try to prioritize it. So I definitely don't want it to be, like, the user's problem. I'd love to… I'd love to hear the feedback regardless, and then we can try to sort that out, just like you said, yeah.
Okay.
Cool.
I see somebody added what I just said in the agenda, but otherwise, I don't see anything else in the agenda, so we could probably end the meeting early here. Yeah, I'm guessing everyone's probably also on break, so…
**Owen Williams (he/she)** 08:47 Short and sweet.
I'm sorry.
**Tyler Yahn** 08:50 Cool. Alright, everyone, good to see you, see you all in the next year. Yeah.
Bye.
**Bryan Boreham** 08:55 Yeah, they hold this one.
**Tyler Yahn** 08:57 Happy holidays, yeah.
