SIG: GenAI Semantic Conventions and Instrumentation Stability
Date: 2026-09-18
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Trask Stalnaker (Microsoft Corporation)** 04:17 Hey folks, we'll give another… Couple minutes.
For folks.
It's Friday.
**Surya Teja** 04:25 Do we have an agenda of what we want to speak today at Trask? Or… I see Ludmila is out of, she's on a vacation or something.
**Trask Stalnaker (Microsoft Corporation)** 04:34 Yeah.
**Surya Teja** 04:35 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 04:36 Oh, I'm getting… I prepared sort of a categorization of the work, For stabilization… And so, what I'm hoping to get is some volunteers to sort of own… Pick an area that you want to try to own and drive.
So we can start.
**Surya Teja** 05:07 Okay.
**Trask Stalnaker (Microsoft Corporation)** 05:07 Splitting up the work.
**Surya Teja** 05:10 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 05:15 But I put a… in the, meeting notes here, I put a link… I just put it in a tab here for now.
But, probably… Tried to put it in GitHub.
The… No, no, the board… I was just kinda… Not finding the board very easy to go through.
So… Oh, hey, Aaron. Hey, Felix.
**Felix Becker (Anthropic)** 05:52 Hey, everyone.
This is the first time I'm joining this call, by the way, so I just wanted to… say hello. I think I've seen some of you from the, like.
**Trask Stalnaker (Microsoft Corporation)** 06:02 Other… the general one, yes, yes.
**Felix Becker (Anthropic)** 06:04 But yeah, as we've been, like, implementing more with OTEL, I've ran into the issue of, like, stability and, like, things being spec'd in ways that don't seem… good for, like, forward compatibility, and so, when I saw this on my calendar, I was like, oh, I should join this.
**Trask Stalnaker (Microsoft Corporation)** 06:26 Perfect.
**Aaron Abbott (Google LLC)** 06:27 Yeah, I think we… about that last week, too. But yeah.
**Felix Becker (Anthropic)** 06:32 Yeah, I'm happy to share, kind of, the issues that we've run into, too, whenever, but also, you know, don't want to take over the agenda.
**Trask Stalnaker (Microsoft Corporation)** 06:44 Yeah, have you seen… this was kind of… I mean, we just started this effort here.
And this was sort of our initial outline of… The things that are in scope that we're considering, in scope for this sort of first wave of stability. So, we're not trying to stabilize everything, we're just kind of taking out, Basically, Core inference and, Agentic execution, frameworks.
**Felix Becker (Anthropic)** 07:21 So when you say stabilized, does that mean, like, kind of cutting, like, a V1 version that's kind of frozen in place, including these things, while other stuff is, like, still… You know, under, like, unstable.
**Trask Stalnaker (Microsoft Corporation)** 07:37 Yeah, so everything is… has a stability level attached to it.
so, status development… status development. Everything in this repo is status development, currently, and so our goal is to take The, you know, these things, in some… in scope.
And, try to get them to RC, by, KubeCon, which is, like, mid-November.
And then… So we would then progress that to RC, and then stability, hopefully, not long after that.
And… So everything else would stay in development, and, you know, we can continue working on all those other things in parallel. That's why we kind of spun off this meeting series separately.
To not block, sort of, work in the… that a lot of people want on other features outside of this set.
**Felix Becker (Anthropic)** 08:51 Yeah. So is the idea here to just decide on, like, what to include in it, and then those are effectively… Frozen, or is it also, like, where are there… attributes or schemas that are, like, you know, not… like, need to… need to be designed differently or spec'd differently to… so they can still evolve, you know, even after they're marked stable, but, like, in backwards compatible ways.
**Trask Stalnaker (Microsoft Corporation)** 09:18 Yeah, definitely, there's gonna be a lot of breaking changes in these areas, between now and RC.
Already.
So that, there's a variety of PRs in flight to rename things.
Do various things, but yeah, all of that would be, as long as it's in the… these core areas, we would want to discuss that and try to make those make that right before, RC.
Nice. At the same time, we do know that this area is… moving fast, and so unlike with, like, HTTP and database, where we had stability, and we haven't had any V2 since then.
We are anticipating in GenAI that we will need to have a V2, even in these core areas.
At some point.
But we should still do… we still, in this effort, we want to do as good of a job as we can.
in the RC initial.
V1.
**Felix Becker (Anthropic)** 10:36 Yeah, that makes sense.
Exciting.
**Trask Stalnaker (Microsoft Corporation)** 10:40 So the… I think the… we can definitely spend some time talking about, things that you have. What would be really great is if you have… do you have issues open for things already?
**Felix Becker (Anthropic)** 10:58 I have not gone through, an opened… issues, I could… probably do that pretty quickly. What's the… are AI-written issues acceptable here? Or is that, you know, I don't know what the etiquette is.
**Trask Stalnaker (Microsoft Corporation)** 11:20 Yeah, so, so we're… we're… this meeting… this group is meeting 3 times a week, Monday, Wednesday, Friday, so we have lots of chances to sync.
We are… kind of trying… right now, we're still kind of figuring out how to work and chip away at these issues. We did create an initial board with the issues we want to, that we think, you know, we need to, work through.
And I was finding… so what I did, because I was finding there's just a lot of issues here, and it's kind of… we need to figure out how to spread this work out and give ownership to people to start driving these, so… What… the first thing I wanted to try to do today was just to, Present these, kind of, categorization here, it's just in the Word doc for now, but, probably would try to figure out how to put this in GitHub, but… different categories. We've got a bunch of things around the JSON schemas, content capture… Naming, inference.
different pieces. These are just kind of… What felt like cohesive fish chunks that… Somebody could volunteer to drive those issues.
And then definitely, Felix for what I would… ideally, I would like to have issues From the… for the things that you're facing, and then we can get those, you know, into these… Into our board, and into our, sort of categorization.
**Felix Becker (Anthropic)** 13:18 Yeah, I could probably file issues today.
**Trask Stalnaker (Microsoft Corporation)** 13:21 Awesome.
**Felix Becker (Anthropic)** 13:28 I think some of these are probably also existing issues, so I'll make sure to look at that. Like, I saw the, like, the tool results and, like, the discriminator generic part stuff, and, like, no, those are the exact same things that we've also noticed.
**Aaron Abbott (Google LLC)** 13:48 Yeah, I just… I found some issues for that, and then, if you scroll to the top Trask, I just put, like, an Uber issue there.
But if you have more detail, or, like.
you know, obviously things specific to Anthropic that we haven't, explored super deeply.
Yeah, you can just file issues and can… Either add them here or work in the dock or whatever.
**Felix Becker (Anthropic)** 14:11 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 14:15 And definitely the, you know, the scope is, It's not in stone, so it's, it's sort of our guidance for now. Like, we do need to keep things scoped fairly tightly to give us a chance to… hit those timelines, but definitely if there's other things that you want to propose, you know, for it, we can definitely have those discussions. Like, there's some things that we're not sure, like, feel like it would be nice to do, but we're, And potentially possible, depending on time and quality.
**Felix Becker (Anthropic)** 14:57 What are the things you're trying to keep out of scope?
**Trask Stalnaker (Microsoft Corporation)** 15:02 Things that we have no… we don't have a lot of experience with, so new things that haven't been, like, new semantic conventions, That we don't… haven't had semantic conventions, and we haven't had instrumentations implement, so we don't have, like, sort of… any experience, like, to say, okay, we tried it and it didn't work, or… Now, potentially, you've tried some things that we haven't, and so that experience can be… valuable.
But sort of… More net new things.
Probably… Trying to keep out.
Given the amount of time that every net new thing takes.
In the cycle.
But also, at the same time, native instrumentations are, like, really high priority for us, and so we love… your, you know, feedback from, I don't think we have… Do we have anyone? Well, Aaron, we have the Google folks, yeah, so…
**Aaron Abbott (Google LLC)** 16:17 Yeah,
**Trask Stalnaker (Microsoft Corporation)** 16:19 representing native instrumentations.
**Aaron Abbott (Google LLC)** 16:23 Yeah, that's in our Agent Framework ADK, but not so much in, like, anti-gravity itself, which, I think… So, you did ask, like, what we don't have in scope. There's obviously stuff we don't have any conventions for at all, which would be, like, coding agents, so we have kind of general framework-based multi-agent stuff.
And then we have… I think a couple examples of native instrumentation, but… Yeah, that, and then there was some security stuff I think we talked about last time, like agent identity and stuff like that is out of scope for now.
And then, obviously, these ones were undecided.
**Trask Stalnaker (Microsoft Corporation)** 17:03 And the Tuesday meeting is still a good time for moving forwards on, you know, new thing… something like coding agents or things that we don't have.
Today, because we definitely want to… we're hoping we'll… see how this Wave 1 stabilization goes, and if things go well, and we seem to have good involvement, then, you know, we can kick off the next wave after that, and sort of… Hopefully have some rolling, stabilizations over time.
**Felix Becker (Anthropic)** 17:37 That's good.
**Trask Stalnaker (Microsoft Corporation)** 17:40 So, Aaron, did I understand that I can put your name on here?
**Aaron Abbott (Google LLC)** 17:45 Yeah, let's do it.
**Trask Stalnaker (Microsoft Corporation)** 17:47 Sweet.
Alright, people, speak up if you, First come, first serve on picking your favorite topics.
A link to this, it's just a tab if you want to look at it.
In the meeting notes here.
**Aaron Abbott (Google LLC)** 18:15 How about you, Trask? Anything you're interested in?
**Trask Stalnaker (Microsoft Corporation)** 18:19 Yeah, but I, I don't wanna… I don't wanna give other people, the first… crack.
I love naming.
Token usage.
**Aaron Abbott (Google LLC)** 18:48 Got a comment. Surya's interested in agent and workflow side of the flow.
Awesome.
I want to say Loudmilla probably for the token usage, just since we already have that PR, but I think it's kind of a big topic, or there's, like, a lot of… Maybe open question still?
**Trask Stalnaker (Microsoft Corporation)** 19:21 Yeah, I also… she'll be out for 2 weeks, or… Let's… wait, maybe… because I'm, I can put my name here for now to help drive that, maybe until she's back.
I'm just gonna do it.
Everybody else hates naming, so… Rightfully so.
**Felix Becker (Anthropic)** 20:03 Yeah. I'm not very happy with a lot of denying, but I feel like it's better for me to not take this. I've decided to not care.
But this is mostly because a lot of the naming doesn't match the Anthropic API terminology, but the OpenAI naming terminology.
**Neil Yashinsky** 20:25 Anyone want to join me on inference? I'm happy to take inference or contribute on inference.
Anybody wants to, co-join, or… Leave me hanging is also a fun option, too, I feel like. Hanging in the wind, that's totally valid. I would do the same, honestly.
**Aaron Abbott (Google LLC)** 20:43 I'm happy to help out. I think the parts stuff is pretty much hand-in-hand with the inference, so if you want to chat, yeah, I'm happy to help out.
**Neil Yashinsky** 20:52 No, that'd be great, yeah.
Yeah, I'd be happy to, like, you know, Pride, Copilot on the other one, too, with you.
**Trask Stalnaker (Microsoft Corporation)** 21:03 Aaron, I know you've… This is, I think, your PRI. You… Probably… No, this is… this is… Billy's… you had the… did we ever… did we already merge the entity?
**Aaron Abbott (Google LLC)** 21:19 I don't think so, unless…
**Trask Stalnaker (Microsoft Corporation)** 21:21 Okay.
**Aaron Abbott (Google LLC)** 21:22 You merged it.
**Trask Stalnaker (Microsoft Corporation)** 21:23 Oh, this is… here it is, got it. I was like, why isn't it here?
**Aaron Abbott (Google LLC)** 21:27 Yeah, this one is… it's… it's kind of related, but I… I don't know if… So there's a couple Googlers who are helping out with this for the ADK stuff on, Just some coworkers who are helping out with the instrumentation for the Nesting and the handoffs and all that stuff.
I don't know if they would… I could ask them if they're willing to help drive this, but, Honestly, I don't have a ton of context beyond that PR.
**Trask Stalnaker (Microsoft Corporation)** 22:00 Okay.
Fair.
**Wolfgang Therrien** 22:02 I could… I could take a look at it, at the identity and hierarchy stuff, and try to tease it apart.
And see how far we can get on it.
I think it might be related heavily to, like, the workflow… the workflow stuff, maybe?
**Trask Stalnaker (Microsoft Corporation)** 22:31 This, aw.
So, new PR… This one, I think, is fairly straightforward, both of these issues.
So I think that's… I'm not too worried about that one. Tours… Anybody like tools?
Would anyone want to put their name on tools.
**Aaron Abbott (Google LLC)** 23:11 I, I wonder if…
**Trask Stalnaker (Microsoft Corporation)** 23:13 Sure.
**Siri Varma** 23:13 Oh, right.
**Aaron Abbott (Google LLC)** 23:15 I wonder if on tools, like, the definitions are kind of inference-related, unless we're talking about how they're inferred, like, from code or something like that, but… the… I don't know, like, you know, obviously none of these are perfectly orthogonal, but what do you think?
**Trask Stalnaker (Microsoft Corporation)** 23:31 Yeah.
**Neil Yashinsky** 23:32 Yeah, I was thinking similar, honestly. I didn't want to be… Whatever, overbearing or whatnot.
I definitely would help with, you know, because especially there's only a few of them in tools, and like you said, they're related.
**Aaron Abbott (Google LLC)** 23:47 Cool.
**Neil Yashinsky** 23:48 And company. Yeah, anybody else who's like, wait, I'm not sure where to join in, like, that's a great place.
**Felix Becker (Anthropic)** 23:56 Yeah, honestly, I probably have thoughts on a lot of these issues across the category.
**Neil Yashinsky** 24:02 You've got notes, we're willing to take notes, Felix.
**Felix Becker (Anthropic)** 24:05 I didn't put my name on any…
**Trask Stalnaker (Microsoft Corporation)** 24:08 We also need PR reviews.
**Felix Becker (Anthropic)** 24:11 Yes.
I am very happy to help with that.
**Wolfgang Therrien** 24:20 I know that we also had… this isn't in this list, so I'm just kind of interested in gauging folks' appetite for it, but we talked a lot about cost. I think we've had a handful of discussions around cost.
Is that something we have any interest in trying to stabilize now, or do we want to punt on that?
**Trask Stalnaker (Microsoft Corporation)** 24:40 I think in, I mean, the token usage is in scope.
All of that stuff.
But doing, like, client-side, you're talking, like, client-side cost?
tables, that kind of thing, I think probably, I would think is not in scope.
**Wolfgang Therrien** 25:01 Even if it's just sort of, like, the… The output, not necessarily, like.
Yeah, I mean, I think that's fair. I think this is already a long list.
But, like, we can see if this goes well, then maybe it can make it into the next one.
**Trask Stalnaker (Microsoft Corporation)** 25:18 Yeah, I mean, I think.
**Felix Becker (Anthropic)** 25:20 Emmitting cost attributes is very hard.
For us, and, like, or basically impossible, at least on, like, API requests, because billing is always asynchronous, and so…
**Wolfgang Therrien** 25:31 Yeah.
**Felix Becker (Anthropic)** 25:32 Maybe it could be metrics, but, Yeah, I'm somewhat happy for now to just emit token usage, and a lot of the platforms I've played around with seem to just, like, give estimated cost, which is fine, like, I would leave it to the platforms for now, because it's just, like, a very complex thing to calculate.
Synchronously, or, like, we can't calculate it synchronously.
**Trask Stalnaker (Microsoft Corporation)** 26:00 Yeah, I understand it's a very popular user request.
It definitely is.
**Felix Becker (Anthropic)** 26:06 Popular from users.
**Neil Yashinsky** 26:08 Trask.
**Felix Becker (Anthropic)** 26:09 It's one of those, like, how hard can it be things.
**Neil Yashinsky** 26:11 I put… I put 3 links, I think, in there that are, like, related to, like, cost conventions and things like that. I don't know how deep you needed it to go, Felix, but there's 3 separate ones, I think, that are in… that are… unless I'm… I'm… Incorrect, but looks like they're, defined on the project board.
And I always get it mixed up.
**Trask Stalnaker (Microsoft Corporation)** 26:30 Yeah, but I don't think that we will…
**Neil Yashinsky** 26:34 It's not part of the…
**Trask Stalnaker (Microsoft Corporation)** 26:36 Or…
**Neil Yashinsky** 26:36 Compared to the idea.
I…
**Felix Becker (Anthropic)** 26:39 I think on the list, there's, like, you know.
I'm way more, interested in just making sure that we, like, figure out all the content, capture, and tools, and, infrastructure spans, all that stuff, before getting started.
**Wolfgang Therrien** 26:56 Yeah, I think getting… getting a token usage nailed down, I think, even for estimated cost, makes, you know, makes… certainly makes that job a lot… a lot easier.
**Trask Stalnaker (Microsoft Corporation)** 27:07 We should discuss this in the Tuesday meetings. I mean, it is a… Given the… how popular of a request it is.
**Wolfgang Therrien** 27:18 I'll bring it up there.
**Trask Stalnaker (Microsoft Corporation)** 27:20 Yeah.
That's kind of what I think we need a… We need to prove out that there's something useful that we can do there, before, sort of, we think about the step of stabilizing.
**Aaron Abbott (Google LLC)** 27:42 I might go ahead and volunteer, I will check with him, but I might go ahead and volunteer, For, yeah, Dylan, for a content capture.
We'll put it down.
Yeah, and I'll chat with him.
**Trask Stalnaker (Microsoft Corporation)** 27:56 Alright, I think that's looking good, because this one is, This one… I mean, this one is… Simple… Although… If anybody wants.
Why don't we get a name?
Here, what's,
**Neil Yashinsky** 28:17 passing through.
**Trask Stalnaker (Microsoft Corporation)** 28:19 Period.
**Siri Varma** 28:20 Yeah, Ivan… Teja Luventus.
**Trask Stalnaker (Microsoft Corporation)** 28:26 Yeah, and even if you can just check the PR here, see if it, you know, resolves them and help review and help, kind of, shepherd that PR through, that would be fantastic.
**Siri Varma** 28:41 I had one question. So, I was just looking at one of the PR, right, PR… for example, it's Epic PR475, or one of the first PR in inference, there are already some comments I see from Dylan, for example, on 475. So… Is it that… We drive this to completion, or just trying to figure out how this thing will work.
That's it.
**Trask Stalnaker (Microsoft Corporation)** 29:08 Yeah, so what I'm thinking is, what I'd like to do in these meetings, in our, you know, treating these as kind of checkpoint meetings.
Where, you know, People could basically share what the progress is, if there's, you know, blockers, if they, you know, if there's certain issues that have been raised in the PRs that Are, you know, tricky, and that, you know, would help for us to discuss synchronously here.
So, yeah, sort of like the… Representative from this group to drive that section.
**Siri Varma** 29:49 Okay, okay. Yeah, that helps.
**Trask Stalnaker (Microsoft Corporation)** 29:59 Cool, So, I mean, that… I feel like that… that was what I wanted to accomplish today, thank you.
And thank you, everyone, for… Every… so many volunteers, appreciate that.
**Wolfgang Therrien** 30:11 I think there's one… there's errors at the bottom that has nobody, attached to it. If there's any… anyone with a helium hand that wants to…
**Trask Stalnaker (Microsoft Corporation)** 30:23 That probably, Probably Ludmila and myself.
Yeah, definitely, if anybody, Wants to, for example, Take token usage.
And we can… not everybody's here today, and we can, you know, shift things around, but… For sure. Yeah.
**Wolfgang Therrien** 31:03 this… this breakdown is, I think, extraordinarily, like, useful. Have other… have a lot of other, like, working groups used, like, this kind of model where they, like, they sort of, like, stabilization push?
Like this? Like, structured in this way?
**Trask Stalnaker (Microsoft Corporation)** 31:20 So, sadly, the stabilization pushes in the past, have mostly been, Lyudmila and myself, and maybe one other person.
And, they have, So, we're blessed to have lots of people here, which is why I want to… Decentralized work.
**Wolfgang Therrien** 31:44 For sure. Cool.
Awesome.
**Neil Yashinsky** 31:50 Well, thanks for all your, thanks to you and Lyudmila's, previous past help, and, kudos, Trask for, doing yeoman's work.
Yo, people's work.
**Trask Stalnaker (Microsoft Corporation)** 32:01 Yeah, the, I mean, this is our first stabilization wave with, AI tooling, so, like, I was looking at this project board, and I'm like, I don't understand this project board, it's too… like, I need to categorize it. So, yeah, I mean, you know, it took a little time working with AI to Create this kind of category breakdowns, but… Yeah.
**Felix Becker (Anthropic)** 32:30 Is there a Slack channel for the stabilization specifically, or are we just using the GenAI Instrumentation channel?
**Trask Stalnaker (Microsoft Corporation)** 32:40 just using the GenAI channel.
**Felix Becker (Anthropic)** 32:42 Okay.
**Aaron Abbott (Google LLC)** 32:47 I'm looking forward to hearing more of your feedback, Felix. I don't know if you would want to join next Tuesday and, Like, if you have high-level themes.
**Felix Becker (Anthropic)** 32:58 Like, across the board.
Yeah, maybe I can… maybe I can,
**Trask Stalnaker (Microsoft Corporation)** 33:03 Yeah.
**Felix Becker (Anthropic)** 33:03 Like,
**Trask Stalnaker (Microsoft Corporation)** 33:04 Yeah, the Tuesday meeting is… is a great time to stop by, like, for kind of more extended chats.
**Aaron Abbott (Google LLC)** 33:10 Yes.
**Trask Stalnaker (Microsoft Corporation)** 33:11 Love to hear.
**Felix Becker (Anthropic)** 33:13 Yeah.
There's a lot.
**Aaron Abbott (Google LLC)** 33:16 distance.
I agree.
**Trask Stalnaker (Microsoft Corporation)** 33:19 But yeah, start with those issues, that'll be great.
Look forward to it.
**Felix Becker (Anthropic)** 33:22 Yeah, I have Claude on it right now.
**Aaron Abbott (Google LLC)** 33:27 Checks out.
Alright.
**Trask Stalnaker (Microsoft Corporation)** 33:30 Alright, then.
Thanks, Al. Thank you all, and yeah, well, let's, make some progress in, I don't know, this afternoon or Monday morning, hopefully. We'll see, I know the next meeting is barely around the corner.
**Neil Yashinsky** 33:45 Yeah.
**Felix Becker (Anthropic)** 33:45 Yeah.
**Neil Yashinsky** 33:46 Thanks, Jack. Thanks, everyone.
