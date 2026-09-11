SIG: Browser SIG
Date: 2026-09-10
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**maxime quentin** 02:14 Hello?
**David Luna Bistuer** 02:15 my team… Afternoon is for you, or morning?
**maxime quentin** 02:22 Yeah, no afternoon.
**David Luna Bistuer** 02:23 Afternoon, okay.
Where are you, where are you located?
**maxime quentin** 02:28 Based in, Sozo, France, close to the Alps.
**David Luna Bistuer** 02:32 Okay.
Oh yeah, I met.
**maxime quentin** 02:35 You're based in Barcelona?
**David Luna Bistuer** 02:36 Barcelona. Barcelona, so it's afternoon for me. Bryan? Good morning, afternoon. We were discussing about time zones.
Oh, good morning.
**Bryan Atkinson** 02:46 Good morning.
Available.
**David Luna Bistuer** 02:49 Okay.
Okay, let's wait one more minute and see… If someone else is going to join.
And then we can… Sorry.
That's me trying to Let's, let's fix that. Okay, thank you.
Okay.
Wolfgang.
**Wolfgang Therrien (Hound Technology Inc. dba Honeycomb)** 04:05 Hello, hello.
**David Luna Bistuer** 04:06 Yeah, put your topics on the agenda, you have some?
Okay.
Okay, today I'm going to… I'm going to be the host.
Okay, Jared, or… Martin couldn't… couldn't make it, so I'll be here. So… Okay, first topic is mine. I'll start with this, Small… this… well, not a small PR, it's a big PR, but basically what it does… let me share my screen.
And this… yeah, this one. Okay.
So, basically, that's a heads up, and I want your opinion on that. As you see, I got already approval from the… from some people from the JavaScript SIG.
Basically. I think that we have already embroidered, an issue.
Okay, but there was the idea to move the webcommon package, but basically this is something different, so… the goal from this RSCP SIG is, like, they want to deprecate and actually remove from the new measure version, the… the new major ZK aviation that they are doing, they want to release at the end of this month.
the SDK 3.0. They're going to release SDKs for metrics, logs and traces. And one of the things that they did was a cleanup from the SDK trace packages. We had 3 different packages, so we have the SDK trace page.
SDK Trace Note and SDK Trace Web.
Basically, the difference was, from the base.
the Note on web, they have a specific Tracer provider that had a register method to do some things on the fly, like registering accountants manager, the default ones, and this kind of stuff, but also the web… the SDK TraceWeb had some utilities, functions, that were used by the Feds and HHR in some editions.
What I want to do in this major version is that to… they are already deprecating these packages. They were going to… there's going to be just only one SDK-traced package, period? No.
No suffixes at all?
And they want to remove the rest of them, okay? They want just to erase them.
This means that, okay, the dependencies that, fetch instrumentation and XHL instrumentation, I want to be missing. So, that's… Kind of a… a way of keeping the code there, okay? So it's moving from the… that package, SDK trace web, to WebCommon, we're moving these utils, so… and the changes that it's doing is, like, okay, we're changing the fetch instrumentation to import, instead of importing the utils from the SDK package, from WebCommon, okay?
My opinion, XOT makes a bit of… makes sense, because These utility functions are not.
SDK components.
So Webcommon, at least, it's an existing package, it's going to… although there is a plan to be depicated, but it's going to be maintained for some time. So, it's just moving the code there, and so… Okay, so… Just a heads up.
Okay, that's the idea. If you are… and that's kind of the whole plan of TSK 3.0.
It's not a strong, you know, it's not a strong will for the… for the JavaScript.
SIG.
So if you see something that it's, you know, that it's way wrong, and it's better to keep those SDK packages there, just put it in the PR.
And we can… we can discuss… I can discuss with the… with the Browser SIG next week, okay?
**maxime quentin** 09:19 Thank you.
**David Luna Bistuer** 09:20 Just a heads up of that. Sorry to take a long time.
But I wanted to explain the whole context, okay?
**maxime quentin** 09:26 Try to have a look, I might miss a bit of context, but I will make my best to, to review it if I have any inputs, but…
**David Luna Bistuer** 09:38 Okay, any comments, questions, whatever, you put it there so it gets registered, and then we can keep track of it. Not me, but there are other… I involved other maintainers, like Mark, that approved the PR, and also Trent.
Those are maintenance from the code repo, and they are also keeping track of these issues. So anything that you want to share, or discuss, or any concern that you have, just put it there.
**maxime quentin** 10:02 Yeah, I remember, like, merging one smaller library out of the GS.
So yeah, I really understand the need of moving from… on something we have more control over.
Makes sense.
**David Luna Bistuer** 10:17 Okay.
**maxime quentin** 10:18 Okay.
**David Luna Bistuer** 10:19 so that was me, next is Bryan.
This.
**Bryan Atkinson** 10:24 Yeah, why don't… I was… Alright, I was… I was hoping to talk about, sampling a little bit here.
We… so, like, we're at Firebase, we're trying to adopt these OpenTelemetry SDKs.
And semantic conventions and so on for the browser.
One area where I've been a little confused by is sampling, and so I know, like, this core OpenTelemetry sampling docs say, you know, vendors, you know, sort of do sampling separately.
Each has their, kind of, their own way of implementing things.
But to me, it seems like for the browser, sampling is a pretty important thing.
feature, and I know, you know, trace, there's trace samplers and set up and so on.
I found, and I dropped a link to it in the… The… the agenda doc there, but there's… in, sort of, the root config object in OpenTelemetry Browser, there's a mention of a sample rate. And it's commented out, and it says, should be discussed in the Browser SIG. And I'm wondering, I can't find any context around, you know, if… has that discussion happened?
Around, like, browser level sample, or browser sampling, and whether or not or how it sort of integrates with, with, interacts between, you know, spans and logs and so on.
Or is this sort of just kind of an undefined area so far?
**Wolfgang Therrien (Hound Technology Inc. dba Honeycomb)** 11:53 Yeah, David, you can definitely, you know, jump in and correct me if I'm speaking any mistruths. I think sampling has been sort of recognized as an important problem, but not one that we've necessarily decided to tackle head-on just yet, because we're trying to get a lot of the other sort of foundational stuff up and working first. I think the major issues right now that we see folks having with sampling, especially with, you know, different head sampling techniques is that they will want to, in their product or in their telemetry, see all of the related spans, traces, logs, etc, for a given session, for a given user, for some correlated attribute, right? But if you're just doing head sampling, that Becomes very, very complicated to do that.
And that's where, you know, you can see folks coming up with their own sort of solutions here to make sure that they are sending all of the things that they need.
And, we see a lot of folks, at least at Honeycomb, reaching for collectors, or collector-like things. Like, we have a thing called refinery, which is, something that looks a lot like a collector, in order to do tail-based sampling.
**maxime quentin** 13:14 I agree.
**Wolfgang Therrien (Hound Technology Inc. dba Honeycomb)** 13:14 But I think it's an area that we would be very excited to, you know, more concretely define, especially once we get more… a little bit more further along with some of the more basic foundational things, like being able to properly measure, like, page load and things like that.
**Bryan Atkinson** 13:30 Right?
**Wolfgang Therrien (Hound Technology Inc. dba Honeycomb)** 13:32 Okay. But yeah, I could definitely imagine us having a handful of, like, browser-specific samplers that would allow us to sample on session, so that at least then, if we are emitting things from a web SDK, we can make sure that we are emitting all of the you know, signals that have a specific session ID attached, which gets into some other sort of asterisk, situations where, like, are you stamping session ID on all of the relevant samples, or are you relying on a parent-child relationship? How do you handle cross-service boundaries? All of that stuff gets very, needs a lot of deep thought. So that's sort of, I think, the high-level, sort of.
Problem space that we're thinking… that we're working in.
**Bryan Atkinson** 14:16 Okay.
Okay, so you'd think it'd be premature to start trying… because, I mean, that is exactly the thought process we were having here also, which is, like, do we need a sampling rate applied on, like, you know, attached to the session, right, so that, you know, you get consistent you know, you're doing head sampling, but you get it consistently based on, you know, for all of your signals, based on the session ID.
And the rate.
**Wolfgang Therrien (Hound Technology Inc. dba Honeycomb)** 14:42 Yeah, and I think that's where, like… it's not guaranteed, right? Because you could have a lot of really shallow sessions that have very few signals in it, but then you could also have a bunch of sessions that have a lot of signals in it, right? So how do you deal with those sorts of things? And those are sort of, the things that I think we need to work through defining. And so, I mean, if you have ideas on that, I'm sure we would love to read through them.
But I think it's just one of those things where… folks just haven't gotten there yet, even though we recognize it as an issue. So, but yeah, I mean, I'm… I'm not gonna speak for everyone, but if you have, some… if you want to start putting down thoughts on that, I could see… I could see those thoughts being… being welcome, even if, It's, you know, something that we have to prioritize against all the other things that we want to do.
Does that feel… does that feel, like, right, David? Or… or… I see that you've got your hand up, Max.
**maxime quentin** 15:40 Yeah, so I was just, like, totally agreeing with you in the fact that, like, you want to sample per session, or per page, or per whatever. You probably don't want to have a flat 10% sampling rate, and you cut whatever is not in your 10%.
And to me, my vision is, like, until we have a clear understanding of entities, on how we want to group stuff together, how we want to aggregate signals together with entities, it would be complex to talk about Like, something.
**Bryan Atkinson** 16:16 Okay, yeah. Yeah, that makes sense. Alright, thank you.
**David Luna Bistuer** 16:23 Okay, alright, and then, finally, it's me.
Let me share again. So that, that was kind of a topic that I brought last week.
So there's a small… it's a small PR bike, basically, that… that does resistant instrumentations, but I put kind of a… highlight that registering instrumentations, at least from the instrumentation package, what it does is actually activates everything. So it just applies the patch and enables it.
Regardless of the configuration. So… Kind of, was kind of a bit misleading.
or at least my point of view as a user, I think it's been misleading, so you are configuring an instrumentation to be disabled.
Maybe you will enable it later, because you have a reference, and you have the enable API to enable it or disable it.
Okay?
But then registering Zoom additions, what it does is, like, it's enabled everything, so you get all the… all the Zoom additions working.
I'm thinking in the use case that I want to control traffic.
And I know maybe that some instrumentation is, like, making a lot of traffic, and they never want to disable it, but they have… still have telemetry.
So that was kind of the point. My discussion, basically, didn't have any follow-ups. Kind of, I was wondering, maybe… okay, we are not many people here, but they… I was wondering, have your opinion on what maybe we can just, you know.
The SIG is experimental.
So, I was thinking that maybe you can just move on, merge that PR, and say, okay, maybe in the future that behavior is going to change.
Okay, we agree, so finally we agree on saying, okay, no, the configuration rules over everything, and you can start an SDK with some… instrumentations being disabled from the… from the get-go. I know that there is a work from Jared that is kind of, redefining the API for… for instrumentations.
Because we don't want to depend on that package.
So maybe that's some conversation that we can have later. But if… I wonder… I was wondering that, if that's okay to have this behavior right now, and maybe just, you know, in a new release.
Which is… we are still in the experimental phase, we can say, hey, that's breaking.
So, now they're disabled, it's going to work this way.
**Wolfgang Therrien (Hound Technology Inc. dba Honeycomb)** 18:41 Yeah, I think, we, in our… in the Honeycomb web SDK wrapper, we do have this sort of configuration model where you can just pass it an array of instrumentation and Customers really seem to like that pattern. It takes a lot of the cognitive load and a lot of the boilerplate off their plates, but but yeah, I'll review that PR and I'll chime in on that.
I think it looks… I think it looks really reasonable.
**David Luna Bistuer** 19:12 Okay then, any more last-minute topics?
**maxime quentin** 19:16 Regarding the instrumentation API, I understand that you want to load it and maybe disable it later?
But can we have an instrument manager that does it, instead of having a… To have individual instrumentation, start and stop, or… maybe should we, maybe Jared has… Like, option for having a better, like, wrapping around the instrumentation, so we can, like… Differentiate, like, the instantiation of the… of the instrumentation and the starting stop.
I mean, if it's blocking, maybe I'm totally up, like, pushing for a simple solution first, and go for… For a refiner one later, but yeah, I was just wondering… how other SDKs are doing, like.
Do they have, like, completely different, kind of, instrumentation behaviors, because they are in Android, or they are in whatever, and then it doesn't work the same in terms of referencing and everything, but Is there a pattern between other SDKs, or are all SDKs doing their own thing?
**David Luna Bistuer** 20:35 Well, Intact, okay, I could talk about… In Node.js, at least in Elastic, what we have in our distribution on Node.js, we are just following what. But in Note, I don't know, maybe it makes sense to enable everything that you have.
So, maybe, let me rephrase a little bit. So, in Node.js, you can… you can do is, like, you have… you can set some bars to say what are the active instrumentations, and those are the instrumentations that have been loaded. So everything that it's load… every instrumentation that it's loaded.
It's activated.
**maxime quentin** 21:13 Okay.
**David Luna Bistuer** 21:14 does the patching, it does enabling. But it makes sense because you, imperatively, you… by configuration, you say, okay, I want this, this, this, and that.
Okay, that's different in our case, but then resistor instrumentations, you just find this list of instrumentations, and it enables everything. So, okay, that's fine, so it's kind of the behavior you expect. In Browser is different, so you have everything bundled already, so you ship everything, all the instrumentations are there, then you may want to enable one or the other, okay? We don't, we don't, I don't know, we don't have a mechanism right now to just ship it, a subset of instrumentations right now, maybe in the future.
We'll see. But, you know, right now, it's… that's kind of the main point. So that kind of was not an issue, and there was no discussion, at least in… at least in Ontarland.
Okay, I cannot talk for other frameworks, I don't know for other agents.
**Wolfgang Therrien (Hound Technology Inc. dba Honeycomb)** 22:06 I, if I remember correctly, the Android one has a similar, like, like, configuration, you know, sort of pattern where you can specify, your instrumentations at build time, and you can be like, hey, these are the… if it finds those instrumentations, it… you know, we'll load them up, but that's, I think, more of a paradigm of the language, right? You know, that Kotlin, Java, sort of ecosystem. I can't remember what Swift does off the top of my head, but I think it's similar because, that is also a very different sort of build time.
sort of, sort of universe.
I… I don't see any harm in, sort of, experimenting with this, Because one of the things that we do hear from customers, they want the ability to turn on and off instrumentation, as, you know, you know.
perhaps sometimes based on, you know, like, a feature flag or something, and like, hey, this class of users, like, needs more instrumentation, and they want to have more control rods for controlling the volume of telemetry, which is maybe not quite the same need as, like, in a Node.js server or something, right? Because you might not have quite the same volume, so… It's definitely an interesting space to sort of operate in.
**maxime quentin** 23:31 That makes sense.
**Wolfgang Therrien (Hound Technology Inc. dba Honeycomb)** 23:34 I would like to understand a little bit more about, like, what, instead of, like, sort of holding on to, like, individual instrumentations and being, like, enable and disable them, like, what a, like, what that sort of manager interface, like, what problem that would solve for us? Or if it's just sort of, like, if that gives us a little bit more flexibility in the future, like, what is… what's your thinking there in terms of, like, why… why we might want to introduce that layer of abstraction and that little bit of complexity? Because it's just not… it's not… Immediately obvious to me, like, what that might… What that layer might buy us.
**maxime quentin** 24:10 I mean, to me, like, the… I like, I would say, like, customers just having all instrumentation by default, and if they want to, share a pick and have a… More control about the instrumentation, when they start, when they stop.
I feel it's better to have, the same, Same API for all instrumentation.
Like, either in a manager, is there… is there… is there in a… I don't know how, but having some kind of API that's, It's all instrumentation and have the same, like… like, all instrumentation would have the same lifecycle.
Do you want to, kind of, have your manager starting your instrumentation when your page is ready, or whatever, or stuff like that, you know?
**Wolfgang Therrien (Hound Technology Inc. dba Honeycomb)** 24:56 Mmm, because…
**maxime quentin** 24:57 being on top of just having, like, a, hey, I have clicked on this button, and then it's on or off.
So, yeah, or, like, maybe you have, let's say, one instrumentation that takes a lot of CPU, or whatever, and then you want to… to debounce it, or stuff like that.
But it was just a suggestion, I think we need to go around.
**Wolfgang Therrien (Hound Technology Inc. dba Honeycomb)** 25:18 Yeah.
**David Luna Bistuer** 25:20 Yeah, just not enable or disable only, but actually… Okay, we have configurations, so the simulations have configurations that are functions, so we cannot pass functions, but… what is a raw value, like a string, or a list of… or a number, or something like that, you can make it. So, thinking about the situation, let's pretend that we have a fetch instrumentation.
And it turns out that the front-end team, I just, it uses a… it uses a new library, maybe it's using something for advertising, and it's doing a lot of fetch requests. And that's, you know.
to a specific URL, the advertiser endpoint, and this increases the traffic a lot. So maybe I want that manager to, I want to somehow to just collect an update of the configuration and say, okay, you know, ignore that URL, So then I can just, you know, keep, you know, keep the fetch instrumentation working, but ignoring that traffic, because it's just giving me no… No… no value, But, you know, but I still want to get the spans from the fetch requester and into my backend.
So, yeah, kind of short. I was thinking, kind of, the conversation started, or at least I started the conversation with that idea in that idea in mind. We don't have… right now in Browser, Some sort of, kind of, a… open, where there is this protocol from, Central for Configuration for getting a configuration from a server.
But, you know, to be ready for that. So you have kind of a disk layer of, okay, it's more complex, you have this layer, but it's something that could manage in, you know, can… can… yeah, manage the instrumentation somehow and say, okay, here's your new configuration, you enable, you disable, something like that, and maybe you don't… I don't know.
Maybe even someone can do their own, you know, endpoint for configurations, and they can have their own dashboard with configurations for that. That, you know, I'm not talking about vendor stuff, like Datadog or Elastic or whatever, but even, you know, you and the front end, you want to have something that, you know, you enable, as Maxim said, something for some segment of your Of your users, feature flag, or whatever.
**Wolfgang Therrien (Hound Technology Inc. dba Honeycomb)** 27:38 Yep, that makes sense. Yeah, and so sort of leaning into, you know, getting ready for that, like.
dynamic config, or, like, even, like, remote static config type, type use cases. That makes a lot of sense. Cool.
**David Luna Bistuer** 28:00 Okay then, 2 minutes left, but if there is something quick… You can… you can slice in if you want.
**maxime quentin** 28:09 MV.
**David Luna Bistuer** 28:10 No?
Okay, Bryan, about context, if you want to keep going the conversation, you can start an issue.
In the browser repo, and we can have the conversation there, and we can keep track of it, if you like.
**Bryan Atkinson** 28:23 Awesome, man. Sounds great, thank you.
**David Luna Bistuer** 28:25 Okay. Yeah.
Good.
**Wolfgang Therrien (Hound Technology Inc. dba Honeycomb)** 28:27 Alright.
**David Luna Bistuer** 28:28 Okay then, so…
**maxime quentin** 28:29 flavor, and…
**David Luna Bistuer** 28:30 See you next week!
**Wolfgang Therrien (Hound Technology Inc. dba Honeycomb)** 28:31 See you. Thanks so much out.
