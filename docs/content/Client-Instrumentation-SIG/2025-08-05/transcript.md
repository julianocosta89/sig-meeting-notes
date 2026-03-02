SIG: Client Instrumentation SIG
Date: 2025-08-05
Duration: 30 minutes
Zoom Recording URL: https://zoom.us/rec/share/zr6v5OuBF8iEdVgmkfm7T5tAh990hJ6eHFQlzBdaYJjOFyx-HUvvWG5kwNj5Df8S.xBJ1n8pmI40zJ6pH
============================================================

## Zoom Recording Transcript

**scheler** 01:38 Hello!
**Hanson Ho** 01:41 Hey!
**scheler** 01:43 Hey, guys.
**Hanson Ho** 01:45 Reading up on on your your your suggested change, Santa S. There's a lot of comments, of course. There's lots of comments.
**scheler** 01:56 Did this meeting happen last week? I no.
**Hanson Ho** 02:01 This is this is every because of the browser safe.
Oh, every week. Yeah, every other weekend. If if the
the have the have the sched, the schedule in the community repo changed? Or should I.
**Jason Plumb** 02:16 It has. Yeah, okay, perfect. Great changed.
I mean, at least on the calendar. I guess I don't know about the text on the read me, but the calendar has the update.
**scheler** 02:40 Yeah, I I don't see it next week. So yeah, it's updated. Okay? Good.
**Jason Plumb** 02:46 Santosh. I thought you were in California.
**scheler** 02:49 I am.
**Jason Plumb** 02:50 There are fireplaces in California.
**scheler** 02:53 I. It's it's not usable. So it's just a show.
**Jason Plumb** 02:58 I mean, I guess it gets cold in the hill country.
California is a big place.
**scheler** 03:04 Yeah.
**Jason Plumb** 03:17 Yeah, github is something special. Right now.
**Hanson Ho** 03:22 I think it's back like it it. I was able to create an issue.
**Jason Plumb** 03:25 You were.
**Hanson Ho** 03:26 And browse and browse the issues as well.
**Jason Plumb** 03:28 Can't browse prs.
**Hanson Ho** 03:32 So I'm looking at the the the spec repo, the the issue that santosh
added, and that loaded for me so.
**scheler** 03:42 Yeah.
**Jason Plumb** 03:44 Oh, maybe it's back cool.
or at least some some amount of its back.
**scheler** 04:03 Do you guys have any other topics to talk or or we can start with my.
**Jason Plumb** 04:09 Yeah, we we can get started because we only have half an hour. I think.
Martin, are you gonna drive.
**Martin Kuba** 04:18 Oh!
**Jason Plumb** 04:19 Sure not to.
**Martin Kuba** 04:22 I mean.
**scheler** 04:23 I mean, if this is the only topic we can. Yeah, depends on the topics.
**Martin Kuba** 04:29 Yeah, there's not, you know, only 4 of us here. So but yeah, go for it. Santosh.
**scheler** 04:36 Okay, so yeah. Thanks everyone. For commenting in the ticket. I think we it is.
It is, I guess, spare from
the folks who said, You know this is not part of this pack, because, you know, we don't know right? I think. Clients is I. Has it been established what the client the term client, refers to, because I think if it is not
an established term in the in the glossary or nomenclature.
then I guess it's fair to say that, hey, this cannot be generally applied to all clients. So I'm okay, not putting in the spec, but it it it can be just an fyi in the user facing dogs that the current instrumentations we have chosen to not use metrics. It doesn't mean that, you know. It is a rule. We it's just a choice that we picked, and you know you can plan your back ends
so that you know you don't need a metrics back end for supporting. You know these client instrumentations.
**Jason Plumb** 05:42 Yeah, I mean, there's.
**scheler** 05:43 Can.
**Jason Plumb** 05:44 I'm assuming this will just keep coming back up like I know I I favor this wording being put somewhere in the spec or the semantic conventions, or somewhere.
**scheler** 05:53 Me!
**Jason Plumb** 05:54 And that's kind of where the trasks last comment left off at the bottom. There is like, maybe we can put in some where it's less contentious.
But if we don't do something, we're just gonna keep having this conversation over and over again with people.
**scheler** 06:07 Hmm.
**Jason Plumb** 06:08 And which is, I mean, it's fine. I'm not blaming people. It's just like they come to the project, and they like they're like, oh, this is a metric! Why aren't we sending metrics, you dummies? And it's like, well.
we've talked about this a lot. There's a lot of history here, and it's complicated.
so I can't expect someone to jump in and just like have a a good foundation of why, it's discouraged.
**scheler** 06:29 What about the term client instrumentation, is it? It should be first.st
**Jason Plumb** 06:33 I don't think we have.
**scheler** 06:34 On, that.
**Jason Plumb** 06:34 Yeah, no, I don't. I don't think that's written down anywhere, and I would. I would sort of hand waving me personally, I would summarize it as mobile apps, desktop apps kiosks and web
like. That's that's what I think of it.
**Hanson Ho** 06:47 So I had. I had a doc that tried to define client, and I want to find a place to put it, and I couldn't find. I don't know where a doc, because I think would be useful to to basically say, when we talk about quote unquote client, we mean, basically user driven apps that that you know where
I mean.
**Jason Plumb** 07:10 Oh, yeah, look at that lot 3.
**Hanson Ho** 07:15 It. It needs to be a lot more than that like like, if if I have like, if I have a thing, where? Where can I stick a Pr and say, Hey, I'm gonna let me jam it in here.
**scheler** 07:24 But we have a starting point. We can reference this
and say that you know the instrumentations catering to the client side apps.
You know this is.
**Martin Kuba** 07:33 Hmm.
**Hanson Ho** 07:34 But like to to the point of the folks commenting, if we have a a more thoroughly fleshed out document to define the the limitations and the different expectations of what a client side app how it interacts with with hotel and what is appropriate to use. We can just stick it all there, and, in fact, put a lot more stuff in there. So I wouldn't mind using this as a opportunity to get that started and and put it there. And maybe you know, link to that page from other places like a semantic conventions.
So is there. Is there a place I can. I can stick something here.
**scheler** 08:11 What! What do you want to add.
**Hanson Ho** 08:13 A more thorough definition of what a client side app is and limitations. I'm calling out things like, Hey, metrics is not appropriate, not only because of the cardinality, but other issues as well. You know, dealing with, or it's a place where we can talk about sessions is a place where we can talk about. You know,
things that are.
**scheler** 08:32 Ideally, I think, in the specification.
You know, there could be just a a client guidelines or or one document
a separate document for for clients.
**Hanson Ho** 08:47 Okay.
**scheler** 08:48 Is is something that might be helpful.
**Hanson Ho** 08:53 Great.
**scheler** 08:54 It's in my opinion, but I I know the spec folks object.
**Jason Plumb** 08:59 We'll see. I mean, if have you attempted to land that yet, Hanson?
**Hanson Ho** 09:03 No, no, cause I couldn't find a place, but if I if just.
I'll just stick it somewhere, and they'll tell me it's the wrong place to stick it into, and I'll stick it in the right place.
**Jason Plumb** 09:11 Yes, that sounds reasonable, Martin. Your hand is up.
**Martin Kuba** 09:15 Yeah, no. I just wanted to like, say, 1st of all, sorry I haven't read all the the whole discussion on this issue. But
I'm just like trying to like sort in my head. Like, what's the goal of like putting it in specification? And
like, do we want to?
Is it for somebody like implementing a new SDK,
**scheler** 09:43 No, actually, it is not an SDK concern. It is it is an instrumentation it is, for it is not even for the
the end users, but that is second. 1st is for the instrumentation authors. We want them to not generate metrics.
**Martin Kuba** 10:01 But I mean.
**scheler** 10:02 Generate spans and events.
**Martin Kuba** 10:04 So. But I mean, we've we've basically just
We can't stop people from doing that. I mean, people could still write instrumentation.
**scheler** 10:11 Yeah, that is why that is why you know, I I don't want to sound it like it's a it's a rule. It's more of a you know the choice that
we have picked.
and this is what you would see, and it's nice to, you know. Stick to that boundary so that the end users who are.
you know, preparing their back ends, they can, you know, prepare accordingly.
**Martin Kuba** 10:36 So I'm wondering, like the reason I'm bringing it up is, I'm just wondering, like if it
would be enough to to make maybe just include it in the documentation of the on the Sdks, like, for example, in in Android, you would have like a design, Doc. That says, this is how we see this SDK being used.
**scheler** 10:56 Okay.
I mean, you'd have to like.
But the end user, I think, is the same right.
**Hanson Ho** 11:02 So so it would have to be duplicated on all kind of sdks.
**Martin Kuba** 11:07 And would have to. Yeah.
**Hanson Ho** 11:08 So so like having a place where we define more thoroughly what a client app is, and what that means, I think, is
probably about, and it also gives us a bit a stronger stance, because a lot of people come in and say, Oh, yeah, hotels got metrics. These clients are just not using it, but it's in the spec. The spec doesn't say you shouldn't use it. So we're gonna use it. And and then they go and implement. And they realize that 1st of all, the cardinality thing is going to be an issue. Even if you solve the cardinality thing, the data you get is going to be fairly useless.
Yeah, actually.
**scheler** 11:44 Actually, I I want to switch the context to that, you know, reasoning right? I think we also had some.
You know, difference of understanding on on those you know individual reasons.
and in my opinion, I think cardinality, you know, is very subjective.
Right? You know I have, you know. like.
like, I have systems at, you know, at our side, where you know we support, you know, one metric system that is, that supports high cardinality, you know. But but the the retention period is small. And and so so it's very subjective. Right? I think. I I to me,
you know. Yeah, maybe we can. We can talk about it. But the bigger reason is what you mentioned Hanson, which is a a metric, is redundant. Right. I think you know, if we need to report it as an event anyway, because it has more information, and therefore, you know, reporting again as a metric
is is not helpful because it it doesn't have everything
it doesn't have. You know, information about, you know, when it occurred more attributes than needed for a typical metric.
And therefore reporting as a metric alone is, is insufficient, and and therefore we we have chosen that the metrics is a server side concern. We'll generate metrics
from these spans or events. You know that that we will, that the instrumentations will will create
cardinality, depending on what? What is supported. You can choose to include high cardinality attributes.
I'll omit them.
**Hanson Ho** 13:34 Yeah, if if I I guess if if the folks's main concern is is that it doesn't belong into the spec, the spec is agnostic. To use case, then then we should find a place that is as prominent as we.
**scheler** 13:46 Oh, yeah, so play.
Yeah, yeah, of course. Yeah. So where to put is one aspect. The second aspect is, what do we? What is the reasoning we want to give, and and I feel like we should.
I don't know, I think. Talk not talk about cardinal team. But yeah, just.
**Jason Plumb** 14:02 I I think that it ha! I mean, I I think that this guidance is very important for anyone who's building new instrumentation like if you come into Ios and you're like, Hey, I have a cool idea. I wanna I wanna I wanna add instrumentation around this one feature, this one capability. When this one thing happens, you have to make a decision on how to implement that. Are you going to emit an event?
Are you going to emit a span. Are you going to emit a metric right.
**scheler** 14:31 You feel this should be part of the spec itself.
**Jason Plumb** 14:36 I think there needs to be guidance somewhere.
Probably spec. But I think it's important for us to establish
common practices across the platforms, ios, android and web, but also for new people that might be instrumenting their own libraries or their own internal portions of their thing, and they they want some guide. They they need to have some guidance from us that helps them craft instrumentation in a way, in a way that's consistent with the the rest of the instrumentation.
Right? If we're generating events for stuff, and they're the only metric coming out. That's that doesn't look great.
**Hanson Ho** 15:16 Vice versa.
It's data. It's data modeling issue. Right? You have these 3 flavors to pick from. You can choose a log and choose a span, you can choose a metric, and then.
you know, a lot of these times you consume things as a metric. So you're like, oh, so why don't we log this as a metric? And then you don't realize that there are issues underneath where, if you implement certain things as a as a hotel metric. You you lose a lot of the the usefulness. So like, you know, the the time component so so having so so, I definitely think it should.
**scheler** 15:48 If it is, if it is this report, where, where could it go? Is it in the policies?
I don't know. Do we have such guidance anywhere today?
**Hanson Ho** 15:57 Part of me wants to do something comprehensive, stick it somewhere, and then kind of like reverse kind of
shove it in, you know, in in cause. I I don't wanna like spend all the time debating on that issue about, you know where to put it and what's appropriate, and just put it somewhere, they'll be okay with. And then kind of say, Hey, we also want to make a reference. In the spec to say, hey? This may not be useful for the client. Use case. Look at this other, doc for more information. So something like that, I think would be I don't know. I just want to get something in there somewhere to be.
**scheler** 16:29 Then my my vote is to put in the spec in a separate client. guidelines.md.
**Hanson Ho** 16:35 Yeah, I'm just gonna try that and and see where it goes.
**scheler** 16:38 Yeah. And and reference, the glossary that you know we have already defined what a client side app is.
So people, this glossary is different than the one here.
**Jason Plumb** 16:53 Is it.
**Hanson Ho** 16:55 Yeah, that's not the repo. That's this. That's the website glossary.
**Jason Plumb** 16:59 Yeah.
**scheler** 17:00 And then then we need to add that glossary in in this book, as well.
**Hanson Ho** 17:05 I think I think starting in the repo is probably okay. And then, as long as as we could, you know, start moving stuff around. There's probably like a separate repo in the end, user repo, or something like that that maintains this or it gets generated, or something like that. I don't know. Who knows?
**scheler** 17:18 To.
Okay. So so you will, you will make an attempt. To. Okay, okay.
**Hanson Ho** 17:29 I'll I'll comment on that saying, Hey, I want to do this, and then I'm gonna shove something out there somewhere, and then, and then we'll go from there.
But then, after we figure out, and then we can clarify exactly what we want to say. But I do agree that cardinality is not the the most important thing. It's the fact. It's useless, and me probably redundant. If we actually want to make it useful. So.
**Martin Kuba** 17:54 Would we in this, in this guideline? Would we also include things like, it's like, we don't want to collect metrics in the SDK, right like sending out to the collector. But but there is still use. It's still useful to generate metrics
from the, from the, from the logs, or from the events.
So yeah.
**scheler** 18:13 Yeah.
**Martin Kuba** 18:14 So like like, would this guideline also include
guide on how to do that?
**Hanson Ho** 18:20 Yep, I I would imagine if not the 1st round, because people may take issue with recommending certain things.
**Jason Plumb** 18:27 Oh, yeah.
**Hanson Ho** 18:27 Maybe get getting something in there. But then I think if we have a place like this, then we can start talking about basically our our best practices, and and codify it into a set of recommendations and guidelines, and say.
You know it. It. We need to know when when shit happens. And for that we need to timestamp and aggregating over an arbitrary period is just we're gonna lose all that that niceness. So you know, even even if there's a need on the client to to kind of do client side aggregation, which really is, is is a scale issue. We shouldn't be recording so much that that we can't aggregate. Anyway. That's
but yeah, we it'll be a stepping stone for us to kind of like. Add more of of these opinions that are not quite specky but also kinda need to know, or else you have to kind of learn. The hard.
**Martin Kuba** 19:18 Yeah, yeah, it's almost like more best, like you said best practices as opposed to specification. Maybe that's why people are hesitant to put it in specification.
but but it needs to go somewhere.
**Jason Plumb** 19:31 Yeah, I mean, we. We ended up adding support for metrics on Android just to be consistent across the signals. I pushed back on it, and I was like, I don't. I don't think we want to make this as easy as we're making it like we should make it hard. But we we have it there. If there were guidance, you know.
then we could be consistent, more consistent between platforms.
**scheler** 19:53 Oh, you're saying that android current android installmentations already generate metrics.
**Jason Plumb** 19:58 No, but we have support for the underlying Sdks metrics. So we do initialize the exporter in the same way, and if someone were to generate metrics, they would pop out and go to the collector, or wherever they're going.
**scheler** 20:13 Okay. I think it is.
**Jason Plumb** 20:14 They get buffered through the disk.
**scheler** 20:16 Yeah, yeah.
**Jason Plumb** 20:16 To.
**scheler** 20:17 Yeah.
Now, I think that that is relatively easier to handle than you know. Removing support.
I mean removing or changing the instrumentations to to, you know, not generate a metric anymore.
**Jason Plumb** 20:30 Yeah, but I'll I'll maybe I'll phrase this a different way.
I have. No, I have no expectation right now that if a an application developer is using open telemetry, android and or the splunk distribution of such that if they decide to emit a metric I have no idea where that's going. We are not expecting to ingest metrics for android apps, and so I think
they would go out of their way to create this metric, and we get ingested, and I think it probably just goes into. I don't know even know where it goes. It goes to Apm. Or something, but it's not going to get tied into the rum experience. Not? I don't think so, and I suspect it's true of most other vendors, too, like you either have support for metrics in ROM, or you don't.
**scheler** 21:15 Exactly. I think I think we need to supplement this
with, you know, the user documentation as well.
**Jason Plumb** 21:22 Yeah.
**scheler** 21:23 Saying that, hey? These instrumentations currently only export.
you know, spans and events, and that is all you need. At your at your back end to accept and just.
**Jason Plumb** 21:36 That's why I was hoping that that guidance you know, the best practices that you started would land, but
not just, I guess.
**Hanson Ho** 21:43 I I think we could like like I said, I wanna I wanna like get it in there back backwards, because this is a limitation of the specification. It is, it is.
it's it's, it's. It's an an implementation of how to generate metrics. It's not the only way to generate metrics using hotel data. And and I fear that people going in there, you know, would just be like, Oh, yeah, there is a metrics packets. But it's not all metrics. It's
most some
try it again.
**Jason Plumb** 22:22 Alright. We have a little more time, so I'm sharing my screen.
Has anybody looked at this one yet?
**Hanson Ho** 22:28 I haven't. I will.
**Jason Plumb** 22:31 Okay? So this adds in functionality to record the details of the app
which the telemetry is coming from to enable support for non-service based scenarios like an android app. So they're trying to make a distinction here between apps
client stuff and like us like a service right? Service.
You might recall that we've talked about this topic many times, and this pr specifically adds,
app.id app dot name sounds familiar. App dot version app dot namespace
and app dot roles. Okay, just a bunch of app stuff.
To which I put a block on and said, we have talked a lot about using service versus app.
**Martin Kuba** 23:25 Yeah.
**Jason Plumb** 23:26 And
there's a lot of history here. And I linked to this pull request which links to all of the other history
which we've talked about. And
am I correct in remembering that we agreed to just concede and call it service.name, even though it is like a mobile app like that isn't decided right? So I guess where I'm what I want to think about is how it would be easier for someone to find that decision and not repeat this work again.
like there might be some other stuff in this. Pr, that's fine to land like app.id, or whatever like. If if there isn't a service.id, then that's probably fine, or I don't know namespace probably fine, but like I don't want us to repeat this discussion yet again.
and if this were more easy to find than buried in some pull request, I think that would behoove us. So it's on the same kind of topic
as this documentation problem that we're currently facing right like this should be easier for people to find.
**Hanson Ho** 24:27 I think we, if we have that landing page for, like you know, the best practices for client applications. This is where we can stick things like this. Yeah, some terminology is is not the greatest. But you know it's.
**Jason Plumb** 24:41 Okay. So maybe we just start doing this stuff in the doc site, like the website
is that is that the place to do it.
**Hanson Ho** 24:52 Maybe I know how to make a pull request to the spec repo, and they can, they can tell me. Hey, put this in the doc site. Then we'll merge it, and I can do it like that. Or if you could point me to the the doc site, I. We just need a place that is
official and visible, and I don't know if the doc site is as visible as the the repo, the spec repo. So I'm I'm okay. Ultimately, I'm okay. If it goes anywhere, you just need to pick a place. And as prominent as possible.
**Jason Plumb** 25:22 I mean the Doc site, or I'm I'm saying Doc Site and the website to mean the same thing. It's opentelemetryio.
And I think that's pretty prominent, I mean. We were just looking at this before.
**Hanson Ho** 25:37 Yeah.
**Jason Plumb** 25:38 There's so much docs in here.
**Hanson Ho** 25:41 The problem is organization. It's it's for me finding like, well, maybe this is a personal preference. But like finding the Docs and Github going to spec repo is a lot easier than trying to find anything specific in the doc site, because the the organization is haphazard.
**Jason Plumb** 26:02 But you'll see, like I just looked for Android just as an example. And I'm sure it's the same, for Ios.
All of these links are basically to the Simcov
maybe it's this one isn't. What is this?
Let's see.
**Hanson Ho** 26:20 Found that.
**Jason Plumb** 26:21 Pay.
**Hanson Ho** 26:21 And Chinese, one.
**Jason Plumb** 26:23 But there's like nothing. There's no docs at all on open telemetry. I/O, about Android period like getting started. What versions we support the desugaring, like none of that is mentioned anywhere in the website.
the fact that, like, there's nothing anywhere. So if you were looking at like clients, instrumentation, for example, like it's again we're we're deep down the SIM com, I think, having some landing pages.
**Hanson Ho** 26:50 There's open challenger client design. Oh, I'm sure this is a different word. The client means different things in this context.
**Jason Plumb** 26:56 Sure it does.
**Hanson Ho** 26:58 No. But yeah, you're completely right. There's there's a stub page for Android, and if there's nothing else, it's just linked to the to the github repo and for ios, and for web.
**Jason Plumb** 27:10 What?
**Hanson Ho** 27:11 Yeah. The.
**Jason Plumb** 27:12 Okay, coming soon. Okay, so like.
**Hanson Ho** 27:14 Yeah.
**Jason Plumb** 27:15 You know, if there was like client and then under client, if we had
whatever android Ios web like Web, isn't it? Already in a different area?
**Martin Kuba** 27:26 I don't think it's. I think it's under Javascript.
**Jason Plumb** 27:29 Yeah, which is the whole. I mean, I'm not involved in that Sig. But right.
**Martin Kuba** 27:34 Click, on.
**Jason Plumb** 27:34 Some of that. Yeah.
**Martin Kuba** 27:36 Expand getting started.
There's.
**Jason Plumb** 27:39 Yeah.
**Hanson Ho** 27:40 Hey? If you click view pay. Actually, I can do that view. Page source, what do you get
like? There's like an edit.
Yeah.
Okay.
**Jason Plumb** 27:49 Through the website.
**Hanson Ho** 27:50 Oh, the website has its own repo.
**Jason Plumb** 27:53 Yeah, yeah.
Same org. But yeah, this is.
**Hanson Ho** 27:57 Okay, well, this this will be a much less contentious place.
**Jason Plumb** 28:02 Doesn't.
So that's what I was thinking. Cause it's like, it's more informative. It's guidance, you know. We've we've we do use the word best practices. It doesn't have to be like this very specific like, don't use metrics on mobile, like, you know, it's more like, Hey, here's a paragraph on the reasons why or we can also have a decision log on here, which is like we've decided to use service.name. Do not please try and add app name.
**scheler** 28:26 1 1 1 challenge, though with this is you will have to repeat it, for you know Browser Android.
**Jason Plumb** 28:33 Well, that's why I was just saying.
**Hanson Ho** 28:34 Yeah.
**Jason Plumb** 28:35 I was speculating like under platforms. If we had client here, then Android and Ios and Web could be under that, and then the the client is like a roll up, and we can put stuff that applies to all 3 in that top client area.
**Hanson Ho** 28:47 Someone got a coming soon. Stub merged. I could put.
**Jason Plumb** 28:51 O'clock.
**Hanson Ho** 28:51 And then all 3, and say, Coming soon, I'm improving the coming soon, and then and then we can add to the coming soon by removing it.
**Martin Kuba** 29:01 That's so funny. When was this? February? Okay, I didn't even know that was out there.
**Hanson Ho** 29:04 Alright! No, no! This is this is good, I mean.
**Martin Kuba** 29:06 Jason.
**Hanson Ho** 29:07 Right.
**Martin Kuba** 29:07 I like this idea.
**Hanson Ho** 29:10 Great Idea.
**Jason Plumb** 29:13 That's cool. We like the website.
**Martin Kuba** 29:17 About the service name. I also wonder like if there could be a note added to the semantic conventions.
You know it's it says, like, I'm looking at the semantic conventions right now.
and it says it just says that it's like a logical name of the service. But since we
did like discuss it in the past, and like the the outcome, was that
that like this applies to everything because it's it's kind of like the unique, unique name across all everything.
Yeah. So maybe maybe it could be added as a like a
that note into semantic conventions. I think that should have been the outcome of that discussion in the past.
**Hanson Ho** 30:06 Sorry.
Think that.
**Jason Plumb** 30:07 I I didn't follow you, Martin. Sorry we're almost we are at time, but sorry.
**Martin Kuba** 30:11 No, just really quick, like you were asking is like, if this person how would this person know? And you had some like historic.
**Jason Plumb** 30:18 Yeah, yeah.
**Martin Kuba** 30:19 Historic links links to like some discussions in the past. So I'm just saying, like, maybe, like the outcome of these discussions in the past should have been a note in the semantic conventions that says that.
**Jason Plumb** 30:31 Or somewhere. That's my like somewhere. That's at least a little more visible than buried in a pull request. Right? So
agreed. Yeah, we could do better.
Alright, thanks, bi-weekly client, Sig.
**Martin Kuba** 30:46 Right.
**Hanson Ho** 30:47 All right.
**Martin Kuba** 30:47 See you later.
**Hanson Ho** 30:48 Bye.
