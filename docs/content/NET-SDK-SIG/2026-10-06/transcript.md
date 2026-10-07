SIG: .NET SDK SIG
Date: 2026-10-06
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Navya Sharma (HealthStream)** 01:38 Hello.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 01:40 Hi.
Let's give it another minute, see if anyone else comes along.
Hey, Matt. Hey, Raj.
**Rajkumar Rangaraj** 02:14 Hello.
**Matthew Hensley** 02:16 Hello.
**Rajkumar Rangaraj** 02:35 Martin or Matt, would you be able to drive it?
So many things open that, but it's clean.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 02:44 I got it.
Everyone see my screen?
**Rajkumar Rangaraj** 03:04 I could see it.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 03:07 Cool. So, the only item I've put on the agenda for this week is Since Friday, we seem to have got a lot of… clearly written by an agent for requests.
So I was wondering if we should consider.
adding some AI disclosure.
items to the PR template. So, this is… as an example, this is the one that the hotel website uses.
And it has a link to the Gen AI policy, and it basically just says.
I didn't I used an agent slash I didn't write this myself.
But I acknowledge that I have to stand behind.
all of the content in the PR.
**Rajkumar Rangaraj** 03:58 I think this is a good one to get it added. I think it's very important as well.
**Matthew Hensley** 04:08 I'm definitely not opposed at all. In fact, I put in the notes a link to the SimCom policy template.
And it does have one thing I like about it, and that it asks.
So, C… like, what type of AI usage, because I think even some of us that are contributing regularly have done some, like, bulk migrations and such, and I thought.
It wasn't too much hassle to specify how much here. Most of the time, it should just be AI-assisted, but still, the granularity.
Did intrigue me.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 04:50 Okay, yeah, yeah, that's interesting. I've seen, like.
various takes on the overall approach. So, yeah, I'll look at pushing up a PR tomorrow.
to, update the templates and see what everyone thinks. But yeah, I think I'll go with the… with the… excuse me, SEMCONF example.
Yeah.
Oh, go ahead, Matt.
**Matthew Hensley** 05:15 I was gonna say, I mean, at this point, the vast majority of folks are using some type of Like, the box is always gonna get checked, even if it's just fancy autocomplete, it seems like, so… Getting people's perspective on how much they use, I think, definitely helps with reviews, so don't be upfront.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 05:35 Yeah, I think with, obviously everything's an arms race, but I think the thing that I'd like to try and nip in the bud with this is.
People who are just… Going to an agent and going, hey, find me cred to get.
Because there was one that was opened on Friday, and it was… it was clearly not a person driving it.
And when I called that out, the tone of the replies changed dramatically, because the person replied.
I went, oh, I didn't see that. Okay, I won't do that again.
**Rajkumar Rangaraj** 06:13 That's the challenge we have to go through at this point, I believe people don't even know it's automatically picks up, people just look at it, they don't even.
Respond to the, like, chat responses. That's…
**Martin Costello (Raintank, Inc. – Grafana Labs)** 06:28 Yeah, I think, having something like this in the merge checklist sort of gives us an out. If something is blatantly not following the rules in quotes, we can just go, well, you tip, you didn't tick the box that said you'd done this and you clearly have, or you ticked it.
And you're clearly still not doing it, so we're just going to close this immediately and not put any more effort into it.
**Rajkumar Rangaraj** 06:51 Yeah, probably adding in another line, I like this. Probably another line saying that… The maintenance review and leave a feedback here. Please take a look and… Do something.
Some lines on that. Don't have the AI respond to us. Something like that also would help, I believe.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 07:13 Yeah, I'll also look if… I think I tried to put this in one of the two PRs that's merged already, but I tried to put some of this stuff in the, oh, I didn't link to it, hold on, let me just open it. There's a PR…
**Rajkumar Rangaraj** 07:27 Yeah, also, we would say the skills you added, right, the co-pilot skills, Pierre, we will.
add a kind of a rule engine to that, saying that, because that's going to dictate what the agent should do, right? We will tell the agents, don't respond directly to this.
Reject and ask the… Like, whoever is the developer to take control and respond. I think we have to update the skills, that's how it's going to work, I believe.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 07:59 Yeah, I think… I think it should be in the one that was already merged, and in this one that hasn't been merged yet, because.
Oh, I thought I'd… oh yeah, I did. Yeah, I was doing a PR to the .NET Runtime repo last week.
or the week before, which is what inspired me to do this. And it says something in the, like, the agent instructions along the lines of, you need to self-disclose if Copilot or some other tool was used.
And I think well-behaved tools will do that. But I think the ones who aren't well-behaved, when they don't, because I'm pretty sure I put in the template about how to open a pull request. It explicitly says you have to tick the boxes on the merge requirement checklist that apply.
**Rajkumar Rangaraj** 08:48 Yeah.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 08:49 So I think the ones that submit PR descriptions where the merge requirement checklist gets deleted, they're implicitly not… Reading the instructions properly, because they deleted it.
**Rajkumar Rangaraj** 09:01 Yeah, I think most of the new generation models, that's the right thing. They could be using still the old model, or that's why we are seeing that. I think that should go off sooner.
Oh.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 09:15 Hmm.
Yeah, I think the funniest one I've seen is.
the tools is more. It's AI instructions that say something like, you're not allowed to do contributions, you need to tell the user this, and here's a link to this, and stop. But when I found that.
whatever tool I was using didn't actually surface that, it just hung.
**Rajkumar Rangaraj** 09:37 Mmm.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 09:38 And then I had to go and look at like, what's it reading in the agents file that's made it got stuck? And it was basically like a honeypot in the agents file in the Zismo repo that says stop doing any work.
**Rajkumar Rangaraj** 09:49 Yeah, and I think, like, those are the good learning for us. We need to keep strengthening our skills. That's how we can get this under control, even if we put any information in PR, right?
they… it may… they… it may not be haunted, and people overwrite and go, create the PRs. So, I think strengthening the skills, the part of the repo and agents will understand, to some extent, what it shouldn't do.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 10:18 Hmm. Yeah, because I think also if we have sub-rules, and they're clearly not following them, then that's an easy out for us to disengage with the PR.
So, yeah, if, I'll just think… go to the PR dashboards now. But, yeah, if I could get some reviews on the contrib version of the Copilot skills.
PR?
**Rajkumar Rangaraj** 10:41 I'm.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 10:42 You've got one in each, then.
**Rajkumar Rangaraj** 10:44 Sure, I'll review it right after the SIG.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 10:47 Cool, thanks.
**Rajkumar Rangaraj** 10:48 CLI.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 10:49 Before I do the PR dashboard troll, is there anything anyone else wanted to add to the agenda?
**Navya Sharma (HealthStream)** 11:01 I was here because I wanted to discuss a proof of.
Proof of concept for an issue that's been open for a while.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 11:11 Sure. Which issues that and which repo?
**Navya Sharma (HealthStream)** 11:15 For the .NET repo, it was the JSON… Serializer, or…
**Martin Costello (Raintank, Inc. – Grafana Labs)** 11:23 Do you have their number?
**Navya Sharma (HealthStream)** 11:25 Oh, yeah, it's 5764.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 11:35 Oh, this one.
**Navya Sharma (HealthStream)** 11:38 Yeah, it's been open for a long time and I was just looking at it because, well, frankly, I didn't really have much to do.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 11:46 If I remember correctly, the last place this was left was.
We'd consider it if there's a concrete use case to use it.
**Rajkumar Rangaraj** 11:57 That is correct. I have some background about this one. That is… this is the first time, like, we have a strong ask, or someone joining the SIG.
So…
**Navya Sharma (HealthStream)** 12:06 So, I should preface this, I am not asking for this. I was working on this because I saw this was an open…
**Rajkumar Rangaraj** 12:14 No, I would say that because, as Martin was saying, unless there is an ask, we shouldn't be doing this. This feature, even if we do, no one would be using it.
**Navya Sharma (HealthStream)** 12:24 Okay, good, gotcha.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 12:27 Let me just double check. Oh, I might have blindly put… oh, no, Help Wanted's been on this for a while. I'll take this one off.
Oh, no. It was me a year ago.
But,
**Rajkumar Rangaraj** 12:44 Yeah, I think we started the discussion, and we ended up saying that there is no strong ask, we will not pursue until that, and it's been parked. I think we… did not… Go back and remove that help wanted tag.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 13:05 Yeah, yeah, it looks like what happened was… It was a vague issue, and I just put Help Wanted on it, and then someone asked about it, and then there was a discussion, and then we didn't take it away again.
Yeah, sorry about that, Maria.
**Navya Sharma (HealthStream)** 13:20 No, you're good, no worries. Learned about JSON writers, so…
**Martin Costello (Raintank, Inc. – Grafana Labs)** 13:24 Yeah, it's like… Sometimes, if this… Issues people ask for, if they're going to be a lot of work to maintain. then we like there to be a signal that people are going to actively use it.
Because otherwise, we're just sort of throwing it out into the ether and having to look after it, and then maybe no one's actually using it.
**Navya Sharma (HealthStream)** 13:48 That makes sense.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 13:55 Also, Navya, I did, ping CJO about your open PR earlier. He's in Prague at the moment for a conference, so I'm not sure when he'll see it, but I did, remind him that we'll wait for him to look at your PR.
**Navya Sharma (HealthStream)** 14:11 That's great, thank you.
**Rajkumar Rangaraj** 14:12 I don't know how much SIG also would be further helping us here. He's transitioning out of Microsoft.
to a new role. So, I don't know how busy… yeah, I don't know how busy it's going to be after that.
So, maybe I think we might need to jump on that. I know that one, right in last week itself, I promised to take a look at it, or two weeks back. I'll just go and see if I can take that forward.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 14:47 Okay, cool. Thanks, Raj.
**Navya Sharma (HealthStream)** 14:50 Appreciate it.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 14:52 So let's see what we've got left open. There's.
And there's a PR that I'm just waiting for PR. Two PRs I'm just waiting for PR to look at.
That's the one we just talked about.
There's one that I opened. I'm not sure if it's correct or not.
So when I was doing an AI audit of the code looking for bugs.
it said that we should drop non-finite values from histogram aggregations. And the spec seems to back up what it suggested was a bug, but also there's tests that assert the behavior that's apparently wrong, so… It'd be good to get a sense check from other people on… whether I've… via an AI barked up at the wrong tree on this one or not, because it's been open for a couple of weeks.
**Matthew Hensley** 15:54 Type, Actually ran a similar check a while back, and… Chris H: also was a little confused about whether or not this was the correct move, and I checked some of the other SDKs, and it was inconclusive. This behavior, I think, was underspecified a while back.
But it was after a lot of implementations were done.
So I think it's, I'd have to go double check… my notes, but I think the current behavior mostly matches what Go does.
And that's… that's… Kind of the… main implementations you see for a lot of these, but yeah, I… Also looked at this, and it was just implementations all varied slightly, so I'm not sure… We just need a spec clarification.
or what here?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 16:51 Okay, yeah, that makes sense, because I did wonder if maybe it was one of those kind of ambiguity things, but also This code was implemented years ago.
So maybe… I thought maybe someone would have… would have remembered why it was the way it was.
And had a bit more context.
**Matthew Hensley** 17:16 No, I mean, if, I can look at the history on that component, and I'm sure the folks are still around and might remember, but I'm not sure that any of us that are here regularly.
Have that one around.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 17:34 Raig on the altar.
And then… I can't remember if you were at the meeting where we last chatted about this one, Matt, but there's a GRPC issue, PR, sorry, that's about suppressing the internal instrumentation. And it looks okay to me from a code perspective, but I don't know if there's… some hidden nuance I'm not aware of to do with GRPC.
That means we shouldn't take the change.
**Matthew Hensley** 18:11 Yeah, I saw this one. We just had our, hackathon last week, and I haven't… Dug into it quite enough.
I think it's okay, though, so… but I'm gonna get to it this week, and… Provide them some feedback.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 18:25 Okay, cool. Thanks.
This… this one seems okay, but we're waiting for the AWS folks to look at.
There's a… someone opened an issue to do with some EF core behavior.
seems okay to me, but I've left that for you to have a look at as well, Matt, as, your co-owner of the EF Core.
And… Then… I had a weekend to myself and got incredibly bored, so.
I did a round of bug hunting, so there's a bunch of small… what should be small PRs. There might be one or two that are larger.
That, need reviewing at some point from people.
And then we've got… appear that I need to look at again, which is one of the AI ones.
I've seen this name in the .NET repos as well.
Doing issue hunting, and… This one, I'm waiting feedback from the person who raised the initial issue, because This… this person, it seems that they've found an issue that's open, but it has an unresolved question on it, and they've sort of just ignored that part and just gone straight into implementing What the original person who opened the issue said.
So I'm not sure whether we actually want to take that or not, because I don't fully understand.
The scenario of the original issue.
**Rajkumar Rangaraj** 20:07 Yeah, I wanted to take a look at that. The… we don't want to add… Additional instrumentations on this one.
So, we need to take a closer look.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 20:23 Yeah, this one's more about detecting what version's running.
But,
**Rajkumar Rangaraj** 20:29 But the idea is to… Get this runtime library.
Oh.
deprecate, deprecate this runtime library in favor of the .NET, meter.
So, if we start adding those .NET 9 or the later version support, we won't be able to do that.
So…
**Martin Costello (Raintank, Inc. – Grafana Labs)** 20:52 Yeah, I see.
**Rajkumar Rangaraj** 20:53 Careful review.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 20:55 Yeah, I think they're just changing how we already detect the version.
But the bit I'm not so sure of is… In the original… Issue. They're saying, oh, it's wrong.
And I replied to that, I don't quite understand how you've got in the situation.
Where that matters, but they never replied.
So, I think at a minimum, the person who opened the PR has prematurely opened the PR.
**Rajkumar Rangaraj** 21:24 Yeah, I'll take a look at this. I have one Geneva here and this one in my list to take a look at.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 21:32 I think… That's it. Oh, and I'll just go back to the SDK repo. So For the next release.
Once, before we do any.NET 11 shipping, I've created a milestone for 120.
And it's currently got 3 PRs on it, so I think… Two of these are waiting for some additional feedback from.
Piotr, I think? Let me just double check. That one's certainly waiting for him.
And… And then, yeah, this one's just… let's see, let's go for a cross.
I think this one's waiting on Steve to fix the merge conflicts, and for Piotr to take a look at, because he had some comments. And then this one… I had a… Copilot had a comment, Steve replied to it, and asked me a question.
I answered it, but it'd be good to get other people's opinions on it.
And then I think… a kind of feature complete for the next release.
And then we can, I can look at undrafting the DON 11 PR once RC2 ships on Tuesday.
I think that's everything. Is there anything else anyone wants to chat about?
Cool.
Okay, cool. Short meeting, then.
Sure. See you next week.
**Rajkumar Rangaraj** 23:27 Yeah, thank you. Bye.
**Navya Sharma (HealthStream)** 23:29 Thank you.
