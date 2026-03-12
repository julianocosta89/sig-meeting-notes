SIG: FAAS WG
Date: 2025-07-17
Duration: 18 minutes
============================================================

## Zoom Recording Transcript

**Tyler Benson** 02:26 Hello! Hello! Good morning, and good afternoon.
**Serkan Ozal** 02:32 Hello!
**Tyler Benson** 02:42 I guess it's more. Good evening for you, Sorkin. Right.
**Serkan Ozal** 02:45 Yeah, it is 6 pm. And I just picked up my son for from Sekul. And then he's yeah. Just came back to to home for the for the meeting, and there was other meetings just after this one.
**Tyler Benson** 03:04 You guys have a school even during the summer like this.
**Serkan Ozal** 03:08 Actually, it is kind of practical, and then it goes, I mean, 20 degrees until the 6 pm.
Here.
**Tyler Benson** 03:16 Got it.
It bogged in.
**Bogdan** 03:22 Hello!
**Tyler Benson** 03:23 Thanks for joining us so early.
**Bogdan** 03:26 Yeah, okay, so shall we start.
**Serkan Ozal** 03:31 Yeah, I think so.
**Tyler Benson** 03:32 Sure Cirken said, that he has a hard stop at the 30 min. So we're gonna try and keep this one short.
**Serkan Ozal** 03:45 Yeah, actually, you guys, I mean, still, continue not sure whether anyone will be joined to Rory or Ivan or or Max.
But I will have to have to leave. I mean, just 6 and a half. Pm, I mean my time.
okay. Do you have any agenda or topic to discuss.
**Tyler Benson** 04:13 So I was gonna say, thank you for doing the the layer releases.
**Serkan Ozal** 04:19 Yeah, sure, no. Problem.
**Tyler Benson** 04:26 The other thing I wanted to mention is, we've got a couple of security vulnerability reports that were recently resolved. And the What's his name from the Tc. Was asking if we should report those as Csv. Or as vulnerabilities.
And I was gonna ask what you thought about that?
Cves. Sorry, not Csvs.
**Bogdan** 05:10 Well, I mean, if if there are critical we should we should report them.
**Tyler Benson** 05:21 So I to me it doesn't seem like they're that critical.
But I'm not really a go expert. So, and they both relate to going, and the collector.
**Serkan Ozal** 05:39 As far as I remember, the the vulnerability I mean was marked as critical, I mean, according to the collector things. But since we are running. Actually, I'm not sure that is really applicable for for our case. It might or might not be, because, you know, we are running the collector, I mean, as a kind of I mean intermediate component between the SDK and the remote, remote target so that might change the level of the vulnerability for our use case. But I'm not sure on that. So. But if it's critical I'm not sure. I mean how we can. I mean report. Those could up that critical vulnerability to.
**Bogdan** 06:25 Yeah, okay, I I will take. I will take a look at that. But I have a question before that was this vulnerability in our code? Or was a 3rd party dependency in the collector that had a vulnerability.
**Serkan Ozal** 06:37 3rd party.
**Tyler Benson** 06:38 I believe I believe they are both 3rd party vulnerabilities.
**Serkan Ozal** 06:42 Yeah. 3, rd party.
**Bogdan** 06:43 Then we don't. Then we don't have to report it. We just we don't have to report them. It's just like we have to mention in the release that we fix the the vulnerability because that that was already reported correct. If it's 3rd party.
**Tyler Benson** 06:59 Yeah.
**Bogdan** 06:59 Yeah.
So if you resolve a 3rd party vulnerability, you just in your release notes you. You explain that that was solved. And we had that problem, but we don't have to re-report it.
**Tyler Benson** 07:13 Okay, that's good.
So do you want Bogdan? Do you want to take a look at the vulnerability reports and and comment on there.
**Bogdan** 07:25 Yeah, but let's not discuss them in public, since we shouldn't discuss them unless there are whatever. You know, there are some rules about that. So.
**Tyler Benson** 07:35 Yeah, that's fine.
**Bogdan** 07:36 Okay. Okay, send me. Send me the link in a private DM, and I'll take a look at them.
**Tyler Benson** 07:42 Okay.
**Serkan Ozal** 07:44 By the way, by a 3rd party I mean, it was related to the goal lines, I mean Wilton libraries built in modules.
So it was not a kind of I mean
**Bogdan** 07:57 Yeah, it was in the go, go, 1, 4, 1, 24, 3, or something had. Yeah, I know, I know.
Okay.
**Tyler Benson** 08:12 So that was a bit that was about all for me. I don't think I have a whole lot else to add.
Serkin, did you have any topics you wanted to discuss.
**Serkan Ozal** 08:28 actually, I don't have any. I mean important topic to discuss here. The only topic I want to mention is that you know. After we upgrade the upstream Js repository package versions. There was some breaking change in the for the node Js layer and trend from from the Gs. Javascript. Seek helped us to to fix that issue. But still before release, I believe that we need to introduce the configure logger function as a replacement or as an alternative to the existing configure. Logo provider. I think I mean Tyler. You already know the know, the discussions on that.
**Tyler Benson** 09:19 Yeah.
**Serkan Ozal** 09:20 I will be merging the trends. Pr.
I just rebase before the meeting. And yeah, it's okay. And I will merge that. And then, I think, before the release before the next no Gs later release, we should introduce the configure logger global configure logo function to allow users to be able to configure the logo provider. Because I mean they are local providers, because through the logo provider they will not be able to add the log processors, but through the logo config that is the the only item I have.
I am planning to send a Pr. For that a small Pr to to add that new global function for for customizing the loggers, and other than that I don't have any topic to discuss.
**Tyler Benson** 10:23 Okay, I I think that's a fine approach, the other. So if you are all already doing planning on doing that, that's great. Otherwise you can also see if any of the other contributors want to work on that
**Serkan Ozal** 10:38 Yeah, sure, I mean, I cannot.
Yeah, I cannot worry, because they are familiar with Javascript, too.
I cannot ask them.
**Tyler Benson** 10:48 So I mean, it all just depends on how much you're available for. But anyway.
sounds good. I I'm I'm good with that. I didn't realize that the the author of that Pr was a Javascript Sig contributor. So that's good.
**Serkan Ozal** 11:08 Yeah, he's from. He's from Trent. Yeah.
**Tyler Benson** 11:13 Okay.
**Serkan Ozal** 11:13 Yeah, yeah.
I have been talking with with him. I mean months ago, very much while working on the cost of optimization. So I know him from from those days.
**Tyler Benson** 11:24 Awesome.
Bogdan, did you have anything you wanted to bring up?
Our meetings are generally pretty quick, and unexciting.
**Bogdan** 11:43 Okay. No, no, I don't have anything. One thing I I need to know from you guys is, if you need any help from DC members or from from notification, so that I can prepare for it.
**Tyler Benson** 11:58 Yeah, sure. I think we've been pretty independent, and you know, pretty stable for a while the main thing that we are hoping to get is more contributors. More people to approve. And review prs, and such.
**Bogdan** 12:24 Okay, I will try to to help with that and see if I can find other people, or I can do by myself. Okay.
**Tyler Benson** 12:31 Yeah, I mean, I think the main thing is our Sig requires a pretty diverse experience background in languages. Since we've got several different implementations.
So I think we've we're kind of lacking a little bit on the going expertise side. So if that's an area where I know we get a lot of stuff coming up on the collector side. So having people that can help out with the collector stuff would be beneficial.
**Bogdan** 13:06 I know somebody.
**Tyler Benson** 13:08 Awesome. Sarkin, do you feel like there's any other big gaps that we need help with.
**Serkan Ozal** 13:16 No, I think, yeah, you are right. I mean, I mean, mostly we. We are lacking because of the bowling experience.
Just we have, Max, and but I'm not sure I mean how much time he can. He can, I mean, put his efforts for the for the going support. I mean the collector support but we me Tyler, and mostly Java person, and also I have many nodes experience. But for the for the Golank we don't have much, much experience on the on the current team.
**Tyler Benson** 13:52 Do you feel like we have enough python experience.
**Serkan Ozal** 13:57 I don't have, I mean, of course I know.
**Tyler Benson** 14:00 That would be another area where I feel like we're probably lacking a little bit, is python.
**Serkan Ozal** 14:05 Yeah, but.
**Tyler Benson** 14:09 I think that comes up as much as as going.
**Serkan Ozal** 14:13 Yeah, hopefully, I mean, fortunately there, there's not. There are not much.
I mean issues or feature requests reported by the committee for the for the python. So I think that is the reason that why, I mean, we didn't see the python experience issue so far. But you know, for the collector.
There are many, I mean bugs, and the feature requests are reported. And also the another point is that for the collector we have the cold start issue, you know. And there might be a few approach. We can. We can. We can follow to reduce the call, start overhead, because, even though we we reduce the call start overhead of the sdks of the layers itself, but still the collector itself has 300 and more, depending on the configuration call start delay. And and yeah, reducing such close art probably require some deeper goal. Go expertise.
**Tyler Benson** 15:18 Okay.
Anything else. Bogdan?
Okay. Yeah.
Sorry.
**Bogdan** 15:34 No, I was muted. I was saying, Yeah, that's that's good. I I know a couple of things where I can try to help. So that's good.
**Tyler Benson** 15:42 Great appreciate the help.
but otherwise I think we can end the meeting early today. There's not a whole lot on the agenda, so.
**Serkan Ozal** 15:54 Yep.
Okay.
**Tyler Benson** 15:58 Have a great day, everyone, and we'll see you in a couple of weeks.
**Serkan Ozal** 16:02 Yeah, bye.
**Tyler Benson** 16:04 Bye.
