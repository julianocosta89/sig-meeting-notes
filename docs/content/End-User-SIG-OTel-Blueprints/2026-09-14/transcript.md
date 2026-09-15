SIG: End-User SIG: OTel Blueprints
Date: 2026-09-14
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Lukasz Ciukaj (Splunk Inc.)** 04:21 Hi, Dan.
Hello?
**Dan Gomez Blanco** 04:26 Oh, hello.
**Lukasz Ciukaj (Splunk Inc.)** 04:28 Sorry for being late. We've got some emergency here in the office. I was working from the office today, and there was some… Water… leakage in the area, it was like, this is huge, like, 50,000, you know, customers is impacted.
And, in the area where Cisco office is located, and we just got an email that we need to leave the building immediately, because there is, you know, low water pressure, and there is some advisory, you know, to save water, etc. So, we're just leaving the… leaving the building, and I'm in the car now, but we can talk a few minutes to review, maybe, you know, the ongoing items.
**Dan Gomez Blanco** 05:04 Yeah, so I think, yeah, just as a quick review. By the way, feel free to… to drop. I mean, I can…
**Lukasz Ciukaj (Splunk Inc.)** 05:12 No, I'm good, I'm good.
**Dan Gomez Blanco** 05:13 We can also send a review on, Let me just… async as well, right? But, so, Alex sent a message, he's not going to be able to join today, but he's been working on the… Sorry, I just gotta create the meeting notes.
He's going to join the… So he's been working on the… on the reference… Sorry, on the Blueprint for Kubernetes.
**Lukasz Ciukaj (Splunk Inc.)** 05:45 Yep.
I've seen some emails, I didn't have a chance to look into the details, but I've seen he was responding, so that was for me the, you know, indication that he is available to continue working on that.
**Dan Gomez Blanco** 06:05 Right, okay. So, just adding some stuff to the notes, what is the statistics north.
Okay.
Right, so if we,
**Lukasz Ciukaj (Splunk Inc.)** 06:26 I'm opening that PR now.
**Dan Gomez Blanco** 06:28 If I share my screen… Let's look at the board first.
Yep. Alright, so, I think you made some changes to… Yeah, so the country… so that was merged, the second PR to the website.
**Lukasz Ciukaj (Splunk Inc.)** 06:52 Rakuten.
**Dan Gomez Blanco** 06:52 Was merged, right?
**Lukasz Ciukaj (Splunk Inc.)** 06:54 Yes, so it was matched last week, on the… document on the OpenTelemetry.io, so we have both areas now covered, so the issue is closed. So I'm good here.
**Dan Gomez Blanco** 07:08 I have also, added more… yeah, so this one is merged as well.
Add in more… Guidance, so thanks for the… the review. So now, if we go here, just for anyone that may be watching this.
Architecture… the architecture section, and this, again, user repo.
Yeah, the… Guidance, the guidelines.
For authoring… Preference implementations, Blueprint guidelines as well.
Over here. Which are basically… is basically what was in the comments of, Of the other… of the… of the template. And the template now just is a bit more…
**Lukasz Ciukaj (Splunk Inc.)** 07:54 I mean, it was fun, when I was reviewing this PR, then I, you know… finally, you know, understood what is the change about, because I was initially confused why we are moving these, you know, comments, but now it makes sense to me that we separate, you know, the one thing, let's say, the issue template from, let's say, the guidelines that we have here, so that definitely makes sense.
**Dan Gomez Blanco** 08:18 One thing that I didn't do, now that I'm reading through it, probably should… Is that we should probably… we mentioned the templates here at the bottom.
But I probably should… Add something here… Around open a proposal issue, proposal,
**Lukasz Ciukaj (Splunk Inc.)** 08:41 That was my PR, so what do you think, what we should change here?
**Dan Gomez Blanco** 08:45 Just… just to add, you know, to link in that guide… those guidelines.
**Lukasz Ciukaj (Splunk Inc.)** 08:50 Oh, yes, that's a good idea, but I'm wondering in which stage… I think step one, maybe? Can you scroll a little bit up?
Proposal issue… No, okay, not proposal, on-ish… I think that's documentation PR, right? Step 3.
**Dan Gomez Blanco** 09:13 Yeah, it will be there.
**Lukasz Ciukaj (Splunk Inc.)** 09:15 Oh, I can open that quick PR. So you can put it on the… or open an issue, or I can open an issue for this, and to update it, include the guidelines that we have. So that will be quick one, so yep, I can do it.
**Dan Gomez Blanco** 09:28 Okay, cool.
Then we've got the Kubernetes… the Blueprint for Kubernetes 4.3.
I will have a look at this tomorrow morning. Okay. Today, I was feeling a bit under the weather.
So yeah, so I think… There was a, like, a push from… From Alex, I did have a chat with him. I think the, the main… The crux of the issue is that we… we're now basically saying the way that you do this in Kubernetes or that you do Kubernetes observability.
is using the OpenTelemetry CubeStack, right? And that changes certain patterns. For example, it was mentioned there that, the most important one, perhaps, the most important thing here, was the fact, one, we were not covering logs at all, which I think we should mention logs, probably being covered now.
From the perspec- not from the perspective of, like, workloads that are used in login… through OTOP, like, from… because that's already covered in the… in the other one, right? Yeah. In the… in the standard, like, if you're using OTOP, you go through a gateway, and… and that's great. But rather, like, the one related to, Yeah, the one related to, logs that are coming from Standard Out, right? That, that you… the, the, the… OpenTelemetry CubeStack deploys.
Can deploy the log file receiver.
So then, that should be there as well. And the other stuff that was related to… Prometheus scraping, right?
So yeah, so I think this is a change in the other one, which is that instead of using the target allocator, even though we should give it as an option, the receipt… the Prometheus CubeStack, sorry, the OpenTelemetry cube stack, deploys a collector daemon set, right? So… by default, that comes with a node-level scraper, basically, so you will scrape anything that has got a particular, like, you know, if it's called Prometheus.io scrape true, you will scrape from node local, and only scrape the pots in those.
in those notes, in their respective notes. So that removes the… the need for a… For, you know, target allocator, having to, like.
spread different scrapes across a pool of collectors. So, yeah, that is another part of the advice that we're giving here.
**Lukasz Ciukaj (Splunk Inc.)** 12:17 And I can see that Alex included some nice diagram as well, so that was one of the feedback I provided, that it was Plain text in the initial version, so it seems that he nicely incorporated some.
mermaid diagram, which I like, so… alright.
**Dan Gomez Blanco** 12:33 So that's cool, and then, yeah, and then some other links to stuff. Right, so I think… If we… Yeah, I'll go and have a look at this, tomorrow. I'm not gonna go through that now, but yeah, it looks like it's in better shape now.
Mmm… Another thing that we… I wanted to talk about today… Walls, and I'm gonna put it here, Right, so, in the, in the website, there are… I had a chat with the, with the comms team.
One of the things that we've been suffering from is, I believe, is, like… these PRs that are huge, right?
As in, like… it's not that they're huge, but they're, like, there's a lot of content here to review.
**Lukasz Ciukaj (Splunk Inc.)** 13:29 That's true.
**Dan Gomez Blanco** 13:31 jungle.
So, the way that this has been approached in the past in docs, in documentation, is, like, is that they, you know, you have a warning at this, you know.
You basically have some type of, like, Yeah, note at the top of a document that says this is a work in progress.
And then you just basically have it at that. Another option… Is that in the… in the, And I don't know if this works for every page, or only for blogs, but there is a draft If you put something in the from matter, that is, like, draft true.
You can merge it, but it doesn't render in the… in the UI.
Right.
**Lukasz Ciukaj (Splunk Inc.)** 14:19 So what's the difference? So this is merged?
**Dan Gomez Blanco** 14:21 Fat to you?
**Lukasz Ciukaj (Splunk Inc.)** 14:23 But you cannot see it on the, on the.
**Dan Gomez Blanco** 14:24 You're gonna see it in… you're gonna see it in public. You can only see it…
**Lukasz Ciukaj (Splunk Inc.)** 14:28 Okay. But what would be the… what would be the difference, then? Why to merge and not publish it? I'm confused.
**Dan Gomez Blanco** 14:34 So, the reason why I was thinking that is that if we merge it.
it is a part of, like, you know, we can take it in a more… in different steps. And I don't know if this is an issue or not, basically, that's what I'm trying to… to think, if it's…
**Lukasz Ciukaj (Splunk Inc.)** 14:49 What problem are we trying to solve here? I know what you mean, that, okay, it's long, like, there is a couple of pages, and there is, like, multiple components, multiple six that quite often need to provide the feedback, but… Matosa.
**Dan Gomez Blanco** 15:06 I'm trying to break it down… basically, I'm trying to apply the principle of, like, breaking it down into smaller… into smaller pieces so that they're reviewed independently. So you could just say, basically, create a PR with the… with the, with the background and the common challenges, right? For example, get that review…
**Lukasz Ciukaj (Splunk Inc.)** 15:26 Oh, okay, I know what you mean. Okay, so there will be actually a couple of PRs for one Blueprint.
**Dan Gomez Blanco** 15:34 Yeah, 2 or 3, yeah.
**Lukasz Ciukaj (Splunk Inc.)** 15:35 Okay, two or three. Okay, and then eventually the last one will be the one that will make this public. Okay. Yeah. That makes sense.
**Dan Gomez Blanco** 15:45 I mean, I'm not convinced either, I just wanted to bring it out as an idea, right? As in, like, if it's… because I see that if these PRs are open for a long time, it may then, sort of, like… what I think it may do is it may, it may damage the morale of the person that's got that PR open, right? But that PR… and then… especially if it's someone that may not be contributing day in and day out to open telemetry, right? But they've got a PR open in there, and then…
**Lukasz Ciukaj (Splunk Inc.)** 16:14 I know, I, I…
**Dan Gomez Blanco** 16:15 Yeah.
**Lukasz Ciukaj (Splunk Inc.)** 16:17 Yeah, yeah, that's a… that's actually an interesting approach that I'm… Then first, we would need to check if there is… if it's possible to have it merged but not published.
And how that works. I think, you know.
there shouldn't be any difference between, let's say, regular documentation pages and blog posts. It's the same mechanism behind, right? It's Hugo…
**Dan Gomez Blanco** 16:39 We… not quite, I think, because there are things that are in the from matter that don't, So if you go to… Content… English.
blog.
That's true.
This one, for example, which… We'll have a from matter… let me see…
**Lukasz Ciukaj (Splunk Inc.)** 17:05 This is merged, but it's not published, or…
**Dan Gomez Blanco** 17:08 No, this is published.
**Lukasz Ciukaj (Splunk Inc.)** 17:10 Do you have an example? Do you have an example of, let's say, work in progress?
**Dan Gomez Blanco** 17:18 But that's not gonna… So yeah, so here we've got…
**Lukasz Ciukaj (Splunk Inc.)** 17:41 Maybe there is some flag, or something that…
**Dan Gomez Blanco** 17:44 So apparently this works, right? Because they're using that here for…
**Lukasz Ciukaj (Splunk Inc.)** 17:48 Oh, there… you see there is a draft… draft true.
**Dan Gomez Blanco** 17:51 Yeah, that's what I mean. So they're using that for the Portuguese translation, right? So if I go to the website… Collect or deploy, choose. If I go to the website…
**Lukasz Ciukaj (Splunk Inc.)** 18:02 Yeah, I know.
**Dan Gomez Blanco** 18:05 If I go to the collector… Deploy… Boy… Agent deployed gateway.
**Lukasz Ciukaj (Splunk Inc.)** 18:21 Yeah, I mean… That's a good point.
But… the other side… Maybe we will overcomplicate the entire process.
**Dan Gomez Blanco** 18:33 Yeah, that's my… that's my concern, basically, is, you know, yeah.
**Lukasz Ciukaj (Splunk Inc.)** 18:42 Maybe we need to find other solutions to the problem, like, how to make sure that We work more efficiently with the reviews and all of that, like…
**Dan Gomez Blanco** 18:51 Yeah, also, like, that when people open the PR, it's not, like, you know, it doesn't sit there for, like, 3 months, right?
**Lukasz Ciukaj (Splunk Inc.)** 18:58 Yeah.
**Dan Gomez Blanco** 18:59 My only concern as well.
**Lukasz Ciukaj (Splunk Inc.)** 19:01 Absolutely, because in this time, there might be some event, you know, that… Architectural change that requires starting from scratch, or something like that, right?
**Dan Gomez Blanco** 19:11 Also, like, the person might… might also… stop contributing, right? So they've spent all the time, and then they just don't have the bandwidth to go and act on, like, the… the comments, right? So, that's another aspect where I think breaking it down could… Help, because it would help to… to do that.
Yeah, I'm not… I need to… yeah. Maybe there's a discussion that we can have in the… in this LAC channel.
And then…
**Lukasz Ciukaj (Splunk Inc.)** 19:40 Yeah, yeah, that's a good point, but I think that we should maybe leave it for, let's say.
For future. Let's try to get it started as it is.
**Dan Gomez Blanco** 19:51 Yeah, let's get it started as it is. Yeah. Thinking about… I wouldn't change it now, basically, that's what I'm saying.
**Lukasz Ciukaj (Splunk Inc.)** 20:00 I think that could… if we can make it to this, working in the same way, like having a draft and a couple of PRs, and keep merging, let's say, this, let's say, bundles or chunks of… of… of actual Blueprint, and then… Have a final version and publish it.
Good. But, yeah, let's see how it works.
**Dan Gomez Blanco** 20:21 Another idea, another idea is without, you know, do it without… a… a PR, right? Which is, like, someone opens a Google Doc.
And we start to basically get feedback in there, when we think that the content is okay, then you open up PR to the… to OpenTelemetry I.O. when, like, the content is good, it's just a matter of, like, just putting it into Markdown. Yeah. So then…
**Lukasz Ciukaj (Splunk Inc.)** 20:48 Yes and no. I mean, this is a good approach, but from the other side, you know, reviewers, they like to have, you know, documented that they did review, that they spent some time, you know. In Google Docs, you don't have that history that you have in GitHub.
**Dan Gomez Blanco** 21:01 True, true.
**Lukasz Ciukaj (Splunk Inc.)** 21:02 That's, that's another, another challenge.
**Dan Gomez Blanco** 21:05 Alright, we can…
**Lukasz Ciukaj (Splunk Inc.)** 21:08 Yeah, I like the idea, Dan, but I think we should get started with what we have, and maybe after a couple of Blueprints, if we see that the problem is still there with this extended, you know, time and challenges, maybe we can try to, you know, revisit that. So that would be my suggestion.
**Dan Gomez Blanco** 21:23 Cool. Right. That makes sense. Now, there are two things here that are left for us, apart from merging this, and then I will add another thing we should probably, yeah, create a blog post after this first round is merged, right?
Actually… I will create an issue.
And then I'll add more details later, but, Because I think there are… as a parent issue, there are things that we need to do there.
I will add more details later.
**Lukasz Ciukaj (Splunk Inc.)** 22:15 Oh, no.
**Dan Gomez Blanco** 22:15 to say here is, like, we need to… there are certain things that one needs to do to close a project.
Like, move… like, basically declare a close, and move it to… move the project, Proposal in the community report to its place, and blah blah blah.
And then, one thing that… We would do as well as part of this is create a blog post.
Summarizing it, asking for more contributions, and really start with the BAU, really, of maintaining this, and then adding more Blueprints. Yep, correct.
Yeah, it's okay. So, one thing that, if we want to close this down, it would be good if you… yeah, so we don't have… this is one thought that I had here, is like, we don't have any… Reference implementations for… I can think about this as well, right? For infrastructure, Well, not for infrastructure, sorry, for non-Kitz environments.
So, any… Let's say, and if we can convince… any of our respective customers to go through the… Yeah.
**Lukasz Ciukaj (Splunk Inc.)** 23:26 I have one customer, actually, that I visited last week, and they are very, like.
heavy into OTel, but they have some crazy, you know, internal policies about contributing, so they are not… they have, like, a team of, you know, very experienced, you know, open telemetry folks, but they are not allowed to contribute or stuff, but they told me last week that they are… discussing internally how to… how to change the policies, so… so they could start contributing. So… so maybe… but it's not, like, next week. I think in the next few months, maybe we'll get something from that… that customer, because what they are doing with, in terms of infrastructure monitoring, standardizing on OpenTelemetry.
And now, getting logs with everything, like, so that would be a great use case, and it would be great to hear from them.
But they are not internally allowed to move forward, but…
**Dan Gomez Blanco** 24:17 Yep.
**Lukasz Ciukaj (Splunk Inc.)** 24:17 So I don't have any other customer that is… maybe we can try to get someone, announce it, maybe internally, maybe someone can help, I don't know.
**Dan Gomez Blanco** 24:27 Let me, let me go through.
Okay. I think, you know, I ran into the same issue as you with some of my customers as well, that they're, like, not, not allowed to share, basically. But yeah, okay. And then this one, I need to bring it up with the DevEx team. I don't think they have published any other… I've not really been following up lately.
But I don't think we have… no, okay.
Nope, nope, nope. So we've got Skyscanner, we've got… what else was it? Adobe?
Yep, and we've got Mastodon… Think… None other.
Huh.
I know that they're working on two others.
Tool.
Yeah.
Okay.
We'll reach out to them.
**Lukasz Ciukaj (Splunk Inc.)** 25:27 Okay, perfect.
**Dan Gomez Blanco** 25:29 We can see where we are. And then the idea here is, like, if it can go through that template and say, hey, you know, this makes sense, we can get it, like, reviewed by the folks that were writing the… the, the Blueprint, basically, the, sort of the reference implementations.
**Lukasz Ciukaj (Splunk Inc.)** 25:47 Okie doke.
**Dan Gomez Blanco** 25:47 Okay.
Alright, well, have a good rest of your day, hopefully… Thanks, man. …back into the office at some point.
**Lukasz Ciukaj (Splunk Inc.)** 25:54 No, no, I'm going home now, actually.
**Dan Gomez Blanco** 25:56 Fair enough. Okay. Alright.
**Lukasz Ciukaj (Splunk Inc.)** 25:59 Thanks, Dan. Let's stay in touch.
**Dan Gomez Blanco** 26:00 the effect.
**Lukasz Ciukaj (Splunk Inc.)** 26:01 They don't…
