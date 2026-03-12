SIG: OpenTelemetry C/C++ SIG
Date: 2025-06-30
Duration: 25 minutes
============================================================

## Zoom Recording Transcript

**Doug Barker** 00:13 Hey, Mark.
**Marc Alff [MySQL]** 00:15 Hi doug.
**Doug Barker** 00:17 How's it going.
**Marc Alff [MySQL]** 00:19 It's very hard to you, is it?
Oh, yeah.
**Doug Barker** 00:24 What's the temperature?
**Marc Alff [MySQL]** 00:26 It was like something like 44 Celsius today.
**Doug Barker** 00:30 Holy smokes. Yeah, that's like in the Territory. They start warning people to not go outside or not spend too much time outside.
**Marc Alff [MySQL]** 00:37 Exactly.
**Doug Barker** 00:39 Yeah.
see where we're at here.
**Marc Alff [MySQL]** 00:49 I'm sorry I'm still used to Celsius.
**Doug Barker** 01:01 Yeah, here. It's only 74°F. So.
**Marc Alff [MySQL]** 01:05 Okay. Not too bad.
**Doug Barker** 01:07 It's in Denver, Colorado.
**Marc Alff [MySQL]** 01:10 Oh, you are in Denver!
**Doug Barker** 01:12 Yep.
**Marc Alff [MySQL]** 01:13 Oh!
**Doug Barker** 01:14 They're actually in in golden. So a little bit outside of the city.
**Marc Alff [MySQL]** 01:18 Yeah. I lived there for 13 years.
**Doug Barker** 01:22 Did you? Oh, wow!
It's right.
What part.
**Marc Alff [MySQL]** 01:27 Aurora.
**Doug Barker** 01:29 Okay, yeah, did you, did you like the area living in Colorado?
**Marc Alff [MySQL]** 01:36 Yes, yes, especially a basin.
**Doug Barker** 01:39 Yeah.
**Marc Alff [MySQL]** 01:51 Do you see my screen? Okay.
**Doug Barker** 01:53 Yeah.
**Marc Alff [MySQL]** 02:14 Well, I guess we can start on the when we're selling tidy Pr's. Then if you if you want yeah, sure, while waiting for the others.
Let's see.
So yeah, thanks for the looking up to approve this one.
And the next one. There is one thing that I think is strange is that you you you change a few files.
but even then the number of warnings is not going down.
So what's.
**Doug Barker** 02:51 Yeah, I noticed that, too. I made a comment. So I went in to fix the slicing warning. And I'm using visual studio code with the claim d extension which runs claim tidy, I think, in a different way.
**Marc Alff [MySQL]** 03:05 Okay.
**Doug Barker** 03:06 But it's also using the latest version. So I'm not sure exactly why there's a difference. But these are legitimate warnings. So I think we should.
**Marc Alff [MySQL]** 03:13 Okay.
**Doug Barker** 03:14 But yeah, I I don't know yet why, there's a difference.
**Marc Alff [MySQL]** 03:21 Would it be because of the config file used.
**Doug Barker** 03:27 I don't think so, because my visual studio code in that extension should be reading the exact same file.
**Marc Alff [MySQL]** 03:34 Okay.
**Doug Barker** 03:35 So I know that with each new version of claim tidy, they add checks, and then they add options, you know, to the various checks and improve things so it could be like what we saw with include what you use. We just need to upgrade.
But I also don't know if that will explain it, because the visual studio code extension runs it in a completely different way, runs these checks in a different way than what the C make clean, tidy integration does. So I'm I'm not sure yet.
**Marc Alff [MySQL]** 04:06 Well, in any case, as long as it's it is legitimate warning and fixes. Of course we can take it.
**Doug Barker** 04:13 Yeah, yeah, they're they're legitimate. Some of them are good because there's like base classes that don't have virtual destructors. You know, we need to, we need to fix that. So.
**Marc Alff [MySQL]** 04:32 Interesting.
So for for history, this list was just made up while trying to integrate sanctuary within ci.
But it has never been discussed in depth. So oh, it's also likely that so currently well, we're just well, you are removing most of the warnings we're trying to code. And when the dust settles, and then we can see a bit more clearly.
It could be that some of those warnings do not make sense, or do not make sense to be fixed, so we may as well just review this list at some point.
**Doug Barker** 05:12 Yeah, that sounds good. I I do have some suggested changes for this one. I think the 1 1 of them were disabling the check on initialized variables. And in my past, like I've I've run into so many production bugs that are caused by uninitialized absolutely turn- turn that one on. And then there's also a cert one that just I think for like you know, security and and c plus plus safety that we should turn on that whole category and then potentially the modernize although I think that will probably come in whenever we're ready to switch to C plus plus 17.
**Marc Alff [MySQL]** 05:51 Okay, sounds good.
So yeah, what I'm saying is, don't take this list as things that we absolutely have to meet. We may change that list as well if it makes sense.
I was hoping for a little, Tom to to join, because voice this pl where I looked at it. Owen looked at it also. But it's still touching some windows.
Things?
Yes.
So this Pr is touching the way the windows build works with Vc package. So I was hoping for Editor Tom to actually take a look at that.
to just to double check that it's okay.
This is why I have not merged it yet. I'm waiting, waiting on them.
**Doug Barker** 06:54 Yeah, that makes sense. I was thinking of after this meeting. If if Tom doesn't reply, I'll just ping Lillette and ask for his feedback directly and hopefully, hopefully even respond. I think the alternative is, if we don't remove that, then we should add tests for it. But I really hope that we don't go in that direction, because what it's doing now is highly unusual for a project.
**Marc Alff [MySQL]** 07:19 Yeah, I agree.
By the way, thanks for your reviews on the previous configuration things. So I've added more than So this is the overall. Pr had something like 191 files touched.
So, as you can see, it's it's decreasing in size.
because some of the files have been has been merged yet, and with the latest change that I have in the 3 new prs, basically that should take care of this.
those header files. All the configuration header files, then, should be should be reviewed once, once the once the 3 new prs are are merged.
so the next step will be actually to see some code no more, only declaration, but actually to see some good using that.
**Doug Barker** 08:36 Sweet sounds good. I took a brief look at some of these files in advance. Do you want me to make some comments in them, or just wait until you submit them, because I noticed a few things like some of the the style guide can still be updated. And I think it might have been the Prometheus.
**Marc Alff [MySQL]** 08:51 Up to you. I don't mind. I can.
I can fix them ahead of time as well, because typically what I do. I fix this Pr. 1st to make sure it breeds all the way, with no no, include what you use, no. Sent any warnings, and then I copy and paste the file, once it is clean in the in the Pr for review.
**Doug Barker** 09:13 Okay.
**Marc Alff [MySQL]** 09:14 So, yeah, if you have comments ahead of time, I can, I can look at them.
So yeah, so this one. So yeah, let's look!
Okay. Oh, someone joined.
Hi, Tom.
**Tom Tan** 09:43 Hi, mark.
**Doug Barker** 09:45 Hey? Don!
**Tom Tan** 09:46 Hi, Doug, yeah.
Apologize for being late.
**Marc Alff [MySQL]** 09:52 That's fine. Do you know, if that is joining as well.
**Tom Tan** 09:55 Let me check. I think maybe he is busy on something else. Let me check.
**Marc Alff [MySQL]** 10:01 Okay.
so Tom.
**Tom Tan** 10:53 Yeah, yeah.
**Marc Alff [MySQL]** 10:54 Yes, So in all the pr that we have there is one which is touching C make.
and it is doing some cleanup in a lot of places, and one of that voice which is affected is the our windows and Vc. Packages used in in the make file.
So I reviewed it. I'm okay with it, or went took a look as well.
But the only thing which is remaining for this one is, if you are ready to take a look specifically at the Vc package part to make sure that it's it's all okay there.
And we we need that to to have so that you can. You can double check that before merging.
**Tom Tan** 11:42 Okay, I'll reply this this comment.
**Marc Alff [MySQL]** 11:46 Okay, thanks.
Okay. So looking at over pls that we just discussed with Doug. It. It's okay. And okay to merge.
Those are the new things I'm sending for review for the file configuration. So if you have some time, please take a look.
I'm glad that the the review overall, for for the Yaml file is progressing because it's The code has been waiting there for for a while. So it's good to have this moving ceiling tidy another part as well already to to be merged.
This one from A went at some comments on that which have been addressed.
so we requested some change earlier, and this has been has been fixed. Now.
so this is okay to merge as well. So I will do that after the meeting this one as we discussed. So there is just the Vc. Package part to look at.
and everything else is pretty much old.
Oh, Tom. So this Pr. For testing with stl.
can you clarify if it's still needed, or close it? If it's not.
**Tom Tan** 13:18 Think we still need it, and I just haven't got time, I think, to to make it and work.
**Marc Alff [MySQL]** 13:29 Okay, sounds good.
And this one, I don't think we have seen any any changes there.
Let me double check.
Yeah. So it looks like the poster is not not around anymore. But we, we need to see what we.
what we do with this pr, whether we merge ourselves and take the code, or let's see.
And the last part from related, I'm guessing.
you didn't have time to make some changes, and this is the overall coughing. Pr, so it's a I am keep. It's progressing because I'm keeping that up to date with all the mergers. But, as explained earlier, all the things to review are just here.
Any pr, you want to discuss in general?
Because I think we've maybe I think we covered it. But maybe I missed something.
**Tom Tan** 14:48 No! From my side.
**Marc Alff [MySQL]** 14:49 Okay, do anything.
**Doug Barker** 14:52 No no.
**Marc Alff [MySQL]** 14:54 In our call.
As far as new issues I just created one for the for the release.
So feel free to add a comment there, if you want some. If you need some specific Pr to be merged by the as part of our treaties, and the only thing which is remaining is But report about the formative exporter the complaint there was that Timestamps could be set, and now they can no longer be set, and I have some trouble to to see what respect says about it, and if we should or should not add over user to set Timestamps do you know who knows what part of the code bests we? We had other contributors earlier, with a lot of knowledge on Promitius? But we haven't seen them for a long time.
and I don't know the the probability specs well enough to decide for this.
for this type. Same thing.
**Tom Tan** 16:08 I also don't know the history. Yeah.
Could we check like the log gate log, or get some insights.
**Marc Alff [MySQL]** 16:16 Cool.
Okay, I will try to take a look. But I was wondering if someone knows the knows the exact story.
**Tom Tan** 16:29 Or Doc, you have some idea on this, or you wanna so, speaking.
**Doug Barker** 16:35 I I don't.
**Tom Tan** 16:38 Okay.
**Pranav Sharma** 16:41 I have.
Hey? Yeah, I can actually this question seems more like a behavior. Whether, should this be allowed or not, I actually have a person on my team who's who contributes upstream to Prometheus. Maybe I can ask them about what the behavior should be, as far as the code for Prometheus exporter in C, plus. Plus. I did some very minor change on C that code. But I I have lost context on it.
But I'll bring this issue to to their attention, and see what they have to say.
**Marc Alff [MySQL]** 17:12 Okay, thanks. That would be great.
**Tom Tan** 17:16 And later will join very soon.
**Marc Alff [MySQL]** 17:20 Okay?
Otherwise, I don't have any special items to discuss. I'm still hoping to get some time to do this at some point which is just to enable the flags by default.
Oh, so, time permitting. Expect some some Prs about this to come.
Oh, otherwise I don't have any specific issues to discuss. Do you have any any special topic.
**Tom Tan** 18:02 No, on my side.
**Marc Alff [MySQL]** 18:08 I don't have anything.
**Pranav Sharma** 18:13 Nothing from my side right now.
**Marc Alff [MySQL]** 18:15 Okay?
And so you know, you know, typically, I also look at over of our repositories to make sure that.
Well, I think the only thing I noticed is just a minor release on Weaver, which is the tool used to generate semantic conventions.
So I don't think we need to release semantic conventions again, because the change there seems minor.
But this is just to be aware of it.
As mentioned earlier, I will try to make a new release. Possibly this week.
for open telemetry. Cvp.
**Tom Tan** 19:11 So, as we discussed before. Maybe this will be the last weekend or last release during the summer. Maybe next one would be September. At that time.
**Marc Alff [MySQL]** 19:22 Well, most likely, because there is also summer vacation. So summer is typically quieter.
**Tom Tan** 19:28 Yeah.
okay.
**Marc Alff [MySQL]** 19:37 Alright! Alex!
**Lalit** 19:40 Hi! Everyone.
**Marc Alff [MySQL]** 19:42 Alright. So so, since you are late, we just decided that you need to fix all the remaining bugs.
**Lalit** 19:52 Very sorry about being late.
**Marc Alff [MySQL]** 19:59 Yes, as we discussed with Tom, there is one pr that needs one of you to to take a look. This which is this one?
It's some cleanup in in C make that affects some things with Vc package.
So everything is reviewed. But it's just to double check this area. If you could.
**Lalit** 20:27 Sure.
**Marc Alff [MySQL]** 20:36 So I need to do any anything to you want to discuss in issues Pr also in general.
**Lalit** 20:45 No, not really.
**Marc Alff [MySQL]** 20:47 Because, yeah, we have. We have been for release already. And it was actually, first, st this time.
**Lalit** 20:55 Okay.
**Marc Alff [MySQL]** 21:06 So to summarize on Pr's thanks for the previous reviews on file configuration. So there is more to come.
and thanks to Doug for all the synthetic cleanup.
So I will merge those 2 or emerge actually 3 prs. After the meeting this one from a went and and to sanctity, so the Prq should be cleaner after that.
And alit, yeah, I'm hoping to do a release this week for open imagery travel, organization.
Out of curiosity. Do you have any vacation plan for this summer?
**Lalit** 22:00 Not me as of now.
**Marc Alff [MySQL]** 22:09 So I will be high in July, but expect some very low attendance, if if at all, in August. After that.
**Tom Tan** 22:19 Or any vacation plan from your side, or mark.
**Marc Alff [MySQL]** 22:23 Yes!
**Tom Tan** 22:24 Maybe after that, at the end of this month. My plan.
Okay, how about you? Yeah.
**Marc Alff [MySQL]** 22:30 Yeah, I will be. I will be mostly offline in August.
**Tom Tan** 22:35 Okay.
Okay.
**Marc Alff [MySQL]** 22:45 Okay, well, unless anyone else has another topic. I guess we can make a quick meeting then.
So nothing else to discuss.
Response. Yeah.
okay, well, thanks everyone for joining and see you soon online, or see you next week. Then.
**Pranav Sharma** 23:19 You know.
**Lalit** 23:20 Oh, thank you!
**Doug Barker** 23:23 Everyone got it.
