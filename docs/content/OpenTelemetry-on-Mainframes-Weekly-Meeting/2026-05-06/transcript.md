SIG: OpenTelemetry on Mainframes Weekly Meeting
Date: 2026-05-06
Duration: 43 minutes
============================================================

## Zoom Recording Transcript

**Jim Porell** 00:11 Hey, Richard, looks like you made it.
**Richard Nikula** 00:17 I should come off commute. Yep, I'm here today.
**Jim Porell** 00:20 Yeah, and I know we need to… Kill this Firefly's AI note-taker.
Antoine did it last week, hopefully Morgan joins, because I think he knows how to kill it, too.
**Richard Nikula** 00:38 These three little dots, let's see, don't…
**Jim Porell** 00:41 that view profile chat thing, and I want to pin it.
**Richard Nikula** 00:46 Nope.
Seems like something somebody that owns this thing has to do.
**Jim Porell** 00:52 Yeah.
**Richard Nikula** 00:53 Participants… Let's see, can we… Nope, came out that way either.
We should ask him. Fireflies, note-taker, how do we get rid of you?
**Jim Porell** 01:09 Yeah.
**Richard Nikula** 01:11 You should tell us.
**Jim Porell** 01:19 I see something, I'm going to claim host.
Oh, you need a key, forget that.
**Richard Nikula** 01:28 There actually is, on the chat, there's actually something.
It says F… FF leave.
the left.
**Jim Porell** 01:44 Hey, awesome.
**Richard Nikula** 01:45 So it was in the chat, it actually did tell us what.
**Jim Porell** 01:48 Yeah, alright, cool, thanks.
**Joris Yangsheng Xu** 01:52 Hello, everyone.
**Jim Porell** 01:53 Good to see you again.
**Joris Yangsheng Xu** 01:55 Yes.
**Jim Porell** 02:00 It was just Yoris, Antoine, and I last week, and Antoine gave a very nice, overview to Yoris.
I don't know where… let me see if I can find, Rick, rooted her.
**atoulme** 02:29 Hey, everybody.
**Jim Porell** 02:57 He's not showing online, unfortunately.
**atoulme** 03:03 Okay.
**Joris Yangsheng Xu** 03:08 I had some questions, about, Slack channel.
Is it correct that you need a… Clouds native?
email?
**Jim Porell** 03:25 No.
**Joris Yangsheng Xu** 03:27 No.
Okay.
I've tried to sign up for it, but I got an email of no account associated.
**Jim Porell** 03:39 I don't remember the process. I have to go look at the Google notes, yeah.
**Richard Nikula** 03:43 It has been a while since we did that, yeah.
**atoulme** 04:01 No, I mean, to gain… to go to a census like the fingers.
Probably an invite on the site or something, here.
You can use any email, including your own.
Sometimes it's a good idea to use your own in case you switch employers and you still want to just have one identity, but if not, let's see, a lot of people who have, like, the same person with three… the same names, 3 different persons on that Slack, just because they switched jobs, and they have to re-sign up with a different email every time.
**Joris Yangsheng Xu** 04:39 It's…
**atoulme** 04:45 It's fairly open, and then we have the Auto Mainframes channel you can join.
Alright, so maybe, let's start this meeting. So, I'm just gonna go and open the new meeting in the dock, make sure we got that going.
Me.
26… Attendees, You put your attendee information here.
Agenda… cure.
I'll just leave the first one open… Okay, as far as the agenda today… I do have one item I'd like to discuss, two, two items.
I'll just put them up.
If you want to go first, this is a good time to let me know.
Update on SIM call.
Partition… Okay.
Got two things going on.
**Jim Porell** 08:24 So, Anton, what's the S390X runners?
**atoulme** 08:28 Yeah, let's go. So, as you know.
We would love to, like, to test that everything works on A180X hardware.
We are having an interesting time, for example, with AX, where, we started to declare support for AX, we have it on core, we try to do it on contrab, and then computation would fail.
Datadog had dependencies that would not work on X. I'm guessing the exact same thing is going to happen to us when we try to make it work on S390X hardware. We need to run our unit tests on that, and some of those unit tests actually perform capture of data But, you know, maybe we can actually, and this is important, it's like, it's not so much trying to make everything work, it's just to carve out what is possible, so we don't make promises we can't follow up on. So, for example.
on AS390X if there is no support for some of the host metrics that are available because you know, the file system is different, the processes are not stored the same way, all that. That's completely understandable. Let's just make sure we put a great note in there, and then… So for that, it would be great if he had access to S390X runners, and the work that Rudiger has been doing, for the last, now 6 months, is to connect the Linux Foundation with, IBM to have some sort of contract that would allow Linux Foundation resources like ours to access GitHub runners.
hosted by IBM Cloud on that architecture, so we can actually test things.
Cure… you know, that's it, right? The GitHub runners themselves are written in something like Node.js, if I remember, which is compatible with S390x. And then from there on, we just use that as a process to run our tests.
The latest update I've had is that, there was a discussion between the two legal departments.
there's a legal contact for the CNCF.
about here… Discussion… Name of that contact is Jeffrey Sika.
But between him, Morgan, Rudiger, and myself.
We've had a… like, you know, a game of tag, where we… ask, you know, what's going on, and they're like, well, we're looking into it. The problem I have the most is that since February 3rd, we have no update from Jeffrey. His, latest update is still waiting. It sounds like it's a LFIT, LF legal… Discussion?
I'm picking on it again today.
Since then, we haven't heard anything.
And Rudiger has, asked him in April, on April 7th, asked him what was the latest. I've asked on April 24th.
And I'll ask today as well for an update. I still haven't heard back.
Okay. If there is a better way to reach out and make sure we are able to get some sort of a timely update, I'm all for it.
That's all.
Does that help?
So, if Rudiger was here, or if anyone working with Ridiger has any idea about this on the end, that works, if you have any skin in the game to support the OS and SP90X CPU architectures for Go, and particularly for the collector, so we can certify it works.
Here we go.
I know, I know ABM has done the work of making it work. Let's actually certify it.
**Jim Porell** 12:13 Okay, I added that note in there, so hopefully that's adequate for you.
**atoulme** 12:18 Networks?
Okay, the next one is, yesterday I was sitting in the maintainer com- discussions.
at 8 AM on Tuesday, there's a bit of a mix of a meeting between all the maintainers of the hotel are invited to attend. It's a public meeting, there's… you can join anytime. And, there's also discussion on semantic conventions and specification issues.
Because bent symmetry is actually just a big spec with, you know, a little bit of code on the side.
The idea is to use those moments to kind of bring all the maintainers together to agree on some big, traversal ideas.
I don't know if you… I think I brought it up in this meeting before, earlier this year, but there's been some interesting development around semantic convention, where they've reached terminal velocity when it comes to the complexities it can handle in one repository.
They don't have the SMEs in place, they don't know how to deal with everything. A good example, as outlined yesterday, is that they've decided to split specific domains out of the main Repository to make it easier to find the right people interested in maintaining some of those things.
The first element that is going to be split out, and I think already happened, is the Gen AI-type semantic conventions. They are also working with external communities, which is a bit of a new thing for me, where, for example, for security mappings, the OCSF community would handle semantic conventions.
For, for those type of events.
I asked who was next, according to them, in terms of importance, to be split into their own domain, or if they were going to split out an existing domain inside some conv.
Into a separate repo. And they said that they were interested to spin out mainframes in their own repository.
Has anyone heard about that?
Would you like to engage with me on that discussion?
No, okay.
Alright, so I got here, a little bit of a discussion in the comments from the roadmap, So, Ridiger, back in February, said, hey, I see open material and mainframes, we plan to contribute to this definition of semantic conventions in the following area.
Mainframe specific entities and related metrics.
For transactions, job processing, databases, messaging, and API. Instructor-related metrics, entities and metrics for virtualization, and Z, HMC API, that's the… your ZOS metrics.
Server spans for ZOS system software, MQ, KICS, IMS, DBTO. We'd like to ask for support from the SMCOM Committee for representing virtualization concepts and from EntitySIG for the definition of relationships in support of virtualization.
That was, I think, as succinct as it can be in terms of the involvement we wanted to have with Semantic Convention.
I think the feedback we're getting is.
we cannot. We cannot possibly take on all of this by ourselves, and I think you should feel free to go and do this directly in Git, separate from the Semantic Convention discussions, because that's too much.
**Jim Porell** 15:23 And so I think we discussed that, Antoine, and I think there was a, you know, there's an understanding that, yeah, there are definitely some unique things in the mainframe. We can spin those off.
Virtualization is not unique.
And so… you know, what, like, ZBM as an operating system is remarkably similar to Azure, Citrix, and that kind of stuff. So.
that kind of thing should be done as a community focus. We, you know, we don't want to drive off something else. And even database, like DB2 is a database. Well, there's a lot of synergy with database. We do have some unique characteristics that we would do on our own.
Right. But we don't want to be diff… so different that, you know, if somebody's looking at a database statistics, you know, it would be familiar to them, regardless of what platform they're on. Okay.
**atoulme** 16:22 That's great.
**Jim Porell** 16:23 Yeah, those were the important distinctions, but things like parallel sysplex, where we have a shared model, yeah, we have to do that on our own, and that's why it's been delayed. We're trying to do the things that are com… Complementary with other, with other, organizations first.
**atoulme** 16:43 Yep, okay, so I'm just gonna put that in… In the notes.
**Greg Shriver** 16:46 Is this, is… does… does this… is this… Related to the federated semantic conventions lifecycle stuff?
**atoulme** 16:56 Yeah, I think it's to make it so that you start to have… sameconf does not have to be bottled up in one repository, but it can start to refer… So what's interesting is, because Gen AI is going first, they're kind of getting the fresh paint of that, tooling.
And they're going through some maturations and some challenges, right? I mean, there are bugs and stuff to do, right? It's not free.
So, in a sense, it's also great not to be first. But if you want to see how they're doing, I think I'm gonna try to keep tabs on what's going on there, what type of kinks they're running into, if there's any trouble.
At the same time, if, so… If there are specific areas that we should start that would be maybe independent from the main SEMConv here, that also gives us a bit more license to kind of get started.
And, I… I've developed a bit of an appetite to go look at the HMI, because you already have a Prometheus exporter.
We could try to build the Weaver model by the HMC, sorry, by… by kind of, reverse engineer from the Prometheus, metrics into a proper model. It wouldn't be too much of a hassle to do that.
Does that make sense?
No, it's, you know, it's very comprehensive, the number of metrics you can get from a Prometheus exporter for… the HMC all the way to the wet edge of your power cord is, you know, very… very, very expensive, so, I mean, we need to… what would be interesting is that we first do a whole mapping of everything, and then we can actually come down and say, you probably want those 10 metrics, not 400 of them.
And here's what you use them for, and what you alert on, because… You might not care that much about the wattage of the power cord, but this particular file system usage needs to be, like, critical.
That might be a fun time for us to engage on, if you're… if you're game. So what that means also is that we can start to kind of de-correlate from the… from the main Semconv, we don't have to work at that pace, we can go a bit faster. We might need to unarchive the repository on GitHub.
That was built for our mainframe SIG, so that we can start to play there, and then find ways to reuse the tuning from GenAI to map it over to the main SIMCOV.
So, I think immediate action item would be looking to own archive this, repository.
open a number of issues related to things that Jim just touched upon, like, the things that are really specific to us that would be separate, so that there is a clear distinction of where are we working? Are we working here in the main one, or are we doing this that's something that's specific to to mainframes. And we don't have to be good about it, I just want to make sure we start to do that.
**Jim Porell** 19:52 Yeah, I think there was some thought that are we slightly different? Then we want to extend the common semantic for a particular topic. If we're very different, then we need to be unique. And the parallel sysplex, the clustering.
you know, clustering is a generic thing, but the way the main… or ZOS does clustering is very different. That's the parallel sysplex, so… That probably warrants his own thing.
again, basic transaction processing of kicks looks a lot similar to Tomcat, so… whatever's in Tomcat, you want to kind of inherit, and then if we do something different, maybe we work to extend it. But we have to work… I think what happens is there's subcommittees that we gotta work with better, versus trying to do this as a giant thing.
**atoulme** 20:44 Yeah, you're right, because it's a completely different, amount of work to go just look at kicks, just look at DB2, just look at virtualization, and just look at, you know, the HMC. So I think we could, We could just create those issues, and then we can just… You know, raise your hand if you want to work on this aspect.
And then we can go.
We could do that right now, if you… no, the, we need to unarchive this repository so we can create issues. Or… is there a place where we keep issues right now?
**Jim Porell** 21:18 That I don't know.
**atoulme** 21:19 Okay.
I think we've been using.
**Greg Shriver** 21:22 We started… we started working in Google Docs.
And then I think we transitioned over to… to the GitHub repository, which then get, you know, archived.
I don't know that we actually ever had started to populate issues.
**atoulme** 21:42 Alright, so…
**Greg Shriver** 21:44 Would it… would it make sense to take a look at, you know, you said that GenAI was the sort of the first one to go… the first penguin, basically, to jump in the water in terms of, the federated semantics?
Should we kind of look at what they do, or are we too early to separate out, or do you think it makes sense to just unarchive the repository that we had and go with that?
And make it conform later.
**atoulme** 22:14 You're talking to the wrong person. I'm very impatient. So, I…
**Jim Porell** 22:21 Oh, come on!
**atoulme** 22:23 Oh, no, no, no, it's, it's, it's, it's a…
**Jim Porell** 22:26 It's pretty obvious.
**atoulme** 22:28 But, I, I think, so… there's nothing wrong with unarchiving things and opening issues. I just want to make sure we… we execute together, right? I'm just… I'm just.
**Greg Shriver** 22:43 Yeah.
**atoulme** 22:43 things that I actually don't know, like, if we have the right stakeholders in today in the call, but we can we need to move, towards this. For the Gen AI, I think we… could ask Ludmila to join us next time, next week, and have her… maybe run with us around this, and she can say, no, alright, it's what it is. But she's been helping them, so that might be also great for her to be able to kind of Explain to us how to get started in a way that is convenient, and we don't have, like, as much soul-searching, but if you look at it, a week's time is not that far, right?
So, we can definitely just, in the week to come, unarchive this repository.
And just make sure we maybe open issues so that we are ready for things that we think are good. And when we talk with Lumina, either in this meeting or maybe a different setting.
She can… she can just bounce off those ideas and say, okay, start with this particular issue here.
And let's go and just do a skeleton of what that would look like to map it out, and work from there.
If she tells us it's too early.
Okay, surely. But I don't think that's the message I got. I think the message I had was, yeah, we're, We're playing with the final aspects of integration, meaning the publication of those things together is actually pretty difficult, right? Because this is where you federate everything back up.
But if it comes to having, for example, expressing a dependency, so like you mentioned, Jim, sorry.
For DB2 is like any other database, except those three things is doing differently, for example.
well, you want to take the database some conv, and then say, I'm taking this, and I'm adding those additional things. I think that is supported today, based on the discussion I've seen in the Weaver tooling, so they, they should not be able to do a, a, a resolution of a remote, definition using, you know, HTTP links and you know, good old semantic web-type things, right? Just, being able to refer to a resource outside of your current repository.
So, yeah, I can at least ask her.
If that's… if that's okay with everybody here.
**Jim Porell** 25:01 Okay, alright, sure.
**atoulme** 25:03 Alright, let's do this. So, I'm just gonna put some…
**Jim Porell** 25:08 We might also have to figure out a better time, because Rudiger is kind of like the… our leader, and I think this team is really… this time has really messed with him, because I think it's 6 PM his time, and I know he's doing a… he always seems to be driving his kids someplace, and… 12.30, he seems to be able to come back, Or my time, 12.30, his time, 6.30.
**atoulme** 25:33 Yeah, so, okay, that… let's put that as an action item, too, so… Look at, unarchiving.
Repository, opens some issues. Meh.
No need to be complete, we just want… read the fuller… Invite.
Here I'm gonna try not to butcher her name, Ludmila.
to present… And work with us on a first escape.
Okay, and then you said, A gym.
Look at finding a suitable UMEA time.
Okay, if it's too late for him, which I get, right? I don't want to work at 6.
**Jim Porell** 26:32 No, no, it was later, before. What happened was it got moved earlier, and and that was a problem. It was good for a lot of other people, but… It doesn't seem to be working out for him.
**atoulme** 26:44 In that case, should we just ask him over Slack?
**Jim Porell** 26:50 Yeah, that's probably not a bad idea.
**atoulme** 26:52 Okay.
Ask Rudy Gear.
What was like.
For a good slot.
Rookie.
I actually do need to jump myself to prepare on something about mainframes as well, so… Gotcha.
But yeah, thank you, folks. For me, I have enough that I can start to work with you on making sure we have a continuation of the effort, and I wanted to let you know about this SP90X runners, because I'm feeling frustrated about this, but I just don't know.
**Jim Porell** 27:26 Yeah, no.
**atoulme** 27:27 Legal recourse, or anything like that.
It's not… I don't think it's actually legal, I think it's more, like, inside the Linux Foundation, how to make a… how to make this work. So, they, they're gonna, they're gonna figure this out.
Thank you.
Did you roll.
**Jim Porell** 27:47 Alright, yeah, I guess…
**Greg Shriver** 27:48 Thanks, Central.
**Jim Porell** 27:49 Anybody else? Greg, you have anything else for Richard?
**Greg Shriver** 27:52 No, I don't have anything else. I was gonna bring up the Federated Semantic Convention's lifecycle, but it sounded like we already kind of talked about that, so… So, I mean, Rudig and I did have the opportunity to talk about that on the 22nd of April.
So, I would recommend that you… that you take a look at the… at the… the… the notes.
for that.
And we had some proposals, though, just make sure that everybody, you know, takes a look at it.
And, maybe even socialize that idea within your organization, you know, and maybe it's a non-event, you know. I, along with Rudiga, think that That us… federate… regardless of whether… I mean, I think federating the semantic conventions makes a lot of sense.
And I also think it makes sense for… Main phone.
And, as… Yeah, and I also… I think it will, allow us to be more quick.
And to also use… to be less of a bottleneck for the centralized semantic conventions. But of course, when we do that, it's gonna be… we still have the same issues, right? Where, like, CICS and Tomcat are, you know… we still have same issues to deal with. It's just, this is really kind of addressing some of the mechanics, I think.
**Jim Porell** 29:19 Yeah, and to be honest, though.
it's kind of contrary to what I just said, but… What you also said, in a way, was we can control our own destiny, but those guys are ahead of us anyways, so we can adopt theirs for our purpose, versus having them change theirs for our purpose.
**Greg Shriver** 29:44 Sure.
**Jim Porell** 29:45 No, that's…
**Greg Shriver** 29:46 I think.
**Jim Porell** 29:46 It's a similar approach.
**Greg Shriver** 29:48 Yeah, I think maybe the message that I would sort of propose is that federated… federating the semantic conventions doesn't mean that it's, you know, that it's the Wild West and we can do whatever we want. We still…
**Jim Porell** 30:03 Right.
**Greg Shriver** 30:04 It still needs to make sense from an OpenTelemetry perspective.
You know, so it's not gonna magically, you know, magically solve all of our issues with With coming up with a reasonable you know, mainframe spec for OpenTelemetry.
But I think it will make it a little bit easier You know, both on the Centralized Semantic Conventions Group and on us.
**Jim Porell** 30:30 Yeah, and I think what they were saying was they have no mainframe knowledge, so for them to approve our PRs, they're like, you know, I don't know.
**Greg Shriver** 30:43 Sure.
**Jim Porell** 30:43 And so, now we can approve our own PRs within our group, but we can't be stupid and… just do unique things. We should do it in light of what they're doing. So, like I said, kind of like, we're adopting theirs, but making our own decisions, versus trying to force our Things on top of them.
**Greg Shriver** 31:04 Sure.
Yeah.
**Jim Porell** 31:06 This is gone.
**Greg Shriver** 31:08 It is, yeah.
**Jim Porell** 31:09 Yeah, it's gone way too slow, so I think we all agree.
**Greg Shriver** 31:13 It is, and in fact, I think, you know, there are vendors that are that are just, you know, ourselves included, that are just not even paying attention to the semantic inventions. We're doing, you know, we're doing whatever… whatever the customers need, and that the back-end… observability back-end vendors are willing to… to… to accommodate and code to.
And that doesn't… I mean, that serves the customer, but it really doesn't… it really doesn't, move the ball forward from an open telemetry or a standards perspective, so… I guess all I would say is, you know, if you take a look at the, the OTEP, that proposes the Federated semantic conventions. There's a lot of decent stuff in there, and we should probably all just read that and sort of understand it as we go forward.
With… with the… our… working in our own repository.
**Jim Porell** 32:14 Okay.
Sounds like a plan.
**Greg Shriver** 32:20 But that's all I had.
**Jim Porell** 32:22 Alright.
I've got nothing else, so…
**Joris Yangsheng Xu** 32:31 Federating semantic convention does that mean that… you… Oh, could you explain, federating semantic conventions?
**Jim Porell** 32:46 Let me take a shot at it. What originally was happening, and this is what Anton was referring to, was they had a giant GitHub repository that talked about databases, talked about transaction processing, talked about hardware, talked about virtualization. And so.
Everybody had to know what everybody else was doing.
And it… it was too complicated. So what they want to do is still have an umbrella, but now think about it as subtrees, have… a tree, you know, on a particular topic, but the mainframe, in this case, the mainframe as an extension has some unique capabilities, and so what I was saying was, we could try and force ourselves into the database to make extensions for the mainframe, but the guys on the database team know nothing about mainframes, and so they felt very uncomfortable about adopting what we wanted to do.
So what they're saying was, let's create some subtrees to do more expeditious stuff, so we could have a mainframe, and then within it, a database transaction processing, stuff like that.
We can look at the broader community of the x86 Linux world and say, what do they say about transaction processing? Start that as a foundation, bring it over, and then add our extensions. And the subject matter experts around the mainframe are all on this call.
And we say, yeah, we agree. That works. So let's do it. Let's do that. And then we… and then we can get decisions done faster. We don't need their help. The problem is, they need our help.
but they're not helping themselves, so, they were just incapable. So it's… the tree, instead of having a single tree.
It's kind of a federation of multiple trees working together to create the standard. But we can independently do mainframe things, and then they can adopt them along the way. I hope that makes sense, yeah.
**Joris Yangsheng Xu** 34:54 Yeah, yeah, it does make sense. Thank you very much.
**Jim Porell** 34:57 Yep.
Greg, did I say that right? Did that work?
**Greg Shriver** 35:00 Yeah, no, I think, I think you nailed it. I also added a link in the chat It's also in the, in the meeting notes under April 22nd, but there's the, there's a link there that kind of explains, you know.
their proposed path going forward, and it's not just mainframe that's in this boat, it's other areas as well. But they're proposing sort of a, an enhancement proposal to break these GitHub repositories up, and then they also talk about some of the automation That they're looking to do to try and do things, or to try and, like, prevent namespace collisions, which is a risk once you break you know, break the GitHub repositories apart. So, I mean, I'd recommend just taking a look-see at that and, you know, giving it a quick read-through before, you know, before our next meeting, if you could.
That goes for everybody.
**Jim Porell** 36:02 That does present problems, though, because where we want to be consistent with them, like, a database is a database, if we now call it a ZOS database.
Right. Just so we get rid of namespace collisions, that one might be a problem. And… Who knows?
**Greg Shriver** 36:20 You're right, because underneath the ZOS namespace, you're gonna have things that are concepts that are, you know, are.
**Jim Porell** 36:26 So.
**Greg Shriver** 36:26 Kind of the same, or at least similar, across other pieces within within the semantic convention. So it, like, you know, like we discussed, it doesn't solve… it's not a magic bullet. It doesn't solve all the problems, but…
**Jim Porell** 36:44 Yeah, the thing I wanted to avoid was exactly that, that we have ZOS unique naming, because then we're just another asterisk, and we want to show that we're just a team player, and… You know, where we are different, let those possibilities happen, but if… If this is creating our own namespace that we have to… put ZOS in front of everything. That, to me, I want to barf.
Yeah, we'll have to figure that out. I think Antoine gets it, though, so let's… let's see what he has to say about that, so…
**Greg Shriver** 37:19 Agreed. Agreed.
**Jim Porell** 37:20 Okay.
**Greg Shriver** 37:23 Alright, I got nothing else.
**Jim Porell** 37:24 Yeah, me either.
**Greg Shriver** 37:28 Anybody else?
Tom? Victory?
**Jim Porell** 37:34 Right.
**Kai Kirsch** 37:37 Oh, I'm good. Thank you, Derek.
**Jim Porell** 37:39 Alright, talk to y'all next week, Ben.
**Greg Shriver** 37:41 Thanks, everybody.
**Joris Yangsheng Xu** 37:42 Alright. Bye-bye. Bye-bye.
**Jim Porell** 37:44 Right.
**Kai Kirsch** 37:44 Alright.
