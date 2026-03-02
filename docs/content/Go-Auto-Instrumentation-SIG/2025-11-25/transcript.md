SIG: Go Auto-Instrumentation SIG
Date: 2025-11-25
Duration: 25 minutes
Zoom Recording URL: https://zoom.us/rec/share/Bh77CXxp6eH5KYVK7G1AdkBEtw8iDg5J3ug2-t_O2I7S-Y0w2_V6jte8ez4M8qrZ.DApdJINPhTSY-Gva
============================================================

## Zoom Recording Transcript

**Rafael Roquetto** 01:12 Hi, Mike.
**Mike Dame** 01:15 Hey, how's it going?
**Rafael Roquetto** 01:17 Good, how are you?
**Mike Dame** 01:18 Good.
Oops.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 03:51 I guess Tyler's not here.
You know, so I wanna get started, and… Or wait a little bit.
**Mike Dame** 03:59 Anyone, try pinging up?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 04:02 Oh, here's Tyler.
**Mike Dame** 04:05 Yee.
**Tyler** 04:05 Hey! Sorry about being late.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 04:08 No worries.
**Tyler** 04:09 How are y'all doing?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 04:11 Yay, how are you?
**Tyler** 04:12 Doing well, yeah, doing well. Super busy on this short week, right?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 04:17 Yeah.
**Tyler** 04:18 It's one of those weeks, right? Yeah.
You come back and everybody wants everything done, and you have half the time, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 04:27 And people shopping like crazy.
**Tyler** 04:29 Yeah, that too, yeah.
Well, cool. We can jump in here. Let me, start sharing my screen. Welcome, everyone. If you haven't yet, please go ahead and add your name to the attendees list, and if you have, agenda items you want to talk about, please go ahead and add them there as well.
First up, Nicola, you wanted to talk about proposing, extension of the hotel demo with non-instrumented, applications that we can…
use OB, all this other great, beautiful goodness, that you've been working on lately?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 05:00 Yeah, so I was just a…
Asking here, wanted to kind of…
Put it out there, see if people thought this was a good idea or a bad idea.
But one of the issues with the OTEL demo is that it doesn't demo this project, neither does Robi or the operator, because all the applications are instrumented.
So… Maybe what we could do is just…
Add a couple of applications that are not instrumented, and then…
Add to the demo automatic instrumentation.
with the operator, using GoAutus Rotation for the Go applications, and…
Maybe install the OBDM set and pick a couple of them to the instrument there.
We'll likely have to do their work ourselves, my understanding is that I…
But, just wanted to hear an opinion.
**Tyler** 05:53 Yeah, I mean, I definitely would love if we could have some integration with the demo ecosystem in highlighting the value of these projects. Like, there's a lot of really great,
A lot of really great stuff there. I mean, there's also, like…
the, the injector could really even be leveraged here as well, which is not currently, right? Because, like, a lot of those instrumented ones with auto-instrumentation aren't there.
Yeah, I think that's a really good question. I would definitely be in favor of it. I don't know how this looks,
From, like, the demo side, there's a whole SIG, that's dedicated to the demo, if I'm not mistaken. It might be worth, like, asking…
Yeah, like, maybe even just, like, asking, like, how we can start to use this, like, because, yeah, I think it'd be great to show, especially in ecosystem, like you're talking about, where it's mixed, where there is native instrumentation, there's auto instrumentation, there's EDPF instrumentation, like, I think all of those above would be, like, great, just showing, like.
the whole ecosystem there. So, yeah, I…
I like the idea. I'm happy to also help contribute to that, if we can get a vision and a, you know, some work, defined.
**Mike Dame** 07:08 Yeah, I think it… I think it fits with the goal of the demo, too, and I'm sure that Austin and those people would…
be down for it if we can explain, like, the benefit, you know, we're not just adding uninstrumented apps, we're adding the apps, and plus the instrumentation, the daemon sets, and setting everything up, too, to show, how auto instrumentation works with manual instrumentation.
And that's a big part of, like, the OB donation and everything, too, was about trying to show users what is the recommended usage of auto instrumentation, what are some, you know, kind of…
standard… like, applications of it, so, it… I think that it…
makes total sense. The other option is… I know the hotel demo is… have… has a really big, like, fork, economy, or ecosystem, so that's always an option, is, you know, you can make your own fork of it, and then you add it to that, like, list of vendor forks that they have, but I think that that…
that's a lot of… a lot more work for us, too, and it also doesn't make sense because we are an open telemetry project, we shouldn't have to fork that OTEL project and do it. So that's the only, like, alternative that I could see as even some pushback, but yeah, I think if it's just a simple, uninstrumented app.
It should be no problem for them to let us add that and, like, make the case for the integration.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 08:32 Cool, thanks, I like your approach. I like your thoughts around how to approach the SIG to say, no, we're not adding on instrumented apps, but we're going to add on instrumented apps and also the instrumentation using the odd instrumentation approaches.
**Mike Dame** 08:44 Exactly, and maybe put, like, a feature flag around it or something that, you know, if people don't want to… but, like, you know, show that on and off, and that mixture, and even… I mean, to a point, having an uninstrumented app in the hotel demo and a way to turn it on and off kind of helps emphasize showing what OTEL is doing, like.
You know, that gap there, and then suddenly the gap has a trace, like…
kind of giving more of the picture, but I don't know, you can…
you can make a case to them anyway, but I'm sure that they'll be open to the contribution, if there's a way for us to, like, own it as, like, you know, maintainers of that section.
Something like that.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 09:21 Yeah, something that Ted Young told me is that when I asked him about this, he's like, yeah, I mean…
Be expecting that you'll have to do the work.
Your SIGs will have to do the work. It's just that, don't expect that somebody else is going to do this for you. So, if you're willing to do that, I think…
It's much easier.
**Mike Dame** 09:42 Makes total sense, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 09:45 Cool.
All right, thank you.
**Tyler** 09:49 Cool. Alright, yeah, sounds good, yeah, keep us in the loop on that, happy to help on that one.
Next up, I just wanted to make an announcement that I'm still also looking at the unification of offset generation, so maybe just in case people weren't, on the last call where we talked about this. So, one of the things that we do share across, auto insertion projects, as well as for custom probes, we'll need is, like, some way to generate offsets for
applications, so not critical, both auto-insertation and the OB Project also, like, will do this at runtime if the debug symbols are there, so it's,
not 100% needed, but, like, it is something that, like, we like to, because it provides caching. So to do that, though, like, right now we have two different ways, like, two different libraries to do that. One of them…
Both of them, I think… actually, I think Obi's is accessible publicly, the one here is not, so that would definitely not work if we ever do add these custom probes, which is still a goal. So I was looking at trying to fix that by
Unifying, our approach in both projects, and then, you know, canonicalizing that into a single, package.
I have…
built up this, like, idea… I've got, like, a spec sheet of what I want to try to accomplish in that package. It's a lot, though. As anybody who's looked at the offset stuff is, it turns out to be a huge problem, trying to figure this out. So I was just wondering, like, if there… like, where it should live, I guess is the question?
I was originally thinking of putting it here, but I'm also wondering if it should just be in its own repository, was my thought as well. If it's going to be shared across it, it may also help reduce noise, in either repository.
But I'm also… like, it's a separate thing for maintainers to maintain and other approvers to watch, so, like, I understand, like, it's… it could be also seen as added load, so I wanted to ask the question here of what people's thoughts on it are.
**Mike Dame** 11:40 I think one of the big…
points could be if the offset generator stuff… I know that the probe API right now uses some of the, like, types from the offset generator, is that right? So if that is…
that could be a point, or at least somewhere where we try to draw the defining line of, you know, is the offset generator, like, machinery itself? Like, the tool pulled into its own repo that imports from
you know, the probe API, but I think that… that point alone could be a case to keep them together. I love the idea of having them as separate repos and this generator tool as its own
thing, but I'm just trying to think of where, like, the other side could come from for that.
**Tyler** 12:24 Yeah, if I remember correctly, there is some duplication, but, in the sense that, like, the offset representation within, like, a program is… is… is in two different places, if I remember correctly, but it's mostly, like, there is shared, types, right?
First, I mean, not share types, the, the API for the offset package is… is then the types exposed from there are used in the probes, but I think that there are…
Translated, into another type, that is actually then,
fed into, like, the actual eBPF values that, like, are used. So it's, like, those aren't directly pushed into, like, eBPF code, so because they aren't, they have to actually, you know, get loaded into a map, and so there is, like, a translation layer.
So, like, it's a loose coupling, but there's definitely a coupling there. I think that, like, the fact that the…
package for offsets would be exported, like, you would have these types exported from that package. There shouldn't be any problem importing that from a local repository versus an external repository, in that sense. So, yeah, I don't know if, like, you want to
if we wanted to more tightly couple them, where, like, the offset package would then use types from the probe API, that would be a problem, because the probe API is not, currently exposed. But that's not currently how it's defined, it's the other way around, where the offset, types are used by the probe, yeah.
**Mike Dame** 13:47 Okay, yeah, that's… that's kind of… I wasn't saying let's make it more tightly coupled, I was just calling out that if they are coupled, then that might help either drive us towards that split in a good way.
You know, so, you know, that… that could be a reason for splitting it out on its own, and kind of emphasize the… that this is a modular
Yeah. You know, you're supposed to be able to pull this tool off the shelf and run to create your own probes.
So, I think that it would make… it would make things, I think, a little bit cleaner as we try to look at this framework and this API, and how to, like, stabilize it if this offset generator tool was pulled out.
So it would be nice to me, but yeah, the maintenance, I don't know, I don't think that the maintenance would be very much on it.
It's a… I don't think we've made many changes to it in a while.
So… No, I think… It's a small tool.
**Tyler** 14:43 the… yeah, it's more the initial overhead, right? Because there's just a lot of, parsing logic, API logic, and then you have to build a CLI around it for this whole thing, which has been done in both projects, so…
It's a lot of work, and it's been… it's duplicated, so, like, yeah, like, there isn't, I don't think, like you said, much maintenance required on it once it's up and running.
There, we have found some bugs, if I remember correctly, but yeah, yeah, the…
I also think that might be helpful, is because you have a dedicated repository to target, like, tests and that kind of thing there, so yeah, to do that, you'd have more comprehensive testing, hopefully, on just that.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 15:21 Yeah, I think it's a good idea to split off. In my opinion, I think Mario also in the past wanted to have a separate repo for this.
before Baylor was donated, and so…
**Tyler** 15:32 Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 15:33 It could be really useful to have it separate.
**Tyler** 15:40 Whoa!
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 15:41 Potentially could go beyond Go?
As well, in the future, I don't know if…
**Tyler** 15:46 Yeah, that's… that's actually included in my spec, is I wanted to, like, think about Rust and C++ from… That's right.
premise design. I don't know, I mean, there's probably other languages as well, but those are the two where I'm starting to think from the design, the start, because, like, I think if we do that, I think we want to keep that in mind for API design and how we're going to be able to support those going forward. So that is… that is… yeah, good point, and that is included
I think what I can do, also, is I can try to,
get that spec that I've been kind of building for this package and load it into some sort of format that I could share it in this meeting, or, and maybe the OB meeting as well, and so we can get a little bit more idea. One thing I haven't done is,
I kind of just assumed, looking at the data model that we're using here in the auto-inter rotation, just because we had talked about this before, it uses explicit versions instead of version ranges, so you don't have the bugs,
But I do… I do want to maybe take a step back and look holistically at what that data model is defined, if we can optimize it, if we can… if there's… bugs exist that I don't see right now, so maybe even more of a review on that.
So I think that's kind of, like, my next step for, like, building out that specification, and then, yeah, and then trying to share it before… before any work is done on the repository, get a good, like, sense of where we want to go with it, just so we can get, I think.
some agreement across… because, like, the OB project would have to change the offset, that it's actually using, and so that would be something we want to make sure that, like, there's an agreed reason to do that, and then…
when we import these types from the API, both projects will have to update to use those new types. So, like, making sure that they're useful, they're functional, there's not something missing, I think is key. So, yeah, having agreement before a lot of work is done is kind of my goal.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 17:32 Sounds good.
**Tyler** 17:35 But yeah, okay, that answers the one question. I will try to…
motivate this to be in a separate repository when I'm defining this, and then we can…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 17:42 Maybe… maybe go for a plan on… after that.
Camel has his hand up.
**Tyler** 17:48 Oh, sorry. Yeah.
**Kemal Akkoyun** 17:50 wasn't that important. It was just another supporting argument that EVPF Profiler also needs some similar plumbing, so having this in a separate tool or, like, a package would help.
yeah, people keep solving the same issue. I've worked on similar issues before, so yeah, definitely.
**Mike Dame** 18:13 It's really… Have you.
**Tyler** 18:15 Yeah, really good to know. Do you… is it pretty easy to find in the profiler repo where, like, the offset stuff, if I just do a search for it, or is it kind of deep in there?
**Kemal Akkoyun** 18:23 No, it shouldn't… I mean, I was just checking that I can just put it here. They… this is the only, like, entry point that I've seen. They are trying to do this for the label offsets.
But… There might be other use cases. This is just an initial search showed me.
**Tyler** 18:42 Yeah, okay. This is… yeah, this looks…
This looks great, okay. I will take a look at this as well, then, because, again, like you're saying, like, I'd like to have a solution for all of these, so let's try to, yeah, do exactly that.
Yeah, thanks, thanks for pointing that out.
Okay, cool.
I will then move forward with that, thanks for the feedback on that. I don't see any other agenda items here. I'll pause really quick.
And, if anybody has another topic they want to talk about?
I guess we have plenty of time, so maybe we could just ask a question about high-level next steps on our,
probe,
migration. I think it's been a while since we took a look at this. One of our goals is to try to have… try to merge the OB project. We talked a little bit about this at KubeCon. Mike and Ron, were there.
Which was great seeing you, by the way. But yeah, it is definitely one of those things that we wanted to talk about, like, how are we… are we still going about this? I know that the next step was to try to look at
migrating a probe, from the auto project into Obi at some point. It's definitely something that's kind of a Herculean task, but it was also stalled at this point.
So I don't know…
Mike, correct me if I'm wrong, were there other aspects we were talking about? Maybe there was something else?
**Mike Dame** 20:12 No, I think that was kind of the over… that was, I think, what did we call that? The, like, silver bullet or something? .
**Tyler** 20:18 Oh, the steel thrift.
**Mike Dame** 20:18 That was the steel thread, right? Yeah, that was the main, like, if we can do this, we built it, and then there were subtasks under that that kind of, I think, the core…
task to get it started was to look at the C, libraries and, you know, the probe code itself, see how can that be portable,
And, then I think from there, it was kind of the API types itself, and I had done a couple, like, experimental, like, approaches at, you know, defining the API, but yeah, the overall,
Porting a probe, kind of lifting and shifting it from this repo to the next one, seeing does it drop in, does it still work?
That is kind of the overall, so I think that we could break that, like, really kind of break that task down. It seems like the OB project is, like, dust is kind of settling around it now, that the donation is done, so maybe there's a little bit more time for that to be,
Kind of a joint priority.
So, maybe we can get some momentum on it in 2026.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 21:25 Yeah, we need to restart that effort. I know on my side, I've sort of failed to find time to work on that. I created this list of things that needed to happen, sort of started going bit by bit, but yeah, there's been so much…
Happening.
**Tyler** 21:41 Yeah, it's open source, right? So I think maybe that's a good way to say it, is just, like, we can start to reprioritize that for the 2026, timeframe. I think that seems reasonable to me, like…
looking at the schedule for the end of the year, like, there's a lot to get done that I don't think this is something that I could put on my plate. So, yeah, I think if that sounds good, we can plan on starting to tackle that in the new year. That sounds great.
Cool.
Any other topics, any other cool uses of honor's rotation?
Oh, I guess, one of the reasons I was late was I was talking to some of the isovalent folks, turns out they're closer to me than… than others, and, one of the things is I am trying to get some, like, help from them and contributions to this and the OB projects, just to, like.
get some expertise, I think, in the library as well as, like, you know, EBPF space. Obviously, we have some really smart people in this space, but having, some of those folks also contribute would be great, so… I guess that's just to whet your appetite. There's no commitments yet, so… but hopefully, hopefully more to come on that one. Yeah, so, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 22:51 That was super cool.
**Mike Dame** 22:53 That would be great.
**Tyler** 22:54 Yeah, I… I'm really pushing for it, so, yeah, yeah, absolutely.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 23:01 Good stuff, Tyler.
**Tyler** 23:06 Well, cool,
Yeah, I just saw, also, videos are coming out of KoopCon Talks, so if people have, talks that they have found were really cool, that they attended, or they find ones from other, I don't know, links or something like that, please, go ahead and post them in our Slack channel. I'm interested to maybe see some more
I know there was a lot that I didn't get to see that I wanted to go see, so I'm gonna hopefully try to go and go back and go through some of those, but…
Yeah, I'm interested in folks, if you have talks that you would recommend, also just posting on maybe the Slack channel would be great.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 23:40 Yeah, it's cool that you found that one up for Rust. That was pretty cool.
**Tyler** 23:43 Yeah, that one… I actually was… I was kind of surprised, like, I remember I was having this conversation, and I was just like, wait, this sounds really familiar, like, what's… and they were like, tell me about it, I was like, oh, I gotta see this. So, yeah, yeah.
But yeah, yeah, other ones, like, other languages as well, I think that'd be cool. Like, I, yeah, I think, I think the Rust stuff is kind of more interesting to me right now than it should be, but…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 24:03 Beautiful.
**Tyler** 24:03 This is because I'm… I'm good at getting nerd sniped, but yeah, so… Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 24:10 It's too bad the strip symbol wasn't hacked.
**Tyler** 24:12 I… I know.
I mean…
That's the problem with hyper-optimization, right? Like, yeah, get all the… get rid of all the good stuff, but…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 24:23 Actually, maybe it's a good thing. Have you ever seen the Rust symbols? How they, like.
**Kemal Akkoyun** 24:29 Crazy.
**Tyler** 24:31 Yeah, it's also true. Yeah. I think you're better off,
Thing some, like, alien language in some of those sometimes, but yeah.
Well, cool.
Well, awesome. We could probably end the meeting early here, then.
No other topics. It's good seeing you all. Excited to go to the holidays as well, so things are slowing down. Oh, I guess… yeah, one of the things that the GC… I think the GC decided was the last two weeks of the year, no meetings, they've already canceled everything, so, just a heads up on that one. Don't expect, these meetings then.
decision was made for us at this point. So yeah, just, just kind of a heads up, on that one. So, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 25:12 Alright!
**Tyler** 25:13 Well, cool. Thanks for everyone. I'll talk to you all in a week's time. I'll see you later.
