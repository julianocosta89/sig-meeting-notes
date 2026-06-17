SIG: CI/CD SemConv SIG
Date: 2026-06-16
Duration: 48 minutes
============================================================

## Zoom Recording Transcript

**Christophe Kamphaus** 00:29 Hello?
**neil yashinsky** 00:31 Hey, Christoph, how are you today?
**Christophe Kamphaus** 00:33 Why not you?
**neil yashinsky** 00:35 Oh, very good, thanks for asking.
What's the weather like in… You're in, Europe, is that right?
**Christophe Kamphaus** 00:41 Yep.
**neil yashinsky** 00:42 Germany?
**Christophe Kamphaus** 00:43 Next to it, Luxembourg.
**neil yashinsky** 00:46 Luxembourg. Oh, okay, very good.
I don't, you know, I'd like to think I know a bit more than the average American about European geography, but I don't really feel like that's much of a distinction, if I'm being honest.
But I did play a lot of this, this, video game that did give me, a fun, fun, I'm trying to remember what it was, it was, like, a little… it was in the 80s or whatever, like, green screen helicopters, and, like, it was across, European theaters of World War II when I remember, like.
**Christophe Kamphaus** 01:17 Oh, yeah.
**neil yashinsky** 01:18 Yeah, yeah, obviously very, but I've… actually, that's been my, if you will, autistic special interest since, COVID, is, like, kind of, catching up on my European history, since I never really, studied that at all in school, and watched a bit of HBO's Rome, and a couple other, kind of.
history, what do they call them? Historical fiction shows, and yeah, got the bug.
**Christophe Kamphaus** 01:44 Yeah, there was, the Schengen Accords were signed in Luxembourg, so that's where you might know us from.
**neil yashinsky** 01:51 Oh, what a corpse, sorry?
**Christophe Kamphaus** 01:52 the Schengen Accords.
**neil yashinsky** 01:54 Hmm, remind me what that is.
**Christophe Kamphaus** 01:56 It's for free travelers throughout Europe.
**neil yashinsky** 02:00 Oh, yeah, okay, that makes sense.
Yeah, oh, and actually, it's like a principality? Is that a right way to describe Luxembourg? I mean, it's its own country, but .
**Christophe Kamphaus** 02:14 Yeah, it's its own country.
**neil yashinsky** 02:16 is it considered a principality? Am I using that word right?
**Christophe Kamphaus** 02:19 No, no, it's a proper country.
**neil yashinsky** 02:22 Oh, okay, okay, yes. Very… but, on the small side, yes? Among the smallest in Europe?
**Christophe Kamphaus** 02:29 Yeah, it's one of the smallest.
**neil yashinsky** 02:30 Which, you know, size, there's lots of things besides size that.
**Christophe Kamphaus** 02:36 Indeed.
**neil yashinsky** 02:38 Hey, Alan, how's it going?
**Alan Clucas** 02:40 Alright, how are you?
**neil yashinsky** 02:41 Very good, thanks.
**Alan Clucas** 02:58 Does that mean you're in Luxembourg, Crystal?
**Christophe Kamphaus** 03:00 Yeah, I'm based in Luxembourg.
**Alan Clucas** 03:02 Okay.
Life.
been through briefly, but quite a long time ago. Been to all the neighboring countries multiple times, but… Yeah.
**Christophe Kamphaus** 03:29 Yeah, we have a lot of tourists coming through our country.
**Alan Clucas** 03:39 The most famous thing, I think, recently was, he got completely free.
Public transport everywhere, is that right?
**Christophe Kamphaus** 03:46 Indeed.
**neil yashinsky** 03:47 Oh, wow! That's very cool.
**Christophe Kamphaus** 03:49 No, it was, it was in all the press, pretty much around the world.
**Alan Clucas** 03:55 Yeah.
**neil yashinsky** 03:56 And, from your opinion, has that… it looks like you think that's been a good move?
Or, sounds like.
**Christophe Kamphaus** 04:02 Yeah, it has simplified a lot of things, but then you also have downsides as well, so… Yeah. You might see some people in the bus you might not want to encounter in other places.
**neil yashinsky** 04:12 Right. I know, like, in New York City, like, they spend more, policing the turnstiles than they actually do collecting the money. So it's, like, just a net loss.
But, yeah, I mean… I'm, I'm from, if you will, the poster child for terrible public, transportation, Detroit, Michigan. Well, area, not in the city properly. And, yeah, it's, It's pretty bad! It's pretty bad.
But, yeah. And that's why I think, actually, in some ways, that's, like, the ideal model, is, you know, just, like, supporting it just like we do highways. We don't, highways don't, you know… Pay for themselves, for sure.
**Christophe Kamphaus** 04:59 Yep.
So, to start with, let's do some triage.
I did some housekeeping, and I went through all issues in SAMConf.
Which were in our area, and added to the board, so that's… Why you might see some new issues on the board.
And we have, two pull requests open at the moment.
One is for… The promotion of VCS conventions?
And the other one is for… Let me open both.
for defining span conventions in VCS.
And here, just a shout-out to Adriel. He had a blocking issue noted down here.
So… Once he sees it, just respond to it.
And the other question that's open is this one.
Basically, the question is whether we should rename the… Entity, or one of the entities.
So, this entity here, uses, mainly the head.
Attributes, so the question is whether we should rename the entity Rare fat, or something like it.
**neil yashinsky** 06:52 Hmm, that makes sense.
I mean, on the surface.
**Alan Clucas** 06:59 Have touch with using things that are not not get.
Do they necessarily have this concept of head, though?
because head feels like a Git-specific term in my memory, but it's been 15 years since I've Any… any scenario.
**Christophe Kamphaus** 07:31 Yeah, the question would also be.
Would we have a second entity ref base?
At some point.
Potentially.
**Alan Clucas** 07:42 Says that.
or what this… that's… you're meaning, therefore, this… this CI is going… is… is for this… pull requests, I'm going to use Git terminology, or GitHub terminology, is going… is being merged into that base? Is that the target branch?
Is that what you're meaning by base?
**Christophe Kamphaus** 08:05 Yeah, we have it marked in some places, if I remember right.
**Alan Clucas** 08:16 Because sometimes you run… well, I certainly run CI on… Without… on things that aren't pull requests.
But that's presumably optional.
**Christophe Kamphaus** 08:28 But I don't think… I don't know if we have… associated this entity in anything.
I think we just use… the attributes.
Oh no, here it is.
**Alan Clucas** 08:55 Smooth, yeah.
**Christophe Kamphaus** 09:36 I think it makes sense to… clarifies this.
I also have here RefHead or RevBase.
Or if it's nicer, then we should… So it's a name…
**neil yashinsky** 09:56 Yeah, I mean, on the surface, I don't think ref has a lot of implicit? Explicit? Either value, it seems like. Not quite, but sort of a placeholder anyway.
Hey, Carlos, let's go.
**Christophe Kamphaus** 10:13 I think this needs some… Discussion, what the role of this entity really should be.
**neil yashinsky** 10:21 Yeah.
**Christophe Kamphaus** 10:21 Because at the moment, I can't judge whether we should rename it, and… or what it should be renamed to.
**neil yashinsky** 10:30 Yeah, or what's the closest, you know.
Thing we could, reference, to extend a decision rather than create a new one, or what have you?
**Christophe Kamphaus** 10:42 Yeah.
And also here, what actually does it represent in this case?
Yeah, it's not fresh in my mind at the moment, so… You'd have to look it up to some… Research as well on this.
**neil yashinsky** 11:03 Yeah.
I always think it's better to delay a decision than make a wrong one.
**Christophe Kamphaus** 11:08 Yep.
I guess we could split it off from this PR.
Not to block the rest.
**Alan Clucas** 12:08 What does going to release candidate actually do? Does it…
**Christophe Kamphaus** 12:13 It's a signal to the community that they should take a closer look to it, because it means we will go soon to stable.
**Alan Clucas** 12:22 But not that it's harder to… modified.
**Christophe Kamphaus** 12:26 We can still change things, and we can also still do braking changes if needed, but it's a strong signal that we don't want to do any more braking changes.
But it's now the time to… Implement them, if you haven't already.
And to find any remaining bugs, basically.
**Alan Clucas** 13:06 Because my… my, sort of, I'm just trying to come up with the right words, but… ahead.
I don't know, it feels like… It's kind of, like, current, in a more generic term, and then… Base is more like parent.
Something like that.
And… common ancestor, but we're not going to put a common ancestor into an attribute name.
It's too long, but… I suppose they're nice and short, aren't they? People know what they mean if they're… In any way, use.
used to Git, but it does feel quite Git-specific.
Because head in subversion didn't mean what it means in Git.
That's the last thing I used for subversion.
Head. Head was… you could only have… well, head was… Like, the… the servers… tip.
Sort of. Whereas we're not really meaning head, we're not meaning what we would get if we did a pull.
Which we fetch head, but…
**neil yashinsky** 14:23 Right? Honestly, that's the thing I'm still trying to just, like, myself internally understand.
**Christophe Kamphaus** 14:29 Yeah, this also brings us to our other PRs that's currently open.
Where we try to define version-controlled spans.
At least the client span.
And then, there's also this point.
Where we try to… Generalize the actions we can perform across the different version control systems.
I think we are… will basically choose… the Git actions, but here with this, we also tried to show What action would be named, in other systems?
**Alan Clucas** 15:16 Yeah.
**Christophe Kamphaus** 15:23 Yeah, you have to call it something, and just inventing new names also doesn't help.
**Alan Clucas** 15:28 There's an XKCD about that, isn't there?
**Christophe Kamphaus** 15:41 So yeah, I guess we can review, please give it a look.
**Alan Clucas** 15:49 This might be quite a fun PR to do to get.
To consume the environment's… If… the OpenTelemetry environment variables are set, emits fans based upon actions.
I don't know whether they'll accept it.
**Christophe Kamphaus** 16:09 You mean in the Git CLI?
**Alan Clucas** 16:12 the actual kid.
**Christophe Kamphaus** 16:13 Emits a spans directly from there.
Oh, yeah, so I might… That would be an interesting one.
**neil yashinsky** 16:26 I mean, it sounds like, what's the word I'm looking for? Like, a useful abstraction layer to drive that.
Little I know.
**Christophe Kamphaus** 16:38 Yeah, an open question I wanted to get your opinion on.
Is this one.
Here, we have, we have not yet defined at the moment, any VCS conventions.
At least at the top level.
If you take a look at the semantic conventions… Here we are at the top level. You don't find VCS here. You need to go under CICD, Metrics to find some here.
At the time, we did it this way.
To keep everything pretty much together.
And now the question is, would we split it off?
Since we now also define Version-controlled spans, or would we also define version control spans under CICD.
**Alan Clucas** 17:56 Well, You could certainly… there are… there's certainly useful VCS spans that are not happening in classical CICD.
**neil yashinsky** 18:12 Hmm.
**Alan Clucas** 18:13 pattern. Yeah.
**Christophe Kamphaus** 18:15 Any example?
**Alan Clucas** 18:16 I'm trying to think of a proper example of that.
I guess you could write a, like, a web… a web UI to access… bits of your VCS system.
So you're going to have spans that are seeded with a web request, but then go through.
a BCS transaction, like… I'm not saying that GitHub would actually enact any of this, but, you know, a Git forge… In theory, is going to perform a commit or a push kind of action.
underneath a web UI.
**neil yashinsky** 19:05 Yeah, like, what kind of granularity are you looking for to track the whatever spans or whatnot of your version control system itself?
I think is, Yeah, that could certainly, I mean, especially maintenance operations and other reasons why you could update your VCS that, you know, don't quite trigger a build or whatnot.
**Christophe Kamphaus** 19:27 Yeah, like a renovate Action or a Dependabot.
**neil yashinsky** 19:31 Right.
**Christophe Kamphaus** 19:32 any bot interaction.
**neil yashinsky** 19:34 Right.
**Christophe Kamphaus** 19:35 It doesn't have to necessarily come from a CI-CD pipeline.
**neil yashinsky** 19:41 Yeah.
Although, to be fair, it doesn't look like… and maybe it's just, you know, me or us, if you will. The use cases aren't, you know, falling out of the sky, you know, they're not everywhere, so it's hard to say how useful that would be.
But it certainly seems like there's a case for them.
**Christophe Kamphaus** 20:09 Maybe I will take a look how other conventions If they are really just strictly for their domain, or if some also contain others.
We'll take a look at that.
**neil yashinsky** 20:21 Semi-related question, not exactly out of left field. There isn't a, like, an inheritance, model for hotel standards, is there?
**Christophe Kamphaus** 20:33 We can have some, We have a model where we can define General descriptions and names and attribute levels on an attribute, and when it's used by a signal, we can override it.
**neil yashinsky** 20:52 I see.
**Christophe Kamphaus** 20:54 So that's how you can… how it was used for HTTP, and also for… database conventions they specified, they did some additional description, depending on which database system it is.
**neil yashinsky** 21:08 I see.
I wonder if that would be… oh, sorry, go ahead.
**Alan Clucas** 21:13 There you go.
**neil yashinsky** 21:14 I was just gonna say, I wonder if that would be applicable here, in… in that, like, on the… I think VCS is… if I… if I heard correctly, Christoph, like, the parent and CICD the child? Did I have that right, or is it the opposite?
**Christophe Kamphaus** 21:28 No, how it's modeled. It's really, it's two different, separate top-level domains of, some conv.
**neil yashinsky** 21:38 Oh. Huh. Okay.
Separate book related,
**Christophe Kamphaus** 21:43 here under the registry, it's really… you see it. So here you have VCS, It's always the top-level VCS and CICD.
This is the top-level CICD prefix.
**neil yashinsky** 21:58 Interesting.
**Alan Clucas** 22:00 Because certainly I… sorry, I'm going to give another counter… another example of where… so, in CICD, if I'm doing a buildX build, for example, building a Docker image.
I would emit spans for the HTTP request to download the Docker image and upload the document and all that stuff, so that's all part of one ginormous span. So again, it's sort of like… Crossing into a different… domain.
Which makes… I don't know that you… I think attempting to define hierarchies is… People go, well.
can I actually use it because I'm not following the hierarchy? Well, yeah, you probably should do.
**neil yashinsky** 22:49 Yeah, inheritance or whatever, a hierarchy kind of implies, order or, like, dependency, and it almost seems like, again, from my very, cursory knowledge, like, we need, like, A metamodeler or something like that, that's not, like, I mean, this is… this is clearly beyond the scope of what we're talking about, but you know, kind of a… the broader… Definition for things like this, how they should share similarities without introducing strict Whatever, hierarchies.
So that you don't have to, like you're saying, it's not forced, but there's a starting point that's logical, but like I said, I don't know if that structure really exists, or if it's… this is really the place to create it if it doesn't.
Probably not, honestly.
**Christophe Kamphaus** 23:41 Yeah, so, from what I see, we do have some other top-level domains here.
that, are under some other category here, like.
**neil yashinsky** 23:52 Hmm.
**Christophe Kamphaus** 23:53 quantum environment… So, for different languages… gRPC… So I think there's precedent to keep it under a different category.
**neil yashinsky** 24:18 Yeah, I mean, in some ways, if you can distill it down to the essential in each of the separate domains there, you could hopefully avoid most of the overlap.
**Christophe Kamphaus** 24:29 Yeah.
It's also to not overload, here's a top-level waitress.
**neil yashinsky** 24:36 Yep.
**Christophe Kamphaus** 24:42 If we search for it, can we find version control?
I guess if you search for it… You would find it.
I would keep it… under CICD for now.
And if we see that it's… We have enough… Dima, if we got… Demand to split it off, we can still do it later.
**neil yashinsky** 25:34 Right.
**Christophe Kamphaus** 25:36 So I would do it similar to this one.
**neil yashinsky** 25:44 Seems like the closest existing… structure.
**Christophe Kamphaus** 25:49 Yeah.
**neil yashinsky** 25:52 I agree.
**Christophe Kamphaus** 25:55 Okay, I will… unless anyone has an objection, I will comment like that on… It's the PR.
**neil yashinsky** 26:05 Great.
Thank you.
**Christophe Kamphaus** 26:11 Thank you as well.
**neil yashinsky** 26:13 Always happy to help.
**Christophe Kamphaus** 26:17 Carlos?
Yeah.
**carlosalberto** 26:21 Oh, shit.
**Christophe Kamphaus** 26:21 towards the collector?
**carlosalberto** 26:23 It's not actually the collector, it's about a prototype for the Span lifecycle processor. I hope Adriel checks this out. It's actually very simple, let me just share my screen.
That's an interesting one that I cannot share.
**Christophe Kamphaus** 26:47 Do I have to make you… presenter?
I thought since it was a… Public, call, anyone could present.
**carlosalberto** 26:58 Yeah, yeah, I just… I share my… sorry, I changed my laptop, and I… and I think that problem forgetting something.
**neil yashinsky** 27:06 Yeah.
**carlosalberto** 27:07 That's a classic one, you know?
Okay, I don't know, and, let me try a pair of things quickly.
Let's do this.
I need 30 seconds.
**Christophe Kamphaus** 27:31 Oh, we'll have to rejoin. I'm having some computer issues.
**neil yashinsky** 27:36 Sounds good.
Well, a confirmed, I should say. Not good.
**carlosalberto** 27:57 Okay, I know what's happening.
Oh, Jesus, that's the…
**neil yashinsky** 28:00 I know of that look. I don't know what your problem is, but I know that look.
**carlosalberto** 28:05 Yeah, yeah, that's stuff, like, okay, that's what I suspected. I may need to quit and reopen. Give me a…
**neil yashinsky** 28:13 True.
**carlosalberto** 28:13 In seconds, yeah.
**neil yashinsky** 28:14 Dennis?
**carlosalberto** 28:33 Okay, let's try now. It should be working, hopefully, now, That's one of the things that I… that is not very… Let's see how it goes. Okay, perfect.
So, yeah, you can see my screen, right? Yeah. I cannot share the entire thing, so sorry for that, like, sort of the entire desktop. Anyway, so this is very, basically a very small, prototype I have about, it could be a new spam processor.
And it could basically be a delegating spam processor, which could be taking a tracing processor.
Sorry, a spam processor. Like, you can see in this part, that when you are creating that, you're taking a processor. And then, besides, like, doing all the operations that the spam processor does, it could be taking a logger, so you are basically reporting at the same time, spans when they are started, but also then, you know, and then when they end, of course, I'm sending them to a span exporter, but also, every time something happens to a span, you're reporting that as an event.
So that's pretty much it. In order to do this, basically what I'm doing is that I'm having a second thread.
So basically, you know, like, we just delegate, like, you can see here in the start, for example, in this part.
that you say, I'm, like, starting a span.
And I'm just, like, delegating that to the actual span that I'm using behind the scenes. At the same time, I am sending this to my thread, which will be… I will be reporting what's happening to that span.
as an event. And this is, for example, what here we would be doing. Let's ignore that part about the synchronization for a second, and this is what we would be doing. We are reporting everything the spawn has, like, literally everything, as an event and attributes, information, you know? The idea is that If you want that, and that's the idea, you can take all the events, all the information in advance to reconstruct fully a span, you know?
basically, that's the idea, you know? It's very simple. So that's for a start, and we are reporting everything. The spawn name, the kind, the name, the version, etc, etc. Now, on the spawn end, we are doing, something like that, the same, you know? But it's simpler because, you know, you're just ending. Now, there's a part that is missing, and this is why I have a PR at specification, which is that we also want to capture, when this is spanned, it's getting its name changed, or updated.
That's number one. Number two is when you are getting a new attribute, or an attribute being overridden, you know, like, new value for the attributes.
And the third one is when you're adding a link. So those three things.
If we have, like, actual, like, operations in processor, we can just go and get, you know, something like this, and just report everything.
That's pretty much it, and then you would have the, Reporting a heartbeat in case the span is sitting idle, and there's nothing happening to it, but it's still alive.
And this is also one of the things, that when you are ending this band, you are removing DAF from the watchlist. It's pretty simple, and it's only for the SDK at this point. One of the things that is… will be tricky is that, of course, you don't want to keep a hard reference.
to the spans, because, you know, you want them to be collected, you want to observe them if they are around. If they are not around, just, you know, do nothing, because otherwise they will stay at the process forever. The second thing is that probably it's not a good idea to try to watch all the spans that are sitting idle forever, otherwise this may create, like, you know, an explosion when it comes to memory usage.
So I would say that's pretty much my, my stuff with this, with trying to have, like, a maximum number of spans that you're watching.
And then if, we can… we should probably do something, like, besides, reporting a log in case, you know, let's say you are watching only the first million spans.
Hopefully, you're not reaching that limit, but if you cross that, then, you know, of course, you're gonna do anything. Just report a log. Maybe it's in a metric, I don't know.
So that's pretty much it. It's pretty simple at this moment. It's, at the SDK-only level. If this works well, and the specification, people like it and all that, we can try to do something at the collector level. And I don't know, I don't think this actually satisfies… all the things we want to do, probably at this group, but this is a start, you know, at least from the SDK perspective.
**neil yashinsky** 33:35 Yeah.
**Christophe Kamphaus** 33:36 Yeah, looks very good.
I have two questions.
Why do you limit the number of spans you are watching?
Are you just… Do you still keep references to closed spans, or…
**carlosalberto** 33:51 No.
**Christophe Kamphaus** 33:52 Okay, so you, only watch in-progress spuns.
**carlosalberto** 33:55 You're great.
**Christophe Kamphaus** 33:56 Why?
Why do you set a limit? Because those funds are anyways in memory.
**carlosalberto** 34:03 Yeah, I was thinking that it's on the safe spot.
just to be on that, it's to be triple sure. Probably we can remove that.
Anyway, Yeah, I would say probably doesn't… it wouldn't hurt. There was also… I also based this one on a previous prototype, that was not the same, it was similar enough, and that person was doing something like this.
Probably we don't need to. As you said, it's, as you said yourself, those funds are in memory anyway.
And we are keeping a self-reference to them.
So probably we could get, you know, remove that for a prototype.
**Christophe Kamphaus** 34:46 Yeah, I just see… Maybe we would hit this limit, and then we would have weird bugs, because we are hitting this… Limit.
And if a process is keeping too many spans in progress anyway, the memory will explode.
**carlosalberto** 35:03 Right, yeah, that's correct. And actually, that's one of the important points that this shouldn't be a… this shouldn't be, like, a good situation that you are keeping way too many spans, you know? That shouldn't be, like, a thing ever, you know?
Yep.
**Christophe Kamphaus** 35:22 My other question was about the attributes.
Okay, you have it as a to-do there.
**carlosalberto** 35:29 Yeah.
**Christophe Kamphaus** 35:32 Okay.
**carlosalberto** 35:32 Yeah, yeah, basically that's the one, yeah, that's pretty much it. And, I mentioned in some other, called that… there's… this is why, as I said before, there's a PR specification to add 3 more operations, one processor.
You know, tools, so we can… Because, you know, like, well, honestly, that's just the easiest, the cleanest way just to do this. Just, you know, like, the spam processor gets notified every time a spam gets a new link, gets its name, updated, or you get an attribute right, you know, which can be either, like, new attribute, or… Or, you know, new value.
Neil?
**neil yashinsky** 36:16 Thanks, Carlos. a question, and this is probably more about what I don't know. Well, you mentioned the link. Is that… were you describing, like, the exemplar that you had set between the log and the span? Is that what you meant by link, or is there another… Something on the…
**carlosalberto** 36:32 No, like, no, it could be literally when you get a new link to the spam.
**neil yashinsky** 36:36 Oh, oh, the new link on the span, yes, yes, yes. So, and then, does it… would it make sense to try to connect an exemplar here between the log and the span?
**carlosalberto** 36:46 I don't think I followed that, like.
**neil yashinsky** 36:51 Will…
**carlosalberto** 36:52 Yeah.
**neil yashinsky** 36:53 Yeah, I was just wondering, like, like, in Grafana, for example, being able to bring back the log, that you have here, as well as the traces that it correspond… or trace, I guess, that it corresponds to this particular log.
Would there be a one-to-one with the log event that… well, obviously, there's two events here, the start and stop, but, assuming that there's, you know, you started this, you know, you log the event that the trace start… or the… well, yeah, I guess it's a trace started, and then you wanted to also find that trace itself within a single query. If you have an exemplar, I thought that would allow those two to be more readily, queried and returned in the same query.
**carlosalberto** 37:39 I don't have a clear answer for that. My impression is that that's something that should be discussed independently regarding how links are used.
Right.
Probably, yeah. So it's a bigger question, let's say, you know?
**neil yashinsky** 37:51 Yeah, I'm not just… oh, sorry, go ahead.
**carlosalberto** 37:55 Also, the sampling group in the past, they also were discussing things like this, like… When you're adding links, because, you know, they are using links, in sampling as well.
And, what kind of information you can keep around, what kind of extra information you should try.
to fetch, or could be added, that it's not spec at this moment, you know? Yeah.
**neil yashinsky** 38:15 Definitely.
**carlosalberto** 38:16 So, yeah.
**Christophe Kamphaus** 38:18 And if you emit matrix.
And you're in the context of a span, then you might get exemplars out of it.
Right. That's independent of here.
**carlosalberto** 38:29 Yep, correct.
**neil yashinsky** 38:32 Yeah, I mean, it seems really great, and that's the only, you know, like, next logical step that I would… that I was thinking, like, Christoph was, like, exactly right, like, as these start… Generating related information, just making it easier or automatic, if you will, to correlate them.
No, good stuff, though. That's… it looks very, helpful.
Hold on.
**carlosalberto** 38:55 Yep.
**Alan Clucas** 38:56 What would be the intention?
Gone.
**carlosalberto** 38:59 Yeah, sorry, I was saying that, yeah, sorry, that this is only at the SDK level for now, I hope Adrian sees this. Yeah, I think he has other stuff in his mind regarding the collector, which we can discuss when… He comes next week. I, I'm… Alan, please.
**Alan Clucas** 39:15 In the event that we've now got events and spans coming out, What… and then somebody's reconstructing the events.
into spans.
we've now got a duplication, and I mean, they've got the same IDs, so they're easy to deduplicate, but they're still, like.
What's the model we would use? So, in… the thing I work on, I go workflows, and I know some spans are not going to need to have come out over the event.
system, so I could have two span… emitters.
Boom.
that, that feels like… is that the intention that you would use?
Two different span… two different span… systems, one for… lift ones, or… but this one's still emitting, sort of, normal spans as well. I was expecting it potentially not to, because otherwise there's a duplication, basically.
**carlosalberto** 40:23 Yeah, correct, that's a good question, and I don't know, usually I think we are abstracting that so that it could be handled in actual backends, but I can tell you, in the previous company where I was working, we had something like this.
And basically, The spans you are getting from, let's say, in this case would be the events that you're reconstructing, they are meta spans, so… You are changing something about this span, so it's not actually the same span.
So you're taking everything you're getting from them.
and say, this span represents this other span. Change the name or something.
So basically, you will have an additional field, for example, saying that's the original span. This is not the actual span. The name will be… whatever, metaspan, dot whatever, you know? So, in theory, you could have Indeed, two spans, you know?
They are not the same, but it's technically duplication, yes.
**Alan Clucas** 41:23 But in some cases, I… my problem is that I can't emit a span, because my span started in a different executable for my… the… the end.
So my span start event is coming out in one executable, it dies, and then another one starts, and then it would want to emit the end, which works with events, but then this… like, I have to construct a span which emits then a span started, and then… I've… I can give it to you in a way that the trace ID is… is identical to the one that has already started and already emitted a span start event.
**carlosalberto** 42:05 Yeah, in that case, I don't know if this is something, like, a good trade-off for you, or it could be, is that then, since this is, See, the process already started delegating one.
You can just do nothing, and just… just rely on the actual spam.
like, that you're creating, and do nothing, like, regarding exporting, you know? You are never exporting an actual…
**Alan Clucas** 42:28 Yeah, I guess.
**carlosalberto** 42:28 And using Span Explorer already. And as I said before, the idea is that everything that happens in Span, you're really getting everything, literally everything. So you could reconstruct that, and then just say, you know what, I'm gonna rely on that part.
**Alan Clucas** 42:43 But I'm not wanting to omit the… the start events, effectively. When I start the span for a second, or third, or fifth time, I… don't actually have a start at that point. I know I've already omitted a start, because I've got evidence of that.
**carlosalberto** 43:00 Yeah, in that case, I think that, yeah, something that we… I don't know, then again, like, that could work for you, like, we just… you configure the span.
processor, like, say, like, in a way that it can detect, and say, like, for whatever span or under these conditions, just don't do that. Just keep on sending the heartbeats, or whatever you can find. I don't know how it could look like, but yeah, that's something we could do.
**Christophe Kamphaus** 43:29 So if I understood it right, you could have… It's a case that your process restarts, and if you persisted which spans were active.
You could restart those spans in your context with the same trace ID, with the same span ID, Just that this processor would emit a new span-started event.
Is that.
**Alan Clucas** 43:53 That's the problem, because I… I'm… I'm just creating deterministic span and, trace IDs.
already.
So, they are deterministic based upon the CI run that's running, so it's a combination of Kubernetes namespace, name, and… creation timestamp, because creation timestamp's pretty much unique anyway, but between those three, everything's unique. They can't actually overlap in time with those three attributes, so I feed those into something that gives me a hash that then gives me a deterministic span ID, and then the trace ID is, for the sub-traces, is also deterministic, because I got similar information.
**Christophe Kamphaus** 44:34 Would it actually be a problem for your backend system to have duplicate start events?
**Alan Clucas** 44:41 well, I'm not… I'm not running the backend system. I'm only going as far as I'm emitting spans in open telemetry, and then it's a bring your own… you know, this is an open source project. It's a bring-your-own telemetry system.
**Christophe Kamphaus** 44:53 Yeah.
**Alan Clucas** 44:54 I recommend, you know, I've got a… I've got a pre-canned… if you spin all this up, you get Grafano and you get some Spartans in it, but, you know, I don't care what you're using.
So… I'm hoping that my long-term goal would be that, the collector can do, or something outside of me, can do that reconstruction, and then… when somebody clicks on, show me the span for your CI run, you get…
**Christophe Kamphaus** 45:23 Yeah, you would see the in-progress spans as well as the completed spans.
**Alan Clucas** 45:28 And you would also see… you wouldn't know that the controller had restarted or not in that life cycle. So I already can do that if the controller doesn't restart, but if it restarts, I have to… I re-emit the span, so you get weird effects. Depends what you're… you've got the same span ID, same trace ID, with different start times. They're all parented to the same span ID, but the span… span has to get re… image, to say.
**carlosalberto** 45:57 By the way, I got too wrong.
**Alan Clucas** 45:58 Uncommon. Go ahead.
**carlosalberto** 46:00 Oh, sorry, sorry, sorry, I thought you had… you were finished. Sorry, continue.
**Alan Clucas** 46:04 I don't think that's an uncommon scenario, so that sort of… wanting a long-running trace span that needs to survive a reboot. It's not a reboot, but effectively.
And that's what I'm trying to, solve.
**carlosalberto** 46:24 Sorry for interrupting, yeah, I thought you were done. I cannot find, at this moment, I don't know why, maybe Josh Surrett changed the name, or it's somewhere else, but he has this idea that I even have a local repo, I think, somewhere.
of OTLP MMAP, which is basically doing what Prometheus does, which is, you know, keeping all the information in a buffer that is written to disk.
Actually, no, it's… I think it's to the memory, and it can eventually be written to the disk, and then you just recover that later on, you know?
I think that's something that we wanted to talk in the past. And, yeah, I don't know, pro- Since I already played with that a little bit in the past.
I can try to give a small introduction to this somewhere in the loop here. This is something that George Surrett is doing in his free time.
Mostly, I think, and there's no plan to make it part of OpenTelemetry right now, but in the future, that's something we could do, you know? Which could probably complement what you need, Alan.
**Alan Clucas** 47:29 Okay.
Thank you.
**carlosalberto** 47:35 By the way, I have to roll, sorry for that. Yeah, I will watch the rest of the video, yeah, so see you, see you around.
**neil yashinsky** 47:43 Girls.
**Christophe Kamphaus** 47:43 See you!
**carlosalberto** 47:44 Nope.
**Christophe Kamphaus** 47:52 Do you have any other topics?
**neil yashinsky** 47:55 I don't…
**Alan Clucas** 47:57 Nope.
**Christophe Kamphaus** 48:02 And Robert, I don't think we've seen you here before.
**Roberto** 48:08 Yeah, hello everyone. Not particularly. I'm following the projects for a while now, but yeah, I'm just, Coming as a spectator.
**Christophe Kamphaus** 48:17 Great to see you. Do you have any questions?
**Roberto** 48:21 No.
Not today, at least. Maybe another day.
**neil yashinsky** 48:26 Fair enough.
**Christophe Kamphaus** 48:27 Good to see you.
And if we don't have any other topics, I will give you back your time.
And see you next time.
**neil yashinsky** 48:37 Thanks for your leadership, Christoph and Ellen. Have a great one. Nice meeting you, Robert.
**Christophe Kamphaus** 48:40 See you.
**Roberto** 48:41 Thank you.
