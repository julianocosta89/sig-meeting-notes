SIG: OpenTelemetry Specification SIG + Maintainers Sync
Date: 2026-10-20
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Ted Young (Raintank, Inc. – Grafana Labs)** 00:45 Jason, is that the Timberline Lodge you're staying in?
**Jason Plumb** 00:50 Yeah, it appears so, doesn't it?
**Ted Young (Raintank, Inc. – Grafana Labs)** 00:52 Yeah.
**Jason Plumb** 00:53 Yeah.
**Ted Young (Raintank, Inc. – Grafana Labs)** 00:54 detecting.
**Jason Plumb** 01:00 Yeah, I thought I used to have one with the twins down at the end of the hall, but I can't find it anymore. Lost it.
**Ted Young (Raintank, Inc. – Grafana Labs)** 01:06 Blast.
**Jason Plumb** 01:08 Yep.
**Carlos Alberto Cortez (Dash0)** 01:12 Hey, hey everybody! Let's wait a couple of minutes, before we start.
In the meantime, please send me important items in the agenda. We have already a few items.
But probably we have enough time, and if you add an item, don't forget to put the time you think you will need trained to be, of course, you know, kind of respectful with the time of You know, other people, so other people can put their own stuff, etc, etc.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 01:44 I was planning on using the first 50 minutes, I hope you don't mind.
**Carlos Alberto Cortez (Dash0)** 01:49 That's fine.
Okay, one more minute, let's wait. I think that's enough, we have 10 people, By the way I like your new look, Teth.
Also, don't forget to put your names in the attendees list.
Okay, we have 15 people now, so I think we're gonna start, let me share my screen. Unless you, Jack, want to share your screen, what do you prefer?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 02:48 I'll share it, and then I'll hand it back to you when I'm done with the SIG heartbeat update. How about that?
**Carlos Alberto Cortez (Dash0)** 02:54 Yeah, just give me 15 seconds, basically just, there's a new release, PR, please review that, and take that into consideration if you're going to merge anything today.
You go, Jack.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 03:05 That's right. So, please review this.
1.62.0 release of the spec.
Okay, so, I have the first topic. It's, it's a SIG heartbeat, for the Java SDK and instrumentation SIG, which I'm a part of, and just to remind folks what SIG heartbeats are, we talked about them last week a little bit. So, what we're trying to do is we're trying to have periodic updates from every SIG in OpenTelemetry in the spec call. There's a lot of them, so that means they're going to be infrequent. That's okay. The format is, you know, the default is just a 5-minute lightning talk, where you give updates on… based on this, you know, short prompt that we have right now, and that we're going to be evolving over time in response to feedback. But you can go longer if you need to, so if you need 15, 20 minutes, that's fine, too. You have lots to talk about.
And the purpose of this is to promote the notion of the spec call as the hotel town square, to keep the community in the loop of current activities of SIGS, and to recognize recurring challenges across SIGS so that we can, create structural solutions to them. So, yeah, Alex gave one last week. There's been a number of them that have happened, over the course of this year, and, you know, just to continue the The pattern, I volunteered to give the Java update. So, okay, JavaSIG.
It's the SDK and instrumentation. Some languages have separate instrumentation and SDK SIGs. We have a combined one. We all kind of work together. And our main assets that we have are the OpenTelemetry Java repo and OpenTelemetry Java Instrumentation. The instrumentation contains instrumentation, and we have this thing called the Java Agent, which bundles up all those instrumentations and automatically installs them And applications.
And it's quite good.
So, you know, the first thing, you know, okay, what are the three most important things for your SIG?
there's this thing that we have called the Instrumenter API, and so this… this is… maybe some folks have heard of, maybe some folks have been aware of this, but in Java, we have somewhere between 170 and 250 instrumentations, and it depends on how you count them.
And the Java ecosystem, I would consider it, like, pretty fractured. There's lots of HTTP libraries, there's lots of messaging libraries, there's lots of libraries to do the same thing. And so, having this many instrumentations is sort of a necessity. It reflects the ecosystem. And the Instrumenter API is this crucial abstraction that we have that helps us make sense of this… the vastness of the set of instrumentations that we have to support. And, you know, what it is in a nutshell, is it is a… It's a library. This is not what I meant to link to. That is the wrong link. Alright, let's see if I can find this on the spot.
I'm gonna update to this link. Alright, so it's a library that, we use.
And so, we don't call the OpenTelemetry API directly to record spans or metrics in Java instrumentation. We call the Instrumenter API, and the Instrumenter API sits on top of the Trace API and the Metrics API, and ensures that we record spans and metrics in a standardized way for standardized things. So basically, it helps make… it helps ensure that, you know, the 20 different HTTP client libraries that we have to support all perfectly conform to the HTTP semantic conventions. As long as we can properly, like, encode those into the instrumenter API, then we can ensure that those 20 different instrumentations all produce Spans and metrics with the same shape.
And so this… this is a… this is a nice little concept. I think a long time ago, some people were trying to have this type of thing landed at the spec level. It didn't really go anywhere, but, you know, this is something to look at if you're working in a language that has to maintain a lot of instrumentation and is looking for ideas on how to maintain consistency and quality.
So, yeah, the Instrumenter API. I need to update that link.
So… Guess I'll do that real quick.
So that's a really important thing to our SIG. We have lots of instrumentation, and the instrument or API helps us ensure quality and consistency and maintainability.
Another important thing for our SIG, we have this, an upcoming Java Agent 3.0 release. So, there's a blog post about this where we talk about the main changes. And so, just really quickly, we're selective in the Java SIG and how we think about major version bumps.
The API and the SDK are still on 1.x, and want to keep it that way indefinitely, but the Java agent and Java instrumentation does do major perversion bumps, and we want to continue doing that.
So we don't have a fixed schedule for this, but roughly, it's maybe, like, every year and a half to two years, that's what's happened so far. The 3.X's release is imminent, and the 2.X was about 20 months ago, and our basic pattern is we are going to continue to support bug fixes and security patches for the last major version plus the current major version. So, the introduction of this new major version, 3.x, basically means that the 1.x major version is, like, phasing out of support.
And, yeah, like, what we do with these major version bumps of instrumentation, which come every year and a half to two years, let's say, is we bundle together lots of breaking changes to, like, to instrumentation. And typically, that takes the form of, like, major version… major changes to semantic conventions. And so what the 3.X release includes is It's a bump to the stable database conventions, so that… there's a bunch of changes there.
It's a bump to the stable code conventions, so all of the, you know, all the code annotations that we add to our telemetry are now using the stable semantic conventions.
And this one isn't… this last one is a… it's not a stable change, so… but, you know, we're updating to the latest version of the messaging instrumentation convention. So we're on a really old version of the messaging conventions, 1.24, and we're updating to 1.43. And even though 1.43 isn't stable yet.
I think the logic here is roughly that, like, 1.24 is just, like, dramatically out of date, and so, you know, we needed to update just to modernize a bit.
So, yeah, upcoming Java agent release, and so if, you know, if you're working at a company that builds off the instrumentation, look out for these changes. Breaking changes are coming.
But, they all reflect the semantic conventions.
So, I couldn't think of the third most important thing for the SIG.
And some of the lines blur between things that I want to talk about in each of these questions. So, what do you need more of from the GC and the TC and the community?
I think the thing that we need more of, primarily, is more people pursuing approver and maintainer. So, things are not going as well as the numbers suggest. If you look at the rosters of our approvers and Maintainers. So just, if I go to these real quick.
you know, for… this is the Java Core repo, you know, it looks like we have two Maintainers, and we have… 6 approvers, and over in instrumentation, We have… 2 Maintainers and 7 approvers, but the problem is, is that, basically, everyone is double-dipping and is, you know, has lots of responsibilities outside of this, and, And the scope of each of these repos is just huge. And so, you know, we've been trying to solicit more people to pursue being an approver or maintainer for a long time, and I guess synchronously on this call.
I know a bunch of you work for observability companies, so if your company has people that are Java experts and are interested in getting involved in OpenTelemetry, please, please reach out, please get engaged and attend the SIG and… Yeah, we'd love to have you.
The other thing… actually, let me pause, because Robert, you have your hand up. Do you… do you want to ask a question at the end, or is it an appropriate time to jump in?
**Robert Pająk (Splunk Inc.)** 11:46 It will be a bit better at the end, I think.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 11:48 Okay, okay, then I'll come back.
Okay.
what else do we need from the community? Another thing we need, or we would really like, is a stable instrumentation config API. So, for some of the folks, you might be familiar with declarative config. It went stable, earlier this year, but it didn't go stable all the way. Selective parts were held back, and one of the pieces that was held back is this Instrumentation Config API. And so, if you're not familiar with this, this is the API portion of Declarative Config, and the callers of the API are supposed to be instrumentation libraries.
So, it's not about configuring the SDK, it's about providing an API that can standardize the configuration of instrumentation libraries. And, like, you know, the elevator pitch of this is it promises to provide language-agnostic, highly expressive instrumentation config, such that you could have a single configuration file that dictates the behavior of your HTTP client library instrumentation across your whole environment. So, like, you know, not everything you want to configure is about the SDK, or your OTLP exporter, or your processors. Sometimes you want to configure the instrumentation mechanics, like which HTTP headers you capture, or whether you collect, like, the full database statement.
And other things like that, like, you know, different obfuscation things. And the instrumentation config API is, like, the language agnostic answer to that. So, this is primarily blocked by prototypes and other languages. I've linked to an issue here. There are implementations in Java and PHP But, you know, in Java, we've really leaned into declarative config, So much so that, you know, internally, all of the instrumentation libraries use the declarative Config API primarily, and, you know, there's actually just a shim that delegates to, you know, environment variables if you're not using declarative config. So, we would like declarative Config to be the, you know, the first answer, and, you know, we're… making a bunch of changes to move in that direction. And instrumentation config is sort of a missing piece there. So, if you're a language maintainer, and this idea of language-agnostic instrumentation config resonates with you, please reach out and get involved with this issue.
That could help unblock us.
Yeah, so that is sort of the end of my spiel a bit. You know, there's this last question, which is, what's a thing your SIG does that no one else does? And, yeah, let me back up, I guess, because I was planning on looping in Trask for this one. One of the things that we do, or that I observe us doing, is over on the instrumentation side of things.
Trask and team has sort of become prolific users of AI to, to… lessen the review burden, to help maintain just this huge catalog of instrumentations that we have, and he's done a lot of really interesting things to do that. And so, Trask, if you're here, I think I saw you on the call earlier, if you could jump in and maybe share a little bit about what you've done. And if you want to drive, I can hand over the screen share to you.
**Trask Stalnaker (Microsoft Corporation)** 15:10 Yeah, yeah, I'll share for just a minute.
So, primarily wanted to share just how, you know, this doesn't happen automatically, getting benefit of good copilot reviews and good, you know, agent, behavior, but I wanted to share. So, we've, And I'm not totally sold that this is the way to organize this, but we have an agent knowledge, section in our repo, that we point all the co-pilot review towards. And just to… we kind of wanted to share, you know, like, that it takes… it takes a lot of effort, but there's a lot of payoff.
So, for example, I checked, and since we've started doing this, we've sent 190 PRs just updating the knowledge articles themselves.
And, kind of looking in the past 3 months, these are the kinds of things that, we… continued to improve, you know, coding style, obviously. Testing verbosity and readability, right? Like, the agents often, don't get this right, right away. Documentation, unnecessary, you know, code, like, very, like.
specific things to our repo, not just, like, generically, don't write unnecessary code and don't over-engineer, but, like, specific things in our APIs, specific ways that we see, AI agents kind of misbehaving and producing PRs that don't conform to what we'd like.
And… Yeah, and then a way that we benefit from that, obviously on our own PRs, then, we benefit from that, Having to cycle through, you know, reviewing our own code less, or having to massage our own code less for it to be… more like a human PR versus AI bot. But also, the co-pilot reviews. So, I know a lot of repos are using this pull request dashboard now, but not many people yet are using, it has a feature where… Before PRs… so PRs are waiting on authors for stuff, and before it will go into waiting on reviewer, it will force a, another co-pilot review. Basically, it'll ensure that you have a clean co-pilot review.
So, what that happens… A lot of people have set up sort of that automatic first review on PRs.
What this does is then, after it continues to ask for another co-pilot review, that people then, you know, reply, and once it's clean, then it will pass on to the reviewers, and so that helps by the time that we spend time on it, reviewing it.
It has already, you know, conforms, much, much better to our kind of repo standards.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 18:34 Yeah, just to parrot something Trask said, in my own words, because I watch him do a lot of this and use this tooling in our SIG calls, and So the Java Instrumentation repo just has, like, massive PR volume, and just being able to ensure that once the PRs get to the reviewer, Trask and Lori and other folks, that they've passed all of the code style, the code quality, you know, idioms that the repository has encoded, that allows the reviewers to focus on like, the meat and potatoes of the issue, rather than getting into the lower level details. All the lower level details have already been sort of ironed out by the time the reviewer spends effort on it, and I think that's kind of one of the key levers.
**Trask Stalnaker (Microsoft Corporation)** 19:26 Yeah, Liudmila.
**Liudmila Molkova** 19:29 I know the answer, but I think it's very useful. Maybe one of you can share about the contract management, how you have two different repositories for instrumentations, and what goes into one and what goes to another.
**Trask Stalnaker (Microsoft Corporation)** 19:44 Yeah, so we have the instrumentation repo, which is, As Jack said, there's about 180 or so instrumentations in there.
This one doesn't follow the kind of contribib model, where, so, there… we don't have component owners per instrumentation here. This is actually owned by the maintainers and approvers.
We… and so this is sort of, like, yeah, the things that we focus most on. We also have a contribib… Repo, which is the more common, like, component owner style, repo.
And so, things that, are… less… critical to… us, us meaning, I guess, vendors, maintainers, people who are, have lots of customers on this, code, Yeah.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 20:51 Yeah, so that's kind of inconsistent in OpenTelemetry, right? Some languages have a contribibrepo, which is basically the home for all of their instrumentation.
And, you know, we sort of go in a different direction. We have the instrumentation repo, which is the home of all of our instrumentation, which is sort of… I describe it as, like, it's all bottom-lined by the maintainers and approvers. So, whereas, you know, the Contrib repo is, is… is more… I don't want to say Wild West.
But, there's less strong ownership, let's say. But because, you know, we do have this large catalog of instrumentation, which is bottom line, we can ensure that the Java agent is, you know, maintains, like, a high level of quality and good user experience as a result.
**Liudmila Molkova** 21:49 And you, sometimes, do you promote things from Contrape, if they are, like, proven to be useful?
And good.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 21:57 We promote things… so Contrib is actually… some… some of the things in here are instrumentation, and some of them are, like, SDK extension components, like, you know, exporters and samplers and things like that. And, you know, the… if we're talking about SDK extension components, well, we promote those to the core repo as soon as they are in the spec. Like, you know, that's the scope of the core repo. If it's mentioned in the spec, then we can include that component in there.
Instrumentation that lives in Contrib, it's a little bit more fuzzy if and when it gets promoted to the instrumentation repo. I think, just to, you know, channel Trask for a second, I think it's like, you know, does one of the Maintainers in the instrumentation repo want to commit to maintaining this?
If yes, then, like, you know, it'll live in instrumentation. If not, then it lives in PintRib.
**Trask Stalnaker (Microsoft Corporation)** 22:49 We've refined that a bit in terms of leaning on semantic conventions, that if there is a semantic invention for it, so we will… For the most part, we accept most, like, messaging, HTTP, database, GenAI, RPC, instrumentations into this repo.
But if it's something outside, then, We don't, because we are… semantic dimensions makes it very easy for us, right, from a, like, what should this repo… what should this instrumentation produce, which… what is good telemetry, which is a very challenging aspect of instrumentation.
And so, that helps us not get into those weeds.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 23:43 All right, well, we're at the… I don't know how many minutes… 20 minute mark, probably, so, why don't we… why don't we move on to the rest of the agenda? Thanks for listening to us, and if you… if you're a maintainer and you're interested in giving one of these, you know, reach out to Alex or I, and if, you know, we're also going to be proactively reaching out to different Maintainers, so, you know, you may see us in your inbox either way.
Thanks.
**Carlos Alberto Cortez (Dash0)** 24:15 Perfect, thank you so much. Moving on then, Robert, you have the next three items you want to share? I can share for you otherwise.
**Robert Pająk (Splunk Inc.)** 24:22 You can share, it should be quick. I think it will…
**Carlos Alberto Cortez (Dash0)** 24:26 Sweet.
I want to apologize for this, thing about storage. I tried to buy that, actually, and it's not working anyway.
You're the first one.
**Robert Pająk (Splunk Inc.)** 24:43 Okay, so this is a PR regarding, like, updating the versioning policy so it captures also the security, how we approach it.
for the SDKs and APIs. It has already a bunch of approvals, but I just wanted to call it out here to make sure if anyone is interested here, just to double check, and I think we can also approve… merge it before the release, Carlos, unless you have some concerns.
There is a… and there's also a connected blog post, because I think it's worth calling out to our end users how we are approaching the security that we are taking… that we care about end user security.
And, the doppos is dropped, because first I want to have this one merged.
And, yeah, any questions?
Yeah, you could…
**Carlos Alberto Cortez (Dash0)** 25:34 This is the important part, probably, for people to review, in case…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 25:43 Robert, can you give us a… A 30-second elevator pitch for what we're doing here?
**Robert Pająk (Splunk Inc.)** 25:52 So, It will better review, but long story short, we accept things which may be considered as a breaking change in some, you know, edge cases.
If we find that the existing configuration or behavior is not secure.
And in the PR description, I also added examples how other, you know, like, things like languages, like OpenSSL has approved it. For instance, a change if TLS 1.2 will occur to not be secure. We may, for example, disable it by default in some future readies, if there will be some vulnerability.
and things like that. So, if something in the future will be considered as unsafe, we may disable support for it. That's one option. Second is, you know, like, second is, like, we may add some limits, which things are right now unbounded. If we find cases.
where people can attack and, you know, just inject some stuff from outside and make unbounded, you know, member usage or whatever, we also may change it. And yeah, that's it. And I try to do it as specific here as possible.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 27:05 Thanks for that.
**Carlos Alberto Cortez (Dash0)** 27:09 Yeah, I think that the thing that got me calm about this one is that there's enough prior art, you know, here, like, different cases where SIGs had to face this situation.
I think that's a good one.
**Robert Pająk (Splunk Inc.)** 27:27 Let's move to the next one.
So, this one is kind of a little bit nitpicky.
But it was called by Codex when I was doing a review before making our OTLP log exported stables. Right now, the specification says that if you go to the changes, file changes.
it says that export must not block identity. Sorry for my English. The thing is that, it's… I don't think it's really realistic.
for things like std out exporters, or file exporters, when you just write, and you… in most languages, you do not have control to interrupt when the file is locked, or you're just in progress of writing to a file.
you cannot really, abort it, unless… and I even checked, and we are not doing anything like that in Go, Java, and .NET, and probably other languages as well. So this only adds an exception, that if we are not having an a network I.O. thing, or something which basically exports to a destination, which does not support cancellation.
Then, it can block.
Because it doesn't make sense, probably, to create some separate thread that will just, you know, still be blocked in the background. Yeah, and that's it. Any questions?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 29:05 Yeah, so… I was just thinking as you're… as I was reading that PR real quick, and It must not block indefinitely, and I think the… indefinitely, I just looked it up, and it has kind of two meanings. One, it means unlimited, and you know, I'm thinking about system outprint Line, and, you know, it's not gonna… it may block, but it's not unlimited.
And so, in that definition of indefinitely, even system outprintLine and these other, like, synchronous operations are not blocking for an unlimited amount of time. But indefinitely.
It also has another meaning, which is, like, unspecified.
And, I think they are blocking for, like, an unspecified amount of time. And so, you know, if it's the unspecified definition of indefinite that we're trying to avoid, then I think this clarification is needed, but if it's the unlimited, then I think these… these synchronous operations, they don't take unlimited time.
**Robert Pająk (Splunk Inc.)** 30:05 They can.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 30:07 They can.
**Robert Pająk (Splunk Inc.)** 30:08 Yes, they can.
I know for one rest assured that they really can.
**Carlos Alberto Cortez (Dash0)** 30:13 Well, you have an example, like, that is… should be obvious, but it's not.
**Robert Pająk (Splunk Inc.)** 30:20 Yeah, there's an example where it should not. In all other cases, there must be a reasonable finite number, and exporters that must perform network I.O. must enforce this upper limit. That's the example.
In the second paragraph.
Anyway… I think the easiest way to follow up would be to do it asynchronously and just leave comments here, if you find any language that will fit better, and also make it more clear.
**Carlos Alberto Cortez (Dash0)** 30:58 Do we go to the next one?
**Robert Pająk (Splunk Inc.)** 31:01 Unless Jack wants to comment here.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 31:06 No, I just… I… I don't know.
I have this general feeling that, like, the spec is full of a million bugs that you can find, depending on how pedantic and precise you want to be. And I think the spec can end up reading horribly if we try to fix every single one of those little bugs and make it ultimately, like, as precise as possible.
And so, in my head, I'm trying to, like, figure out where the line is to draw, because there's, like, kind of the common meaning, and then, like, the literal meaning, and and that's kind of what I'm grappling with.
**Robert Pająk (Splunk Inc.)** 31:44 So this one was using, you know, normative language. We make a spec compliance review, and maintainers want to have it clear.
So, it will help making it stable. So we just want to make clear, and we… initially, we made it smaller changes, but the feedback so far was to make it more explicit. So other Maintainers prefer to have it clear.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 32:09 Alright.
**Robert Pająk (Splunk Inc.)** 32:11 Okay, Carlos, I think we can go to the next one.
**Carlos Alberto Cortez (Dash0)** 32:15 Okay, let's go for that.
**Robert Pająk (Splunk Inc.)** 32:21 This one has a lot of approvals, I just want to call out that we'll merge it. And right now, I think all of this… all of the CART implementations, at least at the time when the PR was created, was not, following this thing which is defined in this PR, and in my opinion, what the PR proposes here is the right thing to do. I think Tyler is here on the call, I don't know, Tyler, you're going to add anything, or what I described is okay.
Or maybe Tyler's not here.
Okay, that's it from my side.
**Carlos Alberto Cortez (Dash0)** 33:07 Okay… And the plan is to merge today, right before release. Okay, that makes sense.
Okay, let's go to the next item. Liudmila, David, you want to share? I can share for you otherwise.
**Liudmila Molkova** 33:24 I'd like to share.
**Carlos Alberto Cortez (Dash0)** 33:26 Perfect.
**Liudmila Molkova** 33:28 So we started the discussion with David a few days ago, and Also, we had this on the semantic conventions call yesterday.
just checking if David is here, I don't want to talk without him.
**David Ashpole (Google LLC)** 33:40 Yeah, yeah, I'm here. I didn't do my homework, though, so I don't have any written up Thing for you yet.
**Liudmila Molkova** 33:46 It's okay, I also did a poor job with my homework, but anyway. So, I've done a little bit of a homework.
So, the… the discussion.
We… in semantic conventions, we kind of have a thing for signals called requirement level.
We document it inconsistently for different signals, and it's essentially not part of the specific, not part of the schema.
The interesting part where it comes to specification is whether we should have some API that… That allows you to enable individual telemetry.
not telemetry items, I call it signals, but apparently it's not clear. So, like, a specific span, specific log, or a specific metric definition.
And an example, sorry, the… Spec part is… I think, David, you would like to introduce the advisory parameters for metrics. That would essentially mean this. If the metric is obtained.
Then it's kinda disabled by default, but users can change it, and it's controlled with metric views, and it's configurable probably through declarative config.
And then the instrumentation code would provide this default advisory parameter, and then the SDK would go no-op if it's truly disabled, right? The instrumentation code does not need to know about the state, about the configuration.
**David Ashpole (Google LLC)** 35:27 Right, it just needs to pass the requirement level through the API.
**Liudmila Molkova** 35:31 Right.
And there is a separate work stream Jack has started that would Result in semantic conventions defining configuration options.
And in my mind, these are two problems that are, if not the same, but very close.
And this is an example.
So, for… Let's start this metric.
something very non-controversial. So, we have something like container CPU usage, and all the usage metrics are opted in, because they are, they can be derived from other metrics, right?
A little bit verbose.
And we currently can do this, we can call them opt-in.
And we do.
And the alternative circuit configuration, if we've done it.
It's completely imaginary, it does not exist, I just printed it here for the, to make it more clear. So these things are kind of related.
And if you wrote a configuration for this, this would become redundant, because by saying the default is false.
You are saying, okay, it's gone.
Plus this has nice effects of, like, if we have this option.
it can be even the same global option across different CPU usage metrics, container, Kubernetes, and whatnot. So, like, you can toggle them together, or one by one. But anyway… So, the first point I'm making, these things are… The same in nature.
But the second one is way more expressive.
**David Ashpole (Google LLC)** 37:20 I mean, I think the… So that, right, the trade-off is… What we're really talking about here is… Whether we want configuration to be… on the SDK?
Or whether we want configuration to be… On the instrumentation library, right?
So, if it's on the instrumentation library, then it can be Extremely specific to… Not just that metric and semantic conventions, but it could be specific to, like, that method of doing instrumentation, even, right? So it could be, like, as specific as you want.
For that particular implementation of the convention, right?
If it's on the SDK, that means it can actually be more general, right? So… I could have… Like, you can use a general configuration option, like some of the ones we've defined, like views.
Logger, config, something else we add in the future, policies… Whatever. We can use very general mechanisms.
To control whether or not something is turned on or not.
Right, so I think the trade-off there is, like.
Whether we use general, but, like, obviously less tailored mechanisms for configuration.
Or whether we have these specific ones that are actually on the instrumentation libraries themselves.
**Liudmila Molkova** 38:44 I think it's Bose, right? So, let me give you another example. So… This is a metric, that has a number of contributors, unique contributors in the repository. If I remember correctly, it's extremely expensive to obtain.
And then this configuration option would… instrumentation would need to know about, for sure.
**David Ashpole (Google LLC)** 39:08 Why is that?
**Liudmila Molkova** 39:10 Because it doesn't want to collect information.
**David Ashpole (Google LLC)** 39:13 We already have… we have is enabled on instruments, so we don't pay that cost anyways, right?
Or we shouldn't, right?
**Liudmila Molkova** 39:23 Something on the instrument.
need to know whether it's enabled or not, right?
**David Ashpole (Google LLC)** 39:30 Yeah, that's part of the API, though.
**Liudmila Molkova** 39:34 Is it part of the configuration?
**David Ashpole (Google LLC)** 39:39 So, each instrument has a function on it called isEnabled.
And so the SDK will return true or false, letting you know if you need to do the work to construct the attribute set and other things on it, right?
**Liudmila Molkova** 39:54 Yeah, so we need to… some way to describe how the configuration property is called.
What I'm saying is that, Okay, so, okay, got your point here.
Another point.
the semconfine.
You would change the whole instrumentation behavior.
across signals.
So this, France.
they are not supposed to be emitted. And you can say that, okay, instrumentation doesn't need to care, but, like, if it always emits two sets.
Of metrics, it's… it drops half of them on the floor. No, it's not a good idea.
**David Ashpole (Google LLC)** 40:44 Is the services for, like, migrations?
**Liudmila Molkova** 40:46 Yeah.
**David Ashpole (Google LLC)** 40:47 Yeah, I… I agree that we don't currently, like, If we think about the… we think about, like, the North Star future, where, like, we want to go. I think we would love to have the instrumentation just write one version of semantic conventions in the actual API, right, whatever the latest one is. And for the SDK, To use some other mechanism.
to do semantic convention, opt-in, opt-out, right? Like, that would be the ideal, but yeah, I agree that, like, that's not where we are today. And today, everyone has toggles.
To go between different versions in the instrument.
sold.
**Liudmila Molkova** 41:27 And it's a little bit inevitable. But, let me give you the final example, like.
This is the… the current story that we have some… logs.
And, like, for the context to others, the story started with, should we have requirement levels for logs? And if the enablement mechanism is true, we already have event name in the enabled, and we have the logger name and everything, and log levels, we have a lot of enablement mechanisms.
But I think… This is all true.
And we also have opt-in logs that are another version of some kind of opt-in, whether you emit span events or ZoomMate log-based events. And this is, again, kind of something that instrumentation needs to know about.
So some of these properties can be supported by SDK. A lot of them make sense in the instrumentation itself.
And having both of these things and semantic conventions looks wrong to me. We should have one or another.
instrument… it's orthogonal to whether metrics should have advisory API, I think?
But, my North Star is that having this allows us to generate instrumentation code.
Taking all of this into account.
And not even enabling, like, not even attempting to do things that are disabled by the instrumentation, but by the configuration.
**David Ashpole (Google LLC)** 43:09 I mean, I… like, I think… I'll give you, like, my… Sorry, I'm trying to… okay, this is a different thread.
From my point of view, I think it's better to have… configuration on the SDK than it is to have it On instrumentation libraries.
I gen… like, when we're asking for configuration on instrumentation libraries, I generally view that as, like.
a signal that we might be missing something in our API.
So, like, a good example of something we're missing is, like, a notion of experimental or stable, maybe, on instrumentation, right? It's like, if we passed that, then we could pretty easily have the SDK provide proper defaults and provide a nice, unified config.
Way of turning on experimental things, right?
Some of these… log-based exceptions enabled. Some of these are definitely things that will need to be configured, so I totally get that, like, switching between logs and exceptions has to be… like, it wouldn't make sense to pass that to any of the individual signal APIs, right?
But… I guess, like, for the most part, I think we need to… there's two things I want to get across. One is, I think that per signal.
when we're talking about just the APIs, right, so, like, the logging API, the trace API, the… Metrics API. We should try and consolidate on one way of expressing Like, how important a piece of telemetry is. So, for logs.
I think that that typically is, like, the log level, right? So if it's something that you want on by default, you make it info, and if it's something you want off by default, you typically would make it, like, debug or something.
Like, and we should probably reuse that mechanism.
when we're talking about the API. Like, I wouldn't want A logging advisory parameter.
That's opt-in versus required, right?
**Liudmila Molkova** 45:26 I'm not suggesting this, to be fair. I'm questioning what… The usefulness of requirement level as a concept.
**David Ashpole (Google LLC)** 45:37 Why… I mean, I think we need some way… configure, like… I think we need to… be able to… I think we should… let's see, I think the semantic conventions, Should line up with what our API provides, right? So… Right now, our API for logs is… Here's your event name, attributes, And your log level.
Right, so I would… like, when we're talking about logs, I would probably have the thing that's in the semantic conventions for logs be Here's the log level for this thing.
Instead of, here's opt-in, opt-out, because that's the API that we have today.
Yeah.
**Liudmila Molkova** 46:22 So…
**David Ashpole (Google LLC)** 46:23 semantic conventions should generate, like, the thing that goes to our… to our APIs.
**Liudmila Molkova** 46:27 It's a little bit tricky, because the log lover for this thing depends on the context, intentionally. So if it's an important exception, then it would be a warning. If it's something unimportant, it would be something else.
The interesting thing you mentioned, that per… Instrument, or per event, or per span type.
Enablement. Probably is the SDK concern.
The features are determination.
**David Ashpole (Google LLC)** 47:01 I think the configuration is… I think the default… needs to be expressed through the API, right?
So if some of it's default on and some of it's default off, like, if there's… A mixture of relative importance here.
We need to, like… What's that?
**Liudmila Molkova** 47:19 Why, though? So, the SDK… gets the default version of config from somewhere, and it knows. Instrumentation doesn't even need to know what is the default.
**David Ashpole (Google LLC)** 47:32 instrumentation.
what… what I want to avoid.
So the… the only tricky part with configuration on the instrumentation library and configuration on the SDK, right? So, for example, logger configurator, is that now, as a user, I need to go find two spots.
And make sure they're both updated in order to opt something in.
Right? So… It's like… You know, obviously, there is going to be some cases where that's necessary, like the one you've highlighted here, where we're switching between log events and exceptions.
As a general rule, I think we should, like… hotels built around the idea that the API It's just for passing information about the telemetry being recorded.
And then the SDK is where the user gets to decide what to do with… with that telemo, like, so…
**Liudmila Molkova** 48:32 Right.
**David Ashpole (Google LLC)** 48:33 We should express it in terms of, like, something about the telemetry in semantic conventions, right?
**Liudmila Molkova** 48:39 Yeah, the… what you're saying is the API we have is not the API that we should have.
the, like, Jack showed Instrumentation API.
And this is… more convenient.
layer that emits… Signals together.
According to semantic conventions.
And this API… on this API level, we wouldn't care, but what I'm saying, with the semantic conventions, we're trying to build this API tailored to the domain.
So maybe the distinction, I'm trying to say the distinction that we can draw. So, if it configures a specific Signal definition, single span, single, log, single, metric.
It is the SDK concern, because this is what SDK knows about. It doesn't know about relationship between features.
Or different signals.
When it comes to more than one type of item.
And it's kind of where we have to apply configuration at the instrumentation layer, because otherwise it's a lot of coordination, and it's on the user to do.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 49:58 Yeah, David, that's actually your same argument. You know, you were talking about trying to… instrumentation config is worse, because then you have to configure things in two places, the instrumentation config and the SDK config. Liudmil is making that argument in a different form, which is like, if you want consistency across spans and metrics.
like, for example, what your HTTP clients, you know, spans and metrics, you know, use for headers captured or something like that, then, you know, you have to coordinate across the signals.
**David Ashpole (Google LLC)** 50:25 And I… you know, I totally… I can't tell if we're disagreeing about the general principle, or just disagreeing about the specifics.
So, like, I totally concede that there are cases, for example, switching between log, logs versus, span events, right? Like… That's not something that's easy to coordinate across… it would span multiple SDK implementations, right? A trace and a log SDK.
Yeah.
**Liudmila Molkova** 50:57 From practical sense, I think we're trying to resolve two questions. The one is, should we remove this guy from semantic conventions?
Syntax, at least. The schema.
And I think my answer is yes, especially since we're going to define pretty much the same.
Instrumentation can set advisory parameters coded on metrics based on this. It's… it's the same information.
**David Ashpole (Google LLC)** 51:25 What advisory param? Sorry.
**Liudmila Molkova** 51:28 So, if we introduce metric advisory perms.
**David Ashpole (Google LLC)** 51:31 Is this a metric?
**Liudmila Molkova** 51:33 Oh, sorry, okay, let's go.
**David Ashpole (Google LLC)** 51:34 Yeah, so for metrics, I'm totally on board.
I think… maybe we can agree on a few things in the last few minutes. I think, I think… requirement level, Doesn't make sense to me on logs.
Or, honestly, on spans, although that's maybe a separate conversation.
I think it only makes sense on metrics.
If we also choose to add an advisory parameter that it maps to.
Right, because my… to my earlier point, like.
what's in here, I guess, except for what's in the configuration block, needs to map to whatever the API You know, allows for, right?
So defining things in semantic conventions that the API doesn't support isn't, like, super useful.
**Liudmila Molkova** 52:28 What I would propose is to remove requirement level from all signals.
Assuming it will be replaced with this.
To be fair, it doesn't even exist, it only exists in Markdown today, and it will stay there.
But long term, I think the configuration block should be the one saying what is the default for this.
**David Ashpole (Google LLC)** 52:55 As a general rule, I strongly disagree. As a specific rule, when we're doing cross-signal stuff.
I'm okay with it as an exception. But, like, we want… If we have this, and this is how all enablement and disablement generally works. Then, like.
You won't be able to use views to do things anymore, right?
**Liudmila Molkova** 53:15 Wait, wait.
**David Ashpole (Google LLC)** 53:16 be able to turn things on with the SDK, because it will already be filtered out at the instrumentation level.
**Liudmila Molkova** 53:23 wait, it can say, okay, it's the SDK config, or it's not, it's not, some other form that… it doesn't tell you what applies it.
So, instrumentation doesn't need to even… know the property. So you can say it's controlled by SDK, there is no property, the default is false.
**David Ashpole (Google LLC)** 53:46 I mean, I think that's fine, but then… we… the better thing would be to define the configuration options in the SDK that allow you to enable or disable arbitrary pieces of telemetry, right?
**Liudmila Molkova** 54:00 Absolutely, yeah.
**David Ashpole (Google LLC)** 54:01 Okay.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 54:06 So then… so then, Ludmila, how… how… if… if we end up defining new knobs in the SDK to enable or disable arbitrary pieces of telemetry, you know, we have… some… we have to do some work there, because they don't exist. But, like, then, like, what would… what would be the purpose of this, defining this in semantic conventions? Like, how… how do you… like, what… what interprets this… this YAML data and does something with it?
Like, because it doesn't… it doesn't, you know, end up being a part of the generated code from semantic conventions, because it's like SDK.
**Liudmila Molkova** 54:38 Oh, it… It would, like, it would be for advisory perms.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 54:44 Okay, for advisory programs, yeah, yeah, but the other stuff.
**Liudmila Molkova** 54:48 And then, if we're saying that metrics that are… that we control per metric, in… in semantic conventions.
Instrumentation… in the lack of advisory params. Instrumentation shouldn't cure at all.
Like, it should not even… attempt any configuration. It should not provide… instrumentation should not provide configuration option.
to enable.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 55:19 Yes, so the instrumentation ends up not caring about this part of the semantic conventions data model, right?
And, like, and then I just kind of worry, like, how would a user consume it? Like, maybe you could… maybe you could use this structured YAML to produce, like, configs to give to the user. Like, hey, if you want to enable this span, or this event, or this metric, you, like, you know, use this SDK declarative config YAML, and that could be, like, generated from From these config options. I'm just trying to just, like, figure out how this is actionable, if instrumentation is not going to act on it.
**Liudmila Molkova** 56:00 Yeah.
I think, David, I, I, I kinda… I'm thinking, From your perspective, because all my perspective is instrumentation should check the flag first.
**David Ashpole (Google LLC)** 56:14 My perspective is… The things that we're trying to do are probably a good indication that we're missing some hopefully small knobs in the API.
Right, so for metrics, we're missing opt-in. I think that's clear. I feel like for logs.
we already have a signal for the relative importance of something. It sounds like maybe it's not the right one in logging level for some of the GenAI stuff.
**Liudmila Molkova** 56:41 It's enough. We… we… it was a mistake that we called it opt-in, just because we didn't have enough infrastructure around it. No reason.
**David Ashpole (Google LLC)** 56:50 Okay. So, my… I guess… to sum it up, like, my preference would be if the things that we put in this YAML file Map either directly to parameters that are passed to the API.
or… To configuration that's going to be available on the instrumentation library itself.
**Liudmila Molkova** 57:17 Right.
And then, in the lack of API.
for metrics.
**David Ashpole (Google LLC)** 57:23 Right, well, yeah, I can… that's on me, I guess. I can pick that back up and try and drive it home if… metrics is one thing. I think… so the concrete proposal would be that we no longer include requirement level on… log, or onEvent.
Semantic conventions, and instead, If we want to, we can provide a log level.
**Liudmila Molkova** 57:46 I do not agree on the requirement level anywhere.
**David Ashpole (Google LLC)** 57:54 Because…
**Liudmila Molkova** 57:55 It doesn't make sense anywhere then.
It's not specific. Oh, and Jack, to your point, What would instrument… what would… would be the benefit of declaring something like this in semantic conventions. It would be the default config that we could generate.
Because something needs to know what should be in the default config. It should be somewhere. It doesn't have to be in semantic conventions, but it kind of makes sense because it's per instrument thing.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 58:28 Yeah.
**Carlos Alberto Cortez (Dash0)** 58:30 By the way, we are one minute away from the end, thank you, this was very interesting, it caught me off guard, and I agree with Joe Magdi saying that probably this needs…
**David Ashpole (Google LLC)** 58:41 I have a write-up that's mostly.
**Carlos Alberto Cortez (Dash0)** 58:42 Oh, nice.
**David Ashpole (Google LLC)** 58:43 So I… but I… yeah.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 58:45 I do think that it was good to bring this to this spec call, and we should continue to have these conversations here. The interaction between semantic conventions and instrumentation and the API and the SDK, it can't go live in… it can't be conversations happening in smaller groups. It needs to be a community-wide conversation, so let's keep having it here.
**Liudmila Molkova** 59:08 Thank you.
**Carlos Alberto Cortez (Dash0)** 59:09 Counting on… counting on you, David. Thank you so much. Yeah, see you around.
**Ivo Anjo** 59:15 Thank you.
