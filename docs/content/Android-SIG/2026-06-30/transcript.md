SIG: Android SIG
Date: 2026-06-30
Duration: 70 minutes
============================================================

## Zoom Recording Transcript

**Jason Plumb** 01:29 Hey, good morning.
**Jason Morris** 01:33 Hi.
**DavidGrath** 01:38 Good day.
**Jason Plumb** 01:40 Yeah.
Yeah, I know.
It's impossible to include all of it.
**DavidGrath** 01:49 Oh, no, sorry, I wasn't trying to correct you, I was just greeting from my own side.
**Jason Plumb** 01:56 No, it's all good.
Hey, Ben.
**Ben Joseph** 02:02 Hi, Jason, I guess.
**Hanson Ho** 02:08 Welcome back! Good morning, everyone.
**Jason Plumb** 02:13 Yeah, I got back from a week on Orcas Island.
And, yeah, I got back, like, 10 hours ago, so… And I haven't looked at anything OpenTelemetry related in a week.
**Cesar Munoz** 02:33 Hello?
**Jason Plumb** 02:34 This is her?
**Cesar Munoz** 02:35 Hey, welcome back.
**Jason Plumb** 02:38 Thanks.
Well, before we jump into Serbi's thing, I don't know, it doesn't look like she's here yet either, What did I miss?
Anything exciting happen in the last week that I should know about up front?
**Cesar Munoz** 03:03 No, I wouldn't say… so… We've got a… I think one PR… a couple of PRs that, you know, I already added some comments there, but… Some x-ray eyes are always… are always best.
And, there was a release.
I found the little book with that release.
Which is not huge, to be honest.
Azari, if I speak kind of a bit slowly right now, it's because I just came… come from the dentist, and they had to.
**Jason Plumb** 03:43 Oh, man. Yeah.
**Cesar Munoz** 03:44 I don't know what's the term, they had to, numb my mouth a little bit, so… I've been struggling to… to talk here.
Anyway…
**Jason Plumb** 03:53 Sorry, man.
**Cesar Munoz** 03:55 No, but it's fine. So… the, the vogue was that… due to some refactoring, the… we accidentally enabled one of the auto-instrumentations from core.
I added more… Details in the issue.
But…
**Jason Plumb** 04:19 Agreed.
**Cesar Munoz** 04:20 It's not like it's crashing or anything like that.
**Jason Plumb** 04:23 That's good. But yeah, we shouldn't have turned it on, so okay. So it's this one, I assume.
**Cesar Munoz** 04:30 Yeah.
**Jason Plumb** 04:32 Okay, do you think that warrants a patch?
**Cesar Munoz** 04:42 I mean… Yeah, yeah, probably. Yeah, because it's, like, it won't, like… Cause any, like, issues, let's say… In the app itself, but… It will add more data to your database. So, yeah.
You know, inadvertently, so…
**Jason Plumb** 05:08 Okay, and yeah, there could be some users that specifically don't want it, and now are getting it, so we should probably back that out. Okay.
So we can look at doing a patch release. It's also a good chance to test the patch release process.
**Cesar Munoz** 05:22 Sounds good.
**Jason Plumb** 05:22 I will say first, thank you for doing the release, I appreciate that. We were… getting pretty far behind, and I think you found out it was a pretty meaty release this time.
**Cesar Munoz** 05:32 There was a lot in there, yeah. Yeah.
But… good stuff. So…
**Jason Plumb** 05:38 Yeah, totally. So, thank you for doing that.
Is… did we get the milestone closed? Because I think there was one created.
And there's no issues in it, that's great.
**Cesar Munoz** 05:54 Yeah, I remember there was one issue, which was about bumping the off-stream versions, if I remember correctly.
**Jason Plumb** 06:01 It was 1-5, right?
**Cesar Munoz** 06:04 Yeah.
**Jason Plumb** 06:05 Okay, and then I think there were some PRs, so it's like, we need to take this one out.
Yeah, okay.
Cool. Yeah. How would one close a milestone? That's a great question. What is this new thing?
Look at this!
And they know what I like! Look at this!
Huh.
**Cesar Munoz** 06:26 Nice.
**Jason Plumb** 06:27 Cool.
**Cesar Munoz** 06:28 You didn't have to set it up, or…
**Jason Plumb** 06:30 No, it just appeared this morning, out of nowhere. I can go away for a week, and there's a new feature waiting for me.
**Cesar Munoz** 06:37 Oh yeah, there is.
**Jason Plumb** 06:41 Alright, Gosh, I am not firing on all cylinders, but that's usually the case at 8 AM. How do we do this again? So there's a way to close the milestone.
I think if we do the releasing, it links to it, right? I hope?
Milestone, list of active milestones.
**Cesar Munoz** 07:00 Oh.
Let me stop.
**Jason Plumb** 07:02 And then we can go… we can go like this.
**Hanson Ho** 07:04 Okay, nice. Yeah.
**Cesar Munoz** 07:06 Nice.
**Jason Plumb** 07:07 So the thing is, I don't know how to get here. So it's from Code Milestones, is it just on the sidebar?
Is it somewhere?
**Hanson Ho** 07:16 Is there a drop-down for that?
**Jason Plumb** 07:22 I seriously don't know how to get there.
**Hanson Ho** 07:26 Projects.
**Cesar Munoz** 07:28 Next up, we have it in the link.
**Hanson Ho** 07:30 Go to projects, and then Sidebar Milestone.
**Jason Plumb** 07:34 Huh, okay.
Thank you.
Kinda hidden.
Great, okay, cool.
**Hanson Ho** 07:46 Should we create one for 1.6, then?
**Jason Plumb** 07:48 Yeah, yeah. I think so.
The way we've been doing it, typically is we just have been creating them where we think it's needed, like, just as, like, an organizational step, so it's not like a… it's not a formalized, rigorous process around milestones, but sure, it doesn't hurt.
**Cesar Munoz** 08:17 Yeah.
**Jason Plumb** 08:19 And realistically, I mean, let's… let's call this the August release.
I mean…
**Hanson Ho** 08:29 Yeah, it's fine.
**Jason Plumb** 08:30 If it's the last day of the month and we're doing a patch release, I mean, realistically, I don't know. Let's just assume it's August.
**Hanson Ho** 08:39 I was just not even dated, I just, like, the 1.6 release. Yeah.
**Jason Plumb** 08:50 Okay, anything else that I might have missed?
Okay, well, please feel free to add yourself… please feel free to add yourself to the agenda.
As an attendee, and then if there are any other items you would like to discuss today… You can add them to the bottom of the agenda, and we'll go through them in order.
But I jumped… I jumped ahead of Servi, and it looks like Servi's here now.
**Surbhi Agarwal** 09:23 Hello?
**Jason Plumb** 09:24 Good morning!
**Surbhi Agarwal** 09:26 Good morning.
Should we.
**Jason Plumb** 09:28 Yo.
**Surbhi Agarwal** 09:29 Yes.
So, I… it has been difficult.
getting the semantic conventions group on board with the semantic conventions. I think my assessment is The main problem is they think that for server-side apps, these attributes can live as part of the span, and they don't like the fact that clients are a little bit different.
Like, iOS and browser, they receive this data asynchronously.
And there are other challenges, too.
I'll quickly share my screen.
**Jason Plumb** 10:12 Sugar.
**Surbhi Agarwal** 10:13 I have asked them… so the new guidance is basically, that… The new process is basically to create… Where did my… yeah, here is my Safari… okay.
So, the new guidance they gave me was, there is this new repo.
So here also… There… there is some conflicts with the already defined semantic conventions, like, for…
**Jason Plumb** 10:55 You're not sharing yet, Servi.
**Surbhi Agarwal** 10:57 Oh, I'm not sharing my screen.
**Jason Plumb** 10:59 Nope.
**Surbhi Agarwal** 11:00 Okay, sorry.
**Hanson Ho** 11:02 Oh, so…
**Surbhi Agarwal** 11:04 Screen now?
**Jason Plumb** 11:05 That's better.
**Hanson Ho** 11:06 For the… For those of you who are new, Serbi's talking about some spans and conventions, about, detailed timing of network requests, that, on the browser side are coming in asynchronously, and cannot be easily put into the span, because, well, it comes after the span is done, for network requests. So, Serbi and other folks are, creating a, an event.
That has these attributes, that effectively linked to that span, that basically have, have these things.
On Android, OKHTP, we have a lot of these attributes available, and then on web, they have, similar, overlapping set. So, this is trying to get, the semantic convention… get these new attributes into the semantic conventions. So, FYI.
**Surbhi Agarwal** 11:58 Thank you for explaining that, yeah.
If there are any questions, let me know as well.
So what had happened was they proposed a few options. One is to add it to the same span, one is to create a new parent span, and I looked into those things and have mentioned why that is not possible.
and why the event works, given the different nature of our US browser, and also the issue with closing the span later and possibly leaking the span, because semantic conventions also mentioned that the span should be closed when the header is received and should not wait for the asynchronous body read and stuff like that. And parenting is also an issue, right? It creates plus one trace level.
the parent can get leaked, the backend can just have the child and not the parent. Asynchronously, when browser and iOS receive this data later, that time they have to fill in the parent and add a parent ID beforehand to this, ex… or the… HTTP span, which they are already going to export. So there are problems with the suggestions that they gave us, right? So now they are mentioning that the way to go about it is to create a new repo, like this. This is one example they gave me.
Wherein you can experiment with such semantic conventions.
They gave examples of, like, interactions, is one space in client where… We do not have semantic conventions right now that could be a contender for such a new repo. I'm guessing perhaps session replay sort of semantic conventions could be a part of that. But yeah, they do not want to make a decision yet. I don't know why, honestly.
I would like them to make a decision right now, given the challenges with mobile. But yeah, that was their suggestion, so I wanted to, like, ask this group here, what are your thoughts on this? Have, like, do you think a new repo helps here?
**Hanson Ho** 14:14 So, I thought new repo was about just grouping existing semantic conventions differently, so that there's a different approval process. It still bubbles up to the same semantic convention, where we put it, right?
**Surbhi Agarwal** 14:29 rejection.
**Hanson Ho** 14:29 is simply the semantic invention existing in its current form.
what does putting in a different repo buy us? It's still gonna be called the same thing, right? We're not namespacing it by a repo.
**Surbhi Agarwal** 14:44 Basically, it buys them time to see how the new semantic conventions will get adapted.
And helps convince them that, yes, on server side, we should also tweak it, because that's the way to go on the client side.
I… I asked them to, because… the experimental and developmental semantic conventions from the main repo, they also go in a new artifact, right? Cemantic conventions Incubating artifact, not the main artifact. So I mentioned that we would create an experimental this is already in development or experimental in my PR. So, I don't think they'll like that idea either.
I have asked them to comment on my PR, I'm still waiting that comment. I'll let… I'll give you guys a heads up when they comment, if we want to discuss any further.
**Jason Plumb** 15:44 Yeah, so I have a little… I have some thoughts on this.
And I think there's a path forward, so I believe that GenAI, specifically, was peeled out into its own repo.
Because of the sheer volume and… frequency with which pull requests were coming in for Gen AI stuff, right? Like, this was happening… So quickly, with so many conventions, and the conventions are complicated, like, this is already, like, a very rich, complicated.
data… data model, semantic convention model, for these things, and so I think to help mitigate some of that insanity, it made sense to just try and carve off this entire massive subsection of what semantic conventions is.
Where instead of being pure, like, primarily focused on observing APM-style apps, you know, have all of this Gen AI stuff, which is, like, a completely new domain. And I think the same case can be made, and I think you might be… Or someone might be making the case that it's kind of true for client-side stuff, too. Like, it looks quite a bit different than APM-style, like, observability, Attributes?
And metrics and events. And so there might be room for us to have another repo that's specifically tailored for the domain of, like, client-side observability.
I do want to call out that I started this initiative in Android recently to start using federated semantic conventions. Serby, can I share again to show you this? Yeah. Okay.
And so, I'm not sure if you have seen this yet, but I opened this issue a couple of weeks ago.
And I… used my fingers to type all these words out, and I, I call out, like, why… like, what the challenge is, and, like, why we don't just start lumping stuff into SEMConv.
And what we can do about it, and how we can go forward, right? So, we have… A pretty significant amount of, like, baked in, inherited, donated… bespoke semantic conventions in Android that don't exist anywhere outside of our repo. They're literally, like, hard-coded event names, hard-coded attributes, and there's no convention for them.
So one way forward for that, for that, for Android, is to start creating, our local federated semantic conventions, which I've outlined here.
And if you haven't seen the Upstream OTEP, it's worth looking at, because it also talks about, kind of, the motivation behind this… In here… And the federation, I think, also applies to that new GenAI repo, right? I think that GenAI repo is using the federated stuff. I think they were the first ones, too.
We're… Definitely early adopters, they want more… Other… they want other repos, other focus areas to… think about using these, but we're still an early adopter for Federation.
But what I've done is I've broken it into… a couple of phases here, right? And we're partway through this.
I'm pretty fired up and excited about this, but we're a couple of phases, you know, into it.
And… When we're done, what we will have is a local copy, and this is kind of already starting.
I can show it to you.
So we have a SEMCOM module now, in Android.
And it has its own definition for attributes and events.
And these will then get created as… Attributes will be constants, events will be actual classes, and we can leverage those within our own repo.
And then we can work on stabilizing those. And if some of those overlap with iOS or browser, then in some cases, we can look at creating a… either another repo that we can all then borrow from.
Or include. I forget the exact definition of how you… how the Federation, like, builds on top of each other, but we're… we're definitely building on top of… I think it's… Is it in here?
Yeah, so you declare, kind of like.
This is the upstream model that we're using.
All of this is outlined in the upstream spec.
But you basically declare that you're layering on top of another, or compatible with another upstream… Semantic conventions entity to create that federated model.
So this is in its early stages, but by doing that, I think that allows us to do some of the things that we're hoping for, is, like, be able to move faster and do things that may not be so easily accepted into the main… semantic conventions repository, because they're too… they're too experimental, too controversial, whatever, and then we can let them bake, and if people start using them, I think over time that gives us… that gives anyone a stronger case for, like, including them. We're like, hey.
this is… this network event has been in Android, also adopted by browser. We've been omitting it for a year and a half. Can we… can we stabilize it in the main semantic conventions? Then I think you've got a stronger case. And they might still… they… I'm not trying to, like, you know, say they, like, if the other maintainers say, you know, it's still probably best suited to be in a client-side repo, then I think is the time that we would make You know, another repo that's dedicated toward client-side stuff.
So, I wanted everyone to be aware of that effort, because I think it's directly related to this, and it has a path forward. And I've said a lot of stuff, so what do you think?
**Surbhi Agarwal** 21:42 Yeah, so, like, multiple steps. First, like, individual platforms, like, maybe Android is doing its own, iOS is doing something of its own, perhaps. Browser is, I know, doing something of their own as well, in a different way. And then… Maybe a combined repo, the next step, if we think that it can be unified across mobile and browser.
And then… The problem I find with this is… Who's… what… how are those steps? Who is looking at those steps and saying, now, let's go to step 2, and let's go to step 3, and finally have it in the semantic conventions? We can drift a lot apart.
**Jason Plumb** 22:31 It's true. Yeah, we… I mean, it's up to us collectively. You know, this is, like… if you… if you want to take charge of that, I think you're welcome to… you're welcome to wrangle that… that, beast.
**Surbhi Agarwal** 22:43 Yeah.
**Jason Plumb** 22:44 Yeah. I mean, it's a good question, like, I don't think there… I don't think there is anybody, like, who…
**Surbhi Agarwal** 22:52 Is in charge, y'all?
**Hanson Ho** 22:54 the clients…
**Jason Plumb** 22:56 It really does come down to the client's SIG, but you know, it's so ragtag, right?
**Hanson Ho** 23:00 Yeah, the client… the client sync is… but this is exactly the type of project that the client sync would take on, because it does cut across all end user-facing app platforms.
I mean, I think my reservations is that we're kicking the can down the road if, you know.
if we're just saying, hey, there's this separate kind of thing that is kind of alike, but not quite. But maybe that's just the way it is, it's just gonna be like that, and maybe that's okay.
So, I think we should raise this in the next client's egg, but at the end of the day, somebody has to actually go and do the work. And I think that… that's more of the challenge. I think if somebody without even a SIG affiliation wants to take this on, I'm sure it'll get the right approvals if it looks correct, because that's all we want. So, That is the person we need to divine, and Seems a bit daunting, but who knows, maybe it's not. Maybe it's, it's fairly straightforward.
**Surbhi Agarwal** 24:02 Yeah, we would also need, like, maintainers from, like, if we were to create, like, a client repo, we would need maintainers from all three platforms, iOS, Android, and browser, to be the maintainers, right?
**Hanson Ho** 24:16 So we have…
**Jason Plumb** 24:17 Yeah.
**Hanson Ho** 24:18 We have a set of approvers already, for, like, the client semantic conventions, and I think it includes, I think I'm on it, Jason, you probably are on it, a couple other people are on it. So, those people would be… like, I would be happy to be a maintainer in this repo, if it comes down to it.
But if that is, like, the direction that they want to kind of move this in, basically have, like, an artifact-level separation, so, people pull in, you know, just the regular semantic conventions, won't even get this, even if it's marked experimental, who have to literally opt into this specific repo or subset. I guess that buys us a bit of, separation, so… Yeah?
**Surbhi Agarwal** 25:03 And there has to be some rules, like, you can't be redundant to what already exists.
**Jason Plumb** 25:09 Well, in.
**Hanson Ho** 25:10 Well, in some way.
**Jason Plumb** 25:11 Yeah, I mean, it's… it's… maybe a little bit complicated then, right? Because whatever we have will probably be namespaced in Android, and if iOS wanted to go do this, or Browser wanted to go do this, if they look at our example, or… okay, so the worst case scenario may be, naively, they don't even know that we have semantic conventions, right? Like, let's say they don't even know we've federated.
**Surbhi Agarwal** 25:33 Hmm.
**Jason Plumb** 25:33 Which they should, which they should, like, we've talked about it, but whatever. Let's say they don't, and they build their own thing, and it looks quite a bit differently. Like, if it, like, maybe they implement it as, I don't know, a span or something, and it looks completely different than the event that you've come up with.
then… then we have to sort of reconcile those, and that's gonna be the most work. But ideally, they would be like, oh yeah, we want network timing. I think Android has network timing, and they could look at what we've done, and they would go.
oh yeah, that's probably good enough, let's try it. And they could either source our YAML, or… or duplicate… our event structure in their own federated, and then we have… then we have this problem where it's like, yes, you've got duplication now, but at least you can sort of look at these two implementations and say, look, Android is, like.
approaching stability, iOS is approaching stability, they're basically the same thing. We want to go stable with it, can we do that in upstream SemConf? The problem with the two duplications is that they probably will be namespaced differently.
Right, like, whatever the prefixes are, because you're federated.
You have your own little namespace.
But if you have two that look the same in two or three different implementations, I think that's a compelling way to get to an upstream approval. And by that, I just mean, like, the main repo approval.
**DavidGrath** 26:55 Hmm. Like, I'm.
**Jason Plumb** 26:56 Unless there's some hard… sorry, last thing. Unless there's, like, some hard line that I'm not aware of, and it's possible, but if there's, like, some hard line where they're like, we're not gonna do client stuff, client really needs to be in its own thing, like, we're not gonna take any more into the main SimCon repo, which I haven't heard.
I'm just… if that were the case. Okay, I'm done, sorry.
**Hanson Ho** 27:15 Cesar's gonna say something, I'll say something after Cesar.
**Cesar Munoz** 27:18 Well, no, I was just gonna… Add that, even if, like, the duplication issue, it's… it's… it's… it's already an issue, anyway. I mean, it's like, we can still… I mean, we have already some specific event names and attributes that are only in this repo.
That might be useful for other clients, but… we have them scattered across the source code, and… and if anything, I think that what Jason is doing of putting everything in a single place Within the reboot, at least it's gonna be easier for… non-Android devs to… to find that, and to see if they can reuse something, so… I like this idea.
**Hanson Ho** 28:11 should we, like, right off the bat, have, like, a layer in between Android and the main that is just client? Because if we're gonna have a repo, it might as well… we might as well start with something that can be shared. Like, certain ones are obviously Android-specific, that we should dump there. The bar is lower there. But if there's one that… that we're trying to, at least, on the end-user client apps, arena, have some sort of alignment, we should have it there. Like, all the app device… all the app click and all that stuff. Really, if we have, you know, a federated repo, we should have a discussion there.
like, the mechanics of setting this up. Is it… is it… is it difficult? Or is it just a lot of approvals? Because…
**Jason Plumb** 29:06 Of setting up a new repo?
**Hanson Ho** 29:08 Yes, so, The semantic conventions you're setting up for Android is living in the Android repo, right?
**Jason Plumb** 29:15 Yeah.
**Hanson Ho** 29:16 Yeah, so I would assume that to do a client semantic convention repo, we'd have to create, or, semantic convention, federated, SEMconv thing. We'd have to create a new repo, and then basically do what you're doing in there, but putting it in the new repo.
it's probably worth bringing up next… next week in the, Client SIG meeting, because I… I feel like this could speed up, adoption. Not adoption, but, approval. So I think that's, you know, it's great to get a Serbi stuff in, but, like, as an aside, it's actually pretty good, in general as well. So it might just be something worth taking on.
**Surbhi Agarwal** 30:01 Yeah, I think they seem pretty convinced.
They don't like that client behaves differently to server, honestly, and they want us to, Prove ourselves via a lot of adoption and trial first, before we can make it to the semantic conventions, yeah.
**Jason Plumb** 30:20 Which I think Federations should help with, I hope.
**Hanson Ho** 30:24 Nope.
**Surbhi Agarwal** 30:24 Yeah.
**Jason Plumb** 30:25 Yeah.
**Surbhi Agarwal** 30:26 ANR crashes, all these don't have semantics, right? We can… like, mobile needs them, we… iOS and Android, at least. I'm not sure if browser needs similar, but that are good contenders also for that reason.
**Jason Plumb** 30:40 We have Cra- we have Crash now.
**Hanson Ho** 30:42 Crashes in there!
**Surbhi Agarwal** 30:45 I wasn't aware of that.
**Hanson Ho** 30:47 There's actually…
**Jason Plumb** 30:48 Four months or something.
**Hanson Ho** 30:50 Probably longer, but, yeah, my fault. The app… the app domain has a whole bunch now. I think there's… I looked at it, there's probably, like, 10 to 12 events.
I can take a look at… oh, God.
**Surbhi Agarwal** 31:05 Hmm.
**Hanson Ho** 31:05 I will try to take a look at, like, how to set this up, because if we're… if Federation acquires, like, a namespace affinity, we might have to, like, bring in, like, app or something like that into it.
So, it would be nice to have something that we could put there.
yeah. That might change the name, But, you know, it is what it is.
**Surbhi Agarwal** 31:34 I have asked them to comment on my PR with that guidance. When it rolls up, I'll… like, this week, before the next week 6 meeting, I'll keep you guys informed. Probably they'll throw in some information about how to go about it.
I think they are still defining it, like, they do not have a full proof process right now.
They were also discussing who should be the maintainer, and…
**Jason Plumb** 32:05 Oh yeah, I mean, that's… that's definitely a whole thing, like, I… I'm… I'm… I'm honestly… I don't wanna… I don't wanna sound like a downer, but, like, I'm skeptical about… there being enough momentum behind this. Like, we've seen kind of what happened with the client, Sig, like, there isn't, like, everyone's interested in, like, there's buzz about it, but there isn't, like, a real… strong leadership or steering of that stuff, and because of that, I think… I don't know, like, who is willing to step up and be a maintainer for such a repo.
And to be able to commit to it, and stick around long enough to really see it through.
**Hanson Ho** 32:43 That's the thing, like…
**Jason Plumb** 32:44 Yeah, if it happens, great, but like, yeah, I don't… Me, personally, I don't have cycles to take on another repo.
**Hanson Ho** 32:52 like, I would love, love, love to volunteer to do this, but I also know that, cycle's already limited, so unless I could, like, literally carve out day. Like, a day, completely. Not, not, like, I have that, but it's fake. But actually carve it out.
**Jason Plumb** 33:11 Yeah.
Yeah.
**Hanson Ho** 33:13 It's necessary, like, this is… This is actually quite necessary if we're… if we're able to do this, but… We can start asking, and then see if it… something shakes out.
**Surbhi Agarwal** 33:28 Yo.
**Jason Plumb** 33:28 Yeah, so Serbi, if you're willing to wait, I don't know how long it's gonna take to sort of get through, like, these steps, I think I'm, like… you know, I think doing these is not really, honestly, that much work, it's just, like, we kind of have to go through the process of doing it, but if you can wait a little bit until we've done events, which is really, honestly, like, step 5, then would you be interested in contributing that semantic convention to Android so we can see what it feels like?
**Surbhi Agarwal** 33:55 Yes, for sure.
**Jason Plumb** 33:57 Okay.
**Surbhi Agarwal** 33:58 Network timing one, right?
**Jason Plumb** 33:59 Yeah!
**Surbhi Agarwal** 34:01 Yes, yeah, it's already there, in the… I'll just have to create the same sort of files in here, so yeah, it should be quick for me.
**Jason Plumb** 34:11 Cool. Awesome. Well, let's… let's keep in contact about that, because I'm fired up about getting this, federated thing going. I think it's really… I think it's exciting.
I wanted to see, and you just reminded me, like, we can keep talking, but now I'm distracted.
Like, we probably publish these, right?
**Hanson Ho** 34:34 Well, in the… in the… the dailies, or the.
**Jason Plumb** 34:39 No, the last release.
**Hanson Ho** 34:40 Oh, yeah, we did, definitely, yeah, yeah, yeah.
**Jason Plumb** 34:43 Well, maybe not, if those classes don't exist yet. Do those classes exist yet?
**Cesar Munoz** 34:47 I think that's… in the VR that is still not merged.
**Jason Plumb** 34:52 Okay, okay.
We'll see.
**Cesar Munoz** 34:54 Also, I'm not sure if you added the.
**Jason Plumb** 34:56 Oh yeah, there's no… there's no… yeah, there's… yeah, that's the… that's the next phase. Okay, so next time. Okay, cool.
**Hanson Ho** 35:04 Extra motivated for 1.6 then.
**DavidGrath** 35:07 Get that in there. Oh, yeah. I also wanted to ask, is it ever possible that KMP and Flutter could throw a range in this thing?
And make things even more interesting to see.
**Jason Plumb** 35:21 Is it possible that what? What gets rearranged?
**DavidGrath** 35:24 that KMP and Flutter threw a wrench in it and make it more complex.
**Jason Plumb** 35:29 with KMP.
**Cesar Munoz** 35:31 In Flutter.
**Hanson Ho** 35:33 Are you talking about semantic conventions, or are you talking about.
**DavidGrath** 35:37 I talk about multi-platform, basically.
**Jason Plumb** 35:40 Yeah.
**Hanson Ho** 35:41 Right, but, are we… are you saying that there might be a KMP, semantic convention repo, or… or… or does KMP make… change this?
**DavidGrath** 35:51 I don't know, like, is it possible that maybe they potentially come up with their own unique brand of… brand of SEMCOV as well, or something like that.
That's still the.
**Jason Plumb** 36:01 Yeah.
**DavidGrath** 36:02 Everything else?
**Jason Plumb** 36:04 No, this is a really good question, right? Like, if we… if we end up… having… Well, okay, so the… the Kotlin… repo, the Kotlin SIG… there isn't a SIG, right? But the Kotlin… well, I guess there is a Kotlin SIG, but the Kotlin implementation, the API and SDK, typically does not include instrumentation And so, there's not really an expectation that those two things use semantic conventions in any way.
With a few exceptions, like… there's internal telemetry around exporters and stuff, but if you ignore that, then the API and SDK really don't even reference semantic conventions, and they, like, in concept, the architecture is such that they shouldn't.
**Hanson Ho** 36:53 Yet.
**Jason Plumb** 36:54 So then the question is, if Android, the Android repo, is moving to be layered on top of KMP, One day.
how does that impact us if we have our own federated semantic conventions, like our own androids Flavored?
And I… I think the answer is it doesn't, really, but if you were using… if you were… and I'm just trying to think this through out loud. If you were using the Kotlin implementation in a KMP scenario to target iOS, then certainly you couldn't… you would not be using the existing Android semantic conventions, there would… then there would have to be something else.
So that… I mean, I guess that does add some complexity, but I'm okay to tackle that at another time. It's good to be thinking about, I think it's worth bringing up.
**Hanson Ho** 37:40 At this point, if Android semantic conventions is something that others will consume, we may want to pull into a different repo. Like, maybe there should be, like, a client semantic conventions repo that contains, like, Android conventions, iOS conventions, the general client conventions, and we'll have, you know, a maintainer for that whole repo, and then, you know, have other maintainers for the specific or approvers, or something like that for the specific projects. Be a federated federation, or a federation within a fed… a federated federation? Something like that.
But that's, that's more… a down-the-road thing, I think.
**Cesar Munoz** 38:18 Yeah, but I think that's what they proposed survey, right? To do, create this client-specific semantic convention repo.
So yeah, that should be coming.
**Surbhi Agarwal** 38:31 I also like the idea that put in the Android, iOS, and browser folders in there itself.
And the common one. So, like, somebody can see this is where these platforms are drifting apart.
In one place.
Was that something you mentioned, Hansen, right?
**Hanson Ho** 38:49 Yeah, like… you know, having the client one be different than the server one, I can see… I can see the… there being, a difference, and intentionally saying, hey, if you're a client, then use this one. But, you know, the same event that exists on all platforms, on the end-user-facing apps, like, ought to have, similar conventions, and that's where the divergence, I think, is going to be most, apparent.
And also most problematic. So having something that unifies, like at the client layer, like the end-user-facing app layer or something like that, would be nice. Again, that's the ideal, whether we can get there with enough folks, maintaining the repos, that's, like, the second more practical question.
**Jason Plumb** 39:38 And I'm still a little bit fuzzy on how the Federation works, sorry, Cesar, but I think if the three platforms had their own semantic conventions, I think a client thing could pull them all in. It could build on top of the… I think it can build on top of those three.
And then have common ones elevated, and then separate ones would still be federated, if that makes sense. Sorry, Cesar, go ahead.
**Cesar Munoz** 40:01 No, yeah, I mean, that… Having these federated semantic conventions will actually be the first step to create a common one.
Because then we'll… we'll just grab them from what we see that has already been common… become common. Yeah, that's… that makes sense.
**Hanson Ho** 40:18 like, if Android starts off, depending on directly the root semantic conventions one, and then, you know, a couple months later, a client one comes in, Android could switch to that and basically inherit or derive from all the ones that are client as well. So you include the Android one, you get the client ones, and you get the main ones.
**Cesar Munoz** 40:36 True.
**Hanson Ho** 40:37 Assuming that's how it works. I'm just… again, I'm assuming that's how it works. Feels like that's how it should work.
**Cesar Munoz** 40:43 That's… I mean, it's something that we'll probably have to adjust as, as, you know, times… Passes by.
But the only thing that… This leaves me with is that the only thought that this leaves me with is that probably we should then Probably never.
mark federated, semantic conventions table.
That's really the only one question I have, because if at some point we know that when, you know, enough platforms use similar stuff, we'll… You know, gather them all in a common… Client semantic convention, then most likely the name will change.
So… So that… that will leave us with… with, you know, some breaking changes if we mark these federated ones stable.
**Hanson Ho** 41:38 Unless it's obvious that it's not gonna change. Like, some things are inherently tied to a specific platform. So if you have, like, you know, I don't know.
Android activity lifecycle. Android, you know, application,
**Cesar Munoz** 41:54 A&R.
**Hanson Ho** 41:55 Yeah, or… I was gonna say AEI, but I forgot what the EI was. But something that's, like, tied to the Android platform. It will never be bubbled up. It may become stabilized at the level it ought to be, which is Android. And maybe certain ones are, like, you know, app click.
you know, you're never gonna have, like, the very top, so maybe it will be stabilized in the Android convention, or the client convention, and be listed there. I think right now, we have all the app stuff in the main one, it's because there's no federation.
But, honestly, why would someone writing a server app want to include any of the ones. They just don't apply. So, I think this model allows the actual conventions to live, at the layer that is appropriate. So you're not gonna basically pull in the world just to have one.
So I think this model is correct. It's just getting from where we are to where we're gonna be, and I think the naming is very important, because it'll kind of signal where we want the stuff to land eventually, as stable.
**Surbhi Agarwal** 43:02 There's another…
**Cesar Munoz** 43:03 Check them.
Yeah. Go ahead, sir.
**Surbhi Agarwal** 43:07 Just mentioning that there's another layer, if I think about it, right? Sometimes iOS and Android, mobile can have something, but browser cannot. So we need mobile also as a category, which includes both iOS and Android and excludes browser.
**Hanson Ho** 43:24 If we get there, but, let's… let's do step one before we… but yes, I could see a world where things are so mature that there is something that's, like, native apps versus browser apps.
**Cesar Munoz** 43:35 I'm sure.
**Hanson Ho** 43:36 IoT or something like that might have, like, a separate one, or…
**Cesar Munoz** 43:39 I agree with that, too. Probably mobile is not a good name.
for that.
Maybe, but yeah, I know what you're saying. Survey, I agree.
**Surbhi Agarwal** 43:50 Hmm.
**Jason Plumb** 43:52 All ontologies are broken, and none of them are…
**Hanson Ho** 43:55 We're perfect, and… Oh, no!
**Jason Plumb** 43:59 What about mobile web? Oh… Yeah, I know.
**Hanson Ho** 44:03 Oh, you used the word ontology, now, now, now we're in the era where ontology has been introduced.
Great.
**Jason Plumb** 44:14 Yep.
**Hanson Ho** 44:16 The epistemological grounds for naming conventions.
I'll raise this in the, client, SIG, Slack, and maybe we'll get some people to show up next week to discuss.
**Surbhi Agarwal** 44:36 That would be great, yeah.
**Jason Plumb** 44:38 Yeah, I think it's a good… it's a good topic.
Do we know who the liaison right now for ClientSig is?
Is it Ted?
**Hanson Ho** 44:49 I think it's Ted.
**Jason Plumb** 44:50 Okay.
Might be good to get him in on this, too.
**Hanson Ho** 44:56 It'll certainly make the browser folks a lot happier if that process is tightened up.
**Jason Plumb** 45:04 Yeah.
We didn't… sorry, just to backtrack a little bit, sounds like we're gonna do a patch release. Cesar, do you want me to handle that? I'm gonna… I imagine most of my day is gonna be getting caught up.
But I could probably do that in the next day or two, unless you think you can get to it sooner.
**Cesar Munoz** 45:23 Yeah, no, I was actually gonna mention, that I'm gonna take off the rest of the week, so… Okay, I'll do it.
**Jason Plumb** 45:30 Yeah.
**Cesar Munoz** 45:31 Thank you. Also, I added a comment in your federated PR.
**Jason Plumb** 45:37 Yeah.
**Cesar Munoz** 45:38 Which is really just the technical stuff, so it's not a blocker, I'm just gonna approve it before I… before I go.
It's just, basically, if we had… if we wanted to have the generated sources you know, tracked in Git, or if we want to do, like, Protobuff does it, and, you know, just generate them at build time.
It's a technicality, it really doesn't matter much, so we can just go… I had a series.
**Jason Plumb** 46:08 Yeah, I think I was following what we're doing in Kotlin, which checks them into source code.
Which is kind of stupid, right?
**Cesar Munoz** 46:16 Check it in the source code.
**Jason Plumb** 46:17 I thought so. Doesn't this generate them?
**Hanson Ho** 46:20 Yeah, it does generate them, or there's a task to generate.
**Jason Plumb** 46:24 Yeah, they're, like, these are all generated.
**Cesar Munoz** 46:28 Right, but, like, also checked.
**Jason Plumb** 46:30 Yeah, yeah.
Yep.
They're part of this VR.
**Cesar Munoz** 46:35 I mean, no, I was asking about the cotling ones.
So, yeah, that was my question, basically, because it's usually the case that with generated code.
It's… it's not Git… it's not Git tracked.
**Jason Plumb** 46:48 It's a good question. I kind of don't like having these in source code.
**Cesar Munoz** 46:53 I can… I can take a look at it, if you like, on a follow-up.
VR or something, because…
**Jason Plumb** 47:00 Yeah.
**Cesar Munoz** 47:00 That will involve some great little shenanigans.
**Jason Plumb** 47:03 Of course. And this won't affect the patch release anyway, so… But I wouldn'.
**Cesar Munoz** 47:09 I don't.
**Jason Plumb** 47:09 I would like to see some of this land in 1.6 at least, so we can keep making progress.
**Hanson Ho** 47:15 single.
**Jason Plumb** 47:16 Yeah.
**Hanson Ho** 47:16 ideal.
**Jason Plumb** 47:17 What's awesome about seeing these now is, like, how silly some of them are. Like, some of them…
**Cesar Munoz** 47:22 The, the last, last attributes?
**Jason Plumb** 47:24 Yeah, exactly. Like, clearly the wrong land. Like, yeah, I was like, what?
So, but at least, you know, at least we have this here to look at and know how… how silly it is.
Where before, it was, like, kind of hidden. Go ahead.
**Cesar Munoz** 47:38 It was, yeah.
**Hanson Ho** 47:40 Oh, I don't think these are meant to be semantic conventions. Last screen name is clearly just an attribute without a domain, so… But yes, you're completely right.
**Surbhi Agarwal** 47:52 Perhaps it should have been screen.last.name.
**Jason Plumb** 47:56 You know, maybe, maybe so, because we have screen attributes, and we have screen.name, so maybe…
**Cesar Munoz** 48:03 Devin.
**Jason Plumb** 48:03 Screen.name.current, screen.name.c.
**Cesar Munoz** 48:06 Of course, now we're talking about it.
**Jason Plumb** 48:09 Yeah.
**Cesar Munoz** 48:10 Everything is working.
**Jason Plumb** 48:11 Exactly.
**Hanson Ho** 48:12 Well, this was brought up in the last, in the last, SIG meeting that you were here for, Jason, which is, how do we migrate, from no semantic invention to semantic invention?
Actually, no, I brought this up… no, right, wrong. This is the client's sake. because right now, we're basically have no semantic conventions for a lot of this stuff, and now we do. And if we decide to change last.screen.name to something else.
Do we do an opt-in, opt-out? We also talked about this, like, two weeks ago, right? Yeah, yeah. I don't know if we came to a decision, but I think more and more, I'm… my preference is that there's a… it should be Boolean, it should be default off, to basically go for legacy stuff. And if you want legacy behavior, you get legacy behavior, but anything new should be… SEMCON's V1, And not attribute per attribute, just, like, all or none, until the time where we get rid of all of them and get rid of this attribute, but until now, here's your fallback.
**Jason Plumb** 49:15 So at least in Java, they have a thing that you can opt into the new experimental names that have not yet stabilized, and what that does is it'll double, so you get both.
And I think the PR that I submitted a couple of weeks ago to do this… Because we realized that there was, like, especially around Crash, right? Like, crash was a breaking change. Like, when we adopted that semantic convention, we matched the semantic convention, we changed the event name. And any users of that event name would, like, have to adapt for that. Like, they're gonna be broken. And we don't want to do that without a major version bump.
So what we need to do is continue the default behavior as the same, meaning the default should be to Output the old name.
And I think you need to opt into the new names until we do a major version bump.
And there's a lot of, like, bookkeeping that has to go into that stupid process, but I think… At least that's what I should have.
done… With… there was a PR, let's see, is it a flag?
**Hanson Ho** 50:23 So, for crash, are we emitting two events, then?
**Jason Plumb** 50:27 No, we're not double, it's like you get either or.
**Hanson Ho** 50:30 So, attribute is…
**Jason Plumb** 50:31 We might want to change that, though.
Yeah, it was this one, I think.
So… what did I say?
**Hanson Ho** 50:46 Okay.
So the…
**Jason Plumb** 50:51 So the flag is, use the latest experimental, and by default, it's false.
If you opt into that, then you'll get the new names.
Which is a breaking change for you, but you have to opt into it.
And so, the mapper, there's some kind of mapping… Layer only has two, but that's the place where we can sort of do the bookkeeping and account for the changes.
**Hanson Ho** 51:17 Okay, cool.
**Jason Plumb** 51:18 So, any… we have to be… like, it's not universally used everywhere, like, I didn't wire it up to… sorry, I didn't wire it up to every… single usage, only the usages that are… were relevant. So, like, there's this thing called SimCon Compat, and it just has literally the mappings right here.
**Hanson Ho** 51:36 That makes sense.
**Jason Plumb** 51:36 And then you have to call map anytime you're using one of these that has changed. Which, in this case, happened to be, like, Fragment, for example.
So instead of just calling screen name, you have to map the screen name.
**Hanson Ho** 51:50 So, it doesn't do the double that you were talking about?
**Jason Plumb** 51:53 We in Android are not doing the double, because I think we're a little more sensitive to that than… Yeah. I think we're less resilient than maybe, you know, server-side Java APM users are.
But I'm open… I'm open to changing that and doing duplicate, and in fact, maybe we add another flag in here… that's, like, you know, use latest, and then… or, like, another one's, like, double published, like, use both. Like, I don't… there's… we have some flexibility in how we implement this.
**Hanson Ho** 52:24 No, that's good. It's good. We already have a way of getting in.
**Jason Plumb** 52:30 Yep.
Yeah, and sometime before too long, we'll do a 2-0, and then we can bump all this stuff forward.
I don't think there's anything in that milestone yet. There might be.
There's one… Okay, yeah, min SDK. So, you know, we're gonna need to do that at some point, and then we can bring all this stuff with us.
**Cesar Munoz** 52:54 I've already did that.
**Hanson Ho** 52:58 Yeah, I thought we did too.
**Jason Plumb** 52:59 Min SDK23?
**Cesar Munoz** 53:02 Yeah.
**Hanson Ho** 53:02 Yeah, because we talked about wanting to, be on par with play. I was like…
**Jason Plumb** 53:09 Oh, and play is already there.
**Hanson Ho** 53:10 I think so.
**Jason Plumb** 53:12 Okay… Which, this is… that would be breaking, though, right?
**Hanson Ho** 53:18 It would be breaking.
**Jason Plumb** 53:19 But it is in accordance with the policy we laid out, which is staying with play. But we should bump… I think we should bump majors on that. I hate to do it. And how many times per year is play bumping Min?
**Hanson Ho** 53:32 Oh, less than one.
**Jason Plumb** 53:34 Okay.
**Hanson Ho** 53:34 less than one. The fact… they went to 23 from 21, this was a few years. I think the last one was 19, or something like that, but… It's been a long time since 21. I want to say it's been 5.
5 plus years since it's 21.
**Surbhi Agarwal** 53:50 We could also introduce a flag, because we know it works on 21-22. If somebody really wanted it, they could turn it on. But then we have to ensure that everything works on 21-22 as well, if somebody were to turn that on.
**Hanson Ho** 54:07 Oh, if we bump into SDK23, there'll be language, usage, and API usage that would be, universally, allowed, and if you lower it, then it'll be disallowed, so it would be a breaking code change. I don't think we could flag it, but, So we did?
**Jason Plumb** 54:30 Yep.
**Hanson Ho** 54:35 The usage for…
**Jason Plumb** 54:37 It's… I mean, it's fine, this is back in March, and like, you know, we discussed it, we talked about it, we did it, and, you know, we should have, in hindsight, we should have bumped the major version, but, you know…
**Hanson Ho** 54:49 I mean… I would… I would…
**Cesar Munoz** 54:51 It's… it's… it's not… it doesn't happen that often, but it's not that rare.
it's… I don't know, it's almost as… well… Yeah, I… I don't know, I mean, it's fine, we can do, like, Gradle and just have major versions.
Every, I don't know, 2 years or so.
**Jason Plumb** 55:11 Or is one year. I think, I think one year, even, is probably fine.
**Hanson Ho** 55:15 I remember talking about this last year, and with you, Jason, about doing this, actually being a little less stigmatized about major version bumps. Yeah.
**Jason Plumb** 55:28 Yeah, I mean, it's not painful, but I think once you do it a few times, you get used to it. It's like doing a patch release, you know?
**Hanson Ho** 55:37 Well, I mean, we're running out of time, but what is the pain in bumping major version?
Other than we could kill some API.
**Jason Plumb** 55:49 The pain… yeah, the pain is supporting users that are not able to migrate, especially when there's security stuff. So there's some window of time during which you're supporting, you know, the newer version and the older version.
And we would need to write down, codify what that time is, and for how long we support it, but… In Android, it's probably, I don't know, 3 months, 6 months? We probably don't have to be that aggressive, and you just say that the old version only gets security fixes.
**Hanson Ho** 56:18 When was the last time we had a security fix? In the code, and not, not, not, not like one of the GitHub, or, you know…
**Jason Plumb** 56:26 I mean, it's always through transitive dependencies.
**Hanson Ho** 56:29 So for, if we're updating, like, old, like, like.
Java or, or, like, instrumentation. Once in a while.
Meh!
**Jason Plumb** 56:45 Yeah, I mean, again, I think it is valuable to sort of destigmatize it, or, like, be more comfortable doing major… major versions, but, you know, there's a process around it, and that just takes… just takes work.
**Cesar Munoz** 56:59 Yeah.
**Jason Plumb** 57:00 Yeah.
**Cesar Munoz** 57:00 I don't know if there's an open telemetry why Policy on, you know, supporting older, major versions. But yeah, that would be the one thing.
**Jason Plumb** 57:11 There is a…
**Cesar Munoz** 57:12 With minor version bombs, you're like, somebody has a problem, you just tell them to upgrade.
But with major ones, it's like, maybe they can't, so…
**Jason Plumb** 57:22 Yeah.
**Cesar Munoz** 57:22 You'll have to support them.
**Hanson Ho** 57:24 A lot of people…
**Jason Plumb** 57:25 the ju…
**Hanson Ho** 57:27 Go ahead. Sorry.
**Jason Plumb** 57:28 I was just gonna say, like, the Java API, for example, has been on 1.0 for, like, 4 years or 3 years, and they're trying really hard not to bump to 2, basically ever, because, like, it's API, it's, like, core, like, foundational stuff.
And they've been really, really careful about Using strategies to not have to make breaking changes and not do a major version bump.
**Hanson Ho** 57:54 I'm hoping… just because of the nature of the clients that we serve, Android apps, bumping majors are less problematic. People aren't going to be, like, using, you know, an old version 5 years from now, kind of thing.
Depends how destructive that is, I suppose, but.
**Jason Plumb** 58:16 Yeah.
**Hanson Ho** 58:16 Won't know until we try.
**Jason Plumb** 58:19 And if you didn't see it, Java Instrumentation is releasing 3, they're bumping to Major Version 3, like, in a month or two.
That'll be exciting.
Alright, well, thanks for a good session today, lots of active discussion, much appreciated, and .
**Cesar Munoz** 58:37 Thank you. I just wanted to quickly mention, since David mentioned Flutter.
that there is currently, I just sent a message in the chat, there is currently a SIG for a DART flutter that might be happening soon. I mean, it seems like… Everything's in place, and it's almost done, so… If you're interested, take a look at that issue.
**Jason Plumb** 59:04 Servi, wink wink, Serbi.
Tell some people.
**Surbhi Agarwal** 59:09 I'll be dependent on the Android repo?
**Cesar Munoz** 59:13 I don't think so, no, no.
**Jason Plumb** 59:15 It's gonna be its own thing.
**Cesar Munoz** 59:16 Yeah.
**Hanson Ho** 59:17 Yeah, the Dart SDK is its own thing that uses, well, Dart, and then the Flutter is built on the Dart part, so I guess… I mean, it'll be interesting because Flutter apps can go down to iOS and Android, but I don't think they'll be loading OpenTelemetry directly there. They may be doing instrumentation. Now they gotta figure out how are they gonna get it back? But that's… that's a… that's a different problem to… to… to sort out.
**Surbhi Agarwal** 59:44 Hmm…
**Jason Plumb** 59:47 Yep.
**Hanson Ho** 59:48 But…
**Jason Plumb** 59:49 Okay, Connett, thanks everyone.
**Cesar Munoz** 59:51 Thank you.
**Hanson Ho** 59:52 Right.
**Surbhi Agarwal** 59:54 Bye.
