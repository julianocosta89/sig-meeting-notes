SIG: Java SIG
Date: 2026-10-15
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Gregor Zeitlinger** 00:55 Hello.
**John Watson** 01:07 Hello, hello.
**Trask Stalnaker (Microsoft Corporation)** 02:01 Is this on now?
Can you hear me?
**Gregor Zeitlinger** 02:07 Hi, Ken.
**Trask Stalnaker (Microsoft Corporation)** 02:09 Fantastic.
We'll start in one minute.
All right.
Well, let's kick off with a, Short… I can give a short update on the… 3.0.
I think things are… On track-ish for next Wednesday.
We've been deleting… Lots of code that was… Hidden behind… We'd added a lot… we'd added a lot of code. This whole maintaining backwards compatibility, during minor releases means us introducing this V3 preview flag and hiding lots of stuff, and then deleting lots of stuff later.
But Thank God for AI for that kind of stuff.
I think we've deleted… Tens of thousands of… lines of codes.
Which means we had to write tens of thousands of extra lines of code originally to hide these things behind flags.
We did just set up a, for the 2X, Maintenance releases… We have set up a… so last time with the 1X maintenance releases, if you recall, we… Stopped at, like, the… a minor version, and we just released patch releases, always, on that.
And that caused a couple of problems for people, because We updated… we would pull in, like, the latest SDK, minor releases in there, and… That introduced, like, pulled in some… changes… I don't remember, I had gone back and Double research this after, Lori reminded me.
But anyway, so what we are… doing what we're going to do for the 2X maintenance… is… We actually have a… Maintenance, 2X maintenance.
branch now.
And so this is sort of, like, main for 2X now, and we will merge into that, and we will do, monthly minor releases.
Out of that branch, doing… with our normal workflow of creating a release branch out of that maintenance branch.
So the release workflow.
is pretty much the same, just had to modify it to not only work off of Maine, but also off of these maintenance branches.
And we set up Renovate To update the maintenance branch.
So, basically, we'll continue doing all the… Just… it'll just be version bumps.
Primarily, dependency version bumps there, and, monthly minor releases out of there, unless we find, like, a regression or… a security CVE that we need to backport.
Any questions about… 3 0.
If not, let's move on. Pranav.
**Pranav Sharma (Google LLC)** 07:25 Yeah, hi. Yeah, I just had this, very small PR about, you know, adding, configuration support for the max export batch size option in AutoConfigure.
I know there were some concerns about adding a new environment variable, but if I understand correctly, like in auto configure, if we add a system property, it was automatically recommended or recognized as an environment variable.
So, I think Jack took a look at this PR, and I proposed a spec change upstream to add that environment variable officially.
Just wanted, like some thoughts on this, or you know, if there's any change that needed. I think I can drop the experimental support if that environment variable gets expect accepted upstream.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 08:18 Yeah, you're right. System properties and environments, environment variables, they're interchangeable. You know, the mechanism that we use, typically, like, we read out the system property notation, which is, like, underscore and dot delimited.
Or lowercase in dot delimited, but, you know, there's a translation process where environment variables get translated to that representation.
**Pranav Sharma (Google LLC)** 08:40 Right.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 08:41 What else is worth talking about? So, yeah, I think we were talking about, like, I was like, hey, if this isn't… we may need the .java to be in there to indicate that this is, like, a Java-specific property, and, you know, I think you indicated, like, this is… this… This is actually, like, a general purpose property, it's not specific to Java. And you're right, but the distinction is, of whether we need the Java as part of the prefix is, like, is this defined as part of the spec, or did Java invent this property? And so, if it's part of the spec, we don't need the Java prefix. If it's… if Java invents this property, then we have to include the Java prefix to prevent collisions with future spec'd properties. And I do think that you're right, that it is a general-purpose property. There's nothing about, like, the concept that's related to Java, but that's just… that's just, like, the rule we follow.
**Pranav Sharma (Google LLC)** 09:39 Got it. Yeah, I think I, this is part of the official spec, like, it's in the periodic metric reader spec, like, this max export batch size option, so… It fits in nicely with the other configuration options there. So, you know, I sent out spec PR, Jack, if you want to take a look at that.
Yeah, just wanted to bring this beyond the attention of folks here. Yeah.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 10:02 And please, other people jump in, and I would suggest that you try to socialize this with other maintainers to other languages.
Because… so, I have multiple hats, right? I have, like, the Java maintainer hat, and then I have, like, the config maintainer hat, and as, like, a declarative config maintainer, who has, like… I've been actively advocating for environment variables to be, like, sort of deprecated, and… And, you know, gone to the wayside, so I've been advocating for not expanding them, and just, you know, only expanding configuration options for declarative config.
So that's what my config hat says, is, like, don't expand the environment variables. But, like, from my Java hat with that on, you know, it seems like a perfectly valid, you know, environment variable, consistent with the other ones, and if it's part of the spec, then we'll support it.
So, you know, these are just the different perspectives that I try to… I have to try to maintain at the same time.
**Pranav Sharma (Google LLC)** 11:04 I see. Sounds good. I think I can reach out to Aaron from, like, the Python SIG, and I can also reach out to someone from JavaScript and see what they think about it.
So if I understand correctly, if the spec gets, like, approved, then there's no problem with the PR barring item.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 11:23 Yeah.
**Pranav Sharma (Google LLC)** 11:23 Okay, got it.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 11:25 Yeah, and if the spec doesn't get approved, or if it just, like, fizzles out or something, like, I don't want to say that we won't do this in Java, but, like, we can… but, you know, we have to make a case, and we have to, like, sort of decide that, well, it would be, like, a Java-specific property at that point, so we'd have to include the Java prefix, and then it's, like, sort of a judgment call, and we don't… we don't… I don't know what our litmus test is for right now for when we add Java specific properties. It's very subjective, I guess.
**Pranav Sharma (Google LLC)** 11:55 If… if we decide, like, let's say, if we decide not to do it either way, then how can… how will the, like, the zero-code agent be able to configure this property other than declarative config? Then declarative config remains the only option to configure this particular thing. Okay, got it.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 12:12 Yeah.
**Pranav Sharma (Google LLC)** 12:14 Okay, well, thank you.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 12:19 And at that.
**Trask Stalnaker (Microsoft Corporation)** 12:20 point, Pranav, if you want to help push on getting the instrumentation, node stabilized in the declarative configuration spec.
that would be the… that's basically kind of the remaining blocker for the Java agent users really fully benefiting from Declarative config.
**Pranav Sharma (Google LLC)** 12:45 Okay.
**Trask Stalnaker (Microsoft Corporation)** 12:48 Jay had… Jay had the, the blog post, recently for the, Java 3.0 preview.
And originally, we were, like.
Promoting declarative config as sort of the first option, but… We sort of had to step back and say, okay, actually, unfortunately, since That instrumentation node, like, you… You can't really use it stably yet in the Java agent, and so we still have to recommend environment variables there.
**Pranav Sharma (Google LLC)** 13:30 I see.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 13:34 Trask, I'm trying to, like, work with Ludmilla on part of that instrumentation stability story, and So the… what I'm sort of advocating is that, the schema for declarative config becomes decentralized, and specifically the definition for the instrumentation node becomes, like, the home for it. It gets moved to semantic conventions.
And… you know, the OpenTelemetry configuration repository would publish and maintain, like, some common scripts and tooling for validation and enforcement to sort of ensure that there is, like, to the extent that we can programmatically verify our schema modeling rules that, you know, we maintain some sort of consistency between this instrumentation type definition that's maintained elsewhere, and the rest of the type definitions, which are maintained in OpenTelemetry configuration.
And then at that point, you know.
like, you know, semantic conventions would have to solve the problem again of, like, further potentially federating it, because I think semantic conventions itself is federated, so maybe the AI definition of instrumentation configuration has to live somewhere else.
But that's the position I'm advocating for right now, and I'm just trying to, like, you know, get some of Ludmilla's attention to try to move that forward. Just wondering, just because we're on the topic, if that aligns with your sort of mental model.
**Trask Stalnaker (Microsoft Corporation)** 15:18 Yeah, so I'm trying to think… so we have the instrumentation node, we have general.
under that.
Which is… The things that, Semantic convention-y, or, like, things that we're actually currently docking.
in the schema.
There's also everything else.
Okay.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 15:46 And I misspoke, because I actually meant that the instrumentation general type would be moved to semantic conventions, not the instrumentation node.
**Trask Stalnaker (Microsoft Corporation)** 15:54 Right, right.
So… Could we, are we comfortable, or do… is the instrumentation Outside of the general node, could we, mark that as stable now?
Or does that not really benefit us until, like, since General is sort of the key piece under there already?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 16:20 That's an interesting question. So… Yeah, what would be… what would be required, and what would be the repercussions of marking the instrumentation node stable?
You know, I think, you know, you're saying immediately, like, not waiting for the semantic convention federation piece to be solved.
So, I think at the spec level, in terms of, like, blockers, at the spec level, there's this, like, you know, there's the language about the API surface area of the instrumentation node, and, you know, needing the three prototypes requirements for that.
I don't know where that stands.
And, you know, it's… I think it's a bit subjective about whether you can stabilize the API piece of instrumentation config and the schema piece of instrumentation config, whether they have to be sort of stabilized together, or, like, you know, can be split.
**Trask Stalnaker (Microsoft Corporation)** 17:29 What are the two pieces there?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 17:32 The, you know, the instrumentation config API in the spec.
And then the instrumentation type node and the OpenTelemetry configuration, like JSON schema, like, would those have to be stabilized together, or can they be, like, disjoint?
had it.
Don't know.
**Trask Stalnaker (Microsoft Corporation)** 17:53 guess, I mean, ultimately, there's gonna be non-stable pieces under there, so… And maybe it's back to that question that has been open of how to mark things as development, how to mark nodes as development, and how to expose that through the API.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 18:24 Yeah, it's… I'm… I… I do think we'll probably… like, it would be much… it would be a much simpler argument to make if we had 3 languages that were all… that all had prototypes of the instrumentation config API, and were, like, sort of clamoring for it, like Java is.
And, you know, without those three languages and that type of, you know, support, maybe there's a way to stabilize the instrumentation type node in the schema, but it's like, you know, we sort of have to do gymnastics to do it. It's.
It's a little trickier.
**Trask Stalnaker (Microsoft Corporation)** 18:59 Yeah.
Yeah, I'll keep track. I think the Python stuff, is… I think there's… support in Python now, and I think the Gen AI stuff might… be using that, but I'll keep a… I'll keep an eye on that, yeah.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 19:25 And I'll try to socialize it, I guess, internally with the folks at Grafana that contribute to the other SDKs, and see if anybody is interested in… And taking that on.
**Trask Stalnaker (Microsoft Corporation)** 19:38 Yeah, and if you're able to join the Samantha Convention meeting on Mondays to discuss sort of that federation stuff.
I think that would be…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 19:55 I don't have a conflict anymore, so I guess, yeah, like, why don't I do that?
**Trask Stalnaker (Microsoft Corporation)** 20:00 Cool.
All right. Jack, you have The next topic…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 20:14 This, you know, I don't think we need to talk about this much unless folks have specific questions. This is just like a call for attention.
I pitched this last week's Java SIG. You know, Josh Surath, who is, I guess I had forgotten this, is not an official approver in OpenTelemetry Java anymore, but was previously, has approved this.
And, you know, I guess he… he was historically a Java approver, and also he's, you know, one of the leads in the entity work as well right now, so I think… It's a pretty good signal that he's approved this. So, if anybody is interested in this, you know, and seeing this move along, please give it some attention.
**Trask Stalnaker (Microsoft Corporation)** 21:04 All right, Jason.
**Jason Plumb** 21:08 Just when we were talking about configuring.
**Trask Stalnaker (Microsoft Corporation)** 21:10 Good, dude.
**Jason Plumb** 21:11 When we, when we were talking about config just now, I was like, maybe 3.0 is a good chance to drop the properties file support.
I don't know that we've talked about this at all.
Or given any consideration, but it helps with the alignment around… Not having 5 config stories, I'm only having 3 now.
**Trask Stalnaker (Microsoft Corporation)** 21:34 In general, I think we've been holding off on deprecating anything… Any of the flat stuff?
Because it's so widely used, and we don't have a stable path forward. Even once we have a stable path forward, it's gonna be a while before we get people… I'm… I'm not sure what we should do as far as… Deprecating. I like the idea of deprecating But not ever removing, kind of idea.
From the perspective of, Pointing new people very clearly towards one supported path.
But not.
**Jason Plumb** 22:25 That's fair. So just for what it's worth, I haven't encountered any users using their properties file.
**Trask Stalnaker (Microsoft Corporation)** 22:32 I'm.
**Jason Plumb** 22:32 I'm sure they exist, but I would suspect that it's a minority.
**Trask Stalnaker (Microsoft Corporation)** 22:38 Yeah.
**Jason Plumb** 22:39 Jack Shirazi is putting me on the spot. Let's see if Jason's migraine brain can cite these five things that he claimed were the configuration methods. Okay.
environment variables System properties, properties file. Declarative config.
Code. Yeah, programmatic. I don't know what the fifth one is, yeah.
**John Watson** 23:06 Programmatic.
**Jason Plumb** 23:07 Sure.
I don't know, I honestly, I pulled that number out of my butt, Jack, so…
**John Watson** 23:20 What about the spring config?
**Jason Plumb** 23:23 Oh yeah.
Sure.
Helm. There you go, Helm.
The one that people actually use.
**John Watson** 23:41 Helm's just injecting environment variables though, right? So that doesn't.
**Jason Plumb** 23:44 Yeah, totally. I know, it's a…
**John Watson** 23:46 It's a dupe.
**Jason Plumb** 23:48 But I don't know, there's probably some amount of people that don't think of it as anything other than Helm.
I suspect.
**Jack Shirazi** 23:55 Do other languages use property files?
**Jason Plumb** 24:00 I don't think so.
**Jack Shirazi** 24:11 Other languages don't use properties either, so… System for those. Yeah.
**Jason Plumb** 24:16 Well, it sounds like we want to wait on it, though, and that there's not any hurry to try and sneak it in or anything, especially with the… like, the… I get it with the stable story for declarative config, so… It was just a thought.
**Trask Stalnaker (Microsoft Corporation)** 24:29 And I… yeah, mostly, I… we don't gain a whole lot by removing this one. Since, like, overlaying, flat properties is easy.
If that makes sense.
It's the… it's the interaction. What would get us a lot is basically sort of deprecating all the flat property stuff, because the overlay over… the interplay between that and declarative config is poor.
Or non-existent.
**Jason Plumb** 25:04 It's true. I mean, that feels a little more nuclear than chipping away at the flat ones, but I'm not going to argue that. It's fine. Like, I see where you're coming from.
I think,
**Trask Stalnaker (Microsoft Corporation)** 25:14 Undocumented. That would be fun. That's really interesting. Yeah. I have no idea if people are using it or not. I don't know how to. It may have. We may have not even. I'd have to look at the code to get history, but we may. That may have just been inherited from.
**Jason Plumb** 25:31 I bet.
**Trask Stalnaker (Microsoft Corporation)** 25:31 Datadog.
**Jason Plumb** 25:32 Yeah.
**Jack Shirazi** 25:33 Somebody somewhere is using every single feature in the agent.
**Jason Plumb** 25:38 I mean, it's that XKCD thing, right?
**Trask Stalnaker (Microsoft Corporation)** 25:48 Cool. Any… Anything else to chat about today?
**Jason Plumb** 25:59 And Yen Cat made a new line here, new bullet point.
**Trask Stalnaker (Microsoft Corporation)** 26:03 That's me.
Oh, that's… oh, am I Nyan Cat?
**Jason Plumb** 26:07 How'd you do that? Nice.
**Trask Stalnaker (Microsoft Corporation)** 26:10 Yeah, it must be you.
**Jason Plumb** 26:13 Yeah, lucky.
**Trask Stalnaker (Microsoft Corporation)** 26:15 How do I go?
Wombats, coyotes, sheep, gopher, elephant, squirrel.
Kangaroo, duck, alligator.
**Jason Plumb** 26:33 I'm elephant. I'm elephant.
**Trask Stalnaker (Microsoft Corporation)** 26:36 How do you know? How can you tell?
**Jason Plumb** 26:38 Because I was typing. I'm typing right now.
**Trask Stalnaker (Microsoft Corporation)** 26:40 Okay, okay.
**Jason Plumb** 26:41 And then I'm looking at this share.
**Trask Stalnaker (Microsoft Corporation)** 26:44 Oh, I see, because I can't see it on myself.
**Jason Plumb** 26:47 Yeah, yeah.
**Trask Stalnaker (Microsoft Corporation)** 26:48 Okay, alright.
Well, stop wasting people's time. Thank you all.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 26:55 See you.
**Trask Stalnaker (Microsoft Corporation)** 26:55 Until next time.
**Jason Plumb** 26:56 Take care.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 26:57 Bye.
**Pranav Sharma (Google LLC)** 26:58 Thank you.
**Bruno** 26:59 Alright.
