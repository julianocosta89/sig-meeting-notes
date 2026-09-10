SIG: GenAI Semantic Conventions and Instrumentation Stability
Date: 2026-09-09
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 02:22 Hello, hi everybody.
**Bernardo Augusto García Loaiza (Albert Heijn)** 02:31 Hello.
**Trask Stalnaker (Microsoft Corporation)** 02:34 Hey, folks.
Ludmila!
I was going to ask if you would mind driving this first meeting, since you have given much more thought to this.
Yeah, sure. Better framing and…
**Liudmila Molkova** 02:56 Yeah, give me a sec, I'll just figure out my, this current situation.
Okay.
So yeah, welcome to our stabilization effort.
What we are… planning to do, what I hope to achieve, is that, we identify some part, reasonable part, of GenAI Semantic Conventions that we can call stable.
We probably will need to spend some time today agreeing on the scope.
But it should be something meaningful, it should be something implementable, it should give reasonable observability for end users.
It probably won't include everything.
And we're… Would try to… Make all the breaking changes that we are aware of up front.
call it stable, and then reserve the right to maybe have V2 at some point in the future. It may be months away, maybe years away.
There is no plan to, like, make one. I don't think we need a schedule, but… Given how fast AI evolves, we probably would want to make some breaking changes at some point.
So, I kind of want to be a little bit more relaxed here than in the previous efforts that we've done with Trask on HTTP or databases, where domain is super well known, and there have been years of semantic conventions beforehand, and a lot of prior art, so we could be much more conservative in what we And strict in what we call stable.
Here, my… First couple of thoughts is… That we're… start with… Two things. The first, obviously, is inference.
And the second thing is probably, the… some basic Agentic layers, which ones we probably need to decide and agree upon, but, like.
Even though, we could start with just inference, a lot of things that we work on these days are Agentic.
And we probably are ready to document at least the basic building blocks for agents.
And it… it creates some additional… like, the choices we make for our agents are important for inference, too, so I think we couldn't even stabilize inference without stabilizing some parts of the Agentic flows, like, I don't know, the agent name, for example, that we want to stamp, or conversations that are not necessarily part of… In the video inference call.
So yeah, that's MeshPill. Let's… target these two layers, swagli.
Let's find the issues and, Concerns we have, let's address them.
That's called stable, and… Work on the instrumentations.
Anything anybody would like to add, or any concerns?
**Trask Stalnaker (Microsoft Corporation)** 06:48 Alright, there, Dylan.
Look like…
**Dylan Russell** 06:55 Oh, sorry.
I was thinking.
That sounds good to me.
And we're planning to meet 3 days… A week.
**Liudmila Molkova** 07:11 Yeah, so…
**Dylan Russell** 07:12 times a week.
**Liudmila Molkova** 07:15 Yeah, so, how we tried in the past… So, this is… there are two reasons for this call. The first one is more like a stand-up, right, what we worked on, and how we can unblock each other. We would probably spend some time reviewing PRs, the three little ones, and also having the hairy discussions on, some important points.
We would also triage issues here, like, we would say, okay, this is probably a possibility. So, it's more like work check-in, and a little bit less than design discussions, but there will be probably a mix of both.
And, like, it's a good forcing factor to, okay, I promised somebody to review this PR or send this change, by, by whatever, Friday, so let me actually work on this, or tell my AI to work on this.
**Trask Stalnaker (Microsoft Corporation)** 08:12 Yeah, we found this useful in the HTTP and database semantic invention, stabilization efforts.
Where… At least for the first couple of months.
There's just, like, a lot of… churn. There's a lot of backlog, a lot of just kind of checkpointing, and it really makes things move… helps us to move things along faster than, weekly, check-ins, kind of keeping us all accountable.
But to that point, I mean, if, you know… If you just want… for folks who just want to follow along this effort, you know, it's not necessarily… we will provide updates in the general, weekly meeting, sort of, of… sort of progress and things that come out of this meeting.
**Dylan Russell** 09:14 Right. I mean, it seems like… Maybe a lot to me, but… We can try it.
Men.
Maybe you guys know better than me.
**Trask Stalnaker (Microsoft Corporation)** 09:28 It is, so what it comes out of, historically, the first couple of times we tried to do stabilization efforts in OpenTelemetry, in Semantic Conventions, the… we tried to do HTTP stabilization effort, like.
At least two times, strewn out over, like, A couple of years.
And it was just… So slow for a variety of reasons.
Like, there's a lot of… stabilization is particularly not… like, you have to make decisions and stick with them, and be… kind of commit to them.
And that can be something that, in OpenTelemetry, we are… Very, as a community, have had trouble with.
As you see, the number of things that are still not marked stable across open telemetry.
So yeah, it's kind of a forcing function out of… learned… problems.
**Liudmila Molkova** 10:38 Yeah. But here, we kind of want to try to have RC by KubeCon, so, like, 2 months.
Literally.
It's… it's going to be intense, and, like, this is the way to make progress. And, of course, it's, the date we came up with, right? But it's also, we had these discussions with Open Inference, and we had this prior community feedback that we were so slow.
And that's why the ecosystem is fragmented, and this is our way to show the community we can actually achieve some important milestones, with reasonable timeframe, not the startup timeframe, but still quite reasonable and fast.
And we kind of have all the pieces in place. We've been talking about Stability for months. It was in our 2026 roadmap for the SIG. People were interested in this, and here we are, it's September, and it's time to actually do this.
Cool! So with this.
**Trask Stalnaker (Microsoft Corporation)** 11:53 Iwa.
**Liudmila Molkova** 11:54 Yeah, sorry, yeah.
**Iwa Wong** 12:01 Yes, yeah, thank you, for, letting me… I mean, starting this, civilization effort. So I'm curious, like, is there any existing design that, OpenTelemetry has been working towards. I'm curious, where is the… where we're at with consensus-wise across the community. Just wanted to see how I can best contribute, as part of this effort.
**Liudmila Molkova** 12:35 You're asking about the designs, in which context? We have a couple… well, more than a couple… a few stable semantic conventions here in this repo. You can look into HTTP databases. Me and Trask and some other folks being involved into this heavily, and we're kind of bringing the… The things we'll learn there to hear, and try to repeat the process we've done before, but was in a better way.
Like, throughout this meeting, so we'll be, like, going through the issues and pull requests, and there will be a lot of things that, you can, volunteer to work on, if you would like to.
Or just participate in discussions, do the research, like, there are different ways to get involved, to implement prototypes in existing instrumentations, So, there are a lot of ways to contribute, and if you stick around, if you have time, there will be a lot of opportunities.
**Iwa Wong** 13:36 Yeah, I am particularly interested in, if there is, like, an industry standard in, observing, bad agents from doing things.
And that's why I've been, trying to insert myself in these discussions. But what I do not have a good grasp on is, where are we at, in the industry-wise, because I can see, like, for example, in topics versions of, agents, they spend a lot of time on memory, versus, like, OpenAI ones, they don't. So… and, like, there are multiple designs that got sent my way, that says, hey, I mean, this is D-Spec that we wanted to.
to implement, but, like, when I asked further, where the consensus-wise, like, that there isn't really, a why consensus, that's my understanding. I just want to check with you guys, because, like, I'm entirely, like… I just took me less than a month ago, so I have no idea where things are at, and I want to understand, are we at, like, the consensus gathering stage, or are we at, like, like, a full execution stage? Like, I'm curious where we're at.
**Trask Stalnaker (Microsoft Corporation)** 14:55 Yeah, so, the… this stabilization effort is not across all of the GenAI Semantic Conventions.
We're going to keep this very narrowly scoped to… Domains that we already have.
a fairly… decent experience in, through that we've already, have existing Semantic Conventions in, and prototypes in, and maybe, you know, slightly Expand things, but mostly, Keeping that scope down.
So anything… but this is why we are keeping… we kind of forked these discussions out of the weekly.
Meeting.
Because there is still a lot of important stuff that has, you know, like you said, no consensus.
And, you know, we need a lot more discussions around, and so that would probably be, you know, better topics for the weekly meeting.
This meeting… the stabilization effort will probably be very scoped to… and we'll try to narrow down what exactly we mean by inference and Agentic scenarios, which… Basically, we'll need to come up with a list of spans… Metrics and events that we want to consider in scope for this stabilization effort.
But I would not ex… you know, it… we're… We want to keep it fairly core, the things that There's at least reasonable consensus around existing consensus around just maybe not naming and, you know, splitting up Metrics and, you know, sort of massaging the… the… from a semantic Conventions perspective.
**Iwa Wong** 17:01 Okay, Kala, understood. Thank you.
**Trask Stalnaker (Microsoft Corporation)** 17:07 Yeah.
**Liudmila Molkova** 17:07 Bernardo?
**Bernardo Augusto García Loaiza (Albert Heijn)** 17:08 Yeah, I do have a quick question, thanks. It's regarding the scope, when you guys say inference, is it the inference as a term in a general way, as an intelligence term, or is it open inference that it was donated some months ago? And, yeah, that's kind of the question.
**Liudmila Molkova** 17:27 Oh, this is the… Good question. So this is essentially what we would call an LLM call, but it's not necessarily language, right? Not necessarily text. So this is the… The model boundary from the client side.
Oh, okay. And it covers… Well… This is the client communication that covers way more than, like, generation of… content, right? Text, or images, or voice, whatever. But, it's probably also embeddings, and there are also some other things, like batching. I don't know if we want to cover batching, if it's a different API, probably different operation. But I think we should talk about this, and it's… It's not a quick question, but maybe we can give, like, quick answers to a specific things.
**Bernardo Augusto García Loaiza (Albert Heijn)** 18:25 Okay, clear, thanks.
**Trask Stalnaker (Microsoft Corporation)** 18:33 And that's probably, like, one of, and maybe I can spin up that issue, to… Start, sort of, adding… What we consider in scope, start at creating, sort of, the list of spans, metrics, and events that we want to target for the stabilization effort.
**Liudmila Molkova** 19:00 Right, and attributes.
Somebody added Agentic identity here. Who did this, and why do you think it should be in scope?
Can somebody who added the identity come.
**Iwa Wong** 19:19 Yes, yeah, it's a question mark, really, so for discussions. I'm curious, like, what is really in scope, in the Agentic, side of things.
**Liudmila Molkova** 19:32 Yeah, so I think what Trask is proposing, to look at the spans we have already.
And, they will… they cover two things, so, well, the tool calls are also a part of both, I think.
they are cover Invoke Agent, so it's like a turn, or run, or whatever it's called in different places.
We have the counterpart of it, which is… Invoke workflow.
It's, like, if you have a multi-agent scenario, and the other thing is not necessarily an agent or something, so this is another candidate.
I would not… include identity, because we don't have anything about Agentic identity, and I believe Agentic identity is no… nothing different from any other identity concept, maybe with a couple of additional considerations on it. So I don't even think it belongs in GenAI domain.
**Iwa Wong** 20:40 Okay.
**Liudmila Molkova** 20:41 If you're talking about the identity, in a sense of authentication or authorization.
**Iwa Wong** 20:50 Okay, interesting,
**Trask Stalnaker (Microsoft Corporation)** 20:52 like, agent name and agent ID part of the entity.
Identity.
**Iwa Wong** 20:59 Yeah, so I think I was, following, Codex, repo, like the public open source one, they recently, very recently, introduced this concept, in their codebase itself, where, each of the agents would carry their own identity, and then it's using, a whiff-style, allowing different, providers to have their own identity solution, and then, federate these access, like you mentioned, authorization side of things. So, but then, like, if we… I'm just curious, like, I mean, is there any, plans to, surface any of these, Any of these, markers, for identifying, like, really who did what and when, and who, in this case, is an agent.
**Trask Stalnaker (Microsoft Corporation)** 22:00 So, I would bring that to the weekly meeting.
Because I wouldn't expect us… this stabilization effort is really taking what is there in the Semantic Conventions today.
And, you know.
Rounding it out a bit, filling in, you know, some gaps, but really trying to keep the scope narrow.
Because that's the only chance we have of landing a RC in a couple of months.
**Iwa Wong** 22:35 Okay, yeah, I'll, I, I, I, so, I guess I don't understand what you mean by, narrowing the scope, but yeah, I'll just watch over and, And, and let the team, go from here.
**Trask Stalnaker (Microsoft Corporation)** 22:50 Yeah, and I'll get an issue open to try to, you know, with a scope, a proposal for scope, or at least that we can discuss over there.
So that hopefully that can become clearer.
But, from a practical perspective, you've seen how long these discussions take, right, for all the new things, like bringing in something like identity, or guardrails, or, these things take… Months just in that discussion and consensus building, so… That's why, you know, we have to keep the scope narrow here to… Have a chance at stabilizing, you know, some core pieces.
**Iwa Wong** 23:40 Makes sense.
**Liudmila Molkova** 23:49 Okay, we have 9 minutes left, and I'm… Thinking we can spend digging into specific topics, or we can, build some plan On what do we want to achieve by Friday?
So I think Trasky would open the issue, and with that… of the existing things, right? And you would propose some, What's in scope, what's out, what's in the middle?
**Trask Stalnaker (Microsoft Corporation)** 24:19 Yeah, I'll put something on the, on the wall that people can poke holes in, yeah.
**Liudmila Molkova** 24:28 Yeah. Okay, so I'll thoroughly do this, I'll go through… this is the AI-generated project board. I'll go through this project board, and I'll DEI it, and try to, Move things that were missed, or obviously in the wrong place.
Somewhere, and then we can compare, your list from… from my list.
**Trask Stalnaker (Microsoft Corporation)** 24:56 Sounds like a good plan.
**Aaron Abbott (Google LLC)** 25:01 No, could you say more about… about this board right now? So you just… you just have, like, an AI prompt to kind of sort the issues into, ones that need to be addressed by stability, or for… for stability?
**Liudmila Molkova** 25:15 Yeah, this is essentially the board of all the issues that we have.
And… the possibility is something that looks like a new feature. We don't have a convention for it yet, and it doesn't look like adding it would be breaking to anything we defined so far. So, like, things like VectorDB goes here, or, like, user information, right?
Yeah. So, Dan, there are things that are… Seems to be obviously in scope.
like, the… I think the segregated token usage attributes, if we're going to stabilize Invoke Agent, that we need to figure out what do we do with the corresponding, usage attributes on That's Pen.
Yeah, that's.
**Aaron Abbott (Google LLC)** 26:16 That's what I was gonna ask is if there's any… Like, there's probably some features that we still need to have, like, a… Minimum viable, stable thing.
**Liudmila Molkova** 26:26 Yeah.
**Aaron Abbott (Google LLC)** 26:26 Which are, which are net new, and that's something that we have right now.
**Liudmila Molkova** 26:31 Yeah, and I guess next time, what we can do, we can go through and agree.
On some things.
Maybe, on… I don't know what's out of scope, or what's in scope, or… And triage, like, things that are in the middle.
And, it seems we are approaching it from two different angles, and just looking at issues Trask is looking at existing things that we have.
Yeah.
And I actually, I think I found a way to… leverage the additional statuses, the stability statuses that we have. We can start marking things that are targeting stability as alpha, just as a marker that we are moving them forward.
**Trask Stalnaker (Microsoft Corporation)** 27:32 Where? Where would we tag that?
**Liudmila Molkova** 27:35 In Semantic Conventions, we would move them to alpha.
**Trask Stalnaker (Microsoft Corporation)** 27:39 Oh, the stability, yes, yes.
**Liudmila Molkova** 27:41 Right.
And then the tooling can help us,
**Trask Stalnaker (Microsoft Corporation)** 27:45 detective.
**Liudmila Molkova** 27:45 We forget about something.
**Trask Stalnaker (Microsoft Corporation)** 27:48 That's a good idea.
**Liudmila Molkova** 27:55 Whew! So then… Do we want to start any specific discussions in this call, or we will… Continue on Friday, Dave is more information.
**Trask Stalnaker (Microsoft Corporation)** 28:11 Yeah, I think that sounds good. I think until we sort of have Just a board with… that we start talking through and, scope.
Then we can… Have more discussions, more meaningful discussions.
**Liudmila Molkova** 28:31 Okay, then sounds good. Good to see y'all, thanks for coming. See you on Friday, same time, right?
**Trask Stalnaker (Microsoft Corporation)** 28:37 Thanks. Yep.
**Aaron Abbott (Google LLC)** 28:38 Bye.
**Bernardo Augusto García Loaiza (Albert Heijn)** 28:40 Thank you. Alright.
**Siri Varma** 28:42 Thank you.
