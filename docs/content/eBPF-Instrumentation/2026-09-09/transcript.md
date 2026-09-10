SIG: eBPF Instrumentation
Date: 2026-09-09
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Stephen Lang (Raintank, Inc. – Grafana Labs)** 00:44 And Nikola.
**Nikola Grcevski @ Grafana / OpenTelemetry** 00:49 How's it go?
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 00:51 Girly.
**Nikola Grcevski @ Grafana / OpenTelemetry** 00:52 Yeah, right? Good.
**Tyler Yahn (Splunk)** 01:11 Hey.
How y'all doing?
**Nikola Grcevski @ Grafana / OpenTelemetry** 01:22 That's good. Good to be back.
**Tyler Yahn (Splunk)** 01:24 Yeah, how was, Grafana Fest?
**Nikola Grcevski @ Grafana / OpenTelemetry** 01:27 Yeah, it's a lot of fun.
Oh, yeah? It's a lot of fun, yeah.
**Tyler Yahn (Splunk)** 01:30 Where was it at? Was it, Nikola Grcevski @ Grafana / OpenTelemetry 01:32 Vienna.
**Tyler Yahn (Splunk)** 01:34 Oh, that's right, yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 01:35 Fair enough.
Yeah, that sounds like…
**Tyler Yahn (Splunk)** 01:38 Quite a flight.
**Nikola Grcevski @ Grafana / OpenTelemetry** 01:39 Yeah, it's a long flight, but they… they… they really spent some money, because it was… Like, we were, like, dining in the royal palaces and whatever, and… yeah.
**Tyler Yahn (Splunk)** 01:53 Oh, wow. Yeah, treated like kings.
**Nikola Grcevski @ Grafana / OpenTelemetry** 01:56 Yeah, exactly. I was saying the Habsburg kings are rolling their graves. All these tech people invaded their precious buildings.
**Tyler Yahn (Splunk)** 02:08 So many Habsburg jokes there, I don't know what to say.
Yeah, that's awesome.
When'd you, when'd y'all get back? Did you just get back recently?
**Nikola Grcevski @ Grafana / OpenTelemetry** 02:22 Yeah, I mean, I came back before Labor Day weekend for us here. I think we all flew back on Friday, I think.
**Tyler Yahn (Splunk)** 02:29 Oh, okay. Yeah, I gotcha. So you've been back all week, yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 02:32 Yeah, yeah.
To recover properly.
**Tyler Yahn (Splunk)** 02:38 Yeah, I saw some photos. There was a pretty.
**Nikola Grcevski @ Grafana / OpenTelemetry** 02:40 Hotel, congratulations.
**Tyler Yahn (Splunk)** 02:41 bomber right there. So, yeah, it's good.
**Nikola Grcevski @ Grafana / OpenTelemetry** 02:43 Oh, yeah, yeah.
**Tyler Yahn (Splunk)** 02:44 Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 02:45 Lots of people over it.
We had Jack Berg talk a little about hotel stuff. Yeah, it was quite fun.
**Tyler Yahn (Splunk)** 02:52 Yeah, was, is, did I see Ted Young there as well?
**Nikola Grcevski @ Grafana / OpenTelemetry** 02:55 Yeah, Ted Yahn, yeah. I don't think Ted came on stage this time around.
Maybe it's on the breakouts, but it wasn't. But Jack Berg was on… had a lightning talk. Yeah.
**Tyler Yahn (Splunk)** 03:05 Oh, cool, okay, yeah.
Was that the only hotel talk there?
**Nikola Grcevski @ Grafana / OpenTelemetry** 03:11 No, there was more hotel, but breakout sessions, so people that… Especially the folks in Grafana there.
We have an hotel department.
**Tyler Yahn (Splunk)** 03:20 Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 03:20 We don't belong, somehow, Ann.
our little Baylor team, OB team, does not belong in that department, but…
**Tyler Yahn (Splunk)** 03:31 You're, like, the… Nikola Grcevski @ Grafana / OpenTelemetry 03:32 the satellite.
**Tyler Yahn (Splunk)** 03:32 light, or something like that.
**Nikola Grcevski @ Grafana / OpenTelemetry** 03:33 Yeah, yeah.
**Tyler Yahn (Splunk)** 03:36 I gotcha.
Well, cool. Alright, let's see, where are we at? 3 minutes in? Looks like we got Quorum, so we could probably start up here in just a second. If you have any yet, go ahead and add your name to the attendees list. If you have agenda items you want to talk about, please go ahead and add them there as well.
And, yeah, then I can… Start sharing my screen, we can get into this.
Awesome. Okay, cool. So, to start us off, I want to follow up on this PR for, issues and description.
enforcement? This is a follow-up from… Last time, Macias had brought up this idea of adding in some sort of AI policy here, so, thanks, Macias, for getting after this and opening up the PR.
Definitely, definitely a step in the right direction. I did want to, follow up on this, though, because I wanted to see about changing the direction here. Right now, this is a CI check.
And it's validating against, like, static Values in a particular description.
I was wondering if we could switch to doing something more in the AI policy? You know, the idea here is that, like, we were trying to enable people who are writing, descriptions with AI to write them better, and write them in a human-readable way.
So if we could use the policy to help them in that process, I think that that would be, I think, a more proactive way to do that, instead of a reactive way, and… It would also, I think better align with, like, what we're trying to do with, like, multi, like, dimensionality to these things, so that they're not, like, one-size-fits-all. But I wanted to ask.
What y'all thought about that.
**Matt** 05:23 So, I think, in my opinion, that, that wouldn't work, because, Because an external contributor needs to read the AI policy first, but if they just, they just compiled a PR, and they open a PR, they… They don't know about the existence of the policy, because they did everything with Cloud Code, for example.
**Tyler Yahn (Splunk)** 05:49 Yeah, it doesn't really make sense to me, though, right? Because, like, if we're validating things with a CI policy, and it's in code.
they'd have to read the CI code to understand, like, what we actually expect of them.
And as you just said, like, if they're writing this with Claude code, like, Claude would already read that.
So I'm not following that logic.
**Marc Tudurí** 06:11 I think…
**Matt** 06:11 Could you repeat? I didn't understand.
**Tyler Yahn (Splunk)** 06:14 Well, so the AI policy, like, you can have an agents policy, right? So, creating, like, a cloud.md or an agents.md file, that's read by these AI agents as they are interacting with the repository.
This is done in a lot of other places as well, like, I know we do this in, like, the OpenTelemetry Go project, I know the specification, the Helm charts, all these things, And when AI is writing code or doing something in the project.
They are actively, like, reading that first.
So they would know the policy if they're using, Claude to write the description. It would be something.
**Matt** 06:51 Yeah, but are they following it? Because I know that in the policy we have, to not have verbose comments, for example, but my cloud still keeps writing and writing and writing, so I don't think that that's used by the agents.
**Tyler Yahn (Splunk)** 07:07 Well, yeah, I got a few questions about that, because, like, I definitely know that a CI check is not used by agents, like, I didn't know that, right? So that's not going to change by adding a CI check.
But I also don't know if… do we have an agents.md? And do we have, like, a clod.md?
**Matt** 07:27 And the cloud just points to the agents in the…
**Tyler Yahn (Splunk)** 07:32 So, is that a failure on, like, the fact that, like, this isn't set up right? Or, like, is there something specific in there that, like, it's…
**Marc Tudurí** 07:39 No, I think it's just Claude, like, decides to ignore it. It's like, People insist to use clothes, so… There's not much we can do. So, either we use linters, or… The markdown file is… It doesn't work.
**Matt** 07:57 By the way, I just wanted to point out this is not a blocking CI check. It's… it's something like, this script will check your PR description, and if it's not right, it will just write a comment, hey, your description is too long, would you please shorten it, or could you…
**Marc Tudurí** 08:16 Nice.
**Matt** 08:17 drop some paragraphs or stuff like that, it doesn't block it. Like, CodCob, for example.
there are PRs which don't,
**Tyler Yahn (Splunk)** 08:26 Yeah, I mean, I understand that.
**Matt** 08:27 But we can just ignore that.
**Tyler Yahn (Splunk)** 08:29 Yeah, that's, I think, my problem with what you're saying, though.
Is that, like… Is this a policy, or is this not a policy?
Right?
Like, you know, as we're talking about in the issue, like, all the maintainers on the call have PRs that would have failed this validation, right? So, we're just gonna ignore it, right? But if you're gonna ignore it in some cases, but not in others, like, you're arbitrarily applying a policy that, like, isn't actually universal.
is.
**Matt** 09:01 Yeah, we do some other stuff, stuff arbitrarily, so we just have to use, I think, common sense.
And when the check fails, we can see, okay, is this a release slop, or is this because it's a release, and it has a changelog in there, and it needs to fail because this.
**Tyler Yahn (Splunk)** 09:22 Yeah. I think that's, like… I'm, like, not okay with that. Like, having subjective, like.
Decision that, you know, we are going to apply a policy or we're not gonna apply a policy arbitrarily is not a great way to foster, like, a welcoming community.
And that's not something that, like, as a maintainer of the project, I'm willing to do.
So, that's kind of like a non-starter for me.
If we wanted to look into ways to help people write better code, or write better descriptions that are more effective to… the reviewers, like, I'm all about that, like, I think that we could definitely do that, but, Yeah, like, that's definitely not something I'm willing to do.
**Matt** 10:07 Good.
**Nikola Grcevski @ Grafana / OpenTelemetry** 10:08 Is there another approach we can take? I'm wondering, can we run something that would… I mean, use an AI agent, I'm not… I'm gonna say the wrong thing here, but use an AI agent to kind of Reduce the spot.
**Tyler Yahn (Splunk)** 10:25 Yeah, I mean, that's actually my idea as well, and I agree. That was, like, where I was thinking as well, Nikola, like, if we could have some sort of, like, agent to help edit this, but the problem is, is that, like, there isn't, like, there's not, like, an OTEL agent, right? Like, and I think that maybe we can try to, like, find that, but… If, like, someone is writing this code and is writing it in, like, an incompatible way with, What we want, like, why don't we just use their agent?
Right? It's kind of my idea. That's where I came back to this, like, Agent.md and Claude.md. And I think that, like, it's a lot easier to say to somebody that, like, you know, you look at their description, and it's not… conforming with syntax, guidelines, it's not conforming with wording guidelines, it's not conforming with all these things, and going, like, yeah, I'm pretty sure you wrote this with an agent, but I don't think that your agent's actually, like, reading this agent's NMD, please, like, you know.
use this Agent's empty. Like, this is actually our policy, this is, like, what we want you to actually do.
And I think that that's a fair thing to ask them to use their agent to write better code, right? Until I think there's, like, an OTL agent that can come back and say, like, hey, this can be improved in this particular way, do you mind if I make this edit for you? Like, that sounds good to me as well, but… I mean, I just don't… that doesn't exist, and I know that there's already an agent in the loop, and that's the user's agent, right? So how do we get the user's agent to do the thing we want?
**Nimrod Avni** 11:46 That's true.
I think it's hard, because… like, we… we also, we already put, like, we have, like, our agent guidelines, and like Macias said, like, you can say.
you know, don't write many comments in the Go code, and you can even give a really, like, fine, like, description of how we expect to write a comment, if it's not a script like Macias did, like, some text-based guideline, but there is no, like.
like, it's kind of probabilistic. It's not even, like… I think in the best-case scenario, you know, an agent, before he writes a PR description, will look at that and try to follow that.
You know, guidelines, but…
**Tyler Yahn (Splunk)** 12:32 Yeah, so, like.
**Nimrod Avni** 12:32 I'm not sure that's gonna happen every time, and if it doesn't happen, then, like, it's on us to catch that and say, like, you know…
**Tyler Yahn (Splunk)** 12:42 Well, I mean, that's… I think, yeah, that is on us, and it's on our reviewers, right, to catch it. Agreed, yeah. I do want to ask that question, though, because, like, I think that people are putting up this, like, little bit of a strawman argument here, because, like, I've used Claude, I've used Codex, I've used… Bunch of other agents, actually. And, like.
I've never had one that ignores this.
You know, I definitely have other repos that it, like, works with, and it will literally not allow you to do certain things.
And, like, I mean, I obviously, like, there's gonna be ways that you can get around that, sure, but, like, I don't… like, there's ways you can get around the CI check as well, right? Like, that's not really, like… those aren't really the people I'm interested in helping here, or…
**Marc Tudurí** 13:23 It might be the counterexample, because every single pull request is violating the rules.
**Tyler Yahn (Splunk)** 13:30 Is it, though? That's, that's.
**Marc Tudurí** 13:31 Yeah, like, like gigantic descriptions with,
**Tyler Yahn (Splunk)** 13:36 There's nothing in here that says anything about that.
**Marc Tudurí** 13:38 Yeah, I added something somewhere, like, somewhere, and I forgot that to be, like… Like, comments should be, like, human-readable.
**Tyler Yahn (Splunk)** 13:49 Comments should be human-readable as not descriptions. That's what I'm saying, Marc. Like, where is the violation that's happening right now? Because I… this is the straw man that I'm having an issue with. Like, people are, like, pointing out that it's violating it, like, where?
**Marc Tudurí** 14:03 I can…
**Nimrod Avni** 14:03 Maybe in the coding guidelines, from what he says, not in the PR guidelines themselves, like, comments in the code, or, you know, uses.
**Tyler Yahn (Splunk)** 14:11 Yeah, I agree. Like, there's definitely comments in the code, right? Like, there's definitely, like, please provide, you know.
Code that… don't, don't over, use comments, right? Like, these are things that I'm actually seeing, but I'm not seeing anything about PR description in here.
**Nikola Grcevski @ Grafana / OpenTelemetry** 14:27 The PR description probably not included, but for me, the agent… I mean, I work with codecs on VS Code. I don't know if my setup is, like, suboptimal or whatever, but it… ignores the agent's MD. I mean, in many cases, I don't know what I'm doing wrong, but maybe it's just my… it's a user error on my side.
I always have to, kind of, if I use it, I have to go back and review the code, and then I ask, no, split that function. Like, that function does, like, three things, right? It shouldn't do 3 things, it should do just one thing each, and then composed, and all these things, and… but, but if you put the effort, that's there, but if you don't, then… people produce, you know, just AI-generated code. I don't know if there… what's the best way to do this. Maybe… We don't have access to Copilot as an org in OTEL, or…
**Tyler Yahn (Splunk)** 15:21 No, like, so, I think you get specifically, like, if you're an org member, you get access to, like, credits, but no, there's not, like, an org, like, co-pilot, no.
**Nikola Grcevski @ Grafana / OpenTelemetry** 15:34 Because I'm wondering if we can actually… if we have an agent that will just point these things out in the review before we even touch it.
I know, like, at Grafana, some teams have added this more in the workflow, but I don't know how I've done it. I think it's probably using something else, maybe even Claude.
But they will call on your PR and say, by the way, you did this, and this is my review of stuff before even humans touch it, and then it just goes in deep and just says, well, that's unclear, this stuff is, like, could be done better, you just, you know, it kind of… Just goes, like, adversarial almost to your code changes to make sure that It keeps… as that first entry to the stuff, but I… without actually having access to a good agent, I don't think we can kind of defend against that.
I hear your points. I think you're making a valid point, Styler, about, you know, being a welcoming community and being overly draconian about what you can and can do. I think, I guess, what we're trying to solve here is to prevent the swap.
Maybe that guy, my 5, whatever, issues open, and 15, and coming in at once, and whatnot, but, Maybe we can…
**Nimrod Avni** 16:49 And, like, I saw what Mark just sent, which is, like, kind of a small, GitHub communication, section about, like, not leaving big walls of text and blah blah blah, but maybe if we try to, like, no, maybe if we try to make it more, like.
you know, not, like, just to send it, but, like, give, like, examples of what's good and what's not, and kind of the same… in the same spirit of what Macias did in the script, but in text, saying, like, I don't know.
We use X now Y blah blah blah blah.
And then, I don't know, we can give it, like, a try run and see if we see less and less of those types of PR, if it improves.
And if not, maybe we can do something that kinda… hard enforces it, and then says, like, point, like, points your agent to these guidelines, and say, implement that, in case they, you know, it's still there, but, like, their agents kind of ignored it.
So maybe we can do some sort of combination with, like, more of, like, guiding agents, how to do it in a more, you know, with examples, what we will accept, what we will not, blah blah blah, and then maybe do some kind of checks to kind of enforce it.
I know.
**Tyler Yahn (Splunk)** 18:08 Yeah, I mean, that sounds great. That's what I'm looking for, that's… yeah, like, something, like, if we could encode… the things that we actually want into this. I would probably expand this to have it actually literally say, like, PR descriptions, and, like.
Give recommendations here.
And then I think, like, if we start to, you know, if we're still having issues where we're getting PR descriptions that are not conforming with what we're looking for.
I agree, like, I think we need to look into ways to, like, automate…
**Marc Tudurí** 18:37 asking…
**Tyler Yahn (Splunk)** 18:38 people who are submitting those PRs to fix it, right?
Because I also think that, like.
You know, as was talked about in the original issue here, like, there's definitely, like, reasons why you wouldn't conform with, like, these very static, settings, right? Like… just released PRs alone are not going to conform with this. Like, PRs that are, like, extremely detailed with API changes that I need a lot of, like, verification. If you were going to be putting in a bunch of, you know, benchmarks on this, right? Like, there are definitely tons and tons of reasons. There's also reasons why, like.
Having one-word PRs or descriptions, or one-sentence PR descriptions is, like, also not really adequate, right? So, like, there's definitely… I don't think that, like, going about it by trying to do some sort of enforcement here, but what you're saying Nimrod is, like, you know, in these particular situations, I would expect to see example A, B, or C, right? Like, I think having AI do that, like, you're gonna get better quality, right, at that point.
**Nimrod Avni** 19:42 at least.
**Tyler Yahn (Splunk)** 19:42 So, I agree.
**Nimrod Avni** 19:43 Like, assuming, you know, most of the agents will manage to follow those guidelines, I'm hoping, because, you know, as I think Nikola said, and I experienced it too, I guess, and maybe some of that, not all the, like, agents and the type instruction are always followed to a T. They may, like, take some inspiration, but you get some slots from time to time, whatever, but… Nikola Grcevski @ Grafana / OpenTelemetry 20:07 air.
**Nimrod Avni** 20:08 I mean, it probably increases the odds of it, I don't know.
**Tyler Yahn (Splunk)** 20:11 I think it's a lot easier to say to that person, like, hey, did you follow this policy, or is this policy being used? Like… instead of saying, like, this is wrong, like, I need you just to completely redo it without any, like, guidance there. I think that that's very helpful. So I agree, like, I would rather go in that direction.
And yeah, like, I think that, like… I don't think it should stop, really, honestly, at, like, the PR description, because, like, I think if we're also finding other things where, you know.
if, you know, it's not in a situation where, like, Nikola, like, somehow it's not reading the agents, like, but it's still not following it, like, then maybe we could try to look into, like, fixing, our agent's policy. Because, like, I don't know what… like, you know, if there are things that we can do better, like, let's do them, I guess is kind of where I'm coming from.
**Nikola Grcevski @ Grafana / OpenTelemetry** 21:00 I think Mark mentioned, you mentioned to me that I had to ask some of these things as a skill or somewhere, like, you mentioned that I should… that it's better if it was added somewhere else.
Because I have to consistently tell it every time before it makes a change. It's like, when you're gonna do this, or work on this.
You have to follow this, this, this to the T, and then I have better success.
**Marc Tudurí** 21:23 Yeah, that's… that's the… the… like, the agent's MD, or, like, the policy for your… For your hardness, like… Nikola Grcevski @ Grafana / OpenTelemetry 21:31 Yeah.
**Marc Tudurí** 21:33 But, like, bye.
I think at least Codex, respects the one from the project, but from what I've seen, Claude.
**Nikola Grcevski @ Grafana / OpenTelemetry** 21:45 So what do you mean if I use Codex directly? Like, as a command… on the command line, or… Because I typically use the VS Code extension, and There, I have to spell out pretty much the policy every time, otherwise it just does whatever.
**Marc Tudurí** 22:01 This I don't know, I don't know, I just… I mostly use the CLI, but, okay.
**Yeah, so… Nikola Grcevski @ Grafana / OpenTelemetry** 22:09 Yeah, some baby people.
**Marc Tudurí** 22:10 I don't know, I think we can try to… I think we can try to refine the agents, and… But… That, my opinion is that it's not gonna help, and… like, I also… today I asked other contributors of, maintainers of OpenTelemetry projects, And they also have… A template, which you can… you have to double-check that you're in… you know… understand the changes, and… But it's like, I don't know, like… In my opinion, we need more linters, and this is not even blocking, it's just informative… comment, like, I don't know, maybe someone… Trust their agents, and then… thinks that they are respecting the Asian's MD, and they open a pull request, and suddenly this… there's a huge wall of text, and I don't know, it's unwelcoming to say… Look, try to make a shorter pull requests.
**Nikola Grcevski @ Grafana / OpenTelemetry** 23:09 In some of the latest PRs that I saw, I mean, we have a linter for no complex goal functions, right? So that checks the goal function complexity, but the PR actually has disabled the linter on that function.
**Marc Tudurí** 23:26 I'm 8.
**Nikola Grcevski @ Grafana / OpenTelemetry** 23:27 I don't know if that was there from before, it just totally moved, but… I mean… It's there in the code, as this… but maybe it can be written better, because it's a switch statement, so it has all these cases in there and whatnot, but… Yeah You can override the linter.
Even if you added a linter, right?
**Tyler Yahn (Splunk)** 23:53 Yeah, you can always ignore them, right? Like, that's… Nikola Grcevski @ Grafana / OpenTelemetry 23:55 Yeah, you can override it, there's no lint something, and if we don't notice it in the code review, it'll just slip.
**Tyler Yahn (Splunk)** 24:01 Yeah. And I think that that's, like, kind of, like.
Honestly, like, the malicious case, like, people that are not paying attention and not, like, Following, like.
policies… there's, I think, little, patience I have with that, but, like, for folks that are, especially new folks, trying to, like, participate in this, like, I definitely want to make sure that they are given the tools. You know, one of the things that, like, Nikola pointed out is that AgentsMD isn't, like, set up, like.
and working for them, like, there seems like there's an opportunity there to try to figure that out, try to help, and try to see if we can, like, change your VS Code settings or change something, because, like.
Yeah, like, and then documenting it for users and saying, like, hey, if you're running here, like, it should just work, if you're running here, it should just work. And then when you start to see these walls of text, which, like, I… yeah, then pointing that and going, like, hey, like, are you using this? Are you not using this? Like… That's actually a policy, and it's a lot easier to say, like, you need to follow the policy, you need to be using this, and if not, then, like, yeah, we can start to set up enforcement.
It starts to become a lot less arbitrary at that point, than just saying that, like.
Yeah, anyways, like, so, I think that, like, I'm really motivated by all of these other, like, suggestions here.
**Roy Reshef (Kubex)** 25:17 Gotcha.
**Nikola Grcevski @ Grafana / OpenTelemetry** 25:17 blah, blah. Yeah, that's right, that's right.
**Roy Reshef (Kubex)** 25:20 Do you want me to show what we are doing with Copilot reviews, internally, of course?
**Again, I… Nikola Grcevski @ Grafana / OpenTelemetry** 25:28 Yeah, if you are.
**Roy Reshef (Kubex)** 25:28 I can show it because… let me share my screen.
**Nikola Grcevski @ Grafana / OpenTelemetry** 25:32 Fair enough.
**Roy Reshef (Kubex)** 25:36 Where the heck is this one? Here.
**Nikola Grcevski @ Grafana / OpenTelemetry** 25:42 It assumes we have co-pilot credits to run.
**Roy Reshef (Kubex)** 25:45 Yeah, that, again, I do not know exactly what, how to… I mean, I'm one of our GitHub admins, so I have access pretty much to everything.
And we have a small enterprise account with GitHub, I don't know, like, 20-something users.
So first, we set a… we don't allow Copilot to approve PRs, but we do allow it to review, and you can even tell it which level to use, And we typically, when it's code, we typically launch a balance. I don't think it is launched I don't remember if it is launched automatically or triggered, but it doesn't really matter, and… The thing is that even when you issue a PR yourself, I mean, you can trigger it. And then… Before you even get to a maintainer approving it.
And, I can show you a few examples here from past PRs, and… Does this one have co-pilot, yeah, so this is a… The review that it does, it sometimes even gives you suggestions to, to fix a code.
And I believe that if you put in an agent.md or whatever else, it would respect it here. Again, I am not the one who set it up.
And, when it makes a comment, I'm trying to find one, when it did make a comment, You can tell it how to fix it, or it can suggest, See, here it made some comment, about my code, and… and you can either accept its own… it gives you a suggestion how to fix it, and you can accept it, and commit it from this… well, this button is now not relevant, but… or you can override it in your own commit if you… and push it back. So there's a lot you can do, as… the person issuing the PR, And, You know, before it gets to a maintainer to review and… I do believe you can instruct it also to look at the description and make sure the description is not an endless wall of text and stuff like this.
**But again, it… Nikola Grcevski @ Grafana / OpenTelemetry** 28:09 It all depends.
**Roy Reshef (Kubex)** 28:10 hands on credits, and I do not know how it works with,
**Marc Tudurí** 28:14 Initially, it's gonna do the same that Macias is trying to achieve, because we have a… I think there is, like.
**a file that you can… it's for Copilot to instruct specific reviews, and we have already Copilot in Inovi, and it's gonna suggest the same, like, maybe your description is too long, and… But the difference is that now we have to go… Every pull request and… and trigger this check, and… Nikola Grcevski @ Grafana / OpenTelemetry** 28:44 Yeah, but at the same time, it also depends on the user that's submitting the PR, whether they have credits or not.
If they don't have credits, this will not run.
**Tyler Yahn (Splunk)** 28:53 Or you have to specifically go in and use your credits, right?
**Nikola Grcevski @ Grafana / OpenTelemetry** 28:56 Yeah, you have to do it for them, and then you're using the credits.
**Roy Reshef (Kubex)** 29:02 I don't know if it's, it's gone on… Again, this setup is different because it's an enterprise setup, but I do not know how it works with open source projects and credits, to be honest. I just don't know.
**Nikola Grcevski @ Grafana / OpenTelemetry** 29:15 Hmm.
**Roy Reshef (Kubex)** 29:16 It goes to your personal credits, or… Nikola Grcevski @ Grafana / OpenTelemetry 29:18 you guys.
**Roy Reshef (Kubex)** 29:18 Maybe you can get as part of the… okay.
**Tyler Yahn (Splunk)** 29:23 But, I mean, I do know that, like, Oh, no. Yeah, I was gonna say Trask has got some AI agent thing running, but he's using… I think his company is sponsoring something later, so there's… I don't think the CNCF actually provides any AI credits, so I think it is all just personal. But, that being said, GitHub, I do… I do think, sponsors any org members.
not a lot, but, like, you're given, like, a certain amount of Copilot-like credit, so, like, every org member, everyone on the call, has… should have, some sort of, like, credits here. But again, like, to Nikola's point, like.
are you using your credits on your PR, or are you using them on other people's PRs, right? Like, it's not infinite, right? So, I think that that's a good point, yeah.
We're coming up on a half an hour, so action items on this?
We need to, I think, maybe go back and look at the AgentSideMD.
**Nikola Grcevski @ Grafana / OpenTelemetry** 30:20 Hmm.
**Tyler Yahn (Splunk)** 30:21 I'm happy to take that action item. Also, Nikola, I'd like to work with you on, like, the VS Code stuff. Like, I've got that set up as well, I just haven't used it in a long time, so I… maybe I can try to figure that out as well.
But, yeah, I'm also happy if somebody else is looking to do the Agent and revising that. Macias, I don't know if this is something you're interested in. You can take the action item as well.
Then I will get a draft going for it then.
**Nikola Grcevski @ Grafana / OpenTelemetry** 30:53 Right.
Yeah, I can help you with that. We can see if why is this gonna work for me, because I think we just… if we had…
**Marc Tudurí** 31:00 If we… Nikola Grcevski @ Grafana / OpenTelemetry 31:01 Go where the people are coming from, in terms, maybe we'll have success at stopping this at the root, before it hits us.
So, if people are using VS Code, like me, with the extension, then they're… It doesn't work for me, doesn't work for them.
They're not paying attention as much as I am.
**Marc Tudurí** 31:22 It's just correct.
**Nikola Grcevski @ Grafana / OpenTelemetry** 31:22 So,
**Tyler Yahn (Splunk)** 31:23 Right. Yeah, I agreed. Let's try to… let's try to enable these people. Agreed.
Okay, jumping back into the agenda, I wanted to jump back, and talk about the… or ask about the blog post. Macias, I haven't seen any movement on this. I wanted to double check. I know we had kind of left it at one of those things where I'm happy to open up a, Google Doc and iterate on this, but I didn't… I didn't, and so I didn't know if I should, or if you're open to collaborating on this.
**Matt** 31:54 No, I actually… so I did it last week, but I forgot to push, and I just pushed.
**Tyler Yahn (Splunk)** 32:00 Oh, okay, alright, so I just missed it, okay.
**Matt** 32:03 Yeah, I completely forgot, sir. Okay.
**Tyler Yahn (Splunk)** 32:06 Cool, alright, yeah, I will… I'll try to get a review on this afterwards, then.
Perfect.
Alright. Next up, I wanted to jump into the V014, milestone, and just double-check that we're… progressing on this. We're… a few weeks, or a week into September.
So, yeah, I just wanted to double-check. So I definitely am looking at this, a few issues in here, I don't know why this isn't scrolling, and I just wanted to ask anyone that maybe has something assigned to them, so that'd be, Nimrod, Giuseppe, Nikola, myself, and Macias.
Oh, no, this is a PR review.
If there's anything blocking you, in that you need some review or you need some help on it.
**Giuseppe Ognibene (Coralogix)** 32:55 For me, only time… I will start on Tokyo tomorrow, I think.
**Tyler Yahn (Splunk)** 33:01 Okay.
Yeah, I could use some of that, too. Yeah.
**Giuseppe Ognibene (Coralogix)** 33:09 I'm able to see.
**Tyler Yahn (Splunk)** 33:10 Yeah, that's my next stop after this meeting.
Cool. And then Nimrod as well, I'm guessing, just time as well?
**Nimrod Avni** 33:20 Yeah, I think it's just, the schema thing is… feels like a rabbit hole, because every time I discover a lot of stuff that we don't conform in. But I think… so, I don't know if you saw, like, I opened, like, many kind of small-ish PRs to kind of consolidate. I think most of it is, like.
Most of the critical stuff that are not, addition, but fixes are merged.
So I'm gonna, kind of rebase… I saw you also commented, I'm gonna, like, rebase and put in all the new stuff from the schema, and, fix your comments, and then I'm gonna put in a review, and I think maybe it's time, like I said, like, after that, unless there's some, like, critical issues, maybe we can merge it and… in worst case, just append stuff to the schema, and I'm gonna… And yeah, and after that, I'm gonna start working on, like, the coverage.
Testing and stuff.
**Tyler Yahn (Splunk)** 34:15 Yeah, okay.
That sounds… yeah, that sounds good. That was my question for you, is, like, if we're getting to a point where we're good enough for that.
**Nimrod Avni** 34:23 But, I think after this meeting, I'm gonna push to, to the 3219, and…
**Tyler Yahn (Splunk)** 34:29 Yeah, this one right here.
**Nimrod Avni** 34:31 Yeah.
**Tyler Yahn (Splunk)** 34:32 Okay.
Well, I will, keep my eye open for it, and then I will try to get a review on that.
**Nimrod Avni** 34:38 Nice.
**Tyler Yahn (Splunk)** 34:41 Okay?
Cool. Alright, moving on, on the agenda. So, Steven, you wanna talk about ARM, coverage?
preferences?
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 34:51 Yeah.
**Tyler Yahn (Splunk)** 34:52 Slack.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 34:53 Yeah, so it's just, I was looking into just putting ARM everywhere, effectively, on all of the workflows to try and get parity between the x86 that we run.
by default, and then, like, we have some partial ARM coverage.
And so there was, like, a… A task to try and get complete parity between the two.
I'm… Someone's got a really loud keyboard.
**Tyler Yahn (Splunk)** 35:21 I think it might be Mark.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 35:23 Oh.
Mark, would you mind going on mute, just for the keyboard? Thank you.
Yeah, so this is effectively to try and unblock all the, all the ARM stuff.
But what I found is, at least for the verifier, workflow.
And this is where we have, like, a whole bunch of different kernels, and we try and boot up a load of, like.
community virtual machines, and we try all these different kernel versions. On x86, this is okay.
But on ARM, the, the ARM runners in GitHub, and I tried all three that they have, plus I also tried the one from CNCF, which is on Oracle Cloud.
None of them have KVM, and what this means is the emulation falls back to much slower TCG.
And it's so slow that the individual kernels Even when they're sharded, can't complete within an hour.
So this, to me seems like, you know, oh, we could… we could run them and hope it would complete in 3 hours, but also it seems like An incredibly long time.
I did wonder about reducing the number of combinations in the verifier, but then you're not really getting the coverage.
I did maybe wonder about using fewer kernels, but then each individual kernel still takes over an hour.
So then I thought, well, there are 3 arm runners.
you know, there's one with Ubuntu 22, and then there's 24, and then there's 26. And, you know, they come with the different kernels, and they happen to be, sort of.
Around, similar versions to what we want to use, effectively, you know, kind of old-ish, Old and newish.
I think, Ubuntu 26 is on kernel 7, for example.
So that at least gives us some coverage. However.
This is much faster, and they seem to work.
But the 22… Runner.
That is already deprecated, and the GitHub are currently removing these.
So, we would lose our older ARM kernel coverage when the 22 runner goes away, and the only alternative is to run, you know, TCG emulation and possibly run a job for, like, 3 hours or something.
And so I thought, well, instead of spending more time trying to work out what we should do with this, I'll just open it to the floor and see, like, is it actually worth it to try and cover, like, older kernels? Should we just run with whatever is available on the GitHub runners?
For example, stick with just 24 in 26 for now.
Or, you know, is it really important that we do try and get specific ARM kernels covered? In which case, maybe I can look at other ways of, you know, maybe we could choose a particular ARM kernel version that's really important to us.
Like 5.10, for example, and then we could maybe make some effort to try and split out I don't know, the verifier combinations across multiple shards or something. But basically, before I spent any more time on this, I just wanted to know, like, is it… is it worth the effort? Should we just stick with these runners that are available?
Or, you know, are the… what's, you know, what are the goals here for the ARM coverage?
**Mario Macias** 38:30 I didn't… No, please go ahead.
**Roy Reshef (Kubex)** 38:35 Did you notice if what takes a long time is a setup of the runners, or actually the run of the tests themselves?
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 38:43 No, so, the setup of the run is… is, pretty fast.
And also, like, I try to pre-compile everything as well outside of the virtual machine, so everything's kind of compiled natively on the ARM runner.
And then we only hand off to the VM for the actual kernel boot, and then running of the, you know, the verification.
So everything before the actual… so all the runner setup is kind of optimized, we do that already.
And then, yeah, so it's just the running of, you know, the verification process. And I believe we run so many different combinations, and they run incredibly slowly. So it's just, like, the emulation and the CPU, the compute constraint here.
It's just… without KVM, it's… it's ridiculously slow. It's like an incredibly throttled virtual environment, that just doesn't have the CPU to… kind of deal with, with what we're running. So that's why, you know, kind of easily hits the hour. So the way that we could kind of deal with that is… You know, for the number of combinations that we're throwing through the verifier, we could, I don't know, try and maybe shard them out to multiple runners and have multiple virtual machines trying to do this. I don't even know if that's possible.
We could try and simplify the verifier in some way, but then you're kind of losing the benefits of having the workflow in the first place.
You know, or we just forget the emulation and stick with the kernels that are available on the native ARM runners, and then you avoid emulation altogether, and then it's effectively as fast as x86, and it works fine.
**Roy Reshef (Kubex)** 40:14 Yeah, that's a… I mean, I dealt with this in… not recently, but in the past, and I… I came to the same thing. Even sometimes compilation, using emulation would take forever.
well, Go you can compile natively, but if you try to do it with… you know, emulation techniques and chemo and the like, it sometimes was just… Painfully slow.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 40:40 Yeah, so we pre-compile, and even… and I know we don't for the verify, but I tried actually pre-compiling the verify tests.
First, and then passing them in.
**Roy Reshef (Kubex)** 40:50 My solution is the time, but again, it's not, that's a solution that you can do as an enterprise. I just spun up some… you know, some ARM… native ARM VMs.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 41:00 Yeah.
**Roy Reshef (Kubex)** 41:01 I want in the cloud, and just have anything I wanted run over there.
But again, you need this, somehow to… to be… So… to report.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 41:11 was around.
There are the CNCF runners, so these, these are the, you know, the org kind of provided… these aren't GitHub hosted, these are effectively self-hosted runners provided by CNCF.
But the ARM runners that we currently have on Oracle Cloud don't have KVM enabled either.
they're effectively the same as what is provided by GitHub. You know, they just come with tons more storage and more compute.
But they… they don't provide the, sort of.
Nested virtualization that we're looking for.
Unless I kind of go to the CNCF and ask them nicely, but that's probably going to be a much bigger effort.
Which I'm happy to do if required, I'm just trying to determine if it's actually necessary.
I don't know, Giuseppe Mario, who had the hand up first. I'm not sure that Zoom provides.
**Mario Macias** 42:04 No, basically, given that we cannot do extensive, I cannot recall any user reporting, verified errors.
That makes me think that… ARM users at currently the… the… the… Smaller group of users.
So… yeah, I will, for example, start with a… kernel version we consider, something that is not too new, but not too old.
and then wait for somebody to complain. So maybe when someone… or we notice the error in another kernel version.
At this other kernel version, and then we see if… In… in the future, we get… Macias runners with KVM, or we can imagine another solution, as Roy said, having our own runners.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 43:05 Yeah, so, I mean, the kernel that comes with Ubuntu 24 is 6.17.
And then Ubuntu 26 is 7.0, so if we just went with those two, you're at least getting you know, a V6 and a V7, but… you know, we wouldn't have the V510 that we do have on x86, and I know that we do have you know, some different code branches, in OB that are targeting older kernels.
And that is the coverage that we would be missing.
On the… on the ARM side.
So that's what I just want to highlight, if that's an acceptable trade-off or not.
I Giuseppe.
**Giuseppe Ognibene (Coralogix)** 43:51 Yeah, so I just want to say that I'm working on a… eBPF verifier, feature, just to reduce the number of combination. And basically, I noticed that, I mean, we currently say that we are supporting 5.8 as a minimum kernel version, but that's not true, because on 5.8, an ARM is not loading anything.
I just did a PR to fix the DNS, and I'm doing another one, but basically, there are a lot, a lot of verified errors, because they are not backported to 5.8 on our…
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 44:33 And, yeah.
Is anybody running?
**Tyler Yahn (Splunk)** 44:37 Giuseppe, can you open a bug for those?
**Giuseppe Ognibene (Coralogix)** 44:40 Yeah, I'm trying to, like, create the full list, but it's too much.
So, I modified theBPF verifier test to report all, all programs that are failing.
But there are very many, many, many. And they are, like, I'm gonna say, it's… maybe the type of bugs are a bunch of, but the number of programs are real a lot.
So… I'm trying to fix it one by one, but I think that if it's too much, I can open a tracking issue and… Yeah.
**Tyler Yahn (Splunk)** 45:20 Yeah, I think that'd be great, just cause… I, yeah, I'd love to have them identified. But anyway, sorry, like, yeah, that's great work, though.
But is it?
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 45:30 I was just gonna say, is anyone actually running 5.8 on ARM?
Because, I mean, we haven't had issues raised.
I mean, we could chase down, you know, every version compatibility matrix necessary.
But are people actually using those combinations?
**Nikola Grcevski @ Grafana / OpenTelemetry** 45:45 I think it's pretty hard, to be honest. Like, how would most people run ARM kernels? Likely on AWS, I know you guys are… I mean, which cloud providers will provide you a server-level ARM chips. I find that usually around newer kernels.
I mean, ARM on Linux is also newer, So… Yeah, I don't know. I mean, if you can probably find some old boards that people are on, but they're not server hardware.
And I think… tend to think, like, cloud vendors do upgrade their main kernels.
**Tyler Yahn (Splunk)** 46:24 So is the suggestion then, like, maybe we drop our compatibility support there?
**Nikola Grcevski @ Grafana / OpenTelemetry** 46:31 I don't know, I'm just saying.
**Tyler Yahn (Splunk)** 46:33 I'm, like, I'm open to suggestions, but I do think that we need to… if we are gonna do that, that's… I'm glad we're talking about it now, because the 1.0's coming up, so if we're gonna jump Something… we should try to do that before then, yeah.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 46:46 It's a good point, because if it's supported, we should probably have coverage.
And then, if we can't cover it, maybe we shouldn't support it.
It's, yeah, kind of go hand in hand.
**Tyler Yahn (Splunk)** 46:58 I mean, that sounds logical to me.
**Giuseppe Ognibene (Coralogix)** 47:01 Can we decide now?
**Matt** 47:02 5.80 LTS kernel, or is 5.10 LTS? Don't remember.
**Nikola Grcevski @ Grafana / OpenTelemetry** 47:08 I think 10 is selfies? Or 15? I don't know. 5'10?
**Matt** 47:12 result, yes.
**Nikola Grcevski @ Grafana / OpenTelemetry** 47:13 Yeah, so 5.8 is not, so…
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 47:16 But LTS, like, Are you talking Ubuntu LTS, or are you talking, like, kernel.
**Matt** 47:23 Yeah, yeah, yeah.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 47:25 It's our own.
**Nikola Grcevski @ Grafana / OpenTelemetry** 47:25 It's only that, because… The other one is 418 that Redhead maintains, but they backboard all the fixes, so…
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 47:32 Right now.
But Ubuntu 22 LTS was 6.8.
Yeah. And, like… Is it still supported?
**Nikola Grcevski @ Grafana / OpenTelemetry** 47:43 Yes.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 47:44 Was it, what, is it, 10 years?
**Nikola Grcevski @ Grafana / OpenTelemetry** 47:46 5, I think?
Yeah, I don't know, we have to check the matrix, though.
**Tyler Yahn (Splunk)** 47:51 I think it's 5, but… Nikola Grcevski @ Grafana / OpenTelemetry 47:53 Yeah.
**Matt** 47:55 Yeah, how about you?
LTS kernels, so there are some companies that are really attached, really affectionate to some kernel versions, and they want to move.
**Nikola Grcevski @ Grafana / OpenTelemetry** 48:04 from them.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 48:06 Okay.
**Roy Reshef (Kubex)** 48:06 Ubuntu 22 is 5 years, it's until April next year.
**Nikola Grcevski @ Grafana / OpenTelemetry** 48:10 But also, within the same 22, they will keep upgrading the kernels, right? So that 22, when it started, it wasn't 6.8, but it was, like, 5…
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 48:18 Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 48:19 15, whatever, and then… They keep pushing, like, with security patches, they upgrade you forward to a newer kernel.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 48:27 So even so, like, with 22 being on 6.8 now, is there any point going older than that on ARM?
**Nikola Grcevski @ Grafana / OpenTelemetry** 48:35 Yeah, I don't know.
**Tyler Yahn (Splunk)** 48:37 Arm? Yeah, I don't know.
**Nikola Grcevski @ Grafana / OpenTelemetry** 48:39 Soy.
**Roy Reshef (Kubex)** 48:39 You have to look at… ARM was pushed heavily by AWS on Gravitone, and I think they still may have Amazon Linux 2 or 2023. I don't know exactly which kernels these are, but those are obviously not the newest.
**Nikola Grcevski @ Grafana / OpenTelemetry** 48:58 Yeah, we need to check what Amazon supports, to be honest.
**Roy Reshef (Kubex)** 49:01 So the only one, I mean, on GCP, you can also get R64… They don't push it as strongly as AWS do.
I don't recall about Azure.
Or other cloud providers.
**Nikola Grcevski @ Grafana / OpenTelemetry** 49:16 I don't think Microsoft has their own ARM hardware. I just don't know how… how pervasive it is.
But Amazon is a really big deal, because you get much better efficiency out of out of the ARM servers.
**Tyler Yahn (Splunk)** 49:30 Yeah.
**Matt** 49:32 By the way, I just wanted to mention that, we are not, like, without coverage for ARM, because we run the PM integration tests on ARM.
I think, starting from 5.10, Already.
It's just that the verifier tests, we don't… we don't run them on ARM, they are slow, because we… we try every combination of everything, so… But we are not, like, fully without coverage.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 50:02 Okay, thank you.
**Tyler Yahn (Splunk)** 50:09 So, unfortunately, Steven, it sounds like you asked for feedback and you got, more questions.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 50:17 Yeah, maybe, maybe, like, if anybody wants to contribute to the thread, or, you know, if there's any ideas, please drop them in the thread in Slack, and I can follow up.
**Tyler Yahn (Splunk)** 50:27 Okay.
And then, compatibility and support, did we want to create an action item for this? Is this something maybe you can look into, Steven, or is this something somebody else has got more context on?
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 50:40 I'm happy to, start the conversation.
**Tyler Yahn (Splunk)** 50:43 Okay.
Yeah, maybe, just open an issue or something like that, or, or, yeah, however you feel the best communication on this one is. I think that makes sense to me, like… Yeah, cause if… if literally no one's using, like, 5.8 with ARM support, we should probably exclude that from our matrix.
Yeah.
Okay.
Cool. And then you can save Giuseppe a bunch of time.
Which he… and he needs to, so then he can go drink his coffee.
Anyways, so, alright.
That's the end of the written agenda.
Any other topics folks wanted to discuss?
I think, I just want to call out again, like, KubeCon, EU, the CFP for that is open right now, I think until early October, if I'm not mistaken. So, if you haven't yet, started thinking about talks for that, which is kind of funny, of course, because, like, KubeCon North America's coming up, but, like.
Yeah, just keep that in the back of your mind. Work, I think that y'all are doing, is worthy of talks, definitely There's definitely places for them at KubeCon for these kinds of things, so definitely think that, you know, just get ideas together. I do know that, like, there's, like, a CFP, like, channel, if I'm not mistaken, in the CNCF, Slack for, like, hotel stuff, if you wanted to run it past people. I think other people on the call.
If you're looking for collaborators, your talk gets accepted a lot better, if you have people from different companies or different, you know, organizations even. So, yeah.
Definitely things to think about.
But yeah, looks like, that might be it. So, yeah, we can probably end the meeting here. Thank you all for joining, it was good seeing you all, good seeing you all coming back. Yeah, and we'll see you in a week's time, or till then.
**Nikola Grcevski @ Grafana / OpenTelemetry** 52:50 Bye.
**Nimrod Avni** 52:51 Never mind.
**Giuseppe Ognibene (Coralogix)** 52:53 Hi, Mike.
