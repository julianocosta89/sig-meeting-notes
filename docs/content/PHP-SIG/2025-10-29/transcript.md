SIG: PHP SIG
Date: 2025-10-29
Duration: 21 minutes
============================================================

## Zoom Recording Transcript

**Chris Lightfoot-Wild** 01:45 Hello?
**Pawel Filipczak** 01:49 Hey, guys.
**Chris Lightfoot-Wild** 01:51 I very nearly get caught out by the time zone, or clocks adjusting.
**Pawel Filipczak** 01:57 Yeah.
Next week, it will go back to normal, hmm?
**Chris Lightfoot-Wild** 02:04 Yeah. Are you guys a week… a week behind us, Bob, with the Switch?
**Bob Strecansky** 02:10 Yes.
**Chris Lightfoot-Wild** 02:13 Nice.
**Bob Strecansky** 02:18 is… Yeah, ours switches this weekend.
**Sergey** 02:40 Are there any voices in any states that, want to cancel that daylight service? Like, is it…
**Bob Strecansky** 02:46 Oh, yeah.
**Sergey** 02:47 Any boy in it?
**Bob Strecansky** 02:49 I think Daylight Savings Time is one of those, like.
It has been politicized for no reason whatsoever.
**Sergey** 02:58 Oh, really? Instead, it's even… even that, is kind of suck?
The… the opinion on that is split according, like, party lines?
**Bob Strecansky** 03:06 Yeah, kind of. It's kind of silly to me. I think there's… I think there are some states that don't follow. I think it's Arizona. Like, there's one or two that just, like, now we're out.
But, very complicated.
**Sergey** 03:20 Right, right. I know that California, they have a split, between… like, they have multiple daylight Was it in Canada? I remember somewhere in North America, I was kind of, like, suddenly noticed that there was a change in time zone in the middle, either of the state or a province in Canada.
Don't remember exactly, yeah.
**Bob Strecansky** 03:39 Wouldn't surprise me.
Agenda, huh?
request. Request.
**Sergey** 04:37 When you show on the graph, my immediate thought is, oh, it's going well. Is there any way to bet on it? To earn money on that graph?
**Bob Strecansky** 04:44 What's that? There's that website now that you can, like, pretty much bet on anything? Is it, like, Poly something… Polymarket?
**Sergey** 04:52 Yeah, I don't think there will, there will be any takers on the bet on that. You need… you need somebody on the other side, right?
**Bob Strecansky** 04:58 Well, that's true, and I feel like those numbers could be artificially inflated relatively easily if you could bet on it, right? Like, you could just install that package over and over and over again on a bunch of machines, and… And then you would… then you'd win your bet.
Alright, I think we can get rockin'.
Does anybody else have open agenda items besides me? I want to talk through the… renovate… the renovate addition and depend upon subtraction, but I'm happy to talk through other things if other people have them.
**Chris Lightfoot-Wild** 05:33 Good for me.
**Pawel Filipczak** 05:36 We have an announcement that… E.php was accepted as a contribution.
So, we will start work on that.
But I guess you know that.
I'm gonna…
**Bob Strecansky** 05:48 Yep, that's true, that's good news.
**Chris Lightfoot-Wild** 05:51 I know that, so that's amazing. Congrats. Thank you.
**Pawel Filipczak** 05:57 I have forgotten to share the issue. I'm working on, I mean, this coordinator process. I will send the link to you, Chris, right now. I just forgotten about that.
That's time.
**Chris Lightfoot-Wild** 06:10 Oh, thank you, no worries.
**Pawel Filipczak** 06:12 Damn.
**Chris Lightfoot-Wild** 06:13 I've forgotten as well, so that makes two of us.
**Bob Strecansky** 06:19 The, so, for those uninitiated, Renovate is a… I didn't know this until last week. Renovate is, like, another… like, another Dependabot that is apparently a lot… a lot more dependable than Dependabot.
And so, I had the, someone from the TC Add it to our 3 repos, and right now we got both running.
I have a plan this week to, like, review some of those changes and… try and true it up a little bit, and then I will probably remove Dependabot from our repos after that's completed. I just want to have them both run for a little bit and make sure they're, like.
Either catching the same thing, or Renovate is doing better.
The general consensus seems to be that Renovate is better, but I think that it's important for us to watch it from our spec… our spec perspective, rather than just taking it for face value.
And so, I'm planning on working on that this week, but… That's the update that I have on that. Does anybody have any questions or comments about that?
**Sergey** 07:22 Is there any way related to the… what we discussed last week, the CVE.
**Bob Strecansky** 07:28 Yeah, yeah.
**Sergey** 07:28 it's using. Yeah.
**Bob Strecansky** 07:29 Yeah, so when… so I asked in the maintainer's channel, like, hey, who's having… who's… who's had this problem before where Dependabot isn't working, like, isn't tagging some… isn't tagging, like, specific GitHaws with… the new… the versions of third-party packages, and they were like, oh yeah, we switched to Renovate. Oh yeah, we switched to Renovate. I was like, oh, okay, like, let's check it out and see if that works out well for us, so… That's how we go.
**Sergey** 07:54 have some way to solve that problem, like, they will still keep up to date. Well, they're gonna be keeping some kind of, like, manually reviewed database of stuff that is not compromised, and… They will only suggest that.
**Bob Strecansky** 08:07 I think it's more along the lines of when they pin… when a version gets pinned, they actually do, like, pin it to a specific GitHaw, which Dependabot seems to do sometimes, but not all the time.
I think that's… that's more along the lines.
**Sergey** 08:22 So they're consistent about that.
**Bob Strecansky** 08:24 Yeah. Supposedly, that's why I haven't had a chance to review all… like, I saw… so that runs daily at 8 AM Eastern Time, and I saw a bunch of PRs come in with that, but I haven't had a chance to review them yet, so… Like, let's take a look, so… Where are you?
Is it too sure that there was a bunch?
Yeah, here, so there's, renovate has some… Actions here, and so does depend about… these look like they are.
Relatively sim… well, yeah. Upload artifact is a little different, but we'll… I'm planning on doing a little bit more fine-tooth comb review of these later this, like, within this week, but…
**Sergey** 09:10 just from the first look, it looks like the names that Renovate gives are a little bit more cryptic, like, it uses… Shazam in the name.
**Bob Strecansky** 09:18 Yeah, it does, which is… And it looks like it does a good job of actually tagging these versions, even though this doesn't seem to… again, well, I'm… I haven't really had a chance to look through it 100%, but that's…
**Sergey** 09:30 That's on my… Looks like the same version with a different shop.
**Bob Strecansky** 09:34 Yeah, that's right, that's right. So, anyway…
**Sergey** 09:38 It seems like it's replaced just the shy and kept the version.
**Bob Strecansky** 09:41 So, yeah, this is one of the ones that we were taking a look at last week, and it's like, I think Dependabot added this.
**Sergey** 09:48 Hmm.
**Bob Strecansky** 09:48 But this is not right.
And I think, Renovate is adding.
this… And not changing this. Like, this is just wrong in general, so I… we may have to do some, like, manual.
**Sergey** 10:02 No, you're saying they can work together to screw the whole thing up.
And copyright on that.
**Bob Strecansky** 10:08 Well, no, I'm not saying that, I'm saying I think, like, I think Dependabot was the last update for this. This updated incorrectly, and I think Renovate Blindly updated this, assumed that this didn't need to change.
And I'm not sure why, so that's why we… I gotta… I have to learn a little bit more this week, because I'm not that well educated on this yet.
**Sergey** 10:32 Yeah.
Makes sense. I don't know how useful it is to know for us to know the exact versions, like, human-readable versions of those, I…
**Bob Strecansky** 10:39 Actions, maybe, it's not even that important.
I think… I think it's one of those things, like, it's not important until it's really important. It's like… if I want to know, like, you can… I can always just, like, go into that… I can go into this… I can copy this, and go to this… this GitHub action, search for this SHA, and find out what version it is, but that's just annoying.
And, like, when you're trying to troubleshoot something that can… could, like, cause confusion or waste people's cycles, so… I would like to make sure that it's okay, but…
**Sergey** 11:10 I guess having both will definitely probably be most useful. I wonder… Is it possible to configure these robots in any way? Like, can you configure them per repo?
**Bob Strecansky** 11:21 Again, I'm not sure. I haven't really had a chance to look at them yet, but I'm assuming that they have some sort of configurable options, and I'm assuming we eventually will want to choose one and stick with it, and I'm going to assume that will be Renovate, but we'll see.
**Sergey** 11:37 Interesting.
**Bob Strecansky** 11:39 Let's look at the pull request. Looks like Brett's working on declarative config.
It looks like Nivea is commenting on those, which is good.
And then it looks like we don't have anything else, really, recently. I'm surprised a bunch of these didn't get closed.
with the stale bot, but I'm sure we'll… I'm sure they will eventually… It looks like these are just, bumps.
Whoa, whoa.
**Chris Lightfoot-Wild** 12:10 I did actually push changes on that second one, that's in the PR list now, and re-requested Brett to do it, but if you've got any time as well, Bob, you're included.
**Bob Strecansky** 12:21 You talking about this one?
**Chris Lightfoot-Wild** 12:22 Okay.
Yeah.
**Bob Strecansky** 12:24 Okay.
**Chris Lightfoot-Wild** 12:25 There's conversation with, with… from Nive, that can't rely on the composer binary being present.
But then I thought, I wonder if… checking the arguments that are passed into the command, and just checking the first one, if it matches the binary.
That might… so I've added that in. It might get battered away, but…
**Bob Strecansky** 12:47 So there's a potential way to work with it.
I will… I will review that, too, because now you got… you have sparked my interest.
**Chris Lightfoot-Wild** 12:57 Thank you.
**Sergey** 12:57 Yeah, it caused a crash when it was accused in the context of, Is it possible that, that this FAR has… some of the OpenTelemetry stuff in it.
**Chris Lightfoot-Wild** 13:13 Composer bundles PSR3, but version 2.
So if you just happen to use, like, a different incompatible monologue, etc, then it blows up. And the composer repo has a bunch of issues and discussions where people are kind of saying, hey, what the hell?
It's just kind of like a… I guess a known side effect, if you're familiar with Composer, which I only run into it when I hit a runtime error.
So it's probably quite common that people get tripped up by this.
**Sergey** 13:46 I wonder, like, it a little bit ties in, sorry for hijacking the discussion, is it okay if I just add a couple of sentences?
So, we were discussing, Pavel and me, because we want to do exactly this to solve this kind of problem, and we saw a tool that already does it, and it seems that a lot of these FARs, they use this kind of tool. It's called BHP Scopper.
It's on packages, and it essentially shadows your… any namespace that you use, kind of like third party, like, direct dependency, and then your transitive dependencies. So when you're building this kind of tool, like Composer, that has a risk of something else will be loaded in its context, well, I guess… I mean, it depends who will blink first in this case, right? Because we can say that a hotel is also this kind of tool, that it's being loaded in a known context, so it should protect itself from interacting with the context, so it should have shaded any of its dependencies, so they will not clash.
With any dependencies. But essentially, there is a tool that will prefix all the namespaces with a predefined thing.
And then, it essentially exists. Now, I'm still investigating it, I don't know if it might have such side effects and cause some… because obviously, just syntactically, and prefixing all the namespace and all the files.
It sounds like it should be okay, but who knows, maybe there are some files generated on the fly, but still with the old namespace, whoever… like, HP is unfortunately a thing that can, you know, can do all kinds of tricks, PHP applications or libraries, that this tool automatically will not solve.
But I'm just wondering, we're gonna do it for Edutton.
Now that EDOT will be contributed, at least that part will also be contributed, but I wonder, maybe we should do it out of the box for the SDK itself.
But I don't know if we want to, because, like, for normal use, right, the problem here is that for normal use, when we just have application that takes dependency on the SDK, then obviously all the dependency will be resolved, And it will not happen in the console application, this clash of any kind of third party, like PSR or whatever. But when you load this tool into something that was not taking dependency, right, direct on SDK, then this clash can happen, right?
So, I was wondering, maybe we can protect it by just, assuming It had independency for this, but I don't know. I guess it's, here we need to be careful. Maybe in some cases we should just rely on developers solving those issues, and… But just, I'm just throwing in the air, like, to let you know that we are working on solving it for Edith, and like I said, it will be contributed as well, but when we reply it, now we only consider it to reply it in this context of Which we're mostly concentrating on for DevOps, right? When we just load an agent site-wise. It's not… you don't need for each application to take dependency on a tail.
on OpenTelemetry, but, maybe… We're thinking maybe we want to, you know, extend this use case.
This will solve this problem, right?
It will still be able to load in even the context of Composer, but it will not clash with anything that Composer uses.
**Chris Lightfoot-Wild** 16:53 would that be, like, so, in the SDK, we use PSR3 logs, so would you have to fork… essentially fork that, and does this package…
**Sergey** 17:01 No, we will download, so essentially what this thing does, this, if you can open packages, PScoper, the tool called.
So it's essentially… it's they seem to claim that different tools already use it. So essentially, you download your vendor folder, and then you run this tool, it goes and prefixes all your vendor folder with some, let's say, you can prefix it.
But something like Shadow Bay Chris, right? Now, all the tools that you use, even the transistor dependencies, they will exist in different namespace, they will not clash. Now, if you load this piece of code in the context of Composer.
you will have two different copies of PSR log. One that you use, and it will be in the namespace shaded by Chris PSR log, and the copy that Composer uses will be regular PSR log, so it will not clutch.
Obviously, in your code that you write manually, you will probably need to reference a shaded by Crispy SR log, right? You'll need to be aware that you're using. But whatever they use between themselves, whatever you have in vendor folder, that will be automatically synchronized. All the code will be using these shaded namespaces.
**Chris Lightfoot-Wild** 18:04 Okay.
Interesting. Now, in some cases, you want to.
**Sergey** 18:09 to build a bridge, right? Like, you can say, okay, fine, but what if some application uses OTL directly, and they produce spawns directly, right? We might want also to consume those funds, so that's a more advanced use case, but if you just want to completely separate the dependencies, you can just do this by this shader.
Hopefully, like, again, it obviously depends on if those libraries don't do any kind of, like, trickery at runtime that is more advanced, like, generate files on the fly.
**Chris Lightfoot-Wild** 18:37 Yeah, I'd be interested in… certainly for me, but I don't know if… Bob, you might welcome that as well, but is it, like, if you could post a link to the issue, maybe, on the Slack channel, and…
**Sergey** 18:46 Yeah, trouble, though.
**Chris Lightfoot-Wild** 18:46 We've got some more eyeballs to, track it, I guess?
It sounds like an interesting thing that.
**Sergey** 18:52 I mean, this issue still exists in our repo, maybe in the future, like, because we mostly concentrate, like I said, on the case when… Our agent, EDOT, hopefully in the future it will be hotel agent, you just loaded site-wise, right? So you don't… so you don't even have ability for the applications to resolve these dependencies clashes, because you don't require application to even mention in its composer the dependency on Autel.
But, so yeah.
But, yeah, I will send you, no problem.
**Chris Lightfoot-Wild** 19:20 Thank you.
**Sergey** 19:26 No, that's it for me. Thank you.
**Bob Strecansky** 19:30 Right, Contrib, just has some chores for me.
Same with instrumentation, it seems.
Backlog… Nobody has anything else in the backlog… Road to V2 looks pretty ready.
Looks like… there's some… Bugs that were opened, those probably need some investigation.
Camel case… Just in a snake case.
You bet.
It's our namespaces…
**Chris Lightfoot-Wild** 20:16 I did actually have a look at that one, but I didn't know if there was going to be something Brett might have, Come out of the shadows for. It looks like the Weaver config has just got their own namespace, but… if I was to run the command, it pulls in a bunch of extra stuff, and there's other changes as well, so I don't know if… I don't know how Brett typically runs this tool.
Well.
**Bob Strecansky** 20:40 Do you think maybe you could ask about that in this issue? Because I'm curious about that, too.
**Chris Lightfoot-Wild** 20:44 Yeah, yeah, I could do that. I mean, in the short term, we could just manually fix, you know, the generate files, and then next time we run this on the new SEMCOM It should be fixed by the, tweak to the Weaver config.
So I could… I could certainly follow up on that.
**Bob Strecansky** 21:00 Thank you, Chris.
Looks like that's all the open issues that are relevant.
Alright, I think that's… I think that's it. Does anybody have anything else they want to talk about?
I'm good.
**Chris Lightfoot-Wild** 21:20 I think so.
**Bob Strecansky** 21:21 What's going on, man?
**Chris Lightfoot-Wild** 21:22 Cheers.
River.
