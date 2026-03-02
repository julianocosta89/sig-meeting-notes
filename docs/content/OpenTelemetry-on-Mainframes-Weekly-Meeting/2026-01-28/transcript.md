SIG: OpenTelemetry on Mainframes Weekly Meeting
Date: 2026-01-28
Duration: 37 minutes
Zoom Recording URL: https://zoom.us/rec/share/ro_QJY4FqzVY-R734Sm6z32NPBME38qf7cqYnb8qNrFQ1A-Lr5I7YVG3SRpNdm30.LpfyXg3IaQifEP51
============================================================

## Zoom Recording Transcript

**Ruediger Schulze (IBM)** 00:40 Hey, Greg.
**Greg Shriver** 00:42 Hey, Rudica, how are you?
**Ruediger Schulze (IBM)** 00:44 Good, good.
**Greg Shriver** 00:46 Good.
Looking good. You got a haircut?
**Ruediger Schulze (IBM)** 00:49 Yes, I did. But it's already a while ago, but you know how this is if you go for…
**Greg Shriver** 00:57 For business trip, then. Yeah.
**Ruediger Schulze (IBM)** 00:59 Get a… get a proper haircut before.
**Greg Shriver** 01:03 We're stepping on the plane, yep.
**Ruediger Schulze (IBM)** 01:05 Yeah, exactly. Hey, Richard. Hey, Kai.
**Kai Kirsch** 01:11 I don't know.
**Richard Nikula** 01:12 Evening, afternoon, morning, Whatever time it is.
**Ruediger Schulze (IBM)** 01:17 Okay.
**Greg Shriver** 01:18 Yeah, yeah.
**Ruediger Schulze (IBM)** 01:18 Thanks.
And, also, hey, Richard.
**Richard Salac** 01:23 Hello?
**Ruediger Schulze (IBM)** 01:23 We have two Richards on the call.
**Richard Salac** 01:26 Yeah, I can be Richard II on this.
**Ruediger Schulze (IBM)** 01:28 Okay, good. Okay, so I think… I guess we have a quorum to get started. So, first of all, thanks for catching up on, you know, the topics during the last couple of sick meetings when I was, you know, traveling, couldn't make it.
I wanted to go with you through a couple of topics, obviously also following up on what was discussed last week. Let me just share my screen here with Steve.
Agenda.
I suppose you can see this here, right?
Okay, so the first thing is,
Test is request for input on the semantic conventions Roadmap.
And, I started to put together a couple of points, also based on what was discussed last week, but would be good to get a little bit more clarification around that.
And, then, let's look at this, you know, what everybody would see as priorities.
And, of how we can assemble this. I, I promise to, to let Milda to send something either today or tomorrow, back on the…
on the PR. I had a brief chat with her earlier this week.
So, last week, obviously, you discussed around,
initial semantic conventions, also from, you know, a resource perspective or entities perspective, as I understand it, around services like transaction databases. Obviously, databases and messaging being in focus here, but then also APIs and HTTP.
I guess my question is,
specifically also to HTTP, I mean, there is already… Specification in place.
Do we expect to have anything different there in the area of HTTP?
Or in addition.
**Jim Porell** 03:44 I'm thinking of the wealth of HTTP servers that we ship today.
I would say that's probably pretty common.
**Ruediger Schulze (IBM)** 03:52 Yeah, so the…
I mean, obviously, there might be things like that from an implementation side, that, you know, maybe the adoption will take time of the conventions, but…
from a specification point of view, I would… assume…
That, you know, we shouldn't be doing anything different, like, like, you know, the…
Actually, you know, anything that is happening on any other platform, presumably.
And they may actually share the…
the code base, to some extent, if there's a corresponding distributed product.
**Jim Porell** 04:37 Yeah, I'm sorry I'm a little late, but we had a… we had a good discussion last week about this, and…
Given the cost of sending out metrics.
It's probably a curated list anyways.
And so, you want to keep it as high… pretty high level. Like, we have so many instrumentation points on ZOS that if we tried to semantically define all of them, we'd never finish. But if we focused on the ones that customers are really interested in.
We could probably get something done a hell of a lot faster.
That, that was…
you and I discussed that when we were in California, but it, you know, and I repeated that conversation to the team here last week.
**Ruediger Schulze (IBM)** 05:26 Yeah, right. Is this maybe fair to, you know, this comment here from the Slack channel being taken from the Slack channel, but is it fair to Atir…
Metrics into this and say.
That, essentially, we look at, a correlated list of Matrix.
Representation or current list of metrics concerning… so the resource and entity definition, apparently, right?
Plus, then, a correlated list of metrics.
You know, those type of services, transaction databases, messaging.
APIs and HTTP, HTTP maybe in brackets, given that we assume this should be actually aligning with what is already in the spec.
**Jim Porell** 06:28 I like that better, yeah.
**Ruediger Schulze (IBM)** 06:31 Okay, good. And then, obviously, infrastructure-wise, and I have a separate bullet on that here as well, infrastructure-wise, obviously, CPU being one, JVM metrics, similar,
As we are in the metrics discussion,
From a… from a pure platform perspective.
I think it's reasonable to build this up from, you know, data that is available via the HMC,
And then also metrics that would concern the virtualization layer, so basic representation of LPAR level.
metrics, and as well, if you think then about a second guest layer virtualization that also serves a proper representation, that not necessarily would have to be mainframe-specific.
But, as there's no virtualization representation today in the semantic conventions, we want to have a common concept there, and maybe this is something that
Border community will be working on as well.
So it puts us here also as a… Dependency, for our work.
But, if you think about that, and we had this discussion here, obviously, on the SIC course previously, so representation of host, hypervisor, VM,
also this representation of the relationships between them. If this will materialize throughout this year, then this obviously will help them also to represent these
platform layers.
And, I can merge that to the… I can merge that into this section above here, but I think there is a focus for this year on… on metrics that we want to get started, and essentially having… having this curated list being
being represented.
And some of this is there, but, you know, obviously, as we discussed, we need to have proper attributes then to represent some of these mainframe concepts.
I kind of want to challenge you on that one. Is the development team for the HMC going to…
**Jim Porell** 08:52 you know, issue open telemetry metrics? Do they have a plan to do that?
**Ruediger Schulze (IBM)** 08:58 I think it's not the HMC development team, probably there's this much I can say here on the call, but you can think about that, you know, there are use cases where you would translate… think about, you have the Premier Source OpenTelemetry exporter today, which is open source and available.
And you may have scenarios where you want to translate this data into proper open telemetry representation coming out there.
**Jim Porell** 09:29 Okay, because, again, I'm kind of going back to…
I think in our customers, especially the finance industry, they're looking at their transactions and stuff like that.
I… I don't see SREs really looking at… hardware…
partitions and stuff for having a lot of value. I don't know, I'm just thinking out loud here, but…
**Ruediger Schulze (IBM)** 09:56 Interesting. Yeah, there's, in fact, also a slightly different use case behind that, building it up from the bottom, but as we also have Linux 1, Linux 1C customers.
They actually have a… and obviously also the tooling in this space is a different one.
**Jim Porell** 10:16 Yeah, okay.
Juan, I get it, yeah.
**Ruediger Schulze (IBM)** 10:18 Yeah, they have this use case of having this data more generically available, while on the COS side, obviously, you know, there's existing instrumentation in various different ways in place, and like you said, right?
not all this data is required from an SRE type of persona, but that changes if you look at this from a Linux 1 perspective, for instance. So, it's probably… and the other aspect here is
This is more my assumption. If we have a proper definition of how these lower layer a resource…
This resource metrics will be named.
then I think some of this, not all, obviously, and there are more metrics, obviously, as well, but that should then actually inform of how we need to name these
These metrics on the… on the higher layers and the…
In the… in the stack, at least when it comes to things like CPU utilization, memory utilization, and so on.
Okay, then, I think aligning with this, we need to have, you know, basic resource
entities being defined. Obviously, this goes along with what we discussed above here. If there's anything missing that we want to add in or introduce there, that should be done. And then also finalizing these solvo spans. Obviously, there's distributed tracing
solutions are there?
we had the discussion about TPS, we will touch on this in a couple of minutes again, but obviously getting these, in place, and…
You know, also targeting to stabilize them in this year is probably reasonable.
So this would be these three areas, right? So, resources and entities, as much as we think we need them for metric or spend definitions, and then, in terms of stabilizing, it's probably helpful for anything moving forward to, you know, have stabilized conventions for these entities, that we are looking at, and as well, these service
bones.
To be covered.
dependency, as I said, on virtualization, and also on the relationships. My understanding is, at least.
from what I… what I have seen so far, I need to go back and check, probably, but relationships is still to be done from a… from a definition point of view.
But I think this would also be helpful once this is… Than available.
Anything else you want to add to this list?
As we are discussing here on plans for 2026.
**Greg Shriver** 13:22 I, I don't… I'm not suggesting any sort of addition.
I guess… One of the things…
So, I mean, we have, we really have… kind of slow.
In getting things moving.
and I guess…
when I view this, I'd say, what do you expect to ship in 2026 and stabilizing in 2026?
Do we really think that, even as a group, that we can get this done?
And a follow-on question to that is stabilization. Is there anything that we have to do? And this is… is there anything that we have to do? What do we have to do in order to progress to stabilization?
Is there… I mean, is it just community scrutiny on…
on the Slack channel and, in the PRs.
**Ruediger Schulze (IBM)** 14:24 That's a good question, Craig. So there is a process, which I think I need to read up on, on what means going to stabilize certain definitions.
Obviously there also needs to be implementations for this.
It's just maybe then a question, you know, among these, you know, ISVs, vendors here on the call, to what extent these implementations are there.
And that is maybe also if there's still a rate of change, but a fair point. It's probably also fair, just as we discuss around this, to maybe say stabilization is
You know, maybe not so much in focus yet.
But creating this… this, you know, specification in a development state as it's being represented on semantic conventions, I think this is crucial.
**Jim Porell** 15:21 Yeah, to me, it's PRs are done, you know, and closed.
agreed to by the community. That should be our target.
**Ruediger Schulze (IBM)** 15:29 Then let's… let me take this off, yeah.
**Jim Porell** 15:34 Those might be the right ones, but it is about PRs, you know.
**Ruediger Schulze (IBM)** 15:38 Yeah, yeah, right.
And in terms of,
you know, progress, yeah, I guess it's… it's this collectively willingness to move and push things forward.
And, I think we got certain experience now with this process. We got experience also with implementing OTEL as a, you know, as an ecosystem.
So, maybe this helps us to be more focused, or more, you know, more on the point to get these things in done.
And, yeah, I think…
Let's just, you know, also evaluate ourselves as we go, right? Do we see the progress that we want to have? And, maybe there are things where we can…
Every now and then bring somebody in as part of certain programs.
We have this…
It starts now, again, we have this, you know, for new hires, open source, contribution program.
This goes to Richard II. There was this one example of making minor updates that maybe is something, you know, for somebody who is new to this topic, but that somebody could do to do such type of contributions. And maybe sometimes there are also people that are more advanced on this.
you know, working with a community, maybe we could have some doing some of these, at least, you know, one PR for a specific topic.
Let's see how that works out. Just making this as an example.
But, maybe there are ways to bring in people, at least for…
Short period of time to get some experience, but also help us with making progress.
**Richard Salac** 17:30 I…
**Ruediger Schulze (IBM)** 17:30 Okay. Yeah, go ahead.
**Richard Salac** 17:33 No, I just, I just wanted to, say that, yeah, it depends how the discussion will evolve, but we are definitely willing to contribute. We are going to live with the OpenTelemetry for quite some time, I believe.
So, yeah, we can… we can take it forward.
**Ruediger Schulze (IBM)** 17:52 Yep.
Okay, then, yeah, long-running TPS, PR for various reasons, long-running,
Also, I have been a bottleneck on this, but… I updated it,
The good thing is, currently, I think it's… It's all checks passed.
The…
comment that I want to make, and this is based on… there was also an earlier comment from the review, from the semantic convention sig. If, you know, these protocols that we have there are really RPC, we were considering to… to include some of these, communications as RPC.
from a kicks perspective, actually, there's also an attribute, which is, let me show this…
Which is now called, DU.
It should be able to see this here.
Oh… Lots of fires, but anyway.
Dude…
Probably should open a different view for this, but the TPS facility type, which would be more indicating, like, if this is an MRO or if this is an IPIC request.
So, more being specific to…
you know, the specific implementation that we have on COS, or protocol or interface, versus just purely relying on our PC.
And so… so what I did, essentially, I made this… this whole definition of TPS more concise and removed the reference to RPC and HTTP, because also,
That might actually, you know, be a second span, so an HTTP server span, for instance, or an RPC server span, and obviously, these definitions are in place.
What I would like to ask here, specifically also, Craig, to your team, have a look again on these definitions which are being made here, if they, you know, are reasonable.
I also will still, on the generated documentation to a sanity check if this is really now looking right.
But the idea was to minimize the definition of TPS so that we actually can have this processed and then go through.
from an implementation point of view, KICS is implementing the TPS spec today, as it's being described here. IMS, not yet. It's something, once this, you know, is all
You know, being defined, they will do that as well.
just FYI.
So the link is in the… in the…
In this… in the… to the PRs in here. And… and please, please comment on the PR if you have concerns or… or questions.
Then, on the documentation PR, so, I added a couple of more comments and a little bit of wording. Go ahead, I think there was a comment.
**Jim Porell** 21:16 No, I cough, sorry.
**Ruediger Schulze (IBM)** 21:17 Okay. On the documentation PR, and Craig, we had this, I believe, discussed earlier, so thanks again for adding this.
I think it's quite comprehensive. The…
I just added a few more words and changed a little bit the couple of sentences.
Not much, and that is also still from the, the, the, the publication, SICK.
A couple of comments, so, once, you know, you have looked at them and they are good to go, it's probably more about fixing these typical issues on these documentation PRs, like.
You know.
things that are reported by linting, you know, having no empty lines, but having a last empty line, and things like this.
Aww.
Right.
And then…
**Greg Shriver** 22:16 Thank you. I'll, I'll, you know, like I said, I, I will,
Appreciate you taking a look at that, appreciate everybody's comments. I will take a look at that, and I… do… I guess, do we do the merge?
**Ruediger Schulze (IBM)** 22:30 It works like this once you have, like, on this other PR that I just showed, when once all fixes are… or all checks are resolved.
And if the approval is all in place, and at least from a SICK perspective, I did the approval now, that should be sufficient if one of us approves.
And, if then also the publication SIG approves.
**Greg Shriver** 22:57 Then that should be automatically merged, or…
**Ruediger Schulze (IBM)** 23:00 Okay. They can initiate it, right?
**Greg Shriver** 23:03 Okay.
Perfect. I will take a look at the comments, you know, your comments and the comments from the publications folks.
I'll take that.
**Ruediger Schulze (IBM)** 23:15 Okay, good.
**Greg Shriver** 23:16 forward. Thank you.
**Ruediger Schulze (IBM)** 23:18 Yeah, and then for… for the SOE discussion, switching topic, Richard.
I tried to answer here on the Slack channel, but I can maybe briefly go through this.
So, this version reporting, and obviously I noticed this is also present on Linux on C, at least according to a couple of screenshots that I'd done some time back.
That might be something that is specific to the platform and the SDK implementation, and maybe a small gap.
Could be also something like I just said, maybe if we get somebody on to, you know, first, first problem, maybe to look at.
In terms of description, what is on the spec, this rather looks like maybe a documentation thing that we should be fixing.
To fully align with what is, you know, just being returned by the SDK. The interesting point there is,
It's maybe something also to test if the SDK's implementation by default behave like if you have Java and if you have Python.
And maybe another one that would run out of the box on COS.
then to validate that, you know, there's also consistent behavior. So where I'm going is, we probably don't want to make a change to the SDK, which is platform-specific, if there's consistency in the output across those SDKs.
But, if there would be differences, then probably we want to fix this in a way that it's, you know, aligning to a common standard for the platform.
From… Recommended versus opt-in,
I would have to look this up,
recommended I always wasn't operating like this, that actually it's good if it's present, it's not as hard, like, required, obviously. There was one case where I was once testing with
Where this opt-in is then really, when you… either you opt-in or you don't get these… these attributes, which is, you know, obviously straightforward.
So
like, for things like the version here, I would actually expect this to be present. I didn't test yet, but I almost believe if you do similar things with the SDK on your Mac or on your Linux system, you will have a version information.
Alright.
When Richard, jump in if you have questions or further comments as I go through this.
Yeah, address space ID, reporting, that's actually an interesting one. So when we put the, and I said this on the slide, but when we put this back initially together, I think we were really thinking just about address spaces.
And that's a good point to actually, you know, alert or make us aware, you know, there are things like Unix System Services that, you know, needs to be taken in consideration here.
And this may be also of interest as more and more workloads maybe move to
different deployment models on COS. So, I think this is more about documentation in the first place, to be more precise in terms of, you know, if you run, let's say, Unix system services, then this is actually the pit, versus if you run this
You know, or if you have a reporting occurring open telemetry-wise from a
yeah, classical COS environment, then this should be the asset ID. Vice versa, obviously, you had to propose it to report both, which I can also see the use case for, which probably needs a little bit more of research.
**Jim Porell** 27:32 Yeah, one of the things that… that…
That discussion triggered was with respect to the process models within transaction programming.
Because the processor ID, or the, you know, the PS-type response, process ID, doesn't make any sense, kicks IMS, TV2 store procedures and stuff, so…
But that's… we have to be able to delineate that with those, you know, where that is an important… one of the curated metrics.
**Ruediger Schulze (IBM)** 28:02 Right.
**Jim Porell** 28:03 I'd be able to describe that well.
**Ruediger Schulze (IBM)** 28:05 Yeah.
Okay, and then the last one, that's an interesting use case as well.
With this dual identification of users,
It's probably, as I say here on the slide, it's probably a question to, as a semantic convention sig.
Or, or even security, semantic conventions, like, because, you know, this use case surely exists, also in other environments.
it may be something just to post on the Slack channel in the first place, if somebody has a point of view on this.
Obviously, you can always go with custom.
Attributes, but, you know.
In the end, it's better to, you know, if it's documented, then it's well described also from a community point of view.
**Richard Salac** 29:11 Yeah, thank you, and this is exactly why we raised the questions for,
I would say most of the issues that we found, that, yes, we can always go with the custom attribute.
But, I had some previous experience with observability, and one thing that… it was a lesson hardly learned.
Is to keep it consistent.
And that's why we are raising even the small things like the ZOS version, because if you have… if you have… if we are investigating, you know, some issue and correlating data from multiple services, and you have, you know, even such…
Tiny discrepancies in the versioned format, and you need to basically
Build very complicated queries and do the transformation on the fly during the query evaluation, which, you know, can make the analysis, the analysis very, very difficult.
So, on one hand, I agree with you that some things can be easily fixed in the documentation, but before doing that, I wanted to ask you and the community how to approach these kind of things in general.
Because while it is easy to fix something, probably in the Java SDK, I believe that we have to be consistent, and it may not be, for example, as easily fixed in, let's say, for some mainframe native products.
**Ruediger Schulze (IBM)** 30:52 Right, right.
And just on the point of the SDKs, I mean,
This is, by the way, also applicable to Linux 1,
sorry, on Linux and C, to some extent. We know that some of these SDKs work on the platform.
And we, we maybe even say sometimes in presentations, like share, you know, Java for CUS, Java for…
Linux on C, we know it works, it's maybe even validated to the point that it's running, but…
This is then really these… you know, there's no… no particular testing around these SDKs happening on these platforms yet by the community, or neither by the community, nor by, you know, maybe any vendor, at least I'm not aware. And…
having these issues being reported is actually helpful. I remember one…
customer that we spoke to, doing very…
And this was more about the fact, as you know, there has different SDKs for… or there has these SDKs for these different languages.
And, this customer was also comparing the state of implementation of the spec
versus these different language SDKs. And obviously, at that time, the SDKs for different languages behaved different, which adds to the problem that Richard just described. So…
being able, first of all, you know, still facing those problems, and then also, you know, let's working or work on these problems to solve them, I think this will help also the acceptance of the platform, then, in the water absorbability ecosystem, and
You may have realized this, at least for Linux on C, we have these discussions around bringing in
self-hosted GitHub action runners that actually, you know, once we could integrate them with the SDKs.
SDK teams, that would even better, because then we get also tested.
versions of these SDKs at some point. Obviously, for COS, this is maybe more challenging.
But, I guess that's, you know, that's the way to go, that we have verification done of the SDKs as well.
Okay.
Yeah, so thanks, Richard, for bringing this up, and also for this detailed information on the Slack channel, but also the presentation that you posted.
**Richard Salac** 33:49 Welcome.
**Ruediger Schulze (IBM)** 33:52 Okay, and by the way, depending on, you know, what it is, also feel free to open an issue with, you know, other, you know, other projects on OpenTelemetry. We don't have a repository ourselves anymore.
Because at some point we said that, we are actually contributing more to the other projects.
So… but, yeah, I… I think,
what I would suggest, actually, you know,
let's maybe have a little bit more testing around some of these, and then define of what we do with this and open issue. Even if we work this, like, you know, updating documentation, obviously, this is something that we can do.
If it's enhancing Java SDK, let's open the issue, then we can see who can work on this.
**Richard Salac** 34:50 Okay, sounds good.
**Ruediger Schulze (IBM)** 34:52 Yeah.
Okay.
Other topics.
Okay, then, let's talk next week, and let's see how things are progressing. Okay.
Bye.
**Richard Salac** 35:13 Thank you. Bye-bye.
**Greg Shriver** 35:14 Thanks, everybody.
