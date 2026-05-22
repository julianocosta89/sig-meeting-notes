SIG: System Sem Conv Stability WG
Date: 2026-05-21
Duration: 29 minutes
============================================================

## Zoom Recording Transcript

**Braydon Kains (Google)** 07:28 I don't know if we're gonna get anyone else today at this rate.
Probably get started.
**Dmitrii Anoshin** 08:09 Overall.
**Braydon Kains (Google)** 08:15 Hello.
**Christos Markou** 08:35 Okay, I just saw that the first one, mostly heads up, don't understand today.
She sent… she has a PR for… The multi-schema migration.
I had a look yesterday, left some comments.
Seems to be to the right direction, I think, but, one issue is… When the metric remains the same, but the attributes change.
Yeah, so I left some.
Comment there, if you have the time to.
To take it away, as well, would be, helpful.
**Pablo Baeyens** 09:14 Is the… approach, they're going to be, like, the ATB1 or ATB0 for metrics with the same name?
**Christos Markou** 09:24 Yeah, I think the approach uses the… what we discussed, the… The at symbol, yeah.
Not the slash one. Yeah.
Dejapin, you want to go next?
**Giuseppe Ognibene | Coralogix** 09:51 Yeah, thank you. I just want to follow in the issue that I presented some weeks ago.
It's about a TCP UDP proposal.
I didn't see any comments, I know that all of you are busy, just want to know if… I don't know, we can just see, or I can just open the PR to get a review.
**Pablo Baeyens** 10:21 I… I haven't been attending this meeting for a few weeks because of various things, but, I… I do want to say that, Right now… We are trying to focus in general on stability, and since this is an additive change, it… It may be less of a priority than.
**Giuseppe Ognibene | Coralogix** 10:47 Great.
**Pablo Baeyens** 10:48 Stabilizing recurring things.
That doesn't mean, like, I mean, maybe somebody individually can… What do you think about? It may… It may take some time because of that, because we are trying to get, the metrics used by… They host my structure super… To be stable.
**Giuseppe Ognibene | Coralogix** 11:11 Okay, and just, I mean, I just want to know… I mean, I don't want to be a review right now. Also, in the meantime, I'm implementing all the metrics in Obi, so… just to have, like, a prototype.
Okay.
**Pablo Baeyens** 11:28 I mean, I think it would be very relevant if there's anything on your proposal that would… Change or affect the, other metrics that we have.
Oh.
**Giuseppe Ognibene | Coralogix** 11:42 Okay.
**Pablo Baeyens** 11:43 Because that would be important for stabilization.
If there is.
I think we should discuss it now.
**Giuseppe Ognibene | Coralogix** 11:54 Okay, I don't think that… there is anything in my browser that will change, stability. I mean, I just want to introduce some new metrics.
Like, for TCP and UDP.
Okay.
**Pablo Baeyens** 12:10 Yeah, okay. Yeah, and I think they are… align with the system network I.O. metrics, so, yeah.
**Giuseppe Ognibene | Coralogix** 12:17 I just sent some questions, because I'm not, let's say, semantic convention person, so I had some questions regarding, like, attributes, or if, It is the right place to put the matrix, Under system, or under network, and stuff like that.
**Dmitrii Anoshin** 12:42 I have a question. Is the motivation here to add those metrics because we are getting them in OB, right? And in OB, we need to be aligned with semantic conventions?
**Giuseppe Ognibene | Coralogix** 12:53 Yeah, so basically, we are implemented in Obi, but I know that some other projects have some similar metrics.
For example.
**Dmitrii Anoshin** 13:02 CPI.
**Giuseppe Ognibene | Coralogix** 13:02 FTT, but they all use their own, metric name, so we, we thought to be, we thought to just add a proposal, so we are all on it.
**Dmitrii Anoshin** 13:16 Yeah, that makes sense. And those metrics are specifically for the host, right?
**Giuseppe Ognibene | Coralogix** 13:25 Yeah.
**Dmitrii Anoshin** 13:26 Okay.
Yeah, makes sense to me.
I mean…
**Giuseppe Ognibene | Coralogix** 13:33 Go ahead, Jan.
Just to… I mean, the proposal is for TCP UDP, I don't know if… you may think to add some other metrics, and this is something that I'm working on, so the proposal is more or less aligned to what I'm working on.
**Dmitrii Anoshin** 13:52 And what you're working on is on obvious sides.
**Giuseppe Ognibene | Coralogix** 13:55 Yep.
**Dmitrii Anoshin** 13:56 Okay.
**Giuseppe Ognibene | Coralogix** 13:58 If you check the intro, I already implemented 3 to 4 metrics.
Because I saw the documentation that, I mean, before the proposal, it's good to have a prototype.
**Dmitrii Anoshin** 14:10 Yeah.
Okay, sounds good. Thank you.
**Giuseppe Ognibene | Coralogix** 14:14 Thank you.
**Christos Markou** 14:17 Would it make sense to bring folks from other projects that are implementing something similar, to bring them in and try to, come into an alignment?
And, I think from this group, if it doesn't affect what we have right now, if there is no specific intersection, and it's, like, their own thing.
Maybe we could be involved, maybe not.
The thing that should be followed here is that, like, the generic semant conventions.
guidelines, how to name things. For example, when you say, network UTP errors, maybe that needs to be named, like, network UDP error.count, for example, and stuff like that, but those are generic, for SMAT conventions. So… Yeah.
I don't know. Maybe it would also make sense to try with the semantic conventions maintainers, or the generic SIG meeting on Mondays.
maybe sharing what we discussed here, that the group is kind of focusing on stability, and what would be the right, path forward for you, so as not to be blocked on us, because I'm not sure how much time we will have.
In the near future.
this.
**Giuseppe Ognibene | Coralogix** 15:37 Okay. I mean, I'm not blocked, I'm implementing it in Obi. I know that if the proposal will be merged, there will be a lot of breaking changes in Obi, but I know that Regarding the… we had a question about, for example, UDP errors, count, I think that I brought a question, regarding something like that, because I mean, I'm trying to follow the already implemented metrics in the semantic convention, so maybe… I… I did some, like, errors.
If you can just check all… at least the questions, it can help me. But it's, as I said, it's not urgent.
**Christos Markou** 16:23 Yeah, I think it totally makes sense to coordinate with other projects as well, if they also implement similar things, and probably bring them in and try to collaborate.
**Giuseppe Ognibene | Coralogix** 16:38 Okay.
Thank you.
**Christos Markou** 17:09 Anything else for today?
Folks…
**Pablo Baeyens** 17:15 So, for the process?
The attributes are now, or are now going to be, release candidate on the next release.
And then we… Sorry, I don't remember whether we have to promote something else to release Candy A.
But…
**Braydon Kains (Google)** 17:36 The next step is the entities.
So there's… there's two. There's the… there's the process entity, and then there's the… process executable.
**Pablo Baeyens** 17:48 And… Do we consider that a blocker for… Adopting those semantic conventions on… The… On any component, really? On the compact component?
**Braydon Kains (Google)** 18:05 We… we consider, at the very least, the process entity a blocker for stabilizing metrics.
**Pablo Baeyens** 18:14 That's funny.
**Braydon Kains (Google)** 18:15 The metrics are designed such that, like, the identity… Of the metric is… is, like, essentially what it says on the entity. Like, the process ID is not on the metric, for example. You can't identify what process it came from without the entity, so… Process entities stable.
And we can then… we can then stabilize the metrics. I think we can hold off on stabilizing process executable, personally.
Because I think that's additive and not necessary for the identity of the metric.
So I think we can… In my opinion, we stabilize process, And then we can work on… and then, like, stabilizing the metrics is the next step after that. I don't think there's any blocker after that.
**Pablo Baeyens** 19:03 Okay, and… I know there were some open discussions from Thompson about… process executable, but I don't know if process entity has anything that needs to be.
**Braydon Kains (Google)** 19:17 I don't think so. There's… there's two… there's two weird… weird things right now in… across our entities. One of them is that For process executable, currently.
It's… you can't nicely… Model… Two different copies of the same executable.
Being run by different processes.
So, like, let's say if… two, like, two copies of a binary. The hash is exactly the same, so the identity being the hash, that… the hash thing that Profile… profiling invented.
They'll have the same hash, so they will be considered the same executable, which, like, technically is correct, like, they're the same… they're the same file, there's just different copies.
so, it… how that gets interpreted by… by backends… Like, we can't make the process executable path identifying.
Because that changes throughout the lifetime of a process.
So… either we come up with a way to identify files more specifically, like we start including inode or whatever version of things on different operating systems.
Or we stick to this sort of new idea of, like, entity joining, and say, like, the way that you figure out what executable is used by a process is you… the process… Is joined to an executable that has a path, and the path is descriptive, but that's how you know at a given time which copy you're using.
And… We don't make any guarantee that that's not going to change throughout the lifetime of the process, because you can move an executable During runtime, and that doesn't matter.
**Pablo Baeyens** 21:06 Yup.
**Braydon Kains (Google)** 21:10 I think probably the latter is the right way to go. I don't think… Because we do need to more… It introduced some more generic, like, file identification semantic conventions, like, this is… this is coming up right now on a mechanical level, not on a metric level, but in… in the file log receiver.
That currently uses just the fingerprint of the file to identify to, like, uniquely identify it. And, like, that works in some scenarios, and really not in others, and so there should be… Alternative ways of identifying files, but we don't… exactly have, like, a file entity, per se, that… where we say that the identity of the file is the… inode and the device, I guess, would be on Linux. Like, it would be different, it would be different on each… on each platform, but… All of that is to say that, like, process executable.
being able to stabilize that is kind of waiting on some of the… this sort of, like, entity joining stuff, or… I think it's called, like, telescoping… Identity.
I think that's kind of… The main blocker for stabilizing process executable.
Which, this is a pretty niche use case, this is just, like, Thompson Tomo brought this up, of, like, you want to be able to figure out which copy of a process executor you're using, like, I guess there might be a scenario where you might want to do that.
And then the other thing for process entity, which I don't think is a blocker on stability, but depending on how you instrument it, you could have PID and creation time clash if you're reading from different namespaces without identifying what namespace you're reading from.
So there presumably needs some sort of, like, process Linux namespace entity that can be joined with.
I don't think we have to block the stability of the process entity on that existing.
But that's technically a case where our identifying attributes aren't fully infallible without the introduction of this. I thought of it as being, like, maybe we should make an optional identifying attribute called, like, of the namespace name, but… It's… it seems that the… having… having a namespace entity is probably the more correct way to do it long-term.
I talked to Josh about it really briefly, and that was… that was his suggestion, so… Those are the two things on my radar. But I think… unless anybody can think of anything else, I think Process Entity is pretty… In a pretty good spot, like, pretty close to being stabilizable.
**Dmitrii Anoshin** 23:42 Braden, is the namespace something that can be… Hmm.
Is it optional in the system itself? Or it's, like, it's always present, there is some default namespace?
**Braydon Kains (Google)** 23:54 So, there is… the overall system?
And then there's, like, optionally, you can put something under a namespace.
**Dmitrii Anoshin** 24:04 Okay.
**Braydon Kains (Google)** 24:05 I don't actually know if the default system's considered a default namespace or not.
I should probably look that up, actually, but… But, like, majority of processes… probably don't have namespaces, let's put it that way, like the…
**Dmitrii Anoshin** 24:22 Fucker.
**Braydon Kains (Google)** 24:22 Yeah, and even the same… the same process depending on what namespace you're looking from, it has different… different attributes. So, like, a process spun up by a namespace would still have a PID on, like, the main system that is different than the PID under the namespace, but…
**Dmitrii Anoshin** 24:38 Oh, okay.
**Braydon Kains (Google)** 24:38 Under the namespace could be the same…
**Dmitrii Anoshin** 24:41 Okay.
**Braydon Kains (Google)** 24:41 Something else, something completely different within another namespace, basically.
**Dmitrii Anoshin** 24:44 So that it's always reflected on the… on the main, like, pit under namespace always reflected in the… as the other repeat in the… in general, right?
**Braydon Kains (Google)** 24:57 I'm pretty sure, yeah, I'm pretty sure, like, depending… depending… like, if you look from just slash proc, like, on the… on the.
**Dmitrii Anoshin** 25:05 Yeah.
**Braydon Kains (Google)** 25:05 mount point on the system. The process… every process under every namespace will be there, having its own, sort of.
like…
**Dmitrii Anoshin** 25:13 The idea.
**Braydon Kains (Google)** 25:14 Yeah.
**Dmitrii Anoshin** 25:15 Okay, in that case, we… there is no… I don't see a problem here, we just, like, we can say that, hey, you don't put processes under particular namespaces.
Like, we can just make a restriction. The PID, process PID, should be the PID under the proc, not under the namespace.
Does make sense.
**Braydon Kains (Google)** 25:40 Yeah, we could do that.
I'll have to… I'll have to take that away and think about that, because that sort of… that ends up potentially… the main way that namespaces are used, I mean, the most common is obviously container runtimes.
And the other thing is, like, people running SystemD services doing their own, like, weird control group stuff, but that's more rare than… Okay. I think the most common one is, like, say you create two containers at the same time.
Both of them will have a PID1.
under their namespace, so, like, the first container and the second. So, like, if two collectors were… Reading under that namespace at the same time.
But without saying they're reading from the namespace, then PID1 with the same creation time would then exist twice.
So we could say, like, don't read from the context of the.
**Dmitrii Anoshin** 26:36 Yeah.
**Braydon Kains (Google)** 26:36 Only report from the root newspaper. Yeah, we could do that.
**Dmitrii Anoshin** 26:40 So, in that PR, what I… for the entity telescoping, I said that specifically entity can have different, different scope identity types. So, for example, process can have, like, let's call it a parent for simplicity.
The process can have a parent as a host, or it can have a parent as a container.
In that case, like, if container is the most… the most typical use case for namespaces, we probably don't even consider that until… until there is a need. And we say that.
**Braydon Kains (Google)** 27:18 Oh, yeah.
**Dmitrii Anoshin** 27:19 process within the container have a parent context entity ID as a container, and that container has a parent of a host.
Or otherwise, if it's not containerized.
Process can be just under the host itself.
In that case, it should be fine, and this, like, notion of having different, like, let's say, parents for uniqueness of the identity.
They can be different, and if we have to, at some point, do that namespace into the picture, we can do it.
**Braydon Kains (Google)** 27:53 Yeah, okay, I think that makes sense then.
So we can… we can write that, like, if you're reporting a process against the host.
It is… it's, like, assumed that you're reading from the host, like, the system namespace, and not from a custom namespace. Yeah, okay, I think that that's probably fair, actually.
**Dmitrii Anoshin** 28:10 We can put it as a requirement, actually, if you… if you put…
**Braydon Kains (Google)** 28:15 Yep.
Okay, yeah, I'll… I'll… research and make sure that actually makes sense, that I'm, like, remembering right how this all works, and then… and then we can add that before stabilizing.
**Dmitrii Anoshin** 28:28 Sounds good.
**Braydon Kains (Google)** 28:29 Yep.
**Pablo Baeyens** 28:50 Thanks for explaining. Sorry, I haven't been able to attend this meeting for a few weeks.
I wanted to catch up. Thank you.
**Braydon Kains (Google)** 28:57 Yep.
That's fine. I haven't actually been able to work on System SEMCOM stuff as much, because I've been on a double on-call shift, so I'm… I'm… I've been quiet.
**Pablo Baeyens** 29:13 Whoa.
See you all next week, then?
**Braydon Kains (Google)** 29:19 Sounds good.
**Dmitrii Anoshin** 29:20 Thank you. See you.
**Braydon Kains (Google)** 29:21 Thanks, everyone.
**Christos Markou** 29:22 Thank you, bye.
