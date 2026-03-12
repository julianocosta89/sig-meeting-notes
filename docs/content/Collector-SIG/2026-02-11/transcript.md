SIG: Collector SIG
Date: 2026-02-11
Duration: 58 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 01:41 Hi, Andrea. Do you think we're in the right meeting?
**Andrew Wilkins @ Elastic Observability** 01:45 Hey, Lyd Miller. Yeah, I think we are. It's usually… there's usually people coming. Oh, here's Josh.
**Liudmila Molkova** 01:52 And Josh.
**jmacdonald** 01:53 I made it.
Yeah.
It's been a long day, so I'm doing my best. I remember it as well. So, yeah, here we are.
Hey, Andrew.
**Andrew Wilkins @ Elastic Observability** 02:04 I think we'll probably have a… There you go. I think we'll probably have another couple of people joining.
You're not gonna get me at my best today, I didn't get much sleep last night, but…
**jmacdonald** 02:13 I'm just off the AeroSig. We… it's running over. I decided I would leave because I didn't want to listen to the rest of the conversation.
Yeah.
Since I don't normally… like, I must find some notes, right? Do we have notes? Is there an agenda?
**Andrew Wilkins @ Elastic Observability** 02:33 Yeah, I'll get a link and put it in the chat.
There you go.
**jmacdonald** 02:40 Thank you.
**atoulme** 02:58 So…
**jmacdonald** 03:02 Wow, there's all kinds of stuff here.
**atoulme** 03:07 Right?
**jmacdonald** 03:15 Yeah, yeah, yeah, yeah, yeah.
Go 126, huh?
**atoulme** 03:39 Yeah.
Probably worth pointing out.
Me pink shots, if he's available.
**jmacdonald** 04:18 Whoa… Okay, new syntax.
New… okay.
Would… would… would you ordinarily run this meeting, Andrew, or Antoine?
**atoulme** 04:50 Whatever, we can just go in order.
**jmacdonald** 04:52 Yeah.
We don't have to be so formal.
**atoulme** 04:55 You can mute. Oh, right, it's fine.
What's up?
**jmacdonald** 05:00 I'm gonna… I could put up a… a screen.
**atoulme** 05:07 Sure.
**jmacdonald** 05:08 Okay, here it comes.
**atoulme** 05:15 So, actually… What is this RFC thing?
**jmacdonald** 05:21 Good question. Don't know.
**atoulme** 05:25 See, this is from Dimitri. Dimitri joined us.
That's an announcement, so there's nothing to do, just so we should know about it, I guess.
**Dmitrii Anoshin** 05:39 That hooks.
**atoulme** 05:40 B.
**Dmitrii Anoshin** 05:41 Yeah, it's just an, just an addition to existing RFC for… Migration from one semantic convention to another.
**atoulme** 05:52 And it just… it clarifies how we handle the conflicts. For example, if…
**Dmitrii Anoshin** 05:58 Metric name is the same, but attributes get changed in one semantic convention.
From one semantic convention to another, we just clarify how we deal with the conflict in this proposed, Alright, good resolution, perfect resolution.
That's pretty much it.
**jmacdonald** 06:20 And it's… got it.
It's… It's this stuff here, and this stuff here, yeah.
Cool, thank you.
Not easy to upgrade semantic conventions.
Well, it's merged. I guess there's not much to… much more, unless there's any comments.
**atoulme** 06:45 No.
**Dmitrii Anoshin** 06:46 Mr.
Actually.
**jmacdonald** 06:48 I'm surprised to see too many people and such a big agenda for this time. Yeah, same. I haven't been in a while. It's, like, kind of daunting. Should we… I'll just… I don't mind clicking into this stuff, I know that, my name is on an agenda item I'm ready to talk about, but…
**atoulme** 07:07 What is there about that one?
**jmacdonald** 07:11 this has a bunch of sub-issues. Is that what we're meant to review? Go through high-priority issues.
**atoulme** 07:17 Trying the board. I looked at the board before the meeting, I don't see anything that we need to really go into, and maybe the three top ones?
**jmacdonald** 07:25 than needed, yeah.
Okay.
**atoulme** 07:29 I mean, you've got Dimitri here, who's a husband, Rick's receiver, good owner, maybe. Do you have any… inside there.
I don't know.
**Dmitrii Anoshin** 07:38 That's actually the one that I… no, no, the PR firm announcement…
**atoulme** 07:44 Oh, okay.
**Dmitrii Anoshin** 07:45 On one of those.
**jmacdonald** 07:45 The RFC is about this.
**atoulme** 07:47 Right.
**Dmitrii Anoshin** 07:48 It was one of the things to unlock host metrics receiver translation, because we had some… some problems with that. But otherwise, yeah, it's been going pretty well. I don't know, not much to add.
Yeah.
**atoulme** 08:10 Okay, does it really need discussion, or…
**Dmitrii Anoshin** 08:12 I don't think so.
Okay. Especially, it might be worth discussing if we have, like, people from… who are working on the MIT conventions for Kubernetes and, host system metrics, but we do discuss those things in, special 6, in, like, Kubernetes systematic connection sick and host metrics receive… host metrics.
**atoulme** 08:38 Okay.
**Dmitrii Anoshin** 08:38 System 6, yeah.
**atoulme** 08:41 I mean, the only thing we can do here is we decide it's workable, and we move it to workable, but it looks like you're saying maybe wait until the SIG is done.
That's what you're saying, right?
Because.
I haven't read the thing, right, so…
**Dmitrii Anoshin** 08:57 Yeah, I think so, yeah.
**jmacdonald** 09:00 This is only from May of 2023.
Yep.
Any… yeah, I think… I think we can probably move past this, I would say.
**Dmitrii Anoshin** 09:13 Yeah, sounds good to me.
**jmacdonald** 09:14 Lila's laughing. No comments from the semantic invention territory?
**Liudmila Molkova** 09:18 I'm scared of admitting I'm here.
**jmacdonald** 09:21 Huh.
**Liudmila Molkova** 09:23 Okay.
**jmacdonald** 09:24 Well, in that case, we can just run forward. I… I got myself involved in a.
offhand comment. Whoa, that was not… where I thought I was gonna go when I clicked that.
**atoulme** 09:37 Yeah.
**jmacdonald** 09:38 Something's wrong.
But just for the record, the idea was I have had a passion for extensions in this project. It started with my research into rate limiting, which I still plan to pick up again.
And working with Bogan on the middleware interfaces, extension interfaces for middleware got me thinking about this topic. So now I care. I've written a, component interface guidelines. It's a PR in the core.
I'm… it's a really hard topic. I'm not sure it's readable yet, but I'm still working on it. That's my third try. We'll keep going. But the point is, I care about extensions. Okay, now we got the… And, I think it's a valuable, important way to make this stable.
ecosystem of code, like, really work in lots of places. So, I think we should use the extension mechanism and grow it. And one of the challenges with extensions is making it so you can add new interfaces to old concepts, like… Having a storage extension, you know, the idea is there's a V1 storage extension, and it's kind of, like, matched to the… RoxDB type of interface. Well, it's… it's a very high-level interface, and… and… And some… somebody finds that useful for the… the exporter helper storage like, persistent storage, right? There's a different kind of storage extension, which somebody else wants, which is a different interface, and we're seeing it come up again and again. Somebody asked for it in the tail sampling processor, and if we put a pebble, which is the CrockDB, RocksDB thing.
Pebble implementation in the Go Collector, it's gonna blow up the image size by some amount, and if users don't want that, they shouldn't.
they should be able to turn it off, right? So, you could build yourself a collector without the Pebble extension.
But that would require a new storage interface extension. New storage extension interface.
And according to my document, my component guidelines, we should just do that, and I like to support that. So that's all that I did, is say that.
That I support the idea of new extensions. I think I know how they work.
One makes sense for Pebble. I've heard… and I said that, and then immediately we found that somebody else had a Pebble extension idea brewing, and that was someone at… observe, I… At…
**atoulme** 12:14 Yeah. Observatory.
**jmacdonald** 12:15 Yeah, somewhere, somewhere. So, how can I help? I'm ready to, you know, review.
any comments, I would be happy to, like, try to defend or whatever, you know.
**atoulme** 12:31 I mean, Josh, you know that we changed a bit the component addition rules recently. It's kind of… It's a bit of a blanket statement, but… I think in general and Contraib, there is now a need for people to develop the extension outside of Contraib and showcase it, even show some usage and some adoption before it gets even considered for, you know…
**jmacdonald** 12:55 Adoptions and culture, which…
**atoulme** 12:57 I personally don't think it's battery wise. I think we're too early for that, but that's the situation we're in. So… That's an unfortunate place we are.
If you want to create additional extensions at this point, like, it's unfortunately gonna have to be outside first, and then come in.
**jmacdonald** 13:17 Okay.
**atoulme** 13:18 So… Yep.
**Dmitrii Anoshin** 13:22 But in order to make it outside, we need this new interface with the extensions, right, that you're proposing, Josh, as far as I understood, correct?
**atoulme** 13:30 He, still won't, you know…
**jmacdonald** 13:33 Yeah, I won't work for tail sampling processor, I think. I mean…
**atoulme** 13:36 Yup.
**Dmitrii Anoshin** 13:39 Why not?
**jmacdonald** 13:42 Well… Can't… I mean… Good question. I'm… I'm… this… this is tricky, like, I think there… what the… what you would want is an interface definition, like, we have extensions, extension middleware, and then there's, like, interfaces. It's just pure interfaces.
**atoulme** 14:02 Oh, yes.
**jmacdonald** 14:02 I think that part needs to be in the repository. And then we could make tailsampling processor have one more config field that was, like, the name of your persistent storage for the Fancy tail sampling off disk… on disk.
**Dmitrii Anoshin** 14:18 Yeah, and we already have a storage extension.
**jmacdonald** 14:23 Yeah, what I mean is that… and I asked immediately, can't you use the storage extension interface? And the answer is… The storage extension interface is a pretty high-level key-value store, and the Pebble interface needs range scan.
It's not there, so…
**Dmitrii Anoshin** 14:41 Okay. So we can extend that interface, add an additional optional interface for the storage?
**jmacdonald** 14:47 That's right. That's, I think, if… if we can find a way to make the Pebble type of storage extension with range scan a superset or a, like, extension on top of the plain built-in Then, one storage extension can be both.
**Dmitrii Anoshin** 15:05 That's how it's supposed to be. This is the… this is the extensions doing their thing.
**jmacdonald** 15:09 In that case, I would say we want to put a new Pebble style of interface in the core, market X extension storage unstable stuff.
**Dmitrii Anoshin** 15:19 Yeah.
**jmacdonald** 15:19 Publish that, then go and implement, Maybe one or more uses of the range scan in the tail sampling processor repository, and still there's no Pebble extension anywhere. That's somewhere else, like, that's in the ObserveIQ, or the Elastic repository, or whatever.
**Dmitrii Anoshin** 15:38 And they can donate it eventually, when they, like, use the new extension interface, they validate that it's working, they can donate their extension to the country. I think that's…
**atoulme** 15:49 how many times.
**Dmitrii Anoshin** 15:50 It's a reasonable, approach here.
**jmacdonald** 15:54 And then at that point, we would, I think, move to make the core storage extension stable. And then it would…
**Dmitrii Anoshin** 16:03 that is right, but we can combine… we can adopt the range, even if it's opt… I don't know, maybe, like, the range can be optional still, like, it's not necessary for other things, right?
**jmacdonald** 16:17 That's right, that's the idea that extensions are meant to provide, is that if someone wants the new thing, you can provide it, but the old thing still works, and the old people who want the old thing don't even know about it.
**Dmitrii Anoshin** 16:26 Right, right.
And I think that's the right way to go here.
**jmacdonald** 16:31 Cool. I…
**Dmitrii Anoshin** 16:32 Yeah, I do agree that it shouldn't be embedded in the… tail-based, tail-based sampling.
The purple, bubble, so…
**atoulme** 16:42 Yeah, my table shouldn't have been there. I was just going to offer maybe an alternative here, which is maybe… you want to be showing end-to-end that it works first. So, you know, in the test sampling processor, you could have casting to an interface.
Without exposing too much, if that makes any sense.
**jmacdonald** 17:03 Yeah, yeah, I hear you. So you're… so that's a, V0 could be… the tail sampling processor implements an extension privately for its own self.
**atoulme** 17:15 Yeah.
**jmacdonald** 17:15 And then once we've been, like, gone through a few releases, and the users are happy with the feature.
**atoulme** 17:22 That's right.
**jmacdonald** 17:23 Okay, I can try to explain that. I think we should not speak much more on this topic. We all seem to understand each other, so I will take that back to the people that are discussing it.
That helps us.
**Andrew Wilkins @ Elastic Observability** 17:33 As one of the people who… Introduce some of these concepts to our products, I just wanted to point out that it's not just range scans. We need TTL prefix queries and also compaction, like, customizable compaction. So I'm… my only concern is that it ends up being approximating Pebble to the degree that it just is Pebble, and it's the only.
**jmacdonald** 18:00 Yeah.
**Andrew Wilkins @ Elastic Observability** 18:00 use, but I think it's worth trying to come up with an interface. Anyway, just saying that it, like.
the more things we add, the more it's gonna look like Pebble.
**jmacdonald** 18:13 Yeah.
Is there an issue that we could maybe… put in the core… I will… I will volunteer to file a core collector issue that describes what we just said, saying we don't quite know how to introduce a new storage extension because we're afraid it's going to turn into Pebble.
Yeah, okay.
I'll just put that there, and then we can follow up again in this somewhere.
**Andrew Wilkins @ Elastic Observability** 18:38 There is another issue I can link later, which is related to the interval processor. So there's a… the interval processor is one that aggregates metrics, and we have a variant of that that uses Pebble, basically offloading to disk, and then doing merges using the LSM functionality, that's… that's where the… the compaction thing I mentioned would come into play.
**jmacdonald** 19:03 Gotcha. I'll try and synthesis… synthesize something, after.
So, thank you. I'll follow up on that.
**atoulme** 19:13 Yeah, I mean, Josh, just think small, right? Just get it to work for your stuff, and then try to generalize from there, because I think you're going to be lost in the multitude of approvals and design discussions otherwise, and…
**jmacdonald** 19:25 I don't… yeah, it's not even for me. I was just trying to help as new owner of the tail sampling processor. This was proposed for the tail sampling processor, and I, you know, I like extensions as an idea.
**atoulme** 19:36 It's gonna be hard, I admit, because…
**jmacdonald** 19:39 Because having an extension interface without the Pebble extension is going to mean you have the Pebble extension in a different repo, and your version locked again. I'm afraid, like… Version lock, meaning you can't release yourself without waiting for another version of the thing, and, like, it's really hard.
**atoulme** 19:58 No, you do typecasting, right? You don't really need to define the interface publicly, you just typecast in your sampling processor for now, and it's like, does it do this?
Anyway, let's…
**jmacdonald** 20:10 Okay, that's my… that'll be my proposal, is we start with something that's totally private to the tail sampling processor.
**atoulme** 20:15 Yep.
**jmacdonald** 20:16 I just need to think about how it's gonna work.
Because, I mean, ultimately, the users who care about… I would say, my impression is the users who care about the tail sampling processor tend to be on the smaller scale of users out there.
And they are not… they're looking for the collector contribib, they're not willing to maintain their own repository. Like, this is a nice feature for the small-time user. It's… at scale, I don't think this is the appropriate use for a tail sampling processor. That's why it's hard.
**atoulme** 20:47 You can definitely… the proposal that we have right now, I think, is too drastic to help country move forward, but it's difficult because we… we're trying to go for stabilization, so…
**jmacdonald** 20:59 Yeah.
**atoulme** 21:00 We need to… we need to be good about it. I think the problem is that, overall, people will get the notion of a mess otherwise. I mean, you can actually see that Contrib has more PRs open than ever.
**jmacdonald** 21:10 Yeah.
Anyway, I just don't want to throw a Pebble build into anything unless a user wants it, so we'll figure… we'll work on this.
**atoulme** 21:19 Alright, alright. Okay, let's…
**jmacdonald** 21:22 gosh, I… it feels like I'm running a meeting. Andrew, do you wanna, That was actually the next one.
**Andrew Wilkins @ Elastic Observability** 21:28 I was gonna announce this on behalf of Blake, but Blake is here, so Blake, do you want to talk about the pipeline reload thing?
**Blake Rouse** 21:36 Yeah, sure. This is something, that we're looking to enable in the collector for, partial reloads of the OpenTelemetry collector. At the moment.
The collector, when a change is done in config, and you do, like, a SIGUP, It results in tearing down all pipelines and bringing them all back up.
This obviously, you know, opens up windows for lost events while the pipeline's down, or not being able to receive events. So that's lost events, downtime windows, and then I'll see the performance overhead of some exporters and things like that, having some performance overhead of brain tear down and brought back up.
So this is something that we would like to do, to the collector if it was accepted and deemed okay. It would be done in a way where it's feature-gated, you know, it wouldn't touch any existing flows that exist in the collector at the moment. Obviously, you know, stability is real important, and so we don't want to do that, so this would be something where a feature flag would be enabled.
But from an elastic standpoint, we would enable it as soon as it was available. We'd obviously like to do it in phases, not to just do this, like, big bang rollout.
It would be, you know, receivers first. That's our main use case.
But we'd like to see it, across the whole pipeline, to provide, you know, just a good feature set across it.
But our main use case is receivers now, but others do apply over time, especially the… just, like, a new pipeline, without touching the other ones.
And so… Yeah, so it would work by, you know, looking at, one, just pipeline additions, like adding or removing receivers, but then also things like, adding, if you modify a receiver, it would tear down that receiver and rebuild the receiver. It does always do… it would work in the same way as the graph works now. It would completely tear down the receiver and create a new one.
And then it also would work in the way of recreating the whole pipeline. So if you… like, if a processor is changed or added to the pipeline.
The processing flow would be… re… the processing… the processes would be rebuilt, and the receiver would be rebuilt, even though you didn't touch the receiver, but the exporter would stay as it was. And so it kind of goes up the chain from where things are. At least that's what we're looking for, With this, with this feature.
I actually have not read this comment on it.
**jmacdonald** 24:28 Yeah, I just… I just started reading it myself. It looks like Evan is asking for, essentially, a more detailed document.
From what I'm seeing.
I… I send… I understand the receivers are the simplest ones, because they don't have in… Input consumer connections and so on.
**Blake Rouse** 24:48 Correct.
**jmacdonald** 24:51 I, I feel like I can comment on… just, I just left the OTEL Aero meeting.
20 minutes ago. And just for background, the Hotel Arrow is building a Rust data flow pipelines. Really not a collector, it's, it's, like.
But it has some common aspects, and we just got out of a conversation about restarting pipelines, and the… there's been an abstraction introduced there called a pipeline group.
And… and because Rust is Rust, we have a lot of control over threads, and so the idea there is, because we really want a lot of control over the thread, we would have a pipeline group be a unit that is a single thread.
And then, the concept is, the reason why we want a pipeline group is to start and stop them independently. You should be able to take down, reconfigure, start just one group at a time.
And the, the, the connection with this conversation here is that, the… there's a pretty big difference in our config models, sort of intentionally so, again, because of the wanting thread-level control. In the GoCollector config, you know, it's a very high-level, asset… a configuration where pipelines and exporters and receivers are connected in a certain way. You… I think we all understand that one receiver can send to multiple pipelines, and again, so we were trying to map the… literally trying to map a GoCollector config onto our model, and there's… there's a question of whether we want to have pipeline groups correspond with One segment of processors and dedicate one pipeline group to each receiver and one to each exporter, simply because those are the natural units of restart.
I'm not sure this is helping anybody, so I'll take that back. The point being something about how there's not a concept here To, say, restart one processor pipeline, that I'm seeing And… So it's a hard problem. Maybe I shouldn't say anymore, I don't have any good ideas.
**Blake Rouse** 27:07 I don't know exactly what you mean. You're trying to just… you're saying it would just restart one processor pipeline?
**jmacdonald** 27:13 I'm trying to say that we went in a totally different direction with config to get control over the thread.
And… And now the thread is the unit of restart, because it's hard to restart just a little bit of a thread.
But we're having trouble… mapping the GoCollector pipeline layout onto it, because Sorry, I feel like I should have said nothing here. I'm just trying to say that, like, that, like, we don't have a… we have a very different way of referring to a pipeline, because there is no one pipeline we can restart in the collector, because you've got multiple outputs from one receiver.
And this gives me lots of thinking to do. I'm not sure what to say.
**Blake Rouse** 28:10 Okay.
**Andrew Wilkins @ Elastic Observability** 28:13 Blake, I had a question while you were talking come to my mind. Did you already look into… sort of splicing… if you… if you just changed a processor, did you look into splicing a new one in? So you would have… so you wouldn't necessarily have to restart the whole pipeline?
**Blake Rouse** 28:30 I did not. I specifically was trying to keep with the same flow that the graph was currently doing, without trying to, like, cause any type of, like, race condition or weird lock… or adding locks anywhere to allow something like that. It was specifically, like, how can we allow partial reload without You know, really changing any interfaces or adding locking or anything like that was kind of my… Ma.
My idea here, so no, I did not. I mean… It might.
definitely could be done. I think in the case of, like.
Adding a new exporter to the end, like, if you're adding a new exporter, that probably could be just appended on to the fan-out at the end.
And it would be safe. It doesn't do that at the moment, like, it would just restart the whole pipeline, even though it probably could just append it.
It was just really for, like.
Not adding locking and things like that in those areas.
It's kind of like, you know, let's not do that.
Our use case for the day, and maybe I wasn't clear here on the issue in looking at the response on the issue, is one of our issues is, reading files… files. So, especially, like, container files. Container files, you know, obviously will be cleaned up quickly, and so if we are dynamically… and we have a flow where we are dynamically changing the config.
to read new containers as they appear. So if they are not done quickly, we are, we're worried that, like, we'd be restarting the whole collector to read, like, a long-running file that's always there, and we're always just restarting it for containers and things that are just randomly appearing.
And so that was kind of like, my… lost event downtime window aspect here. I don't know if that's necessarily portrayed here well, in that.
So… It's not necessarily… So much for… The tracing case, or the, Metrics case, it's much more for the logging case, where this becomes a problem.
Which I know is kind of new to the collector, the logging pieces, so… Yeah.
**Dmitrii Anoshin** 30:51 Can you clarify why do you need restarts for the new container?
It comes up.
**Blake Rouse** 30:59 The way it works now is that when a new container comes up, it gets added as a new receiver, and so that receiver being added means.
**Dmitrii Anoshin** 31:07 What do you use for that? Why is that the case?
What receiver do you use? Why is it required a new receiver to be…
**Blake Rouse** 31:17 It would be Elastic's own custom receiver, the FoulBeat receiver.
That's running File B, but you could think of it the same as a file log receiver. If you were running the file log receiver, you could think of it the same.
**Dmitrii Anoshin** 31:28 No, the FileRock receiver doesn't need any restart, it's, like, it watches… like, set of files by globe expressions.
**Blake Rouse** 31:39 Yeah, but let's say you weren't using a glove.
Obviously, yes, you can use it by law, but let's say you're giving a specific file.
**atoulme** 31:46 Right, and that file… and that list of files in the… in your log receiver.
**Blake Rouse** 31:51 Keeps getting appended to.
**Dmitrii Anoshin** 31:53 You have to keep restarting file log receiver every time that happens.
**Blake Rouse** 31:56 That's a…
**Dmitrii Anoshin** 31:57 Yeah, but why? Why can't you use Google Open instead? Because, like, in Kubernetes, if all file… files for the containers, they have specific, specific pattern. It's… Straightforward to set up the group for that.
**Blake Rouse** 32:13 Yeah, this has to go… it's just the history of, like.
how Elastic runs the collector underneath its existing config, that it has this thing where each… input Is, like, its own… Defined input, basically.
Right, it's its own defined input.
**Dmitrii Anoshin** 32:34 But… okay, you want… so you…
**Blake Rouse** 32:36 But that's not the… I mean, we still see this as an issue. I think it was brought up, maybe.
I've heard, I haven't been on a SIG for the op-amp, but obviously dynamic config reloading through op-amp would be another place where Restarting the whole collector based on a config change.
is… is not.
**Dmitrii Anoshin** 32:57 Yeah, and we need to bring some people from who work on the pump, and I think that might be the issue, but there is some kind of a solution that I'm not aware of at this point.
So they… I mean, my point is that we need to bring OpAMP people to your issue and get their feedback, essentially.
**Blake Rouse** 33:20 Yeah, I think that'd be great, yeah.
**jmacdonald** 33:24 Blake, your description gave me a better way to think about what I was trying to say earlier, and it's that you don't want to add locking if you can avoid it, because otherwise it's going to be, like, you're going to hit the performance cost.
this technique I was describing was in the other Rust environment, was really that we're giving the configurator a mechanism to say, this is a consistent group that we will all start at one time.
And, like, so essentially giving sub-regional, like.
These nodes can be restarted all at once, so they don't need any synchronization between them. Whereas between this group of nodes and this group of nodes, we want to be able to restart independently, therefore we have a lock, or an extra channel, or some extra overhead to facilitate the restarting that you want.
I think that's the direction, just the observation I wanted to make.
**Dmitrii Anoshin** 34:17 We do have it in the… Collector Builder… Start.
time, we do have that dependency, so one day graph pipeline graph is built. We start with the Like, with the, let's say, vertex, which is supposed to be an exporter or something, then we go… I've…
**jmacdonald** 34:43 Yes, the whole pipeline can be restarted in topographical, I think is the right… topographical order. But I believe what Blake is looking for, really, is to have smaller groups.
**Dmitrii Anoshin** 34:55 Correct. Why… it doesn't have to be groups, it's just when you restart something in the middle, that topological restart just has to partially update all of the receivers that the… all of the companies that depend on it, but do not touch those That… that… those that don't depend on it, essentially.
If that sounds…
**Blake Rouse** 35:20 Correct, yeah, that's correct. That's exactly what the, you know, I have a, like, a PR that does that.
Basically what it's doing, it's saying, like, okay, what's changed?
**Dmitrii Anoshin** 35:29 Yeah.
**Blake Rouse** 35:30 You know, what is that touching?
And only restart or rebuild what it's… it's touching.
**Dmitrii Anoshin** 35:36 Yeah, to reiterate what…
**Blake Rouse** 35:39 And it could actually be used as the main flow as well, because if the config diff would notice that, oh, you know, you know, we have nothing existing, so we're going to create everything new. And so it could become the default flow, but obviously the way to do it was to obviously not have that become the default right off the gate. It would be with the feature flag.
**Dmitrii Anoshin** 35:58 Right, but we cannot live with Fisher for luck forever. Whatever we introduce is supposed to have some long-term plan, right?
**Blake Rouse** 36:06 Oh yeah, I mean, from our standpoint at Elastic, we would have it on all the time. We want to support it, we want to iterate on it. I mean, I would prefer to see it be the long-term path as well.
**Dmitrii Anoshin** 36:15 In a nutshell.
**Blake Rouse** 36:15 per se.
**Dmitrii Anoshin** 36:16 that's why Evan is talking about creating an RFC, because this is, like, an important change to the, like, underlying capabilities of the collector, so… And we have a kind of a policy that anything that touches those kind of internals would have to go through a thorough RFC process.
So, first, the DPR should not be adding, like, some proposed… proposing a solution with a feature gate. It should be an RFC with the, like, let's say, some design, Kind of… thorough design description of the… Proposed a solution, problem and solution.
**Blake Rouse** 37:00 Okay, perfect. Yeah, that's fine. That works for me. We can definitely write it.
I can definitely work on an RFC for this, yeah, I mean, I was supposed to bring it up in the SIG just to see, like, what's the process, you know, and it could be… be a no, but…
**jmacdonald** 37:15 Let's look for a connection with OpAmp. I don't know who the right person is, but I know that… well.
Someone can help, find us a partner there to help us in op-amp space.
**Dmitrii Anoshin** 37:29 Yeah, there are… we can look at the cod owners of the pump extension, or our pump supervisor.
**jmacdonald** 37:35 There you go. Let's do that, and then maybe bring them into a conversation and say, I have an idea for an RFC, this is what it's going to look like, and then you can get some feedback before… before it gets, you know, lands in a wider audience.
**Blake Rouse** 37:47 Okay, yeah, do that.
**jmacdonald** 37:50 I'm conscious of time, everybody. We've spent a lot of time here, and I don't want to… I don't want to run out. So, Andrew, yeah, let's do…
**Andrew Wilkins @ Elastic Observability** 37:59 I'll try and keep it quick. Yep, try and quick, keep it quick. I just wanted to raise awareness of a couple of proposals. One we talked about a few weeks ago related to multi-tenant batching. This has been going… ongoing for quite a long time, so I have a proposal here, which is to have configurable multi-tenant batching just for… at the metadata level in Exporter Helper itself, and then we'll have an extension interface that would allow… Oh, sorry, not an extension interface. We would have a processor, sorry, we went back and forth on this. We'd have a processor in Contrib that would allow, OTTL-based batching, which would produce metadata, and then that would feed into the exporter helper. So, anyway, if anyone here has opinions on how we should do multi-tenant batching, please have a read, and I'd love to move this along.
**Dmitrii Anoshin** 38:51 Yeah, I just want to add that we discussed that a few weeks ago, and, like, agreed on this approach, like, we had… a lot of back and forth. I was thinking that exporters should potentially provide any kind of Like, batching capabilities, not only on the metadata, yeah, metadata client key, but eventually we, like, ended up that this This is a good way to go and agree it on. If you have… anyone has other opinions, please go ahead. And it's still on me, Andrew, I gonna… I need to spend time and review the PR. I'll try to prioritize this for this week and do it.
Sorry for the delay.
**Andrew Wilkins @ Elastic Observability** 39:40 Alright.
**jmacdonald** 39:40 I…
**Andrew Wilkins @ Elastic Observability** 39:40 tricks.
**jmacdonald** 39:42 I also was trying to follow this feature, and I didn't realize someone had opened this, two, three months ago, so I would be glad to help. I always want to review batching logic, And… I'm glad to hear it. There was someone working on this, like, 8 or 10 months ago that it didn't seem like it ever arrived, so I'm glad to hear it.
**Andrew Wilkins @ Elastic Observability** 40:04 Cool, thanks both.
The other one, I have an RFC open for introducing a new interface to the core, which is related to scraper receivers. So the… the point… the idea here is to enable, a different… different way… excuse me, different ways of… invoking a scraper. So at the moment, they're always timer-based. You have this scraper helper code, which has a controller config. Controller config has an interval and a delay and etc. I want to introduce a new interface which would allow Let's say, for example, a job queue, or, like, some kind of work queue, so you could poll it for, Some signal to… to invoke a scraper.
Or, you might want to do a one-shot scrape through a CLI command. And the whole point is to, like, the reason why I'm interested in this is so we can horizontally scale scrape receivers. At the moment, you can't effectively do that, because… You would need to somehow orchestrate the configuration across a fleet of collectors.
So you could, for example, use a Kubernetes cron job and, have the collector start up, run a scrape, and then exit.
That's the sort of thing we're trying to enable.
So, please have a read. If you've got any comments, let me know.
**jmacdonald** 41:32 this… okay, this is, as I understand.
a new RFC that we should review, thank you. And… I wonder what Dimitrius thinks, because I think you're an owner of scrapers… the scraper Package.
**Dmitrii Anoshin** 41:51 Yeah, we discussed that as well.
**jmacdonald** 41:56 Must have missed a meeting. I don't… I haven't seen this.
**Dmitrii Anoshin** 42:01 I'm, yeah, I… I was thinking that there might be some other solution for this particular problem.
But, no, I haven't.
come up with anything, then I think that kind of makes sense to provide some.
Girl.
customizable experience to invoke scrapers in general. It might actually be useful for, let's say, fast environments when you want to Run a collector only once.
And scripts often.
And then… Thinking that potentially can be the right approach for those as well.
But yeah, it's still… again, I need to look on the RFC, and maybe we'll review it, and… If anything, it comes up.
Any alternative, or… I'll comment on this.
**Andrew Wilkins @ Elastic Observability** 42:59 Thanks. One other thing I'd like to draw attention to in there is that there's… maybe we would want to have some way of parameterizing the scrapers through an event, an external event, like, you know, you put in the config for scraping Prometheus, and then you have the Prometheus endpoint in the work queue.
That could be done through some… something like the receiver creator, sorry, yeah, receiver creator.
Where the… it's templated. So… yeah, anyway, just look at… there's a comment in the… in the RFC, left.
**Dmitrii Anoshin** 43:30 Okay, I'm also wondering if we can actually, instead of complicating the, is, scraper interface, we can put that capability to address your creator.
In general, to solve your problem.
like, receive your creator, make it… let's say, I've had an ability to, like, temporarily bring something up, or something like that.
Anyway, I'm… I probably… you probably thought about it already, and I'm… I don't want to… complicated as I'll probably better read the RFC and comment.
**Andrew Wilkins @ Elastic Observability** 44:20 Thanks, that's all. That's it for me.
**jmacdonald** 44:22 I don't actually know what Receiver Creator is. More to learn.
Look, we made it to Lyudmila.
**Liudmila Molkova** 44:31 Yay, thank you. So, I have a very little context on the collector, in the collector world, and I hope to get some context from you folks, and maybe identify some next steps. So, there are a bunch of pull requests. Some of them are already merged, some of them are in flight.
But they add… Some things to database receivers.
And the messaging receivers would be in the same group, just nobody got to them yet.
And the core question… is what do we do with resource attributes? Let's say with service.
So, if we… Don't set them, then maybe they will be set later on, but by, let's say, Kubernetes resource detector.
If I set them, then nobody will be able to override them.
Both are bad, because no service instance ID means something very bad for, let's say, Prometheus, and everybody, maybe everybody else.
Having it… results, and that sale receiver says, okay, I know how to populate service instance ID for these metrics.
But pod logs would have something else set by the processor.
So, the first question is, how do we think about collector receivers, collector components, setting resource attributes, and if there is any policy in the collector?
rounded.
**Dmitrii Anoshin** 46:11 The resource attributes are being set by the receivers.
But the service resource, the service entity, it's a bit… it's a bit, like, different and, like, vague here. So… let's say, let's talk about, like, Kubernetes-related receivers.
they always set entities where they met… which metrics they are… they are providing data for. So, for example, pod resource will… would have all the pod resource attributes with pod metrics, and, like, let's say, node… node resource will be set as well. But for the service, it's a bit different.
To clarify, we don't have any processors that would say… that would set service without, like, some kind of… like, just by themselves, right? So, for example, we have Kubernetes attributes.
processor, which would potentially can set those, but in order to get that, they will scan, like, annotations of the pod, and it will be clear, like, Signal that this is the service name, or something.
**Liudmila Molkova** 47:31 Yeah, except if we see service name or service instance ID, or any resource attribute already present.
the Kubernetes, processor will not update it, it will back off. I have an issue for it, and I think this is a bug, which should be fixed.
**Dmitrii Anoshin** 47:48 Yeah, but that data… so Kubernetes Attributes Processor, it populates data that are being sent through the collector with the push model.
From some external applications.
let's say you have a Postgres database, and it sends traces?
And in that case, Kubernetes, like, it would be sent from the outside, and from some pod, and then Kubernetes attributes processor would fetch data from that pod, from Kubernetes API. But here… But here, we are sending data from inside the collector, so Kubernetes Attributes Processor will not be effective at all. It will not do anything, essentially.
Because they're…
**Liudmila Molkova** 48:33 I think it should, because user explicitly told, okay, I want the service name on all the pods.
**Dmitrii Anoshin** 48:41 No, no, we, data that are being scraped by the specialized receivers.
They don't… like, being… they're not being, Enriched by the Kubernetes.
Because… actually, Kuberant's attribute processor is, like, very complicated, you can configure it in many different ways.
But, like, by default, you need to specify the association, which will be used to get, like, idea where the data is coming from.
**Liudmila Molkova** 49:17 Okay. Alright, so I, I want to be… yeah, go ahead.
**Dmitrii Anoshin** 49:20 I just want to say that it's… I think it's okay to set service by the receivers themselves.
But I guess your point is that we need to ensure that consistency is preserved. We shouldn't, like.
**Liudmila Molkova** 49:35 Yeah.
**Dmitrii Anoshin** 49:35 It ends up in a situation when service name is set, it cannot be, like, let's say if logs are collected, they have different service name, etc.
**Liudmila Molkova** 49:44 Yeah, yeah, so, like, some, some, consistency and the same set of attributes everywhere. Okay, it sounds like I need to maybe understand more and, And… understands where this problem comes from. The second problem I think we don't have anybody who owns the Postgres receiver, so it's very special, because it sets things like database name, the schema index table, two resource attributes.
And it's somewhat inconsistent.
Because other receivers don't do this, it's also very specific to certain signal, right? If I send a query that covers multiple tables, what would they do? So I think the proposal, We have is to… Put them to metric attributes.
and remove from resource attributes, but we'd need Postgres.
receiver owners to share their thoughts. Is it right?
**atoulme** 50:57 Yeah, I mean, they don't… they're not the most active people, but we have 3.
Anton Block, Ishin, and Caleb Hirschman.
**Liudmila Molkova** 51:08 Yeah, I'll try to hunt them.
**atoulme** 51:12 So, don't be shy, you can ping them on the PR. If they don't respond, I just go to Hotel CollectorCollector Dev on Slack, and I ping them there, pointing back to the PR.
**Liudmila Molkova** 51:23 I tried both, but okay, I'll try DMs.
**atoulme** 51:27 Hmm.
It's not good. Yeah, I mean, so if there is any, this is just pure bureaucratic process here, but at the scale of control, we have to work like this. If any code owner is not responsive.
After a period of time, we declare them inactive, we open an issue to ask them to move to a merited status based on the evidence, and if they respond and want to continue to be our code owners, we grant that.
If they don't respond, then we move them to Meritus, and then if there are no code owners left on the component, we just let go of the component as deprecated and maintained, and 6 months in, we remove it.
And there's just no sentiment or emotion to be had, this is across all components at the same pace. And usually that puts everything to… a very clear picture, very quickly, so… Also, if you're not getting the involvement you need from that receiver, I don't think you should spend time on trying to make their life better unless they want to play along.
**Liudmila Molkova** 52:26 Okay.
Thank you, I appreciate the advice, and…
**Dmitrii Anoshin** 52:33 Speaking about, like, attributes, whether they go to resource or to metadata point attributes, that's actually also pretty good.
thing that we can have from semantic convention or, like, specifications to provide some guidance. So, from my understanding, like, for example, we have host metrics receiver, and host matrix receiver produces.
some metrics for the host as an entity, and some metrics for the process as an entity. And we have process as an entity with all of the resources added there.
But, like, for example, if we are talking about namespace in the database, Potentially, if we don't… Like, if we don't define that as an entity in semantic conventions, we can say if it's not an entity, everything should… it should be a data point attribute.
That potentially can be the guidance. Or another potential guidance is that if reaggregation over that attribute is, Like, let's say… easy, like, the more… pretty common, right? You have a metric, you either want that metric to be reported across the… for the whole database, aggregated, or for a specific particular namespace.
And if that aggregation is pretty common to be applied, we have capability in the collector to aggregate at the source. So in that case, we can say, this is the recommendation, go ahead with data point attributes instead of resource attributes.
Something like that. Does that make sense? My point is that we need to have some kind of guidelines, I guess, in general, not only for particular Receivers.
**Liudmila Molkova** 54:23 Yeah, we should have certain database server semantic conventions. We don't have them, and if we do, we probably would have them in the collector, because it's the only place that have this instrumentation so far, and we are trying to not take something into semantic conventions that's not generic enough. But yeah, I agree. We should have the guidance documented in wherever it is.
**Dmitrii Anoshin** 54:52 Sounds good, thank you.
**Liudmila Molkova** 54:53 Thank you.
**atoulme** 54:56 Make sure we don't have… Database semantics outside?
**Liudmila Molkova** 55:01 We have client, but not server. Oh, you mean outside hotel?
**atoulme** 55:06 The outside collector, I could see that.
I mean, I could see how you could… you could have the Java SDK perform database monitoring Stuff.
Ugh.
I don't know.
Okay.
I… I'm getting my head ahead of the curve on this one.
**jmacdonald** 55:31 Somehow this makes me want to use scope attributes field that never gets used in OTEL for reasons that I'm not quite sure of, but just a… just a comment.
for various database concepts, to avoid making them per-metric attributes, like, let's have per-scope attributes, maybe.
I, well, we're coming to the end of the list here, and the hour. I did look over the Go release notes, like, garbage collector improvements, that could be big for us, That's what I have to say.
I don't think the improvement in generic Handling is important to anybody here.
Last thing, then, we have something about configHTTP…
**Andrew Wilkins @ Elastic Observability** 56:28 Yeah, I don't think we'll get through this in 4 minutes, but I can try and briefly summarize.
So we have a problem with the ordering of OTel HTTP instrumentation in the config.http package. So configHTTP, when you get a server config, you call this toServer method to get back an HTTP server, and you pass in a handler.
Typically, receivers will pass in a MUX, like an HTTP serve MUX, and they'll have already registered their routes.
But it's… So what we end up doing is we instrument the mucks, and that means that we don't have access to the… the routing information until after it's happened. So really what we should be doing is I think what we should be doing is somehow returning a ServMux, and then allowing the receiver to register routes with that, and then have them instrumented on the way in, as they're registered. That way, the OSHL HTTP instrumentation is after the path routing.
And that's… everything would just work then in OTEL HTTP. The problem that actually… like, the problem that ends up happening is that we… we don't know what to name the spans, like, we can't name them correctly, and we have to have all these awkward workarounds, to pass the… pass the pattern up the stack and whatnot.
So if anyone has opinions on that, have a look. I do have a kind of kludgy workaround for it, which I've described right at the end of the issue, which is that we can identify whether the user has passed in a ServMux specifically, and then wrap it so that we intercept the requests and do some kind of nasty things. Anyways, there's a couple of options in there. Have a read and let me know.
**jmacdonald** 58:20 Interesting. I caught… you caught my ear with middleware stuff. I remember… okay, I have to look into this. I will have time tomorrow.
I also have a hard stop, it's getting really dark outside, I gotta go help my animals.
I'm gonna… I'm gonna hang up. Bye, everybody! See you next time.
**atoulme** 58:40 for covering it. Thanks.
**jmacdonald** 58:41 Yeah, cheers.
**Liudmila Molkova** 58:42 Good luck with your animals.
