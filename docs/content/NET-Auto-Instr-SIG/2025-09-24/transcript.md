SIG: .NET Auto-Instr SIG
Date: 2025-09-24
Duration: 16 minutes
Zoom Recording URL: https://zoom.us/rec/share/PBF3qMedhbaRcBow4g3cSUMN5wZbiPVeBoOtXlzrLgVydHSeIZxnl-gch2vB8xkk.C1HWRiCFWWnZp5o5
============================================================

## Zoom Recording Transcript

**Piotr Kiełkowicz** 01:04 Hey, Zuck.
**Zach Montoya** 01:06 Hello!
**Yevhenii Solomchenko** 01:07 Thanks.
**Zach Montoya** 01:08 How you guys doing?
**Piotr Kiełkowicz** 01:10 Yeah. Fine.
Thanks. How are you?
**Zach Montoya** 01:14 Good. Busy.
**Piotr Kiełkowicz** 01:17 Yeah.
**Zach Montoya** 01:18 It is the end of our quarter coming up, so I'm trying to finish some things.
**Piotr Kiełkowicz** 01:25 I think we have, kind of, a couple more weeks.
In Splunk, but… Yeah, it will be busy.
Do you know… do you know if Chris or Raj will join us, or… Okay?
**Zach Montoya** 02:32 I don't know.
**Piotr Kiełkowicz** 02:43 I'm clicking away.
Come on… I think we can start.
I've had that one topic, we have discussed a couple.
weeks ago, related to MacRes, because there is an announcement that macOS 13 runner will be… will reach end of life.
And there is a question if we should go with updating this to Mac OS 14 on x64, or just replacing by ARM64.
**Chris Ventura** 04:53 Yeah, in the end, I don't have a strong opinion about which one to do. I think it's just a question of time.
Because I think for switching to ARM, it might be just slightly more work.
To do, and it's just a question of availability.
**Piotr Kiełkowicz** 05:15 And… If we switch right now… We'll lose support for macOS 14 and 15.
on x64.
And you're still officially supported by, apple?
We can fully drop x64, Two years from now, probably.
**Chris Ventura** 05:46 I don't really think people are using it except on their development machines.
**Piotr Kiełkowicz** 05:52 Yeah, I agree.
**Chris Ventura** 05:55 And I also think, If people are doing it on their development machines, their support cycle is likely expiring.
I mean, I think I got mine… Right when the first ARM64 Mac came out.
and… I… I'm still using my x64 Mac.
But I… Don't use it for .NET stuff.
**Zach Montoya** 06:30 Yeah, I think at this point, I think a lot of the refreshes for Mac laptops have been ARM now. I think we're, like, what, 4th generation ARM?
**Chris Ventura** 06:39 I think so.
**Zach Montoya** 06:40 Like, M4, yeah.
So… That seems like it should be fine to switch over.
I'm happy to look into that work for, supporting ARM64, or, like, doing that switch to ARM64.
**Piotr Kiełkowicz** 07:13 Before brownouts.
**Zach Montoya** 07:17 Yep.
**Piotr Kiełkowicz** 07:19 Oops.
Hmm… And we have a couple pull requests.
Open it.
Mmm… I also have to, let's say, finish groundwork for… Configuration-based instrumentation.
It is still supporting methods up to 9.
parameters.
And for requirements which we have in Splunk, it should be fine.
If it will be well documented, we can extend it, later.
One user will really need it, and I can show you, kind of, some example how it can be configured.
Right now.
It is knockout section, and we are defining… this setup.
Let's say, attributes. Still, there is no support for… activity kind and static attributes, but it should be easy, V.
Dumb, but… It will increase size of this PR, and I would like to avoid this.
So, if you have time, please look into it and put some comments and approvals if you are fine with proceeding with this.
**Yevhenii Solomchenko** 09:07 I have a question about, return a type. You use only void and, integer and, tasks.
It works 24 hours.
Just a void and the int, or for…
**Piotr Kiełkowicz** 09:19 No, it is working basically in any kind of.
**Yevhenii Solomchenko** 09:23 Okay.
**Piotr Kiełkowicz** 09:24 Should work, at least, with any kind, but this listed here are kind of… important, because int represents, kind of.
Just… just a number, string is a presentation of the… Class and task is needed for the async method, so we are covering all cases.
**Yevhenii Solomchenko** 09:47 return a type string, as I see.
Isn't that fair?
**Piotr Kiełkowicz** 09:53 Yes, we're concerned.
**Yevhenii Solomchenko** 09:56 string.
**Piotr Kiełkowicz** 09:57 Yes.
You have also system-wide and other also, probably. I hope I do not make any…
**Chris Ventura** 10:08 mistakes. I think the Main special case, other than the ones that you're already testing with, would be ValueTask?
**Piotr Kiełkowicz** 10:21 Let's how that entities working?
Volume costs… Yes?
We have this.
**Chris Ventura** 10:36 Taka.
**Piotr Kiełkowicz** 10:39 Yeah, I think that's the type that has the most…
**Chris Ventura** 10:42 Caveats to it.
Or special situations.
**Piotr Kiełkowicz** 10:50 But I think it was working correctly for Aw.
Standard bytecode instrumentation.
In our code base, so it is just kind of a different way to configure exactly the same method, so…
**Chris Ventura** 11:05 Tim?
**Piotr Kiełkowicz** 11:06 No issues so far.
The next one is analog.
**Yevhenii Solomchenko** 11:25 I just checked that you didn't have a test for system string in the return type.
**Piotr Kiełkowicz** 11:32 So… In general, return type, if it is not task, or async task, or value task, whatever, these kind of methods, is fully ignored by our… code. It doesn't matter what kind of class it is.
**Yevhenii Solomchenko** 11:52 Okay.
**Piotr Kiełkowicz** 12:04 There were, kind of, some new comments 4 hours ago.
So, Zach, if you can, just look once more time, and I will also check it tomorrow, once again.
**Zach Montoya** 12:21 Yep.
**Piotr Kiełkowicz** 12:21 If there are, kind of.
harder or technical things to fix, I think we can just push changes and merge it, if you are fine with the technical solution.
**Zach Montoya** 12:33 Yeah, I think, I only had a couple of comments, so if he went in and applied some changes based on that feedback, then I assume it'll be good.
**Piotr Kiełkowicz** 12:52 Last week, I've merged the file-based configuration, and the initial PR, and It is still waiting for you to review, post-merge.
If you have any feedback, it would be great.
If not, you can read how to configure it in this PR.
And when this one is Merchive Guinea has a couple other PRs related to other settings, to extent, Coverage for the file-based configuration.
For now, only resources and resources are configured by the file base, and others are fall back into the environmental variable settings.
Hopefully, we'll be able to finish this work before the… release.
That's the goal, at least on our side.
I think Steve is on PTR this week.
Or we can skip this issue. There's a couple comments to fix it.
Bye. Bye, Steve.
And I think that's all.
new issues, all of them, I think, are related to… Most of them are related to Firebase configuration, and we have… Couple others… Let's call client is in progress.
And I will put it to the next version.
Hmm… I will respond in the offline.
And closing this one.
There is no discussions, and I think that's all what we have on our agenda for today.
Do you have any other topics?
**Chris Ventura** 16:02 The main topic I had was already discussed.
With the macOS brownout?
**Piotr Kiełkowicz** 16:18 So, thank you, see you next week!
**Zach Montoya** 16:21 Thanks. Thank you.
**Yevhenii Solomchenko** 16:23 Okay.
