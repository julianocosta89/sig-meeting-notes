SIG: Arrow SIG
Date: 2025-12-03
Duration: 54 minutes
Zoom Recording URL: https://zoom.us/rec/share/O6dM-_Lyae1LGh3-saFof4d_5u_DpaJs1Gt82s5s0wUDEMvOAmT_G8GFtsQeIgr8._Xp9g-jHsrBiEJ-K
============================================================

## Zoom Recording Transcript

**Albert Lockett** 01:42 Hey guys.
**Joshua MacDonald** 01:55 Hello, hello.
Here we are.
Not sure we start this meeting hard at 4 o'clock or whatnot. I know that Laurent will be out this week.
See, 5 of us.
You can get started pretty soon, maybe not right away.
I actually have been entering some ideas for an agenda And I'll share my screen.
Can you all see my screen? I've had many problems with Teams today.
It's not even Teams, it's Zoom. Of course.
**drewrelmas** 02:36 Of course.
**Joshua MacDonald** 02:37 I'm having Teams problems.
Same problems, though.
Alright… Yeah, well, we can wait a minute or two or three, I'm glad to see us all together. Jake has got some typing… some new ideas for the agenda. By the way, my intention was to, like, put this open PR discussion towards the end. I, so that… so that new topics can come first. So I might… I might suggest we move these around.
So, I'm afraid that if I start talking now, I assume someone will join us immediately be confused, so I'm gonna wait a little bit longer.
Andres joined, hello, hello.
Yeah, so two weeks since the last, regular meeting here, I've been calling it a general meeting now that, by the way, we have I guess, a new meeting on the calendar. I didn't know we had that. I'm not sure we will always need it, but… There has been a splinter group.
called Query Transform, and apparently it's on the calendar.
And Albert and, Drew and company have been in that meeting. I haven't heard much… actually, I have, but I haven't, and I, so this is a new thread.
That, that I am… Placing a… placeholder for. Danny's joined us. Hello, Danny.
So now I feel like we have critical mass.
And… I see some good topics. While I start talking, Danny, let me ask you if you have something to put on the agenda. I would love to hear talking about those graphs that you shared with me privately, and I can say more, when we come to that.
So, I will start us off, following procedure. We're looking at two weeks of new issues, and I don't think we should talk about every one of them.
So, but the high level, that I'm… that I'm seeing from these dozen or so issues are that Albert's very good about filing issues for, steps he's taking with this new columnar query engine prototype.
That's a DataFusion-based query engine.
I and Drew have been filing issues involving Go dependencies and, the way that our Repo is managed, so we won't talk about too much about that. Drew and I have a conversation. If anyone needs to know, you can ask us offline.
In my work on batching, I've been needing more timer support than we currently have, and I hacked it in a kind of interesting way, but this is the issue asking for a proper solution.
And a few other things. So, Lalit had, from my team here, has contributed a view for, essentially a zero-copy export path, which is really great. Albert noted a few fields are missing, and so that's what, that's issue number 1475.
And, as part of this work on Query Engine, we've got, some… some new issues involving the prototype, non-columnar engine that we have, underway as well.
I don't know that we should dwell on any of this stuff, since there are so many good issues on the agenda. Does anybody disagree?
Alright.
So… I… don't feel like going in order here. I put this open PR discussion, new topics, that was a placeholder. I'm gonna move this.
And… that means… I… no.
That means… sorry.
I apparently am not having… Great day, there we go.
I've already given the note about there being a query transform subgroup. Now I know more about it. I will probably catch a recording. I want to know a little bit more about what's been said, and then we'll… we'll continue talking about that. But I don't have any questions at the moment.
As a reminder.
three weeks ago, we had a meeting on Thursday morning, which was well attended, and I promised to have another discussion about what we're calling Phase 3, which is like a roadmapping exercise for this project, like, past the current milestones, or past the current scope of work.
I particularly expect us to be talking about extensibility, how do we interoperate with Go, how do we plug these things together, how can we benefit from Rust without changing the entire world, and so on. Those are the type of topics I expect. I'm also interested in SDK integrations, and so on.
But that will be next week's Thursday morning.
So then, following the plan that's in front of us here, we've got a little note from Cijo, and I would actually like to turn it over to you right now.
**Cijo Thomas (Microsoft)** 08:09 Hello? Can you hear?
**Joshua MacDonald** 08:10 Hi.
Hello?
**Cijo Thomas (Microsoft)** 08:14 Hey, can you hear me?
**Joshua MacDonald** 08:16 I can hear you. Have I been talking to myself without hearing myself? I can hear you.
**Cijo Thomas (Microsoft)** 08:20 Yeah, I have a very small topic. I just want to see if everyone is okay, especially since we are about to start new phase, to update all the benchmarks to point to the one which we have from Phase 2.
If you look at the main report, it's all pointing to Phase 1 benchmarks, which is coming at least one year old one.
We've been running this daily and nightly and per-commit benchmarks for a while now. It's not… Like, it's not covering all the scenarios, but at least… Some scenarios are covered right now, so I want to, like, see if everyone is okay to… update the pages to point to it. I have a PR right now, I will send it shortly so we can review it. I just wanted to make sure if we are okay to start a today sync, that we are at the end of Phase 2 with benchmarks.
**Joshua MacDonald** 09:09 Yeah, I would say yes. I feel like we're kind of… I'm not saying we're at the end of the scope, but we're solidly through much of what we said we would do.
And we're on the tail end of it, for sure. I love seeing that, like, we really checked a lot of the boxes. This Data Fusion prototype is especially exciting to me.
So yeah, and I… so I think it's time to say that we're well past phase one at this point, and I think we can update anything on the website to say so as well.
**Cijo Thomas (Microsoft)** 09:38 Okay, yeah, I'll send a bunch of small, small PRs, to take it, like, one step at a time.
And in that year, I would like to discuss, like, what kind of benchmarks we want to highlight, because we have, like, in nightly, we have few, and on a per commit, it's a different one.
I also plan to propose, like, a few more kind of test we want to do. Like, right now, we are only doing, like, 100K RPS, and we measure how much CPU and memory, and they run on a single core.
Even though the machine we got from CNCF, it's an extremely powerful machine, so we should be able to run on multiple codes and prove that we are indeed scaling linearly as we expect. So, yeah, but those are details which I'll cover in PRs which I'll send, over the course of next day and two.
**Joshua MacDonald** 10:28 That's great. I think there will be, just nice to get a sort of baseline on there, and then, there'll be an opportunity to, like, refine which tests and so on, which measurements. I'm definitely interested as we move forward in having, like, a how-does-it-respond to load type of, like.
as you approach your load limits, for example, how well does it behave? Actually, Jake, I know you have an item on the agenda. In fact, you're next, and this would be, sort of tangentially related. You've been doing some testing on the Go Collector side, I noticed. You shared those results, and I… I've actually digested them at this point, and I didn't have the time to get back to you. So some exciting, or some confirmatory results from Jake showing, you know.
essentially that there are easy ways to make the Go Collector fall apart if you put too much load in. Some… the batch processor may be worse than the exporter helper, or so on, so there's a… there's… there's some… I'm interested in whether we get to where we can measure both the Go Collector and the REST collector, and, like.
Push them a little too hard, basically.
I think that'll be, nice if we can do it. One of our project milestones for Phase 2 was to do an evaluation of the Go Collector versus the pipeline we're building, and I think Maybe that's what I would like to see.
**Cijo Thomas (Microsoft)** 11:52 Okay, got it. So we are okay to add a, like, direct comparison against the existing collector.
**Joshua MacDonald** 11:57 I think… I think it's fair to do, yeah, and I… I mean… we should be honest about what we're cutting corners on, you know, like, we have a wait-for-result mode, and the Go Collector has that similar functionality. That would be a fair comparison.
If we turn that off, there's some differences in what we're exercising, but we're still trying to, you know, measure CPU per byte, or CPU per item, and those are relevant numbers, you know, relevant measurements, I would say.
And if the numbers are terrible.
Well, we'll see what we see. I don't… there haven't actually been a lot of improvements in the Go Collector, so don't be surprised if it's doing better than we expect.
**Cijo Thomas (Microsoft)** 12:35 Okay, yeah, I'll start, like, evaluating how to add the collector, because I believe, like, once we use the existing collector, it… just takes up the entire CPU, doesn't have the per-core or, like, core limitation, so we'll want to do a fair comparison by giving it, same amount of thing here. But anyway, those are details, I won't take up more time, so yeah, please move on to the next items.
**Joshua MacDonald** 12:57 both.
All right, thank you, CJO. So Jake… welcome, Jake. I know you've put together A topic, an issue topic here, and there's been some discussion on it.
Coincidentally, I don't think we have Lalit on the line, but we've been starting to look at auth as well. So, tell us what this is about.
**Jake Dern** 13:21 Yeah, so coincidentally, since you mentioned the, the load testing, my thought was this week, since I had already taken a look at ad hoc load testing, for the Go Collector, was that, well, since I already have the setup, and I've got a big Kubernetes cluster and all of the stuff set up to pump data that I might as well take the Rust collector for a spin and just kind of see how it compares.
And the first thing I was going to take a look at was the Parquet exporter, and I was going to try to hook that up to Azure with auth and, you know, a couple different storage backends. Fabric mirroring for people that know what that is, but then also just Azure Blob Storage and that kind of stuff.
So the first thing I ran into was, that I think only, like, local, you know, file storage is supported, and so I was gonna see about wiring up some config and auth options, just whatever object store supported, but… as soon as I started down that path, I realized, you know, it might have been a bit of a waste of effort, to go and support directly, like, the object store configuration model, because there was quite a bit here that would be reusable across other things if I wanted to support You know, just, like, generic, like, Azure token credential type abstractions, or similar things for, you know, the other clouds as well.
And then that got me thinking down the line of, like, well, there's also this auth extension thing in the Go Collector, which is kind of related to this, and… that sort of is the concept of, you know, you can define an extension, and if it implements some interface, like for HTTP or gRPC, then, you know, you can… you know, like, stick a reference to that in another component, and you can query it at runtime, and then you can pull it in and use that auth extension. And so I, you know, I was kind of just thinking along those lines of, you know, what would be the right way to introduce some code, basically to handle different credential types.
into the project at this stage. And, you know, I had a couple ideas, I wasn't sure if there was an existing, you know, kind of extension proposal available. I could always just throw some reusable libraries in the experimental folder or something for now. I also saw, Josh, as you mentioned earlier, that you guys have a little bit of, like.
identity handling code in, like, the Geneva, exporter that's kind of being worked on. So… that's basically the context, and yeah, if you have thoughts, I'll turn it over to you.
**Joshua MacDonald** 15:33 Sure.
I wish we had Lalit here. I know that he and I have discussed extensions in exactly this context of authing for Geneva, and I, So, as far as the work priorities, we decided that TLS would be more… more impactful and, like, more of a risk to start on, so… But we did talk about it. I will bring in, now that, one of my major involvements in the Go Collector has been learning how extensions work in that setting. I was… I added the middleware extension this year in the Go Collector codebase, which means I'm the last person to have added an extension in the collector, and I'm the only person that actually knows the the feedback that I got, I would say I'm the only person that knows. I've written a document, I think I've shared it to you.
So I do have a feeling for what exactly it means.
We already have this LinkMe crate being used to, like, statically register stuff and find those factories and so on, so it seems like there's a fairly trivial exercise here of just, you know, copying what we've done for finding components and just finding extensions. I can help when it comes to the point of doing all this, like, make the model consistent with the Go Collector and, you know, the concepts, the, the, like.
the idioms that we have there, like, you get a bag of extensions at startup, and you can name them, and you can search for them by name, and you can test if they implement certain extent… certain interfaces in Go, and so on.
And they have start and they have stop, they just don't have pipeline functions. So, so yeah, we will… I think we will get to adding extensions, It's… it's sort of a… I'm curious… it's a curious topic for me and Rust, because I do feel still a little bit inexperienced with Rust, even though I get stronger every day, but, like, the… what I've discovered working in extensions in Go is that, the meat of the problem is about compatibility as you change versions forward and backward. It's not really, like, it's not hard to statically register a factory and find it by name.
and make it conform to an interface, it's hard to keep that working across many releases and so on. So… OTEL has had many debates about whether you should frequently major version yourself so that, like, you just keep changing the APIs so that you can have forward compatibility forever, and… not worry about backward compatibility, or whatever it is. So… what I'm trying to point to is that the specific mechanisms by which we do extensibility tend to differ by language. I don't think I know exactly how to do it in Rust.
And I'm interested in what others might think about it.
But I don't think it's going to be very hard until you… as far as mechanically making them work. It's a version compatibility problem, almost entirely.
Does anybody have thoughts on the topic of… Of… of that.
Don't want to be the only person talking.
So I will keep talking if you force me to.
**Jake Dern** 19:03 So one… I mean, I don't have a thought on that specific question, but just kind of, like, one additional thing that I was thinking about related to this, and this is something that I've done in other applications that I've written, as well, and I've always thought that it might be nice in the Go Collector, or the Rust Collector to have something, but incorporating, like, the concept of identity as kind of, like, a first-class thing, in the engine that all components have access to. So for, like.
example, Most of the time, you know, like, there's some identity that, like, the application is running under, like, your user, which is maybe tied to, like, a CLI credential in, like, dev, or it's running as, like, a managed identity as a VM, or something like that.
And in the Go Collector, you can kind of wire this up to every single component in some way, like, you can define an extension, you can have all your extensions query it if you, like, pass them an ID to… or something like that. An alternative way, you know, would be, like, maybe as, like, a first-class thing.
Within the collector somewhere, you can configure and say, like, this is how, like, the collector gets its identity, like, information.
And that could be available to, like, all components, potentially, just to use, like, by default, without any kind of, like, configuration, right? So, if you have an exporter, you know, like, it can be… you could override, like, what kinds of credentials it's using, you know, after the fact, but by default, maybe it just acts as whatever, like, the, you know, central identity that the application is running under. I don't know if that makes sense, but that was one thing.
**Joshua MacDonald** 20:28 I take it you're familiar with how the GoCollector configures an auth extension. It sounds like you could do that.
**Jake Dern** 20:33 You could, you could with the Go Collector, right? Like, you could define an extension in the Go Collector. The Go Collector ones, and you can correct me if I'm wrong, but I thought they were a little bit… like, tied to some protocol, like HTTP or, like, gRPC, like, you usually implement an interface, but you could, like, define your own, right? And then you could pass it to every component and then cast it to something, but maybe, maybe there's something else there.
**Joshua MacDonald** 20:55 You're correct that they are specific for HTTP and gRPC, but that gets exactly at this extensibility question, is what would you do if there was a new protocol that came along and you wanted to add it to the auth extension package? How would you do that specifically? And again, it comes down to mechanics of the language. I'm going to put two links in the chat, I'll copy them in the notes. This… the first is my RFC that I wrote… Misguided, not well written, maybe don't read it, but it's, what I learned trying to add the middleware extensions in the Go Collector, and what I would say as a style guide that needs to be enforced pretty rigorously to protect this compatibility story, and it involves very Go-specific rules. I also linked to this thing, which I'm excited, or interested in, curiosity maybe, about… it's a Rust Paradigm that can do this.
This guy keeps posting about it, and I'm… I'm kind of like… I keep seeing it, being like, this seems to be an extension solution here in Rust that solves that version compatibility problem in Rust, which is where it needs to be solved.
So I don't know that we should dwell on this, but we were definitely going to have Lalit look at making an extension thing that would work for what he needs, and then, hopefully work beyond that.
And I would expect it to have the same kind of interface that the Go Collector uses, which is… In the case of HTTP, you're… basically, you're an interceptor. You've got your middleware, you can get the GET request, and you body, you can get the headers, and you can respond, you can wrap them all, whatever. In gRPC, it's very, very specific to the gRPC middleware interceptors API.
**Jake Dern** 22:36 Yeah, that makes sense. I guess I was just wondering if there's something maybe even more generic that could be done from the sense of, like, you know, if you take various Azure SDKs, for example, right, because that's the world I come from. If you have an Event Hubs client, or an Azure Data Explorer client, or something like that, oftentimes there is no option to override or intercept, like, the HTTP requests, for example.
But they're operating on kind of, like, a lower level, right? They're using just, hey, give me some way to get a bearer token.
And I will do the rest of the auth from there.
**Joshua MacDonald** 23:06 And…
**Jake Dern** 23:06 Yeah.
**Joshua MacDonald** 23:07 But that sounds, again, kind of like an extension. There's a… there's a bearer token provider extension, maybe, and yeah, I… the document that I linked, I hope to come back to. I'm gonna let Albert speak, but I… I keep finding cases in the Go Collector where it's like, we would like to add a specific new feature. Here's my proposed change, and it, like, messes with a bunch of core components. You're like, well, wait a second, the whole concept of extensions was that you should not have to do that all the time if we can find the right APIs. So, the one that keeps coming up in the Go Collector environment, that's sort of easy is, like, I want to find my, my resource detector, and, like, like, there's lots of ways that you might find a resource, and… and you don't want to have to hardcode them in the core library. It would be nice to just have an extension, which is, I'm a provider of resource about this process.
If you register me as the extension, I will be called at the right moment to configure the resource for the telemetry that this component is showing, or whatever.
Albert didn't put his hand up, so I won't let him talk.
Okay, I think we've belabored the point of extensions enough. I don't think it's going to be our hardest one. It is… except for when it comes to compatibility, which is… Well, going to be fun.
Yeah.
**Jake Dern** 24:28 If I could ask just a tar… like, just pointed question, So how do we feel if I were to just introduce, like, a small, like, auth package, in the sense of, like, just adding some code, maybe in the experimental folder?
**Joshua MacDonald** 24:39 Oh, I would feel great. Also, I would…
**Jake Dern** 24:43 pipes and stuff.
**Joshua MacDonald** 24:44 I would find you multiple code reviewers immediately, as well.
**Jake Dern** 24:46 Okay.
**Joshua MacDonald** 24:47 That sounds great.
**Jake Dern** 24:47 Great.
**Joshua MacDonald** 24:49 And also, if you want to consult, I can get you some people to talk about that, like, right away.
**Jake Dern** 24:54 Yup.
**Joshua MacDonald** 24:55 Namely, Lalit, who's got an open PR, but is not in the meeting.
So, on our agenda, I'm excited to ask Danny to speak. I know a little bit about what he's going to say, but I want to let him say it.
**Danny Chin** 25:11 Okay, so, Astrid, I… texture my screen, or something like that, or it's easier. Or probably…
**Joshua MacDonald** 25:22 I can… I can click in.
To… But I don't know where to click. You gave me a URL yesterday. I could go find it.
**Danny Chin** 25:33 I think I just sent you the, some, some, some results on Slack.
**Joshua MacDonald** 25:39 Yes, want me to pull up my Slack? I would be glad to do so.
**Danny Chin** 25:41 Yeah, no problem.
**Joshua MacDonald** 25:42 Sure, okay.
Let me find the screen.
And I'll just… I'll just…
**Danny Chin** 25:50 Yeah.
**Joshua MacDonald** 25:50 it.
**Danny Chin** 25:51 Oh, I'm, like, kind of, like, evaluating, the comp… like, several combinations of.
like, serialization and compression. So, for example, we have two serialization formats, one is OTLP, and another one is OTAP.
And we have… we usually use ZSCD as our compression form… compression algorithm.
But recently there is another, like, compression algorithm called OpenZL, and… It can, like… It actually, it can, like, after you write some parser for it, it can detect your, detect the structure of the data.
And… but, one thing to note is that you need some data to train.
To train the compressor here. But I actually kind of, I failed, because I… I just… trend on very, very few payloads. I feel maybe it's… universal enough, I need to look more into that, but I feel it's universal enough as long as the schema doesn't change. Like.
**Joshua MacDonald** 27:16 So this, this, example that I'm sharing here, it looks like maybe one of these should say OpenZL at the top, the dark blue triangle. But it's showing that, like, substantial improvement is what I'm seeing.
**Danny Chin** 27:32 Oh, but… .
**Joshua MacDonald** 27:36 compression ratio, which is, like, maybe the first thing I look at, you know, independent of how much time is being spent. There's this other one here.
**Danny Chin** 27:46 But actually, the dashed line is the OTLP+, OpenZO or NZSTD, and the solid line are still OTAP.
**Joshua MacDonald** 27:57 Yeah. So for now, like, the old tab is still, like, winning.
**Danny Chin** 28:00 Although we can see, much improvement in OTLP format, so…
**Joshua MacDonald** 28:08 I see. So you haven't… there's no… I get it. I think this is obvious, but I didn't… I made a mistake. So there's no usage of OpenZL on the arrow representation, because it would be different, you would have trained it differently, it might be something that could be done, but you're just comparing OpenZL on OPTLP.
**Danny Chin** 28:24 Yeah, and I did it on OTAB2, but I didn't find, like, huge increase.
**Joshua MacDonald** 28:29 Got it.
**Danny Chin** 28:30 Almost didn't increase.
**Joshua MacDonald** 28:32 Well, yeah, it kind of looks like the OT, the… the… that… that… and I… you showed me a few of these, that… OpenCL is actually making OTLP compress a lot more like the OTL Arrow protocol, so it's like, this compression algorithm can improve the row-oriented protocol to where it's competitive on compression. That's what I'm seeing as a first result, which is kind of exciting to me. I know that the OpenTelemetry group as a whole would be very excited to be told that they didn't have to change their protocol.
to maybe get some of the benefits, and I think, well, I'm excited that, you know.
We appear to have a good story for reading row-oriented data, and then, you know, getting the best of Arrow out of it anyway.
**Danny Chin** 29:18 So,
**Joshua MacDonald** 29:20 Yeah, this could be a, like.
reason to not focus as much on the Arrow IPC, But maybe that's a different study as far as, like, whether streaming compression using Arrow IPC is still getting us the benefits that we want, versus, like, always using OTLP and letting the compressor do its magic. It's a question that I'm wondering now.
**Danny Chin** 29:43 But for now, what I observed is that OTAP, I think probably because of, like, the resource dedupe.
thing. Like, right now, OTAP is still very, very strong.
Oh.
**Joshua MacDonald** 29:55 Got it.
**Danny Chin** 29:56 Yeah. So…
**Joshua MacDonald** 29:58 So that's to say that because even with a fancy compressor, we're still repeating information that has to be compressed, and in particular, we repeat… a scope object for every resource it appears in, we repeat a metric definition for every scope and resource it appears in, and that's deduplicated by OpenSummit, the OTL Arrow protocol, which is a… helping it, I guess, and that's, independent.
Cool. Well, I, I did, I will say this. I mentioned it to the, the… Where's my… I'm unsharing.
I feel confused about my sharing now, but okay. I mentioned it to the OpenTelemetry specifications SIG this morning because there's been a push to add dictionary support in OTLP, and I think this is relevant to them.
**Danny Chin** 30:49 So… But I actually think dictionary is kind of… it will make OTLP much more efficient, actually. So how do you think, like… I don't know, it's interesting.
**Joshua MacDonald** 31:03 I think these results will help people have that… make… make up their minds on that. Immediately, when I mentioned this in the meeting this morning, one person who has an important opinion suggested that there is a… partly the motivation for dictionaries in OTLP would be Compression, partly, but it's… it's more about, like, ease of working with the data, like, when you're.
**Danny Chin** 31:28 Hmm.
**Joshua MacDonald** 31:29 interpreting one of those profiles, it's full of references, and if you have to perform a string-based lookup, like, every single time, it's also harder to work with.
In some sense, is what I heard this morning.
**Danny Chin** 31:42 Hmm.
**Joshua MacDonald** 31:43 But it's really exciting to see that this new compression algorithm is so good, honestly.
**Danny Chin** 31:48 Hmm.
**Joshua MacDonald** 31:50 So, thanks for sharing.
Well, I had to unshare my window to get to where I could see it again.
We are… So thank you, Denny.
**Danny Chin** 32:01 And I will try to add, like, OTLP with dictionary case.
And share with you guys after that.
**Joshua MacDonald** 32:11 Interesting, yeah, I would be glad to help you promote this… this… report once we have it, especially with the people I spoke to this morning.
**Danny Chin** 32:18 Okay, thank you so much.
**Joshua MacDonald** 32:19 And, and really impressive, like, turnaround on that.
if, I think we'd be glad to see the proof, the code that you did to train the OTLP and compressor. Someone will want to see it, so thank you.
**Danny Chin** 32:32 Yeah, okay, no problem.
**Joshua MacDonald** 32:38 Okay, Halfway through. Okay, mindful of everyone's time, I put up open PR discussion, and I listed four. And I don't want to force us to talk through all of them, but there is one that I want to talk about.
And it's… the fact that Laurent's not here maybe is good.
he's on vacation, and I think he would like it if we merged this while he is away. I wanted to check in with Albert, since you, work closely with him, to see whether you would review this. It'd be one more set of eyes on it. It is not… I was telling Laurent this, essentially, like, he's, like, a project founder, I have a lot of trust in him, and I will give him a little bit of room to make big, messy changes that I wouldn't necessarily give everyone.
So, but even so, this is a big, fairly risky change, and I want to make sure people have seen it before we get it Before we merge it. So… It is… It is… implementing… Half of a new gRPC server… Well, it is hard to follow because it creates a file called server new without deleting the file called server.
And… it's… on a surface level, it looks like there's a little bit of duplication. Like, this type of structure appears almost twice, and I'm… I'm a little confused, so it may be leaving loose ends, which is sometimes okay, but I want to document them very carefully, and it's not clear at this point. So it feels like a little risky to merge while he's away.
That's all I wanted to say. We've… I've reviewed it once or twice. It's not… it's not horrendous, or… or obviously scary, it's just big, and he's not here this week.
So, Albert, if you approve it, I will… we can merge it.
**Albert Lockett** 34:36 Okay, yeah, sure. I had, I had reviewed the same code, like, before it was broken into multiple PRs, and I thought it looked okay with me, so… I… if it's okay, I'll just take a quick pass tomorrow morning. That's great. And and… yeah, and then, like you said, if there's anything that's, like.
outstanding, we can just document it, and then yell at LaRon when he gets back.
**Joshua MacDonald** 35:03 Yeah, like, I found one, like, minor refactoring that was gonna save 25 lines of code that would make it more readable, in my opinion, but I can't modify his branch.
I'd like to resolve it. Anyway, the point is, like, he's not here. So, Mindful of how much time there is, and how I honestly don't really feel like staying the whole hour here, I would like to ask… If… We don't… I would propose to skip talking about… about Exporter Helper and Goken's PR, because I spent an hour with him this morning, and he's not here.
Tls support, I haven't looked at it yet, and… well, it's not here, so I'm gonna propose that we skip over it, and I would like to see if, Andres, if you're willing to speak about your PR, because you are here, and it just was opened recently, so I don't… I haven't looked at it yet.
But I know the feeling.
behind it. And Cijo is also still here, so both of you are able to talk. I would love to hear you talk. Thank you.
**Andres Borja** 36:05 Of course, thanks, Harv, for taking this one.
Oh.
Yeah, being… trying to integrate the Autel SDK.
as our… I mean, we have a few discussions in the past on where to do it.
So basically, I am adding it at the end of the… internal SDK, multivariant SDK, so… So basically, I'm just pulling the metrics from run the internal SDK, and then… and then passing them to the… OpenTelemetry SDK.
I'm breaking it down, trying to make it smaller, but still, it's… the first one is always relatively big, but… In this initial one, adding the… kind of like the instrumentation, which is where we produce those metrics and send them to the SDK.
And I'm briefly mentioning the configuration.
It's more to show how it's gonna look, where it's gonna be pulled, but… but it's not completely implemented in this initial iteration.
**Joshua MacDonald** 37:23 That's… that's totally understood. I had to move my… window so I could see where you were, but now it looks like I'm talking to the side.
I was gonna add that there's a relevant PR from the Rust hotel Rust SDK that you must have merged earlier today, or maybe hasn't quite merged, but is the thing you just referred to. This is like a skeleton PR that's going to set us up for a future step where you integrate with the declarative configuration of the Rust SDK, is that right?
**Andres Borja** 37:54 Yeah.
**Joshua MacDonald** 37:55 Great.
This is good to hear. I know that, you spoke with us, I think, in the same meeting about 4 weeks ago, and we… we asked for declarative configuration, maybe, and so it was awesome to see you turn around so quickly add it to the REST SDK, and I know there was a lot of debate that went into how it was done, so thank you.
Do you… I feel… I feel like I… okay, am I… I'm not sharing my screen anymore. I'm having a bad day with technology. Is there anything that you feel like we could or should talk about as far as this PR itself, or is it, would you say, fairly uncontroversial? I didn't look at it yet.
**Andres Borja** 38:35 So… More than controversial things is to mention a few findings, so, One of the… that comes to my mind is… In the internal telemetry… I'm sorry, in the internal SDK, in the multivariant SDK, we… don't have support for attributes. I'm not sure if this is known, but we don't have support for attributes at metric level.
So… That is, a small difference with… with, you know, with the SDK, with the Rust SDK, open telemetry SDK, so… It means that we will not… support out when producing metrics, which is… I feel like it's important.
**Joshua MacDonald** 39:32 Yeah, I guess… I can see how that came about, like, the goal of having there be a… I feel like we ought to be able to recover some metric… some attributes, and the way I, in… in… OpenTelemetry since there's a… there's been a topic about… What's called a bound instrument, which is sort of like, if you take your attributes and you pre… pre-calculate them, and you give them to the SDK, and you say, okay, these are my attributes, I want you to give me some raw counters, and then… and then you have these raw, like, counter addresses that you can simply implement, increment, and they've been pre-associated with the… with the attributes.
I… that's the model I have for this code, which is to say that each component well, let's suppose it's just one component. I've worked on the retry processor, so I'm familiar with its metrics. So, if there was a service running that had many retry processors, each of them is allocating one struct of its own metrics.
But I said many, so why? Well, there's different positions in the pipeline, maybe, and so there's different retry processors, but they all still have a name.
And they also have a URN, and those are gonna… that name is gonna be different, that identity name.
And to me, like, conceptually, that's an attribute in the sense I know, however, it also would qualify as a scope attribute in OpenSeometry, and now I'm just unraveling, like, you know, there are loose ends here.
**Andres Borja** 41:10 So… I mean, in the SDK, we have two things. One is the attributes, the resource level.
Wish.
Yeah, those are basically for the research and the observation, so you put there things like service and so on.
It looks like, in the internal implementation, those are the ones that are like, fixed, and that are up in the current implementation, is they are appended or attached to every.
metric, so… even when you see the implementation in parameters, it looks exactly… I mean, it looks relatively odd, because every single metric will have its own Replica of the… of the attributes.
**Joshua MacDonald** 41:58 That's Prometheus, however, and that's kind of… Well, there are…
**Andres Borja** 42:01 both steps, right? It has the metric level attributes, and then you have at the bottom the resources. So, Now… The attributes at the metric level?
it opens… I have to say that it opens a bunch of questions in my head, because I don't even know how to consolidate them, but… But technically, it's… when you take, for example, the back end, in our case, Geneva, it's mostly about the dimensions, right? So you can have the same metric with the same name, with the same URL.
Same type of value, but… Values and those dimensions might be different, you know?
so, that's why those fixed attributes look more like a resource-level attributes, more than metric-level attributes, so…
**Joshua MacDonald** 43:02 Andres, are you familiar with, in the OTEL model, that scope have… scopes have attributes? It's just like this corner case that hasn't been widely implemented.
So I wouldn't blame you for having not seen it.
**Andres Borja** 43:13 No, no, I haven't.
**Joshua MacDonald** 43:15 Yeah, so, well, I'm clicking around in the repository, I could kind of click in, and maybe I could find the right thing here, but… You know, I can quickly find the, show how well I know our source tree. The OpenTelemetry protocol.
And if I'm looking at the common protocol, I will find the scope instrumentation scope, it was called originally, so it has a name and a version, and then right here, it has attributes. And OpenTelemetry added this, and then got stuck. It's pretty bad. Honestly, it's not been a good story, because there was a backwards compatibility concern that made it impossible, and that's sort of where we're stuck.
But I don't like being stuck there, and what you… what I described, that was the little asterisk, was, like, you register a whole component worth of metrics, and it's got, like, a bunch of them, and these attributes, like the component name, are scope-wide. They don't affect every metric. They're, like, the entire instance of this metric Producer is associated with these specific attribute values, which are across all the metrics, but not resource level, because there's multiple instances in the SDK.
So… I was saying what you're describing… what I'm… and moreover, I should say that the Go Collector has been working to add these exact things for exactly this reason. We have many components in the collector, they have names, but they also have sub-identities, like they have they have not only a factory type, but they have a secondary identifier. So the secondary identifier is a key attribute, but it applies to all the metrics in the component. It becomes a scope attribute, and that's pretty new in the Go Collector.
they had… they had to, like, bend around the Go SDK a little bit, because again, the OTEL group got stuck on this topic.
So, but I… but I also wanted to respond to what… what you said, and I don't want to… totally, dominate this conversation, but there's one more thing to show, and I was going to use the retry processor as an example. Take me just a second to find it.
So here's the retry processor, and maybe I'll skip down, and it's pretty obvious where the metrics are. Here they are. So, this is an example of what we're talking about.
I've filed issues about how realistically, I would like to see this type of instrumentation be done once, not once per component. Like, we should have a library that handles the pattern here, and the pattern is that it was actually derived from a GoCollector document. There's a GoCollector document that lays out this naming convention, essentially, and I can find that out for all of you as well. But the idea is that you have… several dimensions here. These are attributes, they're just… they're just bound in the sense that I'm giving you a physical memory address for each combination of attributes, and I think we can talk about how to turn them back into attributes. So, this… Three… these three metrics are the same conceptually, but they have signal type, which is logs, metrics, and traces.
So, log success, metric success, trace of success, and that's on the consumed side, that's coming in. Then I've got consumed by, by failure. So I've got logs failure, traces failure, metrics failure, and I've got Failure. So now I've got two dimensions. It's success versus failure, and it's signal type.
And then I've got another one… Well, those are the only two dimensions that I see in this data, because the other variable is part of the metric name, and So you've got consumed items, and you've got produced items. And those are… The two metrics here, with… Well.
Three, three, three signals and two failure cases, or, you know, outcome.
For each. So, if we could put some sort of additional annotation up here, Saying the metric is consumed items… And an attribute named signal is traces.
And I just didn't mean to click that. An attribute named signal is… either traces, logs or metrics, and then an attribute named outcome is success or failure. So there are attributes here, but we would have to encode the translation back from what I'm calling a bound instrument. Does the word bound instrument clear to anybody here? I know CJO knows what I'm talking about.
So, I actually don't think I'm being very clear about bound instruments, but this struct represents the binding of an entire component with a bunch of pre-declared attribute-value combinations. So the first three, that's one metric with three signal values. Again, this is one metric with the other three outcomes for the same three values of signal. So, So this 6… that's one metric.
This 6, that's… There's… little bit of detail here, I don't want to walk through it in too much detail here. But, but the binding that I'm speaking of is… Essentially that you don't have to do any more work with attributes, because you do it once at the startup.
That's what I'm trying to say.
Ugh, you can tell that we're at the end of a day, because I'm not making sense. So, I feel like if this is not making sense, we can talk about it again. Maybe not in the middle of the meeting.
And it doesn't have to slow you down. I will be very happy to see these metrics coming in as they stand now, and to evolve towards making them look more like attributes in OTLP in coming PRs.
If that makes sense.
**Andres Borja** 49:16 So, yeah, this is, again, just a finding there, and… and we need just to define what we're gonna be doing. Are we going to support attributes in the internal one?
Or no, and the answer is no, we just don't have any attributes to the metric when.
**Joshua MacDonald** 49:35 Yeah. And what I'm trying to say is it's fine to start with no attributes. We should file an issue about it, and I think we should do something about it. I can definitely see extending the… math… the procedural macro definition for metric, which is somewhere in our code, to also take, like.
predefined attribute value pairs, so that this… this one here would have signal equals traces and outcome equals success hard-coded, and then the name would be consumed items, or something like that.
That would be a… an idea. We could file an issue to talk about it in more detail.
**Andres Borja** 50:11 And something that is kind of related The other finding is, We are basically in the internal, in internal SDK?
We are using… we are calculating the resource attributes, basically. We are trying to get the instance ID, even the service name, if I'm wrong, and then we calculate them, and then we put them there as attributes that we send as… It's more like a resource attribute, but we are sending them as part of every metric.
Now… in the OpenTelemetry one, is actually a configuration time parameter, right? So, you can get them from whatever you want, or wherever you can, but you need to put them as part of the configuration.
That is… different, and that is something we need to fix, because we don't want to… I mean, we need to fix now. It's just different things, right?
So the resource attributes that I'm putting is… from… in the SDK configuration is because they are passed by configuration, right? So if I am configuring this thing, I'm just gonna pass my service name, and my instance ID, both, so… and so, you know?
**Joshua MacDonald** 51:33 Is that not what you're looking for?
**Andres Borja** 51:36 Yeah, yeah, I'm just mentioning that that is slightly different, you know?
Jessica, just not the way.
**Joshua MacDonald** 51:43 the Go Collector works, you configure your resource somewhere in the service telemetry section?
**Andres Borja** 51:49 Correct, correct. So I'm following that approach.
The internal approach is… is not like that. The internal approach doesn't take those parameters, it just calculates them.
**Joshua MacDonald** 51:59 I see, I see, I see. That seems like something we can and should improve. That also is right back to where I was talking about extensions. Like, what a great idea for an extension is the resource detector extension. You just configure the ones that you want, and they will automatically load. That would be an example of an extension, but that does not exist in Go.
**Andres Borja** 52:18 I think it exists, but… but it's still through configuration, right? Just because you can calculate… let them calculate, it doesn't mean that you don't need to configure them, say, hey, use it, you know?
**Joshua MacDonald** 52:29 Okay.
Cool. I actually don't know the detail, this is… But I agree, we… we wanna… Have a little more control over resource configuration as well.
**Andres Borja** 52:42 So, in some… yeah, that is just to mention, just part of the findings that I got. So, I'm just, yeah, taking it from the configuration, so basically I'm ignoring… I'm not ignoring the other attributes, because I'm sending it as part of the metrics, as… as today.
But those are not the ones that are going to be taken for resource, because you cannot even link them later on, because they are unloading time configuration time.
**Joshua MacDonald** 53:08 Well, okay, thank you. I understand.
And, agree that we should, we will configure metrics. We will configure resources.
Okay, I propose, unless anyone has another topic, or something… somebody wants to talk instead of me, that we have reached the end of the meeting.
Going once, going twice. Alright, we're done. Thank you all. So remember, next time, Thursday, the… 10th or so of, of December will be a more widely attended meeting. 8 AM, we expect to talk with some of the outsiders and stakeholders about the future of Hotel Aero at Phase 3. Thank you. See you next time. Appreciate everyone here. Bye.
