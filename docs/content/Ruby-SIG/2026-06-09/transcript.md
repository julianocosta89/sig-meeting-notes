SIG: Ruby SIG
Date: 2026-06-09
Duration: 34 minutes
============================================================

## Zoom Recording Transcript

**Kayla Reopelle** 00:29 Hey, Matt, it's good to see you.
Oh, hold on, my audio's not working.
Let me… actually, let me switch where I'm at.
**Matt Wear** 00:46 I think the problem was me, if you can hear me now.
**Kayla Reopelle** 00:52 I can, yes.
**Matt Wear** 00:57 I just installed Zoom this morning, so there's… There's, like, settings, settings that need to be tweaked.
**Kayla Reopelle** 01:04 Add a brand new work laptop.
**Matt Wear** 01:06 Yeah.
**Kayla Reopelle** 01:07 Nice, what's your role at the new job?
**Matt Wear** 01:10 Boom.
open source?
**Kayla Reopelle** 01:14 Cool.
**Matt Wear** 01:16 So yeah, I think kind of like my… my old job.
**Kayla Reopelle** 01:22 Before the company changed a lot.
**Matt Wear** 01:24 Yeah.
**Kayla Reopelle** 01:27 Well, nice, it's great to have you back.
**Matt Wear** 01:28 Yeah, good to be back.
**Kayla Reopelle** 01:32 Hey, Sean. Hey, Hannah. Hey, Bart.
Welcome…
**Hannah Ramadan** 01:38 Hey guys.
**Bart de Water** 01:41 Blue.
**Matt Wear** 01:44 Whoa.
**Kayla Reopelle** 02:14 Here is the link to the notes… I'll share my screen… Oops.
Okay, can you guys see the notes?
Great.
Alright, so… Yeah, the agenda's in the chat, if anyone wants to add things to it, I'll get started.
with the spec sig… been listening to these while I've been commuting, and so inevitably there's, like, a section that I can't hear. So we'll go over the parts that I've… Was able to listen to.
The self-observability initiative seems to be moving forward quickly.
They are interested in, kind of, approving the OTEP for this.
Soon, or I'm sorry, getting, like, the specification actually in.
And, moving it towards stability. So I think if this, self-observability project is something that interests you. There's a decent amount of momentum right now. I haven't dove into it with the specifics. This, it just felt like it was more of a heads-up that This is, moving quickly, and so… Encouraging folks to get engaged.
There is also some talk of turning it into… like, an open telemetry project, with a clearer proposal and its own roadmap and things, and I think that's still kind of an open question.
There's even a move for semantic conventions for these self-observability events, so kind of the different pieces throughout the project are starting to come together.
The next one… This is kind of related to self-observability, but… there is a goal to have, a central OpenTelemetry benchmarks repository, at least according to this project proposal.
I know we've added some benchmarks lately to our own repos, but this would be a little more… formalized, it seems.
And here, the main request was just for more reviews, and if, this interests you.
to approve or comment on the OTEP for it.
And then… The big part that I unfortunately couldn't hear was this OTAP Arrow project presentation.
It sounds like Arrow… Does anyone here know what Arrow is before I try to explain what it is?
**Matt Wear** 05:41 It's a, it's from Apache, it's a columnar data format.
So… So yeah, I have a link to the slides somewhere here.
Oh, let me find them really quick.
I thought it was a really good presentation, and basically… some people started off, experimenting with Hotel Arrow as kind of like a wire format, just because, Columnar data can, end up being a lot smaller in size, so they, realized that there was, you know, a lot of potential for that to just decrease the size or the wire.
But, yeah, I think there's, like… there's a lot of projects built around, Arrow, like Data Fusion, because it's also, like, a really, really powerful way to, transform data. It's basically in a… in a columnar format, I don't know how, familiar people are with that, but it's a… it's a post, like, a row format, so it's kind of like, you can kind of think, like.
each, Each column from your data ends up being its own file, so if you want to, like, drop an attribute or, like, modify an attribute, it's just really, like, seeking to that one file and kind of… Changing things, whereas, like, row-based, you always have to kind of, like, read through, find your row, and then, Kind of mess with a bunch of offsets, so it just ends up being a lot more efficient for a lot of different, different ways you want to manipulate data. So I think the… so now they kind of have a collector that they're building around this, and… I don't know if you're familiar with the collector, but the collector kind of, you know, it receives data as, like, protobuf or JSON, and then it converts it into this thing called PData.
That you manipulate inside the collector, and then it's kind of like the intermediary format, and then your exporters will take that P data and then convert it back into whatever you want.
Oh, before sending it out.
And with Arrow, they're using Arrow as kind of the, as the internal format, so there's no kind of conversion to AP data, and I think that, Opens up a lot of possibilities for, like, transforming data in your… in your pipeline.
What?
But yeah, I've been away for a while, so, like, this… I know this project's kind of going on back… back when I was around, and it seems like it's made a lot of progress, so I'm… Interested in kind of digging in a little more and figuring out exactly… exactly what they're doing.
That's… that's my celebrity.
**Kayla Reopelle** 08:29 Nice. Thanks, Matt.
**Matt Wear** 08:31 The browser.
**Kayla Reopelle** 08:32 Cool.
I think that… Yeah, it's interesting, too, that… since there's more transport strategies, one thing that stuck out to me is they might be adding specifications for those transport strategies, since there's… this is kind of like a second version of the collector. It's a… it's a slightly different output. I don't know if I heard that correctly, but… It sparked something in my mind.
Let's see, what else have we got in here?
Some context sharing stuff. Is there anything else on this list that people want to take a look at together?
Okay, but yeah, there was a lot of… a lot of good stuff in this SPECSIG meeting.
Okay, we don't have anything on our agenda so far today. I just put a link to the slides that Matt shared in our notes directly.
Is there anything that the people who are here want to go over before we just kind of look at things more randomly?
Okay, I think one thing… But I will add… is the auto-instrumentation work. So we got… A… I think I can type and think at the same time.
We have a new repo for the, auto-instrumentation code. It would be the first release is coming from that. It's pretty much a copy of what we've been working on InContrib.
And… I think we got to a place in Contrib where we were pretty good with the implementation, and that was ready to get merged in. But, if anyone else here is familiar with auto-instrumentation.
And wants to provide some feedback.
then I think that now would be a good time. We can also have the initial release and do follow-ups, too, based on feedback, if people aren't able to get to it, because we've… This has been worked on for a really long time.
Is there anything about this project, Schwan, that you would want to share synchronously?
**Xuan Cao** 11:11 -Oh.
No, I think, I don't know.
It is easier, and if people want to see the task conversation, they can look at it and shoot.
To see why something… Epassing the other way?
Boom. Yep.
**Kayla Reopelle** 11:31 Sounds good.
**Bart de Water** 11:42 Sorry, I can… can I ask a dumb question? I remember looking at this last week and not quite sure, like, getting what this repo is for, as an outsider, and I frankly still don't, so if someone could give me a one or two sentence, summary, then I… I don't know, might be able to, like, give some, I don't know, fresh-eyed perspective on it.
**Kayla Reopelle** 12:09 So, auto-instrumentation in OpenTelemetry is this idea that you don't have to install, like a gem into your environment.
To get instrumentation, to have OpenTelemetry show up.
you use something else, usually, like, Kubernetes, or… some other strategy, I forget what the other parts are called in OTEL, to install it all for you.
So, if you didn't want to maintain all of the gems that you were installing in your gem file, this would be another approach. I think it's often used to help with, like, fleet management for instrumentation and keeping things on certain versions. There's quite a few other languages that have it.
Go ahead, Jim.
**Bart de Water** 12:56 That makes sense. This actually… behaves a path for another problem that I'm having at work, so thank you for explaining that.
**Kayla Reopelle** 13:04 Yeah, no problem.
So, okay, so I guess let's hop into Core and Contrib then, if nobody else has PRs that they want to talk about first.
Got a whole bunch of renovate pull requests, We… are making good progress on catching up to semantic conventions. I released, version 140 this morning, and then I think 141 Can come out.
Probably tomorrow.
I know we have a couple of PRs.
That we've been… working on lately. Is there anything that this group wanted to look at together today?
This is a PR that I have let languish and did not realize until I saw the stale label this morning.
that I had forgotten about it, but I think that this could be a good one to look at this week, because it is related to A potential security issue.
If, people have time to look at it, that would be great. I know there's also some changes, so I need to look at it as well.
But, yeah, I think this would be a nice one to focus on this week.
Oh, thank you for opening this issue.
Okay, Erin, I have some feedback on it.
**Xuan Cao** 15:27 So, I'm not sure if anyone have, like, preference of how to, Receptor? Or not receptor?
Some ideas, because, the main idea is to not have a separate portal and then… Make the common utilities together.
I don't have any preference of how this structure works, but I do prefer to have a minimum, Oh, yeah.
minimum, Chen Yellow Gems, because, you know.
Now we have to deal with naming stuff, and then… Deprecation… I'm not sharing that information anymore.
Anyway, that's, that's my, Do you mind asking for, for people to, assure the assault.
**Kayla Reopelle** 16:33 Yeah, I think getting rid of separate photos, is… would be quite helpful.
I know that, like, with stability… Well, I'll think about this more thoroughly instead of just… Spouting from the top of my brain here.
Okay, and then these two already have PRs associated with them.
I wonder how the… like, self-observability.
plays into this.
**Matt Wear** 17:35 I feel like that… That's, like, the real solution when you were talking about that, like… I don't know.
I'm sure some people are familiar, but there's kind of, like, some hooks that have been added into, our exporters, and… Shopify was really, Eager to do that, because they needed some way to kind of observe things, And that was the quickest, easiest thing that could be done, but I think that… Once, self-observed.
self-observer… I should be able to say this word. Once self-observability, like, ends up being a thing, I think we're gonna have to kind of probably deprecate and remove the, The hooks that are in the exporters, so… But yeah, it's like… the question is, how long is it gonna be until that's a reality, and should we… in the interim, I guess, extend that.
With the, caveats that it will probably be going away.
**Kayla Reopelle** 19:04 Yeah, deprecating it when we know more about the timeline, we hope.
Okay, cool.
Are we ready to move on to contribute?
A lot of renovate pull requests… Bart, since you're here, let's… let's chat about this one. I know we've been kind of stuck in a loop.
with, the names for the… attributes?
I don't know.
**Bart de Water** 19:42 Hardest part of computer science.
**Kayla Reopelle** 19:44 Naming things, yep.
So, yeah, so I think… You know, we've had similar input.
I'm still… Firm, in my opinion, about, not… like, sticking with, kind of, the metrics, or I'm sorry, the messaging prefix for these new attributes, and then… Continuing to have the conversation.
Matt, just for some background, have you seen this PR?
**Matt Wear** 20:18 haven't.
**Kayla Reopelle** 20:19 Okay, so, Active job continuations, BART's open to PR to add instrumentation for them, so that we get, information about steps.
And the kind of sticking point on the PR has been what to name the attributes. There's some concerns… like, the rest of the active job library has messaging attributes, because it seemed like that was probably the closest semantic invention.
There's some concern from Thompson Tomo that ActiveJob wouldn't be ever fully recognized as a messaging library by the semantic conventions, so we should find it different.
namespace, or kind of conventions, maybe define our own Rails conventions to use instead.
And the… I would say, like, the conflict right now is… do… for these new attributes, do we use something like a Rails namespace, or do we use the messaging namespace so that it's consistent with the rest of the attributes that already exist in this library?
There's a separate Issue where a discussion is happening about whether, you know, like, this library should move to a separate namespace altogether.
I think where I'm at right now is that that discussion needs to be resolved and shouldn't hold up this PR, and so we should just use the… Attribute names that are closest to everything else that's in this library.
But, but yeah, but it's kind of a torn thing. I have a thumbs up from Hannah.
I think Simi was also on the same page, but, yeah, I'm curious.
If in your experience of SEMCOM, if you have any… Thoughts are advice.
**Matt Wear** 22:03 Yeah, this… I feel like this is a continual problem where, The spec has, like, these generic fields that specify a lot of things, and there is, like, some degree of overlap with the thing that you're actually instrumenting, but then there is… Yeah, it's not, like, a complete subset, you know, and… I don't know.
I was hoping all this would be fixed by now.
I've left for a year, hoping that… that we resolve such things, but it appears they're not the same old problems, so I'm… I don't have, like, a definitive answer right now. I think my best answer is… I'd want to kind of search around in some of the other language SIGs and see, and see what they're doing for… for some of these things, and maybe just talk to some people and see what they're doing. See if… see if we have, like, full license, really, to kind of, like, introduce, like, a Rails namespace, or, like, an active job namespace for things, and if that's… if that… if that seems like it is… Like a… permitted route, then I think doing that makes a lot of sense for a lot of things.
Because, yeah, it's like, I feel like these job libraries are one of these things that… in some ways, looks like a message queue. There is a message queue involved, but… But once the message leaves the queue, is… Are… are we out of the messaging namespace? I guess that's my question.
**Bart de Water** 23:45 Oh, and compounding the confusion here is that, like, ActiveJob is an extraction over job queues. So, you know, like, in our case, we're using a Postgres-based baked job worker, so there's not really any messaging queue in the traditional sense happening.
**Matt Wear** 24:01 Hmm.
Yeah, that does make it more… more confusing. So I would say Redis, that's definitely a queue, treat it like a queue. Once the message has moved, then… I feel like you're kind of into the framework, but…
**Bart de Water** 24:16 Yeah. But yeah.
**Matt Wear** 24:17 If you're in Postgres, you're probably not getting a messaging span at all. You're getting a database span, and And nothing works as intended.
**Bart de Water** 24:26 Yeah, so I did sort of, like, like the suggestion that Thompson made, I think 2 days ago in the last message.
To introduce, like, kind of like a SenConf opt-in, but sort of, like, more of a Rails opt-in.
I would be happy to take a stab at that, and, like, land that first, and then make this… use that, so that, you know, like, whatever you end up configuring, like, you know, like, the whole thing will be consistent, depending on the setting that you set.
I'm also happy to just go with messaging here and treat that as a follow-up if and when someone decides to take a stab at it. But, yeah, like…
**Kayla Reopelle** 25:14 Yeah, I think the switch is interesting, and that is a good middle ground, but I do think it would touch a lot more things for this PR, like how kind of compact and focused on steps this one is, so I'd be more inclined to add that in a separate PR and kind of keep the attributes.
With messaging for this one.
And then we could also, kind of.
Decide in 2368 if we, you know.
kind of look at other language implementations, like Matt said, for similar libraries, and make sure that we're picking the right name before we add, like, a namespace switcher for a new name.
**Bart de Water** 25:53 True.
Also, like, didn't the RubySig get, like, ownership of the Ruby and RILS namespaces in another PR a few weeks ago?
**Kayla Reopelle** 26:03 Yes, we did, yeah, we got our own namespaces and semantic conventions, and so we are able to add semantic conventions to that now, if we want to.
**Matt Wear** 26:14 Are we using those pretty, pretty widely for other, you know.
**Kayla Reopelle** 26:18 Brand new.
**Bart de Water** 26:20 Right.
**Matt Wear** 26:20 Okay.
**Kayla Reopelle** 26:21 Yep.
**Matt Wear** 26:21 So, we haven't set, like, the… We haven't set a precedent yet.
**Kayla Reopelle** 26:27 Yes.
**Matt Wear** 26:28 But… Yeah, I will try to look at some other, Implementations this week, just so, Yeah, and I guess I'll report back at the next SIG what I find.
And, that might help us get direction.
**Kayla Reopelle** 26:50 Okay.
That's good.
I guess…
**Bart de Water** 26:54 I will then implement the PR feedback and switch back to the messaging namespace as before, and…
**Kayla Reopelle** 27:00 Campus.
**Bart de Water** 27:01 In a mergable state.
**Kayla Reopelle** 27:03 Okay, sounds good. I can add a comment, to the PR.
Summarizing our discussion today.
Great.
Nice.
Except everyone.
What else we got in here?
This one It's been around for a while.
And this is the maintainer of the HTTPX library.
That'd be nice.
To get this natively instrumented.
I don't know what his feelings are on that.
That sounds like it's just a PR to adapt to his new… System… I'm sorry, this one is languished as well, Bart.
I've kind of lost my… context on it, but I think it would be good to look at again this week, too.
Any other pull requests in Contramp that people would like to look at together or discuss today?
**Bart de Water** 29:06 Can I ask a random question?
**Kayla Reopelle** 29:08 Of course.
**Bart de Water** 29:10 So, a while back.
I took a stab at adding, like, PUMA metrics, but at the time, I believe the.
**Kayla Reopelle** 29:17 Right.
**Bart de Water** 29:17 wasn't fully baked yet.
I was thinking of bringing that back, but then being… wary of the fact that I'll be probably the first one working on adding any kind of, like, metrics to the contrib… library. I was curious if there's, maybe any… sort of, like, off-the-top-of-your-head guidance, or pitfalls, or I should be aware of before I, jump into Without a flotation device.
**Kayla Reopelle** 29:46 I would say… These real old PRs with prototypes are things that you could look at for advice. I think some of the big discussions that we had Around them, we're trying to protect the stable code from the unstable code. So, with these, the philosophy is, I forget if it's both of them, I think… They're the same, it's just one uses rack events and the other doesn't.
But the… the idea is that you need a… config that enables metrics, and then also the presence of the metrics API library. Otherwise the instrumentation won't get installed for metrics. And then, you know, it can live within the same instrumentation library for tracing. I don't think we have any PUMA traces, so that might not have the same problem. I don't think we have any PUMA instrumentation right now.
But, so that could also make it an interesting first… exploration, because we do have, like, the longer instrumentation now that we didn't at the time that this metrics prototype was being discussed. So… Yeah, so maybe, maybe Puma is actually less controversial than adding it to some of these other libraries.
**Bart de Water** 31:12 Yeah, well, because, like, it can be useful to figure out if your, sort of, like, your thread count is, like, properly, set up. That was sort of, like, my main driver.
**Kayla Reopelle** 31:23 Yeah.
**Bart de Water** 31:24 Yeah, I can… I can take another stab at it.
**Kayla Reopelle** 31:28 Okay, great.
**Bart de Water** 31:29 Let's see how that goes.
**Kayla Reopelle** 31:31 I feel like Puma metrics have been… Kind of… in the ether lately, New Relic just got a PR to add Puma Metrics, too.
From the community.
**Bart de Water** 31:42 Yeah, I mean, like… You know, I think as a North Star, it will be useful to make sure that there's great instrumentation out of the box for, sort of, like, the Reels default stack, so that's… That is a solid queue.
Another thing that I might take a stab at at some point is writing a little bit more beginner-friendly talks, because it's right now not easy to get started.
**Kayla Reopelle** 32:07 Yeah, yes. And I think there is a pull request right now to improve some of those docs. Oh, on page 1.
So that could also be another place to add… Some comments or other thoughts?
**Bart de Water** 32:24 I haven't done one yet.
**Kayla Reopelle** 32:26 Yeah, I haven't looked at this one either. Oh, a new developer MD file.
But yeah, since this is in drop mode, I haven't looked at it yet.
But it would be great, since you have, you know, kind of onboarded to the project recently, you've, you know, engaged and contributed, would love to hear how we can improve the documentation to make things.
**Bart de Water** 32:47 Well, like, I was more thinking for, like, even just downstream consumers, where people are, like.
**Kayla Reopelle** 32:53 Well, I heard this old dog.
**Bart de Water** 32:54 thing is the next best thing since sliced bread, but how do I get started as a developer in a hurry?
And then, you know, like, which GMs, how to set it up, It's, it's, you have to, sort of, like.
kind of, like, dig quite a bit, and get into, you know, source code, or, like, you know, specific READMEs of specific gems, and… I've been even wondering, if it might make sense to have, like, a real specific gem, where it's, like, kind of like auto-instrumentation, just drop this one gem in there and it'll… the whole thing kind of, like, automagically works? Don't know yet.
**Kayla Reopelle** 33:32 if…
**Bart de Water** 33:34 Or is that the… do we already have one? Oh, we already have one! Well, there we go.
It's just for.
**Kayla Reopelle** 33:40 the Rails library, so, like, the active job action cables.
**Bart de Water** 33:45 Yeah.
**Kayla Reopelle** 33:45 etc.
So it wouldn't include, like, a… like, a PUMA or any other common… Right.
Things.
**Bart de Water** 33:54 Well, I still need to, like, noodle on that one a little bit.
**Kayla Reopelle** 33:56 Yeah.
**Bart de Water** 33:58 But yeah, I think, Also, to just keep, sort of, like, my open source goals modest and attainable, I'll just start with Puma metrics for now.
**Kayla Reopelle** 34:06 Sounds good.
Alright, let's see… any issues… Nothing new… Since the last meeting… Alright, I guess then, yeah, last… last call for any other discussion topics today?
Okay, I think we'll end early then. Thanks, everyone, for coming.
**Bart de Water** 34:46 Right.
**Kayla Reopelle** 34:47 Hi.
**Xuan Cao** 34:48 Fair.
