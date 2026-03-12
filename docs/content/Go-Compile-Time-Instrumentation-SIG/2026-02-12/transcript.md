SIG: Go Compile Time Instrumentation SIG
Date: 2026-02-12
Duration: 38 minutes
Zoom Recording URL: https://zoom.us/rec/share/ynTy_ojswqqyPNZ8J4fax9CXHn_i_isCZoyMJ229Y7etiZD8oLqNqNpOlJPPiShj.jxM4sw0KAkwH0_1K
============================================================

## Zoom Recording Transcript

**Kemal Akkoyun** 04:07 Hello, hello.
**Dario Castañé** 04:12 Hello, good morning.
I don't go that from…
**Kemal Akkoyun** 04:15 Good morning.
And good afternoon, yes.
Who is the facilitator today? Who was the last one?
Ramichek was the last one. I am the one, I guess. It's always the case, whoever asks.
is the facilitator.
me.
I only give a couple of more minutes for people to join.
Alright.
Brumicek said that he won't be joining.
This might be all of us.
**Huxing Zhang** 05:55 Hello?
**Kemal Akkoyun** 05:56 Hello.
**Huxing Zhang** 05:59 My computer… I have some difficulties with my computer joining this meeting, because our company has limited the access of using this software, so I have to.
Yeah, no.
I have to apply for approval to use that, so I'm joining with the website from the URL.
I can't use the software without the approval.
**Kemal Akkoyun** 06:30 Yeah, we have similar things.
But I guess Zoom is sanctioned for us.
**Huxing Zhang** 06:37 Yeah, the approval I requested has been expired.
We have to refresh, renew this every, like, couple of months.
I'm with Yi Yang in the same meeting room, so he's mute, currently mute, and when needed, he will open the mic, and we can't open it at the same time, so I have to.
**Kemal Akkoyun** 07:10 Okay.
**Huxing Zhang** 07:11 I'll take. Okay.
**Kemal Akkoyun** 07:22 Alright, let's start. I guess this will be, all of us for today.
was just checking the open PRs and issues.
We don't have, like, a specific agenda item, I guess, but, like, we wanted to meet, before your, like, break, I guess?
**Huxing Zhang** 07:44 yet.
**Kemal Akkoyun** 07:45 And I can talk about Hotel Unplugged? Yes, please go ahead.
**Huxing Zhang** 07:52 Oh, yeah, I have added a couple of… Since…
**Kemal Akkoyun** 07:56 Oh.
**Huxing Zhang** 07:57 You're frog?
**Kemal Akkoyun** 07:57 No heavens.
**Huxing Zhang** 07:58 In the beginning of that, yeah.
**Kemal Akkoyun** 08:00 Yeah, let's start with those.
Yes.
You already have them.
We can go ahead. Do we have any waiting action items?
Just checking… We have shared a documentation on instrumenting. I think you did a session about this?
But…
**Huxing Zhang** 08:24 Yep.
**Kemal Akkoyun** 08:25 documentation, yeah, say it's done. I remember you shared a…
**Huxing Zhang** 08:30 Yeah. Link.
**Kemal Akkoyun** 08:32 This is also dumb.
Damn.
Some of them are really old, maybe.
**Huxing Zhang** 08:44 Yeah, I don't… I'm not thinking… saying that we reviewed the task so much earlier, but just.
**Kemal Akkoyun** 08:53 No, no, I also wanted to do that, like, whether we missed anything. I think we've done a lot of it, but we are not doing a good job to check them out.
**Huxing Zhang** 09:04 Yeah.
**Kemal Akkoyun** 09:05 Stop.
When it comes to regular status, I think we have a plan, right, on V1, and don't think we have a disagreement. This is a good plan.
We just need to start building things.
And I guess we are also doing that. I already see, like, yeah, Redis Instrumentation PR, PR… we have a PR from, like, two PRs, actually, from Dario to these, and… There are a lot of nice discussions on this PR. I don't know what is the status of this, maybe, you can say something about this, Dario.
**Dario Castañé** 09:50 Yeah, but this one, the conversation went… To worth discussing about how to… Implement, What kind of rules used in the official instrumentation, whatnot?
We agreed on, allowing to have The rule doesn't mean it's going to be sanctioned as a valid rule for the official instrumentation. We just implemented to allow people… to allow users to To implement every, anything they want.
But, this one is blocked by the other one, the import CPG manipulation support. I'm just working… I will be working on this one today.
Fixing all the concerns and everything.
And… yeah, I see, okay, thank you, young. I see that you are, that, you replied to my… to my last comments. So…
**Kemal Akkoyun** 10:50 Yeah, I guess when you are out, like, the biggest problem we're gonna face, because probably I also want to work next week on the project again, and, like, Dario is already working, and you will be out, so we will be missing some reviewers from your site. Maybe we can just, like, ping Bremichek, and he can chime in.
Because, Xavier also is not… he's not… he's out, you're out. So, we don't want to approve only, like, the PR swab coming from our side, so we need a second, pair of eyes on the reviews. Let's see if we can, find time from Primajek.
**Huxing Zhang** 11:35 Are you saying that Dario is going to not be working on this project?
**Kemal Akkoyun** 11:41 No, no, he will be, and I will be next week, but we will need reviewers.
**Huxing Zhang** 11:47 Oh.
**Kemal Akkoyun** 11:47 outside data mode, right? And you will be out. That's what I'm trying to say.
So, that's why probably we will need to ping PremiCheck for the.
**Huxing Zhang** 11:59 Yeah, we will be, like, unavailable maybe in the next two weeks, I think.
Hmm.
**Kemal Akkoyun** 12:07 Two weeks.
**Huxing Zhang** 12:08 one week, but I don't know if someone will, have more extra holidays. They will have PTOs. Yeah, so you will expect, like.
to roughly 2 weeks, I think.
**Kemal Akkoyun** 12:25 Okay.
Yeah, like, the other week, we are also on a, like, a summit, so probably won't work, but just concerning next week, maybe we can try to merge this PR, the import config stuff, before you, like, you go to the holidays. That would be a nice goal.
**Huxing Zhang** 12:46 Okay.
**Kemal Akkoyun** 12:48 It's on dart.
**Yi Yang** 12:51 Yeah, I… I reviewed the SPR, and I left some comments. I think, it's generally, it's generally good, so I could give, a… Approval, or hede.
Before, you, you can, you can fix the comments and merge without my approval.
**Kemal Akkoyun** 13:16 Awesome, awesome. Thanks for that.
**Dario Castañé** 13:18 Thanks.
**Kemal Akkoyun** 13:22 Cool! Looking at this, yeah, we need to review this. Copilot already does a good job, I guess, but we will check.
I'm not concerned about instrumentations, like, they can wait, but the core functionality, it would be nice so that we can continue iterating.
Okay, this… Actually looks good to me. Ugendos.
the online review and merge list.
So, what else? Is there any other things that we need to, like, that you have in mind?
**Huxing Zhang** 14:06 Yeah, I remember that in the last meeting, we have discussed the proposal of, like, using YAML file to do things, or you just keep the current, current solution, I think PersBank has proposed, that So I want… want to know the, things that you… have… have you… have you discussed with them, or have we… there is a… consensus, Omar, over that.
**Kemal Akkoyun** 14:36 I think after the last discussions, there weren't any concrete items.
And, like… Right now, we are keeping the status quo.
But I think we can address that in the later stages, again.
**Huxing Zhang** 14:53 Okay.
**Kemal Akkoyun** 14:53 Mmm… I'm… Trying to remember. It's been a while we actually discussed that, right?
**Yi Yang** 15:03 I remember that in the.
**Kemal Akkoyun** 15:05 Yeah, too.
**Yi Yang** 15:06 Oh, I remember the, you, not joined that meeting.
**Kemal Akkoyun** 15:12 I didn't, yeah, I wasn't there, and, like, I saw a consensus now, keep the current approach, and discuss the DSL in parallel. I guess that was the consensus.
Do you remember? Dario, you were there… and Yangiwer, like, I guess…
**Dario Castañé** 15:34 Regarding the Go or YAML instrumentation.
**Kemal Akkoyun** 15:38 Yes, yeah.
**Dario Castañé** 15:44 We… I mean, I haven't worked on that, neither… I don't think there has been any progress.
**Kemal Akkoyun** 15:54 I'm just trying… I'm asking if you remember the consensus from the notes. I can see that, like, keeping the current approach is the consensus, and…
**Dario Castañé** 16:02 Yes.
**Kemal Akkoyun** 16:03 Okay.
Then, cool.
**Huxing Zhang** 16:08 Okay. I just want to make sure that you have, been aware of that, and no.
Okay.
**Kemal Akkoyun** 16:18 Okay, so, like, what we discussed, discuss the next step for the, of the, of the month. I think, you will be out, right?
That is basically concluding the February, so… I guess we can meet when you are back that week and discuss the further action items.
**Huxing Zhang** 16:54 Yeah. Have we made release since the last release? I think we have… Which the conclusion that we should release in a fixed rate.
Like, every one or a half, or maybe two months.
I remember that before the new year, I think we have made the first release.
**Kemal Akkoyun** 17:18 Yeah, did we actually… created a… no, we don't have a release doc, do we? Did we agree on… the cadence. Maybe we agreed, but we didn't document it, I guess, right? Yeah, I don't see anything.
**Huxing Zhang** 17:36 Yeah.
**Kemal Akkoyun** 17:37 So, like, we can do that, If we have something to share with the world.
Yeah, we can do it.
We have a release from last week, though.
**Huxing Zhang** 17:53 Yeah, yeah, we actually have released it. Who does that? Yeah, good.
Okay.
Yeah, has done this release. I think, we're in good shape, and, maybe we can keep…
**Kemal Akkoyun** 18:13 We should document this process, and… Where is this?
Tomato release process.
I think we create… we need to create a doc for release.
And then… And we can assign, like, some release shepherds every month, and, like, we can share the burden.
**Huxing Zhang** 18:39 Okay.
**Kemal Akkoyun** 18:54 Yeah, so documentation worked, but yeah, so we need to do this, and then, we can remind ourselves in every meeting, like, who does the release and whatnot. I guess releasing is right now super easy, it's just a matter of tagging.
But it will be nice.
Cool.
Any other, concerns?
Did we actually discuss the, like, deadline of the release? Oh yeah, okay.
I think we should aim for, like, June.
Really?
And then… Yes. I think we can make it. We, you know, have, like, more than 3 months.
And, let's aim for releasing, like, a feature-complete version of the tool.
that we can call V1, in June. What do you think?
Too ambitious?
**Huxing Zhang** 20:06 How many tasks have we left?
**Kemal Akkoyun** 20:12 Mmm… checking these, like, the… chunky ones are actually the, like, the coal site instrumentation that we have proposed. The other ones are, like.
Actually, like, quite achievable.
I guess, like, the… the biggest, obstacle is, like.
from our side. So… and it is… I'm, like, checking the… V1… yeah, these two, like, this… this one, and… and that's, like, a part issue. Is this… Yeah.
And we will be working on this, right?
Yeah, I added this for, like, our roadmap.
we already, like, I already created this issue, and we will have these. And, like, I edited TBD from your site. Is there any, like, Things that you would like to have from your tool.
**Huxing Zhang** 21:15 Okay.
**Kemal Akkoyun** 21:17 if, like, feel free to edit, like, anything that you would like to carry over, and then we can conclude the tool, then we can focus on, after June.
we can focus on the integrations, where to put them, like, decide on how to sanction them, like, how to carry them here. I think that comes later.
What do you think?
**Huxing Zhang** 21:43 Yeah, I think that sounds good to… to me, and I see you… I see that you… List a lot of features there, and do you mean that we should implement all of them before the one point?
**Kemal Akkoyun** 21:59 We plan… we plan to implement this piece.
Before V1. That's our goal.
**Huxing Zhang** 22:05 Okay.
**Kemal Akkoyun** 22:06 Like, our goal is… with the V1, we can actually use an upstream tool instead of orchestrian, right? That is our goal, and we would like to do this as much as soon as possible, right? Otherwise, like, we need to maintain these two open source projects, right? And it's not a position that we would like to be in, right?
So, if you have similar goals, like, in the end, like, we will be using the Hotel C for most of our works. That's… that's our goal.
So, if you have similar ambitions, like, please, like, list them, like, what is the blocker for you to use this, and then we can, like, focus on this.
**Huxing Zhang** 22:52 Okay, maybe, Yang, you… do you have any comments on this? You can…
**Yi Yang** 22:57 Okay, I, I will, I will list some… some items after, after… I… I start work… I… I start work in next 3 months… weeks.
**Kemal Akkoyun** 23:11 Awesome.
**Yi Yang** 23:13 Basically, I think the… we can… I… I believe we can release the first version, so, first version in… in June. I think it's… it looks good to me.
**Kemal Akkoyun** 23:26 Awesome, awesome, yes. Yeah.
And people are waiting, like, that's my last topic, right? Hotel Unplugged.
I proposed a lot of topics about, like, compile time and auto-instrumentation, whatnot, and people were interested. I already shared a picture, like, those plus ones.
they are coming from other community members, and people are looking forward to this. They ask questions how they can use, but the answer is always, like, it's not ready, and it will be ready in a couple of months, so we need to deliver on that promise, right? Like, then we can talk about, like, this is how you can use, and people… and you need to have users, so otherwise, like.
We won't be, like, giving back or, like, improving the tool by itself.
**Huxing Zhang** 24:15 Yeah, right.
I think it's good, I… and we also would like to… to see it stable, and we can… maybe in the next big events of Kukan, like China or Japan, we can… Announce that.
**Kemal Akkoyun** 24:34 Yeah, the KubeCon Japan, I think it's… Still open, right?
The CFP is still open.
It's July.
It's in July. Yeah, this… this, like, could be… like, we can announce something, but it's… also ambitious, but I am trying to understand the CFP, Yeah, CFP's still open.
**Huxing Zhang** 25:04 Right.
**Kemal Akkoyun** 25:05 we can aim for this? I don't know.
If anyone wants to go to Japan.
at the end of June, which… could be hot, like, really hot, I guess? But, yeah.
Go ahead.
Then it's KubeCon Trainer.
**Huxing Zhang** 25:24 Yeah, June, it's… I think October 10 is September.
**Kemal Akkoyun** 25:31 It's not an on-site thing. This is 2025.
Why? Yes, this is cute.
Boom.
**Huxing Zhang** 25:39 It's already published. I think so… It's published? I think it's… you can, you can search KubeCon 2026.
China. Okay.
The second link, the second link, yeah.
**Kemal Akkoyun** 26:02 Oh, it's… Extended to include some…
**Huxing Zhang** 26:07 Yeah, you don't see…
**Kemal Akkoyun** 26:08 Oh, okay.
**Huxing Zhang** 26:08 event, including the PyTorch conference and the.
**Kemal Akkoyun** 26:12 from…
**Huxing Zhang** 26:12 Amid. You're right.
It's gonna be a very big event this year.
**Kemal Akkoyun** 26:17 Yeah.
Yeah, this… this could be the one that we should be announcing, to be honest. If there are a lot of people, this is… this would be better.
**Huxing Zhang** 26:27 Yeah, yeah, yeah.
**Kemal Akkoyun** 26:30 Yeah, let's, like, we can propose something for this one.
Yeah, I think this is more achievable than, japan one.
More realistic.
**Huxing Zhang** 26:47 If we have something to show, we can also, plan to… we can also think about, to talk about that in the group country passing, it's quite… Good.
as well.
But we can target to the Kukan Shanghai as the… The big, the biggest event, and we can make a major release before that.
**Kemal Akkoyun** 27:18 this?
One of the things that keep coming up with the hotel unplug.
to be basically, like, collaboration with the other projects, and how we can mix and match the auto-instrumentation strategies and enable others, whatnot. So, I think… I don't know if the hotel unplugged will be happening next year as well.
We might need better, like, representation, so that we can talk to the other maintainers.
because this OpenTelemetry injector Sync, they are building something, there is OBI, and, like, we can enable some of the features in these projects as well.
one of the things keep coming up, like, how we don't, like, set each other's toes, because, like, they're doing the same thing in an injector thing. Right now, if they see an OpenTelemetry SDK already in the process, they skip instrumenting that.
But yeah, like, maybe… like, there could be an opportunity where, like, we put some, like, identifier information that this is already instrumented with the Go compile time, so, like, you don't need to do that. Something like that, we need to, talk to those people as well.
So yeah, like, feature is bright, let's try to… See this, to make this finish?
**Huxing Zhang** 28:52 So, I, I, I also want to ask, an… Do you plan to join the KubeCon Europe this year?
None of, like, none of my talks accepted, so…
**Kemal Akkoyun** 29:07 There is no plans to join this year.
Are you… are you joining?
**Huxing Zhang** 29:12 I also have… my proposals got rejected, but I will join, because I will speak for another project this year.
So I, I will go to there.
I was thinking of that, if there is a chance to, like, meet with you guys, but I don't know if you will join or not.
**Kemal Akkoyun** 29:36 That would be awesome, that would be awesome, but I think we are not joining. Dario… no, Dario is also not joining, and I'm not joining as of now.
maybe things can change, but yeah, KubeCon is, like, a week, and it's, like, hard, yeah, hard time to just, like, take some time off and go… go there, so…
**Huxing Zhang** 30:00 Yeah.
Okay.
**Kemal Akkoyun** 30:03 I will meet in one of these cube cones, I'm shook.
Like, if we aim for a China announcement, and if you got a talk accepted.
Yeah, we will try to come. But I guess it's hard for us, also, We'll see, we'll see, let's see how it goes.
**Huxing Zhang** 30:24 Okay.
**Kemal Akkoyun** 30:26 At the very worst case, we can aim for KubeCon North America, which is the most popular one of the KubeCons, I guess, and then, yeah, we can try to meet there. We can maybe propose a working session.
for all of us, to the maintainer track, to meet and discuss the details of the project. These sessions are also, like, available for us, right? And…
**Huxing Zhang** 30:51 Okay.
**Kemal Akkoyun** 30:52 We can ask from the Open Telemetry Governance Committee to have a session for us.
And we can use that to get… go to the QCon, and meet there, and work together, and discuss the next steps of the projects next fall.
Thanks, Cubicle.
**Huxing Zhang** 31:12 So, will you consider the same thing that did for the Europe this year? Because… I think it's, still time for us, if we would like to ask, discuss with the community members, the governance community member, maybe.
**Kemal Akkoyun** 31:33 I don't know if it's… I don't know if it's possible. Would you like to ask them on that… on our private channel?
**Huxing Zhang** 31:41 Yeah, yeah, I can try, I can try.
**Kemal Akkoyun** 31:45 Maybe if they can… if can… if we can get a ticket?
it would be easier for us to handle the rest of the things, right? Maybe just for a one day, we can be there. I don't think I would be there for, like, the whole week, but if we decide to meet for the maintainer's day, and if we can get some tickets for me, and maybe Dario, and we can we can do that. I can't speak for Dario, but, like, we can try to be there for a one day.
**Huxing Zhang** 32:17 Yeah, now let me try to ask for… for this.
**Kemal Akkoyun** 32:20 Thank you.
Thank you for doing that.
**Huxing Zhang** 32:23 Yeah.
**Kemal Akkoyun** 32:24 Maybe you can add an action item for that, right?
Ask for KubeCon… EU tickets.
**Dario Castañé** 32:41 Sorry, I heard my name, but I was attending a call.
**Kemal Akkoyun** 32:46 No, no worries.
We discussed whether, like, we're going to ask to the governance committee whether we can have KubeCon tickets.
and have a meeting there, and if we have some tickets, maybe we… I suggested maybe we can go there just for that, meeting, so one day for the maintainer's ticket. Yeah.
It would be easier for us to… Yeah, but first we need the tickets, and then we need to have that discussion with our companies.
**Huxing Zhang** 33:19 Yeah.
**Dario Castañé** 33:20 before the QFCON in Europe, or for, you know.
**Kemal Akkoyun** 33:23 Europe, this is… this is a close car on Mars.
**Huxing Zhang** 33:26 This one, yeah.
**Dario Castañé** 33:27 Okay.
Yeah, it could work.
**Kemal Akkoyun** 33:34 Alright, that's it, I guess.
See you in a couple of weeks. Have a nice break.
And, yeah, see you online, otherwise.
**Huxing Zhang** 33:47 Thank you.
**Kemal Akkoyun** 33:48 Bye-bye.
**Yi Yang** 33:49 Bye.
