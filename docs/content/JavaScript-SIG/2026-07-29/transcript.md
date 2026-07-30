SIG: JavaScript SIG
Date: 2026-07-29
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Marc Pichler** 00:34 Hello?
Hello?
**Trent Mick** 01:27 Hello.
**Raphaël Thériault** 01:31 Hulu.
**Trent Mick** 01:35 Must be summer, it's getting pretty sparse in here.
**Marc Pichler** 01:44 Yeah, I think we had already… Not that many people in the car the last two weeks.
I guess we can get started.
So, the first topic on here is… my own, I did look into compatibility, again, with the… context attached proposal, and I found some… Stuff that was a bit worrying, I did try it out and, like, installed the package into… like, the API package into, clean.
TypeScript project, and I included the ES2022, types.
And then ended up with… a bunch of compile errors, and had to include this ESNext, disposable… thing?
To actually make it work.
And… One of the issues that our users will run into is that, Anybody, even if they don't want to… Use the disposable context thing.
We'll have to include these types.
for… their stuff to compile if they have skip lip check.
turned off.
So… Bunch of alternatives that I would like to propose, like, one is to… Proceed without disposable tokens, and then later on, require these to be implemented.
By the context managers themselves.
Or we move that functionality to the experimental entry point for now. So people would import context from OpenTelemetry API Experimental.
and get it this way. I was just wondering what, Your preferences would be, to move this forward?
**Trent Mick** 04:21 I'm confused with this, not… This isn't about the TypeScript version compatibility.
**Marc Pichler** 04:28 Yeah, it's about, I can actually show it here.
You've probably seen in the pull request that I opened, we have… changes to the tsconfig.
Which is here.
It requires this, eSNextDisposable thing. So even with TypeScript 5.2, you would… Have to configure ESNX disposable to actually use it.
Which we probably can't require, all our users to do.
or at least I think it would be quite painful for everybody to change the tsconfigs to make that happen. Especially also because in our README, We do state that… East 2022 is… What we're targeting.
This is for browser support, technically, but, Like, browser folks would also be… Affected by this.
Most likely, if we include it in the API.
**Trent Mick** 06:09 You know, is there a current TypeScript version? I'm not proposing that we upgrade, but is there a point at which we can have the nice thing.
**Marc Pichler** 06:21 There is… dis… explicit resource, management proposal that actually had a PR that was merged, and that's probably gonna be included in ES 2026, so it's quite far out.
Like, this was merged.
Not that long ago, so… About a month ago.
So it's not included in the current version of the spec that's actually published, but that's probably gonna be published this year.
So…
**Trent Mick** 07:09 I see.
**Marc Pichler** 07:11 Using… using that, we're probably… break a bunch of folks. I suspect, I have no idea if it would actually be that bad, but, Most folks should have skipped lip check.
Set to true. But in the past, we've had a bunch of people Run into that, with skip lip check force, and it seems to be common enough for people to run into these problems.
**Trent Mick** 07:56 Okay, so, of your… proposed alternatives.
I guess going back to the original use case that brought it in for… Using the… right, Tracy Channel.
based instrumentation.
What do you think is the… Serves them best.
**Marc Pichler** 08:22 I think without the disposable tokens.
Is probably the best way of going about it, because then we can actually mark it as a stable feature soon.
If we…
**Trent Mick** 08:36 Without disposable tokens, this is where you have explicit detach instances.
**Marc Pichler** 08:40 Yeah, you could… like, we can still make it so that there's a dispose, method on the token. There's… Almost no performance impact of doing that.
So it wouldn't be… That bad to just… Have a token and then car dispose on it.
And… skip having this, separate detach functionality on the context object that's returned from the API, so,
**Trent Mick** 09:17 I see what you mean. Okay, so it's kind of like the promise-like equivalent, dispose-like, but not using the types.
Okay.
**Marc Pichler** 09:26 Yeah, it's not using the types. We could probably also… have it work in a way that, it actually has symbol dispose defined.
And plain JavaScript users could use it.
But… Typescript users can't.
**Trent Mick** 09:52 Wang Long.
**Marc Pichler** 09:53 So… that's kind of a trade-off, there, but if we move it to the experimental entry point, it will probably be stuck there until we update to support, like, ES2026 and beyond.
Which will be a very long time, which then in turn also means that we probably can't stabilize any tracing channel instrumentation helper that we add.
Which…
**Trent Mick** 10:23 So, I'm still a little confused on the ES2026 versus… so, like, symbol.dispose and the using syntax are in node 24 as a base.
But… Is… is that… does that see us 2026, I guess?
**Marc Pichler** 10:44 I actually have no idea how… how that… Place together.
2p… Completely honest with you. I have no idea how… In Node, there can be a feature that's not in the language, Itself.
Yet.
**Trent Mick** 11:03 That's what I don't get, this, because 2024, because Node24's obviously been around for more than a month, and you said only merge the spec and… So what the hell spec are we talking about? So the… the JS in V8?
is ahead of what's in the ES spec.
Like, I understand that they'll have experimental features, but as…
**Raphaël Thériault** 11:23 They have a policy of, like, implementing Tier 4 proposals, even if they're not, like, merged completely.
**Trent Mick** 11:30 Those would usually be behind flags to turn them on, wouldn't they? Granted, Node could be turning on those flags by default, so I guess…
**Raphaël Thériault** 11:39 I don't think they're even flagged, really.
**Trent Mick** 11:42 Okay.
**Marc Pichler** 11:48 I will do some more digging until next. I'll be out of office next week, but… I'll do some digging, and write a summary on the PR.
Because what you raised right now is a really good question. I don't know exactly, yet how to answer it, but I'll…
**Trent Mick** 12:12 There's a way.
**Marc Pichler** 12:13 in the future.
**Trent Mick** 12:13 Right? 24 is… 24 is not our baseline. That's just for Node. And then there is browser, so if it's… If that feature is not… Widely available, then… And I don't know if I'm missing something, like, there's… there's… so our targets are a base version of Node that we pick, a… Widely available for… JavaScript features for browsers.
And then… What I'm not clear on is whether there's a third, like, TypeScript thing. Like, TypeScript knows… the base version of TypeScript that we have can handle this syntax as well. I don't know if that's a… or types. Anyway.
Pick.
But it sounds like your first alternative is the more likely one.
**Marc Pichler** 13:02 Yeah, one of the downsides that we have with this is, Once we add that feature later on, like, having the disposable token, for real.
That will mean that that will be a breaking change for implementers.
Because suddenly the token will have to implement dispose.
But we can probably… structure it in a way to work around that, so that the API checks if… Dispose is defined.
And it's optional.
Once we add it, and if it's not defined, it just defines it, too.
Call the already defined dispose function, method.
On the token.
Because it just needs to forward it, right? Like, so if the symbol is both… Yeah, yeah. …just cars.
**Trent Mick** 14:06 No, no, I was wondering if you could define it right now to require the shape of the type that's going to come later, so it isn't a Birkin change, but I don't know if I'm missing a detail.
**Marc Pichler** 14:17 Yeah, I think the problem is that then… I need to use SimberDispose.
In the type.
And then it's gonna be required there, so the context manager library will also need this.
ES next disposable.
thing to compile cleanly.
And then we're back to square one.
I've been kind of going in circles with this.
Today, looking into it again. So, it always ends up back in the same place where I can't use it.
Which is unfortunate.
**Trent Mick** 15:02 Okay, well then I'm back and forth, too. I'm thinking the experimental entry point then, but yeah, avoiding and breaking change later would be great, but…
**Marc Pichler** 15:09 Yeah.
**Trent Mick** 15:09 No, it's possible, yeah.
**Marc Pichler** 15:13 Alright.
I guess let's move on to the next one, then.
Unless anybody else has questions?
Alright, so, I've been looking into this PR here, didn't have a lot of time to get back to them. Essentially, what they're asking for here is to add, like, an ignore incoming propagation hook on the HTTP instrumentation, which would allow uses to… not… Inject, or not extract context from requests that are coming in based on rules that they define.
I did put a comment on here that, like, usually the way that I've seen this is people use, like, a reverse proxy or something to strip that, as the request is coming in.
So that they don't end up with, trace context and… Trace… or the trace parent and trace state, had us on it.
But they… Seemed to be more interested in actually having that on the instrumentation.
lever, so I'm wondering if… Any of you have, preference on this. I would prefer it to be… Handled in reverse proxies still, but… Trent or so.
**Trent Mick** 16:56 Do they still want… I… I hadn't read this issue, I don't know how old it is. Okay, 3 weeks.
So… this might be ignorant, what I'm saying, because I haven't read his whole description.
Are they wanting to maintain any of that trace state information, or… Like, I understand that they don't want to continue the trace, because… User could send, like… a bucket load of requests that all use the same trace ID.
**Marc Pichler** 17:34 Yeah, so… from my understanding, is they don't want to keep any part of it. So, when somebody from the outside sends a request, they want to like, essentially… Not take any of the context information from these requests, and just start their own.
Instead.
**Trent Mick** 17:57 Okay, so I'm looking at the paragraph just above short description of the changes. It starts with, there is currently no way to keep Up, up, up, a little bit.
Move your cursor down. There is currently no way to keep there. Okay. So, hotel propagators, none… yeah, so, one other thing I was saying is you can use propagators for this, so you can… But… what… Using hotel propagators none doesn't work, because then… You're no-opping the inject as well as the extract.
Yeah. But if you wrote your own propagator.
that copies a W3CE trace context propagator that no-ops the extract, but does the inject, and you can do that.
Granted, that's, like, having to write your own custom propagator is not super convenient for users, or obvious.
**Jamie Danielson** 18:49 Is that what he did in the other, alternative PR?
**Marc Pichler** 18:53 Yeah, so there's, he… did some… something similar there. They also seem to have an extra requirement, which is to only do it for certain requests, not to do it for all of them. Which is why I'm saying to use the reverse proxy instead, because, It just… completely gets rid of needing that in the HTTP instrumentation, and then you also don't need to… deal with gRPC and other stuff, which suffer from the same issue.
**Trent Mick** 19:33 Okay, so Elastic's free hotel agents had this similar kind of request.
And we had a feature across a few languages called, a config setting called Trace Continuation Strategy that you could configure on your public-facing things. The default behavior was to do the normal trace context propagation. There's a thing called… there was an option called restart, which would do… Basically, what they're asking for here is that it would restart a trace when it's coming in.
And a bonus little side feature is that a spanned link would be created on that top-level span for the incoming trace context data, so you could still see that incoming data if you wanted in the data, but it didn't actually influence… a new trace ID was still created.
Then it had another setting, which is pretty static, called Restart External, and basically it was… it would sniff known the trace state to say, oh, this is one coming from an upstream Elastic instrumentation, because we put a thing in the trace state. So, it would continue if it was a stream elastic service. So that's kind of… a half-assed answer to what he's asking for here, because it looks like he has a callback configured thing to decide, given the request, whether this is one that they want to continue the trace or not.
So… In hotel land, on the… if you go back to your first tab, the document I had linked to… spec discussion.
for adding something like this trace continuation strategy to OTEL.
And this has started a little while ago by a colleague, Ricardo. He is a maintainer in Hotel Python.
Redirecting… Redirecting… Superhighways clogged.
Anyway, Obviously, this is not a quick turnaround thing, this is talking at spec level. I think that spec has moved on from just being a, let's screw around in the propagators to proposing a new… SDK component for doing this thing, because the discussion got off on a number of use cases. And this was also talking about handling baggage, which I think the original poster of the issuei thing was talking about baggage, so… Anyway… Yeah.
I don't have a great answer, because responding with this is kind of like a… wait… wait 2 years, and there might be something for answers to do this thing, so it's kinda… I don't know. Like, I wonder if a custom… Yeah, the problem is the propagators don't get request information, so you can't do that handling of the thing, and I think that's where this discussion went to. It was talking about doing propagate… propagation so you could have your public-facing ones, but then what about something that's public-facing, but also internal things call it, and you want those traces to be continued, and… how do you do that kind of thing? And so, reverse proxy, I think, was discussed as well, which might be the… The best answer if they want to do… anything particularly smart. If they just don't want propagation, then a custom propagator. I think, interestingly, when we were looking at this, I think the Go… OTEL SDK has something like this, so they don't call it… external, I have to go find what the name was. So they do have, in some of their instrumentations, they have things like this where there's a… Callback or some static config for deciding what's an in… internal require… I don't know what the terminology was. So, like, it might be hard to say no if there's a bit of Bright there, but I don't know.
Obviously, if you hit the HTTP instrumentation for Node, that's 99% of the instrumentation cases where there's Roots fans being created, so… Yeah.
**Marc Pichler** 23:34 I… I think I will go look at, Go implementation and see if I can find something like this.
I probably check… also check… Java and… Python and see if there's anything similar there.
Just to get a sense of, like, If there's been discussion on… In the other sixes were to look into something like that or not.
And to figure out how they did it, if they did.
And then I'll also read the spec.
proposal here… Let's see if there's… If that fits what they're asking for, or not.
But those are good pointers. I actually did check if, we at Dynatrace have a feature like that, and wasn't able to find anything. So… Or also… Uno?
**Trent Mick** 24:47 Okay.
**Marc Pichler** 24:47 I'll also ask around internally to see if… that is a common feature request or not. Yep.
Alright, so I guess the… summaries. We're… leaning towards… not wanting this in the HTTP instrumentations, but unsure. If there's a good way.
to accomplish that.
Yes, we can, continue next time.
2… Discuss this there.
**Trent Mick** 25:37 Yeah, sorry, that's the way I'm leaning. I guess there's… there's a certain point in all these things where you want to be able to support all the features that are coming in, but I guess the other limitation is time, and we've got other focuses right now, too, so…
**Marc Pichler** 25:49 Yeah, I'm… I'm more so… I'm not sure if, aye.
showed what my preference would be, but my preference would also be to not have this feature, because I'm… Kind of.
I would like to have… Not that many.
Hooks.
Oh, actually… I wonder if… They could just… Strip the header from… the incoming request.
So that it doesn't.
**Trent Mick** 26:26 Not… not early enough, I don't think.
**Marc Pichler** 26:30 Yeah, because the span is already created at that point.
So…
**Trent Mick** 26:35 I mean, you have to do it before… The instrumentation starts doing any of it.
**Marc Pichler** 26:40 stuff.
**Trent Mick** 26:40 So I guess you wanna…
**Marc Pichler** 26:43 Yeah, it's… too late already, at this point, I think.
Alright.
**Trent Mick** 26:53 your own early run instrumentation, I guess. It doesn't.
**Marc Pichler** 27:03 Yeah, guess, need to look into it a bit more.
But thank you for the discussion there.
Was very insightful.
Let's move on to the next one, then.
It's also a topic that I put on here.
I'm just wondering if anybody would be interested in a SEMCOMF review skill?
I've been playing around with that recently.
because reviewing PRs in Contrip is always a bit difficult, because you have to go to SEMconf, and then go check all the stuff, and find out, like, how the different spans, or, like, span attributes are derived and whatnot, and there's lots of rules, usually, that you have to… look into.
And I've iterated on the skill far enough now that it actually spits out useful findings.
And I'm wondering if… Anybody would be opposed if I were to upstream that one.
**Trent Mick** 28:27 Marylia gave you a thumbs up.
**Jamie Danielson** 28:29 You say it seems like a good idea. I'd also wrote a note in there, but it's sort of unrelated, like, it's related, but it's different, is possibly, like, the Weber live check into CI.
But I haven't really actually done it. I've only seen it set up in a couple of spots.
But the skill is definitely a lighter weight, easier to add thing.
**Marc Pichler** 28:52 is a, Weaver Life Check.
I haven't used it before, so I'm completely… It's a complete unknown to me. Is that something where… We actually run an app with… the instrumentation and emit telemetry to Weaver, and it checks stuff for us.
**Jamie Danielson** 29:13 Right, like, it sees if it matches whatever schema you expect it to have.
I haven't used… like I said, I haven't used it, I just know of its general capabilities.
Like, I know, like, cause for the Gen AI instrumentation, that's been a big thing, for SimConv, and so I know they added it into, like, Python contrib, and so I was gonna try to look at that and figure out how to… Get that added on ours.
**Marc Pichler** 29:48 Yeah, I think, if we add that, it would be a great addition. The… the sameconf review skill is, I think… Helpful in, related, but seem, like.
Related but somewhat different way, because it also checks, like, how you derive the, attribute value.
And sometimes there's, like, 4 packs defined, where it says, like, if… You have that available, then try this, and if you don't have it, then add this.
So it's really… Easy to catch.
Like, these sorts of things with the skill.
Whereas, I guess, Weber LifeCheck would… Just say, hey, this looks okay, But I'm… not sure. I've ever tried it out as well.
But if there's no… objections to me upstreaming it, and I'll try to… Skill first, and…
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 30:58 Yeah, I think, like, I was gonna say, like, different use cases for different types, like, different moments of your, like, coding, so, like, yours is gonna help, especially, like, with reviews, or for the person creating, like, their own. They did it before they put the PR up, they can do their own check just to see if they missed something. Yeah, the Weber would help… Like, some part of it's also in the middle, and for the things that we already have, we can use the the Ecosystem Explorer that I know somebody is actually gonna start looking at the JavaScript, because I'm gonna help them out, so I think that would be, like, a cool one, because for the things that do exist, we can say, like, is anything there, like, we are really behind, or, like, not longer following than we should? So we can also keep a track on that.
So yeah, they're just different parts of the, like, development cycle, but yeah, the skill would be, like, a great one.
**Marc Pichler** 31:54 Ness?
Alright, then I will look into that, and… If it's not helpful, we can always remove it again, so… No harm done.
Alright.
**Trent Mick** 32:16 Actually, back up a little bit, I added a comment to the trace continuation thing.
if I'm reading this correctly, not a super Go guy, but Go has a thing called… when they… you can configure… a with public endpoint function.
our public endpoint function, that's a callback, basically, on whatever incoming HTT instrumentation is, deciding whether to use a spanned link or to continue the trace.
As a child, so I think… That's the equivalent to what's basically being asked for.
**Marc Pichler** 32:54 Yeah, this looks very similar.
I'm just looking into, like, where this was added, because it might be that… Whoever requested it is… Maybe…
**Trent Mick** 33:14 Was that Damien that did it?
**Marc Pichler** 33:15 Yeah.
**Trent Mick** 33:17 Oh, there was… that also might be a refactoring, because there was a different name for this config thing, and I think it was… Anyway, so you'd have to dig harder through the history, see if that was just refactoring or not.
Maybe not.
**Marc Pichler** 33:33 Yeah, looks like this is a new…
**Trent Mick** 33:35 Oh, no, there's public endpoint as a bool.
And then it's a public endpoint function, and I think they maybe will get rid of the other one, or have done so already.
**Marc Pichler** 33:46 Alright, so… yeah, but… Here, there doesn't seem to be an… an issue. I just wanted to follow, like, where it came from.
Just to see if… the person that requested this is somehow affiliated with the person that's requesting it now on JS as well.
But it seems that this is… unrelated.
Tool.
That feature request here.
**Trent Mick** 34:18 Yeah, if people are interested, reading that spec thing that I linked to would be… Interesting. I think, My experience staying customer.
related stuff for our free hotel thing at Elastic, there were a number of independent requests where this was the right answer.
on.
In multiple languages, so something at the spec level sounds reasonable.
**Marc Pichler** 34:39 Yeah, I agree.
Thanks for digging that up. This is interesting.
**Trent Mick** 34:50 Okay, so, yeah, maybe if you could open that. This might be mostly for you, Mark. Some questions. So, I was working through the… declarative config work for creating a meter provider and all of the various edge cases. The… Meter providers, obviously, a bigger surface area than The logger… log record provider.
Holy internet, man. What's going on?
End of the meeting, we'll take a collection, so Mark's internet provider can… Upgrade his account.
**Marc Pichler** 35:23 Hey, now it worked. Alright.
**Trent Mick** 35:26 Okay, two things. Declarative config for a console… Metric Exporter. Is that right? Is that what the title of this one is?
Yeah, the console metric exporter. You can pass in a temporality preference and a default histogram aggregation. Two separate issues going on. A question about the… Yeah, let's look at the second one first, the temporality preference section. Okay, so there, I think, is something weird going on in here. So, currently, Console Metric Exporter accepts a… just mostly reading through this in order there, accepts a temporality selector.
However, the OTLP metric exporters accept a different Hype, or specifying the Temporality preference?
And if you dig through, scroll down a little bit more… Okay, you can see there's… in the… the bottom code block and the third from the bottom code block. There are two enums.
in SDK metrics, there's an enum aggregation temporality, which has delta and cumulative, and then at the bottom, there's an enum aggregation temporality preference, which has delta cumulative, and an extra one, low memory. The code path for The temporality preference argument that a console metric exporter accepts.
Only gets you to the top enum.
But the one that the OTLP metric exporters accept gets you to either of those enums. There's actually a union align, rather. What's going on there? Do you know about.
**Marc Pichler** 37:24 That's incredible.
**Trent Mick** 37:24 those enums.
**Marc Pichler** 37:25 Yeah, so the aggregation temporality preference is… A collection of… Mappings from instrument type to aggregation temporality.
So, a delta aggregation temporality preference will select delta on all instrument types.
Except for the up-down counter, which would be cumulative.
**Trent Mick** 37:53 I got you, and low memory is gonna be special.
**Marc Pichler** 37:55 And low memory is also gonna be special in its own case, and then cumulative… is the only one that actually does cumulative for all of them, except for Gage, which does not have it.
Concept of aggregation temporality.
**Trent Mick** 38:09 Okay, so low memory is delta for some, cumulative for some types.
**Marc Pichler** 38:13 I think low memory is… Delta for… I guess…
**Trent Mick** 38:20 You can check it. It's a mix, but I understand why the difference, no.
**Marc Pichler** 38:24 Yeah.
**Trent Mick** 38:25 Okay.
**Marc Pichler** 38:26 So, let's see, it's always a bit difficult to find this, metrics, SDK, export, TRP… And I think it's defined in here, So, the reason why it's different is because, You can also configure it via… Un… environment variable, and there, the environment variable is defined as an enum.
So, most folks who use the O3P export that they, Don't need to configure it, On a per-instrument type basis, but they just set this enum, because, Vendors usually support, like, one or the other, or bulls.
**Trent Mick** 39:26 Yep. And that enum is the one that includes slow memory?
**Marc Pichler** 39:30 Yeah, exactly. So, here we have…
**Trent Mick** 39:33 Yeah, they're just cutting, yeah.
**Marc Pichler** 39:35 these, I can actually… I copy the link here.
So this is what it defines. So that's why it's a bit weird,
**Trent Mick** 39:53 Okay, so going… okay, so then, if you scroll… Okay, so that first code block under temporarily preference.
Scroll down a little bit. Okay, so that one is showing the types that the… console metric exporter accepts. It does not accept a way of saying low memory. Do you think maybe that That was… A bug in the… Adding that option to the console metrics exporter, and that it should accept temporality preference.
That can then get resolved down to an aggregation temporality selector, which is per… instrument type.
**Marc Pichler** 40:42 I think we initially had the aggregation temporality preference, in… the metrics SDK, but we since removed it because it never was a concept that's actually defined in the Metrics SDK spec.
**Trent Mick** 41:01 Only in the configuration level things?
**Marc Pichler** 41:02 It's, thus, I'm actually not familiar with the configuration lever.
**Trent Mick** 41:15 Okay. This is not something that needs to get solved right now, but yeah.
**Marc Pichler** 41:19 Yeah, it is interesting, though, so… Does the configuration spec?
Apply this exported temporality preference to the console exporter?
**Trent Mick** 41:33 It does. So, fuse… That… so that's an extract of the… the JSON… schema.
And… If you go right to the top of this description, that's an example declarative config, so you can specify A meter provider with a console exporter that takes Temporality preference, is that what you meant?
**Marc Pichler** 42:00 Yeah.
That's… Interesting, because looking at the… at the SDK spec, There is… This right here… So… It doesn't define that, sort of mapping anywhere.
If I understand correctly.
I guess one of the workarounds for this would be to… just define it in the SDK node package.
When constructing, and mirror what the… OTRP exporter is doing.
That's a bit unfortunate, because it duplicates code that doesn't need to be duplicated.
**Trent Mick** 43:34 Yeah, that's not the end of the world. I mean, part of the reason for bringing this up is I wonder if it… feels like… you would want the same option for the same thing on the console metric exporter as you have on the OTLP metric exporter, whether changing one or the other, and that would…
**Marc Pichler** 43:52 Yeah.
**Trent Mick** 43:54 mean of breaking change or deprecation, and I've had two options, but…
**Marc Pichler** 43:59 My preference of… if I could choose where, aggregation temporality preference would live.
is the… metrics SDK, actually.
Because initially, I had added it to the Metrics SDK, and then we removed it, or… Like… I removed it at some point.
Because somebody called it out during a review, that it was in the wrong place.
**Trent Mick** 44:35 Isn't it? It is there now, currently, though.
Is it? Oh, no, it's in the… it's in the exporter.
Okay, got you, it's in the… okay.
But you think it should be SDK metrics?
**Marc Pichler** 44:48 Yeah, because it's the sort of shortcut that you… more, like… Sometimes you just want to have, like, an aggregation… Selector that just does all cumulative.
And you want to use that as the default, and you just want to say, like.
Because the spec always defines, like, oil cumulative as the default.
So it's very convenient to just… Take the cumulative preference with the pre-configured cumulative selector and not having to type it out.
And then also having the delta mapping, which has this odd one out for up-down counter.
having that… delivered from the Metrics SDK is very helpful, because then you can be sure that it would always be in sync.
You don't have to… Like, define that yourself.
And if new instrument kinds are being added, you also don't run the risk of, like, having the default case be wrong.
it doesn't happen that often that instrument kinds are being added, but the last one was gauge, I think, so… For that.
**Trent Mick** 46:10 That's what I was there.
Exponential histogram. That was the last one, but okay.
**Marc Pichler** 46:16 Yeah, it's not the instrument type, which… Since it's the aggregation type.
**Trent Mick** 46:25 But… Okay.
**Marc Pichler** 46:27 Isn't… That common to have either of them be added, actually, so… Doesn't really matter.
**Trent Mick** 46:38 Okay, so this is a bit of an edge case that the declarative could expect. The behavior… In the coming draft PR that I have for… creating a meter provider from declarative config will just be basically ignoring those two options to console for now, because it's not clear to me yet how to move those forward. And this is something we could… Deal with later, so… This is mostly just socializing that, because you're the right person to ask.
Okay.
Cool, we can move on.
**Marc Pichler** 47:10 Alright.
Looks like we are out of topics for today. Remove the triage section here.
**Trent Mick** 47:25 Oh, actually.
Given that Matt's here, maybe I'll add another one.
Where's Matt's issue for… being… Config provider, right?
**Matt Wear** 47:43 Issue or PR? PR.
**Trent Mick** 47:49 Yeah, right, to sound.
Can you add that to the last topic?
**Marc Pichler** 47:55 Yep.
**Trent Mick** 47:56 Okay, so… On that one, there's… this… specification, which I just saw recently.
spec PR.
Being discussed, but this is between… the two jacks of config that I like to talk about. Jack Shirazi works at Elastic, he's working on… using a config provider and, like, remote config the… policy stuff, and Jack Berg, who is the main driver of Hotel can fix stuff. I can't… I'm… Matt, I still haven't gotten fully back to your PR, so I'm trying to remember, but this… change might impact a little bit, because I think there was something there about when to… Well, actually, no, yours was about startup and when to… configure… instrumentations, right? There wasn't anything about a later change coming in?
**Matt Wear** 48:56 Or was there? To be able to reconfigure link?
**Trent Mick** 49:00 Yeah, okay.
**Matt Wear** 49:01 like, in my PR, and kind of just to remind you, maybe, of what we discussed previously was I don't know.
kind of… I had to introduce this, this registry that had, like, a mapping from the instrumentation name, like the NPM package name, to, like, factory that returned an instrumentation, just so that the config provider would be available to the constructor of the Of the, instrumentation libraries, rather than, kind of.
setting config after the fact, and we kind of talked about whether or not that's a great idea, and… and I did link on this PR another branch that, Actually predates this, when, config was set after construction time.
It was kind of before I introduced that factory.
**Trent Mick** 49:56 Yep.
**Matt Wear** 49:56 But yeah, this is… This is kind of the current scope, is that we have a config provider, it's available at construction time, and that's when, instrumentation is being configured, and if that's a bad idea, we can defer it to, defer it to slightly after that. I forget… if you scroll down to this link, I said where we can defer it to. Boom.
This one.
We can defer to enable time.
**Trent Mick** 50:31 Right. That's the only other time it could be.
And without breaking the instrumentation.
Contract our existing transportations, yeah, yeah.
**Matt Wear** 50:40 Yeah, so…
**Trent Mick** 50:41 I remember you'd link to that. So I guess, yeah, I'm gonna read this spec proposal thing, because I have this feeling that this is one that might move along quickly.
And see if there's some… some happy connection between the two. Like, if this thing is gonna propose a… this is the well-known function name where configuration happens, and if it could be kind of the same path for configuring instrumentation.
On initial creation or enablement, and then also later if they're, runtime configuration things coming along, then that would be cool. But anyway, okay, so it sounds like this shouldn't really impact your PR, but…
**Matt Wear** 51:25 It shouldn't, but…
**Trent Mick** 51:26 Might be interesting.
**Matt Wear** 51:27 Yeah, thanks for, like, mentioning it, because I think, I'd be interested to look at it, and yeah, whatever… like, Whatever approach we pick, it should hopefully be compatible with this future. You know, just make sure that we're not painting ourselves into a corner, and it might… It might make enable time versus, construction time. It might make one of those look a little better than the other, so… I think it's relevant.
**Trent Mick** 51:58 Cool.
Okay, thanks. So, just a note, and the usual apologies, I haven't gotten there yet fully.
**Matt Wear** 52:05 Yeah, no worries.
**Trent Mick** 52:08 Are you blocked on this for something at work?
**Matt Wear** 52:13 Boom.
Not necessarily, I think, I think my employer and a lot of people would like to see this at some point in time, but, I have plenty of other things that I'm working on, so…
**Marc Pichler** 52:38 Alright.
I guess let's move on to bug triage.
Looks like… no new… things here… One new bug report for Auto Instrumentation's web.
I think I did see a PR.
**Trent Mick** 53:26 Yeah, I thought there was a PR for this, wasn't there?
**Marc Pichler** 53:29 -
**Trent Mick** 53:35 although using Honeycomb, we could have just pitched it to… volunteered Jamie for this, but… look for closed PR, it might have been.
**Marc Pichler** 53:56 Oh yeah, there it is.
March last month… So that should be included in the latest release already, right?
Thank you, Trent, for driving that.
Latest release?
**Trent Mick** 54:15 It took about 9 tries to get through.
**Marc Pichler** 54:17 Yeah, I was out of office from Thursday to Monday, and then I came back and saw your struggles.
**Trent Mick** 54:27 Good timing.
David was out too, so I couldn't hit him up for… for approvals.
But did they specify the reason? So, Auto Instrumentation's web, the latest release?
**Marc Pichler** 54:48 That's… Says they upgraded from… 65 to 66…
**Trent Mick** 55:00 66 is the release last week.
**Marc Pichler** 55:06 Hmm, interesting. So, we changed… User interaction… But that was actually what… Ow.
So… It might have been introduced in this PR.
**Trent Mick** 55:46 Oh, this… added a bug.
**Marc Pichler** 56:11 I'm gonna put a P1… Label on here…
**David Luna** 56:19 You're gonna say anything to me.
**Marc Pichler** 56:22 Okay, thank you.
**David Luna** 56:26 Well, RSS can do, I think.
Since maybe I'm just, part of the cost.
**Marc Pichler** 56:34 Yeah, thanks for… for looking into it.
**Trent Mick** 56:38 That's your PR.
**David Luna** 56:40 Well, I, I gave the thumbs up.
So…
**Marc Pichler** 56:52 Did I merge it? Probably, right?
Hold on, wasn't me.
This, usually, I'm involved in these sorts of things as well.
Thanks for, looking into that.
If… you need any reviews for the fix, feel free to let me know. I try to make time to look into those.
**David Luna** 57:21 I'm just happy that Jamie is not here, so she can't yell at me.
**Trent Mick** 57:27 Because she yells a lot.
**David Luna** 57:29 Yeah, yeah, no.
**Marc Pichler** 57:37 Alright, so that was it for the contrib repo. Let's see if there's anything that we missed.
Shit.
Looks like a pack, but wasn't reported through the… Template… That's already 3 weeks ago, so… Shouldn't be anything new here.
And… or so… some time already, so… nothing new here as well. And… 2 minutes left, I guess we are out of time for… Aww.
Today, anyway?
So, thank you, R, for joining.
-Oh.
**David Luna** 58:32 Okay.
**Marc Pichler** 58:33 And… see you… In… Probably 2 weeks, I have to check my calendar, but that'll be out next week.
Alright.
See ya.
**Matt Wear** 58:44 Thanks.
