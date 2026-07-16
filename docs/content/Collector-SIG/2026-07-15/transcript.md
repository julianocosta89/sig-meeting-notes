SIG: Collector SIG
Date: 2026-07-15
Duration: 33 minutes
============================================================

## Zoom Recording Transcript

**Pablo Baeyens** 00:21 Hello?
**Blake Rouse** 00:24 Hello.
**Pablo Baeyens** 02:58 I guess we can get started.
On the high priority issues,
**Marylia Gutierrez** 03:11 Hey, Pablo, would you mind if I bring my topic? Because I have, like, several meetings that I'm giving these updates, and I have to jump to the next one.
**Pablo Baeyens** 03:20 Sure, yeah, let's do yours first. Yeah, no worries.
**Marylia Gutierrez** 03:23 Yeah, it's just an update about the survey, so I'm trying every, like, 6 months when we got, like… I was like, oh, 6 months is enough to get a few, and then I saw, like, the contributor had, like, 76 replies. I was not expecting that, so yeah, you guys have a lot of contributors. So, yeah, just to give an update in case people don't know, every time, like, non-member merger. Pr, it shows a message like, take a survey just so we can get a sense of like what is working, not working, because we want to improve, like the new contributor experience, how to make things easier. So we do have this running both on the collector and the collector contrib. So for the past 6 months on the collector, we had 8 responses, the average score of 4.4 A lot of the comments of the pros were, like, the… saying that people are being very responsible, maintainers are very helpful, they… a lot of them actually were saying, like, fast reviews and merge, just… a lot of, like, good experience overall, so, congrats on making the… this repo very welcoming to people. Then just a few comments about, like, the more timely review, merges, and then a couple comments of sometimes, like, people saying that they were opening PRs with a strategy, but they didn't get, like, the buy-in from, like, maintainers that it was a good strategy, so they, like, keep going, but then the end, after they do a lot of work.
a manager comes, like, no, no, this other way was better. So they were hoping to get a little more ahead of, like, you should not be doing, like, this way or that way. Just be a little more, like, mindful of, like, the… the… guess the the order strategy, or that they are thinking about like the feature itself.
For the collector contrib, a lot of more repos, 76. Average score 4.25, still a very high, score.
Again, the amount of pros were like, the comments were very similar to the core one. So talking about the constructor reviews and then the good CI documentation, they found a lot of good.
useful issues for newcomers, and yeah, a lot of people saying, like, it was very smooth. And the improvements, it was a very recurrent one, so long time were inconsistent, like, review and merge time, so people were saying that it got approved, but if from approved to actually merge takes a long time, so they don't know, like, what is the etiquette should I be?
Scaling to people? Should I be tagging people?
so they were a little, like, unsure, and they were saying, like, we have a lot of, like, inactive code owners, so even when they attack, they were not responding. There were, like, some about, like, the CLA, but that is not much that we can do on our side, but I just wanted to share here as well. Then about some CI things that are hard to produce locally.
And… Let's see the yeah, the unclear design expectations. That's kind of like similar to the core one.
So yeah, in general is more related. The is is a common between other Sigs as well. It's just like time to review. And I know that now there is a the issue, for at least the collector can trip that issue that shows all the Prs that are open. So waiting for a maintainer just to merge.
or waiting for a approver to, like, review something, and also the ones for, just waiting on the author. So maybe that now is a little more helpful and can help for, like, maintainers and approvers to see what is, like.
really old PR that should be paying attention, and things like that. So yeah, just bringing up this… this, yeah, the results for the past month, so yeah, in general, awesome job, everyone. Thank you for making this very welcoming, and just keep an eye on how we can make things even smoother for people.
**Pablo Baeyens** 07:29 Thank you, Marilia.
**Marylia Gutierrez** 07:31 If there is no questions, then I'm gonna jump for the next one to update them as well. Thank you.
**Pablo Baeyens** 07:38 Good luck.
Okay, yeah, so I was saying for the high priority issues, I… think… From my side… The only update is that I feel like the, or what the big update is, I feel like the Kubernetes Attributes Processor is ready to be marked stable. I'll comment to that effect on the issue… Later this week, but it feels like… The fulfillments are required, and all the feedback I got was Pretty positive. There's some discussion on the an alternative way for the processor to get information from the kubelet, but it feels like after talking with the code owners, this is something that Doesn't need to be done before it's marked as st In any case, if you have any feedback, feel free to leave it on the issue, or or reach out to me. Ideally.
As soon as possible.
No, I'm not sure if there's anything else… worth discussing.
Okay, doesn't look like it's at all.
we can go to.
Evans topic.
although I'm not sure if he's here.
let's jump to the next topic, and I'll ping Evan on Slack and see if he's.
**Mikiyas Bokan** 10:07 I believe the next topic is ours. I think me and Thomas are going to go through this.
Sounds good.
**Pablo Baeyens** 10:15 Okay.
**Mikiyas Bokan** 10:17 Awesome. Okay, let me go ahead and share my screen here.
Okay, so, my name is Mikias Boken. I'm here with my colleague Thomas Baldwin. We're… contributing this specific issue through the Open Telemetry Bloomberg Mentorship Program.
a while back Thomas had presented this specific issue and the solution that we have proposed at the time. But to sort of recap the basic auth extension currently sources credentials from from a file as well as a line from a config. What we're proposing here is to be able to source these credentials or secrets from a cloud-based secret manager, such as AWS Secret Manager.
But… So at the time, the solution that we had implemented was to sort of fake in all this functionality within the basic auth extension, meaning fetching the secret from AWS.
And also refreshing, the secret in case the secret has been rotated, and fetching the latest secret, as well as, maintaining the internals of the AWS Secret Manager there within the basic auth extension.
So while the solution worked, and we were able to get the latest secret without no, collector restart.
The main concern or, like, the main feedback that we, got last time was, the dependency issue. Introducing the AWS SDK dependency within the basic auth, would increase, the binary size for people that are just using the inline config, as well as the file… the file config, and not relying on the AWS Secret Manager, as well as it will increase the CD surface for people that are not using it. So… so that specific solution created a dependency on AWS SDK for people, you know, that otherwise wouldn't need it. And, we worked with Brayden to sort of come up with a solution, who's also, I think a member within this committee.
And the solution that we came across, or, like, we had implemented is to be able to introduce an interface And I'm gonna show this here.
To be able to introduce an interface called secret provider, which has two methods here. The first one is the gate secret method, which pulls the latest secret.
And the second one is the on-chain method, which allows consumer extensions to be able to register a callback method that the provider will later invoke if the secret has changed. So this would be sort of the interface that the AWS Secret Manager will be using to communicate with consumer extensions such as the basic auth extension.
So, as such, the, AWS Secret Manager extension is, like, a brand new extension that we created, which supplies, the secret from AWS Secret Manager, as well as, in case a secret has been rotated, it would invoke the callback function provided from the consumer extension. So that's pretty much what this PR does here.
So… And I guess, on the… from the side of the basic auth extension here. The change that we made here would be one avoiding the dependency on AWS SDK compile time. So pretty much what this, what this PR does is like the basic auth extension would look up the AWS Secret Manager extension, our runtime using the component ID lookup.
That is, I think, that functionality already exists within Autel. So it will look up that extension. It will type assert that specific interface that I showed earlier, and it will invoke the key secret method, and it will register a callback function at a later point in time.
when the secret has changed, that will be invoked by the provider. So that's the change that we made within the basic auth extension. We also did a bit of work to support both client-side as well as server-side authentication methods here.
So, you know, that's sort of the gist for this PR. But, you know, ideally, all in all, I think we managed to remove the dependency on AWS SDK at compile time, just decreasing the binary size. So I guess the reason why we're presenting here is like, you know, we had this discussion with Braden. He was aligned with some of this implementation. I think he roughly looked at the PR.
But we're mainly looking for, you know, sponsorships, so that we can sort of keep this across the finish line. We've been using the… sorry, we've been using the AWS Secret Manager extension, internally.
Within, within my company here, and it's been, like, producing great results, in terms of, avoiding collector restarts, and not losing, telemetry and flight when the secret has rotated.
Hope that helps.
Any questions or feedback?
**Thomas Baldwin** 16:28 One thing we were also looking for is if there's just any general feedback, and one thing Braden had mentioned is, you know, does this make sense to be part of the collector itself?
And if anyone has any feedback on that, we'd be happy to discuss.
**Pablo Baeyens** 16:49 And if it's not part of the collector, what's the alternative? Sorry.
**Thomas Baldwin** 16:55 Well, right now it's in the contribution, repositories being raised, but if it should be raised to the collector.
Libraries.
**Pablo Baeyens** 17:03 Oh, okay, so OpenTelemetry Collector, yeah.
I think a trip is… it's… it's not a big difference where this lives, code-wise, and I think contributes.
Probably.
Better?
Sorry, Tyler, I cut you off.
**Tyler Helmuth** 17:28 I was just going to say thanks for joining and presenting. This looks pretty cool.
This is the right forum for making people aware that this work is happening. So now the next step will probably be people are going to go look at your issue and look through these PRs and hopefully start providing feedback. I can't guarantee that anyone specifically on the approvers or maintainers will end up being a sponsor.
But that doesn't prevent this from being useful. If it ends up — if you're struggling to find a sponsor, definitely take this implementation, host it somewhere. It's still usable by anyone who's using custom collectors and custom — distributions with OCB, still something that you could use at your own. So, yeah, this is really cool, and well done.
**Thomas Baldwin** 18:24 Thank you so much.
**Mikiyas Bokan** 18:25 All right, thank you.
**Pablo Baeyens** 18:40 I guess… I am next again. Yeah, so… quick.
Thing, we are going to change the… Zoom account that… or accounts that we use for this and other Zoom meetings within OpenTelemetry.
I will change the ones for the collector's sake, so this meeting and the other two.
But… Ideally before the next meeting happens, so this is the last one with the old account.
There's… Two differences that are relevant.
One is that the recordings will end up on this link instead of the The usual recording spreadsheet?
And the other one is that you will need to join as a guest or log in into the Linux Foundation platform to be able to join the meeting. You can just log in with GitHub or… something like that. It shouldn't be… too difficult. And yeah, well, if you have copied this event into your calendar.
You'll need to copy it again with the new Zoom link. I'll post on autocollector.dev when I do the update. Ideally, this is very smooth, but you know.
If you run into any issues, just let me know.
And I guess we can move to other now.
**Evan Bradley** 20:27 Alright, so I'm… we talked about this a little while back, but I stumbled on a PR and then an associated issue yesterday, and just wanted to… I guess get an opinion again, and see if anything's changed, or if we just wanna… Stick with the decision from before.
Basically, this is a second issue, so there's another issue where… They were concerned about the same thing, but basically, right now, the… when you export data over the OTLP HTTP exporter.
Whether that… and you get a, like a non-200, code back from whatever the server is, The exporter will only retry the message if.
It falls under, like, a certain set of response codes.
And we're seeing issues where, so this one, for example, somebody has their… whatever their backend is behind a Cloudflare endpoint. And Cloudflare is, you know, it's agnostic for just HTTP connections, and it's not really thinking about Otlp and specific, so it's not going to abide by what the… I think it's with the spec, or the… I think it's the spec, what the spec defines as being a valid retriable error code for OTLP over HTTP.
And in this case, they… don't want to… or they do want to retry, because the Cloudflare error message, doesn't fall within to… doesn't fall within one of the retriable status codes. Previously, we had seen it where somebody was sending data and was getting The sort of error… they were getting a 429 that wasn't… The semantics were slightly different, and they didn't want to retry it.
So the ask in both of these issues is, can we make it so that the status codes, or the ones that are considered valid for retrying, are configurable?
We kind of determined that we'd like to push back on that and see if people.
want to… or are able to tweak their system somehow to change this. With this one, though, in particular, since it's a cloud provider, I think it's a little less feasible. You'd probably have to put some kind of proxy that would Do these translations, and at that point, I'd say just configure it in the collector, but I wanted to get opinions from others about whether, making this, the set of retriable status codes, configurable is something that we're open to, or whether we'd like to, push back here.
**Blake Rouse** 23:18 I mean, from my perspective, I would see… I think this should be configurable, as I think you're seeing Andrew say, as well, from our side at Elastic. I know we have cloud proxies and stuff in between the collectors, and… making this configurable.
Would be very helpful.
For a lot of different situations that are just, like, sometimes not in your control.
When you don't have, like in this case with Cloudflare, you don't have control on what's response codes.
it might return.
So I think just to me, I look at it like a like an escape hatch.
Like, when something doesn't work exactly right, it's just this escape hash that allows you to adjust those retry settings. I mean, obviously, ship with the best defaults, but giving these escape hatches for people to adjust their configuration, I think, to me, is better than you know.
I mean, they're in this situation here where, you know, they're probably not going to be able to get Cloudflare to change that behavior, because it would affect all their customers, so… Like, without having this escape hatch, they're kind of stuck, I would feel like, from that.
their point of view.
That's just mapping, you know.
**Evan Bradley** 24:34 No, that's that's I guess if there aren't any other opinions on the call, Blake, I'd say please, leave a comment describing that, just so that we have that documented as a… An assenting opinion, but.
I'll… I'll follow up and say that we're we're considering this. And, if anybody else has any opinions, let me know.
Otherwise, I'll personally probably try to push for this, because I also agree, it's just a… I think… The more we see OTLP proliferate, I think the more.
unconventional, setups we're gonna see, and I think eventually this is gonna be, we're probably gonna see more of these requests, so… I think we'll probably inevitably need this, but if anybody disagrees, then… Please feel free to say so on the issue.
And if there's nothing else, Blake, you have the next item.
**Blake Rouse** 25:55 Yeah, that's just… To bring it up, looking for reviews on the phase one partial reload.
Paul already gave us gave me some good reviews. And we've been testing it and using it and have found some issues with it that have been resolved in the Pr.
What was interest. What we found interesting was a lot of the function focus on the Rfc. Was like how the reload will work and things like that, with very little focus on how to determine a reload needs to happen in the config. And once we got in there and started using it, there was a lot of things that happened with the config that were unexpected, like receivers.
modifying the config through like.
their own, like, unmarshaling and things like that, that would cause, basically, detection of config changes to basically be like, okay, config's always changed, it would just, like.
I'll like when a new config would come in, even though nothing really would change, it would think something's changed and perform a reboot when I didn't need to. So that was there. And then Pablo found a really good point about the, the way I was doing the thing wasn't working, and that's fixed as well. It now uses hashing to compare the configs which provides consistency. So Just looking for one, it provides consistency and two, it also helps with memory because we don't hold the whole config in memory. And now we just hold like a hash of it. So that's a like a benefit. So yeah, just looking for reviews, just for more for an informal thing. So if anyone could please review. Pablo, thanks for your first one. And if you can review again, that'd be great.
**Pablo Baeyens** 27:44 Yeah, I will take another look. I think the only thing right now in my mind was the feature gates. So the.
The way that I understood the feature gates.
To work, or the way that I thought they would work.
was that, basically, service.parcelReload would enable it for all components, and service.parcelReload receivers or some of the parser reload processors would enable it only for a certain component kind. So, sort of, service parser reload is equivalent to enabling all of these individual component kind feature gates. And I don't think that's the way it works right now.
**Blake Rouse** 28:32 Correct, and that is the way it will work, but the way this one worked, because of the way this is done in this PR, this PR only does receivers.
So there's an alpha gate for the partial reload, which obviously is off by default, being an alpha gate. And then.
**Pablo Baeyens** 28:48 Deep.
**Blake Rouse** 28:49 partial reload receivers is a beta gate. So it's on by default. So what that means is the turn on partial reload. You only need the partial reload gate.
and then the you automatically get the receivers one. So this one, what it's checking now is that both are true. Obviously the 1st one is false by default, and the second one is true by default. So all you need to do is turn on the 1st one. They're both true. But if you turn on partial reload.
false, and then… sorry, partial reload true, but then turn on partial reload receivers false. It technically right now disables partial reload completely, because That's the only phase we have. Does that make sense?
**Pablo Baeyens** 29:32 Right.
Okay, I got it.
**Blake Rouse** 29:34 That's what the.
**Pablo Baeyens** 29:35 Exactly.
**Blake Rouse** 29:35 The code looks kind of confusing, because right now, it's like, are both true? If both aren't true, turn it off. But that will change. Like, the Phase 2 would change.
**Pablo Baeyens** 29:44 Okay.
**Blake Rouse** 29:45 Yeah, the Phase 2 would say.
Is partial reload on? Well, Phase 2 would have both cases, right? If partial reload is on, and then you have, receivers on and processors on, it's on. If you have all three of those false, it's all off.
If you have partial reload true and the other two false, it's all off. See what I'm saying? Because each of those pieces… If you turn… if you turn on partial reload, but then turn off the both phases.
You know, both receivers and processors, when we add processors, then it's off as well.
**Pablo Baeyens** 30:22 Yeah, I guess… under some of those cases, what I would have expected to happen is just that error, like, this is an incompatible combination of.
**Blake Rouse** 30:31 Oh, I… I mean, I could… we can do that, if that… if you think that would be… Preferable.
**Pablo Baeyens** 30:37 I don't have a strong opinion, I mean, like Yeah, it feels like… There's probably no good answer. Some people are going to expect one thing to happen, and some people are going to expect another when they have these kind of combinations. But your option works well. Thanks for explaining.
but… Yeah, up to you. I… I'll take another look, and I think that's the only thing, really, that was… a bit confusing for me. For the rest, I think it's fine if we have some So, false.
Negatives, even on, like, we do unnecessary restarts, that's… That's okay for now. False positives are more concerning, but false negatives.
**Blake Rouse** 31:22 Right.
**Pablo Baeyens** 31:22 That's fine.
**Blake Rouse** 31:23 Yeah, yeah, well, yeah, we're we're testing it now with the change to the hashing, and it has solved the false.
negatives. So.
**Pablo Baeyens** 31:31 Yeah. Okay.
**Blake Rouse** 31:32 Yeah. So we've tested where, like, you know, if some it it doesn't reload unless it absolutely has to with the hashing. It it does fix it.
There was an issue linked to it. Mikola put it on there that we did have something that came out of interesting, which is status reporting. So that'd be a follow up, I think, even before we jump over to phase 2 on how we track statuses, because this has a unique thing. Now we're with partial reload.
a component status basically lives forever. So like, let's say you remove a component. Let's say you remove a receiver. It'll go to stopped.
and the tracking thing. But then that that kind of memory lives forever, right? Because it was removed. Now.
So there's a little bit more work to do there in the whole status handling.
of components to say like.
stopped.
might really be also removed.
So that's just some more work to do.
**Pablo Baeyens** 32:28 Yep.
Yeah, okay. So yeah, I'll… I'll take another look.
**Blake Rouse** 32:37 Perfect. Thank you.
**Pablo Baeyens** 32:38 I think for… Okay.
**Blake Rouse** 32:43 That's it, and I think I had the last Probably going here unless there's anything else.
Does anyone have anything else they want to bring up?
**Pablo Baeyens** 33:01 Going once.
Good choice. Okay. Alright.
Did you know internet?
**Blake Rouse** 33:09 Bye.
**Evan Bradley** 33:09 Bye, everyone.
**Mikiyas Bokan** 33:11 Thank you, bye.
