SIG: eBPF instrumentation
Date: 2026-02-18
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Rafael Roquetto** 00:44 Hey.
**Giuseppe Ognibene | Coralogix** 00:49 Right off of it.
**Rafael Roquetto** 00:50 Yeah, cool. How are you?
**Giuseppe Ognibene | Coralogix** 00:53 Find you.
**Rafael Roquetto** 00:55 Fine, fine, Jenny, started.
**Giuseppe Ognibene | Coralogix** 00:58 Hi, hello. Hi, Mike.
**Tyler** 01:00 How's it going?
**Giuseppe Ognibene | Coralogix** 01:03 Buy a new one.
**Tyler** 01:05 Did well, yeah.
Also, getting started.
**Rafael Roquetto** 01:10 Hopefully with coffee.
**Tyler** 01:13 Yeah, just, just made it.
**Rafael Roquetto** 01:15 Cool.
**Giuseppe Ognibene | Coralogix** 01:27 I eat.
**Tyler** 01:28 Hey, Steven.
Giuseppe, did you say you were going to KubeCon this year, in Europe?
**Giuseppe Ognibene | Coralogix** 01:54 No, I don't know. Nimrodi will decide. I went to force them with Mattia.
**Tyler** 02:00 Oh, that's what I'm saying.
**Giuseppe Ognibene | Coralogix** 02:03 We invite you going, then?
**Nimrod Avni** 02:05 I don't know if I can decide for you. I need to… I need to check, though. I think we… we have a plan to send a couple people. I need to see.
**Giuseppe Ognibene | Coralogix** 02:14 I only know that I can decide for myself, so…
**Tyler** 02:20 Yeah, so when it comes up, then you get to make the decision, yeah.
Yeah, I mean, I, I'm gonna end up going. I know that Nicola's also got a talk, that he's presenting there as well, so I think there's, there's good reason to come.
Come up to Amsterdam, yeah.
I wonder if, I don't know if Mario's coming. No, there's Mario.
He might be able to…
**Mario Macias** 02:45 So…
**Tyler** 02:47 Hey.
**Giuseppe Ognibene | Coralogix** 02:48 Are you going to, KubeCon EU?
**Mario Macias** 02:51 I haven't… I… I haven't yet submitted any talk.
No, you mean the Amsterdam one, so…
**Tyler** 03:01 Yeah, yeah. I got an audio… I got the audio code. No, I'm not going, I'm not going.
Oh, okay, yeah.
You're maybe thinking of going to, North America, though?
**Mario Macias** 03:13 Oh, yeah, yeah.
**Tyler** 03:16 If you get a talk accepted, something like that.
**Mario Macias** 03:18 Yes, yes, yes, why not?
Yeah.
**Tyler** 03:25 Yeah, Robert, who just joined also, should be there, so… Yeah, I think it should be a good crowd.
Pretty excited about it.
Yeah, so we could probably get started here. If you haven't yet, please go ahead and add your name to the attendees list. If you have, agenda items you wanted to talk about.
go ahead and add them there as well, and then, yeah, we can jump in here and get started. Just a second.
Hmm.
See if this works.
Cool, okay.
This is gonna be a great thing. Awesome.
Well, welcome everybody. Yeah, to start us off, Raphael, you wanted to talk about the, enhanced OTL eBPF, debug environment variable to allow printing, trace pipe only?
**Rafael Roquetto** 04:42 Yeah, so… I've been toying with it, and I just want people's opinion, I'm not sure if it makes sense, but basically the idea would be… now we have… it's a Boolean, right? Either it prints, or it doesn't. And when it does, it will print both to the trace pipe.
And also to the standard output of OBI.
The problem with the standard output of OB is that sometimes the logs are limited, like, because of the amount of characters in the line, because of how the ring buffer works, the events.
And so, I… oftentimes, I find myself just looking at the trace pipe anyway, For the food logs.
And even commenting out the ring buffer output to the standard output so that I can see what OB is doing in, like, split screen and a trace pipe with only the BPF logs without them being intertwined.
So I was just wondering if there's any appetite for, like, changing this to… it could be backwards compatible. Basically, hotel eBPF debug would be… One, or whatever, come up with a name that keeps the current behavior, but another value that would just print to TracePipe without sending the, the, events to, to the ALB output.
So that's, yeah, that's pretty much it.
**Tyler** 06:16 I like the idea of, like.
levels here, like you're talking about, it sounds like. So, based on configuration value, it can send it someplace versus another. I like the idea of keeping the, like.
The default behavior if people wanted to use that, but allowing configuration to move on, that sounds good to me.
**Rafael Roquetto** 06:35 And then, I will also, like, I haven't commented it there, but I've done something locally, which I also would like people, people's opinions on. You know, like, I think it was, Giuseppe who added this functioning towards the end of the logged line.
I find that really useful.
And… but for the trace pipe, it does not need to be at the end of the line. You can put it in the beginning. So I modified locally the macro to just, on the trace pipe event printed in the beginning, but… The downside with that.
is that, you know, like, in some kernels, the older ones, you can only… the VPF print, dbg PrintK, or printk can only take 3 arguments.
Otherwise, the kernel kind of goes bonkers, it doesn't like it. If we do that, then we lose one argument, because one argument becomes the function parameter. So I don't know if this is a good idea. So that's the downside.
maybe we could detect that, I don't know, I'm kind of thinking out loud here. I'm not sure if that's possible. The upside? Maybe it is. The upside, like, is that, I did that in, I added a… with that in mind, I added two other macros, BPFDBG, entered, and exit, which you can put in the beginning of a function, and then the log starts with, I don't know, function name, entered, and then you see the messages, and then it left. So, it's… I found it really… help for, for, for the bugging. So, I don't know. Like, if there is any appetite, no strings attached, I can, a few days from now, maybe raise a PR with that, and people can actually see the code and comment and give their ideas, if… There's any… anything?
Giuseppe?
**Giuseppe Ognibene | Coralogix** 08:25 Yeah, and just want to say that we added the function name at the end, because I think Nicola told me that it is better at the end, because maybe if we put it at the beginning, we… We can lose some information instead of just the function name.
**Rafael Roquetto** 08:47 Yeah, yeah.
Yeah, correct. So yeah, I would… I wouldn't change that. The event that gets shipped to user space keeps that, but the event that… but what we do for… For the trace pipe.
what's the function name in the beginning, so they can be different. And in TracePipe, we don't have this limit of…
**Giuseppe Ognibene | Coralogix** 09:06 Yeah. Character cut, so then it gets easier to read.
**Rafael Roquetto** 09:10 I don't know, it's just an idea. Downside being that in other kernels, You might lose an argument.
We could disable that for all the kernels. I'm thinking out loud here, maybe I could just, you know, when we detect the kernel, not do that. Anyhow.
Just… it's just food for thought.
There are no objections, I could raise a PR, and then people can actually comment on something more concrete.
Yeah, that's it.
**Tyler** 09:42 Okay, yeah, I think a PR sounds good. Let's, let's take a look at it. That sounds great.
**Rafael Roquetto** 09:46 Cool.
**Tyler** 09:47 Awesome. Alright, yeah, thanks for bringing that up.
Let's jump back in here. So, Next up, I wanted to… bring this issue to people's attention. We had talked about this before, this is something that Nimrod had mentioned as well.
It's a long-standing, open issue in open… or, in any sort of eBPF code, and this is the idea to, take our generated, BPF2Go files and include them in the commit history of… of the repo, in some way. So, there's obviously, like, some prior art here.
That we talked about as well, namely, like, this issue, talking around the fact that There's, I think a lot of different things that we've explored to try to solve this in the past. In fact, people have given talks on it.
It's not an easy one. And so, anywhere from running a Go module proxy, committing just to the release branches, post-processing the Go code, obviously, I think that's what we're already doing, documenting the dependency generation step.
Then using Git LFS, and then asking, Silium to support This sort of runtime object storage, as well, but… That never went anywhere. So… I was looking into, like, the impact this would have if we just started committing. One of the things I was looking at, like, was we talked about the release process, and just committing on release branches. I think that's something that we can do. It is… It's a partial solution. I was looking at this mainly because, with the release… or the recent edition of the, collector receiver, that was added, which is pretty awesome. It'd be great to start looking at how we can integrate this as a collector component in any collector, but… The hard part there is, is that you need to have a local copy of this repo to generate the files, and then do some sort of replace statements. And so, like, it's… It would be ideal if you could just tell it, you know, point at this tag and go for it, but it might also be ideal if we could just point it at main, right? Or point it at a commit, so we could do these patch updates if we do have, like, bug fixes or something that comes out that we need to actually get a quick fix in.
So, if we did something where we were only, generating the files on release branches, that would mean that main is still not, like, importable and buildable. It also would mean that, like, the collector, or wherever these dependencies on Obi would be, you know, upstream or downstream, that we could only depend on these tagged releases without having to go through jumping the hoops that, like, we already are doing right now.
So, I was looking at evaluating just, you know, if we did commit every single file to, to main, or every single, like, object file and domain itself.
wasn't great. So I was trying to get some, like, real numbers here, and, like, looking at the actual, sizes that we're looking at, something around, like, 12 megabytes, I think, was, on average, what we would see if we looked at all of the current binary files that exist, compression-wise, this can get down pretty, pretty substantially. It's not, like, you know, amazing, but it definitely can be compressed, which would be something that would be happening, in, you know, the Git history itself.
That being said, if we're, you know, just doing, like, kind of an upper bound and a lower bound, which is, I think, reasonable way to look at it. So, you know, touching something like, all of the actual files themselves and not the headers, you'd get something like, I think it was, like, yeah, 558 megabytes per year.
in the Git history, that's going to be tracked. However, that's likely not… it's the lower bound, because the more likely thing is, like, the shared headers, every time that those get changed, they will mostly trigger a full regeneration, and that's gonna come out to be something closer to, like, a gig per year, based on our current, commit rates, which is about 120 commits I saw over the past, or, 122 commits over the past year.
to these files, like, I'm just assuming we're gonna have the same frequency there, that may be a bad estimate, but it's, you know, it's based on numbers, I guess, so… That's where that's coming from. So, yeah, like, with that together, like, yeah, I think you're gonna start to see, like, pretty severe impacts to the commit history and being able to clone the project within, like, a year or two.
If we start committing to Maine?
I do want to point out, though, that, like, I did check that, like, Go itself, like, if you do, like, a Go import of this package, it… that doesn't pull the full Git history, that pulls, like, just the top-level, you know, files from that particular, Git reference that you're calling, so… the impact on doing something like GoGit is… this won't have an impact there. It'll only have an impact for developers, like.
us who are, you know, fresh clones, or if you're waiting a while, like, pulls for this, or local copies of this may become extremely large, so… Yeah, I wanted to pull this all through.
Obviously, you can, look through this. There's a proposal to try to, like, you know, if you wanted to, commit to Maine, this is something that we would have to do, there's a bunch of different places we'd have to take a look at. But it's more about, asking people on the call, like, what their thoughts on this are, and What their appetite for going in this direction is.
**Rafael Roquetto** 15:17 Yeah, we've talked so much about it in the past, and we've done so… you know, so much gymnastics.
And… I hate the fact that we have to commit stuff, because… first, thank you for the numbers, like, I think this is really good to actually see the numbers and have a proper notion of the impact.
And… Having said that, I feel like we should just do it, because… I think the benefits of integrating this… that's my personal opinion, of course, but the benefits of integrating… being able to integrate this in the collector, Outweighs whatever, you know, just… go get another cup of coffee while your repo clones, and there's no other way. Like, there's no other way. I mean, at least I'm convinced that there's no other way. We tried writing modules, we tried, you know, OBGen files that you removed, we tried everything, and it's always full of trade-offs. This is the… you know, the only downside with this approach, in my opinion, is that it, you know, it blocks the repo.
Otherwise, it's straightforward, it's flexible, you know, it's the go approach, so… you know, I raised my white flag and said, let's just do it and be happy, my humble opinion.
**Tyler** 16:37 Yeah, I'm in the same boat as you, Rafael.
But yeah, I'd love to hear if there's other opinions on this one. I know, Mike, Nicola, you've given talk on this. Robert's got a thumbs up.
**Mike Dame** 16:49 Yeah, I mean, I really don't like, committing it on every commit. I was always kind of, I think, along the release lines. I've actually, like, early in my career, I made the mistake of committing binary files, and, like, our servers, our production servers ended up running out of space pretty quickly, because I didn't know how to use Git.
And I thought, well, I'll just throw these… they were… they were PSD files, so those were a little bit bigger, but… I think that this project is… unique in a lot of ways. It's a unique EBPF project, so when you ask, like… we talked to, like, cilium maintainers and EBPF maintainers and asked, how do you handle this? And they were like, we just commit it.
We're dealing with a bunch, like, in theory, infinite.
files, you know, if we start adding more and more instrumentations, this is… the numbers that Tyler has now could be 5 times as much in a year when we add more instrumentation, so it's literally unbounded.
they're… so it's a unique EVPF project in that way. I think it's also a unique GO project, because for most Go, or for every other Go project, there aren't binary files that you need to generate, or, you know, Go generate can handle most of what you need to, output, but this is unique. It's got these eBPF files, so it's not your standard Go project. That's why I think that Having, you know, an extra step to build them through, whether that's the vendor or a different artifact tooling or something is… I think reasonable, because there's nothing else like this anywhere, ever before.
Yeah, I don't think that the… The trade-off for… just how much space it could add to the repo, it can end up being a lot more than just, like, going and getting another coffee. It could be like, this doesn't fit on my machine anymore. It's a possibility.
So, that's… that's something that I would… really keep in mind, I think for… developers, and I mean, I'm the person advocating for making this, like, a big development, you know, framework project, too, that people are really importing everywhere, so, I do realize kind of the irony there.
But I think that… I don't know, if… if everyone else… would prefer it that way, then that's fine. I'm not gonna stop on it, but I would say that release… Inclusion is probably the best path forward to minimize that, but It's up to other people's opinions, too.
**Rafael Roquetto** 19:28 Do we, Like, to… to be able to add these to the collector, it needs to be vendorable, or does it work differently?
Like, because… we have the, you know, the OB, Docker image that pulls all the Clang tool chain, so I'm just wondering, there's no way… for… For this to work, with them just generating files.
On… on the go, right?
**Tyler** 20:01 Not without, like… Large changes to their tooling.
**Rafael Roquetto** 20:08 In how they're doing the builds over there.
**Tyler** 20:11 Yeah.
**Nimrod Avni** 20:12 We need some pre-built step, I guess, if you want to, like… By default, I think there's some collector builder that you can just, you know, vendor, like, the OB or the profiler or whatever, and if we want to have some free step, we need to, like, I don't know, change the way they do the build.
**Tyler** 20:32 Yeah, I can… I can show a little bit around, We have an example of this, That, Nimrod has added around this building, and so… Yeah, so this is… this is the first step, is… is literally make sure you have the generated files, and then once you have the generated files, you can then… you just run this, as Nimrod said, like, this tooling called the OCP, and all that does is it takes this configuration file here.
And it will run it through. But the important thing to note here is that, like, we are… we're doing, like, that manual vendering, I guess is what you want to call it.
Where we're saying, like, here's the thing that we actually want to use, and this is how you would normally declare it, but since… if you tried to pull this V05, using the standard Go tooling, you won't have any of the, the, generated object, so it has this replace statement that's really critical here.
So, yeah, that's… this is where that comes from.
**Rafael Roquetto** 21:35 We do the same for Baylor, by the way, exactly the same thing.
so, yeah, I mean, Mike has good points as well.
I really don't know, like, -oh… would it be worth trying to, like… I mean, we can always fall back to committing the files with all that entails it. I guess the question is… Have we exhausted all the other options? Like, even helping them with the tooling, or… If we're convinced you of that? No, because maybe we should try to investigate that a bit further, just to prevent committing the files.
And if not, then, I mean, then we know what's… I don't know.
**Nimrod Avni** 22:18 The question is, how much of a footprint is it to commit it… let's say that we take the middle ground of doing it on release.
And even, let's say, like, we say you can't vendor OB from main, like, without, any of these steps.
But we say, okay, we can kinda… push for more, like, patch releases, that's, I mean, like, every week or something, create a patch release, if there is, like, any change that we… want to publish that specifically includes, generate files.
And… Maybe we can check, like, if we do something like that once per week, or once per two weeks, how, like, how much will it inflate our repository?
That'll be fine.
**Rafael Roquetto** 23:06 We do that for beta?
Sorry, I thought you were saying something?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 23:09 Yeah, I think that would be fine.
I mean, it's better. To be honest, like, we ran Bela with committing to binaries for such a long time.
ourselves, I mean, it does add up to the repo over time.
Especially with the… with the velocity of development we're putting.
Things are better now, to be honest. After Mattia made the change to not actually have a debug build and all this, and kind of stripped down to a single tracer, so we're… Kind of, like, tracers are limited in how many we have.
I mean, mostly there's just two objects now, technically.
The Go Tracer and the generic tracer.
I know we're adding more, but those… those other tracers don't change frequently, so, I mean, TP Tracer, now that Raphael is working on it.
So maybe 3 that will change from time to time.
I think it's not the end of the world either way. Release would be better.
from… repo size and whatnot, but you're right, I mean, you can't build OTO Collector main Where they'll be included.
I just… Which is… impediment, in my opinion.
**Mike Dame** 24:21 That's a good point, Nicola. I forgot that… I was still thinking, like, the Go Auto terms, where it's, like, every library and every instrumentation is its own program, but the fact that OB is generic like that… And yet it does make a challenge for… Building the collector, I had a question about, is this… when it comes to, like, repo size, because that's kind of the main concern, is the repo size, I think.
is it permanent? Like, if we do this and it blows up the repo history to, like, gigabytes and gigabytes, and we decide, well, we gotta stop and take it out, is that now… the permanent repo history size because of all those changes, or is it something that we can back out of in the future? I'm not sure about specific, like, the impact on Git.
**Stephen Lang** 25:13 I think it is. You can't undo it. You'd have to… you'd have to rewrite the history with a rebase.
**Mike Dame** 25:18 I was worried about.
**Tyler** 25:19 Yeah, well, so… you can rewrite the history, right, but that's gonna be a, like, a security issue also for our Go packaging, because, like, the module system that we're using right now is going to pull from the Git history, so if you start changing that, then the shot, or, like, the sums aren't gonna match up anymore for old releases.
So yeah, it… I… Yeah, to Steven's point, like, it… yeah, it's pretty drastic, you have to do, like, a forced push to the git history to get all this cleaned out, but then it, like.
I think it's a no.
I think that comes down to, like… I don't think we can do that, yeah.
**Mike Dame** 25:53 So I… I think I've shared this before, I don't know if we do something similar in OBI, but I'll put it in the… The notes here. This is how we generate the, vendored objects in Otagos. We have this, like, that we call at build time, or, you know, you can do it development-wise, and it, like, goes into your, vendor library.
your local GoMod cache and generates it. I don't know if there's a way to, like, include that sort of process into collector contribib. When we add Obi, is there any way to say you know, like, the root makefile or something, update that to include a step like this. I don't know if there's any path for components that have custom Make file, or, like, build steps, but just to… kind of pulling at strings at this point, but yeah.
**Tyler** 26:48 Yeah, currently there isn't, to that point, but I think to yours and Rafael's point, like, maybe that's worth, like, exploring first.
And seeing if we can… can help you know, make that happen.
I, I, yeah, I don't… it's like… I want to be optimistic. I'm also somewhat pessimistic, because, like, the collector contribib is, like, a huge, like, maintainer burden for the maintainers, and they're, like.
already well overwhelmed. So, I mean, it's not like we're completely new to the project, so I think we have some sort of, like.
cachet with them, but, like, still, like, I… I… I'm happy to start the conversation.
But I guess I might be a little bit more pessimistic than I'm letting on, that it'll happen, but I'm happy to take a look, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 27:37 What this, how about we started committing them in the release, so we unblock that?
Process, and then commit to making a release every two weeks?
And then… If anybody wants to build in Maine, we provide the instructions how to do it.
**Tyler** 27:57 So… so committing every 2 weeks is, is the exact same frequency of what I just was showing.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 28:05 Oh, okay. Okay.
**Tyler** 28:07 Yeah. Or, sorry, like, committing, like, two different changes per… like, it was something like, yeah, so… I think.
**Mike Dame** 28:16 So is that only on… are we talking about committing them onto main, or onto, like, a release branch? Because if that's… I don't know if you tested that, if committing these onto a separate branch, does that affect, like, the main size of the return?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 28:28 It will, yeah.
**Tyler** 28:30 So Nicola, can we…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 28:32 every two weeks, it's equivalent to committing them to main, because that's how much we actually change the BPF files, the frequency.
**Tyler** 28:39 Right.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 28:40 Factoring that's fine.
I'll just say go in Maine.
**Tyler** 28:45 So, can we go with maybe asking the collector contrib first?
And then… and then go with what you just proposed, Nicola?
Or do you think it's kind of like a fool's errand to go that direction?
**Pellared** 29:03 I just have one idea on top of my Mike, showed.
just maybe 5 minutes, just maybe having to assess if it's even worth exploring, because what I see, Mike, is basically just, you know.
It's just using make files.
I think it could be possible to do it more reusable using the Go ecosystem, just making it, you know, a Go module, basically, and then the collector could invoke it using Go Generate. I remember that in Go Generate, you can also access other packages, and you can version those.
So I… and if I remember correctly, I think already, I think the collector already uses Go Generating step, if I'm… if I'm not mistaken.
So, I think it could be possible to build something, like, we just need to extract, instead of using the makefile for building these objects, you can just extract it to a… just, you know, to a Go binary, and version it, etc. So, instead of using makefile, you can just use it in Go Generate.
This seems reasonable, or not at all?
**Tyler** 30:16 I don't think it's the tooling as much as it is, like, the processes that are missing in the collector contribib is the problem.
Like, they… they don't… Call any step prior to… the… The building of their, their, repository, like, the collector that they build there.
**Pellared** 30:37 They're not running Go Generate? That's what you say?
**Tyler** 30:41 Yeah, they're not running Grow Generate or… yeah.
**Rafael Roquetto** 30:44 They're new.
**Tyler** 30:45 Calling the OCB task, yeah.
**Rafael Roquetto** 30:48 Even if they were, so the root of the problem is.
And this happens outside the conductor. Everything that's being, vendors like, so, OBIS would be vendor, right? So it ends up in a Go module directory, and that's, by default, read-only, like, it's immutable. And if you do a generate step with Go Generator otherwise, that means you need to write binary files inside that read-only module. That's what, Mike showed us, and that's what we used to do before. We, we, we tried that.
It's very ungo, like, and you're basically writing the user's module, the cache, so it works, but it's kind of, you know, kind of a house of cards, so we, you know, we moved away from that, so that's the problem at the end of the day.
**Pellared** 31:40 Okay, I see.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 31:50 To ask the, co… The collector folks, if it's something they're willing to entertain, and if not.
Bite the bullet.
**Tyler** 31:57 Yeah.
Yeah, we can do that.
I mean, I think… I think that that's probably the best way to do it.
I feel like we'll be back here next week, talking about, committing to Maine, but, Hey, at least we.
**Mike Dame** 32:12 It…
**Tyler** 32:12 Cross all the T's, right? Like…
**Mike Dame** 32:14 Yeah, that's… that's just what I'm trying to do, is just check everything. I get if we… if we go there, and especially what Nicholas was pointing out, it's that it's not a lot of, You know, tracers, so… I get that the size is limited, and, like, what I was sharing for Otogos 2 works, because that's just us, like, we're just building our thing that way, so it's… when you're… we're kind of talking about doing it from the other direction as the library that's trying to provide the thing to do, so… Yep.
**Tyler** 32:52 Okay, yeah, it seems like we've descended into horrible ideas at this point.
I'll go back to share my screen. I will… I'll take it as an action item to try to sync with the collector contrib folks, and I will… I will report back on this one.
Okay.
Okay, cool.
Next up, I also had this PR. I just wanted to call this out really quick, just for asking for reviews on this. This is, for the V050. There's… I've gotten a lot of reviews, thank you already, Mattia and Nimrod, I did update as well, if you could take another look on this one. For other folks that are on the call, this is going over a lot of the things that were just released in the last V05.
If you want a good understanding of the features that are coming out with this one, like, it's pretty, pretty great. I was happy to compile this, it was pretty awesome seeing what we're getting out of this one. So, yeah, there's, just needs more reviews on this, and then obviously somebody from the docs team, but I can ping them afterwards. I just think they're probably waiting on us, agreeing on this one, so I just wanted to call it out again.
Okay, real quick on that one. No big deal.
Yeah, so next, Steven, you want to talk about CI pains?
**Stephen Lang** 34:07 I'm sure everyone's nervous.
**Tyler** 34:09 Yeah.
**Stephen Lang** 34:11 Yeah.
GitHub have, migrated a load of the rumors from, AWS, or whatever it was before. I think it might have even been some kind of GitHub on-site.
data center. But anyway, they're running in Azure now.
And runtimes have gone, kind of, through the roof.
Actually, I click this spreadsheet.
So this is a spreadsheet that I made when I was originally looking at speeding up the runtime, so I don't know if you remember, we had 90 minutes on the VM tests back in the day.
So the… this new column, C, this was where I got the CI to… But then GitHub did an Azure migration, and then we started seeing times like this. So this is the same codebase, just a week apart.
And, you know, the VM tests have gone from 18 minutes to nearly half an hour.
And also, they're really unreliable now, and this is not our fault. So if anyone has seen any steps that are taking, like, an hour, and then timing out.
This is the runners themselves, which have become unstable.
I've tried to mitigate this with a whole series of PRs. I have made them faster again. There should be no steps that take… There should be no workflow, entire workflow.
That should run longer than, 25 minutes now. Everything should be within half an hour.
Even with Azure.
So yeah, just a heads up, if you see, like, a step that takes longer than half an hour, try and cancel it and rerun it. Nothing should take longer than half an hour.
And yeah, things just seem really unstable. We have different hardware now, the CPUs are definitely different, the… the software emulation for the QEMU VM is definitely flaky now. I've seen a load of CPU stalls.
I have put something in to detect stalls and, like, force the VM to exit.
So they should fail earlier, but still, I'm seeing some steps that are taking up to an hour.
So this is on top of flaky tests, right? We still have some flaky tests.
But I'm just trying to improve, like, the… quality of life for just re-running these… these things. I have tried to use the GoTest Sun re… auto-retry feature, on, like, most workflows now.
But yeah, it's still painful, and there's nothing on githubstatus.com, like, it says it's all fully operational.
It isn't. So there's definitely something going on, With GitHub, and yeah, it's not entirely our fault, so just wanted to raise that.
**Tyler** 36:51 Yeah, thanks for… thanks for pointing this out. I definitely feel the pain as well. It's good seeing the numbers. It's also good hearing the context. I didn't realize as much as going on in the background.
I might say you might wanna, raise this to more of, like, the OpenTelemetry governance level, because they have different contacts in, like, the CNCF that may have other contacts or something like that, where they may have contacts at GitHub.
So, I don't know if you want to maybe just post something about this in the maintainer's channel, maybe opening a community issue is something they could do? I don't know if other folks have other ideas, but I think that, like.
Yeah, like you said, like, there's something wrong, and it's not really being identified right now.
**Stephen Lang** 37:32 Which… which channel is that exactly?
**Tyler** 37:35 It's Hotel Maintainers, oh, I see.
**Stephen Lang** 37:38 Thanks.
**Tyler** 37:39 Yeah, if folks… also, you should join that as well, if you want to be more included in… Project-level discussions, by the way, on the call.
But yeah, I think that's a good one to ask this kind of question in, and so… yeah, I'll… I think if… if that doesn't work, or you don't get any response, maybe a community issue, because I know that, like, the GC tracks the community issue stuff, so, that's… Probably also another place, if there's no traction, but there's usually a pretty good reception in the Slack channel.
**Stephen Lang** 38:13 Cool, thanks.
**Tyler** 38:14 Yeah, okay.
Yeah, well, thanks for looking into it, thanks for those fixes. Are there any other, like, things we need to look at? I think you had one more PR, if I'm not mistaken?
**Stephen Lang** 38:23 One more from about half an hour ago. So that I said that no workflow should take longer than 30 minutes. What I want to do is put in, like, a So GitHub has two ways to, exit a job based on a timeout. It's a step timeout and a job timeout.
The step timeout also isn't working.
So the step timeout is already 35 minutes, and so why are we seeing things that are taking an hour? Doesn't make sense. So what's happening is the runner process itself is crashing, and so it can't enforce a timeout.
So, I'm hoping to introduce, like, a global job timeout of 30 minutes. But to do this, I went through all the workflows just to confirm that nothing takes longer than 30 minutes. I did find one that does.
It only runs on the release on main, it's the publish image.
That takes 45 minutes, and so I looked into it. It turns out we're building the ARM images inside a QEMU with software emulation, and so the x86 image takes, like, 3 minutes to build, and the ARM image inside QEMU takes, like, 42 minutes.
And it's all, serialized, so we've got… so this PR parallelizes it, gets rid of QEMU, uses a native ARM runner.
For the Armin Edge, and then an x86 runner, but yeah.
There should be, like, less than 10 minutes compared to the 45 minutes, so should still be able to introduce the global 30-minute.
Job timeout.
**Tyler** 39:53 Okay, yeah, that's funny, I didn't realize we were doing that. I think it probably comes from the time when we didn't have arm runners, or… yeah, so, yeah.
**Stephen Lang** 40:00 Yeah, yeah, it was.
**Tyler** 40:03 Cool. Alright. Well, thanks for looking into that. I will take a look at those PRs as well, and we can, yeah, move on here.
Okay, cool. So… next up is OpenPR review, but normally we try to… do that at the end. So, Robert, you had a question here around, the Cates cache.
You're muted, by the way.
**Pellared** 40:31 There's… yeah, I still know there's an answer from Steven.
**Stephen Lang** 40:37 Yeah, so the question is, what is K8's cache? Why does it exist? Why isn't it documented? I can't answer the latter, but I can tell you what the cache is.
And this is to prevent incidents in large Kubernetes clusters.
when running Obi as a daemon set, every instance connects to a Kubernetes API server.
So if you imagine you've got a cluster with a thousand nodes, you have a thousand OBs, all trying to talk to the API server, all asking for, you know, every single update of every pod IP address change.
all the time, and this causes, effectively, like, a denial-of-service attack on the Kubernetes API server, and it can bring down the entire cluster And this can happen even on managed control planes like GKE.
Yeah. So, you gotta watch out for this. So, to avoid this, you can run the cache as a separate deployment, so not a daemon set.
With much fewer replicas, and then this kind of centralizes the Kubernetes API connections to, A smaller number of replicas.
**Mario Macias** 41:38 Yeah. The… the underlying issue is not all 100 of these connected. Is that for every… since it subscribes to all the resources in the whole cluster.
For one OB connection, each node is connecting to the rest of nodes, so this grows exponentially. This has… this… I'm not sure if it is being fixed currently in the… I don't know if it has been released, but there is a later Kubernetes version will fix this issue, but at the moment, for most Kubernetes versions in production, we need to… we need to do… to centralize this connection instead of distributing from all the OBs.
**Pellared** 42:27 Okay, so, based on that, I have two following questions.
First one is, should we even distribute it as a release as a binary, or is it only, you know, as a separate container? Because it seems to be, like, useful only for Kubernetes.
**Mario Macias** 42:47 Yes, it's only useful currently for Kubernetes.
So, yeah, we already ship it as a container.
**Pellared** 42:55 Okay.
Alright.
And the second is, should we create some issue to document it, or update the OpenTerminal docs to, kind of.
I didn't think about it?
**Mario Macias** 43:11 Oh, good point. I think we slightly documented somewhere, only the option.
And the… the help charts should be… should be already documented, but you're right, maybe mention it.
Is… it will be a good idea.
**Pellared** 43:31 Maybe I'm wrong, maybe it is documented, but it's not maybe searched in the correct way, maybe it's needed some additional troubleshooting section. I have… yeah, just, you know, just the thing that I learned about this just, like, today when I was really looking at Tyler's, yeah, regarding leases.
And yeah, that's how I discovered that it may be useful.
**Mario Macias** 43:50 Yeah, it probably is not well documented. Maybe it's mentioned in some property, in some related property, but… not… I… I don't think it's… Very well documented in detail.
**Pellared** 44:05 Okay, I would… I would just follow up, I'll just create any kind of issue, just to double-check the documentation.
And, you know, just a high level to make sure that people are aware of this.
**Mario Macias** 44:18 Okay.
**Pellared** 44:19 Thank you.
**Tyler** 44:21 Yeah, and so, Robert, I would definitely say, like, DevDocs are really important here, because, like, you just… you know, you don't know what's going on, other devs won't, so DevDocs, I think, is a great place for it. But, yeah, I think creating issues is a great idea, and then if we need to… I don't know if we need something upstream, or, like, in the OpenTexture.io for, like, end users. I don't know if they care so much about the details there, but I do think that, like, what you're.
**Pellared** 44:42 Right now, right now, for your release PR, I will just remove this information about this binary, because that's why I started to think, why is it even, you know, distributed?
**Tyler** 44:55 Oh… I see.
Yeah, I was kind of wondering about that as well. I just included it. Like, so, like.
**Pellared** 45:03 You're saying maybe don't include it in the binary, or don't… Yeah, that's Mario, what's Mario said.
**Tyler** 45:10 Oh, sorry, that's what Mario said, too? Okay. Yeah, alright, well, we can… we can pull that out then. Yeah, because I was figuring… but, okay.
Yep, perfect, okay.
**Pellared** 45:18 Thank you.
**Tyler** 45:19 Queen.
Awesome.
Okay, we have 15 minutes left. I do want to go through open PRs, just to kind of get a status update on this. There's definitely some older ones.
I will maybe just pause here. If people are reminded of a PR they have, we have limited time, so we're not going to be able to get through everything. If you needed some attention on this, is there something, obviously, Steven has just raised this one, I think we need to get some eyes on this, we already talked about it. Any other ones from folks that they're waiting for feedback on, or reviews on that we should take a look at first?
**Mario Macias** 45:51 Oh.
**Nimrod Avni** 45:52 I have, sorry, Maria, go ahead.
**Mario Macias** 45:55 No, no, please, go, go ahead.
**Nimrod Avni** 45:57 Yeah, so I have a couple, like, the very old ones, that I fixed. I tried to, like, finish all the comments before. I think the… Docs one, we talked about it in, like, a couple six back, I was in PTO, and I… I wasn't able to… I saw you talk about it as well. I just updated, like, something that we said about JDK versioning, and I think besides that… besides what you told about, Tyler, about Formatting it a bit differently, but we said maybe we can just push it and then worry about… how we, like, the format. I think this is done, but if anyone wants to have another look… And… Yeah. Yeah, so this is, I think, this is done.
**Tyler** 46:48 Okay, cool. Yeah, so this is just looking for reviews at this point.
**Nimrod Avni** 46:51 Yeah.
Okay. And there's another one of the config, schema one, which is a bit longer, but, like, I just keep… I think I did, like, rebasted it, like, 5 times now, so, if… I think it's… it should be… go. There was a last round of comments that I, applied.
But if anyone wants to review it again, I think I fixed most of the stuff.
And from now.
The only thing I'm… like, I was kind of not worried, but maybe should consult with you guys, is… basically, I want to keep the scheme up to date, so if anyone adds any config.
variables, they'll need to run another, like, make command of make config generate schema. If not, like, the CI will fail. So, do you think it's something that should be added to, like, make FMT, or that should only be reserved for, like, code formatting, or is there anything You know, like… What is your idea for that?
**Tyler** 47:56 So, I think… I've got a lot of ideas, unfortunately. And so, I think that, yeah, to your point, I think that that's a great idea to try to, like, put this into something for the pre-commit. I think we already have a pre-commit command for, like, the Clang Tidy.
Doing something there, I think it'd be great. I don't think in the long term it should go in that direction, and the reason I think that is because I think it should actually switch to be the opposite way around. I think that what you want is for the declarative config in OpenTelemetry is what we want to try to support, right? And declarative config in OpenTelemetry is… using this JSON schema, right? And so we want to be able to have users provide all the tooling with declarative config through this. This is gonna be… this is already used in the collector, so, you know, if we get the collector integration, this is going to be needed there as well. We need some sort of, like, config, definition that we can actually, like, parse off into the declarative config.
So I think in the long haul, I would say we probably want to go the other way around, where the JSON schema is the thing that's going to be generating the code. And from the code, then you would import whatever is generated into… you know, all the different things. Right now, that's not the case. But I think, like, to keep things in sync, do exactly what you just described, and we should try to shoot for the inverse of that, where the code is being generated from the JSON schema, yeah.
Okay, makes sense. I think, I think that's a…
**Nimrod Avni** 49:19 So this is probably, like, a good start for this, and then… once we have this, it's gonna be easier to, like, reverse.
Yeah.
**Tyler** 49:28 And this is, I think, extremely important for the stability path that we're on, the 1.0, because we're talking about, like, the config is going to be the thing that I think is going to be, like, the most important from the end user's perspective that we can't break. Like, any changes there are going to be very impactful for users, so… one, having the universality of the declarative config being supported is going to be very helpful, but two, also, I think, like, having it well documented in the structure is going to be, like, very helpful for a lot of different reasons. So, yeah, I see this as very important as on our path disability here.
**Nimrod Avni** 50:03 Cool. Yeah, so this is, I think, ready for review, as well.
**Tyler** 50:07 Okay.
Yeah, awesome. I will… I'll try taking a look at this. Other folks, please take a look at this as well, and yeah, we'll… we'll try to integrate.
Okay, Mario, you had, I think, a PR you wanted?
**Mario Macias** 50:22 Yes, this AWS cloud metadata, it's… the functionality is missing, but I… I… it's missing. It's complete, but I've… lately, tests are becoming very flaky, so I'm… I'm trying to fix, in parallel some… some flakiness in another PR, but if in the meanwhile you want to check this, pull request about adding… it adds to the metrics and traces the resource attributes related to the cloud.
You know, instance, image, zone, availability zone, etc.
**Tyler** 51:06 Yeah, this is awesome.
I'm really excited about this. I think this is great, yeah. All this kind of stuff is, like, super important for, like.
customer conversations I've had in the past, like, they care a lot about this kind of stuff, so… Having our ability to detect this is gonna be really helpful.
Cool. Yeah, alright. So, yeah, if folks are on the call, if you have time, please take a look at this one, and, also needs review.
Cool. Any others?
I think… Raphael…
**Rafael Roquetto** 51:46 That one, I'm gonna get to it. I'm working on the TP injector, like, and TP Injector deals with TCP options.
And once I'm… I raise that PR, that's when I'll shift to this and update this one. My… might keep it as a separate PR, or it might be part of that, I'm not sure yet. So it's still… it's not… it's not forgotten. Like, it's there, it's just a… I'm reworking things that we went back to this, so I want to finish that before I… I deal with this.
**Tyler** 52:19 Okay, yeah, that sounds good.
Cool.
Nimrod also has a PR for Couchbase, flexible framing. This is pretty recent, yeah, last week, so this could also use.
**Nimrod Avni** 52:36 Yeah, I just, I think I pushed today, Ruffles, your changes for non-allocating, And just, I think it finished the test, and it should be, good.
**Rafael Roquetto** 52:47 I saw that. I didn't review it thoroughly, but it looks good. Thanks for that, like, it looks awesome.
**Nimrod Avni** 52:54 Yeah, thank you.
**Tyler** 52:58 Cool.
I'm gonna skip over some of the draft ones at this point.
introduce app network, Tracer for the TCP RTC sample metrics. I don't know if, Giuseppe's still on.
**Giuseppe Ognibene | Coralogix** 53:13 Yeah, it's mean.
I… I just did the updates that Nicole asked. I think all the tests are good.
**Tyler** 53:24 Cool, so this is just looking for some more review, then.
Oh, this is flaky, but… Okay.
**Giuseppe Ognibene | Coralogix** 53:31 Yeah, there are tons of leggy, actually, I just… yeah.
I hope that… And I have another one in draft, but I think that I will, I will bother Rafael, for that one, for, resize the ABPF maps.
**Tyler** 53:47 Okay.
Perfect, yeah, that sounds good.
**Rafael Roquetto** 53:52 Yeah, about that one, well, let's talk, like, a sync, see how… how, how we go about it, like, I'm happy to help. Like, so, the change that I'm making to the TP injector, like, I'm introducing new maps, there's a second storage, and things like that, that's why it was so fresh in my mind, the whole map things, and I had to deal with, like, context propagation and whatnot. So, this week's been a bit busy for me, but next week, I can, like, set some time aside, and I can, like… help… I don't know how you wanna, go about this, but, let's talk offline, and I can help you.
**Giuseppe Ognibene | Coralogix** 54:30 Okay.
**Rafael Roquetto** 54:31 You know, kind of feel.
**Giuseppe Ognibene | Coralogix** 54:32 We can, we can have a call when you are free. Just keep in mind that, my, my proposal was because Actually, I started with your idea, just to put the max request, and blah blah blah, then I started to, like, say why we don't add this, this, and this, and then I added too many things, I think.
But we, we can avoid…
**Rafael Roquetto** 54:56 Sure. Thanks for that.
**Giuseppe Ognibene | Coralogix** 54:59 Thank you.
**Tyler** 55:04 Cool. Alright, got a few more minutes. So, there's… cleanup for the Bayless stuff, there's resource, or, dependency updates.
Mike, you also have a last selecting instrumentation by PIDS, PR?
**Mike Dame** 55:22 Yeah, and just, as part of what I'm trying to do to drop this into what we have, I was looking… oh, I didn't see that there was a comment already, so I'll check that. Just looking to add, you know, directly passing a PID list to, what's… what's instrumented in making that the… the matcher.
Yeah, I guess maybe we don't need the, the whole… the whole selector here, so I'll look at that comment and get to it. The next thing that I'd like to do after that is try to see if there's any way to kind of, like, dynamically update this list at runtime. That's where it'll really get more useful for us, is if I can add and remove from what's being tracked from the, you know, what matches the PIDs at runtime. It seems like it should be doable.
But just trying to get this through first.
**Rafael Roquetto** 56:10 So, to the second point, we have this valid PIDS map that we, you can… you can update, use that to update things at runtime.
So I think the infrastructure is already there. And I have a question, maybe the answer is already in the PR. But If we're passing pids.
what are we passing? Are we passing just a value? How do we deal, I guess what I'm asking is, how do we deal when, let's say, Obi's a demon set.
but, like, you're instrument in containers, I've been passing the… PID of the container namespace, or the host PID. In that case, if it's the container namespace, how do we deal with the, you know, the possibility of having duplicated things? We need to specify the namespace, like, things like that. Do you… Do you know that?
**Mike Dame** 56:56 Yeah, that's a good question. I think what we're working with is the, the host namespace PIDs. We kind of run similarly, Odigit as a daemon set, and we end up working with the PID value that's passed to that instrumentation that tells it what to attach to through That's, how GoAuto was set up. Similar, you know, it started with the exact… file, like the path, and then the PID is processed from that. So, in this case, we just get the PID directly, because we've already done, like, resource process detection on it. But I'll double-check that, make sure that I understand that correctly. So that's a good question, too. Thanks.
**Rafael Roquetto** 57:35 Yeah, okay. Cool. Thanks.
**Tyler** 57:39 Awesome. Cool. Alright, I think that's about the amount of time we want to spend on that one, coming up in the end here. So, yeah, we can pause.
Here, any other topics or quick mentions people have, that they wanted to mention?
**Rafael Roquetto** 57:52 Yeah, real quickly, like, the message with the git LFS issue, going back to the commit binary, like, that didn't work for us. We tried that in the past, I don't remember why. I don't know if it's worth revisiting it, but Yeah. Yeah, it doesn't solve the…
**Tyler** 58:11 It doesn't solve, like, the Go stuff. So, like, the collector still couldn't do, like, Go Git or Go builds on it, because Git LFS isn't integrated into Go. Well, that's not true. If I remember correctly, you can make… You can make modifications to the Go subs… to the Go system, but it doesn't do it natively. Yeah, so that's something… that's a good point.
**Rafael Roquetto** 58:30 Because if you look at that… that… the issue, there is a comment that says that you can… the accepted solution says you can do, like, require a module, but instead of doing .git, you do .git-LFS, and then go picks it up. So, if I understood correctly, it treats… there are two different modules. There's the… if you do a .git, it treats it as one thing. If you do a .git LFS, something else, like, even though it's a SIM repo?
**Pellared** 58:57 I think what you described is just a proposal, right?
**Rafael Roquetto** 59:00 Oh, okay, it hasn't been implemented yet, I see.
**Pellared** 59:03 No, no, it was just a proposal that I shared, that, yeah, there are people who want it, yeah.
**Rafael Roquetto** 59:08 But it… I thought it was accepted, but maybe I misread the issue.
**Pellared** 59:13 accepted, but it doesn't mean it's implemented, you know, sometimes the stuff is accepted, but it's…
**Rafael Roquetto** 59:19 Okay. Because we tried it in the past and it didn't work, so I just got curious. Alright.
**Tyler** 59:25 Oh, I see. Sorry, yeah, I missed that comment. I got you now.
Yeah, Yeah, proposal accepted, yeah, it's not… yeah, okay.
Yeah, unfortunately. I like to live in that world, too, so I'm with you.
Awesome. Alright, well, we're right at the end of the time here, I want to be respectful of people's time. Good seeing you all, I will see you all in a week's time. Until then, yeah, talk to you later. Bye.
