SIG: End-User SIG: OTel Blueprints
Date: 2026-08-31
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Lukasz Ciukaj (Splunk Inc.)** 00:55 Hey, Dan.
Good afternoon.
Can you hear me?
**Dan Gomez Blanco (New Relic, Inc.)** 01:07 Yep.
Well, it's interesting that the name is… yeah.
I see my name, I'm not sure if I configured that, but, because we're joining the new… Zoom links.
**Lukasz Ciukaj (Splunk Inc.)** 01:18 Yep, yep.
**Dan Gomez Blanco (New Relic, Inc.)** 01:19 There's the company affiliation in there, which is cool.
**Lukasz Ciukaj (Splunk Inc.)** 01:21 Oh yeah, indeed. There is mine, too. Interesting.
**Dan Gomez Blanco (New Relic, Inc.)** 01:24 I mean, I don't use Zoom at work anymore, so,
**Lukasz Ciukaj (Splunk Inc.)** 01:27 Yeah, I think there is this new, you know, portal they are tracking, the CNC, or Renos Foundation, they are tracking who is joining the calls, etc, for getting some statistics, so I think… or some analytics, so I think that's the reason I'm okay with that.
**Dan Gomez Blanco (New Relic, Inc.)** 01:43 Yeah, I think at the moment, I think at least that's only available to… so I do have access to that page for… And you can see that there, but I'm not sure they plan to make it public, as in, like, it's information that's useful for some OSPO, you know.
**Lukasz Ciukaj (Splunk Inc.)** 01:58 Yep.
**Dan Gomez Blanco (New Relic, Inc.)** 01:59 To the open source office in each company to know, you know, How people are.
I guess, joining the meetings and so on, but yeah.
**Lukasz Ciukaj (Splunk Inc.)** 02:08 That's true. How was your trip to U.S, North Carolina? Did you like it? Was it the first time for you in North Carolina?
**Dan Gomez Blanco (New Relic, Inc.)** 02:15 It was the first time in North Carolina, yeah. It was humid.
I think it was just before the storm, yeah.
**Lukasz Ciukaj (Splunk Inc.)** 02:23 Where were you? Which place?
**Dan Gomez Blanco (New Relic, Inc.)** 02:25 It was around, like, Raleigh.
**Lukasz Ciukaj (Splunk Inc.)** 02:27 Oh yeah, so that's what I need.
**Dan Gomez Blanco (New Relic, Inc.)** 02:30 Oh, cool. I didn't know that.
**Lukasz Ciukaj (Splunk Inc.)** 02:32 underneath on the subject.
**Dan Gomez Blanco (New Relic, Inc.)** 02:33 Not that I had much time, I was there for, like, only two days and flew back, so…
**Lukasz Ciukaj (Splunk Inc.)** 02:36 And even on the suburbs of Raleigh, there is a little town called Apex.
Oh, so there's, like, Raleigh and there is… Raleigh is, like, donuts, so there is, like, you know, this main city and the small towns around, and I live in one of them.
**Dan Gomez Blanco (New Relic, Inc.)** 02:50 Oh, cool.
Good stuff.
Right.
I guess let's wait for another minute, and then we can cut.
**Lukasz Ciukaj (Splunk Inc.)** 03:00 enough.
**Dan Gomez Blanco (New Relic, Inc.)** 03:01 Yeah.
**Lukasz Ciukaj (Splunk Inc.)** 03:04 I don't know what is happening, to be honest, with…
**Dan Gomez Blanco (New Relic, Inc.)** 03:07 Yeah, from my perspective, I was just… yeah, so, I was just gonna say that, yeah, let's have a look at the board.
**Lukasz Ciukaj (Splunk Inc.)** 03:15 And just go back.
**Dan Gomez Blanco (New Relic, Inc.)** 03:16 Back to the, you know, one of the things I would definitely like to do is… Try to see where we are.
And by the way, I should probably say, I have, Yeah, I guess I have been on a holiday.
And, and also business travel for a bit, so,
**Lukasz Ciukaj (Splunk Inc.)** 03:34 Same here. I was 3 weeks off, so I'm still, you know, catching up, but yeah, I agree, let's try to look at the board and see where the things are. I know that we have one blueprint that Alex is working on, and I believe you were, like, providing some comments. I need to renew there as well.
**Dan Gomez Blanco (New Relic, Inc.)** 03:54 Yeah, let me just create the agenda for…
**Lukasz Ciukaj (Splunk Inc.)** 04:00 And I don't remember what's the status of that PRs that I submitted. One of them was approved in End-UserSeek, but I don't know about the docs, the OpenTelemetry.io.
**Dan Gomez Blanco (New Relic, Inc.)** 04:11 Have a look at that as well.
What day is it today? Is it 20… no, 31st.
I'm just go- I'm just adding some… Topics to the agenda for today.
**Lukasz Ciukaj (Splunk Inc.)** 04:52 Sure.
Still…
**Dan Gomez Blanco (New Relic, Inc.)** 05:31 Right, okay, so, let's, let me share my screen.
Everything that we work on should be on that, bored, right? Okay, so, So yeah, one of the things that I would like to discuss is, yeah, so we talked about that.
Before we all went on holiday.
Which is that, we want to be able to close this project at some point, right?
this would be a good practice from the perspective of, like, you know, the community. We have basically started with.
Blueprints as a project, and the project was, like, to deliver three, and then, you know, set the framework, have a tried and tested way of doing Blueprints and reference architectures.
We are… we have delivered quite a bunch of work. We now have, basically.
the… this is where we are now, right? Blueprints for Kubernet observability, And we have the…
**Lukasz Ciukaj (Splunk Inc.)** 06:41 That's mine.
**Dan Gomez Blanco (New Relic, Inc.)** 06:43 Yours.
**Lukasz Ciukaj (Splunk Inc.)** 06:44 Yep.
**Dan Gomez Blanco (New Relic, Inc.)** 06:44 Let's start with this one, because I, you know, I wanted to ask, yeah, where we are here. Right, so there… did you link the PRs? Yeah, okay, so there…
**Lukasz Ciukaj (Splunk Inc.)** 06:52 Yeah.
**Dan Gomez Blanco (New Relic, Inc.)** 06:53 So this one has been merged.
**Lukasz Ciukaj (Splunk Inc.)** 06:56 Labels are created.
And this one is another PR, but this is in documentation, like Opentelemetry.io, to add one more banner there. And the… I think… There is some issue with this… I remember before holiday, I tried, you know, to fix that. I believe you provided some…
**Dan Gomez Blanco (New Relic, Inc.)** 07:18 Yep.
**Lukasz Ciukaj (Splunk Inc.)** 07:19 Some comment above, if you scroll a little bit up.
yeah, there is this niche cache, or I don't know how to… how to pronounce it, but… I had some issues with that, so I removed this, because I thought this is, like, automatically created by, you know, CAD, but it seems that I need to…
**Dan Gomez Blanco (New Relic, Inc.)** 07:40 This one.
**Lukasz Ciukaj (Splunk Inc.)** 07:41 Yep.
So that's the only missing thing here.
So I bring it back. I don't know how to do it, to be honest, but I think…
**Dan Gomez Blanco (New Relic, Inc.)** 07:54 I mean, sometimes you can fight with Git, but, like, sometimes it's just… for this, such a small change, right? That might be a good idea to, like, just reset… reset your branch to… Exactly. …to the, to the… to the head, and then, yeah, start again.
**Lukasz Ciukaj (Splunk Inc.)** 08:10 I'm thinking about, like, maybe, like, you know, merging it with head, and then… or resetting it to head, and starting from scratch.
That's what I'm planning to do. But yeah, this is the only missing piece, and I think if I fix this, then we can ping the SEC and ask them forging. It's a small piece.
**Dan Gomez Blanco (New Relic, Inc.)** 08:31 Yeah, I think… did I approve? Yeah, I approved. So, Yeah, let's do that, and then we can get set.
**Lukasz Ciukaj (Splunk Inc.)** 08:38 I will prioritize it this week. Again, it's a small change, so I think we should… we should have it done.
**Dan Gomez Blanco (New Relic, Inc.)** 08:44 Awesome. What I will try to do this week, as well is, and I was starting to work on this, actually, I'll put it in progress.
Yeah, so there's one that is related to taking out some of the advice, some of the more, like.
Best practice advice that is in the template.
And then put it into a dock for Blueprints and reference implementations.
So, yeah. Again, you know, not a big thing.
And then we have this one… okay, so… It would be good to do a bit of a review, and I'm happy to, you know.
to do that of, well, actually, I should mention two things before I say that. We're basically, like, getting to the point where if we… if we… I guess… Fix these things.
Or, sorry, if we deliver these things, we'll just be able to call the project complete. And what we call by complete is that we have a, as I said, tried and tested workflow to do things.
one of the things… I will cancel this… let's cancel that now. So we, sorry, the DevEx SIG… have now… This is when we need to change a little bit of the scope of this project, right? Because the DevEx SIG Have already got 5… Yeah, so there's Skyscanner, Mastodon, Adobe, already published for reference implementations. There are two more that are in progress, and maybe already… I've not really been keeping track of the blog.
But I don't think they have been merged, but they are already working on 2 more. So that means that our project's OTel Blueprints will do 5 reference implementations.
And then we said, well, let's piggyback on that work, right? We already… we already have 5 reference implementations after DevEx, SIG do theirs, and what I was thinking of is, instead of, like.
Instead of, us writing more reference implementations as part of this work, what would be important is to take all the different blog posts that they created.
And then… Mmm… Adapt the template, the reference architecture template.
To that. To basically to make sure that it…
**Lukasz Ciukaj (Splunk Inc.)** 11:16 But what? And then publish it again, or what?
**Dan Gomez Blanco (New Relic, Inc.)** 11:20 No, no, no, we wouldn't be touching the coverage reference implementations, but more like, you know, ensuring that the reference implementation template that we've got that covers the stuff that was already published.
**Lukasz Ciukaj (Splunk Inc.)** 11:30 I don't.
**Dan Gomez Blanco (New Relic, Inc.)** 11:31 also the view that we want to, you know, the structure that we want to give it, but also that we get feedback from the DevEx SIG maintainers that have done that, right? The end goal is basically to have that reference implementation template that is Approved.
**Lukasz Ciukaj (Splunk Inc.)** 11:51 Yeah, that's something, you know, I'm confused still about this DevEx, because I believe that's something they do in parallel now, right?
**Dan Gomez Blanco (New Relic, Inc.)** 11:58 Well, the thing is, it's not like they're continuously doing it, I did check with them, is they did all these interviews.
last year, or the year before, I think it was 2025, they did all these interviews. They just needed to write the blog post, and it's taken a while, right?
**Lukasz Ciukaj (Splunk Inc.)** 12:16 Oh, bad.
**Dan Gomez Blanco (New Relic, Inc.)** 12:16 So, because the interviews were already done.
we were not… you know, it didn't make sense to not write them, right, as blog posts. Yeah. I did ask them to try to follow the template, and I think, you know, it was… Yeah, maybe, like…
**Lukasz Ciukaj (Splunk Inc.)** 12:32 Yeah, I mean, for future, I think it would be great to sync with them and tell, okay, if you guys plan to write another, like, seminar blog post or something, so you can attach to Blueprint or reference implementation process.
And follow it, right? We are happy to support you with this, but we would like this to be part of our initiative, right? Don't… there is no need, you know, to have two seminar initiatives in parallel, right?
**Dan Gomez Blanco (New Relic, Inc.)** 12:56 Exactly, I mean, that's understood. That's all understood, as in, like, the,
**Lukasz Ciukaj (Splunk Inc.)** 13:00 But it's not, like, super urgent, but let's keep it in mind that once we close this project, maybe we can sync, we can join their SIQ, maybe, and explain the process.
how it works, and if there is any, like, plan to work on something similar for other customers, let's go through these reference implementations, because we have a process, we have resources dedicated to that.
**Dan Gomez Blanco (New Relic, Inc.)** 13:22 Yep.
But I will add that here, I'll just add it now, so I don't forget. Remember, review the… Published.
I don't blame.
Actually, there's a need for revenue.
**Lukasz Ciukaj (Splunk Inc.)** 14:12 I would change the label.
Blueprints slash reference implementation. So that's a general, as you may remember, so… This is more for the review process, but the one… this is the, like, general, okay?
Sorry, I'm picky, but I'll throw that, so I know by heart how it works.
But yeah, I agree. Let's do it, and we can put it here. What do you think? What is the… possible deadline of closing this project, like, end of September, can we make it this month? I think we should do it.
**Dan Gomez Blanco (New Relic, Inc.)** 14:48 Yeah, I think… I think we… I would like to aim for that. I need to check with Alex.
**Lukasz Ciukaj (Splunk Inc.)** 14:52 You know what?
**Dan Gomez Blanco (New Relic, Inc.)** 14:53 is happy with… with that, if he's underwater as well, and if he's, like, you know, not got any bandwidth, I am… I'm gonna have some bandwidth in September to… to have a look at this, or… or I can get… actually, there are other folks that… that work with me that I could ask to contribute, if that's the case, right? But, Yeah, let's have a chat with… check with Alex.
I was just reviewing the current blueprint.
there are a few things that I think I would like to… I know that it has been, like.
A little bit of, like… and this… this is… This is normal in OpenTelemetry, right? We're, like, we're in any open source projects, where, like, sometimes review cycles… are not.
Super efficient, because.
well, I have some bandwidth now, and then I won't have bandwidth for, like, a week, and the other person maybe has bandwidth in a week, but not now, so, like, you know, it's, Image.
**Lukasz Ciukaj (Splunk Inc.)** 15:53 We're missing a time where people can actually work together efficiently, right?
**Dan Gomez Blanco (New Relic, Inc.)** 15:57 Yeah.
Yeah.
Also, like, you know, let's this… sorry, let me, finish this.
Alright.
Yes, so, cool. I will… so, just so I remember, there's one… You are working on this one.
Ehh… I'll be working on this one.
Cool.
**Lukasz Ciukaj (Splunk Inc.)** 17:01 This is for their blog post, right?
**Dan Gomez Blanco (New Relic, Inc.)** 17:04 So the blog… so yeah, so the blog post… no, this is not for the blog post, this is for… we talked about having… M… a better… so this is… this was someone, like, raised by Aulita, but, like… I'm… yeah, I've created the ticket. That ends.
**Lukasz Ciukaj (Splunk Inc.)** 17:20 Okay, markdown comments, gotcha.
**Dan Gomez Blanco (New Relic, Inc.)** 17:23 Yeah, so is the stuff that we have currently… in here…
**Lukasz Ciukaj (Splunk Inc.)** 17:28 Cause there's… yeah…
**Dan Gomez Blanco (New Relic, Inc.)** 17:30 So in the template, if you go to the raw thing, there is a bunch, a lot of text. Maybe… maybe not. Yeah, there.
Cool.
Come on.
Right. So you go to the raw text, there's all this stuff here, right, which is, like, hidden, because they're comments.
The idea is to take that out of here, and basically have some best practice outside of this, and let's just keep the template With the stuff that is in comments, right?
Just basically, like… Fairly simple, take the cobbins out.
For the blog post, I think we can start on it.
But I think… I think I would… Yeah, we can start on the blog post. If you want to create an issue for it, I'm just thinking.
**Lukasz Ciukaj (Splunk Inc.)** 18:26 I'm not.
**Dan Gomez Blanco (New Relic, Inc.)** 18:27 My only concern was that we haven't really got the reference architecture template You know, fully, let's say, reviewed and approved.
And then we still have one… one, observability Blueprint, That is in the… That is in the works, from the project. What I wanted to basically avoid is that we start to work on a lot of other stuff.
And the stuff that is needed to close the initial deliverables for the project is not prioritized, right?
**Lukasz Ciukaj (Splunk Inc.)** 18:59 Yeah, I agree. I mean, my opinion, the goal is we need to regain momentum, because we lost a bit of momentum in terms of Blueprints, right? There was a little bit of, you know, noise around this when we started. There was a blog post, there was the… you were in the… you had an interview with Dotan, right? The one that was published.
So it was a good time, so we got a couple of, you know, issues open, proposals, and then, again, we, like, because of the summertime, and we were busy, we lost a bit of momentum, so I think we should try to regain it, so we can either… I mean, we have our session at KubeCon, this is huge, right?
**Dan Gomez Blanco (New Relic, Inc.)** 19:35 That's what I was thinking. It might be a good idea to, let's say… Published a blog post around… End of September… first, you know, early October, that's normally when people will start to put their… put their, you know, the schedule.
**Lukasz Ciukaj (Splunk Inc.)** 19:55 Yep.
**Dan Gomez Blanco (New Relic, Inc.)** 19:56 place for KubeCon, and then we can say, you know, come and see the… They talk, we can explain what Blueprints are, and blah blah blah.
And then we, we cover the current state.
And then…
**Lukasz Ciukaj (Splunk Inc.)** 20:09 There are some other channels as well. There is this What's New in OTel series, and others, so we can maybe try to get somewhere and maybe get a little bit.
**Dan Gomez Blanco (New Relic, Inc.)** 20:19 I think what, yeah, I think it's…
**Lukasz Ciukaj (Splunk Inc.)** 20:21 Oh, yeah.
**Dan Gomez Blanco (New Relic, Inc.)** 20:21 From what's new in OTel? Again, you know, I would probably say… After we close the projects, we… and we say… we call it… not stable, you know, we call it stable in a way. We call it, hey, you know, we've been doing this, we think it's ready to scale, let's do it. Yep. Is when we do that type of stuff. So yeah, I think that would be… So yeah, what's new in OTel? That would be a good place to advertise it. Kubecon, blog post.
Now, what we need to have a strategy is for how we are going to… Prioritize things, right?
Ultimately, We're gonna be asking for… reviews on… The… we need to have a good… Maybe we do it from the perspective of a board, right? For things that are, like… We need to have a list of priorities in terms of what Blueprints we're gonna tackle next. Otherwise, people will get, like, very… I guess, dissolution with it, if they say, hey, I've got a blueprint, I'm ready to write it, but, like.
I have no one to review it.
**Lukasz Ciukaj (Splunk Inc.)** 21:25 What do you mean?
**Dan Gomez Blanco (New Relic, Inc.)** 21:27 So yeah, I think that's… that's one of… that's probably…
**Lukasz Ciukaj (Splunk Inc.)** 21:29 Depends on how many proposals will be, you know, submitted, and how many, let's say, the active Blueprints will be there. I mean, if there is 3, then we are fine, but if there is 15, then there is a problem, right? Because I agree with you, we need to prioritize, so… Yeah, let's see how it works.
**Dan Gomez Blanco (New Relic, Inc.)** 21:51 I'm gonna rename this.
I think we… we don't have anything else to discuss, I think, so we can do this now.
**Lukasz Ciukaj (Splunk Inc.)** 21:58 Hey, good.
**Dan Gomez Blanco (New Relic, Inc.)** 22:00 Well, actually, there's one extra thing, too.
Let's just call it Bootstrap.
Either quote, I had a word.
**Lukasz Ciukaj (Splunk Inc.)** 22:12 Stop.
**Dan Gomez Blanco (New Relic, Inc.)** 22:13 M… So yeah, so this project here is only for bootstrapping, right? But why don't we create a new one?
Mmm…
**Lukasz Ciukaj (Splunk Inc.)** 22:25 I'm skating.
**Dan Gomez Blanco (New Relic, Inc.)** 22:26 Yeah.
By the way, the only other thing that is to discuss is the Kubernetes Blueprint.
**Lukasz Ciukaj (Splunk Inc.)** 22:32 Hmm.
**Dan Gomez Blanco (New Relic, Inc.)** 22:33 Doing a review.
**Lukasz Ciukaj (Splunk Inc.)** 22:34 Do you need any help with that from me? Like, do you want me to review it and provide some comments as well?
**Dan Gomez Blanco (New Relic, Inc.)** 22:41 I'm mid-reviewed, so if you want to, like, you know, chime in after…
**Lukasz Ciukaj (Splunk Inc.)** 22:45 I can double check, yep. I will take a look if there is anything missing, maybe something I noticed.
**Dan Gomez Blanco (New Relic, Inc.)** 22:51 Oops.
Right, so what we can do now, because we've got some time, is, and I need to drop a quarter or two, 20 minutes?
Let's go and create a project here.
**Lukasz Ciukaj (Splunk Inc.)** 23:09 Okay, that's End-U- as part of End-User, okay.
**Dan Gomez Blanco (New Relic, Inc.)** 23:12 So, let's call it a Kanban… Yeah, then we want to make it… Kanban.
Do not import issues yet.
It's not important yet.
This would be… Cool.
**Lukasz Ciukaj (Splunk Inc.)** 23:44 Cool.
Do you want to put, let's say.
something in the name that could differentiate from bootstrapping, you know what I mean? Like, someone looks there to not be confused.
**Dan Gomez Blanco (New Relic, Inc.)** 23:58 Yay.
Fair enough.
**Lukasz Ciukaj (Splunk Inc.)** 24:04 Okay. Or why not to… okay.
**Dan Gomez Blanco (New Relic, Inc.)** 24:08 I'm going.
Or…
**Lukasz Ciukaj (Splunk Inc.)** 24:15 maybe… sorry, I'm too picky sometimes, you know, and pedantic, but maybe, let's call it the same, like, this one, if you copy Blueprints and reference implementations, or OTel, let's start with OTel Blueprints and reference implementations, that I would suggest at the beginning, OTel.
And copy that, and update the… okay, here you can, in brackets, you can put, like, scale.
or Phase 1? I don't know.
**Dan Gomez Blanco (New Relic, Inc.)** 24:44 No, this… I mean, but this would be, like, forever, right? This is, like, the one.
**Lukasz Ciukaj (Splunk Inc.)** 24:48 Okay.
**Dan Gomez Blanco (New Relic, Inc.)** 24:48 Prioritize.
**Lukasz Ciukaj (Splunk Inc.)** 24:50 I know what you mean, like, okay. So ongoing, ongoing is good, I think we can dip ongoing.
**Dan Gomez Blanco (New Relic, Inc.)** 24:56 Sweet.
**Lukasz Ciukaj (Splunk Inc.)** 24:57 And the same name for the other one, but we can put, in the brackets, bootstrap, right? And then we should be good. And we have, like, two similar, let's say, twin projects, but one is for bootstrapping, one is for… that's what I would suggest.
People are not confused.
Yep, okay, now we should be good. Sorry, that was fine. That's okay.
**Dan Gomez Blanco (New Relic, Inc.)** 25:19 That's fine. Right, let's first do this so I'm not the only one that has access to this.
M… Admin role.
Right, okay, so… If you remind me of the blue… we had some different status, you know, status that we… That we had for each of the Blueprints, right?
**Lukasz Ciukaj (Splunk Inc.)** 25:51 Yeah. Mmm… I need to open, I don't remember by heart. So, end-user labels, it was explained somewhere.
We have document for that, give me a sec, seek end-users, but not labels, ish, blah blah blah, code… Architecture, blueprint… oh yeah, here, there.
So… We have… needs auto, needs review, in review, and approved. So we have… Four states.
**Dan Gomez Blanco (New Relic, Inc.)** 26:31 Alright.
needs author.
**Lukasz Ciukaj (Splunk Inc.)** 26:35 You know?
You know, some of them are… hmm… maybe two labels at the same time, like, needs outdoor and mini review, you know what I mean.
**Dan Gomez Blanco (New Relic, Inc.)** 26:51 So, when it got through, like, Oh, wait a second.
**Lukasz Ciukaj (Splunk Inc.)** 26:55 But these pages must match the label name, or not?
I think it can, right? Because if… It's gonna automatically be assigned.
**Dan Gomez Blanco (New Relic, Inc.)** 27:05 Need to get my charger.
**Lukasz Ciukaj (Splunk Inc.)** 27:06 Sure.
No, I think we just need free.
stages here. Needs review, in-review, and approved.
**Dan Gomez Blanco (New Relic, Inc.)** 27:39 Okay.
So back. So what do you say? We need 3 only?
**Lukasz Ciukaj (Splunk Inc.)** 27:44 Free. Needs review, in-review, and approved.
**Dan Gomez Blanco (New Relic, Inc.)** 27:48 And what about needs author? Is that not, like, a state of it, or…
**Lukasz Ciukaj (Splunk Inc.)** 27:52 Oh yeah, it could be, okay. So, yeah, we can…
**Dan Gomez Blanco (New Relic, Inc.)** 27:55 Let me see if we go back to the… I guess.
**Lukasz Ciukaj (Splunk Inc.)** 27:58 I just shared the link with the place where the labels are explained. You can take it in the chat.
Oh yeah, this is the one.
So…
**Dan Gomez Blanco (New Relic, Inc.)** 28:08 Right, so we've got labels at revenue… okay, so it needs… that's a status, right?
**Lukasz Ciukaj (Splunk Inc.)** 28:12 That is amazing. Oh, yeah. So, yeah, let's make 4.
**Dan Gomez Blanco (New Relic, Inc.)** 28:17 Proposal is ready, I'm waiting for the Blueprints team to review.
I'm, actively reviewing. Yeah, okay, that's…
**Lukasz Ciukaj (Splunk Inc.)** 28:25 Yeah, let's make 4.
**Dan Gomez Blanco (New Relic, Inc.)** 28:28 We can change that later. Okay, so needs author…
**Lukasz Ciukaj (Splunk Inc.)** 28:32 Need to review.
**Dan Gomez Blanco (New Relic, Inc.)** 28:33 Meetings with you.
**Lukasz Ciukaj (Splunk Inc.)** 28:42 In review.
**Dan Gomez Blanco (New Relic, Inc.)** 28:44 That's already, yeah.
**Lukasz Ciukaj (Splunk Inc.)** 28:46 And the last one is approved.
Or done.
**Dan Gomez Blanco (New Relic, Inc.)** 28:51 Got it approved.
**Lukasz Ciukaj (Splunk Inc.)** 28:52 So we have a matching with the labels, I agree.
Perfect.
So what about the backlog? Should we keep it backlog here? I think we can, right?
**Dan Gomez Blanco (New Relic, Inc.)** 29:06 I'm just thinking, like, the reason why I would like to keep backlog is that… We can add things… Let's just remove some of these fields that we don't really need an estimate.
Priority…
**Lukasz Ciukaj (Splunk Inc.)** 29:23 Priority is okay, we can live.
**Dan Gomez Blanco (New Relic, Inc.)** 29:26 Size…
**Lukasz Ciukaj (Splunk Inc.)** 29:27 No.
**Dan Gomez Blanco (New Relic, Inc.)** 29:30 Let's not do that. And start date… Mmm, target date? I don't think we need it.
I have, like, target dates that'll be out.
**Lukasz Ciukaj (Splunk Inc.)** 29:40 Right, okay.
**Dan Gomez Blanco (New Relic, Inc.)** 29:40 So, one thing we can do is basically say.
One item is added in the project.
It has some issues, had to have issues with the project, that's fine.
When the status is updated to Approved.
It closes the issue. No, it shouldn't. So I guess that is… that's one of the things that we want to make sure that we get right. So these are four issues, right? So we've got approved.
and then the PR is… and then there's, like…
**Lukasz Ciukaj (Splunk Inc.)** 30:14 Oh yeah, I know what you mean. Because it's approved on our side, on End-User, but it's not yet finished on the OpenTelemetry.io, on the docs, right?
**Dan Gomez Blanco (New Relic, Inc.)** 30:23 Yeah, so I guess what we want to say here, if we were to put this in a Kanban type of… thing.
**Lukasz Ciukaj (Splunk Inc.)** 30:29 We could add one more status, I think, here. Approved, and then… The last… the next stage would be…
**Dan Gomez Blanco (New Relic, Inc.)** 30:45 Right, so we have backlog, goes in.
It hasn't been tri… it hasn't been… triage yet, maybe that's when… But…
**Lukasz Ciukaj (Splunk Inc.)** 30:56 Resistant…
**Dan Gomez Blanco (New Relic, Inc.)** 30:58 There you go, needs author, waiting for author to write the blueprint.
Needs review, needs review from approvers, in review.
Then it's approved as not the work has completed, it's approved as… This work has been,
**Lukasz Ciukaj (Splunk Inc.)** 31:20 for opening PR in OpenTelemetry.ai.
Or, again, documentation, for example.
**Dan Gomez Blanco (New Relic, Inc.)** 31:28 And then we'll have the, I guess… Deliver it? Or…
**Lukasz Ciukaj (Splunk Inc.)** 31:35 Published?
**Dan Gomez Blanco (New Relic, Inc.)** 31:36 Published.
**Lukasz Ciukaj (Splunk Inc.)** 31:37 Published, yeah, I like it. Published.
You have a typo there.
**Dan Gomez Blanco (New Relic, Inc.)** 31:45 Nope.
the lift, and then… Yeah.
**Lukasz Ciukaj (Splunk Inc.)** 31:49 Yeah, I think there is no need for having, like, additional statuses, like, in progress, or… no, let's… let's make it simple.
**Dan Gomez Blanco (New Relic, Inc.)** 31:58 Yeah, they make it simple so that, you know, yeah.
if it's, you know, if it's approved, it's been approved from our perspective, and we know what that means, right? Yep. Which is… yeah.
Maybe… this is one thing, though.
Approved.
I just wonder if, like… from the perspective of the issue triage process, approved is completely fine. I'm just thinking here is, like, if we need to say.
Instead of in review, we say… Something like… Triage and review, or something like that, right?
Mmm… People, if people come here and say, and see that it's in review, they see that the Blueprint itself is in review.
And approved as a saying, like, you know, basically saying, like.
If we were to change these columns to… to something else. Like, for example, we start with… needs author is good, because there's a status of the issue, but also the blueprint. It hasn't started writing the blueprint.
needs review, I would almost say, like, is like… Proposal needs review.
Because… There's a review for, like, the proposal itself needs review, not the blueprint, right?
**Lukasz Ciukaj (Splunk Inc.)** 33:13 Yeah.
**Dan Gomez Blanco (New Relic, Inc.)** 33:16 Proposal and review.
Oh, no, that's cool.
**Lukasz Ciukaj (Splunk Inc.)** 33:32 Propona approved, yeah.
**Dan Gomez Blanco (New Relic, Inc.)** 33:38 And then… Yeah, just published.
Right. That makes sense to me. Now, what we can do is go to the workflows, and we say, auto-close the issue.
Let's edit this. When it goes into published.
Then we close the issue.
Mmm… Right, so when an item is added to the project.
We're only adding issues. We're not adding the PRs here.
Maybe we want to add the PR into it as well, manually.
Let's start with the issues for now.
When an issue is added to the project.
It will go into the backlog.
Fine.
M.
And then auto-add to the project. This is the bit that goes with it. Issues in the SIG End-User Repo.
I have a label… Emm… Reference implementations… Label… Blueprints.
So those are the two labels that we use, too.
So when an issue… and those will be the ones that…
**Lukasz Ciukaj (Splunk Inc.)** 34:57 OR or AND, in this case.
**Dan Gomez Blanco (New Relic, Inc.)** 34:59 Those are OR, basically, I think.
I believe.
Wait a sec, maybe not.
Because they should be.
There's an issue, and it's open.
Right, so these match.
But if I add… no, I think it's, I think it's actually add.
I've had a comment.
Cool, alright.
That is… I needed a comma, not like the other one is mapped.
Right.
Okay, so that will added to it.
And then I think that we can probably move the… I don't know if you can add automation here to say… Put request is linked to the issue.
When a PUT request is linked to an issue, Then it goes into… Let's just… just… let's just not have this…
**Lukasz Ciukaj (Splunk Inc.)** 36:14 No, no, no.
This is not… How are I just not valuing this.
**Dan Gomez Blanco (New Relic, Inc.)** 36:19 And when the item is closed, When the issue is closed.
Set the value to… Published.
Mmm…
**Lukasz Ciukaj (Splunk Inc.)** 36:30 It is. Sometimes we can… can you go to item closed?
Because this means what? That if we close the issue, Then…
**Dan Gomez Blanco (New Relic, Inc.)** 36:41 Then it will go to the… to the column, to the publish column.
**Lukasz Ciukaj (Splunk Inc.)** 36:45 Is it always the truth? Sometimes you can close the issue because we don't like the proposal, but it's not published, right?
**Dan Gomez Blanco (New Relic, Inc.)** 36:51 Good point.
**Lukasz Ciukaj (Splunk Inc.)** 36:53 So…
**Dan Gomez Blanco (New Relic, Inc.)** 36:54 Maybe we should just…
**Lukasz Ciukaj (Splunk Inc.)** 36:56 We should have one more… we should have one more, category then. I don't want to overcomplicate, but… Let's just…
**Dan Gomez Blanco (New Relic, Inc.)** 37:03 Why don't we just disable this one?
**Lukasz Ciukaj (Splunk Inc.)** 37:05 Yeah.
**Dan Gomez Blanco (New Relic, Inc.)** 37:06 We just manage it, yeah.
**Lukasz Ciukaj (Splunk Inc.)** 37:07 What if there is some… there should be something like, you know, black hole, or archive, or something, where we could put all of the issues that… They didn't move forward through the process.
**Dan Gomez Blanco (New Relic, Inc.)** 37:22 Yeah, that's a good point. But they're not published.
**Lukasz Ciukaj (Splunk Inc.)** 37:25 They are not published.
**Dan Gomez Blanco (New Relic, Inc.)** 37:28 But they're not being… yeah, that's a good point. We should have a status in there.
**Lukasz Ciukaj (Splunk Inc.)** 37:33 Yeah, we have lots of stages, but I think that… that could be needed. Here, it's out, or needs…
**Dan Gomez Blanco (New Relic, Inc.)** 37:39 Start a new one then, and we call it, unplanned. That's what…
**Lukasz Ciukaj (Splunk Inc.)** 37:47 Politically correct.
**Dan Gomez Blanco (New Relic, Inc.)** 37:49 Yeah, that's what GitHub uses.
**Lukasz Ciukaj (Splunk Inc.)** 37:52 Damn.
I'm not saying that your proposal is bad, or we don't like it, it's just on planets.
**Dan Gomez Blanco (New Relic, Inc.)** 38:04 Unplanned, yeah. Okay, that makes sense. And I think what we can do now is… Add some items here.
Hmm.
**Lukasz Ciukaj (Splunk Inc.)** 38:22 You know, I think we should automate it even more, like, to pick up some, you know, the labels that we already have, because I assigned them, like, in review.
**Dan Gomez Blanco (New Relic, Inc.)** 38:31 Yeah, that's what I was thinking. I'm not sure if it can be done, but, like…
**Lukasz Ciukaj (Splunk Inc.)** 38:35 Some of them are, like you see, there are double… labels, like, in review, needs out, or… So, I don't know if we need to have dedicated Mmm… Because if it's in review.
I think we could remove the needs outdoors stage here.
It's not providing any additional value, in my opinion.
**Dan Gomez Blanco (New Relic, Inc.)** 39:10 I don't know, I think, imagine, like, you come here, and this is what we publicize.
**Lukasz Ciukaj (Splunk Inc.)** 39:13 Hmm.
**Dan Gomez Blanco (New Relic, Inc.)** 39:14 You say… well, this one, for example, is…
**Lukasz Ciukaj (Splunk Inc.)** 39:18 This one is…
**Dan Gomez Blanco (New Relic, Inc.)** 39:20 approved.
**Lukasz Ciukaj (Splunk Inc.)** 39:21 Yeah.
**Dan Gomez Blanco (New Relic, Inc.)** 39:22 M… Imagine if you come here.
and you see, you're an EndU, or someone that is willing to, like, write something, it would be nice if they… If you see the ones that are… You know, needing an author.
**Lukasz Ciukaj (Splunk Inc.)** 39:39 So then we need to clearly differentiate, like, labels. We cannot say that proposal is in review, and also needs auto. If it needs auto, then it's not in review, in that case.
You know what I mean.
**Dan Gomez Blanco (New Relic, Inc.)** 39:54 Mmm, I see your point.
Right, okay.
Let's remove it.
You convinced me.
But also, like, what I would say, do we need… the needs review is… Yeah, okay, so… maybe this is, like, a triage process as well thing, right? What needs review…
**Lukasz Ciukaj (Splunk Inc.)** 40:16 Proposal needs review is like a backlog, to be honest.
Because that is something that initially sometimes is submitting, it's the first stage.
And I think I documented this somewhere.
**Dan Gomez Blanco (New Relic, Inc.)** 40:27 Yeah, yeah, yeah, no, it is, it is there.
**Lukasz Ciukaj (Splunk Inc.)** 40:30 H1 open proposal.
issue…
**Dan Gomez Blanco (New Relic, Inc.)** 40:35 So, if we are in… So you open that proposal, and then it goes into, like.
**Lukasz Ciukaj (Splunk Inc.)** 40:45 UN approval, and then we have documentation PR.
**Dan Gomez Blanco (New Relic, Inc.)** 40:57 Right, okay, so I guess, yeah, the proposal is ready and waiting for the Blueprints of reference into review.
M… Fine, yeah, so I guess…
**Lukasz Ciukaj (Splunk Inc.)** 41:14 We should have it even automated, that if someone is opening… we should get the review, because that is to us, to the Blueprint team, also something that we can be notified, or we can track the labels, or we have new submissions, right?
**Dan Gomez Blanco (New Relic, Inc.)** 41:30 Nope.
Why don't we… To move this, and then call this needs review.
**Lukasz Ciukaj (Splunk Inc.)** 41:39 Yeah.
**Dan Gomez Blanco (New Relic, Inc.)** 41:40 Because when he goes in there, it's like…
**Lukasz Ciukaj (Splunk Inc.)** 41:41 initial idea.
**Dan Gomez Blanco (New Relic, Inc.)** 41:44 Make sense?
Makes sense.
**Lukasz Ciukaj (Splunk Inc.)** 41:49 And that matches the labels, right?
**Dan Gomez Blanco (New Relic, Inc.)** 41:52 Yeah, so we have the proposal in each review, I guess we can say that.
**Lukasz Ciukaj (Splunk Inc.)** 42:01 It was a neat.
**Dan Gomez Blanco (New Relic, Inc.)** 42:01 Proposal and review, proposal approved, and then we have published.
One thing we could do here is we can… Let's just remove this.
Delete view. All these different views are not really helpful here.
Roadmap view… My adding… maybe, yeah, my items.
We could probably say that the end review, we have been, I guess… I know that Alorita said that she was reviewing this one.
the proposal. Why is this telling me?
Is it a 5 as a number of… oh, because it's a Kanban board, of course.
So then, it will have a maximum per… Whatever.
Maybe this is somewhere else.
Settings…
**Lukasz Ciukaj (Splunk Inc.)** 43:05 I think it's a good start, and yeah, it's a great good job that we…
**Dan Gomez Blanco (New Relic, Inc.)** 43:10 I'm just trying to think. There was a thing here where you could say, actually, the…
**Lukasz Ciukaj (Splunk Inc.)** 43:16 To see the labels on this, or what?
**Dan Gomez Blanco (New Relic, Inc.)** 43:19 Mmm…
**Lukasz Ciukaj (Splunk Inc.)** 43:21 Yeah, that would be good to see the labels, you know, on these issues. Can we show the labels?
**Dan Gomez Blanco (New Relic, Inc.)** 43:27 And it… set limit, there we go.
I don't think you can.
Oh, 0, alright, okay, how many do we want to have in review? I don't know, there's no limit.
Let's do 100. Actually, if we have more than 100 in review, then we'll probably have a problem. And this probably makes sense, to have, like, you know, basically set limits for these ones. How many do we want? That's actually a…
**Lukasz Ciukaj (Splunk Inc.)** 44:03 There is no… there is no… Way to see the labels next to the… Issue name, here in this view.
**Dan Gomez Blanco (New Relic, Inc.)** 44:15 Mmm, there isn't… I don't think there is.
**Lukasz Ciukaj (Splunk Inc.)** 44:17 You know what I mean, so… to not… because that could help us to see where there is need outdoor as well, so someone looking in this could… or label it, you see? That's the one.
**Dan Gomez Blanco (New Relic, Inc.)** 44:28 There we go.
**Lukasz Ciukaj (Splunk Inc.)** 44:29 I love it.
This is the view I wanted to have.
Exactly where we are, and whether it's a blueprint, or whether it's the implement… reference implementation.
No, man.
**Dan Gomez Blanco (New Relic, Inc.)** 44:43 We can do swim lanes as well, which could be a good one.
You cannot do swimlins by label.
**Lukasz Ciukaj (Splunk Inc.)** 44:53 That is okay. That is okay.
So far, so good.
**Dan Gomez Blanco (New Relic, Inc.)** 44:57 You can slice by label, but… Maybe one, too.
**Lukasz Ciukaj (Splunk Inc.)** 45:03 Okay, I know what you mean. But no, it's… that view is good for the easy navigation.
**Dan Gomez Blanco (New Relic, Inc.)** 45:10 Yeah, this is good. Alright, okay, this is good. So, I guess here…
**Lukasz Ciukaj (Splunk Inc.)** 45:18 You can move everything to any review, actually.
**Dan Gomez Blanco (New Relic, Inc.)** 45:21 What I'm trying to say is, like.
**Lukasz Ciukaj (Splunk Inc.)** 45:34 Some of them are… We need the outdoor…
**Dan Gomez Blanco (New Relic, Inc.)** 45:39 Why does it put, like, 3? Oh, that was weird.
M…
**Lukasz Ciukaj (Splunk Inc.)** 45:44 And you need to change the limit in proposal in review to 100 as well.
No limits.
**Dan Gomez Blanco (New Relic, Inc.)** 45:54 No, there is a remove limit.
**Lukasz Ciukaj (Splunk Inc.)** 45:56 That's even better.
set limit, I think.
**Dan Gomez Blanco (New Relic, Inc.)** 46:04 There we go.
**Lukasz Ciukaj (Splunk Inc.)** 46:05 The thing purple, purples.
**Dan Gomez Blanco (New Relic, Inc.)** 46:08 Yeah. Because one of the things is, like, we probably want to have a limit of, like, how many do we have approved, right? And 5… I don't know, let's just have 5 for now, why not?
M…
**Lukasz Ciukaj (Splunk Inc.)** 46:18 But do we… but this one that Alex is working, is it part of ongoing or bootstrap? I think it's part of Bootstrap, right?
Yeah, I mean… on this board, but we can keep it here. Yeah.
**Dan Gomez Blanco (New Relic, Inc.)** 46:31 One thing is, like, do these So if I reload this, does it keep the same… one of the things that we could do is, like, if we want to, like, prioritize.
Things for people to, you know.
**Lukasz Ciukaj (Splunk Inc.)** 46:43 Mmm… Oh, there was something like priorities that,
**Dan Gomez Blanco (New Relic, Inc.)** 46:48 The worst, but like… I think if we have the order as, like.
Sort by… it is sort by priority.
**Lukasz Ciukaj (Splunk Inc.)** 46:58 But how to see priority? Like, does, can we see somewhere the priority? Yeah, so…
**Dan Gomez Blanco (New Relic, Inc.)** 47:03 The way that this works in these items is, like, if you open it here, it'll be at the bottom, which is not very useful.
He opened the issue.
it shows up.
**Lukasz Ciukaj (Splunk Inc.)** 47:17 The right side, fields, priority.
**Dan Gomez Blanco (New Relic, Inc.)** 47:19 Yeah, so in project… Yeah, sorry, here.
**Lukasz Ciukaj (Splunk Inc.)** 47:25 Yep. Oh, yeah, Argent Hein, we can…
**Dan Gomez Blanco (New Relic, Inc.)** 47:28 So we could use that if we want.
**Lukasz Ciukaj (Splunk Inc.)** 47:30 Yep.
**Dan Gomez Blanco (New Relic, Inc.)** 47:31 Not to it for now, but yeah. Okay, cool.
**Lukasz Ciukaj (Splunk Inc.)** 47:33 Awesome, good job.
**Dan Gomez Blanco (New Relic, Inc.)** 47:34 I need to… yeah, I need to drop, but yeah, so, Good stuff. I think we have more… A bit more…
**Lukasz Ciukaj (Splunk Inc.)** 47:41 Let's get to work on that, and we'll meet on Friday to talk about our session.
**Dan Gomez Blanco (New Relic, Inc.)** 47:46 Yep, sounds good. Alright.
**Lukasz Ciukaj (Splunk Inc.)** 47:48 Have a great rest of the day. Take care.
**Dan Gomez Blanco (New Relic, Inc.)** 47:51 Bye.
