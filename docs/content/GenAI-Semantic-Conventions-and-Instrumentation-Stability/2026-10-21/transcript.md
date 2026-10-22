SIG: GenAI Semantic Conventions and Instrumentation Stability
Date: 2026-10-21
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

Max Ind (Google LLC) 00:01:38 Hello.
Neil Yashinsky 00:01:50 Oh, no, I didn't know, I didn't know, I didn't know, I didn't know.
Neil (he / him / his) 00:02:05 Well, that wasn't intentional, sorry about that. Is it just… is it just, I think the song goes, the two of us,
Max Ind (Google LLC) 00:02:11 Oh, interesting.
Neil (he / him / his) 00:02:13 Fraternity or whatever, how are you today?
Max Ind (Google LLC) 00:02:15 That's true. I'm doing great, thanks for asking. Yeah, how are you? Oh, yeah, yeah.
Mikoei… Mikoi came in, and now we can't… we can't continue the song, unfortunately.
Neil (he / him / his) 00:02:26 Yeah, no, that's alright, because I came in like a wrecking ball, I guess.
Max Ind (Google LLC) 00:02:29 Oh, wow.
What's…
Neil (he / him / his) 00:02:33 Trying to break down any walls. Hi,
Max Ind (Google LLC) 00:02:35 I'm gonna.
Neil (he / him / his) 00:02:36 Probably not do right, but Anit Kolaj, maybe? How are you today?
Mikolaj Knap (Google LLC) 00:02:40 You're good? Close enough? How about you?
Neil (he / him / his) 00:02:43 Very good, thanks. Yeah, I, I joined the meeting twice right before you did, and I'm glad I didn't blow out any of your sensitive speakers around, Max, because I, like, you know, double joined, yeah, the… I don't use, what is this?
Microsoft Teams? I think I'm on a browser, and I don't use this a lot, so, yeah.
Max Ind (Google LLC) 00:03:02 Right, Dan?
Excuse me.
Maybe have you connected through, like, maybe Microsoft Teams now allows you to?
Neil (he / him / his) 00:03:08 No, it's a Zoom browser, that's what it is. It's the Zoom browser, that's why I was like, it's really, the UI threw me for a loop for a moment.
Max Ind (Google LLC) 00:03:17 That's understandable, yeah.
Neil (he / him / his) 00:03:18 Hello, everyone.
Max Ind (Google LLC) 00:03:19 Hello, everyone, yeah.
Liudmila Molkova 00:03:21 Whoa.
Okay… Let's see what we have here.
As usual, we have a bunch of pull requests to review.
Let's quickly go through them and see if anything actionable, anything needs additional discussion.
So… Trask is here. I think this one is good to go. Should we just merge it?
Neil (he / him / his) 00:04:06 I think so.
Liudmila Molkova 00:04:07 Oh.
Neil (he / him / his) 00:04:08 Oh.
No?
Liudmila Molkova 00:04:11 Trask, we talked about it on Monday.
And… Turns out, we do not have… Error type.
on those friends.
Neil (he / him / his) 00:04:24 Oh, I think that Aaron did… was that Monday? Yeah.
Liudmila Molkova 00:04:29 But the description says it includes failed operations.
So should we put… Error type, and maybe it's orthogonal.
to this pull request.
Aaron Abbott (Google LLC) 00:04:48 I was assuming it would be, another… Full request, but…
Liudmila Molkova 00:05:01 Okay.
Neil (he / him / his) 00:05:03 and I guess I'll chalk this up to a quote-unquote dumb question, but what defines orthogonal? If I'm hearing you right, and Aaron, correct me if I'm wrong, like, that would be just a separate… it's a separate addition that we don't need to include it in order for this PR to do what it's intended to do.
We can add it separately, and it won't be incomplete without it. Is that what you meant by orthogonal, or what have you?
Okay, see that one.
Aaron Abbott (Google LLC) 00:05:31 I think so, yeah. Like, like, this PR is about, the zeros and the errors, or… Are… can happen with zeros or without zeros.
Neil (he / him / his) 00:05:44 Excellent, very well said, thank you.
Liudmila Molkova 00:06:04 Okay.
So then, if we all agree that this doesn't change the Z how we report positive values.
Should we merge?
Neil (he / him / his) 00:06:21 I have a merge.
Aaron Abbott (Google LLC) 00:06:27 Do we… do we need approval from… Someone else, sir, we're good.
Liudmila Molkova 00:06:31 are good.
Aaron Abbott (Google LLC) 00:06:33 Okay.
Liudmila Molkova 00:06:55 Okay…
Neil (he / him / his) 00:06:56 Buzzah.
Liudmila Molkova 00:07:00 Next one is config.
From Dylan, and I approved. I think you took away the decorative configuration part from everything.
Dylan Russell 00:07:10 Yes.
Liudmila Molkova 00:07:14 Yeah.
Dylan Russell 00:07:15 Yeah.
Got rid of that.
Liudmila Molkova 00:07:17 Huh.
I left under the assumption that this would remain.
Development for the time being.
Dylan Russell 00:07:29 Yeah.
I think that's fine.
Liudmila Molkova 00:07:34 Crevy.
Anything we need to discuss?
To be resolved.
Thing seems to be resolved, and we just need a second approver.
Trask Stalnaker (Microsoft Corporation) 00:07:53 I'll look at that.
So, it's… event only… capture content… Event only, and… The default is not to capture content.
Dylan Russell 00:08:15 I forget if we renamed this the environment variable.
Trask Stalnaker (Microsoft Corporation) 00:08:19 Oh, I see the table. Oh, yeah, the table is perfect. Okay, yeah.
Dylan Russell 00:08:22 Yeah.
Trask Stalnaker (Microsoft Corporation) 00:08:23 Hey, I'm good, I will… Review that.
Liudmila Molkova 00:08:44 Okay… And then… Yeah, go ahead.
Neil (he / him / his) 00:08:50 Oh, sorry, I almost forgot I had my hand up. No, I was just gonna ask, if we have, if we have a moment, Ludmil, you said that, a dictionary, configuration or something was… was taken out of the first version, is that right? You said…
Liudmila Molkova 00:09:03 clarity of configuration.
Neil (he / him / his) 00:09:04 clarity. Do you mind just, like, educating me just for a moment on, like, why… why that was important from that decision? And, like, people listening at home?
Liudmila Molkova 00:09:13 So the declarative configuration is experimental and so on.
And we should define it, but it's definitely not in scope for stability, and ask was to separate And let declarative configuration tickets… Timeline, whatever it takes, because we're not blocked on this by any means.
Neil (he / him / his) 00:09:36 Yeah. In other words, similar to what we kind of ruled in a different fashion, for the last PR. Like, oh, yes, good point, but we're pushing PRs, and we're not… not pushing them because of things that could or should also be…
Liudmila Molkova 00:09:52 No, I think it's different. For the previous PR, it was about positive token usage.
And having error type on this metric would be blocking for stability.
So we would address it, it's just a separate concern. We would need to address… this problem existed even without the… us clarifying positive.
Talking count.
Neil (he / him / his) 00:10:15 You gave me even more than I asked for, but yes, no, thank you, no, and I appreciate the further qualification above the clarification, because of how they're both the same and different. No, super helpful.
Liudmila Molkova 00:10:27 Awesome.
Yeah. Okay, so the next one really quick is about parts.
I almost approved it, but Aaron, my AI found some minor… Thanks.
Aaron Abbott (Google LLC) 00:10:45 Okay, no problem.
Liudmila Molkova 00:10:47 Yeah, do we need to chat about…
Neil (he / him / his) 00:10:51 Is it the generic types?
Liudmila Molkova 00:10:54 Yes.
Neil (he / him / his) 00:10:55 Yeah, I saw that too, and I was trying to find it, I just looked for the Slack messages. I… you wanna… go ahead and say hello, Neil.
Liudmila Molkova 00:11:01 Yo!
What's the point you were going to make?
Neil (he / him / his) 00:11:05 It was, upstream, Python Semantic Convention Libraries, the generic type, was… I guess, I, I, not to use the right technical term, broken or something, like, it failed, so you know already, Aaron, that sounds like, maybe? Or you're.
Aaron Abbott (Google LLC) 00:11:21 Yeah.
Neil (he / him / his) 00:11:23 Okay.
Aaron Abbott (Google LLC) 00:11:23 I think… I think the… sorry, based on the clarifications here, I think we can update the Utiligent AI to do… something a little bit better, because it still has this bug, so…
Liudmila Molkova 00:11:36 I just…
Aaron Abbott (Google LLC) 00:11:36 Yeah.
Liudmila Molkova 00:11:37 I removed it.
Yesterday.
I deprecated it, so we no longer create generic types.
Aaron Abbott (Google LLC) 00:11:44 Okay. If people want to pass, like, if they need the escape patch, is there still a way to do it, Liudmila?
Liudmila Molkova 00:11:50 Yeah, they can pass whatever other part. They can create, their own type.
Aaron Abbott (Google LLC) 00:11:57 Okay, and then does it, does it…
Felix Becker (Anthropic) 00:12:00 Sorry, sorry, is there a generic part or not? Like, can you add additional parts or not?
Liudmila Molkova 00:12:06 You can. It's just you should not use generic part for this, you would rather declare something specific.
It would fall…
Felix Becker (Anthropic) 00:12:15 If the object has to comply to the JSON schema, how does the JSON schema declare that additional parts are valid if there's no generic part?
Liudmila Molkova 00:12:27 It exists in JSON schema.
And, it says that it's not… it has a type.
Right, Aaron? And then it's not one of these types.
Not one of the standard types.
Aaron Abbott (Google LLC) 00:12:47 Yep.
Felix Becker (Anthropic) 00:12:48 Okay.
So that… that's… that's basically what generic part… so generic part is still in here.
Liudmila Molkova 00:12:57 from there.
Aaron Abbott (Google LLC) 00:13:00 We were talking about the implementation for the Python instrumentation, which… I haven't looked at that PR, but the idea was, like, people don't pass generic part, they… like, the… this is mostly just for consumers, as, like, a kind of sentinel that they should allow extra stuff, but producers don't think in terms of generic part, they just put the stuff that they need for JSON. Yep.
Ankit Singhal 00:13:23 And…
Felix Becker (Anthropic) 00:13:24 I just want to call out that, like.
Technically, any time you expand this knot, it would be a breaking change, right?
Liudmila Molkova 00:13:31 Why?
Felix Becker (Anthropic) 00:13:31 Chris.
Because… Some producer could already be producing the exact same Like, discriminator value that you are then trying to forbid going forward.
Liudmila Molkova 00:13:50 They are pretty much, thank you.
Felix Becker (Anthropic) 00:13:51 added image doesn't exist here yet, right? Like, let's say you want to add first-party support for, like, image in the spec.
But some vendor already chose to export image, and now this says not enum image.
Aaron Abbott (Google LLC) 00:14:08 Yeah, that's to… so I think that's why we added this, like, recommendation for vendors to include dot, but it's… it's true, it's not enforced in the schema. It doesn't… to just do whatever, like, vendor prefixing.
Felix Becker (Anthropic) 00:14:21 Yeah, I think that's fine. We can just say that in the spec text to, like, prefix.
Aaron Abbott (Google LLC) 00:14:27 Yeah, yeah, it does… it does say here. I think you left this comment, too, about, You guys currently do underscore instead of dot.
Felix Becker (Anthropic) 00:14:36 Yeah.
I was just writing a response. Like, the only reason we use underscore is because we also have, prefix properties, so, like, anthropic underscore MCP server name.
And I thought dots are difficult to parse in some languages if you want to, like, deserialize it into a struct.
So I used underscore there, and then I wanted to stay consistent with the, like, discriminator value, too.
But no, like, strong reason.
Liudmila Molkova 00:15:09 Do we care? Underscore or dot?
And it would be shooed.
It should, probably, right there.
Aaron Abbott (Google LLC) 00:15:21 Yeah, I don't even think… so I don't think the text here says to use dot, it just says you should do a vendor prefix, so it's kind of…
Felix Becker (Anthropic) 00:15:27 Okay.
Aaron Abbott (Google LLC) 00:15:28 Yeah, like, the goal is to inform you to not collide with that not enum thing. The goal, and yeah, give, like, an expectation. I think either way is perfectly readable for a consumer.
Felix Becker (Anthropic) 00:15:38 Okay, sounds good.
Aaron Abbott (Google LLC) 00:15:40 Yeah.
Neil (he / him / his) 00:15:43 Does that mean we are or are not standardizing on dot versus underscore?
Liudmila Molkova 00:15:49 Awesome. Ankit?
Ankit Singhal 00:15:51 Hey, yeah, one quick question about the generic part and the type field. So, if I add a new generic type, which is… which doesn't have a type field in that enum list, right? When I add a generic part, do I have to add a type to it?
Or… right? Okay, so that's why we are… that's how we are kind of… Okay, go ahead.
Aaron Abbott (Google LLC) 00:16:12 Yeah, so please take a look, like, there's some new test cases in here which are based on, like, YAML files, so you can see the errors that you would get for different things, and I think, based on that, I think it should cover Like, all the info… all the, behavior that you all just said.
Ankit Singhal 00:16:31 I see.
Good, okay.
Sounds good to do.
Liudmila Molkova 00:16:42 Awesome. So then, it seems we still have a few comments, and we need somebody else to approve.
Neil (he / him / his) 00:16:51 I'll approve. If we saw that last bit, I'll approve. I'm gonna do approve. I just didn't want to not approve without that scene, being seen. The generic type, and as long as it's known even.
I think I can do that.
I know.
Liudmila Molkova 00:17:06 Alright, it seems we talked about this yesterday, and we still need another approval on this one.
And there is nothing to discuss.
Aaron Abbott (Google LLC) 00:17:15 But I approve this one, Ludmila, but I think…
Liudmila Molkova 00:17:19 The second company.
Aaron Abbott (Google LLC) 00:17:20 Company. Okay.
Liudmila Molkova 00:17:21 Yeah.
Trask Stalnaker (Microsoft Corporation) 00:17:22 That's on me.
Liudmila Molkova 00:17:26 Yeah.
Yeah, Felix, we should chat about this. I also brought it up.
So, let's talk about this one.
So I think there are two… parts of the problem. The one is… How do we represent?
Inference that happens on the server, like on the hosting model hosting place, or somewhere close to it, the provider.
Felix Becker (Anthropic) 00:17:56 And how.
Liudmila Molkova 00:17:56 How do we… what is the… from the client perspective, when we make a client inference call, what does it mean?
And… I think the bottom of it is this issue you created.
And we went back and forth, right?
And we're essentially picking how those things look like.
And you had a couple of proposals.
The one includes something like this.
And another one I don't completely understood, but probably renaming the client part to this guy.
Felix Becker (Anthropic) 00:18:35 Yeah, well, like, I think the dot internal span you brought up, right, the… I think, basically.
What we have here is… Two separate operations that are currently one span.
And…
Liudmila Molkova 00:18:53 So… They aren't, though, right? Because we're saying it's the client's pen.
Felix Becker (Anthropic) 00:19:01 no, what I'm talking about is, like, the… the… like, in Anthropic, a messages API request.
Which runs a server-side tool loop.
That is an operation that I would like to represent with a span.
And that has a lot of, like, GenAI attributes of, like, how much tokens did this entire request use, right?
and then there's… like… actual, like.
the real, like, inference calls, or I should not say real, but, like, that server set tool loop, does multiple actual, like, prompt and responses, gets multiple… sends prompts and gets responses from a model, right? Multiple times. So that is a nested child operation, like a one-to-N… children that I would also like to represent with a child span, and that also has GenAI metadata, like how much tokens did just this one iteration use, right?
And so, currently, there are not two separate spans defined in the spec. There is only one.
And I would like to see at the bottom.
Liudmila Molkova 00:20:20 Yeah.
Felix Becker (Anthropic) 00:20:20 So, like, the two options, basically, I saw in my last comment was, like, one is.
we could keep the current name of, like, inference as, like, the whole messages request, right? And then maybe the child spans are, like, the .internal new span, or you could do it the other way around, where the internal ones is what we currently consider the inference spans, and then we have a new span that's, like, for the whole server-side tool loop, like, you know, messages, API requests.
Liudmila Molkova 00:20:53 So, hear me out. What we have today, it's only the client side. It's not… it does not represent internal inference.
It represents… and what I'm trying to clarify in the PR, it's only what you see when you call remote model service, which can do tool loop, or might not do internal tool call loop, we don't know.
Like, as long as you're a remote client, you have no… well, little means to know.
And yes, we can add the internal span for the inference. There is a good question, should it be internal?
Should it be server? What's the difference? Because there is a difference, right? Because if you do inference client, you probably have the server, and if it does tool loop, then it probably has a bunch of inference calls under.
So, there's more to discuss there than… Then just, let's introduce another span.
But I think what I'm trying to say, that what we do is find here is limited to this, and I just love to find the right words to express it. I tried, in this PR I had.
Here, and I don't know if I succeeded. It seems I did, so maybe you can suggest some words that I can use to make it clearer.
Felix Becker (Anthropic) 00:22:16 Well, I guess where my confusion just came from is the PR says that it closes the issue I opened, and I'm just saying, like, well, it's not solving the issue that I have, so…
Liudmila Molkova 00:22:27 Does it? Oh, I'm sorry. This… okay, I see, I see.
Felix Becker (Anthropic) 00:22:32 I misunderstood if your intent was more to just, like, you know, clarify, or…
Trask Stalnaker (Microsoft Corporation) 00:22:38 Wait, we're chipping away at that problem.
Felix Becker (Anthropic) 00:22:47 But then, independent of that, would still love to actually, like.
you know, push that discussion forward. Like, right now, we're in public beta, so we can… this feels like a, you know, pretty significant change to the structure of, like, what we would emit, so… If.
Liudmila Molkova 00:23:07 Why?
Felix Becker (Anthropic) 00:23:10 Because, cause, which spans we, like, annotate with which GenAI.operation.name.
would change, right? And then if customers already build dashboards with, like, query filters of, like, where the span has GenAI operation.name equals this, you know, then count that token usage and stuff like that.
Like, those would potentially break, and so it's… it's now a good time to make that change in beta, versus once we go to GA, you know, it's a lot harder to make those very big breaking changes.
Liudmila Molkova 00:23:52 So the thing that would change is that for the queries.
The operation name, I don't know, but the span kind should be taken into account.
Felix Becker (Anthropic) 00:24:04 Well, currently, span kinds aren't really exposed, right? Like, only GenAI.op operation.name is exposed.
Liudmila Molkova 00:24:09 Oh, they are absolutely exposed. They are part of, up until the model.
Trask Stalnaker (Microsoft Corporation) 00:24:13 And type.
Liudmila Molkova 00:24:15 Oh, spend type not, but spend kind is.
This internal client server.
Felix Becker (Anthropic) 00:24:25 Oh, I see. So what you're saying here is this is actually not a different span type, it's just a… just a kind attribute is different.
Liudmila Molkova 00:24:32 It's… both are different. The… there is a span… They are similar.
But, like, I tried to express the difference, I just… it's just a demonstration I created.
So this would be the… let's ignore server for a sec.
So, for, let's say, the client, we are saying that the usage is… what provider returned. And here we would say that the usage is what we actually detected.
Here.
But, they have different kinds, they have different types.
They have very similar set of attributes.
I can, like, argue a little bit on where the global attributes are configured on the span itself, or on the resource attributes and such, but I can definitely define this friend.
Yeah.
Felix Becker (Anthropic) 00:25:35 I think Africa.
Trask Stalnaker (Microsoft Corporation) 00:25:37 that the server and internal were in here, so maybe, Felix, does that solve your… Modeling question, then?
Felix Becker (Anthropic) 00:25:49 Yeah, if this… I mean, so this PR is adding, like, a dot internal.
Liudmila Molkova 00:25:54 No, it's just a random commit I call.
Trask Stalnaker (Microsoft Corporation) 00:25:56 Great to demonstrate.
Sorry, okay.
Felix Becker (Anthropic) 00:25:58 Oh, okay.
Trask Stalnaker (Microsoft Corporation) 00:25:58 I got a lot, okay.
Felix Becker (Anthropic) 00:26:00 But yeah, I think that would work. The one thing maybe to think through here is, like.
I think the server kind, you're only supposed to really use on, like, the HTTP kind of route handler, like, the very outermost layer, right? And then everything below that is internal.
So if there's something sitting in between… the inference server span, like, if there's, like, an HTTP handler span that's already server, it would be a bit weird to be, like, server, server, and not server, and then straight to internal.
Trask Stalnaker (Microsoft Corporation) 00:26:32 So we discussed that a little bit yesterday, around, invoke agent server spans.
And so we do have precedent for there being nested server spans. For example, HTTP server span can… and then RPC server span can be nested under that.
So… It… it could be… it could… be okay to have the inference service pan nested under a HC… under a protocol?
Server span.
Felix Becker (Anthropic) 00:27:08 As long as there's, like, a clear kind of guidance and it's consistent, I think that's… that's fine.
Trask Stalnaker (Microsoft Corporation) 00:27:14 But also, what we discussed a little yesterday is some people would Some hosted, like, agent providers would Likely choose not to omit the protocol.
level span, and only emit the… Invoke Agent Server Span, and, you know, you could do either from Anthropic, you could.
Felix Becker (Anthropic) 00:27:39 Yeah.
And I guess the other point to discuss, You said that, you… The internal one, though, like, you wanted to represent, like.
I don't know, I guess, like, the real… in friends of, like, where the actual GPU runs, or, you know? Or, like, you wanted some kind of distinction there.
Trask Stalnaker (Microsoft Corporation) 00:28:05 So normally, internal span kind would be, in… means in process. Like, it's not a remote call.
So, like, typically, if, so if the inference happened in process there, that would be an inference internal.
But if you were making a remote call to do the real inference.
I think that would be a inference client span.
Felix Becker (Anthropic) 00:28:34 Okay. So, basically, using this internal inference span would be… bike.
Blessed for us to emit this for the, like, server-side tool loop.
So I don't think we intend on, like, emitting, you know.
when the actual inference happened on, like, GPU side, because that's, like, you know, way too low level.
Liudmila Molkova 00:28:59 We have a lot of interest from people who want to actually instrument the engine.
Felix Becker (Anthropic) 00:29:03 Yeah, yeah, that's why I just want to make sure that, like, we're not conflicting with…
Aaron Abbott (Google LLC) 00:29:09 I think.
I don't need to pay.
Yeah, like, we do the same thing with load balancers for HTTP, right? Like, you would have several server clients, because most likely the thing that's serving this response or doing the loop isn't even where the GPU is, right? So you would have more hops if you were representing… if you wanted to add that later, it would be probably a different server or whatever.
Felix Becker (Anthropic) 00:29:33 So would that also be, like, a dot internal span, or would that be, like, a new span? Like, yet another span type that we invent?
Guess that's my question.
Aaron Abbott (Google LLC) 00:29:46 You would pick…
Trask Stalnaker (Microsoft Corporation) 00:29:49 Right.
I think you would just pick, it's an inference span.
Right? That, and you can pick, you pick whether it's, Spankind Internal or spankind Client client.
Based on… If you're making, essentially, like, a remote call, or it's… Happening local. Although, since you're not propagating downstream, and you're not capturing anything on the other side, it sorta doesn't really matter.
I guess.
Ankit Singhal 00:30:28 So, in that case, would the inference client, which is under the user app shown in this hierarchy, would be… It's the same as the influence internal provider under Influencer Responder.
Both are basically the same.
Kind of inference kind of spend, right?
Is my understanding correct, or…
Trask Stalnaker (Microsoft Corporation) 00:30:55 I didn't follow, but
Ankit Singhal 00:30:57 It's true.
Trask Stalnaker (Microsoft Corporation) 00:30:59 Maybe you can…
Ankit Singhal 00:31:00 Alright, use.
Trask Stalnaker (Microsoft Corporation) 00:31:01 using Ludmila's,
Ankit Singhal 00:31:02 Oh, yeah, I think, I think, yeah, that covers it.
Trask Stalnaker (Microsoft Corporation) 00:31:04 Thanks.
Ankit Singhal 00:31:05 Yeah, okay.
Liudmila Molkova 00:31:15 Who else hates that, the, the… The indentation here is not the indentation in preview.
Ankit Singhal 00:31:23 Yeah, I think…
Neil (he / him / his) 00:31:24 It's not what you get.
Liudmila Molkova 00:31:30 Okay, it sounds like we might want a little bit more time to… To let it settle down and discuss.
Maybe we get back to this on Friday and see if we have any additional thoughts.
Ankit Singhal 00:31:45 Yes.
One more thing a little bit on that, for the tool… execute tool span, did we specify what the span kind is?
In the…
Liudmila Molkova 00:31:58 Always internal. Too cool, we don't know.
Felix Becker (Anthropic) 00:32:02 Would you maybe want to put your proposal here, or your, like, scrap commit as an actual PR, and we can comment on it.
Liudmila Molkova 00:32:09 I don't currently have energy to push it forward, and my interest is mainly to like… Try to stabilize what we have.
Felix Becker (Anthropic) 00:32:20 too.
Trask Stalnaker (Microsoft Corporation) 00:32:22 Did you get legal?
Liudmila Molkova 00:32:23 Approval from legal?
Felix Becker (Anthropic) 00:32:25 I did. I'm on the CLA now, guys.
Trask Stalnaker (Microsoft Corporation) 00:32:31 Congrats.
Felix Becker (Anthropic) 00:32:33 I know, big milestone.
Trask Stalnaker (Microsoft Corporation) 00:32:36 Yeah, I mean, I… I'm personally in favor of merging this and, having Felix send a follow-up PR for… The, server and internal kinds.
Felix Becker (Anthropic) 00:32:52 Okay, let me just take another look over the PR with, like, the, you know, context of, like, this is just an intermediate.
step stone. I think there were some comments.
I loved that.
I was still… like… I don't know if they're resolved, by, you know, that added context.
But yeah, we should call for today. We can re-discuss Friday.
Liudmila Molkova 00:33:20 Awesome, thanks, Anna.
Felix Becker (Anthropic) 00:33:22 Really appreciate you, opening that PR, by the way, and, trying to resolve this.
Liudmila Molkova 00:33:29 Yeah, thanks for the confusion, seeing it fixes the issue.
Neil (he / him / his) 00:33:34 You guys have earned your no-pay today. Oh, sorry, go ahead.
Liudmila Molkova 00:33:39 We are out of time.
And we didn't even start talking about this friend.
So maybe while we are still here.
It seems, Max, you have a couple of proposals, right?
Max Ind (Google LLC) 00:33:56 Yeah, I… Yeah, with my initial, I kind of made a mistake, but I treated foreign names and conflicts as… The same, so that led to… And also, like, loop as a term was kind of just, like.
only applicable to a subset of workflows, which is kind of not great. The current kind of… that's… the current proposal that kind of strikes the middle ground of Not being too specific, or not being too vague is the Agentic system.
And, but this is basically… Or, like, something flow. I'm curious how set are we on having… Verb and noun be the naming.
Liudmila Molkova 00:34:52 I don't think it's important. I think what's important is that it's, like.
Broad enough, but also not broader than necessary.
Max Ind (Google LLC) 00:35:02 Yes.
Yes, my current favorite is Agentic System, because… It's broad, but not too vague. That's such that it doesn't mean anything.
Liudmila Molkova 00:35:13 But it doesn't tell the action in any form.
Like, what does it do? Maybe you create Agentic system, or maybe you update Agentic system.
Max Ind (Google LLC) 00:35:23 That's fair.
Yeah, an invoke Agentic system would be… long.
like, run Agentic system would be.
Run Agentic system would, would be shorter.
It wouldn't fit the span, the operation… the current operation names, though.
Hmm… Yeah, but that's fair. So I feel like, yeah, we do need a verb.
Or, like, at least, like, invocation. Invocation.
Liudmila Molkova 00:35:55 And that implies some specific action, like…
Max Ind (Google LLC) 00:35:57 Yay, yay.
Liudmila Molkova 00:35:57 That's why I liked… Turn or run, because it implies something specific, but flow is also… I think we're still ultimately choosing between calling it an agent, like using agent as a noun, or inventing something, some form of it that's less controversial, like Agentic.
Max Ind (Google LLC) 00:36:19 Yeah, Agentic is, you know, slightly less, I feel like it's slightly less controversial, because I feel like workflow is, like, a separate concept, I… Yeah.
Aaron Abbott (Google LLC) 00:36:30 do we consider, like, harness? I think I dropped that in some comments, but I kind of like that it captures that it's before, like, the user-defined agent, and it's… it's kind of like the… the, like, part of the Agentic system that's not You know, it's like the startup code and stuff like that, like, the entry point even before the loop runs, right?
Liudmila Molkova 00:36:51 Wait, it's for all agents.
Aaron Abbott (Google LLC) 00:36:55 What do you mean?
Liudmila Molkova 00:36:56 Any invoke agent would become this spanner metric.
Aaron Abbott (Google LLC) 00:37:01 Okay, okay.
I see.
So it's not just the top level anymore.
Liudmila Molkova 00:37:08 For the top level, we can pick operation name, that would be… But not this panty parametric one.
Aaron Abbott (Google LLC) 00:37:15 Okay, okay, yeah, I remember now.
Max Ind (Google LLC) 00:37:18 Okay, I… I…
Ankit Singhal 00:37:21 For Agent System.
I'll say.
Max Ind (Google LLC) 00:37:26 So…
Ankit Singhal 00:37:26 Agentic system.
Max Ind (Google LLC) 00:37:31 Sorry, could you, could you repeat?
Ankit Singhal 00:37:33 I was saying, like, Agent Existant Turn seems like a good candidate, at least for me.
Max Ind (Google LLC) 00:37:39 Yeah, just needs, like, some action.
Which I didn't realize, Yeah, I don't wanna, like, think, on the spot to come up with, like, a name. I wanna actually, like, have the, like, it go through the ringer of all the names, and I wanna, like, have something which is short enough.
Such that, you know, it's not a mouthful to talk about, but then also, you know, vague enough, but also not too vague, yeah. But yeah, Agentic… Agentic something is, like, a good, Good trail, I think.
Neil (he / him / his) 00:38:24 I was trying to think about handoff, which I think is kind of a variety of this, or a sub-component of this, and just wrapping my own head around, like, how a handoff like, I guess the shapes of it or whatever, and I feel like this is, a subset, superset, some variety of set, and I feel like the nature of it as… Either ACE, what's the word? Bidirectional, unidirectional… defined, you know, undefined, like, those are the types of structures, I think, that we're trying to describe together, and so that's why, like, a workflow in turns, I feel like they conceptually… Cause, like, we haven't defined the right parent term that will allow the The specific behaviors of the varieties or the subsets to nest, like, the little dolls properly.
And so maybe that's… I don't know. So that's why I started thinking about them, and like… their structure, and like I said, you know, is it bidirectional? Am I expecting it to come back? In other words, you know, are there… could there be others along the way, or do I know I'm just handing it to this one, and they're getting it right back? Or maybe I'm never gonna see it again.
So… Is that… Useful? And thinking about how this structure lives in…
Max Ind (Google LLC) 00:39:50 I'm actually now… because, like, after the previous point, I'm now actually very unclear what an agent even is, because it seems that, like, some inference APIs… because I always operated under the assumption that an agent is a model plus tool plus a system instruction, but it seems that, like, now most inference providers just allow you to specify all three of these, and then you… we call something an inference, just because the API calls this an inference, but there's actually, like, an entire agent, or what you may call an agent, running under the hood.
Felix Becker (Anthropic) 00:40:26 I mean, that is a big question, right? Like, what… what is an agent? Is every… like… everything's kind of… anything that has tools is an agent, so technically a messages API request is already an agent.
So I think it's for kind of the standard to decide of, like.
Is there, like, a purist view we have here, where, like, yeah, those should be marked as agent, or is there, like, a… Is it more like a view of… Things that don't market themselves as an agent are not agents, and it's kind of up to whoever implements it to decide what they want to market the thing as.
Aaron Abbott (Google LLC) 00:41:09 I like the water.
Neil (he / him / his) 00:41:14 What was that, Aaron? Sorry? You like what?
Aaron Abbott (Google LLC) 00:41:17 Sorry, I like the lottery, like, you know, somebody's gotta choose, and I think…
Neil (he / him / his) 00:41:21 Oh, the lottery?
Aaron Abbott (Google LLC) 00:41:23 No, no, ladder, the last thing Felix said.
Neil (he / him / his) 00:41:25 Letter, letter.
Aaron Abbott (Google LLC) 00:41:26 Sorry, go ahead, Trask.
Trask Stalnaker (Microsoft Corporation) 00:41:30 Are… is this span, whatever we're calling it, is it still gonna have agent name?
As an attribute.
Max Ind (Google LLC) 00:41:43 It may have either the agent name or the workflow name, or do… yeah.
as in the current proposal. It would have agent-specific attributes for if this… Agentic run means an agent, and workflow-specific attributes if it's a workflow.
Trask Stalnaker (Microsoft Corporation) 00:42:05 I mean, honestly, my… preference, or I would be super comfortable with Calling them all invoke agent, and calling them all Agent.name.
Just using agent as the…
Felix Becker (Anthropic) 00:42:24 I mean, this also goes back to, like, the discussion we had before on my messages request.
Spans, like, are those Stan Invoke Agent 2.
Liudmila Molkova 00:42:36 Yeah.
They could be Invoke Edent Client. Let's… Let's like…
Felix Becker (Anthropic) 00:42:44 The thing is, sometimes, like, there may be many requests where customers don't supply tools, right? Like, this is only if you actually put in like, web set for web fetch or web search tools or MCP connectors into your request. Most requests don't have that, so… That's where, like, it could be confusing to users to, like, say all of these things are an agent, you know, versus… Yeah, I kinda… I also think it's a bit up to the, you know, vendor to decide of, like, what is… what is this thing marketed as, and… and the standard needs to… Just provide the, like, different… Classifications.
Neil (he / him / his) 00:43:29 Gracefully degrade.
Liudmila Molkova 00:43:35 I seem like it's common for…
Neil (he / him / his) 00:43:37 Totally.
Liudmila Molkova 00:43:37 now to host the same, the Agentic and model API behind the same API, REST API. You just choose by choosing the specific thing.
Okay, so it sounds like there are… two options on the table. The one is Invoke Agent Trask.
I'm comfortable with it, too. The other one is something else.
And, this would probably involve something Agentic.
Max Ind (Google LLC) 00:44:11 is…
Liudmila Molkova 00:44:14 And then this, the verbiage part doesn't seem important, or maybe there are some preferences, but… Like, all of them are vague enough.
This being the most… the vaguest one, probably.
Can we just, I don't know, say this is the running candidate? Because who cares?
Max Ind (Google LLC) 00:44:39 Sure. Yeah, I'm curious, because if I'm the only person in the room that feels like that the distinction between workflow and agent is… somewhat meaningful, then… then I'm… I'm complete… I'm, like, fine going with, with Invoke Agent, just as the… As the running candidate, just for the span type and for the… yeah.
Neil (he / him / his) 00:45:02 I mean, I do think it's meaningful and important, I… yeah.
I think what Liudmila was saying, leading candidate, not in that it'll win, it's just, like, that's the… the best option we have on the table at the moment, but Ludmila, I don't mean to… I'm just trying to synthesize what I took away from your statement.
Liudmila Molkova 00:45:22 In other words… In the workflow…
Neil (he / him / his) 00:45:24 Hang on.
Liudmila Molkova 00:45:25 the… I think the story with the workflow is that it probably doesn't even have a name.
Like, we… we create some… something… Out of it, like.
In LangGraph, it's the class name of the graph implementation.
It's not meaningful.
Max Ind (Google LLC) 00:45:46 Because, like, I know at least, like, in… plot code, you can define, you know, workflows where you, like, you know, Where you, like, basically… Have a predefined, you know, Like, a basically structure that, okay, after this agent is called, another agent is… Called always. So, like, you know, you would do… like a… you know, like a code review agent is always called after this something, right? Or you can have, like, deterministic steps that don't involve agents at all in the middle. So some workflows, I think, are called. In Langraph, they may not be called. They may be called just by the… variable name that you assigned the workflow creation to. Maybe they… Don't bother naming them, because, Because… It would be… like, you don't need to name it in code.
Anything other than just give the… Give the workflow the variable name that you assign it to, probably.
And… But yeah…
Liudmila Molkova 00:46:55 It's useful to capture if it was, like, parallel workflow or sequential workflow, and… It… At least in my mind, it doesn't seem super controversial to say that this Agentic invocation is done by a workflow.
And having some workflow-specific attributes on it.
Max Ind (Google LLC) 00:47:17 Yeah, Agentication, that sounds, that sounds like, you know, just enough, just enough, just, like, a smidge of vagueness that pushes it over the line for me to feel completely comfortable with.
Trask Stalnaker (Microsoft Corporation) 00:47:32 I have a question, what the… I know we're… we wanna… we're talking about merging these two spans, workflow and agent.
And we have kind of this third thing that we're grouping in there.
But I'm wondering, like, If the thing doesn't… like, the agent.name feels very… critical to that span. Like, I'm wondering if it does… if it does make sense to have two different span types.
one that's… Invoke agent with an agent… Name… And one which is sort of a… an orchestration, an Agentic flow, something that's, you know, not… just an agent, doesn't have an agent name, because if you have an agent name, you should use Invoke Agent and stamp that agent name on it. If you don't have an agent name.
you have a… Some… this other thing that we're trying… this Gen more… this other thing we're trying to define.
Liudmila Molkova 00:48:45 Even in the… Let's say link chain. The agent doesn't need to have a name.
It's called an agent.
The story, like, from… My side started that… Imagine you did it with workflow, or with some orchestration, and then you switched to top-level Agent API, and nothing substantial has changed, you just changed the shape of the API, you call. For your external users, it's still the same thing. It does the same stuff.
So the… then, if we had two different… Types of the span into different sets of metrics.
then we would need to report to SPANS all the time.
So the one, the outer… That represents overall execution, and then the inner, that is more specific.
Neil (he / him / his) 00:49:53 But what if it's a series of inners, I guess, is the thing that I am… am wondering is, you know, you described, a workflow of, like, hey, I come on, I invoke an agent workflow… sorry, I did it there. I invoke a workflow, and a bunch of stuff happens, and then I return back.
to what I did and I'm done, but if I do multiple workflows at a time.
You know, or my job is to do a series of workflows all day long.
I think if I… maybe if I understand you correctly, Ludmila, if I'm trying to… wrap how I would wanna… structure the data with what you've described. If the first thing itself is, like, a self-referential invoke agent, that's like myself, and then there's a variety of that invoke agent, that's invoke agent, that's a workflow, I don't think that's what you're suggesting, necessarily.
But I… that's how I would allow, or in my mind, you could construct your model in ways that were discrete enough to separate What was the agent's startup before he or she… agents don't have gender, sorry, before the agent got, involved in a workflow, during the workflow, and if you will, whatever comes after the workflow as being separate, potentially, operations that may have their own telemetry needs.
Liudmila Molkova 00:51:14 Somebody I'm saying there is… let's say there is an agent.
And it consists of two sub-agents.
And then tomorrow… I switched to workflow.
Unnamed.
And it has the same adjunct.
I'm sorry.
How do I monitor?
those two systems.
in a similar way. They are very similar functionally, they are the same.
So, the outer metric we… It should be the s- the same… We can report For this guy.
That is an outer thing and agent as well, right?
So let's pick this example.
And then there are nested things for A and B.
The current proposal, if I understand it correctly, if we have the shared knowledge of this.
We are saying that… All of them.
our invoke agent.
Right?
Right.
So, if we decide that we have two different types,
Trask Stalnaker (Microsoft Corporation) 00:53:33 Why do we have outer the new thing there?
Liudmila Molkova 00:53:38 Oh, right. Because… If we don't have it.
So, if we… This is new.
This is… No, no, this is the proposal, and this is the new proposal.
So, in the context of current proposal, This is… Still… Out to invoke Agent.
This is the new proposal.
the… In the current proposal, the telemetry shape does not change significantly if we change primitives.
And this new proposal that… where they are different.
You have to preserve… Okay, there is no invoke agent here.
So for this, structure.
You need something wrapping?
And it's not an agent.
But here, it… There's an urgent.
Neil (he / him / his) 00:55:12 That was really helpful, thank you, Ludmila.
you know, gold sticker for your explanation here. I think for me, that clarifies things, and I think the question for me in this or the others, and maybe this is how it comes down to, is does the telemetry data allow me to, differentiate Let me just make sure I'm seeing… in the current proposal, can I tell… with or not it was a formal workflow that caused Agent A and then B to be called?
Or is it just a sequence of events that I'm calling a workflow that doesn't really have a name, and they're both covered by… this outer invoke agent, which is workflow or not workflow, I guess, I'm seeing now what you're saying. Like, it can be a workflow, but it doesn't have to be, and the telemetry is generic enough to support both?
But the current proposal, you have a change that's involved, the outer new thing, as you put it, and so it… I don't know if it breaks is the right word, but it forces the structure to change into further.
And you think is unsupported by the… as you read it, the… whatever risk-reward, or juice versus squeeze, effort, you know what I'm saying? You know, you favor the current.
Liudmila Molkova 00:56:38 No, I… It seems you've been asking the question, and I didn't get the question.
Neil (he / him / his) 00:56:49 Oh, the question is… Oh, in structure. The current… according to what my understanding, the current proposal… invoke agent is a workflow, or it's not a workflow. It's not specific to how that structure exists, and the new proposal, forces us to choose whether it is some… what variety of invocation is going on.
Is that… do I… do I have that correct?
And if that's right, then you… You think that the current proposal is a better way to do this, because it's less change for more or less the same benefit?
Liudmila Molkova 00:57:29 It doesn't matter what I think. I'm, I'm…
Neil (he / him / his) 00:57:32 Alright, perfect.
Liudmila Molkova 00:57:33 What I think is better. I want us to have a discussion on process.
Neil (he / him / his) 00:57:36 Right, right.
Liudmila Molkova 00:57:37 Thanks.
Neil (he / him / his) 00:57:38 Yeah, yeah, just like the pro… you think there's a lot of pros to be said for the current proposal?
Liudmila Molkova 00:57:42 It doesn't matter.
Neil (he / him / his) 00:57:44 Just like you're a smart person, I guess, I mean, and you think, like, there could be a trade-off.
Liudmila Molkova 00:57:50 Can we talk about this, if you see any pros or cons here?
If you have any specific pros or cons to mention.
Neil (he / him / his) 00:58:00 Well, that's what I was… I guess what… maybe I was… the question that you were asking me that I didn't ask. So, if I understand correctly, and there's a structural change between the current proposal and the new proposal.
On how workflows versus agent calls are… Defined.
And if there's a new structure that is more disruptive in the… new proposal than the current proposal, which seems to offer little to no benefits, then I don't see why we would do the new proposal versus the current proposal.
My ask, though, is, like, workflows matter, I think, and so how we can support workflows is important, and that's why I was kind of trying… seeking your guidance on if you thought one was offer better support or worse support for workflows as a concept.
And if that mattered at all.
you know, I have my perspective, but, like, we're here to talk about what, you know, the shared… shared impact on some of these decisions are.
And so I like workflows as a container object of control structures, as a telemetry bucket or whatever, you know, be able to group operations around how things work and how And when, I guess, maybe when they don't.
want to impose a view if… the consensus from everyone is the… Structure is unwieldy.
Liudmila Molkova 00:59:29 I think we are at the point where we need facts more than opinions, and I'm curious what people think. And it sounds like, Trask, you… you asked, why?
We don't.
Keep the current structure, yeah, what do you think?
Trask Stalnaker (Microsoft Corporation) 00:59:47 So, I think that, metrics is… metrics are compelling.
argument for keeping them consistent there. I… I do feel like… in that restructure, we lost the agent name, the XYZ name, and so I felt like most of your telemetry Like, a lot of your telemetry is going to… B… Different in that workflow, unnamed workflow.
scenario anyways.
But… I, I, I mean, I, I still… I mean, I… combining them, I think… Is nice, avoids that.
I think that Agentic invocation.
Liudmila Molkova 01:00:46 I would…
Trask Stalnaker (Microsoft Corporation) 01:00:47 It's nice and generic. Yeah.
Liudmila Molkova 01:00:49 We… we went… So there is a nice property of Invoke Agent that we keep pretty much everything intact.
The… if we end up with something like Agentic invocation.
It would be a change, but it would also make it consistent, because we have inference, embeddings, Agentic invocation.
It's very minor.
Trask Stalnaker (Microsoft Corporation) 01:01:20 I see, does Agentic… Is it too broad?
Includes… including… tools, inference…
Liudmila Molkova 01:01:30 It seems like this is what, worded up here. So, the model client libraries provide to loop.
Is it an Agentic workflow? Agentic flow? Agentic invocation? Felix mentioned, yes, they call it an invoke Agent. At least the data point is in… is there… in this direction.
Max Ind (Google LLC) 01:01:56 I'm curious if the metric argument applies, like, if you go lower, like, if you go on the inference level, or, like, some… because, like, I think we… like, the consensus is that, like, you know, if some API calls it an inference, but it actually does, like, a tool loop under the hood, we still call it An inference span?
So is there, like, a compelling case that… this inference API should also have the metric be… Unified with whatever we're, like, trying to unify here.
Liudmila Molkova 01:02:33 There, there is a nice benefit of it being client.
And we can maybe align closer Client agent with inference client, because, yeah, we… it's hard to tell the difference.
Max Ind (Google LLC) 01:02:51 Yeah, so maybe that's the differentiating factor, that, like, internal Agentic… like, Agentic system would be only internal?
For, like… for, like, internal inference, that's the… You know, doing the actual inference, like, somewhere.
Liudmila Molkova 01:03:19 Can we… Separate these two problems? Like, they are related, but… Bye.
I don't know.
Neil (he / him / his) 01:03:35 that's… that's how I lean is, basically, like, find where they overlap, or whatever… find the… what's the word I'm looking for? You know, find… find the right cal… Child-parent relationship?
Maybe?
Or, or nested structure, or something, so that you don't have to choose, you just have to decide how, but you don't have to make a choice that will end up without you having the insights that you need.
I know we're super over time now.
I appreciate Ludmil, in particular, your patience, and Trask and everyone else as we talk through very complex things that I don't always understand in the abstract, frankly, fully.
Liudmila Molkova 01:04:21 Would it be helpful if we, try to think about… the dashboard.
And, like, I've tried here, so if you think about queries.
How would they look like, for the comment thing?
And… maybe… Since we're super over time, but maybe people can think about scenarios that we would want to see.
Neil (he / him / his) 01:04:51 Yeah.
Great idea.
Liudmila Molkova 01:04:54 And… So… I don't even remember what it was.
Oh, this is by agent name.
And then, like, probably the presence of agent name is something useful, and it's just something that, Trask, you were concerned about, right?
Trask Stalnaker (Microsoft Corporation) 01:05:21 Yeah, I'm still trying to, like… sometimes we have agent name… like, I understand unnamed agents, not having an agent name. If we don't have one, we don't have one. That is what it is. But then to sometimes have a workflow name instead.
feels… a little…
Neil (he / him / his) 01:05:43 I think it's insane.
Trask Stalnaker (Microsoft Corporation) 01:05:43 metric…
Neil (he / him / his) 01:05:46 Oh, sorry, Trask. I was just thinking, I don't think it's instead, I think it's on top of. Like, the workflow has an owner that's the agent ID, and I'm not sure exactly how the details would be structured, but I think, like.
in my model, at least in my brain, like, workflows are a control structure, much like a, I guess, a trace that's got a parent who's the.
Trask Stalnaker (Microsoft Corporation) 01:06:09 So, I think in the proposal here, workflow spans do not have agent.name on them.
They have workflow.name.
They may have child agent spans.
Neil (he / him / his) 01:06:26 Doesn't have an invoking agent on the workflow itself, as it exists as a standard.
I see a smile on your face, Liudmila, I hope I wasn't missing something obvious.
Trask Stalnaker (Microsoft Corporation) 01:06:40 Look at what she's typing.
Liudmila Molkova 01:06:41 Yeah.
Neil (he / him / his) 01:06:42 Oh, yeah, yeah, yeah.
Trask Stalnaker (Microsoft Corporation) 01:06:58 So maybe, Max, for the… I mean, I do think it's worth… still exploring this, like, other alternate general name. But maybe, maybe you can put together, sort of, like, the proposal for what that would be, and… If there's some kind of name, like, what would be the corresponding name, or…
Max Ind (Google LLC) 01:07:24 I should, like, research if workflows are named often. In ADK, they are, and in, I believe in cloud code they are, and that's the most I've interacted with workflows.
But, yeah.
Liudmila Molkova 01:07:39 Yeah, be comfortable putting it in the agent name on the ADK side?
Max Ind (Google LLC) 01:07:44 I wouldn't be that uncomfortable with it. I mean, it would… because we would… It would be, basically, like, the metric would be a little bit confusing.
It would come with the benefit that we would have an easy time getting the end-to-end duration.
But the operation name would still be, you know, up to us, which means that it would be less confusing to talk about the span structure, which is, like, the… the… I think the main win here.
For us.
Trask Stalnaker (Microsoft Corporation) 01:08:18 Yeah, I mean, you still get the operation name, Will, you know, for these To be reflective of the framework.
terminology… But yeah, I think I am struggling a little bit, I think, specifically with that, having both the agent name and workflow name On that metric of, sort of, it feels like then we're essentially bifurcating that metric, splitting it, it's… I'm trying to think if we have any other examples in semantic conventions where we do that. Normally, we have… it's kind of clear, like, your drill down, approach.
Max Ind (Google LLC) 01:08:57 Yeah.
Trask Stalnaker (Microsoft Corporation) 01:08:59 But I could be wrong, I… Have to think on that a little bit more.
Ankit Singhal 01:09:04 Yeah, for workflow, can we just not say they are workflow agents?
They're just some sort of agents.
It happens to be a workflow.
Trask Stalnaker (Microsoft Corporation) 01:09:15 I liked your thinking, Ankit.
Ankit Singhal 01:09:17 Yeah.
Max Ind (Google LLC) 01:09:17 I mean, we have.
Ankit Singhal 01:09:19 Yeah, to be honest, like, to be honest, in Foundry, we did come up with a concept of workflows where you could build this graph, and we call this workflow agents. I don't know how popular it is, but it's there, and we call it agents, and we instrument them as agents.
And if somebody really cares about the matrix for that agent, they name it. If they don't name it, it's just like a… Quid that comes up, and then… If you don't know the name of something that you want to trace or track, then you don't have anything, and it's hard to track.
Trask Stalnaker (Microsoft Corporation) 01:09:57 I like that. I mean, I think we're kind of getting… we're getting that from the operation name.
dough.
Liudmila Molkova 01:10:16 Okay.
If anybody wants to make any final thoughts?
Neil (he / him / his) 01:10:23 Just gratitude.
For everybody.
Trask Stalnaker (Microsoft Corporation) 01:10:25 to sleep on it.
Neil (he / him / his) 01:10:27 Yeah, appreciate the, tireless and thankless leadership, Liudmila, Trask, everyone.
Aaron… Felix, etc, all the contributors.
And the listeners.
Max, of course.
I know lots of people can Ankit.
Lots of friendly faces.
Mikolaj, first time, chatting with you, but enjoyed it. Christopher, maybe next time.
Liudmila Molkova 01:10:53 Awesome, thank you.
Mikolaj Knap (Google LLC) 01:10:54 cute.
Liudmila Molkova 01:10:54 Yo.
Max Ind (Google LLC) 01:10:55 Thank you.
Trask Stalnaker (Microsoft Corporation) 01:10:56 Right.
Mikolaj Knap (Google LLC) 01:10:57 Bye.
