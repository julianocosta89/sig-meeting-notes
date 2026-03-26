SIG: JavaScript SIG
Date: 2026-03-25
Duration: 58 minutes
Zoom Recording URL: https://zoom.us/rec/share/H4ARFT3sgS0K6BYh6Ctpkp9bs0yiOR55qdtRMcaHd5IEWXkvVEgoM92RkgxwjnaD.GhiB8a80R9V85RdV
============================================================

## Zoom Recording Transcript

**Chengzhong Wu** 01:18 Hello?
**t2t2** 01:20 I… I think it was a KubeCon.
**Trent Mick** 01:46 G.
I just got back from vacation, so I wasn't sure if there was one today during KubeCon. I guess not many JS folks are there, so maybe still.
David, did you happen to notice if… Hotel canceled meetings this week for KubeCon, or not really?
**David Luna Bistuer** 02:27 Don't remember.
But there was no…
**Trent Mick** 02:35 I'm still catching up on Slack everywhere, so I have no idea.
Looks like not.
I'll ping Mark.
Yeah, yeah.
a keyboard in a week and a half. That's crazy. I didn't intentionally bring my computer. Vacation, so just… thumbing it for One time's awful.
Oh, yeah.
Mark was just reminded, so he's showing up, I guess.
Oh, wait a minute.
Hey.
**Marc Pichler (Dynatrace)** 04:29 Sorry, the time difference, caught me off guard.
Not the usual time for me.
**Trent Mick** 04:39 Is it next week everything's back, or…
**Marc Pichler (Dynatrace)** 04:41 Yeah, next week.
**Trent Mick** 04:42 Change this weekend? Yeah, okay.
**Marc Pichler (Dynatrace)** 04:44 next week, everything should be fine again. I'll share my screen very quick, and then we can get… Started right away.
Alright, let's jump right into, shang Tsung's topic here.
**Chengzhong Wu** 05:22 Yep.
**Marc Pichler (Dynatrace)** 05:22 This is a PR on Node.js adding a metrics module.
**Chengzhong Wu** 05:28 It's another request from a series of discussion about adding the… Observability signals, for example, chase and metrics to Node.js.
And, I think there was a discussion about the tracing already. There was another request about adding the hotel tracing APIs to the Node.js as a core module, and this is another one about adding a metrics API, but this, is not adding a hotel metrics API to the Node.js.
It still confusing me that the motivation is saying.
that's add a, metrics API that's different from OTEL. Before, OTEL's metrics is being adopted more.
So, and the current API is, like.
It does not distinguish, like, counters, histograms, or any different, Or any different metric types that are well-known in… Metrics backend.
And.
**David Luna Bistuer** 06:46 umbrella. A male girl.
**Chengzhong Wu** 06:47 I mean, it's… All of these metrics types.
And… into one single metric stock create.
So… It essentially creates burden for consumers to hard-code itch, metrics, type, Hmetrix by name.
To say what's their type and what's their monotonicity?
And what's the value, type? Like, integer, or double, or floating value?
A floating point.
Numbers.
So… Which means… There… Each consumer will have to hard-code, like, say, hundreds of… metrics.
For their metric types and metrics.
Montonicity and metrics, the low types. So… by the metric name, so there's no programmatic API to specify all of this, essential metrics.
Over to you.
So, I… The discussion on the progress was back and forth and not productive.
So I requested a change, on the pull request.
And I think… It'll be more fruitful if we can have more, More observability vendors to weigh in in the discussion to see what's your opinions are.
Because the author has been claiming that their motivation to create this podcast was That optometry metrics has not been adopted.
Broadly, so they want to create a new metrics tool Reprace it.
2… this… motivation is not really convincing at all, is what I can say, that Well, I mean, a standard… a standard is not being adopted.
It's not a good time for us to create a new standard to say to prevent an existing standard to be adopted. So that's kind of like a… Looping back and forth, and it's not really productive.
So yeah, that's kind of, like, the summary of the states, and I think it's… Essential for, more vendors to weigh in this discussion.
Notably, there's a, not just… there's a new not just Collaborative Summit.
Session submitted by, Stephen, who is GitHub handle is Carl.
And I shared the link in the chat, maybe I can share the… Link in the notes as well.
It's more specifically about… Well, I think the topic is… Very… Broad, and, like, in the description.
They have listed several topics in this one-hour session. I'm not sure if we can really cover all of these sessions in one hour.
At all, because they are very indifferent, discussion, in different areas.
So the Node.js Collaborative Summit is open to all… To all, it's not restricted to, you know, just contributors, so… the Collaborative Summit is also, available for remote attendees, not only in-person attendees, so I think it'll be… helpful for… more open telemetry, contributors to participate in the discussion. So, apart from this, Apart from this session, there's a dedicated session for just talking about octetry support in the In the same, collaborator, summit.
That was the one that I submitted earlier.
This will be specifically talking about urban regulated support.
And, improving the… Elementary support out of the box in Node.js.
So this will be more focused on open temperature and related, fields, so I think this will definitely, Appreciate it. No doubt.
on… People in the room.
To weigh in, in a discussion.
I'm sorry for not, bringing up this in the SSEG meetings earlier, because I have… I have a… conflict.
Meeting at this time, so… Yeah, given that the collaborative summit is in 2 weeks, if I'm… if I get… yeah, in 3 weeks. So I'm trying to raise it here for broader visibility.
**Marc Pichler (Dynatrace)** 12:24 Thank you for bringing that up. I think the metrics topic, I did some reading, and it's definitely interesting to see another… API being proposed. I think I'm with you, on… Duh… on the idea that it could be a bit difficult to map to, open telemetry, especially around the things that you mentioned.
**Chengzhong Wu** 12:54 I think the concern that I had with regarding the current API is not that it's not easy to map into Openetry, it's more about mapping to every… It's more about the adding burdens to every consumer of this API, because every consumer has to hard code.
By metric and aim.
for the metric Ives that they want to… Eventually store the magic backend.
So, that's the main concern. I'm… Naming of Autometry here in the review command is because our telemetry API was specifically designed to address this concern that the producer of the metrics Oh, so… How to specify a hint.
programmatically, Saying that… How they want this metric, to be… Store at the Magic backend.
The consumer really disagree with this hint, they can, like, specify a different metric… property, like, the bucket, the histogram buckets, or, like, if they want to map a counter to a lost value, that's… Their freedom, but by default, the producer should give the… should give the… metric type and metric hints about how the metric should be saved at the backend. So this would save A lot of effort at the consumer side.
that if they agree with what producer hints about the metric, they can just pick whatever, and they don't need to hard-code it for every metric. And the current issue with this particular ProQuest API was that The consumer has to article for every metric they want to consume.
**Marc Pichler (Dynatrace)** 15:05 Yeah, so the consumer in that case would be either the person who's instrumenting their app, or somebody providing an instrumentation, right?
**Chengzhong Wu** 15:15 Yes.
**Marc Pichler (Dynatrace)** 15:18 Yeah, I think that, could be a bit difficult, accomplish, and… I'll have a look at this PR here, and I will also be at the… Collaborate the summit, most likely, so, Will be interesting to follow the discussion there.
**Chengzhong Wu** 15:45 Yeah, thank you very much.
I think the Collaborative Summit, in-person registration And deadline is next Friday. The Global Summit is in London.
In April… on April 14th to 15th, so it's about in 3 weeks, so there are still time to register to attend in person.
Remote identity does not need any registration, so… I will try to schedule the session… the two sessions… the two topics.
At the end of the day, so that it'll be easier for, people in… West Coast of America to… Attend.
**Marc Pichler (Dynatrace)** 16:43 Yeah, thank you for bringing that up.
I think I don't have any immediate comments about it, Yeah, I did some reading, and there's some things that I… still don't fully understand, so I'll probably also have to look at the code a bit more, to make sure.
Yeah, no problem. I fully understand it.
Yes, in terms of adoption, The only thing that I can share is that we have seen gradual, increases in metrics from OpenTelemetry here at Dynatrace.
And they're pretty constant, in growth.
So… Don't have any specific numbers that I can share, but it's definitely going up all the time.
**Chengzhong Wu** 17:44 Yeah, that's a very valuable, data point. I think it's also worth mentioning that, from what I can tell from most major vendors.
The website already indicates that they support of temperature metrics, either via the OTLP, Data protocol, or through the… which means… they will support the 11 Geometrics API, and SDK.
and… I… yeah, so, I think… more vendors when you're in the discussion will be definitely helpful to push this, discussion forward, instead of, like, better than for saying that no one Or… Less adoption of temperature metrics than the optometry traces.
But either way, I think… This will be part of the broader discussion about, Upper temperatures are in the… No, Jace.
I don't think it would be a good idea to say Node.js is only going to support our potential traces by dropping metrics.
And… which means the… it will be a partial support of a damaging in Node.js. So that would be a very bad, impression to the Node.js users, so I don't think that would be a, that should be the path forward.
Yep.
**Marc Pichler (Dynatrace)** 19:26 Thank you for… Sharing your thoughts there.
Yeah, I encourage everybody to also have a look, at this.
this PR and also the other one, the, the, older one is.
**Chengzhong Wu** 19:41 Yeah, I can share the audio, the audio link in the, in the notes as well.
**Marc Pichler (Dynatrace)** 19:48 Thank you.
Alright.
Any additional comments or questions around this topic here?
If not, then, let's move on to… The next one is a discussion about trace state edit.
**David Luna Bistuer** 20:22 Yeah, just maybe, I don't know, just, I call for your opinion about this, so if you remember, we have the, tree state class that actually does validation. Every time that we are creating a tree state, it does a partial validation.
And the boy's kind of, the guys from the spec of their past, they changed the spec to say that We should not validate the entire tri-state, although in the conversation from that ticket, there was a conversation in the spec that they told us, they told us it was okay to Validate and drop, invalid entries.
And the, shortening the tickets.
But basically, the dance issue, also says something at the end that is, like, like, something that we should… Only work with the entries that are our entries in the open telemetry.
Inside the vendor key. So, my question would be, now a trace state is being used just for Getting and setting vendor keys, the whole value, okay?
And here in, you know, Pantalemzi, the OT vendor key, we have… Kind of a… A shortlist of members and keys and values.
My question is that if we should also reduce the API to just work with these values. At the moment in our specification, we only have the threshold and random value, randomness.
These two keys, and with their… they are values, so… should we, Limit or scope the rest date.
Just to work with that… those keys inside our vendor key, or… We should… should we keep it, as generic as possible, and then… other people deal with. There is an example in… in, composite samplers.
They are, using the Tracy State, but just to get the OpenTelemetry vendor key, and then they're parsing.
The values in there.
**Trent Mick** 22:35 Okay, I'm not well-read on this, I haven't read on it in a while, but, I think a tray state class should be generic. It definitely shouldn't get into… the values of vendor keys, because by the Tracy definition, that's meant to be opaque. So I think it… it… without having looked at the code recently, it sounds reasonable that the parsing of the individual TH and RV values in the composite sampler packages makes sense. Whether the TraceState API, this is just my opinion, whether it should limit its API to just the OT vendor thing is… I could go either way on that, I'd be inclined to have it be generic, and then make sure that our packages are really only ever using it with whatever the constant is that we have for this OT.
vendor prefix, But I don't know, because I think that if we came up with the… and if we came up with a fairly good generic implementation, then that's something that could get reused by other people if they're putting their own… Vendor keys and stuff in there.
That said, if we find we have a good performance argument for doing just the specific, if it makes it faster, Then… then we could consider doing that.
Was that clear? So I think on the vendor thing, I would be inclined to make our implementation generic.
And have our usage only ever use the OT vendor key.
Yeah.
Unless there's a performance argument against it.
Does that answer your questions?
**David Luna Bistuer** 24:12 Yeah I will not, anyone else have an opinion on that?
**Trent Mick** 24:17 Yeah, and that's just an opinion, yeah.
**Marc Pichler (Dynatrace)** 24:21 I think I agree with Trent. The… Yeah, I… Don't have a strong opinion either way, but… yeah, I think I'm in agreement with that approach, so…
**David Luna Bistuer** 24:37 Okay, so we get that.
Generic, and then, for the OpenTelemetry-specific keys and values, we have our own parsing thing, like the composite sampler.
**Marc Pichler (Dynatrace)** 24:49 Yeah, I think that makes sense, yeah.
**David Luna Bistuer** 24:52 Okay.
**Trent Mick** 24:53 So, is… is this… Different? Mar… very different from what we currently have?
**David Luna Bistuer** 25:02 At the moment, what device… what we have right now is the generic.
So you set the key and value, key is the primary key, and value is the whole value.
But you can set full, bar.
Whatever it is, you can set the OT key with the… with the values.
There is no… and then we are just checking with the, TraceState spec, so we are just complying with the trace state spec. We're not complying with the, open telemet spec for our vendor key.
That's the difference, so… yeah. Right.
Just asking if we should go the extra mile and actually do that validation as well, or not.
But yeah, if not, it's just, it's a matter to be kind of, Being lazy about parsing things.
And, and yeah, and, kind of following the, the reason, the, the reason with this, issue on the trace context issue that is, is linked in the, in here.
It's about when parsing, not discarding the whole tree state.
But just the entries that are not… The… that are invalid.
**Trent Mick** 26:14 Great.
**Marc Pichler (Dynatrace)** 26:23 Would that approach, that approach doesn't have any, probability of… breaking anything, right? Do we know how the other SDKs handle this sort of thing?
**David Luna Bistuer** 26:39 Well, that issue, I haven't checked lately, but that issue tells that although Java was just discarding the whole thing.
And kind of at the end of the discussion was, yeah, maybe not… it's better not to discard the entire thing, but just only the entries. So, I'm…
**Trent Mick** 26:54 They were just skirting.
**David Luna Bistuer** 26:55 with…
**Trent Mick** 26:56 Discarding the entire trace state if there is one unit.
at entering it?
**David Luna Bistuer** 27:01 Yeah.
**Trent Mick** 27:01 Nice.
**David Luna Bistuer** 27:02 actually think that we do it, we do it as well, so JavaScript implementation is doing this as well.
**Marc Pichler (Dynatrace)** 27:09 Yeah, I think it's very likely that we, also do it this way. A lot of the code, that we have was very much inspired by, Chava?
In the beginning, so, there, there are… Similarities between the two implementations there.
**David Luna Bistuer** 27:31 Okay, there was also some… I think there was also a PR… that I put it on hold about, It was… it was improving the serialization of the tray state. That PR was adding some, performance tests.
Do you think that it's reasonable to actually include these performance benchmarks?
**Marc Pichler (Dynatrace)** 27:58 So this is the CR…
**Trent Mick** 28:01 Yeah, I think we had some prior art for, or maybe this was the prior art, for adding benchmarks so you could take a look at them, but not having them in the nightly run, because there's no point in having us on a nightly run, right? It's about comparison, sorry, comparing a new implementation versus an old one that we're getting rid of, and there's no kind of ongoing…
**David Luna Bistuer** 28:21 Okay.
**Trent Mick** 28:22 But I… I can't remember exactly where that other example was.
**Marc Pichler (Dynatrace)** 28:27 I think the example is in ODLP Transformer, where we're benchmarking a bunch of internal, functions there.
We could just do the same approach here, and then, like, optimize this implementation, and also keep the performance benchmarks But also filter them out so that they're not published to the website.
Because I think most… Consumers wouldn't be able to… Do anything with this information. So, We don't need to publish it to the website, I think.
But yeah, I think overall we can still go ahead with… Optimizing this.
First, and then, adjusting the implementation.
Or it later. To follow what we discussed.
**David Luna Bistuer** 29:26 Okay, good.
**Marc Pichler (Dynatrace)** 29:34 Right.
Any other questions or comments around TraceState?
If not, then we can move on to bug triage.
Always if you have any, can you… additional topics that you would like to discuss, please feel free to, cheers.
Put a, topic here on the agenda list, and then we can… about it. Feel free to just interrupt me when I'm talking. Actually, one thing that I can put on the agenda is, we just published a new API release, and also new AutoJS core and, experimental releases, the contrib release.
will follow suit. So… That's… That's sad.
Just typed it up here.
So that we have a record of it.
We currently have some failing tests in the country repo, but these only seem to be related to the latest, Next… Oh no, there seems to be some more problems.
**Trent Mick** 31:21 A TAV test, you mean?
**Marc Pichler (Dynatrace)** 31:23 Yeah, the TAF tests were failing.
Before on main, and now it seems that, Data loader instrumentation test is also failing.
Looks like this, there's already just some… Change in how we serialize things, that it now includes the empty object for attributes.
There should be an easy fix.
Once we have that, we can… probably merge this PR in and, also published contract there.
Let's do bug triage, then.
Up close, this one was stale.
Since there was no response.
We can always reopen if the person gets back to us.
Alright, we have 43 PRs in Contrip, and… We have 41… So let's go with Contrip. There's actually one PR that I was… That I thought we should talk about, so maybe let's go with that one first. This is the console instrumentation PR here.
I guess we need to find some, strategy here, how to go about it, because there's a similar PR open in the browser repo, so it didn't take long until we had the same… same instrumentations in both repos.
Yeah, I guess the idea in the browser repo is going to be to include the concert instrumentation in the single instrumentation package, right?
Yeah.
**David Luna Bistuer** 33:57 There was a comment last week. Last week on the browser, Sick, there was, I think that they mentioned, there is a ticket in the browser.
In their browser repo that, We'll start an effort of moving browser instrument additions to the browser packets. Now, if you remember, they made a release process, and now they have a single package that exports different paths.
So you can import, With Soupads, you can import specific instrumentations, and also get the benefit of the tree shaking from the bundlers.
So, yeah, now that they have it priced, like, browser-friendly, bundle-friendly package for that, they are thinking about moving If it makes sense to move some of the search to the browser repository, so yeah.
**Marc Pichler (Dynatrace)** 34:48 Will that, So these will also be included then in that package, right? So we would deprecate the ones in, that are published right now, and we would instead refer to the browser instrumentation package.
**David Luna Bistuer** 35:02 Yeah, I guess that would be a good way to do that, so to move it.
I don't know if all of them, so there is another, also, I think Dan opened a ticket also last week, or the beginning of this week, about moving out from zone. So, for example, I think that user interaction that depends on zone has a pure dependency. Maybe it's not going to be… migrated to browser packets, but, we'll see. But yeah, the ones that are going to be removed, I guess that would be it. So we're going to duplicate the package, and then we're going to refer to… To the new one.
**Trent Mick** 35:40 Oh, we just… we just lost Hector on the call.
**David Luna Bistuer** 35:43 Let's…
**Trent Mick** 35:45 And that's his in a contributor part.
**David Luna Bistuer** 35:47 Yeah, but he's going to be tomorrow in the Brussels, probably.
**Marc Pichler (Dynatrace)** 35:52 Solved.
**David Luna Bistuer** 35:53 Okay, not a module.
**Marc Pichler (Dynatrace)** 35:56 Yeah, when he's in the browser sig, then I guess there can be some discussion on… How to go forward about this, but if…
**Trent Mick** 36:05 Organ's.
**Marc Pichler (Dynatrace)** 36:05 If it's gonna be merged into the single instrumentation package anyway, then some duplication should be fine, and also the console instrumentation is not that, It is not that much code, so, It, should be fine if it's just duplicated across, two repos.
Just wondered.
Sure, that we don't have a clash for the name.
Sorry, go ahead.
**Trent Mick** 36:37 Is it… well, I mean, even if there's not a clash on the name, there's still potential user confusion here, right? Is the… I haven't looked at… Hector, you're on the call. I haven't looked at.
**Hector Hernandez** 36:48 Yeah, yeah, I'm trying to drive.
**Trent Mick** 36:49 I'm sure.
**Hector Hernandez** 36:50 the Node.js console instrumentation, so definitely there's going to be some name conflicts here.
**Marc Pichler (Dynatrace)** 36:56 And…
**Trent Mick** 36:56 And this one is Node.js… Specific?
Or not, I'm trying to see what the console methods patched are, if it's doing some. Yeah, okay.
Boy, something… Yeah, it is.
**David Luna Bistuer** 37:13 Yeah.
Something that is bugging me is about… If in browser we have all the instrument issues in the same package, so usually we use the scope, the name of the package, we… We put as a scope.
the name of the packets. So we have OpenTelemetry, slash, Instrumentation, whatever.
**Trent Mick** 37:36 I think it should use the… because that's usually the import that you're importing it from, but the browser package is using entry points, right?
**David Luna Bistuer** 37:45 Yes, now you import from OpenTrmity slash browser instrumentation slash experimental slash whatever, whereby…
**Trent Mick** 37:52 Okay, I think that should be the… Instrumentation scope name. Yeah, I think, but I'm not sure what's being done in that package right now.
**David Luna Bistuer** 38:01 Well, the ones that were merged, because at first we have kind of a couple of instrumentations, two or three instrumentations was Web Vitals, personal navigation, I think it was, or… yeah, a couple of them. They just moved the code, so the scope is still, you know, the former package name.
**Trent Mick** 38:19 Okay, so everything's still in the 0.x, so we can…
**David Luna Bistuer** 38:23 Yeah, we can do it.
**Trent Mick** 38:24 Not worry about, oh my god, it's brick and change for brick and.
**David Luna Bistuer** 38:27 Okay, well, I'll… I'll…
**Trent Mick** 38:29 That said.
**David Luna Bistuer** 38:30 I'll bring the topic tomorrow then.
**Trent Mick** 38:32 Okay, I think for clarity, it would be better to… Use the entry point name.
**David Luna Bistuer** 38:38 But that means if we are using the whole… the whole import, it means that when we stabilize it.
That experimental from the scope name, also Bricks.
**Trent Mick** 38:48 Okay, yeah, I… well, I started saying that before you reminded me that experimental is in that path there. I think they could talk about having, like, what the future expected name of the thing is. Another example that is the, So a thing that the NRAG has a few PRs that I've been slowly reviewing is on implementing OpenTelemetry SDK self-metrics, so this is kind of metrics on how the SDK itself is working. There are a whole bunch of metrics in there, and a number of PRs for that.
But the instrumentation scope used for metrics from, like, the log exporter, for example, is… OpenTelemetry… at OpenTelemetry slash SDK logs, and that happens to be the package name, so that works. But for tracing, because tracing has multiple packages with SDK trace base and SDK trace node and that kind of thing, the… the… the name there used doesn't have the dash base in it, so it was just using SK-trace, so it's kind of not… or that's the first example that I know of, where it's not actually the package name, but it's kind of what we would… Envision the meaningful package name matching.
yeah, being so, like, they could talk about dropping the experimental from there. So then it's stable once they move forward, and there's no need to have both experimental and non-experimental Versions of that thing.
I don't know. Just throwing at opinions. That said, I don't know anything in the spec about what stability requirements are for the instrumentation scope name. No idea. Because it can make a difference for people's metrics, views, and things like that, right?
Yeah.
**Marc Pichler (Dynatrace)** 40:33 Oh.
I guess… Yeah, that's a really interesting challenge that I hadn't considered when I suggested that.
**Trent Mick** 40:50 When you suggested which? Oh, having the one grouped browser.
**Marc Pichler (Dynatrace)** 40:54 Yeah, the one group package, yeah.
I think the way that they usually… Recommend using the, Instrumentation scope is to… used a fully qualified name, but that doesn't exist in… in JS, so, Having it with the entry point.
Probably doesn't make… Like, having the thing with the entry bind on here, and also including experimental could be… Could be a bit difficult to deal with, yeah.
**Trent Mick** 41:39 Difficult how? Like, you mean, it's a long string, does… does that really bother people? I don't know.
**Marc Pichler (Dynatrace)** 41:44 No, no, no, not the long… the long string is fine. I think it's, exactly the one with, like, dropping experimental, when it's actually not, A normal thing, but then again, One of the benefits of changing it later is that you're sure that it won't be experimental anymore.
So… pros and cons, I guess.
**Trent Mick** 42:12 Yeah.
It's not like it's… well, yeah, we don't have a well-established pattern there, so it's not like anyone's been following this rule, or… I can check to make sure that all of my… metrics view drops with experimental in there is guaranteeing that I don't have non-experimental things in there. I don't know, like, yeah.
And I haven't thought… Whether… go ahead, you go.
**Marc Pichler (Dynatrace)** 42:34 Oh, sorry, One of the things that you can do in, metric views is you can say… you can put a star in there, and it will do a glob style.
Thing? Yeah.
So if you just have… zero characters in between, then it will work for both the stable and experimental ones, so views should be fine. But then again, you have probably, processing rules on the collector and stuff like that, where you would have to do that everywhere.
Which… Might be a lot more annoying to deal with.
So probably just going with the… what the name would be if it was Staber.
Sounds like the best approach.
**Trent Mick** 43:22 Okay. I'd be fine with either, because I don't think there's… I don't know, hard use cases either way, but…
**Marc Pichler (Dynatrace)** 43:30 Hmm.
**Trent Mick** 43:32 Let the browser say, pick one.
**Marc Pichler (Dynatrace)** 43:35 Yeah.
**Trent Mick** 43:38 Okay, so back to the console thing, Hector, if you're still on, is… somebody wants this? This scares me, because we do have the… the potential infinite loop thing going on here, too, right?
**Hector Hernandez** 43:49 It has some code there, but… We have been offering this for at least 10 years. We have our own, console instrument, yeah, but we want to deprecate the package, so that's why we're trying to push this to be in OpenTelemetry. We had… Okay.
I started the conversation, like, 2 years ago. People were interested in this console. I couldn't find the issue anymore, but I remember there was some conversation here.
**Marc Pichler (Dynatrace)** 44:13 I also remember that, yeah.
**Hector Hernandez** 44:14 You have a… no clue where it is, but.
**Marc Pichler (Dynatrace)** 44:17 Yeah.
**Hector Hernandez** 44:18 Yeah, definitely, people are heavily using this.
**Trent Mick** 44:21 Okay.
My guess would be the stale butt.
Knocked it off the list, but yeah.
**Marc Pichler (Dynatrace)** 44:29 If the blocking… the blocking issue back then was exactly what you mentioned, Trent, the, infinite loop situation.
But… Martin… Cooper merged.
Orlando PR in… the API recently.
that, essentially makes the API, if it's… Used before, Before the instrumentation can change the console thing, then it will just hold on to the uninstrumented console, and then alleviate that, issue a bit. It doesn't fully fix it, but at least it makes the likelihood of it happening a bit lower, and also if we just include it with, like, the auto-instrumentations node package.
should… be the default way of going about things, so… It's also very unlikely to happen there.
**Trent Mick** 45:39 Okay. Okay, that's cool, so that's one concern.
The other one, what about… what about having node-console be the name here? Instrumentation node console. If it's doing… because, well, correct me if I'm wrong, if it's doing node-specific console things, like, is it instrumenting things that Node's console object has that the browser definition of the console object does not?
**Hector Hernandez** 46:05 Well, it's actually patching the… global console in Node.js, so it's very specific to Node.js.
The methods look the same, right? But.
**Trent Mick** 46:16 Yeah, I can't remember if the… well, I'd have to go bear with MDN's console definition, but…
**Hector Hernandez** 46:24 Yeah, you added some comment there, maybe we can have a different name, just include Node.js at the end of it, so there's no customer confusion.
**Marc Pichler (Dynatrace)** 46:45 That sounds… Sounds like a good approach. Let's see what the discussion… Deals with the processing, maybe we can keep it, or maybe we just… Rename it, it should be… Probably fine. Renaming it Instrumentation Console Node makes it very clear what it's supposed to be for.
If we ever need to rename it, we can still do that later.
Alright.
So, I went off-script and picked a different PR, but now we can go back to, Yeah, triage, unless anybody else has any, Anything you would like to talk about?
Right.
So, this was, instrumentation AMQP… Looks like, person… Made quite a few changes here.
Just gonna look at it real quick to see… What these changes are.
Still uses this, CENCOM stability opt-in for messaging.
I had this PR for… SEMConf that unfortunately got still closed.
I had it linked here somewhere.
disappear.
That's the issue, it's the PR.
I was meaning to reopen this one, but… didn't get to it yet. If anybody wants to revive that one, please feel free to go ahead.
can probably just take the same changes that I made.
And pushed him again.
Otherwise I will get to it, hopefully soon.
**Trent Mick** 49:14 So the NQP one, my memories on that one is we kind of stalled saying, Because it wasn't… stabilized… RPC stuff, it wasn't stabilized yet. My sense is, from the link that I put in, that the RPC SEMCOM is… Getting close to being stabilized.
And that would at least… solve the easy problem for us, right? Because then we could revisit this PR.
Or the same work in a new PR, too. Yeah.
Have an easy path.
**Marc Pichler (Dynatrace)** 49:47 I think that would be, would be great. If we had that stabilized, then we can just go ahead with it, the same way as we did with, HTTP and… database.
Yep.
I think I'd still like to land the, latest experimental one, because it would unblock a bunch of other instrumentations as well. We can apply that, 2… other parts of SEMConf as well.
Then we could… Have some progress in other instrumentations.
**Trent Mick** 50:27 So, another question, if other people happen to know, did, like, not JS-specific, have there been hotel discussions about I thought there had been about having some top-level config, whether it's environment variable or whatever, to say.
I just want stable stuffs.
As a user.
And then anything experimental should be watching for that and turn itself off, basically. And then whether… there was… Discussion of having more fine-grained knobs on that, or recommendations on what config should be exposed for allowing certain experimental things, because, just the only examples I know of is there's some instrumentations or parts of the SDK in OTelJava that have, like, otel.java.
Allow experimental whatever things, this specific, basically.
Opt-in things for specific features.
Do you know if there's any… General spec work on that, or no?
Anyone?
**Marc Pichler (Dynatrace)** 51:37 I'm not aware of any… Anything specific there?
I'm also not sure if there's anything on the declarative config side, I think the whole, instrumentation config stuff is experimental there right now, so it probably also doesn't have, Away tool.
specifically enable, features that are experimental there, because the whole thing is still… Okay.
**Trent Mick** 52:09 Okay.
**Marc Pichler (Dynatrace)** 52:14 Yeah, I think, Having some sort of a standardized way of doing that would be helpful.
Because then it also takes the guesswork out of, configuring it.
having something to say. I just want… stable stuff, or I just… I don't want any experimental stuff.
Could already be very helpful.
But I think the… The blog post around, making stable be the default, also kind of makes that idea obsolete, because then, you would… have stable be the default, and you would explicitly opt in to the experimental things.
But then you would have to have the opposite, right? You would have to have some standardized way of turning experimental things on.
So…
**Trent Mick** 53:21 Yeah, that's what I'm getting at, is if I'm reviewing a PR from someone that wants to add an experimental feature.
Should we be requiring some common pattern for what the configuration.
**Marc Pichler (Dynatrace)** 53:32 Yes.
**Trent Mick** 53:33 to turn that thing on, and I realized.
**Marc Pichler (Dynatrace)** 53:34 Sure.
**Trent Mick** 53:35 fully plumbed declarative config or anything yet, but, like, environment variables, or just even the Boolean options that we add to… Instrumentation config, yeah. I'm not exactly sure what the pattern is yet.
**Marc Pichler (Dynatrace)** 53:48 We could also justify our own.
For now.
And see where that leads us. I guess if we have some… Way to, say, use this environment variable to, turn experimental features on, or use this, Or we have some sort of way to… Consistently name flags in code to turn experimental features on, then that would already get us quite far.
Having that would then… give us the same benefits as probably what the Java folks have right now, where they… Already know that this is what they would recommend.
And we would just go the same way.
And then at some point, That approach could be stabilized somehow.
By, specifying it or something.
**Trent Mick** 54:54 Cool. Thanks.
**Marc Pichler (Dynatrace)** 55:03 Right, this is it for… at PR.
Then we have SQS context propagation for AWS Lambda. There seems to be quite a bit of discussion between… Jonathan and person here… And of course, semantic conventions.
Thing.
I remember now. This was, because the… That's back.
was not in line with the actual messaging spec, so… Kind of… caught people off guard.
I wonder if anything has changed, since then.
Seems that this, It's the document.
Look at any… large changes were happening here, only formatting stuff, so I guess that's just still stuck on the same problem.
There's nothing we can do for now.
If anybody has time to drive this on the SEMCOM site, it would be very much appreciated.
We have, instrumentation priorities.
I don't think the component on this, but… Nobody responded yet.
FPR seems, actually, to be fairly smart.
It's well-tested, then.
We should be okay, but… I don't know my way around through ready centers, or I already sent others too much, so, would take me quite a bit of time to… Have a look at that.
I'll reach out to, Amir.
So, let's see if it's up for… We're reviewing that PR.
I'll just put that in my notes really quick.
And it looks like we are out of time anyway, so… Thank you, everybody, for joining today.
Have a nice week, and see you next week.
**Hector Hernandez** 58:41 Thank you very much.
**Chengzhong Wu** 58:43 Bye.
**Marc Pichler (Dynatrace)** 58:43 Bye.
