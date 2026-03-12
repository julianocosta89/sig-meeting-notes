SIG: Governance Committee
Date: 2026-03-11
Duration: 61 minutes
============================================================

## Zoom Recording Transcript

**Pablo Baeyens** 00:40 8.
**Tigran Najaryan** 00:43 Glow.
**Ted Young** 00:45 What up, y'all?
**Alolita Sharma** 00:56 Hi, folks! Good morning!
**Marylia Gutierrez** 01:00 Hello.
**Alolita Sharma** 01:01 A.
But really, I'm glad you're, taking a look at all the, repos, because…
I think, they've changed over time. I wonder if we could…
Like, that's what an MCP would be useful for. It gets maintainer status.
**Marylia Gutierrez** 01:23 Yeah, I was just showing, yeah, Ted saw some of those, the data that I was getting.
**Alolita Sharma** 01:29 Yeah, yeah, yeah.
**Marylia Gutierrez** 01:29 The summer people right now.
**Alolita Sharma** 01:32 Yes, no, no, that's very good.
**Ted Young** 01:33 Yeah.
Yeah, that's… that's fantastic. I was gonna say, present that stuff.
**Alolita Sharma** 01:39 Yes.
**Marylia Gutierrez** 01:40 Yeah, friends, I'm happy, happy to share him.
**Alolita Sharma** 01:44 No, no, totally. It's actually very useful.
we've been trying forever, you know, to get this information accurately from the Grafana dashboards that we used to have for all the projects, and then we moved to Insights, right, from the CNCF.
But, there's some information there, but it's not necessarily… you know, all This is very helpful.
**Ted Young** 02:56 Okay… Well… What counts as quorum for the TCGC meeting?
**Alolita Sharma** 03:07 I know, I should be paying our… Tigrin is here. Hi, Tigrin.
Pat David's here.
Josh is here. Jack is here. Ratt is here. Okay, we have Corum.
**Ted Young** 03:19 Great.
Should we just get rolling? Feels like we've got plenty to talk about.
**Josh Suereth** 03:27 Yeah, I wanted to… the topic that we had that was in private, what, 2 weeks ago? Should we continue that in private, or do you want to talk about it publicly? I'm fine either way, personally, but just wanted to check before I put it on the agenda.
**Pablo Baeyens** 03:43 on…
**Alolita Sharma** 03:43 Revitably.
**Pablo Baeyens** 03:44 fined with it.
Being public, but…
**Ted Young** 03:50 Yeah.
**Alolita Sharma** 03:50 Josh.
**Pablo Baeyens** 03:51 And then there's.
**Alolita Sharma** 03:51 sensitivity of not… Doing it on a call? A public call?
**Josh Suereth** 03:56 No, no, I don't think so anymore. No, I think we, we had, we had a good talk, and I think we're at the, like, proposal phase, so, like, I'm fine. I would prefer it to be public now.
But I just wanted to check with everybody before I just throw it on the agenda, right?
**Severin Neumann** 04:13 I think we're far enough in that, so yeah, let's make it public.
**Pablo Baeyens** 04:20 Okay. Sorry, if you'll let me, like… One minute. Keep coming, eruptors.
the OpenTerno Project update talk, and there's a CollectorSeek-specific talk. Right now, and they are happening,
On back-to-back, and on the same room.
Right now, the collector sick talk will be happening first, and then the general one. I am thinking about reaching out to the CNCF to try and swap those. The collector people, as far as I know, would be okay with that.
Do we think that's a good idea?
**Alolita Sharma** 05:02 Yeah, it's fine.
**Ted Young** 05:03 So people get the general overview, and then a deep dive.
**Pablo Baeyens** 05:06 Right.
**Ted Young** 05:07 Stick around? Yep. Yeah.
**Alolita Sharma** 05:09 Yeah, I think that's a.
**Ted Young** 05:10 If you reach out to them along with the people from both talks, they'll…
**Alolita Sharma** 05:15 Yeah.
**Ted Young** 05:15 We'll do it like this.
**Pablo Baeyens** 05:16 Yeah, yeah, that's a… put 10 people on CC, and that should be good for them, I hope.
**Alolita Sharma** 05:23 Yeah, yeah, they usually like 10 people on CC. So…
Go for it. Sorry for taking time off for that, but…
**Pablo Baeyens** 05:32 keep comments coming, and I need to do that now. So let's… let's move on to Josh's topic.
**Josh Suereth** 05:41 Yeah, so just wanted to follow up. We had a bunch of, like, distributed folks working on project… proposals around project proposals.
some meta-proposals, I guess? I'm trying to copy and paste them from, the chat right now, so someone… if someone can do that. Lyudmila had a great write-up and a set of things that we needed. I'm gonna… I'm gonna call out a few things that we,
I don't think have owners.
As well. So, give me one sec to copy a few things. Pablo, thank you for updating yours.
Oh, let's do… oh, man.
Formatting. Come on, Google Docs.
This was the other one.
And then… Ludmila, I think you had point 3, there was a comment there.
**Liudmila Molkova** 06:38 Yes, I did, but I didn't have a chance to prepare, sorry.
**Josh Suereth** 06:41 That's… that's fine, that's fine. I just… I'm gonna… I'm gonna put them here in the notes so that it's not…
You're okay if I, if I copy-paste the, like, the description we had?
**Liudmila Molkova** 06:53 Yeah, yeah, of course.
**Josh Suereth** 06:54 Okay, beautiful.
Alright, so… and then we can… we can talk through if we need. Alright, so let's walk through… I've put together a quick,
Basically, a strawman proposal. So this has the points…
Do you want me to present? I can present.
**Liudmila Molkova** 07:10 Yeah, please.
**Josh Suereth** 07:15 Here we go.
So this is just, like, 3 bullet points we can do. We want to make sure feedback is direct and actionable, especially if we have fundamental concerns. We want to make sure that we, on project proposals.
And we want to make sure that we are explicit about technical or staffing concerns. So, basically, I have, I think, 4 things that I think will address this that are actionable. So, first, community project proposals immediately are triaged into a TC bucket review that will hit the TC inbox that we would review weekly at the TC meeting.
We would miss once a month, during this meeting, because we don't triage on the monthly meeting, but generally it means within a week, there'd be TC feedback of some form.
Right?
If we discuss it in our triage process. The second would be, we make sure that we do this, and it guarantees at least weekly, but again, you know, every month there might be a two-week delay. At least if it hits the triage bucket, we know to pay attention to it immediately. Second.
or third, I guess. A rubric.
So we put together a rubric for what the TC will generally be evaluating on project proposals, so that people are aware of, like, what our feedback will be based on, and when we have our discussion, we'll take points and concerns and put them into the rubric.
Alright, so this is to try to unbias, be fair, that sort of thing. Make sure people know, when we do a technical evaluation, what are the things we're looking at, why do we care?
And then lastly, it would be, we make sure all concerns are actionable. So, if we have a concern.
We want to make sure that we think the proposal of the project can address that concern.
If we are unable to do so.
that's a sign that we actually will be suggesting to close the project, or, like, we don't think this project is, one that OpenTelemetry can achieve.
Like, that's my litmus test, right? If we think that all our concerns can be addressed, we make them actionable, we make sure someone can address them. If we think they are unactionable, that's a sign from the TC that we think this project proposal needs to be closed.
All right, so those are the four things that I'd like to propose we do. The TC would take action of making the rubric, the GC would update whatever triage process we have in community to make sure it hits our, our, inbox immediately, and then we make sure that we do… that we have this process in place.
Go ahead, Sovereign.
**Severin Neumann** 09:49 I think my comment… so first of all, I like this proposal, so this is more like building on top of it. I think the only thing I wanted to look into from a GC perspective is the first one, because right now, I think the process that we have is, like.
if something lands in the community repository, the GC is looking at it first, because technically there could be a proposal that is community only, where the question is, is there even some
TC review required, chances are slim that this is happening, and I think so far that was the process, so I'm wondering if this should be…
Step zero still, or if you think, like.
whatever happens, TC should take a look at it and make that judgment on their own, and say, like, okay, we need to… we need to jump on that.
**Josh Suereth** 10:41 I'll respond quick, and other TC, feel free to jump in, but I think the idea is to get direct feedback early.
So, I know that this is a little spammy, but I'd prefer it come to the TC immediately as well. Okay. And so the TC can actually make that judgment in addition to the GC. We could even have a chat on our, like, internal chat to say, hey, this came in, TC doesn't think that we need to be part of this, do you agree?
just to… again, the idea is we want to resolve these quickly. If the GC is reviewing and sending it to us quickly, that's great, but if you have the same weekly cadence we have for triage.
That delays this whole thing by 2 weeks, which I think.
**Severin Neumann** 11:20 Yeah, no, so the idea is to let TC and GC have it at the same time? Okay, okay, yeah, that makes sense.
**Josh Suereth** 11:27 Under the assumption, the speed is important here, which I think is true.
**Severin Neumann** 11:31 Yeah.
**Josh Suereth** 11:33 Good.
**Ted Young** 11:35 Yeah, the thing I think I would add to this, just kind of backing up what Severin was saying is, like, on the GC side, I think we have a bit of a tragedy of the commons around the community stuff, and I think…
having a requirement for, like, faster response time for us, right? Especially around these things, having them be, like, maybe assigned to a GC member to eliminate the tragedy of the Commons thing.
And some kind of, like, script or a checklist, right? Like, just like with airplanes and everything else, having a checklist or a script to follow that's posted publicly so that, like, everyone understands the process.
Would be helpful.
Because that's the other feedback we get from people, is they just don't know what's going on, because we're… even if we are making decisions, we're consistently under-communicating them back to the people making the proposal. So, I think that 100% lands on the GC and us just…
Having, like, a commitment to responding faster to these things, and sorting out who's… who's bottom-lining what.
**Tigran Najaryan** 12:46 Yeah, and the other concern is that if the seizing is…
begins involvement with the project proposal a couple months after it was proposed, and then the TC says, oh, this doesn't look right to me, there's objections, we don't think this… then it's a bit too late, right? So for people to be having these discussions with the GC and kind of…
be under the impression that it's moving well, and it's going to be accepted, and then suddenly there's a cold shower, right? So, no, it's not going to happen. That's bad, right?
**Ted Young** 13:20 We had this same problem with things going from, like, SIGs to, like, public review. It was, like, it felt like a similar thing, right? People do all this work in the SIG, and they come to public review, and suddenly they get shot down in a way that's, like, very unexpected.
**Tigran Najaryan** 13:36 You know.
**Ted Young** 13:37 And, like, having just more of that feedback happen earlier helped, like, to use all of that. You can see the same thing here.
So, I think even… I think it should automatically go into TC review, like Joss is suggesting, but if the GC… if we're doing our job and we're being responsive at our response rate, the way we should be, if some weird thing ended up in your review box, we should be able to bat that thing.
out of there, if it turns out it was, like, not worth your time. So, I would be all for it being more automated and kind of causing the TC to at least be something that could poke the GC if we aren't doing our job.
**Josh Suereth** 14:22 I added… I added, two points here, just to make sure, from that, Ted. So one is just, I think the checklist of the process workflow and, like, expected amount of time
possibly, on these things, would be helpful for us to have. So, when we talk about the project proposal process, I think… I think it's kind of documented, but giving people, like, a time
window idea.
**Severin Neumann** 14:44 would also be helpful. Yeah. Do you think… I think the document exists, but we need to communicate it better, and maybe even make the…
PR description or something like that, and they're like, hey.
here are your tasks now, right? And expect this to take this and that many months. Yeah.
**Josh Suereth** 15:03 Yeah, exactly.
**Ted Young** 15:05 We have a process doc in the community repo that we should update.
To have a lot more detail.
**Severin Neumann** 15:13 Yeah.
**Josh Suereth** 15:18 Cool.
I'm gonna put a 2 for measuring the response rate, because I think this is useful, but I think just getting these updates is the most immediate concern now.
Yeah, oh, we have questions. Ludmila, go ahead.
**Liudmila Molkova** 15:33 Yeah, quick note, I was going to put it in my write-up regarding the, the, TC, part. I think we should not just have a process, but also it should be part of the,
project template itself, like, which bucket it goes into, and what kind of support is needed from the TC.
**Jack Berg** 16:02 Yeah, I was gonna add on to that,
this… Lyudmila had provided a number of messages in the GCTC channel last week, and, I don't see a couple of these ideas represented in there. One of them was about, you know, sponsorship level, which Lyudmila was just,
talking about, but then also…
timing constraints and, and trade-offs, right? So,
If the… if TC sponsorship is required.
What do we do if it's not available?
Because we're at capacity, what do we do if…
We have capacity, but nobody volunteers.
**Josh Suereth** 16:49 Yeah, so, so Jack, my proposal… we split, we split into 4 concerns.
My proposal's just about the setting clear expectations for people. The, TC sponsorship level concern, no one signed up to make a proposal around how to address it.
**Liudmila Molkova** 17:06 I signed up for it.
**Josh Suereth** 17:07 Oh, oh, oh, sorry, sorry, Lamila signed up for that one, sorry. Yeah, setting clear expectations was the other one. This… point number two was literally just faster feedback, of, like, what are we gonna do to get faster feedback to people?
And so, that's all I'm trying to address right now. And I agree with you, we have to address all of this. It's just like, in terms of divide and conquer.
I'm hoping, like, let's start with getting the feedback faster.
**Jack Berg** 17:32 I misunderstood the scope, that makes sense.
**Josh Suereth** 17:34 Yeah, yeah, yeah, yeah. But great question, and I think that's a further discussion for later on, because I'd like to get to that, if we can. Go ahead, Ted.
**Ted Young** 17:43 Yeah, so I think another thing we identified was, like, approvals, and what the heck do approvals mean, especially from the GC, right? Because there's a…
a thing of, like, we're trying to help people get this proposal together, and it's sort of like, there's maybe one set of approvals where we're going section by section in that doc, and we're saying, like, this section is approved by the GC in the sense that we believe you've successfully filled this out.
Right? This is no longer a to-do item, and you didn't fill it out in a way that we think is obviously bad. Right? So, maybe it's finding some other way to give approvals for those things, like literal check marks in the doc.
Or something.
Some way to be like, we believe this is filled out and ready to go, and ready for, like, a final evaluation by the TC and other people.
So that…
**Josh Suereth** 18:36 I agree.
**Ted Young** 18:37 We can preserve the official green checks for, like, this is go time.
**Josh Suereth** 18:42 I think that all… that makes a lot of sense. That was around, item number 2.
And the goal of that. And again, like.
I… we should talk through that more in detail. I don't know if anyone signed up to, like, actually take action on it, right?
So I think that's… that's the thing I'd like to get to with these. Lyudmila signed up for this, Pablo signed up for this one, which I'd like to talk about next, if we're comfortable. I signed up to do this faster feedback thing, so, like, I'm… I'm taking ownership, I'm… I put together the straw man, if we agree to it, I will put this into practice and start issuing PRs.
Right? The thing you're talking about, Ted, no one signed up to do yet, and to me, I think it's really critical and important. I like the proposal you put together there, but it's more important to me that someone will do it.
**Ted Young** 19:30 Yep.
**Josh Suereth** 19:31 Okay.
**Ted Young** 19:31 I'm out for the next 3 weeks.
**Josh Suereth** 19:33 I know, we have a QCon coming up.
**Ted Young** 19:35 up, when I come back, I will.
I will look into picking it up.
**Severin Neumann** 19:41 I can try to drive a little bit of it.
I mean, my time is limited right now as well, but I can at least make some initial progress, and then…
Hopefully it helps, so…
**Josh Suereth** 20:01 Cool.
Let's… I want to give Pablo some time for his, making trade-offs visible. Do you want to… you wanna talk… I really liked, what I read in the chat. Do you want to… do you want to give us a quick update on this part of it?
**Pablo Baeyens** 20:14 Yeah, so, sorry, I didn't write, anything, but maybe if you can open the, the link I shared, that could be useful.
So, this is the process that the RAS project follows for, specifying project goals.
They've been doing this, I think, for about 2 years.
This is the most recent I could find. The… the main thing that I like about this is the section that I linked to. So, goals are proposed by contributors and accepted by teams. So…
There's a set of people that want…
something to happen, some… they have some goal, and the different teams in Rust, I guess that would be our SIGs, would accept them. That means the contributors say they will work on it, and the teams…
will support them, things like doing reviews, or, like, guiding them through the project.
I think this is important both for projects that happen entirely within one SIG, one existing SIG, but also for projects that touch on different parts, because…
It…
makes it so that the maintainers of different SIGs explicitly express, like, yes, I am able to commit to this, and
I don't know, I think we don't need to copy their entire process, there's other things happening on the project goals, but I especially like that, and I don't know, I would…
I would like to know what people think, and whether we can include that in our… Workflow.
**Severin Neumann** 21:59 Can I just call out that this is exactly how we do the Ecosystem Explorer?
I mean…
Jay said, like, hey, I want to do this, and, like, now comms is supporting him, but he's, like, the person
Driving this really hard.
And that's why this project is successful, right? Because the person that showed up did not assume that other people do the work for them, but, like, saying, like, hey, I want to do this, and I want to work on that, right?
So I'm… I think that's… that's a good one.
**Tigran Najaryan** 22:33 Is this different from what we do? Isn't that what we're asking people to do? They propose a project, they propose a staffing, which supposedly is… will be contributing, and then we accept or don't accept it, right? Is it different from our process? I'm not seeing the big difference here.
**Pablo Baeyens** 22:52 I think the big difference is on the commitment from SIGS. I don't think there's a big difference on the stuffing, or maybe even how the TC works. Like, the TC does explicitly say, like, you have this person that's going to sponsor it, and it's going to give this level of
support. But I don't think we have a formal process for the commitment from existing SIGs, and I think that…
is something that happens for the collector, for example, and that's part of my inspiration, but also from, IPTC, like, language SDKs. They, the configuration sign needs,
different… Prototypes from different languages.
**Jack Berg** 23:36 I think that's part of the, the, the staffing, right? So for… just back when we did the configuration project proposal a couple of years ago, the thing that made it successful was that we had, people volunteer from Python, Go, and Java to go and actually implement this. So, you know, there was a realistic route to get the prototypes we needed to, you know, get the spec to where we needed it to go. So we do this, but,
I don't know, maybe there's some opportunities for improvement.
making it.
**Pablo Baeyens** 24:02 I don't sit.
Sorry, let me reply to this, and I'll let Lumida talk, but I… I don't think we do this in a way that is formal enough so that it happens on every proposal. I think when the proposals come from
Within the project, that happens more often, but when it's something, more…
new or external, it tends to happen less often. That's at least my impression.
**Liudmila Molkova** 24:29 I think we might follow this process, but it's never explicitly written down, and some people don't understand that we follow this process.
**Alolita Sharma** 24:39 Yeah, that's definitely more like it.
**Ted Young** 24:44 Pablo, where I feel like this could be really helpful, a hole we have right now
that matters more and more as the project goes on is, like, we have a whole proposal and spec process for figuring out what the future looks like, and I feel more and more okay about that. But going from, like, it goes into the spec to, like, we implement it and ship it, that's the part where we just say, like.
underpants gnomes, something happens there, and then maintainers ship things. We don't have a way for, SIGs to, like, coordinate what they're working on, or having any kind of, like, coordinated effort, and…
it's not as simple as just putting high-level, like, public items like we were trying to do, because the SIGs are all in different places, right? So there's some SIGs that are ready to go working on config, but there are other SIGs where that would be a priority inversion to drop what they were doing and work on config.
And we were trying to look at using GitHub projects to maybe help with this, but those things are so invisible.
That they're not useful.
But maybe there is a way to use GitHub issues and just make a GitHub rep… some way to use our GitHub tools.
to help the SIGs coordinate better.
And this relates to the stability stuff and all of that. We just don't have any tools for, like, coordinating at that level right now.
**Josh Suereth** 26:10 I'm going to jump in as a moderator. I think that's a problem, Ted, but I really want to focus our discussion on concrete plans for, like, the actions we have. Like, so I want to go back to exactly what Pablo was trying to address, which is at the project proposal phase. Like, I… again, this was a post-mortem around a project proposal we don't feel we handled well.
And so, I want to make sure acutely we're addressing project proposals at that phase. I agree with you, we need to address that.
I just, like, for the purpose of the next 30 minutes, I want to keep… keep the conversation really, like, what are the bullet point items we're gonna do in the next 2 months to address that?
**Ted Young** 26:46 I don't think we need an additional process than I would suggest here. I think we should focus on the project file and the project process, and I think it's, again, it's like on the GC… if we feel like this project really heavily affects certain SIGs, it's on us to be reaching out to those SIGs and figuring it out. But I don't know that we want…
all the SIGs have to vote on every project, or something like that.
**Josh Suereth** 27:10 Well, I… let's, yeah, go ahead, go ahead, Alolita, sorry.
**Alolita Sharma** 27:14 No, no, I just wanted to echo what Ted was saying, but Josh, to your point,
Again, communication across SIGs, you know, on specific proposals and responses that they need to provide is a aspect that most maintainers, at least who I have talked to or worked with.
continue to see a gap in. So, whether that's at the initial, you know, time when the project proposal is made in the community SIG, but then, you know, fast forward into maturity on the SIGs themselves.
that's an issue, right? I just wanted to echo that, because that's something that we have… I've definitely seen direct feedback from the maintainers on, that they don't… just don't know.
When they need to, when and where they can coordinate, unless they know the maintainers personally or, you know, can reach out.
Pablo?
**Pablo Baeyens** 28:17 Ted, when you say you don't want SIGS to vote on proposals or so, I'm not necessarily suggesting that, but how do you plan on 6 to be aware or, like, commit to things if they do not have the…
Autonomy to decide on what to work on, and, like, say, yes, we will work on this.
**Ted Young** 28:38 I feel like Josh is saying that discussion is out of scope, right? Like, I'm saying where this feels useful is, like, step two, we're figuring out the projects and getting them together, but, like, once we're like, okay, this could be a real thing…
because, like, everyone's ready to go and do it, like, how do we… how do we coordinate spec work with the SIGs after that? We don't… we don't have a process.
**Josh Suereth** 28:58 Well, this is where I think we need to take the project proposal more seriously. It goes back to, like, the approval process of, like, when does the GC mark something as approved?
we have this notion that you need to have maintainers sponsor your project. And, like, to what Pablo's saying here, everything I see in here, we have in our project process, but we're not really doing it.
Like, when someone signs up to sponsor a project from a SIG, there should be an expectation they're participating in that SIG and helping it be successful. And, like, where's that communication? It's in the SIG. It's in the project. Like, when you sign up and say, I'm gonna sponsor this, it means I'm actively gonna help you in some fashion.
Right? I am signing up my time to help this project. And we need to be very careful about not just taking in a whole bunch of projects for which there's no active investment or interest in.
That's the overall issue here. And I agree with you, Ted, that we're running into problems with that second phase, partly it's because I think we're saying yes to everything.
And to the detriment of all of our maintainers. There's so many things that we have to pay attention to that are becoming problematic. I want to actually say, like, profiling is trying to go alpha, and they have gone from being an escalating sponsorship to now, they're guiding.
Which means I'm over my limit, in terms of amount of time I have to pay attention to things.
And, like, we need to figure out ways to address this, because SIGs are not, anyway, we have an attention span problem here in OTEL a little bit, and I think we have to be careful. We need to get people to sign up, and I really like what you're saying, Pablo, because I do really think that this works out.
It means we have to take our own process seriously. We have to make sure people are signed up, we have to make sure people can commit, and we need to not overburden people today.
And this also means we need to grow maintainers, right? So I think all of that's true. What I want to focus on right now… the reason I'm trying to, like, short-circuit this is I really want to focus on the project proposal process, and what we do there, and I think the follow-on effects, I agree, are important, and I agree there's a hole.
But partly if we set expectations early with this, right?
can we get to the point where folks are committed to participating with these SIGs, so we know, like, what we're signed up for, so we know what the commitment will be, and that we take it very seriously of, like, okay, this will actually need help from this SIG, and they will have to work together, and we need someone involved there over here.
And if the SIG is willing to delegate to someone else, great, they should be an approver, a maintainer status, like, they're willing to commit the hard work.
Right?
Okay, I think I said enough, but…
Was it Jack or Carl?
**Ted Young** 31:42 I gotta… I wanna really push hard against that, Josh. I would like the TC to come back and show that we've been accepting project proposals that we shouldn't be doing. I think that's a myth. I think we have a bottleneck in the TC because half the TC is working hard, and half the TC has their foot out the door.
That's the reality.
**Josh Suereth** 32:05 Then let's address that problem straight up.
Right? Like, but if we keep accepting projects without having TC sponsorship behind them.
**Ted Young** 32:13 That we can't do anymore, right? But it's…
It's, like, that's… that's a bottleneck. It's like a literal bottleneck of, like, we've got 5 people this has to go through, and we should have 10.
Okay, said my piece.
**Alolita Sharma** 32:37 No, I think, Riley said the same.
Thank Carlos. Cover it.
**Carlos Alberto Cortez** 32:47 probably we don't have to discuss that here, but probably we should write down some… something, probably because of the TC, but on… on the aspect of adding border to single maintainers, I think that probably we should take into account OTEPs.
Not always within account staffing there.
Sometimes we do, sometimes we don't, but effectively, when we create our tabs, and they may be accepted, because probably that's a great thing to do.
But I am afraid now that I'm… we're talking about that, that, for example, the TC may be reviewing that, and we as TC, as a group, we think it's great to implement that, and we approve that, but then the maintainers didn't review that.
or they're not completely in the loop, and then it's like, suddenly they have to implement this new thing that is coming to them. So we should think about that. I don't know whether it's the GC NTC or ONTC, but let's gripe that down somewhere so we can discuss that in some other call.
**Jack Berg** 33:42 Yeah, so I was gonna offer a suggestion in the… in terms of concrete solutions on how we might increase the visibility and the trade-offs that we're actively making. And actually, what Carlos said, I think, segues into my suggestion. So, you know, we… we have kind of three
kind of large, high-order units of work that have some overlap. We have SIGs, we have projects, and we have OTEPs.
And in all of these things, we need to get a bunch of people to agree on them, and they have, like, implications for the project going forward in terms of our attention. Sometimes a project is a SIG, sometimes it's not.
Sometimes an OTEP is, like, covered by a project or a SIG, sometimes they're not, so, like, you know, they're partially overlapping sometimes. And, what I think it would be good to do
is if, you know, I guess stepping back a second, we also have this spreadsheet out there that Josh Sareth put together a while back that shows a list of all the SIGs, and all the TC sponsors, and the sponsorship level, and what we would want the target to be. That is an artifact that is, like, not kept up to date, but shows actively where we are investing attention.
What if we could reproduce that accurately based off structured data in the community repo, like, on a daily basis?
Like, a report.
Like, we have this sigs.yaml document in the root of community, which shows a list of all the SIGs and who the TC sponsor is. What if we could produce a similar artifact for projects, or, you know, include projects into this sigs.yaml file and kind of re… rethink, you know, what it is conceptually, and then build simple reporting that shows, you know.
for… you could slice and dice it by a variety of factors. You could show, like, a list of all the projects in SIGs, and their sponsorship level, and the key people that are contributing, and then you could also slice and dice it by, sort of, like, TC members, so you could see, kind of, at a glance, who is at capacity, near capacity, or has capacity.
And if you actively want to free up capacity for a new project.
like, or first of all, like, you can point to this artifact and say, like, look, we have to reject this project because we clearly don't have capacity. And if you want to actively clear up capacity for it, you know, here's the map, here's the roadmap of what we… where we're spending attention right now, so figure out what we're gonna cut.
Or figure out what we're gonna finish, and when finishing something opens up attention for something else.
**Josh Suereth** 36:22 Yeah, I just, I just want to add, like…
So, Ted, I'm not… I'm not gonna deny at all what you say. I think there's a different level of investment across TC members.
I also think that that will always be true.
But… I think what… what we, what we should do.
is measure it, and if we see a systemic problem, we need to address it. We need to have hard conversations. And I would like that to be a non-emotional
conversation. If we can make it so it's, like, a process thing, so it's clear, so we understand what's going on, that's gonna make this a lot easier for all of us.
But to Jack's point, yeah, if someone can sign up to actually track this, I think updating SIG's YAML, putting it in there, having, like, a dump of, like, how loaded the TC is, so we get a feel.
for what we're sponsoring, where things are, how much people are signing up for. I will say that not all sponsorship levels are equal either. Like I said, profiling, I think, is now at a stage where it needs to be a guiding sponsorship, no longer escalating. Tigran and I were sharing the responsibility
And both of us have had to put in a lot of time recently for it.
And I think that it's valuable for OTEL that we have done so.
But we need to, like, be able to handle that as well. Sometimes projects go through a phase where, yeah, maybe we didn't have to pay attention, but now we do.
So… yeah.
**Ted Young** 37:46 So, totally agree. I mean, I think that's part of the goal of getting all of this structured and all written down, is because we can then track it, right? And when we had no structure, like, what would we be tracking, even? And I could totally see us having the ability to mod that so we can add weights to it, so just…
Because the point is just to acknowledge, like, people's capacities.
And I also want to be like, yeah, you know, working OSS is not a job, we don't pay people, people have different levels of commitments, but if we're gonna be, like, the TC is capped at 10,
I just think we need to, like, we need to be more flexible on that front. We're either, like, say, TC members can work part-time, and we can have more of them, or we have, like.
a way of, like, segmenting that workout so we can have more people doing some of this, but not keys to other things. Like, whatever it is, we need to figure out a way to expand some capacity there.
**Josh Suereth** 38:42 I agree, but, like, let's not make a 9-month baby mistake here of, like, there's coordination headwinds, there's design, there's, like, aspects of the project that are non-negotiable.
**Ted Young** 38:52 That's right.
**Josh Suereth** 38:52 And there is a limit, and there's a limit to what we can do as a community, and we need to be aware of that. There's a limit to, like, getting approvals through, and that we need to protect a little bit, more than we have been.
**Ted Young** 39:06 So this is a genuine request, like, I would like to know, like, it would be good to do a post-mortem if we feel like there are projects that we accepted, and we're like, we shouldn't have accepted that.
Like, I'm totally fine doing a post-mortem on that, and being like, you know, why should we have, like, held off on this or said no to this when we said yes? Because we keep hearing, like, oh, we're saying yes to too many things, right?
**Alolita Sharma** 39:31 Yeah, that's a good idea.
**Josh Suereth** 39:32 I'm gonna put it in the private chat for you. I'll let you know exactly what project. It had 3 TC members step down from it.
**Ted Young** 39:43 Okay, perfect.
Like, like, let's do that triage. I think that's an important part.
**Trask Stalnaker** 39:49 You named the project.
**Ted Young** 39:52 Yeah.
**Tigran Najaryan** 39:53 So, Pat, can I… can we maybe… Talk about that. Do we…
Setting aside the fact that maybe TC needs to allocate more capacity to existing projects, or maybe some TC members are not
spending enough time being a TC member. It's a discussion that I think needs to happen, but setting aside that for a second, do we believe that OpenTelemetry as a whole
Needs more projects, needs more capacity, that we need to expand.
I think it's not obvious to me that we actually are focused in the wrong way, and that that focus needs to be broader, and there is more things that we need to do as a project.
as opposed to, no, actually, the focus is correct, we just need to go deeper into what we're doing. I don't know… we haven't discussed this, right, in the past. I think it's a question that we need to be asking before we make the call on
Yes, we need more TC capacity, because we need to do more projects.
**Ted Young** 41:02 So we've made two… there's been two attempts that I know of to try to separate this project out, right? Because I totally agree this is another way to do it, is to also figure out some boundaries.
One is to have a sandbox.
I was really opposed to the idea of a sandbox, because that just sounds like a monster training academy, where we build up the exact kind of projects we don't want, and then release them on ourselves once they're too big to deal with. So, like, I've been against having something segmented by life cycle.
Right? Because that just sounds like it'll become our problem eventually. So how is there a way we can permanently put things into another camp?
Where we're like, this is blessed and healthy, but also, like, we're… it's not taking capacity away from this group.
I propose DevTools as maybe a way to do it. I picked the exact wrong project to… to, like, point that at with, like, MCP stuff, because that turns out what everyone wanted was just, like, a thin layer built into the different things.
So…
**Tigran Najaryan** 42:04 Honestly, Ted, that sounds a bit… that sounds a bit like, no, we don't think that's the right thing for OpenTelemetry, but we're not willing to say no.
And so, because of that, we're saying, okay, do it in some other way, but still be associated with OpenTelemetry.
**Ted Young** 42:21 I mean, I think there's more people than just us who can maintain things. I think we are not the only bastion of knowledge, but I do believe all the production stuff really needs to be coherent.
And to some degree, the DevTools stuff, right, people are fine… much more fine with experimental things, things coming and going and, like, other stuff. That stuff needs to be less coordinated. It's sort of downstream of production.
So, I would be fine saying, like, what we need to focus on as a community is making sure all the production stuff, the standards that people, like.
like, depend upon, like, that's our primary goal. And, like, everything else is kind of like icing.
**Tigran Najaryan** 43:02 Okay. Is it the, I guess, the universal feeling in this room that we need to be doing more? There is more things that we should do, but we just don't have the capacity to do? And that capacity is the… I guess, and the TC is the bottleneck. Is that the general feeling here?
It's a genuine question. I'd like to understand if that's true or no.
**Morgan McLean** 43:23 I would say for myself, to a degree, yes. I feel… I would have said yes more strongly probably a year or two ago than I would have today, but I might be ignorant of some of the pressures we're under.
**Tigran Najaryan** 43:37 Okay.
**Josh Suereth** 43:39 I also want to ask, Ted, the thing that you were suggesting there, how does that not wind up a mess that we have to clean up later? Like, as a TC member, that just sounds disastrous to me. Like, we're basically saying, hey, we want something that doesn't have the technical oversight we think the product needs.
**Ted Young** 43:55 No, no, no, I'm saying…
I'm saying spinning it out by having other people do technical oversight for that stuff. That's all I was noting. I'm like, hey, if people want to spin out a DevTools wing.
additional people with more DevTool-y kind of focus, because it seems to be more of a different community that likes to build and hang out and work on those kinds of things, right? Like, we could spin that out.
**Josh Suereth** 44:18 How's that not just a TC, then, right? That's what I'm saying, like, like, basically…
**Ted Young** 44:23 That's why I was like, put it in a different org, completely get it off our plate. That's why I… that was my strong proposal. It's like, what if we very firmly turned that into a second project and said, not our problem?
**Liudmila Molkova** 44:35 We already have…
**Trask Stalnaker** 44:36 CNCF, why not a new CNCF project at that point?
**Ted Young** 44:41 Maybe, yeah, sure.
**Liudmila Molkova** 44:43 We already have capability to delegate to maintainers and spec sponsors. We have people inside the project that can provide technical oversight, but it's an explicit choice to say, this can be delegated.
Currently we are saying, okay, MCP can be delegated because it's under CollectorSIG, and maintainers of collector SIG can provide this capacity. If it's not over… there is no oversight from technical people inside open telemetry community.
that are owners, maintainers of the SIG, that's a separate question. I don't agree with that.
**Alolita Sharma** 45:26 Yeah, and to Lyudmilla's point again, I think there's only so much of
Deferring we can do, because,
you know, there are two things that are happening. One is, of course, that everybody wants to be under the hotel umbrella in one way or the other, and therefore leverage the project's, you know, successes, kind of
On, and adding that to their coattails. And then the other part is that it is actually become harder for project proposals to go to the CNCF and become actual projects.
the ratio of rejection at even the TOC level has gone up a fair bit. So, they've become more stringent, they're reviewing more things, you know, in terms of the requirements, and it's not that easy to get set up as a project.
So those, those things, you know, then again, push most proposals back to us, because…
Hey, you know, it's easier to be under a project umbrella than not.
**Trask Stalnaker** 46:39 just wanted to try to answer Tigrin's question,
with maybe a unfortunately non-answer, which is that it's not clear… I… I don't… I haven't seen this groundswell of people doing more work than we…
can handle, like, I mean, at least in…
I see more places where we're lacking involvement, people who are…
the developers, engineers who are doing semantic conventions, Gen AI, you know, the collector contribib, like, there's… we have a lot of prod things that are just understaffed, and I don't think that is due to lack of…
TC involvement. I mean, yes, would it be amazing to have somebody of TC, who could do, you know, leading more, like, actually doing that work? Yes, but that's not sort of our, you know, we… we need more…
people who are really stepping up, willing to do that work before I think that… Week.
Would expand, be even successful at expanding the scope.
**Tigran Najaryan** 48:01 In our model, that's not a PC job, really, right, trust me? That's more of a maintainer's job, right? So that… that lack of capacity to drive particular projects more strongly…
I don't think it's necessarily a problem with having not enough TC capacity.
the lack of TC capacity, we see that in the inability to accept new projects.
I accept that completely, right? But the fact that some projects are not quite healthy is… wealth.
In some cases, it may be that because the TC is not doing a great job, but in most cases, it's because we don't have enough maintainers and not enough
People who actually… Active maintainers. Active maintainers, yes, if you will, yeah.
**Ted Young** 48:51 Even if we have a great process, we're still gonna have, you know, open source facts of life things happening.
But just to put a bow on it, I feel like a concrete thing proposed in the, chat is just, let's mod the project file, right, for starters, to include a section around, like, SIG impacts, and getting, like, where do we expect this to impact SIGs, and…
And then to do some work as part of that, to check in with those SIGs, and make sure this is okay.
And then I think the other thing we were talking about earlier, that I know it's, like, out of scope for this, but this seems to be…
Around, like, how do we go from, like, project and spec stuff to… to SIG work? We've kind of left that…
Left that to the wind, and that's worked out for us in the past, but it feels like less and less.
that would work out. So it's getting those maintainers involved more quickly.
Okay. And I definitely don't… don't misinterpret me as saying it's all the TC's fault, that is not what I was trying to say. I just want us to acknowledge that, like, we could increase capacity there as well, and we should.
**Josh Suereth** 50:05 I… I… I mean…
**Ted Young** 50:07 I think we should resolve… It's nobody's fault, it's not a blame thing, you know?
**Josh Suereth** 50:11 Whether or not we increase TC capacity, meaning more headcount on the TC, like more people.
We should have that as a separate discussion. I think we already have that coordination.
Where I think just adding more people makes us slower. Like, I don't think you actually make it faster, it doesn't improve anything we need here. With the profiling review today, one of the things we had to do was have a discussion in the TC where we all share
What profiling's doing, and get concerns from folks, right? That doesn't get faster with more people.
**Ted Young** 50:44 It's clear that as the project… Grows, like, the cross-communication grows.
combinatorially, right? And that's a promise. Yes, right.
**Tigran Najaryan** 50:53 Actually, to Josh's point, we've seen that it… in some cases, it can be counterproductive when you get more TC members involved in a particular project, because now they pull in different directions, and it's harder to get that alignment.
So, again, I'm with Josh on this. It would appear to me we would… we should try to address
first, the, I guess, how much time each individual TC member allocates to the TC work before we think about expanding the TC to a larger number of people.
**Ted Young** 51:29 I'm fine getting data first, I think that's totally reasonable.
**Josh Suereth** 51:33 Okay. Alright, so…
to bring it… to bring it back into things that… action items. I think the first set of faster feedback, I don't think there was a lot of contention there. This… this making trade-offs, we had a lot of good discussions on. Pablo, do you want to put this into… into practice and go forward with, like, do you feel like you have enough from this discussion to know what you would do
with project proposals to improve, making trade-offs visible of, like, you know, signing up for work, making it clear.
I think when we talk…
**Pablo Baeyens** 52:07 on the chat, and what Jack suggested is a good next step. So, including on the project proposal, the impacted SIGs, and that's easy enough to make, and we can see whether that improves things.
**Josh Suereth** 52:20 Great. Alright, so let's make that as the action item. For setting clear expectations, Ludmila, this is the one you signed up for, and I know you're going to KubeCon. This is about,
I think we have some proposal here. 7, we're just gonna try to pick this one up.
**Liudmila Molkova** 52:36 Yeah, if anybody else wants to work on this, go for it, but if not, I will do it as soon as I can. The TC sponsorship level.
**Josh Suereth** 52:48 Yeah, I feel like this one, and confirm if I'm wrong from this discussion, the next step here is to actually update the SIGS YAML file to put TC Sponsorship in and get a report of TC Sponsorship load. Is that accurate? Okay.
**Liudmila Molkova** 53:03 Yep.
**Josh Suereth** 53:03 And I know, I know that you mentioned several times in other SIGs that you're super busy the next 3 weeks. If someone else can pick this up and do that, that would be ideal.
I like it.
**Jack Berg** 53:13 do that, but there's, like, a question in my head about, like, the implementation, which is just, like, what are the relationships between these, sort of, slightly overlapping work streams we have? SIGs, projects, OTEPs.
Like, we need to formalize this somehow so that we can structure the data around our commitments to some, like, common representation, some common type, if you will, and, you know, build reports based off of it.
So, I gotta figure that out, maybe it'll be messy, I'll try to come up with something.
You're muted, Josh.
**Josh Suereth** 53:51 Oh, yeah, I… I agree with you. I think… I think that would be ideal to, if anyone from the GC wants to help with this part, let us know.
But I think we have… so, Pablo owns this, I'm gonna own this and drive this. Setting clear expectations, Severin's gonna own, and Jack, you're gonna take on this one. So we have…
a set of clear things we need to do. We have a larger set of problems we need to continue to address, and I think we'll continue to talk about those. And I'm glad we had this discussion, because I think it's good to just put this all out in the open. So let's continue on the broader problems, but in terms of, like, tractable work.
do we feel like we can put a pin in this? We have a set of things that we're going to be doing, we have a set of larger problems we can talk about in the future, but my key is we're taking action, and we have… we have those actions. Anyone have concerns with the ones that we listed?
Awesome.
Thank you, GC, that was,
This was quite a spicy discussion, and I appreciate that we can have these, and do it publicly.
**Alolita Sharma** 54:53 That's me.
**Jack Berg** 54:58 Are we finishing 5 minutes early?
**Alolita Sharma** 55:01 We almost are.
**Jack Berg** 55:03 That's great.
**Josh Suereth** 55:05 I was trying to moderate there, so apologies when I said, hey, this is out of scope, yeah.
**Alolita Sharma** 55:11 But Josh, you need a gong.
**Josh Suereth** 55:13 I need a gong.
**Alolita Sharma** 55:15 Thank you.
**Josh Suereth** 55:17 Well, then I wouldn't be able to hear what you say, ever.
**Alolita Sharma** 55:19 Oof!
**Josh Suereth** 55:23 Yes, this was published.
**Juraci Paixão Kröhling** 55:27 I was just joking, yes.
**Josh Suereth** 55:29 Were there any other topics? I mean, I know I monopolized everything with this one, but,
Nope. Cool.
**Pablo Baeyens** 55:37 Like, is the…
**Trask Stalnaker** 55:39 This table, by default.
**Pablo Baeyens** 55:41 OTAB, would be… I think there was some discussion on the maintainers, on specification, sick call about it, but I wasn't there. But, I think Austin is looking for reviews there, so if people can take a look.
**Alolita Sharma** 56:00 Bob Nagani, add the link?
I'll share it.
**Ted Young** 56:04 mask.
**Trask Stalnaker** 56:07 Can I ask for a quick, vote on the Zig Zig?
Proposal.
Or can I ask the GC to vote on it in… the channel?
I think we're all live.
**Alolita Sharma** 56:22 Channel is better, we should read it.
**Trask Stalnaker** 56:24 we've got TC on board, we've got, two existing maintainers, as approvers, and three,
maintainers of the existing project, I think it looks well-staffed.
**jmacdonald** 56:41 I just approved the community request as well.
**Trask Stalnaker** 56:45 Thank you, John. Thank you.
**Alolita Sharma** 56:50 On the channel, then, Trask. Yep. Yep.
Sounds good.
Thanks, everyone.
**Trask Stalnaker** 56:59 Debates.
**Tigran Najaryan** 57:00 See ya, bye. Bye.
**Pablo Baeyens** 57:01 See ya!
**Morgan McLean** 57:02 be late.
**Severin Neumann** 57:02 Bye-bye.
**Alolita Sharma** 57:03 Bye.
