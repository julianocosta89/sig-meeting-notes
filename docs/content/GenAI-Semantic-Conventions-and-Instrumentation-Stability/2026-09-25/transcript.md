SIG: GenAI Semantic Conventions and Instrumentation Stability
Date: 2026-09-25
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Aaron Abbott (Google LLC)** 01:45 Buh.
**Christopher Cordi** 01:52 Hello.
**Trask Stalnaker (Microsoft Corporation)** 01:54 Hey there.
**Felix Becker (Anthropic)** 01:57 Hi, everyone.
Are we still waiting for folks, or…
**Trask Stalnaker (Microsoft Corporation)** 02:39 No, let's see, am I… yes, I'm audible, it looks like.
Yeah, let's… Let's go!
Hmm… I hope that… Some other people have done their homework, because I have not done my homework for today.
But first, we've got a topic. So let's… let's go to the topic.
**Aaron Abbott (Google LLC)** 03:22 Yeah, I… I am happy to also do this, after updates, if people want.
We can just do it.
**Trask Stalnaker (Microsoft Corporation)** 03:30 Let's… let's do it. Topic.
**Aaron Abbott (Google LLC)** 03:33 Yeah, okay, so basically what I wanted to just chat about was the… I guess the mechanism and the instrumentations for… that we're planning to do for these breaking changes, I know in the past, we have the Semcom Stability opt-in environment variable, So yeah, I guess I'm basically just wondering if we're planning to do something similar, or, you know, rely on semantic versioning, or… The plan is here.
**Trask Stalnaker (Microsoft Corporation)** 04:13 Sort of thing.
**Dylan Russell** 04:14 We should just make the changes.
So I feel like the repo hasn't been around that long.
Like, I don't think we should worry too much about it.
At least for, like, this first batch. Maybe, like, we should have some breaking change policy, like, going forward, but… Yeah, that's my thought.
**Aaron Abbott (Google LLC)** 04:43 would we… like, it's gonna take some time also to implement these changes, and I feel like it would be good to… If we were to do that, or whichever approach to have it all happen at once.
So, either that means, like, working on a branch, I guess, or you end up pretty much implementing this thing anyway, I feel like.
Yeah, there it is.
**Trask Stalnaker (Microsoft Corporation)** 05:07 Yeah, I'm trying to remember why we didn't carry this over.
Into the new repo.
**Dylan Russell** 05:23 That was kind of like a weird flag that… It was, like… a simple Boolean, and… If you set it, you got everything after 1.36. You didn't set it, you got everything, like, before it.
And it was a pretty big change, and like… How we did instrumentation.
And it was kind of, like, worse the old way.
So I think that's why we got rid of it, and it was like, the new way is just better. Just…
**Trask Stalnaker (Microsoft Corporation)** 05:54 Oh, just breaking, just go… having a single… Version to emit.
**Dylan Russell** 06:09 Yeah, we didn't have, like, version, right? We just had, like… Before 1.36 and after.
**Trask Stalnaker (Microsoft Corporation)** 06:18 Yeah, so… at least in Semantic Conventions, it was documented to… use, this value… Which is slightly different from other, if we look at other Semantic Conventions… So the standard is you opt into… Database, which means database stable.
So this was added as sort of, like, an intermediate thing.
If we carried it over, The existing convention, we would have Stability opt-in GenAI.
Which would mean opting into the stable, what we eventually declare as stable.
I guess is kind of… I mean, Aaron is probably… up to… I mean, there's some wiggle room for Python, you know, for repos to interpret.
To do what makes the most sense.
In the Java instrumentation, the Java agent.
Since the Java agent is declared stable, we've been pretty strict about breaking telemetry.
And so, we would… Probably used this… I think we are already using this flag.
To hide changes, and… But we also do major version bumps every year or two.
**Aaron Abbott (Google LLC)** 08:13 Yeah.
Yeah, I mean, I think we can… we can discuss more… Like, when the military as well, but… Yeah, I hear you, Dylan. There's… it's definitely, like, a bit of overhead. It's kind of… extra… extra work to do.
Maybe just, like, one final point, I guess. I think GenAI is one of the places we see the most native instrumentation adoption, so… in, like, some Google stuff.
We see it in the MCP SDK, I think Python has the native instrumentation.
I… I guess there's some stuff… Felix, I don't know if you… if you have context, but some stuff for Anthropic, and… Yeah, I guess, like, we haven't obviously… Recommended this environment variable for things that are natively instrumented, but… Do you have… do we have plans?
for what we're gonna do. I think… I think Microsoft also has… The current Semantic Conventions implemented in…
**Felix Becker (Anthropic)** 09:13 What would you just set this variable to? Do you just say, like, true, or, like, is it a major version?
**Trask Stalnaker (Microsoft Corporation)** 09:20 It's a list of, semantic Conventions… stable semantic conventions you want to opt into.
**Felix Becker (Anthropic)** 09:29 And then everything else just doesn't get emitted.
**Trask Stalnaker (Microsoft Corporation)** 09:34 No, it's whether… so, say you have existing instrumentation that's emitting the non-stable semantic conventions.
And you want to add support, you want to change.
To support the stable. That would be a breaking change.
Even though they were technically not stable before.
And so you would… And maybe that's why we didn't… do this, add this in GenAI? Because… so the history of this is we added it for HTTV database RPC, because we've had kind of… we had never declared them stable in semantic, but they've been around for so long that we had to kind of retroactively call them de facto stable.
**Felix Becker (Anthropic)** 10:27 Hmm.
**Trask Stalnaker (Microsoft Corporation)** 10:29 And…
**Felix Becker (Anthropic)** 10:30 Is the Stability opt-in basically just… Pinning it to one specific major version and everything past that is, like, evolving, but, like, there's no mechanism to ever have, like, a second major version, do I understand this correctly? It's just, like, this is, like, one point in time that we decided was stable, and everything that… after that will eternally be unstable.
**Trask Stalnaker (Microsoft Corporation)** 10:56 So, that is the weakness of this.
approach.
It has… so we have a better approach now in the declarative configuration.
Let's see, Semcom… So, in declarative configuration, you actually get… it actually… we built this more recently. This was built a long time ago, initially, for the HTTP… sort of these de facto stability issues.
This is the hopefully future approach, which… Allows you to… does handle, sort of, multiple major versions.
**Felix Becker (Anthropic)** 11:40 So is this something a user defines?
Like, what version they want? We got it, yeah, that makes sense to me. Yeah, I'm definitely thinking about this, like, especially because the GenAI Conventions are changing very rapidly, so right now we're, like, saying, oh, we're emitting this specific commit hash of the spec.
But, yeah, like, between commit hashes, there's all sorts of breaking changes, and… I haven't fully decided yet if, like, we're gonna maybe come up with our own… configuration variable that's, like… what version do you want us to emit? And we support certain versions, but in any case.
we would then need it to be a little less frequent than, like, or fine-grained than the commit level, right? It would need to be a bit… you can't have backwards compatible, like, different… variants for every single commit, it would have to be, like, certain V1, V2 releases.
**Trask Stalnaker (Microsoft Corporation)** 12:38 Yeah, and so that was kind of the… Goal of, like, having… when we marked, say… you know, the de facto stable, we said, okay, 1.24, for example, Instrument… existing, database instrumentations should not change the version. So basically, we said they should not upgrade to any of these intermediate versions until we hit stable.
Semantic Conventions.
Because we didn't want… there to be… 10 different versions of Semantic Conventions out in the world.
getting emitted. It's easier for backends if they can be like, okay, we support this version, and we support stable.
**Felix Becker (Anthropic)** 13:26 Yeah.
I mean, I… it sounds to me like this… Stability opt-in is maybe a bit more of a hack that we maybe shouldn't use, and I would much rather we have, like, the newer thing that actually has, like, version numbers, and then… Maybe in our repo, also, we can, like, get to tag each release with, like, a… version, so… You can, like, reference what was the spec text at that exact version.
**Trask Stalnaker (Microsoft Corporation)** 13:59 Yeah… So this… the declarative configuration, it's still only kind of defined around, major versions.
And experimental… there's also an experimental… This doesn't show, this is just an example snippet.
But it's not… You don't pin minor versions in here.
Ideally, we wouldn't have that, right? Like, minor ver… like, ideally, minor versions are all going to be backwards compatible, and so you can… instrumentations can always just emit the latest minor version.
And then major versions represent breaking changes.
The problem is the current state we're in, where nothing is stable, and so we're breaking every minor version.
**Aaron Abbott (Google LLC)** 14:59 Yeah, I think… so, one thing I just wanted to call out is, like, in Python, the job is actually maybe a little easier, because we can version the packages that people install. It's not like we ship, like, an Uber super-vendored thing, kind of like the Java agent.
I think for, like, an agent that people use, something like, I don't know, Cloud Code or whatever, like.
people don't really have that option. They're just gonna install the latest thing, and they might need this configuration, so… I don't know, maybe, maybe for, like, the Python GenAI repo, we can… Rely on documenting the versions and just be aggressive with the major version bumps or something like that.
**Felix Becker (Anthropic)** 15:40 I definitely imagine that the GenAI Conventions will probably have to evolve faster in the future, too, and not have the luxury of, like, locking themselves into one version forever, so… Yum.
**Trask Stalnaker (Microsoft Corporation)** 15:54 Now, are you, Felix, are you emitting by… By default, because that's another option if you kind of hide the, like, hey, users have to opt in to open telemetry.
And therefore, you could mark that whole opt-in as experimental.
Which helps with the braking.
Changes, as opposed to… Anything that's emitted by default, that… that's tough.
**Felix Becker (Anthropic)** 16:25 In the SDKs, we are gonna emit by default if there is, like, a tracer provider registered.
But you… if there was a change in the schema, right, you would upgrade your SDK, and so there's a little bit of an explicit… action.
Whereas in the server… It might be, like, a… if there were some serious ranking changes, we might add, like, a config option that's like, do you want V1 or V2 of the GenAI convention?
And then, yeah, it's opt-in on the server.
**Aaron Abbott (Google LLC)** 17:09 I guess maybe my question, Trask is, like, should we consider things that are natively instrumented? Like, is that in our scope to figure out how they should do this? Should we try to give them… Like, a control mechanism for this.
**Trask Stalnaker (Microsoft Corporation)** 17:24 I mean, it would… be potentially helpful. I know that it's come up, I remember in one of the Microsoft SDKs, it came up, Because they didn't want to… Break, the telemetry.
But there were requests for supporting the latest So it's nice to have some kind of standard mechanism.
**Felix Becker (Anthropic)** 17:56 I… I think it would maybe be good, if we are going to have major burdens, to, like, have one standardized.
NFAR, that's, like, how to set the version for… for, like, SDKs or Instrumentation, just so that it's not, like, every Instrumentation doing themselves.
**Trask Stalnaker (Microsoft Corporation)** 18:17 I would…
**Felix Becker (Anthropic)** 18:18 Technically, we also don't need to do that yet, right? Unless you want to kind of manage the rollout of this very first version through that variable, too.
to, like, have a V0 that was, like, you know, before this big… set of breaking changes, and then the V1 is, like, the first release, and still support the B0.
**Trask Stalnaker (Microsoft Corporation)** 18:44 Yeah, and I think that's the problem that I had seen, with the Microsoft FDK, where the… they had already started emitting, the V0, one of the experimental versions, by default, and so… They needed a way to… opt in… for users to opt in to the latest. They're not ready to take a major version bump of the SDK just to… Change the telemetry output.
Would this… Do you all have declarative config in the… in Python now?
**Aaron Abbott (Google LLC)** 19:30 Yeah, we… we have it, it's not… It's not super integrated with the Asian, but yeah, yeah.
**Trask Stalnaker (Microsoft Corporation)** 19:39 Well, this whole… the whole instrumentation notice… In config… in declarative config is still.
in development.
**Aaron Abbott (Google LLC)** 19:46 Yep.
Okay, so maybe I, like, should we just discuss it again later? Like, should I file an issue? Sounds like… We're not completely decided.
**Felix Becker (Anthropic)** 20:03 That sounds good to me. I would… I would just, like, the stability opt-in, that one seems really, like, not well-fitting for the GenAI repo, so I would steer away from that.
**Aaron Abbott (Google LLC)** 20:19 Okay, that's fair.
I will… I wish I could…
**Trask Stalnaker (Microsoft Corporation)** 20:23 when Lynn is back, it'll be good to, she might… because I feel like we probably had that discussion, which is why we removed it in the new repo.
I'll, but I'm not remembering.
Alright.
Yeah, and then let's get it on the… go ahead and put it on the project board for the Stability Project Board.
Felix, let's… Talk about… Chat versus inference. Chat operation versus inference span.
**Felix Becker (Anthropic)** 21:13 Yeah, can you open the shoe?
**Trask Stalnaker (Microsoft Corporation)** 21:15 Yeah…
**Felix Becker (Anthropic)** 21:17 So maybe this is also a conversation for the larger working group, but I just wanted to maybe put it on the radar for the stabilization effort, because it could be a bit of a breaking change.
And also, you mentioned this, like, Formalization of the… Actual, span type.
Which kind of is a bit, like, related to what I'm trying to say here, but basically the, the problem I see is that we have this inference span that is defined as, like, this is supposed to be one request to the model of running inference, but, and it's… it's also defined as, like, it has, like, the GenAI operation.name as chat or text completion.
But in practice… and in practice, like, that is the span that, like, all the instrumentations for OpenAI, Anthropic, like, on the client, Gemini.
Assigned to, like, the… messages API request, or text completion request. But in practice, that is actually not a one-to-one mapping to inference calls, it's a one-to-end mapping to inference calls. Because all three providers have a server-side tool loop within, like, the messages API, or the, Responses API for OpenAI.
And so it's actually… if you scroll down a bit, I put, like, a little ASCII diagram in there.
It's actually, like… you call… you call chat responses API or Messages API, it does inference. That could trigger a tool called, like, Web Search, it runs that, then it runs inference again.
then maybe another tool, and so on. And so… the current conventions, I think, are kind of written by, like, with the assumption that everything is client-side, and so you never see these internal inference spans, or you couldn't emit Spence for them, but with servers emitting them to… We would actually like to represent those internal calls.
And now it creates this problem where, like, it's not clear what is actually the chat span, what is actually the inference span.
And then similarly for Invoke Agent, you have a similar problem, where, like, that doesn't actually necessarily call to the, like, what's the chat API and, like, the messages equivalent?
It just calls the model directly, because it already has its own tool loop.
And so it then also feels inconsistent to, like, put Chad kind of on both of these attribute… on both of those spans. My preferred solution here would be that we actually split these two up and say the inference span Represents inference, like, the actual underlying inference call.
and the… chat request.
is a separate span type, that still preserves that, like, GenAIOperation.name equals chat.
but… can map to 1-to-N inference calls.
And this may become very relevant if we're, like, standardizing now the inference type, because currently inference… like, the inference span type is just an internal spec, internal concept, right? And it's just the GenAI.operation.name that consumers interact with, so we could still… Split these up relatively cleanly right now, without… really breaking existing people, or completely, like, messing everything up. But once we actually say, like.
chat is type equals in friends, it becomes kind of very messy, or like, it would… it would… Embed in the public observable schema that, like, there's actually this impedance mismatch.
Alright, sorry, that was my long-winded explanation. I see there's already two hands up.
**Aaron Abbott (Google LLC)** 25:38 So just to be clear, like, this first ASCII diagram here, is that what you want, or is this the problematic one?
**Felix Becker (Anthropic)** 25:47 It is just a representation of reality, off the call, and what is in parentheses right there with inference basically doesn't have And, like, a correct name right now.
**Aaron Abbott (Google LLC)** 26:00 There you go.
**Felix Becker (Anthropic)** 26:01 Like, right now, you have to decide, do you put the inference or chat span either on the internal inference or on the outer chat one?
And it… it would be weird to put them on both, right? But then one of the two doesn't really have any type.
**Aaron Abbott (Google LLC)** 26:19 No, I see what you're saying. I think… I was just gonna call out, like, I think VLLM has some instrumentation. I don't know if they're following our conventions, but it sounds like you're basically saying the difference between inference happening, like, the, you know, the actual inference running itself internally, like, you know, the GPU and stuff like that, versus… the API level of it? Is that kind of what you're getting at?
**Felix Becker (Anthropic)** 26:47 Yeah, I mean, not even that low level, just, like, one request To… the model.
**Aaron Abbott (Google LLC)** 26:58 Yeah, I think you're next, Surya.
**Felix Becker (Anthropic)** 27:00 like, uninterrupted by tool calls, just where the model starts generating tokens, and then finishes generating tokens with a stop reason, right? Like, that… To me, it's one inference span, and that's also kind of how the… how the existing spec describes the inference slash chat span, but the chat request is not actually that. It has, like, internal, multiple inference calls.
**Surya Teja** 27:30 So, Felix, I have a couple of questions on this one. So, when… say, for example, I'm using the Messages API, and if I'm instrumenting it, if I call messages.create, client.create, that's a real inference plan. But say, if I'm using the Cloud app.
and I type in some message. When you send over that prompt to this server, behind the scenes, you are doing a couple of operations, like, say, a web search and everything, and that's not an inference plan. So.
You want to represent those kinds of operations differently.
So that you could distinguish between a tool call that is happening on the server side, as well as the inference call that happens after the server result is returned back or something, so that, you can represent the actual steps that are happening behind the scenes on the server. So, that's what you are trying to do with this one. So that's the first question.
**Felix Becker (Anthropic)** 28:36 Yes, if I understand you correctly.
**Surya Teja** 28:39 Yeah.
**Felix Becker (Anthropic)** 28:40 Basically, the problem arises when you have servers and, like, AI providers actually emit open telemetry from the server.
**Surya Teja** 28:50 Yeah.
**Felix Becker (Anthropic)** 28:51 The, like, internal… what actually made up this message's API request, right? Because customers wonder, why did this take so long? And it could be… and they think, oh, it's because inference took so long. But actually, there was a web fetch tool call, and the server was just really slow to respond, right? And we don't want them to then think that it was inference that took time.
**Surya Teja** 29:11 Yeah.
Yeah, I… sorry, Trask. If you are fine, I can go ahead, otherwise I'll wait for you to add your thoughts.
**Trask Stalnaker (Microsoft Corporation)** 29:21 Yeah, just wanted to clarify that, it's not specific to, cloud, like, coding agents. You're saying this is for any, like, just even, like, your standard open API calls the server, what we think of as inference. I make a call with my Copilot SDK, anything. The server side is… That's not just an inference call, it's actually a… I didn't know… I didn't realize that tools run on the server. Yeah, okay, cool.
**Surya Teja** 29:58 Yeah, the second part, sorry, I'm getting overexcited about this, sorry for that. Because, this is the same problem that Ludmila was trying to, solve.
in the, in the, agent invocation or workflow thing, there was a discussion that happened around this, and, the idea was to use TURN whenever we are making a call to a local agent, or when we are making a server-side call to an agent. I'm just using broadly an agent to represent all Claude or ChatGPT, or anything. So, what it means is.
You are parenting that operation at turn, and whatever is happening beneath the scenes, say, the tool calls, either on the server side or the client side, or the inference calls that are happening either on the server side or the inference side, they can be, Parented as a hierarchy on this… under this turn.
So, that was something, Lyudmila and others were proposing, so that We can use turn span.
For, the variant hierarchy, and all Things that happen beneath the hood can be, used to represent as a hierarchy. I'm going to pause here and see… If that aligns with, the problem that you're speaking about, It's Felix.
**Felix Becker (Anthropic)** 31:30 I… So you're saying there is a turn span that could be used here?
I… yeah, technically, like, this is a server-side tool loop, and so you could add, like.
the, like, wrap the things that was in my ASCII diagram with turns spans each.
I think the problem still stands of, like, What is the existing chat?
attribute, what does that mean, and what does the, like, inference span mean, and what do… what… Operation or type are actually the real inference.
spans.
**Surya Teja** 32:09 Yeah, sorry, I got confused. Your explanation makes sense to me now, but ignore the turn span for now.
Okay. Thanks.
**Iwa Wong** 32:23 Yeah, I know that we are over time, but I have three, questions, really, related to the, agent, info agent spend. Number one is related to MCP, whether it would be, going under inference for two calls.
Number two is, how do you… how does the team here envision about sub-agents?
Whether it will have its own, like, invo agent spend, or do we actually roll out to the parent one?
number 3, it is regarding, the… The identity side of things, if the team has any idea of, like, how do we handle, approval side of things, because, like, I think the Agent Loop side, at least on the OpenAI side, I'm aware that, there are, like, the approved for me, sessions, for example, like, I mean, if you have, like, a sandbox, that is, set up with, like, permissions profile, if there are actions or, like, the agent decided to actually do outside of Sandbox, then it would actually escalate.
How… what about… I know some of these things happen on the server side. I'm curious how does a team think about, like, whether it would go wrong into, like, inference? Like, would there actually be a separate… saying, say, like, a proofful, or, like, Some of these safeguards.
**Felix Becker (Anthropic)** 33:59 Yeah.
Maybe we can take those questions onto the issue, and then the last one, I would say that's actually a very good question that I would love to discuss more another time, too, because I think… Yeah.
with the structure of open telemetry and traces, we actually can't really represent… like, we can't have a span for waiting for confirmation, because those happen and completely… they'll span the server and the client, they happen in completely different places.
So I agree on that. Just to answer your MCP question quickly, MCP calls, when you use, like, the MCP connector, like, you have OpenAI or, Anthropic just connect to the MCP server, those would be the same as web search here, so that's just, like, a server-side tool call.
**Iwa Wong** 34:47 Interesting,
**Felix Becker (Anthropic)** 34:49 But you can also connect client-side to MCP servers, so that, of course, would then not… be inside of here.
both impossible.
**Iwa Wong** 34:59 Interesting. Yeah, we… yeah, I can Slack you, To close out on these videos.
**Felix Becker (Anthropic)** 35:06 Chat more about this.
**Iwa Wong** 35:07 Yeah, sounds good. Thank you.
**Felix Becker (Anthropic)** 35:11 Just to wrap this up, what, what should we do here? Like, is… Is there… do you guys feel like this is actually something we should solve?
**Trask Stalnaker (Microsoft Corporation)** 35:27 Sue, I think that… Some of the server-side stuff we have said has been out of scope.
But… I think, in particular, I think we've said that this. I think we've said this part has been out of scope, at least to date.
But that doesn't mean… but, sort of, what you're saying is, even if this is out of scope, we still need to think about being able to evolve to the future, and that still affects what we have today.
So, I think it's a…
**Felix Becker (Anthropic)** 36:08 The thing that would worry me is if we do the thing where we publish the, like, type attribute, and we actually start calling the chat span publicly, like, the inference span in the schema, because then it's just, like, kind of forever actually a misnomer.
**Aaron Abbott (Google LLC)** 36:24 Yeah, I agree. I think that's my takeaway, is that the inference should be clearly, like, API inference, not, like.
The actual inference.
**Felix Becker (Anthropic)** 36:33 Yeah.
**Aaron Abbott (Google LLC)** 36:33 Should be clear.
**Trask Stalnaker (Microsoft Corporation)** 36:35 Yeah, let's get it on the board here… But yeah, so I think that would be sort of, you know, the piece we would want to tackle, at least in the stability section, is that.
Part of it.
**Felix Becker (Anthropic)** 36:51 Okay, sounds great.
Should I erase this again on next Tuesday, and then general?
**Trask Stalnaker (Microsoft Corporation)** 36:59 I would, from the perspective of… there's been some… there's a couple of people I know who have been interested in server-side… Stuff that we haven't gone into, Although, I guess even on the… yeah, even for renaming… Yeah, it would be good to get some broader perspectives. It sounds very reasonable to me, but I, like, I'm not as deep into it, the space as some people also.
That would be great.
And then, I think Lyudmila is… Back maybe end of next week, or maybe the week after.
Cool, we didn't get to this. As I said, I didn't do my homework, but if anybody has updates here, yeah, thank you for, yeah, just please go ahead and post status updates over here, would be great.
Alrighty.
**Aaron Abbott (Google LLC)** 38:14 Cool. Thanks, everyone.
**Trask Stalnaker (Microsoft Corporation)** 38:16 Thanks, everyone. Enjoy the weekend.
Right.
**Surya Teja** 38:19 See you guys.
