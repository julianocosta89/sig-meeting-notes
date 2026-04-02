SIG: eBPF instrumentation
Date: 2026-04-01
Duration: 39 minutes
Zoom Recording URL: https://zoom.us/rec/share/fCz3M_USnN1dxW4QO3OY9v2Wcq99gPsJTxRpRml56PVQ_6HYoFdRwjXeNs2Dra_4.0mIvFk99nU3rTEUa
============================================================

## Zoom Recording Transcript

**Mario Macias** 00:45 Hello!
**Florian Lehner** 00:48 Hello, hello.
**Mario Macias** 01:00 Hi, Raphael.
Hi, Nicola.
**Rafael Roquetto** 01:05 Enjoying.
**Mario Macias** 01:07 is going well.
**Rafael Roquetto** 01:13 It's gonna be a long weekend. That's good.
**Tyler** 01:43 Hey.
**Mike Dame** 01:46 Hello?
**Tyler** 01:49 How y'all doin'?
**Mike Dame** 01:53 Good.
**Nikola Grcevski @ Grafana / OpenTelemetry** 01:54 Mike.
You have no beard.
**Mike Dame** 01:59 Yeah, it's it's time to let it go.
**Nikola Grcevski @ Grafana / OpenTelemetry** 02:02 Okay, cool. I can see your face now, I know what you look like.
**Mike Dame** 02:08 Now I actually match my, profile picture. So, I should've… I should have changed my profile picture to one with the beard.
**Nikola Grcevski @ Grafana / OpenTelemetry** 02:15 Very, yeah.
**Mike Dame** 02:16 I keep confusing people.
**Rafael Roquetto** 02:19 Either you're next.
**Tyler** 02:24 Maybe, yeah, I don't know. I don't know. Stay tuned for next week.
Yeah, cool. Okay, so it looks like we're about 2 minutes in. We've got a pretty good quorum, so we could probably jump in here in just a second. I'm gonna start sharing my screen.
If you haven't yet, please go ahead and add your name to the attendees list, and if you have agenda items you wanted to talk about, please go ahead and add those as well, and yeah, let's jump in here.
Okay.
Well, okay, cool, yeah, so, I guess, welcome back to people that were at KubeCon, and I guess we want to talk a little bit about that today, but yeah, looks like I was reviewing some of the meeting dust from last week. You guys were doing… you guys just don't stop, man, you just keep going. It's really impressive. So yeah, this is… this is great. First up, Mattia, you wanted to ask about the next release?
**Mattia Meleleo** 03:27 Yeah, because we have a couple of bugs that are currently fixed in main, and we were wondering when we would have a next release.
**Tyler** 03:37 Yeah, great question. I had the same question. Yeah, I think… I think, actually, I'd like to get that out, like, today, or maybe tomorrow, if there's no opposition to that. The, V07… Zero… Milestone has a lot, like you said, a bunch of bug fixes, but there's actually, I think, enough features here, to… to warrant the… the minor version update. I was looking through this, there's a hundred and… 190 different things we've got merged. So yeah, I definitely think it's worth getting out. I guess the only open question is, is there anything that's pending that people want to address?
I think, taking a look at this really quick, this upgrade here, Mario has a pull request to try to address this.
**Mattia Meleleo** 04:28 That one is currently blocked, because, there is, So there is a regression in psyllium AVPF 0.21.0.
And there is a PR, which is sort of ready. There is some, like, tests, failing.
But it's blocked, yeah. They will release a patch, but it's not ready yet.
**Tyler** 04:52 I see. Okay, so the takeaway on that, Mattia, is that we need to pull that upgrade out of this upgrade, and then move forward without it?
**Mattia Meleleo** 05:00 Yeah, yeah.
**Tyler** 05:01 Okay. Is Mario.
**Mario Macias** 05:02 Okay.
**Tyler** 05:03 Okay, yeah.
**Mario Macias** 05:04 Yes, I'm here.
Yes, I, I, today, I… I updated with… together with others, but yeah, tests are failing, I haven't checked what's going on, but probably I will wait until this regression is fixed and… and released.
**Tyler** 05:18 Yeah, okay.
Well, perfect. If that's the case, I will wait on your, update to this. Let's try to get this merged, and then I'll add this to the milestone so we can get the rest of the go.
Dependencies updated, so, yeah.
Cool, anything else? We can talk about PRs, I guess, here in just a second, but, like… Anything off the top of people's heads that have blockers they want to get into this next release that we should… should gate on?
I don't think anything in this is actually blocking, it's more just tracking things, so, if you think otherwise.
Definitely not this, I thought. Okay, if you think otherwise, then, yeah, please let me know and I'll wait on one of these.
To actually get resolved.
**Nikola Grcevski @ Grafana / OpenTelemetry** 06:04 No, nothing from my side. I think it… I think we have a lot of new stuff, so I think it's good to release.
Yeah.
Cool.
**Stephen Lang** 06:13 Tyler, do you have everything you need for the automated image, building and release this time? Because there was a few issues last time, right?
**Tyler** 06:24 No, that was actually 05, if I remember correctly.
**Stephen Lang** 06:28 Okay, we're older than 06.
**Tyler** 06:31 Yeah, it actually went off without a hitch. Okay, great. It's motivating me to want to switch other projects to use our same tooling, actually, so, yeah.
**Stephen Lang** 06:39 Okay, no, that's all good then.
**Tyler** 06:41 Yeah, this one is going to include the, the bill of materials stuff, hopefully. That is, I guess, one thing that I haven't tested, so that'll go out. The image signing, that stuff should still work just the same, though. Yeah.
But yeah, thanks for asking.
Yeah.
Okay, on that note, I will take this as an action item. I will wait on, Mario, but I'm guessing probably later today, or maybe even, tomorrow at the latest, get this rolled out.
Okay, cool, moving on. Nikola, you want to talk about, a KubeCon recap, and just talk about OB.
**Nikola Grcevski @ Grafana / OpenTelemetry** 07:24 Yeah, yeah, I just wanted to kind of say a few things that, those wholly discussions, with the OTO community as well, the talk we gave on, OB and DNS went really well. It was a lot of attendance, a lot of interest.
And based on the feedback, I sort of have two things that I… it was my realization after talking to many people. First is that, a lawnmower people are seeing OB as sort of like a complement to the OTOL SDKs.
And… And that is, it's great, because, for example, we're able to do now, DNS, right? And it's really hard to get DNS data for… from SDKs. And then we have network support, so people were interested. I think we have an issue open by, yeah.
Antonio? Yeah. About, putting network flows as part of traces and so on, similar to DNS, so kind of get both network and application observability in the same sort of thing, so people have a lot of ideas of how we can improve this.
But also, for example, GenAI support. That's the first SDK out there now that supports the Gen AI spec to the OTEL standards. And so, how do we fit that in with existing SDKs? Can we augment the signals and make more of these metrics that are sort of unique to OB?
Or implemented in OB, be sort of complementer with the SDK instrumentation.
People are super excited, Mattia, I wanted to say about the trace law correlation, 3. You do what, exactly, and when we explain how we do it, and how it works, they're, like, mind-blown, so… That leads me to the second point. We do a lot of cool stuff, but none of this is publicized, so we need to step up our game to kind of spread the word about all the things the project does that can help with the rest of the OTEL ecosystem. That's currently implemented, where we sort of know about it, but nobody else does.
And, yeah. So, which means more blog posts, more talking, across the SIGs, and bringing this stuff forward.
Yeah, also a lot of excitement about the hotel, profiles and traces working together, so… it was all great. I mean, it's just… Not many people knew all the cool stuff we do.
So… there was a lot of comments, I was like, oh, I… I actually don't know what OB does.
And, so we need to change that somehow.
I don't know, I know Robert and Tyler are also there, and Florian, so…
**Tyler** 10:18 Yeah, I think you got the highlights. Yeah, Mattia, I want to second the whole logs thing. That was blowing people's minds, especially the collector SIG. They were kind of like… I was talking to them a lot about trying to get the collector, or Obi and the Collector, and when I pointed out that we do this, they were like.
wait, so, like, the… you could just have the collector scrape those logs, and it's already gonna be, like, correlated? And I was like, yeah. And they're like, that's kind of incredible. So, yeah, it's definitely something they're very, very excited about.
But yeah, on that note, I think it's just more about, like, getting it out there. People were definitely excited to ask us about when it's gonna be stable. That was definitely something that people asked at Nicholas Talk as well.
we've told the GC and the broader community that we're gonna get it out this year, so… quite motivated to make that happen, and I think all of you are as well, so, like, yeah, pretty excited. I think that that's just gonna help with that momentum, and Yeah, I think also similar to what Nicholas is saying, is that, like, there was just a lot of… not knowing things about Ovi that were already there that are amazing, so, yeah.
Yeah, I mean, actually, one of the takeaways that I did have was we had a conversation with the, isovalent and, like, psyllium folks, right?
And they… they weren't even aware of our, like, trace context correlation stuff, that we were doing with their library. So, yeah, I mean, like, it's… it's kind of incredible, that what we're doing here. They… they gave us a congratulations and said that it was pretty impressive. So, yeah, just a… Pat on the shoulder for folks.
**Nikola Grcevski @ Grafana / OpenTelemetry** 11:50 Beautiful.
**Tyler** 11:53 Robert, I don't know if you had other takeaways.
**Pellared** 11:57 Everything captures pretty well everything.
**Tyler** 12:01 Yeah.
Yeah, great work. I'm definitely happy to facilitate more, of the communication side of things and, like, making sure this is going good. I think I think there's a blog posts on just those features that we just talked about, I think the log correlation one would be great, if, Mattia, if you're looking for something like that, but yeah.
**Matia, you're asking about the… Recordings, I don't think so, I've been checking, yeah, but… Nikola Grcevski @ Grafana / OpenTelemetry** 12:27 Yeah, a week or two, yeah.
**Mattia Meleleo** 12:30 Just posted, I'm… I'm interested.
**Tyler** 12:34 Yeah, absolutely, yeah.
Cool.
Okay, well, I think with that, we could jump back in here.
start sharing again. I wanted to go through and just kind of get an update, and maybe we could also double-check if there's anything missing before this next, release.
And go through some of the open pull requests. I think I was taking a look before it looked… Like, a lot of dependency updates, so… Nothing too, blocking here.
The first two are… drafts. One is by Nikola for the use protocol detector to unhandled GO request. I'm guessing this is just still a work in progress? Yes. Yep.
**Nikola Grcevski @ Grafana / OpenTelemetry** 13:18 Yeah, I'm gonna work on that this week. I've cleared up everything else, so I'm gonna pick this up, probably close that one, and start making smaller, incremental pull requests to bring up, the Go support unequal with the rest of it, because I'm quite keen on getting the payload extraction, everything else working, so… Yeah.
**Tyler** 13:44 Yeah, awesome. Okay.
**Cool. Yeah, I'm really excited about this one as well. We talked a little bit about this person. It's definitely… Gonna be awesome Okay, next up, fix the OB Java agent build on macOS. I can't remember… Nikola Grcevski @ Grafana / OpenTelemetry** 13:59 Yeah, this is Andre.
**Tyler** 14:01 Okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 14:02 But, yeah… I don't know, has somebody tried it? Does it not work for macOS?
I think the fix is probably not quite there, I don't know.
**Giuseppe Ognibene | Coralogix** 14:15 I don't know if it's related, but I was trying to build the Dogger image for AMD on a Lima machine, and it was failing.
But I… I didn't see the issue, so I don't know if… Yeah, it was filling the build griddle, yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 14:37 Yeah… Yeah, this… this actually broke when… I removed the last dependency we had.
So we had dependency on GNA, it was easier to implement the native support.
But then I found that I had some class order issues on some programs on JDK8, which is quite old, but a lot of people still use it. So… I moved all the code to pure JNI, which is now a lot more… kind of… verbose, but at the same time, I was able to get fine-grained control of.
The class loaders.
And I obviously tested only in Linux.
And maybe some architecture thing is not quite… Right there.
I'll take a look. JNA does a lot of the build.
Nastiness, all kind of… On its own, and that's the beauty of it, but… Yeah, I can take a look. I have to find a Mac machine, but I'll have some… some old ones that I can maybe try this on.
**Tyler** 15:53 Yeah, are there other, people familiar with Java that are on Mac on the call that could help here?
**Stephen Lang** 16:00 I could try.
**Tyler** 16:03 Yeah, yeah, because I also would have to find some sort of VM for a Mac or something like that, but yeah, if you have that, maybe, Steven, if you could just actually verify if it's possible to build, or failure modes, something like that, that'd be great, yeah.
**Stephen Lang** 16:16 Yeah, Nicola, I can catch up with you.
**Nikola Grcevski @ Grafana / OpenTelemetry** 16:18 Yeah, yeah.
Boop.
**Tyler** 16:21 Cool. Okay.
Okay, next up, EPF proposal resize EPF maps at configuration time. This…
**Giuseppe Ognibene | Coralogix** 16:31 It's mine.
**Tyler** 16:33 Yeah.
**Giuseppe Ognibene | Coralogix** 16:33 there is only a filling test, which is the creation of the zip file. I didn't rerun it. I thought that it was useless, but, not sure.
**Tyler** 16:46 Hmm.
**Nikola Grcevski @ Grafana / OpenTelemetry** 16:47 Yeah, probably, just, we need to rerun it.
**Tyler** 16:51 Yeah, yeah, that definitely… Nikola Grcevski @ Grafana / OpenTelemetry 16:52 Yeah. Okay.
**Giuseppe Ognibene | Coralogix** 16:53 Okay.
**Tyler** 16:56 Okay, cool. But other than that, I think this looks, ready to verge once that passes, right?
**Nikola Grcevski @ Grafana / OpenTelemetry** 17:01 Yeah.
**Tyler** 17:02 Okay.
Cool.
Awesome, yeah, this is great.
Then, if that's the case, actually, let's add this, make sure I don't… Forget this and the milestone.
Okay.
Cool. Alright, Configv2, this is something I've been getting feedback on, I've got a lot of great feedback on it, so I'm still iterating on it.
I plan to get back to this probably later this week, or maybe next week, but this is kind of the big thing for that stabilization effort, so I really want to get back to it. So, yeah, top of my list.
Cool.
Next up is this, Kafka dependency stuff. This is… I don't think it's blocking, it just needs, I think this needs some more… Investigation, definitely some… something's breaking here, so I think we need to take a look closer to it, but otherwise, I think it's just… Is, not a top priority, so yeah.
Cool. Alright, is… I think Nimron might be on, if I saw it correctly.
**Nikola Grcevski @ Grafana / OpenTelemetry** 18:05 No.
**Tyler** 18:06 No, okay. I don't know if we have an update on this, because I know he was working with Oren on this.
**Mmm… Nikola Grcevski @ Grafana / OpenTelemetry** 18:14 So Pierre's approved. I don't know if it's missing… oh, Mattia approved it.
**Mattia Meleleo** 18:17 I think I proved that earlier, but I left then some more comments.
**Tyler** 18:29 Yeah, okay. Yeah, it looks like this just needs some… yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 18:32 Yeah. I had a question here. Would it be easier to just, split this in two parts? One is the user space, one then the VP of space, or do we need both at the same time? Might be.
You know what I mean? First get the… just the regular TCP buffers being parsed, and detect the protocol, and then… Then add the VPF side?
I haven't looked at it.
**Mattia Meleleo** 19:02 I'm not sure it's, convenient, because it's already everything implemented, so it would be more work to, to… Nikola Grcevski @ Grafana / OpenTelemetry 19:11 Okay.
**Mattia Meleleo** 19:11 split it.
**Tyler** 19:13 Hmm.
**Nikola Grcevski @ Grafana / OpenTelemetry** 19:14 I see, okay.
Alright, fair enough.
I haven't looked at it yet, I don't know.
**Tyler** 19:23 Yeah, I think this… it may just also need some… I don't know when the last time Oren was able to… Nikola Grcevski @ Grafana / OpenTelemetry 19:30 I think it's been a day or two or something.
**Tyler** 19:32 I think it might be longer than that, even. 2 days. Okay, yeah, no, I took it back. Cool, okay.
Yeah, so I think it just needs some iteration, then. Okay, no worries.
**Nikola Grcevski @ Grafana / OpenTelemetry** 19:44 Ms. Rafael, you put some comments in there as well, because I see you on the… And, Giuseppe, as well?
**Giuseppe Ognibene | Coralogix** 19:53 And mine was… It's more common.
**Rafael Roquetto** 19:58 Yeah, mine was, related to the large buffer API.
Yep.
**Nikola Grcevski @ Grafana / OpenTelemetry** 20:09 Oh, by the way, speaking of large buffers, we don't support them on HTTP2, right? This is something we need to add at some point.
That would…
**Mattia Meleleo** 20:18 Currently don't have those.
**Nikola Grcevski @ Grafana / OpenTelemetry** 20:21 Yeah.
It's the last one of those that we don't support.
And I was worried a little bit, because when I was working on the, Anthropic support, apparently they use HTTP2 if it supports it, but… Maybe that was… false information, because when I tried, it did regular HTTP from the SDK example I tried, but… Yeah, so payload extraction would not work if a service does support HTTP2, And so, probably a good idea to add that.
**Tyler** 21:00 Yeah, that sounds good.
**Nikola Grcevski @ Grafana / OpenTelemetry** 21:01 Hardy would be, yeah.
**Tyler** 21:02 Do we have an issue tracking it, at least?
**Nikola Grcevski @ Grafana / OpenTelemetry** 21:05 No, no, it's on my list to edit, but yeah, I want to create a quick one, then.
I actually tried instrumenting the Claude binary itself, that didn't go.
Work, actually, they've obfuscated a lot of it.
The strip symbols, we… it's kind of even hard to tell what is built in. I think Rafael and I were… maybe you're thinking Zig or Rust. It seems to have, like, node interpreter built into it, so at least some parts of the node components. Those actually have the symbols.
But there's no TLS.
hook, so we can hook into the SSL calls they make.
**Rafael Roquetto** 21:51 Well, the good news is that apparently the cloud code source has been leaked.
Maybe have a look.
**Nikola Grcevski @ Grafana / OpenTelemetry** 22:02 Yeah, it's kind of interesting, like, I… it's… I've never seen a binary that's partially strict, so it's like, some parts had symbols, But… the important bits were stripped completely. I did see the SSL code in there. I mean, I disassembled it, and I found all the AES, and… added checks they're doing for the encryption and so on, but there's nowhere for us to put the probes. Supposedly, it uses boring SSL, but… which we support, however… There's no… There's no symbols to add the hooks in.
Dns, we do catch it, though, so DNS, I can see they're sending data to Datadog every time you use it, so that's something you should all know.
Yeah.
Yeah.
**Tyler** 22:55 That's pretty funny.
Okay.
Yeah, I've added a… it has an action item to… to add the issue, but yeah, good… good thing to bring up. We'll… Need to keep track of that.
Okay Alright, where are we at? So next up… There's a… yeah, this isn't worth reviewing, still just investigating this, there was just some, like… there was a to-do, and I was working on it, but not worth talking about.
Next up… Mario, you also have a draft PR for selectively replacing tracing programs if the system, supports them? It's a work in progress, I didn't know if you wanted to talk about this, or…
**Mario Macias** 23:41 It's in super early stage, so just forget about it, yeah.
**Tyler** 23:47 Okay, cool.
Next up, Giuseppe, you want to talk about, CheckOS support? I think I was looking at this one this morning.
**Giuseppe Ognibene | Coralogix** 23:54 I need… I need to work on that.
It started as a simple to-do, and then I got a lot of comments, so I need to…
**Tyler** 24:05 Yeah. Yeah, fair enough. Okay.
Cool. Then next up is, dependency for Starlit to V1. I don't know this one.
Yeah, okay.
**Mattia Meleleo** 24:20 I think this breaks some GraphQL stuff.
**Tyler** 24:25 Oh, huh.
**Mattia Meleleo** 24:25 Look into that.
**Tyler** 24:33 Oh, interesting.
Okay, so it's a Python dependency that's breaking it?
**Mattia Meleleo** 24:37 Yep.
**Tyler** 24:39 Alright.
I mean, that is a pretty big jump in versions, so that kind of makes sense.
Yeah, I think we should take a look, and then, if this isn't supported, we can probably close it, but okay, not an important thing.
**Nikola Grcevski @ Grafana / OpenTelemetry** 24:52 Yeah, probably a newer version of the library we don't quite support, or something.
**Tyler** 24:57 Yeah, I think that, or, it's a transitive dependency, and so maybe.
**Nikola Grcevski @ Grafana / OpenTelemetry** 25:02 He, like…
**Tyler** 25:03 It has, like, API breaker changes. Yeah, I'm guessing that might also be, given this big jump here, so… Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 25:12 Right on this.
Yes, it's probably just broke, unbuilt.
**Tyler** 25:16 Right, right, yeah.
So, yeah, just investigation.
This update go is superseded by the PR we saw from, Mario earlier, so this is probably one that we can close after Mario gets, the…
**Mario Macias** 25:29 Yeah, but I'm not sure if this update go is just the minor, or the patch.
**Tyler** 25:38 Yeah.
**Mario Macias** 25:38 No, okay. No, because I saw your concern about updating to Go 126, violating our versioning rules, so maybe we can close my PRs.
**Tyler** 25:51 These, these two, yeah, okay.
**Mario Macias** 25:54 Yeah.
**Tyler** 25:55 Yeah, okay, yeah, sounds good, I can… I can close them if you want, yeah.
**Mario Macias** 26:00 Okay.
**Tyler** 26:02 Oh, oops.
Sorry, a little slow.
**Mario Macias** 26:11 I can… I can close it and write the explanation in the background, so you don't have to waste time.
**Tyler** 26:16 Thank you, appreciate it. Okay, perfect.
Yeah, this is, I think, more of the dependencies. This is, I think, more in your superseding with this one, this GoMod direct dependencies, is what I was talking about, so, yeah.
**There's also this… update Go Major, which I haven't taken a look at, but it's, rare that we actually want to do this, for the same reason as the other ones, where you're going to have API breaking changes across these, which… I'm guessing is happening here. Actually, this may… Okay, this just needs… Nikola Grcevski @ Grafana / OpenTelemetry** 26:44 zone.
**Tyler** 26:45 Yeah, it's almost there, yeah.
So, maybe worth taking a look at. Yeah, interesting, the Mongo one as well.
Okay, yeah, so, worth taking a look at. If, maintainers on the call want to take a look, please do so afterwards. I'm happy to take a look as well.
Next up is this fixed coverage data report. I know, Mario, you're still working on this one, just based on looking at it earlier. It seems like, there's some issues with the coverage. I didn't know if there's anything else you wanted to mention here.
**Mario Macias** 27:12 Yeah, I thought that it could… be the… I thought it could be the… the… the GoCoverage script overwriting the different reports, but no, it seems all the… all the reports are sent So I think this… this… this PR is useless. All the… all the reports are sent, but it's just, like, some reports… report zero coverage data, so probably there is something… we still need to fix, not… not here at the code overage report, at the GitHub option, but at the way it's… tests, or coverage data is generated in the makefile. I need to investigate a bit more.
**Tyler** 28:02 Yeah, we've definitely had problems with this in the past, as well in the Go, SIG, trying to go across modules or across packages to do, like, coverage reporting, but, the modern Go tooling got a lot better at this, so yeah, more and more.
**Mario Macias** 28:14 investigation.
**Tyler** 28:14 David, like you said, so, yeah.
**Mario Macias** 28:18 Okay.
**Tyler** 28:18 Okay, yeah, I can… if you want me to take a look as well, go ahead and ping me, and I'm happy to take a look, after.
**Mario Macias** 28:25 Okay.
**Tyler** 28:25 as well, yeah.
**Mario Macias** 28:26 Okay.
**Tyler** 28:29 Okay, cool.
Next up is dependency updates, This one probably needs to get merged.
Prior to the release, looks like Mattia's already approved, what's the only thing?
Just that CI.
Okay.
Yeah, I don't know why that would cause this. Okay, let's…
**Mattia Meleleo** 28:57 Which one is this?
**Nikola Grcevski @ Grafana / OpenTelemetry** 28:59 Ciao.
**Mattia Meleleo** 29:01 I think I started this test, like, 2 times, but it's always failing. I approved because I wanted to merge right away, but I think it's failing, Consistently.
**Nikola Grcevski @ Grafana / OpenTelemetry** 29:12 But it's failing Java Kafka, and this is…
**Tyler** 29:15 Yeah, this is… Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 29:17 Weird.
**Mattia Meleleo** 29:19 No.
Let's just restart it another time. Maybe this is the right one.
**Tyler** 29:27 Hmm. Did you just do that today? Have you restarted it a few times, is what you're saying? Or has it been over multiple days?
**Mattia Meleleo** 29:34 It's like, yesterday, or two days ago, I can't remember.
**Tyler** 29:38 Huh, okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 29:39 Yeah, it's number 5 on the run there.
I also got a report from somebody, I think, saying that Java Kafka is kind of flaky, so maybe that's just the natural flakiness of this. We need to investigate that.
It depends when Obi starts. Is it, like, new miss, I think, that we… we probably reverse the events or something, and we start missing them?
Yeah, that's my suspicion.
Because the report was that it's, like, depends when you run OB, you may… get the events, or you don't get them, and it persists forever. It's something like that.
So we're, like, unable to straighten up with the TCP events once we catch them in the opposite order or something.
**Tyler** 30:28 Yeah, I think I might have seen this, actually, in that other test I was working on with the Puma stuff.
**Nikola Grcevski @ Grafana / OpenTelemetry** 30:33 Yeah, it's possible. I can… yeah. I need to look into that, it's on my list.
**Tyler** 30:41 Okay.
Yeah, okay, more investigation needed.
But yeah, we'll, keep that in mind.
Similar for the Pydantic Core… Oh, man.
This should be… pretty straightforward.
**Wow, this is really not… Nikola Grcevski @ Grafana / OpenTelemetry** 31:01 Probably just the Python failed to build. That's what my guess is.
**Tyler** 31:06 Yeah, I think you're probably right. Okay.
Yep, okay, more investigation needed on that.
Same for the Docker.
These are both also, looks like they're failing, A few tests here.
So, yeah, just more.
Don't need to waste people's time on the call. Okay.
Mark, you wanted to add support for the memcached, protocol. I don't know if Mark's on the call, I thought I saw him.
**Nikola Grcevski @ Grafana / OpenTelemetry** 31:34 He's not, but I think we had some comments.
And he did address, I haven't reviewed after the… he changed the comment.
After he changed the code.
I just had one comment about… Making it more reliable, so it doesn't actually think it's memcached, and then we stop, processing the protocols, and then… Miss something else.
That was my main worry with the PR, but it seems like he did change it, so… Yeah, I will check again, and I think it should be good to go.
**Tyler** 32:11 Cool. Awesome.
**Nikola Grcevski @ Grafana / OpenTelemetry** 32:12 And we have MEM cash flow, so…
**Tyler** 32:15 Yeah, right? Perfect.
Okay, memcached, we talked about these other two, Mario's gonna close them. The Gomod, direct dependencies is the only other thing, and then this is the one that Mario's working to, pull out the psyllium, upgrade, so, yeah.
**Mario Macias** 32:34 Yeah, I updated, actually, all the dependencies. Maybe if you want to get every… to get the rest of updates merged, maybe we can exclude Silium, or just wait.
for it to get update… to… to get the regression fixed. And it was not urgent… an urgent PR, it was just, okay, I have a few… few minutes.
**Tyler** 33:02 Yeah, I gotcha.
Okay, then yeah, I can, I can take a look as well after this, but yeah, this is great. Okay, I can… Pull us through.
Okay, that's the end of the open PRs. Anything that stood out that we want to get merged in this next upcoming release?
Well, okay, if not, then we can come back here. I don't think there's anything else on the agenda, nope.
So I can stop sharing my screen here, and I can pause. Any other cool topics or things you want to talk about? Antonio, I see you joining the call, We were talking earlier about your, tracing, proposals as well, and, like, the, coverage on that, so… yeah, definitely something Nicholas, excited to bring in, and yeah, it was one of the recaps. I know you were also at… Kubecon, any other takeaways you had from, you know, people talking about OB, or your interactions with people around the Obi space?
**Antonio Jimenez** 34:03 No, sorry I couldn't make it earlier for this meeting. I know that you guys already talked, I will try to watch the recording, but the main goal is, like, I talked to Mario and to Matti on the first day, and we were talking briefly about that thing, about you guys have already trace context at L3 and L4 level, and then we… it was a coincidence that Nicola and Taylor was there, and we were talking about that. Why don't we add also spans into the application trace, which… with regard to network flows, so we can not only draw the application flow, but also the network one.
And I think it's really cool. I also asked my mana if I can try to contribute to that project, so I… he gave me some permission, so I will try to learn more about the code.
with your expertise, help you… help you there. So I'm not saying I'm gonna do it because I don't have knowledge, but I'm gonna try to… to… to help you guys there as much as possible, and try to make sure it's moving.
So yeah, let me know how you want to address it, if you want to create, like, start by creating a small GitHub issues, and then we can address, maybe by protocols, or by scenarios, or by language, and then we can go from there.
**Nikola Grcevski @ Grafana / OpenTelemetry** 35:11 Yeah, that's great. Yeah, I wanted to say, I asked you about protocols, and then I thought about, so, the protocols… Currently, the way we do it in Anobi, if we do not recognize the protocol that two nodes are talking, or two machines are talking, we just don't report it.
let's say… right now, we still don't support AMQP, whatever, and if they're talking, we won't show anything, but… I think this is a good use case for the network traces, right? Because then, if you enable that network spans, then you'll see the communication, even though the protocol isn't supported, but we will actually see the traffic.
So I think it will… it will be good value, especially for end users trying this out, and they're saying, oh, I'm not seeing anything, they can turn this on, and then they'll be able to see.
**Mario Macias** 36:03 C.
**Nikola Grcevski @ Grafana / OpenTelemetry** 36:04 just plain TCP spans, or UDP, or whatever is happening between the… the two parties, right?
**Mario Macias** 36:12 Yeah, the only thing that we should be careful about I think is that, Currently, a network flow doesn't even… doesn't even set the limits of a connection, it's just a flow of bytes, so if you want, for example, to relate it with trace IDs, a single network flow may contain multiple traces… trace IDs. So, yeah, we just need to see how to provide this in a consistent way.
**Nikola Grcevski @ Grafana / OpenTelemetry** 36:48 Yeah. But…
**Mario Macias** 36:49 I think we can take this discussion. If you create the issue, we can discuss later.
**Nikola Grcevski @ Grafana / OpenTelemetry** 36:56 Give me a…
**Mario Macias** 36:58 Humane issue.
**Nikola Grcevski @ Grafana / OpenTelemetry** 36:59 Yeah, okay.
**Antonio Jimenez** 37:00 I put it in the docs, and let me say it here in the chat, but yeah, feel free to start any conversation there, or we can also open in a… on Slack, happy for doing that. You guys know more technically how it works. My… my end goal is, like, I know Cilio.
they have a product called Havel, and they are building that network topology. It's not based on application communication, it's based on network, and this is what we are trying to achieve also, and I think OVI is the correct place to do it, because by talking with Celian people and isoballant people, they are… they were interesting about that trace context, but they were not that interesting about using on their product. It's more like, okay, it's really cool.
**Mario Macias** 37:39 How do you guys.
**Antonio Jimenez** 37:40 Solve that main challenge, but… We have other security, policies, requirements, priorities.
**Mario Macias** 37:47 Okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 37:50 Yeah, cool, cool.
Yeah, I mean, some of the SDKs actually do provide some of this information, not in the same way, but if you… I think the Node.js SDK, when you run a trace, it will show you the TCP Connect, and they'll make an event, TCP Connect, for example, and things like that. It's more like, they're trying to make the, kind of add that kind of stance, so I think this will fit nicely. We just need to find a… the correct way to do it.
**Antonio Jimenez** 38:23 Muslim.
**Tyler** 38:26 Yeah, awesome. Well, cool. Thanks, Antonio, and thanks for opening that issue. Folks that are interested, please do check that out, yeah. So, yeah, we can keep progressing that, and also excited to see you here more, yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 38:38 Yeah.
**Tyler** 38:40 Okay, cool. Any other topics folks want to talk about?
If not, we can, end the meeting early here. Yeah, thanks to everyone for joining, good to see you all. A lot of great exciting things, let's keep that momentum going. Yeah, I'll see you all in a week's time, and, until then, bye.
**Nikola Grcevski @ Grafana / OpenTelemetry** 39:01 Bye.
