SIG: End-User SIG: OTel Blueprints
Date: 2026-04-02
Duration: 39 minutes
Zoom Recording URL: https://zoom.us/rec/share/RDa3QRgyRxRTm-escsACmHYaJlxHzHOEZVlQV4JEHQvldsQfWth4ZX4WfllAB9KX.Nw0Wys6uavzo7pwP
============================================================

## Zoom Recording Transcript

**lciukaj@splunk.com** 04:02 Hello, everyone.
Good morning, good afternoon.
Oh, good evening.
**Tiffany Hrabusa** 04:09 I don't know.
**lciukaj@splunk.com** 04:12 We're based on the West Coast, Tiffany, do I recall it correctly?
**Tiffany Hrabusa** 04:16 I am, yes.
**lciukaj@splunk.com** 04:18 In mourning for you.
**Tiffany Hrabusa** 04:20 Thank you.
**Kevin Wagner** 04:22 Good morning.
**lciukaj@splunk.com** 04:22 What?
Hi, Kevin. Where exactly are you based in, Tiffany?
**Kevin Wagner** 04:27 I'm in Seattle.
**lciukaj@splunk.com** 04:28 Yep.
**Tiffany Hrabusa** 04:29 And I'm in San Jose.
**Kevin Wagner** 04:32 Very good.
**lciukaj@splunk.com** 04:34 I was in Portland last week.
nuts.
Different, it's Portland Oregon, right?
And Seattle, what you do.
**Tiffany Hrabusa** 04:46 I posted in the Slack channel that the meeting is Starting, so we'll give it another minute or two to see if anybody,
**lciukaj@splunk.com** 04:55 the new time for this meeting, 2PM, because it used to be 1PM, then I believe, due to time changes, it was 2PM, but now I think We are back to regular hours, right? Because there was a time change in Europe last week, last weekend, so we should be back to 1PM, or we stay with 2PM Eastern for this call.
**Tiffany Hrabusa** 05:18 I have no idea.
**lciukaj@splunk.com** 05:20 Okay.
**Tiffany Hrabusa** 05:22 Things are hard. Yeah.
**lciukaj@splunk.com** 05:24 That's…
**Tiffany Hrabusa** 05:24 And it's a good point, I should check and see.
**lciukaj@splunk.com** 05:29 Yeah, because I have in my, you know, my calendar a blocker every other Thursday, 1PM. It was… it was 1PM before. Then there was a time change, so it was 2PM, but now I think we should be 1PM again, but…
**Tiffany Hrabusa** 05:45 So, according to the official OpenTelemetry calendar, which.
**lciukaj@splunk.com** 05:48 Okay.
**Tiffany Hrabusa** 05:49 I don't sync with, because there are, like, 30 meetings.
this is the time for the.
**lciukaj@splunk.com** 05:58 I will repair that.
Nope.
**Tiffany Hrabusa** 06:01 But, I agree, things have gotten a little wonky, so, I haven't heard from Dan, so I don't know if he's planning to join or not.
But we can… we can add it as an agenda item to assess. The problem is that we have co-opted the end-user SIG meeting.
which happens on the alternate Thursday, and I don't think that we want to change their schedule if they're happy with that, so… But we can definitely add it to the agenda.
**Kevin Wagner** 06:36 I think you've answered a question that I was gonna ask, which was, is this the end user SIG?
Because it seems the topic is around blueprints.
**Tiffany Hrabusa** 06:48 That's right. So, the end-user SIG meets, bi-weekly, and…
**Kevin Wagner** 06:53 At this time.
**Tiffany Hrabusa** 06:54 At this time. And the OTEL… excuse me, the OTEL Blueprints project is an offshoot of the end user sake. It's actually being housed within the end user sake. So rather than creating an entirely separate meeting, we just… decided to slot ourselves into the alternate.
**Kevin Wagner** 07:13 Alternate weeks. Okay.
**Tiffany Hrabusa** 07:14 Yeah.
**Dan Gomez Blanco** 07:16 There's already way too many meetings.
And they don't tell.
M… It's always really difficult now, these days, to find a slot in the hotel calendar, to be honest.
**Tiffany Hrabusa** 07:33 Dan, I don't have the power to take over the… I don't have the Zoom permissions to boot Hope's Notetaker, so…
**Dan Gomez Blanco** 07:42 Yeah, I'll do it, yeah, I think, if I remember correctly.
There are 5 or 6 accounts.
I always need to remember which one this one is set on.
One second… Yeah, you got the right one.
**Kevin Wagner** 08:05 The alternate weeks is the same.
Zoom invitation, though.
**Tiffany Hrabusa** 08:10 That's right.
**Kevin Wagner** 08:11 Okay, alright.
**Tiffany Hrabusa** 08:13 Yep.
Are you familiar with the Blueprints project? Do you know what we're trying to do?
**Kevin Wagner** 08:18 Well, I… I lurked.
For a couple of weeks.
And I've read some of the… read some of the content, so it… so it looks like you're… you're building a library of best practices.
**Tiffany Hrabusa** 08:30 Yeah, Dan, do you wanna… Take that, or…
**Dan Gomez Blanco** 08:34 Yeah, it's, yeah, effectively, it's a library of best practices. The only difference is that we're taking a bit more of a strategic, thinking approach of, like.
Not trying to recommend… So, like, focusing first on the problems to solve, and then… recommending guidelines for… for those. So, like… In terms of, like, scoping the different blueprints, or the different, sets of recommendations or guidelines.
Or best practices, we're grouping them in… In the different types of problems to solve, right?
**Kevin Wagner** 09:14 Okay, alright.
**Dan Gomez Blanco** 09:18 And… See if I can bring up the notes…
**Kevin Wagner** 09:24 Yeah.
And these… these blueprints are… are they… are they different in any way than any of the other… Sort of, like, architectural… observability, architectural approaches.
That I might just Google.
**Dan Gomez Blanco** 09:40 M… Depends, I guess there are some of, I've not seen many that are struct… I mean, the template that we put together, it's, It's a little bit different than what you may normally see, however.
**Kevin Wagner** 09:56 earning this.
**Dan Gomez Blanco** 09:57 There's nothing… it's not like a completely new way of doing things.
I guess it's a… Done and trusted way of, thinking about… yeah, thinking about strategic blueprints. But, Yeah, so I guess the… the… The end result should be… well, we're not going to be recommending something that is not Pretty much the de facto.
Best practice.
**Kevin Wagner** 10:24 Right.
**Dan Gomez Blanco** 10:24 But in a different way.
**Kevin Wagner** 10:26 Okay.
**Dan Gomez Blanco** 10:26 M.
**Tiffany Hrabusa** 10:28 And maybe the only other advantage is that they're going to be vetted by the experts, right? So, each… each part of the blueprint that touches different parts of OpenTelemetry, we plan to have that reviewed by maintainers in those SIGs, so that we just make sure that it's… what OpenTelemetry wants to recommend.
**Kevin Wagner** 10:49 Okay.
**lciukaj@splunk.com** 10:49 And something to add here, like, based on my observation, I didn't see, like, many good articles or blog posts that are vendor agnostic, and where we see, like, recommendations about, you know, the architecture.
majority of them are, like, either Slang or Grafana or, like, you know, the vendor-specific, you know, the architecture. So, I think what we are doing here in, as part of OpenTelemetry project, in these Blueprint initiatives, is to, like.
have a general recommendation, general best practices, like, vendor… that's what we… what we want to achieve in open telemetry as an open source project, so I think that is a clear differentiation to what we currently have in the internet, publicly available.
**Dan Gomez Blanco** 11:35 Yeah, actually, that's something that we, right.
I wanted to talk about some of the items that we covered during KubeCon.
Which one… one was specifically about that, about the… I guess the… the boundary between the… the vendor-specific.
or observability backend specific, and the OpenTelemetry… General advice, right?
So, but before we go into that, just have a look at the… At the board, I will start to focus more next week on this, after I… I did wanted to get a lot of feedback from KubeCon, and I think we did get a lot of feedback at KubeCon, which is great. And this week has been post-CubeCon, which is always… Difficult. So I…
**lciukaj@splunk.com** 12:29 Time to get back to reality, right?
**Dan Gomez Blanco** 12:32 Exactly, yeah, going through the backlog of whatever it was. Waiting until KubeCon.
So, yeah. But, okay, so… I think this represents… everything we've got in progress.
Anything to… Comment on this. I think there were some comments on your document…
**lciukaj@splunk.com** 12:56 Yeah, and no major progress here. I've seen that Tiffany and you, Dan, reviewed that dog and also Alan.
So from Tiffany, there was, like, mainly formatting comments, so I already accepted all of them, but from you, Daniel, I see there are a couple of comments, like, content-related, and I didn't have a chance to, you know, look into it and address this. So, again, for me, this blueprint was, like.
version 0.1, and my goal was to work on this, maybe, you know, create some diagram.
and make it closer to GA, but unfortunately, I didn't have the time to work on this. It was busy time for me as well, you know, the spring break. Now, I think that I will get back to work on this next week.
I need to set some deadlines, you know, for myself, when I want this to be, like, ready for American Corporation.
**Dan Gomez Blanco** 13:54 I think you're in customer adoption, as well as me, I think, so end of the financial year is always a struggle.
**lciukaj@splunk.com** 14:01 Yeah.
**Dan Gomez Blanco** 14:01 So, yeah, okay, cool.
Yeah, I think, there are… there are a few comments there, but yeah, we're… I mean, I've… I've, one of the things that, I guess, we… it's good that basically this doesn't need to be perfect to open a PR, right? This is the first round of feedback.
it is a bit hidden here, in a way. You know, I know that it's in a… it is in a, you know.
in an issue, it's linked, you know, it's public, right? But, like… until we… when we think it's ready for, you know, after the first round of the review, then we open it, we open the PR in the website, and then we.
**lciukaj@splunk.com** 14:43 Yes, but here I remember we were waiting on the section to be created.
**Dan Gomez Blanco** 14:48 Yeah.
**lciukaj@splunk.com** 14:49 You're not free, or not good.
**Dan Gomez Blanco** 14:51 Well, in that.
**Tiffany Hrabusa** 14:52 It's almost ready.
**Dan Gomez Blanco** 14:53 Almost ready.
**Tiffany Hrabusa** 14:54 There's a PR up, I just need, some approvals, but it… the scaffolding is… is…
**lciukaj@splunk.com** 15:01 How it's gonna look once merged. There will be, like, a section in OpenTelemetry website, but there will be, like, a placeholder, right? Until the first PR will be merged, correct?
Yeah.
**Tiffany Hrabusa** 15:13 Right now, the… I can.
**lciukaj@splunk.com** 15:16 You know what I mean, because… you opened the PR to create a new section, but in that section, we should have blueprints. Blueprints are not yet ready, right? So I think that the first stage, there will be a section created, but they will be empty, so some kind of placeholder only, maybe? Or some quick information that, yeah, here will be blueprints soon, or something like that.
**Tiffany Hrabusa** 15:38 Yeah, so right now, there's a landing page that, is for the top-level NAV, guidance and architecture. There's a landing page that gives some explanation of what these things are, and then there are… there are sub… or there are child pages for blueprints and then reference implementations, and right now, each of those child pages is a landing page that defines what a blueprint is, and then what a reference implementation is, and then at the end of that definition, I've just added coming soon.
Okay. So, we can… we can merge that PR, as is, and it'll be ready for, for you to… to add to in… in your own PR.
**lciukaj@splunk.com** 16:22 Okay.
D, dot.
**Tiffany Hrabusa** 16:24 I'm just waiting for approvals at this point, so…
**Dan Gomez Blanco** 16:26 Cool. Alright, I'll… I'll give it another… another look. I think the… yeah, I had some… I added some comments, but… yeah. So is the… sorry, I forgot I… I didn't catch that last bit. Is the intention that the, that that section will be… Hidden until we have content, or…
**Tiffany Hrabusa** 16:44 No, it, it's, it's ready to be published as is.
**Dan Gomez Blanco** 16:48 Yeah.
I mean, it's already… yeah, the project has already been announced and everything, so I think it's fine to have a… as long as the folks in the website maintainers, as long as you are happy with a section there with, coming soon, then, yeah.
**Tiffany Hrabusa** 17:02 Yeah, we've done it before with, some of the, mobile and browser SIG stuff, that was… we just had, like, more content coming soon, which… In this case, I'm perfectly fine with it, because I know that Lukage is… PR is almost ready to be raised. The… it may not be ready to be published, but the PR is almost ready to be up, so I'm… I'm good having that.
**Dan Gomez Blanco** 17:27 Okay, and I think related to that, I've not started working on it, but there is, I guess these two are the same. We… Yeah, what is it? There was an issue to create the README in the ref… in the architecture directory, and the templates, and the issue templates as well.
Yeah, I'll make sure of that.
I add those here.
Okay, so that'll… yeah, that will be next week, Friday and Monday is, public holiday here, I'm not sure.
If, many folks in… Europe? I'm not sure about… is it a public holiday in… in America? Monday, so Friday, Good Friday, or… Eastern.
**Tiffany Hrabusa** 18:23 No. Is that? Okay.
**Dan Gomez Blanco** 18:26 I think most of Europe would probably be so, if you've got any hotel.
Maintainers in Europe, they'll probably… Be on public holiday.
**Tiffany Hrabusa** 18:35 I'm actually looking forward to it being a little quiet so I can get caught up after a few questions.
**Dan Gomez Blanco** 18:39 Good, good.
Okay, Alright, so second point of today, time zones are hard. Businesses meeting time still work for everyone?
I think they… yeah.
Here's an… an idea, and I know that the CICD I mean, it works for me, but, like, here's, something that the CICD SEG have been doing is, like, have a poll on the Slack channel.
About times. Maybe we could do something like that.
**Tiffany Hrabusa** 19:21 Yeah, I think… I think that's a good idea. We would just have to be okay, essentially, creating a new meeting, right? Because we wouldn't want to affect the end user SIG.
**Dan Gomez Blanco** 19:33 Yeah.
Yeah, yeah, exactly.
**Tiffany Hrabusa** 19:34 Okay.
Okay.
**Dan Gomez Blanco** 19:37 So… I mean, we can put some times… I can create, Yeah, let me just have a note here.
I'll create a doodle, or something.
What a poll.
Because I think there are a few more folks that, joined, or wanted to join the… the… the SIG?
Or the, yeah, the project, so… Yeah.
I'll do that.
Alright, okay. Anything else? Anyone… I don't know who… Originally added this, was it?
**lciukaj@splunk.com** 20:24 Before we were gone, so we were…
**Tiffany Hrabusa** 20:26 Yeah, it was…
**lciukaj@splunk.com** 20:27 Funny.
**Tiffany Hrabusa** 20:27 Bye.
I added it because, Apparently, there were some time changes in Europe over the weekend, and so now it's very confusing about, like, do we adjust this meeting time back to some other time? Yeah.
And I checked the official OpenTelemetry calendar, and this is the time slot allotted, so I don't know if… That… basically… and I knew that it had come up at KubeCon, too.
with Damien, so, I figured it would be a good time to just…
**Dan Gomez Blanco** 20:56 Okay.
Let's do that.
**lciukaj@splunk.com** 20:58 But this time still works for me for first 30 minutes, then I have a regular customer call, 2.30pm Eastern, so… I'm okay with joining just for first 30 minutes, if it's gonna stay 2PM.
**Dan Gomez Blanco** 21:13 Okay, it may… if it's earlier, would I be, I guess, would that be okay, promoting.
**lciukaj@splunk.com** 21:19 Yeah, 1PM, that's where I have my blocker every other week, every other Thursday, and, like, keeping my calendar clear for this time.
Even the… even… I think we should… But I agree with you.
**Tiffany Hrabusa** 21:35 I should do.
**lciukaj@splunk.com** 21:36 Sorry, Gosh, go ahead.
**Tiffany Hrabusa** 21:37 Wings.
**lciukaj@splunk.com** 21:38 Sorry. That we should be aligned with the other, like, you know, end users. It makes no sense to have one meeting at 2PM, one meeting at 1PM. If that other call is 2PM, then yeah, let's… let's keep 2PM, I'll be joining first 30 minutes, and we usually… you know, wrap up after 30 minutes or 40 minutes, so it should be fine, still. And we have recording ourselves.
**Dan Gomez Blanco** 22:01 I'll just put my hand out there. For me, if it's earlier in the day, that would probably be a good thing. This is, like, 7.20pm right now, so… over here. So I wouldn't mind if it's a bit earlier, personally, but yeah.
**Tiffany Hrabusa** 22:15 Yeah, I can do earlier, it just depends what time, because I do have other meetings, so I…
**Dan Gomez Blanco** 22:22 Okay.
**Tiffany Hrabusa** 22:22 If we do the poll, I think that's a good way of…
**lciukaj@splunk.com** 22:25 Let's start with Paul, I agree.
**Dan Gomez Blanco** 22:28 Sounds good.
Okay, so, just a quick summary of, the… I just wanted to bring some of the notes and the discussion points from KubeCon. We had, an on-site, Meeting, had, folks from… The collector and DevEx SIG as well, join in.
Some of the things that we talked about were related to… well, the first one is, like, what is the scope for each of the blueprints? We currently have three.
Three blueprints. But as we evolve, yeah, how do we decide if there's… this corpus too big, this corpus too small?
Or, you know, how do we decide if something overlaps with, between different things, right? And I guess, you know, the thing that we talked about is that we should put attention and effort in defining the scope of the blueprint, and and ensure that the scope is defined by the common challenges section of the template.
So, yeah.
The problems to solve should define the scope.
Mmm… So… I think there was an example here.
If attended for Odell Internal Platform, covers SDK config.
**lciukaj@splunk.com** 23:49 Hang on, quick question here. Is this feedback coming directly from end users, or was it, like, internal discussion of maintainers and contributors?
**Dan Gomez Blanco** 23:58 I'm trying to think, was it any end user in that meeting?
No, I think this came directly from maintainers, but we had two… two meetings, actually. One with… one was the SEG, and then I had another catch-up with, with Juliano from the DevEx SEG in Alolita.
Alolita leads the CNCF, end user… Tap.
I think it's a tap.
So, yeah, so also aligning with what's already been done in the end user… in this… in the end user… reference architectures, peas in the global CNCF.
effort, so, yeah, so I think both of those, but mostly from… Well, no, entirely, the conversation was within maintainers, right.
**lciukaj@splunk.com** 24:43 I mean, it's okay, I agree with that, I mean, but eventually, we are doing that for end users, right? Of course, yeah.
The more feedback we have from end users directly from the field, the better, right? I have one customer who is, like, very, like, open telemetry, very major in OpenTelemetry, so I can check with him, maybe I will share the notes or the link to the project and ask him maybe some feedback, comments.
**Dan Gomez Blanco** 25:11 Yep, yeah, I think, yeah, absolutely. We, we're looking for… It was already called out in the project updates, apparently the room was quite full. I… Yeah, I basically managed to… get myself into the booth duty… booth duty for, OpenTelemetry. I was in the OpenTelemetry booth when the OpenTelemetry project updates was happening, and I think…
**lciukaj@splunk.com** 25:35 Okay.
**Dan Gomez Blanco** 25:35 Marillia was mentioning the hotel blueprints, looking at me in the audience to point at me to get end users to come and talk to us, but I wasn't there. However, it was, yeah, it was mentioned there, so hopefully we get more folks to join as well, right? And give us their feedback.
**Tiffany Hrabusa** 25:56 We can'.
**Dan Gomez Blanco** 25:56 Awesome.
**Tiffany Hrabusa** 25:57 Do a blog post once we have every… once things are in motion.
**Dan Gomez Blanco** 26:02 Yeah, absolutely.
**Tiffany Hrabusa** 26:03 of outcomes.
**Dan Gomez Blanco** 26:04 Yeah, I think that's something that was… that was raised as well, that we should publicize this.
Wider, when we have something Maybe, like, when we've… I was thinking that after we have the… Yeah, I volunteer for this. After we have the, the, the, the… After we have the templates in place for it.
people to be able to raise, hey, I want to have a new… I want to share a reference architecture, or I want to share a work on a blueprint.
then… then I'll create the blog post, and then we'll have something a bit more.
More of a framework around it, right?
Yeah, so on the scope, I think this is one of the things that was identified, is, for example.
if the… so I got this from a maintainer, saying, well, if I want to do… I don't know, like, in an OpenTelemetry Gateway blueprint, for example, the blueprint is not about the OpenTele… not how to deploy an OpenTelemetry Gateway. The blueprint will be, hey, you want to provide an OTEL internal platform.
And these are the challenges that you're trying to solve. So the challenge may not be.
do not drop a single span, like, you know, 100% completeness on spans or on logs for audit logging, right? If that's not a challenge to solve, then the blueprint will not recommend something that's out of scope for that blueprint.
There will be another one, for example, for someone that wants to do audit login in OpenTelemetry, and that will cover that.
the recommendations that you… that you need to follow for that. So it's just the scope, understanding the scope.
On the progress to solve, right?
If, the next one we talked about was what was related to this, I think we talked about links between blueprints.
Yeah, so in the previous example, we should probably say, well, if you want to do… this doesn't… Cover audit login, but if you're interested in that, here's another blueprint, right?
Or if, we can expand in areas. And I think you mentioned at some point, Tiffany, to be able to do a, sort of like a matrix of.
**Tiffany Hrabusa** 28:18 Yep, yeah, we can… we can present… yeah, we can present the connections once we have enough.
Cool. To really, make it, makes sense.
**Dan Gomez Blanco** 28:31 Yep.
Another thing is, we should be able to… If multiple solutions are applicable, we should list them both, or… All of them, right? It would come to mind as, like, hey, you might have two different approaches, and depending on the type of team.
Are you using? I think one of the came… one that came to mind was, like, using the hotel operator for… Automatically instrument workloads, or provide… or if you're a platform team, you want to provide a you know, a default declarative config file that people can pull, and some… base Docker images. There are more different… there are different ways of doing it. They achieve the same result, but sometimes you may want to use one or the other, which you'll probably list, options that are… Achieving the same result.
And then different… And depending on the type of organization, they might choose one over another.
M… Another thing that we talked about was reviews.
We need to build, I guess, the… This will be… I hope that we can get folks that are currently contributing, like yourself, Luke? I mean, I'm… Or others that are contributing blueprints to become like, approvers?
And then have that, build that… at practice. However, for the time being, and for the… at least for the first… not just the three, but probably for a few blueprints.
We're always gonna need the… the approval, as well, of the experts, right? So, the TC to start with.
I know that Riley is the sponsor, the TC sponsor for this project.
So, get, you know, get visibility from the TC to approve these blueprints, or in its absence, maintainers. So, if the blueprint is specific.
let's say, focused on the collector. For example, the one for the Kubernetes, blueprint, the Kubernetes instrumentation, that will mostly be the collector.
Having folks from the collector to… to approve it, right?
That shouldn't be an issue, which is… need to… Let them know, and wait for them to review it, but it shouldn't be a major issue.
**lciukaj@splunk.com** 30:47 I think that we… I like this idea, and I could volunteer at some point to be, like, approver or reviewer for the ideas or for the actual blueprints, so that totally makes sense. But would that be… still part of end-user, yeah.
**Dan Gomez Blanco** 31:05 Yeah, so we are… we're gonna have, like, the idea is that, say, end user will have approvers, for…
**lciukaj@splunk.com** 31:12 or blueprints.
**Dan Gomez Blanco** 31:13 In the second user, we have maintainers.
And then we have approvers. Some of the approvers… I mean, at the moment, the approvers are mostly… I mean, I see the end user SIG having almost, like, two sides of a customer, or the end user side, the DevRel side, and the… and the, sort of, like, SA, or, like.
Yeah.
**lciukaj@splunk.com** 31:37 No, thanks.
**Dan Gomez Blanco** 31:38 Right.
**lciukaj@splunk.com** 31:38 No, my question was… my question was if that's gonna stay as part of the end user seek, or there will be…
**Dan Gomez Blanco** 31:44 It was the last part of the end-user seg, but it will be two… two different groups of people in the same.
**lciukaj@splunk.com** 31:50 Yeah, that makes sense, that makes sense, with the group of folks with a focus on blueprints specifically, right? Okay.
**Dan Gomez Blanco** 31:57 Yeah, exactly, yeah.
And then, yes, I know that you've got another meeting coming up, and just to finalize.
vendors… we see in the… this is currently out of the scope for this project, but in the future, we see maybe vendors wanting to have their own, like, architecture and guidance linked in there, as they… as we currently do with distributions, or as we currently do with, the hotel demo. If someone says, hey, you know, I've got an OTEL architecture, like.
website over here. That is… that takes this guidance and applies it to my particular environment, then we would consider that.
A lot easier than including vendor advice, vendor-specific advice, or back-end specific advice into the… into the website, right? That's not gonna happen.
So yeah, I think, linking out to other architecture websites could be an option, if people are up for it. But we're not… we just basically… that's, like, future, future after this project, right? We'll just discuss it later.
In terms of, like, CNCF, There are end-user architectures in CNCF, and we should encourage Sharing from one to the other.
And so… Yeah.
the… Alolita says that when people are sharing their architectures in the end user tab, they will prompt them to then do a smaller version of that, or, like, a subset of that for the… for this, for reference architectures here.
And the opposite.
talked about framework, like, feature process, it will be driven from the SEC end-user repo, so issue templates and issues will be created there.
Yeah, and yeah, so end users should be able to drive this. However, one of the things that the DevExSig have been doing is helping end users to write those reference architectures, so it's okay to give them a template.
But then maybe that's something that SIG end user can help with.
To, let's say, interview someone, And then write, Reference architecture from that interview, so avoiding them a bit of a bit of… a little bit of work.
Yeah, and then we talked about the taxonomy matrix of… How do different blueprints connect?
Cool. I think the, next steps… I think you mentioned that there are a couple of, you mentioned this in Slack, Tiffany, I don't know if there was an issue for the templates.
That you should know it, but, yeah.
**Tiffany Hrabusa** 34:47 Yeah.
So, the PR that I have for creating the new section will close the two existing issues for creating those sections. The only thing that's missing is How people can contribute.
And so I've created a follow-up issue for that.
Because that is dependent on one… number one and number 2 being completed.
**Dan Gomez Blanco** 35:15 And that would…
**Tiffany Hrabusa** 35:15 And then… Yeah, I think there was no issue for number 2.
So I created that issue.
**Dan Gomez Blanco** 35:24 Yeah.
No.
**Tiffany Hrabusa** 35:27 I don't know if it has a label, but yeah.
**Dan Gomez Blanco** 35:32 You know, we'll take that.
Okay, yeah, that makes sense.
So… This one will be sort of… Blocked by the actual… Template.
Template.
Complete.
Okay, cool.
Sounds good.
**Tiffany Hrabusa** 36:21 Okay. I just saw that, patrice.
reviewed, the scaffolding PR, so he has a couple comments there. He wants to rename the section to guidance and… or no, blueprint… he just wants to call the top-level section Blueprints and Reference Implementations.
**Dan Gomez Blanco** 36:43 Okay.
**Tiffany Hrabusa** 36:44 I mean, I don't have a strong feeling Either way, I mean…
**Dan Gomez Blanco** 36:49 Yeah, I mean, I think that, that, yeah, it's probably more… Yeah, I think it's probably more… It's better at defining, I think, what we're… Otherwise, like, guidance and architecture, guidance could be guidance on anything, right? I guess that, yeah, that could probably.
**Tiffany Hrabusa** 37:09 And architecture could mean… Yeah. You know, other things, too. So yeah, I think that's fine. And then if we… Find that we have additional guidance beyond blueprints and reference implementations at some later date, we can adjust.
**Dan Gomez Blanco** 37:24 Yep, makes sense.
**Tiffany Hrabusa** 37:26 Okay.
So if you get a chance to sign off on that PR, hopefully we can get it merged.
Tomorrow, and that means… that frees up Lukash for, putting up his PR, which I think is important.
Do you want me to copy the Mastodon blog post from DevEx into a PR as well, for the first reference architecture? Okay.
**Dan Gomez Blanco** 37:54 Yeah, that would be good.
**Tiffany Hrabusa** 37:56 As well.
**Dan Gomez Blanco** 37:56 I think what… the only thing is just copying that and then adding the… I guess… Well, I guess it's already got the dates, right? So if you, if you… The moment that you add a document, it will have the date in there.
Mmm…
**Tiffany Hrabusa** 38:11 I mean, we can add an actual date, too, like, it, you know.
**Dan Gomez Blanco** 38:14 There's more of this.
**Tiffany Hrabusa** 38:15 part of… yeah, yeah, we can absolutely do that. But I think getting it into a PR, because we don't have a reference implementation template yet, so I don't know if we want to… Reverse engineer it based on the blog post, or…
**Dan Gomez Blanco** 38:33 It's a good question. I think it's… I think it's good just to put it… put it out there. Okay.
Yeah, I think the template… I mean… for reference architectures in particular, I think I'm less worried about it, because, like, the template it's something that will potentially evolve as well. And we're not going to go back and change all the reference implementations every time we change the template, right? So, so I think that's… that makes sense, yeah.
To just have it as wherever we have right now, yeah.
**Tiffany Hrabusa** 39:05 Okay, so once this scaffolding PR gets merged, I'll put up the PR for the Mastodon.
Implementation.
**Dan Gomez Blanco** 39:13 Awesome.
**Tiffany Hrabusa** 39:14 Okay.
**Dan Gomez Blanco** 39:15 Okay. No, thank you very much.
**Tiffany Hrabusa** 39:17 Yeah, have a good one.
**Dan Gomez Blanco** 39:18 Yeah, see you, bye-bye.
