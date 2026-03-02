SIG: End-User SIG: OTel Blueprints
Date: 2026-01-22
Duration: 64 minutes
============================================================

## Zoom Recording Transcript

Alain Pham 00:02:16 Hi, good evening.
Dan Gomez Blanco 00:02:18 Hello, hello.
Yeah, let me see if,
If nobody is responsible for Hope's Notetaker, I will… Login.
with the… Host credentials, or claim host.
If I remember how to do that, and then do it myself.
These, I mean, these meetings are all being recorded.
And the transcript is being recorded as well, so if you go to the recordings, you'll be able to see it.
Dude.
Tiffany Hrabusa 00:03:20 Are we meant to be using,
the end user SIG notes, or the new note file that's been attached to this meeting?
Dan Gomez Blanco 00:03:30 Oh, so there's been a new… Alright, I think…
Tiffany Hrabusa 00:03:33 The link in there is new, so I think we can use the old one.
Or, not the old one, but the existing nodes, right? Okay.
Dan Gomez Blanco 00:03:42 Yeah.
Tiffany Hrabusa 00:03:44 I'll post a link.
Dan Gomez Blanco 00:03:49 So I'm seeing, maybe I'm seeing in my calendar the link to the notes.
Takes me to the existing hotel sigen user.
Tiffany Hrabusa 00:04:00 Oh.
The one in my calendar opened a brand new…
Dan Gomez Blanco 00:04:04 Alright.
Tiffany Hrabusa 00:04:05 Brand new file.
Dan Gomez Blanco 00:04:07 Ayeh.
neilyashinsky 00:04:08 I think I'm experiencing what Dan is, if I'm… if I'm looking right.
Hi, Al.
Alexandre Ferreira 00:04:14 Oh, I know that voice! Hey, Neil!
Let's go.
neilyashinsky 00:04:17 Yeah, Alex, what's up? How's it going, man? It's great to see, now, great to see you.
Alexandre Ferreira 00:04:24 Yeah, you too, man.
Dan Gomez Blanco 00:04:26 Nice.
Alexandre Ferreira 00:04:27 Hello, everyone.
Dan Gomez Blanco 00:04:28 Hey, Ed.
Amine Amanzou 00:04:30 Hi, everyone.
Dan Gomez Blanco 00:04:39 Right, okay, I'm, found it. Now, I'm gonna try to claim host.
How does this work again?
Tiffany Hrabusa 00:04:57 In the meantime, if anyone has anything that they want to discuss, please go ahead and add it to the agenda.
Dan Gomez Blanco 00:05:04 Yes, please.
lciukaj@splunk.com 00:05:11 Hi guys, sorry for being late.
Dan Gomez Blanco 00:05:23 Sure, this used to be easier.
I just want clean host.
Mmm.
Needs to be a button to do it.
Click on the participants, okay.
Alright, okay, found it.
Alright.
And now that I did it, the Otter AI note-taker has gone.
neilyashinsky 00:06:25 Ta-da!
Dan Gomez Blanco 00:06:29 Yeah, okay.
Alright, so yeah, please add your, items to the agenda, and then, in the… yeah, so in the…
Actually, this is the wrong date. Today is the 22nd.
neilyashinsky 00:06:49 Thanks, you can see how new I am?
Oh, that's the template, yes, my bad.
Tiffany Hrabusa 00:06:55 Yes. Okay, so this is Union.
neilyashinsky 00:06:56 Yeah.
Tiffany Hrabusa 00:06:58 Okay. Perfect.
neilyashinsky 00:07:00 Yeah, please, put me at the end, or on next meeting. I'm happy to talk.
Okay, chalk this up to an anti-pattern. My hope today was really to just, like, obviously introduce myself. I am Neil. I became aware of the Blueprints project, if I'm using that term correctly, very, very recently.
And it happened to have extraordinary overlap with some of the projects that I've been working on, on and off for a while.
And it didn't seem like there were any reference implementations, reference architectures yet, that had been offered, and so, Alex can attest to this, that, like, me and nature both abhor a vacuum, and so, like.
like, if there are some people who can learn from, you know, this thing that I'm building, like, I don't want to hold it back until it's really great. I mean…
I don't wanna… I wanna hold it back until it's got reasonable quality, which I'm still… I think it's in good shape right now, but I was really preparing to…
just meet with people, understand people's expectations, you know, I'm not eager to rush this by any stretch, really just want to be due diligence. But also, it's, for lack of a better word, like, an open source effort, right? So, like, it's also somewhat counterproductive to hold back for too long. So here I am.
Let me know how you'd like me to expand, if at all.
Dan Gomez Blanco 00:08:33 Yeah, no, that's cool. Thank you very much for joining, and welcome to, you know, I guess if this is your first hotel meeting, yeah.
neilyashinsky 00:08:40 The first one of the project blueprint, I've been at… Oh, okay. Because, as you'll see, there's, like, two, kind of.
cross concerns or whatever, like semantic conventions and the Gen AI. I've been trying to…
you know, bring… what's that word? You know, the insights that those groups are…
developing through their operations and, you know, bring it to a blueprint, I guess.
Dan Gomez Blanco 00:09:11 Cool.
Sounds good.
Well… Glad to have you.
neilyashinsky 00:09:17 Yeah, thanks. So I'll just, I mean, I'll post the, the repo here in a moment, in the agenda, at least for anybody who's interested. I mean, I'm happy to expound a little bit more about, what it is, should, should it be the right time on the agenda, and, you know…
Dan Gomez Blanco 00:09:36 I was gonna say, are you familiar with the, CNCF Slack as well? Are you in that?
neilyashinsky 00:09:40 I just joined today, I believe, yes.
Dan Gomez Blanco 00:09:43 Cool.
Right, so we may not be able to have all the, you know, discussions in depth here, and then sometimes we may need to go, you know, async into that, into Slack, and then we can continue the conversation there, right? So…
neilyashinsky 00:09:55 Is there a… I didn't see yet, maybe, is there a channels for the Blueprint project itself? A Slack channel?
Dan Gomez Blanco 00:10:01 Yeah, so it's hotel-blueprints.
neilyashinsky 00:10:04 Okay. It's probably in the, in the, in the meeting notes. I'll look for myself. Thank you, though, Dan. Appreciate the, the welcome and the intro, and, everybody, appreciate you having me.
Dan Gomez Blanco 00:10:13 Cool, cool, cool.
Right, anything else you want to add?
Otherwise, we can move on to the next topic.
Amine Amanzou 00:10:24 Actually, it's the same for me. I'm, kind of also a newbie here.
neilyashinsky 00:10:29 Nice.
Amine Amanzou 00:10:29 My first, SIGME thing,
just, enjoyed the topic, of the end-user experience, and, saw that this was, like, kind of new projects, sub-project of the end-user SIG. So, just following, seeing if, I can help somehow. So, yeah.
Dan Gomez Blanco 00:10:53 Cool.
I just moved your topic up.
Yeah,
Actually, yeah, I mean, if we're on this, if we want to do a round of intros, maybe, like, that would be a good one. Yeah, so, I'll say, you know, I'm Dan, I've been a part of Hotel for a few years, and, you know, I proposed this project initially after, like, having chats with many end users.
I've been maintainer of end-user SEG as well for a couple of years. I've been in the, in the governance, in the governance committee as well.
And, yeah, and now that I'm not in the governance committee, I said, well, I just actually might have more time to focus on this, which is great. So, yeah, so, yeah, the focus of this is to, as you mentioned, like, you know, try to basically bring those reference architectures and those blueprints for adoption at scale as the day two operations, right, of, of hotel. So,
Yeah, that's me. Anyone else wants to go and do a quick intro?
lciukaj@splunk.com 00:11:54 I can go next. Hello, everyone. My name is Ukash, and I'm part of Splunk, Cisco Splunk. I've been working with OpenTelemetry for the last couple of years. I'm also a contributor.
couple of contributions. I achieved membership… official membership status in December, which I'm very happy about. And I work a lot with, like, traditional legacy manufacturing customers, that's part of my co-responsibilities.
where I'm trying to, you know, convince them for using OpenTelemetry. It's not always easy because of some, you know, the barriers, the adoption barriers, and I also identified similar challenge a while ago, that we don't have the referral architectures.
and patterns, that is something what customers are looking for as well, okay? Show me the evidence, show me that someone else is using that, etc. So I, similarly to the previous speaker, forgot your name, I didn't get your name, but… but… but I'm also working something internally, which is very similar to Auto Blueprint, so that's the reason I would like to be involved in this project, and also, you know, contribute in the broader open source.
permanent.
Dan Gomez Blanco 00:13:01 Cool.
lciukaj@splunk.com 00:13:01 Mutual pace.
Dan Gomez Blanco 00:13:03 Thank you very much.
Nobody else?
Alain Pham 00:13:05 Yep, should I go next? So, my name's Alain, I'm a solutions engineer at, Grafana. So, yeah, I've, I actually spent, my days mainly onboarding new customers to,
hotel and observability in general, so it's the reason why I'm very interested in this, this project. I've been working in open source, for…
more than 8 years now, yeah, including… so Red Hat was my previous company, and yeah, so, really looking forward to, work with you all.
So I actually had a first question here.
Because… so, obviously, this is very much hotel-oriented. What I see, though, in… on the field is that,
most folks, are still using, like, Prometheus exporters, and using, like, OTEL in conjunction with Prometheus and all the whole ecosystem.
Like, how much can we actually include of Prometheus inside of this project?
Dan Gomez Blanco 00:14:10 I wanted to talk about that in my point later in starting, you know.
Alain Pham 00:14:15 Okay, okay, cool, yeah.
Let's discuss that later.
Tiffany Hrabusa 00:14:21 I'm mostly here to observe. I don't have a lot of, actual ideas to contribute as far as blueprints go, but I am, Tiffany. I am a tech writer at Grafana, and I am also a maintainer in the communications SIG, which handles the hotel website and documentation.
So, I will be copy-editing, any of the blueprints that are ready to get published to the website, and helping to facilitate, the move from end-user SAGS repo to the Opentelemetry.io repo.
So…
Alexandre Ferreira 00:15:01 Nice, I can… I guess I can be the next one. Name's, Alachendary, but it's quite long. You can call me Alex.
I'm a observability architect here at Grafana, and funnily enough, I see we have some Grafanisas here. We didn't coordinate this, like, we arrived here from different paths, so I guess it goes…
how much this topic is important, right? So, I usually work with customers trying to drive, their observability strategies, and I've come across some heavy customers trying to implement OpenTelemetry, specifically Traces, and then they ask, okay, do you have any reference architectures that detect
You could suggest to us, And then, while I have some ideas on my mind, I…
tried to research what's the state of this in the community, and I stumbled across this… this SID right here. So, I guess all of this shows how important, this is, for… for the community.
And prior to sequence Grafana, I was a developer and then SRE. When I was a developer, I came across the open source community on Laravel, PHP, for quite some time, for a little bit of time, and then, for the most part, I was…
Not, engaging in open source, and now that,
joining back the OpenTelemetry community, I can… I want to see, how I can help, and very nice to meet you all.
Dan Gomez Blanco 00:16:37 I just realized that, I completely forgot to say that, you know, but I work when I introduce myself. So yeah, I work for New Relic, and I do… I basically work on driving observability blueprints, as well as, you know, as you mentioned, that just reminded me that.
So yeah, part of my work as well is helping customers with adoption, or, like, the majority of my work, and then…
thinking about strategy, and strategic thinking is something that I've been doing for a few years before even, you know, joining New Relic, as I was leading observability at a company called Skyscanner.
So, for…
about 800 engineers, and then, sort of, like, going from no open telemetry to all open telemetry. That was the… the challenge. So, okay, so I guess the intro's done. Thank you all for joining. Then we've got the next topic, which is, I think the first one is, Tiffany talking about
Yeah, it's tight.
Tiffany Hrabusa 00:17:30 In the last comms meeting, I, spoke with the… the rest of the group, and
We have agreed that the proposed information architecture sounds good. We've picked a spot in the main docs now for it to live, and we commented on one of the issues. I think there's two, one for architecture and one for blueprints, so I think we just commented on one of them, but…
But one question was raised, just to get you thinking about it, is how we plan to create the diagrams for these blueprints and architectures.
And I think…
the reason for that is we just want to make sure that the website can support it. Like, we can, we can support Mermaid, and obviously if it's,
like an SVG or some other image file, but just something to think about how we want to create those. And, if we do create image files, they should be something that can be edited again later, so something to think about there.
Dan Gomez Blanco 00:18:33 Yeah.
Tiffany Hrabusa 00:18:34 I don't need answers right now, but yeah.
Dan Gomez Blanco 00:18:36 Yeah, so I think it would be good to know, so I think, you know, Mermaid does make it easier with, with marked… well, you know, with… they will be written in Markdown, right, so it will make it easier, but I don't know if you had any…
experience.
Or, like feedback from people that I've used it, and go, like, alright, there's a better way,
That is also… I don't know.
That has the…
Tiffany Hrabusa 00:19:00 I mean, Mermaid is easily maintainable, but for more complex images, it gets a little messy in the presentation.
So, if we have kind of simple, simple workflows, simple diagrams, Mermaid is great, because you can easily keep it updated and,
even formatting isn't really a problem. But if… if we… there… there is actually a mermaid diagram on the hotel website now that I think is part of the demo, and it's…
it's a really, really complex diagram with lots of pieces, and that can be a little hard to really keep track of in Mermaid, because you don't have the ability to make a lot of
differentiation between things. So.
Dan Gomez Blanco 00:19:45 Yeah. Yep.
Tiffany Hrabusa 00:19:47 And we are working with,
Leandro, who's with Oli Garden, and he is a graphic designer.
Dan Gomez Blanco 00:19:54 So, he might be able to help us if we have ideas for more complex images or things that we want to add to the blueprints. We can always pull him in. I'm sure he'd be happy to help.
Nice.
Yeah, okay, cool.
Yeah, I mean, I personally use a tool called Whimsical that I quite like, but, you know, that's… I don't even know if it's free, so, like, as, you know, one of the requirements is that it must be free, so…
Yeah, and free to use, so…
Cool.
Tiffany Hrabusa 00:20:25 one.
Dan Gomez Blanco 00:20:26 Right.
Tiffany Hrabusa 00:20:26 Sorry, one other key thought there is
it would be great to go for uniformity and consistency in the diagrams as well. So, yeah, that's just one other consideration.
Dan Gomez Blanco 00:20:37 Yeah, I think that we should… we should definitely make that decision.
And probably add it to the… to the template as a note, to the… to the Blueprint template. And the…
Reference architecture template as well.
Which, maybe, or… actually, that's a question.
The idea here is that reference architectures will be more customer… more customer… more end-user driven, right? So this is for everyone's, like, benefit. Like, there's two things that are called out in the project template and the project description, which is, one is hotel blueprints.
And the other one is hotel reference architectures. And we distinct… the distinction between them is that a reference architecture is, at one point in time, you know, an end user shares how they approach OpenTelemetry and their organization across a range of areas.
It would be… still be good to have some…
I guess, format in how we… and how we have these, so they follow a certain format.
But I don't know if, like, if they want to share a diagram, I guess, with their own tooling.
a thing that's probably okay if they share it with their own… whatever they want to share, because it doesn't have… it doesn't need to be maintained, right? It's just like…
at one point in time. It's more like a… almost like a blog post, but that stays there, I guess.
Tiffany Hrabusa 00:21:59 Okay.
Dan Gomez Blanco 00:22:00 while the blueprints, I think, will have to be constantly evolved. I think, Lucas was mentioning this at the last meeting that, you know, it's more like a living document, right? So if we're thinking about a particular thing, we will need to maintain them.
So, I guess, yeah, the…
I would probably focus this on, yeah, so we have some standards for blueprints.
whatever diagram…
tooling standard that we… and format that we… that we have should be in the template, I think.
So, yeah, that's a good, good call-out.
M… does anybody… I guess… I don't have any ex… much experience with that, but if anybody wants to…
Tay that as an action to do a bit of… Like… Research.
And to, you know, what's available, what's easy maintainable?
I'm, yeah, happy to… that would be a… a good… A good issue to raise.
And document it.
neilyashinsky 00:23:02 I'll help out with that, especially if someone wants to, you know, I'm so new, I… I'm fine taking on tasks on my own, but also eager to, you know, join in a task with someone new or old, to ensure good continuity, etc.
Dan Gomez Blanco 00:23:19 So, everyone should be able to create issues in the… actually, this is for everyone that's new. The…
Sophia S 00:23:26 You can apply.
Dan Gomez Blanco 00:23:26 For this, yeah, for this, like, if you go to the SIG end user, repo.
on OpenTelemetry, you can create an issue, and if you use the labeled Blueprints, then it will automatically be added to the board for OTEL Blueprints.
Which is… There's one here, I'll drop the link in the chat.
I can put it in the notes as well, but…
I put it because I… yeah. So, if anyone wants to take that on, and then come up with some recommendation, then we can review that, and then, yeah.
You can create the issue.
Alain Pham 00:24:06 Is it the SIG End User Project?
Well, we're supposed to…
Dan Gomez Blanco 00:24:11 Yeah. Okay.
With the blueprints, label. There's a label called.
Alain Pham 00:24:18 Right, Prince. Alright.
Dan Gomez Blanco 00:24:19 Well, actually, I'm not sure if you're able to label it, but if you create the issue, then anyone in the end user will triage it and add the blueprints label, and then we'll add it to the board.
Alain Pham 00:24:36 So when I actually click, it says,
So I only have, like, several choices, auto, in practice, Q&A, survey, blank issue. Should it be a blank issue?
Dan Gomez Blanco 00:24:48 Blank issue, yeah, I think we can use that.
Alain Pham 00:24:50 Okay.
Okay, cool.
Dan Gomez Blanco 00:24:55 Yeah, so that would be… I'll drop the link in here.
Yeah, so if you create a new issue…
Yeah, blank issues should be the one, yeah.
The other ones are just specific items of… that we… that we normally do. Actually, that's a good question, that you mentioned that. I'll keep that in mind for the next one. At some point, when we've got more of a process, I think it would be a good idea to have certain issue templates in the end-user SEG repo.
to say, hey, you know, I'm an end user, I want to share a reference architecture.
open an issue, and the end user say, we'll review it, and then… or I want to share… I want to discuss creating a new blueprint, and then… So then for the… for this current project, we're just scoping it to, like, 3 blueprints and 5 reference architectures.
minimum, I guess. If we want to do more, fine, but we will call the… the… the project finished at the time we've got 5.
reference architectures, and then 3 blueprints. So, yeah.
Cool.
Alexandre Ferreira 00:26:00 I do have a question on the difference between blueprints and reference architectures. So, if I understood correctly, a blueprint is…
A definition of, the…
the strategy that you… that you've put in the template, like, I forgot the name of the author, it was, richard Rumot, so, we have the diagnosis, which layout based on the problem, and then, the current… current actions, and then
The reference architecture is a example on how to solve a specific blueprint.
Dan Gomez Blanco 00:26:40 Yeah, so that… that's the… that's the current…
you know, that's how I'm thinking about it. I'm happy to be challenged about this, to be honest. But the idea is that, you know, we're gonna have, like… if you take that reference architecture, it's very useful by itself, right? You're seeing how a company, certain company, applied hotel.
But what we start to see is that some of the…
environments have common challenges. For example, if you want to provide
an Ontel, platform, like, an ingestion platform, right, in Kubernetes, then you'll have, like, certain challenges that are the same. How do you configure the SDK in a stable way across, or a consistent way across multiple…
teams, multiple deployments, how do you provide reliable pipelines? If you were to think about OTEL and Kubernetes, or, like, Kubernetes observability with OTEL, then, you know, again, there are common challenges that people are trying to solve.
and then a common set of recommendations. And this is where, like, you know.
you will get into… so, I guess, you know, the taxonomy is, like.
You have blueprints, or sorry, reference architectures at individual…
points in time, this is how a company approached it. It may not cover… they… maybe they didn't have all the same challenges, so they had some that are, like, very, very specific to them.
But if we can take some of the most common ones, and then put them into some common, like, best practice recommendations, then… then that should be the… what makes a blueprint a blueprint, right? And then,
Then this is how someone did it before, right?
Yeah. So there can be more, yeah, more of that, more useful.
neilyashinsky 00:28:16 extraction layer.
Dan Gomez Blanco 00:28:17 Yeah, exactly, yeah.
That's a good way of putting it.
Yeah, so, actually, I'm gonna move this… I think I've got two topics here.
One is to discuss
what are the starting blueprints that we want to have? But before we go into that,
I wanted to review the stuff that is on the board.
M…
which I linked there. So, I don't really want to share my screen at the moment, I've got too many tabs open.
neilyashinsky 00:28:53 But yeah, so there's one in progress, which is the draft.
Dan Gomez Blanco 00:28:57 Actually, no, I'll just take that window out, and I'll share my screen.
be easier.
So we've got this in progress. Oh, by the way, for everyone that is not aware, you can have all the project details here on the left, on the right, if you click on that.
stuff. So, we have the…
the blueprint template.
So yeah, we'll be talking about the template. I…
Yeah, I've not seen this comment, Alan, but yeah, so there is a template here that is to be reviewed. The idea of this template, I'm not sure if it's mentioned there, but we will host this template
in the… Well, that was the idea. And the Sagan user repo.
And then, yeah, so, like, this template will ultimately be in the second user report, not in the website.
Maybe, like, I should probably document that somewhere.
Because on the website, what we will have is the actual blueprint and the actual…
reference architectures. But this template… Which… I click on it.
Yeah, this is basically supposed to be copy-paste to Markdown later.
M… Yeah, this can be in our… Sign user repo.
Because…
Yeah, I don't know if it makes sense to have it in the website. If people are going to raise the issue later to create a new blueprint or a reference architecture in the end user repo, it probably makes sense to have the template closer to that, where the issue will be created.
But for now, I guess what I'm trying to get is some general comments on… or some general agreement, if you think this is a… this is the right… a good template. I guess, you know, I don't… also don't want to let…
perfectly the alignment of good, we can just…
As we're writing blueprints, this can change, and we can…
You know, we can adjust it, but,
At least as we drive, you know, we're trialing out the first three ones, right?
yeah, we can probably start with something, and then… Moving forward, but yeah.
Alain Pham 00:31:16 Yeah, I just put a comment today, so, I went through it, I think it's great. The only thing I was thinking is that, from a new user's perspective, you know, when you see these challenges, you might not be able to,
really, identify… sorry, identify with them, because you've never experienced those challenges, really, right? So I would actually put it more of a…
Objective or outcome-oriented thing, for example.
You know, saying instead of fragmented instrumentation.
what's the objective that you want to reach? For instance, you want to be able to correlate through apps and infrastructure in order to,
accelerate your investigations, right? And then, so the fragmented, instrumentation becomes a challenge, to that objective.
I'm sorry, I think, like.
Dan Gomez Blanco 00:32:12 Like, the inverse, yeah, pretty much, like the inverse.
Alain Pham 00:32:15 Yeah, yeah, yeah.
Yeah, so it gives you, like, a target that you can,
better sort of visualize in your head. And then, okay, along the way of getting to this point, I will face these challenges, which I'm not aware of today, which might make it a little bit clearer.
Dan Gomez Blanco 00:32:37 Let's see,
I mean, that could be…
I guess the good thing about challenges, or I guess that I've seen
Normally working quite well, is that… There's, like,
And more like a story being told, right? So these are the things that you normally struggle with, and this is the impacts that those things have when you're…
On your actual day-to-day.
And then these are how we're solving it. If we're thinking about the objective, I guess…
I guess the entry point to this is, like, someone comes to the blueprints and says, I want to do these things.
Now, basically, coming back to the… how we normally would think about blueprints, it's like, there's a common set of problems that people want to solve.
When they approach, let's say, building a, a… Collector platform, right?
And these as… these are these challenges, and then we're moving on to the…
okay, the policies that address… the guiding policies that address those challenges. If we have it as, like.
Objectives, and is it, like…
We're going into… these are the common objectives that people that are in this particular environment One to solve.
Alain Pham 00:34:08 Yeah, it's… I think… I think it's just, like, putting,
a way of putting the challenges, like, organizing the challenges, right? Because here, It looks like,
We have just a set of challenges.
But it's, it's quite hard to…
Understand, like, what's the… what's sort of the golden path
That you want to achieve, right? Why we're actually solving those challenges.
So, I mean, all of the points that I mentioned here are all right.
It's just, like, putting a direction to it.
neilyashinsky 00:34:50 Did you kind of think of this in the, like, Alan, am I saying that right, Alan?
Alain Pham 00:34:56 Yeah, that's alright.
neilyashinsky 00:34:56 You know, kind of, from my experience as well, it seems like maybe just a little bit more, for lack of a better word, like, metadata about who this blueprint is for and why, and to, like.
like, why am I reading this, or why is it… like, what challenges am I… what can you solve, or what processes can you improve?
So that it just has a little bit of, like, outward reflection or abstraction, I guess, to overuse that term, maybe, of the, you know.
intent behind the document, and I think sometimes that's clarifying both from a, like, the author's perspective, and then also it's clarifying from a, you know, from the reader as well. It's like, is this the right document for me, or whatever?
Dan Gomez Blanco 00:35:46 Tiffany?
Tiffany Hrabusa 00:35:49 I don't have a lot to say about the content of the template itself, but thinking about this from the presentation on the website,
it's good to be thinking about the entry point, and I agree that
Structuring it from a goal orientation is…
ideal. Like, you want to present things in a way that,
presents the solution first, but I also understand
that some people might be coming into this with specific challenges. So what we could do on the landing page for guidance and architectures is create a matrix
that… Basically, you know, Delineates what challenges are solved in which blueprint.
So then people could not just scan
the navigation, but also scan the matrix to see if their specific problem appears in one of the blueprints? I don't know.
Dan Gomez Blanco 00:36:50 Yeah, that makes… I actually quite like the idea.
But also, like, I think there's probably a… we can probably combine both, right? I think, I guess, to your… to your point, Alan, is.
Alain Pham 00:37:01 For sure, yeah.
Dan Gomez Blanco 00:37:02 We can say… hey, you know.
this is the… rather, I mean, this is the… rather than call it a diagnosis, like, it would be like the…
the goals, or the objectives, right? But then the objectives need to be backed by…
problems that are being solved. I guess this is the… this is the thing that, I guess, I see with
some strategies.
That goes straight into the objective, without mentioning the problem to solve.
So… You can have an objective to…
I guess you were mentioning, if I go back here… M…
Alain Pham 00:37:42 You know, they're correlating… Apps and infrastructure.
Dan Gomez Blanco 00:37:45 Yeah, ability to correlate application telemetry and infrastructure telemetry to a root cause.
Yeah, but what problem does that solve, right? Why do I need to… why do I need to do that? What problem does the correlation of application telemetry
Solve.
And this is where, like.
thinking about challenges helps, because they're like, okay, you know, this is what… so maybe, like.
A combination of both is, like, thinking about these, but also being able to list the individual challenges that each of those
main goals.
solved, right?
So… That's what I'm saying, we can probably combine both.
Alain Pham 00:38:24 Yeah, yeah, I agree. So, yeah, I think when I was reading the document, it was like, the intro is just,
how essentially to achieve effective observability, right? And maybe we have to define that a little bit better. Like, what does it mean to have more effective observability? It means you can correlate app stuff with infra stuff, it means that you can get, very quickly to,
to the data that's relevant, etc, etc, right? And then, in order to achieve that, you will face these challenges, like fragmented instrumentation, the insufficient data collection, etc, etc, at scale, etc, right?
Dan Gomez Blanco 00:39:07 So, that would be a combination of both.
Alain Pham 00:39:09 I'd say.
Dan Gomez Blanco 00:39:10 So do you think that it's worth maybe, like, adding a… you know, this is trying to read as, like.
the diagnosis, you know, I start jumping to the diagnosis normally, but, like, there's normally an executive summary there, you know, summary that mentions that.
as part of his summary, do you think is worth… or maybe, like, as a different section, if we add a comment here. So this reads as, like, diagnosis, challenge one, challenge two, blah blah blah. And then you've got some guiding policies, so, like, you know, general, like, this is what we recommend doing.
And that addresses challenge 1, challenge 2, blah blah blah. And then you've got some actions to implement those policies. So,
if you think about goals, it's almost like they come before these ones, right? So, your goals are, you want to do X and Y.
And then… to do X and Y, Whoa.
Yeah, I'm just thinking, to do X and Y, you need to…
Well, you have a set of challenges that are solved.
I don't know if the objectives are almost either the…
the guiding policies, in a way. So if you're thinking…
Alain Pham 00:40:21 I don't think so, because the guiding policy would be more of,
How do you really implement things in order to, overcome the challenges, right?
So the objective doesn't really tell you how to overcome the challenges.
Dan Gomez Blanco 00:40:40 But let's say, for example, here, like, a guiding policy would be, instead of, like, ability… so, ability to correlate application telemetry, that's the goal.
Alain Pham 00:40:48 Yep.
Dan Gomez Blanco 00:40:49 The guidance policy can be telemetry, you know.
Must be correlated across infrastructure and application.
And then to implement.
Alain Pham 00:40:58 Regarding post…
Dan Gomez Blanco 00:40:59 Policy.
Alain Pham 00:40:59 Yeah.
I don't know, guiding… you know, I would say guiding policy would be something like,
You have to label your services in a certain way, and that these labels should match
the applications and in the infrastructure as well. So, sort of like, yeah, please follow these semantic conventions that we have,
On apps and infrastructure, so that would be, like, a guiding policy, right?
That shouldn't be the objective.
objective would be, I want to correlate. But how do I… how do I, reach that, point.
Dan Gomez Blanco 00:41:40 I see.
Alain Pham 00:41:40 Does that make sense?
Dan Gomez Blanco 00:41:41 Yeah, that makes sense. I think I'll, yeah, probably need a bit more…
Thinking… I think, Alex, you've got your hand raised.
Alexandre Ferreira 00:41:48 Yeah.
It seems to me that, in this template, the second paragraph of the summary looks like…
the objectives that we want to achieve with this, right? Because by implementing this pattern, organizations can expect to achieve X, Y, and Z. So…
that's what it looks like to me, right? So…
You have this blueprint, and then the executive summary on why it exists, and we hope to achieve a certain objective or end state, and it is laid out in the summary.
Dan Gomez Blanco 00:42:30 Yeah, I think that's… that's…
Alain Pham 00:42:32 It's true, yeah.
Dan Gomez Blanco 00:42:32 So what… cautious of time as well, we've got another couple of topics to discuss.
would you mind, like, adding some comments here, and then we can… we can continue, like, you know, if you see it, if you see… I mean, I agree that, you know, if we want to…
Have that high level… This is the goals that we're trying to…
To do, if you want to add here, like, what would you put it? Would you put it, like, within one place, or like, you know, and we can discuss that?
Async? Does that make sense?
Alain Pham 00:43:03 Yeah, yeah, I can do that async, yeah, sure.
Dan Gomez Blanco 00:43:05 Awesome. Or in Slack as well, if you… so I'm just conscious of that.
What time?
Cool.
Hmm… Or actually, sorry, I was just still sharing my screen.
Yeah, so.
lciukaj@splunk.com 00:43:26 So, in the meantime, I updated one of the tasks here to the blueprint that I'll be working on, and something I wanted to clarify from the process perspective, like, what is expected from us, because here we have a board, we have tasks, do we need to open an issue for that when we are working, or it's okay with this task only being open?
Dan Gomez Blanco 00:43:47 with… so yeah, we'll need an issue, so this can be then converted into an issue. However, before we… so we've got the template and review.
I just wanted to basically have a quick summary of what we are. We…
I probably choose to speak to… Damian, or…
other people in the DevEx SIG, because I forgot to mention this. The DevEx SIG have been doing interviews to some end users, and they've got some reference architectures not published. So, I don't know if they already have a template for this, I need to reach out.
I don't know if they have a template for the reference architectures, or if they've got some that they, you know, they could start sharing, so…
Yeah. I don't think that it's anyone from the DevEx sig here, right?
No.
Alex, you've got a question?
Alexandre Ferreira 00:44:44 Oh, actually, I forgot to lower my hand.
Dan Gomez Blanco 00:44:46 All right. Yeah, so basically, that's for me. I'll reach out to the DevX agency, if they've got anything already.
Related to, you know, a template for reference architectures.
Now, the next thing in this, probably before we jump into that, I wanted to agree on the blueprints, or the initial set of blueprints to focus on.
And I posted a message on Slack, I'm not sure if people have seen it, but I'll add it to the notes.
And then we can probably quickly discuss.
Some ideas.
Well, no, nice, some…
That's… bad formatting.
So, yeah, so I think… I guess the, 3 things in mind.
And then, of course, These are just ideas,
I'm asking for a bit of… Ehh…
Maybe this is how a mind works.
As you can see that I started from the problems to solve, right? So,
Yeah, so ideas. Basically, these are the three that I had in mind, in terms of, like.
one for, you know, deploying a centralized telemetry platform, and what I mean by this is, like, you know, deploying a…
if you're a platform engineering team, you want to provide access to, Kubernetes instrument, or, sorry, OpenTelemetry instrumentation and pipelines, and sort of like that.
Contract with the rest of the engineering team.
And, yeah, and the…
the challenges to solve relate to how to achieve consistency across SDK, config across different teams and challenges and languages, how do you…
Manage Collector Configs Pro, or scalable deployments, data optimization, and so on. So, basically, related to, I guess, this would be more related to the part of, like, configuring the SDK
the language SDKs, and different… across different… teams, and different deployments.
I think we can probably aim this at, like, Kubernetes.
And then… infrastructure in our Kubernetes environment.
And then, so, like, the part of, like, the collector pipeline, and how it all fits together, right? Routine, sampling, blah blah blah, all these, all these things.
The other one that I thought about was more focused on Kubernetes, and this is where, like, Alain, you would mention the…
you know, Prometheus interoperability, if you're deploying Kubernetes, you probably want to have, like.
A story about, like, how do you manage things that cannot be…
monitored, or that cannot expose OTLP, that cannot push OTLP out, right?
That's probably another one.
And then, another one I was thinking was, serverless, but this is what I'm less sure about.
I know that people struggle with serverless, M…
Not just to… it's not just the server… the serverless function itself, but how it all fits together in an environment, right?
So, that's another one. And other things that I consider, like IoT or client-side, which would include, as well, how do you actually make the data, you know, put the data back in collectors, or…
legacy infrastructure. I know that, for example, the blog post that Luke Harris mentioned cover a couple of these, like IoT and legacy infra.
so yeah, I don't know if you… If you have any… any, I guess…
Yeah, any thoughts on this? I would personally, if we were to take this, I would probably… I was thinking of, like.
Taken on this one, if it makes sense.
And then collaborate on this with someone else.
neilyashinsky 00:49:00 Yeah.
Dan Gomez Blanco 00:49:00 But yeah.
Alexandre Ferreira 00:49:01 I can… I can take the Kubernetes observability one, and then my… my thought is…
that, like, 70% of customers will be using Kubernetes, but there are…
users that are not using Kubernetes, or, like, using plain VMs, and then I think that Lucas' idea on having a blueprint for non-Kubernetes environments is very beneficial as well.
So…
Dan Gomez Blanco 00:49:31 So, what we're saying is, like, instead of a serverless one.
we could do one for, like, I guess, SDK and collectors, or, like, platform, which would probably be deployed in Kubernetes, to be honest. Then Kubernetes-specific.
Including workloads that… You know, including that piece about Prometheus interpretability.
And then another one for… like, non-Kubernetes, like… Stuff? Does that make sense?
Alexandre Ferreira 00:50:05 Yep. Permit this.
Dan Gomez Blanco 00:50:09 I guess, you know, we don't need to vote now, but if you're like…
You know that, yeah.
Alexandre Ferreira 00:50:15 Yeah, I think it's a good idea, like, whenever we are working on, or the customer is taking a look into the blueprint for either Kubernetes observability or non-Kubernetes, we will assume that the customer already
have gone through the SDK one, right? Because one thing's about instrumenting everything, and then the other thing is about having the collectors to send everything in. So I think this is a nice story of, hey, deal with SDK instrumentation first, then collectors, either Kubernetes or non-Kubernetes.
Dan Gomez Blanco 00:50:55 Yeah, I think that… that makes sense.
neilyashinsky 00:50:58 Yeah, agreed.
Alain Pham 00:51:02 So, there's also the whole world of, middleware, like…
Kafka, message brokers, databases, and things like that, right?
Dan Gomez Blanco 00:51:12 I mean.
Alain Pham 00:51:12 That's okay, I think that's an important bit.
Dan Gomez Blanco 00:51:15 Yeah, I think we're probably gonna not struggle to… we're not gonna struggle to find different things, right? So I'm just thinking of, like, which ones, you know, like, do we want to take on, for our first batch? You know, I don't want to, let's say, boil the ocean, and then, you know, rather than, like.
If we decide on 3, then we can just do more later, right?
lciukaj@splunk.com 00:51:37 I think we should be, like, smart in terms of, you know, grouping these use cases together, right? Because we can work on 100 different reference architectures or blueprints, or we can be smart and we can make 3 or 4 or 5, then we can cover everything, right? So, I like this approach with Kubernetes, and let's say, non-Kubernetes, and then we can put, let's say, the…
Serverless could also fit into non-Kubernetes, right? Or something else, so… This kind of thinking.
Dan Gomez Blanco 00:52:04 But I guess, you know, when we,
when I was thinking about, like.
centralized telemetry platform, for example. I wasn't thinking of… and maybe this is where, like, it's worth opening the issues to discuss what we, you know, for each one of these. Actually, if you go through here…
Before we actually start to…
lciukaj@splunk.com 00:52:23 To put words onto, you know, like, actually work on the blueprint.
Dan Gomez Blanco 00:52:27 we should probably agree on the scope. Otherwise, there may be, like.
a lot of, like, interlap, you know, between… overlap, sorry, between, between blueprints, right? Which probably we should avoid.
So, on the, for example, on the central telemetry platform, what I was thinking is, like, talking about…
the collector gateway, and the select SDK config.
So, because it all fits together under, like, you know, you're a team, you're providing that service. But then…
the Kubernetes one be more about, like, how do you observe Kubernetes itself?
and then workloads that are deployed in Kubernetes that are Kubernetes native, I don't know, like, Core DNS, or how do you get data out of, like, Argo, you know, all these… all the things. That was my idea around, like, separation there. I'm not sure if that…
If that makes sense. And then…
non-Kubernetes, of course, that will be…
more, like, infrastructure… I guess that's what you were thinking, Lucas, or…
lciukaj@splunk.com 00:53:33 Yeah, yeah, yeah.
Dan Gomez Blanco 00:53:37 So I guess maybe what it's worth doing is, like, I can take the… the 1, 2…
do the central telemetry platform, and basically.
More, like, scope it a little bit there, what we're trying to solve, and what components we're trying to target, and what environments.
lciukaj@splunk.com 00:53:54 If someone can take on the Kubernetes one.
Dan Gomez Blanco 00:53:57 Then you can try to scope that.
And I think if I go back to… the projects, the project board… one second…
I think I already put placeholders in there for…
For these, so we can just do it now. And that will make it easier.
Let me just… Share my screen again.
Tiffany Hrabusa 00:54:27 Dan, I just created an issue for the diagramming tool, so if you want to add the label…
Dan Gomez Blanco 00:54:37 Cool, so,
One second, I'm seeing it,
Right, cool, I see it. I'll like the label.
That, shoot, add it, yeah, that is into the to-do.
Right, so… Who said that was gonna be…
Can I assign this to people?
Who said that we're gonna be looking at, like, different, like, tooling for Blueprint diagrams.
Tiffany Hrabusa 00:55:24 I think Neil said that he was interested.
neilyashinsky 00:55:26 Yeah, I would hop on this,
Yeah, I just wanted to make sure, because I wasn't who brought… the person who brought it by… Tiffany, I thought, was who you're referring to.
Dan Gomez Blanco 00:55:37 What's your GitHub handle?
neilyashinsky 00:55:39 It's N-E-I-L… Dash the… dash…
Knowledge within… without a K. N-O-W-L-E-D-G-A-B-L-E.
Dan Gomez Blanco 00:55:52 Hey, NO…
neilyashinsky 00:55:54 knowledge without the K.
Knowledgeable… sorry, without the K.
Alain Pham 00:55:59 Yeah, yeah, okay. That's fun.
neilyashinsky 00:56:01 Oh, thanks, yeah. It was a little shout-out.
Dan Gomez Blanco 00:56:03 I cannot… right, so unfortunately, I cannot assign someone… I didn't know this. Sometimes, you know, like, there's weird… GitHub is weird. Like, you can tag people, but you cannot see their names if they're not part of your org, but you can still tag them, but apparently…
I can't assign you anything if you're not part of the hotel org.
So for now, if you drop your name… if you… Yeah, if you drop your naming here, then…
neilyashinsky 00:56:29 I can do that.
Dan Gomez Blanco 00:56:30 And then, you know, as you contribute, if you want to be part of the OpenTelemetry organization, we'll sure we'll be happy to sponsor you.
neilyashinsky 00:56:35 Great. Thanks.
Dan Gomez Blanco 00:56:39 Mmm… Cool So, got that.
And then, yeah, so I had Blueprint, so… I guess you took this one, right? You changed the title here, Lucas.
lciukaj@splunk.com 00:56:51 Yeah, slightly change the title, and yeah, I'm happy to collaborate with others, so if someone is interested in this topic, please join.
And we can start working on this. I'm kind of busy this and next week. I'm moving to the new house, so it's a very crazy time for me. We're making different teams, and also there is winter storm coming to North Carolina, everyone is in panic mode.
Dan Gomez Blanco 00:57:12 So…
lciukaj@splunk.com 00:57:13 Oh…
Alain Pham 00:57:14 Oh, dear.
lciukaj@splunk.com 00:57:14 Most likely, I will start working on that, like, beginning of February, but that's my goal for February, for sure.
Dan Gomez Blanco 00:57:20 This is when people started getting, like, milk and bread. It was like, that's the perishable, so you just go for the tin food.
They can just plop it outside in the snow. It'll be that cold.
Cute.
Alright, I will change this then to,
I need to remember to use American spelling.
neilyashinsky 00:57:52 Not on my account, I hope.
Dan Gomez Blanco 00:57:58 Okay, so I will take on…
this one, and then if anyone wants to, you know… I'll scope it a little bit better, but if you think about it, it's like…
the SDK instrumentation… And… Gateway model, basically.
Hmm.
And and then we had a third one that we said, Kubernetes, yeah.
Alexandre Ferreira 00:58:23 Yep.
lciukaj@splunk.com 00:58:30 So, we've got an issue for this task, right, which is… which is created, and…
I remember our previous conversation on the… last week, when we…
discussed that there is no need for open PR as of now, since we don't have yet any, like, blueprint, and there is no structure on OpenTelemetry.io, so I think that, so we can just paste the Google Doc link in the issue, so… so people can collaborate on this, right?
Dan Gomez Blanco 00:58:59 Yeah, so what I would… what I would… as a…
workflow probably makes more sense to do that. I think it's easier to have a… you know, Google Doc.
For quick, so, like, draft, and then when you're ready for a… for review, you can open then up here, and then…
lciukaj@splunk.com 00:59:17 Should that be, like, Google Doc from my private Gmail, or there is some other process for that from OpenTelemetry?
Dan Gomez Blanco 00:59:23 Just your private, your private. Or your company, or your company, if you've got a company Google account, whatever, it doesn't…
lciukaj@splunk.com 00:59:31 Okay.
Sounds good.
Dan Gomez Blanco 00:59:35 Yeah, as long as his, like, one… as long as his, like, Available for everyone to view.
You can give, like, specific people, edit access.
If you won.
lciukaj@splunk.com 00:59:47 Cool.
Dan Gomez Blanco 00:59:48 There shouldn't be any secrets.
lciukaj@splunk.com 00:59:51 That's right.
Dan Gomez Blanco 00:59:54 Cute.
Alain Pham 00:59:57 Dan, so the blueprint that you're taking on, is it related to application?
Instrumentation, is that the thing?
Dan Gomez Blanco 01:00:05 Yeah, it's more like if you… yeah, so if you think… yeah, I think it solves the challenges of, like, as we see in more platform teams.
Providing that abstraction to the rest of the organization. It's like, how do…
how do they do it in a stable way from the, like, SDK config, to the…
gateway, basically. So they… Right, okay. The platform teams are in charge of that. And then, you know, they get their engineers to go in, and this is probably one of the things I would like to discuss in the Blueprint, which is the…
a lot of people miss this on hotel, which is the advantage of that decoupling of API and SDK, right? Because then, if you have a platform engineering team, and you're thinking about, like, contracts between different… or interaction modes between teams.
their developers should only care about the API, and the SDK should be configured automatically by…
you know, tooling, right? In a standard way. Or in a standard and extensible way. I think that's another thing that people get.
I guess… Yep.
Alain Pham 01:01:08 Got it.
Dan Gomez Blanco 01:01:09 But yeah, so I guess, you know, what I'm trying to say is SDK config and the… and the… the contract with the gateway, with a collector gateway.
Alexandre Ferreira 01:01:20 And then the… the foreman of the…
the gate… the format of how the gateway is deployed is then the responsibility of the blueprint of Kubernetes, right? So…
Dan Gomez Blanco 01:01:33 No, I think for the… I think it would be… because, to be honest, that's another thing that I would like to mention. For blueprints.
we are not really trying to reinvent the docs, as in, like, you know, there's really good docs on, like, the collector deployment architect, deployment, patterns, so if I were to mention, like, oh, you know, a gateway, well, I would probably just say, hey, here's the docs for how to deploy a gateway.
Or here's the docs for how to do tail sampling, right? So, I think we don't need to go into a lot of detail into how to do tail sampling or deploy a gateway.
But just point to… to the… to the specific.
neilyashinsky 01:02:14 Shocks.
Should Blueprints take a… a semi, if not full, technology-agnostic approach? Is that kind of what the intention… the separation between a blueprint and a reference architecture is?
Like that.
Dan Gomez Blanco 01:02:31 Well, a little bit more of, yeah, like, what is the problems to solve, and…
But when you say technology… I mean, they should be opinionated.
neilyashinsky 01:02:41 bright.
Dan Gomez Blanco 01:02:41 I just… yeah.
neilyashinsky 01:02:42 But in a non-tool-specific sense, I guess. Like, OTEL, as I understand it, it's like, here's how it should work.
And then there's examples that show how it… how it is working.
Dan Gomez Blanco 01:02:55 Oh yeah, yeah, we shouldn't really mention, like, go and dump this in New Relic or Grafana or whatever, you know, no, like, we shouldn't be…
explain… or… well, and if we were saying, like, hey, using a… you deploying in Kubernetes, I guess, yeah, we are using Kubernetes. We're trying to…
neilyashinsky 01:03:10 Right.
Dan Gomez Blanco 01:03:11 Yeah.
neilyashinsky 01:03:12 Yeah, it's kind of, like, straddle the line, I think Alex brings up a great point in, like, there are these delineations that are not necessarily unclear, but they're nebulous, maybe, is the right word. And different people will expect maybe different things out of a blueprint than others.
Dan Gomez Blanco 01:03:29 And in some ways.
neilyashinsky 01:03:30 If you remove all explicit technology references from a blueprint, you'll start watering down its value, but if they may be working hand-in-hand with the right reference architecture, that's…
how they… I'm gesturing in the air, and I realize I don't have my camera on, but there's an interconnectedness of flow of our sorts between where one ends and the other begins, okay.
Dan Gomez Blanco 01:03:52 Yeah.
Tiffany Hrabusa 01:03:52 I can tell you from the website point of view, we have a policy of prefer CNCF projects first.
tools, in the CNCF ecosystem, and if there's nothing there, then definitely open source.
So… And just use that. That's…
neilyashinsky 01:04:10 Great. Thanks, Tiffany, that's a great.
Dan Gomez Blanco 01:04:13 Yeah. I mean…
To your point, I guess you wouldn't say, oh, you know, well, you can deploy a collector gateway and then, you know, use Cribble for, like, you know.
Again, you know, that's… that wouldn't be… yeah, I guess that probably wouldn't be an advice that many people should just follow, right?
Or we should be recommended. But yeah, cool.
Okay, we're running 4 minutes late, but yeah, thanks all for joining, that was very good, and thanks for being part of this. Quite exciting.
Indeed. Thanks.
Alain Pham 01:04:46 Thank you very much, bye-bye.
neilyashinsky 01:04:47 Thanks, Dan. Thanks, everyone. Bye.
