SIG: PHP SIG
Date: 2025-06-18
Duration: 37 minutes
Zoom Recording URL: https://zoom.us/rec/share/6FpwB3qBEc6rl_7Vr6EgLt3ueQR7JHWD7kQ0FnG21tZSA_lrIKZ3FKMqgOC_FSRc.uIkOVLYzpMLeiqfD
============================================================

## Zoom Recording Transcript

**Chris Lightfoot-Wild** 07:10 Hey, Brett.
**Brett McBride** 07:15 Hello! Hello!
**Chris Lightfoot-Wild** 07:17 Good.
**Brett McBride** 07:19 Where am I?
You know it's nearly how are you, Chris?
**Chris Lightfoot-Wild** 07:23 Yeah, I'm okay. Thank you. How are you?
**Brett McBride** 07:26 Oh, yeah, not too bad.
**Chris Lightfoot-Wild** 07:29 I'm rocking my new mug from Disney the week.
Oh, nice!
I went to.
**Brett McBride** 07:37 When I heard new mug I was sure that you were going to pull up some open telemetry swag.
**Chris Lightfoot-Wild** 07:44 Oh, if only yeah, it'd be nice. Nothing will ever happen. But it'd be nice to see some of the stuff like cubecon and stuff, but so that sort of thing. I think the company would pay for.
**Brett McBride** 07:59 Yeah, yeah, you think so. You think so.
I I once contributed to some. It doesn't matter what it was, but some open source thing, and as soon as I'd signed the Cla they asked me for my postal address so they could send me a mug, and I've got a yeah, right, bug with my my name on it. You know, contributed such and such a date.
**Chris Lightfoot-Wild** 08:30 That's cool.
Are you settled in now that you're back from vacation?
**Brett McBride** 08:40 Well, I'm not quite so sad about being back now.
yeah, I suppose I've settled back. Yeah.
yeah, it's a bit traumatic to to come back and have to, you know, resume life and go to work, cook my own food.
**Chris Lightfoot-Wild** 08:59 It's it's rough.
**Brett McBride** 09:01 He's rough, and it was, and and it's like it's turned bitter, bitterly cold here since well.
since we left. And yeah, yes, all I can do is turn my mind towards the next holiday start, start planning for that. Give me something to look forward to.
**Pawel Filipczak** 09:25 Hey, guys.
**Brett McBride** 09:27 Hello, Paul! Hey! Nick! Bob!
**Bob Strecansky** 09:31 Hello, welcome back, PAL!
**Brett McBride** 09:36 Hope you had a nice break.
**Pawel Filipczak** 09:40 Yeah.
I missed. I missed last week. So yeah, but I I was. I was back 2 weeks ago, so.
**Brett McBride** 09:46 Oh, really. Yeah.
**Pawel Filipczak** 09:48 Yeah.
you know.
**Chris Lightfoot-Wild** 09:54 You've seen you or something.
Did I did imagine that, or did you go to the Grand Canyon as well when you were there?
**Pawel Filipczak** 10:01 Yes, yes, I was there. Hmm.
**Chris Lightfoot-Wild** 10:05 Yeah. It was impressive.
**Brett McBride** 10:07 Hmm.
**Bob Strecansky** 10:10 You might even say that it's grand.
**Pawel Filipczak** 10:14 No.
**Bob Strecansky** 10:17 There you go.
Have you seen Iprat, the Grand Canyon?
**Brett McBride** 10:22 Not Irl, no.
**Bob Strecansky** 10:25 Well, it's you. Everybody's like, Oh, yeah, it's huge and like you don't think about it. And then you go there and go. Oh, wow, this is a yeah, like, be really big.
**Pawel Filipczak** 10:36 Yeah.
**Bob Strecansky** 10:38 Here in America we put an emphasis on everything being big. It doesn't really matter what the thing is. It always just needs to be bigger.
The new. They made a new Cadillac Ev. This that got released relatively recently, and it is the size of a small school bus insane to me. But anywho are we expecting anybody else, or should we just let it rip.
**Brett McBride** 11:09 No, I think we've got a good number. Let's start.
**Bob Strecansky** 11:12 Rip, Rip, we will.
Let's take a look. Oh, no.
Didn't even check to see what's on the back. No, okay, no agenda items today yet. That's good.
Let's see if that sticks around. I have a feeling we'll have other things to talk about, because I know that I do.
But let's just take a quick peek at that. Let's try looking at the backlogs first.st See if there's anything that sticks out to us.
Are there any of these items in to do that people feel are pressing.
**Chris Lightfoot-Wild** 11:47 They are pressing on.
Sorry! Did you say?
**Bob Strecansky** 11:51 Yeah, I said, any of them that people feel like we need to get going.
**Brett McBride** 11:54 1626, you can move over to in progress, because I think I've actually almost finished that.
**Bob Strecansky** 12:00 Okay.
**Chris Lightfoot-Wild** 12:01 Yeah, the one that oh, no, sorry ignore. I've already got one in the in progress column, so ignore.
**Bob Strecansky** 12:09 You have one in the chamber, if you will.
**Chris Lightfoot-Wild** 12:12 That's right.
**Bob Strecansky** 12:14 Alright cool.
Sounds good. Looks like we have a couple cool things in progress a couple. I don't know how these done. Oh, you can archive these. That's nice. Let's try that out.
It's fun alright. And then we also have the Php. Road to SDK. V. 2. That doesn't actively have anything on this yet.
but we can add.
**Brett McBride** 12:35 Do, however, have a I created a a label, and I labeled a bunch of things.
**Bob Strecansky** 12:41 Oh!
**Brett McBride** 12:42 2 point x so.
**Bob Strecansky** 12:44 Got it so is that an issue.
**Brett McBride** 12:46 Me.
Yes, I think both.
**Bob Strecansky** 12:51 So 2 dot X.
Oh, you just create. You haven't used the label.
**Brett McBride** 12:58 Oh, no, I have must be pull requests.
**Bob Strecansky** 13:02 What's a new.
**Brett McBride** 13:02 Probably closed as well.
**Bob Strecansky** 13:06 Oh, yeah, look at that.
**Brett McBride** 13:08 Yeah.
**Bob Strecansky** 13:08 Cool.
Alright? Well, that's good, that's good, and I'll make sure that we use that effectively as we can.
Let's see almost 16 million installs.
Let's take a look at if we have a couple of open pull requests.
Depend about, we can swap that in after this meeting. Brett. Do you want to talk through some of these.
**Brett McBride** 13:40 Yes, oh, which ones? Which ones?
**Bob Strecansky** 13:47 Yeah, I'm I'm there's you have 4 here. We're happy to talk through any.
**Brett McBride** 13:52 Yeah, look, they're all approved all 3 of them before we go ahead. Metric Simcom is the only one.
that I just appreciate more eyes on, just because it's more about like, how do we want to structure them?
Okay?
Just because, you know, I don't think we did a great job 5 years ago, whenever we created the 1st ones. But we're stuck with.
**Bob Strecansky** 14:14 Oh, man!
**Brett McBride** 14:15 So any mistakes from the past we can avoid, in place of some new mistakes.
**Bob Strecansky** 14:25 Got it. Okay? It looks like Nevae had a couple of suggestions for the log right record processor. One.
**Brett McBride** 14:31 I'd better get onto that one.
**Bob Strecansky** 14:33 Okay?
And then Psr transport network exception. This one's probably pretty simple. Chris, do you have the ability.
**Brett McBride** 14:40 Good.
**Bob Strecansky** 14:41 Yeah, because you have the ability to merge, or you just have the ability to approve.
**Chris Lightfoot-Wild** 14:45 Just to prove.
**Bob Strecansky** 14:47 Okay, so I can merge this. Then.
**Brett McBride** 14:49 Yeah, yeah, there was no code. It was just a test to.
**Bob Strecansky** 14:53 Yeah, I remember looking at that one just very briefly, but alright. So I think that's all of them for oh, Cedric, do you want to talk through about your Apache and Fpm. Resource? Detectors thought I saw him here, wasn't he? Here am I gaslighting.
**Brett McBride** 15:13 He was here last week.
**Bob Strecansky** 15:17 Yeah, alright. Well, then, we'll ask. We'll ask him another time, or, yeah, it's been approved, I think, by me.
Alright, Chris, all right, we can leave.
**Chris Lightfoot-Wild** 15:28 I mean.
**Bob Strecansky** 15:28 No one else.
**Brett McBride** 15:32 Neva pointed out that per spec. They should be in okay, as well as changes, but that they should probably be in contribut.
**Chris Lightfoot-Wild** 15:47 Yeah, it should be like vendor agnostic in the SDK.
**Bob Strecansky** 15:52 Okay, well, we'll leave that for now, and when we see him next time we'll get some feedback from him.
Contribute pdo metrics very cool.
I don't know.
So this one has. Let's see, this has a bunch of video. Oh, okay, yeah, this has some Pdo instrumentation that's cool. We? I can. I'll review this later, because this one's actually pretty relevant for me, too, because we use Pdm.
**Chris Lightfoot-Wild** 16:29 That that's gonna depend the fork of the SDK. It's not highlighted in that one was a a Pr for it, I think, as well, and.
**Brett McBride** 16:39 Yeah, it must be. Yeah. So yes, I think I think I asked for this because, the author just submitted some code into our Api, and I wanted to understand.
what are you doing before? So I could understand what the code did.
you know, before we accepted stuff into our Api. So
**Bob Strecansky** 17:03 Right.
**Brett McBride** 17:04 Yeah, but it doesn't. Yes. So what I'm hoping to see is sort of like something that's self contained here that makes sense. And we can see how it would be useful for other things that also want to generate metrics.
and then, you know, once we're happy with sort of how that looks. Then we can split out the reusable bits, and that can probably go and live in our Api always. Well, probably our Api.
**Bob Strecansky** 17:31 Okay, so do you want? Do you want me to review this? Do you want me to leave it as it is.
**Brett McBride** 17:35 No, I do want it to review. Yeah, yeah.
**Bob Strecansky** 17:38 Okay, I will review it.
**Brett McBride** 17:41 I'm just. Yeah. I'm not sure if it's gotten to that stage yet, or if he's just there you are. Yes.
**Bob Strecansky** 17:47 It's out it's out of draft. So it I would hope that it's ready for review. But I'll review it and see if there's anything that's just like, huh.
**Brett McBride** 17:56 Yeah. So anyway, that that's sort of the game plan in my mind, anyway, for what to do with this one.
**Bob Strecansky** 18:02 Cool. Thank you for the contact.
**Shawn Maddock** 18:03 Prove that, Ted?
It. It seemed like you wasn't aware of the existing clock.
**Bob Strecansky** 18:13 Yes, I remember that, so I'll tread carefully with that one. Then.
**Brett McBride** 18:17 Sorry I missed. That was someone talking. They were really quiet.
**Bob Strecansky** 18:21 Yeah, Sean, Sean said, this, this author wasn't aware of the existing clock implementation in the Api. So just I think it was just a reminder to be extra extra careful reviewing it up here.
**Brett McBride** 18:35 Yep.
**Bob Strecansky** 18:39 Okie Dokie.
Then this there was a remove. Unnecessary files from composer package, so.
**Brett McBride** 18:48 I think that was just waiting on Cla. Signing might be worth. It's been a while.
**Bob Strecansky** 18:56 Yeah, I'll agree.
**Brett McBride** 18:57 Otherwise, there's yeah, there's a i, Pr.
**Bob Strecansky** 19:15 No instrumentation flow requests.
All right. I have 2 agenda items.
The 1st one is the the open to the cloud. Native Computing Federation slack is changing from a paid plan to a free plan. On Friday they gave the Cncf. Salesforce, gave the Cncf. Almost 0 notice, saying, sorry you either have to pony up, or and I think it was a pretty significant amount of money, or it's going to turn into a free plan. So on Friday it will turn into a free plan.
The open telemetry Maintainers are actively working on a way to back up the important information that they feel we have from slack. They're, you know, obviously scrambling a little bit before the Friday deadline.
So if there's anything important in our history that you feel you must save, please do so, and if there's anything, if there's any integrations that you depend on, please make sure to know. Know that they won't work like our Github integration most likely will not work.
and anything else that you may or may not have added to the Cncf. Slack most likely will not work. They were discussing alternatives to using slack. There was a lot of positive momentum to using discord, but I think that only time will tell what the correct solution was when we started this project they used a product called Gitter, that I am. And we're actively not going back to using that because that was a terrible, terrible product, but I'm not sure, and I'm not sure what the end solution will be. But we'll keep you all up to, dated as we hear more, but I figured that was important to share. So if you still you will still be able to use the slack, I still plan on using that as the main form of communication for a little bit until the until the powers that be determine what our alternative is.
and then we'll go from there.
Any questions the other one that I was going to talk about was the code owners file that we have. I got during the spec meeting yesterday I was brought privy to this. They're creating a central release file for the community that talks through pat talks through how we perform releases and how we like, how.
who owns the pieces of code that are associated with each repo.
So which made me realize we do not have a code owners file in our repository, and we probably should have one, and we probably need to do a little bit of documentation like some of these other things have done for the release process. So I'm planning on coming up with a plan for that. Does anybody have anything they'd like to add about this.
**Brett McBride** 22:42 I don't know.
**Bob Strecansky** 22:42 Opinions.
**Brett McBride** 22:43 Which you've just scrolled onto now.
**Bob Strecansky** 22:46 Oh, look at that! I didn't even notice that, Brad. Thank you.
**Brett McBride** 22:50 That's right. I got emailed when you commented. I think.
**Bob Strecansky** 22:53 I see!
**Brett McBride** 22:55 Yeah. So I saw that does it also mention somewhere, I've also found somewhere that we shouldn't use code owners files like, in the last couple of days.
**Bob Strecansky** 23:07 Yeah, I think they were. I think that that is How do I say that? The right way? I think that that was definitely a point of contention in the meeting yesterday, like some people were like, Oh, yeah, code owners. Files are great. And then other people like, Oh, code owners. Files are useless, and I think that there wasn't like a very common consensus around the right, the right way to handle it.
But I think that we can put one like. It's easy enough to put one in place because we don't have that many code owners in our repository, and it seems like they're just doing it for the Api and the SDK, not for contrib, or like our instrumentation, or whatever, because a lot of the other Sig maintainers talked about how the they talked about how contrib code owners would be kind of useless because nobody would actually own those pieces, or it would be difficult to get in touch with the people that own those pieces. I thought that was kind of funny. I would have thought that that would be where a code owners file would be the most important when you have, like lots of different organizations and people working on a specific code base. But.
alas! Here we are.
**Brett McBride** 24:16 Mo. Most of those maintainers don't actually have any privileges in our repo, anyway. So what what benefit does the code owners bring there like it doesn't. We can't elevate people's privileges to approve or merge things.
**Bob Strecansky** 24:34 I think it. I think it's more along the lines of like collaboration and understanding, right? Like, if if the insta, if somebody owns the instana instrumentation in our contrib repo. If we need to make changes to it, they should probably know, I think, that that's more along the lines of where the code, like how the code owners would be effective with a repo that doesn't have the scoped permissions for everybody to make changes.
**Brett McBride** 24:58 Yeah. Oh, that would be great. But does it work like that?
**Bob Strecansky** 25:03 You can. So you can have code over like I mean, code owners does give you like the ability to have stuff like that. So? How you would have to use it is like, essentially you would make us the code owners, for all like of the Php. Maintainers, approvers would be code owners for all things, and then you could add additional code owners alongside us. So like you for elastic, you could up house for the like the elastic part of the code base, he wouldn't be able to like, approve, and merge things for the elastic pieces, but he would at least be tagged and aware of times when things get changed, and then he could make comments, and like do it, do his approval, or whatever.
**Brett McBride** 25:47 That'd be yeah. That that makes sense that I can see. Yeah.
**Bob Strecansky** 25:52 Yeah, so we can. I think we can.
I think I can just make like a very generic code. Owners, just to, you know, sort of fall in line with the rest of these other sigs, and then we can see how things play out from there. That's that was my plan. If there's no resistance.
**Shawn Maddock** 26:14 That made me think of 2 other things. Is my volume better now?
**Bob Strecansky** 26:18 You can hear you, Mister.
**Shawn Maddock** 26:19 Okay, one. Have you had any clarity around just how to handle that contrip code that we've been talking about the last few weeks.
**Bob Strecansky** 26:31 No, they they never follow back up about that. Thank you for mentioning that. I'll go and see if I can find find that thread.
**Shawn Maddock** 26:38 And then I think yesterday I saw someone in slack ask about the open telemetry operator, the Kubernetes.
and there's a Php Docker image in there.
Which I wouldn't use. But I I was unaware of, and just wondering if we should be linking to that somewhere in our documentation. Just so if people come into open telemetry through the through Php, they're aware that this thing exists that's not within.
like the Hotel Php Repo, or mentioned anywhere.
**Chris Lightfoot-Wild** 27:18 Yeah, is, is that the bit? I think Sergey did.
**Pawel Filipczak** 27:21 Yes.
just working on that. I will ask him, about the dogs? I thought that he he was doing something around the dogs, but I'm not sure, so I will ask him, and and and let you know.
**Shawn Maddock** 27:34 Specifically the the Php.
Like language section of the Docs. I think it's mentioned within the Kubernetes section.
**Pawel Filipczak** 27:42 Hmm.
**Shawn Maddock** 27:44 Just cross-referencing.
**Pawel Filipczak** 27:46 Yeah.
**Bob Strecansky** 28:02 Actually, I have 1 1 question. So I I got a request about about instrumentation of the Post G, as well.
**Pawel Filipczak** 28:10 A driver. Have you ever heard about any demand on that? Or that's only one request from from my user.
**Bob Strecansky** 28:20 You, said the Postgresql driver.
**Pawel Filipczak** 28:22 Yes, yes, yes.
**Bob Strecansky** 28:24 I think we just haven't come across that yet, and I'm sure that it's going to be a requested feature. Just I think nobody's asked about it yet.
**Pawel Filipczak** 28:33 Okay, okay, I think about implementation. So maybe I will. Maybe just, you know.
create issue for that and and start implementation.
So and the last thing I wanted to update you about the elastic distro and contributing him to the the open hotel.
So when I I came back, so I push it forward. Now we have it stuck somewhere in the decision making. So we need to have a green light and some other departments.
So I created the plan here, and the description of the of the contribution proposal. So it's ready. But still I cannot make it public.
I just need the approvals for that, and I will push it.
So I hope next week it we will get. We'll get it. And we can start. You know.
official talks about yeah. So sorry for that that it took so so some and so so long, so yeah.
**Brett McBride** 29:37 Alright sounds, like exciting progress, even.
**Pawel Filipczak** 29:40 Interesting.
**Brett McBride** 29:41 E-minute.
**Bob Strecansky** 29:44 We are all excited.
**Pawel Filipczak** 29:47 Yeah.
**Chris Lightfoot-Wild** 29:51 I had a final thought. Sorry as well, I think. Maybe I've seen on a an issue, or maybe, Sean, you think you'd mentioned about Psr. Transport.
Not only I was passively debugging something and I was exporting both traces and logs, and noticed that in the Psr. Transport factory.
They both create separate like Google instances.
And then obviously, connection pool in that they both have to establish separate connections. As a different clients and and obviously depends on the config. But in this scenario I've got the same physical host and port combo. It's just a path that differs. But you know. I wondered if that was something that perhaps has already been fixed. And I've just not updated, or if it's worth looking further into how we do our connection pooling for for these transports.
**Brett McBride** 30:48 It's a good point. I I can remember the sort of the issue that that Sean was talking about, which is just a bit of a tidy up or basically removing something that's barely use now, but actually having different things. Share the one guzzle transport.
Yeah, that could be interesting. Yeah, we might need some.
How would we do that? I'm sure we could.
But it's probably auto loading is is the problem. It's probably needs to be a bit smarter about.
**Chris Lightfoot-Wild** 31:26 I think they both go through a transport factory, but just instantiate like an think of that, whereas I've obviously had its own cash in that factory of Host, IP combo, etcetera.
**Brett McBride** 31:40 Oh, yeah.
**Chris Lightfoot-Wild** 31:41 Problems serve back a pre-existing one, and then you can benefit the pooling.
**Shawn Maddock** 31:46 And we already have a pattern elsewhere of using like a a static week map.
by key, like in the context.
So just using that same thing in the factory might allow for reuse.
**Chris Lightfoot-Wild** 32:08 Yeah, yeah, probably.
Yeah. The client probably actually does the pooling by itself, anyways and maps to the right connection. So what would make sense that we just have a central factory, and it takes care of the rest.
Cool. Sorry. Just wanted to, anyway, because I just had noticed something I was hitting, like, you know, a break point a couple of times. And I was like, I've already seen this. But yeah, that's what was going on.
**Brett McBride** 32:34 So.
**Chris Lightfoot-Wild** 32:35 Thank you.
**Brett McBride** 32:37 It's probably worth even just documenting that as a bug or an issue.
just for visibility. Chris. So that we don't.
**Chris Lightfoot-Wild** 32:47 Yeah, I think I perhaps just held off because I I realized I wasn't on the latest and greatest install. So I'll try bumping that, and it's still an issue. I'll I'll do that.
**Brett McBride** 32:59 Yeah, have a look, but I I don't remember seeing any fixes along those lines.
**Chris Lightfoot-Wild** 33:06 Not not say it's obviously broken, but it's just yeah.
Thank you.
**Brett McBride** 33:11 Optimized.
**Chris Lightfoot-Wild** 33:14 Okay.
**Bob Strecansky** 33:21 Just making this issue now, while I remember it.
**Chris Lightfoot-Wild** 33:24 And then I noticed Neva had made an issue as well on the issue border. Did we skip over that one.
**Bob Strecansky** 33:30 We haven't gone through the issues yet, but we can.
**Chris Lightfoot-Wild** 33:33 Oh, sorry. Yeah.
**Bob Strecansky** 33:34 That's right.
Yes, I saw this one, too.
**Shawn Maddock** 33:46 I'm not seeing your screen.
**Bob Strecansky** 33:49 Oh, hmm!
Wonder what happened?
**Chris Lightfoot-Wild** 33:53 Well, you could see a screen, but unless it was a different screen, you were looking at.
**Bob Strecansky** 33:57 You all see this now.
**Shawn Maddock** 33:59 Yes.
**Bob Strecansky** 34:00 Very strange. Alright! Alright! This is the issue that you're talking about. Right, Chris.
**Chris Lightfoot-Wild** 34:06 Yeah, that's it. Yeah.
**Bob Strecansky** 34:08 Okay.
**Chris Lightfoot-Wild** 34:09 I don't know if it was a help wanted one or it was a an indicator that he's gonna pop across.
**Bob Strecansky** 34:18 Yeah.
**Chris Lightfoot-Wild** 34:19 Let's see.
**Bob Strecansky** 34:22 I can ask him.
**Chris Lightfoot-Wild** 34:26 Well, yeah, I think this is.
**Brett McBride** 34:27 He was going to do it, he would have just.
**Bob Strecansky** 34:30 Yeah, that's.
**Brett McBride** 34:31 Yeah.
**Bob Strecansky** 34:33 Yeah, I agree with you. But I just wanna make sure I don't wanna have somebody else start working on it.
**Chris Lightfoot-Wild** 34:38 Only I think this not cross up, but with the environment loader stuff that I was doing. I think it paused in the past that some of these things depended on this SDK configuration package, and like, if it wasn't available like the environment loading wouldn't work, etc, which felt weird them.
But I think this is probably the similar thing point across into the Api makes sense and.
**Brett McBride** 35:09 Yeah, I think I understand.
**Bob Strecansky** 35:16 Another issue. Do we have any other issues that came up recently?
Resource detector name? That was oh, that was you, Brett.
I think I remember seeing that one on the board.
Oh, Sean, you had 1 2 weeks ago about deprecated after Http. Discovery.
**Shawn Maddock** 35:40 If I could remember what this was.
**Chris Lightfoot-Wild** 35:44 No.
**Bob Strecansky** 35:45 Redundant Code.
**Shawn Maddock** 35:47 Oh, yeah. And Brett said, I think Brett said he was good with this. It it's been a slow trickle of yeah moving it. So yeah, I have a few issues that I think y'all have said sounds good. And I just haven't gotten around to making.
**Bob Strecansky** 36:07 Do you want me to?
Do you want me to tag this as help wanted? Or is this something that you would like to work on.
**Shawn Maddock** 36:15 I mean I was.
I'm good working on it, but if someone else has time before me, I'm fine with that, too.
**Bob Strecansky** 36:22 Okay, I'll put it as help wanted, and I'll put it on the project board as to do so. If somebody else wants to pick it up. They can.
Okay.
I think that those are all the relatively recent.
Those are all the relatively recent issues that we have.
Does anybody else have any other agenda items that they would like to discuss today.
No news is good news, all right. Well, if we have nothing else, we can adjourn. Thanks. Y'all.
**Chris Lightfoot-Wild** 37:04 She's also a.
**Brett McBride** 37:05 Thanks everyone. Bye-bye.
**Pawel Filipczak** 37:07 Thanks for.
