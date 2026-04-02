SIG: RPC Sem Conv Stability SIG
Date: 2026-04-01
Duration: 41 minutes
============================================================

## Zoom Recording Transcript

**Trask Stalnaker** 00:27 Yes, video's not failing me.
Hello, ghosts and goblins!
**Ghosts N Goblins (us-svl-mp5)** 00:36 Hi, I'm John from the GRPC team.
Hi, Matt. Nice to man.
**Trask Stalnaker** 00:41 Gotcha.
**Ghosts N Goblins (us-svl-mp5)** 00:42 Lumila, and Kukong, last week, and… Following up here.
**Segway (us-svl-mp6)** 00:49 And I'm Eric from GRPC Team.
**Liudmila Molkova** 00:54 Awesome. Great to see you.
**Trask Stalnaker** 00:56 I know you as I Jonah.
**Segway (us-svl-mp6)** 00:58 Yes.
That one.
**Trask Stalnaker** 01:03 Yes, one of my early open source experiences was in the gRPC repo, and you helped me with some stuff, where I submitted some repros for some stuff. Very cool to meet you in person.
**Segway (us-svl-mp6)** 01:19 Hope it was positive.
I… your… your name seems familiar. It would have been… it would have been older.
a while back.
**Trask Stalnaker** 01:33 Probably 15 years ago.
**Segway (us-svl-mp6)** 01:39 It's been a while.
**Trask Stalnaker** 01:44 Well, we are excited to have you all, join and chat about what we can do here, how we can move forward. Definitely, we are very motivated to… Converge and have a single RPC semantic convention that… in the industry, and obviously, gRPC is a huge player there, so, I think if we each had different ones, that will… that would essentially create two de facto standards, which is… Not great for… Folks.
So, yeah.
curious what your… if you all have… I know the last time we chatted with the team, there wasn't… an ability on your side to participate in the RPC semantic conventions, and, so would… Just… we went forward, and… did what we thought that made sense across, we involved We had a couple of folks from, Alibaba, Dubo, Apache Dubbo, and… Yeah, have you all had a chance to review the… the release candidate that we put out for RPC semantic conventions?
Are there specific concerns that you all have about them?
I guess we're kind of looking to you all for the next steps, sort of, from Your, you know, your perspective.
**Ghosts N Goblins (us-svl-mp5)** 03:43 Yeah, so… I am mainly here in the capacity of pulling resources together and organizing things.
We do have Madav on the team, who's based in Bangalore, and so the meeting time is not good for him, but he's kind of taken up the lead position for us on the telemetry work.
But he's, he's, like, fairly new to this project for, for us.
And yeah, like you mentioned, our previous representative here, Yash, moved to a different team, and so It's been… like, the seat has been unstaffed for, you know, 6 months or something?
And so, yeah, we're interested in kind of learning about, what's here, and, Understanding, you know, we'll probably need to take a little bit of time ourselves to understand what the diff is between, like, what you're proposing for, For your RPC schema, versus what we have.
Currently?
And then, like, you know, we can… we can discuss what the… what a reasonable way forward is.
**Trask Stalnaker** 04:56 Yeah, you… have any timeline in, mind there? Because, I mean, we… You know, we are really… pushing to stabilize things in OpenTelemetry, and… So we did go through a fairly significant effort on our part to put out the RPC release candidate semantic conventions.
And we are, in the middle of Or getting towards the end of prototype, putting out prototypes for those, just to… You know, across the… Cross our T's and dot our I's.
And would like to stabilize Soon.
But certainly if you all, you know, can commit to getting involved and commit to some… something, then we would be… Very willing to, you know, kind of push back our timeframe, but we don't want to just… be like, oh, okay, whenever is good. You know, we don't… we don't want to just open the door up.
indefinitely, so… I'm not sure if… there's… I know you all reached out on… There was a semantic convention issue asking us to kind of hold off on the release candidate.
**Liudmila Molkova** 06:22 Or…
**Trask Stalnaker** 06:23 stabilizing so, again, I think we're kind of looking to you all to… You know, give us some concrete… something concrete that we can use to justify, you know, delaying at this point, or, you know, what are the next steps from your perspective?
**Ghosts N Goblins (us-svl-mp5)** 06:46 Right, so, like I said, I'm… I'm here sort of more in a capacity to pull resources together, so I can… I can definitely get folks going on this and hand this off to… to Madhav, who, is sort of leading from our side. Eric, you've got some experience here also. Can maybe speak to, like, how long it would take us to do… Sort of a rough audit, And then we can kind of think about what that means in terms of a timeline.
**Segway (us-svl-mp6)** 07:16 Yeah, so I see the… the… like, I got… I went to the doc that's on the screen, which does have the pretty direct comparison, which is helpful. And then I also see the… semantic conventions published on the OpenTelemetry.
Just .io.
Although that's… 1.40.0, is that still the… the… Yeah, status release candidate.
**Liudmila Molkova** 07:47 Relevant, yeah.
**Segway (us-svl-mp6)** 07:48 Yeah.
So, those definitely help in people coming up to speed on what y'all have gotten up to this point.
**Liudmila Molkova** 08:00 Yeah, and maybe there is one thing that's not directly mentioned, but whenever you see that there is no equivalent, we want you to have your gRPC-specific thing there.
It's just, we want to introduce something in common that's, like, horizontal, and then there is specialized gRPC telemetry, it's all yours, we don't… We're not going to unify this in the foreseeable future, maybe never.
**Segway (us-svl-mp6)** 08:28 Yeah, so then that would… that would be… and so if we've got the, let's say, the gypsy client call duration, that very first one, that… we would do… the idea is to instead do the RPC client call duration.
**Liudmila Molkova** 08:44 Right.
**Segway (us-svl-mp6)** 08:44 And we wouldn't publish both.
But for these other ones that have no equivalent, those would get published as they are today.
**Liudmila Molkova** 08:52 Right, or how…
**Segway (us-svl-mp6)** 08:53 Like, submitted, you know, the metrics, yeah. Okay.
**Ghosts N Goblins (us-svl-mp5)** 08:57 And I guess… I guess, like, part of our question, right, is it… is it literally just the label change, or is it, like, measuring potentially slightly different things?
**Liudmila Molkova** 09:06 It's… it's the semantic difference, right? So, there are subtle differences. So, for example, you would see that we have some common attributes that are not specific to our PC at all, or that we, have a slightly different, Semantics of how we record errors, so that people don't necessarily know the status, but they can also see that some of them are errors and others are not.
In general, for metrics, it's just the… semantical differences, the metrics, or So this total logical metric is the same thing structurally.
For spans, I think it's also pretty much the same.
Though we put quite a little bit, more details on the spans.
I think, what, what's currently in JRPC, it's just, Bare Bones Pen, so it's just a name.
But structurally, things are the same.
And we… we're… Consulted a lot with your docs, and we consulted a lot with your instrumentations to make them.
Relatively similar.
**Segway (us-svl-mp6)** 10:26 So, just by quickly glancing, I think JRPC Target will be fun to discuss, just because the semantics there are wildly different.
for a higher level, our call, it's not to a server address and a server port. We have neither of those values.
you know, if you're doing simple things with DNS, then yes, you do have those, but that is nowhere near guaranteed for us.
So that we'd have to work through some of those. I see the errors, we'll have to read up on that, but I think that that… Is probably a little bit more ordinary.
The… so… so, gRPC Target we'll have to mess with, and then, The other question is, from y'all's perspective, how… so, so, inbuilt retries… Definitely… a lot has… we've spent a lot of time trying to figure out how to deal with the retries and what metrics to show for what things, how do you represent those. From… This… these semantics perspective.
If gRPC inside of itself can retry whenever configured to do so.
Is that… is each attempt going to be one of the OpenTelemetry metrics for duration, for example? Or is it for the entire conceptual RPC from sort of a higher-level API perspective, what the application sees. Which of those two perspectives?
I'm asking that mostly because I sort of figure y'all might have an immediate response.
**Liudmila Molkova** 12:09 Yeah, so, like, the goal is that we only cover the logical part.
And the physical part is essentially RPC-specific, right? For some protocols, I don't know, if JSON RPC is modeled, the HTTP or whatever, STDIO could be the protocol. We don't target it in the generic RPC conventions. So the only thing we actually propose there is the logical layer.
And physical, the protocol one, remains yours.
**Segway (us-svl-mp6)** 12:45 Okay, I'm not sure that it's really the physical or not perspective, but since you brought up standard I.O, for standard I.O, it just wouldn't have a server address or a server port.
And Unix Domain Socket also wouldn't have these.
**Liudmila Molkova** 13:04 Oh, Unix domain socket is the server address, the name of the socket.
But yeah…
**Segway (us-svl-mp6)** 13:10 Address is the name of the socket.
**Liudmila Molkova** 13:11 Yeah.
**Segway (us-svl-mp6)** 13:12 Okay, so then that…
**Trask Stalnaker** 13:13 And that's how we dealt with… yeah, that's exactly what we did, if you look at the definition, you know.
How we defined, server address is, yeah, because it's not… doesn't have to be an actual server IPv4, or domain address.
**Liudmila Molkova** 13:34 We would even put the… the whole… Target if it's not… a DNS into server address, because it essentially becomes your gRPC target.
**Segway (us-svl-mp6)** 13:46 Where is this?
-Oh.
Oh, this is your other doc, okay.
**Trask Stalnaker** 13:55 The reason we went that route is, that becomes helpful for a lot of backends which do, like, your distributed tracing already, keyed off of server address, aggregating, drawing maps.
And so that allows the RPC and gRPC conventions to get automatically picked up by those.
**Segway (us-svl-mp6)** 14:26 Okay.
And so… Yeah, and if this is gonna be… so, so… How much… What people expect when using these, to see… A match between the client-side and the server-side entries.
Like, is it one-to-one?
**Liudmila Molkova** 14:54 No, no, we wouldn't even expect, by default, that the server side reports relevant server address, because you never know on the server side what is the address that client hit.
**Segway (us-svl-mp6)** 15:10 Okay, okay.
**Liudmila Molkova** 15:12 So ideally, like, in the perfect world, we want them to be the same, but in practice, it's not even the case in HTTP.
**Segway (us-svl-mp6)** 15:19 Well, yeah, so for, like, retries, that… that would… they would… there's no relationship in the cardinality, or, like, how many you have. You, like, you have one initially, sure, you… they may never hit a server, that's normal even in HTTP, but you might see three.
server RPCs.
**Liudmila Molkova** 15:42 Yeah, so here, like, for… because it's a logical call, I think we even suggest that people use the target string to… that was given during the configuration, and not the actual Thing, specific request hit.
**Segway (us-svl-mp6)** 16:00 And then I guess that's true even for HTTP, it's not the resolved IP address, it's the host name, and so that can be any one of a bunch of different things.
**Liudmila Molkova** 16:11 Yeah, unless somebody gave the IP address during configuration, and then it's an IP address, but there is nothing we can do about it.
**Segway (us-svl-mp6)** 16:20 Okay, and so on client side, it's normal to not know which server was hit, like this specific, you won't have an IP address, you expect that there's a little fuzziness in there, and then, the client side… oh, sorry, the server metric side, I'll have to look at those.
Okay, so this doesn't Go quite a bit into it.
**Liudmila Molkova** 16:44 Now go ahead, truck.
**Trask Stalnaker** 16:46 For some comparison with HTTP, since it's a little bit lower level, we have… we actually support both, where sometimes the retries are modeled as individual spans, and sometimes it's at the logical layer. Often it's We prefer to do it at that reach physical retry level, per retry, but a lot of the instrumentations just don't even have that information available, so they have to do it at the logical layer.
**Segway (us-svl-mp6)** 17:21 I see. So you mentioned the span there for talking about the tracing?
**Trask Stalnaker** 17:26 Yeah.
**Segway (us-svl-mp6)** 17:27 We… we… so we have it at both layers, exactly when we know what, some things can get a little funky with, a little bit more than a unary, like, simple request, simple response. Just… I'm sure y'all saw that streaming, makes things a little more complicated for us.
So, for the… So the… so the tracing, you would see… for the spans, you would make… you would hope to see both, and we can look at those semantic conventions to sort of see what they would look like at both layers.
**Liudmila Molkova** 18:06 Phonological.
For our piece.
**Trask Stalnaker** 18:09 the… Yeah, go ahead.
**Liudmila Molkova** 18:12 we only tackle for open telemetry, semantic conventions, we only target the logical layer. It does not mean that there shouldn't be a physical layer for each tray. It's just we don't cover it in… RPC semantic conventions, because we target the logical RPC layer, right? It's not protocol-specific.
Essentially.
**Segway (us-svl-mp6)** 18:37 Okay, so… If we have access to both.
then we should do the logical. But it's that some systems only are closer to the… something lower level, and so they give a little bit more of that perspective, and some things are closer to the logical, and they give a little more of that perspective. But if we have both.
Logical is the one we do.
**Liudmila Molkova** 19:00 If you have both, then the logical is the one that we really want to do generically for different RPC systems, but you probably… there is a lot of value in doing the physical, too.
**Segway (us-svl-mp6)** 19:17 And so then we would just do what we currently have in that space.
**Liudmila Molkova** 19:20 Actually, yeah, however you want to do this, yeah.
**Segway (us-svl-mp6)** 19:23 Okay.
I'm mostly trying to ask questions and stuff.
that I think Madav will end up asking. Like, that's… That's what I'm mostly trying to do here.
Let's see…
**Liudmila Molkova** 19:47 Do you think, like, it would be helpful if we meet with him? We can do, I don't know, a one-off call that's probably better for his time zone, or we can, like.
How can we work together going forward?
**Ghosts N Goblins (us-svl-mp5)** 20:05 Yeah, I think that would be helpful. Monov is primarily on Go, and so we probably also want to make sure that we have Representation from, from our other primary languages.
To understand, like, you know, again, what's here, what the differences are from what we currently have.
Hmm.
And then, yeah, Eric, do you have a sense of, like, you know, roughly… the effort… It would take to kind of determine I think that, like, probably… The big thing to me seems like incompatibilities where it's not a simple label change or some metadata that is kind of easily known.
Are probably the areas where We'd want to kind of highlight the most.
Do you have a sense, Eric, of, like, what that would take?
**Segway (us-svl-mp6)** 21:21 So, I mean, a lot of this, it talks about the conversion to do and such, We would need to do those conversions for each time we record these metrics.
There might be a little bit involved there, but I guess it's not too bad.
Like, from a performance perspective or anything like that.
For, for reference, so these labels, Several of them have been defined.
How much do y'all care about us using those labels on our own metrics? If there was… Should we… do we look at migrating all the things that are… Are similar across all of our metrics, or is this mostly for the metrics that are defined in the semantic conventions?
**Liudmila Molkova** 22:17 Yeah, that's a great question.
**Trask Stalnaker** 22:22 I would say it's, I mean, the most important thing is the metrics.
that are defined in semantic conventions, but I think users would also expect The… to see the same attribute… semantic convention attribute names on your metrics as well, if they apply.
**Liudmila Molkova** 22:52 Yeah, also, if, like, how we do this, of course you don't have to, but instead of doing the conversion, we usually give people an opt-in, and the instrumentation itself, It has this configuration option allowing to emit old or new conventions.
Or even both, it's not possible for metric names, but it's possible for attribute names.
And, like, when, if we ever release a new major version, then we switch the default.
**Segway (us-svl-mp6)** 23:28 So, I saw that. I'm… I'm not quite sure… how that's… plumbed, because OpenTelemetry isn't… like, these strings are being passed into OpenTelemetry, yep. So, is there… is there an OTEL API that we would call to see if it's supposed to be the old or the new, or do we just… are we supposed to look at the environment variable ourselves, or something like that? Okay, okay.
**Trask Stalnaker** 23:59 Yeah.
**Segway (us-svl-mp6)** 24:00 We do have a, like, a builder configuration object that the user interacts with.
Where they can… Tweak some of this.
Because, for example, OpenTelemetry doesn't tell us whether or not something's actually getting recorded. We can learn, do we actually push these details? Like, do we… we compile these… these details to… to push into OpenTelemetry or not? It can do a couple different things. Anyway, but there, there is an option for… having an opt-in, opt-out, various forms of… of things.
So we do have that, but if there's the environment variable, and that's normal, then we can use that.
**Trask Stalnaker** 24:49 I'd say it's less important to… that you use the specific environment variable, especially since you're not coming from the… old OpenTelemetry RPC schema to the new one, which is sort of what that is specifically targeting.
As much as just having that as a strategy for however you're handling, Breaking changes to telemetry.
**Segway (us-svl-mp6)** 25:18 Okay, then our own config object might be the way to go, because we do have the problem also that individual libraries will use GRPC inside of them, and they want to push their metrics certain places.
And so, it's not global configuration, really. You can have, like, 3 different syncs for where do the metrics go. And they're all using OpenTelemetry, but they're each configured for a different perspective, and a different… You know, there's just so many parties and binaries these days.
Okay, so then that would also allow us to give each of those the appropriate… freedom to configure. Okay.
**Trask Stalnaker** 26:04 What is your, I'm just curious, what is your general thinking for breaking changes to telemetry? Would that be… I mean, initially you would… offer that as an opt-in? Would you… do you have major version bumps, or are you comfortable with, at some point, changing the default to be the To be stable semantic conventions someday.
**Segway (us-svl-mp6)** 26:32 So, it's… so… There are many of ours that are marked unstable. Unstable metrics where we can change.
Stable metrics are forever.
Whether a staple metric is enabled by default, basically, once it's enabled by default, it's enabled by default.
Sort of forever?
It's a little hard to change that. In some cases, let's say tracing. Tracing isn't… Become finalized yet, so everything there is still fair game.
everything is so new in general. OpenTelemetry is also moving along and stuff. I don't know if there are certain affordances where we cheat a little, but, I could see, potentially, worst case being an option on the builder that says, use modern open telemetry. Like, you know, whatever. Whatever that means. Use… use the settings you wish we had by default. I don't know. That's probably the worst case in my mind.
If we can do better than that, we'd have to.
**Trask Stalnaker** 27:47 Yeah, yeah.
**Segway (us-svl-mp6)** 27:48 it would… I think some of the ones y'all are talking about here, we've… we've stabilized. And so those are… will be there.
And some of them are enabled by default, so those will be there. We do let people choose, as I said, choose which ones they want us to export, and so they could add and remove some of those. We can work on some of that. That would be on us to figure out what things make sense. We could get those down to a few choices, and then bounce it off of y'all to see what makes the most sense from a larger open telemetry ecosystem perspective.
But.
**Trask Stalnaker** 28:27 Yeah, and we are…
**Ghosts N Goblins (us-svl-mp5)** 28:29 We are… I also…
**Trask Stalnaker** 28:30 Oh, go ahead.
**Ghosts N Goblins (us-svl-mp5)** 28:32 Oh, sorry, I just wanted to, like, clarify, our position, which is, like, we very much would like to unblock you, but, we're not ready to commit to, like, whether we'd pick this up or not yet. So, like, we'll do our due diligence, and, you know, our goal is to try to make this work.
But, you know, we both have limited resources, and, you know, like.
we've already kind of built out, what we have for metrics, and as Eric said, it's hard for us to sort of drop those as the default. And then there's also performance implications as we… like, if we need to have duplicate things or things like added into the codebase to measure differently. There's, like, overhead that gets added there, and so those are just some of the considerations that we're, that we're looking at as we're, you know, kind of considering this. That said, like, I would like to, you know, this is definitely, the preference for us is to do this with you.
We're just not there yet.
So on.
**Trask Stalnaker** 29:36 I was gonna mention there's, There's a declarative configuration model, that has… The basic SDK declarative configuration model has been stabilized recently, but we're building out Other parts of that, which… include semantic convention targeting, version targeting, which will allow users to basically say, you know, I want this version of semantic conventions, at least a standard place to put that information.
in that.
**Segway (us-svl-mp6)** 30:14 shows up through the API, it's not just on the SDK?
**Liudmila Molkova** 30:18 Yeah.
**Trask Stalnaker** 30:19 Yeah, so there is a configuration API now.
That will give you access to that.
**Segway (us-svl-mp6)** 30:27 And so that would… there's an API for that for the metrics and the tracing, both?
**Liudmila Molkova** 30:34 It is there.
**Trask Stalnaker** 30:35 a single… configuration API that gives you access to the configuration structure, and then you can read those nodes from that specific nodes that are then established in the configuration schema.
That will tell you semantic convention, RPC, I want version 1 stable.
**Segway (us-svl-mp6)** 30:59 I'll have to see how that works in the various languages. Java's the only one that we have a nice, clean API, like, that we receive the entire API object, so we can look at what we need to, and we can turn on tracing, and, you know, we can just get everything. I think most of the other languages get, like.
the meter provider, and they get the… the… whatever the tracing thing is, they get those things separately, so we may not have access to that right now. Like, someone could pass it, and then we could start using it, and we… but, I'd have to look at just… I'm sure y'all know the shape can be slightly different in languages, even though y'all do define how y'all wish the shape were, oftentimes.
**Trask Stalnaker** 31:43 Yeah, yeah, I just wanted to throw that out as a kind of a longer-term, like, as you're thinking of how to… if you do need to stay on your current, you know, metrics by default, but then that could potentially be an avenue to allow users the standard open telemetry Opting into certain… the new stuff.
**Segway (us-svl-mp6)** 32:10 That's true. And in general, those sorts of things, like, in… generally, I would prefer to query OpenTelemetry for it to tell us what to do, as opposed to maybe the user has to configure it in both gRPC and OpenTelemetry, or those sorts of things. So yes, if… If there's those options, that sounds actually, definitely worth looking into.
**Trask Stalnaker** 32:35 Yeah, it's… that piece is, bleeding edge, still unstable, so, like, if you want to play around with that, just, feel free to ping me. I can, especially if it's Java, I can send you some code.
**Segway (us-svl-mp6)** 32:49 Yeah, and we can… there's short-term plans, and longer-term plans, and medium-term plans, and everything like that.
We can't depend on the unstable stuff, or at least not easily, just because it creates DLL hell. But we can at least get things in place so that whenever things land, you know, that would be a possibility, so that whenever things land, things get better. Plan for the future.
**Trask Stalnaker** 33:17 I have a… there's an unstable gRPC Java feature that I want to be stabilized to give us access to the, to tracing.
Sure.
**Segway (us-svl-mp6)** 33:27 No, you want the trace con… the, the…
**Trask Stalnaker** 33:31 thingy, where we get the GRP.
**Segway (us-svl-mp6)** 33:33 My stream tracer.
**Trask Stalnaker** 33:36 Yes, yes.
**Segway (us-svl-mp6)** 33:37 Yeah, and the problem is, is that's, like, never. It won't, because it's, it's, it's… it's integrated into GRPC to the point that any changes we do are likely to technically disrupt it.
And so we can't… the only way we can provide a staple API there is not to change the internals.
But, I… I know… yes, it is a… it is a thing. You're…
**Trask Stalnaker** 34:05 Yeah, my second request, then, is… Let's get this convergence done so we can delete our gRPC instrumentation in OpenTelemetry.
**Liudmila Molkova** 34:16 That's exactly what I was going to say, we only need access to this API because we do our own instrumentation. If we didn't, then there would be no need.
**Segway (us-svl-mp6)** 34:24 Yeah, that sounds… yes, that would be our preferred way to give y'all just what you need. Y'all don't need to keep track of what our internals are doing and stuff like that. And then there's also not two different implementations floating around, and people have to choose which one to use.
**Liudmila Molkova** 34:41 How… what are the next…
**Ghosts N Goblins (us-svl-mp5)** 34:43 Excellent.
**Liudmila Molkova** 34:44 Thank you, thanks.
what would be the next steps for us? How we can continue this collaboration and try to… I understand we are constrained on resources on both sides. How can we move forward and maybe see what we can accomplish?
**Segway (us-svl-mp6)** 35:01 So, some of this Madav will need to… to look at and stuff. We're gonna have to find some time on, like, how much time are we dedicating?
And then see who else we're bringing into it for other languages and implementations and stuff on our side.
I sort of… there's many layers here. I sort of expect… Some of those to happen in parallel, like.
we'll try to do the first things, and then some things might linger, and then we'll get on to some other things.
But, I think it's gonna be a little bit of… let's still coordinate, between John and Madhav.
I mean, you can CC me too, you had mentioned a meeting or something like that. Let's… let's give Madhav a little time to read some of the documents y'all have, to watch this video, and just to come up to speed, because, like, I've been… I've been in the weeds a lot more, he's looked, he's not, like, foreign to it, but, I've been poking my… eyes in occasionally. So then I guess either he will suggest, like, hey, I'm ready, or John will suggest, hey, I'm ready, and then we do any discussions. I'm sure we're gonna have some lists. I don't know if async is going to be working the best for everyone. I assume at least one meeting, sort of face… faces is good, even if it's not regular.
**Liudmila Molkova** 36:42 Yeah, sounds good.
**Trask Stalnaker** 36:44 Yeah, we'd love to meet with Madhav as soon as he's comfortable, just… even just having an initial chat, kind of filling… we can help fill in some, some areas for him.
**Segway (us-svl-mp6)** 37:00 Yeah, so I do see things being able to be good, like, there's avenues… we can work through this. Timelines… is still… those are always the fun thing. I need to talk to John Moore, I need to talk to Madav Moore, and see where that's going to be all going.
I know there's gonna be a few things here and there that we need to… we need to look through and argue amongst ourselves on how do we feel. Especially, like, I brought up performance, like, in some languages, what we're talking about performance is not… It's like, this is… this is peanuts. For C++, The performance can… can… seriously matter, to a almost degree, like, like, we're, we're, we're… counting nanoseconds, counting microseconds at times, for certain operations and things. So, like.
We'll work through those, we need to work through those, but, I also know…
**Trask Stalnaker** 38:02 Feel free to…
**Segway (us-svl-mp6)** 38:02 around too much for our intro.
Licoracious.
**Trask Stalnaker** 38:06 Feel free to argue with us, also, like, if you…
**Segway (us-svl-mp6)** 38:10 Sure, sure.
**Trask Stalnaker** 38:10 Things that, you know, you would like to, that aren't quite working out for you.
**Segway (us-svl-mp6)** 38:17 That sounds… that sounds completely fine, yeah. I mean, this is why I was saying we need to figure out how do we feel about things, and if this is like, yeah, that's fine, or yeah, this is gonna cause a problem, and then we can spend the time on what the problems are.
And come to a resolution there.
**Trask Stalnaker** 38:37 Sounds good.
**Segway (us-svl-mp6)** 38:42 But yeah, the… some of these documents you put together, I hadn't seen the… that… that… Was it the compatibility doc?
Yeah, I hadn't seen the GRPC compatibility doc, which shows things pretty clearly.
**Trask Stalnaker** 39:00 Cool, let… will you let, is Madava on the email chain?
And… Yes, yes, okay, great.
Cool. I'll reply there. Also, just let him know that, we're on the CNCF Slack, if he wants to jump on and DM myself and Lydnila.
**Segway (us-svl-mp6)** 39:26 I'd actually…
**Trask Stalnaker** 39:26 We're happy to chat, you know.
**Segway (us-svl-mp6)** 39:28 To point out, yeah.
And I'll… I'll… I guess two of these links in particular, I'll also send in the email, just so he's aware. Along with the… I saw the link in the meeting notes here for where the videos get posted, that sort of thing.
**Trask Stalnaker** 39:45 Yeah, Edge takes maybe, like, half an hour to an hour after the meeting ends.
Should be there.
**Segway (us-svl-mp6)** 39:52 Sounds good.
**Trask Stalnaker** 39:56 Alright.
**Liudmila Molkova** 39:58 Nice!
**Trask Stalnaker** 39:59 Yeah.
Thanks for jumping on, glad to let me know. I don't know, who did you run in… who did you… did you talk… meet… John there, or somebody else at Google?
**Liudmila Molkova** 40:10 Actually, John stopped by, by the OpenTelemetry booth. I wanted to ambush him during his talk, but he did it before.
Before I meet ya.
**Trask Stalnaker** 40:22 Nice.
Awesome.
**Liudmila Molkova** 40:24 Yeah, thanks a lot for coming, Eric.
**Segway (us-svl-mp6)** 40:27 I'm glad I was able to.
**Trask Stalnaker** 40:31 Cool. Hope to see you again.
**Segway (us-svl-mp6)** 40:32 And Trask, I checked, 2016, I think it was.
**Trask Stalnaker** 40:36 I think I found.
**Segway (us-svl-mp6)** 40:37 I think I found it.
**Trask Stalnaker** 40:40 Awesome. Yes.
That was very memorable. I was like, yes, Ijona likes my repro!
**Segway (us-svl-mp6)** 40:52 I feel like… I feel like it's been… I feel like we've crossed paths once after that, at least, but.
**Trask Stalnaker** 40:58 Probably.
**Segway (us-svl-mp6)** 41:01 I guess I'll go ahead and drop off, or… Alright. Is that okay?
**Trask Stalnaker** 41:06 Yeah, yeah, I think we're… we're… yeah.
Great to see you.
Bye.
**Liudmila Molkova** 41:13 No.
**Trask Stalnaker** 41:18 Hey, Matt.
**Matthew Hensley / Grafana Labs** 41:20 Hello.
**Trask Stalnaker** 41:22 I think we're… Ending now.
**Matthew Hensley / Grafana Labs** 41:25 No problem, I'll go ahead and catch up on the first bid, the recording, and alright. Shut up a little late, see if there's anything useful I can do there.
**Trask Stalnaker** 41:33 See ya?
**Matthew Hensley / Grafana Labs** 41:34 Alright, see you.
