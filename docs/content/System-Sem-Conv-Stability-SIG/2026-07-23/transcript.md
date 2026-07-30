SIG: System Sem Conv Stability SIG
Date: 2026-07-23
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Donal O'Sullivan** 00:39 Whoa.
**Igor Peschinskii** 00:42 Boom.
**Christos Markou** 01:29 Hello.
**Donal O'Sullivan** 01:32 Hey, Christos.
**Igor Peschinskii** 01:35 Oh.
**Christos Markou** 03:02 it seems that the Linux Foundation account actually automatically The name and the company that you work for.
**Braydon Kains (Google LLC)** 03:12 Yeah.
**Christos Markou** 03:13 It added Elasticsearch.
Because I joined from another Zoom account.
**Braydon Kains (Google LLC)** 03:20 Yeah, I've just left it as Google LLC. I've been too lazy to change it out, because I put, like, remember my name for future meetings.
**Roger** 03:30 But you need to be locked in, right, on the Linux Foundation account, I guess.
**Braydon Kains (Google LLC)** 03:35 You do need to be, but… I think I could… I could change the name to remove the company if I needed to.
**Roger** 03:42 Okay.
**Donal O'Sullivan** 03:46 I think I logged in with my GitHub, so I don't seem to have any affiliation on my name.
**Braydon Kains (Google LLC)** 03:53 Oh, interesting. Yeah, for me, it was… I logged in with the… Email… the company email, and it was… it's the same company that I used to sign the CLA.
**Donal O'Sullivan** 04:03 the word.
Yeah.
**Braydon Kains (Google LLC)** 04:06 I think Pablo said he couldn't join today, so… This is probably who we're getting. Maybe Dimitri will join in a bit.
**Donal O'Sullivan** 04:32 Yeah, I guess I can start if no one else has anything to talk about.
**Braydon Kains (Google LLC)** 04:37 Sure.
**Donal O'Sullivan** 04:38 Yeah, I actually haven't added it into the agenda, but Yeah, so I'm making good progress on… I think it's essentially done migrating the process scraper to… release candidate.
Just came across a few hiccups with mdata gen, I have to open up very small PRs just to fix bugs in the version metrics, very, very small things. But, it's working. I have to open another PR in OpenTelemetry Go.
for the SDK to add the latest Science Conventions package, where the release candidate was added.
So that's fine, but… while doing the work, there's… and I was talking to Roger about this earlier, there's 3 metrics that are not even… they're not in… well, there's 3 metrics in the process scraper that are not in the process namespace in semantic conventions, 2 of them are in the systems namespace, and one of them just doesn't exist in semantic conventions at all.
I don't know, what do we do there, do we…
**Braydon Kains (Google LLC)** 05:40 Which one is the one that doesn't exist in semantic?
**Donal O'Sullivan** 05:43 I'll actually put a list into the doc there, just make it easier. Sure.
Sorry if I can find my documents.
Bear with me one second.
Where's the dock gun?
Yeah, so… process disk operations, process signals pending, and process memory utilization. So I think, process disk operations and memory utilization are both in the system namespace, and then process signals underscore pending just doesn't exist.
**Braydon Kains (Google LLC)** 06:28 Hmm… I think all three of these probably should be in the process namespace.
This… System memory utilization one, I think, is… is, and system disk operations are both measured differently.
Like, they're measured for the whole system versus just for one particular process.
**Donal O'Sullivan** 06:57 Yeah, that makes sense.
**Braydon Kains (Google LLC)** 06:58 Oh, nice.
So probably the answer is we need to get these into Semantic conventions.
signals pending… also somewhat straightforward, although I don't know… If you could… Actually instrument that.
without PROCFS?
like, if there was a way on Windows to do it, or BSD, I don't actually know for sure.
So we might have to look into that, because that might trigger a… Like, this is an OS exclusive, and I have to name it accordingly.
Realistically, all three of them should get into semantic conventions, though, I think.
**Donal O'Sullivan** 07:38 And they all should be in the process namespace, right?
**Braydon Kains (Google LLC)** 07:41 I think so, yeah.
**Donal O'Sullivan** 07:42 Yeah. Okay.
**Braydon Kains (Google LLC)** 07:44 The system disk utilization and memory utilization… sorry, disk operations and memory utilization can both still stay in system as well, like, they'll end up measuring different things.
**Donal O'Sullivan** 07:53 Yeah, makes sense. Yeah, I can… Yeah, I can look at it, I can create an issue in semantic conventions and… Cut a PR or something like that, sure. Okay.
Thanks, Braydon. There was just one other question I had.
if we're going release… so if we're using the, metrics and attributes that are release candidate, what stability level do they get in the process scraper? Do they stay at… so I think the majority are… I think they're all development. Do they just stay at development, or… for now, I guess?
**Braydon Kains (Google LLC)** 08:29 There's no release candidate stability in the collector, is there?
**Donal O'Sullivan** 08:33 No, no, I think if you look… I think it's defined in mdataGen, but yeah, it goes from, like… Is it alpha, beta, and then to stable, I think? There is no release candidate.
**Braydon Kains (Google LLC)** 08:47 maybe we call the V2 ones… Beta.
**Donal O'Sullivan** 08:52 Yeah.
Okay.
**Braydon Kains (Google LLC)** 08:55 Probably, like… Release Candidate is essentially us saying they will be stable soon, once we're sure, but… It probably doesn't mean we should rush them to stable in our implementation in case something does… need to change. Yeah.
**Donal O'Sullivan** 09:11 Yeah, yeah.
**Braydon Kains (Google LLC)** 09:12 Beta probably makes sense.
**Donal O'Sullivan** 09:14 Okay.
It's okay to go from, like, dev to beta, is it? Like, skip alpha or whatever?
**Braydon Kains (Google LLC)** 09:20 Yeah, I think we're in kind of a weird place where all these metrics are in development, but they're honestly grandfathered into stable, because everybody's using them and have been for, like, 5 years.
**Donal O'Sullivan** 09:31 Yeah, yeah, yeah.
**Braydon Kains (Google LLC)** 09:32 So it's kind of a weird scenario. I think this is basically us just saying, like.
cut our losses, these old… I mean, if we wanted to make it formal, we could go back to the old metrics that are gonna be deprecated soon, call them stable, saying these are not going to change anymore because we're migrating to the new schema. I would also be okay with that.
**Donal O'Sullivan** 09:57 Sorry, say that again, so you would migrate…
**Braydon Kains (Google LLC)** 09:59 Basically, so the original… the old metrics, the old schema, mark those as stable. So, basically, like, these are… these are de facto stable, so we're just saying they're stable, but they are going to be deprecated soon because of the new schema.
**Donal O'Sullivan** 10:15 Yeah, yeah.
**Braydon Kains (Google LLC)** 10:16 If we wanted to communicate it that way, we could.
Yeah, I hear you.
**Donal O'Sullivan** 10:21 Valuable.
**Braydon Kains (Google LLC)** 10:22 But…
**Donal O'Sullivan** 10:23 would you have people arguing then, why are you marking this as stable if it's changing? Yeah.
**Braydon Kains (Google LLC)** 10:27 That's… that's basically, yeah, like… the… The argument is… it's… it's weird for us to go from development straight to what will soon be stable in the new schema.
And our argument is… We've been way too lax on… On upping things from development to future stages. So these are basically just, like, de facto stable.
**Donal O'Sullivan** 10:52 Yeah, yeah, yeah.
**Braydon Kains (Google LLC)** 10:53 We're scared to change them now because of how many people are using them, so…
**Donal O'Sullivan** 10:57 Yeah.
**Braydon Kains (Google LLC)** 10:57 we've been treating them that way, we just didn't write it down.
**Donal O'Sullivan** 11:03 Yeah.
**Roger** 11:03 Development in where? In the host metrics or in the semantic conventions?
**Donal O'Sullivan** 11:09 I see you.
**Braydon Kains (Google LLC)** 11:10 I mean, the host.
**Donal O'Sullivan** 11:10 In the re… yeah.
**Roger** 11:12 things like that.
**Donal O'Sullivan** 11:12 in.
**Roger** 11:13 I think in the receiver, we don't have, let's say, Parametric stability, but we have the… The overall scraper and the process, it's in beta, not in development.
Oh, okay, but… oh, no, no, now I'm checking, yeah, you're… so that's parametric development stability, yeah.
**Donal O'Sullivan** 11:36 Yeah, no, you're… you are, Roger. Yeah, yeah, like, the actual… The actual… the scraper is in beta, but then each metric is development, so yeah, it's… As you say, Brayden, they were never changed.
**Roger** 11:49 Okay, good, that all makes sense.
**Christos Markou** 11:51 I guess that's fine if we keep them in development.
Maybe for people that really know and have been using, these components.
there is this understanding that those are treated as kind of stable, but in general, I think we have an argument that we're doing this change because those were always in development. So, don't come after us, because you should read the docs.
see that everything is, in development, the component is not V1, so things are gonna change. We do it in a very smooth way, or at least that's the intention, but I think if we make them stable now, it's like… You know.
Putting a trojan into, into our area, and allowing people to complain, people that are not really, you know, familiar with these things.
**Braydon Kains (Google LLC)** 12:50 That's true.
Yeah, I agree. This is hopefully… not something that a lot of components are gonna run into, it's just that we happen to be… Making this large change on a component that has just existed for so long, with people just, like, running into production happily-ish, happily-ish, and not thinking about it, but… You know, we feel like we're doing the right thing.
But… Hopefully this won't happen. Hopefully, for future… Future receivers making this kind of transition, they're just… They're going from one beta schema to another or something, rather than our weird little stable, grandfathered-in by default kind of thing.
**Christos Markou** 13:40 Then…
**Braydon Kains (Google LLC)** 13:41 That's about…
**Christos Markou** 13:42 in general, I think the component… so… I think nothing, blocked us from start putting, release candidate metrics into the components behind the feature gates using the migration mechanism. Even if, for example, we realize that we missed 3 metrics from semantic conventions, we can still do the implementation.
Once we have them in ZoomAT conventions, we can port them back, and… while the component is not V1, the feature gauge will remain in alpha. At least that's the plan that we have for… we had for KH Attributes Processor, and… When the component is suggested for graduation to view on.
then there will be APR that will change the feature gates to beta.
And going from a 0 to V1, you are allowed to do breaking changes, so you will have a change look there, people will be aware of everything.
It will be announced that it is going to V1, so it's not gonna be skipped, for example, this information. And probably the feature gate should remain there for a while. I would say for… the whole V1, even V2, maybe? Just to ensure that people will have the time to switch back to the old behavior.
It's not a big deal, I guess, to just maintain the feature gates.
**Donal O'Sullivan** 15:10 Yep.
That makes sense.
Cool, so I can get those, those missing, metrics, add semantic conventions, and… I think we all… we're all okay with using, moving the metrics to better.
And Process Craper then.
the ones that are release candidate, I guess.
**Braydon Kains (Google LLC)** 15:39 Yep, I am okay with it.
**Donal O'Sullivan** 15:42 Okay.
Thanks, guys. I think that's everything I had.
**Braydon Kains (Google LLC)** 15:48 Igor the host ID, Pierre?
**Igor Peschinskii** 15:51 Yeah, I wanted to announce that I made a PR.
Summarizing what we've been discussing last month.
So… Any comments would be appreciated.
**Braydon Kains (Google LLC)** 16:04 I'll try and review it today.
**Igor Peschinskii** 16:06 Thanks.
**Braydon Kains (Google LLC)** 16:17 The only other thing I had is, I've been looking… this… these PRs that, Thompson Tomo's been making about, Well, the problem he's trying to address is… multiple… Copies of the same executable.
And differentiating between them?
The way he's trying to do it is by… Removing the executable path from the executable entity.
And adding an attribute to the process entity called Launch Path.
That's… not… Good to me.
I think that's bad, because… In normal process instrumentation.
There is no way you can possibly know at any given time that the current path of the executable is the one that it was launched with.
You can change the executable's path at any time.
So, it just is round about reintroducing the same problem that had me telling them to remove executable name.
From the entity in the first place.
So… I don't want this attribute.
I understand the problem he's talking about, where if the identifying attribute of a process executable is only the build ID and the hash.
Then two… if you reported two different entities.
But the identifying attributes are the same, even though the path was different. You can't tell that it's two different executables, two different copies of the same executable.
On a file system.
So, it would be good to solve that, but I don't think this is the right way. I think you actually need to introduce, like.
Unique file identification into the executable entity is the way to do it.
like, fundamentally, the path Is never going to be… Good way to identify something like this, because of the way it can just change at any time.
So, I'm thinking of suggesting Some type of new… generic file ID attribute, it'll mean… It'll be kind of a complicated definition, because it'll mean different things on different… operating systems, like, on Linux, it would be the inode number.
on Windows, they have their own file identification number of some kind, I don't remember exactly… how that works, and I think it's not unique to the system, just to the disk. I need to look into that a bit.
And… I think… And all Unix likes using inodes, I think.
I don't know, I need to look into it, but anyways, that's what I'm… that's what I'm thinking. If anybody has any other ideas or wants to… help come up with something that would be good, because I don't think this PR should go through the way it is right now.
**Roger** 19:26 And why is the hash ID that the profiling guys suggested can be used in this case?
**Braydon Kains (Google LLC)** 19:33 So, the reason it… the use case that James is trying to get working is… You have, like, literally the identical executable, but two different copies of it, and you want to be able to differentiate between them in your metrics backend.
**Roger** 19:52 And they will be in different paths, right? If…
**Braydon Kains (Google LLC)** 19:55 Yeah, they would be in different paths, but the path can't be the identifying attribute of the entity, because… or while it can't be an identifying attribute on a process, I don't see it as being a problem being an identifying attribute on an executable.
Unless you care that the identity of the executable changes with the path.
So maybe that's okay, but right now, executable path is a descriptive attribute on… on the entity. And so, how a metric backend would interpret it is that the same entity, the same executable, is churning its path over and over again, because two different time series are reporting
**Donal O'Sullivan** 20:36 Did you not put, like, the… Sorry to interrupt you. But, like, they have two different PIDs, don't they? Could you not have an attribute for the executable where it shows, like, it's PID?
In that scenario.
**Braydon Kains (Google LLC)** 20:48 So for the… for the process, you have the… on the process entity, you have the PID, and the creation time, and that identifies the process.
Something they originally wanted to do was also to have the executable be an identifying attribute of the process.
which doesn't work, because in a process lifetime.
You can always change the path to the executable.
**Donal O'Sullivan** 21:13 Yeah.
**Braydon Kains (Google LLC)** 21:13 that's… on Linux, at least, it's always allowed. On Windows, it's situationally allowed. But either way, you could always change that path, and we don't want that… a backend to identify that as a new process. So we moved… The path to be a descriptive attribute on executable.
but then, if you're only considering the executable and not a process running it, just the executable entity.
**Donal O'Sullivan** 21:35 itself.
**Braydon Kains (Google LLC)** 21:36 and two different time series are reporting it. It's identified by the hash, so he's… the backend sees it as one entity that's churning its path, rather than two different things.
**Donal O'Sullivan** 21:49 Yeah, you just need some unique identifier for that.
**Braydon Kains (Google LLC)** 21:51 Yeah.
Either we introduce, like.
a file ID, like a generic file ID like that, or we say we're okay with the… Path being identifying on an executable.
I think probably the former is more correct, because… Even if you move the same executable to a different path.
On Linux, at least, the path is just, like.
a place to find it, a way to, like, find it in a file system. It doesn't change its ID. It's technically the same file, even if you change the path. So realistically, the right idea is to introduce a new identifying attribute to executable, which is, like, the file ID for the operating system.
**Donal O'Sullivan** 22:41 Yeah, that makes sense.
**Braydon Kains (Google LLC)** 22:48 I'm gonna… I'm gonna comment on this… on this PR, basically saying this, but…
**Donal O'Sullivan** 22:55 Is he trying to instru… is he trying to instrument that, like, now, is it? Or is that why he wants it changed?
**Braydon Kains (Google LLC)** 23:01 Yeah, he is… he is trying to… instrument this. Specifically, he's thinking of, like, in Ruby.
he wants this launch path attribute to, like, be parsed a specific way for, like, a Ruby script, so that the launch path is actually the path to the script file that was launched, and not the path to the runtime executable.
**Donal O'Sullivan** 23:23 Yeah, I remember Florian talking about this, Pierre.
**Braydon Kains (Google LLC)** 23:30 And I'm actually okay with that attribute existing as, like, an opt-in. If you have some specific way that you want to parse this for, like, specific runtimes, like.
like, maybe that's fine, but he's talking about making process.launch path sourced the same way as the original executable path was, which is not good. We don't want that.
**Donal O'Sullivan** 23:49 Yeah, yeah, makes sense.
**Braydon Kains (Google LLC)** 23:55 And he's also talking about something related to, like, in… in .NET, They… they want… Like, to be able to tell which path was used.
To execute it, because they have two copies of the same executable, but… I guess they want to tell when it was launched from one path versus another.
I can't.
really think of… the use case.
I'm just kind of charitably assuming there is one that makes sense that I'm just not seeing.
That was all I had for today, I think.
**Roger** 25:01 Sounds good.
Should we leave it here, then, for today?
**Braydon Kains (Google LLC)** 25:06 Well… look at the Again.
**Roger** 25:10 See you.
**Christos Markou** 25:11 tiers.
**Donal O'Sullivan** 25:12 Anyways.
