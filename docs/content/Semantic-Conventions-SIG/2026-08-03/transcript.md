SIG: Semantic Conventions SIG
Date: 2026-08-03
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Trask Stalnaker 00:03:17 Hey folks, we'll give another minute, and then we'll get started.
Alright, let's… Kick us off.
Let's go straight into our topics. Establish bulky OSS… Semcon… Martin, hey!
Martin Black 00:04:49 Hi.
So, yeah, basically, I am from AWS, and we are working with the Valaki open source community to We won't intend to introduce OpenTelemetry metrics to Valaki for server-side, metrics.
And we would want to work with the OpenTelemetry community to establish a semantic convention for this.
And so basically, just to kick it off, I… Wanted to get some guidance on, like, how this process is looking like, like, what are the steps we need to take to… to come up with a proposal for the SAMCOM, where do we present it, how do we work with the OpenTelemetry community to… to get feedback on this, get things approved, etc, and go through that entire process.
And the other thing is just… I wanted to get some guidance on, like.
who are the people, what are the forums, Slack channels, other venues and forums, where I can get… talk to some people on, like, okay, when I'm working on establishing the, like, or creating the first proposal for, like, what kind of metrics we want, how do we want the metrics to look.
How do this look like? And also, are there any previous… examples of such, because I was looking at the, Semantic Conventions website, and there are not a lot of server-side database metrics, and I was curious, like, why is that?
Trask Stalnaker 00:06:23 Yeah, so in fact, there's no, database server-side metrics. We have, so far, the initial work was all scoped to client-side, database telemetry.
There has definitely been some interest, from folks in server-side Semantic Conventions.
so this, let's see if this… is… I feel like there have been others. I think the Oracle folks involved… I've been interested before… I'm trying to think if there's any other pointers.
Basically, what we need, and what you can, Do is, if you can gather, you know, enough people to basically create a project proposal in the community.
To, extend the database semantic conventions to server-side.
And, you know, get folks together, get enough folks together who are, you know, have expertise in that area.
Then that is something that, could move forward.
Martin Black 00:07:51 And so you're saying that, like, like.
For now, we were just thinking about Valky, because that's what we are working with, but you're saying that in order for the proposal to move forward, we would need to have, like, a generic database server-side convention, because that doesn't exist right now, and Valky needs to live under that.
Trask Stalnaker 00:08:15 Most likely, yes. If you look at how the database client, Semantic Conventions are structured.
there's sort of a base common layer across all of them, and then individual ones, you know, Redis, Postgres, SQL Server.
Oracle, will Mongo have, kind of, some specific stuff layered on top of that?
Martin Black 00:08:45 Yeah, and also, when I was looking around for examples, I saw that there are Quite a few databases that seemingly independently of the OpenTeametry, Conventions established their own metrics, or are working on establishing their own metrics. So, like, I know MySQL has server-side OpenTelemetry metrics, Elasticsearch and OpenSearch, I think, are both actively working on it.
And so then these just seem to be doing their own thing with no regard to the Semantic mention, because it doesn't exist, at least as specific to database server-side metrics.
And so, if we were… if we were to do the same thing, like, okay.
If there's no database server-side semantic convention, And, we do not have the… Investment to… or… or enough pull to… Established the entire database server at Semantic Conventions, so we just go out and do something on our own.
Would that be… what would your opinion as, like, the Semantic Conventions SIG be on that? Like, do you recommend that, or do you want this database server-side Semantic Convention?
Trask Stalnaker 00:10:02 I mean, it would be amazing to, you know, gather those folks if you're aware of people who, you know, are emitting server-side, semantic already.
And I mean, yeah, it would be great to have that base layer.
what we… in the Semantic Conventions, I think.
What we don't need to have in the Semantic Conventions Is… so if we look at the client, database, as an example.
So we would… we would love to have… databases are general enough, I think that it makes a lot of sense to have them centralized here, the common stuff.
But we don't necessarily need the, you know, Cassandra-specific stuff, the Elasticsearch-specific stuff.
All of those, we've invested recently in, being able to federate these semantic conventions.
where, and we've done this with, GenAI Semantic Conventions, where it can live in a separate repo, either under OpenTelemetry or, you know, in the case of like a, MySQL, that could live… I mean, it's almost better in some way… in many ways, for the MySQL folks to own that piece.
But it, it is… still, I think, a huge benefit if there can be that common layer.
Now… I remember some… Where something… someone said, a long time ago about the… that… They had that it's… The servers are very different, and so establishing the common conventions across them is… Challenging.
So, you know, but there may be some basic… I mean, I think they said the same thing about the client side, and, you know, we came up with something that I think works.
Where it's, you know, fairly generic, stuff in the base layer.
Yeah, Ludmila.
Liudmila Molkova 00:12:33 Yeah, I was just going to mention there was a lot of interest in this from, I think, collector folks, people who maintain receivers for specific databases on the collector.
And even though their metrics is very specific to service, right, they depend on the information they can obtain from the collector side.
Today, there is… there are still some common parts. For example, what do we… do we put it as a service name? What do we put there? How do we record common concepts, like instance, and… It sounds like there are a lot of things we would reuse in terms of attributes from the client conventions.
But the way we populate them.
And the way we work with resource attributes Becomes much more important, and definitely needs to be specified.
So Martin, if you're interested, maybe it's worth posting in the collector country chat? I think it's just the collector.
And asking if people are interested to work on Server conventions that are common.
Martin Black 00:13:49 Okay, makes sense. Thanks.
Liudmila Molkova 00:13:52 Thank you.
Trask Stalnaker 00:13:55 Oh, you're on mute, Rob.
Rob Cowart 00:13:57 I had raised my hand. I was just gonna add, to the thing. I would encourage you to do exactly those things. You know, a couple months ago, there was no network SIG. As of last week, officially, there is a merged network SIG, and we have a pretty good-sized initial team that is working on it. Just Friday.
I had someone in my network who has some database activity monitoring technology, and he's like, do you think I should do OpenTelemetry 2? And I said, well, I don't know that there's any semantic conventions for the database server-side yet, he needs to look into that, but I could maybe already have your first collaborator and tell him to join if you, Post in there, so… You might be surprised how quickly you could get together a cohort of people that want to work with you. I know we were, on the network side, surprised how well it's come together, so… I just wanted to give that word of encouragement, sorry, so…
Martin Black 00:14:51 Okay.
What are they doing? Thanks.
Okay.
So, so yeah, I guess that's… those are my questions, so I guess then the next steps are, like, Trying to gather people interested in establishing a database server convention.
And try to push it from that, angle.
Trask Stalnaker 00:15:15 Yeah, so check this out, check… I know that we have a couple of, folks from Oracle… in the, Semantic Conventions… let me find where they are… I think we have a team.
Even… Oh, well, this is cloud approvers. No, those are not… Possibly if we just… Yeah, go ahead.
Liudmila Molkova 00:15:51 Yeah, this person.
Trask Stalnaker 00:15:52 Oh, yeah.
Let me drop that.
Christoph.
Christophe Kamphaus 00:16:13 I also wanted to repeat again, we do have the possibility to define federated semantic conventions.
We did it for Gen AI.
So that's also something you might want to look into.
So you can do that in parallel, already define your own conventions, In a federated way.
While you work, on generalizing the database conventions.
Martin Black 00:16:42 Okay.
Trask Stalnaker 00:16:44 Yeah, so Martin, the way that would look, that would be not necessarily establishing that base layer, but you could… Basically, if you do go the route of establishing your, you know, Valky-specific, entirely Valky-specific Semantic Conventions. You can still use our tooling.
Which makes that easier for people to consume.
Martin Black 00:17:14 Okay.
Thank you all.
Trask Stalnaker 00:17:27 Cool, thanks for joining, Ludmila.
Do you want me to hand over sharing?
Liudmila Molkova 00:17:39 Yeah, yeah, let's do it.
Trask Stalnaker 00:17:42 Cool.
Liudmila Molkova 00:17:44 Okay, so I… I've realized that I maybe spend more time working it around, than it would take to actually introduce SpendType.
So I wrote an ATAP, And it's pretty straightforward, right? There is nothing super difficult except the consensus there. So, we will let spend type as the product field, or the top level. We switched from attribute.
On events to event name top level, and it seems natural to just start there with Sven.
And then all the changes become pretty much trivial. We add this optional type. If you don't want to be precise, don't set spend type. Like, spends without the type are, like.
Logs without event name, right?
So… the tricky part, so I presented it on the SPAC call last week.
And I've got a lot of support, but I've got one tricky question. That is mostly, what if we are blending spans together? Should we record it as an array of spend types? Should spend type be an array?
And I think it's… it's not a good option.
But it's worse.
kind of, discussing and deciding upon it. So my proposal is that, given that the spend type, sorry, the spend definition is not just a bag of attributes, right?
we actually cannot merge identities. So, in most cases where we do, it's wrong. When we merge, like, AWS SDK with HTTP, it's not even how we model things in instrumentations.
These are two different layers, right? So we would have… the… logical operation, and there are multiple HTTP calls under, in easy case, They're very similar, like, if there's just one request, no retrace, everything went well, but still, there are different layers, and… Even if duration is somewhat similar, the information available on them is slightly different.
There is, I think, a natural case where blending makes sense.
And this is the server spends.
Where their scope is pretty much always the same.
And… Ideally, we want one span report that we don't want two server spans.
Where… This is the place where we can ask people to… disable HTTP instrumentation, or augment that earlier, or something.
But, I… It would still work better as individuals by definition.
Because… If… currently, we don't define A good spend name for this.
Sorry, maybe I should edit the comparison, but essentially, for… for this monster.
The SPAN name would be the function name.
But for HTTP, it's different.
things like HTTP route are not really applicable to FAS frameworks, and in general, when we define the FAS spans, when we document them.
Where… Defined quite a few things about it, so… I, I think in… practice in user applications. They should do what they want. They… if they want to blend identities, if they don't want to define things precisely, it's okay for them to report span with whatever type, or without a type at all.
But in semantic conventions, I think, We should be strict, and we should have just one spend type.
I don't think an array makes sense, because essentially an array exists for edge cases where people don't want to be specific in their definitions.
And it's just a hack, and they can do the same with, I don't know, concatenating strings.
That's my pitch, but I want to hear what Semantic Convention People think, and if we should pursue An array identity in, in your… Whatever, in your opinion. Yeah, Christoph?
Christophe Kamphaus 00:22:48 If I understood it right.
There would be very limited cases where it would make sense to combine span types.
Is there a way to define SPAN refinements.
So you could say a specific type is a refinement of another, And then you can, Add your attributes that would be specific to that type.
Liudmila Molkova 00:23:16 That's a great point. Yes.
the caveat that we need to say, okay, this is the HTTP span.
And it has also a bag of, files attributes.
We… we cannot say it.
Well, we can say today it's a refinement.
And we get another interesting question that nobody raised so far. Well, now with you, Chris, of that. How do we identify a refinement?
Because it has the same type, and then we need to identify a refinement.
And the answer is maybe yes, but in a different manner. And I see Josh has his hand raised. Go ahead.
Josh Suereth (Google LLC) 00:24:00 Yeah, I, oh, I don't have my camera on, hold on.
I'm distracted by that. There we go.
So… These are all good questions. I… I want to argue on, like, two main things, that we want to ground on, is, like, what is our use case goal?
for making these decisions, right? And then, second is, like, what… I'd like to keep it simple, if possible, because we're already rather complicated. So, I do think multiple identity is just confusingly stupid.
I… I… I don't see how we scale the ecosystem well, and I think it makes writing things like live check, like, 10 times harder.
How… because effectively what you're doing with multiple identities is you have… I'm gonna use type theory, because I'm a type programming language nerd, but it's basically, the only thing that I allow are unions, right? If you've used C++ unions before and you love them, great, cool, that's the only thing we're gonna allow, is, like, a union type.
For everything.
Actually, it's not even C++ union, it's, like, the notion of a type union, but anyway. You get what I mean. Like, I think that's a really, really complicated place to live.
Regarding refinements, our original theory in Weaver was refinements was kind of a thing that… Did not need to be exposed to users because of two reasons, right? One, if we look at the reason we have semantic conventions, for HTTP.
It is so that I can do something with HTTP spans and metrics, and understand them.
And if I refine an HP span for additional things, right.
the most important thing is that that baseline use case for HDSpan continues to work.
And we decided not to do Like, inheritance-based polymorphism.
Right? So, instead, what we have is you can extend things with additional you know, features and shapes and such.
And that's fine. What I think we're saying here, a way of… a way that I think about what's being phrased.
Well, first, let me end that thought, so that everyone, like, you can agree with where we made our decisions, which was, you know.
there's a structure that if your span abides by, you will get it treated like an HTTP span. That structure is independent of where it's really used. If you want a fast span to get used as an HTTP span, and an account into HTTP-like you know, things, you know, if I'm automatically calculating metrics.
Right? And a fast spin refines an HP span, that would happen.
If a fast spin is fundamentally different, or I'm treating it in a way that's no longer an HTTP spin.
that's now a different type, right? That's a different thing.
And that's kind of where we were with Weaver and everything.
So, back to the original thing.
If we start to do this, kind of structural-based typing here. It's kind of similar to, if you will, Go interfaces, right? Every single semantic convention is now, like, an interface in Go.
Not like an interface in Java.
not like, many, many other systems. It's literally like, hey.
if it looks… if it looks like a duck and it quacks like a duck, you treat it like a duck. And we're back into this, like, weird space of, why do we even have a type ID to begin with? Like, what's the value of it, right? So… I want to take that step all the way back and say, if you engage with type, it's for a specific reason. What are our goals and motivation?
Our primary goal is this live check feature, where we want to say, this span matches the expected definition of it, and I can have a full integration test and compliance feature. And so I can guarantee, say, everything HTTP-related comes with the same set of attributes, or matches the spec.
Right? The reason for that is, if the consumer wants to treat things like ducks, great, we don't care. What we can say is.
We have HTV spans, and they're guaranteed to have these 12 attributes. You want to do something where you treat things with those 12 attributes the same? You want to do things where you treat things with 20 more differently? Cool, that's on you. What we guarantee is those 12 attributes are there, and you can treat this like HTTP, right?
I don't know if we can go stronger in OTO, is my concern.
Like, I think that's where it all hell starts to break loose. I don't really want to do a dynamic typing system. I don't really want live check to be quite as dynamic. I think it makes compliance stupidly hard and crazy.
Personally. So, like, it's not a way I want to walk, but I wanted to kind of talk through what I think we're asking here is basically, you know, if we start having multiple identities, if we start having extensions.
Inheritance-based polymorphism is interesting.
It's really complicated when it comes to, like, live check, when it comes to validating things. So I want to ground to, what is your goal? Like, what is the use case you cannot do?
That we want to unlock, and let's figure that out.
The attributes that they need to have at a bare minimum.
Right? Multiple types, I'm not sure what our goal is.
inheritance.
Not quite sure what our goal is, yeah.
Liudmila Molkova 00:29:55 I want to reply to Josh and Trask, I think you… you're muted, so maybe you had something that… yeah, I will quickly reply. I'm glad you spelled it out that you hate the idea. I also hate the idea. It's just not the thing I want to put the notes up, right?
there are so many things that are broken with it, like, what is the… what are the metrics you report for blended Sven identity? Is it two individual metrics, or one, with comma-supported names for the metrics, or whatever?
But I think the motivation… yes, the driving motivation is life check and things around it, but we cannot just think about this scenario, because I think the most important one is actually for users to query spans based on type.
And… For this, it kinda makes sense that if you query something, you don't care if it was blended or not, it shows up in both places.
On the implementation side and everything else, it sucks.
Josh Suereth (Google LLC) 00:30:59 It's still hard to have an index on an array.
Like, I… I kinda… I get… I get what you're saying.
But I still think users would benefit from us making a choice versus us not making a choice.
When it comes to tech.
But that's also starting to get into the point where is OTEL a product, or is OTEL a standard that products support?
we're kind of in the middle here with Cemcom, right? Like, we make product-y decisions.
Liudmila Molkova 00:31:38 Yep.
Okay, any other thoughts supporting?
Array.
Sven Cowart (ElastiFlow Inc) 00:31:51 What is… what is LifeCheck? Sorry for the ignorance.
I haven't heard that yet.
Liudmila Molkova 00:31:56 Oh, I'm glad you asked.
So, the life check is the tool, like, it's part of the river. It allows you to listen to your telemetry.
And, it validates Compliance with Semantic Conventions.
And more. So, for example, it would… like, if you… today, you run it against metrics.
It would match a metric name against Semantic Convention definition, because you give it the pass to your registry.
And it would tell you, oh, this attribute, I don't know it, it's not in Semantic Conventions, or this attribute was required on this metric, and it was not there.
And it's an excellent way to… automate your, like, you can put it as a CI gate.
Into your PRs, and if somebody adds things, you just run live check, and you, as a reviewer, for example, you don't need to spend mental energy on knowing if it follows semantic conventions very precisely.
But in general, it opens up a lot of possibilities, like, Trask was using it, and still using it to build the… the conformance matrix, so you can see which of the instrumentations actually, support what, right? Because you can extract the report and see, okay, these attributes were populated, this word.
And it opens up the door to the conformance… instrumentation conformance program in ATEL, because we can formally define what… what does it mean to follow Semantic Conventions of. And it's generic. It's not that we write it once per instrumentation, it's like… we don't write pretty much any code, you just run the scenario against Weaver, and it gives you a report, and it fails with Non-zero exit card if it doesn't comply.
Sven Cowart (ElastiFlow Inc) 00:33:57 Okay, thank you.
Trask Stalnaker 00:34:03 I would… oh, go ahead.
Sven Cowart (ElastiFlow Inc) 00:34:05 No, go ahead, Thraska. I'm still processing, I… I'm thinking a lot about the things Josh just said, and it does make a lot of sense, and the reason I'm thinking about it is because, if we're gonna do flow traces as a new span type, which I know we haven't… there's no official proposal for that yet, right? But it will come, and I will submit that.
There could be…
Liudmila Molkova 00:34:32 limited with metrics.
It's right in here.
Sven Cowart (ElastiFlow Inc) 00:34:37 Say that again?
Liudmila Molkova 00:34:39 If you have metrics already, you can play with it right now, you don't need to wait for spend type. The spend type fixes the problem that we don't have for metrics.
Sven Cowart (ElastiFlow Inc) 00:34:47 Yeah, right, yeah, no, so I'm… I was thinking back to the question of span type being an array or not, and And I'm also thinking about it from the, alright, if I have to implement a platform, what kind of complexities does that being an array introduce? And that's where I think Josh's points is like, oh man, that's gonna be really complicated, but it does give people flexibility, and… I can… I kind of go either way a little bit. I can see it from both sides somewhat, so I'm struggling to come up with a… Good.
Good guidance to the rest of the group, so Thras, please go ahead.
Trask Stalnaker 00:35:25 I was just trying to think, Ludmila, through the, Java instrumentations that we have, and… So, we have… Primarily, we instrument at different layers, so we get different spans, and we have suppression techniques if people don't want that verbosity.
One of the ideas I think we've discussed from way back was the ability to, instead of just suppressing, like, say you have a… our PC span and an HTTP… HTTP span underneath it, client spans going out, and… Instead of, suppressing the RPC, I mean, instead of suppressing the HTTP span, stamping those… attributes directly onto the RPC span.
And I feel like that still works with the proposal, like, there's nothing that… would stop us from doing that. It would just be that that would remain an RPC span, sort of augmented with HTTP attributes.
So…
Liudmila Molkova 00:36:53 Right.
Trask Stalnaker 00:36:53 I'm not seeing a… from Java instrumentation perspective, at least, I'm not seeing a practical problem with limiting it to one.
Liudmila Molkova 00:37:09 Yeah, and the opposite is also true. If you want to step outer attributes on an inner span, it would keep the inner span identity.
So…
Trask Stalnaker 00:37:18 Right, right, with the… yeah, we could do that with the context-scoped attributes to push them down.
Right. It would require some knowledge that there was lower instrumentation, but yes.
Liudmila Molkova 00:37:30 Yeah.
Yeah, but then, essentially, it… With you doing this year being… You're explicitly telling your users what is the layer you target.
Okay, cool. So then I'll bring it back on the spec call tomorrow.
It sounds like among Semantic Conventions maintainers, and the people we have on the call, we don't have support for the array type, but if you folks have any thoughts, there is a link to a tap in the notes, and I would appreciate your Thoughts on this?
Christophe Kamphaus 00:38:16 One more question.
Liudmila Molkova 00:38:18 Huh?
Christophe Kamphaus 00:38:18 So, how do you know?
To which… Some conversion this, spam type would belong.
Liudmila Molkova 00:38:29 Sir, just give me a Euro.
Christophe Kamphaus 00:38:31 Okay.
Is that on the instrumentation scope?
Liudmila Molkova 00:38:36 Yeah.
Christophe Kamphaus 00:38:37 Okay.
Liudmila Molkova 00:38:37 So when you create instrumentation scope, you give it a schema URL, And… If we aren't yet, we will soon… be able to use whatever is in the schema URL to, match against, but currently, I think it's manual parameter, so you decide which register you You find it can be a local one, it doesn't even have to be published if you just do the check against some folder with semantic conventions.
Christophe Kamphaus 00:39:08 Thanks.
Liudmila Molkova 00:39:10 Thank you.
Trask Stalnaker 00:39:13 Cool, next topic is yours also, you want to just cover that?
Liudmila Molkova 00:39:17 Yeah, it's just a super quick one, it's the PR, That moves some of the, attributes we have, to V2.
And there are some changes, that we talked through before, but just quickly going again.
So this looks like it disappeared. It's actually now part of… the generated text for server, because it comes from YAML.
And this, this is the snippet, thing in… The file we have.
At the same time, this description disappeared from the Registry, because it was on the group.
And in V2, we don't have groups anymore for attributes. Well, we do, but they are not… Part of the registry.
Maybe we should have the… Public Attribute Groups Registry.
Josh, as well, in the templates, because things like, like, I'd love to eventually get rid of this general attributes doc.
and instead have it as part of individual namespace. But it's not in scope of the PR. The thing that I want to achieve is just unblocking V2 migration, piece by piece, and switching from this group to the new syntaxes.
So yeah, just looking for a few more rice, and if we like this, if we're okay with it, we can proceed with the other few groups that we all… we have the similar ones.
This is… All I had. I'm going to… Stop sharing, and so on, I think you're the next.
Sven Cowart (ElastiFlow Inc) 00:41:13 Yeah, so, just a general question, I think, on the networking SIG side right now, we're, a little bit… chomping at the bits to get started and get organized on the things that we want to move forward on and tackle. There… The problem for us right now is that… Because of the lack of the… Federated repo.
We don't quite know where to put code at the moment, so we're just… sending it, sharing it, or I was gonna start creating personal GIFs, and… for now, and share that information. So the question is, what… what do I need to do, if anything, to get the repo created? And then secondly to that.
I believe the GenAI SIG, based on what I see in GitHub, has a GenAI project board where they pull in issues from that repo and from the Semantic Conventions repo based on tags into that project view.
I think we're gonna wanna do the same thing. So, that being said, what can we do to get the project board up and running there?
I know Ludmila, you and I exchanged a couple slacks about it, but I didn't know, like, just, again, trying to bring it up so that we can get something going.
Trask Stalnaker 00:42:35 So for, for repo, open a community issue.
So, one of these guys, We're… Wait, oh, I'm in the wrong repo.
Community… Repo maintenance,
Sven Cowart (ElastiFlow Inc) 00:43:03 Oh, I see. Okay, I didn't know that was there.
Got it.
Trask Stalnaker 00:43:07 Yep.
for the project board, it's not always… I still don't understand the permissions on the project board. I think anybody in the org can create a project board.
But if you can't,
Sven Cowart (ElastiFlow Inc) 00:43:28 Then… I worry.
I… I…
Trask Stalnaker 00:43:31 I could try.
Sven Cowart (ElastiFlow Inc) 00:43:31 Yeah, but I don't know if I'm actually in the org yet, so… I know that the community project was merged, but I don't… at least I didn't get any notifications or anything that…
Trask Stalnaker 00:43:43 What's your, alias? Your GitHub?
Sven Cowart (ElastiFlow Inc) 00:43:46 SPN.
It's just my first and last name.
Yeah, I'm not there.
Trask Stalnaker 00:43:54 Okay. Okay, well, we gotta get that fixed first. Okay, cool. And then, when you request the, the repo, you'll need to give, you know, come up with a proposed set of maintainers and approvers for it. Yep.
Sven Cowart (ElastiFlow Inc) 00:44:13 Okay.
Trask Stalnaker 00:44:13 And so all of those people will need to be in the org.
And check in the community repo, there's sort of… Responsibilities document, for… What?
It means wrong.
Always go wrong.
1… Nope, still getting the wrong one.
Yeah, so approvers… And maintainers kind of responsibilities, just make sure that everybody agrees to those, and then, you know, post those in the issue, and You know, I… myself and Marillia do a lot of the, sort of, GitHub repo, maintenance, so probably one of us would pick that up, but I would probably… we would probably check with your GC liaison just to make sure that, you know, that all kind of lines up, so it's good… it would be good to keep Ted sort of in the loop.
Sven Cowart (ElastiFlow Inc) 00:45:20 Okay.
Sounds good.
and is inviting, I… Armin, I saw you post the link. Is that how I get… Request an official invitation into the org, or is that just something you have to do on the back end?
Armin (Dynatrace) 00:45:35 No, that's for you. So there's a link in there to an issue template, and that one will open Issue in the community repo, and then someone will take care of adding you.
Sven Cowart (ElastiFlow Inc) 00:45:44 Okay.
Liudmila Molkova 00:45:45 And you will need two sponsors, feel free to mention me, or I think other people on this call would also sponsor you or Braden.
Sven Cowart (ElastiFlow Inc) 00:45:53 Yeah. Okay, sounds good.
Trask Stalnaker 00:45:58 Yeah, it would probably be, yeah, I mean, certainly any of us who've seen you around, we're happy to sponsor you. These folks can also, Okay.
Liudmila Molkova 00:46:10 that… that debit… I thought it was me, or it was David, the sponsor before, for the whole SIG.
Sven Cowart (ElastiFlow Inc) 00:46:19 Oh.
Trask Stalnaker 00:46:19 Did we not update this?
Sven Cowart (ElastiFlow Inc) 00:46:22 Yeah, it doesn't look like that was updated. I will…
Liudmila Molkova 00:46:25 mind if David wants to sponsor, I just thought it was me.
Sven Cowart (ElastiFlow Inc) 00:46:30 Let me update that, I'll take a… I'll update this today and create a PR for it.
Trask Stalnaker 00:46:36 Was Ted the… let's see, maybe Ted isn't even… let's see…
Sven Cowart (ElastiFlow Inc) 00:46:40 He is still the GC.
Trask Stalnaker 00:46:41 He is, okay.
Awesome.
Sven Cowart (ElastiFlow Inc) 00:46:45 But the information there is wrong anyways about meeting time and Slack channels, so I'll update all that.
Trask Stalnaker 00:46:50 Cool. There's a YAML file where that's all.
derived from.
Sven Cowart (ElastiFlow Inc) 00:46:55 Sounds good.
Thank you so much, that was it.
Trask Stalnaker 00:47:00 Yeah.
Rudiger.
You're next.
Rüdiger Schulze (International Business Machines Corporation) 00:47:07 Got it.
Thank you.
Let me share the screen.
Trask Stalnaker 00:47:12 Yeah.
Rüdiger Schulze (International Business Machines Corporation) 00:47:15 Okay… Just, let me get to right.
Sorry, wait.
Absurd.
Can you see my browser? Yes, I think so. Okay.
A couple of updates just from the mainframe perspective. So, we have, like, a first proposal for mainframe.
metrics from a lowest layer of the infrastructure HMC perspective there.
And we started from the HMC point of view, hardware management console point of view, because this would give us kind of, like, the base of what kind of entities we will have, and what kind of… general kind of, artifacts we need to, to work on. Now, first of all, Ludmila, thanks for putting out the, the, shared template, so obviously this works well.
I have one question about it, I'll come to this in a minute.
Right now, we put everything… under the mainframe namespace, and obviously the mainframe is very much about virtualization, type 1, type 2, and, I had some initial discussions, I also showed this at the mainframe SIG last week, and I think what comes out of this discussion is actually that we want to align more with some generic definitions around virtualizations, and secondly, also make more reuse of debase semantic conventions.
And the question that I have is on virtualization, and we discussed this, I think, you know, a couple of months ago already. If we want to start with virtualization as a concept, as a domain.
would it be the right approach if, in the first place, we just define this in the scope of our SIG as a separate namespace, and then concepts underneath, and then bring this back, or should we somehow treat this Differently, in terms of, you know, how we proceed here.
Trask Stalnaker 00:49:40 Sick.
Good question, Adonte.
I don't think we have at least prior art for… That, since we're kind of just new in the federating out and haven't brought things back in yet.
So, just… Seeing if anybody else has thoughts here.
Liudmila Molkova 00:50:11 Well, we, we kinda… I think we, we did it, but in the, in the… You know, sandbox keys when we… Worked on specific, let's say, databases, right?
were RPC systems, we frequently had Something defined for each system individually, and then we realized that that's a common concept, and maybe it should move up.
And it comes with breaking changes.
But we never know ahead of time whether it's a common concept. Oh, in this case, you're saying virtualization, and essentially we know it's a common concept, we just might not have the other Parties interested in.
Outlining the common parts of it.
Rüdiger Schulze (International Business Machines Corporation) 00:51:03 So, right, virtualization, you know, we would like to keep this generic, so applicable to any vendor in this space.
And… You know, then just build on it as a… As a federated Semantic Convention for mainframe, obviously, but… I think, given that we don't have virtualization yet being defined, you know.
We could start with it in our domain or in our repo, but then, I guess, at some point we would want to bring it back, or… Should it be a separate repo that we build on?
Liudmila Molkova 00:51:44 I think it cannot be a shirt.
repo.
It's just not practical.
But… I kind of… it would be nice if it… start… it would be okay if it started in mainframes, as long as we had some pointer from the Core Semantic Conventions saying, okay, virtualization, it exists there.
which is don't have it in this repo, and if you're interested in having it somewhere out of mainframes.
go work with mainframe people and, to build the group that we don't… if we… just… there is no… process that allows us to put it in Semantic Conventions today. There is no group.
but we can't put a link.
Saying it's over there.
Rüdiger Schulze (International Business Machines Corporation) 00:52:40 I would be okay with starting in this way, right? So, we do some base definitions, And, if there is also input specifically just for virtualization, we would take that in, obviously.
And, Then at some point, if this is stabilized, we could, you know, have a discussion around bringing it back to the base.
Okay, let's do that, that sounds like it.
Trask Stalnaker 00:53:05 Makes sense.
Rüdiger Schulze (International Business Machines Corporation) 00:53:06 Yeah. Sounds like a plan.
The one question that I have, Liudmila, on the shared template, how is actually the… template behaving, or supposed to behave for… for refinements. I believe I had the observation that if I do a refinement on an Existing entity… like host, for instance, so the type would be preserved, but the ID would be different. Then it looks like if I just do auto-generation of the documentation, the entity is actually not being shown.
Within our repo here for documentation.
Is the process here that we explicitly have to reference it so that we can get it, or… Do we… or miss maybe something we want to fix on the template?
Liudmila Molkova 00:53:57 I think we should fix it on the template. I… they didn't add templates for refinements, just to keep it under, like, like, keep scope at least somewhat reasonable for this PR.
We can add… Refinement registry.
Right.
Rüdiger Schulze (International Business Machines Corporation) 00:54:14 Okay, yeah. Okay, sounds good.
Liudmila Molkova 00:54:18 bye.
Would you be interested in… adding it? Yeah, let me…
Rüdiger Schulze (International Business Machines Corporation) 00:54:27 Let me look at that. If I… if I manage to get this in, then… then I'll send you a PR, or send generally a PR.
Liudmila Molkova 00:54:36 Yeah, and as I mentioned before, AI is super good at templates. I would not touch them by hand, but if you ask AI to follow the we would evaluate… I would evaluate it based on the outcome, rather than what's in the ginger. Yeah, yeah.
Rüdiger Schulze (International Business Machines Corporation) 00:54:52 Right.
I don't want to take too much time, just one last comment here. We spoke also last week on the V2 definition, or migration to… of the CS entities and the base to V2.
It's underway, I still have a couple of checks failing on the PR. Once I have solved this, I get this over and open it.
And,
Liudmila Molkova 00:55:17 Awesome.
Rüdiger Schulze (International Business Machines Corporation) 00:55:18 Then, then you can use that.
Okay.
Thank you.
Liudmila Molkova 00:55:23 Thank you.
Trask Stalnaker 00:55:27 Alright, diana?
Virginia-Diana Todea (VictoriaMetrics) 00:55:33 Yeah, hello, hi everyone, So, yeah, so… so my question was… well, my question was, there is a newly started initiative from Green Software Foundation, so the folks from Green Software Foundation created a recent initiative, after Otzel's graduation.
To basically deconstruct their software, carbon intensity, yeah, basically, they're, they're, this measurement that they have, they want to deconstruct it for OpenTelemetry.
So the idea is to use whatever cloud-native Semantic Conventions we already have, so not to reinvent the wheel, basically.
Creates this so that they could give us, some kind of… translation, or some kind of, like, yeah, basically, like, a translation for OpenTelemetry, and from this point onwards, Open Telemetry as community can starts doing its work in that sense. So, I know this sounds quite… I don't know, if you're not familiar with what Greece Software Foundation is doing, or the CSI, it's kind of difficult to explain it in 5 minutes, but I wanted to give you a heads up that this is happening.
And definitely what we also want… I mean, what we also want, what the logical question would be afterwards, is to maybe create a subgroup from Semantic Conventions where we can discuss this particular… about this particular initiative.
Yeah, it just started, so there's not anything defined yet. Probably, according to them, this will take around 3 months or so.
This initiative is currently a blend between GridSoftware Foundation folks and OpenSelemetry folks, so we are, yeah, working on this at the moment, but it has a definite impact on Semantic Conventions and would be a good idea to take it into consideration from now, and, I don't know, have your opinion about it.
Trask Stalnaker 00:57:55 So, I think somebody came and, discussed this with us before.
So this is a great, kind of use case for this, probably for these federated semantic conventions that we've been talking about, where, the core Semantic convention repo… We have… we're unable to have that just grow indefinitely.
And so what we've invested in is tooling and, around federating, where people like, GraphQL, like, Oracle, you know, vendors can have their own semantic conventions that are built on top of the existing Semantic Conventions, reuse You know, where it makes sense, but then build their own… maintain their own.
And we don't need to be a bottleneck, for that work.
So I would definitely encourage, you know, and it is still new work for us, these sort of federated semantic conventions, and… the current, sort of probably best example is within the OpenTelemetry community, but it doesn't need to be, and so this repo Here kind of shows a good example of how A new semantic convention can be built on top of the core, but live in its… in a separate repository.
Virginia-Diana Todea (VictoriaMetrics) 00:59:43 Okay.
Perfect, yeah, I'm aware of the GenAI. So, let's say a priori, like, let's say 3 months or so pass by, we are at the point where you know, Grace Hopster Foundation and Open Seminary folks, they make this baby, you know, ready for exploration, and they hand it to us, like, here you go, have it, have fun.
You know, from OpenSelemetry, side, so we should kind of, like, prepare and create this, like, repo and create our… I don't know, maybe, like, a… SIG for it, or sub SIG, some kind of Slack channel where we kind of discuss about this stuff, or… Just to know the guidelines, so we don't…
Trask Stalnaker 01:00:27 Yeah.
Virginia-Diana Todea (VictoriaMetrics) 01:00:28 I'm single.
Trask Stalnaker 01:00:29 So, it kind of depends. In cases where it's multiple, like, commercial vendors, OpenTelemetry community makes a lot of sense to form the group, to have kind of a neutral, governed, body.
In the case of, like, GraphQL, which already has its own org community, and potentially Green Software Foundation, right, they could host that community within themselves, right? And they could own the Semantic Conventions.
And that's sort of… The long term, what… Probably our preference, because it puts the, you know, the domain experts in charge of the semantic conventions living there.
And of course, if there's… you can always come to this meeting and consult with us on, you know, questions.
Virginia-Diana Todea (VictoriaMetrics) 01:01:26 Yeah, okay, so just, I mean, as far as I understood from them, as of now, they don't want to take the ownership of this, so they don't consider them as to be the owners of this, they just want to prepare this, so basically they take their expertise.
they deconstruct the CSI, they make it, let's say, ready for Open Celemetry, and after this, let's say, completion date, they hand it over to OpenSelenetry, so it's completely… From that point onwards, in our hands, let's say, our responsibility. They don't want to grab it, they don't want to have the ownership, they don't want to be any vendor.
They just want to create this kind of, specification, let's say, for open telemetry. And then it's our responsibility to do Whatever needs to be done.
Trask Stalnaker 01:02:16 So, sorry, we ran out of time. Would love to chat a little bit more about it, because it sounds like there's some complexity here.
Yeah.
would love to chat, because to us, these Semantic Conventions is just a specification, so, you know, I think I would kind of push back on them of, like, why not own it? Like, it is just a specific… if they're okay with the specification.
the Semantic Conventions is nothing more. It's not… they wouldn't write instrumentation, they wouldn't be a vendor, that kind of thing.
Virginia-Diana Todea (VictoriaMetrics) 01:02:49 Okay.
Okay, good to know. Yeah. Yeah.
Trask Stalnaker 01:02:53 Yeah, and feel free, if you want to loop me in, ping me in Slack, yeah, I've chatted with various third-party folks about it, so I'd be interested in learning more.
Virginia-Diana Todea (VictoriaMetrics) 01:03:05 Perfect, that sounds good. Thank you so much, Trask, and let me know. Thank you.
Trask Stalnaker 01:03:10 Play out.
Virginia-Diana Todea (VictoriaMetrics) 01:03:12 Bye-bye.
