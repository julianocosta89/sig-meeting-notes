SIG: JavaScript SIG
Date: 2026-04-29
Duration: 63 minutes
Zoom Recording URL: https://zoom.us/rec/share/JbQ4j9IaZnJKiDT3ll9mZBeLwNVdtcLZTnrtbi1sLVQzxqWnxTEFU4qhWke372O3.sM3cJeJq24nReR1P
============================================================

## Zoom Recording Transcript

Trent Mick 00:01:10 The wall?
David Luna Bistuer 00:01:15 Morning.
Daniel Dyla (Dynatrace) 00:01:18 Hello, everybody.
Marc Pichler (Dynatrace) 00:01:41 Hello?
Alright.
It's good.
Urgent.
Welcome, everybody.
Thanks again, we still need to move this up here, do that real quick.
G.
So the first topic on here is something that I would like to bring up, this is… a PR that… essentially just adds a feature to the API, which, allows folks to… change the way that the tracer provider is… created, so it's essentially just wrapping it somehow.
And these feature requests come up from time to time, and I'm wondering, I'm essentially wondering how… We define vendor neutrality in a way that, Like, especially around these sorts of things.
I see that also coming up, not just here, but also in other places where, people want to, just change the data that's being emitted through some, proprietary way.
Which, doesn't exactly, match my understanding of vendor neutrality, because I think… the way that Otter is structured, it kind of makes it a bit harder to do these sorts of things.
By what feels like on purpose, so that people go through the process of getting their components specified and stuff like that, so that, there's not as much stickiness To a vendor on the app side. So you can just export the data to different Different vendors, and, you were… essentially limit the amount of data that you get by just using OTERL, and then… Everybody gets the same stuff, but if you move agents in this way.
Like, you would essentially lose that data.
I don't know if that makes any sense, but… That's essentially what I'm seeing here.
I'm wondering if anybody else has, thoughts about, tacking on features like that.
And if we should block these sorts of things, or if we should… Do more of… or do more to allow people to modify these sorts of things in that way.
Trent Mick 00:05:24 Oof. I don't know about it.
the comfort level I have for setting wide precedent and things like that, but for this one, I'm not exactly sure what they're… trying to do is… is… so this… He's saying like Datadog is… I don't know if he's representing Datadog here. I mean, representing, whatever. But… Are they… having users use the SDK, but before that, a… dash dash require or dash dash import data dog thing is in their monkey patching SDK components being loaded.
As opposed to, if they want users to use a Notel SDK, they could make an SDK that can maybe they're trying to do that, and even so, it's still… it's hard to get to the node tracer provider, because if you want users to use the SDK node package, I don't think it has… Ways for the, like.
SDK node is like an SDK. It's not an SDK builder, so if a vendor wants to make a distro, it's kind of hard to reuse any components out of there, and I think that could definitely improve.
But I don't know if… doing something here at the API level is something that we would want.
But I don't know, I… I did a quick grep of the DD Trace.
repo, and I didn't see, I didn't immediately see what the use case was here, but Maybe I didn't look hard enough. I don't know, do you… would it be reasonable to ask them what to… if they can point to a specific coder of things being done, and we could think about design level, how that could be better supported?
Marc Pichler (Dynatrace) 00:07:14 Yeah, I think that could be helpful. I'm kind of hesitant, to add something like that to the API, because To me, it feels like it's just, like, working around some issue, and we don't know what the issue is.
So, I think finding that out, would probably be the best course of action here.
Trent Mick 00:07:42 Do you want me to follow up on?
Marc Pichler (Dynatrace) 00:07:44 If you, want to look into that, that… And… and you're interested in it, I wouldn't be opposed to you following up, but I can also ask them there, so… Whoever.
asks first, I guess, gets… gets dibs on that one.
But yeah, I think with Node SDK in particular, getting to the tracer provider and modifying that one is a bit difficult right now, so I can see why they would run into this.
particular issue.
I'm also not sure if the idea here is to replace the tracer provider that's being registered with DD Trace in the first place.
Though, it should be possible to just retroactively replace that one by just calling register again.
or whatever it's called, the Register Global Tracer Provider again.
That would…
Trent Mick 00:08:52 I think he's saying that the first… the first one wins right now. You can't. I don't know if there's an override that you can pass.
There was for some things. I think for the Diag logger, you can pass in over… I can't remember specifically.
Marc Pichler (Dynatrace) 00:09:08 I think this is just the way that, this works now.
Yeah, so it's most likely that whatever SDK they have gets registered first, and it wants to prevent, re-registration of an SDK.
So, but what I'm hearing is, we would… Need more info for this particular case.
Trent Mick 00:09:49 Yeah, my read of the code is the first one wins. First one to.
Marc Pichler (Dynatrace) 00:09:52 Costa.
Trent Mick 00:09:52 Global Tracer Provider wins, then you can't… I mean, you can cheat, but it's just JS, everything's open, but anyway, that's not what they want, which is reasonable. Okay.
Marc Pichler (Dynatrace) 00:10:09 Alright. But then, let's look into that a bit more another time, and… We can move on to the next topic if nobody else has any.
Any ideas about that?
Alright.
And the next one is… Marilla, I'm sorry for not getting to review that PR.
Marylia Gutierrez 00:10:34 Yeah, so yeah, just this one, because there was, like, two things here. One of the tests were not passing, the percent address, but I still, yeah, I need some help with the actual contents, because I'm not as familiar, so yeah, just pinging again.
Marc Pichler (Dynatrace) 00:10:48 Okay.
Yes, I'll assign myself as well.
I'm also not familiar with the content.
Marylia Gutierrez 00:10:57 Yeah, so the thing is, like, the part of the Postgres that, yeah, I get it, but about, like.
is that how we propagate context and stuff like that? So that is the part that I'm not familiar, so if any is aware of that part, then, yeah, I appreciate the help.
Trent Mick 00:11:14 I think a similar thing was done with one or two of the other databases, one of them may be Oracle.
Marten Hennoch 00:11:19 Or a brand. Microsoft SQL.
Trent Mick 00:11:22 Okay, there you go.
Marylia Gutierrez 00:11:24 Yeah, I think they put the links for some examples, right, on the description.
Marten Hennoch 00:11:28 Yeah, I can't.
Raphaël Thériault 00:11:28 looks like the collector has merged the PR that they linked.
Marten Hennoch 00:11:34 Yeah.
I have a spec issue also, which is going somewhere, but I haven't addressed their comments yet.
And I have a similar one for MySQL.
But I can book the… Put the links.
Marc Pichler (Dynatrace) 00:11:52 I think we've also had one… This was the one for… Implementation Postgres.
Yeah, I have to read up on that one again. This was a long time ago, 2023.
Marten Hennoch 00:12:14 It's a bit weird, because I initially wanted to use SQL Commenter for this.
But they said it doesn't work for prepared statements, which is true. And then I looked at Datadog, and Datadog for Java, they use a set application name, like I am doing here, but for Node, they are using SQL Commenter to send it, so I'm not sure why.
Trent Mick 00:12:37 But not for prepared statements, though, right?
Marten Hennoch 00:12:40 Yeah, so it doesn't work, yeah, similar.
Raphaël Thériault 00:12:47 Yeah, I can also look at the contents. I'm fairly familiar with that part of the context propagation code, because I contributed it.
Well, the SQL commander part, at least.
Marc Pichler (Dynatrace) 00:12:59 Thank you for looking into that one.
Very much appreciated.
Marylia Gutierrez 00:13:14 Yeah, next one is me again. Just saw someone open a PR, but… seems like a… it is about profile, but it's… they are saying that they are not actually following this back for profiling, so is that a test? And it's also using, like.
the Datadog dependency here, so… a lot of things, kind of, like, weird, so I don't know if they are already… brought this to anyone, so just try to understand, like, the… What is, like, behind this change, and if we actually make sense to accept or not, because… If it is not… Following specs, and it's just…
Marc Pichler (Dynatrace) 00:13:52 There's, like, a…
Marylia Gutierrez 00:13:53 They mentioned, like, it's more of a bridge, so we can have this back. I just was not sure if that makes sense or not.
So just wanna, yeah, to bring to… To people's attention.
Marc Pichler (Dynatrace) 00:14:07 I think I was, this person… already, asked for something like that. There was, like, a profiling idea, and I wonder if their, approach here is similar to the one that they suggested. They were on the SIG meeting a while ago and asked about that.
I didn't have a lot of context, Back then, when they brought it up first, as to, like, what the current plans are from the specification sake of how, like, profiling would look like if we had Something like that added here.
And from reading the specification, it also wasn't very clear to me, how it should look like, so it seemed to be very, very much… Work in progress thing.
I think what we have to do for this one is to… Maybe bring that up in the spec core and see.
What guidance there is.
I don't have an immediate idea of what to do with this bundle.
Jamie Danielson 00:15:43 Is it possible that they didn't mean to open it here?
like, I'm looking at their… like, other PRs around the same time, where they look like they're being pushed to forks.
Of different things?
And so I'm wondering if they meant to push it to their fork instead of… Upstream.
Trent Mick 00:16:08 Is that a hotel copyright header, so…
Marc Pichler (Dynatrace) 00:16:16 I think they also edit, like, these in…
Trent Mick 00:16:21 Yep.
Marc Pichler (Dynatrace) 00:16:23 Open telemetry, namespaced one.
I guess we can… asked them here. Are they also assigned ECCLA here?
Jamie Danielson 00:16:35 Oh.
Well, nevermind.
Marc Pichler (Dynatrace) 00:16:55 I think the dependency… Like, the thin wrapper.
Around the pre-proof package.
might not be what we want. I haven't looked into it that much to be able to form a good opinion of What's acceptable here, and what's… what isn't.
I don't know if anybody else has any thoughts on this.
Trent Mick 00:17:37 Yeah, I don't want to be the naysayer, and I don't really have a lot of comfort at a higher level than Motel.js, but… adding… I mean, I'd certainly change the name to say PPROF in a profile, because that just starts to imply that it's the hotel profile spec.
I don't know, when… Like, this would have a better life outside of hotel.
Potentially.
Marylia Gutierrez 00:18:05 So yeah, that was, like, my thinking, if this is just, like.
more like a, like, a test it out, like, maybe, like, proof of concepts, or… I don't… so this was, like, what is the reason behind this PR? My words, like, keep on their own fork, and then they can use whatever dependency on vendor they want, they can… Point people to test it out on that one, but keep, if we're putting things here.
on, like, this package, I think it should be, like.
following whatever is the right names for, like, profiles and specs and whatever it is. So that was my thinking behind it.
Trent Mick 00:18:43 I mean, Datadog and their PProf work were heavily involved in… hotel profiling stuff, so, I don't know that the Datadog PPROF dependency is necessarily, like, oh, we're vendor-tied, necessarily. I don't really know, but… but I know what you're saying.
Marc Pichler (Dynatrace) 00:19:06 Yeah, the… like, this is the specification for, Profiles at the moment, so it doesn't really give a lot of… Of info, what should… And should not happen.
It seems this is mostly concerned.
About the format that's being used.
But it can't be… Like, translated between the two.
But in any case, I agree that we probably don't want to have it in the form that it is right now, with this thin wrapper, where it's, I suppose it also has some form of export that's non-OTRP.
I haven't looked into it.
In detail.
That was, like, an export definition. I put this on my list as well, to dig into what the person was trying to do here.
Because it's also somewhat related to this, issue right here. I'm not sure if the… Who people that, were working on this are.
Related in some sense.
Or known to each other.
Correct.
Trent Mick 00:20:43 I don't know, Datakit at all. Does anyone else see this?
Marc Pichler (Dynatrace) 00:20:53 Sorry, I didn't get that.
Trent Mick 00:20:55 I don't know DataKit at all, I don't know if anyone else is.
I think I'm on the right place, it's a… On docs.gwants.com?
Marc Pichler (Dynatrace) 00:21:16 I've also never heard of this.
Trent Mick 00:21:31 Gonna jam here faster.
Marc Pichler (Dynatrace) 00:21:46 Alright, lots of stuff today where we don't know what to do with it. I will, I'll have a look into that one, and try to figure out what's, What's going on there?
I also tried to join the… spec core… At some point.
To see if, anybody else has… any profiling-related stuff, because I think nowadays the most profiling-related stuff is in the eBPF thing, right?
Trent Mick 00:22:24 That was my understanding. I don't know if that's the only sported collector of… Profiling data by… In Otel technology?
Like, if so, then this collecting profiles using… V8 Profiler, which, if I understand correctly, this thing is doing, is interesting for JS.
Marc Pichler (Dynatrace) 00:22:47 Oh.
Trent Mick 00:22:48 But yeah, I don't know what… Is this a TC kind of thing? They would require any… or strongly suggest any blessed thing by… in an OpenTelemetry repose, the porting, exporting, and the profiling?
formatting.
Marc Pichler (Dynatrace) 00:23:06 Boom.
Trent Mick 00:23:08 Yeah.
Marc Pichler (Dynatrace) 00:23:16 Right, I guess let's move on to the next topic. Then, David.
David Luna Bistuer 00:23:25 Yeah. Oh.
Basically, since, we are super Javid at the context, so we want to move on on the, on the SDK, To a new major release, and one of the goals is to have a kind of a unified SDK for Traces.
Well, when I was looking around, it looks like, the SDK node doesn't need SDK trace node anymore, because we're already doing the… registration of propagators and also the context manager, and then we are getting… so we are getting all the configuration that is needed.
we even are not calling. So, one of the differences between the base… the basic provider and the node provider and web provider is that Note on web providers, they have a register method A convenient method just to resist the propagators and context manager.
An SDK node doesn't… it's not used anymore.
So, we can just replace it. So that PR is just replacing that, so I'm using… for now, we're just testing directly the SDK tree space.
Because SDK Node already does all the configuration, all the registration of Context Manager and, propagators. So we can use it directly there.
So, my question is, is it too soon to do that? So, I guess the next step is, like, to be, Preview that base package, and finally, come up with the final package, which is going to be a consolidated package of all… that will work for both platforms, weapon and… and Node.
Well, that's a change, so basically I'm just, you know, replacing.
The note is provided for the basic one.
Because it is a NACOS change, so actually we're doing nothing.
With the node, we are not using the method that differs from the basic disk provider.
So my question is, is it too soon? Should we wait for that?
Or should we wait for having everything consolidated, and then just… Migrate directly to the… To the final package, or…
Marc Pichler (Dynatrace) 00:25:43 I think doing it as early as possible is better, because then we can… we don't have one big bang, release where we find out any issues, if there are any, so I think I'm in favor of doing it now.
There's possibly a bunch of other stuff that we can also do to… make, we could essentially introduce, like, an SDK trace package into the low already, Because we're just adding a new package, right?
So that's… that's also something we could do already. So I think the more we can do, before working on 3.0, the less we have to do later, and people can already start trying it out in the way that we recommend it.
So I think it's an all-around… all-around positive thing to do it early.
David Luna Bistuer 00:26:46 Okay, about adding the new package in the 2.0 doesn't… Will that add more maintenance in the 2.X branch?
Marc Pichler (Dynatrace) 00:26:59 It will, yeah. We don't have to do it, like, we don't have to do all of that now. I think we can if we decide to, but We can go step by step and then decide how much is too much at once.
And then defer that to later. One of the things that I've been thinking about is, Right now, we have the basic tracer provider, which does, read the environment variables and all that stuff.
And I think it would be nice to have the… tracer provider that we want people to use later on already in SDK Trace Base.
That doesn't read the environment variables.
Because this way, people can move over to like, the way that the tracer provider will behave in the future already. So then, when it goes to… through the low end, we have this new package.
It's just a matter of changing the imports.
Which would be a lot easier.
That's one of the ways we could continue with this, so… so then… basic tracer provider would essentially just be a thin wrapper around the tracer.
Provider thing that we now introduce.
That doesn't read that in, does read the environment variables.
And just forwards it to that one. Essentially, just a configuration thing around the tracer provider there.
That's also one way we could go about it. So, there's multiple ways we could do this.
To get more changes into 2.0 already, so that, we don't have to do everything all at once, get on.
David Luna Bistuer 00:28:54 Okay. Maybe we can start with this change, and then, make the SDK note.
actually, parts and everything, from the, From the AMP, from the environment, and then use this new class.
Okay, so I can follow up with that, PR. Okay.
Marc Pichler (Dynatrace) 00:29:12 Thank you.
David Luna Bistuer 00:29:13 Yeah, that was a good point.
Then, if that is okay, then, I think also that something that we can do already is also on the contribute, we can… Use… we are using a lot of SDK Trace Node.
to create a new trace provider, and registering just for testing.
What I did… what I think that it could be done is, like, we have, the test utils package.
That registers and everything, so you just give the configuration and does all the registration of propagators, context managers, and so on.
So instead of just doing… repeating that code everywhere, I'm using the register method to give a provider, a trace provider for the tests.
Trent Mick 00:29:56 I actually like repeating the… I actually like repeating the code, but I'm not opposed to using the test details, because it, like, it boils down to, like, two lines, right?
Depending on… doesn't it? To register the tracer… to register the.
David Luna Bistuer 00:30:10 No, I…
Trent Mick 00:30:11 in the context. Yeah, okay, I understand.
David Luna Bistuer 00:30:14 So you register the propagators, the context, and you get the simple spam processor, and then you need a memory span exporter, and then, finally, you register everything, or you call register on the trace provider, and then, okay, you're using these, Memory span exporter just to do the assertions on the spans.
Trent Mick 00:30:34 Or, or you use SDK Node, right?
David Luna Bistuer 00:30:39 Yeah, there's another thing that you can register a complete SDK, yeah.
Trent Mick 00:30:44 Anyway, yeah, okay.
David Luna Bistuer 00:30:47 Yeah, there is a draft VR, so on the document, there's a draft VR, you can have a look and give me your opinion. It's a draft term, I'm just starting with the… It's a PR and contribute that actually does this. Actually, it's just real.
Replaces this usage of… a SICK, the context manager, the… All these kinds of stuff.
Marc Pichler (Dynatrace) 00:31:18 Well, I think we can… figure out the future of D.
the contrib test details later.
Trent Mick 00:31:32 And that's independent, you can go back and forth either way, it's fine, yeah.
David Luna Bistuer 00:31:36 Yeah. Yeah.
Apple things are independent, too.
Marc Pichler (Dynatrace) 00:31:43 I wonder if the test user stuff… Could be simplified with the, declarative config.
Things later.
Because if we just have, like, a declarative config for testing.
That could possibly simplify stuff, and we wouldn't need the extra package anymore.
Haven't thought this fully through, this is just… an idea.
David Luna Bistuer 00:32:13 Well, yeah.
then it means that you have a single trace provider for the whole test suit. Sometimes I've seen that, you know, they're just pre-creating the provider.
I don't know if that's necessary?
Well, at least I've seen that in the instrumentations.
So you have a block of searches, or a block of tests, a test suit that does this, and then you have another Describe block that does the same thing and then creates a new, a new tracer provider.
But I don't know, I'm not sure that that's… Unintentional, or maybe it has… It has, an end.
Marc Pichler (Dynatrace) 00:33:00 I wish I could answer that question.
There's, some weird things going on sometimes in contract tests.
David Luna Bistuer 00:33:09 Huh.
Marc Pichler (Dynatrace) 00:33:12 I think some of these…
David Luna Bistuer 00:33:13 Either way…
Marc Pichler (Dynatrace) 00:33:15 Some of these are intended to just clear internal state.
But I… Can't really tell if that's really, What all of them are doing, or if some of them are just… Doing it because some other package did it the same way.
Yeah. We have a lot of that as well.
David Luna Bistuer 00:33:39 Usually repeat patterns, yeah. Hold on. Sorry, I'm not… I'm not… sorry, I haven't followed the… the implementation of the configuration. It's… is it possible to get already a tracer provider from a declar… from a… Declarative configuration.
Trent Mick 00:33:54 Very recently, yes. Only very recently.
Marillia had a PR that merged last week, I think, for that. There's a bigger PR that's getting emerged today that… make some significant changes there, that's Mike's… long-time work PR for generating, types and using HAV for, schema validation of stuff, so I… I think that stuff's improving right now. I'm not sure I would start using it in tests yet, because it's certainly… it's going to blow up your 5 lines to, like, 30, because now you need YAML content. And I think currently in a file, you couldn't pass it from a string. We could make that kind of thing work if it… if it makes… Testing site.
David Luna Bistuer 00:34:38 while I was…
Trent Mick 00:34:39 Europe, but…
David Luna Bistuer 00:34:40 I was thinking that now we… we already use a Docker Compose file for everything, maybe having kind of a… Well, maybe a singular or a unique, declarative configuration for tests, maybe it's not… the best approach. But maybe some could be reduced, so it's like, okay, you have a default one.
And maybe you need something extra, then you add your own.
Include the confirmation. Well, okay, don't worry.
It's just…
Marc Pichler (Dynatrace) 00:35:09 As I said, I haven't fully thought that… I should have kept that, thought to myself, maybe. Sorry. That's morally suggesting.
Trent Mick 00:35:20 Yeah, like, if you're setting up an SDK for tests, there's… there's the lowest base-level stuff, right, which is…
David Luna Bistuer 00:35:26 Yeah.
Trent Mick 00:35:27 Rate a tracer provider and register it globally, and… manually create the exporter and the processors. And then there's the next level, which is using the SDK.
And that's either Node SDK or the start Node SDK thing that we have going, and the latter, the start one, is one that supports the optionally using environment variables or using configuration files. So, I mean, it's morally equivalent to saying, instead of using the base level primitives, let's use the SDK, and then you can pick your path.
They get poison there.
David Luna Bistuer 00:36:00 Yeah.
Marc Pichler (Dynatrace) 00:36:02 It's probably not something that we want to do soon as well, because there's still development going on for A lot of the stuff in this new code path, and we don't want to block anybody.
Chrome.
Iterating quickly on it.
Trent Mick 00:36:20 Yeah, I think it… right, it puts more balls in the air for an individual test case to be including all the configuration stuff at this point.
Probably easier to just be relying on the primitives, yeah.
David Luna Bistuer 00:36:34 Okay.
Thank you.
Marc Pichler (Dynatrace) 00:36:39 How would that be known that one?
Sorry, go ahead.
David Luna Bistuer 00:36:45 Yeah, I'll move, I'll move up, so I'll… waiting for your review on that, and then on the tests, on the construct part, yeah, I'll update the test, and… Yeah, at least first, the first thing that we're going to do is just to move it to contribute.
Test utils, and then maybe you can think about… Improve that.
Marc Pichler (Dynatrace) 00:37:14 Okay, any additionals?
Discipline.
Nope.
And let's move on to the next topic. This is, Jan, about… Or could the…
Jan Peer 00:37:33 Yeah, so this is basically a thing to… support Cloudflare, because you can run Cloudflare everything on Cloudflare, but they have their own Wrangler thingy, their own built… built thing.
Which needs to have her own export card work ID, otherwise it will always go to default and uses common.js.
Which means then tree shaking won't work, and if you go a little lower, there's a showcase, if you open them up.
But just changing the… the exports.
It's reducing it by 60 kilobytes.
by just using… Trace.getactivespan in the test repo.
So I don't know if this is actually wanted to support WorkID, because before you also said that OpenTelemetry is vendor neutral.
I mean, Burke Cloudflare's not really a vendor, but a place where you can deploy it.
So it's very specific to Cloudflare.
Yeah.
Marc Pichler (Dynatrace) 00:38:42 I think, yeah, the vendor neutrality that we usually talk about is, like, observability vendors, so…
Jan Peer 00:38:49 chicken.
Marc Pichler (Dynatrace) 00:38:50 Yep.
That one, I think, is… is some… thing we would want. We would want to increase compatibility wherever possible. Okay.
Trent Mick 00:39:05 Our story for different runtimes is spotty, though. Like, we don't…
Jan Peer 00:39:09 Yeah.
Trent Mick 00:39:10 have a good story for issues that come up with Bun or Deno, for example, if they… which are other JS runtimes to think about.
Jan Peer 00:39:18 Yeah, but with Cloudflare, OpenTelemetry works in Cloudflare, especially the OpenTelemetry core API.
And semantic convention, of course, they don't actually use any specifics or runtime-specific API.
Trent Mick 00:39:35 Yep.
Marc Pichler (Dynatrace) 00:39:37 And… So, if I understand it correctly, it's… It only works if you add that, specific…
Jan Peer 00:39:45 So, if you…
Marc Pichler (Dynatrace) 00:39:46 Oh, wait, you have not…
Jan Peer 00:39:49 If you open up the first, first link.
Oh, no, sorry, the second league. I'm sorry.
they actually have the bundler, and they go by default from worker D, Worker, or browser, because this will.
Marc Pichler (Dynatrace) 00:40:04 important to craw.
Jan Peer 00:40:04 also by default.
And this is where they default to, if there's no browser and nothing else, then they go to whatever is the default, which is in… In your case, which makes sense, common chairs.
So if you would write browser here, then it would take the browser bundle.
Marc Pichler (Dynatrace) 00:40:25 Oh, if we can…
Trent Mick 00:40:27 A worker name, is that something that's used by other tooling? Are you aware of? There's Worker D, Worker, and browser. Is Worker from… Some other, world.
Jan Peer 00:40:38 Yeah, good question. Maybe worker is actually the better, better one, because work… it's not really a worker D.
But I don't know any other… I mean, Sentry's using a lot of Workiti.
Oh, for this purpose?
But… I don't know if I'll elaborate.
Trent Mick 00:40:56 I don't have a preference one way or the other, I'm just curious why Worker's in there at all, if Worker D's a close or a specific one.
Jan Peer 00:41:03 Yeah, good question. I mean, I can… I can raise the question, or I can… I can actually check.
Why is this the case?
I mean, theoretically, Worker, they have edge functions, so not everything is supported, right?
Trent Mick 00:41:22 I mean, it sounds like a pretty easy addition for Open Declanetry packages.
Jan Peer 00:41:26 Yeah, the only thing I've checked, instrumentations and everything.
And the exports, so from line 9 to line 22, this thing is missing for a couple of exports, or for a couple of package chases, so this has to be added there as well.
But yeah, it's just an addition, just an upgrade.
It's nothing trivial.
Trent Mick 00:41:48 having an exports at all, you mean? Like, can we look at what's…
Jan Peer 00:41:52 Slow exports heat.
Okay, then…
Trent Mick 00:41:55 The potential danger there, then, is that deep imports are broken, but I think our position on that is that we don't care, sorry.
Ugh. Am I…
Marc Pichler (Dynatrace) 00:42:07 I think… I think for deep imports, so if we want to be super careful about it, we can delay that to 3.0, and just add the exports to all the packages in 3.0, and then we say, starting from 3.0, Deep imports are super not supported, versus just not supported with what we had before.
Trent Mick 00:42:31 We're not supported, yeah.
Marc Pichler (Dynatrace) 00:42:34 So, that's one option. So the reason why I asked about the different… the different strings to use here is, I was wondering if there's a way to get compatibility with more build tooling by just using something more generic.
Because if we add the… work at the… thing, And then some other tooling comes around, and they have their own thing, and then we just have this huge.
Jan Peer 00:43:17 Hmm.
Marc Pichler (Dynatrace) 00:43:18 Huge amount of different, exports here, then can become a bit unwieldy.
but I guess it would also make sense to just start with the most, Specific one, and then… We decided…
Jan Peer 00:43:33 I mean, theoretically.
Marc Pichler (Dynatrace) 00:43:35 water.
Jan Peer 00:43:35 Yeah, theoretically, I can also open up issue at the Workers SDK repo, and just ask if they could support it. Did they also… I mean, module doesn't really work, because they have their own edge.
imports.
Yeah.
Yeah, I can still, I can still open up, An issue.
to see if they have actually a different opinion on this, if it would make sense to add it on OpenTelemetry.
Trent Mick 00:44:08 I'm curious if anyone from the browser seg would have an opinion on adding browser.
in there.
Because that would potentially solve the problem for… Belstar workers.
But then, obviously, that doesn't work for node-specific API, so we can't be using a browser condition and having node-specific code in it.
Marc Pichler (Dynatrace) 00:44:34 So…
Jan Peer 00:44:35 Yeah, I mean, this addition, I also wrote it in the ticket, this edition shouldn't be done for browser, if you have a browser-specific Export, you shouldn't do this there.
Of course, yeah.
Marc Pichler (Dynatrace) 00:44:55 Oh… I would say I'm generally in favor of adding this.
I'm just… Wondering how we… can properly test stuff like that.
Trent Mick 00:45:17 Is this something…
Jan Peer 00:45:18 It can fit.
Trent Mick 00:45:18 The bundler… bundler test, having another…
Marc Pichler (Dynatrace) 00:45:21 moved.
Jan Peer 00:45:26 I mean, there's the… the Wrangler CLI?
Which runs locally, and… Basically supports that.
So this could be spin up somewhere, and then you can check the… either bundle size, or… -Oh.
Whatever you want to test them.
Marc Pichler (Dynatrace) 00:45:46 Oh.
Trent Mick 00:45:47 And that is… that is the main goal here, right, in having a reasonable… Target that results in… A tree shakeable…
Jan Peer 00:45:55 Yeah.
Trent Mick 00:45:55 smaller bundle.
Jan Peer 00:45:58 And in our… in the OpenTelemetry case, ESM is the option. I mean, usually you have your own bundle for work ID, but since you don't have any No specific… APIs, it doesn't really matter.
Boom.
But yeah, I could suggest that we can leave this for now. I opened up a ticket there, what they think is the best, because they are the Gross, right?
And then I'll just cross-link it, and then we'll see where it goes to.
Marc Pichler (Dynatrace) 00:46:45 Yeah, I think that's a good idea. Yeah.
Yeah, as long as… I think as long as we can somehow test it, it would be fine. Also, having some sort of an end-to-end test would be great, just to make sure that, like, if we add code, that we don't break something basic that should also work on Cloudflare.
Because also adding this export, it… Has… it gives, like, a certain sense of, like.
us saying we support this specifically. Yeah.
Jan Peer 00:47:24 Makes sense.
Marc Pichler (Dynatrace) 00:47:24 which, like, if we put browser here, then that's a bit more generic, right? But.
This, is very specific already, so we should also test it somehow.
Yeah, it didn't.
Jan Peer 00:47:37 That's for sure. And that works fairly easy.
Marc Pichler (Dynatrace) 00:47:41 Yeah, if we can test it, I think this is one of the things that we could get started with.
already, since you said that the Common.js bundle works at the moment.
We could add tests for it, and then once we add these exports.
We know that everything works the way it should, once we publish it, and should be smooth.
going on from that point. We've just had a lot of issues in the past where we didn't have proper tests for specific ways to bundle stuff up and to build stuff, and then stuff breaks, and it's always very difficult to troubleshoot, so if we have some tests in place.
To make sure that this isn't happening, and to reproduce stuff, then that's a lot easier.
Trent Mick 00:48:33 Is this potentially a long… like, there's… there's a… possible lurking can of worms here. If… If the goal is to have a running hotel SDK in a Cloud for a worker, which I assume it is.
then the API package is just a starter, right? You need it.
many of the SDK packages.
And… Are we talking, like, the browser?
packages, or are we typically… is this closer to a nodeish-type runtime? Actually, I don't really know the runtime at all.
Jan Peer 00:49:07 It's, WinterC.
Or WinterTC, or whatever it's called right now.
Trent Mick 00:49:13 Yeah, okay. Yeah, then again, I don't have a good sense of where.
Jan Peer 00:49:18 Yeah.
it's basically, they try to shim… over the time, they try to shim everything with Node.js, is supported?
But they're not there right now.
So a lot of things are not working, but the majority of things which are also used by OpenTelemetry are working.
But for example, because it's ESM, they can't… How do you see?
they can't patch or monkey patch the modules. If there's, I don't know, Postgres.js, for example?
The instrumentation, they can't use it, because it uses monkey patching, because it would need the dash dash import.
And they don't support that.
But the rest works out of the box.
Trent Mick 00:50:01 So, what kind of things are being instrumented?
So what are you getting?
Tracing data from what.
Jan Peer 00:50:09 to Corey Street.
Trent Mick 00:50:10 package, and you're writing…
Jan Peer 00:50:12 I mean, there is, you can Google for Worker CF Hotel, I think it's called.
Or, CF Hotel, something like that, Cloudflare Hotel.
Trent Mick 00:50:23 Okay, yeah.
Jan Peer 00:50:25 Yeah, the first one?
And this one basically instruments… How long does your… Request take… Yeah, basically everything.
Trent Mick 00:50:40 Okay, so fetch.
Jan Peer 00:50:43 Yeah.
It needs to be wrapped, basically.
But there's this fetch call, and you need to wrap it.
So you can't really monkey patch anything.
Wow.
Marc Pichler (Dynatrace) 00:51:02 re-implement, I don't know, tracing channels, or…
Jan Peer 00:51:11 The… Tracing channels would work.
This is also a reason why we try to invest a lot of time in getting support in tracing channels.
Especially for the… Libraries as well, because Cloudplay is going… like, skyrocketing right now on NPM, at least, like Wrangler.
Marc Pichler (Dynatrace) 00:51:37 Oh, stop.
If we were to land support for tracing channel instrumentation, or tracing channel-based instrumentation, this could also help, that situation here, right?
Jan Peer 00:51:50 Executed.
Marc Pichler (Dynatrace) 00:51:53 Just trying to figure out what, like, The full picture is on all of this.
Jan Peer 00:52:01 I mean, basically, basically, Most tracing channels, everything supports it, like Vasel, Netlify.
Every vendor, like the… Other type of vendor.
Marc Pichler (Dynatrace) 00:52:18 Right. So I guess next steps, let's, see what the Cloudflare folks say. In the meantime, we can look into tests.
First and then once tests are in place, and… there might be an answer or might not be an answer on the Cloudflare side. We can decide what Or which exports to add.
And then, continue from there. Does that sound correct?
Jan Peer 00:52:52 Yeah, then I tried to open a PR this or next week.
Or the week after, because I'm busy.
With the tests?
And then it's just… Spin off some tests, and open up a PR.
As a draft or whatever.
Oh, yep.
Marc Pichler (Dynatrace) 00:53:13 And then we can have a look at that and get that merged, and then once we end up at… Doing this here, we'll also be able to verify that, But the size is reduced, and everything still works, so… - I think that's… that's a good path forward.
Right.
Jan Peer 00:53:42 By the way, one question, do you know, are there any… are there any tests already which checks for bundle sizes?
In OpenTelemetry, I haven't checked that yet.
Marc Pichler (Dynatrace) 00:53:50 Just yet. I don't think we do check bundle size, necessarily. We do check if it works, so… There's a few things that don't work at the moment, and… We also somehow check for that.
essentially that we don't get any additional warnings that we don't want, but we don't do any bundle size tests, so that would probably also be helpful to see in certain PRs if we're adding more, More stuff that's very inefficient to tree shake, or whatever.
Jan Peer 00:54:31 costs… I ask because, theoretically, if you want to check if the panel size is raising, you need to save the state somewhere.
And have a base base state, which needs to live somewhere.
Daniel Dyla (Dynatrace) 00:54:45 We do…
Jan Peer 00:54:46 So this…
Daniel Dyla (Dynatrace) 00:54:47 We do something similar already with the benchmarks. We… state is saved there, it's saved in the… I forget what the branch name is called, like, GH Pages or something like that, and there's, like, a… There's states stored in there, and we could do something similar.
Trent Mick 00:55:05 Similar to coverage, too, though, using a service for that.
Daniel Dyla (Dynatrace) 00:55:09 Yeah, coverage is an external service, same idea.
Bundler size tests are something that… I have thought about for a while.
I think it would be a good idea.
It's just that with so many different bundlers and different configurations, and… Like, it's almost impossible to come up with something that's really, truly representative.
Because if you were… if your bundler test used… all three signals and, you know, instrumentation. Theoretically, ideally, all of the code is actually useful in some way, nothing gets shaken out. So, for tree-shaking tests, it's always kind of odd. And then if you're… testing for, like, okay, how friendly are we to minifiers? That, again, depends on which minifier you're using, and things like that. So it's just not a very easy Thing to do.
Because… like, if we're a vendor, you know, like, I work for Dynatrace, if we're testing the bundle size of Dynatrace, we test with the bundler configuration that we use, so we know exactly what to target. But for this.
we don't know what our customers might end up using in the end. I'm not saying it's not worth doing, I'm just saying there's a lot of challenges involved.
Marc Pichler (Dynatrace) 00:56:42 I'm really, All of that specifically, there's… I think I've seen some repos that still do bundle size tests, But most of them, they just bundle up their packages by default anyway, which we currently don't do. We have all the fires in there.
So they used that as a baseline.
I'm not sure if that would be something that's interesting for us as well.
Jan Peer 00:57:20 I mean, we do it at Sentry.
And we use, Size limits the package, and this generates basically a file where all the bundles are Are in?
And then you just stay which limit you have.
And if this bonus increases, then… basically the PR… It's getting blocked.
Which brings all the challenges, because you have to update that, because you add more features.
So… Right.
Marc Pichler (Dynatrace) 00:57:53 I was about to say, that's, that sounds.
Jan Peer 00:57:56 That's true.
Marc Pichler (Dynatrace) 00:57:58 Something that needs to be updated quite often if you have a package that adds a lot of features constantly.
Yeah, one thing that I've also seen is, I just opened it right here, there's this bundle analysis feature in CodeCoff, which we already use, which might be interesting for that sort of thing.
If it's not for, like, actually having a check.
Then, at least for tracking it over time.
Because.
Jan Peer 00:58:27 No, that's the silly.
Marc Pichler (Dynatrace) 00:58:28 RSOP have for to at least know.
Have an easy way to look up what the size is, so that when we see something.
That's a lot to the size, then we can go in and figure out which commit that was.
So maybe that could also be a first step.
Word stint.
Jan Peer 00:58:54 Yeah.
But I think I don't have access to cold cough, too.
Do anything, right?
Since you said you were using it already.
Marc Pichler (Dynatrace) 00:59:04 I think you don't have access to that. You might be able to, have, like, read-only access.
I'm not sure if you're an organization member yet.
Jan Peer 00:59:16 No, I'm not.
Marc Pichler (Dynatrace) 00:59:18 Yeah, if you, open an issue on the community repo, I can sponsor you.
Jan Peer 00:59:23 Yeah.
Marc Pichler (Dynatrace) 00:59:24 Find one other sponsor still. So you will need to…
Jan Peer 00:59:29 Yo, Daniel, do you want to be my sponsor?
Marc Pichler (Dynatrace) 00:59:32 I need to be from different companies, I think.
Jan Peer 00:59:35 Oh, shit, Trent, do you want to be my sponsor? Yeah.
Trent Mick 00:59:40 I'm in.
Daniel Dyla (Dynatrace) 00:59:42 The sponsorship is mostly, I think, just to make sure that People are real people at this point.
Jan Peer 00:59:49 Huh.
I am real.
Daniel Dyla (Dynatrace) 00:59:54 It's getting harder and harder to tell.
Jan Peer 00:59:56 Yeah, true.
We've actually…
Trent Mick 01:00:04 Way back, Nev added a size limits-based test in the Semantic Inventions package, because that was… A targeted work area for reducing The size of bundles for a while.
But there hasn't really been any maintenance on that. Anyway, sorry. You're talking CodeCov, would… would this… could this be something that's put in the benchmarks? Because then we'd have historical… view of… pick a couple scenarios, and do bundles of them, and then just see those over time growing. Now, it's not going to be something that will actively show up in a PR, so it doesn't necessarily help in the day-to-day, but you can go back and see where something went wrong, I don't know.
Marc Pichler (Dynatrace) 01:00:46 I think that could also help.
Trent Mick 01:00:52 Dan, you were gonna say something, but… I saw your mute button.
Daniel Dyla (Dynatrace) 01:00:55 Yeah, I was just gonna say that, historical data would help a lot, and then even something as simple as commenting on the PR Like, the results of the current run, even if it wasn't commenting with history or anything like that.
You know, if… if… as a maintainer or somebody reviewing PR, as you get used to seeing the same number over and over and over and over, I think you would notice if you saw something drastically different, but… Yeah, I… I don't know how.
Marc Pichler (Dynatrace) 01:01:27 I think this is what you mentioned, Jan, right? The size limit.
action.
But it does exactly… or… It does something similar, where it just says.
like, how the size increased. I don't know how it retains state.
Daniel Dyla (Dynatrace) 01:01:44 It doesn't necessarily need to. You could just run on the main branch and run on the PR branch.
Marc Pichler (Dynatrace) 01:01:50 Yeah, right.
That works.
Jan Peer 01:01:52 Yeah, but the state is stored in a file.
But… Oh yeah, maybe…
Marc Pichler (Dynatrace) 01:02:07 I think it just compares… Maybe from the run from…
Jan Peer 01:02:12 It would be.
Marc Pichler (Dynatrace) 01:02:13 Main project.
I also haven't checked. Well, it would make sense to… For it to just obtain whatever is latest on the main branch.
And, like, read that from the check somehow.
It is somewhat possible.
Anyway, I think we are out of time for today, anyway.
Let's… Look into the… the tests, and then, we can also, during that or after that, look into some… some bundle size, Trekking.
I think it doesn't have to be perfect to start out with.
Adjusted, we have something to have a rough estimate of what the size of these packages is, could already be helpful.
Alright.
Thank you, everybody, for joining.
Have a nice week, and see you next week.
Trent Mick 01:03:20 X.
Jan Peer 01:03:20 Bye.
David Luna Bistuer 01:03:21 Bye.
