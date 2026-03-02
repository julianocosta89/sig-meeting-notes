SIG: Community Demo App SIG
Date: 2025-11-05
Duration: 35 minutes
Zoom Recording URL: https://zoom.us/rec/share/KillJ99NWvQqWtHL_-7PtLuaQN4rNou9XixNejOuyvEudV7IlTtmuDZ6A3KJVZxh.X_nnjkfOpmlyJOvD
============================================================

## Zoom Recording Transcript

**Cyrille Le Clerc** 04:53 Hello, Pierre, how are you?
**Pierre Tessier** 04:58 There you go, no more mute. I'm great!
I'm great.
I'm busy with work, but I'm well otherwise. Yeah.
**Cyrille Le Clerc** 05:13 Good news.
**Pierre Tessier** 05:16 Yeah, we just… I think we just had our best month.
In company history.
**Cyrille Le Clerc** 05:22 Oh, congratulations!
**Pierre Tessier** 05:23 Yeah, so… It's good when that happens, I guess. I don't know. It's… Oh.
just other good news, right? Like, around product and stuff like that, just a lot of developments that we're working on, but it's also meaning, you know, a lot of things that need to be done.
**Cyrille Le Clerc** 05:41 In which part of the company are you?
**Pierre Tessier** 05:44 I'm in sales.
**Cyrille Le Clerc** 05:46 Guaranteed.
**Pierre Tessier** 05:46 I work on the solution or the pre-sales team.
**Cyrille Le Clerc** 05:50 Okay.
Alright.
**Pierre Tessier** 05:53 I sit at the intersection of sales and product, I'd like to say.
**Cyrille Le Clerc** 05:58 Okay. I've heard some stories of customers who…
Who went with you, and for whom you…
When you help them install, you help them identify opportunities of improvements, like performance slowness or stuff like this.
And I felt it was a very, very good thing as a product…
To immediately show the value of your product to the customer, while it's not super complicated for,
Product experts, like, sales engineering people, and I felt it was a very, very smart thing.
**Pierre Tessier** 06:33 Yeah, we've, we… I've got story, you know, I can share one, because I was able to tweet about it, is it was happening live, in front of us, where
Somebody on my team.
whose pre-sales person worked with a customer to solve their problem live on a call, and he just was like, I don't know, try this, and it worked, right? And it was… that was the real, you know, resulting incident. For what it's worth, we had them instrument their code with OpenTellowogy while they were at it. Yeah.
**Cyrille Le Clerc** 07:04 Oh, that's a great territory.
**Pierre Tessier** 07:06 But yeah, we have a lot of fun story wins where, some early thing… early results like that.
I don't know who else is joining. I'm getting this… Agenda here…
Cheap.
Wow, lunch just late this morning.
**Cyrille Le Clerc** 07:47 hurry.
**Pierre Tessier** 07:48 Okay, just know I want to just… And the bot.
Anyone?
**Cyrille Le Clerc** 08:05 Maybe I can… we have topics or not?
**Pierre Tessier** 08:08 I don't have any topics beyond… the only thing I wanted to make sure we continue momentum on, and it's a draft PR,
that's, that you, left several comments on as well. I think it was.
**Cyrille Le Clerc** 08:21 gRPC versus HTTP protocol. The HTTP versus… yes.
Someone from Microsoft.
**Pierre Tessier** 08:31 Okay.
That person… Because I'm like.
**Cyrille Le Clerc** 08:39 Let me bring it.
Hotel demo, hotel demo… Have you tested this? No, I just tested it on.
**Pierre Tessier** 08:49 Okay.
**Cyrille Le Clerc** 08:50 there are some, so it makes me very happy, and there is some programming language knowledge that I don't have, so that makes me… really made my day.
And then there are some interesting things on it that we have to debate, I think.
**Pierre Tessier** 09:10 Alright, let me come… so this is the one that, you know, it's a big PR, first off. Big PRs…
**Cyrille Le Clerc** 09:15 Sorry, which one do you refer to?
**Pierre Tessier** 09:17 It's $26.97.
**Cyrille Le Clerc** 09:19 Yes.
**Pierre Tessier** 09:20 That's what I'm talking about. It's… it's not small, right? It touches everything, almost every service.
**Cyrille Le Clerc** 09:26 Yes, on each screen.
**Pierre Tessier** 09:28 not a rename, it's a functional change, right? Like, typically, if we do, like, a small name change, or
you know, something like that, and you have to touch every service because of it, I think that's fine, but this one here, we're actually functionally changing how we're exporting the telemetry, so…
**Cyrille Le Clerc** 09:43 Yeah, it's not… it's doing much more than the title.
**Pierre Tessier** 09:48 Okay.
**Cyrille Le Clerc** 09:50 Because it's removing instrumentation from many SDKs.
I don't know if it's to rely on SDKs provided in Docker Image, because there is always this,
Microsoft monitoring Docker image that is being used in the PR.
Or if it's because the practitioner expects
to the author expects to use, hotel operator to inject. I'm not clear on this.
**Pierre Tessier** 10:21 Yeah, I see that one. We should leave in the Java auto-instementation, for sure.
**Cyrille Le Clerc** 10:27 Living, stay away from it.
**Pierre Tessier** 10:29 No, we should keep the… we should keep auto-instementation.
**Cyrille Le Clerc** 10:32 Oh, yeah, the age… yeah, the binaries, yeah.
**Pierre Tessier** 10:35 Yeah, yeah, for Java, at least. I see this now, yes, now… okay.
**Cyrille Le Clerc** 10:41 The resource is not yet…
**Pierre Tessier** 10:43 variable underscore Java options, we don't need that one anymore.
**Cyrille Le Clerc** 10:47 But it's still in the Docker Compose, do you know why?
**Pierre Tessier** 10:51 I know why it's there. It's left over, and we should probably put more comments on it. We just probably didn't comment to all the spots it was there for. There was a bug introduced in the JDK last year, or not last year, earlier… no, no, it was last year. It was fixed in April of this year.
And it only affected macOS,
I forget the exact… all the details of it. There was a workaround, and the Java options was the workaround.
**Cyrille Le Clerc** 11:17 Do you mind if I come on live on the ticket?
So here you said you no longer need it.
**Pierre Tessier** 11:24 Yeah, just the… the… the… No, no, it's not this one here. It's not… it's the…
**Cyrille Le Clerc** 11:31 underscore.
**Pierre Tessier** 11:33 Java options is no longer needed.
**Cyrille Le Clerc** 11:35 Yeah.
**Pierre Tessier** 11:37 That's what I'm talking about. That environment variable is no longer needed.
Java tooled options, that's standard, that's still there.
**Cyrille Le Clerc** 11:44 Yeah.
**Pierre Tessier** 11:44 I remember just looking at it. So there were some things in here, I think, Make sense?
And for what it's worth, we should probably remove that environment variable in a separate PR, because it's not related to this.
If that makes sense there.
**Cyrille Le Clerc** 11:59 Yeah.
But it's, decoupled.
**Pierre Tessier** 12:02 Okay, so I see this one here. Yeah, your comment there, we should make sure that we have
Java tool options in there.
We need… we need to continue to welcome the environment for people.
**Cyrille Le Clerc** 12:15 We have not decided to, ship components without, SDKs.
**Pierre Tessier** 12:22 Yeah, so, I guess… Oops, sorry, you were just sharing your screen.
**Cyrille Le Clerc** 12:27 Oh, sorry, yeah, I just wanted to, live edit… to capture your feedback on it.
**Pierre Tessier** 12:33 Yeah, I'll share what line of code I finally found is. This one right here is okay to remove.
**Cyrille Le Clerc** 12:39 Okay, yeah. I, yeah, I, come on Tuesday.
**Pierre Tessier** 12:42 We should probably do it with a separate PR.
And when we remove it, we should remove it out of everything, because it's also a new .env file, it's part of the Docker Compose of definitions, so… but we should be ready to remove this entire thing. It was put in place as a workaround to work around a bug in JDK19, or whatever version of JDK we were using.
And macOS.
So, that has been fixed last April.
all images now that have Java in them have adopted that fix, we should be okay.
So, like, the eclipse timer and images, all the images that were based on Java should have implemented this fix.
So… but that's a separate PR.
**Cyrille Le Clerc** 13:29 Yeah, I dropped in a comment, in a Zoom comment, a link to another piece that I would be interested in getting your vision on it, if you can click on it.
It's also Node.js stuff where… It looks like auto-ingestion, auto,
like hotel operator injection of the Node.js library.
**Pierre Tessier** 13:52 Yeah, we should be,
This is just writing the README for it, right?
**Cyrille Le Clerc** 14:04 Yeah, and so, yeah, it seems that, instrument… hotel instrumentation is removed, this PR removes hotel instrumentation.
**Pierre Tessier** 14:13 Oh, no, no, no, we can't do that.
**Cyrille Le Clerc** 14:15 Oh, no, it's not the topical.
**Pierre Tessier** 14:17 Yeah, yeah, no, no, I see right now that the…
The front-end Dockerfile needs to be re-added in there.
I do like the idea of, for what it's worth.
Option 2, that's listen to that README, should be how we do it.
I don't think we do it that way there, though, because we have some slight customizations to our auto instrumentation.
Like, just some slight customizations to how we bootstrap the SDK.
And I would have to go look at them right now. This app is massive.
Hold on, let me always get this side it up.
Yeah, there's…
**Cyrille Le Clerc** 15:00 Can I let you comment? Because I don't know Node.js, so I'm… I would just quote what you say on the…
**Pierre Tessier** 15:08 I'm gonna go find… the…
our instrumentation… We do this.
That's why.
Because it gets really noisy on startup.
If the node auto instrumenter does this automatically, then we could probably move to it.
we'd have to look to see if the resource detectors are picked up properly by the auto instrumenter. If they are, then I think we could move to using the auto.
**Cyrille Le Clerc** 15:53 If I may say, we have an inconsistency here, because here you activate the AWS detector, which sounds reasonable to me.
But, we typically don't do it on Java.
component.
**Pierre Tessier** 16:09 Also, this is not the latest version. I'll pull it up here.
But… I think some time ago we've added this.
If we're looking to be consistent across all languages.
**Cyrille Le Clerc** 16:26 I guess it's a question, it's a different PR, but I guess it's something to bring.
**Pierre Tessier** 16:32 Yeah, it's… it's been here for…
a while, I'm going to think. Somebody else might have… must have added it.
**Cyrille Le Clerc** 16:42 Maybe with a comment saying, yeah, in production you should.
**Pierre Tessier** 16:45 Oh, look at that, yours truly added it some time ago, but I'm sure if we keep on going to prior blames, it was probably still there.
Yeah,
So Severin added all these resource detectors, I think?
Yep.
Should we add it to all the other… Languages? I think yes.
**Cyrille Le Clerc** 17:14 I think our implementation should be doing this for you, though?
I've discussed with my colleagues who work on the Java SDK, and they brought the question on it slowed down the startup.
Especially on…
**Pierre Tessier** 17:28 at those.
**Cyrille Le Clerc** 17:29 To the detector for the cloud on which you are not.
Deployed.
So that's the reason why, typically in the Java SDKs, they don't activate,
My dream is to do it in the presets of the hotel operator MChart or CubeStack Mchart.
**Pierre Tessier** 17:53 Yeah, or do it inside the collector, or…
**Cyrille Le Clerc** 17:56 Yeah, but in the preset of the hand chart.
Of a handshot, so that people would, yeah, make the conscious decision of booking the…
**Pierre Tessier** 18:03 You know, for what it's worth, the demo that we run at Honeycomb, that's where we put our resource detectors, is inside the Daemen set.
**Cyrille Le Clerc** 18:11 Nope.
**Pierre Tessier** 18:12 I don't disagree with you, that's a different PR, though.
**Cyrille Le Clerc** 18:15 So we don't boil the ocean.
**Pierre Tessier** 18:19 Yeah, like, if we want to remove these, like, I won't be heartbroken either way.
**Cyrille Le Clerc** 18:23 Yeah.
**Pierre Tessier** 18:23 I don't think it… like, maybe just leave this one in and that's it.
It's the only one you need.
Right?
The rest of them.
**Cyrille Le Clerc** 18:36 Sorry, the only one we need, I.
**Pierre Tessier** 18:38 Is the environment detector, so that way, if it sees any of the environment variables, it'll pick them up.
**Cyrille Le Clerc** 18:44 what are the defaults? Shouldn't the defaults work?
I'm curious.
**Pierre Tessier** 18:48 Yeah, you're right, the default should work, and the default should contain an environment.
**Cyrille Le Clerc** 18:51 I did that.
**Pierre Tessier** 18:52 Yep.
You are very correct on it. In fact, I'm looking at all this code. I know there was a lot of talk in Node of disabling.
auto-instrumentation for instrumentation FS, because it was so noisy on startups for Node applications.
I… if they did disable it within, you know, the SDK upstream, That we should use…
**Cyrille Le Clerc** 19:13 Yep.
**Pierre Tessier** 19:14 whatever is inside that PR, We should use the option to list it. We should fix what they did.
So… Bouncing around here a lot, but… We should… adopt, I should say.
I don't think part of this PR, we should do a different PR for it.
This PR, I wanted to be focused on just the gRPC part, but,
I should just go to the front end right here. So, they list this option. We should use this, is what we should do.
**Cyrille Le Clerc** 19:53 risen in.
**Pierre Tessier** 19:53 It's how we should start up our, our, our, our node.
service.
Because this uses the proper, I don't know, best practices for Note today.
And we don't do anything special in our bootstrapping anymore, so it should just work.
Of course, this needs to be inside of our Dockerfile, and I see that it's all removed, so that's not proper. We need to,
Change this line right here to do that. It would also mean to change the package JSON as well. You remove all the other packages, and you only include this package, and everything else is dependent upon properly.
**Cyrille Le Clerc** 20:30 Oh, yeah.
**Pierre Tessier** 20:31 So… You know, we should do that. I don't disagree with doing that.
I agree with you, is that it doesn't belong in SPR.
This pair should really be focused on just gRPC and HTTP.
And I do see that elsewhere in this PR.
**Cyrille Le Clerc** 20:51 If you are knowledgeable also on,
Node.js, there is a payment service, index.js, a lot of Fisdon, I don't understand this.
why we need so much,
**Pierre Tessier** 21:06 Yeah, this one here is… this is clearly not understanding how the front-end tracer works.
I'm looking at it now. Now I'm more deeper understanding of that. I think I skimmed through this originally.
And I seen that we were removing, like, we were changing HTTP to JRFPC in a lot of spots, like, right here. I was like, okay, a lot of the good things. And that's why I asked you, have you chats at this? Because I haven't tried it yet.
**Cyrille Le Clerc** 21:28 No, I have not.
**Pierre Tessier** 21:30 Okay.
We should try it.
**Cyrille Le Clerc** 21:33 And it just dropped, so maybe it's not ready for.
**Pierre Tessier** 21:37 Yeah, that's…
also the other one. I will leave conversations in here as well to indicate that we need to,
have this PR focus on just… Http gRPC instrumentation, change over.
And that the removal of instrumentation from Java and Node.js is not part of this PR, and not at all in scope of what we're trying to do.
**Cyrille Le Clerc** 22:02 And if you can open the link I just dropped.
It looks to me like troubleshooting logs.
like a draft PR, but I'm not sure.
Like, all these clogged messages, so…
**Pierre Tessier** 22:29 Yeah, I wonder if maybe you submitted the PRR to the wrong, repo now.
**Cyrille Le Clerc** 22:35 Oh, yeah.
**Pierre Tessier** 22:36 Or maybe they had leftover code that they were trying to do other things with?
And they wrote this PR against the wrong branch, behind the scenes.
**Cyrille Le Clerc** 22:48 Yeah, yeah, maybe instead they want to do it on their own fork of the…
**Pierre Tessier** 22:51 Yeah.
Yeah.
I'm starting to wonder that, because this is, like, what is this?
Thumbs.
Okay.
**Cyrille Le Clerc** 23:08 But we want, half of the PR in the upstream repo, the.
**Pierre Tessier** 23:12 Yeah, I want happiest PR.
**Cyrille Le Clerc** 23:15 But alpha of it.
**Pierre Tessier** 23:19 Okay.
Yeah, it looks like this here is trying to prepare the demo so that you would add the operator to it in full
pull everything, but I think we just want to do an… yeah, okay.
But not quite what we want. That's the only thing I wanted to discuss today, by the way.
**Cyrille Le Clerc** 23:46 I have one thing I would be interested in discussing with you, is the…
other PR, only the comment from your… the PR I'm doing on the hotel operator on the Hotel CubeStack.
And there is a comment from your colleague, Tyler Elmut.
**Pierre Tessier** 24:06 This is on the Hum turf.
**Cyrille Le Clerc** 24:07 Yes.
**Pierre Tessier** 24:09 Which, which, PR is it, do you know?
**Cyrille Le Clerc** 24:11 I dropped the link in the Zoom chat.
**Pierre Tessier** 24:17 18.
**Cyrille Le Clerc** 24:30 Could you see it?
**Pierre Tessier** 24:33 Yeah, this is about using the operator to manage collectors.
**Cyrille Le Clerc** 24:37 Yep.
So, yeah, I'm busy with another PR, so I couldn't discuss with Tyler's hotel operator improvements on resource attributes.
settings. Did you discuss with Tyler of this idea of showing the hotel operator in the demo eventually?
**Pierre Tessier** 24:59 I mentioned to him that we wanted to get there. He said, that's awesome.
I told him how he wanted to do it was to have it inject, environment variables only into the pods, and nothing else.
**Cyrille Le Clerc** 25:12 Okay.
Do you know if you discussed it before or after he made this comment?
on my PR.
**Pierre Tessier** 25:23 Or… no, it would have been after.
He's even on vacation.
Until, like, last week.
So, depending on, how do I pull the exact date of these comments again?
**Cyrille Le Clerc** 25:34 Yeah, I hate it when they say last week, I was like, October.
**Pierre Tessier** 25:37 I thought if you stopped and hovered, yeah, October 28th. Was that a… That was a Wednesday?
No, I would think of after.
**Cyrille Le Clerc** 25:50 Okay. And it was in an overall thread.
**Pierre Tessier** 25:52 Where I said that's what we were trying to do.
Because he came back the Monday of last week.
from PTO.
**Cyrille Le Clerc** 26:01 Okay. We have to continue on this thread, I guess, to discuss.
**Pierre Tessier** 26:04 Yeah, now, what is this PR doing?
**Cyrille Le Clerc** 26:12 My PR is mostly, Adopting the,
The key thing is, using, doing infrastructure monitoring.
Kubernetes monitoring, Linux monitoring, I implemented it embracing the kubestack M chart, but I can also implement it
Using the collectorium chart.
But the key part is… showcase, Kubernetes monitoring, built in.
whiz… Resource Consumption optimization, which is that, if you remember, the collector is capable of.
**Pierre Tessier** 26:59 Not needing a deployment-style collector, but can use demand sets to scrape.
**Cyrille Le Clerc** 27:05 Kubernetes cluster metrics or events, thanks to the leader election, which is a bit of…
boilerplates, and I avoid the boilerplate because the cube stack and chart is capable of… has presets to do it.
when the hotel collector M chart doesn't have presets, so you would have a lot of boilerplate in…
**Pierre Tessier** 27:26 So why don't we just add the presets for the collector health chart?
**Cyrille Le Clerc** 27:28 Sorry?
**Pierre Tessier** 27:29 Why don't we add the presets to the collector helm chart?
**Cyrille Le Clerc** 27:32 I have started this conversation with Tyler, as well.
on… I am, at the moment, proposing to Fix discrepancies, gaps between the…
collector handshot on the CubeStack handshot, because there are a few, sorry.
On, that, kind of, psychological research, why it's diverging.
So you have presets, Kubernetes attributes that are slightly different.
between the two charts, and also presets, Osmetrics… oh, no, Osmetrics, there are also some discrepancies, but I will.
**Pierre Tessier** 28:18 I'm about to write a PR for Qmetrics. What's your discrepancies on that one?
**Cyrille Le Clerc** 28:23 on.
**Pierre Tessier** 28:25 AKH metrics, what's the discrimination?
**Cyrille Le Clerc** 28:27 No, sorry, I have an os.
**Pierre Tessier** 28:30 I'm sorry, Kubernetes attributes, what's the discrepancy there for that one?
**Cyrille Le Clerc** 28:34 So… major discrepancy.
is that on the cube stack, it uses the… Hotel conventions.
**Pierre Tessier** 28:45 Yeah, I notice.
**Cyrille Le Clerc** 28:48 When it does not on the collector.
**Pierre Tessier** 28:50 to be using K8s.pa.label.star, And K8's…
And Hotel Annotations isn't… isn't there now.
**Cyrille Le Clerc** 29:01 In the collector and chart, I'm not sure.
for me.
**Pierre Tessier** 29:05 Maybe not, no, it might…
I'll have to double check. I was just playing with this yesterday for other reasons. I think I was adding it manually myself, that's why.
**Cyrille Le Clerc** 29:13 Yeah.
**Pierre Tessier** 29:14 Now they come back to it. But also on the way, when you say scrape all pod labels and scrape all pod annotations.
What you end up with is…
The label is just the label. It's just the attribute key is the actual label itself, and it should be case.pa.label.whatever the label key is.
So there's some… some issues there as well, and I wanted to add node labels, mostly because I've had several customers now, and even ourselves, operating our own internal tooling, where it was important for us to know what kind of
Instance type the pod was running on?
And that's a node label, which was not available on our pod, trace telemetry. Okay, yeah. So I just…
**Cyrille Le Clerc** 30:01 Sorry, I, yeah.
And there are a few other discrepancies.
**Pierre Tessier** 30:08 Okay.
**Cyrille Le Clerc** 30:09 like, on Authmetrix, linux.
**Pierre Tessier** 30:13 There should be alignment between the two, for what it's worth. When you configure one, you should be able to take that configuration, drop in the other, so there should be some syncing and alignment on that config.
And we… it might have to follow some kind of deprecation policy as well.
**Cyrille Le Clerc** 30:25 I am totally with you, it should be the same config,
And then when there is a gap, I guess there will be conversation on impact.
Because it's…
**Pierre Tessier** 30:35 Yeah, yeah, if there's a change, if it's a braking change, then we need to have a discussion on how do we handle that breaking change.
Right? Like, how do we… how do we handle documenting the change?
And… You know, is there an interim… State that we go in.
Where we support this and that for an interim period, and then eventually maybe some defaults change, and it becomes breaking.
Or something like that.
Oh, boy.
**Cyrille Le Clerc** 31:03 So, I can tell you the change I saw.
for, use hotel annotation.
is for people who are on Prometheus.
Because suddenly, you have the… Instance label that is populated.
It's a really subtle detail.
**Pierre Tessier** 31:27 What does use hotel annotations do exactly?
**Cyrille Le Clerc** 31:31 It's, providing service.name for every single pod.
**Pierre Tessier** 31:42 It should already be set.
No?
**Cyrille Le Clerc** 31:45 just on SDKs, but not on your kubelet metrics.
your Kubelet metric.
**Pierre Tessier** 31:54 Oh.
**Cyrille Le Clerc** 31:54 They don't have service name, and I love to have service name because it makes the navigation much easier, in my opinion.
**Pierre Tessier** 32:07 Okay.
Now, isn't adding replica set name, and job name, and cron job name, and stateful set name, and all these other things pretty expensive?
**Cyrille Le Clerc** 32:19 it's part of the hotel annotation specs. No, I think it's not, it's not expensive.
Because it's cached by the implementation of Odella annotations.
on the Kubernetes attributes. Kubernetes attributes processor keeps all this in cache.
**Pierre Tessier** 32:34 I think it's pretty expensive for it to do it.
Because each time a new one spins up, it's got to get all the metadata out of it.
So it's not just a one-time thing. It's… especially if your Kubernetes cluster is pretty live, it gets expensive, and I think that's why it's not configured by default.
**Cyrille Le Clerc** 32:50 I thought it was because it was not propagated, so there is another PR,
when I looked at the story of one… how it was done in the kubestack M chart.
**Pierre Tessier** 33:07 No, I'm getting this based on reading the Kubernetes Attributes Processor's docs.
Or it's GitHub Readme, where it mentions that.
So, less about the Helm chart thing, but more about.
When you do this, it becomes, there could be performance impacts.
**Cyrille Le Clerc** 33:33 Yeah, as a… I didn't look at the… the code, I just saw that, here.
**Pierre Tessier** 33:39 Yeah, enabling instruction for deployment, staple sets, statement sets, jobs is disabled. Enabling instruction of these metadata comes with an extra memory consumption cost.
So, it's a memory cost.
Just probably a little bit of CPU in there, but there is… there is a cost associated with it.
**Cyrille Le Clerc** 33:56 Yeah, in my opinion, it's worth a trade-off, because, having the…
**Pierre Tessier** 34:00 Sure.
**Cyrille Le Clerc** 34:01 Payment name as the name of your service is extremely, meaningful.
**Pierre Tessier** 34:05 I… I think deployment is already the default, or maybe we make it our default in what we tell customers to do, but…
**Cyrille Le Clerc** 34:12 No, it's each one.
**Pierre Tessier** 34:13 You told it that it's not the default of her, otherwise the processor doesn't get it.
**Cyrille Le Clerc** 34:18 It's manual config.
**Pierre Tessier** 34:20 Yeah, I know, I noticed some other things. There's also, you have to make some changes to the,
the RBAC rule, too.
For all this work.
**Cyrille Le Clerc** 34:30 Oh, I'm sorry, I have to drop.
**Pierre Tessier** 34:33 Oh, same here. I'm sorry. Okay, I will talk to Tyler about the resource attributes for the operator. I don't disagree with him, though, but the angle of the helm chart is to use the collector helm chart instead of the operator deploy collectors.
**Cyrille Le Clerc** 34:47 We can… yeah, we have to pick the gaps to understand what we can use on…
**Pierre Tessier** 34:52 Yeah.
**Cyrille Le Clerc** 34:52 Long term, I wish we will use the hotel operator, but, so I can rewrite my PR to use the hotel collector.
**Pierre Tessier** 34:59 Yeah, and I think you're gonna find… I get sometimes we want… this is what we want the world… we want to do, but I think the world tells us where we should be going.
Instead of us trying to tell the world where to go.
**Cyrille Le Clerc** 35:10 Yeah, yeah.
**Pierre Tessier** 35:11 Right.
**Cyrille Le Clerc** 35:11 So, yeah.
**Pierre Tessier** 35:12 I dialed during a while and see a lot of people using the operator really only to add auto instrumentation, but not to manage their collectors. They're still managing their collectors themselves.
That's what I've noticed.
**Cyrille Le Clerc** 35:24 Yeah.
**Pierre Tessier** 35:25 So…
**Cyrille Le Clerc** 35:27 Okay, we have to follow up on this conversation.
**Pierre Tessier** 35:29 Yeah, yeah, we'll figure it out, yeah.
**Cyrille Le Clerc** 35:31 A pleasure, like, every time.
**Pierre Tessier** 35:35 We'll chat. See ya. And if I see you next week at KubeCon, awesome!
**Cyrille Le Clerc** 35:38 Nope.
for me.
