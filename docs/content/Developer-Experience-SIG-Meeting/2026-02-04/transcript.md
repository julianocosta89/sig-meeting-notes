SIG: Developer Experience SIG Meeting
Date: 2026-02-04
Duration: 27 minutes
Zoom Recording URL: https://zoom.us/rec/share/ZJxA9YgGNtn-Jb_5TKgnQqbWgRYtI6LjrczoptfubP4UoAWpQwW8weKD_4TXInjf.HcceZlaF6rDL9u_X
============================================================

## Zoom Recording Transcript

**Johanna Öjeling** 01:15 Good morning.
**tristan** 01:22 Morning.
**Juliano Costa | Datadog** 01:23 Hello, hello!
**Johanna Öjeling** 01:25 Sweet.
**Juliano Costa | Datadog** 01:26 Morning.
**Johanna Öjeling** 01:28 How was the faster and hotel-on-like?
**Juliano Costa | Datadog** 01:32 Fosden was a mess, too, too, too much people, I, I didn't like that. Did you get sick?
No, I mean, not yet. I think… but I was, I wasn't… I wasn't on any session.
it was too much people, and I couldn't get into the talks that I wanted to, so I just gave up.
**tristan** 01:58 Oh, wow.
**Juliano Costa | Datadog** 01:59 Yeah, but Auto Plot was great. Yeah, really enjoyed it.
**tristan** 02:06 tools.
**Johanna Öjeling** 02:07 here. What, what did you do during the day?
**Juliano Costa | Datadog** 02:12 So, we… we had… so, the, the, the…
the event was an unplug, unconference, so we wrote down, like, ideas to talk and discuss, and put in a…
Like, you know, all, whatever.
the board. And then, I think Ted, Austin, and Severin, they split the rooms, so then everyone that wanted to discuss on this topic, they joined and discussed.
So, we had two… two sessions, two rounds in the morning and two in the afternoon. And after those two rounds, we had one represented from each group sharing what they discussed, like, in a one-minute summary. So, it was nice.
Related to the dev app, there was a MCP discussion that I wasn't part of it.
I don't know.
**tristan** 03:12 Oh, really.
**Juliano Costa | Datadog** 03:12 Well, we do have the summary, but I was in the hotel blueprints one.
And I had the chance to kind of bring up what we were doing, related to the blogs, and discuss a bit with them and the group about what is the idea for blueprints, and how we can maybe even collaborate with them with the stories that we already have.
So, this was a nice thing.
The MCP… I wanted to attend the MCP one, but I think it was on the same time that someone wanted to discuss… well, a group of folks wanted to discuss some things related to the hotel demo, and I was the only maintainer on the hotel demo there, so I said, well, maybe I need to go to this room.
**tristan** 04:02 Well, that's good about the blueprints, though.
And you did… did you man a booth?
**Juliano Costa | Datadog** 04:11 So, there, there were, sponsors, but there was no booth.
Oh, so… I thought you said that.
Yeah, I… Rafuna, Datadog, New Relic, what is the…
Well, there were, sponsors, but the only thing that we did was, like, putting stickers on the…
**tristan** 04:35 registration desk, that was it. There was no…
**Juliano Costa | Datadog** 04:39 vendor's booth, or anything, so… which… but was good, actually.
I… I… Wouldn't like to stay in the booth and lose the whole event.
**tristan** 04:50 Yeah, that's true, but it's nice to be able to get free stuff.
Legal in the field.
**Juliano Costa | Datadog** 04:55 But…
**Perk (Marcin Stożek) | Elastic Ingest** 04:57 There was no free stuff.
But the food was…
**Juliano Costa | Datadog** 05:02 The foot was really good.
**Perk (Marcin Stożek) | Elastic Ingest** 05:04 Oh, food was a… yeah, very good. Going back to the topic of what was being discussed, Juliana, you mentioned that there were these documents. There is a doc, and all the notes are in there, so if you guys are interested, then just…
Skips from that.
**Juliano Costa | Datadog** 05:21 I can.
I will bring that up, because maybe we can take a look at the…
At the MCP one. Any chance you were there?
Park?
**Perk (Marcin Stożek) | Elastic Ingest** 05:37 Unfortunately not.
**Juliano Costa | Datadog** 05:38 Okay, yeah, no worries.
**Perk (Marcin Stożek) | Elastic Ingest** 05:40 I had the same problem as you. They were, like, 10… 10 tracks at the same time, so you just…
Neither to choose.
**tristan** 05:51 Oh, weird.
Well, you can… Oh, there's the link. Okay, we'll discuss that after we discuss blog posts, I guess.
We can look at it.
As we discussed, updates to the MCP server, proposal.
Cool.
Yep, and we can get started.
Mmm…
**Johanna Öjeling** 06:15 I added the first two agenda items. One is about the Skyscanner blog post. Neil has been active reviewing it, and added some comments, and he also shared the configurations.
So that's great. And he also wanted to ask some more, folks from Skyscaler to review it. But I think… yeah, I think it can be,
Ready, pretty soon.
Which also brings me to the second point. Do we have any timeline for when we want to publish these blog posts, or do we want to publish them in a certain order, or…
**Juliano Costa | Datadog** 07:00 The initial idea was… was to publish in a certain order, but, order, but, Mastodon was really…
Taking a long time to reply, so we just gave up that idea.
**Johanna Öjeling** 07:15 Mmm, okay,
**Juliano Costa | Datadog** 07:16 the only thing that changes is that I will need to change the intro on the… on the Mastodon blog post, and maybe we mention that in whatever post we go first. Like, hey, this is a series of posts, like, explaining why we are publishing this.
**Johanna Öjeling** 07:37 Yeah, I see. Okay, yeah, but then we can coordinate whenever a post gets ready, we'll, yeah, bring it to the… it's the OpenTelemetry I.O. recall, right? Okay, cool. Thanks.
**Juliano Costa | Datadog** 07:51 But seeing the pace that you are with Neil, I think maybe Yara will be the first one.
Yours will be the first one, so we can…
We can align on that. The Macedon one, I think I addressed all the comments. There are some just pending, some pending up things from team, and the final approval, so…
**Johanna Öjeling** 08:16 Okay, yeah.
Yeah, I'll, yeah, I'll check… I'll make sure to get Neil's final approval as well, and then, yeah, we can see which comes first.
**tristan** 08:29 Yeah, I gotta ping Dunks again, because they… Said they were gonna reply.
Within the week, and it's been, like, 2 weeks.
Almost 3 weeks, so… I got it.
Bother them again. Alright.
Well, that's good. Hopefully we… Finally get one out soon.
Maybe that'll start the ball rolling.
if there's nothing else on blog posts, we can move to MCP server stuff, or…
I see it out to unplug notes, so good.
**Juliano Costa | Datadog** 09:07 So, just, I just shared another document here. So, the second one is the schedule.
For all the breakout sessions. And then at the bottom, there are the documents, all the notes documents for all the rooms.
The first link is just the MCP one, but,
If you want to take a look, for instance, at the blueprints and best practices, that's, Rome 8A.
So it's another document.
**tristan** 09:39 Okay. Yeah, I just… Gotta open the MCP server… Session notes…
Most people came to listen, so…
Might not have much in the way of… new information…
Or information related to us,
What's A2A? Does anybody know what that is? Doesn't matter if it's MCP, A2A, or Claude Skills, the goal is to… what's an A2A?
**Nicolas Wörner** 10:19 A2a is kind of another protocol how agents communicate with agents. So MCP is about how…
Access to tools with the standardized protocol and.
**tristan** 10:30 Easily.
**Nicolas Wörner** 10:31 Our agents can talk to each other.
**tristan** 10:33 Okay.
I have one quick, MCP server versus skilled? MCP server seems more… secure. Is that…
It just seems more… Like, you're in control, versus skills, which just kind of…
**Nicolas Wörner** 10:52 Right, right. So…
Mcp servers can be more secure, but just because you use an MCP server doesn't mean it is more secure, so the point is you can add authentication to MCP servers, which is not the nicest thing to do, because it requires some work to be set up, but yes, you can do it. And for skills, it's just a markdown fiber or binary you execute.
**tristan** 11:13 Right. And there's not really any…
Yeah, there's no… it's just like, here's the HTTP…
**Nicolas Wörner** 11:21 Right.
**tristan** 11:21 Do the skill, run it.
**Nicolas Wörner** 11:23 Yeah. Yeah.
**tristan** 11:24 Okay.
But I'm sure that'll be fixed eventually, where they'll have some sort of…
Better way of doing skills. Which SIG does it belong?
**Nicolas Wörner** 11:39 I think that's the question we all ask ourselves these days.
**tristan** 11:44 Yeah, and so this is what connects it to the DevEx SIG, so someone there brought up it was in the DevEx SIG, that's good.
**PL Pavol Loffay** 11:53 Yeah, I think the argument they're making, like, the GCs is, since this is cross-seq effort.
What they suggest is to… Kind of narrow down the scope and start, let's say, in the collector sig.
**tristan** 12:09 Solve the, kind of, collector use cases, and then…
**PL Pavol Loffay** 12:14 If we will start working on, let's say, use cases around cementing conventions, then move this project under the cementing conventions sake.
**tristan** 12:23 Whoa.
**PL Pavol Loffay** 12:26 Personally, I still think that this could be long as well to the DevSig… direct sick,
Because it's… Oriented to end users, developers, and we will be looking at the…
kind of, you know, cross-project. You don't want to necessarily work in one thing and then kind of move to another one.
I have, as well, Sarah, not sure if you've seen, made some suggestions on the pooling quest, on the proposal.
And there will be a meeting this Friday, probably?
with him and Mila, and probably other GC members to discuss the MCP proposal. I hope it will go through, because the suggestions he made was, like.
This is kind of our first attempt,
And it's kind of like a research project, and we will see… we will experiment, and we will see where it goes, actually.
Which I'm totally fine with, because the space moves so fast, and we need to figure out what is gonna be the right approach.
But we should start moving forward and start building some use cases and something that we can deliver. If some things will change, that's fine, it's normal, right? But…
I think we all just want to get started and have something that people can use.
**Nicolas Wörner** 13:55 Yep.
**tristan** 13:56 Yeah, I think… I mean, to me, it makes…
if a SIG, like, semantic conventions wants to own an MCP server, it makes sense that they would, but do they? And so putting it under semantic conventions only makes sense if they're looking to own semantic… looking to own an MCP server,
**PL Pavol Loffay** 14:18 Yeah, I think we should, like, you should definitely respect the…
**tristan** 14:22 Right.
**PL Pavol Loffay** 14:22 then the Sikh owners, if they want to build something in a way they want to build it, because they are experts in the domain, but our goal is to kind of bridge all this together, so it's kind of consistent and coherent across the ecosystem. And they see this as a challenging goal, because not…
They don't have projects like this in the ecosystem.
Which I think, is challenging, but for the end user, it's…
It's something that end users would actually want to have, like, something that works across.
**tristan** 14:59 Hmm.
The, before I go back to going through the notes, what… you already had one GC meeting, right?
**PL Pavol Loffay** 15:11 Yes, I was there last week.
For the first 15-20 minutes,
Yeah, I think these were the main concerns. It's like, the scope is too ambitious.
its cross-seq is something that hasn't been done before, which is hard to believe, but this is what I got, and…
They just want to make sure that we will play well with other six, and…
We would respect what they think and what they build, right?
**tristan** 15:46 Yeah, makes sense.
**PL Pavol Loffay** 15:47 It's like, yeah, I don't see it as a problem, honestly, because this is, like, how we should work anyway. It should be done in this way, that we…
We just collaborate, and they own their space. We help them to…
We will just help them if they want to build something.
**Nicolas Wörner** 16:11 again, For Christmas.
**tristan** 16:13 You mentioned… oh, what's that?
**Nicolas Wörner** 16:16 Probably in particular for you, Pavel, but for everybody.
Which is, again, about the deliverables, in case this still stays a concern that the goal is too broad, or it's too much what we list down there. Do you think it makes sense to just focus on the collector for now, but still try to establish or keep it as a cross-cutting SIG with the background that we, first of all, want to have that central place we discussed, because we think it's beneficial?
We have that in a
cross-seig setup, and then later on, focus on other use cases to simply to slim down the proposal, and maybe to increase the chances.
**PL Pavol Loffay** 16:55 Good.
**Nicolas Wörner** 16:55 Getting through, or you think we should keep it as it is.
**PL Pavol Loffay** 16:59 Absolutely, if they think we should just… we're in the collector seat, let's do that, let's… let's… because this is what we want to solve, is the biggest issue, and
In the meantime, we can kind of experiment with the graphic config or semantic conventions, how to package them,
Yeah, let's do that, let's get accepted,
In whatever forms to, kind of…
the best for the GC to get accepted.
**Nicolas Wörner** 17:36 I think so, too. The important thing is that we finally get started, but still, it would be awesome to be able to do the work here as part of the DevX group, I think. Simply, we already see it here in the proposal that other people who might be interested in similar use cases for not the collector, but I think the handshot operator or something like this was mentioned.
That we have that entry point, or that place where people can come to to learn more about MCP or AI-related tooling in context of OTEL. And there, the DefX SIG, in my opinion, would be awesome, to have that central place.
So, that means we should wait for the meeting on Friday, or what do you think?
**PL Pavol Loffay** 18:21 Yeah, I'll… yeah, let's wait. I will… Trying to get in…
Did you get you invited as well? Would you like to attend?
**Nicolas Wörner** 18:30 Yep.
**tristan** 18:33 Hmm… Let me see more in the notes…
Lots of questions, not many answers.
**Juliano Costa | Datadog** 18:55 Love that there is a comment here,
No one currently knows how to write a MCP servers well.
Maybe in… yeah.
I'm pretty sure don't, but I know that there are some folks that know.
**tristan** 19:15 Well, I wonder if they mean, like, anybody, anywhere, like…
**Juliano Costa | Datadog** 19:18 Yeah, privilege.
**tristan** 19:20 Yeah, so new, I don't know.
**Nicolas Wörner** 19:28 I think that's the whole point of the project, right? Nobody knows how to do those all.
**tristan** 19:33 Right, I love it.
**Nicolas Wörner** 19:34 Wait.
**tristan** 19:36 like, the… Yeah, that's why I think it also should…
makes sense to be in the DevEx SIG that we're… the other SIGs can learn from us if they decide to write in CP servers, and…
**Nicolas Wörner** 19:47 Right.
**tristan** 19:49 Mmm…
**Juliano Costa | Datadog** 19:52 So, one nice thing about the Hotel Unplugged was that we had a bunch of, end users?
So that was good to get feedback on their struggles and their pains.
But it would be awesome to know who attended each session, but that's against the rule that they set at the beginning.
**tristan** 20:14 Oh, yeah.
**Juliano Costa | Datadog** 20:15 conference.
So… We don't know who was there, otherwise we could ping and try to get more, insights, but…
**tristan** 20:24 Adam has rules for…
Interesting. The… I see this other one, it says, we already have an MCP semantic convention server in Weaver.
Is that the case?
**Juliano Costa | Datadog** 20:41 I… wasn't aware of this.
**Nicolas Wörner** 20:45 I think they recently came up with one, quite new, a few weeks ago, where they did some experiments, but it's not, like, something super mature, super established, I think it's also an experiment.
**tristan** 20:57 Okay.
**Nicolas Wörner** 21:37 So I think, personally, for me, the main takeaways, which I get when I read the summary here is, essentially, there are a lot of different use cases. It could be dev time tooling, but also day two operations, which are both very valid use cases, I think.
Then, from what I read in the summary, is the whole security concern that we need to be very cautious about if we give the MCP server or the agent at the end of the day access to something, that we need to take conscious decisions about what it can do and what it cannot do.
And, that nobody knows how to do, things in regarding of AI tooling the right way today, so we need to figure it out. We will certainly sometimes go into a direction which we might change on later.
**tristan** 22:24 So we need to keep in mind whenever we take a decision that this might not be the final implementation or the final decision for now.
**Nicolas Wörner** 22:31 And yeah, I think this makes a lot of sense, everything which is mentioned here.
**tristan** 22:44 Yep.
Yeah, I just read the summary.
That's about right, and… Maybe this will bring some more people in, because… links to… the proposal…
Man, it looks like it.
Had a lot of discussion.
Seems people are interested, even if…
Everybody's still unsure exactly where they can go.
What else do we need to discuss?
Oh, I guess… Pavel, you're talking to the GC, and there's lots of discussion on
Just doing the collector have… Has the collector SIG been… have we talked to them?
**PL Pavol Loffay** 23:44 That's a great point. Yes.
**tristan** 23:48 Even on the pull request, there is…
**PL Pavol Loffay** 23:51 a couple people from the collector sick, kind of offering help to build the MCP, and I was talking to them about the…
the schema for the collector components, I was collaborating with them on that effort, and so…
they were very helpful, and they were aware we want to build MCP, and they always expressed, like,
Interest in it, and, offered help.
**tristan** 24:22 Yep, and no, like, they haven't been…
Saying they want it in their SIG or anything, right?
**PL Pavol Loffay** 24:28 Not really.
**tristan** 24:29 Yeah, okay.
But…
**PL Pavol Loffay** 24:34 I think this is, like, the thing that we'll need to figure out if the…
realize that the MCP server should be part of the collector, then we should open, like, a proposal for the collector component, find a sponsor, and…
And build it there, that's.
**Nicolas Wörner** 24:55 I think so too. So right now, here in the DevExSig, I think we would have a good starting point to start with an experiment, start with trying out what works well, what doesn't work well, and if we see that the MCP collector server would be, like, awesome and work very well.
We could think about adding it to the official auto-collector repo, but I feel like as a starting point for something, we don't know how well it will work. It would not be the best idea to do the active development and everything inside the collector, specific things.
**tristan** 25:27 I mean, it might just be something in Contrib anyway, right? So…
**Nicolas Wörner** 25:31 Yeah.
**tristan** 25:32 Which… Man, that's… Much lower bar to get into.
really start out there. So maybe start out…
Separate repo, contrib, and then eventually, if it proves itself, into the main repo.
**Nicolas Wörner** 25:46 Yep.
**tristan** 25:53 Okay.
Whoop.
There's… Nothing on the blog posts for the MCP server, guess we can wait until…
another meeting this Friday to hear more of where this is going. Hopefully it gets worked out soon. Sounds like it's going in our direction, but…
A few more things to work out.
I guess we can…
**Juliano Costa | Datadog** 26:23 I think from you, Tristan, and myself, we could take a look at Johanna's blog post.
**tristan** 26:31 Yep, I'm gonna do that today.
**Juliano Costa | Datadog** 26:32 Because then, if we have the two approvals from us, plus Neil's, then we're getting to go.
Move to up here.
**Johanna Öjeling** 26:43 Yeah, that would be great. Thank you.
**Juliano Costa | Datadog** 26:47 Cool. Yeah, hopefully we can get that out soon. Alright.
**tristan** 26:50 Well, we know what to do. Let's go.
I'll see you guys later. Everyone.
**Johanna Öjeling** 26:57 See ya. See you. Bye.
**PL Pavol Loffay** 26:59 You're buying.
**Perk (Marcin Stożek) | Elastic Ingest** 27:03 Bye.
