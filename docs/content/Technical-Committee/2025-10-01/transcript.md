SIG: Technical Committee
Date: 2025-10-01
Duration: 34 minutes
============================================================

## Zoom Recording Transcript

**Tigran Najaryan** 01:58 Hey, guys. Hello, Josh. Welcome. Welcome back.
**Armin (Dynatrace)** 02:04 To see it again.
**jmacdonald** 02:05 I also didn't expect this meeting, so I'm gonna mute myself and eat breakfast.
**Tigran Najaryan** 02:10 Yeah, that's fine. You could have skipped, I guess. It was a very short notice.
And nowhere is everyone else, though.
**jmacdonald** 02:45 Well, I feel like Carlos and David are both online, because they both recently acknowledged this meeting invite.
**Tigran Najaryan** 02:53 Let's give them a couple minutes.
We need a bit of a quorum.
Live our work.
**Liudmila Molkova** 03:05 Oh, low.
Welcome back, Josh.
**Tigran Najaryan** 03:11 I didn't know.
**jmacdonald** 03:17 I wasn't expecting to be here at this 8 o'clock meeting, so I'm eating my breakfast right now.
**Liudmila Molkova** 04:06 Hey! Welcome, David!
**David Ashpole (dashpole)** 04:12 Oh, hey, thank you.
**Tigran Najaryan** 04:14 Hi, David.
Welcome.
Congrats.
**David Ashpole (dashpole)** 04:18 Thank you, yeah.
I'm excited.
**Tigran Najaryan** 04:24 So we are, as well.
Okay, I don't know if anyone else is joining. Carlos is here as well. Hey, Carlos.
In the inbox. We have something in the inbox, actually.
**Liudmila Molkova** 04:51 Yep.
**Tigran Najaryan** 04:52 Hasn't happened for a while.
**David Ashpole (dashpole)** 04:54 Twin.
**Tigran Najaryan** 04:54 to 79.
Although, whose week is this? Who's.
**Armin (Dynatrace)** 05:08 I will take care of writing down the notes.
**Tigran Najaryan** 05:13 Thanks, Annie.
I can't remember where we are with SQL Commander. Does anybody know where we stand with that?
**Liudmila Molkova** 05:27 Yeah, so there were some, recent news, So, after Google donated SQL Commenter.
It didn't evolve much in open telemetry, but there were developments that were continued in the Google version of it.
So, I think we've… archive the repo in OpenTelemetry.
But… the… we had also discussions about SQL statement… SQL context propagation in semantic conventions.
And the… the problem with SQL Commenter.
that… it ruins performance, right? So if you have prepared statements or anything, if you… you cannot update the SQL statement.
And there are database caches that rely on it, so it's actually suboptimal to use it for context propagation. It's okay to use it for something static.
Like, operation name or, service name.
For, context propagation, there… there are… like, ideally, it would be part of SQL.
itself.
But in reality, it's not, and every database has… not every, but many of them have their own custom ways to propagate additional information.
So what we do in semantic conventions is that when people are trying to contribute context propagation, we ask them to find these things and use them. So we have something for Oracle, for Microsoft SQL Server, and I think there is some way in Postgres Which is not related to SQL commenting, but it's database-specific.
Thing.
**Tigran Najaryan** 07:24 This custom ways, you mean they are part of the network protocol, essentially, for the particular database?
**Liudmila Molkova** 07:29 Yes.
**Tigran Najaryan** 07:32 Okay.
**Liudmila Molkova** 07:33 Having said this, the context propagation, it's not… Straightforward on how to use the abstractions we have.
to add things.
Into this thing.
And there are some weird, suggestions on how to use SQL commenter for, let's say, service name.
So, it's… It's not the text map propagator, it's a string propagator.
And… it's tricky, and maybe there is some room to… have more propagators, not specific to SQL, but specific to the string nature of it.
**Tigran Najaryan** 08:29 Yup.
I'm just reading a comment that Mark wrote.
Just trying to understand what's the expectation here.
So, obviously, we don't control the network protocol that the databases use, right? They use each… they use different protocols. There's no universal protocol.
There's, we can offer semantic conventions.
to use with whatever is your wire protocol, if you have a concept of context on your wire protocol.
It probably makes sense to use the semantic conventions that OpenTelemetry publishes, so that you can propagate it farther But I don't know what else other than the semantic conventions can come from the OpenTelemetry side on this.
We're not going to be defining a new wire protocol for databases, that's not our job, obviously, right?
And they, they, most of those, at least the old school ones, they, they use completely custom stuff, proprietary, maybe some sort of TCP connection, but not HTTP or anything like that that has a built-in concept of headers, which we then use for the context propagation, right?
So, I don't know what is it that we could do on our end, other than doing the somatic communications.
**Liudmila Molkova** 10:24 I tend to agree with the statement, But I also heard thoughts that, okay.
It ruins performance, but it's updated, and some people want to enable SQL Commenter to get some insights, and vendors are actively building integrations with databases to actually make use of it.
**Tigran Najaryan** 10:46 So… You mean the commenter?
Yes, it is the, I guess, the universal, or the more universal approach, but It proved to be… I guess, unpopular in the community. We didn't get… there's a reason, right? We… we just… we archived it.
So, what is it? Now we want to reopen it?
I, I don't know.
**Liudmila Molkova** 11:10 This issue… well, it's… it's pretty old, though.
Is asking for, the propagator, which is essentially as 3 years old propagator.
**Tigran Najaryan** 11:21 Right, it's years old, but there is, like, sort of multiple recent comments in the last few days.
So people are trying to reopen the discussion. What I'm saying is that there's two options here, right? One is… we reopened SQL Commenter, there's a renewed interest, there are new contributors that would like to work on it.
I'm not convinced that's the case, right, but we can look into that. The other is completely unrelated to SQL Commenter, and that is making it part of the… whatever is the wire protocol the particular database uses, which we won't go, it's not our business, we will not be defining what is the format for that wire protocol.
the best we can do here is offer semantic conventions, right? If you have a mechanism to record some sort of key-value pairs on your wire protocol, here's the values that we offer you to use, keys and values, right? And that's it.
That is the work that can happen in semantic conventions. I think that's… that's good to do that, and I think that's… perhaps the most that we can do here in this situation. And again, we can look into the SQL commenter, I think we will need to I will need to be convinced that it is the right thing to reopen that project at this stage, because it… It will… it was never… he never… amounted to anything in OpenTelemetry.
I don't know if there's any other opinions on this, but that's… that's the way I'm seeing.
**Carlos Alberto Cortez** 13:02 Yeah, I like that.
In a regional position.
**jmacdonald** 13:07 I don't have a… I agree with your position, Tigran.
Is there any engagement from database vendors beyond what I see in this issue thread that we know of?
I also wondered, David, as the only Googler in the room, if you have any thoughts on this, given how it came out of Google, I just wonder if you have any… any other stories.
**David Ashpole (dashpole)** 13:31 I… Now, Josh has most of the context on this particular one, but I know that there are teams that care about this.
but I guess not enough to… Try and make a successful open source project around it.
Yeah.
I don't have much more context, though.
**Tigran Najaryan** 13:51 Okay, in that case, I guess I suggest to do this. I will post in our private channel first what I said, because you're saying Josh may have additional context to give him a chance to maybe… Yeah. He has a different opinion.
If he hasn't, if he agrees with that, then we can comment on the issue and say this is what we're thinking from the TC side.
**David Ashpole (dashpole)** 14:13 Cool.
**Tigran Najaryan** 14:14 Okay.
Cool, I'll do that.
That's the only one, right? There is no… nothing else in the inbox.
**Liudmila Molkova** 14:24 Nope, nothing else.
**Tigran Najaryan** 14:25 Yep.
Okay.
And we don't have anything in the agenda.
Anything? Topics? Anything to talk about?
**David Ashpole (dashpole)** 14:41 Is, is there any, is there anything I should go read? Or, I know that there's, like, PC… There's stuff that comes along with being on the TC, right?
**Carlos Alberto Cortez** 14:56 Yeah, like, the union.
**David Ashpole (dashpole)** 14:58 onboarding… depths, or…
**Tigran Najaryan** 15:01 Is it just come to the meeting every week?
Come to the meeting, we'll take it from there. But there is, yeah, jokes aside, there is a rotation, to take care of the reported vulnerabilities and stuff like that.
**David Ashpole (dashpole)** 15:15 Yours will come, like, in a few weeks from now, so you don't have to worry about anything right now.
**Tigran Najaryan** 15:20 We'll add you to the rotation.
We need to add you to… I think we have a private, Zoom, we need to add you there as well when we need to discuss private.
**jmacdonald** 15:31 Carlos has, I believe, already done that.
**Tigran Najaryan** 15:34 Yeah, okay, cool, cool.
**jmacdonald** 15:35 I remember also, a rotation for taking notes and, posting them in the community meeting, although…
**Tigran Najaryan** 15:44 We're not doing the posting anymore, because this meeting is recorded now, so…
**jmacdonald** 15:49 Okay, great.
**Tigran Najaryan** 15:49 anything like that. But, yeah, there's essentially one rotation for all of whatever is the weekly responsibilities for the TC, but it doesn't amount to a lot of effort, really. It's a…
**Carlos Alberto Cortez** 16:05 One discussion that we need to have… well, not discussion, it's just assignment, that the DC members are assigned to try to help different ZIGs from, you know, like.
speaking with them, like, what's happening, to actually trying to help them, or even lead the project, you know? And actually, that's a good call, because, Jim McD, I was… the one in contact with your sampling SIG, so now you're back, so I can still help, but you can be there.
**jmacdonald** 16:32 Sure, yeah.
I can… I mean…
**Carlos Alberto Cortez** 16:34 It helps someone else sick instead, for example, yeah.
**jmacdonald** 16:36 Thank you. I would be glad to resume the formal responsibility for sampling's sake.
I'm gonna work on that blog post.
**Carlos Alberto Cortez** 16:45 And, David, I think… I don't know, like, maybe I'm wrong, but, I seem to remember that Josh mentioned that you are, to some level, involved with eBPF.
**David Ashpole (dashpole)** 16:56 Yes, the issue is that That SIG meeting conflicts with this meeting.
**Carlos Alberto Cortez** 17:02 Right, actually, yeah, we can talk offline about that. I was the one reviewing what they were doing for now, but I never wanted to contact them to change that, because I know I wouldn't be, like, the permanent contact.
So yeah, let's talk offline, but yeah, basically, if you're involved, you may have to ask them nicely to change that.
**David Ashpole (dashpole)** 17:25 I was involved with Bela, and then since it became the OpenTelemetry eBPF SIG, I haven't been able to attend. So I'm less involved now, but I would love to get involved again.
**Carlos Alberto Cortez** 17:37 Yeah, so what… for example, what Bogdan did for the fast seat is that he was trying to discuss with them a new, you know, time that would work for everybody, at least to some degree, at least bi-weekly, something like that, you know?
But yeah, basically, yeah, I can't give you details, because I was trying to check what's happening with the networking one and the BPF, you know, instrumentation ones.
**David Ashpole (dashpole)** 18:02 Is there a list of who's working with which SIG?
Somewhere? Yes.
Okay.
**Carlos Alberto Cortez** 18:09 Somewhere.
**jmacdonald** 18:11 I really think that's just…
**Tigran Najaryan** 18:13 I've got a spreadsheet with a list of sponsorships.
**David Ashpole (dashpole)** 18:16 Awesome.
**Armin (Dynatrace)** 18:17 I should be able to find it, I'll post it in the Slack channel.
**David Ashpole (dashpole)** 18:21 I think Tigrin just posted it.
**Tigran Najaryan** 18:22 It's in the Zoom chat, I have just posted the script.
**Armin (Dynatrace)** 18:25 Okay.
**Carlos Alberto Cortez** 18:26 Oh, man.
**Liudmila Molkova** 18:27 Apparently, it's not in our bookmarks, I'm going to edit there.
**Carlos Alberto Cortez** 18:33 Yeah, actually, it's not there. I wasn't checking for that there. It is not.
**Tigran Najaryan** 18:47 We also don't see in the bookmarks the private meetings notes document as well. We're missing that as well, I think.
**Armin (Dynatrace)** 18:55 Pinkerton should be in there.
**Carlos Alberto Cortez** 18:57 Yeah, it's there, I think. Both the Zoom, the private Zoom and the private notes.
items.
**Tigran Najaryan** 19:05 Yes, yes, you're right, I see it now. Okay.
**Carlos Alberto Cortez** 19:21 Yeah, so basically, Josh and David, we have some, every TC member should be trying to take an apparel, two, three different zigs to help them.
The ones in red, if I remember correctly, are things that we don't have people assigned to.
I think it's outdated, because, for example, the fast one, it should be bulked on.
**Tigran Najaryan** 19:47 Yeah, we may need to update it. This is maybe a… A month old, or two months old now.
**Carlos Alberto Cortez** 19:54 Yeah.
So, probably we don't have to do it right now, unless you want to, but… If we do it offline, Josh and David, probably you can take a look at the ones in red and see which ones you would be interested in helping.
But probably for UWB, it would be the EPPF instrumentation and networking one. The network is, you know, related.
**David Ashpole (dashpole)** 20:16 What's the estimated column for? Sorry.
There's current TC sponsor and estimated TC sponsor?
**Liudmila Molkova** 20:24 So, the estimated is what we think this group needs to succeed, the maximum level.
the minimum level it needs to succeed. And Current is how much we are actually helping it.
**David Ashpole (dashpole)** 20:40 Okay.
**jmacdonald** 20:43 I'm looking at the same sheet. I… so I could take on the sampling back from Carlos, I could take on Arrow back from Riley, and I… I've been pretty heavily involved in the collector lately, and I don't want to lose that… that responsibility, so, that would be the three I would choose for myself, although that doesn't help fill the red spots really well.
**David Ashpole (dashpole)** 21:05 I'll obviously fill the Prometheus interoperability.
And I will… Is there a difference between eBPF OpenTelemetry Network and eBPF Instrumentation? The OpenTelemetry Network was that ancient one, right?
That.
**Carlos Alberto Cortez** 21:22 Cheer.
**David Ashpole (dashpole)** 21:23 Yeah, yeah, okay. Yeah, I can… be involved in both of those, that's fine.
**Carlos Alberto Cortez** 21:28 Yeah, there are different groups and different repos as well.
Yeah, there's… there's one person, if I remember correctly, that is involved in both of them, but otherwise, it's… they are different.
**David Ashpole (dashpole)** 21:42 Yep.
And would you like me to remove you, Carlos?
from both of.
**Carlos Alberto Cortez** 21:49 Yeah.
**David Ashpole (dashpole)** 21:50 Okay.
**Carlos Alberto Cortez** 21:51 Yeah, please. You can just provide you the quick notes I managed to take over the last weeks on that one. Yeah. Otherwise, yeah, you're the expert there.
**Tigran Najaryan** 22:01 I don't know.
**Carlos Alberto Cortez** 22:01 Does anybody remember? Okay, go ahead, sorry.
**Tigran Najaryan** 22:04 I don't know if we still need the current and estimated as separate columns anymore. We did this exercise back then, but we should probably, from now on, track the current, right?
**Liudmila Molkova** 22:17 I think the security is red, for example, because Josh is escalating sponsor, but we decided that we need a guiding one.
**Tigran Najaryan** 22:27 I see. Okay.
**David Ashpole (dashpole)** 22:30 Let's see, otherwise… I'm happy to be involved in any of the Go SDK-related ones. I see… I see they're empty, and Tigran is listed as.
**Tigran Najaryan** 22:43 Yeah, I'm listed as the sponsor for most of the Go-related stuff there, but if you want to take any of those, I'm happy.
Up to you.
**David Ashpole (dashpole)** 22:53 I'll take that.
**jmacdonald** 22:54 Thank you.
**David Ashpole (dashpole)** 22:57 Of course.
Let's go.
**Carlos Alberto Cortez** 23:13 By the way, just to confirm, I don't know what… there's a document explaining what's the differences between escalating, guiding.
What was the other one?
Leading, correct.
So, just for you to manage, in case you feel tempted to take too many of them, you need to check what's there.
You know, expected involvement.
**David Ashpole (dashpole)** 23:35 Yeah, I'm just listing basically what I'm already doing, for most.
**Carlos Alberto Cortez** 23:39 Okay, nice.
Sweet.
**David Ashpole (dashpole)** 23:46 Tigran, do you want me to take the Kubernetes operator?
**Tigran Najaryan** 23:50 If you want to, sure.
Yeah, I'm happy.
**David Ashpole (dashpole)** 23:55 Take that as well. Okay.
**Tigran Najaryan** 24:06 And by the way, I added you to the GitHub technical committee group. You should be the members of it, they should have the permissions.
**David Ashpole (dashpole)** 24:21 I'm gonna steal Kubernetes Savannah conventions from Josh.
**Carlos Alberto Cortez** 24:28 By the way, the columns are kind of the other way around, because current TC Sponsor was what we had when we started this document, and estimated TC Sponsor is the one, the final one, the one we should be having from now on.
**Tigran Najaryan** 24:42 So, I guess that's what I was saying, maybe keep one of those.
keep the estimated for the changing level, but we don't need two columns for the names anymore, I think, right? Let's just track whatever is the current Sponsor, the name will be one column, and the sponsorship level, if it needs a change, we can set it, whatever, it's estimated, we can call it target, or something like that.
**Carlos Alberto Cortez** 25:08 Yep.
**Tigran Najaryan** 25:08 The structure of the document is a bit outdated now, because it was the right one for the exercise we did back then, but now it doesn't make sense a lot of sense anymore.
**Carlos Alberto Cortez** 25:19 Yep.
**Tigran Najaryan** 25:26 So, I guess what I'm saying is, let's delete the current TC sponsor column, column C, If we estimate it, and rename that to the, essentially, just the sponsor name, and something like that.
**Carlos Alberto Cortez** 25:40 Wait, I would say C and D.
I guess.
**Tigran Najaryan** 25:43 Say again?
**Carlos Alberto Cortez** 25:45 And column D as well.
**Tigran Najaryan** 25:49 Colin, you want to delete that as well?
I mean, what we have now and what we aim for may be different. That's why we want to have to do.
**Carlos Alberto Cortez** 26:00 Okay.
Okay, yeah.
Okay, what not?
**David Ashpole (dashpole)** 26:14 Awesome, thank you.
**Carlos Alberto Cortez** 26:34 By the way, does anybody remember what's up with the end user seat? It's in red, and Jack is helping us. I don't remember what was the deal there. That's a seed that I wanted to probably help, instead of the sampling seat, but I don't know what's established.
Anybody remember?
**jmacdonald** 27:00 You said end user SIG.
**Carlos Alberto Cortez** 27:02 That one, yeah.
**jmacdonald** 27:06 It's still active, I take it.
**Carlos Alberto Cortez** 27:10 Yeah, but I don't remember why it's red.
**Liudmila Molkova** 27:14 It didn't have a sponsor. Nobody…
**David Ashpole (dashpole)** 27:16 Cared much about it.
The current sponsor was listed as no one. Some of them had an estimated sponsor, like, we want this person to be involved or something, but…
**Tigran Najaryan** 27:29 Yeah, so Jack is listed as the…
**Carlos Alberto Cortez** 27:31 Right.
**Tigran Najaryan** 27:32 Possible sponsor?
Check with him, I guess.
**Carlos Alberto Cortez** 27:38 Yeah…
**David Ashpole (dashpole)** 27:40 Okay, since Jackie's not here, I am a little bit curious about that one. I will probably attend, see what's happening there.
**Carlos Alberto Cortez** 27:46 And I will do that before I assign myself there. Because, since I will not be the sampling one, I can help with something else.
**Liudmila Molkova** 28:07 Should we update the name? So, since we are removing TC Core and TC Sponsor, some of them are… different. No, we should probably fix it.
So, for example, for sampling, we striked through Josh McDey and… Carlos, you are the TC sponsor.
Yeah.
**Carlos Alberto Cortez** 28:26 Yep.
**jmacdonald** 28:30 And I had just been editing this document, the other column, the one that we've now struck out today, so I can go write my name in in the new column as well.
**Tigran Najaryan** 29:59 Okay.
Think we're good with this?
Any other things to discuss?
All right.
Go…
**Liudmila Molkova** 30:24 Thank you all.
**Armin (Dynatrace)** 30:26 Oh, sorry.
**David Ashpole (dashpole)** 30:27 Thanks, bye.
