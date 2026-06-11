SIG: eBPF instrumentation
Date: 2026-06-10
Duration: 65 minutes
============================================================

## Zoom Recording Transcript

RC Robert Cowart 00:00:31 Hey, Stefan.
Stephen Lang 00:00:33 Hi, Rob.
Rafael Roquetto 00:00:53 Hey guys.
RC Robert Cowart 00:00:56 Hello?
Stephen Lang 00:00:57 Hey, my friend.
Giuseppe Ognibene | Coralogix 00:01:36 Hi, everyone.
Tyler 00:01:56 Hey, how y'all doing?
Nikola Grcevski @ Grafana / OpenTelemetry 00:02:08 Back agenda today.
Tyler 00:02:10 Yeah, it really is.
Yeah, maybe on that note, I guess we're 2 minutes in. I see everyone's on the call, we can just start in, and .
Nikola Grcevski @ Grafana / OpenTelemetry 00:02:21 Fantastic.
Tyler 00:02:21 I'll start sharing my screen, yeah.
I guess, just a heads up, if you haven't yet already added your name to the attendees list, or you have other items you wanted to add to the agenda, go ahead and add them there, and .
Nikola Grcevski @ Grafana / OpenTelemetry 00:02:33 Throughout all the…
Tyler 00:02:34 We'll, we'll jump in here.
Vivek Akupatni 00:02:45 Stop Thank you.
Tyler 00:02:54 Cool, let's see if there's so many of our… Awesome. Okay, cool. So first off, I wanted to follow up from last week. We had talked about doing a roadmap check-in, where… 10 days into June, so more than halfway through the year.
So check in, I guess, with our goals is kind of the main concern here, and give a little bit of a status update, see how we're doing here.
We can go down the list, but, actually, I don't know where to filter this… Yeah, actually, leave it. By things that are closed. But, looks like we're making some progress.
I definitely can, maybe we can stop in on just, like, the top 5, epics, and then we can follow up, any sort of updates. I know the, stable OB, 1.0 release is definitely a work in progress. We're making a lot of really good goals on, the configuration stabilization.
Moving towards the V2, telemetry stabilization, I think, is, still a work in progress, but I think we're pretty far along on this one. We're thinking a lot in the semantic conventions.
documentation still in these updates. Correctness and stability, I think, is the other one I wanted to kind of mention. There's definitely a lot of issues and, work being done to.
find bugs and, address them. Still, I think there's a holistic look into all the existing issues and, classification, but yeah, that's, I think, still to come.
So, yeah, making progress on this, it's a big one, but yeah, slow and steady on this one.
Additional protocol support. This is, something that Mark and Nimrod are attached to, but, there's been a lot of work from a lot of other people.
Any updates on this one?
Stephen Lang 00:04:45 Mark is out for a few weeks.
Tyler 00:04:48 And… sorry, I'm looking to see if Nimrod's on the call as well.
nimrodavni 00:04:52 I… I don't think I've progressed in anything here, I don't… I think… There was a lot of, progress with GenAI stuff.
But besides that, I'm not sure what else.
Tyler 00:05:09 Yeah, there's the SunRPC stuff, right, that Mike is working on.
nimrodavni 00:05:14 You can even add that.
Tyler 00:05:15 Yeah. Mike, is there an overarching issue for that?
Nikola Grcevski @ Grafana / OpenTelemetry 00:05:19 Mike is not yet on the call, I think. Oh.
Tyler 00:05:25 Okay.
Nikola Grcevski @ Grafana / OpenTelemetry 00:05:27 Wait for me.
I think we should just add it to the list, to be honest.
Tyler 00:05:32 Yeah, yeah, I don't see a… okay, cool.
Get outta here.
Nikola Grcevski @ Grafana / OpenTelemetry 00:05:41 I mean, yeah.
That's almost done, I don't know if you want to click it.
Tyler 00:05:47 Yeah, right?
Nikola Grcevski @ Grafana / OpenTelemetry 00:05:48 Okay.
Tyler 00:05:50 Gotta, you gotta… gotta have some goals, right?
Yeah, okay, cool, right. Well, if that's the case, then we can keep following up on this one.
I don't know if there's anything else on this one. Redis… Nikola Grcevski @ Grafana / OpenTelemetry 00:06:02 Fine, that's one little institute.
Tyler 00:06:06 Okay, cool.
Alright, next up would be the support for .NET. This is something Rafael had been taking a look at. I know there's been a lot of refactors, on this one as well.
Don't know if there's any updates.
Rafael Roquetto 00:06:19 No much progress there yet.
Tyler 00:06:22 Cool. Okay.
Rafael Roquetto 00:06:25 It will be, it will be.
Tyler 00:06:27 Yeah, yeah, yep, sounds good.
Next up, the OTEL API SDK integration.
This is kind of interesting. I didn't think about talking about this one, but .
Nikola Grcevski @ Grafana / OpenTelemetry 00:06:38 Yeah, that's me. I haven't actually had a chance to make a progress on this yet, or the stuff I wanted to do, but, There's still time, so I'm hopeful that… A lot of stuff will get done.
Tyler 00:06:51 Yeah.
Yep.
Nikola Grcevski @ Grafana / OpenTelemetry 00:06:53 And we should add the stuff you're doing now with supporting the Better Goal Manual spans, yeah.
Tyler 00:06:58 Yeah, that was… exactly.
Nikola Grcevski @ Grafana / OpenTelemetry 00:07:00 It's already there.
Tyler 00:07:02 Oh, it is? Okay.
Nikola Grcevski @ Grafana / OpenTelemetry 00:07:03 I mean, there's some manual spend mentioned, but I think it should probably mention, yeah.
Tyler 00:07:08 Yeah.
Yeah, I'll just put it like this here.
It doesn't really tell you what it is, but… Okay, I'll remember that one.
But yeah, I think this is another one where we can continue adding, Support. Obviously, there's a lot of really great things here as well, but, Yeah, so, work in progress on this one still.
nimrodavni 00:07:30 I have, I think I sent it in some channel, I'll try to send it again. I have a… an open spec, and basically… following up on the process context sharing, allowing, instrumentations to share, like, resource metadata that foreign had a POT of, I have suggested… instrumentation… like, the instrumentation to share all the registered instrumentation data, so we can get, for example, if an instrumentation… if, like, a process is sending gRPC spans, and HTTP spans, and whatever, and, like, list that, so OB can work in… like, the, we won't just turn off instrumentation for a process that sends Telemetry will just, like, fill in the gaps of what is not sent. I'll try to find the… issue, I think Florian and some other people commented.
And if anyone wants to take a look, I just sent it.
Tyler 00:08:37 Okay. Let me see if I can pull it in here.
Nikola Grcevski @ Grafana / OpenTelemetry 00:08:42 That would be great if that happens, that would be awesome.
nimrodavni 00:08:46 Yeah, I think that… I think they're for it, generally, I think just of, An idea of how to, Like, if this should be an extension of the protocol, or should be fitted in inside the… the, like, generic attributes that you can send there?
And then we just need to, of course, implement it, or, like, have the… because I don't think this protocol is implemented.
In a lot of instrumentation. I know Evo is, like, the leader of it, and he had, like, this, like, POC implementation in Rust SDK.
But once, I think most SDKs will implement it, I think we can… and I think there's a… like the OTIP itself, maybe it's more… Yeah, like, more descriptive, if anyone wants to have a look.
Tyler 00:09:36 Is this the OTEP that, resolves? Oh, 2 weeks ago. Okay, cool, yeah.
nimrodavni 00:09:41 Yeah, so this is, like, following that issue, and we can, Yeah, basically some discussion there from Florian, some other people, if anyone wants to have… More looks and more opinions is, definitely great.
Nikola Grcevski @ Grafana / OpenTelemetry 00:09:59 Very cool.
Yeah, that's…
Tyler 00:10:02 Great, yeah.
missed this, in my wave of notifications, but yeah, I'll definitely take a look, so, yeah.
Nikola Grcevski @ Grafana / OpenTelemetry 00:10:08 Yeah, I wanted to mention this one last thing there. So, this is sort of completely tangential to this, but there's a lot of push. If you read the comments here, they're working on replacing the core of many SDKs.
for performance reasons to a C-based wrapper, so I think Ruby's on target, and Python.
there seems to be, like, a desire to create a CABI that you can actually build OTEL instrumentations for these languages, because I think, the proposal here reduces the Python overhead by 40%.
So… If this happens.
Now, it would be super easy for us to add manual spans for other languages, because in C++, we can put UProbes in there.
Just like we can put for Go.
Tyler 00:11:01 Oh, I see. And integrate with, yeah, with the SDK, yeah, that'd be great, right? Yeah.
Nikola Grcevski @ Grafana / OpenTelemetry 00:11:05 Right, so then the SDK is just, like, totally eBPF-enabled, out of the box.
if this actually materializes. Seems to be a lot of support from the community.
here to actually make this happen, because the overhead, I think, is just massive.
this proposal is for Python, but I think there's a similar one. They're saying that Honeycomb actually has the same thing for Ruby.
Tyler 00:11:31 Okay, yeah, interesting.
Yeah, that's really interesting.
Okay, cool, I got that documented.
Please take a look. If folks are interested, please comment on it, as well.
And yeah, we'll… we'll keep this… keep this train rolling.
Last up is the improved integration test quality. There's been a lot of work here as well. I guess the main question on this one is actually probably what's the acceptance criteria on this?
Stephen Lang 00:12:04 Yeah, this… I have a bunch of work locally that I haven't, made the effort to push any of this up, so I need to kind of finish this off.
But yeah, this… There's quite a lot here, so I don't know if we want to scope this down a bit.
I couldn't.
Tyler 00:12:22 Yeah, I think… I think having… You know, we did talk about this, like, preferred Docker test stuff as well.
I think this has probably just been dated, at this point. Yeah, maybe it just needs to get, I think, cleaned up.
Maybe pared down, maybe redirected, but yeah, I think… Steven, if you don't have permissions to edit this, please let me know, and I don't know if I can make that possible, but… I think you should. If not, then yeah, I'd love it if you could maybe, just do a refactor on this, it'd be great.
Stephen Lang 00:12:54 Yeah, let me take a look.
Tyler 00:12:56 Okay.
Yeah, a lot of great work on this, and I think that also, like, maybe this doesn't really capture all the work that's already been done as well, so… Maybe we could also try linking some of the issues in the PRs, to show the progress on this, because I think, honestly, I don't know… It's a moving goalpost right now, so… Yeah, we can nail it down, yeah.
Stephen Lang 00:13:17 It looks… it looks like I can edit it.
Tyler 00:13:19 Okay, perfect. Okay, cool. Alright. Sounds good.
Okay, we are kind of at the time box that I was looking to go for, but I wanted to just pause here.
For the remainder of these, are there anything that are miscategorized, or you wanted to comment on, or other things that, like, need attention?
Mario Macias 00:13:43 I can do a super quick, update. This open telemetry… these two tasks related to network attributes. Yesterday, we… we had a… or we met with… in the… in the network seek.
And we have now a roadmap to work in the next weeks about network or the financial anti-convention for network metrics.
Tyler 00:14:09 Awesome. Oh, okay, cool. Yeah, that's super exciting to hear that the networking, working group got kicked off. I know there's a lot of talk around this one, so that's… yeah, I think, it's bubbling up throughout the rest of the community, having some sort of network metrics in Opie. So, yeah, this is phenomenal news to hear. Thanks for sharing, Mario, yeah.
Cool. Any other, top of mind things that are actually, you know, important things to bring up here that you're working on?
I guess Mark's gone. Support Python async context?
Propagation? I guess that's still a workforce, okay.
Nikola Grcevski @ Grafana / OpenTelemetry 00:14:47 I think that's done, to be honest.
Tyler 00:14:48 I thought so, too. Okay.
Nikola Grcevski @ Grafana / OpenTelemetry 00:14:51 I think it was just some examples we needed to kind of confirm, based on the last comments.
By Aaron, but… I… I think most of the stuff works, I think it's…
Tyler 00:15:10 Yeah.
Nikola Grcevski @ Grafana / OpenTelemetry 00:15:11 Yeah, so if the revert in the Ubicorn happens, I don't know if… there's no PR here, but we can follow up. If that happens, then Ubicorn will work out of the box.
So, I think this is done. I don't think we have any work remaining, but…
Tyler 00:15:28 Yeah, okay, let's… let's, button this up, and then, yeah, I think maybe just close this issue, at that point, once we can confirm.
But yeah, that's… I thought so as well, I thought we were… thought we were done.
Nikola Grcevski @ Grafana / OpenTelemetry 00:15:40 seems to be for the.
Stephen Lang 00:15:41 Runtime metrics number 15 is now in progress, I believe.
Tyler 00:15:46 Oh, cool, awesome.
Nikola Grcevski @ Grafana / OpenTelemetry 00:15:48 Nope.
Tyler 00:15:49 Is this.
Nikola Grcevski @ Grafana / OpenTelemetry 00:15:51 That's true.
Tyler 00:15:52 Who's… this is, Mark working on this call?
Stephen Lang 00:15:54 This is Mark, but he shipped to go.
Tyler 00:15:58 Yeah, right. Okay.
I'm gonna add Mark on here as well, I guess he's gone, but .
Nikola Grcevski @ Grafana / OpenTelemetry 00:16:06 Yeah, he's gonna be away for the next three and a half weeks, so… Okay. But that's started. At least for Go, it's there. I think we need to add other languages. It's gonna take a while.
To do everything properly for all languages, but… I think… Yeah.
Blow and Java are the primary ones, there's a lot of work there. The rest don't actually have that many runtime metrics, I believe.
So… It'll be easier for the rest of the languages.
Tyler 00:16:34 Yeah, Java's the one that kind of worries me. Yeah.
Yeah.
Nikola Grcevski @ Grafana / OpenTelemetry 00:16:39 No, I mean, yeah. I mean, we can… we can at least produce the GC metrics. I think that should be easy. Easy. I mean, famous last words, but… I think if we want to get, like, number of, like, objects and heap reaches and stuff like that, and allocations, I think that probably the only reasonable way to do that is using our tiny agent, open a JMX connection to the JMVM, steal that data, and ship it over to the eBPS side, or something along those lines.
Yeah.
Tyler 00:17:13 Yeah, especially if we wanted to try to, like, maintain, like.
board-facing changes that come along with that as well, it's gonna be… Nikola Grcevski @ Grafana / OpenTelemetry 00:17:21 Exactly. But at least, I mean, I think for the JVM, I personally think the most important one is to be able to find the GC times. A lot of Java developers care about that deeply, and And if they see elevated GC time, then they can fire up a profiler or something and figure out what's going on.
Yeah, absolutely. Absolutely.
Tyler 00:17:46 Okay, cool. There's a lot on the agenda, so let's keep this… this train moving.
If you have more things to add to the goals or updates to the goals, please go ahead and do them asynchronously, and I'll try to add, like, maybe a little status update after the end of the meeting.
Okay, next up, Mike, you want to talk about the RPC metrics for attribute labels across multiple systems? Something that came out of your Arson RPC, PR here?
Mike Dame 00:18:10 Yeah, so this isn't about that PR itself, but kind of the issue that we found in there, where, we started to talk about it last week, we're kind of running out of time, the, adding a new RPC system.
kind of puts us in a weird spot with how our… our RPC metrics are right now. So we… we export… these RPC client duration and RPC server duration metrics, which are really… can apply to any RPC system.
But as part of the attributes or the Prometheus labels that we have on it, we have, I think RPC method, RPC system, and then gRPC status code.
I did some looking into the SEMCON for it, and well, I guess first off, the problem is that gRPC, that status code, attribute.
From the first case.
when I add a new system like SunRPC, or we've talked about JSON RPC too, any of them, those aren't going to be using that attribute, but we can't just, like, conditionally not export it, and then sometimes do. It doesn't work with the Prometheus histograms, seems to be the problem there.
So, it goes the other way, too. If we want to add attributes for another system, like SunRPC, that has, you know, whatever values we want to export, that would then get dropped into any other RPC system that's instrumented, and it's all falling under this, like, generic RPC, you know, client duration.
Server duration metrics.
So I looked a little into the semconf for it, and to me, I don't think that RPC, the gRPC status code attribute is actually supposed to be a metric attribute. It seems like it's just a trace attribute in the gRPC semconf.
Looking at the gRPC semconf for metrics, it just says defer to the general RPC metrics, which uses, like, RPC status code, like a generic one that could apply to any of them.
So yeah, this is… yeah, so right here, it just says, just follow the semantic conventions for RPC metrics with the system name, so… I'm thinking that we should, probably… I know this would be breaking, but either remove or have, like, a migration flag or something to… take gRPC status code out of those metrics and use rpcresponse.statuscode, the generic one that any system that we use could use.
There's been the bigger question of, do we even want to have gRPC status code as a metric attribute? If we do, is that going to be controlled under a flag? Like, you know, do you only want to do it if there's no other RPC system instrumented? What if you're trying to instrument multiple RPC systems?
My reading of the SEMCOMS seems like it shouldn't even be a metric attribute at all.
Nikola Grcevski @ Grafana / OpenTelemetry 00:21:10 No.
Mike Dame 00:21:10 But… Nikola Grcevski @ Grafana / OpenTelemetry 00:21:12 Thank you, I agree.
Mike Dame 00:21:13 I'm gonna bring it up to see what people think.
Nikola Grcevski @ Grafana / OpenTelemetry 00:21:15 Yeah, I agree, I think it should just switch. I mean, that's a bug, or maybe didn't exist at the time, who knows, like…
Tyler 00:21:21 It's a… yeah, it's a historical…
Mike Dame 00:21:24 Yeah.
Tyler 00:21:24 They used to… yeah, this was corrected, like, many, many old SEM conversions.
Mike Dame 00:21:28 Right. That's… I should have mentioned that, too. When I was looking through the SEMCOM, like, the RPC SEMCOM pretty recently moved to release candidate stability. The version that we're on, I think it's 38, was still under development, so things have changed. Yeah.
It's totally possible, so… but if we want to… like, OB's not stable yet, if we want to try to get this aligned before stability, then we can just make the… the switch, People can use collector processor.
Nikola Grcevski @ Grafana / OpenTelemetry 00:21:57 Yeah, exactly. Yeah. Yeah, I would say just switch it. Don't worry about backwards compatibility. I'm not even worried about bail on any of those.
Honestly, like, this is a bug, in my opinion, and we always try to be, now that the spec is… Actually, so if you see, there's the deprecated field, it should no longer be there.
Mike Dame 00:22:17 Oh, yeah. I didn't even see… I didn't even come across this page, yeah.
Nikola Grcevski @ Grafana / OpenTelemetry 00:22:20 Yeah. It used to exist, and that's the one we supported, but obviously it's not great for metrics.
Mike Dame 00:22:28 I can take this, then, if you want. I'll make an issue, its own issue, to, like, describe it, and then I won't even touch this in my SunRPC PR. That's kind of what me and Tyler decided was, like, I'm not gonna mess with it here. Okay.
So, yeah, I'll, I'll take that to switch that, and then that'll actually clean up the changes in S on RPC, too, because I had to do some weird, like.
Nikola Grcevski @ Grafana / OpenTelemetry 00:22:53 I couldn't…
Mike Dame 00:22:55 I had to report, like, zero status code for everything under it, and then that's just gonna mess with, you know, if you've got gRPC and sound running in the same system, or any other, you know, it… It's weird. I'll do this first, and this is a higher priority, I think, for the project, so… I can take that.
Tyler 00:23:12 Yeah, thanks, that's great. I think cleaning this up. This comes back to our top-level goal of stable telemetry as well, so… Nikola Grcevski @ Grafana / OpenTelemetry 00:23:19 Yep.
Tyler 00:23:19 This is… scrape.
Okay, thank you. Awesome.
Okay… Got a path forward on that one. Next up, Nikola, you wanted to talk about, Hybin is proposing increasing the limit… this is, I'm guessing, the message size for Gen AI, yeah. This is… Nikola Grcevski @ Grafana / OpenTelemetry 00:23:37 Yeah, I think he somehow missed a meeting. I think he said he was gonna be here, I think, on the channel, but it's midnight for him, so I think it's totally… Possible, like, things happened, and… Yeah, I think we I sort of, like, learned about this feedback, a lot of the… request and response bodies for some of these G9 requests are really large, and our current limitation is 64K.
So to support them properly, if we wanted to do the full spec thing, we're gonna have to kind of go beyond that.
Yeah.
Essentially, that's, That's pretty much the gist of it, and I think I've been has a plan of how to achieve this. I think my main, difficulty would be if any of the individual chunks we see on the kernel side are bigger than 16K, but I think… I'm hoping that most of them will be below.
Then we just reassemble in user space, and support this large streaming, yeah, packets.
Steven, I mean…
Tyler 00:24:51 Seems reasonable. Yeah, oh, that's what you said, too.
Mattia Meleleo 00:24:56 I read this, but it's not clear to me if the proposed solution is to just increase the numbers of the maximum packets, or… To have a different infrastructure for sending the data to user space. It's not that clear to me.
Nikola Grcevski @ Grafana / OpenTelemetry 00:25:17 Yeah, I… my guess is that one is exceeding the size, so… to support larger requests, but I think they also have this streaming, Kinda like… This is some form of requests where they stream, and I think for that we'll need some sort of different infrastructure. But there's two sort of separate… things, I think.
I mean, it would have been better if, Hybean was here, but, yeah.
Endre Sara 00:25:45 Alright, let's the capital a little This is fascinating, Nicola. I am using a bunch of streaming stuff, and I think that maybe if I'm reading this correctly.
These things that are coming in through the different streams are not necessarily part of the same request, so the point is that you not just need a bigger buffer, you need to be able to pick up multiple requests and somehow reassemble them.
Okay, very exciting.
Nikola Grcevski @ Grafana / OpenTelemetry 00:26:15 Yeah, I think it's gonna be able to do everything in user space. I think it's just a matter of… Not jumping the gun on individual requests, but maybe kind of figuring out that this is something that, could be done.
Here's a space.
I don't know, let's see the PRs, let's see the issues as they come through, and we'll…
Tyler 00:26:43 Yeah, I mean, I think that's kind of the key. To your point, Mattia, I think you are right, like, the way we actually pass this user space is gonna have to be restructured in some place, right? Like… you have to signal somehow that, like, this is an incomplete message that needs to get reconstructed in some way.
Mattia Meleleo 00:26:58 Yeah, but we need to know if this is a streaming connection. We need to see the headers in a BPF, or somehow classify them in a user space and handle them differently from the next bucket. I don't know, let's wait and see what's the approach.
Tyler 00:27:16 Yeah, I do think… yeah, agreed. I think there's some engineering challenges here, but I think that the idea alone is worth pursuing, so, yeah.
The colleague agreed on that.
Okay, cool. Yeah, well, we'll… I'm excited to see the PR stuff.
Yeah.
Okay, next up on the list, Roy, you want to talk about survey mode requests. This is the follow-up from last week, I'm guessing, when we were asking for a feature request on this?
Roy Reshef 00:27:40 Yeah, so there is one. I just shared it. I created it yesterday, got some feedback from Nicola.
like, an implementation plan, and I understand it… it will need to be done in, kind of, phases, because, There is a current functionality in Bela, and there is things that I at least would like to see changed, or modified, or added.
So, if you scroll down to the… I mean, first, it would be nice if we get to… if I get more feedback on the feature request itself.
I may have missed something, or maybe people come from different point of views that they want to see as their attributor, or something like that.
I do not know exactly who can provide such, such feedback, but, It'll be nice to get some.
And… and yep.
Tyler 00:28:40 So do you… do you currently use the survey mode when you're doing these, case in place resizing of resources?
Roy Reshef 00:28:47 Well, this is a use case. The thing is that, for example, when you want to do in-place resizing.
If you're touching container limits, especially memory, you would like to know what is application runtime that you're dealing with, because in some cases, you don't want to do in-place resizing.
Especially for JVMs and the like. This is just an example of the… Usability of this, where it can be used.
Yeah, many, many other…
Tyler 00:29:17 Mrs.
These are the kind of things that I was, like, really hoping to get a better understanding of, of, like, what does this… what does this part look like? Like, these are really good prescriptive, like, asks, but understanding, I think, this provides more of a holistic view into, like, what feature we're trying to actually provide here.
Damn.
So, yeah, I mean, I guess, like, I guess it's more about just understanding that challenge, better, is the thing that I was missing before.
Roy Reshef 00:29:44 Okay, I can try to come up with, or to describe here more use cases. I mean, this is, like, the end goal. The thing is that when you are observing, at least where I come from, from the ecosystem of resource optimization.
So what we do, we try to optimize both infrastructures and workloads.
Which boils down, in a lot of cases, to their requests and limits, because that I mean, that's how you do optimization. If you can shrink those, you can put more workloads on your node and the like. One of the mechanisms is to do it with in-place resizing, which is a feature that was graduated in Kubernetes recently. Not graduated, sorry, made generally available.
And… but again, that doesn't fit for all workloads. Depending what your application runtime is.
Some workloads will react better to it, and some will not react, or for some, it could even be dangerous, for that matter.
Tyler 00:30:53 Right.
Roy Reshef 00:30:53 That's where…
Tyler 00:30:54 It's more about, like, finding what those workloads actually exist, or what they are, right? Yeah, what they are. Yeah, what they are, yeah. Yeah, yeah.
Yeah, okay.
Yeah, that kind of stuff is helpful.
Roy Reshef 00:31:05 More than this, in… Some cases you would like to know, these are different use cases, not only the runtime, but also its version and its all kind of runtime parameters or runtime configuration. That especially applies for JVM workloads.
Because JVM has, I do not know how many… I mean, it was just mentioned now, runtime metrics. JVM has… a handful of garbage collection mechanisms. Each one of them can be configured with different parameters, and in a lot of cases, you want to know what these parameters are.
Because… This is actually what would limit… it has… It has to do either with memory management or with CPU management.
So, for example, if your max seep size is a certain number in… for JVM workloads.
There's not much point in bumping up your memory limit if you… because you cannot change this one.
So, these kind of things. That gives you more, from the application runtime point of view, what are the actual limits of… I mean, I can try to describe more use cases for that. That's fine, no problem.
Tyler 00:32:26 Yeah, that'd be great.
Cool, this is great, though. Great, we have it tracking. So yeah, we can keep referencing it.
Awesome. Well, thanks for opening it. Let's… let's continue on in this one. Yeah, this is a cool feature, too, so… sounds like… Seems like everyone's on board.
Okay, next up, Nimrod, you wanted to ask about, the next release. I pulled this in from the milestone itself, all of the open issues and PRs that are still, blocking it.
So, maybe we can just go through some of these really quick.
And, see where we're at here.
Okay, cool, so there's a bunch of bugs that are still open, that would need to get resolved. There is, cloud Node metadata is exported to Prometheus and OTLP without sensitive… or sensitivity filtering.
Don't know about this one. I've taken a look at it, I don't know what to do on this one, honestly. I'm still thinking about this, but I don't know if others have thought about it either, as well.
it seems kind of rooted in, like, the idea of Prometheus. We're dealing with this as well in, like, the Go world, around, like, what Prometheus is actually exporting.
So, I'm not exactly sure the right answer here, but… have taken a look at it.
Yeah, so, definitely need some thought. In-memory PID cache is never cleared. Unblocked PIDs. This has a PR, it looks like.
Yeah.
Oh, that's right.
I think this is the one that I saw… oh, no, no, no, okay, it got opened here as well. Blockpit…
nimrodavni 00:34:13 I think that one is.
Tyler 00:34:15 Yeah, that's right, it's on his fork. That's… okay.
I had mentioned… okay, yeah, thanks for pointing that out again. I think this just needs to get reopened, But it looked pretty straightforward, so… Yeah, okay.
this just needs somebody, I think, to follow up on, at this point, because I asked last week and nothing's been done. I think it was just a little mistake on that one.
Okay.
The next one is the failed SSL read, so it flows into the protocol parsing.
This has a PR open for it, I guess… oh, yeah. I think, Raphael, this needs another look from you. This should be ready to go. I addressed all the things that you had asked for, so I think I did, so it just needs another review from you at this point, but this is something that should be unblockable.
Rafael Roquetto 00:35:01 I'll have a look this morning. Here.
Tyler 00:35:03 Cool. Awesome.
So that would address this one. Timeout does not, cancel block Java execute, extraction.
I also took a look at this one. This one's, I think, a little bit more complicated.
Yeah, there's, like… I think we can handle, like, timeouts, but the actual, like, full, if I remember correctly what I wrote here, there's a lot I think we could do, but it would involve a lot of digging into the Java internals. Essentially, make the Java, attach our context aware, I think is kind of… it's a bigger step. I'm happy to take a look at this and work on it, but I don't think that it's gonna be, like, a quick… 50-line PR kind of thing. But it was on my list of things to do. I think it just needs some, like, major… more major refactors than, like, a bug fix, was kind of the key here. The idea being that, like, if you have a lot of these, calls coming in really quick, it'll actually overload the thread pool, and there's not… like, especially if they're being canceled really quick, like, it'll just hang all those processes, so, yeah, it's… it's… it's an edge case. It's definitely not a common case, but it's still, like, one of those ones where I think if we are able to pass in along this, like, so we know, like, the contact's been stopped, that, like, the call has stopped, if we can just pass that along to the Java world, it should… it should clean things up, I think. It's just… working in.
Nikola Grcevski @ Grafana / OpenTelemetry 00:36:30 Yeah, that… that JVM Tools repo sits in Grafana now, I mean, it doesn't have to sit there if we wanna… we wanna move it over to Optel.
That's without it, too.
Tyler 00:36:39 Yeah.
Okay, that was my… yeah, I guess that was my question for you. I'm happy to do that, like, in a PR, just move it over, and then we can… Nikola Grcevski @ Grafana / OpenTelemetry 00:36:47 Yeah.
Tyler 00:36:47 I don't think that out there, so… Nikola Grcevski @ Grafana / OpenTelemetry 00:36:49 Yeah, absolutely, then. We are free to modify it. Yeah.
Tyler 00:36:53 Okay, cool.
Okay, I will… we can… I'll follow up on this one just while then.
Avoided services, avoided services has unbounded service identity cardinality, I think I've taken a look at this one as well… 2037?
I thought there was a PR… No, this is one, yeah, where it was just holistically.
I do think that this is important to take a look at, and then, Nimrod, I think you make a good point here that this is, like, pretty common for a lot of metrics we have, I think this is kind of an important point to make, because we do want to be careful about the cardinality we're actually exporting on these. It's pretty easy to overload backend systems, and the semantic convention groups are… very key about this, and making sure that, like, attributes or metric names or something like that are not gonna, like, overload, the cardinality limits of particular things. So, I do think that this is important that we probably do want to, like, follow up and take maybe a holistic look as to, like.
all of the things that we're exporting, and having them opt-in, or having them use some non-unique identifiers, super unique identifiers that can't be templated out, I think is kind of a key thing.
That being said, I don't know… Maybe this is just worth starting here, and picking off one of them, but maybe I'll… maybe this also includes doing a little bit of an audit and finding other things that, like, we could actually address here.
I think for the longer… Story, this would be related to that telemetry stability thing, like making sure that we… the telemetry we're producing is… is going to, one, conform with semantic conventions, but also If we do have things that aren't in semantic conventions.
Be… define them in a way that are cardality limiting in some way.
Or have controls over it.
But yeah, another one to take a look at.
Http, preface skips shifts shift's pointer without shrinking its length.
Let's see… where are we at on this one? 2040.
Yeah, I took a look at this one really quick as well. I haven't actually put in… Fix for this… I thought, wow.
Actually, I didn't put a fix in, I thought maybe because somebody else was working on a fix, maybe it's just not linked.
Maybe not.
Okay.
I'll have to take another look at this, or somebody else, if they have time, I think it's worth taking a look at. I thought there was another PR for this.
But, I've looked at a lot of these at this point, so I'm getting a little confused. But yeah, I could've swore there was a PR for this, or maybe I just had a PR waiting and sitting on a branch somewhere. But, Okay, that's worth taking a look at.
Progressing, this is another follow-up issue, I think, that, Nikola, you opened, wow, it's almost a year ago. Document the new selective, telemetry and Sampler.
This was still in the milestone.
this conversation.
Yeah, I think this is just… Hmm.
Nikola Grcevski @ Grafana / OpenTelemetry 00:40:16 I don't even remember what this was.
Is it just documenting?
Tyler 00:40:25 Yeah, it says it's links from here… That's not really that helpful.
Nikola Grcevski @ Grafana / OpenTelemetry 00:40:32 Damn, we haven't documented as a sampler, how you can actually choose?
Stephen Lang 00:40:36 Was it based on whether you could choose.
Nikola Grcevski @ Grafana / OpenTelemetry 00:40:39 Yeah.
Stephen Lang 00:40:39 Like, what type of signal? Like, metrics or traces per service?
Nikola Grcevski @ Grafana / OpenTelemetry 00:40:44 Yeah, that's not documented, yeah.
I…
Tyler 00:40:48 I might… pause on this one and just close it. It was not planned, given the V2 configuration stuff is being done as well.
So yeah, let's just… maybe just close this for now.
Nikola Grcevski @ Grafana / OpenTelemetry 00:41:00 Let us close it, yeah.
Tyler 00:41:14 Okay, document the application span… Hotel… This looks similar application span.
Stephen Lang 00:41:31 This is the feature, right, which is…
Tyler 00:41:33 Yeah, yep.
Stephen Lang 00:41:35 hotel span metrics.
Tyler 00:41:38 I think you're right.
I'm happy to follow suit on this one, unless you think this is worth… Including… Nikola Grcevski @ Grafana / OpenTelemetry 00:41:51 No, we can move it over. I mean, it's just saying what's the difference between application span, Application Span Hotel. One is… there's two formats.
They're slightly different.
Who knows?
Tyler 00:42:05 Yeah.
Nikola Grcevski @ Grafana / OpenTelemetry 00:42:05 Okay.
We can move it over.
Tyler 00:42:12 Moving over, meaning… Nikola Grcevski @ Grafana / OpenTelemetry 00:42:14 Yeah, push it to the next release, or… if you'd like to close it, you can close it, yeah.
Tyler 00:42:19 Yeah, I'm thinking probably just close it.
Given we have a lot of docs work on the Configv2 as well.
Nikola Grcevski @ Grafana / OpenTelemetry 00:42:24 Okay.
Tyler 00:42:24 But I'm happy to keep it open, too, if you wanted to… Nikola Grcevski @ Grafana / OpenTelemetry 00:42:28 Let's close that. Let's close that.
Tyler 00:42:43 Okay, documentation for parent-child association limitations. This is something that was asked by David Ashpole.
Yeah, a few others at KubeCon.
coming up on the next one. So, I think it's just, like.
saying, like, given our heuristic system for understanding, like, trace context propagation, like, what… what things… where are the edges of it, and just having this documented. I don't think this is actually too hard.
Nikola Grcevski @ Grafana / OpenTelemetry 00:43:14 I created a draft, I… Long ago, oh my god.
Tyler 00:43:20 Yeah… Nikola Grcevski @ Grafana / OpenTelemetry 00:43:22 I do have a draft, and it's just not up to date, because we've since then fixed Java.
It's been a while.
Okay.
Yes.
Tyler 00:43:35 Maybe just an update here, yeah.
Nikola Grcevski @ Grafana / OpenTelemetry 00:43:37 Yeah.
Tyler 00:43:38 Oh yeah, just needs an update.
Nikola Grcevski @ Grafana / OpenTelemetry 00:43:40 Yes. Java, then… I think Python async now works, so…
Tyler 00:43:45 Oh, yeah.
Nikola Grcevski @ Grafana / OpenTelemetry 00:43:46 Yes.
Tyler 00:43:46 Yeah. Yeah.
Well, if we can try to get this in, I could do my best when I'm doing releases and updating docs to try to keep this up to date there as well. Okay. I mean, I could also fork this if you want, and I can try to just do those updates, if you don't… Nikola Grcevski @ Grafana / OpenTelemetry 00:44:03 I don't have time. Yeah? Yeah? Okay. I mean, like I said… One more week, I think, is probably… At least for me, for that, I think.
I'll go back to being more useful.
Tyler 00:44:16 You're doing great. I think that sounds good. If nothing gets done, then we can… Follow up in a week, something like that.
Okay.
Next up, eBPF agent saturates internal queues, sending queues full.
Mario Macias 00:44:54 Yeah, This… this was already fixed.
Oh. Months ago, and… Per your last comment in the issue, it was released in 07… in 07.1.
Tyler 00:45:10 Okay, so let's… See if you can find that.
Okay.
Perfect. Okay.
Then… blocked upgrades? I don't think there's any update on this.
There's a PR linked here, let's see if we can find it.
I guess Mattia's on the call, I don't know if you know…
Mattia Meleleo 00:45:42 Yeah, I don't think there have been new releases.
I can try to ask if we want it soon, but…
Tyler 00:45:51 I mean, I don't think there's anything blocking… Moving this, cause, like.
There's nothing, I think, in these new releases that we really need, from this library.
But if there ever becomes that, then yeah, maybe we can push forward on that one.
Mattia Meleleo 00:46:07 Yep.
Tyler 00:46:08 Okay, so this one can get bumped. Support receiver side span links from the Go, channel handoff. Yeah, this is something I'm also working on. We had talked last week, or the week before, I can't remember, no, I guess it would have to have been last week. This POC I had for supporting, links.
in, spans… using Go channels, is something that, like, I wanted to get in. There's been a lot of great work on getting this actually merged in.
I think we're pretty close, I have a PR, no, I don't have a PR, this is the, plan, yeah, so I think we're… I think if I saw this morning, this PR that adds, like, the channel linking, for the events.
Is merged, so really, like, the next thing is just to start actually making this work on the eBPF side, and then building out some docs for it, so we're actually really close on this, which is kind of cool.
One of the things that I did want to ask about is, like, what kind of, like… I didn't want to add to the config for this to turn it on and turn it off, especially if we're just going to remove that.
But I also wanted to know, like, what people's thoughts on, like, if this should just be on by default, did we want, like, a feature flag for this to sit behind? Like, I… I don't have too strong opinions, I don't think there's a lot that's actually gonna get impacted here, but I wanted to maybe just ask folks, like, features on, like, configuration here.
On how we wanted to enable or disable or not do any of that.
Or do, you know, eventually maybe some parsing, so certain links wouldn't get added, certain links would get added, something like that we could do.
I was more just thinking, like, turning it on by default, and then when users have feature requests for, like, hey, this is great, but I don't want this link, or hey, this is great, I want to annotate this link with some attributes or something like that, that would help drive the conversation there.
Nikola Grcevski @ Grafana / OpenTelemetry 00:47:58 Yeah, I agree. Let's turn it on, see what people say, and then they say, no, this is too noisy, or this is it, and then we… yeah.
Tyler 00:48:06 Just… yeah, okay.
Nikola Grcevski @ Grafana / OpenTelemetry 00:48:08 Cool, alright.
Tyler 00:48:09 Yeah, I'll go in that direction then.
Cool, yeah, I think if that's the case, then… I think we're… we're, I think maybe 2-3 PRs away from getting this in, so I'll try to get these out today, or start working on them today, yeah.
Okay, cool. And then, the only other thing is this, V2, configuration docs, so… This is also progressing pretty well, thanks again for all the reviews from folks. This is another follow-up, so… this isn't the one I was thinking about, but this is, like, actually, this is a good one to talk about. So this is one where I actually had missed something originally in our, dev docs. One of the things is, like, this is the HTTP, routes parsing. This… it is bi-directionally different, the way that the new Configv2, setup was, was that it was just a single way, and it was a global.
So this changes that from being… If I remember correctly… Oh, gosh, no, this is a different PR, sorry.
This is just adding docs for things that already exist. I totally forgot the stats stuff. So, yeah, sorry, this is just to clean up on the parities, so this is pretty straightforward. This is just missing docs that were already existing. The HTTP one has already merged, so… Okay. Yeah, this just needs, I think… I think I actually don't think it needs to be a review. It's pretty simple, it's just to clean up.
Nikola's had a review. If you want to take a look, otherwise I'll probably merge this after the meeting.
Totally forgot about this.
Okay, cool. And then… this… this is the one I was thinking of, Yeah, Mario, left a comment on this one.
this is, this is essentially, like, the conversion docs that we're working on for the V2. This is progressing really well. There's some feedback here about the current structure here with maps.
I was in the middle of writing a comment before the meeting, and I think this is a good point, like, I wanted to actually say, like, I don't think it should… that wasn't my plan to keep this in the long term, going with maps. The way I had structured this and tried to break this up, like, I needed some sort of, like, placeholder, so I'd put a map in there.
And then I just started building from the maps, but you're… you're right, like, my goal is to eventually not have, JSON parsing in maps, for the folks who haven't taken a look at this, I wanted to switch those out for actual structures. I don't think I have it listed in the issue to do this. I think I just had it in my mind that I was going to do this, and I don't know if I captured it well. But, yeah, I would like to do that.
I'd probably say this PR, once they take it out of draft, maybe we'll try to just get this merged to the last, for the export, PRs, if we could do it with just the maps this way, and then I will have a tracking item for the cleanup to actually switch those maps into, like, distinctive types after the fact. If you're okay with that, Mario, I'd like to go in that direction.
Mario Macias 00:51:09 Yes, yes, yes, I'm fine, I'm fine, it was just an observation.
Tyler 00:51:12 No, it's a good observation, and thank you for making it, because again, like I said, like, I don't think I actually wrote it down, it just was in my head, so that's not really great. So, yeah, let's make that explicit, and like, let's follow up on that. But yeah, I'm still… Noodling with this, as you can see, there's a little bit of… tooling, but I think it's… I think it's ready for a review. I'm just gonna put some comments on it right before, and then after the meeting, it should be up for review.
Okay, so that's up for the next, release.
folks that are looking for, items to help progress this and move this forward, there's plenty of issues here that don't have owners. If you are able and willing, please go ahead and take on one of those, that'd help move this forward. I do think we're coming up on close to a month since the last release. There's been a lot of really great stuff in this release, so I'm excited to get it out, but yeah, so keep working on this, I will keep working on them, as well.
nimrodavni 00:52:08 Yeah, my… I had the… a question regarding how much… Like, I don't know how much work we have, because it seems… I don't know, maybe we'll go through them quickly, but it does seem like a lot of issues, and maybe we can release some, like, patch, or something like that in the meantime, because I think there's a lot of… features that… are really great and we're missing, but I don't know, I think that's… Up to everyone else here, unless there's something that, like, we are really saying, like, we need this in the latest release.
But I'd love to hear your opinion.
Tyler 00:52:44 Yeah, I added, like, 20 bugs I was hoping to get done in this release, and they're still the ones that are not closed. I still would feel strongly that we try to get those, resolved.
They've been there since the beginning of the milestone planning, so I think I would like to prioritize those.
Given those were kind of, like, the focus that we had agreed on.
At the beginning?
But other than that, like, the configv2 stuff, I don't think that that's much of a blocker. In fact, I structured it in a way that, like, it shouldn't have any public API. So if we get all of the bugs done, and, like, the only thing that's blocking us is this Configv2 stuff, or, like, the Go Channel stuff, like… yeah, I don't… we don't need a block on that, but it's more about, I think, like, those bugs are kind of, like, the things that are, sticking out to me. Yeah.
nimrodavni 00:53:32 Okay, makes sense.
Liquid.
Tyler 00:53:37 Happy to have help on those, though, so if other folks want to jump in there, yeah, that'd be great.
I don't think that it's gonna take, like, another month, Nimrod, just to be clear. I do think, just based on, like, the velocity that we had in the past week, that we could probably get these done in another week or two, so, yeah.
Great. Because otherwise I'm with you on that, like, you can't just have no releases, so, yeah.
Okay, cool.
Next up, we are running low on time.
So… Nimrod, do you want to talk about the OCB support for the OB, stuff? I see you have an issue, exit sharing my screen again.
nimrodavni 00:54:18 Yeah, I'll try to be quick. I went on the collector SIG, and I think there was an issue I raised here about having, like, a OB slash eBPF collector distribution.
I forgot to link that issue, I'll do that later. But basically, they were all in general, for it, but they were still kind of… not, really liking the fact that you can't just build OB with OCB without any, like, script before that. So I… I talked with them, I talked to some, someone from Carlogix on the collector team.
And he told me, like, he, had… like, we had this idea of, basically, instead of downloading it from a Go module with GoGet, you just install it from the archive that you, like, the pipeline that we built.
And just having it as a different option instead of doing GoGet, you basically download the archive, verify it with SHA-256, cache it, and then just do, like, the replace. Like, that all happens behind the scenes, but you do it in, like, a declarative way.
And in that way, we can still continue our, kind of… like, we don't need to change anything in RCI. OCB just has this change, and we have a draft PR that's not such a big of implementation.
And I built OB, like, an OCB, collector distribution with OCB, and it worked, but I just need… You know, confirmation from them that that's, like, a… a good path to go with, like, I didn't think of any other way to do it without any, pre-built script, or whatever, and I think that's a… kind of a compromise? I'm just waiting to see if they… I opened it, like, just today. Oh, someone already commented, could… I didn't see it.
So… Nope.
Cool.
Rafael Roquetto 00:56:15 Is it… do you run into any kind of dependency problems if the OB dependencies don't match with the other, like, components around the OCB? Are you using? I thought the Go mod still need to be kind of compatible, but I'm not sure.
nimrodavni 00:56:30 I think that's… I think that's the same issue that you'll have if you build, like, if you do, I don't know, anything with, like, building it straight from Git, or, like, downloading it, and then doing make docker generate, or something like that.
I don't know if we… I think we already talked about something, and I think someone from Grafana already suggested, and Rafael said, you wrote in Slack that you were thinking about just packaging it as a binary.
Right?
Rafael Roquetto 00:57:03 Yeah, so for… for Grafana Loy, which embeds Grafana Baylor, the direction we're going is, because we run into a lot of dependency hell issues, we're… So, we're just going to pull in the actual binary from the GitHub release.
And wrap it as a sub-process. And then, you know, it gets mapped into, anonymous memory page, config, and everything, and we just launched a controller either. I don't know, not… maybe it doesn't apply in this case, or maybe it's not helpful in this case, but I just want to… to mention that idea, because… It could be an option. It could… could not, it could be an option, just… Just something… To be aware of.
nimrodavni 00:57:50 Yeah, that's interesting. I think we can, I don't know, I don't remember, there was something, like, in the OB recei… like, on the OBPR, that we added the receiver, I think we kind of resoluted that.
We're saying that it's…
Tyler 00:58:09 Yeah, I think…
nimrodavni 00:58:09 Such a big, like, conflict or something.
Tyler 00:58:12 The only dependency issues that I would see there actually may be two. Like, one is, like, the compatibility of the collector components, because they're not stable, so that can be an issue. But that, I think, is resolvable, especially as the collectors become more stable. I don't know if those problems exist, nearly as much, but, like, we would always want to be tracking the latest anyway, so… I don't know if I'd see that as a problem, as much as, like, a… just a… probably want to be following that. And the only other thing that I've seen is before, in, like, the collector contrib, it can cause performance degradations if you pull in packages, which is… bizarre, but that's, I think, for specifically when they're building a single binary, but, like, the OCB stuff uses independent modules, and that's, like, very different, where, like, the modules, they isolate the builds themselves.
So I don't know if there's too much of an issue there. I think it's more just, like, the collector components, like receiver components or something like that would be the problem I've seen, which has happened, and it continues to happen, but again, I think we would want to just keep going in that direction, so, yeah.
I'm a big fan of what you have here.
I'm kind of… it's kind of sad that Braden is not… but maybe I'll respond as well, because I do think that, like, it's not just Obi that needs this. I think that the profiler could also use this. I know that… I think they're committing their binaries, but… Any eBPF program, or anything that doesn't have, like, that has binaries in the source, I think could be useful here, but… Okay, yeah, thanks for doing this. I'm maybe also bringing in some other folks into the conversation here, like, that have approved this in the past, so it'd be good too, so…
nimrodavni 00:59:54 Cool. I'll try to… I'll also comment to him and try to get also more support for that.
Tyler 01:00:00 Yeah, yeah.
Awesome, and folks, if you would please maybe go take a look at the issue, and if you think it's great, Or if you think it's awful, go ahead and comment on it. I think just putting some activity there, would be great, just to show support.
But if you think it's awful, you may be in the wrong SIG meeting. But anyways, enough said. We're out of time. Good seeing you all. I think we have plenty of agenda items for next time. Sorry we didn't get to everything, we will definitely follow up on that. But until next week, I will see you all then, or asynchronously. Bye!
Stephen Lang 01:00:33 Alright.
