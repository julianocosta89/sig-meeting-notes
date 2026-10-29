SIG: Community Demo App SIG
Date: 2026-10-28
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Tobias Oka** 02:06 Hey, Juliano.
**Juliano Costa (Datadog, Inc)** 02:12 Hello, hello!
Good day.
**Tobias Oka** 02:16 How was Brazil?
**Juliano Costa (Datadog, Inc)** 02:18 Ugh… Yeah, good, good.
The events went well, and, yeah, I'm happy to be back home.
**Tobias Oka** 02:30 Good. Sounds like an exhausting trip.
**Juliano Costa (Datadog, Inc)** 02:35 Yes, it is, it is.
How are things on your end?
**Tobias Oka** 02:44 Yeah, lots going on, lots of… Like, overlapping topics, a lot of context switching the whole day, so… I saw your message earlier today, regarding, you know.
using… using the Doppler file for fraud detection.
Yeah, I, I… I… I can… I can see your point there.
**Juliano Costa (Datadog, Inc)** 03:13 I mean… My main concern is… Something that, Piotr, keep… Kailak, his… Yeah. He, he, he brought up, on the other PR.
**Tobias Oka** 03:31 Yeah, on the .NET one, yeah.
**Juliano Costa (Datadog, Inc)** 03:32 Yeah, is the fact that, Well, not just the fact that this is not the recommended approach, but also there is another fact that is people use the demo as reference sometimes.
**Tobias Oka** 03:48 Yep.
**Juliano Costa (Datadog, Inc)** 03:48 And if we have that in our services, that may be an issue.
**Tobias Oka** 03:53 Yeah, I can… I see that, and I think it's actually a very, very good point.
Mmm…
**Juliano Costa (Datadog, Inc)** 04:00 I use.
**Tobias Oka** 04:01 See them anymore.
**Juliano Costa (Datadog, Inc)** 04:01 a lot to learn. I mean, I… yeah. Well, I still use so.
And, Like, to someone that is familiar with the project and is following the project, they may spot that and see, okay, this is, something that it… they're doing to showcase X.
But for someone that is new, and it is starting to learn, and then they will see that and say, okay, so that's how it.
**Tobias Oka** 04:35 That's how you do it, yeah.
**Juliano Costa (Datadog, Inc)** 04:36 Just next week.
**Tobias Oka** 04:37 And I even think we should… potentially adjusted on payment then as well. The question is just, can we find an approach That… because originally we said we want to keep it as one image, right?
**Juliano Costa (Datadog, Inc)** 04:53 Huh.
**Tobias Oka** 04:54 But in that case, maybe we won't.
Maybe it is better to not have one image.
**Juliano Costa (Datadog, Inc)** 05:01 So, I… I don't know, so what we could do, I, I don't know… because… Patient Rye.
**Tobias Oka** 05:10 Excellent, mate.
**Shenoy Pratik** 05:12 Yes, hi Juliano.
**Juliano Costa (Datadog, Inc)** 05:14 Hello, hello.
So, I don't… I don't know how… how the override actually works when we are deploying with the operator. But if we have, one sec.
I'm with a, like, a house cough here.
If there is a way, Jesus, sorry.
Let's put that way.
If we… If we have a stage on the Dockerfile.
**Tobias Oka** 06:03 It's.
**Juliano Costa (Datadog, Inc)** 06:03 responsible for fetching the agent. Then, in the last stage of the Dockerfile, we just copy the agent to… To the… to the path.
**Tobias Oka** 06:15 Yep.
**Juliano Costa (Datadog, Inc)** 06:16 And… So, can you, can you… I know that you already explained once, but can you come again in the process of how the override works when we already have this approach?
**Tobias Oka** 06:33 So, how the operator… Generally does it.
**Juliano Costa (Datadog, Inc)** 06:39 I mean the service that we already have.
Yeah. So, like,
**Tobias Oka** 06:48 So you mean the payment?
**Juliano Costa (Datadog, Inc)** 06:49 Yeah, what are we gonna do there is that we're gonna replace the binary, right? And then, when we call, we are calling the same binary that was overridden, and then we are calling the auto-instrumentation. Is that it?
**Tobias Oka** 07:04 Mmm… I'm not sure if I fully follow your question, because, like, what happens in detail depends on the runtime.
Right, so it's a bit different for Java, and a bit different for Robinet, a bit different for Python.
**Juliano Costa (Datadog, Inc)** 07:17 Yeah.
**Tobias Oka** 07:19 But, like…
**Juliano Costa (Datadog, Inc)** 07:20 Yeah, no.
**Tobias Oka** 07:22 basically, each… so the auto-instrumentation works a bit differently for each language, right? But in principle, how it works is that When you start the application runtime.
we need to add some additional parameters to add, like, a Java agent, or Java auto-instrument… sorry, or whatever other, like, auto-instrumentation, right? The exact mechanism differs by language, as I said, but But basically, it's all in the startup parameters of the runtime.
Like, that's the commonality that they have, is that they have, like.
Different startup parameters to do the auto-instrumentation.
And… So, as long as we are able to replace those, it's fine. It's just that we need to make sure that… whatever we put into the Dockerfile doesn't, like… complete… or into the image, if… Eventually, because, you know, it's, like, its own layers. It must not compete with what the operator would be trying to do.
Right, so basically, we need… We… we need, in one way, shape, or form, to have automatic instrumentation happening, otherwise we cannot let the operator override it. Like, if it is… if it is put in, at build time, in a way that is just part of the runtime, then we can't take it out anymore. I mean, maybe there are ways, but they would be really hacky.
But if… if it is… if it only comes in via those… those runtime options when the .NET or Java or Python runtime gets started. If it comes in via runtime options, then we can Easily let the operator override it.
**Juliano Costa (Datadog, Inc)** 09:36 Yeah.
**Tobias Oka** 09:40 And, and so, so if we, if we… So, what I… what I, what I… what my thought for a payment was… Is that… And I just copied the approach that I did for payment for the other PRs now, which was… if… we, adjust the… the container image in such a way that… It basically does… Runtime instrumentation, even though Act it into the image.
Then we can easily replace it.
Like, if we do build time instrumentation.
basically, there is no way to replace it, and we would just need two different images, one that is instrumented with the SDK, and one that is instrumented with the API, which maybe that's also fine.
Because I think we could relatively easily do that in the pipeline.
Or, like, what were you thinking when you said, like, okay, just use the different stages?
Maybe there's also just something that I'm not aware of that's…
**Juliano Costa (Datadog, Inc)** 10:54 So, let me… Let me real quickly share my screen here.
**Tobias Oka** 11:01 Yeah.
**Juliano Costa (Datadog, Inc)** 11:02 Give me a sec.
Of course, I haven't configured that yet.
**Tobias Oka** 11:13 By the way, Shenoy, while we're at it, do you have a topic for today? I don't want to, like, hog the whole call.
**Shenoy Pratik** 11:20 No, no, no, no topics, it's just open PRs, which is you in the majority, so we need to discuss your stuff.
**Juliano Costa (Datadog, Inc)** 11:28 I… I… I need to restart Zoom. I'll be back in a second.
**Tobias Oka** 11:37 Okay.
**Shenoy Pratik** 11:45 Just some pointers to hurt.
Yeah, we can discuss what, Juliano But do you mind rebasing some of your PRs?
See, some conflicts have emerged.
**Tobias Oka** 12:00 Yeah, sure. Like, I think they're anyway not super ready to… like, we are having some fundamental discussion right now about if.
**Shenoy Pratik** 12:09 Yeah, yeah, yeah.
**Tobias Oka** 12:10 like, I'm happy to rebase.
**Shenoy Pratik** 12:12 If this goes the right way. Yes.
**Juliano Costa (Datadog, Inc)** 12:19 First time, sharing the screen from…
**Tobias Oka** 12:22 From your notebook.
**Juliano Costa (Datadog, Inc)** 12:24 From, from this laptop, yes.
**Tobias Oka** 12:26 Ew.
**Juliano Costa (Datadog, Inc)** 12:27 Da-da-da-da… okay, here.
So, if we… if we take a look here…
**Tobias Oka** 12:36 Yep.
**Juliano Costa (Datadog, Inc)** 12:37 On this step.
**Tobias Oka** 12:40 Yep.
**Juliano Costa (Datadog, Inc)** 12:40 we have… we fetch the agent, the auto installation, Java, whatever.
**Tobias Oka** 12:46 Yep.
**Juliano Costa (Datadog, Inc)** 12:47 And… then we… pass, like, the Java agent using the Java 2 options.
**Tobias Oka** 12:54 Yeah, exactly. That's exactly what, in the case of Java, the runtime Parameters basically are, yep.
**Juliano Costa (Datadog, Inc)** 13:01 Exactly. And I guess this is the path, the… the operator… has also, right? So, if we override this Java 2 options, then… yeah, so my… my…
**Tobias Oka** 13:17 I mean, it doesn't have… the operator doesn't have to put it in the same part, to be honest, it's just that the operator also sets Java tool options and sets a Java agent, and then whatever we wrote in here will just be gone, so…
**Juliano Costa (Datadog, Inc)** 13:28 Perfect. So, basically, my idea was, instead of fetching the auto instrumentation from the operator.
**Tobias Oka** 13:37 Yep.
**Juliano Costa (Datadog, Inc)** 13:37 We can have a frog, whatever, and dispatch the agent.
**Tobias Oka** 13:45 So…
**Juliano Costa (Datadog, Inc)** 13:46 Like we do here, like, this. And then we copy that, to this container.
**Tobias Oka** 13:55 Okay.
**Juliano Costa (Datadog, Inc)** 13:55 Like, in the exact same way, the only thing is that instead of fetching from the OpenTelemetry operator, we will fetch from the OpenTelemetry job instrumentation. Okay.
**Tobias Oka** 14:06 Absolutely, yeah, I mean, that, that will create the same runtime behavior, so… I think that that should be… like, that's… that's easy. Yeah.
**Juliano Costa (Datadog, Inc)** 14:18 I don't know about the other languages.
**Tobias Oka** 14:21 Yeah.
**Juliano Costa (Datadog, Inc)** 14:22 So, we would need… Where is the… Fraud detection is .NET, right?
No, fraud is also Java.
**Tobias Oka** 14:38 We have too much shower. Let me quickly check.
**Juliano Costa (Datadog, Inc)** 14:41 So, yeah, fraud detection in Scotland.
Oka…
**Tobias Oka** 14:45 Front-end, front-end is node…
**Juliano Costa (Datadog, Inc)** 14:48 Yep. So, here, da-da-da-da, let me see… So, before… What we had… I have no idea.
**Tobias Oka** 15:06 Basically, we had this… we had this instrumentos SH, yeah…
**Juliano Costa (Datadog, Inc)** 15:13 Yeah, but then it actually came from the… this dependency, the auto-instrumentation dependency.
So, come from an agent or something like that. So, in that case, I don't know.
**Tobias Oka** 15:29 I think now I actually under… like, I think I misunderstood, actually what the… What the feedback was… Hmm.
Let me quickly also open that.
So…
**Juliano Costa (Datadog, Inc)** 15:59 by the way, I don't know if you… if you guys know… well, I think.
**Tobias Oka** 16:02 Yeah.
We have met together.
**Juliano Costa (Datadog, Inc)** 16:04 But we have… no, no, I mean, I don't know if you know, but we are running the GC election, so I think everyone here is eligible to vote, so vote.
**Tobias Oka** 16:16 I'm not.
**Juliano Costa (Datadog, Inc)** 16:18 You are not?
**Tobias Oka** 16:20 I think, at least, I… at least it looked like it, like I'm not… like, I think it was… I read somewhere that it's only if you have done 10… contributions or whatever, and I think I didn't make the cutoff or whatever.
**Juliano Costa (Datadog, Inc)** 16:37 Okay, okay, let me see, what is your…
**Tobias Oka** 16:43 GitHub handle, or, like… Yeah.
Toby Thompson.
**Juliano Costa (Datadog, Inc)** 16:48 Double B with double B, right?
**Tobias Oka** 16:50 Yeah, T-O-B-I-T-O-M-S-O-N. I checked, I didn't see myself in the list, and I, for now, didn't bother to, like, ask for an exception or something.
**Juliano Costa (Datadog, Inc)** 17:01 Oh, okay.
Oh, in the last year, you do have 12 contributions.
**Tobias Oka** 17:16 I'm not.
**Juliano Costa (Datadog, Inc)** 17:17 All on the OpenTelemptory demo. Yeah, maybe they, they were, like, Maybe those 12 contributions are already counting those pull requests.
So that… would,
**Tobias Oka** 17:31 I think it might be a cut-off… I think it might be a cut-off date problem.
**Juliano Costa (Datadog, Inc)** 17:35 Yeah, yeah, yeah, exactly, yeah.
**Tobias Oka** 17:39 No.
**Juliano Costa (Datadog, Inc)** 17:41 Well, next year, next year.
**Tobias Oka** 17:43 Exactly. Next year.
Oh, jeez.
But, you know, you probably have, right? I mean, you are… yes, you should for sure do, because,
**Shenoy Pratik** 17:55 Yeah, I voted as well.
I have a very dear friend standing for GC, Juliano.
So, I had… I didn't have to think much there.
**Juliano Costa (Datadog, Inc)** 18:08 I appreciate it. I, one of my friends, texted me, and they were like, hey, are you anxious about election? And I was like, dude, we just had Brazilian's election this week.
Like, I'm chill, that's, like, I don't care about GC election at all, like, Lula won, I'm happy.
I don't care about anything else, like… It was a mess, guys. You guys have no idea. The country's like…
**Tobias Oka** 18:38 I have a bit of an idea. My dad lives in Sao Paulo.
**Juliano Costa (Datadog, Inc)** 18:43 Hmm.
**Tobias Oka** 18:45 Boy.
**Juliano Costa (Datadog, Inc)** 18:46 Oh.
Are… maybe not cool, but yeah.
Jeez.
**Tobias Oka** 18:51 Yeah.
**Juliano Costa (Datadog, Inc)** 18:52 mess.
**Tobias Oka** 18:52 And I mean, to be honest, I wonder what will happen, because, you know, after the election is before the election, so what will happen next? Because, I mean, Lula is just too old to do it another time, I think. I mean.
**Juliano Costa (Datadog, Inc)** 19:05 Even this…
**Tobias Oka** 19:05 And I thought he's already…
**Juliano Costa (Datadog, Inc)** 19:07 He's… he's really old, but, like, the other guy was, like, Yeah, the other guy is, like.
I don't know the name in English, but, when you have cops doing, like, controlling regions and stuff, in Brazil, we call militia.
Let me see if I can…
**Tobias Oka** 19:35 Yeah, I think the police system.
**Juliano Costa (Datadog, Inc)** 19:36 militia.
**Tobias Oka** 19:37 just different. Yeah, I think in other places, the police system is just different.
**Juliano Costa (Datadog, Inc)** 19:42 But, like, it's not controlling in a good way. They, like, they kind of own the territory, and they… they are the ones providing security, like internet, and gas, like, water. So, if you want all of that, you need to pay them, and not the government. So, it's a… it's a whole mess. And, like, this guy… is… In, well, we are way too off-topic here, but… Let me wrap that up. This guy, he is working in politics for 26 years, like, the guy that was running against Lula.
So for 26 years, he couldn't be judged, in a normal trial, because all politicians in Brazil, they have, like, a privileged, Legal court, or whatever.
So, as… but to become a… to run for election, you need to, kind of quit your role.
And then run for election. So, that would be the first time that he's… that is the first time in 24 years, 26 years, that he doesn't have a political role, because he wasn't elected.
So what he did?
He just, ran away, so he's in the US now.
**Tobias Oka** 21:09 Nice.
**Juliano Costa (Datadog, Inc)** 21:10 He already… yeah, he already, like, ran away. So, like, the… the… the court asked for his passport and everything, and then he recorded a video. This is, like, political, Jeez, I don't know the words, like… I think so.
Persecution, or whatever.
**Tobias Oka** 21:37 Oh, yeah.
**Juliano Costa (Datadog, Inc)** 21:37 like, people are chasing down him or harassing him, because of politics, and he's… of course, I'm gonna give my passport and, like, go for trial because, yeah, I don't have anything to hide. And then he… he went offline for 18 hours and appeared in the US.
I love it.
But the guy got, like, 50… 50 million votes.
So, the country is split, and people believe that he's really being, yeah, anyways, sorry about that.
**Tobias Oka** 22:15 Yeah, that's just the state of the world, that every country right now has this split problem, I think.
**Juliano Costa (Datadog, Inc)** 22:24 I think, so… so, for Java, I think we have an easy solution here.
for .NET, I don't know, and for… Js. I also don't know.
Let me see.
**Tobias Oka** 22:40 But, you know, with that in mind, with what we just discussed, I can do some research and see.
Proposals that can come.
No.
**Juliano Costa (Datadog, Inc)** 22:54 for the…
**Shenoy Pratik** 22:59 Now, I have a question, like, was there any… thought process behind taking the operator library of auto-instrumentation versus the actual GitHub releases? Does it pull in anything extra?
**Tobias Oka** 23:14 No, no. I mean, it was… like, there was actually one thought process.
Which I think we discussed a while ago, which is if you do it like this, Then… You can have it, Have the version automatically checked, like, for updates that are available.
I'm forgetting which, which, which tool are we using?
For automatic updates, is it dependable, or is it, is it renovated at this point?
**Juliano Costa (Datadog, Inc)** 23:53 Currently, the PandaBot, Kilak and I, we have discussed a bit, we need some things that just Renovate can provide.
So we may migrate, to renovate. But at the moment, we are only on the Penabot.
**Tobias Oka** 24:10 So basically, one thought was, if we do it with this ROM image, then we will get automatic updates for it.
But is that… is that the right reason? I don't know, I'm happy to be challenged on that.
**Juliano Costa (Datadog, Inc)** 24:30 Yeah, with… with Renovate, we can actually create custom rules, and then hey, on this path, find this, regex, whatever, and then replace this based on this repository. Okay. So you can be.
**Tobias Oka** 24:49 So very flexible. Okay, yeah.
**Juliano Costa (Datadog, Inc)** 24:52 But, with Dependabot, no.
**Tobias Oka** 24:55 Yeah.
**Juliano Costa (Datadog, Inc)** 24:55 Yo.
**Tobias Oka** 24:56 Okay, so… so Renovate might then actually change that picture, make that an irrelevant argument.
**Juliano Costa (Datadog, Inc)** 25:09 But I think the main point here, Shenoy, and why Tobias started the flow was to be able to replace the instrumentation without having an extra Docker file.
**Tobias Oka** 25:24 Yep.
**Shenoy Pratik** 25:26 I remember now, from the first, first PR conversations, yes.
**Tobias Oka** 25:30 Yeah, so, right, the question was, do we want to have two images, or do we want to have one image? This allows having one image, and this particular approach allows the Dependapot, To see if there's an update.
No.
We are seeing that actually, yeah, like, that it is… With this, with this, pulling it from, from the, from the operator.
Like, it technically works, but it's not best practice at all, and so it's kind of setting a bad precedent.
So the question is, how can we achieve the same thing?
In a way that doesn't… Like, give a bad example.
**Juliano Costa (Datadog, Inc)** 26:27 Yeah, the thing is that, We don't want to teach people to do things in the wrong way.
**Tobias Oka** 26:34 Yeah.
**Juliano Costa (Datadog, Inc)** 26:36 So, yeah.
**Tobias Oka** 26:44 Yeah, so… For Java, it's pretty straightforward, or… For .NET.
Like, I'm not, like, a .NET expert, so… I was actually hoping that Pyotr would be here, but… He hasn't been here the last few times, has he?
**Juliano Costa (Datadog, Inc)** 27:13 No, he, he never joins the SIG meeting. He has a conflict. Okay. That was one of the points that he raised when he became approver. He was like, hey, yeah, I can… I can take the role, but I can join the SIG meetings, and we were like, yeah, that's fine.
**Tobias Oka** 27:32 Okay.
No.
Yeah, so, I mean, I think I would need his input there.
I mean, I left the response on his comment.
Hope it makes sense.
**Juliano Costa (Datadog, Inc)** 27:45 He is pretty responsible on… responsive on, Slack as well, on the SNCEF Slack, so.
**Tobias Oka** 27:53 Okay.
**Juliano Costa (Datadog, Inc)** 27:54 If you want, just drop him a message, and he will reply.
**Tobias Oka** 27:58 That's a good hint, so I'll do that.
Alright.
**Juliano Costa (Datadog, Inc)** 28:07 Cool.
**Tobias Oka** 28:12 Man, I would say… I mean, from my side, that's it. Like, I will just have to get back to you with some better proposals, basically.
Hmm.
**Juliano Costa (Datadog, Inc)** 28:28 Okay.
Okay, okay.
Yeah, then, see you all next week.
are online. That's good.
**Shenoy Pratik** 28:44 Cheers. Bye-bye.
**Juliano Costa (Datadog, Inc)** 28:45 Cheers, bye.
