SIG: OpenTelemetry Specification SIG + Maintainers Sync
Date: 2026-09-01
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Armin (Dynatrace)** 05:28 Hey, Josh, will you be sharing your part?
Since you're the first one in the agenda.
**Josh Suereth (Google LLC)** 05:39 Sure.
**Armin (Dynatrace)** 05:41 Alright.
**Josh Suereth (Google LLC)** 05:43 Are we… are we getting started? Sorry.
**Armin (Dynatrace)** 05:46 No, no rush.
**Josh Suereth (Google LLC)** 05:48 Okay.
Why does it want me to share audio now? That's weird.
Okay.
Right, so… If it's alright, we can get started now.
Armin, are you running for me?
**Armin (Dynatrace)** 06:08 There, still a few people coming in. Maybe you want to wait another… another minute.
**Josh Suereth (Google LLC)** 06:12 Sure.
**Armin (Dynatrace)** 06:14 I was just wondering if you need some time to get ready, that's why I started early.
**Josh Suereth (Google LLC)** 06:19 Oh, that's fair, yeah, I can… I'm gonna stop presenting, because I don't know, like, I think all you have to do is present the notes, I don't really have anything specifically to show, I put everything in the notes.
**Liudmila Molkova** 06:33 I joined, and I thought… I saw you, Josh, and I thought, oh, Josh is on call, TC on call this week.
While we're awaiting, does anybody want to volunteer for the project updates?
Like, if you had an interesting project.
your SIG worked on, like, stabilization, or, like, a feature development, and you released a major version of something, and you want to share your experience.
That might be helpful for other SIGs in the community.
Please volunteer, we would love to hear from you.
**Armin (Dynatrace)** 07:25 How did the list there on the left go together? Like, come together, actually? So the right one, I gather that… For those lines, it's people that volunteered.
on… on… Their own, but the others.
How did…
**Liudmila Molkova** 07:42 This is, was gentle nagging from the TC for people to come present. I think packaging, there was an impromptu presentation a couple of weeks ago. I… we probably should move packaging. We're always welcoming packaging to present if we want to.
**Armin (Dynatrace)** 08:00 Yeah, I think they were even the very first ones to propose that.
Overall.
**Liudmila Molkova** 08:09 Sorry?
**Armin (Dynatrace)** 08:10 I think they were even the first ones to start with such a SIG update for their proposal back in the days.
**Liudmila Molkova** 08:20 Right.
**Armin (Dynatrace)** 08:22 Alright, so 5 minutes past the hour, let's kick it off with Josh and NTT Spec.
**Josh Suereth (Google LLC)** 08:30 Cool. I was just writing my next topic, too. So… Just wanted to do some updates from EntitySpec PRs that are in flight, and the entity SIG. So, we have two PRs, and we want to sequence them in the order I have listed here, so trying to elicit some more reviews. The first one basically has approval from the entity SIG, the second one will have approval from the entity SIG, but doesn't yet.
So the first one is, we want to clarify resource on SDK startup.
Because that specification is a bit loose, and we're trying to be a little more crisp with what's allowed, and make sure that we can support entities going forward. There's a few complications in there that had to get addressed.
But one of them is an affordance for async resource detection in Node.js. One of the problems that Node.js suffered with with the previous spec, that we're making it clear is that, if resource detection had to make an HTTP call.
It had to be async.
And since Node.js is kind of, like, single-threaded, and you can't really block.
It made for an awkward… implementation. So this actually adds affordance for Node.js for what is allowed to be synced, what's allowed to be async, and make it very clear the resource detection initial resource provider like, looks like. The other thing that this PR does is it formalizes a resource provider, concept. I don't know if Dan is in the call yet, or if you want to say anything else, but… There's a few comments on it. We have some responses from the entity SIG. Just looking for more feedback and reviews, because we'd like to get this one in quickly to unblock the next one.
And I think this is ready for review. Dan, is there anything you wanted to say about that one?
**Daniel Dyla (Dynatrace)** 10:21 Nothing in particular. I'm actually, like, making edits to the PR while we're on the call. I was trying to get it to… to, you know, the final state before this call, but other things interfered.
Yeah, I don't have a lot to add to what you just said.
**Josh Suereth (Google LLC)** 10:38 Cool, and I think the edits you're making are all outlined in the comments too, right?
**Daniel Dyla (Dynatrace)** 10:43 Yes, exactly.
**Josh Suereth (Google LLC)** 10:44 Good, good. So, we… it's still… I wanted to make sure we got folks' attention to take a look at this PR so we can try to get that one through relatively quickly.
Any… any questions or discussions folks have on… that they want to have now on that?
Okay.
The second PR is more interesting, because of some decisions that are going to impact it. The second PR needs to get updated to leverage the first PR. So that's one of the things. This one is… the goal of this PR is to make sure the named resource detectors that were added as part of the config spec Will produce entities by default.
So the decision here was, there… right now in this PR, there is this hotel entities opt-in environment variable flag.
We discussed this in a spec meeting, I guess, like, a month ago, and two weeks ago, and a couple times, about removing the opt-in flag as being unnecessary, because it's a non-breaking change.
That is the… the… proposal we have here is that these resource detectors providing entities is a non-breaking change for people who leverage resource detection. The way the merge algorithm is defined, actually fixes some bugs, with the actual resource merge model.
And so, we're actually considering the change in behavior part of the bug fix of the resource detection merge model that existed, that plagues some SDKs. For context, if you didn't know, most SDKs violate the specification for resource detection merging, because in practice, there's basically an issue where it's a little too restrictive.
So, this actually alleviates that restriction.
And we think fixes the bug, and otherwise does not cause breaking changes to existing behavior.
That is… that is what we're stating here from the prototypes we have.
I wanted to walk that through, everyone, because what this… The goal of this PR is we now have a specification where those named resource detectors will produce entities.
and we can start updating SDKs to produce entities. And this should be non-breaking. There is no opt-in flag to turn it on or off outside of you engaging with the configuration surface to say, here's the resource detectors I want to use.
So, leaving that open for some discussion.
**Tigran Najaryan (Splunk Inc.)** 13:27 Josh, what's the bug fix you're talking about? What is the bug that… that is being fixed?
**Josh Suereth (Google LLC)** 13:33 So, the issue right now is when you have resource attributes that are completely unrelated to each other.
And they live in different binaries, like, sorry, a different library, if you will. So let's say I have GCP resource detection, that's near and dear to my heart.
Or I have, you know, Splunk has a module that has resource detection for the, the telemetry auto SDK fields, right?
If I want to annotate the resource detector with the schema URL that it uses.
what happens in practice if I… if the SDK also annotates with the schema URL? Unless those IDs are exactly the same, we drop we drop resource information. We drop the, attributes if the URLs don't line up exactly across the entire resource.
What this fixes in this specification is because we're actually using the merge algorithm from entities.
Those would no longer be in conflict with each other, and so the merge is now allowed to happen.
you would get not a schema URL, at the baseline resource, you would get the schema URL inside of the entity part of the resource.
In that case. So it's basically allowing more merges to occur that would otherwise have been allowed.
**Tigran Najaryan (Splunk Inc.)** 14:55 Yeah, yeah, yeah, that makes sense. I saw it myself, so yes.
Okay, got it, thank you.
**Josh Suereth (Google LLC)** 15:01 Yeah.
But that also, like, considering that a bug.
Is why this is a non-breaking change.
**Tigran Najaryan (Splunk Inc.)** 15:08 Yeah, I agree. I think it is a bug, yes, I agree.
**Josh Suereth (Google LLC)** 15:19 Cool! I took my 10 minutes, and I did too much talking. So, looking forward to discussions. If you guys have any concerns or thoughts, there was a lot of stuff on the PR. This one is going to be updated to remove the, the opt-in flag.
And I would love to hear if folks have concerns about that. Please either, make notes on the PR or mention it now if you, you know, have them now, but, you know, please let us know as soon as possible. Thanks.
**Armin (Dynatrace)** 15:52 Any other comments from the round on this one?
If not, I'll pass it on to Carlos for the next items.
**Carlos Alberto Cortez** 16:05 Yeah, hello. There are a couple of small issues. We would like to get some initial feedback from this group. They are around the Kotlin SIG.
the first one, it's just a draft, because I'm not sure about, we talked briefly about that last week, and it's basically about the fact that the Cortez SIG will not initially need global… stuff, including propagators, but propagators is the only thing that is actually, using a most language there. So I was wondering… and we were talking about that Even though we are changing normative language, we are going from a very restrictive language to more relaxed language.
So, mostly, we like to get people who are… against this. Before, you know, if anything, that, yeah.
we discuss it more. I see that Robert already reviewed that. Other than that.
Please leave a comment, or we can talk about it briefly here.
**Armin (Dynatrace)** 17:06 Do you know if, as per today, this is something that's broadly implemented, with just some gaps, or… Or is it rather uncommon?
**Carlos Alberto Cortez** 17:16 No, I think every SIG has this, even gold has this.
**Armin (Dynatrace)** 17:20 Okay.
Because then, even from a user perspective, not just from an SDK implementer, but a user perspective, it's… fine, because by the time the Kotlin SIG will… will come to stability, it would already no longer be in place.
So that should work.
**Carlos Alberto Cortez** 17:39 Yep.
Okay, yeah, so thank you so much for, yeah, the attention. Please provide feedback. And the second one is slightly related, but before even discussing more stuff, I wanted to highlight, if you could open the link there.
Basically, this is a section of the specification that is rather old, and there's no normative language, but in the part, the third section, which says the API dependency contains a minimal implementation of the API, I think that's what all SIGs do at this moment, but there's no normative language.
But my impression is that, just to be super clear, or rather, I would like to get a double clarification on this one. That's the attempt, right?
And the context of this is that Kotlin, we're still discussing that, but for a few different technical reasons, there's the idea of potentially separating the API from the no-op implementation. I already brought that topic here, like, a few months ago, but now this is, like, the last thing. And Tigran, I think it was you who wrote this part, so my impression is that this should be a normative language, saying… I mean, there's a section called requirements.
But that only mentions that the SDK and the API must be decoupled, but it never mentions that the API should be part of… that no op should be part of the API artifact or package, and this is the closest we get.
**Armin (Dynatrace)** 19:14 If the no-op implementation is its own package, but the API takes a dependency on it.
Then it should be fine as well, right?
**Carlos Alberto Cortez** 19:24 That could be weird.
And actually, that was one of the important things. If the… if we had to define global instances, like, global, like, everything, then the API would need to contain an op. But since global is not, like, a requirement, you know, we could probably relax that.
No opinions here? What do you think?
as a group, like, I know that, yeah, as I said before, most SIGs already have their no-op.
implementation part of the API.
My impression is that this sounds like normative language that we didn't use, but… That's what.
**Tigran Najaryan (Splunk Inc.)** 20:15 Sorry, Carlos, I'm not sure I understand what the question here is. Are you asking about whether no implementation should be part of the API package, or it can be a separate package, or whether… there… there can be a situation when there is no minimum… what exactly is the question?
**Carlos Alberto Cortez** 20:35 I would say it's the first two things you mentioned.
about, like, the nope has to exist, of course, but whether it has to be part of the API or not.
**Robert Pająk (Splunk Inc.)** 20:49 In my opinion, with specific, depending, you know, how modules, packaging, etc, is language and dramatic.
I think that, you know, for some languages, it can be part of the package of the API, a separate namespace, or something like that.
For others, you know, there are different distribution models. That's why I think the… I think the current, you know, this is… these are the library guidelines, and I think, as library guidelines, I really like this language. I think it's good. It shows, you know, what… what the design should look like, but having a normative language In my opinion, then can make more harm, because some people may have reasons make it a… you know, just… even the language may have different terms, and then even use AI or something, and it will tell you that it's not compliant, because the spec says that it's a must.
**Liudmila Molkova** 21:45 Yeah, like, can you even, like, is there, in the common sense.
Is there a way to not have any implementation without failing?
If it's two different dependencies people install.
And… language allows it to somehow to not have any implementation, and for somebody to call into it.
And not fail, then it's okay.
But it would return null.
Or some version of null, and then it would be… violate other principles.
It's like, I think it's just a summary of other principles we have.
**Carlos Alberto Cortez** 22:20 Right, and on that… on the relative, behavior, let's say. The thing is that… if you are writing instrumentation, like, if you are using… if you're writing native instrumentation, you would need to add a dependency to the API and the no op implementation, if they are separate, because you need to call something. So, you know, you're trying to do something, and then just swap it if the user specifies something else.
Which is interesting. And then there's the other thing, like, if you're writing, like, standard instrumentation, you don't have to declare a dependency to the noop separate package, but you only have it as a test.
Testing tie independency.
But yeah, it could be kind of interesting, because in some cases, I can imagine, instrumentation having dependency, like native one.
for the no-op and the API, which basically… kind of… It's just doing… It ends up doing what all the SIGs have.
**Tigran Najaryan (Splunk Inc.)** 23:24 So, the wording here was years ago, obviously, but the… when it says package here, he doesn't… it doesn't refer to any particular, specific definition of the term package. It doesn't try to refer to any Languages, definition of what the package is.
So, you can… This is deliberately loosely written in this… because in different situations, in different languages, you can… you are allowed to interpret this differently.
you have the two boxes there, the API and the minimal implementation.
there's nothing wrong in saying these are two, I don't know, jar files or whatever, if that's what you're aiming for, right? That, in my mind, it should be open to… developers of the particular implementation to interpret this in a way that matches the spirit of the wording there, right? That's what matters in my mind there.
Doesn't really matter how exactly.
what your distribution looks like, right? Do you package them together in one thing that is downloadable and installable at once, or is it two separate things? As long as the spirit of it is achievable.
And the wording there, I think, is, like, the caller shouldn't need to know and worry about that the minimal implementation is in effect.
As long as that is achieved.
it's fine. You want it in the same package, whatever is the definition of the package and the languages, you want them in the separate isolated things, I think that's also okay. I don't… I don't… I think we're… In some sense, we're splitting here.
**Carlos Alberto Cortez** 25:12 Yeah.
**Tigran Najaryan (Splunk Inc.)** 25:12 Doesn't really matter.
**Carlos Alberto Cortez** 25:14 Yeah, that's a good, take, and, just… for completeness purposes, currently, for example, it's not only the no-op. Also, there are some things like baggage, or spam context. Not spam, but spam context.
And baggage are implemented in DPIs at this moment.
So, that's something interesting, the separation, and I think this is the first time that I see that we may decouple them.
Yeah.
**Jason Plumb** 25:41 I'll just jump in, too, and give some more context from Kotlin, because Carlos is being, like, very thorough, and he's saying, I don't think you can stabilize your API unless you have a no-op, like, packaged with it, so… There's been a little bit of a discussion around that, and so this is hopefully getting an answer as to whether or not the spec… the spirit of the spec wants it to be included, or if it could be a little more idiomatic, depending on the environment.
**Tigran Najaryan (Splunk Inc.)** 26:06 I think you do need to know of implementation, one way or another, right? Because otherwise…
**Jason Plumb** 26:11 Yeah.
**Tigran Najaryan (Splunk Inc.)** 26:11 For sure. If you don't use the SDK package, then what is happening there? Something…
**Jason Plumb** 26:16 Likely.
**Tigran Najaryan (Splunk Inc.)** 26:16 Happens at runtime, that something is the definition of minimal implementation, really.
**Jason Plumb** 26:22 Yep. And as long as, you know, third-party libraries, applications, instrumentation is all coding to the API, then whatever instance they get is fine. It doesn't necessarily need to be packaged with the API as the counter argument, yeah.
**Tigran Najaryan (Splunk Inc.)** 26:36 Yeah, I agree with that.
**Jason Plumb** 26:37 Cool.
**Armin (Dynatrace)** 26:38 the whole spirit of this, and when we've added it back in the early days of OTIL, was to enable everyone to ideally have a first-party instrumentation baked into whatever framework they build, and make it cheap and unproblematic for anyone who's Not interested in, in gathering telemetry.
But also easy to set it up once you're… Starting to collect telemetry, but if… If you can make it in such way that you can easily Add first-party instrumentation without any… any resource burden to it, and without… Breaking the build, obviously, if you… if you don't come with any… any NORP implementation, then it satisfied what we are asking for here.
**Carlos Alberto Cortez** 27:23 Liudmila.
**Liudmila Molkova** 27:24 Is there any practical reason in separating them? Because… By separating them, you just make things harder.
and you add another breaking point for dependency version conflict. Like, any additive change to the API, becomes a compatibility problem with minimal implementation, unless there is some very particular dependency management that deals with it in some way. Like, why is it practical at all? Why is it… does it matter?
**Jason Plumb** 27:54 Yeah, I don't actually feel strongly about it, but I think other people in Kotlin do, and the answer I believe they would give, it's the same reason you would separate any packages. It's just they're separate concerns, and it doesn't bloat the API as much to have stuff in there.
**Liudmila Molkova** 28:09 But it, it, like, it's the purity versus practicality, and it introduces more problems than it fixes.
**Jason Plumb** 28:18 I don't know that in Kotlin that it actually does.
Because, especially if we're not creating a global instance automatically for people, I think it… I think it doesn't… but I'm… I'm open to hearing what sorts of problems it does introduce.
**Carlos Alberto Cortez** 28:35 Yeah.
**Liudmila Molkova** 28:35 Forever compatibility, yeah.
**Carlos Alberto Cortez** 28:37 Sorry, I want to say that, yeah, like, that's something that we're still discussing, but this was hopefully one thing that could have led to that. But we're still not sure, and… Personally, I would prefer if we keep the op with API, but yeah, that's something we're discussing. Sorry, you were going to say something, Liudmila.
**Liudmila Molkova** 28:56 No, I'm just saying that the problems suffer with compatibility, and that somebody who uses it needs to install two dependencies, or one needs to depend on another, and stuff like this. So, like, bloated package… well, it's not that bloated, it's a tiny package still, but, like, it's bloated was this for a reason. You cannot use one word without another.
**Jason Plumb** 29:21 I'm happy to keep talking about this, but I think we're at time.
**Carlos Alberto Cortez** 29:24 Yeah, we're on time, and I think we kind of have enough background and, sorry, context on this.
So it's like, we can, but maybe we shouldn't. Yeah, we'll discuss that in the cold and SIG. Thank you so much. Yeah, sorry for taking longer. Hopefully that was, Enough information for us.
And that's all from my side.
**Armin (Dynatrace)** 29:46 All good, thanks. Then back to the agenda, and… Continuing with Trask.
**Trask Stalnaker (Microsoft Corporation)** 30:03 Can you hear me now? Can I share?
**Armin (Dynatrace)** 30:05 Yep.
**Trask Stalnaker (Microsoft Corporation)** 30:06 Cool.
**Armin (Dynatrace)** 30:06 It's two both.
**Trask Stalnaker (Microsoft Corporation)** 30:11 So this is something that, we've discussed in the SEMCOM SIG the last two weeks, and just wanted to bring here for broader awareness and feedback.
So… as… We've been stabilizing database instrumentations in Java. This came up.
of what to do with server.address for, multi-server, or service discovery, cases. So, for example, client-side load balancing, SIG servers, service discovery.
Similar issue came up in RPC SEMConf recently.
And, through discussion there, we decided that server address… well, server address has always been the logical address.
And logical address in terms of RPC, if it's going through, like, a Zookeeper service discovery, it would actually be that that registry URL, that is your logical address.
And… If it's a gRPC target, that target is the actual logical address.
And… Of course, on any given request, the actual node that you connect to, should go in network peer address.
So, this is, so I have a PR up.
For this, and this is the key section, to read.
Basically, it breaks these cases down into, kind of, two cases. One is where you configure the database client with the… with server endpoints.
And that could be client-side load balancing, you know, that could be seed servers, but it's where you're actually putting in, database server endpoints into your configuration.
And so, examples of that… Well, obviously, the did generate case is a single server.
Multiple servers, and this just talks about what to do with the port, but it's just a comma-separated list of servers, including their ports, if, needed.
The other case, which is, Interesting is the whole service discovery case.
And so there's several examples of this that have come up in the Java database instrumentations.
so we've got Mongo.
I forget what this one… Was… which database, client. This was from… But in theory, you could use Zookeeper for a lot of things. And this is, Redis.
And so it's just kind of attempts to define, obviously, if there's a native, let's see… If there's a kind of native connection string, if you will. It should use that.
for example, that, or Zookeeper here. Otherwise, you know, it attempts to, normalize that a little bit. I think I might have lost a little bit of text here.
But yeah, it kind of keeps this a little bit generic. I guess in specific database cases, we could narrow this down.
So… And this, there's a similar problem in messaging, so this would carry over, in the future to messaging We are proposing this as a non-breaking change, under the… As a clarification.
Because there was just… There was no guidance at all for what to do in server… for server.address in this case previously.
Again, server.address has always been the logical address, and network peer address is the… the actual node that you're connecting to.
So, yeah, just… Wanted to bring it here for awareness, feedback, either here in this meeting or on the PR.
**Liudmila Molkova** 35:27 I just wanted to say that, I think it's a great change. It changes from no server address, no logical grouping, to some.
It's imperfect, but it's the best it seems we can do. This is the information we have.
And in theory, we can allow users to do the mapping. Well, they can do the mapping during cross-processing phase and assign some cluster name that they know of, or in theory, instrumentations can provide an option to map or set the server, the cluster, the proper cluster name of some sorts.
And it's just the fallback value that gives much better observability comparing to what we had.
**Trask Stalnaker (Microsoft Corporation)** 36:11 Yeah, so it preserves, you know, backends that are doing application maps and showing you your logical application map, at the server address level, as well as your physical, application map at the network peer address level.
Your metrics are better because the… you have this logical server.address in the metrics that is stable, low cardinality.
so, yeah.
Things are… things are better. It's… Might take people a little bit by surprise initially, seeing server.address as A comma-separated list of servers, or a service discovery, URL, But again, the benefits are, are big.
Cool. Back to… You are men.
**Armin (Dynatrace)** 37:38 Thanks.
We'll carry on with Josh again.
**Josh Suereth (Google LLC)** 37:44 Yeah, so, I've been, spending a bit of my extra free time on cleaning up the OpenTelemetry Proto repo, so I was gonna do a quick report and next steps for folks.
But basically, ran through… there's a new, agent triage skill for the Protore Repo that tries to extract themes from the different issues. I think it worked out really well.
And it gave us a set of things and kind of priorities. It tries to align those themes with what's going on in, like, the governance committee around projects that we have going on in OTEL, and kind of sort them out. So, the first one was build issues. I… I'm really happy that we're where we are now. I still think it's a bit ugly, but BuildTools is finally up-to-date against latest versions, and we have Renovate, will tell us when we're out of date on version, and try to give us an upgrade.
To have us, you know, pull in latest. For context, build tools is how we test Proto. It builds from source, and it pulls in a lot of, like, native build… C and C++ and libraries and Go. So that's fun, that's now working. Second, the docs clarification section in the triage is almost complete. We have two remaining PRs, I think these are both good changes. One is introducing a sense field on all the proto fields, so that we know where they came from. I believe that was, Tigran. I think you were the one who proposed it. Please take a look at what that looks like. It will put some extra burden on proto Maintainers. There's another clarification that I think was, it… Anyway, there's two PRs there, not super important. Profiling is active, as you know, in the protocol. There's a lot of things that the SIG is working on, so that's great. And then there's this other theme.
that I want to start addressing.
But I actually wanted to bring it here to talk about, because I think this is a little bit more significant, and will impact, kind of, SDKs and Collector. So, but this is on, like, transport hardening error interoperability. There's a set of bugs in this theme. By the way, we're down to about 30 bugs open in the Proto repo, so I think we're doing a good job of bringing it down.
This… this theme, though, is… effectively things like, what is the HTTP contact type matching for when you respond with protobuf error messages? Is it text? Is it proto? There was some mismatch there.
how are we gonna handle retry after? If you have a non-retryable response, currently the spec makes it sound like you have to put a retry after on a retryable response, right?
there's a lot of things around partial success, and I think we might want to actually re-evaluate partial success, do a bit of a retrospective on where it stands with OTLP, and figure out, you know.
to me, when you look at that combined with, like, retry after, also graceful shutdown, there's this notion of graceful shutdown, I think we might want to do a little bit of an evaluation on… OTLP, receiver, sender, agreements.
when to do retries, partial retries, retry after, there's a bit of a cleanup there to do. And so, what I'm looking for is if someone would want to partner with me on this, or if we feel like we have bandwidth in the SIG here to address this class of problem. It seems to me like stuff that is, you know, it's never been high enough priority to address in any individual bug.
But I think when you take them on the whole, if we can address these, like, as a consistent, you know, push to kind of, like, harden the protocol a bit, I think that'd be a good thing to do. So, I would like to propose that for this SIG. For context, the fourth theme was actually around trace metric Specification consistency. That is almost resolved, but there's a few remaining issues, specifically, like, I think it confuses people when, in W3C Specification, everything is about the parent span, and then when you write a span, you're talking about the span itself, and then when you're talking about a log, are you talking about the current span? Are you talking about the parent span? There was a lot of inconsistency in, not inconsistency, I should say. There was a lot of assumptions people made about which one it was, and no one agreed. So that's, the last issue to fix there.
But this transport one, I think, deserves some… some effort. So, I'm talking a lot, ranting, sorry. Transport… hardening, error interoperability, like, how we want to deal with partial retries, resets. Is anyone interested in partnering with me to try to bring, some proposals instead of these issues to this meeting?
For review and adaptation.
**Tigran Najaryan (Splunk Inc.)** 42:40 Josh, I can help at least review what you do there. Not entirely sure how much time I will have to partner fully with you, but… At least you can count on me to take a look at what you have there.
For the transfer bits, yeah.
**Josh Suereth (Google LLC)** 42:55 Yeah, I wasn't… for some of these, I wasn't sure if putting a PR makes sense, or putting a proposal and an issue and getting comments on that makes sense first. Like, whatever you think is going to be easier.
**Tigran Najaryan (Splunk Inc.)** 43:07 Yeah, it works either way, whatever you prefer.
**Josh Suereth (Google LLC)** 43:10 Okay.
**Tigran Najaryan (Splunk Inc.)** 43:11 If it's on the issue, I'd… tag me, because I don't necessarily receive the comments on the issues I'm not… I'm not part of.
**Josh Suereth (Google LLC)** 43:21 Yeah, that's… that's… that's fair. Okay. And then… So… addressing this now, does anyone have concerns with us, with this taking time from other efforts at OTEL? Like, does… I'm not planning to open a formal project proposal, I'm just planning to put this as individual PRs. Anyone have concerns with that?
**Tigran Najaryan (Splunk Inc.)** 43:44 No, I think it's fine, this is a cleanup work, we should do it. We'll do it carefully, we'll make sure we don't break stuff, but yes, let's do that cleanup.
**Josh Suereth (Google LLC)** 43:53 Great. I don't know if I'll be back next week with a proposal around this, but my plan is to work in the extra time that I have on Getting a proposal for, like, a co… Taking all of these bugs and solving them with one proposal?
And then kind of closing them simultaneously, I think, as opposed to trying to nitpick and address them one at a time, because there was a theme there. So cool.
**Tigran Najaryan (Splunk Inc.)** 44:18 If they are… if they are related, I agree, but, Doesn't have to be like that, right? We can go one by one.
**Josh Suereth (Google LLC)** 44:24 No.
**Tigran Najaryan (Splunk Inc.)** 44:25 well.
**Josh Suereth (Google LLC)** 44:25 I'll split it back out. I think the thing I really want to focus on is around partial success.
and some of the, like, partial success retry behavior. And then, once I have a pros around there, we can figure out what issues are unrelated and solve them separately. But that's the thing I wanted to talk about. So, great.
Does anyone have any feedback on partial success or problems they've run into that are not encoded in these bugs that they'd like to bring up so that that's accounted for in the proposal?
**Joshua MacDonald (Microsoft)** 45:05 Do you have a plan to specify how the collector should propagate partial success, or has that been… has that been requested?
**Josh Suereth (Google LLC)** 45:13 That has been requested. That is, if you look… if I… the clarify HTTP content type matching for protobuf error status responses is part of the partial requests issue.
So, I don't think this is, like, again.
Specifically, like, asking how should the collector respond?
is the thing that I think needs to be written. If I just address this bug as written, we might not do that. And that's why I want to do a bigger effort around understanding partial success problems. So if you… if you want to, like, write a new bug, we could mark one as duplicate of the other, with, like, concerns you have.
I'm just trying to collect all the issues now, so we address the right problem.
**Joshua MacDonald (Microsoft)** 46:00 I don't want to sell a new bug. I do want to pay attention to what you're talking about, though. I'd be glad to review. I think this is an important one. I would even throw in content negotiation if you're gonna… if you're gonna step back and look at the protocol like this.
**Josh Suereth (Google LLC)** 46:13 Okay, content negotiation is something I want to do after solving the existing bugs. So, like, right… like, my expectation for the proto was, let's resolve all the issues we have, and then we start looking at new evolution things, yeah.
There is a bug for content negotiation, by the way. I don't remember what theme that was in. It's not in this theme, though.
Okay, great, that's all I had. Thanks, everybody, and I'll let you all know, I think this is too important to, like, have it just show up as a PR without people paying attention to it. I'd like to have discussion here. I will bring it when the proposal's ready.
**David Ashpole (Google LLC)** 47:03 Cool.
I think I have the next topic, so I'll be quick.
A few months ago, I worked on adding the max export batch size.
In the periodic reader and metrics.
We now have 3 implementations.
And the configuration is defined as well, so I'm looking to stabilize this.
I did make some tweaks last week to the spec language to clear up a few things that were uncovered when we Did the first few implementations.
It looks like there are already a couple approvals, so thank you for people who have taken a look, but… Please approve if you support it, or if you have any concerns, feel free to raise them on the PR, or… send them to me in Slack.
Thanks.
**Armin (Dynatrace)** 48:00 Any input on this one from the round?
Alright, then Michal is the next one here.
We can't hear you, at least I can't.
**Michal Jarmolkiewicz** 48:40 Can you hear me now?
**Armin (Dynatrace)** 48:42 Yep, no directs.
**Michal Jarmolkiewicz** 48:43 Yeah? Okay, great, sorry for that. Okay, so I would like to bring up topic of optional folder endpoint. So, basically, today, Autel PX photo supports only one endpoint.
And when absent to the metridor retries, and if the destination is unreachable, the dot bar is basically dropped.
The usual fix for it is a load balancer in front of the pool of collectors, and that basically works well when the app sends to one strip to the pool.
Yeah, but in some deployment, especially a collector sidecar in the same pod, the app sends to local host. There's no load balancer on that path.
They just hop and lock up sidecar. If the sidecar is down, yeah, we basically are using clocks.
So, yeah, we are proposing an optional fallback endpoint in all the LPX filters.
Same configuration style as we already have for the primary endpoint.
Yeah, and basically that's all. I'm looking for some feedback, and maybe sponsor, and yeah. Thanks.
**Tigran Najaryan (Splunk Inc.)** 49:50 This is suggesting to… have this functionality in the SDK exporters, right? Not the collector exporters.
**Michal Jarmolkiewicz** 49:58 Yes, in SDK.
**Tigran Najaryan (Splunk Inc.)** 50:01 And that would be, I guess, my question, why in the SDK and not in the collector?
And my reasoning would be that this is requiring now multiple languages to have this logic implemented, whereas… We relegate, typically, the complicated scenarios like this to the collector.
Where you implement it once, and you can have a locally running collector which takes care of this problem.
Have you looked into that possibility, the alternate?
**Michal Jarmolkiewicz** 50:32 Yes, of course, but yeah, we were thinking about what happened if that collector is down, or something happened to it, and the application, you know, just wait for it and drops, block, blocks.
**Tigran Najaryan (Splunk Inc.)** 50:45 Yeah, I'm talking about the locally run collector, the idea being that it's Should be up and running.
There's no reason for it to be down, it's local.
You're not reaching out over the network to that collector.
Which is our default recommended configuration. You have your application and the SDK experts to a local collector on the local host.
And then you delegate the complicated logic like this, or other complicated stuff to that collector to take care of.
**Michal Jarmolkiewicz** 51:21 Yeah, you're right, it can be done with a collector to their, like, you know, to have some persistent memory of there.
But yeah, still, our problem was that we preferred to Have this option as soon as possible near the application.
**Tigran Najaryan (Splunk Inc.)** 51:46 Okay.
Anyway, I… that's what I'm seeing here, right? A significant effort.
For the entire project, multiple languages have to implement this.
Compared to a smaller effort in just the collector.
My preference would be that we don't do this in the SDKs.
There's many other things that we can do.
Potentially.
in the SDKs that we choose not to do.
And with the exact same reasoning.
So, my default reaction to Puzzles like this is that, okay, go do this in the collector, and if there's a good reason not to do it in the collector, only then consider SDK as the place for it.
**Michal Jarmolkiewicz** 52:40 Okay.
So, I guess I will just close the issue and, yeah, that's all, thanks.
**Robert Pająk (Splunk Inc.)** 52:54 I can only be sure that… I think there are also other pops.
Can also create, you know.
You can even create your own little tool, for instance, Go application, who will be just kind of like a load balancer, which will be just responsible for these fallbacks, etc. And you will just, you know, send these things to your to your sidecard if you're just worried that the collector is a bottleneck and it crashes, so you can always, you know, create a little Go application which just does the thing that you request here.
**Armin (Dynatrace)** 53:27 The little Go application could even just be a custom Opal Collector built using OCB that just has OTP in and then load balance out.
**Robert Pająk (Splunk Inc.)** 53:38 Exactly.
**Jason Plumb** 53:39 I'll offer a counterpoint, though. I think a lot of… there are, I think, still a lot of users, a lot of teams out there that don't necessarily feel the need to manage and run another piece of software, like a collector, when they just want to throw a language agent at a piece of software and have it do direct ingest to a vendor. Like, I think those… I think there's lots of teams out there doing that.
**Armin (Dynatrace)** 54:04 That's certainly the case, but there, the endpoint itself is something that would abstract that load balancing away, right? You will have that one point that a SaaS vendor Interest endpoint, and then… then they would take care of it on their end.
**Jason Plumb** 54:21 Yep.
**Robert Pająk (Splunk Inc.)** 54:22 Yeah.
I agree. I think… I think that… yes, I think what Jason says, that persistent local storage is something different, and yeah, I think it will be more usable if you know that what is unreachable or something like that, right?
That's another story, I think.
**Armin (Dynatrace)** 54:39 And even in an even larger implementation effort that would probably rather not be spread across all language SDK implementations, but… Something for the collector as well.
**Jason Plumb** 54:54 And implementing a robust, like, fallback mechanism in SDKs is actually, like, considerably complicated.
**Tigran Najaryan (Splunk Inc.)** 55:08 Yeah, this is… in no way, this is a trivial feature to implement and get it right.
in all the languages, it's, yeah, it's a significant effort. I'd rather do it once.
And make sure it's done correctly in the collector.
Then try to do it in 10 different languages.
**Armin (Dynatrace)** 55:35 Yeah, thanks for the point to stemmy here. Is that a direction that's helpful for you? Is that something you would like to reach out to the collector folks about?
**Michal Jarmolkiewicz** 55:43 Yeah, I'm just currently thinking about it, because first year, when we think about SDK, But, yeah, I would basically need to get some more knowledge on Collector, and if… maybe it's already possible to do it up there, and the problem is solved, basically.
**Armin (Dynatrace)** 56:02 Alright, thank you.
**Michal Jarmolkiewicz** 56:04 Thanks.
**Armin (Dynatrace)** 56:07 then that would be it, as far as our agenda today goes, do we have any last-minute topics?
Then let's call it here, 5 minutes back to everyone.
Have a nice rest of your day. Bye-bye.
**Trask Stalnaker (Microsoft Corporation)** 56:28 I…
**Reiley Yang (Microsoft Corporation)** 56:30 Bye.
