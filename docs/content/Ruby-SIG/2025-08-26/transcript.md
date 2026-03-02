SIG: Ruby SIG
Date: 2025-08-26
Duration: 58 minutes
============================================================

## Zoom Recording Transcript

**Eric Mustin** 00:25 Origin.
Where are you again?
**Arjun Rajappa** 00:28 Hey, hey, Eric. I'm doing good, how about you?
**Eric Mustin** 00:31 Good, good. There's been… there's a big, …
a lot of on-site stuff this week, all the teams here, so I'm, fighting for phone booth, you know.
Smith.
You're at a… I don't know if we've met before, I've seen you in some of the meetings, are you, …
Did you work with Kayla and, ….
**Arjun Rajappa** 00:54 No, I was joining in, maybe until May, June, so after June, I haven't joined in, so….
**Eric Mustin** 01:03 Okay, cool. Where are you, where are you based?
**Arjun Rajappa** 01:06 Bangalore. Oh, cool. India.
**Eric Mustin** 01:08 Oh, cool, nice.
What did I saw? I saw… oh, Datadog opened a big office in Bangalore, actually, recently. I was surprised.
That's good. It's a good, great hub.
So it's late, it's IST, what time is it in IST right now? It's like….
**Arjun Rajappa** 01:25 at 10.30 p.m.
**Eric Mustin** 01:28 There they are.
Brave. Brave man.
**Kayla Reopelle** 01:32 Wow, thank you for coming.
**Eric Mustin** 01:36 Yeah, I can't. I'm on my second, fridge cigarette of the day, so I don't think I'll make it to 10.30pm.
That's also… Maybe not an appropriate way to refer to Kiffy.
**Kayla Reopelle** 01:50 The new one to me. I hadn't heard that.
**Eric Mustin** 01:52 Yeah, I, like, I cribbed it off some Instagram somewhere, I heard. You'll see on that.
**Kayla Reopelle** 01:58 Nice.
**Eric Mustin** 02:02 But it's very true.
**Kayla Reopelle** 02:06 Indeed.
**Eric Mustin** 02:12 So I broke… I broke everyone's stuff last week, but I just… Randomly approving Schwan's… Sean's, API changes.
**Kayla Reopelle** 02:22 I mean, I approved it too. Like, we talked about it, we thought it was okay, and Francis corrected us.
**Eric Mustin** 02:29 Yeah.
I don't know.
**Kayla Reopelle** 02:30 Which is fine.
….
**Eric Mustin** 02:33 That was my job for a long time, was getting corrected by Francis.
That's cool. Yeah, I feel bad. I hope I didn't, you know, I don't know what stuff they're doing internally. I feel guilty if I, …
Broke production for them, but hopefully they were just….
**Kayla Reopelle** 02:48 I don't imagine it would have broken anything, because you were adding…
an API rather than removing it, but sure, I don't really know how their tests run.
**Eric Mustin** 02:57 Yeah, yeah, hopefully it just… Anyway.
**Kayla Reopelle** 03:00 Yeah, that was a question I wanted to cover, though. It's on the agenda. I don't know if we just want to…
Jump in, or what?
I can….
**Eric Mustin** 03:10 Wait another minute, huh? All good.
Okay, and what a minute it was.
**Kayla Reopelle** 03:25 Alright.
**Eric Mustin** 03:26 to….
**Kayla Reopelle** 03:27 I'm gonna….
**Eric Mustin** 03:27 I don't have it up, yeah, sorry.
**Kayla Reopelle** 03:29 Yeah, that's fine. … Let's see, this looks like the right dock… Okay… let's see…
Cool. Okay, so in the spec seg today, not a lot of terribly exciting stuff.
… the…
spec compliance matrix PR for Ruby is kind of on hold right now. I'm gonna try out this new YAML-ified version that we looked at last week, and update it to kind of…
see if, from, like, a maintainer updating point of view, if this new workflow is, nicer. So, hopefully those updates will be live on the website soon.
…
it doesn't sound like they need any maintainers to approve it. They'll kind of do their own checking on our API to make sure stuff's accurate. So, not much to do there. There's a new proto version that I think is about to be released arounding that,
Attribute… mixed attribute values discussion that was had in the spring and early summer.
I don't think… the rest of these, like, felt very relevant to our SIG.
… This one was kind of a conversation I didn't… entirely…
follow… oh, this was also about config. Okay, so there were just conversations, kind of, about how to authenticate the config using the new declarative file-based config format.
where configuration options should live, like, should they become part of the semantic conventions repo? Should they stay in their own repo? And it seemed like the conclusion…
was to… meet at…
this next, I think, semantic conventions meeting sake, they're gonna have the config people meet there also and discuss these things to try to figure out next steps.
So, yeah, nothing we really need to apply right now or worry about, since we're not doing anything with the config.
So yeah, new spec SIG record, 2 minutes.
**Eric Mustin** 06:08 Yay!
**Kayla Reopelle** 06:12 So, yeah, I guess we can just dive into the agenda. I'll put this link in the chat. If anyone else has things they want to add to the agenda, please do so.
This first one is a question about what we were talking about earlier.
So, we are reverting the PR that adds the SPAN APIs for attributes and events. Schwan, I see that you've been working on a new PR for, fixing the Lambda instrumentation in a different way.
I…
generally think with semantic invention, if you are removing an API, a public API, you need to mark it as a breaking change, so I think that's why I did that in the PR. But I was still kind of shocked this morning, which I probably shouldn't have been, to see that the API was at 2.0 because of this change. And I guess I'm just curious… everyone else's
point of view, like, we've had it out for one release. It wasn't a very long release.
We're reverting it as a bug fix, but it is still removing a public API. So, what are your thoughts on what version it should be? And also, does it even really matter for OTEL? Like, in New Relic land, we are hyper-conscious about versions because of different contracts that exist with customers, and so I don't know if that's
As important here, either.
**Wendy Smoak** 07:35 I mean, it looks like…
Semantic versioning here, so if it's not actually semantic versioning, that's gonna be super confusing.
**Kayla Reopelle** 07:45 is… yeah, right.
remove an API, and it's not.
**Wendy Smoak** 07:48 Yeah.
I mean, we… like, internally, we do just date. We do 25.08 and just 12345, because, like, it's just
it just needs a thing on it, but we don't try to pretend that it's semantic versioning. If you do.
**Eric Mustin** 08:01 Yeah.
**Wendy Smoak** 08:02 what this looks like, and then you don't follow it. I mean, there are plenty of projects who don't.
**Kayla Reopelle** 08:07 Yeah, probably.
**Wendy Smoak** 08:07 Yeah. Is there a statement anywhere that asserts that….
**Eric Mustin** 08:11 Oh, you do? Oh, yeah.
**Kayla Reopelle** 08:13 I think there is, somewhere, but I don't know where.
**Eric Mustin** 08:17 Yeah.
**Wendy Smoak** 08:17 Oh my god.
**Eric Mustin** 08:18 It's, you know, Semver V2, or whatever the… whatever.
**Wendy Smoak** 08:24 So did… did 2.0.0, like, go out, get published in Ruby Gems?
**Kayla Reopelle** 08:29 No, this is the release that, like, when we merge it, it would start it, so….
**Eric Mustin** 08:33 M.
Okay, so, yeah, just… I feel like there's actually something in this spec. Now that the whole point, the whole backstory here being, like, we didn't read the spec, like…
Perhaps I… we should carefully with respect. I would love to not.
Do a major version bump, but, like, yeah, at the end of the day, like, we can't.
can't cheat. The only cheat in Senber is never doing a 1.0, and we already did that.
**Wendy Smoak** 08:57 Oh, yeah, I've never….
**Eric Mustin** 08:58 ….
**Wendy Smoak** 08:59 And what I tell people all the…
integers are free, we can make more, it's fine, like, you know? Yeah. Have a 2, and then have a 3 if you need a 3, it doesn't matter, like, it's not… it gets all tied up in the marketing of what is 1.0.
**Eric Mustin** 09:15 Yeah, that works.
**Wendy Smoak** 09:16 I think everything should just start at 1 and do semantic versioning forever, and, like, that would be great, but we get these zero dot a million…
No, yeah. Yeah, if you're removing something, then yeah, it is a major version, because otherwise… You'll just break.
**Kayla Reopelle** 09:33 Yep.
Okay.
**Eric Mustin** 09:35 Yeah, well, yeah, I would… it would be good to maybe… Kit, like Ariel, or…
Robert or Francis, just, like, confirm. I don't know if there's precedence for being, like, this wasn't unintentional.
break… I guess this is intentional, we're intentionally breaking it, but…
I don't… yeah, I guess we have to. ….
**Kayla Reopelle** 09:54 Yeah, I think since they…
I'll check in with them on Slack, just to make sure we're all aware that this is a major version bump.
And that is what… Senverb would.
want us to do, so… …
Yeah, I don't… I don't mind being the… the scapegoat for this.
**Wendy Smoak** 10:17 Yeah, so OpenTelemetry clients must follow SEMBER2 2.0.0 with the following clarifications.
**Kayla Reopelle** 10:24 Cool.
**Wendy Smoak** 10:24 Are we client?
Yep.
**Eric Mustin** 10:27 Okay.
**Kayla Reopelle** 10:29 … Thanks.
Thanks for sharing that.
Perfect. Okay.
Well, that's that. So maybe it'll be more just, like, I'll let them know to not be…
Too alarmed?
**Eric Mustin** 10:44 Just, yeah, … I mean, it's myrrh, yeah, okay, …
I'm just reading, I'm… I don't want to live read this, or whatever. I feel like I… this is literally what happened in the last thing, is I was like, it seems like the right thing to do, and I was wrong, so…
…
Yeah, but I think we're all on the same page, but maybe let's try to get some social buy-in?
**Kayla Reopelle** 11:10 programs.
**Eric Mustin** 11:11 So, you know, we can ping… The other maintainers, or whatever.
**Kayla Reopelle** 11:15 Okay.
**Eric Mustin** 11:15 ….
**Kayla Reopelle** 11:16 Sounds good, so I'll fold the release until we can get, …
This one's gloomy.
Then, what's next?
Oh yeah, so this was an issue that was opened recently in the core repo. So inject is a method on multiple propagators, but also the TexMac propagator.
And as far as I can tell in the spec, there isn't anything that… defines, like.
What it actually needs to return.
… It looks like Arielle has chimed in since… I brought this up.
But, …
I guess I'm curious, folks here, if anyone is using the text map propagator and Inject, if you've run into problems with this, or just in general.
what your thoughts are. At this time, Inject just returns nil.
…
And… I don't know, maybe it's something we need to bring to the spec as well, or look at what other implementations are doing, because…
At this time… There's clear return values defined in the spec for extract, but nothing mentioned in… for inject.
**Eric Mustin** 12:52 I, … Don't know. … … you know, Besides…
some… what I… maybe some folks who are doing, like, messaging-specific things may have some opinions here. I don't, …
I wonder if it's possible to do this, always? I don't know, ….
Like, I don't know if it's always possible to return something useful. I don't know the, … I don't really remember the implementations of how…
like Kafka, or whatever some of these things are using to inject, ….
**Wendy Smoak** 13:31 You don't love nil and true.
**Eric Mustin** 13:34 Yeah.
It's all I return.
**Wendy Smoak** 13:36 It's either a Boolean or it's not, this tri-state Boolean thing. Yeah, yeah.
**Kayla Reopelle** 13:45 Alright, well, maybe this is a post on the channel as well, to see if we can get more people to discuss.
**Eric Mustin** 14:04 Yeah, I don't have… Wrong, opinions, except, yeah, trying to not…
Do breaking changes unless really needed, so….
**Kayla Reopelle** 14:19 Okay, sounds good.
Yeah, I'll post this in the channel and see if I can get there.
Excellent.
**Eric Mustin** 14:37 Like, I'm just thinking of, sorry to ramble, like, I know I'm, like.
like, SNS or SQS, for example, I think, like, you can inject headers
But there's some limits. Like, it's… if there's more than, like, 5 headers present, or 10 headers, maybe this is no longer the case. It used to just not allow, you know, they'd say it's, like, it would…
It would fail.
**Kayla Reopelle** 14:58 Oh, me.
**Eric Mustin** 14:59 But I don't know if that information… like, I don't know when that injection… I don't know if that's occurring…
you know.
And if that context could be passed back to, like, the return value of inject or not, but, like….
**Kayla Reopelle** 15:12 It's.
**Eric Mustin** 15:12 Some situations in which case it would… it would fail, due to constraints of, like, the underlying…
Software that you're trying to inject into?
**Kayla Reopelle** 15:25 Yeah.
That's a good point.
That might be worth adding as a funnel, too, to the issue, if you have the space to do that.
**Eric Mustin** 15:37 Yeah, let me… you know, per usual, every… all my, like, contacts here is, like, a few years out of date, and I don't remember where it is, so let me find it.
Maybe the messaging sig will have this.
**Kayla Reopelle** 16:11 Here's another PRN that was opened. It is a fix for API tracer start span.
Which makes it spec compliant. It had, …
Oh, sorry, I just saw this.
Yes, that's the API we're talking about. Well, that's, like, the topmost one, and then specifically what he linked to…
would be this one. So I think the spec follows, and… In both our nose.
Yeah, so I guess Shopify has had a fix, this fix running for a few years, and…
the initial implementation either misunderstood the spec, or the spec has changed for whatever reason.
Things needed to shift, and… This, … you know, it has tests, it updates existing tests.
What I can't tell right now is if this also should be…
Breaking, or if it can just be a fix. …
I can't tell if the return values are different enough.
But, but yeah, so calling this out for folks to review this week, just wanted to make sure people were aware that it was out there.
**Eric Mustin** 17:52 Yeah, I'm actually still trying to figure… what's the… … It's… previously, it returned…
It would just check if the context was valid, and now…
And if so, I would return the spam.
Now it's saying if it's not recording… Return… basically return the… Parent spam?
Context.
I'm a little confused. Yeah.
**Kayla Reopelle** 18:23 A non-recording span that has the parent context.
**Eric Mustin** 18:26 Right.
Okay.
**Kayla Reopelle** 18:28 It's kind of like a no-ops fan.
**Eric Mustin** 18:31 Yeah, yeah, yeah, I, … Previously, it returned, just the…
So the only difference is it's returning explicitly a non-recording span, whereas
Other than that, previously, it was just returning.
current spam.
I think? I don't… I'm just reading this. Yeah.
Yeah, I know they patched… there was a patch for a long while.
Because, part of the sampling methodology they used required
Yeah, they were doing… there's a… it's in the Slack channel, I can find it. …
the collapsing traces, basically. It was a concept called verbosity sampling, which Robert may have touched on before, I don't… where you're only, basically.
you only… you don't sample… sample out, like, internal spans. Like, you don't include internal spans in the trace, …
So that way, you could still retain the trace at its, like, nodes and edges, but without… but you could reduce the size.
Which was required for certain… for…
whatever high-volume services, so they're… I… they definitely, like… I'm sure this patch…
is… it's been running in production, so I'm sure it's fine, in terms of, like.
Resilience. I don't… I'm still lost on… I'm actually still trying to figure out what's the difference.
So yeah, I guess I'll… I'll try to review it this week.
**Kayla Reopelle** 19:54 Okay.
**Eric Mustin** 19:55 That helps.
**Kayla Reopelle** 19:56 Thanks, yeah.
I feel like any… any changes to the API and SDK now might be….
**Eric Mustin** 20:05 Yeah, yeah.
**Kayla Reopelle** 20:05 Taking in a little extra….
**Eric Mustin** 20:07 Crazy PTSD.
**Kayla Reopelle** 20:09 You're careful.
… Okay, I think that one's…
Yeah, that was this issue. Alright, that's everything I had called out initially for CORE. Before we move on to Contrib, is there anything else
Related to CORE that people are aware of right now that they want to discuss?
Okay, I'm gonna move forward then, but we can come back to those discussions later.
Alright. Oh, yes, I have an update for everyone on the logger instrumentation. So, I tried…
creating a new, directory called Bridge, and moving everything over. There were some places where it got a little hairy, and…
Mostly related to…
the use of instrumentation base. So right now, the logger instrumentation depends on the instrumentation-based gem, which is a gem that exists to kind of provide shared helper methods to all of the instrumentation libraries. And the methods it's using are related to
Like, whether something should be installed, whether it's compatible, and, …
you know, that whole, like, instrumentation RB file.
And I was wondering if it made…
So, I was wondering if it made sense to still depend on that if we were going to be creating, like, a separate grouping called Bridge. Right now, none of the, like, propagators or, other, like, non-instrumentation libraries depend on instrumentation base.
So that was kind of problem number one, and then problem number two was about registries. Right now, we can get a lot for free by including a logger in the registry for instrumentation, and by breaking
So I've been creating, like, a separate registry for bridges, We are kind of complicating…
I guess where people could look if they want to see, like, what libraries are being altered. So people would then have to look into a bridge registry to see, okay, logger is, you know, prepending things there, instead of being able to look at just this full instrumentation registry and see…
all of the changes in one place. I think those were the two main…
gotchas I found with the transition. Oh, I guess one other one could be that
instrumentation base right now. It instantiates a tracer. We're not using that tracer in the RubyLogger instrumentation, but if we eventually want to have
you know, except some of these PRs that add metrics into the RubyLogger, or I'm sorry, metrics into the existing instrumentation libraries, we will probably need some mechanism to control which
which, like, tracers, meters, etc, get, initialized when instrumentation starts up. So, so yeah, so those are… those are my thoughts, right now. I'm curious about
you know, structurally what other people think. If we, you know, don't mind those things and feel very strongly about logger being separate.
… do we…
want to include logger in instrumentation, but keep it out of instrumentation all for at least until the log's implementation is stabilized, like…
… Yeah, what do you think?
**Eric Mustin** 23:59 I mean Under the hood, these bridges are…
You know, either middleware injections or monkey patches on, you know, Modules, or….
**Kayla Reopelle** 24:11 Yeah.
**Eric Mustin** 24:11 So… I, you know, holistically, it seems like
There ought to be some interoper, you know, you'd want to be able to reuse a lot of the…
Especially at a registry thing, from a registry perspective, like.
you know, you wanna know… I'm just thinking of it as, like, oh, maybe you want to control what's turned off and on by an end bar, like….
**Kayla Reopelle** 24:35 You'd want, you know, I think most….
**Eric Mustin** 24:38 people would just want one NVAR where they could list out the different names. … But… I… don't have…
strong opinions. But yeah, like… It feels like, …
I… and I guess we get… it seems like we get a lot
I guess I'm… so, what is, … okay, so because we move it into bridge, we don't have… we don't inherit from the base instrumentation, you're saying? So you'd have to explicitly depend on it?
So….
**Kayla Reopelle** 25:10 Well, all the….
**Eric Mustin** 25:11 I guess they all depend, yeah.
**Kayla Reopelle** 25:12 Depending on it, yeah. So, we just kind of break logically.
**Eric Mustin** 25:17 Dear, yeah.
**Kayla Reopelle** 25:17 Rude, like, the way things are named.
**Eric Mustin** 25:19 Yeah, it's weird. It is weird. I mean….
**Kayla Reopelle** 25:22 Yeah.
**Eric Mustin** 25:22 But they are. Bridges kind of, like, are. They're just, like, instrumentation that doesn't… that just, like, messes. Does… that does other stuff once you have monkey patched. …
I don't know.
Okay, how's usual?
**Kayla Reopelle** 25:36 Okay.
**Eric Mustin** 25:40 And it also feels like all the methods we want, like, you know, all the hooks.
That base instrumentation provide, we probably would want for the bridges, like, we want to be able to install, uninstall.
**Kayla Reopelle** 25:51 Check.
**Eric Mustin** 25:52 for compatibility, it's, like, all the same, so it's a lot of… but I don't want to necessarily… like, I don't know, I think you don't want to be, like, over-dry early for no reason to, like, it's okay if things are repeated twice, like…
At 3 times, you start to be like, alright, let's try it out. Like, I… so… yeah, I don't have…
I don't mind the little bit of, like, cross… you know?
**Kayla Reopelle** 26:17 Like, required.
**Eric Mustin** 26:17 Crossing the streams of… yeah, but….
**Kayla Reopelle** 26:19 Yeah.
**Eric Mustin** 26:20 Finally.
But I, I would… it does seem like we probably don't want to just have instrumentation all…
just turn on the… that feels like a separate toggle. Yeah. I don't know.
**Kayla Reopelle** 26:30 Yeah. And I don't think it does in this PR.
**Eric Mustin** 26:34 Right.
**Kayla Reopelle** 26:35 But I think that might have been one of the… concerns, …
Schwan raised the concern, so maybe I'll message him after this, just to make sure he's okay with…
Whatever approaches. Yeah.
**Eric Mustin** 26:49 what, … I guess, are there in other languages that abridges, like, may not have the same approach of, like, having a bass instrumentation gem, or equivalent, so it doesn't really…
That's true. Or I don't know if they do, I don't….
**Kayla Reopelle** 27:02 I haven't looked at that, and it is pretty…
split as to whether languages separate bridges into their own directories, or just include logs bridges with whatever their other instrumentation is.
**Eric Mustin** 27:18 Yeah.
**Kayla Reopelle** 27:19 like, I think Node and Java…
for sure, keep it with all of the other instrumentation. Right. Finding Go is an example where it's separate from the instrumentation, just in where the code's stored.
**Eric Mustin** 27:36 …
Yeah, I mean, I'm tempted to just reuse stuff, and then if it turns out to be messy, or if it turns out to introduce some… some issue in the future, then you could…
Do you know, have a unique, instrumentation thingy for… a bass bridger?
**Kayla Reopelle** 27:56 Yeah.
**Eric Mustin** 27:56 I don't know, base feed recruiters, so… … I don't know.
**Kayla Reopelle** 28:01 Yeah, I guess… We could create a separate… a separate gym that does…
The stuff and instrumentation-based that's shared, but then we still run into the registry problem.
**Eric Mustin** 28:13 Quickly getting into, like, left pad territory, if you'll say.
Yeah, or, like, you know, is even. …
Yeah, I don't know. I, …
I don't know, as you can tell, I don't… I would defer… I would def… obviously, since you've been driving the huge majority of all… a lot of this work, like…
defer to your opinion here, but I don't think it's the end of the world to include bass instrumentation.
**Kayla Reopelle** 28:38 Yeah.
Okay, I'll… post this as well in the Slack channel, and see if I can….
**Eric Mustin** 28:46 I'm so bad at giving.
**Kayla Reopelle** 28:47 No, no, no!
**Eric Mustin** 28:47 I'm, like, the worst.
**Kayla Reopelle** 28:49 You just want.
**Eric Mustin** 28:49 Yeah, cool.
**Kayla Reopelle** 28:50 Oh, sounds like a good question.
enough, …
enough people who have mentioned that they have opinions and haven't been active in a while, but I don't want to…
merge, I guess, without, getting their feedback, so… I'll, …
We'll see… see if anyone responds. I think where I'm at right now is post these things, give people a week to check in, and if they don't, …
Go from there.
And just make a decision.
**Eric Mustin** 29:36 Yeah, I like that, I think.
The pragmatic approach.
**Kayla Reopelle** 29:42 Yeah, so we have another PR from the community that is…
just related to some Ethon exception handling that came up. Hannah, they successfully added it to dupe old and stable, so… looks like the system is working, but, …
I wanted to call this out in case anyone else wanted to review it.
if… no one else expresses an interest, I'll probably merge it on Thursday.
Did you have a concern?
**Eric Mustin** 30:24 No, I don't know.
Try to… Spend some time, take a look.
**Kayla Reopelle** 30:31 It's pretty… it's… it's pretty straight.
Pull it, that was true.
in there, so… …
Yeah.
Let's see, okay, this one, this one's a little more of a discussion. So this PR…
is trying to kind of solve the problem with, Puma not…
always shutting down providers, so having, I believe, some, like, dropped spans, potentially.
Where this gets hairy is that right now, it…
is using… it's calling the shutdown method for the different providers, and the shutdown method is in the SDK only, and we do not generally
depend on the SDK for instrumentation. We should only depend on the API. And so…
That kind of creates a problem here, …
Even though it is, I think, a very helpful plugin, …
we would effectively be, like, calling a method that we're not actually going to depend on, so that we could leave the SDK implementation open, but I think, …
this user makes, Sander makes a good point about, like, we also have to account for the OTEL SDK disabled, so…
I'm not really sure what to do here. This might be a case where we need to bring it to the specsig and see what other people have done.
But yeah, I wanted to hear what… what others' thoughts were.
on this, and potentially calling an SDK method in an instrumentation library.
**Eric Mustin** 32:28 … I have some hesitations about owning.
Things like, … Boom up.
plugin? …
Just from a maintenance perspective, but I don't… off the top of my head, I would say it would be nice to ask, what's his name?
Nate… Speed guy, Nate Burkbeck?
**Kayla Reopelle** 32:52 Yeah. ….
**Eric Mustin** 32:53 I think he's pretty active, and he's …
he might be open to giving his feedback. Like, I'd be curious what Puma thinks about this, and whether this is something they want to support better within Puma itself, or…
With the implementation itself, whether it's the right… because I don't… yeah, I don't know… I don't have a ton of experience, ….
**Wendy Smoak** 33:14 It doesn't contrib, so how… how… what is the expectation? I've seen… is it… I think it's the collector, where I've kind of seen labels on things saying, this is unmaintained, it'll be removed after….
**Eric Mustin** 33:26 Yeah.
**Wendy Smoak** 33:27 Sometime if no one….
**Eric Mustin** 33:29 I think it's… we have a sort of, like, benevolent dictator, like, Ariel gets to just, like…
to banish people, kind of… no, it's a huge open question, because it's like…
you know, at a certain point, like, the main… who's the maintenance burden fall on? And we'd be… we're less hesitant… we're more hesitant to accept things if we know we'll have to own it, like, day two. Like, I don't know, if you look at some of our AWS SDK instrumentation, like.
some random Israeli startup came in and, like, just did a drive-by contrib on that, and then was like, yeah, we'll own it, and, like, they're not a company anymore, those guys don't work there, like…
So, I don't know, I think we've been… there's a little bit of once bitten, twice shy with some of this stuff, but we don't have as… Collector has some really strong rules around it, and, like, some schedules, and, like, there's a timeline. I don't think we've gone… we've written out some documents….
**Wendy Smoak** 34:17 There should be some rules about, like, if you're….
**Eric Mustin** 34:19 Yeah.
**Wendy Smoak** 34:20 Is there… is there a… so if it couldn't… if I wanted to use this.
And it can't go in Contrib. Like, is there a way to…
You make your own gem and just stick it in there, and it just works?
**Eric Mustin** 34:32 Oh, you'd have to publish your own gem, and then there's, like, you could publish it in, like, the hotel registry?
Which is, like… the… Just weird little, like.
forgotten section of the hotel website, where it links… it's just a table, and you just make a PR and say, like, this is out there. But it's also… again, it's kind of like, I don't know, the same way with, like, Rack can Trib. It's just sort of like a Wild West.
Of, like, stuff a little bit, ….
**Wendy Smoak** 34:59 I actually need this for a passenger, so I'm interested in it, but to just, like, see what it's doing, because we'll probably have to copy and paste it, and just do it internally.
**Kayla Reopelle** 35:09 Yeah. Yeah.
I think….
**Wendy Smoak** 35:11 So, the thing about calling SDK methods, so why isn't… shutdown seems like a pretty natural thing to need. Why isn't it in the API? Should it be in the API? Do we just need to go.
**Kayla Reopelle** 35:23 I… I don't know, yeah. So maybe, maybe that's the next step, is asking the…
the spec repo, like, hey, why isn't this part of the API, and linking this PR to the question? …
Because, yeah, even as a no-up, I mean, if you're… if you're starting things up, you should likely be able to shut them down.
**Wendy Smoak** 35:46 You're gonna add, you should be able to remove, that's in that, that's in that other thread.
**Kayla Reopelle** 35:49 Yep.
So, …
Yeah, I think that's… that's maybe a good next question. Oh, and back to the conversation about guidelines for
contributing, new instrumentation, there is the… the contributing MD file for this project has been expanded, and there is this expectation that if you are creating a new gem, you need to be around to maintain it, and we would add you to the code owner's file, and that's kind of
as part of that, was part of my movement to try to make sure all the code owners were actually members of OpenTelemetry and could get PRs accepted, but…
that just kind of fizzled because I got distracted, so maybe that needs to become a priority again to make sure that the contributing process is actually working, and it's not on the maintainers to…
Tag all of the contributors whenever something related to their project comes up.
**Wendy Smoak** 36:49 I mean, people are gonna… leave, right? There has to be a way to retire, like, if….
**Kayla Reopelle** 36:54 Yeah.
**Wendy Smoak** 36:55 You don't want to, like… there's got to be a way to say, this is unmaintained, use it at your own risk.
**Eric Mustin** 37:01 Wendy, I've been trying to retire from this….
**Kayla Reopelle** 37:04 I've been….
**Eric Mustin** 37:05 I'm trying to retire from maintaining this for years.
**Kayla Reopelle** 37:09 I keep….
**Eric Mustin** 37:10 Offering, you know, and it's taking me up on it, so….
**Kayla Reopelle** 37:12 So, yeah, I mean….
**Wendy Smoak** 37:14 It's either not accept… because, I mean, that's just open source. People are gonna…
There has to be a way for people to move in and out, and…
Disappear for long periods of time, and then come back.
So…
But having it… having the expectation be clear, like, if you're gonna use this, just keep in mind that the person who wrote it is no longer around, and so you need to.
**Kayla Reopelle** 37:39 Do you think that'.
**Wendy Smoak** 37:39 You're probably gonna have to do it yourself.
**Kayla Reopelle** 37:41 Yep, like, update the… like, a banner on the README or something like that. We did also….
**Wendy Smoak** 37:48 last commit as a proxy for that.
**Kayla Reopelle** 37:51 look.
**Wendy Smoak** 37:52 I mean, some things are done and baked, and the fact that it hasn't been touched in 2 years is not a problem, and some things aren't. It's hard to tell.
**Kayla Reopelle** 38:00 Yeah, yeah.
And I'm sure in a… A repo like this one, where there's so many issues.
And so many different libraries inside of it, it might be kind of challenging to connect, like, how many open issues exist for this particular
Implementation.
**Wendy Smoak** 38:18 I don't have an answer, but that's….
**Kayla Reopelle** 38:20 Yeah, okay. Yeah, well, I think the spec is the best next stop. Oh, and just one other bit of context, too, was we… we had that kind of community approach where someone from the community created an instrumentation
and used the OpenTelemetry name pattern in it, and that kind of created some issues, because then we couldn't release an instrumentation with that name, and so I think that's something else to keep in mind when
And if we encourage people to, like.
release their own gems is, like, is it something that we really would never want to release as OpenTelemetry authors? And, there are actual, like, Puma
metrics and things that we may need to include for semantic conventions compatibility, if we want to be, like, fully,
Yeah, fully compliant, so that's another… but… but this is also in kind of that strange situation where it's not actually emitting any telemetry right now. It is just providing this shutdown helper. So is it really an instrumentation?
I don't know.
….
**Eric Mustin** 39:34 Deep thoughts.
**Kayla Reopelle** 39:36 Yes, lots of, lots of fun questions.
….
**Eric Mustin** 39:42 I'm not, I'm not tech, I don't need it.
**Wendy Smoak** 39:43 If it's outside this repo, it shouldn't be doing… I mean, it shouldn't be using the… how does…
In Java, we had the backwards… you'd use your URL backwards as the namespace.
**Kayla Reopelle** 39:54 Oh, God.
**Wendy Smoak** 39:55 whatever, like, I'm not really… how does one do that in Ruby? Something outside shouldn't be taking over the namespace, or whatever.
**Eric Mustin** 40:04 Yeah, yeah, I think… Ruby Gemsis.
**Kayla Reopelle** 40:07 programs, and… Didn't hear back about, like, how to protect the namespace, so….
**Eric Mustin** 40:13 They have some scanning, I… … The… yeah.
No, never mind, it's not important. … Just keep going.
**Kayla Reopelle** 40:27 I'll check back in with him on that.
Okay.
Cool, there's that lining… What do we got now?
It's the same room… Oh, I put these…
Okay, this one is one that's been open for ages, and I…
Oh, speaking of AWS SDK,
While you were gone, we did have actual people from AWS.
**Eric Mustin** 41:05 Oh, nice.
**Kayla Reopelle** 41:06 And take over the gems and revamp them, so…
Hooray! We have AWS maintainers for the AWS stuff.
I guess I just wanted to bring this…
Because it had been languishing, and I'm trying to clean up some of the old things, so…
I know there's been a lot of requests on time, but just as another opportunity if someone is interested to take a look at this.
I think… there's….
**Eric Mustin** 41:39 Yeah.
**Kayla Reopelle** 41:39 Yeah, some concerns about deprecation. I know configs are always something
You want to be careful with, …
Communicating when you're making changes, too.
**Eric Mustin** 41:51 No.
**Kayla Reopelle** 41:52 But I don't think there's any semantic convention preventing this from happening.
**Eric Mustin** 42:00 Yeah, I mean…
I don't think we should just rip out a config, you know, I think there's a better pattern, but at a high level, I'm not, … is this the AWS folks contributing it?
Yeah, I mean, I generally think… We need to…
allow library maintainers, you know, or folks who are maintainers to have some opinion on what, like, how to… you know, the same way Scikick, we have a bunch of config options for saying, like, hey, don't….
**Kayla Reopelle** 42:29 collect the polling span, or whatever. Yeah.
**Eric Mustin** 42:33 So, it seems reasonable, and certainly…
a noisy… sounds like it could be noisy, so practically speaking, I'm inclined to want to support anything that lets you, yeah, whatever, emit less… less useless bites over the wire, but like…
I, … I guess I'll look at it. I'll put it on my list of the other three things I won't get to this week. …
Yeah, it seems reasonable to support a, … Yeah.
**Kayla Reopelle** 43:03 Yeah.
Okay.
Sounds good. I can… I can add a comment to check in with them to see if they can….
**Eric Mustin** 43:11 Sure.
**Kayla Reopelle** 43:12 Fix the config stuff, and then….
**Eric Mustin** 43:15 Yeah, I mean, Ariel's comment, I think, still stands, which is, like, please don't just….
**Kayla Reopelle** 43:19 Yeah. Yeah, it's been since May, so maybe we'll just ping her and see.
What he thinks about his comment.
Cool. Okay.
Those are all the things I wanted to chat about, … there was…
One other… oh, there is… there is actually one other thing with CORE. …
And… yeah. So, once… once upon a time, one of our maintainers named Rob, created this PR to help migrate Ruby's semantic inventions library to,
the new tool that the Semantic Conventions Repository uses called Weaver to help auto-generate code.
And this… this works. We can use it to update to new versions of the semantic convention without a problem.
In the past, I think the gem release has been… the version number there is kind of tied to the semantic conventions version that it represents. And so we will have, like, a bunch of gaps, I think, when we release, of gems that don't match the particular version.
But there was a discussion in Slack that was kind of, like, questioning whether we should have a semantic conventions gem at all, if instead people should just be using string constants. I think this has come up
Multiple times, but, …
you know, since I was able to test this PR and get it to work, I don't have any qualms about merging it, but I think more…
It seems like people more philosophically have some concerns about
releasing a gem with the semantic conventions in it, and I was… I was curious about, like, yeah, what the folks in the SIG
Think in terms of whether we should
you know, release a gem that has all of the constants, all of the documentation. In this new version, you don't have to require, and it does not require all of the constants automatically. The instrumentation author, whoever's using them, needs to require the specific file that has the constants.
So that that way there isn't, like, this huge burden of strings that you're not going to use in whatever package.
is using it.
… You know, it does…
I guess then add, maybe on the maintainers, making sure that we release new versions of the gem when the new semantic invention comes out. …
But, yeah, I think… I guess I'm just curious. People seem to…
be conflicted about this and also have a lot of opinions. So, would anyone in this room, I guess, find this gem useful? Does this gem feel like a foot gun?
….
**Wendy Smoak** 46:22 I think I'm using it… is it?
the… like, I have S… I have it mapped…
to SCR, and then I'm using the, you know, like.
**Kayla Reopelle** 46:33 Oh, are you using this branch specifically?
**Wendy Smoak** 46:36 No, no, not that. But the Semantic Convention, like, being in a gem.
**Kayla Reopelle** 46:40 Yeah.
**Wendy Smoak** 46:41 What's coming with the thing is…
And I didn't think anything of it. I think it was probably in one of your examples, and I just copied and pasted it, so….
**Kayla Reopelle** 46:48 Okay.
**Wendy Smoak** 46:49 Using the, you know, using the constants that come.
**Kayla Reopelle** 46:52 Yeah.
**Wendy Smoak** 46:53 from the project to avoid misspelling one of the dotted… those really long dotted names. Because then you can't get it… then you can't get it wrong.
**Kayla Reopelle** 47:01 Yeah.
**Wendy Smoak** 47:02 Because we're, you know, we're trying to stick to using the
The conventional name, so that when other things start emitting telemetry, that it's the same attribute name.
**Kayla Reopelle** 47:12 And someone hasn't….
**Wendy Smoak** 47:14 Misspelled it or made up something slightly different, so…
I don't know… I don't quite understand what this… this is just generating that in a different way?
**Kayla Reopelle** 47:21 is just generating that in a different way. So, like, the old conventions we have are very limited, and it….
**Wendy Smoak** 47:28 Why isn't this one in there?
**Kayla Reopelle** 47:30 Yes, exactly, yeah. And so now, the structure would be a little different. There would be this incubating namespace that would hold all of the constants that aren't yet stable, and every constant forever would be added to that namespace so that you wouldn't…
ever lose a constant that you were pointing to. But things would only get moved into stable, which is just the same constant name, without incubating, once it had been marked as stable in the semantic conventions.
And we have tests to make sure that nothing gets dropped, so….
**Eric Mustin** 48:12 I think it's useful for manual instrumentation, or, like, custom instrumentation, when you still want to abide by
The cement, you know, you still want to ensure that you're
whatever, custom span thingy around your custom thingy, other thingy is, like.
can be, like Wendy was saying, like, can be a first-class citizen and, you know, caught by the same queries and OTTL things that your other… whatever your Java stuff is shipping. And, like, yeah, I think…
Having a gem that gives you a constant, so you don't have to think about under the hood.
what that constant represents, like, is right, otherwise you're just carrying a lot of strings and random…
You know, packages, and then you don't, you know, upgrading is…
just a little bit of a DIY adventure, whereas this feels like.
you'd… I guess, as stuff goes from incubating to stable, you'd still have to modify the constant.
But it might be… that's probably something… I guess I'm curious about that, is like…
What happens… let's say something goes from incubating to stable, is it duped in both incubating and stable, then?
**Kayla Reopelle** 49:20 Yep, do it that way.
**Eric Mustin** 49:21 Yeah, I mean, that's… Like, you wanna…
have that be an intentional choice when you move to something stable you'd want to modify. It seems fine. It seems like a good thing to add. I'm confused on what the philosophical dislike is, besides, like.
**Wendy Smoak** 49:38 If it's a question of, like, not having this at all, just, like, not having the semantic conventions constants in the project at all, or…?
**Kayla Reopelle** 49:45 Yeah, yeah, and instead asking every instrumentation author to look up the semantic conventions, create their own constants inside of the instrumentation for them, and write those strings and point to those strings.
**Eric Mustin** 49:58 It's like, you gotta freeze the strings every time, like, it….
**Wendy Smoak** 50:01 Yeah.
**Eric Mustin** 50:02 A lot of work to….
**Wendy Smoak** 50:04 And then everyone who's doing… I mean, I suppose, like, logging… I'm using them, I think, for the resource attributes.
**Kayla Reopelle** 50:11 Yeah.
**Wendy Smoak** 50:11 Yeah, we do, I think so.
I actually… I don't know, I didn't think… They're there, I used them.
**Kayla Reopelle** 50:17 Yeah.
**Wendy Smoak** 50:18 If they weren't there, then I would be on the website, and I would be making my own constants, and pasting in the thing, and potentially making mistakes.
**Hannah Ramadan** 50:25 Like, this won't work if you….
**Wendy Smoak** 50:28 misspell the name of the constant, you're gonna get an error when you try to run your tests or whatever.
**Eric Mustin** 50:31 Right.
**Kayla Reopelle** 50:32 Yeah.
**Wendy Smoak** 50:32 Like, you misspell it in the…
Right. Because you're trying to use code, not… if you misspell the string that you're making up your own constant, then you're, like, you may notice at some point.
Oh, and how you generate them? I don't care.
**Kayla Reopelle** 50:46 Yeah, yeah. Yeah, they… the generation process has been made easy, I think, from Rob's work, because it's been 11 versions since he first created this, and the generation continued to work just fine.
So, ….
**Eric Mustin** 51:05 The real things that I'm gonna be maintaining as SEMCOM versions come out, ensuring that we bump the gem in a timely manner, is…
Yeah, maybe easier said than done. Or maybe, like, if you would….
**Wendy Smoak** 51:17 Won't it settle down at some point? I mean, we're not going to be adding new constants forever.
**Kayla Reopelle** 51:21 I miss those words, yeah.
**Eric Mustin** 51:23 Sorry, the marketing guides will review, you know, LLM observability plus V2, final, needs to come out, or whatever.
**Wendy Smoak** 51:30 Oh, yeah.
I don't… I mean, I don't have… whoever's having to run this and generate it should decide what…
Which way they want… because you could just as soon have…
do it manually, right? Yeah. Look at the website, and go type in a new constant, and then release your job.
The generation's kind of like, if you want to maintain the generation, then do it that way, otherwise….
**Kayla Reopelle** 51:56 What do you think, Hannah?
**Hannah Ramadan** 51:58 Yeah, I was gonna say, because I was just messing with a bunch of semantic conventions, this would have been helpful, or, like, I would have loved to point to Constance. And did you get any feedback from the folks who were… no? Okay.
**Kayla Reopelle** 52:11 Who doesn't that?
Damn.
So, cool. Okay, I think that's helpful to hear with the people in this room.
**Eric Mustin** 52:20 Chappette. Chaput.
**Kayla Reopelle** 52:22 Use that merge power! Yeah.
**Eric Mustin** 52:26 Viola.
**Kayla Reopelle** 52:27 Yeah, I think I'll open up a PR with… there were a few small changes that I made to the generator to make things work, mostly just running RuboCop to make sure everything was spaced properly. …
So maybe that's the next step, and… Asking…
Rob, if he's comfortable merging that into this PR, and then…
kind of closing it up, or taking it over from him, because, yeah, I've… I think it's a shame that this work is all ready, and it's just kind of being….
**Eric Mustin** 52:59 bang him.
**Kayla Reopelle** 52:59 There, yeah.
**Eric Mustin** 53:00 Yeah, agreed. I appreciate you, you know, digging up these stale things and trying to push them across the finish line.
**Kayla Reopelle** 53:08 My… yeah, happy, happy to do it. Glad that I have time right now. At some point, I will disappear and not have time.
**Eric Mustin** 53:15 Labor Day, day after Labor Day, it's… yeah, I'll see you guys on the other side. That's the vibe I'm getting.
Cool. Or sorry, Arjun, September 2nd or 3rd.
**Kayla Reopelle** 53:28 Yes.
Nice, alright, send, PR…
We'll just have that as the summary for that discussion.
Cool. Okay, that's… thanks for, you know, discussing all my questions and topics that I brought up today. Is there anything else that people want to discuss before we close?
**Wendy Smoak** 54:06 Do you have time to look at the metrics feedback? I had another question on the end.
**Kayla Reopelle** 54:11 Exactly.
**Wendy Smoak** 54:11 We can do it in the channel.
**Kayla Reopelle** 54:13 I think that, … That's something I was thinking about yesterday.
But….
**Wendy Smoak** 54:19 I'm just trying to get…
It's not urgent, I can do it in a…
Background job that runs nightly and just spit out the metrics, but…
The way it's all written, it says you should be able… to… it's metrics feedback.
**Kayla Reopelle** 54:38 Sorry, I'm just not seeing it on there. There we go.
**Wendy Smoak** 54:41 … The way everything's written, it, like, says you have control over the… the asynchronous… Instruments?
But…
that config patch is adding… is always adding that one that picks up the default that I have no control over, so…
then my thing happens every minute, whether I want it to or not.
**Kayla Reopelle** 55:06 Yeah, I think this is a bug. I think this is something that we need to fix with the asynchronous instruments.
And… because the… the spec…
it seems like it shouldn't work that way. You should be able to change the default and get it to run, so…
….
**Wendy Smoak** 55:25 Well, no, I mean, I don't want to change the default, I want to… like, I am adding… I didn't put the code here… I'm adding a periodic metric creator with a specific
timing.
**Kayla Reopelle** 55:35 Too.
**Wendy Smoak** 55:35 minutes.
But you're adding another one. So I've got two metrics readers in my meter.
Because that config patch is always adding….
**Kayla Reopelle** 55:45 I see, I see. Okay. So….
**Wendy Smoak** 55:48 So, what is the config patches? I mean, it's lovely, it's nice to have, because when you just first start using the thing, it just works. Like, you make a meter, you make some instruments, and just magically, you've got metrics, but….
**Kayla Reopelle** 55:59 So you can….
**Wendy Smoak** 55:59 No, I don't want that.
**Kayla Reopelle** 56:00 None, and then do all of your own.
**Wendy Smoak** 56:04 Whoa.
**Kayla Reopelle** 56:05 If you wanted to just bypass it.
That's… what I think we do in some of the examples where we try to set it up.
Okay. But I don't know, I'm curious….
**Wendy Smoak** 56:17 I thought I had to have OTLP for, like, anything to work, but that's really only controlling this.
**Kayla Reopelle** 56:22 Yeah, all this is doing is taking… it's creating a periodic metric creator and attaching it to the OTLP metrics exporter. So if you're creating this yourself.
….
**Wendy Smoak** 56:33 And I should be none.
**Kayla Reopelle** 56:33 then it should be fine. Yeah, you can write that same code, and then just set this to none, and….
**Wendy Smoak** 56:40 Okay.
**Kayla Reopelle** 56:41 Or that one, yeah.
**Wendy Smoak** 56:42 Alright, I'll answer myself on the….
**Kayla Reopelle** 56:44 So yeah, so I'd give that a try, but if it's still…
Yeah, I misunderstood your question. I thought you were getting extra intervals, and that the intervals you were setting weren't being respected.
**Wendy Smoak** 56:56 It's just… it's doing that one plus mine, but I didn't, like… I thought the having OTLP there was required to turn on
all the things, like, I didn't realize that this was really the only thing it was doing, like, making the config patchwork.
**Kayla Reopelle** 57:10 Yeah, that's all it's doing. It just creates those for you, yep.
**Wendy Smoak** 57:13 Got it.
**Kayla Reopelle** 57:15 Nice.
**Eric Mustin** 57:18 Yeah, I should have to cut… Kelsey of getting married?
They got engaged.
What? It's very important. Taylor Swift?
**Kayla Reopelle** 57:26 Oh.
**Eric Mustin** 57:27 We got engaged.
**Kayla Reopelle** 57:28 For you to drop.
**Eric Mustin** 57:28 Chelsea. Big news. Added to the….
**Wendy Smoak** 57:30 Taking news in the… expecting news in the movies, like.
**Kayla Reopelle** 57:32 Very important. Reports.
**Eric Mustin** 57:36 My afternoon's host. Yes, exactly, amazing.
**Wendy Smoak** 57:39 Exactly.
That's it.
**Kayla Reopelle** 57:44 It's a perfect note to add.
**Eric Mustin** 57:46 There we go.
**Wendy Smoak** 57:47 Great, thank you. Thanks, everyone. Have a good week.
**Eric Mustin** 57:50 Cheers. Bye.
**Kayla Reopelle** 57:51 Right.
