SIG: Java SIG
Date: 2026-03-12
Duration: 29 minutes
============================================================

## Zoom Recording Transcript

**Trask Stalnaker** 01:27 Hey, folks!
**John Watson** 01:36 Good morning from wet, wet Portland.
You see we have, like, over 2 inches forecast for tomorrow?
**Trask Stalnaker** 01:50 I'm, very interested to check out. There's a road near us that has been flooding, like, all, like.
all winter. Even though it's been dry, like, it just has… there's a stream that goes across it, and it's very marshy, but, like, the stream has somehow, this last year, diverged, and so it's not going through its normal path.
And so it's just been, like, completely flooding this road. And they've been, like, doing all these, like.
Little, tiny, trying to fix it. And finally, they just built this… dug this huge trench along the side of the road to divert it back to original location.
But I haven't seen it, with a big downpour since they did that, so I'm… Very intrigued by civil engineering projects.
**John Watson** 02:48 Yeah.
**Jack Berg** 02:50 Yeah, I was a civil engineer.
**John Watson** 02:52 Oh, cool.
**Trask Stalnaker** 02:52 Yes.
**Jack Berg** 02:54 Long time ago, in a galaxy far, far away.
**Trask Stalnaker** 02:57 Jack, why did you get into… Why did you get into this?
**Jack Berg** 03:03 I don't know, like, I think about that sometimes, but, like, the benefit of getting into this is, like, civil engineers just get, like, dragged around the world and the country for all their projects. Like, I feel like if I didn't… if I stayed with civil engineering, I would just be dragged around to all the data center projects.
People that I know are all wrapped up in that, so maybe all roads lead to this anyways.
**Trask Stalnaker** 03:29 Fair, fair.
**John Watson** 03:31 Hey, my daughter just got accepted to an environmental resource engineering program that she may end up going to, which is pretty cool.
**Trask Stalnaker** 03:37 Bye!
**Jack Berg** 03:38 Cool.
**Trask Stalnaker** 03:41 Yes, I have a… daughter, who is currently, like, waiting for… I think tomorrow is the day that a bunch of colleges release.
**Jack Berg** 03:57 Release acceptance, or, or, like, deny? Yeah. Yeah, oh, man. Sounds stressful.
**Trask Stalnaker** 04:17 Alright, well, that's… Do our agenda, and maybe… Get some time back.
The instrumentation release, IO, I don't think there's any PRs, really, that… Oh, I think we might have tagged one or two, that are approved, I will.
Yeah, I think that one is… I think it's ready to be merged.
Or was there a question for… oh yeah, yeah, I think we're good. Yep, I will merge that.
Anyone else has anything they particularly want in there, speak up.
Cool, Jack.
**Jack Berg** 05:21 Has somebody opened a PR to, the core repo, adding an agents.md file, and since Agents.md have been suggested. There's this thought in my back… in the back of my head about, like, what's the difference between that and contributing.md?
And, like, you know, if we're gonna have… thoughts like, hey, if we're gonna take effort to have, like, a sanitized, well-tuned agents.md, we better spend effort first to have a good contributing.md, because, like, I'll be damned if we prioritize the machines over humans.
And so this thought, like, occurred to me, like, what about…
**Trask Stalnaker** 06:02 Humans are using the machines.
**Jack Berg** 06:04 Yeah, yeah, I know, I know, like, yeah.
That's, that's, that's the…
**Trask Stalnaker** 06:12 The question is… the question in my mind is, is anybody gonna read contributing Read these documents in the future.
Versus just have your… Agent, read them and conform.
**Jack Berg** 06:30 Yeah, well, I do want to be able to have artifacts that I can point to people of for, you know, questions of what's idiomatic in this repository, decisions that have been made previously. Like, you know, there's this there's this issue I just opened about, like, hey, what is our stance on verifying non- null ness of parameters?
despite the fact that we use Null Away and the null able annotations. Like, so, you know, at build time, we can verify that none of our tests or, you know, our APIs, you know.
use null params, or expect non- null arguments where they're not allowed, but, you know, there's nothing ensuring that people don't call our APIs with null parameters. So, like, when is it appropriate to explicitly check those? And, like, how do you explicitly check those? What does that mean? Do you throw an exception? Do you, Do you log an error? Do you, just silently do a no-op? Like, and that's the type of decision I want to have, like, codified somewhere, and point users to, point agents to.
So, yeah, like, even if… even if… there's no user reading it, I want a link in the PR to say, hey, your agent or you didn't do this, and here's why you need to do this.
An index of decisions.
**Trask Stalnaker** 07:59 I like the style guide, file for that.
What is… do you not have…
**Jack Berg** 08:11 I think we have it as a part of contributing.md.
The style guide, yeah.
And so, the question in my head is, like, and I kind of want to lean on some more of the AI experts out there, but, like, you know, what's the difference between a contributing MD and agents.md? Like, the first thing that comes to my mind is, like, verbosity, level of detail. Like, if they're going to read this.
At the beginning of every conversation, like.
To what extent should we, you know, be protective about contacts?
Or, like, what's too long, essentially? And when should you sort of, like, split out?
**Trask Stalnaker** 08:58 This is too long.
In my opinion. Like, what I like is, Giving enough, here, I did some… Work recently in, So I've been working on… Building, sort of, a code review agent in the instrumentation repo that will… Basically, know about all of these kind of conventions.
I like… I do like the style. We have a separate style guide, and it does link out to that. It tells the agent to go read that.
But it… Tells it, you sort of have basic things In the foundation, but then you tell it where to go when it needs to do certain things, so that in its initial context, it's just got something small, but it knows Oh, if I'm doing X, then I'll go read this.
**Jack Berg** 10:11 That… that's where… that's where, that was the counterargument in my head of just, like, a simple sim link, was… would be that, is like, you know, the agents prefer sort of a hub-and-spoke type model, where you have, like.
high-level information, and then, you know, links to how to get more detailed information about different topics. And that's the difference between AgentsMD and Contributing.MD, like, where ContributingMD is just, like, one big monolithic dumping ground for all the info.
**Trask Stalnaker** 10:45 So what I've done over here for this is, So, like, there's just a bunch of, kind of, random conventions and patterns that we follow in the instrumentation repo, so I've created these, kind of, knowledge articles that And then, like, there's a table of contents where It'll read this, and then it knows, oh, if I'm doing something with Byte Buddy Advice, I better go read this document.
**Jack Berg** 11:15 Nice.
**Trask Stalnaker** 11:16 It's… there is still a line between, like, the… I do like the style guide.
Document still for… as, like, a human-readable, like… These are the… R… re… these are the… I don't know, like, traditional style guide. Like, I don't want to flood all of these things, like, there's so many patterns we have in the instrumentation repo.
I'm not sure I really want to document them.
all in the style guide as human-readable, that we even need that? Like, as long as the agents know it, and our code review agent will flag that.
**Jack Berg** 12:05 Yeah.
**Trask Stalnaker** 12:06 But something like what you were describing of the null able pattern, like, that feels very style-guide-y to me.
**Jack Berg** 12:15 I just wonder if all these things are things that you would want a human contributor to know, and it's just that… we… We're, like, trying to be protective of the humans and shield them from having to know all the information at once, because it would be overwhelming.
But, like, when it comes time for them to open a PR, you know, we expect them to follow these, and we're gonna be slowly… adding comments to this effect on the PR until it reflects all of these conventions.
So… Are we better off just… Coming up with, like, an index of these… These bits of knowledge, these patterns, these idioms, whatever you want to call them, and have them tailored to, you know, they're consumable by, like, humans and machines alike.
I actually, like, think that most of the time that you come up with, like, a document or a skill or something, or, like, an agents.md, something that's optimized for a machine. It tends to… it tends to be, like.
kind of what I would want to consume as a human as well, like bulleted lists, tables, you know, good org… good information organization, and so… Maybe a few too many extra examples, that are making a bit verbose, but…
**Trask Stalnaker** 13:50 Yeah, I guess I, as a contributor, like, if I was coming into a repository.
Man, this is a lot to read.
Through.
And that's where, like, I feel… I'm thinking that the… you know, Targeting the agents.
Has, like, specifically has… A lot of benefit, because… people are probably going to use the agent to write the code. If not, that's okay, but more importantly, then, we can have a code review agent that automatically flags all of those things right away on PRs, so they get that fast feedback of things.
**Jack Shirazi** 14:39 Yeah. Just to be clear, the flow now is… I'll write the code, and then I'll tell the agent to look at this document and make the code satisfy all the criteria here. I won't actually read the document, the agent will.
**Trask Stalnaker** 14:55 Yeah, and you can use this agent, Jack. So there's one that… it's a code review, but they share most of the content, they're just slightly different. This one actually instructs the agent to go and fix the problems that it can, and it'll tell you about the ones that it can't.
What do we end up with over… Here…
**Jack Berg** 15:43 This person, right now, the current state of this is to have, like, an agent's MD, which links out to contributing.md, but, also sort of, like, elaborates or has, like, a more terse description for agents, so kind of what we're talking about, and… I think… I think the core repo is gonna have to just, like, evolve towards something like what you've done with the instrumentation repo.
And, it'll be hard for… This to happen without, like… You know, it having this support, or, like, being led by the maintainers and approvers, so… Yeah, maybe I should just get my act together.
**Trask Stalnaker** 16:25 We'll wait till, this is still very mid-flight.
this work.
I'm actually going to… I have, a PR here… So, I've been running this code review and fix locally against, like, module by module in the instrumentation repo, just to see what it produces, to basically test it, make sure it's not doing stupid things, which, of course.
It did lots of stupid things.
And so this is a GitHub action that will… It's gonna go, instrument… just in the instrumentation modules, but we have 500 of them, one by one, and send, see what it reviews and can fix, and send a PR for it.
Throttling… throttling to, like, I don't know, max 10 open PRs at a time or something.
But yeah, once… once we kind of figure it out here, then, yeah, I… Be very interested in… Helping out in the core repo for something similar.
**Jack Berg** 17:42 Just, I'm just thinking about the projects that used to… we used to do, where we'd have, like, a tracking issue to, you know, track all 100 or 200 instrumentation modules as we needed to, like, apply some change and go through them.
This, like, sort of the unlock here is pretty awesome.
**Trask Stalnaker** 18:14 So the current or small local margin, you mentioned generated outputs…
**John Watson** 18:23 I don't understand the point of that mention-generated outputs. Like, what's… what are they trying to accomplish with that?
**Jack Berg** 18:33 I think an AI probably generated this agents.md, so I'm not sure they'll have an explanation for it.
**Trask Stalnaker** 18:42 But this is nice.
I mean, I would, I would hope that agents are generally looking for contributing .md files.
But it's pretty harmless, and it's short, it's small, it's very small, I wouldn't… I'm not worried about the context.
**Jack Berg** 19:03 This has always been the irony in my mind, is you're telling me that these things are smart, and .
**Trask Stalnaker** 19:09 They don't book all.
**Jack Berg** 19:10 They don't look for contributing dead MD, so… What the heck is going on there?
But I get it, there's standards, there's reasons.
It's also irony.
**Trask Stalnaker** 19:29 Cool!
Anyone have anything else they want to chat about today?
**Jack Berg** 19:36 Hey, what is, When you were browsing in the instrumentation repo, I saw that there's a tab up top called Agents.
What's that?
**Trask Stalnaker** 19:45 That's Copilot.
**Jack Berg** 19:49 I see it when I go to this repository as well, but I don't see it on the core repository.
**Trask Stalnaker** 19:55 we probably haven't turned on…
**Jack Berg** 20:02 Is that a setting that's repository level in the Terraform stuff?
**Trask Stalnaker** 20:07 No, close your eyes. No, there's nothing secret here. Copilot… coding agent… Selected repositories… Java?
Search.
**Jack Berg** 20:28 Ugh.
Alright.
**Trask Stalnaker** 20:31 So, what that, Like, you can go here and basically say, do XYZ… run it, and it'll open a PR and try to do it.
Or you can take an issue.
**Jack Berg** 20:52 And is this a community request to add that to… to opt into those repositories?
**Trask Stalnaker** 20:58 Yep.
**Jack Berg** 20:59 Some, some maintainers.
**Trask Stalnaker** 21:01 Don't explicitly don't want it.
**Jack Berg** 21:06 Is it, like, is it bad, Is it just, like, out of process, out of form, to just, like, enable that right now, in this meeting? Given that you have permission?
Alright, just wondering.
**Trask Stalnaker** 21:20 I've done lots of…
**Jack Berg** 21:21 about the problem.
**Trask Stalnaker** 21:21 Thumbs up, thumbs down, don't care.
**John Watson** 21:24 I mean, I just will point it.
**Trask Stalnaker** 21:27 less PRs, you know?
**John Watson** 21:29 I will point at GitHub's current uptime, and the apparent.
**Trask Stalnaker** 21:34 Oof.
**John Watson** 21:35 GitHub using AI internally for everything.
**Trask Stalnaker** 21:38 Oh, yeah, yesterday was rough.
**John Watson** 21:42 Yeah, who has permission for this, by the way? Past 3 weeks have been rough, I will say.
**Trask Stalnaker** 21:49 Anybody with right permission to the repository.
**Jack Berg** 21:53 Okay.
So do you all, in instrumentation, do you have, like, some sort of, policy, convention, something, where the person who requests that the agent does something has to, shepherd, guide that PR to the point where it's ready to be reviewed by everyone else?
**Trask Stalnaker** 22:13 Yeah, so what happens is… let's… let's pull one up here.
**Jack Berg** 22:20 Like, I don't want John to be bothered or to think that he should look at the PRs that are, like, in an interim state that I've.
**Trask Stalnaker** 22:26 Yeah.
**Jack Berg** 22:27 You know, tooling around with an agent life.
**Trask Stalnaker** 22:28 So, it's gonna open them as draft.
And is going to assign the person who opened it.
And so what I usually do is… Once it's ready, then I do two things. One, I approve it, and you'll only get a gray checkmark if you were the person who submitted the co-pilot request.
So that you can't approve and merge it, your own…
**Jack Berg** 23:02 Yeah, we talked about that several weeks ago, yeah, okay, that makes sense.
**Trask Stalnaker** 23:06 And then I mark it ready for review, and that's when, other people look at it.
**Jack Berg** 23:15 I like that.
**Jay DeLuca** 23:19 Do you know when…
**Trask Stalnaker** 23:21 Oh, great.
**Jay DeLuca** 23:22 When you're, I don't know what it's called. When your code review agent is merged, will there be, like, a way to trigger that?
For a particular instrumentation, or…
**Trask Stalnaker** 23:37 That's a good question, like, can you do the… or, like…
**Jay DeLuca** 23:41 Yeah, if you can reference it there or something.
I guess we'll find out.
**Trask Stalnaker** 23:46 Yeah.
Thank goodness you can select.
your model now, because that… For a long time, you couldn't select your model, and so… These were less useful.
**Jay DeLuca** 24:05 And who pays for… The token usage and stuff in this case, is this… Included, or…
**Trask Stalnaker** 24:12 Good.
Good point. So, you also, to do this, you need your own co-pilot Subscription.
**Jack Berg** 24:22 Okay, so it's all done under, yeah, your…
**Trask Stalnaker** 24:25 your…
**Jack Berg** 24:26 contract.
**Trask Stalnaker** 24:27 your identity.
Now, this one, the, the… Code review… Oh, no, I'm not in Pure.
the… GitHub action here to iteratively go through.
That I supplied my personal access token.
To use for these.
**Jack Berg** 24:59 What… what do you mean you supplied it? Like, how did you supply it?
**Trask Stalnaker** 25:02 So, in the… I just put it in as a secret.
So, for example, because it's running Copilot CLI here.
**Jack Berg** 25:13 Oh, I see.
**Trask Stalnaker** 25:14 You have to… Sheeks.
**Jack Berg** 25:19 So this is a specific action you created to kind of kick off this workflow, and it's all gonna… all the executions of this action are done under Trask's name.
**Trask Stalnaker** 25:29 Yeah, but they're going to submit the PRs under the OpenTelemetry bot.
Name.
**Jack Berg** 25:37 In the name of Trask.
**Trask Stalnaker** 25:40 The co-pilot, not, like, the… it's only the Copilot token that's mine.
And I… my… my reasoning is then I can approve and merge those PRs under the idea that we all agreed to the code review conventions. Like, we all approved these Knowledge… articles and patterns and things, and so I'm not asking it to go do something ad hoc at this point.
**Jack Berg** 26:19 Got it.
Yeah, it would be interesting to do a pass on that same type of thing in the core repo. There's, There's, you know, all sorts of patterns that I can think of that are, inter… intermittently fouled, like things like a case of private static variables.
things like testing conventions, like, I have this pet peeve where, like, don't put the test… the word test in the method name of your test method, like… That's redundant.
Just silly things like that. Not as important, I'm sure, as, like, what's happening in instrumentation, and not at the scale of that, but… It's a cool idea.
**Trask Stalnaker** 27:03 Yeah, yeah, I mean, I think it's… I kind of like the idea of, over time, like, if, like, you see some… one of those kind of knit things, you can just throw it then into the knowledge article, and then, you know, from time to time, we can have this, you know…
**Jack Berg** 27:20 sweep.
**Trask Stalnaker** 27:21 Sweep.
And just kind of pick up anything new that it finds.
**Jack Berg** 27:27 I mean, the alternative that I could do, just, like, locally, is, just create a skill for whatever type of thing you're trying to do a sweep on, and then, you know, either just on my local machine, sweep through one module at a time with all the things I want to update, or sweep through all the modules at the same time with, like, one very specific thing to update. Like.
**Trask Stalnaker** 27:51 Yeah.
**Jack Berg** 27:51 pattern across all 20 modules, or do all the patterns across one module.
**Trask Stalnaker** 27:57 So the agents tend to work better to do one thing across all the modules.
**Jack Berg** 28:03 Okay.
**Trask Stalnaker** 28:04 Because it's a very focused task, then.
The reason why I'm specifically want to do it this way is because I want it to be a good code review agent.
And to be a good code review agent, it's gotta do all of those things on one module, or one PR.
**Jack Berg** 28:29 Yeah, and, you know, basically you're creating a nice big sample size by having it run through all of these.
**Trask Stalnaker** 28:35 Yeah.
**Jack Berg** 28:35 first.
**Trask Stalnaker** 28:36 I'm learning… I'm learning what it does well and doesn't do well, and… Yeah.
**Jack Berg** 28:41 Nice little reinforcement loop.
Thanks for sharing all this, Trask, I appreciate it.
**Trask Stalnaker** 28:49 Yeah.
Alright.
Well, let's get some time back, y'all.
**Jack Berg** 28:59 See ya.
**Trask Stalnaker** 29:00 I…
