SIG: LLM Semantic Convention WG
Date: 2025-11-18
Duration: 46 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 01:04 Hi, Alex.
Okay, while we're waiting for people to join, let me do the triage.
I have some new issues here.
Oh, by the way… There was some recent development on… This one, let me update the agenda.
Normally.
Okay, coming back to the triage… I've added this to the agenda, let's see if we can make progress.
agent ID or the client ID for the iServer metric conventions.
Okay, I think it's not a new issue. I think we triaged it, and it needs info, so I'm going to… Remove the status… Oh… Let's take a look at the tool orchestration.
Okay, there was some discussion… tool orchestration… Okay, so it sounds like… Pao is proposing to add a few attributes.
To describe tool configuration.
And it's generic enough.
And it sounds straightforward.
So I'm going to… Put it to Tudoo.
And it's accepted, ready with SEC, wonderful.
Okay, let's take a look at a couple more issues.
Function 2, there's no other guidance for just some representation of other tool types.
So it's to cover… just functions, I think we have a pull request.
Cool definition for the functions.
**Aaron Abbott** 05:26 I think maybe we had one for the, like, model input and output schemas?
**Liudmila Molkova** 05:33 No, we…
**Aaron Abbott** 05:35 Definitely have one.
**Liudmila Molkova** 05:40 Here we go.
But it's only for functions, but not for… Okay, so it sounds like it's… Accepted, that sounds reasonable, and we should go to to-do.
Okay, one more.
This is from Python, and I think there is a pull request.
And, I approved it, it's straightforward, if you folks can take a look at this.
Essentially, on our board.
It's in… Oh, grish.
**Surya Teja** 06:46 I opened up a small, issue in Python repository for adding instrumentation around Anthropic SDK.
So, I have a prototype ready with me, so if, it is fine with you guys, I can raise a PR, but I… the reason why I'm asking here is I haven't seen any activity around Anthrofic or anything, so just wanted to check if you need any permissions or anything regarding that.
And that… that issue is there in the meeting notes, and I did not… I was not able to link it in our issue board or anything. The last one.
**Liudmila Molkova** 07:21 Oh, okay.
Thanks.
aaron or somebody who works on Python, could you comment on the process we follow there?
**Aaron Abbott** 07:33 Yeah, I think, I think we discussed in the last week's Python Sig, Do you mean for adding it to the board, or just in general for the new insurance?
**Surya Teja** 07:45 can I go ahead and add it, or, is there any, representation needed from LLM team or anything? Like, I was just seeing if approval is needed, or I can just, open a PR, so that was my ask.
**Aaron Abbott** 08:01 Yeah, no, I mean, I think it's great that you brought it first, if we could just do it, like, in small parts, I'll take.
**Surya Teja** 08:07 Yeah.
**Aaron Abbott** 08:07 And if we could, you know, agree on the scope, I think, it'd be good. It wasn't super clear to me if this was, like, an agent… remote agent framework thing, kind of like the OpenAI models, sorry, OpenAI agents, or if it was, like, just instrumenting the LLM inference calls and stuff.
**Surya Teja** 08:23 Yeah, it was… so, it is instrumenting the LLM inference calls. There is an agent framework also from Claude, but for keeping the scope limited, I haven't included that in this issue. I'm planning to include that in the subsequent issue once this is completed.
**Aaron Abbott** 08:40 Okay, yeah, that's great. And, I think I mentioned last week, but, like, if you can opt into the typing off the bat, it's just not the default right now, but.
**Surya Teja** 08:49 Huh?
**Aaron Abbott** 08:49 Makes it much easier to review the code and maintain it, so…
**Surya Teja** 08:53 Yeah, sure. I'll try to, scope it in a way that, I'm going to send small chunks for PR.
**Aaron Abbott** 09:00 Okay.
**Surya Teja** 09:01 Yeah, great. So, thanks, thanks, guys.
**Liudmila Molkova** 09:04 Wonderful. Thank you. And, I would imagine we need some component ownership there, right? So… It's not just the contribution, but we would expect you to be on point if things go wrong, if somebody sends a pull request, and we would ask you to review.
Would it work for you?
**Surya Teja** 09:27 Yeah, that works for me, yeah, sure.
**Liudmila Molkova** 09:30 Yeah, and checking Aaron, do we need… is it enough to have just one component owner, or do we need more than one?
**Aaron Abbott** 09:40 I mean… I don't know if we have a hard and fast policy on this, but of course, more would be good if you have any co-workers who are willing to also help out here and put their name on.
**Surya Teja** 09:52 Yeah, sure. I don't work for Anthrophic, so… so that… let me be clear on that, but I can, add a starting discussion in the Anthrophic repository and see if they are also… they also want to be part of this.
So that we can get a direct representation from the cloud team also.
**Aaron Abbott** 10:11 Yeah, I mean, that would definitely be appreciated. I won't, Yeah, if… if that would… if that worked out, that would be amazing as well. Yeah. But if you have, like, I don't know, anybody, Assuming you're using this at work, If you have any coworkers that would also be willing to…
**Surya Teja** 10:27 Yeah, so, it's just me. A lot of others are busy with other things, so I can't ask for my work, but I can ask if from the anthropic community, because they have a substantial amount of users, and they said, someone can.
**Aaron Abbott** 10:43 Gotcha, no worries, yep. I think… I think having, more than one would be… would be ideal. I'll double-check with the other maintainers, though.
**Surya Teja** 10:51 Yeah, quick. Thanks, Ed.
**Liudmila Molkova** 10:53 Is it… is anyone here would be interested to collaborate and be the… another component owner?
Okay.
If you change your mind, come back, please.
**Surya Teja** 11:09 Thanks, guys.
**Liudmila Molkova** 11:11 Yeah, thank you.
Okay, so we are done with our… Trash block.
So, if anybody wants to introduce themselves, this is your chance to tell what brings you here, how can we help you, what are you interested in? If not, that's fine.
Don't do something you don't want to.
Okay.
So if you want to, I don't know, add your name to the agenda later and talk about your projects, or you have any specific topic in mind, go ahead, this is public document.
Okay, moving on to the main agenda, let me close things… I've added a couple of topics, Here, I have heard that we are… we don't get a lot of responses from existing component owners for the pull requests.
And maybe our component owners are not up-to-date for the other components.
So, I, thing.
We should probably… updated, or… there are people who have been quiet for a while, so I don't know, maybe I'll send a PR to update this, and we can discuss if people are interested or should be on or off this list.
So, Aaron, you are more familiar with the situation, can you help me understand it better?
**Aaron Abbott** 13:02 Yeah, I mean, I think we're just… so, for example, we sent, Ricardo sent this PR for OpenAI, and it's just been a little bit difficult to get in touch with the original contributors and some of the code owners.
I don't think this is a unique problem to LMSig, but, like, so far in Python Contrib, we haven't taken any sort of approach like the collector's done, where they will remove components that are like, unmaintained.
But, yeah, I don't know, like, in terms of other SIGs, what they do, but it's definitely an issue.
**Liudmila Molkova** 13:37 Okay, so, I think we can try to solve it, because we have an active seek, and we have plenty of people who were at least initially interested in, maintaining stuff.
So, we can, I don't know, solve it the process-wise, so we are not going to discuss any new features until we, address comments, or, like, have the PRs reviewed. We, I think we can also What we can also do is… Okay, there are people who want to contribute to Gen AI, and they don't know how.
I think the best contribution you could make is to review pull requests, you, like, if you don't have comments, you can at least, I don't know, check out the branch, run it, and see what it produces, the results, or just review the compliance with semantic conventions, so, like, don't be afraid to review pull requests. It is really the best contribution you could make.
And I've seen Ricardo, been doing this, so when somebody asks for the PR review, he asks them to review others' PRs first and exchange. I think this is super useful, and maybe, I'll try to prioritize during these meetings going forward that we pay attention. But also, I'll, I'll probably start the thread, and maybe we will discuss it in the PR, and who should be in this list specifically for the Oh, this is general for everything, right? Yeah.
For this one.
Okay, I think we discussed this… I also added a topic on… MCP?
So, I think there are a few discussions, I'd like to have here.
The first one… is about… The feedback we've got from and, from MCP people, the… Okay, so… MCP recommends using some prefix for the keys in meta. It's optional.
it's kinda weird to put them in OpenTelemetry, because it's not up in telemetry, it's W3C.
W3c is also kind of weird. Would we put everything defined in W3C in this list? How is it helpful?
So, I'm advocating for just doing plain and straight what we've done so far. We just use these properties the same way we use them in HTTP.
And… I talked thus… Sergey Kongelov, who is the, One of the authors of the… WS3C standards, both baggage and trace context.
And he seems supportive that we don't really need a prefix, and W3C would be, Weird prefix to give.
So I'm… my intention is to just resolve this discussion and proceed with what we… F.
And I'm curious if anybody in this group has a preference.
**Aaron Abbott** 17:55 I had one question on this, so if the user sets a different global propagator that's not W3C, or in addition to W3C, would it just put them into the global namespace Like, would instrumentations be expected to just put it in the global namespace with whatever setter they have?
**Liudmila Molkova** 18:13 Yeah, I, I think so. Okay. It depends on the… go ahead.
**Aaron Abbott** 18:18 Yeah, like, so if it was, like, B3 or something like that, like, if the original goal was to avoid key collisions.
Then you're kind of at the whim of the propagator, right?
**Liudmila Molkova** 18:28 Right, yeah.
**Aaron Abbott** 18:32 Yeah, I can't speak to, like, you know, MCP if that's an issue or not, but I definitely see the value in having the standard keys directly in Meta.
We could.
**Liudmila Molkova** 18:46 Yeah, from MCP, what they're saying, they would be… Happy to reserve something for us.
But what they're saying, that it's an optional prefix.
So we are compliant, and it's just there is nothing.
You're reserved for us.
**Aaron Abbott** 19:08 Yep.
Yeah, I mean, I… I'm not gonna… I think for W3C, this, It'd be great to have them flat without a prefix, I agree.
**Liudmila Molkova** 19:26 Cool.
Thanks.
So, I will leave a comment and… Oh, sorry, Alex, I didn't see your comment, Table of transport-related attributes should be in this pack.
You mentioned, like, popping up a comment just above this one, yeah.
Okay.
Okay, I will… I will do this.
So, based on the Aaron's comments, I've done something I want to show everyone.
So, the MCP tool name.
It's now not MCP tool name, but it's the same as GenAI tool name.
I added that tribute, thinking that maybe MCP could be wider than GenAI, but I think either way, it's… It's probably… it probably makes more sense to have one attribute than two with the same meaning, essentially.
Related to this, the prompt name is now also in GenAI Prompts, or inherently GenAI.
And, there is something in OpenAI that allows you to reuse prompts, so you can create the prompt and then use it by ID.
The, the prompt template.
So, I also changed the MCP prompt name to GenA prompt name.
And I… just… If you're… if you're interested, please leave your thoughts.
Okay, there are two, I think, wider discussions I want to have.
So the params.
Maybe the alleged stopping.
Wow.
Where are your comments?
**Aaron Abbott** 22:02 I don't know.
**Liudmila Molkova** 22:07 There we go.
**Aaron Abbott** 22:08 I was having issues with the new GitHub UI, as well, with this.
**Liudmila Molkova** 22:12 Yeah.
Anyway, I think I remember. So, the interesting point is, let's say we have… This. Bing.
How do we capture it? We can capture all params as one object, right?
Or we can capture individual properties.
So in the current proposal, we capture individual properties. You can enable, let's say, params.location.
And then it would capture the location.
Versus, if we think about the… the… Prompts and completions, we capture them as a single structured object.
I… My opinion here is that in prompts and completion, it's all or nothing. You want everything, or… Nothing.
and here… this might be more like, okay, I care about a few parameters, but I don't want to capture all of them, especially, like, meta. There could be some, I don't know, the progress, talking, or whatever they have for long-running operations.
It's not a super strong opinion, though, and I'm curious if anybody has any thoughts.
**Aaron Abbott** 23:52 Yeah, I mean, I… I raised the point mostly because I was just… I noticed it being inconsistent.
I guess I don't have a lot of experience with MCP, so I'm not sure how people use it, and… If… if it makes sense to, like, you know, capture sub… subsections of the params, like, I know we do use this for HTTP headers, that seems like the most prominent use of this template thing in semantic conventions.
And in that case, like, the headers are generally completely distinct. It makes a lot of sense there, but, my understanding of MCP is that the params would typically be, like, a single specific type, depending on the method kind. Like, it's pretty much, like a tagged union kind of thing.
Not to say there's not, like, PII that might be separate, but… I was just a little surprised by the initial design. I don't… I don't have, like, a strong objection, But yeah.
**Alex Hall** 24:49 So, Lyudmila, is Meta getting special treatment here?
I think it might… Go on.
**Liudmila Molkova** 25:02 It might have, because for Meta, we are essentially Assuming that somebody wants to capture things under it.
Like… like, it's the… almost as JSON path.
**Alex Hall** 25:22 So, we, like, flattened one level deeper.
Like, we're not just putting meta as a complex thing.
If mcp.dev slash baz is complex, what happens?
**Liudmila Molkova** 25:40 it would still be a complex thing. It's a template of any.
**Alex Hall** 25:47 I just think this, this, this… Difference with meta is confusing and could easily lead to mistakes.
**Liudmila Molkova** 25:56 Can you elaborate?
**Alex Hall** 26:00 You haven't… you're not saying, That the attribute is param.underscore meta with the value a complex dictionary.
View.
So meta and complex are getting different shapes of attributes here, and… Someone may not expect that, and… Either in instrumentation, querying. Messed that up.
**Liudmila Molkova** 26:31 Let's discuss how we should capture the whole thing, and maybe it will solve the… the concern for Meta.
So, assume… assuming we capture it as a complex object.
Like, like this.
Would it twerk?
Anyway.
So let's say we capture the whole thing.
then, my assumption that people would… would not want to capture Capture it all. People would want to capture some things and exclude others.
We're… Maybe the answer is different for params versus meta.
**Alex Hall** 27:53 Is the idea that there's, like, SDK configuration to… You know, do things on the level of attribute names.
Mike.
You know, filter out these attributes, or… I guess not just the SDK, maybe the collector or something. The point is the idea that it's easier to work with top-level attribute names, as opposed to, like, a JSON path.
**Liudmila Molkova** 28:21 It is, definitely. So, like, if… If you want to use one of those parameters, In your query.
It's probably much more efficient and easy.
To have a top-level one.
I guess we are… We have some prior art, so I… I think, how can we make progress? We don't know how people will use it, and this is the key question.
Right? If we knew, it would be… we could make a decision. We're… Could say, okay.
Let's postpone this question until we know.
Which might never happen. The other… path we can take. Okay, we have a prior art.
And actually, the prior art is for the two calls.
Oh, sorry, I didn't, I didn't… the link… Hello.
So… arguments. So this is how we capture Two arguments, and it's a type of any, so it's all or nothing.
So, if we… Follow the same direction.
where should… Capture it all at once.
And we can say that instrumentations may, I don't know, allow to Opt out of individual properties, or opt in into individual properties.
**Aaron Abbott** 31:11 And I think the subtle difference is that, like, MCP is a protocol, right? Like, we… we have schemas for every kind of MCP request and response type that you could imagine, right? Like, This is pretty much a hard-coded thing.
Or, sorry, the… the tool… I'm having trouble with the zoom.
Sorry, the tools, like, they're completely user-defined versus an MCP, we might know something about the schema beforehand.
Yeah.
**Liudmila Molkova** 31:49 I might know… yeah, I might know something, but…
**Aaron Abbott** 31:53 this params.
**Liudmila Molkova** 31:56 So, okay, so for example, in Meta, there is a progress token. We should never report, like.
Should we never… I don't know, maybe we should never report it.
Good question.
So this is Arbiter, right?
**Aaron Abbott** 32:15 But there's, like, specializations in this file, right? So, like, That's my understanding. Maybe I should… Yeah, so, like, there's, like, ping requests where you know method is ping.
There's progress notification requests where you know.
**Alex Hall** 32:30 We're not going to capture all of that, are we?
**Aaron Abbott** 32:32 Well, isn't that what the PR is proposing?
**Liudmila Molkova** 32:37 PR is proposing optimum.
**Alex Hall** 32:39 We're not gonna, like, specify all of the different types of params in the spec, are we?
**Aaron Abbott** 32:46 I think we're talking about two different things, No, I'm not… I'm not saying that, necessarily.
**Liudmila Molkova** 32:58 So what PR is proposing is to capture something… oh, so actually we have resource… You're right. So this guy becomes the top-level attribute.
Because it's important, because it's meaningful.
So those that are defined, Like, you're rice.
Or, like, I would imagine resource description if it becomes… it's not the parameters, right?
Let's take a look at the ping request. There is nothing here.
token request.
**Aaron Abbott** 33:44 Yeah. I mean, actually, to Alex, to your point, like, you could… I'm not going to advocate one way or the other, because I think it would be pretty clunky, but you could imagine one different spend type for each specialization of requests, like in OTEL, right?
It's weird.
We do know all the specifics.
**Liudmila Molkova** 34:12 So we… the specialization makes sense, and we already do this. The tool called name, right? It becomes the 00plar property.
And then arguments being the… Single.
property makes sense as a top level, right? They are in the… they are orthogonal.
Like, the params are orthogonal to each other.
**Alex Hall** 34:39 Shit.
Should this also be using toolcall.arguments?
Or, like, the actual top-level JAI.
**Aaron Abbott** 34:48 Right.
**Alex Hall** 34:49 Just like you've done with a name.
**Liudmila Molkova** 34:55 Okay.
We're getting somewhere.
**Alex Hall** 35:01 taking it further. Should it just be a tool called Span?
**Liudmila Molkova** 35:12 Wow.
Okay.
So, let me… Get back to there.
whiteboard on this. I'll just capture a few points under this discussion, and I'll experiment.
For the sake of… I don't know, it's been more than half a year.
**Aaron Abbott** 35:35 Can we…
**Liudmila Molkova** 35:37 Can I follow up?
Remove this for now and fill up.
**Aaron Abbott** 35:43 I mean, that's totally fine with me, I don't think it would, like… I don't think it would scale to have a semantic convention for every single thing in MCP.
Or, like, we could obviously automate it, but… Yeah, maybe we can punt this anyway.
So just to be clear, like, we would remove this section and then, you know, potentially wait for somebody to be like, hey, the MCP conventions don't capture the Request tool description, and then… We would follow up at that point.
**Liudmila Molkova** 36:26 I can follow up earlier, it's just, I can follow up immediately after this pull request.
It just feels that, it would be easier if we agree on something, and then incrementally add… this.
**Aaron Abbott** 36:45 Yeah, that sounds good to me.
Alex, is that good with you?
**Alex Hall** 36:49 Yeah, happy to do this later.
**Aaron Abbott** 36:53 I think that resolves the second topic too, right?
**Liudmila Molkova** 36:59 Yes, it resolves the second topic as well.
Okay, and I am going to… This one, and… Okay, have something to think about, and we can make progress on this PR.
a lot.
Hold on.
Okay, so, how much time do we have? Let's put it at the end… Taya? Is it how I should spell your name, or Teja?
I think we already covered this topic, I just wanted to check, it seems we did.
Keith!
Let's talk about Gen AI PRs.
**Keith Decker** 38:58 Okay, so this one, we looked at briefly on… what was it? Wednesday, Thursday?
Oh, it looks like I'm out of date again.
But, I just need another review.
Besides the Miller for this one.
**Aaron Abbott** 39:15 Why don't you have a green checkmark, Milla?
**Liudmila Molkova** 39:18 I don't know.
Good question.
**Aaron Abbott** 39:21 We can add you to the approvers, although I thought you had it… had it from a different group.
**Liudmila Molkova** 39:27 I used to have the ultimate powers being a TC member, but we removed Ultimate Powers from TC members, so I don't have… Any powers anymore.
**Aaron Abbott** 39:37 Okay, well, I'll propose you.
**Liudmila Molkova** 39:40 Thank you, I appreciate it.
so, I think here we, we, on the…
**Alex Hall** 39:49 just the deals we have…
**Liudmila Molkova** 39:52 All the… we have the approval.
**Keith Decker** 39:56 Right, I went through and resolved all the other conversations. Looks like I need to update main again. There was an update since yesterday, so I'll do that real quick.
**Liudmila Molkova** 40:06 But other than that, it seems to be good to go.
Any… anything worth discussing? There was some comment from Aaron.
But I guess it's… Undressed.
**Aaron Abbott** 40:24 Yeah, I thought… I thought Dylan approved this one, too.
**Liudmila Molkova** 40:29 It is.
**Aaron Abbott** 40:30 Oh, okay.
**Keith Decker** 40:32 Yeah, we had just Dylan until later last week. I had just had to resolve the conversation so that it could… Go to Merge, so it looks like I just need to merge Mage back… er, main back into it.
**Aaron Abbott** 40:43 Okay. Yeah, ping me when you do, and I can, merge the PR.
**Keith Decker** 40:46 Okay, we'll take care of that.
**Aaron Abbott** 40:49 Cool.
**Liudmila Molkova** 41:00 So for metrics, So, one thing I'm thinking about, and I'm struggling to find time, so I presented something at the KubeCon. We can actually validate telemetry against the definition.
And it's a question of… updating the CICD pipelines, and there are some, rough edges around the tooling, but it's totally possible to just run integration tests. It can be exported to OTOP, and then the Two, Weaver.
as a life check mode that it will validate it against the definition. And I'm thinking that reviewing the spool requests can become much easier. So, if you know it follows semantic conventions, then it's the matter of just reviewing the Python code.
to… or, I don't know, from the performance, cleanliness, and so on perspective, and becomes much less consuming and difficult.
So, I… I've… I want to find time to do this, And I'll try, if anybody is interested to participate, let me know, and it will… Will be tremendously helpful.
**Aaron Abbott** 42:24 Yeah, that's nice.
**Keith Decker** 42:25 dude.
**Aaron Abbott** 42:25 Ding.
**Keith Decker** 42:27 Go ahead. Okay. I did say I would give Weaver a try on that, but we didn't want to block this one, right?
**Liudmila Molkova** 42:33 Absolutely.
**Keith Decker** 42:34 So I do owe you an attempt on that.
**Aaron Abbott** 42:39 We know the… does it work for just metrics? Does it work for, other signals, too.
**Liudmila Molkova** 42:45 It works for metrics. It… Can… work for logs, so I, I… it needs some… some work on Riverside, which I'm happy to do to make it work for logs. For spans, it's kind of weird, because there is nothing on the span itself to tell which span it should be, like, how to map the definition to the… Span itself.
**Aaron Abbott** 43:10 Yeah, that… It's not just Weaver that impacts me, too, sometimes.
**Liudmila Molkova** 43:16 Right, okay.
Okay, okay, there is a big discussion on how we should even approach this.
from the spec perspective, we can still do something. We can say, okay, this attribute is unknown. Like, we don't know, it's attribute not in the semantic conventions. Or maybe we can have some other… steps. But for metrics or logs, it can work like a charm.
**Aaron Abbott** 43:47 Okay. Great.
**Liudmila Molkova** 43:52 Okay, so then, let's, see if we can find other reviewers for the metrics pure.
And lever some long-term, direction we hope we can move into.
Okay, so the last topic we have on the agenda is something I just wanted to see if there is interest. So we have… Unified problem of workflows.
there are multiple different things that do workflows. I don't know, the jobs execution… jobs runtimes, there is CICD group who is looking into unified workflow conventions.
I am… Adding it here, in case there is an appetite to work with them.
And try to define something. We don't really have any… Agent folks here, do we?
Okay, I'll… I'll post in the channel and check if… if… They would be interested in finding the common ground between GenAI and CICD.
Okay.
Do we have anything else to discuss?
Cool! It's the first time we finish early.
Not sure if it's a bad sign or a good sign.
**Aaron Abbott** 45:46 Okay.
Well, thank you.
**Liudmila Molkova** 45:50 Thank you all. Have a good day.
