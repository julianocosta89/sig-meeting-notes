SIG: Resources and Entities SIG
Date: 2026-08-03
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Josh Suereth (Google LLC)** 00:51 How are we all doing?
**Daniel Dyla (Dynatrace LLC)** 00:56 Doing okay. A little tired from the weekend, you?
Muted.
**Josh Suereth (Google LLC)** 01:05 Coming back from a week vacation, I still haven't finished my email.
And, also super tired, because I… yeah.
it was, I ruined my sleep schedule, like… My daughter wanted to wake up and see the sunrise at the beach, so we did.
And then I made the mistake of changing when I went to bed, and, like, shifting my entire sleep schedule, and so now I do not want to be awake. This is nap time.
Ugh.
**Daniel Dyla (Dynatrace LLC)** 01:37 I had the opposite problem. My brother wanted to stay awake to see the sunset, seemingly, so…
**Josh Suereth (Google LLC)** 01:44 Oh.
**Daniel Dyla (Dynatrace LLC)** 01:45 To see the sun rise. We were up pretty late all weekend, so, I'm just tired, I'm a little out of it.
**Josh Suereth (Google LLC)** 01:55 Yeah, yeah. I think you can go either way, depending on where your current circadian rhythm is, you know?
Yeah.
Anyway, let's, let's begin. I have to drop at, 1.
My time, which is in 25 minutes.
**Daniel Dyla (Dynatrace LLC)** 02:15 In half an hour, yeah, that works for me, too, as well. I don't see anything on the agenda anyways. I assume we'll just talk about the ongoing work that we talked about last week, but…
**Josh Suereth (Google LLC)** 02:26 Yeah, were you… were you here when we talked about some of Robert's concerns around,
**Daniel Dyla (Dynatrace LLC)** 02:31 I was.
**Josh Suereth (Google LLC)** 02:32 Yeah, yeah, okay, and I know that you guys talked about this in spec meeting, so what I… I was looking… I was trying to catch up… I was reading before here, like, the two spec PRs, so I want to go through them.
Because yours, I don't think, has enough attention.
And then, mine got a little too much attention.
Okay, so let's do… that's me…
**Daniel Dyla (Dynatrace LLC)** 02:56 Yeah.
**Josh Suereth (Google LLC)** 02:56 Let's do it.
**Daniel Dyla (Dynatrace LLC)** 02:57 I think the… the entity URL stuff was a little bit tied to questions about the… the breakingness of the change, too. In the spec meeting, we talked about it, and… So, my original point was why make it opt-in? Because, like, the… the breakingness, you know, it implied breaking, I don't know.
And the answer was that it was related to schema URL. We talked about that in the SEMCON meet… er, in this meeting.
Yeah.
And I think we came to the conclusion that We should just… allow implementations to keep whatever schema URL behavior they currently have for the top-level schema URL and mark it as deprecated.
and then use the Entities schema URL for new validation features and things like that with Weaver. Does that match what you remember?
**Josh Suereth (Google LLC)** 04:06 The only concern I have… is… there are… there… you are allowed to actually not merge on schema URL differences at the top level.
And I want to start merging those things, and so we need a behavior for when you… Mergers that were previously not allowed are now fully allowed. Sorry, they were undefined behavior before.
**Daniel Dyla (Dynatrace LLC)** 04:29 Yeah.
**Josh Suereth (Google LLC)** 04:30 And now they're allowed. And I don't want those to be broken, because I think that would be… like, that's one of the things we want to fix, is that behavior was broken before. We think that's a bug.
Right?
**Daniel Dyla (Dynatrace LLC)** 04:41 Yeah, to me, it seems like any merge where all schema URLs do not match should Clear the top-level resource schema.
**Josh Suereth (Google LLC)** 04:53 100%, 100%, but… The nuance there was where schema URLs are empty, What do you do?
**Daniel Dyla (Dynatrace LLC)** 05:02 That's not match.
**Josh Suereth (Google LLC)** 05:04 I agreed, but that's the argument I had with Robert. He doesn't agree with me.
So, and I think Splunk might be relying on that behavior, so it's unfortunate that Dimitri's on vacation here.
Because he pointed at the Splunk distribution of OTEL for Go, I think?
that had some behavior that was doing stuff with resources that they don't want broken. And I was like, well, with the new thing, it wouldn't be broken, you just won't have schema URL and resource. And they're like, okay, but we need it in resource. I'm like, but… It's broken in real… like, you literally can't trust it.
So, but apparently they're using it.
**Daniel Dyla (Dynatrace LLC)** 05:39 So what behavior are they depending on? If you merge a resource with no schema into a resource with a schema.
**Josh Suereth (Google LLC)** 05:47 they won.
**Daniel Dyla (Dynatrace LLC)** 05:47 They want it to be retained.
**Josh Suereth (Google LLC)** 05:49 They want to retain it, yeah.
They want to treat note schema as I have no preference, not as I didn't bother to specify something, and I don't know if I conflict.
**Daniel Dyla (Dynatrace LLC)** 06:00 I guess I see that either way. I don't think that's what the current behavior is of all of the SDKs.
**Josh Suereth (Google LLC)** 06:06 No, and there's a whole bug about it, yeah.
Shut up.
**Daniel Dyla (Dynatrace LLC)** 06:11 If they're depending on it, it's not… yeah, okay.
**Josh Suereth (Google LLC)** 06:14 So… Basically, if I can get the TLDR of what you're proposing… We don't need this at all. We can just start adding entities.
**Daniel Dyla (Dynatrace LLC)** 06:24 Yeah, so this is…
**Josh Suereth (Google LLC)** 06:26 break first.
**Daniel Dyla (Dynatrace LLC)** 06:27 You weren't in the spec meeting, but we talked about this… flag specifically. Yeah. The argument for including it for, Jack… Was that it enables… Protocol-level feature that's not stable.
And what we talked about on the call is that we've done that in the past. Like, when we added fields, we haven't added, new flags for them.
They… I think everybody agreed we don't need this flag for that reason.
as long as we guarantee, if we ever break this feature, we use a new, field number, which I think is…
**Josh Suereth (Google LLC)** 07:11 we already agreed to, that's in, like, in the proto-specification, that's how we added this to begin with, of, like, these things, if they go away, they're… That number's gone, yeah.
**Daniel Dyla (Dynatrace LLC)** 07:21 Right. So, given that, I think people were fine with having entities enabled by default.
**Josh Suereth (Google LLC)** 07:30 Okay?
**Daniel Dyla (Dynatrace LLC)** 07:32 the schema URL thing, we did not, talk about or… or resolve. So that may require this flag for that reason, but it's… Without Dimitri or Robert, I don't know that we can even…
**Josh Suereth (Google LLC)** 07:47 We should probably talk about it at the spec meeting tomorrow. I need to check if I… If someone scheduled something over the spec meeting tomorrow, they did, but I can skip. Okay.
I will be at the spec meeting tomorrow. I'll… we'll put it on… I'll put it on the agenda now.
let me open up the meeting notes.
And… Where am I presenting, man?
**Daniel Dyla (Dynatrace LLC)** 08:15 you're… heh.
I see my comment on your PR right now.
**Josh Suereth (Google LLC)** 08:20 Yeah.
Do you think this is a 5-minute or 10-minute conversation?
**Daniel Dyla (Dynatrace LLC)** 08:27 I think it's probably… 5.
**Josh Suereth (Google LLC)** 08:33 Okay 5 minutes, Josh, and then I'll put a link to, Schema Bureau, behavior, let's… I can tell you.
**Daniel Dyla (Dynatrace LLC)** 08:45 Type up, like, a summary, I guess?
of…
**Josh Suereth (Google LLC)** 08:50 Please do.
**Daniel Dyla (Dynatrace LLC)** 08:51 Just so that we… so that we can… Have a more tar… keep it to 5 minutes, probably easier if we have a summary that keeps the conversation a little bit targeted before we start.
**Josh Suereth (Google LLC)** 09:03 Oh yeah, if you, if you want, here's the, the meeting notes for tomorrow.
I'll put, I'll put both of us.
**Daniel Dyla (Dynatrace LLC)** 09:10 Okay.
**Josh Suereth (Google LLC)** 09:12 Cool.
By the way, I always feel weird, like, you go by your full first name, right?
**Daniel Dyla (Dynatrace LLC)** 09:18 As you know.
**Josh Suereth (Google LLC)** 09:20 You do not, you go by Dan.
**Daniel Dyla (Dynatrace LLC)** 09:21 I go by Dan.
**Josh Suereth (Google LLC)** 09:23 I prefer to call you.
**Daniel Dyla (Dynatrace LLC)** 09:24 Work things… work things are converging on Daniel because we have various internal, like, LDAP reasons that I can't use Dan on, like, things like email and Slack and things like that, so all my coworkers tend to call me Daniel. It seems like this automatically named me Daniel.
It is what it is. I don't worry too much about it, but most people call me Dan.
**Josh Suereth (Google LLC)** 09:46 Okay, good, good, good. My, my brother-in-law… his mom forces everyone to call him Daniel in front of her.
Even though he's, like, you know, 20-something.
And then he goes by Dan when she's not around, so I wasn't… like, I just didn't know. That's all. Okay. Alright.
Let's do, let's get back to the PR.
**Daniel Dyla (Dynatrace LLC)** 10:14 So, the question will be, like.
I mean, if we have to change the behavior anyway, do we treat it as a… like, current implementations don't match each other. Do we treat it as a bug and make them all match? Do we treat it as legacy and say, continue doing what you're doing?
**Josh Suereth (Google LLC)** 10:31 The good news is there's already a bug, so… okay, we have this here. Is there anything else new here?
No. What did we call this? We call it… let's look… if we just look for schema URL, I think there's a set of bugs around it, which messages schema URL applies to. I should actually just fix that. Resource merge area. This is from 2023, which is one of the issues we originally took on.
That led to the formation of this SIG, right? This is, like, one of the founding issues that we took on.
Our merge algorithm is supposed to solve this, but this is the issue.
And then, recently, 2 weeks ago, Robert did a thing where he looked at all the different implementations and what the current behavior is.
**Daniel Dyla (Dynatrace LLC)** 11:19 This is the current behavior if you merge… a schema URL… an empty schema URL into a non-empty one, right?
**Josh Suereth (Google LLC)** 11:29 I believe that's the case, yes.
Yeah, so, like, PHP returns all the attributes merged and null schema URL, which is what we're proposing.
Right.
Rust does the same thing, no scheme your own muller, you know, they don't have… Yeah.
**Daniel Dyla (Dynatrace LLC)** 11:46 Whether it's null, empty string, or undefined, some empty.
**Josh Suereth (Google LLC)** 11:51 This is where things are problematic. Python followed the spec and returns the old resource and discards the new one, which people hate.
**Daniel Dyla (Dynatrace LLC)** 11:58 Oh, they just don't even merge.
**Josh Suereth (Google LLC)** 12:01 Yeah, like, like, people hate that. That's, like, the worst of all behaviors. Like, this is one where abiding by the spec was bad. So… the C++ does, merges and keeps the resource gimmele of the.
**Daniel Dyla (Dynatrace LLC)** 12:16 the newer one.
**Josh Suereth (Google LLC)** 12:17 Yeah, Ruby and Swift just don't have a scheme URL at all.
**Daniel Dyla (Dynatrace LLC)** 12:22 Okay, so what is…
**Josh Suereth (Google LLC)** 12:23 Okay.
**Daniel Dyla (Dynatrace LLC)** 12:24 What is Splunk depending on?
**Josh Suereth (Google LLC)** 12:27 the… this go behavior, I think. They return normally merged attributes with an empty schema URL, the caller may use resourced, detect keeps the URL empty if any conflict occurred in the detector chain, and they just recently introduced this.
**Daniel Dyla (Dynatrace LLC)** 12:41 Yeah, so that's empty.
Yep, that's clearing, yeah?
Java clears it.
**Josh Suereth (Google LLC)** 12:48 Java clears it and sends it to null.
Erlein also sets it up.
**Daniel Dyla (Dynatrace LLC)** 12:52 Yeah.
**Josh Suereth (Google LLC)** 12:54 net, return to… yes, that's a denull.
**Daniel Dyla (Dynatrace LLC)** 12:58 Yeah, so literally only Python.
**Josh Suereth (Google LLC)** 13:02 Only Python did…
**Daniel Dyla (Dynatrace LLC)** 13:03 Python follows the spec.
And only C++ retains the schema URL.
**Josh Suereth (Google LLC)** 13:10 And…
**Daniel Dyla (Dynatrace LLC)** 13:11 What is Splunk depending on?
**Josh Suereth (Google LLC)** 13:13 I think Splunk has a custom behavior in their Go contribute thing or something.
let's see, where was the… there was a… there's a link in some thread in some conversation with Robert on this. He and I had a big back and forth, you can read about it, where I'm like, you know, I disagree, but let me just try to give him some rationale here, right? So what he wants is… His proposed change is that we replace the final schema URL and merge with, the SDK should return a resource above whose schema URL is empty, but it should make conflict observable and may retain current behavior for backwards compatibility, but he also wants to do this when you merge You should not assign an empty SKU URL unless the implementation can establish that the URL applies to all attributes in the resource. This is… these are all shoulds.
So the specification here is actually fine, but then what he wanted to actually implement was different.
So, yeah, reasoning. Empty URL is safe representation. So, if you… an empty URL makes no claim that it has a schema, is what he's saying.
No, that's not what he's saying here. Interesting. Square conflict should not discard otherwise useful data. Yes, that is… this is… this is, I think, the number one thing we want to fix, which is why we have entities with different schema URLs, so we don't discard things when there's conflicts.
Error reporting must remain language neutral. Compatibility allowance is necessary. Resource SDK is stable. Python SDK have established materially different behavior.
**Daniel Dyla (Dynatrace LLC)** 14:54 You know, this…
**Josh Suereth (Google LLC)** 14:55 This one doesn't seem to be real different.
**Daniel Dyla (Dynatrace LLC)** 14:58 This reads very AI-coded to me, it's kind of hard to read.
**Josh Suereth (Google LLC)** 15:02 Yeah, there's a better thing here, so this is what he wants.
Doing this before Entities… he wants to fix this before Entities, like… Launch, or land, or stabilize.
it merely postpones the same change and bundles it with later entities. Yeah, like, I kind of… he blocked my PR, by the way, so I'm, like, not really sure…
**Daniel Dyla (Dynatrace LLC)** 15:30 I'm so hard to tell what he's even saying here.
**Josh Suereth (Google LLC)** 15:33 I… yeah.
We should probably just talk about it at the spec meeting. This is where… oh, here we go. Schema yell, when it exists, should accurately describe a resource and be safe to use for validation performance tests in Weaver. This is what I said. This is what he doesn't agree with.
Like, everything else we agreed on, this was the only thing I said that, because I was trying to rephrase what he said, right? Here's what I hope we agree on. We should treat empty ski URL as an unknown schema, not, I don't care, it's safe to merge.
Right? So it's just… it's an unknown one, meaning there is a schema, I just didn't bother to write it down or pay attention.
But there is something.
We should allow resource merges across schema differences, generally, because we know that we need to, right? So the existing algorithm is way too rigid, we should allow those merges. SchemaReL, if it exists, should accurately describe a resource and be safe to use for validation and conformance tests.
**Daniel Dyla (Dynatrace LLC)** 16:31 Okay. That is…
**Josh Suereth (Google LLC)** 16:33 This is the point that I think he disagreed with.
**Daniel Dyla (Dynatrace LLC)** 16:36 Yeah, he makes an incorrect assertion.
I don't know, I don't remember exactly where it says, but he says that the new entity merge has the… the behavior of treating… the schema URL as I don't care.
And it doesn't.
Any blank… any blank schema URL in the entity merge drops schema URL.
It treats it as unsafe.
that he makes the opposite assertion here, somewhere.
**Josh Suereth (Google LLC)** 17:11 So, we'll have to look at that. This is the other… this is the link here, by the way. This… this is the… signal effects go distribution that he was worried about, where they have this notion of schema-less resources that they merge for the distro that they don't want to be dropped.
**Daniel Dyla (Dynatrace LLC)** 17:29 But if it's schema-less, that's fine to retain the attributes, but you drop.
**Josh Suereth (Google LLC)** 17:33 Yeah.
**Daniel Dyla (Dynatrace LLC)** 17:33 It is schema-less. Yeah.
**Josh Suereth (Google LLC)** 17:35 like.
Doing this means the schema URL gets dropped all the time from whatever Go is doing, which, again, that's literally what you're doing, though. Like, you're…
**Daniel Dyla (Dynatrace LLC)** 17:44 So… I see. Yeah. Because they are adding attributes, so what they're… this will drop the schema URL no matter what.
**Josh Suereth (Google LLC)** 17:55 no matter what, until they start using entities, and entities are unstable part of the spec, so the only way they could figure out that schema URL exists for the resource and is useful is by… Got it.
So that's… that… this is, I think… like, I think they're actually using the resource schema URL, even though it's broken.
Today, and like, this… this… again, if we were to use the schema URL and resource in Weaver for this, this would fail validation because these are unexpected in the schema URL, possibly.
**Daniel Dyla (Dynatrace LLC)** 18:27 Yeah, and the… the… Current state does not work for them, because… So that's what they… that's what they want to change. They want to change the current behavior to retain schema URL. Okay. Yes. I have a different proposal, we can talk about it tomorrow, we're already, like, way through our time.
But I would say that we can have a special case, like, star schema URL that does not You know, that's like… I am not changing, like, you know, to force the behavior, or something like that.
**Josh Suereth (Google LLC)** 19:03 Yeah, for, they're schemaless.
Goodness.
**Daniel Dyla (Dynatrace LLC)** 19:11 Yeah, and it would only…
**Josh Suereth (Google LLC)** 19:14 code implementation.
**Daniel Dyla (Dynatrace LLC)** 19:16 It would… it would work by… like, the detector, the new resource, if it has star, it will not change the old resource.
That's all… that's all that I would propose.
**Josh Suereth (Google LLC)** 19:35 Old resource, yep. Okay.
**Daniel Dyla (Dynatrace LLC)** 19:37 Yeah.
**Josh Suereth (Google LLC)** 19:38 Let's talk about that in the spec and go there. We have, like, 9 minutes left. I think you made changes here, and I didn't actually have a chance to read through them. Were there any updated comments?
Oh, just, is there a prototype?
**Daniel Dyla (Dynatrace LLC)** 19:53 Yeah, I mean, it matches the Java prototype, there is a JS prototype, and we relaxed the wording here, so the old prototype still works just fine.
**Josh Suereth (Google LLC)** 20:06 Yeah, so I think we just need to list them annoyingly.
The observed entity for which telemetry is being produced for which Entities. This is just… Rephrasing… that's rephrasing. You call out entities, which I don't think we called out before, right, in the… SDK spec.
Like, I don't know if I… I… I thought when I made the bare minimum thing, we actually called out Entities, but I guess I didn't, did I?
**Daniel Dyla (Dynatrace LLC)** 20:37 It was definitely not there when I wrote this, but this has been sitting for a long time, so it's possible it's there now? I don't think it is, though, hold on, let me look.
**Josh Suereth (Google LLC)** 20:45 Gross.
**Daniel Dyla (Dynatrace LLC)** 20:45 or SDK.
**Josh Suereth (Google LLC)** 20:47 Yeah, let's just take a look, because, you know…
**Daniel Dyla (Dynatrace LLC)** 20:49 There is not an Entities heading in Resource SDK.
**Josh Suereth (Google LLC)** 20:53 And, oh, you need to merge to latest.
I don'.
**Daniel Dyla (Dynatrace LLC)** 21:00 Nope, okay.
**Josh Suereth (Google LLC)** 21:02 Yeah, it was merged sometime recently, hold on, open to.
**Daniel Dyla (Dynatrace LLC)** 21:05 Yeah, like, sometime last week, I think.
**Josh Suereth (Google LLC)** 21:07 Yeah, like, while I was on vacation, I think it got merged. If we look at resource SDK, and there's no header with entities.
So…
**Daniel Dyla (Dynatrace LLC)** 21:18 There is, in the merge behavior, it mentions behavior with entities.
**Josh Suereth (Google LLC)** 21:23 And here it mentions Entities, but we don't actually call out what the hell an entity is, so I think it's a good addition that you have it, and I can't believe we missed it in this spec BR.
**Daniel Dyla (Dynatrace LLC)** 21:34 Okay.
**Josh Suereth (Google LLC)** 21:35 But you should merge and make sure that we don't have, like, conflicts, and that this links to what you have, right?
**Daniel Dyla (Dynatrace LLC)** 21:41 Yeah, I'll resolve the conflicts.
**Josh Suereth (Google LLC)** 21:43 Yeah, yeah. Okay.
Cool, and I don't think there were any other… Yeah, because this… this… I had already reviewed the Entities section, and that looked good.
**Daniel Dyla (Dynatrace LLC)** 21:53 Yeah, nothing's all that different. The only thing that we changed was the wording around the async.
behaviors, because I had, like, must resolve synchronously, which was not…
**Josh Suereth (Google LLC)** 22:08 Oh, this right here, okay. Yeah.
My resource detectors may injecting script attributes asynchronously, different attributes checked asynchronously, but script attributes detected as… It must be returned with today, my attributes immediately. Yeah, yeah, okay.
Yes.
**Daniel Dyla (Dynatrace LLC)** 22:26 This is… it's kind of, it beats around the bush a little bit, but it's mostly, like, it is… it's encouraging synchronous when possible, and it's saying, like.
If stuff is happening asynchronously, you should make whatever you have available whenever you can.
**Josh Suereth (Google LLC)** 22:44 Yep.
**Daniel Dyla (Dynatrace LLC)** 22:45 But the merge… like, if you have asynchronous, identifying attributes, like, you essentially… it's difficult to make promises until things… Resolve.
**Josh Suereth (Google LLC)** 22:57 Yeah, this is what, like, internally, we use environment variables for identity, for everything, for, like, detection of who you are, where you are, because of that issue and that concern of you want to synchronously read it quickly.
So as soon as we have the OTel Entities environment variable attribute stabilized, I want to get that thing used everywhere where we would otherwise make network calls to figure out who we are. You know what I mean?
**Daniel Dyla (Dynatrace LLC)** 23:22 Yeah, but other, you know, Lambda, for example, the ID is not available right away, like, it's possible that there will always be asynchronous identifiers. It's not ideal.
**Josh Suereth (Google LLC)** 23:33 Yeah.
**Daniel Dyla (Dynatrace LLC)** 23:34 possible. So, this allows it. That line 179, that used to be a must, now it's a should.
**Josh Suereth (Google LLC)** 23:41 Yep, perfect. So, I can approve this. If you do a merge conflict, I'll do one last pass-through to just look for merge conflict, like, issues.
**Daniel Dyla (Dynatrace LLC)** 23:53 Yeah.
**Josh Suereth (Google LLC)** 23:54 Okay. And then, then I can approve. Awesome. Okay.
Cool.
**Daniel Dyla (Dynatrace LLC)** 23:59 Yeah, I think if you go to the commits tab there, Yeah, go to the last one.
**Josh Suereth (Google LLC)** 24:08 This one?
**Daniel Dyla (Dynatrace LLC)** 24:09 The la- yeah, just the last commit, That was what we had talked about, oh, no, never mind, they're out of order. Yeah, yeah, so that's it there.
**Josh Suereth (Google LLC)** 24:28 Yeah.
This was about calling them entity aware of resource detectors, yeah.
**Daniel Dyla (Dynatrace LLC)** 24:32 Yeah.
**Josh Suereth (Google LLC)** 24:33 Yep.
**Daniel Dyla (Dynatrace LLC)** 24:34 Okay.
**Josh Suereth (Google LLC)** 24:35 Instead of entity detector, yep, perfect.
Cool.
**Rob Cowart** 24:40 There's… Before we drop, I did have just one quick question.
On the network side, we are starting to prepare some of our thoughts around entities and things, and… I've really been looking around for, like.
I know Entities is new and all, but looking around for some examples, and especially things that, like, show how, like.
Where do you specify some of the relationship?
parts and what have you, and I was just gonna ask if there's any, like.
Like, what's the best example to stare at right now, to kind of see what I need to be trying to achieve?
**Josh Suereth (Google LLC)** 25:20 Yeah, I think in terms of relationships.
We… we haven't modeled something where it wasn't super obvious outside of service, so I'll show you that quick. So if we look at… Where's resource?
So service actually has, relationships that we just made a quick diagram for. They're not specified formally yet, because we don't have entity relationships formally specified, but we just show, like, what the relationship looks like of the entities that are defined.
Because again, like, in Weaver, there's no way to write an entity relationship yet. Like, that's coming, but it's not there. So instead, we have this, like, here's a namespace, the relationship between namespace and name looks kind of like this, to instance looks like this, and we kind of describe that relationship in the kind of header, if you will.
Got it. And then we made sure that we had names that made sense. So, I think that's one place to emulate. The other… the other set of… Entities that have significant relationships between them is the CAITS relate… Entities?
Where you have, like, a node and a namespace, but I don't think we document the relationship, because the relationship is kind of implicit in the Kubernetes data model, and so it's basically documented elsewhere exactly what all those relationships are and what they mean.
But that's the one that has the most significant number of relationships.
**Rob Cowart** 26:52 Okay, alright, that makes sense, why I didn't see more. I was.
**Josh Suereth (Google LLC)** 26:59 Yep.
**Rob Cowart** 27:00 I was kind of wondering more, like, like, for example, in some of the YAML files, to be able to say, like, this is contained by this other thing, or, you know.
**Josh Suereth (Google LLC)** 27:10 We have not added that to the gamble yet, yeah.
We don't have a syntax for that yet, yeah.
**Rob Cowart** 27:15 So, I think what I'm going to do is just focus then from what… because you went right to Markdown, and I've been in YAML, so I'm probably gonna switch to try to document a little more just in Markdown, and then… Maybe that'll serve as a… as a… Initiator to maybe do some of the other bits, so…
**Josh Suereth (Google LLC)** 27:35 It will, actually. That's usually… so the way… the way we did all the YAML is it all started in Markdown, and we inferred the YAML from the Markdown over time. And when there's a new concept we need to model that we find in Markdown, we move it into YAML after we understand it pretty well.
**Rob Cowart** 27:52 Sounds good. Okay, I'll focus more in that direction then. All right, perfect.
**Josh Suereth (Google LLC)** 27:55 Yeah, and let us know, like, if you, like, once you're done, and you're like, hey, here's how I model it, here's the things I needed.
we can talk about a data model from there. So, like, bring it back.
**Rob Cowart** 28:05 Yeah, I hope… I'd be optimistic to say a week from now, but maybe two weeks from now, I'll have a first pass like that, so…
**Josh Suereth (Google LLC)** 28:12 Our SIG moves on, like, an every-two-week cycle anyway, so, like, don't worry about it. Like, steady momentum is momentum. It gets done eventually, right? Awesome.
Sorry, Jim.
**Rob Cowart** 28:23 Appreciate it.
**Josh Suereth (Google LLC)** 28:24 everybody.
