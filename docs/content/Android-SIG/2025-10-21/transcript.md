SIG: Android SIG
Date: 2025-10-21
Duration: 58 minutes
============================================================

## Zoom Recording Transcript

**Cesar Munoz** 01:02 Hello?
**Jason Plumb** 01:07 Good morning.
**Hanson Ho** 01:09 There we go.
So bright.
Winter now Or… it's fall, but it feels like winter.
**Jason Plumb** 01:32 I love the fall.
So nice.
**Hanson Ho** 01:37 Yeah, the World Series and everything, so good.
**Jason Plumb** 01:43 I might be done with baseball forever.
**Hanson Ho** 01:48 Until next year.
**Jason Plumb** 01:52 Yeah…
Welcome, Francisco.
**Francisco Prieto** 01:59 Hey, everyone.
**Jason Plumb** 02:00 Is this your first time joining us?
**Francisco Prieto** 02:02 Second.
**Jason Plumb** 02:03 Second time, okay. Sorry.
8 o'clock meetings, will not have the most, deep recall.
**Francisco Prieto** 02:12 I brought it.
**Jason Plumb** 02:13 More coffee will help.
Give me one more second for people to trickle in. Our agenda is, pretty open.
But I will add some things, since no one else has yet.
Yep, so everyone, please feel free to add any agenda items that you might have on the shared doc.
For those of you who may not have seen this yet, or didn't notice the PR,
Jamie is now an approver, and so I just wanted to give a little applause and say thank you for your help. It's been, really, really great to have you on board helping with this project, so…
Cool. Really appreciate it. Hey, Manuel.
**Manoel** 03:23 I know, I won't.
**Jason Plumb** 03:25 We can always, you know, this project is actually getting a lot of attention these days, and, like, more than ever, and so we can always use PR reviews, people looking at pull requests, and providing feedback, even if you are not
An approver, or even a triager, or a maintainer, like, please feel free to provide comments and leave feedback and approvals, or not, as the case may be.
Cool.
Alright, aside from going through open PRs and issues, I wanted to talk about the RC1.
So, let's take a quick look at the main issue, this issue.
So I created this, kind of in response to…
blog post that hit the main OpenTelemetry site a couple of weeks ago, soliciting feedback, and it pointed them to here, in hopes that people that are using the library, evaluating the library, have any opinions, they can put them here. And it looks like we probably haven't had too many in the last week.
Yeah, there was a little bit of back and forth, and…
Right, this was around the OKHTTP…
JVM flavor problem, so that should be fixed when we release.
And then there was a new request about R8, but they haven't responded yet. I would also like more specifics, because I thought this was a little bit vague.
Yeah. I know that we, for a while, had ProGuard stuff in there. ProGuard, I guess, largely falling out of fashion in the Android world in favor of R8, which has probably better support these days.
Yeah, so let's see where that discussion goes. I don't think it should hold up in RC1.
But they're asking for some specific R8 rules due to this project, so, you know, if there's… we probably just need some sort of, I don't know, statement or something. It'd be nice to know what they're comparing it to, though.
**Hanson Ho** 05:33 Are they talking about the ignore classes that some instrumentation might bring in? Like, ones that we don't use, but other instrumentation might refer, and might not be available at runtime?
**Jason Plumb** 05:48 I don't know the answer to that.
It's hard to tell from this, so I think…
I think Jamie's response is pretty valid, like, what… what are you actually looking for?
So, anyway, yeah, it'd be good to get more information on that, but like I said, I don't think… I don't think any of the feedback here should hold up an RC1. I think Severin's comment is still very valid, in that, we need to flesh out some docs.
And we need to get the instrumentation into the registry. And those are both on my…
Ever-increasingly growing backlog of to-do items, but.
**Hanson Ho** 06:25 If there are tickets for this, there's some folks at Embrace who might be able to help write some docs. We're talking about doing that in the… yeah, in this general page. Yeah.
**Jason Plumb** 06:39 Yeah, this would be good, and then also the registry. I think there was an ask.
In the blog post PR, I think there was an ask to have the instrumentations that we provide available in the registry.
So let me find that PR, and I'll link to it real quick. So that was…
in the I.O. site.
this one, I think.
Yeah, so there's… there's this issue, but it's not… it's not in the Android repo, but I'll link to it here.
**Hanson Ho** 07:31 Okay, interesting.
**Jason Plumb** 07:33 Because, you know, this is where all the work for the registry and everything on the .io site actually happens, right? So…
Yeah.
**Hanson Ho** 07:41 Cool.
**Cesar Munoz** 07:45 By the way, regarding the RC versioning support, that I worked on.
I was wondering if there was a way to test it, because it's not something I actually…
got to test, I mean, those bash… Shell… shell scripts.
I kind of ran them, locally.
But, you know, usually when growing in GitHub Actions, this tends to be different, so…
If there's any ideas, or maybe we can just try and…
If we… if we mess up RC1, then we can go right away with RC2.
**Jason Plumb** 08:24 Yeah, if it was, like, a critical failure that we couldn't recover from, we could do that. It's not ideal. But you're talking about the one…
Yeah, this thing.
**Cesar Munoz** 08:39 Yeah, there's a ton of shells.
**Jason Plumb** 08:40 Specifically, some of these scripts, yeah, so this one…
That can be run, right? You can just run this from the command line.
**Cesar Munoz** 08:49 I do.
And it worked. It's not all combined.
**Jason Plumb** 08:53 Yeah. I know, it's the interactions that might get… might get, problematic. So I ran… I ran this one, I ran this one, I mean, this one's called by the draft change log, right? These are all our…
I ran all of these independently, and I did a publish to Maven Local.
And, I mean, I changed the version to 10RC1.
And it looked good. Like, the…
**Cesar Munoz** 09:19 Awesome.
**Jason Plumb** 09:20 the agent had RC1 with no alpha, And… the…
Rest of the modules had RC1 and Alpha.
So it looks like it did work.
**Cesar Munoz** 09:35 for the agent to not have alpha, I guess you added the Gradle property.
Also stating.
**Jason Plumb** 09:42 You would think so. Yeah, someone did.
**Cesar Munoz** 09:46 Oh, okay.
**Jason Plumb** 09:49 I mean, maybe I did, I don't think so. Oh.
Maybe I did. Let me, let me double check.
**Cesar Munoz** 09:56 No, but that's a good point, so that's something missing before the RC release.
Forgot about it, to be honest.
**Jason Plumb** 10:03 Yeah, because you have to… yeah, as part… I figured we would do that as part of the release, but it's good not to forget that. Let's make a note of it real quick.
**Cesar Munoz** 10:11 Yeah. Thank you.
**Jason Plumb** 10:18 Let me… Get the exact property here.
Yeah, I must have added that locally.
It's looking good. Yeah, thanks for that, PR. I think it's great. I tried it out, and…
You know, things are bound to be a little bit weird, but, you know, we'll see where it goes.
**Cesar Munoz** 10:59 Yeah.
**Jason Plumb** 11:00 you know, pool.
Yeah, we'll jump…
**Cesar Munoz** 11:06 We're mostly there.
There's just one VR from Jamie that I would like it to get.
merged before RC1?
This one? Yeah.
**Jason Plumb** 11:17 Yeah, I agree.
**Cesar Munoz** 11:20 and apart from that, I don't see what else?
You know, we could do the thing that other projects do and assign a milestone. We've only done it one other time.
**Jason Plumb** 11:31 But that's the way to do it, right? We should have a milestone for RC1.
And then as part of our release notes, like, in the other Java repos, they have, like, pretty clear instructions in the releasing process to also…
make sure that there's a milestone. We don't have any mention of milestone in here, because we haven't been using them.
**Cesar Munoz** 11:52 Let me see if I can create it.
for this issue.
**Jason Plumb** 11:56 A milestone?
**Cesar Munoz** 11:58 Yep.
**Jason Plumb** 12:04 You can just do it right from this dialog.
See?
**Cesar Munoz** 12:09 Ian.
It's…
**Jason Plumb** 12:11 Do you see that, Cesar?
If you just.
**Cesar Munoz** 12:15 If you're fresh, it should be there now.
**Jason Plumb** 12:17 Okay.
Let's see…
We'll do a page refresh.
Yeah, there you go.
**Cesar Munoz** 12:26 There.
**Jason Plumb** 12:27 Cool.
Nice, and I gotta remember that it's RC.1. In my brain, I've just had it as RC1, but that's the… the SEMCOM mentions, like, the semantic versioning specification mentions RC.1, and the scripts are definitely written to handle RC.1 and not RC1.
**Cesar Munoz** 12:48 Oh, to be honest, I didn't know either until I worked on that PR. I had to check December website.
**Jason Plumb** 12:54 Same.
**Cesar Munoz** 12:55 Damn.
**Jason Plumb** 12:56 Yeah.
Okay, well, that's exciting, I agree that this one should go in, so,
Yeah, let's, let's get that in before we do the release. Cesar, I have been kind of…
kind of wrangling most of the releases lately. Are you comfortable with that? Do you want to have a stab at this one, or should I just continue?
**Cesar Munoz** 13:19 To be honest, I'm just… I'm fine either way. Okay. But I can… I can have a look for this one,
Yeah, I guess especially because… I added a lot of changes to the…
It released YAML, so if something goes wrong, I'll probably be quicker.
**Jason Plumb** 13:38 Well, I'm also, you know, I've got a time zone advantage being on the West Coast, so if you… because you're kind of wrapping up your day soon. By the time this gets merged, and we start the process, we get the changelog prepared and stuff, get the version updated, it'll…
It'll be late enough that…
I mean, I'm happy to kick that off if that still works for you. If you wanted to try it, though, if you were like, yo, I really want to see this work, I need to refresh my memory of how the process works, I'll wait until tomorrow, that's totally fine, too. I just wanted to give you an opportunity.
**Cesar Munoz** 14:09 Thanks. No, thanks for that. To be honest, I'm fine.
**Jason Plumb** 14:12 Okay.
**Cesar Munoz** 14:13 Either way, so if you wanna go ahead, just… You know, go ahead.
**Jason Plumb** 14:17 Yeah, okay, cool, that's cool.
**Cesar Munoz** 14:21 So you're planning to kick off the release, because I forgot what was exactly the date that you mentioned on the blog post, is it today?
**Jason Plumb** 14:32 I don't think I gave a date date, but I did say October, I think.
**Cesar Munoz** 14:37 Okay.
I mean, if you want to go right away today.
**Jason Plumb** 14:43 And look, there, I misspelled it, RC1 instead of RC.1.
**Cesar Munoz** 14:49 That's fine.
Okay, I'll put it.
**Jason Plumb** 14:52 Another retroactive, comment.
There we go.
**Cesar Munoz** 15:02 So today, Manuel added the, second approval to that PR that I mentioned.
**Jason Plumb** 15:09 Yeah.
**Cesar Munoz** 15:09 I'm fine for it to go as is.
If you want to have a look, please do, and if you want to, you know, trigger the release today, I'm also okay with that, which would actually be nice to start
To try the release.
You know, early… On… on this week, and not on… not on Friday or something.
**Jason Plumb** 15:32 Yeah, I agree. Do we need… do we want to wait for Contrib? I don't think that Contrib has been released yet. That might be…
That is my fork.
That… oh, so it has been. Okay, we're good. 15 hours ago.
**Cesar Munoz** 15:49 Okay, so… Let me see if I can quickly create a…
PR, because it has breaking changes.
**Jason Plumb** 15:59 Yeah, yeah.
**Cesar Munoz** 15:59 So it's definitely gonna break our bill.
If you want to end…
**Jason Plumb** 16:04 Do we not have that?
Yeah, here, okay, it does break the build. Good. Okay, so let's add this to the milestone as well.
**Cesar Munoz** 16:12 Got it. I'll try to take a look at it before… you know, for, clocking? Off.
**Jason Plumb** 16:22 Yeah, clocking out, that's fine, I mean, I wouldn't sweat that. I can also do that, as long as we have it marked as the milestone. I'm also just gonna quickly file an issue to mention the milestones as part of the…
releasing…
Yeah, just, just so I don't forget.
Let me go… let me just make a link of this…
And the other one…
This one.
Okay, cool.
What else related to the release?
This one needs to be in here, too.
I mean, I'm basically just manually duplicating what the milestone does, but here we are. Okay.
Alright, if we think that's it…
**Cesar Munoz** 18:09 Yeah, I don't think so.
**Jason Plumb** 18:10 So, you got me thinking, though, earlier. So, I linked to…
I linked to this issue in the I.O. repo. That's specifically about the registry.
No, is it? Sorry.
**Cesar Munoz** 18:27 Yeah.
**Jason Plumb** 18:28 This is specifically… About the registry, but there's another request in… The umbrella issue…
To flush out this.
This is not the registry, so we should probably create an issue for this if we don't have one. Hanson, do you know if one exists already for this?
**Hanson Ho** 18:56 No, yeah.
The stub is just a stub, we need to figure out what we want to put in there, so if we know exactly what we want to put in there, we should create some issues.
**Jason Plumb** 19:08 Well, I have some opinions, but we… I mean, and again, it won't block RC1, but we really do need to flesh out… sorry, Cleverchuck, I'm jumping in front of you.
**Hanson Ho** 19:22 Yeah, as long as we have an outline of roughly what we want to see, we could basically say, hey, we generally agree that these are all needed, who can write it, and then, you know, folks can contribute, you know.
You know, bits as they see.
Yeah, Jason, you can write a ticket for… or an issue for what you want to see in there, we can discuss it in there.
**Jason Plumb** 19:47 Okay, and I'll do it in the I.O. repo.
But yeah, I would, I would basically like to see something like,
Something like the demo app main.
So, something like… Where's the demo application? This one.
So, kind of walking through the initializer, you know, and then, like, how to use that, like, so, okay, so how to create an instance of RUM, talking through what the configuration options are, at least the common ones, maybe not all of them, but, like.
how to set… how to set a header and how to specify your endpoints, like, that'll go a long way.
And then how should we enable or disable certain instrumentations?
**Hanson Ho** 20:40 So we should probably have another page underneath Android to specifically talk about OpenTelemetry Android, so we can basically have more latitude in, you know, controlling what is in there. Because this is theoretically just about, you know, Android in general, not hotel Android.
**Jason Plumb** 21:00 Really?
**Hanson Ho** 21:01 Yes.
**Jason Plumb** 21:03 What do they have on iOS? Nothing.
**Hanson Ho** 21:05 Yeah, literally those three stubs is, hey, let's just put something in there rather than nothing.
**Jason Plumb** 21:11 The history of this was, like, it was a way to be able to have somewhere for client-side concerns being called out.
**Hanson Ho** 21:20 Yeah, like, I was thinking, like, on the Android page, we'll talk about things like, like, life cycles with the UI, so Compose versus, you know, non, but we should definitely have a page here, or somewhere here, that links to OpenTel to Android, and talks about.
basically a more comprehensive README, which, you know, things like what you mentioned would be very appropriate.
**Jason Plumb** 21:45 So maybe it's in here, then, under language APIs and SDKs.
**Hanson Ho** 21:51 Yeah, yeah, potentially, if, if, if we want to add an Android one.
**Jason Plumb** 21:57 Because I did, I did raise this question, I'm like…
it's not really a language, right? It doesn't… it's not a language, and they're like… both of the docs people that responded were like, yeah, let's just hand-wave around that fact and treat it like a language, so that it fits into the ontology nicely, so… I… I mean…
Kelsey?
I think it makes sense to put it in here.
**Hanson Ho** 22:22 Yeah, it's weird, because it's also not an API, per se, it is an agent.
Really, but it does make sense to have something, like, even though the nomenclature is slightly, you know, meh, it definitely makes sense to have something here, that says Adroid.
**Jason Plumb** 22:42 Yeah, I was just trying to compare with the… the Java agent. They have it under zero code.
Hmm, automatic instrumentation.
**Hanson Ho** 22:53 It fits. I think it fits. It's just a little bit… or rather, in the spirit of things, it fits. If it's… it doesn't fit.
Technically.
**Jason Plumb** 23:02 Okay, so, yeah, so they have the agent under zero-code instrumentation.
**Cesar Munoz** 23:09 I remember that issue that I just sent. I think it was related to weather.
like, where to put the auto Android docs, and I think…
At least back then, the idea was to do so in… You know, within the platforms.
**Jason Plumb** 23:26 Okay. Menu.
**Cesar Munoz** 23:28 Big as, you know, the same…
Discussion around, is it a… it's not a language, so…
**Hanson Ho** 23:35 Well, separate…
**Cesar Munoz** 23:36 from that issue.
**Hanson Ho** 23:38 Severin mentioned here, for the JS, or rather, browser, it starts with JS, which is kind of janky, too.
So, I don't think we should be under Java, for instance.
like… Kotlin, maybe? Like, if we get there?
But Android… Zero code instrumentation, one of these… it doesn't say language, And it says Android there.
**Jason Plumb** 24:08 It's just silly to put a new category in here called Android, and if you click it, the first thing you start seeing is, like, our initialized code. Like, that is code, that's not no code.
**Hanson Ho** 24:18 Beautiful.
**Cesar Munoz** 24:19 scroll down, because that… that comment that we saw from Severin was the first one that…
Later on, he mentioned that they talked about it in the… in the SIG call.
They came up with the platforms.
**Jason Plumb** 24:33 Okay. Idea.
Yeah, that's how the other section came about, right?
**Cesar Munoz** 24:40 Yeah.
And this all started because I mentioned Auto Andrew.
Specifically, so… It sounds to me that that's the place for Otelandre.
Only.
At least, you know, based on that, in this… on this issue. But, I mean, we can always…
**Jason Plumb** 24:57 Can you be specific? You mean…
**Cesar Munoz** 25:01 platforms. Yeah.
**Jason Plumb** 25:04 Yeah.
**Hanson Ho** 25:04 Oh, but we've changed that now, so right now it's client-side apps, so the stub… like, I…
**Cesar Munoz** 25:11 Okay.
**Hanson Ho** 25:12 I want to add perspective.
**Cesar Munoz** 25:13 Change after that, you mean?
**Hanson Ho** 25:14 Yeah. When I had the stub, it became less…
technical and became more… because this is where we're going to put stuff like sessions, and basically recommendations, so it became less about these are the APIs, but I definitely feel
we could add here, either, either as a top-level page, so if you go to client-side apps, just have one that says Open Telemetry Android, and then specifically, above.
**Jason Plumb** 25:41 And then leave this one?
**Hanson Ho** 25:43 Well, eventually, we'll hopefully have, like, actual Android docs, like, if you want to just work with Android, like Kotlin Multiplatform, or, you know, whatever it is. Or we can put it under there, like, I think, I think…
Honestly, both is fine to me, like, right now. Any… docks anywhere here is better than no docks, so…
**Jason Plumb** 26:01 I agree. I'm not super opinionated about that.
**Cesar Munoz** 26:07 I mean, if we don't have anything else to boot there, I will just…
at the Hotel Andrew Dogs, and then if in the future we think that
We could expand it something else, and probably we can rearrange the… the… the layout later, or…
**Jason Plumb** 26:29 I'm good.
**Cesar Munoz** 26:29 And maybe, unless you already have some ideas.
**Hanson Ho** 26:32 No, that's fine, too. Like, if you click on the Android page and it just says, like, open to Android configuration, and just plop it all there, instead of having, you know, another layer or another level with just one heading, that's totally fine. And then when we have more information, when we have more stuff, then we'll add in the structure.
And the important part is just, like, having information there. How it's organized, it only matters if there's a bunch of stuff.
Which would be a good problem to have.
**Cesar Munoz** 27:04 Yeah.
**Jason Plumb** 27:13 Okay. Well, I think there's some takeaways from that. I will create the issue
specifically for this instrumentation, the other issue about the registry is open, if anybody wants to tackle that, and then we'll go from there, and we'll start the RC1 today. Well, we have a couple of things we need to address first, but then we will get that started today.
And realistically, it might take a day or two.
I think.
Cool. If we're done with this topic, we'll move on.
Alright, we've talked about the release, we've talked about docs.
Clever chuck.
**cleverchuk** 27:56 Yeah, so the question came to my mind, the last time that we were talking about
Always send in the message, the telemetry.
As long as, like, the network is available without, like, buffering.
That was basically a thinking. Are we actually, like, considering, like, how much, bandwidth that we consume? Because I know there are, like, places on the planet, like, where
Data is, like, very expensive.
And, A user might be running out of their data if we're, like.
using a lot of it to, like, transmit the telemetry, so… I'm wondering, like, whether we have anything in place to, like, make sure that we don't…
Consume too much data, like, trying to, like, send.
telemetry only went down, like, on Wi-Fi and stuff like that.
**Hanson Ho** 28:50 the problem to do, if we did that… so, definitely, data usage, especially on mobile, is a concern. But if we start, you know.
only send data when the network is good, then the data will be biased. Which… which is…
you know, not something we do, we want.
And, in theory, this ought to be, controlled and monitored by the apps that use it. Telemetry generally is pretty light. So, unless they're collecting copious amounts of data,
You know, in terms of collecting things that we don't collect. The vast majority of the data coming out of this will probably be network-related traffic.
And that really depends on how much they use it. So for us, it's really hard to… like, at best, we can say, you know, X number of requests will result in X amount. But I think we're talking about something like, if we compress it.
it compresses pretty good. Like, a thousand network spans will probably be, I don't know, compressed a couple hundred K.
So…
**cleverchuk** 30:12 Oh, is the compression enabled by default?
**Hanson Ho** 30:17 It should be. I assume everything is G-zipped.
If it's not, we should definitely do that.
**Cesar Munoz** 30:28 I mean, we're going with whatever the upstream default is. I'm not sure if that's what they're doing. I haven't checked.
**Manoel** 30:36 I think if you're using your KHTP, if not wrong, it's not just zipped by default.
**Cesar Munoz** 30:45 Got him.
It… okay, so… Yeah, no, that's it before.
**Hanson Ho** 30:56 So…
**Cesar Munoz** 30:57 Let's check upstream.
**Hanson Ho** 30:59 we could do things like monitor data usage, or at least, for network stacks that we have visibility onto that. So we could always add a OKHCP listener and count the bytes, and then basically just have a cumulative count.
whether or not we want to expose that as telemetry, I don't know, but this is definitely a good concern, to eventually document and say, hey, roughly, this is how much data is going to be used, because
again, it really depends on usage. It's really hard to say, like, hey, Hotel Android consumes this amount of data, because
Depends how you use it, depends on how many network requests you make, so…
**Jason Plumb** 31:36 So, I'm curious, Cleverchuck, I mean, I think this is a real concern,
I'm curious if you have a design in mind for this, like, do you think that we should allow developers using OpenTelemetry Android to have the ability to constrain what network types we…
export data from?
Like, what's… what's your thought on how we might better manage this? Because I think… I think the short answer is today, I think we don't consider it.
**cleverchuk** 32:07 Oh, okay. Yeah, I do not have any design in mind, but, like, what you just said eventually, would be a good idea to, like, yeah, constrain only when it's on Wi-Fi, or something like that.
**Hanson Ho** 32:20 No, I, I, I…
**cleverchuk** 32:21 Configure that would be good.
**Jason Plumb** 32:23 Okay.
**Hanson Ho** 32:24 I actually vehemently disagree, because the data coming from that is going to be extremely biased.
**Jason Plumb** 32:32 What do you mean by biased, though, Hanson?
**Hanson Ho** 32:34 So basically, you're gonna get more data from folks who are connected to Wi-Fi, rather than folks who are, out in the wild that don't connect to Wi-Fi, and also in environments where there's high bandwidth. So, naturally, there's gonna be,
data that gets sent later will be… less likely to be sent, and if you're always on a network that is not eligible to send, that data is going to be, you know, not there. So, your population, naturally, will get a higher percentage of ones from good data environments.
I think transparency here is the way to go, is it… we should, you know, do some benchmarking and say, hey, it roughly takes this much, data, you know, to… to… to send 100 spans or whatever, and depending on their usage. And this… this…
I did some experimentation with this, and it depends wildly on how many attributes, you use. If you record a span with only a handful of attributes, it's actually quite small. But once that… the number gets really big, then, you know, it gets really bad. So, if we can say, hey.
X number of spans with X number of attributes, with, you know, rough amount of entropy, is roughly this much compressed. And I think folks who use it will have to basically take a look at their usage,
roughly the guidelines that we have, and decide for themselves whether it's too much or too little. And frankly, if they really care, they should do their own measurement.
And they can do that, if you're using OKHTTP, by basically just, you know.
Counting the bytes in and out.
**Jason Plumb** 34:18 I still want to understand this bias, so the idea is that if you have
let's say two phones, your user base is literally two users, and one user lives in a metropolitan area and has Wi-Fi and 5G everywhere they go.
and the other person is, like, on LTE or nothing most of the time, then the way in which that data is biased, even if those two users are doing the exact same user experience, it's the age of the slower ne… like, if we had provisions to not export data when the network's slow.
Then the data is accumulating more on disk for the slow network user.
and has a higher risk of not ever being exported because, that stuff is pretty time-limited. So eventually, even if they, like, drive into town two weeks from now, get on Wi-Fi, some of that data is likely to have been lost, and that is the type of bias that you're describing.
**Hanson Ho** 35:11 Correct, yeah.
**Jason Plumb** 35:13 Okay.
**Hanson Ho** 35:13 sampling bias, I think, is the.
**Jason Plumb** 35:16 But the data collected should be the same, right?
**Hanson Ho** 35:18 Yes, yes.
**Jason Plumb** 35:19 looking at what the open telemetry…
**Hanson Ho** 35:22 instrumentation is doing. That should be identical for those two if they're doing the same things. It's just that it's on disk for longer on the slow network.
**Jason Plumb** 35:30 And it has a risk of being
Corrupt, it has a risk of the session being considered invalid by the backend, or whatever other stuff happens when data gets old.
**Hanson Ho** 35:40 Yep. Okay. So, yeah.
**Jason Plumb** 35:42 So it's maybe less of a bias and just, like, Data aging out.
**Hanson Ho** 35:47 You can call it sampling bias. The data collected aggregate will contain a sampling bias towards devices that have good connectivity.
**Jason Plumb** 36:00 Yeah, okay.
**cleverchuk** 36:02 But, I mean, that shouldn't prevent us from, like, letting the developer choose.
**Jason Plumb** 36:08 It's true.
**Hanson Ho** 36:09 It's… it's a foot gun. This is something people don't consider.
collect tele, especially when they say… if they use things like, what's the P50 startup time?
Or, you know, what are the characteristics of usage? And if you're basically saying you're gonna get 75% data from folks with good connectivity and 35% from folks with bad connectivity, it's gonna seem better than it would be.
It is a very subtle foot gun, which is why,
I think document… documenting and being transparent is the way to go, and not try to… not try to be smart.
If they…
want to be smart and, you know, configure their, their, their, their, their, their flushing based on, you know, network or something like that.
No, I don't even… no, I don't even support that, it's…
It's a foot gun. We have to… we have to be opinionated in some areas, and I think this is… this is an area we need to be opinionated on.
**Jason Plumb** 37:15 Yeah, I don't disagree, but I also want to…
see if there's some… some wiggle room for people that are like, I can't use OpenTelemetry. Like, if it becomes a non-starter.
Cleverchuck, do you have any specific examples of this, of this coming up in a real app, in a real network, in a real country, or anything?
**cleverchuk** 37:36 Oh, I don't have a specific example, but, a region, like, in Africa.
Would… it would be pretty difficult.
**Jason Plumb** 37:45 Can you say that again? You're a little bit muffled, and I didn't catch that last part.
**cleverchuk** 37:49 Can you hear me now?
**Jason Plumb** 37:51 Yeah.
**cleverchuk** 37:53 Well, I'm just saying, like, in regions, like, in West Africa.
**Jason Plumb** 37:57 Yeah.
**cleverchuk** 37:58 It would be pretty, like, difficult for someone to, like, use your app if, when they turn it on, it eats up all their data.
**Hanson Ho** 38:06 it's actually not that… especially, like, if we don't GZIP, we should GZIP, because telemetry is actually a very small amount of data, even on 2G, typically, it's… it's not the bandwidth, that makes things slow in… in… well, I shouldn't say that.
The amount of data you would get from,
API calls, and anything that involves an image. Like, you download one image, and this is…
it's all the data you need. Like I said, it's a couple hundred K. If… if…
if your app can't endure a couple hundred K, of telemetry.
then you probably shouldn't use this, because you're a very specialized use case.
So, bit of background. I got started on Android and performance, at Twitter, working on specifically this problem, which is, folks in 2G environments, in developing, or emerging markets, who have, bandwidth issues, and so they have, like.
50 megabytes a month, or 100 megabytes a month, so they're super careful about this. And the analysis was that telemetry is such a small part, that,
If you can use 3MB for your app, and, you know, we happen to use 100K, that's kind of the cost of doing business.
And you can't really avoid it.
And this wouldn't really be the camel that broke the… the straw that broke the camel's back, unless your camel was really, really weak.
In which case, there's nothing we could do to help.
Other than GZip, like, if we don't GZip, we should definitely GZIP.
**Jason Plumb** 39:48 Hanson, is it a fair comparison to compare downloading, like, a several megabyte asset, to uploading telemetry? Because aren't the networks asymmetric?
Like, in terms of bandwidth. Like, a low-powered handset device probably doesn't have the same bandwidth capabilities as the tower, right? The tower's got a lot more power. I'm assuming there's an asymmetry there.
**Hanson Ho** 40:12 So, if we're talking about data costs, uploading…
**Jason Plumb** 40:16 Cost, I'm more concerned with capacity or capability.
**Hanson Ho** 40:19 So,
That's definitely true, but again, the upload capacity… like, the amount of data we're talking about, we're uploading is… is pretty small packets, like.
20K or whatever, especially with GSA. So, you kind of need to do that type of uploading, even for things like login and other things. So, if we're talking about uploading assets, like an image, that's…
You know, if we have a screenshot capability, and, you know, which we don't, but if we do, that's that kind of thing that we should, like, block or limit, you know.
And bandwidth. And that's easier to, to justify because, you know, it's very explicit. You're not getting this data if your network is X. So you're not gonna, you know, you're not gonna be, like, mis… being misled into this.
But since network, yeah.
**Jason Plumb** 41:18 So that led me to think that I was wondering if, like, I think we're speculating a little bit because we haven't measured it, or I haven't measured it with OpenTelemetry and the data being produced to kind of get a sense of what it looks like.
So if I, like, if I just start up an app.
we record some session events, we might, you know, have a little bit of, like, startup telemetry. How much… how much actual data does that look like?
Something that has been brought up before, Cleverchuck, is that we…
Definitely have no throttling on…
the exporting of data from disk, so when we come, we look at all of the stuff that's on disk, and if we are now on network, and we're clear to send, we basically send as much as we can as fast as we can. And that, I think, there is an issue open on the disk buffering side of things, I think.
Because I do… I think there's probably value in trying to throttle that.
But let's make sure that that issue is there.
**Hanson Ho** 42:19 we only use one connection, right? We don't try to, like, max out the connections.
**Jason Plumb** 42:25 I don't believe so.
**Hanson Ho** 42:26 Okay.
So, we don't really have fine-grained control over bandwidth. All we could do is basically delay sending, or… and also restrict the parallelization. So, if we're already restricting the parallelization.
You know, we're doing our job. You know, sending a chunk of data.
and then waiting a bit of time and sending a chunk, you know, who knows when the user's actually using the network? As long as we're not sending it, like, right at startup, and then delaying app startup because we are too busy sending data while the screen is trying to render the first frame, I think we're okay.
**Jason Plumb** 43:07 Yeah, so I was… I was wrong about this being in the disk buffering repo. It's in Android.
**Manoel** 43:20 Are we measuring the quality of the…
internet, it's pretty hard, like, on mobile, you barely know if there is internet, you just know that the Wi-Fi is connected. So, I think ideally, maybe a configuration of
chaining the data over the wire, if the Wi-Fi is enabled or not is a fair game. But otherwise, you just kind of tell customers to, hey, you know, if it's too much data, just disable a few features, experiment less. It's up to them, because we never know how much data they are capturing. It really depends on their app.
Their instrumentation, and all of that.
Maybe we could have some benchmarking of, hey, if you have disabled in your normal app with 10 screens that do that.
We capture, let's say, 50 kilobytes of data every 10 minutes, just as a shark idea, but more than that, it's hard to tell.
**Hanson Ho** 44:11 With data we've seen from Brace, 95% of telemetry, if not higher, is network requests. So, you could basically, if you can… if you could…
if you could kind of optimize the types of network requests, or the endpoints, or, you know, whatever, that you would, you want telemetry for, for network requests, that will basically get you most of the way there. Everything else is… makes up a small amount.
But I think having some numbers would be good, so if anything, we should allow the… we should somehow expose the ability to track, data usage, which could be done, again, by counting the bytes across the wire, in an OQTTP, event listener.
**Cesar Munoz** 45:02 Okay, I give up. I was trying to find whether GZ bits enabled by default. I couldn't find anything. I did find that it is supported upstream.
But I'm guessing it's not enabled by default, so… Yeah, bro. It's not F2.
**Manoel** 45:23 Yeah, you have to add the interceptor I shared on the messaging thread.
**Hanson Ho** 45:28 But this would be controlled
Is this controlled by us, or is this controlled by the… because do we initialize our own copy of the HTTP client? Look at HTTP client?
If we do this.
**Cesar Munoz** 45:40 Nope.
We… so it's… it's handled upstream when… when we're creating the, the instance of the exporters. So…
**Hanson Ho** 45:50 It's the exporters.
**Cesar Munoz** 45:51 Builders have this set compressor.
etc.
And I think you just have to pass a string with GCP.
**Hanson Ho** 46:02 So folks can… so folks can basically, with our package right now, configure it so that the payload is gzipped.
**Cesar Munoz** 46:11 Well, actually, you're right. We have the intercept, the… yeah, the interceptor for the exporters.
**Hanson Ho** 46:18 There you go.
**Cesar Munoz** 46:18 But… but it's not for the initializer, that's for core. So, maybe in the initializer, we should call this method.
**Hanson Ho** 46:25 We should just expose it as well, because, you know, some people may not want it, because they're, you know…
they're sending it in-network. Some people may… I mean…
**Jason Plumb** 46:33 Yeah, like, what if their… what if their backend doesn't support it for whatever reason? Also, presumably, people that are doing direct ingest will be wanting to use TLS, and you kind of get some compression for free, I think, with that.
**Manoel** 46:49 I think the interceptor has to be clever enough to read the accept encoding.
**Jason Plumb** 46:53 Right, yeah, exactly.
**Manoel** 46:54 Let's just do it.
**Jason Plumb** 46:59 Yep.
**Hanson Ho** 47:03 So I think maybe we should create an issue here and get some more clarity.
**Cesar Munoz** 47:09 Yeah, and I don't think it should be a blocker for RC1, maybe it can be added to RC2, maybe?
**Jason Plumb** 47:14 Yeah, or later, I mean, it's an add-on. We don't… I don't think it has to be, like, a default setting.
**Manoel** 47:23 Yep.
**Jason Plumb** 47:25 And I'm not even sure if enabling GZAT by default would be breaking, per se.
**Manoel** 47:34 It reads the… so, the way how it works is, HTTP does request, read its headers, and then just do the encoding if the server accepts. So, I would say it's not a breaking change unless the server tells it accepts, but it doesn't, right?
**Jason Plumb** 47:49 Yeah, I think I agree with that.
**Hanson Ho** 47:52 when OKHP initially connects, it'll negotiate from… or it'll know from the… from the… from the initial, you know, response from the server, what it accepts, right, from the headers. And…
that will send GZIP if it's possible, and not if it doesn't. So, like, this theoretically should be handled at a layer that we don't have to be responsible for. We just have to set the configuration if we… if we don't expose it, right?
**Manoel** 48:21 Yep.
Chocolate.
**Jason Plumb** 48:24 Okay, Hanson, do you want to create this issue?
**Hanson Ho** 48:26 Yep.
I will do it next Tuesday morning, like I did with the other issue, which I did today.
**Jason Plumb** 48:35 Cool.
Yeah, I added this comment, but I think it would be an interesting experiment just to, like, fire up the demo app, even point it at a local collector, with kind of the stock settings that we have in the demo app, and, just measure it. Just, like, click through, send a couple of events, add some stuff to the cart.
do a checkout, and just see what that looks like. Like, how much…
How much total bandwidth was used?
And disk buffering definitely complicates that, right? Because if you're clicking slowly and methodically, and you get an export, you might get two exports, whereas if you know the demo app really well, and you just sort of click through, all that stuff's on disk, and it will come out all at once.
About the same number of bytes, probably, but it would be, like, two export cycles versus several, or, like, one export cycle versus more than one export cycle.
**Cesar Munoz** 49:31 Or you blows up.
**Jason Plumb** 49:33 It'd be interesting to measure that and publish some results.
**Cesar Munoz** 49:36 You could also, alternatively, Turn off the internet.
From the device you're using, and then just check the files created by this offering.
To their size.
That could be another.
**Hanson Ho** 49:52 Oh, interesting.
**Jason Plumb** 49:52 That is a good… that's a reasonable data point, because we store the protobufs, but that doesn't fully… it won't match identically to what's on the wire, because of…
**Cesar Munoz** 50:03 True.
**Jason Plumb** 50:04 But it's, like, it should be pretty close.
**Cesar Munoz** 50:09 I think having some… No, I think having some data with, like, one envelope with 100 spans versus one envelope with one span, and, you know.
**Hanson Ho** 50:16 Again, we just need some data.
**Jason Plumb** 50:20 Yep.
And to Manuel's point, measuring the internet is hard.
**Hanson Ho** 50:26 Yeah, bandwidth, you can't… you can't really measure bandwidth, because it's first false dynamic, so what you have to do is basically, look at the history, like, you know, do some math with the last n requests, and that's assuming that the…
network doesn't change. So you do, you know, some sort of, you know, decaying back off, and say, hey, it fluctuates, it'll catch up, but it's… it's an exact science. Just because it says you're on, you're on 5G doesn't mean you have good,
latency and bandwidth.
**Jason Plumb** 50:59 Yep.
**Hanson Ho** 51:01 The APIs lie, basically.
**Manoel** 51:08 But to measure internets and save some bytes over the Y, you have to download something.
then you're already burning the data, right?
**Hanson Ho** 51:22 But yeah, I think the most important thing is, we should allow, GZIP.
And set it by default, if possible.
**Jason Plumb** 51:30 So, I mean, my takeaway from this is, I mean, we talked a lot about GZIP, and, you know, that certainly helps things.
But there's kind of, like, two concerns here. Like, one being, if we make it a first-class, easy-to-configure.
throttling mechanism that slows down on certain network types, that we think that that's maybe a dangerous foot gun.
At the end of the day, users can configure their own throttling exporter if they want to do the work of getting a throttling exporter in there. I don't hear consensus around us wanting or trying to make this
Like, this feature a priority.
So I would love…
If it comes up in the future, like, if we have real-world applications being deployed with this.
Or we have users that are backing away from it because they think it's too much bandwidth for their users. I would love to hear stories of that, and I would love to especially hear those stories
if they have measurements associated with them. Like, if we can tell
If they could tell how much bandwidth they're using, or how often they're saturating the network, any, you know, anything that gives us real, tangible data.
**Manoel** 52:46 I think that was a major concern 10 years ago. I mean…
probably some remote area STUs, but it's not as much as before, so…
**Jason Plumb** 52:55 But that was the use case that Kleberchuk brought up, was West Africa.
**Manoel** 52:58 Yeah.
**Jason Plumb** 52:59 Yeah.
**Hanson Ho** 53:00 Yeah, it used to be… it used to be an issue with access, performance, and costs. The cost aspect has, a lot of times disappeared, even, like, cheap data packages, you know, are… or rather, data packages are a lot cheaper now for a lot more data.
But that's just because people who, you know, in West Africa, when they use the apps, they're gonna use… they want images, and when you have an app that has images,
Telemetry is going to be such a small part of, of, cost consumption, in terms of.
**Manoel** 53:32 Nope.
**Hanson Ho** 53:40 I think folks… I think folks that care about this already measure it, and they know how much they can and can't use, and they would… they would zip it, because they can also just control it on their side, with the exporter they add, right? So…
But we should just also be a good citizen.
**Jason Plumb** 53:55 Yep.
**Manoel** 53:57 Yeah, investment's not the book.
**Jason Plumb** 54:04 Okay, there's some new activity on this one. This one was… this one was interesting, if, we're just… I'm switching topics, we only have a couple minutes left,
Yeah, this, this is interesting, if you haven't read this yet.
And then this one was… this came out yesterday, and I didn't know how to respond to this yet. It was late in the day, and I was like, I'm not gonna respond to this, but basically…
This person is doing manual tracing, this is what I can tell, is they have some user activity or some user flows that they're wrapping manual tracing around.
Which is fine, and they have this code to do this, but I think they were hoping…
I think they were hoping for something easier, which we don't currently provide.
Yeah…
I don't… I don't know how to respond to this yet. I think there's… I think there are some opportunities for us to make…
wrapping things in spans a little bit easier for people, which… that's, like, some convenience APIs that we don't really have yet, but they can also build their own. Like, what we're looking at is probably their convenience API, right?
The thing I was confused by in this is, like, why they were tracking
I guess they have some re-entering code, or if there's an event handler that fires twice, or… I don't know, there's something where they didn't want the same named trace to happen twice?
**Hanson Ho** 55:28 So, this is a problem that, that probably Jamie or others can probably go into a little bit, but the whole issue of managing contacts.
And managing how spans are propagated, from different components, that aren't related.
Less this one, but the previous one.
**Jason Plumb** 55:50 Basically… Quick curtains, yeah.
**Hanson Ho** 55:52 Yeah, basically, you know, thread-based, propagation of context automatically is just inherently problematic in an environment where execution is
undefined, in terms of path, in terms of intention. So,
I think if we're able to switch to Kotlin, the hotel Kotlin, I mean, we would have a much…
healthier way of managing this by not immediately having this current context that exists, which could be problematic. But even then, it's a bit tricky to figure out, like, what the best way of going forward is. Something like this would be, you know, there's a million ways of…
of being able to pass contacts or parents, or even the same span. Like a named span, for instance. You can have some sort of global repository that returns, you know… there's a bunch of different patterns that have good sides and bad sides, but,
we should definitely think about, how we can support these cases better, because, yeah, the simple use case of, I have a module, that is unrelated to another module, and I have a span.
I don't want to manually pass this stuff in. Can you use DI to kind of inject context and say, hey, this is the parent span from the…
Yeah.
**Jason Plumb** 57:09 Yeah.
**Hanson Ho** 57:09 Many things could be done.
**Cesar Munoz** 57:13 It seems like they just want to have some sort of utility, probably, so that they can manage
Spans by name.
So, they don't have to… You know, carry around the API objects.
**Jason Plumb** 57:30 That's what it seems like, right, with this active spans, yeah.
**Cesar Munoz** 57:33 Yes, maybe that's static fail or something.
**Jason Plumb** 57:36 Yeah, it's hard to tell from this context, but yeah.
**Hanson Ho** 57:39 In the past, what has worked is some sort of shared context. So if we have a more complex trace, you can basically pass around a state machine, and effectively let that
do the span creation and manage it, so you just have to know what you're doing in terms of, I'm starting a flow here, I'm ending it here.
And you can take care of, you know, things like parents and without managing. Something as simple as this, as you said, something like a… something in static scope that they could reference by name.
again, something they could build. If all they're looking for is that level, that's something they can build.
Or something we can build as contribribs or something like that, you know.
Application scope.
You know, thing. Yeah.
**Jason Plumb** 58:29 Well, cool, I think we hit time.
I was just looking at this response because I hadn't seen it yet, but it's in the… it's in the issues if you want to have a look at it.
Yeah, so I think I've got a… I've got an action item to take away. Hanson, you've got one. I think they're both to create tracking issues, and yeah, we'll get the release started.
Thanks, everyone.
**Cesar Munoz** 58:52 Thank you.
**Manoel** 58:53 Thank you, bye-bye.
**Cesar Munoz** 58:54 Hey.
**Hanson Ho** 58:55 But…
