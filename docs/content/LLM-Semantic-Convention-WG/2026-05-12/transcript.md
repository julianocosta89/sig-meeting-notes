SIG: LLM Semantic Convention WG
Date: 2026-05-12
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Ludmila Molkova** 04:17 Hello, hi everyone.
**Trask Stalnaker** 04:22 Ayy.
**Ludmila Molkova** 04:24 I'm in the weird place today, so… Not… no, no, northern whites, though.
**Trask Stalnaker** 04:32 Heh heh!
I can drive.
**Ludmila Molkova** 04:38 Oh, thank you. I would appreciate that.
Oh, we didn't migrate this, this board.
it uses… The core repo.
**Trask Stalnaker** 05:54 Right, right. Okay.
Well, it's not really repo-specific, it's more, I think, when we transferred all the issues NPRs, they didn't… the… Word isn't wise.
So I don't think project boards are repo-specific, really.
**Ludmila Molkova** 06:20 But why then? Nothing is showing up?
**Trask Stalnaker** 06:23 Because the… when we transferred things.
I think it lost the link to them.
**Mike Goldsmith** 06:33 It might be the automation, so, in the work… on the… you're right that the board doesn't… isn't tied to a particular repo, but in the workflows, it will be able to pull things from certain ones.
And that might have been missed out. So, under Workflows at the top right.
**Trask Stalnaker** 06:49 Thank you, somebody knows how to use GitHub Project.
**Mike Goldsmith** 06:52 we've got AutoAdd, which is the first one selected, but it's coming from Python Contrib.
**Trask Stalnaker** 06:58 Okay, but then we've got this one, yes, yes.
**Mike Goldsmith** 07:03 Yep.
This is definitely my jam, I like this stuff.
**Trask Stalnaker** 07:10 Excuse me.
**Ludmila Molkova** 07:11 We are so lucky to have him.
**Trask Stalnaker** 07:14 I was just…
**Aaron Abbott** 07:15 Thinking the same thing.
**Trask Stalnaker** 07:18 Okay, so I think… do I need to save it?
Let's see, if I refresh, does it show now?
Okay.
Cool, so we might need to repopulate it, but at least new things should start.
getting added.
**Mike Goldsmith** 07:36 Yeah.
**Trask Stalnaker** 07:43 Let's look at the… PR… Dashboard… So, for folks who haven't seen this, what this is doing is, runs once an hour.
and categorizes… uses a LLM, basically, and some logic to categorize whether a PR is in waiting on author state or waiting on approver state.
And sort of how long it's been in that state.
And it, so for approvers, if you add yourself to… as an assignee on the PR, A, it'll show up here, but, B… You'll be able to… Did it get merged already?
Oh, where's my… Notify error.
So… adding a, Slack webhook, and, basically a… just a private channel where I'll add everybody, and, because it can't DM people, but it can… send to a private channel, and it can at the person, basically when a PR moves into waiting for approval on the for a PR that you're assigned to, so we can just kind of manage the notifications on that channel as only, you know, when I'm added, kind of a thing.
And that… Should… hoping that will help with, kind of, the, conversation flow on those PRs.
And given that Many of us are in GitHub notification, overflow.
**Ludmila Molkova** 09:53 I've been using this dashboard over the last week a lot, and it's awesome. Thank you for creating it.
**Trask Stalnaker** 10:00 Yeah, I've been using it in the Java instrumentation repo, and it's been super helpful.
I added… I don't know if it's useful for us here, but, I've been finding the co-pilot reviews really useful, just as a way to, again, Keep the, like.
Quickly, without spending a lot of time, quickly get some basic feedback and get authors to think about certain things, and… Then I will just… I'll re-trigger it, basically, until it's, clean.
Because it's doing pretty good at now, it won't keep asking the same thing over and over. So if you do say no, like, this is… doesn't make sense, it's fine, it'll remember that.
And so it's just another signal to know that, oh, this is waiting on approvers, and it's gotta, you know.
Clean Copilot, review.
And we can definitely keep improving. We have a… Basic baseline of, co-pilot review guidelines, guidance, but, definitely if you see things that it's… Over-indexing on, we… yeah, it would be great to… Fix that.
And can we auto-hide comments or feedback?
Yeah, so ideally.
I think we should kind of work out what we want the flow to be. I was thinking about this in the Java repo also.
Like, ideally, I feel like I would like the PR authors to just go ahead and mark things as resolved for the co-pilot reviews, once they've resolved it.
But it's really not clear to… Authors what our preferred policy is.
So I'm thinking of having some, like, bot comment on the PR, maybe once it's been opened, and once it has the first co-pilot review there, to kind of give them some basic guidance of the flow that we like to, We like in the repo.
**Mike Goldsmith** 12:29 Yeah, I think that'd be good. I've just noticed a couple of times when there's been a couple of co-pilot reviews, it feels like you're having to, like, really scroll through a fair amount of text before you get to where your current state is.
**Trask Stalnaker** 12:42 Yeah, on that, point, another preference I have that is even for user reviews.
is not to use the mainline PR comments for, so, like… I will… if I have a general comment, I will just find a place Someplace to add it on a file, even if it's a more general comment.
So that it can be threaded, and it can be resolved.
**Mike Goldsmith** 13:22 Okay.
**Trask Stalnaker** 13:24 And then that helps somewhat with the, yeah, the eternal scrolling problem.
Related, I put later, but to… just, I… the, as far as responding to things via AI, like AI-driven comments.
I know in some cases, in the community repo, we even have guidance, like, you know.
Don't use AI to post comments.
But this is definitely a place where I think there is a good exception to that, is on the co-pilot reviews.
It just… Like, when you're talking to a bot, why not talk back with a bot?
And I've been just telling Copilot locally, you know, go to this review, you know.
research all of them, decide what the best thing to do, and then post back, reply, add a commit for, you know, issues, so you can link the… link it back. So, like, it's… Yeah.
Exactly, what's the worst that can happen?
But the, the… Copilot reviews… the idea with the co-pilot reviews is mostly to do that as sort of a first pass on things.
And then… and then the humans come in.
Let's see, so anything… we've got, let's see, two things waiting on approvers… This one I know we kind of had a question, Lyudmila, about where do we draw the line as far as adding Enums…
**Ludmila Molkova** 15:28 Yeah, I… Still think that if there is no instrumentation in Auto World, then? What is the benefit?
But it's not a super strong opinion.
So the… the… okay, so if we approach it from our SEMCON guidance.
We would need to research all the names for this product, and apply the naming guidance, and maybe have some little debates on is it the Z underscore EI, or ZI?
And it's just reasonably… High effort to do this.
was not clear.
benefit.
At least I don't see a clear benefit.
There are non-controversial things, probably.
But still.
I don't know, what do people think?
**Trask Stalnaker** 16:33 So, the main benefit would be… the only benefit I'm thinking of is, is, if there are multiple instrumentations Covering that, but… I'm not sure. I mean, not… so if we had an instrumentation that emitted ZAI and GAI had… something, or… Open inference had something… It would be… Helpful to have the same… backend… Not… Critical.
I think my… My bigger question, yeah, is where… what do we do with… where… How do we justify having some and not others without, like, if we do apply the rule of… we need… Some specific semantic conventions for it.
then… we would… You know, need to go back and remove some of these that don't have semantic conventions for them, other than the constants.
**Ludmila Molkova** 17:52 Well, we, we never remove, we deprecate, right?
Yeah, Ern?
**Aaron Abbott** 18:04 Yeah, I just want to call out, like, I think in this case, the… this is a… this is GenAI provider, right? So it's not… They shared a picture of the model leaderboard, and some of these models are available as self-hosted models, but I think the point here is that these are, like.
they might have their own inference API, which is not OpenAI or some other standard one.
So it might make sense to go through those. And it might make sense to record them because they're potentially calling, you know, like, this managed service or that managed service.
**Ludmila Molkova** 18:44 I, I'm not opposed…
**Trask Stalnaker** 18:47 I was just thinking of the database, like, I mean, I know we came… We've discussed this extensively with databases, and… The worry is that, yeah, there's, like.
A thousand databases, and what are we gonna… are we just gonna keep adding more and more and more?
**Ludmila Molkova** 19:08 And where the guidance came from, that we've added a bunch, and some of them turned out not to be databases, they went out of business, they never, had any up until after instrumentation, or any instrumentation at all.
And it makes sense to add them. I think the question is when?
Is there anything in the world that actually would meet this constant?
Or is it the vanity… Well, maybe I'm too proud, but…
**Trask Stalnaker** 19:41 Right.
Getting on the list.
**Ludmila Molkova** 19:43 Yeah.
**Trask Stalnaker** 19:54 Yeah, and that's actually a really good, Point, and coming back to the reference instrumentation, and scenarios… Cool. I will… I'll follow up and ask to… spell that out better, because I think that's a good thing need on here.
The other PR reading for approvers… .
**Ludmila Molkova** 20:37 For this one, I was hoping that the, skill, review skill you added would, trigger this attribute.
But it… it didn't.
Oh, you're right.
**Trask Stalnaker** 20:49 it locally, and it didn't call it out.
**Ludmila Molkova** 20:52 I think it should be the co-pilot instructions that should evaluate whether this constant comes from any input parameters.
Maybe it was, it didn't have the change when, the co-pilot run on this pull request.
**Trask Stalnaker** 21:10 Copilot review doesn't, reference that skill yet.
**Ludmila Molkova** 21:15 Oh, I see, I see.
**Trask Stalnaker** 21:16 Yeah, that's a really good idea, though. I will… Yeah, we can definitely… So I've been… what I've been doing, I just… I've been running it locally and posting the report from it for people.
Let's see, it's… How…
**Surya Teja** 21:43 How are you? I'm good, how are you?
**Trask Stalnaker** 21:45 7k, okay.
This can probably work. The limit for Copilot, I've been learning a lot about Copilot review, the limit is 4K, it'll only read the first 4K of a file.
**Surya Teja** 22:03 And I have orientation, and I still have to, and I got all the badges, yeah. Oh, and my boss, and…
**Ludmila Molkova** 22:10 Terry, can you please mute?
**Trask Stalnaker** 22:18 So… but we can move this to…
**Surya Teja** 22:21 That's why I love straight back, yeah.
**Trask Stalnaker** 22:22 Let's see, so we've got Copilot instructions, so this is the first thing it reads, and then, Lytmila, I found out.
Well, I found out recently that Mila knew.
that you can add multiple files under here, and each one of those can be another 4K.
So yeah, that'll be… that'll be a good change.
It does look like… Krishna ran the skill.
Here.
Anyway, we can follow up.
Alright, let's… go to intro for New People. I see a lot of people on the… Agenda, Kira, thanks for filling that out, and thanks for joining. If anybody wants to, not required, but if anyone wants to come off mute and introduce themselves.
Now's a… Lovely time.
**Ted Young** 23:42 Hey, I'm back.
I don't have anything to say.
**Trask Stalnaker** 23:47 To have you back.
**Ted Young** 23:49 Who am I?
I work on the GC, if you don't know me.
Bye.
**Trask Stalnaker** 23:56 You are the GC liaison for this SIG.
**Alolita Sharma** 23:58 I know.
**Ted Young** 23:59 Yeah, I was trying to hand that off to Austin, but I think he's busy, so I'm coming back.
Yeah, apologies, I was, kind of, like, stretched too thin for a while, and had a busted arm, so I was, I was kind of MIA for a bit.
But I'm back in action now, so… Good to see you all.
**Surya Teja** 24:26 How can you not remember this?
**Ted Young** 24:28 And currently, I am looking for the host key for this meeting.
Cool.
**Trask Stalnaker** 24:37 Looks like Siri got on mute here, so I think we're good. But yeah, looking up the host key is… that should be easier. It takes me forever, every time.
**Ted Young** 24:46 Same, it's like, go find the doc, and then figure out which Zoom call we're actually on, and I'm like, man, we would lose the quickdraw contest.
**Trask Stalnaker** 25:01 Alright, let us go to, let's see what we've got… Issue opened, by Steve, And let's see, does he have any question about it? Proposal for prompt version.
Prompt name, prompt version… Let's see how… what our time… okay, we've got… some… time. What's, Lyudmila, what's the… I have not been attending any of the other Gen AI meetings outside of this one. I… I know there's a APAC one, and… agents one? Are those different?
**Ludmila Molkova** 25:51 Yeah, so the agent one, I think it was temporary, and it's canceled now.
**Alolita Sharma** 25:56 Yeah, but Ludwila, the invite is still on the calendar, so we'll have to remove that.
**Ludmila Molkova** 26:02 Oh, I think…
**Alolita Sharma** 26:03 Mondays, yeah.
**Ludmila Molkova** 26:04 Okay, I'll take another look.
**Ted Young** 26:07 I think it's gone now.
**Ludmila Molkova** 26:10 Yeah, I removed it a few days ago.
**Alolita Sharma** 26:12 Okay, okay, cool, because it was, there last week, sorry.
**Ludmila Molkova** 26:17 Yeah, there is also the, APAC time zone meeting. It's every Monday, 6 p.m. No, every, every other Monday, 6 p.m. Pacific. It didn't happen Last week.
Because, there was no quorum.
It… Actually, it is a problem because it rarely happens.
It depends on me being able to make it, or somebody else from the ScoreSig being able to make it. And it, at best, happens monthly. But we have interest in… from Alibaba folks, and it's… they cannot join this meeting.
So, I hope we can make some reasonable effort to include them.
**Trask Stalnaker** 27:06 Cool, thanks. Yeah, so we've got Steve from Alibaba, and also, Minghui, who is, now an approver in this repo.
From Alibaba. So, yeah, I might… I'll ping them. I'm… I wanna… I'll see if they could… does an hour earlier… Work… Better or worse for you? Okay.
I'm gonna see if… yeah, I'm gonna see if we could move it an hour earlier.
That would work better for me.
So yeah, if anybody's got thoughts on GenAI prompt version, Please leave comment.
Next up is, Surya and Ludmila…
**Ludmila Molkova** 28:12 Yeah, Surya, do you want to talk about it, or if you, if you're not comfortable talking, I can… Quickly, Shira, this is the… Primitive… for GenAI to use to work with streams.
It's important for us to have it common. We can track time to first talking, time between tokens, and believe indication if it's streaming congenia, so individual instrumentations don't need to do much around it. Just use the primitives.
And I think this is the pull request that I've been waiting for before we can pull the trigger on the move between repos. We'll talk about this later. Maybe we shouldn't have these blockers, but we'll talk about it. So, this is the last call for reviews. I think Surya addressed all the changes, and… recently, and Please take a look, and hopefully get it merged.
**Aaron Abbott** 29:12 I'm taking a look right now.
**Ludmila Molkova** 29:14 Thank you.
**Trask Stalnaker** 29:19 Alright, well, that leads us into, yes, the big topic for the day.
**Ludmila Molkova** 29:25 Yeah, thank you. So… What I've been trying to do with this is to… follow the plan where we, take what we have in Python Contrib to start with, And, we're… Migrate to Teals, and that way, migrate libraries one by one.
Turns out it is a lot of coordination between repos.
And, for example, I've been waiting on the deals to get to the reasonable point.
To then migrate it to the new repo.
It's a viable plan, but I think that the amount of coordination scares me a bit, and I'm proposing a slightly different approach that is ripping the band-aid, and we would just take whatever we have in the country, as is, or use the instrumentation libraries. We will move them, Just as renaming folders, probably.
For now, as a first commit. And then, immediately after, I'll follow up with PRs to strip down, legacy parts from them and the necessary parts. It will be easier to review, right, because we will see the delta.
And it's less scary move, we don't need to sync that much, or syncing becomes easier.
And assuming we are ready to start bootstrapping, we can start this today.
**Mike Goldsmith** 31:07 I think this is a good idea. I think the longer we wait, the more painful it's gonna get, and the slower we're gonna go, at the point. We're trying to go faster.
**Alolita Sharma** 31:15 Yeah, but, Lunmula, the option 2 is, easier, right?
**Ludmila Molkova** 31:21 Option 2 is, I think it's easier for… And faster.
**Alolita Sharma** 31:26 Yeah. Easier.
**Ludmila Molkova** 31:26 for, I think us to review.
**Alolita Sharma** 31:28 I think we should just go for it.
**Ludmila Molkova** 31:31 Yeah, it creates a little bit of, questions of, okay, we are taking, I don't know, Anthropic library, I have no idea what the state of it is in Country Repo, and maybe we would rather import it, port it from Arise, if Arise folks are happy with it, but we can also hoard the Delta.
**Alolita Sharma** 31:51 Alright.
**Ludmila Molkova** 31:51 I think it was not… one does not block another.
Okay, so then I'll trust, I'll need your help, I'll ping you, we'll coordinate.
**Trask Stalnaker** 32:03 Yeah, let's do it.
**Ludmila Molkova** 32:05 Yay.
And Aaron, you seem to… Preserve package names, yay!
**Aaron Abbott** 32:14 Yeah, I, I think… it was… most of them were, you know, fine, but there was a couple where I think the thing that we said we were gonna do was match the name on PyPi exactly for whatever comes after OpenTelemetry, basically the prefix.
And there was just a couple of them which were different, so… We don't have to talk about it now. We can sync up offline, but, yeah, I think… Maybe, like, the goal was to, keep the precedent from existing instrumentations that exist out there, which is also fine. We should just, just want to make sure that it wasn't a typo. That's all.
**Ludmila Molkova** 32:54 Yeah, I'm curious, do you know what we should do with Vertex AI and Google Gen AI? Should we keep the old names?
**Aaron Abbott** 33:03 I think Vertex, we don't need to move over, because it's been deprecated, and at least the… for at least 6 months, I think, the actual client library, for at least it's used for, for calling the inference APIs.
So, the reason it was kind of still sticking around was people were stuck on it, like in… for the Langchain integration, for example, but they've… I think they've moved off that at least 6 months ago, so… I'm okay to, you know, pull that one out of scope for now, so we can just… leave it as is. For Google Gen AI, like.
The existing package name is used in a lot of places and stuff that we've built. So, for example, like, in, In… let's see… I think we have it in ADK as an optional dependency, for example, and also some other places, so… You know, we could… we could publish to both, or we could just try to move over to the new one, and then I could… chase everybody down to use the new one, but I don't have a strong opinion.
**Sergey Sergeev** 34:05 Yeah, and also the outdated package, really have a lot of outdated dependencies, so it's a nightmare. Let's try to deprecate it.
**Ludmila Molkova** 34:16 Which one?
**Sergey Sergeev** 34:17 The vertex, yeah, I believe.
At least the vibe itself, not the instrumentation, but…
**Ludmila Molkova** 34:28 So let's just not migrate it. And for Google Gen AI, is there a strong reason to rename package at all?
Like, it's better for users if they don't… Change it, and…
**Alolita Sharma** 34:38 Yeah, agreed.
Redmela, I agree with you. I don't think we should touch it.
**Aaron Abbott** 34:44 Okay.
**Trask Stalnaker** 34:45 Are we talking about Vertex, or are we talking about the other Google.
**Alolita Sharma** 34:49 vertex.
Vertex.
**Ludmila Molkova** 34:51 So, for Vertex, let's not migrate. For the Google Gen AI package, the different one.
I think we should move it to the new repo, but the package name remains.
**Alolita Sharma** 35:03 Yeah.
**Trask Stalnaker** 35:05 Bye.
I mean, you know, Why have that one outlier.
**Ludmila Molkova** 35:12 Because… It's easier for users, because we can.
So, okay, if we… if it matches… if it would match the pattern, it would look like OpenTelemetry Instrumentation, GenAI, Google Gen AI.
It's ugly, and Open Telemetry instrumentation, Google Gen AI, is… looks reasonably good, and also it's, the same package name that we already published, and we own it, it's not a Panelimetry one, right?
**Alolita Sharma** 35:47 Yeah,
**Trask Stalnaker** 35:50 Cool.
**Aaron Abbott** 35:51 Yeah, I'll reserve… I'll reserve this one just in case, also.
**Ludmila Molkova** 35:54 Wait, we already published it.
**Aaron Abbott** 35:58 No, no, I mean, I'll reserve the, the one with the… following our naming convention… convention.
**Ludmila Molkova** 36:04 Oh, Jenny, Jenny,
**Aaron Abbott** 36:05 Yeah.
**Ludmila Molkova** 36:06 Okay, awesome.
**Aaron Abbott** 36:10 Okay.
**Trask Stalnaker** 36:12 GenAI Google?
I'm good. I'm good with, Google Gen AI.
**Aaron Abbott** 36:24 Awesome.
**Ludmila Molkova** 36:37 Okay, so Dan, we should be good with this topic, yay!
**Trask Stalnaker** 36:46 Yeah, alright. Let's… I'm glad that, we have the SEMCONV rep repo, kind of going now. I was worried about having two of these repos in flight at once, so I'm actually glad that the Python one, got delayed a little bit.
So, I think we're good to tackle that one now.
Alright, I've got the next… topic, kind of touched on earlier, just kind of wanted to get people's thoughts. I know we're all figuring out in this brave new world, when we… use AI to make comments, when we don't like AI making… when we don't like people replying to our comments with AI, what… when there's, like, a big AI wall of text.
I've noticed… variety of… well, A, preferences from people, and B, practices in the repo, some of which for me personally, work, and some which don't, but kind of wanted to open up the topic here, since… expectedly, as, Lamila mentioned, In chat, I think this is, I think, the place where people are using Gen AI the most, expectedly.
And, Yeah. Sergey, kick us off.
**Sergey Sergeev** 38:24 Oh, yeah, I can share what we do in some of the reports. Basically, we have documents which were AI-generated, or comments and so on, so they clearly have to communicate.
Basically, it's an agent's config.
clearly communicate that this is AI-generated, and so on.
probably a header, like, the first line in the comment. Once humans, review And basically… Validated, so you can put a status, like, human maintained, or probably username, who maintained it, or who reviewed it.
And, then you can have another instruction for the agent, telling it not to touch it, not to order it, and so on.
So, it's one of the approaches I highly recommend.
Basically, to have clear instructions for the agents, and clear, Status, who or what produces the document.
**Trask Stalnaker** 39:33 I see, so this is… Beyond just commenting But also for editing specific documents.
**Sergey Sergeev** 39:43 Yeah, same about pull requests, was it fully generated, and where is the spec which was used to generate it? So, basically, opening up, The logic behind the generation of content.
It's… it's also, kind of, how… the development shifts from just reviewing the code to reviewing the spec. So, sometimes you need to review the spec, because if the code is AI-generated, so if you agree on the spec.
What needs to be done.
So, you probably… Can catch a lot of problems earlier.
**Trask Stalnaker** 40:34 Yeah, I've seen that's, Common, or not common, but for, repos that are shutting. I've seen multiple repos, shutting down PRs and only accepting issues.
And then they just assign the issues to Copilot and drive them.
I've also seen repos where… they essentially treat PRs as… prompts plus additional context, and then they basically rewrite them using their agents. I don't… I think we want to go that far, but yeah, there's quite a… Spectrum.
Just to follow up on that, Sergey, the… you're doing this in, like, agents.md?
**Sergey Sergeev** 41:34 Yeah, yeah, clear instructions to the agents, like, never overwrite human-generated thing.
And second, basically, clearly identify yourself, so… how to… we can… we can ask the agent to include pull request description, what the spec.
Which is given to the agent to build the code, so you can review the spec and so on.
**Trask Stalnaker** 42:03 Would you mind, if… is that something you can share either publicly or… or just DM me and I can steal things from it?
**Sergey Sergeev** 42:13 I can create a pull request for AgentsMD, probably, but I see a lot of hands raised, so… Yeah, yeah.
**Trask Stalnaker** 42:22 Cool, yo, Lynn Miller.
**Ludmila Molkova** 42:26 Yeah, I would love to see the AgentsMD pull request. I was thinking AgentsMD is our back channel to the people who use AI. We can talk to their eyes through EdgeMD.
And this is the place where we can tell it to be concise, and also to do all our, best policies, so let's just invest in EdgeMD.
And maybe if we… after that, we still need some measures to… like, the policy measures?
Let's do it, but I… I have higher hopes for AgentsMD than to human-targeted policies, and so…
**Trask Stalnaker** 43:12 Aaron.
**Aaron Abbott** 43:15 Yeah, so I was… Tras, was this originally just in regards to, like, design kind of things and comments, not, like, code?
**Trask Stalnaker** 43:23 Yeah, yeah.
**Aaron Abbott** 43:24 Okay, okay.
**Trask Stalnaker** 43:26 comments on PRs, comments on issues.
**Aaron Abbott** 43:30 Gotcha.
The only thing I was gonna say was we… we have… I just pasted our AgentsMD for, like, contrib… I've heard some back and forth on this, I don't know if there's strong guidance from OTEL, but there was concerns that, and this is in regards to, like, you know, code, but there's some concerns that this is advertisement or something, so I guess we could just have it say generically what it was, it doesn't have to be, like, I'm… whoever's AI assistant from whatever Yeah, we do have this for now, I don't know if there's strong guidance in hotel community for this.
**Trask Stalnaker** 44:05 I mean, honestly, I'm just going under the assumption that all commits are… Co-op… assisted by… some… Model, and so this doesn't really… give me any… Information that is useful as an approver.
**Aaron Abbott** 44:24 Yeah, yeah, that's fair.
**Alolita Sharma** 44:25 Yeah, that's fair.
**Aaron Abbott** 44:28 I guess the concern was mostly about just telling it to be generic, as opposed to… Providing, advertisement space or whatever.
**Trask Stalnaker** 44:35 Oh, right, right.
**Aaron Abbott** 44:37 Yeah.
**Alolita Sharma** 44:38 I think, Aaron, the current guidance from the Linux Foundation and CNCF which is the larger, policy that, you know, most of the projects are following, hotel included, doesn't actually specify anything about the model names yet. So maybe we can actually just, Get it changed in the ups… you know, in that centralized policy, and then it'll just flow in.
**Aaron Abbott** 45:07 Okay, yeah, that sounds good. I don't think we need to be the…
**Alolita Sharma** 45:11 Yeah, I mean, let's… let's go and get them to change it.
Trask, does that make sense? I mean, we can definitely go and ask.
Quite an issue, and…
**Trask Stalnaker** 45:25 I… I don't particularly care about the commit assisted by. As I mentioned, like, I'm just… it doesn't.
**Alolita Sharma** 45:32 It doesn't give me any.
**Trask Stalnaker** 45:33 thing as an approver.
**Alolita Sharma** 45:35 Exactly, and…
**Trask Stalnaker** 45:36 So I, I don't… I… I don't care about…
**Alolita Sharma** 45:39 But I mean, over time, right, you'll have, like, all this… Noise by different, you know, different models just being attributed, and… It's kind.
**Trask Stalnaker** 45:51 Yeah, if the CNCF wants to say something about that, I'm happy to… adjust.
**Alolita Sharma** 45:57 Okay, I mean, I can take an action item to file a, Request with them to see what they come back with.
**Trask Stalnaker** 46:06 Okay.
**Alolita Sharma** 46:07 Yes.
**Sergey Sergeev** 46:07 Yeah, also, for those companies who don't have the models… Yeah.
**Alolita Sharma** 46:12 On this one.
**Sergey Sergeev** 46:12 Not necessarily for them, it's kind of internal knowledge, so you don't necessarily want to disclose which tools you use, and so on. So I would not make it required, just optional. And second, for me, personally, the most important, what was the spec the model executed on?
So I want to look at the code before I align on what needs to be done.
So, I don't care what model was used, and so on. I'm more caring about what was the spec.
And then I can review the code.
**Alolita Sharma** 46:53 Yes, again, I agree with you.
**Trask Stalnaker** 47:00 Cool, that's great. Yeah, Surya, that would be amazing. Send a PR, just, at least that'll give us some place to, start.
the conversation there.
**Sergey Sergeev** 47:13 I think Aaron's link from Cantape, the AgentsMD, and Open Inference AgentsMD are a good start, especially if you want Open Inference to continue to contribute to the standards they have. I think it's more in discussion with them.
First, to make an alignment, and then we can extend it as needed.
**Trask Stalnaker** 47:41 that do not… is not to post on issues or PRs that are AI-generated.
Yeah.
So this is where I think there's kind of a line, for me at least, is at least when replying.
to… bots, I'm comfortable.
Using bots to reply to bots.
And maybe to even assist me with some things, but yeah, there's… but not everywhere, like, some… I… yeah, it's a… Interesting gray area. For me, I don't know, for others.
**Sergey Sergeev** 48:20 Yeah, ideally, we improve the agent's MD to provide standards, or AI coders.
So, those AI reviews won't make sense in this case, so if you have clear instructions what to cover, so… and if you're using the same models to review, so why… Why do you think it will be a better review?
**Ludmila Molkova** 48:45 Oh, they totally, flag themselves in reviews.
**Trask Stalnaker** 48:49 Yeah, yeah.
**Ludmila Molkova** 48:57 Oh, gee We can polish this sentence.
I, I don't.
**Trask Stalnaker** 49:04 Yeah.
**Ludmila Molkova** 49:05 Pilots talking to each other.
**Trask Stalnaker** 49:09 Yeah, I agree that, Jamie, that's… I read it.
the same way.
**Jamie Danielson** 49:13 But it was, like, do not engage, like, do not encourage this behavior, is how I read it.
**Sergey Sergeev** 49:22 Yeah, again, I think the most important is to make sure that AI's team is comfortable with continuing to contribute to Open Inference if we Make this donation to happen, and then we can extend it as needed.
Just… just want to make sure it doesn't get into… Non-stop bike trading conversation, which works.
everything else.
**Trask Stalnaker** 49:51 Okay.
**anksing** 49:56 Actually, in my experience, like, one thing that works well for me, maybe certain leads, like, we try to add access to agents and front to see, like, follow things and what to do, right?
And soon it becomes, like, too big, too large, and then, like, breaking out things into, hey, for test, these are the instructions to be followed, and, probably if you have another link, to another file, or to another skill, let's say, hey.
you're supposed to use only Pyth framework, or any Unix frameworks, like, for writing tests, or this is the level of, a mocking that you can do to write the price right. Those kind of things have been very helpful, and not having all of them, like, listed off as is in the agent's not empty is really helpful, I think, that it does not kind of blow off things down.
**Trask Stalnaker** 50:46 Yeah.
I can share what…
**anksing** 50:50 You're blue.
**Trask Stalnaker** 50:51 Done, kind of, in… Where is her?
Oh, I guess we don't have an agent's MD, because I've only… Yeah, we'll link out to… Didn't hear where… Somewhere we link out to this.
Knowledge index, basically, where we tell it, yeah, instead of loading the whole… all the stuff all at once, we tell it, for this stuff, go to this file, for this stuff, go to that file.
And that works.
Well… Alright, thank you for that conversation. Let's go on to our last topic.
Mike?
**Mike Goldsmith** 51:51 Yeah, we've been doing a lot of work in the Python core and Contrib repo to try to make maintaining the repo a little bit easier, so doing more automations, more of the SPDX headers instead of the bigger ones, using Towncry to manage changelogs, once. I guess I didn't… I didn't check the agenda, but I know that we're not quite ready yet with the new repo, but when we are, I'm… I think we should move a lot of that over to make that easier as well. So, yeah, just wanted to make sure that that's something that we know we have to migrate as well as the instrumentation, is, like, those things to make sure the repository is healthy and usable.
**Ludmila Molkova** 52:31 Yeah, do you have a list? Like, if you can create a list, we can just use it as a check. Check the boxes.
As we do.
**Mike Goldsmith** 52:39 Yeah, I could create an issue, and then just put, like, a checklist of things that we want to do, and then make that as, like, the thing, like, to do it that way.
**Ludmila Molkova** 52:46 Okay, so then we will bootstrap the repo, and you would create an issue on this, and more than…
**Trask Stalnaker** 52:51 issue in the current repo, and we can transfer it once we have the.
**Mike Goldsmith** 52:55 Yeah.
**Trask Stalnaker** 52:55 New repo.
**Ludmila Molkova** 52:56 Yeah.
**Mike Goldsmith** 52:57 Yeah, I can do that.
**Ludmila Molkova** 53:00 Any automation.
The answer is automatically yes.
**Mike Goldsmith** 53:05 Yeah, yeah, we're trying so hard in the Python repos to get away from the endless resolve conflicts on changelog.
**Trask Stalnaker** 53:13 Mmm…
**Ludmila Molkova** 53:14 Oh, that's… this is a good… maybe we should have this discussion.
So… should we do changelog, or should we do chlogin that we use in semantic conventions and then go repos? How did you end up fixing it in Python?
**Mike Goldsmith** 53:31 We're gonna use the Town Cryer per package, so you still get the same functionality, so you still get a per package changelog, and then they can independently move, so they can be released independently of each other, too.
**Ludmila Molkova** 53:45 I see.
And this is change log per each instrumentation library.
**Mike Goldsmith** 53:52 Yes.
**Ludmila Molkova** 53:53 Okay.
This makes sense. Oh, the… maybe then the… the login does not make that much sense, but it's still easier on the release scripts. Well, we can always switch to change login later. Yeah.
**Mike Goldsmith** 54:06 Yeah, I did a comparison between Town Cry, which is what we're using in those repos, and ChangeLogin, and if you set it up, Town Cryer, the same way that Chainlogging would want to work, where it's per package, they're very, very similar. I think the difference is that you get a slightly more structure on the YAML format that it wants the fragment to be in. Other than that, they are very, very similar.
**Ludmila Molkova** 54:31 Yeah.
And then, for the new repo, sorry for going off-topic, but I'm curious what folks think. For the new repo.
I'm thinking, the release… we should release everything together. Maybe we can switch to per package release later, if it's absolutely necessary, but based on how we've been releasing things in the past, there is no reason to actually release things independently.
**Mike Goldsmith** 54:59 Yeah. For, so the way that I've got the Python contrib repo is that I'm gonna have a few that are independent, and a few that are centralized, but then one, TOX commander that can do everything all at once, so it's very easy to manage them all together, and then it'll just bump all of them independ… like, their own versions will bump, so if one has been moved.
It doesn't have to be set… the same version doesn't have to be consistent across every package, so it worked quite well that way.
**Ludmila Molkova** 55:26 Oh, cool, so this is… you already figured it out for biking contract, so we can just reuse whatever is done there.
**Mike Goldsmith** 55:33 Yeah.
**Ludmila Molkova** 55:34 Awesome. Let's do it.
**Trask Stalnaker** 55:42 All right, we've got 3 minutes left here till 5-minute cutoff, but no new topic, so, Give people a second here, if they've got anything they want to raise.
Great!
Well, good to see everyone.
See you in the… see you in the repos.
**Alolita Sharma** 56:13 Yes, you're on the repos. Thank you. Thank you.
Thank you.
**Ludmila Molkova** 56:16 So…
**Trask Stalnaker** 56:16 I…
**Leighton Chen** 56:17 Bye. Bye.
