SIG: eBPF instrumentation
Date: 2026-03-11
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Nikola Grcevski @ Grafana / OpenTelemetry** 00:36 Hey, everyone.
**Giuseppe Ognibene | Coralogix** 00:39 Hi, everyone.
**Florian Lehner** 00:42 Hello, hello.
**Tyler** 00:45 Hello. Morning. Afternoon.
**Rafael Roquetto** 00:47 Morning.
**Tyler** 00:51 How y'all doing?
**Nikola Grcevski @ Grafana / OpenTelemetry** 00:55 Yeah. You?
**Tyler** 00:57 It's still not liking this daylight savings thing.
**Nikola Grcevski @ Grafana / OpenTelemetry** 01:00 Aww.
I know.
**Tyler** 01:04 Are you guys…
**Nikola Grcevski @ Grafana / OpenTelemetry** 01:05 Europe hasn't moved, it's just us.
**Tyler** 01:07 Yeah, which is, like, messing things up as well, because, like, people are showing up, like, an hour later to meetings, and they're going, like, wait, what's going on?
**Nikola Grcevski @ Grafana / OpenTelemetry** 01:13 Yeah, exactly.
**Tyler** 01:14 Yeah.
But you, you guys haven't moved yet, Nicola?
**Nikola Grcevski @ Grafana / OpenTelemetry** 01:20 No, we have, yeah. Canada moves with the US, yeah.
**Tyler** 01:22 Okay, yeah.
Yeah, except for, Vancouver, I heard, right?
**Nikola Grcevski @ Grafana / OpenTelemetry** 01:27 Yeah, but didn't they say Washington State is doing the same thing?
the move?
**Tyler** 01:34 I hope so. Oregon… Oregon, like, passed this legislation that they wouldn't move, but only if California and Washington didn't as well. So if Washington's not doing it, then I'd be super excited about that, yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 01:49 Yeah, I think, British Columbia… It's taken the lead from… From, Washington State.
**Tyler** 01:56 Oh, okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 01:56 Clear on.
**Rafael Roquetto** 01:58 So BC's gonna stay, right, I guess, forever with Daylight Savings.
**Tyler** 02:01 Oh, that's true. Yeah, this is the last change. Well, the last change, yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 02:06 Yeah.
**Tyler** 02:07 Yeah.
Yeah, I'm, I'm ready to… to stop.
**Rafael Roquetto** 02:13 I had no idea. Like, I woke up on Sunday, and I was like, man, I woke up late today. What the hell? And then I, you know, looked at the cell phone, then I went downstairs, and I checked, like, the microwave, the clock. Okay, no, this is wrong, and then it dawned on me that it changed.
**Tyler** 02:31 Ugh… My favorite part is that it changes, and then, like, two weeks later, everyone's gonna go fly to Europe for KubeCon and be all messed up again, so it's like…
**Nikola Grcevski @ Grafana / OpenTelemetry** 02:43 Yeah.
**Tyler** 02:44 Yeah, it's a lot of fun.
Oh, well, cool. We can probably jump in here in just a second. If you haven't yet, please go ahead and add your name to the attendees list, and if you have agenda items you want to talk about, please go ahead and add them there as well. And, yeah, we'll, we'll, jump in here. Let me start sharing my screen.
Cool. Alright, so… looks like there's really only one… item, outside of doing a PR review, so far, but Raphael, you wanted to ask about, our… an AI code policy, or should we have one?
**Rafael Roquetto** 03:34 Yeah, so, like, there's more and more, like, AI being part of our lives, put it like that. And I think we are… we, not that we as OB, but everyone, like, in the world is still kind of learning how to make the best out of it. I personally use it a lot.
But there are downsides as well. Some people, like I've observed, like… Start submitting, just like, you know.
AI-generated text, AI-generated issues, AI-generated code that they don't understand themselves.
Which is problematic, because I feel like when you're, especially when you're submitting code, you gotta own it. It doesn't matter if it was written by Claude, by, you know, your bare hands, a mix of everything.
And then there's another thing that I wanted to mention, which is also… yeah, I guess Alinda maybe pretty much sums it up. I saw the, I think it was Florian who posted it, the… the guidelines. I think those guidelines make a lot of sense from… from the project.
So, I don't know what you guys think, I just thought I would bring that up.
And see if there's something that we need to do.
**Tyler** 04:59 Yeah, so just, I like the idea of addressing it. I also like AG, or, Florian's… link to the agents.md.
I actually noticed that was really cool because it, is, like, imported by default into the context, for most, like, agents that are running.
And so, like, this is pretty, pretty, you know, bare bones, like, you should… Do exactly what, Raphael, you're saying, but it also, I think, can be more in saying, like, well, we expect code to show up in this form if you do submit it, we expect it. So you can do, like, a bunch of these, like, other contributing guidelines that we already have, you can encode those as well, so… not only, I think, could it be helpful for new developers, but even existing developers using, AI, I found it to be very helpful as well.
**Marc** 05:50 Yeah, but this, AgentsMD that Royan shared, there's, like, there are guidelines for humans, so I don't know how is that very useful. That should be in contributing, but, like, there's, like… It says, the most important rule is Yeah, like, what is it, Yeah, there's, like, a guideline for humans to, like, not submit code that is AI-generated that you don't understand, but an agent always want to interpret that, so I don't know, is that very useful in this context.
**Nikola Grcevski @ Grafana / OpenTelemetry** 06:28 But maybe it's gonna interpret it. Like, if it… I mean, it does… like, agents do pretty well on extracting context from English language, so if you tell the agent, this is for humans, it would… Not auto-generate, then maybe tell the end user on the repo…
**Marc** 06:46 But if…
**Nikola Grcevski @ Grafana / OpenTelemetry** 06:47 You should actually talk to these people, rather than…
**Marc** 06:51 Yeah, but for example, she says, please ensure that implementation direction is agreed with the maintainers. Is it, like, meanwhile, your coding, it's gonna tell you, no, don't do this, or… You know what I mean? I don't know.
**Tyler** 07:05 Well, I think it's… I think it's more… I think that is interpreted as, like, one of the guidelines is it tells… the agent to not actually go out and, on the behalf of somebody else, post a comment, or to just automatically open something on behalf of somebody. So, like, I think it restricts the scope of, like, skills that it's allowed to actually, like.
implement there. But… I… Mark, I think you also bring up a good point, that, like, it does require, like, you know, people can just be like, go do my thing, and, like, yeah. So, like, there is, I think.
I think, I think, I think a yes-and policy here would be great. Like, having and contributing as well is always great. Like, this is a.
**Marc** 07:47 Oh my god.
**Tyler** 07:47 Like, we, in many places, where it's like, you know, obviously infraction of, like, rules, and just poach that and go, like, look, we're closing, this isn't following our guidelines. But yeah, I think… I think that can help in both ways, yeah.
**Florian Lehner** 08:02 Yeah, I don't want to direct into something, I just wanted to share how other projects of Otel is currently doing it, and yes, the collector is really bright, and, yeah, as already said, agents.md is usually a file that is, used by any agents out there, except for Claude, and that's why there's a Claude.md and, collector that points to agents.md.
So yeah, these are usually considered.
**Nikola Grcevski @ Grafana / OpenTelemetry** 08:37 We should probably, if we ever do this, we should probably add a remark that we should revisit this, because this space is moving so fast, and things change all the time, so any decision we make now should probably not be cast in stone, and we can revisit it.
**Rafael Roquetto** 08:54 Absolutely, I agree. I think we iterate this, I mean, I don't know about you guys, but I'm still learning what the best practices are, and what to look… watch out for. Yeah. If you guys want, I can maybe… Kickstart that doesn't mean, like Nikola's saying, set in stone or anything, or everyone is obviously welcome to amend, contribute, change. You know, I don't have a strong opinion About what needs to be written there. I just think… I know some things I personally… don't agree with, but I guess it boils down to me, ownership. Like, you're submitting code.
You own the code that you're submitting, you're able to explain it, you understand what you're doing.
And, yeah, that was… I think it was Giuseppe who shared with me some OCaml, issue where someone dumped, like, 12K lines of AI-generated code into the OCaml compiler. Yeah, it was a big deal. So, yeah. So, don't do that.
**Nikola Grcevski @ Grafana / OpenTelemetry** 10:01 I mean, this is a good opportunity, in my opinion, for us to kind of create a list of rules for those agents as well, so you can explain. Make small PRs.
make sure you consider code reuse, all these things. So if the agent actually does behave on people, and they're successful with that, why not? At the end of the day, we get good PRs that we can easily review and do this, so…
**Marc** 10:28 Yeah, I think… but I think, like, I was… I was thinking about this before, and also, like, what we discussed about this MCP for Obi, and, like, we could also, like, provide these, what is called skills, and, for example, if you… if people want to add a new protocol, or, like, and he wants to use this, like, AI-assisted code, we can have, like, a skill, for example, that is, like, adding new protocol.
And in this case, it's gonna… like, set the direction how has to be implemented, right? Like, what you said, Nicola, like, the best, like, small PRs.
where… what… what should the agent should do to investigate better the protocol? Like, it needs integration tests, it needs this amount of unit tests.
So, this, I think, is a… Kind of a good direction to steer the… Future contributions that they use agents.
**Nikola Grcevski @ Grafana / OpenTelemetry** 11:27 But do you think we need a skill, or wouldn't it just be able to… kind of, like, add a new protocol by just the fact that it can code, or do we need something special for those kind of things? I thought it was just generic.
**Marc** 11:43 Yeah, I mean, if we provide, like, guidance, for example, like, it's gonna… for people that maybe they don't have the knowledge of what they have to do.
You know already how to add a new protocol, but if there's new contributors, like, Maybe if you have these skills already prepared, that they can, like, produce better results, and they can also help us to review better, I believe.
Yep.
**Tyler** 12:15 Yeah, I think… I think we can evolve this.
I think to be honest, if, Like, Mark, if you are using a skill, or you're using some sort of, like, MCP server or something already, and it's working well for you, like, as a developer who is taking ownership, I think going back to that principle is really important.
you think that it would be useful for other people, let alone the developers, like, let's try to integrate that to the project. I do think that we want to try to enable, right.
**Marc** 12:42 Yeah, I mean, yeah, I think I haven't tried myself yet, but I think it will help a lot when you start giving, like… like, better context of what to do, and I think this kind of skills, or whatever text files are… I'm going to, like, give a direction, and… Some of these directions are, like, our learnings of how to implement different parts of the project, right?
**Tyler** 13:09 Yeah. So, for example, now there… I know that there's gonna be, like.
**Marc** 13:13 some protocols that we have to implement, so maybe I can try first write the skill and… and see if… If the agent is following those, guidelines, produce better results, and… And we can even measure how good it is if the review amount that you have to do is less than Without, you know.
**Tyler** 13:36 Yeah, I mean, I love this idea of trying to enable, both new developers and us, right? Like, I think that's really helpful. I think at the very least, what you're gonna do is produce a bunch of great documentation for people to read on what we expect.
**Marc** 13:50 Yeah.
**Tyler** 13:50 you know, as a community and as developers, so, like, I don't see it as a wasted effort at all. So yeah, I would definitely encourage that.
For Rafael's point, though, I would also probably say that, like, we do need, like.
you know, and Nicola's point that this is an evolving space, we probably need to be clear in the goals and the principles of what we want to try to accomplish in accepting these sort of, like, things and putting out guidelines. And I think that's really what we want to document. I like Rafael's suggestion that, like, you know, it's about ownership.
You know, just clicking, clicking the button and, and… sending us things you don't understand isn't helpful to us, let alone other people, so I think, like, as long as we have contributing, give some broader guidelines, and then start building the tooling like you're talking about, like.
Yeah, I think that's an evolving process, for sure, that I would really look forward to.
**Rafael Roquetto** 14:43 I can add, the things to the contributing.md.
I think I'll… I mean, you guys, obviously, feel free to give any kind of feedback. I'll probably start from, Florian's,
**Nikola Grcevski @ Grafana / OpenTelemetry** 15:00 I'm like.
**Rafael Roquetto** 15:00 Unlink, yeah, as a starting point, and we can, evolve from there.
Yeah, what are you… is it okay?
**Nikola Grcevski @ Grafana / OpenTelemetry** 15:08 Yeah?
Yeah, single girlfriend, yeah.
**Rafael Roquetto** 15:11 Yeah.
**Tyler** 15:12 Sounds great.
**Rafael Roquetto** 15:13 Correct.
Cool.
So that was my… that was it for me.
**Tyler** 15:18 Cool.
Yeah, alright, so let's… let's jump in then.
So yeah, next up, I just wanted to go through, our open PRs. We haven't done this in a while, and I just wanted to double-check on these. They're starting to… get a few of them. So, yeah, I think there's a few, draft PRs down here that I think are still in work in progress. I don't think there's probably too much to say here, I'm guessing they're probably still a work in progress, so we could probably just skip a lot of that.
Unless… maybe I'll pause here for a second.
Cool. So then, the configv2 is still a work in progress. I'm still looking at this.
I don't want to spend too much time on this, but maybe just kind of mention, It's sitting in the back of my mind, Nikola, you brought up some great points. I wanted to still look into specifically this unification around, like.
Yeah, custom samplers, that's a whole thing.
**Nikola Grcevski @ Grafana / OpenTelemetry** 16:19 I am getting a lot of feedback from the declarative config. They are asking around, like, how we want to structure this. That's also something that, we're working on, those two issues that are open there.
**Tyler** 16:28 I think that also, like, the filtering controls and how they're scoped, it's… I was… I'm trying to play around with this. I do think that there's, like, an interesting refactor that may happen here, so I'd rather, like.
it not be that parts of config are fighting with each other, and that there's a more centralized way to do things. And so I didn't want to have, like.
Certain elements try to override the… what is called the selection here, but maybe there's, like, a way we could actually have a target.
Which encapsulates the whole thing, you know, in a single, unified way. So, I'm still looking at that. It's been a while, yeah, I guess it's been 2 weeks, I'm still playing around with that in the background. But, yeah, still a work in progress.
Yeah, and I haven't forgot about it, it's just sitting there, so, yeah.
Cool. Next up is the dynamic, add or remove of the PID selection. Mike, I think I saw you on here.
**Nikola Grcevski @ Grafana / OpenTelemetry** 17:27 Yeah, I'll, review again, yeah.
**Mike Dame** 17:30 Yeah, I was just actually talking to Mario about, he left some comments too, Yeah, this is a follow-up to… I added the PID process, which is basically just a short circuit to say I want… I know the PID, I want it, I want to use OB for it. This gets a little bit more involved, doing it, you know, dynamically. So, while I'm running OB, do I… say, as Otagos, I import the OB code and call instrumenter.run. I want to be able to, like.
store that instrumenter and, through time, add and remove the pids that are running with it.
So I wanted to try to do that without, like, changing too much of the existing code and seeing where I could wire it in through the existing code, without, like, fundamentally refactoring a lot of stuff.
And I was just telling Mario, I was kind of surprised at the amount of hoops that I had to go through for that, especially with, Nicola pointed out detaching pids. I didn't even think of… I was kind of just looking at how do I update the, like, selector in the, the matcher, I think it is, so… the general approach here, that I ended up, going with is it's got this… callback function, where you can pass this option to the instrumenter when you… when you start it up, and then that'll return a reference to something that lets you add and update the PIDs.
But I had to wire that dynamic PID updating through What is it, like, the matcher to the, exact typer to… Finder, watch, like, it was a bunch of hoops through, like, I was really easy to follow it when I got to, like, the App Bali instrumenter, and then I started, kind of.
connecting through things that I didn't quite know what they were doing, just looking at trying to get it to the attacher, so, point of that tangent is that, you know, there's definitely spots that I think could be refactored a little bit more, made a little bit easier to, maintain and adapt to. But Mario also just left a bunch of good feedback on you know, this could be more of a fundamental change, or, like, its own kind of dynamic, selector type, so… I just kind of skimmed that. I'm gonna actually read it a bit more, but… Yeah, I'll push some more updates to this based on what Mario said, or anyone else that does look at it, look at the most recent comments, because there's been a couple changes, and I've pushed some changes to it, too, from the initial description here, but… Yeah, I'm working on that. This'll be really helpful to getting, us to be able to run this in Notagos, too. So, I'll have a couple more refactors and changes after that, and this has been a good intro to the codebase, too, because I'm seeing, like, exactly how things are wired through, and I think I've got some kind of fresh eyes on that.
**Nikola Grcevski @ Grafana / OpenTelemetry** 20:27 Based off, Mike.
**Mike Dame** 20:29 Yeah, oh yeah.
**Tyler** 20:31 You're, you're seeing how the sausage is made, is that…
**Nikola Grcevski @ Grafana / OpenTelemetry** 20:34 Yeah.
**Tyler** 20:34 Sorry, I guess.
**Mike Dame** 20:35 Yeah, it's… it's quite a sausage, and Yeah, you know, I've just been a maintainer here for a year, and submitting my first VRs now.
**Nikola Grcevski @ Grafana / OpenTelemetry** 20:44 That's okay. Better late than never.
**Mike Dame** 20:46 Yeah, but I really…
**Mario Macias** 20:47 I appreciate that.
**Mike Dame** 20:48 review guys, and I'm gonna keep working on this, too.
**Nikola Grcevski @ Grafana / OpenTelemetry** 20:50 Thank you.
Thank you.
**Mike Dame** 20:52 Thanks.
**Tyler** 20:54 Cool. Okay, so yeah, more to come on that one. Next up are… update PRs, which I've been fighting with a lot of these.
So, I don't know if there's too much to say. I think the Kafka ones are a little bit rougher, because I think this actually is changing how, Kafka is operating, and it takes a little bit more internal change here.
especially into this V8, upgrade is definitely, I think, a little bit more of a headache, so… I have been looking at some of these, but I haven't… dived into those as much as, like, the Java and the Go stuff right now, but, we don't have to jump in and waste a lot of people's time on this one, it's just more fighting with things, so… Yeah, so next, Nimrod, you had, allow adding HTTP headers to spans. I've seen this one, it looks like… CI's giving you some issues on this one still, but, yeah, if you want to jump in, maybe… I don't know if you're… Blocked on this one?
**Nimrod Avni** 21:51 Nicole just gave me a last couple comments, I think. I've updated them, just to… make sure we support, like, multiple values per header, and now the CI's failing the test, so I'm fixing them.
Bum… And yeah, hopefully pretty soon to be finishing this, and… hopefully I'm gonna move on to, like, body, like, HEP body extraction, which I… I can link, there's an issue on, like, proposing a new semantic convention for this, but I think we are, like, right on time on that, so… Because someone from, I think from Elastic, worked on, like, some Java instrumentation, adding it as a… As an attribute.
So I try to support that. I'll post it here.
**Nikola Grcevski @ Grafana / OpenTelemetry** 22:42 I'm pretty sure.
**Tyler** 22:43 That's Gregor, right? Yeah.
Yeah, go ahead, Nicole, sorry.
**Nikola Grcevski @ Grafana / OpenTelemetry** 22:50 Yeah, so you'd be able to kind of pick a field from, like, JSON that you want to extract? Like, something like that?
**Nimrod Avni** 22:56 I don't know if the… I don't know, like, if we want to either just extract the full JSON payload with, like, let's say we only, like, support structured data for now, like JSON, maybe XML.
**Nikola Grcevski @ Grafana / OpenTelemetry** 23:10 Or whatever, and then…
**Nimrod Avni** 23:12 Should we just take all the data and maybe have obfuscation rules on specific fields?
**Nikola Grcevski @ Grafana / OpenTelemetry** 23:18 Hmm.
**Nimrod Avni** 23:18 we can say we take only specific feet, like, I don't know exactly what… like, I think maybe it makes sense to have the full body, and just, like, obfuscate specific fields.
Because it makes sense for, I don't know, I want to replay this request So I want the full body of it.
Maybe we can have multiple features, like, one of, like, you know, we can even say, take this… take this, like, JSON path and put it in a different attribute. It doesn't even have to be the HTTP body, but if you want the full HTTP body, I guess we need some semantic… convention for now.
**Nikola Grcevski @ Grafana / OpenTelemetry** 23:56 Wow, that's pretty cool.
**Nimrod Avni** 23:59 Yeah, and I tried to make it, Tyler, kind of similar in the vein of the config V2 stuff, I don't know if it's final, but I tried to… A bit like that.
**Tyler** 24:09 That's great. I'm reading this config, I'm really liking what I'm seeing, this is great, yeah. I like these rules, I like this whole, yeah, this looks great.
The default action, yeah, is this… this is gonna be the default, is to exclude, these headers, and then it's only the ones that you want, right? Yeah, okay, yeah.
Yeah, this is great, I… I'm really excited about it.
**Nikola Grcevski @ Grafana / OpenTelemetry** 24:29 Yeah.
**Tyler** 24:30 Yeah, the body thing, that's gonna be interesting. I do want to point out that the, attribute package from OpenTelemetry Go is also getting updated to add a lot of the complex types right now, so that's also coming, just a heads up on that. So, if you wanted to start representing maps and, null s and bytes and that kind of thing, like, it's coming. Yeah.
More, more to come.
**Nimrod Avni** 24:56 Semantic convention, proposal of having it as, like, any type, and then you can have, like, if you can capture it as a string by, like, heuristic, let's say if it's, you know, content type JSON, then do… pass it as a string, and if it's not, then we can Just ignore it, I guess.
**Tyler** 25:16 Yeah, so we've had a lot of discussion at the spec level around the usefulness of capturing it as a string versus capturing it as, like, structured data, as well, so that might be something we want to take a look at. You know, one of the things is, like, just what you're saying, like, if you want to do some filtering on that, like, it becomes a lot easier if you have… you know, some sort of structured object type that you can iterate through some sort of parser to say, like, hey, take this field out or take that field out. When you try to do it as, like, a string parsing, like, it's not, like, impossible, but it's definitely, like, harder to do, and a lot of the times it just means that people drop the whole thing, in the process, because they're like.
I can't actually process this data, like, backends as well have a lot harder time, like, indexing off of this kind of thing, so, yeah, I think doing what you just said to start sounds great, and we could look into… Structuring it after the fact as well, so yeah.
**Nimrod Avni** 26:10 Also, I'll do, after this gets merged.
**Tyler** 26:14 Cool. Awesome.
Okay… Yeah, Java, working on that. User server spans, use server spans when instrumenting, SQL database. Yeah, I saw this one yesterday. I think it's Nikola, right? Or Mark, sorry, yeah.
It looks like…
**Marc** 26:36 Yeah, I did the integration test and… and, unit test that Nikola said, so… Oh, cool.
to another round.
**Tyler** 26:47 Cool, so this is just looking for reviews at this point.
**Nikola Grcevski @ Grafana / OpenTelemetry** 26:51 Yeah.
**Tyler** 26:52 Okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 26:52 Yeah, I think I'll re-read it again. This is similar to how, I think Nimrod did Redis server, I think Kafka Server, as just.
**Marc** 27:00 Europe.
**Nikola Grcevski @ Grafana / OpenTelemetry** 27:00 sequel.
I think we probably need to add Mongo Server as well, at some point.
**Marc** 27:05 Yeah, it was similar, like…
**Nikola Grcevski @ Grafana / OpenTelemetry** 27:09 Yeah, we had an internal report. People use OB to monitor SQL databases, apparently.
**Marc** 27:16 Turns out.
**Tyler** 27:17 When you, allow that feature, people use it, unfortunately.
**Nikola Grcevski @ Grafana / OpenTelemetry** 27:22 Yeah, it's kind of interesting, the spec does not talk about server SQL calls.
because I guess they didn't occur to them that.
**Tyler** 27:30 something.
**Nikola Grcevski @ Grafana / OpenTelemetry** 27:30 May instrument.
**Tyler** 27:32 Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 27:33 Get out.
**Tyler** 27:33 Yeah, I… that's actually really funny. I think… I was thinking about that when we were doing the automation stuff for Go as well, because it's like… Yeah, what happens when you start to also have the applications, like these completely opaque things that we never thought they would instrument, start to get instrumented? Yeah, so… that's really interesting.
**Nikola Grcevski @ Grafana / OpenTelemetry** 27:51 Yeah?
**Tyler** 27:53 Which is a good problem.
**Robert Pająk (Pellared)** 27:55 As I know, Splunk, we have a team which does some instrumentation for the racial databases, because that's why they wanted to have this, context propagation.
But probably they had not… I'm not sure why it's not in the spec at all. I think there was not enough people who wanted to contribute to the server, SQL instrumentation, semantical machines.
**Tyler** 28:21 Well, so, this is… this is the context propagation stuff, Robert, or you mean specifically, like, inside the, like, the SQL Server stuff?
**Robert Pająk (Pellared)** 28:30 I think even… I think maybe even specifically the SQL Server, I will try to… That's what I found out.
if Sam is also working on the stuff. Because if… if someone knows, then it will be Sam.
**Tyler** 28:43 Yeah, I mean, I think if there's, like… That's a good… that's a good point, actually, because I think you're right, I think, like, the stuff internal to Splunk, I'm, like, really not… authoritative on this, but, like, it's just top-level, kind of similar to what Obi would be doing here as well, so having unification would be great, yeah, yeah.
**Robert Pająk (Pellared)** 28:59 Yep.
Okay.
**Tyler** 29:02 Yeah, yeah, if you want to take a look, please, please let us know, open an issue, or comment at the PR afterwards. That sounds great. Thanks, Robert.
**Marc** 29:10 Yeah, by the way, when I was doing this, because we also have, like, client DB metrics, but not several ones.
**Tyler** 29:18 Right. And I noticed that.
**Marc** 29:20 For Radies server spans, we are generating client metrics, so I don't know if it's that right.
**Tyler** 29:30 We're generating client metrics inside the ser- or Redis server, you mean?
**Marc** 29:34 No, when there is a span that is, like, of a type-ready server, we are generating client metrics, so I don't know, because… Yeah, I was trying to do the same, but then I realized that probably doesn't make sense, so…
**Nikola Grcevski @ Grafana / OpenTelemetry** 29:50 Can you explain? Sorry, I don't get it.
**Marc** 29:54 So, they… So there is a, like, a part in when we generate the client metrics.
Sorry, yeah, the database, operation, I forgot what the name.
And there's the case of a span type, it is, like, Redis, Mongo.
**Nikola Grcevski @ Grafana / OpenTelemetry** 30:13 Yeah.
**Marc** 30:14 all of this, and there's also, like, if it's Redis server, it also generates, like, a DB operation client, metric, and I don't know if it's a bug or it's right.
**Nikola Grcevski @ Grafana / OpenTelemetry** 30:27 But DV operation…
**Marc** 30:29 Why would that be client-specific?
**Nikola Grcevski @ Grafana / OpenTelemetry** 30:32 Or is it… oh, the metric, you mean all the trace?
**Marc** 30:35 Yeah, yeah, yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 30:39 Right. But those, they probably need to be in a separate collection.
Not in, db client, because then, if you're tracking both the client and the server.
Yeah, I mean, maybe it's debatable. The service… The service name would be different, so it would be in DB client. I don't think there is a metric in the spec DB server, right?
So…
**Marc** 31:05 No, it's DV operation, but maybe that part was treating… I don't remember now, but, yeah, I can…
**Nikola Grcevski @ Grafana / OpenTelemetry** 31:14 He's in Divi Operations? Yeah.
**Tyler** 31:16 I don't think the spec defines any, like, server… database server metrics at all. Like, it's very client-specific focused.
**Marc** 31:25 Yeah, okay.
**Tyler** 31:26 Yeah, like, I think that, like, maybe we can, like, shoehorn some of the existing ones there, because that kind of makes sense. Like, you would want to see, like, an operation performed in the server, but, like.
It's more, like, those operations were just, like.
**Marc** 31:38 like a selector, an ad, or an insert, or something like that. Like, that's, I think, what the client side of the thing was.
**Tyler** 31:45 I think that the internals of the database itself are more about, like, query planning, or, you know, data management, or snapshotting, and that kind of thing would be way more interesting, which probably need more specification around, yeah.
**Nimrod Avni** 32:02 I'm not sure what, like, the… server spans for, let's say, SQL, Redis.
Give us, because it will be just a different service name, but it will be… Kind of the same operation, both on the client and… and it's not like… HTTP, where it makes sense because you're, like, propagating context, and you're also looking I don't know, looking at a service, like, you're looking at it as a service, but, like, when you're doing… let's say you're for, let's say you want to view the Redis as, like, a whole, you basically look at all the client spends, you aggregate other, like, the… DB, like, the peer service name, or whatever we take.
And then that's how you, like, aggregate it.
But… I don't know, maybe, maybe that makes sense?
**Marc** 32:53 Okay, thank you guys.
**Nikola Grcevski @ Grafana / OpenTelemetry** 32:55 Okay.
**Marc** 32:56 Yeah.
No, now I found it, and it's… the metric is DB client operation duration, and we are using Like, ready server? Yeah. Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 33:08 But there is no other metrics, so, I mean.
**Marc** 33:11 Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 33:11 make my own and propose one in the spec to split them up, so it's DB Server operations per second. But it's not… I don't think it's going to be technically wrong. If you look per the service, it will be the ready server or the SQL server, you'll see all the operations are being sent there, it's just called client. Perhaps it's not.
**Nimrod Avni** 33:33 And they're also not, like, client spends, right? We derive the metric from the server.
**Nikola Grcevski @ Grafana / OpenTelemetry** 33:40 Yeah.
**Tyler** 33:43 Yeah, I just think that we're… we're on the edge of the OpenTelemetry to find things. So, I do think that… And obviously, it depends on how much time you have. Like, I definitely think opening an issue in the semantic conventions repo is a really good idea to track this, because I don't think that they anticipated people hitting this, or they did, and they didn't think it was gonna come for a long time. And then the other thing is, is, like.
Where there aren't any semantic conventions, OpenTelemetry people should do exactly what I just said, like, try to make them, try to involve them.
But there's nothing stopping us from creating our own metrics as well.
In fact, as long as we're not telling people that they're stable metrics, it's probably a good idea to try to get some field testing to find out if the metrics that we're going to create for the server are viable, and, like, then giving feedback to the semantic convention group and saying, like, here are the things that we found that were useful on the server side, which may be just exactly what we just said, like, a server operation, maybe other things as well, but yeah, I think that, like, having… it set, this is how it usually goes, yeah.
**Robert Pająk (Pellared)** 34:49 have added in the chat an issue about database server metrics. There's already an open issue with proposal.
**Tyler** 34:55 Oh, perfect.
**Robert Pająk (Pellared)** 34:56 And it was even commented by Josh Surrett.
**Marc** 35:00 Oh, nice.
**Robert Pająk (Pellared)** 35:01 Or… Assign.
No, just time.
**Tyler** 35:05 dollar.
share my screen and we can take a look.
**Robert Pająk (Pellared)** 35:09 found anything regarding plans, but I was just looking for myself, even without AI.
**Tyler** 35:16 So, is this.
**Marc** 35:18 Okay.
**Tyler** 35:23 So we've got Actually.
**Marc** 35:25 attributes…
**Tyler** 35:31 Oh, okay. Here we go. This is what they were looking at.
Wow, that's a lot of metrics.
Cool.
Yeah, this is… this is probably what we want.
The thing is, is also, I don't think that we have… details to populate all of these, but we might have enough to populate some of these. Like, especially this throughput stuff, we could probably figure something out here, right?
**Nikola Grcevski @ Grafana / OpenTelemetry** 36:01 Yeah.
If there is a proposal in the…
**Nimrod Avni** 36:08 I know… specific instrumentations on specific databases. It could be, like, a different rental being, like, instead of doing, like, APM, metrics and traces, we also, like, do database performance stuff, which would be cool.
**Nikola Grcevski @ Grafana / OpenTelemetry** 36:23 Hmm.
**Tyler** 36:24 Yeah, I mean, I think that'd be…
**Robert Pająk (Pellared)** 36:26 noting that for sure, some attribute names here are outdated, because I remember that right now, instead of DB system, it should be db system name, and stuff like that. So, some of them probably should be, like, refined, but at least there are some I think there at least can be, you know, some kind of stuff Some monthly click will be reused here.
**Tyler** 36:53 Yeah, that makes sense.
Cool, alright, well, I will… I think… I think we can just leave it, Yeah, if people are interested, please take a look at this, and comment here, as well.
It's about to go stale again, I'm guessing. So, yeah, if we have some thoughts on this, I think that this would be helpful, even if it's just, like.
we plan to do something at the top-level throughput. Like, and you don't have to say this, like, I think that maybe even just saying, like.
DV server operation is viable as something you could propose.
But yeah, this is great.
Okay, moving on to the poll requests. So, up next, Updated go, yeah, fighting with this one. I'm so close on this one.
**Nikola Grcevski @ Grafana / OpenTelemetry** 37:44 Oh, you're trying to go to 126?
**Tyler** 37:46 No, not even that. This is just updates for packages. Yeah, that's also on the list of things to do. No, this is like… yeah, so, this updated, actually, maybe I could ask questions on this one. So, it updated OATS, which… then I looked upstream, and I noticed that a lot of… A lot of people are not doing this upgrade here, so, I reverted that change in this PR, and that fixed, I think, most of the OATS issues, but I'm still getting HTTP and SQL issues here as well. And then… what else? I think I… Downloaded… downgraded oats… Yeah, oh, and I downgraded this, Selium EBPF, library as well, and I captured both of these in issues for our project. So just, you know, like, this blocked upgrade and this blocked upgrade.
Maybe I could ask, like, is there… Is there a path forward for the OATS one? Are we planning to do this upgrade? Like, it looks like there's a completely different syntax for, how you're defining the… The runs themselves, it looks like?
**Mario Macias** 38:56 Yeah, I worked in that in the past, and it involved mostly rewriting all the tests, there were a lot of breaking changes.
**Tyler** 39:09 Okay.
Well, I can track it, like, if we want to do this upgrade, like, it seems like something we can do. I didn't want to do it in the middle of a Dependabot upgrade, so I put it in an issue, but, I'm also fine closing this if we don't want to move to that, but I… yeah, just wanted to raise this as a thing we… I found.
**Mario Macias** 39:27 So, yeah.
**Tyler** 39:28 The other one was, this upgrade of UPF, which, I think Florian? I forget, somebody pointed out, no, Matia, sorry, pointed out that they are already working on this upstream, where there's, like, this exec, requirement.
That was unneeded. Ron's got one thing merged, and I think there's this other issue that's still open. Is Mattia on the call? Sorry, I think I…
**Mattia Meleleo** 39:53 Yeah, I think this was an unintended breaking change. I think we should, This guy proposed, like, to fix it. I think when the fix is out, we should propose, like, a patch.
release.
**Tyler** 40:09 Okay.
Cool. Alright, yeah, so then, on that one, it's just more about waiting for upstream. So that's… that's not too big a deal.
But yeah, I still can't get this, Redis and SQL, OATS test to pass, and for some reason the shards are still… actually repeatedly failing, so, I still have to look at other things here, and maybe there's some more downgrades,
**Nikola Grcevski @ Grafana / OpenTelemetry** 40:30 Can you scroll down, maybe I can spot it. Oh, let's see.
**Tyler** 40:33 Sure. Sorry, it's Lotus. Can we scroll up, or does this make sense to you?
**Nikola Grcevski @ Grafana / OpenTelemetry** 40:39 Yeah, it looks like it can't find the ready separation somehow.
Could be, like, if anything changes in the Redis library… which one failed? Which one did it say?
this Go Redis. What could be is that something changed in the… In the dependency that we no longer… that U-Probe no longer works.
**Tyler** 41:04 Oh, okay. Yeah, alright, so it's more tracking down.
**Nikola Grcevski @ Grafana / OpenTelemetry** 41:07 Yeah, it looks like the… because it's Go, how about the SQL? Which one failed as well? If you click on the SQL…
**Tyler** 41:13 Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 41:17 Yeah, click sequel.
**Tyler** 41:19 This one, again, I think is also… it misses a…
**Nikola Grcevski @ Grafana / OpenTelemetry** 41:22 Yeah, go Postgres. So, my guess is that these are real issues, that we're gonna have to make, changes in the code.
I… if you want, I can help with some of this.
**Tyler** 41:33 Yeah, that sounds good. That's actually really helpful in itself. What I might do is, just to unblock this PR, is I could capture both of these in a issue, and, like, then we can, yeah, I'll ping…
**Nikola Grcevski @ Grafana / OpenTelemetry** 41:47 contractor, yeah.
**Tyler** 41:48 Yeah, and then we can do the upgrade in a separate thing, so… Yeah, okay, that's helpful. So yeah, I will keep chugging along on that one.
Cool. And then there's also, like, Major Go update, I haven't even taken a look at this, I was just trying to get the minor one. But yeah.
The lock maintenance, I'm guessing this is a Node.js one. Also, haven't taken a look at this. This is, I think also failing… this may be transitive, though, it looks like.
**Nikola Grcevski @ Grafana / OpenTelemetry** 42:17 Yeah.
**Tyler** 42:17 So… Okay, yeah, I just haven't… Dived into these too much after… that. So looking at the… trying to integrate with the collector is my main thing right now. So, yeah.
So, not to waste too much more time, giuseppe, you have the parameterize the ring buffer forwarder, and update the, shared ring buffer and the forward ring buffer to generic.
**Giuseppe Ognibene | Coralogix** 42:40 Yep.
I think it's almost done, I saw Matthias comment.
**Tyler** 42:49 Cool. Yeah, looks like you've got plenty of reviews, so it's more up-to-date, and we're just looking for more reviews at this point, right?
**Giuseppe Ognibene | Coralogix** 42:55 Should be merged, I think, I hope.
**Tyler** 42:59 Okay. But yeah, I will, we'll talk with Mattia.
Perfect. Okay, yeah, then we will… we'll wait for more reviews and keep an eye on it.
**Giuseppe Ognibene | Coralogix** 43:09 Thank you.
**Tyler** 43:11 Raphael, a large buffer is enforced per request per direction limits.
**Rafael Roquetto** 43:16 Yeah, so this is changing this, like, OTLE BPF buffer size HTTP, and Kafka MySQL. Those values were per large buffer, when large buffers are enabled.
The… The issue with that is… imagine you have, for instance, an HTTP request.
That is, I don't know, 100 megabytes?
And then… the large buffer size is 1MB. That means that… and then you get chunks off… 2 megabytes.
Right, coming. So, this 100MB chunked in chunks of 2, And that means, Yeah. And then we're just reading the first megabyte of those chunks, so we're sending Only parts of the total request to the user space.
with holes in the middle. So, what this does is instead you cap The amount of bytes you want to read per request, per direction, so request and response.
That, obviously, you know, maybe you don't want to send the entire 100MB to a user space.
Oh, you want to send from 0 to, I don't know, 10, or 0 to 1, so that this is continuous, so it… it does… it does that.
If that… if I'm making sense.
**Tyler** 44:35 Yeah, I think so.
**Rafael Roquetto** 44:37 Ugh.
**Tyler** 44:38 So, it looks like it is in need of review.
**Rafael Roquetto** 44:43 Yeah, Nikola reviewed it. I've, addressed, hopefully, his comments and Copilot's comments as well. I've been finding Copilot very helpful, picking up really, like, corner cases that are not visible from Nick's eye.
So, yeah, I just updated it, it was a problem, problem with the, with the linter. I moved, one interesting thing about this PR is that I moved to the BPF tests to… from internal package internal, package internal test BPF to the BPF directory.
itself, inside BPF tests, and that means that we can now use… the actual BPF test, the actual BPF code inside the test, so I added a few stubs for the VM Linux and BPF helpers, like.
So we can run this in user space, for testing.
And, yeah, that's, I think he's pretty much ready to go, but…
**Nikola Grcevski @ Grafana / OpenTelemetry** 45:44 Yeah, I'll do another review. Yeah.
Today? Nope. Yeah.
**Tyler** 45:49 Yeah, alright, that sounds good. Those on the call as well, looking for more reviews on this one as well.
Cool, thank you.
**Rafael Roquetto** 45:55 Norris.
**Tyler** 45:56 Okay, Nimrod, verify the SikUser 1 handle is not registered before trying to inject the Node.js agent.
**Nimrod Avni** 46:04 Yeah, that's an issue we had, for a while, and then someone, recently opened it about OpenClaw in Slack.
Yeah, I tried to think, like, so there's something Nikola using his, like, Node Harvester, and then, I kind of did some more research and stumbled into this, that… It seems like it consistently works. I tried it with, like, multiple node images, versions.
I'm thinking about adding, like, integration tests for it with, like, multiple node images, but I'm not sure… it's like, I only want to test the injection part and not the full OB, so I don't know… if we should… like, I should just test that context propagation doesn't work.
or have some separate thing that I set up, Docker, I don't know. But, yeah, in general, like, there's some way here to differentiate between the default, C user one that opens the… the… The, inspect, port.
And the one that, like, custom signal handlers use, and that's the ones we want to avoid?
By reading some internal memory from the process, And, yeah, so I'll… I'm thinking if I need to add more, like, I did some manual tests, I don't know if they should… Add some more, like, integration tests for it.
But in general, I just, I just, Nikola and Rafael computed some stuff out, and I fixed it, like, an hour before the call.
**Nikola Grcevski @ Grafana / OpenTelemetry** 47:37 That's…
**Rafael Roquetto** 47:37 I'll do another…
**Nikola Grcevski @ Grafana / OpenTelemetry** 47:38 Cool.
I love doing MPS as well, it's pretty cool.
**Nimrod Avni** 47:42 Thank you.
**Nikola Grcevski @ Grafana / OpenTelemetry** 47:43 Yeah, I can also test, if you like, with some older Node versions that I have to see if it works.
Bye.
I think it's solid.
So you're testing with 22, right? I think I have even an older, like, 18 somewhere. Oh, yeah, I'll give it a shot.
**Nimrod Avni** 48:00 And I also tried with some, images that, like, I tried to search it.
For some reason, it chips with either, like.
Non, like, it's not symbolized, or there's.
**Nikola Grcevski @ Grafana / OpenTelemetry** 48:11 So… Yeah.
**Nimrod Avni** 48:12 Difference between executables, and whatever. But I couldn't, get it to not work.
**Nikola Grcevski @ Grafana / OpenTelemetry** 48:21 Pretty cool.
**Tyler** 48:25 Well, cool, alright, yeah, thanks, that sounds good. We'll wait for more use on this one. Yeah, this is… I'm happy to get this fixed, so… that sounds great.
Next up is… More dependencies, and then… the HTTP to GRPC context propagation, Mattia, this is another, PR from you.
**Mattia Meleleo** 48:50 Yeah, tests are passing right now. I added a test for this, which, tests for 6, services.
**Tyler** 48:59 Oh, nice.
**Mattia Meleleo** 49:00 It, tests for the trace ID being the same for all of them, and then, parent, and the span, correlation.
Yeah, so it's open for reviews. Don't let the 3.6K lines worry you, because it's, like, 2,000 of them are mostly from a Java service, which is used for tests.
That's, yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 49:29 That's crazy, man. Like, I… I can't believe we're… we managed. Yeah.
**Mattia Meleleo** 49:35 I did nothing, it's all clothed.
**Nikola Grcevski @ Grafana / OpenTelemetry** 49:37 Gotcha.
**Rafael Roquetto** 49:38 Haha.
**Nikola Grcevski @ Grafana / OpenTelemetry** 49:39 Yeah, sure.
**Rafael Roquetto** 49:40 How do you?
**Nikola Grcevski @ Grafana / OpenTelemetry** 49:41 Yeah.
**Tyler** 49:42 No, this is great. I've been wanting to add a test, like, because I was doing this manually, and so, yeah, this is great. This is exactly the test I was looking for, so this is awesome. Thanks for doing this.
**Nikola Grcevski @ Grafana / OpenTelemetry** 49:52 This is amazing.
**Rafael Roquetto** 49:53 Yeah.
**Mattia Meleleo** 49:54 Yeah, if you have any suggestions for other relays or hopes I can add to this…
**Tyler** 50:01 I mean…
**Mattia Meleleo** 50:02 Hopefully the tests are more…
**Nikola Grcevski @ Grafana / OpenTelemetry** 50:03 Alright, this…
**Tyler** 50:04 The only thing that I could think to add is more services, which is… things like, .NET or C++ or something like that for particular cases that we support, but I think what you have here is a great starting point, at least. I would probably say hold off on that.
**Nikola Grcevski @ Grafana / OpenTelemetry** 50:20 Yeah, I mean, you've added Go, so Go is doing it probably the other way, and so I… Yeah.
That's great.
**Tyler** 50:31 Yeah, this is great. Yeah.
Cool, yeah. We'll have to take a look after the meeting, but yeah, thanks for doing this. This is great.
And then last up, I don't know the user here, support MySQL… Yeah, I know him, he… I think he had some issues now with.
**Nimrod Avni** 50:53 what's the name of it? Like, the registering his user, that CLI thing.
He opened an issue, like, a while back, he's working on, Microsoft NSSQL support.
Okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 51:07 What's the PR.
**Nimrod Avni** 51:08 Yeah, I think he opened it, and then he told… I'll try to help him with just, like.
**Nikola Grcevski @ Grafana / OpenTelemetry** 51:13 Okay.
**Nimrod Avni** 51:13 setting it up.
Maybe, I think he tried to, like, rebate or something, and…
**Nikola Grcevski @ Grafana / OpenTelemetry** 51:17 Oh, okay. It's just freezing on it, yeah.
**Nimrod Avni** 51:21 Yeah, but I'll try to help him, and I saw the code, it looks good, maybe some Fs missing, but… I think it looks good.
**Nikola Grcevski @ Grafana / OpenTelemetry** 51:29 How are we gonna test that?
**Nimrod Avni** 51:31 I think, I think there are some community… I searched it up, I think there's some community images.
**Nikola Grcevski @ Grafana / OpenTelemetry** 51:36 Oh, perfect. MSSQL. So I think you can… I think there's, like, some…
**Nimrod Avni** 51:41 It's like, you don't need a license.
**Nikola Grcevski @ Grafana / OpenTelemetry** 51:44 Oh.
We shouldn't have done this long ago. Yeah, it's great.
**Nimrod Avni** 51:47 I guess it's just, yeah, it's not… I guess, I don't know if it's super, super, like, widely used, but in their case, it is.
**Nikola Grcevski @ Grafana / OpenTelemetry** 51:54 Oh, it is, yeah. People will use it.
Especially those that have, like, Windows… Traditionally, in their environments, they probably are doing, like, a cloud server or something like that, and they need a bunch of other services to connect to it. Yeah, I think it's good. The more, the merrier, exactly.
Yeah.
**Nimrod Avni** 52:15 I'll help him, open the PR, and I'll also try to do this on… Preliminary reviews as well.
**Nikola Grcevski @ Grafana / OpenTelemetry** 52:22 Thanks, Naura, that's great.
**Tyler** 52:25 Yeah, that's awesome.
Yeah, super excited.
Okay, that's the end of the open PRs. We are coming up on the end of the hour. If there's any other topics people had, or maybe even some cool ideas, cool, things they're doing in the background…
**Nikola Grcevski @ Grafana / OpenTelemetry** 52:40 I just wanted to say congrats to Giuseppe for becoming approved.
**Tyler** 52:44 Yeah, welcome.
**Giuseppe Ognibene | Coralogix** 52:46 do it.
I'm scared about things.
**Nikola Grcevski @ Grafana / OpenTelemetry** 52:51 You're doing a lot of work, so…
**Nimrod Avni** 52:53 Just approve anything, it'll be…
**Nikola Grcevski @ Grafana / OpenTelemetry** 52:55 We've ever taken.
**Giuseppe Ognibene | Coralogix** 52:55 No, no, no.
**Nikola Grcevski @ Grafana / OpenTelemetry** 52:56 First switch.
**Giuseppe Ognibene | Coralogix** 52:57 No, no, I will not approve anything, yeah.
**Tyler** 53:00 The trick is to stay as an improver, though. Don't become a maintainer, trust me.
**Giuseppe Ognibene | Coralogix** 53:04 If someone emails me, I can approve it, no problem.
**Tyler** 53:08 Yeah.
**Giuseppe Ognibene | Coralogix** 53:11 Thank you.
**Tyler** 53:12 Yeah, awesome, awesome.
**Mattia Meleleo** 53:17 Are you in the question?
**Nikola Grcevski @ Grafana / OpenTelemetry** 53:19 I had… Sorry, go ahead, go ahead, Mattia.
**Mattia Meleleo** 53:21 Okay, thank you.
**Nikola Grcevski @ Grafana / OpenTelemetry** 53:22 Thanks, yeah.
**Mattia Meleleo** 53:23 So, so a while ago, I posted a photo in the OpenTelemetry specification, I think it's called, which seems to be a little bit stuck.
I don't know how that process works there. Do these OTEPs remains open until someone reviews them, or should we ping someone? How does it work in general?
I will, put the link in chat.
**Tyler** 53:50 Yeah.
So… I got bad news, is kind of the thing I'm holding on. It's gonna take a lot of work, is the thing. So, if you don't have immediate reaction from a lot of people that they're interested in this, it's gonna be… you're gonna have to drive this, and, you can ask Robert and other people that have written OTEPs, like, it can be challenging. The best way to do this, though, I think, is to come to the specification meeting on Tuesday mornings, or I guess the evenings. It's actually the same time as this meeting, just on Tuesdays.
And, mention it there.
get synchronous feedback from people is… it puts it in their top of their minds. You're gonna get people who are in charge of, like, actually getting the approvals done on this, and if you can motivate it there, and you can motivate saying, like, this is why I want to do it, this is what is needed, that's really how you're gonna be able to push this along, is through those synchronous conversations, unfortunately.
I'll be there, Robert would be there, I'm happy to help amplify your voice if you need to help you out on that one as well.
But yeah, it's gonna take, I think, a little bit of motivating, and then once you can get people motivated to go do it, you need, like, I think 5 reviews of an OTEP, and then from there.
it's a bureaucratic nightmare. So then from there, once that gets merged, then you can write specification for it if it's needed, or you can… if there's not a lot of specification, it could just be an assumed, practice, and then you need prototypes before the specification can actually get merged, so… Yeah, it's a little bit of a thing, yeah.
This is for the, the inner process communication for the trace context stuff between profiles and, Obi.
Yeah, I think this one may be a little bit more, easy to get into the specification, like, in the sense that it's not gonna have a lot of specification around it, given its interaction between two different, like, sub-projects of OTEP, or OTEL. It's not gonna be something that all SDKs have to adopt. So, you also have the precedence that, I think it was recently.
the resource… environment resource format for the profiler is merged, or it's got enough approvals for that OTEP, so I think, like, there's… there is precedence here, so it should be a little bit easier, but, like, yeah, it's just about getting this forefront in the specification mind, so, yeah.
**Florian Lehner** 56:08 You know, what is missing here is probably an, priority ordering. So if something is instrumented with an SDK, and we get this information from the profiling side with the… process context, propagation via the… via the other outtat, basically, so that we… what… what is the decision, which, information has priority if they maybe collide?
Yeah, otherwise this OTEP looks super nice, yeah.
But…
**Tyler** 56:46 So, Florian, could you do me and Mattia a huge favor, and just, like, I know you just told them that, but could you comment that in the issue to show some sort of activity in the OTEP to try to bring it up in people's notifications as well? I think that'd be really helpful.
**Mattia Meleleo** 56:57 I think there is a discussion about that, and I also answered. I'm not sure it belongs in this specific article, because it's more of a general thing, right? Readers against writers.
**Florian Lehner** 57:10 Yeah, I would agree with you that it's more a general thing, around… OTEPS, yeah, but not sure where to place this correctly. From my experience with OTEPS is that, it's best to, do something on then on Mondays, as the meetings are on Tuesdays, and the minds are usually fresher.
**Mattia Meleleo** 57:33 Yeah, I will join the next one. I will see what people think there.
**Florian Lehner** 57:38 No.
**Mattia Meleleo** 57:39 Thank you.
**Nikola Grcevski @ Grafana / OpenTelemetry** 57:43 And if we knew.
**Tyler** 57:43 Cool.
**Nikola Grcevski @ Grafana / OpenTelemetry** 57:44 pick something, I would say, wait, you're just… agree that if the information is from both places, then the SDKs win?
Perhaps they have more insight, closer.
Information or something like that, but… You're just putting in the rules.
**Florian Lehner** 58:03 Yeah, I think I usually join the meetings on Tuesday, so I can bring it up and bring your attention to it again.
**Nikola Grcevski @ Grafana / OpenTelemetry** 58:12 Awesome.
**Tyler** 58:15 Yeah, so, yeah, Mattia, feel free to ping myself, Florian, and Robert before the meeting on Tuesday if you're not going to be able to go there. Sounds like Florian can also kind of bring this up as well, so, like, there's definitely some help, if you're not able to attend the meeting.
But yeah, I think that's… that should be helpful.
Okay, we are right in the last.
**Nikola Grcevski @ Grafana / OpenTelemetry** 58:35 A few minutes?
**Tyler** 58:37 Yeah, Nikolai, did you have one thing to close us out on?
**Nikola Grcevski @ Grafana / OpenTelemetry** 58:40 Yeah, I was… I found out, for somebody who works on the SDKs, that they told me that not many SDKs provide the… The trace to law correlation?
**Tyler** 58:51 Right.
**Nikola Grcevski @ Grafana / OpenTelemetry** 58:52 So only a handful of SDKs, so I think this is a nice use case of what Mattia, added, that perhaps this… oh, we can do this. Even if you're not instrument in Adobe, you can just probably kind of… supplement?
Yes, the case?
**Tyler** 59:09 Yeah, and even in the SDKs, they aren't going to be reaching into, like, exports of logs outside of the OTEL system, so there's just, like, there's very little chance that it would replicate the behavior that Obi's doing. The only chance would be is if they're also using the logs or events API, and then trying to query.
**Nikola Grcevski @ Grafana / OpenTelemetry** 59:25 there.
**Tyler** 59:26 And, like, that… I don't think many people are doing that even in most SDKs, so even… even if they were, there's a use case that this is handling that is not, In the SDKs, yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 59:38 Yeah, I was gonna say, it's gonna be a great KubeCon talk.
Oof.
At least from the next one, in line, whatever that is.
**Tyler** 59:46 Yeah.
Yeah, absolutely.
Well, cool. We're right at the hour, I'm gonna be respectful of people's times. Thanks, everyone, for joining. I will see you all next week, or asynchronously. Until then, bye.
