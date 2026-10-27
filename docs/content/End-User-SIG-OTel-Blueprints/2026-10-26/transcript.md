SIG: End-User SIG: OTel Blueprints
Date: 2026-10-26
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Dan Gomez Blanco** 03:25 Hello?
Hi there.
You hear me, Kate?
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 03:33 Hi, Uzo, how are you?
**Uzochukwu  Nweneary** 03:35 I'm crying at the big…
**Dan Gomez Blanco** 03:37 Hello, hello?
**Uzochukwu  Nweneary** 03:39 How you guys doing?
**Dan Gomez Blanco** 03:40 Yeah, good, good.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 03:46 We were just talking, so I didn't say hello, but I probably stopped for the recording.
**Uzochukwu  Nweneary** 03:55 Thank you.
**Dan Gomez Blanco** 03:57 It's quite dark here now.
The days are getting shorter.
for, well, here in Scotland, normally, sunset? Is it about… 4PM?
In the winter, so, yeah, 3.30 maybe? Yeah, it's, it's quite dark these days.
So the clocks change, right? So at least in the morning you get some, some, Brightness, but now it's just… yeah.
Pretty dark.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 04:34 So, how did… did you give a talk at, KCD UK?
**Dan Gomez Blanco** 04:39 No.
I… I did… I submitted a talk, but it didn't get accepted. It was good. I met with Adriana and other people from OTel, of course, and we talked about… Actually, we talked about Blueprints quite a lot in the hallway track.
with other end users and stuff, so it was, it was good, good to validate some of the things that we're doing. I think one of, Yeah, I said that they wanted to… contribute as well, then maybe join us, so… Hopefully.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 05:13 Yeah, I've seen, a few of the drafts and proposals. I haven't had time to look at them, and I figured.
Now that, alex's, Blueprint is merged, we can maybe triage. Hi, Johanna!
**Johanna Öjeling** 05:27 Correct.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 05:29 It's so nice to see your face!
**Johanna Öjeling** 05:32 Me too! It's been a while.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 05:40 And Uzo, I know that you have, your proposal for, the Prometheus Blueprint, so yeah, maybe, Dan will walk us through what he's thinking as far as where we should go next.
**Dan Gomez Blanco** 05:53 Yep.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 05:55 Hi, Lukasz.
**Lukasz Ciukaj (Splunk Inc.)** 05:56 Hello, everyone.
Good to see y'all.
**Dan Gomez Blanco** 05:59 always last minute, I'm trying to create the notes, and then I'll share.
**Johanna Öjeling** 06:20 Do you use the End-User's, like, meeting notes for this meeting, or is there a separate Blueprint?
**Dan Gomez Blanco** 06:26 There's that one, I just, added a few, so we… We normally do a… I just shared it there… We normally do, M… Yeah, we just put there, like, whatever… there's the general session, and there's the OTHO Blueprints.
session, I need to change the dates.
There we go.
So yeah, please add your topics to the agenda.
I think we're all… So here, should we go through the… First thing I wanted to go through is the, the… The boards, basically.
And then we can cover the draft for the blog post, Lukaszh?
**Lukasz Ciukaj (Splunk Inc.)** 08:31 Sounds good.
**Dan Gomez Blanco** 08:32 Let me share my screen.
Cool.
Yeah, add your name as well, if you're… If you want to add your name. So… Just as a quick summary of a quick, Yeah, basically a summary of where we are.
We have two projects, let's see, Yeah, Lukasz and I, in the last meeting, or the one before.
we decided to split… well, to create a new… a new project for anything that's stacked with Blueprints or reference implementation.
This board is the one that we just… that we will close when the project finishes, or the bootstrap project finishes. And then that is when we do the usual, Well, ceremony and OTel of, like.
put in the project description and the completed projects, and so on. It's not like… nothing else changes, apart from us saying to the community, we have completed the bootstrap, and we're ready for scale, right? That's the… that's the idea.
M… So, yeah, so I think… the two things I wanted to go through… Is… and now that… Johanna's here, that's great.
Because we have had this for… You know, basically, like, the reference implementations that are currently published are the ones that were created not from the template, but from blog posts that were published, and then the DevExSec were doing the, as pre-existing interviews that were before we even started this project, right? And so there are 3 already published, I think. Johanna, there's another one that's already a draft in the website? Is that correct?
**Johanna Öjeling** 10:26 Yes, exactly. There is one about Key Club coming up, and I saw, Tiffany… Tiffany, you set the date to the 30th of October, right? So, yeah, later this week, it should come up.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 10:39 Yep. Yeah, the blog is very busy right now, so,
**Johanna Öjeling** 10:42 It looks good.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 10:43 Coming up on… on the 30th.
**Dan Gomez Blanco** 10:46 Coop.
**Johanna Öjeling** 10:46 Nice.
And we have yet another one after that about Atlassian. It's still in the Google Docu draft that the author is working on, but we have an issue for it on the OT as well. But yeah, those are the ones Based on the interviews.
**Dan Gomez Blanco** 11:05 Cool, awesome. So… Yeah, so I wanted to ask two things and to get, like, consensus on a couple of things. First one is, for those, we always agreed that we would just copy them over to the reference implementations, like, no reformatting, or retemplating or anything like that.
I guess that will be the case anyway. When these get written, we'll do that same thing.
One thing that I wanted to ask from the… maybe from you, Johanna, as you've written a bunch of them, or reviewed… If you could go through the current template that we've got here for reference implementation and, you know, give us some feedback if it's too much, if it's too little, if it's, you know, things that you think would be useful. I think when I put together the template, I just tried to already use some of the things that you were doing in the… in the, in the blog post that you've written, but then I added, perhaps, other stuff that… yeah. Some of the feedback that we've got is, like, everything here should be optional, as in, like, there are different sections of it.
In the template.
But we don't want to… we want to have a relatively low Barrier of entry for… people to write them, right? So we don't want them to have to do everything that is in there.
But yeah, so I guess if you had any other feedback, that would be… that would be awesome.
Because we've not had anyone until now, because we do have a blueprint that's… or a blueprint, a reference implementation that is already following that, and there's a proposal for that.
But up until now, we haven't had anyone follow it, right? So we don't have any feedback on someone that's actually gone through the process, and yeah, if you can give us some, it would be awesome.
**Johanna Öjeling** 12:53 - yeah, I've had an initial look at these resources, and I can take more thorough look as well, but in general, I think the template is really good, and the guidelines as well. I was… Yeah, amazed by how, like, yeah, it really provides good support, for, reference implementation authors, and I think you've covered so many important parts and interesting parts to readers about their stories.
So, like, in general, nothing to complain about. I think, yeah, they are really good, but I, I am thinking, how can we… or maybe… Yeah, how to make it even clearer to users that, it's not… mandatory to… to, like, tell all of these parts, and, like, you can share as much or as little as, you want, Or if we can… Yeah, like, how to even lower the threshold, more, and… maybe… I know it's mentioned in the, the issue template.
That, like, they can… do you want to write it yourself, or do you want support?
**Dan Gomez Blanco** 14:21 Yep.
**Johanna Öjeling** 14:21 I wonder if… Yeah, if… if we can… highlight… Even more that, like, they're willing to support them, and… Maybe even, interview them if… if that would make things easier. I know there are several people of us in the Devixing who are happy to, like, continue interviewing organizations and writing blog posts, so… Yes, I think that's my… My thinking, or my thoughts for… How we could, like, improve this.
**Dan Gomez Blanco** 14:58 Yep.
**Johanna Öjeling** 14:58 Or make it easier to, yeah, get more, reference implementations.
**Dan Gomez Blanco** 15:02 Yeah, it makes total sense. I think two things, then, like, the first one, make it… make… make it clear here.
That they don't need to fill every single section.
And then we can help them to write it. And the second one is, like, even if they don't want to write anything, we can still do an interview with them. And then… It'll be writing for them, okay?
That's good feedback.
**Johanna Öjeling** 15:26 And, is, is, like, the GitHub issue the place where we want the discussion to happen, if… if a user… wants to, like, potentially contribute? Or do we also want to mention, like, Slack channel?
Or we can…
**Dan Gomez Blanco** 15:47 You mentioned the Slack channel. I think my concern is that a lot of people cannot join… well, not a lot, to be fair, but I've heard of End users that are not allowed to join Slack.
**Johanna Öjeling** 15:58 Okay, hmm.
**Dan Gomez Blanco** 16:00 So, I think if we keep at least the… the, yeah.
the conversation, maybe we can offer, like, you know, a chat on Slack or whatever, but, like.
I would rather them open an issue, and we would.
**Johanna Öjeling** 16:15 -
**Dan Gomez Blanco** 16:16 the proposal there, rather than keeping it on Slack, where, like.
**Johanna Öjeling** 16:19 Yeah, makes sense.
**Dan Gomez Blanco** 16:24 M… Cool.
So that's basic… I saw this open as well for… so I guess this means that this is the key cloak.
This will just be a copy of whatever we… We do in there, right?
In the… sorry, in the book… in the blog.
**Johanna Öjeling** 16:42 Yeah, exactly.
**Dan Gomez Blanco** 16:44 And this one… is the one that I mentioned earlier. So they propo- they use the, you know, they clearly use the… the template, so that's great. To be fair, like, they've already… I did mention that we are all quite busy with KubeCon and so on, so it's just to set expectations, but they want to, yeah, write it themselves.
one… and they already opened a draft PR. So, the, one thing that I would… that I want to get consensus here as well, is how do we see… the blog and reference implementations, when people publish a new one. Do we want to follow the same model? We're, like, you know, following the template, we… we push them, we… Publish in both places? Or do we want to… Do a shorter blog post.
Pointing to the reference implementation.
What would you… Say is perhaps the… The best way to approach this.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 17:52 I, my personal take is that the documentation should be the source of truth, so, it would make more sense to do… if we're going to do anything on the blog, just a shorter, post that points to the docs. I would prefer most of these… I mean, obviously, the DevEx interviews originated before Blueprints really had any scaffolding set up, so the order there was switched, but I would prefer to see things go straight into the docs first, and then we can advertise them on the block.
Personal preference.
**Dan Gomez Blanco** 18:30 And the blog would be… in a way, almost, like, optional, right? As in, well, if people want to do it, they can do it, but… yeah.
The truth is, the references, the… the docs.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 18:42 Yeah, and this… Is a bit premature, but we are, moving in a direction where the blog is going to be for, project updates.
As opposed to, outsiders who are looking to write posts to publish on our blog. So,
**Dan Gomez Blanco** 19:06 Makes sense.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 19:06 In that sense, it makes… it would fit with that, Provision, if the docs existed first, and then… And then the blog post comes out.
**Dan Gomez Blanco** 19:17 one of the ideas that I… that were going through my head were… maybe this is when we get more refs implementations, or a lot more.
But if we were to have, like, something like 3 or 4 per quarter, or 6 months, or something like that.
There could be one blog post that summarizes them, right, and then blends to all of them, rather than one per each.
Yep. That would be a… A better way of doing that.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 19:47 Yep, for sure.
And, The authors of the reference implementations are welcome to do whatever social promotion that they want about them, so, That's… that's absolutely fine. I… we're just… the blog has become quite overwhelming for the limited capacity that Communications SIG has.
Yeah. And so we are looking for, practical ways to, create… Space for us to actually work on docks.
Yeah. So, yeah, that's, I think, Unless Johanna has different thoughts about the ordering there, but my personal preference would be put it in the docs first, and then… depending on… the volume of reference implementation creation. We can do one-off Blog posts every once in a while.
to advertise them.
**Johanna Öjeling** 20:50 I agree with you, Tiffin. I think the reference implementation in the documentation should be the source of truth, and if there is a blog post, it could be, like, a shorter version, or just, like, announcing that there is a new reference implementation, but I don't see that there necessarily has to be a blog post either. It could be… like, Yeah, a social media post, or, like, gathering, Many reference implementations into the same announcement.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 21:25 That's a good idea, too. And we are, Severin's actually working right now on a way to kind of automate social media stuff for us, so that we can be more vocal in that respect. Right now, it's very manual.
So we can absolutely do, social media posts about, a new Implementation being published.
**Dan Gomez Blanco** 21:47 I think…
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 21:48 Published.
**Dan Gomez Blanco** 21:49 I think that would be good, actually, because then… I mean, well, the idea with what I was talking to Severin about this, it would make a… I mean, sometimes… I mean, I'm a reviewer in Buffer as well, and I just… I don't normally look at Buffer, but I would… I think I would look more at, like, a PR that's assigned to particular people, right?
And also, that would give different SAGs the, I guess, more clearer access to publish things.
On…
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 22:17 Yeah, I mean, comms has… like, I write… if you see social media about a blog post, I've written it, so it's, it's still a very manual process right now, but, Yeah, I think… Hopefully, we're streamlining that.
Coming up with some guardrails for the blog itself.
Anyway, that's not the topic of this meeting, but yeah.
**Dan Gomez Blanco** 22:45 No, but that's good, good, good, good context. Okay, so I think we've got a path forward, which is… Yeah. We will, for now, just add… apart from the ones that were, like, original by the DevEx Inc. The new ones that get merged don't need a blog post, and they just get directly into the docs, and then we can publish them… we can publicize them on social media.
And then we can think about… Maybe a future of, like, review of the last 6 months or the last year of reference implementation.
Cool. Can I ask a favor then, Johanna? If you leave any… you met… you had a few comments there, if you can just drop them in here quickly, then we can close this, Next section.
Awesome.
Good stuff.
Before we go into that, which is the… The wrap-up of this project.
I wanted to… Also, think, you know, about this one, because there was an issue here to agree on what missing reference architectures or reference implementations we would need to complement Blueprints, and I think we, we are fairly… with the current Blueprints that we've got, I think we're covered on the Kubernetes side, except the fact that we don't have anyone using the OpenTelemetry kube stack.
chart, but that's okay. I think there's, like, we're already calling for… for something there, so that's agreed. I guess the other one that we… that we mentioned here is… Yeah, so something that can back up, back the, infrastructure and processes.
One.
Don't know if you had any other thoughts about this, Luke, but what I was thinking is, like, we can probably… Agree on the ones that we want to… to… to get.
People from, and then we can close this issue as well.
Because I don't think we need to keep this issue open, if we agree on whatever… ADS we want to cover for reference implementations.
So, the common would be, I'm acting at that, is we need To find some end user, that is.
doing the, or already using the OpenTelemetry CubeStack.
And… I've got one in mind, but I've not asked yet.
And then Lukaszu was mentioning someone using some of the infrastructure, related instrumentation, right?
**Lukasz Ciukaj (Splunk Inc.)** 25:18 So, Dan, so the question is, like, if you want to have a reference implementation, assigned or referenced in the Blueprint itself, right? So, so there is no, like, just a blueprint without a reference implementation, correct?
And that… the question is if we want… That before we close the bootstrap.
**Dan Gomez Blanco** 25:42 No, I think we can… I think we can close the bootstrap.
**Lukasz Ciukaj (Splunk Inc.)** 25:46 Yeah, that's what I mean.
**Dan Gomez Blanco** 25:48 Then we can complete… you know, the project is, in a way, complete after we've got 3 Blueprints and 5 reference implementations, that's what we said.
**Lukasz Ciukaj (Splunk Inc.)** 25:57 Yeah.
Yeah, ideally, yeah, we spoke about that last time then. I mean, ideally, it would be great to have, let's say, the blueprint, where we define some, let's say, pattern or architecture, and then below that, we have, okay, so this is the theory, but then we have a practice, right? So we have this organization that implemented that, or something similar, but It's… I mean, I'm not sure if we should push for this, like, if there is someone reaching out, or if there is someone, like, you know, opening an issue, that's fine, but I don't know, like… Blueprint itself, it's okay too, right? Having just the Blueprint.
**Dan Gomez Blanco** 26:39 It's more for, like, people that, either if you're an end user that's watching this, or if, you know.
you and I, and other people that work for vendors, like, you know, you work with end users as well, right? So it might be a good idea to just… propose it to them. Hey, by the way, you know, you're using this, we're looking for… Yeah. Looking for a…
**Lukasz Ciukaj (Splunk Inc.)** 27:02 So, I would I would call it more, like, nice to have than mandatory, right?
So… but maybe we need to figure out some process, right? Maybe… each of us can, or maybe occasionally we can post in, I don't know, in the Slack channel, or on social media, hey, have you… do you have the scenario in your organization that fits into the Blueprints that we have? Reach out, or feel free to open reference implementation, something like that, right? More like outreach to get people that already implemented that, so… but again, in my opinion, that should be more, like, nice to have than mandatory.
**Dan Gomez Blanco** 27:41 Yeah, so what I mean is that we… I don't mean that we need to do it Is this something that, you know, we agree that we want to ask about.
**Lukasz Ciukaj (Splunk Inc.)** 27:52 Yeah.
**Dan Gomez Blanco** 27:53 There's no… there's no mandatory here to close any type of project. If it happens, it happens. If it not, it doesn't happen right. But, like, we should aim to get, you know.
If you find someone that is using either OTel for infrastructure, and this goes for anyone in the core, right? That's using, you know, OTel for infrastructure as per that Blueprint, or someone that's using, sort of, yeah, the OpenTime into CubeStack approach, then just, it's a matter of.
**Lukasz Ciukaj (Splunk Inc.)** 28:21 I see.
**Dan Gomez Blanco** 28:21 send him a message. I don't think.
**Lukasz Ciukaj (Splunk Inc.)** 28:22 What I'm thinking now, John, maybe what we could implement it is, at the bottom of each Blueprint, maybe we could add some paragraph or banner, something like, hey, do you have this implemented in your organization? Like, why not you reach out to us and.
**Dan Gomez Blanco** 28:39 It's a good point.
**Lukasz Ciukaj (Splunk Inc.)** 28:40 They start working on reference implementation.
**Dan Gomez Blanco** 28:42 So, Alex already.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 28:46 Yeah.
**Dan Gomez Blanco** 28:47 Nope.
**Lukasz Ciukaj (Splunk Inc.)** 28:48 Oh, it's a… yeah, so something like that, but this is only in one. Maybe we could do the same for all… Let's say, have it as a part of the template.
**Dan Gomez Blanco** 28:58 Ayyyy… Yeah, we could. I mean, like, if they're already, already reference implementations, we can link them, but if not, then we can add that.
**Lukasz Ciukaj (Splunk Inc.)** 29:08 Exactly.
**Dan Gomez Blanco** 29:09 Maybe one thing to do in yours is, like, add in… yeah, if you add that… You already have it.
**Lukasz Ciukaj (Splunk Inc.)** 29:15 I don't remember. I'm looking at this.
Do we have that in, how about the, the, your, your Blueprint? Dan, do you have it there?
**Dan Gomez Blanco** 29:25 The one that I wrote has already mentioned a couple of…
**Lukasz Ciukaj (Splunk Inc.)** 29:29 Oh, you have it. Okay.
**Dan Gomez Blanco** 29:32 Yeah, so there were… Actually, why is this not?
I've had mixed.
Oh, there wasn't… I was looking at the appendix. Yeah, so… Yeah.
The three that are there because they implement certain parts of it, right?
**Lukasz Ciukaj (Splunk Inc.)** 29:49 So I think we are good, so… but I don't know if that is part of the template, I would need to take a look.
It was funny.
**Dan Gomez Blanco** 29:57 Tiffany?
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 30:01 I don't think that we can depend on most end users being as proactive as AnkBank.
I do think that we will… if we want to continue to grow the reference implementation side of things, we will need to do outreach, and whether that's direct messages for the field folks among us who know these end users and could ask them to do that, or on social media. But, I agree, adding that message to the end of any Blueprints that don't have corresponding implementations is a good idea.
But if no one is looking at the blueprint, they don't know that we're asking for it, so… I would just say maybe as part of the ongoing project, We should be periodically reaching out and just saying.
Either on social media or in that blog post that talks about implementations that have been published. We just need to make sure that we're constantly asking for, new perspectives and implementations.
**Dan Gomez Blanco** 31:05 Agreed.
Yep.
Sounds good.
Yeah.
So… Again, you know, we cannot depend on them, so let's, Should we just close this issue, then? Because we have agreed on the ones that… We need from the current Blueprints.
That we've got, and then we can publicize that in some way.
Either through our prospective roles, or, in social media. But let's close this, then.
Awesome. I'll do that.
And now, the last thing we've got is… Well, we have… actually, we have still a couple of things that we need to… that we want to do before we close a project, right? Which is these… to reference implementations.
The Key Cloak one, that would be the fourth one.
in either Atlassian or… ACBANK.
And that would make Fife, which is what we said in the projects.
Dis- description.
**Lukasz Ciukaj (Splunk Inc.)** 32:14 Can we make it before KubeCon? I think it's a bit difficult, right?
I mean, Kikloak, it's… because it's already there, right? As part of the blog post, so it's only about converting it? Or it's not Keyclog?
**Dan Gomez Blanco** 32:28 KeyCloak is pretty much there, yeah, I think it's just…
**Lukasz Ciukaj (Splunk Inc.)** 32:30 Okay. Yeah.
**Dan Gomez Blanco** 32:33 It's gonna be merged. There's one, I don't know if we… I mean, maybe, but, like… I've not looked at it. So I don't know, if someone can review it.
**Johanna Öjeling** 32:44 I've made a first pass, and I saw they've already committed several times after my review, so I'll have to look at it again.
**Dan Gomez Blanco** 32:54 Awesome. And that PR is for the… Yeah, this is not for a blog post, right? They added directly to the docs.
**Johanna Öjeling** 33:01 Yes.
**Dan Gomez Blanco** 33:03 Cool.
I don't know if they were able to join this call, Hi, Abhi. Just checking, because, we talked before…
**Abhi** 33:23 Yes.
**Dan Gomez Blanco** 33:25 I just saw you join, by the way. It's not like I'm not calling you out for anything.
**Abhi** 33:29 I know she's…
**Dan Gomez Blanco** 33:30 Just, I don't know if you have… if you want to add any topics to the agenda, let me just share the…
**Abhi** 33:35 No, I was just, joining to listen, and I did reach out to you, Dan, to get involved with the Blueprint project, so this is my first time joining this meeting, so just trying to see where the project is, and… Where I can help out in the future.
**Dan Gomez Blanco** 33:49 Awesome.
Cool. Yeah, so let's see, I mean, if we… if we, if we manage to get them done before KubeCon, then we can publish the blog post around… I mean, if we… So, just to… to, to sum up here.
We have published 3 Blueprints. We are close to publishing 5 reference implementations. We have a process to contribute.
We have a template, and so on, basically everything that we put together in the proposal, right?
M… Now we are, yeah, we're at a point that we can close it off, and then to close it off, we mark the project as complete.
and then we were thinking that, and I know that Tiffany, the blog post, or the blog is very busy, but we were thinking of publishing something That just sort of, like, summarizes the project so far, and calls for more contributions, right? I guess. That would be the idea.
Emm…
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 34:57 I'm checking the calendar right now to see.
So, this week is pretty much completely booked up. Yeah.
Next week… We could do something on the 4th or the 6th.
of November.
**Dan Gomez Blanco** 35:21 Or, is there… so is there any, sort of, like, moratorium or anything like that during KubeCon?
Ian.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 35:31 N-no. I, I've… in fact, I've… so… Ideally, we only post two blog posts a week, Tuesdays and Thursdays, but in the run-up to KubeCon, we've done pretty much every weekday.
During KubeCon, I've gone back to just two, and both of those are not project updates, they're from outsiders, with the idea that most of the project folks are going to be focused on the conference itself.
Also, I'm going to be at the conference, and I'm the person who does most of the blog work in comms, so I was trying to make it lighter for my colleagues, who we'll have to cover in my absence.
That being said, if you really want it to go out during the conference, we can make that happen, too.
**Dan Gomez Blanco** 36:14 I'm personally… And Lukaszel, he, see your opinion on this. We can complete the project, close it.
Market has closed, if we, you know, if we get to those 5 reference implementations.
And then, go to KubeCore and do the presentation.
And then after that, we can publish a blog post with all these things after KubeCon.
And in that blog post, we can then… Include a summary of the Blueprints that were done, reference implementation, the process, ask for contributions, and we could even, like.
link to the… to the presentation at KubeCon.
to the recording, basically. And I think that would be a complete blog post.
**Lukasz Ciukaj (Splunk Inc.)** 36:59 Yeah, I mean, both works for me, either publishing it before KubeCon and, like, you know, promoting our session and trying to get more people registered, or posting it after KubeCon and putting the reference to the, to the recording of our session, right? So, so depends, I don't know, I'm okay with both.
And… I mean, I'll be on vacation from November 4th to November 8th, so shortly before KubeCon, so I can open PR, I have a draft for this already, but if there are some final touches needed, so someone needs to take over from me when I'm off.
**Abhi** 37:39 Do we get more, visibility through blog posts or through LinkedIn posts about such things?
Because if it's… if it's LinkedIn, then, what… what we… what Tiffany suggested that before, right, I think to answer that before the… before KubeCon, we could have a LinkedIn post for this, which would get visibility through that. And then as a follow-up, once KubeCon is done, then write a blog post Providing the summary, along with a link to the recorded video.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 38:11 Just to jump in here really quick, we tend not to get into the business of promoting specific sessions at KubeCons, because there are so many.
And so, if we do it for one, we have to do it for everybody.
There is a post out there that I actually just published last week. It has the entire schedule in it, so if you want to do your own promotion using that blog post as a… as a… The LinkedIn post announcing the blog post as the meat of your post.
go for it. If we post the Blueprints blog post before KubeCon, it can't be seen as a promotion of the session. Does that make sense?
**Dan Gomez Blanco** 39:00 Yeah, makes total sense. I think… I think what would make sense is… to do it after. I mean, I would prefer to do it after.
**Lukasz Ciukaj (Splunk Inc.)** 39:09 Okay, I'm okay with that, yeah, so let's do it after.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 39:14 Sorry, it's just… I have to think about scaling all of this, and if we…
**Lukasz Ciukaj (Splunk Inc.)** 39:18 Of course, yeah, thanks for, thanks for your, your…
**Dan Gomez Blanco** 39:21 I also think that, honestly, I think that having the link to the presentation, the link to the recording, is actually…
**Lukasz Ciukaj (Splunk Inc.)** 39:28 Yeah, you're right, you're right, because then the post will… people will be reading that for the next couple of months, and they can look into that, right? So there is a bigger value in looking into the link to the recording.
or the slide deck, then, like, this few days before the conference, where people can maybe get, and maybe a few of them who will read that will be actually at the KubeCon and can go to our session. So, I agree with you, there will be bigger value in having the link to the recording after the event. So yeah, let's do it. Let's publish it after the KubeCon, and I think that would be better.
**Dan Gomez Blanco** 40:00 There's also so much stuff being, like… Yep.
that people… the attention span of people before KubeCon is just not there, anyway, so, yeah.
**Lukasz Ciukaj (Splunk Inc.)** 40:09 Yep.
**Dan Gomez Blanco** 40:11 Cool, awesome. We talked about that.
Emm… We… Yeah, okay, so, I guess we… We have this… so this board is about to be closed, and then we've got this… Other board, which is… Basically has the… it tries to map to the… The proposals for either Blueprints or reference implementations.
Just trying to think.
Our reference implementation is here as well.
Or do we have a… Hmm.
Oh yeah, there we go. Revice implementation.
Mmm… Yeah, so basically, we can prioritize these.
So I think it would be good, that's what I wanted to do as well. We have a bunch of Blueprints proposals, some of them that were proposed by people that wanted to take on them.
And then, sort of, do it.
Themselves, with support from this group.
And some of them that are, yeah, and some of them… That were created during a blueprint to de-scope.
Some of the work.
And that needs someone to pick them up.
So, the first one, actually, that we got was this one for host infrastructure monitoring, So I don't know, I've not really had a look through… through each of them.
And if we took a look at Blueprints… Yeah, so… I know that some of them are already a bit more advanced, right?
for example, yeah, we're talking about the Prometheus metrics in non-Kubernetes environments. We already have that.
More advanced than others, right?
Maybe it's worth talking about that one.
Because these two here, this is why I put them at the top.
They already have some content that has been written.
Mmm… That's why I give them preference, basically.
Alolita's not here, but I know Alolita was, like, reviewing this one.
I think that was the last comment.
So let's just adding comments.
And this one… yeah, I… what's the status of this one? If we… If we… if anyone's got any info?
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 42:59 Uzo, I think that's yours. Do you have, any updates there?
Oh, I think she might be frozen?
**Dan Gomez Blanco** 43:11 Yeah, I think so.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 43:15 So I, I helped Uzo a bit in the creation of this,
**Dan Gomez Blanco** 43:26 Ash.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 43:27 I think we're looking for more input from, people with experience in this, But I'm not… I'm not 100% sure. It looks like she just, is trying to reconnect, so maybe she'll be able to speak to it more.
**Dan Gomez Blanco** 43:44 Cool.
That sounds great. I mean, I've not had a chance to read through this.
I guess the first question that was through here was, look, you had an initial look at it, and then… It was the intersection with… With the infrastructure and processes.
in non-Kit's environments, Blueprint, right?
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 44:09 And I do think this one will intersect with quite a few, because… at its heart, it's more about the Prometheus quirks of, of using both systems.
Yeah, maybe we can hit pause until Uzo joins again.
**Dan Gomez Blanco** 44:36 Yeah, makes sense.
It's a shame. She was there patiently.
I'm going through all the… Hello, y'all.
**Lukasz Ciukaj (Splunk Inc.)** 44:45 No doubt, but I think that what we need to do is have another round of reviews of all of these proposals, and, you know, provide some comments, because it's been a while, I had some… you know, time… I was a bit busy with other topics, so I didn't have the time to review and keep track what is new, what is updated, so I think I need to… Book some time for reviewing it and triaging where we are, which one we need to keep open, which one we should close, so we need to make some housekeeping for this, for sure.
**Dan Gomez Blanco** 45:18 Yep. One of the things that I think we should probably consider is, as well.
how do we… I mean, when we think about… Blueprints.
we think about the problems to solve, right? I think that's the first thing that we should be thinking about. What is the… What are the challenges to solve?
This is where we can… list the challenge, and I think that's something that the Clustered Observability Blueprint does.
It lists a challenge which is, related to managing, Collect… no, the self-observability of collector.
of collectors, basically.
But that's already covered in another blueprint, so it's still a challenge for that one, but it says, we're not covering this in this Blueprint because it's already covered somewhere else.
So if there is anything in this Blueprint that is already covered in another Blueprint, then, yeah, then we can just link out to that, right?
that's one aspect. For example, we're not talking about Kubernetes, so I'm assuming that anything we… the Kubernetes cluster observability doesn't really… touch much on the Kubernetes stuff in particular. It just says.
you can do that, you can scrape Kubernetes locally using a node, a node local receiver, or, like, a node local… Scraping on the… with a collector, right? With a demon set.
I don't… I don't know, I can't remember now if infrastructure and non-Kits environments have discovered much about Kubernetes.
But yeah, I think… one of the things I would say is that if we find, as well, this is my view on this, my personal view on this, if, let's say that, you know, we're now having a blueprint for Kubernetes, sorry, for Prometheus, ingested Prometheus at scale.
the core of that Blueprint, the challenges of that Blueprint, will be how to do Prometheus scale.
So if there is anything in here that is already mentioned in Prometheus, we have two options. Either we remove it from here, and we add it to the other Blueprint.
To the new one?
Or we… and then we link it from here to that one, and say, well, actually, you know, this Blueprint doesn't really focus on Kubernetes deeply. If you want to go to that one, this is already covered in that other one.
this is where I see it, is, like, what is the core of a blueprint here is not Prometheus, right? Even though it may be mentioned.
We just need to… Ensure that we keep Blueprints not growing arms and legs, right?
and link between them. That's my… that's my view on it.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 48:03 Perhaps we should start…
**Dan Gomez Blanco** 48:07 Gotcha, okay.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 48:08 You mean that visualization that we had talked about, whether it be a table or a chart, not… not published yet, but we should keep it somewhere in the repo so that we can start drawing these connections, so that we don't have to keep it all in our head all the time.
**Dan Gomez Blanco** 48:24 Yes.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 48:25 Okay.
**Dan Gomez Blanco** 48:26 That's a good point.
Yeah.
I will…
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 48:32 Or, sorry, just to explain for those who don't know what we're talking about here.
the vision for Blueprints was that they would be interconnected going forward, that there would be lots of overlap in different parts. And so, eventually, we would like to have, like, the landing page in this section of the docs draw those connections for users so that they can see, which ones might benefit them.
We haven't decided how… How to exactly visualize that yet, but, eventually we would like to draw those connections.
**Dan Gomez Blanco** 49:08 Yeah, I think.
**Abhi** 49:08 Maybe drawing a… like, kind of like a map, which… There's, right there, so… kind of like that, to draw mapping one-to-one. We… I was working on a similar blueprint at my company, where we have a reliability blueprint, which is, like.
There's a website, R9Y.tv, which helps you Correlate various areas, so we'd rather… Drew example from there, and then went ahead and… created a map of, like, flowcharts, so people can come in and understand where they are, and in direction that they want to go, so they can click on step service.
all, like, the map was generated all using AI, but we fed the data in, okay, this is where we… so we did initial work in Excel and, like, Word documents, and then fed it to AI to put it in a map.
So, I could… if there's already an issue for that, I can try looking into it, or if not, then I can create an issue and then start figuring out how do we… how can we create that mapping.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 50:16 I don't know if we have an issue for it, Dan.
**Dan Gomez Blanco** 50:19 as you said, a reminder for myself after today to create the issue. But if you want to create the issue, Abhi, go ahead.
Yeah.
**Abhi** 50:29 I'll go ahead and take that. I'll need some help on figuring out, like, what was your initial thoughts on that, because I'm just coming in now, so just help me with that, and then I can take it from there.
**Dan Gomez Blanco** 50:39 By the way, I did mention UML part… as a… partly as a joke. But UML does actually fit that overlap extend, you know, like, you know.
I don't know if it would be the clearest for people, but I think I do have some ideas when I do think about this, like… Annotating the, the, you know, the connections with the bits that… it extends, because it will be… it may extend more than one thing in each Blueprint.
So,
**Abhi** 51:08 But yeah.
**Dan Gomez Blanco** 51:08 If you create an issue in the end-user repo.
You apply this, you can apply this, this label,
**Abhi** 51:18 Alright, sounds good.
**Dan Gomez Blanco** 51:20 Either Blueprints, right? Basically, what we use is, like, we use the labels as there's a Blueprints label that is a reference implementation label.
And there's this one, which is general discussion about either-or, right?
Okay. So, yeah, you can label it.
**Abhi** 51:37 Sounds good. Thank you.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 51:39 Johanna, with your data analytics background, if you have any input on how to best present the information, I'd be curious if you have… you can just add it to the issue that Abhi creates, but…
**Johanna Öjeling** 51:52 Yeah, -oh, I was… Oh, I was thinking about it.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 51:56 Yeah, I totally just put you on the spot there.
**Dan Gomez Blanco** 52:00 I mean, I appreciate that. To me, everything is an architecture diagram, but maybe there's better ways of doing that.
Cool, cool.
A VIN diagram? No, sorry. I like Venn diagrams in general, but no. Okay, cool.
Anything else?
I think we've got 10 minutes left, but I'm not sure if there's anything else to share.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 52:26 I don't have anything to share, more of a question, Given time constraints, it would help me to… Okay, so KeyCloak will, will, be handled this week, and we can, get it transferred over to the docs as well.
for the Oc Bank… Is that where I should be focusing my, my, review?
Time next.
I guess, can we maybe just pick a few that I should focus on before we end the call?
**Dan Gomez Blanco** 52:59 I think the focus now should be on those two reference implementations, I think.
We don't really have anything… I think there's… these Blueprints still need some review.
From the… the scope, and the… Yeah, and the approach. So yeah, I think those… those… those two sounds good.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 53:20 Okay, that sounds good to me then.
**Abhi** 53:25 Is there a separate Slack channel for the Blueprint with End-Us, like… I was trying to find it, because I could only find… the end-users like the Slack channel, not for Blueprint.
**Dan Gomez Blanco** 53:38 Is that OTel… Dash Blueprints.
**Abhi** 53:42 Okay.
Thank you.
**Dan Gomez Blanco** 53:48 Awesome.
Today, and then today. So I'm just trying to think of the next meeting. Is it KubeCon?
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 54:00 I think so, yeah.
**Dan Gomez Blanco** 54:04 Yep, it is CubeCon.
Do we want to… I mean, most of us will be there.
And do we want to cancel that one?
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 54:16 Yeah, if…
**Dan Gomez Blanco** 54:17 Yep.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 54:18 If you have something that you need input on, just put it in Slack, I guess, and we can get to it async.
**Dan Gomez Blanco** 54:23 Yeah. We will try… I've not spoken to Rhys or Adriana as the community managers. There's normally, either in the Project Pavilion, I don't know if we're doing the observatory this year.
I guess that's… yeah, that stopped last year, and I guess… It was… it was fun while it lasted. But, the, we're doing the… the Project Pavilion then, I'm assuming. Something there.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 54:49 Yes, but just for one day. It's the last day, Thursday.
I don't know the, kiosk number yet.
But yes, it's Thursday from, I think, tend to…
**Dan Gomez Blanco** 55:02 Alright, so not a lot… not a lot of time for people to put their sessions up and…
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 55:06 No, and Reece said that there's actually not even a lot of space, so they're not even gonna do meeting time, like, slots.
**Dan Gomez Blanco** 55:15 I mean, one thing that we could do, I was thinking, I was thinking… Lukas and I, when we do the talk.
we can point people to somewhere, and I was thinking that the best place would be that, right? The Project Pavilion.
Stand.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 55:33 Yeah, and I figure once we get the lay of the land, literally, we can maybe post in Slack for, like, we found these picnic tables, and we're staking our claim to them, if you want to comment. Yeah.
Something like that, but yeah. I told Reese, OTel folks always find OTel folks, so I'm not… I'm not super worried about that. It's just, we don't have a dedicated space, so we can't advertise it yet.
**Dan Gomez Blanco** 56:00 Cool. Awesome.
Okay.
Well, if we don't see each other before, and I don't know if, Johanna, Abhi, if you're gonna be at… KubeCon?
**Johanna Öjeling** 56:11 No, unfortunately.
**Dan Gomez Blanco** 56:14 Okay, cool.
**Johanna Öjeling** 56:15 But I will watch the recordings.
**Abhi** 56:17 I'll, yeah, I'll watch the recording, I'll try to make it to the next one, next year. We have one.
conference policy per year, so I already got my quota with SRECON.
**Johanna Öjeling** 56:29 Hmm.
**Dan Gomez Blanco** 56:30 It's gonna say.
**Johanna Öjeling** 56:30 And…
**Dan Gomez Blanco** 56:31 Barcelona's not in a bad place.
**Johanna Öjeling** 56:34 I'd love to go there. So, Dan, you're giving one talk, or more?
**Dan Gomez Blanco** 56:39 Just one.
**Johanna Öjeling** 56:39 Yeah, cool. And Tiffany, are you giving any talk, or…
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 56:43 I am not… I had, some stuff go on earlier this year that meant I wasn't even really around when the CFP happened, so I did not… I did not get a talk submitted.
Or accepted, obviously. But, it's in Salt Lake City, which is, like, a hop, skip, and a jump for me, so…
**Johanna Öjeling** 57:01 Oh, Cool me.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 57:03 I'm gonna show up in… Have a good time. Listen to some good talks.
**Johanna Öjeling** 57:08 Yeah, have fun.
**Dan Gomez Blanco** 57:10 I mean, I attended, KCD UK, I think it was one of the only conferences that I attended in the last few years without giving any talk or anything like that. We didn't have a booth, we didn't have a… I didn't have any talks, I enjoyed it a lot.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 57:23 I think it's going to be… also, just because I've been kind of out of the community for a few months, it'll be nice to kind of… get in again. Nice.
**Dan Gomez Blanco** 57:32 Cool.
Alright, we'll see y'all.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 57:36 Bye.
**Dan Gomez Blanco** 57:37 Bye-bye.
**Johanna Öjeling** 57:37 Cheers.
