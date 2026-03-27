SIG: FAAS WG
Date: 2026-03-26
Duration: 12 minutes
Zoom Recording URL: https://zoom.us/rec/share/FlcOlrWLzzeqdUvaGKzvTvWxwEpKGXODulWnV_hcPDu0ukU9QE7541IfGOTV2agi.h0SfUhYr-A8dCy8P
============================================================

## Zoom Recording Transcript

**Maxime David** 00:34 Hello, hello!
**Warre Pessers** 00:38 Hello, good morning or afternoon, wherever you are.
**Maxime David** 00:43 Yeah, it's 11am here, so…
**Warre Pessers** 00:45 Okay.
In that case, good morning.
**Maxime David** 00:49 Yeah, what about you?
**Warre Pessers** 00:51 Here it's 4 o'clock, 4PM, so… Awesome, noon.
Not sure who exactly… is going to join. I'm suspecting Lucas will be here.
**Maxime David** 01:12 Yeah, let's wait maybe for a couple of minutes, and then maybe we can… we can start.
**Warre Pessers** 01:17 Yeah, exactly.
**Maxime David** 02:19 Hey, Tyler.
**Tyler Benson** 02:22 Good morning!
Or good afternoon.
**Maxime David** 02:28 Yeah, morning for me.
**Warre Pessers** 02:31 Afternoon for me, yeah.
I'm just going to wait one more minute for Lucas, maybe, but I'm not 100% sure that he'll be here.
Hello, Lucas.
I guess, we can kick off the meeting then. Let me share the… Document real quick… I see Serkin has joined us as well.
Hi, Serkin.
**Serkan Özal** 04:00 Hey, Rory. Hello, everyone.
**Warre Pessers** 04:05 Alright?
I don't have much to discuss, just one very minor, thing I was taking a look at, because I've been looking at the security advisories on our, repo, and I saw that some of them originated also from the sample app.
which, we could opt, of course, to just, dismiss them, but I think we can just let Dependabot automatically fix them. But then one thing I ran into was, the current setup, I think I'm sharing my full screen, right? Yeah. So… the way this is set up is, it's like, using NPM workspaces, so we actually have the root lock file, and then we have, two separate workspaces, but the log file is supposed to be used for both, but I found it quite curious that the… Sample app.
workspace had its own log file, so I was just going to quickly check here if you think it's okay for me to just remove this, because you usually don't need separate log files when you use NPM workspaces.
So, if there's no…
**Tyler Benson** 05:35 reasonable to me. I don't have enough experience to really… Weigh in here, so…
**Warre Pessers** 05:44 Yeah, I'll just open the PR right after this meeting, and then attach the NPM docs, and then maybe tag some people, like Ivan maybe is also, got some NPM knowledge, so then those people can maybe give it a quick look, but should be, fine to go ahead with that, and then… Other than that, I have been looking at some of the issues that are open.
**Maxime David** 06:14 Just before we jump into the issue, if I may suggest, maybe we should, if we agree to remove that package lock in the sample app, maybe we should add it to the Git in your as well, otherwise it will pop again. I suspect it might be a mistake when someone is just npm installed directly in the sample app, package lock will be generated, and then it will be committed.
So if we want to avoid that in the future, we might want to add it to the .gitignore file.
**Warre Pessers** 06:44 Yeah, that's a good idea. I'll, I'll do that. That's a great idea, actually.
Okay, and then, yeah, I don't have much to say about the issues, but I'm slowly, like, working my way through them. Some of them are still relevant, some of them aren't. We've also been merging quite a lot of PRs the past two weeks, so some movement there as well. And then, as I said, I'm looking into the security advisories on my enterprise counts, apparently. But I'm also slowly, but surely, working my way through them. Yeah, this GitHub Enterprise setup is, A little bit annoying, so… No showing, right now, but yeah, just so you know, working on that.
Don't know if anyone else has anything they want to discuss today.
**Maxime David** 07:44 And can we go back to the list of issues, please?
**Warre Pessers** 07:48 Yes, then I'll have to… somehow… Get around this stuff, yeah, okay, this is better. Yeah.
**Maxime David** 07:57 A list of pull requests, sorry.
**Warre Pessers** 07:58 Add the support requests.
**Maxime David** 08:00 I think there is one… so… the third one… add cloud account ID. I was wondering what is the state of this, do we want to spend a bit more time reviewing this? Because I think it's very close to get merged.
**Warre Pessers** 08:18 Yeah, so, Raphael is currently at KubeCon, but I guess he'll be joining us next time, and he's also sometimes, giving some updates, but I believe there is still some work to be done in the, in the language-specific SDKs, but I'm not entirely sure of the status currently.
**Lukas Hering** 08:43 I thought he had mentioned that There was maybe an even better way to do this.
**Warre Pessers** 08:48 Yeah, that's right, yeah.
**Lukas Hering** 08:50 What was it again?
So, I think… Yeah, something with just… this could just be implemented as a resource detector entirely.
**Warre Pessers** 09:03 Yeah… That's correct, yeah. I do remember that he was looking into that, but I'm not sure of the status right now, but I'm expecting an update soon, probably, somewhere after KubeCon, coming week, or… hinting.
**Maxime David** 09:22 Yeah, also at AWS, we just released a metadata endpoint, which currently returns the region and the availability zone, sorry, that the Lambda function is running in, so we might want to tag also this.
**Lukas Hering** 09:39 Oh, is it kind of like the EC2 one?
**Maxime David** 09:42 Yeah, exactly.
Oh, nice. I can…
**Lukas Hering** 09:46 I think this one is more around account ID. Does it have account ID?
**Maxime David** 09:50 No, it does not have the account ID right now, but I believe there will be… I cannot disclose too much information, but I believe we are going to push more information to that endpoint, so account ID might be there as well. I'm not sure about the timeline, I can dive a bit into it, but I'm pretty sure that more fields will be… depending on the customer feedback, more fields will be added to that metadata endpoint.
**Warre Pessers** 10:16 Okay, that's good to know, I think we can… Yeah, as soon as you have more info, you can probably just, interact on the PR.
**Maxime David** 10:30 Yeah, I'll talk to Rafael directly.
**Warre Pessers** 10:32 Yeah, that's great.
Anything else for now? Or related to one of the other PRs, maybe?
I don't have any other things to discuss right now.
If no one else has anything to discuss today, then I guess we can end the meeting here.
I'll check in with Raphael about the status again, and We can look into that metadata endpoint as soon as it becomes, relevant.
Alright.
**Maxime David** 11:13 I add the link of the announcement on the… on the… on the doc, and maybe I'll create also an issue, maybe to tag, spans with the availability zone.
**Warre Pessers** 11:27 Hell yeah.
**Maxime David** 11:28 I don't know if there is a semantic name for this already, I will have a look, I'm not sure. Otherwise, we would need to come with a name.
**Warre Pessers** 11:37 Yep, okay, sounds good.
then I thank you for your time, for attending, and I think we can all go back to what we were doing.
**Maxime David** 11:52 Thank you so much, have a good one.
**Warre Pessers** 11:54 Yeah, YouTube.
**Tyler Benson** 11:55 Good to see everyone.
**Serkan Özal** 11:56 Thank you, buddy.
**Tyler Benson** 11:56 Have a good day.
**Serkan Özal** 11:57 Bye-bye.
**Warre Pessers** 11:58 But…
