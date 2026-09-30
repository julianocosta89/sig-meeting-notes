SIG: GenAI SIG (APAC)
Date: 2026-09-29
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 01:12 Hello, good morning.
I cannot hear you. Maybe it's me.
**Trask Stalnaker (Microsoft Corporation)** 01:42 Alright, helps to turn the headset on.
**Liudmila Molkova** 01:44 No.
**Trask Stalnaker (Microsoft Corporation)** 01:45 Oh, I hear you at least now,
**Liudmila Molkova** 01:50 Oh, I can hear you, yeah. It's just very quiet for me.
**Trask Stalnaker (Microsoft Corporation)** 01:55 Hey!
**Liudmila Molkova** 01:56 Hey.
**Trask Stalnaker (Microsoft Corporation)** 01:57 Wasn't expecting to see you.
Are you back?
**Liudmila Molkova** 02:02 Yes, I am back.
**Trask Stalnaker (Microsoft Corporation)** 02:06 Have fun. I'm sure you had a great time.
Oh.
Did you have fun? I'm sure.
**Liudmila Molkova** 02:17 Yeah, I did. I just landed yesterday at, like, 7pm. I'm still not sure where I am.
**Trask Stalnaker (Microsoft Corporation)** 02:24 Yes, yes.
**Liudmila Molkova** 02:28 How things have been here.
**Trask Stalnaker (Microsoft Corporation)** 02:33 Moving along, yeah, I can… Why don't I share… can show you… Oh, Alright, so I… Created this… tab here to… Try to kind of split out work for people.
**Liudmila Molkova** 03:21 Nice.
**Trask Stalnaker (Microsoft Corporation)** 03:22 And people kind of, volunteered for… areas, This one feels like a… Big.
One, seems like a lot of things around the parts JSON schema.
Okay.
I… this is a, I saw Dylan sent a configuration.
PR to the configuration repo, yesterday.
**Liudmila Molkova** 03:56 Oh.
**Trask Stalnaker (Microsoft Corporation)** 03:57 look.
**Liudmila Molkova** 03:57 Interesting.
**Trask Stalnaker (Microsoft Corporation)** 03:58 Yeah.
**Liudmila Molkova** 04:03 Have you seen, you have seen Jack's proposal?
And our… Prototypes around it.
**Trask Stalnaker (Microsoft Corporation)** 04:13 Yes, yes.
**Liudmila Molkova** 04:16 Oh.
**Trask Stalnaker (Microsoft Corporation)** 04:18 I think the last… The last I saw or discussed was.
A while back, so… At which point… He was gonna go and try to make it more, like, a federated thing… There was something… Yeah, I forget the details.
**Liudmila Molkova** 04:42 I think he, he has some… we had some discussions, and I think he sent me something while I was on vacation, I'll go through it, but yeah, probably it doesn't matter. Like, we… it's independent how we would make things work together, but… We can do this regardless.
Yes.
**Trask Stalnaker (Microsoft Corporation)** 05:05 Yeah, I think so. I think we can… I mean, it's… it's still experimental here. General, that's a good… Yeah, when we… I want to remove the slash development here, but we would probably want to add the slash development to this node that… Then…
**Liudmila Molkova** 05:27 Oh…
**Trask Stalnaker (Microsoft Corporation)** 05:33 This is, blocking, basically, any… Stable instrument to any, stable… declarative config from an instrumentation perspective. So, declarative config is stable from the SDK perspective now.
**Liudmila Molkova** 05:48 Hmm.
**Trask Stalnaker (Microsoft Corporation)** 05:50 but not from the instrumentation perspective because of this, and I think the corresponding, like.
API to… for instrumentations to read it is not stable.
**Liudmila Molkova** 06:03 I see, so even if we wanted to declare… This configurations table, we wouldn't be able to, because there is no way to get them without Stable APIs.
**Trask Stalnaker (Microsoft Corporation)** 06:15 Yeah…
**Liudmila Molkova** 06:20 I'll get there.
**Trask Stalnaker (Microsoft Corporation)** 06:21 Yeah.
Naming… The… this is the… this is your PR.
And… So, I just… I… made, like.
two small changes and made it ready for review, and Aaron.
Yesterday said he would review, since this is basically blocking, like, all that kind of cascade of duplicative work afterwards.
**Liudmila Molkova** 06:57 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 07:05 Let's see, there… I haven't really… Discuss… oh, Neil.
No.
Oh, yeah, we might be… Worth checking for other ownership for this, because… So that it doesn't block on the JSON schema stuff.
This one is primarily, I think, the decision around the, Whether to merge the workflow.
span into… Invoke agent, San.
I don't think we've… had any.
We discussed it, I think we discussed it on Friday. I think Sarah was going to… Take an action item to try to.
Because I'm still, like…
**Liudmila Molkova** 08:22 I have a…
**Trask Stalnaker (Microsoft Corporation)** 08:22 Question. Yeah.
**Liudmila Molkova** 08:24 Mental model.
You want to share a video, see what you think.
So… Or.
There is some hierarchy.
The there is a thing people usually call turn, it's like you.
Ask something an agent, and it does the thing.
And it returns you the output. However, whatever happens inside, it is a turn.
And then there is a step of the turn.
like an LLM call, or anything, like, tool call?
Another agent, and whatnot.
And we cannot express.
Like, it's in the name, but let's say Invoke Agent and Invoke Workflow are both turns.
and invoke… But invoke agent, subagent, or… Execute 2 is a step.
And it's a little bit subjective, what's called Turn in what's called step.
And they can be nested under each other.
But… maybe… like, the proposal I have… I had some prototypes, there are some details to polish, but the… in my mental model, we should rename the… the… the… Invoke agent, invoke workflow to turn.
And then… Like, it's orthogonal, right? It's what happens, doesn't matter who does it.
And then we can use the corresponding attributes.
But I think there were some… Some tricks to make things consistent, because I think we still want To know how specific agent does.
Or know something about specific agents, and maybe we should… Anyway, I'll recall my memories, but I remember this for now. And the other thing is.
I think it doesn't really matter who does something, Agent or Workflow, but what matters if it's the outermost thing.
**Trask Stalnaker (Microsoft Corporation)** 10:56 The main agent.
**Liudmila Molkova** 10:57 Yeah, the main agent.
And then we probably should focus on this, so the outermost, maybe local, it's a turn.
Something nasty to the… Step.
But I don't… I'm not proposing to, like, have a step duration… well.
there is a PR proposing stub duration, but it's more like, okay, if it's not agent, if it's not inference, if it's not tool call, if it's some arbitrary crap.
For example, Some people do sanitization.
Which can be complicated, or… Post-processing, or any sorts of pre-post… Activities that are instrumentable.
Those are… could be steps.
Well, they appear like something.
Like, a node in a graph. Like, what is it? Who knows?
**Trask Stalnaker (Microsoft Corporation)** 12:00 So, the… Let's see, so the… outermost… So, it would be at… turn… And you would… Just stamp… it would have the agent name on it.
**Liudmila Molkova** 12:21 Agent name or workflow name.
or… It still needs some thought. Do we want to unify? Do we want to say what kind of thing it is?
But yeah.
**Trask Stalnaker (Microsoft Corporation)** 12:42 Yeah, but then it's…
**Liudmila Molkova** 12:44 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 12:45 Then it's just a… a discriminator on that span. Which I… I like. I mean… I do like… He.
I still… conceptually, I like the idea of, merging these somehow.
Cool.
**Liudmila Molkova** 13:12 I'll add my name to this.
To the tracking tab.
**Trask Stalnaker (Microsoft Corporation)** 13:19 Oh, yeah, yeah, yeah.
**Liudmila Molkova** 13:21 Pretty cool that we came up with this idea.
**Trask Stalnaker (Microsoft Corporation)** 13:25 let's see… what else can I share?
Education… And… Wolfgang has been out… I think he said he may be back tomorrow.
There was one… That… For a question for you. Oh, yes, yes, this.
So, this… Token usage, zero. Whether to record, no.
Don't use a histogram when it's zero.
So, the question was the error… Whether to only record, for successful operations.
Or to add the error type attribute.
And… So, I… I think that… let's see.
I had to… I had other preferences.
The operation… I was worried about the opera… if we leave it with this name, I was worried.
**Liudmila Molkova** 15:10 event.
**Trask Stalnaker (Microsoft Corporation)** 15:11 The histogram count won't match the operation count.
So… if we don't… I understand the… the idea that, your point, that error, like, it's the histograms.
are probably only… useful for… successful operations. Anyway, like, we either… my thought was either to rename it, if we wanted it to just be successful operation.
Or to add the error type, and… let people… Filter, if they only want successful.
**Liudmila Molkova** 15:52 Yeah, I remember I started reviewing the PR This person sent… And I came, I think, to the same conclusion that I don't… like, there are some subtle issues that introduces As well, so… and I think it's just a theoretical concern, because I don't think in practice we ever have the situation when it's… Not zero.
And there is error type.
Because it's sent… After successful completion.
And then… It's.
Like, okay, so maybe error distribution for a specific error type is meaningless.
But it's… the count of those is always zero, so it doesn't matter.
We don't, like… Aha.
**Trask Stalnaker (Microsoft Corporation)** 16:48 Can you explain the… the… Quote the thing about the history distribution.
not being…
**Liudmila Molkova** 16:59 So, like, imagine we have the… the… Option 1, your preference.
**Trask Stalnaker (Microsoft Corporation)** 17:06 Aha.
**Liudmila Molkova** 17:06 And then… Will… is there a realistic case when error type is not empty?
And count is not zero… oh, sorry, the… the… there is… Oh, for input tokens, there is.
For input… oh, we should never have… Should we have a RedType on input token server?
Who cares? It's input.
Or maybe how many tokens you are wasting on failed operations.
Maybe.
**Trask Stalnaker (Microsoft Corporation)** 17:47 Hi.
**Liudmila Molkova** 17:53 So maybe yes.
Let's pick output tokens.
**Trask Stalnaker (Microsoft Corporation)** 17:59 Okay, okay. Yeah, yeah, yeah.
**Liudmila Molkova** 18:01 There's pretty much never… a case when It's not zero for failed operation.
So… In practice, it would not increase telemetry volume, it would have… Zero negative effects.
That we have our type there.
For end users.
But it's consistent with everything else we do for histograms.
**Trask Stalnaker (Microsoft Corporation)** 18:37 Sorry, I think I'm still waking up.
Time zero… But…
**Liudmila Molkova** 18:46 So if you've got some tokens, operation is successful.
Well, if you get usage information, the operation is… means it's… operation is successful.
**Trask Stalnaker (Microsoft Corporation)** 19:08 And so, if we did… if we recorded zero… for…
**Liudmila Molkova** 19:17 In practice, we would not record… This.
was… Error type.
Oh, we will always record zero.
was our type.
in prep. Well.
There… I'm sure there are some variations.
**Trask Stalnaker (Microsoft Corporation)** 19:39 I see. And so you're saying that, the… The… Time series with error type.
Is not very interesting, because it's all zero.
**Liudmila Molkova** 19:54 No, I'm saying, like, I think not having error type creates more problems than… and it's a very minor problem from telemetry volume.
It does not… do much harm, so it's okay. But, it made me think that on the input tokens, it is very interesting.
What does it mean?
**Trask Stalnaker (Microsoft Corporation)** 20:20 Means. It means. Yeah, I think what you said, which is, I guess, how many tokens I wasted on.
But that's… Do we get that?
from…
**Liudmila Molkova** 20:37 Probably it's the same, right? So the failed operation is the one that Didn't get a response.
Object. So it didn't get the usage information.
She probably, in practice, wouldn't have it.
**Trask Stalnaker (Microsoft Corporation)** 20:59 I see. So, Operation… We would record… it at the… Send…
**Liudmila Molkova** 21:14 Oh, wait, so another thought.
If operation failed, we actually don't know the number of tokens.
**Trask Stalnaker (Microsoft Corporation)** 21:25 Hmm.
**Liudmila Molkova** 21:26 So we, by recording zero, we are kind of lying.
**Trask Stalnaker (Microsoft Corporation)** 21:38 Potentially, same with input tokens.
**Liudmila Molkova** 21:43 Yeah, with both.
**Trask Stalnaker (Microsoft Corporation)** 21:50 Well, from a consumption… From a consumption usage… perspective.
Right? I mean, like, we know on the input tokens, we know that That's the number of tokens that are… Agent.
Wanted to send.
**Liudmila Molkova** 22:14 We only know because the backend tells.
**Trask Stalnaker (Microsoft Corporation)** 22:19 Oh, you're right.
Yes.
Okay, so we get this back, so we wouldn't record it up front. Yes, we record it on the response, because that tells us.
I don't know the real value.
**Liudmila Molkova** 22:45 But in theory, we could know there are, like, local token counting libraries, maybe instrumentations could Have an opt-in value that would track them.
**Trask Stalnaker (Microsoft Corporation)** 22:58 Yeah, but that's not what, yeah, our semantics are today.
**Liudmila Molkova** 23:03 Right.
**Trask Stalnaker (Microsoft Corporation)** 23:13 Interesting, okay. So… Successful.
**Liudmila Molkova** 23:23 I think this would be honest, but like, that's so long, right?
**Trask Stalnaker (Microsoft Corporation)** 23:29 Operation input tokens.
Okay, so if we put… error type, but yeah, I… I mean, I definitely understand Okay.
What do you think? What's your… where are you leaning at this point?
**Liudmila Molkova** 24:10 No comment. Tenzapa is this metric name all the time.
**Trask Stalnaker (Microsoft Corporation)** 24:14 Because I think that, the discussion, at least to me, justifies this naming more than… what I was… Thinking before, like, this idea that, like, We don't… record it.
if we don't… I mean, essentially, we're saying we don't record it if we don't get the value back from the… LLM.
**Liudmila Molkova** 24:45 Right.
Well.
I think this, this would be… More future-proof, I'm pretty sure people want to know the usage.
Regardless if operation failed or not.
So, like, I would imagine that If it's a background operation field, it would still return the number of tokens it consumed.
And it's good to record this value, right?
If you don't record it, it says error type.
If we put that successful operation in the metric name, we would need to invent something new first.
For failed operations at some point.
But we probably should tell not to record.
Not to… not to… no.
Not to record zero when operation fails, or record zero.
So the, the edge case.
I sent something.
And I start getting a response and then it.
the stream… Terminated, for whatever network reason.
And didn't get anything back, but I know that there was an also get her.
**Trask Stalnaker (Microsoft Corporation)** 26:10 I guess, I mean, having those zeros… isn't… I'm trying to think consistency-wise, like, HTTP… say, like, an HTTP client spans… if we… durations… like, there's… A lot of times, Things can fail, like, duration zero, like, all these failures at duration zero.
And yes, that messes up… you could say that messes up your distribution.
But… It doesn't really… it's… it's act… Good.
**Liudmila Molkova** 26:59 Yeah, it can be accurate as a query.
**Trask Stalnaker (Microsoft Corporation)** 27:02 The only thing that's weird is that you're actually… you're not getting back zero. You're… you're not recording… Yeah, with duration, it is an actual duration, you're not making it up. In this case.
We don't actually know, so it seems… Justifiable to do either one, to not record it.
**Liudmila Molkova** 27:30 I don't know.
We can put this, that… You.
We have this, the option one, we have our type.
say that… Like, you record the value to the best of the instrumentation knowledge.
It might be zero, if it's the best you know.
And it allows us in the future to.
Blood instrumentations calculate tokens.
From the information they have on the client side.
And it's probably even less controversial that SQL parsing we do on database sites to calculate tokens.
**Trask Stalnaker (Microsoft Corporation)** 28:18 Yes, yes.
Okay. I… Yeah, I think I'm… good any of… those. It is nice for the operation account to match.
**Liudmila Molkova** 28:36 Yeah. Okay, I'll leave a comment on the…
**Trask Stalnaker (Microsoft Corporation)** 28:39 Okay.
**Liudmila Molkova** 28:39 share them.
**Trask Stalnaker (Microsoft Corporation)** 28:41 Cool.
Cool. See ya over in our next meeting.
**Liudmila Molkova** 28:45 Welcome back. See you. Thanks.
