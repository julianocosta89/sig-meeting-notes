SIG: End-User SIG: OTel Blueprints
Date: 2026-09-28
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Lukasz Ciukaj (Splunk Inc.)** 02:26 Hello, Tiffany.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 02:31 Hey, Lukasz, how are you?
**Lukasz Ciukaj (Splunk Inc.)** 02:33 I'm doing good. Hello. Welcome back. Hope you're well.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 02:36 Thank you.
Thank you. Yeah.
Getting back into it.
**Lukasz Ciukaj (Splunk Inc.)** 02:42 So you were, like, totally off from OpenTelemetry for a couple of months, or you were still doing something, but let's say, off from this project or this initiative?
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 02:52 Pretty much all of OpenTelemetry. I did not have… time to do my Grafana work and.
**Lukasz Ciukaj (Splunk Inc.)** 03:03 care.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 03:04 for my dad and.
**Lukasz Ciukaj (Splunk Inc.)** 03:05 Yeah.
And open telemetry.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 03:07 Okay, so… So yeah, I was on hiatus from pretty much all of OTEL, so…
**Lukasz Ciukaj (Splunk Inc.)** 03:15 Gotcha. Hope everything is is okay from let's say this family matters for you.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 03:21 Yeah, yeah, yeah. Thank you.
**Lukasz Ciukaj (Splunk Inc.)** 03:26 Okay, do you know if Dan is gonna join us today?
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 03:30 I do not know. I was about to post in the channel to see.
It's good.
**Lukasz Ciukaj (Splunk Inc.)** 03:36 So last call, it was just me and Dan. I was like joining from my mobile.
For a few minutes, because I couldn't join, so… I don't know if someone else gonna join.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 03:50 Okay, I'm… I'm gonna…
**Lukasz Ciukaj (Splunk Inc.)** 03:52 Dropping the message to the channel. Okay, I see you.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 03:55 Yeah, yeah, I'm gonna just grab the link so that everyone… Copy link.
Okay.
There we go.
**Lukasz Ciukaj (Splunk Inc.)** 04:16 Let me open our project board.
Gotti.
And so when you, when you are off.
We made the decision with Dan to… let me maybe quickly share my screen.
And okay, it's a well-known problem.
In order to share, I need to drop and rejoin. Or maybe I can try, let's… let me try.
Can you see my screen?
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 04:43 I can, yeah.
**Lukasz Ciukaj (Splunk Inc.)** 04:44 Okay, so it's working without rejoining. So we decided to make a breakdown of, let's say, two separate projects. One is for Bootstrap.
And one is for ongoing.
Okay. So, yeah, so for the bootstrap, it's everything that is… is it bootstrap? Yeah, it is bootstrap, so everything that we were discussing.
Before, we still have a couple of to-do and in progress, but we still have some stuff that was done. This is everything that we need to call the project as closed.
And then we have the backlog of this proposal that we have. This is nicely aligned to the statuses that we developed in the meantime, so… I believe it's still not finalized, this project board. It requires some discussion here, if that is what we want to see, and if that is what we want to track. But so far, so good. I think this view is really nice for maintainers to see.
What proposals do we have? Which of them are approved? Which of them needs review? Which of them are in review? Etc.
So that's…
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 05:50 Okay.
**Lukasz Ciukaj (Splunk Inc.)** 05:50 That's the way, and what we have here is.
We have one Blueprint that is still in progress, which I believe you did some review from, let's say, the text and docs perspective, right? The one for…
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 06:06 Yeah, yeah, there were several CI issues that needed to be fixed, and then I just did a quick copy edit of it.
**Lukasz Ciukaj (Splunk Inc.)** 06:13 Yeah. So okay. But this this okay. This is the issue. Right?
So we need to go out.
Where is the PR here?
Is it the one? Yeah, that's the one.
That was a long, long discussion, but finally, we are almost there. Okay, so you suggested something, but it was not yet… Implemented the changes that you suggested, right?
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 06:52 Yeah, and, you know, if, If Alex is fine with it, and I can check with him, I can just commit all of those changes. They're not…
**Lukasz Ciukaj (Splunk Inc.)** 06:59 you.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 07:00 They're not really substantive. It's more just shortening sentences and removing Latin phrasing like via.
In favor of something else, so…
**Lukasz Ciukaj (Splunk Inc.)** 07:12 Gotcha, I see it.
So like minor cosmetic, let's say, changes here.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 07:19 Yeah, just for clarity's sake, we try to avoid words like via
**Lukasz Ciukaj (Splunk Inc.)** 07:24 For…
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 07:24 localization purposes, it's better to use a more specific and English word so that it can be translated easier.
Yeah.
But.
I mean, I'm fine waiting. I can ping Alex. He's actually at Grafana, so I can ping him and just see if he wants me to just commit the change.
**Lukasz Ciukaj (Splunk Inc.)** 07:46 He was a bit busy as well last week, so we were wondering with Dan if he will be able to work on this PR, or someone should take over, but then… He started working on that again, which is great, so he could be the… you know, recognized as the main author of this blueprint, so I think that makes sense. So, yeah, I think that we are almost there, so once this is… Again, either he can implement that, or you can just commit that changes so we could… we could then proceed with publishing, and we would be good with… With, let's say, the… the Blueprints that were part of Bootstrap, yeah, because that's what Dan wanted to have, and we wanted to have a couple of Blueprints published, and also reference implementations. For the reference implementations, I believe there was something… with DevEx team that they were working on, if I remember, were 2 or 3 more reference implementations.
Or customer case studies that we wanted to… Use as a, as a reference implementations, but I don't see issue for that. I think that was mainly something that Dan knew based on the.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 09:00 Okay.
**Lukasz Ciukaj (Splunk Inc.)** 09:00 on the interactions with DevEx team, but I don't know what's the status of that, so it's hard for me to come… oh.
Bingo.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 09:08 Yeah, the last I heard, there was one more that they had completed, but then the… Either the person they interviewed left the company, or the company changed their mind about being featured, so…
**Lukasz Ciukaj (Splunk Inc.)** 09:21 They didn't have.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 09:21 have permission to publish it. But that was that was a while ago. Hey Dan.
**Lukasz Ciukaj (Splunk Inc.)** 09:26 Yeah.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 09:26 while ago.
**Lukasz Ciukaj (Splunk Inc.)** 09:27 Yeah, yep.
**Dan Gomez Blanco** 09:28 Yeah, sorry I'm… sorry I'm late. Meeting overrun.
**Lukasz Ciukaj (Splunk Inc.)** 09:31 It's fun, because we were discussing, I mean, this reference implementations from DevEx team, and I mentioned that I don't see issue for that, and it's something what Dan had in his mind, but then you joined, so maybe you've heard that, or… Yeah, so do you have any feedback from that DevEx team about that reference implementations?
**Dan Gomez Blanco** 09:50 Not yet, no. I need to… yeah, I've got it in my to-do list to ask.
**Lukasz Ciukaj (Splunk Inc.)** 09:57 Zoom.
**Dan Gomez Blanco** 09:58 Should we, like…
**Lukasz Ciukaj (Splunk Inc.)** 10:00 Should we have it as a separate, issue here, or… or in order.
**Dan Gomez Blanco** 10:05 No, I think it's… Is that not in the agree on missing reference architectures to complement Blueprints? I think it should be.
**Lukasz Ciukaj (Splunk Inc.)** 10:12 This one, right?
**Dan Gomez Blanco** 10:13 Yeah, I think.
She should be there, I think.
No, okay, I think,
**Lukasz Ciukaj (Splunk Inc.)** 10:22 But the DevExC have collected a few interviews with end-users.
Yeah, but since then…
**Dan Gomez Blanco** 10:27 I think, you know, we do have two more, I think, or they are working on two, so that, you know, there are three published, right? And then we've got working on two more.
One thing that I was thinking now, today, about asking them is if we want to move… The… the other… the one that's under that one, 399, review published reference implementations.
**Lukasz Ciukaj (Splunk Inc.)** 10:50 we.
**Dan Gomez Blanco** 10:50 We want to move that to the DevEx.
repo. The reason for it is that I would like them to review it, because they've been… You know, doing all these write-ups, so if there is anything that doesn't really match in how they think about You know, Anything that would have been useful to cover, and that we have not been, you know, that we have not covered in that template.
But at least, you know, they can mark it as done from their site. I think from our site, we've reviewed the… the template.
We're happy with it, but we haven't used it yet. And I don't think that we need to use it to call the OTEL Blueprints project complete. If we have 5 reference implementations published as blog posts and moved over to the other section, I think I would rather Call it complete.
And then move on to the next phase, right? To just go on… B A U.
And so on. So I guess… Yeah, so what we're missing from the DevEx SAIC at this time will be a review.
of that template.
And for those two other… And.
reference implementations to be published. I don't know if we've got a… an issue for them, though.
Don't know if anybody knows, but I… we can ask that.
**Lukasz Ciukaj (Splunk Inc.)** 12:14 No.
if you're tracking.
**Dan Gomez Blanco** 12:16 They're tracking those in some way, right? Because then we can just add them to this board.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 12:24 I… I haven't heard anything either. Just so I'm clear in my head, are… if we transfer issues, or if we ask them to open issues, are we expecting them to do… to write the blog post and then also put up the PR for the reference implementation version of that document, or… Is that something you want?
**Dan Gomez Blanco** 12:43 I was thinking we could take the opening the PR too.
To move it, but then for them just to review the template.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 12:50 Got it. Okay.
Sounds good to me.
**Lukasz Ciukaj (Splunk Inc.)** 12:55 Do you have any good contacts there? Who is the main, let's say, point of contact for you in the next team?
**Dan Gomez Blanco** 13:01 And.
But that would be, and.
That would be Juliano, or sorry, Juliano.
Oh, Johanna.
I think they're the one that you know the 2 of them have been.
I am the most active there, and they've replied to…
**Lukasz Ciukaj (Splunk Inc.)** 13:25 Are they part of our Hotel Blueprints?
**Dan Gomez Blanco** 13:31 No, that was…
**Lukasz Ciukaj (Splunk Inc.)** 13:32 channel.
**Dan Gomez Blanco** 13:33 That was, well, Juliano might be, I'm not sure about.
**Lukasz Ciukaj (Splunk Inc.)** 13:37 We could tag them maybe in our channel and ask them for. Yeah.
**Dan Gomez Blanco** 13:43 Yeah, I can do that.
**Lukasz Ciukaj (Splunk Inc.)** 13:44 Joanna is there, and Juliano is there as well, so… so we can… Tag them and ask for help.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 13:54 Yeah, I'm not sure how much Yohama is doing, these days, but yeah.
She… she switched companies, and I'm not sure how much,
**Dan Gomez Blanco** 14:04 Right, okay.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 14:04 involvement she has in OpenTelemetry, but… Yeah.
Definitely reach out to them.
**Lukasz Ciukaj (Splunk Inc.)** 14:13 So, Dan, correct me if I'm wrong, so now for us to call this bootstrap project complete, we need to have the Blueprint by Alex published, and Tiffany did a review as well. We just discussed before you joined that there are some minor cosmetic, let's say.
things to be changed, and Tiffany is happy to commit them.
But obviously, we would love Alex to implement it by his own, if he's the main author. So we are nearly there, so this is almost completed. And then we need to have… what is missing then? Like, reviewing this.
Template by DevEx team.
**Dan Gomez Blanco** 14:57 Yeah, so we called for, like, you know, 5 in the deliverables, right? We said 5 reference implementations and 3 blueprints.
And as I understood, we've got, there was Atlassian and Keycloak.
That were…
**Lukasz Ciukaj (Splunk Inc.)** 15:16 We've got two, we'll have three. For reference implementations, we have three.
**Dan Gomez Blanco** 15:20 3, and we set 5.
**Lukasz Ciukaj (Splunk Inc.)** 15:22 Yeah.
**Dan Gomez Blanco** 15:23 So, And there are two in progress, according to… My last message, which I sent on August 3rd.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 15:36 Oh, okay, good.
**Dan Gomez Blanco** 15:37 So I did send a message. I sometimes forget. I did send a message at some point. Yeah, so both of the, apparently both of the blog posts are written.
But they're waiting on review from… On the Atlassian side, we're waiting on review from Atlassian folks.
And feedback, and for the key cloak size.
It should be good to go, but the person that was driving that was in PTO.
**Lukasz Ciukaj (Splunk Inc.)** 16:04 Mmm.
**Dan Gomez Blanco** 16:05 So,
**Lukasz Ciukaj (Splunk Inc.)** 16:07 Yeah, so we need to definitely check with them.
What's the status?
**Dan Gomez Blanco** 16:11 Yeah, let me just follow up on that thread and ask.
**Lukasz Ciukaj (Splunk Inc.)** 16:14 If they need any help with that, maybe some review, or…
**Dan Gomez Blanco** 16:18 Yeah, I mean, maybe that's a good point. We could just offer, like, you know, to… if people are maxed out, we could…
**Lukasz Ciukaj (Splunk Inc.)** 16:24 Yeah, because this is kind of the blocker for us, right? So we need… if we want this project to be… or bootstrap to be… to be called as completed, then we need… we need to do some, maybe, extra work, so let me know, or let us know when you hear something from the VEX team, and then we can continue that.
**Dan Gomez Blanco** 16:44 Sounds good. And then I wrapped up… and then there is another issue there, which is wrapping up the project, right? Yep.
And I think, in that one.
No description provided, but I will add it. I think the, the… The idea here is that, well, there is some admin that needs to be done to call the project complete, which is Moving one file, you know, just moving one file from a directory to another in the community repo and canceling certain things.
And.
That doesn't mean that, basically, that… this meeting disappears, right? I think we'll keep it.
We don't need another project because we're moving towards like a more BAU, you know, we don't need our projects in the projects, in the community projects, right? But I think one thing that I would like to do is… And it works… this is… doesn't have to be me, right? But we, as a group.
Write a blog post, or maybe say, if someone wants to, to, you know, to take on that.
And.
Just to summarize what we've done.
and then call for contributions, right? I think we can… we can say we're ready for scale, right? I think we… that would be the… and then maybe the next steps, maybe that's something that we can say, you know, we have a bunch of Blueprints in the pipeline, we should probably think about prioritizing those, and I think that's something that we talked about in the past, that we… We have a bandwidth for reviewers, and there will be a… I guess a priority of… Of reviewing things, and we don't want to push too much work onto… And.
The comms team to do copy edits, or… Or the.
or the maintainers of different SEGs to, you know, review and provide feedback.
So yeah, I think we need to manage.
The, the number of Blueprints that are in progress at any point in time, right?
Operate in a camera style, pretty much. Yes.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 18:53 Yeah.
Hey, Alex and Winnie, welcome to the meeting.
**Dan Gomez Blanco** 18:59 Hi there.
**Winnie** 19:01 Hello. Hi, Tash.
**Alexandre Ferreira** 19:04 Joined a bit late, but here I am.
**Dan Gomez Blanco** 19:07 Very good.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 19:08 Yeah, no, we're happy to have you.
**Alexandre Ferreira** 19:10 Can you hear me okay? I'm talking, what a nice…
**Dan Gomez Blanco** 19:15 Yeah, yeah, we can hear you fine.
**Alexandre Ferreira** 19:15 Low volume. My daughter's sleeping, so, like, don't mess with the background.
**Dan Gomez Blanco** 19:22 Nice.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 19:22 No problem.
Alex, we were talking about your PR at the… at the start of the meeting.
It's… it's really close. I made a few, like, clarity changes just to tighten up the language a little bit, and then there were, several, like, formatting things just to get the CI passing, but if.
If you want to go in there and commit the changes, that's… that's, probably the next step, but it's, it's… the ball's in your court, basically.
**Alexandre Ferreira** 19:56 Yeah, sure thing. I saw your comments, and I just applied them. I just, like, put them in a batch review.
I just need to update one line that I couldn't update from here.
Which was like the node locally thing. It's like.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 20:16 Yeah, I didn't…
**Alexandre Ferreira** 20:16 Okay, yeah, that's it.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 20:21 And that might be totally fine. It just sounds weird to me. I don't know.
**Alexandre Ferreira** 20:26 No, yeah, this, this helped me as well, so, like.
most of this was like me and my friend Claude, right? So so like sometimes wording on Llms.
I'm not quite there, right? So… I reviewed everything but a few things, escape my gaze. But I just committed all of them. I'm just making one last commit.
And I saw your comment on the slack thread regarding the the mermaid diagram?
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 20:57 Oh, yeah, yeah.
**Alexandre Ferreira** 20:58 You get… From what I understood, you cannot… increase the diagram and the OTEL docs, so we would like to put an… we would need to put an image, perhaps. I don't have a hard preference, just let me know what's better, and then I'll just change here.
Besides that, I think we should be this close to synergy.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 21:25 Okay, great. Yeah, I forgot about that comment about Mermaid. Thank you for reminding me.
So, just for everyone's edification, we have a deploy preview of the… of Alex's PR now, and when I took a look at it, the Mermaid diagram looks great, but it's really hard to read, and you can't, like, open it in a new tab, because it's not an image. You could, like.
plus plus plus your browser until it gets really big. But I'm not sure that's great UX, so I'm not sure if.
If anyone here has thoughts, concerns, or ideas about how to address that.
Oh, Dan, you're muted.
**Dan Gomez Blanco** 22:20 I guess, yeah, I'm just trying to think of that diagram. I think my answer to a lot of things in Mermaid is change the orientation and go vertical.
That sometimes helps.
Don't know if you've tried that, Alex, but…
**Alexandre Ferreira** 22:35 You know what happened? I actually didn't knew you could change the orientation of the diagram itself. I can have a go at it.
**Dan Gomez Blanco** 22:44 Cool.
I mean, that may make it really bad, as in, like.
Fairly big to… to go down through the… through the list, but I may… it might actually read better, as in… Yeah.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 23:02 I just added the preview link to the chat for anyone who wanted to take a look.
**Dan Gomez Blanco** 23:07 I was looking for that.
**Alexandre Ferreira** 23:08 Nice.
going Let me see it. I I haven't used the preview link.
**Dan Gomez Blanco** 23:14 Oh yeah, I can see what you mean. Yes, quite a small print.
Yeah, I think if you were to… At the top of it, I think it is, like, orientation left… L R.
or orientation TD, I think it's just changing that.
**Alexandre Ferreira** 23:33 I see. So, quick question.
**Dan Gomez Blanco** 23:38 Yeah, see when you've got…
**Alexandre Ferreira** 23:39 top.
**Dan Gomez Blanco** 23:39 Well, actually, you've got floor… You've got… I think it's the opposite, is Flowchart TD at the moment.
And I think you may want to make a flow chart.
LR, so it goes from left to right.
Which, in this case, will make it more vertical.
I can… I can comment that in the… in here.
**Alexandre Ferreira** 24:01 Shut up.
Imagine that You're someone trying to implement this?
and you don't know nothing about observing communities.
And you come across this.
I was rereading this, Doesn't it, like, kind of… Like, it's implicit that you should choose a path out of this, when in reality, you need to implement all of this at once.
So, meaning that here, we have this, This table right here, which tells, like, which, OTel component and a Hamtrot preset you should use.
**Dan Gomez Blanco** 24:50 Yep.
**Alexandre Ferreira** 24:52 Does this mean that we just… we could remove this?
to… Avoid people getting confused.
**Dan Gomez Blanco** 25:00 I was thinking that maybe, yeah, so I was thinking that, well, I was doing the review.
That you could either put this in the guidelines, and it would be… You know, it's a bit more like… See here where you've got this table.
And.
Almost like having the chart.
With the table?
**Alexandre Ferreira** 25:28 Yeah.
**Dan Gomez Blanco** 25:29 Because then.
**Alexandre Ferreira** 25:29 the.
**Dan Gomez Blanco** 25:30 When you go to the implementation, then you can just go straight into, okay, so that's… that's what we're going to be implementing, right?
**Alexandre Ferreira** 25:37 Okay.
Yeah.
**Dan Gomez Blanco** 25:43 I don't know what others think, but it might.
Might be more of the… I tend to… I guess this is more of an experience on the… How I tend to write.
Blueprints or.
or reference architectures is that the the diagram sits at the guideline at the general guidelines level, or at the, you know, more Wide thinking, and then the implementation tends to be a list of steps, right?
**Alexandre Ferreira** 26:13 Yeah, I agree.
My point being that, and certainly I'm biased for this towards this at this stage.
of… I'm thinking if the table is sufficient on itself in and of itself.
And we would remove the the chart. Sorry.
Just, like… Have this, and here on the outcomes, like.
one would hopefully understand that it's not that you should choose something here, but actually use every single line of this via the Helm chart, so…
**Dan Gomez Blanco** 26:58 Yeah, I mean, the only… I can see what you mean, it's like, fairly… I think both… I think people tend to be… some people are very visual, and they like… You know.
To have a diagram. Also, I was thinking that maybe this could be an improvement later, right? It doesn't need to be done.
To get this merged as a nitpick, but, like, having a diagram of how the… The different components in a cluster, as in, like.
People may want to know.
If the… And I don't know if that is in the… is it at the moment?
And.
At the moment, that diagram is based on what are you trying to observe, and then you've got multiple Receivers that you enable, and then the processor in the middle, right?
Some other folks may be more interested in knowing what… how does it integrate into a Kubernetes cluster?
As in, like, you know, you'll be deploying a daemon set, so you're thinking about a diagram with, like, I don't know, two nodes of a Kate's cluster, where you put… when you have, like, the daemon set pod.
In both of them.
And they're seeing that that demon set pod is collecting.
you know, metrics from the kubelet which runs on that node at the control plane level.
And then that one of the daemon sets is querying the Kubernetes Api.
for the cluster-wide level metrics, and all of them are doing file log receiver and Prometheus and… maybe that's something that could be useful for people. I guess I don't want you to be blocked now on this, but also, like, a thing that could potentially be quite useful to, to explain where the metrics are coming from, if you have time this week.
To,
**Alexandre Ferreira** 28:52 Yeah, so, I see what you're saying, so, like.
In other words, perhaps this table is… this chart is redundant with this information right here, but what's not… Visual, at this stage right now.
is the architecture of the collect. I mean, not target.
we could say architecture of the collector, so, like, to one example here, there, like you mentioned, there are some types of, telemetry that you cannot use a demo set for it, otherwise it will get duplicated. So, like, it might be interesting to me, like, refactor this to consider, like, which of those right here runs in the demon set, and which ones either run in a deployment or in a demon set using leader election.
**Dan Gomez Blanco** 29:43 Yeah, I guess, you know, we can go even, like, simpler than that, right? Because we're recommending the default… I mean, we're saying that you might want to deploy this in a deployment or whatever, but I think the cube… the… the… the cube stack.
Chart will deploy the demon set, right, only.
So so maybe we just want to like, do the the simplest architecture possible that will be delivered by the cube stack chart with the with all the options. Right?
I mean, with the default options.
**Alexandre Ferreira** 30:14 So… Noted, and… oops.
**Dan Gomez Blanco** 30:17 So I was thinking that maybe something like that, right? Two clusters, like, sorry, two nodes.
In a cluster.
and all the components, like a component architecture, right? You've got the… You've got a daemon set in a pot. Maybe you want to put like an application perhaps in there in that pod. Sorry, an application in that node, like a container application container, which.
pushes logs to… File, or to, you know, standard out, which will get pushed into a file.
And that basically… And.
And you might want to have a, collect her… You know, almost like in… I was gonna say… As a dotted line.
Like a collector gateway. A collector gateway that's not part of this blueprint.
But if you were to, you know, from the application container.
You would go straight to the gateway in the cluster.
For the… Demon set, you might go straight, you know, also through that gateway. I think we mentioned that. So, so I guess, yeah, something that tells you a little bit more about how the different components are.
Structure.
**Alexandre Ferreira** 31:31 Yep, yeah, I see what you mean. I like to do those.
I can work on this.
But,
**Dan Gomez Blanco** 31:44 How was your bandwidth this week, I guess?
**Alexandre Ferreira** 31:45 Okay.
**Dan Gomez Blanco** 31:46 If we wanted to get this, I know that we've, because we've gone, you know, quite far.
And also, like, we wanted to… that's why I was like, I don't think this is a blocker for us to merge it, if we'd rather do it… After, I'm also okay with that.
I don't think it's an app.
**Alexandre Ferreira** 32:02 Me too.
Yep, we can do that. So should I remove the the the the mermaid diagram?
In either case, we merge as it is, without the mermaid diagram, and then I'll do, like, a small PR afterwards, only with the… Oh, wow.
The… this new diagram.
It does.
**Dan Gomez Blanco** 32:29 What do others think? It will be a reference, it will be a blueprint without a diagram for now.
Which the others do have.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 32:43 I mean, I think that's fine. If it means that we're not putting undue pressure on Alex in his time, I think.
If.
the… if the table covers pretty much everything that's in the mermaid diagram right now, I think it's fine to remove it, because I honestly think most people will look at that and say, what am I supposed to… how am I supposed to read it? What am I supposed to do with it? Like, it's… done.
It's probably adding more confusion at this point.
**Dan Gomez Blanco** 33:12 Yeah. Can we, there's another option.
Is the draft.
Property and front matter applicable to any page, or is it only blogs?
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 33:25 Oh, it's any page. You can suppress any page.
**Dan Gomez Blanco** 33:28 Okay.
I guess that's another option that I wanted to put on the table, is that we merge it.
As a draft.
So it's not… so it's basically not visible.
But we merge it.
And then when we add the other stuff, later.
We We mark it as.
Visible.
What do we think?
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 33:57 Sounds good to me.
**Alexandre Ferreira** 33:58 I don't… yeah, me too. I don't have a hard preference, so…
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 34:03 I think there's a way, it's not draft, it's another… it's another parameter in the front matter, but I think there's a way to… set it up so that it doesn't show in the nav, but if you have the URL, you can access the page.
So, like, it would still be there if we needed to show it to someone?
But it wouldn't be easily findable.
**Dan Gomez Blanco** 34:27 Cool. I think that makes…
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 34:29 That appeals.
**Dan Gomez Blanco** 34:30 That makes sense, I think.
**Alexandre Ferreira** 34:34 Just to double check, I had this diagram, It's for completely different stuff. This is for like traces. You mean something kind of like this, but like with the dotted lines and like better formatting, right?
**Dan Gomez Blanco** 34:49 Yeah.
**Alexandre Ferreira** 34:50 Good.
**Dan Gomez Blanco** 34:51 Something like this, yeah.
**Alexandre Ferreira** 34:55 This is for Taylor Simple, which is… Very complex.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 35:01 Yeah.
**Dan Gomez Blanco** 35:04 Which is another… Another blueprint that we've got in the pipeline, I think, there's something about.
Sampling. Cool.
And.
But yeah, no pressure. I mean, Alex, if you're… This is why it might be a good… A good time to ask if you… if you'd rather, sort of, like, collaborate on this?
I feel like, you know… I mean, I think this week, for example, I've got Some bandwidth.
If you wanted to focus on the edits on the page.
We can work together, if you want, on the other stuff. I don't know, I just… Just want to put it out there.
**Alexandre Ferreira** 35:41 Yep. So, the edits on the page should be good now.
We can have a double check on this.
If you want to collaborate on this, I should have some time on Wednesday, and then we can do it live.
And tomorrow, I might have some time at the end of the day to draft something, and then perhaps to get together on, Wednesday 30, to, like, double-check everything, and then commit, and then deploy.
If you think that's okay.
**Dan Gomez Blanco** 36:18 or.
**Alexandre Ferreira** 36:18 We're happy to do async as well.
**Dan Gomez Blanco** 36:21 No, that sounds good. I mean, if you're like… this… can we aim to, like, I guess.
I guess that's another thing that I don't think is worth doing is basically putting it there as not visible, and then spending a lot of time with it not visible, right? So as long as we can say this week, for example, we can get it reviewed and merged, then… Yeah, then that should be… Be good to go.
**Alexandre Ferreira** 36:46 Yep. Okay.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 36:47 When you say reviewed and merged, you mean… The whole… the existing PR, or a follow-up PR?
**Dan Gomez Blanco** 36:54 Makes sense to none the follow up.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 36:57 Okay.
**Alexandre Ferreira** 37:00 So.
Here's what I propose. I've made some comments on the copy edits now.
Until tomorrow, we could try to merge it, if anything stands out.
I can, possibly change this, and then between tomorrow… tomorrow, I'll have a quick draft at the diagram. On Wednesday, I get together with Dan and, make a new PR, and then… From Wednesday until Friday, we aim to merge it, and then release the picture.
**Dan Gomez Blanco** 37:39 I mean, well, let me just… let's just rethink this, because I think, I… If we're all basically saying that we can do it in a week, or this week, maybe it doesn't make a lot of sense to split it into PRs.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 37:53 That's where I was going with my question.
**Dan Gomez Blanco** 37:57 Okay.
Cool.
**Alexandre Ferreira** 37:59 exist.
**Dan Gomez Blanco** 37:59 If you're if you're happy to put time on this, Alex, this week and to focus on it, I will be also.
Available for any reviews or anything like that, so we can…
**Alexandre Ferreira** 38:09 Okay.
**Dan Gomez Blanco** 38:10 Straight, you know, yeah, we can get it done.
**Alexandre Ferreira** 38:13 Okay. You mean, like, sync, synchronously on a meet, or, like…
**Dan Gomez Blanco** 38:18 Pay me is… yeah, or, like, what I'm.
**Alexandre Ferreira** 38:19 Okay, okay.
**Dan Gomez Blanco** 38:20 Ping me in the channel if you want a review. I think we're on this… I'm asking because I'm saying because we're on the same time zone, right? You're… You're in EMEA, or… well, similar, you're not in America, or…
**Alexandre Ferreira** 38:32 Yeah, I'm, South America, so, Jim T-Minus 3, it's, one.
**Dan Gomez Blanco** 38:39 Yeah, I don't know why I thought you were an EMEA. Okay, but still.
Is that the same? So, wait, am I the odd one here?
In terms of time zones.
**Alexandre Ferreira** 38:53 It's, like, almost 6 for you now, right?
**Dan Gomez Blanco** 38:55 Yeah.
**Alexandre Ferreira** 38:56 Okay.
**Dan Gomez Blanco** 38:57 Alright, okay, so then, whatever, just ping us in the channel, and we'll try to… to give that review, right? As soon as possible.
Cool. I guess that will make it easier from the perspective of copy edit as well, if we just keep everything… In there.
Cool, awesome.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 39:18 Yeah, and I'll double check CI. Alex said that he had already committed my previous copy edit, so I'll just make sure everything looks clean there. I'm sure we'll have some formatting to fix because.
The linters are very, very particular, so…
**Dan Gomez Blanco** 39:34 Sounds good.
By the way.
Another thing that I wanted to talk about, and because I joined late, I didn't have time to add anything to the to the meeting notes. Was something that I was discussing with Severin, although it's just that Well, there are two things. The first one… Was that, just to get more, like, visibility on this.
There is the… so, one thing that I spoke about was the fact that, I guess.
Blueprints are not… That is the Getting Started project, right? Like, the… on the comms SIG.
And then, yeah, so basically what Severin was saying, they're thinking about that getting started project to reignite it right? Because it was sort of like started, and then a little bit abandoned. And then he was saying that, does this be, you know, how does that align with blueprints?
I don't think it does, as in, like… it does in a way, but I don't think it's, like… a replacement for it. We're not in Blueprints. We're not really talking about a getting started guide and maybe more focusing on a particular component.
So.
Yeah, so if people want to answer, how do I get started with OTel, we should give them a fairly easy Way to do it. That's not, like… You know.
That's not putting them… And.
Off.
A top tin hotel.
And that should be really like step by step, run this command, do this, blah, blah, blah. And then you see some data out, right? That's great. I think Blueprints, this is what we talked about. And I think Blueprints are more of, if you want to solve this, you know, more advanced problem.
This are, you know, this is the guidelines of the, or these advanced problems. These are the guidelines and the implementation steps, right? So I think both.
Can… are completely isolated, in a way.
Some was like getting started, and then you might go into Blueprints if you want to adopt them, or.
organization-wide strategy.
So I guess we're all aligned on that, right?
**Alexandre Ferreira** 41:58 Yes.
**Dan Gomez Blanco** 42:00 Cool.
And then… Yeah, so Severin.
Was asking if the… So we've got two things, right? We've got reference implementations, and we've got the ecosystem and the ecosystem section of a website. We've got the list of adopters.
And.
And this is where they're kind of the same thing.
Or at least related.
Because they're also thinking what to do with the list, with the adopters page, long term.
And then one idea was basically getting rid of it and fall back to the… to the CNCF end-user case studies with, you know, that basically tag OpenTelemetry, or to… Do something like this, right?
So I'm.
My view on this is that there are a lot more adopters there than we have reference implementations.
Maybe in the future, that would be… a good idea. I don't know if right now, if we were to drop the adopters page, and we just point people to reference implementations, we've got 3 at the moment, right?
Maybe we need more.
But if we have more, then I don't see why not.
Now we can just drop the list of adopters.
I.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 43:27 Sorry, I didn't raise my hand, I just jumped in. But, My take on it is that the adopters page has little value except for the companies who are advertising that they've adopted OTEL And so, if we want to still offer them that kind of free advertising, we could… do it… But make a reference implementation part of the deal.
So… Get rid of that list that really doesn't have a lot of… core value to it, and say, if you'd still like to be highlighted as an adopter of OpenTelemetry, we would like to hear from you, and how you're using it, and… Basically, do that.
**Dan Gomez Blanco** 44:15 Yep.
Especially the ones that… because I think we, at some point, we dropped the requirement for them to To have, even a blog post, right?
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 44:25 Yeah, yep.
**Dan Gomez Blanco** 44:27 So I guess.
Yeah, it's little value to know that, I don't know, company X, yeah, uses… Ruby OTel.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 44:38 Yeah, it's, circumstances have changed, right? Like, when we first.
**Dan Gomez Blanco** 44:42 experience.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 44:42 that page, we were trying to establish the project as like a mainstream observability.
tool, for lack of a better word.
But now that, you know, OpenTelemetry is… Established. We've made it. We're here.
**Dan Gomez Blanco** 45:00 After graduation, yeah.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 45:02 Yeah, yeah, I think… I think it's okay to say, if you want to keep being listed on our website, tell us how you're using us. Like, don't just tell us that you are, tell us how.
**Dan Gomez Blanco** 45:13 Yeah, yeah, yeah, makes sense.
And.
Yep.
Okay.
So I guess after we close this project, then, and we say, okay, we've got a framework.
Yeah.
**Alexandre Ferreira** 45:36 Okay.
**Dan Gomez Blanco** 45:37 Maybe as a as a step forward before is like.
I don't know.
An extra column in there with a reference implementation, and what… which ones of these companies have a reference implementation, but… Maybe if, you know, as you say, Tiffany, maybe it's just better to, like, drop it, and then…
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 45:57 Well, at this point, we've frozen the ecosystem pages. We are not making any changes to those, at all. Like.
they are… they are essentially frozen, so I don't think anyone is going to be in favor of adding a column, that references implementations. My idea would be.
We have contact information in our metadata for pretty much all of these companies. When they create an entry, they have to include some contact information. My idea would be to do you know, an email to the ones who provided an email, or, you know, create a GitHub issue and tag anyone who provided a GitHub handle, and just say, we're retiring this page, we have this new section, which is going to be way more useful and, helpful to, you know.
End-users and adopters like yourself.
We'd like to feature you. How would you like to work with us and create a reference implementation?
**Dan Gomez Blanco** 46:58 Yeah, makes sense. I wanted to bring this up to the rest of the end-user SEG as well, because there's, You know, maybe this is something that… this is something that Severin mentioned as well. Maybe something that we… That the end-user SIG maintains, because sometimes, you know, like, I was thinking, like, what if the end-user Hasn't done a reference implementation, but they have done an OTelMe YouTube.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 47:26 Hmm.
**Dan Gomez Blanco** 47:27 session, right?
That's also pretty good. Can we ask them to do both? Yeah, great. I mean, it would be awesome if this is something that we talked about in the other meeting, is that for reference implementations, if people can do both.
I'm actually in talk… I'm talking to Adobe… Right now, to… for them to, like, do, Like an OTEL Me session, right?
So, I think we should always follow up with a session. That would be the idea, like, reference implementation.
And then there's a discussion about it in the channel.
I still think that having another page, I don't know, maybe this is, like.
Yeah, okay, maybe this is, like, the… It is redundant, in a way. So if we have the reference implementation, and then maybe later we want to link that to to a session, an OTelMe session or something like that, we can probably add it in the reference implementation itself.
And.
I don't think we'll get… Alright, okay, cool. So if we go for that solution, then… I guess we'll need to… this is, like… Future… future work that we can… that we can take on.
And then take on the, you know, email all the people that are there and tell them that if they want to.
Race or reference implementation, they can do it.
following the process.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 48:58 Yep, I will, I'll create an issue in the project board for the… the follow-on, not the bootstrap, the follow-on.
to, reach out, right? I don't think we want this as part of the bootstrap.
**Dan Gomez Blanco** 49:11 No, that would be… that would be later, yeah.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 49:13 Got it.
**Dan Gomez Blanco** 49:15 Cool, awesome.
Yeah, that was it.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 49:26 Winnie, I, I know that you have a proposal.
or a blueprint.
that you submitted several months ago. We do have a backlog.
And so I think.
maybe in the next meeting, we can take a look at those? I don't know.
**Winnie** 49:49 Okay, that's… that's fine. I do hope you can hear me clearly. My internet isn't so good.
But I should be working on it this week. I actually spoke to Dan about it, in the End-User Singh group channel.
And he gave some suggestions that I'm yet to implement. So I'm working on it this week. So I should have some something.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 50:14 Okay, great.
Great. I'm glad that you're moving forward, at least. Yeah.
I guess.
Is that it? Do we have anything else?
**Dan Gomez Blanco** 50:32 So I'm just trying to get to the… To the.
Meeting notes, I don't think we have anything else, but yeah, I think we're good.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 50:44 Yeah, we didn't even create a section for it.
**Dan Gomez Blanco** 50:46 I will, I will do it now. I'll at least put the, you know, I'll put some notes in there.
So I don't… Oh, you're on it.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 50:57 I'm not adding notes, I'm just doing the setup.
**Dan Gomez Blanco** 51:00 Cool.
What is NASA?
Is that North?
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 51:12 North America, South America.
**Dan Gomez Blanco** 51:14 That's confusing. I thought NASA was joining us.
**Alexandre Ferreira** 51:17 Thank you, guys.
**Dan Gomez Blanco** 51:22 I.
**Alexandre Ferreira** 51:22 I think Danasa does use Grafana though, if I'm not mistaken.
But yeah, it would be nice to imagine having NASA as a reference or technical.
**Dan Gomez Blanco** 51:33 That would be cool.
**Alexandre Ferreira** 51:34 now.
Munching on a bowl over here.
It's there for me, because it's important.
Also, wait, please send…
**Dan Gomez Blanco** 51:47 Cool, cool, cool, cool.
**Alexandre Ferreira** 51:48 is.
**Dan Gomez Blanco** 51:51 Right. What I will do is I'll put the agenda topics later in there. I'll just get them from the… from the transcript.
By the way, have people have you seen the new maybe I just bring that. This is nothing related to Blueprints, but I think it's cool. We've got some time.
If you go to app.lfx Let me share my screen.
So now, if you go to app.lfx.dev, you get your… and you're now seeing my dashboard.
But you can go to… OTEL And see the.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 52:38 Oh, wow.
**Dan Gomez Blanco** 52:40 stuff.
and then go directly to the recording, because it's now part of the LFX.
Zoom.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 52:47 Oh, that's nice.
**Dan Gomez Blanco** 52:49 So it should be, There we go.
This one here.
Yeah, so this should pop up in here after it's done, the recording.
M.
Should be available here.
There we go.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 53:08 What's the… what's the URL for that?
**Dan Gomez Blanco** 53:10 If you go to app.lfx.dev, It should bring you to your personal one.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 53:16 Yeah.
**Dan Gomez Blanco** 53:18 And then you can just find the project as well.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 53:23 Nice.
**Dan Gomez Blanco** 53:34 I lost the Zoom window.
Right.
Okay, so… I will put the notes in in there, or the agenda, at least the topics that we talked about.
And then, yeah, so… let's aim for… Finishing those things this week.
And maybe next week.
Or the week after, we can think about that, writing that blog post too.
To call the project on.
Hopefully. I think we're very close. And then we can move on to BAU.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 54:21 Sounds good.
**Dan Gomez Blanco** 54:22 Awesome. Alright, good seeing y'all.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 54:24 You too.
**Alexandre Ferreira** 54:25 See you. See ya. Bye.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 54:27 Okay.
**Lukasz Ciukaj (Splunk Inc.)** 54:27 Thank you all. Bye-bye.
