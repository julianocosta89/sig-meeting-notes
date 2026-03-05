SIG: Technical Committee
Date: 2026-03-04
Duration: 62 minutes
Zoom Recording URL: https://zoom.us/rec/share/47c252U7r2B0mPFcvMVGOyNJi3xlSZf-Zk0lvMEfG9nzVJvaUR7oW3oJ2yKfMeTG.vlKWPPN9vsTZSGoK
============================================================

## Zoom Recording Transcript

**Jack Berg** 01:09 Hey, Tigran, I think we need to head over to the GC?
meeting, if I remember correctly, we had unfinished business over there, and there's some context clues in the GCTC channel that that's the case.
**Tigran Najaryan** 01:23 Okay.
Is the link there?
**Jack Berg** 01:26 It's in the bookmarks for the OTELTC Slack channel.
**Tigran Najaryan** 01:33 And the shared channels is bookmarked there.
**Jack Berg** 01:38 Alison, I don't think…
**Tigran Najaryan** 01:41 I don't see it. I see meeting notes, but not.
**Jack Berg** 01:46 You're right.
I see a public GC Zoom room, but I don't see a private.
Yeah, I see you're asking a question. I'll wait for the answer.
**Tigran Najaryan** 01:58 Yeah, yeah.
Where's the rest of the TC, then? Are they… did they find their way?
**Jack Berg** 02:14 They must have, I guess.
Maybe they jumped on the public.
Zoom.
**Josh Suereth** 02:26 8.
**Jack Berg** 02:27 Josh, are we… do you know if we're finishing up our conversation with the GC today?
**Josh Suereth** 02:33 I'm gonna ask, because given Ludmela's thing came out yesterday, and I don't think we have any writing, I'll ask if I want to push back a week.
How's that sound?
**Jack Berg** 02:43 Tigran already asked a question if we're meeting today, so maybe you can just jump on that.
**Josh Suereth** 02:51 I'm trying to optimize my own time a bit, so, like, that's why I really wanted the pre-reads, but…
Oh, I need to add something to the agenda.
**Jack Berg** 03:32 And I am on… duty today to run this meeting, so I'll share my screen.
**Josh Suereth** 03:38 Okay.
Oh, we don't have an agenda yet, do we?
**Carlos Alberto Cortez** 03:44 No.
**Josh Suereth** 03:46 Okay. I have one thing,
Alright, I'll put a thing for triage… And then… Gosh.
**Jack Berg** 04:32 Alright, while you're typing out your item, I'm gonna quickly go through some of the triage links. There's nothing in the TC inbox.
There's nothing in the community inbox.
And then, unassigned… spec PRs for…
And we're applying our own filters for…
Excluding OTEPs, excluding PRs by ITC members.
And what do we got? This one seems new.
And drafts, exclude drafts.
Alright, so there's two new ones that need to be… Assigned.
**Reiley** 05:27 assignment.
**Carlos Alberto Cortez** 05:33 Yeah, you can assign that to me. Yeah,
basically, this is a very rough, you may remember we had a few different PRs,
trying to add Kotlin features to the matrix, but there was one for logs, one for metrics… no, for metrics, no. Anyway, they were splits, now we have one. So, I just need to check something that I asked Jamie to do for this PR, but yeah, I will try this.
**Jack Berg** 06:04 Sounds good.
And then this other one is…
this is about entities, so I'm going to assign Josh.
Or maybe it's… is it a combination of entities.
**Josh Suereth** 06:29 No, sorry, I was talking. Yeah, you can assign this to me. I already was talking to him in chat about this and made a few comments that he addressed.
There was one comment I forgot to actually put on the PR that I need to make. I need… so that just got dropped, but yeah, sign it to me.
**Jack Berg** 06:45 Okay.
That is everything assigned, so that's triage.
We talked about OTEP Backlog with Timebox.
So, trying to move forward some of these OTEPs that have been sitting for a while.
Let's timebox this until… 10.15?
Or 10.15 my… no, my time. 15 after the hour, let's say.
Okay, which one do we want to focus on? If I search for OTEP…
We have a lot open
A lot by Josh about entities.
Stable by default, which is…
**Josh Suereth** 07:36 Do you wanna… do you wanna just start at the… the… the oldest one and move up?
**Jack Berg** 07:42 Sounds fair to me.
**Josh Suereth** 07:44 Yeah, I wish… I wish that when you have something open for a draft for 3 months, that it changes the timestamp to be when you take it out of draft, so that they're ordered by, like, when they've been in review, you know what I mean? Anyway, this one, I think, is the longest open one. This one is,
We have prototypes for this. This is around handling, multiple different resources within an SDK.
Oh yeah, that'll be easier to read.
There's a lot of motivation here. I don't know, David, you helped implement one of the prototypes, I don't know if you can speak to this. Carlos, you reviewed it and approved it. I can let other folks defend it, but the problem we're trying to solve here is…
I'm an SDK, but I might be observing something that either has a different lifetime than myself, or that is, like, remote to me.
or, like, somehow has a different, like, tendency than the SDK itself. So the idea is that I can construct a new signal provider where I say, here is the thing I'm gonna look at now, in addition to the raw SDK, and I get a new resource that I can report data against. And then all of the complicated scenarios for handling metric.
Memory management, and making sure that traces and spans are allocated against that resource.
Oh, I will caveat that the entity SIG is not planning to drive this through.
our APIs quickly, or, like, in the near term, because we still have a lot of other things to do. This is kind of a directional PR for how we want to handle the scenario, so that we all agree to the design and the shape of the design.
**Jack Berg** 09:37 And would you… when you say you're not trying to drive it through quickly,
would you all still try to get at least the skeleton of an API added within development status, or would you punt on that as well?
**Josh Suereth** 09:53 What we're trying to do right now is get the SDK to be entity-aware first, and get that to the point where that is stable, alpha, beta, whatever. And then this will be layered in later.
So basically…
**Jack Berg** 10:05 I suppose this depends on that, right? You can't exactly have entity-specific providers until the SDK itself is entity aware.
**Josh Suereth** 10:14 Yeah.
**David Ashpole (dashpole)** 10:21 What do you think this needs to move forward? Is it just…
Raise it at the spec sig again and get more reviews, or…
**Josh Suereth** 10:27 just review… we've wasted, like, 5 times in the spec's sake. Yeah. I, like, from my perspective, I…
you know, if people don't care enough to click merge, then whatever. But, yeah, I.
**David Ashpole (dashpole)** 10:40 I think I still have a comment thread open. That's the only reason I hit the merge button, yeah.
**Josh Suereth** 10:46 I might have missed that. If you ping me what that is, I can take a look.
**Jack Berg** 10:50 So this, like, I don't have any issue with this. I think this is, like, looks good to me conceptually as an API. My understanding, based on previous conversations, is that this OTEP is specifically for the client-side folks.
We… we gotta ping them to approve this thing.
**Josh Suereth** 11:13 So, actually, they finally did a review. They finally did a review last week, and we found out that this actually does not solve their problem.
Then we talked about what… there's a whole 30 minutes in the entity SIG that is just about client-side SIG. That is a different discussion. And since that was recorded publicly, and this one is, I'm gonna say it again, we need to frickin' revisit the client-side SIG. I don't think they're building something that solves the problems that they have.
Specifically, like, the comment there was like, oh, this seems to be all about metrics, we don't care about metrics.
And the reason this cares about metrics is because if you do the shenanigans they want to do, our metrics SDK breaks.
And so you have to solve the metrics problem.
But the client-side SIG doesn't even need a metrics API the way we've defined it. I think they need a new API.
I think they, like, I think it fundamentally is different, where, like, things that live in a browser on a phone.
need a different API than things that live in a server where we have access to long-term memory, we expect lots of things, we don't have to bundle stuff into one little packet that has to get out when I'm still aware of… like, there's a separate set of problems for clients, and I think they need to address that.
This is no longer blocked by them, because they're not going to use it.
**Jack Berg** 12:31 So, so, okay, this…
This is metric-oriented, like how you framed this in the description, but it's not unique to metrics, because it describes these same APIs for tracers and logger provider as well.
Are they not planning on using those? Do they not plan on, like, having… wanting to get this, like, this mutable entities piece for the purpose of spans and logs?
**Josh Suereth** 12:55 they need a mutable entities piece, but the form factor of this is not what they need. They actually still need higher contextual… like, they actually need to reboot their SDK every time session changes, apparently.
So this is not working out for them. Like, the way this works is the SDK still remains immutable, and you construct a new OpenTelemetry API surface, right? Anytime you want to say, I'm reporting against something else. For them, that means they literally have to have some sort of,
Tracker, mutational state.
For instrumentation, where it's actually against a pointer, and they swap the pointer out to the latest thing every time.
This was the assumption, that, like, okay, we can ahead of time say.
When session changes, we'll construct our instrumentation and then register it.
Right? This is… this is more of, like, a, I know about things ahead of time. I know what I'm reporting against ahead of time.
So this is… this actually would probably benefit, like, the collector better, if the collector wanted to… would ever use something. I think there's instances in, like, the JVM world with different, you know.
Things where this would make sense.
**Jack Berg** 14:05 Yeah, it's like application servers, right? Where you want to create a different,
a different provider with a different entity per application instance within the server. But, like, you know, we've gotten by this far without there being a lot of discussion about this. So, in terms of priority around this, like, if it's not solving the browser SIG's specific problems, like, I'm not interested in spending effort.
Like, to drive this through, just because of the things we've talked about, about how, you know, it's a zero-sum game, and attention is scarce.
**Josh Suereth** 14:37 Yeah, the thing is, though, I think this does solve a problem, and I think this is the right design.
And so the question is, are we okay saying, cool, we like this design.
We can merge the design to say this is how we would do it if we need to do it, and then not change the spec, or do you want to just close this? I'm fine either way.
**Jack Berg** 14:56 Okay. I'm fine with this, by the way, this design, to be clear.
**Tigran Najaryan** 15:00 I'm still not sure I understand who is this for, then, if it's not for client sake. You said collector, but does collector need this? Is there an actual demand for that? Who is this for? I don't… I don't get it.
**Josh Suereth** 15:16 Yeah, I will say that internally, we do something exactly like this in all our metrics APIs.
And so this, this somewhat matches, like, needs that we would have. So…
**Tigran Najaryan** 15:28 Whiz, whiz, sorry, I'm not… I…
**Josh Suereth** 15:30 We use Google.
Okay. So even if we… even if we don't execute on it now, which again, it… we might not, this will probably get revitalized by, like, myself or David to push through when we're ready to. But this is… this is actually a major issue for us with OpenTelemetry APIs in this case, internally, that we don't support this.
**Tigran Najaryan** 15:51 Can you,
Are the use cases described in the OTEP? I'm forgetting, it's been a while now. If it's use cases other than the client… client-seq use cases.
If you're saying they don't want it, then in that case, we need other use cases to be described here.
**Josh Suereth** 16:11 Yeah, the general shape of the use case stays the same, it's just replace session with something else, and you're fine. And I can do that if you want. Like, I can update it to have that.
**Tigran Najaryan** 16:20 I think it would be useful, because you're saying you have the need for that at Google.
So, you do have the use cases in that case, right? So, it would be useful to understand what are those use cases. I'm not against the OTAP, I'm just saying, if the client SIC doesn't want it, if the collector does not necessarily need it.
then it becomes sort of a, okay, then why are we doing this? It would be good to have the clear answer to that question there in the OTEM.
**Josh Suereth** 16:48 Yeah, okay, I will say the use case that Jack mentioned of, like, a Java web server, if you will, is the closest that I could point to in open source. It's… but basically, if you think of a service provider.
So, like, a hyperscaler, where I have a service where I'm gonna have multiple clients and multiple things I report against, where I might have one binary that's reporting against multiple things.
I can't use our API today, or I'm instantiating it a thousand times really inefficiently with tons of different exporters, to the point where it's just not used.
So…
**David Ashpole (dashpole)** 17:24 OBI.
If it wasn't trying to be a collector-receiver, might be a natural fit for something, where you discover a process.
You want to, like, temporarily create a resource while you're generating a bunch of metrics for it.
And then you want to rip it out when the process disappears.
But, okay.
That's a real use case today, because they're trying to write to Pdata, to be a collector-receiver.
**Jack Berg** 17:53 Right, so they're not using the APIs, they're not using meter provider, tracer provider, logger provider, they're emitting the raw telemetry to PData.
**David Ashpole (dashpole)** 18:01 Those APIs may also not be performant enough for their use case today.
**Tigran Najaryan** 18:07 So this isn't… so this isn't essentially for regular applications or regular services, this is for people who are building…
Other interesting types of agents, essentially, other types of collectors.
who collect data on behalf of other things, essentially, and those other things can be numerous. There may be more than one of those things. That's when you hit this problem with our SDK.
**Josh Suereth** 18:33 Yeah, I think, basically, OpenTelemetry has an issue with any software as a service.
Any software as a service is actually really hard to do in Hotel well.
And we're running into lots of friction with it. And so, this is one of, like, a set of solutions that we're probably gonna propose to start addressing that.
**Tigran Najaryan** 18:54 I'm not sure I understand what you're saying, Josh. When you're saying software as a service, you mean there's some sort of multi-tenancy involved there, and
and you want to have the tenant ID, whatever that ID is, to be recorded in the resource, essentially. That's what you're saying, instead of it being an attribute of a span or of a metric.
**Josh Suereth** 19:16 In this case, that's what this proposal's about. When the multi-tenancy and the resource are aligned, this is a solution for that case. There are other problems with multi-tenancy that need to get addressed where that's not true. This doesn't solve all of the problems, this is just one of the problems. Yes?
**Tigran Najaryan** 19:32 Yeah, but today, the way that we solve it is by essentially saying, record your tenant ID as a SPAN attribute. That's how it works today, right? It's not that it's impossible, it's just that the shape is slightly different than maybe you would want it to be.
**Jack Berg** 19:50 to be more, more fipping if it's in the resource.
It's impractical to record it at the record level right now, because we don't have good mechanisms to store bits of data like the tenant ID in context, and have those stamped on every bit of telemetry within that context. So that's the missing piece Josh is referring to, is some sort of mechanism that's signal agnostic that allows you to select bits of data out of context and stamp them on metrics, logs, and
from an SDK config standpoint.
**Tigran Najaryan** 20:28 Okay.
**Josh Suereth** 20:29 But this is also, like, what if I instrument my… I have, like, a gateway, right? And the gateway owns a database and owns something else. And I have… that's the only thing I'm gonna have emit telemetry.
And so, I want a resource that represents the database and a resource that represents something else, but the gateway's the thing providing it. That is what this OTEP provides, and Jack is right. The overall problem that we have to resolve as well.
is that issue. Like, that… that is… that is…
Yeah, we don't have a good solution there.
**Carlos Alberto Cortez** 21:01 Don't want to interrupt too much, but is that something that the context scope attributes could help with?
Because you may remember, and I had a prototype since last month, but I wanted to go and remassage the OTEP, and…
So I can put that in my priority list.
**Josh Suereth** 21:17 Yeah, yeah, I think that is the foundation of how to solve that problem, yeah, exactly.
**Jack Berg** 21:21 Exactly. We've talked about this in the past, but, like, we've talked about how the solution needs to be twofold. This, this, like, entity-scoped providers piece that Josh is talking about solves, sort of, one category of problems with multi-tenancy, and then this context-scoped attributes bit that, Carlos, you've been talking about reprioritizing is a different level of granularity, and probably the more useful
And the piece that will be more widely adopted.
If… if we're honest. Okay.
**Carlos Alberto Cortez** 21:51 Yeah, good to know. Okay.
**Josh Suereth** 21:53 Yeah, and what you're doing, Carlos, I would argue, is high priority. This is, like, moderate priority, or low. Like, again, if we were to say, like, I still think the shape of this is right, and we will need this. If you want me to close this and not merge it now, and not worry about it, great, I'm just gonna reopen it later when it becomes a higher priority, fine.
I am worried about whether we agree this is the right direction, but I'm fine just tabling it. Like, that's fine.
**Liudmila Molkova** 22:21 I think it… if we… it seems we all agree that the design for the solving this problem is a good one, and the problem is worth solving, it's just not an immediate one.
And if we agree on all of this, we can just document this decision by approving, if we approve, and merging it, so that we don't need to go through the motions again when this problem happens. And if it never happens, we'll never implement it, there is a very low, like, risk of merging it.
**Carlos Alberto Cortez** 22:50 Yeah, that's a good one. Actually, I wanted to say that. We could do that, and in one year, if this wasn't implemented, we just had a note in the tab, like, this was never implemented.
**Reiley** 22:58 Oh my gosh.
**Carlos Alberto Cortez** 22:59 Or something like that.
**Tigran Najaryan** 23:01 So, I'm not… I'm not entirely convinced that this is the right approach, particularly in situations when you have
a huge number of tenants. This may be fine when you have hundreds or thousands of those. If you have millions or billions of tenants, you don't want to create billions of instances of resources and keep in memory.
**Josh Suereth** 23:22 Tigran, that's in the OTEP. This is designed for low tenancy. Specifically, it's called out. This is not for high tenancy. That's why I'm saying they're complementary.
**Jack Berg** 23:33 That's Carlos' bet.
**Josh Suereth** 23:34 Yeah. The context bid is what solves high tenancy, this solves low tenancy. You still need this. This is still necessary. We still need a solution for this.
But you're right, this cannot be used for the high tenancy problem.
**Reiley** 23:47 Oh my god.
**Josh Suereth** 23:47 That is a separate problem we have to resolve.
**Tigran Najaryan** 23:51 So, I don't understand. If you solve the high tenancy.
by different means. And the different means to me means you record the tenant ID somewhere in a context, and then that ID is recorded as an attribute of a span, or a dimension of a metric, if you want to record it. Why do you need this, then? Why do you need different resources?
**Liudmila Molkova** 24:15 This is a different modeling, right? So, in some cases, you want to model it as a resource attribute, and this is for the low tendency by definition of resource. Sometimes, you want to model it as the, on the individual signal level.
**Tigran Najaryan** 24:30 Okay, so it's not complementary, it's an alternate way of recording that telemetry. It's going to have a completely different shape.
**Liudmila Molkova** 24:37 Yeah.
**Josh Suereth** 24:38 Yes, it's a different model.
What I mean complementary is I think there's a set of problems around this. This is one of those problems. It's not the high cardinality tenant problem.
**Tigran Najaryan** 24:49 Okay, I'm being contrarian here, but I don't understand why do you need two different ways of doing that. Why do you want it to be in the resource, then, in that case? If you have a mechanism to have the tenant ID on a span as an attribute, why do you have this other approach, then?
**Josh Suereth** 25:06 they're not… I'm not solving the same problem.
Tenancy is a very, very, very vague term.
So, first, we probably have to agree what we mean by tenancy.
But again, this is where I have one SDK managing multiple resources and reporting data about them.
And that cannot handle thousands of different resources. We don't want to model, like, users
But that doesn't mean it's not a multi-tenancy thing where I'm managing multiple things from one process. It's just maybe, like, maybe I need to take out the word tenants and just say it is multiple resources in an SDK.
**Tigran Najaryan** 25:44 Yeah, yeah.
**Josh Suereth** 25:46 But it's, like, one… instead of having money.
**Tigran Najaryan** 25:48 But that's very different, George. This is not tenants, what you're describing. These are things that you're observing, and you want to report telemetry about those things, and those things, naturally, what you're observing is a resource, right? And the attributes should be in the resource, obviously. You can't just move them to a spam.
**Josh Suereth** 26:06 Yes, exactly.
So that's what this is about. But it's like, maybe management's a better way to do it, of like, I need an SDK that is managing a couple resources. Multi-observer SDK? Sure. We can get a different name. I called it multiple resource and SDK to be that, but then when you're asking for use cases, and I'm trying to, like, explain to you why.
Sure, I don't want to confuse you with that.
**Tigran Najaryan** 26:31 So I guess a better example would be, if I wanted to use the Autel SDK as a means to generate telemetry inside the collector, I don't have a good way to do that today. If I want to use Autel Go SDK,
in the collector to generate telemetry about, let's say, for example, I have a Kubernetes receiver which observes Kubernetes nodes and pods, and then emits telemetry using Go SDK. You can't do that today. There's no good way to do that. This would enable that, essentially.
And those are not tenants, those are… Observed resources, essentially.
**Josh Suereth** 27:14 Sure, I'll stop using the word tenant.
**Tigran Najaryan** 27:18 Okay.
Okay, it does make sense to me, but I still would like to see the use case described there specifically, because we don't do that in the collector, really. We could, but we don't, and I don't think anybody plans to make that change in the collector. And so then, who is the target then?
If for high tenancy we have a different solution, this seems to be some sort of a more niche problem to me.
**Jack Berg** 27:44 Exactly, it's niche. The example we were talking about earlier with the Java ecosystem and this sort of outdated pattern of having application servers, which run multiple applications within them is, like, a great example of when you would want to use something like this. You create one provider for each of the applications hosted by the application server, and you're emitting telemetry for many resources from one SDK.
So that's, like, the use case, but, like, to your point, Tigran, it's so niche. Like.
we're… we're not gonna prioritize this in OpenTelemetry Java.
So, yeah, it's like, you know, I think it's conceptually right, but, like, not low enough priority to steal our attention from other topics.
Can… Riley, do you have, do you want to wrap us up on this? I have to call time and move on to the other topics, you know, triage, we got a time box lesson.
**Reiley** 28:43 Yeah, so I… I see why Tigrant has this concern. I observed exactly the same thing in Microsoft over the past couple years.
And, so first, I… I suggest we keep the tenant name, but we should write some supplementary guidelines to tell people a tenant can mean 100 different things, and what exactly are we talking about? Avoiding that term is not going to help, because that's a common term that everyone uses.
And then the second one is, depending on what tenant you're dealing with, like, in either host, there's many different teams in Microsoft running service, like either storage, networking, so they, they think this is a tenant. But when you take storage as a particular service.
they're handling requests from whatever user, right? So over, like, one hour, they could be handling 1 million users, and they have audit logs. They don't want to send user A's audit log to user B.
So you can imagine, there's a busy stream, they have all the audit logs, and each one will have the user's resource ID or something, tenant ID. They have to roll the data to a particular user, and mixing that would be a disaster. So this is also tenant, and you can imagine in one single application, there's a mixture of
which team in Microsoft owns this data? This is tenant. And then for that team, which customer is, you know, that's tenant? So there's also a tenant inside tenant, like, let's say, like, 3 layers of tenant. So.
Tigran's concern, I think, can be solved by, we clarify what tenant means, and we give clear recommendation. Like, we gave examples. In this case, you should go and put resource. In that case, you don't use resource, you should use contacts. Otherwise, we give people a gut feeling, like, we have three solutions for the same problem, and they always misuse that.
That's the last time I heard in two years. Total, total.
**Jack Berg** 30:34 Totally, like, there's zero mechanisms to solve this problem today. When multiple mechanisms exist to solve the problem, we need to provide guidance on which to use and when.
**Tigran Najaryan** 30:44 I mean, it's not zero, right? You just have to do it explicitly. You obtain wherever your tenant ID is, and then you add it as an attribute to a spam, right? It's doable, it's just manual.
**Jack Berg** 30:57 It's not practical because the users rely on library instrumentation and auto instrumentation.
**Tigran Najaryan** 31:04 I get it, yes, yes.
**Jack Berg** 31:05 So, practically speaking, you'd have to rewrite all the instrumentation to make this happen.
Alright,
Please go leave your thoughts on that, OTEP. Let's try to make progress one way or the other. If you think that we should reject it and reopen it when it becomes a bigger issue, reflect that in a comment. Let's try to make progress on these things instead of letting them languish.
Okay, moving on in the agenda. Josh, you've got the topic.
**Josh Suereth** 31:38 Yeah, Profiling wants to go to Alpha. We had a side… we have, like, a… Tigran and I are their, sponsors, so there's a sidebar about this, about how we should probably be doing a technical review, of what they're doing. They will be at the SIG presenting next week, so I just want to give everyone a heads up, please attend that. They're gonna walk through what they did, and just…
Briefly, for folks to bone up.
I think the big thing is actually that the protocol wants to move to alpha.
The protocol, currently adds dictionary support. They have very large data demands. There was a lot of investigation done into how to do this in a non-breaking way, and how to make it work in the collector efficiently, all that. The TLDR is
Probably, if we could go back in time and have dictionaries from the get-go, given what we learned, maybe that would have been a good idea.
But for now, we're allowing that for profiling. It will be in some of the, core OTLP things as optional, where it's only used for profiling, and other signals need to ignore it.
And then there's one last kind of blocking decision that Bogdan raised that I wanted to have a discussion here briefly on, that I think this might need to get escalated to the whole TC if we can't resolve the issue. But this is basically, they're adding units
For, attribute key-value pairs,
as part of PPROF compatibility. You can read Bogdan's concern, you can read Tigran's answer and my answer here, but effectively, this is something that we've been asked to do already in semantic conventions, to, like, have units, defined on attributes, and have a way to communicate this with people.
This is like,
effectively, if we have attributes that are values, like ints and doubles, people are reporting values that have units to them, and they want a way to communicate that. And so, the future that I see is, I would love if we could have a way for schema URL to encode that, so you don't have to send it over the wire.
for compatibility with protocols where you have to send it over the wire, or where there's, like, a need to do so, you know, in a hard-coded way, or you're not using schema URL,
Having an optional ability to encode unit makes sense. We absolutely need it for PPROF compatibility. If we want to be able to send a PPROF over OTLP and reconstitute it, it has to be in the protocol.
So, from my… my opinion is, long term, it'd be nice if we support this across OTLP everywhere. In the short term, I'd like to get it into schema URL.
And make sure that we can transmit it that way, and I think that alleviates a lot of the friction for hotel, but I don't think this is a blocking change. Tigrin, I don't know if you want to add to that.
**Tigran Najaryan** 34:27 Yeah, I agree with that. I don't think this is a blocking change. I don't think it should be a blocking change. If we make every single issue like this a blocking change, then we won't be able to make progress on new signals, right? It's just, philosophically, I think it's the wrong approach to try to block everything there. Now.
Do we need units elsewhere? I think they would be very useful if there is anybody who is willing to spend time on figuring out how do we bring them to other signals.
in a non-breaking way, that would be great. If there is no one willing to do that, then profiling should be able to still make progress. I suggested that before they go stable.
we… we give it a last chance, I guess, for people to say if they want to add units to… to… to prop to… sorry, to trace it, or to… to… to map… to… to… to logs, primarily, I guess. We could make that happen, and then eliminate this key value and unit, right, in that case.
If that doesn't happen, this should go as it is, in my opinion. And the main argument why it should be in the protocol and not just in the semantic conventions, to me, is that idea that we always had for OTLP that
OTLP should be expressive enough that you can convert from other formats into OTLP without losing data. And in this case, PProve being an important profiling format requires that.
you can have units in PProf, and when you convert to OTLP, there's no place to put that data. This creates that place for that data. This, to me, would be the main argument in favor of having it for profiles.
Consistency, sure, good to have. If we… if we can't have it, then so be it. It doesn't have to be a 100% consistency principle.
**Jack Berg** 36:36 And so…
failure to do this. So, like, I… there's some good arguments for why we should do this. It's, you know, compatibility with BPRO,
And even if this information can be communicated in semantic conventions, it's good to have OTLP be as expressive as possible, even if it doesn't need to be used, even if that expressiveness doesn't need to be leveraged.
And on the other side of things, like, if we fail to do this, we… we lose? We lose compatibility with PPROF? What's the impact of that?
**Tigran Najaryan** 37:20 Yes, I think we'll lose that, right? We lose the ability to receive PPROF payloads
And transmit them using the collector without essentially losing some of the original meaning of the data.
**Josh Suereth** 37:33 Well, this is like Jack saying, we don't want Prometheus compatibility.
or we don't give a crap about open tracing, or, you know, like, that's how important PPROF is to profiling right now.
**Jack Berg** 37:47 Yeah, like, you lose the lossless translation, and… and when you lose the lossless translation, it's sort of like a, even though it may seem like a small part of PPRO, it, like, it… it creates a bigger issue, because it creates this, like, sort of cultural clash.
That, and…
Prometheus and OpenTelemetry have had this as well. Like, you… the optics are important, even if that information can be… isn't absolutely critical to the, even if it's not critical to have a lossless translation and round trip, and you can make up for it in other ways, the optics still matter.
**Tigran Najaryan** 38:29 Yo.
At the same time, Jack, I think the… that principle of lossless translation was one of the reasons why the collector is successful.
If we… if we didn't have that.
As a property of the collector.
I think it would be, like, much harder to use in environments where you had other types of formats already in place.
So, I would like to stick to that, if possible.
as a principle, when we're designing the protocol. It enables the ecosystem to be interoperable with other participants, like Prometheus, like PProv.
**Jack Berg** 39:12 We've done similar things to this, actually. So, in the metrics, P-Pro.
We added a… I think it's called metadata?
We added an additional place to store metadata, which is not part of, like, you know, a metric identity, but facilitates lossless translation to Prometheus, where the metric types don't have, like, a one-to-one relationship.
And this seems like a similar thing, and I think that was good to do in the metrics case for Prometheus compatibility.
So what do we do? Okay, we, like, we can go forward with this, because profiles is just alpha for now, and you know, we can have this conversation about whether we want to bring this everywhere, or just limit it to profiles.
later, because it's not like it's stable yet, but there's… there's benefit of getting it right now, because even when stuff is experimental in Protobus, we have to… we have to stick with that forever, so it's not like that type can ever go away.
**Josh Suereth** 40:14 Yeah, so I'll call out, like, high level, because Profile wants to go to Alpha, what we need to do is collect a list of decisions that were made, and again, I want… if everyone is able to attend or watch the recording of next week's
profiling, like, demonstration, I want us to collect a list of concerns we have for them going alpha.
And, more importantly.
what is our bar for them going release? Because again, as soon as they're alpha, they're going to be pushing for release later, and there's a set of things that we want to learn and discover. So this here might be a non-blocker for alpha, it might be we want a decision by the time they release, and I want us to be very clear about those decisions with them.
Right now.
To some extent, these are coming as, like, a chain-anking exercise of, they think everything's in line, they think everything's okay, and then suddenly we say, oh, hey, no, right? So I want us to be more proactive about it.
But specifically because they want to go alpha, and because we have time to anticipate now, and we're trying to get, you know, more assurity.
That's the topic I wanted to have today, was just like, let's, you know, if folks have concerns or areas they want to know about, let's make sure they're addressed in the discussion next week.
And then, from that discussion next week, let's come up with a list of, cool, here's the things we think you really need to resolve for Alpha, here's the things we think you need to resolve for release.
And our concerns, so that we have a real, like, a better handle on our criteria, so that they can actually anticipate stuff. They're actually really good. When we give them a problem, they address it, and they work hard on it, and they do a lot of work on it.
But when we give them a problem, like, a week before they want to cut a release, which has happened every single time they've tried… like, it's like a month before KubeCon, they say, hey, we want to do something, and then we give them a list of problems. Let's get ahead of it this time.
Right? That's exactly what happened here, is they want to get this alpha for KubeCon.
Great.
Well, guess when the next cube come in? November.
Cool. Let's get everything resolved for Alpha, but then let's also understand that they're gonna try to do something for November, and let's give them a list ahead of time that they can churn through, because they're good about it.
**Jack Berg** 42:37 Yeah, I have some ideas already, but,
We'll… we'll create a list and discuss that list separately.
**Josh Suereth** 42:45 Yeah, maybe, Tigran, you and I can put together a document, and people can throw in concerns there? Does that sound reasonable?
**Tigran Najaryan** 42:53 Or maybe profiling should do that?
Do you want, like, document… doing what? Listing things that we think may be concerns, potential concerns?
**Josh Suereth** 43:03 Yeah, things that we want answers to, yeah, and then that would be a document we share with them to kind of, like, iterate back and forth and make sure. I do want to, again, get everyone just prepped for the next Tuesday.
where hopefully all those questions come, right? Because again, they're going to be walking us through what they built, the important aspects of it, that kind of thing. And so hopefully they answer all of our questions there, but that, I think, will raise all the questions and the due diligence that we'll need to do for release.
So I would want to put it together after that meeting, effectively.
**Tigran Najaryan** 43:37 Okay.
I'll need to go and read everything they have so far.
Maybe, sort of… Who has the…
full picture in my mind, so that we can do that document. But if we want to start something, I cannot do it.
**Josh Suereth** 43:51 I was literally just gonna make an empty document, people can throw questions in for now.
**Tigran Najaryan** 43:55 Yeah, do that, yeah, that works, yeah.
**Josh Suereth** 43:58 I will… I will do that and make a shareable document.
That's it for the topic, Jack. Like, I think, I think that's what we needed to say. If no one has any major concerns with the,
the current dictionary key value thing, great. We're… we'll move forward with that.
And then, when we listen on Tuesday, I'd like to know if we have any blocking alpha at the end of that. So, our next meeting, I'll put on the agenda to, like, discuss if we have any blocking concerns around profiling alpha. Does that sound reasonable?
**Jack Berg** 44:32 Yep.
**Josh Suereth** 44:33 Cool.
**Jack Berg** 44:36 Next topic, Carlos, do you want to take us away? Do you want me to share my screen?
**Carlos Alberto Cortez** 44:40 Yeah, if you could share, that would be good. It's mostly just, for your information, situation regarding that, out-of-the-box support for OpenTelemetry nodes is probably happening.
This is an ongoing discussion, and we, well, the seed, the JavaScript seed, managed to, have initial conversations. So, long story short, there were… it was a, you know, like, ongoing discussion about what approach should be taking, and this… this one that you are seeing.
What it's doing is that they are having their minimalistic
SDK, let's say, so the user can get, like, spans and probably logs using, what UP JSON, but the user cannot consume that. Like, if the user wants to use that, they just have to bring
like, the official SDK and API.
So we are trying to disclose that so at least hotel, you know, instead of whatever they use inside, they expose the API.
You know? So, it's a hot topic.
And as you… and it's, like, if you want to go and read what's happening there, it's super long. There are so many details, I put some notes in the doc. One of them is that, for example, they are complaining that,
the SDKs, like, the JavaScript SDK is to… it's too big, but probably many users don't need those many, like.
many details, they just want an opinionated default, like, they don't want… in theory, like, according to some people think here, like, maintainers of nodes, that, people… most people don't want… don't need to use custom processors or samplers, etc.
And then DiNetella was showing a potential… well, she has a prototype implementation, of ADPI investigators.
Minimalistic, and that could be used.
For example, maybe. But yeah, this is an ongoing discussion. The GC is aware of this as well?
And yeah, and, I think that, yes, as I said before, we are trying to, to make some,
They just think that maintainers are trying to make a push on, you know, opening the discussion, so hopefully it's a way saying at the start.
Instead of, well, independent of whether there's an alternative SDK implementation, at least the API is available to users, you know?
**Jack Berg** 47:04 Good Miller?
**Liudmila Molkova** 47:06 I think every runtime would have concerns with
hotel, just because runtimes are very picky, but I wonder if maybe, Riley, maybe somebody from .NET could come
And share, like, how this…
happened to be, and the… how the separation works between the .NET and OpenTelemetry .NET, I think it's super successful. Like, if the API is embedded in the runtime, well, in Node.
not the JavaScript, but the Node, it's very good for users.
Thanks.
**Reiley** 47:48 Yeah, so if, I… I have a meeting with Donald folks today. If they agree, what should be the next step?
**Liudmila Molkova** 47:58 maybe comment on this issue? Carlos, what would you recommend if you think it's a good idea?
**Carlos Alberto Cortez** 48:05 Yeah, I would say commencing, or if they have a document that they can share.
To the public? Like, and… or, you know, or write a summary of… like, summarizing what were… what are the benefits, and why it's working well for you.
**Reiley** 48:21 Okay, and by the way, this is not just .NET, I think Ross did a similar thing.
**Carlos Alberto Cortez** 48:29 Yeah, they mentioned that here as well, but I'm not, like, very familiar with that, sadly, to comment. I can take a look there as well.
**Reiley** 48:37 Yeah, is there something, like, from the OpenTelemetry TC or GC that we can do?
**Carlos Alberto Cortez** 48:43 Did you see…
**Reiley** 48:45 like, in the future, what we envision is we want each language and language runtime to do as much as possible to make telemetry API a first-class citizen, so the runtime, for example, if you have a garbage collector, I think the garbage collector also uses OpenTelemetry, and the garbage collector, of course, cannot take a third-party dependency.
Right, so…
So, like, we never had… had this position from OpenTelemetry. Well, like, internally inside Microsoft, like, I think that Mila and I worked… we had this direction for .NET.
And then we learn from that, then when folks work on Rust, we work with the Rust community, set the same direction. But I think given we learned, like, good practice is there, and we're seeing, like, good success, maybe, like, we can write some article there.
**Carlos Alberto Cortez** 49:33 Yeah, that would be great.
**Jack Berg** 49:37 Bye.
**Reiley** 49:37 Yeah, and that's something I can help, like, I'm involved, I think, Melan, up to you, like, you're also deeply involved in this.
**Jack Berg** 49:45 I've thought about her.
Go ahead.
**Liudmila Molkova** 49:47 It would be stronger if it comes from somebody who works on .NET at Microsoft, because I'm not in the position to officially comment on this, right? It's just stronger if it comes from you. I can help with the content.
**Reiley** 50:01 Yeah. I mean, for . I mean, they might be able to help, but I don't see them as part of the OpenTelemetry community. Like, why would they want to spend the energy there? But I think I'm in the right position to help.
**Carlos Alberto Cortez** 50:21 Even if an article is not possible, I would say commenting here, like, one or three paragraphs about why it's successful for you would be great.
**Reiley** 50:34 But, like, just, like, try to get a gut feeling from all of you. Do you think, like, wearing your TC hat, do you share the same vision? Like, it'll be even better that we don't ship the API artifact. The API artifact should come with the language runtime. That's our recommendation.
**Jack Berg** 50:53 Yeah, I was thinking about how this type of thing would play out, like, you know, let's say some part of the JVM internals wanted to, you know, expose telemetry, and it wanted to use open telemetry concepts rather than inventing its own. Like.
you know, what does that look like? They can't take a dependency on the API, so they create something like Node is doing here.
And you give the same example with .NET, like, the garbage collector wants to emit telemetry. It can't take an external dependency, so it has to use something that's built in. And so, it's like…
**Reiley** 51:26 API in the runtime, so don't do that in OpenTelemetry. Implement that in the .NET runtime, in the Node.js runtime in GVM.
**Jack Berg** 51:34 Right, exactly. So it's like, you know, if the API already exists, if there's already an OpenTelemetry API, and then because of OpenTelemetry's success, the runtime wants to adopt it, like, what does that process look like?
And what does it look like from, like, a governance standpoint and a backwards compatibility standpoint? It's a… it's a good problem to have, but it is a problem, and there are, like, open questions about how you actually execute that.
**Liudmila Molkova** 52:00 So, speaking on users' behalf, what it brings you?
and Java ecosystem first, and Java ecosystem context propagation sucks tremendously. If JVM supported proper context propagation, it would be
You would remove a lot of…
thread locals and, I don't know, propagations racing frameworks, right? Second part, Spring, you have this broken ecosystem. Everybody has broken ecosystem. The Spring, is like a separate API, right? If…
the API came from the runtime, from JVM, Spring would not write one. In Azure SDK, we created yet another API
abstraction, just because this is… we don't take dependencies, right? If there was part of the platform, we would not bother creating this abstraction.
So it's hard for us, better for users.
**Jack Berg** 52:59 Yeah, and a messy transition, too, if it is going to happen, and, like, you know, fraught with, like, governance issues. Like, what… I think .NET has solved these problems by having a relationship between open telemetry and the runtime.
And, like, basically, for any other ecosystem where this type of thing would happen, you need to have a similar relationship, where it's just not like… it's not like the framework just decides to go out of spec for no reason. Like, the spec still needs to dictate the design and the shape of the API, even though it's maintained by other people.
**Reiley** 53:36 Right.
**Liudmila Molkova** 53:38 So the cool part about Node, that we have very stable API. With .NET, I feel like a lot of the difficulties were because OTAL was not.
**Reiley** 53:50 whatnot.
**Liudmila Molkova** 53:50 As stable at that time.
And now we are in a good position.
**Carlos Alberto Cortez** 53:58 47.
**Reiley** 53:59 Instead of, like, just replying here, we probably need to write something, like, with all the learnings, pros and cons, because once the runtime is dependent on this, what if, like, you try to add an experimental version of the API? How would the runtime do it? Like, for .NET, they have a very rigid bar.
And they don't want to take experimental things, then from OpenTelemetry .NET project, people have some way to add experimental, then they have to educate the user that experimental API might move from the OpenTelemetry package to the runtime.
once it's stable. So, there are a lot of things that you need to consider. I don't feel it's a simple, like, comment. If you spend, like, 1,000 words, just put a comment here.
I guess we're missing a lot of important parts. We probably need to write something and review with the TC first, like, align with us, then we can always use that later if we talk about a different runtime.
So I can pull the downlight folks, which already have been doing this for, like, 4 years, and also the rust maintainers, they've tried it with a mixture of filling, like the tracing part.
It's not working well. The logging part is awesome.
**Carlos Alberto Cortez** 55:11 Yeah, that could be nice, even if it's something that, of course, we discuss in private.
Yeah.
**Reiley** 55:19 And I also play C++ standard committee, they have, like, 4 years cadence, and open telemetry time, like, wouldn't align with their 4-year cadence, so I completely failed there.
This is why we don't see any C++ as standard libraries that supports OpenTelemetry API, and I wouldn't want to try again, because, like, they work very differently from us.
**Jack Berg** 55:42 Yeah, but let's just say something that I think might be obvious, but we say it out loud. If an ecosystem or a runtime adopts an OpenTelemetry API, or they brand something as an OpenTelemetry API, but it's just, like, extremely conceptually divergent.
That's not a win.
**Reiley** 56:01 It's not.
**Jack Berg** 56:02 Right? So it's not just that the runtime needs to adopt OpenTelemetry and just start using that word, and just say, like, hey, we have OpenTelemetry API. It's like, it has to be done in a way that, like, matches the expectations of our API users across other languages.
**Reiley** 56:16 There's compliance, and also there will be people coming and say, but I'm using this old version of Java, and I don't have that, so what should I use? And I build a library that's targeting a range of GVM versions. So for the old ones that don't have this API, but for new ones, I have this API, what should I do? Do I have a…
like, a conditional dependency, so if it's a newer version, it depends on runtime. So all these problems that we've seen from .NET before.
**Jack Berg** 56:43 Exactly. Exactly.
**Reiley** 56:50 Okay, so I'll…
**Carlos Alberto Cortez** 56:51 Cheers.
**Reiley** 56:52 Alright, folks, we got back here, and we have to decide whether this is something we want to spend energy, because I feel like having a reasonable response is not a simple thing. It requires us to, like, do a reflection on what we learned in the past four years.
**Liudmila Molkova** 57:07 Having some support is better than having none, so if we don't have the energy for full…
exhaustive and everything response, maybe we can just leave a quick comment saying, okay, we actually have done through this in .NET, and we are kind of happy. Our users are super happy, the ecosystem is much better.
**Reiley** 57:30 I'll see, but I suspect if .NET folks will have energy for Node.js, I'll give it a try.
**Carlos Alberto Cortez** 57:38 Okay, thank you, yeah, I'm looking forward to that. That's it from my topic, sorry that it took longer than expected, but I think it was a good discussion.
Figure, I'm sorry.
**Reiley** 57:47 That's right.
**Tigran Najaryan** 57:50 Yeah, I don't, I don't…
Maybe we should move this to the next time, we only have a couple minutes.
I want to start the discussion now.
**Jack Berg** 57:58 That sounds good with me.
**Tigran Najaryan** 58:00 Yeah, yeah.
**Carlos Alberto Cortez** 58:01 Okay?
**Jack Berg** 58:04 Alright, then that's it. Any other parting words?
Alright.
**Josh Suereth** 58:11 Remember to sign up for the discussion with the GC to do some writing.
Prior to the next one.
**Liudmila Molkova** 58:17 Yeah, thanks, Josh.
**Tigran Najaryan** 58:21 Alright, see you next time, everyone.
5 years.
