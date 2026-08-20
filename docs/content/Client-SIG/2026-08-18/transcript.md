SIG: Client SIG
Date: 2026-08-18
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Martin Kuba (Raintank, Inc. – Grafana Labs)** 00:59 Hi, everyone.
**Cleo Schneider** 01:01 Hey, Martin.
Hey, Jason.
**Jason Plumb** 01:04 Hey, good morning!
We need Hansen.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 01:57 They do.
**Jason Plumb** 01:59 Has that issue gone dark?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 02:03 No, so I can… I can start with that, I went to the SEMCON SIG yesterday.
to see, like, what the status is, what, they need from us. Trask said that he's not opposed to creating the repo.
He just wanted to have a conversation with us to make sure that there is an ongoing com… Communication between the new client-side group.
And the chorus and the conventions group, he doesn't want to just, like, us go into our own direction without NA.
communication happening there, so…
**Jason Plumb** 02:42 Yeah.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 02:44 But he said that if we… If we feel like we're blocked, he's… he's fine creating the repo now.
**Jason Plumb** 02:53 Okay, cool.
I want to acknowledge that Michael's here. Hey, I don't know that I've seen you on this call before, but I acknowledge what you're doing over there with Swift and stuff, so welcome!
**Michael Bushe (Mindful Software, LLC)** 03:10 It's, Dart and Flutter, yes.
**Jason Plumb** 03:13 Flutter, sorry, yeah, early morning.
**Michael Bushe (Mindful Software, LLC)** 03:14 So, probably about a year ago, I was, I was, I was on maybe one or two calls, and then, decided I had to put my attention elsewhere, but now that our Dart and Flutter SIG is formed, and it's Dart, so it's server-side too, but most of Dart is Flutter, so I've got to get more involved in the client side. I've been meaning to, but haven't had the bandwidth until now.
**Jason Plumb** 03:40 Cool. Yeah, well, welcome back.
**Michael Bushe (Mindful Software, LLC)** 03:42 Thank you.
So, can you… if I can take a sec, could you guys catch me up? What… one part of my confusion over the past year was how the groups have kind of shifted around. When I was, I think the last, last thing I joined, there was a browser group, maybe not even a client group at the time, and now we're… did I just hear that the groups are shifting again?
**Jason Plumb** 04:12 Do you want to take a stab at that, Martin, or do you want me.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 04:13 Yeah, no, I can… I can start. So the browser… it used to be… this meeting used to be very browser-heavy.
And we actually split off into a separate SIG… SIG now that's just browser-focused, and this one stayed in place, for anything cross-cutting, you know, for anything that's shared.
With, between mobile and browser, and… And it's only every other week, so…
**Michael Bushe (Mindful Software, LLC)** 04:45 Good, I'm in the right place, then.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 04:47 Yeah.
**Jason Plumb** 04:49 And then in addition to that, of course, we have the Android SIG that's doing Android stuff.
That's what I'm here representing, and then also we have a newly formed Kotlin SIG, targeting Kotlin multiplatform.
And, so I'm representing that as well. And that's probably a similar boat to, like, the Dart Flutter story, where, like.
most of the Kotlin KMP multiplatform targets are going to target Android, but certainly you can target tvOS and a bunch of other, you know, hardware stuff, so… Server side, native, whatever.
So, what we were just talking about is this desire to, so, in the semantic conventions, there has been… I mean, semantic conventions has been just… a torrent of activity over the last two years, and it's so much so that it's really hard sometimes to get attention and approval, because stuff feels like it has a little bit of permanence, and so this idea of A federated semantic convention was born. We've adopted that in Android. I think other groups might be adopting that as well. But that runs the risk of having completely fractured, maybe segmented and or conflicting semantic conventions.
So, the idea of having a common one for stuff that is common to client-side targets.
Where we can agree, or at least bike show and stuff there for a while, and the stuff that is truly platform-specific can fall out to the federation. So, you know, that's what's cool about the federated stuff, too, is it allows for this tiering structure to exist.
**Michael Bushe (Mindful Software, LLC)** 06:28 Cool, sounds, sounds smart.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 06:32 And we're kind of talking, like, 3 tiers here, because we have, like, Android already has their own federated, semantic conventions in their repo.
Like, when I were thinking about having a client-side Group, some of the conventions group, that would be, like, anything that's shared across the different client.
Platforms, and then there's the course and then the conventions as well, so…
**Michael Bushe (Mindful Software, LLC)** 06:59 Great, I did see some of that work, and that makes sense.
I'll look into adding a flutter as a child of that tree.
**Jason Plumb** 07:12 I think that makes a lot of sense, yeah.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 07:16 Yeah, I'm kind of expecting this client-side semantic conventions Repo would be most helpful to mobile.
SDKs, but they have probably more overlap than anything with browser.
I'm guessing, aside from, like, sessions or… yeah.
**Michael Bushe (Mindful Software, LLC)** 07:35 And Flutter is more broad. It spans mobile desktop and the web, so I'm gonna have my, Fingers in a lot of pies.
**Jason Plumb** 07:58 Well, so do we have a timeline on that, Martin, for creating that repo?
Do you know who the maintainers are gonna be? Is it gonna be you and Hansen?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 08:07 Yeah.
So I think I do need to talk to Hanson, to see if he's ready to work on this.
**Jason Plumb** 08:19 Cool. I offered to be an improver.
I don't want to be another maintainer.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 08:27 Yeah, and like, speaking about this, Michael, I actually… I think I was listed as a maintainer on the… on the new Flutter, and I don't think I should be, I think I just… Was asked to help out bootstrapping it, but… So I need to follow up on that.
**Michael Bushe (Mindful Software, LLC)** 08:45 Sure, sure, and that's the intent. Both, you and Cesar, Caesar, are there just because you have the experience in the group, and it's intended to be temporary. We have a brand new group.
I'm trying to grow… I'm trying to grow myself, I'm already maintaining it, but still, and I'm trying to grow the rest of the group, and we expect other people to be able to take on those roles, and, and, take the, and eventually you guys would… would stop being maintainers. You can go back to what you're doing and take that off your plate. Meanwhile, I could probably take up, semantic conventions, I could probably help out Hansen.
Or be a maintainer in that if, if you guys are alright with that.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 09:33 Sounds good.
So I think I'm… I think I'm gonna, reach out to Hanson, since he hasn't joined today, and… Then I can ask Trust to create the repo. I don't think there's anything… That we need to resolve before, so… And the other thing that I wanted to, just bring up, we've talked about this before, is, having… Working on… Sessions?
Specifically, you know, data model, semantic conventions, API… There is, that is also… we also… Talked about having, sessions represented as entities, and, I think we need to work on an OTEP for this.
So, do we… I guess my question is, do we need a separate working group for this, or, like, can we do this here?
And, like, do people have capacity to work on this?
**Jason Plumb** 10:50 Those are good questions. I'm giving space for other people to chime in.
**Michael Bushe (Mindful Software, LLC)** 11:02 I didn't want to chime in because I've been the only one chiming in, but I also have Dartastic.io, my commercial thing that I'm launching, and I'm working on sessions there as well. So I do have the interest and have looked at it, so I would love to help out in that space.
**João Oliveira** 11:24 Yeah, I'm not sure, not sure about separate working group, or keeping this one, but… They thought we're also very interested in sessions, so… Where we can, allocate some time to… And hence… For that topic.
**Cleo Schneider** 11:44 And I think… I think over on here… here on Firebase, we're in a similar boat. Also don't care if it's a separate working group or in this space, but… Would love, love to be involved there.
**Jason Plumb** 11:58 I feel like we've been talking about sessions for many years, and if we don't do a working group, we won't put it to bed, and we're just gonna keep kicking that can around.
I think a targeted team that has a charter of, like, defining what sessions are, what the semantic conventions look like, if they're entities, how they're entities, how those are represented, the behavioral definitions, I think without a working group, I think that won't happen. I think we've kind of demonstrated that, and I think, I would like to help out. Do it… do we have cycles? No, but… It's important, like all of the other important things? I don't know.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 12:39 Yeah, I wonder how much time we would need for this, like, do we have, like, a good, I feel like I have a decent, kind of.
picture, like, what that would, look like, maybe just, like, need to work on the OTAB together. So I kind of imagine maybe this taking, you know, a few months, maybe?
And then, then we could, like, dissolve, dissolve the working group.
**Jason Plumb** 13:04 That sounds reasonable to me, kind of in the 3 to maybe even 6-month timeline.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 13:12 Yeah.
**Jason Plumb** 13:12 Including the OTEP, but including… a lot of… probably pro… I mean, continue on the prototype thing that you've already done, Martin, with entities.
you know, I think it could stretch out a little bit, but… Yeah, the OTEP and the working group proposal would be kind of the next… Thing.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 13:35 Okay, so I can take the lead on that, I can… At least, Open an issue for… for us, for, like, proposing a new working group.
And I can… I can share it with this group.
**Jason Plumb** 13:50 Cool.
Thanks for taking that on, Martin. Let me know if you run into specifics where I can help, let me know.
**João Oliveira** 14:03 When we talk about, working group, is it, like, is it, is it called a SIG like this one, or is it, is there a specific thing called, like, working group for more, ephemeral issues like this one?
Like, what are we talking here?
**Jason Plumb** 14:21 I forget the vernacular, how that fell out. I think both have been used historically, so I don't want to give the wrong information. Let me see…
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 14:34 I think, historically, there was a distinction between working group and SIG, but then it got collapsed into just SIG.
But… But there's also a concept of projects now, so maybe it's more like a project proposal.
I'll have to, have to look into that, yeah.
**Jason Plumb** 14:55 Yeah, I think I don't know the answer anymore.
It used to be… Last… last I knew, and I'm… I'm… probably wrong, but the last I knew is that they wanted special interest groups to be short-lived and have Especially project-centric, special interest groups to have a timeline, like a specific charter, and a timeline, and an end of life. Like, so we should be done with this by, boom, like, whatever. So it's not kind of doing what the Client SIG has been doing, and just sort of… kind of kicking around client-side ideas for a long time, like, it'll have it be focused and specific to an area, tag-team it.
And focus only on that, and then once that is done, move on to the next thing. So there was one around… there was definitely one around logging.
And events, like the events that exist in logging came out of a working group.
Again, the name might have been Special Interest Group, I'm not sure. And then, database semantic dimensions also had one. There's also one… I think there's several others in flight right now, I don't know where to find that list, but… Yeah, Martin, you and I… you or I could ask next week, I guess, in the maintainer's meeting.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 16:17 Yeah.
And also, if, I can also ask, ask Ted for help, if he… I need to, so…
**Jason Plumb** 16:29 Oh yeah, your coworker.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 16:41 Alright, well… So, that's… that's what I had. Does… is there anything else that, It's on other people's minds.
**Jason Plumb** 16:58 I don't have anything from the Android side, really, right now.
Other than we have a lot of bad bespoke semantic inventions that need cleaning up.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 17:17 Jason, I've been looking at your implementation of the Federates of semantic conventions.
**Jason Plumb** 17:22 Yeah.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 17:23 And, I like how you've done the phased approach.
to introducing it, so I might mirror that for browser.
**Jason Plumb** 17:31 Cool. Yeah, it worked out pretty well. I think I closed that… If I didn't close that issue, I intend to. I don't… I don't have a good way… Let me just share, since we have a little more time, if you want to talk about this, if that's of interest.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 17:47 Yeah.
**Jason Plumb** 17:48 Alright, I'll just, in case people haven't seen this, maybe, maybe people have, but… there was an issue that I opened, which was, like, this phased approach.
It's the thing that Martin's talking about. So it's still open, but it was, like, the background about why this is a problem, what we can do about it, and then kind of the phases were, like.
like, here's how we can go about this. Instead of dropping one PR that touches nearly every file in the repo, you know, do it kind of strategically to make PRs easier to digest.
And do this, and then unfortunately, this is what I'm hung up on right now.
And I don't think we have a good way of doing this yet. We talked about this last week in the Android SIG.
But… I think these, if you read through these, these are pretty straightforward, right? We have… YAML definitions of semantic conventions, from those we generate Kotlin class files that represent the semantic attribute constants, so that we don't have literals in the code, we can just reference those defined constants, and we also have event classes, those event classes have constructors that require certain arguments, and then have other methods that allow you to set optional attributes, and then they can be omitted, so it's like a code… very fluent code-based approach to generating events. The other thing, though, is the documentation that goes along with those, and that's the thing that I'm… getting a little bit hung up on, so I'll show you what that looks like today.
We have these READMEs for each instrumentation module.
Right? And for each one, we kind of have a section that says what is being emitted. So in the event of a crash, we throw out an event called app.crash, and here's the attributes, and then we can… we link to the semantic conventions.
And I was thinking, like, well, we have the semantic conventions now, that's cool. We should just be able to template this, right? Like, fill this in from Weaver, right? We have… We know all this stuff, like, but those two things right now are not synchronized in any way. The README text and the Markdown Is not generated from a template.
But… We have the registry over here, but the registry doesn't tell you what instrumentation modules are using or emitting a given piece of… Semantic content, right?
So there's nothing that ties this. So then I'm like, well, the way that Java does it upstream is they have these little metadata YAML files, and that's what, for each instrumentation module, they declare, like, what they use or what they emit. And that's pretty cool, too.
But there's nothing keeping that in sync, and that could be wrong. Like, if the instrumentation changes, then the metadata could fall out of sync.
And… It seems like a step in the right direction, but it doesn't solve the problem, so I don't know. Something I need to think more about.
If people have ideas, I'm open to it, yeah, please.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 20:46 Was this just because you already had that in your READMEs, and you wanted to make it automated, or was it some kind of requirement, or something?
**Jason Plumb** 20:55 It was purely… it was purely, like, a nice-to-have. Like, I'll probably close… I'll probably close that issue, not having solved Phase 6 or whatever.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 21:01 Yeah.
**Jason Plumb** 21:03 But yeah, I think it would be nice to have the code be in sync with the documentation, and if the… if the registry was a way to get there, I would love that. It seems like it doesn't quite get us there, but it's a step.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 21:20 Okay, yeah, thanks for sharing.
**Jason Plumb** 21:22 Yeah.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 21:23 I might, I might basically just copy what you've done, I guess.
**Jason Plumb** 21:26 Yeah, please, no, yeah, do. Yeah.
I don't know how to make much of that really reusable.
But I think it's not that much code, I think copying it's probably fine.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 21:46 Cool.
Yeah, sounds good, like, if there's no other topics, then, we can… we can stop here.
Okay, thanks everyone.
**Cleo Schneider** 22:05 Thanks, Martin. Thanks, y'all.
**Michael Bushe (Mindful Software, LLC)** 22:07 Ready?
**Jason Plumb** 22:07 Thanks.
**Michael Bushe (Mindful Software, LLC)** 22:08 Meet?
