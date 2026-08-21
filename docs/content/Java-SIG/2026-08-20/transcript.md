SIG: Java SIG
Date: 2026-08-20
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Trask Stalnaker (Microsoft Corporation)** 02:05 I accidentally joined the Go meeting.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 02:09 Jorge. Thank you, Will.
**Trask Stalnaker (Microsoft Corporation)** 02:15 Too many meetings at this time slot in the calendar.
Lovely.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 02:21 It's a very busy calendar in OpenTelemetry these days.
**Jason Plumb** 02:29 It's a big project, Jack.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 02:32 It is a big project.
**Jason Plumb** 02:34 Okay.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 02:48 Something happened to… no, never mind. Somebody's just… Somebody's highlighting the…
**Jason Plumb** 02:54 I know, it's driving me crazy. Someone's talking.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 02:58 Anonymous Badger. Maybe not.
It's not even them.
Anonymous unicorn.
That's the culprit.
**Jason Plumb** 03:10 Anonymous, stop it.
**Trask Stalnaker (Microsoft Corporation)** 03:24 Alright, well, let's get started.
**Jason Plumb** 03:28 Yeah, I think my thing will be pretty fast, but… so we… we, Instrumentation, have this pretty cool smoke test fake backend, which is a little server that runs and receives OTLP, And holds onto stuff, and then exposes some endpoints that you can then, from a test, query the telemetry back to make assertions about it. And we use that all over the place, right? It's really cool. That thing only supports gRPC, And, client-side users, client-side platforms, like Android, don't like gRPC very well.
So I'm wondering if it would be a welcome addition if we added, HTTP to that thing, or if there's any problems with that.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 04:11 That seems great.
**Trask Stalnaker (Microsoft Corporation)** 04:11 you can…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 04:12 And HTTP is the preference these days for OTLP, so, yeah, if anything, it should be the primary, and gRPC should be opt-in.
**Jason Plumb** 04:20 Okay.
**Trask Stalnaker (Microsoft Corporation)** 04:21 If you want to change our smoke tests…
**Jason Plumb** 04:23 I don't want to switch it, I want to add it as an additional, and do both, But, yeah, changing the smoke test would be a bigger effort. Maybe that'll be a separate set of 100 PRs or whatever.
Cool, yeah, so we… in Android, we now have this, like, smoke test, which can run… it hasn't been merged, but I'll merge it this week, that actually runs on the device, and… That's pretty cool.
But we do have to… I think we're gonna end up spinning up a collector before this… change lands so that we can tran- that's only there to translate from gRPC to HTTP.
And… It would be nice not to have to run the collector at all for the smoke test, so… Cool.
**Trask Stalnaker (Microsoft Corporation)** 05:11 No problem.
**Jason Plumb** 05:12 Okay, cool. Just wanted to raise it in case there was any reason that it would be a problem, so it sounds like we're good. Thanks.
**Trask Stalnaker (Microsoft Corporation)** 05:22 Alright.
Jack.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 05:25 Hi. Yeah, there's this, There's this PR I've had open for a while, and it's addressing an issue somebody reported where they're trying to use our OTLP exporter, and, for some reason, and the OTLP receiver they're pointing it to, doesn't work with modern TLS. They have to use an older version of TLS.
And the problem is, is that when you initialize our OTLP exporters.
they use OKHTTP under the covers, and OKHTTP has its own settings and defaults about which versions of TLS it allows you to connect to. And so, it has this default, which says, like.
modern TLS, and there's a few TLS versions that are included in that, and there's no good way for a user like this that needs to connect to a non-modern TLS version to, to configure this, programmatically or, you know, via environment variables or declarative config. None of that.
And so, what this PR does is it adds a new configuration option, set-enabled protocols, to all of our OTLP exporter builders, and, it accepts just a list of strings, and the strings, are in the… are in the format that there's, like, a… there's a Java spec on how you specify TLS versions in a very standardized way. And so, rather than us creating a new and NUM or anything like that, we just accept a generic list of strings, and it's up to you to conform to the Java spec for specifying the TLS versions you want.
And, you know, by default, if you don't set any of these, we're going to use the, the defaults of the underlying senders. And this is interesting, because the JDK sender has different defaults than OKHTTP.
And the JDK sender, its TLS versions that it accepts, they're influenced by various Java-level system properties.
And OKHTTP is not. OKHTTP, because it's not built into the JVM. It ignores the Java-level system properties and, you know, kind of does its own thing.
And so, you know, I don't want to mess with those defaults. But I do want you to have the ability to set protocols if you want to narrow the set or expand them.
And so, if you call this, and only if you call this, we're going to do everything we can programmatically to configure the underlying senders to accept the set of protocols that you've configured here.
the other thing that's worth talking about is, you know.
the API surface areas. Should we have a new set enabled protocols method? And, you know, there's this other issue that's sort of related, where somebody wants to add support for, configuring encryption algorithms, so not the TLS version, but the actual encryption algorithms that are used. They want to be able to specify that they use, like, a post-quantum algorithm. And, you know, should those sort of be merged together? And if so, what would the shape of that look like?
And there is a type in the JDK that we could consider using. So instead of, like, having, you know, a list of strings for enabled protocols and a list of strings for encryption algorithms, we could use SSL parameters, which is sort of like a bundle of, like, a bunch of, like, SSL-related parameters And it's a superset of this protocols option that I'm adding here, and of the encryption algorithms, and, like, a bunch of other stuff.
And so, that was a decision that I had to make, is like, hey, should we… should we, you know, just support configuring your own SSL parameters, which is, like, a superset of a bunch of things, or just, the protocols? And I… I chose to go, to… go in the individual properties direction, and not, like, accept an SSL parameters, which is, like, a bundled superset of a bunch of things, because There's a lot of things in there that we don't… that we won't handle, and like, you know, I don't know how we would handle in the immediate future. So, accepting SSL parameters as a… as a configuration option sort of gives the implication that we're going to respect all of the properties that that bundles up.
And that's not actually the case. So, even though I think it adds more… even though it adds more surface area, I'm sort of inclined to just, you know, add options as needed, that, you know, even though they're comprised by SSL parameters.
**Trask Stalnaker (Microsoft Corporation)** 10:35 What does the, what does the SSL parameters bundle up besides… Protocols and cipher suites.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 10:45 If you can scroll down… I think, like, these other parameters, like these SNI matchers…
**Trask Stalnaker (Microsoft Corporation)** 10:53 Oh, they're setters.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 10:54 There's setters, yeah, those are just the mandatory arguments for constructor syntax sugar, but…
**Trask Stalnaker (Microsoft Corporation)** 10:59 Yeah, yeah, makes sense.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 11:02 Server names.
**Trask Stalnaker (Microsoft Corporation)** 11:04 Yeah…
**Jason Plumb** 11:05 I thought we… I thought we already had a way, or we exposed a way to get the parameters, the SSL parameters.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 11:11 We allow you to set SSL context And, X509 Trust Manager. That's, like, the low-level thing that we have, and somehow these are not bundled into that.
**Jason Plumb** 11:25 Interesting.
**John Watson** 11:29 If we were to accept SSL parameters, is there something we could just pass them wholesale to, to wire things up?
to stuff?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 11:39 I think in the case of JDK Sender, yes, but in the case of OKHTTP, no. In the case of OKHTTP, we have to, like, extract out the parameters we care about and, like, you know, map them to the equivalent.
Okay, HTTP options.
**Jason Plumb** 11:57 Yeah…
**Trask Stalnaker (Microsoft Corporation)** 12:00 That's not horrible, I mean, to give a warning in the OKHTTP, export that certain things aren't supported.
**John Watson** 12:17 Yeah, putting a… putting… I like… I like the idea of using the JDK class, only because it already… I assume that they have done a lot of hard thinking about like, what all would need to go into configuring a general TLS setup?
And if we can just pass that off to the JDK sender.
That feels like a pretty big win.
Except that JDK Center doesn't support gRPC, right? Yep. Because we don't get,
**Trask Stalnaker (Microsoft Corporation)** 12:53 Java 8.
**John Watson** 12:55 Or Javais, yes.
It's gonna be messy.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 13:08 That's orthogonal, like, JDK, we already acknowledged that it's not perfect, which is why the default is OK HTTP, and why that's used in the Java agent.
**John Watson** 13:18 No, I was just thinking through all of the different ways in which we would need to scare, like, put logging, or warnings, or extra Javadoc, or… things in all the different cases. It's like, JDK Center doesn't support this. Okay, HTTP only supports this subset of things. I mean, it's just gonna be… it's gonna be… that's all… that's what I meant by messy. It's just like.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 13:40 I see.
**John Watson** 13:41 There's a lot of… Like, everything has its own unique configuration, essentially.
**Trask Stalnaker (Microsoft Corporation)** 13:47 Yeah, we basically have to say it's best effort, and best effort kind of sucks when it comes to security stuff.
**John Watson** 13:53 Yeah.
**Jason Plumb** 13:55 With the JDK sender, isn't… doesn't a user have the ability to customize the JDK already to use an older protocol?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 14:05 It's been, over a month since I was really heads down in this. I think the JDK has more options than OKHTTP, because there are.
**Jason Plumb** 14:14 Yes.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 14:15 System properties that came.
**Jason Plumb** 14:16 Right.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 14:16 influence it.
**Jason Plumb** 14:17 Yeah.
So your PR is addressing only the OKHCP case?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 14:24 No, no, no, no, no. I still programmatically, like, want to impact all the senders. Like, there's an escape patch available right now for JDK.
there's no escape hatch for OKHTTP, so, like, you know, I want to solve OKHTTP, but, like, if we have, you know, a public API on our OTLP builders, it needs to impact all of our senders that we support.
**Jason Plumb** 14:47 Got it.
Is, is, like, is supporting the old versions of TLS, like the deprecated, insecure ones, is that the only use case for protocols?
Do we…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 15:00 That's the only use case I know of, like, maybe you could also kind of, like, so, maybe you could narrow the set of TLS protocols that you want to use, if you're, like, if you're really… To, like, force it.
**Jason Plumb** 15:12 1-3 or something, yeah, okay.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 15:13 Exactly, yeah.
**Jason Plumb** 15:15 Okay, that's a good use case.
You kind of hate to allow this codependency on whoever needs TLSv1, but… Yeah.
Okay.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 15:31 But, I… the other issue about, like, post-quantum encryption, it sort of intertwines with this, and so I wanted to do these sequentially, because, you know, whatever shape we choose for this.
in terms of the API, sort of dictates the shape for that as well. Like, do we accept SSL parameters as an argument, or do we, you know, cherry-pick the individual things that we want to make configurable?
**Jason Plumb** 15:56 Makes sense.
**John Watson** 16:08 It sounds like we're essentially Going to be choosing between a set of non-optimals.
whatever we get is not optimal. Like, there is no perfect… there is no perfect solution to this, given what we have to work with, unfortunately. So I won't… I won't block this if you think this is a very… the good way to go, Jack, that seems fine.
**Jason Plumb** 16:29 was…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 16:29 I like the explicit options, where we're explicit about what we support, and we… this is sort of like a syntactic sugar thing as well, like, it's easier to use this, I would say, than SSL parameters. I don't think the SSL parameters API is very good.
**John Watson** 16:51 How does this, how does this fold in with, declarative config?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 16:55 It doesn't yet, but it would, like, if in the future there was a property in the, you know, the common JSON schema to say, hey, OTLP exporters should allow their TLS protocol versions to be specified, then, you know, that property would manifest as a call to this setter, but no such property exists.
So this is only accessible programmatically.
**John Watson** 17:19 And there isn't anything in the spec about this at the moment, on the config side.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 17:24 Nope.
**John Watson** 17:25 Okay.
Cool. As I said, it seems… not optimal, but I don't think there's an optimal solution, so it seems fine to me.
**Jason Plumb** 17:39 There was nothing blocking from the other reviewers, right?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 17:42 Nope.
**Jason Plumb** 17:43 Just discussion, okay.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 17:45 I think the reviewer was actually the person that… one of the people that was suffering from this issue, and so, I think they were content with this.
**John Watson** 17:56 Cool.
I'll give it a thumbs up.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 18:03 Thank you.
**Trask Stalnaker (Microsoft Corporation)** 18:09 Alright, let's move on. Sylvain, glad you're here. I wanted to raise just… for everyone here, a couple of JVM… oh, that's not yours, I think this one is yours.
JVM Semantic Convention PRs.
This one… Seems pretty… Straightforward, just… Promoting it.
Sylvain, I wasn't sure, I meant to look up, the process file descriptor ones. Are those… Already… RC… Let's see…
**Sylvain Juge (Elastic)** 19:07 Actually, I completely forgot about the process ones.
And I just wanted to promote some things that I worked on previously, so…
**Trask Stalnaker (Microsoft Corporation)** 19:18 Yeah, it may be worth checking in. I know they have been… promoting… some of these… yeah, yeah, so this one, it says development up here, which I guess is accurate, but… Oh, look at that! It is RC.
Now, why don't they have limit?
It may be worth checking… Why they don't have limit over there.
And we do.
Think it makes sense still?
And we have a nice mapping in Java, but that would be sort of my only open question.
**Sylvain Juge (Elastic)** 20:12 And so, in this case, do you think, like, linking to, process, semantic convention would help?
**Trask Stalnaker (Microsoft Corporation)** 20:21 Yeah, yeah, I do. I would say that the… because it kind of locks down the naming, right? We're following their naming.
**Sylvain Juge (Elastic)** 20:32 And maybe there was just a question about the limits, so I remember we discussed a while ago, like, should we, like, omit values when we have, like, minus one or, like, maximum integral value?
And do you think this part should be part of the spec to say, there are, like, extreme corner case you need to deal with?
**Trask Stalnaker (Microsoft Corporation)** 20:57 I don't know, I would assume that, you would not… capture it, like, I don't think you would… Like, minus 1 or max value aren't actual counts or limits, so I… think you just wouldn't capture it? That would be my assumption.
**Sylvain Juge (Elastic)** 21:18 Okay, so in this case, it would be better, like, to write it explicitly in semantic conventions to just omit those values.
**Trask Stalnaker (Microsoft Corporation)** 21:26 Yeah, actually, it's probably good here because since we are mapping it, we're kind of saying where it would be captured from.
And that underlying… call does provide some, like, minus one. If it does, then it… so it makes… I think it makes sense to add it to the semantic conventions.
**Sylvain Juge (Elastic)** 21:52 Okay.
**Trask Stalnaker (Microsoft Corporation)** 21:58 This was the other, I haven't… really looked… There's a PR, sim… similarly, to add these to… Oops.
Where is the prototype? Yes, prototype.
So if anybody is interested in these metrics, would be great if you could.
Take a look.
Provide some comments.
Not sure if there's any overlap with the JMX stuff.
I think these ones are coming from… Actually, don't know. They're coming from our… Executor Instrumentation… Yeah, anyway, anybody who's interested would be great to get some… feedback on… that.
Both the, the prototype and the, semantic convention.
Cool, that was all, alright, moving on, Surya, welcome!
**Surya Teja** 23:58 Hey, hi, Trask, how is it going?
**Trask Stalnaker (Microsoft Corporation)** 24:00 Hey, good. Good to see you here.
**Surya Teja** 24:03 Yeah, so the PR that I left is, for adding the, semantic conventions for GenAI, attributes. Minghui actually worked on the original implementation, but he left Midway because, he is working on a few other stuff.
So this PR reintroduces what Ming Hui, worked on, and also, I was planning on introducing the open inference-donated, code and port it to emit GenAI semantic conventions for, OpenAI. We already have OpenAI, along with that Anthropic.
and OpenAI Agent Scotland SDK, and also Spring AI SDK. It's not going to be done in… I'm going to do it in step… in a phased format, rather than one thing, rather than everything at once. But this is the foundation for introducing all those instrumentation into a Java instrumentation ecosystem.
**Trask Stalnaker (Microsoft Corporation)** 25:07 And so, we have some existing GenAI instrumentation in this repo.
Did we not… do we not have, like, the attributes getters?
Or is this, like, a new attributes getter alongside the existing ones?
**Surya Teja** 25:26 We already have some attribute getters for those instrumentations. What I'm doing is I'm trying to bring this with parity with the newly released Semantic conventions 1.42 or 43, because few attributes like retrieval and, agents are missing.
So… I'm bringing those in, and once these are merged, I just want to keep up with what we're releasing in our Gen AI ecosystem over here also, and see how we can Upgrade our, instrumentations to emit those two.
**Trask Stalnaker (Microsoft Corporation)** 26:06 Oh, I see, okay, so we have… A general one, attributes getter, and then… new operation… Attributes, getters…
**Surya Teja** 26:20 Yeah.
we, to summarize, we have inference-related, getters. What I'm doing is I'm adding the agent, as well as retrieval. I believe tools also is existing previously. I just enriched them with new attributes that are being emitted in the new semantic convention library from GenAI.
**Trask Stalnaker (Microsoft Corporation)** 26:44 Okay, and these are different spans, different, potentially, request and response…
**Surya Teja** 26:51 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 26:51 Pipes, which is why they can't… Go into the general attributes getter.
**Surya Teja** 26:57 Yeah. Yeah.
**Trask Stalnaker (Microsoft Corporation)** 27:06 Okay, and this is all just… oh, okay, so this is all just the… infrastructure, the… instrument or API.
**Surya Teja** 27:17 Yeah, yeah. The semantic conventions package is still not stable, right, for semantic conventions, so until it becomes stable, or we release a stable version, I'm just enriching them, and we already have the existing getters and stuff. I'm just adding the new span attributes that are missing in the existing ones.
**Trask Stalnaker (Microsoft Corporation)** 27:44 Cool. I think I left some… just a first round of AI-generated feedback.
It might be interesting to see these in action, like, if you… could… if you want to go ahead and send, another PR that's sort of stacked, On this, or…
**Surya Teja** 28:14 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 28:15 on this.
So that… we can see, sort of, how the new… like, I assume… are we not capturing any tool spans or retrieval spans at this point?
**Surya Teja** 28:31 Not as far as I know. I might be wrong, but when I checked.
I did a semantic search in the repository, and I saw that we are not capturing the tool spans and retrieval spans.
**Trask Stalnaker (Microsoft Corporation)** 28:47 Cool. So, yeah, it might be helpful, to be able to see how these,
**Surya Teja** 28:56 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 28:57 How this is used in, real…
**Surya Teja** 29:01 Shut up.
**Trask Stalnaker (Microsoft Corporation)** 29:01 implementation.
**Surya Teja** 29:03 Sure, I actually added these to OpenAI, the existing OpenAI one.
But the problem is, we still don't… I still… I… I wanted to cut down the bloat on the PR, because I wanted people to look Do it thoroughly, and… give their opinions, but I… I'm.
**Trask Stalnaker (Microsoft Corporation)** 29:22 Yeah.
**Surya Teja** 29:22 Raisin. Raise in another PR, which is going to show how it is going to gel with those in… instrument.
**Trask Stalnaker (Microsoft Corporation)** 29:28 Yeah, and you can just leave that other PR as draft and just reference it from this PR as, like, something that reviewers can go to see, sort of, the bigger picture.
**Surya Teja** 29:39 Sure, Trask. I'm going to do that, yeah.
Cool. Thanks.
**Trask Stalnaker (Microsoft Corporation)** 29:53 Cool. Oh, I guess I… I owe an update on, I have started… The release, the changelog, I, where did you go?
Yes, this has both… I have also the changelog in here. I will get this up.
in a bit today, and hopefully get the, probably get this up, early afternoon, and, I'll ping folks for… Approvals, and hopefully get the release out today.
We will need one more… 2X release.
After this.
Before 3-0.
But it's going… it's going well. We're getting a lot of stuff in,
**Jason Plumb** 30:57 If Lori and Jay are not around to help with that Trask, just DM me.
Just for approvals, yeah.
**Trask Stalnaker (Microsoft Corporation)** 31:03 Yeah, yeah. Awesome.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 31:06 Hey, Trask, there's a PR that's in the core repo, called Remediate Zizmor Findings, and I think we've been waiting for, a release to happen, before we merge that, because the… just… I don't know, if other repos have already merged it.
Yeah. We can benefit from them taking the plunge first.
**Trask Stalnaker (Microsoft Corporation)** 31:25 Yeah.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 31:26 Is, is this the first release that,
**Trask Stalnaker (Microsoft Corporation)** 31:29 Yeah.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 31:29 Okay.
Alright, so this would unblock them.
**Trask Stalnaker (Microsoft Corporation)** 31:32 Yeah.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 31:34 Well, good luck.
**Trask Stalnaker (Microsoft Corporation)** 31:37 Right, Joe.
Alright, anything… Alice.
Yeah, Abdel. Hey.
Welcome.
**Abdel Elyagoubi (Sofrecom)** 32:01 Hey, everyone. Do you hear me?
**Trask Stalnaker (Microsoft Corporation)** 32:04 Yeah.
**Abdel Elyagoubi (Sofrecom)** 32:05 So, actually, I have a question which is not related to code. I don't know if this is the right time for it, but I'll just go for it.
So, I want to just ask you, what do you think about AI-assisted contributors? As I see, like, many, like, it's fluted into, like, PRs, many AI-generated PRs, which make it very confusing, like, for you as maintainers to review each one, which will take… probably a half of your day to review it, and at the end, you will just find it, like, it's AI-generated. So we've seen already the curl, which, stopped at, like.
programs of, like, contributors that uses AI. So, don't you think, like, using some AI policy to, like, stop those agents and stuff like this?
**Trask Stalnaker (Microsoft Corporation)** 32:57 Yeah, so it's definitely… it's a hot topic, for sure. I linked here a, Slack discussion In the Hotel Maintainers channel, just from this week.
And with… A bunch of info and links, that you might find interesting.
I think one of the interesting things is it seems to vary a lot across OpenTelemetry.
Repos?
Some repos are getting hit hard, and it's… Been painful.
And some repos, not so much.
Happy to share, sort of, my… brief, In the Java instrumentation repo, at least.
I haven't seen… It… More I see it in the, security, the CVEs that we get reported. We get a bunch of junk, CVEs reported.
But my… my personal take is I fight AI with AI, and… I just give a… AI, my AI says, hey, this is not a CVE, I look at it, it looks reasonable, I post it, and… I don't spend more than 5 minutes on it, and if the person comes back with something compelling, then that's great, but usually they don't reply at all after that, because they were just farming CVEs, and they… The first pushback they get, they don't reply.
Jack.
**Abdel Elyagoubi (Sofrecom)** 34:55 Actually, that's a good approach.
**Trask Stalnaker (Microsoft Corporation)** 34:58 a teenager.
**Abdel Elyagoubi (Sofrecom)** 34:59 AI with AI.
**Jason Plumb** 35:01 There's also… I'll just say that there's also a limit that was put in place recently, because these technologies make it really easy to spin up a large number of PRs, and so the number of concurrent PRs is now limited for a single given contributor as well.
**Trask Stalnaker (Microsoft Corporation)** 35:20 I don't think we've enabled that on our… Repo, moderation, interaction limits… yeah, we haven't.
**Jason Plumb** 35:29 Beautiful.
**Trask Stalnaker (Microsoft Corporation)** 35:30 on this repo.
**Jason Plumb** 35:31 Okay.
**Trask Stalnaker (Microsoft Corporation)** 35:31 It hasn't been a pro- we haven't had it be a problem in this repo.
**Jason Plumb** 35:35 Okay.
**Trask Stalnaker (Microsoft Corporation)** 35:36 Yeah, I'm sure.
It will, at some point.
The other thing that I've… been doing, but I mean, this is… you know, we get… Most of the contributors here are, fairly consistent folks. I've been doing a lot of just… first of all, we enforce the co-pilot reviews.
And it basically, the PR dashboard, I have a setting in there that's only enabled on this repo at this point, but other people are welcome, other repos are welcome to it, which basically forces A clean co-pilot review before it will forward it on to reviewers.
So if you've seen, we have this PR dashboard.
And it categorizes things as waiting on reviewers, so… Basically, it won't come into this bucket, until it gets a clean co-pilot review, so a user will reply to all the stuff, it'll, before it runs, goes into reviewers, it'll run another co-pilot review.
And iterate, basically, until it's clean.
That has helped.
as well as, once we even get a clean review, the first thing I do is I have a little PR reviewer agent locally that I run, and it usually finds a couple, maybe minor things, maybe major things still.
Before I actually spend any time human reviewing it, and apologies to, contributors, for this, but I think most… most of the comments have been fairly, I'd say it's, like.
I feel like it's better than 80%.
**Gregor Zeitlinger** 37:35 I think they are really good, can you explain what's different from Copilot reviews?
**Trask Stalnaker (Microsoft Corporation)** 37:43 Yeah, I can even, I think I made this public even, so I think I can just show it. Yeah, so… It is this guy here.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 38:03 We talked a while back that co-pilot reviews only have access to The files in the diff.
**Trask Stalnaker (Microsoft Corporation)** 38:11 Not anymore.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 38:12 That changed?
**Trask Stalnaker (Microsoft Corporation)** 38:13 Yeah, they actually do an Agentic review now, so you can see they'll actually go, and sometimes I've seen it flag, they'll be like, hey, in this other repo, XYZ,
**Jack Berg (Raintank, Inc. – Grafana Labs)** 38:27 You can even reference other repos, huh?
**Trask Stalnaker (Microsoft Corporation)** 38:29 Yeah, so it's a full Agentic loop review now, where it has tools, and it can go search, like, so it'll search the semantic conventions repo for stuff. It's been a lot better lately. I've been getting a lot of good results.
**Surya Teja** 38:48 Trask, can we use this with, Claude? And, Cloud Code and other stuff, or is it just solely for Copilot?
**Trask Stalnaker (Microsoft Corporation)** 38:58 I was meaning to… I saw that on the GitHub blog, I saw that there's a standard now… For plugins that work across… Plug in… Agent Plugins 1.0, yes.
So, I think this is a new standard that allows you to Cloth?
Huh. I thought this was, across all compatible agent clients.
I don't know, I was meaning to check this out to see, it probably shouldn't be too hard to adapt it, but I do want to actually see, because that would be very nice to be able to have a standard there.
**Surya Teja** 39:57 Yeah, let me play with it, and I will ping you for some… No, but thanks a lot.
**Trask Stalnaker (Microsoft Corporation)** 40:02 Sure, yeah.
**Gregor Zeitlinger** 40:05 And by lightly filtered, does it mean that you look at it personally, or is it an automatic filter?
**Trask Stalnaker (Microsoft Corporation)** 40:12 No, I look at it for… so I have it, open a pending review for me.
And then I go into GitHub, and I read I read them.
And I'm like, you know, I spend, like, 30 seconds per comment. I'm just like, okay, yeah, that passes the smell test, like, it seems reasonable. I haven't actually gone and personally verified it, though.
**Gregor Zeitlinger** 40:36 Yeah, I think that's… that's a good trade-off.
**Trask Stalnaker (Microsoft Corporation)** 40:43 Yeah, I feel like it's been helping me to move… PRs through, faster, and by the time it's gotten through all those reviews, then I feel like I can just focus on, sort of, the… the bigger picture pieces of it.
And I do scan… I do, you know, go through, the PR descriptions are really important.
I found, and I've been doing some work on I actually have a PR description agent here to help me with mine, but I might… consider doing that for other PRs.
Just because a good, tight, and… accurate PR description allows the agents to validate that it does what the PR description says it does.
And then I can read the PR description to understand what it does.
And then I can, you know, scan the code later, but, like, the agents are pretty good at flagging things that don't match up there.
So, yeah, long… I guess that's a longer answer than I… Intended, but yeah, it's a big topic, and and again, though it's very varied… Like, in the… I think we get a lot better results in the instrumentation repo, because we have a lot of duplication.
Right, we have… like, 20 database instrumentations, you know, 30 HTTP instrumentations that are all so similar, and all the… these common bytecode patterns. There's so much common patterns.
in that repo, that AI, I think, is really good at that, where it's probably… Not, you know, with, like, Say in the core repo, things are, like, you've got the metric You know, more… more complexity there, less commonality.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 43:07 Been developing some local tooling, though, to help me get out of the notification bankruptcy.
From GitHub, and just essentially build GitHub notifications locally with all the filters and views that I want, and tools that I want, and then, the same types of things you're describing, like, be able to check out PRs that are of sufficient complexity, and with a single button, have an AI go review it, and, you know, sort of seed the review for me, where I can take a pass on it afterwards, and then ultimately submit it through the GitHub API.
I think that's, like, I think you've got it, it nailed, Trask is, like, we gotta fight AI with AI, and maybe not fight, but just, like, you know, adapt,
**Trask Stalnaker (Microsoft Corporation)** 43:55 Yeah, yeah.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 43:58 Because I think, like, a lot of the contributions and the increased volume, like, some of them are people's farming reputation, but, A lot of them… a lot of them are good, so…
**Trask Stalnaker (Microsoft Corporation)** 44:10 Yeah, yeah, I mean, we've… we get… we've gotten a… quite a good volume of PRs in the instrumentation repo, and clearly, you know, I mean, people are using AI to submit them, but they're, you know, they're good features and good things that we do want to land.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 44:28 Yeah.
I think the problem is, like, attention.
There's just… there's just so much… so many things to watch, and, you know, you know, the GitHub notifications has, like, it pushes you a notification when anything is updated, and updated these days is just, like.
it's… most of them are completely useless machine updates, like a label was added or removed, or, like, a bot left a comment, or… emerge from main, or something like that, which is… which is not the type of update you're interested in. So, being able to, like, you know, filter minimally for, like, define your own update criteria and your own watch criteria for what you're interested in.
I find very helpful.
**Jason Plumb** 45:12 Right, true.
**Trask Stalnaker (Microsoft Corporation)** 45:14 Yeah, go ahead.
**Jason Plumb** 45:15 Your number is 70! You've got your notifications managed.
**Trask Stalnaker (Microsoft Corporation)** 45:20 Oh… Yeah, yeah, but I… now that I know that, like, the… the Java instrumentation PRs.
I go through the dashboard, I just come through, and I pretty much just kind of…
**Jason Plumb** 45:37 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 45:38 Click, click, click to clear them.
what I don't… what I… I don't understand, there's no way to filter… why do I get notifications for draft PRs?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 45:54 Why can't you define your own arbitrary notification filter logic to say, like, okay, I've got this.
**Jason Plumb** 46:00 Everyone wants this.
Yes.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 46:02 And I care about this criteria, not, like, you know, every single criteria.
**Trask Stalnaker (Microsoft Corporation)** 46:08 I don't want to see draft PR And the reason I mention that is because I feel particularly bad because my draft PRs, I do, like, I loop with Copilot Reviewer a lot, so, like, I know that I am triggering so many stupid notifications for everybody on my draft PRs, but they're draft!
They shouldn't be notifying people. They're mine.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 46:37 Right, right.
Yeah, well, if it's any solace, you can kind of recreate this type of experience, but exactly the way you want, with just a couple of days locally, so…
**Trask Stalnaker (Microsoft Corporation)** 46:53 Yeah, we're all… we're all gonna be there.
**Jason Plumb** 46:59 And what's your number at, Jack?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 47:01 I don't… I don't know, I don't use this anymore.
**Jason Plumb** 47:03 I took.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 47:04 thousands.
**Trask Stalnaker (Microsoft Corporation)** 47:07 Yeah, yeah, I need to invest, yeah, a day or so in that also.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 47:15 You seem to have a pretty good process, Trask, so I've been trying to, you know, emulate some of the stuff you do, so… You've managed the volume, in my opinion, very well, so…
**Trask Stalnaker (Microsoft Corporation)** 47:34 Cool, thanks. Yeah, yeah, I want to try to share more with Folks… Yeah.
We should discuss more.
Because I know it's a big topic across… Opentelemetry.
I'm just not sure where everybody's at. I know people are in different places with AI and AI acceptance, also.
Mix some of the… Discussion's tricky.
The big community. Big tent.
Cool. Well, let's see if anything snuck on our agenda. Nope.
Alright, last call for topics.
Done. Till next time.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 48:33 Alright, take care, everyone.
**Jason Plumb** 48:35 Bye! Bye.
**Abdel Elyagoubi (Sofrecom)** 48:36 dice.
Bye.
