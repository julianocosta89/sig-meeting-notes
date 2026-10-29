SIG: eBPF Instrumentation
Date: 2026-10-28
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Gregor Zeitlinger** 00:49 Oh…
**Rafael Roquetto (Isovalent)** 00:53 Hi there.
**Tyler Yahn (Splunk)** 00:54 Hey, how's it going?
**Rafael Roquetto (Isovalent)** 00:58 Good, how are you guys going?
**Tyler Yahn (Splunk)** 01:01 Good.
**Mike Dame (Odigos)** 01:03 Good. Hey, guys.
**Tyler Yahn (Splunk)** 01:05 Hey.
Mike and, Rafael, are you guys gonna be at the Maintainer Summit?
**Rafael Roquetto (Isovalent)** 01:25 I will try to arrive at least around, like, 4PM, because I land around 3, so we'll see how it goes, but, I can promise to be there.
**Tyler Yahn (Splunk)** 01:36 Wait, on Sunday, or on Saturday?
**Rafael Roquetto (Isovalent)** 01:39 On Sunday, on Sunday. So…
**Tyler Yahn (Splunk)** 01:40 Oh, I don't.
**Rafael Roquetto (Isovalent)** 01:41 I will probably… Yeah, yeah. I don't know, I don't know what the airport is like, you know, if I'll be able to make it, but I'll try to… to get the end of it, but maybe not.
**Nikola Grcevski** 01:50 Airport's pretty good.
**Mike Dame (Odigos)** 01:52 Yeah.
**Nikola Grcevski** 01:52 Yeah.
**Mike Dame (Odigos)** 01:54 If I remember, it's not too far from, like, downtown Salt Lake City, so… I'm gonna be getting in on Saturday, so I should be able to… No reason I shouldn't be able to make the Maintainer Summit.
Oh, cool. I was able to register, we sorted that all out, I saw that the, Now, OTEL SIG maintainers count as CNCF maintainers, so that was… It's a recent change, which is awesome.
So, congrats, everyone. You are officially recognized by the CNCA.
**Nikola Grcevski** 02:22 Yes, yes.
**Mike Dame (Odigos)** 02:24 But yeah, that's really great, so… I was able to register.
**Tyler Yahn (Splunk)** 02:28 Nice.
**Nikola Grcevski** 02:30 I think Steven is getting an award. Did you mention that?
**Tyler Yahn (Splunk)** 02:35 I didn't know.
**Mike Dame (Odigos)** 02:36 I heard that, yes,
**Nikola Grcevski** 02:37 Daniel Lang is getting an award for, his contributions to Kubernetes. He's a Kubernetes maintainer.
**Tyler Yahn (Splunk)** 02:45 Nice.
**Nikola Grcevski** 02:46 Okay.
**Tyler Yahn (Splunk)** 02:47 Oh, cool.
Is he getting it at the maintainers?
**Nikola Grcevski** 02:50 Yep.
**Tyler Yahn (Splunk)** 02:50 I think.
**Nikola Grcevski** 02:51 I think so. I think it's… I think it's on the Sunday that he's getting the award.
**Rafael Roquetto (Isovalent)** 02:55 Yeah, it's at 4 or 4.30 PM, that's why I was trying to make it, but
**Nikola Grcevski** 03:00 You may make it, you may make it. I mean, the airport… I think the biggest challenge was that everybody just books the Ubers, and it takes about 15 minutes to get into yours, but…
**Mike Dame (Odigos)** 03:10 Yeah.
**Nikola Grcevski** 03:12 I like the airport a lot. It's super quiet, nice, easy to find your way around, yeah.
**Tyler Yahn (Splunk)** 03:22 Well, cool.
Yeah, let's, let's jump in here and get started. If you haven't yet Add your name to the attendees list.
Man, we have a lot of… names that start with M.
Go ahead and add them there as well, and then if you have agenda items you wanted to talk about, go ahead and add them, and then, yeah, let's… I'll start sharing my screen.
So first off, I wanted to mention that today's the last day… I think it's the last day, Yeah, it is the 28th. Okay, for the GC elections, if you are… a member of standing, which means that you've just contributed to the project, over the past year, you should have access to vote in the, election. The election link's right here.
If you have issues with the Helios voting system, you can message, some of the Maralia from the GC or something like that, other GC members as well, they can… sort this out. There are some issues with, like, usernames that have capital letters in them.
tell me how I know. And, yeah, you can, you can get them sorted out by using an email instead. So, yeah, if you have issues, let somebody know. Otherwise, yeah, please try and, try and get, voting.
**Rafael Roquetto (Isovalent)** 04:41 Just a quick question. What happens if you don't vote? Is it mandatory, or can you just not vote?
**Tyler Yahn (Splunk)** 04:47 Yeah, yeah.
**Nikola Grcevski** 04:48 We cannot.
**Tyler Yahn (Splunk)** 04:48 vote. I mean.
**Nikola Grcevski** 04:49 You don't have to.
**Rafael Roquetto (Isovalent)** 04:50 Okay.
**Tyler Yahn (Splunk)** 04:51 Yeah. I mean, I know you're from Canada, but in the US, we take it, you know, very seriously, not being able to
**Rafael Roquetto (Isovalent)** 04:59 Fair enough.
**Tyler Yahn (Splunk)** 05:00 Yeah, no, there's not, like, a requirement, but we are at, like, a very low percentage right now, But I think it is still higher than we've had in the past. I think it's something like 300-something votes out of 800 right now, or over 800, so… we're less than half, but, yeah.
It… it's very easy, just to… just to drive it home. It's… you get 4 votes, there's, I think.
8 candidates. You can vote once, you can vote all the way to 4 times. Like, it's really, like, you can submit a vote with zero votes, actually, I think, even. So, like, yeah, it's more about just showing participation. So, it shouldn't take more than 5 minutes, yeah.
**Rafael Roquetto (Isovalent)** 05:40 Sounds good.
**Tyler Yahn (Splunk)** 05:41 Yeah.
**Rafael Roquetto (Isovalent)** 05:42 Thanks.
**Tyler Yahn (Splunk)** 05:42 Yep.
**Nikola Grcevski** 05:43 I'd like to say there's so many people in the community that do good work. I think it's unfair not to vote. In my opinion. I'm not saying you should vote, Rafael, but there's people here that put in a lot of time That are on the GC committee right now, so…
**Rafael Roquetto (Isovalent)** 05:58 Yeah, I was just asking, because I wanted to… if I was to vote, or if I am gonna vote, it has to be a con… I just don't want to vote for anyone. I need to know who I'm voting for, that's, That's the part.
**Nikola Grcevski** 06:09 Check them out, like, some of the people put in tons of work into our community here, so it's a way of recognizing.
**Tyler Yahn (Splunk)** 06:16 I'd be kind of surprised also if you didn't recognize a few names on the ballot.
**Nikola Grcevski** 06:20 Yeah.
**Tyler Yahn (Splunk)** 06:21 But, yeah, like, I mean… the top contributor to the project is up for election right now, so, I mean, like.
I don't know Trask, like, yeah, like,
**Nikola Grcevski** 06:30 You should not trash, at least.
**Tyler Yahn (Splunk)** 06:31 contrast. Yeah.
**Rafael Roquetto (Isovalent)** 06:33 Sounds good.
**Tyler Yahn (Splunk)** 06:33 Yeah, but I mean, there's also, if you wanted, Rafael, in that link I have, there is a, a link to the community page that has all of the bios.
For all of the people on the ballot, with, you know, pictures in case you recognize them via pictures, and, like, their pitch or their blurb as well, if you wanted to get a little bit more background on who these people are.
But yeah, it's all… should all be there in that link.
Okay, cool. Next up, I wanted to talk about the 1.0 release. It's coming out this Friday.
Super excited about that.
It's been a long time coming.
So, I think… I don't see any major blockers that have come up. I don't think there's any, thing that stands out. I did want to check in with people, though. One of the things that, like, I did have included in this Epic was having maintainers sign off.
I guess I already have it open. If… You would, please, Mattia's already on it, just… as a maintainer, as an approver as well, if you're… you wanted to as well, happy to have your input. But as a maintainer, just saying explicitly, that you sign off on the release, it'd be… good to document this. I'm hoping we can get all five, maintainers to actually do this.
It's, it's, I think just showing cohesiveness as well as just, you know, not having the implicit sign-off on that.
It is also your last chance, if you want to have big issues you wanted to, thanks, Rafael, to, sign off on, or to have issues, with the release to raise them. So, speak now or forever hold your peace kind of thing.
the plan for the release itself, I did want to go over this, I thought through this a little bit, but… so, we don't want to release everything that's on main. What I'm gonna do is I'm gonna branch, from… our second release candidate commit, it's gonna be a branch in the upstream repository that's, you know, the name doesn't matter too much, I just chose this name because that's what it is.
From there, I'm gonna create the release PR from that branch, for the 1.0. I'm gonna merge that into the release branch, and then tag on the release branch. I did check our CI. We are, you know, triggered by the release tag, not by the, you know, commits to that branch, so this should work. I've tried to validate it as much as I can.
We can always try to pivot if it doesn't.
But, yeah, so this should work. The only thing that I did catch that, like, we do want to do is that the telemetry schema is only published when main workflows are run, so the idea is to then, after the release is out, merge the release back into the main, just to clean it up.
I don't think it's super critical that the telemetry scheme is out, like, right when the release is out, but, you know, I would like to get it out before next week, so I'll try to get this merged on Friday as well.
But yeah, other than that, I don't… if people have issues with this release plan, I'd love to hear feedback on that as well. But if not, then yeah, I think that's… that's the plan. I'll try to get the, release PR up today so we can get it reviewed.
And then, don't plan on merging it until Friday.
On that note, as well, most of you on the call have seen this, but in case you haven't, there's also a blog post associated with the release. We've got it slated for Friday as well, but probably should have been Saturday. That's… I don't know. We'll coordinate with the docs people. But yeah, if you want, please take a look at this. This is just the announcement.
Any sort of feedback on this would be great.
And just, yeah, there's a lot of thanks in here, mostly to the people on this call, which I really appreciate all the hard work you've put in.
to getting us here, so yeah, I really appreciate it, and yeah, I… finish it by saying, like, we are kind of trying to keep this momentum going, so I'm also really excited about moving forward on this one.
Okay.
That's a lot of me talking for the 1.0. Any questions on the 1.0? Any issues?
Nikola's excited.
Okay.
Then back to business. This is, a cool idea I came up with, got inspiration from Nikola, which I'm sure came from 20 other sources, so I apologize if I'm… stealing your thunder, but the idea is, this cool idea where we could actually instrument OpenSSL, the library itself, so, like, the SO file, explicitly.
And do that using, Frida. So… I'm not an expert in Frida, and so I'm gonna, like, butcher this, just a heads up, but, like, Frida, in my world, is kind of like a monkey patcher. It's so much more, but, like, from my standpoint, like, what I'm using it as is a monkey patcher. It has C APIs, so you can call it, and you can essentially do… very similar things to what a U-Probe does, where it, will do a trampoline to actually User space code, though.
And the user space code that we can control to essentially, like, shoo in particular calls.
So what that means is that we can actually, monkey patch OpenSSL on startup, and say, like, anybody that actually wants to use OpenSSL for TLS, so they'll send it some sort of, you know, buffer, saying, like, hey, I want you to encrypt this, expecting a buffer back.
We can, you know, at that point.
step in and encode, or, you know, add whatever we need to to that trace parent header, into that request before it gets encrypted, meaning that, like, then we aren't, you know, left out in the cold on this one.
What this means is that, like, all of the, you know, you know, obviously, like, C libraries, a lot of them use this, C++, you know, big ones like Apache, all these sort of things, like, they will use OpenSSL.
To actually do these encryptions.
We can hook in free-to-Core, there's a lot of different ways, but I found a way to do it using PureGo, which means that we don't have to include Sego, in this, in this processing here, so this is, like, a PureGo ecosystem. For, just a caveat, for all of the… ecosystems that we support, which is Linux, AMD 64, and then ARM 64 as well. Like, there's more that could be supported, but you would probably need to include Cisco for those, just if we do want to, you know, move forward on this.
It does require that the user points to the SO file, so the linked shared object file, for free, for OpenSSL, because otherwise, like, we don't really know where it is or which one to use, is kind of the idea.
There is also another downside where, once it's been monkey patched, like, it doesn't, it's not possible until the application stops to un-monkey patch it.
So, like, that is a little bit of a issue if you wanted to, like, say, turn off Obi and, like, just get rid of it.
it doesn't completely clean itself up, but you, you know, what it does do is, like, the probes that I've written here, they… once OB's not there, there are essentially no ops. It's just that, like, that… that trampoline still exists within that code path, is kind of the call-out.
Yeah, the specifics are, you know, there's definitely a, a prototype I have.
That's, yeah, here we go.
linked here. You're welcome to take a look at it. It's… it's a little bit large, obviously, but, like, this is… this is kind of, like, the details of how you would actually achieve this. I have an example… I think there's an example in here.
If it's not in here, I can commit it, but Essentially, just using the OpenSSL CLI, yes.
This looks… this looks right.
Sorry, there it is. Yeah.
So, using the OpenSSL CLI, like, literally just calling out and saying, like, I want to make this call, it'll instrument this call.
this actually kind of relates to Nimrod's, short-lived thing, like, if you just do this without having some sort of, like, long-lived process, Obi has a hard time, like, finding, like, one-off instantiations of OpenSSL sClient, but, like.
running it this way with, like, a long-lived process, it has no problem instrumenting this, which is actually kind of cool. I imagine it can get fixed as well, but, like.
Yeah, so it's got a nice example here, worth playing with.
there's definitely trade-offs, because obviously this is moving beyond eBPF to do instrumentation at this point. I think it's extremely valuable, so I wanted to just bring this up.
And get feedback, from the group, and thoughts.
**Nikola Grcevski** 15:15 Yeah, I think it's great, but honestly, I'm maybe biased, but, I think we could expand this to… like, pretty much gives us TLS propagation for all languages that use LibSSL or OpenSSL.
Yeah, this… I mean, my… this came off from… I was looking at how BPF Time, this user space BPF tool, does things, and they use this heavily. I think another user is MeleBear, this company that lets you debug remotely your Kubernetes clusters. So, my biggest concern always was I wasn't able to figure out how to, had to communicate the data back, from the eBPF side to say what the trace ID should be, but then I clicked on that when I was in, at FOSE, this conference, of… open-source software in North America, and had a lot of time on my hands there. And, Yeah, I thought, well, we could just, perform a syscall, and just like we do in Java, for the Java agent, and get the trace ID back from theBPF side, and then… We should be able to inject, and I think it goes beyond the examples here. I mean, we can use the same approach to patch Node.js binary.
To actually patch their, calls through LiveSSL, this actually handles servers as well, like, or clients, such as, I don't know.NET uses LiveSSL.
They don't render it. Obviously, rust.
than Python.
Clients, they'll all be using.
Same stuff. So, I think this gives us… Pretty much everywhere. We have Regular context propagation will now work on TOS.
The only odd ones out will be, Probably Java, which you're already handling, I think. Yeah, yeah. Yeah, at least the sync client got out.
**Tyler Yahn (Splunk)** 17:21 Yeah, and I've got plans for a bunch more, but yeah. Yeah, there's definitely, I think, a lot of work we can do in Java that's separate, but like you said, like, yeah, we can handle that separate.
**Nikola Grcevski** 17:30 Yeah, that's separate, so this actually gives us full coverage of TLS.
And we can expand to HTTP2. I mean, this is easier, because it's easy to detect inside the handler from Frida, whether it's TLS, HTTP2 or HTTP1, so… Yeah.
Roll for it.
**Tyler Yahn (Splunk)** 17:53 Well, cool. Yeah, maybe, you know, obviously it's pretty new. I will… I'll try to clean up that PR, and I imagine it's going to be next week, or… If it's not next week, it'll be in, like, 4 weeks, sort of thing. I'll try to get it out and get people reviewing, but if you want to take a look at it, try and play around with it.
If you're excited about it, yeah, let me know. I'm happy to get some feedback on it. I think it's a cool idea. It's definitely expanding the scope of our, like, technology space that we're using here, but, like.
I… I think that, like, it's the functional value that we're bringing to the end user is definitely, like, really, really helpful, as Nikola has definitely talked about, and I think there's even more opportunities even than what we're thinking about. It's always the unknown unknowns, right?
So, yeah, please take a look.
**Nikola Grcevski** 18:42 I mean, there's also the other opportunity, I mean, I wrote a… I think a ZIG experiment, which did this with LD preload initially, because I wasn't when I was experimenting with this, but it's the same concept. Whatever you can do with Frida, you can actually do with LD preload, but it will require injecting, and it will only be done on application start.
So, for customers that may not be willing to give us permissions to patch their binary.
Maybe working with the old dill injector could be.
the way forward there.
**Tyler Yahn (Splunk)** 19:16 Yeah, good points.
Okay.
Cool. That's… I mean, I'm super excited.
Next up… Nikola, you wanted to talk about a wild issue.
**Nikola Grcevski** 19:34 Yeah, I didn't open an issue, that's a PR, essentially, but, actually, strangely enough, we found this in Grafana. Grafana server, does exec, but it doesn't do a fork.
So what this actually does is keeps the existing process ID, but replaces the binary under the covers from the Linux system.
So, from the time we actually discover the offsets to the time we, essentially attach the probes, the binary could be completely different.
So… This actually causes crashes.
So with this PR, I'm reworking some of the guts of how we discover stuff. I split it by commits, but essentially trying to make sure that we never Injecting the wrong binary, and we detect that we've injected in the wrong binary.
Or do we have a different binary now to actually redo the scan of processes for that.
I think there was some other issue opening. I couldn't find it, though.
Somebody complained that if you did this, we weren't instrumenting the child. We were instrumenting the parent.
And there were missing instrumentation. That is the same problem, except in that case, we survived. So the offsets, didn't crash the binary, but We instrumented the wrong binary, not the one that's exact.
So, with fork, it's easy, because it's a brand new PID, so we detect it, but when it's, I completely didn't miss this sort of edge case.
But we caught it in, actually testing Obi in Grafana at scale. They found that our managed Grafana instances were just crashing once in a while.
And, they eventually… somebody had enough time to look into it, and after a long investigation, it was like, oh, it's the CBPF thing, what the hell are you doing? And, yeah.
**Tyler Yahn (Splunk)** 21:36 So the…
**Rafael Roquetto (Isovalent)** 21:37 Switch.
**Tyler Yahn (Splunk)** 21:37 the solution here? You're just essentially looking Like, how do you detect a failure?
**Nikola Grcevski** 21:42 So, what I actually do is… there are a couple of places where we just assume there's always going to be the same binary. So, for example, we'll find information about this PID, and then later on, we'll just look up the inode number and the device.
And that could be completely different by the time you look one from the other. So I just went through the various places in the code where we do this, and make sure that it's always consistent. If you're gonna look it up, look it up once, get all the information rather than look at different places. And… You know how we do the proc pit and EXE to do the instrumentation? I found that I can actually go through proc pit File descriptor, and then passing the actual file descriptor.
**Tyler Yahn (Splunk)** 22:27 Oh.
**Nikola Grcevski** 22:28 And then… then I'm sure that the file descriptor of this new exec process will be different. Right.
that gives us a more stable path, and then I can check to see if the file descriptor actually matches to the one we're attaching, and I say, okay, then they match, therefore it's good to go. Instrument, attach the probes. Otherwise, don't do it.
and when I added the… I think in Watcher, that if the… when we walk the processes that we've already instrumented, and we actually see, oh, no, that's already been instrumented, I check to see if… I remember now, on the time we add something to the cache of all the instrumented processes, the device and INO number, and next time we scan them, we say, is this the same?
**Tyler Yahn (Splunk)** 23:17 Yeah.
**Nikola Grcevski** 23:17 is the same PID, but either device, and I know number is the same. If they haven't… if they have changed, I say, no, that's not the same process anymore. Delete it from the cache and let it get picked up.
And Mario found that I actually had the same bug in, dynamic bit selector, so… I'm about to push a change that fixes dynamically selector, because… I mean, just the PID being in the list is not sufficient. You have to check.
**Tyler Yahn (Splunk)** 23:42 Right.
**Nikola Grcevski** 23:42 You know, is this, is still something we want to instrument, so… It's a really nasty edge case, happens only during startup of applications, but I realize it's actually quite common. All the people that do… run script, and they, instead of running finally the command, they do exec the command, this is what happens. The shell actually takes over The pit is of the shell, but the binary gets replaced to be the binary of the process.
**Tyler Yahn (Splunk)** 24:13 Oh, okay. Yeah. Yeah, I use this all the time, starting up, like, a Linux, you know, Windows Manager or something like that, right? Like, you want it to do that so that when it crashes, the PID's actually invalid, right? Yeah. Yeah.
**Nikola Grcevski** 24:25 That's right. And the reason why we don't see this more often is because we have the delay on scanning, so we actually… and all the shell scripts kind of finish fast enough, so the process is… the right one is already up and running. Yeah. But if the shell actually took a little bit longer, then, We would… we would die.
**Tyler Yahn (Splunk)** 24:43 So all of the people's optimizations are actually hurting us, is what you're saying?
**Nikola Grcevski** 24:49 Well, I mean… I mean, we get it right most of the time. Otherwise, we'd have seen it long ago, but, Yeah. Yeah.
But it failed in Grafana, I think, once every week, at least. So…
**Tyler Yahn (Splunk)** 25:02 Oh, wow, okay.
**Nikola Grcevski** 25:02 We run a lot of instances, but once every week, we'll see an unexplained data.
Crash or illegal instruction, which is a symptom of us.
Wacky, so in other words, you'll be wacky.
**Tyler Yahn (Splunk)** 25:17 Okay. Well, yeah, I'll definitely, please, those on the call, take a look at this. That's an important bug, so let's, let's try to get that fixed. I guess speaking on that, maybe, like, I anticipate, just a heads up, like, probably getting another, like, 1.1 out.
right after KubeCon, so if you have other big things you wanted to get in, maybe, open issues to track them in the milestone, or open PRs now, and then we can try to get them in right after KubeCon, because we have a lot of stuff, believe it or not.
Stacked up, to release as well. So, yeah.
**Nikola Grcevski** 25:51 Okay.
**Tyler Yahn (Splunk)** 25:53 Cool.
Alright, I think with that, that's the end of the written agenda. Anybody have anything else? Any other topics? Any other cool projects?
If not, I guess we can end the meeting early here. Thanks, everyone, for joining, it was good seeing y'all.
And I'll, see you all next week.
**Rafael Roquetto (Isovalent)** 26:21 Alright, thank you guys, see you then.
**Nikola Grcevski** 26:23 Bye.
**Mattia Meleleo** 26:24 Bye-bye.
