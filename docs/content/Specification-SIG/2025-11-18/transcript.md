SIG: Specification SIG
Date: 2025-11-18
Duration: 58 minutes
Zoom Recording URL: https://zoom.us/rec/share/SVs6eLYLV0IyQx_MohS72BtxN_RACGz7-4xH6-8k7JuADky73J-S40S_i9g-dpGb.Vv17EjI7EvLGP3ED
============================================================

## Zoom Recording Transcript

**Josh Suereth** 00:59 Welcome, everybody.
**Ted Young** 01:09 Hello, hello!
**Josh Suereth** 01:24 I'm muted. Feel free to add your names and your agenda items. We already have a big agenda so far, so, We might get started relatively soon, but we'll give a few minutes for folks. Apologies, I'm coming off of a little bit of a cold, so if I cough, I'll be muting my microphone, hopefully, at that.
Cool.
Is Carlos on yet? Because I was just gonna wait for him before we get started.
No. Okay. We'll give it a few more minutes.
**Ted Young** 02:16 since we're waiting, maybe I can just bump my FYI up to the top, which is just to… if you haven't read it yet, please read the announcement. We'd like OpenTelemetry to graduate.
And, something we've identified, through the graduation process is there's some cleanup around the installation experience and around, like, stabilizing things, that… would be really beneficial at this time for OpenTelemetry. It's a blog post that tries to… to map all that out. We really want maintainer feedback.
For how to go about this, and how they feel about it, in their neck… neck of the woods.
So please have a read, please give feedback in the OTEL Maintainer channel, or even a discussion on the community board.
**Josh Suereth** 03:15 So, I have two questions for you, Ted. When will the OTEPs start showing up from this blog?
Because I think that it mentions that there'll be some, like, proposals and discussions around that. And then, second, what is Snowtel?
**Ted Young** 03:30 So, I've been calling, this whole thing Snowtel, just because I think projects work better when they have a code name.
And I've just been calling it that because my favorite version of macOS was Snow Leopard.
Mac came out with a thing called Leopard, and it was, like, they had finally pushed one feature too many, and now Mac was starting to get a little buggy, it was starting to feel a little too much like Windows, and so Apple turned around, they said, tell you what, we're gonna have a major version called Snow Leopard.
And all we're gonna do is, like, clean things up and fix, you know, stuff that's been bugging us for a long time. And to make room for that, we're not gonna, like, ship features or do anything else big in this major version.
And I kind of feel like OpenTelemetry needs a moment like that. Like, the SDK maintainers just need 6 months to a year where we aren't… Trying to, like, ship logs, or ship profiling, or ship some crazy thing, and just say, like, hey, just focus on, like.
you know, making your garden nice, and making OpenTelemetry feel nice in this language.
**Josh Suereth** 04:44 Cool. Alright. The second question, I know that there… it mentioned there would be, like, proposals and things to discuss and continue, and you mentioned hotel maintainers is a place for discussion. Where are some of the actual, like, formal proposals gonna be made, and are… do they exist yet?
**Ted Young** 05:03 Well, I think we're gonna make some OTEPs. If you read the blog post, it kind of identifies one way to break things down. So we're gonna try that out as a stab.
But also, like, it's kind of a new way of organizing within OpenTelemetry, right? Like, we tend to just, like, put features into the spec, and then say, hey, you know, everyone implement these features You know, as you can in your language with the availability you have.
This is kind of saying, like, hey, let's, like, try to, like.
clean everything up in the core languages and make everything feel kind of, like, stable and presentable. This is just sort of a different way of coordinating. So that's why I wonder if… you know, we need to be more active on the maintainer's channel. We definitely want maintainer feedback through this process, and to not have it just feel like the GC and DC making TC making dictations.
**Josh Suereth** 06:02 Yeah.
Yeah, that's why I, like, I think we need places to coordinate and run These efforts. Okay, so the OTEP should show up soon, hopefully, and you'll see those on this, on the specification repo. Cool. Alright, so we have a lot to get to, so I assume that was just an announcement, right?
**Ted Young** 06:23 Yeah, totally.
**Josh Suereth** 06:24 Great. Let's move into some of the discussion, and we'll continue on. Carlos, do you want to take it away?
**Carlos Alberto Cortez** 06:31 Yeah, please. Could you mind sharing for me? My computer is acting weird today, so I can talk, but I cannot share.
Perfect. So the first one is an old issue regarding W3C Level 2 implementation. If you are wondering what this means, it means there's a new flag called random, which basically is telling, you know, users that part of the trace ID has been, you know, randomly generated.
And, basically, it's like an egg and chicken problem, because the literacy you know, has this level 2 as candidates, but they want people to implement that so it can go stable, and people don't implement that because it's not stable.
So, basically, Sergey and probably Denny Daila are up to date on this one, but they wanted to basically, go and see what's happening now.
So, the current status is that GMXD actually created a PR on randomness, which already mentions that in the spec.
But SIGs haven't implemented that yet.
And they… and of course, they don't want to implement this, because it's still in candidate mode.
So basically, like, I was wondering, like, whether this can be implemented, like, some SIQs can go ahead and implement that in a branch or something, so we can go… come back to the W3C and tell them, like, hey, this is implemented here, this is how it's looking, maybe get it out some… to users, if possible, as some… using some secret flag or whatever.
But basically, yeah, we are there in that camp, you know.
**Joshua MacDonald** 08:08 Can I speak? The W3C, so when I asked the same question maybe a year ago, like, how are we going to stabilize the W3C candidate recommendation level, too?
The answer is someone has to adopt it. We're the candidate user of that spec. I don't think anyone else out there will do that. So, I would suggest OpenTelemetry just goes.
We've decided, we've done a few years of research and diligence on it, spec's done. They're waiting for us. We should not wait for them.
Once we have it implemented, W3C will mark it done.
There's… there's no reason to delay.
**Daniel Dyla (Dynatrace)** 08:47 Yeah, that's more or less… My feeling on it as well.
**Ted Young** 08:52 Yeah, if they're ready for us, we should… we should go.
**Daniel Dyla (Dynatrace)** 08:56 The, the randomness flag…
**Josh Suereth** 09:00 Go ahead. No, I was just gonna say, what's holding up OpenTelemetry here? Is it that people… the R spec isn't stable, and that's why people are afraid to move, or is it that the W3C spec wasn't stable?
Because I think, what I heard from Carlos, and correct me if I'm wrong, Josh, you added a bunch of stuff around randomness in the OTEL spec, but I didn't think all of that stabilized until recently, so it might just be, like, kind of a time thing, but are the relevant pieces of our spec stable that people can depend on?
**Joshua MacDonald** 09:33 No, we haven't marked those specs stable, I think we're… waiting for the SDKs to move and implement these things.
**Carlos Alberto Cortez** 09:43 Basically.
**Joshua MacDonald** 09:47 Go ahead, Carlos.
**Carlos Alberto Cortez** 09:48 Yeah, basically, what I was checking on is that… so, basically, if you open, Oh, the Java link, for example?
The first point, not that one, the previous one.
That one, yeah, perfect. You can see that, Basically, this is a helper, because, you know, the flags are propagated anyway when you are propagating the context.
But this is what we need to have, you know, exposed in public in the 6. And this operation, like, having, for example, JavaScript or Python, they, instead of having a helper function, they have a constant that users can use to check this value, you know? And this is the thing that we don't have currently.
implemented, and this is in a span context. This is, like, well, TristFlex is in a span context, so it's part of the API, you know? So this could become stable even before what GMACD has been working on I think, but currently, funny thing is that In the spec, we do mention the flags, we do not mention that there's a helper method or a constant exposed to help the user do this. They have to, you know.
So this is also the other thing.
**Daniel Dyla (Dynatrace)** 10:56 So, what Josh implemented goes way beyond what the W3C has. The W3C flag essentially is just a hint that part of… at least part of your trace ID is random, randomly generated. That's, like, all it is.
**Joshua MacDonald** 11:15 unfortunately.
**Daniel Dyla (Dynatrace)** 11:17 Due to some decisions that were made a really long time ago, Level 1 implementations set that flag to zero… set all flags to zero that they don't understand. So any implementation that's not up to date.
clears this, which means in order for it to be useful at all, every single participant in the trace has to be updated to level 2, and that's, like, a base minimum for this flag to be useful in any possible way.
So, what Josh built… Is on top of both that, as well as… like a sideband mechanism for when that is not fully implemented, as far as if I'm understanding the current state.
So, the part that the W3C needs is just for, any trace ID that is Randomly generated, or generated with following the randomness requirements, to set that flag True.
And then, if you ever received the flag, propagate it unchanged. That's all we need, and that is extremely unlikely to change, and I would be shocked if any prototypes raise any problems that would cause that to… need to change.
**Josh Suereth** 12:42 But the W…
**Daniel Dyla (Dynatrace)** 12:43 E3C cannot move to the next step until there are some implementations. They don't need to be stable, they just have to exist.
**Josh Suereth** 12:50 Yeah, and if I'm reading correctly here, our trace propagation requirement has been updated to be W3C Trace Context Level 2, in a stable.
**Daniel Dyla (Dynatrace)** 13:00 Or yes.
Yeah, so the spec says… I'm sorry, I didn't mean to cut you off. The spec says to implement level 2. It doesn't really go into what that means, and I think a lot of the maintainers either are not aware of that change, or it's just not a requirement that has bubbled up to the top of the priority queue. Like, they're busy implementing the event API. Like, this, I think, falls so far down the list for a lot of maintainers, even though it is likely a near-negligible amount of work.
**Josh Suereth** 13:39 So, I think what we want, then, is.
**Daniel Dyla (Dynatrace)** 13:44 if the piece of the spec that talks about this is stable, which I believe it is.
**Josh Suereth** 13:49 that we need for this to start moving forward. I mean, there's this stuff that is defined that I think still needs to land, but can happen Independently. Do we, do we also, for, some of our other things, require that we set trace randomness?
in stable parts of the spec, I guess is the question. The reason I'm asking is, I feel like we should… use the new process we want for stable spec and stabilization, where we should open tickets against every SDK that says, hey, implement this feature, here's exactly what you need to do, on every single language. And I think that's the next step for this W3C W3C, randomness bit. And, like, we should just go open them all. You can mark it as closed if you've already implemented it, but we can use this to update our spec compliance matrix. But if the pieces that matter are already stable.
in our spec, then I think we're… we're fine. Like, let's just run that through.
If the pieces are not stable yet, then I think we need to, like, finish some of the randomness sampling to get it there, and let's… prioritize that work, right? Alright, there's a lot of hands, I don't know who was first.
**Joshua MacDonald** 15:09 I'm not exactly sure what the issue here is, but I will… I just want to kind of add some clarity. So.
If you are already generating the correct 56 bits of randomness, there's extremely little to do here, which is… Which is nice. I think what we're asking is, what do we need to do to get the W3C Level 2 part checked off? And that should be very little. I'm not aware of any languages that don't already set those 56 bits.
the low… least significant 56 bits have to be random. And as Daniel said, like, the actual sampled bit, the random sample… the random bit, like, doesn't use… it doesn't have much use right now. It's… it's mentioned for some warning texts and so on to help you understand when not… when the entire system is not upgraded.
So then after… after that baseline of the W3C2 stuff is done, Josh asks a good question about explicit randomness. Like, we already have in our spec the ID generator portion. If you have an ID generator interface, you should do something there, and it's not very hard.
As for whether we should, like, blanket every SDK with a ticket, I kind of feel like that's something we should automate or else not do. The, For my two prototypes, which were in Rust and Go, I have already filed tickets saying, I'm willing to help, I have this prototype, but I don't think I can do it alone. I can't make a… I can't make up a bunch of decisions for how to manage the SDK myself. So, for Russ and Go, I'm here. The Java side has Peter and Atmar available as well, so it's the other languages where we don't necessarily have a ticket or a person already available. I know Python and JavaScript are pretty good on this, so there's going to be a few more. But I think I'm looking for maintainers to kind of be ready for this work. Past the W3CT level.
2 stuff, it's modifying the trace ID ratio-based sampler, it's adding the composable samplers, And, you know, in my opinion, I don't think users are going to get much out of tracing except expensive bills, unless they have sampling really working. And I don't think OpenTelemetry ever really finished tracing, so I think it's pretty important, but that's just me.
Thank you.
**Ted Young** 17:18 Yeah, I think it's… it would be interesting to figure out a way to… to track this work. I kind of wonder about maybe re… rebooting the… spec compliance matrix, right? Like, that was the thing that was useful for a time in the early days, and since then, it's grown into, like, such a feature list, it's… I think a lot of people have questioned, is it useful in its current form?
But maybe rebooting that… because I don't think we want to be in a situation where we're telling every maintainer to implement every piece of the spec all the time, right? That's not feasible, and so maintainers have come back and basically said they tend to implement things when their community wants it.
But I think it's also reasonable for us to say there's some subset of features that, for stability or other reasons or conformance, we'd like to see everywhere.
And maybe some kind of compliance matrix where we figure out what those things are.
And then have a more concentrated effort about getting them done.
And I could totally see sampling being an example of something on the list.
**Daniel Dyla (Dynatrace)** 18:30 I just wanted to wrap back to something that Josh Surath mentioned, that the… as far as I'm aware, there is missing specification. Not just unstable, but missing, in that… There is no defined mechanism for when the ID generator… there's no defined mechanism for the ID generator to say, I generated this with sufficient randomness to meet the requirement, and therefore the flag should be set.
We can… I think… the spec saying implement level 2 is fine, it's all well and good for propagating if it already exists, but as far as I'm aware, there's no mechanism to set it.
**Joshua MacDonald** 19:17 In the Go prototype, I handled that by, an interface. Like, just mark your type, your ID generator with an interface saying, I generate randomness, and that was how I did it. So I assume a language-specific mechanism will work, but, yeah, it's not… it's not exactly spelled out, I think, because it's different by language.
**Daniel Dyla (Dynatrace)** 19:36 Yeah, I don't think the mechanism necessarily needs to be spelled out, exactly how it works, but as far as I know, there's nothing in the spec that even says it should exist in any form at all.
**Joshua MacDonald** 19:55 I remember writing something about it, I'll look for it.
**Josh Suereth** 20:00 Yeah, let's follow up on that. Carlos, you asked for 5 minutes here, we've gone a bit over, I think it was worth it.
**Carlos Alberto Cortez** 20:07 Sorry about, I will follow up, yeah, I will follow up with this one, definitely.
**Josh Suereth** 20:11 No, no, no, I want to hear what you have to say, because I think, I want to make sure we're resolving the reason you added it.
**Carlos Alberto Cortez** 20:17 Yeah, so I think… yeah, okay, so I guess that the… The summary is that I will… will go and manually fill, you know, open issues. Rebooting the matrix is great, but I don't think this should block us at this point. So I will go ahead and open, like, issues myself for now, manually.
Yeah, basically, we want to implement, as Daniel said, there's some missing stuff on the… even on the stable stuff, on the spec side.
So yeah, let's… I will review that. But I just want to say that, just to be clear, I think that a lot of stuff that is something C… something, sorry, has created. Probably… it doesn't have to be, like, stabilized right away.
But the part regarding the span context and trace flags, this has to, yeah.
So I will follow up on that myself.
**Josh Suereth** 21:08 Yeah, and when you open those issues, let's make them very crystal clear what the work is.
Right? So, so we can say, like, this, this is all you have to do.
**Carlos Alberto Cortez** 21:20 Yep.
Thank you.
**Josh Suereth** 21:25 Alright. You're next, Carlos.
**Carlos Alberto Cortez** 21:29 Yeah, actually, yeah, sorry, I have the next items, yeah, so I will try to stay, stick to the planning, to the plan time. The first one is just asking for maintainers. By the way, this is for… just for your information. As you know, the CI CDC has been, working and has relatively recently merged a pair of PRs regarding environment bar propagation.
And so please, if you're a SIG maintainer and you see something coming, please review that. That's important for us.
now that… We are, like, the actual stuff is in the spec.
We don't consider those things prototypes anymore, so they have to go, you know, stable. So please, help us with feedback, you know? Or if you are not available for, like, let's say for the next weeks, because we are busy working something else, let us know. But we want to make sure that maintainers are paying attention to this one.
Okay, the next one, likewise, just for your information, there's the PR that Robert created a few weeks ago. There was a discussion two weeks ago, it's log record processor enabled. We will merge that today.
This is an important part because we're making this, specific operation stable, so that means that, you know, it will go out there for real. So please take a look, but it looks great. All the discussions have been resolved.
Likewise, for always record sampler, this sampler is initially, set as development, so it should be fine, but please take a look. There's some minor stuff raised by CEO.
which I think should be sold today or in the next days, but otherwise it's good to go. If you think that this shouldn't, just let us know. As I said before, this is in development, so it should be fine.
Likewise for the Sipkin deprecation process.
this is something that is looking good. I was pinging Andura so he could ping SIPKIN, you know, community members.
it's looking good. I think they are okay with redeprecating this.
So I wonder if somebody feels like we should wait more or not.
Yeah, just… please comment on that offline, or there. Otherwise, I think we can wait a little bit more time, but I think we're good to go.
**Josh Suereth** 23:40 Well, to confirm with Zipkin, I made a comment early that had a bunch of thumbs up, but I want to make sure we agree on it, which is, we're gonna deprecate Zipkin in our spec, but we're not going to remove the… exporters from SDKs and things for a while, right?
We're just gonna basically say, like, hey, this is deprecated and you should move to OTLP.
So, like, we're not going to actually break people who are using the exporter today, we're just telling them it's deprecated.
Is that correct?
**Carlos Alberto Cortez** 24:11 Yeah, that's correct. And also, I think that hopefully this will motivate the Sitkin, because the Sipkin community, because they have OTLP support, which is unstable, hopefully this will help them to go stable, yeah.
**Reiley** 24:25 Cool. Gosh, I have a question about deprecate. So, what does that mean for the maintainers? Do they maintain that for the next year for security patches, or do they maintain it for the next 3 years?
**Josh Suereth** 24:35 Sdk is a gear.
Okay. So, if you look by policy, right, the SDK has 1 year maintenance, and API has 3 years.
**Reiley** 24:47 Yeah, so… Like… Can we communicate that down the deprecation process, just making sure it's very clear to the user?
**Josh Suereth** 24:56 Making it very clear that, like, if we deprecate Zipkin, it means that it only gets maintained for another year.
**Reiley** 25:01 Yeah.
**Josh Suereth** 25:02 Yeah.
**Reiley** 25:03 Given the exact date.
**Liudmila Molkova** 25:06 Riley, can you leave a comment so I will have a chance to address it?
**Reiley** 25:09 Yeah, I will. Thank you.
**Liudmila Molkova** 25:11 Thank you.
**Carlos Alberto Cortez** 25:12 Okay, so stupid question, do we need a blog posts for this or not? Is that important enough?
**Josh Suereth** 25:21 We should… we should probably do that, yeah.
**Reiley** 25:25 Well, I'm hot.
**Josh Suereth** 25:26 I mean, there's… so, I think there was a comment in the PR about how a lot of Zipkin downloads are because of an implicit dependency, and we're not sure if they're real downloads, but there's enough downloads that we should announce it.
And blog posts is how we hit our end users.
**Ted Young** 25:41 Yeah.
If we wanted to bundle a couple of spec changes into an announcement, it might be worthwhile, but we should definitely announce it.
**Josh Suereth** 25:51 You mean, like, a couple of deprecations, or other things?
**Ted Young** 25:55 I'm just saying, like, if… if the concern is we're making too many blog posts, then… Merge a couple of spec announcements together, but if we don't have that many announcements, just make one.
**Carlos Alberto Cortez** 26:08 Yeah, actually, maybe… I'm not sure about the next point that Robert just, or somebody removed.
on the Proto one, I was wondering whether this is something that we should announce. I don't know where it…
**Pellared** 26:20 because I thought it's… yeah, it's not worth wasting our time.
**Josh Suereth** 26:26 Okay, well, should we… should we move on, then, to that discussion?
Let me, let me just take notes, long post on this… Cool.
skate this one here. Alright, Yeah, let's move on to Robert's topic, then.
**Pellared** 27:02 Okay, I will try to summarize the issue in three… in maybe even one minute. So, this was an issue created by Bogdan.
And the thing is that we have been moving, like.
We have agreed that Logs API could be used by end users. However, one, some of our documentation, for sure, the main README of logs does not call it out, and also there are concerns regarding the user-friendliness of the Logs API itself.
And so, basically, this issue is around discussing how we would, want to go forward with it.
How we want to describe it, how we make… how we want to make, basically, make sure we do not mislead… make… mislead our users.
So, I see a few possibilities.
One which I personally propose is that the languages could be, could basically create their own, like, user-facing API, which we basically, like, kind of like a hotel login library wrapper of the logs API. So, but I just want… this is just a proposal. I'm also not sure if it's something that would have to be implemented by the language as part of the core open telemetry, or it should be something in the country.
Or someone should also create its own version, and even if it's something that we need or not. I think that, I think, basically, My guess is that Java may have also some opinions around it, because of the way how currently the logging.jka is, and preferably, I would… I think I would get the most input from, basically, Java maintainers, how it could be specified.
Yeah, so, that's it. If you have any opinions right now, I'm open to hear it out, but also having anything in the issue itself described would be wonderful, and I can slowly move this forward.
Tess, you wanna go first?
**Ted Young** 29:09 Yeah, I mean, I think this is a great example of where, to my mind, if we're just talking about convenience and usability.
it's a really simple API, right? If we're trying to make it better, to me, that means making it language-specific and leveraging idioms in that particular language.
I feel like a cross-language simplification is probably something that would just feel… Marginally better and, like, equally clunky.
everywhere.
And I would even extend this, potentially, to our other APIs, like, as part of, like, Snowtel and cleanup.
If we can stop pushing features, maybe there's an opportunity for people to start looking at convenience.
**Pellared** 30:00 Okay, deck?
**Jack Berg** 30:02 So… When we made this decision a while back to say that we want to have a log API that we expect end users to pick up and adopt.
And, you know, that's gonna be our recommendation. One of the points I was making back then is that, you know.
we have some work to do on the SDK side of things, because what the existing log frameworks provide is this really rich configuration ecosystem with a huge number of exporters.
And filters, and, you know, all sorts of throttling, that's all built in and configurable via a you know, some sort of declarative syntax, XML or otherwise. And, you know, in Java, I have a hard time actually telling… making the argument, and so I don't.
that, like, a user should use our log API for traditional logging, or structured logging, things that, like, aren't events. Because, while I do want to see log records going out over the network, over OTLP, you know, the debugging use case of seeing logs in the console is extremely valid and useful, right? And so, you know.
something in my head that I was thinking about back then is, like, you know, if we're gonna say… have this guidance, like, we're going to say that our log API is user-facing, then we need to provide tooling to Bring the logs back into those existing frameworks.
Right? So, like, maybe OpenTelemetry is the API you use, and, you know, that routes your logs over to the network via OTLP, but, you know, you still use Log4J for console logging, or log back for console logging, and you get to take advantage of its, you know, its configuration tools and all things like that, but we haven't built that yet. So, you know, we could have an ergonomic API, which is what this issue is about, but, like, I still wouldn't recommend people use it.
**Pellared** 32:01 So, just a few reasons why you may need it. Maybe it's language-specific, so the question is, if you have some instrumentation library.
would you… how would you, you know, emit the records from it? For instance, you have, you know, do you want it to depend on Log4j or other, you know, library? Is it fine for you?
Or you do… you're not… you're not… you do not know right now, Jack?
**Jack Berg** 32:31 I'm just trying to, like, manage multiple things. I was reading the chat as well, so sorry, I kind of missed something.
**Pellared** 32:36 I'm not reading. Oh, I must read the chat, so it's easier for me.
Yeah, but we can also discuss it later, I do not think we need to talk about it now, right, Jack?
**Jack Berg** 32:47 Yeah, we don't need to talk about it now. I just think, like, you know, this vision of the OpenTelemetry Logs API being a first-class, user-facing logs API still has some work to be done.
And, you know, it's like, there's two sides of it that are stopping us from people actually picking it up. There's the more ergonomic API, and I think, you know, I agree with the points that that needs to be language-specific, taking into account the language-specific idioms, but then there's also, like, the kind of tooling side of it, which is like, hey, how do you actually get those logs that you record via the API to have both a good OTLP network experience.
And, you know, good console logging experience.
**Pellared** 33:23 Dip.
Okay, thanks.
**Ted Young** 33:29 Just, I think this is an example of where we want to make sure perfect doesn't become the enemy of, like, good enough. Like, I think… I think it's possible for us to provide something ergonomic to end users and be upfront that, like, we don't have a rich, complicated ecosystem, and to also point people at, like, if you want to use traditional logging in language X, it's totally fine, here's how you do it.
I think we can point people at both directions, and it'll be okay.
So I have faith that we can thread the needle on this one.
**Jack Berg** 34:05 We're just, like, contradicting ourselves, though. We're saying, like, hey, pick up our log API and use it for events, and, because that's the way we think that the picture's going. And then, you know, the follow-up question is, okay, well, how do I, you know, emit these events, and also have my traditional logging experience, where I see these on the console, as well as in my network location?
And then we say, oh, go back and use, you know, Log4J instead, because we suck at doing that. And it's like, okay.
**Ted Young** 34:31 Or we're just… I think where I'm saying enemy of good enough is, like, I think users are often totally fine joining a new ecosystem under the understanding that everything is built in that ecosystem yet.
So… you know, sometimes I hear it put as a barrier. We haven't built everything that a user might want yet, so we should not go down that path.
And I think it's okay to go down that path and be like, we'll eventually have at least all of the normal conveniences, like console logging and stuff here.
But in the meantime, if you prefer something else, go right on ahead and use Log4J or something else, we fully support you.
**Liudmila Molkova** 35:11 Yeah, I don't think we're contradicting ourselves. We're doing it in phases. The first phase is that an instrumentation library, where you already depend on OpenTelemetry API for traces and metrics, it's natural for you to also emit events using hotel login API. Eventually, we will have tooling for the end users to also benefit from it, but nothing stops them from doing it and using console exporter, even though it might suck.
**Jack Berg** 35:42 Yeah.
**Ted Young** 35:45 Yeah.
Josh?
**Josh Suereth** 35:49 Sorry, I was trying to take notes, and I'm doing a bad job.
I… I want to call out that, like, we need to… we need to start asking what will make OpenTelemetry successful, and when we added a logs API at all, like, I… I do think that we knew that this was going to come, that people would want to… OTEL-specific logging API. And, like, if you think about it, if I'm taking a dependency on OpenTelemetry and I need to produce logs.
If we don't have an API of our own, we're forcing an instrumentation library to say, okay.
which one do I pick? And they have to pick, like, are they gonna use Log4J, are they gonna use SLF for J, are they gonna use something else? And so we're actually deferring that decision to them and kind of, bifurcating our own ecosystem.
So, there's a class of instrumentation that will be OTEL first, and those folks will probably want a dedicated OTEL API.
for that use case. That's different than someone who's, like, designing an application and owns everything, right? So this is, like, the library instrumentation author versus everyone. And so, I think if we're going to start expanding into this space, we should focus on that use case of, like, the library instrumentation author, giving them what they need.
of making sure they have enough of the logging API, they can provide instrumentation that does logs, metrics, and traces successfully, right?
And then, this, this concern you have, Jack, I think is still legit, and that's, like, the application owner.
who needs a solution. And there, we're still saying, okay, you're gonna have a bunch of stuff coming from OpenTelemetry, you can use the other logging thing, that's fine, and there's a bridge. I do think eventually that will get pressed on as well, where people will say, well, OTel, I want you to do all of it too, because you do a piece of it.
So, I think that that's coming, and I get this phased approach, but I just want to make sure we're targeted who we think the target user is, and why we're getting the pressure now. And I really think it's this instrumentation author.
of today.
There's… there's hands. I think Robert and Brian… I just… yeah, I just want to put…
**Pellared** 37:51 pushback before really testing. This, like, what you said, Josh, was the exact reason why you are going with this. And also, even in Go.
we are creating the, attributes using Weaver, like, generally the code, so this is, like, one reason to have it so that we can also, you know, use Weaver as, you know, strongly type thing when meeting, when creating instrumentation libraries.
And the second use case, which is, like, optional, that the end users may also take advantage of Weaver and create all even semantic conventions, and also have, you know, this kind of, you know, glue it together very nicely with our APIs and Weaver code generation, instead of, you know, having some conversion with, you know, attributes from the from the OpenTelemetry API… attribute APIs to, you know, for example, look4j attributes. So, yeah, but I… but as you told, like, the most important thing is to have this so that it can be used by instrumentation libraries, and yeah.
And I think that's it, and we can go to Raleigh.
**Reiley** 38:52 Yes, I just want to add one clarification to what Josh just mentioned. I think OpenTelemetry's mission is to have this clarity and support people Write high-quality logs.
whatever goal they have, like, as an application developer, library developer, framework developer, operating system, kernel developer, whatever, right? As long as they write code, they should have that clarity.
But OpenTelemetry doesn't necessarily have to invent its logging API across the board. For example, if there's a, like, a Rust ecosystem.
And the Rust philosophy is you have the login API at the very low layer of the… maybe the runtime or something, then I think open climate transformation can be work with that community to have that clarity for all the Rust developers, instead of inventing a separate thing.
So, I worry about if we go to the very extreme, saying OpenTelemetry will invent logging API across the languages, people might misinterpret that as, hey, instead of working with the language, runtime and compilers, those folks.
we'll just invent a competing solution. I'm trying to clarify, it's not. OpenTelemetry will define a standard and try to collaborate with, like, all the language runtime owners.
And if they agree, for example, if the Rust compiler's runtime folks would agree to meet with the OpenTelemetry spec, then it's perfect. OpenTelemetry should tell people, go and… there's a perfect Rust logging API, and they have the long-term commitment to align with OpenTelemetry. You should go and use that.
**Ted Young** 40:35 I just… Riley, I just have to point out that we go round and round on this. Like, this is a thing that keeps spinning logs and OTEL, is we keep saying, hey, go find the perfect solution that already exists in your language, and just recommend that. And then all the languages come back, and they say there really isn't one.
Even in languages where there's, like, an overwhelming choice, there's, like, reasons why you can't use it in X environment or Y environment. And then we come back to, like, the way the sequence works, we say, fine, well, we'll have our own API, but we won't recommend it to people, we'll just use it. But then it's super confusing.
**Reiley** 41:15 Yeah, we should clarify that per language. I'll give you an example. For .NET, the owner of the .NET runtime, they agreed, and they improved the iLogger API to perfectly meet with all.
**Ted Young** 41:25 Okay, but .NET is, like, the one counterexample that we… like.NET's completely weird.
**Reiley** 41:31 I agree, I agree with you. So the point here is we should clarify the vision, and for each language, we should have that clarity. My worry is we treat all the languages the same. Whatever extreme we pick, we're going to get confused.
**Ted Young** 41:46 Yeah. I don't think we should pick an extreme, and I don't think we gave guidance to pick an extreme. I think what we told maintainers all along is, like, we need to have our own API, because there's no third-party API we can drag with us everywhere as a dependency. But you should, first and foremost, make sure that OTEL works as a good log sync for any existing major logging toolchain that exists in that language. So I feel like we've already given everyone that feedback. It's… I'm a little conf… I don't even know if this is actually confusing to our end users. It feels like… it's more like logging API maintainers are more confused about this issue than end users.
For Caravan.
**Reiley** 42:32 Do folks feel it'll help if, for each language.
like in OpenTelemetry, the maintainers will give one single, like, recommendation.
I know it's hard, like, my question is, like, for example, like, Jack and a couple of folks as the Java SDK maintainer, do you feel you're in the position to tell all the Java users that when they come to OpenTelemetry, tell them, this is the login API that we recommend you to use, or you don't want to get into a muddy situation, you want people to get confused.
**Jack Berg** 43:06 Two issues.
**Liudmila Molkova** 43:06 20 cramps? Correct.
Oh, sorry. When it comes to convenience, we always leave it to the languages to do idiomatic thing, right? The baseline should be the same, the convenience should be language-specific, so… but it definitely would be worth to ask to provide one guidance, definitive preference from each language.
**Reiley** 43:28 Yeah, I'll just pick one concrete example, like, if I'm a Java developer, I come to OpenTelemetry and telling you, I'm willing to follow your guidance, just tell me which login should I use. Do I get the answer, or do I get a very, like.
like, unclear direction.
**Jack Berg** 43:44 Unclear direction is right now. The reasons is because the, you know, there's… it's a fractured ecosystem, so there's lots of log APIs we could recommend, and all of them, it's too easy to do the wrong thing. If you want to emit OpenTelemetry idiomatic logs with any of the options that are available, you have to jump through too many hoops, and it's really easy to shoot yourself in the foot.
And on the other side of things, the OpenTelemetry Log API, you know, like I said, the tooling for configuring what happens on the console with those logs is too bad to recommend in earnest. So we're in a no-win situation right now.
**Reiley** 44:20 I see, then… like, maybe the approach should be for languages that they should bring clarification. If no clarification, they have job to do. But for languages already having the clarification, people don't have the complaints. We don't want to scare people by saying, we're going to invent a different logging API.
**Ted Young** 44:43 I mean, you could even provide people both, it's a little weird, but you could be like, here's our logging API, here's our, like, OTEL log for J adapter, if… you really want to use Log4J, but you really want to make sure you're logging OTEL correctly.
**Reiley** 44:59 You can provide as many as you want, but the point here is when the user come to you and say, I just want to write log, tell me which one I should use. Give them super clear answer.
**Pellared** 45:09 I think it's not the easy thing, because it's also a migration story. A lot of people already use Log4J and other things like that, so I think for this kind of, you know, applications, we still need the L4J, you know, configurations, like symbols, etc, but I think lock term is the declarative config way.
for new applications, which will basically make the SDK, you know, the thing which basically makes… you basically use the creative configuration to set up your logging pipelines that you use it. And then… the APIs, whatever people prefer. For… probably for open telemetry events, they'll use the convenience logging APIs for other application logs.
So, it will be all them, maybe language-specific, like, I don't know, iLogger for .NET, etc.
Yep.
this month.
**Reiley** 45:58 Yeah, I understand that.
**Pellared** 45:59 One thing is the one thing, then it's a phase, the migration.
**Reiley** 46:02 Yeah, the part is fine. I understand it's a complex situation, but the point here is, if the user come to you for each language, you should have a very clear guidance for them to understand what's the direction, and what's the current situation, and how, like, so exactly, they know, when they write a line of code, what they should use.
And if the language already have that clarity, then they're fine. If not, then the maintainers have job to do.
**Josh Suereth** 46:40 I think this is where it gets into confusing things. So, I hear what you're saying, Riley. I think, I think it's a bit too much for us to ask maintainers to choose a logging library of choice in their language.
And to know how that will evolve.
like, I think choosing logging libraries to integrate with And maybe having, like, hey, we integrate with this one well, this one well, this one well, that's fine.
But from an open telemetry standpoint, think of what you're asking the maintainers to do.
Right, we have a specification on the login API, we ask them to implement it, we ask them to integrate into their language ecosystem. I think asking them to pick a winner in some other observability space is a bit much.
To… I understand.
Yeah, so, so, like, I also think we're starting to talk in circles. So what I'd like to do with this, I think there's good feedback that we have on the purpose of the logging API. I think we need to get to a point where, if you look at the original confusion here.
was about whether we have an API that you can interact with independently in OpenTelemetry, or if it has to be a bridge. And so the thing that's listed is unclear.
Is what we're going to recommend to people.
And I think what we're saying and what I heard is basically that is unclear.
Today.
And it's unclear whether users can do that, and it literally is confusing people.
**Reiley** 48:08 And I couldn't need to… So, I want to clarify, it could be clear or unclear, depending on which language we're talking about. For some languages, it's super clear. For some, it's super confusing, and then the other languages in the middle.
**Josh Suereth** 48:25 So let's talk about OpenTelemetry as a whole. It is unclear.
**Reiley** 48:31 Yeah, and my worry is we're trying to make the very unclear languages a bit clearer by making the languages who already have very clear answer now murky. That's my worry.
**Josh Suereth** 48:43 I just want to address this robe and telemetry, and I understand what you're saying. I think let's… Let's sort out what we can do here, right? Because we need to allow each language to have a clear story.
**Reiley** 48:56 Yeah.
**Josh Suereth** 48:57 Yeah, okay. So, in terms of next steps, Robert, I want to get to that, because we only have 10 minutes.
You're looking for feedback on this and the confusing purpose. We talk through, basically, a set of things that we believe.
And I… and as always with logs, we don't get consensus. I think there's a lot of, like, nuances and trade-offs here.
What I would like to do… if possible, for moving forward, is do we think that someone should be able to interact with only open telemetry APIs to write instrumentation, including logs? If the answer to that is yes, let's clarify that on the document and call that out as the primary rationale and motivation.
And let's drive that forward.
Right? And there's a lot of other complications and things to figure out, but, like, that is a clear next step that we need to go, and let's focus on that for now. Does that sound reasonable to everybody? Okay. Ted, you still have your hand up. Did you want to…
**Ted Young** 50:01 Yeah, I just wanted to suggest this… this ties back to just organizing Snowtel in general, right? Like, every SDK, every SIG is different in terms of the amount of, like, people available and where the SIG currently is, but one question I have is, would it be helpful to go through this stabilization effort as a group, by just POCUS… taking some amount of time and just focusing on one aspect of the SDK, like logging, or tracing, or something, sampling, and be like, let's clean up logging, collectively.
And if we do that together, whatever it means in our language, is that helpful? Because then it allows us to communicate with each other while doing that cleanup effort.
**Josh Suereth** 50:45 I think that that would be helpful, Ted. I also want to call out, I was going through the specification and looking at unstable bits.
The stability parts of the specification are unstable.
Right.
Yeah. So, like, there's, there's… If we…
**Ted Young** 51:04 I think it makes sense for us to walk through these in pieces, and maybe it makes sense.
**Josh Suereth** 51:09 One thing I've been trying to do, and I haven't, Haven't had enough time to get it down, is just having, like, a dedicated section of, like, specification stability, like, where things stand, where things are unstable.
to kind of focus that effort. Maybe we could take the specs, piece it out across maintainers, each person can take their spec and say, here's some major themes of stability that we'd like to drive through, areas where it's unstable or unclear, and then also collect from maintainers where their users are struggling with something.
I think that would make a lot of sense.
**Ted Young** 51:40 as a feedback, when we go look at each part of the spec, we're gonna discover there's stuff we forgot to write down, or…
**Josh Suereth** 51:47 Yep.
Okay, so in terms of this 3-minute discussion, I think we have… we have at least a next step, so let's… let's make progress in that vein, and let's move on, because I think we have two more things to discuss in the next 7 minutes, theoretically. So, Robert, stabilized metric instrument enabled. Anything needed towards that? You said a spec compliance matrix.
**Pellared** 52:14 I just looked at it before the Sikh meeting, and I thought that it maybe would just, you know, stabilize this, maybe.
**Josh Suereth** 52:23 Okay.
So we have two prototypes. I think normally we'd like to have three. Does this one have the third prototype?
No? Okay.
**Pellared** 52:42 Okay, so I will follow up on it, at least nobody says no right now, which is also important feedback for me.
**Josh Suereth** 52:49 Yep. Yeah, and I think that… I don't see a lot of contention to this, just besides, I want to make sure that SDKs can implement it.
If there's an SDK that can't make a stable release that has this, that might be a problem blocking it from Being pushed through.
Okay.
Cool. Josh? Donald.
**Pellared** 53:10 I think it's also… I think it's also listed the specifications of optional feature.
But maybe I am wrong.
I will double check this.
**Josh Suereth** 53:19 Okay.
Yeah, take a look. If it's optional, then I'm not concerned.
Josh McDonald, you want to talk about two open spec BRs?
**Joshua MacDonald** 53:29 Briefly, yes. I was just reviewing them, and I don't want us to forget about these. So, the first one, was from the collector, SIG. I read it, and I have feedback as a sort of a native English speaker, which might be useful to us or not. I think that the proposal here does address some clarity, but it's not very natural in my language.
sort of brain. So I'm recommending something at the bottom of this PR. I just wanted you to see it, especially Josh.
This is about how do we, refer to those fields in the entity. I think one of the points is that the ID keys field is, like, sort of too brief. Maybe it should be identity keys.
But definition keys, like, there's a difference between the spec language and the protocol that's confusing people right now. So I just wanted to throw that out, make sure people see it.
The second issue is, kind of a perpetual one in OTEL. I'm interested in trying to help with it, but it's a pretty large effort to talk about this. It's been discussed many times over the years, and it's, it's about how, you know, users come to… have come to expect a way to delete… delete time series from memory to help clear out, sort of, like, long-running time series that are… that become stale, and we've never given the SDK a specification for how to do that. It causes users to show up with this sort of, like.
knee-jerk of sort of, like, saying, I just want to be able to remove. That's what Prometheus calls it. Let's just call it remove. And, you know, this has been discussed many times. I hope there's… I hope there's sort of a will to address it now, and I wanted to sort of, like.
Just… just share that, feeling, and… and hope that if people who are interested in this come together, we could work it out.
**Josh Suereth** 55:13 So there's some…
**Joshua MacDonald** 55:15 Thoughts on the… in the issue there.
**Josh Suereth** 55:16 Have you seen the latest entity prototype here, Josh? If not, we should follow up. So the idea is, from a meter provider, you can get an extended meter provider that says, I want to record things for this entity.
And then I can kill that thing later. So I can actually allocate a new bit of metric space to record metrics against a thing.
And then I can kill it at some point, where there's a life cycle and a lifetime. I… I agree that we need the ability to have some kind of… add-remove on metrics. And I think, like, David's point is my concern here, because I think there's… there's multiple dimensions to that, of a specific metric and a time series, and they're kind of slightly different.
**Joshua MacDonald** 55:58 Yeah, my comment is that I'd like us to have a formal way to sort of, like, flush memory that's just simply stale, and then restart reporting it again, which means defining something about start time, which we absolutely haven't said. So there's, like, literally no solution in OTEL until we do that. Yeah.
**Josh Suereth** 56:13 So basically, you remember the start time with it, and then if you have to report it again, you just change where the start time is. I'm a huge fan of that.
**Joshua MacDonald** 56:21 I think there's a…
**Josh Suereth** 56:21 Prime.
**Joshua MacDonald** 56:22 couple more things we want to do, like make sure that not a number or, like, the missing point flag gets set somewhere. Anyway, I wrote it in the issue. This is interesting to me, I'd like to follow up. I'd like us to follow up.
**Josh Suereth** 56:33 I'm with you.
**Jack Berg** 56:35 I'm with you if you want to help solve this, I can help be part of that group.
I don't think we need to make this harder than it is. I think these are tractable problems, and we just, like, have talked ourselves in circles for years.
**Joshua MacDonald** 56:48 Yeah, I mean, to me, the most important thing is, like, there's a correct answer. Like, I shut down my meter reporting, I need to get final numbers, I would like them to be correct, and I think that that's what's missing when you say remove, like.
**Josh Suereth** 56:59 Who's gonna make sure we flush it? Like, if you remove it, that's the question I have.
Yeah, okay. Let's, let's continue that discussion. I am… yeah, I do agree that we've overthought that, and we need to, We need to be pragmatic here and get something working. Alright, cool.
We only have 3 minutes left, so I think we're gonna call it there. Thank you, everybody, and when we look at some of the follow-ups here, I hope, if anybody needs help, reach out in O-Tel Maintainer's chat. Remember the call for stability and Snowtel.
And the discussions that'll be happening there.
And look forward to seeing y'all next week.
**Reiley** 57:43 Thanks, Laura.
**Carlos Alberto Cortez** 57:44 See you soon.
