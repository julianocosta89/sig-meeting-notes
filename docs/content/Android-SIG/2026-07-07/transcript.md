SIG: Android SIG
Date: 2026-07-07
Duration: 44 minutes
============================================================

## Zoom Recording Transcript

**Jason Plumb** 00:51 Good morning.
I'm finishing up a little bit of food.
**JM Jason Morris** 00:55 Good morning.
**Jason Plumb** 00:57 Keep my camera off for a little bit.
Well, people join in.
**DavidGrath** 01:11 Good evening.
**Jason Plumb** 01:15 Hey, David.
**Cesar Munoz** 01:17 Hello.
**Jason Plumb** 01:19 Hi, Cesar. Hi, J.
**Cesar Munoz** 01:23 8.
**Hanson Ho** 01:38 Hello.
**Cesar Munoz** 01:41 Ito hasn't.
**Hanson Ho** 01:46 Sorry for missing your messages yesterday, Jason, but I see David got it.
**Jason Plumb** 01:50 Yeah, it's all good, we made it happen We also had some coverage from Japan over in Colin. It was great.
**Hanson Ho** 01:59 Nice.
**Jason Plumb** 02:04 One more minute.
Yeah.
Please add yourself to the agenda, and any topics that you have.
Yeah, I friend-loaded a few things.
This is me being cheeky. I don't think anybody's actually scared.
But I opened this a while back, and it's been sitting there.
Without it. Well, David looked at it recently, but.
Yeah, Yeah, please have a look, you know, I described kind of what the deal is here, and it's not, you know, it's not that big, but… This is analogous to… An SPI.
That allows for configuring specific instrumentations.
So, oh my gosh, Jamie!
Welcome back, stranger, and also congratulations. Yeah. Thank you.
**Cesar Munoz** 03:13 That's.
**Jason Plumb** 03:21 So I don't want to belabor this too much. It's out there for you to look at. Hopefully the idea is pretty clear.
The idea being that if you have instrumentation somewhere on your class path, right, we have this thing that will automatically load those for you, if you annotate them correctly.
If your instrumentation has some additional configuration that needs to happen before it is installed, there's currently not a great way of doing that. So this adds, like, another SPI, and you can implement… an instrumentation configurator, and the type specific instrumentation.
and the instrumentation name that you target, and then you will be called configure. And that's in the contract there is that it's invoked before install is called.
**Cesar Munoz** 04:09 Oh, nice.
To be honest, sir, I probably just… Took a glance at it, but… missed the details.
**Jason Plumb** 04:19 No, that's fine, but that's why I bring it up. I mean, we all get busy and it happens.
**Cesar Munoz** 04:24 Yeah, no, thanks. Thanks for bringing it up. It's so it's basically so.
With this SPI, any user can… configure instrumentations, even though… They don't, Right, even though they might be just added by the… the agent, or… Whatever else they can choose.
**Jason Plumb** 04:50 True.
**Cesar Munoz** 04:50 Hook this in and… right.
Sounds good.
I'll take a look.
**Jason Plumb** 04:56 Cool, thank you.
And maybe I should rebase this one if we have Codecov. Actually, Codecov is fine. This was before CodeQL broke. That's how long it's been sitting out there.
Okay, Next thing on the agenda, I think, is also me.
Yeah, so, oh, what a smooth transition that I did not plan for, but yeah, in case you haven't noticed.
Codeql has broken everything for us.
Okay. It was off.
Yeah, it was after that Kotlin 2.4 PR got merged, so all of these that are red, I can just tell you, because I've been looking at this, like, all of this list of reds is due to CodeQL.
like just I'll pick like this one, for example. Well, that might be a bad example. But CoQL will also be broken.
Okay, bad example.
Here's one.
Just a linting PR.
And yeah, CodeQL. So we're waiting on a fix, Just so you know, so that's been disabled for new PRs, and that's a temporary thing that I did, and please help me keep an eye out for when that CodeQL update comes through.
this thing… And here's the tracking issue for you to follow if you haven't already.
And then, yeah, they haven't released it yet. I think… I imagine this will close once they release.
**Cesar Munoz** 06:43 Yeah.
I mean, but it's not the first time it happened.
**Jason Plumb** 06:48 No.
**Cesar Munoz** 06:50 So, I really would like to know if there are alternatives to GoQL.
**Jason Plumb** 06:57 Same.
**Cesar Munoz** 06:58 Every new Kotlin version, they take forever.
**Jason Plumb** 07:02 Yep.
Okay, I want to revisit a topic that we talked about a week or two ago, and I have one other thing, around… this thing. Hold on to the end.
So… Right, so we discussed this previously, and the idea was, hey.
are we… why are we checking all of these generated sources into source control, right? We have these protobufs, well, we have… we have these YAML files that Weaver is then generating source code from.
Wouldn't it be cool if we just, like, built those in a jar, and then we don' source code files that say, do not edit, you know, and just, like, mucking up and taking up space in the repo and matching searches and everything else.
Can't we just bundle it? And I was like, that's And I did that, I tried it, and it worked out, except for… It then requires every person who's building this repo to have Weaver.
So, that was like an… that was a short… like, I… you know, this meeting's also at 8 o'clock in the morning, I'm never thinking very clearly, but… I didn't consider that aspect of it, right? So, if you put… if you put this in the path of needing… if you need to build these every time, because the sources aren't available, then you have to have Weaver available. And I didn't want to put that burden on every developer and every CI build, because it's kind of cumbersome.
So I wanted to bring that up,
**Cesar Munoz** 08:34 There's coincidentally, I created a PR just 5 minutes ago, that… Addresses this.
It's, well, let's just… Checking some co-pilot reviews, which… To be honest, we're surprisingly good.
But essentially, that… Takes care of what you just said.
It's… it's an alternative.
And, you know, it helps preventing checking stuff in Git. And also, I think it helps preventing CI changes that… I think you added in a… in another PR?
**Jason Plumb** 09:19 Yeah, yeah.
**Cesar Munoz** 09:20 I'm in there I mean, he works… And, yeah.
It's an alternative.
**Jason Plumb** 09:29 Cool, this… Yeah, I wanna see the clips of whenever…
**Cesar Munoz** 09:32 Take a look.
**Jason Plumb** 09:33 Yeah, is this architecture aware? Like, it knows the difference between x86 and ARM, like, it knows which binary to install and all that?
**Cesar Munoz** 09:40 Yes.
**Jason Plumb** 09:41 Okay.
Cool, yeah, I will take a look at that too, that's Yeah, so the… the burden of needing Weaver, then, like, by your PR, would be lessened, because it's just sort of done for you automatically, just like needing Gradle, you know? You don't need Gradle when you use the wrapper. Okay.
**Cesar Munoz** 10:06 And and just like just like Reddit rapper.
It's only installed in the project, so it's not like… my changes don't… you know, change the OS like they don't install OS apps or something like that. Just like Reddit wrapper.
**Jason Plumb** 10:28 Cool. Yeah, that's great. I think Cesar was also referring to this PR, which the idea was that if you're… If you're committing the source code to the repo, which is the current approach.
if somebody makes a change to Weaver and they don't regenerate those sources, then you could have a mismatch, they could get out of alignment. And so this… is like a build step that makes sure that if you have changes to those files that it'll fail the build. So you have to run it.
But this approach then, or your, your other, your PR sensor that I've already closed the tab for, alleviates the need for this.
**Cesar Munoz** 11:05 It's true.
**Jason Plumb** 11:06 Yeah, so.
**Cesar Munoz** 11:07 So yeah, when are you?
I mean, please take a look, I'm not sure, I'm fully sure, but it.
**Jason Plumb** 11:17 Yeah, so that is, I think, a… Khan, right?
And then pros of… Having it in there, I don't know. What are the pros? You don't need Weaver. That's the only pro.
Cool, I mean, at first glance, it sounds like this is a great thing, and I will take a look today.
**Cesar Munoz** 11:43 Thank you.
**Jason Plumb** 11:47 Okay, David, I saw that you put this in yesterday, and it's about the NTP issues, like aging out, 'cause these are really old, right?
**Cesar Munoz** 11:56 Yes.
**Jason Plumb** 11:57 Was there anything else you wanted to say about this? Because you reopened it, and I think that's great. I think if this is important to you and you reopen it, that's great. Like, no hesitation. Any of us who maintain this thing are free to do that.
Was there anything else to be said about this?
**DavidGrath** 12:13 No, not really. It just came to mind while I was looking at the source code, and I just wondered what went… what happened, and I checked it out.
**Jason Plumb** 12:22 Okay.
**Cesar Munoz** 12:26 Also, I wanted to… Yep.
I just wanted to add that by the time this issue was created.
Well, it was a long time ago, and since then, a couple of tools have being created.
by Google, that might help with this. So Now.
**Jason Plumb** 12:53 Oh.
**Cesar Munoz** 12:53 I know that this… this, So my, my… the thing is that so far, the times that we've talked about this issue.
It seems like it's not clear.
or it's not. There's doesn't seem to be a consensus.
On the importance of having this.
I think it's important.
because I mostly try to you know, Ensure that, and… Distributed tracing works well.
But I know that there's, there's an argument that for traces that are all within the device, then it's not that important.
So… so, I don't know, it's just that so far, it seems like there hasn't been, like, a… concrete. Yes, I think we need this.
General idea.
But if if that's the case, I think we can now take advantage of one of those tools.
that Google created. So it's easier than ever. That's what I wanted to say.
**Jason Plumb** 14:04 Yeah, Cesar, if you have resources, it'd be cool if you link them in that issue.
Just so that we can have them as talking points, because I don't know what those tools are.
So maybe, maybe adding them to this discussion here?
Now this was marked, and this was marked needs author feedback a long time ago, and that's kind of why it aged out.
I'm going to remove that since we're talking about it. And the author was.
That's me. Yeah. So I think, you know, this is really… I think what we would probably want to argue about is whether or not this is on by default. That's probably, like… I think no one… no one probably disagrees with the idea of NTP being available, but whether you opt into it on a device that's connected most of the time to some sort of cell phone network that has time baked into it.
I know, Jason's like, no!
**JM Jason Morris** 14:59 Don't try that. You can't get the network time on Android anyway.
**Jason Plumb** 15:05 I just mean that the operating system time is usually pretty good, because the phone is network-aware and sets its own time clock based on the network.
**JM Jason Morris** 15:14 But there's drift.
**Jason Plumb** 15:15 There's always.
**JM Jason Morris** 15:15 It sets its own time based on NTP most of the time.
**Jason Plumb** 15:20 There you go.
**JM Jason Morris** 15:21 That's what system clock.
Get network timers. It's the last ATP anchor adjusted.
The time zone, the time data from the cell phone network isn't actually trusted by the operating system most of the time.
because it's too unreliable.
**Jason Plumb** 15:41 Oh, interesting. Okay.
**JM Jason Morris** 15:42 Yeah.
**Jason Plumb** 15:44 So I think we should keep this open, and then I'm gonna mark it, thank you for that input. I think, I'm gonna mark it as… Help wanted?
Because no one's taken this on, and I would also call this an enhancement.
**Cesar Munoz** 16:02 By the way, I think Manuel, the tools that I'm talking about, I think both were mentioned by Manuel.
**Jason Plumb** 16:10 Oh, in this thread.
**Cesar Munoz** 16:11 Yeah, one is that… If you scroll down a little bit.
Whoa.
There.
**Jason Plumb** 16:20 -h.
**Cesar Munoz** 16:22 Yeah, those two.
Just 2 comments.
**Jason Plumb** 16:26 Okay.
This is what Jason was referring to. Okay.
**Hanson Ho** 16:30 So was the goal to provide an alternative time that is based on NTP or wholesale switch to it if it's available?
**Jason Plumb** 16:44 So, I think it would be for our.
**Cesar Munoz** 16:46 You wanted to say something?
You're on m.
**JM Jason Morris** 16:50 I was thinking, I read it as anchor against the NTP based time rather than whatever the wall clock says.
**Hanson Ho** 17:02 So, if it's not available, then do we use the ball clock, and does that create some difference in… so some devices will report one, some will report the other? Do we have to, like, put, like, a Boolean in there saying, hey, this is NTP time? It… just the inconsistency means that the data is gonna be a bit messy when you get it on the collector side, so either you have to be aware of it, or be okay with the inconsistency. So… It's a big caveat to be okay with inconsistency, especially if you're looking at outliers. So I think.
As an alternative, it's… it's good, but it's… it's… this is, you know, pretty big foot gun, potentially. You're like, oh, I use a more accurate time, it's mostly right, and… Define mostly, kind of thing.
**JM Jason Morris** 17:50 At the risk of making this very time centric, you could argue that the system and war clock is already a bit of a foot gun and is already not consistent enough.
So by introducing something that's more consistent, at least it'll, you know.
it can't make the situation worse, in theory. But you are absolutely right. If you're anchoring the time based on multiple different anchors and not reporting which one it comes from.
**Hanson Ho** 18:26 I think traditionally we just don't trust the wall clock. It's inconsistent. We know it's inconsistent with respect to each other, and there's no promise that it's anchored to anything that is common. So it's almost like it's going to be what the device reports. It's going to be anchored to itself. So within a trace, it's going to be consistent. But when you reach outside of it, we don't know.
And if we want to do it to NTP, we'll be like, oh, it's consistent if this were in use. And then we have to basically say, when is it consistent? When can we rely on it? And I think we need to, like, report that and say, hey, we're using NTP right now.
Then there's at least some indication that, oh yeah, this could be trustworthy. And if without that, you know, there, then, then, then, then it's, then we say it's, it's.
Don't trust it. So I think something like some indication of what.
What clock it's being anchored to might be useful.
If we're gonna do that.
**Cesar Munoz** 19:19 It's a challenging task, that's for sure.
So, and, and probably, if this ever gets implemented, then… Maybe, as Jason was mentioning, maybe it should be opting.
So… Yeah, I mean… I've seen some… I've seen value in that Because… even though the OS also uses NTP, to update its internal clock.
It's not as often as you might need it for telemetry stuff.
And… There's also ways… I mean, you could… Can I try this? Like… get a request for or request for the new for the time from the Ntp server once.
then… Compared the, like, the time drift at that moment.
With the current system clock.
then store that, And then use that cash.
until you get the new, I don't know, time drift, in case you have issues in the meantime with connectivity. I mean, there's… There's ways to… Oh.
You know, there's workarounds for these issues.
But it's… it's a lot of work, definitely.
**Jason Plumb** 20:48 Yeah, NTP is complicated, like handling time is, yeah.
**Cesar Munoz** 20:52 Yeah.
**Jason Plumb** 20:53 it's definitely difficult. I did want to ask the dumb, naive question that I think you've already answered part of, but that is why… why is Android or client-side stuff unique in this realm, and why don't servers talk about the same problem? Like, they're gonna also have Problems with tracing if their clock drifts and the clock will drift, but typically the operating system handles your time for you and you can safely, the assumption is that you can safely get the wall clock. And unless you're doing something really highly specifically time sensitive, like, I don't know, like high speed training or computing or something like.
Then you would usually just rely on the system clock, right?
**Cesar Munoz** 21:38 Yeah, I, I think it's, it's, it probably just boils down to how often Andre OS does it due to most likely… resource consumption, as with everything in Android.
So.
**Jason Plumb** 21:52 So sleep modes, clock throttling. Sorry, Jason, I keep talking and you keep trying to.
**JM Jason Morris** 21:58 No, no, I was just gonna say, do… I mean, if we're gonna go down the path of multiple anchors, do we potentially start talking about GNSS clocks as well?
which Android does expose to us on the server side. Things, you know, the data centers usually have.
an NTP server in them somewhere, or at least one, normally several, and those are, depending on the scale of the data center, anything from satellite connected to full-blown atomic clocks. So… It's just.
**Cesar Munoz** 22:36 Yeah, to care about battery.
**JM Jason Morris** 22:38 Yeah, exactly. They really don't have to care about. And your NTP servers also don't just set the clock.
Normally, to change it, they normally cause a local drift towards.
**Jason Plumb** 22:51 Yeah, it's all.
**JM Jason Morris** 22:52 It's like like really, really well done. So yeah, it's just less of a less of a concern.
**Jason Plumb** 22:59 Yeah, it's like drifting toward accuracy over some sort of timescale that is, I'm sure, spec'd in the protocol, and I don't understand.
**DavidGrath** 23:08 Good.
**Jason Plumb** 23:10 Okay, cool, I think… Go ahead.
**DavidGrath** 23:12 Yeah. I thought there was also a system clock API that was guaranteed to be monotonic even when considering sleep mode.
**Jason Plumb** 23:22 Is it this one?
**DavidGrath** 23:24 No, I think it was something elapsed time million or something like that.
**Jason Plumb** 23:27 Yeah, that's what our clock is using now. I think that was brought in… I think it was brought in in this PR.
But that was a while ago.
This thing, right?
**DavidGrath** 23:40 Yeah, that one, yeah.
**Jason Plumb** 23:43 Yeah, so our current clock implementation I think does use that.
Where is it?
**Cesar Munoz** 23:49 Yeah, it's just bear in mind that If I remember correctly, this… It's the time that has passed since boot.
So or something like that. So it's it's not. It's got nothing to do with real time. It's just the.
Processor time, I don't know.
To call it.
**Jason Plumb** 24:10 Yeah.
**JM Jason Morris** 24:10 The baseline there is calculated against wall clock. That's probably the bit that we'd alter to anchor to whichever is the highest precision clock we have reasonable access to.
**Cesar Munoz** 24:25 Yep.
**Jason Plumb** 24:26 Yep.
Does that help, David?
**DavidGrath** 24:32 Yes, it does.
**Jason Plumb** 24:34 Okay.
Let's move on to the next one. I think we've beaten that NTP Timehor To death and continue beating it.
Why is observers a synchronized list? I think because you can add them.
So… This thing… On the session manager, right, so the session manager… Has a mutable list of… mutable synchronized list, I think, is what that reads like, of observers that when the session changes, it will say, hey, session change.
So are you asking about, like, why it's synchronized? Okay, so synchronized is compulsory when entering, doesn't happen, and notify… Oh, good question.
**Cesar Munoz** 25:27 I don't remember, to be honest. Is our observers removable later?
**Jason Plumb** 25:34 I don't think so I don't know how to use computers. Let's see And also this GitHub interface like changes key bindings. Okay.
So the created here, you can add them here, and then we iterate on notify, so we iterate here.
And… I think… what maybe what David was suggesting is that this iteration is not necessarily atomic.
Like, you could still add or mutate while you're iterating, is that the concern?
**DavidGrath** 26:16 No, not so kind of. My concern with that is that the Javadoc says that, it is basically, what do you call that word, mandatory.
that you lock it with synchronized, or else the behavior is undefined, or something like that. Yeah. I just want you to write that it didn't happen.
**Jason Plumb** 26:34 Okay.
I think that's worthy of a… I think that's worthy of an issue. Go ahead, Cesar.
**Cesar Munoz** 26:42 I'm not sure I understand correctly, but it seems like Dave is suggesting that it's not necessary.
To make it synchronize, or… Is that the case, or…
**DavidGrath** 26:54 Bruno, I'm just wondering, like, are there any other aspects of synchronized lists that I might not be aware of that makes it such that… Not synchronizing isn't really an issue. Something like that, yeah. Like, do you get the full benefits without needing to worry about the undefined behavior, basically, yeah?
**Jason Plumb** 27:16 So if this were just a mutable list and you add observers from one thread and you iterate on a different thread, then you could see different versions of that list. So the synchronized is the intention, I think, from the original author, who might have been me, I don't remember.
There's been a lot of hands in here over time, but the idea being that you have this, like, thread barrier, this memory barrier, so that you can see the same version of the list in every thread. And that's what synchronized list… I think synchronized list, if I remember Java, it's like… It just puts the… I think it has the synchronized keyword on every single method.
And so then you just kind of get that memory barrier kind of for free. But that's, you know, it comes with caveats.
**JM Jason Morris** 28:04 I think the caveat that David's pointing out is the fact that the iterators are not synchronized. Yeah. So if… So you're outside of that memory barrier during the synchronization and the mod counts are still potentially being updated, so you can get concurrent modification exceptions in that.
**Jason Plumb** 28:26 I think this is worth fixing.
**JM Jason Morris** 28:28 I would just raise, in terms of listeners and observers, if you want thread safety, I personally prefer a copy-on-write array list, because you are guaranteed stability, and the… typical overheads of adding and removing observers. It's acceptable.
**Jason Plumb** 28:49 Totally. And the amount of observers added over the lifespan of a launch is like probably a handful, you know.
**Hanson Ho** 28:58 It's all done in the beginning, so the fact that it's a copy-on-write list is really to protect.
you know, the moments when we're doing it, which is gonna be rare, so we don't get an exception. That's… Making it synchronized seems a little bit heavy-handed, even if it does what it's supposed to do. It doesn't, so it's even less likely, or even less useful.
**Jason Plumb** 29:30 David, can I ask you to open an issue on this?
**DavidGrath** 29:35 Yes, sir.
**Jason Plumb** 29:37 Thank you. Yeah, I think we should fix that Good catch.
Actually, I want to ask, how did you catch it? Were you just noticed it?
**DavidGrath** 29:48 No, I just fumbled over the Javadoc for synchronized disk, because I wanted to see what it was about. Then I saw that… then I saw that clause about… the specified behavior. So I just got to make sure. Yes.
**Jason Plumb** 30:00 Okay.
That's cool.
Alright, on to the next thing. So… Cesar, you and I have been, like, two ships in the night, and we haven't been on the same call for a while. And now that Jamie's back, it's cool, we have all the maintainers here, and I want to talk about environment secrets.
This also will apply to Kotlin, for what it's worth. So… I don't have the Slack thread in front of me. There's… if, There's a thread on the Maintainer Slack and CNCF that is from Jack Berg that talks about this.
What environment secrets are is a relatively new GitHub feature. It allows you to have this thing called environments.
Over here.
And I don't know where this one came from, but I created this one, and I'm basically following Jack's, His, pattern that he established.
So, this one is called Protected. You can give it any name you want. I've followed his pattern. And then within that, you can say what branches are allowed to deploy to this environment, which That directionality is a little bit confusing for me, but stay with me. So this environment relates to these branches. So anything with main or release now has this environment available.
And then you can define secrets for that environment.
And those secrets are only available, well, we still have them defined across the project, like over wherever it is in here.
We still have them defined here. The idea is to get them out of there and only use environments. And so that limits the like where these secrets are available and decreases the footprint and decreases the possibility of them being exposed through some trickery or buggery. So Buggery in the American sense. Sorry.
That's all I want to say about that. This PR kind of is the last stage of getting that working for Android. I kind of had hoped to get this done before I did the patch yesterday, but it wouldn't have been relevant anyway. What this does then is for each of these steps where it's relevant, right? The build and the release, and I think Build also runs on PR, is that correct?
Do we have a separate workflow for PRs?
It would not run on PRs, that's entirely the point. These secrets should not be available to any random pull request branch, right? So, on the ones that need it, so when we're building and publishing and doing a release, that's when the environment comes into play, and that's when those secrets will be available.
So this was new to me, I've had this kind of on my side backlog for, like, 3 months, or 2 months or something.
And so it's finally happening. And once we get this in place, then I will delete the secrets out of the main… the main build. Any questions about this?
**Cesar Munoz** 33:09 I think it's, it It's, it's fine, as with a lot of GitHub, new stuff.
Like, I'm not fully familiar with it, but I don't know, it's not new, but… Not aware of it, so… I'll have a look.
I actually took a look.
Like, earlier today, I saw that, Copilot suggestion of Not adding this to the whole… Job.
But I don't know if it… if it applies.
Or not.
**Jason Plumb** 33:44 I hadn't seen this yet. I think I did this late in the day, so I will look at this. Yeah, this… Yeah, if you can apply at the step level, then I will dial that in as well. Yeah, this is probably a very good idea.
**Cesar Munoz** 34:00 Okay.
**Jason Plumb** 34:01 Okay, I'll take that.
**Cesar Munoz** 34:02 I'll take a look at the PR.
Later today.
Well, before.
Logging off.
**Jason Plumb** 34:10 Cool. Yeah, it's really just for publishing, right? And even on the build, normal build, it's like the snapshots.
**Cesar Munoz** 34:19 Nice.
Thank you.
**Jason Plumb** 34:21 Yes.
And then, more fun CICD stuff I wanted to call out, or just let people be aware of.
This thing… What's it called spotless? Yeah.
So David smartly caught this thing.
where the license was omitted from some files, and I was like, oh, that's weird, why would the license be omitted?
and in looking into it, it looks like, the spotless check… Is it spotless?
Or is it the other? It's the is it the other linter?
Anyway, it's this, yeah, it's spotless. So was not running as part of the build. So basically, most of the source code did not have the linter check applied to it.
And I'm not sure when that started diverging, but there were lots and lots like Dozens and dozens of files that did not pass linting. In fact, some that didn't even have the license header anymore, like… and we just didn't have that enforcement working, so… I could have submitted one PR that did all the linting and fixed the build in one go, and it would have been, like, 3,000 lines or something. So instead, I kind of started doing it module by module.
There are a couple of them left.
Unless they got merged, it looks like… This one is remaining, and this one is remaining. They've been approved.
So once those get merged, I will do this one, which should fix the build.
**Cesar Munoz** 36:05 Oh, nice catch. So maybe Kotlin, maybe Kotlin sources were ignored or something.
**Jason Plumb** 36:10 Yes, and it might go all the way back to, like, when we did the initial push out of Java toward Kotlin. We just never picked up the Kotlin linter or something, so that's my hunch.
**Cesar Munoz** 36:21 Probably, yeah.
**Jason Plumb** 36:22 Yes.
Anyway, I just wanted people to be aware of that. And thanks for sort of reviewing these incremental piecemeal stupid lending PRs.
Ugh.
All right.
Do we have Ben on the call? We do.
And Vishwan, welcome. I didn't see you join because it scrolled off my list. How are you?
**Vishwan aranha** 36:47 Oh, pretty good. How about you? I'm Vishwan. I work with Ben on the, in Grafana Mobile OL And we just had like one Android crash reporting question we wanted to bring to SIG. So we noticed that the OpenTelemetry Android currently catches the Java Kotlin and Kotlin exceptions, but native NDK crashes are like not covered yet. So the ticket that I added, it's tracked in that.
Umm.
For Grafana Mobile OLE, that leaves a gap for the Android apps that use native code because those crashes would not show up through the hotel path.
So, before we build anything which is Grafana-specific, we wanted to ask, like, is the, like, native SDK… NDK crash reporting something, the SIG would want upstream? Or, and if yes, like, what shape would you prefer?
**Jason Plumb** 37:38 So.
**Vishwan aranha** 37:39 I think they answered the.
**Jason Plumb** 37:40 I think the first thing is the definitive yes, we want this. The shape, I think, has not really been well defined yet, and I imagine vendors have their own thing currently.
**Vishwan aranha** 37:52 Yeah, thank you.
**Hanson Ho** 37:53 So, I have a second part of the, the Crash, SemCons, that, you know, I will eventually submit, that does define some shape to it.
Also, you know, the ASIC nature of it also has to be documented in that the reporting instance is not the actual crashing instance.
So there at least has some there has been some ideas about what what the Talmudgeon ought to look like. But, you know, more to to Jason, you know, doing it.
you know, in the open source layer, and have everybody having it would be useful. And if you're doing that now, you know, I can share with you, well.
if I can get that PR out again, you know, with the second part of it, then you can take a look at that and see if that fits, that… what you're looking for.
**Vishwan aranha** 38:45 They'll be prophetics.
**Cesar Munoz** 38:47 I will say first, thanks for bringing this up.
Yes, we need it.
I'm I'm Skeptical of the, speed at which… Same comp PRs tend to go.
So, I wouldn't wait for that to happen.
**Jason Plumb** 39:12 Agreed.
**Cesar Munoz** 39:13 Before… You know, yeah, so if you… if you… if you have the time to… contributed.
Even if it's not perfect, I think it's better than nothing.
**Vishwan aranha** 39:25 So, if we opened a PR, would you guys have time to review it soon?
We can, we can work on this.
**Cesar Munoz** 39:32 Yeah.
**Jason Plumb** 39:32 Yes, and if there's any way that you can make it incremental, like, please don't drop a 3,000-line PR on us. Yeah, definitely. I know it's tempting sometimes, but if you can kind of stage it, like, if there's a component that on start looks in the file system for crash files, like, that's a well-contained little bit, right?
And if there's another thing that does the writing or if there's, you know, something that exports or transforms, like doing those kind of stage them out to the best that you can, that'll be helpful.
**Vishwan aranha** 39:58 Sounds good. And I can add you guys to review, or, like, the whole team.
**Jason Plumb** 40:03 Yeah, we'll get tagged automatically when you submit.
**Vishwan aranha** 40:06 Sounds good, that'.
**Jason Plumb** 40:07 I mean, if you submit it against Android, yes, we'll all get tagged on it.
One thing of note, as well, is that we are moving… we're migrating toward having our own custom Android semantic conventions in this repo, through this kind of newer… Federation approach, and so… If and when the time comes, we want to make sure that these semantic conventions for whatever the telemetry looks like, even if it's an event or a log or whatever, that we have that spec'd in our semantic conventions locally.
and start building from that.
**Vishwan aranha** 40:41 Sounds good.
**Jason Plumb** 40:44 Well, anything on your end, Ben?
**Ben Joseph** 40:47 No, I think we should cover it all. Thank you.
**Jason Plumb** 40:50 Yeah, yeah, cool.
Cesar?
**Cesar Munoz** 40:55 No, then, well, no, just thank you. Yeah. For taking in on this.
**Vishwan aranha** 41:00 Thanks guys.
**Jason Plumb** 41:00 Yeah, we've been wanting that for a while. I mean, we've certainly talked about it. And I think Embrace.
**Hanson Ho** 41:07 Yep.
**Jason Plumb** 41:08 Do you have native crushes?
**Hanson Ho** 41:11 C++.
**Jason Plumb** 41:13 Yeah, it doesn'.
**Hanson Ho** 41:14 Thanks.
**Jason Plumb** 41:14 But…
**Cesar Munoz** 41:16 No, no, not right now.
**Jason Plumb** 41:19 Well, so the Elastic folks then are in a good position to sort of compare and contrast if there's any differences. I think that'll be awesome.
Sounds like we have good coverage.
**Cesar Munoz** 41:31 I mean, the elastic or they embra.
**Jason Plumb** 41:34 Embrace.
**Cesar Munoz** 41:35 Yeah, it's.
**Jason Plumb** 41:36 It's early.
And they both start with E's.
**Ben Joseph** 41:40 Okay.
**Jason Plumb** 41:49 Okay, I guess we've hit the end of the agenda. I just will also point out if anybody missed it, I got the patch out yesterday, so thanks for helping out with that, everyone.
I did the cherry pick PR, has that been merged?
this one.
So that's the same cherry pick. I'll just merge that now. Oh, no, now there's merge conflicts.
Okay, I'll figure that out.
Not on this call.
Cool.
We have a little more time if people want to go over some stuff or bring up any other topics of interest.
I feel like this was a pretty big agenda, and we got through it.
Oh, this is… I haven't reviewed this one yet, because it's still in draft, but this could be interesting.
I know that's a… it's a rum hot topic.
And we don't really… Yeah, I mean, Hanson, I know this is one of your favorite topics too. Like we don't really have like launch time or start time.
So If and when that lands, it'll be interesting.
Okay.
Well, I think we got there.
**Cesar Munoz** 43:21 Cool, thank you.
**Jason Plumb** 43:22 Jamie, we're gonna need baby pics. You know, it is a tax you have to pay being on the internet.
hahaha.
**Hanson Ho** 43:31 There's also a client, end user client SIG at nine o'clock. I'm going to bring up the topic of federated semantic conventions for end user clients. So we want a repo, but we need maintainer.
**Jason Plumb** 43:44 Is Tay gonna join us?
**Hanson Ho** 43:46 Because he's.
**Jason Plumb** 43:47 Talking about this.
**Hanson Ho** 43:48 I don't know, I didn't check Slack, so…
**Jason Plumb** 43:52 Hopefully. I mentioned it to him, like, a week or two ago, and I was like, yeah, we wanted Hopefully.
Alright, thanks everyone.
**Cesar Munoz** 44:02 Thank you.
**Jason Plumb** 44:02 The indexes?
**Cesar Munoz** 44:04 Yep.
**Jason Plumb** 44:04 Bye.
