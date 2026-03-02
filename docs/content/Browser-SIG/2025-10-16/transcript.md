SIG: Browser SIG
Date: 2025-10-16
Duration: 32 minutes
Zoom Recording URL: https://zoom.us/rec/share/tREPdoE9lsK4n7XzybFdfrokBn5JDdn132Texi6HdFUO1KPeDcVVeDd3OiB22QDT._j3qHCckMwF2R9vz
============================================================

## Zoom Recording Transcript

**Jared Freeze (embrace)** 00:22 Hey, Daniel.
**Daniel Dyla (Dynatrace)** 00:27 Hey there.
**Jared Freeze (embrace)** 01:22 So, no Ted and Martin today, I saw the note.
Looks like there's not a ton on the list today.
**Daniel Dyla (Dynatrace)** 02:19 No, but the first item took, like, half an hour on the spec call on Tuesday, so…
It might be a bigger topic than you're thinking.
**Jared Freeze (embrace)** 02:30 No, I mean, it looks big.
It's just a short list, I suppose.
What's the Tuesday meeting? Exactly?
**Daniel Dyla (Dynatrace)** 02:40 That's the main specification meeting.
**Jared Freeze (embrace)** 02:43 Okay.
**Daniel Dyla (Dynatrace)** 02:49 theoretically, all of these, like, SIG meetings are subsets of that.
**Surbhi Agarwal** 03:49 Can we get started?
Awesome.
Let me…
**Joaquín Díaz** 04:01 Do you want us to share. Can you share? Okay.
**Surbhi Agarwal** 04:04 Yep.
Are you going to share?
**Joaquín Díaz** 04:08 Golfers?
**Surbhi Agarwal** 04:13 I did not understand that, sorry.
**Joaquín Díaz** 04:16 You can share, if you want.
**Surbhi Agarwal** 04:19 Can you share?
**Joaquín Díaz** 04:21 Okay. Oh, yeah, okay, sure.
Hello, for a second.
**Surbhi Agarwal** 04:27 I need to provide some, permissions, so… Hi, Bill.
**Joaquín Díaz** 04:36 Can you see my screen?
**Surbhi Agarwal** 04:37 I can, thank you.
So, this was regarding… like, network requests, different phases break down, like the DNS lookup.
connection setup, TLS handshake, and then the various phases for the network request.
when the response is uploaded to the server… the response is downloaded from the server, the server processing, the request is uploaded to the server. So, basically, there is a requirement for gathering metrics around the durations of these various phases.
So I raised a issue in the semantic convention repo a while back.
So from the browsers, folks, what I learned was, right now, there are separate events on a span that mark these different phases and the duration these phases took.
But span.events is deprecated and going to go away, so the next thing that the browser was doing was having a standalone event.
To mark these different durations or timestamps.
The problem… the… that is needed because…
You know, like, they are… these events are asyn… these callbacks are asynchronous in browser.
But these events don't capture all the required
attributes from the original HTTP span.
Which might be needed for filtering, the metrics with later on, right?
So, like, I am proposing, for mobile, that's not the case, that…
it is asynchronous callbacks, it is all synchronous in mobile, both iOS and Android, so we are able to gather these
timestamps during the HTTP span itself. So, I am proposing, instead of a standalone event, adding individual timestamp attributes to the original HTTP span.
So, that, would, like.
provide some benefits, right? One is, like, we can unify the semantics across browser and mobile.
we can have all the attributes in the original HTTP span itself, we don't need to…
worry about not having them at the time of the event, or having to restore them and replicate them in the event. And there would be one-to-one mapping to each request, which is also important, something very much needed.
And yeah, backends will have all the data in one signal. They don't need to correlate between a span and a standalone event that, let's say, comes back later.
So, wanted to see what the folks here think about this.
**Santosh Kumar Cheler** 07:44 Just to add, a few things to what service says, I think the… Like, I…
I commented in the issue she raised, and I was suggesting that it'll be ideal if…
The conventions are consistent across browser and mobile, because at the end of the day,
Both mobile and web applications are
together considered as, you know, being part of a RAM offering.
So it'll be easier if there is some consistency.
Between the two. So, just wanted to hear out, the opinions from the browser side of…
**Joaquín Díaz** 08:31 Yeah, yeah, I'm definitely on board of consistency. It's not something that…
You already decided on the mobile side, or you are also discussing this on… for mobile apps?
**Surbhi Agarwal** 08:44 The issue is being discussed right now, but sort of we have reached that path. Like, we had quite a good discussion in this issue.
And that seems to be a possible option to go with, having individual timestamps in the original HTTP span itself.
like, span.events are going to get deprecated, that's not an option. The other one was…
a standalone event, which we discussed here, might have some drawbacks. And then individual… there are… there is instrumentations for different network phases.
DNS, TLS, but they cater to other use cases, wherein you need a detailed drive Detailed dive into the…
connection-related stuff. This is… here we are just talking about the network request phases breakdown, the different durations that these phases take.
So, mapping them to the request itself is very beneficial.
**Santosh Kumar Cheler** 09:53 Yeah, there is also a little bit of history. I think Martin…
And never think they know more, but I… what I remember is, as of now, the instrumentation, such as, you know, document fetch.
XHR and, fetch.
instrumentations. They do include the… this timing breakdown
information as part of the span itself, but they… the span is… span is actually, you know.
You know, is ready to be emitted much before the browser provides The… the timing breakdown.
So they wait.
And I think Martin's argument was, you know, why wait, you know, I think… Let's…
You know, split them into independent concerns.
Let's emit the HTTP span as soon as it's ready, and once the browser
you know, calls back with the timing information, let's emit that separately as an event, and then… and we can put sufficient
Information in the event to be able to connect back with the spam.
Yeah, and here, I think Surabhi is suggesting that we go back, stick with what we currently have, let's not separate them out.
**Jared Freeze (embrace)** 11:18 Well, I'll say, just…
In reality, you know, there's a lot of stuff available by the time any given library could report it back.
So… Like, does that make sense? So, like, you have…
Like, a lot of that information.
Right? Because we're gonna have to load a library. You know, there's not… in most cases, in, like, most cases.
the library itself, right, the actual JavaScript is not gonna load until DOM content loaded is done. There's quite a lot of information ready at that point. It's not like you're gonna beat much, except, like, load end, potentially.
Like, there's only gonna be a couple… like, outliers, so, like…
you're not waiting, really. Like, if you call it right away, you're gonna have a ton of events.
**Santosh Kumar Cheler** 12:08 that is true in the case of the initial document load, but
think of the XHR in Fetch, too.
So, in those scenarios.
Your XHR request would complete.
And, you'll have to wait for the browser to report the resource timing.
event.
**Joaquín Díaz** 12:34 Yeah, sorry, so,
I'm getting in context of this, like, by looking at the code, and… so you're saying that if we add them as individual attributes on the HTTP event.
we will still have to wait until the browser reports back the performance entries, and then add those as attributes, and then send the HTV event span to it.
**Santosh Kumar Cheler** 12:56 Correct.
**Daniel Dyla (Dynatrace)** 12:57 You actually can't even end the span until you have all the information, though, because at the moment that you end the span, it can't be modified.
So it goes directly to the export pipeline synchronously at that point.
So you would have to save a timestamp.
Wait, end the spam later.
The risk is, like, if somebody closes the browser or something, the spam may never be ended.
It's probably a very short period of time, very unlikely to actually happen, but…
**Joaquín Díaz** 13:32 Yeah, so…
As you say, like, it's very unlikely, and the overhead is if we have two separate spans or events, then…
There is a lot of overhead in connecting those together, and you have to do that for every span.
If you go that route of having two spans, so one is… one as soon as if
The request ends, and then one as soon as you get all the information, and then you have to connect those together on the back end.
But only you will be solving a few small cases where the browser might be closed before we get all the information.
So, that is… I wasn't on the discussion where you…
when Martin was talking about this, so I don't know the full context, but if I have to…
give an opinion night today, I think, for me, it makes sense.
To add them as attributes.
If that works. If that is the same as mobile is doing, so we are consistent.
But,
Martin is not here, so I don't have full context on what he was thinking about when this discussion happened.
**Santosh Kumar Cheler** 14:41 Actually, I just realized, as we were speaking, that
The current instrumentations are, are not, removing
what exists already. I think… I think Martin suggested adding a configuration parameter to disable
You know, the… waiting for these, performance timing information.
And then those who want this separate event, you know, can add this separate instrumentation library, you know, as needed.
So the question then becomes, that can be transition the, the existing, instrumentations?
To… to send this performance timing back down as attributes as against… Span events.
And it looks like, That might be acceptable.
**Joaquín Díaz** 15:46 Yeah, but only in the case where you wait for all these attributes, right?
**Santosh Kumar Cheler** 15:50 Yeah, yeah.
**Joaquín Díaz** 15:50 Do you accept the results.
**Santosh Kumar Cheler** 15:51 But, so it's an option, right? So those who…
We, we wait today, anyways, so that's the current behavior.
So, if we do that, then…
There is… there is some path to consistency, or there is some option for consistency between mobile and web.
Actually, yeah, at least…
Those who want it separate, you know, can… can, you know, configure, you know, their application accordingly.
But if we… Decide on the semantic conventions for these, breakdown parameters for the performance timing.
Then that's all that might be needed.
**Surbhi Agarwal** 16:36 Yeah, and I would like to add, like, from the log SIG,
event sig, I got to know that, like.
And when span.events are deprecated, the default would be to emit a standalone event instead of a span.event.
from the same APIs which emit the span.event today.
So probably it's better to migrate from that to individual timestamp attributes. Like, we would have to, because the default behavior itself would change, that would be a breaking change.
**Santosh Kumar Cheler** 17:13 Yeah, and I would also, Suggest using maybe an array?
Because if we include those as attributes, I think the older… It's confusing.
But these, these have a certain order, right? They are ordered by the timestamp.
So you… maybe… I mean, as an option, we can consider putting it in an array, too.
now that, I think the span… I, I don't know, is…
Do the span attributes now support nested attributes, or is that still in progress?
**Surbhi Agarwal** 17:58 I'm not sure. I think… I have not seen, like… Array attributes.
Postman so far.
But I will take a look, and that makes sense. Also, like, we were thinking of having configuration properties, where… two configuration properties, one connection level attributes and one request level attributes, that the
User can configure what they want in their span based on their needs.
there could be a… there are these few timestamps, right, for DNS start, DNS end, two response header and body start, and response body end. So, they can config that list.
would be empty to begin with, and they can configure what they need. So we only capture what is
exactly needed.
And that, is a good suggestion that we should probably think of collating them into an array on a span, if that's possible.
We can perhaps have two arrays, one for connection-level attributes and one for… The, second phase.
**Joaquín Díaz** 19:22 Yeah, again, it all makes sense to me. I think…
We will be working soon in migrating some of these old instrumentation to the new browser repo, and doing some cleanup and, like, modernizing what we get.
Because at some point, that desire, also, we may… may… may get more information that…
But when… when we… they run them.
And we can have this in mind when doing this migration, maybe.
But, you know, I think the most important part is that
we should be consistent with all the client SDKs, and I think that's, for me, that's the most important part.
If that's a decision to be made there.
Are you all going to make their,
we can have a discussion here, but I… I think, at least for me, it makes sense. We can, maybe ask in Slack.
For the folks that are not here in this meeting today, so we get their opinion as well, but…
Again, to me, it makes sense.
**Surbhi Agarwal** 20:26 That sounds great. I will probably… I'm not in the browser SIG, but I will join that, and I can tag Martin as well to get his opinion. Anybody else we wanted opinion from, or just putting it in the browser SIG Slack works?
**Joaquín Díaz** 20:43 Yeah, let's start it right on the browser stake, Slack, and so everyone can chime in if they want to.
**Surbhi Agarwal** 20:51 Got it.
Yeah, I think that was a good discussion. Anything else anybody wanted to call out?
Okay, looks like not that… thank you so much, yeah. That sounds great. I'll do the follow-up, and hopefully we can unify the semantics across the browser and mobile.
**Joaquín Díaz** 21:19 Thanks.
**Surbhi Agarwal** 21:20 I agree.
**Joaquín Díaz** 21:23 Okay. Janet, you wanna go next?
**Jared Freeze (embrace)** 21:26 Yeah, so, I was just curious if anybody had vendor instrumentation.
that they know they wanted to submit. We're just gonna try to keep a list. I know that the list of tickets is, like, things to create, but we all have approximations or exact things that match, like, what's needed.
So I'm… we can just post in Slack or whatever, but just wanted to hear from anybody, if you have anything kind of ready to go, or… or not.
So.
**Joaquín Díaz** 22:07 It wouldn't…
Are you talking about instrumentation that doesn't exist currently on the contribute repo, or, like, some… something that each one of DS… like, each one of us in our companies have, and we want to contribute back, or… Yes.
**Jared Freeze (embrace)** 22:22 Yeah, things that don't exist. Like, like things we would find useful that people want to,
look at putting in the repo. The reason I'm asking this is because I want to get more stuff in so we can start building the ecosystem around, you know, like, code quality checks and things like that, and
just think about moving packages over. So, if there's stuff that's ready that's outside Contrib, I just wanted to start a list. That was… that was the only reason, but…
Sounds like there's not anything, so we'll just focus on what's there.
**David Luna Bistuer** 23:00 Sorry, if I get it right, the idea is to contribute here new instrumentations. So there's already
Because I've seen that Martin move a lot of… Issues, and…
One of… some of them is just doing implementation, user action events.
page navigation… those are already in country. So, yeah, it's just to… Add new ones here, right?
**Jared Freeze (embrace)** 23:25 Yeah, that's right. We had talked about migrating them as well. Any… I think what we were talking about was, like, any open PRs, like, just leave, like, in contrib, because that's complicated, but… but the actual files themselves, yes, we would bring over, once they're…
you know, clean, or whatever you want to say. You know, there's not a bunch of outstanding stuff. I think the idea was, like, when we find a moment in time where they're…
You know, there's no work against them, then shh, pull them over, and then…
At that point, look at, you know, publishing
you know, migrating the package name itself, so that way the install now comes from a hotel browser. That was the idea.
**David Luna Bistuer** 24:06 Okay.
**Joaquín Díaz** 24:10 I think, should we find one good example to start working on, so we have a pattern that we can follow for the other implementations? Also there is some setup still needed.
I think, like, the report's pretty much empty, so we need to set up, like, testing. I know I have the test harmless.
That we can merge once we have something to test. So I think…
Maybe we should think about the best candidate here that we can…
Start with, maybe something simple.
I don't know.
**Jared Freeze (embrace)** 24:50 Yeah, sounds good. I guess I'll go through contrib and look.
**Joaquín Díaz** 24:56 Thumbs… No? Yeah. Hold on.
**Jared Freeze (embrace)** 25:05 Oh, I actually had a question for…
Benoit, too. You created… I know it's on the agenda, but you created the list for bundlers, or at least the requirements for what we want to support. I thought that was really cool, so I just want to make sure we continue that on Slack, because you already had the document made, which is great, so…
Yeah, appreciate that.
**Benoît Zugmeyer** 25:31 Yeah.
Sure, we can totally discuss every point, but yeah, that's a start.
**Joaquín Díaz** 25:42 So… We have a lot of things here that are mixed up, so the ones that are ours…
I think this is just a, like, a recollection of other packages, right?
**David Luna Bistuer** 26:01 Yeah, that one just exposes a function.
That conducts all the instrumentation for web, and provides… you can pass that function an object.
**Joaquín Díaz** 26:12 Bye.
**David Luna Bistuer** 26:13 with… each entry has a configuration for each. It's… it's similar to how to instrumentation or not. So you can… just one function called, you can configure all instrumentations and get… get them ready.
For just registering it.
**Joaquín Díaz** 26:27 Yeah. So, then we have this one, yeah.
Yeah, so… We have, user instrumentation.
Yeah, it's really hard to know which ones are.
well, document load here, and the… I think the other ones are in the other repo.
The list that Martin has on issues is all new stuff, right?
Like, for example.
**David Luna Bistuer** 27:10 Well, while some of them are… they have…
Yeah, it's ongoing, like, the navigation.
**Joaquín Díaz** 27:16 Nice.
**David Luna Bistuer** 27:18 Beigeview is also there.
**Joaquín Díaz** 27:20 I wouldn't want to start a navigation, because
the conversation was really long to get there, and I think it's going to be the same with DPR, so…
I think I'll suggest starting with a really simple one, like, for example, user action.
Yes.
And maybe we can have this one as a part for our instrumentations.
**David Luna Bistuer** 27:49 Okay, good.
Any volunteer time?
**Joaquín Díaz** 27:58 Do we need to first merge the semantic cell?
Before working on the cementation.
**David Luna Bistuer** 28:07 Yeah, maybe we need someone to just reopen DPR. I, I tried.
A while ago, and I couldn't do it.
I'm really just created the one.
**Joaquín Díaz** 28:18 Yeah, we couldn't get a new one.
Okay.
if… No, no, I can take it, and if no one wants to take it, I can take it.
maybe at least have some indication, PR app.
Or next week.
So we have there… I mean, that's the usual flow, right? You first merge the semantic conversion PR, then work on the cementation.
**David Luna Bistuer** 28:53 Yeah, that would be… Maybe you can, I think for navigation, we're already making an exception.
the PR for navigation events.
**Joaquín Díaz** 29:02 Yep. And semantic batches is still open.
**David Luna Bistuer** 29:05 But I think that there's not much conversation there, so maybe it's just ready to go.
And there is, the current PR in country repository is, taking those attributes in consideration.
So…
**Benoît Zugmeyer** 29:22 What's missing for the semantic convention PR for user action?
**Joaquín Díaz** 29:31 is sculpt?
**Benoît Zugmeyer** 29:34 It's closed, okay.
**David Luna Bistuer** 29:35 It's ghost.
**Joaquín Díaz** 29:37 Yep.
Is this one, I don't know.
If there is a reason inactive, so…
I don't know if there was more discussion missing, or if it was ready, but I can…
I'm sure that…
I'll see the comments, because I don't know, I don't want to start from scratch if it was already a discussion.
**Benoît Zugmeyer** 30:01 Sorry, but it seems like there is another one.
The 1941.
It's still open.
**Joaquín Díaz** 30:13 19, you said?
**Benoît Zugmeyer** 30:15 Yep.
**Joaquín Díaz** 30:26 Okay, yeah, I think we… Talked out this…
Do we know who is this person, and…
If they are working on it, or if they're actively… Working here.
**Benoît Zugmeyer** 30:49 Carly is joining from time to time. She's also working on the resource… resource timing event.
**Joaquín Díaz** 30:59 Okay.
**Benoît Zugmeyer** 31:00 Fairly active, yes.
**Joaquín Díaz** 31:02 We accompanied her.
One slow.
**Benoît Zugmeyer** 31:22 Hmm.
**Joaquín Díaz** 31:32 Okay.
Alright, we're a bit over time, so, like, I'm… Confair on Slack.
To see what's the status of this, but we can continue it and try to get immersion so we can work on this annotation.
**Jared Freeze (embrace)** 31:58 Thank you.
**Joaquín Díaz** 32:02 Right.
Think of it, but…
**Benoît Zugmeyer** 32:05 Bye.
