SIG: OpenTelemetry on Mainframes Weekly Meeting
Date: 2026-06-10
Duration: 14 minutes
============================================================

## Zoom Recording Transcript

**Ruediger Schulze (IBM)** 00:36 Hi, Greg. Oops, thanks for joining.
**Greg Shriver** 00:39 Hi, Rudica. How are you?
**Ruediger Schulze (IBM)** 00:41 Good, yeah, I'm back from vacation, so sorry about not attending the last two weeks.
**Greg Shriver** 00:47 Yeah, no worries, I was on vacation last week as well. I think they canceled the meeting. I don't think there's any, I didn't see any notes from last week.
**Ruediger Schulze (IBM)** 00:58 No, they said they canceled it. That's… that's right.
**Greg Shriver** 01:04 One thing I did see while I was out last week was, some activity on the repository.
**Ruediger Schulze (IBM)** 01:15 on the… on the PR for the semantic conventions repository, right?
**Greg Shriver** 01:22 I believe so, yeah.
**Ruediger Schulze (IBM)** 01:23 Yeah.
**Greg Shriver** 01:25 Yeah, what is it, repository maintenance on semantic conventions mainframe here.
Who knows?
**Ruediger Schulze (IBM)** 01:38 I think it's… it's not yet there, right? It's still ongoing, isn't it?
**Greg Shriver** 01:44 It's… it's still ongoing, yeah.
**Ruediger Schulze (IBM)** 01:46 as soon as it comes online, I would try to… You know… To… to establish this process that the… semantic convention stick has been building up to test this out.
Let me see here, so what do we have on agenda?
We had the, I think this should be here. The puzzle not ready yet, so that's the same thing, I guess.
Let's check the PR if we need to do anything there.
I think they nominated us as maintainers, which is fine.
**Greg Shriver** 02:31 Yeah. Yeah.
And I think, Trask was trying to get… Antoine to be sort of bootstrap maintainer, until it gets off the ground.
But… but I don't… it doesn't look like Antoine… responded to that.
**Ruediger Schulze (IBM)** 02:49 Yeah, maybe it's also invocation or not.
It's not being available.
Okay.
**Eric Mustin** 02:57 Hey, hey, Greg. Hey, hey Rudiger.
**Ruediger Schulze (IBM)** 03:00 Eric.
**Eric Mustin** 03:01 I'm joining out of left field, so, sorry to interrupt, but yeah, good to see you guys.
**Ruediger Schulze (IBM)** 03:06 Yeah.
As we haven't met, if you have a specific topic, you know.
**Eric Mustin** 03:12 Sure.
**Ruediger Schulze (IBM)** 03:13 Shooted, right?
**Eric Mustin** 03:14 Yeah, yeah, I'll… Eric, I maintain OpenTelemetry Ruby. I'm over at Elastic these days, but I've been maintaining.
**Greg Shriver** 03:21 Oh, sick.
**Eric Mustin** 03:21 my Datadog days back in, I don't know, 2021. Not as active anymore, but… so Elastic has been working, on mainframe observability very recently. I just got out of a call with Jason Brown from IBM Rudiger, who you may be familiar with. So I actually just wanted to kind of join here and start to ramp up on… Yeah, the whole space, because I'll be honest, as I mentioned, I'm a Ruby guy, which means I, I'm a, you know, some of the mainframe stuff is a little more complex than my, my usual day-to-day, but I, yeah, I want to join here and start to understand the space a bit, and then also just, yeah, say hi and, in the event that I do have questions as they pop up.
**Ruediger Schulze (IBM)** 04:04 Good.
And just to say, what we are discussing, and what's kind of like the… Let's say, currently, the topic which is most of… on top of our mind is semantic conventions for the mainframe, and if you have been following, or maybe you noticed this, there is now this concept of Federated semantic conventions being established.
We're waiting for the repository to come online, and then we would get started to put our stuff into this repository using the tools that are available from the community. We had a, let's say, throughout the last year, we had various discussions, various attempts, various… You know, steps taken, but… I think having this dedicated Repository for mainframe semantic conventions actually will help to, you know, make better progress in defining those conventions.
We have certain things in place with spans. I think there are some discussions around metrics from a pure hardware platform perspective. Think of HMC.
as a starting point. So, and then also we had other discussions around representing CUS as an operating system, concepts of the operating system. So, We, We have high hopes that, you know, with the repository, and with this more dedicated approach, we can actually make better progress on semantic conventions.
**Eric Mustin** 05:38 Right, the idea being it's been hard to get anything merged upstream in the big monorepo, you know, SEMCOM monore… yeah.
**Ruediger Schulze (IBM)** 05:44 Yeah, yeah, yeah.
**Eric Mustin** 05:45 I think, as, you know, as long as Weaver and the like take this stuff into account, I think it's a nice way to be able to move fast without needing to… yeah.
Exactly.
getting anything done. Right. So, that makes sense to me.
**Ruediger Schulze (IBM)** 05:58 Yeah, hey, Richard. And obviously, as you're part of the community, we maintain the, you know, the estimating notes. I added you there.
We didn't have the meeting last week due to, you know, several of us being absent, but… Which just goes through what other topics we have to discuss, but as I said, the semantic conventions is… Obviously, the, the, the topic number one… We also had discussions with Antoine around Antoine as being also somebody, contributing here.
getting, Linux S390, surface chitter barnos in place.
For the collector, that's for various reasons, cumbersome process. We had an approach with IBM-hosted ones.
There were process issues, I would say, and there is still in discussion to go with the CNCF.
based approach, but that's also somehow stalled. We tried to get input there, but…
**Eric Mustin** 07:05 Yeah.
**Ruediger Schulze (IBM)** 07:05 Didn't… didn't hear anything recently.
**Eric Mustin** 07:08 Yeah, that would be… I mean, you know, I know the collector builds for S390, an AIX with Tier 3 support?
**Ruediger Schulze (IBM)** 07:18 Yeah, exactly right.
**Eric Mustin** 07:20 But yeah, any way we can have robust tests there is super helpful. I do have some… so for context, I don't work on the OpenTele… you know, Elastic is… I'm working through OpenTelemetry. I don't work on the development team, I'm an architect here, so I work with our customers. So, one is I… I do have, I think.
I do have customers who run S390 Linux, and I went through a whole mess of trying to compile the Elastic agent not to work, or a file beaten instead of this mess. So I… may have the opportunity, if we can get some stuff set up, whether to actually validate whether these things run on real boxes, you know, because it'll be actual customer, data, but that's our, you know, that's kind of why I'm joining here, is we do have some customer interest, I think We have some overlapping shared interest, Rudiger, with your employer, and we're trying to collaborate to… Make sure that they're happy, right? That's why we're all here.
**Ruediger Schulze (IBM)** 08:14 Right, it's an ecosystem effort, right? So, yeah, fair enough.
**Eric Mustin** 08:19 So I'll be, hopefully, in short.
order. I may have some actual validated data coming off of some of these machines, where we could Put the… yeah, actually see if there's whatever, if this… the traces look like they should, to be polite. But yeah, well, I guess, but again, I'm just jumping in here, so, please don't take my silence for, negativity. I just don't know what I'm talking about yet, so… Bear with me.
**Ruediger Schulze (IBM)** 08:46 Fair, fair enough, Frank, thanks.
Okay, Let's also update on… because we discussed this on one of the previous meetings, Richard, we had with the Open Mainframe project.
the discussion around… earlier we called this the collector, now I think we moved to the producer as a name. There is an idea to… a proposal to the OMP project, to… to have a more generic producer for OTEL data from the CRS platform.
This is not necessarily related, and would probably not run on the Open Telemetry project, but at the time when we discussed this, we were still in the defining phase.
So I wanted to put a little bit of clarity on this. We're not talking here about, or not talking any longer about porting the OpenTelemetry collector to CUS, at least not at this stage.
It would be more about having a component that allows easier ingestion of any… any sickness.
from, non… or from a mainframe-specific programming language.
into an OpenTelemetry protocol format using the OpenTelemetry SDKs.
This is in very early stages, Richard, if you want to commend on that, please, please go ahead, but that's the proposal.
**Richard Nikula** 10:09 It's early, and I think the… Still trying to work out how committed any of the contributors are.
To do it. And how's that for…
**Ruediger Schulze (IBM)** 10:26 Yeah, but yeah, like we said on the other call, Richard, let's put the proposal forward and then, you know, take steps by steps, right?
**Richard Nikula** 10:36 I agree, you can't… Can't do it if you don't try.
**Ruediger Schulze (IBM)** 10:40 Right.
Okay, let's see, what else?
Yeah, so, I mean, this goes back to semantic conventions. We had, and I think most of us have been actually on the call, so Ludmiller from the Semantic Convention 6 was on the call. She walked us through the approach with the federated semantic conventions.
And as we said, right, as soon as we have the repository available, we get started with this.
What was this year?
Yeah, I mentioned already the self-hosted Chitop Action Runners that's still in… in flux.
Done… We also discussed… This is about HMC. I think this was more informative the last time we discussed.
that there is… some parameters technology out there. And then for the forever in-flight TPS PR, I think we said this will then go into the dedicated semantic convention, mainframe semantic conventions.
As Antoine… actually, we are looking on Antoine to make the next step here, as he is, you know, helping us out with the… With the repository, I think I don't have anything else right now.
So maybe we would just open it up for questions or, you know, any updates that you would have.
**Eric Mustin** 12:26 Nothing from my end besides what… What we already discussed.
**Ruediger Schulze (IBM)** 12:30 Yeah.
Fantastic.
**Richard Nikula** 12:32 the… I'm sorry.
**Ruediger Schulze (IBM)** 12:34 Go ahead, Rachel.
**Richard Nikula** 12:35 I was gonna say, the proposal that you put together on the… federated model, or is that… I mean, I looked at it, looked fine.
Is that now… Fleet? What's the status of that?
**Ruediger Schulze (IBM)** 12:49 the PR for the… Dpr3432 on the community array per that's still in flight.
**Richard Nikula** 13:00 Okay.
**Ruediger Schulze (IBM)** 13:01 And, it seems like that we are waiting for… Might actually be Antoine to help us here to… Set up the… the repo, and then we can go.
And, have the initial bootstrap being done probably with help from from Antoine and a couple of others, and also using what was done for GenAI as a basis.
**Richard Nikula** 13:32 Okay.
**Eric Mustin** 13:34 If we… if you find that PR's getting stale, or you need it pushed, please do… I can sync with, you know, Damien Matthew, works with me, and… or some of the other folks from the hotel developer community here.
But Antoine obviously is the right person to get stuff done. He's very effective, so I'm sure he'll move it along as soon.
**Ruediger Schulze (IBM)** 13:53 Yeah.
We assume that he might be in vocation, or, you know.
**Eric Mustin** 13:57 He deserves one.
**Ruediger Schulze (IBM)** 13:59 Definitely, definitely.
Good.
Okay, if there's nothing else, then we don't need to take it longer than… and I will ping Antoine on the side, maybe he can take a look at this.
The check was him.
Okay.
Good. Thank you.
Bye-bye.
**Eric Mustin** 14:21 Cheers, hu.
**Greg Shriver** 14:22 Everybody.
**Eric Mustin** 14:23 Thank you.
**Greg Shriver** 14:24 Good meeting you, Luke.
