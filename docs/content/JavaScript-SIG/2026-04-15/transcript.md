SIG: JavaScript SIG
Date: 2026-04-15
Duration: 61 minutes
============================================================

## Zoom Recording Transcript

Daniel Dyla (Dynatrace) 00:01:58 Hello, everybody.
Trent Mick 00:02:00 Oh.
Sure.
Daniel Dyla (Dynatrace) 00:02:05 We don't know.
Trent Mick 00:02:06 I go to two meetings at once.
But yeah.
Daniel Dyla (Dynatrace) 00:02:10 I'm gonna mark gray.
Trent Mick 00:02:12 Someone's talking right now. Yeah, Mark's in on that discussion, and Jen's on the team.
Daniel Dyla (Dynatrace) 00:02:16 Are you listening to the other meeting right now?
Trent Mick 00:02:19 No, I can't do two things at once.
Daniel Dyla (Dynatrace) 00:02:21 Okay.
Trent Mick 00:02:22 I'm already…
Daniel Dyla (Dynatrace) 00:02:23 can't…
Trent Mick 00:02:24 I'm 20 IQ down just with my face on a screen, so in two meetings, forget it, I'll be a toddler.
So…
Marylia Gutierrez 00:02:32 One headphone on each meeting, come on.
Trent Mick 00:02:36 Okay. You wanna tell me how that works? Are you doing it right now?
Marylia Gutierrez 00:02:41 I did join…
Trent Mick 00:02:42 You just tune in.
need, like, one of those… Beats ones where he can turn up one of the ears, but anyway.
Marylia Gutierrez 00:02:49 Kind of like those conferences that people can, like, choose the track that is on the stage.
Trent Mick 00:02:57 That's new to me, I haven't done that before.
Marylia Gutierrez 00:02:59 Oh no, so there are, like, some places that have, like, huge stages.
Yeah. So they actually have, like, two presenters, one in each corner, and with your headphone, you can select which one you want to listen.
Trent Mick 00:03:11 That's cool.
Marylia Gutierrez 00:03:12 Well, depends if you are the person presenting, because it has a color, depending on which one, so you see everybody with a different color, just like one person listed each year, so you're like, okay, then, then you and me, let's talk.
Daniel Dyla (Dynatrace) 00:03:29 Alright, I guess I'll… Get started sharing my screen here.
Trent Mick 00:03:35 Thanks for…
Daniel Dyla (Dynatrace) 00:03:37 Yeah, no worries.
David, pull request review.
David Luna Bistuer 00:03:44 No.
Daniel Dyla (Dynatrace) 00:03:45 You wanna say anything about this, or just call for a review?
David Luna Bistuer 00:03:49 the scalpo review, nothing else. I hope, I think that Well, maybe… But I guess that's it. Being a breakage agent core, maybe it's something that we want to have it for the next major release.
That's the only thing. If there is a kind of a deadline or something like that, it would be the next major.
Daniel Dyla (Dynatrace) 00:04:10 Okay.
Trent Mick 00:04:12 If, I guess the only thing I'd say there, then, is if… It looks clear, like, you're proposing… Or reviews are proposing a breaking change, maybe add it to the… the milestone that we have for the 3.0?
David Luna Bistuer 00:04:28 Yeah.
Trent Mick 00:04:29 So, like, it definitely… or just some way, so it definitely doesn't get forgotten for that 3.0 run, because, when we get to going.
David Luna Bistuer 00:04:36 in doing that, I…
Trent Mick 00:04:40 Yeah, I don't know if it's…
Daniel Dyla (Dynatrace) 00:04:42 about it.
Trent Mick 00:04:42 doing a…
David Luna Bistuer 00:04:44 Well, basically, the behavior changes with… So we don't, it does not discard completely the trace state, but only the entries that are not valid.
So, behavior changes and propagation.
Daniel Dyla (Dynatrace) 00:05:03 Okay.
Yeah, I mean, I… I think it's arguable whether that's breaking or not. I probably would lean on the side of that's not breaking, but since we're doing a 3.0 anyways, it's probably… Fine to just put it out with that.
David Luna Bistuer 00:05:22 Okay.
Daniel Dyla (Dynatrace) 00:05:23 Mary Leah… two different pull requests. Also… Call for reviews, do you want to say anything about either or both of these?
Marylia Gutierrez 00:05:32 This one, yeah, continuing with the declarity config, so I already got the set log provider and metric provider, now it's just a tracer provider missing to get merge.
Daniel Dyla (Dynatrace) 00:05:46 Okay.
Trent Mick 00:05:48 I have a question, Marilla, I'm probably gonna… This one, because this one's, I think, closer to being about configuration stuff.
Though I might be wrong, actually, because I didn't look at this one, I was going to look later. I probably have some bandwidth to help on… declarative config-related PRs?
Do you have a good suggestion on where to start, rather than… I guess I can just play with the existing config and look at all open PRs.
Marylia Gutierrez 00:06:15 Yeah, because I did… I have the project board… board, let me share here.
Okay, yeah. For these projects, and every time that I create, I have the column for, let me put it on the doc…
Trent Mick 00:06:29 I confide. I know it. Yeah. That's the only if we have that thing soon.
Marylia Gutierrez 00:06:33 Yeah, so basically because I have the columns, like, when I start creating stuff, I put it, like, on the backlog. I have a column for, like, ready to pick up, so you can pick up on… Any of those? So yeah, as long as they are not assigned, so…
Trent Mick 00:06:50 Okay, cool.
Daniel Dyla (Dynatrace) 00:06:52 We have one in progress, but not assigned. Is that on purpose?
Marylia Gutierrez 00:06:56 So, yeah, because, like, Mike, he was doing the first one, and then there's actually another person that was just starting doing this without realizing there was an issue for it, so I actually commented on… I cannot assign to the person, because they did not comment on the issue, so that I actually… ask them to, like, can you just comment on the issue so I can assign you? So I'm just waiting for them to comment, and I can just officially assign them.
Daniel Dyla (Dynatrace) 00:07:21 Got it, okay.
Marylia Gutierrez 00:07:29 And the other is the one that I brought on one of the channels of… some things that I found. So yeah, this is just, like, adding extra checks for… Just in case of… Not safe, objects coming, so just checking the type.
Daniel Dyla (Dynatrace) 00:07:48 Got it, okay.
Okay.
Carlos… Looks like, Carlos, you are on the meeting. Do you want to… Talk about this real quick?
Carlos Alberto Cortez 00:08:07 Yeah, just for your information, I will be filling issues. I started doing the reviews, as in the previous week, you were talking, you all, about, requesting, sometime soon, some TC review. So, just for information, I will be doing some, pre-review, let's say, you know? I hope that's fine, in case you see me feeling issues and all that.
After that, whenever this group is ready, we will probably ask for a second or an actual review from somebody else at ATC.
I hope that's okay.
Daniel Dyla (Dynatrace) 00:08:44 Yeah, it works fine, I think. I mean… We're never gonna complain about… having a TC group looking into whether we're doing things right.
Trent…
Trent Mick 00:09:02 Yeah, so, one of the… issues on the milestone for stabilizing the logs API and SDK was, What to do with the special log attributes type that we have, because… Since… attributes for log body, and… or sorry, since the type for log body, the any value type.
Was added, and then attributes on log records were allowed to have wider types than what attributes had initially been restricted to.
Since then, the spec now allows this… extended or more complex attributes types on, like, span attributes and wherever attributes appear in the… in the spec. So… specifically for stabilizing Logs API SDK, the request had been, do we want to rename log attributes to something else? But… I had been considering or looking at seeing if we could As part of the same work, given that we're gonna be… moving API logs into the API, look at having this… we're doing the support for the other signals as well, so basically, seeing if we can get span attributes and metrics attributes and attributes on The rarer things, like, on, Instrumentation.
Daniel Dyla (Dynatrace) 00:10:36 resource and events and stuff, yeah.
Trent Mick 00:10:37 And a resource, right? Yeah, yeah. Getting those, supporting that. And so, like, initial… feedback from Mark on… So, sorry, when… when extended attributes or more complex attributes were added for all signals, Robert, I'm not sure what his last name, who works mostly on Go side things, had to open to PR to look on every one of the languages, asking for feasibility of whether, like, will it be okay for you guys to look at implementing this? And Mark's initial response had been, yeah, but I think it'll be a breaking change, so they did, in the API, he was suggesting, so that the only way to do this would be to… Sdk, fine, we can do a major rev, so if we need a breaking change there, we can do that, but, API, not so much. So… the history… Mark's initial… Sense was that we would add a different attribute type.
And then… I'm not sure exactly what happens next on the APIs, if you want to do that. My… my… Gut reaction is that we're just widening the type, and could we get away with… Just widening the existing attributes interface that we have.
And not consider that a breaking change. For users.
The one problem is, is that, theoretically, you can always come up with a situation where, for implementers of SDK components.
specifically, I guess, third-party ones, so if there's a third-party… span processor, or a sampler, or something like that, that… and samplers receive span attributes. If they get attributes that are a wider type than what they'd coded to, then technically they could be broken there. Is that something that we want to consider a blocker on being able to expand the attributes interface. So, anyway, this draft PR is a… not complete, I haven't done any of the tests, other than just playing with it separately, but gives a sniff at what widening the attributes type would look like.
It updates all of the… SDK components that live in the core repo.
And widens the type. I'm curious what people's thoughts. It's… it's a little bit hard to go just spend 5 minutes and give feedback on it. You need to think about it and play a bit, so I realize it's a big ass, but anyway, so this is kind of the first bush showing that.
Daniel Dyla (Dynatrace) 00:13:06 Yeah, I mean, I know in the past we've said… Changes that are… like, we consider the breakingness of a change to be for end users, not for implementers. That's why we told, like, Datadog, for example, to cap the… Yeah.
the API version that each SDK supports, and to release a new SDK when the API is updated.
I understand the argument of… That's also… Like, for end-user components like spam processors?
But… One, I would say that's also kind of an implementer concern, like, more of a power user concern… But two… I think that's more of an SDK concern than an API.
I mean, we reused the type, which kind of backs us into a corner there.
Trent Mick 00:14:09 I used which type?
Daniel Dyla (Dynatrace) 00:14:11 we reused the… the attribute type. Like, when… when… If you release an API with an updated attributes type.
then any spam processors that import it from the API will get the newer type. It's not like they're importing it from, like, an SDK type's… Import path.
Trent Mick 00:14:36 I mean, so, like, an earlier play at this, which I haven't published a PR for at all, is having an interface extended attributes, or whatever name you want to give to it, it's a different one.
And then… new things, depending… having a minimum API version could use that type, but other SDK things that want to keep working with older API versions could copy that type into the SDK, so they could have an equivalent one that… I think passes type checking, because it's an equivalent type, just copied. But… I'm not sure what you do with some AP… I don't know. Do you turn every API… into… it can accept attributes or extended attributes, and then do you not have the same problem in implementer? So I'm not… I'm not sure if there is an answer without… effectively widening the type in all of the APIs. So, like, when you span.set attribute.
For example, do we need to add a span of set attribute 2, or something like that, that now accepts extended attributes? And, oh my god, how painful is… Is that process, so I don't know.
Daniel Dyla (Dynatrace) 00:15:46 Yeah.
a… I don't know either. I would prefer not to do that.
Which.
Trent Mick 00:15:55 like, I'd started going there, and I'm like, if I just hit, and then if we just widen interface attributes, can we accept that there might be… I don't know, like, who knows the numbers? It might be zero.
Daniel Dyla (Dynatrace) 00:16:12 Yeah, I was trying to think of suggestions.
Trent Mick 00:16:15 SDK complaints.
Daniel Dyla (Dynatrace) 00:16:17 breaking. The only thing I can think of is, like, a spam processor that is iterating through all of the attributes.
And then also taking some action on it that is dependent on the type.
you know, I don't know, maybe they're stringifying or something like that, but they have, like, some switch case, or, you know, if statement that's like, if it's a number, do this, if it's a boolean, do that.
Trent Mick 00:16:41 Yeah, Mark showed me…
Daniel Dyla (Dynatrace) 00:16:43 Right?
Trent Mick 00:16:44 Mark showed me a theoretical breakage in, type checking, so in comp… or transpiling step for people, where, someone was using attributes type, and they were using Oh, David, we were talking about this, what's the… what's the TypeScript term? The type… .
David Luna Bistuer 00:17:04 possession.
Trent Mick 00:17:06 Wait, type assertions, which… that's… but what's… what does TypeScript call it? Type…
David Luna Bistuer 00:17:12 Another one, yeah.
Trent Mick 00:17:13 Type narrowing, there you go.
Well, if someone had this function that's handling an attribute coming in, and they say, okay, well, it's… I've asserted it's not a Boolean, it's not a thing, the only types left are this one, and the rest of your code assumes that it's that type now, and that's what TypeScript thinks it is, but that code breaks now as soon as the type changes to support more types, you need a bigger if-else block or switch statement, or something like that. So, that can break the types. I'm not sure I want to worry about that being a breaking change. Like, people shouldn't be splitting apart and doing the attributes.
Yeah, that's a little…
Daniel Dyla (Dynatrace) 00:17:44 really esoteric break.
Trent Mick 00:17:47 I mean, it's there if you get in general, but, like, that's also in… sometimes, I feel, is in the realm of, like, any bug also breaks.
Daniel Dyla (Dynatrace) 00:17:55 people.
Trent Mick 00:17:55 Sometimes, any time you do a bug fix.
This clearly is not a bug fix, it's adding a new feature.
damn, what was this thing I wanted to say? The… the little looking I did look in other implementations, I was looking at DDTrace and Datadog, because they had been… One of the users that was broken earlier.
where we were careful. And the only uses of attributes that I see for them, they are using the sanitize attributes export from the core.
module.
But a thing that would change there is that the… the… that function, or a renamed one, or whatever from core would now pass through More attribute types, because the type has widened, so… I didn't really get a sense whether that was gonna have an impact on them.
I mean, I suppose there's always the downstream things, right? Like, OTLP is going to accept more types coming through, so… who knows on the receiver side.
Daniel Dyla (Dynatrace) 00:18:54 Yeah, I think exporters are where you're most likely to run into problems, but the most likely problem you run into is that the attributes dropped entirely, right? Like, you're iterating over attributes and serializing them. It's not one that you… You know, it's like, if it's a number, you encode it as a var int, if it's a string, you encode it as a, you know, in bytes, and then… Have a no fallback case, right? And it just gets dropped.
I think that's what would happen with our current exporters, which is… Fine, but… Yeah, the risk is that that happens, and people don't notice, necessarily, or…
Trent Mick 00:19:44 But I mean, if anything, this would be new attributes in the world, so they're seeing telemetry that… they would have been dropping with or stringifying the type before anyway, so I don't know.
Daniel Dyla (Dynatrace) 00:19:54 It also relies on them using some sort of custom exporter.
Because we'll update our exporters, right?
Trent Mick 00:20:02 Yeah.
Yeah, that's true. And I guess the downstream, like.
collectors or whatever already are going to support this kind of type for the logging signals, so it's not an issue of breaking them there, unless they have some special only for spans separate from log records, and I mean, but whatever, that… that's not a JS issue.
Daniel Dyla (Dynatrace) 00:20:24 Yeah, the collector supports complex attributes, and has for a while. I don't know exactly how long, but… Yeah, downstream components, I think. You know, I don't know… Which backends have updated?
To build support, but that's, you know.
Not a problem for the SDK.
Trent Mick 00:20:44 I'll definitely want to give Mark a chance to reply to that.
Daniel Dyla (Dynatrace) 00:20:46 Excuse me.
Trent Mick 00:20:47 Hasn't had a chance, because he's… At the collab summit, obviously, this week, and I think last week he was off for a bit. So… This is not something I'm gonna rush through quickly, though it's something I would like to… Consider and decide on one way or the other before we do the… the logs API.
Stabilization.
Daniel Dyla (Dynatrace) 00:21:07 Yep, okay.
Trent Mick 00:21:08 I'm… yeah.
Daniel Dyla (Dynatrace) 00:21:14 Alright.
That was the last agenda item. We can go on to triage if nobody has anything else to raise.
Alright.
Untriaged bugs.
None.
Look at that. Untriaged contribib bugs.
Only one. Memory leak… Needs a reproducer… It looks like… I mean, it's not a reproducer, but it does look like… They may have narrowed it down to the exact thing that changed.
I think the reason this is showing up in untriaged Bugs is because we haven't prioritized it.
Trent Mick 00:22:31 Yeah, well, to kick the can down the road while we were waiting for a response. But then since then, some just… New user did… This is new, I hadn't seen this new post from last week.
Daniel Dyla (Dynatrace) 00:22:47 Yeah.
Doesn't seem to be happening with Express.
Or… So it's a combination of Express 5 and Auto Instrumentation 72.
Trent Mick 00:23:12 That PR changed from using the clothes event to the finish event was… At least for that user, was the… close event emitter already… Wait, 11 finished listeners added 2. Was there a bug in that thing where we're… So it looks like we're not using the finish.
Won't anymore.
Daniel Dyla (Dynatrace) 00:23:41 in here.
Trent Mick 00:23:43 So the, yeah, the PR that he pushed to is a PR that switched from using the finish event to the close event for… I remember for closing spans properly, in certain cases.
Daniel Dyla (Dynatrace) 00:24:04 I wonder if we were…
Trent Mick 00:24:05 More to go on now.
Daniel Dyla (Dynatrace) 00:24:10 There is no…
Trent Mick 00:24:12 How would that change have caused a warning for too many Finnish listeners.
Anyway, there's something to go on and try to repro now.
Daniel Dyla (Dynatrace) 00:24:26 Yeah… Looks like multiple people are running into it. They might be co-workers, I don't know.
Trent Mick 00:24:44 The… just the one thumbs up, honey?
Daniel Dyla (Dynatrace) 00:24:48 Yeah, like, this… this person and… this person.
Trent Mick 00:24:52 The two of them, yeah, okay.
Daniel Dyla (Dynatrace) 00:24:54 you know, we're both running into it, but we don't know if they're coworkers or anything like that. Like, they may be running into it together. I don't know if… Dank.
I think that's good enough for now.
Trent Mick 00:25:40 I'll try to re-approve with what he's showing, but…
Daniel Dyla (Dynatrace) 00:25:43 Yeah.
That was the only… Contrib untriaged.
Should we go to old PRs?
Trent Mick 00:25:56 And for a little bit.
Stop.
Daniel Dyla (Dynatrace) 00:26:20 Looks like this is still… Active, or revived, anyway.
Trent Mick 00:26:37 Yeah, where it was on last week, I think? He has been looking and trying to push some of this for it, so… that's good.
Daniel Dyla (Dynatrace) 00:26:53 We're skipping dependencies PRs when we do this, right? I haven't done this in a while, so I'm… I don't remember the process as well.
Trent Mick 00:27:02 There's not a hard process, but yeah, generally skipping.
Finance.
this and… I can't remember if it's another iRedis or Redis ones, there are a couple that are just… they're… probably decent PRs, just adding features that… Need a reviewer?
Daniel Dyla (Dynatrace) 00:27:24 As… Has conflicts. Mark tagged the component owners, I guess.
That's still… Situation is unchanged.
Trent Mick 00:27:36 Unfortunately, the situation, unless someone else is able to pick up.
Daniel Dyla (Dynatrace) 00:27:40 Yeah.
This is from October.
Trent Mick 00:27:49 Did Hector give a response in last week? Yeah, okay, so Hector's seeing it, they're following up.
Bing.
Because I think Hector and maybe Jamie will… have more time in the AI space, they might.
Daniel Dyla (Dynatrace) 00:28:06 Yeah.
Trent Mick 00:28:07 I'll pick this up.
Daniel Dyla (Dynatrace) 00:28:07 or… No response here in a month, I mean, they may…
Trent Mick 00:28:13 We have moved on.
Daniel Dyla (Dynatrace) 00:28:15 Yeah.
Unfortunately, that's what happens when peers don't get reviewed.
Trent Mick 00:28:21 Quickly.
Daniel Dyla (Dynatrace) 00:28:26 That's renovate, renovate.
Trent Mick 00:28:28 So, skip those two. Mark was gonna look at… distribution.
Daniel Dyla (Dynatrace) 00:28:32 The CI, like… The CI, too?
Trent Mick 00:28:34 Yeah, they're both related from the same person, talking about changing our renovate config.
Daniel Dyla (Dynatrace) 00:28:39 Okay.
More dependencies…
Trent Mick 00:28:43 There you go, that's the other one I was talking about, just an easier…
Daniel Dyla (Dynatrace) 00:28:48 Is it the other eye over this one.
Trent Mick 00:28:50 Maintenance, yeah.
Daniel Dyla (Dynatrace) 00:28:59 Looks like we might…
Trent Mick 00:29:00 It doesn't have to be the maintainers. Oh, did he?
Daniel Dyla (Dynatrace) 00:29:04 It will, in December.
Yeah.
Trent Mick 00:29:06 Yeah.
Anyone else to call?
Or listening to the recording, I'm sure lots of people do that.
Feel free to pick it up.
Daniel Dyla (Dynatrace) 00:29:19 Yep, just waiting on reviews.
Draft… Runtime node GC duration buckets configuration.
Looks like still has review comments that aren't addressed.
This is just updating tests.
Trent Mick 00:30:12 Oh.
Daniel Dyla (Dynatrace) 00:30:13 Yeah, you made a comment. It looks like he addressed your comment, so…
Trent Mick 00:30:18 That's on me. Which one was that?
Daniel Dyla (Dynatrace) 00:30:21 3329.
Yeah.
Trent Mick 00:30:35 Okay, that's meaningful.
Put it on my list again.
Daniel Dyla (Dynatrace) 00:30:48 draft… Draft… First time contributor, allow control over logged fields.
Log keys now accepts partial custom keys to use the.
Trent Mick 00:31:29 Correlation to mixing? Ugh.
Daniel Dyla (Dynatrace) 00:31:32 Yeah, I'm not sure I understand what they're trying to do here.
Log keys option now accepts partial custom keys.
And explicitly undefined values.
Is this, like, the difference between… A key that exists and has an un… and is undefined versus a key that… like, an object that is missing the key entirely?
Trent Mick 00:32:13 P.
Daniel Dyla (Dynatrace) 00:32:14 really distinct.
Trent Mick 00:32:14 Just from what he's saying.
Or is it his implementation that's doing something?
Oh, it's the… so the log keys thing that he's talking about is an existing feature of this instrumentation.
For saying which of… So, the… Back when logging… when the log signal was just the bridge, one of the… features for these instrumentation for log frameworks was to add fields to… That logging framework's output for… The current context.
Current async context.
So this… the trace ID, span ID, Trace Flags Fields.
And then… Instrumentation Pino was added to be able to do that.
Using standard names for those fields where standard was what was requested as… or suggested as fields in the spec.
And then this log keys feature was added so that you could have it use different field names, so if you wanted it to be trace.id or trace underscore ID, then you could do that there. And I think he's extending that feature so that you can say Don't add the key at all, just drop it.
I think.
Yeah, so if…
Daniel Dyla (Dynatrace) 00:33:53 Yeah, so do you…
Trent Mick 00:33:55 bookmarking.
Daniel Dyla (Dynatrace) 00:33:57 Yeah, so if you set the configuration log keys, where trace ID… is… undefined, this if check will be false, and it will not add the trace ID to the log record.
undefined or… Null . Yeah, he made them optional.
Trent Mick 00:34:22 And Pino's the only one that has this log keys thing, yeah. Bunion and one-stone ones don't have the feature.
Daniel Dyla (Dynatrace) 00:34:28 Yeah.
Setting it specifically, like, undefined is a little…
Trent Mick 00:34:35 Well, it's just not set, I think is what he's saying. Because that's what the… at least the type implies, by just putting… Good question.
Daniel Dyla (Dynatrace) 00:34:42 Well, no, because he's merging it with default log keys. This is, like, a shallow merge.
Trent Mick 00:34:50 Oh, so you have to set it undefined to…
Daniel Dyla (Dynatrace) 00:34:51 You have to send…
Trent Mick 00:34:52 Get out of there.
Daniel Dyla (Dynatrace) 00:34:53 specifically undefined. Yeah.
Trent Mick 00:34:55 Or cheat and make it falsy.
Anyways, I don't know.
the pass… I don't understand the pass log correlation and mix-in thing, though.
The injected trace context into that.
Basin functions.
Why do you want that?
Daniel Dyla (Dynatrace) 00:35:26 S log correlation to mix in.
I'm not… I think… this… And this is a separate feature from this. It looks like this is maybe… Two features being added.
He's also… got it marked as a fix here. I'm not sure that I agree with that, unless this is, like.
in the specification, but I don't think it is.
So he's got log keys, trace ID, span ID, yeah, specifically set it as undefined trace flags, and then trace flags is not set.
Trent Mick 00:36:17 I agree on the idea of using null as a more…
Daniel Dyla (Dynatrace) 00:36:21 It's pretty…
Trent Mick 00:36:22 Clear, the clearer indicator, yeah.
Daniel Dyla (Dynatrace) 00:36:24 Yeah.
Trent Mick 00:36:25 The… that reminds me of another thing, of a… kinda… question I wanted to bring up. So, any value? So, going back to the… Widening the attributes type.
I'm sorry, I don't have any, like, links to show or anything. The spec says… I don't think I opened an issue, I think I just made notes for, like, this is crazy, and what are we gonna do about it? This… the spec… Or any value talks about… empty values are now being allowed. So, in the old version of attributes, there were comments that if you pass in empty values, like null or undefined, the behavior's undefined. Like, don't do that.
or attribute values. But the new… the spec, written by a person, I think, whose main language is not JavaScript, said.
Empty values are now allowed, for example, and it would show examples of empty values in different languages, and so nil and go, I think. And then for JavaScript, it said null or undefined. So, the spec is implying that a valid value for an attribute includes null , which we can do, we can encode, that seems fine. Also includes undefined, which, to me.
is maybe scary, and we want to revisit whether we want to do that, because I think it's fairly common for, and I mean, there are existing usages, where people For convenience, create objects to pass in as attributes where some of them are going to be undefined because, you use the null ish coalescing or something like that.
so that you get an undefined value for something, or if they're just passing an object that was given to that function, passing it through, and it's undefined, and what you're expecting is that the serialization will not have those attributes if the value is undefined. So there, null or undefined. Do we actually want to be… Allowing attributes where the value is undefined.
I think that's a special JavaScript that's weird and actually has a name for something that Most commonly is interpreted as it doesn't exist as a property.
Though technically there are… it is different.
If, you know what I mean.
Daniel Dyla (Dynatrace) 00:38:52 Yeah.
Trent Mick 00:38:54 I really have to write this down in.
Daniel Dyla (Dynatrace) 00:38:56 issue.
Trent Mick 00:38:56 Yeah, I totally have to raise an issue, but just to remind people. Against the spec.
Daniel Dyla (Dynatrace) 00:39:00 When was this done?
Trent Mick 00:39:03 Like, last fall.
Through the winter. Three months ago, yeah.
I guess that's January.
Daniel Dyla (Dynatrace) 00:39:12 Yeah. Okay.
I mean… Yeah, it's an example, but… Are examples considered normative?
But it should probably be fixed. I agree, like, the difference between undefined and doesn't exist… while… technically it's there, I think, is a little bit too fine of a point to… I think only allowing null as a specific empty value is probably more than good enough.
Trent Mick 00:39:50 And so the log attributes type is… where is that defined?
Log record…
Daniel Dyla (Dynatrace) 00:40:01 I don't think there is a log attributes type anymore.
Trent Mick 00:40:05 No, no, well, there is currently in API logs.
Daniel Dyla (Dynatrace) 00:40:09 Oh, I thought you meant in the spec.
Trent Mick 00:40:11 Sorry, is… Oh, there's any value, so it's what the R type for any value is.
Source types, any value inside logs API.
includes null and undefined, so now I'm gonna be potentially proposing that we drop undefined from that set.
Which means that we definitely want to clear up that example in the spec, because it certainly looks confusing.
Daniel Dyla (Dynatrace) 00:40:37 Yeah, and that's specifically in the logs API.
Trent Mick 00:40:41 Yeah, source… Types any value.
That one.
Yeah. I'm not sure if our exporters or the transformer, actually.
Does carry that through, or if it just drops it.
Daniel Dyla (Dynatrace) 00:41:01 Yeah, I don't know either.
Trent Mick 00:41:02 So I'll investigate.
Daniel Dyla (Dynatrace) 00:41:04 Since Mark just wrote, like, a custom serializer, too.
So it's… I'm not even sure… If this is handled the same in the custom serializer as it is in, like, the default.
Trent Mick 00:41:18 And was it possibly done in proto, because… one looks at it differently, and not an adjacent serial… because it's the JSON serialized thing, it's gone.
Daniel Dyla (Dynatrace) 00:41:29 Yeah.
Trent Mick 00:41:29 They're adjacent to the Stringify, yep, so…
Daniel Dyla (Dynatrace) 00:41:34 Okay.
Good catch.
Anyway. I think it's… definitely is worth an issue.
Let's see, where did we get to?
And then C is I.O. Redis… I'm a certain… Draft, draft… Pino.
We're on Pino again. Avoid mutating user options.
Trent Mick 00:42:07 That's probably a good idea.
Daniel Dyla (Dynatrace) 00:42:09 Yeah… I'm not sure. The code that actually… is the offending code, I don't think is… this.
Because obviously something in the logger Must be modifying… options somewhere.
Like, this is…
Trent Mick 00:43:15 No, I think that's fine.
Daniel Dyla (Dynatrace) 00:43:16 Right, so what that.
Trent Mick 00:43:16 thing is doing is creating… so when you call the Pino function to create a pinot logger.
our wrapper needs to change the constructor options, or the args that are passed to that pino function.
To insert the hotel mix in as one of them, and I think that's the thing he's referring to.
That's the mix-in that will add the trace ID attribute if there is a current context.
And it looks like… Well, okay, so I know what you're saying. Yeah, something's mutating that arcsync, but…
Daniel Dyla (Dynatrace) 00:43:50 Yeah, something is mutating the args array.
like… in… You know, psh, maybe something… Down here.
Trent Mick 00:44:03 Wait, so that's just adding it there.
What is mutating marks?
Daniel Dyla (Dynatrace) 00:44:07 Yeah, I don't know, that's what I was saying. I think that the mutation code is somewhere else. It might even be inside Pino, for all I know.
Trent Mick 00:44:16 Huh.
Daniel Dyla (Dynatrace) 00:44:19 And this is just copying the array.
Before sending it to… You know, before passing it to the original function.
And it's even… check.
Trent Mick 00:44:33 No, it's…
Daniel Dyla (Dynatrace) 00:44:34 The first one is an object, then it's even copying the object also, but it's a shallow copy.
Trent Mick 00:44:54 Yeah.
What's going on?
Daniel Dyla (Dynatrace) 00:44:58 Right, if… if the… first argument is an object. It's copying the array no matter what.
But that's… this… Is already doing that.
This says if the first argument is an object.
also copy that object. So we're passing a copy of it.
Rather than… The original.
And this object must be what's being mutated somewhere.
But I don't know if we're mutating it, or if Pino is mutating it.
Trent Mick 00:45:42 this patch Pinot thing in Instrumentation Pino here, the code that you're looking at, doesn't touch that args… Variable anywhere, so… Feels like it's… Pretty subtle access, if it's… if our… if the instrumentation code is mutating it.
Yeah, you're right, it could very well be in Pino, because Pino's gonna… they're all about speed, they're gonna avoid copying.
Things.
Daniel Dyla (Dynatrace) 00:46:12 Yeah.
Trent Mick 00:46:12 They put the burden on the user to not… Have things that can't be mutated when you pass in multiple options like that.
Daniel Dyla (Dynatrace) 00:46:19 You create 3… bloggers…
Trent Mick 00:46:24 I wonder why 3 and not 2, but…
Daniel Dyla (Dynatrace) 00:46:28 And then does not throw.
I mean, to me.
this does seem, yes, obviously, this should not throw. If this test case is failing before.
Then this is obviously a bug fix, in my opinion.
But… it's not clear to me exactly what's being fixed, and I think this… test description… doesn't… answer my questions.
Like, it's… it's… The test says, does not stack mix-ins. We're not actually checking any mix-ins, we're checking if it throws.
Like, that the assertion doesn't match… The description, in my opinion.
I'm sure it's a good test, but… And then… I'll add a comment here, too.
Trent Mick 00:48:21 I had an issue.
Oh, no, they were replying to someone else's issue.
Which we'd already triaged.
Daniel Dyla (Dynatrace) 00:49:44 Active Resource Gauge… Is there… Yeah, Mary Leah's already on this one. Is… is there a semantic convention for node runtime, or…
Trent Mick 00:50:10 Yeah, there is… well, the separate one's for V8 and Node runtime. Which one was this setting to V8?
Which I think Marillier had shepherded.
this… Once instrumentation is being created.
Daniel Dyla (Dynatrace) 00:50:25 Yep, so it looks like there's a PR now for… The SEMCON.
I think this PR, you know, can be considered, like.
a prototype for that SEMCOM change, but… Should we merge it? Should we wait to merge it until the SEMCOM is merged?
I've seen a bunch of these where, or just while we've been looking at these today, where these checks are not finished.
Has anyone else seen these?
Or know what's going on here?
Normally.
Trent Mick 00:51:09 I could run off to status.github.whatever.
But it would have been at the time of…
Daniel Dyla (Dynatrace) 00:51:15 Yeah, it is.
Trent Mick 00:51:16 So when was this?
Yeah, 3 weeks ago.
Daniel Dyla (Dynatrace) 00:51:22 At least 3 weeks.
Trent Mick 00:51:24 So.
Daniel Dyla (Dynatrace) 00:51:25 Probably.
Trent Mick 00:51:25 of actions has been way less reliable than it's been… In the past. I don't know how to re… Trigger those, do you?
Daniel Dyla (Dynatrace) 00:51:35 You have to either… Push a change, or closing and reopening the PR.
We'll rerun them. Close… Reopen.
Trent Mick 00:51:56 Alright, and then approve.
To run.
Daniel Dyla (Dynatrace) 00:52:00 Yeah.
Trent Mick 00:52:02 I'll do that in a second, just looking at the code.
Don't see a Bitcoin miner, so… good.
Daniel Dyla (Dynatrace) 00:52:27 Okay.
Trent Mick 00:52:37 It looks like it's getting approvals, so…
Daniel Dyla (Dynatrace) 00:52:41 What, the SimConf PR, you mean?
Trent Mick 00:52:44 It had, and there was some action from last week.
Yeah, looks like Marilla's helping on that.
That looks like it's actually moving.
Daniel Dyla (Dynatrace) 00:52:57 PGPool release span… is… I don't know enough about PG and PGPool, but is release actually a message that Get sent.
Like, it's… Is it an operation with, like, time that justifies a spam?
Trent Mick 00:53:33 I don't know.
Daniel Dyla (Dynatrace) 00:53:44 I wonder if… There's some comp for this. There's an issue.
The issue doesn't mention any semantic conventions, though.
Can't hurt to just ask, right?
draft.
Dependencies…
Trent Mick 00:55:00 Do you want a couple?
Is that a promised interface from the Lambda extension?
Daniel Dyla (Dynatrace) 00:55:14 I don't know.
This is the same person, so it looks like he updated the Lambda extension to write this file.
And now he…
Trent Mick 00:55:36 then…
Daniel Dyla (Dynatrace) 00:55:37 dating… Our resource detector to read it.
Trent Mick 00:55:43 And he's done PRs… Or all the other languages as well.
Daniel Dyla (Dynatrace) 00:55:48 Has he?
Trent Mick 00:55:50 Yep.
They're all open the .NET one guy.
Closed.
Why did it get close? It just went stale.
Daniel Dyla (Dynatrace) 00:56:20 Yeah, I mean, it looks like… He's pulling the… a field from the SEMConv package, so, like, it's definitely a field that exists.
probably wasn't being gathered before…
Trent Mick 00:56:47 I vaguely recall in LambdaLand, there were some things that weren't available Until…
Daniel Dyla (Dynatrace) 00:56:53 Until the first request.
Trent Mick 00:56:55 Right. I don't know if this is one of those, though. But then I see this comment on the .NET one… Which, I'm not sure that that's… Adopt to comment.
Saying that it's… that the AWS access key ID in FAR is always available, beginning?
Use that to account.
We calculate the account ID. Which means that all of this other work shouldn't be necessary, I guess, if that's… Truly the case.
Okay, and then someone questioning whether that's a reliable promised interface from AWS.
Daniel Dyla (Dynatrace) 00:57:49 it's not promised from AWS.
This is when you register… when the extension registers, it gets an account ID. So that is promised.
The writing of the file is done by… the extension.
Trent Mick 00:58:08 which was added in February.
With no documentation, though.
Daniel Dyla (Dynatrace) 00:58:12 With no… yeah.
Trent Mick 00:58:14 I don't love that.
Daniel Dyla (Dynatrace) 00:58:17 And it just, you know… It's undocumented, but it does seem…
Trent Mick 00:58:24 It has a test.
Yeah, it gets written.
on Tempter.
Daniel Dyla (Dynatrace) 00:58:33 I guess, maybe it's worth asking.
Is there any…
Trent Mick 00:58:42 Worry Pressers was on that.
W… Sorry, not pressors, pessers.
And he'd been active on the SQS-related one.
Daniel Dyla (Dynatrace) 00:58:57 Yeah, I've seen him around.
I don't know who this person is, but… dash zero.
I think the answer is likely that this will be merged. It seems like a decent idea to me. It's better to… You know, if you can get the account ID at startup for resources, clearly that seems like an improvement, versus waiting for the first request to come in.
I think it's just…
Trent Mick 00:59:36 I'm weak on my Lambda flow. Does the Lambda extension register call always happen and complete before.
Daniel Dyla (Dynatrace) 00:59:45 I do not know.
Trent Mick 00:59:47 the JS code for the handler starts.
Daniel Dyla (Dynatrace) 00:59:49 I do not know.
Trent Mick 00:59:52 Okay.
Daniel Dyla (Dynatrace) 00:59:53 of ice… Yes.
I think…
Trent Mick 00:59:56 You guys seen a scoop.
Daniel Dyla (Dynatrace) 00:59:56 Must.
Trent Mick 00:59:58 Defend well, but… okay.
Daniel Dyla (Dynatrace) 01:00:05 But I don't see… Any links to, like, specification or…
Trent Mick 01:00:12 So, I mean, yeah, that's the thing I would like. I would like a doc entry on the… in the Lambda repo where the extension's built, and then have a link a comment with the URL link to that doc where… Right.
Where this…
Daniel Dyla (Dynatrace) 01:00:26 As long as they document… As long as they document, like, if you use this extension, the file will exist before your application starts.
Then, if the feature breaks, it's on them.
Trent Mick 01:00:40 Yeah, and this already just… Has a try-catch, so, like, that would be totally fine.
Daniel Dyla (Dynatrace) 01:00:45 Yeah.
Trent Mick 01:00:46 Okay.
Daniel Dyla (Dynatrace) 01:00:47 Cool. And I added a comment, so… We'll see where that goes.
My guess is just… Looking at the people who are… Involved in this?
it is… Probably… Reasonable.
But… I'd like some… some written-down guarantee somewhere.
Cool.
Yep. We've got 5 chat comments. People saying they're leaving… Yes. Okay.
Should be all good.
Trent Mick 01:01:30 Thanks for driving.
Daniel Dyla (Dynatrace) 01:01:32 Yeah, no problem. See you next week.
Trent Mick 01:01:35 Gotcha, yeah.
David Luna Bistuer 01:01:36 But…
