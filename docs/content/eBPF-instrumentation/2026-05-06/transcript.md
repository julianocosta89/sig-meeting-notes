SIG: eBPF instrumentation
Date: 2026-05-06
Duration: 63 minutes
============================================================

## Zoom Recording Transcript

**Giuseppe Ognibene | Coralogix** 00:22 Hi, Mario.
**Mario Macias** 00:24 Hello, Giuseppe!
**Giuseppe Ognibene | Coralogix** 00:26 Hey, how are you?
**Mario Macias** 00:28 Pretty good, thank you.
**Giuseppe Ognibene | Coralogix** 00:31 Alright, it's fine.
**Mario Macias** 00:33 Cool.
Profile…
**Rafael Roquetto** 00:39 Hey, how's it going?
**Mario Macias** 00:41 What are the…
**Rafael Roquetto** 00:44 Bonatard? No, bonatarda?
**Mario Macias** 00:49 Yeah. Bona tarva. Bona tarva.
**Rafael Roquetto** 00:52 Bon comerillo.
**Giuseppe Ognibene | Coralogix** 00:54 Cooperated.
**Michele Mancioppi** 01:00 We're all Latin Mediterrans here? What's going on?
How about it.
**Rafael Roquetto** 01:06 Yeah, pr…
**Mario Macias** 01:06 Hello, Michelle.
**Nikola Grcevski @ Grafana / OpenTelemetry** 01:12 I just couldn't tell. This was Italian, or Spanish, or something in between?
**Michele Mancioppi** 01:17 All of them.
**Nikola Grcevski @ Grafana / OpenTelemetry** 01:18 All of it, all of them.
**Rafael Roquetto** 01:19 Yes.
**Michele Mancioppi** 01:21 The answer is yes.
**Tyler** 01:57 Cool. Let's see, we're about 2 minutes in, but it looks like we have… Quorum at this point, so we could probably jump in here and get started in just a second.
If you haven't yet, go ahead and add your name to the attendees list, and if you have agenda items that you wanted to talk about, please go ahead and add them there as well, and then, yeah, we can jump in here and get started.
Awesome. Okay, welcome, everyone. Yeah, so to… Start us off, Nimrod, do you want to talk about, the OTEL Obi… Ebepf, Profiler collector distribution?
**nimrodavni** 03:03 Yeah, I just, read what your… what you responded, so maybe you can also probably be helpful with this. Some people, specifically in CoreLogic and other places, wanted to… use OB as a collector distribution, and I know that most of, like, the technical blockers, we are now, like, past, and technically we can build a collector distribution.
Not particularly being part of the collector concept, but maybe even just having a separate distribution, like the profiler, that has only OB as a receiver and minimal other, like, components, like only a OTLP exporter, and some extensions, and whatever, So I wanted to know if that's something, like, first of all, is, like, feasible, and you think people will accept if it's just a separate distribution, and if people are in favor of doing… of doing something like this, or maybe even… having, like, combining it with the profiler and having one distribution that's, like, eBPF-centric, like, that you need?
I don't know if you want to run them, combined, for some… Like, mainly because of… you need to give them both kind of similar privileges, or, like, if you want to have one… privilege the container.
Plus, with all the trace profile correlation stuff, Might be helpful to run them both to combine, but wanted to get your opinions on that.
**Tyler** 04:41 Yeah, I mean, I'd love to get a… a collector distribution out, given it's, like, it works. I know that there's, like, other folks that are building their owns and, running their own. So yeah, like.
why this isn't there, I think, is a little bit more on just, like, maintainability, from the collector side, and, like, what they're… what they're looking for.
I mean, I don't think there's any harm in asking if you wanted to open an issue in that collector distribution on this new distribution.
I do think that, like, it's gonna be… Y-y, I think it's gonna be a product discussion, more than anything, from, like, a hotel perspective, like, how are we positioning this, like.
This technology and trying to, like, get users to use it, like… like, do we want a, like, an OE and a profiler collector distribution, plus the profiler distribution, plus, like, the collector distribution?
like, what's the… like, what's the combinations here? And, like, is the long… is the long-term solution to get… OB integrated into the collector, I think is another question, because, like, if that's the case, then… There's… I… I don't think there's actually too much more to… unblock us here other than our, configuration updates, and, we would need to… I guess, that's not true. So we need configuration updates, but then we also need to, like, look at how we're bundling the collector into the, into our package for what I think it's called the collector package, something like that, just to make sure that we're restricting so we don't have a lot of the same overlapping features, is the idea.
**nimrodavni** 06:27 Yeah, I think, like, the main reason we wanted is to have, like, enjoy the couple parts, let's say, of the, like, op-amp, protocol for, like, agent management that… Kinda comes built in if you use the supervisor and all that.
And I've discussed this with, like, some contributors, and there's, like… I think we can suggest both.
And, like, either have only OB, or OB and the profiler, and maybe once we, do, like, resolve all the issues you said with, like, the config v2, and restructure everything to that, we can, I don't know, maybe even be part of the main collector contrib, but… I would love… I see some people have hands if you wanna, Like, Michelle, Michael, wanna talk?
**Michele Mancioppi** 07:18 Okay, Luke.
Nicola, do you want to go first?
**Nikola Grcevski @ Grafana / OpenTelemetry** 07:21 You are first with the hand up. Go for it.
**Michele Mancioppi** 07:24 So, the, I've heard very different opinions about whether either of the eBPF projects.
instrumentation or provider should be part of the, collector contrib build, realistically. In, at KubeCon Amsterdam, the, collector maintainers I seem to be very sat on the fact that People should get comfortable with the, OCB.
To create their own builds.
And I was under the impression that they would not accept out of three, components to be part of the collateral contrib, and they would try to shrink the collateral contrib over time, given the fact that DPF instrumentation lives in literally out of three, so a different repository.
I, I don't know.
**Tyler** 08:16 No, that's not true. We've talked to them. We've had these conversations already.
**Michele Mancioppi** 08:21 Alright, then I just had the wrong impression. The, in terms of security aspect, I think what Nimra said is very valid, I mean.
Probably people would try to reduce the amount of components run with elevated security privileges. So, I can tell you, for example, at our zero, we would, use a minimal Collider build just for the eBPF stuff on the side. We will not mix it with… components, and rather forward, Like, have the collection of the data very thin, and then forward it to… Something else that has many more components inside.
**Tyler** 09:03 Yeah, I think.
**Nikola Grcevski @ Grafana / OpenTelemetry** 09:04 Yeah.
**Tyler** 09:05 your particular situation is gonna be unique, though.
And I think that a lot of people are going to have unique situations on how they want to run it.
And we are continually going to be supporting OB Running as a standalone, in its own situation, like, if you didn't even run it or run it as a collector.
You can also run the collector that has it bundled in with just Obi, and run it just the way you described it.
Like, bundling actually doesn't change any of those runtime, like, properties there.
**Nikola Grcevski @ Grafana / OpenTelemetry** 09:37 Yeah, there's… like, when we opened the issue a while back, I mean, there's… people are in two camps. Some want to have this separate, and they… they want to fine-tune permissions and protect the VPF components, but there's plenty of people that want this bundle.
So I just wanted to say, Nimrod, we do build it for ourselves in Grafana, collector distribution with both components, because we find it, it's, like.
And typically what we ship is just that component, and people can configure it to not give it permissions if they don't want to use the eBPF components. But a lot of folks, like you said, with OPAMP and this stuff being deployed, it's so easy to get when, for a lot of people, it's, like, easy to bootstrap.
Get all signals out.
With no effort, and… A lot of times, you need a collector component if you're gonna ship this data. It's just much easier to… deploy.
especially with additional pipelines to enrich the data, put custom stuff on top of it, so… I… I kind of echo what your desire here is, and I don't know if maybe until… time is that we actually have a separate distribution? Could we build our own artifact that bundles them both and distribute it, or is that against the rules? Like, build it as a community artifact that has collector with these two components in?
**nimrodavni** 11:09 like, both OB and the profiler, you mean? Yeah. I think we can, like, suggest it, and, like, for me, it sounds, kind of the best solution, because it captures both use cases of, like, T1 run.
like, one privileged collector with both Profiler and Obi, you can, and if you want to have, like, you want to separate it, like, based on, like, resources and whatever, you can run, like, one OB and give it the only specific privileges Obi needs, and then one profiler, just enable, disable the receiver.
**So I can… I think that's, like, I think the… people, like, the… most of, like, the collector people at least want those kind of distribution to be as minimal as possible, but just the receivers and, like, extensions and OTLP exporter, that's, like, the bare bones, Like, configuration, but… Nikola Grcevski @ Grafana / OpenTelemetry** 12:06 Hmm.
**nimrodavni** 12:06 I… I can suggest, like, both… directions, see what people, or, like, the contributors and then the maintainers of the collector distributions agree on. I just want to get, like, an agreement between us of, like, does it make sense to do it? And if so, I can open an issue and tag everyone.
**Nikola Grcevski @ Grafana / OpenTelemetry** 12:29 For us, this is extremely useful, I don't know for others, but for us, we… We'd like to be able to just drop this component if customers want to run… enable the CBPF components, they do it, and they… like, there's plenty of them that just go on autopilot, get all the data.
Like, a lot of companies don't have the communication skills amongst the teams, and… or departments don't talk to each other, and people that want to instrument are in the ops department, people that want to build applications are in some other departments, and it's easy to just have something that… they can control through OPAM, deploy, and get the data.
**nimrodavni** 13:10 No.
**Tyler** 13:12 Yeah, my only concern, though, is that, we're adding a distribution To the collector distribution?
Right? Like, that's definitely something that, like, it's added load for maintainers of that.
It also limits the scope. This is, like, gonna be picked up. Like, people… Can't just take the collector distribution and, like.
start running OBI, like, they have to go find a different distribution, right?
I'm kind of wondering, like, what… I'm also worried that you're not going to get a lot of, like, buy-in because we haven't actually addressed any of the things that we said we were going to address.
**Nikola Grcevski @ Grafana / OpenTelemetry** 13:56 Oh, with config?
**Tyler** 13:58 Yeah.
**nimrodavni** 14:01 I think we can still, like, the… if you only run OB, as, like, in the simplest way of, like, OB receiver and exporting to OTEL to, like, a main pipeline. Later, it's kind of the same architecture that, I guess most customers deploy now. They deploy just the OB image.
And forward it to an auto collector. But this has the added bonus of being, like, you can manage it via the OpAMP protocol.
**Tyler** 14:32 Yeah, no, I mean, I get that. Like, the op-amp protocol is pretty great. And there's actually more than that, right? Because, like, you get the whole collector pipeline included into the processing, right? Like, there's a lot of.
**Nikola Grcevski @ Grafana / OpenTelemetry** 14:42 Yeah.
**Tyler** 14:43 running Obi that close, like, there's a lot less… resource allocation, your network is not as loaded, right? Like, there's definitely, like, a lot of benefit.
But it's more about, like.
Yeah, so I, like, I'm not discounting any of that, like, and then I think we all agree that that's the direction we want to go. I think it's also, like, to Nicola's point, like, you drop it in, and, like, it's kind of the autopilot mode, like, you don't have to think nearly as much, it can just start finding things for you.
So, like, I mean, I can't… seeing the benefits of this more than anybody, like, I mean, this is definitely a really cool thing. It's more about the resistance from the collector side, and, like, we've talked to them, they're open to, like, adding this, but they've asked us to do things, right? And so… I mean, I'm open to if you want to, like, go and ask them, but it also then becomes, like, you know, this is not just a collector question, I've had… I've had conversations with, like, the GC as well, because they're… And concerned about, like, what's the positioning of how we want to, like, structure this? Do we want… You know, 5 different distributions of the collector, and like, how do you then resolve telling people how to run things, right? Like… If we have a situation where, yeah, you have you know, a collector distribution with the profiler, a collector distribution with OBM, the profiler, and then a collector distribution, and then you have a user come along and they go, like.
I just want one binary, I just want one thing to run, like, how do I… like, what am I doing here, right? Like, you can't solve that problem, but you can solve it if you bundle it all into one, right? And then you can say, like, well, you can run one version here, one version here, one version here.
I think is… I think it's the… the GC, like, contention here, because, like, they… they get a lot of that kind of stuff talking to users. It's like, well, what's the ease of use for them? Like.
They don't, like, it sounds dumb, but it's, like, it's one of those things where it's, like, hard for people to figure out, like, what's their, like, deployment and operation strategy when you have all of these things coordinating across all of the other things, right?
So… I… I like the idea of getting it out there faster. I don't know if it's gonna happen, though, just based on that collector feedback we have gotten so far.
I don't think there's any harm asking.
I do think that, like, if it's going to, like, hamper our long-term vision of getting it bundled with the collector, I would want to try to focus on that, but… What I'm saying, though, is that, like, if we come back and we say, like, hey, we've actually updated, like, our, configuration story, and we can isolate these things, I think it's a little bit easier of a story to tell these people, like, can we look at this, can we look at that? Like, that becomes a little bit more of a conversation than… Us coming back and going, like, well, we haven't actually done the things we said we would, but can we just.
**Nikola Grcevski @ Grafana / OpenTelemetry** 17:23 But we still had this duration, yeah.
**Tyler** 17:26 Yeah.
**nimrodavni** 17:29 Okay, I think I can, I agree, like, I can… get, like, open the issue, like, discussion, and see if, like, if we can have it as a separate thing, at least for now, and just because of the requirements and the benefit it will give us, until we do whatever we want, like, we need to do, and they accept all our changes, and we have Nothing in duplicate with the collector and all that stuff.
And then we'll be part of the main, collector distribution, I'll see if it's something that they agree, and if not, I guess you just, like, each one will need to build their own distribution or something.
But until we reach the point that we're, like, stable and they are fine with letting us in the collector.
**Tyler** 18:16 Yeah, so stability wasn't the prerequisite, remember? It's just…
**nimrodavni** 18:19 That's the ability, yeah, what you… Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 18:22 Like.
**nimrodavni** 18:23 being modularized, like, modularizing components to be only the core of what we need, of, like, not duplicating anything, yeah.
**Tyler** 18:31 Right, right, yeah. And I think that, like, Yeah.
I honestly don't think that that's too far away. I think it just takes, like, unblocking people's development effort to get it done, so, Yeah, Blitz.
Let's keep going on that one, I guess is my goal, yeah.
**nimrodavni** 18:51 Cool. Well, thanks.
**Tyler** 18:53 Cool.
Okay, next up, Rafael, you wanted to talk about hardening the AI policy? Yeah.
Go ahead.
**Rafael Roquetto** 19:03 Yeah, well, the… We already have the policy on agents.md and other files, scattered across the repo?
And… it was still not, like, really solving the problem, I guess, or problem for me, at least.
Which is, like, yesterday, for instance, I got a 1PR out of many.
That was, like, 100% AI-generated, and… while we do encourage the use of AI, I use it every day, I feel like PRs like that, the person doesn't understand what they're doing. Like, it's the AI.
we all… I think we've all been there, seen that… something like that before.
So I… and it wasn't, like, a huge… like, the actual PR description was larger than the actual code changes. It was about JSON RPC or something like that.
And, when I looked at that, and I, like, we had maybe because… 3 or, two or three JSNRP CPRs, like, in parallel, going from different people who kind of raised the same or related things.
So I looked at that, and I thought, hmm, I'm not going to… Revealed that… Before doing, like, a first co-pilot pass, just, you know, just to filter it out.
So I added Copilot, Copilot left some comments.
And… and then… I did take a look afterwards, and it was like… Yeah, a lot of… all generated code, but I think if the person had at least pointed their AI agent to, or, like, AI.agents.md.
you would have generated better code, like, more towards what we agreed on those instructions and those files. So I kind of suggested, hey, like, I haven't reviewed this yet, but if you want to point your agent to this, you know, and do another pass, and also address the co-pilot.
Comments and whatnot.
And the person started, like, to basically respond with AI, like, huge AI comments, some of them were nonsense, they're completely like, we'll run a test when FSCI goes green. It's like, what?
It's, like, nonsense, nonsense, Yeah, so… all of these I could see there was, like, AI-generated responses, and that kind of pissed me off a bit, because, like, I was taking time to at least look into it, and didn't deep dive into it. It was a simple… PR, but So I was like, start pointing the policies to this person, saying, hey, check this out, you gotta under… like, the policy says you have to… you can use AI, but you have to understand the code, you have to, you know, otherwise, how do we have confidence?
That we know what they're doing, and once you have one PR or two PR, that's okay. But we're being flooded, so we have, like, I don't know, 10 PRs coming in, how can we tell apart, okay, this is actually the person, know what they're doing?
And… this is just, like, some guy that is a bad proxy for, you know, cloud, or ChatGPT, or whatever they are using, because I start… the guy then answered some of my questions I raised with a cloud plan, at which point I was like.
in our policy, we say that you… the contributor is expected to vet the PR, not us. So I pointed it on, and I closed the PR, because I got grumpy, and it's like, this is… this makes no sense. In… As a counterpoint to that, we had another PR, that the guy… I think he was also… it was the same JSON RPC, or related to that, kind of using AI?
But unlike this first person, the second person is like.
putting some effort to at least dialogue with us. The PI was really good, I think he got merged, you know, so AI is not the problem, in that sense.
So I was wondering.
if this can continue as a trend, how do we kind of manage this? And I… I mean, what I… I was wondering is the first, I guess, on the front line, the first thing we could try to do, and I don't know if it's possible, is it… somehow get Copilot or something to actually flag those PRs, so basically what we have now is now being read by Copilot. Agents.md, or the Copilot instructions.
So that, you know, fight AI with AI, if that makes sense. I don't know if that's possible, if that's feasible. Copilot doesn't seem to work very well with the instructions. So usually when I do review a PR and I want to review it based on our, like, guidelines. I will actually get my own agent and point it to the gate lines and said, help me review this PR with these guidelines. So I wonder… first, I wonder if there's something we could do with Copilot, or… I don't understand that very well, how it works. I can research that if no one knows.
To kind of filter that out.
and then… See the results of that, and if that doesn't yield anything fruitful, I wonder if we should at least bend, or not bend, maybe is a strong word, but Well, I guess you guys know what I mean, like… constrain a lot interactions that are AI-generated. So, like, we can still accept AI-generated code, but at least when you're discussing on the PR, we kind of… don't paste a cloth plan there. You know, if I want a cloth plan, I can just go and point my own clothes and say, help me understand this, generate a plan for this. I don't need someone to do that, so… Yeah, I don't know what you guys think, if… Maybe banning that… at least comment… PR-generated comments would kind of make people think a bit on what they're doing, and even if they go to their AI agent and then try to tweak it, at least it makes them think a bit and go back and forth and understand what's being done.
I don't know.
**Tyler** 25:16 Yeah, so… First off, world-class rant right there, that was pretty great. I really loved it.
**Rafael Roquetto** 25:23 Sorry.
**Tyler** 25:25 No, I, I'm not, I'm not, yeah. And I, I think, I think you're, you're right, like, I mean, I don't think you're right, you're right. Like, if somebody's putting zero-effort code into their part repository, whether they're using AI or they're using anything, like, that's not acceptable.
Right? So, yeah, I think you should, first off, feel empowered to do what you did and close the PRs. Like, nobody's… nobody's coming after you for doing that. I think that was the right move. Probably should have done it earlier, is the only thing I would say.
I think that… yeah, Nikola and I were talking about this as well a little bit yesterday, like, there's, I think, appetite for people to try to, like.
get involved in these projects, because they see them as valuable, and, like, I think that that's fine. It does require a basic level of skills, though, right? Like, it does require the ability to communicate, like you're saying. It does require the ability to, like, read and review your own code, whether that's through tooling or whatever, right? Like, so, Yeah, I think you come up with a lot of really good suggestions there. I think that you can try to make that policy clearer. I think you might also want to take a look at, there's a… there's a… maybe I'll post a link later. There's a survey… something like 5 years ago, 4 years ago, on, like, open source maintainers, on, like, their day-to-day, and, like, one of the hardest things that they've come to find is, like, saying no.
And it was a really interesting, like, post on this, because, like, what you think you're struggling with more is not that… The fact that… there was bad code, it's how to tell somebody, like, you need to stop, like… That's… that's usually the harder part, right? Because it's a lot harder to, like, distinguish that and then get it wrong, and you don't want to, like, discourage people in the community.
And I think that you're struggling with that right now, so, it's a tough one. So, yeah, I think whatever tools you want to come up with, I'm in favor of. You've done a really good job so far.
I did link a, interesting thing that I saw the other day, I don't know if you've been following Open Claw at all, but, the author of that also came up with his own thing called Claw Sweeper, which is kind of like its own agent, which does exactly what you're talking about. He's of the same opinion, he can… He has a nice paid subscription to all of these OpenAI AI agents, and, like, there's no reason for a free-tier AI agent to be posting code there that is total garbage, right? Like, so… you need humans as well, and so he's done heuristics using AI to try to, like, do these sort of findings.
I don't know of anything in the open source world that we could set up as, like, a CI or something like that, but, like, I think we could look into maybe something… On that, on that field.
**Rafael Roquetto** 28:05 I will… I will look and see if there is any way to make Cloud work better, Cloud, sorry, co-pilot. If… a good start would just… just be, like, flagging our policies, because then it works as, like, a… it forces the person to go, and to your point of… like, discouraging versus not discouraging. Yeah, that is, I was thinking about it yesterday, like, because I saw people coming to our, like, Slack channel, and they actually want to understand the code. They're asking for guidance, and I think this is the kind of contributors we want. So, that's why… one of the reasons why I didn't just close the PR, even though I looked at it like I felt like doing it, is because I'm gonna give this guy a chance. Like, let's try to engage the conversation, because I don't mind… helping, you know? But if you have, like, multiplied that by 10, then it just becomes noise, and maybe… not… some of these noise is gonna, fall through the cracks, land in our codebase, and that's when the code starts to rot, basically. So, we need… otherwise, there's no point on code reviews. They just let people merge. That's… So yeah, I would maybe then look into these, if anyone has any other suggestions, that we could… You know, pursue, or… or maybe, you know, we revisit this in a month or two, see how we fare, because maybe we're touching the policies, just make them very explicit.
Yeah. That's all for the rent.
**Tyler** 29:37 Yeah, no, it's good. But yeah, let's… let's keep following up on that, because, like, the last thing I want is for you to get discouraged due to… due to this. Like, that's not ideal. So, if we need to build more tooling and put more thought into it, then let's… let's do that.
**Rafael Roquetto** 29:52 Okay, I'll look into it.
**Tyler** 29:53 Yeah.
Okay, jumping back in here, let me start, sharing my screen again.
Cool, I wanted to check in on the next release. This is an interesting one. I think we're… We've got a lot of really cool things going out. I was just looking at some of the things, it's pretty, pretty extensive. A lot of the Gen AI stuff is going to be going on in this one as well, so yeah, I'm pretty, pretty excited about this.
I am wondering what's left. We also have some, like, security patches we're working on as well. There's, I opened a ton of bugs yesterday, so yeah, those are not included in this release. There's definitely, I wanted to scope this into, like, what we've already accomplished, and then maybe stage a lot of other, like, fixes into the next one.
But I did want to ask, like, what is in flight that people maybe are trying to get into this next release? For reference, I want to try to get this out maybe the end of this week, so Thursday or Friday. So, if you can get a PR merge, I guess that's the idea.
Is there anything we should look at here?
speak now, or for… For about a week or two, hold your peace.
**Nikola Grcevski @ Grafana / OpenTelemetry** 31:13 Maybe… The only thing I'm thinking of, if we… since we're doing a lot of work on the GNAI, But I don't know if the author actually pushed the fixes, I haven't checked.
So Ishan found a number of issues with our GenAI SEMCOV.
So, he put up a PR, Too aligned, but there's issues.
I commented on a few things, so… Okay.
Yeah.
I mean, it's good, but I think it can be better. I think there's some missing tests. He's trying to normalize the responses, similar to what Hybean did for the embeddings.
To make sure the mattress understood the… But, yeah, I can't predict, when Isha's gonna have time to follow up on this.
**Tyler** 32:07 Okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 32:08 But…
**Tyler** 32:08 Do you only know Ishan through this PR, or do you know them.
**Nikola Grcevski @ Grafana / OpenTelemetry** 32:11 No, no, he's not his girlfriendista, so I can ping him, so perfectly ask him, yeah.
Okay. That isn't not in our team, or, yeah.
**Tyler** 32:21 Yeah, I'm happy, like you're saying, like, to add this to the milestone, try to get this in.
**Nikola Grcevski @ Grafana / OpenTelemetry** 32:26 I'll message him today and see.
**Tyler** 32:28 Okay.
Cool. Yeah, that'd be great, yeah.
Okay, yeah, any others for folks?
Nimrod, I know you have a few PRs, maybe…
**Giuseppe Ognibene | Coralogix** 32:43 Tyler, if… if you're looking for some PR to… to merge.
There are two, there are mine. Number… 58… Okay.
**Tyler** 33:00 This one here and this one here? Yeah.
**These are, yeah, we've got an approval… Nikola Grcevski @ Grafana / OpenTelemetry** 33:11 I don't know if Matt's here.
Right.
**Giuseppe Ognibene | Coralogix** 33:15 F.
**nimrodavni** 33:16 Bye.
**Tyler** 33:16 Yeah, not here.
**Nikola Grcevski @ Grafana / OpenTelemetry** 33:18 He's not here.
**Tyler** 33:19 I see him working at, like, 4AM sometimes, I don't know.
**Giuseppe Ognibene | Coralogix** 33:24 He's in Italy, but he's not in Italy.
**Nikola Grcevski @ Grafana / OpenTelemetry** 33:28 Okay.
It's a guy that never sleeps, in my opinion.
**Tyler** 33:33 God, man.
**Rafael Roquetto** 33:34 It's amazing, right? You message him, he's just like, hey! He's like, dude, it's 8pm for me, what time is it for you?
**Nikola Grcevski @ Grafana / OpenTelemetry** 33:41 That's…
**Tyler** 33:41 Yeah, exactly, right? Like… I, I, yeah, I admire his dedication. I, I just have… I will add this to the milestone.
**Giuseppe Ognibene | Coralogix** 33:50 Okay.
**Tyler** 33:50 And so it'll… if it… Mattia doesn't respond by the time that I'm looking to get the next release out, I'll merge it, but… Otherwise, I'm just gonna wait until… see if Mattia, can respond to this. But otherwise, yeah, this looks… looks ready. If others… if others want to take a look as well, one more review, I think we could probably just merge it without Matia's feedback.
**Giuseppe Ognibene | Coralogix** 34:11 Thank you.
**Tyler** 34:12 And then this one as well, Giuseppe?
**Giuseppe Ognibene | Coralogix** 34:15 Yep.
**Tyler** 34:16 Yeah, this one looks like it's also got a… I wonder if you… Nikola Grcevski @ Grafana / OpenTelemetry 34:19 Yeah, it was on my list this morning to review it.
gone to it yet.
**Tyler** 34:26 Well, if that's the case, I'll wait for Nicola to take a look, or other people, if they're looking as well. But it's added to the milestone, I won't forget it as well.
**Giuseppe Ognibene | Coralogix** 34:35 Thank you.
**Tyler** 34:36 Yeah.
Any others?
**nimrodavni** 34:43 I think I have mostly documentation stuff. I think, urgent.
**Tyler** 34:49 Yeah, I thought… By the way, thanks for doing all that, that's… it's been really helpful.
Oh, I thought this merged.
**nimrodavni** 34:59 I think there's, like, a couple… there's, like, I opened it in 3 different, repositories.
**Nikola Grcevski @ Grafana / OpenTelemetry** 35:04 Okay.
**nimrodavni** 35:05 Indeed.
**Tyler** 35:05 Oh, okay.
**nimrodavni** 35:06 The website, and the Helm chart, and this.
**Tyler** 35:10 Okay, yeah, I think I just missed this, oh, no I didn't.
**nimrodavni** 35:16 I think… I know there's something left for me to fix, I don't remember.
I think I addressed most of it.
**Tyler** 35:23 No, this… I… I think you did.
They look all outdated. Okay, yeah, I'll… this is on my list then, I need to take another look. Let's add this.
**Nikola Grcevski @ Grafana / OpenTelemetry** 35:32 Mario as well, I don't know. If Mario… He's mentioned, I believe.
noise.
You requested him, or… Hey, there's.
**nimrodavni** 35:43 Or if you just responded on something, and I… Nikola Grcevski @ Grafana / OpenTelemetry 35:45 Okay.
**Tyler** 35:46 I think he's… yeah… Two weeks ago. Wow, okay. Yeah, this just fell through the cracks.
Okay, yeah, I'll take another look. Oh, it looks like there's merge conflicts, too. If you can handle those, yeah, then let's try to get that one.
**nimrodavni** 36:01 Hmm.
**Tyler** 36:02 Do you not review, okay. Improvements to the Weaver schema tooling, as well.
**nimrodavni** 36:07 You know.
**Nikola Grcevski @ Grafana / OpenTelemetry** 36:08 This morning, as well.
**Tyler** 36:10 Yeah.
**nimrodavni** 36:11 trying to… cover all our tests with, like, semantic convention stuff, and the other PR is, like, 100 files, but most of them are, repetitive, so I try to, like, get all the logic stuff here, and then the other PR is, like, 100 files, each of them is, like, a minor change.
Okay.
**Tyler** 36:31 Yeah, so this is, before the other, Weaver one we just saw. Okay, so this is a priority.
Is this, need to get out in this next release, or is this just not a… No.
**nimrodavni** 36:41 It's not like… it's only, like, integration test, improvement.
**Tyler** 36:44 Yeah, okay, okay, cool.
I'll still prioritize reviewing, just won't add it to the milestone.
Okay, any others?
Steven, did we merge the, I think we merged the daily report PR, right?
**Stephen Lang** 37:04 There's a… there's gonna be a few more coming. There's a couple more, but, yeah, I had a long weekend, so I'm… practically been out since the, the last six.
**Tyler** 37:14 Yeah, no worries.
**Stephen Lang** 37:15 Yeah, I'm gonna do a few more to just improve the accuracy of the numbers.
Start doing weekly roll-ups, and do some prep work for a monthly roll-up as well, so that there'll be a few more coming.
**Tyler** 37:27 Awesome. Yeah, that's exciting.
**Nikola Grcevski @ Grafana / OpenTelemetry** 37:31 Yeah, I had a question here, maybe it's easier. I wanted to ask Nimrod, just to get a… kind of, like, a green light from him. So… We're gonna create an optional attribute for the error message.
response, from things and make it off by default. Are you cool with that, or… I mean, it could be enabled in a config, so you can bring it back, but just, To kind of be more in line with what the other SDKs are doing.
**nimrodavni** 38:01 Yeah, makes sense.
**Nikola Grcevski @ Grafana / OpenTelemetry** 38:02 Yep.
**nimrodavni** 38:03 It's, like, the same as, The, like, the DB.
**Nikola Grcevski @ Grafana / OpenTelemetry** 38:07 Yeah, TV query text, yeah, it would be, like, error attribute or something, whatever, is the right name. I don't… haven't looked, but…
**nimrodavni** 38:16 Yeah, we just need… because it's not… it's not actually an attribute, so we need to, like.
**Nikola Grcevski @ Grafana / OpenTelemetry** 38:20 Yes, we all added in attributes, and then I'll make sure it follows the exact same thing as the dbQuery text.
**nimrodavni** 38:28 No? Yeah, I'm on board.
**Nikola Grcevski @ Grafana / OpenTelemetry** 38:30 No, okay, cool. So I'll prepare the PR tomorrow. Sorry, today, so hopefully, yeah.
**Tyler** 38:37 Cool, right, yeah, and we talked about this. We want to get this in as the next release, so yeah, that sounds good. I'll make sure it's in the milestone, so yeah, that sounds good.
**Nikola Grcevski @ Grafana / OpenTelemetry** 38:44 Yeah, cool. It's coming.
out time yesterday. Yeah.
**Tyler** 38:49 I think we could all be a little more like Mattia, is what I'm hearing.
**Nikola Grcevski @ Grafana / OpenTelemetry** 38:52 Yeah, work at 4am? No.
**Tyler** 38:58 Cool, alright, well, if that's the case, the last thing on the agenda is to do just a PR review. We've gone over a few of them, but we can… we can just jump through again, so I'll open this back up and… Awesome.
**Nikola Grcevski @ Grafana / OpenTelemetry** 39:18 Yeah, I put it there, because I don't know, we have a lot, 30, I don't know if a lot of them are just automated, but… We catch up.
**Tyler** 39:27 Yeah. That being said, we've actually been… Merging a ton lately.
**Nikola Grcevski @ Grafana / OpenTelemetry** 39:33 Which is… Oh, God.
**Tyler** 39:34 really inspiring. We're getting a lot done. But yeah, I think this just might be a part of the project growing a little bit. But, yeah, let's do some cleanup here.
**So this, I think, is still… not been touched. I think this is something… Nikola Grcevski @ Grafana / OpenTelemetry** 39:47 Yeah.
**Tyler** 39:48 Was it you or Mario who's gonna take a look at this?
**Nikola Grcevski @ Grafana / OpenTelemetry** 39:50 Yeah. I believe I fixed this, but… It needed somebody with a Mac, which I don't have.
But I believe he was trying to implement the same thing I did, which… with the multi-platform build. Maybe we can ask him if that is actually… Oh, Steven, you still reproduce it with May? You can't build it?
**Stephen Lang** 40:12 Well, yeah, but this is probably stale now, because I think this was before the, the multi-platform Java build you did. Java support, yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 40:21 So let's confirm if that's fixed now, then… I think we should just…
**Stephen Lang** 40:26 I don't know, I think this PR should be closed, and maybe, I don't know if there's an issue associated with… Nikola Grcevski @ Grafana / OpenTelemetry 40:33 No miscompass.
**Stephen Lang** 40:34 compatibility.
But I can just go ahead and test it anyway, Nicola. I'm pretty sure I tried this the other day and it didn't work still. It complained about some JNI issue.
**Nikola Grcevski @ Grafana / OpenTelemetry** 40:45 Yeah, but, I mean, I don't have a Mac, so I don't know how you guys built this, but I did test, I have an arm.
Linux box.
worked, so.
**Stephen Lang** 40:59 Yeah, well, I mean, I can try it and, let you know how it goes.
**Tyler** 41:05 Yeah, okay, that sounds good. And then we'll just open and issue the track if it doesn't work. I think it's probably a better way to do that, instead of PR here. Yeah.
Okay, cool. Configv2, this is, another big one. Actually, maybe I'll ask you about this one. I know Nicholas approved this, there's a lot of other reviewers on this. I think that this is still ready for review.
I'm happy to split this up into smaller things, or remove files, or something like that, if there's feedback like that.
But I am trying to get this one across the line, so… any sort of feedback on this would be great, and I'd like to move on. I don't want to just… merge this.
with one review, it's a pretty big change. I definitely don't want to merge it right before a, a release.
So, yeah, I guess… Can I get some, like… I actually, maybe just now, like, are there people that are still looking at this, or is this just under the radar?
**nimrodavni** 42:05 I'll try to get a… review it as well. I think I kind of missed it after my initial one, but I'll go ahead and do it.
**Tyler** 42:13 Okay.
Yeah, that'd be.
**Nikola Grcevski @ Grafana / OpenTelemetry** 42:15 It could be helpful. I could ping Mario as well, if you like.
**Tyler** 42:19 Yeah, that'd be, that'd be helpful.
More eyes.
**Nikola Grcevski @ Grafana / OpenTelemetry** 42:22 social proof, yeah.
**Tyler** 42:23 I think I have addressed all the comments, but if I missed them, please point them out.
I definitely addressed Dimitri's comments, so yeah.
take a look. Also, if… like, there's… there's a lot of, like, minutiae around this. If people just want, like, a new… schema definition, like, I'm happy splitting this up, like, I had a lot of validation around this, and, like.
proving things, that I don't want to, like, block the review, that I can… I can pull out into another PR as well, so… just, yeah, let me know.
Okay.
The Kafka stuff… Yeah, this is a tough one. I think this is one where we looked at it, and we were wondering if we should just close these, because there's, like, testing matrix compatibility, like… I haven't gone back to look at this, but, like, essentially the V8 tag here is a duplicate of another integration test that already tests this V8 tag, So it's wondering if, like, this actually is even needed, but I just haven't gone back and taken a look at this. So, it just needs, I think, somebody to definitively say, like, we want to go this direction or not.
Selectively replacing tracing programs if the system supports them? Still a work in progress.
I'm guessing Mario's still working on it, so we'll just leave it there.
Update Docker… update Docker Major. This probably just needs to get ignored. This needs to get shepherd in. It's still on my list of things to do.
**the POC supporting linking spans connected, with Go channels is, probably needs a pretty big rebase at this point, given I think we just did a lot of, changes for… Nikola Grcevski @ Grafana / OpenTelemetry** 44:11 Yeah, the GO tracing, yeah.
**Tyler** 44:13 Yeah, okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 44:14 Or…
**Tyler** 44:14 that's still there. But, I did ask for feedback last time, and I think it was Matti and others said that, like, they would be interested in seeing this getting cleaned up and turned into a real PR, so that's just on me. I haven't done that yet. I think that this is a good proof of concept.
**for not supporting Select, but just supporting, like, direct channel, Nikola Grcevski @ Grafana / OpenTelemetry** 44:33 Communication.
**Tyler** 44:33 so… I think this is a good place to start. Let's… let's… I'll try to put this on my agenda for, The next milestone, and replace it with something that is actually going to be mergable.
So, yeah, let's do that.
**Nikola Grcevski @ Grafana / OpenTelemetry** 44:48 Yeah, let me know, do you want me to take a look as well, or… I'll read it.
**Tyler** 44:52 Yeah, if you would like to take a look, I… my… my subtle goal on you taking a look is I would nerd snipe you, and then you could just even do a better job than what I did. But yeah, like.
**Nikola Grcevski @ Grafana / OpenTelemetry** 45:03 God.
**Tyler** 45:04 Yeah, if you want to take a look, please do. Obviously, I had, like, it was a working concept, but I don't know if it's, like, ideal. So yeah, the feedback that you could provide would be great, so, yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 45:15 Cool. Yeah, I… it wasn't on my radar because it's draft, I wasn't sure if I should be looking at it, but I'll take a look, yeah.
**Tyler** 45:21 Okay.
Yeah, I think… I think the consensus last time at the meeting was that we want to move forward with this, so let's try to… yeah, if you want to give a feedback, and then I will try to… or one of us can try to move this into a real PR.
**Nikola Grcevski @ Grafana / OpenTelemetry** 45:33 Yeah, probably while I was at that conference, yeah.
**Tyler** 45:36 Yeah, yeah, yeah, exactly, yeah.
Okay, cool. This is also.
**Michele Mancioppi** 45:44 I have a tiny question, given the PR description that confused me. What do you mean, reciprocal span links?
**Tyler** 45:53 Sorry.
**Michele Mancioppi** 45:54 You go with the PR that you were discussing about the linking of spans.
**Tyler** 46:00 Yeah.
**Michele Mancioppi** 46:01 Their description, there is, when you go to the behavior, and there is this big sample.
It says, reciprocal spandlings.
**Tyler** 46:14 Yeah, and this… The sense that, like, both the sender and the receiver are now going to have links on their spans?
**Michele Mancioppi** 46:22 So, they link each other?
**Tyler** 46:25 Yep.
**Michele Mancioppi** 46:27 I've never seen anything like this. Usually, it's the server that links to the client, not the vice versa.
**Tyler** 46:33 That's usually because the client can't understand the server span.
Like, right, that doesn't have the context of the service fan? Yes. It's on a completely separate.
**Michele Mancioppi** 46:43 I know some backends of a break, you know, cyclical dependency, but… Are you sure that you want to do this?
**Tyler** 46:51 No? No. This is just a proof of concept. This is how it was working, yeah.
**Michele Mancioppi** 46:57 I… my advice would be only the server points to the client, not vice versa as well.
**Tyler** 47:02 Yeah, it's a little tough to figure out which one's which, but… that's… also could be server-to-server, even. This is more to trace across Go routines, so it's not necessarily, a particular.
**Nikola Grcevski @ Grafana / OpenTelemetry** 47:16 Yeah, hierarchy.
**Tyler** 47:16 structure, yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 47:18 Hold on.
**Michele Mancioppi** 47:20 Okay.
**Tyler** 47:22 But yeah, we can take a look at this. Shows up in Jaeger, which is where this is tested, but yeah.
**Michele Mancioppi** 47:30 Yeah, I mean, Jaeger effectively just gives you an HTTP link to the other span.
To do, draw some backends that are performing algorithms on the stretch of the trace, and although they are no longer trees.
Thanks to the span links, there still are a latex, so there are no cycles. But this introduces cycles.
**Tyler** 47:52 Yeah, it would, yeah.
Yeah, if you want to comment, please do. Yeah, love all the feedback.
**Michele Mancioppi** 48:02 Siobhan.
**Tyler** 48:05 Okay, cool.
So moving on, the gRPC support, this… I feel bad I haven't taken a look at it. It looks like Rafael also is on… Taking a look, and there's been…
**Rafael Roquetto** 48:19 Yeah.
**Tyler** 48:19 So, it looks like it just needs more reviews, right?
**Rafael Roquetto** 48:22 Yeah, yeah, he just posted an update this morning for me, whatever time it was for him.
And it seems that he's solved. I haven't had the chance to look into it today yet, but it's… from the common sense that he fixed most of the painting stuff, so hopefully that will be it. I will take another, look at this today.
**Tyler** 48:43 Yeah, yeah, same.
**Rafael Roquetto** 48:44 It's… it's getting there, yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 48:46 It's going there, yeah, it's gonna be huge.
**Tyler** 48:48 Should we try to wait on merging this until the next milestone?
**Nikola Grcevski @ Grafana / OpenTelemetry** 48:56 Yeah, no, I'm 9, let's release 9 without it, and then… Let's do some testing, let it cook a little bit in Maine.
**Tyler** 49:03 Okay.
Cool.
Rafael, also a work in progress, new socket tracer. I'm guessing we don't need to dump any of that.
**Rafael Roquetto** 49:15 Be a work in progress, yeah.
**Tyler** 49:17 Cool.
**Rafael Roquetto** 49:18 I did hear, like, from a guy that it's increasing CPU usage by a lot, so… it's… all my, like, the background tasks I've been doing, I actually want to wait for Matthias, JRPCHCP2, like the previous patch, to be merged, because I will incorporate that into this, so… after that gets merged, maybe I'll… I'll speed things up on this.
Sock Tracer.
**Tyler** 49:42 Hmm. Okay.
Cool, alright. Document the Cates cache, also something we need to take a look at, this just got stale. I'm on the hook on that. Same with, Mario.
**update Java, again, just needs a maintainer to come take a look at this, and baby… shepherded along. Our updates are pretty big, so, yeah. I haven't actually jumped into this one. I jumped into the last one, but… Nikola Grcevski @ Grafana / OpenTelemetry** 50:11 What broke?
**Tyler** 50:13 It's always breaking.
Oh, this might just be a notice update, actually.
**Nikola Grcevski @ Grafana / OpenTelemetry** 50:20 Probably notices, yeah.
**Tyler** 50:22 Yeah.
Yeah, looks like it noticed updates.
**Nikola Grcevski @ Grafana / OpenTelemetry** 50:27 Okay.
**Tyler** 50:29 Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 50:30 That's amazing.
**Tyler** 50:33 I feel like I had it a command here.
I kind of wonder if I could… yeah, I'll have to resurrect the command and see if it works. I totally forgot the command, I haven't used it in a while.
But it might just be that… yeah.
That might just fix it. Okay.
Next up, Florian's got another draft.
Steven as well.
You know, skip over those, because they're still a work in progress.
Fix, JSON RPC span name. This is, I think, one of the PRs that Raphael was talking about earlier.
**Nikola Grcevski @ Grafana / OpenTelemetry** 51:06 No, I think this one's okay, I believe.
**Rafael Roquetto** 51:09 Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 51:11 I think you and Raphael wanted some changes in the way that it's done.
**Tyler** 51:16 Oh, it's a different one. Yeah, okay, yep, yep.
**Nikola Grcevski @ Grafana / OpenTelemetry** 51:20 Yeah, I think…
**Tyler** 51:21 Alright.
**Nikola Grcevski @ Grafana / OpenTelemetry** 51:22 I think this user was, or contributor was pinging me and Nimrod on… on Slack about this, and we sort of agreed that we'll do a first step and then fix the RPC things, but we can push for it to get done.
Fully.
I think we just want A current bug first, and then… Because the metrics right now for JSON RPC end up being as HTTP metrics, which is wrong. They should be RPC metrics.
So there's a lot more issues than just the…
**nimrodavni** 51:52 Nope.
**Nikola Grcevski @ Grafana / OpenTelemetry** 51:53 But… But…
**Tyler** 51:55 Right, yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 51:56 Good, because right now, the way that the previous contributor that the Go Jason RPC was storing it into the short buffer, rather than the long buffer.
And so the name was being cut off, so you could barely see what the RPC method was.
Hmm.
**Tyler** 52:15 I see, okay.
**Rafael Roquetto** 52:20 Yeah, I just asked, like, I think… he might not need to have, like, a string, and then all this block doing comparison, but if he just passed up a bool instead on the struct, he can just check and, like, I think he can reduce the code if I understood it correctly. So, see what he says. It's not a… It's not a major blocker, what he's doing.
I don't know what you guys think, like, have a look and send a check, my stuff, too.
**Nikola Grcevski @ Grafana / OpenTelemetry** 52:50 I mean, we're using the same fields that exist, so it's not… But, okay, yeah, let it respond. I mean, it's not critical to fix this, the bug is already there for a long time.
**Rafael Roquetto** 53:01 Yep.
**Tyler** 53:06 Okay.
**Fixed-race student parent header, yeah, for 1 kilobyte HTTP… Nikola Grcevski @ Grafana / OpenTelemetry** 53:13 Yeah, there's some good pictures. I saw some updates, I don't know if he… he added the tests, but I think… I mean, I like the fix, and I actually proposed that we can either Accept the fix without the test, and then write the test after, because…
**Rafael Roquetto** 53:34 8 minutes ago, cool.
**Nikola Grcevski @ Grafana / OpenTelemetry** 53:35 Yeah.
**Rafael Roquetto** 53:36 Yeah, I think… so this is a good… this guy has found a legitimate bug. I mean, this is, great PR, for instance.
**Nikola Grcevski @ Grafana / OpenTelemetry** 53:44 Yeah, and added a test now, so it's good. Okay. Yeah, this is legit. I mean, is using AI in the right way.
So no…
**Rafael Roquetto** 53:53 Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 53:55 No issues on my side. He found a legit bug, explain it, show the math why it's wrong. So, I bet.
**Tyler** 54:03 Do we want to try to get this in the next release?
**Nikola Grcevski @ Grafana / OpenTelemetry** 54:06 Yeah, it would be nice.
**Rafael Roquetto** 54:07 Yes, yes, yes, there's an actual bug.
**Nikola Grcevski @ Grafana / OpenTelemetry** 54:09 If the test actually works, we should…
**Tyler** 54:15 Cool.
Okay.
Fixed tracing correct, trace ID not found.
**Nikola Grcevski @ Grafana / OpenTelemetry** 54:26 And we can ignore all of them.
the next three, I think these need a lot of changes.
**Tyler** 54:32 Yeah, okay.
So then next up is Florian, add event-based Docker container info caching.
**Nikola Grcevski @ Grafana / OpenTelemetry** 54:39 Yeah, I really hate it, it looks… okay to me, I don't know, but I… I bet you have some comments.
**Tyler** 54:46 Yeah… this is definitely one where it was, like, storing with one ID, and then it was clearing with another, and, like, there's actually a.
**Nikola Grcevski @ Grafana / OpenTelemetry** 54:56 Oh my god.
**Tyler** 54:56 I missed, but… Nikola Grcevski @ Grafana / OpenTelemetry 55:01 Interesting, okay, I understand.
So, maybe it needs a test on that.
**Tyler** 55:07 Yeah, it, like, it, yeah, it had a test, but it was in the test also capping, Nikola Grcevski @ Grafana / OpenTelemetry 55:12 Okay.
**Tyler** 55:13 Yeah, so… It was one of those things where, like, yeah, we just need to get that testing behavior correct, yeah. But I think it's not too severe. I think it's a good PR, I just, yeah. Okay.
Okay, next up is, Align AI Instrument. Yeah, we talked about this one.
**Nikola Grcevski @ Grafana / OpenTelemetry** 55:33 Yep.
**Tyler** 55:34 Hopefully get a ping on that one.
Weaver Full Coverage is something that split off, we were looking at that other PR.
The network TCP handshake role. Again, we talked about this, Giuseppe needs more reviews on this, and then it's also going into the next milestone.
This update just got redone, so this just needs some eyes on it. I think this is… Pretty… obviously, sea ice sailing, so… just need some more… somewhere to figure out what's going on there.
Gen AI re-rank support, I think I just saw this this morning. Yeah, this is.
**Nikola Grcevski @ Grafana / OpenTelemetry** 56:08 Yeah, one more of the Jenna aspect, yeah.
I'll review it too, yeah. So I guess he added re-rank support, which is nice.
**Tyler** 56:17 Very cool. I think there's that big issue, so let's just keep going, yep.
**Nikola Grcevski @ Grafana / OpenTelemetry** 56:21 Yeah, I mean, we're pretty close to… completing it. I don't know if you've looked, but he's done so much work.
**Tyler** 56:28 Yeah, it's kind of incredible, so I'm pretty excited about this.
I think the GenAI semantic convention people are gonna be super excited as well, because we can become a testing ground for a lot of the stuff we're doing.
Skip loading unused eBPF programs when features disabled by Stats Ollie. This, again, we talked about this earlier, just needs, more review. Otherwise, going out in the next, Next release.
Improvements to the Weaver schema and tooling also needs review. This is definitely a new one.
And then add integration just for Go MQTT.
This is Mark.
Just an hour ago. Looks like it's already been reviewed.
So, yeah, this could probably also get included in the milestone.
But more reviews.
**Nikola Grcevski @ Grafana / OpenTelemetry** 57:16 I think we can merge that, unless you guys think anything else, but… because we already had the test that… for Go MQTT that Steven added.
But we weren't using it, because… We thought initially we could add the MQTT probes.
That we needed to add them, but now that I added generic support for Go, then… districts work, which is pretty much enabling the test, then, that Steven added.
It worked out of the box, so…
**Tyler** 57:48 I'm happy to merge this, look pretty straightforward.
**Nikola Grcevski @ Grafana / OpenTelemetry** 57:51 It's just a test, yeah.
**Tyler** 57:58 Cool. Alright, that's the end of the PRs. We are right up at the end of time.
So, yeah, I think we can probably end it here. Thanks, everyone, for joining.
It's good seeing you all.
**Nikola Grcevski @ Grafana / OpenTelemetry** 58:09 Okay.
**Tyler** 58:10 Yeah, we'll try to get this next release out, and keep progressing.
Alright, talk to you all later.
**Rafael Roquetto** 58:15 Alright, see you guys!
**Nikola Grcevski @ Grafana / OpenTelemetry** 58:16 Bye.
**Rafael Roquetto** 58:16 Right.
