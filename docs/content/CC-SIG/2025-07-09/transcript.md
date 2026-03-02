SIG: C/C++ SIG
Date: 2025-07-09
Duration: 45 minutes
============================================================

## Zoom Recording Transcript

**Doug Barker** 01:30 Hey! Son.
**Ehsan** 01:36 Hi.
**Doug Barker** 01:39 How are you doing.
**Ehsan** 01:44 Good! How are you?
**Doug Barker** 01:45 Pretty good.
hey? Tom!
**Tom Tan** 03:06 Hi, Doug, and you have time.
Hello!
**Lalit** 03:25 Hi! Tom! Hi! Everyone.
**Doug Barker** 03:29 He'll let.
**Tom Tan** 04:41 Added quite a few topics to today's
meeting agenda. Assume he will join this meeting.
**Doug Barker** 04:59 Looks like. Mark made a note saying that he's gonna be absent today on the agenda.
**Lalit** 05:32 Hey, Tom, would you like to drive the meeting? I mean, I think, Mark is not there today.
**Tom Tan** 05:41 Oh, okay, yeah.
Just meeting this morning.
**Lalit** 05:53 Sorry. Can you repeat, hey? Can you repeat, Tom? Sorry. It was not audible.
**Tom Tan** 06:02 I was asking, can can you please drive the meeting this morning?
**Lalit** 06:07 Okay, yeah, let let me share. I mean, last one week I have not been looking into the
to the Prs. But yeah, I think, probably let me open, share the screen and we can discuss.
Just just give me a sec turn on just a minute.
I think it's
okay.
oh, yeah, yeah, let me know if it's visible. If it's visible
oops.
hey? Can you guys see my screen?
Probably.
**Doug Barker** 07:27 Not yet.
**Lalit** 07:30 Okay? Yeah. So yeah, we can start the discussion. I see one
at least 1 1 point, which is written is, sem con, one dot 3, 5 dot O is
released. But it is broken.
Okay, so we we don't need to do anything. We just need to wait
for the release to be published correctly, or probably a new new patch release to come. And then probably we need to. We have to.
Oh, do the do. The corresponding release for Hotel c plus plus and then
I don't see any other points, any anything specific in the specs. And oh.
which we want to discuss here.
Yes, let me just see if
so it is.
Yeah.
Just opening the spec specification repo, just to see
anything which is going to change recently, or it's we are going to have some.
Oh, client, key password and certificate, revocation, configuration options.
Yeah, I think this would be a good
change, at least to add right now, right now, the certificates
which we configure there is no way to re to, at least, do a revocation for those certificates
in case they are expired, or anything. So I think probably that's from where it is coming on
longer limit.
Oh, and, Tom, I think there is one another.
I'm looking into this. Pr, that reminds me that we don't support log record processor on emit.
or do we do it? I'm not sure we don't support it right?
As of now.
Yeah.
So probably. So we that that was a new addition in the specs on emit.
And I think it was not correspondingly. We didn't add this support in
our, at least in Hotel Cpp. So probably we need to look into this. I'm just adding it
talk?
Okay?
Yeah. I think I don't see anything specifically which we want to discuss. Apart from this.
let's see anything closed recently.
No, I don't see anything.
There is a new change going to happen. Sorry, I'm just looking into this. There is a new.
I think.
Change any value. Rate.
Let me see.
Yeah, this.
Okay?
so basically, we may have to add the support for supporting the complex values in span attributes. Right now, span attributes can only be primitive types.
or it can be the list of primitive types. It cannot have a list of, say, heterogeneous list
or a more complex attributes
unlike log attributes. So probably this is something which is changed with this Pr getting merged.
And yeah, we may have to add the support
but this is this is right. Now, I think, Otep, so probably probably once it goes into the specs which we may have to look into this. I was just going through this pr.
that reminded me that at least in specs, we are going to have a change where any value
type can be a heterogeneous type for for span attributes.
Just going to add that.
Yeah, I think that's all I could see in specs and
you can go to the Prs, I mean, in in case there is
no other point specifically to discuss in the upstream
or no specific issues in the Prs which we want to discuss upfront. We can just go
with the list
looking into the Pr's Switch hotel proto to use fetch content.
This is already approved. Right?
**Doug Barker** 13:41 Yeah, I think I would approve that. So I just updated it to
merge in main. So I think it should be ready to merge. Once the passes.
**Lalit** 13:51 Okay, yeah.
Yeah. Thanks. I mean, I think looks good to me. I've not been reviewing a lot. Most of the C make C make Prs. But I think this in general looks good.
Oh.
well, I mean I I've most of the Cmake Pr. 30 normally.
I think as long as ovent is looking into that those
good to have another eye, but I think probably will have trust on his review, for for the C. Make.
Oh.
**Doug Barker** 14:30 So sounds good most of these Prs, and I've got a few more. I'll I'll complete it for all the dependencies. But really the goal with these Prs is to use the modern fetch content module.
and then that lets people bootstrap the open telemetry. Cpp build much easier, you know, by just fetching them all from Github, or from the sub modules.
**Lalit** 14:51 Yeah, that's I think that's could be supported, at least for all the external dependencies which we have.
**Doug Barker** 14:58 Sure.
**Lalit** 14:59 Oh, yeah, at C make script to find or fetch Microsoft. Gcl.
this is all this is also doing the fetch right.
**Doug Barker** 15:14 Yeah, same- same thing. It just makes it more formal putting file to find or fetch Microsoft. Gsl.
**Lalit** 15:22 No.
yeah, thanks.
Yeah. The configuration. Prs, you haven't seen that. But in case
I mean any anything specific that, like, you see anything
specific in these or normally, these are.
**Doug Barker** 15:44 No, it looks like Mark is filling out the test. That's what I was interested in. So I think that what he's doing is he's getting the main Pr, so 2, 5, 1, 8,
he's putting all the
and everything is building and running in that Pr, and then he's picking out pieces like files for these other prs, so the tests aren't even the codes, not even building in these other pr, so I just looked at the main pr.
okay, the tests are all passing and and cling tidy and include what you use as happy.
And then I just do a quick code review of of the smaller Prs, and then I've been approving them. But
yeah, I think Mark would would definitely appreciate if you have time to to take a look as well.
**Lalit** 16:25 Yeah, yeah, sure. Sure, I think. Let me spend some time. I think I'm
to have a look into that.
but in general, I think probably we all should have. These are these are.
I think, for the configuration feature I think, good to have. We all have an eye on that, I mean, though it is behind the feature flag.
But I think at one time we do need to
add it in the mainstream so definitely. I think we should have a look into that.
**Doug Barker** 16:55 Definitely, yeah.
**Lalit** 16:59 And thanks. Thanks for reviewing this, I think.
**Doug Barker** 17:05 Yeah, I'm looking forward to getting the feature in.
**Lalit** 17:08 Yeah, anything else. Probably it looks like caller.
Yeah, these all. Probably I was trying to use co-pilot.
Oh, but I think there are some more discussions which we have to do for co-pilot
before really you start using it.
And Mark has rightly put it on on blocking.
Yeah, this is also cooperate. Yeah.
**Doug Barker** 17:38 Interesting. Are you guys using it internally in in Microsoft? Yet.
**Lalit** 17:43 Yes, we do use it internally,
But having said that, I mean that was not really the reason to put it.
yeah, in the at least, in the open source. It's just that Github supports that, and
probably it's just got added, enabled with that. So
I mean by in general, I think I I definitely support it, I mean, at least for more of more routine tasks like up bumping the versions for proto or semantic conventions.
which which are more routine, can be easily this can be easily reviewed, and any issues can be caught. But yeah, I think it needs more wider discussion, not just in total CC plus, plus, but at the community level.
Oh, yeah, add bundle version of Utfa range to validate.
It's a draft. I'm not looking into that unless there is any comment here.
I don't see any comment apart from copilot.
Yeah.
this is this is approved right, I mean I don't see it got merged till now.
**Doug Barker** 19:10 The cling, Teddy one. There's 1 more con. A few comments for moment that I'm gonna reply to. So
I think we hold off on merging it to address Owen's comments, and Owen approves.
**Lalit** 19:24 Okay, yeah. Cool
from this is on draft so no update rate on this.
Hi, is Tom still there, or probably is.
I can't see him.
**Tom Tan** 19:48 Yeah. Just joined back. And
**Lalit** 19:53 I mean, there's no update right on this.
**Tom Tan** 19:55 Yeah. Yeah, no. Update on this one.
**Lalit** 19:57 Okay? Fine. Yeah. No problem. If this this was an action item on me to contact the original author of the Pr. But I think
I don't have any update as of now for both these.
So yeah.
And this was what we were talking about, right the main main Pr, where we are adding all the unit is.
**Doug Barker** 20:22 Yep.
**Lalit** 20:24 Okay.
yeah, yeah, I think, probably I'll
okay. If nothing else. Probably you can just have a look into the issues
support periodic exporting meta. Reader, config from environment variables? I'm not sure.
Okay, I was not aware if there is a okay, yeah. So I think.
**Tom Tan** 21:00 Landon. I can't see your screen. Oh, is it okay
screen sharing so just prime.
This is only from my side or.
**Lalit** 21:12 Oh, I'm sharing it right, I think.
And I thought, we all are. All others are able to see. I mean.
you guys can see, you can. Right? Okay.
**Doug Barker** 21:25 No, I can't. I can't see it either. I'm I'm just.
**Lalit** 21:28 Oh, my God!
Sorry! I thought you were able to see it, and
I'm sorry! Let me let me see, then
that's that's on me, I mean, I thought, I'm doing it.
Let me try it again.
Oh, my God, I
yeah, I'm doing it from my macbook, and I think it needs some permissions. Probably I didn't realize it.
Oh.
I have to. I won't be able to do that. It says that you have to quit the zoom and reopen it
for my permissions to get enabled.
Oh, but yeah, I mean, let let probably let me rejoin again. Just give me give me a sec.
**Tom Tan** 22:28 Okay.
Nope.
**Lalit** 23:45 Oh, hey! Is it visible now?
**Doug Barker** 23:52 Yes.
**Tom Tan** 23:53 I, yeah, I can see them. Now. Yeah.
**Lalit** 23:55 Oh, okay, sorry. I was taking from
my macbook, and somehow I didn't realize that I need to enable some permissions, and I missed out the
the warning it was showing so
sorry about that. I thought I was
going through all these specifications repo, and I thought I've been. I was able. I was. It was making sense. But yeah, sorry.
Yeah. So we I mean, I was kind of discussing the issues.
Oh.
support periodic exporting metric reader, config from environment variables. Yeah, we we need to support it.
The only thing is that environment variables are not. I mean, the supporting environment variable is not a mandatory as per the specs. So it's good to have feature. So I mean, if somebody want to add the support
you can ask them to do it.
**Tom Tan** 24:57 So market as like 1st good issue, this kind of.
**Lalit** 25:04 Yeah, you can do that.
And I think we'll we can add it as part of the. There is one issue, right? It's kind of pinned issue. Which welcome. Yeah.
I'll add it here also.
We'll do it afterwards. Here.
**Tom Tan** 25:30 Okay.
**Lalit** 25:32 Karen cannot shut down metric provider manually without a warning from a destructor.
Okay, yeah, I think that's shutdown can be invoked only once.
Hmm, interesting, I think, in the in the Destructor, we are calling the shutdown.
And okay.
yeah, that's a problem. So if somebody is explicitly calling a shutdown, and then we also call it in the district.
Yeah. So that warning would be there.
which is kind of okay. But if some
there is a concern. Then probably we can.
We can remove this warning. I mean, we don't need to really
put any warning because it's already shut down, so we can just remove it. I think that also should be okay.
Somebody makes sense to shut down a meter program manually, however, that they should also call Shut down it.
Yeah, I think that looks good. I think we don't need to.
If if you guys are okay, I think you can accept it right?
So.
**Tom Tan** 27:05 Yeah, I think interesting.
**Lalit** 27:08 Oh!
**Tom Tan** 27:09 A valid issue.
**Lalit** 27:11 Yeah, oops, and prepare this.
Hey? Was there any discussion on this release?
I'm not sure if last week we discussed anything.
**Tom Tan** 27:29 Yeah, I think we sort of discuss. Maybe we should do do a release, either, last week, maybe this week, and then
the next release movement will be like in December or so
due to maybe. Yeah. Vacation plan for the.
**Lalit** 27:49 Okay, so so so there's no release at least this week. I don't see.
Oh, I mean, unless unless because I thought, probably we are, I mean, we are targeting
the the config changes for this release or not, I mean, I don't know.
or if there is anything substantial which has been delivered.
**Tom Tan** 28:18 Yeah.
**Doug Barker** 28:20 We're talking with Mark. I don't know how many more Prs are needed until we get the
the full implementation end, but it might be quite a few.
**Lalit** 28:30 Yeah, that's right.
And.
**Tom Tan** 28:31 Every week.
Don't speak all over them with the release, but you need Mark to confirm.
**Lalit** 28:37 Okay, yeah. Probably. Probably, I think, let Mark decide when when he feel is the right time. I mean
or maybe in the next meeting. I think we can discuss.
These are 2 weeks old. I don't see. We need to discuss these.
Yeah, I don't see anything updated apart from these.
add support. For this was added by me, yeah.
input file corporation was already done by
Mark. Yeah, I think rest are the old ones.
So then there is, there is a, I think, point by mark.
Discuss the use of generative AI co-pilot concerned about the intellectual property for the repo concerned about license licensing
is the generated code compatible with license of Hotel Cpp. Easy, Cla for generated code.
So so I mean, the answer for all of them is
that open telemetry the general terms and condition in open telemetry somewhere they have a link that generative AI
should be used.
The Linux Foundation also has a terms and conditions somewhere where they they allow use of of generative. AI
easy cla is something which is being done.
So I think probably a decision once easy class, I mean.
once easy, Cla is enabled. That means that
the generated AI user that is, a co-pilot user
is able to raise a Prs which can be directly merged.
But yeah, this, this probably has to be discussed.
not not. It's not something specific to c plus plus repo. But it's more more generic
for the open telemetry. Gc. And Tc. To take care.
Oh.
hey, Tom, if you're talking, I think you are mute.
**Tom Tan** 30:51 Yeah, thanks. Thanks for for the reminder. I mean, as we don't have a Tc member in our meeting like, can we raise all like all these questions to like to the community and let the Tc member to answer for this.
And if we get a Yes, maybe.
and then we can enable the co-pilot thing.
**Lalit** 31:14 Yeah, I think that's that's what has happened. Mark has raised this concern with the Hotel Cpp licensing. Tc, member.
What's his name, I mean.
let me let me open that issue. Probably.
**Tom Tan** 31:31 Community.
**Lalit** 31:32 Question. Community. Yeah. Sorry.
I don't know where it is.
**Tom Tan** 31:45 Or maybe already closed that issue, because.
**Lalit** 31:48 Let's see.
**Tom Tan** 31:48 Yeah.
**Lalit** 31:55 Oh, I don't see.
Probably. Let's search on.
**Tom Tan** 32:01 It's a search call co-pilot, or.
**Lalit** 32:08 Yeah, this was the issue.
This is open.
Yeah. So I think this guy is somebody which is kind of our contact with our contact person for anything
which we want to raise. To gc, Otc.
Severin. So he's basically the OP. Open telemetry Cpp contact with.
we see. So Mark has raised, raised the concern with him, and he raised. He opened this issue.
Yeah.
**Tom Tan** 32:38 See, it's for their role back. I think maybe.
**Lalit** 32:40 Yes.
**Tom Tan** 32:41 Open and separate issue. Yeah.
I think the robot thing is, I think, the enable of the code agent in not agreed by all the maintenance. I think that currently there is no workflow or process defining this right hope. This will be addressed like, I think there's some comment from trust, right.
**Lalit** 33:04 Yeah.
**Tom Tan** 33:05 Yeah, there will be a new policy, maybe, to address this. And then we then how about we file
a separate issue to the, to these questions, I think Tc members or Gc. Will be in better position to answer the like. The copyright thing. The questions, yeah.
**Lalit** 33:24 Yeah, I think. Let let probably I'll say, let's let's use this
issue, and task is already said that he he's going to come back after discussing with Gc. On Wednesday. That's today.
And that discussion Will should should sort out all the issues regarding easy Cla and the policies whether it should be enabled anything issue related to licensing, and all those things.
**Tom Tan** 33:49 Okay.
**Lalit** 33:49 Should address it. Probably I think we can. We can ping him, maybe tomorrow, if we don't see any reply here.
Oh.
so I think. Let's see, let's use this as of now. Unless until we really need feel a need afterwards, since
for a separate one.
**Tom Tan** 34:08 Okay, that's awesome.
**Lalit** 34:09 I I understand this is for rollback. I understand this is for rollback, but I think, as of now, we can use this for discussion, and then see if any.
**Tom Tan** 34:15 Then, yeah, once there, there's a decision like it is okay. Maybe we should have revert the rollback like that.
I mean, re-enable it. And like.
**Lalit** 34:25 Yeah.
**Tom Tan** 34:26 Besides this question, or I'm I'm wondering, like, or Doc, do you have any other like concern or questions on? On enabling the the co-pilot for for repo.
**Doug Barker** 34:41 I looked into it briefly, and I'm not sure if approvers can interact with copilot. But maybe that's something that we can test. I I think it's just people who have
right access to the repository like, if you make a comment
like if it's a reviewing my Pr, and it makes a comment. I'm not sure I can
tell Copilot to do anything with that.
**Tom Tan** 35:03 You don't think
as based on the the play we did. I think if you can like, set the assign an issue, or to copilot. I think the agent will like see work on behalf of you, maybe good to have a try once we enable it.
**Lalit** 35:20 So so, Doug, like, I mean, you're saying that you you are not able to assign. I mean right now. Okay, right now, anyway.
**Doug Barker** 35:26 I don't know. I haven't tested it, but I just looked into it as you started assigning I was looking into copilot and how it works, and it I think I read that it only like if somebody adds a comment, saying, Copilot, do this, or whatever I think it only works. If you're if you have right access to the repository. But I could be wrong.
**Lalit** 35:47 Okay. Yeah.
**Tom Tan** 35:48 Yeah, so ideally, we won't enable everyone to can do this right
like even that Maintainer approval maybe can also see.
But I'm not sure whether that makes sense.
**Lalit** 36:02 Yeah, I think it should be right. I mean, anybody should be open, able to open a
or or.
**Tom Tan** 36:07 But if that requires right access to the repo, then October may
maybe. But for other users like open telemetry community users, I think. No.
But yeah. Good questions to to figure.
**Lalit** 36:23 Can you like, Tom? Can you check, probably. This open telemetry rush if you have an access to like, if any of the issues here.
**Tom Tan** 36:32 I can. Yeah, give it a try.
Okay, yeah, yeah. Yes.
**Lalit** 36:36 Yeah, anything, because because for this, I mean, I think I raised at least I was able to, because I'm the Maintainer in Rush, so I won't be able to do that.
But yeah, just see if any, if you can do it here. So that will. That will answer the question like.
**Tom Tan** 36:50 Yeah, yeah, that's a good.
I will give it to try and update back.
Oh, nice.
**Doug Barker** 36:56 The other concern it. It looked like it, didn't. It? Wasn't able to see the Ci output. Is that right? Because you were like me had a manual copy Ci logs for it to look at.
**Lalit** 37:10 Logs, I mean, I'm not sure if you're saying that like, if copilot can can see the Ci logs and iterate iterate over fixing them, or
sorry.
**Doug Barker** 37:24 That would be ideal. But what I was seeing with the test Pr, that you were interacting with it, you you had to tell.
**Lalit** 37:30 A year, a year.
**Doug Barker** 37:31 Failed. And here's the thing.
Yeah, yeah.
**Tom Tan** 37:34 Same as you can have.
**Lalit** 37:36 See? Ya.
yeah, it's yeah. It's not still up to there. I mean, I think it's that's that's the reason I found it found based on my experience using it in. I mean, I've been using it quite extensively in rust. So my experience is that it works very good for a routine task.
But but as the things get complicated, it's not able to handle it. Well.
and and yeah, definitely, it cannot really go through these Ci logs, any trade over till or everything is fixed.
We have to. We have to manually tell it as a comment what to do.
So yeah, it's still not there. and
I mean, as I said, that as of now, I think it's good to rely on it for
for more routine things which we can automate in terms of peers.
**Tom Tan** 38:26 But it is still evolving around, addressed later.
**Lalit** 38:32 Yeah, yeah, I I do use it like, at least in Vs code, I'm I'm not sure if if somebody has tried Vs code with copilot or Vs code with client
or Vs code with cloudy for code.
I I mean, these works really good to complete automate any, any new change in that helps to raise a Pr.
so so that way it works good, but at least on a github. It is not.
Oh, it! It's not still up to there.
So yeah, but yeah, all these are, I mean from Mark. All these are very concerned. And
I mean, even though I know the answers for
for some of them, but I think best. Best. Gc, and Tc. To come up with the answers, and they should
they should they? Yeah. And then then I think we should. We should see when, whether it should be enabled or not.
**Doug Barker** 39:33 So sounds good. I just posted the link to the
limitations that I found, and it says that it's limited to who can add, who can assign tasks to copilots only users with right access to the repository. So I think that's probably just the maintainers. I think.
**Lalit** 39:51 Only users with right access. Okay, yeah, that would be. Only maintainers here can trigger co-pilot to work interesting.
**Tom Tan** 39:58 But I think the cooper doesn't need to push change to the repair that's usually push the change to the
but.
**Doug Barker** 40:05 Talk, right.
**Lalit** 40:06 And then I don't know but but I think if it.
**Tom Tan** 40:10 We don't.
You're welcome in a report. Yeah, maybe.
**Lalit** 40:12 No, Tom, if it is co-pilot, I think it
tries to create a branch in the main repo. That's what I feel. It does not has a foke or something where it will do use it.
**Tom Tan** 40:23 Okay.
**Lalit** 40:25 Alright.
Let me. Probably we can see it here. I mean, that's a good point.
It's like this is a Pr. Which I tried.
And so it's move from, yeah, it's the main. It's in the main branch. Yeah.
So.
**Tom Tan** 40:39 Okay.
**Lalit** 40:42 See, it's a it's a branch in the main, in the main repo, not not not in the co-pilot users. Repo.
**Tom Tan** 40:49 Yeah, this makes sense to require like, right access to that.
Oh.
I think it for our repo. It is not recommended to create a pr. Like any branch. Now release branch in a memory. Pro, so
not sure if there's a way.
**Lalit** 41:04 I'm not sure if I'm not sure if maybe G, maybe Tc. Or Gc. Is going to configure it, to have a separate.
**Tom Tan** 41:11 For.
**Lalit** 41:11 Of co-pilot as a user. And then, that done, I don't know how it will do, but as of now, it's in the main
me and repo, yeah.
yeah. So so yeah, I think it's still still in the discussion. We don't have any. We don't have enabled. Have it enabled for the Hotel. Cpp. So I think we are are good with Mark's concern. And let's see, let's see, I think how it goes further.
Okay, yeah. Anything else to discuss.
**Tom Tan** 41:49 Oh, I was wondering like, do you send you have any concern or question on this.
**Ehsan** 41:57 I'm co-pilot.
Yeah.
I mean, the only concern I could have is the the licensing.
Maybe.
**Tom Tan** 42:07 Okay, that's a cla part. Yeah.
**Ehsan** 42:10 Yeah.
**Tom Tan** 42:11 That would be the only concern.
Okay, I think the
someone is working on this part, right? For for the all the open temperature pro projects.
**Lalit** 42:29 Okay, if not, I think
probably we are done for the with the meeting. Thanks everyone for joining.
See, you guys, next week have a good rest of the week.
**Tom Tan** 42:42 Thank you.
**Lalit** 42:43 Okay.
**Ehsan** 42:44 Everyone, bye.
**Doug Barker** 42:46 Bye, everyone.
**Lalit** 42:47 Gilbert.
