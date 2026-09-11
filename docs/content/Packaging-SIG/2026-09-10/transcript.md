SIG: Packaging SIG
Date: 2026-09-10
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Diego Hurtado (Dash0)** 00:46 Antoine. How's it going?
**Antoine Toulme (Splunk Inc.)** 00:48 Yay.
How are you?
Yeah.
**Diego Hurtado (Dash0)** 00:51 Right?
You're playing Pac-Man.
**Antoine Toulme (Splunk Inc.)** 00:59 Yeah.
**Sina** 01:02 Hello.
**Antoine Toulme (Splunk Inc.)** 01:03 Greg, actually.
Wait. It's enough.
Putting the name in the thing.
**Sina** 01:15 Pardon?
**Antoine Toulme (Splunk Inc.)** 01:17 I am the duck for the agenda today… Here is… We can talk about what's gonna happen.
Okay, what else? Oh, yeah, I just saw a bug in, the committee repo.
Our meeting is still on Wednesdays. I need to fix that.
I'm just gonna go up.
Makeup change.
conduit is at the best one.
How's everybody doing? Do you have anything you'd like to discuss today?
Yeah, I think, once Caba joined me…
**Sina** 02:17 I don't chat was here, but maybe it's still Sago.
We had an idea for… that we pitched the last time we were here with two dentists.
**Antoine Toulme (Splunk Inc.)** 02:25 Yep.
**Sina** 02:26 about, potentially using these. I'm just considering the… The… Feasibility of using a SAP, having a SAP in addition to their packages?
So, I mean, once we get a chance, we can discuss that if you have no other items.
**Antoine Toulme (Splunk Inc.)** 02:47 I'm not familiar with snaps, but… What does that bring us?
**Csaba Gy** 02:56 Basically, the benefit would be that, onboarding, the packages to Ubuntu takes a lot of time, because Ubuntu has very strict policies that every build dependency and every dependency must be built from source and must be in the Ubuntu archive. And it was basically just a side quest. It's a bit… unintuitive, but basically, we were thinking that maybe in the Snap Store, we would have an easier life until we can get everything into the Ubuntu Archive.
And basically, we were doodling this idea, and if you have any feedback or any obvious points earlier.
**Michele Mancioppi (Dash0 Inc.)** 03:38 I don't believe Snap works for automatic injection.
Okay, I don't know if the Zap Store still does.
the classic snaps, which are effectively… they used to be tarballs, because that is… Like, if we need to go and create interfaces between snaps so that the injector package can go and talk to the OpenTelemetry Java package, and then can be injected to whatever other Snap application, that's never gonna work.
I'll tell you what.
**Csaba Gy** 04:12 So,
**Antoine Toulme (Splunk Inc.)** 04:13 Yeah.
**Csaba Gy** 04:15 Classical confinement is still a thing, as far as I know.
And, basically, but give the idea is that I can write a very short snap that basically takes the currently available upstream dev package and just installs it on the host.
So, this intuitively shows that you can, in theory, make all the changes you want.
Of course, you won't use many of the features that Snaps would give you, so all the connect, all the sandbox is all that is ignored, but you could still have just one command that installs everything.
**Antoine Toulme (Splunk Inc.)** 04:56 Okay.
I suppose that's helpful. I mean, we… I think the problem we're having right now is more like, how do we get those in a place that is, like you mentioned, highly available, archivable?
We're not… This is fancy. We don't need fancy right now, we need basic.
You know, we've had some really hard work from Denise to kind of get us to a point where we can host this at large. We, we've been looking to get some Cloudflare, so we would be able to kind of, host this in a way that would not just be managed by us, but available to the community and, we… We're hitting a bit of a wall, because we're running into bureaucratic processes of how do you get provisions.
Accounts for this, and how do you run them?
So on top of that, having a convenience layer with a snap, or scraped, or homebrew, or what have you.
I don't mind, I don't care, right? It's just great, great, whatever. It's just… I would, I would even say that the Packaging SIG… might not even be responsible for that directly. Someone can come up and build a stamp on top of the Packaging SIG Csabian package. I don't care. That's fine. That's great.
So… Thank you.
Yeah, but yeah, I mean, I hear you, I'm guessing there's… What we can do there, for… for the Debian package that we're building, I know that with Copper, we've had, some success now, I don't know where we left things on that.
So, let's check.
You know, there's a break.
**Michele Mancioppi (Dash0 Inc.)** 06:33 I mean, copper… copper is more or less done.
**Antoine Toulme (Splunk Inc.)** 06:37 Exactly.
**Michele Mancioppi (Dash0 Inc.)** 06:37 It's, there is some, some cleaning up streaming, but, I mean, the moment we have a little bit of capacity, we can start onboarding the thing. It's more a matter of us setting up an account in a way that the CNCF can deal with that more than a technical issue.
**Antoine Toulme (Splunk Inc.)** 06:56 I didn't get any response.
That could work with the community issue, though.
So… Let's go to that.
**Michele Mancioppi (Dash0 Inc.)** 07:07 Antoine, I remember that you had volunteered to set up Let's talk with Trask about setting up these accounts.
**Antoine Toulme (Splunk Inc.)** 07:14 I did. Here, here is what I opened.
I haven't had time to look at it more. So the copper account, we asked them for 3 things. A copper account, a Cluster account, and a package domain.
**Michele Mancioppi (Dash0 Inc.)** 07:28 Horrible fast.
**Antoine Toulme (Splunk Inc.)** 07:30 It got up sits in.
**Michele Mancioppi (Dash0 Inc.)** 07:32 complete.
**Antoine Toulme (Splunk Inc.)** 07:37 Unfortunately, I think I'm gonna have to take time with the OpenTeometry admins.
Or Trask?
So…
**Michele Mancioppi (Dash0 Inc.)** 07:48 Yeah, but it feels to me like this is something that, like 1Password, it must be administered by the GC.
**Antoine Toulme (Splunk Inc.)** 07:59 Yeah.
I don't think I need one passport bolt. I think I need…
**Michele Mancioppi (Dash0 Inc.)** 08:03 Exactly.
**Antoine Toulme (Splunk Inc.)** 08:05 This is not gonna work.
**Michele Mancioppi (Dash0 Inc.)** 08:07 That's always that cool stuff.
No, sir, Dr. Caleb.
**Antoine Toulme (Splunk Inc.)** 08:11 What… what do you… what do you recommend the best way to do this is? I can go to Trask again and say, this is not… this is not the answer I need, this is… I need better.
**Michele Mancioppi (Dash0 Inc.)** 08:20 Exactly. I would even not even have the discussion, Git, I would just call him.
And I would also probably try to call Tad in parallel.
**Antoine Toulme (Splunk Inc.)** 08:28 Alright, so here's what I'm gonna do. It's risk.
We, need, dipper dive.
This is the topic.
Is there a way to get in touch over hope?
to discuss this.
**Michele Mancioppi (Dash0 Inc.)** 08:51 Details.
**Antoine Toulme (Splunk Inc.)** 08:52 This is a blocker for… For the packaging's sake.
Forward.
And politicize. Oh.
**Michele Mancioppi (Dash0 Inc.)** 09:06 Oh, beautiful.
**Antoine Toulme (Splunk Inc.)** 09:07 And moved to Club.
Alright, I'll put a comment up on that issue. Yeah.
That's it.
So, for now, we're kind of blocked on that, That's what I have.
Other than that…
**Michele Mancioppi (Dash0 Inc.)** 09:34 Good luck.
**Antoine Toulme (Splunk Inc.)** 09:35 So, anything else we should talk about?
**Michele Mancioppi (Dash0 Inc.)** 09:36 Folks.
**Antoine Toulme (Splunk Inc.)** 09:38 Just grab some notes in the agenda as we go, so… Step.
discussion of layer… Convenience.
density Cooker off.
Is it a quiche?
to… Okay.
Anything else we can work on today?
**Michele Mancioppi (Dash0 Inc.)** 10:15 Yes.
**Sina** 10:16 Wanted to bring it up as… just briefly that we have a PPA for the injector version 0.11.0, and we're going to be uploading it to the universe either late this week or early next week.
So that, 11… sorry, 0, 11, 0 will be in, stone cake.
**Michele Mancioppi (Dash0 Inc.)** 10:38 But… The, I mean, the injector alone doesn't, Doesn't do much. Yes. You also need the AutoJava agent, at least, to get anything, right?
**Sina** 10:52 Sure, yes, that is correct. The problem that we're having is that, like Shabu mentioned earlier.
Ubuntu policy is a little bit restrictive in the sense that all built and runtime dependencies with the correct versions must be in the archives before you can have them as dependencies, so that's why we hit a little bit of a wall with, for example, the Node.js and the Java.
Auto instrumentation packages, because all the depend… most of the dependencies they relied on required packaging themselves.
So, for now, we're focusing on the injector, and we're saying that, for example, when we're doing testing, for example, ourselves, we grab the Debian packages that you have created using FPM, but the injector comes from the Ubuntu-compliant dev package.
It would need to be an iterative process where you resolve, you know, you resolve the problem of the missing dependencies by packaging them and pushing them to the archives, and then And then iteratively adding each of the other instrumentation packages.
**Michele Mancioppi (Dash0 Inc.)** 11:54 If I remember the Ubuntu policies correctly.
They were murky with respect to the granularity of packages.
So, if you go down the route of packaging every single NPM package separately, you are going to be there until the heat death of the universe.
Correct. If instead you go and package all of them together, say, yo, this is no doubt instrumentation 1, 2, 3, 4, 5, That's a much simpler route.
**Antoine Toulme (Splunk Inc.)** 12:25 These are products, not really libraries, right? So…
**Michele Mancioppi (Dash0 Inc.)** 12:28 Sadly, I mean, I would not split them up separately.
I would keep, my advice to you, if you want to ever be done with this, is actually to treat the entire SDK plus auto-instrumentations as one package. Then maybe later, if you want, you can split it up further.
Because that is a reversible decision.
But in the interest of getting done, I mean, you lamp all of them in one single refractory node modules, and you're done.
**Sina** 12:54 But, vendoring itself is a bit of a gray area, right? So, I mean, let's say I have… we have 70 NPM packages that need to be And the node modules.
I can obviously say, okay, we'll vendor them, and then we'll create the package, but… it's not necessarily an U-2-compliant way of doing it, right? It will just…
**Michele Mancioppi (Dash0 Inc.)** 13:16 Why do you need rendering for this?
**Sina** 13:21 So, for example, the Node.js other instrumentation package.
I tend to rely on the, offensive elementary Packaging.
**Michele Mancioppi (Dash0 Inc.)** 13:29 Yeah, but who cares? Why do you need to create… to package each of the open third dependencies separately?
As opposed to putting all the OpenTangular packages you need in the same package.
Because I don't remember any policy in Ubuntu That would give you guidelines of how to split up node module packages.
Which, it doesn't mean that it doesn't exist, I'm just telling you that I used to work there. I was looking up the Node.js stuff, and I couldn't find, at the time, anything that would force me to go very granular on Node.js dependencies.
If anything, the Node.js ecosystem with all the micro-dependencies it has, I mean, that is a death wish.
**Csaba Gy** 14:28 I think if we, if we put 70 note packages in one package or in different packages.
I am sure we can discuss it, but we still need to do everything from source code. So, for example, if it's compiled from TypeScript, then we need to do it. If, for example, in case of Java, then we need to compile it from the Java source code, which requires a relatively recent Gradle version, and in the Ubuntu Archive, there is Relatively old one.
And if the dedicated team so far, this is where… they can keep up, then I think that very well shows that this is not a small task. For example, get that exact Gradle version there.
And this is just one.
Node.js is the other one.
**Michele Mancioppi (Dash0 Inc.)** 15:32 So, things have not gotten any easier since I left, yeah?
**Csaba Gy** 15:37 Probably not. But my question would be, which would really help the Ubuntu side, although the… Total work wouldn't, be reduced.
why don't we put it first in Debian, and then we just bring it to Ubuntu from Debian? That would be a much smaller step.
**Michele Mancioppi (Dash0 Inc.)** 15:59 Yeah, that is actually something that we would favor, because we don't want only Ubuntu to work, we want Debian and all the downstreams.
**Antoine Toulme (Splunk Inc.)** 16:06 Yep.
**Csaba Gy** 16:08 Because for Ubuntu, even this is the preferred way, that if something is not Ubuntu-specific, then let's get it into Debian, and then we can just mirror it, merge it, and do the changes we need, and maintain our data.
**Michele Mancioppi (Dash0 Inc.)** 16:23 Yes. Is it something that, Canonical could drive?
**Csaba Gy** 16:28 I have to check with that, so…
**Michele Mancioppi (Dash0 Inc.)** 16:32 Because that would definitely be 100% better.
**Csaba Gy** 16:39 We will definitely, ask around and come back with an answer.
**Michele Mancioppi (Dash0 Inc.)** 16:46 I mean, I never had a Debian developer account. I don't know… I don't know what kind of hoops I would have to jump through to get anything done there. I hear total stories of how long it takes.
**Csaba Gy** 16:58 Yeah, I am also not familiar with the Debian packaging world.
So, this is why I don't say anything right now, but for us, this is great news, because at the Ubuntu side, this would be a big help, even though if in total.
We have to do the same work expert.
**Michele Mancioppi (Dash0 Inc.)** 17:20 Amazing. Yeah, definitely going to do about this platform.
I'm actually surprised that we didn't discuss this before, because my expectation is that, That was what you would have reached out to instinctively.
But I, I should've, I should have asked. Yeah, hey, welcome to the Rakuten Debian, my bad.
**Sina** 17:48 Yeah, so regarding, for example, this OpenTelemetry core node package, right, notice all the dev dependencies that are out, and just the semantic conventions dependencies, for example. I mean, the dev dependencies are probably a different case.
**Michele Mancioppi (Dash0 Inc.)** 18:01 Yeah, and even there, I mean, really, I strongly advised against, if you can avoid it, against creating separate packages, because nobody on planet Earth is going to install the API or the semantic conventions as a separate package. Nobody needs that.
**Antoine Toulme (Splunk Inc.)** 18:19 No, no.
**Michele Mancioppi (Dash0 Inc.)** 18:20 Literally nobody.
The APIs, it's useful only when either you inject it as part of the rest, or the API is already part of the application dependencies. Like, there is zero value in packaging it separate, there's just overhead and more confusion later.
**Antoine Toulme (Splunk Inc.)** 18:40 Okay, so… Who's going to… if, Caba, you will be looking into the… the VIN angle for us?
**Csaba Gy** 18:52 Well, I will ask around, within the company what is their position, so…
**Michele Mancioppi (Dash0 Inc.)** 18:58 They don't.
**Csaba Gy** 18:58 Obviously, I am… I cannot make this decision on my own.
**Michele Mancioppi (Dash0 Inc.)** 19:02 Does, does Canonical still employ that, I don't remember the name, but that developer in Berlin that was doing the Java and Node.js packaging?
**Csaba Gy** 19:12 Hmm… I don't know.
**Michele Mancioppi (Dash0 Inc.)** 19:17 Yeah, there was this guy in Berlin.
**Sina** 19:19 How about…
**Michele Mancioppi (Dash0 Inc.)** 19:19 Because when most of the Java logistics work, but they don't remember the name.
**Sina** 19:23 How long ago was this?
**Michele Mancioppi (Dash0 Inc.)** 19:26 I don't know, this is 5 years ago now.
**Sina** 19:28 Oh, okay, then, never mind.
**Michele Mancioppi (Dash0 Inc.)** 19:30 It's, I am… my, my, my mental model of the canonical organization layout is half a decade old now.
**Sina** 19:40 Yep.
**Antoine Toulme (Splunk Inc.)** 19:43 Yeah.
Alright.
So… Okay,
**Michele Mancioppi (Dash0 Inc.)** 19:55 By the way, one thing.
**Antoine Toulme (Splunk Inc.)** 19:57 Yeah.
**Michele Mancioppi (Dash0 Inc.)** 19:57 Would you folks… video canonical folks be interested in, panning together an article for, Not launchpad. How do you call the platform where you post stuff about ongoing work to Ubuntu?
**Csaba Gy** 20:12 Discord.
**Michele Mancioppi (Dash0 Inc.)** 20:13 Yes, discourse.
I'm gonna call, actually.
**Sina** 20:18 Yeah, wouldn't know.
**Michele Mancioppi (Dash0 Inc.)** 20:19 It used to be a hot topic back when, where if it could go on this course, it should go on Discourse, and I would gladly work with you To write an article about what we're working on together.
**Csaba Gy** 20:32 Sure.
**Michele Mancioppi (Dash0 Inc.)** 20:35 I haven't.
I think it's a little.
**Csaba Gy** 20:37 We have a bit of, visibility.
**Michele Mancioppi (Dash0 Inc.)** 20:40 Yeah, so maybe, Sina or Caba, you take, you take some time in my calendar for next week, and then we sit down and write it together. It's less than half an hour. We can also use some material from the, OpenTelemetry blog.
**Antoine Toulme (Splunk Inc.)** 20:58 Okay, yeah, let's see.
**Sina** 21:10 Okay.
**Michele Mancioppi (Dash0 Inc.)** 21:12 I mean, you're doing much more work than Red Hat, you should get the credit for it, right?
**Antoine Toulme (Splunk Inc.)** 21:21 Yeah, thank you for being here. I really appreciate you staying here and helping us. Okay.
Anything else?
**Sina** 21:35 No, thank you.
**Antoine Toulme (Splunk Inc.)** 21:37 Alright, So we got some work cut out for ourselves. I am not around next week, I'm at a conference, I will try to move these… community issue, painfully, up… up the hill somehow. Make sure it happens. And, I will post on Slack if I get any breakthrough.
Other than that, we are good to go.
**Michele Mancioppi (Dash0 Inc.)** 22:04 Hit that huddle button, Antoine. Go and huddle people.
**Antoine Toulme (Splunk Inc.)** 22:10 I can't do that much. That's, That's why I wanted to get Packaging to go, is like, I knew it would be a lot of, You know, herding a lot of cats,
**Michele Mancioppi (Dash0 Inc.)** 22:21 Yes.
**Antoine Toulme (Splunk Inc.)** 22:22 As far as that, so… Yep.
**Michele Mancioppi (Dash0 Inc.)** 22:24 Yeah, but luckily it's also pain that you usually have to go through only once in the lifetime of the SIG.
And then it's done, and we can all leave behind all the pain.
**Antoine Toulme (Splunk Inc.)** 22:35 I think you're right, I think you're right. It's also no… there's no malice here, it's just, like, they don't have the time and the brain time to.
**Michele Mancioppi (Dash0 Inc.)** 22:42 Yes.
**Antoine Toulme (Splunk Inc.)** 22:43 So,
**Michele Mancioppi (Dash0 Inc.)** 22:44 Well, something that we could also do.
Yeah. Quite frankly, is to check if there is a way to transfer accounts And then we get started on our own.
**Antoine Toulme (Splunk Inc.)** 22:55 Yeah, that's exactly… I'm about, like, okay, Cloudflare is free by default.
how about we get something started, and we give them access?
**Michele Mancioppi (Dash0 Inc.)** 23:06 Yeah, if you tell me that it's not free, I'll… you send it to me, I'll put the company credit card in, and then we transfer it.
**Antoine Toulme (Splunk Inc.)** 23:13 I'd like to just make sure I don't… Surprise them more?
In the sense, the fact that it's been 3 weeks is kind of giving me a little bit of a pretext to take this type of action. I'm like, hey, I just need to get going here, so here's a new plan, right? We get going, and then you're able to kind of catch up and eventually take over the account.
Yes.
Let's see, let's see what they say. I'm just gonna give them one more chance this week, and then if that doesn't happen, I say we're gonna start to move a little harder towards that.
**Michele Mancioppi (Dash0 Inc.)** 23:46 Remember that my fingers are twitchy on the one.
**Antoine Toulme (Splunk Inc.)** 23:50 Okay, good to know.
**Michele Mancioppi (Dash0 Inc.)** 23:52 I have two fingers. I may click that create account before next week.
**Antoine Toulme (Splunk Inc.)** 23:57 So, Michele, you remember also, like, we, We have been accepted for KubeCon to from the Packaging SIG, so it also puts it into a lot more light, and we need to have, frankly, something ready for Prot by then.
**Michele Mancioppi (Dash0 Inc.)** 24:12 Exactly, exactly. Exactly.
**Antoine Toulme (Splunk Inc.)** 24:15 Otherwise, all we've done is we're gonna show up, and what are we gonna talk about for 30 minutes? If you can do this.
**Michele Mancioppi (Dash0 Inc.)** 24:21 Yeah, but just…
**Antoine Toulme (Splunk Inc.)** 24:22 Don't pull too hard, you can do it on the GitHub pages, but you only have the latest version, like, none of that makes sense.
**Michele Mancioppi (Dash0 Inc.)** 24:28 Exactly.
**Antoine Toulme (Splunk Inc.)** 24:28 ridiculously.
**Michele Mancioppi (Dash0 Inc.)** 24:31 That's not serious work, yes.
**Antoine Toulme (Splunk Inc.)** 24:33 Ideally, what I would like to get out of the talk is that we also open up the committee to say we need more people to help us with, let's say, the collector, or other packaging that we're not thinking about.
**Michele Mancioppi (Dash0 Inc.)** 24:43 Contrib. Please come and help me contrib. It's a wasteland.
**Antoine Toulme (Splunk Inc.)** 24:48 help us, right? And we can have more people on this call to sustain the effort moving forward, so it's not just three guys.
And, we can make it a bit easier on ourselves.
**Michele Mancioppi (Dash0 Inc.)** 25:03 Alright, folks.
**Antoine Toulme (Splunk Inc.)** 25:04 Right. See you the future.
**Michele Mancioppi (Dash0 Inc.)** 25:06 This was a productive call.
See you next week. Bye.
**Antoine Toulme (Splunk Inc.)** 25:09 Later.
**Diego Hurtado (Dash0)** 25:11 Yo…
