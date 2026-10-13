SIG: Policies SIG
Date: 2026-10-12
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Josh Suereth (Google LLC)** 01:39 Hey.
**Jack Shirazi** 01:43 Hiya.
**Josh Suereth (Google LLC)** 01:44 How's it going?
**Jack Shirazi** 01:46 Yeah, good.
You finally got the, the calendar invite.
**Josh Suereth (Google LLC)** 01:54 I did not get the calendar invite. I added myself to the group, and I was gonna go debug what's up with the calendar invite.
Yeah.
It is October 12th, so I'm gonna make a new… Thing for us here.
Jacob is out, by the way, so… The date.
**Jack Shirazi** 02:37 I have no idea why.
My faces have partly blurred.
**Josh Suereth (Google LLC)** 02:43 I think Zoom just wanted to keep you anonymous.
**Jack Shirazi** 02:46 Yeah.
**Josh Suereth (Google LLC)** 02:48 you All right.
I wonder how many people are going to join. How many did you. I watched last time, by the way.
So, I was trying to get caught up.
**Jack Shirazi** 03:03 I think the attendees are listed there. I think that's how many were pretty much.
**Josh Suereth (Google LLC)** 03:07 Yeah, so that was, that was accurate. 1, 2, 3, 4, 5, okay.
Cool.
Oh…
**Jack Shirazi** 03:37 Well, I'm guessing… We may be the only ones.
**Josh Suereth (Google LLC)** 03:45 Okay.
I'm gonna grab a few of my thoughts, and I think we can talk with just the two of us, and then call it quickly. Sure.
Give me one second, though, just responding to two things.
I wasn't expecting to, like, be the person running the meeting today.
We're, like, trying to coordinate, yeah.
Ugh.
Okay, let's see… Don't think I have any useful links.
I was gonna go through… I know Jacob's still working on things, but you guys had a really good discussion last time.
And I have, I took notes.
of your discussion, and then I had AI go through and listen to everything, and make notes of, like, what are the questions that we need to answer? Because when I look at these notes here, right?
Let me make this a little bigger.
there's this listed, but there were a bunch of good questions that you had, and I am trying to find where I put my notes.
**Jack Shirazi** 05:17 Well, after the, last week, I updated the, the issue itself.
The PR, rather.
**Josh Suereth (Google LLC)** 05:27 Okay.
**Jack Shirazi** 05:28 whether I think there's two, two updates.
explaining… The last… the long list of changes that are needed to, to accommodate… SDK stuff, yeah, there's that one and the one before that.
**Josh Suereth (Google LLC)** 05:48 Okay.
**Jack Shirazi** 05:50 So the thing is that in its current form, This is very much a These are all the policies that the collector can do really nicely, and you can take… we can take out YAML from collector and put it into a policy, and it matches one-to-one, and it cleans up the collector YAML really nicely, because We can have telemetry policies do it instead, and externally specified.
But it's completely unsuitable for the SDKs.
Which have a very different set of… Requirements, desires, so, like.
all of the things that are in the, in the PR at the moment.
Sure, I mean, that's fine for the SCK, they can do these filterings, these droppings, but nobody cares about that.
For SDKs, for the most part.
You don't want to do that dynamically. They are used, but they're used statically. So that sort of config is really done statically in SDKs, and they're not the sort of things that people want to change. What they do want to change are the things that I've listed here.
And the actual… specification in the PR, Can't do any of these.
**Josh Suereth (Google LLC)** 07:16 Yes, but that was intentional. So two things I want to say. So one is, I want us to design for the future, not for where we are now, if we can.
If we think that that's going to be reasonable. So… I agree with you that this, like, this turning individual instrumentation on and off, to me, is, like, number one for SDK.
trace sampling percentage is actually number one, overall. That was actually where the idea for Policies first came, where I was talking to.
to folks about this was, you know how we have Jaeger remote sampling? Yep. And we have that in the collector, and there's no, like, OTEL equivalent. Well, it's like, what is the OTEL equivalent of that applied across everything?
So, I agree with you that we need to make sure, like, things work, but I also think, in the future, it might be that users don't care where a policy happens, just that it does. So there are things that people rely on the collector doing, and things that, that, that.
People don't apply to, like, an SDK, partly because it's not practical, like, you can't do it today.
But if we get to a point where, say, some of these filtering capabilities actually make sense in a SDK, is it more efficient to do it in the SDK level than at the collector level?
And I think if the answer is yes, we should push it all the way up there.
Right? So some of these filter drop things we do in a collector, because that is currently the component that is.
Owned by, like, you know, the observability person, or the SRE.
And the SDK isn't, and the SDK is usually hard-coded configuration. If you change that configuration, you break the whole project from running, so it's risky to do it there.
But in the future, if actually we could do it efficiently.
If we could do it safely, if we could do it the same way as, like, changing sampling configuration.
maybe people would actually want to do it there, too, if it's actually better for the health of their system. Now, I'm not saying it is or isn't, right? I'm saying… I just want to, like, leave that open. So… when you say, like, this doesn't work at all for SDKs, I think we have to address that. Like, I think we have to get this to the point where it… we can take these policies and enforce them various places efficiently, and I'd love to make sure At least, in the long run.
that we cover things in an SDK. And I think, like, you're 100% right in, like, saying, here are things we have to do in an SDK. I remember that Jacob and, David and folks were talking about, starting with the collector first, and a set of collector use cases.
My question to you, Jack, is do you think… that is reasonable. To, like, what if we start with the collector and move into the SDK, or if we start with the collector, we would never be able to do SDK things.
**Jack Shirazi** 10:11 It's okay. The OTEP structure.
Yeah. The definition of telemetry policies in the OTEP was Wider.
And it allowed for the SDKs to do all of these things.
And this current PR narrows the scope enormously.
And prevents you being able to do it in the SDKs.
Because it's missing policy definitions that you just are unable to do these kinds of things in an SDK.
Yeah. When… when… although the… overall project, suggest, you know, description. It was saying, let's do it in the collector first.
It's kind of… that's behind the mark, because this has already been implemented in the Java SDK. It's already being implemented in the Python, the .NET, and… The node SDKs.
So saying let's do the collector first is nice in principle.
But it's wrong in practice, and having this PR actually sets us back rather than forward. So, because we've narrowed the scope from the OTEP, and we've narrowed it to essentially what the collectors can do, and said, well, we're not going to do what the SDK can do.
We've kind of said, okay, all the stuff that's in progress by all the SDKs is no…
**Josh Suereth (Google LLC)** 11:42 I think what we need to do, then, is divide and conquer, right? So, like…
**Jack Shirazi** 11:46 Yeah, sure.
**Josh Suereth (Google LLC)** 11:47 Yeah. So so I I'm I'm on board with that. One of the things that I wasn't there for last time, and I know David, I don't know how, David and I both work at Google together on, like, this kind of thing. But my my assumption on my role here was actually gonna be the bridge between the collector and the SDK.
For context, I was pushing SDK-related things earlier. That's one of the reasons the OTEP has SDK-related things, and I'm really happy to see all the work you've done, particularly on, like, SDK stuff.
But maybe what we do is divide and conquer, where we take this initial PR and we kind of split it, and have a collector-focused area and an SDK-focused area. But the thing I really want to walk through with what you have here is what… What can we share between the two that makes sense? Like, I do want trace sampling to be something that is, very clearly could be done both places if needed.
**Jack Shirazi** 12:43 So, the trace sampling is, the policy that's defined for the trace sampling.
is workable, because the SDK… in the SDK, because the SDK could just ignore the things that it can't do, the attributes.
So you could just ignore that.
But… Fundamentally, the policy is defined for a late sampling decision and not an early sampling decision, and that's the big difference between the collector and the SDK.
**David Ashpole (Google LLC)** 13:15 What do you mean?
So, if I can speak for a minute, I think.
**Josh Suereth (Google LLC)** 13:19 Good.
**David Ashpole (Google LLC)** 13:21 My hope was actually to focus on the things.
That could be implemented in both the SDK and the collector first.
Because if we can get those written out.
Then it's much easier for us to split into two groups and extend, like.
The core patterns and stuff that we all think are gonna work, like, it's hard if we go and build 2 different types of things.
That have different patterns and different, like, feels to them.
But, like, if we can all agree on what a filter looks like… Then it's way easier for us to say, oh, okay, and this is how we'll define.
This thing in this other specific domain.
That was… that was more my thought, was, like.
I want to make sure that the policies that are more collector-focused and the policies that are more SDK-focused are You know, are, like, kind of… Fruit of the same tree.
**Jack Shirazi** 14:14 Just going back to that, why exactly are we defining policies when the OTEP said we wouldn't define policies?
**David Ashpole (Google LLC)** 14:23 Did you separate?
**Josh Suereth (Google LLC)** 14:24 The OTEP wasn't going to define policies. The OTEP was like, here's what a policy is and how policies will work with the idea being that this work stream now defines policies that we all agree to and make consistent between all the different components.
**David Ashpole (Google LLC)** 14:41 Yeah, I don't think we can have, like.
The universality that we want from policies, if it's… everybody writes their own thing for their own component.
It's like, the… one of the… like, for me, one of the most important bits is that I can take a policy and give it to OB, or I can take a policy and give it to the collector or to an SDK, and it all does the same thing.
**Josh Suereth (Google LLC)** 15:06 Yeah.
we want to be less… we want to be pretty resilient to your topology, if possible. So, like, let's say… another thing is we're starting to work with Prometheus more, right? If a Prometheus client library supports policy, great! We can push a policy straight to it, it's not even on OTEL, but it does the thing that we want.
**Jack Shirazi** 15:26 this.
**Josh Suereth (Google LLC)** 15:26 Push it, yeah.
**Jack Shirazi** 15:28 I mean, it was very clear at the OTEP and still clear here that if it doesn't understand the policy, it just ignores it.
**Josh Suereth (Google LLC)** 15:37 Yeah.
**Jack Shirazi** 15:38 It's, it's… I don't see a problem with us defining generic… implementations rather than specifying… I don't… I liked the OTEP, I thought it worked really well, and it was fine that we could implement policies, and then components that didn't understand it.
We're not… just not going to implement it.
If we're going down the road that we're going to specify all policies.
It's going to slow down development enormously.
**Josh Suereth (Google LLC)** 16:10 I see what you're saying. Okay, so I would argue two things here. One is, we want to try to share some universal policies that we should specify together. But policies are designed around open extension. So, like, anyone should be able to define a policy and start shipping it.
But…
**Jack Shirazi** 16:25 Okay, that's not, that's not what this PR says.
**Josh Suereth (Google LLC)** 16:29 Then… then we should probably fix that?
**David Ashpole (Google LLC)** 16:34 the.
**Josh Suereth (Google LLC)** 16:36 Oh, oh, so here's another thing, where this PR lives, right? This PR is in, is in OpenTelemetry Proto, and so I think there's a few things that we want policies to share overall, and then we want to figure out where extension is. So…
**David Ashpole (Google LLC)** 16:51 I think that there was at one point an ask for like a container, like a policy set. Like I think if we had that definition and it was extensible.
Then it would allow for what you're interested in.
**Josh Suereth (Google LLC)** 17:04 Like, there's some generic things to go on to that. There's some generic things around policies that we probably want to have of, like, you know, is a policy applied or not? Like, every component, if I can find a way to advertise, I ignore this policy.
Then it makes the whole system a little more resilient because you can have self observability data, right, of, like, I'm ignoring these sets of policies that I don't understand that you sent to me.
So that a controller coordinator system.
knows that you're ignoring policies. So, I would, you know, say I'm ignoring policy by name or something, or I have some way of rejecting the policy that's communicated. I don't really have to care what's in the policy if I don't know it, I just need to have a common way of telling you I'm not applying it.
Right? So the container, I think, is important, but you're right, like, there's probably some language in here we can… We can push on.
I do want to go through your comment more because I think you had a lot of really good points about things in SDKs we have to think through.
Umm.
**David Ashpole (Google LLC)** 18:19 And… Like, I do think we need… A spec somewhere before we can start defining policies.
Just because Even if we wanted them to be super extensible, I think we need to take all the, like, more high-level Things that the OTEP said and actually write them down as.
You know, normative language that we can all make sure that we stick to so that we Even when we're designing in parallel, we can… Like, design similar… similar behaving things.
**Josh Suereth (Google LLC)** 18:50 Yeah.
**Jack Shirazi** 18:52 I mean, that's where I thought we were gonna start.
at that higher level, where we would take the OTEP and Make that specification, and then start implementing or specifying policies Based on that, so these… this is the spec, but these are the optional policies that we think everybody should have, and then you can add policies beyond that.
But that's not what this PR says. This PR says, these are the policies, and that's it.
And if you.
**Josh Suereth (Google LLC)** 19:20 Yeah.
**Jack Shirazi** 19:20 You're stuffed.
**David Ashpole (Google LLC)** 19:23 Great.
Some of the things, yeah.
**Josh Suereth (Google LLC)** 19:25 Go ahead, David.
**David Ashpole (Google LLC)** 19:27 I think some of this is the stuff that we want and so then some of this is a bit more specific to the exact policies that we're defining in the ProtoRepo.
So I think there's a mixture of both here.
**Josh Suereth (Google LLC)** 19:40 Yeah.
I do think, like, to me, this is kind of some of the most important set of this, right? Of, like, this notion of a policy has a structure to it, some baseline structure.
There's a notion of maybe a set of policies that you're applying that we give as a label or that every policy has an ID. This is the other thing I think is super important. We have an ID and then we have this notion of matching of like, where does the policy apply?
And you had a few things in your comment, Jack, that I like of, like, well, maybe matching is, like, on a component. Or maybe, like, I think the matching is one of the things we kinda have to figure out.
But then the actual policy of like what you do, I don't think it's supposed to be hard-coded here.
Into, like, these are the only three, it's just, like, these were the first three that Jacob is proposing.
Yeah. And, like, this notion of how we select, like, fields and things, there's this interesting… There's an interesting question in my mind, you know, related to this.
of scope attribute and instrumentation scope, and then the actual, like, turning on and off instrumentation in an SDK. We have this weird thing where, in the collector, right, you have instrumentation scope, which is supposed to be your proxy for instrumentation itself being turned on and off.
And in the SDK, you have the instrumentation, which is the actual meter or logger or whatever. And so if I'm targeting policy in the SDK, I'm targeting technically instrumentation scope. Right?
But the way I do that between those two is very different. And so how do we bridge that gap?
And…
**Jack Shirazi** 21:29 Just to be clear, there is instrumentation scope in the SDK as well.
**Josh Suereth (Google LLC)** 21:34 Yes, yeah.
But the… the rollout of instrumentation scope in SDK is at various levels of sophistication, depending on which SDK you're in. Correct. And so, if we have a generic instrumentation scope targeter, we might not actually work in some SDKs, and I think that's okay. You know, we'll get around that, but…
**Jack Shirazi** 21:55 But the likelihood is that if you want to Enable disabled instrumentations in the SDK.
You will need instrumentation scope to do that. The SDKs that don't have instrumentation scope will not be able to handle those telemetry policies until they've implemented it. So I don't think it's a problem saying instrumentation scope generically.
**Josh Suereth (Google LLC)** 22:17 Okay.
Then, yeah, we can also make that be a requirement for interactive policy and encouragement for folks to implement instrumentation scope correctly.
Okay, but, like, in my mind, the important part of this PR is this, like, the, the field selection, the overall policy structure, like, rules about how we can apply these to various components. That's the thing I want us to spend a ton of time on. The actual, like, which policies… you know, the fact that this is filter, transform, metric, filter, and trace sampling.
This should be SDK friendly if it's going to exist. These should also be SDK friendly if they're going to exist.
And the, yeah, just filter…
**Jack Shirazi** 23:04 clear.
**Josh Suereth (Google LLC)** 23:04 Where to apply them is the thing that I'm worried about, yeah.
**Jack Shirazi** 23:07 Yeah, to be clear, the SDK can do all these. That's not the pro… that's not my issue. It's not that these are unfriendly to SDKs. The SDKs can do that, but that's not the policies that people want to do in an SDK.
That… so these are… they're implementable fairly straightforwardly in the SDK.
But nobody cares about them.
**Josh Suereth (Google LLC)** 23:30 Right, we need a different set. Go ahead.
**David Ashpole (Google LLC)** 23:32 So it's like people want to be able to turn off stuff, right? And this, like a filter policy would let you turn things off more.
**Jack Shirazi** 23:39 Yes, I mean, the list I put in my comment.
**Josh Suereth (Google LLC)** 23:43 We're driving…
**Jack Shirazi** 23:44 everyone's Do we need some…
**David Ashpole (Google LLC)** 23:47 That's like.
**Jack Shirazi** 23:47 the.
**David Ashpole (Google LLC)** 23:48 An inverse of a filter, like an enabler policy.
**Jack Shirazi** 23:53 you.
**Josh Suereth (Google LLC)** 23:57 So changing the sampling percentage, this should be… the current sampling policy that we have should line up with this, and I think we just need to update the sampling policy for that. But yeah, this is the notion of turning an instrumentation on and off.
So the question here, David, would be, like.
I is is filtering something off the same as enabling instrumentation?
**David Ashpole (Google LLC)** 24:20 I… well… It's not the same, or if we did, we would have to rename it from filter policy, because I don't… I think it sounds weird to have a filter policy that turns things on.
**Josh Suereth (Google LLC)** 24:30 Yeah.
**David Ashpole (Google LLC)** 24:31 I think… I think conceptually targeting a piece of telemetry.
And turning it on.
Feels very, like, structurally similar to targeting a piece of telemetry and turning it off.
So, like, I might want the two to look similar.
If we were designing them both together.
Rather than say have like an HTTP instrumentation policy or something.
That allowed you to specifically tune HTTP related.
Instrumentation stuff, right?
**Josh Suereth (Google LLC)** 25:08 This is something I do think I would want very soon as well, because this is the most important thing for like SDKs and OB, right?
**David Ashpole (Google LLC)** 25:18 you.
**Josh Suereth (Google LLC)** 25:19 Turn stuff on and off.
Yeah.
So, if we think this is a different policy, And because we have enough people in the SIG, I… and with all the work on the SDKs, I think we should add this in scope for sure.
But we should also just make sure that the… We should make sure the PR doesn't make it seem like these are the only policies that will ever exist for all time.
**David Ashpole (Google LLC)** 25:46 Yeah, yeah, right. That's for sure. I definitely view this as like, Step zero.
Is… if we can define a policy.
And try and implement it in a few places.
**Jack Shirazi** 25:58 Saying that this is…
**David Ashpole (Google LLC)** 25:59 We messed up.
**Jack Shirazi** 26:00 Are we saying that this is an enablement policy? Yeah. If we're going generically.
**David Ashpole (Google LLC)** 26:06 I think that would make sense.
**Josh Suereth (Google LLC)** 26:07 I like that word. Yeah. Because I think an enablement policy makes sense for instrumentation on the SDK, in OB, even the collector has things that it can enable.
**David Ashpole (Google LLC)** 26:17 Receivers, yeah.
**Josh Suereth (Google LLC)** 26:18 Yeah, the different receivers like I can turn on and off syslog for example, you know.
**Jack Shirazi** 26:22 More likely for the SDK, it's a disablement policy, but it shouldn't matter which way.
**David Ashpole (Google LLC)** 26:28 Isn't that just a filter, or…
**Jack Shirazi** 26:31 Well, it's like, if you look at the, the, the… not the next bullet point, but the one after, I point out the logging of the SCC logging level. It's not a filter, because… There's conceptually a difference there between Turning on… starting the agent with debugging on, and then filtering out all the debug logs, versus switching it to debug.
**David Ashpole (Google LLC)** 26:57 Maybe filter policy is just the wrong word, because what we… What we really and I think filter is just, like, conceptually simple, which means like, we want a policy that means I don't want this thing.
Right? But… Whether it's called filter or disable, It's… The end result is the same, which is someone doesn't want a thing, right?
**Josh Suereth (Google LLC)** 27:22 Another way to phrase this, Jack, is if I have a filter policy that is targeted appropriately broadly, I should be able to have is enabled return false on the logger, for example.
**David Ashpole (Google LLC)** 27:34 Exactly.
**Josh Suereth (Google LLC)** 27:35 Right? So that I'm not paying the cost of the instrumentation.
**Jack Shirazi** 27:45 So… Yeah, it's definitely not filtering.
**Josh Suereth (Google LLC)** 27:48 Well, I mean, you… from conceptually, you could call it filtering, but it's like, okay, if I can optimize the filter to say, I don't even have to make the log to begin with.
You know, like, what's the difference there?
**Jack Shirazi** 28:04 Okay.
**David Ashpole (Google LLC)** 28:05 Right.
**Josh Suereth (Google LLC)** 28:08 So that that's that's the like, if we wanna make a hard diff between generation and filtering.
in policies, we can, but I think our, like, when I was talking to Jacob and David and folks before, one of the things with the SDK was, like, okay, if we get this right.
and we can optimize these things in the SDK, we could have it so that if you filter something so that you're dropping everything, just disable it to begin with, so the SDK doesn't even do the work, because then you're more efficient, it's more optimal, right?
**Jack Shirazi** 28:41 Okay, I mean, I don't have a problem with saying that disabling is the same as filtering, just more optimally done. That's fine. In which case, that would cover, turning instrumentations off, turning exporters off.
I'm not entirely sure how it would cover the logging level, because when you set the logging level, it's, like, it's an enum, and you're actually setting it to… a specific… so, I'm not sure if the filter covers that.
**Josh Suereth (Google LLC)** 29:10 Yeah, this one's fun because it's not just that it's an enum, it's that it's like a escalating level of enum where every.
**Jack Shirazi** 29:18 exactly.
**Josh Suereth (Google LLC)** 29:18 Enuma covers the thing below it. Yeah.
**Jack Shirazi** 29:20 Yeah.
**Josh Suereth (Google LLC)** 29:21 Yeah, so log level might… go ahead, David.
**David Ashpole (Google LLC)** 29:25 It's like, I can see how… A log level configuration option could be turned into two policies, right? One enabler policy and one filter policy.
Right? To make sure that all the stuff above a level is turned on, and all the stuff below is turned off.
Whether that's… a useful UX for users.
Is maybe more debatable?
Right? But it's like, if someone says, I want only fatal errors, or like, I want only, like, the fatal log level.
Then that's equivalent to a filter policy for everything Aaron below.
And if somebody says, I want to enable debug logs.
That means that they want all the regular ones plus debug enabled as well, right?
I guess the only weird thing is you would never say, I want to filter out only the info logs and leave the rest of them, right? Like, that…
**Josh Suereth (Google LLC)** 30:25 Yeah.
**David Ashpole (Google LLC)** 30:26 It's… it's like… It's a greater than or less than, not like a.
**Jack Shirazi** 30:31 I kind of feel like this is turning something that's actually very simple and consistent across the whole of IT into something that's complex.
**Josh Suereth (Google LLC)** 30:39 Yeah, I do think just having a diagnostic log level policy would make sense. That's targeted, right? So it has the same matchers, it has the same scope level, all that kind of junk, and you get a diagnostic log level that hits your logger.
That… that seems tot… like, so my proposal, based on what we have here, is I actually think the diagnostic log level should be added.
Instrumentation enabled's another fun one, where I think the notion of enabling instrumentation should be added. The notion of filtering stuff out, we want to make sure filter is generic enough that you can, Make it optimal.
**David Ashpole (Google LLC)** 31:14 I would like if a collector could implement.
See, it's interesting, because, like, you can't… If a collector gets a log level policy.
I guess it can just filter out things that are below the desired log level, right?
**Josh Suereth (Google LLC)** 31:30 Yeah.
**David Ashpole (Google LLC)** 31:30 It gets a log level policy that says.
Info logs only for this application.
then it could do that filter, but it obviously can't turn on logs in the same way that an SDK could.
**Josh Suereth (Google LLC)** 31:44 I actually have to drop, I thought this was… is this only 30 minutes?
**David Ashpole (Google LLC)** 31:47 only.
**Josh Suereth (Google LLC)** 31:48 Okay. Two things I want to add. This notion of changing HTTP routes to ignore when creating traces.
So, Jack, the… I might be stale, because I'm used to using Jaeger Remote Sampler, but I thought that was part of your sampling policy, where you would basically say, like, I want a specialized sampling policy that includes a route target that says sample this at zero.
Am I thinking of that wrong, or not?
**Jack Shirazi** 32:16 That's… it's not a standard thing in any SDK.
It is… has become an optional A sampler that you can specify, just recently.
So, it's part of the…
**Josh Suereth (Google LLC)** 32:30 Your remote sampler was added to the spec like two years ago, but it's no.
**Jack Shirazi** 32:35 Not the yoga sampraday, consistent I can't remember exactly what it's called.
**Josh Suereth (Google LLC)** 32:39 Oh, the new one from Josh and folks. Yeah, the Sam Fitz. Gotcha. Yeah.
**Jack Shirazi** 32:45 Okay.
But that can't… that's only static, so that can't be defined domainic, but that… I think that one… filtering works fine for that one, but for the next one, changing which methods to instrument.
That is not a filter. There's no way you can define that as a filter, because the filter would be every single method, and then you'd have to define every method that's not instrumented, which is insane, so…
**Josh Suereth (Google LLC)** 33:11 Yeah, this gets into the enabling disabling instrumentation and it's like a special case of it or a more intense one.
**David Ashpole (Google LLC)** 33:19 I think… Conceptually, like, I'd love to start with maybe enabler-disabler policies, or, you know, filter-enabler policies, however you want to call them.
And then… Try and collect the important gaps.
And figure out what… What needs to be its own thing and kind of try and work that way. I'm not sure if that… Makes any sense to you, Jack, or if…
**Jack Shirazi** 33:44 Sure.
**David Ashpole (Google LLC)** 33:44 Other ideas. Like, I'm definitely… Right, I'm definitely happy with an enabler policy, I think, if that's… it sounds like that's especially an important thing for SDKs.
I feel.
**Josh Suereth (Google LLC)** 33:55 You might also want to do this diagnostic log level one, too.
**David Ashpole (Google LLC)** 33:59 Yeah.
Okay.
**Josh Suereth (Google LLC)** 34:01 I'm still thinking about that. So, so, like.
But I think I… I have 5 seconds before I have to drop. So, I think for me, the next steps would be, Jack, I want to go through all your feedback, like, with what David's saying, and look for gaps in what we have.
And then call out, is there a new, unique policy that's truly unique, or do we need to make changes to existing ones? We should prefer taking existing ones and making them as general as we can, and reusable across components.
But I think you have a few things that are truly, like, actually new policies that should be included in the initial set, because they're just common things everyone wants to do.
You know, like, the first set should be the most common things everyone will need.
That we already know from implementing stuff, so… Yeah, cool.
Hey, great discussion, sorry I missed the last time, and
**Jack Shirazi** 34:50 Good meeting.
**Josh Suereth (Google LLC)** 34:51 Yeah, look forward to chatting with you all again in two weeks.
**David Ashpole (Google LLC)** 34:55 Thanks, Jack.
**Jack Shirazi** 34:56 Cheers, bye.
