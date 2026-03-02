SIG: C/C++ SIG
Date: 2025-09-17
Duration: 9 minutes
============================================================

## Zoom Recording Transcript

**Nikhil Bhatia** 00:25 Oh, yeah, son.
**Ehsan** 00:28 Hi.
I'm just checking the Slack channel… It seems nobody will join.
So, from maintainers, it's only me. Do you have any topics to discuss?
**Nikhil Bhatia** 00:50 Yeah, actually, I had my PR, so I wanted to discuss a few things.
Regarding it. So, can I share my screen?
**Ehsan** 01:00 Yeah, sure.
**Nikhil Bhatia** 01:01 Yep.
So, yeah, I think you're able to see my screen, right?
**Ehsan** 01:16 Yep.
**Nikhil Bhatia** 01:17 Yeah, so…
This, this issue was for, custom hash and equality for attribute processor in the unordered map.
So… What was happening before was,
That, we had to use, extra, copy, so, so we needed to optimize it for zero copy.
So, I, implemented a custom hash and equality, but, heterogeneous lookups.
are only present for versions after and C++20, so it is for C++20 and after.
But, so for before, what I did was, if… if the version is before C++20, I just use… I just materialized with std string.
Hello.
I left also a comment regarding it.
So, Molly, this was my primary note.
**Ehsan** 02:29 And what is wrong with the CI?
**Nikhil Bhatia** 02:33 Yeah, I think, I'm not sure why this… why these two tests are failing.
**Ehsan** 02:53 I have to check the… The main branch, let me see if we have…
It seems it's only on your brand.
this year…
**Nikhil Bhatia** 04:19 Oh, then I need to check it out once.
I… I hope you understood what I was trying to say here.
**Ehsan** 04:52 Failed.
**Ehsan** 05:00 So it's… I got disconnected.
Do you hear Mini?
Yeah, I hear you.
So… I was saying that,
And normally, once your CI is cleared.
Maintainers and approvers will just review.
**Nikhil Bhatia** 05:25 Carol, look into it.
And I…
**Ehsan** 05:29 Do you have questions you could either ask in your PR, or…
In the Slack, your Slack channel, Slack channel.
**Nikhil Bhatia** 05:39 Oh, yeah. Okay, and I also had,
Another issue which I was interested in working on.
In this issue, actually I was interested to work on, and I added a comment.
**Ehsan** 06:08 Mark didn't reply, no?
I, I could ping him on Slack. He, he seems in another meeting.
**Nikhil Bhatia** 06:24 Oh.
**Ehsan** 06:24 Okay, I'll ask him to reply on…
Not sure if he's working on this issue himself. The issue number is 22085.
If I could find him in the snake.
20, 85…
The issue number is 2085, right?
**Nikhil Bhatia** 07:59 Yep.
**Ehsan** 08:26 I… I guess it should be okay, because he did not assign it to himself, so…
Should be okay. They'll just… Pink him on his leg.
**Nikhil Bhatia** 08:41 Yeah, I'll try to…
**Ehsan** 08:44 Then… He would probably assign it to you.
**Nikhil Bhatia** 08:49 Boom.
**Ehsan** 08:53 Dane, thanks for your contribution.
**Nikhil Bhatia** 08:56 Thank you, thank you for your support, Ahsan.
**Ehsan** 09:05 Yeah, and feel free to ping us once your PR is ready.
**Nikhil Bhatia** 09:09 Yep.
**Ehsan** 09:10 And… we will review that.
**Nikhil Bhatia** 09:15 Yeah.
**Ehsan** 09:19 If you have no other topics to discuss, I think we could close the… close the call, because nobody will join, everybody has conflicts.
**Nikhil Bhatia** 09:29 Yeah, I think I'm, done with my topics, so…
**Ehsan** 09:33 Alright, thank you very much, and have a nice rest of the day.
**Nikhil Bhatia** 09:38 Thank you so much, Ahsan. Have a nice day.
**Ehsan** 09:41 Thank you. Bye.
