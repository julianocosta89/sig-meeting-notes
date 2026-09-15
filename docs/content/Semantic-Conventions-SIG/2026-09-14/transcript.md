SIG: Semantic Conventions SIG
Date: 2026-09-14
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Trask Stalnaker (Microsoft Corporation)** 02:37 Happy Monday, everyone!
**Aryan Singh** 02:44 Hi, everyone. Happy Monday.
**Josh Suereth (Google LLC)** 02:48 Happy Monday!
**Hanson Ho** 02:50 Happy Monday, good morning, good afternoon.
**Trask Stalnaker (Microsoft Corporation)** 03:15 Alright, I can… I can drive this.
Bus… Alright, we've got a lot of topics.
Yes, we have Riccardo.
Let's jump in.
**Riccardo Magliocchetti** 04:23 Hi. Hi, everyone. So, I have this topic from a few weeks ago, where In Python trip, we received the PR, Adding to an HPP instrumentation.
Like, introducing the usage of, code attributes.
In order to be more precise on, where the code… Handling the spam we create is… And I'm not sure that's the correct way to handle this. And the issue we have is that HTTP route is not precise enough, because it could land, like.
Depending on the method, some part of the code or another could run, the very same path.
So, wondering if anyone has opinion?
If we are setting the wrong thing in HTTP route…
**Trask Stalnaker (Microsoft Corporation)** 05:33 Yeah, maybe you can, Do you want to share and kind of give us, like, explain… if you could explain that concept, because I'm trying to think through in the Java instrumentations.
I'm not quite sure what you mean by the route not being specific enough.
**Riccardo Magliocchetti** 05:57 Okay, so if, I don't think I have anything to share, but, like, I can explain a bit more. Like, I think on the jungle instrumentation, the route is, like, the path of the URL.
With the variables, like, like… Substituted with, like, ape solder.
the problem is that in Django, at least.
like, not only in Django, but in Django, like, the same… What is… what in members is called controller, can run more than one, URLs?
So, like, so for the same, path.
Where it could be, like, a function.
but can run for the GET method, one for the POST method, And something similar.
So, luck, like… With the span we create, We are precise.
To the path, but not to the specific part of the code that creates the span.
**Christophe Kamphaus** 07:13 I think you could also… have the same URL, the same… Endpoint, but with different content types.
**Trask Stalnaker (Microsoft Corporation)** 07:31 Yeah, okay, I think I understand what you're getting at. Yeah, so in the Java instrumentation, I think we have the same problem then, we just haven't noticed or bothered with it.
In that the… so we don't templatize the URL, right? But we do have, like, controllers have, sort of, templates for matching, But I think we're only taking the… essentially the URL template, and not potentially other factors, like the HTTP method or the content type.
Into, recording those.
though, I mean, the HTTP method would be captured in the telemetry, so that would distinguish it.
The content type, I mean, you have to opt… I think you have to opt into that, I forget.
**Riccardo Magliocchetti** 08:29 And I think it's recommended, or… Yeah.
**Trask Stalnaker (Microsoft Corporation)** 08:33 Okay.
**Riccardo Magliocchetti** 08:35 But, like, as far as I understand, the reporter, I think, very used.
To have a link to the class or me for the implement… like, handling the… the… the path in question. So, like, they really need, like, a precise, Reference to the code.
And so we're introducing the code.
**Trask Stalnaker (Microsoft Corporation)** 09:01 So, I mean, cert… certainly, I mean, it's totally… it… it's non… I think it's totally non-controversial to… Have an opt-in Mechanism to add the code attributes.
If that's the question.
All… but… and then, I don't know for… by default, that's maybe an interesting question, I don't know, Be curious if anyone has thoughts on capturing those by default.
like, today, our conformance… I think our ACTB conformance tests.
I think would flag those as, sort of.
attributes that are not part of the HTTP schema URL.
But it's a light violation, it's a very light violation, like, you should be able to… Add more detailed stuff.
**Riccardo Magliocchetti** 10:13 Okay, thanks.
If anyone has a comment.
or want to chime in the… chime in on the PR, you're welcome. Thanks.
**Trask Stalnaker (Microsoft Corporation)** 10:25 Yeah, nobody, nobody on the call has thoughts.
**Josh Suereth (Google LLC)** 10:37 You mean about opt-in versus not? Like, I…
**Trask Stalnaker (Microsoft Corporation)** 10:41 Yeah, whether… Default, capturing them by default.
Yeah.
**Josh Suereth (Google LLC)** 10:47 It's kind of like a decision for, like, what's best for users, you know what I mean? Like, if we feel… These are gonna be good. One thing we're adding, by the way, Trask, I don't know if you saw, for the conformance test and live check, there's this notion that you could have attribute groups that would be enforced across all spans, and you can have matchers now, where you could say, like, for this instrumentation, we want these attribute groups to be everywhere. So we could say, cool, for, Django, we're going to have, you know, function name, file path, and code line number attached to every single span that's generated.
My opinion here is this is starting to blur the line between profiling and observability. So if you do it on, like, one span, it's okay. If we put this on every span.
it gets a little bit awkward. So, like, I'm fine with this as an entry point, so I know where to go. I think that's the idea behind HTTP route. When I use HTTP route, it's me finding in my code where I need to start looking at things, right? If it's not obvious where to find that in my code.
But I… so, like, my opinion here on adding this by default would be it's okay if, like, the first spin Does it, but it's not okay if every single span is doing this, because now we're basically profiling, and we're using a technique that is not optimal for that.
You know what I mean?
**Trask Stalnaker (Microsoft Corporation)** 12:19 Riccardo, I did think of, something similar that we are doing in Java instrumentation, which is we do have an opt-in to capture a span for the route.
at the route, like the… the MVC layer, the controller, we call it a controller span, and we capture that, and we do stamp those code attributes onto that.
But since we… Semantic Conventions doesn't have the definition of a controller span, That whole span is opt-in.
**Riccardo Magliocchetti** 12:55 Thank you.
**Trask Stalnaker (Microsoft Corporation)** 13:08 Cool. Let's move on. Hanson, welcome.
**Hanson Ho** 13:15 Hi, so, thanks, Trask for creating the repo for the federated client-side Semantic Conventions, what, Martin and I, he's here as well, want to talk about is, is… Now that the repo exists, how do we, start creating a process, that is durable with… in terms of governance and process… and, you know, reviewing and accepting things in. The actual technicalities of getting a federal repo going is actually the easy part. I've got that working.
And everything. But… How do we make sure that what we put in is, is, is reasonable, at least in terms of the maintainers? Like, do we just talk about it and get it in? Do we have a very structured process, similar to the main one? Are there recommendations that we should follow so we don't go off the rails in terms of, hey, it sounds good, put it in, realize, hey, we should have a more thorough, vigorous process.
So that's the main question that we have, and I want to kind of bring it up in this forum to kind of get some advice.
**Trask Stalnaker (Microsoft Corporation)** 14:28 Yeah, so I can give my, thoughts first, and then I would love for Josh to jump in with, his. So… My feeling is that, you all are blessed as repo maintainers. Maintainers in OpenTelemetry are, you know, own that repo and that work, and don't… require oversight from anything? Like, you all get to decide.
The… one ask that, kind of, I had going into this was just to, like, your… have that authority, But I… my ask is if you can kind of stay connected with this group and stay… You know, bring us interesting things that might go outside of conventions in… that have already been defined in the Semantic Convention?
Just so that we can weigh in, In my opinion, if you all decide That, you know, you have good reasons to do something else after listening to… after discussing it, then, to me, that's… You all get to make that decision.
**Hanson Ho** 15:55 Awesome.
**Josh Suereth (Google LLC)** 15:57 Yeah, I want to add two things to that. One is, you have a set of namespaces that you own.
If you want to expand that set of namespaces, please make sure we know so we don't reserve them or send them to someone else. Like, this is… that's one of our divisions, right? It's like, you have a namespace, and you have… Not carte blanche, but like, you know, it's supposed to be very freeing, you guys can make decisions and bring interesting things back here.
The second thing is we do, and we're trying to make this really easy for you, but that set of policies around, like, naming conventions and standards around that, so all of those… we're trying to put those all in Weaver and have them automatically checked, so it's not a burden, but if any of those pass, and you're like, oh, I have to violate some principle.
and you think you should, come to us, because, like, it doesn't mean that you, that you have to find a different way. It could mean that, like, we have to update our principal, right? And that will be evolving over time, so make sure that when you have those checks, that you have them in a way that, like, Renovate is updating to latest version.
of the policies. That's… that's the part that I'm a little bit nervous about right now. We haven't really got that sorted, but as we do, and we work together on that, I think those are the two caveats I'd have, but the whole premise is that you own this area, you make changes rapidly, you bring it up rapidly, so unless you're changing the area itself.
Right? Ben, I think you're good.
**Hanson Ho** 17:25 So how do we have, namespaces that we own? Because right now, we have, you know, app. is… is when we put the… a lot of the shared ones in, but there are a handful of ones, in app.
Not to mention the ones that are already in the official conventions. Do those get migrated over? Do we get a new namespace that we own? Do old things get grandfathered in, or however… however…
**Josh Suereth (Google LLC)** 17:52 So what we.
**Hanson Ho** 17:52 John.
**Josh Suereth (Google LLC)** 17:53 what we did for Gen AI, you can probably mimic. I don't… how happy are we with that, Trask?
You think it's okay? Alright, I'll describe it first, and then you can… yeah. But basically, you deprecate all the existing ones in current Semantic Conventions and say they've moved, and where they've moved to, and then in your repo, you still have a dependency on Semantic Conventions, but you now own those namespaces. So they're no longer in General SemComp, they're in your repo.
**Trask Stalnaker (Microsoft Corporation)** 18:20 And you have a new schema URL.
So they are… Effectively, like, and you can re… you can decide what versioning scheme you want to use there?
If you want to, you know, reset at 1.0, go move forward. I forget, if Ludmila would know off the top of her head, but I forget what we did in Gen AI.
I think we continued, on the 1.X, just… we thought that would be least confusing for users.
**Hanson Ho** 18:53 Okay, cool, that's something you…
**Josh Suereth (Google LLC)** 18:55 There's a…
**Hanson Ho** 18:56 Yes.
**Josh Suereth (Google LLC)** 18:57 Yeah, and look at GenAI, because there's a flag you write in Weaver.
That will tell, like, downstream code generation and stuff that, like, this has been deprecated in a way that it's now somewhere else.
So that it doesn't cause a tooling explosion for everyone.
**Hanson Ho** 19:16 Awesome.
**Josh Suereth (Google LLC)** 19:17 Cool.
**Hanson Ho** 19:20 Martin, anything to add?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 19:22 Yeah, I was gonna ask, do we need, a separate… Meeting on the calendar for this? Or should we just use the one… the client instrumentation one. Hanson, do you have… Any opinion on that?
**Hanson Ho** 19:38 I think we should just use the original one, maybe do it weekly instead of bi-weekly, yeah, but we can talk about that.
**Trask Stalnaker (Microsoft Corporation)** 19:49 Cool. Awesome.
Yeah, yeah, let a, if you run into anything with the… when you're kind of templating off of GenAI, if you don't mind, DMing, Ludmila and myself, because the one thing we… we have not made a release out of the GenAI repo yet.
So, there may… we… Have probably some… hurdles left, possibly. And anyway, it would be good for us to hear any feedback or ideas.
**Hanson Ho** 20:24 What do you mean by release? Is there an official… version that people can say that GenAI Repo 1.0?
Right. We just use main?
**Trask Stalnaker (Microsoft Corporation)** 20:36 Well, people don't use it.
**Hanson Ho** 20:39 Oh, got it.
**Trask Stalnaker (Microsoft Corporation)** 20:41 There's no… there's no release, there's no tag out of it, so people are still stuck on the old ver- the last version, which was released out of the core repo.
**Hanson Ho** 20:53 Understood. Are there any other federated, repos that have had releases?
**Trask Stalnaker (Microsoft Corporation)** 21:01 I don't think mainframe… As… yet. I think that's the only other… federated one.
I think…
**Rüdiger Schulze (International Business Machines Corporation)** 21:12 That's correct, Trask. So mainframe is kind of, like, in the same situation. We still need to… You know, goes through a number of authoring semantic conventions, and then plan further of how to incorporate this into a release.
**Trask Stalnaker (Microsoft Corporation)** 21:30 Yeah, and we're… in Gen AI, we're kind of holding off, kind of on purpose, because we're doing massive breaking changes, and we want to… we don't want to kind of strew those out over multiple releases. Maybe it would be okay either way.
I think not a super strong reason.
But check… Ludmila did do some thinking around the release process and releasing, so we do actually have some workflows and some documentation and processes in place. We just haven't exercised them, so they may not work.
If my experience with GitHub, release workflows.
**Hanson Ho** 22:17 Cool.
I made some sample ones on my test repo, and they seem like they work, but who knows if they actually have all the required stampings and things, so we'll be doubly sure when we do it, if we're effectively the first one. If we get there first, I should say.
**Trask Stalnaker (Microsoft Corporation)** 22:34 Cool. Awesome.
Let's… Anything… any last things for the client?
Side repo?
**Hanson Ho** 22:47 I'm good, unless Martin has things… there's lots to talk about between Martin and me and the other maintainer contributors, so we'll come back to y'all for any additional advice that we need. Thanks.
**Trask Stalnaker (Microsoft Corporation)** 23:01 Fantastic.
Alright, let us… Move on to… let's see, James… I don't see… Light of approval of… Okay, span type.
Should this banking requirement be a must?
Okay… So probably just follow-ups once… I mean, this is… looks like it's gonna get merged, but hasn't been merged quite yet.
Dbsemcom can't be… To… oh, the schema.
Refinements… Alright, well, since James' not here, probably we'll need to follow up, in Slack or async.
Let's move on. Sven, hey!
**Sven Cowart (ElastiFlow Inc)** 24:15 Hey! Alright, I got a hopefully pretty quick one.
There's a discussion going on around… My… How to choose selection guide for network attributes.
That I'm working on, and… Do you mind if I share my screen real quick? It's probably best for you to see.
The reason I'm bringing… I'll ignore my looking at flights for a second. The… The reason I'm bringing it up here is because I feel like we're going back and forth, and I don't know if we're making much progress on deciding where it should go. So, it's probably good for… The maintainers of much of this codebase have much… a better say into where it goes, and maybe you have some obvious ideas based on prior knowledge. But to just quickly catch you up, what this is, is a… Rather… large… Document, helping people understand.
When to choose either client server.address.
sourcedestination.addresses, or network, local.network.peer address, and this guide will expand as we get into more L3, L2 things. So this is the… this is the full document here.
Originally, I put this into the general attributes Paged, because right now, that's where we have this bulk of… information.
Which, for me, just speaking from my own experience of getting into open deployment tree about a year and a half ago.
I never came here for a while, and I was confused about some of these things, because it seems so non-obvious that it would be in general attributes. So I don't think that's a good location. So then… Ludmila last week said, well, we need a network index page here anyways, so we're gonna add a network index page that'd be listed like these.
And so, for me, the logical place there would be to drop it into that network index page, so what would happen is we'd have, like, something like an introduction, and at the bottom would be this guide on how to select which attribute pairing to take. The only thing that feels awkward about that is because it is a cross… area conversation.
Like, it pertains to the domain of networking, all those attributes do, but, right, it does touch on source destination, client server, and network spaces. And so maybe that's a little bit weird to be there.
The other argument Is to put it into how to write Semantic Conventions.
That, to me, feels… Like, it does get into check common attributes type of thing, and there's some other language further down.
When it talks about, specifically, spans, and when to pick Like, it could fit somewhere in here, picking the right.
**Christophe Kamphaus** 27:14 No, I don't think it should be under how to write conventions, because that's how can we… Change the conventions themselves, not how can we use them.
**Sven Cowart (ElastiFlow Inc)** 27:25 I… I fully agree. If you don't mind leaving a comment on this PR, saying that, that would be useful. Sure.
Because that's kind of the main pushback I'm getting here, is that it should… like, it should be there. And I don't think that makes any sense. The other… And then these other two don't address the problem. And the fifth option here is that, What we could do, instead of having it as an index, like, in the actual top-level index page for network that I have to create, it would be just another document in here, like, how to… how to… how to, choose the network attribute pair, and then you link to it here, so it keeps this document short, and you can link to it in other places. But I can still link to it, even if it's just in here.
From other places. So, like, for me, the.
**Trask Stalnaker (Microsoft Corporation)** 28:20 Sorry, what was that last… I didn't follow… catch that.
option.
**Sven Cowart (ElastiFlow Inc)** 28:24 So it's either embedded inside of here, or it's a… another page inside.
**Trask Stalnaker (Microsoft Corporation)** 28:28 added inside of system?
**Sven Cowart (ElastiFlow Inc)** 28:30 No, no, sorry, I'm just using this as an example. I'm sorry. I'm using this as an example because the networking doesn't exist yet, because I'm creating.
**Trask Stalnaker (Microsoft Corporation)** 28:37 Yeah, yeah, yeah.
**Sven Cowart (ElastiFlow Inc)** 28:38 Right? So, it's either embedded in this top-level area… Page here, or it's another document that's just linked to here, and then… yeah, that's, I think, the conversation, but I'm also having trouble finding or justifying Alright, what should I say?
I'm having trouble… I… I don't, I really don't.
**Trask Stalnaker (Microsoft Corporation)** 29:05 I don't see a problem with the…
**Sven Cowart (ElastiFlow Inc)** 29:06 Conventions.
**Trask Stalnaker (Microsoft Corporation)** 29:08 I don't see a problem with the original plan, Ludmila's plan, of… Putting it in that network.
Page… It being cross… Cross… domain… Really bother me.
**Christophe Kamphaus** 29:33 Also, think that whatever solution we end up.
We probably will link to it from other places.
**Sven Cowart (ElastiFlow Inc)** 29:40 Yes. Yep.
**Josh Suereth (Google LLC)** 29:42 Yeah, I think the complaint about it, like nothing else, looking like this.
is… I mean, it's true that nothing else looks like this, but it's… it's okay for you to be the first one. Like, that's not a problem. Because, yeah, we… and… and I also agree, I think having this under generic attributes is so unfindable right now.
that pulling it out and putting it somewhere that's easier for people to find is a higher priority in my mind than consistency, and should be. So, while we should figure out how to make things consistent and all that, I don't think that this comment should be considered blocking. I think you should be able to move forward without it.
**Sven Cowart (ElastiFlow Inc)** 30:19 Okay.
Alright, thank you.
**Trask Stalnaker (Microsoft Corporation)** 30:22 We do have, like, code.
The code attributes?
Those are cross.
And I… if they don't have a top-level dock there. Maybe they should. I mean, they probably should.
**Josh Suereth (Google LLC)** 30:38 Yeah, I would say that I would put them in the same category as something that is under general, but should be moved somewhere easier to find.
**Trask Stalnaker (Microsoft Corporation)** 30:48 Oh, our code attributes in general right now?
**Josh Suereth (Google LLC)** 30:51 They were at one point, I don't know if we moved them, but they were… they were very hard to find when I first needed to find them, I'll just say that.
**Sven Cowart (ElastiFlow Inc)** 31:00 Okay, so if I have… if I can get the blessing here, then… which sounds like I do, to continue to move forward, then I will do that, because it… that, to me, seems like the most logical place to be as well.
**Trask Stalnaker (Microsoft Corporation)** 31:23 General attributes.
Okay, source code, yes. So maybe that's, Part of justifying the… like, if you want to explain in the comment that the one-offness of it is that actually it's not one-off, and we're going to… we want to do the same thing for…
**Sven Cowart (ElastiFlow Inc)** 31:44 Okay.
**Trask Stalnaker (Microsoft Corporation)** 31:44 Code attributes and thread attributes.
And…
**Sven Cowart (ElastiFlow Inc)** 31:50 Okay.
**Trask Stalnaker (Microsoft Corporation)** 31:51 Service Pure, like, we want to remove this.
Yeah. Junk drawer. And, so there is a consistency to it, to the plan.
**Sven Cowart (ElastiFlow Inc)** 32:03 Cool. That makes a lot of sense, and I actually do that in this PR. I just remove the whole section and put a link-like code attributes where it goes there. Very similar.
**Trask Stalnaker (Microsoft Corporation)** 32:17 Alright.
We don't have Ludmila, graph attributes… oh, yes.
This came up in… the GenAI, stability discussion on Friday.
Probably will need to… Wait for that discussion… Reviews on V2 blockers… Let's see, Oh, okay. I will.
When… let's see, am I gonna resource? Oh, probably Azure, probably Azure, okay.
I will take a look at that, but it's got the reviews needed.
And… Network core… Oh, I think… Sven through that, okay… Oh, Sven. Would you mind approving If you've… Looked at it.
We can't… you're on mute.
**Sven Cowart (ElastiFlow Inc)** 33:48 Yes, I would be happy to. I just got rights to do that.
Huh.
**Trask Stalnaker (Microsoft Corporation)** 33:53 Fantastic.
And just for everybody, actually, even if you don't have, like, Even if you're not an official approver, you can approve PRs, you just get a gray checkmark here instead of a green one. But the maintainers do factor those gray checkmarks in, to our decisions to, you know, bless and rubber stamp something and merge it.
**Liudmila Molkova** 34:23 Hello! I'm here.
**Trask Stalnaker (Microsoft Corporation)** 34:25 Oh, hey!
**Liudmila Molkova** 34:26 stuff.
**Trask Stalnaker (Microsoft Corporation)** 34:26 Good timing. Yes, yes. So, I think on your V2 blockers, Sven is going to approve the network one.
You're asked… For, I will take a quick look at this, but I… I'm probably… like, you've got the approvals, so I think you're good, assuming it's.
**Liudmila Molkova** 34:50 In fact.
**Trask Stalnaker (Microsoft Corporation)** 34:51 on Azure.
**Liudmila Molkova** 34:52 Butchers things quite a bit for… for this event.
**Trask Stalnaker (Microsoft Corporation)** 34:57 Okay.
**Liudmila Molkova** 34:59 Well, it doesn't change anything, it essentially deprecates everything useful about it.
**Trask Stalnaker (Microsoft Corporation)** 35:08 But yes, let's, let's talk about ref attributes.
Do you want to share? Do you want me to share?
**Liudmila Molkova** 35:17 Can, can you share? Yeah.
Yeah, thanks. So, the proposal here is to finally formalize the thing we have in Gen AI.
Around the rough attributes, initially introduced by somebody else, and I'm just trying to resurrect it.
I'm combining it with a special annotation for the unbounded size.
We have a few attributes in semantic conventions that are like this, the HTTP request response body, the… we have an attribute, turns out, for the original log record.
And we probably have more, but those three are obviously unbounded in… oh, the database query text.
In a sense that they are… like, instrumentation should limit, how much memory they allow it to take, and also, on the… telemetry pipeline, they can occupy unbounded size. I… been thinking about different ideas, if we can have it as an enum, like the expected size. I think it's impossible, and it's more importantly, kind of useless to know if it's a small or medium, what small medium means.
I think the important aspect is that they are effectively unbounded.
And… I'm proposing an annotation for this.
And then we can enforce all kinds of things. For example, that this attribute is opt-in.
I'm not enforcing it here, because the db query text is both recommended and unbounded.
But I'm proposing to… to not let these attributes be required, at least.
In the future, we can do other things. And, The other thing I want to propose, which is not part of this PR, is that we… well, it's part in terms of guidance, and this is what I'm here for.
To say that, for cases like this.
When things are unbounded in nature.
It's recommended to define an accompanying attribute, which is underscore attribute name underscore ref.
And then we can, record the pointer to this thing. This pointer can be something existing for the Like, in the… instrumented library.
So it's just some external, place where things are. For example, when AI returns your URL to something, you can potentially put this URL in attribute like this.
Or something in the pipeline can take the original attribute, upload it somewhere, and stamp a ref instead of it, so it's not on the telemetry.
And… this PR documents some guidance around introducing these refs. It does not introduce any refs, but I wanted to introduce them in the Semantic Conventions GenAI.
But they want guidance to be in this repo, because… It should be consistent, we should have a set of policies, I would like to have a set of policies for these refs things to exist in the shared Weaver packages.
Yeah, that's my speech, and we can evolve the sanitation value quite a bit in the future, because it's quite useful to track other things.
That may be… Not important on the OTLP, but important in the pipeline.
Yeah, and to mention the concern we had while we didn't merge it before, when Michael, proposed this is we… in GenAI, we debated quite a bit about, should we record, like, individual parts of the content and put ref and site complex attributes, or record the whole thing?
And… the… the motivation for the top-level thing is that, okay, we are going to use it for things like HTTP request body, which is a string. You may have additional conventions for the nested values inside complex things, but Offloading the whole thing somewhere else still makes sense.
**Trask Stalnaker (Microsoft Corporation)** 40:19 Any, any… format for the ref, or is it arbitrary? Like, is it supposed to be a URL, or is it gonna be just anything?
**Liudmila Molkova** 40:33 So the thing I'm proposing here is to just say it's required to be a string.
We can… try to force it to be a URI of some sorts. I think it's… it's a good idea, yeah.
**Trask Stalnaker (Microsoft Corporation)** 40:56 Prototypes? Is Python, some of the… any of the Python Gen AI instrumentation already… Doing something like this?
**Liudmila Molkova** 41:08 Oh yes, we have the whole upload hook, it's actually instrumentation time thing.
that instead of stamping attribute on a span, it would take the data and offload it to, let's say, the cloud storage or, local file. I'll put the link here.
**Trask Stalnaker (Microsoft Corporation)** 41:32 What are the current options as far as… or, oh, it's just a hook, and… Or are there any kind of pre-built-in, storage mechanisms?
**Liudmila Molkova** 41:45 Oh, there is a, there is a pre-built storage mechanism, I forgot how it's called, the FF… Pack… Fs… Yeah, F… S… spec. It's… the library that… essentially an interface that, has a lot of implementations, like logger providers, and, you, you get a link, you get a URL to a FSS, FSS spec thing.
And the implementation of this library, depending on what you configured, can upload it to any popular cloud storage, to your local file system, and so on.
I'll add details to the PR.
**Trask Stalnaker (Microsoft Corporation)** 42:32 Last question. Any, any collector pipeline, Prototype.
Interest.
**Liudmila Molkova** 42:42 I think Michael did the collector prototype, but I'll check what the status is of it.
Yeah, thanks for reminding me about the prototypes.
Trying to think of this.
**Trask Stalnaker (Microsoft Corporation)** 43:11 any broader… Yeah, if it applies to… oh, maybe the client, the client… side books… Let's hope.
**Liudmila Molkova** 43:22 Like, the crash dumps.
**Trask Stalnaker (Microsoft Corporation)** 43:23 Probably wouldn't.
Yeah, I, might be worth pinging the… client, side… Slack channel.
Yeah, awesome. I… I… I think it's… a very… useful.
feature.
Oops, I gotta not close that window so I don't forget about that.
Alright, cool, you have the next topic span name.
Design in YAML.
**Liudmila Molkova** 44:10 back off of it until next week, or maybe even I will be out for the next… Two meetings, sorry. I'll back off from it for now. Maybe if you want to take a look offline, it would be awesome.
I'm trying to formalize the spend name, but I need to drop off, like, you know.
**Trask Stalnaker (Microsoft Corporation)** 44:32 Okay, no worries.
**Liudmila Molkova** 44:34 Yeah, sorry.
**Trask Stalnaker (Microsoft Corporation)** 44:37 And our last topic, Aryan A.
**Aryan Singh** 44:43 Yeah, hey everyone, hi. Hi, so I was, like, reaching out here, because I raised this, Semantic Conventions, issue, which was… closed without any, response, and has been closed for the 10 days. So it's basically in the messaging side, and, areas.md says that messaging, areas.md marks messaging as inactive.
And need staffing, so I just wanted to know how can I get, some motion on this, Semantic Conventions. If you guys want, I can give you a brief of what I'm trying to do here as well.
**Trask Stalnaker (Microsoft Corporation)** 45:21 Sure, sure, why don't you, yeah, give us just a, kind of, very high level, would be great context.
**Aryan Singh** 45:29 Yeah, so my basic proposal is that I have two editions, which are into the spans of… so, first, let me get a step behind this. So, I was trying to see how we can implement distributed tracing when we are actually, instrumenting an APM application which, interacts with IBM MQ.
OpenTelemetry APM, which interacts with IBM MQ. So now, what I saw is in Java, since IBM MQ also uses JMS, I could see that there are spans already existing for Java. For others, they were not.
So I, just, read around and found that there is a field which is the MQCA queue manager identifier, or basically, which is the ID of queue manager. And in case of IBM MQ, one-to-one comparison is not fair, but we can imagine that a queue manager is something very similar to Kafka, Kafka's broker.
Okay, so I have the proposal, which has two editions. Number one is the field messaging.ibmq.QManagerid.
And this next thing is that I also want to, add one IBM MQ2Messaging.system enum. So this is what this, Semantic Conventions PR is about.
**Trask Stalnaker (Microsoft Corporation)** 47:00 And, okay, so you have… this… And… let's see… so, broadly, the messaging Semantic Convention Work is… is on hold.
Because we don't have a group working on it at this point.
But for small changes, we're… Can kind of one-off decide, whether we would take them in or not.
I was just trying to check… Okay, so this is… Oh, because you added the… I was wondering why it was so many lines of code, because you added the… okay, the… Okay.
So add IBM MQ…
**Aryan Singh** 48:20 So, basically, in case of Java, I can reuse the enum JMS, but not for other languages. So, for IBM MQ, I think we should, like, put a separate one. It's a pretty big product for messaging as well.
**Trask Stalnaker (Microsoft Corporation)** 48:45 Sue, what I can… Propose here is, I will, review it from the Java instrumentation, the prototype.
And… If it feels like… Something that… basically, we want to kind of sponsor and push for from the Java Instrumentation SIG.
then, I can propose Opening the Semantic Convention PR.
Reopening that.
**Aryan Singh** 49:24 You've only had one round of review on this PR, which was AI-generated.
**Trask Stalnaker (Microsoft Corporation)** 49:29 Yeah, yeah.
So if you can… So the dashboard says it's still pending… Yeah, if you can… get this back. Basically, our… the way our dashboard works is on…
**Aryan Singh** 49:51 Yeah, I'm new here, so…
**Trask Stalnaker (Microsoft Corporation)** 49:53 Yeah, we've got so many PRs that we need a little bit, more, better process here, so… Ibm… MQ is currently, waiting on author, so you can check this on the dashboard comment on your PR here, and it'll tell you, what you need to do to get it back into waiting on reviewers.
**Aryan Singh** 50:21 Got it. I did, push a lot of, stuff, like, on your comments, like, maybe yesterday. It should not be, I'll have to look into it, why is it waiting on offer? I'll, work on it quickly.
**Trask Stalnaker (Microsoft Corporation)** 50:35 Yeah, yeah, it just shows you the one, the one thing that it didn't get closed out.
So you can either address that, or if you… If this doesn't look right, you can always comment Dashboard Route Reviewers, if you think you've…
**Aryan Singh** 50:52 Okay, got it.
**Trask Stalnaker (Microsoft Corporation)** 50:52 Mistaken on anything.
**Aryan Singh** 50:55 Got it, got it. Perfect.
**Trask Stalnaker (Microsoft Corporation)** 50:57 Yeah, and we'll go from there. We'll see where… how that goes.
**Aryan Singh** 51:00 Yeah, sure. Thank you so much, Trask.
**Trask Stalnaker (Microsoft Corporation)** 51:10 Alright, we have hit the end of our agenda.
Anything… Else anyone wants to discuss today?
Cool. Well, great to see everyone.
Have a good rest of your Monday.
**Josh Suereth (Google LLC)** 51:34 YouTube?
