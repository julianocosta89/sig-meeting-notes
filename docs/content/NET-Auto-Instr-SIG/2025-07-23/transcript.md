SIG: .NET Auto-Instr SIG
Date: 2025-07-23
Duration: 13 minutes
============================================================

## Zoom Recording Transcript

**Mateusz Łach** 00:16 Hello!
**Yevhenii Solomchenko** 00:17 Okay.
**Zach Montoya** 01:01 Hello!
**Piotr Kiełkowicz** 01:15 Hi, guys.
do you know, if we should wait for Chris or other guys suck.
**Zach Montoya** 02:17 I have no idea this might be the the corn we have today.
**Paulo Janotti** 03:10 Hello, folks!
**Piotr Kiełkowicz** 03:13 No problem.
Do you have a plan to drive Pablo meeting today?
**Paulo Janotti** 03:24 No, I'm gonna ask you to drive.
**Piotr Kiełkowicz** 03:32 Who the hell?
Let me share the screen in this case.
Oh, that's that!
**Paulo Janotti** 03:45 Yeah.
**Piotr Kiełkowicz** 03:45 I see why I understand why now.
**Paulo Janotti** 03:49 Yeah.
I. I have not been able to prioritize a lot of the work on.net directly myself, and I think for me. It's time to move to the Americas, the State. I will submit a Pr later, either today or tomorrow.
it's been great working with the group is just that I don't have more bandwidth to do stuff with the.net right now.
So I prefer to kind of go to the background.
I think, Zack was here since the beginning to increase. Chris is not here today. I'll send a message to him. Yeah. Just been great to work with this group. The Sig have been a pleasure during the last few years. But now it's time for me to move on, you know. So I will, maybe because there is a lot of people that ask me.net stuff. I may bring up things here post to slack or github but I will not be anymore. A maintainer of the project.
**Piotr Kiełkowicz** 05:15 Thank you, Pablo.
**Zach Montoya** 05:20 Yeah, it would be.
Oh, miss, working with you in the project.
**Paulo Janotti** 05:27 Thanks guys.
**Piotr Kiełkowicz** 05:35 Open prs, because we don't have any other non standard topics.
my SQL is failing on the downloading the new docker image. I think we can rerun tomorrow, or something, if it will be fixed or recreate. Pr with dependable 1, 3 for more topics to discuss. Raj created Pr to for the metrics out of the process collection. This is the second. Our second branch.
more or less looks good kind of, but there is ability of X unit only I found.
But if you have time, please please check it also.
Not. I wish any comments for selective sampling.
**Mateusz Łach** 06:45 No, I don't think so. This is this is follow up for the previous pr, so basically, the changes that were requested by, and also the the test that I wanted to write small modification to this.
it's I think this is described in A, in A, in a pure description. So if you could take a look, especially Fd. And Evgenias, you were requesting some changes there, so.
**efshaikh** 07:14 Sure I'll take a look. Thank you.
**Mateusz Łach** 07:16 Thank you.
**Piotr Kiełkowicz** 07:22 Rabbit and queue. We have request, internal in spank to add support for some old version.
It is working technically, it is breaking change. We are removing this set of public contract. And I think, instead of this, this, 4 passes to have cleaner codes.
Chris, approve this, and I'm also do not think that it is worth to keep ugly code or increase major version due to these changes. It should be fine. No cases, if if you are fine So also to regret if you can review and approve.
Other thing is pretty straightforward, because the methods are are pretty similar to the only change is, let's say.
Oh, this is the only change. Modern 6 old versions versus the old version.
Nothing, nothing. I and I have finally some time to back to configuration based instrumentation.
Chris was asking if it is working with tasks. It was not working. Now it is so, Zack. If you could double check this solution. It will be great.
So.
**Zach Montoya** 09:03 What's the the high level question or one of the main concerns that you just said.
**Piotr Kiełkowicz** 09:09 So the question was, if it is supporting Async methods.
**Zach Montoya** 09:15 Did you sell.
**Piotr Kiełkowicz** 09:16 Supporting it is done by on methods we have now 2 on method of end in each. Now integration class, and based on last changes, it is correctly resolving.
**Zach Montoya** 09:32 Gotcha. Okay.
**Piotr Kiełkowicz** 09:34 And still it is hard coded in.
The instrumented methods are technically hard coded in in our managed code, but in the future it will be passed from kind of file or something.
**Zach Montoya** 09:51 Okay, yeah, I'll review that.
**Piotr Kiełkowicz** 09:56 And that's all. If we're speaking about the pull requests interesting, no discussions and new issues.
I think we can skip it and wait until Russ moves back to this, I think our current solution is still cool enough. And oh, based on Chris.
Right? It is also fine.
This guy is still on vacation, so we can skip it for now, and methods not found.
I will add the style attributes here.
and we can close probably next week.
as you do not have any pro steps.
I think that's all ash.
I would check this one. Zack, do you have any updates on this or no?
**Zach Montoya** 12:12 I haven't tried to write a fix yet, but it the issue is pretty clear, so I have some next steps.
**Piotr Kiełkowicz** 12:19 Okay, great project, the board?
I doubt that we have any updates here.
that's all.
Do you have guys any other topics?
Thank you.
**Paulo Janotti** 13:14 Bye, everyone.
**Mateusz Łach** 13:15 See ya.
