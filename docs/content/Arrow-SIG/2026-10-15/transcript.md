SIG: Arrow SIG
Date: 2026-10-15
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Drew Relmas** 00:29 Hello, good morning, Josh.
**Joshua MacDonald (Microsoft)** 00:33 Hi.
Thought I was maybe like in the wrong place or the wrong day.
But you have confirmed my correctness.
**Drew Relmas** 00:44 No, I think we're okay.
**Joshua MacDonald (Microsoft)** 00:53 Usually I come into these minute, like a minute late and like everyone's already talking and I'm like, oh, here we are.
I'm gonna share the notes. Good morning, Aaron.
Good morning.
Cool.
And then… There we go.
So, empty agenda… I'm gonna start looking here, and people can come in.
A few more already, okay, good.
So I wanted to to to. I'm just gonna talk to myself for a minute. So we have this this process of doing discussion, stale, and deciding. And the problem I'm noticing is that when I file an issue.
because I'm a maintainer.
It gets marked… As deciding, and we don't have a deciding list.
We don't have a deciding list because…
**Drew Relmas** 02:01 Deciding, excuse me, deciding is just the default for anything new.
**Joshua MacDonald (Microsoft)** 02:06 Right. So what I mean is that our meeting workflow does not discuss deciding issues, and it's assumed that someone's going to triage them and turn them into needs discussion.
**Drew Relmas** 02:15 That is correct, yes.
**Joshua MacDonald (Microsoft)** 02:17 And I guess I'm just realizing that maybe that's not happening regularly, or… Something like that. So… Maybe we can cover some… Some triage as well. But I'm just gonna… yeah, and this has a link that's bad, okay, whatevs.
So here we are.
We're 3 minutes in, we may as well start. Maybe it's gonna be a light one this time. I see 6 people so far, very good. So, for needs discussion.
I think the biggest one probably we all knew about is… actually the one… That is listed in the agenda.
**Drew Relmas** 02:59 Just put it in the agenda.
**Joshua MacDonald (Microsoft)** 03:00 366. Let's have that be the main show. How about that?
**Drew Relmas** 03:05 All right.
**Joshua MacDonald (Microsoft)** 03:06 Okay, and then Aaron… Has one here.
**Aaron Marten** 03:12 Mine is very related.
**Joshua MacDonald (Microsoft)** 03:13 Very related, I kind of suspect.
**Aaron Marten** 03:15 Probably discuss those together, yeah. Okay, so we'll put those in the.
**Joshua MacDonald (Microsoft)** 03:18 The same place.
**Aaron Marten** 03:20 incursion.
**Joshua MacDonald (Microsoft)** 03:20 is.
**Aaron Marten** 03:20 Comprehensive than mine.
**Joshua MacDonald (Microsoft)** 03:26 And then, so we have a new, RFC open as well on this one here.
**Drew Relmas** 03:35 I guess this was marked accepted, but also still has needs discussed.
**Joshua MacDonald (Microsoft)** 03:39 Oh, yeah.
So I think, We did discuss that last time.
**Drew Relmas** 03:45 Yeah, maybe it just needs discussion removed.
**Joshua MacDonald (Microsoft)** 03:48 So, I'll take away… I've actually read the draft, so I think we can take away… needs discussion. Okay, well, that took care of our needs discussion ones, at least the ones that were already marked, and I… I want to discuss JSON, so I'm kind of, like, placeholding that.
Stale, this is always the reminder of what was happening six months ago. I kind of like it. So why don't we just dive in? Oldest first.
They're all old.
Okay, so looks like there's a problem here with batch processor.
Guidance relating to durable buffer.
Okay, so this is a, pointing to a problem.
Short-term fix is to change the guidance.
Line receiver batch durable buffer exporter if crash resilience matters.
Okay.
**Drew Relmas** 05:00 I'm not following ex… I'll have to read this.
**Joshua MacDonald (Microsoft)** 05:03 I think we're saying to take retry out after batch, after durable.
Because Durable Buffer is going to do retry.
**Drew Relmas** 05:11 Oh, yes, yes, yes. Okay, that makes sense.
**Joshua MacDonald (Microsoft)** 05:15 Interesting. I could imagine having some sort of, like, check that happens for, like, invalid or, like, discouraged pipeline configurations. We're actually seeing something in the Go collector as well, where it's like, we want to prevent you from double batching because we're in a migration, and… but it's pretty hard to detect all the cases, so… I'm not sure if this is a special case or a general case here.
I sometimes think we should try and have Lalit come to a meeting, but the times are the wrong ones, and maybe we should talk about… We should discuss…
**Drew Relmas** 05:48 Yeah, changing the times.
**Joshua MacDonald (Microsoft)** 05:49 Yeah, I actually want to have a conversation about meeting time because I know nobody likes the four o'clock in the afternoon and I like 8:00 AM but I'm not sure I'm the only one.
**Aaron Marten** 05:59 All it did just join the call.
**Joshua MacDonald (Microsoft)** 06:01 Oh, good.
Oh, I can only see part of the… okay, here we go.
Hi Lalit, we're just talking about, the… the stale issue… From a while ago, we just got through saying that accepting it, I think. We wanna… Figure out a way to, prevent the, The bad configuration here, and whether that might be a rule, or a documentation, or some other kind of enforcement.
**Jake Dern** 06:34 Just some quick commentary on that. Laurent actually did ask me to file an issue about some kind of pipeline topology linting library. I don't know how widely this has been discussed, but it's been on my backlog.
I've got some ideas about what shape that would take, but that seems like something that would help here.
**Joshua MacDonald (Microsoft)** 06:57 why.
**Drew Relmas** 06:57 don't discover that our pipelines are actually not recommended.
**Jake Dern** 07:03 Okay.
**Joshua MacDonald (Microsoft)** 07:04 this.
**Drew Relmas** 07:04 Talking about internal configurations of it.
**Joshua MacDonald (Microsoft)** 07:09 So yeah, Jake, if you're filing one, I'm just putting this in this issue since we're here. But this is the one I have open right now. It's like a similar issue. Like we'd have two batch processors in a row. Like that's a problem. You shouldn't do that. And because of the migration, we want to warn you about it.
Yeah.
**Jake Dern** 07:25 Definitely.
**Joshua MacDonald (Microsoft)** 07:26 Cool.
Yeah, lots of stale. Let's try and go a little faster. So, entities… yeah, I'm gonna mark some of these on stale. Entities are a feature of OpenTelemetry that's coming, and we don't have that fully baked in, because we snapped the… we have set the OpenTelemetry protocol Like, version before it was added, basically.
Or something like that.
Yeah. High nose.
LAURENT, hello.
**LAURENT QUEREL** 07:56 Yeah, sorry, sorry to be late, guys.
**Joshua MacDonald (Microsoft)** 08:00 So, yeah, entities are there. I don't think we need to discuss it. I also, like, profiles are there, we need to do that as well. I know something came up about metric metadata in the last week. Does anyone have a topic or a thought on that?
I think we were starting to implement, or at least you asked me a question about it.
**LAURENT QUEREL** 08:19 So, Metric Federator, We already support it at the protocol level.
**Joshua MacDonald (Microsoft)** 08:28 Okay.
Maybe we should close that.
**LAURENT QUEREL** 08:31 And, and we already, provide access to those metadata in OPL.
The main issue is the fact… I mean, the issue I'm aware of They are unfortunately named attributes.
at the Opl level instead of metadata.
which is ambiguous, because then you have attributes for 2 locations inside matrix.
Data plant attributes, and what should be metadata, which is also named attribute.
of the mystery clearing.
So I think we need to fix that.
But otherwise, I'm not aware of, missing things.
**Joshua MacDonald (Microsoft)** 09:18 So we have metadata, but it's called attributes.
**LAURENT QUEREL** 09:22 Yes.
**Joshua MacDonald (Microsoft)** 09:23 Sounds a bit confusing.
**LAURENT QUEREL** 09:25 It is.
Definitely. Don't ask me why. I mean, I don't know.
**Joshua MacDonald (Microsoft)** 09:32 Just so everyone knows, this is, like, a feature that was added on OpenTelemetry Metrics, after it was fairly stable, just to convert some corner cases in Prometheus. So if you have a Prometheus instrument that has some sort of special typing, like Enum, they have one, and they have one for state set.
If you have one of those, and you want exact fidelity round trip to and from Prometheus, you've got to fill in some information in the metadata.
**LAURENT QUEREL** 10:02 Can you add, oops, sorry, can you add maybe, just, Albert?
To this, entry, so,
**Joshua MacDonald (Microsoft)** 10:10 Yeah, okay.
I'm gonna just do that. Thank you. Thank you.
Bye.
Okay, well, trying to move through the stales quickly. Build cash needed, I remember this 6 months ago.
So these…
**Drew Relmas** 10:26 the.
**Joshua MacDonald (Microsoft)** 10:26 are related here.
**Drew Relmas** 10:28 Yeah, we've done a tiny bit of work with this and we have seen some build times improving, but we also have a very limited like, default cache size to store with GitHub, as opposed to something, like, dedicated, so there's only so much we can do. I personally think it's been a bit better the last week or two. We haven't seen, like, crazy long Windows build times.
But, you know, this… we should remove stale. This isn't ever… Present data.
**Joshua MacDonald (Microsoft)** 11:00 Okay.
**LAURENT QUEREL** 11:00 Yeah, and on that, personally, I did some experiments, for my local environment.
Leveraging cash with a K.
And and mold for the linker.
With good results. But I think that the most recent, the most urgent.
problem to solve for the CI is the fact that I think we are still using Cargo Next.
Next test, sorry. And next test, for whatever reason, is super slow.
On this project.
So… I think I will take the time to remove it and just switch to… switch back to cargo tests.
Which is faster for our specific project.
Yeah.
**Jake Dern** 11:47 interestingly.
**LAURENT QUEREL** 11:47 wound.
**Jake Dern** 11:48 Brandon.
**LAURENT QUEREL** 11:48 the.
**Jake Dern** 11:49 Internally as well, Laurent, we ripped it out, yeah.
**LAURENT QUEREL** 11:52 Yeah. So I try to understand why, because the Cargo Next test has been designed initially to be faster, but for whatever reason, it's not the case on this project.
**Drew Relmas** 12:03 Yeah, I would happily sign off on a PR if someone here wanted to.
**LAURENT QUEREL** 12:08 Okay, I will do it, because I start to be annoyed by this one.
Okay.
**Joshua MacDonald (Microsoft)** 12:13 Six months from now, we're gonna see those issues again, we'll see what happens.
**Drew Relmas** 12:16 Six months from now, we'll go back to Next Steps.
**Joshua MacDonald (Microsoft)** 12:18 the I wish that cargo wouldn't just fill up my disk, like, without control. For some reason, that's my daily issue.
**LAURENT QUEREL** 12:28 Use cargo, use the cash.
That can fix this issue.
**Joshua MacDonald (Microsoft)** 12:32 Okay.
Yeah, thank you.
**LAURENT QUEREL** 12:36 Because you can limit…
**Joshua MacDonald (Microsoft)** 12:37 Running cargo clean on one of my clients because my desk is always full.
**LAURENT QUEREL** 12:40 Yeah, you can limit the maximum number of, Then the, yeah, the maximum size, and then there is, some kind of.
LRU, and, automatically will, will drop the…
**Joshua MacDonald (Microsoft)** 12:54 This is cash with a K.
**LAURENT QUEREL** 12:56 Cash flow, okay, yes. And I already shared… Google Doc, I can share it again if you want.
**Joshua MacDonald (Microsoft)** 13:05 Sounds good to me. Just curious. Yeah, I feel like what I learned is that when you add these not… well, you can add tests, and they just blow up your disk, because they're not the same as the module, like, unit tests. They're, like, the standalone tests are what fill our disk.
Okay, moving on.
Expression tree support, function signature, I'm gonna open that because I don't know what it means.
**LAURENT QUEREL** 13:38 That's about the optional parameters in OPM, and… To some extent, to any,
**Joshua MacDonald (Microsoft)** 13:44 Okay, okay.
**LAURENT QUEREL** 13:45 Yeah, I think it's still, yeah, it's still, it's not steady.
**Joshua MacDonald (Microsoft)** 13:49 Yeah, okay.
And, Okay, I'm always nervous when I'm the one who filed them. Investigate making non-component features optional.
**Drew Relmas** 14:05 About binary size.
**Joshua MacDonald (Microsoft)** 14:07 I think this has been done at this point, right?
**LAURENT QUEREL** 14:10 Yeah, yeah, we, recently, Added two, two profiles.
Release perf and release, size.
Which I think, combined with all the features that, Drew also added, for each individual node.
We can… we have a lot of flexibility now.
**Joshua MacDonald (Microsoft)** 14:33 So this one I filed here next, I think this is, like, the least feasible ever, but I filed it just so we could discuss it 6 months ago. And I was.
And I think it maybe is now time to close it, but… but, the… the… the We… Yeah, I don't actually want to defend this idea anymore. We were sort of looking at what's the smallest you could get, and if you just have OTLP bytes going through, maybe having Arrow is, some baggage, but I could… but I can't imagine at this point taking it out.
So I'm going to.
**LAURENT QUEREL** 15:09 We can remove Data Fusion.
**Joshua MacDonald (Microsoft)** 15:13 the.
**LAURENT QUEREL** 15:14 compatible.
**Joshua MacDonald (Microsoft)** 15:14 the transform processor, which was part of your binary size.
**LAURENT QUEREL** 15:17 Yes, yes, yes.
**Joshua MacDonald (Microsoft)** 15:18 Yeah, data fusion. I think maybe data fusion is really what I want to get rid of, but
**LAURENT QUEREL** 15:22 Yes, that's the biggest, the biggest contribution to the size.
**Drew Relmas** 15:26 Okay.
**Joshua MacDonald (Microsoft)** 15:27 Anyone.
**Drew Relmas** 15:27 wanna.
**Joshua MacDonald (Microsoft)** 15:27 Pretty open this they can.
**Drew Relmas** 15:30 I want to actually say something about that when we say data fusion's a problem, which is, I know Blanche has still been slowly investigating if there's a better… if there's a way to do a columnar transform engine without the heavy data fusion dependency. So, I know he has another PR out, he's… He's interested in this offline, so… Maybe.
**LAURENT QUEREL** 15:57 Just to clarify, the problem with the diffusion is, I mean, for me, there is no problem. If you, if you have a basic pipeline.
And you don't want to pay for… a full engine like Data Fusion.
No problem. You can do it. You can just use a filter, for example, which is only based on Apache Arrow.
And not based on data fusion.
Oh.
So we provided more flexibility, but I would be very surprised if there is a… I mean, Data Fusion is providing a lot, so for complicated queries, I don't see, any.
Option to avoid that.
**Joshua MacDonald (Microsoft)** 16:39 Yeah, you know, I think, just to… my understanding of what Blanche is doing is, like, I think of Data Fusion as this high-level, you know, very complex compiler, basically, for queries and so on. What I see Blanche trying to do is, like.
maybe the simplest columnar transform engine that he's… that he can, and the… which is to say.
maybe a more straightforward translation from syntax into execution, and I think what the hypothesis is that Data Fusion is very good, because it's going to Optimize our queries, and… Blanche may try to disprove that hypothesis, and we'll see how he does.
I can imagine, like, I'm thinking of, like, this is the assembly level, like, the assembly language of, like, this is the small version of a query engine that maybe works sometimes and doesn't. I don't know. Let's let him work on it, and we'll see.
**LAURENT QUEREL** 17:43 them.
**Joshua MacDonald (Microsoft)** 17:44 So, I found this, about thinking about how we could use DataFusion, or sorry, the Dataflow engine from other places. if we could compile it as WebAssembly, you know, people compile, like, this codebase could be compiled into a browser. I don't know, I was just looking at that for some reason 6 months ago.
maybe thinking about integrating with the Go Collector as well. So, just, what would it take for us to compile, and what does that even mean, is this issue here?
I'm inclined to move forward without discussing it.
So then the next two are about Windows. I remember what we were doing six months ago. We had tests, trouble building, and then the the crypto configuration feature matrix was a problem.
So, do you think, so let's say, Drew, do you think we could close either of these?
**Drew Relmas** 18:43 Well, we also have Aaron, who opened the,
**Joshua MacDonald (Microsoft)** 18:47 True. Yes, I could also ask Aaron. Aaron, how do you feel about these?
**Aaron Marten** 18:54 On the TLS backend one, I think that in some… cases that still might make sense. I do actually have one or two folks I'd want to probably check with internally to see if we still want Want this or not before we completely give up on it.
**Joshua MacDonald (Microsoft)** 19:11 Okay, I remember this. So this is not about using, like, the SIM crypt, this is about falling back on OpenSSL.
**Aaron Marten** 19:18 Yeah, it's about… it's about just using the platform native.
**Joshua MacDonald (Microsoft)** 19:21 Or whatever, yeah.
This sounds still valuable to me.
I'm gonna say accepted.
not stale.
And for the Windows platform stuff, Just remove that.
We're almost there.
I feel like we've restored most of those tests, but I… I don't know.
**Drew Relmas** 19:54 I'm not sure either.
**Joshua MacDonald (Microsoft)** 19:57 deleted.
**Drew Relmas** 19:58 Yeah.
**Joshua MacDonald (Microsoft)** 19:59 Okay, we reached the end of stale.
Deciding issues, and then I want to fall back… I want to come back around to the ones that are new that haven't been triaged.
So, so many of the same issues. We didn't do our homework 6 months ago.
So, none of these are… very new, and I want to skip this, and someone should come back. I can do it. Come back and clean this list up.
If anyone wants to just, to propose an alternative. So now, I'm looking at the new issues list, and I wanted to do that because, as I was saying, like, some of these get automatically are not triaged yet, and I thought maybe, Elise, if there's any new issues that people want to discuss right now.
Here's one of them.
I was reviewing some code, and I noticed… I just keep seeing new JSON apparatus, and, you know, like, maybe 4 or 5 pieces of JSON code are now scattered around the codebase, and before long, I would like to see us do something about that.
I don't… didn't want to block the PR that was opened, which is one of our ADX, Azure Data Explorer PRs. But… and maybe there's another issue. Hey, hey!
Okay, maybe related. So, so, if anyone here has an interest in JSON consolidation or JSON health, JSON code structure, please come forward. This is your issue.
These two issues.
And I marked that as needs discussion. Does anybody want to discuss that with me?
No, no discussion. Very good.
**Pierre Mariani** 21:48 I'd be happy to discuss that with you, Josh, if you want to. Thank you, Karen.
**Joshua MacDonald (Microsoft)** 21:52 Yeah, I just have a sense that the code is kind of getting to be out of hand. One of our biggest problems that I'm seeing with agents writing code is that love to duplicate existing code. Like, I've seen this before.
So, From this list that we see, Two of those needs discussions are waiting for us. A few reds here.
Involving, from the F5 side, Chris has filed extensions on client cert off.
I see those… those look like we can accept them.
And then… We have some TLA plus work going on by, Max Satz.
Okay, I think we're reaching the end. Hey, there's Maxette. Maxette, would you like to talk?
**Maksat Maratov** 22:43 Hey folks, yeah, so you could probably just remove it from the list and assign it to myself.
I'm halfway through, but I'll let you guys know when I reach the end of my plan, and then we can collectively decide what's good, what's bad, what we are leaving.
And yeah, that kind of questions.
**Joshua MacDonald (Microsoft)** 23:04 So this is exciting. I've seen your draft, or one of them was out of draft now. This is, for those of you who aren't following, Maksat has begun to do some formal validation of some of our logic, and I want to know more about how this works.
But I, maybe think that we… that, I will follow up this week.
Any questions on the TLA Plus stuff, or validation otherwise? I know Jake is also interested in this topic.
**Maksat Maratov** 23:36 Yeah, to be fair, like, I'm more enthusiast on this area. I'm not nowhere near to call myself an expert, but using the power of AI, I just wanted to do a bit of an experiment, based on, like, I did the formal verification course in my… back in time in my master's.
So, I did… I took the workshop, at Microsoft. By the way, folks, we have a workshop on TLA+.
So… Yeah, and trying to start small and use, like, the Pareto principle, try to kind of, get the low-hanging fruits. So far, I'm happy, so it definitely found some issues which were hard to find with unit tests on using the conventional testing.
But yeah, I'll share my results when I get all the 4 PRs out, and then… The question there is whether we need to preserve the TLA spec inside the repo or not. Like, the code fixes are viable, I'm kind of eager to keep them.
But the question is more about the verification part. Like, if we redo, like, do we need to keep them? We'll be running it as part of CI. Like, those are the questions I want to… I want a bit of the input.
**Joshua MacDonald (Microsoft)** 24:54 Per month.
**LAURENT QUEREL** 24:54 Yeah, so, in my opinion, we need to put the TLD+, Spec, in the repo.
Okay. But we have to be careful on one thing. That was a discussion we had yesterday with Jake.
TLA twist could be used.
By various person, including us.
Saying, oh, by the way, we… we… We checked with some kind of formalization.
the behavior of XYZ.
But, the problem is, what we are formalizing.
It does not necessarily reflect the code.
That's the problem with CAD+.
And does not necessarily cover the entire logic.
So, it's very hard to derive conclusion from a search exercise.
And we know that already, because you discover something.
Which was already known, but not fixed.
But the TNA Plus logic didn't find Multiple other things that are also known, which are problematic in the… in the… In the… in the implementation.
So, what I'm saying is we need to define Maybe a goal, a direction, okay? Do we want to… cover the entire… logic of ACNAC.
And then we can say, with confidence that we… we validated the logic with a formal verification, like TLA+.
All notes.
**Maksat Maratov** 26:42 Yeah, I completely agree with you.
**LAURENT QUEREL** 26:45 Thank you.
**Jake Dern** 26:45 What.
**Joshua MacDonald (Microsoft)** 26:46 So what we're saying is that this is a useful tool for investigating and documenting what we have, and then you run it, and it finds some bugs, but then it doesn't… like, the code keeps drifting from where the model is.
I think.
And the question is, what good is it to save a model that's not tied to the code?
especially to run it frequently, like, that, like, I… this is the type of question I had coming in, like, I want to know more about how people use TLA Plus in practice.
**Jake Dern** 27:16 Yeah, I definitely.
agree with the sentiment that maybe it's not useful to run this continuously and treat it like some kind of unit test. It definitely seems valuable, perhaps, to check it in, and And just have these models there, you know, so somebody's already done, like, the bulk of the work, and in case we discover some drift or want to model in a higher fidelity, you know, we can kind of take what's there and adapt it.
I do think there's a question about whether TLA+ is the right language for it. I know there's some kind of, like, newcomers that I've played around with, like Quint, there's, you know, others like FISB.
Just speaking like from my personal experience writing a few specs by hand in both, like TLA+ is very hard to read and very hard to write. I had much more success with Quint, which can compile into a TLA+ model. I know there's some limitations that come along with that. They weren't limitations that I ran into.
But yeah, I don't know, maybe it's worth doing an investigation and kind of picking our specification language of choice for this project, be that TLA or Quint.
Or something that's not even based on TLA. I think FYSB is not. It might be its own thing.
**Joshua MacDonald (Microsoft)** 28:31 Cool, and just to be… So everyone knows we're talking about Quint, Q-U-I-N-T dot S-H, maybe the newcomer. Are there others? Nevermind. We can follow up on that.
**LAURENT QUEREL** 28:44 Please be FIZZ.
the… EE.
**Joshua MacDonald (Microsoft)** 28:55 Got it. Fisbee.
I'm finding it here. Okay, maybe. So, but very interesting, and I know that the… liveness property of our ACNAC solution was in question 6 months ago, and we had some bugs, and… Or 8 months ago, and… This is progress.
Yeah. Thank you.
**LAURENT QUEREL** 29:19 Thank you.
**Joshua MacDonald (Microsoft)** 29:20 We have come through the, triage section, and we left, there are two items left here on the agenda, and I want to… Choose somebody here to speak about this topic, whether it is Ukarsh.
Looking at the list here.
**Drew Relmas** 29:40 I don't think we.
**Joshua MacDonald (Microsoft)** 29:41 Aaron, or Drew, anybody.
**Drew Relmas** 29:45 I'm more than happy to. Do you think you could open up Utkarsh's, issue proposal?
It's the top one, yeah.
So, As I'm sure… We're all aware we've had an increase in contribution lately, from… both from internal partners at either Microsoft or F5, as well as, you know, externally.
I actually see this as a sign of, you know, increasing maturity with so many contrib nodes being added, it means we're not investing so much time in the engine fundamentals, but rather, you know, extending our capabilities to interact with more vendor systems, or things like that. So, this is all a good sign.
A few weeks ago, the maintainers had also made a decision to raise the approval, Count to 2 from 1.
Meaning that, you know, you need two approver slash maintainer approves to merge PR.
However, we also tried experimenting with the code owner concept, where if a folder declares a metadata file with a couple other GitHub aliases in it, those are the people that we look to for the authoritative review on a subject.
And who get pinged, hopefully, or assigned by GitHub when a PR is opened.
Up.
So, I think this has caused a little bit of friction, and in some cases, slowing down velocity, specifically in times where A code owner of a node might be making a change, and they get… So they're intimately aware of the subject matter at hand, and then a approver or maintainer approves it. So you would think that should technically qualify as ready to merge.
But oftentimes we've had to go find like a second approver or maintainer to also sign off on it.
So… Good.
this problem in a nutshell is just having a discussion as a community about what we think the right, approval policies are. Ukarsh here was proposing that, like, the table that we see in front of us. So yeah, if anyone here on the call would like to chime in, please go ahead.
**Joshua MacDonald (Microsoft)** 32:27 I can confirm that I have seen this problem. I've… the… the thing I've been doing to try and help is not great, which is sometimes I see a PR that I know is going to need two, and I don't… two approvals, and I don't really want to review it, so I approve it first, because I know that then the second approver has to do a little bit more work.
Thinking about whether they want to permit it to merge and so on. But I… but I could… I could easily see, relaxing for contrib the 2 down to 1 again.
**LAURENT QUEREL** 32:59 Samir, my only, comment was, I think it was mentioned previously in the Slack channel, just making sure that the… The boundary are effectively properly determined, we could imagine a PR that is focused on ContribNode, but in fact doing some modification in some internals.
in the engine.
Just want to make sure that the system that we will use to To relax the constraint, we'll, we'll.
Make sure that this kind of thing could not happen.
**Drew Relmas** 33:40 Yeah, I agree. Totally makes sense. My biggest concern with this, proposal was simply… We're probably gonna have to go script up something custom rather than using like native GitHub rule sets.
But that's not to say we can't do that. I'd just like to keep it to a minimum if possible.
But I assume, you know.
I assume other folks in the call have also experienced this, particularly from a PR author standpoint.
**Joshua MacDonald (Microsoft)** 34:22 Drew, as a non-expert on GitHub automation, I would definitely support, like, doing what's simple and not going bespoke on this. Is there an easy solution?
And it gets us most of what we want.
**Drew Relmas** 34:39 Okay, yeah, I can… I can definitely do Maksat's thumbs up as well. I can do a bit more, research about this. The weird part is… I'm not sure if you can have a different number of required reviewers based on folder path.
That's something.
**Joshua MacDonald (Microsoft)** 34:58 I can, by the way, because I've seen that elsewhere. The collector, the Go collector has.
RFC's folder, which is special. It requires 4 approvals.
**Drew Relmas** 35:09 Oh, okay, gotcha.
**Joshua MacDonald (Microsoft)** 35:10 And I've noticed that because if I just like I have an RFC that's already merged and I just want to edit it, like I got one little mistake, and like, no, don't touch it. It's got four approval.
**Drew Relmas** 35:20 He's.
**Joshua MacDonald (Microsoft)** 35:20 It's for approvals, just to touch it, so… I avoid touching it.
**Drew Relmas** 35:25 Okay.
Well, in general, unless anyone else would like to speed up at the moment, I guess the takeaway is, the maintainer group is aware of this problem and is, thinking of ways to solve it.
**Joshua MacDonald (Microsoft)** 35:42 And this is another take on the same from Aaron. I think we were all feeling this. Aaron, do you have any.
Sort of quick summary of… or alternate proposals?
**Aaron Marten** 35:54 Yeah, no, this was almost a sub… subset of what Ukarsh's proposal was. His is much more comprehensive. Mine was more filed just kind of as a pet peeve, where I had a Quiver PR and a WASM host PR, and Yourself, myself, and Laurent are listed as the code owners on those folders, and we were the only ones notified.
of those PRs, whereas it wouldn't necessarily need all of us to approve, you know, anybody else in the approvers group wouldn't satisfy it, so… but they weren't getting notified, so that's all.
**Joshua MacDonald (Microsoft)** 36:28 So we just need more of this.
Open Telemetry Arrow approvers.
**Aaron Marten** 36:34 Well, we have that. We have that in code owners, but the trouble is the lines after that, which are folder-specific, override it.
**Joshua MacDonald (Microsoft)** 36:42 So, if we…
**Drew Relmas** 36:43 So it's just an ordering problem.
**Joshua MacDonald (Microsoft)** 36:49 And it sounds like we could add this clause to every line afterwards and get what we want.
Maybe.
**Aaron Marten** 37:01 Maybe.
That would still… the trouble with that is, if the intention was that one of the listed individuals needs to sign off, if you added Arrow approvers on every row.
Then that kind of negates it.
**LAURENT QUEREL** 37:16 That was the intent.
In my opinion.
Absolutely right.
Yeah. So, I mean, if it's a problem of order, maybe that will fix the problem, but adding Arrow approver for any, additional specific rules.
I think we'll… we'll basically, Can't sell the initial intent.
**Joshua MacDonald (Microsoft)** 37:40 Okay.
**Aaron Marten** 37:41 the.
**Joshua MacDonald (Microsoft)** 37:42 It's working as intended, at some level.
**Aaron Marten** 37:45 Yeah, I was proposing there is a way to solve this, but you have to use GitHub's rule sets.
So we would keep code owners as it is, with just the listed individuals, but if you added a rule set, that would invite Arrow approvers on all PRs.
**Joshua MacDonald (Microsoft)** 38:03 Yeah, I think Arrow approvers should see them, but we're still asking for one of the code owners to approve. That's correct.
**Aaron Marten** 38:11 Yep.
**Joshua MacDonald (Microsoft)** 38:13 For the record, I don't even look at GitHub notifications. There's too many of them. I just read the PR listing throughout the day again and again and again.
**Drew Relmas** 38:22 I also want to take this opportunity, I put it in the chat, but I'll say it verbally as well. I know we have a lot of people who are contributing a lot of code in the repo. We are desperately looking, always, for more triagers and approvers, so if you're interested in Doing that, you know, reach out to a maintainer and we can talk about how to get there.
**Joshua MacDonald (Microsoft)** 38:51 Very good.
Excuse me, I'm going to sneeze. We have another, issue coming here. Let's see.
Oh, good. Pierre is here, and we have been talking about this issue for a while, and I'm glad that we're back.
Here.
**Pierre Mariani** 39:11 Hey, folks, good morning, good evening. Okay, so here's the context.
Of course, the pipeline accepts protocol buffer messages in metrics, logs, and traces.
We have a bespoke parsing facility, as well as a prost-based parsing facility. A few weeks back, we realized that there were some gaps in how the bespoke parsing facility implements the protocol buffer.
Specification.
In particular, it's not handling some duplicated fields correctly.
As per the… specification, duplicated fields can happen a little bit any place in the message. They can be consecutive, or they can be separated by other fields, and depending on the type of fields they are, you need to pick the last one that shows up, or you need to merge them.
I've implemented some tests that are highlighting some of the issues between both implementations, between the post-implementation and our bespoke implementation.
Laurent had, suggested an API to, implement those tests. I'm still looking at that.
One quick, thought is that Laurent's, suggestion includes a.
the ability to define the expected results. I was thinking that maybe if we consider that PROST is the reference implementation, and we compare whatever our bespoke and PROST return, we can skip this expectation. That's one small thing.
Another small thing on this topic as well is that we were discussing Lib, Protobuf.
mutator as a way of identifying interesting use cases. After looking at it, I don't think it's a promising avenue in this case, because we would need to implement a subclass and define our own mutations, so we might as well just do it directly.
What I'm worried about is the following. I think that our bespoke parser right now is rather greedy. I'm not fully sure, but I think that's what it does.
But to be compliant with the specs, we have to… parse the message more fully, so that we have full context of the fields, so that we can merge and pick the correct one.
And I'm wondering, what that's going to do to the performance of our bespoke parser, and how much delta we're gonna get between our own parsing and the prose parsing.
What I need to start looking at, I've not done it yet, is whether, you know, there is some simplifying assumptions that we can leverage.
Based on the knowledge that we are only parsing metrics, logs, and traces, and we don't need a general parser that will help it be materially faster than post.
So that's what I wanted to… I wanted to give a status, I guess, on the latest thoughts, and also put the problem to the group of maintainers and contributors here.
**LAURENT QUEREL** 42:38 So… The, the… I think the problem was not… Performance, passing performance, us versus us.
The problem with POST is… The fact that it will create an intermediary representation that we don't need.
So.
So, POST will basically create structures Different alien.
Scalar information.
resulting of the OTLP bytes, and then… that was one of the first implementations. Then we have to use this, gigantic tree of small objects and convert it into.
And the type of presentation.
And and the principle of what we have here is something that will convert directly from a TLP bytes to Arrow without this intermediary representation, so we… we remove a gigantic amount of allocation with this approach.
That's the main, the main objective. Now.
I will be curious to see… What are the… the gaps?
between what we did, and what the spec is saying, so I'm aware of the… The problem on which you work, the one-off, the fact that, we, we, we should… Keep only the last value.
For the corresponding one-off.
Is there any other, Gap with the… with the spec that, will be meaningful.
**Pierre Mariani** 44:30 Yeah, I found one more, which is, so some of the messages of the schema URL, and if I specify two.
Prost correctly picks the last one, and our implementation picks the first one.
And I was kind of hunting for others, but was not successful, but I also have not been able to dedicate as much time lately as I would like, so I'd like to complete that a little more.
Okay.
And I, you know, I think I could do a fairly exhaustive job at that, because, I think it might be important, and, you know, the structure is not that deep and complex.
And also, I wonder… there are things that are puzzling me, and I'm wondering if Prost is doing the wrong thing, or if I'm misinterpreting the spec, and I'm sure I am misinterpreting the spec, so…
**LAURENT QUEREL** 45:26 Okay.
**Joshua MacDonald (Microsoft)** 45:27 Let me add something. Let's see. I have been, like, I feel like Protobuff is baked into my DNA from so many years of working with it, and I know that.
So, in the case of the one-of, like, this is a scenario where, like, there's no valid reason that you should ever see more than one value inside of a one-of. It is, like.
Corner case, because there's no valid way to concatenate protobuffs that would result in the encoding that you're trying to protect against. Because the way one-ofs are wrapped.
**Pierre Mariani** 46:08 So.
**Joshua MacDonald (Microsoft)** 46:08 You don't just get a one of… payload, you get a one-of field with a value inside of it. And what… what we're protecting against here is a one-of field that had two values inside of it, which is an encoder problem.
Now, the other category that Pierre has described, as I see it, is cases where A non-one-of field, which is not repeated.
which looks like a plain old field, could be repeated, and PROS will take the last value, and we may take the first value. But this is not like one of, where there's no valid encoding that can get you that. It's purely a bug, in my understanding, for one of.
But, in the case of… any other random protocol message is not a one-of. If you concatenate bytes of the protobuf representation, what you're expecting to get is an override or a replacement. So the last value wins when you append bytes. That's how it's supposed to work.
And this is a case where, if someone has a bespoke encoder for protobuf bytes.
That uses this trick.
of, like, concatenating the bytes encoding. They will… the parsers are supposed to do the last value wins for that reason.
So then the question might be, when could this be the case? I don't have any good answers, partly because For us.
we're dealing with OTLP payloads, and I'm trying to answer the question Pierre posed, which is, are there anything… is there anything special here that we know that we could help… that could help us? And the only thing I have there is that we only ever concatenate top-level OTLP objects here. That's a normal thing for us to do. The batch processor does it.
And, however.
There are, to my knowledge, no non-repeated top-level fields in our OTLP protos. The top-level field is purely repeated, and that's for a good reason for this to work, is that you can always concatenate two OTLP encodings as bytes.
and they there's and it will never run into this problem of having a non repeated field be repeated.
And need the override behavior, last value wins.
So, structurally, we are not going to see this ourselves, at least I don't know of any reasons to, but someone out there could be encoding, like, protocol messages like… in a way that exercised this bug, and they could defend themselves as doing something legitimate, and we would parse it incorrectly.
So I can see that corner case, but it's extremely elaborate. You have to be constructing protobufs as bytes.
inside of, like, on the inside. Like, I'm saying it's okay at the top level, because we're all repeated. That's my… that's the nuance that I would add.
**Pierre Mariani** 49:11 Well… Yeah, it seems like it maybe would be a gotcha, or trying to exploit something deep in the parser.
One quick thing, though, is I did test… two Separate one-off messages, not necessarily one of… one… one-off message with two.
fields inside of it. And I think, I think the custom parser is not doing the correct thing there either, but your Uber point, remains anyway.
**Joshua MacDonald (Microsoft)** 49:45 Thank you, your point is received as well, thank you. So, multiple one-of encodings.
That should be the same to me as multiple any field encodings.
Any non-repeated field encodings.
But yes, this is an interesting corner case. One ofs are sort of terrible, honestly.
**Pierre Mariani** 50:10 Yeah, so I'm not sure, you know, the… I mean, I think I need you guys to… to decide, you know, the level of protection at which we want to go there on this external-facing, you know, endpoint.
**Joshua MacDonald (Microsoft)** 50:25 Yeah, I…
**LAURENT QUEREL** 50:28 There is two type of protection. Is it something that will Leads to some kind of panic, no.
Is it, something where we will interpret the data not exactly the same way that some other.
Like, post will do, yes.
Is it a problem?
I think that's the answer we need to provide. And based on what Joshua mentioned.
I'm not entirely sure it's a real problem.
**Joshua MacDonald (Microsoft)** 51:06 Yeah, I kind of agree that this is not a real problem. If you find yourself in this problem.
It will take a lot of explanation to understand how we got here, and then should we offer a, like, slow mode, or, like, a fallback where we be, like.
spec compliant on Protobuf.
Appended fields and so on.
I will wait for someone to ask for me to do that. I'd like to see how they produce this data in the first place, because… you know, it's gonna be a weird case. I'm all for producing protobufs by concatenating bytes, but when I do that, I don't generally repeat fields that I don't want to repeat. Like, if I'm doing something so custom as to be wrangling bytes of protobuf by myself.
I shouldn't duplicate a field. That's… That's sort of where I… like, you're gonna have to explain why you're doing something crazy and dumb at the same time.
Maybe. There's gonna be a reason, but it's gonna be really obscure.
Okay, that's what.
**Pierre Mariani** 52:10 Yeah.
**Joshua MacDonald (Microsoft)** 52:10 Yeah.
So I think, what I… the takeaway then, Pierre, is I would say probably we're willing to just take first value wins and ignore the problem.
And, maybe in a couple years, someone will find a reason to complain about it, and then we can reevaluate, but I would love to see us not make extra work or CPU, like, extra allocations of memory, for sure, just to, like, handle this obscure case that we don't expect to see.
**Pierre Mariani** 52:39 Yeah, that makes total sense to me. It started to feel very, you know, very pushed. I'm more than happy to document what we discussed in the issue there. I don't know what the practice is as far as closing the issue or tagging it as some type of one fix or something like that.
**Joshua MacDonald (Microsoft)** 52:58 I think we can mark this as.
Won't fix and let somebody reopen it.
**Pierre Mariani** 53:07 Awesome.
**Joshua MacDonald (Microsoft)** 53:20 There we go.
**Pierre Mariani** 53:23 Awesome.
**Joshua MacDonald (Microsoft)** 53:23 I think we can wrap that one up. So, Pierre, we will not be doing any bespoke work to handle this corner case, unless… until further notice, I think.
**Pierre Mariani** 53:33 Yeah, yeah, good.
Loud and clear. Yeah, no problem. Thank you.
**Joshua MacDonald (Microsoft)** 53:36 Very good.
Anything new on the agenda? We have a few more minutes here.
Not required.
I will say this, going once, going twice, anybody last comments?
Well done, everybody. We made it to the end of another meeting.
Happy Thursday!
**LAURENT QUEREL** 54:00 Happy Thursday. See you later. Thank you. Bye.
**Pierre Mariani** 54:02 Thank you, goodbye.
**Jake Dern** 54:03 do.
