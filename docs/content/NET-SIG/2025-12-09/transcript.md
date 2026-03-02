SIG: .NET SIG
Date: 2025-12-09
Duration: 17 minutes
Zoom Recording URL: https://zoom.us/rec/share/oKf3UtEDhgMlDKyLkKBHsdEDf2KDo3IAElU7-c14pzg1XEL5YqGPrDbPY501DqXi.ofZ6TaqIusbH-oE3
============================================================

## Zoom Recording Transcript

**Rajkumar Rangaraj** 01:38 Hello, Martin.
**Martin Costello** 01:40 Hey Raj, how's it going?
**Rajkumar Rangaraj** 01:42 Yeah, it's going good for me. How's it going for you?
**Martin Costello** 01:45 Could be better. I've picked up a cold, which I've been trying to get over it after a week.
But hopefully I don't sound too much like Barry White.
**Alan West** 02:02 There you go.
**Martin Costello** 02:04 And…
**Rajkumar Rangaraj** 02:05 And…
we can get started. Just before going to agenda, I just want to check. I won't be there, next week onwards till the start of the, January next year.
So I may not be able to join the SIG. Just want to check, like, if anyone is available to drive the SIG, for the weeks, or should we…
Just call out saying, we will not be doing next 36.
**Martin Costello** 03:06 I'll be here next week, but I think there was an announcement in the community repo saying to cancel the meetings for the last two weeks of December, for the 6th.
**Alan West** 03:20 Oh, good deal. I didn't see that announcement, but yeah, I'll be around mostly.
So, anyways, yeah, I'll be here next week, so…
**Rajkumar Rangaraj** 03:29 Sure, then I'll let you drive around, like, next week. Okay.
Cool. Let me share my screen, and then…
Okay.
No, there is no agenda for today. Is there anything… That people want to discuss.
**Alan West** 04:05 Yeah, I haven't added it to the agenda yet, but
I opened a PR to get the ball rolling on cutting a release candidate for the SQL client instrumentation. I think a few of you saw that.
And…
I'm gonna move it out of draft, but I guess first I just wanted to ask…
Was there anything… is there any reason why we should hold? Is there anything outstanding?
that, Y'all think still needs to be addressed.
Before we, move forward with this. Specifically, Martin, I think I recall one issue that you'd pinged me on, you pinged me and Steve on, with respect to the, database, like, statement parsing stuff.
**Martin Costello** 05:00 Yeah, I think if it's just RC, I think that's fine.
But we should properly check it before stable.
**Alan West** 05:09 Okay, and…
**Martin Costello** 05:11 Steve said he'd pick it up and take a look at it in the next week or two, anyway.
**Alan West** 05:15 Oh, good deal, okay, great, so you've talked with him.
I wasn't super clear on… What the issue was.
You mind if we talk about that issue for just a second? I don't remember which number it is.
**Martin Costello** 05:29 Yeah, sure. I think it was mainly because I got into a conversation with Roji on the EF Core team about the EF Core instrumentation.
And… He'd misread the semantic conventions about… he thought he'd said you should never parse them.
And it's like, you shouldn't parse them in a specific scenario. But then that led to a com… for him, he left a comment in the other issue in EFCore repo, saying he saw some issues with…
ways the sanitation might not work correctly, so that's why I just flagged that up in the issue.
In… because, we had that conversation
A few weeks or months ago about,
How we need to make sure it was right if it wasn't opted.
So that it didn't accidentally leak information.
**Alan West** 06:22 Great.
The one thing on the issue that Caught my eye was…
the bracketed identifiers, and I suppose we don't have test cases for that. That's something I might be able to do.
Quick today, just to add some test cases.
For bracketed identifiers, because that's a… that's a T-SQL kind of syntax.
To ensure that… That's not a problem, but I think from the conversation that I saw you have.
with Rotate was that…
was about other things, like other… other dialects, like… like the back-ticked identifiers from MySQL and… and whatnot.
**Martin Costello** 07:10 Yeah, yeah, I think it was just the square brackets specifically for SQL Server.
That I thought was… because I didn't… I didn't… haven't yet gone and looked through all the test cases to see if it was already covered, but it was just, like, as he raised it and said.
Quote, I see some issues.
