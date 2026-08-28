SIG: Swift SIG
Date: 2026-08-27
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Nacho Bonafonte** 01:07 Good morning, Baptek.
**Vishwan aranha** 01:10 Morning.
**Nacho Bonafonte** 02:38 Okay, I think you kind of started.
No, I don't see anything?
Tomorrow.
At least I don't escape from more people.
Okay, so I will start saying the document.
Yeah, please, here.
Nang there.
Thanks. Okay, as always… Yeah, if you have any topic that you want to… To talk about, apart from what?
Tisna?
From last week, or next things?
You can add it, if not, we will continue also later, if we have time, as we had last week.
Any issues on me, PR.
That we've reviewed, or that we've been… San decision or comments.
Okay, so first of all… There… there was a topic last week that came from People from Apple that… said they work on this work also to talk about this, but they shared a document with some ideas they had for the APIM.
SDK?
Yeah, I think the document is public.
It was shared.
I think, in the channel last week, if anyone is interested.
Yeah, I think it was made public.
So, yeah, basically, Apple was… Pushing, for, integrating their own… observability libraries onto OpenTermetry Suite.
And yeah, we had a long talk about that, and the limitations that there were.
Anyone has any Comment about it?
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 04:55 I think we had discussed adding it as an issue and attaching the document on the repo for the wider community, right? Like, can we do that, or, like, are we waiting for them?
**Nacho Bonafonte** 05:06 Yeah, I mean, they thought they were coming this week, right?
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 05:11 Yeah.
**Nacho Bonafonte** 05:12 What was the… what was, what was the opinion from the maintainers?
Yeah, we have talked a bit.
Under the, yeah, internally.
Yeah, bud. Cheers.
I was expecting them to come here and talk about it, but yeah, let's… I don't know.
I don't know why… why they didn't come. They also didn't see anything. But, I mean… If you see the history of this SIG meeting, that's something that happens from time to time. Poor people come to the meeting once, and they just are out for a… long period. Yeah, I don't know.
The what?
Yeah, I mean, I think they had some ideas, I think they… there were some ideas from them that were not… What we want as a project?
or as OpenTelemetry, we… I mean, as I said, we cannot replace all of our… things with Apple stuff, because basically it's not the same API, right? That they… So, yeah, I don't know. But that has been the public… Point from over, always.
Let's see… Yeah, maybe they will appear next week, and we can talk about it.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 06:34 Yeah, also, I remember you raised some points about, like, not being able to bump up the minimum supported version, owing to contractual obligations, like, do we have any current, like, have we heard from any of the, you know.
Like, companies, like, what, what their plan is, like, moving forward.
How long… like, I…
**Nacho Bonafonte** 07:00 Typically.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 07:00 minus 3, right? Yeah.
**Nacho Bonafonte** 07:02 Yeah, the last time it was because Embrace.
The company had problems with that. They had a very low minimum version.
So we kept that somehow locked.
Yeah, but the idea is once… I mean, we, I think that's a topic we have been saying lately, is that we still have to release a version for Cocoa Pods, that will be the last one. After that, we will merge both.
But the, the, the core… Source code into the main one.
And then we will evaluate. Apple will already have the new iOS 27, and Mac OS 27, and blah blah blah 27.
So, yeah, then we will… Probably be able to discuss what minimum versions we can support. Yeah, probably something.
Much newer, so we will be able to use it.
Newer things.
So, yeah, that, that will, that, that will come, yeah.
Soon.
So yeah, apart from that, I don't know, John from Apple, Anything about the… this document? Anything you… Have in mind for it, or it's just… or just… you just came, to the meeting as… as…
**John Rudden (Apple Inc.)** 08:29 I just came to the meeting following up from a break. I wanted to start participating, so I was going to, lurk for a little bit and see if I can help in any way.
**Nacho Bonafonte** 08:42 Okay, okay, yeah, yeah, perfect, thanks, thanks a lot.
**John Rudden (Apple Inc.)** 08:45 Thank you.
**Nacho Bonafonte** 08:46 Yeah, so, yeah, so regarding the next topic, issue cleanup.
We talked last week about this, there were people interested in cleaning very… all the issues that we have in the project.
I think that can be done. We can start, probably.
when we review the PRs and the current issues, and maybe if we have time, we can start removing some of the very old ones.
So… The next release of Hotel Swift, yeah, here we, we had a specific Question about, having a release for one of the users of the library.
And we released a pre-release version for him, so he could use that for his uses, because once you have a number, it works. But yeah, probably the idea is… as we have talked with, lately, is… Releasing one version, probably a bigger number one.
For core, main street library.
as the last CocoaPod supported version.
That will come.
We said end of August, early September, so probably we will try to wrap it up within the next week or two.
To have that release up. So, all the… PRs, or things that you want to… To have, it will be a good moment.
to do that.
But yeah, please, let's try not to put… possible issues in the code, because it would be the last CocoaPots version we wouldn't like to have a baggy CocoaPods version.
If it's the last one. So, yeah, And yeah, apart from that, we have a topic from Vishwan… Can you explain it, what you… yeah.
**Vishwan aranha** 11:18 Yes, so, I'm currently working on, like, consistent mobile session across SDKs, and, Hotel Swift, like, has session support from 899, the issue that I just posted in the chat, and it follows, like, 683, where, like, but I wanted to check, like, two things for this, like, can I, like, use the same session ID, to be, like, added to traces, to add two traces and logs and metrics? And, like, Can we, like, retain, this original session ID for metric crash reports that arrive after start? Like, if that is possible today, that would be great, or do we, like, need a follow-up change for this?
**Billy Zhou** 12:04 Yeah, I can't remember how I implemented the crash reporter, but it should be able to recover the session ID, at least it's, like, what I contributed to, A.Swift.
I can take a double check on the crash instrumentation, But, yeah, the same session ID applies to logs and traces, right now.
**Vishwan aranha** 12:29 Sounds good. Then I should be all set. Thank you.
**Nacho Bonafonte** 12:35 Yeah, I… Yeah, yeah, you did that part right, Billy? Do you remember if we… Yeah, that's just one session, right? For the whole, For the whole run of the app.
**Billy Zhou** 12:53 Yeah.
**Nacho Bonafonte** 12:53 Yes.
Yeah, is… I mean, there is no different sessions, right, for an app?
There is always just one session, because basically it's just one execution, right?
**Billy Zhou** 13:05 Yeah, we, when we implemented it, we just went with, the definition of, like, a expiring user session, which is, like, the typical definition.
Yeah, we, like, cache it, and I think the user defaults… The cache, and then, Yeah, it just… it just works that way.
**Nacho Bonafonte** 13:32 Okay. Yeah, so it should be more or less easy just to recover, right? It's not like the active span or something like that.
That you can have several active spans in different areas of execution.
**Billy Zhou** 13:44 No, no, there's a single… there's a single ID. Double-check the crash implementation. I should probably rewrite that.
**Nacho Bonafonte** 13:52 Okay, yeah.
**Vishwan aranha** 13:54 just to clarify, like, the session module isn't, like, strictly one session per app execution, right? It can, like, restore session from… user default across, like, launches, and then, like, rotate it after, like, inactivity or, like, maximum lifetime, and, like, link the previous ID, is that correct?
**Billy Zhou** 14:15 Yeah, exactly.
It works across launches.
**Vishwan aranha** 14:19 Yeah, and that rotation is why I'm checking, like, metric kit.
So…
**Billy Zhou** 14:24 Yeah, I mean, metricade is, like, sampled as well, isn't it? So you're… Yeah, you might have some issues there, but yeah, yeah, you can use it.
**Vishwan aranha** 14:37 I think, yeah, definitely, I think we should confirm, like, whether the original ID can be retained or document that, like, attribution limitation, if we have any.
**Billy Zhou** 14:46 Yeah, like, I think Metric… the payloads that MetricKit will support, from what I recall, like, I haven't worked on iOS since, like, November of last year, but, like, it's heavily sampled, right? So, like, the payload that is recorded by MetricKit will not necessarily be attributed to the… Like, user session that is current when it gets reported, because it'll likely, like, aggregate over, like, you know.
I don't know how exactly how it works, but it's like… where I call it, like, an aggregation.
It's not necessarily, like, real user monitoring.
So… There's that issue as well.
**Nacho Bonafonte** 15:36 Yeah, you mean that when you recover with MetricKit, it's an aggregation created later, right?
**Billy Zhou** 15:43 Yeah, like, it may not necessarily be, like, associated with the ongoing user session that it gets reported.
**Nacho Bonafonte** 15:52 In fact, it is never related with the current session, right? Next step.
**Billy Zhou** 15:57 Yeah, I didn't think it was. I'm not sure how it works, honestly. Like, I remember just being confused by, like, how it worked when I was like.
**Nacho Bonafonte** 16:04 Yeah, I think it… It… it… if I don't remember, maybe they have changed something, but I think it was every 24 hours, the next… Time you opened the app, you received.
Metric kit from the last 24 hours or so.
So you can have different sessions there, and you can have different things there.
Because as Billy said, they are just aggregated into the same Into the same value.
That's… that's why we… when we integrated with… With, with, with the OpenTelemetry metrics?
We had to create an aggregation method to add several of them automatically.
**Billy Zhou** 16:47 I see. Yeah, I was always kind of confused by how it worked. Like, a lot of it's internal only, so I guess we do have someone from Apple today, and maybe they will be able to provide some more details on how Metricit works under the hood, because I don't know if all of it's, like, documented.
**Nacho Bonafonte** 17:06 Yeah, it didn't work on that. I think it was Bryce, who did that.
**Billy Zhou** 17:11 Okay.
**Nacho Bonafonte** 17:11 But, yeah, I remember, Mentioned about that, and the problems when we change the metrics.
To the, to the updated OpenTremetry met, metrics that, yeah.
How difficult it was to… Add new values to the metrics without… The calculations inside being done.
by how OpenTelemnity is configured. So, yeah, providing just… Made-up, values, was quite tricky.
**Billy Zhou** 17:43 Okay.
**Nacho Bonafonte** 17:46 Okay, so let's go then, with, with new issues and, and… and PR, from the different projects.
Starting with CORE, Issues… I don't know… yeah, dependency does for questions about Swedish concurrence immigration.
Yeah, I think this is… the only that I think we have had some talks about it.
Yeah, I think that that's part of what we are.
It was there.
So, let's go with the peers.
Yeah, I think a plea default view when no user view matches. It was approved.
I don't… yeah, fine. But I don't know why… Science supports… I don't know why we couldn't… I think the problem was that we couldn't… We've gone with it.
kind of… Yeah, we're gonna throw a run.
When more than a month has… has moved. So yeah, this is a bit blocked.
So… NTTPOC, that's an old one.
Yeah, synchronies of OpenTelemetry singleton to resolve that erases. Yeah, this is from you, Willie. Billy?
**Billy Zhou** 19:37 Okay.
**Nacho Bonafonte** 19:37 Yeah, this was about the issue we've talked before, right?
**Billy Zhou** 19:44 Yeah, I should be able to have time, though, to work on iOS for a bit.
**Nacho Bonafonte** 19:51 Yeah, so… This was missing some changes.
Or it's… and it's a work in progress. Do you plan to continue on this, Billy?
**Billy Zhou** 20:06 Well, you asked me to rewrite, didn't, didn't you?
**Nacho Bonafonte** 20:11 Sorry?
**Billy Zhou** 20:12 You asked to, rewrite this PR, right?
**Nacho Bonafonte** 20:17 Yeah, the only thing I, basically was, about the protocol one.
That you were adding the same level to the protocol?
that… I think it forces all the implementers of the protocol to be sendable, and maybe it's not needed.
That…
**Billy Zhou** 20:36 Okay.
**Nacho Bonafonte** 20:37 young. So…
**Billy Zhou** 20:38 Yay.
**Nacho Bonafonte** 20:40 So, probably, if we can keep the protocols without forcing send-level on them, that would be great, except if we really need them to be sendable, right? But you added sendable to many protocols here, and I think that That somehow forces the implementer.
To be sent out when I don't think all of them need… to be sendable.
**Billy Zhou** 21:02 Okay, yeah, I'll reread, I'll reread.
**Nacho Bonafonte** 21:04 Only, only those that, that, that… You know, are in a callback, or have something that can… happen, into threat mode, or could be changed, would mean that. But I don't think all of the… you added many of them.
So, yeah, that's basically that.
just try to reduce all the sendable from them. For me, the rest is perfect, just… Fo… It was a bit forced, right? Making sendable all the protocols.
**Billy Zhou** 21:37 Yes.
**Nacho Bonafonte** 21:38 Probably not needed. So yeah, let's try not to… make things more complex than needed. That's the only point, but for the rest, it really makes sense. So yeah, if we can merge this, this is very important, I think.
For… for… for the next release with Suki 2.6.
5. Briley.
For… yeah, this will be great, yeah.
**Billy Zhou** 22:02 Okay, when are you trying to release the next one?
**Nacho Bonafonte** 22:07 As we have separately… we have promised.
to have the latest open, sorry, the latest CocoaPods version released.
We said end of August, early September in our plan.
So probably, yeah,
**Billy Zhou** 22:25 Okay.
**Nacho Bonafonte** 22:26 Week or two.
If that's… I mean, it's just removing… It's just removing sand double from the places where it's not. For the rest, it looks perfect.
**Billy Zhou** 22:40 Okay, thanks, Nacho. Yeah, I'll try to put out a revision today. Sorry I've been absent, I've been unable to.
**Nacho Bonafonte** 22:47 No worries, I mean, yeah, I mean… I mean, all of us are here, probably on our way.
On time, so… So, we, you, we, yeah, we, we tried to… Fix things as soon as possible, and this was working really well, so yeah, great.
**Billy Zhou** 23:06 Okay.
**Nacho Bonafonte** 23:09 Okay, this is another dependency to turn away bot.
So with this kind of workflow, yeah, and also this… what's those minimum required version, someone wanted to.
upgraded because of Xcode 27? Yeah, probably this is all, as we said before.
We… once we release the late desktop, one, and we'll merge everything to OpenTelemeter Swift. Again, we will… we will review, again, minimum iOS versions.
Yeah.
Yes, yeah, probably… focusing on Oxcode 26 minimum supported version or so. Maybe not 27, but 26.
Which is the latest one that Apple will… It's probably now letting the app… the apps to be built.
So yeah, this for the core.
Let's go with the main library.
Yeah, here is where we have lots of all issues.
That we will review later if we have time.
Okay, so we have here some issues.
Nothing new.
Next, yeah, should record payout has no effect for delegates that only if you are associated.
These, yeah, I think this has a PR, also.
Yeah, this is the URL session, Swishly.
And I think there are some… some PS promo.
that addresses exactly this about delegates. So yeah, let's go with the PRs.
Okay, let's see… yeah, KS Cross Reporter, this is very old, but yeah, believe you are here.
yeah, I think it was also quite advanced. I think… You were not here, Billy, but I think someone said was working… trying to use it, or using it in production, or near that. I don't know if it's here.
Whoever said was testing this?
That is a work in progress, Yeah, I don't know if… yeah, probably this… I don't know if you can address this also. It would be great to add that, but we can also add it later, so… Yeah, do you see… There are several, yeah, there is quite a lot of interns here.
**Billy Zhou** 26:09 Bye.
**Nacho Bonafonte** 26:11 So yeah, that, that… No pressure.
Yeah, also, we have the dependencies to the PC Swift 2, that's the same. Let's wait for… Newer versions that we are sure that doesn't bring Color dependencies that are incompatible with our minimum version.
Yeah, we also have… Pattern upload failures.
This is from Yasura.
I think these are related, right?
Yasura?
You are here? No, he… oh, he has been here before.
He… Yeah, I think they were more or less advanced.
This was working with a single weight, and it has conflicts.
Some other… yes, this other is also about… The asynchronous export.
That was supported in SwiftCore.
But they still have… It's still, as… as more complex.
So yeah, let's go with the next one.
Yeah, about URL session, there are several related to URL session.
I think the author of this is not here.
I think this is the PR about… The issue that we were talking about.
Basically, it says that Sometimes.
You, you leave sessions open, so… so the spans are leaking, because we are not capturing the, the, the… And he created some code.
I need to watch a mute.
What's missing here?
Oh, they have conflicts.
Yeah.
Okay, so we are waiting for these conflicts to be fixed.
I will ask whom.
Yeah, this was another interesting… That also has a conflict, and some… Updates recorded last week.
Yeah, this is about… The data task?
When are we capturing the ZRA session the payload?
But, yeah, it was not following.
Dude.
exactly what we say. Parameters… yeah.
Vishwan… somewhere… Yeah, this is basically the one that… you don't detect the spans that are ended from your session, or negative request that never ends, or are not captured. Sometimes you have just network requests in your app.
that… Yeah, they're just… Running when you… when the app quits, or we send it.
So we never… By default, the URL session instrumentation is not detecting them.
I'm manually closing, so you don't get a spam for that.
Will this change agree?
But the same with conflicts.
Okay, yeah, this is for associating the response with the request.
Do that, Nathan?
Professor.
so we… of truth, but… I suppose… yeah.
Payload recording to be decided at the request.
Yeah. I don't know if you're interested in this… But also, I think it's missing.
Concrete?
Yeah, it was also having some feedback not addressed, so those are for the… Where it says, yeah.
One for renovate… Treating me.
Like, something so a simpler one.
The name of the wedding?
She's been… Wait time.
Yeah, I don't know, I will check later.
I'm… Yeah, I think this is a new one, but from Yasura, we all sold it, but it's okay.
Still open.
Okay, yeah, I think those are… All the PRs.
Anyone?
That's… You want to focus on, or any other idea you have for it?
Anyone?
**Vishwan aranha** 33:35 I might have some session updates coming through, some PRs, I will just appreciate some look on that, review on that when you get a chance. Maybe, probably by next week.
**Nacho Bonafonte** 33:49 Okay, about the session?
**Vishwan aranha** 33:50 Yes.
**Nacho Bonafonte** 33:51 recommendation?
**Vishwan aranha** 33:52 So, yeah, for sessions and instrumentation, I will have some PRs coming through.
**Nacho Bonafonte** 33:57 Okay, Billy, will you have bandwidth for that?
**Billy Zhou** 34:02 Yeah, yeah.
**Nacho Bonafonte** 34:03 Maybe… I mean, just… if you have not, just say, I mean… No person anywhere.
**Billy Zhou** 34:12 Yeah, send cinema over, yeah.
**Nacho Bonafonte** 34:16 Yeah, Yeah, I… I'm totally confident on… on… on the link, video, so yeah, I will… I, I will try to, You know, review and match when possible.
Yeah.
Okay.
Do we want to review very old issues and remove those that doesn't make sense anymore?
Or… no.
**Vishwan aranha** 34:52 Go to the old ones, like, from several years ago.
**Nacho Bonafonte** 34:57 Yeah, probably not more than 5 years, I think, or 6. Yeah, I don't know, maybe.
Yeah, Linux support and new integration, I think it's extremely old.
Nope.
We don't have NEO integration.
But we have Linux support, so this…
**Billy Zhou** 35:25 Yeah, there's no Linux approval workflow, isn't there? Yeah.
**Nacho Bonafonte** 35:33 Yeah, Yeah, because the support would pass local, literally.
Language server, that's good.
From Meteor's exportation, who's God leading?
Cool.
Yeah, it was assigned to Gibbino.
Like, yesterday.
It was hard to preview, yeah.
Yeah, so it… as it's been reviewed, probably, I will keep them.
It's enough to use, huh?
review constants and determine if they need to localize. So, semantic measures we localize, and might be able to respect regarding localization.
Anything about this?
Constance and better management with two localize.
I don't think, right? Because he is the collector.
Issues to handle that.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 37:14 These are not user-facing strings, and I don't think that makes sense.
**Nacho Bonafonte** 37:18 Yeah, totally, totally agree.
your accession metrics instrumentation. Yeah, this one's very interesting. Yeah, it's… it's about… using, you can granularly instrument the… the… The network request with much granular information, not only the The duration of the task.
Yeah, there was this.
Did finish collecting metrics, and with the metrics, you could get Most of it.
At least a diamond on the areas.
Yeah, that's true. I… Address some of this in the past?
So the method was… Possible to be twisted?
But that doesn't create the spans or anything like that. That code is probably there.
I don't… yeah, but they didn't continue with it. I think we are gonna… Those must review.
Yeah, let's, let's keep that.
Yes, 10Ks.
Semantic commissions of the API… I think he's coming.
Closed, also?
**Billy Zhou** 39:02 Did I… did we change this a few months ago?
Did I do that?
**Nacho Bonafonte** 39:09 Apparently.
It was addressed long ago, yeah.
I think so.
Which one was mine.
Oh, yeah. Yeah, it's not an app.
Because we moved to… yeah.
To let go.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 39:30 On this semantic conventions topic, like, Like, did you guys, are you aware, like, there is this, federated semantic conventions, and there is, an effort to bring together client semantic conventions together in a separate repo?
**Nacho Bonafonte** 39:51 Okay, you mean… Yeah, they are in core. Semantic conventions are in core, or… You mean… We, we… Probably have an outdated version of the semantic conventions?
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 40:08 Right,
**Nacho Bonafonte** 40:08 Maybe that…
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 40:11 I think there are certain label names that are also not present in the upstream semantic conventions. For example, anything in the metric kit, signal, right? Like, that is… that is not… not part of semantic conventions. So, now OTEL allows for each, project to define its own semantic conventions.
That's the idea behind Federated semantic conventions. You… if you feel something is very specific to your platform, you don't have to… you know, convince the upstream project, hey, this is how we should name it, and it should be incorporated into the, you know, the wider, semantic convention spec. Like, each project is free to maintain its own, its own semantic conventions, it's just the maintainers and, like, can agree upon that spec.
So, I think that, that could definitely come in handy for certain, you know, certain items within our project, like metric kit labels, if we want to standardize them and include that as part of a semantic convention, so we can have a new, like.
probably some generated class or whatever, like, this could help consumers also build against a specific version, so… Just again, going back to the Metricade example, somebody building the consumer site today, they'll have to look up the names manually, and then add this.
add it on the consumer side. And if we update some label in the next version, there is no single tracker that will tell us, hey, in which version was this label name updated. So, like, just like having a semantic convention version.
that we use from upstream. We could have a similar one for the project that would hold the source of truth, and, like, any migration-related information, for the repo-specific labels.
**Nacho Bonafonte** 42:09 So, what, what, sorry, I… Not sure I understood.
All you said? Sorry, yeah, but it's, yeah, it's my English, sorry.
Yeah, you, you mean… You have such several things, right? One about each project having their own semantic conventions, and.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 42:30 Yes.
**Nacho Bonafonte** 42:32 What about us creating new semantic conventions for metricKit?
That was one thing, right?
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 42:38 Yes, yes.
**Nacho Bonafonte** 42:41 Yeah, I mean, that can work.
We could add that.
I think that, anyway, we should try to Use the standardized one as much as possible, because if not, when we… when we mix with other platforms, we will get a lot of different, semantic meanings that wouldn't be… it's a… is… Compared easily, or, or searched easily.
For the user, right?
You know what I mean? So…
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 43:19 Yes, I mean, that is…
**Nacho Bonafonte** 43:22 I think it makes sense to have… a specific… conventions for those things that are not in the spec. To be honest, yeah, that will be… that will be useful, and we are totally… With that.
But also, just to add that probably our current semantic mentions are a bit outdated, and And the spec for the semanticers is probably newer than what we have now in the project.
So Starting updating that will bring many of those.
User-client conventions that are probably not… Right now, updated, or added in the project.
So yeah, that… that's also a good PR, a good task if you want to create that.
And I think you have said another thing more?
you added something more, right?
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 44:21 But client SIG, or, like, client.
**Nacho Bonafonte** 44:26 Yeah, they're.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 44:26 Klein Ripper.
**Nacho Bonafonte** 44:27 No, the last thing you said about this, I don't remember exactly… Yeah, sorry, did I address all your questions?
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 44:39 I, I, I think so. I, I understand, like, just to add to that, I understand, like, we should, like, try and stick to the, in-off stream ones, but, like, for certain things, like metric kit, right? Like, that is very specific to the Swift, hotel project, I feel like, and, like, that, that is the whole idea.
**Nacho Bonafonte** 45:00 Yeah, I agree. Yeah, I agree. We cannot… all that is not in the spec, or that we don't expect to be in the spec. And in the future, we can also… Move to… to… to something new that appears in the spectrum.
But yeah.
I mean, we can add whatever we want, but… Yeah, we are open to adding that. But yeah, first we should try to… Use the semantic… or the general semantic conventions when possible, or try to adapt.
To existing metrics that could make sense.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 45:41 Under… understood.
Totally.
**Nacho Bonafonte** 45:48 Okay, I see.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 45:49 the tri-Agize thing, sorry, you can continue with the…
**Nacho Bonafonte** 45:52 Yeah, no, no, yeah, no worries. Also, I see that… you know, Safari has crashed somehow. I cannot select anything.
You can sleep, right? That is…
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 46:06 Yeah, yeah, yeah.
**Nacho Bonafonte** 46:06 We're trying to run.
I'll kind of… So let me quit.
Yes, you let me do your thing now.
Let's see… oh, there was something new.
Okay, reaction, I'm not really good chat.
Yeah, we can… Yeah, now it works.
Yeah, I think then we can close this, that they did already.
Add type safety to semantic attributes.
I don't know what to expect.
Yeah, I think the semantic attributes are now in another way.
Isn't that… Yeah, I know.
The semantic commencers are in core, or are in the main library?
Excuse me.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 47:48 I'm not sure about that, but, like, I think the idea in that ticket is to have classes generated that would add to the type safety, right? I've seen, like, a lot of projects use this tool called Weaver.
I mean, like, Autel projects.
I'm not sure, like, if there is Swift support for that, if that's the case, like, we can, like, generate, classes using, like, once you have the semantic conventions defined in the YAML file, I think there's a specific, format to it, and then it will generate classes on the fly, and then, All your events and everything, like, you have pre-built classes that would add to the type safety, I think.
That's the idea. I know that issue's pretty old.
**Nacho Bonafonte** 48:41 Yeah, that issue's very old. Yeah, so, yeah, we have to… Yeah, I was thinking just about this.
about… How to update these.
I don't remember… Yeah, we had this for semantic convention, but I… probably this is old.
Basically, this was a… This was the… Way to generate them automatically.
the last time it was done, that was 2 years ago. So if it has changed.
We also must update the semantic attributes file. That is… I… The semantic attributes and the source attributes are created here.
or were created here with this. And as you said, I think… This is our version of some of the incarnation.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 49:38 Okay.
**Nacho Bonafonte** 49:39 the latest one.
And this… script created the files that we had to push into the project, and commit in Azure app.
Yes, so, yeah, basically… This, this created the files with these templates.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 50:05 Okay, yeah, I think this is the same model. I mean, I think we can continue using this,
**Nacho Bonafonte** 50:12 So, probably, if you want something newer, maybe… updating this.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 50:21 Sure.
**Nacho Bonafonte** 50:22 I mean, the thing will be updating this so you get The version you want, And then run the script directly.
That's the way it was done before. I don't know if they still keep the semantic conversions with a compatible Way of doing that.
Because there was, this Docker, Image was the one that was created.
Where the last time we updated.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 50:56 Got it.
**Nacho Bonafonte** 50:57 I don't know if that's the same thing.
You want to try to address it?
And use the latest one, you… we can probably update to what we want.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 51:09 Yeah, I can, I can, you know, give it a try this week.
So, I'll be out next week, but when I come back, it's a week after, I think I can… I can let you know how that went.
**Nacho Bonafonte** 51:22 Okay, yeah, I don't know, probably it's outdated, because it… Yes.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 51:28 Okay.
**Nacho Bonafonte** 51:29 Commit was 2 years ago.
And they like to change how things work.
Yep.
Okay.
Peace.
Only issues.
Wait, so we… I'm gonna close this, because it's outdated, we still don't know how it comes now.
This is probably outdated.
Yeah, I think we can also drop this.
Okay, yeah.
I don't think anyone.
I would try to use the language.
inputs.
Definitely not.
Where we want to spend the time.
A small tutorial, I think these are done, right?
In the documentation, there are… there is a tutorial, or there is code how to do that.
In the official page, right?
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 53:30 Not sure. I've been referring to an internal implementation, mostly.
But yeah, this would be nice to have.
**Billy Zhou** 53:39 Yeah, I think we need a demo app that has all the features, especially since we're adding, like, instrumentation style.
**Nacho Bonafonte** 53:47 Oh.
Okay.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 53:56 Yeah, a demo app is a great idea. I'm not…
**Nacho Bonafonte** 54:00 We had documentation, right?
We have some examples here in the documentation? No, we have… this is our… We have some sample code.
It's not a demo project.
But it has… some documentation.
So I don't know if that's, like, a small tutorial?
I will at least link on me.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 54:51 Would you guys be open to a demo app project, like an iOS one?
**Nacho Bonafonte** 54:58 There is… I think there is a demo project for OpenTelemetry in general, right? For all the languages?
I think there is a… Did you say that?
And I think there are… samples for sampling, which is… I don't know exactly about that.
**Billy Zhou** 55:24 Yeah, this is the demo app I put together, and then… Ari has, or back when he was in Brace, they had some pretty good DevOps you can refer to as well.
Okay, so…
**Nacho Bonafonte** 55:41 Yeah, I think that for the PCL of Pente demos, probably we don't have one for Swift.
If anyone wants to add that, I don't… By the way, we have some.
At least some documentation, yeah.
And we have the examples. I don't know… these examples must compile, but yeah, they are probably very, very simple.
In our project.
No.
They're with NBC Screens.
What's coming through?
we have All right.
Because I've got QR in the CI.
This is the synthetic disclosed.
Core data instrumentation, yeah, this is something we don't have.
Price with data should be agreed.
We just have it updated, clearly, right?
Should we close it?
Because… If so, it will be with strict data, right?
**Billy Zhou** 57:28 Are you closing it?
**Nacho Bonafonte** 57:30 Yeah, I mean, there is SWIP data now, instead of core data, so SWIP data, too.
**Billy Zhou** 57:35 Oh, I see. Okay.
**Nacho Bonafonte** 57:38 So, yeah, probably it is updated, no one has… Wanted to work on this.
**Billy Zhou** 57:44 Yeah, they'll just reopen if they want it, yeah.
**Nacho Bonafonte** 57:47 Swift Tracer instrumentation, this is done, right?
We'll have a first version of the sweet taste. I'm not going to… Open the images here. Okay.
And we are almost on time. I think we can… We'd have to clean… Underline documentation, this is also done.
Excellent.
phone call closeness?
Awakening.
Yeah, I'll be using documentation with DocC. That will be great. I will leave with Docman.
Oh, I… I lost this link.
Okay.
So, yeah, I think we have done some more cleaning, and we are on time.
Yeah, anything, last minute thing?
Okay, then I think we can close it here.
Thanks for joining.
A Bonsai.
**Vishwan aranha** 59:49 You too, thank you.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 59:50 Bye.
