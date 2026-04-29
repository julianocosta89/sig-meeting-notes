SIG: LLM Semantic Convention WG
Date: 2026-04-28
Duration: 62 minutes
============================================================

## Zoom Recording Transcript

Trask Stalnaker 00:03:32 Hey, folks.
Wolfgang Therrien 00:03:35 Hello?
shuwpan 00:03:39 Oh.
Trask Stalnaker 00:03:41 I figured Ludnula was just on her way from the SPEC meeting, which just barely ended.
Liudmila Molkova 00:03:51 Hello!
Trask Stalnaker 00:03:53 Hey, hey.
Liudmila Molkova 00:03:55 I'm wondering if anybody wants to drive this call?
Surya Teja 00:04:00 I can happily drive this call, Lutmila, but…
Liudmila Molkova 00:04:05 fridge.
Trask Stalnaker 00:04:06 Yeah.
Surya Teja 00:04:07 Yeah.
Great.
Liudmila Molkova 00:04:14 I'll start preparing the… Document.
While we are getting ready.
Surya Teja 00:04:24 Okay, everyone can… you guys see my screen?
Trask Stalnaker 00:04:29 Yes.
Surya Teja 00:04:31 Correct.
So… We have, quite a bunch of topics that we want to discuss.
There's a… You already have a populated agenda.
Hmm… would open the… Project Board, and see if… There is any outstanding… Things that we want to discuss.
Yep.
Lyudmila, as you were here last week, we skipped discussing this because, you were not here, but guys, feel… free to let me know which ticket should I pick up so that you can discuss those.
Liudmila Molkova 00:05:19 I think we… I like the idea that Trask brought up, that we should talk about PRs more than issues.
Then it helps us make progress and not get stuck onto the discussions for new things every time. I don't think we have any view here, or we can filter by ESPR in this board.
I don't know, though, if we… did a great job, I didn't, Okay, so if somebody added PRs to the dashboard, that's awesome.
Surya Teja 00:05:54 Yeah.
So, we have memory operations, Google Gen AI systems, workflow duration metric, and… Gen AI agent planning operation.
Is anyone related to this?
B.S.
In the call.
Trask Stalnaker 00:06:17 the memory operations PR, as… is pretty close now. Ludmila and I have both approved it. Ludmila has a few, follow-up comments that need to be addressed still. But if anybody is interested in this topic, please look at the PR, because, probably once, the Ludmila's last comments are resolved, we will be merging it.
So speak up now if you've got thoughts about memory operations. Please.
Yes, Jamie, until the next release.
Surya Teja 00:07:14 So, can I conclude that… Since everyone is silent, everyone is okay with this, and they are planning to… leave comments on the PR, and take it from there.
Trask Stalnaker 00:07:30 Yeah, I think it's kind of too big to try to recap Here, and discuss here, unless anybody has specific… has looked at it and has specific questions.
Surya Teja 00:07:44 Yeah.
Liudmila Molkova 00:07:48 Yeah, we usually treat silence as agreement, unless there's the silence… there is too much silence, and it's too… it sounds controversial. You never know.
Surya Teja 00:07:59 I have one shameless plug for this planning operation. I have been reviewing this PR, and I have been doing a little bit of reading around the agent operations that are happening.
I believe it has got some scope in it, and it might add some value if we have plans around the… not just planning, but around orchestration and stuff, so this is, to Trask and, Ludmila. So if you guys can take a look at this and add your comments around it, it will be helpful in driving, discussion around how we can, instrument agent orchestration.
If we have Spencer on it, and I'm missing something, don't mind me.
Liudmila Molkova 00:08:51 I think it needs some of the Trask magic with sculpturability study, because I…
Surya Teja 00:08:56 -Oh.
Liudmila Molkova 00:08:58 It's unclear how and what it exactly means for instrumentations and… When it would take to implement it.
Surya Teja 00:09:07 Yeah, makes sense, makes sense. Yeah. In that case, I can work on entering task on the side and add my thoughts around it so that I can get this moving.
Trask Stalnaker 00:09:20 Yeah, and I'll… I'll cover that in, with the update on the SEMConf GenAI repo breakout, and that kind of more formally defines the reference implementation work as part of the PRs.
So, yeah, and I think we are… we're very close to switching over there, at which point, you know, we'll need to take the in-flight PRs and, resubmit them to the new repo.
Surya Teja 00:09:52 Yeah, that's awesome.
So, I guess we can switch back and… Go to our agenda and, start there.
So, guys, I'm going back here.
Yeah.
Hmm… Anyone who is new to this meeting, feel free to, introduce yourself.
You have 5 minutes.
Billy Zhou 00:10:27 I think I'm the only one. Hey guys, I'm Billy, from AWS, I'm just here observing today, just, like, on board to, this whole new stack, so, you know, just, just wanted to say hi. Thank you everyone for your contributions. Thanks, super cool project.
Surya Teja 00:10:46 Hey, Billy, welcome to the SIG. I hope you're part of our Slack channel, so any questions, please feel free to… Ping over there.
Billy Zhou 00:10:55 Thank you.
Surya Teja 00:10:57 Yeah.
Anyone else?
Going once, going twice.
going thrice. So, yeah, the first one on our agenda is a SIG roadmap.
Jamie? Litmila, do you want me to… Start with this one.
Liudmila Molkova 00:11:21 I've edited it because it was in the next topic, and I wasn't sure what we should discuss there. I think we are acting on some of the items identified, and I didn't think we've got a lot of… oh, there were some comments.
So, Jamie, maybe you, you wanted to drive something, let me know.
Jamie Danielson 00:11:41 Let's see, I know we talked about it a little bit last week.
But wanted to wait for you to be back, also, to, kind of go through it. Last week, really, we just talked about, like, what were maybe our next action items of things that we wanted to do, and seeing if anyone hadn't seen it yet, if there was, you know, major objections to sort of the things that are on there.
Like, last week, we talked about wanting to have two new repos and having those get started, and… I think… Let's see, I'm trying to recall if there was anything specific to call out other than just, do we know what sort of next steps are, and is, you know, do we have alignment on what we want to work on, and where we can have people get involved?
Liudmila Molkova 00:12:34 Yeah, so I think the immediate next step that Trask is working on is the new report.
not just trust, but other people too, that we want new reports for semantic conventions.
And you folks talked about it last time. Do we need to add it to the agenda? Do we need to talk about it here? Are people aware? What's going on?
Trask Stalnaker 00:12:59 I'm covering… I have that in my bullet.
Liudmila Molkova 00:13:02 Oh, nice.
Trask Stalnaker 00:13:02 the agenda.
Liudmila Molkova 00:13:03 Oh, awesome. Sorry, I missed it.
The other part is the new Python repo and the scope there. I didn't have a chance to prepare any write-up, but this is my main focus for this week, so, we will have something more tangible by next time.
Jamie Danielson 00:13:26 Okay, I'm just putting notes in the doc then, like, so, like, your next thing is you're working on the Python repo setup, Trask is already gonna talk to us a little bit about the GenAI repo.
I have a task that I forgot to do, which is, working on the PR guidelines that we want to have, for the repos. So I set myself a reminder for that, as well, unless it's already something that Trask put in there, which is very possible.
Trask Stalnaker 00:13:53 some stuff in there. Perfect. Yeah, we'll talk about that, yeah.
Jamie Danielson 00:13:57 Okay.
Liudmila Molkova 00:13:58 Oh, we've also added something in patent contract, for the co-pilot reviews. I'll paste some links.
Cool, so it seems we are acting on some of the parts in the roadmap.
We'll be done with roadmap before we mark it on draft.
Not the drafters.
Surya Teja 00:14:46 So…
Liudmila Molkova 00:14:46 Did we move on?
Surya Teja 00:14:47 I'm… Should we move on? And that's my second question, yeah.
Ludmila, the next two topics are from you, so please feel free to take the screen share and drive the meeting.
Liudmila Molkova 00:15:07 Yeah, so probably none, no need to share for the next topics. There is a blog from James Newton-King from Microsoft who works on, some parts of .NET and Aspire Dashboard about, Well, if I can summarize, it's about VS Code and GitHub Copilot supporting hotel semantic conventions and the meeting telemetry, and how Aspire Dashboard shows it all.
It's not very specific to any of these technologies, well, like, specific enough. So, I… I don't have a problem with it, because I think this is all open source, and it's not a pitch, but if people want to take a look at it, who are not don't have any affiliation, I still have affiliation in my heart with Microsoft, so if you folks want to take a look at this, was, more objectivized and, like.
steer it into the, whatever direction you want, please, review.
The iron part is that the really stuff, Things that are probably native instrumentations, in this blog.
And… If you folks know about some native instrumentation, That's, not related to Microsoft World.
Would you mind dropping a comment on this PR, and to include it?
I think what I mentioned there is there is MCP, There are MCP for Python and .NET instrumentation, and there were… it's for the libraries. There is a Gemini, Gemini CLI that reports up in telemetry.
And if you can think about other things that you may not tell in some way or another.
It would be awesome to mention.
Yeah, Ankit?
anksing 00:17:02 Yeah, I was trying, like, GitHub Copilot to emit these, like, the enigmatic function, and I came across when you use GitHub Copilot with VS Code.
The extension, there's a way you can enable that.
Liudmila Molkova 00:17:16 That's what the blog is about, yeah.
anksing 00:17:17 Oh, got it.
Liudmila Molkova 00:17:19 Well, it, it, it's… Mentions it was one of the things.
anksing 00:17:22 Yeah, that was pretty neat. I liked it. And, I hope, or probably I can add some comments about, like, if you can have that available in the GitHub Copilot CLI as well, which right now does not emit the same telemetry, or there's no way to… So, ugliness.
Liudmila Molkova 00:17:39 You can probably ping James on Teams and ask him if he can…
anksing 00:17:44 Interesting.
Liudmila Molkova 00:17:45 it in some ways.
anksing 00:17:46 Yeah, yeah, yeah. I think there is some work going on that I got to know, but, it's still, like, still work in progress from this.
Liudmila Molkova 00:17:56 Awesome.
Okay, so I don't think there is much to add on this topic. The other…
Jamie Danielson 00:18:04 I do have one quick question, actually, I just thought of reading it. So one of the things on there is, you know, if you have issues, or you want to report issues to put it on Symantec Convention's repo, I'm curious if… we want to update that to whatever the new GenAI SimConf repo is once it's created, so we don't have to go back and change it.
Trask Stalnaker 00:18:27 Good point. Let's see when the GenAI repo actually lands, and then, depending on timing, or if it's been posted, we can go back and update it afterwards.
Liudmila Molkova 00:18:44 Nice, thank you.
Trask Stalnaker 00:18:46 I don't want to hold it up, because while I think that I'm… while I'm ready to hit the button today, Things happen.
Liudmila Molkova 00:19:01 Cool.
Okay, so then, another small announcement. There is, turns out, there is an end user, SIG, that runs WhatsApp or TAO, like a podcast, And they invite… I tell SIGS to share what's going on.
It would be cool if… Some of us decided to go and just share.
It also helps with all the current efforts where driving and some… Add fur for… Like, shameless plug for, standardization efforts we are driving.
Would anybody… Be interested.
I can go, but I don't want to, I'd rather not.
Jamie Danielson 00:19:51 Is it tomorrow?
Liudmila Molkova 00:19:54 It's just you sign up on the… form, and it can happen whenever we… I feel like it. So I think there's April, May, June, July, and so on.
Jamie Danielson 00:20:06 Is it just…
Surya Teja 00:20:08 Sorry.
Jamie Danielson 00:20:11 I think I was talking to myself, and I thought it was muted.
Surya Teja 00:20:17 Is it a place to showcase what we're trying to do and, Bring it to a much broader community, or what should we be doing over there in the livestream?
Liudmila Molkova 00:20:31 It's more of, okay, what's going on?
It's for people with little to no context about Intelligent AI seek to learn about what we do. That's my interpretation, but it can be anything.
That's… We wanted to be.
My goal is to, like, showcase, okay, we exist, and we do awesome things, and you can work with us, and here's what we do.
And here's where we're going.
Surya Teja 00:21:03 Yeah, that's cool, actually.
Jamie Danielson 00:21:05 How many people, I guess, would do it?
this is just, like, open-ended? I haven't seen any of them before, maybe that's a good first step, is seeing what the other ones look like, but I might be interested in helping.
Liudmila Molkova 00:21:18 I would imagine one or two, Yeah, there are some pre-existing work streams, sorry, streams on YouTube.
Okay. And it's, like, 100 people watching it, so it's not intimidating at all.
Cool, so then, think about it. If you're interested, if you want, support, I can support you, and I can go with you if you're scared to go alone, but if you want Jamie, go for it.
Jamie Danielson 00:21:53 I don't want to take it from anyone else if someone else really wants to, but otherwise, yeah, I'm happy to put our names out there.
Liudmila Molkova 00:22:01 Okay, I'll post them Slack, so, and people can coordinate there. But I think, Jamie, you should… Oh!
So, I think that we're done with this, and the… Next topic is from Trusk.
Surya Teja 00:22:24 Yeah. Tas, do you want to grab the screen share?
Trask Stalnaker 00:22:27 I will, yeah, thank you.
I think you have to unshare first, yeah, alright.
Cool. So, yeah, I think that with the repo is… ready in my view.
I've discussed it in the semantic convention meeting yesterday, and a good point was brought up to… that we should also update to Weaver Schema V2 at the same time.
Which is, pretty… straightforward. There are a lot of… if you look at this PR there's a lot of diffs to MD files, but they're all just this mechanical diff, so… If you want to validate, these are… this is how to see, basically, if you strip out these renames, then you'll see there are no diffs to the MD files, which is good.
The Weaver file… the YAML files themselves… have changed, and this, I'm looking forward to Ludmila, having a look later, just that this all looks normal. My… I assume it's all good, given that it regenerates the exact same Markdown files.
But maybe there's some new features in the V2 that I'm not aware of.
And… Let's see, so… yeah, so I did include, So, some of the stuff we talked about in the PR template.
This is sort of the motivation section, So, you know, there's kind of two things that we struggle with, on reviews for the GenAI SimConv. One is, the… Reference instrumentation, and scenarios, sort of, like, is this… does this map well to existing libraries?
And… The other is… how will this be used?
And so, this motivation section kind of covers how will this be used, what's the… what user journey does it support?
What's the prior art for this?
And the prototype… I guess this is maybe not technically under motivation, but the… the reference scenarios, are the ideal prototype, but sometimes that's not possible, and that's okay, to include a alternate prototype.
Yeah, Aaron.
Aaron Abbott 00:25:54 Sorry, it wasn't on this, it was a question about the V2 schema.
Yeah.
Yeah, I was wondering, does this… does… is there any, like, difference besides just renaming stuff and whatnot? And the reason I'm asking is because we have these JSON schemas, which are kind of, like, not integrated with Weaver, they're just kind of living on the side.
Liudmila Molkova 00:26:17 Yeah, I didn't have a chance to look. Actually, I opened the PR task, and GitHub showed me as closed, with no changes. I don't know, maybe it was some fluid.
subside.
Trask Stalnaker 00:26:26 No, it was because I had force-pushed to main, so here's the new one. I reop… I reopened it.
Liudmila Molkova 00:26:35 Cool. Yeah, so from video perspective, it's a slightly different structural change. You can't think about it from definition perspective, just as you rename some things.
For the JSON schemas, nothing changes.
But we should talk about it, because I think we should incorporate JSON schemas into the… Schema, the semantic convention schema.
I don't want to do it right now, because we are moving, actively moving cover to V2, and I don't want to add anything to V1.
We can already… validate these attributes against schema.
With, a little bit of, custom stuff.
Because we can hard code that for this attribute, we expect this JSON schema.
And the validation can already… Work was just a little bit of duct tape.
Aaron Abbott 00:27:37 Okay, cool, sounds good.
Sorry to interrupt.
Trask Stalnaker 00:27:40 No, no, that's great.
Sue, in the… for the reference instrumentation, and I think I… showed this last week, but each of the… so the reference instrumentation is part of the SEMCOM repo.
So that the PRs can include the reference instrumentation, example at the same time, and we can use that as part of the PR criteria.
And so there's kind of a baseline of a lot of different, GenAI libraries already.
And so… you would just come in here, and if you're adding another attribute to the proposal, to the SEMCOMF, you would add that here, and we could then, you know, see clearly that, for example, request model.
We're capturing it here. Okay, yes, it really does feed into the, the library API, so it is something that's capturable.
And then as, overview, sort of, with, Say, with invoke agent internal spans, like, when you're adding a new attribute, ideally, all of these attributes would have some coverage.
And if we see ones that don't have coverage, I mean, there can be good reasons, but it can also be something that, you know, maybe we were a little too early and libraries haven't, Aren't really supporting this yet.
Definitely would appreciate, all the, domain experts in this, SIG, you know, looking over these, and, you know, some things might jump out to you as, like, oh, that Should be capturable in such and such library.
And, you know, it'd be great to, you know, PR that, to add it, or open an issue just to document it, That would be super helpful.
And… Yeah, so, you know, we're really hoping to be able to use in this repo, speed up the PR process in getting things approved and merged.
And one of, the aspects of that is… you know, we need approvers, you know, are the critic… the key component there, and so… I tried to write up some, like, guidelines on how, you know, how we can… what expectations that we could have from approvers, how approvers can help to make this successful, because we really do rely on this… the domain experts in this SIG to, validate and, you know, drive these conventions.
So… The… my initial thought here is, and, you know, really looking for feedback from folks here, is that for non-editorial PRs, approvers would assign themselves to them, to… basically indicate that they will drive the review for that PR.
it's fine to have for multiple people to sign up.
to review, to drive that PR, especially on, you know, medium and high complexity PRs. Basically, I… you know, there could be an unbounded number of… the more reviewers of those, the more active reviewers of those, the better.
And to, you know, really… one of the problems that we've… seen in the past, one of the issues we've seen in the past is sometimes, and we have this currently with the current GenAI approver's team, is that people will be around for a while, and then, you know, they get pulled into other projects, and so they're not around, and so We really want to have a clear, you know, what is… how would we bring people on, and how would we bring people off of that team to make sure it's, you know, staffed appropriately, or that people are, doing… following that… following that. And so… Kind of, I just put a stab in the dark here over, 3 months, Approvers would be expected to sign up and drive, you know, at least 3 of these PRs. So, you know, kind of approximately one PR a month.
Driving the review means, you know, being very active through its… until it's either merged or closed.
You know, following up when people, when authors, you know, add, respond to feedback, following up quickly, because, we see that's one of the reasons why PRs lag a lot, is that we, as maintainers or approvers.
let a lot of time elapse there before we get back to PRs.
And, I'm gonna work on, sort of, some… see what… I know one of the problems is we're all suffering from GitHub notification failure, overload, and so it's often hard to, like, we just genuinely miss stuff.
And so, I'm trying to think of how ways to be able to, you know, really… help people, help approvers with that. One thought is… Like, if we had approvers Slack.
aliases. We could have a bot that, you know, when… authors reply to stuff that, you know, we ping you on Slack, So, you know, ideas like that, to really, you know, really want to focus this repo on how do we… how do we move it, efficiently.
And… We'll find out what works and doesn't work, and maybe we can be a, spread some of these practices to other hotel repos.
But this one is especially, like, I feel like we have a lot of people who are interested in this topic.
Which is an area where, Some other repos kind of suffer, so… I feel like… We can capitalize on that interest here.
And do something really good.
Liudmila Molkova 00:35:18 I've already mentioned we are going to revisit the current GenAI approvers, some kind of GenAI approvers group. We… this group is mostly… Consists of people who went quiet over time.
I… thing among these existing people.
Aaron and I are the original approvers who are still around. I think some put people who are still active and up in telemetry, and they are Not quite interested in Gen AI work for now.
So, I think we will establish just a brand new approver group, and it will follow the existing Wattel process, plus we will, whatever the policies we have, we will try to polish them to make things faster. Plus, we will have this, 3 months window.
kind of enforcement.
For people to stay active. And just to have the clear list of who actually cares about it.
Aaron Abbott 00:36:39 So, one, one question.
I mean, that all sounds great to me, I think.
That's good. I'm definitely guilty of the GitHub, notification.
All works. Very guilty. But anyway.
Trask Stalnaker 00:36:51 Failure, yeah, yeah.
Aaron Abbott 00:36:53 Yeah, failure.
Trask Stalnaker 00:36:54 So say we all.
Liudmila Molkova 00:36:56 Yes.
Aaron Abbott 00:36:58 Yeah, so I was gonna ask, do we want to do the two-company policy for, like, semantic convention VRs? I know I know a lot of repos, like, you know, they start with that, or they say it, and then sometimes… Things are a little different in practice, just given, You know, how hard it is to get reviews.
Trask Stalnaker 00:37:21 Yeah, so… What I… put in the repo here as kind of a proposal is, just for editorial-only changes, I'd like it to just be one approval in this repo.
Where, like, in spec and SEMCon today, we have the two approval set in GitHub, and so… That requires two approvals there.
But for non-editorial changes, Definitely.
to approvals. Is this what you mean, Erin? And should I just add from different companies here?
Just…
Aaron Abbott 00:38:10 You tell me, I mean, I was just… raising the question, I… that makes sense to me, and I think two companies is reasonable, unless it's something like You know, some complicated thing that only applies to one company.
Trask Stalnaker 00:38:25 Which is new and normal.
Jamie Danielson 00:38:26 Even then, that's even more reason to have two companies approve it, I would think, right? If it was, like… like, if I came in and said, this is very specific to Honeycomb and is only good for that, that would be more reason, I think, for someone to come in and challenge it.
Aaron Abbott 00:38:40 Yeah. I meant more, like, specific to an AI vendor, so, like, For example, like, for example, like, we have a bunch of OpenAI or Bedrock-specific attributes right now. But yeah, I hear you.
Liudmila Molkova 00:38:55 I think we are… We can have different ways to enforce it.
Right? So, the people on the Proverse and maintainers list will be from different companies, for sure.
And veto power.
Stace.
what I think we have in this report that Gives us confidences this, reference instrumentations, and if we see that reference instrumentations are only applicable to one library.
Done.
It's a signal, we shouldn't merge it regardless of Approvals.
Oh, well, we should not.
We should merge it with the… with caveat that it only is specific to this.
Library or provider.
Jamie Danielson 00:39:51 Like, there's a lot that's generic across everything, right? And so, I guess the first look would be, if it is specific to one, is it a way that it could be made generic, or does it make sense to keep it specific?
That makes sense.
Aaron Abbott 00:40:05 Yeah, I think that's actually an interesting point, For, kind of, two reasons, because, like.
You know, one, maybe it would move faster to just start with it, not generic, and then we could, like, after we have, you know, the list of things, and we're like, hey, look at all this stuff that we could merge into one.
I think there's probably a small set of, like, just because there's existing stuff, for example, like, we… for the inference conventions, it was pretty obvious that we needed to just have, like, a single thing, and try not to have it diverge too much. But then the other question was, like, I think in SEMCONG, we have… the prefixes are now gcp. or, like, OpenAI.
And I'm not sure, would those live in this repo or the other repo, and do we reference them?
Liudmila Molkova 00:40:56 By default, they leave, if they are for GenAI, they live in this repo, unless that company, let's say OpenAI, wants to maintain their own set of conventions.
Then we'll probably happily reference them, maybe with caveat where they, contradict ours, if they do.
But, but, I think they should live here.
Well, the more… like, I think that having multiple companies requiring approval from multiple companies is a measure that prevents us from having, let's say, I don't know, Microsoft or Google coming and just owning the whole story on their own, right? And, yeah, we…
Trask Stalnaker 00:41:41 I don't see any problem with adding the, the two-company rule here.
Jamie Danielson 00:41:49 Oh, I guess the latest question that Aaron had just asked, though, so we have some attributes that were renamed from, like, genai.openai to just OpenAI.
So, I guess that's a question of whether… That would live… in the generic semantic conventions repo, or here, because it's no longer prefixed with the namespace of GenAI, even though the… area is… Gen AI.
Trask Stalnaker 00:42:22 I would hope that we could make it work for them to live in this repo.
I think be a little bit more complicated for something like GCP, Where there's a root namespace in the core repo.
I still feel like there's a sub-namespace. I don't think there's a problem with having a root namespace split across two… Registries?
Liudmila Molkova 00:42:55 Shouldn't be a problem at all.
Trask Stalnaker 00:42:59 And I might have missed that then. Are there some things under GCP… like, vertex or something, namespaces that I should pull in here.
Aaron Abbott 00:43:12 there were some open PRs, which I never really pushed through, but there's no… there's nothing today. There are probably some things that we would add.
But if the tooling supports it, then I think I would prefer it to live here. It's just kind of… Yeah, maybe we'll hit some friction with Weber. I guess we'll just have to try it out.
Liudmila Molkova 00:43:34 Well, if I shouldn't…
Aaron Abbott 00:43:36 Okay.
Okay, cool.
Liudmila Molkova 00:43:43 We would need to publish.
The schema URL for this one.
The moment we want to do a release from here, we will need to publish We will need to work with, our telecoms people to… Do this.
Oh, sorry, Siri, you have your hand raised, go ahead.
Surya Teja 00:44:06 Oh yeah, so I just want to add one thing, the common conventions are going to be easier for inference vendors, like OpenAI and Anthropic and others, but more specific instrumentation around agents is going to be difficult, because each one have their own philosophy while they're designing agents.
So, we should, I mean, I… calling this out earlier, because tomorrow it might become a little bit tougher, because people might create their own, OpenTelemetry standards for their agent frameworks, and it might become a little… Difficult tracking those.
Liudmila Molkova 00:44:51 I didn't… this is the… discoverability process. I think if we discover it.
We should probably have a page here, or up in Telemetry.io that tracks this.
conventions that are… that live somewhere else. Hopefully, they take dependency on these conventions.
Yeah. In the same way they could take dependency on the query port. It probably doesn't matter for them which one to take dependency on.
Surya Teja 00:45:19 Okay, yeah, that makes sense.
Liudmila Molkova 00:45:22 Yeah, it will be, like, essentially, it will be a problem. If people do a good job documenting conventions, like, defining their own convention somewhere else, it will be a problem that we will not know about this, and people will have a hard time to discover, but I think we can solve it.
Trask Stalnaker 00:45:43 Speaking of the schema URL, I think there's, an open question about the version number.
When we come over to this repo.
There's sort of two, thoughts we discussed in the SEMCOM meeting yesterday.
One is… To basically reset the version to 0.something.
As, hey, this is… It's… everything's in development.
Today, and we, you know, as we've discussed, one of the goals here is to mark a 1.0 fairly quickly, and then iterate from there.
The… Other option is to… go to… stay at, like, the SEMConf version is 1.41 now. We could stay in the 1.X and go kind of make that de facto stable, and then go to 2.x.
For our next… version. I think that's, Lyudmila, what you're… the alternative?
Liudmila Molkova 00:47:04 Yeah.
Trask Stalnaker 00:47:08 So, I don't think we have to… we just cut a 1.41 SEMCOM release yesterday, so I think we've got… A month here in this repo to decide on that.
So I think it's okay to go forward. I kind of, I guess, I kind of like resetting it to 0.something, just because that may… sense in my head of Semver, But there's also benefits to going to, kind of the confusion of… I mean, the downside there is the possible confusion of we're going from version 1.41 for GenAI stuff backwards.
To zero dot something.
Liudmila Molkova 00:48:09 What we do?
Just following up on another discussion we had in… Regarding this format, would we do schema slash gen AI?
dash deaf.
Trask Stalnaker 00:48:24 Oh, right, right.
Liudmila Molkova 00:48:28 Like, a good chat, a good way to test our… decisions.
Trask Stalnaker 00:48:36 Yeah.
Yes, yes, so the goal, and so the reason we want this dash dev here is… Really more because when we get to 1.0, We're still going to have, We're gonna have some things… Stable, and there's still going to be some unstable attributes in development.
Or even if we mark everything as stable, as we add new attributes, we may want to add them as development initially.
And… So… if we… Put them in here, then it's confusing, because it looks stable.
Whereas, so we want to have two different schema URLs, two different, essentially, all the dev stuff goes in here, all the stable stuff goes in here.
And maybe… I don't know, Linmil, if you saw my comment about why this dash dev isn't Completely redundant here.
Just because it is a SEMVR that means something to SEMVR in generic tooling.
But it also… Is possibly redundant, so…
Liudmila Molkova 00:50:04 Yeah, well, figure it out, and… regardless of what we do, we can bump to V0, we can bump to V2. Either way… We will have pros and cons, and you kind of feel it's not important enough.
Unless people have some good reasons to pick one over another.
The one more thing I wanted to chat about here is… We talked about what should we do with GenAI conventions in the query. They are not disappearing, we cannot remove them from there.
But we think maybe once we get to close to releasing this one.
We should coordinate the release of this one with Query Reaper release.
And which would deprecate conventions there.
And add some links saying, okay, they have moved.
Here, into this new repo.
Would have an interest… go ahead.
Trask Stalnaker 00:51:19 Oh, I was just gonna say, I'll prepare a PR, a draft PR, just so we can kind of see what that will look like.
Jamie Danielson 00:51:27 A question I have, I guess, is… do we… does that mean, then, that we don't have plans to ever reintroduce GenAI semantic conventions into the core semantic conventions package? Because I assume that would, get weird if we have, like, something is deprecated, but it ends up keeping the same name And we want to reintroduce it.
I don't know how that re… Reintegration would work.
Trask Stalnaker 00:51:54 We've deprecated and undeprecated things before.
Jamie Danielson 00:51:59 Lovely. Okay. Well, great.
Trask Stalnaker 00:52:02 But I… yeah, I'm not sure if we want to ever reintegrate it. Like, the core… Like, we… we really… we… the federated SEMCOM feels… Right? I mean, only things that really Are shared across You know, broadly, like, I guess, like… Yeah, client, server, I don't know, really core things.
Have to live in the core repo.
And maybe, probably, HTTP.
I don't even know if database has to.
Yeah, Aaron.
Aaron Abbott 00:52:51 Was… Ankit, were you before me?
Trask Stalnaker 00:52:55 Zoom says you're.
anksing 00:52:56 Yeah, I think it was Octavia.
Aaron Abbott 00:52:59 Oh, cool, I don't even see that in my Zoom, because I just used the browser one, but… Yeah, sorry, I was gonna say… So, like, yeah, they're federated. I was wondering… the… like, you don't want to create a dependency cycle, but would there ever be, like, an Uber… repo that incorporates all the federated SEMCOMs into one.
that maybe is, like, a stable and an unstable one that would incorporate them all, like, I'm assuming it wouldn't be the main repo, because you don't want a dependency cycle there.
But yeah, I mean, honestly, having them federated makes sense to me, because, like, the… we have this whole schema URL thing, it kind of reads nicely and works, but yeah, I was wondering if there would be, like, an Uber build of it.
Liudmila Molkova 00:53:44 Why not? There could be.
Trask Stalnaker 00:53:50 to contribute.
Artifact, contribro that has everything.
Aaron Abbott 00:53:59 Yeah, I don't know if we got that far, but that was just something I was thinking about.
Ankit, you wanna go ahead?
anksing 00:54:07 Yeah, actually, I wanted to, like, share at least some of the feedback from my experience with the different versions and, like, with the stable and experimental features or attributes kind of mixing together in one SDK. And this is mostly coming from the Python SDK experience of mine. I don't know if that applies to Jenny's, like, the semantic convention super as well, like.
having, like, experimental features being available along with the stable one, and then they just go along with it. Whatever becomes stable, make them stable and rest everything which is experimental marks them experimental.
I think that has worked really well, other than, like, splitting, like, into two different branches, where I have a stable branch running through, and then… like, the experimental branch where you install this package to get the experimental features, right? So, having one package with the experimental, kind of.
features marked somehow through a decorator of those sorts has worked, like, better than managing two different Forks off, same repo.
That's my experience with the Python one, but yeah.
Liudmila Molkova 00:55:18 This is… what Python does, I'm sure… I want to make sure I understand. So what Python does, the incubating thing, or a deaf thing has everything, and here the philosophy is the same. The deaf thing would have everything.
stable thing would only have stable. Does it… I missed the… is it good, or you've found some problems with it?
anksing 00:55:40 No, actually, that has worked well. Then, actually managing two different forks of the same repo where you have it. One which, hey, if you want to know experimental features, install from this version badge of fork, right, rather than from the main one. So, I think that has worked well, in my experience overall.
So…
Liudmila Molkova 00:55:57 Awesome.
Trask Stalnaker 00:55:57 Yeah, I don't think we would want to change that with the… in the instrumentations, I know with Java, we have, like, an experimental flag that you can enable in all the instrumentations that will get you additional experimental attributes, and that works nicely.
anksing 00:56:17 And, regarding the version, like, whether going back to 0 or 2.0, right, I just wanted to, ask one question.
when a user is kind of using these conventions, like, I'm guessing the name salute remains the same, right?
Alright.
Trask Stalnaker 00:56:32 the attribute names.
anksing 00:56:33 I see. Yeah, attribute names, and even also, like, Gen AI, like, namespace still remains the same, right? There's no change in there.
Trask Stalnaker 00:56:42 Yeah, so it's… oh, go ahead.
Liudmila Molkova 00:56:45 the only change that the user should experience is they would see a new schema URL, Most of them would never care or notice, but, like, we hope that with the tooling we're introducing around validation, and, like, there are more work happening in V2… around V2 schemas, where when you hit this URL, you would actually see the full conventions, for this subset of world.
There will be more people relying on this. In practice, I think today, nobody would care, actually, about the schema URL change.
anksing 00:57:16 Oh, dude.
Again, like, this was coming from, like, Python, experience, where, like, it is all those, like, paper UV read.
based on the semantic convention, like the… they follow some semantic versioning, and based on that, if it goes back, they'll just assume… those tools kind of just assume that this is an older version, not a newer version, right? And they won't… so then you need some sort of, kind of either pinning to a version, or saying that, this is the range of the version that you need to deal with, right? Things like those come up, which can sometimes become a little tricky to deal with, unless you really know what you're kind of dealing with.
So…
Liudmila Molkova 00:57:54 Yeah, the good thing that nothing… there is no tooling that supports it yet, so… The future problem, not the current problem.
anksing 00:58:02 I see, okay. Because I keep hearing the Weaver tool, so I was not sure if that's something, for public consumption, or is it just more for, like, CICD pipelines for some call depot?
Liudmila Molkova 00:58:15 it's about a lot of things around semantic conventions, it's just what we are adding there around this federated semantic conventions and schema URL versioning. It's pretty… No.
Yeah, I sent this one.
Trask Stalnaker 00:58:33 Yeah, something related to these. Josh is working on resolving, you know, depend… Weaver dependencies.
anksing 00:58:45 And to be honest, I think we were also looking at some point to introduce, like, an attribute to capture the semantic convention version that's being used by a certain library, so that's… As these semantic conversions evolve, and you kind of start supporting multiple versions, it's easy to kind of work with them.
Liudmila Molkova 00:59:05 This is what Schema Euro is for, exactly.
Trask Stalnaker 00:59:13 Cool, we are… Basically, at time.
Any last… I will, I'll keep, I'll send updates into the, Slack channel.
To keep folks updated on this, I would love to get this done.
Cut over this week.
So, and just… and live with the consequences, as opposed to, let it, kind of drag on for a long time.
Aaron Abbott 00:59:50 Yeah.
I had one more question on the thing that Anki brought up, and that was, So I… it wasn't clear to me if we would want to just generate one, or generate it into the Python semantic conventions generated code package. Like, would we want a separate package that's, like, OpenTelemetry, semantic conventions, Gen AI or whatever.
Liudmila Molkova 01:00:16 That's the cool one, yeah. So, it will have consequences for some conf packages.
in Java, Python, other languages.
So the… we would probably have a separate package.
Why? Because… We hope that the release cadence will be different, right? The versioning, will be different.
And… We can… It just makes sense to have a separate artifact. Maybe we should merge it into the Otils?
Or have it just, like, next to Teal somewhere in this new recall for Python?
I'm curious what we would come up with in other languages like Java.
Aaron Abbott 01:01:06 like, one of my concerns is, if I understand correctly, with the federated schema, you can… You basically can reference the core repo at a certain version for certain conventions.
And if those… those are gonna have their own version, too.
And it's not clear to me if they would be pinned or opened, because… that kind of matters if you, because if you say, I'm doing GenAI 1.0, you need to make sure you have exactly the convention for all the dependencies at that Semantic conventions depends on.
Liudmila Molkova 01:01:40 This is probably the Uber package discussion. Like, if we want an Uber semantic convention package, that's probably also repo-specific, because it combines the conventions that are… Only applicable to certain Language Roger System.
Aaron Abbott 01:02:00 I have some ideas, we can talk about it next week for Python's sake.
Trask Stalnaker 01:02:07 Alright, we're over time. Thanks, Saul.
Liudmila Molkova 01:02:10 Thank you all.
Aaron Abbott 01:02:12 off to the good work later.
Trask Stalnaker 01:02:13 Bye.
