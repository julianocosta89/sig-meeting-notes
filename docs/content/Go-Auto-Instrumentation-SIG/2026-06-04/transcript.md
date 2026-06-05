SIG: Go Auto-Instrumentation SIG
Date: 2026-06-04
Duration: 52 minutes
============================================================

## Zoom Recording Transcript

**Nikola Grcevski @ Grafana / OpenTelemetry** 00:29 You saving?
**Stephen Lang** 00:30 I ain't a clue.
**Tyler** 01:22 Hey.
**Mike Dame** 01:25 Hey guys, what's up?
**Nikola Grcevski @ Grafana / OpenTelemetry** 01:26 Bye.
**Ron Federman** 01:29 8.
**Mike Dame** 01:35 So we do have the notes doc for this, too. Should be on the… the meeting invite.
I don't think that we're gonna have, too many more people show up for this.
I think I told Jurassy about it.
**Tyler** 02:32 Yeah, I was wondering about that one.
**Mike Dame** 02:34 Yeah, I can give him a ping, and just see, were you planning on joining? If not.
**Tyler** 02:40 I see there's also… some folks from Datadog on the invite?
**Mike Dame** 02:46 Hi there…
**Tyler** 02:47 Did you… did you add them, or did somebody else add them, Mike?
**Mike Dame** 02:51 No, it must have been… somebody else, or maybe they were on the… the old meeting?
Yeah, I didn't… I didn't.
**Tyler** 03:00 Okay.
**Mike Dame** 03:00 I think… I think Ron is the only one that I sent it to, so that's why he's on there.
**Tyler** 03:09 I'm guessing, yeah, it was probably just a curiosity thing.
**Mike Dame** 03:22 Send him a message and see if he's back.
Otherwise, I think we could probably… get into it here, we've only… We've got an hour? Okay, so… Yeah, just wanted to bring this together to talk about what are we gonna do with the Go Auto project?
it was… And everyone's pretty much familiar with it. We've all been, maintainers of it for a while. I kind of, set up some of the… the, ideas. Oh, pretty dressy.
For… for what kind of would evolve and grow into… to OB, or at least some of the… the ideas around, like, Go instrumentation, using EPF for tracing, stuff like that.
I think that… Not too… not, like, trying to blame the OB donation or anything in that, but I think that that is such a superset of a project that, a lot of attention has kind of shifted away from GoAuto. I know that me and Ron both also haven't really been keeping up with the Go Auto project very much. Tyler, I think, has been the one that's been doing most of the maintaining there and keeping things up to date. So really appreciate that, but overall, there's a lot of just confusion from… from users, from other maintainers, the, the GC, wondering, like, what is the plan with this project? How does it fit in with… with OB?
people… a big thing, I think, is kind of when we think about the whole context of where OpenTelemetry is right now, moving to graduated, really reaching the status as, like, a production-ready, standard for enterprises to use.
Having, like, confusion around what project does what is really not… fitting in with the marketability of OpenTelemetry and… and reaching those users. And it doesn't help eBPF either, in general, either of our projects, if, you know, we want to have a clear message for people to find eBPF tracing and instrumentation and adopt it, and this is a really critical time for that.
Where, you know, if it lingers, and it's too confusing, and the space is just not very clearly defined for too long, then we kind of miss the launch of it. It's gonna end up… it's gonna get that reputation of… Being messy and not really well-defined.
So, I mean, all that said, I think that kind of the general impression, and, you know, talked to Ron about this, and talked to other people at Jurassi and everyone, is that having OBI, kind of be the… the main, eBPF instrumentation and tracing project in OpenTelemetry. It's really kind of where everything is pushing, that meaning that we should come up with a plan to kind of archive and sunset the Go Auto project. That's something that people have been asking about for a while, and I know that I've been pretty vocal about saying, well, you know, people are using it.
Oh, it goes for one, we have… I mean, we're using a fork off of it, but it's still the same idea of having that upstream that we're based off of. But also, you have things like the OpenTelemetry operator that's using that image, and… the repo gets a lot of traffic. If you look at the traffic stats for it, it's kind of… it's impossible to know how many people are really using it, but I would say that the number is more than zero.
That's good, and that's bad, because that traffic and those people that are coming to see it are seeing this empty repo, so we don't want that to be the impression.
So… That said, trying to kind of shift all of the users, vendors, like Odagos and the end users, and if you open telemetry operator, anyone that's using GoAuto.
into Obi, We, kind of need, like, a sunset and almost like a migration path, and kind of look at What is it that, you know, what can we confidently and, like, proudly say, okay, we're… we're shutting down this… this project, here's the replacement, and, you know, be… be confident in that, that… that users, anyone that's finding it will… will see it. It's… kind of sets a precedent also for open telemetry on the whole. I think that it would reflect really good on both of our SIGs, or, like, all of the people involved, if we can kind of take this… this seriously.
Yeah, Jassy, that's no problem.
So yeah, that's… that's at least where I'm coming from with it. I was first off, trying to see if everyone else kind of feels that way. I don't want to just… like, I'm not the one leading this or anything, you know, this is a team, project here, so… I'm happy to talk. I'm sure everyone knows. But I want to hear from everyone else, too. What does everyone think about that?
**Juraci Paixão Kröhling** 08:42 Well, Mike, if you allow me, I'd like to say a few words as well at the very beginning. I tried to join on time, but apparently when you join Zoom twice, it kicks you out from the other one, so I had to find a way to join two calls at the same time.
I'm sure you gave some context here already, but I wanted to share the perspective of the GC here.
we… so I'm the liaison for… for the SIG.
I hope that you all know that. And I'm here as, in that capacity, so I'm here to help you out, to help you navigate the situation. And the main idea, or the main conversation here is, we had a discussion a few weeks ago, perhaps a couple of months now, at the GC, where we were talking about some SIGs, and how activity is very low on some SIGs.
And, and, the Go Auto was mentioned there. That's when I pinged Mike and said, like, let's have a conversation, let's see how is it going, what is… where are we in terms of the roadmap between GoAuto and Bela and Obi, and so on and so forth.
I also got a little bit… concerned about the lack of feedback that I was getting from GoAuto maintainers in general, not very specific to anyone.
And… And that's how… Mike and I started this conversation. So we started discussing, like, what can we do for the future, what is… what is happening, what is the current situation, and what is the desired outcome? What was the desired outcome for the beta donation back then, and did we achieve that? Did we not achieve that? And and really, the main… there's no… desired outcome when it comes to the GC for a specific solution, for a specific Decision?
it is really, in the benefit of end users. Like, if there is confusion from end users, we should clarify that, and if the project is in a state where Where users should not expect any support anymore, then have a conversation about sunsetting, about merging, and… really, this is not… I don't have an outcome in mind. It is really just, so that we can… we can find what do we want for the future? And then work towards this goal.
I think right now, it's a bit confusing from people from the outside. Which one should I use if I have a Google application? I'm confused myself, I think most of the GC is confused as well, so I think at least a clarity of vision and messaging would be useful.
But, again, When it comes to the technical side, it's all on you all.
**Mike Dame** 11:46 Yeah, thanks, Jessie. Yeah, I did kind of talk about the confusion and everything, and that's, I think, what it really comes down to.
**Tyler** 11:58 Yeah, I'm all in favor of what we've got planned. I think archiving the project and moving forward sounds good.
**Mike Dame** 12:06 Yep.
I kind of just thought about some of the other things that Drassi said of, like, what were the goals of the OB donation? Did we achieve those? I think that's kind of a good framing to look at it, see… I think the idea of our… what we need to archive is kind of it's obvious, because just the overall interest and the activity isn't totally there to keep this project up. I did do some, you know, homework and look back through the OB donation and try to see what the goals were there, and I think we had some kind of ambitious and maybe optimistic, ideas that… it was spelled out that Go Auto and Obi would exist separately, and there's, you know, phrasing, like, users that are depending on Go Auto shouldn't need to take a dependency on Bela, and it was kind of, you know.
I… looking at the goals of Go Auto at the time.
we were really, I think, trying to build a, like, an API that Obi would… would consume there. You know, the whole custom probe idea was really our main goal. We had a blog post that posted, hey, we're beta, this is what we're working towards.
But the thing is that, like, priorities and ideas and things change. This is open source, it's tech, it's always evolving, and so, We can look back and say.
Did we achieve, those goals?
I don't think so. I think that there was a lot of overlap in the maintainers, and… A lot of, you know, just not really enough pushing that to, you know, build that consumption, that API.
So… that's not bad. Like, no one did anything wrong, but just from that perspective.
I think that we were a little ambitious with the goals, and it's really, I know that I was one of the people that wanted to push to keep them separate.
Other people were… agreed with that idea, too, but, Yeah, moving forward from that, that's kind of where I think some of the transition idea comes from, is can we take that kernel of the idea, and say, okay, what's… what's missing? How can we migrate? How can we incorporate that?
So yeah, that's… that's kind of what I've been starting some work to do in Obi, with some of that, like, API-based, like, dynamic selector stuff to make sure that at least the way that GoAuto was as a, like, SDK for people to import and use, that's usable.
Is there any… what other things do people think? Like, if we were to, like, shut this down tomorrow.
What are some of the gaps in… Obi, because I don't think that the consumption model is going to work, for me at least, and anyone if you think elsewise. I see it as, like, let's just make sure that there's feature parity in Obi, like, baseline feature parity, make Obi the thing, and we don't have to worry about trying to wire up GoAuto into OB anymore, because that wasn't working out.
Does that seem Kind of like the approach?
**Nikola Grcevski @ Grafana / OpenTelemetry** 15:22 Yeah, it seems reasonable from my perspective. I think we added compatibility in OB for the environment variables that Go Auto was using, so… I mean, that could help with transitioning, say, if we want to try OB into the operator. I know there was, there was desire for that to happen on the operator SIG.
I was mostly concerned there because our main deployment model is DemonSet, and there's no such thing there. They want a sidecar.
Which Obi can work in, it's just less efficient. But since then, there have been a couple of things that were added into OB, like the dynamic map resizing.
So we can create a config that would be… Sort of, like, work in a sidecar mode and not take too many… memory, too much memory from the Kubernetes cluster and whatnot. So… Yeah, we can… we can try to make a package that… that cannot get upgraded.
Yeah, but I think the command line options are there.
Yeah, not 100% at all, but maybe that's another thing to look into, to port everything so it could be used as a… Directly as a replacement for any end users.
They're expecting continued GO artist instrumentation support if we sunset this project.
**Mike Dame** 16:50 Yeah, I think the hotel operator is a big one. You know, if we… if we shut down Go Auto, the operator loses Go Auto Instrumentation. If OB replaces that, then that's… that's, I think, the direction to move to.
So, looking at that… What about, the library instrumentation. I don't know, maybe Ron, or… I don't need to be the one that's doing all the talking, anyone can jump in.
**Ron Federman** 17:24 I think, one important part is the Auto SDK.
which we have, like, the OpenTelemetry Go repo depends on it, I think, like… the API part depends on it.
And, like, by transitive dependencies, that makes it… Like, a dependency of all the users of the Autel Grove API?
I think this is, like, a really cool and important feature, so I think we need to… I don't know if… Move it to the Obi repo, or move it to the HotelGo repo, Well, somewhere that's just… keep… keep it alive, I guess.
**Mike Dame** 18:13 Yeah, what do people think about that? Where does… the, like, the Auto SDK… what does Obi have for Auto SDK support?
**Nikola Grcevski @ Grafana / OpenTelemetry** 18:23 This is for adding, ensuring that you can use the Go SDK to add manual spans and to be linked.
**Mike Dame** 18:30 Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 18:30 We do have a slightly different approach.
to, to what was done in Go Auto, because I wanted to avoid BPF ProRideUser as being a dependency.
So… We have a slightly different approach.
I don't remember off the top of my mind.
But… Sort of works without it.
I don't think we have the full capabilities, though. You can't… You can add manual spans.
And using the Go SDK, but you cannot set the eBPF tracer as your Go SDK tracer.
I don't think everything exactly works.
So… I need to remember. I did it, like, I don't know, 6, 8 months ago, I don't quite remember exactly, but I know I looked at the Go Auto SDK, and I was like, yeah, I should do this, but then… probe, EVP, probe right user discouraged me, so, I think you can… so in Obi, you can write… you can import the Go SDK and start creating manual spans, and… We put a probe similar to Go Auto.
Into the manual spans, and then… Find the parent and everything else.
But it's, but you cannot set it as tracer. That's just slightly different.
**Ron Federman** 20:07 And…
**Mike Dame** 20:07 So that's… I'm curious what that part… I was just curious what that part means by not being able to set it as the tracer, because that… like, the tracer was kind of just, like, the internal implementation, right? The auto SDK, when eBPF was active, that's what kind of behind the scenes would set it as the tracer, is that… Like, are the spans linked? Does it… Nikola Grcevski @ Grafana / OpenTelemetry 20:29 Yeah, spans are linked. You don't define exporter or anything, you just start writing manual spans, or whatever you like, and… This stuff magically goes to your incoming and outgoing.
I don't remember exactly how I did, but we do have an example, in the tests, how that works. A few examples, I can try to share my screen, if you like.
If we're looking now… if you want to look now, we can look at separately. But I know I didn't actually implement a… The whole exact thing.
Because of that probe, right.
Business.
So, I'm trying to remember. There might be limitations to what we do compared to Co-Auto, maybe not all things…
**Tyler** 21:15 So, like, the only right, if I remember correctly, was, like, there's, like, a pool in.
**Nikola Grcevski @ Grafana / OpenTelemetry** 21:19 Yeah.
**Tyler** 21:21 API, and you had to write it at the beginning of the.
**Nikola Grcevski @ Grafana / OpenTelemetry** 21:24 Hmm.
**Tyler** 21:24 Like, the startup to say, like.
start using this, start using, like, the auto SDK, essentially that's in the global package.
Yeah.
I feel like there's ways around that.
Okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 21:42 Yeah, that's…
**Ron Federman** 21:44 If it's just, like, one… one time write to these bullets… Doable with pit race, I guess?
**Nikola Grcevski @ Grafana / OpenTelemetry** 21:52 Yeah, we could do that, too. Yeah, we looked at that.
**Tyler** 21:55 I can't remember why we didn't do it. I think it was, like, too complicated in GoAuto.
But maybe it's worth taking a look to get around the BPF, right, user. Yeah, I can't remember.
**Ron Federman** 22:06 But I think the right user is used for also, like, You can have, like.
the EBPS probe, like, tell you, like, the grow code, this is the spend context currently, this is, like, this is sample doughnut sample, like.
Like, when you create a new span, and then it goes to the Auto SDK, then you can get the actual span ID of the DBPF span, if it's active, or something like that.
**Tyler** 22:33 Mmm, yeah, you're right.
**Nikola Grcevski @ Grafana / OpenTelemetry** 22:38 Yeah, I think that that doesn't exist in OB. You can get the actual tracer in Go and manipulate and do stuff with it, because we don't do that. So we don't actually have a tracer at the back.
You just can write manual spends, and they will just get linked. But you can't do all this stuff. That's why I said it's not fully matching what GoWater could do. So that will need to get ported, if we want to retain that functionality.
As to… as to where this code, lives, I don't… Don't have an opinion. Either way, it's fine.
**Tyler** 23:14 So the… so you're talking about the code for the auto SDK that we have in the… Yeah. Auto transportation project. I… I'm not too sure… So the thing is, is, like, the global one also has a copy of that.
And that's what's used in, like, the main API. I'm not exactly sure where else it's used outside of the Go Auto project, I guess.
**Mike Dame** 23:41 I think that that is the… the Go Auto slash SDK import, that's the transitive, like, import that I think anything that uses OpenTelemetry gets, right?
Okay, I think it's go.opentelemetry.io slash… I don't… I'm… I'm, like, looking up.
**Tyler** 24:06 Yeah, but, I mean…
**Mike Dame** 24:07 Yeah.
**Tyler** 24:08 from the… from the users of the Go SDK, or the Go API, like, they don't import that.
**Mike Dame** 24:14 Oh, yeah, yeah. Okay.
**So then, yeah, we're… Nikola Grcevski @ Grafana / OpenTelemetry** 24:20 Is it a depth of the main Go SDK? Does the main Go SDK depend on that?
**Ron Federman** 24:26 Go API, I think.
**Nikola Grcevski @ Grafana / OpenTelemetry** 24:28 Cool.
**Ron Federman** 24:28 Fine?
**Tyler** 24:29 No. No, we wrote a fork of that, and then it's a copy.
Specifically to avoid that dependency.
**Mike Dame** 24:39 And what I'm wondering is, like, why… so this is in Kubernetes, why does it… transitively import go.opentelemetry.io slash auto. I never really understood the copy of it in the global And why it's still… Existed in auto.
Like, if that's, like, the transitive dependency, yeah, we can change that import easily, and it doesn't break anyone's, like, import path.
But I just never understood what… What that point was.
**Tyler** 25:10 Let me, let me double check here.
We can…
**Mike Dame** 25:16 We don't have to…
**Tyler** 25:16 Actually, there is a… there is an import here of… Auto. So maybe, maybe I'm wrong, actually.
Hmm.
Yeah, the Auto SDK, is… is, is imported by the main Go API.
Trying to find where it is.
Yeah.
Yeah, it's in this global trace, Package.
I don't… I think this is just that switch over. So there's, I mean.
I thought we copied this, I'm a little confused about this right now, but .
**Mike Dame** 26:12 Yeah, we definitely did. I remember you doing the copy.
**Tyler** 26:16 Yeah.
**Mike Dame** 26:17 I never knew why.
**Ron Federman** 26:19 I think there was, like, a few use cases that we wanted to support, like, well… Use cases of getting the spend from the current context, or getting it from the global, like, a few different scenarios, and one of those scenarios required, forking it into Dell, something like that.
**Tyler** 26:41 Yeah, I mean, I… so, anyway, like, there's nothing stopping us from just, like, copying that SDK package into the internal. It's just a question for the, the Go maintainers. So, we can… we can work on that.
**Mike Dame** 26:57 Yeah, I think that that… and we don't have to work out the entire plan right now, it's kind of like identifying what we're gonna do, and maybe set a… you know, I think coincide this sunsetting with, like, the OB stable that we're planning for later this year would be kind of a good plan, so we can then… like, when OB's stable, it's, like, clearly, okay, there's nothing else, messing with that.
So, a little bit of time.
**Tyler** 27:22 What I'm saying is, like, is if we deprecate the package, Big ol' maintainers aren't.
Comfortable keeping it there, so we'll copy it and just maintain it over there.
Yeah, I mean, I would say…
**Mike Dame** 27:32 deprecate.
Well, the… oh, yeah, they don't want to keep the Go Auto deprecated. The auto SDK is stable, right? So how does that… In fact, that's like a V1.
**Tyler** 27:44 You can deprecate D1, V2.
**Mike Dame** 27:46 I guess, man.
**Tyler** 27:46 Whatever.
**Mike Dame** 27:47 Yeah, that's true.
Alright, so… if that's not a problem, then… Yeah, as long as there's… so that's one thing. I think that's probably the biggest piece out of this project, is making sure that there's auto SDK support.
then… The rest would be… What, I mean… I mentioned library instrumentations, that was a big part of, like, the probe API that we were talking about doing. Is there anything… Bet.
Obi doesn't… support, I mean, GoAuto had, because it was more user space, it had, I think, more… like, function-relevant attributes? But is there… what are the gaps there between Like, how will spans look any different if we switch the hotel operator over, go to OB?
**Nikola Grcevski @ Grafana / OpenTelemetry** 28:42 That'll look different, for sure.
We can see if there's any attributes that are missing.
So… I tried to keep up with the spec, but I actually don't know off the top of my head, depending on which instrumentation exported what attributes, if we're missing any.
Yeah. Yeah, we need to do a survey of that.
To make sure that it matches.
Instrumentation is wide… wise in terms of what instrumentation is supported, I think OB's a superset, if I remember correctly, last time I checked.
And, Yeah, Obi now does also the generic instrumentation, so even if the library isn't actually supported, let's say somebody's using Franz Kafka, whatever, to talk to Kafka.
It will still produce bats.
So, we can have targeted instrumentation, but… There's also the fallback.
**Mike Dame** 29:54 And it's also, you know, this isn't, like, a blocker to get every attribute in every library in, like, GoAuto is only beta.
So… if it… like, just kind of a… from a due diligence perspective of, like, we're at least aware of what's gonna be changing, and maybe have some to-dos that get added to OB, even after stable and new libraries and new attributes support.
that's really, I think, all of this stuff, right? It's… there isn't… it's a beta project that we're shutting down.
You know, just taking reasonable care to think about what we're dropping is… I'm happy with that, so… We have some idea of the differences. It can be, like, you know, even one-time blog posts, as if you were using this.
You might notice you're not gonna have these attributes anymore, working on it.
**Nikola Grcevski @ Grafana / OpenTelemetry** 30:55 Yeah, added a line there. I think we should compare and make sure that we don't break anything.
**Mike Dame** 31:01 Yeah.
Yeah, it's… it's… It's just trying to do the best that we can to migrate.
it doesn't need to block, like, Obi going stable if, like, oh, we can't get this attribute that GoAuto had, or something, right?
**Nikola Grcevski @ Grafana / OpenTelemetry** 31:20 Huh.
**Mike Dame** 31:22 Okay, so… Those were kind of… I think, for me, the, like, 3 big things were, like, the dynamic encode stuff.
I'm pretty much handling that. That's, like, features, too, right? It's things like, okay, in Go Auto, we could have, like, with resource attributes, okay, we can end up adding that to Obi.
Don't think that needs to block OB stable.
The Auto SDK, I think, is a bigger… bit bigger of a task.
Because it's… I don't know, it's reached other projects at this point, like sharing the Kubernetes import. I know me and Ron have done a lot, like, showing off how you can instrument, a Kubernetes cluster, like, automatically with, with, Go and OpenTelemetry now, so that's pretty cool. Don't know if anyone's using it, but… that was something that we put to stable, and maybe we could talk to the GO maintainers about just where should that live? Trying to keep that… I know Tyler put a ton of work into that.
It's a real, like, fully capable, compatible SDK. It's really cool. That would be great to keep. I think that's the biggest one. And then, trying to make sure that, or at least being aware of generally, what's the difference? What libraries are supported? What's not?
and differences between that. Maybe we get a couple small PRs for OB out of that, and say, oh, this attribute was in GoAuto, we'll add it here in OB2.
Are there any other, like… You know, homework tasks that we want to look through between them.
Kind of think about, like, a timeline, and… how to coordinate it with… with the OB.
State, stability.
**Nikola Grcevski @ Grafana / OpenTelemetry** 33:15 That's good. I… I like the plan.
I'd say we probably need to assign owners and add tasks into OB, so it doesn't get forgotten.
**Mike Dame** 33:28 Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 33:31 Nor.
It becomes a blocker for stability, if we want to do that.
**Mike Dame** 33:40 yeah, I really don't want to block the stability, I'm just kind of putting it out there as, like, it… I think it would help Sell the stability of it if… Like, if ObiGo Stable and Go Auto still doesn't have, like, an archived thing.
I don't think that that's gonna help OB stability land as well.
Cause there'll still… people will look up auto-instrumentation, eBPF, and still see those repos.
And I also think that we can do this before OB goes stable, too. If we're looking at, like, end of the year.
I don't know what the timeline plan was for Obi.
I was assuming it was, like, gonna be KubeCon-ish time.
But, I don't know, Tyler, you probably… Nicola, you guys know better.
**Tyler** 34:23 Yeah, I mean, my… to be perfectly honest, my goal is… is to focus on OB stability. Like, that's my priority.
I don't see any of this blocking that. Like, if there's missing features, there's nothing blocking us to stable release there.
I think that those features can always be added after the fact. We have a pretty clear roadmap for OB stability at this point.
And I, yeah, I plan to pursue that, pursue it to try to get it, like, in those timelines that you were just describing as well.
I think a lot of these feature sets are really great, but… I mean, I think this is kind of, like, the main reason why we're having this discussion right now, is because, like, it is open source, and, like, it's a meritocracy, and it's a duocracy, right? And if, like, nobody's gonna actually do these tasks, like.
then they're not gonna get done. Like, I definitely am motivated to try to get some SDK support in there, but… it is not a priority compared to the stability of OB right now, so…
**Mike Dame** 35:24 Yeah.
**Tyler** 35:24 Like, I'm happy to work on it, I just can't… guarantee that it's gonna get done in the timeline prior to the stable release of OV.
**Mike Dame** 35:34 Yeah, I didn't want to have any of this construed to be, like, it's blocking I know I'm really well aware that the OB stability plan is very well organized and has a lot in it already, so I'm not trying to dump more onto that. What I meant was more, like.
kind of a P2, like, idea subtask, it would be great to, have this kind of wrapped up before the OB announcement, but that's also something that maybe we could talk to the OB SIG about, but again, it's not… it's not blocking anything, and it… all of this is stuff that can be added after OB is stable, so, even if… like, I think another part that we should take out of this is trying to put it out there and put a big, maybe, notice on the Go Auto repo that says this is going to be archived, this isn't the standard anymore.
send people to OB to start using that, say, hey, this is planned to be deprecated. That alone will help a lot with the OB stability. I'm trying to see how this can… Be as much… clear up as much confusion as possible.
Before we, really launch OB.
So that's… that's what I meant by that, not to try to, say, hey, we gotta slide this in and block it.
**Tyler** 36:53 Yeah, I mean, I think that, the sooner you can get people to move over, the more you're gonna find, through using it in anger, like, the gaps that people actually want. So, like, I'm all in favor of that, like.
The more… the more users from here that you can shift over, the faster, the better.
I… that's… I'm… honestly, I think that's fine.
I… that's why I, honestly, I would prefer just… Like, a two-phase approach of, like, what you just said, of, like, give notice, maybe give an announcement somewhere, and then, honestly, like, a month or two later, like, start the deprecation process. Like, I think… the… the features that people care about, they'll ask for. The… the missing things that they want to use, like, they'll… they'll raise issues on, right? Like… The things that we think are really important and nobody cares about?
are not gonna get mentioned, right? Like… Yeah. I'd rather, I'd rather do it that way.
So, yeah, I mean, that's mine, but, like… I… again, I go back to that idea that, like, it's about, like, who's gonna actually do that, and if that's… something… they want to change the strategy on how they're gonna do it, then I think that's, you know, fine as well. Like, I think it's just about, like.
open source, like… That, you know…
**Mike Dame** 38:19 Yeah.
Yeah, I mean, we don't have to sit around on this, and, like, we're already… it's clearly, like, we're not very active in the Go AutoSig as it is while it was active, and, deprecating it. I mean, at least there's kind of an end goal with deprecating it, so you can think, well, maybe people will work more on that, but history kind of shows with this that we're all really busy with other stuff as it is, and so kind of just pulling the plug.
might be the strategy, too, you know, put it out and say, we're gonna pull the plug on this date. That could be the approach that we take. And, you know, speak now, forever, hold your peace kind of thing is also completely valid.
**Tyler** 39:01 And to be, to be clear, like, I think we should consider it as a final step, but, like, none of these things are irreversible.
**Mike Dame** 39:09 Nope.
True.
I did just think about… I know that, Obi imports Go Auto, right? How does it use that? Because I know that we've had to… like, we recently just did a Go Auto release, right? Or was that something else that was depending on GoAut? Like, when we were trying to deprecate the Go version support, Tyler, what was… what is it that's… Does Obi depend on Go Auto at all?
**Tyler** 39:37 I don't think so.
**Mike Dame** 39:39 Okay. Why did we do that? Nice.
Was that for… oh, that was for the Go… it was coming up in the OB SIG, though.
What was it?
**Tyler** 39:50 I mean, it depends on Psyllium's library, I'm not… I'm not sure.
**Mike Dame** 39:55 There was some reason that we had to do, Yeah, that Go Auto release where we, like, dropped Go 124?
**Tyler** 40:06 Oh, that was just for… for all of the dependencies that are sitting there waiting for GoAuto.
**Mike Dame** 40:15 Maybe I misunderstood that then.
**Tyler** 40:18 I mean, I think… I think that we wanted to upgrade the… the… the Go SDK and APIs, and we can't do that until we dropped the 124.
**Mike Dame** 40:27 Maybe that was it.
Okay, yeah, so that's… If… if that was it, I just… I just… Thought of that and said it wasn't that a thing.
Okay.
So, yeah, I kind of like the, like… we've… I think that we've done our homework here, What do you guys think for timeline for… I like the approach of, let's just rip the band-aid off, you know?
**Nikola Grcevski @ Grafana / OpenTelemetry** 40:59 I would say, like, the only thing is, like, this will break the operator. I know it's an experimental package, but do we want to provide an alternative before then, or just say.
when OB gets stable, you're gonna get something to get used to the operator, or… What are we thinking?
**Tyler** 41:16 I think that somebody's gotta commit to it, is the only thing.
I think that that's one of the big problems that we had, like… Yeah. I mean, I agree, like, I'd love to say yes, but… I cannot say yes, and I will do it, is the problem.
**Nikola Grcevski @ Grafana / OpenTelemetry** 41:33 Okay.
**Mike Dame** 41:34 It would… I mean, we could even just talk to the operator, like, open an issue update. Once we announce this deprecation, open an issue in the operator, it says, hey, by the way, this instrumentation is deprecated.
So you guys… someone might have to remove it from here. Again, I'm not volunteering, but… Could be.
they're not going to want to keep shipping a, you know, deprecated, archived old version that's going to have a bunch of CVEs and that image that every week, another thousand Vulnerabilities comes out.
So…
**Tyler** 42:10 Well, I mean, that's up to them, right? Like, they can…
**Mike Dame** 42:12 Yeah.
**Tyler** 42:13 they can just take it over, right? Like, they can… Yeah.
**Mike Dame** 42:16 I'm not saying fix it for them, but saying it's nice to… to let them know, you know.
work with the community, hey, as a heads up, we're shutting this project down, and maybe that'll motivate them to contribute more to OBI. Like, I think that's kind of your point, Todd, is, like, to people, right, that have a big problem with it, maybe this will pull more contributors into Obi, and other people will pick up those tasks.
**Nikola Grcevski @ Grafana / OpenTelemetry** 42:41 Yeah, there's an issue about OB being added to the hotel collector, to the auto operator, already.
So maybe that just ticked, you know, should happen.
I think there's already an issue open, but… I think it was waiting on the Helm chart, to be honest, but now we do, or… I don't know, there was some dependencies.
**Tyler** 43:00 Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 43:01 I think… There was some dependency, they couldn't really couldn't do it because of that, but I think now the Docker image is there, I think we should probably be able to write Probably be done.
**Mike Dame** 43:17 Address, you gotta hand up?
**Juraci Paixão Kröhling** 43:19 Yeah, if you… if you all need any help, in… in making noise, in letting people know, and anything like that, like blog posts, or live streams, or anything like that, ping me. I can get the community managers also involved.
They can help you all, spread the message, and make… again, as you all mentioned before, Or… there is no time pressure. It's all based on you, like, you decide, you take the timing, but If you… Whatever you decide, whenever you decide.
Let me know, and I can help.
Make people aware, and make noise, and bring attention to Whatever you want me to bring attention to.
**Mike Dame** 44:02 Yeah, making the noise and letting people know is probably… that's the goal, right? That's the… it's because it's not just about letting people know that are using it, that it's deprecated, but it's also about… the main point from the GC was the confusion. Making noise that this is being deprecated and going away, that clears up the confusion with everyone.
That's really why we should be announcing and opening these issues in the operator, letting people know, hey, this project, it was great, it's done now.
So… If you have any questions, forward it to the OB SIG, and that's the messaging that we want.
**Juraci Paixão Kröhling** 44:40 Yeah, we can help craft the right message there. I mean, it… I think the real message, at least from my perspective, from my side, is not even to clear up the confusion, it's really, this is how the project as a whole, this is how OpenTelemetry recommends you In doing this kind of instrumentation. This is, this is how you do it, and here's an example, here's how you can do it right now, today, and get telemetry out of it, and so on and so forth.
**Mike Dame** 45:12 Well, I don't know, I mean, we can start that.
Now, is there any… did we… have any last releases to want to do with GoAuto? We want to put a 125 or something? I know that there was… we did that one, and then I thought there was another one that we were trying to get it up to, like, 125 on, but… Otherwise, I mean, we can… open a PR to put a big thing on this and say, this is gonna get deprecated now and start working on Blog post and some announcements.
**Tyler** 45:42 Yeah, go for it.
**Mike Dame** 45:46 Right.
I've done a lot of talking. Does anyone else have any… Feedback or input, I think… am I all on the same page, or… did I say anything ridiculous?
Got it.
Well, I think, yeah, we kind of have what we're gonna do.
Which is just start… Making noise is the action… action item. There was stuff to… The Go Auto SDK, we want to talk to, like, the Go maintainers, right? Is that… Tyler, do you want to let the Go maintainers… now, you are one of the Go maintainers, right? Let them know that that's going to be going away, and if they want to keep hosting that or not, and then kind of… that's more just, like, cleanup, it's not a blocker to anything, but that's part of your Go SIG responsibilities.
**Tyler** 46:43 Yeah, we can… we can pull that in.
**Mike Dame** 46:47 Could you…
**Juraci Paixão Kröhling** 46:47 Two, perhaps the two communities, or the three, if you want to involve goal, get me a short statement to circulate with the GC.
like, what was discussed, what are the next steps, very internal to the GC, like, just letting them know that this is happening. They know that we are having this discussion here right now, but, I'd like to get a doc that I can share with them and say, you know, this is what was decided, this is what was discussed.
And then, perhaps another version of that doc, to circulate with the community managers, if you feel the need to have another set of docs.
And then I can share with them, and then I can get you, Mike, perhaps, involved to lead this, communication.
Get the community managers in touch with you, so you can all figure out, what kind of noise do you need.
And then we… we got it moving.
**Mike Dame** 47:47 Yeah, I'm happy to do that, if anyone else really wanted to… do that, I don't wanna… jump in, but I… I think that I'm probably the one that is the most trying to make a big deal out of this, so, I guess that's my responsibility. I can… I'll work on a doc… you wanted a… just something for the GC, just a short… this is what we talked about.
And, Yeah, and outlining how it's… how it's gonna affect other projects very minimally, but I think worth noting that we've thought about that.
And then, yeah, any other messaging that we want to do.
**Juraci Paixão Kröhling** 48:24 Who's the liaison for… for OB? Do you know that, Tyler, Nicola?
**Nikola Grcevski @ Grafana / OpenTelemetry** 48:29 Yeah.
**Juraci Paixão Kröhling** 48:29 Is it Morgan?
**Nikola Grcevski @ Grafana / OpenTelemetry** 48:31 No.
I think it's Severin. Severin.
**Mike Dame** 48:33 Sovereign?
**Juraci Paixão Kröhling** 48:34 Okay, okay. So, I'll probably ping him directly, on the trailer that I opened with the GC.
But yeah, we might want. So… Are we then gonna sunset, go auto, and then fold everything into OB? Like, is that the gist of it?
**Mike Dame** 48:56 Yeah, I think it's… it's not even so much folding things into OB, it's gonna be, like, best effort if people complain about a missing feature.
**Juraci Paixão Kröhling** 49:06 Yep.
**Mike Dame** 49:06 It's kind of just cleanup of… the Ghostig probably doesn't want to host this deprecated thing anymore.
Does it go somewhere? Does someone complain enough about it?
let the operator know. But yeah, there isn't really, I think, any features or functionality. From going through it here.
like, I'm working on stuff in Obi that I… that we did care about for having… you know, like I said, other people will hopefully do the same, and if no one does it for things, then no one really cared about it. But I think we've done here more than our responsibility, and I'm really proud of that, of just being able to Put some thought.
**Juraci Paixão Kröhling** 49:47 Alright.
**Mike Dame** 49:47 Into it.
**Juraci Paixão Kröhling** 49:53 Alright, sounds good.
**Mike Dame** 49:56 Dang.
Well, we're a little… early, but if there's nothing else, then we can probably wrap up. Thanks, everyone, for doing this. It's… I think it's something that it shows… reflects well on us for at least taking the time and putting the thought into it.
**Juraci Paixão Kröhling** 50:16 Same, same. Thank you very much, folks.
**Ron Federman** 50:18 Hmm.
**Nikola Grcevski @ Grafana / OpenTelemetry** 50:19 Thank you.
**Mike Dame** 50:20 You guys.
**Juraci Paixão Kröhling** 50:22 Right.
