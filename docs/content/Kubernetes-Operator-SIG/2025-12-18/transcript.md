SIG: Kubernetes Operator SIG
Date: 2025-12-18
Duration: 20 minutes
Zoom Recording URL: https://zoom.us/rec/share/UdPNTDw1Q_-pMrNkEorTKouP8k4sH6ZFA8ETmgy_6YP00_6HxmBz6EdV7OhQCfI.azb2VACuafuVFLT3
============================================================

## Zoom Recording Transcript

**jea** 01:18 Hey.
I don't know how… I don't know if we have anything… Today, too much.
It's, like, end of year, and… I don't know, I don't know who else is gonna join, basically.
**Mikołaj Świątek** 01:33 That's some pull requests.
That…
**jea** 01:36 Yes.
**Mikołaj Świątek** 01:37 I have approved, they're not very interesting at this point, I just want someone else to approve them.
**jea** 01:44 I can do that. Is it the scrape Classes one?
**Mikołaj Świątek** 01:47 The scrap classes one is on the more complex side, but at this point, it's been changed to… to use any config.
So, it's kind of just fine. And there's an end-to-end test showing that it works, and so on, so I'm, like, perfectly fine with it. There's also one where it's, like, host PID, and I've also.
**jea** 02:13 Oh, that one? Oh my god.
**Mikołaj Świątek** 02:15 That one's also fine.
Yeah. Opinion, as you wait.
**jea** 02:19 Yeah, the Screen Plus one, I'm reading through it right now, looks fine to me.
I'm just gonna approve it and merge it.
**Mikołaj Świątek** 02:30 Because that's what's been waiting for a while, so I don't know how… It is, yeah. I'm just gonna…
**jea** 02:35 I'll approve and merge, like, right now.
And so…
**Mikołaj Świątek** 02:39 The host PID one might need, like, a rebase because of the release, because it modifies the… The release manifest?
But… Other than that, nothing very interesting happens in it.
**jea** 02:58 Should I wait for Benny to read this, or should I just merge it?
**Mikołaj Świątek** 03:02 I want it. But if he's not here today, then I would just go.
**jea** 03:06 I'm merging it. He's… he's lost his chance.
**PL Pavol Loffay** 03:12 Basic, so it will not properly… gets to.
**Mikołaj Świątek** 03:17 Well, you know, rough, you know, rough, rough.
**jea** 03:20 Yeah, too bad.
**Mikołaj Świątek** 03:20 This is a fast-paced, laissez-faire environment. If you don't show up.
**jea** 03:27 The.
**Mikołaj Świątek** 03:28 You don't care about…
**jea** 03:31 What was the other PR that you wanted me to look at?
**Mikołaj Świątek** 03:35 The one… the hostbed one, yeah. That one, I actually kind of want Benet to have an opinion on, because he originally had some.
**jea** 03:44 Oh, okay.
**Mikołaj Świątek** 03:45 reservation about this, but honestly, honestly, I… that PR does not do anything.
anything, like, that you can't just do in Kubernetes directly, if you want to. It doesn't do anything other than just adding a field that is directly then proxied to the, to the pod template, so…
**jea** 04:08 This would also be a good one to discuss. Someone was like, hey, we can get rid of that container unknown unknown problem.
We're probably.
**Mikołaj Świątek** 04:16 Do you understand how this works? I understand. Well, I understand basically how this works. Well, so you understand, like, Providence and, like, SBOMs, right?
**jea** 04:26 Yeah.
**Mikołaj Świątek** 04:27 I know what an S bond is, and I know what the word provenance means, yes. That is… that is the limit. That is where my knowledge ends.
**jea** 04:36 Essentially, what this guy found is that because we aren't doing the necessary pre-work for that… for the SBOMs and Providence to exist on the container.
and we're not disabling it explicitly, then it shows up as unknown unknown, because that's just, like, the default for when you don't have the proper setup for provenance. And so what he's saying is that, oh, we can fix this problem by just disabling provenance. And I'm like, well, yes, but, like.
why don't we actually figure out how to do provenance correctly, which is a thing that OTEL is, like, asking us to do anyway.
So… I think I would rather see the reverse than… Continuing.
I also think that he is… Kind of just, like, doing some AI-generated responses.
Because this format is too AI-like.
I don't love the idea of us being like, yeah, oh, security isn't working? Oh, let's get rid of security. Like, I would rather fix security, I think.
**Mikołaj Świątek** 05:41 Well, you know, you know, this is the… it sounds like the large language models have, like, inherited the instincts of junior developers, all… you know, from the start of time, like, if there's a test failing and you don't know what's going on, you just remove the test and everything's green, right?
Easy.
**jea** 06:05 Yeah.
So, close that.
What else do we have on here?
I can't stay too long, I have to drop to other calls and things, unfortunately.
**Mikołaj Świątek** 06:16 There's a PR adding final… making… re-scoping the finalizer.
**jea** 06:21 Oh, yeah, right.
**Mikołaj Świątek** 06:23 Which I think is fine, but I would like at least one other person to look at it.
**jea** 06:30 Yeah, Paul, do you…
**Mikołaj Świątek** 06:31 I'm taking a look at that.
**jea** 06:32 I think that it, touches some of the stuff you added in last year.
It's a pretty.
**PL Pavol Loffay** 06:38 I can take a look.
**jea** 06:40 I'm putting it in the agenda here.
**Mikołaj Świątek** 06:42 Yeah, at this point, at this point, the only change it makes is that it only adds the finalizer if you're creating any, any, like, cluster roles.
As part of reconciliation, or rather, if, like.
**jea** 06:54 That's easier. Like, I…
**Mikołaj Świątek** 06:59 I reviewed it and basically, basically asked for this to be… to be the only logical change in there.
Yeah. I also wouldn't mind if we finished early, early today, because I spent my whole day fixing… fixing build errors in Elastic Agent before, like, a feature freeze.
Not funny. So, I'm a little bit wrung out. I'm a little bit wrung out. I swear, if I see another, like, linker error on macOS, I'm just gonna… I'm gonna go change profession. Something else.
I have a new pizza oven, making.
**jea** 07:52 That's.
**Mikołaj Świątek** 07:52 So relaxing, yeah.
**jea** 07:55 Yeah, working with those is a very relaxing thing.
**Mikołaj Świątek** 08:00 I mean, if you do it, like, 10 hours in a day, it's probably less relaxing, but for me.
After… after a day of typing, it is very relaxing.
I know, by the way, Pavel, I promised to open an issue about the upgrades. I still haven't done it yet, because I'm gonna do it. I'm gonna do it before Christmas.
**jea** 08:26 Jesus.
**Mikołaj Świątek** 08:26 Because I'm… I am… as of… as of today, I am… I am, like, done with my, urgent stuff.
And I'm gonna have some.
**PL Pavol Loffay** 08:37 Are you mean for the instrumentation, P1, Beta 1?
**Mikołaj Świątek** 08:40 Yeah, it's fine.
Yeah?
**PL Pavol Loffay** 08:44 I started looking into it, and I created a CR based on the JSON schema.
I'm not sure I like that structure, to be honest.
It's… it's way more complicated to what we have. I'm not saying it's bad. Maybe it's not bad, because if people are kind of comfortable with the schema already, it's gonna be a good thing, but… It's not an easy one, I would say.
**Mikołaj Świątek** 09:17 I actually have a problem, maybe you guys can advise me.
So the problem is, I wanna… there's actually… I have a draft pull request, which actually passes. It passes all the tests, and it's fine.
In this respect. Right now, I might think it might also have, like, some conflict in Go mods and stuff, but that's whatever. Basically, I'm updating Prometheus from Prometheus operator.
to, like, the newest version. You can see I put it in Zoom chat.
And I'm doing a bunch of stuff.
in there.
Because Prometheus did a bunch of stuff.
**jea** 09:57 Aren't they always?
**Mikołaj Świątek** 09:59 One of the biggest… so, whatever, the test I can update, I… there's even now… there's even now a way to disable sharding in a more reasonable way, so… so we can get rid of putting, like, the shard equals zero on… on… on collector containers, and so on.
But there's one problem with this. So this passes tests just fine, and everything works, as far as I can see. There's only one problem with it. Prometheus changed their internal label representation.
**jea** 10:33 Oh my, why would they do that?
**Mikołaj Świątek** 10:35 I mean, okay, so they have 3 different ones, and it's based on a build tag, okay?
The problem is, are, like, performance-optimized, like, relabeling, for example.
Kind of implicitly relied on the label just being a slice, and the label structure just being the slice.
And now it's not a slice, now it's, like, a single string. And there is no, like, public API, to do what we've currently been doing, and I've tried, like, 5 different things, and none of them have, like, have recovered the performance that we used to have.
Like, some of them are, like… plus 30% CPU usage on non-relabeled, for example. And I'm wondering… Like, basically, I wanna… I wanna try some… a few more things. It's probably still gonna reduce the performance, even if we, like, build tag ourselves into the old structure.
Hmm… but… I don't know, like, I was wondering what you think. Like, is it worth keeping back this whole upgrade of several versions for this? Like, how important are performance regressions for us?
in this.
**jea** 11:50 I think, I would rather us update so that we don't continue to fall behind. Are we able to do this without a breaking change, or is this, like, de facto a breaking change?
**Mikołaj Świątek** 12:00 It's not a breaking change at all.
**jea** 12:02 Oh, it isn't? Oh, it sounded like it was.
**Mikołaj Świątek** 12:04 No, no, it's not a breaking change. Like, there's some… it's not even a lot of, like, if you look at the PR, there's not even, like, a lot of code changes, honestly.
And some of them are actually simplifications. The problem is, like… the problem is just the performance.
Like, we are… Action.
**jea** 12:25 I think it's okay. I think we can accept the performance hit.
If it becomes, like, A massive problem.
We can re-optimize if we need to.
**Mikołaj Świątek** 12:37 I'll try a little bit over the holidays as well. This has waited for, like, 3 months, it can wait for, like, 3 more weeks.
**jea** 12:44 Yeah.
**Mikołaj Świątek** 12:45 And I'll try to get… I'll try to get the best… the best that we can, like, with this, structure. And… and then… I don't know, probably we'll just have to kind of… Do the, like, bite the bullet and implement the relabeling inside.
Complete full target relabeling inside the target allocator, and that's gonna improve performance a lot.
Overall?
It's just gonna be, like, a pretty big change.
But, like, the stuff that we're doing right now is really just kind of convoluted. For example, we calculate, target hashes differently, whether we're relabeling or not, because if we're relabeling, then we have to calculate it on the relabeled.
Labels, but we still have to expose the original labels.
To… to the actual collector, so they have to keep both of these, and doing that in a way that doesn't literally just double the memory consumption is a source… a significant source of, like, the complexity that causes the performance regressions wherever you change something.
**jea** 13:57 Yeah.
I'll need to see some code.
to…
**Mikołaj Świątek** 14:04 We could do that.
**jea** 14:05 Understand what you're saying.
**Mikołaj Świątek** 14:15 But we don't have to do it now, if you're in a hurry. I can… Yeah, I just have to…
**jea** 14:21 some other stuff to do, and it doesn't sound like it's a massive… we don't need… it's, like, not a rush to…
**Mikołaj Świątek** 14:26 No, it's not a rush, but, like, the longer we delay, the potentially bigger mess.
**jea** 14:31 The worst it'll get, yeah.
**Mikołaj Świątek** 14:32 Un… to unwind, yeah.
**jea** 14:35 Yeah.
We can… I think, yeah, if you want to take a look over the holidays, that'd be great, and then I'll review it after the fact.
**Mikołaj Świątek** 14:44 Oh, oh, oh, there's one thing I want to talk about. We have a PR… It says, addagents.md.
**jea** 14:53 It's from Eastwire.
**Mikołaj Świątek** 14:54 Yes. And I read this PR, and my immediate reaction to it was.
this is useful documentation for humans. Why is it called AgentMD? I read it, and it was very useful to me. Like, it's like somebody doesn't know the project at all, they just look at this file, and it's like a very kind of, it's kind of very… terse.
But it's very information-dense, and it kind of tells you all sorts of, like, things that are really useful to know when you don't know.
**jea** 15:25 Yeah.
**Mikołaj Świątek** 15:25 So it makes sense. So… I think.
**jea** 15:31 I think the big thing is that it just… it turns out that, good documentation is good for everybody.
**Mikołaj Świątek** 15:38 Agents included.
I'd like you guys to check out that PR and tell them.
**jea** 15:44 I think it looks great.
**Mikołaj Świątek** 15:46 Yeah, but I like the file, I like the documentation, I just don't know if it should be called AgentsMD, or maybe it should just, like.
**jea** 15:55 Agentsmd is, like, a conventional thing. So, it's, like, if you have… if you're running, like, Claude Code, or Claude… or, sorry, if you're running Cloud Code, or, like, Cursor, or something, it'll, like, default, like, load that into its memory.
And then it'll be like, oh, I already know how to use this codebase, or whatever.
**Mikołaj Świątek** 16:15 I know, but…
**PL Pavol Loffay** 16:15 Yeah.
**Mikołaj Świątek** 16:16 about is that, like, whether it should be, like.
like, whether there should be, like, an architecture.nd file, and then agentsnd is just a link to that. That's kind of what I was wondering. Because if it's agentsnd, then people are not going to read it, and I think it's useful to people, too, not just my agent, not just agents. That's, like, my, like…
**PL Pavol Loffay** 16:34 I think we should just… the agent's ID should probably just point to the contributing MD.
And it's duplication, like, the purpose of the agent MD is to tell the AI agent, like, how to execute the test, where are the packages, what is in the packages, which is essentially a contributing document.
So I think what we should do is to test, How to, kind of, cross-link these documents, and if the agent will properly Consider the links in the doc.
**jea** 17:08 I think as long as you do just a soft link, it works.
Because that's what he's doing already.
**PL Pavol Loffay** 17:17 It's better.
**jea** 17:17 Claude, clod.md file.
**PL Pavol Loffay** 17:21 So, I mean, maybe I just wonder if you are fine with adding the cloud MDNA just into the repo?
And then we can figure out, like, what is the… what is the most… what is the best way to, kind of, maintain these files, because we have edited in different repositories, and it can become quickly unmaintained.
**Mikołaj Świątek** 17:46 Mmm… I am very, very fine with just updating ContributingMD with the stuff that's in the AgentsMD as far as proposing, and then, like you said, linking AgentsMD to Contributing MD. Like, I am… I'm very… I'd be very happy.
**PL Pavol Loffay** 18:09 Yeah, I liked it the most.
**Mikołaj Świątek** 18:11 I, I am, I, I am definitely not against putting, like, you know… instructions for AI agents and the thing. Like, we already have… I've already committed some code written by Cloud to the operator repository. It was, like, a bunch of unit tests, but… You know?
**PL Pavol Loffay** 18:35 D… the PRI emerge today, the removal of the KubeRB proxy.
**Mikołaj Świątek** 18:43 That's all prompted.
**jea** 18:46 Oh, yeah, I'm really excited about that, Pavel. That's… that's gonna be a great change.
**Mikołaj Świątek** 18:52 I also, like, I also, over the past, like, 2 or 3 months, merged a bunch of PRs that were just basically consolidating end-to-end tests, and that's also… that was also an AI agent.
Which I basically told it, you know, look for all these tests and find ways to kind of find common patterns and move them out into step templates. And that worked quite nicely.
So, I am not… I am not against coding assistance.
Alright, do we have… do we have anything else?
**jea** 19:37 That sounds like it's it. I don't think we should meet in 2 weeks, which is New Year's Day.
That's maybe my only comment.
**Mikołaj Świątek** 19:48 Okay, well, let's… how do we… how do we cancel? Who has the power?
**jea** 19:52 We just, you just, we just say we're not showing up to this. I'm messaging in the channel right now.
**Mikołaj Świątek** 19:58 Okay.
**jea** 20:17 Okay, all good.
Have a good holiday, everybody. See you.
**Mikołaj Świątek** 20:21 Next year.
See you.
**jea** 20:23 Yeah, bye.
**PL Pavol Loffay** 20:25 See you, bye.
