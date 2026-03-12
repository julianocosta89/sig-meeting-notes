SIG: System Sem Conv Stability WG
Date: 2025-08-07
Duration: 7 minutes
============================================================

## Zoom Recording Transcript

**Pablo Baeyens** 01:20 Hey!
**Roger Coll** 04:06 Like there won't be much people today.
**Pablo Baeyens** 04:10 Yeah, should we cancel? Or oh, you have a topic.
**Roger Coll** 04:16 Yeah, but it's super super small. It's just let's see if we can finally close this memory thing because it has been just open for a while.
And basically, I think that some of you already reviewed the Pr to change to the available etcetera. But Dimitri just mentioned, if we could do a little research on what other vendors we're doing.
I just shared. Well, basically the that in an gather that in an issue. And and put it here. Maybe I will share with him directly.
But basically, the the thing is that other vendors don't, or until now they did not use attributes.
so they didn't have. Let's say this requirement of of you know.
**Pablo Baeyens** 05:12 To add up to, you know.
**Roger Coll** 05:14 So we cannot compare with them, at least for what I have seen that are gelastic and new relic. So yeah, that is different in this case, but at the same time I think that what it would be more accurate is to remove the current free cuts buffer whatever to opt out and do not count, as let's say, as this assumption.
And let's say, instead of relying on the old used, the new used should be mem total minus available and just provide us as default the used and the new available. And I think that that would work, and also why I'm in favor of that is because it will be the same attributes for windows for Linux, for 3 vsd. Or something on whatever. It's just like a another higher abstraction layer, I would say.
and also why I think this is correct is because the let's say that the old used or the use that we are currently providing is is wrong. So it actually, it's like a legacy thing from the kernel that should not be used. So I think we are also in a good moment to to do breaking changes.
and that's it. Just just put it here to see if we can can move on. And and yeah.
let's see if other folks just saw the the issue as well.
**Pablo Baeyens** 06:56 Okay, I think I did not approve the original Pr. Although I am in favor of it. So I'm just going to approve it.
**Roger Coll** 07:10 Okay, thank you. And I think the mail also approve it. So I guess that it's on there nursing queue or something like that.
Yeah, I I will. Ping Dimitri, just for him to know. And and that's it. Thank you.
**Pablo Baeyens** 07:31 All right quick one today. Then.
**Roger Coll** 07:33 Yeah. Have a good rest of the week.
**Pablo Baeyens** 07:37 Yeah, likewise.
**Roger Coll** 07:39 Bye-bye.
**Pablo Baeyens** 07:39 See ya bye.
