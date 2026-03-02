SIG: LLM Semantic Convention WG
Date: 2025-12-16
Duration: 66 minutes
============================================================

## Zoom Recording Transcript

Liudmila Molkova 00:01:48 Hello, hi everyone.
Josh Bonczkowski 00:01:54 Hello.
Liudmila Molkova 00:02:07 So let's… Start… Looking at our project board…
We have a new issue…
And… what do we have here? Using tokens.
Gray…
This is accepted…
I think there was an issue about… or PR.
And cash tokens.
Is it fair to say it's, duplicate…
No.
We don't mention them here.
Okay, this is going to be in our backlog,
What else do we have?
I think I want to remove this lane. I don't think we need it anymore. We are done with pretty much…
All of the modeling here.
And… yay.
So let's see what we have in progress. Quite a few things.
This is an old one, this is…
Something… Ankit, you are going to bring it up, right?
anksing 00:04:31 I don't know if it's… Yeah, yeah, yeah, I have a PR, which kind of…
Liudmila Molkova 00:04:37 Yeah. So we have it on the agenda, awesome. Yeah. The MCP, I have it on the agenda, it's the issue,
This is… definition for… Tilt definition, I think there is some good discussion there.
Nothing to bring here.
Oh, cash tokens.
I didn't have a chance, but let's also… Feeling kit.
Okay, everything is linked to this issue.
Wonderful.
I… this is something for people to review. It seems, Alex, you had some Get back…
Okay, there are a bunch of things that probably need to happen.
Alex Hall 00:05:43 Am I correct that? In the terminology here, opt-in means the user opts into this when configuring instrumentation?
Liudmila Molkova 00:05:53 Yeah.
Alex Hall 00:05:54 Right, so yeah.
Liudmila Molkova 00:05:57 Yeah, I agree with you, this…
Oh, quite, what else do we have?
I want to make sure we have it on the agenda of workflow.
energetic system metrics.
Do we have folks here who want to talk about this today?
Bye.
Don't see them, so if you come back, please… if you come…
If you're here, please add it to the agenda, and we'll make sure to talk about it.
Okay.
Let's get formally started.
If anybody wants to introduce themselves, go ahead.
Zach Groves 00:06:54 I can introduce myself.
Hi, I'm Zach Groves, I'm, from Datadog.
Specifically on LLM observability, and we've just been doing some work around, GenAI attributes and mapping them to Datadog attributes, stuff like that, so I've been, pretty up-to-date on the specs and stuff, and I thought I would start coming to the meetings.
Yep.
Liudmila Molkova 00:07:21 Jay, great to have you.
Srinivas Kommoori 00:07:24 Hi, guys, this is, Srinivas Komuri, I work for a company, Geekomon. We are a deep observability pipeline company, so…
Happy to contribute, as this is my first meeting, so…
We'll… we'll be learning as… as I go.
Liudmila Molkova 00:07:39 Wonderful.
Thank you. If you're interested in anything in particular, please, add things to the agenda. The agenda is open to everybody. If you're…
interested, like, in any of the particular work, the best way to start contributing is by reviewing for requests. We have tons of them, and you can pay attention to what concerns you, and, like, be…
you can definitely, pick up issues or create new issues. Go for it, but if you ask me what is the way to contribute for request review is the one.
Okay.
Anybody else wants to introduce themselves?
Then let's move on to the agenda.
Okay, Ankit, do you want to talk about the built-in tools? I think we started the discussion last time, but I don't remember where we stopped.
anksing 00:08:43 Yeah, I think, so, there were, like, two open things that came up. One was about…
I think there's a comment from Aaron about, like, can we have a different part type? Like, part?
Which can represent, like, built-in tools separately and not extend the tool call one.
That's one thing I want to talk about, and the second one was about
Can we have a generic code interpreter or, like, some of these common tools in a gen… represented in a generic way versus vendor-specific?
And I think these are the two bigger…
like, questions that came up, so just wanted to discuss. And probably we can start with, with Aaron's comment about, like, if you have a flattened…
A representation of it, and have a different part type.
Yeah, so, yeah, I thought about this a bit, and I think,
there were two questions that comes to my mind when I think about, like, flattening it. One was, like, most of the tool calls have few properties in common, like…
Liudmila Molkova 00:09:50 Tool call ID…
anksing 00:09:52 And, probably even name to some extent.
And those common properties could be a part of the toolCall object itself, and then if we have a property called toolCall within that tool call part to extend what specific tool it is.
That kind of helps.
So that was the reason why I went with this.
This approach, rather than having a separate part.
Type, specif- which is, like, specific to a… the tool.
Hey, hey, Alex, yeah, please go ahead.
Alex Hall 00:10:27 So… Previously, I…
Thought that the right approach here would be to have a tool call and a tool call response part.
Because I liked it resembling normal tool calls. But I'm not sure about that anymore. In particular.
So, for example, OpenAI Code Interpreter, you know, there's one item in the response, and it…
And it contains both the arguments and the response, and to… to say…
You have a call and a response essentially means defining which parts of that Code interpreter part count as…
call and response, and it's like, well, you have to specify anyway, and you're back to square one of now you kind of need a spec for every part out there, or you have to…
Rely on the instrumenter to, sort of.
guess… I mean, not really guessing, I suppose they can tell which things are input-ish and output-ish, but…
I don't know how one specifies that.
Properly.
anksing 00:11:36 So… so for the OpenAI, I know, like, Code Interpreter specifically defines, like, there's an output field, like, and it's kind of, to some extent, a part of it is optional, and you really have to ask it to give you back those things.
Yeah, if you open that… thanks, Lamila. Yeah, if you go to the two, yeah, responses, and then…
the output and the tool call, one of the… actually, if you go to the code interpreter one, I think that's,
Yeah, right, right there.
They could have sorted it. Yeah, so the outputs field is there, right? So it's specifically.
Alex Hall 00:12:18 not Tail.
anksing 00:12:20 Sorry?
Alex Hall 00:12:20 But…
anksing 00:12:21 Yeah, outputs is clear, but code, container ID, status.
Alex Hall 00:12:25 I mean, yes, I can look at these and I can tell.
anksing 00:12:28 No problem.
Alex Hall 00:12:29 what makes sense, but do we specify things that feel like input go into the call, and things that feel like output go into the response? Is that reasonable?
anksing 00:12:43 To me, yes, it does feel reasonable, because, like, I think there was another reason why we wanted to go this way, was to make sure that the
function tool calls and these tool calls, they look pretty similar, right? Because at the end of the day, these are the tools that are being called with some inputs, and they provide some output, right?
So, for the function tools, it's pretty…
like, clear on what the inputs are, what the outputs are, but yeah, I agree here. It might not be that clear, but here we can say, like, outputs are pretty clear, right?
So, and would we want this representation to be consistent across both?
And my feeling would be, yes, that would make things easier.
Liudmila Molkova 00:13:23 Why do we…
What is in common between, function2Call and Condor interpreter tool call? Is there really something in common?
anksing 00:13:34 Something common.
Liudmila Molkova 00:13:35 Like, why do we want.
Alex Hall 00:13:36 conception over that.
Like, if, if you represent… built-in tools as… same as function tool calls, you can expect
the… the backend and… Whatever a front-end it has to…
reasonably interpreted. If you have something nice for displaying function tool calls, then it will naturally display these as well.
Liudmila Molkova 00:14:06 Yeah, but as we see, for the function tool cost, we would have, hopefully, a span, and we would have
As you mentioned, the input and output, and for the built-in tool called We, in generic case, get…
just a… Something.
Alex Hall 00:14:24 Well, it depends on the provider. I think in Google, you do get two parts. You get a separate call and response.
Liudmila Molkova 00:14:34 I see. Okay.
Dylan Russell 00:14:41 Yeah, I think for Google… Like, the tools are called under the hood, for the built-in tools.
You just kind of see, like, the response, but you don't know… You don't actually see…
The tool call invocation.
Aaron Abbott 00:14:58 I sent a link in chat, actually.
Liudmila Molkova 00:15:00 Oh, thanks.
Alex Hall 00:15:03 There's an executable code part, and there's a code execution result. So there, they already separated.
Which…
Aaron Abbott 00:15:12 If you scroll down a little, you can see the response.
Alex Hall 00:15:14 Yes.
All that, yeah.
Dylan Russell 00:15:22 So you can see a response, but can you…
Is there anything that tells you that it was, like… called…
Alex Hall 00:15:33 Well, again, here, you kind of have to… if you wanted to map these, you'd kind of have to…
somehow specify which… parts become…
calls in which paths become responses. Executable code would be the tool call, in a sense, and code execution results is the tool call response.
Do we try and, like, specify this for everything, or tell intimiders to use judgment?
Liudmila Molkova 00:16:00 And we can outline the… generic pie.
And… that… So what, what, what's common? That there is a…
the result, at least, right? It's guaranteed.
Alex Hall 00:16:23 Well, they have different shapes.
Liudmila Molkova 00:16:25 They have different shapes, of course.
Let's see…
Xander Song 00:16:47 Could I maybe ask a really high-level question?
I'm sort of wondering,
In terms of adding support for built-in tools.
I think Alex was maybe alluding to, like, one… Reason, which would be, like…
you wanna… you wanna see them in a way that's, like… or you wanna display them in some UI that's, like, different from…
how you display normal function calls.
Or maybe that's one thing that you might want to do.
I mean, I guess the other thing that you might want to do would be, like.
Just be able to easily, like, re-invoke the,
Bespoke tool in some way, like, from… maybe from, like, a playground or something.
I guess…
Yeah, I guess I wanted to kind of clarify, just… maybe that's a little bit of brainstorming there, but, like, what is it that we're trying… like, what are we trying to accomplish by, like.
creating… Specialized attributes for… for building tools and distinguishing them from, like, function tools, I guess.
Those are two things I could think, yeah.
Alex Hall 00:17:53 we get requests about this quite a bit. Being able to reconstruct the actual request from the telemetry is very valuable.
Xander Song 00:18:05 Yeah, I agree. I agree.
So, so I think that's maybe one of the… one of the things that we'd like to do, so that, like, observability platforms could, from the telemetry.
like, in a playground, like, actually, maybe directly invoke a tool, for example.
Or so that the user just is able to, like.
Have a record of, and be able to re-invoke it themselves.
But then, as I'm… if that's the goal, right, then part of the challenge is just, like.
this is… this is, like, a very vendor-specific thing. Like, OpenAI has a code interpreter, Google has a code interpreter, but they don't…
necessarily look all that similar in terms of their API.
So I almost wonder if it's, like, a vendor kind of situation as well. Like, maybe there's, like, some kind of, like, built-in type, but then there's, like, a vendor…
Set of arguments or something.
Liudmila Molkova 00:19:04 Yeah, that's a great point, and I think that maybe it's a mixture. I, so, you…
Let's… let's set the exact match discussion aside for a sec. I don't think we can commit to, like.
Being able to record everything exactly as it happened.
But, let's… Think about how we are…
part parts. Do we need to record them in some way? Yeah, probably we don't have means today. We have a generic part.
Is it good enough?
And what we can record at first, we… it should be… Obvious that it's a built-in
To call, right? If we can recognize it.
it would have some arbitrary vendor-specific properties.
Does it need to have anything in common.
Maybe not.
anksing 00:20:15 Are we discussing, like, the common part, just related to the tool, what input and the output of the tool, or…
Like, just tool call, in general.
So, for example, like, for the tool call, there are some properties which are kind of generic, applies to any tool call, like tool call ID.
And probably a tool name at some point, right?
Liudmila Molkova 00:20:39 There is nothing…
anksing 00:20:42 Oh, in the butt.
Liudmila Molkova 00:20:43 Yeah, right, right. So, like, this is the… let's say it's a Google version.
anksing 00:20:48 This is the…
Liudmila Molkova 00:20:50 Sorry if my screen is too small.
This is the OpenAI version.
of the same tool call. Would it be helpful, like, the code interpreter, we should know that it happened, we should know that built-in tool call happened.
I don't even know.
If we would… Have a good time distinct, like, extracting it from the… Google.
Aaron Abbott 00:21:25 I mean, I think this one in particular, you could come up with a structure.
like, you might have some fields which are only used by OpenAI, some fields that are only used by Gemini, but…
Like, they both have code.
They both have a result, right?
Alex Hall 00:21:43 I mean, I think that a generic It's like code interpreter pods.
would be very useful. I'm concerned about the… just the broad… broader set of… of built-in tools.
Aaron Abbott 00:22:01 Yeah.
Liudmila Molkova 00:22:01 Okay, so…
Aaron Abbott 00:22:03 Yeah, I was just gonna say, I agree, like, I think we should do… we should start small, and have, like, a way to add more, and do it kind of case by case, but yeah, code interpreter is clearly something that…
Could probably be generalized.
Alex Hall 00:22:17 Like, yeah, it's worth unifying across OpenAI and Google, and then, like, for example, the front end knows that this is code, and I should syntax highlight it.
Okay.
Liudmila Molkova 00:22:31 So let's say we have a list of tools, a subset of tools, of built-in tools that we will generalize.
Bye.
Is it fair to say that in the meantime, the rest of them will be captured as generic parts?
We do have generic part, right? We would capture something as generic part, or wouldn't we?
Alex Hall 00:22:54 I think that… We do want to be able to capture all kinds of tools, and…
I guess we can still, like, stick to the code interpreter.
In case as an example, you know, if we just imagine that we're not planning on
Making some kind of code interpreter part in OTel.
We can still, like, look at that Google case or the OpenAI case and think, okay, well, how to make this into some kind of generic
Catch-all thing.
Liudmila Molkova 00:23:26 Oh, so we… we don't have a generic part.
We have tech support.
Alex Hall 00:23:31 country.
Aaron Abbott 00:23:32 We do have one.
Alex Hall 00:23:42 Just, where's the union?
With all the parts.
Liudmila Molkova 00:23:46 We'll try the generic part.
I see.
So, it can have whatever properties.
So then…
it would mean that, let's say we have special case code interpreter today. Maybe tomorrow we will special case, I don't know, CLI tool execution, or, you know, external server request, or…
bad examples. Anyway, so we will, we will,
Provide a special convention for another.
built-in tool.
File search, yeah, good example.
It would then turn from a generic part to something more… Specific.
It will be a braking change, I'm not worried about this braking.
The Beauty.
Fair.
We should… even if we go stable with this, so once we go stable with this.
I think we should somehow keep the generic parts experimental.
Yeah, Ankit?
anksing 00:24:58 Would that mean, like, say, for example, file search or code interpreter, we start it as generic part, and then we're gonna have another one in the list, which is called file search request part and file search response part? Or…
Would it be just… File search part.
Liudmila Molkova 00:25:18 I don't know, let's try to figure it out for the COD interpreter to start with.
anksing 00:25:22 Like, one part, two parts, maybe it depends on the tool, I don't know, right? If we…
Alex Hall 00:25:27 We've seen OpenAI has one part.
Google has two parts, so the same question as before comes up. Unless we had specified what to do for OpenAI and Google, would we tell instrumenters to use their judgment?
If there was a request and response part, I mean.
Would we say, okay, in the OpenAI case, split it up into two, and… Or do we say…
that the better thing to do is to have just one part, and Google parts must be merged into one.
At least that doesn't require judgment, but…
Aaron Abbott 00:26:25 I think… I think we need to, like, sit down and…
maybe just decide. So, like, I think for when I was working on this file, URI, et cetera, et cetera, I spent some time combing through also, like, the Anthropic docs.
And just writing everything out to kind of come up with the most common case, I guess?
like, I think… I think we kind of agree that they're all…
You could just come up with a rule and represent.
Like, you could round-trip everything.
if Google has, like, a rule that says we have to convert it to one part, or vice versa for OpenAI, I think…
Alex Hall 00:27:04 It's okay, we should just do whatever is…
Aaron Abbott 00:27:06 Most common for other vendors, right?
Liudmila Molkova 00:27:15 So this, to summarize what you say to Rakoy, that,
the way we can make progress on this is if we take a look at how it's done by different vendors. Like, let's just think about Code Interpreter for a second.
Let's take a look, we know what OpenAI does, we know what Google does, maybe worth checking what Entropic does, and then,
Well, that's… Make a proposal on what's common, what's not common.
And let's try to capture it.
let's say, using one part, or we can entertain the other option. Like, there are two options, right? One part or two parts. Let's entertain one option, let's entertain the other option, let's see how it maps to the three providers.
And based on this, we can make a better decision.
Aaron Abbott 00:28:09 Yeah, and then… and maybe… maybe we say, you know, like, we looked at this a lot, and after looking at it for a bunch of time, we think that one part is just bad, even if more people use it. Like, whatever we come up with, I think we just kind of need more data points.
anksing 00:28:27 And, I also wanted to, like, bring the third option, possibly, just to, like, when we are kind of evaluating all of them, about, like.
extending tool call request and tool call response? Would that make sense? Because right now, I think the tool call request and response are pretty…
Specific, or seems very tailored to function tool calls.
Liudmila Molkova 00:28:52 And if we only do this if there's one part?
Oh, sorry, there are two parts?
And if we can map this reasonably well.
Aaron Abbott 00:29:11 So, I mean, the reason I left that comment on it was, like,
I feel like when you're writing code over, like, a tagged union, it's sometimes… I mean, we can… we can generate, like, a bunch of parts with the same type, with, like, subclassing or whatever, and then it will generate the JSON schema, so I feel like when you're kind of trying to consume this or reason about it, sometimes if…
the entire tagged union is flattened instead of being multiple levels. It's a little bit easier.
So even if there's common fields.
I… at least that's my personal preference. If there's common fields, they can just be repeated across the different types, as long as… if they… if they all have a distinct type string, it's just a little bit easier to work with.
anksing 00:29:56 I see, okay. So, like, I think definitely, I think that makes sense if there are not too many, like, common fields that kind of really… doesn't really matter, like, if you have separate classes for those. However, like, the one thing that came to my mind was.
If I have to, like, kind of look at all the tool calls.
just for my purposes, then I have to kind of have these if statements, which kind of considers all these different classes to kind of figure out, okay, these are the possible tools that my agent can call, right? And… or my…
Gen AI app can call, then I have to have this, yeah.
That kind of makes it a little…
challenging, but I guess if you are, like, looking for some specific tools, that's still okay.
So if I have to, like, say, for example, and we use 10 different tools, I have to say if file search, or code interpreter, or this, like, and then…
Aaron Abbott 00:30:49 That's scary.
anksing 00:30:49 Gives me all the tools I can gather together if I want to just look at the tool calls. Not anything specific, but just tool calls.
But yeah.
Aaron Abbott 00:30:59 Yeah, I hear you.
anksing 00:31:02 Yeah, but I agree. I think, both have, like, pros and cons, you can kind of debate and make a decision, agree.
Liudmila Molkova 00:31:10 Okay, so I think we spent a fair bit amount of time on this one. Ankit, you know what are the next steps, right?
anksing 00:31:21 Yes, I'm gonna go through these notes, and yeah, follow up on the next steps, and yeah, let's chat some more next week.
Liudmila Molkova 00:31:27 I see.
next week, that we have a break in open telemetry till January 5th, so we are…
consider it a holiday. We're taking a break from all meetings, there won't be any open telemetry stuff going on, but if you… if you want to share something in the chat, maybe people will be around and would be able to take a look.
anksing 00:31:49 Oh, definitely.
Thank you.
Liudmila Molkova 00:31:54 Cool, thank you. So, moving on to the next topic, we got some great feedback from Alex on the MCP stuff. I, addressed
everything I could,
Got one approval. I see, Erin, you would like to take the final look? Go for it.
I, Dan, would plan to push for…
like, I will ask somebody from the general, semantic conventions to approve it probably next year. And let's target next year. I also want to write a blog post about this, because, yeah, we came up with a lot of, like, gotchas and,
there are things that are complicated about MCP, and the interaction with other instrumentation, so I want to maybe write a blog post and elicit feedback this way after it's merged.
Cool, moving on to the next topic, retrieval, spend support.
Josh… Do you want to talk about anything in particular? Do you want to present?
Josh Winerman 00:33:08 No, I was… in terms, I was looking over the comments he made. Thank you, Liamla, and I was just looking for some clarifications on a few of them. Most of them I agreed with.
Very good insight. I think… let me just pull it up as well on my end.
So the first one was about the prototyping. I understand that was looking for existing instrumentation. I was wondering if you might be able to help a little there?
Liudmila Molkova 00:33:51 I don't know, does anybody…
Josh Winerman 00:33:54 No, nothing, I was just…
Liudmila Molkova 00:34:01 So do we have any prototypes for this one?
It seems we do, right? But do… are they on GitHub somewhere?
Josh Winerman 00:34:11 Oh, so it's just… it's not even in just OpenTelemetry, I can just link a prototype
From anywhere, per se, or…
Liudmila Molkova 00:34:21 You can link a prototype from anywhere, if there is open telemetry instrumentation that does what you think you're proposing here, it makes sense. Oh, okay. But please, please share the prototypes, or… yeah, they don't have to be in OpenTelemetry.
Josh Winerman 00:34:37 Okay, perfect, yeah, I can do that then. The second one was about, you mentioned formally defining schema in terms of the, the retrieved docs, I think.
Can I get a little clarification? I'm a little confused by, that one, just…
Liudmila Molkova 00:35:00 So, when you… I created the attribute for the… Document… Right, this one.
So you… we just had a discussion about defining the… how the tools…
tool definitions would look like. Sorry, the tool…
calls would look like. It's pretty much similar, so when you describe this attribute, you're… you're saying,
array of objects with each object represented a retrieved document, I… think this,
Y-you- you should be able to…
what we do today is a JSON schema, right?
So, let's pull it up.
So if you look in this folder, we have, the Jupyter Notebook was…
the Python definitions, it's not normative, we also have a JSON schema for, let's say, input messages.
Josh Winerman 00:36:19 Oh, okay, okay.
Liudmila Molkova 00:36:21 So you… I would imagine that the document looks like… Sorry, it's an array.
Off.
document, where we have, let's say, ID or name.
The score, which is important.
And whatever additional properties, anything else can go here. And this is the structure you explained with words, but I think we should define it formally.
Josh Winerman 00:37:02 Okay, sounds good. So, in input messages, gotcha.
Right, and then the, the last… Well, so…
Going down to those last two comments you left, I think when I was looking at the generated span, or the generated MD for, GenAI spans, error type, and server address slash port were,
There, via the extends.
Just wondering.
Liudmila Molkova 00:37:36 Oh, I might be just having modest, let's see.
Josh Winerman 00:37:40 Yeah, no worries at all. I was just wondering if I did something wrong.
Liudmila Molkova 00:37:45 Error type is here, awesome. Server port, server address is here, awesome. Yeah, sorry, I… I just missed it.
Josh Winerman 00:37:52 No, no, no worries at all. Then the last thing was, looking over a few of those docs that I linked, regarding…
Enums that might potentially relate to, retrieval types from different frameworks, or, let's see…
Yeah, right there. Any of those? Yeah. How do those look?
Liudmila Molkova 00:38:17 So let's take a look,
So when you… when you say retrieval type here, what I understand is the…
Josh Winerman 00:38:31 I don't understand what it means.
Liudmila Molkova 00:38:34 So, here, the retriever type, it's… Any.
thing here. It's just the type of the class.
Right.
Josh Winerman 00:38:48 Yeah, so I'm sort of trying to clarify that for myself as well, because there are,
Well, there are a lot of different retrievers in the scenario. It's here, and then, here we use…
specific…
Liudmila Molkova 00:39:08 It's like…
if he… what is that that you actually want to capture, and why? And if we don't have an answer to this question, why do we need this attribute at all?
Josh Winerman 00:39:19 That is a good thought,
Yeah, I might need to flush that out for myself a little more as well.
Liudmila Molkova 00:39:29 So I think what I heard in the past, and there are, some vendor-specific stories around this, for example, you can run Azure Search
With vector search, you can run it with the,
some, text-based search, you can run it in many different ways, and there is an enum that effectively you set, and there are a lot of things that depend on it. It effectively clarifies the… not the type of the retriever, but the type of the search underneath.
I think it's vendor-specific, or there are different, when vector search happens, you have different similarity metrics, and some people want to capture this, but this sounds like a sub, type
Of the vector search, and it might not be, reasonable to bring all the different
Functions, and algorithms, into one huge enum.
So, I mean… if you…
like, the way I would suggest
Doing this, is we take it away for now.
And you can make a progress on this PR without necessarily introducing this attribute, but you can introduce this or other attributes
As a follow-up, if you still need them.
Josh Winerman 00:41:00 Okay, yeah, I think that sounds good.
That's all from me, then. Thank you so much, Liam.
Liudmila Molkova 00:41:07 Yeah, thank you.
Cool, okay, moving on to the next one, I already mentioned that there is a hotel-wide meeting, break till January 2nd, so we'll see each other on Gen 6 next time.
And yay! Happy holidays!
Aaron, do you wanna… Talk about new semantic conventions for inference.
Aaron Abbott 00:41:40 Oh, yeah, yeah.
So this is, you know, mostly talking about the overhaul we did a couple months ago. I wanted to get, kind of, feedback from anybody if they have it.
Like, if anybody's adopted it, at their companies, heard any customer feedback or anything like that.
So I was just also going to share, we've kind of adopted this at GCP, so we built a UI on top of this data model, and, specifically doing, like, the… I think I have a draft semantic convention PR open for the
Uploading bit, which, allows uploading to, like, you know, external storage.
In the more simplistic way that we talked about, so it's just uploading the, you know, proper response system instructions separately, not doing any fancy deduplication or flattening. So I'm happy to do, like, a demo of this in the new year, but I wanted to kind of get feedback or see if anybody's adopted it, plans to adopt it.
Yeah.
Liudmila Molkova 00:42:44 That's exciting! Yay!
So cool.
Sergey Sergeev 00:42:48 And, is it, is it some part of your, observability…
UI, or whatever you do on the Google side.
Aaron Abbott 00:43:00 Yeah, yeah, yeah.
Yeah, I think there might be some screenshots in here, but basically, we've built a dedicated viewer in, like, our Cloud Trace Explorer, which is, yeah.
a trace viewer, so you can see, kind of in addition to, like, having a nicer format for just showing the Gen AI stuff, you can see the chat history.
historical messages. It will render, like, images, videos, et cetera, right?
And, since the things get uploaded to GCS,
with this, we have what's called a GCS external table.
or sorry, BigQuery external table, which lets you look at
the actual stuff in GCS and link it with logs, which we make available in BigQuery as well. So there's kind of, like, a BI portion, and then just the trace viewer is completely updated to show the historical data.
Sergey Sergeev 00:44:00 And, basically, so, you can upload it in instrumentation in the YouTube GenAI using FSpec.
Aaron Abbott 00:44:13 And.
Sergey Sergeev 00:44:15 Permissions are set, basically, on the agent,
To upload there, and then your observability suit.
Using those permissions. Just trying to think through how generic Can it be?
Puaso providers.
Aaron Abbott 00:44:33 Yeah, so all of this stuff is in Contrib,
So the only kind of experimental bit that's not in the conventions is the…
the upload hook format, but you can… it already works with, like, S3, or you can even write, like, local files to disk.
you know, we can add additional uploading adapters and stuff like that, but I want to emphasize the main part here is that we're using the JSON schemas
As the thing powering the UI.
And as a thing that we capture.
Sergey Sergeev 00:45:04 Nice.
Aaron Abbott 00:45:05 Okay.
Liudmila Molkova 00:45:11 Yay!
Aaron Abbott 00:45:14 Yeah?
So, I mean, I can share some feedback, or maybe we could do it after the holidays,
In terms of, like, I can do a demo also, but does anybody, like, have plans to adopt this? Any other vendors adopted it?
Customer feedback, etc.
Liudmila Molkova 00:45:34 I haven't heard anything except what I heard from Sujay on your site, but I would love to hear if people are using it, if they find it helpful, and if you have any feedback, yeah, I mean, I would love it.
Aaron Abbott 00:45:50 Yeah, I'll see if I can get Sujay to join in the… in the new year. He's out on…
On, holidays, but, yeah.
He would… he would have more customer insight than me.
Liudmila Molkova 00:46:03 Awesome, and if you do a demo, it would also be great, yeah.
Okay, we have 15 minutes. Pavan, Ritema, do you want to talk about this one?
Ridhima Satam 00:46:17 Yes, you know, so,
The background here is last time we had a proposal for workflow and sessions, and we have combined here this time, because people were having a question about why session ID is not part of… why it is not a workflow ID. Pavan can also talk about the session ID, but briefly, just want to…
say, mentioned that I think workflow…
we spoke about it briefly, and the team here were positive about it, but just that I had to polish it with a couple of, examples there. So,
I spoke about there was this Anthropic blog post, like, a year ago, where they have mentioned different workflow patterns, and I have added the link. Maybe I can share for a bit?
Liudmila Molkova 00:47:07 Yeah, of course.
Ridhima Satam 00:47:21 Okay, can you see my screen?
Liudmila Molkova 00:47:27 Yep.
Ridhima Satam 00:47:28 Thank you. So,
mostly, it talks about the LLM patterns over here. I think it's an year-old post, right? So…
it's talking about different patterns here, and the basic terminology of workflow we wanted to get through was what would be a workflow? So, it's like orchestration of multi-agent through a predefined path. So, there are some patterns which are routing and parallelization and secret… sec…
sequential orchestrated. So they have mentioned those, and just to coin that into other frameworks, like we said last time.
in… in Creo AI, there was this Creo kickoff, so there is this outer layer where we can add that workflow span, create a workflow span for overall multi-agent orchestration. And similarly, like.
In the other framework, which was, I think, yeah, that was the Creo AI, and then LandGraph was the…
the root chain, and aaron also pointed, and then I have also added that link in the… in that same proposal about the ADK agents, like, they have this workflow agents, which are similar to, like, SQL parallel agents, which orchestrate… which are orchestrated in these patterns.
And then Alex had a question about, what about the OpenAI agents, and then OpenA agents also have similar thing, like, you can add, like, a…
trace for multi-agent runs, so that can be captured as a workflow. So, we have this proposal in here. Okay.
where, we have, yeah, coined this concept of workflow span. We want to have,
the name of the workflow description, and then the framework name. So this is very bound to a specific framework, so every…
framework would have its workflow, it's not across frameworks, it's just going to bound to one, one framework. And then we have added the session ID, and Pawan can speak more about it, like, it's kind of a top-level body where you can have the session ID across multiple workflows.
That's the idea here.
Alex Hall 00:49:48 I'm concerned about this event attributes section. When you say events, what do you mean by event?
Ridhima Satam 00:49:56 I think it's just the… the log, if you want to provide, on this, the input message and the output message, the content capture.
Alex Hall 00:50:09 Is the input and output of the workflow different from the input and the output of the… whatever…
LLM spans happen within, is the idea that this is, like, the top level.
Ridhima Satam 00:50:21 Yeah, it's the basics, the beginning, the interaction, what you have, the interaction, input message you have, that would be for the workflow.
And the output, finally, eventually, which will be generated, would be on the output message.
Alex Hall 00:50:40 I mean, the workflows even always…
have that kind of input and output. I imagine one could have a workflow that just accepts
Like, a sort of function arguments type of thing, and also that outputs would typically be one thing rather than a list of messages.
Ridhima Satam 00:51:01 So, some of the,
agent, agentic frameworks, which we, did some POC with, like, we were able to get.
The input and outputs on those, like, at least the frameworks provided those.
For the interaction, examples, yeah.
Liudmila Molkova 00:51:27 I remember last time we talked that,
In some cases, you know it's a workflow. In some cases, you don't, and it's just the invoke agent span.
And I think… Yeah, we talk that when we can, no, it would be useful to separate them.
I mean, can we have the best of the both worlds?
We kind of have the… The workflow span is pretty much the same as the invoke agent span.
With the difference being that you have a workflow name and a workflow description.
Which are… To some extent, the outer agent name and outer agent description.
can we just… When we know it's a workflow.
add the corresponding, I don't know, an attribute or some distinction in the invoke agent span to say, okay, this is the outer workflow.
Sergey Sergeev 00:52:30 Yeah, I was wondering about the same and the best, I could come up, on differentiation, so,
in some frameworks, or some agents, developers use workflow, As a deterministic, steps.
of different Gen AI operations, and, use it kind of like a runbook, let's say. You have an agent.
And it's usually an arcus data pattern with some tool usage and etc. And then, it can…
Decide to execute a workflow.
Which is, basically a static
Set of actions, and the reason why you want to separate workflow and agent, because you want to monitor for specific workflows.
How often they were used, how long they took, and etc. And basically, to have separate set of metrics.
innovation to workflow and agents. So, agent trajectory is dynamic.
Workflow is static, so you don't need to do those types of metrics.
Liudmila Molkova 00:53:50 Yeah, so what I'm saying is, you have… you have… okay, we have invoke agent operation.
We could have a workflow operation.
Sergey Sergeev 00:54:03 Yeah, yeah.
Liudmila Molkova 00:54:04 Operation name is a workflow, and then there is a separate metric, which is specific to the workflow, or you can…
That's a good question. Should we…
We could merge all, and we do merge all the… metrics into… Gen AI.
operation.
A genetic client operation duration.
And either the workflow duration is the metric filtered by the operation name, Let's set the workflow where…
It's a separate metric.
Yeah, Erin?
Aaron Abbott 00:54:50 Yeah, I was thinking about this a bit, and I feel like it would be better to do separate metrics in the future, especially for the histogram metrics.
And one big reason is, like, the…
it makes it difficult to target with views, and also makes it so that they all have the same default buckets. Yeah.
Sergey Sergeev 00:55:10 Yeah, Aaron, so two options, from my point of view. So, we can have separate metrics, basically, created at particular
Span, let's say we have workflow, Action or, agent invocation.
However, the challenge is that, whatever creates the metric, it will need to… basically to parse the graph, so if you want token usage by agent, or token usage by workflow.
You, you would need to, drivers.
All the child's parents identify all, invocations, and basically, to collect that information to create the metric,
If we can extend, our manification metric with just those specific attribute names, so it's easier to push down to the child,
Spans.
those attributes, and I think this is what TraceLoop is doing. This is, what on the Splunk side, we were doing with
our extension… OpenCelemet, so I see two options here, and… It's hard to… bubble up.
Token usage from the child.
Spence. I don't think it's possible.
But it's easy to push down, to the child, LOM and vacation agent name, and workflow name attributes.
Liudmila Molkova 00:56:48 So what you're saying that if, everything stamps the workflow name.
Sergey Sergeev 00:56:57 Yep.
Liudmila Molkova 00:56:57 than, including the LLM spends.
And you can kinda… Query. Oh, I'm only spent… where the…
That belong to this workflow for their attribute… sorry, for the token usage.
Sergey Sergeev 00:57:15 Yes, yep.
And interesting, interesting, edge cases when you have another workflow, sub-workflow of the workflow. So, what we realized we should do, if a workflow name suddenly changes on one of the spans.
If you set a new workflow name, different from the parent, so you basically start, to push down
That sub workflow, it's…
Alex Hall 00:57:43 But then, sorry, so I think there's a way to do this, which is with baggage.
I don't… I don't see what the alternative is, because we can't ask every instrumentation to…
Check for the current workflow.
Sergey Sergeev 00:58:03 So, what we can do for instrumentations is basically to provide that UTGNA functions.
Which will, help.
Doing it and maintaining it, Yeah, but, it's definitely a challenge.
Liudmila Molkova 00:58:22 It's also…
Sergey Sergeev 00:58:23 Highlight that there are two options.
Liudmila Molkova 00:58:25 it would be limited to the single process, but I would imagine that workflows
Will, at some point, be distributed.
If not already.
Sergey Sergeev 00:58:34 Right.
Aaron Abbott 00:58:38 Yep.
I am just sharing a PR here that a coworker sent for…
the Google Gen AI instrumentation, which is used, like, internally for ADK, so…
Yeah, I mean, they're not trying to propagate across the wire in a distributed way, but, like, a single context key to push stuff down, because I think we already have in the conventions the conversation ID on the inference spins, to your point, Sergey.
So this was kind of the way to implement it. It's not merged yet, but…
Yeah, if we wanna… if we wanna propagate it, then yeah, I agree, baggage.
Definitely is the way to go.
Liudmila Molkova 00:59:17 Okay, so we have 2 minutes left. I think what we, R… Have consensus on that workflow
Is long, and wouldn't… Work, as a part, generic metric.
What?
It's also true for the… Agent and vacation, but let's… let's keep it separate.
I'd like to entertain the idea of merging the workflow and Invoke Edge and DOE.
And maybe take an adjunct.
Away from the metric duration, because it's already long.
Structurally, I don't think it's a… it's… it's… it would change much, because the workflow here is the operation name, and we should record it as an operation name.
But what I also heard, that the agent name and workflow name are inherently different, and you would push workflow name down, so you would be able to stamp it on the things under.
In addition to Argent name, maybe.
Sergey Sergeev 01:00:44 Yeah, I think just, workflow name, and, yeah, I still see, benefits of having a different operation name.
for invoke workflow, And basically, to push down that, workflow name.
Don't just stick.
Liudmila Molkova 01:01:11 Okay, so then,
this proposal kind of makes sense to me. I think we need to talk a bit more about the session ID, but if it's the same as the user session ID, then it's effectively already opt-in. I, well…
let's just talk about it, at some point. But the workflow span…
Makes and metric makes sense to me.
Aaron Abbott 01:01:45 Yeah, I still kind of have the question about, for ADK, where there's workflow agent, so you get invoke agent for the workflow, but I think…
We can, yeah, we can chat offline or next week, or after holidays.
Right?
Liudmila Molkova 01:02:04 Cool! Dan, it was a great year. Thank you all for being here. Welcome, new people. Hope to see all of you in 2026. Enjoy your holidays.
Aaron Abbott 01:02:14 Yep.
Sergey Sergeev 01:02:14 Have a good evening.
Merry Christmas and New Year.
