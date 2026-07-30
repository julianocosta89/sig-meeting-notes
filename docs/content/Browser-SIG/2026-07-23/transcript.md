SIG: Browser SIG
Date: 2026-07-23
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Jared Freeze** 02:11 What is up, everybody?
**Martin Kuba** 02:13 Okay.
**Jared Freeze** 02:22 Let me pull up the doc real quick.
**Martin Kuba** 02:41 Do you want to drive today, Jared?
**Jared Freeze** 02:43 I'm sure.
**Martin Kuba** 02:44 Thank you.
**Jared Freeze** 02:45 Yeah, yeah, yeah.
Cool. Let's see… What do we have?
Roadmap. Does anybody else have anything they want to add?
Alright, cool. We can get started then.
**Martin Kuba** 03:26 Yeah, so I just wanted to bring this up, for a number of… for a few reasons.
I think we're… we've done a lot of work over the last year, that was part of the Phase 1.
There's a link… project, auto project, so there's a link, also in the notes for the Phase 1. Our goal is, essentially, were to kind of bootstrap this SIG, work on some Basic instrumentations, And, gonna review, review where we are as far as, our dependency on the JS, packages… our APIs, and so I think, for the most part, like, we've made a lot of progress. For the most part, we have achieved our goals for Phase 1. I'm curious, like, if anyone feels otherwise, but, they're at a place now.
And we have, we have two packages published, we have instrumentations, pretty much all the instrumentations that we wanted to do, or we felt like were important to start with.
You know, I also have the SDK, And the question, is, I think, would be… I think my question is, it would be helpful for this group to have kind of consensus, especially among the maintainers and active contributors. What are the, like, our next priorities?
I have linked this, so the Android SIG has done something similar. They have, documented their high-level roadmap, in their repo. I think it might be useful for us to do the same.
We have also been asked That has been asking for us to present the status of this SIG, in the… to the wider hotel community in the specification SIG, probably.
And I think when we do that, I think it would be helpful to kind of have alignment among us.
And to, like, to be able to describe what are our next steps and priorities.
So yeah, that's… that's where I would like to start. I think… I think, I have some ideas, but I want to collaborate on this.
So I'm proposing that we open an issue or a PR, where we can collaborate on this, and, You know, and make it part of our documentation, as a living document.
But I wanted to kind of kick off that conversation here.
kind of the themes that I'm… that I… that are kind of top of my mind is, probably the most important for me is semantic conventions.
As kind of the foundation of, what data we're actually producing. So we have… a lot of new, a lot of new instrumentations, but only one of them is… has semantical mentions that are documented in the SEMCON repo.
Yeah, and there is… there is… First of all, before I go into the themes, like, does anyone have any comments or… Questions?
**Jared Freeze** 07:04 I think it's a great idea to… to get everything down and to present, we can find a time to do that.
What do you think the audience for that would be?
Like, is there a main meeting, like a maintainer's meeting or something?
**Martin Kuba** 07:19 Yeah, I mean, so I think… the… like, the specifications in the spec SIG, that's what Ted asked us to do.
**Jared Freeze** 07:27 Okay.
**Martin Kuba** 07:28 But I think for, like, any… even, like, for any new contributors, you know, like, this… and… or use… even the users of… of the… of the… of this SDK, to be able to, like.
Understand where we're going.
**Joaquín Díaz** 07:46 I think it would be nice to have, like, leave document on the repo with all the things that we think we're missing from Phase 1, and the things that we think are next.
Maybe it's a good idea to wrap up what we call Phase 1 before starting with new stuff.
Mainly around some of the stuff that is still on the JS repo.
I think… the video once the patch and XHR implementations are still there.
And, I don't know what else, so yeah, I think it would be better for us to have I know we have lists somewhere.
Over the… like, even around issues or any other documents, maybe the best way to have it is just have it on the repo, copy it.
We can look at that.
See what's next.
Yeah, here, so… okay.
Is it… is this up-to-date?
**Jared Freeze** 09:06 We may have to review this.
Like, this one… This one's almost certainly deprecated, so, like, that definitely needs to get updated.
These are already in flight.
So… you know, yeah, this needs review. I can go over this, or we can link it out together, Martin.
Also, this is disappearing soon, so we gotta deal with that pretty quick.
**Joaquín Díaz** 09:36 Yeah, I think it's fine if it's an issue, or… I personally, I prefer it to be on the Red Bull itself. It's… to me, it's easier to find. But if we have it here.
maybe we can pin it, I don't know if we can pin issues, but yeah. I think you… we can have a really good understanding of what's… Remaining, before starting with new stuff.
**Jared Freeze** 10:06 Oh, you're muted, Martin.
**Martin Kuba** 10:09 Oops, sorry. Yeah, yeah, I agree, I think it's, You know, it does help, you know, with, like, what I… even, like, aside from the roadmap, like, what our priority is right now.
So I think finishing or moving all the packages and the consolidation is… I agree that it needs to be finished.
**Joaquín Díaz** 10:32 Yeah, I don't know if David is here, I don't see him. I think his PR for Fetch is… it was really good progress, and…
**Trent Mick** 10:41 He's on vacation for 2 weeks, he's back next week.
**Joaquín Díaz** 10:44 Oh, okay.
**Trent Mick** 10:45 Last I remember him saying is that it was… it was almost there. He was happy for… while he was away for someone to take it over and finish it, or he'll get back to it next week.
**Joaquín Díaz** 10:57 Okay.
**Jared Freeze** 11:01 Cool, okay, we can look at that, too.
Make sure that's on the list.
Bo, anything else, Martin?
**Martin Kuba** 11:17 Yeah, I mean, is there… aside from this, I mean, is there anything else that people feel, like, was unfinished in Phase 1, before we start, kind of, thinking…
**Joaquín Díaz** 11:29 I think… session management is something that we always like to have, and I don't think we… we have ideas, but I don't think we settle on anything?
Or… or do you think that's part of the roadmap itself?
**Martin Kuba** 11:51 Yeah, so I think the sessions is a bigger topic to talk… to discuss. We actually talked about this in the client instrumentation SIG on Tuesday with the Android folks.
They're, you know, they have their own implementation, we have our own implementation, and it's not, you know, it's not, I think we need to come up with a unified API, unified data model for that, so the current idea that was proposed is that maybe it might be worthwhile to spin up a temporary working group, access sessions working group, as a project, to work on you know, to finish to some other dimensions, an API, the spec around this, and… Yeah.
**Ted Young (Raintank, Inc. – Grafana Labs)** 12:39 Yeah.
One thing I'll note is, like, Entities is actually trucking along. Josh Surith has, like, got his legs back under him, and he's making a, like, a Java… java implementation of it, right, that I'm sure the Android people will be able to get their hands on.
So, I think it's actually good timing.
**Jared Freeze** 13:12 Cool.
Does anybody have anything else?
Any questions? Anything general?
**Joaquín Díaz** 13:24 Sorry, so for the roadmap, are you going to create a separate issue, just to talk about that?
**Martin Kuba** 13:30 Yeah, yeah, I will, I will.
**maxime quentin** 13:33 On the duplication, like, issue.
Like, if, I don't know if you can be reviewed, so, some people, can pick some remaining tasks, I would… I would happily help if, there is one in… you have in mind.
But, yeah, having this kind of structured, Roadmap, where we can, kind of, Like, walk on something and communicate about it.
And, A bit like OKRs or stuff like that, I don't know.
What framework we want to use, but, being able to, to attach ourselves to an initiative, and then work on it.
I think it's… I would vent.
**Martin Kuba** 14:20 Yeah, I think it'd be… Useful to, label the issues, which ones are… Up for grabs, and… No.
**Jared Freeze** 14:34 Yeah, I can go back and I'll review, I'll review all the issues today and mark, like, good first issues and all that stuff, because I think it has been a little bit since we did, like, a top-to-bottom review.
**maxime quentin** 14:48 Thanks.
**Ted Young (Raintank, Inc. – Grafana Labs)** 14:52 Just another high-level note, we've been discussing there is, like, a client SIG that meets every other week on Tuesdays, and we've been… discussing what… what level of, like, cross-IG organizing that we want to do. We know that, you know, we'd like to get more people with client expertise onto the TC, but do we need, like, some other amount of structure other than, you know, Maybe spinning off the occasional, you know, working group, like, for sessions, but is there anything more that we want to do? Especially with Flutter, I, probably getting its approval this week to get started. I think they've got Carlos now, to be their TC sponsor, and that was, like, the last piece. But because Flutter is cross-platform.
That also brings up questions, and I think what we decided in that client group is, like, probably the best next step there is around semantic conventions and federated semantic conventions, creating a repo for a client.
semantic conventions.
And also having all of, like, the different platforms move their platform-specific semantic conventions there as well. So there's sort of one place where you can see everything, like, that's basically our mental model for how clients work, right, is our semantic conventions. And if we can make that repo really clear and comprehensive to people. Maybe that's, like, the place we can all work out of, to coordinate across different clients, because we don't really need to coordinate so much on our implementations, right? The place we need to coordinate is on the data model that we're providing.
so, that's in the work, Hansen Hoes, holding that down.
But that seemed like, like, a reasonable next step, and we kind of felt like, beyond that, maybe we don't really need any additional structure right now, but if we can get that thing kicked off, that would be the place to coordinate everything out of.
**Jared Freeze** 17:11 Yeah, I was trying to find a ticket, just so I could open it for people.
Hanson asked for a new repo.
I'll… I'll add it to this docket after. I don't have it handy, so… Okay, anybody else?
The only other thing I was gonna mention, I guess, was, the… actually, Trent's here, you can probably do it, but there's a schedule for the SDK the JS SDK 3.0 release.
which is Code Freeze on September 1st, release on September 30.
our contribution from this group is that I am redoing… I'm taking the build system from OTEL Browser and sort of porting it into JS Core. So they'll get files with extension names, that's probably the biggest change, and move from, like, build to dist.
As the output folders, and there will be export keys. So, no deep linking any longer to… to files in the node modules. You won't be able to just pull stuff out willy-nilly. So, anything else to add?
**Trent Mick** 18:28 Not really. I guess the thing that had been brought up earlier on… the one issue about moving things from the core and contribute over to web was the SDK trace web goes away, but you… You mentioned that already. There's still a little bit of work left on that. I guess I'm a little bit behind on which of the… Sorry, there were two things in SDK Choice Web to finish up.
I know I'm distracting a little bit from… from the release thing here, but I think the recently published Browser SDK… Provides an alternative to the stack.
context manager that can be pointed to as a fallback, and then the other one was, SDK TraceFib, but a bunch of utilities that are used by instrumentations. I don't know if those are all covered now by the instrumentations moved over, or maybe that gets finished when the fetch instrumentation moves over, something like that. Anyway, I have to go through and do those.
Yeah, I don't know, other than that, there is a… In the core repo, there's a milestone for SDK 3.0 that, if people are curious, they can browse through the list there, that's… A pretty complete set of what we expect to do.
Leading up to September, and then… start merging everything September 1st.
**Jared Freeze** 19:49 Yeah, I'll link this one as well.
**Trent Mick** 19:52 Okay.
**Jared Freeze** 19:59 Alright.
I guess we're done early. That's probably it for today, unless anybody has anything. Ted, anything good? Nope. All good? Nope.
**Ted Young (Raintank, Inc. – Grafana Labs)** 20:08 Excited.
**Jared Freeze** 20:10 Okay, see you guys on Slack.
