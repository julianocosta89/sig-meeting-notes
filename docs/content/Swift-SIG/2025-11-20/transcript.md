SIG: Swift SIG
Date: 2025-11-20
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Ariel Demarco** 01:01 Dale.
**Bee Klimt** 01:05 Hello.
**Bryce Buchanan** 01:45 Hello, sorry I'm a little late.
**Ariel Demarco** 01:52 I'm Rice. How are you?
**Bryce Buchanan** 01:54 Good, how are you doing?
**Ariel Demarco** 01:57 Good! It's starting to rain here, so… Posting everything.
**Bryce Buchanan** 02:02 Oh, yeah.
It's just been getting really cold here.
**Ariel Demarco** 02:11 Oh, really?
**Bryce Buchanan** 02:13 Yeah, not quite freezing, but… but close.
**Ariel Demarco** 02:18 Here is… Spring, so weather is…
One moment is sunny, the other is raining, so…
**Bryce Buchanan** 02:27 Very nice.
Alright, I suppose we can get started.
Alright, topics from last week. Crash issue discussion. I don't believe there was any follow-up for this,
I don't… and I don't believe…
the individual that brought the topic is here, so I think that we can just skip over that.
Repo status update.
Oh, I guess that's just… The usual thing.
We don't really need to… that doesn't need to be on here, really. Okay. Billy, new topics?
**alexcohen** 04:40 I, I guess somebody, I, I just added that, this morning, someone pointed out that, I guess they, they released their, their OpenTelemetry Swift
Library. I went through it, it's pretty cool, it's well-written, so thought I'd just, you know…
Mention it. That's all.
**Bryce Buchanan** 05:00 Oh, right on. Do you have a… do you have a link to it?
**alexcohen** 05:03 Yeah, I'm looking for it now, I'm trying to get the link back to it.
**Billy Zhou** 05:06 And I'll… I'll give a… at the link.
Yeah, thanks.
**alexcohen** 05:10 Yeah, pretty cool.
**Billy Zhou** 05:11 I'll be a lot more free now. Yeah, I was like, I couldn't say anything, but…
Yeah, I was, I have a lot more free time, though.
**Bryce Buchanan** 05:23 Right on.
**Billy Zhou** 05:30 Yeah, Alex already submitted the first issue. Thanks. Thanks, Alex.
He's so sharp.
**alexcohen** 05:45 Should be an easy change for you.
**Billy Zhou** 05:50 Yeah, I didn't see that, so thanks. Super good suggestion.
**Bryce Buchanan** 05:58 Very cool. Very cool.
Are there, any other topics that anybody wants to discuss?
Right, if not, then maybe we can just go through… Open issues…
Oh, this looks like a new one from last week.
URL session instrumentation not in place when using KTOR client.
Not to be confused with KOTOR.
**alexcohen** 06:38 What is KTOR?
**Bryce Buchanan** 06:41 I don't know, I've never heard of Ketor before.
**alexcohen** 06:43 Me neither.
**Ariel Demarco** 06:45 It's, like, it's like there,
the library for all the routing and handling requests and executing requests in Kotlin. It's used in Kotlin multiplatform, but it's also used for microservices.
**Bryce Buchanan** 07:06 Oh, well, it would make sense that we, do not instrument it, then.
**Ariel Demarco** 07:12 It depends, because under the hood,
Gator uses Darwin and uses URL instrumentation, so it should work.
I can do some follow-up. Also.
I was asking internally when I saw this issue, because at Embrace they are doing the… the OpenTelemetry Kotlin.
Repo, so maybe it's part of instrumentation that they may want to do at some point.
Instead of us.
**Bee Klimt** 07:46 I don't know if it's related, but yesterday afternoon, I discovered a few cases, like, a few ways of using URL session, where the auto instrumentation used to work, but now doesn't find anything, so I'm gonna…
**Bryce Buchanan** 08:01 Oh, interesting.
**Bee Klimt** 08:01 Is that an open issue? I have no idea if it's the same thing they're running into, but it's possible, I guess.
**Ariel Demarco** 08:08 Okay.
That's curious.
**Bee Klimt** 08:13 Yeah, I have no idea which commit made it stop working either. None of them look particularly suspect, but…
We'll see.
**Bryce Buchanan** 08:42 Okay, interesting.
Yeah, that'll be interesting to see what comes of that. I also suspect that they might be using, like, the default URLs.
Session implementation, which,
Is a problem as well, since the system initializes it, and, we generally cannot instrument
URL sessions that have already been instantiated.
So that could be a problem there.
It's probably related to methods by the method.
When used by the Darwin engine, yeah. Yeah, it could be.
Okay. Well, I guess, B, if you find anything.
Please mention it on this issue.
Otherwise, we can follow up again.
Okay, still haven't made any progress on this. I guess I've made a PR, but I haven't done any verification on this one yet.
That needs to get reviewed.
Food.
And we just haven't received any feedback on that one.
And, let's see here… Here.
I guess Nacho's not here today to give us an update on that one.
Receive response. Doesn't seem to have data. Ariel, have you had a chance to look at this at all?
**Ariel Demarco** 10:45 I wasn't able to reproduce it, that's…
Basically. So, even though there are some cases where, obviously, you don't receive data because of the async nature, on the ones that are expected to receive it.
I was able to, so… I… I have some other cases, or some other ways to try it out, but…
Wasn't fully able to do.
So maybe I'll reach ba- reach out.
this… Agar.
To… to actually see if he can help me out on doing the repro.
**Bryce Buchanan** 11:25 Yeah.
That might be the next step, is asking for a reproduction.
**Ariel Demarco** 11:30 That said, there are some limitations based on how we capture
There are some limitations on how we capture the async request, so some data, we are not going to receive them.
Bob.
Regardless of that, that doesn't seem the thing that he's reporting.
**Bryce Buchanan** 11:58 Okay, so implement metric filters. Vinod, have you made any progress on this?
**Vinod Vydier** 12:03 No, I haven't actually got to.
do much with this much time. So, yeah, I will… I think if someone else wants to pick it up, let them, you know.
Take it up.
But yeah, I… Okay. When I get back on this, I'll… I have been…
Kind of busy with other things, so…
**Bryce Buchanan** 12:27 Yeah, I know… I know how you feel.
I am in the same boat.
let's see…
Have you… have you had a chance to review this response, Ari?
**Ariel Demarco** 13:00 Oh.
IV and T-Venom.
So that one My bad. But I think that this is… this is related to the new one.
**Bryce Buchanan** 13:11 He said that, he's still seeing the race condition in 2.0.
**Ariel Demarco** 13:18 Hmm. Okay.
Yeah, sure.
I can't check it out. I have the sample project already graded, so it's just checking.
**Bryce Buchanan** 13:28 Cool.
**Billy Zhou** 13:29 Yeah, what do you guys use for, threat safety?
Do we need a sample app in the… in upstream?
**Ariel Demarco** 13:43 Can repeat.
I, I didn't listen.
**Billy Zhou** 13:47 I was just wondering, like, what do you guys use for, for testing? I'm sure everyone has their own sample app, but, like, do we need a… do we need a sample app in Upstream for, certain features, or… for testing?
**Bryce Buchanan** 14:01 it's not… it's not a terrible idea. I use a,
I use an app that I threw together for Elastic. I'm not sure if it's public or not, actually.
Oh yeah, it is, okay.
So I have this sample app that I use, OptBean Swift, that kind of, you can hook it into some of the other,
elastic, like, testing applications, although I think this might be deprecated. But there's, like, some, like, a whole slew of, like, opbeans
like… Like, applications, like, there's, like, a web server, like, I think Node… opens Node, maybe? Yeah.
So,
the iOS app populates data with… with this OpBeans node, and it's like… it's like a coffee service, you know, you can buy coffee on it.
**Billy Zhou** 15:05 Oh, sweet.
**Bryce Buchanan** 15:05 simulated APIs.
But, yeah, I'm… I haven't really updated it in a long time, so…
But that's what, that's what I use to test against.
**Ariel Demarco** 15:21 I just use our desktop.
of our CK, and just import.
the things from OpenTelemetry I have to test, and that's it.
**Billy Zhou** 15:31 Oh yeah, the one with the game and everything, right? I think I saw it before, yeah.
**Ariel Demarco** 15:35 Yeah. Yeah, exactly.
**Billy Zhou** 15:36 Yeah.
Cool.
Thanks.
**Bryce Buchanan** 15:44 Okay…
I haven't had a chance to really dig into this either, Yeah.
Just need to find some time. It's been… it's been busy over here with internal stuff.
Grpc 2.0, I don't think that we've made it…
That probably needs to get replied to.
**Ariel Demarco** 16:47 Does it change a lot, gRPC 2.0, do you know?
**Bryce Buchanan** 16:57 I think that there is a few… I think it uses, Swift 6, so that might be the blocker with this project, particularly. I don't know off the top of my head.
**Ariel Demarco** 17:08 Okay.
**Bryce Buchanan** 17:10 Yeah, I think that's the problem, is that it requires an upgrade to Swift 6.
**Ariel Demarco** 17:15 I see.
**Bryce Buchanan** 17:34 And then we have all these, reviewing projects.
Which is just…
Verifying that our implementation is still within the spec, as things have changed since the original implementation.
Mmm… okay.
Yeah, so we do have a lot of those.
Yep, yep, yep, yep, yep. Lots of stuff, lots of stuff to do, and so a little time to do it.
And then, of course, you know, we just have all of these…
I keep getting interrupted by minor changes. I wonder if there's a setting Where we can,
merge something without… like, if it…
If it's not, no, of course.
**Ariel Demarco** 18:44 What? Yes, you can disable that.
**Bryce Buchanan** 18:47 Is this because…
**Ariel Demarco** 18:48 You've done it.
I don't have access to.
**Bryce Buchanan** 18:56 It's really bizarre, I wonder what… has anybody else been speaking that?
**Vinod Vydier** 19:01 Yeah, I think you have to keep it in sync, your branch, right?
**alexcohen** 19:09 What's the issue?
**Bryce Buchanan** 19:11 Oh, I don't know, for some reason, I've been getting this issue if I try to do, like, an update.
**Ariel Demarco** 19:16 Because you are… you are forced to fork right now, and this is from an internal branch.
And you are forced to fork in order to get the ECC.
**Bryce Buchanan** 19:27 Oh, I see. Yeah, I gotcha. Okay, I need to stop doing that.
**Ariel Demarco** 19:34 Happened the other day, Adam.
One of the GCs told me.
**Bryce Buchanan** 19:40 What is it triggered?
**Vinod Vydier** 19:42 So, what is the issue again?
**Ariel Demarco** 19:45 You have to fork in order to make a contribution.
**Bryce Buchanan** 19:50 Yum, yum.
This needs to be, resolved, Vinod, so if you could,
Fix that, and then we can merge this.
**Vinod Vydier** 20:01 Oh, girl.
Let's see…
**Bryce Buchanan** 20:06 What else has been approved? This has been approved.
Please just merge. There we go, okay.
I believe there is also,
a way… Isn't there also a way to, like, rebase if there's no… if there hasn't been any, like, changes in the files?
in the PR on the main branch.
Isn't there just a way that, like, so it doesn't always have to, like, so we don't run into this thing where it just needs to update the branch, rerun everything constantly, just takes forever.
Especially when it's, like.
**Ariel Demarco** 20:51 A minor, like, it's totally an unrelated change to the rest of the repo.
**Bryce Buchanan** 20:56 So, there's an option in GitHub.
**Ariel Demarco** 20:59 But I don't have access in those settings to actually make a change.
**Bryce Buchanan** 21:04 Okay, I'll… I'll look into that.
**alexcohen** 21:07 Could also change the, the workflows a bit to not react to things that are… the things that we don't want them to react to.
If you will.
**Bryce Buchanan** 21:17 Yeah, that's true too, yeah.
**alexcohen** 21:19 everything.
**Bryce Buchanan** 21:21 Yeah, that's another solution.
Okay,
And I'll… I'll look into that.
Alright.
I think that can speed up this… all this blocking that's been going on.
Okay, let's see, any other… any other topics we'd like to discuss?
**Bee Klimt** 22:37 You… you mentioned Swift 6. I was just wondering if there's any update on that, or, like, what the next steps are?
**Bryce Buchanan** 22:46 I think that we just need to bite the bullet and start working on, migrating to Swift 6.
I don't think that there's…
Like, I'm not sure if there's any, like, trade-off for it, like, we won't be able to build for older versions of Xcode or what, but…
I think it just is something that needs to get done, and it's a little bit of…
A task, so nobody's had time to really take that on at the moment.
**alexcohen** 23:19 I haven't tried this yet, but I think you can support, multiple packages, like, if you put the, like, package at 5.9 or something like that, and package at 6.0, and whatever… whatever you… whatever's importing it through, will support that, so, like…
We could start a 6.0 pretty easily and keep what we have without changing anything, I think. But I also believe, I don't know if anyone's tried it, but.
**Bryce Buchanan** 23:47 Yeah, that's not a bad idea.
**alexcohen** 23:51 We just changed to 6.0. I don't think there's gonna be a lot of issues with the code. It's when we get to, like, 6.1 and 6.2 where things go a little bit nuts.
At least that's what I found when trying it.
**Bryce Buchanan** 24:07 Okay, okay. Yeah, actually, we've done that in the past, where we've had different packages for different versions of Swift,
But, I think, yeah, that's not a bad idea. Maybe now that we have Swift Core, we could just try even, adding a 6.0 package Swift to Core, and see… just see how that goes.
Yeah.
**Ariel Demarco** 24:33 Shall we dig, 6.0, or shall we just jump to 6.2 directly, considering all the changes they… they made to make it more approachable?
**Bryce Buchanan** 24:45 I would say, let's…
Try initially with 6.0 and see how bad it is, and if it's not too bad, then bump it up to, like, 6.1, and if it's not too bad…
Bump it up to 6.2.
**alexcohen** 25:10 6.2 might be rough.
**Bryce Buchanan** 25:30 Does anybody wanna, b-point on the… on this, like, sort of POC for Swift 6?
**Billy Zhou** 25:40 Yeah, I have a lot more free time now, I can,
Give it a sub if you want.
**Bryce Buchanan** 25:46 Cool. Yeah, that'd be awesome, Billy, thank you.
**Billy Zhou** 25:49 Cool. I also had a quick question, do you know what the… if there's any, pink telemetry standard for, log sampling? I've noticed that, like, Android SDK doesn't have it either, and I don't think we do either. Is it… is it typical? Or do we… are we just locking, like, instrumentation for it?
**Bryce Buchanan** 26:10 I think we're just lacking instrumentation for it. Part of…
Part of the reason we haven't decided to really, entertain that is, like, a blanket logging solution for mobile,
I think it's kind of viewed as a bad idea, just because it can produce way too many logs from so many different devices, depending on how popular your app is.
But I'm not… I'm not sure, if that is actually, like, a concern that, downstream users actually have or not.
So…
**Billy Zhou** 26:48 Oh, is that for, like… Like, just, like, normal logs instead of, like, log events.
**Bryce Buchanan** 26:55 Yeah, is our… yeah, maybe… is that not what you're referring to?
**Billy Zhou** 26:59 Yeah, I guess,
I guess for AWS itself, like, we only do log events, so I wasn't thinking about, like, logs in general.
Okay, yeah, I'll give it some thought. I was, like, working on upstreaming some stuff yesterday, like, like session sample rate, for example. I think it's, like, a feature people typically want, and…
for, for ADOT, like, I did, like, a workaround to get some log sampling, but, yeah, I was wondering whether or not I should upstream that, since we don't… we didn't have, like,
I didn't want to upstream something hacky for it, so.
**Bryce Buchanan** 27:41 I mean, if it's… if it's some instrumentation, I'm sure somebody would find it useful.
So don't, yeah, don't be hesitant to upstream stuff.
**Billy Zhou** 27:51 Okay, cool.
**Bryce Buchanan** 27:53 Yeah, right on.
Any… anything else?
Going once, going twice?
Oh, go ahead.
**Billy Zhou** 28:09 Oh, no, nope, I'm just saying I don't have anything else.
**Bryce Buchanan** 28:12 Oh, okay. All right, well, I suppose we could, call it here. Just remember, if you have any free time, we've got lots of issues in the… in the issue, as we all saw, so…
Snag something if you can.
I know I'm trying to find free time to do it myself, but it's just been… just been swamped. But hopefully, maybe with the holidays, they'll be a little less busy.
**alexcohen** 28:36 Alright. So you're gonna work on the… during the holidays and make yourself busy?
**Bryce Buchanan** 28:41 Oh, no, I, you know, during, during work days during the holidays.
**alexcohen** 28:44 Yeah.
**Bryce Buchanan** 28:45 I don't know, I feel like, you know…
**alexcohen** 28:47 Rally.
**Bryce Buchanan** 28:49 I think, I think most of them are, yeah, like… Good,
especially, like, these trace… like, these ones are, like, reviews, of our ins… of our implementation, so I think that just…
spending some time and just reviewing the actual spec and seeing what our… our implementation is doing, like, that's really all that needs to get done here. And either you can close them or… or elevate them to a not, like, you know, not review, but, like, this, like, what needs to actually get fixed.
So that… those ones, like.
I don't think necessarily will take too much time once somebody buckles down and does it. But, yeah, I mean, I don't know, I feel like…
There's always a big, like, rush to get stuff done right before the holidays, and then there's, like… they're not taking 4 weeks off, you know, there's usually not a lot to do.
When you're actually in the office, so…
Because everybody else is taking 4 weeks off.
**alexcohen** 29:54 Okay, cool.
**Bryce Buchanan** 29:55 Sounds nice. Alright, well… I guess that's, all we have for today.
So I hope everybody has a good weekend!
See you later.
**Vinod Vydier** 30:09 Oops, you know.
