SIG: LLM Semantic Convention WG
Date: 2026-04-14
Duration: 63 minutes
============================================================

## Zoom Recording Transcript

Liudmila Molkova 00:03:36 Hello, hi everyone.
shuwpan 00:03:40 Hello!
Dat Ngo 00:03:41 Hey, Lyudmila.
Liudmila Molkova 00:03:44 Hey, how are you?
Dat Ngo 00:03:46 Good, good.
Can't complain, I'm alive.
Liudmila Molkova 00:03:53 Wow, you have, low expectations.
Dat Ngo 00:03:57 What do they say about happiness? Happiness is expectation minus reality.
Liudmila Molkova 00:04:04 Yeah.
One way to increase your happiness.
Dat Ngo 00:04:24 -
Liudmila Molkova 00:04:25 Hey, let's see what I have.
Please add your name to the attendees, please, and… Oh, let's see what are the staining topic?
And we didn't get to a lot of things last time.
Trask, I remember I… are you here already?
He's not here yet, but he'll come.
Trask Stalnaker 00:05:07 I'm here.
Liudmila Molkova 00:05:08 Oh, you're here. Did we discuss it fully? Span for evaluation results, or is there something we want to talk about?
Trask Stalnaker 00:05:17 I had a… yeah, I had follow-up.
Liudmila Molkova 00:05:20 Okay, awesome.
Trask Stalnaker 00:05:21 Question…
Liudmila Molkova 00:05:27 R… Not sure if Jamie is joining today. Welcome, do you know?
Wolfgang Therrien 00:05:34 Jamie, is traveling right now, so… but I can, she's brought me up to speed, and I can jump in for her.
Liudmila Molkova 00:05:40 Awesome, thank you.
Okay, so we'll keep this on the agenda. Please add your topics.
And Maybe we should… About this one… Okay, let's do the triage… Nothing in progress, some new issues.
Trask Stalnaker 00:06:36 Good mulet.
Did we include PRs?
That are in progress in the triage board?
Liudmila Molkova 00:06:45 Ehh, yes, that's a great… yeah.
They should be here. For some reason, they're not, Let's make it as a quick note.
Trask Stalnaker 00:06:58 I can… I can add them.
Liudmila Molkova 00:07:02 Nice.
The tricky part is that we have PRs in Python, PRs in semantic conventions, And this board contains… Both repos. But.
Trask Stalnaker 00:07:38 dash AI, gen dash AI.
Liudmila Molkova 00:07:40 Alright, thank you.
Nope.
It's label.
Trask Stalnaker 00:07:46 Label colon area, there we go.
Liudmila Molkova 00:07:52 Finally.
Quote, There is a bit… quite a few.
I'm going to exclude Ruft.
They are… So… It's actually a great point. I think we should start from the PRs, not from the issues.
Cool. So, let's get a quick check on what's going on, Now, Kumar, are we ready to review this?
nagkumar 00:08:38 Not yet. I think the… there will be other, working groups which will… which are talking about it.
So I'm still in talks with them, and they're reviewing it, before we bring it up here. The OCSF, and You know, other working groups, COSI working groups.
Liudmila Molkova 00:09:01 That's awesome. Can I convert it to draft? Oh, sorry, go ahead, Drask.
nagkumar 00:09:05 Yeah.
Trask Stalnaker 00:09:05 Yeah.
nagkumar 00:09:06 Let's do that.
Trask Stalnaker 00:09:08 I'm gonna go to the… attend the OCSF meeting on Thursday to kind of start, not for this PR specifically, but for the broader question of how can we collaborate with them on GenAI security.
nagkumar 00:09:24 Perfect.
Trask Stalnaker 00:09:24 It'd be great if you can… I'll send you the info if you don't have it already.
nagkumar 00:09:29 Oh yeah, it's on my calendar already there.
Trask Stalnaker 00:09:31 Awesome.
Liudmila Molkova 00:09:39 Okay, I converted it to the draft, thank you, and it's, it's awesome. Great work.
collaborating there.
So the semantic conventions for memory operations.
I think I had a comment, Jask had some comments. Should we add it to the agenda, and spend maybe, like, 5-10 minutes talking through?
Trask Stalnaker 00:10:07 Yeah, I think we're pretty close on that.
Liudmila Molkova 00:10:09 Yeah.
Reasoning tokens.
I remember… Okay, so this was a good PR.
But I think it did some unintentional changes.
And… We are… Not able to… Merge it now.
Yeah, I'll take another look. I don't see immediately if changes were resolved, or… Oh, no, I think there are some unintentional changes.
Still.
Trask Stalnaker 00:11:29 Yeah, I left a comment about unrelated, that there were what seemed like some unrelated Changes… as well.
But overall, I mean, the edid prototype I did post a prototype for it. It does look… I mean, the… I feel like we should be able to get this in.
Liudmila Molkova 00:11:58 Yeah.
Is Otter Verdi… Gregor, other here in the call?
Doesn't seem so…
Alolita Sharma 00:12:09 No, doesn't look like a funeral.
Liudmila Molkova 00:12:14 he, thank you. Okay, so there are some Google-specific peers.
I'm looking at Aaron and Dylan to… to bless them first before… We would review them from GenAI or Semantic Convention's perspective.
Aaron Abbott 00:12:36 Yeah, that's fair. I… I think Rima's a coworker, but not, like, on my team, so I'll sync up on these and see if they're still needed.
Liudmila Molkova 00:12:48 Awesome, thank you.
Okay, and… The last two… the workflow, metric… Radima, do we have it on the agenda? Should we add it?
Ridhima Satam 00:13:06 We don't have it in agenda, it's just that there are some comments to be addressed, but yeah, we can discuss about it.
Liudmila Molkova 00:13:13 Okay, so, like, can you take a quick look, kind of, if there's anything important to discuss in this call, please add it to the agenda?
Ridhima Satam 00:13:20 Sure.
Liudmila Molkova 00:13:22 Yeah, thank you.
Planning operations…
Surya Teja 00:13:50 The person who raised the request is not in the call, but I synced up with him, and told him that we can leave any questions as comments on the PR, and he can get back.
to us whenever he's free. I took a quick look at this one, and this looked good, and fine, but I'm not sure if the SIG is good with raising another span for, the plan operation that we do with agents or not, so… Please comment on it, and If it looks good, we could go forward by seeing if it aligns with the semantic conventions and standards or not.
Liudmila Molkova 00:14:32 Yeah, just gives it a good opportunity to use the prototyping skill for this one?
Trask Stalnaker 00:14:43 Yeah, I think I missed this one.
Liudmila Molkova 00:14:52 And you still do it yourself because you're still testing it, or, like, is it something that others can still doing?
Trask Stalnaker 00:15:01 Yeah, I mean, it's still in my personal repo. People like you can send PRs to it, for sure. I am, this week, I'm working on, figuring out how to get it into OpenTelemetry.
But I can… yeah, it's… it's… I'll send a… I'll tell the agent to run the skill and see what it produces on this one.
Liudmila Molkova 00:15:31 Thank you.
Okay, and we are out of the box, for our agenda. It's great that we spent it on PRs and not issues.
Okay, if anybody is new to this call, and you want to introduce yourself, tell us what brings you here.
The stage is yours.
Benjamin Kawecki 00:15:57 I can go.
Yeah, so my name is Ben Kwecki. I've been active on the, the Slack channel for a bit, so I work at Bloomberg, and I do some of our, like, internal Gen AI, observability stuff.
So previously, all of my correspondence has been around that, but Bloomberg is currently doing an engagement with OpenTelemetry directly, where we're contributing a bunch of open source hours from employees as part of their company time. I'm involved in that as well.
So, I wanted to see if I could just help out on anything in general. The kind of guidance has been to look for, like, good first issue and stuff like that, but I know the codebase pretty well, specifically with, like, SemConv, the instrumentation contrib, like, the GenAI, and OpenTeometry Python in general.
So, if there's anything, you know, that you guys, think I could help out on, or if you guys just want me to take a look through issues and just see, you know, if anything makes sense, please let me know. But if there's anything you're like, hey, this would make sense, or, you know, if we need some extra time and hours here, I'd love to help out, so…
Liudmila Molkova 00:16:57 Yee, nice!
I, I think we'll talk about this, you have a topic on the agenda, but I don't think we just encourage people to work on good first issues, we don't have any good first issues. But we have a lot of issues and pull requests.
And, if there are any particular areas that you care about, and you have opinions, and you see if things are not moving in the right direction, or there are PRs for the areas that you care about.
and you are willing to spend some time reviewing them, that would be awesome. I think there will be some interesting work, coming with the conformance testing, Trask is working on, and also have a bunch of instrumentations in Python that need a lot of work, that don't have enough feature coverage.
These are the areas where I think contribution would be awesome.
I wish we had it documented better.
Benjamin Kawecki 00:18:06 Yeah, I'll take a look for sure.
Liudmila Molkova 00:18:10 Thanks. And maybe the first topic on the agenda would… would be… a good starting point. Anybody else wants to introduce themselves? Sorry, it's a symmetric, it's the stage for new people, and old people kind of kept… keep quiet, but… Well… Yeah.
Wolfgang Therrien 00:18:29 I'll say hello real quick. I think this is my first time being on the Zoom call for this one. My name is Wolfgang Therian, my pronouns are he and him. I, work at Honeycomb on the AI observability team.
And so we have a vested interest in, define… helping define and push forward the semantic conventions here, so that we can help folks make sense of, like, what their agents and their, their, their, agentic systems are doing. So, that's, that's my… 30 seconds.
Liudmila Molkova 00:19:03 Great to have you here.
Aaron Abbott 00:19:06 You're welcome.
Shubhanshu Surana 00:19:08 Hi, everyone. My name is Shubhan Shu. Sorry, Wolfeng away, you're gonna say anything, I just jumped in.
Okay, okay. Hi everyone, my name is Shivan Shusurana. I'm part of Apple, I'm part of the observability team here, and we help engineering teams with their instrumentation, as well as sending data through OpenTelemetry to different observatory systems we run here at Apple.
excited to be part of the community and contribute as we start to look more into SEMCOV and Gen AI instrumentation alongside all the Apple-related apps.
Liudmila Molkova 00:19:45 Nice.
Aaron Abbott 00:19:45 them.
Liudmila Molkova 00:19:54 Okay.
Anybody else?
Thank you all for coming!
Great to have you.
Moving on to the first, big topic, Jamie did a great job, drafting, the… Road up?
For the group, and this is the… something I think we… we discussed in the past, we, like, voted on where the… what are the areas the SIG would be interested in contributing to, and evolving over time, and… here they are, with some additional, information. This is the, list of applicable issues craved by AI, so it totally could miss something, or, Maybe miss where it is, but… Essentially, the top areas are the instrumentation coverage.
Right, we do have some reasonable coverage for conventions, we don't have operations for certain things, like tasks, oh, sorry, the planning, maybe some tasks, and And so on. We're… Do, though, have coverage for many other things, but not on the instrumentation side.
So… This is probably the… Top area.
than, there were… Things that could be better in terms of, the process, or… I don't know how to phrase it, maybe we need to find a better name, but essentially, the velocity with which we make, how we can do things faster and better.
Yeah, well, sorry, I'm taking over. Maybe Jamie instructed you how to present it. Do you want to present?
Wolfgang Therrien 00:21:53 No, no, I think this is, pretty much what we had in mind, you know? I think, when Jamie and I were just sort of going over this the other day, we sort of, identified, like, a handful of, like.
areas that we might want to think about first, and one was actually, like, kind of writing down, how we want to set ourselves up to go faster, right? So getting those… that process clearly identified, right down somewhere in the repo, because if we can go faster, what are the steps that we need to do there? Do we need to, you know, create that separate repo? Like, how do we get to that point of going fast? Then we can figure out, you know, what instrument… where to focus for our instrumentation coverage. The one other thing that I wanted to bring up with this group was, how do we decide, sort of, what is our leading priorities, right? Are we interested in, sort of, documenting, like, these are the top X number of use cases that we're looking at right now, not to say that other use cases aren't important, but, like, if we're trying to fill those semantic convention gaps, like, do we want to document those use cases so that we can hang those semantic conventions off of those?
So that we have a clear, you know.
prioritization path, and then we can sort of batch up things in the backlog, and sort of treat those as sort of, follow-on chunks of work. But, basically.
I think the idea that we were proposing was, you know, sort of outline our process improvement, what are the things that we need to do go faster, fill in, you know, what we think are the necessary instrumentation gaps, and then sort of, being able to triage the, you know, agent, multi-agent, you know, conversations that we have there.
And, let me see, and… and sort of any other sort of, inference… inference gaps that we might be… might be, interested in filling. But figuring out how we can go fast was sort of our… Our sort of, primary, primary goal.
Liudmila Molkova 00:23:55 And by the way, I'm hearing this is… Let's put it P0, Priority Zero, or… Because if increasing instrumentation coverage at the snail's pace, it would not help anyone, right?
Wolfgang Therrien 00:24:18 But yeah, I think that was, that was sort of, like, how we wanted to set the stage, and I'm not quite sure where to… how to… how to take the conversation to the next step, Luke Milla, so if you, what… what… where do we go from here? How do we, you know, reach a consensus in this group?
And what we should be doing next.
Liudmila Molkova 00:24:38 Yeah.
I think… Yeah… Pushed upon something.
We kind of lack focus.
Because we talk about all those different things.
Wolfgang Therrien 00:24:53 Yep.
Liudmila Molkova 00:24:53 And, there is a foundation that's… Like, a good, good set of practices that allow us to do… Instrumentations, and fill the important gaps in conventions.
So, at least in my mind, these are the two most important things.
And everything… they call the new features or a cherry on the top, but I'm curious what other people think.
Aaron Abbott 00:25:27 Yeah, I think I agree, like, the instrumentation coverage is… Is my biggest concern right now, like, We put a lot of effort into… inference conventions last year, and we only have kind of, like, a handful of providers, which Which is not terrible, and… Yeah, I think… The multi-agent conventions, like, we should focus on parity, because if we want to kind of have convergence, we should just Maybe pull that stuff in, so… In terms of whatever, like, you know, some of this extra stuff that we have here, if it's… If it's not contributing to parity, maybe we can push it out a little bit. What do you think?
Alolita Sharma 00:26:17 Toria.
Liudmila Molkova 00:26:17 to react!
Alolita Sharma 00:26:18 Did you want to go first?
Surya Teja 00:26:21 Yeah. Oh, sorry, can I go, or…
Alolita Sharma 00:26:25 Go ahead, go ahead.
Surya Teja 00:26:26 Yeah, so the question is, do we have an understanding of what all libraries are we going to support? Say, Anthropic, OpenAI, Cohere, and those? Do you have a list of those, or we are going to support whatever the community is asking for?
Liudmila Molkova 00:26:46 I think… we need to find means to have comparable coverage, because we want people to contribute to Autel, rather than… or… and use Autel rather than other libraries, and yeah, but it's a great question, which… which… What are the most important ones?
Surya Teja 00:27:04 Yeah.
Yeah, I mean, if you need help in compiling a list, I can take a look and shop.
prepare a document comparing what we have in OpenLelementary, LangFuse, and Langchain, because those are the currently used ones, if the SIG is fine with it.
But I would probably defer to SIG on what the path they want to go ahead and, guidelines they want to suggest on this one.
Alolita Sharma 00:27:34 Yeah, I mean, I agree with that. That's a good idea.
Wolfgang Therrien 00:27:40 I think both, like, on the, like, the framework access and sort of, like, the target language access, right? Because a lot of those also have multiple, like, language bindings, right?
Alolita Sharma 00:27:51 Yeah, but, I, I think, to… Aaron's point, instrument, instrumentation coverage is very important from an end-user perspective, and… and really, you know, kind of, having a instrumentation, API available from OpenTelemetry directly, to Lyudmilla's point, because there's just too much fragmentation in the implementations You know, and it's just very difficult for end users otherwise. So I think, Surya, to your point, having a list of gaps.
For even the libraries you suggested would be super helpful to begin with.
Surya Teja 00:28:39 Sorry for cutting you, but I saw in the chat that Aaron has mentioned a good point. Trask already has something of that kind in his stuff. Maybe we can use that and.
Alolita Sharma 00:28:50 Yes, yes, absolutely.
Surya Teja 00:28:51 Yeah.
Alolita Sharma 00:28:52 Nice list, actually. Yeah.
Liudmila Molkova 00:29:02 Sorry.
Oh.
I'm never in the right place here. It's per library, or is it per… we should have per library thing, right?
Alolita Sharma 00:29:22 Yeah, it's okay, J.
Aaron Abbott 00:29:22 Endall.
Alolita Sharma 00:29:24 Yeah.
Trask Stalnaker 00:29:29 At the top, there's a… oh yeah, go ahead, you're good.
If you, as Aaron was suggesting, expand all at the top. There's a.
Liudmila Molkova 00:29:38 It's beautiful.
Trask Stalnaker 00:29:38 button.
Liudmila Molkova 00:29:40 Right.
Surya Teja 00:29:46 ask one small question. I believe this covers all the libraries, like Langchain, LangFuse, and Opal Elementary, and it does not need any Any additional library that needs… that has to be added to this.
Trask Stalnaker 00:30:01 Likely. Likely, yes. I'm not positive.
I tried to basically pull in and test any of the instrumentations that I could find.
Surya Teja 00:30:20 Yeah, cool, I'll sync up with you offline. Thanks a lot.
Trask Stalnaker 00:30:23 Fantastic.
Liudmila Molkova 00:30:30 Whoa. And I think with all the automation we have, Where's the checks, and conformance testing.
this AI. We could… Do this pretty fast.
We don't need to spend time on individual instrumentations, we could do it in bulk.
the tricky part that I think we can, We need to figure out how to resolve, is that, okay, we have this, all these beautiful libraries in the industry.
And in theory, we can convert them.
how can we do this ethically, in the way that we don't just take somebody else's open source and convert it to Auto? So, if you own these libraries, if you're interested in collaboration.
I'll be happy to work with you to take your libraries and make them an hotel, if it's something that you could consider.
Alolita Sharma 00:31:33 Yeah, I think ideally, Ludwilla, you're absolutely right, because again, it's a collaboration, and, you know, the implementations that already exist should just converge onto the project.
And…
Dat Ngo 00:31:46 And Ludman, anything for open inference, just, yeah, pull us in.
Trask Stalnaker 00:31:53 -Oh.
Liudmila Molkova 00:31:53 Can you… can we pull you in?
Alolita Sharma 00:31:55 Yes.
Liudmila Molkova 00:31:56 And you're like, person?
Dat Ngo 00:32:00 Yeah, absolutely.
Liudmila Molkova 00:32:04 Okay, let's talk about it.
Trask Stalnaker 00:32:06 Yeah, yeah.
Dat Ngo 00:32:06 Give them black. Let's do it.
Trask Stalnaker 00:32:09 Yeah.
Liudmila Molkova 00:32:15 Yeah.
Okay.
We're… we're carried off.
carried away, but I think it's a good, good stuff, What should we do in the context of the… The roadmap, yeah, Erin?
Aaron Abbott 00:32:39 Hey, maybe before we move on, I don't know if you were planning to move on, but I was gonna ask if we could discuss the, major release cadence a little bit. There was some discussion in chat.
And I wanted to make sure that we, Maybe gather feedback from everybody?
Or did… I don't know, Lumila, where were you going?
Liudmila Molkova 00:33:00 No, like, exactly this, like, what, I… it's not the roadmap that I want everybody to sign with Black, unless we have a good discussion.
So, if the cadence is something we need to discuss, let's discuss it. Maybe we should time box things to maybe 5 more minutes, and then this comment is public. You can comment, we can, like, do as much as possible offline, and then next week we can think again on any big discussions that come, come, come up.
But yeah, the release cadence, I think the discussions in chat that we need something for major.
Maybe faster than regular hotel.
Aaron Abbott 00:33:40 Yeah, I think… Can we… excuse me, like, this is mainly… to be clear, this is… is this focusing on the semantic conventions, or is this focusing on the GenAI libraries? Because I think for the… for the libraries, I have no concern with that.
For the semantic conventions, I… I don't know, I just want to validate that that works for everybody, like, teams building UIs and stuff like that. I… I'm just doing instrumentation. It's easy for me to, you know, suggest breaking stuff, but I don't know what goes into, You know, like, evals and dashboards and stuff like that, if all this stuff is built on our semantic conventions, and then we want to have a pretty fast Major version release cadence.
Any thoughts?
Alolita Sharma 00:34:27 I think, Aaron, having a monthly cadence on semantic conventions would be useful, even if they are, you know, in progress, because that helps in aligning even the minor releases, from an instrumentation perspective to keep moving.
Aaron Abbott 00:34:47 Yeah, yeah. Makes sense. No concerns at all for me on the minor releases.
Trask Stalnaker 00:34:54 So, at what… yeah, I think the idea of the major… SEMCON releases are that you would have instrumentations well, at least the way we've used majors in other SEMCOMs is… We'll have, like, a de facto stable.
Which was, like, say, the old database semantic conventions.
And instrumentation's kind of pinned to that.
Wolfgang Therrien 00:35:30 And then…
Trask Stalnaker 00:35:31 M… We work towards, you know, we bring a lot of breaking changes in, we make a new major release for semantic conventions, and instrumentations bump from kind of the old de facto stable, old stable to new stable.
And the… Idea there being that we minimize the exposure of all the intermediary breaking changes to end users.
What I don't know is if that model works well right now, today, in Gen AI world.
Will… in… will instrumentations… Do instrumentations?
Will they stay on a major… a stable major version, like an LTS kind of version?
And… wait.
Or will they just want to keep rolling with the latest changes, given that We just keep, you know, there's so much new stuff coming in constantly.
And what if some of that stuff is breaking?
Yeah.
So that… I don't have any answers, so I just wanted to sort of lay the problem out there as far as what we've done before and why that may or may not apply in this group now.
Aaron Abbott 00:37:10 Yeah, yeah, that sounds good. I think maybe we can validate, like, the… the need also a little bit to justify the complexity.
Alolita Sharma 00:37:20 I would also suggest, kind of calling out the stability guarantees of these, minor and major instrumentation library, releases, because it's evolving, right? So again, as Trask said, there will be some breaking changes, there will be some changes, you know, as we go along.
Trask Stalnaker 00:37:49 I guess I… I would like to throw out the, the… like, I'd li- As a vendor, like, who, like, as you say, doing dashboards, like, the biggest problem that we're seeing today is the proliferation of so many different instrumentations, emitting so many different semantic conventions.
And… Even once we get… let's say we don't have all these different instrumentations out there, but even within OpenTelemetry, Contrib, say we have lots of different versions of semantic conventions, of people emitting them, that's still… a challenge. Like, it's still nice to kind of have these… my landmark… versions that are… The stable ones that we… You know, encourage people to use.
And that's where, you know, I think we threw out the 6 to 12 months.
Initially, 6 months does feel very fast.
For a major version.
But… Also, maybe not. I mean, maybe that gives us… You know, then people aren't having to wait more than 6 months to kind of get all the new semantic convention stuff that we've kind of worked through in the meantime.
Alolita Sharma 00:39:22 Yeah, I agree with you, Trask, because I think, 6 months is a decent clip. If we see that we're not, you know, there are some gaps.
You can always adjust.
Trask Stalnaker 00:39:35 Booking.
Wolfgang Therrien 00:39:36 Yeah, I… I'm curious if we think, like, 6 months, like, might be… might be too long, right? Like, we are seeing the definitions of these telemetry shapes evolve so, so rapidly, and 6 months in a product lifecycle is forever. Like, we see, you know, now we're seeing products, like, erupt overnight, and, like, you know, and they'll be dead in 2 months, right? Like, and so, is there any harm in saying, like, okay, major versions come every quarter, you know, and if you're not ready to absorb that… the cost of updating to that new major version, you can stay on the last major version. But that also gives us the opportunity to say… to keep up with the pace of these evolving telemetry shapes as… as the… this area evolves, right? I'm like, I'm… I kind of feel like 6 months is too… too long.
Alolita Sharma 00:40:30 But, I mean, you have minor versions in the interim, and also, those could be used for that specific purpose of CAC, because, at the end of the day, major versions in hotel, at least, you know, come with some stability guarantees.
Trask Stalnaker 00:40:53 The other option we have sort of in the middle there is, what we've done for even the other SEMConf major bumps is we have an opt-in in the meantime to… Emit the latest experimental version.
So that… 3 months into that 6-month cycle, you could… Opt-in. Users who want the new stuff could opt-in.
And then at the 6-month… at the major version bump, that becomes the new default.
Liudmila Molkova 00:41:39 Oh, when does it… does it help? So, like, that we would… we can ship non-breaking things.
Was May and Minor.
Wolfgang Therrien 00:41:50 Yeah, I think so. I think so. I just wanted… I just wanted to ask the question, but I think that sounds super reasonable, and, I know that we are coming up against the edge of the time box, so, we can definitely, you know, chat about it more, next week, but, but yeah.
For sure.
Liudmila Molkova 00:42:10 Awesome! So then, the document is public. Anybody can comment, I think. If you cannot leave comments, let me know, we will update the… permissions.
Alolita Sharma 00:42:23 Ludmila, I cannot comment, so I asked…
Liudmila Molkova 00:42:26 Comment.
Alolita Sharma 00:42:28 Yeah.
Yeah, thank you.
Liudmila Molkova 00:42:34 Cool.
Let's discuss offline, and we'll get back to it next time.
Put it here so it don't forget.
this was my topic from the past, I'm not going to… I'm going to bring it up at pregnancy, let's not do it here. Redeema, We've been postponing this from the last time, let's… I could.
Ridhima Satam 00:43:09 Yes, so the second issue is related to the workflow name, so it could be similar, it's just that we have to discuss on the propagation mechanism what we want.
Just to green mine. In the agent name?
We are trying to say that, to add agent name to the child span, so propagate it to different, child spans, like, execution tools, or exit tools, or, LLM spans, so that we know what's the logical agent for that, and similarly for the workflow.
Yeah, I mean, I opened two issues, and I would have opened one single issue for both.
Liudmila Molkova 00:44:00 Yeah, I think there are two questions. The first one, do we do this? The second one is how.
Ridhima Satam 00:44:07 Neal.
Liudmila Molkova 00:44:07 And for the second one, there is something generic that hopefully is coming through the hotel specification.
It might take a bit.
But I think we should discuss here.
whether we should do it. And I think there are other similar proposals we heard from Alibaba folks. They joined up a call Maybe a week ago, and they are also interested in something very similar.
I kind of want to learn if… if people… what people think about it. It's a little bit, redundant, because you can, in theory, join things together, and you can, like, join telemetry, and from… by joining telemetry, you can find out what is the workflow name that this chat operation applies to.
But it's… Expensive, and that doesn't allow you to do metrics nicely.
Erin?
Aaron Abbott 00:45:06 Yeah, I mean, I'm guessing you're getting at the context scoped attributes, right?
Liudmila Molkova 00:45:10 Right, yeah.
Aaron Abbott 00:45:12 Yeah, so my understanding of the direction of that one was that we said there wouldn't be any, like, instrumentation-specific component At least in the initial OTEP, so maybe we'll tackle it later, but… So I guess my question is, the user would have to opt in in the current model with that. But I think, you know, the context of that specific OTEP aside, like.
do we think that's the best practice? Because if… if we think it's noisy, we can just let people opt in, right?
Liudmila Molkova 00:45:45 Yeah, I think for the context scope attributes, the ATAP is open.
And this is a good time to influence the direction. If we think we should do it in Gen AI, we would just go and push for this for that app.
Aaron Abbott 00:46:03 Yeah, and I mean, I think we could prototype it as… the implementation of this, too. It'll probably be helpful for the OTEB.
Ridhima Satam 00:46:11 So, quick thing here, for the OTEP is mostly because we need some attributes which do not cross the boundaries, right? That's what the OTEP is about.
I just added a PR… sorry, a POC where we can use the baggage for this, but in that case, we obviously cross the boundaries there. So, we have to decide here, like, what do we want, like, or do we have, like, an opt-in where it is okay to have it on baggage, or… That OTIP, the context scope value attributes.
Liudmila Molkova 00:46:47 From the use case, do we need it to cross the boundary?
process boundary.
I hope we don't, but…
Ridhima Satam 00:46:59 Yeah, so, yeah, I just tried one POC with, like, there's an MCP tool which is calling, a remote agent, so with that.
If you pass the workflow name there, you can… attribute that, like, add that agent spans and the following child spans in that single workflow or CHAB.
Like, a top-level agent for that.
Liudmila Molkova 00:47:27 This is the argument for… Passing it across service boundary, right?
Ridhima Satam 00:47:33 Yeah.
Yeah, but in some cases, say, if we are saying that maybe agent name is, like, a secret agent or something, if you don't want to do that, then do we have to have another opt-in? Like, even if it's on baggage, just drop it, and in that case, I think the context scope attributes work.
Trask Stalnaker 00:48:00 And back to Lyd Miller's question of, Is this… Because of a limitation on the back end, of not being able to join the downstream spans together with the upstream spans to get the agent name.
Or is this specifically… Due to the metric, the problem of, you know, I mean, if you want it on the downstream metrics, that's a different… problem. You can't get that through just joining.
Ridhima Satam 00:48:35 Yes, so right now in the pro… in the issue, like, at least the proposal, we are asking for both span and a metric.
Yeah, just because, span is, like, just, you know that the span has some logical agent.
directly without having so many expensive operation for that. And, yeah, metric is, like you said, right, we can aggregate on a single agent and see.
Trask Stalnaker 00:49:04 Yeah, we don't have… in OpenTelemetry, kind of broadly and historically, we have not… we haven't done this. We have… not automatically propagated things. We haven't kind of denormalized things in this way. We've kind of kept it… said that, okay, if you want to know what database calls were for this particular HTTP route.
You know, you have to join that on the back end. You haven't provided any propagation down.
But it does seem like this is coming up a lot in the GenAI space, and so I think that's where, Linmila and I are both trying to figure out the right balance here, between what we have. We just don't have any… prior art in OpenTelemetry, I think, for doing this. But… And so we need to put together kind of a really strong reason and case for… Going against the prior art.
Yeah, Benjamin.
Benjamin Kawecki 00:50:24 trying to share, because we… we just tackled this internally, and it raised some interesting things. Obviously.
we have a lot more control of our own internal ecosystem, but there were some interesting challenges that arose. The first was, it kind of started as someone maybe owns a sub-agent.
That's called by a primary agent, and that sub-agent may call tools, and that sub-agent may get invoked multiple times in the same trace, and they want to be able to easily aggregate, like, you know, how many tool calls did I did on a per individual call basis. So, you know, for the first request to my sub-agent, maybe I called 20 tools, second request, I called 2.
But this very quickly became a problem where now the top agent also wants to set this as well, and so how do you make sure that The… they're not stepping on the same attribute key.
Became a pretty big issue, because then… yeah. So, those were kind of some of the problems that we ran into. It started to get into discussion of, like, maybe we add some, like, key namespacing with the service name, and it got really complicated, but… Yeah, but then the main agent also could be a sub-agent, so it goes kind of… It's turtles all the way up.
Alolita Sharma 00:51:37 I mean, Benjamin, to your point, I think, having namespaces is definitely useful, because, it, you know, just limits the blast radius of these attributes, you know, kind of, Being used in different directions, or for, you know, different contexts, until we can get to the point here in the… In this work group, To establish, you know, some common naming conventions, as well as, Just categories.
just… it just avoids the exact issue that you called out. We see that a lot, too, where there's just a lot of stepping over each other.
Benjamin Kawecki 00:52:23 Yes.
Yeah, but then it becomes hard to normalize these…
Alolita Sharma 00:52:27 Yes.
Benjamin Kawecki 00:52:28 Exactly. So it's, exactly.
The two competing forces.
Alolita Sharma 00:52:32 Yep.
Liudmila Molkova 00:52:34 Would… Redima, for the sake of time, would it be reasonable for your backend? You work at Splunk, right? At Cisco?
Ridhima Satam 00:52:42 Yes, Dan.
Liudmila Molkova 00:52:43 Is it possible to infer this?
At query time, and, like, at visualization time. It might not be efficient. It might be hard.
But is it someplace we can start?
I feel like we're talking about, okay, we need a better visualizations and different approach than just this tree Gantt chart for tracing.
And we just… it's just a bigger problem to solve than… Okay, let's just stamp the agent name on everything under.
And, like, okay, it feels like we need to understand why you… what we want to achieve with it.
And maybe if we just do something slightly inefficient on the backend for now, over time, we will figure out what we need for sure.
Ridhima Satam 00:53:34 Okay, but then what about the metrics? Like, what do you think about the metrics on anyone here?
Liudmila Molkova 00:53:41 We would re-aggregate the spans, into metrics.
At the later point. Like, I'm… here, I'm not saying we must do this, I'm… I'm saying… Can we start here?
Alolita Sharma 00:53:56 Yeah, I agree with Mila, because we could pull out span metrics, right? So, again, I think that starting from traces is important.
Ridhima Satam 00:54:08 Okay, sounds good.
Aaron Abbott 00:54:09 We do have metrics, though, right? Like, we have… Similar to take inventions for metrics, I think the context scoped attributes would be a good way to push down The agent name, right?
Liudmila Molkova 00:54:23 Yeah, it would take a while, though, to context cop attributes to Materialize, and by that time, we probably will know better how to use it, if we start experimenting with What we can do on the backend.
Like, somebody would need to… Either rebuild this metric, or have another one to include Agent.
Name and workflow name.
Aaron Abbott 00:54:53 Okay.
Trask Stalnaker 00:54:55 I'm… yeah, I mean, I… I'm interested in… using… I mean, Continuing this discussion in the context of… context, like, trying to play out what this would look like.
I agree that, you know, it… Redima, it… it will be multiple months before we have something there, so I think Lydmilla is giving you, sort of, the… if you need a solution today.
That's, I think, the only solution you're gonna get is sort of re-aggregating spans to metrics in the pipeline or back end.
But I have seen this come up, enough, Stamping both agent down, and even this idea of the main agent, stamping that down onto, spans and metrics.
That… it feels like a… an opportunity with the new context scoped attribute, OTEP.
to, Kind of bring that use case out, and… Talk through that more and prototype that.
Ridhima Satam 00:56:15 Yeah, so currently at Splunk, we are… we have some implementation of, this in the GenAI utils, like the Splunk side JNA utils, where we are actually using context for, stack, and… We do that, in that way, to identify which was the parent agent.
So, yeah, in some way, we are having implementation for that, and we are stamping, actually, the agent name or the workflow name on the spans.
So we have a solution, it's just that we want to then align it with the upstream and… See how it goes there, yeah.
Trask Stalnaker 00:56:52 Yeah, we, we're, we have a similar thing, that we're doing of, Stamping, taking span attributes in span processors, reading the… basically automatically stamping, parent span attributes for agent and… and main agent down into sub-spans, So yeah, I feel like there's a bunch of people here probably doing something similar there, and I would love to see us figure out how to Take advantage of context, scope, attributes, or steer that in a conformant direction.
Liudmila Molkova 00:57:34 Okay, so it sounds like the next steps here would be that we would, I took an action item to comment on the context scope attributes that we want to use in instrumentations.
At least we want to explore this option, and we see a lot of use cases for it in GenAI.
The… this would be the good… long-term solution, and I… I don't want to explore other solutions in the… While we are waiting for this one.
what other people think. Should we explore any hockey?
Ways to achieve it in the meantime.
Given we already have them, we have spent present.
Trask Stalnaker 00:58:20 So…
Liudmila Molkova 00:58:20 We have,
Trask Stalnaker 00:58:21 I think we should use it… use this as an opportunity to prototype And steer the… the OTEP.
Liudmila Molkova 00:58:36 And I would be hesitant to put things in semantic conventions until we… Like, clear the pus.
For the context sculpt attributes.
Ridhima Satam 00:58:47 So, we are not considering baggage here for now.
We just want to focus on context, scope attributes.
Liudmila Molkova 00:58:58 Good question. So, my concern's about baggage, because you… the moment you put something in the baggage, you cannot stop propagating it. It will leak everywhere.
Alolita Sharma 00:59:06 Yeah, exactly.
Ridhima Satam 00:59:09 I see.
Sophie, we want to first go with the context, right?
Scope attributes, and then see… If we can enhance it where we want.
to have it on the baggage. We want to tackle that later.
Trask Stalnaker 00:59:29 Yeah, I think baggage is gonna have to be a much more strongly opt-in thing, That… I'm… yeah, I would… Focus on the… the in-process.
Peace.
potentially context, scoped attributes, I mean, that would be an interesting addition to the, you know, to discuss on the OTEP, if there's a… You know, if there could be a configuration option for users to specify certain context scope attributes that they want to end up in baggage.
To give the users that control.
Liudmila Molkova 01:00:37 We have 3 minutes left. I don't think we can achieve anything meaningful And this… Time?
We… probably should take things offline.
Let's see if we have some… trivial PRs, or, like, some non-controversial things can… people can review.
okay, so I see 3 PRs that are probably… Close to the… Merging… And let's take a quick look at them.
Somehow it's not in the Gen AI.
And it's a great PR to have time to… Sorry, to cover the gaps we had in the streaming. Please take another look, I think there are some comments.
Or maybe they're resolved, but if we have another approval, it should be ready to go.
We talked about memory, I think there are some open discussions. Maybe Trask, Nakumar, we can just, I don't know, sync in Slack.
Sorry, we've been postponed.
nagkumar 01:02:03 Mine.
Liudmila Molkova 01:02:03 Two weeks straight.
nagkumar 01:02:05 No worries. I just posted here, so if anyone else wants to take a look, Please do.
Liudmila Molkova 01:02:12 Yeah, thank you. And for the workflow duration, I think it's in, good shape, but there were some comments I, I… I'll take another look, Radhima, thank you.
Cool. Then… Great discussion. Please make sure to review the… Roadmap.
And we'll talk about it next time again. Thank you.
Aaron Abbott 01:02:46 Awesome.
Alolita Sharma 01:02:46 Thank you, thank you, thank you.
Trask Stalnaker 01:02:49 I…
Alolita Sharma 01:02:49 bye.
