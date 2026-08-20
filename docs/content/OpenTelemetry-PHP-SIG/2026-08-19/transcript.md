SIG: OpenTelemetry PHP SIG
Date: 2026-08-19
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Chris Lightfoot-Wild** 08:29 Sorry, we just saw the other one going, I wonder if Bob's turning up today? We were… me and Pawel were both in that one.
I can't hear, sorry, I don't know if it… is it me, or…
**Pawel Filipczak** 08:42 Is that better?
**Chris Lightfoot-Wild** 08:44 They can handle, yep.
**Bob Strecansky** 08:47 They, yeah, they changed that, they wanted us to use the new one, that's why I changed the Slack bot version, but y'all probably have a meeting… an outdated meeting invite somewhere.
**Chris Lightfoot-Wild** 08:57 Yeah, I think I've got… so, I did delete the old one from my calendar, but then I've got the Ubuntu reminders, and I just got that one, which I guess isn't synced up somewhere, so… Try and delete that one.
**Bob Strecansky** 09:10 Awesome, keep on your problem.
This is the year of the Linux desktop.
Alright, laddin.
Get to sharing.
Let's rock.
Brett told me he was 50-50 for coming or not coming, because he's also on baby duty, so… we may see him, we may not, but… Alright, let's look at the agenda, and, we'll get Paw on here… Alright, chris, you have two highlighted issues that you wanted to talk through.
**Chris Lightfoot-Wild** 09:56 Yeah, yeah, if you could open them, because I've, I was going to discuss them last week, and it was just, me, myself, and I, so I just carried them, so I've kind of semi-forgotten what they're about. I think this one was… The gist of it was suggesting that other languages A more opt-in than what we are?
I don't know how true or not that is.
But this certain individual obviously had seen it as a surprise that things were happening.
Just because of the existence of the packages being composed in.
Versus having to, like, you know, enable an environment variable or something to… to get instrumentation going.
**Bob Strecansky** 10:34 Grab it.
**Chris Lightfoot-Wild** 10:35 So, I just wondered if there's any, like.
opinions on that? Like, is that actually the case? Are we… are we the different ones from other languages?
But… Was that intentional, or is it… Incorrect.
**Bob Strecansky** 10:50 All I can do with the international… Auto package is not the instrument.
No, I think… I feel like that was done… sorry, I'm changing my Zoom screen before I reshare, one second.
I don't… I mean, this is auto-instrumentation, right? If you're installing an auto-instrumentation package.
I could see both sides, right? I could see you wanting it to be auto-instrumented, and I could see you not wanting it to be auto-instrumented.
And maybe that's just something that we need to… Determine.
**Chris Lightfoot-Wild** 11:24 Yeah, I guess I'm the same. It might be frustrating if you're on a team and someone else happens to have added that, you know, because… they're able to instrument, you know, they've got all the APMs set up, but then you've just pulled the repo and gone, what the hell is all this stuff? And why is it slowing my… Test executions, though.
Yeah.
And obviously, there's that… is instrumentation-enabled stuff, which, It's different behavior than the SDK is disabled, but you can still instrument You still actually hook into functions and the overhead of that, if you're not even doing anything with it.
Yes, ma'am.
**Pawel Filipczak** 12:07 I have no strong opinion on that. I would also check the… how Java behaves, so note… We have the how it works for the node, but I'm wondering how it works for the Java.
**Chris Lightfoot-Wild** 12:21 Okay.
So, yeah, I can check then for Java, but even if it… if Java is the other way around, we can't change that until, like, we have a V2 anyway, if we decided we'd go that direction, so… Yeah, I can follow up on this and, Yeah, I just didn't know if… maybe, Bob, you just had a, like, an answer to this off, you know, top of your head, that's definitely done this way, and we discussed it years ago, or whatever.
**Bob Strecansky** 12:50 No, I think… I think this is a classic one man's trash is another man's treasure.
**Chris Lightfoot-Wild** 12:55 Yep, yep.
**Bob Strecansky** 12:58 Okay, well, thanks, Chris. Yeah, if you could see what Java does, then we can… If you want to continue that discussion there, that's… I think that's a good place for it, and if you want to… if you want to get more insight, or if you want to tag me in too, I'm happy to help.
**Chris Lightfoot-Wild** 13:11 Yeah, I guess, is there… outside of Java, then, do we have any other… SIG that is, like, you know, if the top two were doing it, would… like, who's the other one I should check? Like, Java, and then…
**Bob Strecansky** 13:26 Probably Go, I guess, or Python.
**Chris Lightfoot-Wild** 13:29 Do all Python, cool.
**Bob Strecansky** 13:30 net would be a good one, too, but .NET code always reads like Spanish to me.
**Chris Lightfoot-Wild** 13:36 Okay, cool, cute.
**Bob Strecansky** 13:38 Then this was the other one that you had, Stranded values do not get a reference count increase, which corrupts memory.
**Chris Lightfoot-Wild** 13:46 Yeah, so there is actually a link to PR at the bottom, and there's some, unit tests, etc, but… yeah, someone with C expertise, would probably be better to look at that,
**Pawel Filipczak** 13:58 Yeah, before I went to… to vacation, I was… Investigating it a bit, so we have also some issues in the distro.
Implementation.
And I'm not sure if I get any conclusions about the… about that, so I will take a look.
**Chris Lightfoot-Wild** 14:16 Okay.
**Pawel Filipczak** 14:18 I will focus on that, so…
**Bob Strecansky** 14:21 Why does it never let you do that?
Did I spell your name wrong?
**Pawel Filipczak** 14:30 Into. Into.
**Bob Strecansky** 14:35 Jacob?
this… You have to, like, write the comment before you can assign it to somebody.
Sometimes it still won't let you.
**Chris Lightfoot-Wild** 14:56 Is it something to do with group membership? Like…
**Pawel Filipczak** 15:00 Excellent.
**Bob Strecansky** 15:01 Got it I don't know. You're tagged in it, so you can assign yourself. Cool. Thank you for doing that, pal.
Alright, So those were the two open agenda items. Were there other things that y'all wanted to talk about before we walked the board and stuff?
**Pawel Filipczak** 15:26 So, Servio left elastic, so that's… that's…
**Bob Strecansky** 15:29 Whoa!
**Pawel Filipczak** 15:30 Good news, so… Maybe he'll contribute, maybe not, we'll see, but… Right now, we lost one of the contributors, and so I'm alone.
So we'll see what will happen in the future, but so… so far, I… I'm not living.
**Bob Strecansky** 15:50 Oh, man. What, did he leave voluntarily?
**Pawel Filipczak** 15:55 I'm not sure about that, so… Maybe… maybe I… I… I wasn't able to contact him, because he left when I was on vacation, so…
**Bob Strecansky** 16:04 Oh, no!
**Pawel Filipczak** 16:05 And when I came back, I just got the news in the morning that he left, so unfortunately.
I'm not sure what's the… I don't know what was the reason.
**Bob Strecansky** 16:17 Got it.
Did you have a good vacation?
**Pawel Filipczak** 16:20 So, yeah, it was… it was nice and good. I was… I… I came back Tired?
I mean, physically, but… Mentally, I recovered, so yeah, it was very nice.
**Bob Strecansky** 16:33 Where'd you go?
**Pawel Filipczak** 16:35 I was in south of Poland, I was visiting mountains, caves, Mining factories, and yeah.
**Bob Strecansky** 16:43 Wow, that's cool.
**Pawel Filipczak** 16:45 Yeah, yeah.
I wasn't in the high mountains, in the medium ones, but the views are still outstanding.
It's Helazian District.
So…
**Bob Strecansky** 17:00 The what district?
**Pawel Filipczak** 17:01 Silaziano.
**Bob Strecansky** 17:03 I don't know how to spell that, you'll have to give me some…
**Pawel Filipczak** 17:05 S. E.
as I… as I… I'll, I… as… Jeez.
**Chris Lightfoot-Wild** 17:14 That's A.
**Pawel Filipczak** 17:15 Yeah, I'll put it on chat, like…
**Bob Strecansky** 17:18 Yeah, that might be easier. That might be easier.
Even though I have a… even though I am of Polish descent, my Polish is zero, so…
**Pawel Filipczak** 17:32 Yeah, I put the names on the… On the… on the chat.
The tetra, the mountains are higher.
**Bob Strecansky** 17:43 La la.
**Pawel Filipczak** 17:43 Must be. Yeah.
**Bob Strecansky** 17:47 That's some… Look at that!
Nice. These guys?
Man, I can see why you need a vacation from your vacation. These look like some pretty steep boys.
**Pawel Filipczak** 18:00 Yeah.
For a nice rocks, you can put the last name. It's called Strelin, it's weird.
So, it's, it's, it's, it's a very beautiful place.
Man, it's a nice trail.
**Bob Strecansky** 18:17 Do they have good food in these places?
**Pawel Filipczak** 18:20 Yes, it's a mix of Polish and Czech, so because it's on the display, it's on the border of Czech Republic.
So, it's a mix of German, Polish, and Czech foods. So, yeah, it's… it's, you know, it's powerful.
Paintful food, so… You are… I get a lot, and I got a lot of energy, so…
**Bob Strecansky** 18:47 Good.
**Pawel Filipczak** 18:47 I need…
**Bob Strecansky** 18:48 I need… I need to discover more Polish food. My Polish food encyclopedia includes pierogies and halopkes, and that's about it. I need to learn some more.
**Pawel Filipczak** 18:58 Yeah, but you shouldn't… you shouldn't spell Pierogis.
Because it's already, it's already, plural, right? So it's a… it's…
**Bob Strecansky** 19:09 Oh, you just said pierogi.
**Pawel Filipczak** 19:11 You're on me, exactly.
**Bob Strecansky** 19:13 Good to know.
That shows my ignorance, I guess.
Alright, let's… Let's walk some repos.
I feel like, Bob… do y'all… are y'all familiar with… The Price is Right, the TV show, or no?
There's this famous game… there's this famous game show in the United States called, The Price is Right, and the host would always go, come on down, to have people… Alright, looks like I gotta do some renovate stuff. I gotta merge some of those, and I'll work on that, hopefully this week.
Is there anything in… I gotta… we gotta review some.
**Pawel Filipczak** 19:57 I reviewed one, there is Carol, the fourth or fifth from the, from the top.
**Bob Strecansky** 20:03 Okay.
**Pawel Filipczak** 20:03 So, it's okay, so you can, you can merge it.
**Bob Strecansky** 20:07 Okay, I will take a look at that later today in the merge.
And then… yeah, a lot of these are just renovate, so I'll probably slap through those sooner rather than later.
And then, instrumentation, there's a couple, and they're probably just… Oh. This one has…
**Chris Lightfoot-Wild** 20:28 But I think that's the one we're trying to assign Pawel to.
**Bob Strecansky** 20:31 Oh, yes, yes, yes.
**Chris Lightfoot-Wild** 20:32 You could try again now, in case it works on this repo, but… Nope, nope.
That's a beauty.
**Bob Strecansky** 20:42 This is… no, this is a different… this is a different PR.
So I tagged that one.
**Chris Lightfoot-Wild** 20:47 No, that was an issue.
**Pawel Filipczak** 20:49 Yes.
**Bob Strecansky** 20:51 I tag, attacking in the issue. Got it, okay.
Alright, and then the distro has some pull requests open.
**Pawel Filipczak** 21:01 Yeah.
**Bob Strecansky** 21:02 Anything in here that you need me to review, pal?
**Pawel Filipczak** 21:05 Not now, so I'm just reviewing everything.
**Bob Strecansky** 21:10 Almost at 50 million, let's go!
Gettin' there. Getting there, boys.
Alright, I think that's all we got for today. Y'all have anything else to talk about?
**Chris Lightfoot-Wild** 21:22 The backlog, I did pull up… can we just open that in a second, sorry. I did put a couple of things, or pull it through, at least. I don't know if that was something we wanted to…
**Bob Strecansky** 21:33 The backlog… are you talking about this project board?
**Chris Lightfoot-Wild** 21:36 Yeah, sorry, yeah.
**Bob Strecansky** 21:37 Good.
Come on.
Come on, GitHub. They've been having some real problems lately, huh?
**Chris Lightfoot-Wild** 21:49 Yep. Sort of, seems to be less reliable.
Down more than it's up.
**Bob Strecansky** 21:57 Well, I might not be able to see this board, so let's try it, let's figure it out.
There we go.
Okay.
**Chris Lightfoot-Wild** 22:07 Cool, so… I guess, should we… This was your, thing a while ago, Bob, like, is it… how do we get stuff out of done to, like… I guess we're not working in, like, a sprint, but, like, how do we say.
**Bob Strecansky** 22:20 Oh, good question.
**Chris Lightfoot-Wild** 22:21 Let's get rid of them.
**Bob Strecansky** 22:25 do this? Unda, yep. There we go.
Nice. It's adding… Looks like we can continue to move forward. I gotta do this response body size limitation PR again.
At some point.
**Chris Lightfoot-Wild** 22:40 Yeah, there's a couple of also… so I did actually have another thing then, We've got a lot of older PRs.
But in the past, I thought we had, like, a stale bot that was going through.
**Bob Strecansky** 22:52 We did, I wonder what…
**Chris Lightfoot-Wild** 22:54 And then following up on having the moto closed, if it's so old.
**Bob Strecansky** 22:59 I wonder what happened to that, because I do remember… I very vividly remember that the… Stalebot, or whatever.
**Chris Lightfoot-Wild** 23:06 I think it's similar to what Severin said, it takes away that, like, human aspect of…
**Bob Strecansky** 23:10 Yeah. Like…
**Chris Lightfoot-Wild** 23:11 Feeling guilty about having to remove someone from something.
**Bob Strecansky** 23:15 This is not in action… Show my workflows… There's more… still… I don't see one.
But… maybe we have to do… Cncf sale bot…
**Chris Lightfoot-Wild** 23:38 I mean, there's a stale YAML file in the .github repo… sorry, directory in the repo, but… Yeah, I'm not sure if that was… Some app that was in the org that was… Who written these up or something, or…
**Bob Strecansky** 23:55 Yeah, let's see if we can find where steel.yaml is referenced anywhere, if at all.
It's just, Okay, so I bet we just need to add…
**Chris Lightfoot-Wild** 24:17 Workflow back.
**Bob Strecansky** 24:19 Let's see, okay.
Okay, so let's see if I can do this…
**Chris Lightfoot-Wild** 24:28 So I guess that… do we think then we should… we should reinstate that, if that's…
**Bob Strecansky** 24:33 Oh, yeah, I think… I think that that's something that, I think that's something that we…
**Chris Lightfoot-Wild** 24:41 Yeah, I was in, like, contrary, even from, like, Cedric from, you know, quite a while ago now. Yeah.
And I guess the chances of them coming back to life are less likely than just having their auto clothes and…
**Bob Strecansky** 24:55 Yeah.
Yeah.
Alright, let's see… Compression issues, right?
Let's give it a go.
**Chris Lightfoot-Wild** 25:23 Does that repo have a still… Yamblin as well, I know.
**Bob Strecansky** 25:28 Which one? Contribute.
**Chris Lightfoot-Wild** 25:31 Pondrip does, but does this one as well? I don't know.
**Bob Strecansky** 25:34 Yes, I believe it does.
**Chris Lightfoot-Wild** 25:37 Okay.
**Bob Strecansky** 25:39 I think that's what I clicked on.
Yeah.
**Chris Lightfoot-Wild** 25:45 So if it works in this one.
**Bob Strecansky** 25:47 Oh, no.
**Chris Lightfoot-Wild** 25:51 What's up?
It's true.
**Bob Strecansky** 25:53 There's an error committee interchange. File could not be edited.
It is on the description.
Hmm… there we go.
We'll give that a go here, and if it works, we'll do it on the other repost, too.
Thank you for bringing that up, Chris. I don't know… I want to know where that went. It just, like, disappeared. Maybe they did some sort of… I bet you they did some sort of migration with, repos and… And… got removed.
**Chris Lightfoot-Wild** 26:32 Yeah, there's only one other thing then, sorry, that I've seen you'd added in the channel as well, Bob, about the distro approvers in that group.
**Bob Strecansky** 26:41 Oh, yeah.
**Chris Lightfoot-Wild** 26:42 Looks like the hierarchy is different for that group, it's like a standalone.
one, but I guess if you ask… To want to add you into the group.
Unless Pawel can only do it.
**Bob Strecansky** 26:52 I don't know if you can or not.
**Chris Lightfoot-Wild** 27:01 Because what are the… Merge requirements on the distro repo.
Can you merge your own stuff, Pawel, or does it need to…
**Pawel Filipczak** 27:13 No.
**Chris Lightfoot-Wild** 27:15 Okay.
**Bob Strecansky** 27:17 We're… yeah, we're… I gotta look back.
**Pawel Filipczak** 27:19 I have to update. I will add you to the approvers. I thought I added you, Chris, already, but I'm not sure I will… I will check that.
**Bob Strecansky** 27:29 Sounds good.
**Chris Lightfoot-Wild** 27:30 Yeah.
**Pawel Filipczak** 27:31 I also… I also tried to add myself to them as members to other repositories, so I mean the SDK as a reviewer.
**Bob Strecansky** 27:39 Whoa.
**Pawel Filipczak** 27:40 Let's say, but I'm not sure if someone should take a look into that or not, so maybe… maybe you got some notification.
**Chris Lightfoot-Wild** 27:50 When you say the SDK, what do you mean, like, the… not the split, not the subtree?
**Pawel Filipczak** 27:56 I… I'm… I'm in the… I'm in the contribository, but I cannot approve any other repositories than… than contributors, but…
**Chris Lightfoot-Wild** 28:08 Okay.
**Bob Strecansky** 28:12 Let me see if I can add Jude to that or not.
No…
**Pawel Filipczak** 28:17 They… there are those groups, you know, in the… somewhere, so the teams are defined somewhere, and I… I just click to… there to… to include me, or…
**Chris Lightfoot-Wild** 28:28 If you go to the OpenTelemetry org, there's a team section.
**Pawel Filipczak** 28:32 Yeah, yeah.
**Bob Strecansky** 28:34 Oh…
**Pawel Filipczak** 28:36 It was a few weeks ago, so I don't remember.
**Chris Lightfoot-Wild** 28:41 It's just a PHP sort of song, yeah.
**Pawel Filipczak** 28:45 Yam.
**Bob Strecansky** 28:46 Just take a look at all of them, see what's going on.
Alright, one pending.
**Pawel Filipczak** 28:52 General.
**Bob Strecansky** 28:53 That's you, I approve.
**Pawel Filipczak** 28:58 So, yeah.
Double, like, number.
**Bob Strecansky** 29:05 Yeah, congratulations!
Alright, you should be in there now.
Contribute provers, you're there… Php contributors…
**Chris Lightfoot-Wild** 29:20 Yeah, Jerry, I don't know if you've seen, sorry, Jerry, accepted being a pondrip for the code owner's workflow?
**Bob Strecansky** 29:26 That's it, I did see.
Okay, so I requested being a distro approver and a distro maintainer.
And then PHP maintainers, just me and Brett.
Triagers are in three of you, and there you go.
That's it.
With PAL, remember, with great power comes great responsibility.
**Pawel Filipczak** 29:53 Yeah, and you cannot assign the issues to me right now.
**Bob Strecansky** 29:57 That's right.
**Pawel Filipczak** 29:57 I guess.
It will be easier.
**Bob Strecansky** 30:00 Great power comes great power.
**Chris Lightfoot-Wild** 30:05 Is that worth trying again, then? Does it actually work now, that you're in the group?
**Bob Strecansky** 30:08 Okay, good question. I can do that and go.
**Chris Lightfoot-Wild** 30:11 We've tried to end the meeting about 5 times, Boba.
**Bob Strecansky** 30:13 No, no, no, you're good.
**Chris Lightfoot-Wild** 30:14 Stop talking.
**Bob Strecansky** 30:16 No, you're… I, let's go take a look… I'm not… you're… I'm not trying to end the meeting, I just… I don't like… Doodling if we don't have to, but… Let's see… is this this one?
Intuit face. Look at that? Look at that!
Welcome to the jungle.
**Chris Lightfoot-Wild** 30:41 Cool.
**Bob Strecansky** 30:45 Alright, for real this time. We'll see you all next week.
**Pawel Filipczak** 30:50 Cheers, though.
**Chris Lightfoot-Wild** 30:50 Hello.
