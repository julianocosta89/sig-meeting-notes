SIG: Client Instrumentation SIG
Date: 2025-07-22
Duration: 31 minutes
============================================================

## Zoom Recording Transcript

**Hanson Ho** 00:54 Hello!
**Martin Kuba** 00:56 Handsome. How's it going.
**Hanson Ho** 00:58 Not bad.
How's the browser say, going.
**Martin Kuba** 01:05 It's yeah. I mean, it's picking up. I think it's there's yeah, I mean, it's still still very early stage stage. But but I think we'll we'll get get going soon.
**Jason Plumb** 01:21 I mean, this web thing is probably just a fad, though right.
**Martin Kuba** 01:27 Yeah, I mean, who cares? Right?
**Jason Plumb** 01:29 Yep.
**Hanson Ho** 01:32 Just wait 50 years. I'm sure something will be there to replace it.
**Martin Kuba** 01:43 You're trying a new look, Jason.
**Jason Plumb** 01:46 I am.
I'm not sure I like it. I know my wife doesn't like it, so.
**Hanson Ho** 01:52 Oh, I didn't even notice.
**Jason Plumb** 01:56 Yep.
Gotta keep them guessing. You know. You gotta you gotta keep them on their toes.
**Hanson Ho** 02:06 I accidentally set my razor to be too short to trim my beard, and kind of got it all off, but it's good when you'll have a really short, it just takes a few days and it's back. And it's like, Yeah.
**Jason Plumb** 02:18 It always grows back. Yeah.
**Hanson Ho** 02:20 Sometimes, sometimes.
**Jason Plumb** 02:29 Just grows back. White is the problem.
**Hanson Ho** 02:31 Yep.
**Jason Plumb** 02:32 Yeah.
**Hanson Ho** 02:38 Jason, you want to put in the metrics thing, or do you want me to do that?
**Jason Plumb** 02:41 Do that? Yeah.
**Hanson Ho** 02:42 Cool.
**Jason Plumb** 02:49 Yeah.
**Martin Kuba** 02:52 How are things going in the Android Sig.
**Jason Plumb** 02:58 It's been a little slow, like I feel like it's it's kind of dipped down since summer started.
There's still there's still people showing up and work being done, but it's like it feels slower.
**Hanson Ho** 03:10 Oh, one thing we should have talked about doing the Android Sig is that we've internally used the Kotlin Api not exposed it to anybody but internally, and had some benchmarking, so looks, looks good, looks fine so far. But.
**Jason Plumb** 03:31 Give some context here.
**Martin Kuba** 03:41 So is the is the Android SDK that you guys work on is that in Kotlin, or is that separate thing.
**Jason Plumb** 03:48 It's mixed.
**Martin Kuba** 03:49 It's mixed. Okay?
**Jason Plumb** 03:50 Yeah, we have an initiative to try and move everything to Kotlin.
I don't know that we've decided that that would be a precursor to 1 point. Oh, because it's still a lot of work. There's a lot left.
But yeah, we're we're chipping away at it piece by piece.
and most of the time new code. We encourage people to write Kotlin.
**Martin Kuba** 04:11 Okay.
And it's just like it's easier to manage or more like natural to android developers.
**Jason Plumb** 04:17 It's it's more natural. Yeah, it's more idiomatic for android developers.
**Martin Kuba** 04:22 Gotcha.
**Hanson Ho** 04:23 Compared to basically like Java, 8 slash Java 11, you know, it's also it's it's just nicer.
**Martin Kuba** 04:35 It's nice that you can make, mix and match, and just do it over time.
**Hanson Ho** 04:38 Yeah, it's totally fine. I mean, just compiles down to the same thing.
**Martin Kuba** 04:47 Okay? Well, I guess we have a couple of things on the agenda.
Think the 1st one is from Grace Grace.
**Grace** 05:00 Yeah. Hi, I think it's my 1st time in the client. 6. So just to introduce myself, I'm Grace. I'm from the Cloudwatch ROM team in aws. And yeah, my main question today revolves around.
what we're going to use for the telemetry on views in Ios applications. So like in Android. I can see that we're using screen.name, for you know all the activity and fragment spans and telemetry. I was just wondering if we had thought about whether we would also be using, like the same naming conventions for ui kit views and Swiftui views, or if we had considered something else. And the reason why I'm asking is because I saw what other providers have been using, and it seems like they have been doing something like view.name, and so I just wondered if we had come to agreement on kind of what we were thinking for this.
**Hanson Ho** 05:56 Is there a semantic convention for this? Or
**Jason Plumb** 06:01 I just. I just started looking, and I don't think there is.
**Hanson Ho** 06:04 I think the problem becomes really problematic, especially when we're talking about the the declarative uis, yeah, the the swift ui, and compose when there's like, not like a screen per se. It's you know.
you have work. We have, you know, things like destinations and and hosts, and the view tree. You know, the top doesn't move. So you're basically arbitrarily saying.
you know what is.
You know it and screen is sometimes what people use. People sometimes use something else, so I don't think so. I think settling in on a on a semantic convention would be good, so we could like, once we decide what to put in there. There's like a common one, I think, following the the so so view name is definitely, I think, out, I think in screen name is out. I think we have an app dot something, as most of our conventions are, so probably something like app dot something dot name So settling on that is probably the 1st thing to do is define a semantic convention if one doesn't exist. So, Jason, did you did you check that? It exists.
**Jason Plumb** 07:22 Yeah. The only reference to screen.name is in the closed Jank, Pr, so there's no other mention of screen.name. But we certainly do use it on Android like. That's what we put in the activity and fragment. Telemetry.
So yeah, I agree we we ought to. This group ought to. Make some recommendations and try and standardize around that. I I think about it from the perspective of a a user of a room product or any sort of mobile front end instrumentation view.
And how would you refer to that thing like if you you, if you were troubleshooting a problem you're like, well, okay, what screen are they on when it's crashing like? That's a pretty common mobile concern, or like, where do they? Where did they click on the screen when it like, it's like, you know, it's it's at least on Mobile. It's definitely screen, based on web. It might be different. But whatever you have your own signal, go figure it. No, I'm just kidding It would be cool to have a semantic image, and I agree.
And I mean, there is precedent around screen.name if we want to prefix it with app dot, because it's in the client namespace, then that's then that's cool, I mean.
I think, proposing that would be a good, a good start.
Grace, are you familiar with the semantic conventions repository?
**Grace** 08:46 So I've taken a look at it a couple of times, but I'm not that familiar with it. I just mainly double check to see like whether there are like conventions existing for what I want to add. But then I haven't done any more exploring.
**Jason Plumb** 08:59 Okay, yeah. So you're familiar with the basic concept, though, and just tell me to shut up if I'm over explaining. But I think The the intention is to be able to define attributes and metric names and span names in a way that that makes it consistent across different types of telemetry. So in this case, a screen name, and how we refer to that kind of collectively, universally, would be probably an attribute. It'd be like a piece of data that we had then attached to a span, or we attach to an event or a log that says like what what screen they were on, depend, regardless of how we end up finally calling it.
it would be an attribute, and I think that that's an attribute that could exist in the the way that the semantic conventions are kind of hierarchically broken down is like by what do they call it like? Is the name target? I forget. But there, there's a there's a bit of a hierarchy, there's a categorization of attributes for the registry.
And so we have this app one that's like kind of in its infancy, and I think what Hanson was proposing is maybe app.screen.name would be a good a good start to propose that. So?
Yeah, I think we're. I think this group would be open to that. I'm open to it.
**Hanson Ho** 10:12 Yeah. Embrace. Right now, we're trying to figure out what to actually call that because of of various things and and how to actually capture it. All the names are bad, so might as well just pick one and and you know we could bite shit all day on it.
**Jason Plumb** 10:29 Yeah, I am. Yeah. And I, I could probably take on that work. I don't mind initiating that bike shed. I'm gonna be doing that again for for this other event, which we can talk about a little bit in a second. Oh, I gotta remember this only a 30 min meeting now. Okay, so I can take that on if unless someone else wants to. Grace you brought it up, and I'm happy to let you do that if you would like to.
**Grace** 10:53 Like I, I can definitely take it. I'm just not as familiar with their process. So is there like a doc. I can reference just to get this started.
**Jason Plumb** 11:00 Yeah, let's find it. Let's pull it up.
No one's sharing the screen right now.
**Hanson Ho** 11:06 The last time I all I found were Prs. So to emulate hopefully now something.
**Jason Plumb** 11:13 I'll share my screen. Just so we have something common to look at.
If that's okay, Martin.
**Martin Kuba** 11:17 Of course.
**Jason Plumb** 11:19 Alright. So this is in the semantic conventions repository. The contributing Md. Is like the starting point. A lot of this is kind of boilerplate from other repositories.
There's kind of like there's like 3 main things to sort of know.
One is that if you add a new attribute, they, I think that that wants to be represented in the change log.
So oh, yeah, there's a this is like the biggest contributing and all of open telemetry, I think. But you can. You'll add an entry to the change log, and they do that by creating a new template in a directory.
So that's that's the 1st thing to know about is like new stuff wants to show up in the change log. The second thing.
is that the thing you want to create the like, the source of truth. The origination for this attribute definition wants to be in the form of Yaml.
So a machine readable definition. I'll see if I can find it. I'll see if I can find an example. So like, Hansen was saying, looking at other examples is like a good start. This one's a little bit big, but
**Hanson Ho** 12:27 I will warn you. There's a there's a lot of different files you have to touch.
**Jason Plumb** 12:31 The main thing we're gonna be looking for is this is kind of the hierarchy I was talking about is like there will be one here called App, and the thing you care about is registry.
So within registry, Yaml, and you can fully, just like crib off of an existing one.
the. And so for each attribute you will define an id, a unique id for it, which is almost the same thing, almost always the same thing as its name.
Oh, wait. This is a group. Okay, so let's here's an attribute. Okay, so here's its id.
And then it's type. This one happens to be an enum screen.name or app.screen.name is probably just a string stability, because it's new will be in development. There's 2 things a brief and a note. The brief is the description, and the note is like a supplemental like, here's a little caveat or or gotcha about this thing.
and that's it. So once you have. And this is all in the change. Log. Sorry in the contributing Md. I showed earlier. Once you have this Yaml defined, you can run some scripts that will then generate the appropriate Md. File. So the documentation. So all of the Md. Files that you see in here are auto generated from the Yaml.
And so when you're cruising through that, just know that the source of truth is the Yaml. There's some scripts to run to generate the Markdown, and everyone's pretty friendly, and will help you, especially if it's your 1st time.
**Grace** 13:58 Nice. Okay, yeah. I think I found this.
the doc in the semantic conventions repo. So yeah, I'll take a look and start from there.
**Jason Plumb** 14:07 I'll link it in the doc as well, just so that you have it handy that we all have it handy.
**Grace** 14:12 Alright sounds good. So if I get this started, should I join back next week to kinda prioritize it on the agenda.
**Jason Plumb** 14:20 Sure. Yeah, we're meeting every 2 weeks right now on the client, Sig.
**Grace** 14:24 Sure. Okay.
**Hanson Ho** 14:26 Feel free to just to join the slack and and just comment there. Because if it's if it's if it's you're looking for feedback on the the actual Pr and stuff.
you know, going on the slack, you'll you'll get more people, you know, on there.
**Grace** 14:40 Nice. Okay.
**Hanson Ho** 14:41 You have to wait 2 weeks as well. That's probably more important.
**Jason Plumb** 14:44 Yeah, yeah, there's a channel called client telemetry, or client. What's it called.
**Grace** 14:52 Client, instrumentation.
**Jason Plumb** 14:54 So.
**Hanson Ho** 14:55 Oh, client, side, telemetry, hotel, dash, client, dash, side.
**Martin Kuba** 14:59 Oh, yeah.
**Hanson Ho** 14:59 Telemetry.
**Grace** 15:01 Yeah. Oh, I see. Yeah, it's the one linked at the top right.
**Jason Plumb** 15:04 Oh, yeah, cool.
**Hanson Ho** 15:05 There you go!
**Jason Plumb** 15:07 Nice. Okay.
**Grace** 15:09 Alrighty sounds good. Thank you guys so much. I'll go ahead and get started on this.
**Jason Plumb** 15:13 Yeah, I think that would be super helpful. And you know, we'll we'll have to bike chat on them, I'm sure, for a little while, but it's it'd be good to have. Yeah.
**Hanson Ho** 15:20 They all suck. There's just no universal one.
**Grace** 15:24 For sure.
**Jason Plumb** 15:25 I mean, we also don't want to be in the app namespace. But whatever we decided that long ago, okay.
yeah, at least, it's not in 4 different places. Let's just pick one and whatever.
And let's talk about service name again.
Okay, if we're ready to move on from screen name. I'm I'm still driving, Martin so.
**Martin Kuba** 15:47 I actually have a question about the this screen name.
**Jason Plumb** 15:50 Yeah, get it?
**Martin Kuba** 15:51 Would you? Would you consider that?
A resource attribute.
**Jason Plumb** 15:58 I would not. No.
**Hanson Ho** 16:01 Not right now, I mean, if resources become entities and they become mutable, then potentially, almost definitely, because it's effectively a state that changes. But right now all we have are attributes.
**Martin Kuba** 16:17 Yeah. Yeah. But but you also, okay, yeah, the reason I'm asking is is because of the entity and entity provider work that's going on. That's in progress right now. So like, I think, for I think the similar thing that we have in web, I guess, would be like the page, URL, that you're on so like. And I. And I also wonder like if that would be something that you would send as a part of entity that could be updated as as opposed to like adding it to every signal. Yeah.
maybe eventually. But I was just curious. Like, if if you have an opinion.
**Hanson Ho** 16:54 Conceptually, I definitely think it should be it's effectively a state, right? Anything that is is a state like that ought to be coming from an entity, and and things like that. So.
**Jason Plumb** 17:04 I don't know. To me it seems too granular to be in it to be part of the resource.
but I don't think we really know where that line is. I don't think it's been defined right like in the old. In the olden days, like before, entities were a thing.
The resource was the instance of your application for its life cycle. And that was basically it. And.
**Martin Kuba** 17:26 Hmm.
**Jason Plumb** 17:27 You know we're making some changes to that.
but I don't know where that where it breaks down, because there are subcomponents of screen as well across every platform. And why not that one? And then it's at what point do you do? You stop?
And it's good.
**Hanson Ho** 17:43 So. So I mean that I mean, that was the second part of the question, which is like, what do you put in there? And that even harder is that because of the different your architectures like for web, you know, if you use URL, you know a single page app versus a multi page app, you know, you're gonna have problems like that for us. Similarly, with you know, multi activity apps or like a compose, you know, switch ui versus you know, different.
I forgot what they're called. But you know it, what are you trying to represent? And you know, I think when we look at this and we say, Oh, yeah, it's where the user is. But you know, do you do you make the the application set that, do you programmatically figure it out. And you know what are the limitations of one versus the other. And it's like, there's all these details basically so populating it is going to be, I think, a difficult thing. But let's just have something that just says, this is where the user is, and then just be very unspecific and say, Yeah, yeah, I know this is unspecific. That's the point.
**Jason Plumb** 18:47 Yeah.
**Martin Kuba** 18:49 Okay, okay, that was just a side question. Yeah.
**Jason Plumb** 18:54 That's cool, and it shouldn't change the semantic convention. Right? Like the attribute, is an attribute as an attribute. We get it defined. We agree upon it where it goes as as a separate concern.
**Martin Kuba** 19:04 Alright!
**Hanson Ho** 19:05 It should probably be very broad the way the Smash Convention is written for that.
**Jason Plumb** 19:10 Yeah.
**Martin Kuba** 19:11 Okay.
**Jason Plumb** 19:18 Because I I mean correct me if if my memory is failing me. But I think that like resource attributes and normal like span attributes are defined the same way in semantic conventions. There's not a distinction between them.
**Martin Kuba** 19:33 Yeah, I don't know. There's like, if I look at the the categories there's like a separate category for resource. But.
**Jason Plumb** 19:40 Okay.
**Martin Kuba** 19:41 Yeah, I don't. I don't know.
**Jason Plumb** 19:44 That might be it, then.
**Martin Kuba** 19:45 But then, but then, like some of the categories of like for events, there is an events.md.
**Jason Plumb** 19:52 Yeah.
**Martin Kuba** 19:54 I don't know. I don't quite.
**Hanson Ho** 19:57 I feel like if if there were a distinction between resource attributes and regular attributes with entities, they're gonna start to converge a little bit, because if we're talking about doing session, id as part of, or rather session is is, and and the provider will provide the session. Id, then, if that's gonna go into resource, you know that currently, it's it's basically in in in spans. And yeah, right in line.
So.
**Jason Plumb** 20:25 Yeah, that'll need to change. Yeah, if if and when that lands, yeah, that'll, I mean, it's trending that direction. It's just glacial.
**Martin Kuba** 20:34 It's yeah, yeah, okay, okay.
**Jason Plumb** 20:39 Okay, we have 9 min left. I want to jump into this topic so that people have a chance to at least have heard it and be thinking about it. Cause. This is something handsome, and I have been thinking about and discussing.
So I opened this very what I thought was a seemingly simple Pr a while ago, and it was to my intention here was to convert the existing Android 0 duration spans into an event for Cenk Santosh.
you're muted.
**scheler** 21:11 You can finish what you're talking, and then.
**Jason Plumb** 21:13 Oh, okay, okay, right? So what I thought was initially, a pretty simple spec for an event which is just like an event, name, and a few attributes it. It it it ballooned, I will say, into a larger topic with some reviewers, noting that something like an event that has a period defined and an a a time threshold, and it's reported with consistent an event that's reported like maybe consistently or on a regular period certainly feels like an like a metric.
and so rewinding a little bit sorry Jank in Android is when you've exceeded a certain display, rendering threshold so if it takes more than I forget the exact times 30 ms, or whatever to render a frame.
**Hanson Ho** 22:12 16 or 60. Megahertz.
**Jason Plumb** 22:16 So there, there's a threshold. Yeah, there's a threshold at which, if you take longer than that to to render, the user probably notices it and then reporting these to a rum rum thing is like pretty important because you can troubleshoot when the app is seemingly unresponsive to a user.
So, the commentary here being that this looks like a metric. Why aren't we using metrics? Why are you trying to spec this as an event, Jason, when you could just be using like a histogram or a gauge or something. And we talked about this at length.
and I decided to also do like this little straw man experiment, which is, can we make metrics that are usable in android like? Not necessarily for Jank, but really for anything. So the main challenge with using metrics on Mobile, as we've discussed, I think, previously several times, and I keep saying mobile, I just mean on the client side. Sorry I'm mobile on the brain, and I will continue aliasing those 2 things. But I do. I'm not excluding Browser here.
So the the point being that metrics by default in open telemetry, especially on on client side, are high cardinality. So by default, I just I made a metric and sent it to a collector and looked at the attributes that are on that thing, and the resource attributes include all of this information. And if you imagine this deployed across a million different clients.
The cardinality of this gets quite high, especially when you consider app versions, different versions of the platform, the operating system, etc. The cardinality is very high.
and then, you know, session also being included, would also make things extremely high.
And so this Pr was like, What's a minimal set that might be useful. The challenge then, with metrics, though, is you're looking at. Let's take Jank as an example. If if something like this were to land, what you end up with are is a gauge that is now blended or melded across all of your sessions for a bunch of different users, and it becomes very difficult.
It becomes impossible to troubleshoot maybe an individual session which is often what rum users care about, but it's also impossible to make any like informed, actionable decisions based on that data because you've lost insight by removing attributes.
And so there's a and I think Hanson did a good job of making this distinction between these point in time events that let you know that something bad or something interesting happened along a session timeline versus a continuous signal. If you have a continuous signal of dropped frames. You've got bigger things to worry about. If you really do need a gauge to tell you how many frames you're dropping all of the time. Then I think that's a different concern than a user was switching from screen one to screen 2. It felt sluggish. We dropped, you know, frames. For these 2 seconds we were switching between maps of this game. We drop some frames like that kind of stuff is like more actionable and more sporadic, so I'll leave it at that. I just wanted to say that there was some talk in that, and I will be introduced. My my intention, and I stated, this last hour is I will be reopening a new Pr to cover Jank. I'm gonna keep it as small as possible, and we can restart some of that discussion if we want to, and if it if it gets too hairy, then I may break that out into some sort of like Time Limited Working Group, because I do think it is important to try and capture Jank or dropped frames. And so I'm speed running this topic a little bit. But I want people to at least be aware that this is out there, and to be thinking about the cardinality of metrics on a client side platform, because it's it's bonkers, and I think there's not a lot of utility in it. But with only 4 min remaining. I want to make sure we give Santosh a chance.
**scheler** 26:14 Yeah, thanks. Yeah. I don't know if I've fully understand the the concerns here. But I I want to object to the client side RAM telemetry, you know, generating metrics at least a year plus ago, when we used to discuss with Nav, I I think at least there was, some agreement, at least in our belief, not in a in written form, that the client side, at least the browser, you know, we will not use the metrics. SDK, for multiple reasons. One you know, it increases the bundle sizes of of the client agents. But, more importantly, you know metrics is for at least for RAM. You know we we wanted it to be a server side concern, because, you know, take anything that the client side image, you know, you would be transmitting them into metrics on the server, anyways, for for most of them, if not all. So you count the number of, you know, page views like the number of you know, a any event you take on the client side. You want to count them, you know, either as a gauge metric or for latency metrics. Now you would, you know, build a histogram metric on on the server side. And lastly, the metrics. Api.
I'm not fully familiar, as some of you are, but I think it is quite comprehensive, and it may be overwhelming for RAM customers, for RAM clients to be exposed to the metrics. Api. So I suggest that we, as a principle, agree. Maybe we should debate if it's not well accepted. That we should stay away from generating metrics on the client side, stick to spans and events, and make metrics a server side concern.
**Jason Plumb** 28:23 So what do I think?
Go ahead.
**Hanson Ho** 28:25 So I think that's the conclusion we came to. So somebody said, Hey, we can do this as metrics, and Jason kind of, you know, plotted this out and and said how we do it. But I think you know, there are 2 main issues. One is that it's not useful. You know, having it pared down.
And and lastly, the most important thing that we need is the time aspect of it. And even if we can get the back end, the support as high cardinality dimensions, the lack of time and pinpointing. What, when this is perceived by the users, and what happened before and after makes this useless, so it may bark like a dog and look like a dog, but it its usage is not a dog. It's a human, you know, barking so so I think I think we've talked about this a lot, and Jason went in kind of tried it out, and I think the the conclusion is that this is not useful specifically for Jank. But I think largely for the same reasons. Santosh, you brought up because we we need to know when it happened, and and that basically says.
like, even if you know how many frames are dropped in within, you know, a particular session that's not useful, because the frequency of drops when it happened? And and you know not the aggregate number of frames. But, like, you know, is it? Is it all happening in the particular 2 seconds where thing freezes, or it's kind of just like drops like a frame every every second, and you don't even notice it, so like those 2 qualities makes makes munging them together as a metric useless. It's possible, but it's useless, so that, above all, I think, is why, this is not something that we'd want to do. And I yeah, I think I think, having an agreement for all the clients and say, Hey, until there's a like a use like an actually use useful use case we shouldn't even consider it, for for all the reasons that that you brought up. And so.
**Jason Plumb** 30:28 I wonder if this is worthy of some spec language like I think we touched on this before, like there's very little about client telemetry in the spec right now. There's probably some room for that also, maybe starting to dial in on what a session actually is. And there's room for that, too. So I don't know. Yeah. Saying, like a strong should not use metrics, I think, would be maybe worthy of of a spec entry.
But where would that out of time?
Okay, no. I appreciate that, Santos. Thanks for thanks for chiming in on that.
**Martin Kuba** 31:07 Yeah, I guess.
**Hanson Ho** 31:07 We all agree.
**Jason Plumb** 31:09 So far.
**Martin Kuba** 31:10 I guess we can continue the discussion and slack if you need to. So yeah, alright.
**Jason Plumb** 31:15 Cool.
**Martin Kuba** 31:15 Thanks. Everyone.
**Jason Plumb** 31:16 Thanks.
