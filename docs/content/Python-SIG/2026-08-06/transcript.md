SIG: Python SIG
Date: 2026-08-06
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Diego Hurtado 00:02:07 Hello, buddy.
Emídio Neto 00:02:12 Sweet.
Aaron Abbott 00:03:13 Hello everyone, how's it going?
Emídio Neto 00:03:20 B.
Aaron Abbott 00:03:29 Hey, so I think Tammy's not gonna join today, so, grab the next one.
Yeah, please add your name.
names to the attendees, if you get a chance, and I guess we'll just start with the triage.
Alright, I'll do my best since Tammy's not here, but feel free to jump in.
I guess we'll just go through this no status column here.
Okay.
Oh.
Are these the ones that are already in the agenda, some of these?
Did you say something?
Diego Hurtado 00:04:42 Sorry.
No worries.
Sir, are we doing triage, or should I… should I…
Aaron Abbott 00:04:53 Yeah, yeah, yeah, exactly, exactly. So yeah, I was… I was just asking if you already added it to the agenda, we could just, Got about it in a minute. Okay.
Diego Hurtado 00:05:02 I don't… yeah, I think so, 5… yeah, that's, 5-3… 81… No, that's, 548… 5… no, I don't think I added it.
Aaron Abbott 00:05:21 Okay. Well, I think we'll just, like, Looks like it's ready for review, probably.
Great.
Diego Hurtado 00:05:29 Yeah, it's totally ready for review.
Aaron Abbott 00:05:33 Okay.
Cool.
Diego Hurtado 00:05:35 This is, oh, sorry.
No, no, yeah, go ahead.
Aaron Abbott 00:05:39 Oh, I was just gonna go on to the next one, if that's okay.
Diego Hurtado 00:05:42 Yeah, that's… that's fine.
Aaron Abbott 00:05:44 Okay, cool.
This one's got no reviews yet. This is Python, correct instrument, name validation error message, there's a bug.
Yeah, party for review, I think.
Next one.
Fixed Photo Core, this one's got an issue.
Cool.
Beautiful. I'm gonna put it in easy to review.
It's two lines.
These are… these are the helpful AI PRs, so… This one is, Dylan's. I think maybe let's add this to the topics, I think.
It's pretty uncontentious, we've already discussed it a couple times, but… Okay, cool.
I'll market… Pretty cool.
This is the same thing. Put it ready for review.
Okay.
Cool. This one's from Lukas Removes Dependence on Incubating attribute, and it's a pretty short one. I think I'll do easy to review.
async PG, report Unix socket connections.
Alright, this one doesn't have a bug, some config.
Liudmila Molkova 00:07:25 Marinique!
Aaron Abbott 00:07:29 Lilmila, were you saying something?
Liudmila Molkova 00:07:33 Oh, sorry, I didn't realize I'm unmuted, sorry.
Aaron Abbott 00:07:36 Oh, no worries, you're good, you're good.
Anybody can interrupt me, though, because I don't want to just run on here, so… I don't have a lot of context on this one, does anybody…
Leighton 00:07:46 No, Aaron, you're doing great.
Aaron Abbott 00:07:48 It sounds like there's a bug here, Yeah, seems pretty straightforward. Let me ask if there's an issue.
Cool. Yeah, we should probably… I think Ricardo's back next week, so we can talk about the… automatic stuff that… does exactly what I just did. And maybe we have time for one more.
I'm gonna leave that one in that column, so this will be the last one.
Discord Pi, add prefix, and app command tracing.
I think this is… I saw somebody said something in Slack, but this is a new package altogether, right?
So…
Emídio Neto 00:08:40 Yeah.
I believe we can discuss this in the agenda, because… I'm not sure if… like, the materials of this library, they are not open to instrument the library with the OpenTelemetry native code.
And that's why they are creating the instrumentation here, but…
Aaron Abbott 00:09:01 Yep.
Okay, I… I'm volunteering you, Emidio to talk about this one, but I added it to the agenda.
Emídio Neto 00:09:10 It comes up.
Aaron Abbott 00:09:11 Okay, and we'll leave it in that column. Okay, awesome.
Let's… let's timebox it there, and go on to the topics.
Cool.
So, Diego, over to you.
Diego Hurtado 00:09:27 Right, sorry for hoarding the… Entire. Cool.
It's just something that happened, many topics, Alright, I'll try to be quick. This one, I'm just asking for, Another review, I think this is, I think this… actually great.
Because… not only because of the problem it solves, but because it introduces a mechanism that can help us In the future, deal with the problem of dependencies, which is, By removing, a particular dependency and replacing it with, I don't know, like, a Rust implementation or something like that. So, getting eyes into… into this… It's, definitely gonna help us Have a… A mechanism that is very powerful and can help us solve one of our major problems, which has always been the fact that There can be… Collisions… between ourselves and the application that is being instrumented, because of how Python handles dependencies.
Aaron Abbott 00:10:48 Okay, so I think this one, I kinda… I don't think Lucas is here today, right?
No.
Yeah, I would like to chat with Lukas some more and figure out what he wants to do, because I kind of reached out to… I'm not sure how to say his name correctly… Ivo or Evo on Slack, and… I was hoping that maybe, like, most of this implementation could live in a repo outside of Python, because most of it is just the protocol published in the OTEP that he wrote.
But I don't want to block this PR, so I'm kind of… Leaving it up to Lukas to decide what he wants to do here.
But yeah, I think… given… given the context here, it seems like we're gonna need a native package anyway, so I think I'm okay with this.
I don't know, Leighton, if you have any thoughts.
Leighton 00:11:40 Yeah, I haven't taken a look at it yet, I'll take a look today.
Diego Hurtado 00:11:45 Thank you, thank you very much. Oh, Lukas, there you are.
Lukas Hering 00:11:47 Yeah, sorry, I joined late. what was the, I'm also fine, we can move this to the contrib repo, and maybe it doesn't also belong in the main repo.
Was something else that I wanted to bring up.
Aaron Abbott 00:12:05 Well, I was just saying, like, I know I kind of… I hope I didn't stretch this out too much, but I brought up the possibility of putting this in a separate repo, because most of it's not Python-specific, and I was just saying, I'm kind of leaving it up to you, Lucas, like, whatever you want to do, I think we could always refactor it later, and yeah, I'm okay with this… with this Rust thing, I think.
We're gonna need it anyway, like you mentioned here, so…
Lukas Hering 00:12:34 Got it, yeah. Yeah, if anyone has any strong opinions, like, we could even pull in the C++ Code that they use.
Instead of, like, writing our own… implementation, but…
Aaron Abbott 00:12:55 Yeah.
Diego Hurtado 00:12:56 Yeah, I'm okay with this, living here, sorry, yeah, that's already proofed.
Aaron Abbott 00:13:01 Okay.
Do we have… like, Lukas, do you know what you want to do? You want to put it here, or contribib, or… you know, discuss more with the… with Evo or Ivo, however you say it.
Lukas Hering 00:13:17 I'd say we're not in a rush.
I think it was, like… I tried using it with the eBPF profiler, and it… I think they only recently added support, so… It's still pretty new, so… we can… I think we can… I want to hear more… more thoughts, probably.
Aaron Abbott 00:13:41 Okay, so maybe… Yeah, it sounds like the discussion's still going here. Maybe I'll just write in the notes what you said, like, Yes.
Sorry, I'm not even sharing the notes.
And you said you, you… you were able to test it with the profiler?
Lukas Hering 00:14:21 I… it's a little hard to test on Mac, but, Yeah, I wasn't actually… I think that there's still… it's still not fully supported. Maybe… it might have changed, but, Yeah, I would like to also verify it, like, end-to-end before we merge it in, probably.
Aaron Abbott 00:14:51 Okay, cool. Any other thoughts on this one? Should we go on?
Okay, cool.
Dio, you got the next one again.
Diego Hurtado 00:15:11 Right, that's quick, please just, Reopened that PR, If you're sharing, yeah, thank you. I forgot to update it for a while, and the bot closed it, but I still want to… Yeah, thank you.
Aaron Abbott 00:15:32 does not.
Diego Hurtado 00:15:32 Oh, yeah, I… yeah, I tried reopening it myself, and I force-pushed to it, so maybe if it's not… if it's not gonna work out, I'll just create a new PR, that's fine.
Aaron Abbott 00:15:45 AI, I don't really know.
How to… how to get…
Diego Hurtado 00:15:47 Probably it's not.
Yeah, don't worry, don't waste time on this, I'll just create a new period.
Aaron Abbott 00:15:54 Okay. Cool. Did you want to… did you want to talk about it at all, or maybe another… No, no.
Diego Hurtado 00:16:00 No, it's, it's something I'm still working on, But, when it's ready, I'll let you know.
Aaron Abbott 00:16:10 Okay.
Cool.
Here's the next one. Is this topic again,
Diego Hurtado 00:16:17 Oh, yeah, that one.
Aaron Abbott 00:16:20 Yeah, Dia, are you okay?
Diego Hurtado 00:16:21 So…
Aaron Abbott 00:16:21 If we wait for, Ricardo to come back next week, or do you want to discuss still?
Diego Hurtado 00:16:28 No, actually, if Ricardo's gonna be next week, then that's fine, because that was actually a whole point of, Not discussing this, last week.
Aaron Abbott 00:16:43 Okay.
Okay, sounds good. Let's, right down here… Okay Well, thank you. Sorry, sorry we haven't made progress on that one. Just hard with the vacations and everything.
Cool.
Diego Hurtado 00:17:06 Right.
Aaron Abbott 00:17:07 Next one.
Diego Hurtado 00:17:08 Yeah, that one. So… I wanted to give, all of you a little bit more context on this one. So, we're using packaging as a dependency of open telemetry instrumentation.
And that's, causing issues, for us in the packaging slash instrumentation projects, right? For the same reasons of, Protob and so on, right? So… Actually, this PR is a little bit large, in the sense that it contains quite a bit of code, but it's logically pretty simple to understand.
The features of packaging that we are using are just, the features of a couple of, PEPs that, define how diversions of… packages are compared with each other. So, for example, it defines if, 0.6, 0.0, 0. Dev.
Or 1.3.5, which one is bigger, if a range of version contains another version, and so on, right? There's a little bit of, detail there, because we need to… consider some prefixes and suffixes and stuff like that. So it's pretty… straightforward, in the sense that it's just implementing that same logic here, so that we can remove this dependency. So, it's pretty harmless in the sense that it has actually nothing to do with OpenTelemetry itself. It's something that we just use for… the bootstrap, When we compare, when we check the versions that are installed in the In the application environment, so that we can make sure if we use, If the versions that we use If the instrumentation support, match, right, so… That's pretty much the only thing this PR is doing.
Aaron Abbott 00:19:24 Yep, gotcha.
So, so one question, I see the issue here, and you mentioned the, injector.
Could you say, like, was there specific issues or things people ran into, or is this… like, could you just share a little more context on the background?
Diego Hurtado 00:19:43 Oh yeah, it's pretty much the exact same thing that happens with any other dependency that we have.
That it can crash, collide, right, with another dependency that lives in the application.
Michele Mancioppi (Dash0 Inc.) 00:19:57 If you want, I can put a little more color on this one.
There are, for example, in case in point was MLflow.
an older version of MLflow, which, in the installation script runs, pip install.
And the injection brought along a version of the packaging package in Python that was incompatible with the version that MLflow wanted.
And, that is… that is what broke.
Aaron Abbott 00:20:31 Okay.
I guess… we don't need to, like… I don't wanna… belabor it too much, but, like, the logical conclusion of this is we don't want any dependencies in the instrumentations. Is… is that kind of, like, the direction?
Diego Hurtado 00:20:51 That's ideal, yeah. We're also, many times, using just a few features of, big dependencies.
In… in our code. So, it's, most of the time, it's pretty feasible.
Just to implement a small part.
That covers the features that we use and need.
on the… on… Get rid of that problem, forever, right?
Aaron Abbott 00:21:21 Yep.
So Diego, I guess… I guess I'll stop there, I've been talking a lot. Does anybody else have thoughts on this one so far?
Leighton 00:21:35 I feel like I'm all for keeping the instrumentations kind of bare-bone, but… we're essentially, like, taking the burden of, like, maintenance of, like, these utilities now. Not saying that's a… It's… Worse or better, but… like, are we okay with setting that precedence, I guess?
Diego Hurtado 00:21:59 Yeah, I get your point, it is definitely, Something to consider when we follow this approach.
for this particular scenario, I am very… not worried, because this is an algorithm that was defined a time ago in these steps.
And, I don't expect any logic to change there, right? Into how we compare versions, right? So, I think that's… Pretty stable, and, it'll be quite rare that we need to, Make any changes in… In this logic.
Oh, sorry, Lukas Alberts.
Lukas Hering 00:22:43 Yeah, I know we've brought this up before, but would it be, like, less… maintenance or maintainer burden to just vendor this into the… yeah, vendor it directly in, I feel like that would be pretty easy, right? In this case.
Aaron Abbott 00:23:04 Yeah, I was gonna raise that, because in terms of, like, review, it'd be… it'd honestly be easier to just be, like, rubber-stamping a rendered copy, I think, and… I don't think there's great tooling in Java… sorry, in Python compared to Java for this, where there's, like, the shadow… shadow plugin.
I mean, somebody get me honest, I don't know of such a thing, but… I think even if it was, like, a one-off case like this one, which is pure Python and pretty small, I think it would be easier Like, on the maintainers and every… everybody, if it was just a vendor to copy.
Diego Hurtado 00:23:41 Right, could be… I'm not sure if, I mean, when you mean vendor, you mean… just… Creating a package… That, That it has the exact same content.
With a different name, right? That's what you mean, right? Just to make sure that we understand.
Lukas Hering 00:24:09 I think we would just copy it directly into the… instrumentation package.
Michele Mancioppi (Dash0 Inc.) 00:24:14 There is a catch. A lot of the stuff that shadowing does in Java is avoiding, global symbols to clash.
And this is something that copying over the file with the rename of the package name is not gonna do.
Aaron Abbott 00:24:32 Yeah, you…
Diego Hurtado 00:24:33 Another problem with… Sorry, yeah, the other problem with the vending is that if the… Package… imports… If the vendor package has an import that references It's… itself, it's gonna end up importing the… The installed package, right? Because.
Aaron Abbott 00:24:57 Right, and listen.
Diego Hurtado 00:24:58 Turn into that.
Aaron Abbott 00:25:00 You have to update the imports, right? Like, I believe when Java does this, you put a prefix in the package name, and I think we'd have to do something similar here, right?
Diego Hurtado 00:25:08 Yeah, but you will need to edit the code of the vendor package to make sure that Imports are safe.
Aaron Abbott 00:25:19 can you give an example? I don't know if I got it. Like, If it uses relative imports versus absolute imports, like, that kind of stuff.
Diego Hurtado 00:25:29 Exactly, right? So, for example, let's say you have a, a package named, I don't know, Google, right? Like, Google's package, right? So, and you want to vendor it, and then you create underscore Google, But then, if… The code inside of… the underscore Google package says, from Google Import, blah blah blah.
it's gonna import the non-vendored Google package, right? So you will need to change those imports inside of the vendor package to prefix them with the underscore.
Aaron Abbott 00:26:05 Yeah, that's what I meant by the… I don't know of a tool that has, that's as good as the Java Shadow plugin to… that automatically does this kind of renaming. I know, like… I know there's some general-purpose tools, and we can dig around, but I think that would probably still be preferable to… like, I… like, I'm assuming most of this code was probably, like, you know.
White Clawed or something, based on the site.
Diego Hurtado 00:26:30 Oh, no, that's… That's actually pretty much copy and pasted from the… Because the… the packaging is pure Python as well, so…
Aaron Abbott 00:26:40 Okay, I mean, I'm… Then we need, like, notices for you.
Sorry, go ahead, Lucy.
Diego Hurtado 00:26:48 Sorry, Lukas?
Lukas Hering 00:26:50 Oh, I was just saying, like, I mean, if you're already copying it, we're just saying, like, maybe just do it in a more maintainable way, so, like, if there is updates, you don't have to go manually copy it again, right?
Diego Hurtado 00:27:07 Right, but do you suggest publishing a package of ours?
Lukas Hering 00:27:13 I mean, there's multiple ways you can do it, but I think typically you just have, like, a, like, underscore vendor subpackage within this package, so it's not published independently.
And then you would just… Copy directly all the files into that, like, underscore vendor slash packaging.
So… Subdirectory, and then… You just need to make sure… yeah, you'd have to do the import rewrites, which should be pretty easy, because packaging itself doesn't have any other dependencies.
And then, yeah, and then we'd have to update the callers.
Potentially any other callers to always use the vendored import.
Diego Hurtado 00:28:01 Alright.
Lukas Hering 00:28:02 I think, like, I mean, like, one example of this is, like, Ray.
the ML… they vendor a lot of stuff, so maybe, like, we can see what their strategy is and, like, look at… how to do this properly. I think, yeah, I think the general disconcern is that if we're already copying this, we're basically just doing a manual vendor, so we might as well… Kind of formalize it and automate it so that when the packaging package does bump, we just… Need to rerun a script or something.
Diego Hurtado 00:28:35 Yeah, that's… That's, sounds even better, so if you want to leave a comment in the PR, I'll appreciate that very much, and I'll look into that.
Aaron Abbott 00:28:51 Leighton, were you gonna say something?
Oh, you put your head down?
Leighton 00:28:56 I think you could… Yeah, Lukas covered what I was gonna say.
Aaron Abbott 00:29:00 Yeah, yeah, and I was gonna say pretty much the same thing, so, I just did, like, a quick book around, and I found there's… there's this tool that is supposed to do it, but we could check what Ray does, and then… Another option, this is, like, a really generic tool.
Which is, like, at least I have some experience with it, because it's a Google project, but it's on… GitHub, and you can basically write rules to do transformations when you import stuff, so the end result is you basically get a script that you can use to copy in all the vendor code. So I think there's a couple options, and yeah, plus one on just having it be more maintainable, especially if we're copying the code.
Yeah.
Lukas Hering 00:29:42 I think PIP itself actually also vendors, so that might be a good… a good thing to look at.
Aaron Abbott 00:29:50 You mean, like, PIP supports vending, or, like, PIP does vending on their own internally?
Lukas Hering 00:29:54 actual Python package pip, like, just pip, like, they vendor stuff, So… and yeah, that's kind of… Probably the most standardized At least, I'm almost 100% sure, but I'd have to look.
Aaron Abbott 00:30:10 Yeah, yeah.
Lukas Hering 00:30:10 Yeah, I think we should just do more research, into, like, the vending.
Or, like, how we want to do vending, And then maybe we could extend it to, like, vendor stuff in the exporters, too, that would maybe help people? I don't know.
Aaron Abbott 00:30:26 Yep, and I…
Diego Hurtado 00:30:27 Please don't forget to add that anything you mentioned added to the notes or to the PR, so that I can take a look.
Lukas Hering 00:30:36 Yeah, I can add two.
Diego Hurtado 00:30:39 Thank you.
Leighton 00:30:47 Hey, sorry, quick question. So I noticed that the… Package dependency for packaging on instrumentation… open-telling instrumentation is a… Greater than equals?
We do vendor it, it is… technically, we're pretty much… painting the, like, whatever frozen version that we can choose. This might be a dumb question, but, like.
Does that mean that we have to… we should probably, like.
rename the public symbols or something?
If users want to bring in newer versions of packaging that don't want to conflict with our vendor version.
Aaron Abbott 00:31:26 Yeah, that's…
Diego Hurtado 00:31:27 I mean.
Aaron Abbott 00:31:27 I think that's what we were saying, that's what these tools should do, is they would rewrite the imports so that they would be either, like, a, you know, opentelemetry.underscore vendor or something like that. Like, I think you can usually customize them.
Leighton 00:31:40 Oh yeah, so I forgot how the behavior was this, so even if it's a different import path, but the same symbol name, like, is that fine?
Diego Hurtado 00:31:51 If it's a different input pad, then it's a different symbol.
Leighton 00:31:56 Oh.
A… But, like, they're not aliased as something different, right? Like… maybe I'm just not understanding, that specific use case, but… Does… do people know what I'm saying? Like, if it's, like, import underscore vendor… like, I don't know, like, HTTP duration, whatever, right? And then packaging releases something called… packaging.htb duration, right?
If I try to use that symbol.
Would there be any conflicts, or no?
Diego Hurtado 00:32:33 Well, I mean, if you… are you referring of importing those two symbols in the same module?
Leighton 00:32:42 Yeah.
Diego Hurtado 00:32:44 Well, then you need to use, the as, right, when you import, so each one gets named differently. Right, so…
Leighton 00:32:53 I mean, yeah, that was what I was… thinking, is that… that… then we have to do that as the aliasing on our side, right? Like, the vending side? Because we can't expect users to not use the public symbols there.
Maybe, maybe it's a… moot point, but… sorry, Aaron, you were gonna say?
Aaron Abbott 00:33:16 Yeah, I think the intention is for this to entirely be, like, an internal implementation detail, so it… it wouldn't be part of our public API, it would just be, like.
kind of like Diego said, instead of reimplementing it, we would just copy the code over instead, which gives you more or less the same result.
Leighton 00:33:33 Oh, okay, no. Yeah.
Aaron Abbott 00:33:34 Yeah, I think maybe one case is… Yep, sorry, I was just gonna say, one edge case is anywhere that you have to, like, use… interact with the user's version of the library and your version of the library, it won't work, so, like… You see this a lot in Node.js, where you can accidentally get multiple versions of a library, and then if you pass data between them, it causes all kinds of issues, but yeah.
Lukas Hering 00:34:00 Yeah, just to add there, we can… we can expose select public APIs for people to consume, like, similar to the, What do we use it again for?
Leighton 00:34:10 the import loop metadillo?
Lukas Hering 00:34:12 Yeah, yeah, yeah. Yeah, import the metadata, yeah, yeah.
Leighton 00:34:16 Yeah, sounds good.
Aaron Abbott 00:34:21 Okay, cool, and then I guess maybe the last thing just to mention is… we could discuss more after, but I believe on AWS Lambda, there was a lot of issues with, like, the package size, and I think it should be, like, not the same, because the amount of code is still the same, we're just copying it into our package, but we should just be careful about, for people who can use normal packages, that we're creating, like, some code duplication, so I think… I think there's some trade-offs, that's what I'm trying to say.
Lukas Hering 00:34:49 It's actually… well, Lambda… Lambda actually comes with pre-installed Python packages, like URLub3, so if we did vendor that, it would… it would bloat it.
Although I'm not.
Diego Hurtado 00:35:02 Right, that… Yeah, I think that's something that we should also consider when rendering, if it's worth it, in the sense that if there's a huge package and we are using just a tiny feature of it.
It may not make any sense to vendor it and add That one, that big package.
Lukas Hering 00:35:25 I mean, we could just… we can always vendor a subset. Again, I'm not sure if the, like, the tooling is very mature, but, like… Right, you could just copy The package that you actually use.
Diego Hurtado 00:35:36 Yeah, that'll be ideal.
Leighton 00:35:42 Yeah, I definitely care less about, size and more about, like, maintaining correctness over time without, like, human intervention.
Aaron Abbott 00:35:54 Yep.
Okay, cool. Sounds like we have some next steps, and yeah, thanks everyone for the discussion.
Diego, you… I tried this Slack link, I don't know if it worked for me. Do you wanna… Talk through this one.
Diego Hurtado 00:36:13 Thank you.
Can you try opening it?
Aaron Abbott 00:36:19 Yeah, it just… it just kind of went to the main Slack.
Diego Hurtado 00:36:24 Okay, so, well, then just help me, try to find this channel name.
And telemetry packaging…
Aaron Abbott 00:36:35 Do you want to share? That's fine, too.
Diego Hurtado 00:36:37 Oh yeah, that makes more sense, right? Let me just find the… Find this thing, okay, let's see… Okay, so… Just gonna share.
the… Okay, so… No.
in this, oh, no, it's in the automated Python channel. So, a few days ago, We stopped publishing the Elasticsearch experimentation, right?
And this… caused some issues.
Because, we have… the dependency… Every instrumentation that we have has OpenTelemetry instrumentation as a dependency, and that is a hard dependency. It is… We want, it says, use this exact version of mental limitry instrumentation, so… In the scenarios where someone is using Elasticsearch, and they want to keep upgrading.
OpenTelemetry and using new versions, right? This is not gonna work, because OpenTelem… the Elasticsearch implementation in its last release is pinned to an old version of OpenTelemetry instrumentation.
Which is gonna conflict with that same dependency for the new one, so… I was gonna suggest… to… Create one new last, release of Elasticsearch that removes this.
Hard dependency, and actually do the same for every other dependency.
Every hard dependency that we have.
of OpenTelemetry cementation in every segmentation that we have, right?
Just gonna stop sharing.
Did I share my screen?
Aaron Abbott 00:39:21 Yeah, yeah, we saw it.
Diego Hurtado 00:39:24 How can I stop sharing?
Someone help.
Leighton 00:39:31 the 13th.
Aaron Abbott 00:39:32 No, I think you're good now.
Diego Hurtado 00:39:34 Alright, great.
Yep.
So, actually, can you open the OpenTelemetry Python, the country repo?
And open any instrumentation.
Please.
Show, I wanna show you.
Yeah, just to exactly open any instrument.
Right? The… right, exactly there, so… See, it says, So… I think we can live without that.
The one below as well.
Aaron Abbott 00:40:20 Yeah, I agree. I think… I think we've discussed it a couple of times, and… It's, like, gonna be a requirement anyway when we start stabilizing some of these packages.
Yeah, I think it's just a matter of having somebody work on it, I don't… I don't think anybody's working on it yet, to be honest, but, yeah, I'm for this.
Diego Hurtado 00:40:48 Yeah, so… I'm just thinking about removing that constraint there.
those two.
Dependencies, and opening up ER fixes that.
Leighton 00:40:59 Diego, you meant, like, loosening the dependency?
Diego Hurtado 00:41:03 Yeah, just removing that constraint completely.
Leighton 00:41:09 Like, like, there's no hard dependency at all, or we have, like.
A tilde equals, or something like that.
Diego Hurtado 00:41:16 No, no, no, I mean, line 28 will only say open telemetry instrumentation.
Leighton 00:41:26 Oh, okay, okay, I see.
Lukas Hering 00:41:31 Well, probably at least.
Leighton 00:41:32 Yeah.
Lukas Hering 00:41:33 Till equals 1.0, right? When that…
Leighton 00:41:36 Right.
Lukas Hering 00:41:37 does happen.
Leighton 00:41:38 Right.
Diego Hurtado 00:41:44 So, I wish that Ricardo was here so that we could discuss what to do with the… The elastic spiritual.
instrumentation, but… but yeah, that's… that's what I was going to suggest, that we… The… make a new release that, removes this instrumentation.
Now, there is some, Also… D.
I don't know if, also, you want to reconsider This approach of removing, of dropping an instrumentation completely, And maybe just keep, releasing it.
Even with no changes, until the end of time.
What do you think about that?
Instead…
Aaron Abbott 00:42:43 the iPhone.
Diego Hurtado 00:42:44 experimentation.
Aaron Abbott 00:42:46 Yeah, I mean, I wish it fixed the immediate issue, but… would prefer to deprecate it, just because the one we… when we discussed this one, the actual instrumented library is deprecated, and it does cause, like, some headaches from Dependabot, for example.
Because we obviously can't bump the versions, and there's gonna be security vulnerability, stuff like that.
Diego Hurtado 00:43:09 Right, yeah, the point for keep… Continuing the… the release is that the instrumentation gets tested.
with, every release.
Which, should help people.
We use this for mutation, right?
Aaron Abbott 00:43:32 Yeah, but like… You know, presumably in 3 years, it's gonna… Have a bunch of vulnerabilities, and people probably don't want to… even for development, they probably don't want to have to install that stuff on their system.
Diego Hurtado 00:43:47 Okay, wanted to open discussion, about, about that.
I guess I can… I can open a… thread in the Slack channel, so we can discuss that in writing, but at least for this particular one, removing the constraints there, I don't know if there are any objections.
Aaron Abbott 00:44:15 Yeah, so I guess two thoughts, David. One is, for the specific issue with Elastic, is there a… somebody opened an issue in the repo yet?
Diego Hurtado 00:44:23 No, don't think, I can do that, I can…
Aaron Abbott 00:44:28 Yeah.
Diego Hurtado 00:44:28 I can…
Aaron Abbott 00:44:29 That would be great.
Diego Hurtado 00:44:31 Open those years. Alright, thank you.
Oh, I'll be back to me.
Aaron Abbott 00:44:36 Okay, the second thing, Diego, is on this one, like, I'm a little nervous about just removing it. I feel like… there's kind of this move in OTEL right now that we should just actually follow semantic versioning instead of pretending things are you know, beta forever, so… we're gonna have to stabilize the OpenTelemetry instrumentation and the semantic conventions packages, like, before we can do any of this, and I prefer that we could just pin… er, sorry, not pin, but we could allow all, you know.
whatever minimum range up to 1.x once we do that. I think Lukas said something similar, but the kind of prerequisite would be stabilizing the instrumentation API package, and then doing a release of that one.
Diego Hurtado 00:45:18 Right, but for the time being, we can just remove this constraint, it's… I mean, and we can stabilize later, right?
Aaron Abbott 00:45:31 I mean, I… I think… I think it goes both ways, right? Like, some… sometimes people will… Pulled this stuff in, and maybe we made a change, and then it breaks things, and then they're mad that the dependency constraints weren't correct, so… I don't know, it kind of goes both ways.
Diego Hurtado 00:45:47 Right, My point is that this particular constraint, right now, it's pretty meaningless, because it's pointed to something that starts with zero, right? So if we remove this constraint.
we… End up with the same logical constraint, but without the The dependency of it, so… It's… it's an… it's an… it's advantages to… to just remove this now, and And decided on stabilizing experimentation later.
Aaron Abbott 00:46:26 Lukas, you wanna go ahead.
Lukas Hering 00:46:28 I think the easiest… Interm solution is to just bring the package back.
And then… until we go to 1.0?
Because, like, I mean, my concern, like, we can't just leave this as a bare, dependency, because… I mean, I'd have to look at the Elastic instrumentation, but in particular, like, the SEMCOM opt-in, opt-out, those… there's a bunch of private stuff that's being imported, so if we ever change any of that, it'll blow up anything that's not, like, using the exact same version of the instrumentation library.
Which is… I mean, that's, I believe, why we have everything pinned against everything to begin with.
Hmm.
But, yeah, I think when we do go to 1.0, like, we should try to have these as lax as possible, so that you can actually have, multiple versions of… like, you can have, you know, 1.2 of AIO HTTP client and 1.3 of asyncIO.
Yeah, so, yeah.
Leighton 00:47:45 Yeah, Diego, sorry we can't give you, like, a short-term solution right now, but I think… Yeah, we brought this topic up so many times, and what Aaron has mentioned, like, on the reverse side, we've also Kind of got bit in the ass, too, where, you know, a lot of symbols, or… public API functionality was changed, and people were relying on Beta versions of packages anyways, so we were forced to pin this.
I think… also following, like, OpenTelemetry, like, guidance, or… getting these two stable, I think we are pretty firm on… Not making any of these… kind of hacky, short-term… not… I don't want to say hacky, but, like, short-term, like, exceptions just for one-off instrumentations, so…
Diego Hurtado 00:48:46 Hmm…
Leighton 00:48:48 Also, second thing, I… I've kept trying to start the stability for instrumentation, but I keep getting sidetracked, but… Yeah, if anyone is… interested in doing that. Sorry, I haven't… I haven't been able to get around to it, so…
Diego Hurtado 00:49:08 Right, well… I guess we can continue the conversation in an issue.
Because, I've already taken pretty much the entire meeting.
So yeah, let's continue with the rest of the topics.
Aaron Abbott 00:49:25 Okay.
Thank you. Yeah, I think Emidio dropped, so, we can… briefly discuss it, but maybe just next week as well. It doesn't seem super urgent, so… Yeah, we have this one on rough line length, and I think We've discussed it at great length, like, the… we kind of agreed to do this. I think Marcella was going to send a PR, but I never… I don't know if he got around to it or didn't see it. So this basically makes the line… Line length, sorry, line width wider, which creates a ton of formatting changes, but it has some… it's both for people reading it, and then for also, like, agents, because we're removing a bunch of characters, especially because Python uses spaces for white space, so… Yeah, I don't… I don't really have much to say on this one, but… We can ignore these… revisions in the Git blame, there's a feature to do that on GitHub, which is pretty nice.
And the last thing was it will mean that people have to… open PRs will have to… run the pre-commit check again after this happens, which, maybe we could automate that to avoid annoying people, but… Yeah, I think we should do this one.
We've already discussed it a couple times, so, yep.
Lukas Hering 00:50:48 I think Marcella had a PR, but he was getting annoyed because… You had to keep rebasing.
So I think, yeah, we should just merge this, like, as soon as possible, probably, just to save Dylan pain.
Aaron Abbott 00:51:05 Okay.
I mean, I… I… I can do it today.
I think that's fine, unless anybody objects.
Okay, cool, I will… I guess, merge these in, and we can… I could see if Copilot can maybe update the open PRs, that would be kind of nice, instead of bothering people with it, but… yeah, awesome.
Leighton 00:51:43 Oh, excuse my ignorance, but, like, how does the, ignore Git functionality ignore work for the, The commits… Do we have to do anything special, or is it just, like, a command?
Aaron Abbott 00:52:00 No, no, no, so…
Leighton 00:52:01 actually…
Aaron Abbott 00:52:03 Hold on, I'm not sharing the right tab.
Yeah, so there's this file, and we actually already did it when we switched to the SPDX headers, and you just drop the commit shot in this file. You could leave comments, and then, when you look at a Git blame, it will show you that I could probably pull up one of these files, let's see.
Leighton 00:52:22 So, is the current manual process, like, you squash your PR, and then in a follow-up, you add it to this… File.
Aaron Abbott 00:52:33 Yeah, yeah, I think we have to do that because we don't have rebase merging enabled in this repo.
Leighton 00:52:41 Okay, sounds good.
Aaron Abbott 00:52:43 Yeah, Leighton, did you want to send, like, a docs update to… Mention that, or the contributing guide, or whatever?
Leighton 00:52:49 Yeah, sure, I can do that.
Aaron Abbott 00:52:54 Okay.
Cool.
Last topic, this one was from where I volunteered in Emidio, and I think he left a comment in the meeting notes.
Basically, we had this discussion a couple times about accepting new contributions, that it would be nice if people could approach the library maintainers beforehand and see if they would accept native instrumentation.
Which, obviously, you know, sometimes that works and sometimes it doesn't, so… I think the… I don't know if the context is here, maybe it's in here, but… Yeah, I don't think the maintainers were open to it for this package, so… In this case, I'm assuming what Emidio was gonna say was it makes sense to have this in contribib.
And then the question was about component owners, so… Yeah, I don't know, anybody have thoughts on this one?
Yeah, Lucas.
Lukas Hering 00:53:52 I don't know if there's a convention, but… I would… from a maintainer point of view, I would only want to accept things that have a lot of people wanting it, like, you know, reactions on the issue and stuff.
I… I'm a little worried, like… I'm guessing, like, this is all probably claw-generated, like, people are just, you know, finding something to instrument versus, like, actually having a use case, so… We need to be a little… careful about that, I think. I mean, I think this is a valid use case, but, I'm not sure, like, how many people are actually… Actually really want this.
Right.
Aaron Abbott 00:54:35 Yeah, absolutely.
Diego Hurtado 00:54:38 Well, I mean, sorry, sorry I interrupted, Actually, the issue here is… is adding this fermentation for the Discord library here, in the contract rep, because they can have it Anywhere.
They can make their own.
Leighton 00:54:59 Yeah, but the problem is…
Diego Hurtado 00:55:01 For a particular need, right?
Leighton 00:55:02 Yeah, but the issue is, like, we… like, the… the… the Open Solomon for contributors Bear the burden of supportability if, like, we don't have a dedicated component owner, like, over time, so… I think… I think previously, without, like, agents, it was easier to manually kind of gate these things by, like.
Having a promise from the original contributor, and we kind of outlined that in the contributing guide now, but now it's, like, so easy to create Instrumentations, or any contributions, really.
Diego Hurtado 00:55:40 I think it's, like, a fine balance.
Leighton 00:55:42 Between, like, dating.
Oh, sorry, go ahead.
Diego Hurtado 00:55:46 No, I mean, so what I'm getting from you, Leighton, is that we should reject this?
Leighton 00:55:53 No, I'm not saying that specifically, it's more like we still want to always encourage, like, contributors and everything, but… I think it's… this is more of a nuanced problem now.
I'm curious at how other… SIGs, deal with this.
Ludmila, I think you have a hand up.
Liudmila Molkova 00:56:15 Yeah, so I don't know how all SIGs deal with this, I think Java has a special place called Java Country, but they kind of separate the instrumentation with blessed set of instrumentations, the ones that we know community is interested in, versus the Java country, where All the questionable things end up in, and they can be promoted.
But… one thing I would push back on, like, do we… do we have Discord semantic conventions? Why do… why Open Celebrity should be the, entity that owns this?
And, like, yeah, to Diego's question, why does this instrumentation can live in this repo, it can live anywhere.
This is, like, a popular framework that's used by the places where Python app and telemetry is used, primarily in the server applications.
Probably not.
Aaron Abbott 00:57:22 Yeah, and I think the only thing I would add, maybe as a devil's advocate, is… People do… well… I think in Gen AI, nobody came here and offered to necessarily drop a bunch of instrumentations, but it is nice to have it in an open governance place where, People can come and contribute, and if a maintainer disappears, or a code owner disappears, we can find somebody else, but… Yeah, I think that's kind of a subjective question, and I don't have the answer right now. I don't have any experience with this library, so… I would… Yeah, I hear you on the semantic conventions for sure, Liudmil, like, it doesn't seem like a super common use case, but… Yeah, I don't know if we're gonna make a decision today, so maybe we can chat about this one again next week. I think Ricardo has more context, too, because he was going back and forth on the issue.
Yeah, anyone? We've got…
Liudmila Molkova 00:58:15 Quest shift.
Oh, sorry.
maybe we should establish a principle, like, what puts instrumentation here? Like, doesn't matter for this library, but what are the criterias in general?
Diego Hurtado 00:58:34 Well… I mean, my criteria would be that, We went a little bit, Out of our way to support a lot of instrumentations here, and now we are facing the consequences, so… No more new instrumentations. What I mean is that I'm okay with being the bad guy and just telling them, no, we're not going to support this and close on the reach.
I'll do that.
Lukas Hering 00:59:05 I would say, like, we can just maybe wait it out, like,
Diego Hurtado 00:59:10 like…
Lukas Hering 00:59:11 If, like, there's a… like, if people keep coming back to us, and there's more and more interest, like.
yeah, then we can go ahead. Like, I… I think, like, maybe letting the issue kind of bake for, like, maybe a month or so, and if there's, like, you know, 10 reactions on it, then, okay, yeah, there's clearly people want this, so let's do it. But if there's, like, 2, which is what… there's only two people that actually want it, right? That's not… I don't think that's enough. And I don't know if there's a way to formalize it, but…
Liudmila Molkova 00:59:42 The issue's been there since April.
Lukas Hering 00:59:47 The issue has been there since April?
Yeah. But it's still…
Liudmila Molkova 00:59:50 PR is new.
Lukas Hering 00:59:52 Yeah, it just doesn't seem like there's still a lot of interest, but, like, I don't think we should just straight out say, like, no, we're never gonna merge this, but just say, like, okay, well, there doesn't seem to be a lot of support now, if that's what we… if that's what we determine.
So maybe, like, we could just suggest, like, okay, you can create your own package if you have interest, and then maybe if, you know, if that gets enough popularity, we can consider, like, taking ownership of that sometime in the future.
Liudmila Molkova 01:00:22 I think that the voting should not be from the people in the community who want it, the voting should be among people who want to maintain it.
Diego Hurtado 01:00:34 Excellent point.
Leighton 01:00:36 Then there's gonna be none.
Liudmila Molkova 01:00:39 Exactly.
Aaron Abbott 01:00:44 Alright, folks, I think we're over time. Good discussion. See y'all next week.
Leighton 01:00:50 Nice, thanks guys.
Lukas Hering 01:00:51 Durham.
Liudmila Molkova 01:00:52 Yeah.
