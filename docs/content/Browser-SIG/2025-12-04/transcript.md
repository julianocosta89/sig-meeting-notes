SIG: Browser SIG
Date: 2025-12-04
Duration: 29 minutes
============================================================

## Zoom Recording Transcript

**Ted Young** 00:43 Yellow, yellow.
**Martin Kuba** 00:46 Hi, Ted. How are you?
**Ted Young** 00:48 Doing alright. Doing alright. Y'all doing?
**Benoît Zugmeyer** 00:52 Hello.
**Ted Young** 00:57 we've… Fallen into December.
The month where, technically, we're still working, and yet somehow nothing gets done.
**Martin Kuba** 01:07 Yeah, I was just, thinking that there's probably not gonna be much happening in December.
**Ted Young** 01:14 Yeah.
Yep.
Actually, that's maybe a reminder…
**Joaquín Díaz** 01:36 Hey, how are you?
**Ted Young** 01:39 Doing good.
**Martin Kuba** 01:41 Hero Kin.
**Ted Young** 02:28 Cool.
**Marco Schäfer** 02:51 Everyone…
**Martin Kuba** 02:54 Hi, Marco.
**Ted Young** 03:15 Cool.
Well, feel free to add things to the agenda if you've got them.
I've been pretty out of the loop. It was Thanksgiving in the U.S. last week, and this week has just been…
Like, a total blizzard. And I'm in Japan next week. So…
That's why I was kind of like, December's here.
**Martin Kuba** 04:05 Well, I have, I have the first, topic.
**Ted Young** 04:09 Kick us off.
**Martin Kuba** 04:11 So, this is about the navigation instrumentation.
I think it's very close to being done.
I would like to approve it and merge it.
Abinad's been working on it for a long time, and he's been doing a great job, so I think it's very close. The one thing that I wanted to ask this group is…
Part of the PR is sanitizing URLs.
And I wanted to just… just see, like, if people have opinions about whether this should be…
Enabled by default.
Or if it should be optional.
So, Abinad added the option for users in the configuration to supply a custom function.
So that you can, you know, users could write their own rules, or…
For sanitizing URLs, but there's a default function that's enabled, like, if you don't supply the function, then the instrumentation uses the default implementation.
I added a link there. I mean, I think it's good to have it. I guess my only question is, should it be on by default? And the reason I'm wondering about that is, once it's default, we can't…
You know, turning it off will be a braking change.
And…
If it's by default, if it's on by default, then we have to maintain it, basically. Like, we'll have… we'll probably have a lot of questions about, or a lot of issues about… I'm expecting.
So I was wondering if anyone had any thoughts on this.
**Ted Young** 05:53 What's the behavior of other systems?
Like, if you install New Relic or Pharaoh or something, by default, does it scrub stuff? It seems like a good default, to be like… by default, we're going to scrub your stuff, and if you don't want that, you can turn it off.
**Benoît Zugmeyer** 06:16 We don't.
**Ted Young** 06:18 You don' Yeah.
**Benoît Zugmeyer** 06:23 But it caused, issues, honestly, so I think…
Having a default sanitizer is a good idea.
One thing, I'm thinking is…
if there is other places where we can have URLs, like, if there is other events, like, for example, resources.
Well, we have, uRLs, we should be able to sanitize it in the same way.
So… Yeah. Either we pass the same function to both instrumentations, or maybe we can have a…
A sanitization concept.
I don't know.
**Wolfgang Therrien** 07:15 I was having a… a similar thought. I think it's a good… a good default, I think.
It also feels like it could be something that happens, like, on a…
you know, as the signal is leaving the system, right? There could be a set of, like, URL-based attributes, or something like that that just say, any of these attributes will get run through this sanitizer, and therefore will not make it to your system. And that could be
That could be a way to approach this, and that sort of decouples, what the responsibility of the… this instrumentation is versus that sanitization as sort of, like, a separate feature.
It's not to say that we can't do this now and then move it there, but it's just sort of, like, what is the burden of that maintenance cost in that effort?
**Martin Kuba** 08:08 Yeah, as far as we… as far as I know, like, we don't do anything like that anywhere else in hotel instrumentations right now. We have, like, the fetch and XHR instrumentations, they don't do that.
I also imagined, like, that the URL
probably should be, at some point, a resource attribute. Like, it should be, like, every…
signal should be… should have that, be associated with the URL.
So, like, you would probably want it there as well.
So, like, yeah, it does seem… it does feel like more of a broad… feature.
**Wolfgang Therrien** 08:41 and…
And so, like, for me, that's, like, indicating that we probably should include it, and we should include it as sort of, like, either an opt-in so we don't incur the maintenance burden of an enabled default, but still provide that functionality, because we're not going to build that
you know, sanitization feature hold cloth today, but this is still very useful for folks in this particular instance.
So I think a lot of times what I've seen folks do is they're like, hey, here's this thing, and in the example usage, it's like, and we recommend using this sanitizing, like, opt-in feature.
So it kind of becomes sort of a documented default rather than a programmatic default, and…
That's a lesser burden for us to maintain.
**Martin Kuba** 09:27 So I'm… I'm all for that. I think I… my…
I think we definitely should include it. An opt-in sounds good to me.
I just wanted to see if it should be… default.
On enabled by default.
Yeah.
**Joaquín Díaz** 09:45 Yeah, it wasn't the…
enable a default team, because I think, like, once you start sending data, it's too late, and you are already sending credentials to somewhere that you don't want to.
But I think I also agree with, Wolf again about adding, like, a documentation default, like, if we are very explicit on the documentation that we say you should do this, but…
by default, the call doesn't do it, and I think that makes sense.
**Ted Young** 10:13 Yeah, I mean, we kind of want… ideally, OpenTelemetry is zero config out of the box, right? Like, you turn it on, and it should be ready to roll in production the way we think you should roll it in production.
It shouldn't be, like, turn OTEL on, and then have to configure a bunch of instrumentation, and turn off these 5 packages, because they're too noisy. We're not perfect, right? It does, like, even trying to get it balanced, I feel like people still end up with noise and stuff they have to futz with.
But definitely the worst thing in OpenTelemetry is, like, having to configure instrumentation packages. Maybe in the future, we can figure out a good way for configuration packages to be configured through the config file and stuff like that, so that might make life better, but it's kind of like a death of a thousand
paper cuts, because also, like, if it's instrumentation-level config, it's like, how do you… do you start making environment variables? Like, where do you start putting this stuff?
Obviously, for the browser, it's a little bit different, talking a little bit generically.
So… It's kind of nice if…
But on the flip side, something we've said for a long time in OpenTelemetry is that we don't make the collector a required component.
sometimes in our design, we're like, well, if we can just assume everyone's running a collector, then we can move all this stuff out of the SDK and into the collector.
But we tend to say, like, well, we can't assume people are running a collector, right? They may want to run nothing, or they may want to run some third-party thing.
We don't want OTEL to be this one
as soon as you want to grab one piece, will you have to grab all of it? But it might be a little bit different for the browser, but maybe not. Like, we definitely want to say you need to run some kind of proxy, you know, to run OTEL in the browser, and you don't want to just stick the collector
out there, you know, so we have to come up with some kind of, like, public proxy solution, whether it's the collector or the collector sitting behind NGINX or something.
We need to tell people what to use. But it's an interesting question of whether that's required or not.
And if we start saying, like, hey, we're gonna move processing power and, like, stuff out of the browser, and that's fine, because we're gonna assume you're running this, like, gateway, so all of the scrubbing and, like, everything else we're gonna do in this gateway.
We would start to be… it feels a bit like we're starting to say, you kind of have to run this thing…
Or you're gonna get, like… Raw data and… and have to, like, figure something out on your own.
So for those reasons, it seems, like, valuable to always have this thing at least as an option.
And it seems sort of like, if it's an option, do we want it to just be, like, the one way that it works, rather than have, like.
in JavaScript and in Go, trying to main two different things that maybe try to do the same thing.
So…
I don't know, I'm a little torn, basically. It seems like the collector or a gateway would be a great way to do this work and not have to do the work in the browser, but…
You know, it means we're firehosing sloppy data if you don't run that thing.
Given that we don't have this component at all, and we're kind of, like, scoped to, like, not touching that in this phase of the browser work, trying to say, like, let's just stay away from the collector and everything, you know?
I would suggest, maybe we do this, maybe leave it off by default.
Because if we did have to, like, surprise everyone by changing the default later, probably surprising people by turning this thing on is better than surprising them by turning it off.
Right. Like, that would just be irritating if we turned it on, but it's a little more defensible than we, like…
took away all the PII and, like…
cardinality scrubbing. So maybe that's… we build it, we leave it off by default.
But we make it super clear in our docs.
maybe in our docs, the config blocks include it on by default or something, right? Like, explicitly include the turn it on in the docs that we give people.
**Wolfgang Therrien** 14:47 Yeah, I think… I think that makes a lot of sense for now.
I don't see any, like… it's a little bit more of a configuration burden, but I think that prevents us from
having to deal with a lot more change management burden, down the road. Should we… should we choose something… something else?
**Ted Young** 15:07 Yeah.
**Jared Freeze** 15:10 I had a question about, is there a concept of, like, limiting logs?
In, like, hotel as a general idea.
Like, any sort of limits on, like, any of the data? Like, is that outlined?
**Ted Young** 15:24 You mean, like, payload size limits and things like that?
**Jared Freeze** 15:27 Hmm.
**Ted Young** 15:27 That is a good question.
I think there are some places where we have defined
this stuff, but I don't know about logs.
It'd be worth checking the spec, that's where it would be.
**Jared Freeze** 15:41 I just looked, I need to study it more. We have this concept, in… in the SDK that we work on, and so it seems like, sort of, a nice analog here of, like, do you… because we just catch everything on the way out. It's like, do we catch everything on the way out in this way as well?
So I like that idea. I guess I'm sort of torn on the enabled by default, but… Yeah.
**Ted Young** 16:06 Yeah. If I were to guess what we did around
rules around size limits and stuff like that. If I were to guess, probably what we did was we told people, like, suggestions, but didn't set a hard limit. We said, like, probably don't stick more than 512K in span attributes, or something like that, at some point to people, but didn't actually, like.
Cap it anywhere in our system.
Because what might be a good limit for a Java app might be different for the browser, for the collector, for who knows what.
**Martin Kuba** 16:46 So, one more thing that I want to point and say about this is that we also, in the past.
Considered adding…
like, a Web SDK package, which would combine all the, you know, configure everything for you, provide a better, like, configuration interface.
better APIs, and better, like, some built-in defaults.
So, we could have all those recommended default… defaults on in that package, but the instrumentation itself would be… would include it only if it's configured that way.
You could handle it that way, too.
**Jared Freeze** 17:23 So, I mentioned that before, I think… I think Dan's on the call, but he said that's not really the hotel way.
**Daniel Dyla (Dynatrace)** 17:30 I am on the call. I'm sorry, what's not the hotel way? I have to admit, I was a little bit distracted. I was looking up…
**Jared Freeze** 17:38 No, you're fine. Yeah, I'm interested in that as well. The, like, having a convenience method that sort of does auto-magic to, like, pull in good defaults.
**Daniel Dyla (Dynatrace)** 17:50 I don't know that I would say that's not the hotel way. I would say that we're not very good at that. They don't exist. I would say they don't exist, not necessarily they shouldn't exist.
If I was going to define what the hotel way is from, like, the way that
we want it to be and hope it is, would be we provide primitives that allow you to do whatever you want to do, whether we think it makes sense or not, and then build,
you know, I guess convenience wrappers, or whatever you want to call…
Around those to encourage what we consider to be the happy path.
Realistically, we're better at the first part than the second part.
There are a lot of extremely confusing APIs that are really, really powerful.
But difficult to use.
**Ted Young** 18:46 Yeah.
This is something we'd like to improve with config files, to use the existence of config files as kind of an excuse to revisit initialization, and to be like, for languages that have…
are still just a kind of, like, you copy-paste all the lower-level provider primitives and exporters and everything in a big way? You know, is there a way to just be a little bit more like, new SDK, and you get a whole bunch of defaults out of the box, and…
The different SIGs are all pretty different when it comes to, like, that level of convenience right now.
**Daniel Dyla (Dynatrace)** 19:23 Well, yeah, it was never specified to begin with, so every SIG, you know.
you have to be able to start up the SDK somehow, or it's not useful, but the startup process was never defined by the spec, so every SIG came up with their own startup process, and…
Yeah, it's kind of a mess.
**Ted Young** 19:45 It kind of had to be that way, because, you know, it's like Node.js versus Go versus Java, they all have, like.
**Wolfgang Therrien** 19:51 Yeah.
**Ted Young** 19:52 really weird things. But also, we were like, in the future, we'll define this convenience stuff, and it's, like, years later, and we're like, we're gonna get to that at some point.
So, we really need to get to that now, as part of, like, cleaning everything up. That's sort of, like, the next phase of OTEL.
I don't know what that means for the browser sig, though. Like…
**Jared Freeze** 20:12 I mean, I envisioned it like you npm install OTel slash browser, and it's just, like, this nice entry point, which doesn't have to do any version management, doesn't have to do… you know, it'd be, like, V1 or V2 or whatever, and then you don't have to really understand what's going on underneath, unless you really want to get into that. We could keep some
dependencies, people really wanted to do that, but… Yup.
**Daniel Dyla (Dynatrace)** 20:36 Yeah, now I… now I know what you were referring to when… when I said that's not the OTEL way. What you're referring to is a single package that encapsulates the API and the SDK all together, right?
Yeah, I would… again, I would say that there's no reason that that shouldn't exist. It is imperative that you are able to use them separately. So, if…
if you used, like, OpenTelemetry slash browser, and, you know, some other, part of your application used the API directly, there's, you know, that should be linked.
But… It shouldn't be the only way to use it in the browser.
**Ted Young** 21:21 Yeah.
the iOS SIG has actually been in a bit of a fracas with Datadog over this, because of the… again, because in Swift, the way packaging works, reasons, maybe not perfect reasons, there's, like, reasons for why they felt it would be better to
to ship them both in the same package, the API and the SDK. But sure enough, we have a vendor showing up, and they're being like, we want to use your API and your instrumentation, but we have our own implementation that we want to use. We don't want to use your thing.
And, like, the fact that they're both in the same package is creating, like, a ton of bloat for us.
So we do need to be able to let people
You know, run their own implementation?
But I totally think this is something I'd like to do with the SIGs in general, is not… not dictate how it works, but just go to each one and be like, hey, if we were to clean up install, if there was, like… now that we have the primitives, if we wanted to, like, give people something else based off of the primitives that they could just go around if they didn't want.
That would be, like, super helpful in, like, most languages.
Certainly browser.
I mean, browser's gonna be, like, kind of a special child anyways, so… Yeah.
It's just a question of what that looks like. I would like us to ideally have one convenient way we give people, not like…
3 or 4 half-convenient ways.
But getting back to your point, Martin, around, like.
There's another question, even if this all lives in the browser, of, like, do we do this kind of, like, work in the instrumentation?
Or do we do it as, like, an SDK processor? I assume it's more efficient to do it in the instrumentation, but then, like other people were saying, if you want to be applying the same
Kind of thing everywhere, and configuring everywhere.
like…
It seems like that would work better if it was more like an SDK plugin that was like a scrubber.
So, I don't know.
**Martin Kuba** 23:43 So I think for this, for my original question, I would say, like, let's just make it opt-in for now. We can always, like, change… if we change our…
You don't mind later, we can… we can make it…
We can change that, but for now, to merge this PR, I think we can just make it up opt-in.
I've been at a, I'm not sure if you followed the whole discussion, but.
**Abinet Debele** 24:08 Yeah, I joined late, yeah, I've, had,
Yeah, some of the ideas, yeah. So, yeah, the current implementation is just… they have… the customer has to pass… I mean, the user has to pass the…
sanitize URL function. Otherwise, if they don't pass anything, it will be used default sanitizer.
So, you're saying that default should not be…
a must, like, it should be… they should opt in for that one, right? So, we should have something, maybe another flag, I don't know if, to just…
Accept… use the default sanitizer or not, or, oh, ow.
**Martin Kuba** 24:49 Yeah, either flag or maybe export the default function, and then document how it would be used.
**Abinet Debele** 24:57 Okay.
Yeah, that makes sense, okay.
**Martin Kuba** 25:07 Okay.
**Ted Young** 25:18 Well, we're running low on time. David, do you wanna…
Let's jump over my stuff. You have an actual issue. Yeah.
Bye, no.
**Trent Mick** 25:34 Oh, the David add-in's done, that was added to the…
**David Luna Bistuer** 25:37 Yeah.
**Trent Mick** 25:38 thing. It… that resolved itself. All the time.
**Ted Young** 25:42 Okay.
**David Luna Bistuer** 25:43 So, sorry.
**Ted Young** 25:47 Jared, you got some stuff you want us to review?
**Jared Freeze** 25:49 Yes, there's a link. You can check it out.
I got some of the new…
I was looking through the CI, trying to figure out, like, what we can do for, importing workflows across
from OpenTelemetry JS and JSContrib.
Not super straightforward, but I'm gonna sort of hack on that. What is there now is just super basic, just like.
NPM run build, run lint, whatever, just to get us started, so…
double files, nothing's blocking, I'll hit up whoever to make them blocking when the time comes.
But just a little safety, and then we have more tickets and issues and things, but, yeah, some small stuff.
**Ted Young** 26:37 Sweet.
I just have, like, a small update. I've been getting more and more disaffected with GitHub projects.
And I've been noticing that the, the collector…
Is using, like, a… they're doing a good combo of, like, pinned issues to bring attention to them.
And then, sub-issues… When you go into one of these.
for, like, the actual work needing to be done. So they're making kind of, like, a tracking issue for some big initiative they have, and then they're making sub-issues to kind of track the work, and this is, like, super limited in, like, what you can do with it, but the flip side is it's, like.
It's pretty obvious to anybody how it works, and it puts all of this information, like, right in users' faces, as opposed to projects where it's, like.
You know.
**Wolfgang Therrien** 27:41 This is helpful, but does anyone look at it? And if anyone did wander in.
**Ted Young** 27:45 Would they really be able to make sense of this thing?
Right?
Versus, like, when people wander into the collector, they can totally make sense of, like, this stuff.
Up at the top.
So…
These are just, like, my thoughts. I might try to reorganize us into something more like this, because we're seeing more SIGs that kind of naturally start to use these tools.
Anyways, that's just my quest to try to get OTEL a little more organized from, like, a backlog perspective. But I might use us as a lab rat and switch to this and see if it's helpful.
But if people have thoughts on… on this stuff, or they're seeing, you know, good patterns out there, let me know.
**Trent Mick** 28:31 I don't work in the collector a whole lot, but I'm just looking at their milestones, and they seem to have a milestone for each release, and it looks like they have a GitHub Action that adds
any closed issue to the next release milestone, and then I'm assuming that they rename that milestone to the release name when they do release. It's kind of nice, because it captures all the issues that were done in that.
And that milestone release kind of automatically, instead of having to go, like, when you're doing your release, back-reference all those issues. So it's kind of neat.
**Ted Young** 29:01 Yeah, that's nifty.
Cool.
Okay.
Well, that's all I got, and we're at time. I'm glad to see stuff, coming along, though.
See you all on the internet.
**Jared Freeze** 29:17 See ya.
**David Luna Bistuer** 29:17 Yeah, that…
