SIG: Specification SIG
Date: 2026-04-07
Duration: 61 minutes
============================================================

## Zoom Recording Transcript

**Pellared** 02:22 Oh, hello, how are you?
**Ted Young** 02:26 Hello, hello!
**David Ashpole** 03:05 Welcome, everyone. Please add yourself to the attendees list.
And if you have topics… add them to the agenda I see Jack's on the call. Jack, do you know when the next, like, deep dive from a SIG is scheduled for?
**Jack Berg** 03:37 I don't think there's… I didn't know of anyone scheduled. I was thinking about that briefly the other day, and I thought Prometheus was the last one on the books.
**David Ashpole** 03:45 Okay.
**Jack Berg** 03:50 Should probably take an inventory of, Which ones we've done this on, and which ones are still outstanding, and maybe reach out to those people.
**David Ashpole** 03:59 Okay, we'll do that offline, though.
**Jack Berg** 04:01 Yeah.
**David Ashpole** 04:53 See, I'll give one more minute, then we'll get started.
Alright then.
Welcome, everyone.
Robert, do you want to kick us off?
**Pellared** 05:39 Yeah, sure. So, I'm asking for review of this PR, which already opened the separate tab here. So, this is… this is a cleanup of the environment… environment variable carrier propagation.
And, this is just another step towards the stabilization.
in… as far as I remember, like, currently even the… what is defined in documentation, the Java and Go implementation already supports.
So the next steps after this is merged will be probably creating a spec compliance matrix, and checking how other languages are compliant with this, because there's already a C++ Python and PHP implementation, but probably you just need to be sure that they also implement in a spec-compliant way, and also if they do it, then I think we'll be able to stabilize this document, and I think the more we stabilize, the better.
And yeah, Jack, do you want to add something? Because you were recently reading this document, and you're probably more… you have more… You're more fresh than myself.
**Jack Berg** 06:49 Yeah, so, basically, the existing document provides two different ways, suggestions on how you can implement this environment variable propagator. One is by, you know, I guess, let's start with approach two. Approach two is you, you have getters and setters, which embody this, the environment variable.
propagation requirements.
And, you know, that's how almost all, all but one of the prototype implementations do it. And the other one, the approach one, is, like, you provide a dedicated environment context propagator, and it doesn't really make sense. What's the best way to put this? Like, propagators are… it's like a concept… it's like a conceptual mismatch. Like, propagators are things like baggage and W3C trace context.
and, and Jaeger, and they describe, like, how you take bags of attributes.
And, or they describe specific attributes that you use, to encode information as you're propagating from one place to another. You know, and… like, that's not what we're talking about here with environment variable propagation. We're talking about, like, hey, given a set of attributes from propagators, how do you encode those in a POSIX-compliant manner as environment variables, so that, like, a new process can read those? So I think it's, like.
You know, recommending this as a possible implementation is confusing and wrong, and the one implementation that embodies this is Swift, and I believe, Robert, that you tried to open a PR against Swift to adjust this and, you know, have it mirror the approach that we've taken in Go, Java, and other languages, and so, you know, let's just… Adriel, I see your hand up. Why don't you jump in? I think you, wrote this initial, proposal, or this initial spec.
**Adriel Perkins** 08:54 Yeah, I'll just give some context. So there were actually two, prototypes. Python originally was an AMV propagator 2, it just never got merged in.
And that was, like, 3 years ago?
Maybe… maybe almost 4 years ago was that, like, prototype was originally written, and that, like.
like, predated the whole, like, can we get this into the spec in general? So, like, the… when we went through this creation of this spec, because Python's original prototype, even though it wasn't merged, was a propagator, and Swift already had a propagator. The ask was that we just do some non-normative language for prior art. But now that we've done implementation and see, like, that the environment carriers, like, makes a lot more sense.
then I'm all for going to just the one… one case and not even having the non-normative language for how you implement this, and just saying, like, this is the way to do it. But that's just where it came from. So that's the context of, like, you know, there were a few prior arts.
Did we want them to have to change to match a specific thing? Let's just do non-normative language now, and then once these implementations and the languages start to implement this, we can figure it out from there.
I'm totally good to just standardize on one, and I want to say, you know, thank you for also, like, moving forward to stabilize this, because this is super helpful. I appreciate y'all taking the reins on that.
So yeah, I just wanted to give that extra context of, like, there was a few implementations, you know, in the past, and we had kind of discussed just having some non-normal, non-normative language to make sure, like, both were covered in that case. But AMV carriers does make a lot more sense from the perspective of.
Kind of the description you gave there from propagation, so… Yes.
**Jack Berg** 10:35 Thanks, Adriel. I appreciate that, and I think, you know, just glancing at this, we've seen 3 additional approvals since this conversation started, so, yeah, I imagine… I imagine this is going to get approved and merged.
**David Ashpole** 10:49 Alright.
Productive 5 minutes.
And Robert, I think you have the next one as well.
**Pellared** 10:58 This will be shorter, I guess. So, this has been discussed during last meeting. It has, like, 10, if I remember correctly, or 9 approvals. There's only one open conversation from Tigran.
which, if needed, I can address later, or Tigran can even address himself, it's mostly… and… Yeah, that's basically it. And I think as a follow-up, we can consider the next PR, which still is in draft.
And… oh, I see there's a new comment, which I missed, maybe?
No, there's no new one.
And yeah, Jack, go on.
**Jack Berg** 11:36 Yeah, so, I think in the last meeting, I was saying that I was gonna… I was planning on merging this Friday, if there was no additional conversation, and so, like, the reason why we want to merge this soon is because there are a number of implementations Go, Java, and .NET that, are all trying to update their implementations to add these limits.
**Pellared** 12:00 that Laura There's already PHP and Node.js, as far as I know.
**Jack Berg** 12:04 Okay, so 5 implementations. And so, like, you know, we want to make sure that at least the 4MB limit part, at least that's the part that I care about, and that the semantics around the behavior are consistent the first time that these 5 implementations go and publish new releases with these changes. So we don't want to ex… we don't want the churn. We don't want it to go from, like, 4MB to 32K, and then back up to 1MB, or something like that, because that's not a good user experience. And we're… like, I don't know about you, Robert, like, can you… maybe you can speak about the, from, like, a Go maintainer's perspective, but, like.
we have a release coming up in Java that needs to include this on Friday. So, like, you know.
It'd be great if this PR was merged so that, like, we could have confidence that there isn't going to be churn. And so, yeah, Tigran, if you could maybe clarify which parts of your comment need to be implemented for this to merge, and which could be pushed to a follow-up PR, that would be fantastic.
**Tigran Najaryan** 13:11 I think it's fine, though, I just approved, we can merge it.
We… we still need to do the request size PR, and I had a discussion with the profile exec on this, because they are probably looking at, Typically larger sizes of payloads in the request compared to other signals.
I think they will comment on the PR for the request sites, but this one I think we can nourish now.
**David Ashpole** 13:39 Alright, any objections?
Okay, cool.
And Carlos, as an FYI, that…
**Pellared** 13:57 question.
Good question to Tigran. Should I undraft my PR for the request, or not yet? Do you prefer to have it as draft?
**Tigran Najaryan** 14:06 I think it's fine. We just need to make sure we get the input from the profiling seed before we merge.
**Pellared** 14:15 Okay, so we just… so I can abrupt it and just make sure… Or you prefer to first complete as draft before we get the response from the compiler stick, or you have no opinion here?
**Tigran Najaryan** 14:27 Yeah, I think it's fine, doesn't have to be a draft. We want to make it happen, it's just a matter of getting the input from ProfilingSeek.
**Pellared** 14:35 Okay, so once this one is merged, I'll reserve the conflicts.
**Tigran Najaryan** 14:39 It's 782, right? The number is 782.
**Pellared** 14:43 Yes, I think this is the next one.
**Tigran Najaryan** 14:44 Yeah, yeah, yeah, okay.
Okay, fair.
**Pellared** 14:47 Thank you.
**David Ashpole** 14:53 Great. We have an FYI from Carlos that the… Process, context, sharing resource attributes with external readers was merged.
And then, Ted, you want to talk about system packages?
**Ted Young** 15:08 Yeah.
So, just coming back from break here, system packages is something that we know is important to end users, but in terms of, like, prioritizing it internally, I'm noticing, and this kind of came out of a conversation I was just having with Jack and Arthur before the call.
That there's sort of, like, an issue here, which is, like, the closer you are to open telemetry, the closer you are to being a contributor or a maintainer of OpenTelemetry, the less… you need this, right? Like, if you're a hardcore telemetry person, you're totally used to just installing this stuff and it seems fine. The people who get the most value out of this are actually end users who are less connected to OpenTelemetry.
And so, it feels like there's a bit of a catch-22 when it comes to trying to figure out how to prioritize this work, right? Because if we just ask each other, is this important, the answer is going to be like, but the people who would… Who it is important for, and also whom we want the feedback from as to whether we've hit the mark.
are actually these end users who are less connected to open telemetry, especially people who are more like infrastructure teams and SREs and stuff at big organizations. Like, those are the places in the wild where we're seeing, you know, people really want this kind of approach to installation.
So, my question… for the crew is just, like, what's a good way to square this circle, right? Because to get feedback from those people, the best way to do that would be to ship them a prototype, and be like, try it, and, like, is this what you want?
But in order to do that, we would want to spin up the SIG. But in order to spin up the SIG, we need to see that this is something we should maybe be taking resources away from other priorities, potentially, when we're trying to figure things out.
And we wouldn't want to do that, without some, like, proof that people really want it. So, I'm just kind of posing the question to the crew, like.
I can go gather around, you know, end users and have them kind of come back, but… and we've talked about using thumbs up and stuff like that, but we haven't really socialized any of these mechanisms for getting end-user feedback on priorities. So I'm curious what people think about this.
**Bob Strecansky** 17:47 Are we trying to think about this from a perspective of, like, I want my grandma to use OpenTelemetry, or are we trying to think about it as, like, I want my project manager to use OpenTelemetry, because I think those are two very different Mentalities, it would obviously take a bunch of different levels of effort.
**Ted Young** 18:02 Yeah, so what… where we see this is, Our current tools, basically, they automate the installation of OpenTelemetry to a certain degree, but it's still this approach where you kind of have to go one way or another and touch every application deployment to add OpenTelemetry.
And that's fine for, like, smaller crews and startups and things like that, and some larger organizations where they are capable of doing a coordinated rollout.
But what we see more often with this approach in big organizations, and it gets worse the bigger and more enterprise-y the organization is, is that asking all of the application teams to do this, and do it in a coordinated fashion is, like, really, really hard. It goes against the grain for how organizations structure, which is they want to keep all of their teams independent from each other.
The other thing is, like, often at these organizations, they would prefer that people who are more like operators, infrastructure teams, SREs, stuff like that, be the people who deploy and manage OpenTelemetry. And they can't really do that on their own with the current installation path that we have.
So it's not really about, like, letting grandma install OpenTelemetry, it's more about letting these, like, large-scale organizations install and manage OpenTelemetry.
And it's also, frankly, following in the path of, like, how APM agents and things like that have had success spreading in these organizations, in the path. They take an approach that's a little more like this.
Than what we've currently been doing.
So it's also about expectation management, with those organizations.
**Bob Strecansky** 19:51 I think this… this discussion also begs the question, too, is like, is installing this via a system package the most effective mannerism in which to… propagate all these things, or would it be better to come up with, like, as much as I hate to say it, like, an agent skill that helps to implement them, so that it can be a little bit more flexible on environment and other extraneous factors?
**Ted Young** 20:17 Josh, I see you got your hand up.
**Josh Suereth** 20:20 Yeah, I just want to… so I want to echo that the problem statement, as you phrased it, I want to get behind 100%. Like, this is a thing we see. There's usually a central… in large organizations, there's a central observability team.
They may not have access to developers, and they need to find a way to install OpenTelemetry, and that's where things like auto instrumentation are huge.
That's why, like, seeing Obi here is a big deal, right?
The thing… the thing that I, I have a few concerns, but let's talk about the governance aspect of this, because I think that's your question, right? Of, like.
We want… we… if we want this… if we want this proposal approved.
what do we need to do to get it approved? And I think that, from my perspective, I don't know if you need more user research for me. I would say that, like, we know this is a problem, and we need to solve it. The question I would have is, what would you… stop doing, so we could start doing this. Like, what… what… something's gotta give. What is it? And I think that… that's a harder discussion to have. Because I… like, sometimes when we say, like, hey, we need more evidence, this is needed, what we're saying is, we want more evidence that this is needed more than the things we're doing now.
And so I want to rephrase your question that way, of, like, what… what would you put this up against?
And I don't want to make it competitive, but technically it is, because our time and attention's limited, and we have to compete for it. So, like, I agree this is a problem, and I think it's actually, you know… there's those things that are always at the top of the next part of your list that's, you know, the top of your backlog, if you will. This is one of those top of the backlog things.
What is it that we put in the backlog to make this happen?
**Ted Young** 22:13 Yeah, completely agree. And I know, Jack, you're doing work, you know, to… to… you've got some PRs and stuff to help.
try to, clean up, that side of the fence, right? Around, like, what are our other priorities, where are we spending our time, how thin are we stretched at the TC level?
you know, being able to surface that a bit more so that we can have a more coherent conversation about… about priorities. So that… that seems relevant.
**Jack Berg** 22:43 Yeah, I'm actually going to share a link in the notes document. This is probably relevant to the broader specsig as well. So, there's this PR I have open. What I've done is I've tried to create a data model for our work streams and open telemetry. We have a lot of tribal knowledge and inconsistent vocabulary, in things. You know, there's, there's language about a SIG and, vocabulary, we call things SIGs, sometimes work streams, sometimes projects, sometimes working groups.
And maybe other terms as well. And, you know, this makes it hard for us to have, like, meaningful conversations about trade-offs. Like, hey, you know, we want to do this, this packaging SIG, but we're too busy. Okay, are we too busy? Like, where are we spending our coins? Where are our attention coins being spent?
And so, like, I view this PR as, you know, some foundational work to start to codify, you know.
where we are putting effort in right now, so that we can figure out and actually have a meaningful conversation about what trade-offs we're making to do the packaging SIG instead of something else. Please take a look if you're interested.
There's one particular piece that's, I think, cool about this, which is, like, after you have a data model, and, you know, you capture all the things that we're doing.
Right now, you can, you know, use some CodeGen to generate a mermaid.
chart that, like, is a visualization of where we're spending effort, and so I'll put a link to that as well.
And there's some interesting takeaways in there. I'm not gonna sort of lead the witness and describe what they are, but yeah, this is what… this is the current state of affairs. Go interpret it and… and make your own conclusions.
I added it to the meeting notes as a like.
**Ted Young** 24:50 Yeah, and Tigrin mentioned in the comments, you know, it's not even about stop doing X, it can be more about wait until we finish doing Y, and yeah, I think that's a great motivator. One of the things we wanted to do with projects is kind of get to a point where we can say, hey, if you want to start Y, help us finish X. And, you know, the faster we finish X, the sooner we can get to Y, so… If you're interested in Y, grab a shovel and work on X, I think is potentially another way to do this.
So… Anyways, that's kind of all I had, but one kind of action item. If people do have end users that they know of who would be interested in this, or the Kubernetes operator improved version of this, you know, have… You know, have them chime… at least chime in on that thread.
And if for no other reason, then we also then start collecting people who we can go back to once we have something for them to try, to see if it's the thing that they want.
Oops.
**David Ashpole** 26:03 Cool.
Thanks, Ted.
Josh, tell us about telemetry policies.
**Josh Suereth** 26:09 Yeah, so this is… this is just a call to please take a look. We made this in draft form, and there was a lot of work done by Jacob Arnoff. He actually put out a really cool blog article with a set of, a set of implementations that kind of blew me away performance-wise that I think everyone should take a look at. But this is a fun idea. It is something that's supposed to be complementary to both configuration and op-amp.
And it's a different take on how to control your telemetry pipelines and telemetry collection going forward. The performance numbers that Jacob showed are… fun. Like, it proves… proves out the idea. Just asking for folks to review it, take a look, take a look at the… take a look at the… set of examples, take a look at the motivation, and take a look at the blog that Jacob put out with, implementations for the collector and a… and a implementation. Yeah, I should… I should include a link. Thanks, Josh. It's in the, it's in the notes.
Yeah, please take a look at all this and review. It's ready, and just looking for folks to, you know, comment and give us feedback.
**Carlos Alberto Cortez** 27:12 By the way, if I can make a comment on that front, I just want to clarify something with you, Josh. Maybe we don't… maybe we don't have to discuss that here, maybe we can. But it seems that the SDKs could have to implement some dynamic loading, or, like, basically the configuration can be updated at runtime.
So I wanted to call that out. If that's the case, I think that maintainers have to be aware of that.
**Josh Suereth** 27:34 Yeah, yes. The current thinking there is there would be a new component that you would create within the SDK to enforce policies.
For metrics, it gets a little more awkward, so that still needs to be prototyped. But the idea would be that the configuration for control is the same regardless of what SDK you use, or if you're in the collector.
And so I just say, I want telemetry that is shaped like X, and it will get enforced somewhere in the architecture, and any component that can handle that policy will enforce it, and it only gets enforced once. So there's a set of rules in there and stuff, but yeah, like, Carlos, that's a good call-out. This is… a form of kind of a dynamic configuration capability, and that is also key to it. So, that would be something that would have to be encoded in SDKs.
There's a proposed architecture in the policy, Inside of the markdown, somewhere.
Oh, if Jacob's here, I just saw you in chat. Do you want to say anything specifically?
**jea** 28:47 Nothing in particular. I think that you've shared out most of it, I think. But happy to answer any questions. I have a bunch of implementations done, and sort of, like.
future work on this that I can share if anybody's interested. You know, mostly just here to answer any questions, though.
**Josh Suereth** 29:13 I think I only booked 5 minutes to try to get people to read it, so I expect questions to come later, but we'll be back next week to find out, those of you who've read it, what questions you have and concerns and things.
**David Ashpole** 29:39 Fun. Thanks, Josh.
Alright, and last on the agenda, Jack.
You're planning to merge… require spec changes to consider declarative config schema. I think this has… yeah, this has quite a few approvals.
**Jack Berg** 29:57 Yep, this popped up, or came up in the spec discussion several weeks ago now at this point. Just to recap, the basic idea is that declarative config is stable now, and when we propose new SDK, enhancements to the spec. We want to have those considered, you know.
with the corresponding changes to the declarative config schema. The declarative config schema is becoming an increasingly important user-facing expression of our… of, like, of our SDK API, how users actually interact with this thing, and so we want to be able to evaluate new proposals holistically, and also keep declarative config schema up to date, and sort of guarantee that.
This adjusts the, the, the spec.
You know, proposal process to reflect that.
Yeah, it's got enough approvals, I think it's good.
I'm gonna merge it, unless there's additional comments.
**David Ashpole** 30:58 Do we… should we make a change to the PR template or anything?
I don't know if that would be in here, a different PR.
**Jack Berg** 31:07 We could do that.
**David Ashpole** 31:12 I don't think it walks, but… Cool.
Alright, that is the end of the agenda. Does anyone else have topics they'd like to raise?
Josh.
**Josh Suereth** 31:35 I… I… the only thing I want to raise is, we've been doing these, Reviews of different projects in the ecosystem.
And, I'm sorry, I missed last week, I was out of office, but do we have one in the queue, in the hopper, for next? And if not, can we pick one now?
And ask folks to, come and present.
**Jack Berg** 32:10 Yeah, so I'm adding a list of ones that I know were previously done.
And, you know, the thought that we had, and I was going back through the notes, and we had this conversation back on February 17th, and, you know, on February 17th, Josh Sareth gave a sort of impromptu status update on entities.
And it was really useful. It sort of pulled this broader group back up to speed with all of the stuff that's happening with entities.
And, you know, I did a similar sort of impromptu discussion of the state of declarative config, and… we just realized that, you know, given that the maintainers meeting is gone, and the specsig is this sort of cross-functional group of people consisting of, you know, implementation maintainers and, and spec approvers and spec sponsors and that type of thing. This is a great place to keep us all in sync and apprised of the things that's happening with these various projects. And so, you know, we were tossing around terms like, hey, if you're a spec sub-sig, you need to give, like, a mandatory occasional update of your project. And I like that idea. I think we're still in the experimental phase of that, so we're looking for volunteers, but, yeah, we may, you know, change this from a volunteer basis to a mandatory update in order for these specs, sub-sigs, to continue at some point. So, yeah, you know, the context here is, in the past.
SPEC sub-sigs have, you know, gone off and worked in a group, and they've done good work and, you know, adjudicated different issues, and then they come bring their work back to the parent spec sig, and they struggle to get it merged, because everyone's like, what the heck is going on here? I haven't heard of any of this, and they have to sort of, like, re-adjudicate things that were previously discussed and, you know, are caught off guard and otherwise surprised.
And so, you know, occasional status updates help relieve that, to keep everybody in the loop so that we're not surprised when changes are happening, and so, you know, we can give the feedback earlier, rather than, you know, extremely late in the process and, you know, at the expense of frustrating those spec sub-sig, leads, so… That's the context here. What other spec subsigs do we have that, I think there's… there's sampling, I don't think we've heard from them.
There's logs, or did Ludmilla, did you give an update on logs previously?
**Liudmila Molkova** 34:43 No, I didn't, but, Trask was going to, if I remember correctly.
**Trask Stalnaker** 34:47 I was, yes.
**jmacdonald** 34:51 I think this is a great idea, Jack. I would be glad to sign myself up for a sampling update, as well as an arrow update.
On that topic, there's a lot of discussion that goes on in collector SIGs that doesn't surface here, and I've been involved in a couple of really tricky ones recently. It reminds me of Austin's proposal about stable by default, which has some conversation going on it.
I've been involved with, and yesterday, in a collector-related SIG, I was saying, this is, like, a major stability issue here.
we have to discuss it. I'd like this group to hear it, but I'm not ready to present.
I can drop some links about it if you'd like to see.
**Josh Suereth** 35:34 I wanted to back that one up, Josh. Like, a few things… thank you for proposing both of those, because I think those would be awesome. I'd love to hear more. I try to stock Hotel Arrow a lot, it's just hard to keep up with you guys, you're moving quickly.
But the, the stable by default stuff, and, like, Federated SemConv. That's another one that I was thinking about. Like, Lyudmila has an OTEP, out on that, and we've been doing a lot of work on there. I think these… anything stable by default might be a good idea to have some dedicated time here for. I want to make sure that that is moving successfully.
And, you know, we… Yeah.
if we aren't tracking it, if we aren't talking about it together, I'm afraid that it won't be moving. So, I… I hear what you're saying, and I don't want to sign up Ludmila for… for work.
Or myself, yet. But I think maybe in a few weeks, a stable by default, like, where we can talk about what we're doing with Semcov and what we're talking in the collector, we could do a set of those. I think that would actually be really valuable and timely.
Go ahead, Lou.
**Liudmila Molkova** 36:43 Yeah, I… I would be happy to sign up in a few weeks. The other thing, I would love, Jenny, I seek to share their status, because we're doing… We're considering quite a lot of… things there, and I would… I think it would be useful for the overall community to know first what we've already done, and where we're going.
I'll ask Anjani Isika if anybody would like to present it.
**Jack Berg** 37:11 Yeah, that would be fantastic. I've been taking some notes here and adding some, you know, a wish list of status updates here in the notes document, and so, in addition to sampling logs and Arrow, EBPF instrumentation, something about OBI, that would be good to hear about. You know, we talked about Josh McDonald, you talked about how the collector has conversations that are tough conversations.
you know, it'd be great to have an occasional, you know, representative from the collector here at this SIG giving, you know, giving details about the things that they're having problems with, and the things that, you know, we could help mitigate at the spec level or at the SDK level. That would be a good thing to do.
Stable by default, we mentioned that, so, if anybody wants to volunteer for that, and then Gen AI semantic conventions. So, you know, I think that the way that we can do this, for now, is that if you want to just… you know, if you want to volunteer to do this on an upcoming meeting, please just sketch out, like, add your name to a future agenda, right? Like, so add a placeholder, on, next week's meeting notes, or the week after that, or whatever date seems appropriate, and we'll plan around that.
**jmacdonald** 38:34 That sounds good, and we should all be ready to present our projects with very little notice. It shouldn't be very hard to present this kind of stuff if you're really involved in the SIG.
Since there's time here, and it's been discussed and teased already, and because we have Arthur here with us, I'm going to request if Arthur would like to give us a summary about the collector stability question that we summarized yesterday, because it's gnarly.
**Arthur Silva Sens** 39:06 Okay, I did not expect that.
As you said, I guess I can just say out of nowhere.
**jmacdonald** 39:14 You're very qualified to give this. We can also defer until later if you'd like. I think you'll do great, Arthur.
**Arthur Silva Sens** 39:22 I can talk about this specific problem. I think collector, to reach stability, it requires a lot more… there are other things happening.
But what we discussed yesterday is that in the Prometheus specification and the Prometheus community overall, it's, again, the dots versus underscores problem. In Prometheus, underscores is the sender, and there is a functionality in Prometheus that depends on metric naming, and that's why to not… sacrifice some of the features of Prometheus, we decided that the… in the Prometheus spec, we go with underscores as well.
In the collector.
**David Ashpole** 40:12 Sorry to interrupt. This is… we're mostly talking about the defaults here. So, we support both… Sanitizing to underscores and keeping the original names, but the default, based… that the Prometheus spec has is to replace dots with underscores.
**Daniel Dyla (Dynatrace)** 40:29 When you say we, in that context, you mean we, Prometheus?
**David Ashpole** 40:35 We, the Prometheus Interoperability SIG.
**Daniel Dyla (Dynatrace)** 40:38 Got it, okay.
**David Ashpole** 40:39 Yeah, with a lot of feedback from both the OpenTelemetry community and the Prometheus maintainers.
**Arthur Silva Sens** 40:48 Great, thank you.
Yeah.
So, we want it to be stable by default, right? And a collector wants to be stable as well. But today, the way Collector exposed its own internal metrics.
It does not translate dots to underscores if the metric happens to have dots, or attributes as well.
But then we are in a very tricky situation where we need to intentionally break to comply with the Prometus pack, or we will intentionally Violate the spec, just so we don't break the users.
And collector adoption is huge, so any breakage on the collector side, it has a very… high blast radios.
Yes, that's the problem, Joshua.
**jmacdonald** 41:47 Yeah, thanks, Arthur. Yeah, so, just to kind of reiterate that, we have things like attributes and metrics name… metric names coming through the collector of its own self-observability or self-diagnostic metrics, and Because of the legacy settings, it's been maintained throughout. So now we're here today, and we have these dots coming through.
And we can't fix the Prometheus exporter without changing the metrics. Like, a huge number of metrics for every collector user.
And it's… It's a problem. So, right now, we're sort of leaning towards stable by default, which means leave the work forever, and it's not very good. We're not sure what to do here.
**Jack Berg** 42:29 Well, it doesn't… it doesn't mean leave it forever. So, like, you know, in certain contexts, being stable with something does mean effectively forever, or, like, a really long time horizon. Like, you know, for an OpenTelemetry API, Like, if we had… if we decided to scrap the OpenTelemetry Java API and release it 2.0, it would be hugely consequential.
And we really don't want to do that. But, we can… we can say that something is stable in instrumentation, and then make a breaking change to it in the next major version of that, because certain things tolerate major version bumps better than others.
And so, like, like, you know, I think my interpretation of stable by default is to, you know, say that things that haven't changed in a long time are effectively stable at 1.0, and, you know, that doesn't block us from changing them so long as those components are, you know, going to have major version bombs sometime in their future. And I think the collector is one of these components that can tolerate major version bombs.
**Arthur Silva Sens** 43:34 it's been 5 years without a 1.0.
**Jack Berg** 43:38 And it's a culture thing.
Like, we have to, you know, it hasn't gotten to 1.0 because we're so scared of, like, making breaking changes, but if we adjust the expectation to say, like, hey, like, things don't have to be perfect on 1.0, we just need to be clear and communicative about when and how we're going to break things.
And, like, we bring things when we have major version bumps. That's what SEMVR is for.
**Arthur Silva Sens** 44:06 Alright, so as long as we, like.
We built a plan on how, like, explain to the end user why this breaking change is necessary.
Write blog posts, or whatever kind of communications we need to do.
To, like, make people aware, then we are, we are, allowed to do this braking change, and then finally comply to the spec.
**Jack Berg** 44:33 Yeah, like, look, if the collector… if the collector comes up with some sort of release cadence for major versions, maybe it's, like, once every three years, maybe it's once every 1 year, I'm not sure. I'm not gonna… I'm not gonna, like, have an opinion on that. But they could, you know, when they release a 1.0, they could sketch out their ideas for breaking changes in 2.0. So there's, like, more than a year of time, ahead of time, planning, to say, like, hey, look, this is what's happening in 2.0, prepare yourself.
**Arthur Silva Sens** 45:06 It makes sense.
**jmacdonald** 45:09 I very much like that proposal, Jack.
I think there's much… there's a lot of fear of leaving your 1.x, like, we can't even get to 1.x, but once we're stuck on 1.x, we're never leaving because of the wide user impact. And I… I think that that… tendency kind of, like, reinforces itself, and now we're really scared of changing from 1.x in various places, including your Java case. I look at the Rust ecosystem, and it's pretty different. Like, Arrow is on version 50, 55 right now. It's not bad. That's a data point.
Ted.
**Ted Young** 45:44 Yeah, I think, you know, part of the… concern we've traditionally had is that, you know, we do have a couple of places where issuing a 2.0 just from a dependency management perspective would really screw things up for people. But those are, like, very specific places, right? Like, the API packages are the number one thing.
That comes to mind. So maybe part of being able to loosen up in other areas, because there are definitely plenty of other areas where there just isn't that big of a deal.
with releasing a 2.0, 3.0 relatively quickly. But having, like, some places where it's fine to do that and other places where it's not fine to do that is confusing, so maybe… doing a pass at being explicit around, like, what really are the places where we really, really have to be careful about this. You know, Jack, you mentioned tribal knowledge in the past, and I feel like This is an example of that. Like, we have written this down, maybe in the spec in one or two places, but maybe that's something we can do, is just make it super clear what are the places where this actually creates a dependency management problem versus the places where we just want to be respectful of our end users.
**Josh Suereth** 47:08 Yeah, I'm probably beating a dead horse at this point, but I just want to agree, like, this cultural thing needs to get fixed. Like, we have had successful 2.Xs already in OpenTelemetry, right? I think the Java agent went 2.x.
The… I don't know if you're gonna say this, Daniel, but the Node, OpenTelemetry.js had a 2.x of the SDK, and that was widely… like, I… as far as I know, that was considered widely successful. I consider it widely successful. I think we… We need to get over the fear and uncertainty and doubt of a 1.0, and we need to commit to keeping things stable for users, and yeah, that means that your architecture might not be perfect, but it's fine, because we do have the ability to pull 2.0s. I will caveat the protocol is one of those areas that I think is a little bit more sensitive.
And even there, we are talking about a 2.X at some point.
It might be 5 years, it might be 10 years, but I think that it could be coming, right? So, let's, do the right thing for users, I think is the TLDR.
**Jack Berg** 48:13 And if I could just jump in real quick before Daniel. So, on the Java agent having a 2.0, I think one of the reasons that that has been successful is because the Java agent has committed to maintaining N-1. So, it releases patches.
for its 1.X version while it has a 2.x. And Trask, if I'm saying anything out of turn, please correct me here, but if one day when there's a.
**Trask Stalnaker** 48:43 We only did that for one year.
**Jack Berg** 48:46 For one year, right, but that was a stated policy ahead of time, right? So that was good, right? Users knew, kind of, what they were getting and what their time horizon was for updating.
And when there's a 3.x of the Java agent, presumably, Trask, and again, correct me if I'm talking out of turn, there will be, you know, patch updates for 2.x.
you know, for one year as well. So just, like, being communicative up front and continuing to release the prior major version for some documented period of time is what helps this actually land.
**Daniel Dyla (Dynatrace)** 49:20 I was indeed going to bring up the JS 2.0, and actually, we have a 3.0 coming up in a couple of months here. The 2.0 was wildly successful from my perspective.
For a couple of reasons, but one of the most important is that if you never… if you never bump your major version, it becomes… Like, if you never go to 1.0, if you don't start declaring stuff stable, things become… Like, de facto stable in this weird, like, halfway state where your users can never really completely… understand what is going to change when, and if you change anything, everyone gets mad. And you say, like, oh, it was zeroed out whatever, like, we said it was unstable, but, like, it's been unstable for 5 years.
people started relying on the behavior. If you go to 1.0, and then go to 2.0, and then go to 3.0, when you change those things, you're telling your users, this is the one where things are changing, and… It provided a lot of clarity. We get… we get less complaints… got less complaints about the 2.0 release than we did about the 1.0 release.
Which, yeah, a little bit paradoxically, in my opinion, but it made things a lot easier to change once we started stabilizing them.
**Arthur Silva Sens** 50:54 Just… just as point of order, neither I or Josh or David Edgeball are collector maintainers. We are all approvers, and we have some say in there, but, like.
just the discussion here is already… give us a good material that we can bring back to the maintainers and start discussing this, so thank you very much.
**Jack Berg** 51:16 Yeah, and, you know, I think one thing that I would say is, like, if it would be useful, we could bring the collector maintainers to have a conversation in this call, or if we wanted, we could have the collector maintainers have a one-off call with the TC as well. Like, let's talk this through, let's reach a resolution here.
**jmacdonald** 51:51 Well, thank you all for this conversation about stable by default. I know Austin, was interested in that, and he wasn't here, but he can probably catch the conversation, and we'll keep that one going.
I'm not sure there was an agenda after this.
**Jack Berg** 52:06 Carlos added a late item, so.
**Carlos Alberto Cortez** 52:10 Yeah, correct. This is mostly from the Kotlin, SIG, that is a new SIG, as you… in case people know about this one.
So, this is mostly a mobile thing, and because of that, some choices some of the centuries have been made differently. And one of the important things is that now they think that logging is in a good state there, and they're trying to, you know, just to check everything is great. And one of the interesting things is that, they have the API package, which defines all interfaces, but there's no… there's no… no AWP implementation. And I think that most of the SIGs actually have that.
And I wanted to double-check here, because I think I would rather prefer myself, probably, to keep that no op implementation in the API package. But I do remember somebody, it was probably Daniel Dyla, or somebody else mentioning that Something about the problem with that. Maybe I'm confused.
Also, I'm, like, pointing to the actual, document in the specification about how no op should look like.
So, and one thing that the maintainers there want to know is, like, whether this makes sense, you know? To have the API package that has all interfaces.
Which, of course, instrumentation and end users would use. But then, when you are actually using your application, then you just bring either the SDK or the no-op package, which implements this.
**Liudmila Molkova** 53:44 Carlos, did I understand it correctly, that they would like Just the API?
**Carlos Alberto Cortez** 53:51 I did.
**Liudmila Molkova** 53:52 just pure interfaces for the API.
**Carlos Alberto Cortez** 53:55 That's correct, yes.
**Liudmila Molkova** 53:57 What would happen if user didn't bring?
anything. Like, if it's a native instrumentation, how one would do native instrumentation, how would it behave in runtime an application that doesn't bring any implementation?
**Carlos Alberto Cortez** 54:10 Yeah, that's a good point. In that case.
they would have to bring the knot up, which is a problem, of course.
**Jack Berg** 54:18 Well, the native instrumentation would have to have a default dependency on the NOAP in order to avoid breaking its own users, you know, because the UX of saying, like, hey, you have to depend on this library, and in addition to it, you always have to place a dependency on either the OpenTelemetry NOP or the OpenTelemetry SDK. I think that would be a hard sell for any library looking to natively instrument with OpenTelemetry.
**Ted Young** 54:49 Yeah, the purpose of the no-op was to make sure the API was safe, essentially.
Right, so you don't… the default isn't your stuff blows up the moment you run into an API call.
It just doesn't do anything.
**Carlos Alberto Cortez** 55:06 Yeah, and I think that for you… in that regard, I think that it's kind of easy to work around that when you have an a final, like, an end-user application, but for the native instrumentation. I don't know how often that happens in the mobile space, but I would rather stick to the safe spot, you know?
**Liudmila Molkova** 55:23 It's a philosophy, I think, right? That our choice is that your API should do nothing, but it should be self-sufficient.
**Josh Suereth** 55:38 Doesn't… doesn't the API… doesn't context propagation happen, in the NOAP API?
**Carlos Alberto Cortez** 55:46 Right, that, yeah, that could be the only thing that, if Kotlin goes this way.
That would be the only thing that would have to be implemented there.
**Josh Suereth** 55:54 Right, because if I remember right, Context doesn't have a no-op API.
And so, if you have instrumentation, like, the context propagations still occur, you just won't make traces.
**Jack Berg** 56:08 So, Carlos, I would probably actually flip this on the head for the Kotlin maintainers. So, you know, you know, they're asking, can we do this? And, you know, I think the burden of proof is on them to say, like, why they want to do this. Because, like, as it stands right now, virtually all of the, you know, the language implementations bundle and no op with the API, And so choosing to not do that is, like, squarely going against the grain. You need to have a really good reason to do that.
**Ted Young** 56:38 Yeah, I would wonder, like, what's the big deal about just… just including a no-op, right? It shouldn't itself require any dependencies or anything, it's pretty simple.
**Carlos Alberto Cortez** 56:50 Yep.
Okay, I think the feeling is that, yeah, it's a bad idea. Okay, I will bring that back to the code maintainers.
Sweet.
In that case, that's all from my side. Thank you so much.
**David Ashpole** 57:10 And let's check the agenda again, I think.
We managed to fill up 55 of 60 minutes. Good job.
With that, thank you everyone for joining, and I'll see you guys next week.
**Jack Berg** 57:22 Dear.
