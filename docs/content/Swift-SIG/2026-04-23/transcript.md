SIG: Swift SIG
Date: 2026-04-23
Duration: 52 minutes
============================================================

## Zoom Recording Transcript

**Billy Zhou** 01:17 Hey, Bryce.
**Bryce Buchanan** 01:18 Hey, how's it going? How you doing, Billy?
**Billy Zhou** 01:22 It's gone. Yeah, a lot of interesting stuff going on here. How's, how's your life?
**Bryce Buchanan** 01:30 It's been good.
**Billy Zhou** 01:31 Huh?
**Bryce Buchanan** 01:41 Can you still hear me?
**Billy Zhou** 01:43 Yeah, yeah, I can still hear it.
**Bryce Buchanan** 02:09 There we go.
Okay.
Well, I hope somebody else shows up. Oh, there's Nacho. And there's Vinod.
Because I don't know what's going on.
Hey, Binod, how you doing?
**Vinod Vydier** 05:00 Hey, Bryce.
Long time.
**Bryce Buchanan** 05:03 Yeah.
**Vinod Vydier** 05:08 Yeah, we were… Waiting for a lot of… Issues, too.
to discuss with you, I think, something that…
**Bryce Buchanan** 05:16 Oh, no!
**Vinod Vydier** 05:23 So you… everything good at your end?
**Bryce Buchanan** 05:26 Yeah, everything's going.
**nacho** 05:28 Hello again.
**Bryce Buchanan** 05:28 It's fine.
Hey, guys.
**nacho** 05:31 Yeah, nice to see you, Bryce.
**Bryce Buchanan** 05:33 Yeah, good to see you!
**Ari** 05:35 Hey, Holo.
Welcome back, boys.
**Bryce Buchanan** 05:38 Gary. Thank you.
How's it been?
**nacho** 05:47 quite steady?
Yeah, not much movement. I think some of the people that used to come to the meetings, I think that Yes, yes.
are not working at their companies. I'm gonna…
**Bryce Buchanan** 06:02 Dang.
**nacho** 06:03 Inc.
So I think… yeah.
**Bryce Buchanan** 06:06 Well, it's too bad.
**nacho** 06:09 Yeah.
And we… and I think last week.
Yeah, the meetings have been not with many people, and…
**Bryce Buchanan** 06:18 Yeah.
**nacho** 06:23 Okay So, yeah, I don't know what we can… I, I can…
**Bryce Buchanan** 06:35 Oops.
**nacho** 06:42 Yeah, I know why.
We lost everything.
Do you want me to share the document? Are we…
**Bryce Buchanan** 06:51 Yeah…
**nacho** 06:52 All of that?
**Bryce Buchanan** 06:53 I figured I'd let somebody else run the meeting, since I don't have any context of where we've been or what's been going on.
**nacho** 07:01 Okay, yeah.
Don't let me pair… Yeah, I have driven a bit late because I was in a meeting.
So I have not updated this document so far, but someone… Oh, this was from last week. I didn't.
This for today… You're watching… you're seeing my screen, right?
**Bryce Buchanan** 07:38 Yep.
**nacho** 07:40 Okay.
So, basically… Yeah. Last week, the last thing we did was, we released the core package.
Because it had a… Fix for, numeric issue with… with something, and… and it… we… we checked that it was building in the night list, and… and building correctly. So we should probably release, Mainly library, with that changes.
I don't know if, finally, Ari was able to test that properly in his end.
**Ari** 08:25 Yup.
I said it, I didn't have… any big problems, to be honest. Okay. So…
**nacho** 08:34 Yeah, so then we could probably just release that.
Cities?
And create a release with it.
**Ari** 08:42 I didn't do the release, because, you know, I left the other company, but I tested it out.
**nacho** 08:47 You lost all your permissions, okay.
So, okay, yeah.
But, yeah, so that, that, we should just release that. And for the rest, there has been some… some, we can track the PRs and the issues if you want.
We have not, toward the last… Yeah, we have been basically on that, talking about the span events that are getting deprecated. Bryce?
I don't know if you knew about that, but they are using just logs with their… with the linked spans.
**Bryce Buchanan** 09:34 Cool, that's cool that it's finally getting deprecated. I remember them talking about it, it's like, well, these are kind of useless now, but that's cool that they're finally… Getting rid of it.
**nacho** 09:46 Yeah, They don't need to have.
**Ari** 09:52 You also did, at some point in time.
the Events API PR. I don't know if you want to reopen that on… on… On the new repo?
**Bryce Buchanan** 10:04 the events API PR.
You just… do you just mean, like, the, the helper methods, or… Because the, I thought that… the, Kind of, like, the, the event builder stuff was kind of deprecated as well, because it's, it, you know, it's kind of not a side thing anymore.
Right? Was that… or is it something else?
**Ari** 10:39 Let me check… Which was?
**Bryce Buchanan** 10:45 Because, the event name got elevated to a, to a, Primary field, rather than just being an attribute, right?
And I'm not sure… I'm not sure what happened with the, What was it? The event… the other one.
Because there's the event name, and then the event type, maybe? Or event… I can't remember what that was.
**Ari** 11:15 Oh, no, I… Ayy.
I confused the entity proof of concept with the event CPI thing. My bad.
Probably my bad.
**Bryce Buchanan** 11:29 Oh, entity, right, right, okay. Oh, is that, is that picking up?
**Ari** 11:37 I don't know.
**Bryce Buchanan** 11:38 Oh, okay. Which I haven't…
**Ari** 11:40 Would you…
**Bryce Buchanan** 11:41 Removed.
**Ari** 11:41 To the… to the new…
**Bryce Buchanan** 11:43 Right, yeah, it's kind of an old, old PR that's been… that's stale. I can move that over.
**Vinod Vydier** 11:54 I think they'll… The blog… actually, I should, link that blog as well. It talks about, you know, basically using Log API.
Into the… span event.
API.
**nacho** 12:12 Okay.
**Bryce Buchanan** 12:14 Yeah, that's been… I think that's already been implemented.
**Vinod Vydier** 12:17 Okay.
**nacho** 12:22 Yeah, so do you want… do you think we… Okay, yeah, from Larry, that… and we have this, topic about the Swift version 6, PR.
Billy, you wrote it?
**Billy Zhou** 12:35 Yeah, so I'll, finish rebasing it, and then, there's just a failing Linux build, and then I'll raise it for, review, and then I'll send it to you guys for review.
Yeah, sorry, I've been kind of away a few months as well, but yeah, let's… let's get this out.
**nacho** 12:58 Yeah, so let's go with the other… PRs on the project?
For the core, we have the documentation here that has been open for a long time.
I think it was… also for… Millie?
Just a small change, and I think that… Would be done.
It's not urgent, but yeah. Regarding… yeah, they also created, someone created a, API for exporters, adding a single weight for them.
We've been… Yeah, providing some feedback here.
Yeah, basically, we asked to keep the same names for them, and to use the async in the method.
Yeah, basically… It's… I think now it's more ready for you.
Everything has been addressed.
So now it uses the same name, but you can tackle with the Wix or not.
But yeah, we should review if that… that really works now.
Yeah, there are many changes. Basically, changing to async, yeah.
Cool. And let's see if that's workable.
I think, yeah, having a single result will be good.
For… for error handling, much better than the current API that we had that had no callback and nothing like that. So, I mean, I think we… we… it was in the… in the… PIs that we propose people to take, and that… It looks good, I have not given it a full preview.
But… it… It starts to look, quite good.
Also, there was this about environment bar propagation.
For better answer that since what we have now.
No reviews so far.
then… I think that those are changes that are happening.
**Vinod Vydier** 15:18 This was the AI, this was the AI PR, right?
**nacho** 15:21 Not so… Yes, he said he had no experience, yeah.
**Vinod Vydier** 15:26 Okay.
**nacho** 15:27 Some of these things are, like…
**Vinod Vydier** 15:34 Or not this one, I think there was another one which was.
**nacho** 15:36 No, it was another one, yeah, I think so. Yeah, basically, it… it removes, the way it was just before, and how to do now.
yeah, I don't know if… that's, a good solution. I didn't agree with, so… The other… Fixed metrics, apply default view when no user view matches.
I think, yeah.
We can approve it to see if it runs or not.
but yeah, this has been new.
I've not seen this before.
for… Okay, UEM.
I think it's cool.
**Bryce Buchanan** 16:35 Is that correct, though?
I guess, I don't know what the default view is. I thought that it was not supposed to do anything if no view was available.
I'll have to take a look at that to… and review the spec.
Just to make sure.
**nacho** 16:59 Yeah, and the… yeah, yeah, and that sort.
For requests and issues, we have… Yeah, we have some old issues, like… The change to 2.0 here.
this was the… the… the issue we opened, the Ashenga weight for exporters that has been They don't fit.
And these… is the… the Running pot is speckling, from Ari.
The open also the issue.
And we have one about switch concurrency migration here. I have not answered anything.
Basically, they were asking where we are… we're going to… Concurrency.
Okay. I mean, one thing is building with Ship 6, and another is… Fixing all the swift concurrency issues, which is a fantastic task.
Probably difficult.
So he was more or less asking where that will be.
Yeah, we… Till not.
At that point, I'm probably won't.
For a long period.
**Billy Zhou** 18:20 What are the main, concurrency issues that we're worried about?
**nacho** 18:25 I mean, yeah…
**Billy Zhou** 18:26 Yeah, just small things here and there.
**nacho** 18:27 Basically, the thing is that if you move to Sweep 6 with street concurrency checks, We are gonna have lots of…
**Billy Zhou** 18:36 Yeah.
**nacho** 18:37 Things that won't be real, right?
That… that will fail, or that we will have to put a transcendable, and things like that to… to build.
**Billy Zhou** 18:48 Right, but are there, like, known issues that, like, we're, like, worried about in particular, or just in general?
Okay.
**nacho** 18:56 I think it's just in general. Okay. Because we have someone checks sendable that fixes the bins, but are not really being sendable at all. So the concurrency checks will not Flag it, but we will be… we won't be safe. I think that's more or less what he says.
I mean, it's not that there is any concurrency issue per se, but… That the street concurrency checks won't pass, because we… We… we are… Not… being valid there.
Yeah, I think that's for the cover. Oh, sorry, yeah, they opened this.
3 days ago, I checked it, but… Yeah, they said… that the value.
**Bryce Buchanan** 19:49 Or…
**nacho** 19:51 are different between languages.
I don't think that's… Right?
I mean, we don't have to keep that.
Do we?
**Bryce Buchanan** 20:03 I don't know.
**nacho** 20:08 And, yeah, and we are following the sea.
structure that, okay, is a zero, right? And whatever is not a zero is not a good result. That's Unix standard result values. And the thing is, while we whenever… OTLP is created, or when we are reporting to the cloud, or to the backend, not TLP, then we must have the same value, right? But what The values you have in the library in between?
Is that set in the spec?
**Bryce Buchanan** 20:44 I'm looking at it right now, and it could be interpreted that way, because it says the unset status is the default status, so if you, you know, like, that might… you might… Infer that that means that it should be zero?
**nacho** 21:10 I don't.
**Bryce Buchanan** 21:12 But I don't think that it's really relevant for anything.
**nacho** 21:16 It shouldn't.
**Bryce Buchanan** 21:18 Right? Or… or does it… does this get translated into… I mean, we…
**nacho** 21:30 The only problem is when you export to a TLP or to some other.
**Bryce Buchanan** 21:34 Yeah, does this… does this get sent through OTLP?
**nacho** 21:38 Yeah, but it will.
Yes, it must be sent… be sent, for sure, but we are probably… Not sending the value itself, but comparing with the… it's not the natural value, right?
**Bryce Buchanan** 21:55 For me, look at that.
Let me look at the Proto.
**Vinod Vydier** 22:08 Yeah, the instrumentation library should set the status as unset.
Which is… 0.
**nacho** 22:19 But we are setting it to 0 to 1.
**Bryce Buchanan** 22:23 I guess the question is, if we are… Yeah, so, in the OTLP, that is the case, so unset OK error.
But the question is, is are we… are we improperly passing the… The enum there.
Mmm, Oh yeah, it looks like we might be doing it backwards.
Yeah, you're in this… you're looking at the same spot I am.
**nacho** 23:43 Yeah, we are setting the values, right?
**Bryce Buchanan** 23:46 Well, yeah, I guess, are those… those must be the proto… values, right? Like, where are the, are they the, Which one are we setting? Yeah, like, is it… is it using our enum to set it, or is it using the… Oh, yeah, it is.
Yeah.
**Vinod Vydier** 24:09 It's secure.
**Bryce Buchanan** 24:10 It's doing it… I think it's doing it properly. It's just that internally, it's… it's not using the right… order, but I think that doesn't really matter.
**nacho** 24:22 Okay, we are not using the raw values.
**Bryce Buchanan** 24:25 Yeah.
Okay, so it's not really… it's just like a… it's like a…
**nacho** 24:29 Yeah.
**Bryce Buchanan** 24:30 kind of thing.
**Vinod Vydier** 24:32 So this is not even set, you know, this is coming from the protobuf, right? It's… the compiler sets it up, yeah, or the protobuf compiler does it.
**nacho** 24:43 Yeah, yeah.
But yeah, I think it's…
**Vinod Vydier** 25:06 So how come the… for JavaScript, it's, answer this… you know, maybe the JavaScript support of Companel.
Is not setting it correctly.
**Bryce Buchanan** 25:26 Well, the JavaScript one, it's… It's the same order as, the proto or the OTLP definitions.
Ours is just… ours is just, That swaps 0 and 1.
**Vinod Vydier** 25:48 Well, the person is saying… the open issue is saying it is, unset is 0, and… Okay is one.
**Bryce Buchanan** 25:57 Yeah.
In, yeah, in OTLP.
**nacho** 26:02 Yeah, but it's just an internal representation, right? We are not using the raw value anywhere.
**Bryce Buchanan** 26:07 Yeah, it does…
**nacho** 26:07 It could be an integral, or it could be just a chair, you know, it's not…
**Bryce Buchanan** 26:13 YAMP.
**nacho** 26:14 It's not something that, really change anything.
**Bryce Buchanan** 26:19 Nope.
**nacho** 26:22 Yeah, that was my concern when I read it.
So, for a pandemic issue, we have way more requests.
Many of them are just.
**Bryce Buchanan** 26:32 Oh, they're just chores, yeah.
**nacho** 26:34 Yeah, these… these shows are… are… Or even.
So, from there, we have… Yeah, the older ones that we have here, the crash reporter that got some feedback.
to… to update.
I liked it, but yeah, probably, I don't know if we should just land it and let the people evolve it.
With the changes that we want.
And release it as a beta.
Because it has been here for many months now. I know Willie Billy has been probably busy with other things I couldn't update. You have, you know, you have been working on the Swift 6 in many other, Everyone doesn't have time for everything, so… my take is not… for you to address in this, or it's more about, is this useful as it is? Can we release it as a beta? Can we let it open for others to improve what they reported as good changes?
Because it was working, right?
It's basic, it has some limitations, it's probably not the best option, but… Does it add value to users?
Can users improve on what they reported? That's my take, if we should think about that. Do we want to learn something really complete?
Can we release a better list?
What it is there.
**Bryce Buchanan** 28:03 I think some of the feedback in there could potentially be crashing issues.
Like, Let me see here. So, there's some, like, thread safety concerns in, And… where is it? Let's see here… It's in the way that the crashes are processed.
Because it's… it's accessing a queue.
From what I understand, That could potentially be… That's incredible. Yeah, like, yeah, there could be… There could be risk conditions there, so… Yes.
**nacho** 28:54 Yeah, there's…
**Bryce Buchanan** 28:54 Yeah, I think… I think that sort of thing needs to be addressed before we merge it, but I think there might be some other more nitpicky kind of… Things in there that aren't as important.
**Billy Zhou** 29:07 Okay, yeah, let me at least, rebase, and I'll address that, yeah.
**nacho** 29:15 Yeah, yeah, that's… yeah, basically that's my point, right? Is… Do we have to address everything, or can we just land something and let… Like…
**Bryce Buchanan** 29:26 Yeah, for example, there's the, like, you know, allowing more configuration by exposing, like, a crash configuration API, but we don't necessarily need to do that. That could just be, like, a feature improvement that we do later on.
**nacho** 29:44 Yeah, I think, yeah, those few things and this mutex, for example, here, that could be nice to have.
Yeah. And probably a threat sanitizer will… will… raise the issues here, just exercised.
Quickly, and yeah, and… The thing is, I've been PR open for… Months.
I think it doesn't add value, so… Just, just that, my, my opinion for that.
Okay.
So let's go with the other. We have, Yes, we distribute the tracing bridge. This is also something, that was asked in the, in the, in the… The issues, for anyone to take.
And, yeah, and we have, Simon that… I just started this. I started with some changes and asked for feedback.
I encourage him to continue with that, because it's something that we really want to have.
And he had this question, I don't know, how to say that. Basically, his problem is, I don't know if maybe the spec… the open telemetry spec has changed recently or not. I didn't check that. Probably you know better.
Because we use that. Yeah, basically, the thing is that the pentelemmetry… when he's converting from a pentelemetry… from shift tracing to a pentelemetry shift.
He found that he can add links to expense in… Any time of the life of this plan.
And in our library, you can only add links, At the span creation time.
I don't know if that's forced by the spec, Or you could… Or it's just that our library is not supporting that?
**Bryce Buchanan** 31:55 I've got it here. Let me read the specs. So, links exist so that you can associate one span with one or more spans, implying a causal relationship. For example, let's say we have a distributed system.
Where some operations are tracked by a trace. In response to some of these operations, additional operations are queued to be executed, but the execution is asynchronous. We can track these… the subsequent operation with a trace as well. It would… we would like to associate the trace for the subsequent operations with the first trace.
But we cannot predict when the subsequent operation will be started.
We need to associate these two traces so that we use a spam link.
You can link the last span from the first trace of the first, or to the first span in the second trace.
Now they are causally associated.
Links are… links are optional, but serve a good way. Okay, that didn't really help.
**Vinod Vydier** 33:04 It can be added… it can be added during span creation, which is preferred, or after.
**nacho** 33:12 Yeah, yeah, I was going to… if the spec doesn't say the opposite, I was going to tell him to just make links… Mutable.
while they span.
After the span has been created.
**Bryce Buchanan** 33:30 Oh, that didn't work. Oh, oops.
There shouldn't be a space there.
**nacho** 33:35 You were trying to share?
**Bryce Buchanan** 33:38 Yeah, I posted a link.
**nacho** 33:41 Oh.
**Bryce Buchanan** 33:41 To the, to the spec.
There we go, okay.
**nacho** 33:45 So let me then continue staring.
**Bryce Buchanan** 33:49 Api must provide… Can I take span context or the span to link.
Either an individual parameter or an immutable object encapsulates them, whichever.
The pollination should record links containing.
**nacho** 34:19 Yeah, must… the IP documentation must state that adding links at the span creation is preferred to calling at link later.
**Bryce Buchanan** 34:29 Yeah, so, for contexts that are available during spam creation, because head sampling decisions can only be considered in, Creation present during the span creation. Yeah, so it, I guess, is the, the solution is you create the link when you create the next span, the downstream span.
Not on the span that's already running, right? Is that it?
**nacho** 35:01 Yeah, but it doesn't… I mean, it says that it's preferable because you have the sampling decision at creation time.
If you add it later, you can lose that.
That sampling, or your preferred sampling, but it doesn't… So, Bradley, We could add… Links after creation, right?
If that's needed.
**Bryce Buchanan** 35:28 Yeah, I suppose.
**Vinod Vydier** 35:29 Yeah, that's what it says, right? Prefer to do it on the creation.
**nacho** 35:36 Yeah, totally. I guess, yeah.
**Vinod Vydier** 35:41 And you can also add additional. We can mutate it, but you have to preserve the order in which the links are set.
**nacho** 35:48 Yeah, I mean.
**Vinod Vydier** 35:49 Add multiple links, also.
may provide.
**nacho** 35:57 So maybe we should… tell him to… change the API to support adding links later.
For this thing to happen?
**Vinod Vydier** 36:16 Okay, so right now it only does initiation, okay.
**nacho** 36:23 to me, I think it's not… Forced by this pick?
Because it only says that Add multiple links at… It must provide an API to record a single link.
But…
**Bryce Buchanan** 36:46 Yep, guy takes a span context to the… LinkedIn and the attributes, okay.
**Vinod Vydier** 37:06 So, the must is to record a single link, May is… Multiple with the… and if there is multiple, you have to set Preserve the order.
But yeah, definitely you can add later.
Okay, so…
**nacho** 37:24 Okay.
Yeah, probably this has changed with the years.
So, yeah, I think we… We can telekin to…
**Vinod Vydier** 37:38 So what is the… actually, what's the last part? The way… because head sampling decisions can only consider information.
Present during expand creation.
**Bryce Buchanan** 38:01 Oh, interesting, okay.
I see. So, the SWIFT distributed tracing after spam creation. Yeah, so I think that it seems reasonable to Allow… Existing spans to… get links. I guess the problem is, is that there might be downstream effects on the, like, mutability of spans or something.
We might… we might run into problems implementing it.
But I don't think I have any problems with allowing that, right?
**Vinod Vydier** 38:42 It's definitely in the spec, but Yeah, I'm still trying to understand that last part. What is that?
That is… that seems to be the… Documentations must state that adding links at the span creation is preferred to calling ad links later for contacts that are available during span creation.
Because… of the head sampling. So they're saying gracious, but… Link at span creation is preferred because of the head sampling.
Oh, so… Hmm.
So if it is sampled, you know, not picked up, then the span is not going to be created.
If the span is not created, there's no link, so…
**nacho** 39:47 Yeah.
What do you think about this answer for him?
**Bryce Buchanan** 39:50 That looks… that looks good.
**nacho** 39:52 So, if we want to add that, before we do… Yeah, if it follows the spec, and we can add that data, yeah.
Okay, that one… Yeah, we have a Docker.
Not sure, or however they are.
Yeah, also we have this… This is the one that I did not mention.
We have this.
Plastics?
No description.
unjustico.
We… you know, my, my, my Chinese… I think it's Chinese. I… it could be other kind of, like, language. It's not very good, so I don't know what they are saying. Yeah, I expect it's documentation, but the thing is that they should ask cloud code to… in English, so it documents in English, right? And they will also say, if it's, AI-generated, it should be, I think, in the comments.
Yeah, this is with, basically with the… Network status, I think you did this long ago, Bryce.
**Bryce Buchanan** 41:21 Yeah.
**nacho** 41:22 But basically, the thing is that you can only check that value when the system comes back to you. That's what it tries to do here. But we have another PR that does the same.
**Bryce Buchanan** 41:35 There's been some changes to this API recently, like, they blocked it down.
**nacho** 41:39 Yeah, could be that. We have this one. We've had a crash with this long ago, but never received more feedback when we asked that. But yeah, basically, I asked for a description and attached the crash stat, and also the comments in the code should be in English, so that's what I asked.
But no feedback, from… from that.
We have… the thing is that we have… in the issues, he opened it.
But he didn't link both, so I don't know.
And this is the same fix by another guy, Who also… yeah, they… he… at least he added all the Sumai.
And the things here.
**Bryce Buchanan** 42:24 Very nice.
**nacho** 42:25 I think he's… yeah, that's very nice.
Work on the air. We'll take… To be honest, and also documentation is like this.
I… yeah, I was waiting for this meeting with more people, because… Yeah, clearly, clearly.
this is AI generated, and I would like that People say that… they have used this AI or this other for getting the results, and probably the documentation is extremely I mean… You shouldn't write these, right?
This is not the documentation. This is not what is documented here.
Right? But… The AI is just adding the… documenting what it has changed.
And why it did, and that's not what we want. But I was waiting for… meeting with more people, because, yeah, we were talking about this last week, be not a mix.
I think we.
**Bryce Buchanan** 43:30 Yeah.
**nacho** 43:30 ask for… proper documentation and proper, attribution of the things that are done. And this kind of documentation is not the style of the documentation for things like white thread safety, what does threat safety Has to…
**Bryce Buchanan** 43:47 Right?
**nacho** 43:49 I don't know how to answer this.
To be honest. It's great that they are doing this, this is probably the fix we need.
But we should be attributing to AI when that's… Part of the work, and we should try to follow the style of documentation.
I don't know if you agree with Raz.
**Bryce Buchanan** 44:13 Yeah, I don't necessarily care whether or not they say it's AI, It's evident. But, but, yeah, I mean, we can definitely give them the feedback that, like, the… there's too much… like, the documentation that I had there is not valuable, so that should probably just get cleaned up. And, I mean, we could even just clean it up ourselves.
**nacho** 44:39 Yeah, and the other thing was, we had this PR… Requesting change.
**Bryce Buchanan** 44:42 pages.
**nacho** 44:43 Yeah, we had this PR from, this other, developer, with the comments, I think, in Chinese.
I… And, yeah, he was first, right?
So we should merge his… changed, but he has not provided any feedback since I is I asked him, so I don't know if we should Ask for cleanup gear, and the first who answers, we merge that.
Or we wait for the other.
**Bryce Buchanan** 45:18 I mean, yeah, whoever… whoever… Comes back first.
**nacho** 45:23 Okay.
**Vinod Vydier** 45:24 Okay, so both the fixes are for the same? It's the same fix?
Yeah. Okay, wow.
Until is that?
Oh, yeah, I can definitely find things that, Humans cannot find, sometimes, bugs and so on, but… Yeah, you can clean it up, right, in terms of when you're… Updating the repo.
**Bryce Buchanan** 46:05 I'm not really sure at this point how useful this, network info instrumentation is anymore, now that you can't get like, the telephony data? I guess you can figure out if you're on Wi-Fi or cell, but that's it. I guess that's the use of it.
**nacho** 46:21 Yeah, several people are using it, it's because it's useful, right? If they are fixing the crash, it's because they are finding it useful in their code.
**Bryce Buchanan** 46:31 Yeah, I, I'm just trying to remember. I guess it was… it was just the carrier information that was, removed from From it, I believe.
**nacho** 46:51 I was going to do something like this, I don't know if that's also… That's hurting.
**Bryce Buchanan** 47:31 Yeah, like, the changes are documented by the GitHub, or by the Git history, and commit messages. It doesn't need to be… Yep. In the file.
**nacho** 47:46 Yeah, we'll put… dot, yeah.
How about that?
**Bryce Buchanan** 48:50 Yeah, that sounds good.
**nacho** 48:51 And my shitty news, okay.
Okay, so I, I think that for food requests, those are all.
So, as you'll see, not many things happening. And issues, I think, basically… the same… This… the… the value, the N64, new IN64 value is the thing that was fixed in the latest 2.4.1 in core.
That when we release, it will be fixed.
Changed to a bank.
spend, Events API.
**Bryce Buchanan** 49:38 Cool.
**nacho** 49:39 And this is the cross. They cross that from the… the, the, the… the developer that didn't put anything in his PR.
places, right? It's like, ugh.
Yeah, I don't know.
**Bryce Buchanan** 49:54 I had a question about, the, it's one of… some of the PRs, I know that we're kind of on time, but, I was just curious if we have done any discussion about Like, updating… Some of the dependencies, like, the Swift Neo stuff.
Have we… has anybody looked into that at all? I know that it was kind of a hairy concern.
**nacho** 50:29 I think Ari has been… Handling some of this?
**Bryce Buchanan** 50:35 Oh, okay.
**nacho** 50:35 In the past, some of the dependencies But… Yeah, but not others. This is extremely noisy.
Yeah.
It creates so many messages that you miss the real important ones.
**Bryce Buchanan** 50:55 Yeah.
**nacho** 50:56 In my opinion. But yeah, I think he has been handling some of them, but some others, I think we are… we have not checked.
because, for example, Swift NEO could bring Some compiling issues, right?
**Bryce Buchanan** 51:11 Yeah, because I think… are we waiting on the Swift 6, support implementation, I guess, for that stuff? That's really the key thing?
**nacho** 51:21 Yeah, early.
**Bryce Buchanan** 51:23 Okay.
Alright.
That's all I had.
**nacho** 51:28 Okay.
**Bryce Buchanan** 51:29 Just another note for myself, I'm only working half days, I'm still kind of partially on leave.
So I'll try to… to help where I can, but, I have limited… limited time.
**nacho** 51:44 Okay.
Yeah, you know, I also have limited time.
Yeah, I think we are… I think we currently… don't have anyone who can really take a lot of time, because Harry, I think he… I'm not sure he has time at his new company.
**Bryce Buchanan** 52:07 Right.
**nacho** 52:07 or…
**Bryce Buchanan** 52:08 That's unfortunate.
**nacho** 52:09 Some of… I don't know, he didn't… tell, but I don't know if he… he was not sure that he will have .
**Vinod Vydier** 52:18 No, but the thing is, this new company is also an observability company, so… Oh, that's good. Mobile…
**nacho** 52:24 Yeah, it's observability related, right?
**Vinod Vydier** 52:26 Yeah, yeah.
**nacho** 52:27 Marshall?
So probably he might have time from his company to work on things like this.
But, yeah, I don't know.
**Bryce Buchanan** 52:37 Okay.
Cool.
**Vinod Vydier** 52:41 Alright.
**nacho** 52:43 Yep.
**Vinod Vydier** 52:45 Sounds good.
**Bryce Buchanan** 52:46 Alright, everybody.
**Vinod Vydier** 52:47 Thanks, sweet.
**Bryce Buchanan** 52:47 Have a good rest of your week.
**nacho** 52:49 See you next week.
**Billy Zhou** 52:50 Hey, guys.
