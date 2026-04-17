SIG: End-User SIG: OTel Blueprints
Date: 2026-04-16
Duration: 29 minutes
Zoom Recording URL: https://zoom.us/rec/share/yxDzT5IviI0KVcoaojTDf8ATwOd1MtcodaGRiK9bscn00vTEN1Hd6_18wmVeZ9dx.VltFSrDIWg2Cyad0
============================================================

## Zoom Recording Transcript

**Dan Gomez Blanco** 00:26 Hello?
**lciukaj@splunk.com** 01:24 Hi, John. Hi, Tiffany, how are you doing?
**Dan Gomez Blanco** 01:28 Good.
**Tiffany Hrabusa** 01:29 How are you, Lucas?
**lciukaj@splunk.com** 01:32 Can you hear me?
**Dan Gomez Blanco** 01:34 Yep.
**lciukaj@splunk.com** 01:35 Okay, sorry, I have an issue with my audio. Good, good.
I'm doing good. We have beautiful weather, North Carolina. It's actually the heat wave this week, which is something unexpected this part of the year, but we are, like, above 90s, almost entire week, it's beautiful weather.
**Dan Gomez Blanco** 01:52 Nice.
**Tiffany Hrabusa** 01:53 Wow.
**Dan Gomez Blanco** 01:56 I will be in Georgia next week, in Atlanta. I'm not sure what the weather will be like, I'm not… I've not checked.
**lciukaj@splunk.com** 02:03 No, I think it should be the same. Let me quickly check upon the weather… Yeah, it should be nice next week.
**Dan Gomez Blanco** 02:11 Nice.
**lciukaj@splunk.com** 02:12 Cool. Would you guys… would you have there some conference, or some customer meeting?
**Dan Gomez Blanco** 02:17 Yeah, conference, like, internal, but yeah, company. Conference.
**lciukaj@splunk.com** 02:24 That's true.
Nice.
So guys, I can only stay 15 minutes, because I have a busy day, a couple of other calls today, so I just wanted to give you an update that there's no progress again from my side, as I was busy with other stuff, like tax return and other things, so it was busy time again for me.
But this is on my agenda, for sure. I've seen the update that Tiffany created the page on OpenTelemetry documentation. We have now blueprints, and the placeholder is there, so I believe now everyone is waiting on me to actually create the PR and start working towards it.
So that's what I'm planning to do in the next few days.
So I will move the text that I have in Google Doc to the actual PR, And… but something I would like to clarify with you, I was thinking earlier today.
Give me a sec, so if I go to… I will share my screen, open telemetry… blueprints… Because then we have, How should I make it? I'm a bit confused, so let me share my screen. Okay, I cannot share my screen, or I can.
That's permissions.
Yeah, I need to rejoin. Sorry, guys, I don't have permissions to share in Zoom, so I'll be right back.
**Dan Gomez Blanco** 03:44 Okay.
**lciukaj@splunk.com** 03:49 In a minute.
**lciukaj@splunk.com** 04:19 Okay, I'm back, and I believe now.
I'll share my screen.
Hmm, can you see my screen?
**Dan Gomez Blanco** 04:35 Not quite. Still… but, yeah.
I could see that you were trying to shut your screen, but it was black.
**lciukaj@splunk.com** 04:42 Research.
Okay, I think it should work.
Blueprints…
**Dan Gomez Blanco** 04:55 Here we go.
**lciukaj@splunk.com** 04:56 Okay, perfect. So, we have now the page that is created, the blueprints and Reference Implementations.
there is a blueprint section, so how should I do it? I'm a bit confused, so there would be, like, a new article on the… and that will be just linked here? Or that must be the part of this page? So can you just guide me here for this?
**Tiffany Hrabusa** 05:23 Sure. So, when you create your PR, you're going to create a markdown file, underneath the Blueprints page. The page you're on right now.
in the URL will be right before there'll be a slash, and then the title of your markdown file will be there.
So you're creating a child page.
You don't need to make any changes to this page. Our Hugo build automatically adds links to any child pages that get created.
**lciukaj@splunk.com** 05:54 Okay.
File page, got you, okay. So it's like a sub-page, something like that, right? On this one.
**Tiffany Hrabusa** 06:00 Yeah, so this is intended to be a landing page, and then as we add blueprints, they will just, kind of just end up populating below that. Eventually, if we have enough, we'll have to come up with some kind of organization and matrix and all of that, but for now, I think just listing them is good enough.
**lciukaj@splunk.com** 06:21 But, I don't know, I mean, previously I was creating new blog posts, and there was, like, a… Nice process to do it, so does it work the same with the pages here?
**Tiffany Hrabusa** 06:33 Yes, it basically does.
**lciukaj@splunk.com** 06:38 So, so we have a data here, okay, no.
**Tiffany Hrabusa** 06:42 Sorry, no, it's under Content EN.
**lciukaj@splunk.com** 06:44 E-N…
**Tiffany Hrabusa** 06:46 docs.
**lciukaj@splunk.com** 06:47 Docs, yes.
And then we said…
**Tiffany Hrabusa** 06:50 There's a new section for guidance.
**lciukaj@splunk.com** 06:53 Guidance… And then we have blueprints. So, would you… I should create a new MD file here, right?
**Tiffany Hrabusa** 07:02 That's right. That's right.
**lciukaj@splunk.com** 07:03 Oh, okay, okay, gotcha. So that is, that is clear now. And then on this page, the link will be created automatically, or we need to update MD as well later to provide the link?
**Tiffany Hrabusa** 07:15 You… it updates automatically.
**lciukaj@splunk.com** 07:17 Okay, that makes sense. Alright, okay, I know what to do, so I will just move the content there.
**Dan Gomez Blanco** 07:23 In terms of.
**Tiffany Hrabusa** 07:23 If you… if… Sorry, go ahead, Tim.
**Dan Gomez Blanco** 07:26 No, go ahead.
**Tiffany Hrabusa** 07:27 I was just gonna say, if you want to, Lukash, when you create your PR, you can also remove that coming soon.
On the Blueprints file?
But if you don't want to deal with that, if you just want to create your markdown file, that's totally fine. I can come in after and remove that in a separate PR. But if you feel like it, you can remove that.
**lciukaj@splunk.com** 07:49 So just for me to better understand, so later, once we have this PR created and merged.
Here on this page, share this stuff. So, here, under this coming soon, we will have the links to the individual blueprints, correct?
**Tiffany Hrabusa** 08:07 Yeah, if you click on any of the other top-level pages, you'll see what that looks like. Like, if you click on just the word collector, sorry, just the top-level landing page.
**lciukaj@splunk.com** 08:17 Okay, collector.
**Tiffany Hrabusa** 08:20 If you scroll down to the bottom, you'll see what it.
**lciukaj@splunk.com** 08:23 It's like.
**Tiffany Hrabusa** 08:24 That's what it looks like.
**lciukaj@splunk.com** 08:25 It just hot.
**Tiffany Hrabusa** 08:26 It populates all of the child pages automatically.
**lciukaj@splunk.com** 08:29 Alright, I see. Gotcha. Alright, makes sense.
So I know what to do. I know that there is some work still needs to be done with the content itself, but yeah, let's at least have a PR created and then we can get others to review it and maybe contribute to that PR. So that is my goal.
And I know there is a little bit of the delay, so apologies for that, but as I said, it was… it was a bit busy time for me.
Hopefully now, we can move forward with this.
**Dan Gomez Blanco** 08:56 That's cool.
Just to check, you've… you've seen the template that we've got? There's a markdown template in the SIG end user repo?
**lciukaj@splunk.com** 09:07 Okay, I didn't see that.
**Dan Gomez Blanco** 09:09 So, I think this, this, again, you know, when… these are the first blueprints we're putting together, the process in place.
**lciukaj@splunk.com** 09:16 Right?
**Dan Gomez Blanco** 09:16 But now we've got a, and I can… I can babyshaw it. One second.
**lciukaj@splunk.com** 09:22 Yep.
**Dan Gomez Blanco** 09:24 Let me just open on your window.
Yeah, so we've got now… two things that you might, you know, want to have a look at. The first one is, if you go to architecture, friend template.
And as well, we'll have the from matter as well.
And I'm assuming that, yeah, this will work, basically, in terms of, like… I didn't want to develop.
The from matter for… for that, so that it shows in the… you can populate the link in the title, and the date, and author, and all that.
**lciukaj@splunk.com** 10:13 Okay.
**Dan Gomez Blanco** 10:14 But yeah, so this is just basically the temp… the same template that I already used, like, that I had… that we had reviewed. It's just no good.
**lciukaj@splunk.com** 10:23 Yeah, I think it's my Google Doc is structured in a similar way, so there will be no challenge to moving this under this…
**Dan Gomez Blanco** 10:33 Can we, from the reference architecture, well, we don't have any to link to, but I don't think any other blog posts.
**lciukaj@splunk.com** 10:40 them with reason.
**Dan Gomez Blanco** 10:41 released from Adobe.
Skyscanner or Mastodon have any non-Kates stuff, so, like, you don't, you don't have to, you don't have to add it here.
**lciukaj@splunk.com** 10:51 Okay.
**Dan Gomez Blanco** 10:52 Another thing that we have added was the… is if you come to issues now… You can then create a new issue, And a blueprint proposal.
**lciukaj@splunk.com** 11:04 Mmm.
And Zane's.
**Dan Gomez Blanco** 11:06 We'll guide people a little bit about the, you know.
The, to the template, and then to scope out… the blueprint proposal, and then from then on, like, you know.
We create an issue here, so we can track it.
**lciukaj@splunk.com** 11:21 This is good, yeah, like, a new category for issues, and also, like, the entire guidance, how to make it. Good job.
**Dan Gomez Blanco** 11:30 And we're… discussing now… I mean, we have already one for reference implementation, so… I mean, you work with customers as well, from, you know, from your, company, in the same way that I do, so if… now, basically, as we're putting together this process, and like, you know, we're now review… if you want to review this as well, feel free to… to do that. We're adding the template for the reference implementation, right?
So, this goes for anyone watching this recording as well, that may be working with… within users of OpenTelemetry. If you want to guide them to this, to share their reference implementations, then that would also be a good one.
**lciukaj@splunk.com** 12:13 Yep.
**Dan Gomez Blanco** 12:14 But yeah, this should hopefully be… Married to soon as well.
I guess that's the other… I know that we're segueing into something that was not in the list of topics, but yeah, so this is what I've been… working on, to put together this, template for reference implementations. A couple of comments here that I think are very valid, in terms of, Making them, perhaps, a little bit more… Well, the first one is, and I think… there is no… this is not contentious. I think we… we should link… In the issue templates, we're not really explaining What a reference implementation is.
Or… or anything like that, so I think we should just link to… to the website.
This is one proposal to do, to add a link, so you don't… let's say you're opening an issue.
And you want to know… what is a blueprint? What is a reference implementation? That should be in the website, other than we… Yeah, we can link there. The majority of times, I think.
What will happen is that people go to the website and then open an issue.
But I guess it could be the opposite as well, right? That someone opens an issue, and yeah, they don't know what they need.
**Tiffany Hrabusa** 13:33 Yeah, one other piece to that, to complete that kind of loop is, we also have an issue to create a README or the directory in the end user SIG. Just… we don't have to… we can link to the website, but we should give just, like, brief definitions of what those things are, and where to find more information if they want it.
**Dan Gomez Blanco** 13:58 Actually, that's a good question.
in here, then we should… what we're saying, we'll put a README here, right?
**Tiffany Hrabusa** 14:06 Great.
**Dan Gomez Blanco** 14:08 But I think we should probably refer to the website, or link to the website as well.
Right, rather than, like, trying to explain it in both places. Like, it's not… it shouldn't be a copy of what's in the website, right? That's what I'm trying to say.
**Tiffany Hrabusa** 14:21 Right.
**Dan Gomez Blanco** 14:23 Okay, cool. I'll… I'll take that on.
Well, if anyone wants to open up here, go ahead, but…
**lciukaj@splunk.com** 14:31 And what are the plans later to promote it? Because I believe we discussed that last time, like, having some blog posts or something.
**Dan Gomez Blanco** 14:37 Yeah, so there'll be a… so after we… we have the… the… I guess the… the, the process in place. That means that I wanted to get the template for the reference architecture, or for the reference implementation merged, and the issue templates in place, then we can, you know, change the advice on the website, and then I volunteered to write a quick blog post on what blueprints and reference implementations are, and where we're going with this, right? And then that will start to publicize the… the, The… yeah, the work…
**lciukaj@splunk.com** 15:14 That makes sense, yeah, I mean, because, you know, I believe that end users, they don't review the, you know, the SIG notes, etc, so having, like, blog posts the external article that can be shared or re-shared on LinkedIn, or maybe in some newsletters, I think that will help us to reach more end users, and maybe then contribute to the new blueprints and new reference architectures.
**Dan Gomez Blanco** 15:38 Yeah, I just didn't have to… I didn't want to, basically link to… you know, open up… create a blog post, and then not having the process in place, right? Yeah.
**lciukaj@splunk.com** 15:48 Yeah, absolutely, we need to have it first, but one suggestion, maybe, for the blog post later, when you'll be working on that, to have some diagram, maybe, like, you know, the blog diagram showing what is the process, right? Maybe, like, the visual process, I think that could help some people, you know, to quickly look at this, okay, I have an idea, I would like to submit the issue, let's say that this is a good blueprint, or maybe I want to work on this, or something like that. But I can help you with that, maybe, to review or provide some comments if you… if you start working on it.
**Dan Gomez Blanco** 16:16 I mean, I… next week, I will be at this conference by the week after. I'm basically taking, basically, that… that week to… To, to work on this, so…
**lciukaj@splunk.com** 16:27 Okay, hopefully by this time, we'll have a PR submitted by me, and maybe in this, you know, pre-merged status, so we can maybe coordinate that. So, I have that on my list now, I think I should have a little bit more time, so I will continue working on this.
And, yeah, let's keep moving forward with that.
**Dan Gomez Blanco** 16:46 Awesome.
**lciukaj@splunk.com** 16:47 Alright guys, I need to go for another meeting. Have a good one. Take care.
**Tiffany Hrabusa** 16:51 You too.
**Dan Gomez Blanco** 16:53 Cool. Alright, so the next topic, is the meeting time and date change, and I think we've got… 4… we had 5 respondents in the… And the, In the poll. And, 4 said, Monday.
8 AM Pacific.
So… yeah, let's go with that.
I'll confirm to Marilia, she just… I saw her message, but… Yeah, are we good with that? Yeah, I guess we're only two here, but, I guess, Lucas also said, yes, right, so, yeah, and hopefully we can get more folks at that time. It will be easier for… for EMEA, it'll be easier for, well, not sure if easier. 8am on a Monday is not easy for me, so, like…
**Tiffany Hrabusa** 17:47 I have a 7am meeting on Mondays, so I'll already be… It's the curse of the West Coast.
**Dan Gomez Blanco** 17:54 Good, good.
**Tiffany Hrabusa** 17:55 But, yeah, it works fine for me, so…
**Dan Gomez Blanco** 17:59 Good stuff. Alright, let's make that change.
And, yeah, let me… share my screen, and then look at the board. I don't think there's much to discuss, but Well, I think… We can close this one, actually, that's part. Yeah, so we… I just closed this one. I just saw that there, and it's like, we have agreed on… Ehh… I guess… I just… Copy the… the issues.
It's 246.
47… 2… 2, 4, 5.
That's cool.
Let's do that.
It's done.
Right, so… Yeah, we've got this in review.
We've got… this is in progress, this one is sort of in progress, yeah, as I said, next week, or sorry, the week after, will be when… When I was there.
Fully focus on this.
And I'll give that. My intention is that in… Yeah, so the week after, I'll create an initial draft, and I'll be able to share it.
I don't think we've got anyone here that has been… Yeah, I don't know if Kyle… Nice is…
**Tiffany Hrabusa** 20:00 So I think Alex is back from paternity leave, so I can ping them and see, If they're willing to take that up again, and if not, then to just comment and let us know.
**Dan Gomez Blanco** 20:12 Yeah, I think there were some comments on the… on the dock, And this one will be a good one to get the folks from the… So, spoke to… G-Corp.
about this, and he's trying to… well, not himself, I think more. The maintainer's trying to put together a chart that will do a lot of this stuff, and basically, like, the intention is that if we have the reference, or the blueprint.
And then with the blueprint, we can say, and a lot of these things are covered by this… Helm chart that you can just deploy.
Indo.
You know, implement that, that… the architecture, then that would be awesome, right? So… they'll definitely… we'll definitely want to get their… their point of view on it. I'm not sure if Jacob already… yeah, he's already commented on this, so… Yeah.
Good. This is just a scope, right? But, awesome.
So if you can ping Alex, that would be great.
**Tiffany Hrabusa** 21:10 Yep, I'm making a note. On a sticky note.
**Dan Gomez Blanco** 21:15 And… And this is what… I don't know… I don't… I might not have the automation here, but this was closed, right?
So we now have the guide, oh, that's still open.
No, that's the… that's the issue. So, sorry, this, this is… this was merged on the website.
**Tiffany Hrabusa** 21:38 Yep.
**Dan Gomez Blanco** 21:38 So we should…
**Tiffany Hrabusa** 21:39 I think you can close that one.
Yeah.
**Dan Gomez Blanco** 21:43 See if the automation is in place.
Does it close it I might not have any automations in this. Oh, no, it is, okay.
M… And I think both of these, right? Because they're both the same.
Blueprints and reference architecture sections have been created.
**Tiffany Hrabusa** 22:06 Yep.
**Dan Gomez Blanco** 22:08 Good stuff.
**Tiffany Hrabusa** 22:12 And then I will go back and… sorry.
**Dan Gomez Blanco** 22:17 No, go ahead.
**Tiffany Hrabusa** 22:20 I'll go back and add, like, how to contribute, or how to do that once, The last template is merged, and everything's in place.
**Dan Gomez Blanco** 22:31 Cool.
I think these ones keep them in draft for now. I think we probably need them, I just wanted to get, like, Something in there.
around, you know, Gather feedback from people that have gone through the process, right?
And see what we could improve. I, I, although.
Yeah, I'll turn them into issues at some point.
**Tiffany Hrabusa** 23:04 Okay.
I had it on the agenda, but we can just talk about it now. I know that I said that I would move the first DevEx blog post into reference implementations, but I just wanted to double check, because I… in between us having that conversation and me not doing that, I reviewed the reference implementation template, and I just wanted to make sure that you're okay with me just essentially copy-pasting what's in the blog post, and maybe tweaking the language so it doesn't read like a blog post, but essentially just copy-pasting? Is that okay with you? Okay.
**Dan Gomez Blanco** 23:43 Yeah, that's perfect. Yeah, we don't need to follow the, Yeah, the only thing is, like, adding the… Try to follow at least the front matter, like… Section? As in, like, you know… see what the… I think we… we had in there something, like, what's the… the date?
Like, maybe not in the front matter, but at the top of, of the reference I can.
**Tiffany Hrabusa** 24:06 Yeah, yep.
**Dan Gomez Blanco** 24:07 That's having, you know, this was… this was written by… Company X on this date, right, or something like that, I don't know, but… Something that tells us that it's a snapshot in time.
Rather than…
**Tiffany Hrabusa** 24:20 Got it.
Okay, and then the last thing is more of just an FYI, but I'm… I'm co-mentoring, Uzo, who is working on the Prometheus and… OpenTelemetry interoperability documentation. That's a mouthful.
But, we've kind of settled on one of her… objectives and outcomes being at least starting a blueprint. If it doesn't get merged by the end of her mentorship, that's fine. I'm not totally clear on what the direction on that is.
how… I know that's not one of the first three that we, like, agreed on, so how do you want us to approach that?
Should she just… Submit the issue proposal.
And we'll go from there, or do you want her to wait until the other ones are further along?
**Dan Gomez Blanco** 25:27 I think it would be a good idea to submit it and see if, you know, if, for example, we're explaining well enough what… what is a blueprint and what is not, and like… avoiding the, I guess, frustration for people that may want to share, like, you know, might want to create a blueprint, but then don't really know what the… what the scope should be, for example. Like, this is one of the things that was just… popped into my mind now, is like… is Prometheus interoperability by itself, you know?
we'll have to think about what challenges are we trying to solve with that blueprint, right? Maybe that's the… which is… hopefully that's what the issue template is guiding people towards, right? It's like, what…
**Tiffany Hrabusa** 26:10 Yeah, and…
**Dan Gomez Blanco** 26:11 myself, yeah.
**Tiffany Hrabusa** 26:13 I gave her, the template template, not the issue template. And I emphasize… I… when we were discussing this in our meeting.
I told them that we're actually coming at this backwards. Like, the idea of the blueprint is that you're addressing challenges, and then you work your way to the recommended solution.
In this case, we're kind of starting with the recommended solution, and we're reverse engineering what challenges those meet.
Arthur, who's one of the Prometheus maintainers, is my… one of my co-mentors, so he, I think, is going to guide her a bit more on the technical aspects of it, but… Yeah, okay. I'll encourage her to do some more research, figure out her plan, and then raise the issue using the issue template, and then we'll just see where it goes from there.
**Dan Gomez Blanco** 27:06 Yeah, I think as long as… I just think, like, you know, for example, let's do… maybe we should give some examples in the… in our documentation or somewhere. I was just thinking of, when is the blueprint scope too small, for example? When is it too big? Because maybe, you know, we don't… we don't have a good… Mentor model of that.
I mean, too small would be, like, here's how you configure the OpenTelemetry SDK for Java, right? That's not a blueprint.
Maybe if it only touches one component.
And if it only touches one, I don't know. It would be interesting to see what they think about. What components does this touch.
I don't know, for example, if it's only talking about… in the collector… Prometheus receiver, right? Then that may be to… too tightly scoped, but if it's considering all the parts of the toolchain and how it all fits together, I think a blueprint should cover multiple elements, right?
So maybe that's, that's something to think about.
is, like… What components are we… are we thinking that this would solve, or that this would help solving?
M… I'm trying to think from the application all the way down to… to collector, and even, like, the semantic conventions, right? For example, that would be a… actually an interesting… an interesting thing to… to discuss.
**Tiffany Hrabusa** 28:36 Okay, I will keep you posted on the progress there, but I'll relay this information to them so that they… They know where to focus their attention.
**Dan Gomez Blanco** 28:48 Nice. I actually think it would be, I mean, it can be a really cool idea, as in, like, a really cool blueprint.
Because lots of folks will have that.
that issue, and I do think that, and just thinking about it, like, a little bit more in detail, like, in my head right now, I'm like, yeah, there's probably a lot of places where, like, Prometheus interoperability is… Applicable, like, multiple things that we're trying to solve.
Not just, like, it's great metrics with a collector, right?
**Tiffany Hrabusa** 29:15 Yeah, I am learning a lot in this mentorship, probably just as much as Uzo is, because I don't know a lot about Prometheus, so…
**Dan Gomez Blanco** 29:25 That's cool.
**Tiffany Hrabusa** 29:26 Yeah.
**Dan Gomez Blanco** 29:27 Awesome. Alright.
I'll catch you later. I think we're done… yeah, there's nothing else that I would like to discuss, but, yeah. I'll confirm to Marilia that we're moving to 8am on Monday. Not next Monday, but the Monday after, right?
**Tiffany Hrabusa** 29:41 Right, yeah, the 27th.
**Dan Gomez Blanco** 29:43 27th. Yep, sounds good. Awesome.
**Tiffany Hrabusa** 29:46 Okay, thank you.
**Dan Gomez Blanco** 29:46 Mayor, to your point.
**Tiffany Hrabusa** 29:48 Bye.
