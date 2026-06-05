SIG: End-User SIG
Date: 2026-06-04
Duration: 36 minutes
============================================================

## Zoom Recording Transcript

**Dhruv Ahuja** 02:13 Hi, Dan.
**Dan Gomez Blanco** 02:16 Hello, Lou, how's it going?
**Dhruv Ahuja** 02:19 I'm good, how are you?
**Dan Gomez Blanco** 02:21 Good, good.
Just went in to see if, I see that are a few people that are missing today, Ernest and Victoria.
**Dhruv Ahuja** 02:29 Yep.
**Dan Gomez Blanco** 02:50 the topics.
I'm sorry, I've not been able to, join the last few ones, So, is this your first one? You've been joining before?
**Dhruv Ahuja** 03:04 Yeah, this is my second end-user SIG meeting, so I actually started, getting into the OpenTelemetry ecosystem on the community side.
Just this last month, actually.
**Dan Gomez Blanco** 03:17 Alright, perfect.
**Dhruv Ahuja** 03:20 Yeah, so I've mainly been working on some of the, couple issues on the OpenTelemetry website.
made a couple of issues there, and then fixed a couple, which are more aligned towards the contributor experience, but I think these two SIGs have some… something of a crossover, right? I would assume.
**Dan Gomez Blanco** 03:44 A little bit. A little bit of…
**Dhruv Ahuja** 03:46 Crossovers.
**Dan Gomez Blanco** 03:47 Sometimes, yeah.
**Dhruv Ahuja** 03:52 Right, and then I've been looking at some other Slack discussions, so I think I'll be picking up an issue soon, maybe the one where we have to go through a couple of articles and then update the contributing page.
I'll have a link somewhere, I think.
**Dan Gomez Blanco** 04:11 Let's add the, topics to the list, and we can then discuss them in detail.
**Dhruv Ahuja** 04:18 Yeah, let me… Or you've got…
**Dan Gomez Blanco** 04:19 I'll drop the link to the notes in there, in the chat.
**Dhruv Ahuja** 04:25 Yeah.
**Dan Gomez Blanco** 04:30 Hey, Adriana.
**Adriana Villela** 04:31 Hey, how's it going, Dan?
**Dan Gomez Blanco** 04:33 Good.
finally I can make this. I don't know what happened, but, like… whatever, 3 ones. I was either traveling, or on holiday, or something.
**Adriana Villela** 04:43 Oh, I feel that.
Don't ask me what my autumn is looking like, because it's a bit of a shitshow. I'll be in your neck of the woods for a chunk of it.
**Dan Gomez Blanco** 04:52 Are you coming to KCD Edinburgh? That would be good.
**Adriana Villela** 04:55 I, I applied, so if you're… if you're one of the CFP reviewers…
**Dan Gomez Blanco** 05:00 I'm not…
**Adriana Villela** 05:01 Wink, no. I did apply for KCD Edinburgh, so, I… let's see, let's see what happens. But, timing would work out well, because I'm gonna be at, Cloud Native Poland, later that same week.
And then, Cloud Native Bergen on, like, the Monday.
**Dan Gomez Blanco** 05:22 at the same time, so…
**Adriana Villela** 05:24 Yeah, they're all… but fortunately, there's… there's no overlap, so it's not like, oh, I have to decline one because I got into the other, so that'll be… that'll be manageable.
And it's not like I have to be away in Europe for, like, 2 weeks. It'll be, like, a week, week and a half, depending, so… yay!
**Dan Gomez Blanco** 05:45 Yeah, I'll definitely be a… I… I think I… I don't know if, CFP… is still open for… I think it is.
**Adriana Villela** 05:53 I think it is… I think it closes end of, like, this week, or early next week, or something.
**Dan Gomez Blanco** 05:58 I will… I will post something. So, I mean… Yeah. It's walking distance from my flat, where, like, the, the conference.
**Adriana Villela** 06:07 Man, if I get to go, I would love to, like, hang out.
**Dan Gomez Blanco** 06:13 Definitely. Alright, should we get going?
**Adriana Villela** 06:19 Yeah, let's do it.
**Dan Gomez Blanco** 06:20 Right. I was gonna say, Drew, if you wanna add some topics… To the agenda, the… no, the…
**Dhruv Ahuja** 06:30 Yeah.
**Dan Gomez Blanco** 06:30 You know, its own…
**Dhruv Ahuja** 06:31 Trying to find that, thread.
Alright. Yeah, I'll do that.
**Dan Gomez Blanco** 06:37 M… Right, so I just wanted to give a quick update on Blueprints, because that is part of you know, in a way, part of his SIG.
And, yeah, so we have the first well, we had reference architectures from end users published that were originally worked on by the DevEx.
SIG, and now they have been published with the… within the… this section.
Which I'll add in… one second.
And, in the notes.
Well, actually, let me just link in the notes first.
There was a blog post, if you want to share that. It was a blog post published that introduces the concept of blueprints, what they are, what are reference architectures, how do they all, you know, relate to each other.
So that was published. Then there were a bunch of reference architectures that were published, that had been published as blog posts before.
So these are end-user reference architectures.
And then we have, adobe, Mastodon, and Skyscanner that publish their reference architectures.
And… just today, or… What was it yesterday? I think it was yesterday. Yesterday, we had the first blueprint published, so that was Lukash… Published. This reference… this blueprint.
for… yeah.
for non… infrastructure and processes in non-Kubernetes environments.
So that is the first blueprint that's published.
And now we have… two in progress… we have two in progress, but I will link here the ones that is… The one that I'm currently working on.
Which is this one, looking at the notes… Is the one for, clonative, telemetry platform. So it's more of, about, yeah, provide, like, using platform engineering practices to provide that layer of, telemetry… consolidating telemetry across SDKs, and collector pipelines, and going into a bit of sampling as well.
It's quite white.
But hopefully that can then link to other blueprints that may go more in detail into specific things.
And… yeah. So, that's the current state. We have one published, One in progress.
And then we have a few in the pipeline as well, which brings me to another thing that I wanted to talk about.
Yeah, so I guess… Maybe this is for… you and I to talk about Adriana with reason and, and Andrea?
I was thinking that… Someone from that group.
potentially, like, Lucas has been… basically, and I'll say this is recorded, so if you've seen this, he's been great at, like, you know, basically helping with, one, with the blueprint that he wrote, but he's also reviewing a lot of other stuff.
So, I would like to, at some point after these… this initial blueprints project is complete, I'm gonna have a process for, like, you know, getting more, like, reference architectures, getting more blueprints and all that, that, yeah, that Luke Cash is, you know, can help with that aspect of the SIG. So then… I would… nominate Lukash as, approver, but then, you know, the way I see it is, like, having two like, approvers… almost, like, not having two groups, or two teams in GitHub, but almost, like, listing in our repo that some people may be, like, working on more on the reference architectures, blueprint stuff.
and other people may be working on other parts of the SIG that are more, like, end-user surveys, almost like areas of interest for people that are… That are in this egg? Don't know what your thoughts are on that.
**Adriana Villela** 10:55 Sorry, say, is, what were you… what do you mean for… So if you have, like…
**Dan Gomez Blanco** 11:03 Yeah, so if you have, like, you know, approvers, right?
**Adriana Villela** 11:06 Help.
**Dan Gomez Blanco** 11:06 to, you know, both, I guess, triageers and provers for the end-user sig. So far.
has been focused on, like, surveys, session…
**Adriana Villela** 11:18 films.
**Dan Gomez Blanco** 11:18 sessions and all that.
**Adriana Villela** 11:19 Yes.
**Dan Gomez Blanco** 11:20 and stuff, and they know there's ads.
I don't… basically, this adds, like, reference implementations and… and blueprints.
as a bit more of a technical, you know, requirement.
**Adriana Villela** 11:33 Yeah.
**Dan Gomez Blanco** 11:34 what I'm thinking is, like.
pretending that every… like, the… I think… I think the sake is, like, getting quite wise.
**Adriana Villela** 11:41 Yeah, yeah.
**Dan Gomez Blanco** 11:42 So basically, like, there could be areas of interest for people in the SIG that are like.
**Adriana Villela** 11:47 Yeah.
**Dan Gomez Blanco** 11:47 I'm more… I'm an approver, but I'm more interested in, like, doing surveys that I'm in.
**Adriana Villela** 11:52 Oh, so like a more an area-aligned approver.
**Dan Gomez Blanco** 11:56 Yeah, like, we can… I think we can… Yeah, it…
**Adriana Villela** 11:58 Yeah, yeah, I think that makes sense, actually.
**Dan Gomez Blanco** 12:03 I think they do it in the… it's similar to what they do in the, in the website, right, in the comms, SIG. But they've got, like, people, other maintainers that are across the whole thing.
Yeah. And you've got approvers that are per, like, language.
Translation, or whatever.
**Adriana Villela** 12:20 Yeah, yeah, yeah.
**Dan Gomez Blanco** 12:22 Something like that.
**Adriana Villela** 12:23 Yeah, yeah.
So, cuz, yeah, I think that makes sense.
How do we, is there a way to denote that in Git?
Or is it just a…
**Dan Gomez Blanco** 12:38 We could. Actually, we could. We could, I think that's probably something that we'll need to think about. What makes more sense?
Everyone to be, you know, split.
in GitHub Teams.
**Adriana Villela** 12:50 Yeah.
**Dan Gomez Blanco** 12:51 We can create a different guarantee.
Or if you want to have a single GitHub team, but then people sort of know, you know… I don't know. People might get… A bit of spam from, like, being tagged to… And many issues and stuff, and there's not gonna.
**Adriana Villela** 13:05 Yeah… True, true. Yeah, because if we created… oh, yeah.
Right, right, right, right, right. Yeah.
**Dan Gomez Blanco** 13:14 Yeah, I think…
**Adriana Villela** 13:15 teams… I think… I think the specific teams might be… Might be best, because then, if someone wants to be on all the teams, then they can be on all the teams, and if they don't, they don't.
**Dan Gomez Blanco** 13:27 I guess we got.
**Adriana Villela** 13:28 Yeah, because I guess it would be more used for, like, just tagging purposes, right?
**Dan Gomez Blanco** 13:33 Yeah.
**Adriana Villela** 13:34 Yeah, they're…
**Dan Gomez Blanco** 13:35 Like, you know, interact.
**Adriana Villela** 13:36 Because I don't think we can… we can have, like, an approver per area of the repo. I feel… I don't think that's even… like… I don't think there's an approver, like, if we had a Blueprints folder.
for a SIG repo, I don't think you could be an approver just for the Blueprints folder. Like, there's not that level of granularity, right?
**Dan Gomez Blanco** 13:57 I mean, we could, but the blueprints are not public… blueprints are published in the, you could have it as code owners, basically, where you assign… Reviews to only particular areas of the report itself, but then.
**Adriana Villela** 14:09 Oh, okay, okay.
**Dan Gomez Blanco** 14:10 Just thinking of, like, issue. I think we do more issues than we do code. Yeah.
**Adriana Villela** 14:16 Yeah, that's true. That's true.
**Dan Gomez Blanco** 14:17 The issue is, like, they may be, like, assigned to… Or not assigned, but someone will be… We'll know who to tie.
**Dhruv Ahuja** 14:25 We'll know who to…
**Dan Gomez Blanco** 14:27 As in, for example, in the website, if someone is writing a blueprint, they'll know that they need to tag the blueprints team, or something like that, right?
**Adriana Villela** 14:36 Yeah, yeah, yeah.
Yeah, and I know that there's, like, On the website, there's, like, automations that tag The appropriate team as well, right?
**Dan Gomez Blanco** 14:51 Yep.
**Adriana Villela** 14:52 So, yeah, I'm sure we can implement those.
**Dan Gomez Blanco** 14:58 Yeah, I think we can do code owners, and then do that.
**Adriana Villela** 15:01 Yeah, yeah.
**Dan Gomez Blanco** 15:02 You're on a.
**Adriana Villela** 15:02 Okay, cool, cool, cool.
**Dan Gomez Blanco** 15:03 Yeah.
**Adriana Villela** 15:04 Oh, yeah.
**Dan Gomez Blanco** 15:05 So let me write a message, because I think, you know, let's see what people… Fair.
think… maybe, like, chat with Marilla as well.
So, unless the guidance has changed from… from the GC.
**Adriana Villela** 15:20 Yeah.
**Dan Gomez Blanco** 15:20 We need to create new… new teams, if we need to create new teams.
**Adriana Villela** 15:24 Yeah.
**Dan Gomez Blanco** 15:26 As an idea, I don't think they need a specific, you know, let's see… SIG.
**Adriana Villela** 15:34 Yeah.
**Dan Gomez Blanco** 15:34 I wouldn't want to do… I wouldn't want to… spin up a new SIG, basically, I think.
**Adriana Villela** 15:39 Yeah, yeah.
**Dan Gomez Blanco** 15:40 I see.
**Adriana Villela** 15:41 Yeah.
**Dan Gomez Blanco** 15:42 So I think there is still value in having blueprints and reference architecture is highly linked to the work that we do with HotelMe and…
**Adriana Villela** 15:53 Yeah.
**Dan Gomez Blanco** 15:54 You know, till Q&A.
Yeah. I think they're like, I would love that, you know, for every hotel meet that we have, that whatever, whoever we invite.
they could create, a reference implementation or something like that, right? That would be…
**Adriana Villela** 16:09 Hmm…
**Dan Gomez Blanco** 16:10 That would be pretty… I mean…
**Adriana Villela** 16:12 That would be great, I just… I feel like they would… unfortunately be put off from that. They'd be like, oh no, it's more work.
**Dan Gomez Blanco** 16:19 More work, yeah.
**Adriana Villela** 16:21 Yeah, no, I agree, that would be… that would be super cool.
**Dan Gomez Blanco** 16:26 That'd probably be what they say, is like, that sounds really good. However, that also sounds like work.
**Adriana Villela** 16:31 Yeah, yeah, exactly.
**Dan Gomez Blanco** 16:33 that. Exactly.
Alright, so yeah, that's me for Blueprints. I think, you know.
**Adriana Villela** 16:39 Cool.
**Dan Gomez Blanco** 16:39 Going through the… The, the comments, sort of the… the first round.
And, and I think we've got… a… This is what I think is important to have links. We have someone that proposed a reference implementation, and that is… There was a triage… Let me see if I can find it.
If I go to… seek.
End user… One second.
Someone that proposed.
a reference implementation from a company called Crystalline X.
Crystalline Exchange.
From financial services.
And my thinking is… the opposite, maybe, right? So if someone proposes a reference implementation.
Yeah. We should… we should definitely have him on a HotelMe,
**Adriana Villela** 17:38 Yeah, that's true, that's true.
That's cool. Wow.
Proof of observability crypto exchange shit.
Yeeee…
**Dan Gomez Blanco** 17:55 Yeah, so, I'll keep mine.
**Adriana Villela** 17:59 Should I… should I reply to that?
Issue, and say, hey, would you be interested in being in one of our streams?
**Dan Gomez Blanco** 18:08 Yeah, although I think… do you think that it's better to, like, publish the reference implementation first?
**Adriana Villela** 18:14 Oh, yeah, yeah, actually, that would be a great idea, because then we can, yeah… Then we can… Say, and by the way, look at that.
Yeah, yeah.
**Dan Gomez Blanco** 18:24 discussed aspects of this, and was like, oh, if you want to go into detail, you can.
**Adriana Villela** 18:27 Yeah.
**Dan Gomez Blanco** 18:28 Yeah, right?
**Adriana Villela** 18:29 Yeah, I agree.
**Dan Gomez Blanco** 18:40 Alright, I'll have a look at that. Cool.
Okie doks, just going through the next.
M… Alright, okay, so I just saw the comments that you… so this is related to Blueprints as well, Dhruv, just moving to your… To your point.
**Dhruv Ahuja** 19:06 Yeah.
**Dan Gomez Blanco** 19:09 So the first one, this issue.
Should have been marked as blueprints, by the way, should have been tagged.
This has been done already, so… .
**Dhruv Ahuja** 19:21 Okay.
**Dan Gomez Blanco** 19:22 Yeah, I think, almost like Tiffany opened it.
And then she took care of it.
And I think we.
**Dhruv Ahuja** 19:31 What?
**Dan Gomez Blanco** 19:32 Let me just close it with a message.
And then the other one… you wanna talk about that? The survey?
the Japanese.
**Dhruv Ahuja** 19:48 Yeah.
Yeah, because I think the previous issue that I mentioned, maybe that was in the other second, or the other Slack channel, and I just confused it.
So, I'm just trying to understand or take up some issue where I can maybe contribute even some units of work, right, if the scope is too large for me to do on my own, or understand at this point.
So, I had gone through the first Japanese survey, read through the blog as well as the responses, and so I was thinking that maybe that's something that I can work on with Ernest, if it is going to be picked up sometime soon.
Because one question that I would definitely think that maybe we should consider is, at my workplace as well, I'm hearing that people are really, really making positive use of MCP servers and AI to improve their observability experience, not just with open telemetry, but in understanding observability concepts as well, because let's say that if you're using Claude and you pull up a trace, right, if you have an error of… or if an alert fires off.
you ask Claude to start the diagnosis, then you can actually ask it to then break down each and every part of what went wrong, what are all these moving parts, and such things. So, I was thinking that whatever survey we conduct next, we should have, kind of… if an open-ended question is possible, then I think that would be the best, that how are you using AI tools, and how are they helping you in observability or with open telemetry? I think there'd be some interesting info to get from the community there.
So I was thinking that if I can come up with a couple of questions that I could add to the survey, or maybe start a discussion on.
**Dan Gomez Blanco** 21:40 For the Japanese one, or would you think of, would you think… Well, maybe that's something to check with, with Ernest as well.
**Dhruv Ahuja** 21:49 Yeah.
**Dan Gomez Blanco** 21:50 I don't know if the intention of rerunning the Japanese survey was to… have a before and after, or, like, to create some type of, like, you know, has there been an improvement? I don't know what changes happened in that community, right, over the last few months. So if they wanted to run that again, they may want to run it with the same questions, I don't know.
So maybe what's.
**Dhruv Ahuja** 22:08 Stream with them.
Yeah.
**Dan Gomez Blanco** 22:12 And the other thing that I would say is.
That would be interesting. There is an empty… there is, an initiative, right, to create an MCP Has there been a… Let me just try to link to it.
There is an initiative, I'm not sure if it's been approved.
Mmm… Agentic workflow.
So it's this one here.
Post it in the chat.
Mmm… So that would be interesting. So this group… They're basically saying that there is already a bit of tooling I would say first, I think… I think we should focus on the OpenTelemetry side.
If you… even if you have an open-ended question.
If you have it, like, related to how people use… AI tooling.
**Dhruv Ahuja** 23:36 Yeah.
**Dan Gomez Blanco** 23:36 On their backend.
Then, you know, after the data is ingested in whatever vendor, or whatever.
then the insights that we will get from that is not going to be very useful to OpenTelemetry, because we cannot get into the… vendor discussion, right? .
**Dhruv Ahuja** 23:54 Yeah.
**Dan Gomez Blanco** 23:54 So… So yeah, I think… However.
here we're saying that there is the Weaver NCP server, and there is, some other people out there that put their own whatever.
OpenTelemetry MCP servers.
So, yeah, so this project's aimed to… Enable agentic workflows?
And then try to understand, I guess, you know, try to basically centralize that MCP.
M… story, really.
So, with that in mind, maybe there will be interest in running E.
Survey in the community that is aimed at that in particular.
**Dhruv Ahuja** 24:49 Got it. So you mean the agentic workflows, as a whole, right? Where you have MCP servers, what kind of MCP servers are people running, or what they're doing with them? Or what kind of workflows they're building for their own observability journey?
**Dan Gomez Blanco** 25:05 Yeah, as in that, what would it be useful for… what would be useful for people?
if OpenTelemetry had an MCP server.
**Dhruv Ahuja** 25:14 Right.
**Dan Gomez Blanco** 25:15 Not if their vendor had an MCP server, right? Because that's the difference, that is. What would be useful for you if you're a… If you're an end user, and… you say, hey, you know, the hotel collector, or gives me an MCP server, or Weaver, as it does already, gives me an SCP server. What do you want to do with it?
Or what are you missing?
**Adriana Villela** 25:41 That would be a great one.
There are… there are, like… There's stuff in motion, right, around… hotel MCP servers?
Like, I remember seeing an issue, but nothing, like, firm, right?
**Dan Gomez Blanco** 25:57 Yeah, so I linked that project, I'm not sure where it is, I think it's just merged a few weeks ago.
**Adriana Villela** 26:02 Okay, cool.
**Dan Gomez Blanco** 26:03 Two months ago, but I don't know what the status is of, of this project… Alright, so… it's got… this is why we've got these things.
They seem to… I've created some tasks, and… Alex is the one that seems to be driving a lot of it.
By the looks of it.
Cool. Alex… Alex Bolton?
**Adriana Villela** 26:36 Bowen? Yeah.
**Dan Gomez Blanco** 26:41 So, yeah, so I guess they are creating that collector.
MCP extension.
**Adriana Villela** 26:50 Yeah, yeah.
**Dan Gomez Blanco** 26:55 Yeah, so basically, I don't know what this data says, but they might be interested in a phase, you know, after they've got all this tooling, that people are basically… Willing to donate, wherever.
**Adriana Villela** 27:07 Yes.
**Dan Gomez Blanco** 27:08 extension.
Then, they might be interested in knowing what people want to do with it.
**Dhruv Ahuja** 27:16 Makes sense, yeah. Yeah, I…
**Adriana Villela** 27:18 Definitely.
**Dhruv Ahuja** 27:19 We searched and open an issue, at least, so we have somewhere to track progress.
**Dan Gomez Blanco** 27:28 Twice a second.
**Dhruv Ahuja** 27:29 Yeah, I said I'll at least do some initial research and open an issue so we can track progress and discuss as needed.
**Dan Gomez Blanco** 27:37 Yeah, what I would say as well, it might be a good idea to, Is there an MCP? Is there an Autel MCP? OTEL Collector MCP?
So there's a channel, let's go hotel collection MCP.
If you wanted to, like, you know, Ultimately, I think.
If they're not gonna… if it's not gonna be useful for them.
then there's no point in running it, right? I guess, you know, that's the… I guess… I don't know, that's my… that's my point of view. I mean, what's the point of running a survey if the people running on MCP are not, like, willing to collaborate? Because the way that, you know, you've probably seen that in how we run surveys, that the SIG that is… Running the survey, or helping us run the survey, they… we collaborate with them, right, to… To craft the questions and all that, so that the answer questions that the… That they want to.
to… to… answers for. So yeah, it might be a good idea to reach out in that channel.
And ask if, hey, you know.
**Dhruv Ahuja** 28:43 Good morning.
**Dan Gomez Blanco** 28:43 We were just talking about this from the end user's sake.
you may want to… if you want to run a survey to understand how people are using MCP, Is this something that would be useful?
For this group to know.
And would they be willing to?
collaborate, I guess.
And then you can create the HAVE.
If I want to. Because that's… that's my view on it, but I don't know if, Adriana, you agree?
**Adriana Villela** 29:10 Yeah, yeah. Yeah, I like that.
**Dan Gomez Blanco** 29:14 Cool.
**Dhruv Ahuja** 29:16 Cool, and yeah, one other question. So, Adriana, are we not running the WhatsApp Hotel livestream this month? The previous month, I mean. I didn't see any…
**Adriana Villela** 29:26 Oh, yeah, no, we… we… travel schedules kind of killed it. But we are… we are planning one for this month, like, for June.
So Reese has got the wheels in motion for reaching out to, To, the appropriate folks, so we'll be… we'll be doing that, for sure.
**Dhruv Ahuja** 29:46 Awesome.
**Adriana Villela** 29:48 Hey, Sophia!
**Dan Gomez Blanco** 29:52 Oh, no.
**Sophia Solomon** 29:52 Oh! Hi!
**Adriana Villela** 29:53 How's it going? Good.
I think you muted yourself.
**Sophia Solomon** 30:09 Oh my god.
**Adriana Villela** 30:10 There we go.
**Sophia Solomon** 30:13 I don't even know how long I was talking, I don't know. Don't worry about it.
**Adriana Villela** 30:17 Oh, not very long, not very long, you're good.
**Sophia Solomon** 30:19 Okay.
**Adriana Villela** 30:21 Yeah, yeah.
**Sophia Solomon** 30:22 Yes, hi. I don't know if you guys are done.
this… past.
topic, but…
**Dan Gomez Blanco** 30:29 Hello.
**Adriana Villela** 30:31 Yeah, yeah, I, yeah, I think… yeah, your question was on, on what's Up Hotel, right? Was that…
**Dan Gomez Blanco** 30:39 Oh, the hotelinaire, the… who wants to be an hotel?
**Adriana Villela** 30:42 Oh, the hotel… oh, yeah, what happened with Hotelianaire? Did we… we got one person, but we need a phone-a-friend person.
**Sophia Solomon** 30:50 Yeah, so this is…
**Adriana Villela** 30:51 with that.
**Sophia Solomon** 30:52 This is what I'm putting in the notes, the… I tried to reach out to the person that we got for our guest contestant, who is Braden Keynes.
He mentioned Alex as a possible phone of friend, but I don't think.
**Adriana Villela** 31:11 Yeah.
**Sophia Solomon** 31:12 wanting to do that right now. So, he also mentioned, Pablo Bayans. Oh, yeah. Because he's a governance committee member, but, apparently he doesn't usually like to use his camera in live or reported environments, so…
**Adriana Villela** 31:29 Try Evan Bradley.
**Sophia Solomon** 31:31 Evan Bradley.
**Adriana Villela** 31:33 Yeah, he's… he works with me at Dynatrace. I can maybe nudge him if he's shy.
**Sophia Solomon** 31:40 Okay, I'm getting the questions out in the cahoot, and I'm gonna speak with, Victoria.
About collaborating on that.
And then… we just gotta worry about scheduling. I was thinking…
**Adriana Villela** 31:58 Yeah.
**Sophia Solomon** 31:59 Towards the end of June, but I don't… I don't know what's going on with, like, what's up with OTEL, and, like, I don't.
**Adriana Villela** 32:07 Oh.
**Sophia Solomon** 32:07 Flash with anything.
**Adriana Villela** 32:09 I can tell you when we have it planned. One sec.
What's up? Hotel is gonna be… Oh, crepes.
One sec.
Oh, crap.
I don't know, I gotta ask… It's not on the calendar for some reason. I'll reach out to, Reese and Julia, figure out what… what happened.
Because it fell off my calendar.
It could be one of those, like, annoying things where you… It ends the recurrence.
**Sophia Solomon** 32:58 Yeah.
**Adriana Villela** 32:59 And you're not aware of it.
Yes, yes.
Okay, I'll, I'll get back to you on that.
**Sophia Solomon** 33:09 Okay.
But yeah, I think we're… We're still turning gears at this moment. I had a bunch of conferences to go to, so… which I saw Reese at, and I also saw Julia, so it was nice.
**Adriana Villela** 33:25 Oh, nice. That's awesome.
Yeah, and you were at KCD Austin, right?
Open Source Summit.
**Sophia Solomon** 33:32 Observability Summit, but yeah.
**Adriana Villela** 33:35 Oh, yeah.
**Sophia Solomon** 33:35 Nothing different.
**Adriana Villela** 33:36 Oh, right, right, right, right.
Oh, and by the way, there should be an observability summit in Europe.
I mean… Like, it's scheduled for the 5th of, as of October, but I haven't gotten any more details on CFPs and stuff.
**Sophia Solomon** 33:54 Oh, no CFP.
**Adriana Villela** 33:56 Yeah, so FYI.
**Dan Gomez Blanco** 33:58 Too cool.
**Adriana Villela** 33:59 That'll be in Prague, and Open Source Summit is… so this is happening on the Monday, and then Open Source Summit's supposed to happen on the Thursday-Friday.
**Dan Gomez Blanco** 34:06 Oh, wait, I did get, yeah, Observability Summit Euro 2026, I did get an email about that.
**Adriana Villela** 34:11 Oh, we did? Oh, yay.
**Sophia Solomon** 34:13 Oughta.
**Adriana Villela** 34:14 No, I didn't get…
**Dan Gomez Blanco** 34:15 age.
No, sorry, just got an email, if I wanted to be part of a… program.
**Adriana Villela** 34:21 Oh.
**Dan Gomez Blanco** 34:21 To review all this.
No, not too… I don't know if there's, like, a link already for the…
**Adriana Villela** 34:27 Yeah, I don't know if there… yeah, I didn't get one for Observability Summit. I got one for Observ… Bloody day… Huh.
**Dan Gomez Blanco** 34:39 Maybe they're just targeting you.
**Adriana Villela** 34:41 Wow. Yeah.
**Dan Gomez Blanco** 34:41 Folks.
**Adriana Villela** 34:42 Oh, possibly.
**Sophia Solomon** 34:43 If that makes sense.
**Adriana Villela** 34:45 Possibly…
**Dan Gomez Blanco** 34:56 Alright, I think we went throughout quite a few topics.
**Adriana Villela** 35:02 Oh, I have some potential people for, hotel in practice and hotel me.
But… Like, one person was asking for more prep time.
So… Shit, and I can't remember who the other one was. So they're not, they're not confirmed yet. Oh yeah, one, one is from Oxide Computer.
A friend who works there introduced me to his coworker who's doing some hotel stuff with their hardware, so… I think that could be really cool.
So I'm just waiting to hear back. He did the intros yesterday, I'm waiting to hear back on… if he's interested in HotelMe, Hotel in Practice, or both, and then we can figure out dates as well for that.
**Dan Gomez Blanco** 35:51 Sounds good.
Okay, Is there anything else that we want to… Discuss.
**Adriana Villela** 36:30 Nothing from my end.
**Dhruv Ahuja** 36:33 No, Paul, good.
**Sophia Solomon** 36:34 No, me neither.
**Dan Gomez Blanco** 36:36 Who's seeing you again.
And, yeah, I guess we've got a few actions to… Yeah, to keep chip in it.
**Adriana Villela** 36:48 Sounds good.
**Dan Gomez Blanco** 36:50 Alright. Cool. Have a good one.
**Adriana Villela** 36:51 Cool. See you in a couple weeks. You too!
**Sophia Solomon** 36:53 Right.
**Adriana Villela** 36:54 Yay.
**Sophia Solomon** 36:54 Thank you.
