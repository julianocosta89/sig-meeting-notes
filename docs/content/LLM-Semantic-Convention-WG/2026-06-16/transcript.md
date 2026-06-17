SIG: LLM Semantic Convention WG
Date: 2026-06-16
Duration: 36 minutes
============================================================

## Zoom Recording Transcript

**Trask Stalnaker** 03:33 Hey, Huxing! Hey, Steve.
Itching along.
**Steve Rao** 03:38 Hello, Casco.
**Huxing Zhang** 03:39 I don't know. Awesome.
**Trask Stalnaker** 04:25 Alright, we have… agenda. Thank you, Hoshin.
You wanna kick us off?
**Huxing Zhang** 04:34 Yeah, before that, I think, Chang Long may have some unfinished discussion, not, In the last meeting, I think, but he didn't, didn't write it down in the agenda, I think, so maybe we can continue, that first.
Sure. No, my topic.
**changlong** 05:04 Yes, it's a, it's still, it's about, JNI… command line, and, I'm… what I'm doing now is, I'm following this, same curve to instrument, an OB and observe CLI.
I… as I made the… the… the… the merger request, and the maintainer is reviewing it, so after… when it's done, I think it's ready to… To get in touch with the community.
**Trask Stalnaker** 05:50 So… tell me, where did you submit the… You said you submitted a PR?
**changlong** 06:00 Yes, and then… Screw down, screwed down, yeah, then that's too.
**Trask Stalnaker** 06:06 Oh, here. I see. Oh, okay.
**changlong** 06:10 Yes.
**Trask Stalnaker** 06:25 I see, so this is… what is this?
This is generic observability… CLI, okay.
And… Should have… this… Is there anything in here that is… GenAI specific… And have you seen… I think we have… so if there… if not, it probably belongs over here in this repo.
I forget what we have… So there are some CLI spans defined over here already. Have you seen these?
**changlong** 07:21 Yes.
**Trask Stalnaker** 07:22 Oh, God.
**changlong** 07:22 Oh, but this one is for… I mean, compared to the, the gate command, or the grip command.
There are… there are a lot of command line… Just for… for agentic.
So I think it's better to put it in the GNI repository.
**Liudmila Molkova** 07:49 Can you clarify, put what, exactly?
**changlong** 07:54 I… I think, it's about the, observability command line is meaningful, for the agent.
to invoke the… The command line.
It's not about the… the usual, or the common command line, like the gate, or the grip, or the bash.
**Liudmila Molkova** 08:21 It's like if you're an agent, and then you're executing a tool, a CLI command.
Yes. Then you would report something AI-specific, but the tool itself might be instrumented.
But it would follow generic conventions.
How would it be… Like, it seems to be some combination of the CLI and… tool execution in Gen AI, some merge of these two spans.
Is it where you're going with it?
**changlong** 09:00 Yes.
And then combined with… and combine with the skills.
cost. Usually, an agent, don't know the… what the command line, except for the common ones. If… if it's a newer command line, I think the, the LM or the agent, they don't know the command line, so they need, the skills to learn the… the command line, how to query it.
How do you execute it?
So this is part of it.
**Liudmila Molkova** 09:42 Yeah, thanks, and what are the attributes that are, like, what about this?
understands.
**Trask Stalnaker** 09:55 Yeah, so that was where… This is looking very… like, non-Gen AI… There's no Gen AI span, attributes on… B's… Integration with AI agent traces.
Oh, here's the picture, yes. So, GenAI tool, okay.
Yes.
This makes sense.
Cli execution… Is this… So this is… this is instrumented on the… tool, After the handoff to the tool?
Or before the handoff to the tool.
process execution.
This is the actual process that is running like the grab.
**changlong** 11:31 Yes.
**Trask Stalnaker** 11:45 Oh, go ahead, please.
**Liudmila Molkova** 11:48 So it sounds like… The proposal is… I'm just trying to understand what's the delta.
And it seems it's just the hierarchy, the expected hierarchy and the recommendation for the agents to do just a regular tool execution, instrumentation, and inside the CLI tool implementation to also reduce CLI spans, is that right?
**changlong** 12:21 I'm, I mean, most of the CLI, I mean, implemented by… by Alibaba or other companies, I think… I don't think they have the, open OTL instrumentation.
So… I think, we, the community can suggest or support.
the other maintainers to… to instrument the CLI part.
And… For… for the agent.
**Liudmila Molkova** 12:58 Yeah, that's…
**Trask Stalnaker** 13:00 Oh, go ahead, please.
**Liudmila Molkova** 13:02 Sorry. The… it's… we can probably, I don't know, write a blog, speak at the conferences, show what's missing, and how would it be cool if… I don't know, certain tools submitted, like GitHub.
might do this. Like, it sounds improbable that Grip would implement OpenTelemetry, but GitHub CLI might.
More likely to.
And we would love your contributions if you want to write a blog post, if you want to share how Alibaba CLI tools do this.
I think we would be happy to sponsor it from the Gen AI SIGDA, the blog post.
**changlong** 13:51 It's a good idea, yeah.
**Huxing Zhang** 13:54 Yeah, I can add some comments. I think from our scenario, I can give an example.
If you see, we have Alibaba Cloud provider, Alibaba Cloud CLI for the agents to, access to the cloud service, like, you create, virtual machine you buy… you can create or delete or, create any resources on the cloud. So this CLI can be a very complicated, tool. It can have multiple, functionalities.
So within that CLI, we want a deep observability of how they worked. So maybe the COI should be instrumented, and I think Changlong proposes, what we are missing here. I don't know exactly, I'm not quite looked into this proposal very in detail, but I'm thinking that if there is something missing, maybe we can add some, semantic convention or, spends, I don't know, just an example. So we want to know how this CLI acts, when they… it's… when it's actually doing, complicated, complicated actions, and yeah, that's maybe some of the examples.
**Trask Stalnaker** 15:32 the… the main confusion… I mean, I think the first thing… To me, is… figuring out how… like, we're not… I really don't think we will have… like, I don't want to have CLI spans in GenAI.
and CLI spans in the core semantic conventions.
So, that's the first thing that this proposal immediately is confusing to me.
Okay. So maybe you can… You know.
Figure that out, how that they can play together, and… You know, then this proposal hopefully could be a lot smaller.
In terms of describing You know, this relationship, And then, you know, we can have a… and maybe these, you know, correlation pieces… And then, at that point, I think we could have a… more… A better discussion about… whether there's something we model in Gen AI semantic conventions around this, or, as Lydmilla says, like, if it's more like a blog post community, advertising of, hey, this is possible, already using the CLI, existing CLI spans kind of a thing.
**Huxing Zhang** 17:19 Okay, it looks like a kind of a practice using semantic convention existing. Maybe, we can find out there's something missing we can add to the Added to, to the existing COI expands.
I'm… I don't know.
**Liudmila Molkova** 17:41 Yeah.
I'm… I'm thinking… There is an awesome opportunity to instrument pretty much everything with eBPF.
Because it should know when the process is called, and it can instrument those sites, and it would be a cool place to add this.
**Huxing Zhang** 18:03 Okay.
**changlong** 18:04 Okay.
**Trask Stalnaker** 18:11 Cool, let's… Go on to, Huxing.
**Huxing Zhang** 18:20 Yeah, that's what I've, have proposed to the… in the Slack channel, and, I want to discuss in… detail of how we can collaborate on the open inference donation and the possible contribution from non-suite instrumentations.
Maybe first we can go… go first with the open inference donation, so… I have some comparis- I did some comparison between the Open Inference one and the non-suite one. I actually found there's, varied, varied, implementations across small frameworks. I think, we can… work on some, work on some frameworks that we both implement in common, because we… for example, in the land channel, I think in the, OTO has already had the launch and implementation, so I don't know if the… whether the open inference donation will happen when… When… in terms of the 9chan, there's some frameworks that has already been there. How… how we gonna do… deal with that? And the second… secondly, if there is instrumentation that is missing, and, and from both the open inference one and the non-suite one, we can maybe figure out how, how the They are implemented in… a common implementation, and we can maybe, I don't know, help ring review, or… And I don't know how to… contribute in detail, but let's discuss. And then the third, third, thirdly is the… the implementation at, non-suite has implemented, but the open inference, has… has not done that yet. So we can contribute them maybe one… one by one, just as, Trust has proposed. That has been… become, normal contributions, but it's not a bad… a one-time effort, but we want to keep, contributed and kept maintaining them, because these frameworks are, maybe popular in China, and, most of the developers have… has already really… using them. So, yeah, that's what I'm thinking, so maybe we can discuss.
**Liudmila Molkova** 21:15 Yeah, thanks a lot. So… The first question was if… What… how do we handle this… this migration?
And… even though… the… We have some instrumentations on, like, link chain.
The coverage of operations is lower than an open inference.
And it depends, it can be the case. So I have a PR to add skills, and what it suggests is to, compare what's already in the repo.
Where, the one for free, yeah.
R… If you open the migrate from Open Inference, and there is an inventory of what's already there.
So, if you… If there is an existing package, odd.
The recommendation is to compare what's already there versus what's available in optimal inference, and only migrate the new features, new operations.
And I've tried this, it, on OpenAI, it worked really… reasonably well. I'm pretty sure there are some edge cases for other libraries, but the skill just makes the first pass, and of course, some human overlook is necessary after this.
Ironically, I've tried it on Mr. Owl, and I found that they have native instrumentation.
I found it because Agent told that, okay, there is a dependency conflict for semantic conventions. What?
Anyway, so we could, there is also a review skill, that compares, the migration against the open inference. Here, actually, we can tell it to also consider long suit, as a reference source. It would not take changes from it, but it would give you understanding, okay, where the open inference instrumentation was, where what was covered in long suit, what's missing everywhere, and it would be relatively easy to just add more reference sources for this review skill.
**Huxing Zhang** 23:43 Okay.
**Liudmila Molkova** 23:46 And, of course, we would… like, this is just AI we would much… more appreciate your… involvement on the PRs themselves, like, if you want to review, if you want to contribute, that would be awesome.
**Huxing Zhang** 24:05 I actually, I looked into the… what Trust has implemented, The conformance test.
on the GitHub, and we… I think that's a very good tool.
To use, against, different implementations.
We are working on, on adding the non-suite implementation to that conformance test.
we can, publish that, send the PR to Trask's repo.
soon, or soon, I think.
And we can compare the different implementations, under the conformance, check the conformance.
For across each, different, implementations.
**Trask Stalnaker** 24:59 Nice. Yeah, I have a, there's… also a PR from the Open Inference folks to update, some of their stuff. I need to… once I get out, I've… once I'm done with this, Java release, hoping to get back to, pushing that forwards.
**Huxing Zhang** 25:23 Yeah, I think that repo should be in the hotel repo, it's not… should not…
**Trask Stalnaker** 25:28 Definitely.
Yeah.
**Huxing Zhang** 25:31 Okay.
If we… I… I'm… I still, Thinking that whether we can divide this task into, like, small… smaller ones, so that we can, claim, claim that some, some of the issues, I think it's, I think it's a large, Notch, kind of work.
It's a large amount of work, so if we can divide it into Smaller tasks may be better for us to help.
**Liudmila Molkova** 26:13 Yeah, that's the intent, right? So that, somebody who volunteers to migrate a package will add their name here, will link the PRs, and this is a tracking issue to just know the progress and where we are, and have, like, the guidance documented in a single place.
So if you are interested in any of them, in particular.
**Huxing Zhang** 26:32 Oh, okay.
**Liudmila Molkova** 26:33 Let us know.
**Huxing Zhang** 26:35 Okay.
I think we will, first, do, comparison, or performance check after adding our implementation, and then we'll compare with the open inference one, and the checkout.
Which is the… most not interested from our side, we can then, send our comments on future works, I think.
**Liudmila Molkova** 27:14 Awesome.
**Trask Stalnaker** 27:15 Cool.
Yeah, and I think the, you know, this is a really… We definitely need lots of… contributors, and this is a… I think it's a really good way to break things down, because you can just take one of these, and it lives very much on its own, and whether that's, you know, from I think starting from the open inference and the skills that Lydmilla's Written. And then, you know, at that same time, while you pull things in, or as other people pull things in, you can compare also to the long suite, implementations to see if there's anything additional that Could be layered on or improved.
**Huxing Zhang** 28:08 Okay.
So, regarding, of the long suite implementations, I'm not sure if the… Community has some priorities of how we, which is the more… which one is more interesting from the community side? I didn't send the… I didn't send the link, I just… I think I sent the link, the long suite implementation in the… select channel, I didn't paste it here. Let me… Paste the link.
**Trask Stalnaker** 28:51 I would say, I mean, so from the open inference side, you know, for things that are… As Lyudmila kind of sorted by, you know, downloads is a very, very rough approximation of priority.
If anything, you know.
is interesting. It doesn't mean you have to do them in that order, but, like, you know, maybe take something in the top 10, And work on that.
From the long, sweet side, you all probably have a much better idea than we do of what's popular in China.
And so, you know, feel free to drive that in the priority order that as best.
**Huxing Zhang** 29:45 Okay.
**Trask Stalnaker** 29:48 Cool, we've got, 2 minutes left, .
**Huxing Zhang** 29:52 This is not a very urgent issue, but maybe we can… discuss in more detail in the next meeting. I… just a quick re… Introduction is that we have, have recently published, this, pilot, non-suite pilot. I think we, it's actually, generated, hotel, semantic convention compatible traces for my phone, the coding agent, like Cloud, codecs, cursor, a bunch of this, and send that to the backend, just one short sentence discretion is like this, but maybe we can discuss it in more detail in the next, next week, maybe, and I… I really want… the community to know about this project, and I think this was very popular recently in China. Everyone is working on Coding agent, observability of witness, and We are… we take, like, one… one or two months' effort, the recent effort, to implement them, and, making it compatible with the… semi-conventions. So, this, this can be sent to any TLP compatible backends, I think.
So, so it's, just open sourced, last week.
**Liudmila Molkova** 31:29 Nice.
**Trask Stalnaker** 31:32 is, as… Copilot, does Copilot emit some of this natively?
I can't remember.
**Huxing Zhang** 31:41 Basically, installing some hooks into this coding agent, and, write, write logs in a local file, and then the code pilot is like a collector, send the… collect the logs, and, reconstruct it into hotel traces.
And send it to the backend.
**Trask Stalnaker** 32:06 Cool.
Yeah, yeah, sounds neat.
Alright. Thank you, y'all.
**Liudmila Molkova** 32:16 Thank you.
**Huxing Zhang** 32:16 Yeah.
**Liudmila Molkova** 32:18 See you later.
**changlong** 32:20 Aye.
