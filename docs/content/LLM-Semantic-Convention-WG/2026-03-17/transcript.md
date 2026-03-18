SIG: LLM Semantic Convention WG
Date: 2026-03-17
Duration: 56 minutes
============================================================

## Zoom Recording Transcript

**Trask Stalnaker** 01:15 Hello again.
**Keith Decker** 01:18 Good morning.
Or afternoon, wherever you are.
**Erdenesaikhan Tserendavga** 01:23 Good morning, Adrian.
**Trask Stalnaker** 02:41 We can't hear you, Linmilla.
We can't hear you, Lytmila.
Can anyone hear me?
**Keith Decker** 03:02 Yeah, I can hear you, Trask. I can't hear the bill either.
**Aaron Abbott** 04:04 Hello.
**Trask Stalnaker** 04:06 Yes.
**Liudmila Molkova** 04:07 It's embarrassing. I'm sorry, I don't know what happened.
Okay.
Let's get backdate.
Okay, this is sheer.
So the pro… Of this thing, it's just a grouping thing for… LLM and 2.
It adds nice.
Beautiful.
And if we do this, it's probably opt-in.
**Aaron Abbott** 05:09 Yeah, this seems to have a lot of overlap with the workflow.
**Liudmila Molkova** 05:15 The workflow is across multiple agents.
This is… for one step within Invoke Agent.
**Aaron Abbott** 05:28 Okay, okay. So, root… proposed here, like, react… overall thing.
**Liudmila Molkova** 05:37 Yeah, Ankit?
**Aaron Abbott** 05:48 Are you… are you muted, Alkit?
**anksing** 05:52 So, yeah, my bad, I was muted and speaking. Thanks, Aaron. So, this looks very similar to, like, the chain nodes that created… that gets created when you, instrument line chain code, where the step looks very similar to me.
So wanted to call that out.
And I think in, Some of them, the way it was, like, in line chain, like, everything can be, like, a chain.
Because it's always, like, an executor and a run.
So… I don't know, like, if that needs to be… Shown specifically here, or can there be a more… like, an abstraction on top of it, like, this is just how Langchain… Like, framework kind of models thing.
And does that really neatly. For example, here, like, React step, right?
React step… React step that you see everywhere. It's very similar to, like.
The chain node that shows up In 191 as well.
**Liudmila Molkova** 07:01 Yeah, I think we have some instrumentation for link chain.
Did people instrument it here?
**anksing** 07:14 I don't know in the open telemetry and the Contrib repo, right now, I think only LLM spans are instrumented.
So there, I don't see, I think, those, chain nodes showing up.
That's what I remember.
But I can try it out, like, probably.
I tried out a couple of months back, so probably I can travel later. And now, to see if there's any changes there.
**Liudmila Molkova** 07:48 My… so I think there are two options. First, we just don't do this.
I think it still can be supported, like, this grouping can be a visual concern, because you know that this LLM ended with an execute tool, and visualization can just be based on this without a new span.
It know, it, it might know, like… It… It has no specific knowledge, but it can map the… Tool name from the response to that tool name in the next execute tool.
Or something. And I… I… Seeing that if this is done, it should be opt-in anyway, so the benefit of, like, adding it to the instrumentation is pretty low.
So I'm inclined to leave a comment here.
With this, and, move it.
They keep it open, so we collect feedback.
Let me spend a couple of minutes here.
You do!
Sorry for spending… So much time on this. Let's take a look at this one as well.
Kill Span.
Dynamic loading of skill packages, skill fi… Filter and actual invocation Progress.
**I'm… Aaron Abbott** 12:13 I wonder if, I can definitely see the value of seeing when the, like, the skills were loaded, so you could understand when they came into context, or when it decided to load them, but… This seems, like, pretty similar to skill… Sorry, to tool overall, right?
**Liudmila Molkova** 12:34 Yeah.
Is it… can skills be removed?
**Aaron Abbott** 12:44 I don't… I don't see why not.
I think we'd probably have to check some, frameworks and see how they… Implement the skills.
**Liudmila Molkova** 13:04 Yeah.
**Aaron Abbott** 13:06 J.
**Liudmila Molkova** 13:07 So essentially, this would require research.
And some prototypes.
**Aaron Abbott** 13:17 Yep.
**Liudmila Molkova** 13:20 Okay.
I don't want to take a lot of time from this call anymore, but, if anybody has thoughts… Please show them.
Okay, do we have any new members that would like to say hi?
P.S. Welcome?
You're also welcome.
Okay, feel free to jump in if you want to say hi and introduce yourself. I understand it's weird that, You're introducing yourself, but other people don't.
It's just very hard for everybody to introduce themselves on every call.
Oh, Leighton, you're shy.
**neil yashinsky** 14:15 I'll introduce myself, Ludmila, if you wanted me to get the ball rolling again, people feel comfortable sometimes.
sometimes if they're not the first to go. If we want to focus on other agenda items, then we don't need to, spend much time here. But yeah, I'm Neil Yashinsky. I only started attending hotel meetings a few weeks back, and I'm really excited for the potential to learn from so many smart people, and possibly contribute a non-terrible thought every once in a while. So, thanks for the opportunity. We are always better off with people's contributions, so that's a thing that I really love, is, like.
I am to quote a general, I can't remember his name, but vitality springs from diversity, and diversity of thinking is very important, I think, for something like, ironically enough, conventions. If you want to establish good conventions, it's got to come from a diverse group of individuals who think differently, but can agree on some very important things. So, if you're already here, you're doing, you know, 90% of the hard work is done by just showing up, so… Welcome.
**Liudmila Molkova** 15:24 Thank you.
Awesome.
Then, let's move to the first topic on our agenda. This is the splitting invoke agent Trask, do you want to talk about this?
**Trask Stalnaker** 15:49 We can just look at the description there. I think it's… Basically, covers, what is changing here. So before, we had, we said that the span could be either the kind for Invoke Agent could be either client or internal.
And this PR splits those into two separate span definitions, so that we can be more precise about which attributes apply to client invoke agent, and which attributes apply to internal invoke agent spans.
So you can see on the client side, the… some of the response attributes… are removed, and in the… the link, if you want to… if anyone wants to see, I know we looked at this, I think, last week, But I did some research over here.
To look at what, existing Gen AI libraries, expose.
And so it's… Based on that.
So I didn't see anyone exposing those Attributes like model on the… Client spans… And then… Another interesting piece, and if you go back to the description, Is on the internal spans.
I removed the tokens… The token attributes.
And… For the most part, they don't expose. There was one that did expose an aggregation of the tokens used, underneath it.
But we had discussed, I think last week, about That making aggregating over your tree more difficult?
The token usages.
And… So I removed that.
It's also, I mean, arguable how much use… I mean, it's kind of interesting, the total token usage, but if you don't have the model that it's associated with, which in the invoke agent internal spans, it could be multiple models.
It's… Much less useful.
So yeah, would love… thoughts… Reviews from folks who know more about this than myself.
**Aaron Abbott** 18:56 Yes, I think I owe you a review task, and I was going to, see if I can get some feedback from the UI team.
On the token question in particular.
And, yeah, I'll follow up on that.
**Trask Stalnaker** 19:13 Awesome. Yeah, and anyone else?
Love your… Review feedback on… on it as well.
**Liudmila Molkova** 19:29 Thank you. I was thinking that, Surya, do you want to speak up?
**Surya Teja** 19:39 Yeah, for sure, I took a pass at the PR, and it's really a step in the right direction, and I really like the vision that has been set in this one.
the reason I'm a little behind, because I'm trying to understand the gist of it and the granular details. I will add in a few comments around this, but those are going to be questions, but overall, it looks great to me. Just wanted to add this in because It's integrating the ecosystem well.
with different providers, like OpenAI and Anthropic in picture.
**Liudmila Molkova** 20:17 Boom.
**Trask Stalnaker** 20:17 Great, thank you.
**Liudmila Molkova** 20:20 Makes me think that maybe we should document somewhere that we see the token usage.
Ever only appearing on belief notes.
Not just for this, too, but just in general.
**Trask Stalnaker** 20:38 Yeah, so we've still, in this PR, it's still being captured on… Invoke agent client spans?
Which… Could be a leaf node if you don't have Tracing of your remote system, but might not be a leaf node if you do.
**Liudmila Molkova** 21:00 Okay, unknown clients.
And servers.
Boundaries, not internals. Yeah.
**Trask Stalnaker** 21:08 Yup.
**Liudmila Molkova** 21:11 Yeah, I think I, I… They like this mental model.
**Trask Stalnaker** 21:17 Possibly not servers, since… They have nested, and that kind of relates to, the… next quest… the next topic, anyways, so let's move on.
**Liudmila Molkova** 21:30 Yeah.
So this has the approvals now, but here, folks, Should we resolve it?
**anksing** 21:45 So I think, there were questions now about, span kind internal.
Span Kind Server for Invoke Agent, and how they can probably coexist. If they do coexist, like… And there's a very, common scenario right now where I can have my line chain or any framework code that I created, like, which runs as is on the client. Then I put this behind the server.
And… So when it was running on the client side, it emits an invoke agent client span, and then when you move it behind a server, probably it's emitting invoke agent internal span, right?
Then, having that encapsulated by the service in an invoke agent server span.
Does that add any value?
Or can that internal and server coexist?
**Liudmila Molkova** 22:51 So let's see.
This is the… Internal… this is the invocation.
Let's open another one side by side.
That's the… Internal.
**Trask Stalnaker** 23:16 So I guess part of the question here is that we're kind of debating ourselves the… About this… proposal.
is that, I mean, your server… like, are you still… are you going to capture the HTTP server span that, for your REST endpoint, and then you're calling… LaneChain, which is generating then an internal Invoke agent, span.
Or… You know, is this something that… Only would apply to… kind of custom… Bill… Servers that are dedicated to invoking agents?
It's not really… there's not really a protocol for… invoking agents at this point, so the server span… Although… I mean, we do… we did decide with RPC, for example, that it's at the logical layer, so… Certainly could justify having an invoke agent server span as being the logical layer there.
**Liudmila Molkova** 24:45 I'm… I see what you're saying. I'm coming from the perspective of, okay, they look the same on the surface, but information you get on the client is probably very different from information you get on the server.
For example, we are very optimistic here with having Like, named Edge and description version.
In invoke agent on the client.
But they are probably always available on the server, and along with many other things that would be important on the server.
**Trask Stalnaker** 25:20 So it's not so much about the difference between client and server as the difference between server and internal.
**Liudmila Molkova** 25:27 Yeah, the internal, I mean, the information available about things… About the… oh, yours… oh, yes, I see.
And then… How would we feel about modeling internal span as a child of remote?
Quiet.
**anksing** 25:48 Yeah, exactly.
**Trask Stalnaker** 25:51 if you didn't have the HTTP.
**anksing** 25:54 Yeah, which are all.
**Trask Stalnaker** 25:55 Yeah, in there.
**anksing** 25:55 Yeah, which are always, like, you could always not admit them.
**Trask Stalnaker** 26:04 But then in frameworks, you don't really know… I mean, in Langchen, you don't know when you're emitting the span.
That's just always gonna be an internal span.
**Liudmila Molkova** 26:16 And it will always have either no parent or local parent.
**Trask Stalnaker** 26:24 Unless, I mean, you… your HTTP server, like, you could propagate context down and not capture the span, the HTTP server span, but that would be… Kinda weird.
**Liudmila Molkova** 26:36 It would be the server span. So maybe the only difference between them, that they are declined, is different.
**Trask Stalnaker** 26:46 Yeah, and is that weird?
In… to have… Something that only differs by span… like, semantically.
**Liudmila Molkova** 27:02 There's defense as well.
There's the French.
**Trask Stalnaker** 27:10 That's true.
So you're kind of collapsing the… HTTP server span into.
**Liudmila Molkova** 27:25 you were collapsing some, protocol span. It could be something not HTTP.
**Trask Stalnaker** 27:32 Right.
So what would, I mean, as far as prototype, This would only be a… kind of custom server, like, how… we wouldn't have any… open source… Prototypes for this.
Server span, I assume?
Does anyone know of any… sort of… server… That open source server that is… just about… That you call Invoke Agent.
**Liudmila Molkova** 28:34 The A2A agents, maybe?
**Aaron Abbott** 28:37 Yep.
I mean, I think a lot of model frameworks, or sorry, a lot of agent frameworks expose, like, an API, Some of them, you know, a lot of them do expose A to A also, but for example, I think Wangchain… I know ADK, they have, like, an API server command, which just exposes a server, and… When you do that, it's… yeah, you can look up API underscore server.
Yeah, when you do this, like, it's running with Ubicorn, like, there's a whole stack that it includes, and there's probably a Swagger document defined somewhere.
**Trask Stalnaker** 29:18 So in… let's take that link chain example.
I am assuming if you… Ran that, it would probably… today capture an HTTP service ban, and then an invoke agent Internal span underneath it.
**Aaron Abbott** 29:44 I don't know if link chain's a good… like, like, what it should do, you mean? Or, like, what it… Just because they do their own weird thing with Lingsmith, but That… that is what I would expect, yeah.
**Trask Stalnaker** 29:59 Okay, but that helps, yeah, I… we can look at… I think that would help us to look at some… sort of… prototypes.
**anksing** 30:08 So, that would be true for, like, any web server that's put in front of an agent, right?
**Trask Stalnaker** 30:18 Yeah, so I guess that's the question here, is… Are all of those examples going to be capturing an HTTP REST endpoint, HTTP server span, and then an invoke agent?
span underneath it, internal span underneath it, and is that… the preferred modeling I mean, because it is an HTTP server.
**anksing** 30:54 Like… Can we call agents over a different protocol as well?
I think that should be possible then.
**Like, not just HTTP, like… Trask Stalnaker** 31:05 Sure.
**anksing** 31:05 I'm the GRPCO, right?
I mean, that's… I did this look possible?
If you really need to.
And for A2A also, like, is it, like, different protocol altogether, or… Something like… Yeah, it's good.
**Aaron Abbott** 31:28 Yeah. Yeah, I can say A to A is always HTTP. Sorry, sorry.
It's… I think it's HTTP or gRPC.
But they don't… it's not transport agnostic, there's, like, a fixed list of transports that are supported.
**anksing** 31:43 Got it, okay.
**Liudmila Molkova** 31:46 And the product… anksing 31:48 So, similar thing would come up in MCP as well, right?
I don't know.
**Aaron Abbott** 31:54 Yeah, yeah, it's… neil yashinsky 31:55 I think so.
**Aaron Abbott** 31:57 Yeah, because MCP also supports, like, you know, standard I.O, which has no.
**anksing** 32:02 Yeah.
**Aaron Abbott** 32:09 Yeah, I feel like we're fighting the… way that hotel is designed to just kind of naturally compose, like, without you thinking about it.
I don't know if you guys get that feeling.
**neil yashinsky** 32:20 it's… maybe we're just so new that, like, these things are changing so fast that they're trying to not quite… it's not hurting cats, but I think, like.
you know, how old is MCP itself? It's, like, a year-ish or something like that, and where it fits in all this, and I think people still don't really know, like, if that's the ideal, or if it should use something different than what, I guess, the standard in standard… or, well, standard out? Is that how it, like, kind of, like, works, essentially?
I'm not an MTP expert by any means.
**Liudmila Molkova** 32:54 HTTP, it's, it's pluggable.
**neil yashinsky** 32:56 Oh, right, right, yes. So, by default, yeah, thanks for what would be the way to standard out, I guess is the way you say it. And so that… but I think back to your questionnaire is, like.
Kind of finding out the commonalities, even to what they do versus how they do it is, we're on the forefront, I'd say, so it's less… clear. The past models are… need reconsideration for the new context.
**Liudmila Molkova** 33:26 MCP servers are similar in a sense. Remember, folks, I think our end, we had these discussions that we… when we have MCP server over HTTP, we're saying that the HTTP in coming context is in parallel, is a sibling of MCP servers, Ben.
Because… of how… Http context is orthogonal to… logical flow, and that the one HTTP request can carry multiple MCP messages, so I think that this is some somewhat common.
I… But… It seems like that we're… at least here, we would be really breaking the natural flow of… Having… The incoming request processing.
Handling the… Covering the Invoke agent.
**Trask Stalnaker** 34:47 That was kind of where I was leaning with… As we were… as we discussed internally.
**Liudmila Molkova** 35:00 Would anything bad happen if we just start with the internal span? No network information, then?
**Trask Stalnaker** 35:13 I don't… I… I'm Ken, maybe you can enter that.
**anksing** 35:19 I believe, I mean, the major idea of having this is to show how agent is coming up with a response to a query, right?
So this would obviously already capture that, even if it is internal, right? So… From that perspective, I don't see any… Yeah, anything rich had, or something along those lines, no.
It will still give you that information as a user.
**Liudmila Molkova** 35:48 report.
**anksing** 35:49 Oh yeah, please go.
**Liudmila Molkova** 35:52 Wood reported.
In absence of HTTP server span, I would imagine.
And at least for… that's what I imagine Azure.
Foundry would do.
**anksing** 36:10 But, like, have those internal invocations span on the server side just child off.
Whatever trace context is passed in, right?
**Liudmila Molkova** 36:21 Right.
**anksing** 36:28 Or did I get the question right?
It's not on the profile.
**Trask Stalnaker** 36:35 I think the question is, would, you know, Foundry, for example, or some, another, you know, platform that is just modeling Invoke, agent, server.
workflows.
would you… Still capture the protocol-level server span.
Or would you… remove that.
**anksing** 37:03 Okay, so when we say protocol levels, man, do we mean the transport protocol, or… Trask Stalnaker 37:09 The HTTP server. The HTTP server spanned.
Essentially.
**anksing** 37:15 Got it.
I mean, hmm, that'll be interesting.
**Trask Stalnaker** 37:24 I mean, it is an HTTP server, I mean, it is protocol.
Some kind of protocol span, and it does include some potentially interesting.
Things.
Gives you a place to put, like, Client.
**anksing** 37:49 Yeah.
**Trask Stalnaker** 37:50 IP… anksing 37:54 So, I think, like, this is, one of the case that we just looked at is, like, in case of ADK as well, and same is true with, foundry, like, hosted agents as well, where There's a bootstrapping web server that's provided, right, which right now is an HTTP server.
web server, and that has the functionality that, that's just, like, a publicly available web server, and then you can enable HTTP Traces for that are optional if you want.
By default, they're not enabled, at least in Foundry.
So in that case, like, it will be onus on the customer if you have to capture that HTTP service number.
It's not gonna be, like, something that, And we would say, okay, we're gonna always disable, but even if we enable, customer can still disable them.
**Trask Stalnaker** 38:47 I mean, the HTTP server… Needs to be instrumented.
Somehow, whether to… just to propagate context.
Whether it produces a span or not is maybe optional.
**Liudmila Molkova** 39:08 It sounds, to me, that there might be… this is definitely an edge case?
And there are a handful of… Providers that would have it.
And… We don't know how to model them, it could be either or.
What if we start with this case?
And try it out. And if it doesn't play well, if we believe that the server span is necessary.
We can get back to it.
Yeah, I'm good.
**anksing** 39:54 Just wanted to add this information. I was, checking out Agent Core as well, and I think which right now does what you are highlighting, Lumila Protocol plus internal, at this point.
And in Foundry also, like, we want to kind of align with hotel recommendation, rather than, like, going and doing something which is not total recommended. So that's why I think we want to have this discussion, like.
**And I don't know, like, how ADK handles that, or… He said… Trask Stalnaker** 40:26 I think this is interesting, the self-hosted agents… I mean, the… Since we kind of feel like that's gonna be protocol plus internal.
Then aligning, like, there's a lot of benefit to aligning with that, and just having one way.
**Liudmila Molkova** 40:56 Assuming protocol assessed STDIO, Could be server, but yeah.
I feel it's a caveat. It's, it's… Is it even important?
Okay, it could be server, in some edge cases.
**anksing** 41:12 Oh, what could be?
**Trask Stalnaker** 41:13 Oh, I see what you're saying, sure.
**anksing** 41:16 Sorry, what are those edge cases? Just want to understand more.
**Liudmila Molkova** 41:19 The SDIO, the protocol without the protocol.
**anksing** 41:24 Yo, yo.
**Liudmila Molkova** 41:42 Great, so we… Trask Stalnaker 41:43 Yup.
No, go ahead.
**Liudmila Molkova** 41:46 third time… time boxing it, I think, From the prototype's perspective, the only reasonable prototype that's possible to get is this one.
Today, at least.
**anksing** 41:58 Sorry, one last thing I wanted to ask about this. So, for, like, we have 8-way protocol, right? And right now, like, over HTTP and gRPC, you could still do that. So, say if an agent service exposes that you can invoke that same agent through any protocol, right?
I'm assuming we would still have the invoke agent span generated that looks similar in all the cases, or would it be different?
Based on if you expose or involved it through A2A versus, like, HTTP or… Tech we have right now.
Would that matter?
Curious.
**Liudmila Molkova** 42:42 I would imagine it's the same with maybe some… Small differences that are not… Significant.
**anksing** 42:48 Okay, go ahead, okay, awesome.
That's fair, thank you.
**Trask Stalnaker** 42:59 I'm interested in understanding the MCP server relation to this, but I will bump that topic to two weeks from now.
Okay.
**Liudmila Molkova** 43:09 Yeah.
**Trask Stalnaker** 43:09 I'm sure it's a whole other can of worms.
**Liudmila Molkova** 43:14 Yeah.
Cool. Moving on, cubeCon next week. I'll be there.
I'll give a talk about GenAI. I'll highlight all the awesome work people did here in terms of uploading stuff to storage.
annihilations, but I think… What's important is that we should have Gen AI SIG office hours.
And… If you haven't voted on the… Sick, chad.
Please go ahead.
I'm looking for it.
Sorry.
Here we go. Please vote here.
for your… Did I copy the link to the chat or to the post? I hope to the post.
And I'll post it here in the chat, we should pick the time.
There are very few times that are, still available, and… If you're the CubeCon, I would love to catch up.
Okay, and done.
The last topic is Surrey, but I think you had to drop.
**Surya Teja** 44:52 I'm here, I'm here, sorry. I was… fortunately, I was here. I'm here. So, this, is a small PR, for extracting the… Span attributes from, responses API of OpenAI.
The reason for throwing this PR over here is because I'm trying to create some strong typing in our repository so that we can reduce our reliance on any or objects in our codebase and, make it… more readable.
So… with that intention, I tried using Pydantic, that is, used both by Anthropic and, OpenAI, so that we can do some validations, as well as we can extract out the attributes. Folks who are well-versed with Python can take a look at it and let me know if I can refactor or refine this a little bit more to make it better.
So that's the small ask.
Thank you.
**Liudmila Molkova** 45:56 Thanks a lot for doing this.
**Aaron Abbott** 45:58 I think I had the same question as Ricardo on this one, like, Most of these providers use Pydantic already. I was wondering, is OpenAI already using it?
**like, the… Surya Teja** 46:12 Yes, sir.
**Aaron Abbott** 46:13 Yeah, yeah, go ahead.
**Surya Teja** 46:14 ESRN, it's using Pyreantic. I'm… It's, it's more or less, It's just for extracting out the attributes and creating some used classes that contain the attributes according to their grouping.
**Aaron Abbott** 46:32 Right.
Like, I guess the question is, wherever we do the monkey patching, do we have the Pydentic objects directly? Or, like, why… why are we starting with the straight dictionaries instead of having the identic objects? Is it… is it a limitation with the… with OpenAI.
**Surya Teja** 46:52 I don't think it's not, okay, you're asking why I created the classes, right?
**Aaron Abbott** 46:58 Yeah, yeah, or like, why… Because, because this is, you know.
I don't think the overhead's a huge deal, but, like, I'm more familiar with Google Gen AI, for example, and that one, the user generally passes the Bydantic models directly, so we can kind of just rely on them being there.
**Surya Teja** 47:17 Yeah, so the Bytronic models are directly available in the ARGs that are supplied through our monkey patching.
the models that I created are for grouping the attributes according to their, class, like, say, response attributes or request attributes and stuff like that, so that I can reuse them inside the extractors and, Do the logical mapping.
To our, span attributes.
That is the intention behind creating these models.
**Aaron Abbott** 47:50 Okay. I'll take a look. I think I'd understand better if I just review.
**Surya Teja** 47:55 Good, thank you.
Yeah, but, the question is around why I created the classes right, so that I can write down more, better answer… coherent answer over there.
in the GitHub… Pull requests, so that it can structure down my thinking.
**Aaron Abbott** 48:11 Yep.
**Surya Teja** 48:13 Cool. Thank you.
I'll write down something over there.
**Liudmila Molkova** 48:19 Thank you.
Yeah, Aaron, you were… just added a topic?
**Aaron Abbott** 48:31 Yeah, sorry, sorry about that. I was just going to say that… so this is Matt Kumar, this is, your PR on the guardrail stuff.
I just wanted to share that I, you know, I shared this with the Model Armor team, at Google, so they're… they're interested. I'm still going through some of their feedback and, kind of sharing it here, and I think You know, they're acting as the subject matter experts, kind of, for us, so that we can… you know, make a better decision here. I'd like to get them to either come here, or maybe we could, chat offline or something, but there was a lot of… there's a lot more feedback. I added a couple comments here so far.
I hope… I think one of them is Bike Shetty, which I apologize about, I think it's a good point, though, like, Because I think Guardrail and Guardian are kind of used interchangeably in this doc so far.
it might just be also the YAML things, it could be just, like, a refactor issue, but, Besides that, I think the base set of attributes are pretty applicable.
**nagkumar** 49:38 Awesome. Thank you so much. I will, I'm also working with, another working group for security. One of the representatives showed up on… yesterday on the agent's call, so happy to sync over Slack, and then, address all these things.
**Aaron Abbott** 49:57 Okay.
Cool, and I think, I guess one high-level question I had, and sorry if it's already been answered, but… Does this… like, obviously there's a lot of SaaS or cloud providers that do the guardrails thing.
Are we also targeting some open source offerings? Because I think Some of the attributes.
don't make a lot of sense for SaaS, but we should, of course, support open source, too.
**nagkumar** 50:21 Yeah, for sure, we can… we can add some.
**Aaron Abbott** 50:29 Okay, cool, thank you. You still sync offline.
**Liudmila Molkova** 50:39 Awesome, thank you.
It seems… oh, Keith! Pending PRs.
**Keith Decker** 50:44 Yeah, I just wanted to, note that there's a few PRs out there for GenAI utils for the different types, like tool calls, embeddings, and agents. Just would like to get some more eyes on them, and yeah, just raise worries.
For him. I know a lot of them have conversations that are going through him, and… Getting resolved, just… Bring it to attention.
**Aaron Abbott** 51:07 Okay. I think I looked at some of these, hopefully. Keith, if there's… if there's any that are just waiting for a merge, feel free to just ping me on Slack.
**Keith Decker** 51:17 Sounds good.
Yeah, I don't think any of them are ready for merge. I think we still need, multiple approvers on some of them.
But yeah, we're making a push to try and get, any of the types from SEMCOMs into the Gen AI Utils.
**Recently, so… Liudmila Molkova** 51:34 Nice.
I'll… I'll probably bring it up on the Thursday call, again, that we… we want… we probably need to.
start releasing… releasing things together. Otherwise, we would not be able to… like, nobody will be able to find the… list of compatible versions, for different AI instrumentations.
**Keith Decker** 52:01 Yeah, they're starting to get intertwined, so it makes sense to kind of… Release them all together.
**Liudmila Molkova** 52:12 Okay.
I will take a look, and the TSPRs. Anything else?
We have 8 minutes left.
Okay, so then… Thanks for coming. And, oh, okay, we… I think Ivan will be here next week.
I think, Aaron, you're also coming to KubeCon and you won't be here.
If you're one of folks, you… Oh, Jamie, you will be at KubeCon! Nice!
Looking forward.
to it, I don't know if you folks want to meet, the meeting is on the calendar. No, you don't.
**Would anybody want to… neil yashinsky** 53:05 It's a good one to pass. I mean, I'm always up for meeting on this topic with these fun people, but it seems like if ever there was a time to pass, this would be it.
CBD? Yeah, I feel like that's a balanced choice.
Or maybe you could even say, because people… can people remotely connect on that office hours that you were mentioning?
Or is that not, virtually possible? It's only… it's only in the meet space?
**Liudmila Molkova** 53:35 It's intentionally not possible, but it's also very hectic there, so… neil yashinsky 53:40 Yeah, yeah.
**Liudmila Molkova** 53:40 It would be hard, even if it was possible, technically.
**neil yashinsky** 53:42 hmm, hmm.
Maybe, maybe next year we'll, or next one we can strive for a virtual one of sorts for people who can't make it.
**Liudmila Molkova** 53:50 This is the virtual office hours, you know.
**neil yashinsky** 53:53 Well, well, like, touche, then.
**Liudmila Molkova** 53:58 Awesome. Dan, thank you all.
See you in two weeks, enjoy some quiet time.
make some PR reviews.
**neil yashinsky** 54:07 Thanks, Lumil. Thanks, everyone.
**Trask Stalnaker** 54:08 Right.
**Liudmila Molkova** 54:09 Yeah.
**lechen** 54:10 Who knows?
