SIG: Kubernetes Operator SIG
Date: 2025-10-23
Duration: 52 minutes
============================================================

## Zoom Recording Transcript

**Antoine Toulme** 00:45 Ew.
**Benedikt Bongartz** 00:49 Blue.
**Mikołaj Świątek** 00:56 Benny, you okay?
Yep. Didn't you want to, like, turn on the lights or something?
**Benedikt Bongartz** 01:06 Oh.
It's actually not that dark, like, on the.
**Mikołaj Świątek** 01:11 You look like your screen is the only light source in your room, your head.
**Benedikt Bongartz** 01:18 Yeah, it wasn't too… bad, actually.
**Antoine Toulme** 01:23 Welcome back.
**Benedikt Bongartz** 01:25 Thanks!
**Mikołaj Świątek** 01:27 Welcome. How are you doing? Sleeping okay?
**Benedikt Bongartz** 01:30 Today, yes. Yesterday, no. So it's a thing I need to re-evaluate on a daily base, currently.
**Mikołaj Świątek** 01:39 Mmm.
**Antoine Toulme** 01:39 Yep.
**Benedikt Bongartz** 01:40 But yeah, so the majority of time, It works quite well.
She has some stomach issues, which is a bit odd.
So, which means sometimes it's… yeah, you sit there, you cannot really do much than just walking around and carrying her.
And wait until it gets better.
And, that's then the nights where you have not that much sleep.
But, yeah, it starts to be less an issue.
**Antoine Toulme** 02:14 I think I miss those moments.
You'll… you'll come to miss those moments. I'm just telling you, these two shall pass.
**Benedikt Bongartz** 02:23 So…
**Antoine Toulme** 02:24 Yeah, I enjoy. It's a… it's a magical time.
**Mikołaj Świątek** 02:32 Who are we waiting for?
**Antoine Toulme** 02:36 I mean, I don't know.
Jacob's always so good at managing the notes.
So…
**Benedikt Bongartz** 02:47 Miss him, though.
**Antoine Toulme** 02:50 It is…
**Mikołaj Świątek** 02:54 Did Jacob say he's not attending?
**Antoine Toulme** 02:57 No, I don't… I haven't seen anything from him.
**Mikołaj Świątek** 03:06 Kind of neck and legs, maybe 2 more minutes sometimes get stronger than drink.
**Antoine Toulme** 03:11 Good.
**Mikołaj Świątek** 03:19 I'm sure they have topics. We have the two…
or one… one recurring topic, and I've added another.
**Antoine Toulme** 03:27 Thank you.
**Mikołaj Świątek** 03:35 I think stuff to discuss at SIG already still has.
a bunch of things, but I think some of those are
spurious, so I'll just unhook them.
Because we've already discussed these, and just didn't.
Remove the label.
**Antoine Toulme** 03:56 Okay.
**Benedikt Bongartz** 04:02 And with the feature gate, we have this for native sidecar.
You think we can just remove it?
**Mikołaj Świątek** 04:12 I don't mean you, but actual… I shouldn't listen.
Yeah, technically, we have this for multiple releases in now, and…
**Benedikt Bongartz** 04:22 As far as I'm aware.
**Mikołaj Świątek** 04:25 Is it actually enabled?
**Benedikt Bongartz** 04:27 It should be enabled by default.
**Mikołaj Świątek** 04:31 You see my screen?
**Benedikt Bongartz** 04:32 Yes?
**Mikołaj Świątek** 04:35 So, in that case, let's just get started, and let's look at this.
Right, so I want to occasionally review the feature gifts, because for the past, we haven't been very good at tracking their life cycle, and just go through them… go through them and check.
Whether we should be doing something.
And yeah, the first time, the first one is the side-code containers, and you told me, Benny, you implemented this.
**Benedikt Bongartz** 05:06 Yeah, so now it takes,
So we added this discovery mode, so if your Kubernetes version is high enough and it's technically supported, you will use native sidecars. If not.
It's the old-fashioned.
And… Yeah, so this is enabled by default now.
**Antoine Toulme** 05:26 since…
**Benedikt Bongartz** 05:28 couple of releases, I guess.
**Mikołaj Świątek** 05:31 No, I'm okay.
**Benedikt Bongartz** 05:33 I'm okay, I would… I would just create an issue in that case, and track.
**Mikołaj Świątek** 05:37 what you're doing, Robert.
Usually, because once you move it to stable, it can't be disabled anymore, but I'm saying this also for the benefit, for my own benefit, because I keep forgetting how the FutureGate API works exactly, so… if it's in beta, it's enabled by default, but you can disable it.
If it's unstable, it's enabled by default, but you cannot disable it. If you try to disable it, you'll get a panic, but…
you can still keep it enabled. If it's stable and you have it enabled, that's still okay. After you remove it, even… obviously, even that is not okay.
So that's… that's what the progression is like. So the… Duh…
The set of releases where it's unstable is basically just to let people who have it enabled by default have it enabled explicitly somewhere to have the opportunity to turn it off.
So I'm fine. If you think this is… if you think this is fine, we have tests for it, and it's been on for a while, then…
you know.
Is this enabled for all sidecars?
**Benedikt Bongartz** 06:56 Yep.
That's when we adopted all the end-to-end tests.
I think it was before I left.
**Mikołaj Świątek** 07:04 Mine.
I'm… I'm good, then. Let's do it.
**Benedikt Bongartz** 07:30 Right.
**Mikołaj Świątek** 07:30 The other one is this… Golang, the GOMEM limit, and Go Max Prox.
But, from what I know, Golank now in 125 does that automatically, right?
**Benedikt Bongartz** 07:44 They support this in containers, right? Previously, you needed to set this, and now it detects something there was… I've seen this on the release notes, I didn't read it yet.
**Mikołaj Świątek** 07:58 I'm not sure if both of these, but at the very least, Go Max Prox, it does.
It does set it automatically. I don't remember if it sets COMEM limit according to the cgroup.
studying.
But there's also an extension in the OPL collector that does it.
So, there's, like, several overlapping ways you could set this correctly, and my feeling about this is that
It's an alpha.
for a long time. I don't know what Jacob wants to do with it.
I would be kind of inclined to just deprecate it, to be honest, since it's gonna be solved.
Upstream.
Russ?
You can remind me, Antoine, but the collector… the collector binaries are built using latest Go, right?
**Antoine Toulme** 08:55 Hmm.
Let me check.
**Mikołaj Świątek** 08:58 Like, they require, they require the previous one, but… but I think they're…
**Antoine Toulme** 09:04 Yeah, and I think when we build it, I think you are right. Let me just make triple sure of that.
**Mikołaj Świątek** 09:14 Longitude.
It's…
would be like…
**Antoine Toulme** 09:23 we use 1.5.0.
**Mikołaj Świątek** 09:28 Huh.
So, and, and like…
**Antoine Toulme** 09:32 Do you have a… do you want a link to the release notes in Go for the…
**Mikołaj Świątek** 09:36 OLA, 125…
**Antoine Toulme** 09:39 It's not…
**Mikołaj Świątek** 09:39 Bainer Awarego Max Prox.
But I don't know about GoMan limits, though.
**Antoine Toulme** 09:47 So you won't… so there's a note about container…
Then it's chat, okay, so we can put it in the notes.
For the, GOMEM limit?
**Mikołaj Świątek** 09:59 Hmm?
**Antoine Toulme** 10:04 There's nothing about that, there is notes, she knows it's already… Go work.
Fantastic.
**Mikołaj Świątek** 10:13 You're putting it under the sidecar thing.
**Antoine Toulme** 10:19 Doesn't… I don't think it's done. There's a proposal open right now.
Look, I have this, issue here.
**Mikołaj Świątek** 10:31 Nope.
**Antoine Toulme** 10:41 I'm not sure Gumame Limit is done in the same way.
**Mikołaj Świątek** 10:45 Jacob. It's good.
It's good, it's good that you're here.
Because we're talking about a feature flag you added.
**jea** 10:53 Oh, no.
**Mikołaj Świątek** 10:54 this one.
**jea** 10:57 Yes.
We could make this stable. I mean, I don't know why it's still in alpha, to be honest. This is, like, a thing that we should just move, because it's… good. There's no reason for this to remain alpha.
**Mikołaj Świątek** 11:10 The point that we've been discussing is that as of Go 125, at least the max prox is just Go standard behavior.
So we don't actually need to set it, I think. I think the… that can just go away, but I'm in favor. Goldman Limit, from what Antoine's saying, is still not.
No.
**jea** 11:32 Yeah, I do think we should set that. I mean, both of these are things that, we set in the charts, I think, so I think it's worth, like…
Doing it automatically for the… Operator CRs?
**Mikołaj Świątek** 11:44 Okay.
Let's enable it, and then we can just,
Eventually, we can… we can get rid of it, because it will just be a default, from the… from… from the Go runtime itself.
**jea** 12:00 Yeah, but for now, we'll keep it in, probably, right? Is that what you're saying?
**Mikołaj Świątek** 12:04 Yeah, well, because… because Goldman Limit, it sounds like, is still, not… In there.
The MTLS stuff, no.
It was still kind of…
There's still issues coming out about this. In particular, there's a recent issue where it turns out that if you set… if you provision two certificates, one of which is a CA certificate.
for another certificate. So what happens here is that we provision a CA certificate and use it to sign two different certificates, one for the collector, one for the calculator, and that's how we have mutual TLS.
And it turns out that if you give all of them the same duration, and they get renewed at the same time, you can get a raise condition. And you can end up with one of them signed with one CA certificate, and the other signed with a different CA certificate.
as I have been made aware. So there's, like, some funny, funny bits.
**Benedikt Bongartz** 13:03 In here…
**Mikołaj Świątek** 13:05 So this isn't yet ready to be enabled by default.
This one should never be enabled by default, I think. It's just here as an escape hatch.
Until… until we introduce proper configuration for the strategies.
**Benedikt Bongartz** 13:25 It should happen.
**Mikołaj Świątek** 13:27 This is just here, so, so, like, one particular egregious hole.
can be filled.
Well, we decide how that configuration API should look like.
Conflict defaulting is in beta.
Should it just go staple?
**jea** 13:50 Yeah, probably. No one's complaining about it.
I think it's the right move.
**Mikołaj Świątek** 14:04 Alright, you're… you're making…
**Benedikt Bongartz** 14:08 Yeah, so…
**Mikołaj Świątek** 14:10 Again, make an issue to… to move it to stable, and just track it, move it to stable, and then one release later, remove it. The only reason there's, like, stable and then removal is to give…
Users, one version worth of.
**Benedikt Bongartz** 14:28 Of warning.
**Mikołaj Świątek** 14:30 Be able to… to remove that, if they're actually setting this.
on their alum.
And these are relatively new.
So… so I would not touch them yet.
This is Alpha, and Pavel isn't here.
I don't know what this is. What is this? It doesn't have a roof register conversion.
Stanza.
**Benedikt Bongartz** 15:02 That's relatively new, I guess. This is,
to automatically create network policies for the OpenTelemetry operator.
And the collector, I think.
Pavel was adding this, in the past.
**Mikołaj Świątek** 15:22 Why is this a feature gate and not a setting on the collector?
**Benedikt Bongartz** 15:27 It's also for the operator itself.
**Mikołaj Świątek** 15:30 But the operator has a separate one here, right?
**Benedikt Bongartz** 15:33 shouldn't… Dan, I don't know, to be honest.
I didn't even know.
**Mikołaj Świątek** 15:43 I don't have to do anything with them right now, but…
**Benedikt Bongartz** 15:46 Delperance.
**Mikołaj Świątek** 15:49 I'd like to eventually understand.
Alright, there's, like, some…
Some forward movement. I have… I have… I have now removed the feature gate that causes
collectors to use the target allocator CRD by default, for the record?
That is now removed. It's been on for a long time and hasn't generated any issues. In fact, it has generated numerous issues where people are like.
I want to add this field to the embedded target allocator, and I have to tell them, no, use the target allocator CRD, where you can just set it right now.
Alright, on that note, Jacob, do you have anything you want to talk about before we go to the…
Tagged issues.
**jea** 16:50 Yeah, maybe just wanted to get, quick thoughts on, kubeCon, because…
I know I'll be there, Antoine will be there, nikolai and Ben, are you gonna be there?
**Mikołaj Świątek** 17:04 No, and… in Atlanta.
**jea** 17:08 Yeah, in Atlanta.
**Mikołaj Świątek** 17:09 Nope.
**jea** 17:11 Okay. I just wanted to check, I'm gonna try and run…
I think I put in a request for us to do, like, an operator session, again, like, at the booth. And so…
David, I assume you're gonna be there, is that an incorrect assumption?
**David Ashpole (dashpole)** 17:26 I'll be there, yeah.
Okay.
**jea** 17:30 But yeah, so I was thinking, going over some, like, next steps. I really want to begin on the instrumentation stuff that I keep putting off,
the injector project that Antoine and I work on, I'd say mostly Antoine works on and I review for.
Is going well.
with the Dash Zero folks, and I'd really like to begin doing an instrumentation rewrite, to actually incorporate their work, more effectively.
Because I really want to get rid of that old code… code path, because I… I…
really don't like reviewing it and looking at it. Makes me sad.
So, I think that's one thing that I want to discuss, is sort of just drawing out a vision for that, and then drawing out a vision for…
The actual, like, architecture, for that as well.
But is there anything else that you would like for us to discuss there?
**Antoine Toulme** 18:36 I'll just point out that when we're at CapCon, Gina Jane will be with us. She's been working towards having this additional CRD for the network cluster observability, for the cluster observability CRD, so she's going to open that PR anytime soon.
**jea** 18:53 Great.
**Antoine Toulme** 18:54 Hopefully this week.
And then, all going to be able to have some level of discussion, review. Benny was… because he's just back, was reaching out, like, where are we on that? He's going to kind of do some review of this.
And she'll be there at the observatory, so we could have a meaningful discussion. If you have any feedback at all, you know, we can go at this, and
doesn't have to be particularly, private, we can invite more people, so we can do, like, a SIG meeting of sorts and discuss this type of stuff.
So, hopefully it's really the… It's freezing enough to have a party, and, you know, dude, it's…
David makes 4, maybe it's a… it's a whole-blown, like, submitting right there.
**Mikołaj Świątek** 19:37 Jacob, do you also want to…
Is everyone okay? Because my Zoom is… must be behaving now.
**jea** 19:48 No, I can see your cursor and hear you fine.
**Antoine Toulme** 19:53 It's just, you know.
**Mikołaj Świątek** 19:54 Yeah, okay.
**Antoine Toulme** 19:56 We see your, we see… everything. Here, we see the… the chrome.
**Mikołaj Świątek** 20:00 Okay.
So…
Do you also want to… do you also want to… because I saw… I also saw Jurassi's message.
Asking whether we have any updates.
And I think our update is basically that we've added enough tests for all sorts of things that we're now more confident in making changes to them.
Which I'm not sure if that's, like, an update that we actually want to share, but we do actually have… we have tests for…
both the latest instrumentation versions, and the defaults that we have, including, like, actually more tests that try the instrumentation and check whether they actually work, and they do catch rings. We also have tests which
catch bugs in actual collector releases. Now, those are also running nightly on, contrib. So, we've made an effort, like, an effort towards stability, right? I don't think we actually have, like, a major feature that we wanna…
show off, unless you guys have done something that I am not aware of.
**jea** 21:10 I think, if we can land the cluster stuff that Antoine and his colleague have been working on, that might be a thing to call out.
But I don't think that's necessary. I mean, I…
I think the testing stuff is good, but that's more, to me, of, like, an internal GC thing of note, maybe? Where it's just like, hey, you know, we know that there's a big stability push in the project, and as part of that, like, we are running, far more tests that increase our release confidence by…
You know, a significant margin, something like that.
I don't know if you, if you all looked at the,
CNCF, like, graduation notes that were posted in the maintainer's channel.
But a lot of that is around, like, release confidence and stability. I talked with Austin recently about this, and ultimately, it's like.
Us getting to, graduated status is just all about, like, stability, functionally, and doing both nightlies, but also, like, quarterlies, rather than week… like, weekly, bi-weekly cadence.
And then being very confident that each of the releases has an amount of stability.
So, I think that we're working towards that really effectively. I don't think we need to, like, call that out and…
I don't know how much, like, users will be interested in that.
**Antoine Toulme** 22:34 The operator was mentioned at some point by Austin during a maintainer call this week.
He mentioned that some people were signing that the operator was stable, or in some sort of stability that I don't think
We're at. David, yeah, go.
**David Ashpole (dashpole)** 22:48 I think it was more… Users expected a project like OpenTelemetry to have a stable operator.
Not that anyone read anywhere that
The thing we have is stable, just that, like.
It was an assumption that people made that was incorrect.
**Mikołaj Świątek** 23:08 We don't even have a stable collector.
**Antoine Toulme** 23:12 No.
**David Ashpole (dashpole)** 23:13 That was also called out.
But yeah, things that people expected to be stable for a project like ours are a collector and an operator, right?
But that's, yeah, just not the case today.
**Antoine Toulme** 23:29 even if the operator is stable, even if it did a really good job and everything in the operator is stable, then you're distributing a collector which is now stable. So, that's also brought up.
**Mikołaj Świątek** 23:39 But I think…
**Antoine Toulme** 23:41 put a big warning on the README or something, right?
**Mikołaj Świątek** 23:45 I mean, does that actually make any kind of difference? We haven't… we're not promising anything, and it's definitely used in a lot of
Environments where stability is a requirement, and nobody really complains, nothing really blows up.
No, people are complaining.
**Antoine Toulme** 24:03 now, the graduation process for pentometry is hitting a little bit of a set of difficulties, because
the feedback that the CNCF is getting is that people had issues with breakage or whatnot, and they're reporting that back to us as a… as a maturity sign that we're not quite ready.
**Mikołaj Świątek** 24:26 Okay. Is it about the operator projects?
**Antoine Toulme** 24:30 The whole, like, it's just, like, this vibe.
**David Ashpole (dashpole)** 24:33 I take this.
Most of the complaints were around the collector.
But that some of them, at least, were around the operator.
But I…
**Mikołaj Świątek** 24:43 I'd love to hear, I'd love to hear them. I think.
I think our radar stability is actually pretty good.
**David Ashpole (dashpole)** 24:48 I was in the call, and they weren't, like… they were basically, like…
We don't want to share any details, because we don't want, like.
to… one, we don't want you to focus on, like, yes, this particular breaking change that Antoine made the other day is what failed graduation, like, hone in too close on, like, some particular thing, right? That… and two, they didn't want to, like, necessarily give away
Who the customers were, or exactly what their stack was.
But it was more just, like.
like, they got… like, they want us to think about it more generally, basically. Like, there's a lot of things that people depend on.
mostly the collector, but I guess the operator came up with SDKs, for example, that are marked unstable, that,
people who have adopted OpenTelemetry.
Decided to use and end up being bitten by at some point in their, like, implementation journey, right?
the feedback is meant to be general. And, like, I don't know if this SIG is, like, under a super tight microscope?
Cause I think…
the collector definitely has most of the focus, in terms of, like, the thing that everyone thinks should be stable but isn't. But…
I still think, like, Taking the spirit of the feedback.
To heart as much as he can.
Without taking it, like, personally. And given, like, whatever, like, Resources and stuff.
we have.
It's, like, totally reasonable, yeah?
**Mikołaj Świątek** 26:24 Out of curiosity, I'm actually looking for the changelog, for a changelog right now under the braking changes section. And the braking changes are pretty much all either things that are just us relaying a braking change that happened somewhere else, that we are just forced to…
to tell users about, or just, flaming, enabling, or removing feature flags, which are… in practice, in practice, that's not actually a breaking change to anyone's behavior, but it's a breaking change that, like, a feature flag becomes unusable, to basically separate those.
**David Ashpole (dashpole)** 27:01 Yeah, I wouldn't be surprised if you guys get blamed for a lot of things that are actually just breaking changes to the collector, because…
you really…
**jea** 27:09 Yeah, I mean, we get that with instrumentation as well. I was saying… I was, like, expressing this frustration to Austin, where I was like.
we are very close to… we're, like, sort of the closest SIG to actual, like, customer deployment, and so when things go wrong, we tend to get people who complain to us about things that are, like, not within our control. I'd say it's gotten better. I think that it used to be a lot worse, as we were, like, bumping versions.
We also, I think, Over-corrected and tried to,
Fixed too many things in advance, which then caused more problems.
Like, we tried to upgrade people to new strategies automatically, like, to change config around or whatever, when the collector would push breaking config, and then that would break people more as we tried to fix it for them. Very frustrating stuff. But I think that we've learned our lesson from doing that too many times.
Anyway, all of this is good stuff to, I think, bring up when we meet in, Atlanta. I personally want there to be, like, more communication between us and instrumentation. I think we… I mean, all of… I think we're all in agreement there.
**Antoine Toulme** 28:26 Yes. But…
**jea** 28:28 I think that it's the same with the collector. I tried to explain, I talked… we did a Hotel New York meetup, Lola, earlier this month.
I want to say 2 weeks ago, and one of the big things from that, because there's a lot of, like, banks in New York, there are a lot of people from, like, banking industry who run, like, observability teams.
And a lot of them have a bunch of custom collector components, and they were complaining about how when the collector pushes breaking changes, they then need to, like, update a bunch of interfaces, and their expectation was that these interfaces should be relatively stable, and they weren't.
And so I had to explain to them… they don't really… I guess, all that to say, I don't think users know that there is a stability effort going on, and, like, what…
can be relied upon. I don't think that we're, like, communicating that effectively.
Which is challenging. Like, I tried to explain to this guy that
period, like, we are… the collector group is, like, adding in more stability for, each of the, you know, modules, and once the thing is V1'd, it should be hopefully not going to, like, break your interfaces anymore.
And, you know.
**Antoine Toulme** 29:37 I mean, from the Go, like, code level?
You cared about that?
Yeah, well, yeah, because they built a bunch of, like, custom receivers, for example.
Wow.
**jea** 29:49 And he was like…
**Antoine Toulme** 29:50 He was like, I'm very frustrated when, you know, we upgrade.
**jea** 29:54 their distribu- their internal distribution had, like, 3 versions, and then everything just, like, breaks immediately, and it's like…
Yeah, that sucks.
like, ultimately what they want is a guaranteed, backwards compatibility for the things that they build on top of the collector, which I think is, like, the more important thing for these, like, large enterprises.
**Antoine Toulme** 30:22 Is that so?
**jea** 30:24 I think so. I think that they care less about doing just, like, a config migration, and more it sucks that they have to, like.
go in and make a bunch of code changes every time, someone pushes, like, an interface change.
**Antoine Toulme** 30:38 I don't think these are the people they talk to.
From what I got from the feedback.
**Mikołaj Świątek** 30:42 Yeah. Is this actually such a big problem? Is this so… is there so much churn in those interfaces?
**jea** 30:54 Yes. I think…
**David Ashpole (dashpole)** 30:56 There's also some delay to the feedback, right? So…
**Mikołaj Świątek** 30:59 Like…
**David Ashpole (dashpole)** 31:00 They've been at work stabilizing half a dozen You know, ish?
Of the core ones?
And I know that there's some up next, so, like, this may just be feedback from, like.
the efforts to stabilize that happened 6 months ago that people adopted when the surveys were being done, right?
**Mikołaj Świątek** 31:20 Like, even if there's… Yeah, because, right.
**jea** 31:24 But, like, previously there were…
**Mikołaj Świątek** 31:25 Yes.
**David Ashpole (dashpole)** 31:25 A lot of things that were breaking. There definitely were a lot of…
**jea** 31:29 Yeah, a while ago.
Like, one of the big ones was around the…
health status reporting, component status reporting, right? That was huge. That broke a lot of people. Another one now is, like, the exporter helper changes is, like, also changing stuff, and…
batching is gonna break people. It's, like, all of these things that are important for stabilization that will break people that, again, like, users aren't aware that these efforts are ongoing. I think it's hard to, like.
Keep track of that.
**Mikołaj Świątek** 32:00 I think the exporter helper changes are actually backwards compatible, at least right now.
Aren't they?
**jea** 32:09 Kind of? From the interface design, there's just a new interface, and they're going to deprecate the old one.
But if you're upgrading every 3 versions, right, like, once a quarter, you're… it's gonna be the same, like, thing, functionally, right?
Like, eventually, what…
I mean, I don't know what the collector's gonna do. We're not the collector group. This is for them to decide, but it's like…
Eventually, there will be people that
you know, there'll probably be, like, some branch builds where there's just, like, a full beta candidate, where all of these breaking changes exist, and then you break users, like, once a year on, like, some deprecation schedule. I don't know.
**Mikołaj Świątek** 32:51 I'm like… so…
I would have thought that the bigger problem than this would have been the actual end users, in, like, breaking changes in, like, semantic conventions, or, or, you know, the…
Mmm… the, the actual shape of the metrics emitted by the collector of her…
**jea** 33:16 Yeah. I mean, those are problems, too.
**Mikołaj Świątek** 33:18 geometry, alright?
**jea** 33:19 Those are also problems. I… these are all problems. I guess, like, I'm just synthesizing that
There are a lot of problems in the road to stability that users complain about, which then prevents graduation from happening, which then…
trickles down back to us. And,
Yeah, this is just the path to stability, and I think it's, like.
**Mikołaj Świątek** 33:46 I would…
**jea** 33:47 I don't know.
Go ahead.
**Mikołaj Świątek** 33:50 So, like, one thing that we can take from the general feedback, I think, is something we should do anyway, and I don't recall exactly what we were waiting for. We were waiting for something, and that is go take instrumentation to beta.
the CRD.
**jea** 34:07 Well, the thing that we were waiting for was…
that we don't… I don't think that instrumentation is ready to go to beta.
Because I don't think that the method for it is stable. Like, I think that using annotations for doing it is just wrong. And very inefficient.
**PL Pavol Loffay** 34:26 I think that's… that it would be…
part of refactoring to beta, like, change the instrumentation to label, change the structure to… adopt this SDK config.
Yeah. Schema. There's a bunch of stuff we should improve on that CR.
So it makes sense to move it to beta, do all of these changes, and then…
see, like, let it sit there for some time, and if there's no other changes, then move it to V1. Because it's fairly simple CR, right? It shouldn't be…
issue to kind of make a GA at some point.
**jea** 35:04 Yeah, the harder part is the internals, right? Like, actually doing the injection
Correctly. That's why, like, we've also been waiting for The injector group to,
Finish up or continue, like, to a point of… stability.
**PL Pavol Loffay** 35:21 Is there…
**jea** 35:22 Go ahead. Is there any movement on that?
Oh, yeah, definitely, like, the…
the Dash Zero people and Antoine, again, like, I'm reviewing everything, I'm not writing any of this code, but, they've been making a ton of progress, and they're already using it in their operator, why they have their own operator, and it's not just…
committing back to ours, I've mentioned many times. But they are contributing it back, at least into the injector project, and it'll be up to us to, like.
change to use that, which is better. It is a much better approach than what we have today.
**PL Pavol Loffay** 35:57 Awesome, maybe, shall we maybe start some, like, milestone, like…
Beta milestone, and, like, list all these changes that we… Are thinking about.
**jea** 36:08 I think that'd be great.
**Mikołaj Świątek** 36:09 Actually, is our beta blocked by the injection method?
**jea** 36:15 Doesn't have to be. I think that we should use it, because it's, it would simplify our internal code a lot more.
Because we would use this one injector to do the injection for a bunch of applications, rather than individual
It would be a simpler method, essentially. So…
I also haven't seen… like, I need to look at their code for how they're doing the injection today, in relation to how we would do it, but…
I… from my understanding of it, it looks a lot simpler.
From a user experience. Plus, it doesn't require CP, which, like, it doesn't require GLipC, which is great.
**Mikołaj Świątek** 36:55 Yes, so it sounds like… let's start a milestone for… if we don't have it yet. I kind of vaguely recall that we might have it, for…
**jea** 37:05 Okay.
**Mikołaj Świątek** 37:05 We're moving instrumentation to beta, and let's put everything in there that needs to happen.
I think the main thing that actually needs to happen is the switch from annotation to label, that's probably the most difficult part of it.
**jea** 37:18 Yeah.
Though that also, to me, is the most valuable part of this change. Like, the injector is nice, it's cherry on top, but, like.
I think the operator would run at, like, 1… 100th.
The, like, the current, resource utilization, because we just hammer it so hard right now.
**Mikołaj Świątek** 37:44 Honey.
**jea** 37:56 This is a separate thing, but for anyone interested,
I read through this blog post recently about, like.
Kubernetes efficiencies, and it was a very good post to think about, like, scaling for components like ours, so…
Check it out. It's a very good read. It's really interesting.
**Mikołaj Świątek** 38:16 on that note, while I'm here, because there's a bunch of PRs and a bunch of issues asking for things like.
I would like to set labels on the specific thing that you're making.
I would like to… your annotations to… to, you know, to propagate during… to some specific, to some specific owned objects of your CRD.
Does anyone here have, like, a good, kind of, holistic sense of how this should work? Because I really don't. I really don't.
I'm not sure what should happen, like, if you put an annotation on an OpenTelemetry corrector CRD, what…
should happen with this annotation, exactly. Where should it go? Should it go to every owned object… to every owned resource, or should we expose, like.
pod annotations, deployment annotations, network policy annotations for everything inside the CR. I honestly, I'm not sure.
**jea** 39:15 I think annotations, you usually copy… I believe it's, like, copy from the spec.
So if we have, like, a template… like, the way that other…
The way that at least, like, the prom operator works is they just fully… again, my understanding of it…
they have their, like, common fields, and then they have a thing in there for pod metadata, and then they just copy that over directly. So it's like…
Let me find it.
And we could probably do a similar approach now that we have the common fields, but,
Nice. Okay, let me copy this for ya.
Copper.
Okay, check that out.
Just sent it in the chat.
I mean, that seems like a reasonable approach, though I guess we're kind of a little different than that, but I think that that also… like, I think that this makes sense.
**Mikołaj Świątek** 40:31 Okay, but what if someone wants to have
Annotations on a deployment we create.
**jea** 40:39 I think that that's what this is for, no? Oh, annotations on Oh…
**Mikołaj Świątek** 40:44 or a service, or any other of the, like, 8 or 9 or 10 resources that an OpenTeometry collector CR.
**jea** 40:54 Yeah.
Let me look at what Prometheus does, and I will tell you a better answer.
**Mikołaj Świątek** 41:02 Is this… is this what we're gonna default for? Is this the decision-making process? I don't mind, I was, earlier, there was an ask for someone who was saying, I would like you to put a label on every… on each pod that you instrument, so I can easy… find them easier.
And that's not invalid, and I went and checked what Istio does.
The answer is that Istio doesn't do this.
And I don't think this is…
**jea** 41:28 It also doesn't do this.
**Mikołaj Świątek** 41:30 Yes. So, I mean, Prometheus doesn't… it doesn't instrument… doesn't have a mutating pod webhook, so… so… so you know.
They don't have that problem.
Specific.
**PL Pavol Loffay** 41:40 But the…
**Mikołaj Świątek** 41:41 We have this problem where we inject fines into pods.
**PL Pavol Loffay** 41:47 Yeah, I would close that issue, saying that we're gonna implement it once we migrate to the label.
From annotation.
**Mikołaj Świątek** 41:55 But that label doesn't actually do what they're asking for, exactly. Like, that label is a way to tell the operator, instrument this, but the fact that you have that label doesn't mean that you're instrumented.
**Benedikt Bongartz** 42:06 The question is, if we do this, if we run into some reconcile infinity loop at some point, where you change your label somewhere, and then the other operator sees a change, and then reverts it.
Something like this, so when we.
**Mikołaj Świątek** 42:21 Yeah, I'm also, like…
I'm a little bit reluctant to add labels or annotations to resources that we don't own.
**jea** 42:31 Meanwhile…
**Mikołaj Świątek** 42:35 Can you add completely custom stuff to a pod status? I think no, but that would be, like, a good place for it.
**Benedikt Bongartz** 42:42 What I'm with anyone.
**jea** 42:43 No. That… that's…
**David Ashpole (dashpole)** 42:45 You can report your own conditions, is the way that… like, condition is just a generic thing, so you can always report, like.
This pod is, you know, launched into outer space, true, false, unknown, like…
You know, and throw it on it, and whoever cares about it can go find it.
**Mikołaj Świątek** 43:01 That's, like, that's a pretty, pretty reasonable thing. If you can have a completely custom condition, then we can have a condition which is, like, you know, open telemetry, something, something, something instrumented.
**PL Pavol Loffay** 43:12 But does it solve their issue? So they want to, like, see all the instrumented bots? Is there a way to, like, query or, like, list by condition?
**Mikołaj Świątek** 43:23 Using JSON path, yes, I'm pretty sure. You could also query… they could… their problem could also be solved by querying… look… if we have, like, a…
Consistent naming for the instrumentation container.
then they could also use that. Like, it is possible to do, like, a JSON filter using JSON path.
to say, you know, to say something like, this… this pod has a container named X.
**David Ashpole (dashpole)** 43:56 It, like, it's meant for something that is…
observing the current, like, state of a pod periodically, and making updates. Like, that's how conditions are meant to be updated. For example, you can't…
update the condition in the same request where you update spec, and I'm not sure about mutating admission controllers, but it's used by, like.
cube proxy if it wants to let something know that the network has been configured for a pod, and something else wanted to block on that. Or, I think there's some finalizer-related stuff where you don't want to tear down a pod until
No, no, I'm misremembering. But it's, like, meant for that sort of thing, not like…
Yes, no, has the mutating admission controller done its job?
**Benedikt Bongartz** 44:45 Wouldn't it be something where you can just create… An event, or even…
Yeah, just write a lock line, and send it somewhere, so that we have some telemetry that goes out, and then just tell… there is a new pod which was instrumented.
So that we… Just get rid of this telemetry data, and…
You can do whatever you want.
**Mikołaj Świątek** 45:12 In general, I think it's a very valid ask to be able to, like.
how do I easily tell that the pod was instrumented?
by the operator. Slash, you know, how do I tell that my pod, easily tell that my pod had an Istio sidecar?
Injected to it.
Right?
What is the… What is the…
**PL Pavol Loffay** 45:39 By checking the init container at the moment.
**Benedikt Bongartz** 45:42 appropriate.
**PL Pavol Loffay** 45:42 most reliable.
**David Ashpole (dashpole)** 45:46 The other thing you could consider is not putting this type of thing on the pod itself.
putting that type of information on the instrumentation resource in status, because if it's something where you could periodically say.
like, list all the things that I'm instrumenting.
And…
you know, update this count here in the status of my instrumentation CR, so that if someone wanted to know, like, if they messed up their label selectors.
**Benedikt Bongartz** 46:14 That they could tell.
**David Ashpole (dashpole)** 46:15 I don't know how much detail you really want to include, but… I think that's the other…
The way you could do it, if someone wants a central view of, like, What is this instrumentation reason?
**Mikołaj Świątek** 46:27 I'm not sure how practical that is, though, if you have a lot of pots.
And also, you have this problem, potentially, where you can have the same instrumentation Or…
Do we… do we allow multiple instrument versions to rest, act on a single pod? We don't.
But we could.
**David Ashpole (dashpole)** 46:57 You could do something like the account of pods, or something like that, maybe.
**Mikołaj Świątek** 47:09 Yeah, we could definitely attach, like, a list of pods, instrumented pods, to an instrumentation…
But it is also, like, the reason people are asking for this, to not kind of lose sight of the actual user need here.
The reason people want to do this is because they kind of want to have a certain level of observability as to how their… what their instrumentation, how the pods are being instrumented, right? They want to have, like… for example, they want to have a dashboard which tells them.
**Benedikt Bongartz** 47:39 Not.
**Mikołaj Świątek** 47:41 how, you know, you have 100 pods, which are… should be instrumented, but all of these 70 are actually instrumented, right? This is, I think, a very, very valid thing to want to know.
About your, about your cluster.
And how do you… what is the… right, we could emit a metric like this, no problem. We have an issue that nobody has actually acted on it. We have… we have an issue to emit some metrics which track… which track us, because it's pretty easy for us to calculate that internally. It's just that the question of how to
expose it externally, let's call it. As it turns out, this is not very obvious.
I actually think the kind of blessed way of doing it is really to just add an annotation, not a label, but an annotation.
**Benedikt Bongartz** 48:39 But…
**Mikołaj Świątek** 48:41 That's also not that nice.
**jea** 49:12 Well, it sounds like we're all thinking about it, but not… I don't know what is next for that.
I think that the good… a good first step for us is going to be at least, going towards instrumentation beta and moving to labels. I think that that's… that's, like, the first step to me, because I think the way that we do it now is silly.
But… I don't know. Other… do we have anything else? I mean, we… I think this is a good topic, but…
**Benedikt Bongartz** 49:43 I added some issues in the pull request, which tried all different approaches, adding it to the status field.
Editing, added to the condition.
And also, adding it as a label.
Let's follow which workload is instrumented.
**Mikołaj Świątek** 50:08 I don't know, I'd like to go and do a review. Like, there's a bunch of more mature
Operators, which do this kind of thing.
**jea** 50:18 I think the tough thing is that, like, Kubernetes doesn't release a lot of guidance on how these things should work, and I would love for them to do more of that.
**Mikołaj Świątek** 50:27 Yeah, like, like, when we…
**jea** 50:28 David, that was…
**Mikołaj Świątek** 50:29 Are we using conversion records correctly, right?
When we asked about that.
**jea** 50:36 Well, it just feels like, I remember John Howard gave a good talk about, like, their Istio patterns, and he was like, this is what we're doing, and I think that this is right, but who knows?
And I was like, that's useful, but…
It also feels like someone knows more… it feels like we should be at a place with a Kubernetes project at this point that they have a better
pattern for doing reconciliation, but it seems like everything
for reconciliation in CRDs is the Wild West.
Unfortunately.
For better or for worse. It's just kind of weird to me that, like, I don't know.
**David Ashpole (dashpole)** 51:21 Yeah, I agree. It…
I think there was an effort to do this with, like, all the controller runtime and KubeBuilder-related stuff to try and just codify it, rather than explain it.
It… sort of worked.
Like, people use it, but it's clearly not enough. And it does always feel like there's…
a dozen people in the Kubernetes API reviewers that actually know All of this, and
I don't know, just… Yeah.
**Mikołaj Świątek** 51:56 Alright, anyway, I'll try to… I'll try to do some research. I want to at least know what other projects have done.
I don't know, like, whether that… whether that will mean that we wouldn't do the same thing, but…
It would be good to know at least what works in the wild, and how well it works.
In a practical sense.
But other than that, I think we're… I think we're done.
And I missed those anything else?
Any of you would like to talk about?
Alright then, thanks for coming.
Had some… had some really nice chats.
See you soon, Nick Club.
**jea** 52:49 Yeah, too.
