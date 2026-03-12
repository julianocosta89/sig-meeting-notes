SIG: .NET Auto-Instr SIG
Date: 2026-02-11
Duration: 21 minutes
Zoom Recording URL: https://zoom.us/rec/share/UxCJJmzEXrCl056sVKtqaN-tDArg-ROa4Pt1IwhfYGl11d5Pl3VnogoxTquazXKF.-l-47O1Zzhssz1O-
============================================================

## Zoom Recording Transcript

**Zach Montoya** 03:51 Hey, everyone.
**Yevhenii Solomchenko** 03:52 Oh.
**Zach Montoya** 03:53 blah, blah, blah.
Guess we should probably get started. I don't want to waste people's time here on the call. Let me, let me start sharing screen, and we can, start going through our agenda.
Alright, so let's see.
I'm starting with our open pull requests… We got a couple of dependency ones. There's a MongoDB one updating the spanning Conventions.
Last I checked.
Looks pretty good, I think maybe just some cleanup there. We don't need to go into that at the moment.
I know that this big one with the result… the resolving the semi-version conflict, is quite large. I haven't had a chance to look at this yet. Hopefully I can get to this by the end of the week, just to start.
So, I know, other reviews would be appreciated.
Yeah, is there any… anything else, Alexi or Ivory, you wanted to mention on this one?
**Alexey Pukhov** 05:17 Yeah, thank you, Zach, for spending time and looking into this. Yeah, I'll be moving this pull request soon, to ready for review.
**Zach Montoya** 05:28 Yep.
**Alexey Pukhov** 05:28 I'm just polishing things that I just must do in it. Then, I mean, obviously, there'll be… probably comments as well. While it's gonna be reviewed, I'll be working on the automation specifically to cover things that I added in this.
Pull request.
But yeah.
Don't have much updates.
Actually, I do have a question. There is a documentation failure in the CI-CD that says that the changelog contains a link that does not exist.
I didn't add this link, so I'm just wondering… Why nobody else's?
**Zach Montoya** 06:12 Oh, in the fishing.
Interesting. It's… it's likely because your PR is stale, because I think we… I think maybe since the time that you opened it, they've changed the macOS runners on GitHub, and we updated ours as well, so I don't think… I'm guessing main doesn't have this anymore.
**Alexey Pukhov** 06:34 Yeah, it doesn't have it. They removed the 13 version, but I'm just curious, what should I do? I keep merging the latest main into my pull request.
**Zach Montoya** 06:44 Oh, that's…
**Alexey Pukhov** 06:44 still pops up.
**Zach Montoya** 06:46 That's insane.
**Alexey Pukhov** 06:47 I think.
**Zach Montoya** 06:47 That's interesting, I would guess that… That would, resolve it, but if not… You could consider… completely, overriding… well… So you're completely overriding that, but, yeah, that's odd that if you've merged main, then… There's no reason that this should still be in your… your brain.
**Alexey Pukhov** 07:20 You know, in that case, I'll check the state of this file on my latest pull request, see if it has this link, because maybe I missed something.
**Zach Montoya** 07:31 Yeah, let's just quickly see what it's… what it shows here.
Oh, yeah, I mean, it shows no changes.
So, yeah, I'm not really sure.
**Alexey Pukhov** 07:48 Bleach.
You know, maybe it'll go away.
**Zach Montoya** 07:54 Yeah, we can… yeah, we can see if it goes away. I mean, if that's… if that ends up blocking the PR, we'll figure it out then.
**Alexey Pukhov** 08:01 Okay, yeah, thank you.
**Zach Montoya** 08:02 Yeah.
**Igor Kiselev** 08:04 I believe what happened, so probably that file has been just recently removed.
So, you first time have seen that issue, but nobody else have yet seen that issue. And, we just have that link in some hour in change log somewhere deep.
inside it, and now, as soon as the files have been removed, you are affected by it. Okay, now our change log is no more… is have a broken link, but it's an interesting question, what we should do with a broken historical link.
**Alexey Pukhov** 08:40 Probably don't make it a link.
But, I mean, it's bizarre, because I believe they removed this… file, like, 4 days ago. How come no one else?
in… in the repository, hit that, because I keep merging latest main, which means someone is merging changes.
**Zach Montoya** 08:59 Yeah, .
**Alexey Pukhov** 09:01 or I guess all the changes that were merged.
**Zach Montoya** 09:04 This one passed the eye, apparently.
It's not running all the… Unless it's not running all the checks.
What was the… what was that job call that failed?
**Alexey Pukhov** 09:25 It's called… .
**Zach Montoya** 09:28 They validate documentation, maybe they're just not running it.
Oh, they're not running it. I think everyone should be hitting this soon.
But we have some logic that determines whether we should check documentation.
**Alexey Pukhov** 09:42 Okay.
**Zach Montoya** 09:43 Alright.
**Igor Kiselev** 09:43 Change document… you change documentation.
Probably not that file, and that's why he…
**Alexey Pukhov** 09:48 I did, I did.
**Zach Montoya** 09:51 Yeah, so this is not… yeah, this isn't gonna be exclusive to you. Whoever… Works on the Nets feature, we'll also hit this, so… yeah, we gotta figure that out.
**Alexey Pukhov** 10:00 Okay, anyway, I'll leave it there until someone fixes it, or if not, then I'll fix it, and closer to the end of the PR, it's still a lot I had to do there.
**Zach Montoya** 10:11 Yeah, sounds good.
**Alexey Pukhov** 10:13 Oh yeah, thank you.
**Zach Montoya** 10:16 Alright, let's see. So yes, we talked about the dependency bumps, this one for the conflict resolution.
And then there's… Igor, you have this one for assembly redirect for non-fault app domain?
**Igor Kiselev** 10:29 So… The only piece admission is intern test, but right now it's on hold, because it would have some merge, with, what Alexis is doing, so I'd like… I don't want to be before he… before him, his pair is much bigger, much touching, much more things, so let's finish with his pair, and by that time I probably have enough time to finish that on-turn test. At the same time, as a principal development finished, if anybody would be able to look and trade and comment, the only thing that's really missing is on-turn test and merge with what RX3 is doing.
**Zach Montoya** 11:11 Got it. Okay. Yeah, sounds good.
And then we still have, environmental op-amp client. I'm not sure if… Rasmus has updated this recently.
Okay Yeah, so Mateo said it's… it's bought, okay.
Yeah, okay, we're waiting on that. Okay.
So it looks like that covers all the current pull requests.
For issues, we have this one that we left open last time.
There's just conversation… With Robert about… how we should add attestations to our release, artifacts. I think the conversation stalled, I don't… I think Pietro was gonna talk to him internally, so I'll follow up.
Within, to see if there's any… Any movement there. But I don't see any requirement at the moment. This is… it's mostly, like, nice to have, so, it's not really blocking anything.
Okay, and then, yeah, if we just go through the rest, we have discussions, nothing, no open discussions, and then… There were no issues on the… For this milestone.
So, the last thing is updating this board, which I think, kind of reflects what's, the current state. So, the big thing that's going on is the semi-version conflicts.
Other than that, we have this MongoDB one in flights.
And yeah, I'm not sure if we're tracking anything else.
At the moment, so, is there anything else that you guys wanted to… to track and commit or put in progress?
I'm not sure there's really any updates.
My end.
**Chris Ventura** 13:06 There was a question raised in Slack, and I haven't had the time to look at it, and it was about, Are all of the instrumentation really experimental still?
**Zach Montoya** 13:21 Yes.
Yeah, where do we document that? Is that… Just our main… Mmm…
**Chris Ventura** 13:28 Yeah, I think it's in Docs…
**Zach Montoya** 13:31 Oh, let's just, yeah, let's just, like, read me.
**Chris Ventura** 13:33 And then configuration…
**Zach Montoya** 13:38 Config? Or…
**Chris Ventura** 13:40 Yeah, one of the configuration Because I think it's in here where we list out… this is our tracing.
**Zach Montoya** 13:49 Instrumentations… Okay, so trace instrumentation says… traces are stable, but particular instrumentations are in experimental status. Oh, yeah, we have all these listed experimental.
I think… For the one… I think there's definitely a subset that we can mark as stable.
Which ones? I'm not actually sure. Are they ASPNotes?
Those ones are marked stable, correct?
**Chris Ventura** 14:27 That's what I don't remember.
**Zach Montoya** 14:29 Yeah, okay, I think we need to… Investigate this.
**Rajkumar Rangaraj** 14:35 Which one? ASPNet? It's, stable.
We did a stable release and added that here.
**Zach Montoya** 14:42 Okay, yeah, I think we can go through… I mean, I would assume that if we're pulling in, stable instrumentation libraries from Contrib, then we can also mark it stable here.
The ones I'm not sure about are our level of… confidence, or, like, what we want to declare, like, bytecode instrumentations, what that bar would be for stable versus experimental, Not sure if we should do some, like, additional review or something to, like, make sure it meets semantic conventions, but I think we could definitely start with the instrumentation libraries.
**Rajkumar Rangaraj** 15:22 That also raises another question. Whatever we have listed, it's… not all of them are instrumentation libraries. For them, few of them, like Azure and all, uses a native instrumentation. We just… we listen to the, just say ad source, and we listen to that.
So, I don't know, what's the approach we should take to handle those scenarios?
**Zach Montoya** 15:50 Yeah, I think this kind of… I would say this also involves a discussion with just SDK, maintainers as well, like… Because I think the explanation libraries, yeah, we can… we kind of… we vet those, but for source instrumentations, or, like, library, self-instrumentations, I don't know what to call it, those ones, yeah, we kind of have to review them. So, I think that would actually be a good conversation with, like, SDK folks as well.
So we're all on the same page about how we mark them.
**Rajkumar Rangaraj** 16:30 Yeah, but because in the SDK, we don't have that challenge. The reason is, both in SDK and Contra, we are not so much worried about the native instrumentation. For example, if there is an Azure Service Bus, or here, something like, I believe, RabbitMQ, is there. So all of them may not have an instrumentation library, and the instrumentation is done as a part of the product itself. I know from an Azure perspective, those are a part of the stable release, which means the stability is guaranteed by the product owner.
So, we need to go and figure out, for each and every product, how the stability is provided, because, SDK has nothing to do with the native instrumentation. The dependency is what we have taken here. SDK is not aware of which are the products even have taken the native instrumentation. So it's purely a problem with the auto-instrumentation than the SDK, yeah.
**Zach Montoya** 17:26 Yeah, yeah, that's a good point.
Yeah, the reason I just mentioned SDK, maintainers, I think, since… Well, both the SIG and the SDK SIG are probably the authorities on, like, kind of providing a stance of, you know, if a library should be used, kind of thing. So… I think we could also mark… kind of give the status of… Like, it's… Provided by the library, and kind of asked for due diligence from or… or say it's, like, based on the library? I'm not really sure.
But yeah, we can indicate that, it's not an instrumentation library from OpenTelemetry, it's from the source product. So… In a way, it's a little bit… like, your mileage may vary.
but some of them we do want to provide out of the, like… I'm sure we probably want to provide out of the box, like Azure, so…
**Rajkumar Rangaraj** 18:29 Probably, anyway, we have a dependency, we have to be careful about bumping the dependency after that, if we give a stability guarantee. For example, if there is a… right now, we have a dependent about blindly going and upgrading all that, and we just do an approval, probably… our department about need to be more strict on the, native source libraries and see, Like, if there are any breaking changes that can bring to the product, and we may need to do… scrutinize those reviews after making… if we are going with that approach.
**Zach Montoya** 19:03 Yeah.
**Rajkumar Rangaraj** 19:07 Yeah, nothing comes as a magic. Everything is included by us, and the libraries are present with us. We can make that decision.
Yeah.
**Chris Ventura** 19:16 Yeah, that's an interesting point, Raj, because… Right now, Dependabot's just bumping the dependencies for the tests… It's not necessarily… Bumping auto-instrumentation's dependencies.
But it's with those test app updates that we see the newer version of the library, which brings the newer version of the instrumentation.
and so, do we need a more robust test definition to ensure semantic convention compliance?
In that scenario.
**Rajkumar Rangaraj** 19:58 Yes.
**Chris Ventura** 19:59 Just a thought.
**Rajkumar Rangaraj** 20:00 It's a thought that needs to be branched on. I see there are, like, maybe this is a topic we can take it forward also with the… getting the other maintenance, like Pyotr and all, taking their decision. This is a topic of discussion to land it in an appropriate way.
If not, we will invade unnecessary supportability issues after making everything that has a stable marking.
**Chris Ventura** 20:24 Okay, I… I'll… Have a takeaway to open up an issue for us to discuss this, and then we can all discuss it async.
**Zach Montoya** 20:36 Yeah, that sounds good.
Yeah, thanks for bringing that up, Raj. And, I think, Chris, you brought up the, the Slack message, so yeah.
Definitely good for us to talk about that.
Cool. Any other topics? I think we've… Kind of gone through our entire agenda already.
Alright, sounds like nothing else for today, so thanks everyone for, for meeting.
Talk to you guys soon.
**Alexey Pukhov** 21:17 Thank you. See you next week.
**efshaikh** 21:20 Thank you.
