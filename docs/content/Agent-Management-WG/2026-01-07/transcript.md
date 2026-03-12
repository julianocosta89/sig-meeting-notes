SIG: Agent Management WG
Date: 2026-01-07
Duration: 15 minutes
============================================================

## Zoom Recording Transcript

**dpaasman** 00:54 Hey.
**Michel Laterman** 00:58 Whoa.
**dpaasman** 01:00 How you doing?
**Michel Laterman** 01:02 Morning, tell you.
**dpaasman** 01:04 Not too bad.
**Evan Bradley** 01:42 Happy New Year, everyone.
**Michel Laterman** 01:46 Happy New Year's.
**JM Juande Manjon** 01:48 Happy New Year.
**Michel Laterman** 03:29 Do we want to wait for anyone else?
**Evan Bradley** 03:33 It's about 5 minutes after the hour, I think we're good to go.
**Michel Laterman** 03:38 Okay.
Oh, well, on the only thing on the… notes right now.
It's not just a skill test driver, but it started that… It started out that I wanted some way to… test the amount of connections an op-amp server could actually handle, so… The initial implementation.
which is, in the first years of that PR, had a… I'm done eating, I would just try to connect.
And you can pass.
had a dumb agent, but I've since refactored, so… I'll be splitting that draft into a couple PRs.
Must have found a few different things.
So far?
The main part is gonna be the steel test driver, so it's gonna be an example, it's gonna be… under the examples, directory… And you should just be able to do that to launch.
Agents to connect to.
a server. By default, you can use the example soon.
And I've chosen to use the example agent, so… Whatever features we implement can be tested as well.
Part two of it is when I was actually doing the work, I found Some improvements we can do to the… A server library, and a couple bugs in the example server, and… client library, so that's gonna be split off into other PRs.
I don't know if anyone has any interest in this one.
any feedback, but I'm welcome to it.
**Evan Bradley** 05:45 I can't say too much. I mean, this does sound like it'd be interesting.
And, I don't… I guess the only feedback I have is… I could see this if… we really want to, offer this as, like, a tool. I could see it going in, like, the CMD, directory, and being published as a binary for, like, use, like, telemetryGen is, for the collector.
I mean, it does make sense, right? I mean, we need something that… can, you know, generate op-amp messages, for… For use with, you know.
Testing, you know, implementations, so… I don't know, I generally agree. I can't speak to the rest of the changes here. I see that you made changes to the agent and the server. I expect we'd want to make those separate.
**Michel Laterman** 06:44 Of course, you know, we do that.
**Evan Bradley** 06:45 But I mean, you were already calling out the fact that we probably want to split this out.
Yeah, my only feedback would be to move it from the internal examples to a CMD.
Directory and publish it as a binary, if… you know, we decide that this is something we want, but broadly, it makes sense to me.
**Michel Laterman** 07:05 No. Right now, it's…
**Raphael Menderico** 07:07 And examples, because that's where the example agent lives, but…
**Evan Bradley** 07:12 Checks out.
**Michel Laterman** 07:13 an easy change.
**JM Juande Manjon** 07:15 Yeah, so for me it looks fine, but I don't see any information in the PR, and also there is no issue to provide more context to understand better.
**Michel Laterman** 07:27 Just cause I have extra time this week.
Huh.
**Raphael Menderico** 07:31 Due.
**Michel Laterman** 07:32 5 projects, so… That's what this is right now. I can make an issue for it.
**JM Juande Manjon** 07:49 Accordingly, then… The example has built, a Docker image.
for the server and the agent, maybe it makes sense to also have a Docker image to To run this utility to… To do a scale test in the server.
**Michel Laterman** 08:11 Yeah, we can… I'll clean up the PRs, and we can discuss if it should be moved as a… binary under command, or it should just be, Docker imaging examples.
**Evan Bradley** 09:01 I can throw something on the… Agenda real quick.
One second… oh, well… Okay, anyway, I was just gonna throw… a request… if you're all good, Michael.
I assume you're good on your… your agenda item?
Oh, you're muted, okay, that's why, okay, I couldn't hear you. Got it. Cool.
**Michel Laterman** 09:34 Yeah, I'm good.
**Evan Bradley** 09:35 Okay, anyway, yeah, if anybody, Has time… I could use a preliminary review on… Oh, whoops, I need to change the… Boom.
the labels here. I could use a preliminary review on… any supervisor extension PRs that are open. I have not had as much time lately to look, and just kind of…
**Raphael Menderico** 10:22 Getting something that looks like it's kind of ready to go would…
**Evan Bradley** 10:26 help make my review cycle a little bit quicker. Here we go… Yeah, there's a couple that are open that I will hopefully be able to take a look at soon, but if anybody has extra time, an initial review would help me out.
**dpaasman** 10:47 Just any supervisor PRs that are open.
**Evan Bradley** 10:51 Supervisor extension PRs, I mean, anything op-amp-related in the collector repo.
**dpaasman** 10:57 Yeah, I'll see if I can take a look at any of it this week.
**Evan Bradley** 11:01 Yeah, of course.
And that's all we got on the agenda. Anybody? Have anything else?
Okay.
I think we're ready to call it, then.
See everyone at the next one.
