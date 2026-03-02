SIG: Go Auto-Instrumentation SIG
Date: 2025-08-19
Duration: 23 minutes
============================================================

## Zoom Recording Transcript

**Tyler Yahn** 01:23 Hey, Ron.
**Ron Federman** 01:26 Hey, what's up?
**Tyler Yahn** 01:28 Not much. How you doing?
**Ron Federman** 01:32 Good, thanks.
**Tyler Yahn** 01:40 You have any, summer vacation you still have planned?
**Ron Federman** 01:45 No, I… like, I had my vacation on June.
It was, like, 3 weeks.
**Tyler Yahn** 01:54 Yeah, I thought Europe, you're supposed to take, like, 3 months off.
Yeah. No, that sounds pretty good. Did you go anywhere fun, or you just stay, in your home?
**Ron Federman** 02:05 I was in the US, like, mainly doing, yeah, hikings in, like, a few national parks.
**Tyler Yahn** 02:14 Where'd you go?
**Ron Federman** 02:17 In a few national parks, like, many Wyoming and, Utah.
**Tyler Yahn** 02:22 Did you go to the Tetons, or did you go to Wind Rivers?
**Ron Federman** 02:24 Yeah, detons and, … Yellowstone, and then Utah, Utah, there was, like, a bunch of them.
**Tyler Yahn** 02:33 Did you go to Zion, then, I'm guessing, in Utah?
**Ron Federman** 02:35 Yeah.
**Tyler Yahn** 02:36 Yeah, that's… I think, actually, Capital Re… Excuse me.
like, Capital Reef is, like, what, like…
less popular, but man, Zion is just, like, super dramatic, it's amazing.
**Ron Federman** 02:51 Yeah, yeah.
**Tyler Yahn** 02:53 Yeah, you didn't make it to the Grand Canyon then, huh?
**Ron Federman** 02:58 No, I was in the Grand Canyon, like, a lot of years ago, but….
**Tyler Yahn** 03:03 Yeah.
It's tough to go in the summer, like, it's just so popular. I guess Yellowstone's kind of the same, right? Like, it's just, like, the crowds are kind of incredible.
**Ron Federman** 03:11 Yeah, Yellowstone is insane, like, the amount of people, though.
**Tyler Yahn** 03:15 Yeah, yeah, it's… yeah, like a slow day, you're only in traffic for, like, you know, 20 minutes or something, but yeah, it's ridiculous, but yeah.
Well, cool, we could probably get started here. I don't have too much, I see… yeah, hey, there's Raphael, I think he was gonna be a little late, so, we could jump in here. I know, Mike messaged me, or Mike messaged the group, he's not gonna make it, and then, …
Nicola's out on vacation at this point, so, yeah, …
I don't have too much on the agenda as well, so I kind of wanted to wait for Raphael just to… just to include everyone.
**Rafael Roquetto** 03:52 Sorry.
Typing together wrong. I was about to say this, Splunk, I'm going crazy.
Alright.
There he goes. Sorry. ….
**Tyler Yahn** 04:07 Cool. Alright, so I wanted to check in on our milestone. I've been working a lot in the, hotel space, but first I just wanted to point out, Raphael, you opened this PR, appreciate it. It's the claim format PR.
I took a look at it, looks good to me. Looks like it's doing a lot of great formatting, things that, you know, are putting into some sort of standard.
I wanted to call it out just to make sure that everyone sees it. I'd like to get some eyes on it, just to make sure. Like, obviously, as Raphael, you had mentioned, …
You know, a lot of this stuff is, …
up to us, so if you have really strong opinions at this point as to, like, you know, some of these configurations, now's a good time to speak. We could always change it in the future as well, but yeah, I think that this is, …
really helpful. So, yeah, just… if you have time, check it out.
Rafael, anything else you wanted to say about this one?
**Rafael Roquetto** 05:00 Yeah, so… one thing that I did, if you'll see there, I formatted everything, including vendor, like, dependencies, like Libbf. The reason I did that, and we do that in OBI, is just because it's… it's just easier to have everything, you know, and you don't have to worry about
Having a class of files that you want to formatted in a way, and another class of files that you want untouched.
So, this is the rationale behind it. It just becomes, like, solid for everyone. You format it once, and then you just keep up. Those files, at least on Obi, are…
Hardly, if ever, updated. But, I mean, I can see why people might not want to do that, so it's not a problem if you don't want to do it, for instance, the vendor, like, lead BPF dependency thing, like, this is just a matter of changing this PR. It's just… I just brought it like this as a starting point for a discussion.
But, that's, you know, it goes either way.
**Tyler Yahn** 05:58 Yeah, I didn't… I don't have strong opinions. I'm fine formatting the files, but… I mean, we're copying them here, we can do whatever we want, is how I see it, but, I'm also fine if people are like, let's leave them the way they are. That sounds good, too.
**Rafael Roquetto** 06:12 it's just less cognitive burden after the first PR. In my opinion, it's easier to maintain. But, again, no strong opinions. Just thought I would mention that. The other thing…
… I will mention is…
we might wanna, in addition to Clank format, to have Clank Tidy, which is a linter. This will pick up things like, you know, missed parameters, or unused parameters, things like that.
But that should be in a different PR, if we do that. So, food for thought. I can help with that as well.
If we decide to do it.
**Tyler Yahn** 06:51 I'd be very interested in that as well. I think this is really helpful just from, like.
trying to get things in a consistent format, but, like, I'm all about, some sort of linters, if we can get them set up. They're usually very helpful, especially, like, if we wanted to, like.
start instituting policies on how we write code. I really dislike having, like, English prose defining policies. I, like… obviously, it happens, like, it's going to happen, but, like, it's nicer to have automation tell you, like, this is the way that we try to do things here, yeah.
**Rafael Roquetto** 07:20 Yeah, I agree. …
the thing with Linktidy is that it's mostly designed with C++ in mind, so the C support is there, we use it. I think it's way better than nothing, and it brings a lot of value.
But, for instance.
it will still miss something. Like, I don't know how you guys… how you guys are familiar with this, but, like, the cost correctness
support inclement tidy is C++ only, so it won't nag you and see that you forgot to call some variable, things like that. So we will still be missing. I looked into other linters that exist.
for C, but they are… they are more work to do, and they are not, like, supported out of the box by GitHub runners and things like that. So, my recommendation, if you want something quick and dirty, Clank Tidy would do the job and at least catch
lot of things. It's better than nothing, that's what I'm saying, for, bang for your buck.
Yeah, I think it's a good starting point, at least.
**Tyler Yahn** 08:25 It's configurable, right? Like, we can tell it to ignore things?
**Rafael Roquetto** 08:28 It's configurable, yes, it's configurable.
**Tyler Yahn** 08:32 Yeah, I think that that sounds… Fine, then that sounds great.
**Rafael Roquetto** 08:36 Yeah, okay. I will… I'll try to work on that.
ASAP. It's been busy with half of the team in vacation, but … after this period, I'll jump into that.
**Tyler Yahn** 08:50 Ron, any thoughts here?
**Ron Federman** 08:54 It looks great. I just wanted to ask about the pre-commate hooks, like, I'm not very familiar with it, I just wanted to hear your thoughts about the… like, how common is it to have, like, this kind of stuff in it?
We commit hook.
**Rafael Roquetto** 09:10 … Honestly, I cannot answer for, like, hotel perks and old projects. When I used to work on QT,
This was common, like, for QT1 requirements, you had a pre-commit book for something else, not for formatting.
It would add some sort of ID to your, GitHub, commit message, so it could be matched and Garrett and things like that.
I use it a lot, just because then I don't have to worry about hitting CI and CI complaining that I forgot to format my files, but it's entirely optional. If you don't.
do this, pre-commit hook. Like, if you don't do make, make, install hooks, that's why it's an optional target. You don't have to do that. The worst that can happen is that once you raise a PR, you… you might, you know, if you forgot to run clean format.
By running make length format, the…
CI is gonna tell you if there's something wrong with your format. It's just a convenience.
**Tyler Yahn** 10:16 Yeah, I'm, personally not a fan, just because it takes over, and I sometimes have issues, but I… like, the way you set it up, where, like you said, like, it's just, like, an optional thing.
That's kind of why I was like, yeah, that sounds great.
**Rafael Roquetto** 10:30 If you want, we can, like, if you think this is more harm than good, we can remove it altogether. It's not a big deal. It's, …
or renamed… I mean, I don't… I don't have any…
Strong opinions either way, so it's up to you guys.
**Tyler Yahn** 10:44 I won't be using it, but I… I definitely am not opposed to adding it here. Like, I think it… like, a lot of people do, like you said, use it in their workflow, so having something for developers here seems reasonable.
**Rafael Roquetto** 10:56 Maybe I can rename it to Install Clings for MacBooks, just to make it more specific, so… I don't know.
**Tyler Yahn** 11:03 I… I imagine there's gonna be one for the tidy as well, so…
like, I might just want to leave it as install hooks.
Or you could also, you know, give a very specific install Clang Tidy hooks, and then have it as a dependency of make hook, or the install hooks target as well, but… Okay.
I… yeah.
Ron, are you planning to install this?
**Ron Federman** 11:27 I'm not sure about the pre-commit hook stuff, but, …
But if it's optional, like, I don't see why not.
I think so.
**Tyler Yahn** 11:39 Yeah, okay. That's my… yeah, I'm with you on that.
**Rafael Roquetto** 11:42 You don't have to decide on the spot, so whatever is best.
**Tyler Yahn** 11:47 Yeah, if they are installed, I do know you can run, like, a… like, a no verify option. Whenever you run, like, a git commit option, it'll also skip the hooks, but, …
Yeah, that's… that's if you install them. That's… I… I… yeah.
I'll just leave it at that, I guess.
But yeah, regardless, I'm happy about the rest of the changes, so… yeah.
…
I just noticed this. This is tied to a specific version of Clang format? Is there any way….
**Rafael Roquetto** 12:23 Yeah.
**Tyler Yahn** 12:24 Tie this to… have, … Renovate, update it?
**Rafael Roquetto** 12:31 That's a good question. I need to look into this again. So, last time I looked into it, which was a few months ago, because this bothers me as well.
**Tyler Yahn** 12:39 Basically, the behavior between Clank Format 18, 19, and 20.
**Rafael Roquetto** 12:44 have changed. … and there was… I couldn't find a configuration option.
to kind of override it. It seemed to be, like, a bug on playing format or something like that when I looked. I will… I will look into it again.
to see if there is, anything we can do. For instance, if you look at the history of this PR, like, I… the first commit I pushed.
I failed, and, and the claim… I mean, at least it validated the,
the claim from a checks complaint, even though I have the pre, like, the commit installed and I formatted it, and that's because on my machine, I used a claim 20, and claim from a 20. So…
And it has to do with, like, there's a… it had to do with some space.
I first pushed. Sorry. …
some space in a bracket, something like these. I couldn't… last time I checked in… I checked these, I couldn't find…
a way to kind of enforce that, so that's why I settled on ClinkFirm 19, which is the most recent available on the Ubuntu runners.
And at least it's an explicit version of baseline, okay, use that version.
If you want to. But I will double-check. I see where you're coming from.
**Tyler Yahn** 13:59 So this is actually maybe a good point that, …
Yeah, I have no idea what version of clang format is on my system right now, but …
I imagine if there's going to be very big differences across, like, installations, then we may want to just run this in a Dockerized environment.
And if we run it in a Dockerized environment, then we can have Renovate manage the format.
… just using the dependencies docker file? Do you know what I'm saying?
**Rafael Roquetto** 14:31 No, but I can look into it.
**Tyler Yahn** 14:34 Yeah, so what we do for, like, CodeSpell and Markdownlint is we have this file exist.
And, Renovate can update these, no problem.
So if there is a Docker file that contains the right Clang format, installation.
we can… we can do it there. Otherwise, we could also just…
build our own, as well. That could also be something we could do. But, …
So, so what you do here is you take that, and then you go into the, Markdown file, and so for, let's see…
things like, CodeSpell, what you can do then is you can say, like, okay, …
there's a Docker Py thing, and essentially it says, like, run the Docker utility, with the Python script, essentially, and so what that does is it looks into the Python image by just using awk on that dependencies docker file to get the version that you need. So Renovate handles the updates there, but then here in the makefile, it actually just uses the, …
you know, just some sort of, like, scraping to find out what version of the Dockerfile to run. And then it will run whatever commands you wanted in a Dockerized environment. Obviously, there's, like, some…
you need to be careful of, you know, setting the correct user, setting the repository up as, like, the working directory and that kind of stuff, but, like, that's just abstracted. In fact, it's all pretty much here, so you should be able to just copy this.
Okay. But yeah, I mean, so we could look into that, because then we can make sure that every development environment is going to use the same version of Clang.
format.
it's going to add the overhead of Docker running, … For these format operations, so…
You may want to keep, …
like, a Clang format target, but also maybe also have, like, a Clang, Docker format, or a Docker Clang format target, on top of that. So if somebody wanted to use the system one and, like.
maintain and make sure that it's installed to be the correct version. This is… this will likely be faster. I… I mean…
I don't know if it's, you know, 10 times faster, but, like, it'll be faster, so you might want to have both, targets, is what I would say there.
**Rafael Roquetto** 16:44 Right. What I would do… if you'll agree.
is… first, I'll try to see if I can solve this by only enforcing using the .clang format, file. I'm going to repeat that again, meaning that maybe our clink format file is too… too loose, and if I add a little bit more options there, it will… it will…
not produce different results in different Clank versions, and then it doesn't matter. I'll revisit that, because I think, in my opinion, that would be the best option, then we don't have to involve Docker or any of that. If not, I'll fall back to the solution that you're saying in
And, ….
**Tyler Yahn** 17:19 Okay.
**Rafael Roquetto** 17:20 We do that.
**Tyler Yahn** 17:22 Yeah, that sounds… that sounds good to me.
**Rafael Roquetto** 17:24 Okay.
**Tyler Yahn** 17:25 Yeah, yeah. I'd like consistency, that'd be helpful, just to, like, prevent developers being like, what?
I ran the tools locally, and it gave me one thing, and then I shipped the PR, and it's saying it's failing, because, like, that's definitely really annoying, is when you get these sort of failures, and you're like, … why?
**Rafael Roquetto** 17:43 Yeah.
**Tyler Yahn** 17:44 yeah, I can't reproduce it, which, yeah, happens way too often in a lot of other tooling, so, yeah. But otherwise, yeah, I think that's maybe the only feedback, yeah.
**Rafael Roquetto** 17:53 Okay, I will… I will have a look, because we also have the same problem in Albi anyway, so…
Two birds, one stone.
**Tyler Yahn** 18:01 Yeah, right? Perfect.
Okay. Well, cool. Then, I think with that, we can take a look at the next milestone. I don't think there's been too much progress here. I, have been looking at this, …
I don't know where the issue went. Oh, I think we probably moved it to the other, …
Oh, no, we did it, it's right here. Sorry. So I have been looking at this issue. I have, started working on a prototype, it's just kind of slipping. I'm trying to get the, upstream release out, so that's been more my priority.
I do think that it'd be nice to have that out before we made our release, so I was trying to prioritize that, but I have been taking a look at this. I've been looking at what Nikola did, and porting it over. It's, …
not straightforward, but it's not too complex. So, yeah, still just working on this. No update other than that.
… I see, obviously, this has got a PR… Associated with it, … Is this going to…
need to have the tidy before we resolve this, or do you think that just having the format, should resolve this, Raphael?
**Rafael Roquetto** 19:16 … I… up to you, to be honest. I mean, formatting resolves that, pretty much. The title would be a linker.
So… I don't know if you want to… That's fine.
**Tyler Yahn** 19:30 Sounds… sounds good to me. I think….
**Rafael Roquetto** 19:32 Yeah, okay.
**Tyler Yahn** 19:34 I don't know why that's not finding it, but…
And then… let's add this to the milestone.
Cool.
Alright.
Okay, and then, Ron, this is the only other option, for fixing the other, arch stubs. Is this still something you're looking at, or…?
I'm guessing also.
**Ron Federman** 19:59 Yeah, I just, didn't get to it yet.
**Tyler Yahn** 20:03 Okay.
Yeah, no worries.
That's, …
Sounds like, my excuse as well, so… still working on it, but yeah. Okay, cool. Well then, it sounds like we have, in track, I think that the… I'm trying to get this upstream release out this week.
There's, …
A little bit of vacations, that are causing, people to be slow on their responses, so I'm trying to get things done upstream, but hopefully we'll get that out. Ideally, then, we can do some updates here to update our dependencies on, like, a tagged version instead of just a commit hash would be really ideal before we get this out, otherwise…
I think a lot of other folks are gonna be a little annoyed at certain of the things there, but…
It's not the end of the world, since things are breaking, so… Okay, cool.
With that, that's the end of the agenda that I had. Any other topics y'all wanted to talk about?
**Rafael Roquetto** 21:01 I'm… I'm good.
**Tyler Yahn** 21:03 Yeah.
Okay.
Well, cool. Any, cool… Fun, experiments you guys are playing with?
I got a lot of fun things that I'm doing, but they're all hotel, related, so…
We're trying to do, like, self-instrumentation, for a lot of the, …
the pipelines, so for, like, the processors and the exporters in OTEL. And so, obviously, that's gonna be helpful for here as well as in Obi, just getting more, metrics from internal systems as to, like, what's going on.
it's all gonna be experimental right now, but … yeah, it's… it's a whole thing. There's a lot of hurdles there as well, so a lot of reviews, codes. But yeah, so I'm guessing it's gonna be, like, a month or so before we really see that.
kind of turn out. I guess, actually, in the next release, there should be some, so we could even start playing with it then, but…
Yeah, I guess that's, yeah, something to look forward to.
**Rafael Roquetto** 22:02 I'm working on… on a new network tracer for Obi, so I have this…
If you look at the OBPR, this is working to not review, because it's a messy
PR, but basically, it… it's a whole new implementation that's…
brings a lot of filtering that we do from, like, network flows. They generate a lot of events, a lot of events, and we start seeing some things, some interesting things on our profiler.
And then I thought that I can do a lot of it in eBPF rather than doing user space, and hopefully, yeah, it would be better. But, to be continued.
**Tyler Yahn** 22:46 Yeah, whet your appetite, yeah.
Well, cool. If that's the case, we can end the meeting early.
Thanks, guys, for joining, really appreciate it. I will, see you all probably tomorrow morning, but if not, next week, yeah.
**Rafael Roquetto** 23:02 Alright, have a good one.
**Tyler Yahn** 23:04 Bye.
