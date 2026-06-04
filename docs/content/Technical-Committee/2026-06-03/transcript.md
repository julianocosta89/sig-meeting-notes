SIG: Technical Committee
Date: 2026-06-03
Duration: 53 minutes
============================================================

## Zoom Recording Transcript

**Reiley** 01:11 Hello, Tigran.
**Tigran Najaryan** 01:17 I'm old.
**Liudmila Molkova** 01:18 Hey, everyone.
**Reiley** 01:19 Hammer.
No.
Let me share my desktop.
Can you see what they saw?
**Liudmila Molkova** 02:11 Yep.
**Reiley** 02:14 Okay, let's do the triage.
Okay.
Alright, Central OpenTelemetry Benchmark.
I think Cigio has a proposal, like the old type, already.
**Tigran Najaryan** 03:08 Yeah, and this is the project, right? I think that it was an OTAP initially, but it needs to be a project, really, because, yeah, it's not an OTAB.
**Reiley** 03:16 And the old hype has maybe, like, 2 approvals, I think.
**Tigran Najaryan** 03:25 And I guess, as a project, it needs to go through the project process, essentially.
**Reiley** 03:30 Yeah.
**Tigran Najaryan** 03:35 Is it… it's already in our inbox, right? It landed in the inbox.
**Reiley** 03:39 It is, yeah, it is in the inbox.
**Tigran Najaryan** 03:41 Okay.
**Reiley** 03:42 Yes, I… I think we should give some time for the… would have.
**Tigran Najaryan** 03:47 What is the… what is the suggested staffing for the… for the project?
**Reiley** 04:04 maintainer tool.
And it didn't mention a TC sponsor, I think.
**Tigran Najaryan** 04:13 This is going to be a cross… OpenTelemetry project, though. This is not…
**Reiley** 04:19 limit.
**Tigran Najaryan** 04:20 to a particular Sikh, so when they are saying.
they will maintain the harness themselves. It still works for other… all… virtually all other language Sikhs who want to opt into this, right?
So, we will have to make a decision on this. Can be… we can say that it's totally optional, and the language seeks can voluntarily opt into that, in which case.
Fine, we're not adding more work than they are willing to take on.
But if this needs to be mandatory, then that's a completely different story in that case, right? They will need to find… make sure that they have the support of the language seeks before we go ahead and approve the project.
**Reiley** 05:05 Yeah, I agree. We don't have an exception for any, like, quote-unquote small product, right? A project proposal has a template, has a process. We can go through that.
**Tigran Najaryan** 05:15 Yeah.
**Reiley** 05:16 Also, I think it's probably too early. I want us to first see a reasonable number of approvals on the old tab first.
Before we start this, right?
**Jack Berg** 05:28 So, if we… if we want to have that type of requirement, let's, let's guide people that might be potentially reviewing this, that, you know.
if you… if you agree with this, if you want to see this move forward, please also review the OTEP and approve that, because we're looking to that as a signal.
**Reiley** 05:47 Okay.
Sounds far, sharp?
**Jack Berg** 06:05 Yes.
Just intuitively, when I'm reviewing this stuff, my intuition is that this isn't as big of a project as others that we've seen proposed, it seems like it has a sort of well-bounded scope.
Like, if you had the support of maintainers in 3 or more languages, that you could, you know, get something reasonably good in a short amount of time.
So, yeah, I don't know what that means. I guess I'm just… I don't have the… I don't have the immediate reaction that we have to have, like, an elevated TC sponsorship level, and that this is something that's going to drag on for years.
For what it's worth.
**Reiley** 06:52 Yeah, one… one thing I'm… I'm a little bit curious is, Like, if this product is becoming bigger.
how is this going to be related to the Diamond project?
**Liudmila Molkova** 07:08 Diamond Process?
**Reiley** 07:10 the, the OpenTelemetry demo, like, like.
**Liudmila Molkova** 07:12 Oh.
**Reiley** 07:13 blueprint, the open timesheet demo, and the benchmark, in my opinion, they're highly related. I worry about, for example, if the blueprints are saying.
we recommend that people do XYZ. Then the demo is showing something else, like full bar, then the benchmark is doing something else. I feel it's a little bit chaotic.
And people will get, like, really confused, and if they want to recommend, for example, they want to say, instead of doing this, we should do that, do they need to go and update 3 different places?
Anyway, so I have a recommendation for Sido, but I think that's a bigger topic. It doesn't have to be a blogger.
**Jack Berg** 07:51 And the benchmarks that I've written for Java that are meant to be user-facing, and I view those benchmarks as sort of a prototype or sort of language-specific version of what CJO is providing here, and I hope we can, like, my benchmarks will evolve into or be a part of this, of CJO's thing.
So, in those, I, you know, let's take metrics, for example. You're trying to measure, different metric situations, and you don't just pick one. You pick a set of scenarios that reflect how people will use the metrics API. So, you know, you use the different instruments. That's one of the dimensions in there. What instrument are you choosing? Histogram or counter? You choose different attribute set sizes, like small or big. You choose different, like, types of scenarios, like whether the attribute sets can be bound at the application initialization time, or they can only be computed at record time. And so, like, if you choose your scenarios right, then, like, the benchmarks, like, they don't have to be opinionated and aligned with the demo and with the… what was the other project? The…
**Reiley** 09:03 open.
**Jack Berg** 09:04 the blueprints, right? Because, like, you know, the benchmarks are just trying to, like, measure what's possible with the API and the different common scenarios. So as long as they capture the things that are in the demo, in the blueprints, then, you know, they're still representative.
**Reiley** 09:20 Dune.
Okay, so let's move to the next one.
The support maturity model.
**Tigran Najaryan** 09:36 Rockpad and I commented on this. We asked them to… change… The formulation of the… of the project.
So that it doesn't become a rating of other CNCF projects.
I don't know if they… actually made changes.
Yet.
Last comment is from Ted.
As far as I remember, they did reply, okay.
But I don't know why this is in our inbox anymore.
shouldn't be.
**Jack Berg** 10:27 Should we remove the label? It's not… oh, it is still in our inbox. Should we remove the label and send a message in the GCTC channel saying, like, you know, we removed the label, the ball's in your court, please correct us if you think we're wrong.
**Reiley** 10:42 Yeah. Awesome.
**Tigran Najaryan** 10:43 I think we can do that, yeah, yeah.
**Reiley** 11:19 By the way, do we know who added the TC inbox?
**Liudmila Molkova** 11:25 It should go on the PR.
**Reiley** 11:28 It's, like, automatically added, or someone added that.
**Armin (Dynatrace)** 11:31 I think it's the GC usually, right?
**Jack Berg** 11:35 Yeah, but who from the GC?
**Reiley** 11:40 No, it's, GitHub Actions, right, so… That's it.
**Armin (Dynatrace)** 11:43 The project proposal? Yeah, right.
**Reiley** 11:48 Yeah, then I probably need to also follow up and see what's the criteria with… do we want every product proposal to be automatically assigned to TC inbox? For example, if we're already running out of capacity, then What does that mean? Do we even spend time here, or not?
**Tigran Najaryan** 12:11 I think we asked for… for this to happen at some point, right? We wanted to be notified early so that we can provide an opinion. That… that was… That's what I remember at some point, because… But before that, the GC looked into the project, they made a call, and then told us that this is something that is coming your ways, and it was a surprise to us. This is so that it's not a surprise anymore.
**Reiley** 12:40 This particular…
**Tigran Najaryan** 12:41 particular one, I think they need to rework what they are proposing anyway.
And Ted and I both told them that it needs to change.
I don't know if they have changed anything, I'm not seeing any new commits there.
**Reiley** 12:55 Then once they're changed, they will come back, and we expect that will be in the TC inbox, and someone will be assigned to review that.
**Tigran Najaryan** 13:03 I think that's fine, right? Depending on what the change is, right? What does that look like?
**Reiley** 13:08 Okay, sounds good.
I think this is related to the discussion yesterday.
I think Braden is already working on… some of the PRs.
Anyways, so I remember the discussion has a lot of supports.
So… I feel like the… the ship has already started.
**jmacdonald** 13:40 I agree. This… this was, like, work that was underway in the collector anyway, and then people started asking for the same in this SDK, so it seems like a pretty reasonable and easy one to accept.
**Reiley** 13:55 Folks agree?
**Carlos Alberto Cortez** 13:57 I guess that I just have a small question, it's not really important, but I'm curious where this, the output will end up.
Probably everything will be kept in Google Docs for the time being, and when the time comes, it will land in the specification.
And probably the collector will have its own section.
Is that your impression, Jim McD?
**jmacdonald** 14:21 That we would… Oh, sorry, I didn't quite follow the question.
**Carlos Alberto Cortez** 14:28 Yeah, well, anyway, let me, take a step back. There was, some question in the, in the, in the PR. Somebody was asking about where… This will be, like, the discussion will happen, and we're… and there was a note by the author saying that they will put this information in some place, maybe some repository, even.
for me, it was kind of weird. It's like, why doesn't that go… even.
**jmacdonald** 14:55 True, yeah. Braden has been using GitHub Gists to share his design philosophy.
And, you know, I think an OTEP is more appropriate, at this point. Maybe that's good feedback for… or at least for Braden's approach.
I think he was doing that because it was sort of like, we need a place to brainstorm, and it's across SIGs, so, like… the entire collector's SIG is not only the only party interested, and so on.
But I… but I can recommend to Brayden that we start with an OTEP.
**Carlos Alberto Cortez** 15:32 Or Google Docs, or, you know, I mean, I don't know, but something that can be super easy to access, and it's not too complicated either, just, you know.
Simple, and that other people can review.
That's all.
**Tigran Najaryan** 15:44 If this is going to be a project, it's going to be a pretty short one, I assume, right? The project is necessary so that everybody can align on what the batching approach is, and that's it. As long as people are on board.
doesn't have to be implemented by every language, as long as there is an agreement to a particular approach by collector and by language seeks, if there is an OTEP that is approved and it is accepted, we're good then. I think we don't need the project as a project to continue. That now becomes part of the spec, and then the language 6 can go ahead and implement that part of the spec, just like any other new capability we add to the spec. That's how I see it. So this is going to be a pretty short-lived project.
**jmacdonald** 16:27 Ideally, yes.
**Reiley** 16:30 Okay, I have a question. I guess the TC doesn't have the power to accept a community issue. We should just mark it as TCA reviewed, I guess.
The GC has the power, right, if I remember correctly.
Do you think so?
**Tigran Najaryan** 16:47 Yeah.
Yeah, I think it's… it's fine. I guess we can approve the project.
Like, use the regular proof feature.
**Reiley** 16:55 Yeah, so what was the TC revealed?
And for this one, I also see TC revealed. TC revealed could mean either we reviewed, we agree, then we'll have approvals here, or we reviewed, and we disagree, we have suggestions, and we'll just… Make comments there.
**Bogdan Drutu** 17:15 Do you wanna make a comment? Do you wanna add a comment at the end?
With the result.
**Reiley** 17:21 What comment do you want to make?
**Bogdan Drutu** 17:23 Right? TC approved, TC denied, whatever.
Decision was made.
**Reiley** 17:54 Okay, so we all know this one.
**Tigran Najaryan** 18:03 Unlike the new name.
**Reiley** 18:06 Yeah.
**Tigran Najaryan** 18:08 it's…
**Reiley** 18:08 Yeah.
**Tigran Najaryan** 18:09 Yeah.
That's a good name.
**Reiley** 18:13 Yeah, so… from… from my understanding, this is something, like, we want to do. This is about being more explicit, have clarity, and be accountable.
But there are a lot of things mixed here, and I gave some suggestions about like, how we divide and conquer, and also the names that one has to avoid, just to, like… Not introducing additional confusion.
I… I guess I still want to see an updated PR.
Like, the current one still seems, like, a little bit murky to me. That's my take.
**Tigran Najaryan** 18:55 So, the question I have is, based on the new name, the name of the project is… Post-graduation roadmap.
Is the project… About producing the roadmap, or about producing the roadmap and implementing the roadmap?
Does it have to live for the entire duration of that roadmap? Because you always have some sort of a roadmap, right?
for OpenTelemetry. There will always be something, some continuation of the project, of OpenTelemetry as a whole.
if the… We could say that the purpose of the project is to figure out what is the… what's the post-graduation roadmap, what's the future roadmap for OpenTelemetry, run that for… that project for whatever number of weeks you need to run it.
come back and say, we're done, this is the roadmap, we commit to this particular roadmap as of now, and everybody knows, language seeks to implement this, collector implement that, Opam implement this, and etc, right?
could it be the right approach in this case? So that it's not a never-ending project otherwise, right? That's what… if you say that the project is for Until everything on the roadmap is complete.
As long as… once that is complete, you're going to open another one, because there's going to be a new roadmap after that roadmap, right?
**Reiley** 20:18 I think this is a meta project. The goal is to… She's like… Like, define the work, identify the work.
**Tigran Najaryan** 20:27 I mean, yes, and roadmap is that definition, right? What is the roadmap? It's the definition of what you plan to do. So, if that's the case, then I'm… I was worried about the scope of the project, as it is written in this proposal, but if If the work that is expected to happen in the project is the definition of the roadmap, that's fine. In that case, all it needs to say, let's say, is for all pump, right? For all pump is… here's the roadmap. I actually have the roadmap already. I can just bring it to Ted, and he can put it into a document. We're done. I only need, let's say, a couple hours for that.
If the project is to implement all of that, that's an entirely different story.
**Reiley** 21:14 Right.
I don't think this one is talking about implementation, but if you think it's unclear, I think we should ask that.
**Tigran Najaryan** 21:24 Yeah, yeah. I would suggest that we do exactly that, right? So that the project… the purpose of the project is to bring people together from all of OpenTelemetry.
to agree on what is the continuation after the graduation, what do we do, come up with that roadmap, we'll spend maybe a few weeks on that, maybe a couple months at most, and we're done. We'll publish the roadmap, and that will be essentially the expectation of What needs to happen in the next year, couple years, whatever it is that we choose to have the timeline for that roadmap.
**Reiley** 22:01 And, I'm… I'm already curious, but let's go with Baldan first. Balda?
**Bogdan Drutu** 22:07 We should do?
We should follow up that the SIGs will implement this roadmap, and who is… Who's gonna be responsible to make sure that We just don't publish a roadmap for the… Sick of publishing something, but somebody is taking that.
**Tigran Najaryan** 22:27 Yeah, and we usually don't have anybody enforcing this sort of thing, so that's a good point.
**Reiley** 22:36 I have a quick question about the roadmap versus the ongoing project proposal. So, for example, if we publish a roadmap saying we're going to do these five things, and then someone come and have a project proposal, they're saying, this is awesome, a lot of people are super excited.
Are we going to accept that and come back to the roadmap and make the changes? And we're going to say, okay, we're going to drop one item from the roadmap because there's a new thing.
**Tigran Najaryan** 23:03 Go.
**Reiley** 23:03 Or…
**Tigran Najaryan** 23:04 I think that' Very good question, Ali. The purpose of the roadmap is to declare what is going to be your focus.
For the next whatever number of… months, but I think it doesn't have to be set in stone. It's okay to make adjustments.
So, the call has to be made every time. If there is a proposal.
what is very good about having the roadmap, you can always assess new proposals against that roadmap. You can say what you're suggesting is interesting, but it is not aligned with our current roadmap, that's why we're not going to do it. That's essentially a tool for making decisions.
That's, by the way, what we did for Before Pump very recently. There was so many different requests coming in for the… for the protocol to change at this and add that, and we said, we're going to come up with the, essentially, a roadmap for the next few quarters, and we'll stick to it.
When we can. And it's a great tool. Now, when somebody comes and tells me, I want this, I tell them, you know what? Wait, maybe, right? But this is not what we're going to do now, because we have other work to do, here's our roadmap. I like that as a tool for this sort of discussions.
**Bogdan Drutu** 24:30 Should we… should we create… projects out of Roadmap, if we… And just stick with this, say, 10 projects, and say this is what the community is gonna work on?
**Liudmila Molkova** 24:47 I think maybe it's the… not individual projects, but the projects with the issues. So for example, I don't know, the collector V1 is already happening, and this work is already tracked somehow. The instrumentation stability, to a certain extent, is happening.
And then, if these issues are created for each SIG that owns it. Most of those things are owned.
And GC liaisons and CC, sponsors would… come to their SIGs and ask for it.
And it would be awesome.
**Reiley** 25:34 Okay, so I… I feel we probably need some more review here, and I don't think, like, at this stage, NATC is giving approval.
So, I'll just keep this in the inbox, just to, like, have our attention here.
**Liudmila Molkova** 25:51 I would expect the people who are the leads for every of the related Effort.
To comment and support it.
It's a bit enormous task, but that's what Ted, I think, was going to do.
**Tigran Najaryan** 26:07 I agree with that, yes. I would like everybody who is listed as in the scope of the project, they explicitly come and say, okay, I commit to doing this. I like that.
**Reiley** 26:41 Sounds fair?
And I'll leave this in the TC inbox, because I expect this will be updated, and… We… we need more review.
Sorry, is GitHub down or something?
Anyways, I'll… I'll come back.
Okay, so I… I think that's… Okay, sorry.
I think that's all of it.
Let's look at the, assignment.
OpenSpec PRs.
Okay, all types we don't assign.
Draft without a sign, okay.
Let's move to the topics.
Duck.
**Jack Berg** 27:36 So… just before Josh left the TC, he successfully merged this PR to the proto-repository to decouple proto-maintainership from TC maintainers, from the TC group.
We've talked about this for years, but, you know, about having a dedicated spec maintainers group.
Given the support of having a dedicated proto-maintainers group, and how smoothly that seems to have gone, do we want to follow the lead and do something similar with the specification?
**Tigran Najaryan** 28:14 Jack, what are the permissions that spec sponsors have today?
Approval rights? They have approval rights? Okay. So, presumably, then, they would become maintainers, or maybe some of them would become maintainers, in addition to TC members? That's what will happen?
**Jack Berg** 28:30 I think they're the obvious candidate pool for maintainers, and just like Proto, with the proto, change. There were some TC members that wanted to continue to be maintainers of Protos, and others like myself, who said, hey, I'm okay just being an approver. And some that, I think at least one stepped away from Proto altogether without context, but my memory might be failing.
So I'd expect a similar thing to happen with the specification.
**Tigran Najaryan** 28:58 similar, meaning that also some TC members would not be maintainers of the spec anymore? Or that's…
**Jack Berg** 29:06 I would leave that up to each TC member, a decision that they can make. But, you know, yeah, like, if all want to be maintainers, great. If some feel that they don't want to be for any reason, then I would feel comfortable with them stepping back.
**Tigran Najaryan** 29:23 I'm not quite sure about that, I… I'm… totally fine if not all TC members want to be product maintainers, that's completely fine, because it's a fairly niche.
Type of work that needs to happen.
spec, though, I'm not so sure about that, right?
If you… if you… If you don't want to be a maintainer, essentially you're signaling that you're not going to be that much involved anymore in the spec. You're not following it daily. I don't know if that's the right signal to send as a TC.
**Jack Berg** 29:59 It might not be, right? It's definitely a change in scope for the TC. The TC's work today, I would say, is sort of, like, the gravitational well of it is the spec. It all sort of gravitates around the spec.
if we create a dedicated spec maintainers group, and we kind of go in this direction, where not all TC members have to be spec maintainers, then that sort of allows TC responsibilities to fund new centers of gravity, like, maybe somebody can be on the TC, and they can really, really focus on the collector, and that's, like, their main responsibility as the TC. Or they can really, really focus on profiling, or these other parts of OpenTelemetry that are important, but don't have lots of representation in the spec.
**Tigran Najaryan** 30:53 Yeah, that's essentially what it is today, right? It's spec plus leadership of some project or of some SEC. That's what, essentially, the entirety of the responsibilities, mostly, I guess.
So you're saying we're okay with removing a big chunk of it, which is the maintainership.
And, and saying that, as a TC member.
it's okay if you're just a leader in some other project or some other SIG.
you… it's okay, you're still a TC member, because it's a significant shift in my mind, of what we think Statistics should be responsible for.
**Reiley** 31:33 I'll.
**Jack Berg** 31:35 Go ahead, Riley.
**Reiley** 31:37 I'll give one example. I think originally, a lot of protocols and semantic conventions are mixed in the spec, and then we have the TCS maintainers. Then we decided one repo is just too… too, like, crowded, so we… we divided and conquer, so we moved semantic convention. Then, if you think, like, if it made up being a maintainer of the semantic convention repository, and… and even now, like, people are thinking about maybe, like, divide that repository into smaller… set up repositories, right? So if the meta is doing all the work there, then I don't think we… we want to force her to also be a maintainer of the spec repo. I mean, if she wants to, fine, but if she's just doing great maintainer job.
for the semantic convention recall, I would consider that as good as the rest of the protocol and spec.
So spec repo doesn't seem to be that unique to me.
**Jack Berg** 32:33 Other examples include OpAmp. You know, I consider that a sort of extension of the spec. The specification for OpAmp lives in a different repo, but it is, like, spec-like material. Proto, the OTLP spec, lives apart as well, so those are other examples.
But there are two directions you could kind of go with this, and so with… you can create a dedicated spec maintainers group, which is TC, plus other members, so, you know, TC still is obligated to be a spec maintainer, and then the other direction is, you know, it is just completely independent from the TC. And, if there are TC members that are maintainers of the spec, it's, It's coincidence, it's… they're just independent things.
**Tigran Najaryan** 33:31 Yeah, I'm totally fine with bringing more maintainers, I think that's great. We should try to do that as much as possible. Saying that PC members don't have to be spec maintainers. I don't feel quite comfortable with that. I think it dilutes a bit the responsibilities and expectations we have from TC members. And spec… the specification repository, it's unlike most other parts of OpenTelemetry, to be honest.
it impacts… virtually all language implementations, and that's a very, very big chunk of OpenTelemetry. If you remove Let's say collector, which is another big piece.
Almost everything is impacted by the spec, otherwise.
So I don't know, if you want to do that change, maybe let's have that as a separate discussion.
independently from the fact that we want to have a different group for… just for maintainers, which I'm totally fine with. I just suggest that we make the TC members.
part of that group for now, and let's have the discussion separately, whether we're okay with saying TC members don't have to be spec maintainers.
**Reiley** 34:48 Yeah, so how about we do this? Like, I think the first step would be, let's just go and introduce these maintainers and approvers, and move to that model, and the maintainers should just be the TC at the starting point. And then the next step is for us to identify who should also become the maintainers, besides the TC. And unless we have any TC members saying, oh, I want to step back, then we don't need to even have the discussion about, like, do we want, like, do we want to allow TC members to be not, like, not as a maintainer, right? So… so I want us to be maybe, like, lazy here.
If nobody asks, like, nobody asks from the TC that they want to step down from containers, we don't even want to drive that discussion.
**Tigran Najaryan** 35:34 Yeah, that… I think that's a… that's definitely a separate discussion that needs to happen. So many things that we do revolve around the specification of repo that look at the… how do we do the triaging? We have a spec inbox. We have spec PRs that we need to take a look at. All of that somehow has to change now, because in this hole, supposedly you're going to have half the people who don't know what the spec is about.
anymore, right?
**Bogdan Drutu** 36:03 Yeah, that's what I was about to say, like, do you invite the maintainers to this meeting? Because half of this meeting is about the spec repo.
**Jack Berg** 36:11 It is a substantial change, and I do think it's, it's… it's possible to do this sequentially, like Riley and Tigrin have articulated. If the spec maintainership became something that was independent of the TC, the natural place to do spec triage work would be on the spec call.
**Tigran Najaryan** 36:37 Yo.
Maybe, right? I'm open to discussing it. I think that discussion needs to happen. I don't think we can… we don't have to couple those two decisions into one, right? Let's decide to have maintainers as a group.
And we can decide whether TC members have to be or don't have to be maintainers.
**Bogdan Drutu** 36:59 But did we agree that we have Outside members?
**Tigran Najaryan** 37:04 I'm fine with that. There's, like, I can think of a person who has been very active in a spec, who is not a TC member. I would I'd like to have him as a maintainer if he wants to be.
Robert is a good example.
**Jack Berg** 37:19 Yeah, the question is, are there…
**Tigran Najaryan** 37:20 of work there.
**Jack Berg** 37:21 Exactly, and I think he has displayed, you know, really good judgment, and I trust him merging PRs as much as I trust myself, so… That's what you get as a maintainer of the spec, is the permission to merge the PRs.
**Reiley** 37:35 Yep.
Good a minute.
**Liudmila Molkova** 37:38 I was going to say that, This is the way we scale the project, is it… the… project is much more… much bigger than spec now.
And maybe we should talk less about the spec-only year-end of the project proposals we gather across.
across SIGs. That's probably why it's so hard to make a new project in Hotel.
And having dedicated maintainers would help us scale.
**Reiley** 38:09 Okay, so do folks think this approach would work? If yes, then let's don't wait, let's make progress, and we don't need to talk about whether it's a TC obligation unless someone wants to step back.
We assume nothing will change there, for now.
**Jack Berg** 38:27 That makes sense. I can take the action item to sort of kick this off, and the one thing that I… I'll ask, before we sort of put a bow on this and move on, I see hands up, I don't want to stop the conversation if there's more comments, but, like, is in the initial step, I would propose that we say, hey, we're creating a dedicated maintainers group and a dedicated approvers group with the intent of expanding maintainers beyond the TC, but also obligating TC members to be there. So, it's not just, like.
a no-op refactor to create maintainers and approvers. We're saying we're creating maintainers, and the intent is to have a superset of the TC members as maintainers, even if we don't add any immediately. But we make that clear to the community.
**Reiley** 39:16 Yep.
**Bogdan Drutu** 39:20 For me, for me, I wanna make sure, before you add others.
And again, I'm supporting 12 others.
Let's make sure we change our process around what we do with the spec, so that these people are involved.
Like, let's make sure we move our triage of spec PRs or anything to the spec meeting, and things like that. Does it make sense to you? Like, I want to make sure we give them all the visibility into what they need to do, and what They have to do, and then let them decide that this is what they have to.
**Jack Berg** 39:59 I think that makes sense. Quick proposal on that.
Since we already have triage as part of this call, and since the spec call has been getting sort of crowded lately, we've had to start doing some curation of topics, because it's, like, it's regularly exceeding the, the hour. What if we invited any new maintainers just to the first 15 minutes of this call.
To see how that works, because we have the first 15 minutes of this call dedicated to triage, and, like, you know, just continue doing that and see if it works.
**Tigran Najaryan** 40:33 Yeah, something like that. I really wouldn't want to have another weekly call or anything like that.
I like it.
And, presumably, we have two candidates, I don't know if we want to discuss them now or elsewhere, but… We already said the names, Josh.
**Carlos Alberto Cortez** 40:53 I wouldn't.
**Tigran Najaryan** 40:54 Being the obvious one? Yeah.
**Carlos Alberto Cortez** 40:56 Yeah, I would like to disclose that in private, but yeah, I think that the obvious choice is Josh, for sure, because he already was, or is a maintainer, you know?
**Tigran Najaryan** 41:05 Okay, let's have that discussion, maybe, in the blockchain.
**Jack Berg** 41:12 Well, thanks for the conversation. I'll take the action item to follow up with this.
**Tigran Najaryan** 41:27 Okay.
Shall we move forward?
**Reiley** 41:30 Yeah.
**Liudmila Molkova** 41:32 Yeah, I have a heads up. So, there is a donation proposal from Arise for their set of instrumentation libraries for GenAI.
Called up an inference. It's something we've been discussing with them, and they are donating the code But not contributing the manpower.
But GenAI Sig seems to be fine with this. We would like to take their instrumentations, refactor them into what we already have.
And, own it.
This really helps us fight the fragmentation there is in the GenAI world around instrumentations and semantic conventions, and that's something we initiated effectively.
R… the GC reached out to CNCF, They are, CNCF gave some guidance on how to approach it.
And, GC, I don't see the explicit mention that they approved, but I believe they are either approved or are discussing it, And… So the next step is that, Arise folks will send the donation proposal. I will write the due diligence, but I'm just sharing that my intention is to accept it. I've been reading this quote quite a bit, and it will really help us.
**Tigran Najaryan** 43:03 So are you doing a due diligence in the end? Yeah. You decided to do it? Yeah. Okay, so we're not bypassing that.
**Liudmila Molkova** 43:10 No, we're not bypassing that. I will prepare the document by the next call.
**Tigran Najaryan** 43:15 Okay, sounds good. That was my concern there, but we're good.
**Carlos Alberto Cortez** 43:21 So, I haven't reviewed the proposal, I will do that, but a question that I have is that you said that they are not providing the manpower?
So, this would be effectively a fork, or is that something… I don't know how that will work.
**Liudmila Molkova** 43:35 It is effectively a fork.
So, the… They are not ready to give up their own set of instrumentations, because the AI is moving so fast, and they want enough control.
But we are going to have some regular syncs with them, and hopefully in… some amount of time, like 6 months, we can demonstrate that We can actually maintain quite a lot of our instrumentation as well. We have a lot of experience doing this, and we can probably move fast, and maybe we'll figure out the hook-in mechanism, allowing them to have some extensibility and control.
Over their version, maybe they will develop wrappers, but at this point, we, they are not ready to use us as the core component.
**Tigran Najaryan** 44:31 No, I'm not sure I understand that. I think Trust said they will be doing it as a donation. The purpose of that, so that from legal perspective.
they transfer the copyright to OpenTelemetry. That's what the donation means.
So it's not a fork in that case. Am I misunderstanding something here? But if they can't both donate and keep it.
The copyright doesn't work that way. You can't have two people having copyright of one thing.
So either they give it to us, or they don't give it to us.
Some… somebody has to be the owner after that.
That's my understanding.
**Bogdan Drutu** 45:09 And the same applies for IP, not only copyright.
**Tigran Najaryan** 45:13 Yeah, yeah, so… If they donate, they obviously can fork OpenTelemetry and do whatever they want with it.
But it becomes the property of OpenTelemetry after the donation.
Or if they don't do that, we do the opposite. We fork and do whatever we want with the fork.
So I think we would meet… I just want to be in some sort of… Legal misunderstanding of what is happening there.
**Liudmila Molkova** 45:39 Okay, I'll check. I don't have an answer to your question right now.
**Tigran Najaryan** 45:42 Yeah.
Thank you. Okay.
**Liudmila Molkova** 45:47 But then you're asking how to ensure we don't diverge. We will diverge.
Like, that's the point, we will take what they give, and we will diverge it right away.
We are not taking their codices.
**Bogdan Drutu** 46:01 So we will not do a constant resync and re… yeah, resync, it's the right time. Okay.
**Tigran Najaryan** 46:10 And we could… I mean, why aren't we simply forking? Like, it's… it's easier. The only thing that changes, we just add a notice file, which has This is the origin of this source code, and that's it, right? There isn't much else to do there. It's Apache licensed, from what I remember.
**Liudmila Molkova** 46:28 And there was a, a lot of pressure from the GC to do it the right way through the nation.
Why so? I don't have all the context. But they, they mentioned that having the copyright given to us is important for CNCF.
**Bogdan Drutu** 46:45 Yeah, and the IP, Tigran. If they… if we fork it, the IP belongs to them.
And there are some… some limitations of that. I know a long time ago, there was a long discussion with the Microsoft lawyers and Google lawyers about IP and who owns the IP, even though it's Apache, even if it's everything. There was some discussion about that. I'm not an expert into that, but I know they were very picky on who owns the IP, and that's why they want CNCF non-profit, to own the IP. They can… whatever. I'm not an expert.
but I know it's… it's also not only the copyright, it's also the IP part of the… Ding.
**Tigran Najaryan** 47:22 Okay.
Okay, I think we forked something else in the past from Datadog, PHP, Python, something like that, so we have done this in the past.
**Reiley** 47:35 Yeah.
Just, like, like, in my opinion, like, fork and donations, they're mutually exclusive.
**Tigran Najaryan** 47:43 Yeah, exactly. I think from legal perspective, exactly as you said. You either do one or the other, you can't, like, you can't do both.
But the reason is because only one person or one entity, one legal entity, can be the owner of intellectual property. Or it can be shared, whatever, right? But you cannot both own 100% of intellectual property. There's no way to do that.
Not a lawyer, that's just my understanding.
**Reiley** 48:17 Let me wait for due diligence from Lionmeil. Sorry, sorry, go ahead.
**Liudmila Molkova** 48:21 I'll start the thread and GCTC channel so we all can see, what are the details.
**Bogdan Drutu** 48:27 Yeah, shouldn't we?
**Liudmila Molkova** 48:27 Horrified.
**Bogdan Drutu** 48:29 Sorry, Lumina, should you push this on GC to figure out, with lawyers and everything?
**Liudmila Molkova** 48:33 Yeah, absolutely, yeah.
I'll just start a thread.
**Reiley** 48:40 Okay, anything else to add here?
Anything else you want to discuss?
Okay, then we can finish early and give 12 minutes back to everyone.
**Tigran Najaryan** 49:00 Alright.
Thank you, all.
**Liudmila Molkova** 49:02 Thank you.
**Jack Berg** 49:03 Take care, bye.
