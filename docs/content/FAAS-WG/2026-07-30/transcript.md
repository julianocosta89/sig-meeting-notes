SIG: FAAS WG
Date: 2026-07-30
Duration: 14 minutes
============================================================

## Zoom Recording Transcript

**Raphael Manke** 03:47 Boom.
**Warre Pessers** 03:57 have to, find out how to click the bot again, but otherwise…
**Raphael Manke** 04:04 chat. There was, like, a chat message that you can put in to kick off.
**Warre Pessers** 04:11 Yeah, I remember, last time I mentioned something about it, the bot put it in the chat himself, but I can't seem to, Get him to do that right now.
I guess it'll stay for now.
**Tyler Benson** 05:44 Nice. I was just gonna boot them, but…
**Warre Pessers** 05:48 Yeah, Apparently, after some time, the bot puts in the overview of the command, so I was able to get him to leave. It's very annoying that we can't just permanently block them, but…
**Tyler Benson** 06:04 Yeah, I assume… So you know how the, the, other SIGs are starting to adopt this Linux Foundation login system?
I'm betting that that's gonna help, with the… The bots as well.
**Warre Pessers** 06:24 Yeah, I guess. Makes sense.
Not sure if you're waiting for anyone else, so I guess I'll just get started.
Oops, apparently Zoom needs permissions again. Yeah, so Tyler actually, he notified me yesterday, because I indeed had promised I would be doing a, release, but, it's been very busy at work, and also, Hi, Serkan. We were just getting started.
**Tyler Benson** 07:07 I think this is, like, the first time in a long time we're all actually meeting together.
**Warre Pessers** 07:12 Yeah.
**Tyler Benson** 07:13 It's been a busy summer.
**Serkan Özal** 07:15 Yep.
**Warre Pessers** 07:16 Lee.
Yeah, but so, as I was saying, this evening and tomorrow in the afternoon, I also have a day off, so I'll be, Trying to get the release done, should be… should be fine.
And then I'll obviously let you know when it's done. Other than that, I really haven't been able to spend that much time looking at open PRs and stuff like that, but as I said, I'll get, I'll get to it this evening and tomorrow.
And yeah, there's not really any big, efforts or whatever, that I'm currently working on. The, SQS context propagation stuff, it is in the… Javascript instrumentation library right now, so it will be part of the next release.
Yeah.
basically that.
**Tyler Benson** 08:17 Has much changed in the release process, in terms of, like, Besides just, like, cutting the tag and having it automatically build and push the images?
**Warre Pessers** 08:32 Not really. That's all, remained the same. So, the integration tests that we introduced, those are just… for now, still manually, you have to trigger them manually. Just in the GitHub UI, you can easily… can, Or, yeah, you're probably all familiar with GitHub, I suppose I don't have to show this… Or is anyone interested, to see?
**Tyler Benson** 08:59 I assume there's just a workflow that you can trigger manually?
**Warre Pessers** 09:03 Yeah, exactly. So, if you do that, the integration tests will run you can check out the results, and then if everything's good to go, it's basically the same process I did manually, in my own AWS account before. It's not 100%, airtight, or I don't know if that's even a correct English, but…
**Tyler Benson** 09:27 That works.
**Warre Pessers** 09:28 So, but it's a best effort for now, so it's just a quick check you can do before, releasing, but the… just pushing the tags is… it's still the same system.
But we don't automatically trigger the integration tests on pushing a tag yet, so you do have to run them manually if you want to.
**Tyler Benson** 09:51 How long do they take to run?
**Warre Pessers** 09:54 Takes a couple of minutes, because it sets up some infra, and then it destroys it again, so…
**Tyler Benson** 10:00 10 minutes, that's fine.
**Warre Pessers** 10:02 Yeah, it's not that long.
There is one thing to be aware of, though, if any of you would be running these in the future, because I suppose it will be me for the near future, but… the Ruby layer, it's… I opened an issue for that, and someone is working on that. It's only being released for, like, the layer is only built to work on the AMD architecture. What am I saying? Yeah, yeah.
So the integration tests for the ARM architecture, it will always fail, but someone is working on that, so that's just a… false positive for the moment, but it… yeah, that's something I coincidentally found, that we apparently, don't support ARM for the Ruby layer.
So I'll just, let me just copy this stuff, and then, I'll put in my… action item, which is that I'll be doing the release.
**Tyler Benson** 11:16 You can just type at today, and it'll populate today's date.
**Warre Pessers** 11:20 Oh, really? I didn't know.
Good to know.
So… So, not sure if anyone else, has any items to discuss today.
Me neither for now.
**Serkan Özal** 11:52 Yeah, actually, I don't have anything to… I mean, as we're working… working on, but if there is any help needed from my side, or… or any PR to be received by me, just let me know, so I can just check it, but… yeah.
**Warre Pessers** 12:10 Will do. Thank you.
**Raphael Manke** 12:12 I think one of my PRs got pinged, regards a contract for the cloud account ID, and this thing that we are extracting from the extension and setting it in a temp variable, if we have some documentation or contracting for that.
The only thing that I'm aware of is the contract of the extension API from Lambda that is setting this value, so that's the reference I can give. And then the extension itself, who's implementing this feature of setting it. These are the only two angles I can see as a contract.
And… the bigger question is, where should I put that? This documentation, or this contract thing… thing?
**Warre Pessers** 12:59 Do you remember? It's probably this one, then I guess, the cloud account ID… resource.
**Raphael Manke** 13:06 and guesses.
I need to check my notifications, otherwise.
**Warre Pessers** 13:11 Wait, or maybe it's the other one.
Is it this one?
Because the other one was also something with the AWS account ID…
**Tyler Benson** 13:23 The other ones are all draft.
**Warre Pessers** 13:25 Yeah…
**Raphael Manke** 13:27 I need to clean it up.
**Warre Pessers** 13:32 Yeah. I'm… I'm not entirely sure, what exactly, you mean without seeing it, but maybe you can just, drop it in Slack if you find it again. Or was it a comment from Serkan maybe about the documentation?
**Raphael Manke** 13:52 I see if I can find it real quick.
Should be in the inbox… I need to check.
**Warre Pessers** 14:14 Yeah, that's fine, just whenever you get the time, you can let me know, and I'll take a look.
Right? If there's nothing else for today, I think we can… Wrap it up already.
Okay, then, guess I'll talk to you later.
**Serkan Özal** 14:45 Thank you.
**Tyler Benson** 14:46 everyone.
**Serkan Özal** 14:47 Take care. Talk to you.
**Warre Pessers** 14:48 bye.
**Tyler Benson** 14:49 Bye.
