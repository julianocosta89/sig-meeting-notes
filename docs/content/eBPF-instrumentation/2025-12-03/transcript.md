SIG: eBPF instrumentation
Date: 2025-12-03
Duration: 64 minutes
============================================================

## Zoom Recording Transcript

**Tyler** 00:46 Hey, Mario.
**Mario Macias** 00:48 Hello!
**Tyler** 00:49 How's it going?
**Mario Macias** 00:51 Fine, and you…
**Tyler** 00:53 Doing well, yeah.
Just getting back into… starting up the day. How about you, Raphael? How's it going?
**Rafael Roquetto** 01:01 I'm good, good, getting started as well. I got myself a new, coffee grinder, so it's…
**Tyler** 01:09 What'd you end up going with?
**Rafael Roquetto** 01:10 Just a preview one.
**Tyler** 01:13 Yeah, okay.
**Rafael Roquetto** 01:13 I, I, I couldn't… couldn't get myself to…
**Tyler** 01:16 To pay 500 bucks for that one yet. We'll see how it goes.
Yeah, yeah, stay tuned. I'm sure, I'm sure that'll, that'll come. The coffee addiction material.
**Rafael Roquetto** 01:27 I can see your smirk, so yeah.
**Tyler** 01:30 That's what I thought, too, when I first, bought my first coffee grinder, and then years and years later, yeah.
But yeah.
**Rafael Roquetto** 01:37 You don't…
**Tyler** 01:38 Soon you'll be… soon you'll be pulling espresso and, yeah, having your own little cafe.
**Rafael Roquetto** 01:43 That's when you won't see me around here anymore, then.
**Tyler** 01:48 No, we'll see you, because you'll be so active, super hyper.
**Rafael Roquetto** 01:50 Fair enough, fair enough.
**Tyler** 01:52 Yeah, with caffeine, right?
Well, cool. Welcome everybody, looks like we're getting some people filtering in.
If you haven't yet, go ahead and please add your name to the attendees list.
And if you have agenda items you wanted to talk about, go ahead and add them there as well, and we can get started here in just a second.
Okay, alright, so, starting us off, we don't have too much on the agenda.
Rafael, you wanted to ask about using, mailing lists or GitHub discussions?
**Rafael Roquetto** 02:50 Yeah, so, I raised it a little, a little thread on Slack.
about doing something like that, but I wanted to know what… people think of it. I think, for instance, Mattia, I guess he suggested using GitHub Discussions.
I came from it from a standpoint of mailing lists, but the main idea is to have a space for people to propose ideas, or suggestions, or tell all of us what they're planning on doing or working on.
And, Let people digest that asynchronously and respond asynchronously, you know, so you don't have to sometimes reason on it on the spot.
I don't know, it's just a thought, I don't know if… it's something we want to do, but I thought I would bring it up.
**Tyler** 03:45 Yeah, I mean, I think.
**Rafael Roquetto** 03:45 Thank you.
**Tyler** 03:46 I like the idea of GitHub Discussions, is that… I think it should be enabled, right?
Yeah.
It looks like it is.
But yeah, I mean, I'd probably… Is it?
Oh, it's not enabled. Okay.
Huh. Alright.
Yeah, so, I mean, I think if we can enable that, I think that'd be probably ideal.
I don't know why that's not enabled by default, but, Oh, maybe it is now.
Yeah, so I think maybe, we can go there. I'm a little bit hesitant to… go email mailing list, just because, personally, I, would not follow any of that discussion. So, yeah, I'm interested to hear other people's thoughts, though.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 04:45 I like the discussions in GitHub, to be honest. I subscribe to the repo, I get all notifications, I know it's relevant.
So… I mean, mailing lists, also, people may be hesitant to expose their email addresses they're using.
well, GitHub is maybe, you know.
**Mario Macias** 05:08 Okay.
**Mattia Meleleo** 05:09 Yeah, also, as I was saying, is GitHub discussions I like because you can redirect people here instead of opening issues for simple questions.
or Slack, we can redirect people there and have it more organized.
**Rafael Roquetto** 05:28 I think that's awesome. One question that I have, because I've never used GitHub Discussions, can you have more than one Threads. So, for instance, in QT, we have at least, well, have more than one, but 2 million lists. One is called QT Interest, where users discuss QT, for instance.
But there's the Qt dev, where the developers of QT will discuss, you know, do I bumped C++ version, or here's this new feature, or just refactor that. I think the distinction, maybe not in the beginning, I don't know, it's just something to bear in mind, it helps organizing things, like, more… people contributing to the project versus people asking questions about the project. I don't know if it's a distinction I want to do, just thought I would mention it.
**Mattia Meleleo** 06:12 Basically, basically there are these, categories, on the left, and, there are, like, normal questions, questions and answers.
There are the ideas category, general, it's, it's organized this way, and this can be customized, I think.
I have never played with it, but I think it can be done.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 06:37 Yeah, that sounds amazing.
A lot of the stuff that we do, I think we talk on GitHub for a specific thing, like an open an issue, tracking, like, upgrading the C++ version, and we can have a discussion there, specific to the topic.
I think we can make do without mailing list, but…
**Rafael Roquetto** 06:55 We can always elect to split later if push comes to show, yeah.
**Tyler** 07:02 There's also this labels function, Raphael, if we wanted to start categorizing things, like, further, like, you're saying, like, a particular topic or thread, but yeah, I think that… In general, like, the categories are probably a pretty good indicator.
**Rafael Roquetto** 07:21 Sounds good.
**Tyler** 07:23 Yeah.
Yeah, I mean, they're kind of, like, a little bit… it depends on how we want to use them. You know, if we want to, like… Yeah, I guess take them seriously, I think, like, that'd be interesting, I'd be interested to try that. I don't see them that useful in a lot of other projects, but yeah, if you find this to be useful in other projects, and we can try to, you know, prioritize these, I think that sounds good.
**Rafael Roquetto** 07:50 Yeah, my suggestion would be… don't force yourself to use it, but if you see the need, like, I don't know, if I have an idea, for instance.
That will take me… time of the prototype, I might first go there, open your discussion, tag everyone who's involved, and see… get some thoughts.
**Tyler** 08:08 Before putting in the effort, that would be, I guess, my main motivation.
**Rafael Roquetto** 08:13 and then you'll see if it's there, if it's not there, it's not there.
**Tyler** 08:19 Yeah, and I like the idea because it takes a lot of this async conversations that we're having, you know, as a priority, or trying to prioritize them, I guess is kind of the thing, because… Right now, it's all this synchronous conversation that we're having here in this meeting, where everyone has to show up outside of time zones, so I think that makes sense.
Alright, shall we give it a shot, see how it goes?
**Rafael Roquetto** 08:44 No strings attached.
**Tyler** 08:45 Yeah, it should be enabled, now it looks like, but if not, let me know, or let a maintainer know, and we can try to get a… Better setup.
**Rafael Roquetto** 08:55 Alright, thanks.
**Tyler** 08:57 Cool. Alright, next up, Mark, you want to talk about, Python Async.io?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 09:08 Sorry to put you on the spot, Mark, I had to put on our names.
**Tyler** 09:10 Oh, I guess Nicola's there as well. Oh, sorry.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 09:12 I mean, if you want to talk, yeah, welcome to.
Not Alga.
Yeah, okay, yeah.
**Marc** 09:21 Yeah, go ahead. Okay, sure.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 09:25 Yeah, so, I guess after KubeCon this happened, I think David Ashpel and, and, Aaron here kind of started talking about, Python ASICIO, which was sort of… we don't have any examples for that, and it… And, there's cases where our context propagation currently does not work, but fortunately for us, Aaron here has done a lot of work for us, and he even wrote a little BPF trace program that showed us how we can do this.
So, I… this morning, from my time with Mark, we were just trying out various combinations, to see conscious propagation fail.
And we came up with an example that actually was reproduced, reproduces this issue.
And, I think it's up to adding two U-probes, and we'll be able to support async IO, thanks to the work that Abbott actually Aaron, sorry, I have it.
It's down here.
But essentially, he… he found these two places where Python, before it does anything work, it kind of dispatches the context, the current context of the variables, I guess.
To another thread?
And we can use that to correlate.
to, So, I don't know, I can share the other link that he tagged me on. This is part of the, OpenTelemetry Python.
Let me tag it in the… In our notes as well.
**Rafael Roquetto** 10:58 So there is no need for anything on the Python side, it's all done by your probes on our end? Okay, that's awesome.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 11:06 Yeah.
Okay, cool. Let me add the link, just a second. So, technically, he experimented a lot with few options here, How… so if you look, like, he tried various things.
But I think at the end, what he has… if you see us in that U-probe context for ours, on the side, there's an example PNG.
Yeah, if you open that, you're gonna see that the BPF trace He showed us how, you have multiple… thread programs here.
And before… The handoff between one thread to another happens through the parent doing CopyCurrent, and uses the context pointer, so whatever he has Actually correlate any yellow.
And then… Once we actually switch the thread to run on the separate thread, so 292 thread.
Canning over to 296.
Then the context run on the fault… on the Child thread, or the one that actually is going to do the async work.
is on Context Run, so… If we track copy current to create that parent-child relationship for the context we're tracking in a map, then we should be able to look up on context run to see if we have a parent.
So this… this allows us to do full correlation. So I did a quick hack into a branch, to see if it worked, and yeah, absolutely, these two U-probes will let us do this.
So it should be a simple patch to support.
async I.O, Python.
Which is kinda cool.
**Tyler** 12:59 What is… what is this BT?
Oh. File.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 13:02 Yeah, it's like, I don't know if you guys have seen this, but BPF Trace is a pretty cool kind of programmed you can install in your Linux system, and then you can write scripts, and it's so easy to attach any probes. You can just say, oh, in this library, attach a probe, and yeah, write this C code, and it's sort of like a script. It's a subset, like, of C, But it's very approachable, so if you need a quick and dirty thing to kind of, like, try out a couple of probes and extract information, it's… It comes pretty handy.
So, without him touching Obi or understanding our codebase, he was able to prove out this.
We're just printing the values.
**Tyler** 13:44 That's cool.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 13:45 Lauren?
**Florian Lehner** 13:47 Yeah.
**Tyler** 13:47 I mean, I… this sounds promising. Go ahead, Florian.
**Florian Lehner** 13:52 question on… I just opened the BT Trace script and see a lot of references to the internals of Python.
We did have the experience that, the… internals and… These functions are not consistent across minor versions.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 14:12 Is there…
**Florian Lehner** 14:15 Was there work on checking various minor versions, or is this just explicit for, 3.13.9, as I see it in the script?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 14:26 Yeah, we're gonna have to probably, look through, and see if… I try… I have 312 on my machine here, I haven't actually upgraded to 313 yet, and… The signatures are simp… the same.
And it's perhaps not very unusual, I guess. Run context, the first argument is the context, which is what we use as a key, and then… The copy current returns the value of the new context, so… Probably won't break too often, but yeah, they might actually change.
the internals… Between miners, so we're gonna have to… keep updating, like, for other things. Like, Go is also, like, we… Business as usual, I guess, for us.
just recently, gRPC… Let's provide a patch.
to support GRPC177 or something like that.
Made.
Yeah, and then sometimes it's a back and forth. They'll do a change, make something a pointer, then we have to do something different, and then they'll… They'll revert back, it's just… It's not a point anymore, but yeah.
**Florian Lehner** 15:35 Yeah, I see the struggle that we are facing the very same, that's why I ask.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 15:42 I think some work we need to… I don't know if you have a proposal or maybe a suggestion. Do you guys do this differently?
But it seems like, so for LibSSL, we were kind of… lucky, because the Linux usually links the libssl.so to whatever version.
I see the Python doesn't do that, so this is… libpython 312.
that is, like, Python 313, and so on. Do you have each individual ones that you list, or… Is there a…
**Florian Lehner** 16:13 We do a little bit of a trick. We do on-demand disassembling on the endpoint, so we don't hard-code offsets and stuff like this.
We read memory from symbols, and then do disassembles of the function.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 16:30 Oh, I see. So do you… do you also have, like, an offset… table for the Python… Based on the version, or no?
**Florian Lehner** 16:39 For some, yes, just to say, hey, this, symbol is available in this version, but the offsets are, dynamically checked, with, with disassembled.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 16:54 Oh, interesting.
So this would work even if Python stripped their symbols, or no?
**Florian Lehner** 16:59 Yes.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 17:01 You know, so maybe we can…
**Florian Lehner** 17:03 That's why we can work with, stripped Go executables as well.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 17:12 Okay, so maybe that's something that we can… yeah, it's really good if we can reuse some of that code.
**Tyler** 17:17 This is in the profiler, Floria?
**Florian Lehner** 17:20 Yep.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 17:23 Because I noticed that…
**Tyler** 17:24 How do you… How do you do the disassembly of, like, the Go code? That if the symbols have been stripped, you just are looking in the memory specifically for a particular symbol itself, or how do you identify that?
**Florian Lehner** 17:37 For Go, it's quite easy. For Go, if you strip the symbols, you still have the GoPCLN top, a special section for Go.
**Tyler** 17:44 Otherwise you will not see panics in Go and, the output.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 17:48 Yeah.
**Florian Lehner** 17:48 And, it's quite… we walk the executable and find the magic header of the GoPCLN tab, and then walk the… just walk the GoPCLN tab.
That's the… that's the way for… Go?
And for other languages, like Python, Ruby, whatever, we do actual disassemble of the function, so we have a disassembly package for x86 and ARM64.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 18:18 Do you look for the specific pattern of code? How do you know this is the start? Yeah?
**Florian Lehner** 18:21 Yep.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 18:22 So you try to say, oh, this matches, so it must be the start of.
**Florian Lehner** 18:27 context.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 18:27 It's wrong, whatever.
**Florian Lehner** 18:29 But we don't do… we go, we don't go into, much detail about, function offsets and stuff like this. It's something we are not interested as, we are just interested in, hey, Is this a function start, yes or no? And that's… that's enough for us, that's why we keep it quite simple.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 18:47 I see.
**Tyler** 18:49 So you don't really need the parameters being passed to those functions? You just look for the… okay.
**Florian Lehner** 18:53 Yes, we don't cross it.
**Tyler** 18:57 Yeah, that might be a little bit harder.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 18:59 Yeah.
**Tyler** 18:59 If… especially… yeah, but… And maybe it's something we can take a look at.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 19:06 Yeah, I mean… I mean, for us, it's like, we'll… we'll make this async IO work if there's Python symbols.
I mean, for now, and… see how many people complain. The official Python versions that you get in Docker images, or you do pyenv install, or any of that stuff, they come with symbols.
Like, Aaron actually mentioned that Ubuntu strips them, and I know they strip them even for Java. Like, OpenJDK will come without symbols, which is… whatever, I don't know, but if you get the official OpenJDK image, It does contain symbols, so… Maybe that's the first step, and then we can see… If many people run… or they, they run with, like, whatever, they did an app to install Python.
Yeah, I think, to be honest, the latest version of Ubuntu complains if you do that. They're saying, well, no, you should version your Python environments and all this, so… I don't see that as big of an issue, but… If you get an official image, it probably will work.
**Tyler** 20:14 Yeah, okay. It sounds like it's worth pursuing, though, Nicola, to your point, so I think everyone's… I don't hear any opposition to going down this path.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 20:23 Yeah, yeah, I think so. I think maybe the only trickery we're gonna have to do is… right now, the way we look for the modules, we look for a specific name.
to attach the U probes to, so we're gonna have to come up with a way that we can just look for a prefix.
So, we see litpython.so, but not .12, whatever, 13, and then we're gonna say, between these versions, we know this works, so…
**Tyler** 20:51 Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 20:53 These are the symbols we attach to, and for these versions, we… this, but… So we need to add that into our uProbe, kind of, lookup.
Apart from that, I think… Should work.
**Tyler** 21:07 Cool. Yeah, sounds good.
Okay, Next up on the agenda is, something I added there just a second ago, but it was asked by, I think, Nimrod, actually, in Slack, and the question is just, are we… do we want to do another release?
It looks like, Nirma, you had mentioned that the code, Node.js rod harvesting was added, Elastic, open search spans, TCP-based context propagation, OB Java Agent… I think there's even more than that now, at this point.
But, yeah, that sounds, like, worth releasing. What are people's thoughts? I don't think we've seen a release go out.
**Nimrod Avni** 21:50 I'm… I'm for it, because, some of our customers are really wanting to, use the new features, and I don't want to tell them to pull from main, because that's… I think we kind of want to discourage that, but I still want them to keep, you know.
Keep, like, the… the newest versions.
**Tyler** 22:11 Yeah, I'm… maybe we can talk during the review of the PRs, but I don't think there's anything… that we really want to try to get included in here as well, so I can take that as an action item to try to get a release out this afternoon, if everybody's okay with that.
**Nimrod Avni** 22:30 On 4th.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 22:31 We did have a question on the on the Slack, somebody asking about, okay, so it worked for me, but do I deploy this? I guess we have to take a stance. Do we think it's stable enough for people to run this?
**Tyler** 22:47 This is the… oh.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 22:49 Regan Carter?
**Tyler** 22:51 Yeah, yeah, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 22:55 I don't…
**Nimrod Avni** 22:58 I can say, like, what we have, like, I know, I guess, in Grafana, you encourage people to use Vela, and that's, like, partly Obi, right? Or, like, you know…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 23:08 It's mostly open.
**Nimrod Avni** 23:09 Mostly homie.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 23:10 Like, we just have the Grafana Cloud integration and some other stuff that… we didn't donate. I mean, not because we didn't… But the process metrics were… considered, like, duplicated with Prometheus, and… exporter, and… Otto collectors, so…
**Nimrod Avni** 23:28 Thanks for…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 23:28 backwards compatibility, like, people that have been using Velo for 2 years, they're… We need to migrate them over to use the new environment variables and stuff, so we do have a layer that converts them.
**Nimrod Avni** 23:41 Yeah, I think we have a couple of customers using it, and I mean, some of them had, like.
onboarding issues, but I think most of them, it's, like, working in production, but I think we can say something like, you know.
Deploy it on, like, a restricted set of nodes first, and then… You know, see how it, works, and then, like, you can expand it, but, like… My thing, it should be fine.
It might also relate to the next, topic I wrote.
The agenda.
**Tyler** 24:20 About troubleshooting? Yeah. Yeah, I… so… I think, just going back to the response to Regan Carter here, like, I'll probably try to write something, like, it's not a stable project, right? So we don't actually make any guarantees yet.
That being said, like, our stability is… is probably more… Than… than we're alluding to, just from the fact that, like, we just talked about, like, we have, like, people using this. It's actually a pretty well-matured project, like, things are already, like, pretty tested in environments, like, battle-tested, because it came from the Bela ecosystem.
I think we talked about this previously, like, we're trying to fast-track, stabilization here. I think the configuration is the only other thing that we're waiting on, which we probably should talk about, I think, as we go through some of the PRs. I saw Mario had a PR.
So yeah, I mean, I think that our recommendation should always be, like, conservative, in the sense that, like, you know.
understand that, like, there… there are potential changes that could come, but I don't think that there's… a likely… I mean, I don't see… Major shifts happening, right?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 25:35 Yeah, I mean, maybe the response should be, like, config options and that stuff will likely change.
And we don't guarantee stability of the config.
However, we can say Grafana and CoreLogix do ship this to customers, at least, to companies, and we stand behind the products. If you run into issues, we'll help you fix it.
**Tyler** 25:54 Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 25:55 It's no… no different. We… we have an official product that we give to customers on a Bela, which is based fully on Obi. That's their core technology, so… it's just with additional packaging to support Brafana stuff, so… It's not like… Don't use it in production content.
**Tyler** 26:18 Yeah, I think we're all on the same page.
Yeah, I think maybe the concern from them is maybe something to the effect of, like, yeah, concerns with security and other issues or something like that, like turnaround times of those, but, like, we're really responsive, there's a really rich and healthy developer community here right now, and I think it's only growing, so, like, I think in that sense, like, it shouldn't be a hard thing. I think, to Nimrod's point, the deploying and the troubleshooting is probably going to be the hardest part, especially if you're trying to incorporate it with a vendor, right? Like… But otherwise, I think that is kind of… I don't know, the friction point, which we're still working on anyways with the configuration, so, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 26:58 Well, it's on a POC, and it seems like it works for them, so…
**Tyler** 27:01 Yeah, yeah, yeah, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 27:03 Yeah.
**Tyler** 27:03 I do wish other people would chime in here, other than us maintainers, but… or developers, but yeah, I mean, I think that we can always provide a perspective, too, but yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 27:12 Yep.
**Tyler** 27:14 Okay, A little bit of a tangent, I guess, like, I'll… yeah, hopefully we can get some responses to Regan here. But otherwise, I'll plan on getting a release out, don't think there's any breaking changes going on in this release, so that's exciting, just a bunch of new, awesome features.
Nimrod, you did want to talk about this troubleshooting guide. Let's, move on to this. I'll start sharing my screen again.
**Nimrod Avni** 27:36 Yeah, I… did a quick, right up on… on the OpenTelemetry AIO website of… Basically, a guide, like, that's what… we had some, like, internal, internal documentation and CoreLogix about, like, issues that we encountered, and we wanted to, like… I think I spoke with Nikola, and I said, oh, maybe we should have something.
you know, public. And I really want to get, like, your feedback of, like, that's, like, stuff, like, recommendations and approaches that we take, stuff like configuration logging and, like, log levels, debug exporters, whatever, and there's also a section… of common issues. Right now, we had, like, common issues, like, issues that I don't know if we can… detect them… through Obi. So, like, one of them is the Node.js stuff that we encountered a couple times.
like, the custom signal, handling, and one of them is something to do with Click House, which I think is something that, Rafael, solved in some of his PR, like, some issue when it restarts Cliffhouse.
So, mainly, like, if you have any more, like, issues that you, like, encounter, and people commonly ask you, and it's something that, like, people can review this doc instead of… You know, needing to either debug or, approach, you know, approach us, and if you have any, like, other common stuff that you usually do, like, stuff that you check, I don't know, I thought of maybe having stuff with checking the, the, you know, BPF, like, with some BPF tools or stuff, like, checking the probes themselves, I don't know.
That's it.
I think it could be really good.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 29:37 Great work, man. Yeah. We definitely, I… sorry, I didn't… I know you were talking about this, I just, sort of missed the review on this PR, but I will take a look, for sure.
**Tyler** 29:51 Yeah, is it, yeah, for some reason, I don't EPF.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 29:56 I think we often… I think one thing I'm not sure in here, but I can propose a change if it's not. It's, like, people run into, like, permissions issues, and with a recent change.
For UPropes to require sysadmin, and some of our customers were surprised.
So we can flip that image as well.
People that were very successfully before, and I… I know one customer is particularly, I think they got forced by their cloud vendor to, upgrade the kernel.
And so once they do that, like, oh, it doesn't work anymore.
But there's a specific line you can look in the log saying, oh, you see this, then it means you're lacking this permission.
And things like that, so…
**Nimrod Avni** 30:44 Cool?
**Tyler** 30:44 Yeah, I think that sounds like a great addition. Nicola, if you could maybe, include that, that'd be great.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 30:49 Yeah, I… I am… I'm gonna review this, and…
**Tyler** 30:53 Yeah, sounds good.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 30:54 Thank you, Ranimrak. Great stuff.
**Nimrod Avni** 30:56 Thank you.
**Tyler** 30:59 Okay, cool.
We can, jump through and just take a look at what OpenPRs we have.
There's some stale ones that are kind of accumulating, so… I think that's just going to happen. So one of the things that is maybe starting off is we have the Grafana tempo and Docker tag. I thought there was a collector… yeah, collector contribib.
This looks like there was some issue that still needs to be tracked down, so these are still open. Still working on these, though.
Similar for the patch update, there's definitely some work to get this patch update, passing the CI, if I remember correctly. I was just taking a look at this a little while ago.
Yeah.
This is also the problem with bundling everything, is.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 31:42 You kind of…
**Tyler** 31:43 Don't know what is causing the… Failure, but Yeah, looks like it's going again. Okay.
**Mario Macias** 31:52 Yeah, I retrig… it was failing. I re-triggered it before the… before the meetings, or before this meeting, just to see if they pass, I can change. I don't know if they are so old.
that, I don't know if Renovate will keep updating the… the patches, or they are still also we need to remove and recreate again.
Not sure.
**Tyler** 32:18 But it'll… it'll… yeah, it'll update every single time.
So every time that it does one of these, like, repushes, here, it'll actually sync to make sure that there aren't any updates, and if there are, like.
some big updates, like a major version or something like that, it goes outside of the patches, it'll close this and open up another one. So, yeah, it's pretty smart about that kind of thing, yeah.
**Mario Macias** 32:40 Okay, nice, nice.
**Tyler** 32:42 Yeah… C.
**Mario Macias** 32:50 Yeah, maybe… maybe it's… oh, I think this was fixed by… by Rafael, Disco Mot TD stuff.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 33:01 Yeah, true.
**Rafael Roquetto** 33:04 This…
**Tyler** 33:10 What was that again?
Looks like Gilmod Tidy is failing here.
**Rafael Roquetto** 33:17 Yeah, I… I… I… Okay. Now, this already has the fix, this dash dash quiet.
It's something else. Because the fix that… the fix that I pushed was because, we're just doing git diff.
in general, without constraining to go… go the… go mud and go sun. So, and then, If you had anything else.
that was, showed up in this git diff, like, unstaged files, because we generated artifacts, like the eBPF files, this would fail. But in this case, it's there already, the fix, so it's something else.
**Tyler** 33:56 Yeah, it looks like somebody needs to just go in and actually do go mod tidy then, because the renovate sometimes isn't smart enough to figure that out, especially for cross… dependencies.
**Mario Macias** 34:05 Okay.
**Tyler** 34:07 You should have permissions, Raphael, to push directly to this branch, by the way, so you should be able to just do that.
**Rafael Roquetto** 34:17 Okay, I can have a look at it.
**Tyler** 34:19 Yeah, yeah, sounds good.
I… if that's all that is… it is, I… I think… That's actually great. I thought I saw that there was more issues to this earlier, but if that's just a GoModTidy issue, that's pretty easy to fix, yeah.
Yeah.
Okay.
Okay, and then, looks like maybe you kicked off the tempo one as well. Have you taken a look at this one, Mario?
**Mario Macias** 34:46 Nope.
**Tyler** 34:48 Okay.
**Mario Macias** 34:48 No.
Probably I re-triggered it, again, I mean, rebase and re-trigger and see if it passes, but okay, they are not passing.
So…
**Tyler** 34:58 Yeah, this one may have the error. I think this was… who knows, actually? It may be more at this point, but… I think that… I think the tempo one was very similar, if not the same thing as this, where it was actually, like, having issues Sending data, or sending… telemetry? I can't exactly remember what was causing that.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 35:20 Ew.
**Tyler** 35:21 Yeah, it's definitely missing something.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 35:24 Yeah, that might be a flaky test, but…
**Tyler** 35:29 Yeah, it could be a flaky test, but I definitely have seen this consistently failing something, if this isn't the one.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 35:40 Yeah, we need.
Plowed through this, find enough time to do this.
**Tyler** 35:45 Yeah.
Okay, yeah, just things that I need to take a look at. We can continue on here.
For… Oh, wait a minute, update and fix… yeah, this is… this is the thing I was thinking about.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 36:00 Yeah, yeah.
**Tyler** 36:01 Okay, so somebody has taken a look at it, and it just isn't… this wasn't passing for some reason.
**Mario Macias** 36:08 Yeah, there is… because there were so many broken changes in oats, it required changing many things, so yeah, I dedicated some hours A few weeks ago, but…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 36:23 Maybe this should be me, since I wrote most of these tests, okay?
**Tyler** 36:32 Yeah, it looks like… I see. Okay, yeah, because the test is looking for a particular… Values, and it's just not finding them in the response data, so maybe these have changed, or maybe they don't exist anymore.
Yo.
**Mario Macias** 36:46 It's… I think the problem was in the setup of the… the setup of the… of the… of the cluster, of the test cluster. So, yeah.
**Tyler** 36:58 Oh, okay.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 36:58 into it. I'll put it on my list.
**Tyler** 37:03 Okay, I think… Yeah, you've already… okay, so yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 37:06 Yes.
**Tyler** 37:06 Alright, yeah.
Okay, cool, this also is another update.
That… I just saw it get updated again this morning. It looks like it's still failing, though.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 37:24 It's pretty bad.
**Tyler** 37:25 Really doesn't like this one.
Python SQL metric.
**Rafael Roquetto** 37:38 Probably… So it looks like it's a true error.
**Mattia Meleleo** 37:40 a major version of Python?
**Tyler** 37:43 No.
**Mattia Meleleo** 37:44 What's the update here?
**Tyler** 37:46 it is… three… two… two minor versions, it looks like.
**Mattia Meleleo** 37:53 Oh, yeah, because we filter spans by command, so it will change the tests.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 37:59 That's right.
**Mattia Meleleo** 38:01 That's why it breaks.
**Tyler** 38:02 Okay. Okay.
Mattia, do you have, Oh, I don't know if you have permissions either.
Okay.
Hmm.
**Mattia Meleleo** 38:15 I can open another branch manually if I have to fix this, but you can assign this to me.
**Rafael Roquetto** 38:21 You're an approver, right? So you should have permissions.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 38:25 Dude.
**Mattia Meleleo** 38:25 Yeah. Pushed directly to this, though, I don't, I don't think he does.
**Tyler** 38:30 But… Alright.
If that's the case, then go for it.
**Rafael Roquetto** 38:35 But yeah. Because I managed to push forward to that other one.
**Tyler** 38:40 Okay, cool. Then, yeah, Matthi, then that should… that should be the case then.
**Mattia Meleleo** 38:44 Yep. Yep.
**Tyler** 38:47 Cool, alright.
Then… moving on here… Mark, you are working on a, capture hostname for GoSQL operations? Yeah. I don't know if this is ready to look at. Well, it's still draft, so probably not, but just maybe talk about it?
**Marc** 39:06 No, this is… I have another branch, and maybe I'm gonna close this, because the implementation is completely different.
**Tyler** 39:15 Because… okay.
**Marc** 39:16 Yeah, this, we discussed with Nicola, and it… it kind of work if, Yeah, if you don't restart… if you have… if you restart the application using… doing SQL operations, which is quite… useless. But now I… I managed to have an implementation working with MySQL, so every time there is a query, it's able to capture the host there.
But I'm battling with progress. It works different, so… yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 39:47 Cool.
**Tyler** 39:47 Yeah, I remember trying to write interpretation for this, and it's really hard, because there's multiple ways to set this up, but I'm guessing since we have access to the internals, it's a little bit easier, but yeah.
**Marc** 39:56 Yeah.
Yeah.
**Tyler** 39:59 Okay.
Well, we'll keep our eyes peeled for that one. Steven looks like he's working on MQTT Here, I don't think I… Steven on the call?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 40:09 No, Steven's away this week, but I can give an update.
Essentially, like, Steven's trying to implement MQTT and AMPQ as protocols detectors, so he started by producing an example that we can use using Python. I think he started initially with Go, but that's a bad idea, because we need to actually instrument the libraries.
**Tyler** 40:29 So.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 40:31 Yeah, so I think he's writing the first, the example, and I think he's just now working on parsing the protocol, but it's away this week, so we'll see some update next week.
**Tyler** 40:41 Yep.
Cool. Awesome. That's exciting. That's really exciting.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 40:45 Yeah, alright. AMPQ is big, so we should have more than just Capco.
**Tyler** 40:51 Yeah, right, exactly, so that's, I think… That's gonna be exciting, yeah.
Okay, cool. Uniform debug print messages for BBPF code. I think this is just CEPI, right?
**Giuseppe Ognibene | Coralogix** 41:03 Yep.
Yep. I didn't have time to update, but thanks for the comment.
I tried what Nikola advised me. It was really good, but I need to have some time to update it.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 41:19 Awesome.
**Tyler** 41:20 Okay.
Cool.
Yeah, sounds good. Well, yeah, we'll wait for the update then. Thanks for the… thanks for the update.
**Giuseppe Ognibene | Coralogix** 41:28 Exactly.
**Tyler** 41:30 Also, Mattia, you're working on a trace log correlation?
**Mattia Meleleo** 41:35 Yeah, I did some additional research on how to… to block, logging from… for target applications. And, basically, if we don't talk to, like, a shipper.
there are no LSM hooks for blocking this.
And, all the other ways I found were more dangerous than using VPF probe, write, user. So, I guess I will stick with that for now.
At least it's, it's behind the config flag.
Some, updates here. I implemented the PID filter, which seems to work.
I'm also writing an integration test for this, Yeah, so if you have any suggestion that I missed from last week, because I forgot everything, or almost everything, please write in the request so I can update it.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 42:38 Nice.
**Mattia Meleleo** 42:38 I guess I will, will push, an updated branch tomorrow.
**Rafael Roquetto** 42:43 So, what is the… no rhetorical question, just so I understand, what is the issue with, shipping our own logs, instead of messing with it, leaving the originals… the original logs and… alone, we just enrich the logs and ship it our own, it's… That doesn't work, or not preferred?
**Mattia Meleleo** 43:04 I don't think there is an issue with that. It's just a different implementation, and I think that the bigger counterargument to that is that you are taking responsibility of… Of, of doing this, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 43:21 Yeah, scalability, right? I mean, it's easier to scrape individual pods where they're standard out, rather than having everything go through OB and be shipped.
It will become the bottleneck, and then the question of how fast can you process that?
If you are responsible for every pod.
You know, large cluster, or large mode.
To get every log.
**Rafael Roquetto** 43:44 Let's see.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 43:45 But it's definitely an option, and we can add a new, like, once this lands, nothing stops us from adding old TLP login export, and see if that's… for certain customers, maybe that's feasible.
**Rafael Roquetto** 43:58 Okay, makes sense. Thanks.
**Florian Lehner** 44:01 Quick question on the PID filter.
As PIDs can be different in ports versus, the system and across different hosts, why filtering on the PID and not used, hotel infrastructure, the filtering processor in the next step?
So I…
**Mattia Meleleo** 44:25 It's not, like, a real PID filter, so I'm not filtering on… well, I am filtering on PID, but, it's based on some attributes, that, that we also use for filtering it, In the normal K-props.
So you can, you can filter by open port or executable path, and Yeah, that's the filter, basically.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 44:51 Just to choose which… because we like to choose which services we'd like to instrument, and then we're adding a second option to say, choose which services we should be collecting logs for.
We're doing this for, because…
**Florian Lehner** 45:04 I see your point, but…
**Rafael Roquetto** 45:06 So, sorry, the way it works is you don't usually specify a PID, You specify something else, like service name or any attributes, and then that gets resolved to a PID, a host PID in this case.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 45:19 And we find the correct tip based on even multiple layers of, containers and whatnot.
**Florian Lehner** 45:26 I think I get that point. I think it's more conflicting with how OTL process and sees data.
And… It duplicates, filtering techniques across different layers.
So if someone says, hey, I'm deploying OB with whatever filter for Chrome, or, anything, then… or we will do something. And then, if the data is pushed through an auto-collector pipeline with a process filter.
There will be a conflict, if these, will be not… or so.
There are different stages of filtering that might be not… obvious to some… some users, and I think it will… integrating with the rest of OTA hardware.
**Rafael Roquetto** 46:19 Is it possible to… pass that information back to Obi, because one of the reasons of this filtering is if we don't do that, that means we are, on the key probes, we are analyzing every single pro… every single process in the system, and that's… that's unfeasible, because that means we're gonna be… shipping… a lot of events from the eBPF layer to user space, and that's just, doesn't scale.
So, I see your point, I think it makes total sense, but we just need to take this other aspect of it into account. The least… the less events we ship from eBPF to user space, the better, because it derails very easily otherwise.
So, I don't know if that's possible.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 47:05 Maybe when we're an auto component, then… Collector component, then receiver.
I'm done… Maybe that can be synchronized.
**Florian Lehner** 47:16 Yeah, if you are a collective component, it should be… you should have access to this configuration, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 47:23 Maybe then…
**Florian Lehner** 47:24 But not in the current state of the firm, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 47:26 Right now.
**Rafael Roquetto** 47:29 I have a… sorry, go ahead, Nicola.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 47:31 Yeah, there's, like, some of the… if we… the filtering is critical, because if we don't… like, there's some even pre-default… predefined lists of stuff we want to avoid by default. So, for example, we want to avoid the auto collector.
as a… we don't instrument the auto-collector, because it just creates this endless loop of telemetry. Just… it… every send of AutoCollector is a new trace, and then that becomes a new send, and it just goes exponential and blows up.
So, there's definitely… we have a list of things we just don't.
Don't wanna touch.
**Rafael Roquetto** 48:11 I have, completely unrelated questions, but since you guys mentioned the auto collector component.
If we ever become one, What happens… to our, like, dependency tree. I don't have any experience with the AutoCollector component. Does it have to match the, whatever, hotel collector Dependence tree.
Assuming we're done with the current discussion, or how does it work?
**Florian Lehner** 48:33 I can just pick how we are doing it in eBPF profiling, and it's super simple. We implemented an API called New Factory.
And this new factory calls our complete setup of, of eBPF profiling, and with this new factory, we get a configuration from, hotel collector. So.
if you go into eBPF profile at the moment, and run make agent or a make in general, you get an executable that is independent of Autel, but with the package controller, we have implemented the API that is expected by the OTEL collector, that is also calling the same main, like, the main executable for eBPath Profiler, just from a different point, basically.
**Rafael Roquetto** 49:27 Hmm, so you have a sub-process.
some… Something like that, or…
**Florian Lehner** 49:32 Yeah, you can think about it like this, yeah.
**Rafael Roquetto** 49:35 Okay, Nicola?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 49:37 Yeah, so that was gonna be my question. Do you… when you embed yourself into… I haven't looked, unfortunately, but if you… when you add yourself as an auto component, does the auto component… launch the profiler as an executable, or… or does it… Required that it's a goal… mod, and it actually becomes part of the collector, and you just call the go function, essentially.
**Florian Lehner** 50:04 I, we are GoMod and GoFunction, so, if you look into OpenTelemetry, OpenTelemetry Collector Release.
Okay. There you see a manifest?
And in this manifest, the Gomote is referenced that we'll call it just a new factory.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 50:23 Okay.
**Florian Lehner** 50:23 So you're…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 50:24 is a function, right? So… And in that case, that means all the profiler dependencies must match what the dependencies are in the OTL collector. So if you use a.
**Tyler** 50:35 It doesn't always have to be.
**Florian Lehner** 50:36 No.
**Tyler** 50:37 So, a lot of the times, like, it is the case if you're trying to include yourself into, like, the main collector repository, because they only have a single module, but all the collector-contributor modules, I think, are better examples where each one of the components, like each receiver, each, like, processor, all that, they're all their own modules. So then your dependencies are isolated at that point, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 50:57 Oh, interesting. So how does it stitch it together? Does it just launch it as a… builds it and launches it? I…
**Tyler** 51:04 Yeah, usually it'll take all of those different modules, it'll build it into a single binary, but each one of the modules has its own dependency tree, essentially, so it'll all be resolved during the… it's just like, we could do the same thing here, like, we could have our own, you know, multiple… we do, actually… all our test servers are their own modules, so… If there were dependencies across those, then you could… you could just still build them into a single binary that way, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 51:27 Wow, that's pretty awesome.
**Rafael Roquetto** 51:29 Oh, that was.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 51:29 Possible.
**Tyler** 51:32 Yeah, it goes, pretty smart about that. I mean, there is… Package resolution, so if there are, conflicting packages, like, in conflicting versions, they will get upgraded, unless you specifically override those.
So say, like, your both packages depend on… like, gRPC, a particular version of gRPC.
if, you go and build the binary, like, the importer of whatever, like, that dependency, you know, since it's a transitive dependency, it'll use whatever the importer's, like, version is at that point. Unless you've explicitly said in, like, your GoMod file, like, you can restrict it that way, but, but that's a little bit… More detailed there, yeah.
**Rafael Roquetto** 52:18 So…
**Tyler** 52:19 Usually, usually it doesn't matter, but yeah.
**Rafael Roquetto** 52:22 So, just so I understand, if I… if we say we have an OB component, that depends on… CDWPF2, and then we have some other component sealed into OB, that depends on run C, that depends on CD into EBPF3. What happens?
**Tyler** 52:40 So those are different packages, because they're different major versions.
**Rafael Roquetto** 52:42 Okay.
**Tyler** 52:42 That won't…
**Rafael Roquetto** 52:43 I promise.
**Tyler** 52:43 But it's more like if you…
**Rafael Roquetto** 52:44 It's the same breeding, then.
**Tyler** 52:46 Oh, yeah. So, well, it's… yeah, so if you have the same major version, so it's like, you know, 2.1 versus, like, 2.5 or something like that, since Go uses semantic versioning, it assumes that those are going to be compatible, and it will use 2.5, it will use whatever the latest is, unless you explicitly say, like, for this package, downgrade in this specific instance.
**Rafael Roquetto** 53:04 Hmm.
**Tyler** 53:04 But yeah, it'll… it'll… it'll go through the highest of a major version, yeah.
**Rafael Roquetto** 53:09 Okay, and if it's a 0.something package, then…
**Tyler** 53:13 Same thing, too. Still go to the highest, okay. You still go to the highest, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 53:16 You can pinch individual sub-components, go mod to a specific version, essentially.
**Tyler** 53:22 Yeah, yeah.
And that's, that's only if you're, yeah, taking these, like.
dependencies like this and this transit of dependencies are the things it's trying to resolve. That's how it will resolve them, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 53:34 Nice.
**Tyler** 53:35 I mean, there's always, like… that's… I mean, that's… one of the reasons the collector actually doesn't use multiple Go modules, because it wants it to be explicit, and it was easier for them to, like, see it that way, and they're really worried about performance regressions there. Here, I think we're worried more about compatibility, is what we would be worried about, but… That's something that I think you can, you can work on.
On a case-by-case basis, especially. So, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 54:04 Very cool.
**Tyler** 54:08 Okay.
Let's see, there's only one more pull request open, it's to create a placeholder for, Sorry, trying to find my window to share again.
Create a placeholder for the meter provider configuration to match, declarative config…
**Mario Macias** 54:30 Yeah, the, the idea, basically, is merging two… issues. One is, as requested from David Ashpole and so many other people, to start, using the hotel declarity configuration. I think trying to implement everything from zero is… is not feasible, so I think we can get a progressive approach.
and start implementing few sections progress… progressively. The other part is that we will require some… currently, some features that are… or some configuration options that are currently global to OBI should be, handled by application.
For example, if users want to get a service… a service map from all the… all its services, and want to implement, want to provide service graph applications. Currently, it… they should instru… service graph metrics, sorry, they should instrument all the applications also for red metrics, which will not be feasible. So, for example.
this kind of per-application configuration options, I was thinking that in order to avoid having even more per-application configuration options, also allow adding it within this declarative configuration as OBI-specific, fields.
Like, these OE features.
**Tyler** 56:20 I think… I think I, hmm. So, so is the question about taking, like, filtering of particular, like.
interpretations or protocols into moving it into the meter provider section? Is that what the question is?
**Mario Macias** 56:33 Yes, well, yes, yes, but yes, into the meter provider, and later allow a meter provider per application.
So, we have a meter… a global meter provider, and then another meter provider per application. So, you can enable, or you can have either a global configuration using the declarative the hotel declarative configuration, and the other will be later, in a second point, allow providing… specify this per application.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 57:13 I think… I mean, we've already started down this path, there's just not everything is available I think in a specific configuration section. So, let's just say, for example, you want to say, I want to instrument all applications in this specific namespace, but for those applications, I only want metrics.
But this other namespace, I also want to get traces, or one or the other, and whatever.
**Mario Macias** 57:37 Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 57:38 So that is supported, but you can't go and say, oh yeah, but for this namespace.
For these metrics, I want to select just… I don't know, HTTP. I don't want SQL.
Which exists as an option.
But it's global.
**Mario Macias** 57:54 Yes, exactly.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 57:56 Yeah, so this rework, I guess what we want to get to is that all the global options, you can actually Make them with a declarative configuration, for a specific, like, subsections, so I say, we want to discover this services in this namespace.
And then for them, we wanna… generate HTTP metrics only.
**Mario Macias** 58:19 Yes, yes.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 58:22 So it's what we've already started with, but just go take it to the next level. So everything is, like, configurable.
the discovery.
And in the same time, make sure it matches the OTEL declarative configuration format.
**Mario Macias** 58:35 Yeah, exactly.
**Tyler** 58:39 Okay, I'll have to take a closer look.
here, I don't think I fully understand yet, but we're running pretty close on time, so I don't wanna… get too much into it. But yeah, I'll take a look. Thanks for opening this up, Mario. That's, I think it's a great first step. We're headed… headed in that direction.
Minute left, anything else people wanted to bring up? Any announcements really quick before we end the meeting?
Cool. Alright, if not then, thanks everyone for joining. Good to see you all. Look forward to getting this next release out, and yeah, we'll keep chugging along. Thanks, everyone.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 59:19 Talk to you later. Bye. Thank you, bye.
