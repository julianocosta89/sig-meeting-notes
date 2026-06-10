SIG: CI/CD SemConv SIG
Date: 2026-06-09
Duration: 29 minutes
============================================================

## Zoom Recording Transcript

**Adriel Perkins** 02:40 Good day.
**neil yashinsky** 03:52 Oh, hey, Adriel, how's it going?
I was, a little worried I was the only one on this call.
**Adriel Perkins** 03:59 Odds going alright. How about you?
**neil yashinsky** 04:03 Can you hear me okay?
**Adriel Perkins** 04:05 Yes, can you hear me?
**neil yashinsky** 04:06 That's just fine, thanks. How's it going?
**Adriel Perkins** 04:08 It's gone. How are you?
**neil yashinsky** 04:10 Well said, well said, yes. Also, it is going.
Summertime, at least, so, you know, it's a little warm, but it's pretty nice. I'm from the, Metro Detroit area. How about yourself in Michigan?
**Adriel Perkins** 04:24 Virginia.
**neil yashinsky** 04:26 Oh, okay. Have we chatted before? Forgive me, it's been a little while since I've been in the hotel, calls or whatever.
Can't recall if we've chatted much before.
**Adriel Perkins** 04:36 Yeah, we have. It's been a while, though.
**neil yashinsky** 04:37 Okay, okay, thank you, yes.
Yeah, I went all in for hotel for a while, then I just pulled back entirely, not… Oh, what's the word I'm looking for? Yeah, just, like, not by choice per se, but yeah, Glad to be back, and thank you for, having better memory than me, out of that regard. Doesn't take much, frankly, but.
**Adriel Perkins** 05:00 Oh, no worries.
**neil yashinsky** 05:01 Yeah, I saw… so, are you, So I was looking through the events listing, And, oh yeah, here are our attendees. Is this still run by… is it, Alan? Is it the one who was kind of, our fearless leader here?
**Adriel Perkins** 05:19 So I lead the SIG alongside…
**neil yashinsky** 05:22 What are you saying?
**Adriel Perkins** 05:22 Don't, Tim?
**neil yashinsky** 05:23 Oh, Docan, that's what I was thinking, yes, okay, great, thank you.
Appreciate the reminder.
**Adriel Perkins** 05:32 Yeah, no worries.
Good to have you back.
**neil yashinsky** 05:35 Yeah, thanks. Yeah.
**Adriel Perkins** 05:36 This might be a light meeting. I have been gone the last couple weeks. Actually, like, the last 3 weeks.
**neil yashinsky** 05:43 Okay.
**Adriel Perkins** 05:44 And so, I'm… I'm actually catching back up myself.
**neil yashinsky** 05:49 I don't know if you see this per se, as volunteering, that's kind of the, the broad term that I kind of see my hotel work. It's not entirely volunteering, right? But sort of some… I mean, obviously, no pay, for me. Maybe you get a little pay, that'd be awesome if it was true, but I guess… I'm guessing not. But it's like, it happens in… so, you know, you have some time, you do it, and then all of a sudden.
no time, and it's the first thing to go, right? If you got, like, work and family and stuff, and like, up, onto your time, it's just like… She gets the first, casualty of busyness.
**Adriel Perkins** 06:26 Yep, I understand that one for sure.
**neil yashinsky** 06:30 And in some ways, it's kind of amazing we do as much as we do, considering how challenging it is to get things done anyway. Much less volunteer, aha, you know, whatnot.
**Adriel Perkins** 06:42 Yeah, the, Yeah.
**neil yashinsky** 06:51 Heh!
**Adriel Perkins** 06:51 Very good.
**neil yashinsky** 06:53 I do have the, the project board in front of me, whenever you felt like kicking that off, if you wanted to kick that off, if it's worth, spending some time on, or whatever you've got planned on your agenda, long may you reign.
**Adriel Perkins** 07:05 Yeah, I was hoping to get caught up to speed from Kristoff and, Alan. I don't think they're gonna be on today. I have been going through a lot of different emails that I've received over the period of time reviewing things. There's a few more things that I need to review.
But if there's something on the board that interests you, that you're curious about, that you would like to pick up, or something to that effect, I mean, feel free to ask questions about it, and we can chat about it for a minute, but I don't know that it warrants going through the whole board at this point in time.
**neil yashinsky** 07:36 Great, yeah, no, I mean, honestly, my involvement is, I would say, twofold, like, I'm just a big, if you will, fan, or even supporter, proponent of… Hotel, broadly speaking.
And I do have a project that I'm working on, we don't have to get into it, we can if we have time, that is basically, connecting people to OTEL. But yeah, I, for the matter of the conversation, don't have anything, I'm… I think this is the… the… This is gonna sound weird, but this is, like, the SIG that I like the most for just, like, hearing what people are working on, and without having any, if you will, dog in the race? Is that how it says? Dog in the race?
Horse in the race? Maybe it's Horse in the Race, but yeah.
Looks like Carlos joined, maybe. Hey, Carlos, how's it going?
**Adriel Perkins** 08:25 We can race dogs, too.
**neil yashinsky** 08:27 Yeah, yeah, true.
**Carlos Alberto Cortez** 08:29 Hey.
**Adriel Perkins** 08:29 Hey, Carlos.
How's it going?
**Carlos Alberto Cortez** 08:36 It's going, it's going, it's going. There's a PR that we don't have to discuss here, because it's relatively simple, and actually we need more eyes on the specification repo, and we should probably look for comments there. Let me… Basically, the agenda.
**Adriel Perkins** 08:56 Is it the, span processor one?
**Carlos Alberto Cortez** 08:59 Right, that one. Yes.
**Adriel Perkins** 09:01 Yeah, okay.
**Carlos Alberto Cortez** 09:03 Yeah, basically, Jim McD, approved of, well, the thing is that it's experimental, so it's a small piece for now.
It's a small piece for now on India. There are some comments, mostly editorial, I think, by Robert, and there were some latest comments by CEO about, details, and Yeah, I think there's nothing big, and I… I need to update, the PR based on the feedback, but in general, it's good. And it could be good that people in DC could review that.
just… we are sending the good signal that this group, you know, approves that. The other thing is that this is one of the potential alternatives. I mean, we need to, one way or another, This behavior to spam processor, these operations.
But, there was… you may not remember, or maybe, maybe you do, that In the current PR, we have 3 new methods added to a spam processor, but there was one more that Jack had proposed, which is a single one, and then you just provide the information as parameters.
Yeah, I don't know if… how people feel about that, and I didn't have time to work on that prototype. So yeah, anyway, just, yeah, we don't have to discuss that here. It's very minor, in my opinion, what I have now. So yeah, if it… if the current approach feels good, just put a symbolic comment there, or approval.
**Adriel Perkins** 10:31 Okay, yeah, no, absolutely, that was… I've been gone for, like, 3 weeks. I've just been way too busy to be able to… do anything open source related. I'm, like, back… way backed up. I've got, I think, like, 10 different AI-generated PRs that I have to review on the collector side. And so, like, anyway. We all know how that goes.
**Carlos Alberto Cortez** 10:52 Yep.
**neil yashinsky** 10:53 I might be able to help with that if you want.
**Adriel Perkins** 10:55 A little bit of…
**neil yashinsky** 10:55 Oh, sorry, go ahead.
**Adriel Perkins** 10:57 Yeah, yeah, for sure. If you want to, like, give a cursory review, that's totally cool. I can send you the query for it in GitHub. The… I guess my one… I haven't read through the… this was actually, like, the next tab open I had reviewed.
**neil yashinsky** 11:12 It's hard.
**Adriel Perkins** 11:12 other spec PRs for ENV carriers and the JavaScript stuff that I've been going through. I guess my one question is, like, for this processor, and I haven't looked through the example code yet in Java.
I've also purposefully forgotten how to write Java, so take that for what it is. It's gonna take me a minute to… to grok through the code, is what I really mean by that, but, how do we foresee, like.
So… I'll give you the example of GitHub, right? The GitHub events are, like, non-standardized.
Tons of garbage fields, tons of wildness that exists within the data structure.
How do we foresee, like, turning events like that into traces through the spam processor, while, like.
mapping the attributes and values they have to be able to figure… like, they even have multiple timestamp fields, right? How do we foresee being able to do that through a span processor without having to write a bunch of code that's, like, dedicated for… Converting those attributes, picking the right timestamps, understanding the data structure, etc.
**Carlos Alberto Cortez** 12:27 I think I wasn't aware of that, so if you have any documentation or piece code, I can review that, yeah.
**Adriel Perkins** 12:37 Yeah, actually, I can share my screen, because I have the example of it. So, I mean, it's not an example, it's in production.
I love the fact that the most… like, if I type GitHub, the… it's almost always exclusively the first result is the hotel conserve repository, if that doesn't tell you where I spend most of my time.
And life, like, on GitHub, it's usually this repo.
**neil yashinsky** 13:08 No competit goes unpunished.
**Adriel Perkins** 13:10 Yeah.
So, like, for example, so in the GitHub receiver, I have this thing called model.go, which defines, a lot of these I need to start to clean up, because we've got a lot of, like, the semantic conventions have been published since then, right? This predates a lot of the semantic conventions, so, like, I built a model and then used this as the thing. Not all of them will be deleted, right? Like, these are gonna get… They're gonna stay. But if you look here, like, we have two types of events that come from GitHub. We have workflow run events, and we have workflow job events.
Workflow job events are essentially child, spans of the workflow run events. The workflow run event is, like, the parent, and it starts the trace, and then all workflow job events deterministically get associated with the workflow run.
Trace?
And so, like, what we have to do is, like, figure out, like, hey, you know, is there… is there a service name? If there's not a service name in a custom property, we'll just use the repo name.
Or some custom attribute people set in config if they wanted a one-to-one relationship with a repository.
We do some adding of custom attributes, so there's this field in GitHub that says, like, on a repository, I can set forth a custom property, and it's just a key value… a list of key value pairs.
And I'll just add those as attributes, into the span. We'll then, of course, like, get the repo name, and attach it as the attribute VCS repository name, but this is, like, the most basic example, right? Like, I have to actually get the repository name From a specific field inside of the event to turn it into the correct, because this would be an entity attribute.
where the entity is the repository, and I need to make sure that that's available, right? And then I have to do that same thing with all of these different things, right? Like, so, VCS ref head revision, GitHub has no concept of, like, a semantic convention for that, they just use GitHeadshaw.
So I have to do this mapping pretty manually inside of the code, based off of the data structure, to be able to properly set forth, the, set the correct fields and attributes and statuses on each of the spans, and then I have to repeat that for workflow jobs, as an example. And I have to actually have to… not just workflow jobs, but I have to do that for steps, which are child spans of workflow job, events.
And so it's very complex, like, and maybe GitHub's not the best scenario, but, for this, but I think the GitHub is where this kind of originated from anyway.
Oh, how would I do that in, like, this span processor world, where it's… You know, how do I make sure that attributes are getting set correctly based off of n number of potential data models? How do I make sure that, spans are, or trace IDs are deterministic in such a way that, like, if there are children events.
They're associated with the proper trace.
How do I make sure that that waterfall hierarchy is correct? What is a… You know, child, what is a sibling, how do those fit correctly into the thing, and so forth.
**neil yashinsky** 16:49 Did you… oh, and Carlos, feel free to jump in, because there's almost no way you are less informed about this than me, but the first question that I have is, like, the… about abstraction and… and… Is the plan to have a GitHub, basically, client, if you will, that makes the connection into what we're looking at now?
Did you have that kind of scoped out at all?
Like, where the call was gonna originate from into the existing… Process as it exists today.
**Adriel Perkins** 17:25 Well, in today, so this receiver specifically listens to GitHub webhook events, because that's the only place you can get these from. Okay. And so, if you look at the test data.
these are all, like, actual events that were just sanitized, so a workflow run will look like this. This is the JSON event that comes over webhook to the GitHub receiver, and I transfer this thing and turned this into a span.
Alright.
Instantly.
**neil yashinsky** 17:56 And… I'm sorry, go ahead.
**Adriel Perkins** 17:58 No, go ahead.
**neil yashinsky** 17:59 So, I was just wondering if that span generation class, if you will, or whatnot, Is that… does that single… piece of code create all the events for, you know, for this GitHub source? Is that how it kind of works? Like, you know, you've got this as, like, gathers all the events, and then you pushes it into what you just mentioned?
**Adriel Perkins** 18:25 Well, so, in a GitHub receiver context, the GitHub receiver just handles all of this natively, right, at the receiver.
level.
In the spam processor world.
we would receive an event, whether it be via webhook, or whether it be just, like, a log receiver, right? Because logs are essentially events.
And then we would use the span processor to say, alright, we are going… well, I guess it'd be a connector, but, the span processor would then, create a span out of those events, and transfer it over into the Traces pipeline so that it can be emitted over a TLP, if we're talking about it at the collector level. Yeah.
like…
**neil yashinsky** 19:11 I'll contact.
**Adriel Perkins** 19:13 Go ahead.
**neil yashinsky** 19:13 Well, I was just gonna say, I think the question then is… For me, I would put it, between the… Emitter and the receiver, and so the emitter is… Pushing things that the receiver's smart enough to… And again, without seeing it, you know, I'm drafting in my head here, but I feel like, the span processor itself hopefully will receive the data in a format that makes its processing… Pretty straightforward, and not dependent upon the structure.
And I think that's really the key, is, like, pushing that event through the pipeline in a way that the configuration doesn't have to really think about it. There's some middleware, lack of a better word, you know, there's some… some… logical interface, on the GitHub side that's specific to the events coming there, thus the, I guess it'd be the ingestor?
on the pipeline before the… or the span… it's not the span processor, whatever calls the span processor, you were just saying. That, I think, should just have a thin layer of logic.
such that it can use the, you know, the input that it got from GitHub, and there's, enough metadata in the fields that it's sending over for it to be able to format it without having to really know too much about it. Does that make sense? It's very abstract, but… So the.
Swiss… go ahead.
**Adriel Perkins** 20:54 Yeah, I mean, I guess… I guess, Carlos, I'm looking for, like, more… Of the, like, actual how.
**neil yashinsky** 21:00 Totally fair.
**Adriel Perkins** 21:01 Just the abstraction?
**Carlos Alberto Cortez** 21:05 Well, I think that the problem there for me is that the spam processor is very general at this moment, and this is… so basically, there are two pieces, I would say, or let's say three, but… The two pieces that we need to do that, one is extending the spam processor interface, so we can actually have the actual processor that we need to send the data implemented correctly. And the second… and the third part is that this is only for SDKs. I don't think that this is meant to be used as a collector the way it is, so I don't know how that would have to be modeled there. As I said, this is only for SDKs, and yes, and there could be probably a limitation. I don't think that, there's any Documentation outside the collector repo regarding how, its processing has to be specified, you know, at the specification level.
It's only the collector, I think.
But, in that regard, what about we do this? Because I think we need to probably have more details. But what about next, Tuesday, I present some… my prototype of the collector, and you see how it works.
We still need to get these spam production updates happening, but at least I can show you what I have in my current prototype.
So you can see what's doing there, and then we can start thinking. But yeah, this is a very general stuff, and it's for the SDK only at this moment.
**Adriel Perkins** 22:40 Okay, and because it's for the SDK, then what people essentially have to do is write that transformation logic ahead of time, before it calls the SDK API?
**Carlos Alberto Cortez** 22:52 What… can you elaborate a little bit?
**Adriel Perkins** 22:55 So, like, they would need to manually build… their data… And do the data transformation first, before sending it over the API.
To the processor internally.
**Carlos Alberto Cortez** 23:16 Actually, no. Actually, what would you be doing is that, part of this, effort is that we will have an out-of-the-box processor that would do that. So, what users would need to do is simply have the spam processor that does this.
And then you just do that. They don't have to do manually any stuff. So every time, like.
And this is for Spence specifically only, so every time that… you create span.
You can configure that so you know When an event… event, no… sorry, events not anymore. When… but when an attribute was set, like, basically, you can think that what you are sending over OTLP regarding spans, you're sending the same, but using events. The same, like, you could reconstruct that at the… at the collector level. But yeah, this could be out of the box. You just have to add the processor configuration.
**neil yashinsky** 24:18 Oh, so that does the translation, the processor configuration does the translation in combination with the SDK code, such that when the span comes in, it just matches already, more or less?
**Carlos Alberto Cortez** 24:29 Kind of, yeah.
**Adriel Perkins** 24:34 Okay.
**neil yashinsky** 24:35 Sounds like there's work on the SDK and the configuration side in order to format the data O-L-T-P? Is it OLTP native?
**Carlos Alberto Cortez** 24:49 Yeah, I mean, yeah, I mean, configuration-wise, we don't need anything, unless you need to actually shape the output in some way. We… we shouldn't, I'm hoping, because it's just OTLP, standard OTLP. With standard semantic conventions, we will be defining.
But basically, just… you can think that what we are sending over OTLP for spans, it will be the same OTLP, the same, but instead of using the structs that we use for tracing spans, we will be using events, you know? And basically, they are equivalent using semantic conventions for logs.
But yeah, the SDKs have to add this processor, and this processor is not so trivial, by the way, because of a pair of reasons. One of them is that You may not want to track all this, every single span you may be creating, maybe you want to track only some of them.
Also, do you want to keep… because you have to essentially watch all the spans.
And it's like, do you want to watch, like, Any of… any of them?
**neil yashinsky** 26:00 Right.
**Carlos Alberto Cortez** 26:01 you see what's.
**neil yashinsky** 26:01 relevant, or…
**Carlos Alberto Cortez** 26:02 Right, so basically the current strategy that I have is that, that basically you define, like, a max buffer, so to speak. Like, I don't know, I want to watch for 1,000 spans. If you get more, well.
Sorry to bother, we'll not be watching that.
Yeah, so there's some… that's not gonna be trivial. It's not super hard, but not trivial, for sure. And that's something that every SDK will have to implement.
**Adriel Perkins** 26:27 Alright, yeah, a demo Tuesday sounds really good.
**neil yashinsky** 26:32 Perfect.
**Adriel Perkins** 26:32 I'm gonna go ahead and put that on the… the doc, I'm gonna just go ahead and create next week's.
**Carlos Alberto Cortez** 26:45 Yep.
**Adriel Perkins** 26:46 Meeting… the 16th.
And, I'm just gonna give you 30 minutes. That sound good.
**Carlos Alberto Cortez** 27:19 I think we need less, like 15, but yeah, because it's a very small thing, yeah, but let's say, yeah, sure, 15 or 30 is fine, we can adjust that on the fly.
**Adriel Perkins** 27:31 Alright, I'll put that for next week then, and then that way we have… It ready, and importantly, just on the list of things to obviously do. So, that'll be helpful, and I will, in the meantime, I will definitely review that pull request.
So that I can make sure that I'm not… like, I have the mental fortitude and context to be able.
**neil yashinsky** 27:58 It's actually…
**Adriel Perkins** 27:59 Ask reasonable questions.
**neil yashinsky** 28:01 You're brave, you're very brave.
**Adriel Perkins** 28:10 Thank you.
**neil yashinsky** 28:11 I will try and do the same. I'll hold up to your example. Attempt to.
**Adriel Perkins** 28:16 Alright, cool. Anything else?
**neil yashinsky** 28:23 Not for me.
**Carlos Alberto Cortez** 28:26 I'm fine.
**neil yashinsky** 28:28 Do you want to send over the… a link or two to some of those pull requests? By next week, I will have time to take a look at a few.
**Carlos Alberto Cortez** 28:37 Yeah, it's in the chart, but I can copy that with the agenda, but it's only one for now, yeah.
**Adriel Perkins** 28:41 Yeah, I'll send you the contribib one, as well. Let me… let me just pull up the…
**neil yashinsky** 28:49 Thanks for the pointer to the chat, Carlos.
**Adriel Perkins** 28:51 There's, listed, label, receiver, GitHub… Oh, I guess I had less pull requests than I thought. Oh, some of them aren't open, that's why.
**neil yashinsky** 29:02 Mmm.
**Adriel Perkins** 29:03 Boom got closed.
**neil yashinsky** 29:04 Oh, well, there you go. The system works.
**Adriel Perkins** 29:07 Yeah, not really.
**neil yashinsky** 29:09 It does work, I just…
**Adriel Perkins** 29:11 I mean, good to him in time.
**neil yashinsky** 29:14 Oh, they got up.
**Adriel Perkins** 29:14 Yeah, clothes is stale.
Right.
**neil yashinsky** 29:17 Alright, well, this is… that's, like, that's another system that sort of worked? Okay, maybe not. Oh, sort of. Okay.
Well, thanks for your fearless leadership, Adriel and Carlos. Always a pleasure.
**Adriel Perkins** 29:32 Yep. Alright, well, if there's nothing else, y'all have a good rest of your day, and we'll catch you next week.
**neil yashinsky** 29:37 Sounds great. Thanks. Bye.
**Carlos Alberto Cortez** 29:38 See you, Ciao.
